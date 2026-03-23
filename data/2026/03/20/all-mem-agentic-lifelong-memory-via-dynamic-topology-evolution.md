---
title: "All-Mem: Agentic Lifelong Memory via Dynamic Topology Evolution"
authors:
  - "Can Lv"
  - "Heng Chang"
  - "Yuchen Guo"
  - "Shengyu Tao"
  - "Shiji Zhou"
date: "2026-03-20"
arxiv_id: "2603.19595"
arxiv_url: "https://arxiv.org/abs/2603.19595"
pdf_url: "https://arxiv.org/pdf/2603.19595v1"
categories:
  - "cs.IR"
  - "cs.CL"
tags:
  - "Agent Memory"
  - "Lifelong Learning"
  - "Retrieval-Augmented Generation"
  - "Memory Consolidation"
  - "Long-Context Management"
  - "Online/Offline Framework"
  - "Topology Evolution"
relevance_score: 8.5
---

# All-Mem: Agentic Lifelong Memory via Dynamic Topology Evolution

## 原始摘要

Lifelong interactive agents are expected to assist users over months or years, which requires continually writing long term memories while retrieving the right evidence for each new query under fixed context and latency budgets. Existing memory systems often degrade as histories grow, yielding redundant, outdated, or noisy retrieved contexts. We present All-Mem, an online/offline lifelong memory framework that maintains a topology structured memory bank via explicit, non destructive consolidation, avoiding the irreversible information loss typical of summarization based compression. In online operation, it anchors retrieval on a bounded visible surface to keep coarse search cost bounded. Periodically offline, an LLM diagnoser proposes confidence scored topology edits executed with gating using three operators: SPLIT, MERGE, and UPDATE, while preserving immutable evidence for traceability. At query time, typed links enable hop bounded, budgeted expansion from active anchors to archived evidence when needed. Experiments on LOCOMO and LONGMEMEVAL show improved retrieval and QA over representative baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长期运行的自主智能体（Lifelong Autonomous Agents）在持续积累海量记忆时，如何高效、可靠地检索相关证据的核心难题。随着智能体与用户交互数月甚至数年，其记忆库会无限增长，而下游任务（如回答查询）的可用上下文窗口和响应延迟预算却是固定的。现有方法在历史增长时性能会显著下降：简单的记忆累积会导致检索池中充满冗余、过时或相互纠缠的记忆单元，挤占有限的检索预算，使得返回的上下文信息质量低劣、分散甚至具有误导性。

具体而言，现有记忆系统虽已尝试运行时上下文编排、基于压缩或结构的检索，甚至引入大语言模型（LLM）进行维护（如重写、合并），但仍存在根本性不足：1）**实时性约束**：有效的记忆重组需要跨项目分析和大量计算，这与在线交互所需的低延迟形成矛盾；2）**结构漂移**：长期运行后，记忆组织会累积“结构债务”，如项目混淆、重复或状态不一致，而基于固定规则或只追加不修改的系统会加剧这一问题；3）**安全维护**：纠正结构漂移的编辑操作可能产生全局副作用，现有方法缺乏可验证、可逆且能保留完整溯源链的机制，容易导致信息不可逆丢失或隐藏错误。

因此，本文提出的All-Mem框架，其核心要解决的是**在固定计算和延迟预算下，如何通过一种可追溯、非破坏性的动态记忆拓扑演化机制，实现长期记忆的高质量维护与精准检索**。它通过在线/离线解耦、基于智能体（Agentic）的非破坏性拓扑整合（使用分裂、合并、更新等操作），以及拓扑感知的检索，来对抗结构漂移，确保智能体在长期服务中能持续访问到最相关、最一致的证据。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕长周期记忆管理和结构化记忆维护两大方向展开。

在**长周期记忆管理**方面，现有研究主要通过启发式方法（如分段、摘要、压缩、遗忘和更新）来优化在固定计算和延迟预算下的记忆写入与检索。然而，许多系统本质上是“仅追加”或依赖原地重写，导致随着历史增长，记忆库中出现冗余、过时和噪声信息，从而损害检索质量。本文提出的All-Mem框架将长周期记忆视为一个预算化的维护与恢复问题，其核心区别在于将低延迟的在线写入与离线的非破坏性整合分离，旨在保持在线检索表面的整洁，同时确保对不可变证据的可追溯恢复能力。

在**结构化记忆维护**方面，相关研究通过图、树等显式结构来组织记忆，以支持超越扁平相似性搜索的多跳证据聚合。但现有方法通常缺乏一个统一的、非破坏性的维护接口，其容量控制仍依赖于重写或遗忘操作，可能在长期运行中损害可追溯性或安全修正的能力。本文工作与此类研究的区别在于，All-Mem构建了一个类似Zettelkasten的、动态演化的记忆网络，并强调通过非破坏性的拓扑编辑（如分割、合并、更新）进行操作，同时支持从精心维护的可见表面出发，进行跳数受限、预算可控的恢复，以回溯到不可变的原始证据。

### Q3: 论文如何解决这个问题？

论文通过提出All-Mem框架来解决长期交互智能体中记忆系统随历史增长而退化的问题，其核心是构建一个通过动态拓扑演化进行显式、非破坏性整合的结构化记忆库，从而在固定上下文和延迟预算下实现高效、精准的检索。

**整体框架与主要模块**：All-Mem采用在线/离线分离的双阶段架构。在线阶段，系统以最小开销处理实时交互：将新观察创建为包含原始证据、可再生的摘要和关键词等字段的记忆单元，并通过稀疏链接将其临时锚定在“可见表面”上，同时仅将单元标识符缓冲以供离线处理。这确保了在线检索和写入的成本仅取决于可见表面的大小，而非整个历史。离线阶段则定期启动，进行“智能体拓扑整合”：系统并行地对缓冲单元及其邻域进行LLM诊断，生成带有置信度得分的拓扑编辑提案（包括SPLIT、MERGE、UPDATE三种操作），并通过置信度门控筛选后，按固定顺序（先拆分、后合并、再更新）串行执行这些编辑。所有操作均遵循非破坏性原则：原始证据永不删除，仅通过版本链接进行归档，从而保持完整的可追溯性。

**关键技术细节与创新点**：1) **结构化记忆库与可见表面**：记忆被建模为拓扑图，节点为记忆单元，边为四种类型的有向链接（时序、语义、版本、同源）。通过可修订的可见性指示器，将向量搜索范围限制在可见子集上，使粗检索成本与无限增长的历史解耦。2) **非破坏性拓扑编辑算子**：SPLIT将混杂单元的证据拆分为多个可见的兄弟单元并归档原单元；MERGE将冗余的可见单元集合合并为一个新的代表性单元并归档源单元；UPDATE用新单元描述符更新当前单元并归档被取代的旧单元。这些操作均通过添加版本链接来维持与归档证据的关联。3) **基于预算的跳数受限检索**：检索采用从粗到精的三阶段流程：首先在可见表面进行锚定检索；然后沿类型化链接在预设跳数和候选数预算内进行扩展；最后对候选集进行重排序并提取证据。这种方法实现了检索过程的显式成本控制。

**创新性**主要体现在：通过在线/离线分离和可见表面机制，在保证检索质量的同时严格限制了在线延迟；通过动态、非破坏性的拓扑演化（而非基于摘要的压缩）来持续优化记忆组织，避免了信息丢失；利用类型化链接和跳数限制实现了对归档证据的可控、高效访问。实验表明，该方法在多个基准测试中显著优于现有基线。

### Q4: 论文做了哪些实验？

论文在LOCOMO和LONGMEMEVAL-S两个基准上进行了实验，评估长期对话记忆性能。实验设置方面，使用Gpt-4o-mini作为生成器，All-MiniLM-L6-v2生成嵌入向量，所有方法遵循相同的增量协议，并在匹配的检索和上下文预算（通过相同的生成器输入token上限控制）下进行比较。

对比方法包括：完整历史记录（Full History）、密集检索基线（Naive RAG）以及多种记忆中心方法（MemGPT、A-Mem、HippoRAG2、Mem0、LightMem）。

主要结果如下：在LOCOMO和LONGMEMEVAL-S上，All-Mem在答案质量（4o-J/F1）和检索质量（R@5/N@5）指标上均取得最佳性能。例如，在LOCOMO上，All-Mem的4o-J为54.63，F1为52.18，R@5为46.63。在部署成本方面，All-Mem每轮记忆构建消耗1776个token（其中在线539个，摊销离线1237个），每次查询时注入918个token，相比A-Mem（注入2546个token/查询）和Mem0（注入1764个token/查询）显著降低了查询时开销。

通过预算扫描实验，在LONGMEMEVAL-S上，All-Mem在可比token预算（约1.4k-2.1k）下始终获得更高的F1值，最佳设置（K=16, k=10, L=40）达到峰值F1 45.19，优于A-Mem的峰值30.82（其token开销更高，约2.8k-3.5k）。可扩展性实验显示，当历史长度N=460时，仅搜索可见表面（而非完整记忆库）将第一阶段检索延迟从20.10ms降低至10.88ms（减少45.9%）。消融实验验证了可见表面门控、离线整合和预算恢复等核心设计的必要性，移除它们会导致性能下降和延迟增加。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其拓扑编辑操作（如分割、合并、更新）的置信度门控和调度策略尚为固定或启发式，可能无法自适应不同任务或数据分布；链接语义相对简单，限制了复杂推理场景下的鲁棒性；评估仍局限于模拟数据集，未在真实世界智能体中验证其长期稳定性、隐私与安全性。未来可探索自适应学习机制，动态调整编辑阈值与操作顺序；引入更丰富的语义关系（如因果、时序）以增强链接表达能力；结合增量学习技术优化内存更新效率。此外，需在开放环境中测试框架，考虑人类反馈融入与道德约束，并探索跨模态记忆整合以支持更全面的智能体交互。

### Q6: 总结一下论文的主要内容

该论文提出了All-Mem框架，旨在解决长期交互智能体在固定上下文和延迟预算下，如何持续写入长期记忆并准确检索相关证据的核心问题。现有系统随着历史增长常出现检索内容冗余、过时或噪声大的性能退化。

其核心贡献是设计了一种通过动态拓扑演化来管理记忆库的在线/离线终身记忆框架。方法上，在线运行时，系统将检索锚定在一个有限的“可见表面”以控制粗略搜索成本；离线阶段则利用LLM诊断器，以置信度评分驱动并执行SPLIT、MERGE和UPDATE三种拓扑编辑操作，进行非破坏性的显式记忆巩固，避免了基于摘要压缩的不可逆信息丢失。查询时，系统通过类型化链接在必要时从活跃锚点进行跳数受限的、预算可控的扩展，以访问归档证据。

主要结论显示，在LOCOMO和LONGMEMEVAL基准测试中，All-Mem在检索和问答任务上优于代表性基线方法。该框架的意义在于为构建可持续学习、记忆可追溯且检索高效的长周期智能体提供了新的系统设计思路。
