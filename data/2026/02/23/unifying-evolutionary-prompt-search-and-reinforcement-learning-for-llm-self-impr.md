---
title: "Unifying Evolutionary Prompt Search and Reinforcement Learning for LLM Self-Improvement"
authors:
  - "Lunjun Zhang"
  - "Ryan Chen"
  - "Bradly C. Stadie"
date: "2026-02-16"
arxiv_id: "2602.14697"
arxiv_url: "https://arxiv.org/abs/2602.14697"
pdf_url: "https://arxiv.org/pdf/2602.14697v2"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent Self-Improvement"
  - "Agent Architecture"
  - "Reinforcement Learning"
  - "Evolutionary Algorithms"
  - "Prompt Engineering"
  - "Reasoning"
  - "Generalization"
relevance_score: 9.5
---

# Unifying Evolutionary Prompt Search and Reinforcement Learning for LLM Self-Improvement

## 原始摘要

Building agentic systems that can autonomously self-improve from experience is a longstanding goal of AI. Large language models (LLMs) today primarily self-improve via two mechanisms: self-reflection for context updates, and reinforcement learning (RL) for weight updates. In this work, we propose Evolutionary System Prompt Learning (E-SPL), a method for jointly improving model contexts and model weights. In each RL iteration, E-SPL samples trajectories under multiple system prompts in parallel. It applies RL updates to LLM weights conditioned on system prompts, and evolutionary updates to system prompts via mutation and crossover, two genetic operators based on LLM self-reflection. Each system prompt is assigned a TrueSkill rating for evolutionary selection, updated from relative performance within each RL iteration. E-SPL encourages a natural division between declarative knowledge encoded in prompts and procedural knowledge encoded in weights, resulting in improved performance across reasoning and agentic tasks. For instance, in an easy-to-hard (AIME $\rightarrow$ BeyondAIME) generalization setting, E-SPL improves RL success rate from 38.8% $\rightarrow$ 45.1% while also outperforming reflective prompt evolution (40.0%). Overall, our results demonstrate that RL and evolutionary prompt search are deeply synergistic, and unifying the two yields consistent gains in sample efficiency and generalization. Code: https://github.com/LunjunZhang/E-SPL

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在自主自我改进过程中，如何协同优化模型权重与系统提示（上下文）这一核心问题。研究背景是，构建能够从经验中自主改进的智能体系统是AI的长期目标。当前LLM主要通过两种机制自我改进：一是通过自我反思来更新上下文（即提示工程），二是通过强化学习（RL）来更新模型权重。现有方法通常孤立地优化这两者：提示进化等方法专注于在离散、高层级的提示空间中进行探索以编码陈述性知识，而RL则擅长对固定的模型参数进行细粒度的梯度优化以编码程序性知识。这种分离导致两者的潜力未能充分协同，限制了智能体在样本效率和泛化能力上的进一步提升。

本文指出，将高层行为规范（提示）与底层参数策略（权重）的优化割裂开来是一个关键不足。因此，论文提出了进化系统提示学习（E-SPL）方法，其核心目标是统一进化提示搜索与强化学习，实现模型上下文与模型权重的联合优化。E-SPL在每次RL迭代中并行采样多个系统提示下的轨迹，一方面基于提示条件对LLM权重进行RL更新，另一方面利用基于LLM自我反思的变异和交叉这两种遗传算子对系统提示进行进化更新。每个提示根据其在迭代内的相对表现获得TrueSkill评分，用于进化选择。通过这种紧密耦合，E-SPL鼓励了陈述性知识（编码于提示）与程序性知识（编码于权重）的自然分工与协同进化，从而在推理和智能体任务上实现更优的性能与泛化能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为四类：提示演化与上下文记忆、面向大语言模型的强化学习、进化搜索与强化学习的结合，以及遗传编程。

在**提示演化与上下文记忆**方面，相关工作如EvoPrompt、PromptBreeder等采用基于种群的进化搜索优化提示，而Reflexion、Self-Refine等方法通过自我反思迭代优化上下文。这些工作均保持模型参数不变，仅优化上下文或提示。本文的E-SPL方法同样利用进化操作（如突变和交叉）和基于自我反思的评分来优化系统提示，但关键区别在于E-SPL将提示优化与模型权重更新相结合，而非冻结参数。

在**面向大语言模型的强化学习**方面，早期偏好学习方法及近期如o1、R1等工作专注于通过RL更新模型权重以提升推理和问题解决能力，但通常假设系统提示固定。本文同样使用RL更新权重，但创新性地将系统提示视为可优化的对象，在RL循环中联合优化提示和权重，从而减轻全局优化压力并提升泛化能力。

在**结合进化搜索与强化学习**方面，传统方法如ERL、PBT等结合种群动态与梯度优化，但不在提示层面操作。近期LLM引导的系统（如FunSearch）在代码层面进行进化搜索。本文的E-SPL直接针对系统提示进行进化搜索，并与RL在单一训练循环中深度融合，实现了程序性知识与陈述性知识的协同优化。

在**遗传编程**方面，现代GP方法在符号回归等领域表现优异，并将LLM视为一种程序。先前工作曾结合LLM遗传算子与DPO，但主要针对组合优化任务。本文则将GP范式应用于更通用的LLM后训练场景，进化生成能指导后续迭代的系统提示，以解决通用问题，且无需额外的智能体框架。

### Q3: 论文如何解决这个问题？

论文提出的E-SPL方法通过统一进化提示搜索与强化学习来解决LLM自主改进的问题。其核心是设计了一个协同框架，将基于权重的RL更新与基于系统提示的进化算法（EA）深度融合，使模型能同时优化上下文（提示）和权重。

**整体框架与主要模块**：E-SPL在每次RL迭代中并行使用多个系统提示。框架包含两个紧密耦合的循环：1) **RL循环**：对每个问题，模型在多个系统提示下采样轨迹，计算奖励，并执行策略梯度更新以优化模型权重。策略梯度目标条件于系统提示，鼓励权重专注于编码程序性知识。2) **进化循环**：重用RL产生的轨迹数据，无需额外评估成本。它通过TrueSkill评分系统持续评估提示的适应度，并基于评分进行选择，然后通过变异和交叉两种遗传算子生成新提示。

**关键技术细节**：
- **并行提示采样与竞争**：每次迭代采样M个系统提示，使权重不依赖于单一提示，并诱导提示间直接进化竞争。
- **基于TrueSkill的适应度评估**：将每次RL迭代视为锦标赛，根据提示在相同批次和权重下的相对表现（价值估计V_i排序）更新其TrueSkill评分（高斯分布）。这提供了跨迭代、可比较的持久能力估计，支持基于评分（μ+λσ）的乐观选择策略，平衡利用与探索。
- **基于自反思的遗传算子**：
  - **变异**：仅对当前迭代中表现最好的提示（argmax V_i）进行。首先使用参考模型对轨迹进行自反思，总结错误并生成教训；然后基于教训，以类似git diff的格式编辑原提示，生成变异后代。后代继承父代评分但增加不确定性（σ+Δσ）。
  - **交叉**：旨在重组多个父代优势。它构建一个得分矩阵Φ，记录每个提示在批次中每个问题上的平均奖励，从而识别各提示在不同问题上的相对优势。将这些信息输入交叉自反思提示，指导参考模型生成差异编辑，应用于最佳总体提示（argmax ΣΦ_i,b），产生融合多父代知识的新提示。其评分初始化为父代评分的加权平均。
- **知识分离**：条件化RL使系统提示编码可明确表述的陈述性知识（如策略原则），而模型权重编码隐性的程序性知识，降低了权重全局更新的优化压力。

**创新点**：
1. **无缝集成**：进化算法直接复用RL在策略数据，无需独立验证集，几乎无额外开销，与RL后训练流程高度兼容。
2. **相对评估与持久评分**：通过TrueSkill将噪声训练时排名转化为稳定、可比的技能评分，解决了因数据和权重变化导致的绝对回报不可比问题。
3. **自反思驱动的遗传操作**：变异和交叉均以LLM自反思为核心，使提示进化建立在经验总结与知识重组之上，而非随机扰动。
4. **协同效应**：进化提供多样化的、不断优化的陈述性知识（提示），改善RL探索与泛化；RL为进化提供性能反馈与数据，两者相互促进，在样本效率和泛化上获得一致增益。

### Q4: 论文做了哪些实验？

论文在数学推理和智能体搜索基准上进行了实验，主要评估了E-SPL方法。实验设置包括：使用DeepSeek-v3.1模型，在有限的数学推理数据上，通过强化学习（RL）更新模型权重，同时通过基于LLM自反思的突变和交叉操作进化系统提示。每个系统提示根据其在每次RL迭代中的相对表现分配TrueSkill评分以进行进化选择。

使用的数据集/基准测试包括：
1.  **DAPO100→AIME25**：在DAPO数据集的100个选定问题上训练，在AIME 2025竞赛题上测试。
2.  **HMMT 23/24→25**：使用HMMT 2023、2024和2025年2月的所有问题作为训练集，2025年11月的问题作为测试集。
3.  **AIME→BeyondAIME**：使用历年AIME（22、23、24年）作为训练集，在难度更高的BeyondAIME（原创问题集）上测试泛化能力。

对比方法包括：仅使用自反思（提示优化）、仅使用进化（提示优化）、仅使用RL（权重更新）。

主要结果与关键指标：
*   E-SPL（进化+RL）在所有方法中表现最佳，证明了联合优化提示和权重的协同优势。
*   在**AIME→BeyondAIME**的从易到难泛化设置中，E-SPL将RL的成功率从**38.8%提升至45.1%**，同时也优于仅进行反思性提示进化的方法（40.0%）。
*   结果表明，将RL与系统提示进化相结合，实现了一种任何单一方法都无法达到的协同自我改进形式，在样本效率和泛化能力上均获得了一致的提升。

### Q5: 有什么可以进一步探索的点？

该论文提出的E-SPL方法虽在统一进化提示搜索与强化学习上取得进展，但仍存在若干局限与可拓展方向。首先，其进化操作依赖LLM的自我反思生成新提示，成本较高且可能陷入局部最优；未来可探索更高效的提示空间搜索策略，如结合梯度信息的软提示优化或基于课程学习的渐进式提示演化。其次，方法主要针对单任务自我改进，未涉及多任务间的知识迁移；可研究如何通过共享提示库或元学习机制，使系统能在不同任务间复用与适配学到的提示知识。此外，实验集中于推理与代理任务，在更复杂的现实场景（如长期交互、动态环境）中的泛化能力仍需验证。最后，当前架构未明确处理“知识冲突”——当权重编码的程序性知识与提示中的声明性知识不一致时可能影响性能；未来可引入一致性约束或知识蒸馏技术，促进两类知识的协同优化。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为进化系统提示学习（E-SPL）的新方法，旨在统一进化提示搜索与强化学习，以实现大语言模型（LLM）的自主自我改进。核心问题是当前LLM主要通过上下文更新的自我反思和权重更新的强化学习（RL）两种机制进行改进，二者通常独立进行，未能有效协同。

E-SPL方法的核心是在每个RL迭代中并行采样多个系统提示下的轨迹。它基于系统提示条件更新LLM的权重（RL更新），同时利用基于LLM自我反思的突变和交叉这两种遗传算子，对系统提示进行进化更新。每个系统提示根据其在每次RL迭代中的相对表现，被分配一个TrueSkill评分，用于进化选择。这种方法促使声明性知识（编码于提示中）与程序性知识（编码于权重中）自然分离与协同优化。

主要结论表明，RL与进化提示搜索具有深刻的协同效应。在从易到难（AIME → BeyondAIME）的泛化设置中，E-SPL将RL成功率从38.8%提升至45.1%，并且优于单纯的反思性提示进化（40.0%）。统一两者在样本效率和泛化能力上带来了一致的增益，在推理和智能体任务上均实现了性能提升。其意义在于为构建能自主从经验中学习的智能体系统提供了一种更有效的统一框架。
