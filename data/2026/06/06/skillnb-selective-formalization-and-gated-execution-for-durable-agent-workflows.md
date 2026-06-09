---
title: "SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows"
authors:
  - "Amine El Hattami"
  - "Nicolas Chapados"
  - "Christopher Pal"
date: "2026-06-06"
arxiv_id: "2606.08049"
arxiv_url: "https://arxiv.org/abs/2606.08049"
pdf_url: "https://arxiv.org/pdf/2606.08049v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "Web Agent"
  - "Agent Workflow"
  - "Memory/Experience Reuse"
  - "Lifecycle Management"
  - "Gate-Conditioned Execution"
  - "Selective Formalization"
  - "Benchmark Evaluation"
relevance_score: 9.5
---

# SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows

## 原始摘要

AI agents increasingly turn past experience into reusable artifacts such as code, workflows, and procedural memories. Reuse can improve efficiency, but it also creates a lifecycle reliability problem: artifacts that succeed once may fail under environment drift, underspecified tasks, or changing task distributions, especially in web automation. We introduce SKILL.nb, a framework for governing reusable agent workflows with evidence-calibrated lifecycle policies. SKILL.nb uses selective formalization: execution evidence decides which workflow steps should become executable code, which should remain natural-language guided, and when those choices should be revised. Workflows are stored as auditable, versioned notebooks that interleave natural-language guidance, multi-language executable cells, validation gates, fallback paths, and multimodal evidence such as outputs, screenshots, and error traces. At runtime, gate-conditioned execution lets each step run code when its gates validate, or fall back locally when drift invalidates the executable realization. On WebArena-Verified, SKILL.nb achieves 53.7% single-round success, improving over the strongest baseline by 3.9 percentage points. Across three re-executions, it retains 91.7% of initially successful tasks, 15.5 points above the next best method. Under bounded repair, it recovers 72.9% of subsequent failures while limiting post-repair regressions to 4.2%, compared with 15.0% to 17.0% for persistent baselines. It also leads on Mind2Web cross-website and cross-domain splits. In a GitLab migration test, SKILL.nb preserves performance when reusing frozen state learned on GitLab 15.7, with frozen-versus-fresh target-version gaps of -1.7 points on GitLab 16.11 and +0.6 points on GitLab 18.9. These results identify lifecycle governance and gate-conditioned execution as reliability axes beyond one-shot task success.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决AI代理在重复使用其生成的可复用工件（如代码、工作流和程序性记忆）时面临的“生命周期可靠性”问题。研究背景是，现有代理系统越来越依赖从过往经验中提取工件来提升效率，但频繁复用会引入软件维护式的生命周期隐患。现有方法的不足在于：1）记忆中心系统通常仅将经验作为提示词上下文复用，缺乏验证与版本控制；2）工作流与工件系统虽然提供了执行、验证或状态管理等独立组件，但缺乏将这些机制协同起来作为联合生命周期策略；其核心挑战是，当环境发生漂移（如网站UI更新）、任务说明不明确或任务分布变化时，工件可能失效。在网页自动化这一高漂移场景中，问题尤为突出。因此，本文要解决的核心问题是：如何利用积累的执行证据来对可复用的代理工作流进行全生命周期的治理，即决定何时将工作流发布或停用、何时将一个步骤从自然语言引导的提案形式化为可执行代码、何时修复或降级脆弱的实现，以及何时将不再满足假设的工作流停用。

### Q2: 有哪些相关研究？

本文的主要相关研究可分为三类：**智能体经验记忆**、**自演化智能体**和**持久性工件管理**。

在经验记忆方面，相关工作如Synapse、ExPeL、MemP以及Agent Workflow Memory（AWM）和ReasoningBank，都将过往经验（如原始轨迹、程序性洞察或可复用工作流）作为提示上下文来指导生成。与这些依赖随机LLM判断的“顾问式”记忆不同，SKILL.nb将记忆转变为可执行、可验证、受版本控制的工件，并通过确定性验收检查来执行，实现了从被动提示到主动执行与治理的跨越。

在自演化智能体方面，Voyager和TroVE通过探索构建可执行代码的技能库以实现持续适应。然而，它们缺乏严格的生命周期门控，单一错误更新可能悄无声息地破坏未来行为。SKILL.nb通过强制离线验证和确定性门控检查来治理演化，允许在性能回退时安全回滚，弥补了这一关键风险。

在持久性工件管理方面，ALAS、AgentGit、Atomix及ReUseIt等系统通过版本日志、状态检查点或事务语义管理工件。但ReUseIt的验证依赖随机LLM分析截图，其他系统在故障时则高度依赖人工介入。SKILL.nb的独特之处在于，它完全通过离线确定性门控检查和重放校准来管理工件生命周期，替代了前者的随机运行时验证和后者的手工监督。总的来说，SKILL.nb将先前工作中的孤立原语（记忆、工作流程归纳、工件治理）整合为一个统一的生命周期框架。

### Q3: 论文如何解决这个问题？

SKILL.nb通过选择性形式化和门控执行来管理可复用的Agent工作流。核心架构是一个版本化笔记本系统，它将自然语言指导与可执行代码单元交错存储，每个步骤包含意图I_i、自然语言过程P_i、可选可执行代码C_i、验证门Γ_i和元数据。

整体框架包含离线维护和在线执行两个阶段。离线阶段使用基于阈值的生命周期策略π_θ，通过四种信号驱动生命周期动作：创建、形式化（NL→代码）、降级（代码→NL）和退役。阈值通过历史日志的回放估计优化维护成本与违规率的权衡，并采用分组自适应阈值处理数据稀疏性问题。

关键技术包括：1) 证据校准的选择性形式化，根据执行证据决定步骤应使用代码还是自然语言引导；2) 门控执行，运行时检查预/后置条件门γ_pre和γ_post，失败时按C_i→P_i→I_i级联回退；3) 回放验证过滤，通过Wilson置信上限确保阈值动作的安全性；4) 受RLVR启发的执行证据信号，用于工件治理而非模型权重更新。

创新点在于将生命周期治理作为可靠性维度，通过验证门控的版本化工件更新保持稳定性，在WebArena上达到53.7%成功率，三次重执行保持91.7%成功率，且修复后回归仅4.2%。

### Q4: 论文做了哪些实验？

论文进行了多维度实验评估。首先，在WebArena-Verified的812个任务上测试单轮性能，SKILL.nb以53.7%的成功率领先，超过最强基线ReasoningBank 3.9个百分点（p=0.029）。在Mind2Bench上，它分别在跨网站和跨领域分片中取得最佳元素准确率（46.8%/44.9%）、动作F1（54.3%/46.0%）、步骤成功率（38.1%/39.7%）和任务成功率（4.1%/1.9%）。其次，在生命周期可靠性测试中，经过三轮扰动重执行，SKILL.nb保持91.7%的重用一致性，远超次优方法（76.2%）；在故障修复中，它以72.9%的恢复率和仅4.2%的回归率优化了修复-回归权衡，而基线回归率达15-17%。在GitLab迁移实验中，对比实际UI漂移下的冻结状态复用，SKILL.nb在GitLab 18.9上实现了61.7%的冻结复现成功率（新鲜启动为61.1%），而传统记忆基线出现显著负迁移（退化11-14点）。消融实验验证了门控执行、选择性形式化等机制的有效性。

### Q5: 有什么可以进一步探索的点？

SKILL.nb的局限性主要集中在生命周期决策依赖日志证据、验证门控质量以及成本度量不够全面。未来可从以下方向探索：1）改进选择性形式化的动态性，例如引入在线学习机制让系统在不依赖固定阈值的情况下自适应调整代码与NL的边界，或者采用强化学习优化提拔与降级策略。2）增强验证门的鲁棒性，针对门控错误或稀疏重复任务，可设计概率性门控或集成多种校验信号（如视觉一致性检查），避免因单一证据失效导致执行崩溃。3）扩展生命周期管理的范畴，不仅关注代码的版本化，还可对NL指导、验证逻辑及回退路径本身进行自治更新，形成真正的元生命周期管理。4）在成本代理上融合延迟、存储和人工干预等实际指标，更准确地衡量维护开销。5）将框架推广到多智能体协作场景，研究不同智能体间共享工作流的版本冲突与一致性保障，进一步提升在长期部署中的可靠性。

### Q6: 总结一下论文的主要内容

本文提出SKILL.nb框架，旨在解决AI代理工作流在环境漂移下的生命周期可靠性问题。核心贡献在于引入“选择性形式化”机制：基于执行证据决定工作流步骤应转化为可执行代码、保留自然语言指导，或何时修订这些选择。同时采用“门控执行”策略，运行时通过验证门决定执行代码或回退到自然语言过程。工作流存储为可审计的版本化笔记本，整合自然语言、多语言代码、验证门、回退路径及多模态证据。主要结论显示，在WebArena-Verified上，SKILL.nb单轮成功率达53.7%，比最强基线高3.9个百分点；三轮重执行中保留91.7%的初始成功任务；有限修复后恢复72.9%的后续失败，回归率仅4.2%。在GitLab迁移测试中，重用冻结状态时性能几乎无损。该研究将工作流治理从一次性任务完成扩展至持续可靠性维护，表明耐久代理工件需作为生命周期管理对象，其晋升、修复和退役应由执行证据驱动。
