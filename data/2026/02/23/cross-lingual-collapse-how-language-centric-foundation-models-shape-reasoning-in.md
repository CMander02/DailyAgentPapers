---
title: "Cross-lingual Collapse: How Language-Centric Foundation Models Shape Reasoning in Large Language Models"
authors:
  - "Cheonbok Park"
  - "Jeonghoon Kim"
  - "Joosung Lee"
  - "Sanghwan Bae"
  - "Jaegul Choo"
  - "Kang Min Yoo"
date: "2025-06-06"
arxiv_id: "2506.05850"
arxiv_url: "https://arxiv.org/abs/2506.05850"
pdf_url: "https://arxiv.org/pdf/2506.05850v3"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "大型语言模型"
  - "强化学习"
  - "思维链"
  - "多语言模型"
  - "推理能力"
  - "模型训练"
  - "语言一致性"
relevance_score: 5.5
---

# Cross-lingual Collapse: How Language-Centric Foundation Models Shape Reasoning in Large Language Models

## 原始摘要

Reinforcement learning with verifiable reward (RLVR) has been instrumental in eliciting strong reasoning capabilities from large language models (LLMs) via long chains of thought (CoT). During RLVR training, we formalize and systemically study an empirical phenomenon whereby a multilingual model's CoT reverts to its dominant pre-training language (e.g., English) even when prompted in another language, which we term Cross-lingual Collapse. Because the long-CoT regime magnifies exposure to linguistic priors, the underlying trade-off between maximizing reasoning depth and preserving target-language fidelity has remained under-characterized. To examine this trade-off, we train LLMs with Group-Relative Policy Optimization (GRPO) on translated versions of math datasets widely used to elicit long-CoT reasoning. Throughout training, we track both task accuracy and the language consistency of reasoning chains. Our experiments yield three findings: (i) under RLVR, CoT in LLMs systematically drifts toward the pre-training dominant language as reasoning performance rises; (ii) English-centric priors, long-CoT GRPO optimization, task difficulty, and high-entropy decoding jointly amplify this drift, and the pattern persists beyond mathematics; and (iii) interventions that favor target-language traces--via a language-consistency reward, decoding-time controls, or more balanced backbones--mitigate collapse but reveal a persistent performance-fidelity trade-off.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并系统研究大语言模型在强化学习验证奖励训练中出现的一种现象，即“跨语言坍缩”。研究背景在于，当前通过长思维链监督训练的LLMs在数学、代码生成等复杂推理任务上表现出色，但这类研究多集中于英语，对多语言环境下的推理能力探索不足。现有方法通常假设模型能保持目标语言推理，然而在追求深度、可验证的长思维链推理时，模型会大量暴露于预训练阶段的先验知识；由于主流开源基础模型多为英语中心，优化过程可能偏好英语推理路径，导致即使用其他语言提示，思维链仍会回退到英语，牺牲了目标语言的保真度。

本文要解决的核心问题是：在强化学习验证奖励框架下，如何理解并量化模型在提升推理性能与保持目标语言一致性之间的固有权衡。具体而言，论文通过在多语言数学数据集上训练模型，追踪任务准确率和思维链语言一致性，首次形式化了跨语言坍缩现象，并系统分析了其放大因素（如英语中心先验、长思维链优化、任务难度等）及缓解措施（如语言一致性奖励、解码控制等），最终揭示了性能与保真度之间难以完全消除的权衡关系。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。

在方法类研究中，强化学习与可验证奖励（RLVR）是激发大语言模型（LLM）推理能力的关键技术。相关工作包括使用**思维链（CoT）** 进行推理，以及基于强化学习的优化方法。本文特别聚焦于**组相对策略优化（GRPO）**，这是一种无需监督预热、纯粹基于强化学习的训练范式。例如，DeepSeek-R1-Zero和DeepSeek-R1模型的研究，通过大规模GRPO训练在数学等领域取得了显著性能提升，这构成了本文方法的基础。本文与这些工作的关系在于，它同样采用GRPO来训练模型以激发长链推理，但其核心区别在于，本文系统性地研究了在此过程中出现的**跨语言崩溃**现象，即模型推理语言会向其预训练主导语言（如英语）回归，这是先前强化学习推理研究中所忽视的。

在应用类研究中，相关工作主要集中于使用多语言模型进行数学推理等任务。本文与这些工作的区别在于，它不仅关注任务准确率，还首次系统性地追踪和量化了**推理链的语言一致性**，揭示了在追求深度推理性能与保持目标语言保真度之间存在的根本性权衡。因此，本文在应用层面深化了对多语言模型推理行为内在机制的理解，补充了现有研究。

### Q3: 论文如何解决这个问题？

论文通过系统性实验和分析来探究和解决“跨语言坍缩”问题。其核心方法是利用基于可验证奖励的强化学习（RLVR），特别是分组相对策略优化（GRPO）算法，在翻译后的数学推理数据集（如GSM8K）上微调大语言模型，并追踪任务准确性与推理链语言一致性之间的权衡。

整体框架包含几个关键模块：首先，选取具有不同语言主导特性的基础模型（如英语主导的OLMo2-1B和多语言主导的Llama-3.2-3B、Qwen-2.5-1.5B）作为研究对象。其次，使用GRPO算法进行微调，旨在提升模型的长链思维推理能力。训练数据为将GSM8K数据集翻译成多种语言（如中文、韩语、乌克兰语、泰语、日语）的版本，以模拟多语言推理场景。评估则同时在翻译后的GSM8K和MATH500测试集上进行，使用准确率（Acc）和目标语言词比率（Target WR）等指标。

研究发现的核心问题和解决思路体现在对“性能-保真度权衡”的机制剖析上。论文指出，在RLVR训练过程中，模型为最大化奖励（即解题正确性），其思维链会系统性地漂移回预训练主导语言（通常是英语），导致目标语言词比率下降。这种坍缩由几个因素共同放大：英语中心先验、长链思维GRPO优化、任务难度和高熵解码。

为缓解坍缩，论文探索了几种干预措施：1）引入语言一致性奖励（Lang loss），在训练目标中额外鼓励模型保持输出语言与输入提示语言一致；2）在解码阶段进行控制；3）使用语言能力更平衡的骨干模型（如多语言模型）。实验表明，这些干预能在一定程度上维持目标语言保真度，但往往会以牺牲部分性能提升为代价，揭示了准确性与语言忠实度之间固有的、持续的权衡。此外，研究还发现，任务难度（如混入更难的SimpleRL-Zoo数据集）会显著加速跨语言坍缩，且该现象不限于数学领域，在通用知识问答（如MMLU-Lite）中同样存在。

创新点在于首次形式化并实证研究了RLVR训练中出现的“跨语言坍缩”现象，系统性地揭示了其驱动因素（模型先验、训练算法、任务属性）和微观机制（探索阶段对英语轨迹的优势加权），并通过控制实验量化了性能与语言保真度之间的根本性权衡。

### Q4: 论文做了哪些实验？

实验设置方面，研究使用GRPO（一种强化学习算法）对基础大语言模型进行微调，以增强其推理能力。基础模型分为两类：英语主导模型（如OLMo2-1B Instruct）和非英语主导的多语言模型（如Llama-3.2-3B Instruct和Qwen-2.5-1.5B Instruct）。训练数据集主要使用广泛用于数学推理的GSM8K训练集，并将其通过GPT-4o翻译成多种目标语言，包括中文（ZH）、韩语（KO）、乌克兰语（UK）、泰语（TH）和日语（JA），这些语言覆盖了不同的文字脚本和预训练资源水平（高、中、低资源）。评估则在翻译后的GSM8K和MATH500测试集上进行。

对比方法主要考察了不同基础模型在GRPO微调后的表现，并引入了干预措施进行对比，例如添加语言一致性奖励（Lang loss）、在训练中混合更具挑战性的数据集（如SimpleRL-Zoo子集），以及分析不同解码策略的影响。

主要结果和关键数据指标如下：
1.  **性能与语言保真度的权衡**：GRPO训练一致地提高了目标语言的任务准确率，但往往以牺牲目标语言的保真度为代价。例如，英语主导的OLMo2模型在微调后，在多个目标语言上准确率大幅提升（如韩语GSM8K准确率从基线的约6.6%提升至46.5%，相对提升+39.9%），但目标语言词比率（Target WR）急剧下降至接近0%，而英语词比率（EN WR）飙升至80%-97%。多语言模型则表现出对资源水平的敏感性：高资源语言（如中文、日语）能较好保持语言保真度（Target WR ≥ 92%），而中低资源语言（如韩语、泰语、乌克兰语）则出现不同程度的目标语言词比率下降和英语词比率上升。
2.  **任务难度加剧跨语言坍缩**：实验表明，增加训练数据的难度（如混合SimpleRL-Zoo数据集）会显著加速“跨语言坍缩”。例如，Qwen-2.5-1.5B模型仅在韩语GSM8K上训练时，能保持较高的韩语词比率（GSM8K上94.0%，MATH500上86.5%）；但当加入更难的数据集后，韩语词比率在GSM8K上暴跌至14.5%，在MATH500上跌至2.1%，同时准确率上升至47.5%和46.7%。
3.  **干预措施的效果**：引入语言一致性奖励能有效维持目标语言的词比率，但会抑制准确率的提升幅度，证实了性能与保真度之间存在持续的权衡。
4.  **领域通用性**：在非数学领域（如使用韩语Global MMLU-Lite进行评估）也观察到了类似模式：使用更难课程训练的模型准确率最高，但韩语词比率也最低（降至23.4%），表明跨语言坍缩现象具有领域通用性。

### Q5: 有什么可以进一步探索的点？

基于论文的讨论，未来研究可从以下几个方向深入探索。首先，论文揭示了在强化学习验证奖励（RLVR）训练中，存在准确性与语言保真度之间的持久权衡。一个关键改进方向是重新设计探索机制，使模型在语义空间保持广泛探索，同时将表层语言形式约束在目标语言上，例如开发能区分语义多样性和语言形式的探索策略。

其次，论文指出跨语言崩溃可能是优化器在当前目标下的“最佳路径”。未来研究可将训练建模为约束或多目标强化学习问题，明确追踪准确性与目标语言一致性之间的帕累托前沿。采用自适应拉格朗日或原始-对偶方法，根据早期预警信号（如目标语言比例下降）动态调整约束强度，从而在不必要牺牲性能的情况下阻断英语捷径。

最后，论文提出需重新思考多语言设置中可解释思维链（CoT）的目的。未来可探索潜在推理与目标语言摘要相结合的折中方案，即模型内部进行推理，但必须生成简洁的、符合目标语言的计划或解释以供人类检查。同时，建立同时奖励任务准确性和目标语言可解释性的评估协议，以明确何时应优先保真度，何时性能提升可证明偏离目标语言是合理的。这些方向不仅针对数学推理，还可扩展至其他领域，以更全面理解语言中心基础模型对推理的影响。

### Q6: 总结一下论文的主要内容

这篇论文研究了在多语言大语言模型中进行强化学习验证奖励训练时出现的“跨语言坍缩”现象。核心问题是，当使用长思维链来激发模型推理能力时，即使使用非英语提示，模型的内部推理过程也会系统地回退到其预训练的主导语言（通常是英语）。这揭示了在追求深度推理性能与保持目标语言保真度之间存在一个未被充分认识的权衡。

论文通过形式化定义该现象并系统研究其成因。方法上，作者在广泛用于引发长思维链推理的数学数据集翻译版本上，使用组相对策略优化训练大语言模型，并同时追踪任务准确性和推理链的语言一致性。

主要结论有三点：首先，在RLVR训练下，随着推理性能提升，思维链会系统性地向预训练主导语言漂移。其次，这种漂移被英语中心先验、长思维链GRPO优化、任务难度和高熵解码共同放大，且该模式不限于数学领域。最后，通过引入语言一致性奖励、解码时控制或使用更平衡的模型主干等干预措施可以缓解坍缩，但会暴露出性能与保真度之间持续的权衡关系。该研究的核心贡献在于揭示了当前以英语为中心的基础模型在塑造多语言推理能力时的内在局限性及其影响。
