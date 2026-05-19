---
title: "DiagEval: Trajectory-Conditioned Diagnosis for Reliable Software Evaluation with GUI Agents"
authors:
  - "Sirui Hong"
  - "Zhijie Liu"
  - "Tengfei Li"
  - "Wei Tao"
  - "Yifan Wu"
  - "Chenglin Wu"
date: "2026-05-17"
arxiv_id: "2605.17439"
arxiv_url: "https://arxiv.org/abs/2605.17439"
pdf_url: "https://arxiv.org/pdf/2605.17439v1"
github_url: "https://github.com/scutGit/DiagEval"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "GUI Agent"
  - "Agent Evaluation"
  - "Diagnostic Protocol"
  - "Software Testing"
  - "Failure Attribution"
relevance_score: 8.5
---

# DiagEval: Trajectory-Conditioned Diagnosis for Reliable Software Evaluation with GUI Agents

## 原始摘要

Evaluating LLM-generated interactive software requires execution in addition to static analysis. The key difficulty is that correctness is a graph-level reachable property over latent UI state-transition graphs, whereas a GUI evaluator observes only a single execution trajectory. A failed rollout therefore rules out only one realized path, leaving failure attribution ambiguous between evaluator-side execution error and genuine software defect. We present DiagEval, a trajectory-conditioned diagnostic evaluation protocol for post-failure GUI-agent evaluation of interactive software. Rather than blindly retrying from scratch, DiagEval reuses the failed trajectory to choose targeted diagnostic probes and aggregates their outcomes into an internal attribution signal. The latent-graph view motivates the diagnostic problem; DiagEval does not reconstruct the graph or estimate calibrated posterior probabilities. We evaluate DiagEval on WebDevJudge-Unit and RealDevBench across multiple GUI-agent evaluators and LLM backbones. On false-negative cases, DiagEval recovers 45.6-62.1% of failures that were initially misattributed to software defects, outperforming retry-based baselines with 34.4-160.6% relative gains. On the full evaluation sets, this recovery improves accuracy from 69.9% to 78.3% on WebDevJudge-Unit and from 65.0% to 81.6% on RealDevBench. These results suggest that reliable GUI-agent evaluation requires not only stronger execution, but also active failure diagnosis to disambiguate evaluator-side errors from genuine software defects. Our code is available at https://github.com/scutGit/DiagEval.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于GUI智能体评估交互式软件时存在的失败归因模糊性问题。研究背景是，随着大语言模型生成的软件从孤立代码片段发展为具有复杂界面的全栈应用，评估方式必须从静态分析转向交互式执行验证。现有方法（如ReAct-style智能体、简单重试、Best-of-N采样和自我修正等）虽然能提升执行鲁棒性或减少瞬态错误，但核心不足在于：它们没有针对失败后的归因过程进行专门设计。当一次GUI智能体执行轨迹失败时，失败原因在结构上是不确定的——可能是智能体自身的执行错误（AgentFail），也可能反映了软件本身的真实缺陷（EnvFail）。由于软件正确性是图级别的可达属性，而评估者仅观察到一条局部的执行路径，单一轨迹的证据不足以区分这两种假设。本文提出DiagEval，一个轨迹条件化的诊断评估协议。核心思路是在一次失败后，不从头盲目重试，而是复用失败轨迹来选择有针对性的诊断探针，通过主动收集额外证据来归因不确定性，从而更可靠地区分评估者侧错误与软件侧缺陷。

### Q2: 有哪些相关研究？

与本文相关的研究主要分为三类：**评估方法类**、**可靠性增强类**和**GUI智能体类**。

1. **评估方法类**：WebDevJudge和RealDevBench采用基于执行的动态环境评估，但将失败轨迹直接判定为软件缺陷，缺乏失败归因能力。本文的创新在于提出后验归因协议，主动区分评估器执行错误与真实缺陷。LLM-as-a-Judge和Agent-as-a-Judge评估静态输出或轨迹，但均将评估视为对固定产物的评分，不适用于图级正确性部分可见的交互式软件评估。

2. **可靠性增强类**：现有方法如去偏、减少幻觉、微调裁判、提示模板和多裁判集成均假设评估证据固定。本文突破这一假设，将失败轨迹视为主动获取诊断证据的机会，而非终止判定的终点。

3. **GUI智能体类**：基于多模态LLM的智能体（如Claude 3.5 Sonnet）已成为评估工具，但WebGen-Bench和UXAgent等的判断仍依赖单条轨迹，无法区分缺陷与评估器错误。本文通过轨迹级诊断和跨轨迹证据聚合解决了这一核心限制。

### Q3: 论文如何解决这个问题？

DiagEval的核心方法是诊断性评估协议，旨在解决GUI Agent评估中执行失败归因不明确的问题。整体框架是一个顺序诊断循环：在初始Agent执行轨迹获得负面判决后，评估器通过解析失败轨迹、选择分叉点、生成诊断分支并聚合证据，来区分是Agent执行错误还是软件环境缺陷。

主要模块和流程如下：首先，**分叉节点定位**，通过一个基于LLM的反思性裁判，从失败轨迹中识别最早且信息增益最大的分叉点，作为重新探索的起点。其次，**故障诊断摘要**构建，包含分叉点、主导的故障源推测类型和恢复环境上下文。然后，基于故障源推测类型，生成三种**诊断分支**：A类测试替代行动是否可达，B类扩展观测范围，C类测试失败是否可复现。这些分支会通过**预期信息增益分数**排序，优先执行最具区分度的分支。执行后，使用贝叶斯更新规则，根据分支结果（验证成功或失败）动态更新内部归因评分，该评分反映对“软件缺陷”假设的倾向性。若验证成功则立即停止并判定为Agent错误；若评分超过阈值则判定为软件缺陷；否则在预算内继续诊断。

关键技术包括利用LLM基于轨迹摘要进行隐式的分叉点选择和故障源类型预测，以及通过结构化的分支类型和贝叶斯更新规则实现非校准但有效的归因信号聚合。创新点在于主动利用失败轨迹进行定向诊断，而非盲目重试，从而显著提高了评估准确性。

### Q4: 论文做了哪些实验？

论文在WebDevJudge-Unit (502个单元级任务)和RealDevBench (429个可执行用例)两个基准上评估了DiagEval，报告了准确率和每个用例的平均成本。对比方法包括AppEvalPilot、WebVoyager、UI-TARS和模型原生CUA，使用的LLM后端有Qwen3.5-35B-A3B、Claude Opus 4.6和Gemini 3 Flash Preview。诊断设置中，AppEvalPilot作为评估框架，仅在初始判为Fail时调用DiagEval，设置了×1和×2两种诊断预算，候选分支池N=5，执行前K=3。

主要结果：在Gemini 3 Flash Preview后端下，DiagEval (×1)在WDJ-U上准确率达76.1%，在RDB上达78.6%，相比AppEvalPilot的69.9%和65.0%分别提升6.2和13.6个百分点；DiagEval (×2)进一步提升至78.3%和81.6%。假阴性恢复率：×1轮后WDJ-U降低45.6%（114→62），RDB降低47.0%（132→70）。消融实验表明，SOU引导的分支机制是恢复的核心，全DiagEval (×1)的恢复率是NR+IE的两倍多（45.6% vs 20.2%）。双侧归因评分结果显示，DiagEval的终末信号p_end能有效区分AgentFail和EnvFail，ROC-AUC在RDB上达0.620-0.761，在WDJ-U上达0.720-0.763。效率分析显示EIG排序的首分支成功率最高达66%。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于 DiagEval 仅依赖启发式探针和固定更新模型进行二值归因，无法处理多因混淆或概率化不确定性，且对复杂状态图缺乏重构能力。未来可探索以下方向：(1) 引入贝叶斯框架对评估器执行错误与软件缺陷进行概率化建模，从而在证据不充分时输出置信度而非硬归因；(2) 基于失败轨迹自动生成更结构化的诊断探针，例如利用LLM规划最优探针序列以最小化执行成本，或结合强化学习动态选择探针；(3) 将诊断过程扩展至多轮交互场景，通过跨时间步的证据积累实现更鲁棒的归因；(4) 结合GUI状态差分分析，显式建模状态转移图中的未探索路径，为探针设计提供理论指导。这些改进有望提升归因可信度并降低人工复核成本。

### Q6: 总结一下论文的主要内容

论文针对LLM生成交互式软件评估中的核心挑战——正确性是潜UI状态转移图上的图级可达属性，而评估器仅能观测单条执行轨迹，导致失败归因模糊（评估器执行错误 vs 真实软件缺陷）。提出了DiagEval，一种轨迹条件化的诊断评估协议：在失败后，复用失败轨迹选择针对性诊断探针，聚合结果生成内部归因信号，从潜图视角驱动诊断，无需重建图或估计后验概率。在WebDevJudge-Unit和RealDevBench上，DiagEval对假阴性案例恢复45.6-62.1%的初始误归因失败，相对基线提升34.4-160.6%；完整评估集上准确率从69.9%提升至78.3%（WebDevJudge-Unit）和65.0%提升至81.6%（RealDevBench）。结论是可靠GUI评估需结合主动失败诊断来区分评估器错误与真实缺陷，而非仅加强执行。
