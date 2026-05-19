---
title: "$\boldsymbol{f}$-OPD: Stabilizing Long-Horizon On-Policy Distillation with Freshness-Aware Control"
authors:
  - "Xianwei Chen"
  - "Shimin Zhang"
  - "Jibin Wu"
date: "2026-05-18"
arxiv_id: "2605.17862"
arxiv_url: "https://arxiv.org/abs/2605.17862"
pdf_url: "https://arxiv.org/pdf/2605.17862v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Agent训练与微调"
  - "工具使用Agent"
  - "代码Agent"
  - "策略蒸馏"
  - "异步训练"
  - "长时域任务"
relevance_score: 8.5
---

# $\boldsymbol{f}$-OPD: Stabilizing Long-Horizon On-Policy Distillation with Freshness-Aware Control

## 原始摘要

Scaling on-policy distillation (OPD) for large language models (LLMs) confronts a fundamental tension: asynchronous execution is necessary for system efficiency, but structurally deviates from the ideal on-policy objective. To address this challenge, we theoretically decompose the objective discrepancy into rollout drift and supervision drift, capturing staleness in student rollout and teacher context, respectively. Building on this, we introduce a sample-level freshness score that quantifies the reliability of a buffered sample with respect to the on-policy objective. Guided by this signal, we further propose f-OPD, a novel framework that adaptively regulates stale-sample influence and constrains policy drift accumulated under asynchronous training. Across reasoning, tool-use, and coding-agent tasks of increasing interaction horizon, f-OPD consistently achieves task performance comparable to synchronous optimization while largely retaining the throughput advantages of asynchronous execution. Our results establish the first recipe for achieving a performance-efficiency trade-off in OPD, paving the way for long-horizon agentic post-training at scale.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大规模语言模型（LLM）在线策略蒸馏（OPD）中的性能-效率权衡问题。研究背景在于，OPD通过将在线策略学习与密集监督相结合，已成为提升LLM性能的强大技术。其理想流程要求学生策略的轨迹生成、教师模型的监督以及学生策略优化三者同步执行，以确保训练步骤完全符合在线策略。

然而，现有方法存在明显不足：严格的同步执行会导致严重的系统利用率低下，尤其是在处理长序列任务时，轨迹生成和监督的成本急剧增加。为此，现代OPD系统普遍采用异步执行模式以提高吞吐量，但这引入了“陈旧性”问题：缓冲区中的轨迹及其对应的监督可能已不再匹配当前的策略，导致优化目标失真、训练不稳定，最终损害任务性能。简单粗暴的刷新缓冲区策略又难以兼顾有效学习信号的保留与陈旧优化的抑制。

本文要解决的核心问题正是如何克服这种因异步执行产生的陈旧性带来的目标函数偏差，在保持异步执行高吞吐量优势的同时，尽可能恢复接近同步优化的任务性能。为此，文章理论分析了偏差的两个来源（策略漂移和监督漂移），并提出了基于新鲜度感知的量化与控制框架f-OPD，实现了在性能与效率之间的有效平衡。

### Q2: 有哪些相关研究？

相关工作可从三个类别组织：

1. **LLM后训练与同策略蒸馏（OPD）**：直接相关的工作包括SFT（基于固定数据集的前向KL优化）和RL（基于自生成轨迹的奖励驱动优化）。本文的OPD介于两者之间，结合了RL的探索能力与蒸馏的稳定学习信号。最近的同策略自蒸馏和在线教师监督变体进一步展示了该范式的潜力。本文的核心区别在于系统性地解决了异步执行导致的统计保真度问题，而非仅关注算法层面的改进。

2. **异步系统与新鲜度失配**：异步强化学习系统（如IMPALA、APPO）通过解耦数据收集与优化提升吞吐量，但导致策略陈旧性。相关研究如GAE、V-trace等提出了离策略修正方法。本文的新意在于将新鲜度问题扩展到教师监督的OPD场景，识别出**学生rollout漂移**和**教师上下文漂移**两种失配源，并引入样本级新鲜度评分进行自适应控制。

3. **长程任务与稳定性方法**：数据集聚合（DAgger）和信任域优化（TRPO/PPO）旨在控制策略漂移。近期长程RL工作（如Explicit Trust-Region Masking、解耦PPO）通过分离近端策略与行为策略来更好利用陈旧数据。本文在这些基础上，首次将新鲜度意识控制应用于OPD框架，在推理、工具使用和编码智能体任务中实现了性能-效率权衡。

### Q3: 论文如何解决这个问题？

论文通过提出f-OPD框架来解决长时序同策略蒸馏中的异步目标差异问题。核心方法是对异步训练中的目标偏差进行理论分解，将其拆分为两个主要来源：rollout drift（学生策略陈旧导致的分布偏移）和supervision drift（教师上下文过时导致的监督偏移）。基于此，论文设计了三个关键技术组件：

1. **新鲜度评分机制**：对每个样本维护三个诊断指标——rollout drift（通过当前策略与旧策略在相同前缀上的KL散度衡量）、supervision drift（通过当前教师上下文与旧上下文的KL散度衡量）以及更新滞后$\tau_i$。将这些指标融合为样本级新鲜度分数$f_i = \frac{1}{\tau_i+1}\exp(-\alpha\sqrt{D_i^{roll}}-\beta\sqrt{D_i^{sup}})$，用于量化样本对同策略目标的可靠性。

2. **三管齐下的新鲜度控制**：a) 新鲜度加权——使用ReLU函数$\sigma(f_i-\xi)$过滤低新鲜度样本，减少陈旧样本对梯度的负面贡献；b) rollout锚定正则化——引入$D_i^{roll}$作为正则项，约束当前策略与产生样本的策略保持局部一致性，防止策略漂移累积；c) 自适应缓冲刷新——监控缓冲区的平均新鲜度$\bar{f}^t$和对齐覆盖率$\bar{\mathcal{M}}^{t,roll}/\bar{\mathcal{M}}^{t,sup}$，在指标低于阈值时主动刷新缓冲区，确保监督质量和诊断有效性。

整体框架在保持异步训练吞吐优势的同时，通过样本级新鲜度感知机制实现了与同步优化相媲美的任务性能，在推理、工具使用和编码代理等长时序任务中验证了效果。创新点在于首次从理论上分解异步蒸馏偏差，并建立了基于新鲜度控制的性能-效率权衡方案。

### Q4: 论文做了哪些实验？

论文围绕长程在线策略蒸馏（OPD）中的性能与效率权衡设计了三类实验。首先，通过手动控制策略更新延迟（lag=0,2,4,8）进行故障分析，发现所有任务性能随延迟单调下降（编码代理任务在lag=8时下降约40%），且监督漂移比 rollout 漂移更严重。主要实验在三个任务族上进行：短程推理（MATH500，Avg@1准确率）、中程工具使用（1,000道奥林匹克题，Avg@4准确率及无效工具率）和长程编码代理（SWE-bench Verified，解决率）。学生模型采用 Qwen 系列（8B），教师模型为更大的 Qwen，在同步和异步流水线下训练。与同步 OPD（解决率41.8，吞吐量1.00×）、异步 OPD（解决率26.8，吞吐量1.61×）及简化变体（硬刷新、仅延迟加权）相比，f-OPD 实现了1.46×吞吐量提升，同时达到39.4解决率（同步的94%），后补丁回归仅2.6，无崩溃。消融实验证实三个机制（新鲜度加权、rollout锚定正则化、自适应刷新）协同互补：新鲜度加权单独恢复大部分性能（编码解决率+9.7），正则化进一步缩小差距（+1.6），自适应刷新完全消除崩溃。

### Q5: 有什么可以进一步探索的点？

该论文虽在异步蒸馏任务中展现了性能与效率的平衡，但仍存在若干可深入探索的局限性。首先，文中提出的新鲜度评分虽有理论依据，但其计算依赖静态或者预设的阈值，在真实训练中可能无法实时适应模型策略变化的动态特征，未来可以考虑引入自适应或元学习机制动态调整新鲜度权重。其次，当前框架仅考虑了教师与学生之间的分布漂移，但未显式建模反馈信号中的噪声或偏差，尤其当短评奖励信号稀缺时，新鲜度控制可能不够鲁棒。建议引入基于不确定性回馈的置信度加权来增强对低质量样本的抑制。此外，目前仅在有限任务规模上验证，未来应扩展到多模态Agent环境与指令层次更复杂的一般型任务，提升蒸馏范式在异构执行条件下的泛化性与可解释性。

### Q6: 总结一下论文的主要内容

这篇论文聚焦于大型语言模型（LLM）在线策略蒸馏（OPD）中因异步执行而引起的性能-效率权衡问题。作者形式化地将异步OPD带来的目标函数偏差分解为两类“陈旧性”：来自学生模型rollout的“策略漂移”，以及来自教师模型上下文的“监督漂移”。基于此，他们引入了细粒度的样本级“新鲜度评分”来量化每个样本对在线策略目标的保真度，并提出了新颖的 **f-OPD** 框架。该框架利用新鲜度信号自适应地调节陈旧样本在优化中的影响，并主动约束累积的策略漂移。在包含推理、工具使用和代码智能体等多种长程交互任务上的实验表明，f-OPD能持续实现与同步优化相当的任务性能，同时几乎保留了异步执行的高吞吐优势。该工作的核心贡献是首次建立了在OPD中实现性能与效率平衡的可行方案，为大规模长程智能体后训练夯实了基础。
