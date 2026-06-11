---
title: "TreeSeeker: Tree-Structured Trial, Error, and Return in Deep Search"
authors:
  - "Zhuofan Shi"
  - "Mingzhe Ma"
  - "Lu Wang"
  - "Fangkai Yang"
  - "Pu Zhao"
  - "Yiming Guan"
  - "Youling Huang"
  - "Wei Zhang"
  - "Qingwei Lin"
  - "Dongmei Zhang"
  - "Saravan Rajmohan"
date: "2026-06-10"
arxiv_id: "2606.11662"
arxiv_url: "https://arxiv.org/abs/2606.11662"
pdf_url: "https://arxiv.org/pdf/2606.11662v1"
categories:
  - "cs.AI"
tags:
  - "Agent推理"
  - "Web搜索"
  - "树搜索"
  - "推理时计算"
  - "多步决策"
  - "分支回溯"
  - "Agent记忆"
relevance_score: 9.5
---

# TreeSeeker: Tree-Structured Trial, Error, and Return in Deep Search

## 原始摘要

Deep search requires agents to answer complex questions through multi-step web search, browsing, evidence comparison, and synthesis. A central challenge is deciding how to search when several directions look plausible but only some will later lead to reliable evidence. If an agent greedily follows the current best-looking direction, it may keep extending a weak continuation. If it explores without discipline, it may waste budget on disconnected trials. We propose TreeSeeker, an inference-time framework for controlled trial-and-error in deep search. TreeSeeker organizes search as branch-and-return search over tree-structured states, where each branch is a tentative direction for a sub-goal. At each round, TreeSearch reads all sub-goal trees, identifies active goals, and uses textual UCB signals of value, uncertainty, and risk to select among exploiting a promising branch, exploring an uncertain alternative, or pruning an unproductive continuation and returning to an earlier branch point. TreeMem supports this control loop by keeping evidence, uncertainty, conflicts, progress, and failure cues attached to the branches that produced them, so trial outcomes can guide later decisions. Experiments on XBench-DeepSearch, BrowseComp, and BrowseComp-ZH show that TreeSeeker consistently outperforms strong open-source baselines, suggesting that explicit branch-and-return control complements stronger reasoning and tool execution.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文针对深度搜索任务中的控制问题提出解决方案。深度搜索要求智能体通过多步网络搜索、浏览、证据比较和综合来回答复杂问题。现有方法虽然通过智能体训练、上下文压缩和结构化子目标分解提升了搜索能力，但未能解决当多个搜索方向看似合理时，智能体如何有效分配搜索预算的核心问题。具体而言，现有方法存在两大不足：一是若贪心地持续跟随当前最优方向，可能陷入并延伸一条薄弱线索；二是若不加区分地探索替代方向，则可能在零散尝试中浪费预算。因此，当早期搜索方向存在不确定性（如一个网页、查询或假设初看有价值但后续证据薄弱或冲突时），智能体缺乏明确机制来决定何时继续、何时尝试替代、何时放弃并回溯。本文提出的TreeSeeker旨在解决这一搜索控制问题，通过将搜索组织为树状结构上的分支与返回过程，利用价值、不确定性和风险信号进行类似UCB的决策，使智能体能够在有限预算下实现受控的试错，有效利用有利方向、测试不确定替代方案并从无效果的路径中恢复。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是**顺序推理-行动-观察循环**的方法，如ReAct、IterResearch、WebSailor、WebDancer和WebtThinker，它们通过工作区重建、改进的Web推理或长程训练来增强搜索，但均未在目标内跨替代路径进行基于证据的预算重新分配。TreeSeeker的核心区别在于将每条候选路径视为持久语义分支状态，并基于累积证据和失败信号决定深化、探索或剪枝哪个分支。第二类是**长时程智能体的上下文瓶颈缓解**方法，包括ReSum、IterResearch、MemAgent和AgentFold，它们通过压缩或重构历史来避免上下文过载，但组织历史为单一演化状态。TreeSeeker采用了不同的总结角色——TreeMem将证据保留在生成该证据的分支上，形成分支本地状态作为决策对象而非记忆设备。第三类是**基于探索-利用权衡的树搜索方法**，如Language Agent Tree Search (LATS)、Plan-MCTS、ExACT以及MCTS-RAG系列方法，它们在定义明确的行动空间（如查询改写、文档选择）上运作。TreeSeeker将UCB直觉扩展到深度搜索场景，通过文本评分规则从语义分支状态估计价值、剩余不确定性和风险，并配备返回机制以剪枝无效延续并重定向到早期分支点。

### Q3: 论文如何解决这个问题？

TreeSeeker 将深度搜索组织为树状分支-回归搜索，核心由 TreeSearch 和 TreeMem 两个组件构成。整体框架首先将根问题分解为多个子目标，每个子目标关联一棵搜索树。第一层分支是解决子目标的候选路径（如不同查询或来源），更深层节点记录沿路径产生的动作和观察。TreeSearch是中央试验-错误控制器，在每个决策轮次，它一次性读取所有子目标树的状态，为每个活跃的、依赖就绪的子目标输出一个操作。它使用文本UCB信号（价值、不确定性、风险）从三个操作中选择：Exploit（继续有前景的分支）、Explore（测试不确定的备选分支）、Prune（停止无用的延续并回归到较早的分支点）。这种操作级选择避免了穷举路径-动作对的组合爆炸。TreeMem为每个分支存储故障感知的记录，包括证据、不确定性、冲突、进展和失败线索。它采用三层结构：根节点存目标状态，第一级节点是候选路径并存储分支状态，更深节点存最近工具调用和观察的原始轨迹。被剪枝的延续会被压缩为简短的失败线索。这样，TreeSearch可以根据各分支的结构化信息进行比较决策，将试验-错误转变为系统的分支-回归搜索。关键创新点在于：1）显式的分支-回归控制，允许从失败路径中恢复；2）文本UCB信号，以语义形式量化分支价值、不确定性和风险；3）操作级决策，在单个轮次中并行管理多个子目标树。

### Q4: 论文做了哪些实验？

论文在三个公开的深度搜索基准上评估了TreeSeeker：XBench-DeepSearch、BrowseComp和BrowseComp-ZH（后者为中文场景）。由于资源限制，从BrowseComp和BrowseComp-ZH中各随机采样100个实例作为测试子集。对比方法包括Tongyi DeepSearch、IterResearch、Flash-Searcher、LATS等开源系统，以及OpenAI DeepResearch、Gemini DeepResearch等闭源系统。实现上，默认使用gpt-5.2作为骨干模型，并在同等搜索和浏览工具下与Flash-Searcher进行gpt-4.1对照实验。主要结果显示，使用gpt-5.2时，TreeSeeker在XBench-DS上达到56.3分，在BrowseComp上达到47.0分，在BrowseComp-ZH上达到43.0分，均超过所有评估的开源基线方法。与Flash-Searcher相比，使用gpt-4.1时TreeSeeker在三个基准上分别高出1.7、2.0和2.6分。消融实验在XBench-DS上进行，去除Textual UCB使分数下降至52.0（-4.3），去除Explore和Prune操作导致最大下降至48.0（-8.3），去除TreeMem叶迹使分数降至51.3（-5.0）。操作频率分析表明，完整的TreeSeeker维持了Exploit（51.39%）和Explore（43.45%）的相对平衡，Prune使用较少（5.17%）。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：首先，当前评估局限于纯文本搜索场景，未整合多模态工具（如图像/视频理解），未来可扩展至多模态证据源以增强深度搜索的泛用性；其次，分支-回溯控制引入了额外推理代价，尽管总成本可控，但在延迟或预算敏感场景下仍需优化控制器与记忆模块的调度策略，例如通过稀疏化记忆更新或自适应UCB计算频率来降低开销；最后，系统依赖的外部网页搜索存在噪声、偏见或过时风险，虽然TreeSeeker通过证据比较与失败线索保留了鲁棒性，但高可靠性场景仍需要人类审核。未来可探索引入可信度评级机制（如与知识图谱或权威源交叉验证），或设计动态预算分配算法（根据搜索复杂度自动调整返回层级深度）。此外，结合强化学习对分支选择策略进行端到端优化，可能进一步提升在长尾查询或对抗性信息场景下的表现。

### Q6: 总结一下论文的主要内容

论文提出TreeSeeker，一个用于深度搜索的推理时框架，旨在解决多步网络搜索中的分支决策难题。传统方法要么贪婪跟随当前最佳方向导致弱延续，要么无纪律探索浪费预算。TreeSeeker将搜索组织为树结构状态的支路-返回搜索，通过两个核心组件实现：TreeSearch利用文本UCB信号（价值、不确定性、风险）在探索当前最佳支路、探索不确定替代或剪枝低效支路并返回之前分支点之间做出决策；TreeMem将证据、不确定性、冲突、进展和失败线索附着在产生它们的支路上，以指导后续决策。在XBench-DeepSearch、BrowseComp及BrowseComp-ZH上，TreeSeeker持续优于强开源基线。核心贡献在于证明显式的支路-返回控制机制能有效补充更强的推理和工具执行能力，为长程深度搜索中早期决策不确定性问题提供了系统化解决方案。
