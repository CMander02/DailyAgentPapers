---
title: "BacktestBench: Benchmarking Large Language Models for Automated Quantitative Strategy Backtesting"
authors:
  - "Zhensheng Wang"
  - "Wenmian Yang"
  - "Qingtai Wu"
  - "Lequan Ma"
  - "Yiquan Zhang"
  - "Weijia Jia"
date: "2026-05-18"
arxiv_id: "2605.17937"
arxiv_url: "https://arxiv.org/abs/2605.17937"
pdf_url: "https://arxiv.org/pdf/2605.17937v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Multi-agent"
  - "Quantitative Backtesting"
  - "Benchmark"
  - "Code Generation"
relevance_score: 7.5
---

# BacktestBench: Benchmarking Large Language Models for Automated Quantitative Strategy Backtesting

## 原始摘要

Quantitative backtesting is essential for evaluating trading strategies but remains hampered by high technical barriers and limited scalability. While Large Language Models (LLMs) offer a transformative path to automate this complex, interdisciplinary workflow through advanced code generation, tool usage, and agentic planning, the practical realization is significantly challenged by the current lack of a large-scale benchmark dedicated to automated quantitative backtesting, which hinders progress in this field. To bridge this critical gap, we introduce BacktestBench, the first large-scale benchmark for automated quantitative backtesting. Built from over 6 million real market records, it comprises 18,246 meticulously annotated question-answering pairs across four task categories: metrics calculation, ticker selection, strategy selection, and parameter confirmation. We also propose AutoBacktest, a robust multi-agent baseline that translates natural language strategies into reproducible backtests by coordinating a Summarizer for semantic factor extraction, a Retriever for validated SQL generation, and a Coder for Python backtesting implementation. Our evaluation on 23 mainstream LLMs, complemented by targeted ablations, identifies key factors that influence end-to-end performance and highlights the importance of grounded verification and standardized indicator representations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决量化回测自动化过程中面临的高技术门槛和可扩展性不足的问题。尽管大型语言模型(LLM)在代码生成、工具使用和智能体规划方面展现了自动化复杂跨学科工作流的潜力，但当前缺乏专门用于自动化量化回测的大规模基准，严重阻碍了该领域的发展。

现有方法存在明显不足：传统的量化回测流程高度复杂且依赖专家经验，需要策略工程师精确构建因子组合、查询历史数据并编写无错误的回测代码，效率低下且难以规模化。同时，现有的代码生成或Text-to-SQL数据集无法捕捉量化回测中独特的时间序列逻辑和多步推理需求。

为弥合这一关键差距，本文提出了BacktestBench，这是首个专门为自动化量化回测设计的大规模基准。该基准基于超过600万条真实市场记录构建，包含18,246个精心标注的问答对，覆盖指标计算、标的筛选、策略选择和参数确认四类任务，旨在系统评估LLM在量化回测这一垂直领域的综合能力。

### Q2: 有哪些相关研究？

相关研究主要分为方法类、应用类和评测类。方法类工作中，**Automate Strategy Finding**和**QuantAgent**专注于因子挖掘与自改进交易智能体，但优先考虑盈利性而非代码执行的标准化与可重复性；**FinMem**关注交易决策的长期记忆，但忽略了复杂数据检索与指标计算的挑战；**AutoPrep**虽自动化表格数据预处理，但缺乏金融回测所需的时序逻辑以防止前瞻性偏差。应用类研究中，**TradeMaster**和**FinRL-Meta**为强化学习提供市场环境，但未评估可解释策略逻辑的生成；**FNSPID**将新闻与市场数据对齐，主要作为信息检索资源。评测类方面，**QuantEval**仅包含60个问题的策略编码评估，规模较小；**StockBench**侧重交易决策的盈利性；**Market-Bench**评估入门级策略的实现准确性。相比之下，本文提出的**BacktestBench**是首个大规模自动化量化回测基准，涵盖18,246个问答对，涉及指标计算、证券选择、策略选择和参数确认四类任务，并设计了**AutoBacktest**多智能体基线，系统评估从自然语言理解到SQL检索及回测执行的端到端流程，弥补了现有工作在回测严谨性、标准化和可验证性方面的不足。

### Q3: 论文如何解决这个问题？

论文提出AutoBacktest，一个多智能体框架，用于将自然语言策略自动转化为可复现的回测结果。整体框架由三个核心模块组成：Summarizer、Retriever和Coder，它们顺序协作，模拟量化研究员的工作流程。

首先，**Summarizer**负责语义解析。它使用大语言模型从用户自然语言策略中提取因子和KPI关键词，然后通过BM25检索机制将这些关键词与预定义的标准化指标库进行匹配，最终输出已验证的标准指标名称列表，以此消除自然语言歧义，确保后续模块使用统一的术语。

其次，**Retriever**构建数据层。它将Summarizer输出的指标名称映射为唯一的短代码（Short Code），这些短代码是紧凑的token效率标识符（如`DELAY(HIGH,1)-DELAY(EMA(CLOSE,13),1)`）。Retriever将短代码与原始策略文本作为上下文，提示LLM生成单条可执行的SQL查询语句，并在PostgreSQL数据库上执行验证循环，确保SQL运行成功且返回非空结果。这一设计结合了结构化检索与LLM的文本理解能力。

最后，**Coder**作为执行端点。它接收用户策略、指标上下文（名称+短代码）以及Retriever获取的数据预览（DataFrame的头尾行），在严格回测协议的提示下，调用Python执行工具，迭代式地编写、调试并运行代码来计算所需指标或执行策略逻辑。

关键创新点包括：1）**多智能体协同流水线**，将复杂的端到端任务分解为语义理解、数据检索和代码执行三个专业子任务，降低了LLM的推理复杂性；2）**基于验证的检索机制**，通过SQL执行验证和标准化指标短代码映射，将模糊的自然语言与精确的结构化数据库有效连接，避免了LLM的SQL幻视问题；3）**标准化的回测协议**，通过严格的交易规则（如T+1、按开盘价买入、收盘价卖出）和明确的计算定义，保证了回测结果的唯一性和可复现性。在BacktestBench基准上，该框架在23个主流LLM上的评估表明，标准化指标表示和验证机制是影响端到端性能的关键因素。

### Q4: 论文做了哪些实验？

本研究在BacktestBench基准上评测了23个主流大语言模型，涵盖开源与闭源两大阵营。实验设置包括三个核心任务：因子检索（使用准确率、精确率、召回率和F1分数）、SQL生成（计算可执行率和执行准确率EA）、以及四类策略回测问题（指标计算、股票选择、策略选择、参数确认），最终报告端到端整体准确率。关键发现：闭源模型Gemini 3 Pro以67.41%的整体准确率（OA）领先，在最具挑战的指标计算任务中获51.67%高分；最佳开源模型GLM 4.7的OA为56.83%，落后12.54个百分点。参数规模效应显著：Qwen3从235B降至4B时，指标计算得分从34.71%骤降至1.77%，而因子检索F1仅从94.18%下降至88.48%。非思维链模型Kimi Linear 48B呈现语法熟练与逻辑推理的显著脱节（可执行率99.22%但执行准确率仅48.46%）。消融实验证明Short Code机制可将SQL执行准确率提升超20个百分点，且包含Short Code的配置性能显著优于仅使用Gold SQL的配置，凸显语义锚点在策略生成中的关键作用。

### Q5: 有什么可以进一步探索的点？

**局限性与未来方向**  
现有的BacktestBench虽在规模上覆盖了回测核心任务，但数据来源仅为单市场记录（推测为股票），未纳入多资产（期货、期权、加密货币）或高频场景（Tick级数据）。其次，任务类型偏重单步代码生成（SQL/Python），缺乏对**策略演化**（如参数自适应调整、多周期鲁棒性验证）的评估。此外，AutoBacktest的“Summarizer→Retriever→Coder”级联模式易出现误差累积：若语义因子提取阶段遗漏关键趋势指标，后续SQL查询与代码实现将无法纠偏。  

**改进建议**：  
1. 引入**对抗性噪声注入**：在数据集中混入市场微观结构噪声，测试LLM对异常值（如闪崩、数据缺失）的鲁棒性。  
2. 设计**迭代修正机制**：让Coder生成代码后自动运行并对比基准结果，若回测指标（夏普比率、最大回撤）偏差超阈值，则触发Retriever重新检索替代参数。  
3. 扩展**时间序列因果推理**：要求模型不仅输出代码，还需给出“为何选用该策略参数”的因果链解释，例如通过反事实分析验证因子有效性。  

通过上述方向，可将基准从“单次代码生成”升级为“动态策略验证闭环”，更贴近量化研究员的实际决策过程。

### Q6: 总结一下论文的主要内容

本文提出了BacktestBench，这是首个专门用于自动化量化策略回测的大规模基准测试。回测是评估交易策略的核心环节，但传统方法技术门槛高、可扩展性差。该基准基于超过600万条真实市场记录，构建了涵盖指标计算、股票选择、策略选择和参数确认四类任务的18246个高质量问答对。同时，论文提出AutoBacktest框架，这是一个多智能体协作基线系统，通过协调摘要器进行语义因子提取、检索器生成验证过的SQL代码、编码器实现Python回测代码，将自然语言策略自动转化为可重现的回测流程。在23个主流大语言模型上的评估表明，该基准能有效识别影响端到端性能的关键因素，特别是验证机制和标准化指标表示的重要性。这项工作弥合了通用代码生成与量化投资研究之间的鸿沟，为智能金融决策领域奠定了坚实基础。
