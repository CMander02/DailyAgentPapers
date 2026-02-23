#!/usr/bin/env python3
"""
主入口脚本：获取昨日 arxiv Agent 论文，LLM 评分/摘要，写入 markdown。

用法:
    python scripts/fetch_papers.py                   # 自动获取昨日论文
    python scripts/fetch_papers.py --date 2026-02-22  # 指定日期
"""

import argparse
import os
import sys
import yaml
from datetime import datetime, timedelta

from arxiv_client import build_query, fetch_arxiv_papers, filter_by_date, keyword_filter
from llm_client import score_and_summarize
from markdown_writer import write_paper_file, update_readme, update_papers_json


def load_config(base_dir: str) -> dict:
    """加载 config.yaml"""
    config_path = os.path.join(base_dir, "config.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="Fetch daily arxiv agent papers")
    parser.add_argument("--date", type=str, help="Target date (YYYY-MM-DD), default: yesterday")
    parser.add_argument("--base-dir", type=str, default=None, help="Project root directory")
    parser.add_argument("--dry-run", action="store_true", help="Only fetch and filter, don't call LLM")
    args = parser.parse_args()

    # 确定项目根目录
    base_dir = args.base_dir or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 确定目标日期
    if args.date:
        target_date = args.date
    else:
        # 默认昨天 (UTC)
        yesterday = datetime.utcnow() - timedelta(days=1)
        target_date = yesterday.strftime("%Y-%m-%d")

    print(f"=== DailyAgentPapers ===")
    print(f"目标日期: {target_date}")
    print(f"项目目录: {base_dir}")
    print()

    # 加载配置
    config = load_config(base_dir)
    search_keywords = config.get("search_keywords", [])
    categories = config.get("categories", [])
    filter_keywords = config.get("filter_keywords", [])
    boost_keywords = config.get("boost_keywords", [])
    max_results = config.get("max_results", 200)

    # Step 1: 查询 arxiv API
    print(f"[1/4] 查询 arxiv API (关键词: {len(search_keywords)}, 类别: {len(categories)})...")
    query = build_query(search_keywords, categories)
    all_papers = fetch_arxiv_papers(query, max_results=max_results)
    print(f"  获取到 {len(all_papers)} 篇论文")

    # Step 2: 按日期过滤
    print(f"[2/4] 按日期过滤 ({target_date})...")
    date_filtered = filter_by_date(all_papers, target_date)
    print(f"  日期匹配: {len(date_filtered)} 篇")

    if not date_filtered:
        # 尝试扩大日期范围 (有时 arxiv 更新延迟)
        alt_date = (datetime.strptime(target_date, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
        print(f"  尝试扩展日期 ({alt_date})...")
        date_filtered = filter_by_date(all_papers, alt_date)
        if date_filtered:
            print(f"  使用扩展日期，匹配: {len(date_filtered)} 篇")
            target_date = alt_date

    if not date_filtered:
        print("  没有找到目标日期的论文，退出。")
        sys.exit(0)

    # Step 3: 关键词精筛
    print(f"[3/4] 关键词精筛 (过滤词: {len(filter_keywords)})...")
    filtered = keyword_filter(date_filtered, filter_keywords, boost_keywords)
    print(f"  关键词匹配: {len(filtered)} 篇")

    if not filtered:
        print("  关键词过滤后没有论文，退出。")
        sys.exit(0)

    if args.dry_run:
        print("\n=== Dry Run 结果 ===")
        for p in filtered:
            print(f"  - [{p['arxiv_id']}] {p['title']}")
        print(f"\n共 {len(filtered)} 篇待处理")
        return

    # Step 4: LLM 评分 + 摘要
    print(f"[4/4] LLM 评分与摘要 ({len(filtered)} 篇)...")
    papers_with_results = []
    for i, paper in enumerate(filtered):
        print(f"  [{i+1}/{len(filtered)}] {paper['title'][:60]}...")
        result = score_and_summarize(paper)
        if result:
            print(f"    评分: {result['relevance_score']}/10, 标签: {result['tags']}")
            papers_with_results.append((paper, result))
        else:
            print(f"    跳过 (评分过低或处理失败)")

    if not papers_with_results:
        print("  所有论文评分过低，无输出。")
        sys.exit(0)

    print(f"\n最终收录: {len(papers_with_results)} 篇")

    # 写入文件
    print("\n写入 markdown 文件...")
    for paper, result in papers_with_results:
        filepath = write_paper_file(paper, result, base_dir, target_date)
        print(f"  写入: {filepath}")

    # 更新 README
    print("更新 README.md...")
    update_readme(papers_with_results, base_dir, target_date)

    # 更新 papers.json (供前端使用)
    print("更新 papers.json...")
    update_papers_json(papers_with_results, base_dir, target_date)

    print(f"\n=== 完成! 共收录 {len(papers_with_results)} 篇论文 ===")


if __name__ == "__main__":
    main()
