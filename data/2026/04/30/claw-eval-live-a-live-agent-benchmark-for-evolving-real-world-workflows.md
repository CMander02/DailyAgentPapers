---
title: "Claw-Eval-Live: A Live Agent Benchmark for Evolving Real-World Workflows"
authors:
  - "Chenxin Li"
  - "Zhengyang Tang"
  - "Huangxin Lin"
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
pdf_url: "https://arxiv.org/pdf/2604.28139v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Workflow Agent"
  - "Live Benchmark"
  - "LLM Agent Evaluation"
  - "Task Completion"
  - "Multi-step Agent"
relevance_score: 9.5
---

# Claw-Eval-Live: A Live Agent Benchmark for Evolving Real-World Workflows

## 原始摘要

LLM agents are expected to complete end-to-end units of work across software tools, business services, and local workspaces. Yet many agent benchmarks freeze a curated task set at release time and grade mainly the final response, making it difficult to evaluate agents against evolving workflow demand or verify whether a task was executed. We introduce Claw-Eval-Live, a live benchmark for workflow agents that separates a refreshable signal layer, updated across releases from public workflow-demand signals, from a reproducible, time-stamped release snapshot. Each release is constructed from public workflow-demand signals, with ClawHub Top-500 skills used in the current release, and materialized as controlled tasks with fixed fixtures, services, workspaces, and graders. For grading, Claw-Eval-Live records execution traces, audit logs, service state, and post-run workspace artifacts, using deterministic checks when evidence is sufficient and structured LLM judging only for semantic dimensions. The release contains 105 tasks spanning controlled business services and local workspace repair, and evaluates 13 frontier models under a shared public pass rule. Experiments reveal that reliable workflow automation remains far from solved: the leading model passes only 66.7% of tasks and no model reaches 70%. Failures are structured by task family and execution surface, with HR, management, and multi-system business workflows as persistent bottlenecks and local workspace repair comparatively easier but unsaturated. Leaderboard rank alone is insufficient because models with similar pass rates can diverge in overall completion, and task-level discrimination concentrates in a middle band of tasks. Claw-Eval-Live suggests that workflow-agent evaluation should be grounded twice, in fresh external demand and in verifiable agent action.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

## 本文要解决的问题

该论文聚焦于现实世界工作流场景下LLM智能体的评估问题。现有评估基准面临两大不足:一是静态发布问题,大多数基准在发布时冻结任务集,无法反映持续演变的真实工作流需求,随着工具栈和业务瓶颈的迁移,任务组合逐渐过时;二是评估粒度粗糙,许多基准主要依据最终回复评分,而非验证智能体是否实际执行了所要求的操作,导致"听起来正确"的虚假表现无法被识别。为解决这些问题,本文提出了Claw-Eval-Live实时基准。其核心创新在于:将可刷新的信号层与可复现的快照层分离,从公共工作流需求信号(如ClawHub Top-500技能)动态构建任务集;同时引入行动锚定的分级机制,通过执行轨迹、审计日志、服务状态、工作区工件等可观测证据进行评分,而非仅依赖最终文本。目标是在持续追踪需求变化的同时,实现对智能体真实工作能力的可靠评估。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：

1. **Agent基准测试**：如AgentBench、GAIA、WebArena、OSWorld等，测试通用或浏览器/桌面交互能力；专业工作场景基准如WorkArena、TheAgentCompany。本文不同之处在于不强调界面真实感，而是基于公开需求信号构建工作流组合，并在可复现的快照中评估。

2. **代码与工作区Agent基准**：包括API-Bank、ToolBench等聚焦工具操作，以及SWE-bench、OpenHands等侧重代码仓库或命令行执行。在OpenClaw生态中，PinchBench、ClawBench等评估编码、沙箱或工作流场景。本文区别在于将服务驱动的业务工作流与本地工作区修复统一到一个基于信号校准的版本中。

3. **评估方法论**：Claw-Eval是本文最接近的方法学近亲，强调轨迹感知证据、混合评分和多维评估。其他工作如ToolEmu、Agent-SafetyBench关注风险安全，LiveCodeBench、EvoClaw等关注基准时效性。本文结合了这些关注点，既通过实时公开工作流信号确定测量内容，又通过可观察执行证据确定评分方式。

### Q3: 论文如何解决这个问题？

论文通过构建一个可刷新的动态基准来解决问题。核心方法是提出Claw-Eval-Live框架，将基准的构建分为时间变化的信号层和固定的发布层。信号层从公开的ClawHub Top-500技能排名（按下载量和流行度排序）中获取现行工作流需求信号，作为任务分布的先验知识。发布层则将信号转化为可复现的快照，包含105个固定任务、夹具和评分器。

整体架构包括五个概念阶段：信号采集、模式聚类、家族权重计算、种子扩展与实现、以及区分度感知的公开发布选择。关键技术涉及混合整数线性规划（MILP）用于优化发布集的选择，通过最大化任务在候选模型间的排序一致性来保证区分度。每个任务都是完整的可执行单元，包括YAML定义、夹具、工具模式和专用评分器。

主要创新点包括：1）分离信号层与快照层，支持基准随工作流需求演变而刷新；2）基于公开需求信号而非作者主观分类构建任务分布；3）通过确定性检查（如审计日志）和结构化LLM评判相结合的方式进行验证；4）评估整个工作流轨迹而非仅最终答案。实验表明，领先模型仅通过66.7%的任务，HR、管理和多系统业务流程是持续瓶颈。

### Q4: 论文做了哪些实验？

该论文《Claw-Eval-Live》构建了一个动态的工作流智能体基准测试，并在发布版本中进行了全面的实验评估。实验设置了105个任务，涵盖受控商业服务和本地工作空间修复两大执行面，包括开发/终端、生产力、人力资源、销售/客户关系管理、财务、研究/文档和管理/运营等7个分析族。评估了13个前沿模型，采用严格的公共通过率规则，并结合确定性检查与结构化LLM评判。主要结果显示，领先模型Claude Opus 4.6的通过率仅为66.7%，总体完成度83.6；GPT-5.4紧随其后，通过率63.8%，完成度81.7。没有任何模型通过率达到70%。任务族表现差异显著：开发/终端任务接近饱和（最强模型达100%），而人力资源管理任务极其困难（所有模型通过率低于22.2%，多个为0），生产力族分化最大（从88.0%到48.0%）。在执行面层面，所有模型在本地工作空间修复上的通过率均超过72.2%，但服务型工作流最高仅59.8%。任务辨别力分析表明，高区分度任务（如电商月度对账、首次响应时间审计、多文档合并）集中于中等通过率区间，而极端任务（全通过或全失败）辨别力较低。效率分析显示，GPT-5.4在顶级模型中效率最佳（126万token，104分钟，6.27美元），而准确率最高的Claude Opus 4.6成本显著更高。

### Q5: 有什么可以进一步探索的点？

基于Claw-Eval-Live的局限性和研究空白，未来可从三方面深入探索。第一，**任务构造的生态扩展**：当前基准依赖ClawHub Top-500技能，但真实世界工作流的长尾需求未被覆盖。可引入动态种子任务生成机制，结合用户论坛、工单系统等低频但高价值的信号源，使任务库更贴近真实使用场景。第二，**评估粒度的深化**：目前采用“是否通过”的二值化评分，但未区分部分完成、错误纠偏等中间状态。设计分级成功率指标和基于执行轨迹的细化失误归因（如工具调用失败、逻辑分叉），可更精准刻画模型能力短板。第三，**对抗性鲁棒性测试**：论文表明基于LLM的判分仍用于语义维度，未来可构造“诱骗性工作流”测试——即设计多步交互中单步语义正确但累积逻辑错误的场景，专门探测LLM judge的盲区。此外，当前模型在跨系统协作任务上持续失败，提示可能需要预训练阶段引入结构化API操作序列或使用流程记忆增强的微调策略。

### Q6: 总结一下论文的主要内容

Claw-Eval-Live是一个为工作流智能体设计的新型实时基准，旨在解决现有基准任务集固化、难以评估动态工作流需求和任务执行验证的问题。其核心贡献在于设计了一个可更新的信号层（基于ClawHub Top-500技能）与可复现的时间戳版本快照。该基准通过记录执行轨迹、审计日志、服务状态等实现确定性检查，仅在语义维度使用结构化LLM评判。当前版本包含105个任务，涵盖商业服务和本地工作空间修复，评估了13个前沿模型。主要结论显示，领先模型仅通过66.7%的任务，无模型达到70%，表明可靠的工作流自动化远未解决；HR、管理和多系统协调是持续瓶颈，而本地工作空间修复相对容易但未饱和。该基准强调，工作流智能体评估应双重锚定于实时外部需求和可验证的智能体行为，而非仅依赖最终答案的可信度。
