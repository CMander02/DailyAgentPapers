---
title: "Claw-Eval-Live: A Live Agent Benchmark for Evolving Real-World Workflows"
authors:
  - "Chenxin Li"
  - "Zhengyang Tang"
  - "Mingxin Huang"
  - "Yunlong Lin"
  - "Shijue Huang"
  - "Shengyuan Liu"
  - "Bowen Ye"
  - "Rang Li"
  - "Lei Li"
  - "Benyou Wang"
  - "Yixuan Yuan"
date: "2026-04-30"
arxiv_id: "2604.28139"
arxiv_url: "https://arxiv.org/abs/2604.28139"
pdf_url: "https://arxiv.org/pdf/2604.28139v2"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "LLM Agent Benchmark"
  - "Workflow Agent"
  - "Live Benchmark"
  - "Agent Evaluation"
  - "Multi-System Agent"
relevance_score: 9.0
---

# Claw-Eval-Live: A Live Agent Benchmark for Evolving Real-World Workflows

## 原始摘要

LLM agents are expected to complete end-to-end units of work across software tools, business services, and local workspaces. Yet many agent benchmarks freeze a curated task set at release time and grade mainly the final response, making it difficult to evaluate agents against evolving workflow demand or verify whether a task was executed. We introduce Claw-Eval-Live, a live benchmark for workflow agents that separates a refreshable signal layer, updated across releases from public workflow-demand signals, from a reproducible, time-stamped release snapshot. Each release is constructed from public workflow-demand signals, with ClawHub Top-500 skills used in the current release, and materialized as controlled tasks with fixed fixtures, services, workspaces, and graders. For grading, Claw-Eval-Live records execution traces, audit logs, service state, and post-run workspace artifacts, using deterministic checks when evidence is sufficient and structured LLM judging only for semantic dimensions. The release contains 105 tasks spanning controlled business services and local workspace repair, and evaluates 13 frontier models under a shared public pass rule. Experiments reveal that reliable workflow automation remains far from solved: the leading model passes only 66.7% of tasks and no model reaches 70%. Failures are structured by task family and execution surface, with HR, management, and multi-system business workflows as persistent bottlenecks and local workspace repair comparatively easier but unsaturated. Leaderboard rank alone is insufficient because models with similar pass rates can diverge in overall completion, and task-level discrimination concentrates in a middle band of tasks. Claw-Eval-Live suggests that workflow-agent evaluation should be grounded twice, in fresh external demand and in verifiable agent action.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前LLM智能体基准测试面临的静态性与评估表面化问题。研究背景在于，LLM智能体正从单轮问答转向跨工具、跨服务、跨工作区的端到端工作流执行，需完成事务协调、多系统信息检索、文件修复等实际任务。然而，现有基准测试存在两大不足：一是任务集在发布时即被冻结，无法反映真实世界中不断变化的工作流需求（如工具栈演进、业务瓶颈迁移），导致基准逐渐与用户实际关心的自动化需求脱节；二是评估方式仅依赖最终回答的合理性，缺乏对智能体实际执行动作（如是否正确查询记录、修改状态、修复工件）的可验证证据，导致“听起来正确”与“真的完成工作”之间出现偏差。为此，本文提出Claw-Eval-Live，其核心是在不断更新的公共工作流需求信号中构造任务快照，并基于可执行的追踪记录、审计日志和工作空间状态进行确定性分级评估，从而将基准测试锚定于真实需求与可验证行为。

### Q2: 有哪些相关研究？

本文的相关研究可分为以下几类：

1. **Agent基准测试**：包括通用型如AgentBench、GAIA，浏览器/桌面交互型如WebArena、VisualWebArena、OSWorld，以及专业工作场所型如WorkArena、TheAgentCompany。本文与它们的区别在于不单纯强调界面真实感，而是根据公共工作流需求信号构建任务混合，并在可复现的快照中评估。

2. **代码与工作空间基准**：如ToolBench、SWE-bench、OpenHands等关注API或代码执行；在Claw生态系统中，PinchBench、Claw-Eval等评估编码或工作流。本文创新性地将服务型商业工作流与本地工作空间修复任务整合在同一个由需求信号校准的发布版本中。

3. **评估方法论**：Claw-Eval是本文最接近的先行工作，强调轨迹感知证据和混合评分。其他研究如ToolEmu关注安全性，LiveCodeBench、EvoClaw则强调基准随任务或环境老化而变化的“新鲜度”问题。本文融合了这些关注点：既用实时公共工作流信号定义“测什么”，又用可观测的执行证据定义“如何评分”。

### Q3: 论文如何解决这个问题？

Claw-Eval-Live通过一种双层基准构建方法解决了问题。核心思想是将基准分为两个层：一个可刷新的信号层和一个可复现的快照层。信号层基于公共工作流需求信号（如ClawHub Top-500技能）确定任务分布的优先级，而快照层则将这个优先级具体化为可执行的、可复现的评估任务。

具体架构分为五个阶段：
1. **信号收集**：从ClawHub Top-500快照中获取公共信号，而非人工编写任务类别。
2. **模式聚类**：将相关信号按用户目标、操作工件和执行表面聚类成稳定的工作流模式。
3. **族加权**：根据信号质量计算每个工作流族的权重，作为任务分布的优先级。
4. **种子扩展与实现**：将加权模式扩展为任务种子，并实现为包含提示、工具定义、固定装置（fixtures）和特定任务评分器的可执行候选任务。
5. **可区分性感知的发布选择**：使用混合整数线性规划（MILP）从候选池中选择公共发布子集，平衡发布规模、族覆盖率和模型的区分能力。

关键技术包括：使用确定性验证作为主要评分手段（如工具调用日志、服务审计日志、工作空间状态），仅在语义维度（如报告完整性）上使用结构化LLM评分；提供了105个跨受控商业服务和本地工作空间修复的任务；采用两种度量标准：通过率和总体完成分数。

创新点主要在于：通过公共信号驱动任务分布，保持与真实需求的对齐；通过快照固定保证可比性；通过包含完整执行过程的端到端评估而非仅最终答案来提升评估的可靠性。

### Q4: 论文做了哪些实验？

论文构建了一个包含105个任务的实时基准测试，覆盖受控商业服务与本地工作空间修复两大执行面。实验评估了13个前沿模型（包括Claude Opus 4.6、GPT-5.4、Claude Sonnet 4.6等），采用公共通过率(Pass Rate)和总体完成度(Overall Completion)作为主要指标。结果显示，领先模型Claude Opus 4.6通过率仅66.7%（总体完成度83.6），第二名GPT-5.4为63.8%（81.7），无一模型突破70%大关。实验按7个分析组（开发/终端、生产力、HR/人事、销售/CRM、财务、研究/文档、管理/运营）展示任务族级差异：开发/终端组最易（顶级模型达100%），HR/人事组最难（无模型超22.2%），生产力组差异最大（88.0%-48.0%）。执行面对比显示，本地工作空间修复任务通过率均超72.2%，而服务型流程任务最高仅59.8%。任务区分度分析表明，最具区分度的任务（如月度对账、响应时间审计）处于通过数中间区间，而终端类任务趋于天花板。资源消耗方面，GPT-5.4效率最佳（126万tokens、104分钟），Claude Opus 4.6成本最高（332万tokens、$31.61）。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要包括以下几点：首先，当前基准测试仅覆盖105个任务，且主要集中在受控商业服务和工作空间修复，缺乏对更广泛、更复杂的真实世界工作流程（如跨组织协作、动态决策）的覆盖，未来可扩展任务类型和复杂度。其次，证据对齐的评分机制虽然优于纯文本评估，但依赖确定性检查和结构化LLM评判，可能对模糊或创意性任务（如策略规划）不敏感，可探索更细粒度的自动化评估方法，如结合环境反馈的强化学习。第三，任务区分度分析显示大量任务处于“全通过”或“全失败”极端，中间区分度任务较少，未来可设计更具挑战性的中间难度任务，如多步骤推理或延迟反馈任务。此外，当前基准忽略了模型的经济成本和效率权衡，未来可引入多目标优化（如成本-准确率帕累托前沿）。最后，实时更新的“信号层”虽然保持基准时效性，但不同版本间的可比性可能受损，可建立版本对齐机制（如锚定任务集）来确保长期性能追踪的科学性。

### Q6: 总结一下论文的主要内容

Claw-Eval-Live 是一个面向工作流智能体的实时基准测试集。它解决了现有基准测试因任务集固定而无法评估智能体对演变的真实工作流需求的适应能力，以及仅凭最终答案评分而难以验证任务是否被真正执行的问题。核心贡献在于设计了一个可刷新的管道，将来自 ClawHub 的公共工作流需求信号转化为有时间戳的、可复现的基准快照。当前版本包含 105 个跨受控商业服务和本地工作区修复的任务。评估采用混合评分方法，优先使用确定性检查记录的执行痕迹、服务状态和产物，仅对语义维度使用 LLM 评判。实验结果显示，最强的模型仅通过 66.7% 的任务，没有模型达到 70%。结论表明，工作流自动化远未解决，失败模式与任务类型和执行面相关，人力资源、管理和多系统业务工作流是持续瓶颈，而本地工作区修复相对容易。该基准强调工作流智能体的评估应锚定于真实的外部需求和可验证的执行动作。
