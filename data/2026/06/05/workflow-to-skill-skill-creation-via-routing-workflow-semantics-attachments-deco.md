---
title: "Workflow-to-Skill: Skill Creation via Routing-Workflow-Semantics-Attachments Decomposition"
authors:
  - "Yuyang Zhang"
  - "Xinyuan Han"
  - "Xudong Jiang"
  - "Run Wang"
date: "2026-06-05"
arxiv_id: "2606.06893"
arxiv_url: "https://arxiv.org/abs/2606.06893"
pdf_url: "https://arxiv.org/pdf/2606.06893v1"
categories:
  - "cs.AI"
tags:
  - "Skill Creation"
  - "Agent Workflow"
  - "Agent Memory/Planning"
  - "Autonomous Agent"
  - "LLM Agent"
relevance_score: 8.5
---

# Workflow-to-Skill: Skill Creation via Routing-Workflow-Semantics-Attachments Decomposition

## 原始摘要

Large language model agents increasingly rely on Skills to encode procedural knowledge, yet high-quality Skills remain costly to hand-write. This paper studies automatic Skill construction from heterogeneous interaction evidence, including demonstrations, agent trajectories, tool traces, and execution logs. We argue that trace-to-skill construction is not simple summarization tasks, because traces are fragmented, redundant, and may miss rare but safety-critical behaviors. To address this, we introduce RWSA, a workflow-oriented intermediate representation that decomposes Skills into Workflow structure, execution Semantics, and runtime Attachments, capturing task decomposition, control flow, verification, safety, rollback, and state management. Building on RWSA, we propose W2S, a framework that segments traces, induces local Skill drafts, aligns shared structures, reconciles branches, and compresses redundancy while preserving evidence and confidence annotations. Experiments on 70 Skills show that W2S improves behavioral replay consistency by 10.5% over summarization- and prompting-based baselines, highlighting the need to treat traces as executable runtime specifications rather than compressible text.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）智能体中技能（Skill）的自动化构建问题。研究背景是，LLM智能体正从简单的文本生成系统演变为能够执行工作流、调用工具和读写状态的运行时系统，而技能作为一种可复用的能力封装和运行时规范，对于提升智能体的可靠性、可迁移性和可维护性至关重要。然而，当前的高质量技能主要依赖昂贵的手工编写，难以规模化扩展并适应变化的场景。

现有方法（如总结或提示）的不足在于，它们将轨迹到技能的构建视为简单的文本总结任务，忽视了交互轨迹的碎片化、冗余性和对关键行为（如安全、回滚）可能缺失的特点。这导致生成的技能容易过拟合偶然细节、遗漏关键前置条件或恢复流程，且难以验证和维护。

因此，本文要解决的核心问题是：如何将异构的交互证据（如演示、轨迹、工具调用日志）转化为结构化、可复用的运行时规范，而非可压缩的文本。为此，论文提出了工作流导向的中间表示RWSA，将技能分解为路由头、工作流主干、节点语义和运行时附件四个组件，并在此基础上构建了W2S框架，通过轨迹分段、草稿归纳、结构对齐和分支协调等步骤，实现自动化的、高保真的技能构建。

### Q2: 有哪些相关研究？

相关研究主要集中在基于交互轨迹的技能自动化构建领域。方法类研究包括：Agent Workflow Memory通过检索过去轨迹生成可复用工作流；Agent Skill Induction将技能表示为可执行程序以便验证；AutoSkill从交互模式中抽象出可维护技能；SkillRL在强化学习中让技能库与策略协同进化；Trace2Skill并行分析多条轨迹并提取技能。这些工作表明经验可压缩为持久化程序制品，但存在根本性的表示挑战。

本文与这些工作的核心区别在于：现有方法将轨迹视为可压缩文本，压缩为自由形式摘要或松散的教训，容易丢失激活条件、重试规则、验证检查等关键运行时结构。而本文引入RWSA中间表示，将技能分解为工作流结构、执行语义和运行时附件三部分，明确建模控制流、验证、回滚等细节。W2S框架在此基础上通过轨迹分段、局部草稿归纳、结构对齐和分支协调来重建可执行规范，而非简单压缩文本。实验证明该方法在行为回放一致性上比基线提升10.5%。

### Q3: 论文如何解决这个问题？

RWSA（Routing-Workflow-Semantics-Attachments）是论文提出的核心中间表示，它将技能分解为四个组件：路由头（激活条件）、工作流骨干（执行单元及有向边）、节点级语义（目标、决策标准、验证规则）和运行时附件（工具、资源、状态要求）。W2S框架基于这一表示，首先将异构交互证据（轨迹、演示、工具日志）转化为结构化的工作流证据EW、语义证据ES和运行时证据EA，并记录每条观测的出处（直接观测、推断、未观测）。然后，框架执行WSA重建：通过多信号分离技术（用户请求→激活条件、动作序列→工作流顺序、推理过程→决策标准、失败路径→约束），分别恢复工作流结构Ŵ（节点集N̂和边集Ê）、语义映射Ŝ（节点→目标/标准/输出）和附件Â（全局和节点级绑定）。重建后，生成阶段在三个约束下合成技能文档：指令必须可追溯至WSA证据、分支和稀有路径必须显式保留、不确定信息标记为未观测而非编造。最后，引入反馈循环进行结构检查：覆盖性检查（对比重建组件与证据，标记缺失片段）、一致性检查（检测矛盾，如要求审批却设置为无条件执行）、可执行性检查（验证步骤有序性、决策位置合理）。反馈以WSA语言表达（ΔW处理节点/边错误，ΔS处理语义错误，ΔA处理附件错误），迭代修订直至无高优先级错误或达到预算上限。创新点在于将技能生成从文本摘要任务重新定义为可执行运行时规范的恢复问题，通过结构化中间表示和证据纪律避免过度压缩和过度泛化。

### Q4: 论文做了哪些实验？

论文在RWSA框架下进行了基于回放的忠实性评估实验。实验设置使用了一个围绕WSA技能分类法构建的基准数据集，为每个参考技能提供了对应的WSA概要、工作流主干和回放场景。对比方法为Anthropic官方的技能构建流程Anthropic Skill Creator (ASC)，该方法通过结构化访谈和起草过程将交互证据转化为可复用的SKILL.md文件。主要评估指标是回放行为忠实性，即比较重建技能与参考技能在相同回放场景中的执行行为一致性，涵盖任务推进、决策结果、工具使用约束、验证要求和最终响应等维度。

在全部8种WSA技能类型上，W2S的平均得分为0.503，相比ASC的0.455提升了10.5%。具体来看，W2S在T0（0.623 vs 0.520）、T1（0.522 vs 0.407）、T2（0.760 vs 0.638）、T3（0.573 vs 0.533）、T4（0.276 vs 0.227）、T6（0.515 vs 0.450）和T7（0.652 vs 0.613）上均优于ASC，仅在T5类型上落后（0.480 vs 0.550）。T5类技能结合了工作流主干和运行时附件但缺乏显式操作语义，表明附件密集型工作流对W2S仍是主要挑战。

### Q5: 有什么可以进一步探索的点？

该论文提出的RWSA框架将技能构建从简单的文本摘要转向结构化归纳，但仍存在一些可进一步探索的方向。首先，当前方法假设所有轨迹片段都同等重要，未考虑噪声数据或错误示范的影响，未来可引入异常检测机制来过滤低质量轨迹。其次，RWSA对安全关键行为的处理仍然有限，论文虽然提及了罕见但重要的行为，但未提出具体生成验证条件的方法，可探索将运行时断言或形式化规范自动注入工作流模板中。第三，该工作对跨领域技能迁移的评估不足，未来可研究如何从不同领域的轨迹中提取共享的workflow原语（如循环、条件分支）。此外，目前的技能评估仅关注行为一致性，可引入用户研究来评估技能的可用性和可调试性。最后，将RWSA与持续学习结合，让技能库在部署中通过反馈自动更新分支和约束条件，将进一步提升实用性。

### Q6: 总结一下论文的主要内容

本文研究从异构交互痕迹（如演示、轨迹、工具调用和日志）自动构建高质量技能（Skill）的问题。作者指出，传统的痕迹到技能生成方法往往简单地将任务视为文本摘要，容易丢失关键的执行结构、安全约束和恢复流程。为此，论文提出了RWSA，一种面向工作流的中间表示，将技能分解为路由头、工作流结构、节点级语义和运行时附件四个部分，以清晰捕获任务分解、控制流、验证和安全机制。基于RWSA，作者进一步设计了W2S框架，通过分段痕迹、归纳局部技能草稿、对齐共享结构、合并分支并压缩冗余，同时保留证据和置信度标注。在70个技能上的实验表明，相比基于总结和提示的基线方法（如Anthropic Skill Creator），W2S将行为回放一致性提高了10.5%。核心贡献在于将技能生成重新定义为结构化归纳任务而非文本压缩，强调了将痕迹视为可执行运行时规约的重要性，显著提升了生成技能的可靠性、可迁移性和可维护性。
