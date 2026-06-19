---
title: "ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search in Open Literature Environments"
authors:
  - "Tingyue Pan"
  - "Mingyue Cheng"
  - "Daoyu Wang"
  - "Yitong Zhou"
  - "Jie Ouyang"
  - "Qi Liu"
  - "Enhong Chen"
date: "2026-06-18"
arxiv_id: "2606.20235"
arxiv_url: "https://arxiv.org/abs/2606.20235"
pdf_url: "https://arxiv.org/pdf/2606.20235v1"
categories:
  - "cs.IR"
  - "cs.AI"
tags:
  - "学术搜索Agent"
  - "Agent评测基准"
  - "信息检索Agent"
  - "LLM Agent"
  - "多意图查询"
  - "数字图书馆Agent"
  - "Taxonomy引导"
relevance_score: 9.5
---

# ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search in Open Literature Environments

## 原始摘要

Academic paper search is a core step in scientific research, and LLM-based search agents are emerging as a promising paradigm for iterative, intent-driven literature exploration. However, existing benchmarks are insufficient for systematically evaluating agentic academic search under realistic open literature environments. We propose ScholarQuest, a large-scale, taxonomy-guided benchmark for agentic academic paper search. ScholarQuest is constructed from over 1,000 computer science topics and four representative research intents, including method-oriented, setting-anchored, comparison-based, and scope-controlled queries. It further provides scalable answer construction and a shared retrieval backend ScholarBase for reproducible evaluation. Benchmarking results show that agentic methods outperform single-shot retrieval baselines, yet the best-performing agent only achieves 0.314 Recall@100 and 0.355 Recall@All, indicating substantial room for improvement. In addition, analyses of search efficiency, intent-level robustness, and failure cases further highlight the benchmark's ability to provide multi-dimensional evaluation signals for academic paper search agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

学术论文搜索是科学研究的核心环节，现有方法主要依赖基于词法或语义匹配的单次检索范式，无法有效处理细粒度、带条件的研究查询（如寻找使用特定方法的论文、比较不同技术主张的文献）。尽管基于大语言模型的智能体搜索代理能自主迭代、扩展和精炼候选论文，展现出前景，但现有基准测试存在三大不足：一是查询多依赖人工构造或从论文衍生，存在标注偏差且覆盖的研究意图有限；二是构建高质量答案集成本高昂、难以扩展；三是缺乏公开、标准化的可重复评估环境。本文提出 ScholarQuest，旨在系统性地解决现有基准在开放文献环境下评估智能体学术搜索的不足。该基准通过覆盖超过1000个计算机科学主题，并设计方法导向、场景锚定、比较型和范围控制四类研究意图，实现了可控的查询多样性与广泛的领域覆盖；同时，它提供了可扩展的答案构建流水线和一个百万级共享检索后端 ScholarBase，以支持大规模、可复现的评估，从而填补了当前缺乏全面、多维评估智能体论文搜索能力的空白。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为方法和评测两类。在评测类工作中，PaSa 提出了 AutoScholarQuery（基于顶级AI会议论文的大规模合成数据集）和 RealScholarQuery（小规模真实学术查询），但前者存在主题和引用偏差，后者规模有限难以覆盖细粒度主题和多样查询意图。SPARBench 通过专家筛选查询和多源相关性验证改进了标注质量，但规模较小且覆盖范围较广而非系统性的 CS 主题层次。本文的 ScholarQuest 则提供了基于分类法的主题覆盖、可控的查询分布和更广泛的金标准答案池。在方法类工作中，PaSa 将论文搜索建模为多步骤的智能体工作流，SPAR 集成了查询理解、多源检索、引文探索和重排序，PaperScout 进一步增强了工具使用自主性。这些方法展示了超越传统单次检索的智能体文献探索潜力，但现有工作缺乏系统性评测。ScholarQuest 通过提供涵盖检索质量、搜索效率、多轮决策能力和不同研究意图下鲁棒性的多维评测信号，与这些方法形成互补。

### Q3: 论文如何解决这个问题？

ScholarQuest通过构建一个大规模、分类学引导的基准来系统评估学术论文搜索智能体。其核心方法包括三个部分:首先,基于ACM CCS分类系统收集超过1000个计算机科学主题种子,利用Qwen3-Max将其映射到arXiv类别,随后根据四种研究意图(方法导向、设置锚定、范围控制和比较型)生成多样化查询,经过去重和质量控制后得到1111个高质量查询。其次,构建可复现的检索后端ScholarBase:通过多源候选检索,包括原始查询和LLM生成的多种改写(方法聚焦、任务聚焦、宽泛主题、窄化主题和术语变体),并调用Google Search API、arXiv API和Semantic Scholar API等多个互补来源;再通过引文图扩展从高置信度论文出发收集引用和被引论文,并进行二跳扩展。最后采用多阶段相关性判定:先基于检索分数、元数据和小型相关性模型进行召回导向的粗筛选,再由多个LLM裁判基于查询、标题和摘要对候选论文进行0-2分评分,聚合后选择阈值τ=2的论文作为答案集,并对边界和高分歧案例进行人工审核以确保质量。该基准的创新点在于:分类学引导的查询生成确保覆盖系统性检索需求而非单篇论文衍生的查询,多源多策略检索结合引文扩展弥补词汇匹配的不足,以及多阶段LLM裁判与人工鉴定的结合实现可扩展的答案构建。

### Q4: 论文做了哪些实验？

论文在ScholarQuest基准上进行了系统实验，该基准包含1111个高质量查询，覆盖cs.LG、cs.CV等主流计算机科学领域，查询分为方法导向（27.2%）、设置锚定（29.0%）、范围控制（28.5%）和比较型（15.3%）四类。实验环境为开源的ScholarBase平台，支持BM25稀疏检索、BGE-M3密集检索及RRF混合检索。对比方法包括三组：传统检索基线（密集检索、RRF混合检索）、商业学术搜索系统（Google Search、Google Scholar、Semantic Scholar API、DeepXiv）和开源智能体系统（PaSa、SPAR、PaperScout）。主要指标为Recall@25/100/All及搜索效率指标。结果显示智能体方法显著优于单次检索基线，但最佳智能体PaperScout仅达0.314 Recall@100和0.355 Recall@All。在性能差异上，PaperScout在方法导向查询上达0.408 R@100，优于PaSa（0.345）和SPAR（0.333）；但所有智能体在范围控制查询上表现最差，R@100仅为0.182-0.193。效率分析表明PaperScout使用更少工具调用（34.3次）和候选论文（408篇）实现最高召回效率（0.120/百篇）。此外，智能体在20个零召回案例中暴露了意图匹配失败的根本问题，如忽略范围控制中的负面约束。

### Q5: 有什么可以进一步探索的点？

该基准主要局限在计算机科学领域和arXiv文献环境，未来可扩展到多学科、多来源的学术数据库（如PubMed、IEEE），并引入不同出版格式和语言以提升泛化性。当前相关性判断仅依据标题、摘要和元数据，忽略了全文中的细粒度证据（如实验结果、方法论细节），未来应探索基于全文的语义匹配或段落级检索，以捕捉更深层的相关性。自动构建的答案集可能遗漏重要论文，可引入更强的人机协同验证机制（如多LLM一致性校验与专家抽查结合）。此外，当前查询意图固定为4类，可增加跨意图复合查询；搜索效率分析仅涉及基础指标，未来可建模动态检索策略（如自适应成本感知的预算分配）、引入多轮交互中的推理路径可解释性。最后，评估指标侧重召回率，可补充精度、排序质量及用户满意度等维度，以更全面反映实用效果。

### Q6: 总结一下论文的主要内容

学术论文搜索是科学研究的核心环节，基于大语言模型的搜索代理正成为迭代式意图驱动文献探索的新范式。现有基准测试无法在真实开放式文献环境下系统评估这种智能体搜索。为此，我们提出了ScholarQuest，一个大规模、分类法引导的基准测试，用于智能体学术论文搜索。该基准测试基于超过1000个计算机科学主题和四种代表性研究意图构建，包括方法导向、设定锚定、比较型和范围控制类查询。它还提供了可扩展的答案构建和共享检索后端ScholarBase，以确保可重复评估。实验结果表明，智能体方法优于单次检索基线，但表现最佳的智能体仅达到0.314的Recall@100和0.355的Recall@All，表明存在巨大改进空间。此外，对搜索效率、意图级鲁棒性和失败案例的分析进一步凸显了该基准测试为学术论文搜索智能体提供多维评估信号的能力。
