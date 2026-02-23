"""
arxiv API 查询客户端
- 宽泛搜索 agent 相关论文 (cs.AI, cs.CL, cs.MA, cs.LG)
- 关键词精筛
"""

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from typing import Optional
import time
import re


ARXIV_API = "http://export.arxiv.org/api/query"
NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def build_query(keywords: list[str], categories: list[str]) -> str:
    """构建 arxiv API 搜索查询字符串"""
    # 关键词 OR 组合
    kw_parts = [f'all:"{kw}"' for kw in keywords]
    kw_query = " OR ".join(kw_parts)

    # 类别 OR 组合
    cat_parts = [f"cat:{cat}" for cat in categories]
    cat_query = " OR ".join(cat_parts)

    return f"({kw_query}) AND ({cat_query})"


def fetch_arxiv_papers(
    query: str,
    max_results: int = 200,
    start: int = 0,
    sort_by: str = "submittedDate",
    sort_order: str = "descending",
) -> list[dict]:
    """查询 arxiv API 并解析返回的 Atom XML"""
    params = {
        "search_query": query,
        "start": start,
        "max_results": max_results,
        "sortBy": sort_by,
        "sortOrder": sort_order,
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"

    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "DailyAgentPapers/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read().decode("utf-8")
            break
        except Exception as e:
            if attempt < 3:
                wait = 2 ** (attempt + 1)
                print(f"  arxiv API 请求失败 (attempt {attempt+1}): {e}, 等待 {wait}s...")
                time.sleep(wait)
            else:
                raise RuntimeError(f"arxiv API 请求失败 (已重试 4 次): {e}")

    root = ET.fromstring(data)
    papers = []

    for entry in root.findall("atom:entry", NS):
        paper = parse_entry(entry)
        if paper:
            papers.append(paper)

    return papers


def parse_entry(entry: ET.Element) -> Optional[dict]:
    """解析单个 arxiv entry"""
    arxiv_id_raw = entry.find("atom:id", NS).text.strip()
    # Extract clean arxiv ID: e.g. "2602.12345" from URL
    arxiv_id = arxiv_id_raw.split("/abs/")[-1]
    # Remove version suffix
    arxiv_id = re.sub(r"v\d+$", "", arxiv_id)

    title = entry.find("atom:title", NS).text.strip().replace("\n", " ")
    title = re.sub(r"\s+", " ", title)

    summary = entry.find("atom:summary", NS).text.strip()

    # Authors
    authors = []
    for author_el in entry.findall("atom:author", NS):
        name = author_el.find("atom:name", NS).text.strip()
        affiliation_el = author_el.find("arxiv:affiliation", NS)
        affiliation = affiliation_el.text.strip() if affiliation_el is not None else ""
        authors.append({"name": name, "affiliation": affiliation})

    # Categories
    categories = []
    for cat_el in entry.findall("atom:category", NS):
        categories.append(cat_el.get("term"))

    # Primary category
    primary_cat_el = entry.find("arxiv:primary_category", NS)
    primary_category = primary_cat_el.get("term") if primary_cat_el is not None else ""

    # Published date
    published = entry.find("atom:published", NS).text.strip()
    updated = entry.find("atom:updated", NS).text.strip()

    # PDF link
    pdf_url = ""
    for link in entry.findall("atom:link", NS):
        if link.get("title") == "pdf":
            pdf_url = link.get("href", "")
            break

    return {
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": authors,
        "summary": summary,
        "categories": categories,
        "primary_category": primary_category,
        "published": published,
        "updated": updated,
        "arxiv_url": f"https://arxiv.org/abs/{arxiv_id}",
        "pdf_url": pdf_url or f"https://arxiv.org/pdf/{arxiv_id}",
    }


def filter_by_date(papers: list[dict], target_date: str) -> list[dict]:
    """
    按日期过滤论文。target_date 格式: YYYY-MM-DD
    arxiv published 的时间是 UTC，我们取 published 日期匹配的论文。
    """
    filtered = []
    for p in papers:
        pub_date = p["published"][:10]  # YYYY-MM-DD
        if pub_date == target_date:
            filtered.append(p)
    return filtered


def keyword_filter(papers: list[dict], must_have: list[str], boost_keywords: list[str]) -> list[dict]:
    """
    关键词精筛：
    - must_have 中至少命中一个关键词才保留
    - boost_keywords 用于后续评分加权
    """
    filtered = []
    for p in papers:
        text = (p["title"] + " " + p["summary"]).lower()
        hit = any(kw.lower() in text for kw in must_have)
        if hit:
            # Count boost keyword hits
            boost_count = sum(1 for kw in boost_keywords if kw.lower() in text)
            p["keyword_boost"] = boost_count
            filtered.append(p)
    return filtered
