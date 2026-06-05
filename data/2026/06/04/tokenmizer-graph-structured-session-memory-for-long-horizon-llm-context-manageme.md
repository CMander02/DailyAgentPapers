---
title: "TokenMizer: Graph-Structured Session Memory for Long-Horizon LLM Context Management"
authors:
  - "Shweta Mishra"
date: "2026-06-04"
arxiv_id: "2606.06337"
arxiv_url: "https://arxiv.org/abs/2606.06337"
pdf_url: "https://arxiv.org/pdf/2606.06337v1"
github_url: "https://github.com/Shweta-Mishra-ai/tokenmizer"
categories:
  - "cs.AI"
tags:
  - "LLM Agent memory management"
  - "session history compression"
  - "knowledge graph"
  - "context window optimization"
  - "long-horizon tasks"
relevance_score: 7.5
---

# TokenMizer: Graph-Structured Session Memory for Long-Horizon LLM Context Management

## 原始摘要

Large language model (LLM) deployments for long-horizon tasks face a fundamental constraint: context windows are finite while productive work sessions are not. When history exceeds the Maximum Effective Context Window (MECW), critical structured information - architectural decisions, task transitions, file histories - is silently discarded. Existing mitigations treat history as flat text, destroying the relational structure that makes sessions resumable. We present TokenMizer, an open-source proxy system that models LLM session history as a typed knowledge graph. The schema defines 14 node types and 7 edge types. A hybrid extraction pipeline populates the graph incrementally, while a three-tier checkpoint system serializes it into compact resume blocks. An 8-layer compression pipeline reduces context overhead, and a semantic cache reduces repeated-query latency. Evaluated on a controlled benchmark of 21 sessions spanning 5 domains, TokenMizer demonstrates significant token economy. It produces resume blocks averaging 78 tokens (range: 42-124) - 2x smaller than evaluated baselines (159-170 tokens) - while achieving higher decision recall (+9-17 percentage points). Crucially, baselines only preserve that a technology was mentioned; TokenMizer preserves the rationale. Across all sessions, TokenMizer achieves mean task recall 51.0%, decision recall 46.6%, and file recall 58.7%. Variance reflects domain heterogeneity: explicit imperative phrasing (software engineering) scores higher than implicit reasoning (research). Ablation studies show fuzzy label matching is the dominant improvement factor (+33 pp task recall). The heuristic compression achieves 47.3% token reduction with zero external dependencies. TokenMizer provides a queryable alternative to text-retention baselines at half the token cost.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

大型语言模型（LLM）在软件工程、数据科学等领域的长期会话（long-horizon sessions）中面临核心挑战：上下文窗口有限，而生产性会话却可能无限持续。当历史记录超过最大有效上下文窗口（MECW）时，关键的**结构化信息**——如架构决策、任务转换、文件历史——会被静默丢弃。现有缓解方法（如截断、摘要、检索增强）均将历史视为**扁平文本**，破坏了使会话可恢复的关系结构。例如，摘要无法区分“已完成任务”与“待处理任务”，也无法保留技术决策的完整理由；检索增强方法则可能因语义距离而遗漏早期关键信息。针对这一不足，本文提出**TokenMizer**，一个开源代理系统，旨在解决的核心问题是：**如何在有限的Token预算内，保留长期LLM会话中结构化的决策逻辑与状态转移信息，而非仅仅保留文本片段**。TokenMizer将会话历史建模为类型化知识图谱，通过14种节点类型和7种边类型保留任务、决策、文件间的因果与依赖关系，从而在更低Token成本（平均78 tokens）下实现更高的决策召回率（比基线高9-17个百分点），并能保存“为什么做这个决定”的理由，而非仅“提到了什么技术”。

### Q2: 有哪些相关研究？

本文与以下相关工作存在关联和区别：

**方法类：**
- **MemGPT** 提出OS启发的层次记忆模型，区分主上下文和外部存储，由LLM自主控制内存管理。TokenMizer 针对同一会话内的结构化连续性，且不增加推理成本。
- **LangChain ConversationKGMemory** 使用无类型、无模式的图。TokenMizer 提供包含14种节点类型和7种边类型的正式模式，并具有状态生命周期管理和验证层，且作为透明代理运行。
- **Active Context Compression (ACC)** 通过LLM调用压缩上下文（22.7%），TokenMizer 使用启发式方法（47.3%）零推理成本，但覆盖范围不如基于LLM的方法。
- **LLMLingua/LongLLMLingua** 使用小型代理LLM计算词重要性。TokenMizer 将其作为压缩流水线的一部分，在启发式预处理后应用。
- **RECOMP** 为检索增强生成进行选择性摘要。TokenMizer 进行结构化提取而非文本检索，支持类型化查询。
- **GraphRAG** 从文档语料库构建知识图谱，面向静态语料。TokenMizer 构建面向会话的图，包含任务生命周期节点（如TASK状态转换、ERROR/FIX对），属于会话管理领域。

**评测类：**
- Paulsen 提出的最大有效上下文窗口（MECW）概念及“lost in the middle”现象，直接激励了TokenMizer 的16k token MECW设定，强调结构保留的重要性。

与这些工作相比，TokenMizer 的核心贡献在于：通过类型化知识图谱保留会话的*关系结构*和*决策依据*，而非仅保留扁平文本或提及记录，且以更少的token（平均78 vs 159-170）实现更高的决策召回率。

### Q3: 论文如何解决这个问题？

TokenMizer的核心方法是将LLM会话历史建模为结构化的类型化知识图谱,而非传统扁平文本。其整体框架是一个透明的HTTP反向代理,无需修改应用代码即可接入。

架构上包含五个关键组件:1) **图内存模块**定义了14种节点类型(如TASK、DECISION、FILE)和7种边类型(如DEPENDS_ON、IMPLEMENTS),节点带有重要性评分、置信度评分和状态生命周期。2) **混合提取管线**采用正则表达式和可选的小模型(Claude Haiku/GPT-4o-mini)从用户消息中增量提取实体,通过模糊标签匹配(基于单词重叠率≥50%)解决正则遗漏问题,并通过GraphValidator计算置信度(κ≥0.5才插入)。3) **三级检查点系统**在token累积超MECW的85%时触发,按重要性排序序列化为三档(关键/标准/完整)紧凑恢复块,平均仅78 token,并通过图差分存储实现增量更新。4) **8层压缩管线**逐层去除填充语(31.2%缩减)、重复内容、正则化空白等,其中启发式压缩无需外部依赖即达47.3%缩减,可选LLMLingua-2额外压缩5.3%。5) **语义缓存**基于sentence-transformer嵌入的余弦相似度(阈值0.92)缓存重复查询结果,70%命中率。

**创新点**在于:①保留会话的结构化关系而非扁平文本,使恢复时不仅知道"提到过技术X",还能追溯"为何选择X"的决策依据;②混合提取兼顾规则速度与LLM语义理解;③分区重要性驱动的检查点机制在更小token开销下实现更高召回率(决策召回比基线高9-17个百分点)。

### Q4: 论文做了哪些实验？

论文在一个包含21个会话、横跨5个领域（软件工程、数据科学、DevOps、研究、调试）的合成基准测试上评估了TokenMizer。实验设置了三个文本基线方法：朴素截断（保留最后300词）、滑动窗口（保留最后10条消息）和朴素摘要（取前300词），均代表当前实践中管理LLM上下文的方法。主要结果通过精确度、决策召回率和文件召回率比较。TokenMizer V2在决策召回率上显著优于所有基线（+9到17个百分点），达到平均47%（基线为30%-38%）；任务召回率为51%（基线为42%-50%），文件召回率为59%（基线为48%-60%）。关键优势在于token经济性：TokenMizer生成的恢复块平均仅需78个token（42-124范围），而基线需要159-170个token，实现了2倍以上的缩减。消融实验表明，模糊标签匹配是最关键的改进因素，将任务召回率提升了33个百分点。此外，启发式压缩实现了47.3%的token减少且无外部依赖。

### Q5: 有什么可以进一步探索的点？

基于论文分析，TokenMizer 的局限性和未来探索点包括：首先，47%的决策召回率意味着超过一半的关键决策被遗漏，尤其是在探索性讨论、学术写作或高层规划等隐性推理的会话中效果较差。未来可引入更细粒度的实体关系推理或基于LLM的补全机制，提升对非显式决策的捕获能力。其次，当前图结构依赖手工定义的14种节点和7种边类型，领域扩展性受限，可探索自动本体适配或动态类型学习。再者，压缩流水线虽减少了47.3%的token，但仍可能丢失微妙的上下文关联，可结合分层语义缓存与自适应压缩策略。此外，论文未评估图查询延迟与长期会话的扩展性，建议设计增量图重构和稀疏化注意力机制。最后，可尝试将图结构作为检索增强生成（RAG）的记忆模块，实现跨会话的决策迁移与因果推理。

### Q6: 总结一下论文的主要内容

大型语言模型在长时交互会话中面临上下文窗口有限的问题，当历史超过最大有效上下文窗口（MECW）时，关键的结构化信息（如架构决策、任务转换、文件历史）会被丢弃。现有方法将历史视为扁平文本，破坏了会话的可恢复结构。TokenMizer提出将会话历史建模为类型化知识图谱，定义了14种节点类型和7种边类型。它采用混合抽取流水线增量构建图谱，通过三级检查点系统序列化至紧凑的恢复块，其8层压缩流水线减少开销，语义缓存降低重复查询延迟。在跨5个领域的21个会话基准上，TokenMizer产生的恢复块平均仅78个token，比基线小2倍，同时决策召回率高出9-17个百分点。基线仅保留“提到某技术”，而TokenMizer保留了“为何选择”。该方法平均任务召回率51.0%，决策召回率46.6%，文件召回率58.7%，其中模糊标签匹配是主要改进因素（+33个百分点任务召回率），启发式压缩实现47.3%的token缩减且无外部依赖。TokenMizer证明，结构化知识图谱能以一半的token成本提供可查询的替代方案，革命性地解决了长会话中上下文丢失问题。
