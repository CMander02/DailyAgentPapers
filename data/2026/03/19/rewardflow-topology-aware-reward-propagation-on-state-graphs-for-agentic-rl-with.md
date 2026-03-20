---
title: "RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models"
authors:
  - "Xiao Feng"
  - "Bo Han"
  - "Zhanke Zhou"
  - "Jiaqi Fan"
  - "Jiangchao Yao"
  - "Ka Ho Li"
  - "Dahai Yu"
  - "Michael Kwok-Po Ng"
date: "2026-03-19"
arxiv_id: "2603.18859"
arxiv_url: "https://arxiv.org/abs/2603.18859"
pdf_url: "https://arxiv.org/pdf/2603.18859v1"
github_url: "https://github.com/tmlr-group/RewardFlow"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "强化学习"
  - "奖励塑形"
  - "状态图"
  - "Agentic Reasoning"
  - "LLM Agent 训练"
  - "过程奖励"
  - "图传播"
relevance_score: 8.0
---

# RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models

## 原始摘要

Reinforcement learning (RL) holds significant promise for enhancing the agentic reasoning capabilities of large language models (LLMs) with external environments. However, the inherent sparsity of terminal rewards hinders fine-grained, state-level optimization. Although process reward modeling offers a promising alternative, training dedicated reward models often entails substantial computational costs and scaling difficulties. To address these challenges, we introduce RewardFlow, a lightweight method for estimating state-level rewards tailored to agentic reasoning tasks. RewardFlow leverages the intrinsic topological structure of states within reasoning trajectories by constructing state graphs. This enables an analysis of state-wise contributions to success, followed by topology-aware graph propagation to quantify contributions and yield objective, state-level rewards. When integrated as dense rewards for RL optimization, RewardFlow substantially outperforms prior RL baselines across four agentic reasoning benchmarks, demonstrating superior performance, robustness, and training efficiency. The implementation of RewardFlow is publicly available at https://github.com/tmlr-group/RewardFlow.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大型语言模型（LLM）的智能体强化学习（RL）中，由于环境奖励稀疏而导致的细粒度优化困难问题。研究背景是，LLM作为自主智能体在与外部环境（如计算机控制、GUI操作）交互以完成复杂任务时，通常需要通过强化学习来优化其策略。然而，这类智能体环境往往只提供稀疏的终端奖励（仅在任务成功或失败时给出），缺乏对中间状态的过程反馈，这导致信用分配困难、训练信号不足，从而削弱了RL优化的效果。

现有方法试图通过训练专门的奖励模型来提供过程奖励，但这通常依赖于大量人工标注数据，并带来显著的计算成本和扩展性挑战。这些不足限制了智能体RL的效率和性能提升。

因此，本文要解决的核心问题是：如何在不训练额外奖励模型的情况下，客观、高效地为智能体推理任务中的中间状态估计细粒度的过程奖励？为此，论文提出了RewardFlow方法。其核心思想是利用从智能体推理轨迹中构建的状态图所蕴含的拓扑结构信息。通过将多个轨迹中的等价状态聚合为节点，并基于观察到的动作构建有向边，形成状态图。该方法随后通过图传播技术，将成功终端节点的奖励反向传播至中间状态，从而量化每个状态对最终成功的贡献度，生成客观的状态级奖励。这些密集奖励信号随后用于RL策略优化，以实现更有效的训练。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

**方法类**：主要包括传统的强化学习（RL）方法和基于奖励建模的方法。传统RL方法（如PPO）在智能体任务中常受限于稀疏的终端奖励，导致状态级优化困难。而基于奖励建模的方法（如训练独立的奖励模型）虽能提供过程奖励，但依赖大量人工标注数据和计算资源，成本高昂且可扩展性差。RewardFlow与这些方法的区别在于，它无需训练外部奖励模型，而是利用轨迹中状态的内在拓扑结构（构建状态图）来客观估计过程奖励，从而实现了轻量、高效的密集奖励生成。

**应用类**：涉及将LLMs与外部环境结合的智能体推理任务，例如计算机控制（如ALFWorld）、GUI操作（如WebShop）、机器人操控和游戏（如Sokoban）。先前研究通常直接应用标准RL算法或结合启发式奖励设计。RewardFlow则针对这类长视野、多状态的任务，通过图传播量化状态对成功的贡献，提供了更细粒度的优化信号，从而在多个基准上取得了更优性能。

**评测类**：包括用于评估智能体RL性能的基准测试，如Sokoban（推箱子游戏）、ALFWorld（文本型交互任务）、WebShop（在线购物任务）和DeepResearch（研究任务）。这些基准通常只提供稀疏的终端奖励。RewardFlow在这些基准上进行了广泛验证，其性能超越了之前的RL基线（如GRPO-based方法），展示了在成功率、鲁棒性和训练效率上的优势。

### Q3: 论文如何解决这个问题？

论文通过提出RewardFlow方法来解决智能体强化学习中终端奖励稀疏、难以进行细粒度状态级优化的问题。其核心思想是利用智能体推理轨迹中状态间的内在拓扑结构，构建状态图，并通过图传播技术量化每个状态对任务成功的贡献，从而生成密集的、状态级别的奖励信号。

整体框架分为两个主要阶段：状态图构建与奖励学习。

首先，在状态图构建阶段，方法从大语言模型策略采样的多条轨迹中聚合状态和动作。关键步骤包括：1）**状态与动作规范化**：通过一个规范化函数 \( f \) 将语义相同的原始状态映射到一致的规范表示，以消除观测中的表示变异性；同时，聚合等效动作并剔除环境无效的“幻觉”动作，以净化图结构。2）**构建统一状态图**：将处理后的所有轨迹中的唯一状态作为节点，有效的状态-动作-状态转移作为有向边，形成一个全局状态图 \( \mathcal{G}_{state} \)。该图近似了环境的底层概念图，其结构属性（如状态的可达性和中心性）揭示了状态对任务成功的前提贡献。

其次，在学习阶段，利用构建的状态图推导密集奖励并进行策略优化。具体包含：1）**基于图传播的奖励塑造**：从所有成功终端状态集合 \( \mathcal{S}_{succ} \) 出发，执行多源逆向广度优先搜索，计算每个状态节点到最近成功节点的最短跳数距离 \( d(\hat{s}) \)。基于此距离，为每个状态分配一个传播的过程奖励 \( R(\hat{s}) = \gamma^{d(\hat{s})} \)，其中 \( \gamma \in (0,1] \) 为折扣因子。这使得越接近成功的状态奖励越高。2）**动作级奖励计算**：将图节点的奖励投影回原始轨迹中的状态，并为每个转移 \( (s_t, a_t, s_{t+1}) \) 定义动作形奖励 \( \tilde{r}(s_t,a_t) = R(s_{t+1}) - R(s_t) \)。该差值提供了每一步动作是靠近还是远离成功的即时、可解释的信用分配。3）**协同优势估计**：为了更稳健的优化，方法结合了两种粒度的优势信号。**动作级优势**通过聚合经过同一规范状态的所有观察到的动作奖励，计算其相对于该状态平均表现的标准化差值，提供细粒度的本地指导。**轨迹级优势**则基于整个轨迹的成功与否（二元奖励）进行标准化，提供全局监督。两者通过超参数加权结合，形成最终的协同优势 \( A_{t,k}^{(i)} \)，确保在数据稀疏时也有有效引导。4）**策略更新**：采用类似PPO的裁剪替代目标函数，利用计算出的协同优势更新策略，鼓励选择局部更优且全局有效的动作，并通过KL散度项防止策略偏离参考策略过多。

创新点在于：1）**轻量级的图结构利用**：无需训练复杂的奖励模型，直接利用采样轨迹的拓扑结构来量化状态贡献。2）**拓扑感知的奖励传播**：通过逆向BFS在状态图上传播成功信号，生成具有全局一致性的密集状态奖励。3）**多粒度协同优势**：融合动作级和轨迹级优势，兼顾了细粒度信用分配和全局任务成功的监督，提升了学习的鲁棒性和效率。

### Q4: 论文做了哪些实验？

论文在四个智能体推理基准上进行了实验：文本环境ALFWorld、WebShop、DeepResearch和视觉环境Sokoban。实验设置方面，使用不同规模的Qwen2.5系列模型（如1.5B、3B、7B）进行训练，并采用E5作为嵌入模型来度量状态间的文本相似性。对比方法包括RLOO、GRPO、GiGPO等RL训练基线，以及在DeepResearch任务上的R1-Instruct、Search-R1等方法。

主要结果显示，RewardFlow在所有基准和模型规模上均优于先前方法。关键数据指标包括：在ALFWorld上，7B模型总体成功率高达89.8%，较最佳基线GiGPO提升7.0%；在Sokoban上，7B模型成功率达到62.4%，较GiGPO提升28.0%；在DeepResearch上，3B和7B模型的平均准确率分别为44.3%和49.1%，均优于基线。此外，在分布外环境评估中，RewardFlow表现出更强的鲁棒性，性能下降幅度更小。消融实验证实了状态归一化和噪声转移剪枝对性能提升的关键作用。效率分析表明，其图构建和奖励传播的开销可忽略不计。

### Q5: 有什么可以进一步探索的点？

基于论文内容，RewardFlow方法虽然取得了显著效果，但仍存在一些局限性和值得探索的方向。首先，该方法高度依赖状态图的构建质量，其核心假设是状态间的拓扑关系能有效反映贡献度。然而，在状态表征高度复杂或动态变化剧烈的环境中（如部分实时决策场景），如何稳定、准确地构建图结构仍具挑战。未来可探索更鲁棒的状态相似性度量或自适应图构建机制。

其次，RewardFlow在实验中对任务完成状态（成功/失败）有明确依赖，这在现实世界中往往难以获得。可研究如何结合弱监督或自监督信号，在仅有部分或稀疏反馈的场景下进行奖励传播。此外，论文主要测试了离散决策任务，未来可扩展至连续动作空间或更复杂的多智能体协作场景，验证其泛化能力。

从方法改进角度看，可考虑将奖励传播过程与模型的内在探索机制相结合，例如引入不确定性估计来权衡图传播奖励与环境原生奖励，以更好地平衡探索与利用。另外，当前方法未显式建模长期信用分配问题，未来可尝试将图传播与基于模型的规划相结合，进一步提升在超长视野任务中的效果。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型（LLM）在强化学习（RL）中因终端奖励稀疏而难以进行细粒度状态优化的问题，提出了一种名为RewardFlow的轻量级方法。其核心贡献在于无需训练额外奖励模型，通过利用推理轨迹中状态的内在拓扑结构来估计状态级奖励。具体方法为：首先构建状态图以分析各状态对任务成功的贡献，然后进行拓扑感知的图传播来量化贡献并生成客观、密集的状态级奖励。实验表明，将RewardFlow作为密集奖励用于RL优化，在四个智能体推理基准测试中，其在性能、鲁棒性和训练效率上均显著优于先前基线。这项工作为提升LLM的智能体推理能力提供了一种高效且可扩展的奖励设计新思路。
