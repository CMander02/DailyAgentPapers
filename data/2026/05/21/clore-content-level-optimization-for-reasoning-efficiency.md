---
title: "CLORE: Content-Level Optimization for Reasoning Efficiency"
authors:
  - "Yuyang Wu"
  - "Qiyao Xue"
  - "Guanxing Lu"
  - "Weichen Liu"
  - "Zihan Wang"
  - "Manling Li"
  - "Olexandr Isayev"
date: "2026-05-21"
arxiv_id: "2605.22211"
arxiv_url: "https://arxiv.org/abs/2605.22211"
pdf_url: "https://arxiv.org/pdf/2605.22211v1"
categories:
  - "cs.AI"
tags:
  - "LLM推理效率优化"
  - "内容级监督"
  - "RL后训练"
  - "思维链压缩"
  - "DPO优化"
  - "数学推理Agent"
  - "深度强化学习"
relevance_score: 8.5
---

# CLORE: Content-Level Optimization for Reasoning Efficiency

## 原始摘要

Reinforcement learning post-training has improved the reasoning ability of large language models, but often produces unnecessarily long, repetitive, or semantically opaque reasoning traces. Existing efficient reasoning methods mainly regulate response length through explicit budgets or length-aware rewards, leaving intermediate reasoning content weakly supervised. We propose CLORE, a content-level optimization framework that improves reasoning efficiency by editing correct on-policy rollouts. CLORE uses an external augmentation model to delete repetitive segments, illegible or task-irrelevant content, and superfluous reasoning after the solution is established, while preserving the final answer. The resulting augmented--original pairs are optimized with an auxiliary reference-free DPO objective alongside standard policy-gradient training. By restricting augmentation to correct trajectories and performing local deletion, CLORE keeps edited rollouts close to the policy distribution and mitigates off-policy mismatch. Experiments on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-Math-7B across five mathematical reasoning benchmarks show that CLORE improves the accuracy--efficiency trade-off and remains compatible with GRPO, DAPO, Training Efficient, and ThinkPrune. Content-level analyses further show that CLORE reduces repetitive reasoning, illegible content, and post-answer exploration, supporting content-level supervision as a complementary direction to length-level control.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型在推理过程中产生低效长链思维的问题。研究背景是：通过强化学习后训练，模型虽然提升了推理能力，但常常生成长度过大、包含重复、语义模糊或无关内容的推理轨迹。

现有方法的不足在于：当前提高推理效率的方法主要依赖序列级别的长度控制，如通过显式长度预算或基于长度的奖励函数来约束输出长度。这些方法只能粗粒度地控制整体长度，无法对中间推理内容进行精细监督，因而无法识别和剔除低质量推理片段。

本文提出的核心问题是：如何实现内容级别的推理优化，直接监督和改善推理过程的质量，而非仅依赖长度控制。CLORE框架通过编辑正确策略轨迹，删除重复、不可读、任务无关或多余的推理内容，同时保留最终答案，并利用DPO偏好优化在策略梯度训练中提升推理质量。该方法旨在改善准确性与效率的权衡，并与现有强化学习方法兼容。

### Q2: 有哪些相关研究？

1. **推理效率优化方法**：当前主流方法通过显式长度预算或长度感知奖励来约束响应长度，例如预定义/自适应长度预算训练、基于参考长度或相对比较的长度感知奖励，以及使用最短正确推理轨迹作为锚点的多采样策略。本文指出这些方法仅控制长度而非中间推理质量，导致低效用、难理解或无关内容未被有效惩罚。CLORE 提出内容级优化，通过对正确轨迹进行局部删除（如重复片段、无关内容），直接监督推理内容质量。

2. **过度思考与可读性研究**：相关工作揭示了长链推理模型存在“过度思考”现象（产生冗余推理）和“可读性”问题（中间步骤语义模糊或不可解释）。已有研究表明模型可能在获得正确答案后仍继续探索无用步骤。CLORE 通过显式删除“答案确定后的冗余推理”和“不可读内容”，直接解决这两个问题，与仅关注长度控制的现有方法形成互补。

3. **与强化学习微调方法的兼容性**：本文实验证明 CLORE 可与 GRPO、DAPO、Training Efficient、ThinkPrune 等标准策略梯度方法兼容。与这些方法仅优化最终答案正确性不同，CLORE 在策略梯度训练基础上引入辅助参考无关的 DPO 目标，对推理内容进行局部编辑，从而保持编辑轨迹接近策略分布，缓解离策略不匹配问题。

### Q3: 论文如何解决这个问题？

CLORE提出了一种内容级优化框架，核心方法是通过编辑正确的策略轨线来提升推理效率。整体框架在标准策略梯度强化学习训练基础上，引入基于增强轨线的离线感知监督。

主要模块包括：(1) **轨线生成**：从当前策略πθ采样N条推理轨线，筛选出回答正确的子集T^cor(x)。仅对正确轨线进行增强，因为其低质量推理内容更少，所需编辑更少，从而减轻离策略分布偏移。(2) **推理增强**：使用外部增强模型E删除三类低质量内容——重复推理片段、晦涩或任务无关内容、以及确定答案后的多余探索，同时保留最终答案。增强后的轨线必须通过正确性一致性检查（R(x,τ̃)≥R(x,τ)），确保偏好反映推理质量提升而非偶然的正确性退化。(3) **在线策略偏好学习**：对每个(τ, τ̃)对采用无参考策略的DPO风格目标函数优化，公式为L_DPO=-log σ(β[log πθ(τ|x)-log πθ(τ̃|x)])。由于τ̃是通过局部删除τ中低质量片段构建的，保持了与原始轨线的结构和分布接近性，因此无需额外参考模型即可稳定优化。(4) **与策略梯度方法兼容**：最终训练目标为L=L_PG+λL_DPO，其中L_PG可实例化为PPO、REINFORCE、GRPO等变体，不改变骨干优化器但添加了辅助偏好监督项。同时与长度级高效推理方法互补，可叠加为L=L_PG+L_len+λL_DPO。

**创新点**在于从内容级别而非长度级别优化推理效率，通过局部删除操作保持编辑轨线与策略分布接近，缓解离策略问题，并通过内容级监督补充长度级控制的盲区。

### Q4: 论文做了哪些实验？

论文在数学推理基准上进行了全面评估。实验采用DeepSeek-R1-Distill-Qwen-7B和Qwen2.5-Math-7B作为基础推理模型，使用Qwen3-4B-Instruct作为增强模型，在DAPO-Math-17K数据集上微调。评估在五个基准上进行：OlympiadBench、Minerva、MATH500、AMC2023和AIME2025。对比方法包括GRPO、DAPO、Training Efficient和ThinkPrune等基于长度控制的优化方法，以及各自加上CLORE的变体。

主要结果：CLORE在所有基准上一致提升了准确率-效率（AE）分数。在DeepSeek-R1-Distill-Qwen-7B上，将CLORE应用于各基线平均提升AE约0.4，输出长度减少20-30%；在Qwen2.5-Math-7B上提升更显著，如GRPO+CLORE在Minerva上AE提升超过6点，长度减少30-50%。最佳组合因模型而异：DeepSeek-R1-Distill-Qwen-7B上DAPO+CLORE达到最佳AE（如OlympiadBench上AE=1.21），Qwen2.5-Math-7B上Training Efficient+CLORE实现最短输出和最佳AE（如Minerva上AE=16.16）。消融实验表明适中的DPO权重（0.05）提供最佳准确率-长度权衡，较小的增强模型（Qwen3-1.7B）仍有效。

内容分析进一步显示CLORE能减少重复推理、后续推理和难以理解的推理内容，而不仅仅是压缩长度。

### Q5: 有什么可以进一步探索的点？

这篇论文提出的CLORE框架在内容层面优化推理效率上取得了进展，但仍存在若干可探索的局限与方向。首先，CLORE当前依赖外部模型进行论文中定义的“高效编辑”，即删除重复、无关内容，但该模型本身可能引入新偏差或编辑质量不稳定，未来可探索自适应编辑策略或端到端学习编辑规则。其次，框架仅在正确轨迹上做局部删除，未考虑修正错误推理步骤或添加必要的中间推理，这限制了内容质量的全面提升，未来可扩展至混合编辑（如合并、重写）。第三，CLORE与现有长度控制方法的结合仍较浅层，可设计动态平衡内容质量与长度预算的联合优化目标。最后，当前评估限于数学推理，未来应验证其在科学、法律等更依赖链条推理的领域中的泛化性，并分析编辑操作对模型可解释性的影响。

### Q6: 总结一下论文的主要内容

CLORE提出了一种内容级优化框架，用于提升大型语言模型的推理效率。现有方法主要依赖响应长度控制，但忽略了推理内容的质量，导致模型产生冗长、重复或语义不清的推理链。CLORE通过编辑正确的策略轨迹，利用外部增广模型删除重复片段、不可读或任务无关内容以及解决方案确定后的多余推理，同时保留最终答案。之后，采用无参考的DPO目标对增广-原始轨迹对进行优化，并结合标准策略梯度训练。通过限制增广于正确轨迹并进行局部删除，CLORE保持编辑结果接近策略分布，减轻离策略问题。在DeepSeek-R1-Distill-Qwen-7B和Qwen2.5-Math-7B上的五个数学推理基准测试中，CLORE显著提升了准确率与效率的平衡，并与GRPO、DAPO等方法兼容。内容级分析表明，CLORE有效减少了重复推理、难以理解的内容和解答后的探索，证明了内容级监督是长度级控制的重要补充方向。
