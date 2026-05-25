---
title: "Push Your Agent: Measuring and Enforcing Quantitative Goal Persistence in Long-Horizon LLM Agents"
authors:
  - "Yuandao Cai"
  - "Yuzhang Zhu"
  - "Liyou Gao"
  - "Wensheng Tang"
  - "Shengchao Qin"
date: "2026-05-22"
arxiv_id: "2605.23574"
arxiv_url: "https://arxiv.org/abs/2605.23574"
pdf_url: "https://arxiv.org/pdf/2605.23574v1"
categories:
  - "cs.LG"
  - "cs.SE"
tags:
  - "Agent评测"
  - "长期任务"
  - "目标持久性"
  - "工具使用"
  - "工作单元追踪"
  - "状态追踪"
relevance_score: 8.5
---

# Push Your Agent: Measuring and Enforcing Quantitative Goal Persistence in Long-Horizon LLM Agents

## 原始摘要

Long-horizon language agents can make many plausible local tool calls yet fail to persist until a requested count is actually complete. We study this gap as Quantitative Goal Persistence (QGP): whether an agent keeps working until an external verifier confirms enough distinct valid items. PushBench turns this into a benchmark for repository-artifact collection and verifier-backed work units, so repeated work, duplicate submissions, false completion, and progress drift are measured directly rather than hidden behind a final success flag. In matched controller comparisons, a state-tracking retrieval controller reaches 69-78% success while eliminating duplicate submissions, and a backlog-tracking work-unit controller reaches 25-50% success in settings where standard and completion-gated controllers complete no task instances. Black-box frontier-agent evaluations with Claude Code (Sonnet 4.6) and Codex CLI (gpt-5.4) solve many 50-artifact tasks but drop to 3 out of 9 successes per condition at 100 artifacts. The results show that quantitative goals stress a different reliability requirement from local task competence: agents must maintain verified progress and stop only when the requested work is complete.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要研究了长周期语言智能体在执行需要完成特定数量任务的场景中，未能坚持到目标完成的问题。现有的智能体基准测试虽然评估了任务最终成功率，但常常掩盖了进度丢失的具体原因，例如提前停止、重复工作、重复提交或对已完成工作的夸大汇报，这些行为在最终的成功率指标中不可见。本文提出的核心概念是“定量目标持久性”，即智能体是否能够持续工作，直到外部验证器确认其完成了足够数量且不同的有效工作单元。为了解决这个问题，论文设计了 PushBench 基准测试，通过仓库工件收集和基于验证器的工作单元两类任务，直接衡量重复工作、重复提交、虚假完成和进度漂移等行为。其核心目标是评估和强制要求智能体具备定量目标持久性，使其在满足明确的数量条件前不会停止工作，从而区分局部任务能力和可靠的进度维持能力。

### Q2: 有哪些相关研究？

相关研究主要可分为以下几类：

**1. 方法与基准类**：如ReAct、Toolformer、ToolLLM、API-Bank、Gorilla等研究改进了工具调用和推理-行动交错能力，但通常将定量停止条件隐含处理；本文则聚焦于外部可审计的进度状态与控制器合约。

**2. 评测类**：AgentBoard提出了多轮智能体的细粒度进度率，但本文的定量目标坚持（QGP）将停止条件本身作为评估对象，直接测量虚假完成、过早停止、重复工作等失败模式，而非事后轨迹摘要。

**3. 软件基准类**：从HumanEval、MBPP到SWE-bench等基准强调任务真实性与可执行成功，而PushBench专门隔离了定量坚持性与外部可审计的终止条件。

**4. 记忆与编排类**：记忆增强型智能体管理上下文与用户偏好，QGP失败看似记忆问题，但本文区分在于QGP状态是外部可检查的进度（已提交单元、重复项、剩余目标计数），而非任意回忆的上下文。

本文与这些工作的核心区别在于：它不关注局部任务能力或工具选择，而是将已验证的进度跟踪作为任务合约的一部分，要求智能体仅当外部验证器确认足够数量的不同有效项时才停止。

### Q3: 论文如何解决这个问题？

论文通过提出 **PushBench 基准** 和 **状态追踪控制器** 来解决长时域 LLM Agent 在定量目标持续性上的缺陷。核心方法在于将定量目标持续性定义为可验证的任务元组 (环境、目标、验证器、目标数量、预算)，并围绕外部验证器构建评估体系，从而直接测量重复工作、虚假完成和进度漂移，而非仅依赖最终成功标志。

**整体框架** 包含两大任务族：`Reposcan` 测试搜索提交场景下的持续性，`DataOps` 则在验证器背书的工作单元上增加短工作循环。框架分离策略提议和控制执行，通过标准化指标（如验证进度、虚假完成率、重复工作计数）量化 Agent 表现。

**关键技术** 创新性地提出了三类持久性控制器：1) **Stateful 控制器** 专用于标识检索，通过存储已提交标识、已查看搜索页、查询状态，自动过滤重复提交，并在 Agent 过早终止时阻断并提示目标未达成；2) **验证器门控控制器** 仅拦截最终或询问用户的动作，在验证进度不足时拒绝终止，隔离了虚假完成的影响；3) **Workunit 控制器** 扩展至验证器背书任务，追踪单元状态，识别并修复停滞循环，将 Agent 引向待处理单元。这些外部机制通过强制执行持久性不变量，弥补了模型依赖自身记忆的脆弱性。实验显示，标准控制器在 50 标识符任务中成功率骤降，而状态追踪控制器系统性地消除了重复提交，并在高难度设定下维持了 25-78% 的成功率，证明了外部状态对定量目标持续性的关键作用。

### Q4: 论文做了哪些实验？

论文进行了两个实验。实验一（Repository-Scanning）基于requests、pytest、flask三个真实项目的36个任务实例（每个目标计数N∈{10,25,50,100}各有9个实例），评估了三种GPT模型（gpt-4.1-mini, gpt-4.1, gpt-5.4）在Native LLMPolicy、LangGraph两种代理实现和标准、验证器门控、状态追踪三种控制器下的表现。主要结果：状态追踪控制器在所有模型上均达到69%-78%的成功率，并将重复提交率降至0.000，而标准控制器成功率仅2.8%-30.6%，且随目标计数增大急剧下降。实验二（Work-Unit）使用包含公开数据和仓库派生工件的24个待办事项任务（N∈{3,5,10,20}，每目标6个待办事项），评估相同模型和控制器。结果：标准和验证器门控控制器在所有模型上均无法完成任何任务实例（成功率为0），而待办事项追踪控制器恢复了25%-50%的成功率。额外对比了Letta和LangGraph+Memory两种外部记忆基线，结果显示记忆在强模型上有效但不可靠替代专用控制器。

### Q5: 有什么可以进一步探索的点？

该工作的主要局限包括：基准测试（PushBench）覆盖范围有限（仅3个代码仓库、36个任务实例，数据操作任务也较为局限），外部记忆基线（如LangGraph+Memory）并非严格的对照消融实验，以及前沿智能体评估以牺牲控制性换取现实性。未来探索方向包括：1）扩展至更多样化的代码仓库、数据源和任务类型，以验证QGP的普适性；2）设计更精细的消融实验，解耦记忆系统、控制器组件与策略模型对持久性的贡献；3）探索无需在线验证器的方法，如利用大型语言模型自身进行进度估计或设计隐式奖励信号，使QGP适用于最终由人工评判的场景；4）结合定性评估（如推理路径分析）来补充定量指标，以捕捉因目标模糊或语义复杂导致的任务放弃。改进思路：可尝试在控制器中融入自适应阈值机制，根据历史进度动态调整重复工作过滤的严格度；或利用强化学习从验证器反馈中直接优化持久性策略，减少对人工设计的规则依赖。

### Q6: 总结一下论文的主要内容

本文研究了长程LLM代理在定量目标持久性（QGP）上的可靠性问题，即代理是否能在外部验证器确认足够多的有效工作单元前持续工作。核心贡献是提出PushBench基准，包含仓库工件收集和验证器支持的工作单元两类任务，通过直接测量重复工作、重复提交、虚假完成和进度漂移来评估QGP，而非仅依赖最终成功标志。方法上，对比了多种控制器：状态跟踪检索控制器在仓库任务中达到69-78%成功率并消除重复提交；积压跟踪控制器在标准控制器无法完成任何实例时达到25-50%成功率。黑盒前沿代理评估表明，Claude Code和Codex CLI虽能解决50工件任务，但在100工件时成功率骤降至9例中3例。主要结论为：定量目标对可靠性提出了不同于局部任务能力的要求，代理必须维持可验证的进度，并在请求工作完成前持续执行，而非仅凭表面能力提前停止。研究强调了将QGP指标纳入代理评估标准的重要性。
