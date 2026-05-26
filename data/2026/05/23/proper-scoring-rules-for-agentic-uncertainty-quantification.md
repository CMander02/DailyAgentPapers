---
title: "Proper Scoring Rules for Agentic Uncertainty Quantification"
authors:
  - "Suresh Raghu"
  - "Satwik Pandey"
  - "Shashwat Pandey"
date: "2026-05-23"
arxiv_id: "2605.24756"
arxiv_url: "https://arxiv.org/abs/2605.24756"
pdf_url: "https://arxiv.org/pdf/2605.24756v1"
categories:
  - "cs.AI"
tags:
  - "Agent Uncertainty Quantification"
  - "LLM Agent Calibration"
  - "Trajectory Proper Score"
  - "Agent Evaluation Metrics"
  - "Epistemic Uncertainty in Agents"
relevance_score: 9.5
---

# Proper Scoring Rules for Agentic Uncertainty Quantification

## 原始摘要

Language-model agents increasingly emit uncertainty signals throughout a trajectory, but existing agentic UQ evaluations often conflate ranking usefulness with probabilistic truthfulness. AUROC, AUPRC, risk-coverage, Trajectory ECE, and scalarized trajectory scores evaluate discrimination, binwise calibration, or collapsed summaries, but do not strictly elicit the full prefix-conditioned success-probability trace $q_t = P^π(Y=1 | H_t)$. Building on prequential proper scoring, we introduce the Trajectory Proper Score (TPS), a predictor-agnostic family of strictly proper trajectory-level scoring rules for any per-step uncertainty signal calibrated into a probability of eventual success. We prove that TPS strictly elicits the success-probability process under complete observation, within the chosen score family and weight schedule. We extend the construction to administratively censored trajectories by projecting the complete-data score onto the observable stopped prefix, yielding an exact $q_Z$-weighted reduced score and a tractable approximation when $q_Z$ is unestimated. We further show that common trajectory evaluators target weaker objects than the full prefix-conditioned probability process: Trajectory ECE is resolution-blind, while scalarized Trajectory Brier elicits only the collapsed scalar, not the full trace. Experiments on StrategyQA, Tau2-Bench, HotpotQA, and WebShop show that these theoretical distinctions are operationally visible: probability recalibration can substantially change TPS while leaving rank metrics nearly unchanged, and the tractable censored approximation can change the verdict relative to complete-only evaluation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决语言模型代理在长时间交互轨迹中不确定性量化评估的问题。研究背景是，当前的代理系统在推理、工具调用等过程中会生成逐步骤的不确定性信号，但现有评估方法存在根本性缺陷。现有方法如AUROC、AUPRC、风险覆盖曲线、轨迹ECE和标量化轨迹分数等，虽然能评估排序有用性或分箱校准度，但解决的核心问题存在不足：首先，这些方法严格意义上无法激励模型输出完整的前缀条件成功概率过程 q_t = P^π(Y=1 | H_t)；其次，它们混淆了排序有效性（区分正负例）与概率真实性（概率值是否准确）两种不同的评估目标。实际上，两种代理可能在排序指标上表现相似，但概率值差异巨大，而下游干预（如延迟、反思、人机交接）依赖于概率尺度而非排序。因此，本文要解决的核心问题是：如何设计一个严格适当的、与预测器无关的评估标准，能够严格激励模型输出并正确评估整个前缀条件下的成功概率过程，而不仅仅是其排序、分箱校准或聚合标量。

### Q2: 有哪些相关研究？

与本文相关的研究可分为三类。首先是**评估方法类**：传统严格适当评分规则（如Gneiting & Raftery的Brier/对数评分）构成理论基础，但本文指出现有代理UQ指标（AUROC、AUPRC、风险覆盖曲线、轨迹ECE、标量化轨迹Brier）仅度量排序或分箱校准，而非完整前缀条件成功率轨迹。本文提出的轨迹适当评分（TPS）通过将逐点二元评分规则加权聚合，首次严格激励该完整概率过程。其次是**删失数据处理类**：生存分析中的删失评分扩展（Rindt et al.的删失对数评分、Blanche et al.的C指数失效证明）为本文提供方法论借鉴，但本文目标对象是终端结果的逐前缀条件概率（非单调），与生存分析中的累积分布函数不同。第三是**代理不确定性预测类**：SAUP、UProp、AUQ、STeCa等方法关注如何产生/传播轨迹级不确定性信号（如SAUP的态势感知权重、UProp的决策链传播），而本文聚焦于如何评估这些信号转化为前缀条件成功概率后的诚实性。核心区别在于：现有工作将轨迹聚合后再应用指标，本文证明这种做法会丢失分辨率信息，TPS能通过加权逐点评分保留完整过程。

### Q3: 论文如何解决这个问题？

该论文提出了一种名为“轨迹适当评分（TPS）”的新方法，用于严格评估语言模型智能体在轨迹中不确定性量化（UQ）的准确性。TPS是一个预测器无关的严格适当评分规则族，其核心思想是：将每个时间步的任意不确定性信号校准为最终成功概率后，通过加权求和构建轨迹级别的评分。

整体框架基于“前序适当评分”理论。主要模块包括：1）一个固定权重调度（如线性前端加权），用于强调不同位置前缀的重要性；2）任意严格适当的二元评分函数（如Log、Brier或Beta(2,4)）作为基础评分单元。通过这些组件，TPS被定义为所有时间步上二元评分与权重的加权和。

核心创新点包括：1）严格证明，在前缀条件成功概率过程完全观测下，TPS是严格适当的，确保只有当预测完全等于真实成功概率时才能达到最优期望值；2）针对管理性截断轨迹，提出了两种扩展：精确简化评分（利用截断点处的条件成功概率q_Z加权处理未观测结果）和简单近似评分（用q_Z≈0的悲观近似），后者可视为伪标签目标的评分器；3）实验显示，概率重校准能显著改变TPS值，但不影响排名指标，验证了TPS对不同不确定性量化属性的敏感度。

### Q4: 论文做了哪些实验？

论文进行了两个主要实验：1) 在Tau2-Bench上，比较了原始语言模型口头置信度与Platt校准后置信度对评价指标的影响。实验设置固定ReAct框架，使用Gemma 4 31B模型，数据集包括Tau2-Bench、StrategyQA、HotpotQA和WebShop。对比的方法包括AUROC、AUPRC、AURC等排名指标与新提出的Trajectory Proper Score (TPS)采用对数评分。关键结果显示，校准使AUROC仅变化-0.010（Δ/SE≈0.3），而TPSlog提升5.67 nats（Δ/SE≈43）。原始流比基准率低5.66 nats，Platt流仅高0.008 nats。2) 在WebShop上验证自然删失（轨迹因达到步数预算而截断）。从500条轨迹中排除192条解析错误（信息性删失），剩余308条：163条完成（δ=1），145条管理性截断（δ=0），删失率47.08%。对比完整数据评价与删失感知评价。主要结果表明，使用Platt校准口头置信度和对数评分，完整数据评价得分为-0.816 nats，删失扩展得分为-0.657 nats，配对变化为+0.159 nats（95% CI [+0.133, +0.188]）。按删失率归一化后为+0.337 nats，接近人工删失实验的+0.404 nats。不同置信度区域呈现不同模式：低置信度删失前缀获得轻微失败分支修正，而过度自信的删失前缀则受到严厉惩罚。

### Q5: 有什么可以进一步探索的点？

论文的主要局限在于：1）删失扩展要求非信息性行政删失假设，而自适应监控停止和解析错误截断会违反该假设，未来可引入逆概率删失加权（IPCW）或双稳健方法处理信息性删失；2）当前框架仅支持二元终端结果，可扩展至部分信用、分级成功、多目标或向量值奖励场景，例如通过多类别proper scoring规则或结构化预测的评分函数。此外，实验仅使用单一模型和ReAct-style框架，未来需在更多模型族和代理框架上验证TPS的稳定性。一个有趣的改进方向是结合动态权重调度，让评分自适应地关注关键决策节点，而非固定权重；另一个方向是探索TPS与在线学习中累积后悔理论的联系，以构建更严格的概率校准边界。值得注意的是，TPS在重新校准后AUROC几乎不变而TPS明显变化，表明未来研究可设计双阶段评估流程：先用TPS检测校准需求，再用校准后的概率进行下游决策。

### Q6: 总结一下论文的主要内容

该论文定义了智能体不确定性评估中缺失的目标：前缀条件成功概率过程 \(q_t = P^\pi(Y=1 | H_t)\)，并提出了轨迹正确评分(TPS)作为严格正确的评估框架。核心问题在于现有评估(AUROC、轨迹ECE、标量轨迹Brier)只能衡量判别能力或边缘校准，无法严格激励完整的过程。方法上，TPS是一族与预测器无关的、严格正确的轨迹级评分规则，通过将每个时间步的不确定性信号校准为最终成功概率并加权求和。针对管理性截断轨迹，论文推导了基于条件投影的精确截断评分及可计算近似。理论证明显示，轨迹ECE忽略了概率分辨率，而标量化的Brier仅能激励坍缩后的单一标量。实验在多个数据集上证实，概率重校准能显著改变TPS却几乎不影响排序指标，且考虑截断的评估会改变结果结论。这项工作分离了智能体产生不确定性与报告不确定性的校准问题，为评估智能体轨迹级概率校准提供了理论基础和实用工具，对部署依赖概率的干预决策有重要指导意义。
