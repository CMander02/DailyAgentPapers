---
title: "Temporal Action Representation Learning for Tactical Resource Control and Subsequent Maneuver Generation"
authors:
  - "Hoseong Jung"
  - "Sungil Son"
  - "Daesol Cho"
  - "Jonghae Park"
  - "Changhyun Choi"
  - "H. Jin Kim"
date: "2026-02-21"
arxiv_id: "2602.18716"
arxiv_url: "https://arxiv.org/abs/2602.18716"
pdf_url: "https://arxiv.org/pdf/2602.18716v1"
categories:
  - "cs.RO"
  - "cs.AI"
tags:
  - "强化学习"
  - "混合动作空间"
  - "表示学习"
  - "机器人控制"
  - "时序依赖"
  - "对比学习"
relevance_score: 6.5
---

# Temporal Action Representation Learning for Tactical Resource Control and Subsequent Maneuver Generation

## 原始摘要

Autonomous robotic systems should reason about resource control and its impact on subsequent maneuvers, especially when operating with limited energy budgets or restricted sensing. Learning-based control is effective in handling complex dynamics and represents the problem as a hybrid action space unifying discrete resource usage and continuous maneuvers. However, prior works on hybrid action space have not sufficiently captured the causal dependencies between resource usage and maneuvers. They have also overlooked the multi-modal nature of tactical decisions, both of which are critical in fast-evolving scenarios. In this paper, we propose TART, a Temporal Action Representation learning framework for Tactical resource control and subsequent maneuver generation. TART leverages contrastive learning based on a mutual information objective, designed to capture inherent temporal dependencies in resource-maneuver interactions. These learned representations are quantized into discrete codebook entries that condition the policy, capturing recurring tactical patterns and enabling multi-modal and temporally coherent behaviors. We evaluate TART in two domains where resource deployment is critical: (i) a maze navigation task where a limited budget of discrete actions provides enhanced mobility, and (ii) a high-fidelity air combat simulator in which an F-16 agent operates weapons and defensive systems in coordination with flight maneuvers. Across both domains, TART consistently outperforms hybrid-action baselines, demonstrating its effectiveness in leveraging limited resources and producing context-aware subsequent maneuvers.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自主机器人在资源受限环境下进行战术决策时面临的核心挑战：如何有效建模离散资源使用与连续机动动作之间的因果依赖关系和多模态特性。现有基于强化学习的混合动作空间方法通常忽视这两个关键方面，导致策略缺乏战术灵活性。具体而言，论文提出TART框架，通过学习时序动作表征来统一资源控制与后续机动生成，使智能体能够理解资源消耗如何约束未来动作选择（因果依赖），并在动态环境中针对同一资源决策生成多种合理的后续机动模式（多模态）。该方法通过基于互信息的对比学习目标来捕获资源与机动交互中的时序依赖，并将学习到的表征量化为离散的战术模式代码本，用以指导策略生成上下文感知且时序一致的行为。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕混合动作空间强化学习、强化学习中的表征学习以及行为多模态建模展开。

在**混合动作空间强化学习**方面，已有工作将问题建模为参数化动作马尔可夫决策过程（PAMDP），并提出了相应的Q学习扩展（如Masson等人和Xiong等人的工作）和演员-评论员方法（如Hausknecht等人和Fan等人的工作）。近期，Li等人提出的HyAR利用条件变分自编码器（cVAE）嵌入单步混合动作以减少冗余。然而，这些方法未能充分捕捉资源使用与后续机动之间的**长期战术依赖关系**，而本文的TART框架正是为了建模这种时序因果依赖而提出。

在**强化学习表征学习**方面，现有研究多集中于通过对比学习等自监督目标学习紧凑的状态表征以提升样本效率（如Oord等人的CPC、Allshire等人的LASER）。也有工作学习状态-动作对的嵌入，例如TACO通过最大化状态-动作对与未来状态的互信息来获取动作表征。这些方法为本文的时序动作表征学习提供了基础，但并未专门针对混合动作空间中离散资源决策与连续机动分布之间的**时序耦合**进行建模。

在**行为多模态建模**方面，相关研究通过向量量化（VQ）将轨迹离散化到码本中以鼓励多模态行为（如van den Oord等人的VQ-VAE、Luo等人的Action-Q）。本文借鉴了这种离散化思想，但将其应用于学习到的**战术模式表征**，使得策略能基于不同的量化编码生成多模态且时序连贯的机动行为，从而解决了先前工作在快速演变场景中忽视战术决策多模态性的问题。

### Q3: 论文如何解决这个问题？

论文提出的TART框架通过一种新颖的时序动作表征学习方法来解决混合动作空间中资源控制与后续机动动作之间的因果依赖和多模态决策问题。其核心方法、架构设计和关键技术如下：

**核心方法与架构设计：**
TART框架的核心是学习一个离散-连续（混合）的战术表征，该表征用于条件化策略以产生多模态的混合动作。整体架构包含表征学习和策略生成两个紧密耦合的部分。首先，框架通过互信息目标学习状态和动作的嵌入表示，旨在捕捉资源使用（离散动作）与后续机动序列（连续动作）之间的时序依赖关系。具体而言，它定义了状态编码器φ、离散动作编码器ψ_d和连续动作编码器ψ_c，将原始状态和动作映射到嵌入空间。其核心目标是最大化一个固定时间窗口K内的互信息J_TART = I(u_{t:t+K-1,c}; [z_{t-K+1:t}, u_{t,d}])，这迫使学习到的表征能够将历史状态（包含当前状态）和当前的离散决策与未来的连续机动序列联系起来，从而促进时序连贯的控制。

**关键技术：**
1.  **基于对比学习的互信息最大化**：由于直接计算互信息难以处理，TART采用InfoNCE损失函数作为其可处理的下界进行优化。它设计了上下文投影器H和未来投影器P，分别将“历史状态序列与当前离散动作”的上下文和“未来连续动作序列”映射到公共嵌入空间。通过对比学习，使正样本对（同一时间步的上下文与未来动作嵌入）相似，而与批次内其他时间步或轨迹的负样本对相异，从而有效地对齐时序状态-动作表征。
2.  **战术模式的向量量化**：为了利用对比学习得到的聚类动作表征，TART引入了一个向量量化（VQ）码本。将上下文嵌入h_t通过最近邻搜索量化到码本中的一个离散条目q_t（即战术模式）。这个离散的战术模式作为条件信息，用于指导后续连续机动动作的生成，从而捕捉重复出现的战术模式并实现多模态、时序一致的行为。
3.  **战术引导的混合策略分解**：策略被分解为离散执行器和连续执行器：π(a_{t,d}, a_{t,c}|s_t, q_t) = π_d(a_{t,d}|s_t) · π_c(a_{t,c}|s_t, a_{t,d}, q_t)。在推理时，先由离散策略选择资源控制动作a_{t,d}，然后基于当前状态、该离散动作以及量化得到的战术模式q_t，由连续策略生成具体的机动动作a_{t,c}。这种分解明确建模了离散决策对连续动作的因果影响。
4.  **统一的训练流程**：训练分为两个阶段。预热阶段使用探索性数据单独训练表征模块（编码器、投影器、码本）。主循环阶段则交替进行表征学习和策略优化（采用PPO算法）。整体损失函数结合了PPO策略损失、InfoNCE对比损失和VQ量化损失，通过梯度更新联合优化，但码本本身不接收来自RL损失的梯度，以保持其表征的稳定性。

总之，TART通过互信息驱动的对比学习捕获资源与机动间的时序依赖，通过向量量化将学习到的模式离散化为可解释的战术代码，并以此条件化一个分解式的混合策略，最终实现了在资源受限下进行多模态、上下文感知的序列决策。

### Q4: 论文做了哪些实验？

论文在两个资源受限的混合动作环境中进行了实验：迷宫导航和空战模拟。实验设置方面，迷宫导航任务基于POGEMA扩展，包含简单、中等和困难三种难度场景，地图尺寸分别为10x10和20x20，困难场景包含动态障碍物。智能体拥有两种特殊动作（穿透和加速），每局限用两次。空战环境基于高保真模拟器，模拟F-16战机，配备有限导弹和防御系统，同样分为三个难度等级，对手能力逐级增强。

基准测试中，论文比较了TART与多种混合动作强化学习基线方法（PADDPG、PDQN、HPPO、HyAR）以及两个消融版本（去除对比损失或向量量化损失）。评估指标包括成功率、到达目标时间（TTG）/消灭对手时间（TTE）、占用覆盖率（迷宫）和每次消灭消耗导弹数（SPE）。

主要结果显示，TART在所有场景中均取得最佳性能。在迷宫导航中，TART在困难场景的成功率达到72.8%，显著高于最佳基线HyAR的60.4%，且TTG更短、路径更高效。在空战任务中，TART在困难场景的成功率为76.8%，优于基线的61.8%-65.4%，同时保持了较低的SPE，表明其能更有效地利用有限资源。消融实验证实了对比学习和向量量化损失的关键作用，去除任一组件都会导致性能下降。定性分析进一步显示，TART能学习到协调的战术模式，如在迷宫中使用穿透动作解决死锁，在空战中协调进攻与防御动作。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于实验场景相对有限，主要集中于迷宫导航和空战模拟两个领域，其方法在更复杂、动态性更强的开放环境（如长期自主机器人操作）中的泛化能力有待验证。此外，框架依赖于对比学习与量化表征，其训练稳定性和对超参数的敏感性可能是一个实践挑战。

未来方向可从以下几点深入探索：一是将TART框架扩展到涉及多智能体协作与对抗的场景，研究资源控制与机动生成的协同策略。二是探索所学战术表征的可解释性，使其能为人类操作员提供决策洞察。三是研究如何在线适应或增量学习新的战术模式，以应对非平稳环境。最后，可考虑将该时序动作表征学习范式与基于模型的规划或分层强化学习结合，以处理更长视距的战术推理任务。

### Q6: 总结一下论文的主要内容

这篇论文提出了TART（Temporal Action Representation learning for Tactical resource control）框架，旨在解决自主机器人在资源受限（如能量、感知）场景下的战术决策问题。其核心贡献是设计了一种基于对比学习和互信息目标的时间动作表征学习方法，以显式捕获离散资源控制（如使用武器、开启传感器）与后续连续机动动作（如飞行轨迹）之间的因果依赖关系和时序模式。该框架将学习到的表征量化为离散码本，用于条件化策略，从而能生成多模态且时间连贯的战术行为。论文在迷宫导航和高保真空战模拟（F-16战机）两个领域验证了TART的有效性，结果表明其性能优于现有的混合动作空间基线方法。这项工作的意义在于为复杂动态场景中资源与动作的联合优化提供了新的表征学习思路，提升了智能体在快节奏演化环境下的战术决策能力。
