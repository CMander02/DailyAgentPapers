"""
LLM 客户端 - 兼容 OpenAI API 格式
用于论文评分、摘要生成、标签提取
"""

import json
import urllib.request
import os
from typing import Optional


def call_llm(
    messages: list[dict],
    model: Optional[str] = None,
    base_url: Optional[str] = None,
    api_key: Optional[str] = None,
    temperature: float = 0.3,
    max_tokens: int = 2000,
) -> str:
    """调用 OpenAI 兼容 API"""
    model = model or os.environ.get("LLM_MODEL", "gpt-4o-mini")
    base_url = base_url or os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1")
    api_key = api_key or os.environ.get("LLM_API_KEY", "")

    # Ensure base_url ends properly
    base_url = base_url.rstrip("/")
    if not base_url.endswith("/v1"):
        if "/v1" not in base_url:
            base_url += "/v1"

    url = f"{base_url}/chat/completions"

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                result = json.loads(resp.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"]
        except Exception as e:
            if attempt < 2:
                import time
                wait = 2 ** (attempt + 1)
                print(f"  LLM API 请求失败 (attempt {attempt+1}): {e}, 等待 {wait}s...")
                time.sleep(wait)
            else:
                raise RuntimeError(f"LLM API 请求失败 (已重试 3 次): {e}")


def score_and_summarize(paper: dict) -> Optional[dict]:
    """
    对单篇论文进行评分和摘要生成。
    返回: {relevance_score, tags, chinese_summary, core_contributions, analysis}
    如果论文不相关(评分<4)则返回 None。
    """
    authors_str = ", ".join(
        f"{a['name']}" + (f" ({a['affiliation']})" if a["affiliation"] else "")
        for a in paper["authors"][:10]
    )
    if len(paper["authors"]) > 10:
        authors_str += f" 等共 {len(paper['authors'])} 位作者"

    system_prompt = """你是一位 AI/Agent 领域的研究专家。你的任务是评估 arxiv 论文与 "AI Agent" 研究领域的相关性，并生成中文摘要。

评分标准 (1-10):
- 9-10: 核心 Agent 论文（Agent 架构、多智能体系统、Agent 规划/推理/记忆/工具使用）
- 7-8: 高度相关（LLM 应用于 Agent 场景、Agent 评测/基准、Agent 安全）
- 5-6: 中等相关（通用 LLM 能力提升但可用于 Agent、强化学习用于决策）
- 3-4: 弱相关（纯 NLP/CV 任务，仅间接相关）
- 1-2: 不相关

机构过滤指引：
- 如果论文纯粹来自东南亚/日本/大洋洲的本地小机构，且内容质量一般，可适当降低评分
- 顶级机构（MIT, Stanford, Google, Meta, OpenAI, DeepMind, 清华, 北大, 中科院等）的论文应基于内容评分

你必须严格按 JSON 格式输出，不要添加任何其他文字。"""

    user_prompt = f"""请评估以下论文：

标题: {paper['title']}
作者: {authors_str}
类别: {', '.join(paper['categories'])}
摘要: {paper['summary']}

请输出以下 JSON（不要用 markdown code block 包裹）:
{{
  "relevance_score": <1-10的浮点数>,
  "tags": ["标签1", "标签2", ...],
  "chinese_summary": "200-300字的中文摘要",
  "core_contributions": ["核心贡献1", "核心贡献2", ...],
  "analysis": "150-250字的中文解读，分析这篇论文的创新点、方法论亮点和潜在影响"
}}"""

    try:
        response = call_llm(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3,
            max_tokens=1500,
        )

        # 尝试解析 JSON
        response = response.strip()
        # 移除可能的 markdown code block
        if response.startswith("```"):
            response = response.split("\n", 1)[1]
            if response.endswith("```"):
                response = response[:-3]
            response = response.strip()

        result = json.loads(response)

        # 验证必要字段
        required = ["relevance_score", "tags", "chinese_summary", "core_contributions", "analysis"]
        for field in required:
            if field not in result:
                print(f"  警告: LLM 返回缺少字段 {field}")
                return None

        # 过滤低分论文
        if result["relevance_score"] < 4:
            return None

        return result

    except json.JSONDecodeError as e:
        print(f"  警告: LLM 返回非法 JSON: {e}")
        print(f"  原始返回: {response[:200]}")
        return None
    except Exception as e:
        print(f"  警告: 论文评分失败: {e}")
        return None
