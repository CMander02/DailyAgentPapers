---
title: "Multi-agent deep reinforcement learning with centralized training and decentralized execution for transportation infrastructure management"
authors:
  - "M. Saifullah"
  - "K. G. Papakonstantinou"
  - "A. Bhattacharya"
  - "S. M. Stoffels"
  - "C. P. Andriotis"
date: "2024-01-23"
arxiv_id: "2401.12455"
arxiv_url: "https://arxiv.org/abs/2401.12455"
pdf_url: "https://arxiv.org/pdf/2401.12455v2"
categories:
  - "cs.MA"
  - "cs.AI"
  - "cs.LG"
  - "eess.SY"
tags:
  - "多智能体系统"
  - "强化学习"
  - "集中训练分散执行"
  - "深度强化学习"
  - "决策优化"
  - "约束处理"
  - "基准环境"
relevance_score: 7.5
---

# Multi-agent deep reinforcement learning with centralized training and decentralized execution for transportation infrastructure management

## 原始摘要

Life-cycle management of large-scale transportation systems requires determining a sequence of inspection and maintenance decisions to minimize long-term risks and costs while dealing with multiple uncertainties and constraints that lie in high-dimensional spaces. Traditional approaches have been widely applied but often suffer from limitations related to optimality, scalability, and the ability to properly handle uncertainty. Moreover, many existing methods rely on unconstrained formulations that overlook critical operational constraints. We address these issues in this work by casting the optimization problem within the framework of constrained Partially Observable Markov Decision Processes (POMDPs), which provide a robust mathematical foundation for stochastic sequential decision-making under observation uncertainties, in the presence of risk and resource limitations. To tackle the high dimensionality of state and action spaces, we propose DDMAC-CTDE, a Deep Decentralized Multi-Agent Actor-Critic (DDMAC) reinforcement learning architecture with Centralized Training and Decentralized Execution (CTDE). To demonstrate the utility of the proposed framework, we also develop a new comprehensive benchmark environment representing an existing transportation network in Virginia, U.S., with heterogeneous pavement and bridge assets undergoing nonstationary degradation. This environment incorporates multiple practical constraints related to budget limits, performance guidelines, traffic delays, and risk considerations. On this benchmark, DDMAC-CTDE consistently outperforms standard transportation management baselines, producing better policies. Together, the proposed framework and benchmark provide (i) a scalable, constraint-aware methodology, and (ii) a realistic, rigorous testbed for comprehensive evaluation of Deep Reinforcement Learning (DRL) for transportation infrastructure management.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大规模交通基础设施全生命周期管理中，在多重不确定性和高维约束下进行序列化检测与维护决策的优化难题。研究背景是，全球许多国家的基础设施面临老化与资金短缺的严峻挑战，例如美国弗吉尼亚州有大量桥梁已超设计寿命，而预计更换成本远超可用资金。传统方法（如遗传算法、基于风险的启发式方法等）虽广泛应用，但存在明显不足：它们往往难以在优化性、可扩展性和不确定性处理之间取得平衡；许多方法采用无约束优化形式，忽略了实际运营中的关键约束（如预算、性能指南、交通延误和风险限制）；并且现有方法多基于静态假设，难以处理基础设施非平稳退化等动态随机特性。

针对这些不足，本文的核心问题是：如何构建一个既能处理高维状态与动作空间、部分可观测性、多重操作约束，又能保证计算可扩展性的决策框架。为此，论文将问题建模为约束部分可观测马尔可夫决策过程（Constrained POMDPs），以提供严格的随机序贯决策数学基础。为解决维数灾难，论文提出了DDMAC-CTDE——一种采用集中训练与分散执行范式的深度分散多智能体演员-评论家强化学习架构。该架构通过分散的智能体（代表各个基础设施组件）处理本地信息，同时利用集中式的评论家进行训练，从而在保持梯度信息流的同时大幅提升可扩展性。此外，论文还创建了一个基于美国弗吉尼亚州真实交通网络的综合基准环境，以验证所提框架在异构资产、非平稳退化及多种现实约束下的有效性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**传统优化与决策方法**、**深度强化学习（DRL）方法**以及**多智能体深度强化学习（MADRL）方法**。

在**传统优化与决策方法**方面，交通基础设施管理长期依赖于基于马尔可夫决策过程（MDP）或部分可观测马尔可夫决策过程（POMDP）的序列决策方法。然而，这些方法在处理高维状态/动作空间、多重不确定性以及实际运营约束（如预算、风险）时，常面临最优性、可扩展性不足的局限，且许多现有方法采用无约束形式化，忽略了关键约束。

在**深度强化学习（DRL）方法**中，价值基方法（如DQN）和策略基方法（如策略梯度）被用于解决高维问题。**演员-评论员（Actor-Critic）方法**（如PPO、A3C、DDPG）结合了二者优势，在稳定性和收敛性上表现更好，成为主流。本文提出的DDMAC架构本质上属于此类，但其创新在于针对多智能体场景进行了专门设计。

在**多智能体深度强化学习（MADRL）方法**中，已有研究将MADRL应用于基础设施系统管理，但通常仅在包含数十个智能体或组件的相对简单环境中进行验证。本文与这些工作的核心区别在于：1) **问题规模与复杂性**：本文处理的是包含近百个异构组件、具有非平稳退化过程且嵌入多种实际约束（预算、性能指南、交通延误、风险）的真实复杂场景；2) **方法框架**：本文提出了**DDMAC-CTDE**，即采用**集中训练与分散执行（CTDE）** 范式的深度去中心化多智能体演员-评论员架构。这使其能够有效应对传统POMDP点求解器（如基于点的算法）在大规模问题上计算不切实际的挑战，同时通过CTDE机制协调多智能体决策，以处理高维空间和约束条件。此外，本文还开发了一个新的综合性基准测试环境，为评估DRL在交通基础设施管理中的应用提供了更现实、更严谨的测试平台。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为DDMAC-CTDE的新型深度强化学习架构来解决大规模交通基础设施管理中高维状态和动作空间带来的组合复杂性、计算可扩展性以及实际约束处理等问题。其核心方法是将优化问题建模为约束部分可观测马尔可夫决策过程（Constrained POMDPs），并采用集中训练与分散执行（CTDE）范式的多智能体深度强化学习。

整体框架基于去中心化部分可观测马尔可夫决策过程（Dec-POMDP）。在该框架中，每个智能体（对应一个基础设施组件，如桥面或路面）仅能访问其局部观测信息，并维护一个局部信念状态来表征其不确定性。系统整体状态由所有智能体的局部信念状态构成。

架构设计包含两个主要模块：分散的演员网络和集中的评论家网络。每个智能体拥有一个独立的演员网络（策略网络），其输入仅为该智能体对应的局部信念状态，输出是其动作概率分布。这种设计实现了策略参数化的稀疏化，避免了智能体间在隐藏层的交互，从而显著降低了计算复杂度，并支持真正的分散式执行。与此同时，一个集中的评论家网络在训练阶段被使用，其输入是整个系统的联合信念状态，输出是全局状态价值函数。该评论家用于计算优势函数，为各个演员网络的策略更新提供指导。

关键技术包括：1) **CTDE范式**：训练时利用集中评论家获取全局信息来协调各智能体策略优化，缓解多智能体环境中因策略同时更新导致的非平稳性问题；执行时则丢弃评论家，各智能体仅凭局部信念状态独立决策，确保了可扩展性。2) **离策略演员-评论家方法**：使用经验回放缓冲区进行批量采样，以提高样本效率和训练稳定性。演员网络通过策略梯度定理进行更新，梯度计算中引入了截断的重要性采样权重来处理行为策略与目标策略的差异。评论家网络则通过时间差分学习来最小化价值函数的均方误差损失。

创新点在于对原有DDMAC架构的改进。之前的DDMAC虽然为每个智能体设置了独立演员，但仍要求每个演员接收全局状态作为输入，这在智能体数量增多时仍会带来计算负担，且不利于完全分散的执行。DDMAC-CTDE通过将演员网络的输入严格限制为局部信念状态，并与CTDE范式结合，实现了训练效率与执行时分散性、可扩展性的更好平衡。该方法在论文新开发的、包含多种实际约束的交通网络基准环境中得到验证， consistently outperforms standard transportation management baselines。

### Q4: 论文做了哪些实验？

该论文的实验设置基于一个模拟美国弗吉尼亚州真实交通网络的新建综合基准环境，该环境包含异质的路面和桥梁资产，并模拟了非平稳退化过程。实验考虑了多种实际约束，如预算限制、性能指南、交通延误和风险考量。数据集即为此定制化仿真环境，用于评估不同方法在长期风险和成本最小化任务上的表现。

对比方法包括传统的交通管理基线方法（如基于规则或经典优化的方法），这些方法通常面临最优性、可扩展性及处理不确定性方面的局限。论文提出的DDMAC-CTDE（深度分散多智能体演员-评论家架构，采用集中训练分散执行）作为核心深度强化学习方法与之对比。

主要结果显示，DDMAC-CTDE在该基准环境中持续优于标准交通管理基线，能够生成更优的策略。关键数据指标体现在长期累积成本与风险的综合降低上，尽管论文未给出具体数值百分比，但强调了所提方法在满足多种操作约束的同时，显著提升了策略效果。实验验证了该框架在可扩展性和约束处理方面的优势。

### Q5: 有什么可以进一步探索的点？

该论文提出的DDMAC-CTDE框架在交通基础设施管理上展现了潜力，但仍存在一些局限性和可进一步探索的方向。首先，模型在非平稳退化环境中的长期泛化能力有待验证，实际基础设施的老化模式可能更为复杂多变。其次，虽然采用了CTDE范式，但在完全去中心化执行时，智能体间的隐式协调机制可能不足以应对突发的高耦合性约束（如跨区域的连锁维修需求），未来可探索引入轻量级的通信协议或分层协调策略。此外，论文的基准环境基于特定区域数据，其普适性需通过更多样化的地理和资产类型进行检验。从方法改进角度看，可考虑将领域知识（如工程模型）与DRL结合，使用物理信息神经网络来约束学习过程，提升策略的可解释性和安全性。另外，探索离线强化学习与在线微调的结合，有望利用历史数据提升样本效率，并降低在真实系统中探索的风险。最后，将多目标优化（如成本、风险、可持续性）明确纳入约束POMDP框架，也是值得深入的方向。

### Q6: 总结一下论文的主要内容

该论文针对大规模交通基础设施全生命周期管理中的优化问题，提出了一种基于约束部分可观测马尔可夫决策过程（POMDP）的建模框架，以处理高维状态和动作空间中的不确定性及多种运营约束。核心方法是设计了一种深度去中心化多智能体行动者-评论家（DDMAC）强化学习架构，并采用集中训练与分散执行（CTDE）范式，即DDMAC-CTDE，以提升算法的可扩展性。为验证框架有效性，论文构建了一个基于美国弗吉尼亚州真实交通网络的综合基准环境，包含异质的路面和桥梁资产及其非平稳退化过程，并整合了预算、性能、交通延误和风险等多重实际约束。实验表明，DDMAC-CTDE在该基准上显著优于传统交通管理基线方法，能够生成更优的维护策略。论文的主要贡献在于提供了一种可扩展、考虑约束的深度强化学习方法，以及一个真实、严谨的测试平台，为交通基础设施管理领域的进一步研究奠定了基础。
