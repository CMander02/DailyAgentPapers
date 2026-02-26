---
title: "Evolutionary System Prompt Learning for Reinforcement Learning in LLMs"
authors:
  - "Lunjun Zhang"
  - "Ryan Chen"
  - "Bradly C. Stadie"
date: "2026-02-16"
arxiv_id: "2602.14697"
arxiv_url: "https://arxiv.org/abs/2602.14697"
pdf_url: "https://arxiv.org/pdf/2602.14697v3"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent 自演化"
  - "Agentic 强化学习"
  - "系统提示学习"
  - "进化算法"
  - "LLM 自我改进"
  - "推理"
  - "Agent 架构"
relevance_score: 9.5
---

# Evolutionary System Prompt Learning for Reinforcement Learning in LLMs

## 原始摘要

Building agentic systems that can autonomously self-improve from experience is a longstanding goal of AI. Large language models (LLMs) today primarily self-improve via two mechanisms: self-reflection for context updates, and reinforcement learning (RL) for weight updates. In this work, we propose Evolutionary System Prompt Learning (E-SPL), a method for jointly improving model contexts and model weights. In each RL iteration, E-SPL samples trajectories under multiple system prompts in parallel, then jointly applies RL updates to LLM weights and evolutionary updates to system prompts. System prompts evolve via mutation and crossover, two genetic operators driven by LLM self-reflection; selection is based on relative performance ratings updated across RL iterations. E-SPL encourages a natural division between declarative knowledge encoded in prompts and procedural knowledge encoded in weights, resulting in improved performance across reasoning and agentic tasks. For instance, in an easy-to-hard (AIME $\rightarrow$ BeyondAIME) generalization setting, E-SPL improves RL success rate from 38.8% $\rightarrow$ 45.1% while also outperforming reflective prompt evolution (40.0%). Overall, our results demonstrate that RL and system prompt evolution are deeply synergistic, and combining the two yields consistent gains in sample efficiency and generalization. Code: https://github.com/LunjunZhang/E-SPL

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在自主自我改进过程中，如何协同优化模型权重（参数）与系统提示（上下文）这一核心问题。研究背景是，当前LLM主要通过两种机制自我提升：一是通过自我反思来更新上下文（如提示工程），二是通过强化学习（RL）来更新模型权重。然而，现有方法通常孤立地优化这两者——要么单独进化提示而不更新权重，要么仅用RL微调权重而固定提示。这种分离限制了模型的潜力，因为提示能编码高级的、陈述性知识（如策略和原则），而权重则蕴含低级的、程序性知识（如执行直觉）。论文指出，这种割裂使得两种优化范式（进化算法在离散结构上的探索与RL在连续参数上的精细调优）未能发挥协同效应，导致样本效率和泛化能力提升有限。

因此，本文提出的核心问题是：能否设计一个统一框架，在RL训练过程中联合优化模型权重和系统提示，从而利用两者的互补优势实现更有效的自我改进？为此，论文引入了进化系统提示学习（E-SPL）方法。该方法在每次RL迭代中并行采样多个系统提示下的轨迹，然后同步应用RL更新权重，并基于自我反思驱动的遗传操作（突变和交叉）来进化提示，选择依据则是在RL迭代中更新的相对性能评级。E-SPL旨在自然划分陈述性知识与程序性知识，通过提示进化促进结构化探索，通过RL梯度优化执行能力，最终提升模型在推理和智能体任务上的性能与泛化能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为四类。第一类是**提示演化与上下文记忆**，包括EvoPrompt、PromptBreeder等进化搜索方法，以及Reflexion、Self-Refine等基于自反思的上下文迭代优化方法。这些工作将提示或上下文视为可优化的对象，但通常固定模型权重。本文的E-SPL同样优化系统提示，但关键区别在于将其与模型权重的强化学习更新**联合优化**，突破了参数冻结的限制。

第二类是**面向大语言模型的强化学习扩展**，如基于偏好的对齐方法以及近期专注于推理的o1、R1等工作。这些研究通常假设训练期间系统提示固定，而本文则将上下文视为可程序化优化的对象，并探索其与RL的协同效应。

第三类是**进化搜索与强化学习的结合**，例如ERL、PBT等传统混合方法，以及FunSearch等LLM引导的程序级进化。本文受此启发，但专注于在单一训练循环中**共同进化系统提示和更新模型权重**，这与DGM等仅修改提示而不更新权重的工作不同。

第四类是**遗传编程**，其通过变异和交叉迭代改进程序。本文将特定系统提示下的LLM视为一个“程序”，并利用LLM本身设计遗传算子。与之前将LLM遗传算子与DPO结合、专注于组合优化任务的工作相比，本文解决的是更通用的LLM后训练场景，旨在发现能指导模型解决通用问题的系统提示。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“进化系统提示学习”的方法，将强化学习与进化算法相结合，协同优化模型权重和系统提示。其核心思想是在每个RL迭代中并行使用多个系统提示来采样轨迹，并同时更新模型权重和进化系统提示。

整体框架包含两个主要组件：强化学习和进化算法。在RL部分，模型在多个系统提示条件下并行采样轨迹，计算奖励和价值估计，然后通过策略梯度更新LLM权重。进化算法部分则维护一个系统提示种群，通过基于LLM自我反思的突变和交叉操作来进化提示，并使用TrueSkill评分系统持续评估和选择提示。

关键技术包括：1）**并行多提示采样**：每个RL迭代使用M个系统提示并行采样，防止权重过拟合到单一提示，并引入进化竞争。2）**无缝集成的适应度评估**：直接重用RL rollout产生的批次统计量评估提示性能，无需额外验证集，通过TrueSkill将相对排序转化为持久可比评分。3）**基于自我反思的遗传操作**：突变操作针对当前最佳提示，让参考模型反思轨迹错误并生成类似git diff的提示修改；交叉操作分析不同提示在特定问题上的优势，通过自我反思重组互补知识片段。4）**探索性选择策略**：基于TrueSkill评分的乐观估计（μ+λσ）进行采样，结合滑动窗口机制平衡探索与利用。

创新点在于首次将RL权重更新与系统提示进化联合优化，实现了陈述性知识（编码于提示）与程序性知识（编码于权重）的自然分离。该方法使RL能受益于不断进化的提示库，同时进化算法直接利用RL训练数据，几乎不增加额外开销。实验表明，这种协同作用显著提升了样本效率和泛化能力。

### Q4: 论文做了哪些实验？

论文在数学推理和智能体搜索基准上进行了实验。实验设置方面，主要使用DeepSeek-v3.1模型，对比了四种方法：仅自我反思（提示优化）、仅进化（提示优化）、仅强化学习（权重更新）以及本文提出的E-SPL方法（进化+强化学习）。

数据集和基准测试包括三个数学推理任务：1) DAPO100→AIME25，使用DAPO数据集的100个问题训练，在AIME 2025竞赛题上测试；2) HMMT 23/24→25，使用HMMT 2023、2024和2025年2月的问题训练，在2025年11月的问题上测试；3) AIME→BeyondAIME，使用历年AIME问题训练，在难度更高的BeyondAIME数据集上测试。此外还涉及智能体搜索任务。

主要结果显示，E-SPL方法在各项任务中均取得最佳性能。关键数据指标包括：在AIME→BeyondAIME的泛化设置中，E-SPL将强化学习的成功率从38.8%提升至45.1%，同时优于仅反射提示进化的40.0%。结果表明，联合优化系统提示和模型权重具有协同效应，显著提高了样本效率和泛化能力。

### Q5: 有什么可以进一步探索的点？

该论文提出的E-SPL方法将强化学习与基于进化的提示优化相结合，但仍存在一些局限性和值得探索的方向。首先，其进化过程依赖模型自反思生成突变和交叉，这可能导致搜索空间受限或陷入局部最优；未来可引入更丰富的遗传算子或外部知识库来引导提示变异，增强探索能力。其次，当前方法主要针对单任务优化，未来可研究如何将进化获得的提示知识跨任务迁移，实现终身学习或元提示学习。此外，实验集中于推理和智能体任务，在更复杂的现实环境（如多轮对话、具身交互）中的泛化能力仍需验证。另一个方向是降低计算成本，例如通过分布式进化或提示共享机制提升效率。最后，可探索权重更新与提示进化更精细的协同机制，例如动态调整两者学习速率，或让模型自主决策何时更新提示而非固定周期，从而进一步提升样本效率和性能上限。

### Q6: 总结一下论文的主要内容

该论文提出了进化系统提示学习（E-SPL）方法，旨在联合优化大语言模型（LLM）的上下文（系统提示）和模型权重，以实现自主的自我改进。核心问题是现有方法通常孤立地优化提示（如通过自反思或进化）或权重（如通过强化学习），未能充分利用两者之间的协同潜力。

E-SPL方法在每次强化学习迭代中并行采样多个系统提示下的轨迹，然后联合应用RL更新模型权重，并应用进化算法更新系统提示。系统提示通过突变和交叉两种遗传算子进行进化，这些算子由LLM的自反思驱动；选择则基于跨RL迭代更新的相对性能评级。这种方法鼓励将陈述性知识编码在提示中，而将程序性知识编码在权重中，形成自然分工。

主要结论表明，RL与系统提示进化具有深刻的协同作用。在从易到难（AIME → BeyondAIME）的泛化设置中，E-SPL将RL成功率从38.8%提升至45.1%，也优于仅进行反思性提示进化的方法（40.0%）。实验在多个数学推理和智能体任务上验证了该方法能一致提升样本效率和泛化性能，证明了联合优化比单一方法更有效。
