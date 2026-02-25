---
title: "EBPO: Empirical Bayes Shrinkage for Stabilizing Group-Relative Policy Optimization"
authors:
  - "Kevin Han"
  - "Yuhang Zhou"
  - "Mingze Gao"
  - "Gedi Zhou"
  - "Serena Li"
  - "Abhishek Kumar"
  - "Xiangjun Fan"
  - "Weiwei Li"
  - "Lizhu Zhang"
date: "2026-02-05"
arxiv_id: "2602.05165"
arxiv_url: "https://arxiv.org/abs/2602.05165"
pdf_url: "https://arxiv.org/pdf/2602.05165v3"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "强化学习"
  - "策略优化"
  - "大语言模型"
  - "Agentic 强化学习"
  - "训练稳定性"
  - "推理能力"
  - "基准评测"
relevance_score: 7.5
---

# EBPO: Empirical Bayes Shrinkage for Stabilizing Group-Relative Policy Optimization

## 原始摘要

Reinforcement Learning with Verifiable Rewards (RLVR) has proven effective for enhancing the reasoning capabilities of Large Language Models (LLMs). However, dominant approaches like Group Relative Policy Optimization (GRPO) face critical stability challenges: they suffer from high estimator variance under computational constraints (small group sizes) and vanishing gradient signals in saturated failure regimes where all responses yield identical zero rewards. To address this, we propose Empirical Bayes Policy Optimization (EBPO), a novel framework that regularizes local group-based baselines by borrowing strength from the policy's accumulated global statistics. Instead of estimating baselines in isolation, EBPO employs a shrinkage estimator that dynamically balances local group statistics with a global prior updated via Welford's online algorithm. Theoretically, we demonstrate that EBPO guarantees strictly lower Mean Squared Error (MSE), bounded entropy decay, and non-vanishing penalty signals in failure scenarios compared to GRPO. Empirically, EBPO consistently outperforms GRPO and other established baselines across diverse benchmarks, including AIME and OlympiadBench. Notably, EBPO exhibits superior training stability, achieving high-performance gains even with small group sizes, and benefits significantly from difficulty-stratified curriculum learning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决强化学习与可验证奖励（RLVR）范式中，特别是主流方法组相对策略优化（GRPO）所面临的关键稳定性问题。研究背景是，为了提升大语言模型（LLM）的推理能力，利用数学解题、代码生成等任务中客观正确性作为奖励信号的RLVR方法已成为一种稳定且可复现的后训练范式。GRPO通过在同一提示词下采样的一组输出内部对奖励进行归一化来估计优势函数，避免了训练独立价值网络的计算开销，因而被广泛采用。

然而，现有GRPO方法存在明显不足。首先，其基线估计仅依赖于局部组内样本的均值，当计算资源受限、组规模较小时，估计器方差很高，导致训练不稳定。其次，GRPO在“饱和”失败场景下缺乏鲁棒性：当一个困难提示词对应的所有生成结果奖励均为零时，组内相对优势会消失，梯度信号为零，造成训练步骤的浪费。虽然已有方法尝试通过过滤或重加权不稳定更新来缓解波动，但这本质上丢弃了数据，导致数据利用率低下。因此，标准GRPO往往需要更大的组规模来抑制噪声，这显著增加了计算成本。

本文要解决的核心问题是：如何设计一种更稳定、高效的优势估计方法，以克服GRPO在高方差和小组规模下的不稳定性，以及其在全零奖励的饱和场景中梯度消失的问题。为此，论文提出了经验贝叶斯策略优化（EBPO）框架。其核心思想是引入经验贝叶斯推断，不再孤立地估计局部基线，而是通过一个收缩估计器，将噪声较大的局部组统计量向一个动态更新的全局先验均值收缩。这种方法能够区分模型是失败于一个全局意义上“困难”的任务（与先验一致），还是失败于一个“简单”的任务（偏离先验），从而分配自适应的惩罚信号，确保即使在饱和情况下也能提供非零梯度，同时显著降低估计方差，实现更高的样本效率和训练稳定性。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为两类：强化学习与可验证奖励（RLVR）方法，以及经验贝叶斯估计方法。

在**RLVR方法**方面，已有研究证明利用可自动检查的信号能有效提升大语言模型的推理与事实正确性。其中，基于组相对策略优化（GRPO）的各类变体是主流方法，它们通过整合可验证奖励来优化策略。这些研究致力于提升训练效果与效率，例如设计新的学习目标、引入基于熵的探索机制或构建更稳健的奖励函数。然而，它们大多未深入考虑优势计算中奖励均值或标准差的估计问题，而这会显著影响组间差异。本文的EBPO框架直接针对这一空白，通过经验贝叶斯方法更稳健地估计组奖励的统计量，从而稳定GRPO的训练动态。另一项相关研究同样关注GRPO的高方差问题，并利用斯坦悖论理论保证其收缩基线的方差降低。与之不同，EBPO采用经验贝叶斯推断，根据方差比动态控制收缩强度，这对于避免困难提示下的梯度消失至关重要。

在**经验贝叶斯估计**方面，该方法为处理并行噪声数据提供了框架，融合了频率统计的数据驱动特性与贝叶斯推断的层次建模结构，广泛应用于贝叶斯强化学习的超参数调优、多任务元学习中的先验估计、深度神经网络的不确定性估计以及贝叶斯对话代理的开发等领域。尽管贝叶斯原理已越来越多地用于大语言模型，但其应用主要局限于评估框架和黑盒优化（例如将LLMs集成到贝叶斯优化中进行超参数调优），而非在线策略训练。本文提出的EBPO是首个将经验贝叶斯直接集成到GRPO在线优化循环中的框架，利用收缩估计器在主动训练中稳定梯度方差。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为经验贝叶斯策略优化（EBPO）的新框架来解决GRPO方法在计算约束（小组规模）下估计器方差高，以及在所有响应都产生相同零奖励的饱和失败机制中梯度信号消失的稳定性挑战。其核心方法是利用经验贝叶斯收缩估计，将局部组统计量与通过全局历史数据更新的全局先验动态融合，从而正则化局部基线。

整体架构设计上，EBPO在标准的RLVR框架内运作。对于每个提示，策略采样一组响应并获得验证奖励。关键创新在于基线计算模块：它不再像GRPO那样仅使用局部组均值（μ_group），而是计算一个“智能基线”（V_q^{EB}）。该基线是局部组均值与全局先验均值（μ_glob）的加权平均，权重由收缩因子（S_q）决定。收缩因子取决于组内方差（σ²/G）和组间方差（τ²）的比率，确保在局部数据噪声大时更多地向全局先验收缩。

主要组件包括：1）**在线全局统计量估计器**：使用Welford在线算法动态更新全局成功率均值（μ_glob）、组内方差（σ²）和组间方差（τ²），避免了小批量统计的噪声。2）**收缩估计器**：根据方差比率计算收缩因子，并生成融合后的基线值。3）**优势计算模块**：基于正则化后的基线计算优势值，并进行批次级别的标准化。

关键技术及创新点包括：1）**经验贝叶斯收缩**：将每个提示的真实潜在成功率建模为来自一个全局高斯分布（均值为μ_glob，方差为τ²）的样本，通过数据估计先验参数，构造出具有更低均方误差的收缩估计量。2）**解决饱和失败机制**：当整个组奖励为零时，GRPO的基线等于零，导致优势信号消失；而EBPO的基线由于包含正的全局先验μ_glob，仍能产生非零的负优势信号，从而提供信息梯度。3）**理论保证**：论文证明了EBPO相比GRPO具有严格更低的基线估计均方误差、有界的熵衰减，以及在失败场景中非消失的惩罚信号。4）**与课程学习结合**：论文进一步提出按主题或难度对训练流进行聚类排序，使全局先验能更快适应局部数据分布，进一步减少先验估计误差，提升性能。

### Q4: 论文做了哪些实验？

论文实验设置方面，使用了DAPO-Math-17K数据集进行训练，并在多个数学推理基准上评估，包括AIME2024、AIME2025、AMC23、Math-500和OlympiadBench。评估指标为Pass@1，每个评估集重复运行32次以取平均值确保统计稳健性。使用的模型涵盖不同架构和规模，包括LLaMA3.1-8B、Qwen3-8B和Qwen3-14B。

对比方法包括Naive GRPO、DAPO、Dr. GRPO和EntropyMech。所有方法在相同条件下训练，包括数据顺序、批次大小和优化配置。此外，论文还评估了两种聚类采样策略：按主题聚类（EBPO-topic）和按难度聚类（EBPO-diff）。

主要结果显示，EBPO-topic在大多数模型和基准上均优于基线。例如，在Qwen3-8B上，EBPO平均Pass@1达到64.39%，比GRPO高出超过5个百分点。在15个（模型，数据集）组合中，EBPO在9个案例中取得最佳结果。关键数据指标包括：在Qwen3-8B上，EBPO-topic在MATH-500、AIME2024、AIME2025、AMC23和OlympiadBench的Pass@1分别为76.80%、56.04%、47.92%、86.25%和54.93%。

实验还分析了训练动态，显示EBPO能维持健康的梯度范数和非零的更新信号，而GRPO在训练后期出现梯度消失或更新幅度不稳定的问题。EBPO还表现出更强的探索行为，政策熵值更高。在样本效率方面，EBPO在小分组规模（如G=8）下仍能取得高性能，平均领先GRPO 11.28%。课程学习（EBPO-diff）进一步提升了在高端基准上的表现，例如在Qwen3-8B上，EBPO-diff在AIME2024和AIME2025上分别比GRPO-diff高出3.95%和6.04%。

### Q5: 有什么可以进一步探索的点？

本文提出的EBPO方法通过经验贝叶斯收缩估计器有效缓解了GRPO在小样本组和奖励饱和场景下的稳定性问题，但其仍有进一步探索空间。局限性在于：1）方法依赖在线更新的全局先验，其收敛性和偏差在非平稳环境中仍需理论保证；2）当前实验集中于数学推理任务，在开放域对话或多模态任务中的泛化能力未经验证；3）课程学习策略依赖人工设计的难度分层，自动化难度评估机制尚未开发。未来研究方向可包括：1）设计自适应先验更新机制，结合策略置信度动态调整收缩强度；2）探索分层贝叶斯框架，在任务簇层面建立结构化先验以提升跨任务迁移能力；3）将证据聚类机制与LLM内部注意力模式结合，实现基于语义结构的动态分组优化。此外，可研究EBPO与模型剪枝、低秩适配等高效微调技术的结合，进一步降低计算成本。

### Q6: 总结一下论文的主要内容

该论文针对强化学习与可验证奖励（RLVR）中主流的组相对策略优化（GRPO）方法存在的稳定性问题，提出了经验贝叶斯策略优化（EBPO）框架。核心问题是GRPO在计算受限（小组规模小）时估计器方差过高，以及在所有响应均得零奖励的饱和失败场景中梯度信号消失。

方法上，EBPO通过引入收缩估计器来正则化局部的组基线，其关键创新在于动态地将局部组统计量与通过Welford在线算法更新的全局先验信息相结合，而非孤立估计基线。这实质上是利用策略累积的全局统计量来增强局部估计的稳定性。

论文的主要结论是，理论上EBPO能保证比GRPO更低的均方误差、有界的熵衰减，并在失败场景中提供非消失的惩罚信号。实证结果表明，EBPO在AIME和OlympiadBench等多个基准测试中稳定优于GRPO及其他基线，尤其在小组规模下仍能保持高性能和训练稳定性，并能有效结合难度分层的课程学习。其核心贡献在于显著提升了RLVR训练过程的鲁棒性和效率。
