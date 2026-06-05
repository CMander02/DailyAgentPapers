---
title: "AURA: Intent-Directed Probing for Implicit-Need Surfacing in Situated LLM Agents"
authors:
  - "Yang Li"
  - "Jiaxiang Liu"
  - "Jiang Cai"
  - "Mingkun Xu"
date: "2026-06-04"
arxiv_id: "2606.05557"
arxiv_url: "https://arxiv.org/abs/2606.05557"
pdf_url: "https://arxiv.org/pdf/2606.05557v1"
github_url: "https://github.com/innovation64/AURA"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "隐式需求探测"
  - "意图推理"
  - "ReAct风格Agent"
  - "工具使用"
  - "探测预算控制"
  - "评测基准"
relevance_score: 9.5
---

# AURA: Intent-Directed Probing for Implicit-Need Surfacing in Situated LLM Agents

## 原始摘要

A situated query like "where is Lin Wei?" often encodes more than its literal content: the user may also want to know whether Lin Wei is free, in a good mood, or worth interrupting now. Standard tool-use agents answer the literal question and stop. AURA inserts an inference step between scene perception and tool use that produces an IntentFrame: a structured estimate of the implicit need with a scalar gap score that controls per-query probe budget and tool selection. On a 100-query four-scene implicit-intent benchmark, AURA improves implicit-need coverage over ReAct-style probing (Delta = +0.07, p < 10^-6); three of four scenes are individually significant, the gain reproduces on a second backbone, and a prompt ablation attributes the lift to gap calibration rather than answer memorisation. On factual lookup the controller trades raw accuracy for 82% fewer probes and zero forbidden-tool violations on a privacy-sensitive slice; scope conditions are detailed in Limitations. Code, simulator, and benchmark are released at https://github.com/innovation64/AURA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文针对的是情境化LLM Agent（如家居或办公场景中的智能助手）在理解用户隐式需求方面的不足。研究背景是：当用户提出一个情境化查询（例如“林伟在哪里？”），其字面含义背后往往隐藏着更深层的需求，比如用户可能还想知道林伟是否方便、情绪好不好、是否值得现在打扰。然而，现有的标准工具使用Agent通常只回答字面问题就结束了，无法捕捉并满足用户的隐式意图。现有方法（如ReAct风格的探测）虽然能进行一些推理，但缺乏对隐式需求的显式建模和成本控制，往往探测过多或过少。本文要解决的核心问题是：如何让LLM Agent在感知场景后、使用工具前，自动识别并量化用户的隐式需求，从而在有限的探测成本下，更全面、精准地满足用户未明说的意图，同时避免不必要的资源浪费（如减少无效探测）和隐私风险。为此，论文提出了AURA框架，通过插入一个意图导向的推理步骤，生成一个包含隐式需求估计和预算控制的IntentFrame，以实现更高效、更符合用户期望的智能响应。

### Q2: 有哪些相关研究？

本文相关研究主要分为三类：**工具使用与推理方法**、**隐式需求理解**以及**智能体评测基准**。

在**方法类**中，ReAct、Toolformer 等标准工具使用智能体仅执行字面查询，本文对比实验表明 AURA 通过场景感知与工具使用间的意图推理步骤（IntentFrame），在隐式需求覆盖率上显著超越 ReAct 式探询（Delta=+0.07）。与强调链式推理的 Reflexion 不同，AURA 不依赖回溯修正，而是通过差距校准（gap calibration）动态控制探询预算。

在**隐式需求理解**方面，现有工作多聚焦于显式指令遵循或常识推理，而 AURA 首次针对情境化查询（如“林伟在哪？”）建模非字面意图（如是否可打断）。本文提出的 gap score 机制与结构化 IntentFrame 框架，区别于传统隐式意图分类方法。

**应用与评测类**中，当前工具使用基准（如 ToolBench）侧重功能正确性，而 AURA 构建了包含 100 个查询、4 个场景的隐式意图基准，填补了评估维度空白。消融实验证明改进源自 gap 校准而非记忆，开源代码与仿真器确保了可复现性。

### Q3: 论文如何解决这个问题？

AURA 通过引入一个基于意图的推理层来解决隐式需求挖掘问题。其核心方法是在场景感知和工具使用之间插入一个中间推理步骤，该步骤生成一个IntentFrame结构化估计：包含用户隐式需求的估计以及一个标量的“差距分数”。这个差距分数动态控制每个查询的探测预算和工具选择。

整体框架包含三个主要模块。第一是场景感知模块，处理输入的情境查询和环境信息。第二是IntentFrame生成模块，这是创新核心：它不仅解释字面问题，还推断用户的深层意图（如是否需要知道对方是否空闲、情绪如何等），并通过差距分数量化当前信息与完全满足用户需求之间的差距。第三是差异感知控制器，该控制器根据差距分数决定是继续探测假设以缩小信息差距，还是调用具体工具执行操作。

关键技术包括：1）基于差距分数的动态探测预算控制，相比ReAct风格的固定探测，能更高效地利用资源；2）结构化意图表示框架，让模型显式处理隐式需求；3）差异校准机制，通过消融实验验证了正是差距分数的校准带来了性能提升，而非简单的答案记忆。该设计使得AURA在保持事实查询准确性的同时，将探测数量减少了82%，并在隐私敏感场景实现零违规工具调用。

### Q4: 论文做了哪些实验？

论文评估了AURA在隐含需求覆盖率和工具使用效率两方面的性能。实验设置围绕一个包含100条查询、覆盖四个场景的隐含意图基准（benchmark）展开。主要对比方法为ReAct风格的探测基线。在隐含需求覆盖率指标上，AURA相比基线提升了+0.07（p < 10⁻⁶），且四个场景中有三个达到统计显著性。该结果在第二套骨干网络（backbone）上得到复现。消融实验（prompt ablation）证实，性能提升源于差距校准（gap calibration）而非机械化答案记忆。在事实性查找任务中，AURA的控制器以牺牲少量原始准确率为代价，将探测次数减少了82%，并在隐私敏感数据切片上实现了零禁用工具违规。实验关键指标包括：隐含需求覆盖率提升（Δ=+0.07）、探测次数减少82%以及零违规率。

### Q5: 有什么可以进一步探索的点？

AURA目前的局限性在于：(1) 基准测试仅包含100个查询和4个场景，规模较小且场景多样性不足，可能无法充分验证方法的泛化能力；(2) 意图框架中gap分数的校准依赖人工标注，缺乏自动化评估机制；(3) 工具选择的决策策略较为简单，未能动态适应不同用户或任务上下文。未来研究方向包括：(1) 构建更大规模、更多样化的隐含意图基准，涵盖跨语言、多模态场景；(2) 探索基于强化学习的gap分数自动优化方法，或利用用户反馈进行在线学习；(3) 引入个性化建模，使代理能根据用户历史行为推断其常用意图模式；(4) 将意图推断与长期记忆结合，实现跨对话的意图追踪。也可尝试将AURA框架扩展到多代理协作场景中，使代理能主动协商意图理解。

### Q6: 总结一下论文的主要内容

AURA 提出了一种面向隐式需求探测的意图导向推理框架，解决当前 LLM Agent 仅回答字面问题、忽略用户潜在意图的局限。论文定义问题为：在场景感知与工具使用之间，对类似“Lin Wei 在哪儿”的查询进行隐式意图推断，明确用户是否想知道对方有空、心情好或是否适合打扰。方法核心是 IntentFrame，它结构化估计隐式需求并附加一个标量 gap score，用于控制每查询的探测预算和工具选择。在 100 查询四个场景的隐式意图基准上，AURA 相比 ReAct 风格探测，将隐式需求覆盖率提升 +0.07（p < 10^-6），三个场景显著，且在不同骨干模型上可复现。消融实验证实提升来自 gap 校准而非记忆。在事实查询场景中，它用 82% 更少的探测次数换取准确率，并在隐私敏感切片上实现零禁止工具违规。论文同时阐述了局限，并开源了代码、模拟器和基准。该工作系统性地增强 Agent 场景理解与用户意图匹配能力。
