---
title: "General Preference Reinforcement Learning"
authors:
  - "Muhammad Umer"
  - "Muhammad Ahmed Mohsin"
  - "Ahsan Bilal"
  - "Arslan Chaudhry"
  - "Andreas Haupt"
  - "Sanmi Koyejo"
  - "Emily Fox"
  - "John M. Cioffi"
date: "2026-05-18"
arxiv_id: "2605.18721"
arxiv_url: "https://arxiv.org/abs/2605.18721"
pdf_url: "https://arxiv.org/pdf/2605.18721v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "LLM对齐"
  - "偏好优化"
  - "奖励模型"
  - "多维度偏好"
  - "表征学习"
  - "策略梯度"
  - "奖励破解"
  - "信任区域"
relevance_score: 8.0
---

# General Preference Reinforcement Learning

## 原始摘要

Post-training has split large language model (LLM) alignment into two largely disconnected tracks. Online reinforcement learning (RL) with verifiable rewards drives emergent reasoning on math and code but depends on a programmatic verifier that cannot reach open-ended tasks, while preference optimization handles open-ended generation yet forgoes the continuous exploration that powers online RL. Closing this gap requires a verifier for open-ended quality, but a scalar reward model is the wrong shape for the job. Quality is multi-dimensional, and any scalar score is an incomplete proxy that lets online RL collapse onto whichever axis the score is most sensitive to. We turn instead to the General Preference Model (GPM), which embeds responses into $k$ skew-symmetric subspaces and represents preference as a structured, intransitivity-aware comparison. Building on this, we propose General Preference Reinforcement Learning (GPRL), which carries the $k$-way structure through to the policy update. GPRL computes per-dimension group-relative advantages, normalizes each on its own scale so no axis can dominate, and aggregates them with context-dependent eigenvalues. The same structure powers a closed-loop drift monitor that detects single-axis exploitation and corrects it on the fly by reweighting dimensions and tightening the trust region. Starting from $\texttt{Llama-3-8B-Instruct}$, GPRL reaches a length-controlled win rate of $56.51\%$ on AlpacaEval~2.0 while also outperforming SimPO and SPPO on Arena-Hard, MT-Bench, and WildBench by resisting reward hacking across extended training runs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型（LLM）后训练中在线强化学习与偏好优化两条技术路线相互割裂的核心问题。研究背景是：RLHF通常使用标量奖励模型配合PPO进行在线训练，但存在训练不稳定、易导致奖励破解（reward hacking）等缺陷。当前领域分化为两个独立方向：一是基于静态或迭代偏好数据的离线优化方法（如DPO、SimPO、SPPO），这类方法能很好地处理开放任务，但放弃了持续在线探索；二是基于程序化验证器（如数学检查器）的在线强化学习方法（如GRPO、RLVR），这类方法通过在线采样激发了自我反思等涌现能力，但无法应用于缺乏程序化验证器的开放任务。一个直观的结合方案是使用学习的标量奖励模型替代程序化验证器运行在线RL，但实践中在长期训练下仍会因奖励破解而失败。该问题的根源在于，人类对回答质量的需求是多维的（如有用性、事实准确性、安全性、风格等），任何标量评分都是不完整的代理，优化它会导致模型在奖励模型最敏感的单一维度上过度优化而忽视其他维度。本文提出的核心解决方案是：利用通用偏好模型（GPM）提供结构化的多维偏好信号，并在此基础上提出通用偏好强化学习（GPRL），通过计算每个维度的组相对优势并归一化聚合，以及设计闭环漂移监控器来在线检测和纠正奖励破解，从而将在线RL扩展到开放任务。

### Q2: 有哪些相关研究？

在相关工作中，本文主要在三个方向上与现有研究进行了对比。首先，在直接偏好优化与博弈论方法方面，DPO及其变体（如IPO、KTO、SimPO、SPPO、Nash-MD）通过重新参数化RLHF目标来避免显式奖励建模，并将对齐视为博弈。但这些方法依赖静态或迭代更新的批次，优化一旦固定便停止探索，其改进上限受限于偏好数据质量而非计算量。本文的GPRL则通过在线RL持续探索，突破了这一限制。其次，在线RL与可验证奖励方面，GRPO、DeepSeek-R1、DAPO等方法结合了群体相对优势估计与二进制验证器，在数学和代码任务上展现出涌现推理行为，但它们需要程序化验证器，无法应用于开放式任务，若改用标量奖励模型则又会产生奖励滥用问题。GPRL通过结构化的多维奖励解决了这一矛盾。最后，在多维度偏好建模方面，Fine-Grained RLHF、Rewarded Soups、MODPO等方法通过独立标量线性和或权重插值来处理多维度质量，但缺乏对单维度滥用风险的监测。GPRL基于GPM的k维非对称嵌入结构，实现了分维度归一化的优势估计和实时漂移监测，有效防止了奖励破解。

### Q3: 论文如何解决这个问题？

GPRL通过将GRPO的标量奖励替换为GPM的多维偏好信号来解决奖励黑客问题，并将这种k维结构延续到策略更新中。

核心方法包含三个关键设计。首先，GPRL为每个prompt采样G个响应，通过冻结的GPM模型获得每个响应的2k维嵌入和特征值。然后，在优势估计阶段，它计算k个成对得分矩阵，通过组内平均得到每个维度的群体得分。与GRPO直接聚合不同，GPRL对每个维度独立进行归一化（减去均值除以标准差），确保不同尺度的子空间信号得到平等对待，避免了某个维度过大主导整体优势。最后，利用特征值作为权重聚合归一化后的各维度优势，形成最终的聚合优势。

架构上，GPRL保持了与GRPO相同的裁剪代理目标函数形式，仅替换了优势函数计算，因此能够无缝集成到现有的大规模RL基础设施中。

创新点在于：(1) 将GPM的多维偏好结构(包括不可递性)完整引入策略优化；(2) 通过逐维度归一化确保没有任何单一轴可以主导训练；(3) 设计闭环漂移监控器，通过跟踪各维度优势的方差分布变化(α^(t)相对于初始值的KL散度)来检测奖励黑客行为，当检测到单一轴利用时，自动调整维度权重(m_l)和信任区域(β)，抑制过度优化。这种多维结构理论上确保当策略试图单轴优化时，聚合优势反而会降低，从而引导梯度远离黑客行为。

### Q4: 论文做了哪些实验？

论文在Llama-3-8B-Instruct基座上，比较了GPRL与DPO、SimPO、SPPO、GPO、GRPO五种基线方法。实验设置：使用两套奖励模型（标量BT模型和六维GPM模型），分别在Gemma-2B-it和Llama-3.1-8B-Instruct两种规模上训练；从UltraFeedback采样提示，在线生成长度512、G=8的回复，共训练3个epoch（与SPPO/GPO三轮迭代计算量匹配）。主要评测四个基准：AlpacaEval 2.0（805条提示，报告长度控制胜率LC.WR）、Arena-Hard v2（500条对抗性查询）、MT-Bench（80条多轮提示）、WildBench（1024条野生指令，输出WB-Score和WB-Reward）。核心结果：
1. GPRL（8B GPM）在AlpacaEval 2.0上达到56.51% LC.WR，胜GRPO+BT（41.92%）达14.59个点，胜最佳迭代方法SPPO（8B BT，42.55%）达13.96个点；平均回复长度仅1600 token，远低于其他基于奖励模型的方法（2400-3300 token）。
2. Arena-Hard上GPRL以1.3胜率领先（最佳基线约0.9），MT-Bench得分8.33（最佳基线约8.1），WildBench达37.98/11.15（最佳基线约37.05/9.57）。
3. 消融实验显示：子空间数k从1增至3带来最大提升（LC.WR从44.21升至56.51）；每维度归一化比全局归一化降低长度漂移（维持在1600 vs. 2104 token）；漂移控制器在扩展训练中至关重要，第三epoch贡献约3.67个LC.WR点，第五epoch差距扩大至8.65-10.91点；群规模G=8时增益饱和。

### Q5: 有什么可以进一步探索的点？

这篇论文提出的GPRL方法在利用多维偏好结构抑制奖励黑客方面很有潜力，但未来仍有若干可探索的维度。首先，其依赖“通用偏好模型”提取的k维嵌入空间，物理意义尚不明确（如各维度可能对应“创造性”与“准确性”的重叠），可探索通过对抗性解释或人为标注来赋予维度可解释性，并允许人类专家动态调整权重。其次，当前闭环漂移检测基于固定阈值与重新加权策略，可尝试将其变为自适应元学习过程，让策略自动学会何时收紧信任区域，或结合贝叶斯不确定性估计预防维度坍缩。此外，实验仅在Llama-3-8B上验证，可扩展至更大模型（如70B）或不同架构（如Mamba）测试其通用性，并探索在长链条推理（比如代码生成、数学证明）中的行为——这类任务可能依赖单维度穿透而非多维度平衡，需要设计任务自适应维度聚合策略。最后，可研究将GPRL与过程监督、世界模型结合，构建完全无标量奖励的强化学习范式的理论界限与收敛性证明。

### Q6: 总结一下论文的主要内容

这篇论文提出了通用偏好强化学习（GPRL）框架，旨在弥合大语言模型后训练中在线RL与偏好优化之间的鸿沟。问题在于：在线RL依赖可验证奖励，虽能推动数学和代码推理，却无法处理开放式任务；而偏好优化虽能处理开放式生成，却缺乏持续探索能力。作者认为，根本原因在于奖励的形状而非强度——标量奖励模型是多维人类质量的“不完整代理”，会导致在线RL仅沿其最敏感的轴进行单轴利用。方法上，GPRL基于通用偏好模型（GPM）将响应嵌入k个斜对称子空间，结构化地表示偏好（支持非传递性比较）；在策略更新中，它计算各维度的组相对优势，归一化后结合上下文相关特征值聚合，防止单轴主导。同时，闭环漂移监控器可检测并纠正单轴利用。主要结论：基于Llama-3-8B-Instruct，GPRL在AlpacaEval 2.0上达到56.51%的长度控制胜率，并在Arena-Hard、MT-Bench和WildBench上优于SimPO和SPPO，有效抵抗了奖励黑客攻击。该工作首倡将监督结构作为一等设计变量，对偏好优化之外的学习任务具有重要借鉴意义。
