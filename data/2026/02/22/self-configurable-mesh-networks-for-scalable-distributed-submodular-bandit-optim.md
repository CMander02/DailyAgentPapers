---
title: "Self-Configurable Mesh-Networks for Scalable Distributed Submodular Bandit Optimization"
authors:
  - "Zirui Xu"
  - "Vasileios Tzoumas"
date: "2026-02-22"
arxiv_id: "2602.19366"
arxiv_url: "https://arxiv.org/abs/2602.19366"
pdf_url: "https://arxiv.org/pdf/2602.19366v1"
categories:
  - "eess.SY"
  - "cs.MA"
  - "cs.RO"
  - "math.OC"
tags:
  - "多智能体系统"
  - "分布式优化"
  - "在线学习"
  - "通信约束"
  - "子模优化"
  - "多臂老虎机"
relevance_score: 6.0
---

# Self-Configurable Mesh-Networks for Scalable Distributed Submodular Bandit Optimization

## 原始摘要

We study how to scale distributed bandit submodular coordination under realistic communication constraints in bandwidth, data rate, and connectivity. We are motivated by multi-agent tasks of active situational awareness in unknown, partially-observable, and resource-limited environments, where the agents must coordinate through agent-to-agent communication. Our approach enables scalability by (i) limiting information relays to only one-hop communication and (ii) keeping inter-agent messages small, having each agent transmit only its own action information. Despite these information-access restrictions, our approach enables near-optimal action coordination by optimizing the agents' communication neighborhoods over time, through distributed online bandit optimization, subject to the agents' bandwidth constraints. Particularly, our approach enjoys an anytime suboptimality bound that is also strictly positive for arbitrary network topologies, even disconnected. To prove the bound, we define the Value of Coordination (VoC), an information-theoretic metric that quantifies for each agent the benefit of information access to its neighbors. We validate in simulations the scalability and near-optimality of our approach: it is observed to converge faster, outperform benchmarks for bandit submodular coordination, and can even outperform benchmarks that are privileged with a priori knowledge of the environment.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大规模分布式多智能体在未知、部分可观测、资源受限环境中进行主动态势感知等任务时，面临的协调优化与通信约束之间的根本矛盾。具体而言，它针对四个现实挑战：有限的通信带宽、有限的数据速率、无法保证的网络连通性以及非结构化的未知环境。在这些约束下，传统的分布式次模优化算法（通常依赖无限速率的多跳通信或全连接假设）无法同时实现可扩展性和近似最优的协调性能。

因此，论文的核心问题是：**如何在严格的通信约束（带宽、数据速率、连通性）下，设计一个可扩展且能保证近似最优性能的分布式多智能体在线协调框架？** 为此，论文提出了一种自配置网状网络方法，其关键创新在于通过智能地限制信息访问来平衡决策时间与决策质量：一方面，通过限制中继通信仅在一跳范围内、并压缩消息大小（只传递自身动作信息）来确保可扩展性；另一方面，通过分布式在线赌博机优化，让每个智能体根据任务效用函数动态优化其通信邻居（即自配置网络拓扑），从而在信息受限的情况下仍能实现接近最优的动作协调。论文还从理论上定义了“协调价值”这一信息论度量来量化邻居信息访问的收益，并提供了严格的正值次优性保证。

### Q2: 有哪些相关研究？

本文研究分布式次模赌博机优化中的可扩展协调问题，相关工作主要分为三类。第一类是经典次模优化算法，如顺序贪婪（SG）算法及其在已知环境中的分布式变体，广泛应用于多智能体感知任务。第二类是在线/赌博机环境下的算法，通过连续域的多线性扩展或在线SG变体处理未知环境，但通常假设无限通信速率或全连通网络，难以在现实通信约束下扩展。第三类是针对通信限制的优化方法，包括量化通信、利用信息依赖稀疏性等方法，但这些工作主要集中于凸优化问题；而在离散次模优化中，现有研究（如Grimsman等人工作）仅进行与目标函数无关的固定拓扑限制，或如作者先前工作仅限制单跳通信但无法优化网络拓扑。

本文与这些工作的关系在于：它首次在离散次模赌博机协调中，通过分布式在线优化主动配置通信拓扑（即智能优化信息访问），同时实现可扩展性与近似最优性。具体而言，本文方法限制了单跳通信和小消息尺寸以确保可扩展性，并引入了“协调价值”度量来量化邻居信息访问的收益，从而支持对拓扑进行目标函数相关的优化。这弥补了现有方法在现实通信约束（带宽、数据率、连通性）下无法兼顾扩展性与性能的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“交替协调与网络设计算法”（AlterNAting COordination and Network Design Algorithm, \alg）的分布式在线学习框架，来解决在通信带宽、数据速率和连通性受限的现实约束下，多智能体进行可扩展分布式次模赌博机优化的问题。其核心方法是将联合优化问题分解为两个交替进行的、形式化为对抗性赌博机问题的子任务：动作协调与通信邻域设计。

**核心架构与流程**：每个智能体 i 在每一时间步 t 并行执行两个模块：1) **动作选择（\actionsel）**：智能体从其动作集 \(\mathcal{V}_i\) 中选择一个动作 \(a_{i,t}\)，目标是最大化给定当前邻居动作条件下的边际增益 \(f(a_{i,t} \,|\, \{a_{j,t}\}_{j\in\calN_{i,t}})\)。由于邻居动作在自身动作选定后才可知，这被建模为一个对抗性赌博机问题，采用 EXP3 类算法进行在线学习，通过权重更新来逼近最优动作。2) **邻居选择（\neighborsel）**：智能体从其潜在的协调邻域 \(\mathcal{M}_i\) 中，在带宽约束 \(|\calN_{i,t}| \leq \alpha_i\) 下，选择一个通信邻居集合 \(\calN_{i,t}\)。该选择同样被建模为对抗性赌博机问题，其“奖励”与协调收益相关。

**关键技术**：1) **联合在线优化**：算法通过交替执行上述两个赌博机过程，实现了通信网络拓扑与动作策略的协同在线优化。智能体仅依赖单跳通信，且只传递自身的动作信息，极大降低了通信开销。2) **协调价值（VoC）量化**：论文创新性地定义了“协调价值” \(\smi{a_{i,t}}{\calN_{i,t}}\) 这一信息论度量，它量化了智能体通过从邻居获取信息所能获得的边际收益提升。该指标为邻居选择提供了理论依据，使得智能体能够评估并优化其信息访问策略。3) **理论保证**：即使在网络可能不连通的情况下，该框架也能保证一个任意时间的次优性界，并证明其遗憾是次线性的，从而确保算法随时间推移能渐进接近最优协调性能。

总之，该方法的核心是通过分布式在线学习，使每个智能体在严格通信限制下，自主且同步地优化其动作和通信对象，利用 VoC 来指导网络形成，最终实现接近全局最优的协调效果，并具有良好的可扩展性。

### Q4: 论文做了哪些实验？

该论文通过仿真实验验证了所提出的自配置网状网络方法在分布式次模赌博机优化中的可扩展性和近优性。实验设置模拟了多智能体在未知、部分可观测、资源受限环境中的主动态势感知任务，智能体通过受限的带宽、数据速率和连接性进行通信。基准测试包括传统的分布式次模协调方法以及一些具备先验环境知识的特权基准方法。主要结果显示，该方法在收敛速度上表现更快，优于现有的次模赌博机协调基准，甚至在部分情况下能够超越那些拥有环境先验知识的基准方法，证明了其在严格通信限制下仍能实现近优的行动协调。

### Q5: 有什么可以进一步探索的点？

本文提出的分布式子模多臂老虎机优化方法在通信受限场景下展现了良好的可扩展性，但仍存在一些局限和值得深入探索的方向。首先，该方法假设所有智能体共享相同的子模目标函数，这在现实异构多智能体系统中可能不成立，未来可研究如何在目标函数不同或存在部分冲突的情况下进行协调优化。其次，当前通信拓扑的优化主要基于带宽约束，未充分考虑动态网络环境（如链路不稳定、延迟波动）的影响，未来需要设计更鲁棒的自适应通信策略。此外，理论分析中的“协调价值”度量仅考虑了直接邻居，未来可扩展到多跳信息价值评估，以更好地权衡通信成本与协调收益。最后，该方法目前仅在仿真环境中验证，未来需要在真实物理系统（如无人机集群、传感器网络）中测试其性能，并考虑更复杂的部分可观测环境动态。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种用于分布式次模赌博机优化的自配置网络框架，旨在解决多智能体在未知、资源受限环境中协同感知时的通信可扩展性问题。核心贡献在于设计了一种分布式算法，该算法通过两项关键策略实现可扩展性：一是将信息中继限制在单跳通信内，二是保持智能体间消息的简洁性（仅传输自身动作信息）。尽管信息访问受限，算法通过在线优化智能体的通信邻居关系，实现了近乎最优的动作协同。论文还定义了“协调价值”这一信息论度量，以量化每个智能体从邻居获取信息的收益，并据此证明了算法在任何时间、任意网络拓扑（包括非连通图）下都具有严格正值的次优性界。仿真验证了该方法在收敛速度和最终性能上优于现有基准，甚至超过了某些拥有环境先验知识的基准方法。其意义在于为大规模分布式智能体系统在严苛通信约束下实现高效协同提供了首个可理论保证且支持网络自优化的解决方案。
