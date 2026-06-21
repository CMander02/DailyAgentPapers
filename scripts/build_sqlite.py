#!/usr/bin/env python3
"""Build a local SQLite database from DailyAgentPapers JSON/Markdown data.

The repository's canonical data format is currently static files:
  data/YYYY/MM/DD/papers.json + matching markdown files.

This script mirrors those files into a query-friendly SQLite database for
server-side use without changing the existing frontend/static-data pipeline.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def dumps(value: Any) -> str:
    return json.dumps(value if value is not None else None, ensure_ascii=False, sort_keys=True)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def read_text_if_exists(path: Path) -> str | None:
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def infer_date_from_papers_path(path: Path, data_dir: Path) -> str:
    rel = path.relative_to(data_dir)
    # YYYY/MM/DD/papers.json
    if len(rel.parts) >= 4:
        return f"{rel.parts[0]}-{rel.parts[1]}-{rel.parts[2]}"
    raise ValueError(f"Cannot infer date from {path}")


def create_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        PRAGMA foreign_keys = ON;

        CREATE TABLE IF NOT EXISTS metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS paper_days (
            date TEXT PRIMARY KEY,
            paper_count INTEGER NOT NULL DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            arxiv_id TEXT NOT NULL,
            version INTEGER NOT NULL DEFAULT 1,
            date TEXT NOT NULL,
            title TEXT NOT NULL,
            authors_json TEXT NOT NULL,
            author_count INTEGER,
            categories_json TEXT NOT NULL,
            arxiv_url TEXT,
            pdf_url TEXT,
            github_url TEXT,
            published TEXT,
            tags_json TEXT NOT NULL,
            relevance_score REAL NOT NULL DEFAULT 0,
            md_path TEXT,
            markdown_content TEXT,
            taxonomy_json TEXT,
            attributes_json TEXT,
            raw_json TEXT NOT NULL,
            UNIQUE(arxiv_id, version, date)
        );

        CREATE TABLE IF NOT EXISTS paper_authors (
            paper_id INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
            position INTEGER NOT NULL,
            name TEXT NOT NULL,
            PRIMARY KEY (paper_id, position)
        );

        CREATE TABLE IF NOT EXISTS paper_categories (
            paper_id INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
            category TEXT NOT NULL,
            PRIMARY KEY (paper_id, category)
        );

        CREATE TABLE IF NOT EXISTS paper_tags (
            paper_id INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
            tag TEXT NOT NULL,
            PRIMARY KEY (paper_id, tag)
        );

        CREATE INDEX IF NOT EXISTS idx_papers_date_score ON papers(date DESC, relevance_score DESC);
        CREATE INDEX IF NOT EXISTS idx_papers_arxiv_id ON papers(arxiv_id);
        CREATE INDEX IF NOT EXISTS idx_papers_published ON papers(published DESC);
        CREATE INDEX IF NOT EXISTS idx_papers_title ON papers(title);
        CREATE INDEX IF NOT EXISTS idx_paper_tags_tag ON paper_tags(tag);
        CREATE INDEX IF NOT EXISTS idx_paper_categories_category ON paper_categories(category);
        """
    )


def reset_data(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        DELETE FROM paper_tags;
        DELETE FROM paper_categories;
        DELETE FROM paper_authors;
        DELETE FROM papers;
        DELETE FROM paper_days;
        DELETE FROM metadata;
        DELETE FROM sqlite_sequence WHERE name = 'papers';
        """
    )


def insert_paper(conn: sqlite3.Connection, repo_root: Path, date: str, paper: dict[str, Any]) -> int:
    md_path = paper.get("md_path") or ""
    markdown_content = read_text_if_exists(repo_root / md_path) if md_path else None
    authors = paper.get("authors") or []
    categories = paper.get("categories") or []
    tags = paper.get("tags") or []

    cur = conn.execute(
        """
        INSERT OR REPLACE INTO papers (
            arxiv_id, version, date, title, authors_json, author_count,
            categories_json, arxiv_url, pdf_url, github_url, published,
            tags_json, relevance_score, md_path, markdown_content,
            taxonomy_json, attributes_json, raw_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            paper.get("arxiv_id", ""),
            int(paper.get("version") or 1),
            date,
            paper.get("title", ""),
            dumps(authors),
            paper.get("author_count"),
            dumps(categories),
            paper.get("arxiv_url"),
            paper.get("pdf_url"),
            paper.get("github_url"),
            paper.get("published"),
            dumps(tags),
            float(paper.get("relevance_score") or 0),
            md_path,
            markdown_content,
            dumps(paper.get("taxonomy")),
            dumps(paper.get("attributes")),
            dumps(paper),
        ),
    )
    if cur.lastrowid is None:
        raise RuntimeError(f"Failed to insert paper: {paper.get('arxiv_id', '<unknown>')}")
    paper_id = int(cur.lastrowid)

    for idx, author in enumerate(authors):
        conn.execute(
            "INSERT OR REPLACE INTO paper_authors (paper_id, position, name) VALUES (?, ?, ?)",
            (paper_id, idx, str(author)),
        )
    for category in categories:
        conn.execute(
            "INSERT OR REPLACE INTO paper_categories (paper_id, category) VALUES (?, ?)",
            (paper_id, str(category)),
        )
    for tag in tags:
        conn.execute(
            "INSERT OR REPLACE INTO paper_tags (paper_id, tag) VALUES (?, ?)",
            (paper_id, str(tag)),
        )
    return paper_id


def build_database(repo_root: Path, data_dir: Path, output: Path, rebuild: bool) -> dict[str, int]:
    output.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(output)
    try:
        create_schema(conn)
        if rebuild:
            reset_data(conn)

        paper_count = 0
        day_count = 0
        for papers_path in sorted(data_dir.glob("*/*/*/papers.json")):
            date = infer_date_from_papers_path(papers_path, data_dir)
            papers = load_json(papers_path)
            if not isinstance(papers, list):
                continue
            day_count += 1
            conn.execute(
                "INSERT OR REPLACE INTO paper_days (date, paper_count) VALUES (?, ?)",
                (date, len(papers)),
            )
            for paper in papers:
                if isinstance(paper, dict):
                    insert_paper(conn, repo_root, date, paper)
                    paper_count += 1

        index_path = data_dir / "index.json"
        if index_path.exists():
            conn.execute(
                "INSERT OR REPLACE INTO metadata (key, value) VALUES (?, ?)",
                ("index_json", dumps(load_json(index_path))),
            )
        conn.execute(
            "INSERT OR REPLACE INTO metadata (key, value) VALUES (?, ?)",
            ("generated_at", datetime.now(timezone.utc).isoformat()),
        )
        conn.execute(
            "INSERT OR REPLACE INTO metadata (key, value) VALUES (?, ?)",
            ("source_data_dir", str(data_dir)),
        )
        conn.commit()
        return {"days": day_count, "papers": paper_count}
    finally:
        conn.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Build data/papers.sqlite from data/**/papers.json")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--data-dir", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--no-rebuild", action="store_true", help="Do not clear existing rows before importing")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    data_dir = (args.data_dir or repo_root / "data").resolve()
    output = (args.output or data_dir / "papers.sqlite").resolve()

    stats = build_database(repo_root, data_dir, output, rebuild=not args.no_rebuild)
    size = output.stat().st_size
    print(f"SQLite database written: {output}")
    print(f"Imported days: {stats['days']}")
    print(f"Imported papers: {stats['papers']}")
    print(f"Size bytes: {size}")


if __name__ == "__main__":
    main()
