---
title: "Intrinsic Selection and Particle Resampling for Inference-Time Scaling Beyond Domain Verifiability"
authors:
  - "Giorgio Giannone"
  - "Mustafa Eyceoz"
  - "Shabana Baig"
  - "Shivchander Sudalairaj"
  - "Anna C. Doris"
  - "Faez Ahmed"
  - "Akash Srivastava"
  - "Kai Xu"
date: "2026-06-07"
arxiv_id: "2606.08850"
arxiv_url: "https://arxiv.org/abs/2606.08850"
pdf_url: "https://arxiv.org/pdf/2606.08850v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
  - "stat.ML"
tags:
  - "推理时扩展"
  - "粒子滤波"
  - "智能体推理"
  - "输出选择"
  - "无验证域"
  - "自适应计算分配"
relevance_score: 8.2
---

# Intrinsic Selection and Particle Resampling for Inference-Time Scaling Beyond Domain Verifiability

## 原始摘要

Inference-Time Scaling (ITS) has largely succeeded in verifiable domains like math and coding, where cheap verification enables scalable output selection. However, extending ITS to tasks prone to systematic failure - driven by faulty initial assumptions or unmet multidimensional constraints - typically relies on costly external solvers or brittle, model-based verifiers. Our key insight is that the intrinsic statistics of parallel sample sets, specifically length-adjusted tail entropy, provide a robust discriminative signal for solution quality without access to ground truth. Crucially, these statistics serve as a difficulty gate for adaptive compute allocation, dynamically routing problems across scaling regimes. First, Intrinsic Selection (iS) ranks candidates post-hoc, matching consensus-based algorithms across three domains and improving engineering design selection by 20% over pass@1 baselines. Second, Intrinsic Particle Filtering (iPF) generalizes this to step-level resampling, guiding generation toward high-confidence reasoning trajectories to improve pass@1 by 6.1 points on average on hard math problems. Finally, Particle Distillation (dPF) injects privileged guidance via early logit blending and KL-guided resampling, steering generation past systematic reasoning errors to satisfy expert rubrics, yielding up to 26.5% gains on complex clinical responses. Our pipeline applies seamlessly across broad-purpose, domain-specialized, and multimodal architectures, successfully extending ITS to open-ended domains without requiring trained reward models or exact ground-truth verification.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决如何将推理时扩展（ITS）技术从可验证领域（如数学和编程，其中低成本的外部验证可行）推广到缺乏外部验证的开放领域这一核心问题。现有方法，如自一致性（self-consistency）和基于奖励模型的采样，严重依赖外在指标（例如输出标准化、解析器或训练好的奖励模型）来对候选解进行排序和选择。然而，在创意写作、工程设计或复杂临床推理等开放领域，外部验证要么成本高昂，要么不可用或不可靠，且基于模型的验证器也常常脆弱且昂贵，这构成了严重的瓶颈。导致许多需要系统性推理的任务（如复杂数学问题或工程设计）常常因为错误的初始假设或多维约束而遭遇失败。因此，本文要解决的核心问题是：**能否仅从生成样本集本身的内在统计特性中提取判别信号，来指导推理时计算资源的分配和候选解的筛选，从而彻底绕过对外部验证器（如奖励模型、标准答案）的依赖。** 论文的关键洞见在于，并行样本集的固有统计量（特别是长度调整后的尾熵）包含了无需真实答案的解的质量和问题难度的判别信号。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：  
1. **基于共识的选择方法**：如Self-Consistency（SC）通过多数投票从并行采样中选择答案，依赖廉价语法验证，但在开放域或多部分任务中受限；Universal SC引入LLM评判扩展能力，但增加验证成本。本文的Intrinsic Selection（iS）不依赖外部验证，利用样本集的长度调整尾熵进行排名，在开放域中匹配共识算法效果。  
2. **基于置信度的选择方法**：包括强化学习模型的内在验证、Self-Certainty、token级logit加权等，通过对单个轨迹熵量化模型不确定性。本文补充了这些方法，从N样本集的集体统计中提取判别信号，而非仅依赖单轨迹的步骤级验证。  
3. **基于粒子的推理与引导方法**：如序贯蒙特卡洛（SMC）和粒子滤波（PF），通过重要性重采样近似后验，但通常需要过程奖励模型（PRM）作为观测模型，而PRM昂贵且易过拟合。本文的Intrinsic Particle Filtering（iPF）和Particle Distillation（dPF）将重采样推广到步骤级，利用内在统计避免PRM依赖，可引导生成避开系统性错误。  

本文的核心区别在于：通过样本集内在统计（尾熵）替代外部验证或PRM，使ITS扩展到非可验证域，无需训练奖励模型或精确真实答案。

### Q3: 论文如何解决这个问题？

该论文通过利用生成样本的内在统计特性（如熵）来扩展推理时间缩放（ITS）到难以验证的开放领域，无需外部奖励模型或真实标签。核心方法包括三个组件：Intrinsic Selection (iS)、Intrinsic Particle Filtering (iPF) 和 Particle Distillation (dPF)。

整体框架基于自适应尾熵（Adaptive Tail Entropy）指标，该指标通过计算样本序列尾部（基于长度和熵自适应确定）的token级熵中位数来评估样本质量。这一指标同时作为难度门控：低熵样本直接通过iS选出最佳候选，高熵样本则路由至iPF或dPF进行更深入的干预。

iS是一种后验候选选择方法，通过比较各样本的自适应尾熵得分（得分越小越优）来识别最佳答案，无需外部验证。在三个领域上，其性能与基于共识的算法相当，在工程设计选择上相比pass@1提升20%。

iPF将粒子滤波思想推广到步骤级重采样。它利用内在熵定义伪观测似然（`w_t ∝ w_{t-1} exp(-H[z_t])`），并通过稳健归一化（使用批均值和标准差标准化熵值后再用softmax）避免粒子退化。这使得iPF能聚焦于高置信度推理轨迹，在困难数学问题上平均提升pass@1达6.1点。

dPF针对系统性失败（`pass@N≈0`）问题，引入特权信息引导。其关键技术包括：早期步骤的logit混合（类似无分类器引导，线性退火混合系数α）和后续的KL散度引导重采样（`w_t ∝ w_{t-1} exp(-KL[p_θ || q])`）。该方法能主动纠正错误初始假设，满足多维约束，在复杂临床响应任务上实现高达26.5%的性能提升。

整个方法无需训练奖励模型或精确真实验证，可直接应用于通用、领域专用和多模态架构。

### Q4: 论文做了哪些实验？

该论文进行了覆盖五大领域的全面实验。实验设置包括：在数学（AIME、HMMT）、推理（GPQA-Diamond）、代码（LiveCodeBench-v6）、医疗（HealthBench-Hard）和工程设计（Fusion360）五个数据集上进行评估。使用Qwen3-4B、Gemma-4、MedGemma和Qwen2.5-VL四种架构。

主要实验包括三部分：1）**Intrinsic Selection (iS)实验**：在7个基准上使用单一尾熵估计器，iS@1达到最佳中位数47.7%和加权平均41.9%，优于pass@1的38.8%，与Self-Consistency（46.0%）竞争。在工程设计的Fusion360上，iS@1将平均IoU从0.41提升至0.45，相比pass@1提升20%。2）**Intrinsic Particle Filtering (iPF)实验**：在AIME最难25%子集上，iPF将pass@1从17.0%提升至22.8%（AIME2024），从5.6%提升至14.7%（AIME2026），平均提升6.1个百分点。在HealthBench-Hard上持续改善临床推理分数。3）**Particle Distillation (dPF)实验**：仅用8个样本，dPF在数学基准上匹配或超越32样本i.i.d.基线，在HMMT-2026上提升8.9个百分点，在复杂临床任务上获得高达26.5%的提升。

对比方法包括pass@1、Self-Consistency、pass@N和DeepConf基线。关键指标显示尾熵AUROC>0.79，自适应计算的精度>90%。

### Q5: 有什么可以进一步探索的点？

论文在扩展推理时缩放（ITS）至非可验证领域方面取得了重要进展，但仍存在若干可探索方向。首先，其核心指标“长度调整尾熵”的鲁棒性有待验证：当样本生成长度方差极大或任务涉及多模态信息时，熵对质量信号的区分能力可能下降。未来可研究结合语义相似度或跨样本一致性（如投票熵）构建复合信号。其次，iPF的步骤级重采样依赖中间状态熵，但未考虑推理路径的因果依赖关系，可能导致“局部合理但全局错误”的轨迹被保留。引入结构化剪枝或基于反事实推理的路径评估或许能缓解此问题。此外，dPF通过早期logit混合注入先验知识，但混合权重需人工设定，未来可设计自适应策略（如梯度引导的权重更新）以适配不同任务。最后，该方法在真实临床场景中依赖专家编写规则，成本较高，探索利用少量标注数据自动提炼关键约束将显著提升实用性。

### Q6: 总结一下论文的主要内容

该论文提出了一套基于内在统计量的推理时扩展（ITS）框架，旨在突破传统方法对可验证领域（如数学、编码）外部验证器的依赖。核心问题是在缺乏真值或奖励模型时，如何对采样结果进行有效筛选与生成引导。作者的核心洞察是，平行样本集的内部统计特征（如经长度调整的尾熵）可作为解质量的判别信号，并充当难度门控以自适应分配计算资源。方法包括三个互补组件：内在选择（iS）利用集合级熵指标实现后验排序；内在粒子滤波（iPF）通过步骤级熵引导重采样，聚焦高置信轨迹；粒子蒸馏（dPF）则引入特权信息（如评分标准）进行对数几率混合与KL散度引导修正。实验表明，iS在不依赖输出验证时匹配了共识算法的性能，并在CAD任务中将pass@1提升20%；iPF在困难数学题上平均提升6.1个百分点；dPF利用8个粒子便实现了复杂临床响应26.5%的增益。该框架无需训练奖励模型，成功将ITS扩展至开放领域，验证了内在熵作为跨领域、跨架构通用信号的有效性。
