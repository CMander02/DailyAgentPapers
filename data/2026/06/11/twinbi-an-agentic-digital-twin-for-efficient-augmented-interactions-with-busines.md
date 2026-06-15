---
title: "TwinBI: An Agentic Digital Twin for Efficient Augmented Interactions with Business Intelligence Dashboards"
authors:
  - "Jisoo Jang Wen-Syan Li"
date: "2026-06-11"
arxiv_id: "2606.13731"
arxiv_url: "https://arxiv.org/abs/2606.13731"
pdf_url: "https://arxiv.org/pdf/2606.13731v1"
github_url: "https://github.com/simonjisu/TwinBI"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "LLM Agent"
  - "Business Intelligence"
  - "Dashboard Agent"
  - "State Management"
  - "Agentic Digital Twin"
  - "Provenance Tracking"
  - "Benchmark Evaluation"
relevance_score: 8.5
---

# TwinBI: An Agentic Digital Twin for Efficient Augmented Interactions with Business Intelligence Dashboards

## 原始摘要

Business intelligence (BI) increasingly combines dashboard interaction with LLM-based assistance, but these two modes often fall out of sync during multi-step analysis. As users switch between direct dashboard manipulation and natural-language queries, it becomes difficult to preserve a consistent analytical state across filters, hierarchies, metrics, and chart context. We present TwinBI, an agentic digital-twin framework that couples an LLM-based agent system with an executable BI dashboard state. TwinBI unifies conversational interaction, dashboard manipulation, semantic grounding, and provenance tracking through a shared analytical state reconstructed from a unified interaction log. It also exposes artifacts such as schema views, SQL, logs, and an /insights command for state-grounded analytical summaries. We evaluate TwinBI in two complementary ways. In a controlled A/B benchmark with the same backbone agent, TwinBI improves exact-match accuracy from 43.3% to 63.3%, partial-credit accuracy from 48.3% to 70.8%, and substantially reduces timeout rate from 40.0% to 10.0% relative to Dashboard alone. In a usability study, participants benefited from the integrated dashboard-and-chat workflow, with high task accuracy, moderate workload, and favorable ratings for state-aware interaction mechanisms. These results suggest that TwinBI improves both agent-level analytical reliability and user-facing analytical support by turning visible dashboard state into richer actionable context. Our dataset and source code are available at: https://github.com/simonjisu/TwinBI

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决商业智能（BI）系统中，基于大型语言模型（LLM）的对话式助手与传统仪表盘交互之间存在的“分析状态不同步”问题。研究背景是，现有BI系统正结合仪表盘直接操作与LLM辅助的对话查询，但在多步骤分析过程中，用户在这两种模式间切换时，过滤器、层级结构、度量指标和图表上下文等关键分析状态难以保持一致。现有方法的不足之处在于，LLM代理往往脱离仪表盘所编码的精确语义约束（如度量定义、聚合粒度、过滤范围），虽能生成流畅的自然语言回答，却可能与系统的实际分析状态产生不一致，导致回答虽看似合理但分析结果不可靠。TwinBI的核心目标是通过一个智能体数字孪生框架，将LLM代理系统与可执行的仪表盘状态耦合，通过统一的事件日志重建共享分析状态，从而实现对话交互、仪表盘操作、语义锚定和操作追溯的统一，确保用户意图、语义定义与查询执行在整个分析过程中始终保持同步，提升BI分析的可靠性与用户体验。

### Q2: 有哪些相关研究？

在相关研究中，本文主要从自然语言数据接口（NLIDB）、NL-to-SQL系统以及基于LLM的智能体等方向展开对比。

**方法类**：现有学术系统多聚焦于单一维度，例如NLP驱动的图表生成、对话式分析辅助或仪表盘可用性优化，但缺乏跨对话与仪表盘交互的状态同步管理。TwinBI通过可执行的仪表盘数字孪生状态，将对话、操作、语义和溯源统一到共享分析状态中，弥补了这一空白。

**应用类**：商业BI助手虽然开始结合自然语言查询和仪表盘，但公开文档显示其对显式状态同步、模式感知交互连续性和全面溯源日志的支持仍不完善。TwinBI则明确实现了这些机制，并通过统一交互日志重建状态。

**评测类**：本文通过A/B基准测试（将TwinBI与单一仪表盘模式对比）和用户可用性研究进行评估，结果证明了其在精确匹配准确率、部分匹配准确率及超时率上的显著优势。

总而言之，TwinBI与现有工作的核心区别在于：它并非仅解决查询生成或可视化问题，而是通过数字孪生框架实现了仪表盘状态与LLM智能体之间的双向、一致的状态同步和上下文感知交互。

### Q3: 论文如何解决这个问题？

TwinBI通过一个五层架构的智能孪生框架来解决BI分析中对话与仪表盘状态不同步的问题。核心方法是将LLM智能体系统与可执行的仪表盘状态深度耦合，通过统一交互日志重建共享的分析状态。

整体框架包含五个层次：表现层（Streamlit+Apache Superset）、编排层（FastAPI多智能体系统）、语义层（Cube声明式模型）、BI工具层（Superset仪表盘）和数据层（DuckDB）。关键技术包括：

1. **统一交互日志**：系统记录所有对话交互、仪表盘操作（标签切换、交叉过滤、全局筛选等）和工具调用元数据，作为状态重建和溯源的唯一权威记录。这解决了多步分析中用户切换操作模式时分析状态丢失的问题。

2. **状态感知的编排层**：后端将对话历史、仪表盘操作日志和工具输出整合为统一分析上下文，路由子任务到专门智能体（如Schema Explorer智能体），并基于当前重建状态生成响应。所有外部交互都通过后端管理的工具进行。

3. **语义层与层级模式图**：通过Cube声明模型定义度量、维度和层级，并派生出层级模式图，为Schema Explorer智能体提供结构化视图。这确保了对话查询和仪表盘查询使用兼容的语义模型。

4. **/insights命令与检查点机制**：专门命令可从当前状态生成分析摘要，包括当前分析切片、定量观察和建议步骤，确保输出始终基于可见分析证据。系统还暴露SQL查询、交互日志和模式图等检查点，方便用户验证推理过程。

创新点在于：将仪表盘状态作为可执行的上下文载体，而非孤立提示，使得后续聊天请求与当前操作状态自然对齐，如用户问“为什么这个类别增长了？”时，系统能恢复激活的图表、已应用的筛选器和层级位置。

### Q4: 论文做了哪些实验？

论文进行了两类实验。首先是一个受控的A/B基准测试，采用30个分析查询，基于零售销售仪表板环境，使用基于Playwright的浏览器智能体，以gpt-5-mini作为决策模型。对比方法为：A）仅依赖可见仪表板的Dashboard系统，B）TwinBI系统，额外提供聊天界面和后端支持。主要结果为：TwinBI在精确匹配准确率上从43.33%提升至63.33%，部分匹配准确率从48.33%提升至70.83%，超时率从40.0%显著降至10.0%，平均步数从16.47降至6.90。行为指标显示，TwinBI的无效动作率从10.93%降为0.00%，循环查询率从36.67%降至27.59%。其次是一个可用性研究，5名参与者完成3个难度递增的分析场景。任务准确率在S1和S3为100%，S2为73.33%；洞察准确率分别为80%、100%和80%；感知难度从1.8升至4.2。参与者偏好状态感知组合（可点击仪表板、通过智能体查找图表、点击+聊天），且工作负荷评估在低到中等范围。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于：评估仅基于单一数据集和有限用户，结论的普适性有待验证；图表解析与数值提取能力在复杂分析场景下仍显不足，可能导致上下文丢失。未来可从以下方向深入：一是跨仪表盘状态迁移，允许用户在多仪表盘间无缝继承分析上下文，提升复杂工作流的连续性；二是增强图表理解模块，利用视觉编码或多模态模型提升在不规则图表中的值提取精度；三是探索主动式决策支持，使Agent能基于状态历史预测用户意图并推荐下一步操作，而非仅被动响应。此外，可引入更细粒度的可信度评估机制，对Agent解析结果进行不确定性量化，帮助用户判断何时需要人工干预，从而构建更稳健的人机协同分析系统。

### Q6: 总结一下论文的主要内容

商业智能（BI）中，仪表盘交互与LLM辅助的多步分析常因状态不一致而脱节。为此，论文提出TwinBI，一个基于智能体数字孪生的框架，通过共享分析状态同步LLM智能体与可执行的仪表盘状态，统一了对话交互、仪表盘操作、语义锚定和溯源追踪。该方法从统一交互日志重建状态，并暴露模式视图、SQL、日志及/insights命令。实验表明，在A/B基准测试中，TwinBI相比纯仪表盘将精确匹配准确率从43.3%提升至63.3%，部分匹配从48.3%提升至70.8%，超时率从40.0%降至10.0%；用户研究也证实其整合工作流提升了分析可靠性与用户体验。核心贡献在于将仪表盘可见状态转化为可操作上下文，实现了智能体与用户的协同分析支持。
