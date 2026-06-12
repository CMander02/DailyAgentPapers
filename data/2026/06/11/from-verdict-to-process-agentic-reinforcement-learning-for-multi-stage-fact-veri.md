---
title: "From Verdict to Process: Agentic Reinforcement Learning for Multi-Stage Fact Verification"
authors:
  - "Rongxin Yang"
  - "Shenghong He"
  - "Siyuan Zhu"
  - "Chao Yu"
date: "2026-06-11"
arxiv_id: "2606.13262"
arxiv_url: "https://arxiv.org/abs/2606.13262"
pdf_url: "https://arxiv.org/pdf/2606.13262v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Multi-Agent"
  - "Tool Use"
  - "Reinforcement Learning"
  - "Retrieval-Augmented Generation"
  - "Fact Verification"
  - "End-to-End Optimization"
  - "Reward Design"
relevance_score: 9.5
---

# From Verdict to Process: Agentic Reinforcement Learning for Multi-Stage Fact Verification

## 原始摘要

Recent approaches combining Large Language Models (LLMs) with retrieval-augmented reasoning have shown promise for automated fact verification. To process complex claims, these verification pipelines typically execute multi-stage workflows that coordinate tightly coupled modules, including claim decomposition, evidence gathering, and verdict prediction. However, existing methods optimize individual stages in isolation or rely on fixed heuristics, which limits adaptive coordination among stages and can lead to suboptimal outcomes. In this work, we propose ProFact, an agentic reinforcement learning framework for end-to-end optimization of multi-stage fact verification trajectories. ProFact trains a unified policy to coordinate claim decomposition, evidence seeking, answer generation, and verdict prediction. To address the sparse and delayed supervision provided by final veracity labels, ProFact introduces process-aware rewards that provide stage-level learning signals throughout the verification process. Empirical evaluation shows that ProFact consistently outperforms strong baselines in both verification performance and inference efficiency. These results highlight the effectiveness of process-aware trajectory optimization for multi-stage fact verification.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有自动化事实验证方法在多阶段流程中缺乏自适应协调和端到端优化的问题。研究背景是，开放域事实验证通常需要分解复杂声明、检索分散证据并推理得出最终判断，是一个多阶段决策过程。现有方法（如InFact、HerO、DebateCV）虽然利用大语言模型构建了包含声明分解、证据检索、答案生成和裁决预测等阶段的流水线，但存在明显不足：它们要么独立优化各个阶段，要么依赖固定的启发式规则来协调。这种分离式优化导致中间决策（如如何分解声明）与最终验证目标（正确裁决）脱节——例如，一个看似合理的分解策略可能无法产生产出最有利于最终判断的证据，从而限制了阶段间的自适应协调，导致次优的验证结果。针对这一核心问题，论文提出ProFact框架，将事实验证形式化为一个长时序决策过程，通过统一的策略进行端到端优化，联合协调声明分解、证据检索、答案生成和裁决预测。同时，为应对最终标签监督稀疏延迟的挑战（无法揭示哪些中间步骤导致了错误），ProFact引入了过程感知奖励函数，为每个验证阶段提供密集的中间学习信号，从而实现对整个验证轨迹的端到端优化。

### Q2: 有哪些相关研究？

相关研究主要分为事实核查方法和强化学习智能体两大类。

在事实核查方法方面，相关工作包括：InFact采用静态六阶段流水线，通过工程化提示词和证据检索进行核查，但依赖专有模型；HerO通过生成假设性事实核查文档增强证据检索，但使用独立的LLM组件分别完成问题生成和真实性预测；DebateCV通过多智能体辩论提升证据审视能力。这些方法的共同局限在于各模块独立训练或使用固定提示，缺乏跨阶段的适应性协调。本文ProFact的创新在于将事实核查建模为长期智能体决策问题，通过端到端训练的统一策略联合优化多阶段核查行为。

在强化学习智能体方面，相关方法包括：RLHF、GRPO等偏好对齐方法，以及面向智能体LLM的RAGEN（StarPO）、GiGPO（层级组优势估计）等长程智能体训练方法，还有Search-R1、Search-P1等检索增强推理方法。这些工作证明了RL在推理和搜索任务中的有效性，但本文ProFact首次将其应用于多阶段事实核查的端到端优化，并引入过程感知奖励以解决最终标签提供的稀疏延迟监督问题。

### Q3: 论文如何解决这个问题？

ProFact将事实验证建模为有限时域的马尔可夫决策过程。核心框架是统一策略πθ协调三个阶段：Question阶段，智能体生成验证问题并接受基于METEOR的奖励r^q（与标准问题进行最大权重二分匹配）；Search阶段，智能体通过工具调用从证据库K中检索语义证据，生成答案后同样获得匹配奖励r^s；Verdict阶段，智能体预测真实性标签并获得指示函数奖励r^v。关键技术在于，该框架使用GRPO进行端到端策略优化。对于每条声明，采样一组G条轨迹，每个轨迹由过程感知奖励函数评分，在组内计算归一化相对优势。GRPO目标函数包含裁剪的比率项和KL散度正则化项，以限制策略偏离参考模型。创新点主要体现在：第一，将分阶段验证工作流（分解、检索、判决）作为统一MDP进行端到端优化，而非分别独立优化各阶段；第二，设计过程感知奖励，通过在每个阶段提供密集的中间监督信号（问题分解质量、证据回答质量、最终判决正确性）来解决最终标签的稀疏和延迟问题，从而鼓励策略改进验证全过程的行为；第三，使用语义搜索（Qwen3嵌入+kNN索引）和结构化工具调用实现证据检索。整个框架使得验证轨迹的探索和利用更加高效。

### Q4: 论文做了哪些实验？

论文在AVeriTeC基准数据集上进行实验，该数据集包含真实世界主张、正确性标签及标注的问答证据，并提供预收集的网络文档作为检索来源。评估指标包括：Q-only METEOR（衡量问题生成质量）、Q&A METEOR（衡量问答证据对齐度）、Accuracy（最终真实性分类准确率）以及AVeriTeC Score（联合评估证据充分性和标签正确性，证据分数阈值λ=0.25）。对比方法包括：Consistency（基于固定证据的提示基线）、InFact（多步证据获取与推理流程）、HerO（增强检索与微调LLM预测）。所有方法在Qwen2.5-3B/7B/8B和Qwen3-4B/8B四种开源骨干模型上评估。

主要结果表明，ProFact在所有骨干模型上均最优：AVeriTeC Score最高达48.00（Qwen2.5-7B），Accuracy最高达70.28（Qwen3-8B），Q-only METEOR最高达46.08（Qwen3-4B）。消融实验移除过程奖励后，AVeriTeC Score下降至34.40（Qwen2.5-3B），验证了过程奖励对稀疏延迟监督的关键作用。效率对比显示，ProFact显著降低推理时间（如Qwen2.5-3B从16.32秒降至7.29秒）和总Token消耗（输入Token从55.15M降至7.26M）。强化学习算法对比中，GRPO优于PPO、DAPO和GiGPO，因组相对目标更适应多阶段轨迹优化。

### Q5: 有什么可以进一步探索的点？

尽管ProFact在端到端优化上取得了进展，但仍存在可进一步探索的方面。首先，当前过程奖励依赖于预定义规则或小样本标注，未来可探索利用LLM自身生成更细粒度、自适应过程奖励的机制，以应对多样化错误类型。其次，实验仅在单一基准AVeriTeC上进行，需在更多领域（如政治、医疗）和长尾claim上验证泛化性。此外，当前策略网络对长轨迹的信用分配仍存在挑战，可引入分层RL或注意力机制以更好处理长程依赖。另一个方向是结合专家演示或逆强化学习，提升初期探索效率。最后，如何确保多阶段间上下文一致性与证据无冗余，以及将可解释性（如归因图）融入训练目标，也是提升可信度和实用性的关键。

### Q6: 总结一下论文的主要内容

本文提出了ProFact框架，将多阶段事实验证建模为有限时域决策过程，采用智能体强化学习方法进行端到端优化。现有方法通常孤立优化各阶段（如证据收集、判决预测）或依赖固定启发式规则，导致阶段间协调不足。ProFact训练统一策略来协同规划线索分解、证据检索、答案生成和判决预测，并针对最终标签监督稀疏迟滞的问题引入过程感知奖励，在验证全程提供阶段级学习信号。在AVeriTeC数据集上的实验表明，ProFact在验证性能和推理效率上均显著优于强基线方法。核心贡献在于证明了过程级轨迹优化对多阶段事实验证的有效性，为复杂任务中智能体协调和延迟奖励处理提供了新思路。
