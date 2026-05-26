---
title: "ProActor: Timing-Aware Reinforcement Learning for Proactive Task Scheduling Agents"
authors:
  - "Lei Ding"
  - "Bin He"
  - "Chenguang Wang"
  - "Yang Liu"
date: "2026-05-24"
arxiv_id: "2605.24900"
arxiv_url: "https://arxiv.org/abs/2605.24900"
pdf_url: "https://arxiv.org/pdf/2605.24900v1"
categories:
  - "cs.AI"
tags:
  - "proactive agent"
  - "reinforcement learning"
  - "task scheduling agent"
  - "timing-aware RL"
  - "GRPO"
  - "RL training infrastructure"
relevance_score: 9.0
---

# ProActor: Timing-Aware Reinforcement Learning for Proactive Task Scheduling Agents

## 原始摘要

Proactive task-oriented agents must autonomously anticipate user needs, identify actionable opportunities, and trigger software actions at appropriate moments - fundamentally shifting from reactive systems that await explicit instructions. However, existing approaches lack generalizable end-to-end solutions for measuring and optimizing such anticipatory behaviors.
  This paper introduces ProActor, a unified framework for conversational task scheduling that integrates: (1) a domain-agnostic automated annotation methodology that enables scalable proactiveness reinforcement learning (RL) by generating full opportunity time windows instead of rigid point labels, (2) systematic proactiveness metrics capturing both timing quality and reference action alignment, and (3) RL optimization using GRPO with various reward designs. Our insight is that RULER-based rewards with proactiveness rubrics are crucial for improving timing quality, and that proactiveness optimization enabled by stage-aware composite rewards is key to balancing timing quality and reference action alignment.
  Timing-aware RL requires extensive exploration, demanding efficient infrastructure. We develop ART-F, an adaptive framework combining request-adaptive inference clusters with DDP-based training on single-node multi-GPU systems, enabling LoRA training of 4-bit Qwen2.5-14B-ProActor-Q4 with 4-8x speedups. Experiments on two newly auto-annotated datasets demonstrate significant improvements in proactive timing while maintaining action consistency comparable to state-of-the-art (SOTA) baselines. Ablations validate the effectiveness of distinct composite reward variations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有任务调度智能体在主动行为优化中面临的核心挑战。研究背景是，AI助手正从被动等待指令的系统转变为能主动预测用户需求、发现机会并适时触发的智能体。然而，现有方法在会话任务调度场景中存在不足：第一，主动行为允许多个有效时机选择，但监督微调（SFT）因强制精确复制单一标注时间点，会惩罚其他有效时机并掩盖底层时序规律；第二，缺乏自动化的主动行为标注流程，导致数据构建困难；第三，现有方法难以量化“就绪状态”和“终止条件”等时序关键因素，且强化学习后训练需要大量的资源与GPU协调。因此，本文提出ProActor框架，核心要解决如何通过端到端的方式测量和优化智能体在对话中的主动触发时机，在保持动作一致性的同时提升时序质量，并通过高效训练框架降低资源消耗。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为三类：

1. **方法类 - 主动智能体与任务调度**：现有工作关注工具抽象、动作表示标准化和特定领域数据流水线构建，但评估时忽略时间敏感的主动行为，将主动时机视为单答案问题，惩罚与标签偏离的预测。本文提出的ProActor框架通过生成参考动作时间窗而非固定点标签，并使用时序级优化探索主动时机，解决了这一限制。

2. **方法类 - 强化学习优化与高效训练**：已有研究将RL应用于对话式任务调度（如对话策略学习、多步工具优化），但缺乏显式时序模型，时间敏感的主动性未被探索。本文将此问题建模为步级优化问题，采用复合奖励平衡早期动作与正确性。同时，针对分布式RL框架复杂、单节点LoRA量化RL易出现rollout-训练失衡的问题，本文开发了ART-F系统，通过请求自适应推理和异步负载分发实现高效共置训练。

3. **评测类**：现有工作仅提供定性主动指标，本文通过引入量化时序质量与参考动作对齐的系统化指标，实现了主动性的可测量优化。

### Q3: 论文如何解决这个问题？

ProActor通过一个统一的框架系统性地解决了对话任务调度中的主动性问题。核心方法包括三个部分：首先，提出了一种领域无关的自动标注流水线，利用配置驱动的目录生成器和具有全局对话视角的大语言模型标注器（类似事后经验回放），为每个对话轮次生成完整的主动机会时间窗口（而非固定的时间点标签），从而为大规模强化学习提供数据基础。其次，设计了一套系统性的主动度指标，包括动作一致性（AC、Max AC）和主动时序（PT、FTR、RAR），分别衡量预测动作与参考动作的对齐质量以及触发时机的合适性。最后，采用基于GRPO的强化学习优化，关键在于奖励函数设计：基于RULER的奖励配合主动度评估能有效提升时序质量；而阶段感知的复合奖励（如自适应度量奖励和自适应RULER奖励）通过在不同训练阶段调节动作一致性和时序质量的权重（例如前期鼓励探索、中期平衡、后期保守），实现了两者的最佳平衡。整体架构上，ART-F框架通过自适应推理集群（动态管理vLLM服务器）和异步分布式训练（主从架构、负载分发）实现了高效的协同训练，支持在单节点多GPU系统上对4位Qwen2.5-14B模型进行LoRA训练，获得4-8倍加速。创新点在于：采用时间窗口而非点标签的自动标注、阶段感知的复合奖励设计、以及高效的协同训练基础设施。

### Q4: 论文做了哪些实验？

论文在两个自标注数据集上进行了实验：ABCD+（客户支持场景，含历史动作日志，7042个对话）和 Home Loan（抵押贷款咨询，不含软件动作触发，968个对话）。对比方法包括：Non-Reasoning（直接预测动作机会、状态和时间）、Reasoning（通过<think>显式推理）、Reasoning + ASG（维护动作状态图）、以及 SFT（监督微调），基线模型涉及 GPT-5.1、Gemini-2.5-flash、Claude-sonnet-4 和 Qwen2.5-14B-Instruct。

主要结果通过提出的 Proactiveness Ranking Index (PRI) 衡量，该指数综合了动作一致性（AC、Max AC、Difference）和时序质量（Proactive Timing、Fault Trigger Rate、Ready Action Rate）。在 ABCD+上，ProActor-Q4 + Custom RULER 取得最高 PRI 0.7293，其 Proactive Timing (PT) 达 0.2347，Ready Action Rate (RAR) 达 0.546，均优于最强基线（GPT-5.1 Non-Reasoning 的 PT 0.2023、RAR 0.419），且一致性差异仅 0.136。在 Home Loan 上，Gemini-2.5-flash Reasoning 获得最高 PRI 0.7303，但 ProActor-Q4 + Adaptive RULER 实现了更平衡的改进，PRI 为 0.6232，AC 达 0.395，PT 为 0.0501。

消融实验验证了不同奖励设计的影响：Custom RULER 在时序上最优，Adaptive RULER（基于 Max RAC 且 \(\lambda_{\max}=0.3\)）在平衡性和一致性上表现突出，而仅使用 RAC 或 Max RAC 的奖励则效果较差。结果表明，RULER 基础奖励的主动性子评分对提高时序质量至关重要，而阶段感知的复合奖励能有效平衡时序与动作一致性。

### Q5: 有什么可以进一步探索的点？

论文《ProActor》在构建主动任务调度Agent方面迈出了重要一步，但仍存在若干可深化的方向。首先，**动作观察范围受限**：当前评测仅覆盖系统中实际发生的动作，而理想主动行为可能包含大量未被触发的潜在动作（如系统未记录但用户希望的提醒或调整）。未来可以探索**反事实数据生成**或**交互式模拟环境**，通过用户模型或仿真器主动探索“本应发生但未发生”的时敏动作，来扩充训练信号的覆盖度。其次，**时间粒度的细化**：目前的“完整机会时间窗”仍是一种区间层面的标注，而实际场景中的最佳触发时点往往具有细粒度、动态变化的特征。可以考虑引入**时序点过程**（如Hawkes过程）或**连续时间RL**，让模型直接学习触发时刻的概率密度函数，而非仅学习窗口边界。再次，**奖励函数的泛化性**：文章强调了RULER评分与阶段式组合奖励，但奖励函数的设计可能依赖于特定领域细粒度规则。未来的工作可以尝试**元学习**或**逆强化学习**，让Agent从少量用户反馈或演示中自适应归纳出个性化、跨任务的时机偏好。最后，**多模态与记忆增强**：任务调度常涉及时序性、情境性信息（日历、通知、环境状态），可借助图神经网络或时间感知的记忆网络，提升对非规范化异步事件的表征能力。总体而言，将主动性的时机感知从“窗口匹配”推向“连续、概率化、可泛化的决策”是值得深化的方向。

### Q6: 总结一下论文的主要内容

ProActor提出了一个面向主动任务调度智能体的时序感知强化学习框架。现有系统多为被动响应式，缺乏衡量和优化先发行为的统一方案。该框架包含三项核心贡献：一是领域无关的自动标注方法，生成全机会时间窗口而非固定标签，实现可扩展的主动性强化学习；二是系统化的主动性度量指标，同时捕捉时序质量与参考动作对齐度；三是采用GRPO结合多种奖励设计进行优化。关键发现是，使用RULER奖励与主动性评估准则能显著提升时序质量，而分阶段复合奖励则平衡了时序与动作一致性。实验在两个新自动标注数据集上显示，该方法在保持动作一致性接近最优基线的同时，大幅提升了主动时序性能。此外，ART-F高效基础设施支持4-bit LoRA训练，实现4-8倍加速。该工作为时序感知的主动任务调度提供了可推广的基准方案。
