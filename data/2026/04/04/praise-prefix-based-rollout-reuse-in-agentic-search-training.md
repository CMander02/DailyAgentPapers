---
title: "PRAISE: Prefix-Based Rollout Reuse in Agentic Search Training"
authors:
  - "Erhan Zhang"
  - "Yiqun Chen"
  - "Zechun Niu"
  - "Wei Yang"
  - "Xiaochi Wei"
  - "Yan Gao"
  - "Yi Wu"
  - "Yao Hu"
  - "Jiaxin Mao"
date: "2026-04-04"
arxiv_id: "2604.03675"
arxiv_url: "https://arxiv.org/abs/2604.03675"
pdf_url: "https://arxiv.org/pdf/2604.03675v1"
categories:
  - "cs.AI"
tags:
  - "Agentic Search"
  - "Reinforcement Learning"
  - "Multi-Hop QA"
  - "Data Efficiency"
  - "Credit Assignment"
  - "Intermediate Rewards"
  - "Rollout Reuse"
relevance_score: 8.0
---

# PRAISE: Prefix-Based Rollout Reuse in Agentic Search Training

## 原始摘要

In agentic search, large language models (LLMs) are trained to perform multi-turn retrieval and reasoning for complex tasks such as multi-hop question answering (QA). However, current search-based Reinforcement Learning (RL) methods suffer from two core limitations: expensive long-horizon rollouts are under-utilized during training, and supervision is typically available only at the final answer, resulting in severe reward sparsity. We present Prefix-based Rollout reuse for Agentic search with Intermediate Step rEwards (PRAISE), a framework for improving both data efficiency and credit assignment in agentic search training. Given a complete search trajectory, PRAISE extracts prefix states at different search turns, elicits intermediate answers from them, and uses these prefixes both to construct additional training trajectories and to derive step-level rewards from performance differences across prefixes. Our method uses a single shared model for both search policy learning and prefix answer evaluation, enabling joint optimization without extra human annotations or a separate reward model. Experiments on multi-hop QA benchmarks show that PRAISE consistently improves performance over strong baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体搜索（agentic search）训练中存在的两个核心问题：数据效率低下和奖励稀疏性。研究背景是，大型语言模型正从单次生成转向多步交互的智能体式问题求解，尤其在知识密集型任务（如多跳问答）中，模型需动态执行多轮检索与推理。当前基于搜索的强化学习方法通常将整个搜索轨迹视为单一训练样本，仅依据最终答案质量提供监督信号，这导致了两大不足：一方面，昂贵的多步轨迹中包含大量有信息的中间搜索状态未被充分利用，造成数据效率低下；另一方面，仅在轨迹末端提供奖励使得信用分配困难，难以判断哪些中间步骤对最终答案有贡献。因此，本文的核心问题是：如何最大化每个昂贵搜索轨迹的训练价值？为此，论文提出了PRAISE框架，通过利用搜索轨迹的前缀结构，将完整轨迹拆解为多个前缀状态，并基于这些前缀生成中间答案，从而既实现了轨迹重用以提升数据效率，又通过比较相邻前缀的答案质量差异构建细粒度的过程奖励，以改善信用分配。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、效率优化类和奖励设计类。

在**方法类**研究中，近期工作专注于训练大语言模型作为智能搜索代理，结合多步推理与外部检索。例如，Search-R1和R1-Searcher等代表性方法利用PPO或GRPO等强化学习框架，显著提升了复杂搜索任务的性能。同时，也有大量研究针对搜索中的特定组件（如规划、查询改写、文档选择）进行优化，并逐渐转向对这些模块化组件的联合优化以提升整体表现。本文的PRAISE框架属于此类，旨在优化智能搜索训练，但更侧重于解决数据效率和奖励稀疏性这两个核心限制。

在**效率优化类**研究中，提升数据效率是关键挑战。常见策略包括数据选择（如优先选择当前策略中等难度的问题）和轨迹重用（通过回放缓冲区或宽松的同策略更新重用近期数据）。近期工作如PROS和SPEC-RL研究了前缀重用以减少冗余生成，但它们主要针对数学或代码推理任务，其“前缀”定义在token序列上。本文的PRAISE则不同，它专门针对智能搜索任务，在搜索轮次（turn）层面提取前缀状态并构建额外训练轨迹，从而更直接地提升搜索训练的数据效率。

在**奖励设计类**研究中，为缓解长视野推理中的奖励稀疏问题，许多工作引入了更密集的监督信号。例如，StepSearch利用参考子问题等构建逐步奖励，ReasonRAG通过从部分状态展开来估计中间效用，而TIPS和IGPO则通过教师模型或策略模型本身定义轮次级奖励。PRIME展示了仅从结果监督中在线学习密集过程奖励的可能性。与这些方法不同，PRAISE直接从相邻搜索前缀之间的性能差异推导出步骤级奖励，无需人工标注或外部奖励模型，实现了在单一共享模型内的联合优化。

### Q3: 论文如何解决这个问题？

PRAISE 通过一种基于前缀的轨迹复用与中间步骤奖励框架，解决了智能体搜索训练中数据利用效率低和奖励稀疏两大核心问题。其核心方法是将一次完整的多轮搜索轨迹高效拆解并复用，同时利用前缀答案的质量差异构建细粒度的过程奖励，从而在无需额外人工标注或独立奖励模型的情况下，实现更高效和精准的信用分配。

整体框架包含三个主要阶段，对应论文中的图示。首先，在**主搜索轨迹生成**阶段，策略模型在搜索提示下执行多轮检索与推理，产生一条包含查询、多轮思考、搜索动作、观察结果以及最终答案的完整轨迹。随后，从该轨迹中按时间顺序提取出一系列**前缀状态**，每个前缀状态包含了截至某一搜索轮次的所有可用信息。

其次，在**前缀答案生成与轨迹复用**阶段，同一个模型切换到答案生成模式，基于每个提取出的前缀状态独立生成一个中间答案。这一关键步骤将单次昂贵的长视野搜索轨迹，转化为多个（T+1个）答案生成训练样本，极大地提高了每次搜索 rollout 的数据利用率，尤其对于轮次多的长轨迹效果显著。

最后，在**奖励构建与联合优化**阶段，框架通过一个可验证的答案评分函数，评估每个前缀答案和最终答案相对于标准答案的质量。其创新点在于，利用相邻前缀答案的得分差异来定义每一搜索轮次的**过程奖励**，从而将稀疏的终端监督信号转化为与搜索步骤对齐的密集反馈。同时，原始轨迹的最终答案仍获得**结果奖励**。这些奖励被稀疏地分配给轨迹中对应的决策时间点（如每轮搜索结束时）。此外，每个复用得到的前缀答案样本也获得其自身答案得分作为终端奖励。

所有样本（原始搜索轨迹和复用的前缀答案轨迹）被一同放入经验池，通过**共享的策略模型和评论家模型**，使用PPO算法进行联合优化。这使得模型在一个统一的训练过程中，同时优化搜索决策行为和基于部分信息的答案生成能力，而推理时仅需执行标准搜索，不增加额外开销。

### Q4: 论文做了哪些实验？

论文在HotpotQA和2WikiMultihopQA数据集上训练，并在NQ、HotpotQA、2WikiMultihopQA、Bamboogle和MuSiQue五个基准上进行评估。实验设置以Qwen2.5-7B为基础模型，使用verl训练框架、E5检索器，并在Wikipedia语料库上进行检索，评估指标为精确匹配（EM）和F1分数。

对比方法包括四类基线：1）非智能体方法（如直接LLM回答和朴素RAG）；2）智能体搜索方法（如Search-o1、Search-R1和R1-Searcher）；3）过程监督方法（如StepSearch、ReasonRAG和TIPS）。主要结果显示，PRAISE在所有五个基准的F1和EM上均取得最佳结果，显著优于基线。例如，在HotpotQA上F1达到60.62，在2Wiki上为58.14，在MuSiQue上为30.73。与R1-Searcher等强基线相比，在HotpotQA和2Wiki上提升尤为明显，表明其对多跳推理任务更有效。

消融实验分析了联合优化和过程奖励的贡献。移除联合优化（使用策略模型本身或冻结的Qwen模型作为评估器）会导致性能下降，如在HotpotQA上F1降低约3.46。移除过程奖励（α=0）或前缀评估器也会降低性能，如在MuSiQue上F1分别下降3.11和1.94。过程奖励权重α的实验显示，α=0.5时效果最佳，且PRAISE对α选择具有鲁棒性，正α值均能提升性能。联合优化策略使前缀评估器在训练中持续改进，进一步验证了其有效性。

### Q5: 有什么可以进一步探索的点？

该论文提出的PRAISE框架虽然有效，但仍存在一些局限性和值得探索的方向。首先，其核心依赖于从完整轨迹中提取前缀并评估中间答案，这假设模型本身已具备一定的推理和评估能力。若初始模型能力较弱，生成的前缀质量可能不高，从而影响训练效果。未来可研究如何结合更鲁棒或自适应的中间奖励机制，例如引入不确定性估计来过滤低质量前缀。

其次，方法目前主要在多跳问答任务上验证，其泛化性有待考察。可以探索在更复杂的决策任务（如代码生成、交互式问题解决）中的应用，这些任务可能涉及更长的规划视界和更稀疏的奖励。此外，共享模型设计虽然高效，但可能限制了搜索策略和评估函数的独立优化；未来可尝试轻量化的分离架构，在保持效率的同时提升灵活性。

另一个方向是改进前缀重用策略。当前方法基于固定间隔提取前缀，未来可引入动态选择机制，例如根据信息增益或置信度选择最具训练价值的前缀，以进一步提升数据利用率。最后，可探索将PRAISE与课程学习结合，逐步增加任务复杂度，以缓解训练初期的不稳定性。

### Q6: 总结一下论文的主要内容

该论文提出了PRAISE框架，旨在解决基于搜索的强化学习（RL）在训练智能体进行多轮检索与推理任务（如多跳问答）时面临的两个核心问题：长轨迹样本利用率低和最终答案监督导致的奖励稀疏性。PRAISE的核心方法是通过重用完整搜索轨迹中的前缀状态来提升数据效率和信用分配。具体而言，它从不同搜索轮次截取前缀状态，并基于这些前缀生成中间答案；这些前缀既用于构建额外的训练轨迹，也通过比较不同前缀的性能差异来推导步骤级奖励。该方法使用单一共享模型同时进行搜索策略学习和前缀答案评估，无需额外人工标注或独立奖励模型即可实现联合优化。实验表明，在多跳问答基准上，PRAISE能持续超越现有基线，显著提升任务性能，为高效训练搜索智能体提供了可扩展的解决方案。
