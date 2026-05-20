---
title: "MOCHA: Multi-Objective Chebyshev Annealing for Agent Skill Optimization"
authors:
  - "Md Mehrab Tanjim"
  - "Jayakumar Subramanian"
  - "Xiang Chen"
  - "Branislav Kveton"
  - "Subhojyoti Mukherjee"
  - "Anlan Zhang"
  - "Sungchul Kim"
  - "Somdeb Sarkhel"
  - "Sunav Choudhury"
date: "2026-05-19"
arxiv_id: "2605.19330"
arxiv_url: "https://arxiv.org/abs/2605.19330"
pdf_url: "https://arxiv.org/pdf/2605.19330v1"
categories:
  - "cs.AI"
  - "cs.LG"
  - "cs.SE"
tags:
  - "Agent Skill Optimization"
  - "Multi-Objective Optimization"
  - "LLM Agent"
  - "Prompt Engineering"
  - "Pareto Front"
  - "Chebyshev Scalarization"
relevance_score: 9.2
---

# MOCHA: Multi-Objective Chebyshev Annealing for Agent Skill Optimization

## 原始摘要

LLM agents organize behavior through skills - structured natural-language specifications governing how an agent reasons, retrieves, and responds. Unlike monolithic prompts, skills are multi-field artifacts subject to hard platform constraints: description fields are truncated for routing, instruction bodies are compacted via progressive disclosure, and co-resident skills compete for limited context windows. These constraints make skill optimization inherently multi-objective: a skill must simultaneously maximize task performance and satisfy platform limits. Yet existing prompt optimizers either ignore these trade-offs or collapse them into a weighted sum, missing Pareto-optimal variants in non-convex objective regions. We introduce MOCHA (Multi-Objective Chebyshev Annealing), which replaces single-objective selection with Chebyshev scalarization - covering the full Pareto front, including non-convex regions - combined with exponential annealing that transitions from exploration to exploitation. In our experiments across six diverse agent skills - where all methods share the same multi-objective mutation operator and baselines receive identical per-objective textual feedback - existing optimizers fail to improve the seed skill on 4 of 6 tasks: 1000 rollouts yield zero progress. MOCHA breaks through on every task, achieving 7.5% relative improvement in mean correctness over the strongest baseline (up to 14.9% on FEVER and 10.4% on TheoremQA) while discovering twice as many more Pareto-optimal skill variants.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决LLM Agent技能优化中的多目标权衡问题。研究背景是，现代LLM Agent已从使用单一提示词转向使用结构化技能（skill），技能包含描述字段、指令主体和元数据等多个组成部分，并受到硬性平台约束（如描述字符截断、指令长度限制、共存技能争夺有限上下文窗口）。现有方法的不足在于，已有的提示词优化器通常将技能视为单目标文本进行优化，要么完全忽略这些权衡，要么通过加权求和的方式将多个目标合并为一个标量，导致无法覆盖非凸区域中的帕累托最优解。本文要解决的核心问题是：如何在受平台约束的多字段技能优化中，同时最大化任务正确性和平台合规性这两个冲突目标，并有效探索非凸的帕累托前沿。为此，论文提出MOCHA框架，用切比雪夫标量化替代单目标选择，以覆盖完整帕累托前沿（包括非凸区域），并结合指数退火策略，从探索阶段（基于超体积贡献接受）过渡到利用阶段（精炼最弱目标），从而在有限预算下实现多样化的帕累托最优技能变体。

### Q2: 有哪些相关研究？

在相关研究中，本文将问题分解为三个主要类别：提示/指令优化、智能体技能发现与优化、以及多目标优化。

1. **提示/指令优化**：现有方法分为梯度依赖和梯度无关两类。梯度无关方法中，基于反思的迭代优化（如ProTeGi使用UCB波束搜索、TextGrad使用贪心选择、GEPA引入帕累托感知过滤）是本文的基础。区别在于，所有先前方法都将优化目标视为针对单一指标的单一提示，而MOCHA专门处理具有多字段和约束的智能体技能定义，这是关键创新。

2. **智能体技能发现与优化**：相关工作（如SkillRL、Voyager、EUREKA）侧重于从轨迹中提取新技能，样本效率低且与工具耦合紧密。本文则聚焦于在给定现有技能（无论是手工编写还是自动发现）后，通过提示优化来精炼其自然语言定义，这适用于底层模型为闭源API的场景，且无需模型权限。

3. **多目标优化**：经典方法（如NSGA-II）假设连续决策空间和廉价评估，不适用于离散自然语言和昂贵LLM调用的技能优化。线性标量化虽常用但会错过非凸区域中的帕累托最优点。MOCHA首次将切比雪夫标量化和指数退火引入这一无梯度、离散的领域，从而覆盖整个帕累托前沿。

### Q3: 论文如何解决这个问题？

MOCHA将技能优化形式化为多目标优化问题，提出基于切比雪夫标量化的退火搜索算法。整体框架包含两个阶段循环：阶段1通过随机化切比雪夫标量化选择父代技能，从狄利克雷分布采样权重向量并最小化最差加权偏差，保证能覆盖包括非凸区域在内的完整帕累托前沿；阶段2采用指数退火机制在探索和利用模式间平滑切换。探索模式下通过超体积贡献(HVC)评估候选技能，只要在任意方向改善前沿就接受，最大化帕累托多样性；利用模式下则采用切比雪夫接受准则，要求候选必须沿父代选择的权重方向改进前沿。退火阈值τ(b)随预算消耗指数衰减，从初期高阈值促进广泛探索过渡到后期低阈值专注精细优化。关键技术包括：保持HVC优先队列(容量K=5)延迟昂贵验证评估，仅当候选超过退火阈值时才触发完整验证并提交最优候选；通过结构感知变异操作符，向LLM变异器传递字段长度约束和合规状态，引导生成可行区域内的候选；所有目标映射到[0,1]区间，合规性采用线性评分函数。实验证明MOCHA在所有6个任务上突破进步僵局，平均正确率提升7.5%。

### Q4: 论文做了哪些实验？

论文在6种Agent技能上进行了实验：GPQA（研究生STEM问答，正确率）、TheoremQA（数学推理，正确率）、HoVer（事实验证，正确率）、HotpotQA（问答，F1）、FEVER（事实验证，正确率）和DebugBench（代码调试，pass@1）。每个基准采样100训练/100验证/100测试样本。优化目标为正确率、描述合规（≤1024字符）和主体合规（≤5000字符），并报告3D超体积（HV）和帕累托前沿大小。所有方法在相同预算（1000次rollout，5个随机种子）下运行，使用Claude Haiku 4.5执行技能，Claude Opus 4.6作为反射和变异模型。对比方法包括TextGrad（贪婪选择）、ProTeGi（UCB束搜索，束宽3，c=√2）和GEPA（随机帕累托感知选择）。

主要结果：MOCHA在所有6个任务上均取得改进，平均正确率0.675，相对改进7.5%于最强基线ProTeGi（0.628），21.8%于未优化种子（0.554）。基线和种子无改进的任务有4/6（GPQA、HoVer、FEVER、DebugBench），MOCHA分别提升至0.636、0.660、0.726和0.666。在TheoremQA和HotpotQA上基线有改进，但MOCHA在TheoremQA上领先ProTeGi 10.4%（0.762 vs 0.690）。MOCHA发现3.6个帕累托最优变体（基线1.6个），3D HV为0.531（基线0.514）。消融实验显示，移除HVC门控导致最高正确率（0.687）但多样性降低，移除退火导致更多变体（3.8个）但正确率略降（0.671），MOCHA平衡了勘探与利用。

### Q5: 有什么可以进一步探索的点？

论文的局限性首先体现在对低冲突任务（如HotpotQA）的失效场景：当目标之间不冲突时，MOCHA退化为单目标方法的昂贵替代品，未来可设计自动检测目标冲突程度的机制，在低冲突时自适应切换为轻量优化策略。其次，固定的指数退火调度是一个超参数，缺乏对优化进程的响应能力，可探索基于Pareto前沿进展或梯度信息动态调整退火率的自适应调度。第三，合规指标绑定于特定平台SKILL.md规范，不同平台约束差异会改变权衡景观，未来应构建跨平台的约束抽象层来验证方法的泛化性。此外，当前仅优化技能规格而未涉及执行管线（meta-harness），将MOCHA扩展到同时优化管线和技能的组合搜索空间是自然延伸。另外，可结合技能发现（skill discovery）自动生成初始种子技能，避免优化完全依赖人工设计。最后，Chebyshev标量化虽能覆盖非凸区域，但存在权重敏感性，可尝试集成多种标量化策略的元学习框架。

### Q6: 总结一下论文的主要内容

这篇论文提出了MOCHA（多目标切比雪夫退火方法），用于解决大语言模型智能体技能优化中的多目标权衡问题。在现实平台中，技能需要同时最大化任务性能和满足描述长度、指令压缩、上下文窗口等硬约束，这使得优化本质上成为多目标问题。然而现有优化器要么忽略这些约束，要么通过加权求和将其整合，导致无法在非凸区域找到帕累托最优解。MOCHA的核心创新是使用切比雪夫标量化替代单目标选择，能够覆盖整个帕累托前沿（包括非凸区域），并结合指数退火策略从探索过渡到利用。实验覆盖六种不同的智能体技能，在四种任务上现有优化器反复执行1000次仍无进展，而MOCHA在所有任务上均实现突破，平均正确率相对最强基线提升7.5%（FEVER上达14.9%，TheoremQA上达10.4%），并发现两倍以上的更多帕累托最优变体。这项工作展示了多目标优化在技能设计中的关键价值。
