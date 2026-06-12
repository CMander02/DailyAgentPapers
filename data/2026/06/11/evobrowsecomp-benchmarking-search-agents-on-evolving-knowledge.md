---
title: "EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge"
authors:
  - "Yunhan Wang"
  - "Jiaan Wang"
  - "Lianzhe Huang"
  - "Xianfeng Zeng"
  - "Fandong Meng"
date: "2026-06-11"
arxiv_id: "2606.13120"
arxiv_url: "https://arxiv.org/abs/2606.13120"
pdf_url: "https://arxiv.org/pdf/2606.13120v1"
categories:
  - "cs.CL"
tags:
  - "Search Agent"
  - "Agent Benchmark"
  - "Data Contamination"
  - "Live-Web Knowledge"
  - "Multi-Agent Collaboration"
  - "Reasoning Graph"
  - "Evolving Knowledge"
relevance_score: 9.5
---

# EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge

## 原始摘要

Search Agents -- large language models augmented with search tools -- have intensified the need for future-proof evaluation benchmarks. Existing benchmarks such as BrowseComp rely on static knowledge, making them vulnerable to test-set contamination and parametric memorization. Consequently, models can achieve high scores through fact recall rather than genuine retrieval, obscuring true browsing competence via reasoning shortcuts.
  In this paper, we introduce EvoBrowseComp, an evolving benchmark of 400 English and 400 Chinese contamination-free complex questions synthesized via live-web traversal. To collect these questions, we design a three-agent collaborative framework: (1) a QA synthesis agent that retrieves fresh knowledge from the live web to synthesize QA pairs; (2) an information filtering agent that filters retrieved knowledge in terms of credibility and popularity to block parametric shortcuts; and (3) a high-level guidance agent that formalizes questions into reasoning graphs to reduce logical redundancy and shortcuts in synthesized QA pairs. Because the framework supports fully automated synthesis, EvoBrowseComp can be regularly updated to prevent data contamination and maintain temporal freshness. Extensive experiments confirm its great difficulty, requiring broad horizontal search. It establishes a scalable paradigm for auto-updatable, high-difficulty benchmarking that keeps pace with both evolving world knowledge and advancing agent capabilities.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有搜索智能体基准测试（如BrowseComp）因依赖静态知识而导致的数据污染问题。研究背景是，大语言模型结合搜索工具后，在信息检索任务上表现优异，但现有基准测试（如BrowseComp、GAIA、DeepSearchQA等）均基于固定时间点的静态知识构建，使得模型可能通过参数记忆（即预训练语料中已包含的答案）而非真正的检索与推理能力来获得高分。这种静态特性导致基准测试极易受到测试集污染——随着训练数据扩展，基准内容会泄露到模型参数中，使模型通过推理捷径（parametric shortcuts）掩盖真实的浏览能力。本文的核心问题是：如何构建一个能够抵抗数据污染、真正评估模型多跳检索与推理能力的动态基准测试。为此，论文提出了EvoBrowseComp，一种从实时网页遍历中自动合成的新基准，包含400个英文和400个中文复杂问题，通过三智能体协作框架（QA合成、信息过滤、高级引导）确保问题涉及新鲜知识、避免参数记忆，并可低成本持续更新。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要包括以下几类：

**（一）评测类基准**

- **早期事实检索数据集**：如 NaturalQuestions、TriviaQA、HotpotQA，主要用于单跳或多跳事实检索，但已被现有大语言模型轻松应对。
- **高难度浏览基准**：BrowseComp 及其变体（如人工验证语料库的 BrowseComp-Plus、中文扩展的 BrowseComp-ZH）强调搜索的持久性和创造力；WebWalkerQA 侧重结构化网站垂直遍历；GAIA 提出概念简单但执行复杂的多工具、多步规划任务；DeepSearchQA 从单答案检索转向穷举集合生成；SealQA 关注检索结果冲突、噪声和误导下的鲁棒性。

**（二）本文与现有工作的区别**

现有基准多依赖**静态或固定语料**，易受“测试集污染”和“参数化记忆”影响——模型可通过事实回忆而非真正的检索/推理达到高分。本文提出的 **EvoBrowseComp** 通过**三智能体协作框架**（QA 合成、信息过滤、高层次指导）从**实时网络**自动合成免污染、高难度问题（400 英文 + 400 中文），支持定期更新以保持时间新鲜度，且无需昂贵的人工标注。这使得评估更能反映智能体在**不断演变的世界知识**下的真实浏览与推理能力，而非依赖静态知识库。

### Q3: 论文如何解决这个问题？

EvoBrowseComp通过设计一个三智能体协同框架，实现了一个全自动、可持续演化的基准测试构建方法，以解决现有基准因依赖静态知识而易受测试集污染和参数记忆影响的问题。

整体框架是一个迭代反馈循环，主要由以下三个核心模块协作完成：

1.  **QA合成智能体**：从实时网络中搜索新鲜知识（设定在指定时间戳后出现的信息），为种子实体构建包含证据列表的复杂问答对。它通过多轮网页交互收集知识，并区分新鲜与非新鲜证据，最终答案仅基于新鲜知识，并通过混淆特征（如模糊时间参考）提升难度。

2.  **信息过滤智能体**：对合成智能体收集的证据进行质量筛选。对于新鲜证据，通过联网交叉验证其可靠性；对于非新鲜证据，评估其流行度，过滤掉“不可靠”或“过度覆盖”的知识，防止模型通过参数记忆或推理捷径作答。

3.  **高级指导智能体**：将候选问题解析为逻辑推理图（使用交集、补集、投影等操作），自动检测图中的推理冗余（孤立节点）和捷径（结构旁路）。基于检测结果生成指导指令，反馈给QA合成智能体，引导其在下一轮迭代中优化问题，避免逻辑缺陷。

该框架的创新点在于：(1) **全自动持续更新**：通过定期从网络重新采集知识并退役暴露问题，无需人工维护；(2) **反污染设计**：严格依赖新鲜知识，并通过流行度过滤阻断参数记忆捷径；(3) **结构化的质量控制**：利用推理图显式控制推理路径的复杂性和逻辑完整性。最终，经过文本质量、唯一性和难度筛选，生成了400个英文和400个中文的高难度、无污染的复杂问答对。

### Q4: 论文做了哪些实验？

论文在EvoBrowseComp基准上进行了全面实验。实验设置包括：在数据收集中使用DeepSeek-V3.2作为三智能体协作框架的基础模型，信息过滤代理的预定义阈值k设为5；模型评估时所有开源LLM在NVIDIA H20 GPU上部署，采用采样解码（温度0.6，top_p 0.95），最大上下文长度128K，最大工具调用次数40次，并使用GLM-5-Chat作为评判模型，每个LLM独立运行三次取平均。评估的模型包括Claude-Opus-4.6、Qwen3.5系列、DeepSeek系列、GLM-5和Kimi-K2.6等。两个子数据集分别为400个英文和400个中文问题。

主要结果：
- **无工具设置**：大多数LLM准确率低于5%，最佳模型DeepSeek-V3.2仅达6.3%（英文）和10.3%（中文），表明EvoBrowseComp有效防止参数化记忆。
- **工具设置**：英文方面，Claude-Opus-4.6以44.8%准确率排名第一，其次是Qwen3.5-397B（42.0%）和GLM-5（39.2%）。中文结果趋势相似。
- **与BrowseComp对比**：模型在EvoBrowseComp上的性能显著低于BrowseComp，例如DeepSeek-V3.2在英文上从51.4%降至23.0%，在中文上从65.0%降至30.5%，说明新基准难度更高。
- **推理努力的影响**：DeepSeek-V4-Flash在三种配置中，高推理设置表现最佳（英文34.5%），而最大推理设置因超过工具调用限制（英文ER达75.5%）反而最差，突显推理效率的重要性。

### Q5: 有什么可以进一步探索的点？

根据论文内容和分析，进一步探索的点包括：首先，当前框架依赖DeepSeek-V3.2作为骨干模型，可能引入模型自身的偏见和有害行为，未来可集成多模型校验机制，例如使用不同架构的LLM进行交叉验证，以增强合成数据的鲁棒性。其次，评估仅基于最终答案而非完整推理轨迹，这会导致难以区分真实推理能力与偶然正确（如幸运猜测），后续可设计分步推理审计接口或过程奖励模型，对每个搜索步骤和中间推理进行量化打分。此外，当前仅覆盖英文和中文，未来需扩展至多语言及低资源场景；同时可探索增量式知识图谱构建，使基准能够自适应跟踪事件的时间演变，避免静态更新偏差。还可引入对抗性测试用例，专门探测模型利用检索捷径（如记忆偏见）的倾向，从而更精确地分离检索能力与记忆依赖。

### Q6: 总结一下论文的主要内容

EvoBrowseComp 是一个针对搜索智能体的动态基准测试，旨在解决现有基准（如 BrowseComp）因依赖静态知识而容易受到测试集污染和参数记忆影响的问题。论文定义了通过实时网络遍历合成无污染复杂问题的新任务。方法上，提出了一个三智能体协作框架：QA 合成智能体从实时网页获取新鲜知识生成问答对；信息过滤智能体通过评估可信度和流行度阻止参数化捷径；高层次指导智能体将问题形式化为推理图，减少逻辑冗余。实验表明，该基准具有高难度，需要广泛的水平搜索能力。核心贡献在于建立了一个可自动更新、抗污染、高难度的可扩展评估范式，能随世界知识和智能体能力进化而保持时效性，为搜索智能体的未来评估提供了可持续方案。
