---
title: "AEL: Agent Evolving Learning for Open-Ended Environments"
authors:
  - "Wujiang Xu"
  - "Jiaojiao Han"
  - "Minghao Guo"
  - "Kai Mei"
  - "Xi Zhu"
  - "Han Zhang"
  - "Dimitris N. Metaxas"
date: "2026-04-23"
arxiv_id: "2604.21725"
arxiv_url: "https://arxiv.org/abs/2604.21725"
pdf_url: "https://arxiv.org/pdf/2604.21725v1"
github_url: "https://github.com/WujiangXu/AEL"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.CE"
tags:
  - "Agent记忆与反思"
  - "LLM Agent自适应学习"
  - "多智能体协作"
  - "Agent评估基准"
  - "开放环境Agent"
relevance_score: 8.5
---

# AEL: Agent Evolving Learning for Open-Ended Environments

## 原始摘要

LLM agents increasingly operate in open-ended environments spanning hundreds of sequential episodes, yet they remain largely stateless: each task is solved from scratch without converting past experience into better future behavior. The central obstacle is not \emph{what} to remember but \emph{how to use} what has been remembered, including which retrieval policy to apply, how to interpret prior outcomes, and when the current strategy itself must change. We introduce \emph{Agent Evolving Learning} (\ael{}), a two-timescale framework that addresses this obstacle. At the fast timescale, a Thompson Sampling bandit learns which memory retrieval policy to apply at each episode; at the slow timescale, LLM-driven reflection diagnoses failure patterns and injects causal insights into the agent's decision prompt, giving it an interpretive frame for the evidence it retrieves. On a sequential portfolio benchmark (10 sector-diverse tickers, 208 episodes, 5 random seeds), \ael{} achieves a Sharpe ratio of 2.13$\pm$0.47, outperforming five published self-improving methods and all non-LLM baselines while maintaining the lowest variance among all LLM-based approaches. A nine-variant ablation reveals a ``less is more'' pattern: memory and reflection together produce a 58\% cumulative improvement over the stateless baseline, yet every additional mechanism we test (planner evolution, per-tool selection, cold-start initialization, skill extraction, and three credit assignment methods) \emph{degrades} performance. This demonstrates that the bottleneck in agent self-improvement is \emph{self-diagnosing how to use} experience rather than adding architectural complexity. Code and data: https://github.com/WujiangXu/AEL.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决LLM智能体在开放端环境中无法有效利用过往经验来持续提升自身行为的问题。当前，LLM智能体虽已具备规划、工具调用和记忆存储等模块，但在处理跨越数百个连续回合的开放端任务时，仍近乎“无状态”：每个任务都从零开始解决，无法将过去的经验转化为未来更优的表现。现有的自我改进方法如Reflexion、ExpeL、EvoTool，都只进化单一模块（如记忆、工具或规划），而固定其他模块。然而在实际的开放端环境中，智能体的能力是规划、工具使用和记忆等多个模块协同交互的结果，当多个模块同时变化时，性能变化的归因会变得模糊，这被称为多模块信用分配问题，它阻碍了智能体作为一个协调系统进行整体改进。因此，本文的核心问题是解决智能体如何*利用*已记住的经验，包括应用何种检索策略、如何解读先前结果以及何时当前策略本身需要改变，其瓶颈在于自我诊断而非增加架构复杂性。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：

1. **基础智能体框架**：ReAct提出推理-行动范式，Tree of Thoughts通过分支扩展推理，Toolformer实现工具调用。这些方法构成现代智能体的“规划器、工具、记忆”三模块，但部署后通常固定不变。AEL的创新在于让这三个模块都可进化。

2. **自我改进方法**：Reflexion在上下文窗口累积自我批评（无结构化检索）；Voyager通过课程学习构建技能库（不调整工具或规划）；ExpeL用关键词匹配提取经验；Meta-Reflexion将反思蒸馏为规则（最接近AEL但未进化工具/规划器）；EvoTool通过归因变异进化工具策略（固定记忆）；FactorMiner结合技能与经验记忆。与这些方法不同，AEL是唯一同时进化工具、记忆和规划器，并采用双时间尺度反射驱动自我诊断的系统。

3. **在线学习与归因**：上下文赌博机与Thompson采样提供高效在线学习。Shapley值为多模块归因提供博弈论框架，但通常将模块视为黑箱。AEL系统评估了三种信用分配方法（均匀、因子反事实、LLM驱动），发现简单方法在噪音环境下更优，揭示了信用分配仍是一个重要开放挑战。

### Q3: 论文如何解决这个问题？

AEL通过双时间尺度框架解决开放环境中智能体无法利用历史经验的问题。核心方法是结合Thompson Sampling多臂赌博机与LLM驱动的反思机制。在快速时间尺度上，每个episode开始时，Thompson Sampling从五种记忆检索策略池中选择最优策略，维护Beta后验分布来平衡探索与利用，根据episode结果进行贝叶斯更新。在慢速时间尺度上，每M个episode后，LLM接收聚合轨迹进行因果诊断，包括每个工具准确性统计和市场条件分析，生成因果洞察注入到决策提示中，帮助智能体理解检索到的证据。

整体框架包含三个主要模块：一是三级记忆系统（episodic、semantic、procedural），通过复合相关性评分函数（结合特征匹配、质量分数、新鲜度和层级权重）渐进式蒸馏经验；二是Thompson Sampling赌博机选择检索策略；三是LLM反思系统诊断失败模式并触发进化。技术创新点包括：统一学分分配将episode结果转化为Beta分布更新，防止高噪声环境下的错误归因；智能体进化仅在诊断出结构性失败时触发（连续3个慢窗口失败），避免随机变异。实验表明，在208个episode的基准测试中，AEL实现了2.13的夏普比率，优于所有基线方法，且消融研究发现增加任何复杂性都会降低性能，证实了核心瓶颈在于如何使用经验而非堆积机制。

### Q4: 论文做了哪些实验？

论文在D-full基准测试上进行了实验，该数据集包含10个跨7个GICS板块的股票代码，共208个回合（140训练/40验证/28测试），采用1小时分辨率数据。对比方法包括4种非LLM基线（等权重、动量加权、最小方差、逆动量）、5种先前自我改进方法（Reflexion、ExpeL、FactorMiner、Meta-Reflexion、EvoTool）以及HyperAgent。所有方法共享相同的12个工具和Claude Haiku 4.5作为骨干LLM。主要结果使用夏普比率、索提诺比率、卡尔玛比率、累计收益率、最大回撤、胜率和尾部比率7个冻结测试指标评估。AEL取得了最佳性能：夏普比率2.13±0.47，索提诺比率4.08±1.11，卡尔玛比率10.40±2.75，在所有基于LLM的方法中方差最低。增量构建实验显示：无状态1.35→+内存1.68→AEL 2.13，记忆带来+24%提升，反思进一步带来+27%提升。9种消融实验揭示“少即是多”模式：移除预热组件导致绩效下降最大（Δ=−0.88），而添加任何复杂性（规划器演化Δ=−1.72、每工具选择Δ=−1.70、冷启动初始化Δ=−1.31、技能提取Δ=−1.11）或更改信用分配方法（FCC信用Δ=−1.09、LLM-FCC信用Δ=−0.64）均降低性能。

### Q5: 有什么可以进一步探索的点？

论文的局限性与未来方向集中在实验环境的短视性（仅208轮）和“少即是多”的反直觉发现上。在短期、高噪声场景中，任何自适应机制（如规划器进化、工具选择）的探索成本都超过了其收益，这暗示现有评估范式可能低估了长期学习的价值。未来可探索以下方向：1）在更长的时间跨度（如数千轮）中验证框架，以观察慢速反射能否积累足够的因果洞察来克服初始探索开销；2）当前统一的Thompson采样可能过于保守，可研究分层或多臂赌博机结构以区分“何时保留旧策略”与“何时探索新记忆检索”；3）AEL的反射机制依赖LLM诊断失败模式，但缺乏对诊断质量的自评估，可引入元认知校验模块来自动过滤无效因果假设。此外，如何将模块化信用分配（如每组件独立信号）泛化到非组合式决策场景，也是破解“复杂架构反噬”瓶颈的关键方向。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为 Agent Evolving Learning（AEL）的两时间尺度框架，用于解决 LLM 智能体在开放环境中的记忆利用问题。主要挑战在于智能体不知如何使用而非记忆内容。方法上，在快时间尺度，用汤普森采样学习每轮应采用的记忆检索策略；在慢时间尺度，由 LLM 驱动反思来诊断失败模式并注入因果洞察到决策提示中。在包含 10 个行业多样股票、208 轮、5 个随机种子的时序投资基准上，AEL 实现夏普比率 2.13±0.47，超过五种已发布的自我改进方法和所有非 LLM 基线，且方差最小。关键结论是，智能体自我改进的瓶颈在于自我诊断如何使用经验，而非增加架构复杂性，多数附加机制（如规划器演化、工具选择、信用分配等）反而降低性能，其中统一信用分配方法优于复杂方案，表明信用分配仍是开放挑战。
