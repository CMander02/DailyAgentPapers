---
title: "GAAMA: Graph Augmented Associative Memory for Agents"
authors:
  - "Swarna Kamal Paul"
  - "Shubhendu Sharma"
  - "Nitin Sareen"
date: "2026-03-29"
arxiv_id: "2603.27910"
arxiv_url: "https://arxiv.org/abs/2603.27910"
pdf_url: "https://arxiv.org/pdf/2603.27910v1"
categories:
  - "cs.AI"
  - "cs.IR"
  - "cs.MA"
tags:
  - "Agent Memory"
  - "Knowledge Graph"
  - "Retrieval-Augmented Generation (RAG)"
  - "Multi-Session Interaction"
  - "Long-Term Memory"
  - "Personalized Agent"
  - "Graph-Based Retrieval"
  - "Hierarchical Reasoning"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# GAAMA: Graph Augmented Associative Memory for Agents

## 原始摘要

AI agents that interact with users across multiple sessions require persistent long-term memory to maintain coherent, personalized behavior. Current approaches either rely on flat retrieval-augmented generation (RAG), which loses structural relationships between memories, or use memory compression and vector retrieval that cannot capture the associative structure of multi-session conversations. There are few graph based techniques proposed in the literature, however they still suffer from hub dominated retrieval and poor hierarchical reasoning over evolving memory. We propose GAAMA, a graph-augmented associative memory system that constructs a concept-mediated hierarchical knowledge graph through a three-step pipeline: (1)~verbatim episode preservation from raw conversations, (2)~LLM-based extraction of atomic facts and topic-level concept nodes, and (3)~synthesis of higher-order reflections. The resulting graph uses four node types (episode, fact, reflection, concept) connected by five structural edge types, with concept nodes providing cross-cutting traversal paths that complement semantic similarity. Retrieval combines cosine-similarity-based $k$-nearest neighbor search with edge-type-aware Personalized PageRank (PPR) through an additive scoring function. On the LoCoMo-10 benchmark (1,540 questions across 10 multi-session conversations), GAAMA achieves 78.9\% mean reward, outperforming a tuned RAG baseline (75.0\%), HippoRAG (69.9\%), A-Mem (47.2\%), and Nemori (52.1\%). Ablation analysis shows that augmenting graph-traversal-based ranking (Personalized PageRank) with semantic search consistently improves over pure semantic search on graph nodes (+1.0 percentage point overall).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI智能体在多轮会话中长期记忆管理的关键问题。研究背景是，随着AI智能体（如客服助手、个人助理）与用户进行跨越多轮会话的持续交互，它们需要持久的长时记忆来维持连贯、个性化的行为。现有方法存在明显不足：基于扁平检索增强生成（RAG）的方法仅依赖嵌入相似性进行文本块检索，丢失了记忆之间的结构关系（如实体、事件间的关联）；而基于记忆压缩和向量检索的方法则难以捕捉多轮会话中的联想结构。尽管已有少数图技术被提出（如HippoRAG），但它们仍受限于“枢纽节点主导检索”的问题——实体节点积累过多边，导致个性化PageRank（PPR）权重分散、检索精度下降，且对动态演化的记忆缺乏有效的层次推理能力。

本文的核心问题是：如何构建一个能够有效存储、组织并检索多轮会话记忆的系统，既能保留记忆间的结构化关联，又能避免因图结构失衡导致的检索性能退化。为此，论文提出了GAAMA（图增强联想记忆系统），通过引入概念介导的层次知识图谱（包含对话片段、事实、反思、概念四类节点及五类结构边），结合语义相似性搜索与边类型感知的个性化PageRank混合检索，旨在实现更精准、关联性更强的记忆检索，从而提升智能体在长期交互中的上下文一致性与推理能力。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕智能体长期记忆架构展开，可分为以下几类：

**1. 基于知识图谱的检索方法**：HippoRAG 利用 OpenIE 三元组构建图谱，通过 Personalized PageRank (PPR) 进行检索，但其以实体为中心的设计在多轮对话中易形成“枢纽节点”，导致精度下降。GAAMA 同样使用 PPR，但引入了边类型感知的权重和枢纽抑制机制，并增加了概念节点作为跨会话的遍历路径，以缓解枢纽主导问题。

**2. 结构化记忆网络与压缩方法**：A-Mem 受 Zettelkasten 启发，构建了带有关键词和链接的记忆网络，但检索仅依赖嵌入相似度，缺乏图上的相关性传播。SimpleMem 通过语义结构化压缩和意图感知检索来实现信息浓缩，其优势在于信息密度而非图结构。Nemori 则会话分割为叙事片段并进行语义提炼，但检索仍基于向量相似度，未利用图关联路径。

**3. 基于学习的记忆管理策略**：AgeMem 将长短期记忆管理统一为智能体的可学习策略，通过强化学习训练记忆操作。这与 GAAMA 形成互补：前者侧重于“何时及如何”存储检索的决策策略，而 GAAMA 聚焦于“如何更好地”利用图结构进行检索与推理。

**4. 检索增强生成（RAG）及其图扩展**：传统 RAG 使用向量检索，虽能应对单跳事实查询，但丢失了记忆间的结构关系。GraphRAG 等图扩展方法为静态文档设计，难以直接适用于动态演进的对话记忆。GAAMA 针对多会话场景，构建了包含事件、事实、反思和概念四类节点的层次化图谱，并通过结合语义相似度与 PPR 的加性评分函数，实现了图遍历对语义检索的增强，而非替代。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为GAAMA的图增强联想记忆系统来解决多会话智能体长期记忆的结构化存储与检索问题。其核心方法分为知识图谱构建和混合检索两个阶段。

在知识图谱构建阶段，GAAMA采用三步流水线将原始对话转化为具有层次结构的知识图谱。第一步是**会话片段保留**，无需调用大语言模型，直接将每个对话轮次存储为“片段”节点，并通过NEXT边按时间顺序连接，保留了原始文本和时间信息以支持时序推理。第二步是**事实与概念提取**，调用大语言模型从片段序列中提取两种衍生节点：“事实”节点代表原子性事实断言，“概念”节点代表主题级标签（如“陶艺爱好”）。事实节点通过DERIVED_FROM边链接到源片段，而片段和事实则分别通过HAS_CONCEPT和ABOUT_CONCEPT边链接到相关概念节点。第三步是**反思合成**，再次调用大语言模型从多个事实中合成更高层次的“反思”节点，用于捕捉跨会话的通用模式或偏好，并通过DERIVED_FROM_FACT边链接到支持性事实。最终图谱包含片段、事实、反思、概念四种节点和五种结构边类型。

在检索阶段，GAAMA设计了一种结合语义相似性和图遍历的混合检索机制。首先，基于查询的嵌入向量，通过余弦相似性检索一个广泛的候选节点池（K近邻搜索）。然后，选取其中相似度最高的节点作为种子，在图结构上进行深度为2的局部子图扩展，以发现与种子结构相连但语义相似度可能不高的节点。接着，系统运行**边类型感知的个性化PageRank算法**来计算每个节点基于图结构的相关性得分。该算法为不同类型的边分配了不同的基础权重（例如，NEXT边权重为0.8，DERIVED_FROM_FACT边权重为0.5），并对高度数节点（连接数超过50）应用了枢纽抑制策略，以防止PageRank质量过度分散。最后，通过一个**加性评分函数**将归一化的PPR得分和语义相似度得分结合起来（默认权重分别为0.1和1.0），形成最终的相关性排序。检索结果还会按节点类型进行配额限制（如最多60个事实、20个反思、80个片段），并受总字数预算约束，以确保传递给答案生成大语言模型的上下文是平衡且信息丰富的。

该方法的创新点主要体现在：1）引入**概念节点**替代传统的实体节点作为关联索引，有效避免了实体中心化设计导致的“枢纽主导”问题，使图结构更稀疏且关联路径更有效；2）设计了**三步分层构建流水线**，将低成本的结构化操作与有针对性的LLM调用分离，实现了从原始对话到高层次洞察的渐进式抽象；3）提出了**语义相似性检索与图遍历检索的协同增强机制**，通过加性评分使两者优势互补，在基准测试中显著超越了纯语义检索或纯图检索的方法。

### Q4: 论文做了哪些实验？

论文在LoCoMo-10基准上进行了实验，该基准包含10段多轮对话，共计1540个问题，涵盖多跳推理、时序、开放域和单跳四类问题。实验设置采用“生成-评判”三步流程：首先，系统通过混合检索管道（结合余弦相似度k近邻搜索和基于边类型的个性化PageRank）从知识图谱中检索相关记忆，形成最多1000词的上下文；其次，使用GPT-4o-mini（temperature=0）基于检索内容生成答案；最后，由同一LLM作为评判员，根据生成答案覆盖参考关键事实的比例给出0-1的奖励分数。对比方法包括A-Mem、Nemori、HippoRAG以及一个经过调优的RAG基线（使用相同嵌入模型和上下文预算）。主要结果显示，GAAMA在整体平均奖励上达到78.9%，优于RAG基线（75.0%）、HippoRAG（69.9%）、A-Mem（47.2%）和Nemori（52.1%）。关键数据指标：在多跳问题上GAAMA得分为72.2%（对比RAG的67.5%），时序问题上为71.9%（对比RAG的59.0%），开放域问题上为49.3%（对比RAG的44.6%），单跳问题上为87.2%（与RAG的87.1%相当）。消融分析表明，在图节点上结合个性化PageRank的图遍历排序相较于纯语义搜索能带来整体1.0个百分点的提升（从78.0%到78.9%），其中单跳问题受益最大（提升1.6个百分点）。实验还分析了不同对话和问题类别下的性能变化，并指出图谱结构质量（如概念节点的泛化程度）是当前的主要瓶颈。

### Q5: 有什么可以进一步探索的点？

论文的局限性与未来研究方向可从其结论部分和系统设计本身进行延伸。首先，GAAMA依赖LLM进行知识提取和图构建，这可能导致错误累积和计算开销大。未来可探索更轻量级或增量式的构建方法，减少对重型LLM的依赖。其次，其个性化PageRank（PPR）的边权重是手动设定的，未来可通过端到端学习动态优化权重，甚至引入基于查询的适应性图遍历门控机制，以提升开放域问题的检索鲁棒性。

此外，概念节点的规范化（canonicalization）不足可能造成图碎片化，未来需研究自动合并语义相似概念的算法。从更宏观视角看，当前工作主要评估于静态基准（LoCoMo-10），未来需在动态、长期交互环境中测试其记忆的演化和遗忘机制。最后，GAAMA目前是独立记忆模块，如何与其他Agent组件（如规划、工具使用）更深度集成，实现闭环学习和记忆更新，也是一个值得探索的方向。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为GAAMA的图增强联想记忆系统，旨在解决AI智能体在多轮会话中需要持久长期记忆以保持连贯个性化行为的挑战。现有方法如扁平化检索增强生成（RAG）会丢失记忆间的结构关系，而基于向量检索的压缩方法难以捕捉多会话对话的联想结构。GAAMA通过三步流程构建概念中介的层次化知识图谱：首先保留原始对话的逐字片段，接着利用大语言模型提取原子事实和主题级概念节点，最后合成高阶反思。图谱包含四种节点类型（片段、事实、反思、概念）和五种结构边类型，其中概念节点提供了跨越性遍历路径以补充语义相似性。检索方法结合了基于余弦相似性的k近邻搜索和边类型感知的个性化PageRank，通过加性评分函数整合两者。在LoCoMo-10基准测试中，GAAMA以78.9%的平均奖励显著优于RAG基线及其他方法，消融实验表明基于图谱遍历的排序与语义搜索结合能持续提升纯语义搜索性能。该工作的核心贡献在于通过结构化图谱记忆系统有效捕捉对话的联想与层次关系，为智能体的长期记忆管理提供了新思路。
