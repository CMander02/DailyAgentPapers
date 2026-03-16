---
title: "Collaborative Multi-Agent Optimization for Personalized Memory System"
authors:
  - "Wenyu Mao"
  - "Haoyang Liu"
  - "Zhao Liu"
  - "Haosong Tan"
  - "Yaorui Shi"
  - "Jiancan Wu"
  - "An Zhang"
  - "Xiang Wang"
date: "2026-03-13"
arxiv_id: "2603.12631"
arxiv_url: "https://arxiv.org/abs/2603.12631"
pdf_url: "https://arxiv.org/pdf/2603.12631v1"
categories:
  - "cs.MA"
tags:
  - "Multi-Agent"
  - "Memory System"
  - "Reinforcement Learning"
  - "Personalized LLM"
  - "Collaboration"
  - "Optimization"
relevance_score: 7.5
---

# Collaborative Multi-Agent Optimization for Personalized Memory System

## 原始摘要

Memory systems are crucial to personalized LLMs by mitigating the context window limitation in capturing long-term user-LLM conversations. Typically, such systems leverage multiple agents to handle multi-granular memory construction and personalized memory retrieval tasks. To optimize the system, existing methods focus on specializing agents on their local tasks independently via prompt engineering or fine-tuning. However, they overlook cross-agent collaboration, where independent optimization on local agents hardly guarantees the global system performance. To address this issue, we propose a Collaborative Reinforcement Learning Framework for Multi-Agent Memory Systems (CoMAM), jointly optimizing local agents to facilitate collaboration. Specifically, we regularize agents' execution as a sequential Markov decision process (MDP) to embed inter-agent dependencies into the state transition, yielding both local task rewards (e.g., information coverage for memory construction) and global rewards (i.e., query-answer accuracy). Then, we quantify each agent's contribution via group-level ranking consistency between local and global rewards, treating them as adaptive weights to assign global credit and integrate local-global rewards. Each agent is optimized by these integrated rewards, aligning local improvements with the global performance. Experiments show CoMAM outperforms leading memory systems, validating the efficacy of our proposed collaborative reinforcement learning for joint optimization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决个性化大语言模型（LLM）中多智能体记忆系统协同优化不足的问题。研究背景在于，记忆系统对于突破LLM上下文窗口限制、保存长期对话历史以实现个性化交互至关重要。典型的系统包含多个专门智能体，分别负责多粒度记忆构建（如提取关键事件或用户偏好）和个性化记忆检索。现有方法主要通过提示工程或微调独立优化每个智能体在本地任务上的表现，但它们忽视了智能体间的协作。这种独立优化将系统视为“本地专家的集合”，而非为全局目标协同演进的团队，导致局部优化无法保证全局系统性能。例如，独立优化的细粒度构建智能体可能存储冗余信息损害检索效果，而检索智能体若忽略构建策略可能过滤掉关键细节。

本文要解决的核心问题是如何对异构且异步执行的多智能体进行联合优化，以促进协作并实现局部改进与全局性能的对齐。这面临两大挑战：一是智能体在配置和任务执行上的异质性与异步性，使得端到端优化复杂；二是需要明确各智能体对全局目标的贡献度，避免均分奖励带来的模糊性。为此，论文提出了协同强化学习框架CoMAM，通过将智能体执行建模为序列马尔可夫决策过程来嵌入智能体间依赖关系，并利用本地奖励与全局奖励的一致性量化贡献，从而自适应分配全局奖励，驱动智能体在优化本地任务的同时协同提升系统整体表现。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：个性化LLM的记忆系统、多智能体系统优化以及信用分配。

在**个性化LLM的记忆系统**方面，已有工作如MIRIX通过设计元智能体和多个专用智能体来管理记忆，Mem-α和Mem1则分别利用强化学习优化记忆构建和记忆检索智能体。这些系统都采用了多智能体架构来处理记忆的构建与检索子任务，但本文指出它们主要关注单个智能体在其局部任务上的独立优化。

在**多智能体系统优化**方面，现有方法大多通过提示工程或微调对智能体进行独立优化，但这往往忽略了智能体间的协作，对全局系统性能的提升有限。近期研究如MAPoRL和MARFT开始转向基于强化学习的协作训练，以进行端到端的系统优化。本文提出的CoMAM框架属于这一协作优化范式，但进一步创新地将智能体执行过程规范化为序列马尔可夫决策过程，以显式建模智能体间的依赖关系。

在**信用分配**方面，这是多智能体强化学习中的一个核心挑战。朴素的方法是将全局团队奖励平均分配给所有智能体，但这会导致信用分配模糊，使智能体难以评估自身贡献，进而导致策略更新不稳定。本文的CoMAM框架通过基于局部奖励与全局奖励之间组级排序一致性的方法，来量化每个智能体的贡献，并以此作为自适应权重来分配全局信用、整合局部与全局奖励，从而更精细地解决了信用分配问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为CoMAM的协作式强化学习框架来解决多智能体个性化记忆系统中独立优化导致全局性能不佳的问题。其核心思想是将整个系统的执行过程建模为一个序列化的马尔可夫决策过程，并设计了一种自适应的信用分配机制，以联合优化各智能体，促进它们之间的协作。

整体框架基于一个标准的多智能体记忆系统，包含三个专门化的智能体：提取智能体（负责从对话历史中提取细粒度记忆）、画像智能体（负责从细粒度记忆中抽象出粗粒度记忆，如用户偏好）和检索智能体（负责从多粒度记忆集合中检索相关信息并生成个性化回答）。为了解决这些智能体在任务和运行频率上的异构性与异步性，CoMAM将整个构建与检索流程形式化为一个序列MDP。在这个MDP中，状态空间捕获了系统在每个步骤的状态（如原始历史、提取的记忆、查询等），动作空间定义了每个智能体的可执行动作，状态转移函数则明确地嵌入了智能体间的依赖关系（例如，画像智能体的输入是提取智能体的输出）。每个智能体执行其动作后，都会产生一个本地任务奖励（如提取覆盖率、抽象合理性、检索精度），而系统最终会基于回答准确性产生一个全局奖励。

该方法的创新点在于其自适应信用分配机制。它没有将全局奖励平均分配给各智能体，而是通过量化每个智能体对系统全局性能的贡献度来动态分配信用。具体而言，对于一组采样的MDP轨迹，计算每个智能体的本地奖励序列与全局奖励序列之间的排序一致性（使用NDCG指标）。这个一致性分数被归一化为自适应权重，用于将全局信用分配给各智能体。最终，每个智能体的优化信号是其本地奖励与分配到的全局信用的加权和。

通过这种方式，CoMAM在优化每个智能体策略时（使用GRPO算法），不仅考虑了其本地任务表现，还纳入了其对系统全局性能的贡献，从而实现了本地改进与全局性能的对齐，有效促进了智能体间的协作。实验表明，该框架优于现有的领先记忆系统。

### Q4: 论文做了哪些实验？

实验在PersonaMem基准数据集上进行，该数据集包含超过180段长期用户-LLM交互历史和约6000个后续多选题查询，并设置了32K、128K和1M三种不同历史长度（token数）的实验场景。实验对比了三大类基线方法：无记忆系统（Base、RAG）、基于提示构建的记忆系统（A-Mem、CAM、MemoryBank）以及基于强化学习优化的记忆系统（Mem1、Memory-R1）。主要评估指标为查询-回答准确率。

主要结果显示，CoMAM在所有上下文长度和Qwen、Llama两种骨干模型上均取得最佳性能。例如，在Qwen上，准确率在32K、128K、1M设置下分别达到0.64、0.70、0.66，相比最优基线Memory-R1提升幅度达8.5%至16.7%。消融实验验证了三个核心智能体（提取、画像、检索）的必要性，移除任一智能体均导致性能显著下降。此外，将智能体执行规范化为序列MDP并进行联合优化（MDP RL）的策略，显著优于独立优化智能体的策略（independent RL）。在信用分配方面，结合局部奖励与全局奖励的自适应机制（Ours）优于固定权重分配（MDP RL w/ LG），准确率进一步提升。训练效率上，联合优化虽可能增加单个智能体的收敛步数，但通过并行训练减少了总步数，例如在32K设置下，总步数从独立的160步降至68步。

### Q5: 有什么可以进一步探索的点？

本文提出的CoMAM框架虽在协同优化上取得进展，但仍存在若干局限与可探索方向。首先，其实验主要基于特定对话基准，泛化能力未在更开放、动态的真实场景（如多轮复杂任务规划）中得到充分验证。其次，框架依赖预定义的本地奖励（如信息覆盖率），这些奖励的设计仍较启发式，未来可探索端到端的奖励学习机制，使系统能自适应不同用户交互模式。此外，当前方法假设智能体执行顺序固定（序列MDP），实际协作中可能需要动态调整执行流或引入异步通信机制，以提升系统灵活性。另一个重要方向是扩展协同规模——当前工作聚焦于记忆构建与检索的少数智能体，未来可研究如何将协同强化学习推广至包含数十甚至上百个智能体的复杂系统，并解决信用分配中的可扩展性问题。最后，可结合理论分析（如博弈论或多智能体策略梯度理论）深入理解协同优化的收敛性与稳定性，为算法设计提供更坚实的理论基础。

### Q6: 总结一下论文的主要内容

该论文针对个性化大语言模型中的记忆系统优化问题，提出了一种协作式多智能体强化学习框架CoMAM。现有方法通常独立优化处理多粒度记忆构建和检索的各个智能体，忽视了跨智能体协作，导致局部优化无法保证全局系统性能。为解决此问题，CoMAM将异构智能体的异步执行建模为序列马尔可夫决策过程，在状态转移中嵌入智能体间依赖关系，并同时产生局部任务奖励（如记忆构建的信息覆盖率）和全局奖励（如查询回答准确率）。其核心贡献在于通过衡量局部与全局奖励之间的组级排序一致性来量化每个智能体对系统的贡献，并以此作为自适应权重来分配全局奖励份额，最终将局部与全局奖励整合以优化每个智能体，从而实现局部改进与全局性能的对齐。实验表明，CoMAM在长期个性化对话任务上优于现有领先的记忆系统基线，验证了所提协作强化学习框架对于联合优化多智能体记忆系统的有效性。
