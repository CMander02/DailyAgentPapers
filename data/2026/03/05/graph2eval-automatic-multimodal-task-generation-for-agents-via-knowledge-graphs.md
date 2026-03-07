---
title: "Graph2Eval: Automatic Multimodal Task Generation for Agents via Knowledge Graphs"
authors:
  - "Yurun Chen"
  - "Xavier Hu"
  - "Yuhan Liu"
  - "Ziqi Wang"
  - "Zeyi Liao"
date: "2025-10-01"
arxiv_id: "2510.00507"
arxiv_url: "https://arxiv.org/abs/2510.00507"
pdf_url: "https://arxiv.org/pdf/2510.00507v3"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Benchmark/Evaluation"
  - "Architecture & Frameworks"
relevance_score: 8.5
taxonomy:
  capability:
    - "Benchmark/Evaluation"
    - "Architecture & Frameworks"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "Graph2Eval"
  primary_benchmark: "Graph2Eval-Bench"
---

# Graph2Eval: Automatic Multimodal Task Generation for Agents via Knowledge Graphs

## 原始摘要

As multimodal LLM-driven agents advance in autonomy and generalization, traditional static datasets face inherent scalability limitations and are insufficient for fully assessing their capabilities in increasingly complex and diverse tasks. Existing studies have attempted to generate agent tasks using LLMs, but due to the inherent hallucinations of LLMs and the lack of internal data relationship modeling, these tasks often exhibit semantic inconsistencies and solvability issues. To address these challenges, we introduce Graph2Eval, a knowledge-graph-driven framework for automated, scalable, and semantically grounded agent task generation. At its core, Graph2Eval leverages a knowledge graph built from heterogeneous external data sources as a structured task space, generating multimodal agent tasks through subgraph sampling and task construction guided by task templates and meta-path strategies. To further ensure task reliability, a multi-stage filtering pipeline based on node reachability analysis, LLM scoring, and similarity analysis ensures the diversity and solvability of the generated tasks. By unifying both RAG Agent and Web Agent scenarios, Graph2Eval enables efficient generation of multimodal document understanding tasks and multi-step web interaction tasks. We instantiate the framework with Graph2Eval-Bench, a curated dataset of 1,319 tasks spanning document understanding and web interaction scenarios. Extensive experiments show that, on average, Graph2Eval improves task semantic consistency by 20% and solvability by 17% over baselines, while Graph2Eval-Bench effectively distinguishes agent performance, offering a new perspective on agent evaluation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态大语言模型（LLM）驱动的智能体（Agent）在评估过程中面临的核心挑战：如何自动生成大规模、多样化且高质量的评估任务，以准确衡量智能体在复杂真实场景中的泛化能力和真实认知水平。

研究背景在于，随着智能体自主性和泛化能力的提升，传统的静态评估数据集存在固有的可扩展性限制。它们通常依赖人工标注或复用现有资源，构建成本高昂且更新缓慢，导致任务多样性不足，难以与动态环境对齐。更重要的是，静态数据集无法区分智能体的成功是源于真正的推理能力，还是对训练数据中记忆知识的简单检索，从而无法可靠评估其真实能力。

现有方法试图利用LLM自动生成任务以缓解人工瓶颈，但存在两大不足：1）缺乏明确的实体关系建模。现有方法通常直接让LLM分析预处理好的文本和图像数据来生成任务，没有显式地对数据内部的语义结构和实体间复杂依赖关系进行建模，导致生成的任务常出现语义不一致和可解性差的问题。2）对动态环境的适应能力有限。在生成网页交互任务时，现有方法要么依赖具有预定义页面关系的静态数据，要么让LLM分析简化的环境，无法有效建模真实网站中内容和页面间的动态关系，导致生成的任务难以迁移到真实的动态网络场景。

因此，本文要解决的核心问题是：如何构建一个自动化的、可扩展的、且语义基础扎实的任务生成框架，以克服现有方法在语义一致性和任务可解性上的缺陷，并能够统一支持文档理解和网页交互等多种模态的智能体评估任务。为此，论文提出了Graph2Eval框架，其核心创新在于利用从异构外部数据源构建的知识图谱作为结构化的任务空间，通过子图采样和任务模板引导来生成任务，从而确保生成任务具有可靠的语义基础和可解性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为**人工标注数据集**和**合成数据生成**两大类。

在**人工标注数据集**方面，现有基准如GAIA、MiniWob、Mind2Web等，以及结合真实环境的OS World、AndroidWorld等，其任务规范主要依赖人工定义，虽环境丰富但**可扩展性有限**，难以适应日益复杂多样的智能体任务评估需求。

在**合成数据生成**方面，现有研究利用大语言模型通过种子任务生成、问题重写、自迭代等方法合成数据，或从网络语料中提取问答对。然而，这些方法主要面向大语言模型的训练或评估，**并非针对智能体任务**。近期工作如TaskCraft尝试自动化构建工具使用智能体任务，通过LLM遍历文档生成原子任务并进行组合，但其**依赖LLM对任务间依赖关系的判断，缺乏对显式实体关系的有效建模**。类似地，也有方法从文档合成智能体-环境交互数据，但仅通过去重和LLM对齐来保证质量，且基于静态文档生成网络智能体任务，**无法理解真实动态场景中的任务，难以可靠评估任务可执行性**。

**本文与这些工作的关系和区别**在于：本文提出的Graph2Eval框架，通过构建知识图谱作为结构化任务空间，从根本上**解决了LLM因幻觉和缺乏内部数据关系建模导致的语义不一致和可解性问题**。与依赖人工定义或纯LLM合成的方法相比，Graph2Eval利用子图采样和元路径策略，结合多阶段过滤管道，确保了生成任务的多样性、语义一致性和可解性，并**统一了RAG智能体和网络智能体两种场景**，实现了自动、可扩展且语义可靠的多模态智能体任务生成。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Graph2Eval的知识图谱驱动框架来解决现有LLM生成智能体任务时存在的语义不一致和可解性问题。其核心方法是利用从异构外部数据源构建的结构化知识图谱作为任务空间，通过子图采样和任务模板引导来生成多模态任务，并采用多阶段过滤管道确保任务质量。

整体框架遵循一个五阶段的工作流：数据摄取 → 知识图谱构建 → 子图采样 → 任务生成 → 覆盖优化。主要模块包括：
1.  **知识图谱构建模块**：将文档和网页等非结构化/半结构化数据转化为可计算的知识图谱。节点提取涵盖段落、标题、超链接、表单、按钮等多种元素，并保留其结构路径。节点表示融合了文本内容和视觉内容（通过视觉描述函数转换），并编码为语义嵌入向量。边构建则捕获文本间的结构、语义、上下文关系以及网页特有的导航、交互关系。
2.  **场景化子图采样模块**：根据任务目标（文档理解或网页交互）采用不同的采样策略。对于文档理解，基于节点嵌入的语义相关性和结构匹配性进行采样。对于网页交互，采用种子驱动策略，首先识别任务相关的种子节点（如按钮、表单），然后收集其k跳邻居节点以捕获局部交互上下文。
3.  **任务生成模块**：基于采样的子图实例化具体任务。对于文档理解任务，结合预定义的任务模板库（涵盖问答、比较、分析等），从子图中提取变量，并利用LLM生成具体任务实例。对于网页交互任务，提出“种子识别 → 子图采样 → 元路径匹配 → 动态生成”的流程。元路径模式用于匹配和扩展子图，形成具体的任务链（如“搜索+筛选+详情”），再结合页面上下文信息由LLM生成任务。
4.  **多阶段优化管道**：为确保生成任务的可靠性、多样性和代表性，设计了一个过滤与优化流程。通过基于节点可达性分析、LLM评分和相似性分析的多阶段过滤，来保证任务的可解性和语义一致性。最后，使用基于最大边际相关性的策略，在多个维度（如节点类型、边类型、模式、难度、语义多样性等）上优化任务集的覆盖度和新颖性。

创新点主要体现在：1) **知识图谱驱动的结构化任务空间**：利用知识图谱建模数据内部关系，从根本上缓解了LLM的幻觉问题，为任务生成提供了语义基础。2) **统一框架支持双场景**：在同一框架下高效生成文档理解（RAG Agent）和多步网页交互（Web Agent）两类任务，扩展了评估范围。3) **种子驱动与元路径匹配的任务链生成**：针对网页交互的复杂性，通过种子节点锚定和元路径扩展，能灵活生成具有上下文相关性和多步分支的任务链。4) **覆盖与多样性导向的优化**：通过多维度的覆盖量化和基于MMR的迭代选择，系统化地提升了生成任务集的代表性和评估效力。

### Q4: 论文做了哪些实验？

论文的实验主要围绕Graph2Eval框架及其生成的基准数据集Graph2Eval-Bench进行评估，涵盖任务质量验证和智能体性能评测。

**实验设置与数据集**：实验基于Graph2Eval-Bench数据集，该数据集包含1,319个任务，分为文档理解（1,002个任务）和网页交互（317个任务）两大场景。文档任务源自信件，网页任务来自多个网站，包含截图和DOM结构。知识图谱的边精度达到88%，验证了其可靠性。实验评估了两种智能体：RAG智能体（包括单智能体和多智能体协作）用于文档理解，Web智能体（包括SoM Agent和Agent S 2.5）用于多步骤网页交互。

**对比方法与评估指标**：在任务生成质量上，Graph2Eval与无知识图谱的变体（KG-free variant）以及现有基准OSWorld、MMBench和TaskCraft进行了对比。评估指标包括任务语义一致性（Consistency）和可解性（Solvability），并通过人工标注和智能体评估进行验证。对于智能体性能，测试了多个模型系列，包括GPT系列、Deepseek系列、Qwen系列和Gemini系列，以及GUI理解模型UI-TARS-1.5-7B。文档任务使用F1、ROUGE-L和LLM-as-a-Judge评分，网页任务使用成功率（Success Rate, SR）。

**主要结果与关键数据**：
1.  **任务质量**：与无知识图谱的变体相比，Graph2Eval在人工评估中将任务一致性平均提升了20%（文档任务从0.74提升至0.95，网页任务从0.62提升至0.78），将可解性平均提升了17%（文档任务从0.73提升至0.93，网页任务从0.60提升至0.72）。这表明知识图谱能有效确保语义一致性和任务可解性。
2.  **智能体性能区分**：在文档理解任务中，GPT-4o在单智能体设置下取得最高F1（0.5766）和ROUGE-L（0.4874）分数；Deepseek-V3在LLM-as-a-Judge评分中表现最佳（0.8351）。在网页交互任务中，Agent S 2.5显著优于SoM Agent，例如在Gemini 2.5 Flash上，前者整体成功率达69.20%，后者仅为14.51%，凸显了任务对多步骤推理能力的考察。开源模型Qwen2.5-VL-72B也表现强劲，整体成功率排名第二。
3.  **方法对比**：与OSWorld和MMBench等人标注数据集相比，Graph2Eval实现了低成本自动化构建，同时保持了高一致性和可解性。与合成方法TaskCraft相比，Graph2Eval采用自上而下的知识图谱驱动方法，能利用数据内在关系生成更广泛的任务类型。

### Q5: 有什么可以进一步探索的点？

本文提出的Graph2Eval框架在利用知识图谱提升任务生成的语义一致性和可解性方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，框架目前主要依赖静态知识图谱，未来可探索动态图谱的引入，使任务能实时反映网络信息变化，增强评估的时效性。其次，任务生成虽通过多阶段过滤确保质量，但对复杂推理或多模态深度融合的任务生成能力仍有不足，可结合强化学习优化采样策略，生成更具挑战性的高阶任务。此外，论文提及的未来方向如安全策略集成和细粒度错误定位虽具价值，但如何量化安全边界、设计对抗性环境，以及将节点/边层错误关联到具体agent决策缺陷，仍需大量实验验证。最后，框架目前侧重于文档理解和网络交互，未来可扩展至更多场景如具身智能或跨平台协作任务，进一步检验agent的泛化能力。

### Q6: 总结一下论文的主要内容

本文提出Graph2Eval框架，旨在解决多模态大语言模型（LLM）驱动的智能体在评估时面临的挑战：传统静态数据集扩展性有限，而现有基于LLM的任务生成方法因幻觉和缺乏内部关系建模，常导致任务语义不一致和不可解。Graph2Eval的核心贡献是利用从异构外部数据源构建的知识图谱作为结构化任务空间，通过子图采样和基于任务模板与元路径策略的任务构建，自动生成多模态智能体任务。为确保任务质量，框架采用基于节点可达性分析、LLM评分和相似性分析的多阶段过滤流程，以保障任务的多样性与可解性。该方法统一了检索增强生成（RAG）智能体和网页交互智能体两种场景，能高效生成文档理解任务和多步骤网页交互任务。作者据此构建了包含1,319个任务的基准数据集Graph2Eval-Bench。实验表明，Graph2Eval相比基线方法平均将任务语义一致性提升了20%，可解性提升了17%，且其基准能有效区分不同智能体的性能，为智能体评估提供了新的视角和工具。
