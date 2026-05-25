---
title: "SkillOpt: Executive Strategy for Self-Evolving Agent Skills"
authors:
  - "Yifan Yang"
  - "Ziyang Gong"
  - "Weiquan Huang"
  - "Qihao Yang"
  - "Ziwei Zhou"
  - "Zisu Huang"
  - "Yan Li"
  - "Xuemei Gao"
  - "Qi Dai"
  - "Bei Liu"
  - "Kai Qiu"
  - "Yuqing Yang"
  - "Dongdong Chen"
  - "Xue Yang"
  - "Chong Luo"
date: "2026-05-22"
arxiv_id: "2605.23904"
arxiv_url: "https://arxiv.org/abs/2605.23904"
pdf_url: "https://arxiv.org/pdf/2605.23904v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent技能优化"
  - "文本空间优化"
  - "多智能体系统"
  - "技能迁移"
  - "自我进化Agent"
  - "SWE-bench"
  - "WebArena"
  - "LLM驱动Agent"
relevance_score: 9.5
---

# SkillOpt: Executive Strategy for Self-Evolving Agent Skills

## 原始摘要

Agent skills today are hand-crafted, generated one-shot, or evolved through loosely controlled self-revision, none of which behaves like a deep-learning optimizer for the skill, and none of which reliably improves over its starting point under feedback. We argue the skill should instead be trained as the external state of a frozen agent, with the same discipline that makes weight-space optimization reproducible. SkillOpt is, to our knowledge, the first systematic controllable text-space optimizer for agent skills: a separate optimizer model turns scored rollouts into bounded add/delete/replace edits on a single skill document, and an edit is accepted only when it strictly improves a held-out validation score. A textual learning-rate budget, rejected-edit buffer, and epoch-wise slow/meta update make skill training stable while adding zero inference-time model calls at deployment. Across six benchmarks, seven target models, and three execution harnesses (direct chat, Codex, Claude Code), SkillOpt is best or tied on all 52 evaluated (model, benchmark, harness) cells and beats every per-cell competitor among human, one-shot LLM, Trace2Skill, TextGrad, GEPA, and EvoSkill skills. On GPT-5.5 it lifts the average no-skill accuracy by +23.5 points in direct chat, by +24.8 inside the Codex agentic loop, and by +19.1 inside Claude Code. Transfer experiments further show that optimized skill artifacts retain value when moved across model scales, between Codex and Claude Code execution environments, and to a nearby math benchmark without further optimization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有Agent技能（skill）优化方法缺乏系统性和可控性的问题。当前，Agent技能通常是手工编写、一次性生成或通过松散控制的自我修订产生，这些做法都不像深度学习优化器那样对技能本身进行可复现的优化，导致技能在反馈下无法稳定提升。现有方法虽然从执行经验中提取可复用的文本技能（如蒸馏轨迹、文件夹式优化等），但未能解决核心问题：如何像训练模型权重那样，系统性地、可控地优化作为适配层的技能文档。为此，本文提出了SkillOpt——首个系统性的、可控的文本空间技能优化器。它引入了一个独立的优化器模型，将带评分的执行轨迹转化为对单一技能文档的有界增/删/改编辑，并通过保留验证集上的严格评分提升来接受编辑。通过文本学习率预算、被拒编辑缓冲池和逐轮慢/元更新等机制，SkillOpt使得技能训练过程稳定且可复现，同时部署时零额外调用。其核心是让技能优化遵循与权重空间优化相同的严谨性，将技能文档视为冻结Agent的外部可训练状态。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可以分为两类：

**Prompt自动调优与Agent配置搜索类**：包括GEPA（利用轨迹反馈引导反思性Prompt演化）、ABSTRAL和EvoTest（将可优化对象从单一Prompt扩展到多智能体设计文档和测试时系统演化）。这些方法将语言制品作为可优化对象，直接利用执行反馈，但主要针对Prompt、系统设计或完整配置，而非可复用的领域适配。本文SkillOpt则优化一个持久的技能文档，具备可训练、验证、导出和复用特性，实现了语言级可控性与稳定程序化技能状态的结合。

**技能构建与技能演化类**：包括SkillsBench、Agentic Skills SoK（将技能定义为可复用程序化知识），以及从终身经验、轨迹教训、技能知识库等构建技能的方案，并通过失败分析、创建-评估-修订循环、协同演化生成器与验证器、集体更新或强化学习来改进技能。这些工作强调技能发现、仓库增长、共享、演化搜索或策略优化。本文则专注于一个更窄的问题：如何像深度学习一样，通过轨迹批次、反思微批次、文本学习率、验证门控、拒绝编辑缓冲区和慢/元更新等控制手段，训练一个紧凑的领域技能，产出可移植的best_skill.md而不改变模型权重。

### Q3: 论文如何解决这个问题？

SkillOpt通过引入一个独立的优化器模型和严格的验证机制，将技能优化建模为可控的文本空间优化过程。其核心是模仿深度学习训练中的权重更新，将技能文档视为冻结智能体的可训练外部状态。

整体框架是一个迭代优化循环，包含三个主要组件：**执行模块**、**优化器模块**和**验证门控**。首先，冻结目标模型使用当前技能在训练数据上执行一批任务，收集包含轨迹和分数的完整执行证据。接着，优化器模型分析这批数据：它将成功和失败的轨迹分开，并分组为反思微批次，避免单条轨迹导致偶然性修复。每个微批次产生结构化的**添加/删除/替换**编辑操作，然后通过层次化合并过滤重复、矛盾和建议，最后根据可编辑预算只保留排名靠前的有限个编辑。这个预算充当**学习率**，防止技能被无限制重写破坏已有规则。优化器还引入**被拒编辑缓冲区**，记录失败模式及其导致的性能下降，供后续反思避免重复错误。生成的候选技能立即在验证集上评估，只有**严格提高验证分数**的编辑才会被接受，否则被拒绝。此外，跨epoch的**慢/元更新**机制保留长期经验，逐步巩固快速局部变化而不改变目标模型。整套流程在部署时不增加任何推理开销，最终输出一个最优技能文档。

### Q4: 论文做了哪些实验？

论文在六个基准测试（SearchQA、SpreadsheetBench、OfficeQA、DocVQA、LiveMathematicianBench、ALFWorld）上评估了SkillOpt，涵盖GPT和Qwen两个模型家族共七种目标模型，以及三种执行框架（直接对话、Codex、Claude Code）。实验采用确定性数据集划分（split_seed=42），使用分离的测试集报告准确率或硬分数。对比方法包括无技能、人工技能、单次LLM技能、Trace2Skill、TextGrad、GEPA和EvoSkill。主要结果：在全部52个（模型、基准、框架）组合单元格中，SkillOpt全部取得最佳或持平。以GPT-5.5直接对话为例，六基准平均准确率从无技能的58.8%提升至82.3%（+23.5个百分点），超越最佳单单元格基线均值76.9%。具体提升幅度：SpreadsheetBench从41.8%到80.7%（+38.9），OfficeQA从33.1%到72.1%（+39.0），LiveMathematicianBench从37.6%到66.9%（+29.3）。在Qwen3.5-4B上SpreadsheetBench从9.3%提升至23.9%（×2.6），GPT-5.4-nano上ALFWorld从34.3%提升至69.4%（×2.0）。跨模型规模、框架和基准的迁移实验进一步验证了优化技能工件的泛化价值。

### Q5: 有什么可以进一步探索的点？

论文的核心贡献在于将技能优化视为可控的文本空间搜索，但存在明显局限：优化器模型本身是冻住的，这意味着其编辑策略无法随任务分布变化而自适应调整。未来可探索的方向包括：1）引入元学习框架，让优化器根据验证集反馈动态调整编辑偏好，例如对成功率低的任务增加替换操作权重；2）当前文本学习率控制的是编辑幅度，但未考虑技能文档的结构化信息（如代码块层级），可设计基于抽象语法树（AST）的细粒度编辑策略，对高风险操作施加更严格的预算约束；3）拒绝编辑缓冲区的去重机制可进一步优化，利用嵌入相似度检测冗余拒绝样本，避免优化器陷入局部最优。此外，跨环境迁移实验表明技能具有可迁移性，这提示我们可以构建一个技能演化池，通过强化学习自动筛选跨任务泛化能力强的技能变体，使技能优化从被动接收验证分数转向主动探索更有效的编辑模式。

### Q6: 总结一下论文的主要内容

SkillOpt的核心贡献是提出了一种系统性的文本空间优化方法，将智能体技能作为可训练的外部状态，首次实现了类似深度学习的可控技能优化过程。该方法针对现有技能手工构建、一次性生成或自我修改不可靠的问题，通过一个独立的优化器模型将带评分的执行轨迹转换为受限的增/删/改操作，仅在严格提升验证集性能时接受编辑。论文在6个基准、7个目标模型和3种执行框架上的52个评估单元中均取得最优或并列最优，在GPT-5.5上平均提升无技能基线23.5-24.8个百分点。主要结论表明，文本学习率、拒绝编辑缓冲区和epoch级慢/元更新机制使技能训练稳定，且优化后的技能工件可跨模型规模、执行环境和相近基准迁移，无需调整模型权重，实现了可审计、可复用的紧凑技能文档（300-2000 token）。
