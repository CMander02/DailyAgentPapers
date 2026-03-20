---
title: "D-Mem: A Dual-Process Memory System for LLM Agents"
authors:
  - "Zhixing You"
  - "Jiachen Yuan"
  - "Jason Cai"
date: "2026-03-19"
arxiv_id: "2603.18631"
arxiv_url: "https://arxiv.org/abs/2603.18631"
pdf_url: "https://arxiv.org/pdf/2603.18631v1"
categories:
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Long-horizon Reasoning"
  - "Retrieval-Augmented Generation"
  - "Dual-Process System"
  - "Computational Efficiency"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# D-Mem: A Dual-Process Memory System for LLM Agents

## 原始摘要

Driven by the development of persistent, self-adapting autonomous agents, equipping these systems with high-fidelity memory access for long-horizon reasoning has emerged as a critical requirement. However, prevalent retrieval-based memory frameworks often follow an incremental processing paradigm that continuously extracts and updates conversational memories into vector databases, relying on semantic retrieval when queried. While this approach is fast, it inherently relies on lossy abstraction, frequently missing contextually critical information and struggling to resolve queries that rely on fine-grained contextual understanding. To address this, we introduce D-Mem, a dual-process memory system. It retains lightweight vector retrieval for routine queries while establishing an exhaustive Full Deliberation module as a high-fidelity fallback. To achieve cognitive economy without sacrificing accuracy, D-Mem employs a Multi-dimensional Quality Gating policy to dynamically bridge these two processes. Experiments on the LoCoMo and RealTalk benchmarks using GPT-4o-mini and Qwen3-235B-Instruct demonstrate the efficacy of our approach. Notably, our Multi-dimensional Quality Gating policy achieves an F1 score of 53.5 on LoCoMo with GPT-4o-mini. This outperforms our static retrieval baseline, Mem0$^\ast$ (51.2), and recovers 96.7\% of the Full Deliberation's performance (55.3), while incurring significantly lower computational costs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的自主智能体在长程交互中进行高保真记忆访问和深度推理时所面临的核心挑战。随着智能体向持久化、自适应的方向发展，其需要积累经验并在长期任务中自我演进，但LLM参数的静态性与有限上下文窗口成为瓶颈。现有主流方法（如MemoryBank、Zep、Mem0）采用增量式记忆处理范式，通过持续提取、压缩对话记忆到向量数据库来实现高效的语义检索。然而，这种基于查询无关压缩（query-agnostic compression）的方法存在根本性不足：它在压缩过程中不可避免地丢失了大量上下文细节和细微逻辑（如未明确表述的时间逻辑、多跳依赖关系），导致系统在处理需要精细上下文理解或严格演绎的查询时，经常遗漏关键信息，从而陷入性能瓶颈。

因此，本文的核心问题是：如何设计一个记忆系统，既能保持高效检索的实时性，又能确保在复杂推理场景下不丢失关键上下文信息，从而实现高保真度的长程记忆访问。为此，论文提出了D-Mem，一个双过程记忆系统。它保留了轻量级的向量检索（System 1）用于处理常规查询，同时建立了一个详尽的全审慎模块（System 2）作为高保真度的备用方案。为了解决两个过程之间的平衡问题，论文引入了多维质量门控策略，动态评估System 1输出的质量（包括相关性、忠实度、一致性、完整性），仅在必要时才触发计算成本高昂的System 2，从而在保证推理准确性的同时实现认知经济性。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提升大语言模型（LLM）智能体记忆与检索能力的框架和方法，可分为以下几类：

**1. 检索增强生成（RAG）与优化方法：**
标准RAG通过稠密相似性检索文档并生成回答。后续研究通过查询扩展、重排序、相关性过滤和查询转换等技术优化检索流程。这些工作聚焦于**如何更好地检索**，但本质上仍遵循预存储、后检索的范式。

**2. 基于增量处理的记忆系统：**
如MemGPT、Mem0和MemoryBank等框架，受操作系统启发，采用增量处理范式，持续将对话记忆提取并更新到向量数据库中。这类方法虽然快速，但为了存储效率会进行**有损的语义抽象和向量化**，导致细粒度的上下文、时间与因果逻辑信息丢失，难以处理需要深度情境理解的查询。

**3. 注重结构完整性的记忆优化：**
为了缓解语义碎片化问题，G-Memory、Mem0^g 和 A-Mem 等工作引入了图结构层次或互连笔记，以更好地保持记忆元素间的**关系完整性**。然而，这些方法在存储阶段仍进行预固定的压缩表示，本质上是**与查询无关的**，因此无法从根本上避免有损抽象带来的信息损失。

**4. 高保真度情景重建与深思范式：**
为彻底规避有损抽象，GAM和E-mem等最新研究转向情景上下文重建和多智能体深思范式。它们**放弃轻量级检索**，转而彻底处理原始的、未压缩的历史上下文，优先保证推理的保真度。但这种方法计算开销巨大且缺乏灵活性，忽视了多数常规查询可通过快速语义回忆（即“系统1”的认知经济性）高效解决。

**本文与这些工作的关系与区别：**
本文提出的D-Mem系统与上述工作均有关联，但核心创新在于**融合了两种范式**。它保留了轻量级向量检索（类似第1、2类工作）来处理常规查询，同时引入一个详尽的高保真度“完全深思”模块（类似第4类工作）作为后备。关键区别在于，D-Mem通过一个**多维质量门控策略**动态桥接这两个过程，实现了**在保证准确性的前提下追求认知经济性**，从而避免了第2、3类工作的信息损失问题和第4类工作的 indiscriminate 巨大计算开销。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为D-Mem的双进程内存系统来解决传统检索式记忆框架因依赖有损抽象而丢失关键细节、难以处理需要细粒度上下文理解查询的问题。其核心方法是构建一个动态路由的双层架构，在保持计算效率的同时，为复杂查询提供高保真度的推理能力。

整体框架由三个紧密耦合的组件构成：
1.  **Mem0*模块（轻量级检索模块）**：作为基础的“系统1”，负责快速处理常规查询。它对标准Mem0框架进行了两项关键改进：一是在提取阶段，利用前10个最相似的记忆（而非通用摘要）和最近的对话消息作为上下文，来提取新的显著记忆；二是在更新记忆前，增加了基于严格余弦相似度阈值（>0.8）的相关性过滤步骤，以减少认知负载和噪声。在回答查询时，它先检索前30个相似记忆生成初始答案，并采用一个严格的过滤流程来提炼上下文，以减轻幻觉。
2.  **质量门控策略**：这是一个动态评估路由器，是系统的创新核心。它负责评估Mem0*模块生成的初始答案（A_init）、用户查询（q）和检索到的上下文（C），并依据一个多维质量评估标准来决定是否触发回退机制。该标准从三个正交维度进行评估：**相关性**（答案是否与查询直接相关）、**忠实性与一致性**（答案是否基于给定上下文且无矛盾）、**完整性**（答案是否充分回答了查询）。只有当答案通过全部三个维度的检查时，系统才会直接输出A_init；否则，质量门控将触发值为1，启动回退。
3.  **完全审议模块**：作为高保真度的回退路径（“系统2”），仅在质量门控判定轻量级检索不足时被触发。它完全绕过压缩的向量表示，直接对原始的、未压缩的完整对话历史进行详尽处理。其过程分为三个阶段：首先，将对话分块并进行查询相关事实提取与评分；其次，通过基于分数的阈值和LLM进行多阶段过滤，筛选出最相关的事实子集；最后，用这些过滤后的事实替代Top-30记忆来生成最终答案。

该架构的主要创新点在于：
*   **双进程解耦设计**：结构上将快速的常规语义检索与资源密集型的完全审议分离，实现了认知经济性与高保真度推理的平衡。
*   **动态多维质量门控**：提出了一种智能路由策略，通过可解释的多维度评估（相关性、忠实性、完整性）动态决定是否启用高成本回退，而非静态或基于简单共识的触发机制。实验表明，该策略能以显著更低的计算成本，恢复完全审议模块96.7%的性能。
*   **Mem0*的增强**：通过使用Top-K相似记忆和近期消息作为提取上下文，以及引入严格的相关性过滤，提升了基础检索模块的准确性和鲁棒性。

### Q4: 论文做了哪些实验？

实验在LoCoMo和RealTalk两个长对话基准数据集上进行。LoCoMo包含10个平均24K token的对话和1540个问题，涵盖单跳、多跳、时序和开放域四类推理；RealTalk包含10个平均超16000词的现实对话和728个问题，涵盖多跳、时序和开放域三类。评估指标包括F1分数、BLEU分数和LLM-as-a-Judge分数。主要使用GPT-4o-mini作为骨干模型，并辅以Qwen3-235B-Instruct验证泛化性。

对比方法包括：Full Context（输入全部历史）、标准RAG、LangMem、Mem0、Zep、Nemori、EMem-G等基线，以及论文提出的Mem0*（增强版System 1基线）、Filter、Majority Voting、Consensus、Quality Gating（多维质量门控策略）和Full Deliberation（完整审阅模块）。

主要结果：在LoCoMo数据集上，使用GPT-4o-mini时，Quality Gating的F1分数达到53.5，优于Mem0*（51.2）和Nemori（49.5），并恢复了Full Deliberation（55.3）96.7%的性能，同时显著降低了计算成本（token消耗仅为后者的35.8%）。在RealTalk数据集上，Quality Gating的F1为39.4，同样接近Full Deliberation（40.6）并节省资源。分问题类别分析显示，对于更难的时序和开放域问题，Quality Gating带来的F1提升更大（例如在LoCoMo上分别提升2.7和4.1），表明门控机制能有效识别静态检索不足的查询。此外，实验还分析了不同路由策略的回退率、选择偏差和模型特异性差异，验证了系统的适应性和效率。

### Q5: 有什么可以进一步探索的点？

该论文的D-Mem系统在平衡效率与准确性方面取得了进展，但仍存在若干局限性和可进一步探索的方向。首先，系统的可扩展性受限于“完全审议”模块对全部对话历史的详尽扫描，这在终身学习或无限上下文场景中会带来巨大的计算开销。尽管质量门控机制缓解了此问题，但如何设计更高效、可动态裁剪的长期记忆压缩与索引机制，仍是未来研究的关键。

其次，当前系统在长程推理方面存在明显短板。“完全审议”模块将历史分割为孤立块进行并行事实提取，仅依赖LLM的自注意力机制在提取事实间建立联系，缺乏显式的逻辑链构建与跨块状态追踪。这限制了其对需要全局语境和复杂依赖关系的复杂任务的推理能力。未来可探索引入显式的状态追踪架构，例如基于图神经网络的记忆网络或可微的符号推理模块，以显式建模事件间的因果、时序逻辑关系。

此外，论文的实验主要基于特定基准和模型（如GPT-4o-mini和Qwen3-235B-Instruct），其泛化能力有待在更多样化的任务、领域和开源模型上进行验证。质量门控策略的多维度阈值目前可能较为静态，未来可研究自适应或基于强化学习的动态门控策略，以更精细地权衡成本与性能。最后，将此类双过程记忆系统与工具使用、规划等智能体其他模块更深度地集成，构建具备连贯认知流的统一架构，也是一个富有前景的方向。

### Q6: 总结一下论文的主要内容

本文针对LLM智能体在长程推理中面临的高保真记忆访问需求，提出D-Mem双过程记忆系统。现有基于检索的记忆框架通常采用增量处理范式，依赖向量数据库进行语义检索，这种方法虽然快速，但存在有损抽象问题，容易丢失关键上下文信息，难以处理需要细粒度理解的查询。为解决此问题，D-Mem系统保留了轻量级向量检索用于常规查询，同时建立了一个详尽的高保真回退模块——完全审议模块。为实现认知经济性且不牺牲准确性，系统采用多维质量门控策略动态桥接这两个过程。在LoCoMo和RealTalk基准测试上的实验表明，该方法的有效性显著：多维质量门控策略在GPT-4o-mini上实现了53.5的F1分数，优于静态检索基线，并恢复了完全审议模块96.7%的性能，同时显著降低了计算成本。核心贡献在于通过双过程架构与动态路由机制，在保证高记忆保真度的同时，实现了效率与精度的平衡。
