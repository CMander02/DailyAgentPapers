---
title: "EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective"
authors:
  - "Yuyao Wang"
  - "Zhongjian Zhang"
  - "Mo Chi"
  - "Kaichi Yu"
  - "Yuhan Li"
  - "Miao Peng"
  - "Bing Tong"
  - "Chen Zhang"
  - "Yan Zhou"
  - "Jia Li"
date: "2026-05-18"
arxiv_id: "2605.18421"
arxiv_url: "https://arxiv.org/abs/2605.18421"
pdf_url: "https://arxiv.org/pdf/2605.18421v1"
github_url: "https://github.com/DSAIL-Memory/EvoMemBench"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent Memory"
  - "Benchmark"
  - "LLM Agent"
  - "Self-Evolving"
  - "Memory Scope"
  - "Memory Content"
  - "Retrieval-based Methods"
  - "Procedural Memory"
  - "Long-term Memory"
relevance_score: 9.2
---

# EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective

## 原始摘要

Recent benchmarks for Large Language Model (LLM) agents mainly evaluate reasoning, planning, and execution. However, memory is also essential for agents, as it enables them to store, update, and retrieve information over time. This ability remains under-evaluated, largely because existing benchmarks do not provide a systematic way to assess memory mechanisms. In this paper, we study agent memory from a self-evolving perspective and introduce EvoMemBench, a unified benchmark organized along two axes: memory scope (in-episode vs. cross-episode) and memory content (knowledge-oriented vs. execution-oriented). We compare 15 representative memory methods with strong long-context baselines under a standardized protocol. Results show that current memory systems are still far from a general solution: long-context baselines remain highly competitive, memory helps most when the current context is insufficient or tasks are difficult, and no single memory form works consistently across all settings. Retrieval-based methods remain strong for knowledge-intensive settings, whereas procedural and long-term memory methods are more effective for execution-oriented tasks when their stored experience matches the task structure. We hope EvoMemBench facilitates future research on more effective memory systems for LLM-based agents. Our code is available at https://github.com/DSAIL-Memory/EvoMemBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）智能体在记忆能力评估上的空白。当前基准测试主要关注推理、规划和执行，但智能体在交互中存储、更新和复用信息的能力（即记忆）却缺乏系统评估。现有方法存在三点不足：第一，文本类基准（如LoCoMo、LongMemEval）仅评测对话或文档中的知识保留，无法覆盖动作和工具执行场景；第二，交互式基准（如MemoryArena、Evo-Memory）虽涉及跨回合或终身记忆，但未同时评估回合内与跨回合的记忆演化，也未区分知识导向与执行导向的记忆需求；第三，部分相关基准未完全开源，限制了可重复比较。为此，本文引入EvoMemBench，从“自我演化”（self-evolving）视角出发，沿两个维度（记忆范围：回合内 vs. 跨回合；记忆内容：知识导向 vs. 执行导向）构建统一基准。核心问题是：现有记忆系统能否在不同场景下有效支持信息的持续更新与复用？实验表明，当前系统尚无通用解决方案，长上下文基线仍具竞争力，而不同记忆形式仅在特定条件下（如当前上下文不足或任务复杂时）发挥优势，但缺乏跨设置的一致性表现。该基准旨在系统揭示记忆方法的适用边界，推动更优记忆系统的研究。

### Q2: 有哪些相关研究？

相关研究可分为两类。**记忆机制类**包括：基于检索的方法（存储过往信息并在推理时检索）、长期记忆系统（结构化存储、更新和管理持久事实与偏好）、程序化记忆方法（将轨迹抽象为可复用工作流或技能），以及逐步演化的记忆架构。**记忆基准类**包括：LoCoMo和LongMemEval（评估多轮对话长程问答记忆）、MemoryAgentBench（测试增量输入下的检索与选择性遗忘）、MemoryBench（模拟用户反馈的持续学习）、Evo-Memory（评估测试时记忆演化）、MemoryArena（多会话环境中的记忆引导行为）以及StuLife（侧重执行演化）。本文与这些工作的核心区别在于：现有基准仅覆盖部分记忆维度（如LoCoMo仅评估知识演化，Evo-Memory仅关注跨场景），而EvoMemBench首次统一覆盖记忆范围（片内/跨片）和记忆内容（知识型/执行型）四个象限，并提供标准化评测协议对15种代表性记忆方法进行公平比较。

### Q3: 论文如何解决这个问题？

该论文通过构建统一基准测试框架EvoMemBench来解决智能体记忆能力的评估问题。核心方法围绕两个维度组织记忆类型：记忆范围（episode内 vs 跨episode）和记忆内容（知识导向 vs 执行导向），将记忆任务划分为四种基本类型。

整体框架包含六个子数据集：InEp-Know（评估episode内知识保留与更新）、InEp-Exec（评估工具使用场景中的执行状态跟踪）、CrossEp-Know（评估跨episode知识积累，涵盖领域事实、规则系统、程序和实证模式四种知识形式）、CrossEp-Tool/Web/Emb（分别评估工具使用、网页搜索和具身交互中的跨episode执行经验复用）。对于每个子数据集，论文通过重构原始数据集（如对BFCL进行隐式引用替换和子步骤拆分）来强化记忆依赖，并采用标准化协议对比15种记忆方法和强长上下文基线。

主要创新点包括：1) 首次从自我演化视角系统定义智能体记忆，明确区分知识演化和执行演化两种机制；2) 构建覆盖4种记忆场景的统一评估框架，支持细粒度记忆能力分析；3) 揭示关键发现：长上下文基线仍具竞争力，记忆在上下文不足或任务困难时最有效，没有单一记忆形式能适应所有场景。检索型方法适合知识密集型任务，而过程记忆和长期记忆在执行导向任务中更有效。

### Q4: 论文做了哪些实验？

论文围绕EvoMemBench基准进行了系统性实验。实验设置了内存范围（幕内 vs. 跨幕）和内存内容（知识导向 vs. 执行导向）两个维度，共评估了15种内存方法，并与强长上下文基线（Gemini-3-Flash、GPT-5-mini、DeepSeek-V3.2）对比，使用统一骨干模型DeepSeek-V3.2。数据集包括：知识导向任务（InEp-Know含Event QA、LME、Ruler等子集，CrossEp-Know按难易度分）和执行导向任务（InEp-Exec含Gorilla File System、Vehicle Control等4个场景，跨执行场景含工具、网页、具身任务）。主要指标是准确率和成功率。关键结果：1）长上下文基线仍极具竞争力，Gemini-3-Flash在InEp-Know上排名第一（保留和修正平均排名均为1.0）；2）现有内存方法在保留任务上优于修正任务，如BM25、Mem0在Event QA上表现好，但在FactConsolidation多跳任务上性能骤降；3）内存优势在约束上下文下最明显，16K时最优内存比无内存基线提升14.5个百分点（ReasoningBank达43.0%），128K时增益缩小；4）程序式长期内存（如ReasoningBank、AWM）在执行任务上表现更佳，而短时压缩（如MemAgent）可能有害，16K时仅26.0%低于基线28.5%。

### Q5: 有什么可以进一步探索的点？

基于实验分析，EvoMemBench揭示了当前智能体记忆系统的核心局限：长上下文基线依然极具竞争力，而现有记忆方法在知识保留上优于知识修订，尤其在多跳信息冲突场景下表现脆弱。未来可探索的方向包括：一是设计能够动态评估信息重要性和冲突程度的记忆更新机制，利用元学习或强化学习来学习何时保留、更新或删除记忆。二是结合混合记忆架构，例如将检索式记忆的强项（知识密集型）与程序性记忆的泛化能力（执行导向）融合，通过路由机制根据任务类型动态选择记忆形式。此外，当前记忆系统在跨系列（cross-episode）任务中扩展性差，可研究分层记忆结构，区分短期工作记忆与长期知识库的演化机制，并引入压缩损失感知的认知框架。记忆模块的资源消耗也是瓶颈，需要开发更高效的稀疏化记忆管理策略，以在有限上下文窗口中最大化信息密度。

### Q6: 总结一下论文的主要内容

论文介绍EvoMemBench，这是一个从“自演化”视角评估大语言模型智能体记忆能力的统一基准。现有基准主要评估推理、规划等能力，但忽略了记忆的动态更新与复用。该基准沿着两条轴划分了四种评估场景：记忆范围（场景内 vs. 跨场景）和记忆内容（知识导向 vs. 执行导向），系统性地评估了记忆系统在知识更新、执行状态维护等方面的能力。作者在标准化协议下比较了15种代表性记忆方法及强长上下文基线。主要结论是：当前记忆系统远非通用解决方案，长上下文基线依然极具竞争力；记忆仅在当前上下文不足或任务困难时才显著有效；没有任何单一记忆形式能适用于所有场景；检索型方法在知识密集型场景表现强劲，而程序性与长期记忆方法在执行导向任务中更有效，但前提是其存储经验与任务结构相匹配。该工作的核心贡献是提出了一个系统、开放的评估框架，揭示了不同记忆方法的适用边界，为未来开发更有效的智能体记忆系统指明了方向。
