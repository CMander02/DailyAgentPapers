---
title: "SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior"
authors:
  - "Zhiyu Chen"
  - "Zihan Guo"
  - "Bo Huang"
  - "Bingwei Lu"
  - "Jianghao Lin"
  - "Yuanjian Zhou"
  - "Weinan Zhang"
date: "2026-06-10"
arxiv_id: "2606.11543"
arxiv_url: "https://arxiv.org/abs/2606.11543"
pdf_url: "https://arxiv.org/pdf/2606.11543v1"
github_url: "https://github.com/zhiyuchen-ai/skill-juror"
categories:
  - "cs.AI"
  - "cs.SE"
tags:
  - "Agent技能组织"
  - "渐进式技能披露"
  - "技能基准评估"
  - "LLM Agent运行时行为"
  - "程序性知识"
relevance_score: 8.5
---

# SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior

## 原始摘要

Agent Skills augment large language model (LLM) agents with procedural knowledge at inference time, but current benchmarks rarely distinguish what a Skill says from how it is organized. We study this distinction through Progressive Disclosure, where a concise root file points agents to supporting resources on demand, and compare it with a normalized flat baseline. We present SkillJuror, a framework for evaluating Skill writing paradigms through semantically controlled variants, matched multi-trial evaluations, and trajectory evidence while holding task knowledge fixed. In an 82-task SkillsBench study, Progressive Disclosure changes runtime behavior before aggregate outcomes: distinct Skill resources touched per trajectory rise from 1.18 to 3.85, and effective uptake events rise from 1.33 to 3.92. It also yields 17 additional verifier-passing trials out of 410 matched trials (+4.1%) over the normalized flat baseline. The benefit is task-dependent. Progressive Disclosure helps when supporting resources guide implementation, checking, or repair, but is weaker when success hinges on exact output conventions, numerical thresholds, or long artifact-generation pipelines. These results show that Skill organization is not mere presentation: it can change how agents search and apply procedural knowledge, while outcome gains depend on whether the exposed resources are actionable for the task. Code is available at https://github.com/zhiyuchen-ai/skill-juror.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前Agent Skills评价中的一个根本性盲区：技能的组织方式（如何组织技能内容）与技能所包含的知识本身（技能说什么）在影响智能体运行时行为时被混淆了。研究背景是，Agent Skills已成为大语言模型智能体在推理时获取程序性知识的关键机制，但现有基准测试和风格指南大多只关注技能的有无或知识的覆盖范围，未能严格分离“知识内容”与“组织结构”这两个变量。现有方法的不足在于，自然形成的技能集合会同时包含知识覆盖、作者风格和结构组织上的差异，导致无法归因性能提升究竟是源于更好的组织、更丰富的知识，还是两者共同作用。这一归因缺口使得技能编写建议缺乏严谨的实证支持。本文要解决的核心问题是在保持任务知识完全固定的前提下，通过控制实验系统性地评估技能组织（具体关注逐步揭示策略）如何改变智能体的运行时行为（如资源访问模式），并最终影响任务成败。论文通过SkillJuror框架，构建知识匹配但组织方式不同的技能变体，结合多轮匹配测试和轨迹证据，从而将组织本身作为一个可控的运行时干预变量进行隔离研究，为技能编写范式提供可归因的实证基础。

### Q2: 有哪些相关研究？

主要相关研究按类别可分为三类。第一类是技能验证与评测研究：如**SkillsBench**对比了无技能、精选技能和自生成技能条件下的任务通过率，发现精选技能能提升通过率但效果异质性强，且自生成技能可能无效甚至有害；**SWE-Skills-Bench**则将技能采纳问题扩展到基于仓库的软件工程任务。这些工作聚焦于“技能是否有用”，而本文则关注**同一任务知识的不同组织形式**如何影响行为，即从技能可用性转向受控的变体比较。第二类是技能学习与生成研究：**SkillLearnBench**评估持续技能学习方法，**SkillGenBench**和**SkillGen**分别从仓库/文档及成功/失败轨迹中生成技能。这些工作关注技能来源与生成质量，而本文通过固定任务范围、辅助工具等，隔离出组织范式这一单一变量。第三类是智能体行为评估研究：现有成果如轨迹感知基准（评估工具使用、推理过程）和成本感知评估（结合资源消耗），而**SkillJuror**在此基础上引入受控的执行平台（harness）以及LLM作为评判者，从轨迹中捕获资源有效利用事件，从而量化技能布局对运行时搜索和应用行为的因果影响。

### Q3: 论文如何解决这个问题？

SkillJuror通过一个三阶段的流水线框架来解决技能组织方式如何影响智能体运行时行为的问题。首先，在构造阶段，它采用知识保持约束下的Skill-to-Skill转换方法，将原始技能束转化为语义匹配的控制对：一个扁平化的基线版本和一个渐进式披露（PD）变体。PD变体以轻量级根文档SKILL.md为核心，通过超链接指向按需加载的支持文件，而基线版本则将所有知识平铺在单一文件中。这一转换通过LLM智能体在沙箱环境中自动完成，并经过结构遵守性和知识保持性两层严格验证，确保两种变体仅在组织结构上存在差异，而任务范围、工作流义务、阈值和验证合约等知识内容完全不变。

在执行阶段，SkillJuror将同一任务的标准执行环境（指令、工作空间、环境、验证器）固定，仅交换暴露的技能束，在多个独立试验中重复执行任务-条件对，收集轨迹和验证器记录。评估阶段则将运行痕迹映射到四个分析维度：结果效用、效率权衡、范式实现和资源路由质量。其中，有效资源获取（ERU）作为核心指标，通过LLM裁判审计轨迹事件，判断技能资源是否被实际消费到实施、验证、纠正或阻塞诊断中。此外，SkillJuror还为每个任务附加属性模式，包括上下文标签和机制标签（如工作流类型、验证类型），以支持任务依赖性的异质性分析，从而探究资源摄取何时与结果增益相关联。

### Q4: 论文做了哪些实验？

论文在82个SkillsBench任务上进行了实验，使用GPT-5.4作为运行时模型，每任务-条件组合运行5次试验，每个条件共410次试验。实验对比了三个条件：无Skill、归一化扁平基线（Baseline）和渐进式揭示（Progressive Disclosure, PD）。主要结果包括：PD的严格验证通过率为46.1%（189/410），Baseline为42.0%（172/410），PD比Baseline多17次通过（+4.1%）；PD的每通过时间从20.1分钟降至17.8分钟，但每通过成本几乎持平（$1.31 vs $1.28）。PD改变了过程行为，每个轨迹接触的不同Skill资源从1.18升至3.85，有效资源采用事件从1.33升至3.92，Skill步骤占比从5.4%翻倍至10.8%，且更多Skill使用发生在轨迹中后期。实验还通过确定性门控、基于量规的语义审计和人工裁决验证了构造可靠性，88个任务中仅3个需要人工审核。任务依赖分析显示PD在23个任务上优于Baseline，44个任务持平，15个任务不及Baseline。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向包括：首先，SkillsBench的82个任务规模有限，且主要来自SWE-bench等源代码领域，未来需要在更多元化的任务类型（如多轮对话、物理世界操作）和更大规模任务集上验证结论的泛化性。其次，当前仅对比了Progressive Disclosure与扁平基线两种组织形式，未来可探索更多组织范式（如分层、动态路由、基于任务类型自适应调整结构），并研究Skill内容的语义相似度、颗粒度等对行为的影响。第三，论文发现过程指标（如资源触达）与结果指标（通过率）有时存在脱节，未来可设计更精细的验证合约，使“局部有用”的资源使用能更直接地转化为最终成功。最后，可结合强化学习或元学习，让智能体在运行时自适应选择最优的Skill组织方式，甚至动态重构Skill依赖关系。

### Q6: 总结一下论文的主要内容

这篇论文研究的是如何衡量智能体技能组织方式对运行时行为的影响。其核心问题是：技能的组织结构（而非内容本身）是否以及如何改变智能体的行为。论文提出SkillJuror框架，通过保持任务知识不变，构建语义匹配的技能变体（渐进式披露与扁平化基线对比），并匹配多轮评估和轨迹证据，来隔离技能组织作为实验性干预变量的效果。在82个任务的SkillsBench研究中，渐进式披露改变了运行时行为：每轨迹接触的不同技能资源从1.18个升至3.85个，有效资源利用事件从1.33次升至3.92次，并在410个匹配试验中带来17个额外的验证器通过（+4.1%）。然而收益取决于任务：当支持资源能指导实现、检查或修复时有效，但在任务成功依赖精确输出约定或长工件生成管道时较弱。结论表明，技能组织不仅是呈现方式，它改变了智能体搜索和应用程序知识的方式，而收益取决于暴露的资源对任务是否可操作。该工作首次将技能组织作为可控运行时变量进行实验评估。
