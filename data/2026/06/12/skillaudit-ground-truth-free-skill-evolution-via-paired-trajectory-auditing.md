---
title: "SkillAudit: Ground-Truth-Free Skill Evolution via Paired Trajectory Auditing"
authors:
  - "Haowen Gao"
  - "Haoran Chen"
  - "Can Wang"
  - "Shasha Guo"
  - "Liang Pang"
  - "Zhaoyang Liu"
  - "Huawei Shen"
  - "Xueqi Cheng"
date: "2026-06-12"
arxiv_id: "2606.14239"
arxiv_url: "https://arxiv.org/abs/2606.14239"
pdf_url: "https://arxiv.org/pdf/2606.14239v1"
categories:
  - "cs.AI"
tags:
  - "技能进化"
  - "无反馈学习"
  - "成对轨迹审计"
  - "PACE评估"
  - "领域泛化"
relevance_score: 9.0
---

# SkillAudit: Ground-Truth-Free Skill Evolution via Paired Trajectory Auditing

## 原始摘要

Agent skills are structured procedural packages that guide frozen LLM agents in specialized workflows. Skills rarely remain sufficient after deployment: edge cases, API changes, and deployment constraints become visible only through use, making skill evolution a practical necessity. Existing methods depend on privileged feedback such as held-out validation scores, hidden test outcomes, or environment rewards -- signals often unavailable when a practitioner has only a task description and workspace data. We introduce SkillAudit, a framework for evolving agent skills without ground-truth feedback. The key idea is paired trajectory auditing: at each iteration, the same task is executed with and without the candidate skill, isolating how the skill changes agent behavior without external labels. To turn behavioral differences into edit guidance, SkillAudit uses Process-Aligned Contrastive Evaluation (PACE), a cluster of evaluators that maps trajectory divergences to diagnostic signals linked to specific passages in the skill document. A structural verifier, compiled once from the task specification and then fixed, checks task constraints and rolls back harmful updates. SkillAudit routes edits through two pipelines: Refine removes noisy or irrelevant guidance from broadly useful skills, while Repair replaces passages that conflict with the task. Across 89 containerized tasks spanning 8 professional domains, SkillAudit achieves 73.9% average task reward, outperforming an agent without skills (40.9%) and the static expert skill (56.7%). These gains are obtained without accessing hidden tests, reference solutions, or external scoring functions during evolution.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在缺乏外部真实反馈（ground-truth feedback）的情况下，如何让LLM智能体的技能（skill）在部署后自主演化、提升可靠性的问题。当前，智能体技能（如多文件指令包）用于指导冻结的LLM执行专业化工作流，但部署后常因边缘案例、API变化或环境约束而失效。现有技能演化方法依赖两种外部信号：一是Oracle门控方法（如SkillOpt），需要验证集分数、隐藏测试结果等；二是失败信号驱动方法（如SkillForge），需要企业知识库、交互日志或任务奖励等。但在许多实际部署场景中，从业者仅拥有任务描述和工作区数据，无法获取这些特权反馈。因此，核心问题是：如何在没有任何外部真实标签（隐藏测试、参考解、任务奖励、Oracle反馈）的条件下，自动诊断技能缺陷并生成有效更新。论文提出SkillAudit框架，通过配对轨迹审计（Paired Trajectory Auditing）——即对同一任务分别执行有技能和无技能的智能体，对比轨迹差异来剥离技能对行为的影响，从而无标签地定位技能问题，并借助结构验证器和过程对齐对比评估（PACE）实现无需真实反馈的技能演化。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要可分为以下两类：

1. **Oracle-Gated Evolution方法**：如SkillOpt和CoEvoSkills。这类方法依赖外部验证信号（如留出验证分数、隐藏测试结果或oracle通过/失败反馈）来接受或拒绝技能更新。本文与它们的核心区别在于，SkillAudit在演进过程中完全不访问这些外部真实标签信号，仅依赖任务描述和工作区数据。

2. **Failure-Signal Driven方法**：如SkillForge和SkillClaw。这类方法利用更丰富的外部监督信号，包括企业知识库、历史支持工单、跨用户交互日志或任务结果奖励。相比之下，本文的方法设定更为严格，假设实践者仅拥有任务描述和工作区数据，没有部署日志或真实评分函数。

本文提出的SkillAudit框架通过成对轨迹审计（paired trajectory auditing）——即同一任务在有/无候选技能的情况下分别执行，从而隔离技能对行为的影响——实现了无需真实反馈的技能演进。其核心创新在于结合了PACE（Process-Aligned Contrastive Evaluation）进程对齐对比评估模块和固定结构验证器，通过Refine与Repair两条编辑流水线处理不同类型的技能-任务不匹配问题。在89个容器化任务上的实验表明，该方法显著优于无技能基线（40.9%）和静态专家技能（56.7%），达到了73.9%的平均任务奖励。

### Q3: 论文如何解决这个问题？

SkillAudit通过四组件协同的闭环进化框架解决无真值反馈下的技能进化问题。核心创新是配对轨迹审计（Paired Trajectory Auditing）：每次迭代中，同一任务分别在有技能和无技能条件下并行执行，生成轨迹对(τ_w, τ_wo)，通过对比直接隔离技能对代理行为的因果效应，无需外部标签。

关键技术包括：(1) 过程对齐对比评估器集群（PACE），包含流程遵守、工件证据、一致性和效能增量四个维度的12个模板化评估器，将轨迹分歧映射为锚定到技能文档特定段落的诊断信号（如“某段落导致代理在该步骤采取错误操作”），并生成可执行的手术目标列表和受保护段落列表。(2) 锚定验证器，从任务描述一次性编译确定性检查脚本（检验文件存在性、格式合规、可重算值等），锁定后在整个进化过程中只作为硬约束边界防止回归，弥补PACE作为LLM判断的漂移风险。(3) 双管道路由机制：任务解释器预评估S₀与T的兼容性，将任务分配到精炼管道（删除噪声/冗余，保护有效段落）或修复管道（定位冲突段落并替换为无技能轨迹中的验证方案），两管道共享审计基础设施但采用不同的编辑约束门控。每次编辑由PACE手术目标引导、三路判决（skill_helped/hurt/inert）控制提交/回滚，最多迭代5次直到技能稳定。该方法在无隐藏测试、答案或环境奖励条件下，89个容器化任务上取得73.9%平均奖励。

### Q4: 论文做了哪些实验？

论文在 SkillsBench 基准测试上进行了评估，包含 89 个可运行的容器化任务，覆盖 8 个专业领域。实验设置严格分离演化和评估：演化在无访问权限的 stub 容器中运行，无法获取 pytest 验证器或任何测试内容，验证仅在演化结束后执行。对比方法包括无技能的 agent 和专家编写的静态技能。主要结果以平均任务奖励（范围 0-1）衡量，超时任务计为 0。

SkillAudit 的平均任务奖励达到 73.9%，显著高于无技能基线（40.9%）和静态技能基线（56.7%）。在 8 个领域中，SkillAudit 在 7 个领域上优于静态技能，其中软件工程提升最大（+38.5 pp，达 78.8%），金融与经济学持平（44.4%）。演化保护了 92% 的高质量初始技能（59 个任务中 54 个保持或提升），并恢复了 43% 的低质量技能（30 个中 13 个提升至通过状态）。值得注意的是，三个被技能伤害的任务（技能比无技能更差的特殊情况）全部被成功修复至奖励 1.0。

进一步分析表明，技能的可进化性主要取决于可观测性而非领域：基于可执行、可观察知识的技能（如库API使用平均 79.2%、数学方法 80.7%）进化效果好，而编码领域过程的知识（平均 69.2%）在失败任务中占 77%。

### Q5: 有什么可以进一步探索的点？

技能演化依赖的“行为差异假设”可能不完全成立——当技能修改同时改变任务执行策略时，轨迹对比可能无法区分“有效改进”与“偶然偏差”。未来可探索引入对抗性扰动测试，通过合成边缘案例验证技能修改的鲁棒性。当前PACE评估器对长链逻辑错误的检测能力有限，可设计基于程序合成或符号推理的细粒度诊断模块，将轨迹差异分解为原子操作的正确性判定。另一个方向是跨任务迁移验证：当前89个任务均为独立环境，未考虑技能在相似领域间的泛化效果。可以构建技能知识图谱，利用修改后的技能在关联任务上的表现差异作为额外对比信号。此外，结构化验证器目前仅检查任务约束，未来可扩展为动态约束库，通过因果干预学习环境规律与技能修改的关联模式。

### Q6: 总结一下论文的主要内容

SkillAudit提出了一种无需真实反馈即可进化智能体技能的方法。针对当前技能在部署后因边缘情况、API变化等而失效的问题，现有方法依赖外部验证信号（如隐藏测试集或任务奖励），不切实际。核心创新在于“配对轨迹审计”：在每次迭代中，对同一任务分别使用和不使用候选技能执行，生成轨迹对，从而隔离技能对行为的影响。为了将行为差异转化为编辑指导，该方法提出“过程对齐对比评估”（PACE），将轨迹差异映射回技能文档中的特定段落。同时，一个从任务规范编译的结构化验证器检查约束并回滚有害更新。编辑分为两个流程：Refine移除噪声，Repair替换冲突内容。在89个任务、8个专业领域的实验中，SkillAudit平均任务奖励达73.9%，远超无技能基线（40.9%）和静态专家技能（56.7%），证明了无真实反馈下技能进化的可行性和有效性。
