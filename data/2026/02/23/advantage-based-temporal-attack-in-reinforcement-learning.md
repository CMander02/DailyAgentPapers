---
title: "Advantage-based Temporal Attack in Reinforcement Learning"
authors:
  - "Shenghong He"
date: "2026-02-23"
arxiv_id: "2602.19582"
arxiv_url: "https://arxiv.org/abs/2602.19582"
pdf_url: "https://arxiv.org/pdf/2602.19582v1"
categories:
  - "cs.LG"
tags:
  - "强化学习"
  - "对抗攻击"
  - "时序攻击"
  - "Agent安全"
  - "Transformer"
relevance_score: 6.0
---

# Advantage-based Temporal Attack in Reinforcement Learning

## 原始摘要

Extensive research demonstrates that Deep Reinforcement Learning (DRL) models are susceptible to adversarially constructed inputs (i.e., adversarial examples), which can mislead the agent to take suboptimal or unsafe actions. Recent methods improve attack effectiveness by leveraging future rewards to guide adversarial perturbation generation over sequential time steps (i.e., reward-based attacks). However, these methods are unable to capture dependencies between different time steps in the perturbation generation process, resulting in a weak temporal correlation between the current perturbation and previous perturbations.In this paper, we propose a novel method called Advantage-based Adversarial Transformer (AAT), which can generate adversarial examples with stronger temporal correlations (i.e., time-correlated adversarial examples) to improve the attack performance. AAT employs a multi-scale causal self-attention (MSCSA) mechanism to dynamically capture dependencies between historical information from different time periods and the current state, thus enhancing the correlation between the current perturbation and the previous perturbation. Moreover, AAT introduces a weighted advantage mechanism, which quantifies the effectiveness of a perturbation in a given state and guides the generation process toward high-performance adversarial examples by sampling high-advantage regions. Extensive experiments demonstrate that the performance of AAT matches or surpasses mainstream adversarial attack baselines on Atari, DeepMind Control Suite and Google football tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度强化学习（DRL）中现有对抗攻击方法在时序相关性上的不足。具体而言，当前基于未来奖励的对抗攻击方法（reward-based attacks）在生成序列时间步上的对抗扰动时，未能有效捕捉不同时间步之间的依赖关系，导致当前扰动与历史扰动之间的时序关联性较弱，从而限制了攻击效果。论文提出了两个核心挑战：一是现有序列建模方法无法区分和有效利用不同时间尺度（如短期和长期）的依赖关系，而这些关系对于在序列决策中生成有效的对抗扰动至关重要；二是在缺乏高质量“专家”攻击轨迹数据的情况下，现有方法难以从次优轨迹中学习并生成高性能的对抗样本。

为此，论文提出了一种名为“基于优势的对抗Transformer”（AAT）的新方法。该方法通过两个关键机制来解决上述问题：1）多尺度因果自注意力（MSCSA）机制，它能动态建模不同时间尺度的历史信息与当前状态之间的依赖关系，从而生成具有更强时序相关性的对抗扰动；2）加权优势机制，它量化了特定状态下扰动的有效性（即“扰动优势”），并以此为指导，优先采样高优势区域的扰动，从而减少对专家数据的依赖，并能从次优数据中学习生成高性能对抗样本。最终目标是生成具有高攻击性能的“时间相关对抗样本”，以更有效地降低智能体的累积奖励，更全面地揭示DRL模型在时序决策中的脆弱性。

### Q2: 有哪些相关研究？

相关研究主要分为两类：梯度基攻击和奖励基攻击。梯度基攻击方法（如FGSM）利用梯度优化技术在每一步生成扰动，但仅关注当前时刻，忽略了长期目标，限制了攻击效果。奖励基攻击方法（如基于强化学习的方法）通过利用当前状态和未来奖励来生成对抗样本，以改善长期攻击性能。然而，现有奖励基方法未能有效捕捉当前状态与历史信息之间的依赖关系，导致生成的扰动时间相关性较弱，从而难以有效降低智能体的累积奖励。

本文提出的AAT方法（Advantage-based Adversarial Transformer）与这些工作密切相关，但进行了关键改进。针对奖励基攻击的不足，AAT引入了多尺度因果自注意力机制（MSCSA），以动态捕捉不同时间尺度（短期和长期）的历史信息与当前状态之间的依赖关系，从而增强扰动的时间相关性。此外，AAT还设计了加权优势机制，通过量化扰动在特定状态下的有效性（即扰动优势），引导生成过程朝向高性能对抗样本，减少了对专家轨迹数据的依赖。因此，AAT在序列建模的框架下，综合提升了攻击的时序连贯性和有效性，实验表明其性能优于主流基线。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“基于优势的对抗性变换器（AAT）”的新方法来解决强化学习模型中对抗样本攻击的时序相关性问题。其核心架构设计围绕两个关键技术：多尺度因果自注意力（MSCSA）机制和加权优势引导机制。

首先，MSCSA机制旨在增强对抗扰动生成的时序相关性。它通过定义多个不同长度（短、中、长期）的因果注意力窗口，并行地捕捉历史状态序列在不同时间尺度上的依赖关系。每个尺度使用独立的因果自注意力块处理对应的子序列，并通过门控融合操作将各尺度的输出整合为一个统一的、具有时序感知的潜在表示向量。这使得生成的当前扰动不仅能考虑近期状态以立即翻转关键决策，还能保持与长期历史扰动策略的一致性，从而形成连贯的、具有轨迹级影响的攻击。

其次，加权优势机制用于引导生成过程产生高攻击性能的扰动。该方法首先通过训练Q网络和V网络，并利用期望回归技术来估计状态-动作价值函数和状态价值函数，进而计算对抗优势值A（量化特定扰动对策略性能下降的预期边际影响）。为避免优势值估计的过拟合问题，论文进一步引入一个加权函数对原始优势值进行平滑约束，得到加权优势值Ã。在生成阶段，扰动分布由两部分构成：一个从训练数据学习的基础生成模型，以及一个以加权优势值为条件的指数权重项。这确保生成过程优先采样历史上高效（高优势）的扰动模式，而不是简单地模仿数据。

在具体实现上，AAT采用自回归训练方式，将状态、动作、扰动和加权优势序列作为轨迹表示进行学习。对于图像等高维输入，采用Vision Transformer的补丁编码来聚焦任务关键特征。训练损失结合了动作预测的均方误差和扰动幅度的L2正则化。在攻击阶段，还训练一个优势预测网络，通过最大化熵正则化来更好地覆盖状态空间中的高优势区域，从而动态生成每一步局部最优的扰动。

综上，AAT通过MSCSA捕获多粒度时序依赖，并通过加权优势机制实现面向高性能攻击的定向优化，二者协同工作，生成了具有强时序相关性且攻击效果显著的对抗样本。

### Q4: 论文做了哪些实验？

论文在Atari 2600的六款游戏（Breakout、Pong、Chopper Command、Sequest、Qbert和Space Invaders）、DeepMind Control Suite（连续动作空间）以及Google Football（高维状态空间）环境中进行了实验。目标策略包括DQN、A3C、TRPO、DDPG和PPO。实验将提出的AAT攻击方法与两类基线进行比较：一类是基于奖励的攻击方法（PA-AD、AdvRL-GAN、TSGE、PIA），它们通过强化学习构建攻击策略；另一类是主流基于梯度的攻击方法（FGSM、Skip、S-T、EDGE）。评估指标为目标策略在遭受攻击后的平均累积奖励（游戏分数），分数越低表明攻击性能越好。实验设置了白盒和黑盒攻击场景。

主要结果以Breakout游戏为例（表格数据不全，但提供了关键信息）：在无攻击（*）时，DQN和A3C的累积奖励分别约为355.83和384.52。在白盒攻击下，AAT对DQN的攻击效果（6.56±2.54）与表现最佳的基线TSGE（6.42±4.21）相当，并显著优于其他基线方法（如FGSM的34.30±3.78）。这表明AAT能够生成具有强时序相关性的对抗样本，有效降低智能体的性能，其攻击效果达到或超越了主流基线方法。

### Q5: 有什么可以进一步探索的点？

本文提出的AAT方法在强化学习对抗攻击中引入了时序关联性，但仍有进一步探索的空间。局限性在于：1）方法主要针对离散动作空间，在连续控制任务中的泛化能力有待验证；2）攻击假设需获取环境交互权限，实际部署中可能受限；3）未考虑防御机制下的鲁棒性测试。

未来方向可包括：1）开发更轻量的注意力机制以降低计算开销；2）研究黑盒攻击场景下的迁移攻击方法；3）探索多智能体系统中的协同攻击策略；4）结合元学习实现跨任务的快速攻击适配；5）从防御角度研究时序攻击的检测与缓解技术，形成攻防闭环。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为“基于优势的对抗性变换器”（AAT）的新方法，用于生成针对深度强化学习（DRL）智能体的时序相关对抗样本。其核心贡献在于解决了现有基于未来奖励的攻击方法在生成序列扰动时，难以捕捉不同时间步之间依赖关系、导致时序相关性弱的问题。AAT通过两个关键机制实现突破：一是采用多尺度因果自注意力（MSCSA）机制，动态建模历史信息与当前状态之间的依赖，从而增强当前扰动与先前扰动之间的相关性；二是引入加权优势机制，量化给定状态下扰动的有效性，并通过采样高优势区域来引导生成高性能对抗样本。实验表明，AAT在Atari、DeepMind Control Suite和Google Football等多个基准任务上的攻击性能达到或超越了主流基线。该工作的意义在于显著提升了对抗攻击在时序决策场景下的有效性和隐蔽性，为评估和增强DRL系统的鲁棒性提供了更强大的工具。
