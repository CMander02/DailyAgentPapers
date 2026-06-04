---
title: "Temporal Order Matters for Agentic Memory: Segment Trees for Long-Horizon Agents"
authors:
  - "Yifan Simon Liu"
  - "Liam Gallagher"
  - "Faeze Moradi Kalarde"
  - "Jiazhou Liang"
  - "Armin Toroghi"
  - "Scott Sanner"
date: "2026-06-03"
arxiv_id: "2606.04555"
arxiv_url: "https://arxiv.org/abs/2606.04555"
pdf_url: "https://arxiv.org/pdf/2606.04555v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent记忆"
  - "长期对话"
  - "层次化记忆架构"
  - "时间顺序建模"
  - "Segment Tree"
relevance_score: 8.5
---

# Temporal Order Matters for Agentic Memory: Segment Trees for Long-Horizon Agents

## 原始摘要

Long-horizon conversational agents need to interact with users through evolving events, tasks, and goals. Such histories are naturally temporal, yet many existing memory systems organize information primarily by topical similarity and may ignore the order in which events occur. We introduce Segment Tree Memory, or SegTreeMem, a memory architecture that represents conversation history as a temporally ordered Segment Tree over utterances. SegTreeMem incrementally inserts new utterances through an online rightmost-frontier update rule, preserving chronological order while forming hierarchical memory segments. For retrieval, SegTreeMem propagates relevance scores through the tree to combine local semantic matching with hierarchical temporal context. Across three long-horizon memory benchmarks and two LLM backbones, SegTreeMem improves answer quality over flat retrieval, graph-structured memory, and tree-structured memory baselines. Additional temporal-order permutation analysis shows that the performance gain depends on preserving temporal order during memory construction, supporting the claim that temporal order is a key structure for agentic memory.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长时程对话代理在记忆系统设计中忽视时间顺序的问题。研究背景在于，用户与代理的交互本质上是随时间演进的，对话历史自然地按时间顺序组织成连贯的语义片段。然而，现有记忆系统（如基于语义相似度的扁平检索、图结构或树结构记忆）大多按主题相似性组织信息，忽略了事件的时间顺序。这导致两个关键不足：一是检索时可能返回语义相似但上下文错位的信息，因为同一片段内后续语句的含义依赖于前序语句；二是现有树结构虽能形成层级，但构建过程往往侧重主题聚类，而非保持连续时间跨度。本文核心要解决两个设计问题：第一，如何在线实时构建一个既能保持主题连贯性又能严格保留时间顺序的树结构索引；第二，如何设计检索机制，既能利用局部语义匹配，又能结合层级时间上下文，从而避免检索到上下文不匹配的信息。为此，论文提出了Segment Tree Memory（SegTreeMem），通过将对话历史表示为时间有序的线段树，并设计右边界在线更新规则和基于传播矩阵的结构感知检索，来系统性地提升长时程对话的答案质量。

### Q2: 有哪些相关研究？

在记忆构建方面，RAPTOR和LATTICE通过聚类构建语义抽象树，但不支持在线更新且不保留顺序；MemWalker通过固定大小分组保留文档顺序，但仅适用于静态场景；MemTree支持在线更新，但基于相似度插入优先考虑主题相关性而非时间顺序。本文提出的Segment Tree Memory（SegTreeMem）通过在线最右前沿更新规则增量插入新话语，同时保持时间顺序并形成层次化记忆段，兼顾了在线更新与顺序保留。

在记忆检索方面，RAPTOR和MemTree采用扁平化检索，将所有树节点作为独立候选，不利用结构或时序上下文；MemWalker和LATTICE使用LLM引导遍历，利用树层次结构但未利用其他树诱导关系或时间顺序。SegTreeMem通过相关性传播机制，结合局部语义匹配与层次化时间上下文，在检索时同时利用树结构和时间顺序筛选证据。实验表明其在三个长时记忆基准和两个大语言模型上均优于现有方法，并通过时间顺序置换分析证明了保留时间顺序是性能提升的关键。

### Q3: 论文如何解决这个问题？

论文提出了分段树记忆（SegTreeMem），一种面向长程对话的时序记忆架构。其核心是将对话历史表示为按时间顺序组织的话语分段树，并通过在线右前缘更新规则实现增量构建。

**整体框架**：SegTreeMem是一个带注释的分段树，根节点覆盖全部历史，内部节点对应连续时间区间，叶节点对应单条话语。每个节点携带LLM生成的该区间摘要作为注释。

**主要模块**：
1. **在线更新模块**：当新话语到达时，通过兼容性模型（余弦相似度、点式LLM或批量LLM）从右前缘（Frontier）中选择兼容的非叶节点作为附着点。若找到，则在新话语与所选节点间创建中间节点链并更新祖先节点；若无兼容节点，则创建新根，将原树和新话语作为子节点。该机制保证每次插入仅影响O(log|M_t|)个节点。
2. **检索模块**：采用矩阵化的多跳分数传播机制。首先计算每个节点与查询的局部相关分数并归一化。然后通过传播矩阵（自上而下或自下而上）进行多步迭代传播，使高相关节点向其结构邻域扩散。最后结合初始分数与各跳传播分数（带衰减因子α）得到结构感知的最终检索分数，选取top-K节点作为记忆单元。

**创新点**：1) 首次将分段树结构用于智能体记忆系统，严格保持时间顺序；2) 提出右前缘更新规则，实现高效的在线记忆构建；3) 设计基于矩阵传播的结构化检索，融合局部语义匹配与层级时序上下文；4) 通过时序置换分析证明时间顺序是带来性能提升的关键结构因素。

### Q4: 论文做了哪些实验？

论文围绕SegTreeMem进行了四组实验。实验设置上，使用gpt-5.4-mini和qwen-3.5-flash两个LLM骨干，采用LLM-judge准确率和token级F1作为指标，证据预算K=10。数据集包括LoCoMo（10个对话组，1986个查询）、LongMemEval-MAB（5个上下文组，300个查询）和RealMem（10个人物角色，1415个查询）。对比方法涵盖三类基线：扁平检索（BM25、Dense）、图结构记忆（A-MEM、Mem0、HippoRAG）和树结构记忆（RAPTOR、MemTree）。

主要结果：（1）时间顺序构建优于非时间相似性聚类树，在三数据集上准确率一致提升（如批LLM+无传播下SegTreeMem达0.639，比非时间树的0.603高）；（2）时间顺序置换实验显示，置换30%对话对后SegTreeMem准确率下降0.111-0.144，远大于非时间树的0.020-0.051，证明时间顺序是关键结构；（3）批LLM提供最佳构建质量，而余弦相似性在准确性与成本间取得更好权衡，速度约为批LLM的5倍；（4）注意力感知检索最优策略依赖数据集，自顶向下在LoCoMo和LongMemEval-MAB上效果最好，自底向上在RealMem上更优；完全SegTreeMem系统在所有数据集上优于或持平基线，例如在LoCoMo上LLM准确率0.639，优于HippoRAG的0.570和RAPTOR的0.588。

### Q5: 有什么可以进一步探索的点？

论文的局限性与未来探索方向主要集中在三个方面。首先，当前检索时使用的传播策略（如固定视窗）是静态的，未能根据查询需求动态调整粒度。未来可以引入查询感知的传播策略选择，例如根据问题复杂度自适应选择无传播、自上而下或自下而上的检索路径，从而在局部细节与全局上下文间取得平衡。其次，当前系统仅处理文本，而真实长期智能体需要融合多模态观察、工具调用和动作轨迹。将时间有序的分段树扩展为支持多模态嵌入（如视觉、音频与结构化动作序列）并设计跨模态的时间对齐是重要方向。最后，长期部署中记忆索引会持续增长，缺乏增量维护机制（如局部子树重建、周期性压缩或去重）可能导致效率下降。可探索基于访问频率或时间衰减的树节点剪枝策略，以及利用在线学习动态调整树结构，在保持时间序的同时控制索引体积。这些改进将使内存系统更鲁棒、灵活和高效。

### Q6: 总结一下论文的主要内容

这篇论文聚焦于长程对话代理的记忆问题，指出现有记忆系统多按主题相似性组织信息，忽略了事件发生的自然时序。为此，论文提出了一种名为Segment Tree Memory（SegTreeMem）的新型记忆架构。该方法将对话历史表示为一棵基于话语的时间有序线段树，通过在线最右前沿更新规则增量插入新话语，保留时间顺序的同时形成层级记忆片段。检索时，通过树传播相关性分数，将局部语义匹配与层级时间上下文相结合。在三个长程记忆基准和两个大语言模型主干上的实验表明，SegTreeMem在答案质量上优于扁平检索、图结构记忆和树结构记忆基线。时间顺序排列分析进一步证实，性能提升依赖于构建记忆时保留时间顺序，从而论证了时间顺序是代理记忆的关键结构。该工作的核心贡献在于将时间顺序和层级结构作为长程对话记忆的基础，为对话代理的长期交互提供了更有效的记忆组织范式。
