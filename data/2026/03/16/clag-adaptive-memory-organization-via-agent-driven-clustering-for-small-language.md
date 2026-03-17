---
title: "CLAG: Adaptive Memory Organization via Agent-Driven Clustering for Small Language Model Agents"
authors:
  - "Taeyun Roh"
  - "Wonjune Jang"
  - "Junha Jung"
  - "Jaewoo Kang"
date: "2026-03-16"
arxiv_id: "2603.15421"
arxiv_url: "https://arxiv.org/abs/2603.15421"
pdf_url: "https://arxiv.org/pdf/2603.15421v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent_Memory"
  - "Small_Language_Models"
  - "Memory_Organization"
  - "Clustering"
  - "Retrieval-Augmented_Generation"
  - "Knowledge_Management"
  - "Reasoning"
relevance_score: 8.0
---

# CLAG: Adaptive Memory Organization via Agent-Driven Clustering for Small Language Model Agents

## 原始摘要

Large language model agents heavily rely on external memory to support knowledge reuse and complex reasoning tasks. Yet most memory systems store experiences in a single global retrieval pool which can gradually dilute or corrupt stored knowledge. This problem is especially pronounced for small language models (SLMs), which are highly vulnerable to irrelevant context. We introduce CLAG, a CLustering-based AGentic memory framework where an SLM agent actively organizes memory by clustering. CLAG employs an SLM-driven router to assign incoming memories to semantically coherent clusters and autonomously generates cluster-specific profiles, including topic summaries and descriptive tags, to establish each cluster as a self-contained functional unit. By performing localized evolution within these structured neighborhoods, CLAG effectively reduces cross-topic interference and enhances internal memory density. During retrieval, the framework utilizes a two-stage process that first filters relevant clusters via their profiles, thereby excluding distractors and reducing the search space. Experiments on multiple QA datasets with three SLM backbones show that CLAG consistently improves answer quality and robustness over prior memory systems for agents, remaining lightweight and efficient.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大型语言模型（LLM）的智能体（AI Agents）在长期任务中，其外部记忆系统因采用单一的全局检索池而导致的记忆稀释、知识污染及检索效率低下问题，尤其关注该问题对上下文干扰更为敏感的小型语言模型（SLM）智能体的严重影响。

研究背景是，AI智能体日益成为LLM在现实世界中长期任务中的主要范式，其依赖记忆机制来支持知识重用和复杂推理。现有方法主要遵循检索增强生成（RAG）范式，将记忆作为静态存储库，或虽引入主动管理（agentic memory）但仍普遍采用单一、非结构化的全局记忆池。现有方法的不足在于：随着记忆库增长，全局检索面临搜索空间膨胀，容易检索到语义相关但任务无关的“干扰项”；同时，记忆的更新演化过程暴露在主题混杂的全局环境中，容易受到误导，导致存储的知识逐渐退化或损坏。这对于能力有限、极易受无关上下文干扰的SLM智能体而言，问题尤为突出。

因此，本文要解决的核心问题是：如何为SLM智能体设计一个高效、鲁棒的记忆框架，使其能够主动、持续地组织记忆，避免全局存储带来的干扰和知识退化，从而提升智能体在长期任务中的答案质量和鲁棒性。论文提出的CLAG框架通过智能体驱动的聚类，将记忆组织到语义连贯的簇中，并在这些局部邻域内进行记忆演化与检索，以此实现结构化、自组织的记忆管理。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕检索增强生成（RAG）与智能体记忆系统展开，可分为方法类与应用类。

在方法类中，**检索增强生成（RAG）** 是基础，它将参数化模型与非参数化外部知识库结合以扩展上下文。然而，标准RAG系统通常是静态、只读的，缺乏基于持续经验动态整合记忆的能力。在应用类中，研究转向 **LLM智能体记忆**，早期工作（如静态RAG式设计）将记忆视为仅追加的全局检索池，通过相似性搜索查询，但难以从反馈中学习并进行巩固。近期**演化记忆系统**（如A-mem、MemoryOS、GAM）引入了反思、压缩和重写等维护操作，但大多仍依赖单一的全局记忆池，可能导致知识稀释或干扰。

本文提出的CLAG框架与这些工作的核心区别在于其**基于聚类的主动组织机制**。不同于全局池检索，CLAG通过智能体驱动的路由将记忆在线聚类到语义连贯的簇中，并为每个簇生成概要标签，形成独立的功能单元。这实现了**局部化演化**，减少了跨主题干扰，并通过两阶段检索（先筛选簇，再细粒度检索）提升了检索效率。因此，CLAG在保持轻量高效的同时，针对小语言模型易受无关上下文影响的问题，提供了更鲁棒的记忆组织方案。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为CLAG的、基于聚类的智能体记忆框架来解决小语言模型（SLM）智能体在单一全局检索池中存储记忆时，因知识稀释或污染而导致性能下降的问题。其核心方法是让SLM智能体主动地对记忆进行聚类组织，从而构建语义连贯、内部密集的记忆单元，并通过两阶段检索来抑制噪声。

**整体框架与核心组件**：CLAG框架包含三个核心组件，均围绕同一骨干SLM通过角色化提示词驱动。
1.  **智能体路由**：负责将新记忆分配到语义连贯的簇中。该过程分为冷启动和常规路由两阶段。冷启动阶段先缓冲一定数量的记忆，然后通过初始化算法建立初始簇结构。常规路由阶段，首先基于向量距离筛选出top-k个候选簇，然后由SLM智能体（扮演“路由器”角色）根据这些候选簇的语义档案（如主题摘要、描述性标签）做出最终路由决策。如果新记忆与选定簇的相似度低于阈值，则创建新簇。此外，框架采用自适应聚类机制，当簇大小超过阈值时，通过K-Means动态分裂，防止语义漂移和过度饱和。
2.  **局部化演进**：所有记忆的链接生成和知识演进都严格在其被路由到的簇内进行。对于新加入的记忆，CLAG首先在簇内基于余弦相似度找出其最相关的k个邻居记忆。然后，SLM智能体（扮演“演进器”角色）分析新记忆与这些邻居之间的细粒度关系（如因果、时序），生成显式的链接。接着，系统进入一个反馈循环：对于每个邻居记忆，SLM会判断其属性（如关键词、描述）是否需要根据新信息进行更新，从而实现知识的局部精炼。这种设计模仿了人类的认知过程，新经验主要重塑相关概念的理解，而不干扰无关知识域，从而增强了每个簇内部的语义密度和一致性。
3.  **簇感知的两阶段检索**：在推理时，用分层的检索流程替代扁平的全局检索。第一阶段是**智能体簇选择**：给定查询，先基于向量距离找到K个最接近的候选簇，然后由SLM智能体（扮演“选择器”角色）评估查询与这些簇的档案，返回一个可变大小的相关簇子集，这起到了高层语义过滤的作用，有效约束了搜索空间并抑制了无关噪声。第二阶段是**簇内检索**：仅在上一阶段选定的相关簇的并集内进行记忆检索。这种设计显著减少了有效搜索空间，并避免了全局相似性搜索中常见的语义相关但任务无关的记忆干扰。

**创新点**：
1.  **智能体驱动的主动聚类组织**：不同于静态或学习式的记忆组织，CLAG利用SLM智能体本身的理解能力，主动进行路由、簇档案生成和簇选择，使记忆结构具有语义感知和自适应性。
2.  **严格的局部化操作**：将链接和演进限制在簇内，避免了全局计算的昂贵开销，同时最大程度地减少了跨主题干扰，保持了知识的纯净性和内聚性。
3.  **层次化、语义过滤的检索机制**：两阶段检索，特别是由智能体驱动的簇选择步骤，为SLM提供了一个强大的噪声抑制层，使其对检索噪声的脆弱性大大降低，从而提升了答案质量和鲁棒性。整个框架保持了轻量高效，仅依赖单一骨干SLM和角色提示，无需额外的训练模型。

### Q4: 论文做了哪些实验？

论文在三个基准数据集上进行了实验评估：LoCoMo、HotpotQA和BioASQ。实验设置方面，采用了三个小型语言模型作为骨干网络：Llama-3.2-1B-Instruct、Qwen3-0.6B和DeepSeek-R1-Distill-Qwen-1.5B，并使用MiniLM-L6-v2模型进行语义嵌入和检索。对比方法包括标准的RAG基线以及代表性的智能体记忆架构A-mem、MemoryOS和GAM。

主要结果如下：在检索性能上，CLAG在多个指标上显著优于基线。例如，在LoCoMo数据集上，使用Qwen3-0.6B骨干时，CLAG的证据F1值达到2.07，远高于A-mem的1.17和RAG的1.12。在生物医学领域数据集BioASQ上，CLAG的优势更为明显，证据F1达到25.11，而RAG和A-mem分别仅为2.29和2.20。在HotpotQA上，CLAG的检索指标与RAG基线相近，但最终答案质量更高，这归功于其局部演化机制提升了信息密度。此外，消融实验表明，CLAG的智能体驱动聚类策略（F1: 22.01）显著优于基于余弦相似度（F1: 14.78）或K-Means（F1: 15.64）的非智能体聚类方法。在效率方面，CLAG在保持高精度的同时，端到端延迟比GAM等基线低数个数量级，实现了性能与计算成本的良好平衡。

### Q5: 有什么可以进一步探索的点？

CLAG的局限性主要在于其提示工程依赖性和对新领域/风格的泛化能力不足。未来研究可从以下方向深入：首先，可探索更鲁棒的聚类机制，例如引入轻量级适配器或元学习策略，使系统能动态适应分布变化和新主题，减少对固定提示模板的敏感度。其次，在隐私保护方面，可研究联邦学习或差分隐私技术，在本地化处理记忆的同时避免敏感数据泄露。此外，当前框架主要针对问答任务，未来可扩展至更复杂的多轮对话或长期规划场景，测试其在动态环境中的持续学习能力。最后，可结合神经符号方法，将聚类过程与逻辑规则相结合，提升记忆组织的可解释性和可控性。

### Q6: 总结一下论文的主要内容

本文提出CLAG框架，旨在解决小语言模型（SLM）智能体在外部记忆存储中面临的知识稀释和干扰问题。传统记忆系统通常将经验存储在单一的全局检索池中，容易导致知识污染，而SLM对无关上下文尤其敏感。CLAG的核心贡献是通过智能体驱动的聚类方法，动态组织记忆：它利用SLM驱动的路由器将新记忆分配到语义一致的聚类中，并自主生成包含主题摘要和描述性标签的聚类档案，使每个聚类成为独立的功能单元。通过在这些结构化邻域内进行局部演化，CLAG减少了跨主题干扰并提升了记忆密度。检索时采用两阶段过程，先通过聚类档案筛选相关聚类以排除干扰并缩小搜索空间。实验表明，CLAG在多个QA数据集和三种SLM骨干网络上均能提升答案质量和鲁棒性，同时保持轻量高效。该框架为有限能力智能体提供了一种实用的记忆层解决方案，显著增强了其可扩展性和抗干扰能力。
