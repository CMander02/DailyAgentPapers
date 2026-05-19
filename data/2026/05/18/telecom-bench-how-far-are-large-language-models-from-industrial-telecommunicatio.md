---
title: "TeleCom-Bench: How Far Are Large Language Models from Industrial Telecommunication Applications?"
authors:
  - "Jieting Xiao"
  - "Yun Lin"
  - "Huizhen Qiu"
  - "Rui Ma"
  - "Chen Zhong"
  - "Dongyang Xu"
  - "Xiao Long"
  - "Chaoyu Zhang"
  - "Qiaobo Hao"
  - "Ding Zou"
  - "Zhiguo Yang"
  - "Yanqin Gao"
  - "Fang Tan"
date: "2026-05-18"
arxiv_id: "2605.18025"
arxiv_url: "https://arxiv.org/abs/2605.18025"
pdf_url: "https://arxiv.org/pdf/2605.18025v1"
github_url: "https://github.com/ZTE-AICloud/TeleCom-Bench"
categories:
  - "cs.AI"
tags:
  - "Telecom Agent"
  - "LLM Benchmark"
  - "Knowledge Graph"
  - "Domain-specific Agent"
  - "Industrial Application"
relevance_score: 8.0
---

# TeleCom-Bench: How Far Are Large Language Models from Industrial Telecommunication Applications?

## 原始摘要

While Large Language Models have achieved remarkable integration in various vertical scenarios, their deployment in the telecommunications domain remains exploratory due to the lack of a standardized evaluation framework. Current telecom benchmarks primarily focus on static, foundational knowledge and isolated atomic skills, neglecting the equipment-specific documentation and end-to-end industrial workflows essential for real-world production systems. To bridge this gap, we present TeleCom-Bench, a comprehensive benchmark comprising 12 evaluation sets with 22,678 curated samples, which evaluates LLMs across a synergistic hierarchy: (1) Multi-dimensional Knowledge Comprehension, which integrates telecommunication fundamentals, 3GPP protocols, and 5G network architecture with proprietary product knowledge across wired, core, and wireless networks via knowledge graph-driven synthesis; and (2)End-to-End Knowledge Application, which formalizes six core tasks on authentic trajectories from live network agent workflows, including intent recognition, entity extraction, event verification, tool invocation, root cause analysis, and solution generation-across network optimization and fault maintenance scenarios. Evaluations of eight state-of-the-art LLMs reveal a universal Execution Wall: while models achieve 90% accuracy in linguistic interface tasks such as intent recognition and entity extraction, performance collapses to approximately 30% in procedural execution tasks like solution generation. This capability gap demonstrates that current LLMs function competently as diagnosticians but fail as field engineers. TeleCom-Bench provides standardized diagnostics to precisely pinpoint this deficit, offering actionable guidance for domain-specific alignment toward production-ready telecom agents. The dataset and evaluation code have been released at https://github.com/ZTE-AICloud/TeleCom-Bench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在电信工业场景中缺乏标准化评估框架的问题。虽然LLM已在医疗、金融等领域取得应用，但在电信领域仍处于探索阶段。现有基准测试（如SPEC5G、TeleQnA）存在两大不足：一是主要关注3GPP标准等静态理论知识，忽视了实际网络设备的产品手册、技术专利等设备专属文档，导致理论理解与操作现实脱节；二是仅评估意图识别、实体提取等原子化技能，无法模拟网络优化、故障诊断等端到端工业流程所需的多步推理与因果分析能力。核心问题在于当前评估体系无法量化LLM是否具备电信运营所需的专业智能——即从掌握设备规格到生成可执行工程方案的完整能力链。为弥合这一鸿沟，本文提出TeleCom-Bench基准，通过构建知识图谱驱动的多维度知识理解测试（融合基础理论、3GPP协议与产品知识）和基于真实运维轨迹的端到端应用任务（涵盖意图识别、根因分析、解决方案生成等6项核心任务），系统评估LLM在电信领域的实用化水平。

### Q2: 有哪些相关研究？

相关研究主要分为两类。**电信领域基准**方面，从早期基于通用协议理解的SPEC5G、TeleQnA，到扩展任务多样性的TSpec-LLM、ORAN-Bench-13K、TelecomGPT，再到关注操作垂直领域的TeleTables、TeleLogs、OpsEval、TeleYAML等，这些工作建立了从术语理解到操作应用的分层评估体系。本文与它们的核心区别在于：1）克服了现有基准的任务碎片化问题，通过知识图谱驱动整合了产品专有知识；2）首次基于真实运维工作流轨迹构建端到端评估，而非依赖孤立的公共标准数据。**基准构建方法论**方面，现有电信基准多依赖LLM生成或模板合成，缺乏领域专家深度参与和真实操作序列建模。相比之下，金融领域的CNFinBench和医疗领域的MedBench展示了高风险场景下基准构建的三个关键支柱：专家深度参与、基于真实操作序列、显式建模工具辅助的多步执行。本文是首个满足这些方法论要求的电信基准，通过整合供应商专有文档和真实代理工作流轨迹，填补了工业部署就绪性评估的空白。

### Q3: 论文如何解决这个问题？

该论文通过构建双层次评估体系解决当前大语言模型在电信工业应用中的评估缺失问题。核心方法包括知识理解与知识应用两个维度：

1. **知识理解层面**设计了完整的知识理解流水线。首先建立多源数据采集框架，整合3GPP协议、IETF RFC等标准化文档与产品手册、现场案例等工业数据，形成1.52TB异构语料。随后通过统一预处理流水线实现格式归一化（多模态OCR处理）、语料净化（语义去重与层级分割）和结构化标注（安全标签与质量标签）三阶段处理。在此基础上提出任务自适应LLM知识蒸馏方法，针对四种文档类型设计不同生成策略：对技术标准采用范式约束抽取生成封闭域槽填充任务；对设备手册采用层级结构生成转为JSON解析任务；对学术论文采用渐进式提示链挖掘实现深层认知推理；对异构文档采用跨文档知识图谱拓扑合成实现多源融合。最终通过场景图结构设计（装备层级树+故障因果链）、图遍历多粒度QA合成（原子/多跳/聚合三类）、GraphRAG质量修正和基于子图差异的干扰项生成四个步骤构建包含17,442个样本的知识理解评估集。

2. **知识应用层面**从真实商业网络采集性能管理（15分钟时序KPI）、配置管理（拓扑快照）和故障管理（事件日志）三类数据，经过隐私保护ETL处理后，采用Agent-in-the-Loop范式让领域智能体在真实网络数据环境中执行任务，通过轨迹挖掘技术提取6个核心任务（意图识别、实体抽取、事件验证、工具调用、根因分析和方案生成）的输入-推理-动作三元组，最终形成5,236个端到端应用评估样本。

该工作创新点在于：(1)提出知识图谱驱动的电信场景评估基准构建方法，通过显式建模知识关联消除幻觉；(2)揭示大语言模型在电信领域的执行壁垒(Execution Wall)，即语言接口任务（意图识别90%准确率）与过程执行任务（方案生成仅30%准确率）间的显著能力落差；(3)建立从理论协议到设备知识再到现场工作流的完整评估层次，超越传统静态知识测试框架。

### Q4: 论文做了哪些实验？

该论文在TeleCom-Bench基准上评估了8个代表性大语言模型（Qwen3-32B、Qwen3-235B、DeepSeek-V3.2、Gemini2.5、Grok4.1、GLM-4.7、Doubao-pro、Kimi K2）。实验设置统一：温度0.7，启用推理模式，每个实例进行3次独立采样后多数投票。评测涵盖两个层次：(1) 知识理解，包括基础理论、有线网络、无线网络和核心网络4个数据集；(2) 知识应用，包括意图识别、实体抽取、事件验证、工具调用、根因诊断和方案生成6个任务。共12个评测集，22,678个样本。指标方面：多选题采用Macro-F1，结构化问答采用精确匹配，开放式回答采用三专家LLM评分（5点李克特量表，Krippendorff's α=0.82）。主要结果：(1) 知识理解方面，模型表现中等（60%-70%），其中Qwen3-32B在无线网络上反超Qwen3-235B（73.04% vs 70.80%）；(2) 知识应用揭示出显著的"执行鸿沟"：在意图识别和实体抽取上模型达90%以上精度，但方案生成性能骤降至约30%，最佳Doubao-pro也仅30.72%。最典型的是Qwen3-235B：根因诊断71.49%而方案生成仅4.67%，差距达66.82个百分点，表明当前LLM胜任"诊断师"角色但远未达到"现场工程师"水平。

### Q5: 有什么可以进一步探索的点？

论文揭示了LLMs在电信领域“诊断强、执行弱”的Execution Wall现象，但当前基准仍存在若干可探索方向。首先，知识维度可进一步扩展：现有评估聚焦于静态知识，未纳入电信网络动态演化的实时配置（如网络切片更新）或跨厂商设备互操作场景。其次，任务流程可更贴近人机协作：未来可探索多轮对话中的渐进式故障排除，或引入安全约束下的动作修正机制（如自动回滚错误指令）。此外，当前评测侧重单模型性能，可研究模型集成或检索增强生成（RAG）如何弥补知识短板。值得关注的是，是否可通过设计分层奖励机制（如过程奖励模型）逐步对齐专业工作流，以突破执行鸿沟。最后，建议引入对抗性测试（如噪声输入、边缘案例）评估鲁棒性，并探索少量专家数据微调是否能高效迁移到新设备协议。

### Q6: 总结一下论文的主要内容

大型语言模型（LLM）在垂直领域取得进展，但在电信行业的应用缺乏标准化评估。为此，TeleCom-Bench 基准应运而生，它包含12个评估集和22,678个样本。该基准构建了一个协同层次：（1）多维知识理解，通过知识图谱驱动，整合电信基础、3GPP协议及5G网络架构与有线、核心、无线网络的专有产品知识；（2）端到端知识应用，基于真实网络运维轨迹，形式化意图识别、实体抽取、事件验证、工具调用、根因分析与方案生成六大核心任务。评估8个顶尖LLM发现普遍存在“执行壁垒”：模型在意图识别等语言接口任务上准确率达90%，但在方案生成等流程执行任务上骤降至约30%。这表明当前LLM是优秀的“诊断师”，却无法胜任现场工程师角色。TeleCom-Bench提供了标准化诊断，精准定位这一缺陷，为构建生产级电信智能体提供了可操作的领域对齐指导。
