---
title: "Scaling Inference-Time Computation via Opponent Simulation: Enabling Online Strategic Adaptation in Repeated Negotiation"
authors:
  - "Xiangyu Liu"
  - "Di Wang"
  - "Zhe Feng"
  - "Aranyak Mehta"
date: "2026-02-22"
arxiv_id: "2602.19309"
arxiv_url: "https://arxiv.org/abs/2602.19309"
pdf_url: "https://arxiv.org/pdf/2602.19309v1"
categories:
  - "cs.MA"
tags:
  - "Agent 架构"
  - "多智能体系统"
  - "Agent 推理"
  - "Agent 规划"
  - "在线学习"
  - "博弈论"
  - "对手建模"
  - "推理时计算"
relevance_score: 9.0
---

# Scaling Inference-Time Computation via Opponent Simulation: Enabling Online Strategic Adaptation in Repeated Negotiation

## 原始摘要

While large language models (LLMs) have emerged as powerful decision-makers across a wide range of single-agent and stationary environments, fewer efforts have been devoted to settings where LLMs must engage in \emph{repeated} and \emph{strategic} interactions with unknown or dynamic opponents. In such settings, recipes built upon \emph{offline} pre-training or fine-tuning, though robust against worst-case adversaries, do not fully exploit the capability of LLMs to adapt \emph{online} based on interaction feedback. Instead, we explore the more natural perspective of scaling inference-time computation as a mechanism for adaptation, embedding the principles of a classical game-theoretical learning dynamic, \emph{smooth Fictitious Play (sFP)}, into LLM inference: (i) for belief formation, we employ an auxiliary opponent model that in-context learns to imitate the time-averaged behavior of the opponent; (ii) for best response, we advance best-of-$N$ (BoN) sampling by simulating against the opponent model. Empirical evaluations on two distinct forms of repeated negotiation games demonstrate that our method enables significant performance improvement over repeated online interaction compared to various baselines, offering a scalable and principled approach to repeated strategic decision-making without any parameter updates.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）在**重复、动态的多人战略交互环境**中缺乏**在线适应能力**的核心问题。具体而言，当前LLM在单智能体或静态环境中表现出色，但在需要与未知或随时间变化的对手进行多轮战略博弈（如重复谈判）时，仅依赖离线预训练或微调的方案（如寻求纳什均衡）往往过于保守，无法利用在线交互反馈进行实时调整。论文认为，依赖梯度更新的在线适应方法数据需求大、延迟高，因此探索了一种更自然的替代范式：**通过扩展推理时计算来实现在线战略适应**。为此，作者将经典博弈论学习动态——平滑虚拟博弈（sFP）——的原则嵌入LLM推理过程，设计了两个模块：利用辅助对手模型从历史中学习对手行为（信念形成），以及通过与该模型模拟对局来优化候选策略的响应（最佳响应）。该方法旨在为LLM提供一种无需参数更新、可扩展且原则性的途径，使其能在重复战略决策中实现持续的在线性能提升。

### Q2: 有哪些相关研究？

相关工作主要围绕两个方向展开。首先是**语言模型在谈判游戏中的应用**。早期研究如Lewis等人（2017）和He等人（2018）使用循环神经网络和对话行为解码进行谈判。近期工作则利用大语言模型（LLM）作为自然语言接口，侧重于在单次谈判中评估（如Davidson等人，2024）或提升（如Hua等人，2024；Zhang等人，2025）LLM的谈判能力。这些研究主要关注单回合内的静态策略性能，而非本文重点的在线适应与重复交互中的持续改进。

其次是**LLM智能体用于通用战略决策**。在LLM作为核心控制器应用于各种单智能体决策问题（如Yao等人，2023；Zhou等人，2024）的背景下，许多研究评估了LLM在具有明确符号动作空间的战略环境（如标准形式博弈、强盗问题）中的决策能力。这些方法可分为两类：第一类（如Meta，2022；Xu等人，2024）依赖于微调、自博弈或强化学习等参数更新技术，旨在学习一个可静态部署的强策略，但在重复谈判中可能过于保守且不适合测试时的在线适应。第二类无需参数更新，包括输入级的提示工程（如Fu等人，2023；Yu等人，2025）和输出级的搜索（如Kempinski等人，2025；Light等人，2025）。其中，仅提示工程方法与在线适应相关，但本文方法与之不同，它通过将平滑虚拟博弈（sFP）原理嵌入LLM推理，系统地在推理时扩展计算，实现了基于对手模型模拟的在线信念形成与最佳响应，为重复战略决策提供了更具原则性和可扩展性的无参数更新方案。

### Q3: 论文如何解决这个问题？

论文通过扩展推理时计算来解决在线战略适应问题，核心方法是将经典博弈论学习动态——平滑虚拟对局（smooth Fictitious Play, sFP）嵌入到LLM推理过程中。该方法包含两个关键步骤：信念形成与最佳响应。

在信念形成阶段，论文设计了基于上下文学习的对手模型（in-context opponent modeling）。由于自然语言动作空间巨大，传统基于频率的信念更新不可行，因此采用一个辅助LLM作为对手模型，通过历史交互数据（过去多轮对话轨迹）进行上下文学习，模仿对手的时间平均行为。该模型在预测时不仅接收历史上下文和当前部分轨迹，还通过特定提示词要求其先总结对手的高层战略模式，并融入“面对不确定性的乐观”（OFU）原则，在不确定时偏向对己方有利的预测，从而构建对对手策略的估计。

在最佳响应阶段，论文改进了Best-of-N（BoN）采样方法，结合对手模拟进行战略决策。首先，通过“战略头脑风暴”结构化地生成N个多样化的候选策略（如“以牙还牙”、“公平分割”），而非独立同分布采样，以确保广泛探索策略空间。然后，对每个候选动作，利用己方基础策略和上述对手模型，模拟完整的未来对话轨迹，并估算己方累积奖励。最后，选择模拟奖励最高的候选动作执行。这一过程本质上相当于在推理时执行了一次策略迭代：模拟步骤近似于策略评估（估算Q值），选择最优动作则对应于策略改进。

整个架构在推理时完成，无需参数更新。理论分析表明，对手模型的误差会线性影响价值评估和最终策略的最优性差距，验证了方法的可靠性。实验证明，该方法在重复谈判游戏中能显著提升在线交互性能，实现了可扩展、有理论保证的重复战略决策。

### Q4: 论文做了哪些实验？

论文在两种重复谈判游戏（买家-卖家游戏和资源交换游戏）中进行了实验，实验设置遵循了先前研究，但调整了部分参数以增加挑战性（如卖家成本设为43，买家预算设为63）。基准测试涵盖三类方法：标准推理（零样本基线、带思考的基线）、推理时计算扩展（BoN评估、BoN自模拟、BoN对手独立采样）以及外部自适应方法（AI反馈、经验反思、私有信息预测）。主要结果包括：1）面对通用动态对手时，论文方法（BoN-oppo）通过学习曲线展现出最显著且一致的性能提升，优于所有基线，其中BoN自模拟通常排名第二；2）面对专业自适应对手时，该方法仍持续超越现有先进方法；3）在环境随机性（对手私有约束随机化）下保持稳健性能；4）在不同骨干LLM的对手架构中具有良好的泛化能力；5）在资源交换游戏中，双方均使用该方法时实现了最高的社会福利，表明推理时计算扩展能促进更高效的均衡结果。机制分析进一步验证了对手模型随历史积累提高模拟准确性，以及战略头脑风暴生成更多样化候选策略的有效性。效率分析显示，该方法支持完全并行化，延迟开销低，且即使较小的采样数N也能带来较高收益提升。

### Q5: 有什么可以进一步探索的点？

本文提出的基于对手模拟的推理时计算扩展方法，虽然在重复谈判场景中展现了在线策略适应的潜力，但仍存在一些局限性和值得深入探索的方向。局限性方面：首先，方法依赖于对对手行为的上下文学习与模拟，当对手策略高度复杂或非平稳时，模拟的准确性与适应性可能受限；其次，采用最佳N采样（BoN）进行最优响应计算，计算成本较高，在实时性要求高的交互中可能面临可扩展性挑战；此外，当前实验集中于特定谈判游戏，其泛化能力到更广泛、开放式的多轮战略交互（如外交、经济博弈）尚未得到验证。

未来方向可重点探索：1）**高效模拟与推理机制**：研究更轻量级的对手模型与响应生成方法，以降低计算开销；2）**长期记忆与元学习**：引入长期记忆模块，使智能体不仅能适应单次会话，还能在跨会话中积累经验并进行元策略调整；3）**多智能体协同与通信**：将框架扩展至多方动态博弈，探索基于模拟的协同策略与显式通信机制；4）**理论保障与安全边界**：结合博弈论分析，为在线适应过程提供收敛性、稳定性与安全性理论支撑。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种通过推理时计算扩展来实现在线战略适应的新方法，特别针对LLM在重复战略交互（如重复谈判）中的决策问题。其核心贡献在于将经典博弈论学习动态——平滑虚拟博弈（sFP）——嵌入到LLM推理过程中，从而无需更新模型参数即可实现在线适应。具体通过两个关键机制实现：一是信念形成，利用一个辅助的对手模型进行上下文学习，以模仿对手的时间平均行为；二是最佳响应，通过与该对手模型进行模拟，改进了最佳N采样（BoN）方法。实验表明，该方法在两种不同的重复谈判游戏中显著优于各类基线，为LLM在动态、未知对手环境下的重复战略决策提供了一种可扩展且原理清晰的新路径。
