---
title: "PivotRL: High Accuracy Agentic Post-Training at Low Compute Cost"
authors:
  - "Junkeun Yi"
  - "Damon Mosk-Aoyama"
  - "Baihe Huang"
  - "Ritu Gala"
  - "Charles Wang"
  - "Sugam Dipak Devare"
  - "Khushi Bhardwaj"
  - "Abhibha Gupta"
  - "Oleksii Kuchaiev"
  - "Jiantao Jiao"
  - "Jian Zhang"
  - "Venkat Srinivasan"
date: "2026-03-22"
arxiv_id: "2603.21383"
arxiv_url: "https://arxiv.org/abs/2603.21383"
pdf_url: "https://arxiv.org/pdf/2603.21383v1"
categories:
  - "cs.AI"
tags:
  - "Agent Post-Training"
  - "Reinforcement Learning"
  - "Supervised Fine-Tuning"
  - "Compute Efficiency"
  - "Generalization"
  - "Agentic Coding"
  - "Policy Optimization"
  - "On-Policy Rollout"
relevance_score: 9.0
---

# PivotRL: High Accuracy Agentic Post-Training at Low Compute Cost

## 原始摘要

Post-training for long-horizon agentic tasks has a tension between compute efficiency and generalization. While supervised fine-tuning (SFT) is compute efficient, it often suffers from out-of-domain (OOD) degradation. Conversely, end-to-end reinforcement learning (E2E RL) preserves OOD capabilities, but incurs high compute costs due to many turns of on-policy rollout. We introduce PivotRL, a novel framework that operates on existing SFT trajectories to combine the compute efficiency of SFT with the OOD accuracy of E2E RL. PivotRL relies on two key mechanisms: first, it executes local, on-policy rollouts and filters for pivots: informative intermediate turns where sampled actions exhibit high variance in outcomes; second, it utilizes rewards for functional-equivalent actions rather than demanding strict string matching with the SFT data demonstration. We theoretically show that these mechanisms incentivize strong learning signals with high natural gradient norm, while maximally preserving policy probability ordering on actions unrelated to training tasks. In comparison to standard SFT on identical data, we demonstrate that PivotRL achieves +4.17% higher in-domain accuracy on average across four agentic domains, and +10.04% higher OOD accuracy in non-agentic tasks. Notably, on agentic coding tasks, PivotRL achieves competitive accuracy with E2E RL with 4x fewer rollout turns. PivotRL is adopted by NVIDIA's Nemotron-3-Super-120B-A12B, acting as the workhorse in production-scale agentic post-training.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长视野智能体任务后训练中存在的计算效率与泛化能力之间的矛盾。当前，监督微调（SFT）方法计算效率高，但容易在分布外（OOD）场景下性能严重退化。相反，端到端强化学习（E2E RL）能保持OOD能力，却因需要多次完整的策略轨迹展开而计算成本高昂。现有尝试利用SFT轨迹进行RL的方法存在两个瓶颈：一是随机选择的中间步骤往往学习信号微弱，导致梯度更新无效；二是要求生成动作与演示数据严格字符串匹配过于苛刻，排除了许多功能等效的有效动作。

因此，本文的核心问题是：能否结合SFT的数据效率和E2E RL的泛化能力，在不进行完整轨迹展开的高成本下，同时提升任务域内精度并保持OOD性能？为此，论文提出了PivotRL框架。其核心解决方案是：首先，通过执行局部策略展开并筛选出“枢纽点”——即采样动作结果方差高、能提供强学习信号的中间步骤，从而仅需从这些状态进行简短的部分展开。其次，利用领域验证器为功能等效的动作赋予奖励，而非苛求与演示数据的严格匹配。理论分析表明，该方法能最大化域内学习信号，同时保持策略在与训练任务无关动作上的概率顺序，从而缓解OOD退化。实验证明，PivotRL在相同数据下，其域内精度提升优于SFT，且OOD回归显著减少；在智能体编码任务上，能以比E2E RL少4倍的展开步数达到与之竞争的精度。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类，围绕智能体后训练的效率与泛化权衡展开。

在方法类研究中，相关工作主要包括：1）监督微调（SFT），该方法计算效率高但常面临分布外（OOD）性能退化问题；2）端到端强化学习（E2E RL），能保持OOD能力，但依赖大量策略内（on-policy）轨迹展开，计算成本高昂；3）结合专家演示与RL更新的方法，旨在桥接离线与在线学习。此外，具有可验证奖励的RL（RLVR）在推理领域取得成功，而策略内蒸馏则用于缓解策略外分布偏移。

本文提出的PivotRL与上述工作密切相关但存在关键区别。它并非完全从头进行在线RL，而是创新性地在已有的SFT轨迹上操作，从而结合了SFT的计算效率与E2E RL的OOD准确性。具体而言，PivotRL通过局部策略内展开并筛选出关键决策点（pivots），以及采用功能等效奖励而非严格的字符串匹配，实现了高效且有效的优化。这区别于直接使用SFT令牌作为奖励或仅利用部分轨迹前缀的先前方法，专注于多轮工具使用的场景。

在应用类研究中，相关工作涉及智能体语言模型在工具使用、代码和网络导航等复杂环境交互中的探索。本文的工作直接定位于此类智能体任务，并通过实验在多个智能体领域验证了其提升效果。

### Q3: 论文如何解决这个问题？

PivotRL 通过一个创新的训练框架，在保持计算效率的同时提升模型的泛化能力，其核心在于两个关键机制：基于信息量的转折点筛选和基于验证器的功能等效奖励。

整体框架分为三个主要步骤。首先，从已有的监督微调轨迹中提取所有可能的转折点，构成候选数据集。其次，通过离线分析筛选出信息量高的“枢纽”转折点，这些状态在当前参考策略下能产生多样化的结果。最后，在这些选定的状态上进行局部策略采样，并使用基于验证器的奖励进行策略优化。

主要模块包括转折点筛选器和功能奖励机制。筛选器通过评估每个状态在参考策略下的奖励均值和方差，保留那些方差大于零且均值低于阈值的状态，确保训练集中在结果混合、尚未完全掌握的关键决策点上。功能奖励机制则使用领域特定的验证器来判断动作是否在功能上可接受，而非要求与演示数据严格字符串匹配。这允许模型探索多种等效的正确行为，增强了泛化能力。

创新点体现在两个方面。理论上，论文证明了奖励方差与自然梯度范数直接相关，因此筛选高方差状态能最大化学习信号；同时，功能奖励能在提升可接受动作概率的同时，最小化与参考策略的KL散度，并保持任务无关动作的概率顺序，从而保留领域外能力。实践上，PivotRL仅需在筛选后的少量关键状态进行短轨迹展开，大幅降低了端到端强化学习所需的大量交互成本，实现了效率与泛化的平衡。

### Q4: 论文做了哪些实验？

论文在四个智能体领域（对话工具使用、软件工程、终端控制、网页浏览）上分别进行了实验，评估基准分别为τ²-Bench、SWE-Bench Verified、Terminal-Bench和BrowseComp。所有实验均基于Qwen3-30B-A3B-Thinking-2507（Base模型），使用相同的提示词和专家轨迹数据，对比方法包括监督微调（SFT）和端到端强化学习（E2E RL）。

**主要结果如下：**
1.  **领域内性能**：PivotRL在三个基准上超越了相同数据的SFT，具体提升为：τ²-Bench (+5.37分)、Terminal-Bench (+6.25分)、BrowseComp (+9.80分)，平均领域内增益为+14.11（Base模型为基准），优于SFT的+9.94。在SWE-Bench上，PivotRL得分为32.67，略低于SFT的37.40。
2.  **领域外性能保持**：在八个领域外基准（如IFBench、AIME25、MATH500等）上，SFT平均性能下降9.83分，而PivotRL平均变化仅为+0.21分，基本保持了Base模型的性能，有效缓解了OOD退化问题。
3.  **计算效率**：在软件工程任务（SWE-Bench）上，PivotRL达到了与E2E RL相当的精度，但所需的环境交互轮次（rollout turns）减少了约4倍，墙钟时间减少了约5.5倍。
4.  **消融实验**：在τ²-Bench上的消融研究表明，移除关键组件会导致性能下降：移除枢轴过滤（pivot filtering）使准确率从63.81降至59.68；移除功能等价奖励（functional reward）则降至57.34，验证了二者均为必要设计。
5.  **大规模应用**：PivotRL被应用于Nemotron-3-Super-120B-A12B模型的后期训练，在其实验中，经过PivotRL阶段后，各智能体基准准确率均有显著提升（例如，SWE-Bench Verified从12.87提升至61.33）。

### Q5: 有什么可以进一步探索的点？

该论文提出的PivotRL框架在计算效率和泛化能力之间取得了良好平衡，但仍存在一些局限性和可进一步探索的方向。首先，当前方法依赖于程序化验证器（programmatic verifiers）来生成奖励信号，这限制了其在缺乏明确规则的任务（如开放式对话、创意写作）中的应用。未来可探索集成非程序化验证器，例如基于LLM的评判框架或过程奖励模型，以扩展其适用场景。

其次，PivotRL的“枢纽点”（pivot）检测机制基于动作结果的方差，这可能对噪声敏感或忽略潜在的重要决策节点。未来可研究更鲁棒的检测方法，例如结合不确定性估计或隐状态分析，以更精准地识别关键决策时刻。

此外，论文主要关注离线轨迹的利用，未来可结合在线学习策略，例如动态采样或主动探索，以持续优化策略并适应新任务。同时，当前实验集中于特定领域（如代码生成），未来需验证其在更复杂、多模态任务中的有效性，并探索如何平衡领域内性能与跨领域泛化能力，进一步减少灾难性遗忘。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为PivotRL的新型框架，旨在解决智能体长程任务后训练中计算效率与泛化能力之间的矛盾。核心问题是：监督微调（SFT）计算高效但易出现分布外（OOD）性能下降，而端到端强化学习（E2E RL）能保持OOD能力但计算成本极高。

PivotRL的核心方法是在已有的SFT轨迹上进行操作，结合两者的优势。它通过两个关键机制实现：首先，执行局部在策略轨迹展开，并筛选出“枢纽点”——即采样动作导致结果方差较高的信息丰富中间步骤；其次，利用功能等效动作的奖励，而非严格要求与SFT演示数据的字符串精确匹配。理论分析表明，这些机制能激励具有高自然梯度范数的强学习信号，同时最大程度保持与训练任务无关动作的策略概率顺序。

主要结论显示，在相同数据上，PivotRL相比标准SFT，在四个智能体领域平均提升了4.17%的域内准确率，在非智能体任务上提升了10.04%的OOD准确率。尤其在智能体编码任务中，PivotRL仅用E2E RL四分之一轨迹展开轮数就达到了与之竞争的准确率。其意义在于提供了一种高精度、低成本的智能体后训练方案，已被应用于NVIDIA的Nemotron-3-Super-120B-A12B模型，支持生产级智能体训练。
