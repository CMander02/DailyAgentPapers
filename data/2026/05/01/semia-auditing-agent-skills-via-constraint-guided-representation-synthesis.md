---
title: "Semia: Auditing Agent Skills via Constraint-Guided Representation Synthesis"
authors:
  - "Hongbo Wen"
  - "Ying Li"
  - "Hanzhi Liu"
  - "Chaofan Shou"
  - "Yanju Chen"
  - "Yuan Tian"
  - "Yu Feng"
date: "2026-05-01"
arxiv_id: "2605.00314"
arxiv_url: "https://arxiv.org/abs/2605.00314"
pdf_url: "https://arxiv.org/pdf/2605.00314v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.PL"
tags:
  - "Agent安全审计"
  - "Agent技能形式化验证"
  - "LLM驱动Agent安全"
  - "静态分析"
  - "Datalog"
relevance_score: 9.5
---

# Semia: Auditing Agent Skills via Constraint-Guided Representation Synthesis

## 原始摘要

An agent skill is a configuration package that equips an LLM-driven agent with a concrete capability, such as reading email, executing shell commands, or signing blockchain transactions. Each skill is a hybrid artifact-a structured half declares executable interfaces, while a prose half dictates when and how those interfaces fire-and the prose is reinterpreted probabilistically on every invocation. Conventional static analyzers parse the structured half but ignore the prose; LLM-based tools read the prose but cannot reproducibly prove that a tainted input reaches a high-impact sink.
  We present Semia, a static auditor for agent skills. Semia lifts each skill into the Skill Description Language (SDL), a Datalog fact base that captures LLM-triggered actions, prose-defined conditions, and human-in-the-loop checkpoints. Synthesizing a fact base that is both structurally sound and semantically faithful to the original prose is the central challenge; we address it with Constraint-Guided Representation Synthesis (CGRS), a propose-verify-evaluate loop that refines LLM candidates until convergence. Security properties (e.g., indirect injection, secret leakage, confused deputies, unguarded sinks, etc.) over an agent skill can then be reduced to Datalog reachability queries. We evaluate Semia on 13,728 real-world skills from public marketplaces. Semia renders all of them auditable and finds that more than half carry at least one critical semantic risk. On a stratified sample of 541 expert-labeled skills, Semia achieves 97.7% recall and an F1 of 90.6%, substantially outperforming signature-based scanners and LLM baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决如何对AI Agent的技能（agent skill）进行静态审计这一核心问题。研究背景是：AI Agent技能是一种混合文档，它同时包含结构化的可执行接口声明（如API端点）和非结构化的英文自然语言策略描述（如“外部转账需审批”）。当前，Agent技能被大规模分发，但安全风险急剧上升。现有方法存在严重不足：传统的静态分析工具只能解析结构化部分，完全忽略了对安全至关重要的自然语言策略；而基于LLM的审计器虽然能理解文本，但输出不稳定、不可复现，无法确定性地证明攻击路径的存在。因此，这两种方法都无法回答“受污染的输入能否在不经过明确的安全检查点的情况下，到达高影响的操作”这一关键问题。本文的核心贡献是提出了Semia，一个通过约束引导表示合成（CGRS）方法，将技能的自然语言策略忠实地翻译成结构化的Skill描述语言（SDL）事实库，从而将安全属性审计简化为确定性Datalog可达性查询的静态分析工具，最终解决了对Agent技能进行可复现、高精度的预部署安全审计问题。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可按以下类别组织：

**方法类研究**：本文与基于Datalog的静态分析工具（如Doop、bddbddb、Vandal等）关系密切，这些工具通过将程序表示为关系事实库并使用Datalog规则进行可达性分析来检测漏洞。本文的创新在于将这一范式拓展到混合文档（agent技能），核心区别是本文必须通过CGRS（约束引导表示合成）从非结构化文本生成事实库，而非依赖确定性编译器。直接使用LLM进行单次合成的方法（如本文消融实验中的基线）被证明效果有限，F1仅为86.6%。

**应用类研究**：相关研究包括对插件生态系统的安全分析、MCP特定威胁调查等，这些工作记录了无结构约束时组合这类工件带来的风险。本文与它们的区别在于，本文开创性地将静态审计应用于agent技能这一全新工件类型，并实现了规模化审计（13,728个真实技能）。

**评测类研究**：本文与传统的基于签名的扫描器和直接LLM分析进行了对比，在541个人工标注的技能样本上，Semia的召回率达97.7%，F1为90.6%，显著优于基线方法。这表明本文方法在安全审计的精确性和覆盖率上具有明显优势。

### Q3: 论文如何解决这个问题？

Semia的核心方法是提出了一种基于约束引导的表示合成（CGRS）方法，将智能体技能转化为结构化事实库以进行静态审计。整体框架首先定义了技能描述语言（SDL），这是一个基于Datalog的关系事实模式，能够捕获技能的安全相关元素，包括调用骨架、数据流、动作注释、秘密与屏障、文档声明和代码级标记。主要模块包括SDL事实模式定义和CGRS合成算法。CGRS采用提议-验证-评估循环：首先让LLM从混合了YAML、代码存根和自然语言散文的原始技能中初步生成SDL事实候选，然后通过结构性约束（确保事实符合SDL模式）和语义性约束（确保事实忠实于原文散文）进行验证，识别出不准确或遗漏的部分；接着基于验证反馈评估候选质量，如果未收敛则重新提议。这一过程迭代进行，直到事实库既结构有效又语义忠实。关键技术在于将安全属性（如间接注入、秘密泄露、代理混淆、未保护接收点等）规约为Datalog的可达性查询，通过在合成的事实库上执行这些查询来检测风险。创新点有两个：一是SDL将散文定义的条件与结构化接口统一为可供推理的谓词集合；二是CGRS通过结合LLM的灵活性和约束的精确性，解决了从非结构化文本中生成可证明的正确事实库的挑战，从而替代了传统静态分析器忽略散文和基于LLM的工具无法可重复验证的局限。

### Q4: 论文做了哪些实验？

Semia在13,728个来自公共市场的真实Agent技能上进行了实验。实验设置包括：使用约束引导表示合成（CGRS）将每个技能转化为技能描述语言（SDL）事实库，然后通过Datalog可达性查询检测安全属性（如间接注入、秘密泄露、混淆代理、未保护接收器）。对比方法包括基于签名的扫描器和LLM基线。主要结果：Semia使所有技能都可审计，发现超过一半的技能存在至少一个关键语义风险。在由专家标注的541个技能分层样本上，Semia达到97.7%召回率和90.6%的F1分数，显著优于基线方法。关键数据指标：Recall 97.7%，F1 90.6%。

### Q5: 有什么可以进一步探索的点？

这篇论文提出的Semia框架在agent技能审计上取得了突破，但仍有多个值得深入探索的点。首先，论文主要聚焦于单一技能的静态分析，未来可扩展到多技能交互场景下的组合性风险分析，例如多个技能串联使用时可能出现的间接注入或权限提升。其次，CGRS的收敛性依赖LLM候选生成的质量，可探索引入对抗训练或结构化约束增强来提升语义提取的鲁棒性，减少对LLM基础能力的依赖。此外，当前审计属性限于预定义的安全类别，未来可研究自动发现新型攻击模式（如跨技能数据流隐通道）的归纳方法。另外，Semia对动态环境（如运行时用户输入导致的技能行为变化）的建模仍有局限，可考虑结合符号执行或运行时监控来完善。最后，为提升实用性，可探索将审计结果自动转化为安全加固策略（如插入检查点或最小化权限），形成审计-修复闭环。

### Q6: 总结一下论文的主要内容

Agent技能是赋予LLM代理具体能力的配置包，包含结构化接口声明和自然语言策略描述。传统静态分析只能处理结构化部分，LLM工具虽然能理解文本但无法可重复地证明恶意输入能到达高影响操作。本文提出Semia，一种针对Agent技能的静态审计器。其核心贡献是约束引导表示合成（CGRS），通过提出-验证-评估循环，迭代优化LLM生成的技能描述语言（SDL）事实库，确保其在结构正确性的同时语义忠实于原始文本。安全属性（如间接注入、秘密泄露、未防护sink等）被转化为Datalog可达性查询。在13,728个真实技能上的评估显示，Semia使所有技能可审计，并发现超过半数存在至少一个关键语义风险。在541个专家标注样本中，Semia达到97.7%召回率和90.6% F1分数，显著优于签名扫描器和LLM基线，并发现17个已确认的零日漏洞，证明了其对Agent技能静态安全审计的有效性和必要性。
