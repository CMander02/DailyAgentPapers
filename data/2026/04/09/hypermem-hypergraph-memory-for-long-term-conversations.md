---
title: "HyperMem: Hypergraph Memory for Long-Term Conversations"
authors:
  - "Juwei Yue"
  - "Chuanrui Hu"
  - "Jiawei Sheng"
  - "Zuyi Zhou"
  - "Wenyuan Zhang"
  - "Tingwen Liu"
  - "Li Guo"
  - "Yafeng Deng"
date: "2026-04-09"
arxiv_id: "2604.08256"
arxiv_url: "https://arxiv.org/abs/2604.08256"
pdf_url: "https://arxiv.org/pdf/2604.08256v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Long-Term Conversation"
  - "Hypergraph"
  - "Retrieval-Augmented Generation"
  - "Memory Architecture"
  - "Hierarchical Memory"
  - "Conversational Agent"
relevance_score: 8.0
---

# HyperMem: Hypergraph Memory for Long-Term Conversations

## 原始摘要

Long-term memory is essential for conversational agents to maintain coherence, track persistent tasks, and provide personalized interactions across extended dialogues. However, existing approaches as Retrieval-Augmented Generation (RAG) and graph-based memory mostly rely on pairwise relations, which can hardly capture high-order associations, i.e., joint dependencies among multiple elements, causing fragmented retrieval. To this end, we propose HyperMem, a hypergraph-based hierarchical memory architecture that explicitly models such associations using hyperedges. Particularly, HyperMem structures memory into three levels: topics, episodes, and facts, and groups related episodes and their facts via hyperedges, unifying scattered content into coherent units. Leveraging this structure, we design a hybrid lexical-semantic index and a coarse-to-fine retrieval strategy, supporting accurate and efficient retrieval of high-order associations. Experiments on the LoCoMo benchmark show that HyperMem achieves state-of-the-art performance with 92.73% LLM-as-a-judge accuracy, demonstrating the effectiveness of HyperMem for long-term conversations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长对话中智能体因固定上下文窗口限制而难以有效利用历史信息，导致对话连贯性、持续性任务追踪和个性化交互能力不足的问题。当前主流方法如检索增强生成（RAG）和图结构记忆主要依赖成对关系（pairwise relations）来关联信息，但它们在捕捉高阶关联（high-order associations）——即多个元素之间的联合依赖关系——方面存在固有缺陷。例如，在涉及多个主题（如运动和工作）的对话中，相关的事件片段和事实可能分散在不同对话部分，传统方法难以将这些分散内容建模为一个整体，导致检索结果碎片化，无法恢复对话的完整语义连贯性。

因此，本文的核心问题是：如何设计一种记忆架构，能够显式地建模对话中多个元素之间的高阶关联，从而将语义上分散但主题相关的内容统一为连贯单元，以支持更准确、高效的长时记忆检索与利用。为此，论文提出了HyperMem，一种基于超图（hypergraph）的分层记忆架构。它通过超边（hyperedges）显式地对这些高阶关联进行建模，并将记忆组织为三个层次：主题（topics）、事件片段（episodes）和事实（facts）。利用这一结构，论文还设计了混合的词义-语义索引以及从粗到细的检索策略，以实现对高阶关联的完整且高效检索。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为基于检索增强生成（RAG）的显式记忆方法、基于图结构的方法、分层记忆方法以及探索替代范式的非检索方法。

在基于RAG和图结构的方法中，**GraphRAG** 等研究利用知识图谱的拓扑结构进行推理和多跳检索，但它们主要依赖成对的二元关系，难以显式地对多个分散元素之间的高阶关联进行建模。近期有工作初步探索了**超图**来建模多实体关系，但这些方法通常针对静态知识库设计，不适用于对话中持续演化的智能体记忆，且缺乏能保持长期对话语义连贯性的分层检索机制。本文提出的HyperMem则首创将超图用于构建智能体记忆，通过超边显式分组相关记忆，并设计了分层检索策略，以解决上述局限。

在分层记忆建模方面，**RAPTOR、SiReRAG、HiRAG** 等方法构建了树状索引以实现多粒度信息集成。类似地，近期智能体研究如**MemoryBank、A-Mem、G-Memory、LightMem** 等也探索了用于会话持久化的结构化或图基表示，并进一步研究了分层结构与压缩以提高效率。HyperMem与这些工作的共同点是采用了分层结构（主题、情节、事实三级），但其核心创新在于引入了超图来统一分散的内容，形成连贯的语义单元，从而更好地捕获高阶关联。

此外，还有一类研究**避免显式检索**，例如**MemGPT、MemOS** 借鉴操作系统概念进行内存调度，**MIRIX** 通过共享内存协调多智能体状态，而**MemInsight、Mem1** 等采用强化学习优化记忆存储与检索策略。与这些方法不同，HyperMem坚持基于检索的显式记忆架构，但通过超边分组和主题引导的层次检索，确保了在长时间对话中相关记忆的准确、高效召回。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为HyperMem的、基于超图的层次化记忆架构来解决长期对话中高阶关联难以捕获和检索碎片化的问题。其核心方法是利用超图（hypergraph）显式建模话题、情节和事实之间的多元关联，而非传统的成对关系。

整体框架是一个三层级的超图结构：**话题层**捕捉跨越长期交互的共同主题；**情节层**表示时间上连续、描述连贯事件或子对话的片段；**事实层**编码从情节中提取的原子事实，作为精确的检索目标。超边用于连接属于同一话题的多个情节节点，以及属于同一情节的多个事实节点，从而将分散的内容统一为连贯的单元。

构建该记忆涉及三个关键过程：
1.  **情节检测**：采用基于LLM的流式边界检测机制，将原始对话流增量式地分割成语义连贯的情节单元。每个情节节点包含原始对话、标题和叙述性摘要。
2.  **话题聚合**：设计基于LLM的流式话题聚合机制。通过检索历史相似情节，判断当前情节应初始化新话题、创建新话题还是更新已有话题，并生成或更新话题的标题与摘要。随后构建连接话题与其所有组成情节的超边，并由LLM为每个情节分配重要性权重。
3.  **事实提取**：在话题及其关联情节的上下文中，使用LLM提取突出的、基于语境的事实断言。每个事实节点包含内容、可能回答的查询模式（用于主动对齐用户意图）以及关键词。同时构建连接情节与其所有事实的超边，并为每个事实分配重要性权重。

为了支持高效、准确的检索，论文设计了**混合词汇-语义索引**与**由粗到细的检索策略**。创新点包括：
*   **双索引构建**：为所有节点类型同时构建基于BM25的稀疏关键词索引和基于嵌入模型的稠密语义索引。
*   **超图嵌入传播**：提出一种轻量级的嵌入传播机制，通过超边聚合信息来丰富节点表示，使语义相关的记忆获得对齐的嵌入，从而促进检索时的高阶关联。
*   **分层检索流程**：检索时，首先在话题层进行检索，筛选出相关话题；然后通过超边扩展到这些话题下的情节进行二次检索；最后再扩展到相关情节下的事实进行精细检索。每个阶段都结合了RRF排名融合和重排序模型来提升精度。
*   **响应生成优化**：最终的响应上下文主要基于检索到的事实内容构建，并可选择性补充上层情节的摘要以提供叙事背景，这显著减少了令牌消耗，同时保留了可回答的信息。

通过这种架构，HyperMem能够显式建模和高效检索对话元素间的高阶关联，从而在长期对话中实现更连贯、更准确的记忆访问。

### Q4: 论文做了哪些实验？

论文在LoCoMo基准测试上进行了全面的实验评估。实验设置方面，作者使用Qwen3-Embedding-4B进行语义编码，Qwen3-Reranker-4B进行重排序，并采用GPT-4.1-mini进行思维链推理生成答案。在分层检索中，首先检索100个初始候选，然后选择前10个主题、前10个片段和前30个事实作为最终上下文。节点嵌入更新时使用传播权重λ=0.5以融入超边信息。评估使用GPT-4o-mini作为LLM评判员，报告3次独立运行的平均分数。

对比方法包括两大类：基于RAG的方法（GraphRAG、LightRAG、HippoRAG 2、HyperGraphRAG）和记忆系统方法（OpenAI、LangMem、Zep、A-Mem、Mem0、MIRIX、Memobase等）。主要结果如下：HyperMem在整体准确率上达到92.73%，显著优于最强的RAG方法HyperGraphRAG（86.49%）和最佳记忆系统MIRIX（85.38%）。在具体问题类别上，单跳问题准确率为96.08%，多跳问题为93.62%，时序推理问题为89.72%，开放域问题为70.83%。关键数据指标显示，在多跳问题上相比LightRAG提升9.58%，在单跳问题上相比HyperGraphRAG提升5.47%。

此外，论文还进行了消融实验和超参数敏感性分析。消融实验表明，移除片段上下文（EC）导致整体性能下降3.76%，对时序推理影响最大（下降5.61%）。超参数分析显示，主题层Top-k值从1增加到10可使准确率从76.88%提升至92.66%，而片段层Top-k值在10到20之间变化时性能稳定。效率分析显示，HyperMem在仅使用2.5倍令牌时即可达到89.48%的准确率，显著优于需要25-35倍令牌的RAG方法。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于其单用户假设和开放域问题的处理能力。未来研究可首先探索多用户/多代理场景下的内存架构，这需要设计细粒度的访问控制、隐私保护机制以及可能的分层或分区超图结构，以隔离和共享不同用户的记忆。其次，可深化与外部知识库（如维基百科、领域数据库）的集成，以应对开放域查询；一种思路是将外部知识实体作为超图节点动态引入，或设计一个混合检索系统，协同查询内部对话记忆和外部知识。此外，超边的构建目前可能依赖启发式方法，未来可研究利用LLM自动识别和演化高阶关联，使记忆结构更具动态性和适应性。最后，在效率方面，可探索超图索引的近似检索算法或压缩技术，以支持更大规模的长期对话应用。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为HyperMem的新型记忆架构，旨在解决长期对话中智能体记忆碎片化的问题。现有方法如检索增强生成（RAG）和图记忆主要依赖二元关系，难以捕捉多个元素间的高阶关联，导致检索内容不连贯。

论文的核心贡献是引入了基于超图的层次化记忆结构。该方法将记忆组织为三个层级：主题、事件和事实，并使用超边将相关的事件及其事实分组，从而将分散的内容整合为连贯单元。基于此结构，作者设计了一种混合的词法-语义索引以及从粗到细的检索策略，以支持对高阶关联进行准确且高效的检索。

实验在LoCoMo基准上进行，结果表明HyperMem达到了最先进的性能，其基于大语言模型的评判准确率达到92.73%。这验证了HyperMem在建模高阶关联、提升长期对话连贯性和个性化交互方面的有效性。
