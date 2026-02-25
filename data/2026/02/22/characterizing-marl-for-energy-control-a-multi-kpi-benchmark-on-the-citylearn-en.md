---
title: "Characterizing MARL for Energy Control: A Multi-KPI Benchmark on the CityLearn Environment"
authors:
  - "Aymen Khouja"
  - "Imen Jendoubi"
  - "Oumayma Mahjoub"
  - "Oussama Mahfoudhi"
  - "Claude Formanek"
  - "Siddarth Singh"
  - "Ruan De Kock"
date: "2026-02-22"
arxiv_id: "2602.19223"
arxiv_url: "https://arxiv.org/abs/2602.19223"
pdf_url: "https://arxiv.org/pdf/2602.19223v1"
categories:
  - "cs.AI"
  - "cs.LG"
  - "cs.MA"
tags:
  - "多智能体强化学习"
  - "能源管理"
  - "基准测试"
  - "城市能源系统"
  - "关键性能指标"
  - "去中心化训练"
  - "CityLearn"
relevance_score: 7.5
---

# Characterizing MARL for Energy Control: A Multi-KPI Benchmark on the CityLearn Environment

## 原始摘要

The optimization of urban energy systems is crucial for the advancement of sustainable and resilient smart cities, which are becoming increasingly complex with multiple decision-making units. To address scalability and coordination concerns, Multi-Agent Reinforcement Learning (MARL) is a promising solution. This paper addresses the imperative need for comprehensive and reliable benchmarking of MARL algorithms on energy management tasks. CityLearn is used as a case study environment because it realistically simulates urban energy systems, incorporates multiple storage systems, and utilizes renewable energy sources. By doing so, our work sets a new standard for evaluation, conducting a comparative study across multiple key performance indicators (KPIs). This approach illuminates the key strengths and weaknesses of various algorithms, moving beyond traditional KPI averaging which often masks critical insights. Our experiments utilize widely accepted baselines such as Proximal Policy Optimization (PPO) and Soft Actor Critic (SAC), and encompass diverse training schemes including Decentralized Training with Decentralized Execution (DTDE) and Centralized Training with Decentralized Execution (CTDE) approaches and different neural network architectures. Our work also proposes novel KPIs that tackle real world implementation challenges such as individual building contribution and battery storage lifetime. Our findings show that DTDE consistently outperforms CTDE in both average and worst-case performance. Additionally, temporal dependency learning improved control on memory dependent KPIs such as ramping and battery usage, contributing to more sustainable battery operation. Results also reveal robustness to agent or resource removal, highlighting both the resilience and decentralizability of the learned policies.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体强化学习（MARL）在城市能源管理任务中缺乏全面、可靠基准测试的问题。随着分布式能源资源（如光伏、储能系统）的集成，城市能源系统变得日益复杂，需要智能、协调的自动化控制系统。MARL 虽然被视作一种有前景的解决方案，但其在实际能源管理场景中的优劣和适用条件尚未得到充分理解。

具体而言，论文试图填补现有研究的空白，通过提供一个在 CityLearn 仿真环境下的综合性 MARL 算法基准。它系统性地比较了两种主要训练范式（去中心化训练与去中心化执行 DTDE、中心化训练与去中心化执行 CTDE）、不同神经网络架构（前馈与循环网络）以及代表算法（如 PPO 和 SAC），以评估它们在多种关键性能指标（KPI）下的有效性。研究超越了传统的平均 KPI 比较，引入了针对实际部署挑战的新指标（如单体建筑贡献、电池寿命），旨在揭示不同算法在性能、鲁棒性、稳定性与可分散性方面的根本性权衡，从而为复杂多智能体能源管理任务的算法选择提供清晰、实用的见解。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕强化学习（RL）与多智能体强化学习（MARL）在能源管理中的应用，以及标准化基准测试的进展。

在**RL用于能源管理**方面，已有研究证明了其在优化实时能耗、整合分布式能源（DER）方面的经济与环境效益，但普遍存在可复现性挑战，如算法随机性、超参数报告不足和测试环境不统一。为此，**CityLearn**环境被开发为标准化框架，其举办的CityLearn挑战赛已成为评估RL与混合控制算法的主要基准。例如，2021年冠军团队采用混合策略（线性化MPC结合进化算法调优），在峰值负载、成本与排放等多目标上表现优异。

随着问题规模扩大，管理多栋建筑自然导向**MARL解决方案**。CityLearn环境支持多智能体范式，后续挑战赛中，2022年获胜团队使用MAPPO实现建筑间协同决策，另有团队结合手工规则与MARL以平衡性能与可解释性。此外，独立研究如**MARLISA**（基于SAC的分散式框架）和**MERLIN**（为个体建筑定制独立RL智能体）进一步探索了分散化架构的有效性。

然而，现有研究在**标准化基准测试**上存在不足。尽管早期工作为评估奠定了基础，但在算法覆盖广度、统计可靠性（如多次运行以考量随机性）以及实验设置报告完整性方面仍有欠缺。本文正是在此背景下，针对CityLearn环境，通过系统比较多种MARL算法（如PPO、SAC）与训练范式（DTDE、CTDE），并引入新颖的关键绩效指标（KPIs），旨在填补这一空白，为MARL在能源控制领域提供更全面、可靠的评估标准。

### Q3: 论文如何解决这个问题？

论文通过构建一个系统性的多智能体强化学习（MARL）基准测试框架来解决能源控制场景中算法评估不全面、不深入的问题。其核心方法、架构设计和关键技术体现在以下几个方面：

**1. 系统性的算法与架构对比框架：**
论文在统一的CityLearn仿真环境中，系统性地对比了两种主流的多智能体训练范式（DTDE与CTDE）及其具体算法实现（如ISAC、IPPO、MAPPO）。为了探究时序建模的影响，所有算法均实现了前馈网络和基于GRU的循环网络两种变体。这种设计允许直接比较不同算法架构（分散vs集中、前馈vs循环）在相同任务和奖励设置下的性能差异，从而揭示不同范式与架构的固有优势和弱点。

**2. 引入面向实际部署的关键性能指标：**
除了使用环境内置的标准化KPI（如碳排放、用电量、舒适度）外，论文创新性地提出了两个领域特定的新KPI：
*   **电池放电深度：** 采用源自疲劳分析的雨流计数法，将复杂的电池充放电模式分解为可识别的循环，从而更准确地量化电池使用强度和对寿命的影响，直接关联实际系统的可持续性。
*   **智能体重要性分数：** 借鉴沙普利值思想，通过计算每个智能体对团队奖励的边际贡献，来评估多智能体信用分配的效率。该指标能有效识别“懒惰”智能体或算法对少数智能体的过度依赖，揭示了算法在协调与责任分配方面的质量。

**3. 严谨且鲁棒的评估协议：**
为确保评估的公平性和结论的可靠性，论文设计了一套严格的评估流程：
*   **超参数调优与模型选择：** 所有算法均在独立的大规模超参数搜索（21种配置，3个随机种子）后进行最优模型选择，避免了因参数设置不当导致的性能误判。
*   **多维度的性能度量：** 评估不仅关注传统的平均性能（使用官方加权平均分），还引入了**绝对性能指标**（在大量回合上评估最优参数模型的性能）、**四分位均值**（IQM，降低异常值影响）和**条件风险价值**（CVaR，量化最坏情况下的性能）。这种组合能全面揭示算法的中心趋势、鲁棒性和在不利条件下的表现。
*   **统计可靠性保障：** 采用分层自助法计算95%置信区间，并辅以改进概率度量、排名分布图和学习曲线分析，确保了比较结果的统计意义和稳定性。

综上，论文通过构建一个**算法范式对比全面**、**评估指标贴近实际挑战**、**实验协议严谨可靠**的三位一体基准测试框架，系统地解决了如何深入、公平地评估MARL算法在复杂能源控制任务中性能的问题，超越了传统仅靠平均KPI的粗粒度评估方式。

### Q4: 论文做了哪些实验？

该论文在CityLearn城市能源管理仿真环境中，对六种多智能体强化学习（MARL）算法进行了全面的基准测试实验。实验设置涵盖了两种主流算法（PPO和SAC）、两种训练范式（去中心化训练与执行DTDE，如IPPO和SAC；中心化训练与去中心化执行CTDE，如MAPPO）以及两种神经网络架构（前馈网络和循环网络）。评估采用了多维度关键性能指标（KPI），包括传统环境级指标（如平均得分、碳排放、负荷波动“ramping”、不舒适度比例）和作者提出的新指标（如电池放电深度DoD、放电持续时间），以全面衡量算法在效率、稳定性、电池寿命等方面的表现。

主要实验结果如下：在聚合性能上，基于DTDE的独立学习算法IPPO在平均表现和最差情况表现（CVaR）上均优于CTDE算法MAPPO，展现出更强的鲁棒性。在具体KPI上，循环网络架构（如Recurrent IPPO）在具有强时序依赖性的指标上优势明显，例如能显著降低电网负荷波动（ramping），并实现更浅、更长的电池放电周期，有利于延长电池寿命。然而，对于碳排放和不舒适度等更依赖即时、局部反应的指标，循环网络并未带来一致性的提升，甚至有时表现更差，表明模型复杂度的收益因任务而异。此外，SAC算法初期学习效率高但后期容易陷入平台期，而IPPO则收敛更稳、最终性能更优。实验结果表明，DTDE范式在能源控制任务中整体上优于CTDE，且引入时序记忆对优化电池使用和平滑能源需求具有关键作用。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于主要基于现有经典算法（如PPO、SAC）及其变体进行评测，未充分探索更先进的MARL架构（如基于注意力或值分解的模型），也未深入优化奖励函数与观察空间设计，这些因素可能限制算法性能的进一步提升。实验环境虽具代表性，但可能未涵盖所有现实能源系统的复杂动态与异构性。

未来方向可重点探索：1）采用更先进的MARL架构，如多智能体Transformer或Sable等高效可扩展模型，以提升协调能力与泛化性；2）系统研究奖励塑造与观察设计，以更好地平衡短期目标（如舒适度）与长期目标（如电池寿命）；3）将评测扩展至更复杂、异构的城市能源场景，并考虑动态环境变化与不确定性的影响；4）结合离线强化学习或模仿学习，利用历史数据提升策略的实用性与安全性。

### Q6: 总结一下论文的主要内容

这篇论文针对城市能源系统优化这一智能城市关键问题，提出了一个基于多智能体强化学习（MARL）的综合性评测基准。其核心贡献在于，利用CityLearn仿真环境，首次系统性地从多个关键性能指标（KPI）维度对主流MARL算法进行了评估，超越了传统单一平均指标的做法，揭示了不同算法在协调、鲁棒性等实际挑战中的真实表现。

研究意义重大。它不仅通过引入个体建筑贡献、电池寿命等新颖KPI，将评估标准与实际工程挑战（如去中心化部署、设备耐久性）紧密结合，还通过对比分散训练分散执行（DTDE）与集中训练分散执行（CTDE）等范式，发现DTDE在平均和最差性能上均更优，为构建更具韧性的去中心化能源控制策略提供了实证依据。此外，研究证实了时序依赖学习对改善电池使用等记忆依赖性指标的有效性。这项工作为未来MARL在复杂能源管理场景中的应用与算法发展设立了更可靠、更贴近现实的评估新标准。
