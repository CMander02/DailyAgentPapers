---
title: "LegacyTranslate: LLM-based Multi-Agent Method for Legacy Code Translation"
authors:
  - "Zahra Moti"
  - "Heydar Soudani"
  - "Jonck van der Kogel"
date: "2026-03-14"
arxiv_id: "2603.14054"
arxiv_url: "https://arxiv.org/abs/2603.14054"
pdf_url: "https://arxiv.org/pdf/2603.14054v1"
categories:
  - "cs.SE"
tags:
  - "Multi-Agent"
  - "Code Agent"
  - "Tool Use"
  - "API Grounding"
  - "Iterative Refinement"
  - "Software Engineering"
relevance_score: 7.5
---

# LegacyTranslate: LLM-based Multi-Agent Method for Legacy Code Translation

## 原始摘要

Modernizing large legacy systems remains a major challenge in enterprise environments, particularly when migration must preserve domain-specific logic while conforming to internal architectural frameworks and shared APIs. Direct application of Large Language Models (LLMs) for code translation often produces syntactically valid outputs that fail to compile or integrate within existing production frameworks, limiting their practical adoption in real-world modernization efforts. In this paper, we propose LegacyTranslate, a multi-agent framework for API-aware code translation, developed and evaluated in the context of an ongoing modernization effort at a financial institution migrating approximately 2.5 million lines of PL/SQL to Java. The core idea is to use specialized LLM-based agents, each addressing a different aspect of the translation challenge. Specifically, LegacyTranslate consists of three agents: Initial Translation Agent produces an initial Java translation using retrieved in-context examples; API Grounding Agent aligns the code with existing APIs by retrieving relevant entries from an API knowledge base; and Refinement Agent iteratively refines the output using compiler feedback and API suggestions to improve correctness. Our experiments show that each agent contributes to better translation quality. The Initial Translation Agent alone achieves 45.6% compilable outputs and 30.9% test-pass rate. With API Grounding Agent and Refinement Agent, compilation improves by an additional 8% and test-pass accuracy increases by 3%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决企业环境中大规模遗留系统现代化迁移的实际难题，尤其是在迁移过程中如何确保生成的代码既能保留原有业务逻辑，又能符合企业内部特定的架构框架和共享API规范。研究背景是许多企业仍依赖数十年前用PL/SQL等语言编写的遗留系统，随着相关技术人才减少和架构需求演进，将这些系统迁移至Java等现代平台的需求日益迫切。论文以某欧洲金融机构正在进行的、涉及约250万行PL/SQL代码迁移至Java架构的项目为具体场景。

现有基于大语言模型（LLM）的代码翻译方法存在明显不足：它们通常在通用语言对（如Python与C++）的基准测试中表现良好，但在企业实际环境中，面对遗留语言、内部API和领域特定框架时，其生成的代码往往仅语法正确，却无法在目标生产框架中编译或集成。先前研究多局限于函数级别的翻译评估，且未充分考虑与内部库、共享API及架构约定的交互约束，导致其输出难以直接投入实际使用。

因此，本文要解决的核心问题是：如何设计一种能够系统性地处理企业级约束的代码翻译方法，以生成真正可编译、可通过测试且符合内部API规范的生产就绪代码。为此，论文提出了LegacyTranslate这一多智能体框架，通过分解翻译任务、引入API知识库和迭代反馈机制，来弥合语法正确性与生产可用性之间的鸿沟。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：代码翻译、遗留代码现代化改造以及多智能体协作。

在**代码翻译**领域，先前工作多集中于流行语言对（如Java、Python、C++）间小型自包含代码单元（如函数）的转换。例如，Zhu等人提出了多语言预训练方法；Roziere等人引入了无监督神经翻译方法；Szafraniec等人利用编译器中间表示来指导翻译；近期UniTrans通过生成目标端单元测试来引导和验证翻译。然而，这些方法主要适用于小规模代码片段，难以推广到企业现代化中面临的类级或框架级迁移。G-TransEval研究也证实了模型在处理复杂框架或算法级任务时存在困难。

在**遗留代码现代化改造**方面，工业界的研究关注在真实架构约束下迁移大规模用特定语言（如COBOL、PL/SQL）编写的代码库。例如，Hans等人和Solovyeva等人的工作分别专注于将COBOL和PL/SQL翻译为Java，这与本文的工业背景直接相关。

在**多智能体协作**领域，近期工作如TransAgent引入了代码生成器、语法检查器和语义分析器等多个智能体角色来迭代优化翻译代码。但其仍仅处理短代码片段，且未解决与内部API和共享库对齐等实际现代化任务的需求。

**本文与这些工作的关系和区别**在于：本文提出的LegacyTranslate框架，专门针对企业环境中大规模遗留系统（如PL/SQL到Java）的现代化挑战，其核心创新是构建了一个包含初始翻译、API对齐和迭代精炼三个专门智能体的多智能体系统。这区别于以往主要关注小规模、通用语言对的学术研究，也超越了现有多智能体方法（如TransAgent）未深入解决API集成和框架依赖的局限。特别是，本文的API Grounding Agent通过检索内部API知识库来确保代码与现有生产框架兼容，这借鉴了相关代码补全工作的思路，但将其创造性地应用于翻译任务，以解决实际集成编译的关键难题。

### Q3: 论文如何解决这个问题？

论文通过设计一个基于大语言模型的多智能体框架LegacyTranslate来解决遗留代码翻译问题。该框架的核心思想是使用三个专门化的智能体分工协作，逐步提升翻译代码的语法正确性、API合规性与功能正确性。

整体框架遵循流水线设计，依次执行初始翻译、API对齐和迭代优化三个阶段。主要模块包括：1）**初始翻译智能体**，它利用检索增强生成技术，从一个参考集中检索语义相似的PL/SQL到Java的翻译示例对，并将其作为少样本示例与任务定义、待翻译源代码一起构成提示词，驱动LLM生成初始Java代码草案。2）**API对齐智能体**，它负责将生成的代码与目标架构的现有API进行对接。该模块基于一个从项目Java库中通过静态分析构建的、包含API类、签名、实现和描述的精选知识库。当初始代码编译或测试失败时，该智能体分析错误信息与代码，并提示LLM从知识库中筛选出最可能用于修复错误的相关API列表。3）**迭代优化智能体**，它形成一个修正循环，利用前一步得到的相关API列表、具体的编译器错误信息以及单元测试反馈，反复提示LLM对代码进行修改和优化，直到代码成功编译、通过测试或达到预设的终止条件。

该方法的创新点在于其系统性的多智能体协同机制。首先，它通过**检索增强的初始翻译**，将领域特定的翻译模式作为上下文示例，显著提升了初始输出的结构有效性（从42.6%提升至98.5%）。其次，它创新性地引入了**API知识库与对齐机制**，使生成的代码能主动适配企业内部既定的架构和共享接口，解决了LLM直接翻译代码与生产框架脱节的核心痛点。最后，它设计了一个**基于编译器反馈与API建议的闭环迭代优化流程**，将编译错误和测试结果转化为优化信号，动态引导LLM进行针对性修正，从而将编译成功率从初始的45.6%进一步提升至52.9%，测试通过率从30.9%提升至33.8%。这种分阶段、反馈驱动的多智能体设计，有效结合了上下文学习、知识库检索和迭代修正，确保了翻译结果在语法、接口和功能上的综合质量。

### Q4: 论文做了哪些实验？

论文实验设置以Qwen2.5-Coder-14B作为核心LLM，SFR-Mistral作为检索器，并在单个NVIDIA A100 GPU上进行。评估指标包括结构有效性（SV）、编译率（CR）和测试通过率（TPR），以及检索质量的NDCG@3、MRR@3和Recall@3。对比方法包括：1）LLM-only基线（直接翻译，无示例或API信息）；2）LLM+Random Examples基线（添加随机选择的示例对）。实验数据集为内部整理的68个对齐的PL/SQL→Java代码对，代表遗留代码库中的模块类型，并包含工程师编写的单元测试。此外，还维护了用于检索的参考示例集和包含80个条目的API知识库。

主要结果显示，LLM-only基线的CR和TPR均为0%。LLM+Random Examples基线将SV提升至98.5%，但CR仅增至1.5%。而LegacyTranslate框架（包含初始翻译、API对齐和迭代优化三个智能体）实现了显著提升：SV达到100%，CR为52.9%，TPR为33.8%。仅使用初始翻译智能体时，CR和TPR分别为45.6%和30.9%，表明后续智能体带来了额外增益（编译率提升约8%，测试通过率提升约3%）。在模型选择实验中，Qwen2.5-14B表现最佳，而更小的模型（如Qwen2.5-7B）基本无法生成有效输出。检索器评估中，SFR-Mistral（嵌入维度4096）的检索性能最优。这些结果验证了多智能体方法在API感知的遗留代码翻译中的有效性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于依赖特定API知识库和缺乏公开数据集，这限制了方法的普适性。未来研究可探索以下方向：一是构建跨领域、多语言的公开基准数据集，以促进模型泛化能力；二是引入动态知识图谱来增强API理解的上下文感知，而不仅是静态检索；三是设计自适应代理协作机制，根据代码复杂度动态调整代理数量和职责，提升效率。此外，可结合符号推理或形式化验证来补全LLM的语义盲区，确保转换后代码的逻辑一致性。长远来看，将翻译过程与持续集成管道结合，实现实时反馈迭代，可能推动企业级应用的落地。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为LegacyTranslate的多智能体框架，用于解决企业环境中遗留代码（如PL/SQL）向现代语言（如Java）迁移的实际挑战。核心问题是直接使用大语言模型（LLM）进行代码翻译时，生成的代码虽然语法正确，但往往无法与目标架构的内部API和共享库兼容，导致编译失败或集成困难。

方法上，框架设计了三个专门的LLM智能体进行协作：初始翻译智能体利用检索的上下文示例生成初步Java代码；API对齐智能体从知识库中检索相关API，确保代码符合公司内部框架；精炼智能体则利用编译器和测试反馈，对代码进行迭代修正以提高正确性。

实验表明，该多智能体方法显著提升了翻译代码的可用性。仅使用初始翻译智能体时，编译通过率和测试通过率分别为45.6%和30.9%；加入后续两个智能体后，编译率进一步提升8%，测试通过率增加3%。论文的核心贡献在于证明了针对API对齐和迭代精炼设计的多智能体架构，能有效弥合LLM生成代码与生产就绪代码之间的差距，为大规模遗留系统现代化提供了可行方案。
