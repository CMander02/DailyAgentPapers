---
title: "Towards Pareto-Optimal Tool-Integrated Agents with Pareto Ranking Policy Optimization"
authors:
  - "Junyi Li"
  - "Xiaowei Qian"
  - "Yingyi Zhang"
  - "Wenlin Zhang"
  - "Guojing Li"
  - "Sheng Zhang"
  - "Xiao Han"
  - "Yichao Wang"
  - "Xiangyu Zhao"
date: "2026-06-15"
arxiv_id: "2606.16111"
arxiv_url: "https://arxiv.org/abs/2606.16111"
pdf_url: "https://arxiv.org/pdf/2606.16111v1"
categories:
  - "cs.CL"
tags:
  - "Tool-Integrated Agent"
  - "Multi-Objective Optimization"
  - "Pareto Ranking"
  - "Policy Optimization"
  - "LLM Alignment"
  - "Tool Use Efficiency"
  - "Agent Alignment"
relevance_score: 9.0
---

# Towards Pareto-Optimal Tool-Integrated Agents with Pareto Ranking Policy Optimization

## 原始摘要

Recent advances in tool-integrated language agents have significantly improved their ability to solve complex reasoning tasks. However, existing alignment methods predominantly focus on maximizing task accuracy, while overlooking auxiliary objectives such as tool-use efficiency, which are essential for practical deployment. To address this gap, we introduce ParetoPO, a two-stage multi-objective optimization framework for aligning tool-using large language models (LLMs) under competing objectives. In the first stage, ParetoPO leverages hypervolume-guided dynamic scalarization to adapt reward weights based on global Pareto frontier progress. In the second stage, it replaces scalarized learning signals with Pareto-ranking-based advantage computation, promoting nondominated trajectories through dominance-aware credit assignment. This design enables fine-grained, action-level optimization across multiple conflicting objectives. Experimental results on mathematic reasoning and multi-hop QA tasks show that ParetoPO consistently discovers policies with superior accuracy-efficiency trade-offs compared to static and heuristic baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有工具集成语言智能体在训练过程中仅关注任务准确性，而忽视了工具使用效率等辅助目标，导致在实际部署中资源消耗和可靠性不足的问题。研究背景是，在线强化学习已成为对齐工具增强的大语言模型智能体的主流方法，但现有对齐策略主要优化最终答案的准确性，忽略了推理效率（如工具调用次数）等过程级目标。现有方法的不足体现在两个方面：一是固定权重标量化或启发式奖励混合方法，由于不同目标的学习动态和尺度差异，静态权重会导致训练后期学习效率低下，且只能恢复凸面部分的帕累托最优解，错失非凸区域的最优解；二是基于梯度的多目标强化学习方法，虽然理论上可行，但计算成本高且主要应用于简单场景，缺乏对智能体动作级决策的优化。因此，本文提出的核心问题是：如何在多目标冲突下（如准确性与工具效率），通过动态调整优化策略和帕累托排序，实现对工具使用大语言模型智能体的有效对齐，以发现更优的准确性与效率权衡策略。

### Q2: 有哪些相关研究？

在多目标强化学习方面，传统方法如线性标量化（linear scalarization）和基于偏好的多策略架构（如进化算法）虽能逼近帕累托前沿，但存在固定权重无法覆盖凹面区域、多策略维护计算成本高昂等问题。本文提出的ParetoPO通过超体积引导的动态标量化与帕累托排序优势计算，在单策略训练中自适应调整权重，实现了更高效的前沿探索。

在LLM对齐与效率研究方面，现有工作主要基于PPO/GRPO等策略，通过启发式奖励塑形（如惩罚长回复）或固定权重组合优化准确率与辅助目标（如推理长度、工具调用次数）。但这些方法存在静态权重导致简单目标过早饱和、无法主动寻求帕累托最优平衡等局限。ParetoPO则创新性地将帕累托排序引入强化学习优势估计，在动作级别实现多目标权衡，无需后处理调整即可在数学推理、多跳QA等任务中获得准确性-效率的帕累托最优策略。

### Q3: 论文如何解决这个问题？

ParetoPO的核心方法是一个两阶段的多目标强化学习框架，旨在同时优化任务准确性和工具使用效率两个冲突目标。

**第一阶段：动态标量化（全局探索）**。此阶段采用基于超体积的动态标量化技术。它维护一个已发现的Pareto最优解集档案，并计算每个新轨迹的平滑超体积增益。通过将该增益作为元级奖励来放大或缩小原始标量奖励（加权和），框架能够自适应地调整有效目标权重。这种动态机制鼓励策略探索Pareto前沿中尚未充分覆盖的区域，获得一组具有不同权衡的多样化策略，从而全局逼近Pareto前沿。

**第二阶段：Pareto排序策略优化（局部精炼）**。此阶段引入基于Pareto支配关系的优势计算，替代了传统的标量奖励信号。具体而言，对于每个查询采样的一组轨迹，首先进行非支配排序，为每条轨迹分配一个Pareto等级。然后，基于这个等级计算基础优势值，并根据该轨迹在用户偏好权重下的归一化标量奖励对该优势值进行微调，保证等级高的轨迹优势值一定高于等级低的轨迹。这种设计允许在行动层面进行细粒度的多目标优化，使策略在局部进行Pareto稳定的精炼，收敛到不存在对所有目标同时改进方向的驻点。

**创新点**在于：1) 结合了全局探索（动态标量化）和局部精炼（Pareto排序）。2) 使用平滑超体积增益实现稳定的元级奖励自适应。3) 提出基于Pareto等级的优势函数，实现了不依赖固定权重的、精细的多目标信用分配。

### Q4: 论文做了哪些实验？

论文在两个复杂推理任务上进行了实验：数学推理和多跳问答。数学推理使用MATH500、AIME2024、AIME2025、OlympiadBench和AMC23五个数据集，工具为Python解释器；多跳问答使用Natural Questions (NQ)和HotpotQA数据集，工具为检索系统。评估指标为精确匹配(EM)和工具调用次数(#Tool)。对比方法包括无工具模型、工具集成模型(SFT、RAG、Search-R1)以及多目标优化基线(ToRL-GRPO、OTC-GRPO、MO-GRPO)。主要结果：在Qwen2.5-Math-1.5B上，ParetoPO在MATH500上达到80.0 EM（#Tool 0.9），优于ToRL-GRPO的77.8 EM（#Tool 2.1）和OTC-GRPO的74.0 EM（#Tool 1.3）；在NQ上（Qwen2.5-3B），ParetoPO达到48.0 EM（#Tool 0.9），优于OTC-GRPO的44.4 EM（#Tool 1.0）。消融实验表明，去除Stage 1或Stage 2均导致性能下降。训练动态分析显示，ParetoPO持续降低工具使用并缩短响应长度。权重敏感性分析表明，ParetoPO对初始权重设置鲁棒，在(0.6, 0.4)权重下表现最佳。

### Q5: 有什么可以进一步探索的点？

根据论文的局限性和未来研究方向，以下是值得进一步探索的点：

首先，当前方法主要在数学推理和多跳QA任务上验证，可拓展至更复杂的真实场景（如代码生成、对话系统），并测试其对噪声反馈或动态目标（如用户实时偏好变化）的鲁棒性。其次，ParetoPO依赖预先定义的奖励函数来量化效率和准确性，未来可探索如何从人类反馈中自动学习或修正这些目标权重，减少手动调参需求。此外，论文的Pareto排名仅在当前轨迹集合内计算，可结合离线数据或在线自适应采样策略来提升Pareto前沿的覆盖率和收敛速度。最后，考虑到工具调用场景中潜在的高延迟或API成本，可以设计轻量级代理模型来自适应地触发ParetoPO的优化步骤，从而在资源受限环境中实现更高效的部署。这些方向有望进一步提升多目标对齐的泛化性与实用性。

### Q6: 总结一下论文的主要内容

ParetoPO提出了一种两阶段多目标优化框架，用于解决工具增强语言模型在部署时面临的任务准确性与工具使用效率等目标冲突的问题。现有对齐方法仅最大化任务准确性，忽视了实际应用中的辅助目标。ParetoPO的第一阶段通过超体积引导的动态标量化，基于全局帕累托前沿进展自适应调整奖励权重；第二阶段用基于帕累托排序的优势计算替代标量化的学习信号，通过优势感知的信用分配促进非支配轨迹。该方法实现了跨多个冲突目标的细粒度动作级优化。在数学推理和多跳问答任务上的实验表明，ParetoPO能持续发现比静态和启发式基线更优的准确率-效率权衡策略。核心贡献在于将多目标优化思想引入工具智能体对齐，实现了兼顾任务表现与资源消耗的帕累托最优策略。
