---
title: "HONEST-CAV: Hierarchical Optimization of Network Signals and Trajectories for Connected and Automated Vehicles with Multi-Agent Reinforcement Learning"
authors:
  - "Ziyan Zhang"
  - "Changxin Wan"
  - "Peng Hao"
  - "Kanok Boriboonsomsin"
  - "Matthew J. Barth"
  - "Yongkang Liu"
  - "Seyhan Ucar"
  - "Guoyuan Wu"
date: "2026-02-21"
arxiv_id: "2602.18740"
arxiv_url: "https://arxiv.org/abs/2602.18740"
pdf_url: "https://arxiv.org/pdf/2602.18740v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "eess.SY"
tags:
  - "多智能体强化学习"
  - "交通信号控制"
  - "自动驾驶车辆"
  - "分层优化"
  - "网络级控制"
  - "能效优化"
  - "去中心化智能体"
relevance_score: 7.5
---

# HONEST-CAV: Hierarchical Optimization of Network Signals and Trajectories for Connected and Automated Vehicles with Multi-Agent Reinforcement Learning

## 原始摘要

This study presents a hierarchical, network-level traffic flow control framework for mixed traffic consisting of Human-driven Vehicles (HVs), Connected and Automated Vehicles (CAVs). The framework jointly optimizes vehicle-level eco-driving behaviors and intersection-level traffic signal control to enhance overall network efficiency and decrease energy consumption. A decentralized Multi-Agent Reinforcement Learning (MARL) approach by Value Decomposition Network (VDN) manages cycle-based traffic signal control (TSC) at intersections, while an innovative Signal Phase and Timing (SPaT) prediction method integrates a Machine Learning-based Trajectory Planning Algorithm (MLTPA) to guide CAVs in executing Eco-Approach and Departure (EAD) maneuvers. The framework is evaluated across varying CAV proportions and powertrain types to assess its effects on mobility and energy performance. Experimental results conducted in a 4*4 real-world network demonstrate that the MARL-based TSC method outperforms the baseline model (i.e., Webster method) in speed, fuel consumption, and idling time. In addition, with MLTPA, HONEST-CAV benefits the traffic system further in energy consumption and idling time. With a 60% CAV proportion, vehicle average speed, fuel consumption, and idling time can be improved/saved by 7.67%, 10.23%, and 45.83% compared with the baseline. Furthermore, discussions on CAV proportions and powertrain types are conducted to quantify the performance of the proposed method with the impact of automation and electrification.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决城市混合交通流（包含人类驾驶车辆HVs和网联自动驾驶车辆CAVs）中，网络级交通效率与能源消耗的协同优化问题。传统方法通常将车辆轨迹规划和交叉口信号控制视为独立问题，限制了网联移动性在混合交通条件下的潜在效益。论文指出，现有协同优化方法受限于计算负担和可扩展性，且大多假设传统内燃机车辆，较少考虑不同动力总成类型（如电动汽车）的影响。

为此，论文提出了一个名为HONEST-CAV的分层优化框架，其核心目标是**通过联合优化车辆级的生态驾驶行为和交叉口级的交通信号控制，来近似实现网络整体效率（如速度、延误）和能耗的全局最优**。具体而言，框架上层采用基于多智能体强化学习（MARL）的去中心化信号控制方法，以提升网络通行效率；下层则通过创新的信号相位与配时（SPaT）预测方法，结合基于机器学习的轨迹规划算法（MLTPA），来指导CAVs执行生态接近与离开（EAD）操纵以节省能耗。该框架旨在设计一个模块化、可扩展且能实时部署的解决方案，以应对大规模城市网络中信号与车辆控制的协同挑战，并评估其在不同CAV渗透率和车辆动力总成类型下的性能。

### Q2: 有哪些相关研究？

本文的研究领域是车路协同控制，主要涉及交通信号控制（TSC）和网联自动驾驶车辆（CAV）轨迹规划的协同优化。相关工作主要分为以下几类：

1.  **早期规则与优化方法**：早期研究如Malakorn等人（2010）和Li等人（2014）的工作，主要关注单个交叉口的车-信号协同控制，采用基于规则或混合整数规划的方法。这些方法虽能实现理论最优，但计算负担重，难以扩展到大规模路网。

2.  **分层学习框架**：近期研究趋势是利用分层学习框架来平衡计算效率与协同效果。例如，Esaid等人（2021）使用模仿学习（IL）进行车辆生态驾驶，而Mei等人（2023）则应用多智能体强化学习（MARL）进行交叉口信号控制。这些方法开始整合车辆与信号控制，并考虑混合交通流。

3.  **现有方法的局限**：现有协同优化方法仍普遍受限于计算复杂度、可扩展性不足，且大多假设车辆为传统内燃机汽车，较少考虑不同动力总成（如电动汽车）的影响。

**本文与这些研究的关系**：本文提出的HONEST-CAV框架直接建立在上述分层学习框架（如MARL for TSC, IL for EAD）的基础上，是对这一趋势的深化和扩展。其核心创新在于：
*   **系统性整合**：通过新颖的信号相位与配时（SPaT）预测方法，更紧密地耦合了基于VDN的MARL信号控制层和基于IL的车辆轨迹规划层，实现了网络级的协同。
*   **提升可扩展性与效率**：采用多进程技术加速MARL训练，增强了框架在大规模路网中实时部署的潜力和计算效率。
*   **扩展评估维度**：不仅评估混合交通流中CAV的渗透率，还首次系统分析了不同动力总成类型（内燃机与电动汽车）对协同控制性能的影响，填补了现有研究的空白。

因此，本文是对现有车路协同分层优化研究的重要推进，致力于解决其可扩展性、计算效率和评估全面性方面的关键挑战。

### Q3: 论文如何解决这个问题？

论文通过一个分层优化框架解决混合交通流（人类驾驶车辆HV与网联自动驾驶车辆CAV）的网络级协同控制问题，其核心方法结合了多智能体强化学习（MARL）与机器学习轨迹规划，实现信号控制与车辆轨迹的联合优化。

在架构设计上，系统分为两层：**路口级信号控制**与**车辆级生态驾驶**。路口控制采用基于**集中训练分散执行（CTDE）** 的多智能体强化学习框架，每个路口作为一个智能体，通过**值分解网络（VDN）** 将全局奖励分解为局部Q函数之和，实现分布式协同优化。智能体状态为144维向量，包含各车道在信号周期内的占有率、平均速度、排队长度及CAV渗透率等多特征时空聚合信息；动作空间为5维，包括周期长度变化率及各相位绿信比，通过软最大化与裁剪操作确保安全与协同。奖励函数鼓励更多车辆通过并减少排队。算法采用**多智能体软演员-评论家（MASAC）**，结合熵正则化促进探索，并利用异步并行训练加速收敛。

为解决RL信号控制下CAV轨迹规划所需的实时信号相位与配时（SPaT）预测问题，论文提出**混合预测机制**：将基于当前状态通过训练策略预测的相位，与历史记录相位按时间权重融合，提高动态环境下的鲁棒性。

在车辆轨迹规划层，采用**基于模仿学习的轨迹规划算法（MLTPA）** 为CAV生成生态接近与离开（EAD）速度曲线。MLTPA作为代理模型，学习了基于图的最优轨迹规划算法（GBTPA）生成的轨迹，在保持近似最优性能的同时大幅降低计算开销，支持大规模实时部署。

关键技术包括：CTDE框架下的MASAC与VDN实现可扩展协同信号控制；加权时空状态表征捕捉路口动态；混合SPaT预测桥接信号控制与轨迹规划；以及MLTPA实现高效节能轨迹生成。整个系统通过分层协同，在提升通行效率与降低能耗方面显著优于传统方法。

### Q4: 论文做了哪些实验？

论文在仿真环境中进行了系统性实验，主要分为基准场景性能测试和不同CAV比例与动力总成类型的讨论。

**实验设置**：研究使用开源交通仿真器SUMO，在一个经过校准的真实世界4x4杭州路网中进行。交通流包含人工驾驶车辆和网联自动驾驶车辆，基于SUMO默认的内燃机客车配置建模。训练配置方面，采用8个并行工作进程，最大训练轮次为150。信号控制代理使用SAC算法，学习率为0.0003。

**基准测试**：在CAV渗透率为60%的设定下，将提出的方法（MARL TSC + MLTPA）与三种基线进行对比：1）传统的Webster信号控制方法；2）独立强化学习（IRL）TSC + Krauss跟车模型；3）MARL TSC + Krauss跟车模型。评估指标为网络层面的平均能耗、平均怠速时间和平均速度。每种基于RL的方法都进行了50次不同随机种子的蒙特卡洛模拟。

**主要结果**：如表所示，提出的HONEST-CAV框架（MARL TSC + MLTPA）在所有指标上均取得最佳性能。相较于Webster基线，平均速度提升7.67%，平均能耗降低10.23%，平均怠速时间大幅减少45.83%。MARL方法也显著优于IRL方法，证明了全局奖励共享的价值。此外，研究还探讨了不同CAV比例（10%-90%）和动力总成类型（内燃机 vs. 电动）的影响。结果显示，性能随着CAV比例升高而持续改善，在70%-90%的高比例区间提升最为显著。在电动化环境中，HONEST-CAEV能带来额外的能耗收益。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其框架目前主要针对特定网络规模，尚未扩展到城市级大规模路网。未来可进一步探索的方向包括：引入区域划分策略，将分层优化框架应用于各子区域，以实现城市级部署的扩展性；研究更复杂的多智能体协作机制，以处理动态交通流和突发事件；探索不同CAV渗透率下的鲁棒性优化，并考虑混合动力车辆等更多元化的动力系统类型；此外，可结合实时交通预测数据，进一步提升轨迹规划与信号控制的协同效率。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为HONEST-CAV的分层协同优化框架，旨在提升混合交通流（包含人工驾驶车辆和网联自动驾驶车辆）的网络效率与能源经济性。其核心贡献在于**将网络级的交通信号控制与车辆级的节能驾驶轨迹规划进行联合优化**。具体而言，框架上层采用基于价值分解网络的多智能体强化学习方法，实现路口交通信号的分散式自适应控制；下层则通过创新的信号相位与配时预测算法，结合机器学习轨迹规划，引导网联自动驾驶车辆执行节能接近与离开操作。实验表明，该框架在真实路网中显著提升了平均车速、降低了燃油消耗与怠速时间，并且性能随着网联自动驾驶车辆渗透率的提高而持续增强，同时展现了交通电动化的进一步节能潜力。这项工作为大规模城市智慧交通系统的协同管控提供了有效的解决方案。
