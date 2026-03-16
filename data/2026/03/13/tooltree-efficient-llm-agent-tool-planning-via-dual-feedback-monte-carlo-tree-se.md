---
title: "ToolTree: Efficient LLM Agent Tool Planning via Dual-Feedback Monte Carlo Tree Search and Bidirectional Pruning"
authors:
  - "Shuo Yang"
  - "Soyeon Caren Han"
  - "Yihao Ding"
  - "Shuhe Wang"
  - "Eduard Hoy"
date: "2026-03-13"
arxiv_id: "2603.12740"
arxiv_url: "https://arxiv.org/abs/2603.12740"
pdf_url: "https://arxiv.org/pdf/2603.12740v1"
categories:
  - "cs.AI"
tags:
  - "Tool Planning"
  - "Monte Carlo Tree Search"
  - "Reasoning"
  - "Multi-step Tasks"
  - "Tool Use"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# ToolTree: Efficient LLM Agent Tool Planning via Dual-Feedback Monte Carlo Tree Search and Bidirectional Pruning

## 原始摘要

Large Language Model (LLM) agents are increasingly applied to complex, multi-step tasks that require interaction with diverse external tools across various domains. However, current LLM agent tool planning methods typically rely on greedy, reactive tool selection strategies that lack foresight and fail to account for inter-tool dependencies. In this paper, we present ToolTree, a novel Monte Carlo tree search-inspired planning paradigm for tool planning. ToolTree explores possible tool usage trajectories using a dual-stage LLM evaluation and bidirectional pruning mechanism that enables the agent to make informed, adaptive decisions over extended tool-use sequences while pruning less promising branches before and after the tool execution. Empirical evaluations across both open-set and closed-set tool planning tasks on 4 benchmarks demonstrate that ToolTree consistently improves performance while keeping the highest efficiency, achieving an average gain of around 10\% compared to the state-of-the-art planning paradigm.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在执行复杂多步骤任务时，工具规划能力不足的问题。研究背景是，随着LLM智能体被应用于软件工程、网页浏览、多模态理解等多个领域的复杂任务，通过调用外部工具来扩展其功能边界变得至关重要。然而，现有的工具规划方法存在显著缺陷：一类是通用智能体框架（如LangChain），它们通常采用贪婪的、反应式的工具选择策略，每一步只选择看似局部最优的工具，缺乏长远规划视野，无法考虑工具间的相互依赖关系，导致早期错误决策会累积并影响后续步骤；另一类是基于树搜索的方法（如Tree-of-Thoughts），虽然引入了搜索来探索行动序列，但通常只评估文本层面的“思考”，与实际工具执行的效用脱节，且当工具种类繁多、参数复杂时，搜索空间会指数级膨胀，带来高昂的计算成本和不可预测的延迟，难以扩展到多模态、多领域的真实工具生态系统中。

因此，本文要解决的核心问题是：如何设计一种既具备前瞻性、能进行多步序列规划，又能够基于实际工具执行结果进行接地气评估，同时保持高计算效率的LLM智能体工具规划方法。具体而言，论文提出了ToolTree框架，其核心创新在于将工具规划构建为一个由蒙特卡洛树搜索（MCTS）启发的搜索问题，并引入了双阶段LLM评估（执行前预测效用与执行后评估实际贡献）和双向剪枝机制。这使得智能体能够在固定计算预算下，自适应地探索有前景的工具使用轨迹，并及时剪除不理想的搜索分支，从而在复杂、存在工具依赖的任务中做出更明智、更鲁棒的决策。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕LLM智能体工具规划方法展开，可归纳为以下几类：

**1. 基于贪心或反应式策略的方法**：这类方法（如ReAct、Toolformer等）在每一步根据当前状态选择最合适的工具，缺乏长远规划能力，无法考虑工具间的依赖关系。本文指出它们属于“短视”策略，而ToolTree通过树搜索实现了序列级的规划。

**2. 树搜索增强的规划方法**：部分研究将工具规划构建为搜索问题，使用广度/深度优先搜索或启发式搜索。本文借鉴了蒙特卡洛树搜索（MCTS）框架，但传统MCTS在工具规划中面临搜索空间大、仿真成本高的问题。ToolTree的核心创新在于引入了**双反馈评估机制**（执行前LLM评估与执行后实际反馈结合）和**双向剪枝**（执行前后均进行分支剪枝），显著提升了搜索效率与效果。

**3. 基于强化学习或学习型策略的方法**：一些工作尝试通过强化学习或模仿学习来训练工具使用策略，但它们通常需要大量训练数据或环境交互。本文的ToolTree属于无需训练、基于搜索的规划范式，更适用于工具库动态变化或样本稀缺的场景。

**与现有工作的区别**：ToolTree区别于传统贪心策略，具备前瞻性；相较于普通树搜索，它通过双阶段LLM评估和双向剪枝降低了搜索复杂度，在保持高效的同时实现了更优的序列决策。实验表明其在多项基准上平均优于现有方法约10%。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为ToolTree的新型规划范式来解决LLM智能体在复杂多步骤任务中工具规划效率低、缺乏前瞻性的问题。其核心方法是将多工具使用建模为一种受蒙特卡洛树搜索（MCTS）启发的、在可执行轨迹上的搜索过程。

整体框架遵循MCTS的基本循环，但进行了关键性改造。主要模块包括：选择、预评估、扩展、执行、后评估和反向传播。整个过程以一个固定的调用预算（R_max）为约束，目标是找到最大化任务效用的工具调用轨迹。

架构设计的核心创新在于**双反馈评估与双向剪枝机制**。首先，在传统的MCTS利用（由Q值驱动）和探索平衡基础上，ToolTree引入了**预评估信号** r_pre(s,a)。这是一个在工具执行前，由LLM“法官”根据当前上下文、工具卡片和生成的参数草案快速预测的有用性分数。该分数被整合到改进的UCT选择公式中，作为先验增强的探索奖励，从而在搜索早期将探索偏向有前景的分支。其次，在工具执行后，引入**后评估信号** r_post(s,a)，由同一LLM“法官”对实际产生的输出进行基于任务一致性、相关性等标准的评分。该分数用于更新行动的价值估计Q(s,a)，驱动后续的利用行为。

关键技术体现为**双向剪枝**。预评估支持**执行前剪枝**：在扩展节点时，只对预评估分数超过阈值τ_pre（或保留前K个）的候选工具动作创建子节点，从而在调用前就过滤掉明显不兼容或低收益的分支，有效控制分支因子。后评估支持**执行后剪枝**：对于执行后评分低于阈值τ_post的边，将其标记为不可扩展，防止在已被证据证明无效的路径上继续浪费预算。此外，系统还采用了确定性缓存（避免同一调用重复执行）和错误令牌处理（使下游能明确处理失败）等技术来提升效率。

总之，ToolTree的创新点在于将前瞻性的预评估与后验性的后评估深度融入MCTS循环，通过双向剪枝在探索与利用、广度与深度之间实现高效平衡，使得智能体能够在有限的调用预算内，做出具有适应性和远见的规划决策，从而显著提升任务性能与效率。

### Q4: 论文做了哪些实验？

实验在闭集和开集工具规划两种任务上进行评估。闭集任务使用GTA和m&m数据集，每个数据集提供固定工具集（大小分别为14和33），包含类型化输入/输出和短多跳链，评估采用逐步模式和端到端模式。开集任务使用ToolBench和RestBench数据集，分别包含16,464和143个真实API，涉及多工具检索与规划场景，评估指标为通过率和胜率。

对比方法方面，闭集任务比较了零样本、ReAct、思维链、最佳优先搜索、思维树、A*搜索和蒙特卡洛树搜索等方法；开集任务比较了零样本、思维链、ReAct、DFSDT和蒙特卡洛树搜索。所有方法在相同的工具模式、类型预选管道和缓存策略下进行公平比较，并保持相同的计算和探索预算。

主要结果显示，ToolTree在闭集任务中整体表现最佳。在GPT-4o模型上，GTA数据集平均得分达66.95，优于普通MCTS基线2.2分以上；m&m数据集平均得分达88.61，优于零样本基线8分以上。关键指标如工具选择F1、参数预测F1、规划与执行F1均领先。在开集任务中，ToolTree在RestBench和ToolBench上同样取得最高平均分，例如在GPT-4o上，RestBench-TMDB平均分为74.50，ToolBench为69.04。效率分析表明，ToolTree在步数限制为16-64步时性能优势最明显，且单位时间内的准确率提升最高，实现了性能与时间的最佳权衡。

### Q5: 有什么可以进一步探索的点？

该论文提出的ToolTree方法在工具规划效率和效果上取得了显著提升，但其局限性在于仍依赖于预定义的工具集和固定的评估机制，缺乏对动态环境变化的适应能力。未来研究可探索以下几个方向：首先，引入在线学习机制，使代理能根据实时反馈动态调整工具选择策略，而不仅依赖离线搜索；其次，结合强化学习优化树搜索的启发函数，减少对人工设计评估提示的依赖；此外，可研究跨领域工具迁移能力，通过元学习让代理快速适应新工具组合。从系统层面看，当前方法在长序列任务中可能面临组合爆炸风险，未来可集成分层规划思想，将复杂任务分解为子目标，再应用树搜索，以进一步提升可扩展性。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为ToolTree的新型LLM智能体工具规划方法，旨在解决现有方法在复杂多步骤任务中因贪婪、反应式工具选择而缺乏前瞻性和忽视工具间依赖关系的问题。其核心贡献在于设计了一种受蒙特卡洛树搜索启发的规划范式，通过双阶段LLM评估与双向剪枝机制来高效探索工具使用轨迹。具体而言，该方法在工具执行前后分别进行前瞻性评估和结果验证，动态剪枝低潜力分支，从而在扩展的工具使用序列中做出更明智、自适应的决策。实验在四个基准测试上进行，涵盖开放集和封闭集工具规划任务，结果表明ToolTree在保持最高效率的同时，性能相比最先进的规划范式平均提升约10%，显著提高了LLM智能体在跨领域多工具协作任务中的规划能力与执行效果。
