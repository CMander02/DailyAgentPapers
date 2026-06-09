---
title: "SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History"
authors:
  - "Zhiwei Li"
  - "Yong Hu"
date: "2026-06-07"
arxiv_id: "2606.08671"
arxiv_url: "https://arxiv.org/abs/2606.08671"
pdf_url: "https://arxiv.org/pdf/2606.08671v1"
categories:
  - "cs.LG"
tags:
  - "Agent Skill Evolution"
  - "Persistent Decision History"
  - "Continual Learning"
  - "Multi-Agent Collaboration"
  - "Web Agent"
  - "Deep Research Agent"
  - "Skill Refinement"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History

## 原始摘要

Agent skills extend language-model agents with task-specific procedures, scripts, and references, but the tasks and environments they target continually change. Existing methods improve skills in bounded runs and retain only the final artifact, discarding the decision history that later agents need to interpret prior revisions, evaluations, and rejected alternatives. We introduce SkillHone, a harness for continual agent skill evolution grounded in persistent decision history. SkillHone pairs skill revisions with evaluation-side evidence that supplies practice feedback, recording structured histories of diagnoses, revisions, evidence, and outcomes. Role-separated subagents run candidate skills on practice probes with redacted reporting and propose revisions informed by prior decisions, enabling cross-session refinement without rediscovering past rationale. We evaluate SkillHone on deep-research benchmarks in a raw open-web setting, where agents are not given an integrated search stack and must organize retrieval through portable skills. We compare against a deep-research agent backed by commercial retrieval services. With Qwen3.6-35B-A3B as the evaluation-time backbone, the resulting skills outperform the deep-research agent by 15.8 points on GAIA and 3.2 points on WebWalkerQA-EN, while also exceeding prior skill-evolution methods.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体技能进化过程中“决策历史丢失”的问题。研究背景是，基于大语言模型的智能体通过“技能”（即特定任务的程序、脚本和参考的封装）来扩展能力，但所面对的任务和环境持续变化，需要技能不断演进。现有方法（如基于合成的Skill-Creator和基于反射优化的GEPA方法）存在一个核心不足：它们将技能改进视为一个有边界的运行过程，只保留最终优化后的技能工件，而丢弃了整个决策历史。当后续的智能体会话继承这一技能时，它无法获取诸如“为什么做此修改”、“哪些替代方案被否决”、“评估证据是什么以及为何被接受”等关键上下文信息。这导致后续的优化可能重复之前的修复、撤销有用的改动，或在丢失背景的反馈上继续优化，即无法实现真正的持续维护。因此，本文要解决的核心问题就是：如何建立一种机制，在技能进化的整个生命周期中持久化记录包括诊断、修订、评估证据和结果在内的完整决策历史，使得后续智能体能够基于前序决策进行跨会话的持续优化，而无需从头推导。为此，论文提出了SkillHone框架。

### Q2: 有哪些相关研究？

相关研究主要分为三个方向。首先，关于Agent技能获取与技能习得的研究（如基于探索的自动化发现、强化学习演化），这些工作聚焦于如何从零开始获取或生成新技能并提升任务性能。而SkillHone则关注在技能已存在并投入运行后，如何持续维护和优化它，而非单纯地创造新技能。其次，针对提示词、系统及技能的优化工作（如DSPy的声明式编译、GEPA的反思式演化、Hermes-SE对技能和代码的优化）提供了在单次优化轮次内改进产物的强有力机制。SkillHone的不同在于将技能演化视为持续维护过程，后续智能体不仅继承最新产物，还继承了包含失败、候选修订和评估结果的结构化历史。最后，多智能体协作与开发工作流（如MetaGPT的角色分工）启发了角色分离原则。但SkillHone将角色分离用于持续的技能维护，而非一次性产物生成，通过权限区分优化子智能体和评估子智能体来积累可读的决策历史并减少评估资产向优化侧的泄露。

### Q3: 论文如何解决这个问题？

SkillHone提出一种基于持久决策历史的持续技能演化框架。核心设计包括两个隔离的仓库：技能仓库存储正在修订的技能包，技能评估仓库保存练习探针、验证器、轨迹和脱敏报告。整体架构采用角色分离的双边子代理系统：优化侧子代理负责诊断失败、提出修订、审查更改并记录结果，可操作技能仓库但无法访问未脱敏的评估目标；评估侧子代理则运行候选技能、生成脱敏反馈，可查看完整数据但无权修改技能仓库。运行时调度器作为消息路由器，动态调度新鲜子代理并路由证据，确保两侧间安全隔离。

关键技术在于持久决策历史的构建。每次开发步骤记录为一个四元组决策记录h_t=(诊断q_t,候选修订r_t,脱敏证据e_t,结果o_t)，累积形成结构化历史H_t。这不同于简单的版本差异，而是将文件变化与其解决的问题、评估证据和最终决策关联起来。当环境变化时，后续子代理可通过检查历史记录判断失败是否为新的、类似修复是否已尝试过、以及先前替代方案被拒绝的原因，从而避免重复推导相同诊断。

创新点包括：1) 优化侧与评估侧权限分离，防止实践反馈成为直接记忆目标；2) 决策历史作为演化过程本身的持久记忆，支持跨会话持续改进；3) 随机化探针报告机制隐藏进度，维护真实的自我评估。在无集成搜索栈的原始开放网络环境下，该框架使基于Qwen3.6-35B-A3B的代理在GAIA和WebWalkerQA-EN上分别超越商业深度研究代理15.8和3.2个百分点，并显著优于先前技能演化方法。

### Q4: 论文做了哪些实验？

论文在GAIA和WebWalkerQA-EN两个开放域深度研究基准上评估了SkillHone。实验设置分为两种情况：使用商业检索服务的精选搜索设置，以及无预集成搜索工具的原始开放网络设置。后一种设置中，所有系统共享同一初始技能池（来自ClawHub和SkillHub），比较了四种方法：直接使用现有技能（Existing-Skills）、内置迭代优化的Skill-Creator、反思式优化的Hermes-SE，以及本文提出的SkillHone。开发控制器使用Claude Opus 4.6，执行和评估骨干使用Qwen3.6-35B-A3B。主要结果：在GAIA上，SkillHone平均准确率64.6%，超过精选搜索设置的深度研究agent（48.8%）15.8个百分点，在L2级别提升最显著（66.7% vs 47.0%）。在WebWalkerQA-EN上，SkillHone平均66.4%，超过深度研究agent（63.2%）3.2个百分点，Hard级别表现突出（68.4% vs 67.1%）。在原始开放网络同源比较中，SkillHone比Skill-Creator在GAIA和WebWalkerQA-EN上分别提升20.5和28.3个百分点，比Hermes-SE分别提升14.2和13.4个百分点。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于实验仅基于英文基准，且只针对单一技能的独立演化。未来研究可以从两个方向深入：一是扩展到多语言环境，测试SkillHone对非英语任务与提示的适应能力，并探索语言差异如何影响决策历史的跨会话迁移；二是实现多技能的协同演化——现实中Agent常需同时调用多个相关技能（如信息检索与信源验证），如何设计角色分离的子体以管理技能间的依赖关系和冲突策略，将是一个重要的技术挑战。此外，当前方法依赖预定义的评价探针，未来可尝试让子体自动生成探针或引入在线环境反馈，从而减少人工干预。另一个改进思路是结合元学习，让Agent从历史修订模式中学习“如何高效修改技能”，从而加速收敛。

### Q6: 总结一下论文的主要内容

SkillHone提出了一种用于智能体持续技能演化的框架，解决了现有方法在有限运行中仅保留最终技能而丢弃决策历史的问题。该方法通过记录诊断、修订、证据和结果的持久决策历史，并采用角色分离的子智能体在实践探针上运行候选技能并基于先前决策提出修订，实现了跨会话的持续优化。在原始开放网络环境下的深度研究基准测试中，SkillHone开发的技能无需预集成搜索工具，以Qwen3.6-35B-A3B为评估骨干，在GAIA和WebWalkerQA-EN上分别超越商业检索服务的深度研究智能体15.8和3.2个百分点，同时优于先前的技能演化方法。主要结论表明，持久决策历史帮助智能体将实践反馈转化为更强的技能集合，为智能体技能的持续进化提供了有效范式。
