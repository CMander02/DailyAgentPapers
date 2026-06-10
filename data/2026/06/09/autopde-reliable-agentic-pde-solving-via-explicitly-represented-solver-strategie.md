---
title: "AutoPDE: Reliable Agentic PDE Solving via Explicitly Represented Solver Strategies"
authors:
  - "Huanshuo Dong"
  - "Keyao Zhang"
  - "Hong Wang"
  - "Zhezheng Hao"
  - "Zhiwei Zhuang"
  - "Ziyan Liu"
  - "Jiacong Wang"
  - "Gengyuan Liu"
  - "Xin Jin"
date: "2026-06-09"
arxiv_id: "2606.10752"
arxiv_url: "https://arxiv.org/abs/2606.10752"
pdf_url: "https://arxiv.org/pdf/2606.10752v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "代码Agent"
  - "偏微分方程数值求解"
  - "Agent框架"
  - "自适应求解"
relevance_score: 8.5
---

# AutoPDE: Reliable Agentic PDE Solving via Explicitly Represented Solver Strategies

## 原始摘要

Numerical solvers for partial differential equations (PDEs) are core computational tools in science and engineering. Building reliable PDE solvers requires not only executable code, but a numerical solver strategy, a set of decisions about discretization, stabilization, solver configuration, and resolution control, that matches the PDE structure. Recent LLM-based coding agents have begun to reduce the programming burden by generating and debugging solver implementations. However, they typically move directly from a PDE problem to solver code, leaving the solver strategy implicit in implementation details. Feedback from a failed solve is therefore routed back to code edits rather than to the underlying strategy, so numerical decisions remain hard to check before code is generated and hard to revise using numerical evidence when it fails. To address this limitation, we propose AutoPDE, a code agent that maintains the solver strategy as an explicitly represented object throughout the solving process: an independent, inspectable object that is built before any code is written and can be revised, using numerical evidence, whenever a solve fails. AutoPDE builds and maintains this object in three stages, all drawing from a library of reusable PDE-solving skills: PDE analysis identifies the equation type and algebraic structure; numerical method selection chooses a numerical method that matches the analysis result and commits to a discretization, stabilization, and linear solver accordingly; and adaptive tuning runs low-cost pilot solves to calibrate resolution and tolerances under the prescribed accuracy and runtime budget. We evaluate AutoPDE on the PDE Agent Bench, where experimental results show that AutoPDE achieves a pass rate of $54.5%$, improving over the strongest baseline by $14.2$ percentage points.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前基于LLM的编码代理在构建偏微分方程数值求解器时，由于缺乏显式的求解策略而导致的可靠性不足问题。研究背景是，数值求解器是科学工程仿真的核心工具，其构建关键在于设计匹配PDE结构的求解策略，包括离散化、稳定化、求解器配置和分辨率控制等数值决策。现有方法如SWE-agent、CodePDE等LLM编码代理虽然能自动生成和调试代码，但它们直接从PDE问题跳到代码实现，求解策略隐含在代码细节中而不可见。当求解失败时，反馈只能用于代码编辑，无法直接修正底层的数值决策。例如，将共轭梯度法用于不定亥姆霍兹系统，或在高对流占优问题中忽略SUPG稳定化，这类策略级错误难以通过局部代码修补修复。因此，本文提出AutoPDE，核心思路是将求解策略作为一个显式的、可审计的对象，在代码生成之前先构建该策略，并在求解失败时利用数值证据对其进行定向修订，从而恢复传统数值实践中专家先制定策略再实现的反馈循环，同时保持全流程自动化。

### Q2: 有哪些相关研究？

**方法类相关研究：**

- **CodePDE** 研究了重复采样、自调试、改进和测试时扩展的代码生成方法；**PDE-SHARP** 采用分阶段数学分析与求解器合成；**AutoNumerics** 结合了多智能体设计、实现和基于残差的验证；**PDE-Controller** 将自然语言指令映射为形式化PDE控制任务。

  这些工作虽然展示了LLM驱动求解器生成的潜力，但求解策略仍是生成代码的隐性副产品，而AutoPDE将其作为独立表示对象，在代码生成前构建并基于数值证据进行修订。

**应用类相关研究：**

- **FEniCS、Firedrake、deal.II** 等经典PDE软件将数值流程暴露为显式选择（离散化空间、稳定化方案、Krylov求解器与预条件器、自适应控制）。

  AutoPDE将这种人工策划的工作流提升为智能体化设置，使得求解策略成为从可复用数值方法技能库构建的显式、可修订的工件。

**评测类与系统类相关研究：**

- **SWE-agent、OpenHands、MetaGPT** 等LLM编码智能体能交互执行、调试和编辑代码，但未显式表示耦合的PDE决策。

  AutoPDE继承了交互式智能体范式，同时增加了PDE特定策略表示和技能库，在PDE Agent Bench上取得了54.5%的通过率，比最强基线提升14.2个百分点。

### Q3: 论文如何解决这个问题？

AutoPDE通过显式维护求解器策略对象来解决隐式策略难以检查和修正的问题，核心方法是一个三阶段管道。整体架构基于mini-swe-agent，并扩展了策略卡片协议和两个专用工具。

第一阶段为PDE分析，系统提示代理检查输入规格，识别方程族、线性性、时间依赖性、边界条件等，生成DIAGNOSIS卡片，区分对流主导、扩散主导问题及代数系统类型（如SPD或鞍点系统）。第二阶段为数值方法选择，代理根据DIAGNOSIS卡片调用get_pde_skill工具，从覆盖十种方程族的技能库中检索结构化文本指南（非代码），然后生成METHOD卡片，明确选择离散化方法（如Taylor-Hood P2-P1单元）、稳定化方案（如SUPG）、代数求解器和预处理器。第三阶段为自适应调优，代码生成后，代理执行规则驱动的剖析指南，运行试算并测量误差和时间，若误差过高则细化网格或提升多项式阶数，若运行时过长则简化求解或调整容差，通过迭代修正直至满足目标或无法进一步改进。

AutoPDE的三大创新点在于：1) 将求解器策略作为显式、可检查的对象，在写代码前构建并可在失败时基于数值证据修订；2) 引入可重用的PDE求解技能库，提供结构化文本指南而非代码；3) 采用基于规则的试算调优，自适应校准分辨率和容差。

### Q4: 论文做了哪些实验？

论文在PDE Agent Bench上评估了AutoPDE，该基准包含8个方程族（热传导、对流扩散、斯托克斯、纳维-斯托克斯、亥姆霍兹、双调和、线弹性、反应扩散）共191个案例，每个案例指定了精度和运行时间预算。主要指标是端到端通过率，要求求解器成功执行、相对L2误差低于目标误差且运行时间低于目标时间。

对比方法包括三类：(i) 朴素LLM（单次生成，无工具使用），涵盖DeepSeek V3.2、Gemini 2.5 Pro、GPT 5.1和Claude Opus 4.6四种骨干；(ii) 通用编码Agent（mini-swe-agent、OpenHands）；(iii) PDE专用Agent（CodePDE）。所有Agent基线均在Claude Opus 4.6和GPT 5.1上运行以隔离骨干影响。

主要结果：AutoPDE在两种骨干上均达到54.5%的总体通过率，领先最强基线OpenHands（GPT 5.1，40.3%）14.2个百分点，超越Claude上最佳基线CodePDE（31.9%）22.6个百分点。AutoPDE是唯一在所有方程族上都保持非零通过率的方法（最低22.2%），尤其在需要对流扩散等需要复杂数值决策的族上表现突出（GPT 5.1上达60.0%和59.5%）。消融实验在107个案例子集上（对流扩散、斯托克斯、纳维-斯托克斯、亥姆霍兹）表明，各阶段均贡献正向增益：移除PDE技能阶段导致最大下降（34.6个百分点），移除自适应调优和诊断阶段分别下降11.2和9.3个百分点。

### Q5: 有什么可以进一步探索的点？

尽管AutoPDE在显式策略表示上取得了显著进步，但54.5%的通过率表明仍有大量PDE难以被可靠求解。首先，其策略库的覆盖范围有限，特别是对高度非线性、多物理场耦合或具有奇异性的PDE（如流体湍流、等离子体物理方程）缺乏成熟的数值方案模板，未来可系统化扩充可复用技能库，引入领域专家知识。其次，当前自适应调优仅基于低代价预跑，对计算预算与精度的权衡是静态的，可探索在线贝叶斯优化的动态资源分配方法。第三，策略修正依赖“失败”信号，缺乏更细粒度的数值证据（如残差震荡、稳定性判据）诊断具体数值问题，可结合物理信息引导的分层回溯机制。最后，未考虑硬件感知的强可扩展性，对于大规模PDE求解，尚需将分布式并行策略纳入显式决策空间。

### Q6: 总结一下论文的主要内容

AutoPDE提出了一种基于显式求解策略的偏微分方程(PDE)求解代理。传统LLM代码代理直接从PDE问题生成求解器代码，将求解策略隐式嵌入实现细节中，导致失败反馈只能用于代码修补而无法从根本上修正数值决策错误。AutoPDE将求解策略构建为独立的、可检查的对象，该对象在代码生成前建立，并可通过数值证据进行修订。其方法分为三个阶段：PDE分析识别方程类型和代数结构；数值方法选择匹配分析结果并确定离散化、稳定化和线性求解器配置；自适应调优通过低成本试算校准分辨率和容差。在PDE Agent Bench上，AutoPDE达到54.5%的通过率，比最强基线高出14.2个百分点。该工作的核心贡献在于恢复了人类专家式的“策略-反馈”循环，使得数值决策在求解过程中保持可见、可查和可修订，显著提升了PDE求解的可靠性。
