#!/usr/bin/env python3
"""
主入口脚本：获取昨日 arxiv Agent 论文，LLM 评分/摘要，写入 markdown。

用法:
    python scripts/fetch_papers.py                   # 自动获取昨日论文
    python scripts/fetch_papers.py --date 2026-02-22  # 指定日期
"""

import argparse
import glob
import json
import logging
import os
import sys
import yaml
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv

from arxiv_client import build_query, fetch_arxiv_papers, keyword_filter
from llm_client import quick_relevance_check, score_and_summarize
from markdown_writer import write_paper_file, append_paper_json, update_readme
from paper_content import fetch_paper_content

logger = logging.getLogger("dailyagentpapers")


def setup_logging():
    """配置日志格式。"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    # 抑制第三方库噪音
    logging.getLogger("arxiv").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)


def load_config(base_dir: str) -> dict:
    """加载 config.yaml"""
    config_path = os.path.join(base_dir, "config.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_history_index(base_dir: str) -> dict[str, int]:
    """
    扫描所有历史 papers.json，构建 {arxiv_id: max_version} 索引。
    用于去重：跳过已收录且版本相同的论文。
    """
    index = {}
    pattern = os.path.join(base_dir, "data", "*", "*", "*", "papers.json")
    for path in glob.glob(pattern):
        try:
            with open(path, "r", encoding="utf-8") as f:
                papers = json.load(f)
            for p in papers:
                aid = p.get("arxiv_id", "")
                ver = p.get("version", 1)
                if aid and ver > index.get(aid, 0):
                    index[aid] = ver
        except Exception:
            continue
    return index


def dedup_papers(papers: list[dict], history: dict[str, int]) -> list[dict]:
    """
    去重：
    - 历史中不存在 → 保留（新论文）
    - 历史中存在但版本更高 → 保留（论文有更新）
    - 历史中存在且版本相同或更低 → 跳过
    """
    kept = []
    for p in papers:
        aid = p["arxiv_id"]
        ver = p.get("version", 1)
        hist_ver = history.get(aid, 0)
        if ver > hist_ver:
            kept.append(p)
        else:
            logger.info("  跳过已收录: %s v%d (历史 v%d)", aid, ver, hist_ver)
    return kept


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Fetch daily arxiv agent papers")
    parser.add_argument("--date", type=str, help="Target date (YYYY-MM-DD), default: yesterday")
    parser.add_argument("--base-dir", type=str, default=None, help="Project root directory")
    parser.add_argument("--dry-run", action="store_true", help="Only fetch and filter, don't call LLM")
    args = parser.parse_args()

    # 确定项目根目录
    base_dir = args.base_dir or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 加载 .env 文件
    load_dotenv(os.path.join(base_dir, ".env"))

    # 确定目标日期
    if args.date:
        target_date = args.date
    else:
        yesterday = datetime.now(timezone.utc) - timedelta(days=1)
        target_date = yesterday.strftime("%Y-%m-%d")

    logger.info("=== DailyAgentPapers ===")
    logger.info("目标日期: %s", target_date)
    logger.info("项目目录: %s", base_dir)

    # 加载配置
    config = load_config(base_dir)
    search_keywords = config.get("search_keywords", [])
    categories = config.get("categories", [])
    filter_keywords = config.get("filter_keywords", [])
    boost_keywords = config.get("boost_keywords", [])
    max_results = config.get("max_results", 200)

    min_score = config.get("llm", {}).get("min_relevance_score", 4)

    # Step 1: 查询 arxiv API（含日期过滤）
    logger.info("[1/4] 查询 arxiv API (关键词: %d, 类别: %d, 日期: %s)...", len(search_keywords), len(categories), target_date)
    query = build_query(search_keywords, categories, date_str=target_date)
    date_filtered = fetch_arxiv_papers(query, config, max_results=max_results)
    logger.info("  获取到 %d 篇论文", len(date_filtered))

    if not date_filtered:
        alt_date = (datetime.strptime(target_date, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
        logger.info("  当天无结果，尝试前一天 (%s)...", alt_date)
        query = build_query(search_keywords, categories, date_str=alt_date)
        date_filtered = fetch_arxiv_papers(query, config, max_results=max_results)
        if date_filtered:
            logger.info("  使用扩展日期，获取到: %d 篇", len(date_filtered))
            target_date = alt_date

    if not date_filtered:
        logger.info("  没有找到目标日期的论文，退出。")
        sys.exit(0)

    # Step 2: 关键词精筛
    logger.info("[2/4] 关键词精筛 (过滤词: %d)...", len(filter_keywords))
    filtered = keyword_filter(date_filtered, filter_keywords, boost_keywords)
    logger.info("  关键词匹配: %d 篇", len(filtered))

    if not filtered:
        logger.info("  关键词过滤后没有论文，退出。")
        sys.exit(0)

    # Step 2.5: 历史去重
    logger.info("  加载历史数据去重...")
    history = load_history_index(base_dir)
    logger.info("  历史索引: %d 篇论文", len(history))
    before_dedup = len(filtered)
    filtered = dedup_papers(filtered, history)
    logger.info("  去重后: %d 篇 (跳过 %d 篇已收录)", len(filtered), before_dedup - len(filtered))

    if not filtered:
        logger.info("  去重后没有新论文，退出。")
        sys.exit(0)

    if args.dry_run:
        logger.info("=== Dry Run 结果 ===")
        for p in filtered:
            logger.info("  - [%s] %s", p["arxiv_id"], p["title"])
        logger.info("共 %d 篇待处理", len(filtered))
        return

    # Step 3: LLM 预评分（基于摘要快速过滤低相关度论文）
    logger.info("[3/4] LLM 预评分 (%d 篇, 阈值: %s)...", len(filtered), min_score)
    relevant_papers = []
    for i, paper in enumerate(filtered):
        logger.info("  [%d/%d] %s", i + 1, len(filtered), paper["title"][:60])
        score = quick_relevance_check(paper, config)
        if score is None:
            logger.info("    预评分失败，保留")
            relevant_papers.append(paper)
        elif score >= min_score:
            logger.info("    预评分: %.1f/10 -> 通过", score)
            relevant_papers.append(paper)
        else:
            logger.info("    预评分: %.1f/10 -> 跳过", score)
    logger.info("  预评分通过: %d/%d 篇", len(relevant_papers), len(filtered))

    if not relevant_papers:
        logger.info("  预评分后没有论文通过，退出。")
        sys.exit(0)

    # Step 4: 逐篇处理（获取全文 → LLM 评分/摘要 → 立即落盘）
    logger.info("[4/4] 逐篇处理 (%d 篇)...", len(relevant_papers))
    total_saved = 0
    source_stats = {"latex": 0, "pdf": 0, "abstract_only": 0}
    for i, paper in enumerate(relevant_papers):
        logger.info("  [%d/%d] %s", i + 1, len(relevant_papers), paper["title"][:60])

        # 获取全文
        content, source_type = fetch_paper_content(paper["arxiv_id"], config)
        source_stats[source_type] += 1
        if content:
            logger.info("    全文来源: %s (%d 字符)", source_type, len(content))
        else:
            logger.info("    全文来源: %s", source_type)

        # LLM 评分 + 摘要
        result = score_and_summarize(paper, config, full_content=content or None, content_source=source_type)
        if not result:
            logger.info("    跳过 (评分过低或处理失败)")
            continue

        logger.info("    评分: %.1f/10, 标签: %s", result["relevance_score"], result["tags"])

        # 立即落盘：写 md + 追加 papers.json + 更新 README
        filepath = write_paper_file(paper, result, base_dir, target_date, config)
        logger.info("    写入: %s", filepath)
        append_paper_json(paper, result, base_dir, target_date, config)
        update_readme(base_dir, target_date, config)
        total_saved += 1
        logger.info("    已落盘 (%d 篇累计)", total_saved)

    logger.info("  全文统计: LaTeX %d, PDF %d, 仅摘要 %d",
                source_stats["latex"], source_stats["pdf"], source_stats["abstract_only"])
    logger.info("=== 完成! 共收录 %d 篇论文 ===", total_saved)


if __name__ == "__main__":
    main()
