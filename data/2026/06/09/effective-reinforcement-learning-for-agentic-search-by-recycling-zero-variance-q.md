---
title: "Effective Reinforcement Learning for Agentic Search by Recycling Zero-Variance Queries During Training"
authors:
  - "João Coelho"
  - "João Magalhães"
  - "Bruno Martins"
  - "Chenyan Xiong"
date: "2026-06-09"
arxiv_id: "2606.10709"
arxiv_url: "https://arxiv.org/abs/2606.10709"
pdf_url: "https://arxiv.org/pdf/2606.10709v1"
categories:
  - "cs.IR"
  - "cs.AI"
tags:
  - "LLM Agent训练"
  - "GRPO强化学习"
  - "查询回收机制"
  - "搜索Agent"
  - "多跳问答"
  - "零方差问题"
relevance_score: 8.5
---

# Effective Reinforcement Learning for Agentic Search by Recycling Zero-Variance Queries During Training

## 原始摘要

The use of GRPO-style algorithms has become the standard strategy for training LLM search agents under outcome-only rewards. With these algorithms, a query contributes to parameter updates only when its rollout group mixes successes and failures; all-correct (too-easy) and all-incorrect (too-hard) groups are zero-variance and waste rollout cost. Existing approaches treat zero-variance as a static property and either discard or pre-filter such groups. We hypothesize and empirically validate that queries flip between zero-variance and signal-bearing states as the policy evolves during training. Building on this intuition, we propose query recycling, which returns zero-variance groups to a mutable pool for future resampling, so that the effective training distribution co-evolves with the policy. With the proposed technique, a 1.7B parameter model trained on synthetic data can reach 66.0 average Pass@1 accross seven multi-hop QA benchmarks, matching or surpassing systems with up to 7B parameters trained on benchmark-derived supervision. Analysis of recycling patterns shows that recycled queries supply roughly three quarters of the effective batch by the end of training, with contributions split between recovery from policy improvement and policy drift.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决训练基于强化学习的LLM搜索智能体时，零方差查询（zero-variance queries）导致的训练浪费和信号丢失问题。研究背景是在智能体搜索领域，GRPO等算法已成为主流训练方法，但仅在查询的 rollout 组内同时包含成功和失败案例时，才能产生有效的策略更新信号。现有方法（如DAPO、ASearcher、GRESO）均将零方差视为静态属性，要么直接丢弃这些组，要么基于历史统计进行预过滤，认为它们始终无法提供有效信号。然而，本文通过实验观察到，零方差状态是动态变化的：随着策略在训练中演化，原本“过易”或“过难”的查询会重新进入能产生信号的状态。核心问题是：如何有效利用这些被现有方法浪费的、但在训练后期可能转变为有效信号的零方差查询，以提升训练效率和模型性能。为此，作者提出了查询回收（query recycling）机制，将零方差查询放回可变池（mutable pool）以供未来重新采样，使有效训练分布与策略共同演化，从而在不增加计算预算的情况下，显著提升模型在复杂多跳问答任务上的表现。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类**搜索智能体训练方法**，其中Search-R1确立了用GRPO在稀疏结果奖励下训练搜索智能体的范式，后续工作如SmartSearch采用双层过程奖励、Fathom-DeepResearch引入逐步奖励、BehaviorPrime使用SFT过滤教师模型轨迹。本文基于相同的GRPO框架，但聚焦于零方差查询的效率问题。第二类**零方差缓解策略**，包括DAPO的动态采样丢弃零方差样本、GRESO基于跨epoch统计量预测并跳过、RL-ZVP通过熵加权重塑优势值、ASearcher在搜索场景下沿用DAPO过滤、DAVID-GRPO对全部失败组截断重采样。这些工作都将零方差视为静态属性，而本文首次发现零方差状态会随策略演变动态切换，并据此提出查询回收机制。第三类**搜索智能体合成数据**，如WebSailor的实体图模糊化、WebShaper的集合论构造、ORBIT的答案可验证性强制。本文采用DeepResearchGym的静态ClueWeb22快照作为可复现检索环境，并扩展其合成查询生成协议，与现有方法在数据来源上形成互补。

### Q3: 论文如何解决这个问题？

该论文提出了一种名为“查询回收”（Query Recycling）的动态池管理方法，以解决GRPO风格强化学习训练中零方差查询（全正确或全错误的查询组）浪费计算资源的问题。核心框架包含两大部分：一是构建多样化的合成查询池，二是通过动态权重更新实现查询的反复利用。

在架构设计上，首先通过三种方法生成合成查询：基于网页图（Webgraph）的链接跳转问题、基于迭代搜索（Iterative Search）的密集检索链式问题、以及基于比较搜索（Comparative Search）的并行检索聚合问题，再经过LLM验证过滤，最终形成15k条用于监督微调、10k条用于强化学习的查询池。搜索代理采用简化版ReAct设计，仅保留搜索工具，允许每轮最多三次并行查询。

关键技术方面，论文形式化训练池为带权重的查询集合，初始权重均为1。每个训练步骤中，以权重比例采样kB个候选查询（k≥1为过采样因子），生成K个轨迹后识别信号组（0<成功数<K）。仅从信号组中取最多B个查询构成有效批次进行梯度更新，并将这些查询的权重置0（消耗掉），而零方差和未选中的信号查询保持权重1，从而在未来步骤中可被重新采样。过采样提高了每步发现信号查询的概率，回收机制则使得训练分布随策略演化而动态调整，避免了静态丢弃。实验证明，1.7B模型通过此方法在7个多跳QA基准上达到66.0平均Pass@1，匹配或超越7B模型。

### Q4: 论文做了哪些实验？

论文进行了多维度的实验验证。实验采用两阶段训练：先在合成搜索轨迹上进行监督微调（SFT），再应用GRPO算法。训练使用基于ClueWeb22构建的合成查询池，批次大小B=32，组大小K=4，过采样因子k∈{1,2}，总rollout预算84.5K条轨迹。对比方法包括SearchR1、DeepResearcher、R1Searcher、BehaviorPrime、ASearcher-Web-7B、ORBIT和SmartSearch。在多跳问答基准上（2WikiMultiHopQA、Bamboogle、HotpotQA、MuSiQue、Natural Questions、PopQA、TriviaQA），1.7B模型使用query recycling达到66.0平均Pass@1，优于标准GRPO（64.9）和Bounded-DAPO（64.1）；4B模型达到71.3，同样优于对比方法。在长程推理基准（GAIA、HLE、WebWalkerQA）上，回收策略也表现良好。关键发现：回收的查询在训练后期占据有效batch约四分之三，包括从“太难”和“太易”类别中恢复的查询；组大小K=4比K=8产生更多回收但最终精度相当，计算效率更高；更大的模型（4B）能将更多困难查询转化为有效查询。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其训练依赖一个固定大小的查询池（10k）。随着策略提升，池中“过于简单”的查询比例增加（4B模型接近一半），导致有效训练信号减少，这限制了训练视野。未来可探索以下方向：（1）动态查询生成：根据策略当前能力在线生成难度匹配的新查询，避免池中信号退化，这能持续提供具挑战性的训练样本。（2）结合密集奖励与优势整形：当前仅使用结果奖励，若在零方差组中引入过程奖励或优势估计（如对全对组施加探索奖励），可进一步挖掘被丢弃信号。（3）扩展到长文本生成：对于深度研究系统（如报告生成），奖励设计本身更复杂，需研究如何在此类场景下定义并利用零方差组信号。（4）改进回收机制：当前回收仅依赖状态翻转，未来可引入难度预测器主动挑选高价值组进行重采样，或设计混合策略结合丢弃与预过滤的互补优势。

### Q6: 总结一下论文的主要内容

这篇论文针对强化学习训练LLM搜索智能体时遇到的零方差查询浪费问题，提出了查询回收方法。核心问题在于，GRPO算法中全对或全错的查询组在策略更新时无梯度贡献，被现有方法视为静态特性而直接丢弃。作者通过实验验证，零方差状态是随策略演化而动态变化的，并非固定属性。方法上，论文构建一个带权重的可变查询池，将当前零方差查询保留在池中供未来重新采样，而信号查询则被消耗，使训练分布与策略共同演化。实验基于DeepResearchGym合成数据，在7个多跳问答基准上，仅1.7B参数的模型达到66.0平均Pass@1，匹配或超越7B参数在基准监督上训练的系统。分析表明，训练后期回收的查询贡献了约75%的有效批次，信号来自策略改进时的太难查询和策略漂移时的太易查询。该方法显著提升了数据利用效率。
