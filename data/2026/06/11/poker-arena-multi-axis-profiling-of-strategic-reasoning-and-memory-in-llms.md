---
title: "Poker Arena: Multi-Axis Profiling of Strategic Reasoning and Memory in LLMs"
authors:
  - "Pratham Singla"
  - "Shivank Garg"
  - "Vihan Singh"
date: "2026-06-11"
arxiv_id: "2606.13815"
arxiv_url: "https://arxiv.org/abs/2606.13815"
pdf_url: "https://arxiv.org/pdf/2606.13815v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Agent Benchmark"
  - "Multi-Agent System"
  - "Strategic Reasoning"
  - "Memory Architecture"
  - "LLM Evaluation"
  - "Agent Profiling"
  - "Game-Playing Agent"
relevance_score: 8.5
---

# Poker Arena: Multi-Axis Profiling of Strategic Reasoning and Memory in LLMs

## 原始摘要

Strategic reasoning under uncertainty underpins consequential decisions in negotiation, finance, and policy, but prevailing game-play benchmarks collapse heterogeneous reasoning dimensions into a single scalar, leaving the capability structure of frontier LLMs unexamined. We introduce Poker Arena, a no-limit Texas Hold'em tournament platform that couples a three-layer memory architecture (within-hand, session, and cross-session) with a nine-axis cognitive profile decomposing strategic reasoning into interpretable dimensions such as bet-sizing calibration and positional awareness. We evaluate seven frontier models across 50 sessions of 1,000 hands and a controlled memory ablation; tournament chips and aggregate axis score order the field differently: Claude Opus 4.6 wins +$15,730 chips with 14 first-place finishes, yet ranks only fifth of seven on mean axis score, while persistent memory helps some models and hurts others. These findings show that multi-axis evaluation surfaces capability structure that scalar leaderboards systematically misrank, with cross-dimensional consistency outweighing peak performance on any single axis.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前大语言模型(LLM)策略推理评估中的核心问题。研究背景是：LLM在谈判、金融和政策等不确定性条件下的决策中日益重要，而扑克因其包含下注、诈唬、对手建模和期望值推理等多种可解离的认知能力，成为测试LLM战略推理的理想场景。现有方法的不足主要有三点：第一，现有的游戏基准测试将异质的推理维度压缩为单一标量(如总筹码)，无法揭示模型的能力结构；第二，最优扑克AI依赖反事实遗憾最小化和大规模自对弈搜索，这些训练时方法不适用于推理时冻结权重的LLM；第三，现有记忆架构主要研究单智能体或合作场景，缺乏对竞争性多智能体行为的刻画，且很少将持久记忆作为控制变量。本文要解决的核心问题是：设计一个多轴认知评估框架(Poker Arena)，通过三层记忆架构和九轴认知剖面(包括下注校准、诈唬、对手阅读、位置意识等可解释维度)，在1000手德州扑克比赛中分解测量LLM的战略推理能力，揭示标量排行榜对模型能力的系统性误排，并探究持久记忆对不同模型能力的异质性影响。

### Q2: 有哪些相关研究？

以下是与本研究相关的主要工作类别及关系说明：

**方法类相关工作**：经典扑克AI依赖反事实遗憾最小化（CFR）和大规模自对弈搜索，但这些是在线训练方法，无法直接用于推理时的固定权重LLM；朴素提示的LLM智能体则缺乏跨手牌的持久记忆能力。本文提出的三层记忆架构（局内、会话、跨会话）填补了这一空白，允许细粒度控制和消融实验。

**评测类相关工作**：现有游戏类基准（如博弈Benchmarks）通常将多种推理能力压缩为单一标量指标，混淆了出牌策略、筹码规模校准、位置意识等可分离的认知维度。本文引入九轴认知剖面，将策略推理分解为可解释的多个独立维度，揭示了标量排行榜的系统性误排名问题。

**应用与记忆架构相关工作**：现有记忆研究多聚焦于单智能体或协作环境，缺乏竞争性多智能体行为的刻画。本文在竞争性扑克环境中系统探究持久记忆（会话级与跨会话级）对不同模型的影响，发现记忆效果具有模型依赖性——某些模型受益而另一些模型受损。

**对手建模与心理理论评估**：本研究在匿名化对手处理、适应性决策等方面与对手建模相关，但更侧重于可控记忆条件下的多维能力分解，而非单纯的对手预测能力评估。

### Q3: 论文如何解决这个问题？

Poker Arena通过一个多维评估框架来系统性地剖析LLM在策略推理和记忆方面的能力结构，其核心方法包括一个三层记忆架构和一个九轴认知画像。

整体框架由四个组件构成：游戏引擎、三层记忆系统、提示词管道和模型网关。游戏引擎模拟无限注德州扑克锦标赛，包含精确的底牌评估、蒙特卡洛胜率采样和边池计算，确保符合标准锦标赛规则。

三层记忆架构是核心创新。第一层是“手内上下文”，在每个决策点临时构建，包含手牌、公共牌、下注历史和对手化名，并在决策后丢弃。第二层是“会话级记忆”，为每个智能体在每个会话中维护一个最大16K字符的文本缓冲区。每手牌结束后，智能体根据摘要选择性更新该记忆，而非被动累积所有信息。第三层是“跨会话记忆”，它是持久化的终身记忆，在会话结束时通过合并函数更新，并在新会话开始时通过播种策略初始化会话记忆。这种设计允许智能体在多个时间尺度上保留和整合策略信息。

九轴认知画像提供可解释的能力分解。它包含九个评估维度，其中五个基于确定性行动日志统计（如下注规模校准、情绪稳定性、适应性、策略混合、位置意识），两个基于正则表达式匹配推理文本（如预测准确性、事实准确性），还有两个是混合方法，结合确定性计数和LLM裁判评分（如诈唬检测、对手解读）。混合方法尤其创新，因为“有意诈唬”和“具体对手读牌”这类信号只存在于推理文本中，无法简化为正则表达式匹配。裁判模型选择时避免了家族偏差，确保与被评估的选手不属于同一模型家族。

这个框架的创新在于能够揭示标量排行榜系统性错误排序的能力结构，表明跨维度一致性比任何单一维度的峰值表现更重要。

### Q4: 论文做了哪些实验？

论文进行了两项核心实验。首先，在50场7人制德州扑克锦标赛（共1000手牌，9115个动作）中，评估了7个前沿大模型（Claude Opus 4.6、Grok 4、GPT-5.4、DeepSeek V3.1、Qwen3-max、Gemini 3.1 Pro、Kimi K2）。实验记录了每位模型的累计筹码变化、胜率、第一名次数等指标。结果显示：Claude Opus 4.6以+15,730筹码和14次第一名大幅领先，而Kimi K2表现最差（-12,558筹码，平均排名5.10）。但九轴认知剖面分析显示，冠军Claude的平均轴得分仅排第五（0.5754），而Grok平均轴得分最高（0.6137）却仅获亚军，Spearman检验显示排名相关性不显著（ρ=+0.571，p=0.180）。其次，进行了持久记忆消融实验（600手牌，每组10场配对比赛），通过向会话层2注入前序会话信息，发现记忆对不同模型影响方向不同：GPT获益（+114.6筹码）、Kimi受损（-109.4筹码）、Claude轻微受损（-42.5筹码），但均未达到统计显著性（p>0.05）。

### Q5: 有什么可以进一步探索的点？

论文的局限主要在于仅评估了七种模型，样本量有限且缺乏人类基线的对比，无法充分揭示LLM策略推理与人类水平的差距。未来可扩展更大规模的模型面板，并引入人类玩家作为参照基准。当前九轴剖析虽具解释性，但忽略了风险偏好和反事实推理等关键维度，可增加“风险调适”和“对手模型学习”等轴以覆盖更全面的认知结构。记忆消融实验显示会话间记忆对不同模型影响各异，表明记忆并非统一增强因素，未来研究应设计模型条件化记忆机制，例如根据模型架构定制记忆衰减率或上下文窗口，避免一刀切。此外，锦标赛中的牌局动态依赖多智能体交互，当前单智能体评估可能无法捕捉协作或对抗性的涌现行为，可引入多智能体博弈模拟来检验模型在复杂社会推理中的表现。最终，多轴综合评分与标量排名之间的不一致暗示需要新的聚合方法，如加权帕累托前沿，以更公平地反映模型在不同维度上的权衡。

### Q6: 总结一下论文的主要内容

Poker Arena 提出了一种多轴评估框架，用于剖析大语言模型在战略推理和记忆方面的能力。传统博弈评估将异构推理维度压缩为单一标量，忽视了能力结构。该工作构建了一个无限注德州扑克竞技平台，结合三层记忆架构（局内、会话和跨会话）与九轴认知画像，将战略推理分解为下注尺度校准、位置意识等可解释维度。通过对七个前沿模型进行50个会话（1000手牌）评估和受控记忆消融实验，发现锦标赛筹码与聚合轴得分排序结果不同：Claude Opus 4.6筹码赢最多（+15,730）但轴得分均值仅排第五。记忆对模型表现的影响也呈现异质性。结论表明，多轴评估能揭示标量排行榜系统性地错误排序的能力结构，跨维度一致性比单一维度的峰值性能更关键。
