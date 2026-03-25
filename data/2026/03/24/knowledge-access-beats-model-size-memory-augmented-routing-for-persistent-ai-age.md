---
title: "Knowledge Access Beats Model Size: Memory Augmented Routing for Persistent AI Agents"
authors:
  - "Xunzhuo Liu"
  - "Bowei He"
  - "Xue Liu"
  - "Andy Luo"
  - "Haichen Zhang"
  - "Huamin Chen"
date: "2026-03-24"
arxiv_id: "2603.23013"
arxiv_url: "https://arxiv.org/abs/2603.23013"
pdf_url: "https://arxiv.org/pdf/2603.23013v1"
categories:
  - "cs.CL"
tags:
  - "Memory-Augmented Agents"
  - "Inference Efficiency"
  - "Retrieval-Augmented Generation"
  - "Persistent Agents"
  - "Model Routing"
  - "Conversational Memory"
  - "Cost-Effective Inference"
relevance_score: 8.5
---

# Knowledge Access Beats Model Size: Memory Augmented Routing for Persistent AI Agents

## 原始摘要

Production AI agents frequently receive user-specific queries that are highly repetitive, with up to 47\% being semantically similar to prior interactions, yet each query is typically processed with the same computational cost. We argue that this redundancy can be exploited through conversational memory, transforming repetition from a cost burden into an efficiency advantage. We propose a memory-augmented inference framework in which a lightweight 8B-parameter model leverages retrieved conversational context to answer all queries via a low-cost inference path. Without any additional training or labeled data, this approach achieves 30.5\% F1, recovering 69\% of the performance of a full-context 235B model while reducing effective cost by 96\%. Notably, a 235B model without memory (13.7\% F1) underperforms even the standalone 8B model (15.4\% F1), indicating that for user-specific queries, access to relevant knowledge outweighs model scale. We further analyze the role of routing and confidence. At practical confidence thresholds, routing alone already directs 96\% of queries to the small model, but yields poor accuracy (13.0\% F1) due to confident hallucinations. Memory does not substantially alter routing decisions; instead, it improves correctness by grounding responses in retrieved user-specific information. As conversational memory accumulates over time, coverage of recurring topics increases, further narrowing the performance gap. We evaluate on 152 LoCoMo questions (Qwen3-8B/235B) and 500 LongMemEval questions. Incorporating hybrid retrieval (BM25 + cosine similarity) improves performance by an additional +7.7 F1, demonstrating that retrieval quality directly enhances end-to-end system performance. Overall, our results highlight that memory, rather than model size, is the primary driver of accuracy and efficiency in persistent AI agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决生产环境中AI智能体（如个人助手、客服代理）面临的核心矛盾：处理大量重复性用户查询时，如何在保证回答质量的同时显著降低计算成本。研究背景是，当前大型语言模型（如235B参数）虽然回答质量高，但推理成本极其昂贵；而小型模型（如8B参数）成本低，却缺乏对用户历史对话知识的记忆，导致面对用户特定问题时只能猜测或产生幻觉（即自信地编造错误答案）。现有方法主要分为两类：检索增强生成（RAG）通过检索历史信息提升答案质量，但通常假设使用固定模型；模型路由（routing）则根据查询难度将问题分配给不同规模的模型以优化成本，但假设输入是固定的。这两种技术以往被孤立研究，尚未探讨它们结合时的相互作用，而实际部署中这种结合的效果并不直观——记忆注入可能帮助小型模型更自信地处理用户特定问题，也可能因引入无关上下文而干扰路由决策。

本文要解决的核心问题是：如何通过结合记忆增强和模型路由，构建一个高效且持久的AI智能体框架，以利用对话中的重复性（高达47%的查询语义相似）将成本负担转化为效率优势。具体而言，论文提出一个无需额外训练或标注数据的记忆增强推理框架，其中轻量级8B参数模型通过检索相关对话上下文，能够以低成本路径回答所有查询。研究发现，对于用户特定查询，知识访问比模型规模更重要——即使没有记忆，235B大模型的性能（13.7% F1）甚至低于独立8B小模型（15.4% F1），而结合记忆后，8B模型性能提升至30.5% F1，恢复了235B模型69%的性能，同时成本降低96%。关键洞见在于：路由本身在实用置信度阈值下已将96%的查询导向小模型，但若无记忆，小模型会因自信幻觉导致准确率低下（13.0% F1）；记忆并非主要改变路由决策，而是通过基于检索到的用户特定信息夯实回答，将“自信错误”转化为“自信正确”，从而使路由在节省成本的同时保证质量。此外，论文通过实验量化了这种协同效益，并分析了混合检索（BM25+余弦相似度）对端到端性能的进一步提升（+7.7 F1），强调了在持久AI智能体中，记忆而非模型规模是准确性和效率的主要驱动力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 对话记忆系统**：如 Mem0（基于图的记忆提取）、MemGPT（操作系统启发的分层内存）以及 Zep、LangMem 等 SDK。这些工作专注于记忆系统本身的设计。本文则进一步研究记忆如何与模型路由决策交互，特别是检索到的上下文是否会影响小模型的置信度信号。

**2. 模型路由与级联**：如 FrugalGPT（基于输出对数概率的级联）、RouteLLM（训练偏好分类器路由）、AutoMix（少样本自验证）以及 Dekoninck 等人将路由与级联统一的最优框架。这些方法将路由视为独立优化问题。本文的贡献在于揭示了路由与记忆注入的协同作用，并指出在缺乏记忆时，置信度信号会与答案正确性解耦（即模型可能“自信地犯错”）。

**3. 基于对数概率的置信度估计**：一系列研究探讨了使用令牌级对数概率作为LLM的置信度信号，涉及模型校准（Kadavath等人）、校准修正（Guo等人）、幻觉检测（Varshney等人）以及白盒与黑盒置信度方法比较（Xiong等人）。本文在此基础上，将该信号用于二元路由决策，并揭示了在用户特定问题上，即使模型自信，答案也可能因缺乏相关知识而错误。

**4. 跨模型规模的知识迁移**：传统方法如知识蒸馏通过训练学生模型来迁移知识。RetriKT 提出了基于检索的替代方案，将大模型知识提取到存储中供小模型查询。本文的跨模型记忆注入将此原则扩展到对话系统，使从小模型和大模型交互中积累的记忆都能被检索，且无需重新训练。

**5. RAG中的检索质量与噪声**：相关研究（如 Shi 等人）表明不相关的检索上下文会降低LLM性能。因此，本文选择存储逐字对话轮次对，而非LLM生成的摘要，以避免与检索噪声复合的幻觉风险。

**6. 混合检索**：研究指出，结合稠密检索（擅长语义匹配）和BM25（擅长关键词匹配）的混合方法在开放域QA中表现更优。本文在对话记忆场景中研究了混合检索，以应对从事实查找（BM25擅长）到语义推理（稠密检索擅长）的各种查询。

**7. 智能体工作负载中的重复性**：生产数据表明智能体查询高度重复。现有方法通过语义缓存或计划复用来利用这一点，直接复用之前的输出。本文的方法是互补的：它将知识缓存为对话记忆，供小模型生成新鲜且上下文合适的响应，这对于需要基于累积知识进行推理（而非重播旧答案）的个性化智能体至关重要。

### Q3: 论文如何解决这个问题？

论文通过一个结合了记忆增强、路由决策和混合检索的复合推理框架来解决用户查询高度重复带来的计算成本问题。其核心思想是利用对话记忆将重复查询从成本负担转化为效率优势，而非单纯依赖增大模型规模。

整体框架是一个位于客户端和推理后端之间的路由层。主要包含三个关键组件：**记忆存储与检索模块**、**提示增强模块**和**基于置信度的路由模块**。工作流程如下：首先，系统将每次对话的“用户问题-模型回答”对（turn-pair）存入按用户分区的向量数据库，记录包含文本、嵌入向量和元数据。当新查询到达时，路由层通过**混合检索**（结合稠密向量余弦相似度和稀疏BM25关键词匹配）从记忆库中召回最相关的k条历史记录。这些记忆被作为系统上下文注入到提示中，形成增强提示。

随后，系统执行**“探测-升级”路由策略**。增强提示首先被发送给成本最低的小模型（8B参数），并获取其输出序列的平均对数概率。该概率经过归一化处理（设定一个最小值下限）后，被映射为一个[0,1]区间的置信度分数c。如果c超过预设阈值τ，则直接接受小模型的回答作为最终响应（低成本路径）；否则，查询将“升级”至昂贵的大模型（235B参数）进行处理。无论走哪条路径，本次交互的问答对都会被存储，以持续扩充记忆库。

该方法的创新点在于其**复合协同效应**：
1.  **记忆增强提供事实依据**：通过检索并注入用户特定的历史对话信息，为模型（尤其是小模型）提供了回答所需的精准知识背景，从根本上提升了答案的正确性。实验表明，记忆使小模型的F1分数从15.4%提升至30.5%。
2.  **路由机制保障成本效率**：基于模型自身输出概率的零样本置信度估计，实现了查询的自动分流。在实用阈值下，96%的查询能被路由到小模型，大幅降低计算成本（有效成本降低96%）。
3.  **两者协同实现质效兼得**：论文指出，单纯路由会导致小模型因“自信的幻觉”而产生低质量回答；单纯记忆则无法降低成本。二者的结合是关键：记忆将小模型“自信但错误”的答案转变为“自信且正确”的答案，而路由决策本身（即流向小模型的比例）并未被显著改变，从而实现了准确性与效率的同步提升。
4.  **跨模型记忆积累与摊销**：记忆库是跨模型共享的，即大模型处理查询后产生的优质回答会被存储，后续小模型也能利用这些知识。随着时间推移，记忆覆盖的重复话题增多，小模型能正确处理的查询比例上升，性能差距逐渐缩小，实现了早期高成本投入的“摊销”。

此外，**混合检索技术**是提升记忆相关性的关键技术。它同时利用语义匹配（处理同义、转述）和词汇匹配（处理专有名词、日期等精确信息），相比单一稠密检索，能额外带来+7.7 F1的性能提升，确保了检索质量直接增强端到端系统性能。

### Q4: 论文做了哪些实验？

论文在实验设置上，主要使用了两个模型：Qwen3-VL-8B-Instruct（8B参数）和Qwen3-VL-235B-A22B-Instruct-AWQ（235B参数），并在单个GPU上同时运行。记忆存储使用Milvus向量数据库，嵌入模型为2D Matryoshka。

实验基于两个数据集：1）**LoCoMo**：一个包含19个会话、214轮对话的对话记忆QA基准，用于测试记忆与路由的协同效应，包含152个问题（单跳70、多跳40、开放域12、时序30）。2）**LongMemEval**：一个来自ICLR 2025的多会话对话基准，包含500个问题，每个问题对应约48个会话的“干草堆”背景，用于更稳健地评估检索策略。

对比方法上，在LoCoMo上设计了六种实验条件以形成2×2因子设计（记忆×路由），包括：Cold 8B（无记忆、无路由的小模型基线）、Cold compound（无记忆+置信度路由）、Warm memory only（仅记忆检索注入8B模型）、Warm compound（记忆检索+置信度路由的完整流程）、Cold 235B（无记忆、无路由的大模型基线）以及Full-context 235B（将所有会话历史提供给235B模型，作为质量上限）。在LongMemEval上，则比较了纯余弦相似度检索与混合检索（BM25+余弦相似度）在完整路由流程中的表现。

主要结果方面：在LoCoMo上，完整的记忆增强路由流程（Warm compound）取得了30.5%的F1分数，相比无记忆的8B模型（15.4%）提升了15.0个百分点，恢复了全上下文235B模型性能（43.9%）的69%，同时有效成本降低了96%。值得注意的是，无记忆的235B模型（13.7% F1）甚至表现不如无记忆的8B模型，凸显了对于用户特定查询，相关知识访问比模型规模更重要。路由行为几乎不受记忆影响（在置信度阈值τ=0.50时，96%的查询由小模型处理），但记忆通过基于检索到的用户特定信息来生成回答，将准确率从Cold compound的13.0% F1大幅提升至30.5%。在LongMemEval上，混合检索相比纯余弦检索带来了+7.7 F1的显著提升（从36.5%到44.2%），尤其在知识更新（+26.7 F1）和单会话用户（+19.0 F1）等问题类型上增益最大，证明了检索质量直接提升端到端系统性能。关键数据指标包括：F1分数、BLEU-1、有效成本（EffCost）以及由小模型处理的查询比例。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来研究可以从以下几个方向深入探索。首先，论文指出当前方法在时间推理方面存在局限，仅依赖带时间戳前缀的对话对无法有效处理时序问题，未来可探索结构化时间索引（如时间轴表示或时序感知嵌入）来增强记忆系统对时间关系的理解。其次，论文强调记忆保真度是关键前提，若记忆内容存在幻觉会导致性能下降，因此需研究更可靠的记忆存储与更新机制，例如引入验证或纠错模块，防止错误信息积累。此外，当前路由决策主要基于模型置信度，但置信度可能存在误校准，未来可结合不确定性估计或多指标路由（如查询复杂度分析）来优化分流策略。从系统层面看，论文实验基于相对有限的基准，需在真实生产环境中验证其长期效果，特别是冷启动阶段记忆积累的动态过程及其对性能的影响。最后，检索质量直接影响整体性能，可进一步探索更先进的混合检索技术（如结合知识图谱），或使检索模块与生成模型进行端到端协同优化，以更好地捕捉语义与实体之间的互补信号。

### Q6: 总结一下论文的主要内容

本文针对生产环境中AI代理处理用户查询时存在大量语义重复（高达47%）导致计算成本高昂的问题，提出了一种基于记忆增强和路由的推理框架。核心思想是将重复查询从成本负担转化为效率优势，通过利用对话记忆来提升小模型的性能，而非单纯依赖扩大模型规模。

论文的方法概述是：采用一个轻量级的80亿参数模型作为主要推理路径，并为其配备一个检索增强的对话记忆系统。系统首先基于置信度路由决定是否将查询交由小模型处理；对于路由到小模型的查询，会从累积的用户特定对话历史中检索相关上下文，以此为基础生成回答，从而大幅降低成本。

主要结论和贡献在于：第一，实证表明对于用户特定查询，相关知识的访问比模型规模更重要。一个无记忆的2350亿参数模型性能（13.7% F1）甚至低于独立的80亿参数模型（15.4% F1）。第二，所提出的记忆增强框架，在不需额外训练或标注数据的情况下，使小模型达到了30.5%的F1分数，恢复了大型模型69%的性能，同时将有效成本降低了96%。第三，分析发现，路由本身已将96%的查询导向小模型，但若无记忆支撑，小模型会产生自信的幻觉导致准确率低（13.0% F1）。记忆的作用并非改变路由决策，而是通过基于检索到的用户特定信息生成回答来提升答案的正确性。随着对话记忆的积累，系统对重复话题的覆盖度增加，性能差距进一步缩小。此外，采用混合检索（BM25 + 余弦相似度）能额外提升7.7个F1点，证明了检索质量对端到端性能的直接增强作用。总之，该研究强调了在持久性AI智能体中，记忆而非模型规模，是驱动准确性和效率提升的主要因素。
