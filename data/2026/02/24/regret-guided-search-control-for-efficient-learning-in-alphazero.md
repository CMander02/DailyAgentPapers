---
title: "Regret-Guided Search Control for Efficient Learning in AlphaZero"
authors:
  - "Yun-Jui Tsai"
  - "Wei-Yu Chen"
  - "Yan-Ru Ju"
  - "Yu-Hung Chang"
  - "Ti-Rong Wu"
date: "2026-02-24"
arxiv_id: "2602.20809"
arxiv_url: "https://arxiv.org/abs/2602.20809"
pdf_url: "https://arxiv.org/pdf/2602.20809v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "强化学习"
  - "AlphaZero"
  - "搜索控制"
  - "学习效率"
  - "蒙特卡洛树搜索"
  - "决策"
  - "游戏AI"
relevance_score: 6.5
---

# Regret-Guided Search Control for Efficient Learning in AlphaZero

## 原始摘要

Reinforcement learning (RL) agents achieve remarkable performance but remain far less learning-efficient than humans. While RL agents require extensive self-play games to extract useful signals, humans often need only a few games, improving rapidly by repeatedly revisiting states where mistakes occurred. This idea, known as search control, aims to restart from valuable states rather than always from the initial state. In AlphaZero, prior work Go-Exploit applies this idea by sampling past states from self-play or search trees, but it treats all states equally, regardless of their learning potential. We propose Regret-Guided Search Control (RGSC), which extends AlphaZero with a regret network that learns to identify high-regret states, where the agent's evaluation diverges most from the actual outcome. These states are collected from both self-play trajectories and MCTS nodes, stored in a prioritized regret buffer, and reused as new starting positions. Across 9x9 Go, 10x10 Othello, and 11x11 Hex, RGSC outperforms AlphaZero and Go-Exploit by an average of 77 and 89 Elo, respectively. When training on a well-trained 9x9 Go model, RGSC further improves the win rate against KataGo from 69.3% to 78.2%, while both baselines show no improvement. These results demonstrate that RGSC provides an effective mechanism for search control, improving both efficiency and robustness of AlphaZero training. Our code is available at https://rlg.iis.sinica.edu.tw/papers/rgsc.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决强化学习（特别是AlphaZero框架）中学习效率低下的问题。研究背景是，尽管强化学习智能体在诸多领域取得了卓越性能，但其学习效率远低于人类。人类在学习复杂任务（如围棋）时，能够通过反复回顾和纠正错误的关键状态来快速提升，而典型的RL智能体（如AlphaZero）则需要从初始状态开始进行海量的自我对弈，对所有状态进行均匀更新，导致学习过程缓慢且数据利用率低。

现有方法（如Go-Exploit）尝试通过“搜索控制”来改进，即从过往轨迹或搜索树中采样状态作为新的起始点，而非总是从初始状态开始。然而，这些方法存在一个关键不足：它们将所有存储的状态视为同等重要，忽视了不同状态对学习进步的贡献差异。实际上，许多状态可能已被掌握，只有少数关键状态（如智能体评估与实际结果偏差大的错误状态）才是改进的关键。这种均匀采样策略在训练后期尤其低效，因为错误变得罕见且难以捕捉。

因此，本文要解决的核心问题是：如何更智能地识别和优先选择那些对学习最有价值的状态进行重点训练，从而模拟人类高效学习模式，显著提升AlphaZero的训练效率和最终性能。为此，论文提出了“后悔引导的搜索控制”方法，通过一个后悔网络来识别高后悔状态（即智能体评估与实际结果差异最大的状态），并将其存储在优先缓冲池中用于重复训练，从而引导智能体集中纠正其最严重的错误。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕搜索控制（search control）方法及其在强化学习（尤其是AlphaZero框架）中的应用展开，可分为以下几类：

**1. 通用搜索控制与重启分布方法**：搜索控制的概念最早源于Dyna框架，通过从非初始状态重启来加速学习。后续工作如Go-Explore通过维护有潜力的状态数据库，在稀疏奖励环境中实现高效探索；Jump-Start Reinforcement Learning (JSRL) 从专家轨迹中采样初始状态，提升早期训练效率。此外，有研究形式化定义了重启分布ρ(s)，并提出均匀重启和基于时序差分误差的优先级重启策略。这些方法为本文提供了理论基础，但多关注任务层面的课程学习，而本文则专注于同一游戏内的关键状态识别。

**2. AlphaZero框架中的搜索控制改进**：针对AlphaZero训练效率低的问题，已有工作尝试引入搜索控制。例如KataGo通过随机走步或修改历史状态生成起始状态；Go-Exploit则系统性地研究重启方法，维护来自自对弈轨迹或MCTS节点的状态缓冲区，并均匀采样作为起点。Go-Exploit是本文最直接的基线，但其均匀采样忽略了状态的学习潜力差异。本文提出的RGSC在此基础上引入遗憾网络，优先选择高遗憾状态（即代理评估与实际结果差异大的状态），从而更针对性地提升学习效率。

**3. 基于遗憾的优先级机制**：在课程学习领域，已有研究基于估计的遗憾自适应采样训练关卡，以聚焦学习潜力高的任务。本文借鉴了这一思想，但将其应用于状态层面，通过遗憾网络量化每个状态的“错误程度”，并构建优先级遗憾缓冲区进行状态重用。这与Go-Exploit的均匀采样形成核心区别，使得训练更集中于具有高学习价值的区域。

综上，本文与相关工作的关系在于继承并融合了搜索控制、AlphaZero改进和遗憾优先级等思路，其创新点在于首次在AlphaZero中引入基于遗憾的优先级搜索控制机制，从而更高效地利用自对弈和搜索树中的数据，提升训练效率和最终性能。

### Q3: 论文如何解决这个问题？

论文通过提出“后悔引导的搜索控制”（RGSC）框架来解决AlphaZero学习效率低下的问题。其核心思想是让智能体像人类一样，专注于从过去犯错的“高后悔值”状态重新开始自我对弈，而非总是从初始状态开始，从而加速学习。

整体框架在AlphaZero基础上扩展了三个关键组件：**后悔网络**、**优先后悔缓冲区**和**基于后悔的搜索控制机制**。主要工作流程是：在自我对弈和蒙特卡洛树搜索过程中，利用后悔网络识别出高后悔值状态（即智能体评估与实际结果差异大的状态），将其存入优先后悔缓冲区；随后，在开始新的自我对弈时，以一定概率从缓冲区中采样这些状态作为起始点，引导训练聚焦于未掌握的局面。

核心方法包含以下创新点：
1.  **后悔的定义与计算**：将状态 \(s_t\) 的后悔值 \(\mathcal{R}(s_t)\) 定义为从该状态到终局的所有后续状态中，MCTS选择动作的价值与最终结果差异的平方均值。这捕捉了评估错误对结局的长期累积影响。
2.  **基于排序的后悔网络**：直接预测精确的后悔值面临数据分布极不平衡（高后悔状态稀少）和目标非平稳（一旦重访，后悔值迅速下降）的挑战。为此，论文创新性地采用**排序学习目标**。后悔网络输出一个未归一化的排序分数 \(\gamma_s\)，目标是通过优化损失函数 \(\mathcal{L}_rank\)，使网络对高后悔状态赋予更高的采样概率 \(\rho(s \mid \mathcal{S})\)，从而确保能识别出最具学习潜力的状态，而非预测其具体数值。
3.  **双网络结构**：为了兼顾识别与定量评估，后悔网络由**后悔排序网络**和**后悔价值网络**共同组成。排序网络负责从候选状态中识别出高后悔状态，价值网络则估计这些状态的近似后悔值，用于缓冲区的管理与采样。
4.  **优先后悔缓冲区**：这是一个容量固定的缓冲区，用于存储高后悔状态。新状态仅当其后悔值高于缓冲区中最低后悔值时才会被加入，确保了缓冲区始终维持高质量。采样时采用基于后悔值的softmax分布进行优先采样。
5.  **动态更新机制**：当从缓冲区采样状态重启对弈后，会基于新对弈轨迹计算该状态的后悔值，并使用指数移动平均更新缓冲区中的旧值。这使得一旦智能体掌握了某个状态，其后悔值会逐渐衰减，被采样的概率也随之降低，模拟了人类通过反复练习直至掌握的学习过程。

通过这一系列设计，RGSC使AlphaZero能够主动、高效地挖掘并利用训练过程中产生的“错误”信号，显著提升了学习效率和最终策略的鲁棒性。

### Q4: 论文做了哪些实验？

论文进行了四组主要实验。首先，在一个n层稀疏奖励二叉树的玩具环境中，对比了无搜索控制、随机采样和基于遗憾值采样的方法，结果显示基于遗憾的方法获得了更高的平均奖励，验证了其有效性。

在核心实验中，RGSC与AlphaZero（无搜索控制）和Go-Exploit（均匀采样）在9x9围棋、10x10黑白棋和11x11 Hex三种棋盘游戏上进行了对比。实验设置采用3块残差网络，每步200次MCTS模拟，训练300轮。为确保公平，固定每轮收集的训练状态数（围棋16万，其他12万）。主要结果以Elo评分衡量：RGSC最终在三种游戏上平均超越AlphaZero 77 Elo，超越Go-Exploit 89 Elo。具体而言，在9x9围棋上分别超越76和96 Elo；在10x10黑白棋上超越70和50 Elo；在11x11 Hex上超越84和122 Elo。此外，与开源强程序（如KataGo）对弈的胜率也一致显示RGSC最优，例如在9x9围棋上达到53.6%的胜率，高于AlphaZero的45.5%和Go-Exploit的49.5%。

第三组实验从一个已训练好的15块网络围棋模型（对KataGo胜率69.3%）开始继续训练40轮。结果RGSC将胜率进一步提升至78.2%，而两个基线方法均无显著改善。

最后，论文分析了遗憾值网络与遗憾排序网络在识别高遗憾状态上的差异。实验表明，排序网络选出的状态具有更高的真实遗憾值，尤其在训练后期能持续聚焦于困难状态，从而带来更优的性能。此外，对优先遗憾缓冲区（PRB）的分析显示，其中状态的遗憾值随着训练逐渐降低，证实了模型通过重复访问这些状态修正了错误。

### Q5: 有什么可以进一步探索的点？

本文提出的RGSC方法虽然有效，但仍存在一些局限性和可进一步探索的方向。首先，该方法主要针对完美信息、确定性环境的棋盘游戏，其在高维连续状态空间（如机器人控制）或非完美信息博弈（如扑克）中的泛化能力尚未验证。其次，后悔值的估计依赖于蒙特卡洛树搜索（MCTS）的模拟结果，这在计算上较为昂贵，且可能受模拟次数限制而产生偏差。此外，论文中使用的后悔排名网络虽优于价值网络，但其训练目标（如成对排名损失）可能并非最优，未来可探索更高效的表示学习或对比学习方法来提升状态选择的准确性。

未来研究可以从以下几个方向深入：一是将RGSC框架扩展到更广泛的强化学习领域，如结合基于模型的RL或离线RL，研究其在样本效率上的提升。二是优化后悔估计机制，例如开发轻量化的后悔预测模型，或利用不确定性估计（如贝叶斯神经网络）来区分认知不确定性与偶然不确定性，从而更精准地定位“可学习的”高后悔状态。三是探索动态的搜索控制策略，不仅基于后悔值，还结合课程学习或元学习，自适应地调整状态重启的分布，以平衡探索与利用。最后，可研究多智能体场景下的后悔引导，例如在对抗性环境中，如何利用双方策略的后悔来协调自我对弈的改进。

### Q6: 总结一下论文的主要内容

该论文针对强化学习智能体学习效率远低于人类的问题，提出了一种名为“后悔引导搜索控制”的方法来改进AlphaZero。核心问题是传统自对弈训练从初始状态开始效率低下，而人类善于从错误中快速学习。RGSC通过引入一个后悔网络来识别高后悔状态，即智能体评估与实际结果差异最大的棋局位置，这些状态从自对弈轨迹和蒙特卡洛树搜索节点中收集，并存储在一个优先缓冲池中作为新的训练起点。实验在9x9围棋、10x10黑白棋和11x11六边形棋上进行，结果表明RGSC在Elo评分上平均优于AlphaZero和Go-Exploit基准方法，且在已训练模型上能进一步提升对抗KataGo的胜率。主要结论是RGSC通过有效引导搜索控制，显著提高了AlphaZero的训练效率和鲁棒性。
