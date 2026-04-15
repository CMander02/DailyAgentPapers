---
title: "MolMem: Memory-Augmented Agentic Reinforcement Learning for Sample-Efficient Molecular Optimization"
authors:
  - "Ziqing Wang"
  - "Yibo Wen"
  - "Abhishek Pandy"
  - "Han Liu"
  - "Kaize Ding"
date: "2026-04-14"
arxiv_id: "2604.12237"
arxiv_url: "https://arxiv.org/abs/2604.12237"
pdf_url: "https://arxiv.org/pdf/2604.12237v1"
github_url: "https://github.com/REAL-Lab-NU/MolMem"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agentic Reinforcement Learning"
  - "Memory-Augmented Agent"
  - "Molecular Optimization"
  - "Sample Efficiency"
  - "Tool-Augmented Agent"
  - "Multi-Turn Agent"
relevance_score: 7.5
---

# MolMem: Memory-Augmented Agentic Reinforcement Learning for Sample-Efficient Molecular Optimization

## 原始摘要

In drug discovery, molecular optimization aims to iteratively refine a lead compound to improve molecular properties while preserving structural similarity to the original molecule. However, each oracle evaluation is expensive, making sample efficiency a key challenge for existing methods under a limited oracle budget. Trial-and-error approaches require many oracle calls, while methods that leverage external knowledge tend to reuse familiar templates and struggle on challenging objectives. A key missing piece is long-term memory that can ground decisions and provide reusable insights for future optimizations. To address this, we present MolMem (\textbf{Mol}ecular optimization with \textbf{Mem}ory), a multi-turn agentic reinforcement learning (RL) framework with a dual-memory system. Specifically, MolMem uses Static Exemplar Memory to retrieve relevant exemplars for cold-start grounding, and Evolving Skill Memory to distill successful trajectories into reusable strategies. Built on this memory-augmented formulation, we train the policy with dense step-wise rewards, turning costly rollouts into long-term knowledge that improves future optimization. Extensive experiments show that MolMem achieves 90\% success on single-property tasks (1.5$\times$ over the best baseline) and 52\% on multi-property tasks using only 500 oracle calls. Our code is available at https://github.com/REAL-Lab-NU/MolMem.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决药物发现领域中分子优化任务的样本效率低下问题。分子优化需要在有限的“先知”（oracle）评估预算内（例如昂贵的湿实验或高保真模拟），迭代改进先导化合物的特定性质，同时保持与原始分子的结构相似性。现有方法主要面临两大挑战：一是基于试错搜索的方法（如遗传算法、单步强化学习）由于缺乏先验知识，需要大量昂贵的先知调用，样本效率低；二是基于外部知识的方法（如利用大型离线数据集或预训练模型）虽然起步较快，但往往局限于模仿已知的转化模板，在面对超出模板范围的困难优化目标时表现不佳。这两种范式都缺乏一个关键机制：能够积累和复用经验的长期记忆。人类专家在进行优化时，会基于相关参考进行决策，并将成功的尝试转化为可重用的策略，这种从经验中学习的能力是实现样本高效优化的核心。因此，本文的核心问题是：**如何设计一个能够将多轮试错探索的轨迹提炼为长期、可检索的技能，从而实现样本高效分子优化的智能体框架？** 为此，论文提出了MolMem，一个融合了双记忆系统的多轮智能体强化学习框架，以模拟人类专家的学习与决策过程。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：分子优化方法、多轮智能体强化学习以及记忆增强智能体。

在**分子优化**领域，现有方法包括遗传算法、贝叶斯优化和强化学习等，旨在通过计算减少实验成本。然而，这些方法在有限的评估预算下常难以平衡属性提升与结构相似性。近期，大语言模型被用作灵活的分子编辑器，但通常以单步方式运行，未能系统地从完整优化轨迹中学习，限制了其在严格预算下的跨轨迹改进能力。本文提出的多轮框架正是为了克服这一局限。

在**多轮智能体强化学习**方面，该方法将大语言模型视为通过与环境交互学习的策略，而非单次生成器。它在语言任务中取得了进展，但在分子优化中应用较少，且通常仅将轨迹历史用作短期上下文，难以将有用见解迁移到后续优化中。本文则在此基础上，强调对轨迹进行密集的逐步奖励训练，以提升长期性能。

在**记忆增强智能体**方面，现有工作通过记忆机制跨步骤和任务复用信息。在分子设计中，记忆常表现为静态检索（如从数据库检索相似分子），但这类上下文通常只读，不随优化结果更新。而通用智能体（如Voyager、ExpeL）则探索了以经验为中心的记忆，将成功轨迹提炼为可复用技能。本文的创新在于，结合了静态范例检索（用于冷启动 grounding）与动态技能记忆（从成功轨迹中蒸馏可重用策略），专门针对分子优化中预算严格、需兼顾属性与相似性的挑战进行了定制。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MolMem的多轮智能体强化学习框架，并引入双记忆系统来解决样本效率低下的问题。其核心方法是利用外部知识和内部经验来增强智能体的决策能力，从而在有限的评估预算内实现更高效的分子优化。

整体框架基于一个多轮马尔可夫决策过程。其主要模块包括一个双记忆系统和一个两阶段的策略优化流程。双记忆系统由静态范例记忆和演化技能记忆组成。静态范例记忆存储了来自ChEMBL数据库的数百万个分子及其预计算的物理化学性质，用于在优化进程停滞时提供冷启动的参考。它通过两阶段检索机制工作：首先利用分子的摩根指纹通过FAISS进行近似最近邻搜索，然后通过塔尼莫托相似度约束和目标任务得分进行重排序，确保检索到的范例既与当前分子相关，又保持与初始先导化合物的相似性。演化技能记忆则从智能体自身成功的高奖励轨迹中蒸馏出可重用的策略。其形成过程是：从多轮交互中提取高奖励改进的分子对转换，构建包含编辑分解、骨架分析、官能团变化等信息的结构化编辑卡片，然后使用一个总结性大语言模型将其提炼成可操作的策略语句（如“将芳香环上的甲氧基替换为氟以提升目标分数”）。这些技能被存储并索引。在检索时，它采用混合匹配策略，同时考虑指纹相似度和官能团集合的杰卡德相似度，并优先选择改进幅度大的技能。

创新点在于：1）设计了按需触发的记忆检索机制，仅在优化进程停滞时引入外部指导，鼓励智能体前期独立探索，避免过度依赖记忆。2）将昂贵的多轮交互轨迹转化为可长期重用的结构化技能知识，实现了跨轮次的经验复用。3）在策略优化中，结合了监督微调初始化，并采用近端策略优化算法，利用密集的步进式奖励进行训练，使得智能体能够从包含记忆增强状态的信息中进行学习，从而将单步决策与长期知识积累相结合。这种方法将代价高昂的试错过程转化为了可持续积累和利用的知识，显著提升了样本效率。

### Q4: 论文做了哪些实验？

论文在单属性和多属性优化任务上进行了广泛的实验。实验设置方面，作者将对比方法分为三类：Novice（如Graph-GA、QMO、Reinvent 4）、Apprentice（包括检索、提示、SFT和特定任务LLM等方法）以及Expert（即本文提出的MolMem）。MolMem使用Qwen2.5-1.5B作为骨干模型，并设置了静态范例记忆和演化技能记忆的双记忆系统。

使用的数据集/基准测试包括五个单属性优化任务：QED、plogP、SA、DRD2和JNK3，以及多属性优化任务。评估时，每个任务仅允许进行500次昂贵的oracle调用，以评估样本效率。关键指标包括成功率（SR，要求分子与原始分子的Tanimoto相似度≥0.4）、相似度（Sim）和相对改进（RI）。

主要结果显示，MolMem在单属性任务上取得了显著优势。具体数据指标为：在QED任务上成功率为91.0%，plogP为100.0%，SA为63.5%，DRD2为96.0%，JNK3为98.5%，平均成功率约为90%，是最好基线方法（如PEIT-LLM）的1.5倍。在多属性任务上，MolMem也达到了52%的成功率。与基线相比，即使是参数规模更大的任务特定LLM（7B-8B），其性能也普遍低于使用紧凑骨干（1.5B）的MolMem，这验证了其双记忆系统和强化学习框架的有效性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其静态范例记忆和演化技能记忆的构建与检索机制仍有优化空间。例如，静态记忆可能无法充分覆盖多样化的分子空间，而技能记忆的蒸馏过程可能丢失部分关键决策细节。未来研究可探索更动态的记忆更新策略，例如引入遗忘机制或基于不确定性的记忆筛选，以提升记忆的时效性和相关性。

结合个人见解，可能的改进思路包括：1）引入图神经网络增强分子结构的表征能力，使记忆中的范例和技能能更好地捕捉分子间的拓扑相似性；2）结合元学习框架，让智能体能够快速适应新的优化目标，减少对历史记忆的过度依赖；3）探索多智能体协作机制，通过分布式记忆共享加速知识积累。此外，可考虑将外部化学知识库（如反应规则库）以结构化形式融入记忆系统，进一步提升决策的合理性。

### Q6: 总结一下论文的主要内容

该论文针对药物发现中分子优化任务面临的样本效率挑战，提出了一种名为MolMem的记忆增强智能体强化学习框架。核心问题是：在昂贵的真实评估（oracle calls）预算有限下，如何通过迭代优化先导化合物，有效提升分子属性并保持结构相似性。

方法上，MolMem构建了一个包含静态范例记忆和演化技能记忆的双记忆系统。静态记忆用于初始阶段检索相关范例进行决策引导，演化记忆则通过蒸馏成功轨迹，将经验提炼为可复用的优化策略。在此基础上，框架采用多轮智能体强化学习，并利用密集的步骤级奖励训练策略，从而将高成本的尝试过程转化为长期知识，提升未来优化效率。

主要结论显示，MolMem在仅使用500次真实评估的严格限制下，于单属性优化任务上取得了90%的成功率（达到最佳基线方法的1.5倍），在多属性任务上也实现了52%的成功率。其核心贡献在于通过记忆机制实现了经验的有效积累与复用，显著提升了样本效率，为数据昂贵的分子优化问题提供了新的解决方案。
