---
title: "GeoNatureAgent Benchmark: Benchmarking LLM Agents for Environmental Geospatial Analysis Across Frontier and Open-Weight Foundation Models"
authors:
  - "Gabriel Diaz-Ireland"
  - "Diego Prieto-Herráez"
  - "Mario García Peces"
  - "Javier Velázquez"
  - "Devika Jain"
date: "2026-06-11"
arxiv_id: "2606.12821"
arxiv_url: "https://arxiv.org/abs/2606.12821"
pdf_url: "https://arxiv.org/pdf/2606.12821v1"
categories:
  - "cs.AI"
  - "cs.ET"
tags:
  - "LLM Agent Benchmark"
  - "Geospatial Analysis"
  - "Environmental AI"
  - "Tool Calling Agent"
  - "Agent Evaluation"
  - "Open-weight Models"
  - "Multi-turn Conversation"
  - "Spatial Reasoning"
relevance_score: 9.2
---

# GeoNatureAgent Benchmark: Benchmarking LLM Agents for Environmental Geospatial Analysis Across Frontier and Open-Weight Foundation Models

## 原始摘要

Environmental scientists spend disproportionate effort on data wrangling rather than analysis, and AI agents that automate geospatial workflows remain unvalidated: no benchmark evaluates agents operating through structured tool calling against real APIs. We introduce the GeoNatureAgent Benchmark, the first benchmark for environmental analysis agents that operate via structured tool calls to a production-style geospatial API. It comprises 93 tasks across 18 categories, covering municipality analysis, multi-turn conversation, spatial reasoning, cross-indicator synthesis, error handling and recovery, ranking, comparison, multilingual understanding, habitat analysis, and task rejection. Tasks are evaluated against an open, self-hostable API serving three environmental indicators across Spain and Portugal via sixteen tools. We evaluate seven LLMs (Claude Sonnet 4, DeepSeek V3.2, GLM-5, Gemini 2.5 Pro, Qwen3-235B, GPT-OSS-120B, Llama 4 Scout) under three temperature-1.0 seeds, reporting capability and per-case cost as orthogonal axes. We find: (1) Claude Sonnet 4 leads at 60.8% +/- 0.8%, followed by DeepSeek V3.2 at 56.3% +/- 3.1%, with no other model above 51%; (2) the cost-accuracy Pareto frontier is occupied mostly by open-weight models, with DeepSeek V3.2 offering 93% of Claude's capability at 11x lower cost ($0.011/case); (3) comparison tasks remain universally unsolved (0% on close-value comparisons), exposing systematic reasoning limits; and (4) structured tool calling against a real API is more discriminative than general-purpose GIS benchmarks, with accuracies 25-35 points lower. We further show extensibility by integrating BigEarthNet V2 land cover for Portugal alongside Spanish CO2 and erosion indicators. The benchmark, harness, and self-hostable API are publicly available.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决环境科学领域AI智能体缺乏系统性评估基准的核心问题。研究背景是:环境监测需要多时相地理空间分析(如土地覆盖变化检测、侵蚀风险评估等),但科学家们花费大量精力在数据处理和调试代码上,而非实际分析。现有方法存在明显不足:已有的地理空间AI基准(如GeoBenchX、ThinkGeo)面向通用GIS任务而非环境科学;环境知识基准(EnviroExam)只评估知识而非智能体行为;代码生成基准(UnivEARTH)不反映实际生产系统采用的结构化API交互方式(58%的LLM生成地球引擎代码无法执行);基础模型基准(GEO-Bench)评估像素级视觉模型而非智能体工具编排能力。因此,本文提出了GeoNatureAgent Benchmark,这是首个通过结构化工具调用面向生产风格地理空间API的环境分析智能体基准,包含93个任务、18个类别,评估7个前沿大模型在真实API上的表现,并报告能力与成本的正交维度,填补了环境科学AI智能体评估的关键空白。

### Q2: 有哪些相关研究？

相关研究可按方法类、应用类和评测类组织。方法类包括：LLM + Tool Pool 范式（如 GeoGPT 使用 GPT-3.5-turbo + LangChain、LLM-Geo 基于 GPT-4 进行 DAG 分解、GIS Copilot 集成 LLM 到 QGIS）；微调专家模型（GTChain 微调 LLaMA-2-7B，比 GPT-4 准确率高 32.5%；EnvGPT 在 1 亿环境 tokens 上微调 8B 模型，性能媲美 GPT-4o-mini）；多智能体系统（GeoJSON Agents 的 GPT-4o Planner-Worker 架构达 97% 准确率，比单智能体高 49%；GeoLLM-Squad 通过专业子智能体提升 17%）；成本高效混合模型（Geo-OLM 使低于 7B 的模型以 100 倍低成本达到 GPT-4o 的 90% 性能）。应用类包括 Google Earth AI（地理问答准确率 82%）和 Pan 等人的 MCP 接口（空气质量监测事实精确度 4.78/5.0）。评测类包括 GeoBenchX（最接近本文，202 个任务、24 个通用 GIS 工具、LLM-as-judge 评分，但使用低层级本地文件操作）；地图推理（MapEval、MapQA）、空间推理（GPSBench、SpatiaLab）、基础模型（GEO-Bench 和 PANGAEA 评估像素级分类/分割）。本文的关键区别在于：GeoBenchX 使用低层级 GIS 原语操作本地文件，而 GeoNatureAgent Benchmark 使用高层级领域操作调用生产级云 API，且首次评估智能体在真实地理空间 API 上的结构化工具调用，涵盖多轮对话、多语言输入和跨指标综合等能力。

### Q3: 论文如何解决这个问题？

该论文通过构建一个完整的评估框架和公开可用的基准测试来解决问题。核心方法包括三大组件：一是GeoNatureAgent Benchmark，包含93个跨18类别的任务，覆盖工具选择、错误处理、多轮对话、空间推理等关键能力；二是ReAct式智能体架构，智能体在循环中接收查询、推理工具、执行调用、观察结果并生成响应，可调用16个工具，包括领域专用工具（如地图分析、比较、排名）和从GeoBenchX适配的通用GIS操作（如缓冲区创建、空间关系选择）；三是生产级地理空间API，以云优化GeoTIFF和预计算JSON形式提供西班牙和葡萄牙的三个环境指标。关键技术在于结构化工具调用而非代码生成，因为实证表明函数调用的准确率远高于agent生成可执行代码。创新点包括：设计“能力与成本正交”双指标评估体系，避免将预算约束与推理能力混为一谈；首创对真实API进行结构化工具调用的环境分析agent基准测试；包含故意不可解决的错误处理任务来测试agent优雅拒绝而非幻觉的能力；通过公开可用的自托管API和评估工具实现可扩展性，如集成BigEarthNet V2土地覆盖数据。

### Q4: 论文做了哪些实验？

该论文对7个LLM在GeoNatureAgent Benchmark v5上进行了评估，该基准包含93个任务、18个类别（涵盖市政分析、多轮对话、空间推理、跨指标合成、错误处理与恢复、排序、比较、多语言理解、栖息地分析和任务拒绝）。实验设置使用v3零样本ReAct提示、max_turns=10、max_tokens=4096和temperature=1.0，采用连续云端运行以确保基础设施一致。评估的模型包括：Claude Sonnet 4、DeepSeek V3.2、GLM-5、Gemini 2.5 Pro、Qwen3-235B、GPT-OSS-120B和Llama 4 Scout。每个模型在3个随机种子下运行（Claude因API限制运行2次）。主要结果：Claude Sonnet 4以60.8% ± 0.8%的准确率领先，DeepSeek V3.2以56.3% ± 3.1%紧随其后，其他模型均未超过51%。在成本-准确率帕累托前沿上，开源模型占据主导地位，DeepSeek V3.2以Claude 11倍低的成本（0.011美元/案例）实现了其93%的能力。关键发现包括：比较任务（接近值比较）在所有模型的所有种子中均失败（0%），暴露出系统性推理限制；与通用GIS基准相比，结构化工具调用的准确率低25-35个百分点。实验还展示了通过BigEarthNet V2土地覆盖数据扩展基准的能力。

### Q5: 有什么可以进一步探索的点？

该基准测试揭示了多个未来探索方向：(1) 当前模型在“接近值比较”任务上普遍得分为0%，表明在数值推理和精细空间判别上存在系统性短板，未来可探索设计专门的推理链或符号混合模型来增强比较逻辑。(2) 真实API交互带来的不确定性（如COG切片、JSON解析错误）远高于本地文件操作，可研究“工具调用容错机制”和“自适应重试策略”以提升鲁棒性。(3) 多轮对话中的记忆连贯性是尚未充分解决的问题，可引入记忆增强检索或结构化历史摘要来改善。(4) 开源模型与商业模型间的成本-精度Pareto边界尚不清晰，未来可系统探索模型蒸馏、工具调用微调或基于强模型弱监督的自动化数据生成路径。(5) 当前仅覆盖三个指标和两个国家，扩展至更多区域、指标（如水文、灾害）和时间序列分析将是自然延伸，同时可引入动态数据源更新机制以模拟真实长期监测场景。

### Q6: 总结一下论文的主要内容

GeoNatureAgent基准测试是首个评估LLM代理通过结构化工具调用与真实地理空间API交互进行环境分析的能力基准。它包含93个任务，涵盖18个类别，包括市政分析、多轮对话、空间推理、跨指标综合、错误处理与恢复、排序、比较、多语言理解、栖息地分析和任务拒绝。评估基于一个开放的、可自托管的API，提供西班牙和葡萄牙的三项环境指标，通过16个工具实现。主要结论：(1) Claude Sonnet 4表现最佳（60.8%），DeepSeek V3.2次之（56.3%），其他模型均低于51%；(2) 开放权重模型主导成本-精度帕累托前沿，DeepSeek V3.2以11倍低的成本达到Claude 93%的能力；(3) 比较类任务普遍未解决（接近值比较准确率为0%），暴露了系统的推理局限；(4) 结构化工具调用比通用GIS基准更具区分度，准确率低25-35个百分点。该基准、测试平台和可自托管API已公开提供。
