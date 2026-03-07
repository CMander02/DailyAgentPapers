---
title: "Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory"
authors:
  - "Shunki Uebayashi"
  - "Kento Masui"
  - "Kyohei Atarashi"
  - "Han Bao"
  - "Hisashi Kashima"
date: "2026-03-03"
arxiv_id: "2603.02663"
arxiv_url: "https://arxiv.org/abs/2603.02663"
pdf_url: "https://arxiv.org/pdf/2603.02663v1"
categories:
  - "cs.CL"
  - "cs.CV"
tags:
  - "Perception & Multimodal"
  - "Reasoning & Planning"
relevance_score: 4.5
taxonomy:
  capability:
    - "Perception & Multimodal"
    - "Reasoning & Planning"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "Multi-modal and multidimensional item response theory (M3IRT)"
  primary_benchmark: "N/A"
---

# Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory

## 原始摘要

Multimodal Large Language Models (MLLMs) have recently emerged as general architectures capable of reasoning over diverse modalities. Benchmarks for MLLMs should measure their ability for cross-modal integration. However, current benchmarks are filled with shortcut questions, which can be solved using only a single modality, thereby yielding unreliable rankings. For example, in vision-language cases, we can find the correct answer without either the image or the text. These low-quality questions unnecessarily increase the size and computational requirements of benchmarks. We introduce a multi-modal and multidimensional item response theory framework (M3IRT) that extends classical IRT by decomposing both model ability and item difficulty into image-only, text-only, and cross-modal components. M3IRT estimates cross-modal ability of MLLMs and each question's cross-modal difficulty, enabling compact, high-quality subsets that better reflect multimodal reasoning. Across 24 VLMs on three benchmarks, M3IRT prioritizes genuinely cross-modal questions over shortcuts and preserves ranking fidelity even when 50% of items are artificially generated low-quality questions, thereby reducing evaluation cost while improving reliability. M3IRT thus offers a practical tool for assessing cross-modal reasoning and refining multimodal benchmarks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态大语言模型（MLLMs）评估基准中存在的关键问题。研究背景是，随着MLLMs（尤其是视觉-语言模型VLMs）的快速发展，它们被期望能够执行需要跨模态推理的下游任务（如医疗图像诊断）。因此，需要可靠的多模态基准来评估和比较模型性能。然而，现有基准存在严重不足：其中充斥着大量“捷径问题”，这类问题仅凭单一模态（例如仅文本或仅图像）即可解答，而无需真正的跨模态整合。这导致基准测试结果不可靠，无法真实反映模型的跨模态推理能力，同时这些低质量问题还徒增了基准的规模和计算成本。

针对上述问题，本文的核心目标是提出一种新方法，以更精准地评估MLLMs的跨模态推理能力，并构建更紧凑、高质量的评估基准子集。具体而言，论文引入了多模态多维项目反应理论框架（M3IRT），它扩展了经典IRT，将模型能力和题目难度分解为图像、文本和跨模态三个潜在成分。通过这一分解，M3IRT能够量化每个模型的跨模态能力以及每个题目对跨模态推理的真实需求，从而有效区分真正的跨模态问题与单模态捷径问题。这使得研究者能够从现有基准中筛选出高质量、真正需要跨模态推理的题目子集，在显著降低评估计算开销的同时，确保模型排名的可靠性。实验表明，即使在基准中混入高达50%的低质量人工题目，该方法仍能保持排名保真度。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多模态大模型（MLLM）评测基准、基准优化方法（非IRT方法与IRT方法）。

**1. 多模态大模型评测基准**：相关工作包括大型静态基准（如MMMU、MathVista、SEED-Bench、EMMA、CCHall）和动态/实时评测方法（如VLB/FLEX、MAC、LiveXiv）。这些基准旨在评估多模态整合能力，但本文指出它们普遍存在“捷径问题”（即仅凭单一模态即可作答的低质量题目），导致评测结果不可靠且计算成本高昂。本文提出的M3IRT框架旨在从这类基准中筛选出真正需要跨模态推理的高质量题目子集。

**2. 非IRT基准优化方法**：包括基于聚类的代表性题目选择（如主动测试、定制基准创建）、自适应采样（如SubLIME、Dele）以及考虑题目间依赖关系的方法。近期工作如FlashEval为文生图任务提出了进化算法。这些方法虽能压缩基准规模，但本文指出其共同局限是**未明确考虑题目是否真正需要跨模态整合**，因此仍可能包含大量捷径问题。

**3. 基于IRT的基准优化方法**：项目反应理论（IRT）已应用于NLP、推荐系统及大模型领域，用于同时建模模型能力与题目参数（如难度）。相关工作包括MetaBench（从多个基准中提炼稀疏基准）、TinyBenchmarks（基于聚类的采样）以及用于自适应测试的方法。**本文与这些工作的核心区别在于**：传统IRT是单维度的（如仅一个“难度”参数），而本文提出的M3IRT是**多模态、多维度的**，它将模型能力和题目难度分解为“仅图像”、“仅文本”和“跨模态”三个独立成分，从而能专门估计模型的跨模态推理能力和题目的跨模态难度，实现对跨模态推理更精准的评估与基准净化。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为多模态多维项目反应理论（M3IRT）的框架来解决现有多模态大语言模型（MLLM）基准测试中充斥“捷径问题”（即仅凭单一模态即可解答的问题）导致评估不可靠且成本高昂的问题。其核心方法是对经典项目反应理论（IRT）进行扩展，将模型能力和题目难度分解为模态特定成分与跨模态成分，从而精准量化并筛选出真正需要跨模态推理的高质量题目。

整体框架基于一个概率模型。首先，为每个题目定义模态指示符（例如在视觉-语言任务中，s = (s_image, s_text) 表示是否提供图像或文本）。对于每个待评估的模型（即“被试者”）i 和题目 j，模型的能力 θ_i 被分解为四个潜在成分：基础能力 θ_base、图像特定能力 θ_image、文本特定能力 θ_text 以及关键的跨模态协同能力 θ_synergy。相应地，题目的难度 b_j、区分度 a_j 也分解为对应的基础、图像、文本和跨模态成分（b_base, b_image, b_text, b_synergy 与 a_base, a_image, a_text, a_synergy）。通过模态指示符 s 对这些成分进行线性组合，得到在该题目格式下的综合能力值 θ_full、难度值 b_full 和区分度 a_full。例如，当图像和文本都提供时（s=(1,1)），θ_full = θ_base + θ_image + θ_text + θ_synergy，这迫使模型必须利用跨模态协同能力。

关键技术在于利用这个分解模型进行参数估计与题目选择。论文提出了两种具体模型：多模态项目反应理论（MMIRT，即单维版本）和多维多模态项目反应理论（MMMIRT，即多维版本）。在MMMIRT中，能力、难度和区分度都被表示为向量，并通过一个包含模态指示符的向量运算来计算模型正确回答的概率。参数估计采用随机梯度下降法最小化负对数似然损失，这种方法能处理部分观测数据（即不需要每个模型回答所有题目的所有模态变体），降低了数据收集成本。

最大的创新点在于将上述估计模型与计算机化自适应测试（CAT）相结合，构建一个紧凑而高质量的基准测试子集。具体而言，利用费舍尔信息量（对于MMMIRT是信息矩阵）来衡量每个题目对估计模型（特别是跨模态）能力的信息贡献度。采用D-最优性准则，自适应地选择能最大化累积信息矩阵行列式的题目，从而在保留评估排名保真度的前提下，显著减少所需题目数量。实验表明，即使基准中混入50%的低质量（捷径）题目，该方法也能优先选择出真正需要跨模态推理的题目，在保证可靠性的同时降低了评估的计算开销。

### Q4: 论文做了哪些实验？

论文实验主要围绕验证所提出的多模态多维项目反应理论框架（M3IRT）的有效性展开。实验使用了三个视觉语言模型（VLM）基准测试：MMMU（验证集900个问题，涵盖艺术、商业、科学等多学科本科水平推理）、MathVista（test-min集1000个问题，评估涉及图表等的数学推理）和SEED-Bench（L1和L2集共1000个问题，用于全面评估多模态能力）。为了模拟现实数据集中可能存在的低质量问题，研究还构建了一个合成污染基准，通过交换原问题的图像或文本来生成简单的低质量问题，使基准中低质量问题占比达到50%。

实验评估了24个VLMs，包括GPT-4.1、Gemini-2.0、Claude-3.7系列以及Qwen-2.5-vl、Llama-3.2、Pixtral等开源模型。对比方法包括随机选择（Random）、基于经典IRT的Fisher信息子集选择（IRT）、基于多维IRT（MIRT）的选择、TinyBenchmarks（基于IRT的LLM基准优化方法）以及扩展用于VLM基准的FlashEval（将问题视为提示词）。

主要结果包括：1）M3IRT能有效估计问题的跨模态难度（β_synergy）和模型的跨模态能力（θ_synergy），从而识别真正需要跨模态推理的问题。例如，在MMMU上，排名第一的模型展现出高跨模态能力，而第二、三名则主要依赖文本理解。2）在从污染基准中选择紧凑子集以评估模型排名的任务中，M3IRT和其变体MMIRT显著优于基线。关键指标上，在MMMU中，MMIRT仅使用3%的子集就能达到0.9的斯皮尔曼等级相关系数，M3IRT仅用1%的子集即可达到0.8；在MathVista中，M3IRT用2%的子集达到0.84的相关性。同时，所选子集中低质量问题的比例（γ）远低于基线方法，例如在MMMU中即使抽取50%的子集，γ也仅为24%，而基线方法则高很多。3）在预测模型回答的ROC-AUC指标上，所提方法与标准IRT性能相当（AUC约0.8），表明其能有效捕捉模型能力和问题特征，即使存在低质量问题。

### Q5: 有什么可以进一步探索的点？

本文提出的M3IRT框架在评估多模态大模型的跨模态推理能力方面迈出了重要一步，但其仍有局限性和广阔的探索空间。首先，当前方法主要聚焦于视觉-语言模态，未来可扩展至音频、视频、触觉等多模态组合，以构建更通用的评估理论。其次，M3IRT对题目难度的分解仍依赖于统计模型估计，未来可结合生成式AI自动生成或改写题目，主动控制其单模态与跨模态难度成分，从而构建更精准的基准测试。此外，该框架目前侧重于静态评估，未来可探索其在模型训练过程中的动态监控作用，例如实时反馈哪些数据或任务最能提升跨模态能力，以指导更高效的训练。最后，如何将评估结果与模型的可解释性结合，深入理解模型进行跨模态推理的内部机制，也是一个值得探索的方向。

### Q6: 总结一下论文的主要内容

该论文针对当前多模态大语言模型（MLLMs）评测基准中普遍存在的“捷径问题”（即仅凭单一模态信息即可作答）提出了一个创新的评估框架M3IRT。核心问题是现有基准因包含大量低质量题目，导致对模型真实跨模态推理能力的评估不可靠且计算成本高昂。

论文的核心贡献是提出了多模态多维项目反应理论（M3IRT）。该方法将经典的IRT扩展至多模态场景，将模型的“能力”和题目的“难度”都分解为仅图像、仅文本和跨模态三个独立分量。通过这种分解，M3IRT能够精准估计出模型的跨模态推理能力以及每个题目对跨模态能力的真实需求程度。

基于此方法，论文的主要结论是：M3IRT能有效识别并优先选择真正需要跨模态整合的高质量题目，过滤掉“捷径问题”。实验表明，在三个基准上对24个视觉语言模型进行评估时，即使数据集中混入50%的人工生成低质量题目，M3IRT构建的紧凑子集仍能保持模型排名的保真度。这为创建更可靠、更高效的多模态评测基准提供了实用工具，显著降低了评估成本并提升了可靠性。
