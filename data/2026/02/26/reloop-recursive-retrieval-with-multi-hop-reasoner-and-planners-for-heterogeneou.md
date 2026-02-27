---
title: "RELOOP: Recursive Retrieval with Multi-Hop Reasoner and Planners for Heterogeneous QA"
authors:
  - "Ruiyi Yang"
  - "Hao Xue"
  - "Imran Razzak"
  - "Hakim Hacid"
  - "Flora D. Salim"
date: "2025-10-23"
arxiv_id: "2510.20505"
arxiv_url: "https://arxiv.org/abs/2510.20505"
pdf_url: "https://arxiv.org/pdf/2510.20505v3"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent 架构"
  - "检索增强生成 (RAG)"
  - "多步推理"
  - "工具使用"
  - "规划"
  - "问答 (QA)"
relevance_score: 7.5
---

# RELOOP: Recursive Retrieval with Multi-Hop Reasoner and Planners for Heterogeneous QA

## 原始摘要

Retrieval-augmented generation (RAG) remains brittle on multi-step questions and heterogeneous evidence sources, trading accuracy against latency and token/tool budgets. This paper introduces RELOOP, a structure aware framework using Hierarchical Sequence (HSEQ) that (i) linearize documents, tables, and knowledge graphs into a reversible hierarchical sequence with lightweight structural tags, and (ii) perform structure-aware iteration to collect just-enough evidence before answer synthesis. A Head Agent provides guidance that leads retrieval, while an Iteration Agent selects and expands HSeq via structure-respecting actions (e.g., parent/child hops, table row/column neighbors, KG relations); Finally the head agent composes canonicalized evidence to genearte the final answer, with an optional refinement loop to resolve detected contradictions. Experiments on HotpotQA (text), HybridQA/TAT-QA (table+text), and MetaQA (KG) show consistent EM/F1 gains over strong single-pass, multi-hop, and agentic RAG baselines with high efficiency. Besides, RELOOP exhibits three key advantages: (1) a format-agnostic unification that enables a single policy to operate across text, tables, and KGs without per-dataset specialization; (2) \textbf{guided, budget-aware iteration} that reduces unnecessary hops, tool calls, and tokens while preserving accuracy; and (3) evidence canonicalization for reliable QA, improving answers consistency and auditability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决检索增强生成（RAG）在处理多步骤问题和异构证据源时存在的脆弱性、效率低下以及缺乏统一性的问题。研究背景是，尽管RAG通过引入外部证据减少了LLM的事实性错误，但在面对需要多跳推理的复杂问题，以及混合文本、表格和知识图谱（KG）等多种格式数据源时，现有方法仍面临显著挑战。

现有方法的不足主要体现在三个方面：首先，单次检索生成管道（C1）难以追踪完整的证据链，因为密集检索器通常关注点状召回，文档分块会破坏上下文连贯性，而长上下文提示又会引入无关信息且无法判断证据是否充分。其次，采用多智能体协作的迭代系统（C2）虽然能进行多步推理，但搜索空间容易爆炸，导致计划分支过多、工具调用重复、思维链冗长，从而产生不可预测的延迟和资源消耗，且终止机制往往依赖启发式方法，效率低下。最后，针对不同数据格式（C3），现有系统通常需要各自独立的索引、检索器和控制逻辑，缺乏统一的表示和可逆的序列化方法，导致策略难以复用且可能丢失来源信息。

本文要解决的核心问题是：如何设计一个统一的、结构感知的框架，以高效、可控且可审计的方式，从异构数据源中迭代检索“恰好足够”的证据来回答复杂的多步骤问题。为此，论文提出了RELOOP框架，其核心创新在于将异构数据线性化为可逆的层次化序列（HSEQ），并在此统一表示上进行由指导计划驱动的、预算感知的迭代检索，最后对证据进行规范化处理以生成可靠答案。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为以下几类：

**1. 检索增强生成（RAG）**：这是本文工作的核心背景。传统RAG系统通过从外部知识源检索信息来增强LLM的回答，但通常在处理多跳问题和异构数据源（如文本、表格、知识图谱）时显得脆弱，需要在准确性、延迟和计算开销之间权衡。近期研究尝试将图结构数据引入RAG（GraphRAG），利用实体间关系提升知识可解释性。

**2. 结构化与统一RAG接口**：针对标准文本RAG的局限，一系列研究致力于引入结构化或统一的检索层。例如，基于图的RAG系统构建异构图，节点代表文本片段或实体，边编码语义或链接关系，通过图传播进行检索以改进多跳推理。另一些系统则为混合文档格式构建分层索引，或定义统一的数据模式来训练语言智能体。然而，这些方法常将不同来源的数据压缩成不透明的图或索引，缺乏对模态特定结构的可逆性保留，也未能提供通用的、LLM原生的分段模式以供统一导航。

**3. 基于LLM的多智能体问答系统**：多智能体系统使多个智能体能够协作解决复杂任务，例如通过智能体间的合作进行代码生成或决策。这类系统体现了从孤立模型向协作中心方法的转变。

**本文与这些工作的关系与区别**：RELOOP框架直接建立在RAG和多智能体系统的基础上，旨在解决现有方法在处理多步、异构问答时的不足。其核心创新在于提出了**分层序列（HSEQ）**这一统一、结构感知的接口。与将数据压缩为不透明图的GraphRAG等方法不同，HSEQ将文档、表格和知识图谱线性化为带有轻量级结构标签的**可逆**分层序列，从而保留了原始结构信息。这使得RELOOP能够使用单一策略跨模态操作，无需针对每个数据集进行专门化处理。同时，它通过“头智能体”和“迭代智能体”的协作，实现了**有引导、预算感知的迭代检索**，减少了不必要的跳转和计算开销，并通过证据规范化提高了答案的一致性和可审计性。因此，RELOOP是对现有结构化RAG接口研究方向的一种深化和具体实现，特别强调了结构的可逆性、操作的统一性以及资源消耗的明确控制。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为RELOOP的结构感知框架来解决异构问答中多步推理和证据源整合的难题。其核心方法是将检索过程重构为在统一数据结构上的、有指导的迭代选择，而非传统的单次检索增强生成（RAG）。整体框架包含三个关键模块：HSEQ适配器（HSEQ-A）、RELOOP迭代器（RELOOP-I）和RELOOP头部模块（RELOOP-H）。

首先，HSEQ-A模块负责将异构数据源（文本、表格、知识图谱）线性化为一个统一的、可逆的层次化序列（HSEQ）。每个数据项被转换为一系列带有轻量级结构标签的片段，这些标签记录了层级（如句子、段落、表格行）、父指针、人类可读内容以及标准化元数据。这种表示方式统一了不同模态数据的接口，使得后续处理无需针对特定数据集进行专门化设计。

其次，RELOOP-I模块是一个学习到的迭代策略，它在HSEQ上进行有指导的、预算感知的迭代以收集证据。迭代过程由一个头部模块（RELOOP-H）生成的简洁计划（guidance）所引导。在每一步，策略基于当前问题、已收集证据、候选窗口和预算状态，执行两种核心操作：从候选窗口中选择至多k个最有希望的片段，以及通过结构感知的邻域操作符（如跳转到父/子节点、表格行/列邻居、KG关系）来扩展候选集。迭代由一个预算感知的充分性准则控制，当证据被认为足够或预算耗尽时停止。算法采用滑动窗口机制来管理上下文，确保每一步的计算开销与语料库总大小无关，从而实现了高效率。

最后，RELOOP-H模块承担双重角色：在迭代前生成指导计划，以及在迭代结束后基于规范化后的证据合成最终答案。一个规范器（canonicalizer）会将迭代收集的原始证据片段打包成保留来源信息的紧凑格式供头部模块使用。此外，系统还包含一个可选的精炼循环，当检测到证据矛盾时，会触发一个简短的额外迭代步骤以解决不一致性。

该方法的创新点主要体现在三个方面：1）**格式无关的统一化**：通过HSEQ表示，使单一策略能够跨文本、表格和知识图谱操作，无需针对每种数据模态进行专门化。2）**有指导的、预算感知的迭代**：通过引导计划和充分性判断，减少了不必要的跳转、工具调用和令牌消耗，在保持准确性的同时提升了效率。3）**证据规范化**：提升了答案的一致性和可审计性，为可靠的问答提供了支持。

### Q4: 论文做了哪些实验？

论文在多个异构问答数据集上进行了实验，评估了RELOOP框架在答案质量和效率方面的表现。实验设置包括使用四个基准数据集：HotpotQA（纯文本多跳推理）、TAT-QA（表格与文本混合的金融问答）、HybridQA（维基百科表格与链接文本）以及MetaQA（知识图谱，使用其2跳和3跳问题）。评估指标主要包括准确率（Acc）和F1值，以及反映效率的平均迭代步数和端到端延迟（毫秒）。

对比方法分为三组：1) LLM-only QA，使用多个大语言模型（如Falcon3-10B、Llama-3.1-8B等）直接回答问题；2) 针对特定模态的RAG基线方法，例如针对表格的TAT-LLM、TableRAG，针对文本的TTQA-RS、ODYSSEY，针对混合模态的HippoRAG，以及针对知识图谱的Graph-constrained Reasoning、Think on Graph (ToG)和AdaptiveRAG；3) RELOOP方法本身，报告了最佳代理对和中等代理对的性能，并进行了消融实验（包括无监督微调、无指导信号、仅启发式指导等变体）。

主要结果显示，RELOOP在多数数据集上超越了所有基线。关键数据指标如下：在HotpotQA上，RELOOP最佳配置的Acc/F1达到56.3/58.6，优于最佳基线HippoRAG的53.2/55.7；在MetaQA-2hop和3hop上，RELOOP最佳Acc分别达到95.9和93.4，显著高于图RAG基线；在TAT-QA上，RELOOP最佳Acc为75.7，超过TAT-LLM的73.1；在HybridQA上，RELOOP最佳Acc为66.4，略优于HippoRAG的65.8。效率方面，RELOOP在HotpotQA上的平均迭代步数为4.0，延迟为6247毫秒，远低于ToG的13.28步和22708毫秒，实现了精度与效率的更好平衡。消融实验表明，移除监督微调或指导信号会导致性能显著下降，验证了各组件的重要性。

### Q5: 有什么可以进一步探索的点？

RELOOP框架在异构数据统一检索与推理方面取得了显著进展，但其仍存在一些局限性和可进一步探索的方向。首先，论文提到未来将扩展至动态语料库的多轮/流式场景，这提示了当前系统可能对静态、预定义知识源的依赖较强，在实时更新或交互式对话中可能面临挑战。其次，噪声证据下的充分性判断易产生幻觉，这反映了模型在复杂或冲突信息中稳健推理的不足。

结合个人见解，可能的改进思路包括：1）引入更细粒度的置信度校准机制，例如通过多模型投票或不确定性量化来减少幻觉；2）探索自适应预算分配策略，让模型能动态调整检索深度与广度，以平衡效率与准确性；3）将框架与持续学习结合，使其能在线更新知识表示，适应动态数据流。此外，RELOOP目前侧重于结构化与半结构化数据，未来可扩展至图像、音频等多模态证据源，进一步提升异构QA的通用性。

### Q6: 总结一下论文的主要内容

RELOOP是一个用于异构问答的检索增强生成框架，旨在解决多步问题和异构证据源（文本、表格、知识图谱）上的挑战。其核心贡献在于提出了一种结构感知的迭代检索方法，通过将不同格式的数据统一编码为可逆的层次化序列（HSEQ），并利用轻量级结构标签保留来源信息。该方法采用双智能体协作：头智能体指导检索方向，迭代智能体根据结构感知动作（如父子跳转、表格行列邻居、KG关系）选择并扩展证据序列，在收集足够证据后提前停止以控制成本。最后，头智能体对规范化的证据进行合成生成答案，并可进行矛盾检测与精炼。实验表明，RELOOP在多个基准上均取得了更优的准确率与效率，其优势包括：格式无关的统一表示使单一策略能跨模态工作；预算感知的迭代减少了不必要的跳转和调用；证据规范化提升了答案的一致性与可审计性。该框架在精度与成本间实现了可控权衡，为复杂问答提供了高效可靠的解决方案。
