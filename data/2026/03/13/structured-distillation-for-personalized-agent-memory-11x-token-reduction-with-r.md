---
title: "Structured Distillation for Personalized Agent Memory: 11x Token Reduction with Retrieval Preservation"
authors:
  - "Sydney Lewis"
date: "2026-03-13"
arxiv_id: "2603.13017"
arxiv_url: "https://arxiv.org/abs/2603.13017"
pdf_url: "https://arxiv.org/pdf/2603.13017v1"
github_url: "https://github.com/Process-Point-Technologies-Corporation/searchat"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.IR"
tags:
  - "Agent Memory"
  - "Retrieval-Augmented Generation"
  - "Long-Context Management"
  - "Personalization"
  - "Information Distillation"
  - "Software Engineering Agent"
relevance_score: 7.5
---

# Structured Distillation for Personalized Agent Memory: 11x Token Reduction with Retrieval Preservation

## 原始摘要

Long conversations with an AI agent create a simple problem for one user: the history is useful, but carrying it verbatim is expensive. We study personalized agent memory: one user's conversation history with an agent, distilled into a compact retrieval layer for later search. Each exchange is compressed into a compound object with four fields (exchange_core, specific_context, thematic room_assignments, and regex-extracted files_touched). The searchable distilled text averages 38 tokens per exchange. Applied to 4,182 conversations (14,340 exchanges) from 6 software engineering projects, the method reduces average exchange length from 371 to 38 tokens, yielding 11x compression. We evaluate whether personalized recall survives that compression using 201 recall-oriented queries, 107 configurations spanning 5 pure and 5 cross-layer search modes, and 5 LLM graders (214,519 consensus-graded query-result pairs). The best pure distilled configuration reaches 96% of the best verbatim MRR (0.717 vs 0.745). Results are mechanism-dependent. All 20 vector search configurations remain non-significant after Bonferroni correction, while all 20 BM25 configurations degrade significantly (effect sizes |d|=0.031-0.756). The best cross-layer setup slightly exceeds the best pure verbatim baseline (MRR 0.759). Structured distillation compresses single-user agent memory without uniformly sacrificing retrieval quality. At 1/11 the context cost, thousands of exchanges fit within a single prompt while the verbatim source remains available for drill-down. We release the implementation and analysis pipeline as open-source software.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI智能体与单个用户进行长期对话时产生的历史记录存储和检索效率问题。随着对话历史的增长，直接保存原始对话内容（verbatim）会导致token数量急剧膨胀，占用大量上下文窗口资源，使得检索成本高昂且不切实际。研究背景是，在软件工程等持续协作场景中，开发者与AI助手会积累大量对话，其中包含许多对后续工作有价值的决策、错误解决等关键信息，但现有方法往往面临两难选择：要么完整保存历史导致资源压力，要么采用通用的摘要压缩方法，但这类方法缺乏结构化指导，容易在多次压缩中丢失重要信息，且无法保证检索质量。

现有方法的不足主要体现在：主流的检索增强生成（RAG）方法需要加载大量原始对话文本，token开销巨大；而常见的压缩策略（如LLM驱动的通用摘要）是无结构、无目标的“黑箱”操作，压缩过程中没有明确的提取目标，可能导致关键信息丢失，且多次迭代压缩会不断劣化信息质量。此外，这些方法通常忽略了原始对话数据其实仍保存在本地磁盘中，只是未被有效索引和利用。

本文要解决的核心问题是：能否为单个用户的持久化对话历史构建一个紧凑的、结构化的记忆层，在实现大幅压缩（论文中达到11倍的token减少）的同时，保持与原始对话相近的检索效果？为此，论文提出了结构化蒸馏方法，将每个对话交换（exchange）提取为包含四个字段（如exchange_core、specific_context等）的复合对象，从而保留可检索的核心信息，并系统评估了在纯蒸馏检索、跨层检索等多种配置下的个性化召回性能，最终证明该方法能在极低成本下维持检索质量，实现索引与显示分离的两层架构。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：记忆管理系统、对话摘要方法和提示压缩技术。

在记忆管理系统方面，MemGPT将记忆管理构建为层次结构，将旧上下文移出即时窗口以供后续检索。本文的研究范围更窄、更具体，专注于单用户与智能体的对话历史，并探讨如何将其蒸馏为紧凑的检索层，同时保持检索能力。关键区别在于本文采用了结构化表示（包含四个字段的复合对象），并将蒸馏文本作为索引而非直接面向用户的输出，检索时返回原始对话，实现了检索表示与显示证据的分离。

在对话摘要领域，现有工作包括提取式方法（选择原文片段）、抽象式方法（生成新文本）和运行摘要方法（维护滚动摘要）。本文不旨在生成精炼的运行摘要，而是研究将每个对话交换蒸馏为结构化对象后，在保留原文供深入查看的前提下，检索质量能在多大程度上得以保持。本文特别强调“幸存词汇原则”，要求大语言模型重用参与者的措辞而非自由释义，以保留关键技术术语。

在提示压缩技术方面，如LLMLingua等方法通过在推理时移除低信息量token来减少token数量，其优化目标是单次推理调用。本文方法则不同，是离线蒸馏成可搜索的结构化对象，输出不仅是更短的文本，而且是可通过关键词和语义搜索进行检索的独立表示。此外，本文的应用场景也更为特定，专注于个性化的单用户对话历史压缩，而非通用的公共基准或跨用户语料库。

### Q3: 论文如何解决这个问题？

论文通过一种名为“结构化蒸馏”的方法来解决长对话历史存储成本高昂的问题。其核心是将冗长的原始对话历史压缩成一个紧凑的、可检索的表示层，同时尽可能保留未来检索所需的关键信息。

**整体框架与主要模块**：
该方法首先将对话流按“回合”进行结构化分割。每个完整的用户-助手交互被定义为一个“回合”。随后，每个回合被蒸馏成一个包含四个字段的复合对象：
1.  **回合核心**：由LLM生成，用1-2句话概括该回合完成的事项，类似于提交信息。
2.  **具体上下文**：由LLM生成，提炼出一个具有区分度的技术细节，类似于代码差异。
3.  **主题房间分配**：由LLM生成，将回合内容分配到1-3个主题“房间”中，类似于目录树分类。
4.  **涉及文件**：通过正则表达式从原始文本中提取引用的文件路径。

这些字段共同构成平均仅38个令牌的“蒸馏文本”，用于后续检索。原始对话文本则被完整保留，通过蒸馏对象中的元数据（对话ID、回合起止位置）进行关联，确保用户最终看到的是原始内容。

**关键技术细节与创新点**：
1.  **词汇保留原则**：指导LLM在生成“回合核心”和“具体上下文”时，必须重用对话中出现的具体术语（如“连接池超时”），而非自由意译。这确保了未来查询中可能使用的关键词汇得以保留在蒸馏文本中，从而维持检索有效性。数据证实，查询词汇的保留率很高，而丢失的多是罕见且很少被查询的交换特定词汇。
2.  **双层检索架构**：系统为原始文本和蒸馏文本分别构建了独立的检索索引。对于蒸馏文本，由于其长度很短，每个对象生成一个向量（使用轻量级嵌入模型all-MiniLM-L6-v2），并存储在FAISS向量索引中；同时，也为所有字段的拼接文本构建了BM25关键词索引。
3.  **多模式检索与融合策略**：论文系统性地评估了多种检索配置：
    *   **纯模式**：仅在单一文本层（原始层或蒸馏层）使用单一检索机制（如向量搜索HNSW或关键词搜索BM25）。对于包含多个字段的蒸馏对象，测试了多种结果融合策略。
    *   **跨层模式**：**这是关键创新之一**。同时使用原始层和蒸馏层进行检索，然后将两个结果列表融合。例如，用BM25搜索原始文本（获取精确关键词匹配），同时用HNSW向量搜索蒸馏文本（获取语义匹配），再进行加权融合。实验表明，最佳的跨层配置（MRR 0.759）甚至略微超过了最佳纯原始文本基线（MRR 0.745）。
4.  **效果与机制依赖性**：压缩效果显著，平均将每个回合从371个令牌压缩至38个令牌，实现11倍的压缩率。在检索质量上，最佳纯蒸馏配置达到了最佳原始文本配置96%的MRR值（0.717 vs 0.745）。结果高度依赖于检索机制：所有向量搜索配置在压缩后性能下降不显著，而所有BM25配置则出现显著下降。这凸显了在压缩文本上，语义向量搜索比依赖精确词汇重叠的BM25更具鲁棒性。

总之，该方法通过**结构化字段设计**、**严格的术语保留原则**以及**创新的跨层检索融合**，在实现极高压缩比的同时，非但没有统一牺牲检索质量，反而通过巧妙的信号组合，在部分配置下实现了与原始基线相当甚至更优的检索性能。

### Q4: 论文做了哪些实验？

论文实验围绕个性化智能体记忆的结构化蒸馏方法展开，旨在验证压缩后的记忆能否保持检索效果。实验设置方面，研究使用了一个单用户真实对话语料库，包含来自6个软件工程项目的4,182次对话（共14,340次交换）。核心方法是将每次对话交换压缩为一个结构化对象（称为“宫殿对象”），包含四个字段（exchange_core, specific_context, thematic room_assignments, regex-extracted files_touched），使平均长度从371个token降至38个token，实现了11倍的压缩比。

数据集基于用户与Claude Code的实际交互历史，涵盖调试、功能实现、代码审查等任务。评估时构建了201个面向回忆的查询，分为概念性、短语和精确术语三类。检索配置共107种，涵盖5种纯检索模式（如BM25、HNSW向量搜索）和5种跨层融合模式。评估采用5个本地LLM（如Qwen3-8B、Phi-3.5-Mini）对查询-结果对进行独立评分（0-3级），最终通过多数投票达成共识，共产生214,519个共识评分对。

主要结果以MRR（平均倒数排名）为核心指标。最佳纯蒸馏配置的MRR为0.717，达到了最佳原始文本基线（MRR 0.745）的96%。检索效果高度依赖于机制：所有20种向量搜索配置在Bonferroni校正后均未出现显著性能下降，而所有20种BM25配置则显著退化（效应大小|d|=0.031-0.756）。最佳跨层设置（融合原始文本BM25与蒸馏文本HNSW）的MRR为0.759，略优于最佳纯原始文本基线。此外，精确术语查询在部分蒸馏配置中表现优于原始文本，而概念性查询的蒸馏性能下降最明显。关键指标包括：压缩比11倍，蒸馏后平均交换长度38 token，最佳蒸馏MRR 0.717，最佳原始文本MRR 0.745，最佳跨层MRR 0.759。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估主要集中于软件工程领域的对话，在其他领域（如客服、教育）的泛化能力尚不明确。结构化蒸馏的四个字段设计可能过于领域特定，且依赖于正则表达式提取，在非结构化或跨领域对话中可能失效。此外，实验仅测试了检索效果，未评估压缩后记忆对下游任务（如决策连贯性、个性化推荐）的实际影响。

未来研究方向包括：1）探索自适应字段结构，利用LLM动态生成压缩模式，以提升跨领域适应性；2）研究分层蒸馏策略，根据对话重要性进行差异化压缩，平衡保真度与效率；3）将记忆蒸馏与增量学习结合，支持动态更新而无需全局重压缩；4）在更多元场景（如多轮医疗咨询、创意协作）中验证方法，并量化压缩对长期用户体验的影响。此外，可探索神经符号结合的方法，将结构化字段与隐式语义嵌入融合，以增强对模糊查询的鲁棒性。

### Q6: 总结一下论文的主要内容

该论文研究个性化智能体记忆的高效压缩问题，旨在解决长对话历史直接存储带来的高计算成本。核心贡献是提出一种结构化蒸馏方法，将单用户与智能体的对话历史压缩为紧凑的可检索层。方法上，它将每次对话交换提炼为包含四个字段（交换核心、具体上下文、主题房间分配、正则提取的文件操作）的复合对象，使平均可检索文本从371个令牌降至38个令牌，实现11倍压缩。通过在大规模软件工程对话数据集上评估，使用多种检索配置和LLM评分，研究发现最佳纯蒸馏配置的检索效果（MRR 0.717）可达原始逐字检索的96%，且最佳跨层设置（MRR 0.759）甚至略优于原始基线。结论表明，该方法能大幅降低存储开销而不均匀牺牲检索质量，使数千次对话交换可纳入单个提示，同时保留原始细节供深入查询。
