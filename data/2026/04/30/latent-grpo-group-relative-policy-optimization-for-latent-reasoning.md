---
title: "Latent-GRPO: Group Relative Policy Optimization for Latent Reasoning"
authors:
  - "Jingcheng Deng"
  - "Zihao Wei"
  - "Liang Pang"
  - "Junhong Wu"
  - "Shicheng Xu"
  - "Zenghao Duan"
  - "Huawei Shen"
date: "2026-04-30"
arxiv_id: "2604.27998"
arxiv_url: "https://arxiv.org/abs/2604.27998"
pdf_url: "https://arxiv.org/pdf/2604.27998v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "LLM Agent推理"
  - "强化学习"
  - "潜伏推理"
  - "GRPO"
  - "思维链压缩"
relevance_score: 8
---

# Latent-GRPO: Group Relative Policy Optimization for Latent Reasoning

## 原始摘要

Latent reasoning offers a more efficient alternative to explicit reasoning by compressing intermediate reasoning into continuous representations and substantially shortening reasoning chains. However, existing latent reasoning methods mainly focus on supervised learning, and reinforcement learning in latent space remains highly unstable. We study this problem through the lens of Group Relative Policy Optimization (GRPO), and show that directly adapting GRPO to latent reasoning is fundamentally non-trivial: latent reasoning changes both the probability density and the sampling mechanism, causing three coupled bottlenecks: absence of intrinsic latent manifolds, where unconstrained exploration pushes rollouts off the valid latent manifold; exploration-optimization misalignment, where trajectory-level rewards can induce incorrect token-level updates; and latent mixture non-closure, where jointly reinforcing multiple correct latent paths can produce an invalid averaged state. To address them, we propose \textbf{Latent-GRPO}, which combines invalid-sample advantage masking, one-sided noise sampling, and optimal correct-path first-token selection. Across four low-difficulty benchmarks (e.g., GSM8K-Aug) and four high-difficulty benchmarks (e.g., AIME), Latent-GRPO improves over its latent initialization by 7.86 Pass@1 points on low-difficulty tasks and surpasses explicit GRPO by 4.27 points on high-difficulty tasks while using 3--4$\times$ shorter reasoning chains. It also achieves stronger pass@$k$ performance under Gumbel sampling. These results establish Latent-GRPO as an effective approach for stable and efficient latent reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在潜在推理（latent reasoning）中应用强化学习（RL）时面临的核心稳定性和有效性问题。潜在推理通过将中间推理步骤压缩为连续表示，相比显式推理（如思维链CoT）能显著缩短推理链、降低计算冗余和延迟。然而，现有潜在推理方法主要聚焦于监督微调（SFT），而将强化学习扩展到潜在空间时存在根本性挑战。直接采用主流的组相对策略优化（GRPO）算法会遭遇三个耦合瓶颈：（1）缺乏内在潜在流形，未约束的探索会使模型产出偏离有效流形的样本；（2）探索-优化不匹配，轨迹级奖励可能错误地导致符号级概率更新方向颠倒；（3）潜在混合非封闭性，即对多条正确潜在路径的联合强化可能产生无效的均值状态。因此，本文旨在设计一种稳定的强化学习框架，使潜在推理既能保持压缩效率，又能通过RL训练提升性能，甚至超越显式GRPO，同时避免上述瓶颈导致的训练崩溃或次优解问题。

### Q2: 有哪些相关研究？

相关研究主要分为三类。首先是**显式推理方法**，以思维链（CoT）和GRPO为代表，通过生成离散推理序列提升复杂推理能力。本文指出这类方法存在冗长、延迟高的缺点，而Latent-GRPO通过将推理压缩为连续表征，以更短的推理链实现了更优或相当的性能。其次是**无训练的隐式推理方法**，如Soft Thinking及其Gumbel-Softmax变体、并行测试时扩展方法。它们仅修改推理过程而不更新模型参数，探索性强但性能提升有限，且未像本文那样在训练中结合强化学习以稳定优化。最后是**基于训练的隐式推理方法**，如Coconut、CODI、CoLaR、Latent-SFT和SofT-GRPO。这些方法通过学习连续表征进行推理，部分已涉及强化学习。本文的核心区别在于：直接以Latent-SFT模型为起点，系统分析了GRPO直接应用于隐式推理的三大瓶颈（潜在流形缺失、探索-优化错位、潜在混合非封闭性），并针对性提出Latent-GRPO方案（包括无效样本优势遮掩、单侧噪声采样和最优正确路径首令牌选择），从而在极短推理链下同时提升任务性能和推理效率。

### Q3: 论文如何解决这个问题？

Latent-GRPO通过三项关键技术系统性解决了连续潜在推理中的三个核心瓶颈。整体框架建立在Soft-GRPO数学基础上，以Latent-SFT初始化的策略模型为起点，确保RL探索前已存在有效的潜在流形。

**核心方法**：
1. **无效样本优势掩码**：针对无内禀流形问题，将未在最大长度内终止的轨迹标记为无效，仅基于有效轨迹子集计算组基线μ_R和σ_R，无效轨迹的优势设为0。这防止脱流形轨迹污染组统计量，确保探索始终限制在有效潜在推理区域。

2. **单侧噪声采样**：解决探索-优化错位。对Gumbel噪声进行裁剪平移变换ξ_i^+ = clip(ξ_i, -a, b) + a + δ，保证所有潜在分量的扰动边距恒为正。结合条件直通估计器，在多次PPO更新中维持正边距，确保梯度方向与优势信号一致。

3. **最优正确路径首Token选择**：针对潜在混合非封闭性，在首步(t=1)从多个正确轨迹中，依据平均代理对数概率选择最优路径，仅保留其首隐Token的梯度更新。后续步则允许多路径并行优化，避免确定性连续动作的平均化陷阱。

**创新点**：通过优势掩码、定向噪声注入和选择性路径保留的协同设计，使得强化学习首次在潜在空间实现稳定训练。实验表明，该方法在低难度任务上比潜在初始化提升7.86% Pass@1，在高难度任务上超越显式GRPO 4.27%，且推理链缩短3-4倍。

### Q4: 论文做了哪些实验？

论文在低难度和高难度两个实验体系下评估了Latent-GRPO的性能。低难度任务使用GSM8K-Aug、GSM-Hard、SVAMP、MultiArith基准测试，基础模型为LLaMA-3.2-1B-Instruct。高难度任务使用Math500、AIME24、AIME25、GPQA，基础模型为Qwen2.5-MATH-7B。对比方法包括显式推理的SFT和GRPO，以及隐式推理的Latent-SFT和Soft-GRPO。

主要结果：在低难度任务上，Latent-GRPO平均Pass@1达58.32，超过显式GRPO的57.98，推理长度仅为GRPO的1/4.44；在隐式推理中，Latent-GRPO相比Latent-SFT提升7.86个点，远超Soft-GRPO的+0.27。在高难度任务上，Latent-GRPO平均Pass@1达41.72，比显式GRPO高4.27个点，推理长度仅为GRPO的1/3.31；相比Latent-SFT提升14.77个点，而Soft-GRPO出现负增长(-2.57)。在Gumbel采样评估pass@k时，Latent-GRPO在AIME24上pass@64达50.0，远超GRPO的23.3。消融实验表明，One-sided Noise Sampling是稳定训练的关键，而First Token Selection在高难度任务上提供额外增益。

### Q5: 有什么可以进一步探索的点？

根据论文内容，未来可以进一步探索以下几个方向：首先，当前Latent-GRPO主要解决了低维连续潜空间中的RL稳定性问题，但如何将该方法推广到更高维或更复杂的潜空间（如大规模语言模型的深层表示）仍然是一个开放挑战。其次，论文中的三组技术方案（无效样本优势掩码、单侧噪声采样、最优正确路径首token选择）虽然有效，但可能并非最优组合，未来可以探索更统一的优化框架或自适应调节策略。第三，当前方法在困难任务上表现优于显式GRPO，但在低难度任务上的提升幅度有限，暗示可能在简单任务中存在过约束问题。从我的角度看，一个很有潜力的方向是将潜推理与显式推理相结合，构建混合推理范式，让模型自主选择何时使用潜推理、何时使用显式推理。此外，探索更高效的潜空间正则化方法，如流形约束或几何先验，可能进一步提升潜推理的稳定性和泛化能力。

### Q6: 总结一下论文的主要内容

该论文研究如何在潜在空间进行强化学习以提升推理效率。现有显式推理方法生成冗长中间步骤，而潜在推理通过连续表示压缩中间过程，但现有方法主要依赖监督学习，在潜在空间进行强化学习极不稳定。论文发现直接应用GRPO到潜在推理面临三个瓶颈：缺乏内在潜在流形导致探索偏离有效空间；轨迹级奖励与token级更新错配；多条正确潜在路径的联合强化可能产生无效平均状态。为解决这些问题，作者提出Latent-GRPO，包含无效样本优势掩码、单边噪声采样和最优正确路径首词选择。在四个低难度基准（如GSM8K-Aug）和四个高难度基准（如AIME）上，Latent-GRPO在低难度任务上相比其潜在初始模型提升7.86个Pass@1点，在高难度任务上超越显式GRPO 4.27点，同时推理链缩短3-4倍。在Gumbel采样下也实现了更强的pass@k性能。这些结果确立了Latent-GRPO作为稳定高效潜在推理方法的有效性。
