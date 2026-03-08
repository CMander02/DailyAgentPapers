---
title: "MC-Search: Evaluating and Enhancing Multimodal Agentic Search with Structured Long Reasoning Chains"
authors:
  - "Xuying Ning"
  - "Dongqi Fu"
  - "Tianxin Wei"
  - "Mengting Ai"
  - "Jiaru Zou"
date: "2026-03-01"
arxiv_id: "2603.00873"
arxiv_url: "https://arxiv.org/abs/2603.00873"
pdf_url: "https://arxiv.org/pdf/2603.00873v1"
categories:
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Perception & Multimodal"
relevance_score: 9.0
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Perception & Multimodal"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "Search-Align"
  primary_benchmark: "MC-Search"
---

# MC-Search: Evaluating and Enhancing Multimodal Agentic Search with Structured Long Reasoning Chains

## 原始摘要

With the increasing demand for step-wise, cross-modal, and knowledge-grounded reasoning, multimodal large language models (MLLMs) are evolving beyond the traditional fixed retrieve-then-generate paradigm toward more sophisticated agentic multimodal retrieval-augmented generation (MM-RAG). Existing benchmarks, however, mainly focus on simplified QA with short retrieval chains, leaving adaptive planning and multimodal reasoning underexplored. We present MC-Search, the first benchmark for agentic MM-RAG with long, step-wise annotated reasoning chains spanning five representative reasoning structures. Each example specifies sub-questions, retrieval modalities, supporting facts, and intermediate answers, with fidelity ensured by HAVE (Hop-wise Attribution and Verification of Evidence), resulting in 3,333 high-quality examples averaging 3.7 hops. Beyond answer accuracy, MC-Search introduces new process-level metrics for reasoning quality, stepwise retrieval and planning accuracy. By developing a unified agentic MM-RAG pipeline, we benchmark six leading MLLMs and reveal systematic issues such as over- and under-retrieval and modality-misaligned planning. Finally, we introduce Search-Align, a process-supervised fine-tuning framework leveraging verified reasoning chains, showing that our data not only enables faithful evaluation but also improves planning and retrieval fidelity in open-source MLLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态大语言模型在面向复杂、知识密集型查询时，其代理式检索增强生成能力缺乏有效评估和训练数据的问题。研究背景是，随着多模态大语言模型的发展，其应用场景已从简单的检索-生成范式，转向需要多步骤、跨模态和知识密集型推理的代理式多模态检索增强生成。然而，现有基准测试（如OK-VQA、ViQuAE等）主要关注简化的问答任务，通常只涉及1-2步的短检索链，且缺乏对推理过程的细粒度标注。这导致现有方法存在三个主要不足：一是评估范式固定，无法考察模型自适应的规划能力；二是缺乏对长推理链（≥4步）的评估；三是缺少对推理过程（如子问题分解、模态选择）的逐步标注，难以精确评估模型在复杂多模态环境下的真实推理和检索性能。

因此，本文要解决的核心问题是：如何构建一个能够系统评估并提升多模态代理式搜索与推理能力的基准。为此，论文提出了MC-Search基准，它包含长且结构化的逐步标注推理链，覆盖五种代表性推理拓扑结构，并通过严格的验证确保每一步的必要性。该基准不仅引入了超越答案准确率的、针对推理过程的新评估指标，还揭示了现有领先模型的系统性缺陷（如过度检索、检索不足和模态规划错位）。此外，论文进一步提出了Search-Align框架，利用经过验证的推理链对模型进行过程监督微调，从而证明该基准数据不仅能用于忠实评估，还能有效提升开源模型在规划和检索方面的忠实度。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**评测基准类**、**方法框架类**和**模型评估类**。

在**评测基准类**方面，现有工作如OK-VQA、ViQuAE、WebQA、InfoSeek、MMSearch、Dyn-VQA、MRAG和M²RAG等，主要关注单跳或短链（≤2步）的检索增强问答，且通常采用固定的“检索-生成”范式。这些基准大多缺乏逐步的推理链标注，也未能涵盖复杂的跨模态推理结构。本文提出的MC-Search基准与这些工作的主要区别在于：它首次专注于**长链**（平均3.7跳）、**逐步标注**且包含**五种代表性推理拓扑结构**的多模态智能体检索增强生成（MM-RAG）任务，并通过HAVE程序确保推理步骤的必要性和高质量。

在**方法框架类**方面，传统RAG及MM-RAG方法通常为固定流程，缺乏智能体所需的适应性规划与迭代检索能力。本文提出的Search-Align框架与这些工作的关系是，它建立在智能体MM-RAG范式演进的基础上；其区别在于，它利用经过验证的逐步推理链进行**过程监督微调**，而不仅仅是监督最终答案，从而直接提升了模型在跨模态规划和检索方面的忠实性。

在**模型评估类**方面，已有研究多基于前述的短链基准评估MLLMs的答案准确性。本文与这些工作的关系是，同样对主流MLLMs（包括开源和闭源模型）进行了评估；其区别在于，本文开发了统一的智能体MM-RAG评估流水线，并引入了**过程级评估指标**（如推理质量、逐步检索准确率和规划偏移度），从而系统性地揭示了现有模型在长链、跨模态推理中存在的过度检索、检索不足和模态规划错位等系统性问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个统一的智能体化多模态检索增强生成（MM-RAG）流程和一个名为Search-Align的过程级对齐框架来解决现有基准测试在自适应规划和多模态推理方面的不足。其核心方法是将复杂的多模态搜索推理建模为一个包含三个模块的迭代过程：子查询与动作生成、证据获取、以及迭代推理与合成。

整体框架是一个循环执行的智能体系统。在每次迭代中，智能体首先根据当前上下文生成一个具体的子目标（子查询），并自适应地选择三种检索动作之一：基于文本查询的文本搜索、基于文本查询的图像搜索，或基于输入图像的图像搜索。这构成了第一个模块。接着，在证据获取模块中，系统在本地多模态知识库中执行所选动作，通过多模态编码器进行稠密检索，并返回最相关的文本或视觉证据（top-1）。然后，模型基于此证据生成一个中间答案。第三个模块是迭代推理与合成，生成的子答案和证据被反馈回模型，以指导下一步的规划。智能体会动态判断累积证据是否充足，若充足则输出最终答案，否则开启新一轮迭代。这种设计使得完整的推理轨迹得以暴露，支持细粒度的过程评估。

其关键技术创新点主要体现在两方面。一是**过程级评估指标**：MC-Search基准不仅关注最终答案准确性，还引入了针对推理质量、逐步检索准确性和规划准确性的新指标，从而能够系统性地诊断模型在规划（如检索过度或不足）和模态对齐方面的问题。二是**Search-Align对齐框架**：这是一个利用已验证的长推理链进行过程监督的微调框架。它并非仅监督最终答案，而是将逐步标注的子问题、检索动作、证据和中间答案，辅以由大模型生成的解释性“推理思路”，构建成连贯的对话轨迹。通过对开源MLLMs在此类数据上进行监督微调，模型能够学习如何进行跨步骤的规划、选择检索模态并整合证据，从而显著提升其在长视野、多模态推理任务中的规划忠实度和检索准确性。

### Q4: 论文做了哪些实验？

本论文在提出的MC-Search基准上进行了系统性实验。实验设置方面，作者构建了一个统一的智能体化多模态检索增强生成（MM-RAG）评测管道，对6个领先的多模态大语言模型（MLLM）进行评估，包括闭源模型（GPT-4o-Mini, Gemini-2.5-Flash, Gemini-2.5-Pro, Claude-3.7-Sonnet）和开源模型（InternVL3.5-8B, Qwen2.5-VL-7B）。所有模型在相同条件下评测：使用相同的嵌入模型进行多模态检索、相同的提示词和解码参数，每步检索限制为从本地多模态知识库中返回Top-1结果，并强制执行相同的最大推理迭代次数。

数据集/基准测试即MC-Search，它包含3333个高质量样例，平均推理链长度为3.7跳，涵盖五种代表性推理结构（如图像发起链、多图像分叉链、文本发起链等）。对比方法包括上述各MLLM的基线版本，以及应用了论文提出的Search-Align过程监督微调框架后的开源模型版本。此外，附录中还补充了固定步数RAG基线（1跳和2跳）的结果。

主要结果通过六项指标呈现，包括答案准确性（F1、ΔF1、Golden F1、LLM-as-a-Judge）和推理链对齐度（每步命中率HPS、推演偏差RD）。关键数据指标显示：在闭源模型中，Gemini-2.5-Pro在多项任务中表现最佳，例如在图像发起链任务中F1达到47.61，在多图像分叉链中F1为40.37。开源模型初始表现较弱，但经过Search-Align微调后性能显著提升，例如Qwen2.5-VL-7B在图像发起链上的F1从26.30提升至45.70，链对齐指标HPS从16.51大幅提升至33.59，RD从4.04降至0.70。实验还深入分析了推理链长度的影响、过度检索与检索不足的现象、模型的模态偏好以及典型的错误类型。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来可进一步探索的点包括：首先，论文的基准测试主要集中于五种推理结构，未来可扩展至更复杂、动态或开放域的真实世界场景，如涉及实时信息更新或多轮对话交互的代理任务。其次，当前检索限制为 top-1 结果且依赖本地知识库，这可能导致信息遗漏或偏差；未来可探索动态检索数量、多模态检索的融合策略以及对外部动态知识源（如网络搜索）的集成。此外，论文揭示了模型存在过度检索、检索不足和模态规划错位等系统性问题，未来研究可设计更精细的规划模块，例如引入强化学习来优化检索决策，或开发跨模态对齐的预训练目标以提升模态切换的准确性。最后，Search-Align 框架虽提升了开源模型性能，但其监督微调依赖于人工标注的推理链，成本较高；未来可探索半监督或自监督方法，利用模型自身生成的可信轨迹进行迭代优化，从而提升方法的可扩展性和泛化能力。

### Q6: 总结一下论文的主要内容

该论文提出了MC-Search基准，旨在评估和增强多模态智能体搜索中的长链结构化推理能力。核心问题是现有基准多关注简短检索链的简单问答，而忽略了自适应规划和多模态推理。为此，论文构建了首个专注于长步骤、带注释推理链的智能体多模态检索增强生成基准，涵盖五种代表性推理结构，并通过证据逐跳归因与验证确保数据质量，最终包含3333个高质量样本。

方法上，论文开发了统一的智能体多模态检索增强生成流程，用以系统评估六个领先的多模态大语言模型，并揭示了过度检索、检索不足及模态规划错位等系统性问题。此外，论文提出了Search-Align框架，这是一个利用已验证推理链进行过程监督微调的方法，旨在提升模型规划与检索的忠实度。

主要结论表明，MC-Search不仅能实现忠实的过程级评估，其数据还能有效提升开源模型在复杂多模态任务中的规划与检索性能，推动了智能体多模态推理向更结构化、可靠的方向发展。
