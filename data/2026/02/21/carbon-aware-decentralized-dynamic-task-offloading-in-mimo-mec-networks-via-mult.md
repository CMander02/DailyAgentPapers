---
title: "Carbon-aware decentralized dynamic task offloading in MIMO-MEC networks via multi-agent reinforcement learning"
authors:
  - "Mubshra Zulfiqar"
  - "Muhammad Ayzed Mirza"
  - "Basit Qureshi"
date: "2026-02-21"
arxiv_id: "2602.18797"
arxiv_url: "https://arxiv.org/abs/2602.18797"
pdf_url: "https://arxiv.org/pdf/2602.18797v1"
categories:
  - "cs.DC"
  - "cs.AI"
  - "cs.LG"
tags:
  - "多智能体强化学习"
  - "去中心化决策"
  - "任务卸载"
  - "资源管理"
  - "可持续计算"
  - "边缘计算"
  - "部分可观测马尔可夫决策过程"
relevance_score: 6.5
---

# Carbon-aware decentralized dynamic task offloading in MIMO-MEC networks via multi-agent reinforcement learning

## 原始摘要

Massive internet of things microservices require integrating renewable energy harvesting into mobile edge computing (MEC) for sustainable eScience infrastructures. Spatiotemporal mismatches between stochastic task arrivals and intermittent green energy along with complex inter-user interference in multi-antenna (MIMO) uplinks complicate real-time resource management. Traditional centralized optimization and off-policy reinforcement learning struggle with scalability and signaling overhead in dense networks. This paper proposes CADDTO-PPO, a carbon-aware decentralized dynamic task offloading framework based on multi-agent proximal policy optimization. The multi-user MIMO-MEC system is modeled as a Decentralized Partially Observable Markov Decision Process (DEC-POMDP) to jointly minimize carbon emissions and buffer latency and energy wastage. A scalable architecture utilizes decentralized execution with parameter sharing (DEPS), which enables autonomous IoT agents to make fine-grained power control and offloading decisions based solely on local observations. Additionally, a carbon-first reward structure adaptively prioritizes green time slots for data transmission to decouple system throughput from grid-dependent carbon footprints. Finally, experimental results demonstrate CADDTO-PPO outperforms deep deterministic policy gradient (DDPG) and lyapunov-based baselines. The framework achieves the lowest carbon intensity and maintains near-zero packet overflow rates under extreme traffic loads. Architectural profiling validates the framework to demonstrate a constant $O(1)$ inference complexity and theoretical lightweight feasibility for future generation sustainable IoT deployments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大规模物联网（IoT）微服务在移动边缘计算（MEC）网络中，如何实现可持续、低碳的动态任务卸载这一核心问题。具体而言，它针对三个相互关联的挑战：1）随机任务到达与间歇性绿色能源（如太阳能）在时空上的不匹配；2）多用户MIMO上行链路中复杂的用户间干扰，这增加了传输功耗和碳排放；3）在密集网络中，传统集中式优化或强化学习方法面临可扩展性差和信令开销大的难题。为此，论文提出了一个名为CADDTO-PPO的碳感知去中心化动态任务卸载框架。该框架将多用户MIMO-MEC系统建模为一个去中心化部分可观测马尔可夫决策过程，目标是最小化碳排放、缓冲区延迟和能源浪费。其核心创新在于采用基于多智能体近端策略优化的去中心化执行与参数共享架构，使每个IoT设备能仅凭本地观测自主做出细粒度的功率控制和卸载决策，并通过一种“碳优先”的奖励机制，自适应地优先利用绿色能源时段进行数据传输，从而将系统吞吐量与依赖电网的碳足迹解耦。最终目标是为下一代可持续IoT部署提供一个理论上轻量、可扩展且真正降低碳强度的实时资源管理方案。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕三个领域展开：碳感知计算与能量收集、MIMO边缘计算与干扰管理、以及去中心化深度强化学习（DRL）用于任务卸载。

在碳感知计算与能量收集方面，早期研究如Sun等人（2021）专注于能量效率，但未区分不同能源的碳强度。后续工作开始量化碳排放（Yu等人，2023），但多假设静态环境且未考虑多天线干扰。Wei等人（2023）提出了基于DDPG的碳感知框架，但依赖非可再生能源备份且缺乏动态碳强度适应。本文的CADDTO-PPO框架则在一个完全去中心化的设置中，集成了碳感知优化、MIMO干扰管理和能量收集。

在MIMO边缘计算方面，Zhou等人（2021）利用李雅普诺夫优化进行建模，但需要集中式控制和全局信道状态信息（CSI），导致高信令开销。Chen等人（2020）的DRL方法支持本地执行，但仍依赖集中式训练。本文提出的框架则通过完全去中心化的方式，联合优化MIMO功率控制、任务卸载和能量收集调度，无需全局CSI交换。

在去中心化DRL方面，基于价值的方法（如DQN）被用于任务图调度（Liu等人，2024），但在连续动作空间（如功率控制）中收敛困难。多智能体方法如MAPPO（Li等人，2024）优化负载均衡，但忽略了动态电网碳强度。本文的CADDTO-PPO基于多智能体近端策略优化（MAPPO），引入了“碳优先”奖励结构，并首次通过架构剖析验证了其在实际部署中的轻量级可行性，弥补了现有研究多局限于仿真验证的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为CADDTO-PPO的碳感知去中心化动态任务卸载框架来解决MIMO-MEC网络中随机任务到达、间歇性绿色能源以及复杂用户间干扰带来的实时资源管理难题。其核心方法、架构设计和关键技术如下：

**核心方法与架构设计：**
论文将多用户MIMO-MEC系统建模为一个**去中心化部分可观测马尔可夫决策过程（DEC-POMDP）**，以联合优化碳排放、缓冲区延迟和能量浪费。框架采用**集中训练与去中心化执行（CTDE）** 范式，并引入了**参数共享（DEPS）** 的扩展架构。具体而言，所有物联网（IoT）用户代理共享同一个策略网络（Actor）和价值网络（Critic）的参数。在训练阶段，中央服务器汇集所有代理的经验轨迹来更新这个共享网络；在执行（推理）阶段，每个IoT设备仅基于自身的局部观测（如缓冲区长度、归一化信干噪比、采集的绿色能量），利用本地的策略网络副本自主做出细粒度的功率控制和卸载决策，无需与其他设备或中央服务器进行实时通信。

**关键技术：**
1.  **基于多智能体近端策略优化（MAPPO）的算法**：选择PPO这一**同策略（on-policy）** 的Actor-Critic方法，因其能处理连续动作空间（实现精细的功率控制），并利用新鲜样本进行更新，在干扰快速变化的非平稳去中心化环境中能保证稳健收敛。算法通过裁剪的替代目标函数和广义优势估计（GAE）来稳定训练。
2.  **碳优先的奖励函数设计**：奖励函数是一个负的加权和，旨在最小化长期平均计算开销。它明确纳入了**碳排放量**、**缓冲区队列长度**以及**能量浪费和缓冲区溢出**的惩罚项。通过调整权重，系统可以自适应地优先在绿色能源充足的时间槽进行数据传输，从而在理论上将系统吞吐量与依赖电网的碳足迹解耦。
3.  **轻量级且可扩展的局部观测与决策**：每个代理的**状态空间**仅包含归一化的本地缓冲区水平、采集的绿色能量以及前一时刻的归一化SINR反馈，极大减少了信令开销。**动作空间**是本地执行功率和卸载传输功率的连续值。这种设计使得每个设备的前向推理计算复杂度仅取决于神经网络结构（层数L和隐藏层大小H），即O(L·H²)，而与网络中的总用户数U无关，实现了**常数级O(1)的推理复杂度**，确保了框架在大规模物联网部署中的可扩展性和轻量化可行性。

### Q4: 论文做了哪些实验？

论文在动态移动边缘计算（MEC）环境中进行了仿真实验。实验设置包括：默认5个物联网设备在100米基站半径内随机移动，信道采用相关性和误差模型；任务到达和能量收集均遵循泊松过程，分别设定比特和焦耳参数；优先使用收集的绿色能源，电网碳排放因子为700 g/kWh；状态观测归一化，奖励权重均衡分配；实验在配备Intel i7 CPU和NVIDIA GPU的硬件上运行，并固定随机种子以确保可复现性。

基准测试方面，论文将提出的CADDTO-PPO框架与深度确定性策略梯度（DDPG）和基于李雅普诺夫优化的基线方法进行了对比。

主要结果显示，CADDTO-PPO在多项关键指标上均优于基线。具体而言，该框架实现了最低的碳强度（即单位能耗的碳排放量），并且在极端流量负载下保持了接近零的数据包溢出率，有效联合优化了碳排放、缓冲延迟和能量浪费。此外，架构分析验证了该框架具有恒定的O(1)推理复杂度，证明了其轻量级特性和在未来可持续物联网部署中的可行性。

### Q5: 有什么可以进一步探索的点？

该论文提出的CADDTO-PPO框架在碳感知任务卸载方面取得了进展，但仍存在一些局限性和未来探索方向。局限性方面：首先，模型依赖于对可再生能源和任务到达的统计假设，在现实世界高度动态和不确定的环境中可能性能下降；其次，DEC-POMDP模型中的局部观测可能无法充分捕捉全局网络状态，导致次优决策；再者，参数共享（DEPS）虽提升了可扩展性，但可能限制了智能体针对高度异构环境的个性化策略学习。

未来方向可重点探索：1）**更鲁棒的环境建模**：引入在线学习或元学习机制，使智能体能自适应非平稳环境，减少对先验统计知识的依赖；2）**改进的通信与协调机制**：在完全去中心化基础上，设计轻量级的智能体间通信协议，以有限的信息交换提升全局协同效率；3）**多层次优化目标**：当前框架主要优化碳排放和延迟，未来可整合更多维度的可持续性指标（如设备生命周期能耗、经济成本），实现多目标权衡；4）**从仿真到真实部署的跨越**：研究在物理物联网测试平台上的验证，解决实际信道干扰、硬件异构性等挑战，推动框架的实用化。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为CADDTO-PPO的碳感知去中心化动态任务卸载框架，用于多用户MIMO移动边缘计算网络。其核心贡献在于利用多智能体近端策略优化方法，将复杂的资源管理问题建模为去中心化部分可观测马尔可夫决策过程，旨在协同优化碳排放、缓冲延迟和能量浪费。该框架采用参数共享的去中心化执行架构，使每个物联网设备能仅基于本地观测，自主做出细粒度的功率控制和任务卸载决策。此外，论文设计了一种“碳优先”的奖励机制，自适应地优先利用绿色能源时段进行数据传输，从而将系统吞吐量与依赖电网的碳足迹解耦。实验表明，该框架在碳强度和极端流量下的数据包溢出率方面优于基线方法，并具有恒定的推理复杂度，为可持续物联网部署提供了轻量且高效的解决方案。
