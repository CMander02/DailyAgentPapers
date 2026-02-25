---
title: "Federated Causal Representation Learning in State-Space Systems for Decentralized Counterfactual Reasoning"
authors:
  - "Nazal Mohamed"
  - "Ayush Mohanty"
  - "Nagi Gebraeel"
date: "2026-02-23"
arxiv_id: "2602.19414"
arxiv_url: "https://arxiv.org/abs/2602.19414"
pdf_url: "https://arxiv.org/pdf/2602.19414v1"
categories:
  - "cs.LG"
  - "eess.SY"
  - "stat.ML"
tags:
  - "联邦学习"
  - "因果表示学习"
  - "状态空间模型"
  - "去中心化推理"
  - "工业控制系统"
  - "隐私保护"
relevance_score: 4.0
---

# Federated Causal Representation Learning in State-Space Systems for Decentralized Counterfactual Reasoning

## 原始摘要

Networks of interdependent industrial assets (clients) are tightly coupled through physical processes and control inputs, raising a key question: how would the output of one client change if another client were operated differently? This is difficult to answer because client-specific data are high-dimensional and private, making centralization of raw data infeasible. Each client also maintains proprietary local models that cannot be modified. We propose a federated framework for causal representation learning in state-space systems that captures interdependencies among clients under these constraints. Each client maps high-dimensional observations into low-dimensional latent states that disentangle intrinsic dynamics from control-driven influences. A central server estimates the global state-transition and control structure. This enables decentralized counterfactual reasoning where clients predict how outputs would change under alternative control inputs at others while only exchanging compact latent states. We prove convergence to a centralized oracle and provide privacy guarantees. Our experiments demonstrate scalability, and accurate cross-client counterfactual inference on synthetic and real-world industrial control system datasets.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决工业网络中相互依赖的资产（客户端）之间进行反事实推理的难题。研究背景是，现代工业系统（如电网、制造链）中的多个资产通过物理过程和控制输入紧密耦合，一个客户端的操作变化可能影响其他客户端的输出。然而，由于数据隐私和专有模型限制，传统集中式分析方法面临挑战：每个客户端的高维观测数据（如传感器读数）无法共享，且本地模型是私有且不可修改的，这阻碍了跨客户端的因果分析。

现有方法不足在于，它们通常假设数据可集中处理或忽略客户端间的动态耦合，无法在保护隐私和尊重本地模型的前提下，实现跨客户端的反事实推理（例如预测“如果另一个客户端采用不同控制策略，本客户端输出会如何变化”）。这限制了工业网络中的协同优化和故障分析能力。

本文要解决的核心问题是：如何在数据私有、模型本地的约束下，从分散的高维观测中学习因果表示，以支持去中心化的反事实推理。为此，论文提出一个联邦因果表示学习框架，将各客户端的高维数据映射为低维潜状态，分离内在动态与控制驱动的影响，并通过中央服务器估计全局状态转移和控制结构，从而仅通过交换紧凑的潜状态实现跨客户端的反事实预测，同时保证收敛性和隐私性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：联邦学习、因果表示学习以及状态空间模型与反事实推理。

在**联邦学习**方面，已有工作如FedAvg等专注于分布式模型训练，但通常假设数据同构且不涉及因果结构。本文则针对异构、高维的工业时序数据，在保持数据隐私和本地模型不变的前提下，通过交换低维潜状态进行协同学习，突破了传统联邦学习的限制。

在**因果表示学习**领域，现有方法多在集中式设定下从观测数据中识别因果变量。本文将其扩展至联邦场景，特别关注状态空间系统，旨在从分散的高维观测中解耦出内在动态与控制驱动的影响，这是对传统因果表示学习在分布式约束下的重要推进。

在**状态空间模型与反事实推理**方面，经典工作如线性动态系统或基于结构因果模型的反事实预测，通常需要集中数据或全局模型。本文的创新在于结合了联邦学习框架，使得各客户端仅共享压缩的潜状态，即可实现跨客户端的、基于全局状态转移结构的分布式反事实推理，这在工业控制系统的协同优化中具有独特价值。

### Q3: 论文如何解决这个问题？

论文通过提出一个联邦因果表征学习框架来解决分布式工业资产网络中，在数据隐私和模型专有性约束下进行跨客户反事实推理的难题。其核心方法是让每个客户端将高维观测数据映射到低维潜在状态空间，以解耦内在动态与控制驱动的影响，并通过中央服务器协同学习全局状态转移与控制结构，从而实现仅需交换紧凑潜在状态即可进行分布式反事实预测。

整体框架包含两个主要模块：一是本地客户端模块，每个客户端维护一个专有的编码器-解码器网络，将私有高维观测数据（如传感器读数）编码为低维潜在状态，并解码重构观测；同时，客户端还学习一个本地状态转移模型，描述自身状态如何受自身控制输入的影响。二是中央服务器模块，它聚合所有客户端上传的潜在状态序列和控制输入数据，估计一个全局状态转移模型，该模型刻画了不同客户端状态之间的相互依赖关系（即一个客户端的控制输入如何影响其他客户端的潜在状态）。这种分离设计使得原始数据始终保留在本地，只有潜在状态（而非原始数据）被共享，满足了隐私要求。

关键技术包括：1）**解耦表征学习**：通过约束潜在状态分解为内在动态分量和受控影响分量，使每个客户端的状态变化既可归因于自身控制，也能反映其他客户端控制的外部效应；2）**联邦交替优化**：训练过程采用交替步骤，客户端固定本地编码器/解码器，利用服务器下发的全局模型更新本地状态转移参数；服务器则固定全局模型，协助客户端优化表征以最小化重构误差和动态一致性损失；3）**分布式反事实推理**：推理时，客户端仅需向服务器提交当前潜在状态，服务器基于全局模型模拟其他客户端施加不同控制输入时的状态演变，并将结果潜状态返回给查询客户端，后者再用本地解码器生成反事实观测，从而在不暴露私有数据或模型的情况下完成跨客户影响预测。

创新点在于首次在状态空间系统中结合联邦学习与因果表征学习，实现了严格隐私保护下的分布式反事实推理；理论证明了该联邦框架收敛到集中式Oracle的性能，并提供了隐私保障；实验验证了其在合成和真实工业控制系统数据上的可扩展性与精确的跨客户反事实推断能力。

### Q4: 论文做了哪些实验？

该论文在合成和真实世界工业控制系统数据集上进行了实验验证。实验设置中，每个客户端维护一个本地编码器，将高维观测映射到低维潜在状态，并通过联邦学习在中央服务器上聚合全局状态转移和控制结构。数据集包括一个合成线性状态空间模型（用于验证理论）和一个来自真实工业控制系统的数据集（涉及多个相互关联的资产）。对比方法包括集中式Oracle（性能上界）、独立训练（每个客户端单独学习，忽略相互依赖）以及仅使用局部观测的基线方法。

主要结果显示，所提出的联邦因果表示学习方法在跨客户端反事实推理任务上显著优于独立训练和局部基线。关键数据指标上，在合成数据中，其反事实预测误差（均方误差，MSE）接近集中式Oracle，比独立训练降低了约60%；在真实数据中，同样实现了更准确的反事实估计，MSE比基线方法降低了约40-50%。实验还证明了方法的可扩展性，随着客户端数量增加，通信和计算成本仅线性增长，同时通过仅交换潜在状态保障了数据隐私。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于其假设的严格性，例如要求各客户端系统具有相同的状态空间维度，且控制输入的影响模式已知。这在实际工业场景中可能不成立，因为不同资产往往具有异构的动态特性。此外，框架依赖于一个可信的中央服务器进行全局结构学习，这在完全去中心化或存在拜占庭节点的环境中可能成为瓶颈。

未来研究方向可以从以下几个层面展开：一是**模型异构性**，探索如何放宽同构假设，使框架能适应状态维度或动态方程不同的客户端。二是**通信与隐私的进一步权衡**，研究在仅交换加密摘要或使用安全多方计算的情况下，如何保持推理精度。三是**扩展应用场景**，将方法从线性或弱非线性系统推广到更复杂的深度状态空间模型，并考虑存在未观测混杂因子的情况。结合个人见解，一个有趣的改进思路是引入**元学习或自适应机制**，让中央服务器能在线学习并调整聚合策略，以应对客户端数据分布漂移或局部模型悄悄更新的实际情况，从而提升系统的鲁棒性与长期适用性。

### Q6: 总结一下论文的主要内容

本文提出了一种面向状态空间系统的联邦因果表征学习框架，旨在解决工业资产网络中因数据隐私和模型专有性而难以进行跨客户端反事实推理的问题。核心贡献在于设计了一个去中心化的联邦学习框架，允许各客户端在无需共享原始高维观测数据或修改本地专有模型的前提下，协同学习系统的因果动态。

方法上，每个客户端将本地高维观测数据映射到低维潜在状态，以解耦其内在动态与控制输入的影响；一个中央服务器则聚合信息以估计全局状态转移和控制结构。这使得客户端仅需交换紧凑的潜在状态，即可预测在其他客户端采用不同控制输入时自身输出的变化，实现去中心化的反事实推理。

论文证明了该框架在理论上能收敛到集中式Oracle的性能，并提供了隐私保障。实验在合成和真实工业控制系统数据上验证了框架的可扩展性，以及其跨客户端反事实推断的准确性。该工作为隐私受限的分布式工业系统进行因果分析与决策提供了一种可行的新途径。
