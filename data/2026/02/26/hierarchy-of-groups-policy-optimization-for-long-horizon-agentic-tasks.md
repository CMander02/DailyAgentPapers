---
title: "Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks"
authors:
  - "Shuo He"
  - "Lang Feng"
  - "Qi Wei"
  - "Xin Cheng"
  - "Lei Feng"
  - "Bo An"
date: "2026-02-26"
arxiv_id: "2602.22817"
arxiv_url: "https://arxiv.org/abs/2602.22817"
pdf_url: "https://arxiv.org/pdf/2602.22817v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Agentic Reinforcement Learning"
  - "Policy Optimization"
  - "Long-Horizon Tasks"
  - "Group-based RL"
  - "Advantage Estimation"
  - "Memory"
  - "Decision-Making"
relevance_score: 9.0
---

# Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks

## 原始摘要

Group-based reinforcement learning (RL), such as GRPO, has advanced the capabilities of large language models on long-horizon agentic tasks. To enable more fine-grained policy updates, recent research has increasingly shifted toward stepwise group-based policy optimization, which treats each step in a rollout trajectory independently while using a memory module to retain historical context. However, we find a key issue in estimating stepwise relative advantages, namely context inconsistency, where steps within the same group may differ in their historical contexts. Empirically, we reveal that this issue can lead to severely biased advantage estimation, thereby degrading policy optimization significantly. To address the issue, in this paper, we propose Hierarchy-of-Groups Policy Optimization (HGPO) for long-horizon agentic tasks. Specifically, within a group of rollout trajectories, HGPO assigns each step to multiple hierarchical groups according to the consistency of historical contexts. Then, for each step, HGPO computes distinct advantages within each group and aggregates them with an adaptive weighting scheme. In this way, HGPO can achieve a favorable bias-variance trade-off in stepwise advantage estimation, without extra models or rollouts. Evaluations on two challenging agentic tasks, ALFWorld and WebShop with Qwen2.5-1.5B-Instruct and Qwen2.5-7B-Instruct, show that HGPO significantly outperforms existing agentic RL methods under the same computational constraints. Code is available at https://github.com/langfengQ/verl-agent/tree/master/recipe/hgpo.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于分组的强化学习方法在长视野智能体任务中进行逐步策略优化时，所面临的历史上下文不一致问题。研究背景是，大语言模型驱动的智能体需要在复杂环境中执行长序列决策，而基于分组的强化学习（如GRPO）因其高效性已成为提升智能体性能的关键后训练范式。为了进行更细粒度的策略更新，近期研究转向了逐步策略优化框架，该框架将轨迹中的每一步独立处理，并利用记忆模块保留历史上下文。然而，现有方法（如GRPO及其扩展GiGPO）在估计逐步相对优势时存在一个关键缺陷：当同一分组内的多个步骤共享当前状态但历史上下文不同时，会导致优势估计出现严重偏差，即上下文不一致问题。本文的核心问题正是如何在这种逐步、分组的优化框架下，设计一种能够有效缓解历史上下文不一致带来的估计偏差，同时保持估计方差平衡的优势估计方法，以实现更稳定、高效的策略优化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于LLM的决策智能体、用于LLM智能体的强化学习，以及长视野智能体强化学习。

在基于LLM的决策智能体方面，早期工作如ReAct和Reflexion依赖于固定预训练模型和结构化提示，并辅以记忆、检索或工具调用机制。这些方法无需训练但适应性有限。本文的HGPO则属于需要训练优化的方法。

在用于LLM智能体的强化学习方面，早期研究将DQN、PPO等经典算法应用于文本环境。近期，为避免价值网络，出现了GRPO、Dr. GRPO等基于分组的RL算法，它们通过组内样本估计优势函数。然而，这些方法多针对单轮交互设计。本文的HGPO也属于分组RL范式，但专门针对长视野任务中组内步级优势估计的“上下文不一致”问题进行了改进。

在长视野智能体强化学习方面，研究旨在将LLM扩展至多轮决策。近期出现了对多轮轨迹进行优化的长视野策略优化框架，以及步级策略优化方法（将每一步独立处理但用记忆模块保留历史）。本文指出，现有的步级方法在长视野任务中会因历史上下文不一致而导致优势估计偏差。HGPO正是针对此问题，通过分层分组和自适应加权来改进步级优势估计，从而区别于前述各类方法。

### Q3: 论文如何解决这个问题？

论文通过提出“层次化组策略优化”（HGPO）方法，来解决长视野智能体任务中，基于逐步组策略优化时因历史上下文不一致导致的优势估计偏差问题。其核心思路是构建一个层次化的分组结构，对轨迹中的每一步进行多粒度分组，并自适应地聚合各组的优势估计，从而在偏差和方差之间取得更优的权衡。

整体框架包含两个关键组件：上下文感知的层次化分组和自适应加权优势估计。首先，在收集到一组从相同初始状态出发的轨迹后，HGPO不是简单地将具有相同当前状态的步骤归为一个组，而是根据历史上下文的一致性，将每个步骤分配到多个不同层级的组中。具体地，对于轨迹中的第 \(t\) 步，定义一个 \(k\)-步上下文操作符 \(\mathcal{C}_{k}(\bm{s}_{t}^{(i)})\)，它返回当前状态之前的 \(k\) 个历史状态。基于此，第 \(k\) 层级的组 \(G^{H}_{k}(\bm{s}_{t}^{(i)})\) 包含了所有具有完全相同 \(k\)-步历史上下文的步骤索引。这样形成了一个嵌套的层次结构：\(G^{H}_{0} \supseteq G^{H}_{1} \supseteq \cdots \supseteq G^{H}_{K}\)，其中 \(K\) 是最大上下文长度。\(G^{H}_{0}\) 对应传统的步级分组（仅当前状态相同），而更高层级的组要求更长的共同历史，因此组内上下文一致性更高，但组规模通常更小。

其次，进行自适应加权优势估计。对于每个层级 \(k\)，在组 \(G^{H}_{k}\) 内计算相对优势 \(A^{H}_{k}(\bm{s}_{t}^{(i)})\)，其定义为当前步骤的回报与组内平均回报的标准化差值。直观上，高层级组因上下文一致性强，优势估计的偏差更小，但可能因样本少而方差较大；低层级组则相反。HGPO 创新性地引入一个自适应权重 \(\bm{w}_{k} = (k+1)^{\alpha} / \sum_{k} (k+1)^{\alpha}\)（\(\alpha \geq 0\)）来聚合所有层级的优势估计，得到最终的优势值 \(A^{H} = \sum_{k=0}^{K} \bm{w}_{k} A^{H}_{k}\)。该加权方案倾向于给高层级组分配更高权重，以利用其更准确的比较，同时通过聚合所有层级来保持较低的方差。整个过程完全离线进行，无需额外模型或数据收集。

最终，策略优化目标采用近端策略优化（PPO）风格的裁剪目标函数，并加入与参考策略的KL散度惩罚项，使用计算得到的 \(A^{H}\) 作为优势估计进行更新。理论分析表明，HGPO 的优势估计器的偏差和方差介于步级估计器（\(k=0\)，方差低但可能偏差高）和Oracle估计器（\(k=K\)，偏差低但方差高）之间，从而实现了更好的偏差-方差权衡。在ALFWorld和WebShop任务上的实验表明，HGPO在不同模型规模下均显著优于现有的智能体强化学习方法。

### Q4: 论文做了哪些实验？

实验在ALFWorld和WebShop两个长视野智能体任务基准上进行，评估LLM智能体的多步决策能力。实验设置方面，采用Qwen2.5-1.5B-Instruct和Qwen2.5-7B-Instruct作为基础模型，所有强化学习方法共享相同的超参数配置，其中基于组的RL方法中的rollout组大小N设为8。对比方法包括闭源LLM（GPT-4o、Gemini-2.5-Pro）、提示方法（ReAct、Reflexion）以及RL训练方法（PPO、RLOO、GRPO、GiGPO）。主要结果显示，HGPO在所有RL训练方法中表现最佳。具体数据指标上，使用Qwen2.5-1.5B-Instruct时，HGPO相比GiGPO在ALFWorld（K=2）平均提升4.01%，ALFWorld（K=4）提升1.08%，WebShop（K=2）提升2.81%，WebShop（K=4）提升4.36%；使用Qwen2.5-7B-Instruct时，HGPO在ALFWorld分布内任务成功率最高达95.96%，WebShop任务成功率最高达79.29%。此外，HGPO在分布外任务上性能下降更少，显示出更好的泛化能力。实验还发现HGPO对小模型（1.5B）的提升更大（平均增益3.41% vs. 7B的0.74%），并随记忆大小K增加性能持续提升。

### Q5: 有什么可以进一步探索的点？

本文提出的HGPO方法通过分层分组策略优化缓解了上下文不一致问题，但仍存在一些局限性和值得探索的方向。首先，该方法依赖于轨迹分组，其分组策略的通用性和自适应能力有待验证，未来可研究更动态的分组机制，例如利用在线学习实时调整分组粒度。其次，当前优势估计的加权聚合方式虽能权衡偏差与方差，但可能未充分考虑不同任务的结构特性，可探索结合任务先验知识（如子目标依赖关系）的个性化聚合策略。此外，实验集中于特定领域（ALFWorld和WebShop），未来需在更复杂的多模态或现实世界任务中验证其泛化能力。从方法扩展角度看，可尝试将分层分组思想与模型基规划相结合，以进一步提升长视野决策的连贯性。最后，计算效率方面，尽管HGPO未引入额外模型，但分层计算可能增加开销，未来可研究轻量化分组算法以适配资源受限场景。

### Q6: 总结一下论文的主要内容

该论文针对长视野智能体任务中的策略优化问题，提出了一种新的层次化组策略优化方法（HGPO）。现有基于分组的强化学习方法（如GRPO）在逐步优化时，由于同一组内不同步骤的历史上下文可能不一致，导致优势估计存在偏差，即“上下文不一致”问题，这会严重影响策略优化的效果。

为解决这一问题，HGPO的核心创新在于引入了层次化分组机制。具体而言，在一组轨迹中，该方法根据历史上下文的一致性，将每个步骤分配到多个不同层次的组中。然后，为每个步骤分别计算其在各个组内的优势值，并通过一种自适应的加权方案进行聚合。这种方法能够在无需额外模型或环境交互的情况下，在逐步优势估计中实现更优的偏差-方差权衡。

论文在ALFWorld和WebShop两个具有挑战性的智能体任务上进行了评估，使用了Qwen2.5-1.5B-Instruct和Qwen2.5-7B-Instruct模型。实验结果表明，在相同的计算约束下，HGPO显著优于现有的智能体强化学习方法，验证了其有效性和优越性。
