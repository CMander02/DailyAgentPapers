---
title: "Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration"
authors:
  - "Zhicheng Yang"
  - "Zhijiang Guo"
  - "Yinya Huang"
  - "Yongxin Wang"
  - "Dongchun Xie"
  - "Hanhui Li"
  - "Yiwei Wang"
  - "Xiaodan Liang"
  - "Jing Tang"
date: "2025-08-19"
arxiv_id: "2508.13755"
arxiv_url: "https://arxiv.org/abs/2508.13755"
pdf_url: "https://arxiv.org/pdf/2508.13755v6"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Agentic Reinforcement Learning"
  - "LLM Reasoning"
  - "Reinforcement Learning"
  - "Algorithm Analysis"
  - "Exploration Strategy"
  - "Training Optimization"
  - "Reasoning Capabilities"
relevance_score: 8.5
---

# Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration

## 原始摘要

Reinforcement Learning with Verifiable Reward (RLVR) has emerged as a powerful paradigm for unlocking reasoning capabilities in large language models, yet its full potential is hindered by two under-explored dimensions: Depth-the hardest problem a model can sample; Breadth-the number of instances consumed in a single iteration. We dissect the popular GRPO algorithm and reveal a systematic bias: the cumulative-advantage disproportionately weights samples with medium accuracy, while down-weighting the low-accuracy instances that are crucial for pushing reasoning boundaries. To rectify the depth neglect, we introduce Difficulty Adaptive Rollout Sampling (DARS), which re-weights hard problems through targeted multi-stage rollouts, thereby increasing the number of positive rollouts for hard problems. Empirically, naively enlarging rollout size only accelerates convergence and even hurts Pass@K. Our DARS, in contrast, delivers consistent Pass@K gains without extra inference cost at convergence. Just as we adaptively expanded the depth of exploration, we now ask whether aggressively scaling the breadth of training data can further amplify reasoning gains. To this end, we intensely scale batch size and replace PPO's mini-batch iterations with full-batch updates over multiple epochs. Increasing breadth significantly enhances Pass@1 performance. Large-breadth training sustains high token-level entropy, indicating continued exploration and reduced gradient noise. We further present DARS-B, which augments DARS with large breadth, and demonstrate simultaneous gains in Pass@K and Pass@1. The results confirm that breadth and adaptive exploration across depth operate as orthogonal dimensions in RLVR, which are key to unleashing the reasoning power of RLVR.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决强化学习与可验证奖励（RLVR）范式中，探索的“深度”与“广度”两个维度未被充分探索和协同优化的问题，以更有效地解锁大型语言模型（LLMs）的复杂推理能力。

研究背景是，以OpenAI-o1等为代表的推理专用LLMs在数学和编程等复杂任务上取得了突破，其核心驱动力是RLVR。RLVR利用可自动验证的正确性（如数学答案或代码测试）作为奖励，无需人工标注，被视为实现LLM自我进化的有前景路径。然而，现有RLVR框架（如GRPO及其变体）存在明显不足。

现有方法的不足主要体现在两方面：一是**深度探索不足**。论文分析发现，GRPO等方法的“累积优势”计算存在系统性偏差，会不成比例地关注中等准确率的样本，而低估了低准确率、高难度样本的重要性。这些困难样本恰恰是推动模型解决更复杂问题、提升推理边界的关键。这种偏差限制了模型能学习的“最深”问题难度，从而制约了Pass@K（考虑多个输出）性能。二是**广度探索未被充分重视**。即单次训练迭代中消耗的实例数量（批次大小）及其对模型持续探索能力和Pass@1（单次输出准确率）性能的影响未被系统研究。

因此，本文要解决的核心问题是：**如何通过分别纠正深度探索的偏差并系统性地扩展训练广度，并最终将两者协同，以同时显著提升RLVR在Pass@1和Pass@K上的性能**。具体而言，论文提出了难度自适应采样（DARS）来重新分配计算资源，通过多阶段采样增加对困难问题的正反馈，以纠正深度偏差、提升Pass@K。同时，论文探究了大幅增加批次大小（广度）并采用全批次多轮更新的方法，发现其能有效提升Pass@1并维持探索活力。最终，论文将两者结合为DARS-B，证明了深度与广度在RLVR中是正交且互补的维度，协同优化能同时提升两项关键指标，从而更充分地释放RLVR提升LLM推理能力的潜力。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕强化学习在大型语言模型推理能力提升中的应用展开，可分为方法类和应用验证类。

在方法类研究中，早期工作基于奖励模型进行偏好优化，随后**直接偏好优化（DPO）** 通过利用成对偏好简化了训练流程。**基于可验证奖励的强化学习（RLVR）** 范式在此基础上发展起来，显著推动了数学和代码推理基准的进步，代表性工作包括OpenAI的o1和DeepSeek-R1的零强化学习突破。在算法层面，**GRPO** 作为当前主流算法，通过引入组相对优势扩展了PPO，并启发了DAPO、VAPO和Dr. GRPO等一系列变体。然而，本文指出GRPO及其变体存在系统性缺陷，即低估困难问题的重要性，从而损害了Pass@K指标。本文提出的**难度自适应采样（DARS）** 正是为了纠正这一“深度忽视”偏差，通过针对性多阶段重采样来重新加权困难问题。

在应用验证类研究中，一系列**大型推理模型**（如Kimi 1.5、Gemini-Think、QwQ）的成功进一步验证了RLVR范式的有效性。本文的工作与上述研究紧密相关，其核心区别在于：首次系统性地剖析并解决了RLVR中“深度”（探索难题难度）与“广度”（单次迭代数据量）两个未被充分探索的维度之间的协同关系。本文不仅提出了改进深度探索的DARS方法，还创新性地研究了大规模扩展训练数据“广度”（即大批次训练）的影响，并最终将二者结合为DARS-B，证明了深度与广度是RLVR中两个正交且互补的维度，共同释放模型的推理潜力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为DARS-B的集成框架来解决RLVR中深度（最难问题的探索）和广度（单次迭代消耗的实例数量）两个维度未被充分利用的问题。其核心方法是分别针对深度和广度进行优化，然后将两者协同，以实现推理能力的全面提升。

在深度优化方面，论文提出了**难度自适应轨迹采样（DARS）** 方法，以纠正GRPO算法中累积优势对中等难度样本的偏好偏差。DARS包含两个阶段：1）**预采样难度估计**：对批次中的每个问题 \(q_j\) 进行少量（\(N^{pre}\) 次）初始采样，根据轨迹的二元奖励（正确/错误）计算经验准确率 \(\hat{a}_j\)，并定义难度分数 \(x_j = 1 - \hat{a}_j\)。2）**多阶段轨迹重平衡**：根据难度分数，动态地为每个问题分配额外的采样轨迹 \(\Delta n_j\)，目标是使每个问题的有效累积优势成为其难度的增函数。论文设计了两种重平衡策略：**平等对待（ET）** 将所有低准确率（\(\hat{a}_j < 0.5\)）问题的累积优势提升到中等难度（\(\hat{a}_j=0.5\)）问题的水平；**难度加权（HW）** 则施加一个单调递增的权重，为更低准确率的问题分配更多轨迹。这确保了模型在训练中能获得更多关于难题的正反馈，从而突破推理边界。

在广度优化方面，论文发现简单地增加批次大小（Breadth-Naive）能提升Pass@1，但会损害Pass@K。为了同时利用广度优势并兼容DARS的动态采样，论文进行了关键的**架构设计调整**：**用多轮次的全批次梯度下降取代了PPO风格的小批次更新**。这一调整解决了DARS动态分配导致批次大小不固定、与小批次更新不兼容的问题。全批次训练消除了小批次梯度噪声，并维持了较高的词元级熵，意味着持续的探索和隐式正则化，防止过早收敛。

最终，论文将深度优化（DARS）与广度最大化（全批次训练）结合，提出了**DARS-B** 集成方法。其创新点在于揭示了深度（自适应探索）和广度（数据规模）是RLVR中两个正交的优化维度，并设计了一个统一的框架来协同它们：DARS通过重采样聚焦于难题，优化了探索的深度，主要提升Pass@K；而大广度训练通过更稳定、探索性更强的全批次优化，主要提升Pass@1。实验结果表明，DARS-B在多个基准测试上同时实现了Pass@1和Pass@K的显著增益，验证了这种协同效应的有效性。

### Q4: 论文做了哪些实验？

论文在五个数学推理基准测试（MATH-500、OlympiadBench、MinvervaMath、AIME24和AMC23）上进行了实验，使用OpenR1-45K作为训练数据。实验设置包括与多个基线方法对比：RLVR-baseline（GRPO，rollout size=8，batch size=128）、Depth-Naive（仅将rollout size增至32）、Breadth-Naive（仅将batch size增至3072）、DARS-ET/HW（提出的自适应深度探索算法，batch size=128，N_max=32）以及DARS-ET/HW-Breadth（结合深度与广度的协同算法，batch size=3072，N_max=32）。所有方法均设置PPO mini-steps为2。

主要结果如下：在Pass@1（Avg@128）指标上，Breadth-Naive相比GRPO基线和Depth-Naive有显著提升，在AIME24、MATH500和Olympiad任务上平均提高1.9–3.7个百分点。DARS-Breadth（深度与广度协同）进一步扩大了优势，获得了最高的Pass@1性能，同时匹配或超越了最佳的Pass@128（即上限能力）分数。例如，在Llama-3.1-8B模型上，DARS-ET-Breadth的Avg@128达到22.0%，Pass@128达到67.2%，均优于其他方法。关键数据指标包括：DARS算法大幅降低了平均每个提示的rollout数量（例如在Qwen2.5-Math-7B上，DARS-ET仅需12.8次，比Naive的32次下降60%），表明其更高的训练效率。此外，DARS-HW调度在保持Pass@1与ET调度持平的同时， consistently 产生了更优的Pass@K曲线。实验还证实深度（通过DARS自适应探索）和广度（扩大批次大小）是互补的维度，协同作用能同时提升Pass@1和Pass@K性能。

### Q5: 有什么可以进一步探索的点？

该论文揭示了深度（难题采样）与广度（单次迭代数据量）在RLVR中的协同作用，但仍有多个方向值得深入探索。首先，论文主要基于GRPO算法分析，未来可研究其他RL算法（如PPO、A3C）中是否存在类似的深度-广度权衡，以及DARS方法在不同算法架构下的泛化能力。其次，当前方法依赖人工定义的难度阈值或采样策略，未来可探索自适应难度评估机制，例如通过模型自身的不确定性或学习动态来自动识别“硬问题”。此外，论文未充分探讨计算效率与性能的平衡——大规模广度训练虽提升性能，但计算成本高昂，未来需研究更高效的分布式训练或梯度压缩技术。最后，研究可扩展到多模态推理或跨领域任务，验证深度-广度协同在复杂场景中的普适性。这些方向有望进一步释放LLM在推理任务中的潜力。

### Q6: 总结一下论文的主要内容

本文针对强化学习与可验证奖励（RLVR）在提升大语言模型推理能力时存在的深度（模型能采样的最难问题）和广度（单次迭代消耗的实例数）两个未充分探索的维度进行了研究。核心问题是发现流行的GRPO算法存在系统性偏差，其累积优势函数不成比例地加权中等准确率的样本，而低估了对推动推理边界至关重要的低准确率（困难）实例，从而限制了Pass@K性能。

为纠正此“深度忽视”问题，论文提出了难度自适应采样（DARS）方法，通过有针对性的多阶段rollout对困难问题进行重新加权，从而增加其正样本数量。实验表明，单纯增加rollout规模仅加速收敛甚至损害Pass@K，而DARS能在不增加收敛时推理成本的情况下持续提升Pass@K。同时，论文探究了“广度”维度，通过大幅扩展批次规模并以多轮全批次更新替代PPO的小批次迭代，显著提升了Pass@1性能，并保持了较高的令牌级熵，表明持续探索和梯度噪声降低。

最终，论文将DARS与广度扩展结合为DARS-B框架，实现了Pass@1和Pass@K的同时提升。主要结论是：深度上的自适应探索与训练数据的广度扩展是RLVR中两个正交且协同的维度，共同释放其推理潜力。
