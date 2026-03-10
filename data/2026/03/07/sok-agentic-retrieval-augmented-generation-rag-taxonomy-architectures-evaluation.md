---
title: "SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"
authors:
  - "Saroj Mishra"
  - "Suman Niroula"
  - "Umesh Yadav"
  - "Dilip Thakur"
  - "Srijan Gyawali"
  - "Shiva Gaire"
date: "2026-03-07"
arxiv_id: "2603.07379"
arxiv_url: "https://arxiv.org/abs/2603.07379"
pdf_url: "https://arxiv.org/pdf/2603.07379v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.CR"
  - "cs.IR"
tags:
  - "Agentic RAG"
  - "系统综述"
  - "架构分析"
  - "形式化建模"
  - "评估方法"
  - "风险分析"
  - "研究方向"
relevance_score: 8.0
---

# SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions

## 原始摘要

Retrieval-Augmented Generation (RAG) systems are increasingly evolving into agentic architectures where large language models autonomously coordinate multi-step reasoning, dynamic memory management, and iterative retrieval strategies. Despite rapid industrial adoption, current research lacks a systematic understanding of Agentic RAG as a sequential decision-making system, leading to highly fragmented architectures, inconsistent evaluation methodologies, and unresolved reliability risks. This Systematization of Knowledge (SoK) paper provides the first unified framework for understanding these autonomous systems. We formalize agentic retrieval-generation loops as finite-horizon partially observable Markov decision processes, explicitly modeling their control policies and state transitions. Building upon this formalization, we develop a comprehensive taxonomy and modular architectural decomposition that categorizes systems by their planning mechanisms, retrieval orchestration, memory paradigms, and tool-invocation behaviors. We further analyze the critical limitations of traditional static evaluation practices and identify severe systemic risks inherent to autonomous loops, including compounding hallucination propagation, memory poisoning, retrieval misalignment, and cascading tool-execution vulnerabilities. Finally, we outline key doctoral-scale research directions spanning stable adaptive retrieval, cost-aware orchestration, formal trajectory evaluation, and oversight mechanisms, providing a definitive roadmap for building reliable, controllable, and scalable agentic retrieval systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前Agentic RAG（智能体化检索增强生成）领域因快速发展而缺乏系统性认知和统一框架的问题。研究背景是，随着大语言模型能力的提升，传统的静态RAG系统（即一次性检索后生成）因其僵化的流程，在处理知识密集型或多跳推理任务时表现出脆弱性，例如存在检索盲目、缺乏纠错循环、上下文过载等问题。为了克服这些不足，业界开始探索动态、迭代的检索范式，并借助大语言模型的工具调用与规划能力，发展出能够自主协调多步推理、动态管理记忆和迭代检索策略的Agentic RAG架构。

然而，现有方法存在显著不足。尽管工业界采纳迅速，但当前研究对Agentic RAG作为一个序列决策系统缺乏系统性的理解，导致该领域架构高度碎片化、评估方法不一致，并且存在未解决的可靠性风险。具体表现为：缺乏统一的分类体系来厘清各种系统的设计模式；评估实践仍多局限于静态的答案质量指标，无法有效衡量动态决策轨迹的质量；同时，对自主循环中固有的系统性风险（如幻觉传播、记忆污染、检索错位等）认识不足。

因此，本文要解决的核心问题是：为Agentic RAG这一新兴范式提供一个系统化的知识梳理与统一框架。论文试图通过将其形式化为一个有限视野的部分可观测马尔可夫决策过程，来建立其理论基础；进而构建一个全面的多维度分类法和模块化架构分解，以厘清其设计空间；并深入分析传统评估方法的局限性与自主循环中的系统性风险，最终为构建可靠、可控、可扩展的Agentic RAG系统指明关键的研究方向。

### Q2: 有哪些相关研究？

本文梳理了与Agentic RAG相关的研究，主要可分为以下几类：

**1. 经典检索增强生成（RAG）与基础模型：** 这是Agentic RAG的起点。传统RAG系统（如基于DPR、FiD的方法）将检索与生成静态耦合，遵循“检索一次，生成一次”的固定流程。其局限性在于无法根据生成状态动态调整检索，对初始查询质量依赖过高。本文的Agentic RAG正是为了克服这种静态管道的脆弱性而提出的。

**2. 工具增强与智能体范式：** 将LLM视为能够与环境交互的智能体是另一条关键脉络。ReAct范式通过交错推理与行动（如API调用），实现了迭代信息收集。Toolformer让模型学习自主决定何时调用工具。MRKL系统提出了LLM作为路由器的模块化架构。这些工作确立了智能体的核心设计模式（规划、工具使用、反思），并直接为Agentic RAG系统所嵌入。

**3. 多步推理与查询分解：** 针对需要多步证据推理的任务（如HotpotQA），相关研究提供了规划机制的基础。方法包括查询分解、Least-to-most提示、Plan-and-Solve提示以及Self-Ask。更进一步，IRCoT、Tree-of-Thoughts等方法将检索与思维链生成紧密交织，利用演进的推理轨迹指导下一步检索，这为Agentic RAG的迭代检索-推理循环提供了直接基础。

**4. 记忆架构：** 有效的多步推理需要状态维护。相关研究涉及短时记忆（如动态上下文管理）和长时记忆系统（如基于检索的记忆、情景记忆），以及统一架构来动态管理工作记忆与持久存储。这些记忆机制是Agentic RAG实现状态追踪、区别于静态管道的关键前提。

**本文与这些工作的关系与区别：** 本文并非提出一种新方法，而是对上述分散在不同子领域的研究进行系统化知识梳理（SoK）。它首次将Agentic RAG作为一个**序列决策系统**进行统一形式化（建模为部分可观测马尔可夫决策过程），并在此基础上构建了涵盖规划、检索编排、记忆范式和工具调用行为的综合分类法与模块化架构分解。本文明确指出，现有研究缺乏对这种自主系统本质的系统性理解，导致了架构碎片化、评估方法不一致以及可靠性风险未被充分认识，而本文旨在填补这一空白并提供明确的研究路线图。

### Q3: 论文如何解决这个问题？

论文通过提出一个统一的形式化框架和系统化的分类法来解决Agentic RAG领域架构碎片化、评估方法不一致以及可靠性风险未解的问题。

核心方法是首先将Agentic RAG形式化为一个**有限视野的部分可观测马尔可夫决策过程**。该形式化将系统定义为一个元组，包括潜在环境状态、离散动作空间（检索、推理、工具调用、终止）、观测空间、观测函数、由LLM参数化的随机控制策略、作为可观测历史/信念状态近似值的动态工作记忆，以及潜在状态转移函数。这为理解其作为顺序决策系统的本质提供了严格的数学基础。

在整体架构设计上，论文构建了一个**模块化的架构分解**，核心包含三个关键角色：
1.  **规划器**：负责将复杂查询分解为子任务图。
2.  **控制器/推理引擎**：基于局部状态执行即时下一步行动。
3.  **编排器**：管理不同专用代理之间的输入输出路由。
这种设计明确分离了认知推理与工具执行，并通过闭环反馈确保最终输出的可靠性。

关键技术组件和创新点体现在提出的**四维分类法**上，该系统地对现有架构进行归类：
1.  **规划拓扑**：区分单代理、规划器-执行器、多代理系统，明确了决策实体的分布方式。
2.  **检索策略**：涵盖一次性检索、迭代检索和自优化检索，定义了检索动作如何依赖于系统状态动态触发。
3.  **推理范式**：分类为思维链、ReAct式交错、基于反思的推理以及基于树的探索，描述了多步推理如何驱动工具调用。
4.  **记忆与上下文管理**：包括动态上下文修剪、情景记忆和持久长时记忆，解决了跨步骤和会话的状态持久化问题。

此外，论文的创新在于明确区分了**主动RAG**与**Agentic RAG**，指出前者本质仍是单次生成过程，而后者是策略驱动的、分离规划与生成的多步骤规划循环，具备对工作内存的读/写/修剪能力以及自我纠正能力。通过这种形式化、分类和模块化分解，论文为构建可靠、可控、可扩展的Agentic RAG系统提供了清晰的理论框架和工程蓝图。

### Q4: 论文做了哪些实验？

该论文作为一篇系统综述（SoK），并未进行具体的实验，而是对现有研究进行了系统性梳理、分类与分析。其主要工作包括：

**实验设置/分析框架**：论文将智能体化检索增强生成（Agentic RAG）形式化为一个**有限视野的部分可观测马尔可夫决策过程**，以此作为统一的理论框架来分析其决策循环、控制策略和状态转移。

**数据集/基准测试分析**：论文并未引入新数据集，但**批判性地分析了当前评估方法的局限性**。它指出，传统的静态评估（如基于单个问题/答案对）无法有效衡量Agentic RAG在多步推理、长期交互中的性能，并强调了开发**轨迹级评估方法**的必要性。

**对比方法与分类（即提出的分类法）**：论文提出了一个全面的模块化架构分类体系，用于系统性地对比和理解不同的Agentic RAG系统。该分类法主要依据四个核心维度进行归类：
1.  **规划机制**：如链式思考、任务分解。
2.  **检索编排**：如迭代检索、自适应检索。
3.  **记忆范式**：如短期工作记忆、长期知识存储。
4.  **工具调用行为**：如如何集成和执行外部工具。

**主要结果与关键发现**：
1.  **架构梳理**：提供了首个对Agentic RAG系统的统一分类与架构分解。
2.  **风险识别**：系统性地揭示了自主循环中固有的严重系统性风险，包括**幻觉传播复合、记忆污染、检索错位以及工具执行漏洞级联**。
3.  **评估批判**：明确指出当前评估实践与系统实际动态行为脱节。
4.  **研究路线图**：提出了未来关键研究方向，如稳定自适应检索、成本感知编排、形式化轨迹评估和监督机制，为构建可靠、可控、可扩展的智能体化检索系统指明了道路。

### Q5: 有什么可以进一步探索的点？

该论文指出当前Agentic RAG研究存在架构碎片化、评估方法不一致及可靠性风险未解决等核心局限。未来可深入探索的方向包括：首先，开发动态、自适应的检索机制，使系统能根据任务进展和反馈实时调整检索策略，而非依赖固定模式，以缓解检索错位和幻觉传播问题。其次，设计成本感知的协调框架，在多步骤推理中权衡计算开销、检索精度与生成质量，实现高效资源分配。再者，需建立形式化的轨迹评估方法，对智能体的决策序列进行可解释的量化分析，以系统性检测记忆污染或工具执行漏洞等级联风险。最后，引入强健的外部监督机制，如实时一致性校验或安全护栏，确保自主循环的可控性与稳定性。这些方向将推动Agentic RAG从实验性架构迈向可靠的实际应用系统。

### Q6: 总结一下论文的主要内容

本文针对新兴的智能体化检索增强生成（Agentic RAG）领域，首次提供了一个系统化的知识梳理与统一框架。核心问题是：当前工业界快速采用的Agentic RAG系统缺乏统一的理论理解、导致架构碎片化、评估方法不一致且存在可靠性风险。

论文的主要贡献在于：首先，将Agentic RAG形式化为一个有限视野的部分可观测马尔可夫决策过程，对其控制策略和状态转移进行了显式建模。其次，基于此形式化，提出了一个全面的分类法和模块化架构分解，从规划机制、检索编排、记忆范式和工具调用行为等维度对现有系统进行分类。论文还深入分析了传统静态评估方法的局限，并指出了自主循环中固有的系统性风险，如复合幻觉传播、记忆污染、检索错位和级联工具执行漏洞等。

主要结论是，Agentic RAG代表了一种从静态“检索-生成”流程向模块化、基于策略的多步推理轨迹的根本性转变。论文最后为构建可靠、可控、可扩展的智能体化检索系统，指明了涵盖稳定自适应检索、成本感知编排、形式化轨迹评估和监督机制等关键研究方向。
