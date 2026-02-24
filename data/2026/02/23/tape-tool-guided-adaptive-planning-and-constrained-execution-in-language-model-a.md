---
title: "TAPE: Tool-Guided Adaptive Planning and Constrained Execution in Language Model Agents"
authors:
  - "Jongwon Jeong"
  - "Jungtaek Kim"
  - "Kangwook Lee"
date: "2026-02-23"
arxiv_id: "2602.19633"
arxiv_url: "https://arxiv.org/abs/2602.19633"
pdf_url: "https://arxiv.org/pdf/2602.19633v1"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "工具使用"
  - "规划"
  - "约束执行"
  - "自适应重规划"
  - "Agent 评测"
relevance_score: 9.0
---

# TAPE: Tool-Guided Adaptive Planning and Constrained Execution in Language Model Agents

## 原始摘要

Language Model (LM) agents have demonstrated remarkable capabilities in solving tasks that require multiple interactions with the environment. However, they remain vulnerable in environments where a single error often leads to irrecoverable failure, particularly under strict feasibility constraints. We systematically analyze existing agent frameworks, identifying imperfect planning and stochastic execution as the primary causes. To address these challenges, we propose Tool-guided Adaptive Planning with constrained Execution (TAPE). TAPE enhances planning capability by aggregating multiple plans into a graph and employing an external solver to identify a feasible path. During execution, TAPE employs constrained decoding to reduce sampling noise, while adaptively re-planning whenever environmental feedback deviates from the intended state. Experiments across Sokoban, ALFWorld, MuSiQue, and GSM8K-Hard demonstrate that TAPE consistently outperforms existing frameworks, with particularly large gains on hard settings, improving success rates by 21.0 percentage points on hard settings on average, and by 20.0 percentage points for weaker base models on average. Code and data available at here.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决语言模型（LM）智能体在具有严格可行性约束（如时间、成本预算或安全限制）的环境中，因单次错误导致任务彻底失败（即不可恢复的失败）的脆弱性问题。作者指出，现有的主流交互式框架（如ReAct）存在两大根本缺陷：一是规划不完善（规划错误），即智能体内部推理可能产生不可行的行动建议；二是执行具有随机性（采样错误），即语言模型在生成行动时可能偏离原本正确的计划。这两种错误在任务步骤增多时会相互叠加，显著降低成功率。为此，论文提出了名为TAPE的新框架，它通过聚合多个候选计划形成计划图，并借助外部求解器选择可行路径来减少规划错误；同时，在执行阶段采用约束解码来抑制采样噪声，并在环境反馈偏离预期时进行自适应重规划，从而在存在不可恢复失败风险的任务中最大化成功率。

### Q2: 有哪些相关研究？

相关工作主要围绕语言模型智能体（LM Agent）的规划与执行框架展开。核心范式是 **ReAct（Reasoning and Acting）框架**（如 ReAct、Reflexion、RAP、ToT 等），它通过迭代的“思考-行动-观察”循环与环境交互，但其在严格可行性约束下容易因单次错误导致不可恢复的失败。另一类方法是 **“先规划后执行”（Plan-and-Act, PA）框架**（如 PlanAndSolve、AdaPlanner 等），它在执行前生成完整计划以减少采样误差，但对规划误差依然脆弱。此外，**工具增强型智能体**（如使用搜索、编码、机器人工具）的研究（如 PAL、LLMCompiler）关注如何利用外部工具扩展能力，但未系统解决规划与执行的可靠性问题。

本文与这些工作的关系是：**TAPE 框架直接针对现有 ReAct 和 PA 框架的缺陷进行改进**。它指出规划误差（内部推理不完善）和采样误差（令牌生成的随机性）是导致不可恢复失败的主因，并通过**多计划聚合与外部求解器选路**来优化规划（减少规划误差），同时采用**约束解码执行**来降低采样噪声。此外，TAPE 引入**自适应重规划机制**以应对环境反馈偏离，从而在严格约束任务中显著提升成功率。实验表明，TAPE 在多个基准上均优于现有框架，尤其在困难任务和弱基础模型上提升显著。

### Q3: 论文如何解决这个问题？

TAPE 框架通过四个核心步骤系统性地解决了语言模型智能体在严格可行性约束环境下因规划不完善和执行随机性导致的脆弱性问题。

首先，在**规划图构建**阶段，框架利用语言模型生成多条抽象轨迹（即包含预测状态和动作的序列），并通过合并具有相同核心信息（如智能体位置、库存物品、任务进度）的状态节点，将这些轨迹折叠成一个有向图。该图结构扩大了规划搜索空间，提高了可行计划存在的概率。同时，框架利用语言模型内部的世界模型为图中的节点（状态）和边（动作）分别预测奖励值和成本向量，为后续的优化选择提供依据。

其次，在**规划路径选择**阶段，TAPE 将当前状态节点、目标节点集合以及预测的奖励与成本输入外部求解器（如整数线性规划 ILP）。求解器在给定的最大步数内，以最大化累计奖励为目标，并满足动作唯一性、路径起始终止节点、流量守恒（路径连续性）以及可能的预算约束，求解出一条最优的可行路径。这一步通过形式化的优化方法替代了语言模型本身的随机规划，显著减少了规划错误。

然后，在**约束执行**阶段，框架采用约束解码技术来抑制采样误差。当智能体在环境中的实际状态节点与计划路径上的预期节点一致时，系统会强制语言模型仅生成计划中规定的下一个动作，通过固定工具选择和工具调用格式来确保动作的精确执行，从而避免了语言模型自回归生成过程中的随机性偏差。

最后，通过**失配检查与重规划**机制来保证鲁棒性。框架持续监控环境反馈的实际状态是否与计划路径上的预测状态一致。一旦检测到失配（如环境意外转移或预算消耗与预估不符），系统便会立即基于最新的观察信息，重新启动规划图构建与路径选择流程，生成适应新情况的最优路径。这种自适应重规划能力使智能体能够动态应对环境的不确定性，从错误中恢复。

### Q4: 论文做了哪些实验？

论文在四个基准测试上进行了实验：Sokoban（推箱子规划谜题）、ALFWorld（具身决策模拟环境）、MuSiQue（多跳事实推理）和GSM8K-Hard（数学推理）。实验设置上，将提出的TAPE框架与两个代表性基线框架进行对比：ReAct（交错推理与行动）和Plan-and-Act（执行预生成计划）。所有方法均基于GPT-4.1-mini模型实现，并集成了相同的提示优化技术（MPO）以确保公平比较。

主要评估指标是任务成功率。实验结果表明，TAPE在所有四个基准测试上均一致且显著地优于基线方法。特别是在容易出现不可恢复状态的困难设置中，TAPE平均将成功率提升了21.0个百分点。分析指出，ReAct受限于规划和采样错误的累积，而Plan-and-Act通过显式计划减少了采样错误，但TAPE通过其工具引导的自适应规划和约束执行机制，更有效地缓解了这两类问题，从而实现了最高的成功率。

### Q5: 有什么可以进一步探索的点？

本文提出的TAPE框架在工具引导的规划与约束执行方面取得了显著进展，但其局限性也为未来研究提供了方向。首先，TAPE依赖外部求解器进行图规划，这增加了计算开销并可能限制其可扩展性；未来可探索更轻量级的内部规划机制或与模型微调结合。其次，约束解码虽减少了执行噪声，但可能过于保守，未来需在灵活性与可靠性间寻求更优平衡。此外，当前实验集中于特定基准环境，未来应测试其在更开放、动态的真实世界场景中的泛化能力。最后，框架对基础模型能力仍有依赖，如何使较弱模型更鲁棒地利用工具与规划，或研究模型无关的Agent架构，是值得深入的方向。

### Q6: 总结一下论文的主要内容

这篇论文提出了TAPE框架，旨在解决语言模型智能体在严格约束环境中因规划不完善和执行随机性而容易失败的问题。其核心贡献在于通过工具引导的自适应规划和约束执行来提升智能体的鲁棒性。具体来说，TAPE首先通过聚合多个初始规划构建规划图，并利用外部求解器寻找可行路径，从而增强规划能力。在执行阶段，它采用约束解码来减少采样噪声，并在环境反馈偏离预期状态时进行自适应重规划。实验表明，TAPE在多个基准测试中显著优于现有框架，尤其在困难设置下平均成功率提升21.0个百分点，并能大幅提升较弱基础模型的能力。该工作为构建更可靠、能处理复杂约束的智能体系统提供了有效方法。
