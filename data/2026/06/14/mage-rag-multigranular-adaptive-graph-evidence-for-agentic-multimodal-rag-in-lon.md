---
title: "MAGE-RAG: Multigranular Adaptive Graph Evidence for Agentic Multimodal RAG in Long-Document QA"
authors:
  - "Yilong Zuo"
  - "Xunkai Li"
  - "Jing Yuan"
  - "Qiangqiang Dai"
  - "Hongchao Qin"
  - "Ronghua Li"
date: "2026-06-14"
arxiv_id: "2606.15906"
arxiv_url: "https://arxiv.org/abs/2606.15906"
pdf_url: "https://arxiv.org/pdf/2606.15906v1"
github_url: "https://github.com/laonuo2004/MAGE-RAG"
categories:
  - "cs.IR"
  - "cs.AI"
  - "cs.CL"
  - "cs.DB"
  - "cs.MM"
tags:
  - "Agentic RAG"
  - "多模态RAG"
  - "长文档问答"
  - "图证据检索"
  - "自适应证据控制"
  - "多粒度检索"
relevance_score: 8.5
---

# MAGE-RAG: Multigranular Adaptive Graph Evidence for Agentic Multimodal RAG in Long-Document QA

## 原始摘要

Long-document multimodal question answering requires a system to locate sparse evidence in long PDFs and integrate clues from text, tables, images, charts, and complex layouts. Existing RAG methods mostly rely on fixed Top-k retrieval over text chunks or pages. Text retrieval can compress the context but often loses visual and layout information; page-level visual retrieval preserves the original page, yet it also sends large irrelevant regions to the reader, leading to a static trade-off among evidence coverage, noise, and inference cost. This paper proposes MAGE-RAG, a multigranular adaptive graph evidence framework for long-document multimodal QA. MAGE-RAG uses page retrieval as the entry point for query-time evidence construction. Offline, it builds an evidence graph with page nodes and element nodes, encoding containment, reading order, layout adjacency, section hierarchy, and semantic-neighbor relations. At query time, an online evidence controller iteratively activates, opens, searches, and prunes evidence under explicit budgets. The resulting evidence subgraph is then rendered into structured multimodal reader input, allowing the LVLM to consume compact and relevant evidence within a limited context. On LongDocURL and MMLongBench-Doc, we establish a unified comparison and analysis protocol covering Direct MLLM, Text RAG, Page-level Visual RAG, and Graph/Agentic RAG. Experiments show that MAGE-RAG achieves 52.75 overall accuracy on LongDocURL, and 53.26 accuracy with 51.19 F1 on MMLongBench-Doc. Fine-grained breakdowns, budget-performance curves, ablations, and trace-based analysis further show that query-time evidence subgraph construction can balance dispersed evidence coverage with context-noise control. Our code is available at https://github.com/laonuo2004/MAGE-RAG.git.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长文档多模态问答中证据组织与检索的固有问题。研究背景方面，尽管已有LayoutLM、Donut等文档模型及DocVQA等基准，但现实场景如LongDocURL和MMLongBench-Doc显示，长PDF（数十至数百页）的答案证据稀疏，可能分散在文本、表格、图表、布局等多模态元素中，且需要跨页推理。现有RAG方法主要有三点不足：1）固定Top-k检索与静态预算，难以兼顾单页、跨页及不可回答问题的差异，k值小会遗漏证据，k值大则引入噪声；2）单粒度证据，文本块检索丢失视觉与布局信息，页面级检索保留完整页面但带入大量无关区域；3）缺乏查询时的证据状态控制，检索后直接拼接给生成器，无法动态追踪已观察线索、待搜索缺口及冗余剪枝。因此，本文的核心问题是：系统如何针对当前问题，动态决定对长文档中的哪些证据进行扩展、保留或剪枝。为此，论文提出MAGE-RAG框架，将长文档多模态QA形式化为在预算约束下的查询时证据子图构建，通过多粒度自适应图结构实现证据的动态激活、展开、搜索与剪枝，以平衡证据覆盖度、噪声与推理成本。

### Q2: 有哪些相关研究？

以下是与本文相关的主要研究工作，按类别组织：

**方法类相关研究**：本文与GraphReader、G-Retriever、MLDocRAG、LAD-RAG和G²-Reader等结构感知方法相关。GraphReader将长文本组织成图并让agent逐步访问节点，G-Retriever将图检索形式化为子图选择。与这些方法不同的是，MAGE-RAG将图作为查询时处理空间，在预算约束下物化证据子图，而非自由形式的问答。同时，区别于LAD-RAG的布局感知符号图和G²-Reader的双图规划，MAGE-RAG采用多粒度自适应证据图，包含页面节点和元素节点，编码包含关系、阅读顺序、布局邻接和语义邻居关系。

**检索增强生成（RAG）类研究**：文本检索方面，BM25和ColBERTv2等传统方法虽能压缩上下文但丢失视觉信息；视觉检索方面，ColPali、VisRAG、M3DocRAG等方法保留页面原始信息但引入噪声。MAGE-RAG通过保持页面检索作为稳定入口，同时维护多粒度证据图，并利用查询时控制器决定打开、保留或修剪哪些局部证据，实现了兼顾覆盖率和噪声控制的平衡。

**评测类与基准**：MMLongBench-Doc和LongDocURL基准将评估从单页内容识别转向证据定位、跨页整合和多模态信息对齐，MAGE-RAG在这两个基准上建立了统一比较协议，涵盖Direct MLLM、Text RAG、Page-level Visual RAG和Graph/Agentic RAG等多种方法。

### Q3: 论文如何解决这个问题？

MAGE-RAG提出了一种多粒度自适应图证据框架，用于解决长文档多模态问答中证据稀疏、跨模态融合困难以及固定Top-k检索带来的噪声与覆盖度权衡问题。其核心方法包括四个组成部分：离线多粒度证据图构建、页面级初始定位、在线证据控制器和结构化多模态读者渲染。

首先，离线阶段将PDF文档解析为两种节点：页面节点和元素节点（如段落、表格、图表等），并构建五类关系边：包含关系（页面-元素）、阅读顺序、布局邻接（如左右对齐）、章节层次和语义邻居。这些关系边模拟了不同的阅读行为，为后续的图扩展提供了结构基础。

在线阶段以页面级视觉检索为入口，选择Top-k相关页面作为工作记忆的初始状态。随后，在线证据控制器迭代执行候选生成、边际效用评估和预算控制。候选生成器从当前激活页面或元素出发，沿关系边枚举候选节点。评估器基于问题、当前证据状态和历史轨迹，输出结构化决策（如激活、打开、搜索、剪枝）。预算控制包括每轮激活次数上限、总激活次数上限、最大迭代轮次和最终打开节点预算，防止证据状态无限增长。

最终，渲染器将非剪枝的页面和元素组织成XML结构，并配以页面截图和局部节点图像，生成紧凑且相关的输入供LVLM消费。该框架的创新点在于将证据覆盖与噪声控制之间的权衡转化为每个问题特有的证据状态更新过程，通过多粒度图结构和自适应控制器实现了灵活的证据扩展与精炼。

### Q4: 论文做了哪些实验？

论文在LongDocURL和MMLongBench-Doc两个长文档多模态QA基准上进行了实验。实验设置包括统一对比协议，涵盖四类基线方法：直接MLLM（直接输入完整文档）、Text RAG（文本块Top-k检索）、Page-level Visual RAG（页面级视觉检索）以及Graph/Agentic RAG（图或智能体驱动的RAG）。MAGE-RAG在LongDocURL上取得52.75%的整体准确率；在MMLongBench-Doc上获得53.26%的准确率和51.19的F1分数。实验还包括细粒度指标分解（按证据类型和问题维度）、预算-性能曲线分析（观察证据预算对性能的影响）、消融实验（验证自适应图构建、在线控制器等组件的贡献）以及基于追踪的分析（展示查询时证据子图构建如何平衡分散证据覆盖与上下文噪声控制）。主要结果表明，MAGE-RAG通过自适应多粒度证据图构造，在覆盖稀疏证据和减少无关噪声之间取得了更优的平衡，优于固定Top-k检索的静态折衷方案。

### Q5: 有什么可以进一步探索的点？

MAGE-RAG在证据图构建和查询时控制方面展现了优势，但仍存在若干可探索的方向。首先，当前证据控制器主要依赖启发式规则（如预算约束和迭代激活），未来可引入强化学习或基于在线反馈的元学习策略，使控制器根据查询难度和文档结构自适应调整搜索深度与剪枝阈值。其次，论文主要评估长文档QA场景，其图结构对多跳推理、跨模态冲突（如图表与文本不一致）等复杂查询的鲁棒性尚未充分验证，需引入对抗性查询测试。此外，节点间的语义邻居关系构建仅基于简单相似度，可探索利用多模态大模型（LVLM）的深层语义对齐或外部知识库增强图边权重。最后，当前对文本、表格、图表等不同模态的证据重要性权重是隐式的，未来可设计显式的跨模态注意力融合机制，或在图构建时加入模态类型作为元特征，提升子图对低频证据的敏感度。

### Q6: 总结一下论文的主要内容

长文档多模态问答需要系统从PDF中定位稀疏证据并整合文本、表格、图像、图表及复杂布局的线索。现有RAG方法依赖固定Top-k文本或页面检索，导致证据覆盖、噪声与推理成本间的静态权衡。本文提出MAGE-RAG，一种多粒度自适应图证据框架。离线阶段构建包含页面节点和元素节点的证据图，编码包含、阅读顺序、布局邻接、章节层级和语义邻居关系。在线查询时，证据控制器在显式预算下迭代激活、打开、搜索和剪枝证据，最终将证据子图渲染为结构化多模态输入，使LVLM在有限上下文中消费紧凑相关证据。在LongDocURL和MMLongBench-Doc上，MAGE-RAG分别达到52.75和53.26的准确率。实验表明，查询时证据子图构建能有效平衡分散证据覆盖与上下文噪声控制。核心贡献包括：诊断固定检索问题、提出状态化证据子图构建框架、建立统一实验协议并提供细粒度分析。
