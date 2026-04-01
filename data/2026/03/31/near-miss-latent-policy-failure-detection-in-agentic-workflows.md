---
title: "Near-Miss: Latent Policy Failure Detection in Agentic Workflows"
authors:
  - "Ella Rabinovich"
  - "David Boaz"
  - "Naama Zwerdling"
  - "Ateret Anaby-Tavor"
date: "2026-03-31"
arxiv_id: "2603.29665"
arxiv_url: "https://arxiv.org/abs/2603.29665"
pdf_url: "https://arxiv.org/pdf/2603.29665v1"
categories:
  - "cs.CL"
tags:
  - "Agent Safety & Robustness"
  - "Agent Evaluation"
  - "Tool Use"
  - "Policy Compliance"
  - "Agentic Workflows"
  - "Failure Detection"
  - "Benchmark"
relevance_score: 7.5
---

# Near-Miss: Latent Policy Failure Detection in Agentic Workflows

## 原始摘要

Agentic systems for business process automation often require compliance with policies governing conditional updates to the system state. Evaluation of policy adherence in LLM-based agentic workflows is typically performed by comparing the final system state against a predefined ground truth. While this approach detects explicit policy violations, it may overlook a more subtle class of issues in which agents bypass required policy checks, yet reach a correct outcome due to favorable circumstances. We refer to such cases as $\textit{near-misses}$ or $\textit{latent failures}$. In this work, we introduce a novel metric for detecting latent policy failures in agent conversations traces. Building on the ToolGuard framework, which converts natural-language policies into executable guard code, our method analyzes agent trajectories to determine whether agent's tool-calling decisions where sufficiently informed.
  We evaluate our approach on the $τ^2$-verified Airlines benchmark across several contemporary open and proprietary LLMs acting as agents. Our results show that latent failures occur in 8-17% of trajectories involving mutating tool calls, even when the final outcome matches the expected ground-truth state. These findings reveal a blind spot in current evaluation methodologies and highlight the need for metrics that assess not only final outcomes but also the decision process leading to them.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体在工作流中执行任务时，对业务策略的遵守情况进行评估所存在的一个关键盲点问题。

研究背景是，LLM智能体正被越来越多地部署于业务流程自动化场景中，它们需要遵循用自然语言描述的领域特定策略（如修改航班预订需验证客户资格）。目前，评估智能体是否遵守策略的主流方法是**基于参考的评估**，即将工作流的最终系统状态（如数据库状态）与预定义的“黄金标准”结果进行比对。如果最终状态一致，则认为智能体行为合规。

然而，现有方法的不足在于，它只能检测出那些导致错误最终状态的**显性策略违规**，却可能遗漏一类更微妙的问题：智能体**绕过了必要的策略检查步骤**（例如，未验证预订时间就直接同意取消），但由于用户提供的信息碰巧属实（例如，客户确实是在24小时内预订的），工作流最终仍达到了正确的状态。这种“侥幸成功”掩盖了决策过程中的缺陷。

因此，本文要解决的核心问题是：如何检测和量化这种**潜在的策略失败**（文中称为“near-miss”或“latent failure”）。即智能体在决策时未能充分获取必要信息来支撑其工具调用，但其行为因环境有利而未引发可见错误。论文提出了一种新的度量方法，通过分析智能体的对话轨迹（而非仅看最终结果），来判断其工具调用决策是否基于了充分的信息验证，从而揭示当前评估方法所忽视的这一安全与合规隐患。

### Q2: 有哪些相关研究？

相关研究主要围绕智能体工作流中的策略遵循评估展开，可归纳为以下几类：

**方法类研究**：早期研究如ToolGuard框架，通过将自然语言策略转换为可执行的守卫代码，在ReAct式工作流中监控工具调用，以检测显式策略违反。本文正是在此基础上，进一步分析智能体轨迹，以识别策略检查被绕过但结果仍正确的潜在失败（即“near-misses”）。其他方法包括基于规则或领域特定语言（DSL）的框架、基于马尔可夫逻辑网络的概率推理，以及使用Datalog派生语言的实时监控机制，这些多侧重于安全性与访问控制，而非本文关注的潜在失败检测。

**评测基准研究**：多项工作构建了评估策略遵循的基准。例如，早期研究在多领域（航空、零售、电信）模拟工作流中评估公司策略遵循；后续的τ²-verified基准修正了标注与数据库错误，提升了任务明确性，本文即采用此版本。另一研究关注多步骤单轮任务中的策略组合评估，而近期工作则针对以标准操作程序（SOP）图表示的服务策略构建客户支持智能体基准。这些研究均通过对比最终状态与预期结果来评估策略违反，但未系统检测潜在失败。

**应用类研究**：部分工作聚焦于特定场景的策略遵循，如为Terraform等基础设施即代码系统生成与验证合规规则。这类研究与本文方向相关，但领域与目标不同。

本文与上述工作的核心区别在于：现有研究主要检测显式策略违反（即最终状态错误），而本文首次系统关注“潜在失败”——即智能体绕过必要策略检查却因有利条件偶然达成正确结果的情况。本文提出的新度量方法弥补了当前评估仅重结果而忽视决策过程的盲点。

### Q3: 论文如何解决这个问题？

论文通过引入一种基于轨迹分析的“潜在失败”检测方法来解决智能体工作流中策略遵守评估的盲点问题。其核心思路是：不只看最终状态是否正确，而是检查智能体在执行关键操作（修改系统状态的操作）前，是否主动获取了必要信息以验证相关策略。

整体框架建立在ToolGuard之上。ToolGuard是一个将自然语言策略编译成可执行守卫代码的框架，包含离线编译和运行时检查两个阶段。本研究的创新在于，利用ToolGuard生成的守卫代码作为“探测器”，对已完成的智能体对话轨迹进行事后分析，以检测“侥幸成功”（Near-Miss）情况。

具体方法流程如下：
1.  **检测关键操作**：在给定的任务轨迹中，识别出所有的“变更类工具调用”（MTC），即会修改系统状态的操作（如`cancel_reservation`）。
2.  **加载并模拟守卫代码**：对于每个MTC，加载其对应的、由ToolGuard自动生成的守卫函数（GF）。该函数编码了执行此操作前必须满足的策略条件（如“预订时间在24小时内”）。
3.  **分析信息需求**：执行（模拟）该守卫函数。守卫函数的执行逻辑中，通常会调用一个或多个“只读工具”（RO，如`get_reservation_details`）来获取验证策略所需的数据。研究指出，满足同一信息需求可能存在多种等效的只读工具（例如，获取预订时间既可用`get_reservation_details`，也可用`get_reservation_timestamp`）。
4.  **历史轨迹搜索**：在MTC发生之前的对话历史中，搜索是否出现过该守卫函数实际调用的那个只读工具，**或任何其他能提供完全相同信息的等效只读工具调用**。
5.  **判定潜在失败**：如果搜索不到任何满足条件的只读工具调用记录，则判定该MTC存在“潜在失败”（即侥幸成功），因为智能体在未验证策略的情况下得出了正确结果。

关键技术包括：
*   **“侥幸成功”的形式化定义**：将一次MTC是否构成“侥幸成功”定义为一个布尔属性，其值为TRUE当且仅当在轨迹历史中找不到任何能满足其守卫函数信息需求的等效只读工具调用。
*   **等效信息获取的识别**：这是方法的核心创新点。它认识到策略验证可以通过多种数据访问途径实现，而不仅限于守卫代码中写死的那一种。为此，论文提出了两种实现历史搜索的技术：
    *   **基于LLM的搜索**：使用LLM直接分析轨迹历史，判断所需信息是否已被获取。
    *   **基于生成代码的搜索**：利用LLM生成专门的代码，来系统性地分析工具规格和轨迹，以更精确、可验证的方式完成上述搜索。实验表明后者准确率略高，因此被选为主要方法。

总之，该方法通过“回放”策略守卫代码并检查其信息需求是否在行动前被满足，创造性地将策略遵守性的评估从结果层面推进到了决策过程层面，从而能够发现那些结果正确但过程存在风险的智能体行为。

### Q4: 论文做了哪些实验？

实验基于增强版的策略执行数据集τ²-verified Airlines基准进行，该数据集包含50个多样化且贴近现实的任务，并提供了用于评估的真实状态。实验设置中，作者为弥补原始数据缺失，额外添加了get_flight_status()和get_flight_instance()两个数据访问工具。评估涉及六个当代LLM作为智能体：三个专有模型（Claude-Sonnet4、GPT5-chat、Gemini-3-pro）和三个开源模型（GPT-oss-120b、Kimi-K2.5、Qwen2.5-72b）。每个任务运行四次，总计每个智能体进行200次模拟，用户模拟器使用GPT4.1。

实验首先评估了两种对话历史搜索策略（基于生成代码和基于LLM直接搜索），用于检测潜在策略失败（near-miss）。使用Claude-Sonnet4和Kimi-K2.5作为智能体生成约400次模拟运行，并由作者人工标注真实near-miss情况用于评估。结果显示，基于Claude-Sonnet4生成代码的搜索方法达到了完美的精确度和召回率（均为1.00），因此被选为后续实验方法。

主要结果方面，评估指标包括：总失败率（未能匹配预期数据库状态）、策略违反率（由ToolGuard检测出的显式违反）、涉及突变工具调用（MTC）的轨迹数量，以及near-miss率（NMR）。关键数据如下：在涉及MTC的轨迹中，各模型的near-miss率在8.6%至17.3%之间。具体而言，GPT-oss-120b表现最佳，NMR为8.6%；Claude-Sonnet4为12.1%。值得注意的是，当仅计算涉及MTC的轨迹时，near-miss率显著高于基于全部200次模拟的计算值。此外，Qwen2.5-72b的MTC轨迹数异常高（144条），其NMR需谨慎解读。分析还发现，update_reservation_flights()是最常被无策略检查就调用的突变工具，而最常被绕过的只读工具是get_flight_status()。

### Q5: 有什么可以进一步探索的点？

该论文提出的潜在策略失败检测方法存在几个关键局限，为未来研究提供了明确方向。首先，其检测准确性高度依赖ToolGuard生成代码的质量，若LLM生成的守卫代码存在错误或遗漏，将直接影响检测结果。这提示未来可探索更鲁棒的代码生成方法，或结合形式化验证技术来确保生成逻辑的准确性。其次，当前方法仅用于离线评估而非运行时强制执行，未来可研究如何将其集成到实时代理工作流中，实现动态干预与策略修正。此外，实验仅在单一基准（航空领域）上进行，工具和策略类型有限，未来需扩展至更复杂、多元的业务场景（如金融、医疗），以验证方法的泛化能力。从计算效率看，基于LLM的变体存在额外调用开销，而生成代码方案虽降低运行时成本，却依赖部分参数化代码，这启示可探索轻量级符号推理或编译优化技术来平衡检测精度与性能。最后，当前方法主要关注工具调用决策的“知情充分性”，未来可进一步结合因果推断或反事实分析，深入探究代理决策链中的隐性偏差与风险传导机制。

### Q6: 总结一下论文的主要内容

该论文针对基于LLM的智能体工作流，提出了“近失”或“潜在策略失败”的概念，即智能体绕过了必要的策略检查，但由于有利环境仍达到了正确最终结果。传统基于最终状态的评估方法无法检测此类问题。

论文的核心贡献是提出了一种新的轨迹级评估指标，用于检测潜在策略失败。该方法基于ToolGuard框架，将自然语言策略转化为可执行的守卫代码，通过分析智能体的对话轨迹，判断其调用工具的决定是否充分基于必要的验证步骤。

主要结论显示，在τ²验证的航空公司基准测试中，即使最终状态正确，涉及状态修改工具调用的轨迹中仍有8-17%存在潜在失败。这揭示了当前评估方法的重要盲点，强调了对决策过程（而不仅是最终结果）进行评估对于可靠衡量智能体策略遵循性的必要性。
