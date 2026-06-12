---
title: "SkillCAT: Contrastive Assessment and Topology-Aware Skill Self-Evolution for LLM Agents"
authors:
  - "Kunfeng Chen"
  - "Qihuang Zhong"
  - "Juhua Liu"
  - "Bo Du"
date: "2026-06-11"
arxiv_id: "2606.13317"
arxiv_url: "https://arxiv.org/abs/2606.13317"
pdf_url: "https://arxiv.org/pdf/2606.13317v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Skill Self-Evolution"
  - "Contrastive Extraction"
  - "Agent Memory"
  - "Agent Benchmark Evaluation"
  - "Training-free Agent Framework"
relevance_score: 9.5
---

# SkillCAT: Contrastive Assessment and Topology-Aware Skill Self-Evolution for LLM Agents

## 原始摘要

Skill self-evolution methods for LLM agents aim to turn execution trajectories into reusable skill documents, but current pipelines typically learn from one trajectory per task, merge candidate skill patches before checking them, and load the full skill corpus before inference. We propose SkillCAT, a training-free framework that separates this process into three stages. Contrastive Causal Extraction (CCE) samples multiple trajectories for each task and compares same-task success/failure pairs to identify evidence that explains outcome differences. Assessment-Augmented Evolution (AAE) replays each candidate patch on source-task clones and keeps only patches that improve or preserve task outcomes before hierarchical skill patch merging. Topology-Aware Task Execution (TTE) compiles the evolved skills into a routable sub-skill topology, so inference loads only the capability nodes relevant to the task. We evaluate SkillCAT on common agent benchmarks, including SpreadsheetBench, WikiTableQuestions, and DocVQA, and further test cross-model and out-of-distribution generalization. Across these settings, SkillCAT raises the average score over baselines by up to 40.40%, demonstrating reliable skill evolution without model training.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文针对LLM智能体技能自我演化方法中的三个核心问题展开研究。现有方法（如Trace2Skill）遵循离线批处理管道，从单条执行轨迹提取技能补丁并进行合并，但存在以下不足：1）单轨迹偏差（Single-Trace Bias）：单条成功轨迹可能反映偶然策略，而失败轨迹难以定位根本原因，导致证据不充分；2）未经验证的合并（Unvalidated Merging）：候选补丁直接合并前未独立检验其对源任务的帮助，导致低质量或有害补丁混入技能库；3）上下文过载（Context Overload）：技能库持续增长，推理时向智能体提供无关或冲突的规则，增加提示长度并干扰任务相关内容的聚焦。为解决这些问题，论文提出SkillCAT框架，这是一个无需训练的框架，将技能生命周期分离为三个阶段：对比因果提取（CCE）通过多采样生成同任务成功/失败对比对，提取因果分水岭处的关键证据；评估增强演化（AAE）在源任务克隆上回放每个候选补丁，筛选出能改善或保持任务表现的补丁并进行分层合并；拓扑感知任务执行（TTE）将演化后的技能编译为可路由的子技能拓扑，推理时仅加载任务相关节点。核心目标是在不进行模型训练的前提下，实现可靠、高效的技能自我演化与部署。

### Q2: 有哪些相关研究？

相关研究可分为两类：

1. **Agent和技能组织方法**：Graph of Skills和GraSP建模技能依赖与前置条件，SkillRAE构建检索上下文，SkillsBench和SkillLearnBench评估跨任务使用与持续获取能力。这些工作假设已有高质量技能库，而本文SkillCAT关注如何从执行经验中自主提取可靠技能，并在测试时仅暴露任务相关部分。

2. **技能提取与演化方法**：Trace2Skill通过Map-Reduce从轨迹提取局部补丁并合并为技能文档。后续工作扩展了技能来源（多模态经验、个性化交互）、内存维护、质量控制（坏例诊断、替代验证、对比执行、聚合信号）及强化学习等方法。这些工作通常将经验提取、补丁验证与技能选择分离处理。

SkillCAT的创新在于：通过CCE对同任务多条轨迹的正误对比提取因果证据；AAE在合并前对候选补丁进行源任务重播验证，仅保留改进或保持效果的补丁；TTE构建可路由的子技能拓扑，推理时只加载任务相关能力节点。这种方法将三个环节有机整合，无需模型训练即可实现40.40%的性能提升。

### Q3: 论文如何解决这个问题？

SkillCAT通过一个三阶段的无训练框架解决了LLM Agent技能自演化中的三个关键问题：低效的经验提取、缺乏验证的合并策略以及完整的技能加载。核心方法分为以下三个阶段：

1. **对比因果提取（CCE）**：针对每个任务采样多条轨迹，构造同任务的成功/失败对比对。通过定位因果分水岭（即首次行为差异点），提取仅聚焦于该差异点的局部证据、推断的失败原因和可编辑的经验记录。当所有轨迹结果一致时，采用单轨迹提取作为回退机制。这避免了将任务难度差异误判为技能证据。

2. **评估增强演化（AAE）**：将每个候选技能补丁视为待验证的假设，通过在源任务克隆上回放并评分（成功→失败得0分，失败→成功得3分），仅保留改善或保持任务表现的补丁（阈值θ=2.0）。通过分层分级合并策略，优先合并高分补丁，确保演化后的技能不会破坏已有的成功行为。

3. **拓扑感知任务执行（TTE）**：将演化后的技能编译成可路由的子技能拓扑结构，包含始终加载的核心技能和可路由的节点集合。在推理时，通过LLM路由器根据任务描述选择最多k个相关节点，结合确定性扩展（添加依赖和基础节点），只加载与当前任务相关的技能片段，避免完整技能加载带来的上下文干扰。

该框架的核心创新在于：对比式因果提取确保了经验的可信度；评估增强的验证机制防止了劣质补丁的混入；拓扑感知的技能路由实现了轻量化的测试时技能加载。实验表明，SkillCAT在SpreadsheetBench、WikiTableQuestions等基准测试中，相比基线方法平均分提升了最高40.40%，并展现出良好的跨模型和分布外泛化能力。

### Q4: 论文做了哪些实验？

SkillCAT在多个基准上进行了实验。主要数据集为SpreadsheetBench-Verified，400样本按200个演化/200个测试拆分，主指标为held-out准确率（VRF）；同时在完整SpreadsheetBench上报告Soft和Hard指标。跨领域泛化使用了WikiTableQuestions（转换为电子表格格式）和DocVQA（前2700对用于演化，剩余2649对评估，报告ANLS和Acc）。对比方法包括No Skill、Human-Written（Anthropic官方xlsx技能）、Parametric（提示生成的xlsx-basic）以及Trace2Skill的+Combined和+Error变体。实验设置两种初始化：Skill Deepening（从Human-Written开始）和Skill Creation（从xlsx-basic开始）。主要使用Qwen3.5-35B-A3B和Qwen3.5-122B-A10B作为技能作者和用户，跨模型测试使用gemma-4-31B-it和gpt-5.4-mini。关键结果：在Skill Deepening中（Qwen3.5-35B），SkillCAT Full达到55.50% VRF，比Trace2Skill +Combined（29.67%）高25.83个百分点；在Skill Creation中（Qwen3.5-35B），SkillCAT达到54.50%，比Parametric高34.33个百分点。消融实验表明每个模块都不可或缺：移除CCE使VRF降至32.50%，移除AAE降至26.00%，移除TTE降至46.50%。AAE验证显示：将失败转为成功的补丁表现最佳（51.00% VRF），而将成功转为失败的补丁最差（23.50%）。TTE实现了41.6%的上下文缩减，同时VRF提升至55.50%。DocVQA上，SkillCAT Full在Qwen3.5-35B上达到0.9159 ANLS和93.3% Acc，优于所有基线。

### Q5: 有什么可以进一步探索的点？

尽管SkillCAT在技能自演化方面取得了显著进展，但仍有几个值得深入探索的方向。首先，该方法依赖同一任务的多条轨迹进行对比提取，在冷启动场景下可能面临轨迹稀缺问题，未来可研究如何结合弱监督或合成数据生成初始轨迹。其次，AAE模块在源任务克隆上验证候选补丁，但可能难以推广到分布偏移场景，建议引入跨任务迁移验证机制。第三，TTE构建的子技能拓扑路由表目前仅通过相关性筛选，可进一步结合强化学习动态优化路径选择。此外，框架虽然避免训练，但多轮轨迹采样和验证增加了推理成本，高效采样策略（如主动学习）值得尝试。最后，当前评估限于表格和文档理解任务，可拓展到更复杂的决策场景（如web导航或机器人控制），并探索技能文档的跨智能体共享与可解释性分析。

### Q6: 总结一下论文的主要内容

这篇论文提出SkillCAT，一种无需训练的大语言模型智能体技能自我进化框架。现有方法存在三个问题：单次轨迹偏差、未经验证的合并以及推理时上下文过载。SkillCAT通过三阶段解决这些问题：对比因果提取(CCE)对同一任务采样多条轨迹，对比成功/失败案例，识别导致结果差异的关键证据；评估增强进化(AAE)在源任务副本上回放候选补丁，仅保留能改善或保持结果的补丁，然后分层合并；拓扑感知任务执行(TTE)将进化后的技能编译成可路由的子技能拓扑，推理时仅加载与任务相关的能力节点。在SpreadsheetBench、WikiTableQuestions和DocVQA等基准测试上，SkillCAT相比基线将平均分数提升高达40.40%，并展示了跨模型和分布外泛化能力。核心贡献在于提出了一种可靠的无训练技能自我进化方法，有效解决了现有方法的关键局限性。
