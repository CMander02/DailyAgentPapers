"""
Markdown 文件生成器
- 生成单篇论文的 markdown 文件 (YAML frontmatter)
- 更新 README.md
- 生成 papers.json 供前端使用
"""

import os
import re
import json
from datetime import datetime
from typing import Optional


def slugify(title: str) -> str:
    """将标题转为文件名友好的 slug"""
    # 移除特殊字符，保留字母数字和空格
    slug = re.sub(r"[^\w\s-]", "", title.lower())
    slug = re.sub(r"[\s]+", "-", slug.strip())
    slug = re.sub(r"-+", "-", slug)
    # 限制长度
    return slug[:80].rstrip("-")


def generate_paper_markdown(paper: dict, llm_result: dict) -> str:
    """生成单篇论文的 markdown 内容"""
    # YAML frontmatter
    authors_list = []
    for a in paper["authors"][:20]:
        author_str = a["name"]
        if a.get("affiliation"):
            author_str += f" ({a['affiliation']})"
        # Escape quotes in YAML
        author_str = author_str.replace('"', '\\"')
        authors_list.append(f'  - "{author_str}"')

    tags_list = [f'  - "{t}"' for t in llm_result.get("tags", [])]
    cats_list = [f'  - "{c}"' for c in paper.get("categories", [])]

    contributions = llm_result.get("core_contributions", [])
    contributions_md = "\n".join(f"- {c}" for c in contributions)

    escaped_title = paper['title'].replace('"', '\\"')

    md = f"""---
title: "{escaped_title}"
authors:
{chr(10).join(authors_list)}
date: "{paper['published'][:10]}"
arxiv_id: "{paper['arxiv_id']}"
arxiv_url: "{paper['arxiv_url']}"
pdf_url: "{paper['pdf_url']}"
categories:
{chr(10).join(cats_list)}
tags:
{chr(10).join(tags_list)}
relevance_score: {llm_result.get('relevance_score', 0)}
---

# {paper['title']}

## 原始摘要

{paper['summary']}

## 中文摘要

{llm_result.get('chinese_summary', 'N/A')}

## 核心贡献

{contributions_md}

## 文章解读

{llm_result.get('analysis', 'N/A')}
"""
    return md


def write_paper_file(paper: dict, llm_result: dict, base_dir: str, date_str: str) -> str:
    """
    写入单篇论文的 markdown 文件。
    返回文件路径。
    """
    # date_str: YYYY-MM-DD → YYYY/MM/DD
    year, month, day = date_str.split("-")
    dir_path = os.path.join(base_dir, "data", year, month, day)
    os.makedirs(dir_path, exist_ok=True)

    slug = slugify(paper["title"])
    filename = f"{slug}.md"
    filepath = os.path.join(dir_path, filename)

    content = generate_paper_markdown(paper, llm_result)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def update_readme(papers_with_results: list[tuple[dict, dict]], base_dir: str, date_str: str):
    """更新 README.md，展示当日最新论文"""
    readme_path = os.path.join(base_dir, "README.md")

    # 按评分排序
    sorted_papers = sorted(
        papers_with_results,
        key=lambda x: x[1].get("relevance_score", 0),
        reverse=True,
    )

    year, month, day = date_str.split("-")

    lines = []
    lines.append("# DailyAgentPapers")
    lines.append("")
    lines.append("每日 Arxiv Agent 论文自动摘要 | Daily Arxiv Agent Paper Summaries")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"## 📋 最新论文 | {date_str}")
    lines.append("")
    lines.append(f"共收录 **{len(sorted_papers)}** 篇 Agent 相关论文")
    lines.append("")

    for paper, result in sorted_papers:
        score = result.get("relevance_score", 0)
        tags = result.get("tags", [])
        tags_str = " ".join(f"`{t}`" for t in tags[:5])
        slug = slugify(paper["title"])

        lines.append(f"### [{paper['title']}]({paper['arxiv_url']})")
        lines.append("")
        lines.append(f"**评分: {score}/10** | {tags_str}")
        lines.append("")
        lines.append(f"> {result.get('chinese_summary', 'N/A')[:200]}...")
        lines.append("")
        lines.append(
            f"📄 [详细解读](data/{year}/{month}/{day}/{slug}.md) | "
            f"📎 [PDF]({paper['pdf_url']})"
        )
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## 📅 历史归档")
    lines.append("")
    lines.append("论文按日期归档在 `data/YYYY/MM/DD/` 目录下。")
    lines.append("")
    lines.append("## 🔧 关于")
    lines.append("")
    lines.append("本项目通过 GitHub Actions 每日自动运行，使用 arxiv API 获取论文，")
    lines.append("LLM 进行智能筛选和中文摘要生成。")
    lines.append("")
    lines.append("- 数据源: [arxiv.org](https://arxiv.org/)")
    lines.append("- 关注领域: AI Agent, Multi-Agent Systems, LLM Agent, Tool Use, Planning, Reasoning")
    lines.append("- 更新频率: 每日北京时间 07:00")
    lines.append("")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def update_papers_json(papers_with_results: list[tuple[dict, dict]], base_dir: str, date_str: str):
    """
    更新 papers.json 供前端 GitHub Pages 使用。
    结构: {dates: {YYYY-MM-DD: [paper_summary, ...]}}
    """
    json_path = os.path.join(base_dir, "data", "papers.json")

    # 加载已有数据
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            all_data = json.load(f)
    else:
        all_data = {"dates": {}}

    # 构建当日数据
    day_papers = []
    for paper, result in papers_with_results:
        year, month, day = date_str.split("-")
        slug = slugify(paper["title"])
        day_papers.append({
            "arxiv_id": paper["arxiv_id"],
            "title": paper["title"],
            "authors": [a["name"] for a in paper["authors"][:5]],
            "author_count": len(paper["authors"]),
            "categories": paper["categories"],
            "arxiv_url": paper["arxiv_url"],
            "pdf_url": paper["pdf_url"],
            "published": paper["published"][:10],
            "tags": result.get("tags", []),
            "relevance_score": result.get("relevance_score", 0),
            "chinese_summary": result.get("chinese_summary", ""),
            "core_contributions": result.get("core_contributions", []),
            "analysis": result.get("analysis", ""),
            "md_path": f"data/{year}/{month}/{day}/{slug}.md",
        })

    # 按评分排序
    day_papers.sort(key=lambda x: x.get("relevance_score", 0), reverse=True)

    all_data["dates"][date_str] = day_papers

    # 保留最近 90 天数据，防止文件过大
    sorted_dates = sorted(all_data["dates"].keys(), reverse=True)
    if len(sorted_dates) > 90:
        for old_date in sorted_dates[90:]:
            del all_data["dates"][old_date]

    all_data["available_dates"] = sorted(all_data["dates"].keys(), reverse=True)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
