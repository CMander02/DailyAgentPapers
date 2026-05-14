---
title: "SkillOps: Managing LLM Agent Skill Libraries as Self-Maintaining Software Ecosystems"
authors:
  - "Hongji Pu"
  - "Xinyuan Song"
  - "Liang Zhao"
date: "2026-05-13"
arxiv_id: "2605.13716"
arxiv_url: "https://arxiv.org/abs/2605.13716"
pdf_url: "https://arxiv.org/pdf/2605.13716v1"
github_url: "https://github.com/Hik289/SkillOps"
categories:
  - "cs.SE"
  - "cs.MA"
tags:
  - "LLM Agent"
  - "技能库管理"
  - "技术债务"
  - "库维护"
  - "多智能体系统"
relevance_score: 8.5
---

# SkillOps: Managing LLM Agent Skill Libraries as Self-Maintaining Software Ecosystems

## 原始摘要

Large language model agents increasingly rely on skill libraries for multi-step tasks, yet these libraries can accumulate persistent defects as skills are added, reused, patched, and linked to changing dependencies. We call this failure mode skill technical debt: library-level defects that may not break a single skill locally but can harm future retrieval, composition, and execution. Existing skill-based agents mainly focus on task-time retrieval, planning, and repair, while library-time maintenance remains underexplored. We propose SkillOps, a method-agnostic plug-in framework for maintaining skill libraries. SkillOps represents each skill as a typed Skill Contract (P, O, A, V, F), organizes skills with a Hierarchical Skill Ecosystem Graph, and diagnoses library health across utility, compatibility, risk, and validation dimensions. Given a raw skill library, SkillOps produces a maintained library that can be used by existing retrieval or planning agents without changing their internal code. On ALFWorld, SkillOps achieves 79.5 percent task success as a standalone agent, outperforming the strongest baseline by 8.8 percentage points with no additional task-time large language model calls. As a plug-in layer, it improves retrieval-heavy baselines by 0.68 to 2.90 percentage points. The current rule-based maintenance implementation uses nearly zero library-time large language model calls or tokens, showing that skill-library maintenance can be added as a low-overhead architectural layer.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决LLM代理技能库长期积累“技能技术债务”的问题。研究背景是：LLM代理越来越多地依赖技能库完成多步任务，但技能库并非静态，随着技能不断添加、修补、复用及依赖关系变化，会积累如冗余、缺失验证、接口漂移、实现过时等持久缺陷。现有方法主要关注任务时的技能检索、规划、修复等，但忽略了“库时维护”这一关键环节——一次性的任务时修复可能解决了当前失败，但库底层的缺陷并未消除，未来复用该技能时仍会引发问题。因此，本文的核心问题是：如何在库维护阶段，主动诊断并修复技能库中的持久缺陷，从而预防下游任务中的失败。作者提出SkillOps框架，通过契约式技能表示、层级化技能生态图（HSEG）、健康诊断及维护动作，将原始技能库清理为一个更健康、可直接供下游代理使用的库，且当前实现几乎不消耗LLM调用或token，实现了低开销的架构层维护。

### Q2: 有哪些相关研究？

在相关研究方面，本文涉及的主要工作可分为三类：**任务时技能使用方法**、**库时库维护方法**，以及**软件与机器学习系统的技术债务**。  
1. **任务时技能使用方法**：现有技能型智能体主要聚焦于任务时的技能检索、规划、组合与修复，例如基于检索增强的模型、依赖感知的图搜索等。这些研究的共同假设是技能库本身是健康的，但在库长期演化后该假设变得脆弱。SkillOps则关注库时问题，在任务使用前主动维护库，而不是依赖任务时补丁。  
2. **库时库维护方法**：目前很少有工作直接研究LLM智能体的技能库维护。一些系统试图通过自适应学习自动扩展库，但未系统性地诊断和修复库级缺陷。SkillOps首次形式化技能技术债务，并通过契约表示、层次图结构及健康诊断实现低成本维护。  
3. **软件与ML技术债务**：本文借鉴了传统软件工程和ML系统中的技术债务概念（如冗余、接口漂移），但将其专门化为技能库场景。与现有工作不同，SkillOps的维护不依赖LLM推理，而是基于可观察信号，因此具有极低的库时开销。  
总之，SkillOps填补了任务时方法与库时维护之间的空白，是一个轻量级、与下游方法无关的维护层。

### Q3: 论文如何解决这个问题？

论文提出SkillOps框架解决LLM智能体技能库的“技能技术债务”问题，即技能库随着添加、复用、修补和依赖变化积累的持久性缺陷。

核心方法是将技能库视为自维护软件生态系统，通过两个交替循环实现。整体架构包括：**分层技能生态系统图(HSEG)**，内部技能图将每个技能建模为包含前提(P)、操作(O)、工件(A)、验证器(V)和失败模式(F)的契约图；外部图-图通过依赖、兼容、冗余和替代四种类型边连接技能。

**任务时循环**包含四个阶段：1)技能匹配，结合BM25和语义相关性评分并过滤前提不满足的技能；2)依赖拼接，仅当存在依赖边和兼容边时才允许技能转移，避免接口不匹配；3)验证器和适配器插入，对缺失验证器的边插入验证器，对不兼容边插入适配器恢复类型约束；4)本地修复，执行失败时尝试替代或重新调用修复。

**库时循环**通过五维健康诊断评估技能：效用、冗余、兼容性、失败风险和验证缺口。创新点包括**合约图传播诊断(CGPD)**，沿依赖边传播风险分数，实现对结构完整但继承上游高风险技能的前置验证器插入。每次执行后，框架诊断健康状况并应用合并、修复、退役、添加验证器和适配器等维护操作，以低开销实现技能库的自维护。

### Q4: 论文做了哪些实验？

在ALFWorld基准测试（基于ALFRED PDDL的多步家庭操作任务）上，论文构建了包含229个真实技能及合成退化变体的技能库，使用9个库规模（200至2000）和3个随机种子（42,7,123）评估，共有185个任务实例。对比方法包括ReAct（扁平提示）、LLM_Skill_Planner（GPT-4o-mini语义排序）、Hybrid_Retrieval（BM25+嵌入）、GoS_Style（单依赖图）、SkillWeaver（任务时自修复）等，均使用GPT-4o-mini骨干。主要实验：1）作为独立智能体在200技能库上，SkillOps成功率达79.5%（标准差0），优于最强基线LLM_Skill_Planner达8.8个百分点；2）作为即插即用维护层，改善检索型基线0.68-2.90个百分点；3）在噪声梯度放大至2000技能时，SkillOps稳定保持约80%成功率，远超其他基线（领先31个百分点以上）；4）消融实验显示任务时循环、库维护、图结构和特定操作（如适配器、验证器添加）均对性能有重要贡献。

### Q5: 有什么可以进一步探索的点？

**可以进一步探索的点：**

1. **语义与深层冲突检测**：当前基于规则（V4）的维护虽零LLM成本，但难以捕捉语义冗余或复杂技能冲突。未来可引入轻量级嵌入相似度（如BGE）或小模型（如蒸馏LLM）进行低开销的语义一致性检查，平衡效率与深度。

2. **动态技能验证与选择**：论文指出CGPD未提升成功率，因为验证器字段未被任务时规划器消费。可探索将维护阶段产出的“风险/兼容性标签”动态注入检索或规划过程（如基于条件拒绝采样），使维护结果直接指导技能选择。

3. **真实长期部署评估**：当前仅基于半合成ALFWorld库，未考虑技能库随时间涌现的隐式依赖（如用户偏好的风格迁移）。未来需在真实聊天日志或持续更新环境中评估，并应对技能版本冲突与回滚问题。

4. **自适应维护策略**：规则权重（如冗余检测阈值）当前固定。可结合库的演化统计（如技能调用频率、失败率）自动调整维护参数，形成“维护元学习”机制。

### Q6: 总结一下论文的主要内容

本文提出SkillOps，用于管理大语言模型代理的技能库中的“技能技术债务”——即库级别持续性缺陷（如冗余、缺失验证、接口漂移等）。问题定义在于现有方法主要关注任务时的检索、规划与修复，而忽视库维护时机。SkillOps将每个技能表示为带类型（前提、操作、产物、验证器、失败模式）的Skill Contract，并组织成分层技能生态系统图（HSEG），从效用、兼容性、风险、验证等维度诊断库健康度。方法上，它是一个与代理无关的即插即用维护框架，接收原始技能库，输出经过清理的库，无需修改下游检索或规划代理的内部代码。主要结论：在ALFWorld上，SkillOps作为独立代理实现79.5%任务成功率，比最强基线高8.8个百分点且无额外LLM调用；作为插件层，使检索密集型基线提升0.68-2.90个百分点；规则化维护几乎零库时LLM开销。这表明技能库应被视作可管理的软件资产，而非静态检索池。
