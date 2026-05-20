---
title: "STAR-PólyaMath: Multi-Agent Reasoning under Persistent Meta-Strategic Supervision"
authors:
  - "Jiaao Wu"
  - "Xian Zhang"
  - "Hanzhang Liu"
  - "Sophia Zhang"
  - "Fan Yang"
  - "Yinpeng Dong"
date: "2026-05-19"
arxiv_id: "2605.19338"
arxiv_url: "https://arxiv.org/abs/2605.19338"
pdf_url: "https://arxiv.org/pdf/2605.19338v1"
github_url: "https://github.com/Julius-Woo/STAR-PolyaMath"
categories:
  - "cs.MA"
  - "cs.AI"
  - "cs.CL"
tags:
  - "多智能体系统"
  - "数学推理"
  - "元策略监督"
  - "状态机架构"
  - "长程推理"
  - "基准测试"
relevance_score: 9.0
---

# STAR-PólyaMath: Multi-Agent Reasoning under Persistent Meta-Strategic Supervision

## 原始摘要

Frontier AI models and multi-agent systems have led to significant improvements in mathematical reasoning. However, for problems requiring extended, long-horizon reasoning, existing systems continue to suffer from fundamental reliability issues: hallucination accumulation, memory fragmentation, and imbalanced reasoning-tool trade-offs. In this paper, we introduce STAR-PólyaMath, a multi-agent framework that systematically addresses these challenges through meta-level supervision and structured Reasoner-Verifier interaction. STAR-PólyaMath is structured as an orchestrated state machine with nested challenge-step-replan loops, governed by a reasoning-free Python orchestrator that separates control from inference and bounds error propagation through trace-back and re-planning. Our key innovation is a persistent Meta-Strategist that maintains cross-attempt memory and exercises meta-level control by issuing high-level strategic guidance or mandatory directives, so the system can escape unproductive loops rather than stagnate or over-rely on tools. STAR-PólyaMath achieves state-of-the-art results on all eight top-tier competition benchmarks: AIME 2025-2026, MathArena Apex Shortlist, MathArena Apex 2025, Putnam 2025, IMO 2025, HMMT February 2026, and USAMO 2026. It obtains perfect scores on AIMEs, Putnam, and HMMT, and shows its largest margin on Apex 2025, scoring 93.75% compared with 80.21% by the strongest baseline GPT-5.5. Ablation studies show that the gains arise from the framework's orchestration rather than from model-level diversity since removing key components or substituting in mixed backbones consistently weakens performance. Code is available at https://github.com/Julius-Woo/STAR-PolyaMath.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长链条数学推理中现有AI系统面临的三个核心可靠性问题：幻觉积累、记忆碎片化以及推理与工具使用的失衡。当前，前沿AI模型与多智能体系统虽在数学推理上取得显著进展，但对于需要长时间、多步骤推理的复杂问题，现有方法仍存在根本性缺陷。例如，自由形式的推理难以验证，导致错误在长解答轨迹中逐级传播并产生自信但错误的论证（幻觉积累）；多次尝试后难以保留关键信息，导致重复无效探索（记忆碎片化）；过度依赖代码执行等工具会掩盖数学结构，并产生系统性偏差（推理-工具权衡失衡）。

为应对这些挑战，本文提出了STAR-PólyaMath框架，其核心创新在于引入一个持久的**元策略师（Meta-Strategist）**角色。该角色通过维护跨尝试的记忆并行使元级控制，在系统陷入无产出循环时发出高级策略指导或强制指令，从而引导问题解决过程。整个系统由无推理能力的Python编排器组织为状态机，包含嵌套的挑战-步骤-重规划循环，以限制错误传播。最终目标是通过这种结构化管理和元级监督，克服现有方法在长时推理中的根本性不可靠问题。

### Q2: 有哪些相关研究？

相关研究可分为以下类别：

**1. 数学推理方法类**：与本文最相关的工作包括链式思维提示（CoT）、自我一致性、程序辅助方法（如PAL、ToRA）以及代码自验证（CSV）。这些方法侧重于通过提示工程或代码执行提升单模型推理能力。本文的区别在于采用**多智能体架构**，通过专业角色分工和持久记忆实现元策略监督，而非依赖单一模型的自我修正。

**2. 多智能体推理系统类**：相关工作包括基于辩论的方法、CAMEL、AutoGen、MACM、MALT（生成器-验证器-精炼器管道）和ReMA（层次化元推理）。这些系统通常将控制逻辑嵌入推理智能体内部，且在会话间重置上下文。本文的创新点是**控制与推理分离**：使用无推理的Python编排器控制流程，并引入持久元策略师，负责跨尝试记忆和元级监督，从而避免系统陷入无意义循环。

**3. 自我修正与验证类**：自我精炼等迭代方法存在根本局限——犯错模型难以自检错误。本文通过**结构化辩论协议**解决该问题：验证器对推理者的主张进行分类评估（代码结果、可核查声明、纯数学论证），并保持完整的会话连续性。

**4. 竞赛数学应用类**：AlphaGeometry、AlphaProof、FunSearch分别针对几何证明、形式定理证明和数学发现。本文的独特之处在于**覆盖所有竞赛数学题型**（不限于几何），并通过基于辩论的验证与持久元认知监督实现整体最优。

### Q3: 论文如何解决这个问题？

STAR-PólyaMath通过一个由Python编排器（Orchestrator）协调的多智能体框架来解决长链条数学推理中的核心问题。该框架设计为嵌套了“挑战-步骤-重规划”循环的有限状态机，核心创新在于一个持久的元策略师（Meta-Strategist）。**整体框架**通过控制流与推理过程解耦来实现，Python编排器掌控所有控制流，管理智能体间的交互、状态机推进和决策解析，从而将错误传播限制在局部。

**主要模块**包括四个专门智能体：1) **推理者（Reasoner）**：主问题求解者，负责探索、制定计划、执行步骤并撰写最终解法，但其输出需经严格验证。2) **验证者（Verifier）**：严格的评审，对推理者的每一步输出给出接受、挑战、回溯或提议重规划四种判决，并通过结构化辩论协议允许推理者回应挑战。3) **元策略师（Meta-Strategist）**：关键创新点，是唯一拥有持久会话的智能体。它维护跨尝试的记忆，在决策点提供元策略指导，或在系统陷入低效循环时下达强制指令（如切换至纯推理模式），并能基于历史失败模式做出重规划或中止的最终决策。4) **Python编排器**：作为控制核心，解析智能体输出并执行确定性决策（前进/回溯/重规划/中止）。

**关键技术**包括：通过显式的**步骤分解与计划**来缓解幻觉累积；通过**分层验证标签**（verified、easy-verify、hard-verify）实现推理与工具使用的平衡；通过**挑战循环**和**回溯机制**（回溯至步骤M，归档后续内容并重置推理者会话）实现早期错误检测与阻断传播；通过**元策略师的重规划决策**（统一裁决Continue、Trace-Back、Approve-Replan、Abort）防止系统在已失败方向上重复尝试。此外，**探索阶段**允许在正式规划前进行低承诺调查，并通过**纯推理模式**等元认知干预直接应对工具使用失效的情况。这些设计协同作用，有效解决了幻觉累积、记忆碎片化和推理-工具权衡三大挑战，在多个顶级竞赛基准上取得了完美或领先的成绩。

### Q4: 论文做了哪些实验？

论文在八个顶级数学竞赛基准上进行了全面实验，包括AIME 2025/2026（30题，整数答案）、Putnam 2025（12题，证明评分0/0.5/1）、IMO 2025和USAMO 2026（每题0-7分制）、HMMT February 2026（33题）、MathArena Apex 2025（12题）及Apex Shortlist（48题）。对比基线包括GPT-5.5、GPT-5.4、Gemini 3.1 Pro、Claude Opus 4.7等闭源模型与DeepSeek-v4-Pro等开源模型。主实验结果：STAR-PólyaMath在AIME 2025/2026、Putnam 2025、HMMT 2026上取得100%满分；在Apex Shortlist达94.27%，Apex 2025达93.75%（最强基线GPT-5.5仅80.21%），IMO 2025达88.69%，USAMO 2026达99.40%。消融实验显示：移除回溯和重规划机制导致证明基准准确率骤降（如Putnam从91.67%降至37.50%）；移除元策略师使IMO从75%降至33.33%；探索阶段主要影响推理时间而非准确率。骨干网络替换实验证实，使用GPT-5.5统一配置优于混合模型，证明框架收益来自结构化编排而非模型多样性。

### Q5: 有什么可以进一步探索的点？

该工作的核心局限在于计算成本、验证可靠性和基准饱和三方面。未来可探索的方向包括：1) 优化推理效率，通过动态资源分配或轻量级路由策略降低成本，使其适用于延迟敏感场景；2) 引入神经符号验证器（如Lean），将自然语言验证升级为形式化证明，从而消除幻觉积累和模糊判断；3) 拓展至开放研究级数学问题，此类问题无封闭答案且需持续数日的新颖推理，可测试框架的长期记忆与元策略适应能力。此外，当前元策略主要依赖回溯和重规划，可尝试结合强化学习或贝叶斯优化来自动搜索更优的高层策略，进一步提升跨尝试记忆的利用效率。基准饱和也提示需设计更细粒度的难度分层评估，避免天花板效应。

### Q6: 总结一下论文的主要内容

STAR-PólyaMath提出了一个多智能体推理框架，用于解决长程数学推理中的三大核心问题：幻觉累积、记忆碎片化以及推理与工具使用的不平衡。方法上，它将系统构建为一种编排状态机，包含嵌套的问题-步骤-重规划循环，由无推理的Python编排器控制，将控制与推理分离，并通过回溯和重规划限制错误传播。其关键创新在于一个持久的元策略师，该模块维护跨尝试的记忆，通过发布高层战略指导或强制指令实现元级控制，从而帮助系统跳出无效循环，避免过度依赖工具或陷入停滞。在AIME 2025-2026、MathArena Apex Shortlist、Putnam 2025等八个顶级竞赛基准上，该方法取得了最优结果，并在AIME、Putnam和HMMT上获得满分。消融实验证实，性能提升源于框架编排而非模型多样性。这项工作的意义在于为需要持续监控和结构化交互的长时域推理任务提供了一种可靠范式。
