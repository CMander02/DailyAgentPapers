"""
论文全文获取模块 - 通过 arxiv-to-prompt 获取 LaTeX 源码，PDF 作为 fallback。
支持按 section 提取内容，实现精准送达 LLM。
"""

import logging
import os
import tempfile
import urllib.request

logger = logging.getLogger(__name__)


def _fetch_latex(arxiv_id: str, config: dict) -> str | None:
    """尝试通过 arxiv-to-prompt 获取 LaTeX 源码。"""
    try:
        from arxiv_to_prompt import process_latex_source

        latex_config = config.get("paper_content", {}).get("latex", {})
        result = process_latex_source(
            arxiv_id,
            keep_comments=latex_config.get("keep_comments", False),
            remove_appendix_section=latex_config.get("remove_appendix_section", True),
            use_cache=latex_config.get("use_cache", True),
        )
        if result:
            return result
    except ImportError:
        logger.warning("arxiv-to-prompt 未安装，跳过 LaTeX 获取")
    except Exception as e:
        logger.warning("LaTeX 获取失败 (%s): %s", arxiv_id, e)
    return None


def _fetch_pdf_text(arxiv_id: str, config: dict) -> str | None:
    """下载 PDF 并提取文本（fallback 方案）。"""
    try:
        import fitz  # pymupdf
    except ImportError:
        logger.warning("pymupdf 未安装，跳过 PDF 获取")
        return None

    network_config = config.get("network", {})
    user_agent = network_config.get("user_agent", "DailyAgentPapers/1.0")
    timeout = network_config.get("request_timeout", 60)

    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
    tmp_path = None
    try:
        tmp_fd, tmp_path = tempfile.mkstemp(suffix=".pdf")
        os.close(tmp_fd)

        req = urllib.request.Request(pdf_url, headers={"User-Agent": user_agent})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            with open(tmp_path, "wb") as f:
                f.write(resp.read())

        doc = fitz.open(tmp_path)
        text_parts = []
        for page in doc:
            text_parts.append(page.get_text())
        doc.close()

        text = "\n".join(text_parts)
        if text.strip():
            return text
        return None

    except Exception as e:
        logger.warning("PDF 获取失败 (%s): %s", arxiv_id, e)
        return None
    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)


def get_section_list(latex_content: str) -> list[str]:
    """从 LaTeX 内容中提取 section 级别目录。"""
    try:
        from arxiv_to_prompt import list_sections
        return list_sections(latex_content)
    except Exception as e:
        logger.warning("提取目录失败: %s", e)
        return []


def extract_sections(latex_content: str, section_names: list[str], max_chars_per_section: int = 15000) -> str:
    """
    从 LaTeX 内容中提取指定 section 的内容，拼接返回。
    每个 section 截断到 max_chars_per_section。
    """
    try:
        from arxiv_to_prompt import extract_section
    except ImportError:
        return ""

    parts = []
    for name in section_names:
        content = extract_section(latex_content, name)
        if content:
            if len(content) > max_chars_per_section:
                content = content[:max_chars_per_section] + "\n[... 已截断 ...]"
            parts.append(content)

    return "\n\n".join(parts)


def fetch_paper_content(arxiv_id: str, config: dict) -> tuple[str, str]:
    """
    获取论文全文内容。

    返回: (content_text, source_type)
      - source_type: "latex" | "pdf" | "abstract_only"
      - 当全文不可用时，content_text 为空字符串，source_type 为 "abstract_only"
    """
    max_length = config.get("paper_content", {}).get("max_content_length", 50000)

    # 主路径：LaTeX 源码
    content = _fetch_latex(arxiv_id, config)
    if content:
        if len(content) > max_length:
            content = content[:max_length]
        return content, "latex"

    # Fallback：PDF 文本
    content = _fetch_pdf_text(arxiv_id, config)
    if content:
        if len(content) > max_length:
            content = content[:max_length]
        return content, "pdf"

    return "", "abstract_only"
