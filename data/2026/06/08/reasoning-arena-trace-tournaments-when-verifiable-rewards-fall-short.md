---
title: "Reasoning Arena: Trace Tournaments When Verifiable Rewards Fall Short"
authors:
  - "Han Zhou"
  - "Adam X. Yang"
  - "Laurence Aitchison"
  - "Anna Korhonen"
  - "Albert Q. Jiang"
date: "2026-06-08"
arxiv_id: "2606.09380"
arxiv_url: "https://arxiv.org/abs/2606.09380"
pdf_url: "https://arxiv.org/pdf/2606.09380v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM推理增强"
  - "可验证奖励强化学习"
  - "奖励信号设计"
  - "Trace锦标赛"
  - "智能体训练"
  - "竞技数学"
  - "代码生成"
relevance_score: 8.0
---

# Reasoning Arena: Trace Tournaments When Verifiable Rewards Fall Short

## 原始摘要

Reinforcement learning with verifiable rewards (RLVR) has become a leading paradigm for improving the reasoning ability of large language models through outcome-based supervision. However, verifiable rewards frequently become uninformative at the group level: when all sampled traces of a given prompt receive identical rewards, group-relative advantage estimation provides no gradient signal, even though the traces may differ substantially in reasoning quality. We propose Reasoning Arena, an adaptive training framework that routes such non-diverse reward groups to a judge system instead of discarding them. Beyond examining the final answer, Reasoning Arena constructs trace tournaments, where reasoning traces are compared head-to-head to expose finer-grained preferences within the group, converting reasoning quality into rich relative reward signals. To make reward estimation efficient, rather than exhaustively comparing every pair, each new trace is evaluated against a small, dynamically updated pool of previously generated traces as anchors to efficiently establish a relative ranking. We then fit a Bradley-Terry model on the incomplete comparison graph, enabling scalable RL integration without quadratic pairwise comparisons. Empirical results demonstrate that Reasoning Arena consistently outperforms the RLVR baseline by 7.6% on average in competition mathematics and coding benchmarks. By converting otherwise wasted zero-advantage samples into useful gradient updates, our method accelerates training by 27% to 41%, saving nearly 50% of generation compute, and substantially improves overall reasoning performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决在可验证奖励的强化学习（RLVR）训练大语言模型推理能力时，由于奖励信号缺乏多样性导致训练效率低下和梯度信号浪费的问题。现有方法通过结果监督进行组相对策略优化（如GRPO），依赖组内采样轨迹的奖励方差来提供梯度信号。然而，当数据难度与模型能力不匹配时（例如所有轨迹全对或全错），组内奖励会坍塌为常数，导致优势估计为零，无法为策略更新提供任何有效梯度。现有文献主要通过预过滤或难度预测来丢弃这些“非多样性奖励组”，但这不仅浪费了昂贵的生成计算资源，更丢失了隐藏在推理轨迹中关于推理质量、逻辑严密性等方面的细粒度学习信号。另一类方法通过熵引导进行奖励重塑，但完全依赖模型自身的词元分布，无法区分严谨的证明和自信的幻觉。因此，本文核心要解决的问题是：如何在RLVR框架下，有效利用这些被丢弃的非多样性奖励组中蕴含的丰富推理质量信息，将其转化为对策略优化有价值的梯度信号，从而提升训练效率与模型推理性能。

### Q2: 有哪些相关研究？

与本文相关的研究可分为两类：

1. **基于可验证奖励的强化学习（RLVR）方法**：这是当前训练推理模型的主流范式，通过结果导向的监督信号进行优化。典型工作包括DAPO（动态采样过滤全正确/全错误组）、DEPO和GRESO（数据筛选阶段跳过无信息提示），以及RL-ZVP、ZAPO（通过熵引导优势塑造从零方差组提取信号）和RLPR（用概率替代验证器）。本文区别于这些工作的核心在于：现有方法要么直接丢弃非多样组（浪费生成计算），要么从策略自身提取内在信号（无法区分严谨证明与幻觉推导）。本文提出自适应性引入外部裁判奖励，在RLVR梯度步内按组组合验证奖励和裁判奖励，使非多样组获得丰富梯度信号，同时保留精确验证器对信息组的驱动作用。

2. **大语言模型作为裁判的奖励方法**：此类方法在非可验证领域（如文本生成、文生图/视频）使用锦标赛排序进行配对比较产生奖励，典型工作包括RLAIF及其后续改进。本文在根本不同的设定下运作：推理任务中存在验证器但无法区分相同正确答案的中间推理轨迹。不同于完全替换验证器，本文将锦标赛嵌入RLVR框架中，仅在非多样奖励组上自适应调用裁判，在保留精确验证器作用的同时恢复丰富的相对排序信号。

### Q3: 论文如何解决这个问题？

Reasoning Arena通过自适应分组路由和迹线锦标赛来解决可验证奖励不足时零梯度问题。核心方法分为三个模块：首先，**自适应分组路由**根据奖励方差动态分配奖励源：若组内奖励有差异（D(G)=1），直接使用标准RLVR更新；若所有迹线获得相同可验证奖励（D(G)=0），则路由至迹线锦标赛。这确保计算昂贵但能评估推理质量的LLM法官仅作用于零梯度组。

其次，**迹线锦标赛**替代点式评分，采用两两比较迹线生成相对偏好信号。每对迹线通过法官输出软结果（胜/平/负），并引入顺序去偏（随机化呈现顺序与对称增广）消除位置偏差。为避免O(N²)的完整循环赛开销，采用**实时对手策略**：新迹线生成后，仅与当前最佳、最差和中位三条锚迹线进行对比，将比较复杂度降至O(N)。

最后，**Bradley-Terry奖励聚合**对非均匀采样产生的不完全比较图进行建模。通过最小化带L2正则化的软交叉熵损失，估计每条迹线的潜在推理强度βᵢ，再经min-max归一化为最终奖励。L2惩罚项防止稀疏比较图下的极端估值。整体架构的创新点在于：将原本零梯度的样本转化为有效梯度更新，训练加速27-41%且节省近50%生成计算量，在竞赛数学与编程基准上平均超越RLVR基线7.6%。

### Q4: 论文做了哪些实验？

论文在多个基准上进行了实验。**实验设置**：使用Ministral-3-8B-Instruct-2512作为策略模型，DeepSeekMath-V2为主要评判模型，并消融了Qwen3-235B-A22B和Qwen3.5-122B-A10B。训练使用STEM RL数据混合，过滤了编码和视觉推理数据，使代码任务成为分布外评估。**数据集/基准测试**：包括竞赛数学（AIME 2024/2025/2026、Beyond AIME）、研究生级领域推理（GPQA-Diamond）和代码推理（LiveCodeBench v6）。数学和GPQA-Diamond报告平均pass ratio@16，LiveCodeBench报告pass@5。**对比方法**：包括RLVR（CISPO基线）、RLAIF（逐点评判）、ArenaRL（全锦标赛无自适应路由）、Adaptive Pointwise（自适应路由+逐点评判）以及本方法Reasoning Arena（ours）和Reasoning Arena-Live（ours-Live）。**主要结果**：ours-Live平均得分53.9，比RLVR（46.3）提高7.6%，在AIME 2026上提升12.9分。训练效率上，ours-Live相比RLVR将墙钟步长减少27%-41%，每次步长生成数量减少近50%。消融实验表明，自适应路由机制和锦标赛形式均优于替代方案，且对不同评判模型（如Qwen系列）鲁棒。分析显示，锦标赛在“全对”组中惩罚逻辑跳跃，在“全错”组中奖励结构化推理，从而提供密集的信用分配信号。

### Q5: 有什么可以进一步探索的点？

这篇论文《Reasoning Arena》通过引入轨迹锦标赛机制，有效解决了RLVR框架中组级奖励无法区分时梯度信号消失的问题，但仍存在若干可探索的改进方向。首先，其评判系统的设计依赖于一组预先生成的锚定轨迹，这些锚点的质量与多样性会直接影响偏好估计的准确性，未来可探索自适应锚点选择策略，例如基于轨迹语义或推理步骤的聚类方法动态更新锚点集合。其次，Bradley-Terry模型假设偏好满足传递性，但实际长链条推理中可能存在循环偏好（如A优于B、B优于C但C反超A），需要引入非传递性偏好模型或图神经网络来捕捉复杂关系。此外，当前方法主要应用于数学和编程等可验证领域，向开放域推理（如创意写作或策略规划）扩展时，如何定义有效的锦标赛比较标准仍需研究。最后，可以尝试将稀疏比较图与在线强化学习的探索-利用平衡结合，利用不确定性采样主动生成最有价值的比较对，进一步提升训练效率。

### Q6: 总结一下论文的主要内容

强化学习与可验证奖励（RLVR）已成为通过结果监督提升大语言模型推理能力的主流范式，但面临关键瓶颈：当同一提示的所有采样推理轨迹获得相同奖励时，组相对优势估计无法提供梯度信号，尽管这些轨迹在推理质量上存在显著差异。本文提出推理竞技场（Reasoning Arena）这一自适应训练框架，将此类无区分奖励组路由至裁判系统而非丢弃。该方法通过构建推理轨迹锦标赛，进行轨迹两两比较以暴露组内细粒度偏好，将推理质量转化为丰富的相对奖励信号。为提升效率，每条新轨迹与动态更新的少量历史轨迹锚点比较，建立相对排名，再通过Bradley-Terry模型从不完全比较图中拟合奖励，实现无需二次比较的可扩展强化学习整合。实验表明，该方法在数学竞赛和编程基准测试中平均比RLVR基线提升7.6%，将原本无梯度样本转化为有效梯度更新，加速训练27%至41%，节省近50%生成计算量，显著提升整体推理性能。
