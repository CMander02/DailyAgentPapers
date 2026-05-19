---
title: "FML-bench: A Controlled Study of AI Research Agent Strategies from the Perspective of Search Dynamics"
authors:
  - "Qiran Zou"
  - "Hou Hei Lam"
  - "Wenhao Zhao"
  - "Tingting Chen"
  - "Yiming Tang"
  - "Samson Yu"
  - "Yingtao Zhu"
  - "Srinivas Anumasa"
  - "Zufeng Zhang"
  - "Tianyi Zhang"
  - "Chang Liu"
  - "Zhengyao Jiang"
  - "Anirudh Goyal"
  - "Dianbo Liu"
date: "2026-05-17"
arxiv_id: "2605.17373"
arxiv_url: "https://arxiv.org/abs/2605.17373"
pdf_url: "https://arxiv.org/pdf/2605.17373v1"
github_url: "https://github.com/qrzou/FML-bench"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "AI Research Agent"
  - "Agent Strategy"
  - "Search Dynamics"
  - "Benchmark"
  - "Tree Search"
  - "Greedy Hill-Climbing"
  - "Evolutionary Optimization"
  - "Process-Level Metrics"
  - "Exploration Behavior"
  - "Agent Infrastructure"
relevance_score: 9.5
---

# FML-bench: A Controlled Study of AI Research Agent Strategies from the Perspective of Search Dynamics

## 原始摘要

AI research agents accelerate ML research by automating hypothesis generation, experimentation, and empirical refinement. Existing agent strategies range from greedy hill-climbing to tree search and evolutionary optimization, yet which strategy choices drive performance remains unclear. Answering this question requires a benchmark that separates agent strategy (e.g., search topology) from execution infrastructure (e.g., code editor), so that performance differences are attributable to strategy rather than infrastructure, and that provides process-level metrics beyond final scores to analyze exploration behaviors. Existing benchmarks offer limited support. We propose FML-Bench, a benchmark of 18 fundamental ML research tasks across 10 domains that separates agent strategy from execution infrastructure and defines 12 process-level behavioral metrics. Evaluating six representative agents, we find that: (1) strategy complexity alone does not guarantee strong performance: a simple greedy hill-climber nearly matches the best-performing tree-search agent, both well above the remaining agents; (2) our analysis suggests this pattern relates to improvement opportunity structure: greedy search tends to be more effective when opportunities are dense, while tree-search and evolutionary strategies tend to be more effective when opportunities are sparse; an adaptive agent built on this insight switches to broader exploration upon detecting improvement stagnation and outperforms the other six agents, lending initial support to this observation; and (3) process-level analysis reveals that early convergence and directionally focused exploration are significantly associated with final performance, while solution diversity and compute cost are not. Our benchmark is available at: https://github.com/qrzou/FML-bench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决AI研究代理（AI research agents）领域的一个核心问题：在自动化机器学习研究中，代理策略中的哪些具体选择（如搜索拓扑、记忆机制等）真正驱动了最终研究表现的提升？当前的研究背景是，虽然出现了多种代理策略（从贪婪爬山法、树搜索到进化优化），但缺乏受控实验来分离策略与执行基础设施的影响。现有方法存在两个主要不足：第一，每种代理通常自带专用的执行基础设施（如代码编辑器），导致性能差异难以归因于策略本身；第二，现有评估主要依赖于最终分数（如测试指标），缺乏过程层面的行为指标来分析代理的探索过程。因此，本文提出了FML-Bench基准测试，包含18个跨10个领域的基础机器学习研究任务，其核心创新在于将代理策略与执行基础设施完全分离，并定义了12个过程级行为指标。通过评估六种代表性代理，本文试图回答：策略复杂度是否直接决定性能？不同搜索策略在什么样的改善机会结构下更有效？哪些过程指标与最终性能显著相关？这些问题的解答有助于为设计更高效的AI研究代理提供理论指导。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要从基准测试和智能体策略两个维度梳理了现有工作。

**基准测试方面**：现有相关工作包括MLAgentBench（13个手工ML任务）、MLE-bench（75个Kaggle竞赛）、DSBench（540个数据科学任务）、ML-Dev-Bench（30个ML工作流）、SWE-bench（2294个GitHub问题）和RE-Bench（7个R&D任务）。这些基准的局限性在于：1）每个智能体自带执行基础设施（如代码编辑器），导致性能差异无法归因于策略本身；2）除MLAgentBench和RE-Bench外，大多仅报告最终分数，缺乏过程级指标。FML-bench通过分离执行基础设施与智能体策略，并引入12个过程级行为指标来克服这些问题。

**智能体策略方面**：相关工作覆盖从贪心爬山到树搜索再到进化优化的搜索拓扑谱系。贪心策略代表如Autoresearch；树搜索策略包括AI Scientist v2（最佳优先搜索）、AIDE（交替改进与调试）、AIRA（UCT-MCTS）、MARS（预算感知MCTS）；进化策略包括AlphaEvolve（MAP-Elites）、OpenEvolve（种群进化）；此外还有Agent Laboratory等角色分工框架。与这些工作不同，FML-bench在同一受控基础设施上公平比较不同策略，并首次从搜索机会结构角度解释策略有效性差异。

### Q3: 论文如何解决这个问题？

论文通过FML-Bench基准框架系统性地解决了如何分离AI研究代理策略与执行基础设施影响的问题。核心方法是将搜索策略（如拓扑结构、提示模板、记忆机制）与代码编辑、实验执行等共享基础设施解耦，使性能差异完全归因于策略本身。框架设计了12个过程级行为指标（如探索展开度、到达距离、有效维度等）来分析代理的搜索动态，超越传统仅关注最终分数的评估。

关键技术包括：1）统一的迭代实验循环，其中只有"下一步尝试什么"的决策由代理策略控制；2）共享的代码编辑器和执行环境，所有代理使用同一个LLM（GPT-5.4）确保公平性；3）严格验证/测试分离；4）统一的指标渲染格式。评估了6种代表性代理（从简单的贪心爬山到复杂的树搜索），发现自研的AdaptiveSearch代理通过在线检测改进停滞信号（连续W步无提升），自适应地从贪心搜索切换为多分支探索，在18个任务上取得最优平均归一化测试改进（0.208）和胜率（58.6%），验证了搜索策略应根据在线观察的改进动态自适应的核心创新点。

### Q4: 论文做了哪些实验？

论文在FML-Bench基准上进行了系统实验，该基准包含10个领域的18个基础机器学习研究任务，将智能体策略与执行基础设施解耦，并定义了12个过程级行为指标。实验设置了6种代表性AI研究智能体：TAS v1、TAS v2、AIDE、AIRA、Autoresearch和OpenEvolve。每个智能体在每项任务上运行3轮独立实验，每轮预算为100个优化步骤，总共324次运行，所有运行使用同一底层LLM（GPT-5.4），训练和测试在NVIDIA A100-80GB GPU上进行。性能报告为标准测试改进量$\hat{p}$。

主要结果：TAS v2平均测试改进最高（0.193），胜率58.5%；Autoresearch几乎持平（0.192，57.4%）；AIDE和OpenEvolve居中；TAS v1和AIRA垫底。值得注意的是，最简单的贪婪爬山器（Autoresearch）几乎匹配最复杂的四阶段最佳优先树搜索（TAS v2），而理论上最严谨的UCT-MCTS智能体（AIRA）排名最后，表明策略复杂度与性能无单调关系。

进一步实验设计了自适应智能体AdaptiveSearch，其核心思想是当贪婪搜索在连续$W$步后无改进时，自动切换到多分支探索。AdaptiveSearch实现平均测试改进0.208，胜率58.6%，均超过其他所有智能体。事后分析显示，Autoresearch在高密度改进机会任务上排名第一，但在低密度任务上降至第六，而AdaptiveSearch在两类任务上均排名前二。

过程级分析显示：AUC-over-steps是最强预测因子（$\rho=+0.784, p<0.001$），First-improvement step负相关（$\rho=-0.291, p<0.001$），Exploration Reach正相关（$\rho=+0.115, p=0.039$），Effective dim负相关（$\rho=-0.140, p=0.011$），而探索唯一性、token成本和壁钟时间与性能无显著关联。

### Q5: 有什么可以进一步探索的点？

基于FML-bench的发现，未来可从以下方面深入探索：(1) 自适应策略切换：论文已验证“检测改进停滞时切换至更广探索”的有效性，未来可设计更动态的混合策略，如基于贝叶斯优化的实时策略选择，根据搜索空间的局部密度自动调整探索-利用平衡。(2) 更广泛的智能体覆盖：目前仅涵盖六种拓扑，可引入强化学习、贝叶斯优化或基于LLM的元学习智能体，进一步验证策略复杂性与性能关系的边界条件。(3) 执行基础设施的解耦研究：当前统一剥离原生代码编辑器可能低估性能，未来可系统研究不同编辑器（如交互式调试器、自动代码修复工具）对策略有效性的调节作用。(4) 过程级指标的因果分析：虽发现早收敛速度与性能相关，但需通过干预实验（如强制引导探索方向）确认因果关系，并探索如何将“方向聚焦”纳入策略设计目标。此外，在固定步长下的排名稳定性需通过变步长实验验证，以避免预算偏见影响结论。

### Q6: 总结一下论文的主要内容

这篇论文介绍了FML-bench基准，旨在通过分离智能体策略与执行基础设施，控制性地研究AI研究智能体的搜索策略效果。该基准包含10个领域的18个基础ML研究任务，并定义了12个过程级行为指标。通过评估六种代表性智能体（从贪心爬山到树搜索和进化优化），主要发现：（1）策略复杂度不保证性能，简单的贪心爬山智能体与树搜索智能体表现相近，均远超其他智能体；（2）贪心搜索在改进机会密集时有效，而树搜索等更广的策略在改进机会稀疏时更优；基于此洞察设计的自适应智能体在检测到停滞时切换策略，性能超越所有六种基线；（3）过程分析表明，早期收敛速度和定向探索与最终性能显著相关，而解多样性和计算成本则无关。该工作为设计更有效的AI研究智能体策略提供了控制性实验基础。
