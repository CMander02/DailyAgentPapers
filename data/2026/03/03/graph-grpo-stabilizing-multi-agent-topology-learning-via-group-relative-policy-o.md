---
title: "Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization"
authors:
  - "Yueyang Cang"
  - "Xiaoteng Zhang"
  - "Erlu Zhao"
  - "Zehua Ji"
  - "Yuhang Liu"
  - "Yuchen He"
  - "Zhiyuan Ning"
  - "Chen Yijun"
  - "Wenge Que"
  - "Li Shi"
date: "2026-03-03"
arxiv_id: "2603.02701"
arxiv_url: "https://arxiv.org/abs/2603.02701"
pdf_url: "https://arxiv.org/pdf/2603.02701v1"
categories:
  - "cs.CL"
tags:
  - "多智能体系统"
  - "Agent架构"
  - "通信拓扑"
  - "强化学习"
  - "策略优化"
  - "训练稳定性"
  - "信用分配"
relevance_score: 9.0
---

# Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization

## 原始摘要

Optimizing communication topology is fundamental to the efficiency and effectiveness of Large Language Model (LLM)-based Multi-Agent Systems (MAS). While recent approaches utilize reinforcement learning to dynamically construct task-specific graphs, they typically rely on single-sample policy gradients with absolute rewards (e.g., binary correctness). This paradigm suffers from severe gradient variance and the credit assignment problem: simple queries yield non-informative positive rewards for suboptimal structures, while difficult queries often result in failures that provide no learning signal. To address these challenges, we propose Graph-GRPO, a novel topology optimization framework that integrates Group Relative Policy Optimization. Instead of evaluating a single topology in isolation, Graph-GRPO samples a group of diverse communication graphs for each query and computes the advantage of specific edges based on their relative performance within the group. By normalizing rewards across the sampled group, our method effectively mitigates the noise derived from task difficulty variance and enables fine-grained credit assignment. Extensive experiments on reasoning and code generation benchmarks demonstrate that Graph-GRPO significantly outperforms state-of-the-art baselines, achieving superior training stability and identifying critical communication pathways previously obscured by reward noise.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的多智能体系统中，通信拓扑结构动态优化所面临的训练不稳定和信用分配难题。研究背景是，随着大语言模型的发展，多智能体系统在复杂推理和代码生成等任务上展现出强大能力，而智能体间的通信拓扑结构（即信息交换的图结构）是影响系统性能的关键因素。现有方法（如EIB-LEARNER）虽然能够动态生成任务特定的拓扑，但其优化范式通常依赖于强化学习中的单样本策略梯度（如REINFORCE算法）和绝对奖励（如二进制的任务正确性）。这种范式存在两个主要不足：一是梯度方差高，因为数据集中查询任务的难度不均，简单查询可能使大量次优拓扑侥幸获得正奖励，引入噪声，而困难查询则常因失败导致梯度消失；二是信用分配问题，当拓扑成功时，现有方法将奖励均等地归因于图中的所有边，无法区分哪些连接是成功的关键、哪些是冗余的，从而阻碍模型学习精确的结构模式。

本文要解决的核心问题是如何在离散的拓扑结构搜索中实现稳定、高效的优化，以准确识别出对任务成功至关重要的通信路径。为此，论文提出了Graph-GRPO框架，通过引入群体相对策略优化来应对上述挑战。该方法的核心创新在于，对于每个查询，采样一组多样化的通信拓扑，并基于群体内的相对性能（而非绝对奖励）来计算每条边的优势值。这种群体比较机制能动态归一化奖励，过滤掉因任务简单性带来的噪声，并实现细粒度的信用分配，从而稳定训练过程并提升学习效果。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多智能体系统框架、自适应通信拓扑学习，以及强化学习优化策略。

在多智能体系统框架方面，早期工作如CAMEL和AutoGen通过角色扮演和对话实现协作，但它们通常依赖预定义的静态通信拓扑（如链式、星型或全连接图）。这些静态结构缺乏对任务复杂度的适应性，可能导致通信冗余或信息不足。

在自适应通信拓扑学习方面，近期研究致力于动态构建任务特定的图结构。例如，AgentPrune和AgentDropout采用剪枝技术从全连接图中移除冗余边；而G-Designer和EIB-LEARNER等生成式方法则利用图神经网络从头构建拓扑。其中，EIB-LEARNER从因果视角平衡错误抑制与洞察传播，为本文提供了架构基础。然而，这些方法大多依赖基于绝对二元奖励的标准策略梯度算法，存在梯度方差高和信用分配困难的问题。

在强化学习优化策略方面，PPO等算法虽广泛应用，但其依赖价值网络会带来内存开销和训练不稳定。近期提出的GRPO通过组内奖励归一化有效降低了数学推理任务的梯度方差，但其应用此前仅限于连续文本生成领域。本文的创新在于首次将组相对机制引入多智能体系统的离散结构搜索中，针对图拓扑学习中的边级信用分配挑战，设计了Graph-GRPO框架，从而在继承EIB-LEARNER等先进拓扑建模方法优点的同时，从根本上改进了优化过程的稳定性和鲁棒性。

### Q3: 论文如何解决这个问题？

论文通过提出Graph-GRPO框架来解决多智能体通信拓扑优化中的梯度方差和信用分配问题。其核心方法是引入分组相对策略优化（Group Relative Policy Optimization），通过细粒度的边级信用评估来稳定学习过程。

整体框架沿用G-Designer的策略网络架构，包含两个主要模块：节点编码器和结构生成器。节点编码器使用预训练的MiniLM模型将智能体角色描述与查询内容编码为特征向量。结构生成器采用图注意力网络（GAT）更新智能体嵌入，并通过双线性内积建模有向连接概率。关键创新在于施加了有向无环图（DAG）约束，强制信息从早期智能体流向后期智能体，确保推理过程的渐进性。

核心技术是边级Graph-GRPO机制。针对每个查询，策略网络采样K个不同的拓扑结构（通过伯努利采样实现），形成一组多样化的通信图。通过计算组内每条边的条件成功率（即该边存在时任务成功的经验概率），量化具体连接对任务成功的贡献。随后对边得分进行组内标准化，得到每条边的优势值，使高于平均贡献的边获得正强化，低于平均的边被抑制。这种方法无需额外的价值网络（Critic），降低了内存开销和训练不稳定性。

最终损失函数结合优势驱动的策略梯度与KL散度正则化项，防止策略偏离初始分布过远。推理阶段采用确定性阈值化生成稀疏拓扑。该方法通过组内相对评估有效消除了任务难度差异带来的噪声，实现了对关键通信路径的精准识别。

### Q4: 论文做了哪些实验？

论文在推理和代码生成领域进行了广泛的实验。实验设置方面，采用GPT-3.5-Turbo作为基础大语言模型，策略网络使用all-MiniLM-L6-v2编码器和3层GAT。智能体数量根据任务设定（MMLU为6，HumanEval为5，数学任务为4）。训练时，组采样大小K设为16，最大通信轮数为3，使用Adam优化器，学习率为1e-4。

使用的数据集/基准测试包括六个：通用推理领域的MMLU；数学领域的GSM8K、MultiArith、SVAMP和AQUA；以及代码生成领域的HumanEval。

对比方法分为三类：单智能体方法（如CoT、Self-Consistency）；固定拓扑结构（如Chain、Tree、Complete Graph、LLM-Debate）；以及拓扑优化方法（如AgentPrune、AgentDropout、G-Designer、EIB-LEARNER）。

主要结果如下：Graph-GRPO在所有六个基准测试中都达到了最先进的性能，平均准确率最高，为92.45%。与固定拓扑结构相比（平均性能约84%），其优势明显，例如完全图准确率仅为82.16%，凸显了拓扑修剪的必要性。与之前的动态拓扑优化方法相比，Graph-GRPO显著优于最强的基线EIB-LEARNER（91.38%），在复杂任务上优势更大，如在GSM8K上高出0.9%，在HumanEval上高出2.1%。消融研究表明，采用图级奖励的变体性能平均下降1.82%（在HumanEval上下降2.18%），验证了边级信用分配的重要性。此外，在效率方面，Graph-GRPO达到了帕累托最优前沿，在保持与AgentPrune相近的令牌消耗量的同时，实现了更高的准确率。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要体现在可扩展性和动态适应性两方面。在可扩展性上，当前基于GAT的策略网络具有O(N²)复杂度，虽然适用于小规模智能体群（如N≤6），但在大规模群体（如N>100）中会面临计算瓶颈，未来可探索分层或稀疏化的拓扑生成策略以提升效率。在动态适应性上，当前方法为每个查询生成静态拓扑，难以适应多轮对话中通信结构可能随轮次动态变化的需求，因此需要设计更细粒度的、支持轮级动态调整的拓扑优化机制。

进一步探索的点包括：1）算法层面，可研究如何将相对策略优化的思想与更高效的图神经网络（如线性化GNN或Transformer架构）结合，以降低计算复杂度并提升对大尺度群体的支持；2）应用场景层面，可扩展至长期交互任务，探索拓扑结构随任务进展的在线学习与演化机制，例如引入记忆模块或元学习策略；3）理论层面，可深入分析相对奖励归一化对信用分配问题的理论保证，以及梯度方差减少的量化影响，为方法提供更坚实的理论基础。这些方向有望进一步提升多智能体系统在复杂环境中的鲁棒性与适应性。

### Q6: 总结一下论文的主要内容

本文提出Graph-GRPO框架，旨在解决基于大语言模型的多智能体系统中通信拓扑优化的关键挑战。核心问题是现有方法依赖单样本策略梯度与绝对奖励（如二元正确性），导致梯度方差大且难以进行细粒度信用分配，即简单查询可能给予次优结构正向奖励，而困难查询则缺乏有效学习信号。为解决该问题，Graph-GRPO引入群体相对策略优化方法，其核心创新在于对每个查询采样一组多样化的通信图，并基于组内相对性能计算特定边的优势，通过组内奖励归一化来抑制任务难度差异带来的噪声，实现精细的边级信用分配。实验表明，该方法在推理与代码生成基准上显著优于现有基线，不仅提升了训练稳定性，还能识别出被奖励噪声掩盖的关键通信路径，最终收敛到稀疏且语义丰富的拓扑结构，在决策准确性与令牌效率之间达到帕累托最优平衡。
