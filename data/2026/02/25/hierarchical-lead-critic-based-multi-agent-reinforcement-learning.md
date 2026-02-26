---
title: "Hierarchical Lead Critic based Multi-Agent Reinforcement Learning"
authors:
  - "David Eckel"
  - "Henri Meeß"
date: "2026-02-25"
arxiv_id: "2602.21680"
arxiv_url: "https://arxiv.org/abs/2602.21680"
pdf_url: "https://arxiv.org/pdf/2602.21680v1"
categories:
  - "cs.LG"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "强化学习"
  - "分层架构"
  - "协作学习"
  - "MARL"
  - "样本效率"
  - "策略鲁棒性"
relevance_score: 9.0
---

# Hierarchical Lead Critic based Multi-Agent Reinforcement Learning

## 原始摘要

Cooperative Multi-Agent Reinforcement Learning (MARL) solves complex tasks that require coordination from multiple agents, but is often limited to either local (independent learning) or global (centralized learning) perspectives. In this paper, we introduce a novel sequential training scheme and MARL architecture, which learns from multiple perspectives on different hierarchy levels. We propose the Hierarchical Lead Critic (HLC) - inspired by natural emerging distributions in team structures, where following high-level objectives combines with low-level execution. HLC demonstrates that introducing multiple hierarchies, leveraging local and global perspectives, can lead to improved performance with high sample efficiency and robust policies. Experimental results conducted on cooperative, non-communicative, and partially observable MARL benchmarks demonstrate that HLC outperforms single hierarchy baselines and scales robustly with increasing amounts of agents and difficulty.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决协作式多智能体强化学习（MARL）中，现有方法通常局限于单一优化视角（要么完全局部独立学习，要么完全全局集中学习）所导致的性能与效率瓶颈问题。研究背景是，在部分可观测的协作任务中，智能体需要协调行动以实现共同目标，而当前主流遵循“集中训练、分散执行”（CTDE）范式的方法，虽利用集中信息进行训练，但往往仅从单一的局部或全局视角进行优化，忽略了任务本身可能存在的层次性结构。现有方法的不足在于，这种单一视角的优化可能无法有效协调高层目标与底层执行之间的关系，例如，若个体智能体连基本任务都难以完成，团队整体目标也难以有效达成，且同时使用多个批评家（critic）信号时容易产生梯度冲突，影响学习稳定性。

因此，本文要解决的核心问题是：如何设计一种MARL框架，能够融合多层次（局部、小组级、全局）的视角进行学习，使智能体策略既能优化局部执行，又能协同实现高层团队目标，同时保证训练稳定、样本高效，并能适应智能体数量增加和任务难度提升的挑战。为此，论文提出了分层主导批评家（HLC）架构及相应的顺序训练方案。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于集中式评论家的MARL方法、多评论家学习框架以及多智能体顺序更新机制。

在基于集中式评论家的MARL方法方面，MADDPG首次在CTDE范式下应用集中式评论家以缓解环境非平稳性问题，但未解决信用分配问题。COMA通过反事实基线改进了信用分配。MAAC引入了注意力机制，而MAT和SABLE则基于Transformer架构和顺序更新。HASAC作为当前连续控制领域的SOTA，结合最大熵强化学习与顺序更新，保证了理论上的单调改进。HLC借鉴了HASAC的顺序更新思想和集中式评论家学习风格，但将其扩展为多层级的评论家结构。

在多评论家学习框架方面，多任务强化学习（MTRL）和部分MARL研究探索了单个演员对应多个评论家的方法，通常采用加权平均方式融合多个Q值或梯度，但需要调整权重超参数且可能引发梯度冲突。为此，CoNAL和PCGrad等技术被提出以缓解冲突。MA-POCA在MARL中使用了多个集中式评论家，每个评论家协调一个无重叠的智能体子群。HLC与这些方法的关键区别在于：HLC让每个演员从多个层级的评论家学习，通过顺序更新机制，每次更新后基于最新策略推理新动作并由下一级评论家评估，从而避免了梯度冲突和加权平均的局限性。

在顺序更新机制方面，HASAC、MAT等工作已证明顺序更新有助于稳定训练。HLC在此基础上，将顺序更新与层级化评论家相结合，实现了从不同层级视角（局部与全局）进行优化，从而提升了样本效率与策略鲁棒性。

### Q3: 论文如何解决这个问题？

论文通过提出一种新颖的分层引导评论家（HLC）架构和顺序训练方案来解决多智能体强化学习中局部与全局视角割裂的问题。其核心方法是在演员-评论家框架中引入多个层级的评论家，使智能体能够从不同层次（如局部、小组、全局）的视角进行学习，从而平衡个体执行与团队协作。

整体框架基于软演员-评论家（SAC）算法，关键创新在于设计了**分层引导评论家**和配套的**顺序更新机制**。引导评论家被定义为评估一组智能体的评论家，其感知范围可灵活设置，从而统一了局部评论家（仅评估自身）和集中式评论家（评估所有智能体）这两种极端情况。多个引导评论家可以按层次或并行方式组织，每个评论家使用非局部奖励（如小组特定奖励或局部奖励的组合）来鼓励协作。

架构设计包含两个主要部分：**评论家网络**和**演员网络**。评论家采用基于Transformer-Encoder的架构，可直接处理智能体的观察-动作对，无需全局状态信息，并能处理异构智能体与环境。演员网络则专门为多层次优化设计，其创新点在于结合了**混合专家风格**的子网络和**交叉注意力机制**。具体而言，输入经过一个公共特征提取器后，由多个不同的子网络（各司其职，类似专家）计算不同的表征。这些子网络输出经过嵌入（共享稠密层、正弦位置编码、层归一化）后，通过交叉注意力进行处理。同时，一个基础网络路径并行处理观察信息并生成交叉注意力所需的查询。最后，基础网络路径和交叉注意力路径的输出被拼接，并通过一个SimBa网络进行动作预测。这种设计使演员在训练早期主要依赖基础网络，而在后期训练中，交叉注意力路径能学习提供更复杂的协作行为信息。

关键技术是**双重顺序更新方案**，这是HLC的核心运作机制。首先，在更新单个演员时，多个评论家按其感知范围（评估的智能体数量）从小到大的顺序依次对其进行更新。每次策略更新后都会推理出新动作，确保每个评论家总是评估最新的策略，避免了梯度冲突问题。其次，在智能体之间也进行顺序更新：当一个智能体被所有相关评论家更新完毕后，再按顺序更新下一个智能体。由于最后一个更新总是由感知范围最大（最注重协作）的评论家完成，因此后续智能体的更新可以基于其他智能体已调整至更协作的版本。这种顺序更新机制使得智能体能够依据多个层次行动，同时促进合作。

总之，HLC通过引入可灵活分组的引导评论家概念、专为多层次优化设计的演员网络架构，以及独特的双重顺序更新训练方案，实现了从多层级视角进行高效学习，从而提升了样本效率、策略鲁棒性和整体性能。

### Q4: 论文做了哪些实验？

论文在三个多智能体协作基准任务上进行了实验：MOMAland Escort任务（包括3、5、8个智能体的变体）、新提出的Surveillance任务（4个智能体）以及PettingZoo的MPE SimpleSpread环境。实验设置遵循CTDE框架，智能体间无通信且部分可观测。对比方法选择了当前离线策略MARL的SOTA方法HASAC（单一集中式评论家）和Independent-SAC（ISAC，仅局部评论家），以验证HLC结合局部与全局视角的有效性。

主要结果显示，HLC在所有任务上均超越了基线方法。在Escort任务中，HLC在最终性能和样本效率上均优于HASAC和ISAC（见图表）。例如，ISAC依赖局部奖励能取得进展，而HASAC仅依赖全局奖励在Escort8上甚至退化为避免终止的保守策略；HLC则成功融合两者优势，取得了最佳性能。在Surveillance任务中，HLC同样展现出卓越的性能和样本效率，而ISAC性能有限，HASAC则难以解决任务。在SimpleSpread中，尽管奖励设置以全局目标为主，HLC仍表现出与HASAC竞争的性能，而未像ISAC那样性能下降。

此外，论文进行了消融研究，包括将HLC的演员网络替换为简单MLP的HLC-Simple变体，以及使用单一智能体对数概率的SingleLogp变体。结果显示，即使简化架构，HLC-Simple仍优于基线，但完整HLC设置（结合序列更新、分层演员和平均对数概率）性能最佳。在Escort8的变体实验中，HLC在部分可观测（仅观察最近2或4个邻居）和降低终止惩罚（从-500减至-320，以制造局部最优）的困难设置下，依然保持稳健性能，而HASAC在后者中快速陷入早期终止的局部最优。关键指标方面，团队奖励（如Escort中的 \(r_{team} = \sum_{i=0}^n{r^i_{scalar}}\)）和回合长度被用于评估性能，图表显示HLC能获得更高的累积奖励和更稳定的回合长度。

### Q5: 有什么可以进一步探索的点？

该论文提出的HLC方法在分层多智能体强化学习上取得了显著进展，但仍存在一些局限性和可进一步探索的方向。首先，其顺序更新机制虽提升了性能，却增加了训练时间成本，未来可通过参数共享策略（如在智能体间或子网络间部分共享参数）来优化计算效率，甚至探索异步更新或蒸馏技术来加速训练。其次，HLC目前专注于合作式任务，未来可扩展至竞争或混合场景，并研究其在多目标MARL中的应用潜力，以处理更复杂的权衡问题。此外，方法依赖于预设的层次结构，未来可探索自适应层次学习，让智能体动态调整局部与全局视角的权重。在架构方面，可结合更高效的注意力机制或图神经网络来提升群体协作的表征能力。最后，HLC在非通信环境中的鲁棒性已得到验证，但未来可引入轻量通信协议，以在部分可观测环境下进一步改善协调效率。

### Q6: 总结一下论文的主要内容

该论文提出了一种新颖的分层引导评论家（HLC）多智能体强化学习算法，旨在解决协作任务中局部与全局视角的平衡问题。其核心贡献在于设计了一种分层学习架构，通过引入引导评论家概念，从不同层级（如局部智能体与全局群体）评估行动价值，并结合顺序更新机制优化策略。方法上，HLC采用基于Transformer编码器的评论家网络，有效整合局部观察与群体行动信息，同时配合混合专家风格的行动者网络编码观测数据。实验表明，在部分可观测、无通信的协作环境中，HLC在性能与样本效率上均优于单一层次基线，并展现出良好的可扩展性与鲁棒性。该工作为多智能体系统提供了兼顾局部优化与全局协作的通用框架，具有推动复杂协作任务研究的实际意义。
