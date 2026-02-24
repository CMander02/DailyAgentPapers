---
title: "Cost-Aware Diffusion Active Search"
authors:
  - "Arundhati Banerjee"
  - "Jeff Schneider"
date: "2026-02-23"
arxiv_id: "2602.19538"
arxiv_url: "https://arxiv.org/abs/2602.19538"
pdf_url: "https://arxiv.org/pdf/2602.19538v1"
categories:
  - "cs.RO"
  - "cs.AI"
  - "cs.LG"
tags:
  - "主动搜索"
  - "多智能体系统"
  - "决策规划"
  - "扩散模型"
  - "强化学习"
  - "探索与利用"
relevance_score: 7.5
---

# Cost-Aware Diffusion Active Search

## 原始摘要

Active search for recovering objects of interest through online, adaptive decision making with autonomous agents requires trading off exploration of unknown environments with exploitation of prior observations in the search space. Prior work has proposed information gain and Thompson sampling based myopic, greedy approaches for agents to actively decide query or search locations when the number of targets is unknown. Decision making algorithms in such partially observable environments have also shown that agents capable of lookahead over a finite horizon outperform myopic policies for active search. Unfortunately, lookahead algorithms typically rely on building a computationally expensive search tree that is simulated and updated based on the agent's observations and a model of the environment dynamics. Instead, in this work, we leverage the sequence modeling abilities of diffusion models to sample lookahead action sequences that balance the exploration-exploitation trade-off for active search without building an exhaustive search tree. We identify the optimism bias in prior diffusion based reinforcement learning approaches when applied to the active search setting and propose mitigating solutions for efficient cost-aware decision making with both single and multi-agent teams. Our proposed algorithm outperforms standard baselines in offline reinforcement learning in terms of full recovery rate and is computationally more efficient than tree search in cost-aware active decision making.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自主智能体（如机器人）在未知环境中进行“主动搜索”时的决策效率问题。具体而言，它关注如何让单个或多个智能体在探索（发现新区域）和利用（基于已有信息精搜）之间取得平衡，以高效、低成本地找到所有目标物体。现有方法存在局限：基于信息增益或汤普森采样的“短视”贪婪策略往往不是最优；而能进行“前瞻”规划的算法（如蒙特卡洛树搜索）虽然效果更好，但需要构建计算昂贵的搜索树，可扩展性差，尤其当动作空间或搜索空间维度增大时。为此，论文提出利用扩散模型的序列建模能力，直接采样出平衡探索与利用的前瞻性动作序列，从而避免构建耗尽的搜索树。此外，论文还指出了此前基于扩散模型的强化学习方法在主动搜索场景中存在的“乐观偏差”问题，并提出了缓解方案。最终目标是开发一种计算高效、成本感知的决策算法（CDAS），用于单智能体或多智能体团队，在部分可观测、有噪声的环境中实现更好的目标全发现率和更快的推理速度。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕扩散模型在决策规划中的应用，特别是其在离线强化学习和多智能体协同中的进展。

首先，扩散模型作为一种强大的生成模型，已被用于序列决策。Janner等人（2022）和Ajay等人的工作将离线强化学习视为序列建模问题，训练扩散模型来生成达成目标的状态-动作序列。其中，Janner等人引入了基于奖励梯度引导的扩散模型作为规划器。Alonso等人（2024）则提出了基于条件扩散的世界模型来训练强化学习策略。这些方法主要利用扩散模型对可行状态的多模态分布进行建模的能力。

进一步地，Zhou等人（2024）提出了在模型预测控制框架下，对状态和动作进行联合建模的扩散算法，并通过奖励梯度引导进行前瞻规划，在确定性环境下的表现超越了标准强化学习基线。然而，该方法并未处理状态转移随机性（如观测噪声）带来的挑战，而这正是主动搜索场景中的核心问题。

在多智能体方面，相关研究多在集中式训练与分散式执行框架下进行。Shaoul等人（2024）将单智能体扩散模型与基于约束的规划器结合，用于多智能体路径寻找。Zhu等人（2023）则在网络中引入交叉注意力层来建模智能体间的协调。这些方法都需要一个中央控制器进行协调，与本文关注的异步、去中心化的多智能体主动搜索设置有所不同。

本文与上述工作的关系在于：它继承了利用扩散模型进行序列决策和前瞻规划的思路，但明确指出将其成功直接外推至主动搜索任务并非易事。本文重点解决了在部分可观测、存在随机性的主动搜索环境中应用扩散模型所面临的挑战（如“乐观偏差”），并针对单智能体与去中心化多智能体团队，提出了高效、成本感知的决策方案，从而填补了现有研究在异步去中心化多智能体主动搜索方面的空白。

### Q3: 论文如何解决这个问题？

本文提出了一种基于扩散模型的主动搜索方法，核心在于利用扩散模型的序列生成能力来采样前瞻动作序列，从而在无需构建昂贵搜索树的情况下平衡探索与利用。方法的关键架构与设计如下：

首先，**信念表示**采用卡尔曼滤波器更新智能体对搜索空间的后验信念，将后验均值与方差矩阵沿通道维度拼接为状态表示，以捕捉空间网格信息。

其次，**前瞻规划生成**是核心创新。为避免直接生成状态-动作序列导致的“乐观偏差”（即动作过于乐观、忽视探索），论文训练一个扩散模型来生成**条件于当前信念状态的动作序列**。具体而言，模型输入是当前信念状态，输出是未来H步的单通道图像序列，每个图像代表一个区域感知动作。这通过两个模型实现：轨迹生成模型ρ_θ学习动作序列分布，回报估计模型ν_ψ评估序列的期望累积奖励。训练时采用梯度引导的扩散采样，通过优化轨迹损失和回报损失，使生成的动作序列最大化期望的全恢复奖励。

此外，**数据生成**使用信息贪婪策略模拟多个回合，构建包含状态、动作和奖励序列的训练数据集，确保模型学习到有效的探索-利用权衡。

最后，通过**条件采样与梯度引导**，在决策时基于当前信念采样动作序列，并利用回报模型的梯度调整生成过程，实现成本感知的高效决策。该方法避免了传统树搜索的计算开销，同时在单智能体与多智能体团队中均表现出更优的全恢复率和计算效率。

### Q4: 论文做了哪些实验？

论文在主动搜索场景下进行了实验，主要围绕扩散模型生成的“前瞻性动作序列”的有效性展开。实验设置方面，作者构建了一个训练数据集 $\mathbb{D}_M$，其中包含 $M$ 个由信息贪婪策略（公式 \ref{eq:genplan_IG_action}）模拟生成的轨迹，每个轨迹的搜索向量 $\bm\beta$ 不同且目标数量 $\numtargets=1$。数据被切分为长度为前瞻视野 $H$ 的序列 $(\bms_{\itime:\itime+H}, \action_{\itime:\itime+H}, r_{\itime:\itime+H})$ 用于训练。

基准测试主要对比了标准的离线强化学习方法。主要结果是，论文提出的算法在“完全恢复率”（full recovery rate）指标上优于标准基线方法。同时，在考虑成本感知的主动决策中，该扩散模型方法在计算效率上比传统的树搜索方法更高。实验还识别并解决了先前基于扩散的强化学习方法在主动搜索中存在的“乐观偏差”问题，即模型会生成过于乐观、未能平衡探索与利用的动作序列。通过改为训练一个以智能体信念状态 $\bms_t$ 为条件、用于生成动作序列 $\bmx_{t:t+H}$ 的扩散模型，并配合梯度引导（使用一个回报估计模型 $\nu_\psi$），该方法能够有效缓解此偏差。

### Q5: 有什么可以进一步探索的点？

本文提出的扩散模型主动搜索方法虽在计算效率和目标恢复率上优于传统树搜索和离线强化学习基线，但其核心局限在于依赖预训练的扩散模型生成前瞻动作序列，这可能导致在高度动态或未知环境中的适应性不足。扩散模型对训练数据分布敏感，若环境动态与训练数据差异较大，生成的序列可能不够优化。此外，多智能体协作部分仅初步探索，未深入处理通信开销与任务分配问题。

未来可探索的方向包括：1）增强模型的在线适应能力，结合元学习或在线微调，使扩散模型能根据实时环境反馈调整序列生成；2）扩展多智能体协同机制，引入显式通信协议或分层规划，以优化团队探索效率；3）将成本感知维度进一步细化，纳入能源、时间等动态约束，实现更实用的自主决策；4）结合世界模型进行隐式环境模拟，减少对精确环境模型的依赖，提升在部分可观测场景中的鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为“成本感知扩散主动搜索”（CDAS）的新方法，用于解决自主智能体在未知环境中进行主动搜索时的探索-利用权衡问题。核心贡献在于利用扩散模型的序列建模能力，直接生成前瞻性的动作序列，从而避免了传统树搜索算法（如蒙特卡洛树搜索）因构建和更新搜索树而带来的高昂计算成本。论文指出，此前基于扩散模型的强化学习方法在主动搜索场景中可能存在“乐观偏差”，并针对单智能体和多智能体团队提出了缓解方案。实验表明，CDAS方法在离线强化学习基准测试中，在目标完全恢复率和计算效率方面均优于标准的近视贪婪策略和树搜索基线。其意义在于为资源受限的实时决策场景（如搜救、环境监测）提供了一种更高效、可扩展的规划范式。
