---
title: "Skill-to-LoRA: From Using Skills to Learning Behaviors for Token-Efficient LLM Agents"
authors:
  - "Tianyi Zhang"
  - "Zhonghao Qi"
date: "2026-06-15"
arxiv_id: "2606.16769"
arxiv_url: "https://arxiv.org/abs/2606.16769"
pdf_url: "https://arxiv.org/pdf/2606.16769v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Skill Learning"
  - "LoRA Adapter"
  - "Token Efficiency"
  - "SWE-Bench"
  - "Behavioral Module"
  - "Multi-Skill Agent"
relevance_score: 9.0
---

# Skill-to-LoRA: From Using Skills to Learning Behaviors for Token-Efficient LLM Agents

## 原始摘要

Agent skills are commonly distributed as SKILL.md files: human-readable procedural documents that describe workflows, tools, resources, and domain conventions. While convenient for inspection and reuse, this design requires the same reusable procedure to be repeatedly injected into the runtime context. We propose Skill-to-LoRA(S2L), a behavior-centric skill representation that replaces runtime skill text with skill-specific LoRA adapters. Rather than compressing the skill document itself, S2L models the behavioral change induced by the skill text: offline, the complete SKILL.md is used to synthesize skill-guided demonstrations; online, the full document is omitted and the corresponding LoRA adapter is dynamically loaded to activate the learned skill behavior. We evaluate S2L with Qwen3.6-27B on a 21-skill subset of SWE-Skills-Bench. Compared with the no-skill and Full Skill Text baselines, S2L improves pass rate by 2.9 and 5.2 percentage points, respectively, while reducing per-step token cost by 6.6% relative to Full Skill Text prompting. S2L matches or improves Full Skill Text on 18/21 skills and the no-skill baseline on 15/21 skills. Control experiments further show that the gains depend on skill-specific adapter alignment: Wrong-LoRA and Shared-LoRA both reduce performance. These results suggest that many procedural agent skills can be converted from runtime instructions into trainable, dynamically loadable behavioral modules. Code will be released upon acceptance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）智能体在使用技能库时面临的一个核心矛盾：现有的技能分发通常采用人类可读的SKILL.md文本文件，虽然便于检查和复用，但每次任务执行时都必须将完整的技能文档重复注入到推理上下文中。这种方法存在几个显著不足：一是长技能文档会与仓库状态等局部证据竞争上下文窗口，导致信息干扰；二是增加了每一步推理的Token消耗，提高了计算成本；三是固定的文本提示可能僵化模型的行为，在SWE-Skills-Bench基准上甚至观察到，精心设计的技能提示有时对性能是中性甚至有害的。现有的压缩、检索或缓存策略虽然可以减少冗余上下文，但本质上仍将核心技能过程作为运行时文本保留。本文提出的Skill-to-LoRA（S2L）方法，旨在将技能从运行时文本指令转变为可学习的参数化行为模块。其核心思想不是压缩或总结技能文档，而是将技能文档所诱发的模型行为变化（包括工作流程、工具使用模式、验证策略等）蒸馏成轻量级的LoRA适配器。这样，在在线推理时，智能体无需加载完整的SKILL.md，只需动态加载相应的LoRA适配器即可激活对应的技能行为，从而实现Token高效且性能更优的技能调用。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及以下几个类别：

**方法类：** 参数侧上下文与技能内化（Parameter-side context and skill internalization）。LoRA和QLoRA为技能级适配提供了基础。相关工作包括PromptIntern（将重复提示内化至微调中）、Text-to-LoRA（将任务描述映射为LoRA参数）、Doc-to-LoRA（将文档映射为LoRA参数）以及SKILL0（通过强化学习逐步撤回技能上下文）。本文（S2L）与这些工作的核心区别在于：S2L采用监督学习路线，利用原始技能文档合成工作流演示来训练LoRA权重，而非从环境反馈或强化学习中学习，且专门针对SWE-Skills的. skill.md文件进行替换。

**评测类：** 技能基准（Skill benchmarks）。SkillsBench和SWE-Skills-Bench用于评估过程性技能注入对任务的影响。SWE-Skills-Bench最接近本文设定，其单技能分配是S2L设计的基础。本文指出，SWE-Skills-Bench报告了平均增益有限、许多技能无改进及全技能文本提示的巨额token开销问题，这正是S2L试图解决的替换问题。

**应用类：** 经验驱动的文本技能与技能记忆（Experience-derived textual skills and skill memories）。Trace2Skill、SkillNet、SkillRL等研究从交互经验中提取可复用过程性知识。与这些工作不同，S2L不依赖于从基准测试回滚或验证信号学习，而是直接利用原始技能Markdown合成工作流演示。

### Q3: 论文如何解决这个问题？

论文提出Skill-to-LoRA (S2L)方法，将自然语言技能文档转换为可动态加载的LoRA适配器，从而在推理时降低token开销。整体框架分为离线训练和在线推理两个阶段。离线训练阶段采用基于技能的自蒸馏方法：首先，使用完整的SKILL.md文档，通过两个LLM驱动的数据生成代理自动构造训练数据——一个代理根据技能文档生成多样化的任务输入（如用户请求），另一个代理结合任务输入和完整技能文档生成目标输出（展示技能应用的具体行为）。然后，冻结基础语言模型，仅训练与每个技能对应的轻量级LoRA适配器，以标准因果语言建模目标优化，让适配器学习技能文本所诱导的行为偏差（如工作流模式、工具使用偏好等）。在线推理阶段，系统不再在提示中注入完整技能文档，而是根据任务关联的技能ID，从预训练的适配器库中动态加载对应的LoRA适配器到冻结的基础模型上，激活技能特定的行为。核心创新在于将技能知识从运行时文本转移到参数化的LoRA模块中，实现了token高效的技能执行。实验表明，S2L在SWE-Skills-Bench的21个技能子集上，相比完整技能文本基线，通过率提升2.9个百分点，每步token成本降低6.6%，且效果依赖于技能特定的适配器对齐。

### Q4: 论文做了哪些实验？

论文在SWE-Skills-Bench的21个子技能（共210个任务）上评估了Skill-to-LoRA (S2L)。实验设置使用Qwen3.6-27B作为冻结基座模型，通过OpenCode和vLLM运行，采用32K上下文预算和4K输出预算。对比方法包括：无技能的Vanilla LLM、注入完整SKILL.md的Full Skill Text，以及用技能特定LoRA适配器替换技能文档的S2L。此外还设置了加载最不相似技能适配器的Wrong-LoRA和在多技能数据上训练单一适配器的Shared-LoRA作为控制实验。

主要结果：S2L在210个任务中解决了65个，高于Vanilla LLM的59个和Full Skill Text的54个。相比无技能基线，S2L通过率提升2.9个百分点，相比Full Skill Text提升5.2个百分点。S2L将每步token成本降低了4.89%（相对Full Skill Text降低6.6%），而Full Skill Text则增加了13.39%。S2L在18/21个技能上匹配或优于Full Skill Text，在15/21个技能上优于无技能基线。错误适配器和共享适配器均导致性能下降，表明技能特定适配器对齐至关重要。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于S2L对稳定流程型技能的依赖。那些依赖具体代码示例、灵活语法迁移或开放式推理的技能，仍可能受益于运行时文本提供的丰富上下文和检索能力。此外，将技能行为蒸馏为LoRA参数本质上是行为压缩，可能丢失稀有边缘案例或高度特定的配置模式，同时降低了直接可解释性。未来可探索以下方向：1) 研究技能类型与参数化表征的匹配度，开发混合系统，对不稳定技能保留文本提示，稳定技能则使用LoRA；2) 解决多技能组合问题，包括动态适配器路由和冲突管理，例如设计任务感知的路由机制或应用元学习来协调多个LoRA的行为；3) 提升参数化行为的可解释性，可能通过联合训练解释性文本或设计可视化工具，使黑箱化的LoRA行为更易于理解和调试。

### Q6: 总结一下论文的主要内容

这篇论文提出了Skill-to-LoRA（S2L），一种行为导向的技能表示方法，旨在解决传统基于文本的技能文档在运行时反复注入导致的高token消耗和推理干扰问题。核心贡献在于将技能定义从“可读文本”转化为“可学习的行为模块”：离线阶段，利用完整的SKILL.md文档合成技能引导的示范数据，并通过LoRA训练将行为模式蒸馏为轻量级参数；在线推理时，移除完整技能文本，动态加载对应LoRA适配器激活技能行为。在SWE-Skills-Bench数据集的21个技能子集上，使用Qwen3.6-27B模型评估，S2L相比完整技能文本基线提升了5.2个百分点的通过率，同时每步token消耗降低6.6%。主要结论表明，参数化技能表示不仅能减少上下文开销，还能缓解长文本干扰，且性能提升依赖于技能特定适配器的对齐，错误的或共享的LoRA会降低效果。这项工作将程序性技能从运行时指令转换为可训练、可动态加载的行为模块，为构建token高效型LLM智能体提供了新范式。
