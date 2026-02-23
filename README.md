# DailyAgentPapers

每日 Arxiv Agent 论文自动摘要 | Daily Arxiv Agent Paper Summaries

---

## 项目说明

本项目通过 GitHub Actions 定时任务，每天自动从 arxiv 获取 AI Agent 领域的最新论文，经 LLM 智能筛选、评分和中文摘要生成后，归档到本仓库。

### 特性

- **三层筛选**: arxiv API 宽搜 → 关键词精筛 → LLM 评分过滤
- **LLM 摘要**: 中文摘要、核心贡献提炼、文章解读
- **结构化存储**: YAML frontmatter + Markdown，按日期归档
- **网页浏览**: GitHub Pages 部署，日历导航，暗色模式支持
- **每日更新**: 北京时间每天 07:00 自动运行

### 目录结构

```
data/
  YYYY/MM/DD/
    paper-slug.md       # 单篇论文 markdown（含 YAML frontmatter）
  papers.json           # 前端数据源
scripts/
  fetch_papers.py       # 主入口
  arxiv_client.py       # arxiv API 查询
  llm_client.py         # LLM API 调用
  markdown_writer.py    # Markdown 生成
web/                    # Next.js + shadcn/ui 前端
config.yaml             # 搜索关键词、类别配置
```

### 配置 Secrets

在 GitHub 仓库 Settings → Secrets and variables → Actions 中添加：

| Secret | 说明 |
|--------|------|
| `LLM_API_KEY` | LLM API Key |
| `LLM_BASE_URL` | API Base URL（OpenAI 兼容格式） |
| `LLM_MODEL` | 模型名称 |

### 手动运行

```bash
# 安装依赖
pip install -r requirements.txt

# 获取昨日论文
cd scripts && python fetch_papers.py

# 指定日期
cd scripts && python fetch_papers.py --date 2026-02-22

# Dry run（不调用 LLM）
cd scripts && python fetch_papers.py --dry-run
```

---

*暂无论文数据。首次运行 GitHub Actions 后将自动更新。*
