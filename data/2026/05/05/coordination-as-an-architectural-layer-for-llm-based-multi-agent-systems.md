---
title: "Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems"
authors:
  - "Maksym Nechepurenko"
  - "Pavel Shuvalov"
date: "2026-05-05"
arxiv_id: "2605.03310"
arxiv_url: "https://arxiv.org/abs/2605.03310"
pdf_url: "https://arxiv.org/pdf/2605.03310v1"
categories:
  - "cs.MA"
  - "cs.LG"
  - "q-fin.TR"
tags:
  - "Multi-Agent Systems"
  - "Coordination Architecture"
  - "Prediction Markets"
  - "LLM-Based Agents"
  - "Orchestration"
  - "Failure Mode Analysis"
  - "Brier Score Decomposition"
relevance_score: 8.0
---

# Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems

## 原始摘要

Multi-agent LLM systems fail in production at rates between 41% and 87%, mostly due to coordination defects rather than base-model capability. Existing responses split between cataloguing failure modes empirically and shipping declarative orchestration frameworks as engineering tools; neither delivers a principled mapping from coordination configuration to predictable failure-mode signature. We argue that coordination should be treated as a configurable architectural layer, separable from agent logic and from information access, enabling architectural reasoning rather than only engineering productivity.
  We instantiate this with an information-controlled design on prediction markets: a single LLM, fixed tools, fixed per-call output cap, and fixed prompt template across five reference coordination configurations, with total compute per question treated as an endogenous architectural output. The Murphy decomposition of the Brier score separates calibration from discriminative power, so configurations leave distinguishable signatures even when aggregate scores coincide.
  On 100 Polymarket binary markets resolved after the model's training cutoff (claude-opus-4-6) we report Murphy signatures, a cost-quality Pareto frontier, category-conditioned analysis, and a bootstrap power-projection. Three of five pre-specified predictions are upheld in direction; two configurations dominate the Pareto frontier within this regime; exploratory bootstrap intervals separate consensus alignment from others, though pairwise tests do not survive Bonferroni correction at n=100. We also deploy the same configurations as live agents on Foresight Arena under web-search-enabled conditions, as an on-chain replication channel accumulating in parallel. Harness, trace dataset, and production agents are released. We position this as a methodology-validating first instantiation, not a general cross-model claim.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多智能体LLM系统在部署中因协调缺陷导致的高失败率问题。研究背景是，多智能体LLM系统在生产中的失败率高达41%至87%，且现有研究表明这些失败主要源于协调问题（如规范模糊、智能体间目标不一致、验证缺失），而非基础模型能力不足。现有方法存在两大不足：一是实证研究虽然详列了失败模式，但未能将具体的架构配置（如谁向谁委派、何时决策、结果如何聚合）与可测量的失败特征联系起来；二是工业界的声明式编排框架（如AWS Strands、Microsoft Foundry）虽然将工作流与代码分离，但其动机仅为工程效率（加快部署、方便修改），并未将这种分离作为预测或解释系统行为的分析工具。此外，现有经验比较中常混淆架构效应与信息访问量变化的影响。因此，本文的核心问题是：能否将协调视为一个可配置的架构层（独立于智能体逻辑和信息访问），并建立从协调配置到可预测失败特征（如校准度和区分度）的映射，从而实现架构推理，而不仅仅是工程便利。

### Q2: 有哪些相关研究？

根据论文，相关研究主要分为三类：

1. **失败模式经验分类研究**：如MAST论文（分析了AutoGen、MetaGPT等7种框架的1600+执行轨迹，识别出14种细粒度失败模式，发现79%的失败源于协调而非基础模型能力）、辩论式多智能体系统研究（揭示对齐压力会压制正确少数派观点）、以及关于纯协调能力的基准测试（Overcooked、Hanabi）。这些工作的共同点是描述性而非预测性，不能从架构配置预测特定失败模式。

2. **声明式编排框架研究**：包括AWS Strands协作模式、微软Foundry Agent Service、领域特定语言（将工作流编译为JSON中间表示，减少67%开发时间）、以及“认知蓝图”与“运行时引擎”的分离方案。这些方法主要关注工程生产力（更快的部署和重构），而非架构预测。

3. **方法论批判研究**：提出了基于信息的决策理论模型，核心是非可识别性定理——当两种架构在工具访问、上下文检索或对话长度上存在差异时，无法将性能差异归因于协调而非信息。这与本文的信息控制设计直接相关，本文将此要求作为硬性方法论约束。

此外，论文还借鉴了分布式系统协调理论（Linda元组空间、CSP、actor模型）和概率预测评估方法论（Brier评分分解、LLM预测文献中的参考分数）。本文的创新在于将协调视为可配置的架构层，实现从架构配置到失败模式签名的可预测映射。

### Q3: 论文如何解决这个问题？

论文提出将协调（coordination）从代理逻辑和信息访问中分离出来，作为一个可配置的架构层（architectural layer）。核心方法是信息控制的实验设计：固定信息层（工具、检索上下文、提示模板）和代理层（单一LLM、固定输出上限），仅变化协调层。协调层由七要素明确定义：代理端点、通信拓扑（有向图）、决策权威分布、同步机制、聚合规则、终止条件和故障处理。这使协调配置成为可独立分析的变量，而非隐含在代码中的工程细节。

实验采用五类参考配置，在中央化程度和信息共享两个轴上覆盖设计空间：独立集成（并行聚合）、同行批评辩论（多轮修订）、编排器-专家（分解分派）、顺序流水线（固定阶段执行）和共识对齐（迭代至收敛）。这些配置在信息层固定、计算量作为内生输出的条件下比较，从而将性能差异归因于协调结构而非计算量。

关键技术是使用Murphy分解将Brier评分拆分为校准误差（REL）和分辨能力（RES）两个独立分量。不同协调配置在这些分量上产生可区分的特征签名：例如，共识对齐预测极低REL和极低RES（多样性坍塌），同行辩论预测REL改善但RES下降（分歧抑制）。这使得协调缺陷（如错误级联、过早收敛、上游脆弱性）从隐式运行故障变成可通过Murphy签名验证的显式预测。实验使用Polymarket的未来二元市场（训练截止后）确保污染抵抗，Brier评分的严格适当性确保准确性不被策略行为混叠。总体上，该方法将协调从一个工程问题转化为可通过架构推理和分解测试系统分析的设计空间。

### Q4: 论文做了哪些实验？

论文在信息控制方法论下进行了两组实验。**核心实验**在100个Polymarket二元市场（结果发生在模型训练截止日期`claude-opus-4-6`之后）上进行，采用固定LLM、工具集、提示模板和单次调用输出上限，仅变化五种协调配置（如独立集成或顺序流水线）。主要结果包括：1）Brier评分的Murphy分解将校准度（REL）与分辨力（RES）分离，揭示不同协调架构即使聚合分数相同也会留下不同的失败模式签名；2）报告了成本-质量Pareto前沿，其中两种配置在该前沿上占据主导；3）类别条件分析显示架构效应在特定问题域更显著；4）Bootstrap功率投影（Proposion 3，需约350个样本/条件以达到0.02的Alpha差异、0.80的统计功效）在n=100时将共识对齐配置与其他区分开，尽管配对检验未通过Bonferroni校正。**部署实验**将相同配置作为实时智能体部署在Foresight Arena（启用网络搜索环境），作为链上复制渠道并行积累数据。论文释放了数据、全追踪集和生产智能体。关键数据指标包括Brier分数及其Murphy分解项、Alpha分数（相对于市场共识的超额Brier）及其分解，以及每个问题消耗的总token数（作为内生计算成本）。

### Q5: 有什么可以进一步探索的点？

论文提出的“协调作为架构层”框架仍存在明显局限：其一，实验仅基于单一模型（Claude-Opus-4）和预测市场领域，泛化性存疑，未来需在多种模型（如GPT-4、Llama系列）、多任务类型（编程、问答、谈判）中验证；其二，协调配置与失效模式间的映射仍停留于统计关联层面，缺乏可解释的因果机制，可引入可解释性工具（如注意力归因、干预实验）深入剖析；其三，当前Brier分数分解虽能区分标定与区分能力，但未考虑动态交互中的策略性适应（如模型间的对抗性博弈），未来可结合强化学习或进化论视角，构建协调模式的自我优化机制。此外，探索“混合协调架构”——在同一任务生命周期内动态切换协调模式——有望在成本-质量Pareto前沿上突破当前局限，实现更鲁棒的多智能体系统设计。

### Q6: 总结一下论文的主要内容

这篇论文认为，多智能体LLM系统在生产中的失败率高达41%至87%，主要源于协调缺陷（如规范模糊、智能体间不一致等），而非基础模型能力不足。现有应对方法要么是经验性地分类失败模式，要么是提供声明式编排框架作为工程工具，但都缺乏从协调配置到可预测失败模式特征的原则性映射。本文提出应将协调视为一个可配置的架构层，使其与智能体逻辑和信息访问分离，从而实现架构推理。作者通过一个基于预测市场的信息控制实验来验证这一设计：固定底层LLM、工具、输出预算和提示模板，仅改变五种参考协调配置（独立集成、同行批评辩论、编排器-专家、顺序流水线、共识对齐），并利用Brier分数的Murphy分解将校准误差与区分能力分离。在100个Polymarket二元市场上的实验结果显示，三类预设预测得到支持，两种配置在成本-质量帕累托前沿上占优，且bootstrap区间将共识对齐配置与其他配置区分开。论文的贡献在于提出了架构框架、预设预测、实验方法论及其实例化，而非提出新的智能体框架或通用最优结论。
