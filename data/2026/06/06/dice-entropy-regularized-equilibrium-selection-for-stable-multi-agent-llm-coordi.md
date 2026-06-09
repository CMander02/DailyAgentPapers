---
title: "DICE: Entropy-Regularized Equilibrium Selection for Stable Multi-Agent LLM Coordination"
authors:
  - "Yi Xie"
  - "Zhanke Zhou"
  - "Chentao Cao"
  - "Bo Liu"
  - "Bo Han"
date: "2026-06-06"
arxiv_id: "2606.08068"
arxiv_url: "https://arxiv.org/abs/2606.08068"
pdf_url: "https://arxiv.org/pdf/2606.08068v1"
categories:
  - "cs.LG"
tags:
  - "Multi-Agent LLM Systems"
  - "Equilibrium Selection"
  - "Entropy Regularization"
  - "Game Theory"
  - "Coordination"
  - "Prompt Control"
  - "Fine-Tuning"
  - "Multi-Agent Coordination"
  - "LLM Agents"
  - "Benchmark Evaluation"
relevance_score: 9.5
---

# DICE: Entropy-Regularized Equilibrium Selection for Stable Multi-Agent LLM Coordination

## 原始摘要

Multi-agent large language model (LLM) systems often fail to reliably outperform a single strong model equipped with best-of-N sampling. We argue that a core source of this instability is ill-posed equilibrium selection: current systems specify what information agents share, but not which coordination convention should be selected. We formalize a broad class of such systems as discounted incomplete-information Markov games and show that two common pathologies, oscillation between competing conventions and drift across them, can both induce unstable learning and linear Bayesian regret. To obtain a well-posed target, we introduce the Heterogeneous Quantal Response Equilibrium (HQRE), an entropy-regularized equilibrium concept with agent- and state-dependent temperatures. Under a monotonicity condition, HQRE is unique, admits linearly convergent mirror updates, and yields bounded Bayesian regret; the same condition yields rollout-measurable stability diagnostics. We instantiate this objective in two algorithms: DICE-PC, which coordinates frozen models through prompt-control actions, and DICE-FT, which performs parameter-efficient mirror fine-tuning. Across eleven benchmarks in four domains, DICE improves accuracy-cost trade-offs over strong within-class baselines; on reasoning and planning tasks, DICE-PC improves by 4.3 percentage points on average and DICE-FT by 8.5 points.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多智能体大语言模型（LLM）系统中常见的稳定性问题。研究背景是，尽管多智能体系统通过分配规划、求解、批判和验证等角色理论上能提升性能，但实践中往往无法可靠地超越配备最佳采样（best-of-N）的单一强模型。现有方法的不足在于，它们主要关注智能体之间共享什么信息（如对话记录、评判器、摘要器或路由启发式方法），却忽视了一个关键设计维度：**均衡选择**（equilibrium selection）。具体来说，系统没有指定在多种自洽的协调惯例（如分治协议或辩论合并协议）中应该选择哪一种，导致系统可能在不同惯例间振荡（oscillation）或漂移（drift），从而引发学习不稳定和线性贝叶斯遗憾。本文要解决的核心问题正是这种因“不适定均衡选择”导致的**协调不稳定**。作者通过将多智能体协调形式化为折扣不完全信息马尔可夫博弈（IIMG），引入异质量化响应均衡（HQRE）概念，利用熵正则化（带有智能体和状态依赖的温度参数）来明确选择唯一且稳定的均衡目标，从而将隐式的惯例选择显式化，从根本上消除振荡和漂移，实现稳定协调。

### Q2: 有哪些相关研究？

相关研究可分为五类。第一类是单模型推理方法，如思维链和自一致性，它们提升单一策略的探索但无法解决多智能体协调约定间的稳定性问题。第二类是多智能体协调协议，包括辩论框架（如MAD）和系统级框架（如MetaGPT、AutoGen），这些方法增加通信带宽但缺乏形式化的均衡选择目标，本文通过提出一个熵正则化均衡概念来填补这一空白。第三类是聚合与裁决机制，如ChatEval和RECONCILE，它们指定输出如何组合但不保证联合策略的收敛性，而本文则构建了统一定价的不完全信息马尔可夫博弈视角。第四类是多智能体强化学习形式体系，如DEC-POMDP和CTDE方法（如QMIX），这些工作解决可扩展性和信用分配，但未处理均衡多重性问题。第五类是正则化博弈论，本文的HQRE概念建立在量化响应均衡和镜像下降方法基础上，但将其扩展到了具有共享公共流的折扣不完全信息马尔可夫博弈。此外，本文明确区分了单智能体熵正则化（如SAC）与HQRE：单智能体熵用于探索，而HQRE的熵用于将多智能体集合值最优响应转化为唯一不动点，实现均衡选择。

### Q3: 论文如何解决这个问题？

多智能体LLM协调中稳定性不足的核心原因是均衡选择不当。本文论文提出了一种基于熵正则化的均衡选择框架DICE来解决这一问题。首先，论文将多智能体LLM协调形式化为折扣不完全信息马尔可夫博弈，揭示了现有系统因多次均衡导致震荡和漂移两种病态，产生线性贝叶斯遗憾。为解决此问题，论文引入了异质量化响应均衡，这是一种带有智能体和状态依赖温度参数的熵正则化均衡概念。在单调性条件下，HQRE是唯一的，能够避免多重均衡带来的选择不稳定性。论文证明了HQRE的镜像更新具有线性收敛性，并能产生有界贝叶斯遗憾，同时提供了基于rollout的可测量稳定性诊断。基于此理论，论文实例化两种算法：DICE-PC通过提示控制动作协调冻结模型，DICE-FT则进行参数高效的镜像微调。整体框架包含共享公共流和私有历史的信息结构，以及异质温度正则化的目标函数，关键技术包括熵正则化、异质温度参数、镜像下降更新和softmax策略映射，其创新点在于将不稳定的均衡选择转化为唯一的HQRE，通过理论保证稳定性并提升协调效果。

### Q4: 论文做了哪些实验？

论文在四个领域的11个基准测试上进行了实验，包括推理（GSM8K、MATH、MGSM）、规划（PlanBench、Blocksworld）、主动信息获取（BabyAI、ALFWorld）和多智能体协调（Overcooked-AI、Cooperative QA、Negotiation、Debate）。实验设置了两个主要对比算法：DICE-PC用于协调冻结的预训练模型（通过学习提示控制动作的分布），DICE-FT进行参数高效的镜像微调。对比基线包括单模型best-of-N、辩论式方法（如Debate）和集成方法。主要结果显示，在六个推理和规划基准上，DICE-PC相比提示控制基线平均提升4.3个百分点，DICE-FT相比微调基线平均提升8.5个百分点。此外，论文报告了稳定性诊断指标（如单调性条件相关的滚动可测量指标）来验证收敛性，并比较了准确率与token成本的权衡。关键数据指标包括平均准确率提升百分比（如4.3pp和8.5pp），以及在不同基准上DICE方法相比基线的一致改进。

### Q5: 有什么可以进一步探索的点？

论文的局限性与未来探索方向包括：首先，HQRE的单调性条件在实践中可能过于保守，尤其在LLM规模下难以验证，未来可探索更松弛的约束条件或自适应温度调节机制。其次，DICE-PC依赖预定义提示控制动作空间，限制了灵活性；可尝试学习连续化的动作表征或引入可微分提示优化。第三，DICE-FT在协调密集型任务上提升显著但优化困难，可结合离线预训练与在线微调两步法，或利用低秩适配器降低参数干扰。第四，当前分析聚焦于离散动作与有限状态，未来可扩展至连续动作空间与开放域对话场景。此外，理论假设强单调性在实际中可能松动，可开发近似唯一性度量或基于置信区间的稳定性检验工具。最后，当前诊断仅依赖rollout指标，未来可融合信息论指标（如互信息）量化约定漂移，或设计基于元学习的快速适应机制以应对未见过的协调场景。

### Q6: 总结一下论文的主要内容

多智能体大语言模型系统常因协调不稳定而无法优于单模型结合Best-of-N采样。核心问题在于博弈均衡选择不当：系统仅指定信息共享方式，而非选择何种协调惯例。论文将此类系统形式化为折扣不完全信息马尔可夫博弈，指出两种病态——惯例间振荡和跨惯例漂移——均导致线性贝叶斯遗憾。为解决该问题，引入异质量化响应均衡（HQRE），这是一种熵正则化均衡概念，具有智能体与状态依赖的温度参数。在单调性条件下，HQRE唯一且镜像更新线性收敛，贝叶斯遗憾有界。基于此，提出两种算法：DICE-PC通过提示控制协调冻结模型，DICE-FT进行参数高效微调。在四个领域的十一个基准测试中，DICE显著改善准确率-成本权衡，推理与规划任务上DICE-PC平均提升4.3个百分点，DICE-FT提升8.5个百分点。研究揭示了均衡选择是稳定的关键设计维度，并为多智能体协调提供了理论框架和实用方案。
