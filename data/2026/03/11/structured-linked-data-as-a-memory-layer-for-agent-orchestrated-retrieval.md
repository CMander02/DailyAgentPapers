---
title: "Structured Linked Data as a Memory Layer for Agent-Orchestrated Retrieval"
authors:
  - "Andrea Volpini"
  - "Elie Raad"
  - "Beatrice Gamba"
  - "David Riccitelli"
date: "2026-03-11"
arxiv_id: "2603.10700"
arxiv_url: "https://arxiv.org/abs/2603.10700"
pdf_url: "https://arxiv.org/pdf/2603.10700v1"
categories:
  - "cs.IR"
  - "cs.AI"
tags:
  - "Agentic RAG"
  - "Retrieval-Augmented Generation"
  - "Knowledge Graph"
  - "Linked Data"
  - "Tool Use"
  - "Multi-hop Reasoning"
  - "Evaluation Framework"
relevance_score: 7.5
---

# Structured Linked Data as a Memory Layer for Agent-Orchestrated Retrieval

## 原始摘要

Retrieval-Augmented Generation (RAG) systems typically treat documents as flat text, ignoring the structured metadata and linked relationships that knowledge graphs provide. In this paper, we investigate whether structured linked data, specifically Schema.org markup and dereferenceable entity pages served by a Linked Data Platform, can improve retrieval accuracy and answer quality in both standard and agentic RAG systems. We conduct a controlled experiment across four domains (editorial, legal, travel, e-commerce) using Vertex AI Vector Search 2.0 for retrieval and the Google Agent Development Kit (ADK) for agentic reasoning. Our experimental design tests seven conditions: three document representations (plain HTML, HTML with JSON-LD, and an enhanced agentic-optimized entity page) crossed with two retrieval modes (standard RAG and agentic RAG with multi-hop link traversal), plus an Enhanced+ condition that adds rich navigational affordances and entity interlinking. Our results reveal that while JSON-LD markup alone provides only modest improvements, our enhanced entity page format, incorporating llms.txt-style agent instructions, breadcrumbs, and neural search capabilities, achieves substantial gains: +29.6% accuracy improvement for standard RAG and +29.8% for the full agentic pipeline. The Enhanced+ variant, with richer navigational affordances, achieves the highest absolute scores (accuracy: 4.85/5, completeness: 4.55/5), though the incremental gain over the base enhanced format is not statistically significant. We release our dataset, evaluation framework, and enhanced entity page templates to support reproducibility.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决检索增强生成（RAG）系统中普遍存在的一个关键问题：现有方法通常将文档视为扁平的无结构文本，从而忽视了网页中已广泛存在的结构化元数据（如Schema.org标记）和知识图谱所提供的实体关联关系。这种处理方式限制了RAG系统检索的准确性和答案质量。

研究背景是生成式AI和AI驱动搜索（如谷歌的AI模式）的兴起，它们需要从多个来源检索、推理并合成信息。RAG已成为将大语言模型输出与事实性信息相结合的主流架构。然而，现有方法的不足在于，它们大多丢弃了网站本已通过结构化数据（如JSON-LD）和知识图谱实体页面提供的丰富语义与链接信息，未能充分利用这些“关联数据”来提升检索效果。

因此，本文要解决的核心问题是：**结构化关联数据能否提升RAG的性能，而智能体（Agent）驱动的多跳链接遍历能否进一步释放这种潜力？** 具体而言，论文通过设计对比实验，系统性地探究了不同文档表示形式（普通HTML、带JSON-LD的HTML、以及为智能体优化的增强型实体页面）与不同检索模式（标准RAG vs. 具备多跳链接遍历能力的智能体RAG）的组合效果，以验证结构化关联数据作为“记忆层”对于智能体协调检索的价值。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类。

在方法类研究中，检索增强生成（RAG）是核心基础。Lewis等人正式提出了RAG框架，将检索与生成模型结合。后续研究探索了检索目标的预训练和大规模检索语料库。Self-RAG引入了自适应检索的自反思机制。Trivedi等人的工作表明，将检索与思维链推理交织能显著提升多步问答性能。然而，这些系统主要处理非结构化文本。本文则通过利用Schema.org JSON-LD等结构化元数据来弥补这一差距，将其作为提升检索质量的补充信号。

在应用类研究中，结构化数据和知识图谱是关键。Berners-Lee等人阐述了机器可读网络的愿景，并通过关联数据原则实现。Schema.org作为主要搜索引擎的合作项目，为网络结构化数据提供了共享词汇表。早期将结构化数据引入内容管理系统的努力包括WordLift和MICO。近期研究探索了LLM与知识图谱的统一，以及Graph RAG等方法。特别是，LightRAG和HippoRAG等系统从文档构建图索引以改进RAG，证明了图结构对检索的价值。但本文方法与它们有根本区别：这些系统在索引时从非结构化文本构建专用图，而本文则直接利用已通过Schema.org和关联数据平台发布在网上的现有结构化数据，无需构建步骤。

在评测与优化类研究中，Aggarwal等人提出的生成引擎优化（GEO）表明，通过添加引用、统计数据和权威语言等内容优化策略，可显著提升在生成式搜索引擎中的可见性。本文将GEO的范畴从可见性优化扩展到检索准确性优化，并聚焦于以结构化数据作为优化杠杆。

此外，在智能体系统方面，Yao等人提出的ReAct框架将推理轨迹与行动步骤交织，Schick等人证明了LLM可以自主学习使用外部工具，谷歌智能体开发套件（ADK）则提供了构建多工具智能体的生产框架。本文的智能体RAG配置实现了跨实体边界的链接遍历，模拟了AI驱动搜索系统聚合信息的行为。模型上下文协议（MCP）为LLM与工具集成提供了标准化接口，也是相关背景。

### Q3: 论文如何解决这个问题？

论文通过一个精心设计的实验系统来解决传统RAG系统将文档视为扁平文本、忽略结构化元数据和关联关系的问题。其核心方法是构建一个三层架构，将结构化关联数据（Linked Data）作为智能体（Agent）的外部记忆层，并通过对比不同文档表示形式与检索模式的组合来验证其效果。

**整体框架与主要模块**：
系统架构模拟了AI搜索引擎（如Google AI Mode）的工作模式，包含三个核心组件：
1.  **检索层**：使用Vertex AI Vector Search 2.0作为检索主干。它是一个自调优、全托管、AI原生的搜索引擎，通过单一混合查询结合了密集语义搜索（基于text-embedding-005嵌入）和稀疏关键词匹配，自动优化检索参数。
2.  **智能体推理层**：由Google Agent Development Kit (ADK)驱动，提供具备工具使用能力的ReAct风格循环。智能体可以规划一系列动作（搜索、跟踪链接、搜索知识图谱），然后综合生成最终答案。
3.  **结构化数据层**：由独立的关联数据平台（WordLift知识图谱）提供，它提供具有可解引用URI的Schema.org类型化实体，支持内容协商。这层充当了智能体的外部记忆。

**核心方法与关键技术**：
研究的关键在于让智能体能够利用结构化关联数据作为记忆层。智能体不再仅仅依赖向量存储中的扁平文本块，而是可以通过跟踪类型化关系（如 `schema:about`, `schema:author`）来发现上下文相关信息，这些信息是仅基于嵌入的检索所无法“看见”的。

为此，论文设计了 **$3 \times 2$ 因子实验**，交叉测试三种文档表示形式和两种检索模式，共产生六个核心实验条件和一个增强变体（Enhanced+）：
*   **文档表示形式**：
    *   **纯HTML**：移除所有JSON-LD脚本块，作为基线。
    *   **HTML + JSON-LD**：包含嵌入式Schema.org JSON-LD的原始网页，提供类型化实体、属性和实体间链接。
    *   **增强型实体页面**：**论文的核心创新格式**，旨在最大化智能体的可发现性。它包含：从结构化数据生成的自然语言摘要、完整的嵌入式JSON-LD块、带有可解引用URI的可见实体导航链接、为LLM智能体提供明确指导的`llms.txt`风格指令、用于跨实体发现的神经搜索SKILL引用，以及用于层次化上下文的Schema.org类型面包屑导航。这种格式弥合了人类可读网页与机器可读结构化数据之间的差距。
*   **检索模式**：
    *   **标准RAG**：使用混合搜索检索前K个文档，并单次调用LLM生成答案。
    *   **智能体RAG**：基于ADK的智能体在ReAct循环中可以使用三个工具：`search_documents`（执行向量搜索）、`follow_entity_link`（通过HTTP内容协商解引用链接实体URI，实现知识图谱的多跳遍历）、`search_knowledge_graph`（通过特定API端点执行知识图谱的神经搜索）。智能体最多可进行2跳链接跟踪。

**创新点**：
1.  **增强型实体页面设计**：这是最关键的创新，它通过整合结构化数据、显式导航链接和针对智能体的操作指令，创造了一种同时面向人类和AI优化的内容格式。实验表明，该格式带来了显著的性能提升（标准RAG准确率提升29.6%，完整智能体流程提升29.8%）。
2.  **将关联数据平台作为智能体的外部记忆**：明确提出了利用可解引用的结构化关联数据来扩展智能体的检索和推理边界，使其能够进行多跳、关系型的知识发现。
3.  **系统化的实验验证**：通过跨四个领域（编辑、法律、旅游、电商）的大规模可控实验，严谨地评估了不同数据表示与智能体能力组合的效果，为“优化内容以利于AI驱动搜索”提供了直接相关的实践依据。

### Q4: 论文做了哪些实验？

论文实验设计严谨，旨在评估结构化关联数据（特别是Schema.org标记和增强型实体页面）对标准与智能体化RAG系统检索性能的影响。

**实验设置**：研究在四个垂直领域（电子商务、法律、旅游、编辑）进行，共使用349个查询。实验测试了七种条件，这些条件是三种文档表示形式（纯HTML、带JSON-LD的HTML、增强型智能体优化实体页面）与两种检索模式（标准RAG、具备多跳链接遍历能力的智能体化RAG）的交叉组合，外加一个在增强型基础上增加更丰富导航功能和实体互连的“Enhanced+”条件。检索使用Vertex AI Vector Search 2.0，智能体推理使用Google Agent Development Kit (ADK)。评估由LLM法官在1-5分制上对答案的准确性和完整性进行打分。

**对比方法与主要结果**：核心对比围绕不同文档格式和检索模式展开。
1.  **JSON-LD标记的影响**：在标准RAG下，相比纯HTML（C1，准确度3.62），添加JSON-LD（C2，准确度3.89）带来小幅但统计显著的提升（Δ=+0.17，p<0.05），但效应量小（d=0.18）。
2.  **增强型实体页面的关键作用**：增强型页面（C3）在标准RAG下相比纯HTML基线带来巨大提升：准确度从3.62升至4.69（Δ=+1.04，+29.6%），效应量中等（d=0.60）。在智能体化RAG下，增强型页面（C6，准确度4.70）也显著优于带JSON-LD的智能体化检索（C5，准确度4.40）。
3.  **智能体化检索的价值**：在相同文档（HTML+JSON-LD）上，智能体化RAG（C5，准确度4.40）显著优于标准RAG（C2，准确度3.89），提升13.1%（Δ=+0.50）。
4.  **最佳性能**：“Enhanced+”智能体化条件（C6+）取得了最高绝对分数：准确度4.85/5，完整性4.55/5。不过，其相对于基础增强型智能体化条件（C6）的增量增益在统计上不显著。
5.  **查询类型与领域差异**：事实性查询从增强型页面中获益最大（C3对比C1提升66.8%）。不同领域的提升幅度差异显著：在旅游（SalzburgerLand）和编辑（WordLift Blog）领域提升巨大（Δ>+2.47），而在基线已接近满分（4.92）的电子商务（BlackBriar）领域提升微乎其微（Δ=+0.07）。

### Q5: 有什么可以进一步探索的点？

本文探讨了结构化关联数据作为智能体检索记忆层的潜力，揭示了几个值得深入探索的方向。论文的局限性在于实验主要基于特定平台（Vertex AI, Google ADK）和有限领域，其结论在更广泛的RAG架构和复杂知识图谱中的普适性有待验证。未来研究可朝以下方向拓展：

首先，**优化结构化信息的动态整合与推理机制**。当前增强型实体页面虽提升了检索准确性，但其结构相对静态。未来可探索如何让智能体在推理过程中动态构建和利用知识图谱关系，例如开发能实时解析页面关联、进行多跳推理的适应性更强的智能体架构。

其次，**研究跨模态与多源数据的统一记忆层**。论文聚焦于文本和结构化标记。一个重要的延伸点是设计能同时处理文本、图像、表格及API数据流的结构化记忆层，并研究智能体如何在此混合记忆基础上进行规划和决策。

再者，**探索成本、效率与可扩展性的平衡**。增强页面虽提升效果，但可能增加存储与处理开销。未来需研究轻量化的结构化数据嵌入方法、高效的链接遍历算法，以及适用于大规模分布式环境的记忆层索引策略。

最后，**建立更全面的评估基准**。除了准确性和完整性，未来应评估智能体利用结构化数据完成复杂、多步骤任务的能力，并设计衡量其推理透明度、可解释性以及知识溯源能力的指标。这有助于推动AI可见性从“被引用”向“被深度理解与执行”的范式转变。

### Q6: 总结一下论文的主要内容

这篇论文探讨了在检索增强生成（RAG）系统中，利用结构化关联数据（如Schema.org标记和可解引用实体页面）作为智能体的记忆层，以提升检索准确性和答案质量。核心问题是传统RAG将文档视为扁平文本，忽略了知识图谱提供的结构化元数据和关联关系。

方法上，研究设计了对照实验，在四个领域测试了七种条件：结合三种文档表示形式（纯HTML、带JSON-LD的HTML、以及增强的、为智能体优化的实体页面）与两种检索模式（标准RAG和具备多跳链接遍历能力的智能体RAG），并增加了一个提供更丰富导航功能和实体互连的“增强+”变体。实验使用Vertex AI Vector Search进行检索，Google Agent Development Kit进行智能体推理。

主要结论是，仅使用JSON-LD标记带来的改进有限，但论文提出的增强型实体页面格式（整合了类似llms.txt的智能体指令、面包屑导航和神经搜索能力）能显著提升性能：标准RAG准确率提升29.6%，完整智能体流程提升29.8%。“增强+”变体获得了最高的绝对分数，但相比基础增强格式的增量增益在统计上不显著。论文释放了数据集和模板，其核心贡献在于实证证明了结构化关联数据作为智能体记忆层的有效性，为构建更高效、可解释的智能体检索系统提供了新方向。
