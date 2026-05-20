---
title: "Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries"
authors:
  - "Xing Zhang"
  - "Yanwei Cui"
  - "Guanghui Wang"
  - "Ziyuan Li"
  - "Wei Qiu"
  - "Bing Zhu"
  - "Peiyang He"
date: "2026-05-19"
arxiv_id: "2605.19576"
arxiv_url: "https://arxiv.org/abs/2605.19576"
pdf_url: "https://arxiv.org/pdf/2605.19576v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.SE"
tags:
  - "Agent Skills Library"
  - "Self-Evolving Agent"
  - "Failure Diagnosis"
  - "Skill Retrieval"
  - "Agent Governance"
relevance_score: 9.0
---

# Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries

## 原始摘要

Self-evolving skill libraries face a silent failure mode we term \emph{library drift}: unbounded skill accumulation without outcome-driven lifecycle management causes retrieval degradation, false-positive injections, and performance stagnation. Recent evaluation confirms the symptom--LLM-authored skills deliver +0.0pp gain while human-curated ones deliver +16.2pp (SkillsBench)--yet the underlying mechanism has not been isolated. We provide (1) a reproducible trigger: ablations that isolate drift--one disables skill injection (flat floor, +0.002), one imposes premature retirement (active harm, $-$0.019); (2) trace-level diagnostics: an append-only evidence log with per-skill contribution scores, attribution verdicts, and router engagement metrics that make the failure visible before it reaches end-task scores; and (3) a verified fix: a minimal governance recipe (outcome-driven retirement + bounded active-cap + meta-skill authoring prior) that lifts held-out pass@1 from a 0.258 baseline to a late-window mean of 0.584 (rolling gain $+$0.328) on MBPP+ hard-100 over 100 rounds. Eight ablations decompose which governance mechanisms are load-bearing and which are subsumed, providing a concrete playbook for diagnosing library drift in any self-evolving agent.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决自进化大语言模型技能库中一个被忽视的失效模式——“库漂移”问题。研究背景是，基于Voyager等工作的自进化技能库允许冻结的LLM智能体在不更新权重的情况下积累可复用的程序性知识，理论上应能通过技能积累加速后续任务。然而，现有方法的不足在于，实际表现中LLM自生成的技能带来的性能提升为0%（相对于无技能基线+0.0个百分点），而人工筛选的技能则能带来+16.2%的提升。最新调查也表明，超过20个此类系统普遍缺乏生命周期管理（如版本控制、冲突检测、废弃机制）。本文要解决的核心问题是：当技能库无限制增长且缺乏基于结果的退出机制时，会导致检索精度下降、注入过时或有害的指导，智能体有效性能停滞甚至低于无技能基线。这种失效是“沉默”的，因为最终任务指标缓慢下降而无显式错误信号，因此需要从轨迹级诊断暴露问题。论文通过可复现触发条件（消融实验）、轨迹级诊断日志（证据日志与归因）和已验证的修复方案（Ratchet治理方案），系统性地诊断并修复了这一漂移问题。

### Q2: 有哪些相关研究？

相关研究可分为三类。**方法类**工作包括：Voyager开创了不断增长的技能库；ExpeL从轨迹提取文本洞察但缺乏结果驱动的淘汰机制；AutoManual编制操作手册；CASCADE在元技能上叠加累积创建；AutoSkill添加版本控制但未按任务贡献进行淘汰。EvolveR将轨迹蒸馏为战略原则；Trace2Skill从跟踪池诱导技能；Strategy Genes将失败历史附加为元数据。本文与这些工作的根本区别在于引入了结果驱动的淘汰机制和有限活跃容量，这是阻止库漂移的关键组件。**失效模式类**研究关注工具使用、规划和自我纠正中的失败，但库漂移是持续跨任务记忆特有的新失效模式。与权重更新系统中的灾难性遗忘不同，库漂移是冻结点权重对应物：累积的持久技能工件替换神经网络权重作为退化基质。**诊断信号类**工作中，LLM-as-judge在人类偏好上达到>80%一致性，本文将其扩展为每个技能的归属判定（帮助/伤害/中性），需≥3次共享规范模式的失败才生成新技能，实现了比事后评估器更早的预警。

### Q3: 论文如何解决这个问题？

论文提出了一种名为 Ratchet 的治理机制来修复自进化技能库的“库漂移”问题。其核心方法是引入三个关键组件：**结果驱动的淘汰机制**、**有界活跃容量**和**元技能创作约束**。整体框架是一个单智能体循环，其中冻结的语言模型负责编写、检索、管理和淘汰自己的自然语言技能。

首先，**结果驱动的淘汰机制**直接针对“无质量信号积累”阶段。当一个技能积累了足够多的试验次数（默认为100次）且其经验贡献度低于阈值（默认为-0.10）时，该技能会被淘汰。淘汰阈值经过精心设计，在随机噪声和有害技能清除之间取得平衡（霍夫丁界限约为0.20），确保有用技能存活，同时逐步移除有害技能。

其次，**有界活跃容量**（硬性上限，默认50个技能）直接缓解“检索退化”问题。当新技能合成会导致技能库超出上限时，规划器会强制淘汰贡献最低的技能。通过限制技能库大小，检索精度不会因技能无限增长而下降。这两者结合提供了形式化的非发散保证：在有限容量和淘汰阈值下，期望评估指标不会无限劣化。

最后，**元技能文档**从源头解决“静默注入伤害”。它约束合成器生成风格一致的技能，从而提高技能的结构同质性，减少有害或冗余技能的生成，有效减轻了下游淘汰的负担。消融实验表明，移除元技能会导致默认方案43%的性能损失，是单最有价值组件，而显式的去重机制（如模式规范化）在该设定下被元技能所覆盖，不是必需的。

### Q4: 论文做了哪些实验？

论文在MBPP+ hard-100基准上进行实验，该基准从MBPP+测试集中剔除了Claude Opus 4.7全部答对的约273题，保留100个有难度的题目（60训练/40评估）。所有LLM调用使用Claude Opus 4.7，嵌入使用Cohere embed-v4，Solver为单次直接调用（无执行反馈或工具使用）。运行100轮，报告3个种子的均值±标准差。

默认配置（完整治理）将held-out pass@1从0.258基线提升至0.584的晚期窗口均值（峰值0.658），增益+0.328。对比实验包括：A1（无技能注入）建立无技能基线，增益仅+0.002；A2（仅检索路由）增益+0.077，验证LLM门控的重要性；A3（无元技能）增益+0.187，表明元技能是最关键组件（缺失损失-0.141）。A4（激进淘汰）将Nmin降至20，τ设为0.0，导致增益-0.019，低于无技能基线，验证了证据不足时淘汰规则的危害。A5（无规范化）增益+0.374，A6（无覆盖防护）增益+0.363，两者均略超默认，表明元技能的作者指导风格一致性使显式去重产生过多误判。A7（容量100）增益+0.317但方差显著增大（±0.110 vs ±0.018），表明容量主要控制方差。A8（元技能刷新）增益+0.372（峰值0.725），但耗时增加55%（10.1小时 vs 6.5小时），计算开销不合理。

### Q5: 有什么可以进一步探索的点？

论文的局限性首先体现在仅使用单一基准（MBPP+ hard-100）和单一模型（Claude Opus 4.7），未来需要在多步智能体（如SWE-Bench）和不同模型上验证库漂移现象的普遍性与治理策略的鲁棒性。诊断阈值目前基于经验选择，未来可探索基于贝叶斯方法或强化学习的自适应阈值校准机制，使干预决策更可靠。此外，论文假设漂移信号（如贡献分数和“伤害”判定）在多步智能体中会更敏感，因为可定位到具体步骤的损害，这需要实证验证。从更广视角看，库漂移作为一种通用失败模式，其诊断框架（每件贡献分数、归属判定、路由器参与度）可推广到规则系统、工作流记忆等，但如何将这些指标标准化并整合进现有智能体评估体系仍是挑战。改进方向包括：设计动态容量上限而非固定值，引入元技能自更新机制以适应任务分布变化，以及利用离线强化学习从历史轨迹中预筛负面技能，而非被动等待诊断信号触发。

### Q6: 总结一下论文的主要内容

论文针对自进化技能库中存在的“库漂移”这一无声故障模式展开研究。该问题表现为技能库无限制积累、缺乏结果驱动的生命周期管理，导致检索退化、误报注入和性能停滞。实验表明，无治理时LLM生成的技能收益为+0.0pp，而人工策划则达+16.2pp。作者通过三项核心贡献解决了该问题：首先，提供了可重复的触发机制（禁用技能注入导致+0.002，过早淘汰技能造成-0.019的主动伤害）；其次，建立了痕迹级诊断系统，通过技能贡献分数、归因判定和路由器参与指标在端任务指标下降前检测故障；最后，提出了最小治理方案（结果驱动淘汰+有界活跃容量+元技能创作先验），将MBPP+ hard-100的pass@1从0.258提升至0.584（滚动增益+0.328）。八项消融实验验证了淘汰和元技能机制的关键作用。该研究的核心意义在于揭示了自进化智能体的原始创作瓶颈不在于作者而在于管理员，通过系统化生命周期管理可显著提升性能，为诊断任意自进化系统中的库漂移提供了可迁移的实践指南。
