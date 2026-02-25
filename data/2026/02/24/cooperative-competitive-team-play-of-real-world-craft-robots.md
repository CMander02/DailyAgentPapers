---
title: "Cooperative-Competitive Team Play of Real-World Craft Robots"
authors:
  - "Rui Zhao"
  - "Xihui Li"
  - "Yizheng Zhang"
  - "Yuzhen Liu"
  - "Zhong Zhang"
  - "Yufeng Zhang"
  - "Cheng Zhou"
  - "Zhengyou Zhang"
  - "Lei Han"
date: "2026-02-24"
arxiv_id: "2602.21119"
arxiv_url: "https://arxiv.org/abs/2602.21119"
pdf_url: "https://arxiv.org/pdf/2602.21119v1"
categories:
  - "cs.RO"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "强化学习"
  - "机器人"
  - "Sim2Real迁移"
  - "合作与竞争"
  - "分布式学习"
  - "策略训练"
relevance_score: 7.5
---

# Cooperative-Competitive Team Play of Real-World Craft Robots

## 原始摘要

Multi-agent deep Reinforcement Learning (RL) has made significant progress in developing intelligent game-playing agents in recent years. However, the efficient training of collective robots using multi-agent RL and the transfer of learned policies to real-world applications remain open research questions. In this work, we first develop a comprehensive robotic system, including simulation, distributed learning framework, and physical robot components. We then propose and evaluate reinforcement learning techniques designed for efficient training of cooperative and competitive policies on this platform. To address the challenges of multi-agent sim-to-real transfer, we introduce Out of Distribution State Initialization (OODSI) to mitigate the impact of the sim-to-real gap. In the experiments, OODSI improves the Sim2Real performance by 20%. We demonstrate the effectiveness of our approach through experiments with a multi-robot car competitive game and a cooperative task in real-world settings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何利用多智能体深度强化学习（RL）高效训练真实世界中的集体机器人，并将学习到的策略成功迁移到实际物理系统这一核心问题。研究背景是，尽管多智能体RL在游戏AI（如《星际争霸》）中取得了超人表现，但在机器人领域，尤其是在涉及多机器人协作与竞争的复杂场景中，其应用仍面临巨大挑战。现有方法的不足主要体现在两个方面：一是训练效率问题，为多机器人系统手动设计控制系统不切实际，而传统RL在复杂多智能体环境中训练效率低下；二是仿真到现实（Sim2Real）的迁移难题，由于无法构建与真实世界完全一致的仿真环境，存在仿真与现实之间的动态特性差异（即Sim2Real鸿沟），这严重影响了学习策略在真实机器人上的部署性能。先前工作多集中于虚拟环境，或使用域随机化等方法，但这些方法存在可扩展性问题和可能导致策略过于保守的局限。

因此，本文要解决的核心问题是：如何构建一个完整的多机器人AI系统（包括仿真、学习框架和物理机器人），并开发有效的训练与迁移技术，以实现真实世界中多机器人协作-竞争团队策略的高效学习与鲁棒部署。具体而言，论文提出了引导式RL来提高学习效率，并创新性地提出了“分布外状态初始化”（OODSI）方法，专门用于缓解多智能体动态特性中的Sim2Real差异，从而提升策略在真实环境中的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多智能体强化学习（MARL）方法、仿真到现实（Sim2Real）迁移技术，以及面向机器人应用的引导式强化学习。

在**多智能体强化学习方法**方面，已有大量工作专注于开发合作或竞争场景下的智能体策略，例如基于值分解或策略梯度的算法。本文在此基础上，构建了一个包含仿真、分布式学习框架和实体机器人的完整系统，并专门针对该平台评估了高效的训练技术，以同时处理合作与竞争任务。

在**仿真到现实迁移技术**领域，现有研究常通过域随机化或系统辨识来缩小仿真与现实间的差距。本文则创新性地提出了“分布外状态初始化”（OODSI）方法，其核心是通过修改初始状态分布来增强策略对现实世界不确定性的鲁棒性。这与Florensa等人通过逐步增加初始状态与目标距离来训练机器人的方法有相似思路，但本文的OODSI旨在直接缓解Sim2Real差距带来的影响，实验证明其将迁移性能提升了20%。

在**机器人应用的引导式强化学习**方面，已有工作探索利用专家演示、自然语言或程序等先验知识来加速策略学习。本文的研究也属于这一范畴，其目标是整合额外知识以提高学习效率与现实部署成功率，但具体实现是通过所提出的OODSI机制来引导训练过程，使其更适应真实物理环境。

### Q3: 论文如何解决这个问题？

论文通过提出两项核心创新来解决多智能体强化学习在真实机器人应用中的高效训练和仿真到现实迁移难题。整体框架基于一个包含仿真环境、分布式学习框架和物理机器人组件的综合机器人系统，并采用集中训练分散执行的架构。

第一项创新是**基于动作掩码的引导式强化学习**，旨在应对真实机器人约束下的高效学习挑战。该方法通过规则化的子程序规划器，在给定状态下屏蔽无效或不有利于下游任务的动作，从而缩小智能体的探索空间。例如，在机器人工艺竞技场中，移动至斜坡或移出方块需要特定朝向，动作掩码能引导机器人高效探索。这种设计将低层细节（如拾取方块）交由环境处理，使RL智能体能专注于学习高层策略，结合基于规则的局部规划器与数据驱动的RL策略，高效学习复杂任务。

第二项创新是**分布外状态初始化（OODSI）**，专门解决多智能体仿真到现实的差距。由于训练环境（基于pyBullet）与测试环境（基于Gazebo和真实机器人）在动作执行同步性和连续性上存在差异，导致动态特性不同，产生分布外状态。OODSI方法将从测试环境中收集的OOD状态添加到训练过程的初始状态分布中，使智能体学习针对这些状态的鲁棒策略。其核心思想是通过从OOD状态到下一个OOD状态的轨迹增长，顺序组合局部稳定策略，从而提升智能体在现实遇到未知状态时的应对能力。

在系统实现上，智能体策略由多层感知机表示，同队智能体共享网络权重以提升效率。采用大规模分布式训练框架，通过Kubernetes部署学习器节点和执行器节点并行收集样本，使用近端策略优化算法更新权重，并裁剪梯度范数以稳定训练。对于竞争性任务，采用自博弈机制：当一队达到成功率阈值时暂停训练并固定其策略，使另一队将其视为环境的一部分进行学习，随后交替角色，促使双方策略协同进化。

实验表明，OODSI将仿真到现实的性能提升了20%，在合作建造字符和两队竞争建造任务中均显著提高了在Gazebo环境中的成功率。结合动作掩码和OODSI的方法，有效解决了多智能体在真实机器人场景中的策略迁移与鲁棒性挑战。

### Q4: 论文做了哪些实验？

论文实验主要围绕一个由机器人小车、方块和斜坡组成的真实机器人竞技场展开，设计了协作与竞争两类任务。协作任务要求机器人合作搭建“TPX”字符；竞争任务则将机器人分为两队，竞争使用有限资源搭建双层结构。

实验设置上，研究使用pyBullet仿真环境进行训练，并在更真实的Gazebo仿真中测试性能。为提高训练效率，采用了名为TLeague的分布式强化学习框架。实验首先对动作掩码进行了消融研究，验证了其通过引导RL提升训练效率的作用：在两项任务中，训练步数均为3×10^6步，带有动作掩码的方法能显著加快收敛速度并减少训练时间。

核心实验是比较不同方法在Sim2Real（仿真到现实）迁移中的性能，对比了PPO、PPO+动态随机化（DR）、PPO+OODSI以及PPO+DR+OODSI四种方法。所有模型仅在pyBullet中训练，在Gazebo中评估。DR以30%概率用停止动作随机替换动作以模拟执行失败，提升鲁棒性；OODSI则利用在Gazebo中收集的轨迹片段构建初始状态集用于训练。每种方法使用3个不同随机种子训练模型，各在Gazebo中测试10轮，最终计算30轮的平均成功率。

关键数据指标如下：在搭建字符任务中，PPO+DR+OODSI组合方法相比基线PPO，成功率提高了30%；在双队竞争任务中，该组合方法的成功率提升了23.34%。结果表明，DR和OODSI均能提升Sim2Real性能，而OODSI的加入（实验称可提升20%的Sim2Real性能）能帮助智能体学习对抗仿真与现实差距的鲁棒策略。此外，实验还观察到了智能体习得的高级策略，如“阻挡”和“偷取”方块行为，并在Gazebo和真实世界中均得到了验证。

### Q5: 有什么可以进一步探索的点？

该论文在现实世界多机器人协同与竞争任务中验证了MARL和Sim2Real方法的有效性，但仍存在一些局限性和值得深入探索的方向。首先，论文提出的OODSI方法主要关注状态初始化的分布差异，但Sim2Real差距还体现在动力学模型误差、传感器噪声和延迟等多个维度，未来可研究更全面的域随机化或系统辨识方法以覆盖这些因素。其次，实验集中于相对结构化的手工任务（如竞速游戏），未来可探索更开放、动态的环境，例如部分可观测场景下的长期协作规划，或引入人类专家进行人机混合团队训练。此外，当前工作未充分讨论多智能体策略的可解释性与安全性，这在物理机器人部署中至关重要；可结合课程学习、分层强化学习或引入符号约束来提升策略的鲁棒性和可信度。最后，分布式训练框架的效率与扩展性仍有优化空间，例如探索异步学习、通信高效的算法，或利用离线强化学习数据来加速在线训练。这些方向有望推动MARL从受限实验场景走向更复杂的现实应用。

### Q6: 总结一下论文的主要内容

该论文针对多智能体深度强化学习在真实机器人集体协作与竞争任务中的应用挑战，提出了一套完整的系统框架与训练方法。核心问题在于如何高效训练多机器人策略并实现从仿真到现实的有效迁移。作者首先构建了一个包含仿真环境、分布式学习框架和实体机器人组件的综合机器人系统，并在此基础上设计并评估了适用于协作与竞争策略的强化学习技术。为应对仿真与现实间的差异，论文创新性地提出了“分布外状态初始化”方法，以减小仿真到现实的性能差距。实验表明，该方法在真实多机器人汽车竞争游戏和协作任务中表现有效，并将仿真到现实的性能提升了20%。这项工作的主要贡献在于提供了一个可操作的平台与迁移技术，推动了多智能体强化学习在复杂现实机器人任务中的实用化进程。
