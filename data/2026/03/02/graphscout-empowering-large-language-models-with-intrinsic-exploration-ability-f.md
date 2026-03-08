---
title: "GraphScout: Empowering Large Language Models with Intrinsic Exploration Ability for Agentic Graph Reasoning"
authors:
  - "Yuchen Ying"
  - "Weiqi Jiang"
  - "Tongya Zheng"
  - "Yu Wang"
  - "Shunyu Liu"
date: "2026-03-02"
arxiv_id: "2603.01410"
arxiv_url: "https://arxiv.org/abs/2603.01410"
pdf_url: "https://arxiv.org/pdf/2603.01410v1"
github_url: "https://github.com/Ying-Yuchen/_GraphScout_"
categories:
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 9.0
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "Qwen3-4B, Qwen-Max"
  key_technique: "GraphScout (a training-centric agentic graph reasoning framework with flexible graph exploration tools)"
  primary_benchmark: "N/A"
---

# GraphScout: Empowering Large Language Models with Intrinsic Exploration Ability for Agentic Graph Reasoning

## 原始摘要

Knowledge graphs provide structured and reliable information for many real-world applications, motivating increasing interest in combining large language models (LLMs) with graph-based retrieval to improve factual grounding. Recent Graph-based Retrieval-Augmented Generation (GraphRAG) methods therefore introduce iterative interaction between LLMs and knowledge graphs to enhance reasoning capability. However, existing approaches typically depend on manually designed guidance and interact with knowledge graphs through a limited set of predefined tools, which substantially constrains graph exploration. To address these limitations, we propose GraphScout, a training-centric agentic graph reasoning framework equipped with more flexible graph exploration tools. GraphScout enables models to autonomously interact with knowledge graphs to synthesize structured training data which are then used to post-train LLMs, thereby internalizing agentic graph reasoning ability without laborious manual annotation or task curation. Extensive experiments across five knowledge-graph domains show that a small model (e.g., Qwen3-4B) augmented with GraphScout outperforms baseline methods built on leading LLMs (e.g., Qwen-Max) by an average of 16.7\% while requiring significantly fewer inference tokens. Moreover, GraphScout exhibits robust cross-domain transfer performance. Our code will be made publicly available~\footnote{https://github.com/Ying-Yuchen/_GraphScout_}.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在知识图谱上进行推理时存在的灵活性和探索能力不足的问题。研究背景是，尽管基于知识图谱的检索增强生成方法通过结合LLMs与图结构数据来提升事实基础和推理能力，但现有方法存在显著局限。现有方法主要分为两类：被动检索驱动方法依赖静态检索和固定规则扩展子图，灵活性差；主动遍历方法虽然允许动态交互，但通常依赖于人工设计、数量有限的图交互工具（如节点查询和关系扩展），并且需要复杂的外部提示工程或工作流控制机制来引导探索。这导致模型缺乏对图结构的内在理解和自主探索能力，使得推理过程效率低下，难以处理复杂的多跳查询，且泛化能力有限。

本文要解决的核心问题是：如何让LLMs具备内在的、自主的图谱探索和推理能力，从而摆脱对人工设计工具和外部控制机制的依赖。为此，论文提出了GraphScout框架，其核心思路是通过提供更灵活的程序化图探索工具（如代码解释器和节点检索器），并利用一个“高级侦察兵”LLM自动合成高质量的图推理训练数据，进而对“初级侦察兵”小模型进行针对性训练，从而将智能化的图探索能力内化到模型参数中。这避免了昂贵的人工数据标注，从根本上提升了模型在图环境中的自主推理和探索能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：方法类、应用类和评测类。

在方法类研究中，相关工作主要围绕LLMs在图任务中的应用范式展开。一类工作将LLMs视为特征提取器，通过LLM-GNN级联架构，利用LLM编码文本信息，再交由GNN处理图结构。另一类则将LLMs作为最终预测器，通过将图结构序列化或结合专门训练的GNN来提供结构监督，应用于节点分类、链接预测等任务。本文与这些工作的核心区别在于，它并非将图仅作为特征源或隐式结构线索，而是致力于让LLMs在知识图谱上进行显式推理。

在应用类研究中，针对LLMs存在幻觉和知识过时的问题，检索增强生成（RAG）被广泛应用。传统RAG难以处理关系型知识，因此催生了结合知识图谱的GraphRAG方法。这些方法又可细分为两类：一是被动检索驱动范式，检索相关节点或子图并将其线性化为文本供LLM使用；二是主动遍历范式，如GraphCoT、PolyG和GraphCounselor等方法，让LLM通过预定义操作与图谱进行迭代交互。本文与这些GraphRAG工作的关系在于同属主动交互范式，但关键区别在于：现有方法严重依赖人工设计的交互方案和外部控制机制（如预定义工具或查询语言），而本文提出的GraphScout框架旨在通过合成训练数据对LLM进行后训练，从而内化其自主的图谱探索与推理能力，减少了对人工干预的依赖。

### Q3: 论文如何解决这个问题？

论文通过提出GraphScout框架来解决现有基于图的检索增强生成方法中存在的工具预定义、探索受限以及依赖人工引导的问题。其核心方法是一个以训练为中心的智能体化图推理框架，旨在通过让模型自主与知识图谱交互来合成结构化训练数据，从而将图推理能力内化到语言模型中，无需繁重的人工标注。

整体框架包含两个主要模块：Graph Quizzer和Graph Solver。Graph Quizzer作为“高级侦察兵”，使用一个强大的大语言模型，结合灵活的图探索工具，主动在知识图谱中探索并生成多样化的图推理问题-答案对，用于后续训练。Graph Solzer则作为“初级侦察兵”，通过后训练一个小参数模型，学习一个多轮决策策略，使其能够自主使用工具解决图推理问题。

在架构设计上，GraphScout的关键创新在于其智能体图探索工具集。它摒弃了有限的预定义工具，集成了两个互补的核心组件：1) **代码解释器**：提供一个安全的Python执行环境，允许模型编写可执行的Cypher查询代码，实现对图谱的精确、组合式查询，灵活控制查询逻辑和探索策略。2) **节点检索器**：一个基于FAISS的向量搜索模块，支持模糊实体链接，将问题中的文本提及映射到图谱中的候选实体节点。这两个工具极大地扩展了模型的行动空间，使其能够进行高阶模式分析和全局图检索。

训练过程由答案奖励驱动，并辅以基于线索的辅助奖励，以在稀疏反馈下引导探索。Graph Quizzer根据抽象的任务目标（包括答案类型、查询模式和难度）生成多样化的训练数据，并记录中间节点线索。Graph Solver则在这些数据上进行训练，学习协调实体链接、图遍历和答案合成的策略。

该方法的创新点在于：通过可编程的探索工具实现了对图谱的灵活、深度探索；通过自动化合成训练数据，将图推理能力内化到小模型中，实现了优于大基座模型的性能；整个框架形成了从问题生成到策略学习的闭环，显著提升了模型在图推理任务上的内在探索能力和跨领域迁移性能。

### Q4: 论文做了哪些实验？

论文在GRBENCH数据集上进行了广泛的实验，该数据集包含来自五个领域（如医疗、文学等）的1,740个问题，并按难度分为简单、中等和困难三个级别。实验设置方面，作者使用Qwen3-4B-Instruct-2507和Qwen3-8B作为基础模型，并采用DeepSeek-Chat在知识图谱探索阶段合成训练数据。训练时使用了verl框架和Group Relative Policy Optimization (GRPO)进行强化学习，共进行400步优化。

对比方法包括BaseLLM、TextRAG、GraphRAG、Cypher、GraphCoT、PolyG和GraphCounselor，这些基线方法均使用GPT-4o、GLM-4.6、Qwen-Max和DeepSeek-Chat等先进大语言模型实例化。评估指标包括基于Qwen-Max评判的QwenScore（衡量答案正确性比例）和预测与真实答案之间词元重叠的F1分数。

主要结果显示，GraphScout在微调后取得了最强的整体性能。具体而言，基于Qwen3-4B的GraphScout在五个领域的平均表现上，超越了基于Qwen-Max等领先大语言模型的基线方法平均16.7%，同时在推理时所需的词元数量显著更少。关键数据指标上，在医疗领域（具有11种节点类型和24种边类型的复杂图谱），GraphScout的QwenScore达到0.819，F1达到0.855，显著优于基线。此外，跨领域泛化实验表明，GraphScout在单一领域训练后，在未见领域上仅出现轻微性能下降，展现了强大的迁移能力。消融研究证实，移除代码解释器工具会导致性能最严重下降（如医疗领域QwenScore从0.819降至0.107），凸显了工具介导的图谱交互的必要性。按难度分析显示，GraphScout在中等难度问题上优势最为明显，表明其内在探索能力在多跳推理中尤为有效。

### Q5: 有什么可以进一步探索的点？

该论文提出的GraphScout框架在提升LLMs的图探索能力方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其知识图谱交互工具虽比现有方法灵活，但本质上仍受限于预定义的操作集合，未来可研究如何让模型动态生成或适配新的图谱查询操作，实现更开放式的探索。其次，该方法依赖合成数据对模型进行后训练，合成数据的质量与多样性直接影响泛化能力，未来可探索引入人类反馈或对抗性生成来提升数据真实性。此外，框架目前主要针对静态知识图谱，现实场景中图谱常动态更新，如何让智能体持续学习并适应图谱演变是一个重要挑战。从更广视角看，可探索将GraphScout与多模态推理结合，使其能处理包含文本、图像等异构信息的图谱。最后，该方法的计算效率虽已提升，但训练阶段仍较复杂，未来可研究更轻量的适配机制，如参数高效微调，以降低部署成本。

### Q6: 总结一下论文的主要内容

该论文提出GraphScout框架，旨在解决现有图增强检索生成方法中图探索能力受限的问题。现有方法通常依赖人工设计的引导和有限的预定义工具，限制了大型语言模型与知识图谱的交互深度。GraphScout的核心贡献是设计了一个以训练为中心的智能体化图推理框架，通过提供更灵活的图探索工具，使模型能自主与知识图谱交互，并自动合成结构化训练数据。这些数据用于对LLMs进行后训练，从而将图推理能力内化，无需繁琐的人工标注或任务设计。实验表明，经GraphScout增强的小模型在多个知识图谱领域上平均性能超越基于领先大模型的基线方法16.7%，且推理所需token数显著减少，同时展现出强大的跨领域迁移能力。
