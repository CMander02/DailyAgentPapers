---
title: "EXG: Self-Evolving Agents with Experience Graphs"
authors:
  - "Yuxin Jin"
  - "Siyuan Zhang"
  - "Hanchen Wang"
  - "Lu Qin"
  - "Ying Zhang"
  - "Wenjie Zhang"
date: "2026-05-18"
arxiv_id: "2605.17721"
arxiv_url: "https://arxiv.org/abs/2605.17721"
pdf_url: "https://arxiv.org/pdf/2605.17721v1"
categories:
  - "cs.AI"
tags:
  - "self-evolving agent"
  - "experience graph"
  - "structured memory"
  - "online learning"
  - "offline reuse"
  - "code generation"
  - "reasoning"
  - "LLM agent"
relevance_score: 9.5
---

# EXG: Self-Evolving Agents with Experience Graphs

## 原始摘要

Large language model (LLM)-based agents have demonstrated strong capabilities in complex reasoning and problem solving through multi-step interactions, yet most deployed agents remain behaviorally static, with knowledge acquired during execution rarely translating into systematic improvement over time. In response, a growing line of work on self-evolving agents explores how agents can improve through experience during deployment, but most existing approaches either rely on ad hoc reflection limited to single-task correction or adopt unstructured memory that accumulates fragmented experience with delayed usability. To address this limitation, we introduce EXG, an experience graph framework for self-evolving agents that explicitly organizes accumulated successes and failures into a structured, relational representation. EXG is the first experience graph designed for self-evolving agents, supporting both online, real-time graph growth during execution for immediate cross-task experience reuse, and offline reuse of a consolidated experience graph as an external memory module. This design also enables EXG to serve as a plug-and-play component for existing self-evolving agents, organizing prior experience into a unified experience graph and improving both solution quality and resource efficiency as deployment progresses. Extensive experiments across code generation and reasoning benchmarks show that EXG attains more favorable performance-efficiency trade-offs than reflection- and memory-based baselines in both online and offline evaluations. Our results suggest that structuring experience as a graph provides a principled foundation for scalable and transferable self-evolving agent behavior.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于大语言模型的智能体在部署过程中缺乏自我进化能力的问题。研究背景是，现有智能体虽然在复杂推理和问题解决上表现出色，但大多行为静态，执行中获得的知识很少能转化为系统性的性能提升。现有方法的不足主要体现在两个方面：一是多数方法依赖临时的反思机制，仅限于单一任务的修正，缺乏跨任务的可迁移性；二是采用非结构化记忆，积累碎片化经验，导致复用延迟。本文要解决的核心问题是，如何设计一种结构化、可复用的经验表示框架，使智能体能够在部署中通过持续积累和复用成功与失败经验，实现自我进化。为此，论文提出了EXG，一种经验图框架，将经验组织为包含案例节点、任务锚点节点以及多种关系边（包含、相似、修正）的有向图，支持在线实时积累和离线静态度量，从而提升解决方案质量和资源效率。

### Q2: 有哪些相关研究？

相关研究可分为三大类：**参数更新方法**、**非参数推理方法**和**Agent记忆系统**。参数更新方法通过迭代训练或强化学习将经验内化到模型参数中，实现持续改进，但代价是重训练开销和模块性降低；本文采用的非参数方法则避免此问题。非参数方法进一步分为在线和离线两类：在线方法如reflexion或轨迹级优化主要针对单个任务进行行为修正，缺乏跨任务经验复用；离线方法则通过外部记忆或经验库积累跨任务经验，但通常采用平面或弱结构化的表示，且需要大量离线精炼才能复用。与之相比，本文提出的EXG利用经验图显式组织成功与失败经验，既支持在线实时图增长以实现即时跨任务复用，又支持离线复用作为外部记忆模块。此外，Agent记忆系统研究如何将外部记忆融入长程交互，但多数方法将记忆视为辅助信息源，侧重检索与提示注入，而非建模经验驱动的行为演化。EXG的独特性在于它是首个专为自演化Agent设计的经验图框架，通过结构化关系表示克服了先前无结构化记忆的碎片化与延迟可用性，可作为即插即用组件提升现有自演化Agent的解决方案质量和资源效率。

### Q3: 论文如何解决这个问题？

EXG通过经验图框架实现自我进化，核心是将代理的交互轨迹抽象为结构化案例，并组织成有向图。整体框架包含三个主要组件：

**经验图构建**：将每次任务尝试的完整轨迹压缩为案例节点，包含任务输入、输出、成功标志和关键执行信号(如错误信息)。成功案例为黄金节点，失败案例为警告节点。每个任务设有锚点节点，通过包含边关联所有相关案例。案例间建立相似边(基于语义嵌入)和修正边(记录同一任务中错误与修复的关系)。

**检索与重排序**：接收当前部分案例(仅有任务输入)后，通过三种互补路径检索相关案例：任务锚点下的本地案例、基于相似边的语义种子扩展(包括查询侧种子和桥接种子)、沿修正边的纠正轨迹。召回案例经重排序，通过结合提示语义相似度和故障感知相似度的评分函数，并沿相似边进行一轮传播，最终选择最高分案例构建提示：优先考虑修复提示(含错误修复关系)、其次警告提示(失败模式)、最后黄金提示(成功示范)。

**自我进化闭环**：在线模式中，检索指导的代理执行产生新案例，实时加入图结构并建立包含边、修正边和相似边，使经验立即用于后续任务。离线模式复用预先构建的冻结图，不进行更新。该框架可作为即插即用模块，无需修改模型参数，仅通过结构化经验组织即可提升解决方案质量和资源效率。

### Q4: 论文做了哪些实验？

论文在代码生成和推理两类基准上评估了EXG框架。实验设置包括HumanEval、EvalPlus（代码生成）、MuSiQue和HotpotQA（多跳问答），使用Qwen3系列模型（1.7B、8B、14B、Coder-Flash、Plus、Max）。对比方法包括在线自演进基线Reflexion和SE-Agent及其简化版SE-Agent-Rev，以及EXG与这些基线插拔式结合的变体（EXG-Reflexion、EXG-SE、EXG-SE-Rev）。离线对比采用ExpeL基线。

主要在线实验结果（pass@1/pass@2）：在HumanEval上，Qwen3-1.7B下EXG达到0.537/0.585，比Reflexion（0.207/0.543）提升超过150%的pass@1；Qwen3-Coder-Flash下EXG达到0.805/0.835，比最强非图基线高30%以上。在EvalPlus上，Qwen3-8B下EXG为0.409/0.530，优于Reflexion的0.183/0.274。MuSiQue上Qwen3-14B下EXG-Reflexion达0.480/0.748，提升约40-50%。HotpotQA上Qwen3-8B下EXG为0.460/0.500，提升超60%。效率方面，EXG平均LLM调用次数比Reflexion降低34.4%（HumanEval 1.20 vs 1.83），推理延迟降低4.6%-30.5%，检索开销仅18-22ms。

离线实验：EXG-Reflexion在在线收集阶段HumanEval上pass@1达0.824（ExpeL为0.573），平均调用1.35次（ExpeL为1.85）；测试阶段pass@1为0.879，略低于ExpeL的0.909。

### Q5: 有什么可以进一步探索的点？

EXG将经验组织为图结构确实是一个有前途的尝试，但当前框架仍存在若干可深入探索的方向。首先，图结构的动态扩展策略目前较为简单，未来可引入更智能的节点合并与剪枝机制，避免存储冗余或冲突的经验，同时控制图规模膨胀带来的计算开销。其次，EXG的经验组织主要以“任务-步骤”为粒度，缺乏对底层推理逻辑的抽象；作者可以探索通过元学习或因果推断，从成功/失败路径中提炼出通用的任务分解模式或决策规则。第三，当前离线阶段的图复用是静态的，未来可引入持续学习机制，使冻结的图在接触新任务时能自适应地调整节点权重或关系。最后，跨领域迁移能力有待评估，目前的实验集中在代码生成和推理，能否将图经验迁移到如机器人控制、对话系统等差异较大的领域，以及如何设计领域无关的索引与检索策略，是一个重要的开放问题。

### Q6: 总结一下论文的主要内容

本文介绍了 EXG，一种面向自演进智能体的经验图框架。其核心问题是解决现有智能体在执行过程中知识难以系统积累和复用的局限，即现有方法多依赖单任务反思或非结构化记忆，导致经验碎片化且复用延迟。EXG 方法将积累的成功与失败经验显式组织为结构化的、基于关系的经验图，支持在线执行时实时增长以实现跨任务经验复用，以及离线时将固化经验图作为外部记忆模块复用。它还可作为即插即用组件整合现有智能体的历史经验。在代码生成和推理基准上的大量实验表明，EXG 在在线和离线评估中均比基于反思或记忆的基线方法取得了更优的性能-效率权衡，在更少的模型调用下实现更高任务成功率，并降低推理时间。主要结论是，将经验结构化为图为可扩展、可迁移的自演进智能体行为提供了原则性基础，使改进能持续累积而非随任务重置。
