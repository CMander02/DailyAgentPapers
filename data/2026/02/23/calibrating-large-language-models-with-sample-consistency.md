---
title: "Calibrating Large Language Models with Sample Consistency"
authors:
  - "Qing Lyu"
  - "Kumar Shridhar"
  - "Chaitanya Malaviya"
  - "Li Zhang"
  - "Yanai Elazar"
  - "Niket Tandon"
  - "Marianna Apidianaki"
  - "Mrinmaya Sachan"
  - "Chris Callison-Burch"
date: "2024-02-21"
arxiv_id: "2402.13904"
arxiv_url: "https://arxiv.org/abs/2402.13904"
pdf_url: "https://arxiv.org/pdf/2402.13904v2"
categories:
  - "cs.CL"
tags:
  - "LLM Calibration"
  - "Confidence Estimation"
  - "Model Reliability"
  - "Reasoning"
  - "Post-hoc Methods"
relevance_score: 5.5
---

# Calibrating Large Language Models with Sample Consistency

## 原始摘要

Accurately gauging the confidence level of Large Language Models' (LLMs) predictions is pivotal for their reliable application. However, LLMs are often uncalibrated inherently and elude conventional calibration techniques due to their proprietary nature and massive scale. In this work, we explore the potential of deriving confidence from the distribution of multiple randomly sampled model generations, via three measures of consistency. We perform an extensive evaluation across various open and closed-source models on nine reasoning datasets. Results show that consistency-based calibration methods outperform existing post-hoc approaches. Meanwhile, we find that factors such as intermediate explanations, model scaling, and larger sample sizes enhance calibration, while instruction-tuning makes calibration more difficult. Moreover, confidence scores obtained from consistency have the potential to enhance model performance. Finally, we offer practical guidance on choosing suitable consistency metrics for calibration, tailored to the characteristics of various LMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）预测置信度校准的难题。研究背景是，尽管LLM在各种任务上表现出色，但其预测往往缺乏可靠的置信度估计，即模型给出的置信水平与其答案正确的实际可能性并不匹配。这种“未校准”状态限制了LLM的可信部署，例如在需要选择性预测或用户决定是否信任模型的场景中。现有方法主要分为两类：一是依赖模型输出概率对数等内部信息的传统校准技术，但这些方法通常需要对模型进行重新训练或调整，对于规模庞大、参数不公开的闭源模型而言，成本高昂甚至不可行；二是近期出现的基于样本一致性的后校准方法，它们仅需模型多次生成结果，更具实用性。然而，现有一致性方法主要依赖“原始生成与多个随机生成之间的一致性（即答案的简单多数同意）”，未能充分利用多次生成结果的完整分布信息，可能导致过度自信（例如，当所有答案出现频率相同时，仅基于最流行答案的简单一致性会给出高置信度，但这并不合理）。

因此，本文要解决的核心问题是：如何更好地从模型多次生成样本的一致性中，提取出更准确、更可靠的置信度估计？具体而言，论文系统性地研究并比较了三种衡量一致性的指标——基于同意度、基于熵和基于第一-第二距离（FSD）的方法，以探索如何最有效地利用生成样本的分布信息进行置信度校准。研究旨在为不同特性的LLM（开源与闭源）在多种推理任务上，提供一种高效、无需额外训练数据的后校准方案，并深入分析影响校准效果的各种因素（如是否生成中间解释、模型规模、指令微调、样本数量等），最终为实践者提供选择合适一致性指标的具体指导。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：置信度校准、一致性概念以及大语言模型的推理策略。

在**置信度校准**方面，传统方法（如基于概率、集成或密度的方法）需要访问模型内部逻辑或预训练数据，成本高昂且不适用于闭源大模型。为此，研究者开发了多种事后校准方法，例如提示模型自我评估其答案为“真”的概率，或让模型直接口头表达置信度。另一类工作则基于样本一致性进行校准，仅需模型的输入和输出，但现有研究多集中于基于“一致同意”的度量，可能导致过度自信。本文系统性地探索了如何从一致性中更好地提取置信度，并比较了三种一致性度量，弥补了现有研究的不足。

在**一致性**概念上，NLP领域存在多种定义，如事实对齐、逻辑严谨性或不同输出间的一致性等。本文特指“多个模型生成结果的分布均匀性”，并通过三种定量指标进行衡量，与此前工作形成对比。

在**推理策略**方面，大语言模型通过上下文学习展现出强大的推理能力。除标准提示外，基于解释的提示（如生成推理链、分解子问题或使用结构化语言）能显著提升性能。本文研究了不同代表性推理策略对校准效果的影响，将校准研究与推理技术进展相结合。

### Q3: 论文如何解决这个问题？

论文通过提出一种基于样本一致性的后校准方法来解决大语言模型置信度难以准确评估的问题。其核心思想是：对同一输入进行多次随机采样生成，通过分析这些生成答案之间的一致性来推导模型预测的置信度。

**整体框架与流程**：首先，对于给定的输入x，使用LLM生成n个候选输出。接着，从每个输出中通过正则表达式解析出最终答案，形成一个答案多重集。然后，对该答案集进行多数投票，得到最高票答案。最后，基于整个答案集的分布，计算一致性分数作为该预测的置信度分数。

**主要模块与关键技术**：
1.  **多答案生成与解析模块**：采用随机采样策略生成多个输出，确保答案的多样性，并使用正则匹配可靠地提取结构化答案。
2.  **一致性度量模块**：这是方法的核心创新，提出了三种不同的度量方式：
    *   **基于同意度**：计算所有答案中与最高票答案一致的比率。该方法直接但可能忽略次优答案的分布信息。
    *   **基于熵**：计算答案分布的归一化熵。熵越低表示答案越集中、一致性越高，通过“1-熵”将其转换为置信度分数。该方法考虑了所有唯一答案的完整分布。
    *   **基于首-次距离**：计算最高票答案与次高票答案的同意度之差。这是本文的创新点之一，旨在处理模型对前两个答案都较为确信的情况，避免仅基于最高票答案导致的过度自信，能更细腻地捕捉模型在“犹豫不决”时的置信状态。

**创新点**：
1.  **无需模型内部访问**：该方法完全基于模型的黑盒生成输出，不依赖模型内部的logits或概率，适用于无法获取内部信息的专有或大规模模型。
2.  **提出多种一致性度量**：特别是FSD度量，针对LLM开放式生成任务中答案分布的特点进行了设计，比传统的同意度或熵度量更具针对性。
3.  **系统性实证研究**：论文不仅提出了方法，还通过大量实验分析了不同因素（如提示策略、模型规模、采样数量）对校准效果的影响，并给出了根据模型特性选择合适一致性度量的实用指南。

### Q4: 论文做了哪些实验？

论文进行了广泛的实验来评估基于一致性的校准方法。实验设置包括：使用九种推理数据集（涵盖数学应用题、多跳问答、规划和关系推理四大任务），对比了三种一致性指标（熵、一致性和FSD）与多种后处理方法（原始logits、P(True)和言语化置信度）。评估主要使用Brier Score（越低越好）和ECE作为校准指标。

主要结果如下：基于一致性的方法在所有测试模型上均显著优于基线方法。例如，对于闭源模型，一致性指标的平均Brier Score（Codex: 0.151-0.175, GPT-3.5-turbo: 0.205-0.221, GPT-4: 0.114-0.119）均低于最佳基线。对于开源模型（如LLaMA-70B），一致性指标（0.154-0.182）也远优于logit基线（0.252）。在一致性指标中，开源模型和Codex倾向于使用“一致性”指标，而GPT-3.5-turbo和GPT-4则使用FSD和熵效果相近。

分析表明：模型缩放（如LLaMA从7B到70B）能改善校准；指令微调（如Mistral-7B-instruct）会使校准更困难；增加采样数量（如达到15-20个样本）能提升校准效果，但3-5个样本已是成本效益较好的选择。此外，包含解释的提示策略（如CoT、FCoT）能显著提升校准水平，且一致性置信度还能用于提升模型性能（如在自我纠正中提高准确率）。

### Q5: 有什么可以进一步探索的点？

本文的局限性为未来研究提供了明确方向。首先，一致性指标缺乏普适性，未来可探索更自适应的指标选择机制，或设计能融合多种一致性度量的元校准器。其次，采样成本虽在15-20次后饱和，但如何动态优化采样次数（如基于问题复杂度自适应调整）值得研究。温度参数的影响分析缺失，需系统探索温度与一致性校准鲁棒性的关系。再者，当前方法仅校准最终答案，未来可扩展到对思维链每一步的置信度进行细粒度校准，这或能提升复杂推理任务的可靠性。最后，可探索将一致性校准与模型内部特征（如注意力分布）结合，以降低对生成样本的依赖。从更广视角看，如何将一致性校准集成到模型训练阶段而非仅后处理，也是一个有潜力的方向。

### Q6: 总结一下论文的主要内容

该论文研究如何通过采样一致性来校准大语言模型的预测置信度，以提升其可靠性。核心问题是传统校准方法难以适用于大规模或专有模型，而论文提出利用多次随机生成样本的一致性来估计置信度，扩展了基于简单一致性的方法，引入了熵和频次标准差等度量。方法上，论文在九个推理数据集上对多种开源和闭源模型进行了广泛评估，发现基于一致性的校准方法优于现有的后处理技术。主要结论包括：生成中间解释、模型规模扩大和增加样本量能改善校准效果，而指令微调则使校准更困难；此外，一致性获得的置信度分数还能通过理想的自校正流程提升模型性能。论文最终提供了根据模型类型、规模和任务选择合适一致性度量的实用指南，推动大语言模型在更可靠的方向应用。
