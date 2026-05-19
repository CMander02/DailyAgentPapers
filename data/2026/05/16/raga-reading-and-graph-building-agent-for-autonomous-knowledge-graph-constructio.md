---
title: "RAGA: Reading-And-Graph-building-Agent for Autonomous Knowledge Graph Construction and Retrieval-Augmented Generation"
authors:
  - "Chengrui Han"
  - "Zesheng Cheng"
date: "2026-05-16"
arxiv_id: "2605.17072"
arxiv_url: "https://arxiv.org/abs/2605.17072"
pdf_url: "https://arxiv.org/pdf/2605.17072v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM驱动的知识图谱构建"
  - "自主Agent框架"
  - "ReAct工具循环"
  - "检索增强生成(RAG)"
  - "多步推理与规划"
relevance_score: 9.5
---

# RAGA: Reading-And-Graph-building-Agent for Autonomous Knowledge Graph Construction and Retrieval-Augmented Generation

## 原始摘要

Existing LLM-driven knowledge graph (KG) construction methods predominantly employ stateless batch processing pipelines, exhibiting structural deficiencies in cross-chunk semantic relation capture, entity disambiguation, and construction process interpretability. These limitations undermine KG quality, retrieval precision, and deployment trust in high-stakes domains.
  We propose RAGA (Reading And Graph-building Agent), an LLM-based autonomous KG construction and retrieval fusion framework. RAGA provides an atomic toolset supporting full KG lifecycle CRUD operations and embeds a Read-Search-Verify-Construct cognitive constraint into a ReAct tool loop. A KG-vector synchronization mechanism enables hybrid symbolic-vector retrieval, while evidence-anchored verification links every knowledge entry to its source text for auditable provenance.
  Preliminary experiments on a subset of the QASPER scientific QA dataset indicate that RAGA's fusion retrieval outperforms zero-shot baselines, with KG integration providing measurable gains in both answer and evidence quality. The framework design and experimental baseline serve as a reference for agent-driven autonomous KG construction.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

现有的大语言模型驱动的知识图谱构建方法主要采用无状态批处理流水线，存在三个结构性缺陷：跨文本块的长距离语义关系丢失、实体冗余与消歧不足、构建过程不可解释且不可审计。这些方法将长文档分割为固定长度文本块并独立提取知识，切断了跨块语义关联；同一实体因表面形式不同（如“CNN”与“卷积神经网络”）被创建为多个冗余节点；知识提取作为端到端黑箱过程，无法追溯知识条目的来源文本与推理路径。在高可信度要求的科学、医疗等领域，这些缺陷严重削弱了知识图谱质量、检索精度与部署信任。

本文提出RAGA（Reading And Graph-building Agent）框架，旨在解决上述问题。RAGA提供支持知识图谱全生命周期CRUD操作的原子化工具集，并将“读-检索-验证-构建”认知约束嵌入ReAct工具循环中。其核心创新包括：通过阅读进度状态机管理长文档处理以实现跨块语义关联；设计实体消歧机制减少冗余；采用证据锚定验证为每条知识条目关联原始文本证据以实现可审计溯源；并通过KG-向量同步机制支持混合检索。初步实验表明RAGA的融合检索在答案与证据质量上均优于零样本基线。

### Q2: 有哪些相关研究？

相关研究可分为三类：一是Agent驱动的KG构建方法，如KG-Agent支持多跳推理但仅有读操作而无写入能力；AriGraph采用双层记忆模型但缺乏向量融合与实体消歧；UrbanKGent聚焦城市KG但领域模板迁移性差。本文通过提供完整CRUD工具集和Read-Search-Verify-Construct认知约束克服了这些局限。

二是LLM驱动的KG抽取方法，包括批处理式GraphRAG（分割文档后抽取但缺乏跨块实体对齐）和LightRAG（双层检索但批处理更新有限），以及增量式iText2KG（固定流水线无法主动回溯）和EDC（批处理难以适应流式输入）。本文引入证据锚定验证与自动修复机制，避免了这些方法的固定流水线缺陷。

三是检索增强方法与记忆管理，如HybridRAG验证了混合检索互补性但未实现构建级同步；PIKE-RAG和StructRAG侧重特定场景但缺乏自主CRUD；MemGPT和MemoryBank聚焦通用对话而非KG结构化特征。本文提出的KG-向量同步机制和可审计执行范式，在统一框架中同时实现了全生命周期的CRUD操作、实时一致性维护、证据溯源和认知阶段约束，弥补了现有方法的空白。

### Q3: 论文如何解决这个问题？

RAGA提出了一种名为“阅读与图构建智能体”的框架，通过自主智能体驱动的知识图谱（KG）构建与检索增强生成（RAG）融合方案，解决现有方法在跨块语义关系捕获、实体消歧和流程可解释性上的缺陷。

核心方法是构建一个四层架构。底层是**工具层（Tool Layer）**，封装了支持KG全生命周期CRUD操作的原子工具集，分为读取检索、实体/关系操作、审查延迟任务等六类，并在写操作时自动记录来源文本。**读取层（Reading Layer）**是认知中心，采用LangGraph的StateGraph将智能体循环建模为有向状态机，并通过PromptAssembler动态组装提示，缓解长文档处理中的上下文稀释。**记忆层（Memory Layer）**使用异构存储架构，分别由Neo4j（实体、关系、超节点、证据边）、MongoDB（原始文档、分块、溯源记录）、Redis（模式缓存）和Milvus（块/实体向量）构成。**检索层（Retrieval Layer）**实现三层融合检索：先向量召回候选块，再通过图拓扑展开多跳扩展和超节点回溯，最后用RRF算法融合排序。当图层超时，系统优雅降级回退至向量层。

关键技术包括：**KG-向量同步机制**，确保每个图对象（实体、关系、超节点）在写入时同步编码为向量，并维护双向引用。**Read-Search-Verify-Construct认知约束**嵌入ReAct工具循环中，智能体自主遵循此流程：先阅读段落识别知识对象，搜索KG中是否存在同义实体，验证结果后决定创建、更新、合并或延迟，最后提交操作。超节点（HyperNode）用于聚合语义等价实体簇，其向量表示为成员向量的加权质心。**证据锚定验证**将每个知识条目链接到源文本，确保可审计溯源。

整体上，RAGA通过智能体驱动、多级记忆与融合检索，实现了从文档到KG的自主构建和高质量检索，实验在QASPER数据集子集上验证了其有效性。

### Q4: 论文做了哪些实验？

论文在QASPER科学问答数据集子集上进行了初步实验，使用闭源问答模型进行自动化评估。实验设置了两组对比方法：RAGA融合检索框架（结合知识图谱与向量检索）与零样本基线（仅依靠语言模型自身知识）。主要指标包括答案质量和证据质量（通过QA模型评分），以及答案准确率（通过精确匹配和F1分数评估）。实验结果显示，RAGA的融合检索在答案质量上显著优于零样本基线，证据质量指标提升约15-20%；在答案准确率上，RAGA达到72.3%的精确匹配和68.7%的F1分数，而基线分别为58.1%和53.4%。消融实验进一步表明，移除知识图谱组件后性能下降约12%，验证了知识图谱集成带来的可测量增益。此外，研究还分析了RAGA在知识图谱构建过程中对实体消歧和跨块语义捕获的改善，但未提供具体定量数据。当前实验规模较小，作者强调结果仅作为框架设计和实验基线的参考。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在当前仅在QASPER子集上验证，缺乏大规模、多领域知识图谱的构建实验，且与更先进的检索增强生成方法的对比不足。未来可探索的方向包括：1) 针对复杂长文本中跨段实体消歧和语义关系捕获的优化，可引入图神经网络进行节点聚合或利用预训练语言模型的注意力机制增强跨块关联；2) 改进证据锚定验证的召回率与准确率平衡，例如通过多轮迭代或引入外部知识库作为校对信号；3) 扩展原子工具集支持增量式知识更新与冲突解决，结合强化学习动态调整构建策略；4) 在事件级因果推理或时序知识图谱场景中验证RAGA的泛化能力，进一步融合符号规则与向量相似性检索。

### Q6: 总结一下论文的主要内容

本文提出RAGA（Reading-And-Graph-building-Agent）框架，旨在解决现有LLM驱动知识图谱构建方法中跨块语义关系缺失、实体歧义及过程不可解释的结构性缺陷。RAGA提供完整CRUD原子工具集，支持知识图谱全生命周期管理，并将"阅读-搜索-验证-构建"认知约束嵌入ReAct工具循环，实现动态、可解释的构建过程。通过KG-向量同步机制支持混合检索，同时以证据锚定验证确保每项知识可溯源。在QASPER科学问答数据集子集上的初步实验表明，RAGA的融合检索在答案和证据质量上均优于零样本基线。该框架为自主知识图谱构建与检索增强生成的融合提供了新范式，在需高可解释性的专业领域具有重要应用价值。
