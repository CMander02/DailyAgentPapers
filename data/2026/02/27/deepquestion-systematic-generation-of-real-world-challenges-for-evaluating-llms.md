---
title: "DeepQuestion: Systematic Generation of Real-World Challenges for Evaluating LLMs Performance"
authors:
  - "Ali Khoramfar"
  - "Ali Ramezani"
  - "Mohammad Mahdi Mohajeri"
  - "Mohammad Javad Dousti"
  - "Majid Nili Ahmadabadi"
date: "2025-05-30"
arxiv_id: "2505.24532"
arxiv_url: "https://arxiv.org/abs/2505.24532"
pdf_url: "https://arxiv.org/pdf/2505.24532v2"
categories:
  - "cs.CL"
tags:
  - "Reasoning & Planning"
relevance_score: 5.0
taxonomy:
  capability:
    - "Reasoning & Planning"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "DeepQuestion framework"
  primary_benchmark: "DeepQuestion dataset"
---

# DeepQuestion: Systematic Generation of Real-World Challenges for Evaluating LLMs Performance

## 原始摘要

While Large Language Models (LLMs) achieve near-human performance on standard benchmarks, their capabilities often fail to generalize to complex, real-world problems. To bridge this gap, we introduce DeepQuestion, a scalable, automated framework that systematically elevates the cognitive complexity of existing datasets. Grounded in Bloom's taxonomy, DeepQuestion generates (1) scenario-based problems to test the application of knowledge in noisy, realistic contexts, and (2) instruction-based prompts that require models to create new questions from a given solution path, assessing synthesis and evaluation skills. Our extensive evaluation across ten leading open-source and proprietary models reveals a stark performance decline with accuracy dropping by up to 70% as tasks ascend the cognitive hierarchy. These findings underscore that current benchmarks overestimate true reasoning abilities and highlight the critical need for cognitively diverse evaluations to guide future LLM development.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）评估与现实世界需求脱节的核心问题。研究背景是，尽管LLMs在GSM8K、MMLU等标准基准测试上取得了接近人类甚至专家级的性能，但这些成绩往往无法泛化到复杂、真实的场景中。现有评估方法（即主流基准测试）的不足在于，它们主要针对回忆、理解等低阶认知能力，问题结构清晰、背景纯净，导致模型可能过度依赖模式识别而非真正的理解与推理。当面对包含无关细节、模糊语境或需要创造性综合的现实任务时，最先进的LLMs也会出现显著失败，这表明现有基准高估了模型的真实推理能力。

因此，本文要解决的核心问题是：如何系统性地构建能够评估LLMs高阶认知能力（如应用、分析、综合、评价）的评测框架，以更准确地反映其在复杂现实挑战中的实际性能。为此，论文提出了DeepQuestion框架，其核心思路是基于布鲁姆教育目标分类学，通过自动化方法系统性地提升现有数据集的认知复杂度，生成两类新问题：1) 基于场景的问题，用于测试模型在嘈杂、真实情境中应用知识的能力；2) 基于指令的提示，要求模型根据给定解题路径创造新问题，以评估其综合与评价技能，从而填补当前评估体系在认知深度上的空白。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及两个领域：学习科学中的认知分类框架，以及大语言模型在复杂现实问题评估方面的局限性研究。

在**认知分类框架**方面，论文借鉴了学习科学中的层级化学习理论，特别是SOLO分类法和布鲁姆分类法。SOLO分类法将学习从“前结构”到“扩展抽象”分为不同层次；而更广泛应用的布鲁姆分类法则定义了从“记忆”到“创造”的认知层级。本文的创新之处在于，首次系统性地将这些人类学习理论应用于构建LLM的评估框架（DeepQuestion），通过生成基于场景和指令的复杂问题，来检验模型在应用、综合与评价等高阶认知任务上的表现。

在**LLM评估与基准测试**方面，相关研究包括MMLU等标准基准，以及为应对模型性能饱和而提出的更复杂的MMLU-Pro。同时，诸如“The Illusion of Thinking”等研究揭示了LLM在处理复杂推理任务时的局限性。近期也有研究开始关注LLM在标准基准与现实场景之间的性能差距。**本文与这些工作的核心区别在于方法论**：现有研究多集中于构建新的静态数据集或揭示现象，而DeepQuestion则提供了一个可扩展、自动化的框架，能够系统性地提升现有数据集的认知复杂度，从而动态生成更贴近现实、更具认知深度的评估挑战。这为持续、系统地评估LLM的真实推理能力提供了新工具。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为DeepQuestion的可扩展、自动化框架来解决现有基准测试无法反映真实世界任务复杂性的问题。该框架基于布鲁姆分类学，系统地提升现有数据集的认知复杂度，从而更准确地评估大语言模型在复杂、真实场景下的推理能力。

核心方法包括两个关键转换技术：问题到场景（Q2S）和问题到指令（Q2I）。Q2S针对布鲁姆分类学中的“应用”层级，将原始问题嵌入到充满约束和冗余细节的现实叙事场景中，要求模型从中提取相关信息并应用知识解决问题，从而测试其在嘈杂真实环境中的知识迁移和适应能力。Q2I则针对更高的“评估”和“创造”层级，将任务方向反转：不是让模型解决问题，而是根据给定的解决方案路径，生成一个与之主题和推理过程一致的新问题。这要求模型具备深层的概念理解、批判性评估和创造性综合能力。

整体框架由一个自动化的提示生成管道支撑，这是实现可扩展性的关键技术。该管道通过两个LLM（提示生成器和提示评估器）之间的迭代对话运行：生成器根据源基准的随机样本和高级目标描述生成初始提示；评估器根据预定义标准（如清晰度、相关性）对提示进行评分并提供反馈；如果评分低于阈值（如8分），生成器则根据反馈修订提示，循环直至生成合格提示。最终通过的提示会由人类专家审核，确保质量。此后，该提示被用于自动将整个基准数据集转换为Q2S或Q2I变体。

创新点主要体现在三个方面：一是理论指导的系统性，以布鲁姆分类学为原则框架，为认知复杂度的增加提供了可解释、可度量的路径，超越了随意增加难度的方式。二是任务设计的针对性，Q2S和Q2I分别精准对应了真实世界常需但基准测试中 underrepresented 的高阶推理技能（应用与创造/综合）。三是实现过程的自动化与可扩展性，通过创新的提示生成管道，摆脱了对人工设计提示的依赖，使得框架能够高效适配不同领域和风格的基准数据集，实现了从“人工精心设计”到“系统自动生成”真实世界挑战的转变。

### Q4: 论文做了哪些实验？

实验设置方面，研究者构建了DeepQuestion基准，其方法是将框架应用于随机选取的60个GSM8K英文数学题和60个伊朗大学入学考试的波斯语物理题。生成的问题经过人工质量审核。评估时，模型温度设置为0以确保可复现性。框架内部使用了Gemini 2.5 Pro作为提示生成器、评估器和问题生成器LLM。实验包含两种任务设置：Q2S（根据场景问题生成解决方案）和Q2I（根据指令生成问题）。评估采用两步法：首先进行可解答性检查，验证强模型（O4-mini）和模型自身能否正确解答生成的问题；其次采用LLM-as-Judge方法，使用O4-mini根据专家定义的五个标准对问题质量进行定性评估：推理需求、数值质量、物理真实性、清晰简洁性以及解答泄露情况。

使用的数据集/基准测试包括GSM8K（英文数学）和伊朗大学入学考试物理题（波斯语）。对比方法涉及将生成的深度问题（Q2S和Q2I）与原始问题进行比较。评估模型涵盖了十种领先的开源和专有模型，包括Gemini-2、GPT-4.1、Llama-3.1、Deepseek-V3、Deepseek-R1、O4-mini、Gemma3、Phi4和Qwen3。

主要结果与关键数据指标如下：在Q2S任务上，通用模型性能下降适中，部分模型如Gemma-3-27B和DeepSeek-v3甚至取得相当或更好的表现。然而，在要求更高认知水平的Q2I任务上，所有模型均出现显著性能下降。具体而言，在GSM8K和物理数据集的指令式问题生成（Q2I）上，没有模型准确率超过38%（尽管原始问题准确率超过95%）。推理模型在Q2I任务上性能下降相对较小，但仍下降8-30%，例如Deepseek-R1在GSM8K上下降30%，在物理数据集上下降10%；Qwen-3-32B在两个数据集上均下降11%。质量评估显示，在物理问题的推理需求、创造性和简洁性等维度上，原始问题在超过50%的情况下优于模型生成的问题。跨语言实验进一步证实了性能下降源于认知复杂性而非语言因素：例如，在翻译后的物理数据集中，O4-mini在原始、Q2S和Q2I任务上的准确率分别为83.33%、80.00%和73.33%；在波斯语翻译的GSM8K上，Llama3-70B的准确率从88.33%降至75.00%，再降至11.67%。这些结果一致表明，随着任务在布鲁姆分类学认知层次上的提升，模型性能出现急剧下降，准确率最大降幅可达70%，凸显了当前基准对LLM真实推理能力的高估。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来可进一步探索的点包括：首先，将DeepQuestion框架扩展到法律、医学、工程等专业领域，以评估LLMs在特定领域的深层推理和知识应用能力，这能揭示模型在复杂现实场景中的局限性。其次，研究如何利用该框架生成课程式训练数据，按照认知层次（如布鲁姆分类法）循序渐进地训练模型，可能提升其高阶思维和迁移学习能力。此外，可以探索自动化基准构建与自我改进评估管道的结合，使评测体系能动态适应模型发展，更精准地反映其真实能力。最后，论文指出模型在创造性问题解决上表现薄弱，未来可设计更强调综合与评价能力的任务，例如让模型基于解决方案反推问题或进行多步骤规划，以推动其实现更接近人类的深度理解与泛化。

### Q6: 总结一下论文的主要内容

该论文针对当前大语言模型在标准基准测试上表现优异，但在复杂现实问题中泛化能力不足的问题，提出了DeepQuestion框架。其核心贡献是构建了一个基于布鲁姆分类法的、可扩展的自动化框架，用于系统性地提升现有数据集的认知复杂度，从而更真实地评估LLMs的高阶推理能力。

方法上，DeepQuestion将传统问答对转化为两类任务：一是基于场景的问题，在嘈杂的现实情境中测试知识应用能力；二是指令驱动的任务，要求模型根据给定解题路径生成新问题，以评估其综合与评价技能。这为评估增加了可解释的认知复杂度层次。

通过对十个领先的开源和专有模型进行广泛评估，论文主要结论是：随着任务认知层级的提升，所有模型的性能均出现显著下降，准确率降幅高达70%。这证明当前基准测试高估了LLMs的真实推理能力，并凸显了构建认知多样性评估框架以指导未来LLM发展的紧迫性。该框架为跨领域构建有意义的基准测试提供了可复现的基础。
