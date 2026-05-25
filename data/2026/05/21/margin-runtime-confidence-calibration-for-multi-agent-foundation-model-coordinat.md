---
title: "MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination"
authors:
  - "Joss Armstrong"
date: "2026-05-21"
arxiv_id: "2605.22949"
arxiv_url: "https://arxiv.org/abs/2605.22949"
pdf_url: "https://arxiv.org/pdf/2605.22949v1"
categories:
  - "cs.LG"
  - "cs.MA"
tags:
  - "Multi-Agent Systems"
  - "Confidence Calibration"
  - "Foundation Model Agents"
  - "Runtime Adaptation"
  - "Distribution Shift"
relevance_score: 8.5
---

# MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination

## 原始摘要

Foundation model agents increasingly operate in multi-agent deployments where a coordinator must decide which agent's response to trust. The standard approach weights agents by their self-reported confidence, but recent evidence shows that foundation model confidence is systematically mis-calibrated and, on hard tasks, inversely correlated with accuracy. Design-time calibration methods (temperature scaling, Platt scaling, histogram binning) cannot address this problem because they fit a fixed correction to held-out data and degrade under distribution shift.
  We present MARGIN (Multi Agent Runtime Grading via Incremental Normalization), an online calibration method that learns per-agent, per-confidence-band calibration factors from the task stream itself, requiring no model access, no held-out data, and no retraining. MARGIN uses symmetric exponentially weighted moving averages with Bayesian shrinkage blending, and has three hyperparameters with robust defaults. Across 19 foundation models, 8 benchmarks, and over 50,000 observations, MARGIN achieves 3-6x lower calibration error than the best design-time baseline under distribution shift. In multi-agent selection, raw verbalized confidence produces pairwise resolution worse than random (45-56%) on hard benchmarks. MARGIN corrects this completely, raising pairwise resolution to 70-89% and surpassing the always-best-model oracle on three of four benchmarks. Six formal propositions characterize convergence, tracking speed, and the optimality of symmetric updates for non-strategic agents, with all predictions illustrated empirically.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体基础模型协作中的运行时置信度校准问题。研究背景是，在多个基础模型智能体协同工作的场景中，协调者需要根据智能体自报的置信度来决策信任哪个智能体的输出。然而，现有方法的不足在于：首先，基础模型的置信度存在系统性误校准，甚至在困难任务上与准确率呈负相关，导致选择最高置信度的智能体反而会选出错误答案；其次，已有的校准时方法（如温度缩放、Platt缩放、直方图分箱）均属于设计时校准，它们依赖固定验证集拟合校正函数，一旦部署后任务分布发生偏移，校准效果会急剧恶化（实验中分布偏移下ECE从个位数飙升至37-63）。本文要解决的核心问题正是：在连续变化的在线任务流中，如何无需访问模型内部、无需预留校准集，实时动态地校准每个智能体在不同置信度区间上的可信度，从而提升多智能体协调的正确率。方法上提出了MARGIN，利用对称指数加权移动平均和贝叶斯收缩技术在线学习校准因子。

### Q2: 有哪些相关研究？

相关研究主要分为以下几类。**校准方法类**包括设计时校准（温度缩放、Platt缩放、直方图分箱）及其在LLM上的扩展（如Thermometer、ConfTuner、DACA），它们均存在分布偏移下性能退化的问题；MARGIN则是首个运行时在线校准方法，无需预训练数据和固定修正。**多智能体协调类**涵盖多智能体辩论（如Du等人、AutoGen）、异构辩论框架（如A-HMAD）以及基于置信度的模型选择（如FrugalGPT、Gerych等人），这些方法均直接依赖未校准的置信度进行权重分配或路由；MARGIN在底层提供校准层，确保下游协调机制可靠。**信任与声誉系统类**（如Jøsang综述、EigenTrust）跟踪全局可靠性，但无法捕捉置信度条件性差异；MARGIN则记录每个智能体在不同置信带内的条件可靠性，并证明对称更新（非战略智能体最优）与经典非对称规则有本质区别。**在线学习与自适应校准类**包括指数加权移动平均（EWMA）和自适应共形预测，MARGIN创新性地将其应用于结构化置信度校准，引入贝叶斯收缩融合解决冷启动问题，并提供了对称性最优的形式化分析。

### Q3: 论文如何解决这个问题？

MARGIN的核心方法是提出一种在线校准框架，解决了传统离线校准方法在面对分布偏移时失效的问题。整体框架包含三个关键模块：首先将置信度区间划分为K=3个等宽带，每个(智能体,置信带)对独立维护两个运行估计——经验准确率和平均置信度，均通过对称指数加权移动平均（EWMA）以学习率α=0.04进行在线更新。这种对称更新设计基于核心观察：基础模型智能体的误校准是认知性的而非策略性的，对称EWMA在此条件下是无偏估计器，而非对称更新会引入系统偏差。其次采用贝叶斯收缩技术应对冷启动问题：将带级校准因子与全局模型级先验进行混合，当某置信带的观测数n较小时，因子被拉向更稳定的模型级估计，收缩常数k_s=100控制混合速率，随着观测积累逐渐过渡到纯带级因子。最后，校准后的置信度通过加权投票进行多智能体选择：对每个候选答案累加校准置信度，选择得分最高的答案。MARGIN的三个创新点包括：无需模型内部访问、无需离线校准集、完全在线运行；通过置信带划分捕获不同置信区间的异质性误校准模式；对称EWMA+贝叶斯收缩的组合在分布偏移下能快速自适应，实现3-6倍更低的校准误差。

### Q4: 论文做了哪些实验？

论文主要进行了两大实验：**单模型校准误差实验**和**多智能体选择实验**。实验涵盖了19个基础模型（包括Qwen、DeepSeek、GPT等云端API模型及4-bit量化的本地模型）和8个基准测试（HumanEval、MBPP、BigCodeBench等）。实验设置包括在无分布偏移（同一数据集划分）和分布偏移（从简单基准迁移到困难基准）两种场景下评估。对比方法包括Raw（原始置信度）、Temperature Scaling、Platt Scaling和Histogram Binning。主要评价指标是预期校准误差（ECE）和多智能体选择的pass@1。

**主要结果**：在分布偏移下，MARGIN的ECE比最优设计时基线低3-6倍。在多智能体选择中，原始口头置信度在困难基准上成对分辨率低于随机水平（45-56%），而MARGIN将其完全纠正，提升至70-89%，并超越了始终选择最佳模型的神谕基线。

### Q5: 有什么可以进一步探索的点？

论文中MARGIN方法虽然展现了优秀的在线校准能力，但仍存在几个值得进一步探索的方向。首先，MARGIN依赖于固定置信度分箱（bands），但最优分箱边界可能随任务分布变化而动态调整，未来可探索自适应分箱策略。其次，EWMA的单一学习率α=0.04虽然在实验中表现稳健，但Proposition 4揭示的偏差-方差权衡表明，若能根据任务流中估计的漂移率δ动态调整α，可能获得更优的校准性能。此外，当前方法假设代理为非策略性的（Proposition 5），但在真实多智能体系统中，代理可能自适应调整其策略以响应校准反馈，这将打破对称最优性假设，需要设计考虑策略互动的校准机制。另一个有趣的方向是结合MARGIN与设计时方法：利用MARGIN的在线估计来检测分布偏移，触发设计时校准器的动态更新或迁移。最后，当前验证集中在问答等结构化任务，在更开放、多模态的智能体协调场景（如具身机器人协作）中的有效性有待验证。

### Q6: 总结一下论文的主要内容

多智能体基础模型部署中，协调者需要根据各代理的自报告置信度决定信任哪个响应。然而，基础模型的置信度在困难任务上系统性地校准不良，甚至与准确率呈负相关。现有设计时校准方法（如温度缩放、Platt缩放）因在固定数据上拟合校正，在分布偏移下性能严重退化。本文提出MARGIN（多智能体运行时增量归一化分级），这是一种在线校准方法，通过对称指数加权移动平均和贝叶斯收缩混合，从任务流中学习每个代理在特定置信区间的校准因子，无需模型访问、保留数据或重新训练。在19个基础模型、8个基准测试和超过5万次观测中，MARGIN在分布偏移下校准误差比最优基线低3-6倍。在困难代码生成任务中，原始置信度成对选择比随机更差（45-56%），MARGIN将其完全修正至70-89%。此外，MARGIN校准后的多代理选择在四个基准中的三个上超越了始终最优模型基线。六个理论命题刻画了收敛性、跟踪速度和对称更新对非策略代理的最优性。这项工作为多智能体系统提供了首个运行时置信度校准方案，显著提升了分布偏移下的可靠性和选择性能。
