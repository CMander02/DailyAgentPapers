---
title: "Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents"
authors:
  - "Shuo Ji"
  - "Yibo Li"
  - "Bryan Hooi"
date: "2026-06-04"
arxiv_id: "2606.06036"
arxiv_url: "https://arxiv.org/abs/2606.06036"
pdf_url: "https://arxiv.org/pdf/2606.06036v1"
categories:
  - "cs.AI"
  - "cs.IR"
tags:
  - "LLM Agent"
  - "Memory Management"
  - "Graph Memory"
  - "Active Reconstruction"
  - "Long-horizon Reasoning"
  - "Retrieval-Augmented Agent"
relevance_score: 9.0
---

# Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents

## 原始摘要

Despite recent progress, LLM agents still struggle with reasoning over long interaction histories. While current memory-augmented agents rely on a static retrieve-then-reason paradigm, this rigid pipeline design prevents them from dynamically adapting memory access to intermediate evidence discovered during inference. To bridge this gap, we propose MRAgent, a framework that combines an associative memory graph with an active reconstruction mechanism. We represent memory as a Cue-Tag-Content graph, where associative tags serve as semantic bridges connecting fine-grained cues to memory contents. Operating on this structure, our active reconstruction mechanism integrates LLM reasoning directly into memory access, allowing the agent to iteratively explore and prune retrieval paths based on accumulated evidence. This ensures that memory retrieval is dynamically adapted to the reasoning context while avoiding combinatorial explosion caused by unconstrained expansion. Experiments on the LoCoMo benchmark and LongMemEval benchmark demonstrate significant improvements over strong baselines (up to 23%), while substantially reducing token and runtime cost, highlighting the effectiveness of active and associative reconstruction for long-horizon memory reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决LLM智能体在长时间交互历史中进行推理时面临的记忆访问僵化问题。研究背景是，尽管大语言模型在数学、推理等任务上表现出色，但在需要长期记忆的交互式场景（如智能助手、决策支持系统）中，受限于有限的上下文窗口，难以有效利用历史交互信息。现有方法通常采用检索增强生成（RAG）或知识图谱等外部记忆系统，但这些系统大多遵循静态的“先检索后推理”范式，记忆检索是固定且被动的：它们依赖固定的top-k选择或预定义的子图遍历，无法根据推理过程中发现的中间证据动态调整访问策略。例如，当需要推断用户七月份的活动时，被动检索只能返回与“视频游戏锦标赛”直接相关的内容，而无法主动推理出时间线索“七月”并进行关联记忆。为此，本文提出MRAgent框架，核心创新在于将记忆访问与LLM推理深度整合，实现主动与关联的记忆重构。具体地，它构建了“线索-标签-内容”（Cue-Tag-Content）的记忆图结构，其中标签作为语义桥梁连接细粒度线索与记忆内容；并设计了主动重构机制，允许智能体基于累积证据迭代探索和剪枝检索路径，避免组合爆炸的同时动态适应推理上下文。最终目标是将静态、被动的记忆检索转变为动态、主动的多步推理过程。

### Q2: 有哪些相关研究？

基于提供的论文信息，相关研究主要分为三类。

**方法类相关研究**：首先是检索增强生成（RAG）范式，包括GraphRAG通过图结构和社区摘要改进多跳推理，以及Agentic RAG（如Search-o1、Search-R1）将检索纳入推理循环。本文与这些工作的区别在于，RAG面向外部知识库填补事实空白，而本文面向智能体自身的持久交互历史进行记忆重建。其次是图记忆系统如A-Mem、Zep和LiCoMemory，它们用图结构捕获记忆间依赖关系，但本文指出这些方法的遍历受限于预定义操作符，无法根据检索中积累的证据动态调整。

**评测类相关研究**：本文在LoCoMo和LongMemEval基准上进行实验，这些基准用于评估长历史记忆推理能力。

**核心区别**：本文提出的MRAgent框架通过主动重建机制，将LLM推理直接集成到记忆访问中，实现基于中间证据的迭代探索和剪枝，而现有方法（包括分层记忆系统如MemoryOS、Mem0、SeCom）的检索过程都是被动的，即记忆单元选择仅作为查询的固定函数，不进行基于中间证据的推理。

### Q3: 论文如何解决这个问题？

为解决大语言模型在长程交互中静态检索的局限性，论文提出了MRAgent框架，核心创新在于将记忆访问建模为“主动重构”过程，而非简单的“静态检索”。

**整体框架**：MRAgent构建了一个结构化的关联记忆图（Associative Memory Graph），并在此基础上设计了主动记忆重构机制（Active Reconstruction Mechanism），将LLM的推理直接集成到记忆访问中。

**核心组件与架构**：
1.  **关联记忆系统（Cue-Tag-Content图）**：记忆被组织成一个异构图，包含两类节点：**Cue（线索）**（细粒度关键词如实体、属性）和**Content（内容）**（存储具体记忆项）。二者通过**Tag（标签）**这一关系属性连接。Tag作为语义桥梁，总结Cue与Content之间的关联关系。记忆图分为三层：**情节层**（存储具体事件）、**语义层**（存储稳定的知识如偏好）和**主题层**（存储跨情节的抽象模式），支持多粒度访问。

2.  **主动记忆重构机制**：该机制维护一个显式的**重构状态S(t)**，包含当前活跃节点集Z(t)和已积累证据H(t)。通过定义两类遍历动作：**前向遍历**（从Cue到Tag再到Content）和**反向遍历**（从Content回溯到新的Cue和Tag），LLM能够迭代地执行以下步骤：
    *   **LLM推理与动作选择**：基于当前状态和查询，LLM选择有希望的遍历方向，而非穷举所有路径。
    *   **受控记忆遍历**：执行选定动作，从图中获取候选节点。
    *   **LLM路由与状态更新**：LLM评估候选节点的语义相关性，剪枝无关分支，更新活跃集和已积累证据。

**创新点**：该方法打破了传统的“先检索再推理”的静态流水线。LLM能够基于推理过程中发现的中间证据，动态地调整访问路径，进行“探索-剪枝”的迭代循环，从而避免了组合爆炸，实现了对大规模记忆图的精准、高效访问。理论证明，主动检索的假设类严格包含被动检索，具有更强的表达能力。

### Q4: 论文做了哪些实验？

论文在LoCoMo和LongMemEval两个基准上评估了MRAgent。对比方法包括RAG、A-Mem、MemoryOS、LangMem和Mem0，使用Gemini-2.5-Flash和Claude-Sonnet-4.5作为LLM骨干，主要评估F1分数和LLM-Judge评分。在LoCoMo上，MRAgent在Gemini骨干下总体J分从68.31提升至84.21（相对提升23.3%），在Claude骨干下提升12.4%。在LongMemEval上，MRAgent总体J分达72.95，相对最强基线提升32%。计算成本方面，MRAgent每样本仅消耗118k token，远低于A-Mem的632k，运行时为586.11秒。消融实验显示，主动多步推理是主要增益来源，变体在无推理设置下性能从CE到CTE到CTC单调提升，表明关联标签提供有效语义引导，且情节记忆与语义记忆层互补。多轮推理分析表明，多跳查询受益于迭代探索，召回率逐步提升超30%，智能体能自主决定停止时机。案例研究展示了MRAgent在结构化记忆图上主动重建多会话证据的能力。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于将复杂关系推理负担转移至检索阶段，导致重建成本随探索深度线性增长，长序列查询延迟较高；同时静态记忆构造策略使记忆图谱随交互单调扩展，存储开销持续累积。未来研究方向包括：开发自适应记忆构造机制，引入遗忘与整合策略，如基于时间衰减或信息重要性的动态剪枝；设计轻量级记忆维护算法，在保持关键信息的同时控制图规模；探索更鲁棒的遍历策略，结合强化学习或蒙特卡洛树搜索优化路径选择。此外，当前方法依赖单一LLM驱动推理，可尝试多智能体协作（如分离检索与验证角色）以减少迭代错误。将主动重建与知识蒸馏、稀疏注意力结合，有望在长时推理场景中实现更高效的平衡。

### Q6: 总结一下论文的主要内容

这篇论文提出MRAgent框架，旨在解决大语言模型智能体在长程交互历史中推理能力不足的问题。其核心贡献在于重新定义了记忆中检索范式：从静态的“检索-推理”被动模式转变为主动的、联想式的记忆重构过程。论文定义的问题是如何让智能体在推理过程中动态适应中间证据，而非仅依赖初始查询进行一次性检索。方法上，MRAgent构建了“线索-标签-内容”联想记忆图，标签作为语义桥梁连接细粒度线索与内容。在此基础上，智能体通过集成大语言模型推理的主动重构机制，在图中迭代探索并剪枝检索路径，将检索融入推理步骤。主要结论表明，在LoCoMo和LongMemEval基准测试上，MRAgent相比强基线取得了最高23%的性能提升，同时显著降低了令牌和运行时间成本，验证了主动、联想式重构在长程记忆推理中的有效性和效率。该研究将记忆重构的认知科学概念引入AI系统，开辟了新的研究范式。
