---
title: "Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation"
authors:
  - "Zhanghao Hu"
  - "Qinglin Zhu"
  - "Hanqi Yan"
  - "Yulan He"
  - "Lin Gui"
date: "2026-02-02"
arxiv_id: "2602.02007"
arxiv_url: "https://arxiv.org/abs/2602.02007"
pdf_url: "https://arxiv.org/pdf/2602.02007v2"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent 架构"
  - "Agent 记忆"
  - "检索增强生成"
  - "多智能体系统"
  - "Agent 数据合成"
  - "Agent 规划/推理"
  - "工具使用"
  - "Agent 评测/基准"
relevance_score: 9.5
---

# Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation

## 原始摘要

Agent memory systems often adopt the standard Retrieval-Augmented Generation (RAG) pipeline, yet its underlying assumptions differ in this setting. RAG targets large, heterogeneous corpora where retrieved passages are diverse, whereas agent memory is a bounded, coherent dialogue stream with highly correlated spans that are often duplicates. Under this shift, fixed top-$k$ similarity retrieval tends to return redundant context, and post-hoc pruning can delete temporally linked prerequisites needed for correct reasoning. We argue retrieval should move beyond similarity matching and instead operate over latent components, following decoupling to aggregation: disentangle memories into semantic components, organise them into a hierarchy, and use this structure to drive retrieval. We propose xMemory, which builds a hierarchy of intact units and maintains a searchable yet faithful high-level node organisation via a sparsity--semantics objective that guides memory split and merge. At inference, xMemory retrieves top-down, selecting a compact, diverse set of themes and semantics for multi-fact queries, and expanding to episodes and raw messages only when it reduces the reader's uncertainty. Experiments on LoCoMo and PerLTQA across the three latest LLMs show consistent gains in answer quality and token efficiency.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体记忆系统中直接套用传统检索增强生成（RAG）方法所导致的检索效率低下和证据冗余问题。研究背景是，随着大语言模型被广泛用作需要长期、多轮交互的智能体，其记忆系统需要存储和检索过往对话以支持连贯推理和个性化。然而，当前大多数系统仍沿用为大规模异构文档库设计的标准RAG流程，即通过向量相似度检索固定数量的文本片段。

现有方法的不足在于，智能体记忆是一个有界、连贯且高度相关的对话流，其中许多片段内容相似甚至重复。在这种场景下，基于固定top-k相似度的检索倾向于返回大量冗余的上下文，导致检索“塌陷”到语义密集的单一区域，无法有效分离出真正需要的证据。此外，事后对检索结果进行剪枝或压缩的方法也常常失效，因为这些方法依赖局部相关性线索，而对话证据在时间上存在共指、省略和时序依赖等复杂关联，盲目剪枝可能破坏推理链中的必要前提。

因此，本文要解决的核心问题是：如何为智能体记忆设计一种超越简单相似度匹配的新型检索范式。论文主张，检索应转向对潜在语义组件的操作，遵循“解耦到聚合”的原则。具体而言，需要将记忆流分解为语义组件，并将其组织成层次化结构，然后利用该结构来驱动检索，从而从根本上避免冗余，并确保证据链的完整性。为此，论文提出了xMemory系统，它通过构建一个包含原始消息、情节、语义和主题的四层记忆层次，并利用一个平衡稀疏性与语义一致性的目标来指导结构的动态调整（分裂与合并）。在推理时，系统执行自顶向下的检索，先为多事实查询选择一组紧凑且多样的主题和语义单元以拓宽召回，仅当能有效降低读者（即LLM）的不确定性时，才向下展开更细粒度的情节和原始消息，以此在保证答案质量的同时显著提升token使用效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：记忆管理方法与检索及上下文管理方法。

在**记忆管理**方面，现有LLM智能体记忆系统主要分为扁平化上下文和结构化设计。扁平化方法（如MemGPT、MemoryOS）通过分页控制器或基于流的存储扩展有效上下文，但通常记录原始对话或仅经最低限度处理的痕迹，随着历史增长会累积冗余并增加检索与处理成本。结构化系统（如MemoryBank、Zep、A-Mem）将记忆组织为层次结构或图以提高连贯性和可导航性，但其检索单元仍多为原始或轻度处理的文本，且在查询时经常跨层或社区广泛扩展检索，可能引入大量上下文和高开销。本文提出的xMemory与之不同，它在构建时通过稀疏性-语义目标显式优化结构，旨在控制冗余检索并保持证据结构，从而实现高效检索。

在**检索与上下文管理**方面，大多数智能体记忆框架采用标准的RAG范式，通过嵌入相似性检索固定的top-k记忆集。这种方法适用于异构外部语料库，但与对话记忆的特性不匹配。在对话记忆中，检索源是有界且高度相关的，固定top-k检索容易返回具有共享背景的冗余片段，从而增加上下文长度并分散读者LLM的注意力。此外，为RAG长上下文推理开发的通用上下文压缩或剪枝方法（可能加剧“中间丢失”等问题）对于聊天记忆可能很脆弱，因为关键证据在时间上是连续的且依赖省略。本文方法则通过在图结构上进行贪婪子模代表性选择来获取紧凑的证据骨架，并应用不确定性门控的自适应包含来控制预算内的冗余，而无需在证据单元内部进行剪枝。

### Q3: 论文如何解决这个问题？

论文通过提出名为xMemory的层次化记忆系统来解决传统RAG在智能体记忆场景中的局限性。其核心方法是“解耦与聚合”，将高度相关的对话历史分解为可重用的语义组件，并组织成层次结构以驱动检索。

整体框架采用四层层次结构：原始消息 → 片段 → 语义节点 → 主题。原始消息块被映射到片段，片段可提炼出多个语义节点，语义节点被分配到唯一的主题中，主题则聚合多个相关语义节点。这种设计将冗余的片段轨迹与可重用的语义组件显式分离，保持了每个粒度上证据单元的完整性，防止时间关联的前提条件被错误修剪。

关键技术包括：1）通过稀疏性-语义性目标函数指导层次组织，该函数平衡了主题划分的均衡性（避免候选集过大导致检索集中在密集区域）和语义连贯性（同时避免主题间过度相似或孤立），具体通过计算主题划分的SparsityScore（基于期望簇大小）和SemScore（基于簇内凝聚度和簇间相似度正则化）来实现；2）基于k近邻图的高层导航，存储节点间的相似度边以支持高效检索；3）两阶段检索机制：第一阶段在kNN图上进行查询感知的代表性选择，通过贪心算法平衡覆盖增益和查询相关性，从主题和语义层面选取紧凑、多样化的节点集合以支持多事实查询和多跳推理；第二阶段基于不确定性的自适应证据纳入，仅当片段或原始消息能显著降低读者LLM的预测不确定性时，才将其纳入上下文，从而在预算控制下避免冗余并保持证据链完整。

创新点在于将检索从原始的相似度匹配转变为对潜在组件的层次化选择，并通过信息论驱动的目标函数动态管理记忆结构，实现了在高度相关、有界对话流中高效、非冗余的上下文构建。

### Q4: 论文做了哪些实验？

实验在LoCoMo和PerLTQA两个基准测试上进行，评估了xMemory在长程对话推理和个人长期记忆任务上的表现。实验使用了三个最新的LLM作为骨干模型：Qwen3-8B、Llama-3.1-8B-Instruct和GPT-5 nano。对比方法包括Naive RAG、A-Mem、MemoryOS、LightMem和Nemori这五种当前先进的智能体记忆系统。主要评估指标为BLEU-1、词级F1以及PerLTQA上增加的ROUGE-L，同时记录了每个查询的平均令牌消耗量（Token/query）以衡量效率。

主要结果显示，xMemory在所有骨干模型和两个数据集上均取得了最佳或极具竞争力的综合性能。在LoCoMo上，使用Qwen3-8B时，xMemory将平均BLEU从基线最佳（Nemori的28.51）提升至34.48，平均F1从40.45提升至43.98，同时将令牌消耗从最昂贵的基线（A-Mem的9103）大幅降低至4711。在GPT-5 nano上，平均BLEU从36.65提升至38.71，F1从48.17提升至50.00，令牌消耗从9155降至6581。在PerLTQA上，xMemory同样在多数指标上领先，例如在Qwen3-8B上获得了47.08的F1和42.50的ROUGE-L，优于MemoryOS的42.35和38.48。实验表明，xMemory通过解耦与聚合的检索机制，在保证答案质量的同时，有效减少了冗余上下文的检索，实现了精度与效率的双重提升。

### Q5: 有什么可以进一步探索的点？

本文提出的xMemory系统在提升检索质量和效率方面成效显著，但仍存在一些局限性和可进一步探索的方向。首先，其分层记忆结构的构建和动态重组（如节点的分裂与合并）依赖于特定的稀疏性-语义性优化目标，该目标的通用性和在不同任务领域的适应性有待验证。未来可研究更自适应或可学习的结构优化准则。其次，系统在推理时依赖不确定性估计来控制低层证据的扩展，这需要读者模型（如LLM）提供可靠的置信度信号；若信号不准，可能影响检索完整性。可探索更鲁棒的不确定性量化方法或多模型协同验证机制。

从更广阔的视角看，Agent记忆系统需与长期规划、技能学习等更复杂的认知功能结合。例如，记忆检索如何主动预测Agent未来需求，或与外部知识库进行动态对齐与更新。此外，当前实验集中于对话和QA任务，未来可测试其在具身交互、多模态环境等场景下的有效性。最后，xMemory的计算开销主要来自层次构建和检索时的图操作，对于大规模在线应用，需进一步优化其时间和空间效率，例如引入近似索引或增量学习机制。

### Q6: 总结一下论文的主要内容

该论文针对智能体记忆系统直接套用标准检索增强生成（RAG）框架的局限性，提出了新的解决方案。核心问题是标准RAG面向大规模异构语料库，而智能体记忆是有限、连贯且高度相关的对话流，导致固定top-k相似性检索常返回冗余信息，且后处理剪枝可能破坏推理所需的时间关联前提。

论文的核心贡献是提出了xMemory框架，其核心思想是“解耦与聚合”：首先将记忆解耦为语义组件，并将其组织成层次结构，然后利用该结构驱动检索。方法上，xMemory通过一个兼顾稀疏性与语义性的目标来指导记忆的分裂与合并，从而构建并维护一个由完整单元组成的、可搜索且忠实的高层节点组织。在推理时，它采用自顶向下的检索策略：针对多事实查询，先选择紧凑、多样的主题和语义集合；仅当能降低阅读器不确定性时，才向下扩展检索具体事件和原始消息。

主要结论是，在LoCoMo和PerLTQA数据集上，使用最新大语言模型进行的实验表明，xMemory在答案质量和token效率方面均优于RAG基线，能够检索到证据更密集的上下文，在减少冗余的同时保留了时间关联证据。
