---
title: "Learning What to Remember: Observability-Safe Memory Retention via Constrained Optimization for Long-Horizon Language Agents"
authors:
  - "Qingcan Kang"
  - "Liu Mingyang"
  - "Shixiong Kai"
  - "Kaichao Liang"
  - "Tao Zhong"
  - "Mingxuan Yuan"
date: "2026-06-09"
arxiv_id: "2606.10616"
arxiv_url: "https://arxiv.org/abs/2606.10616"
pdf_url: "https://arxiv.org/pdf/2606.10616v1"
categories:
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Constrained Optimization"
  - "Memory Retention"
  - "Long-Horizon Agent"
  - "Observability-Safe Learning"
relevance_score: 8.0
---

# Learning What to Remember: Observability-Safe Memory Retention via Constrained Optimization for Long-Horizon Language Agents

## 原始摘要

Long-horizon language agents accumulate observations, reasoning traces, and retrieved facts that exceed their finite context windows, making memory retention a fundamental resource-allocation problem. Existing memory systems improve management through heuristic scoring, retrieval optimization, or learned compression, but largely treat retention as a local decision problem and do not explicitly model its long-term consequences under realistic observability constraints. To fill this gap, we formulate memory retention as a constrained stochastic optimization problem with explicit budget feasibility, evidence utility, and delayed costs including miss penalties, reacquisition delays, and stale-information risk. We then propose OSL-MR (Observability-Safe Learning for Memory Retention), a novel framework that enforces a strict separation between online-observable features and offline-available supervision (OAS). OSL-MR combines an evidence learner trained from realized evidence supervision with a Mixed-Score heuristic that serves both as a deployable online-safe baseline and as a structured inductive prior for learning. The resulting policy learns query-conditioned evidence value directly from interaction data while remaining deployable under the same observability constraints. Experiments on LOCOMO and LongMemEval show that OSL-MR consistently outperforms recency-based methods, Generative Agents-style scoring, and other heuristic baselines, particularly under tight memory budgets. The Mixed-Score prior further improves precision while preserving recall, and sensitivity analysis demonstrates robustness across a wide range of cost configurations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决长时域语言智能体在有限上下文窗口下的记忆保留问题。研究背景是，当前语言智能体在执行长期任务时会积累大量观察、推理痕迹和检索事实，但受限于有限的上下文窗口，如何高效管理记忆成为一个基础资源分配问题。现有记忆系统存在显著不足：大多数方法依赖启发式评分、检索优化或学习压缩，将记忆保留视为局部决策问题，缺乏对长期后果的建模。它们没有显式考虑预算可行性、证据效用以及延迟代价（如遗漏惩罚、重新获取延迟和过时信息风险），更未在现实部分可观测性约束下进行建模。针对这些不足，本文的核心创新在于：首次将记忆保留形式化为一个受约束的随机优化问题，显式建模预算约束、证据效用、遗漏惩罚、重新获取代价和过时风险等延迟代价。同时，为解决优化中的可观测性挑战，引入在线可观测特征与离线可用监督的严格分离，并提出OSL-MR框架，确保部署策略仅依赖在线可观测输入，从而在严格的现实约束下学习查询条件的证据价值，实现长时域智能体的高效、鲁棒记忆管理。

### Q2: 有哪些相关研究？

相关研究工作主要可分为三类：**记忆管理系统**、**优化式记忆保留**和**学习式记忆策略**。在记忆管理系统方面，MemGPT引入类操作系统分层分页机制，MemoryBank采用艾宾浩斯遗忘曲线，Generative Agents按时效性、相关性和重要性排名，但这些静态重要性分数缺乏查询特异性。本文指出这些方法将保留视为局部决策，未建模长期后果。在优化式记忆保留方面，Fofadiya和Tiwari将记忆保留建模为单步预算优化，每次独立最大化即时相关性，AdaGReS和CORAG聚焦于单轮上下文选择而非长程保留。本文提出OSL-MR框架，首次将保留建模为多步顺序决策问题，显式优化整个时间跨度的累积奖励。在学习式记忆策略方面，Mem-α通过强化学习学习记忆构建，CSIM压缩上下文，MemRL将检索建模为价值决策。但这些方法侧重于检索或压缩而非硬预算约束下的保留，且依赖部署时不可用的监督信号。本文与它们的核心区别在于：严格分离在线可观测特征与离线可用监督（OAS），仅使用在线安全特征部署冻结策略，并通过混合分数启发式将结构化归纳先验融入学习过程。

### Q3: 论文如何解决这个问题？

OSL-MR将记忆保留形式化为一个约束随机优化问题，核心在于严格分离在线可观测特征和离线监督信号。整体框架包含三个关键组件：结构化优化目标、混合分数启发式和证据学习器。

首先，框架将记忆保留建模为长时序约束优化问题，定义明确的奖励函数r_t，综合权衡命中收益、缺失惩罚、重新获取代价和过时风险，并在预算约束下最大化累积期望奖励。这避免了传统方法的短视决策。

其次，混合分数（Mixed-Score）作为冷启动部署方案，整合时间、相关性、上下文和风险信号，结合存储效率形成统一的效用函数，在严格在线可观测约束下运行。它同时作为学习阶段的归纳偏置，为后续训练提供结构化先验。

证据学习器是核心创新。当积累足够交互日志后，利用离线可获取的黄金证据标签训练二元分类器，预测记忆是否为查询所需的证据。学习器以混合分数为额外特征，采用加权二元交叉熵损失，通过约束解码在预算内选择记忆集。与行为克隆基线对比证明，直接基于真实证据监督学习优于模仿改进启发式。

关键技术包括：连续新鲜度代理利用轻量级LLM分类器估计语义衰减动态；延迟反馈处理通过离线收集完整交互日志实现；观测性安全设计确保部署时仅依赖在线特征，不泄露未来信息。

### Q4: 论文做了哪些实验？

两个基准测试（LOCOMO和LongMemEval）上，实验严格遵循在线可观测性分离原则：可部署策略仅使用查询上下文、记忆元数据、近期性、语义/实体重叠等在线特征；离线监督（如黄金证据、答案文本）仅用于训练或作为Oracle基线。对比方法包括：最先进时间戳的Recency、用启发式规则或LLM打分的Generative Agents (GA-heuristic/GA-LLM)、作为归纳先验的Mixed-Score、模仿教师策略的行为克隆基线BC-learner，以及移除先验的消融变体OSL-MR (w/o prior)。在三种预算水平（LOCOMO：32/64/128 tokens；LongMemEval：256/512/1024 tokens）下，OSL-MR在所有预算上均取得最高证据F1和奖励值，例如在LOCOMO 64 tokens预算下，其F1比Mixed-Score高约12%，比Recency高30%以上。消融实验显示，Mixed-Score先验主要提升精确率（在LongMemEval 512 tokens下精确率提升4.5%），而对召回率影响较小。敏感度分析表明，在0.25倍至4倍系数范围内的奖励变化下，OSL-MR性能保持稳定，体现对成本系数设定的鲁棒性。

### Q5: 有什么可以进一步探索的点？

该工作将记忆保留建模为约束随机优化，但仍存在若干拓展空间。首先，其“证据效用”计算依赖离线获取的完整轨迹标签，实际部署中难以保证此类监督信号的及时性与准确性，未来可探索在线环境下利用弱监督或自监督信号进行渐进式学习。其次，Mixed-Score启发式先验虽提升了精度，但本质上仍是手工设计的权重组合，缺乏对动态环境中交互模式变化的自适应能力。可考虑引入元学习框架，使先验参数能随任务分布迁移而调整。此外，当前实验仅考察固定预算下的性能，未涉及预算随时间动态变化（如任务复杂度驱动）的场景。结合在线强化学习中的预算调度机制或许能进一步提升鲁棒性。最后，长程对话中的记忆污染（如误解级联）尚未被明确建模，引入因果推断来区分事实性记忆与推理噪声将是重要的改进方向。

### Q6: 总结一下论文的主要内容

本论文针对长时域语言智能体在有限上下文窗口下的记忆保留问题，将其形式化为一个带预算约束的随机优化问题，明确建模了证据效用、错失惩罚、重新获取延迟和过时信息风险等长期后果。现有方法多采用启发式评分或局部优化，忽略了决策的未来影响。作者提出OSL-MR框架，核心创新在于严格区分在线可观测特征与离线可用监督(OAS)，确保策略在真实部署中不依赖未来信息。该框架包含一个从交互日志中学习的证据学习器，以及一个混合评分启发式方法，后者既作为可部署的在线安全基线，又为学习提供结构化归纳先验。实验表明，OSL-MR在两个基准上持续优于基于新近度、生成式智能体评分等基线，尤其在紧预算下表现显著，且混合先验在保持召回率的同时提升了精确度。该工作首次从约束优化视角定义了最优记忆保留问题，为构建具备长期记忆管理能力的语言智能体提供了理论基础。
