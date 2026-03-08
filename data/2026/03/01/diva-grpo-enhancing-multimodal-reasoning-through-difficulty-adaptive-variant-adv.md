---
title: "DIVA-GRPO: Enhancing Multimodal Reasoning through Difficulty-Adaptive Variant Advantage"
authors:
  - "Haowen Gao"
  - "Zhenyu Zhang"
  - "Liang Pang"
  - "Fangda Guo"
  - "Hongjian Dou"
date: "2026-03-01"
arxiv_id: "2603.01106"
arxiv_url: "https://arxiv.org/abs/2603.01106"
pdf_url: "https://arxiv.org/pdf/2603.01106v1"
github_url: "https://github.com/Siaaaaaa1/DIVA-GRPO"
categories:
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Learning & Optimization"
relevance_score: 8.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "New Algorithm"
attributes:
  base_model: "N/A"
  key_technique: "DIVA-GRPO (Difficulty-Adaptive Variant Advantage Group Relative Policy Optimization)"
  primary_benchmark: "N/A"
---

# DIVA-GRPO: Enhancing Multimodal Reasoning through Difficulty-Adaptive Variant Advantage

## 原始摘要

Reinforcement learning (RL) with group relative policy optimization (GRPO) has become a widely adopted approach for enhancing the reasoning capabilities of multimodal large language models (MLLMs). While GRPO enables long-chain reasoning without a critic, it often suffers from sparse rewards on difficult problems and advantage vanishing when group-level rewards are too consistent for overly easy or hard problems. Existing solutions (sample expansion, selective utilization, and indirect reward design) often fail to maintain enough variance in within-group reward distributions to yield clear optimization signals. To address this, we propose DIVA-GRPO, a difficulty-adaptive variant advantage method that adjusts variant difficulty distributions from a global perspective. DIVA-GRPO dynamically assesses problem difficulty, samples variants with appropriate difficulty levels, and calculates advantages across local and global groups using difficulty-weighted and normalized scaling. This alleviates reward sparsity and advantage vanishing while improving training stability. Extensive experiments on six reasoning benchmarks demonstrate that DIVA-GRPO outperforms existing approaches in training efficiency and reasoning performance. Code: https://github.com/Siaaaaaa1/DIVA-GRPO

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态大语言模型在强化学习训练中，特别是采用组相对策略优化方法时，所面临的奖励稀疏和优势消失问题。研究背景是，尽管GRPO方法无需价值函数模型即可进行长链推理，并已广泛应用于增强MLLMs的推理能力，但其固有缺陷限制了训练效率与最终性能。现有方法存在明显不足：样本扩展策略缺乏对问题难度的感知，可能加剧优势分布的稀疏性；选择性样本利用会减少数据多样性，可能使模型难以接触复杂问题；间接奖励设计则可能与最终任务目标不完全对齐，导致模型优化方向出现偏差。这些方法都未能从根本上应对一个核心动态挑战：随着模型训练推进，其整体解决问题的能力提升，导致数据集中问题的相对难度持续下降，进而使得组内奖励差异变小、优势信号减弱甚至消失，最终造成训练效率递减和梯度不稳定。因此，本文要解决的核心问题是，如何设计一种能够动态适应问题难度变化、并据此调整训练数据分布与优势计算的方法，以在GRPO框架下持续提供清晰有效的优化信号，从而稳定、高效地提升多模态模型的复杂推理能力。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕强化学习在多模态大语言模型推理优化中的应用，可分为方法类和应用类。

在方法类中，相关工作主要包括基于群体相对策略优化的强化学习框架及其改进。GRPO通过组内奖励标准化计算相对优势，避免了依赖评论家模型，但易受奖励稀疏和优势消失问题困扰。现有解决方案有三类：一是样本增强与扩展，通过增加问题规模来丰富数据，但未调整内在难度；二是样本选择与利用，提升训练效率但可能丢失困难样本，降低多样性；三是间接奖励设计，通过额外监督信号丰富奖励，但可能引入优化偏差。这些方法均未能稳定维持组内奖励分布的方差，导致优化信号不清晰。

在应用类中，研究聚焦于多模态推理任务的性能提升，包括数学解题、视觉推理等基准测试。现有方法通常在特定难度范围内有效，但难以适应问题难度的动态变化。

本文提出的DIVA-GRPO与上述工作的核心区别在于：从全局视角动态评估问题难度，自适应调整变体难度分布，并通过难度加权和归一化缩放计算局部与全局群体优势。这直接针对奖励方差稳定性问题，避免了现有方法在样本处理或奖励设计上的局限性，从而在训练效率和推理性能上实现更优平衡。

### Q3: 论文如何解决这个问题？

论文通过提出DIVA-GRPO方法来解决GRPO在强化学习训练中面临的奖励稀疏性和优势消失问题。其核心是动态评估问题难度、自适应生成不同难度的语义一致变体，并通过难度加权的优势计算来优化训练信号。

整体框架包含三个主要模块：首先是**动态难度评估机制**，基于历史rollout的正确率动态更新每个问题的难度系数，公式为 \( D^{new} = \operatorname{clip}(D^{old} + \eta \cdot (0.5 - \alpha), D_{\min}, D_{\max}) \)，确保难度随模型能力演变而调整。

其次是**自适应变体生成策略**，根据评估的难度系数生成不同难度的变体：对于简单问题（\( D_q < D_{\text{mid}} \)），通过对文本和图像施加扰动（如重述、旋转、噪声）来增加多样性；对于中等难度问题（\( D_q \approx D_{\text{mid}} \)），生成语义等效的文本变体以提升泛化能力；对于困难问题（\( D_q > D_{\text{mid}} \)），则引入由闭源模型生成的中间推理步骤作为提示，以提供学习支架。

最后是**难度自适应的优势计算与平衡策略**。该方法同时计算局部优势（基于单个问题）和全局优势（基于问题及其变体集合）。为解决局部与全局优势量级不平衡的问题，采用批级别的z-score归一化。随后引入**难度加权缩放**：对于每个响应 \( y_i \)，其最终优势计算为 \( \hat{A}(y_i \mid q^{(i)}) = \exp(k \cdot (D_q^{(i)} - \bar{D}_q) \cdot \operatorname{sgn}(\tilde{A}(y_i))) \cdot \tilde{A}(y_i) \)。该设计使得对于比组平均更难的问题变体，正确响应的优势被放大；对于更简单的变体，错误响应的惩罚加重，从而引导模型聚焦于具有适当挑战性的样本。此外，论文还提出了**基于奖励范围的重新缩放**，以缓解因奖励分布范围过小导致的优化信号失真问题。

创新点在于：1) 将问题难度定义为动态、与模型能力相关的属性，而非静态固有属性；2) 根据难度系数差异化生成变体，实现了探索与利用的平衡；3) 通过难度加权的优势计算，使优化信号与问题挑战性对齐，有效缓解了奖励稀疏和优势消失，提升了训练稳定性和效率。

### Q4: 论文做了哪些实验？

该论文在六个多模态推理基准测试（MathVista、MathVerse、MathVision、OlympiadBench、WeMath和MMK12-test）上进行了广泛的实验。实验设置以Qwen2.5-VL-7B-Instruct为骨干模型，使用AdamW优化器（学习率10^{-6}）和EasyR1框架进行训练。对比方法涵盖三类基线：闭源专有MLLM（如GPT-4o、Claude 3.7-Sonnet）、开源基础MLLM（如Qwen2.5-VL-32B、InternVL2.5-VL-78B）以及开源微调MLLM。

主要结果显示，DIVA-GRPO在7B规模模型上实现了最先进的性能。在五个主要基准测试上的平均得分为54.58，相较于其骨干模型Qwen2.5-VL-7B平均准确率提升了8.23个百分点。在MathVista、MathVerse和WeMath等数据集上，其性能与更大的Qwen2.5-VL-72B模型相当，并显著超越了多个开源基础模型和专有系统。训练动态分析表明，该方法能维持稳定优化，在训练后期即使面对高难度样本也能保持信息丰富的优势信号，避免了奖励稀疏和优势消失问题。

消融实验评估了其三个核心组件（自适应变体生成、难度加权、基于奖励范围的优势重缩放）的必要性。移除任一组件均导致性能下降，验证了完整设计的有效性。此外，效率分析表明，该方法仅导致每步训练时间轻微增加，主要源于生成长度的增加，整体训练效率优异。

### Q5: 有什么可以进一步探索的点？

该论文提出的DIVA-GRPO方法虽然有效缓解了GRPO中的奖励稀疏和优势消失问题，但仍存在一些局限性。首先，其难度评估机制依赖于预定义的全局视角，可能无法充分适应动态变化的问题分布，尤其在面对开放域或高度异构的多模态任务时，难度标定可能失准。其次，方法主要针对推理任务进行优化，对于需要创造性生成或复杂决策的跨模态任务，其优势计算方式可能仍需调整。

未来研究方向可以从以下几个角度展开：一是引入更细粒度的自适应难度评估，例如结合在线学习或元学习动态调整难度权重，以提升对未知任务类型的泛化能力。二是探索多模态奖励信号的深度融合，当前方法可能过于依赖语言模态的推理结果，未来可整合视觉、音频等模态的独立奖励，形成更鲁棒的优势估计。三是将难度自适应机制扩展到多智能体协作场景，研究如何在群体决策中平衡个体难度与整体奖励分布。此外，可考虑结合课程学习思想，设计从易到难的渐进式训练策略，进一步提升模型在极端困难样本上的表现。

### Q6: 总结一下论文的主要内容

该论文针对多模态大语言模型在强化学习训练中面临的问题，提出了DIVA-GRPO方法。现有基于组相对策略优化的方法虽无需价值函数，但在处理困难问题时易出现奖励稀疏，而在问题过于简单或困难时又因组内奖励差异过小导致优势信号消失。传统解决方案难以维持足够的组内奖励方差以提供清晰的优化方向。

为此，作者提出了一种难度自适应的变体优势方法。该方法从全局视角动态评估问题难度，并据此采样具有合适难度水平的变体样本。通过结合难度加权和归一化缩放，在局部和全局组别间计算优势值，从而缓解奖励稀疏与优势消失问题，同时提升训练稳定性。

实验部分在六个推理基准上验证了方法的有效性。结果表明，DIVA-GRPO在训练效率和推理性能上均优于现有方法，核心贡献在于通过难度自适应机制优化了强化学习的信号质量，显著增强了多模态模型的复杂推理能力。
