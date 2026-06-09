---
title: "Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory"
authors:
  - "Haoran Sun"
  - "Wenjie Li"
  - "Yujie Zhang"
  - "Zekai Lin"
  - "Fanrui Zhang"
  - "Kaitao Chen"
  - "Xingqi He"
  - "Yichen Li"
  - "Mianxin Liu"
  - "Lei Liu"
  - "Yankai Jiang"
date: "2026-06-08"
arxiv_id: "2606.09365"
arxiv_url: "https://arxiv.org/abs/2606.09365"
pdf_url: "https://arxiv.org/pdf/2606.09365v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "医疗Agent"
  - "技能记忆"
  - "自进化框架"
  - "临床决策"
  - "多分支记忆库"
  - "持续学习"
  - "可迁移技能"
relevance_score: 9.5
---

# Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory

## 原始摘要

Medical agent systems are increasingly expected to support interactive clinical decision making rather than only static question answering. In such settings, effective agents must reuse prior experience across evolving cases, yet existing memory mechanisms often retain raw historical traces that are redundant, noisy, and difficult to govern. More importantly, they rarely distinguish which memories are truly useful for future reasoning. This limits their ability to accumulate compact and reliable experience for long-horizon clinical reasoning. To close this gap, we propose SkeMex, a post-deployment self-evolution framework that improves medical agents through a skill-based memory without updating model weights. SkeMex distills informative interaction trajectories into structured skills that encode reusable procedural knowledge, and organizes them into a multi-branch repository spanning general, task-specific, and action-level experience. To determine which memories should be reused and retained, SkeMex estimates context-dependent utility from environment feedback and uses it to guide value-aware retrieval and repository governance. A closed-loop ``Read--Write--Assess--Govern" lifecycle further supports continual evolution by writing new skills, updating utilities, promoting useful memories, and removing harmful entries. Experiments across diverse clinical tasks show that SkeMex consistently outperforms representative memory-based agents in both offline and online settings. It also generalizes across model backbones and supports transferable skill memory. All data and code will be released publicly.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决医疗智能体系统在动态、多步临床决策中经验复用能力不足的问题。研究背景是现有医疗大语言模型多聚焦于静态、单轮问答任务（如MedQA、MedMCQA），但真实临床决策需要智能体在不确定性下进行持续交互、证据收集和多轮推理。现有方法的不足体现在两方面：一是大多数记忆增强方法仅保留原始交互轨迹，这些冗余、噪声化的历史记录使得记忆库臃肿且难以管理；二是缺乏对记忆长期有效性的评估机制，无法区分哪些经验对未来推理真正有用，导致低质量或有害记忆的累积，限制了跨案例泛化能力。此外，部分方法将记忆改进与模型参数更新耦合，带来高昂计算成本和灾难性遗忘风险。核心问题是如何在不更新模型权重的前提下，构建一个能够自主进化、动态评估并持续优化记忆的智能体框架，使其能够从过往交互中提取紧凑、可复用的技能型经验，并在多样化的临床任务中实现可靠的经验复用与泛化。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及两类工作：LLM-based Medical Agents和自进化记忆机制。

首先，在LLM-based Medical Agents方面，现有系统如i-MedRAG、EHRAgent、MedAgents等虽在特定任务上表现强劲，但普遍缺乏积累可重用经验的机制。近期工作如Agent Hospital、AMC、STELLA等开始引入记忆和自我改进，但往往将记忆绑定到特定工作流或使用启发式规则组织过去案例，限制了跨任务泛化。相比之下，SkeMex将记忆演进与固定工作流解耦，通过提炼可复用技能并基于环境反馈选择性保留高价值经验，实现持续跨任务学习。

其次，在自进化记忆机制方面，早期系统存储原始轨迹或反思指导行动，近期工作如Agent Workflow Memory、GSEM、HealthFlow等转向结构化模块设计。Trace2Skill、SkillClaw等表明轨迹可蒸馏为分层技能库，但管理技能记忆仍具挑战。SkillRL等方法将技能演进融入策略训练需要参数更新，在医疗领域可能导致灾难性遗忘。SkeMex则通过估计技能效用并指导存储治理，在不更新模型参数的情况下演进技能库，兼顾了可靠性。

### Q3: 论文如何解决这个问题？

SkeMex通过一个名为“技能记忆”的自我进化框架来解决医疗智能体在长期临床推理中难以积累和复用可靠经验的问题。其核心是构建一个持续演进的技能仓库（Skill Repository），将冗余、噪声化的原始交互轨迹蒸馏为结构化的、可复用的程序性知识，并组织为通用、任务级和动作级三个分支，实现不同抽象层次经验的分离管理。

整体框架遵循“读取-写入-评估-治理”的闭环生命周期：
1. **读取阶段**：采用值感知检索（Value-aware Retrieval）。首先通过临床类别路由（Clinical Category Routing）缩小检索范围，然后结合语义相似度、历史效用（Utility）和基于艾宾浩斯遗忘曲线的时间衰减信号进行多通道筛选与排序，并确保三个分支的平衡选择。
2. **写入阶段**：引入门控轨迹缓冲器（Gated Trajectory Buffer），过滤掉无意义的交互，保留包含多步推理或信息性失败的轨迹。随后通过分析-突变双过程（Analysis-Mutation Pass）将轨迹蒸馏为技能草稿，并通过新颖性和质量门控审核，决定是创建新技能、补丁更新现有技能还是忽略。
3. **评估阶段**：采用窗口级估值（Window-level Valuation），通过相对优势函数（Relative Advantage）为技能分配公平的信用，避免绝对奖励的噪声。对于每个临床类别，维护一个指数移动平均奖励作为基线，以此计算轨迹优势，并根据技能采用事件（积极、消极或忽略）对其进行正负赋值，实现鲁棒的效用更新。
4. **治理阶段**：定期应用仓库治理（Repository Governance）操作，合并冗余技能、移除低效用技能，并限制每个分支的容量，维持仓库的紧凑性和可靠性。

关键创新点在于：1）将技能效用与具体临床类别关联，支持细粒度的值感知检索；2）通过风险敏感正则化（Risk-sensitive Regularizer）抑制高风险技能积累不良行为；3）整个框架不更新模型参数，仅通过操作经验仓库实现持续进化。

### Q4: 论文做了哪些实验？

论文在九个医学基准上评估了SkeMex，涵盖临床交互和知识密集型推理。数据集包括AgentClinic、LiveClin、MedJourney、LiveMedBench、HealthBench、MediQ以及MedXpertQA、MMMU和MMMU-Pro（后两者仅用健康与医学子集）。实验设置分为离线模式和在线模式：离线模式从静态训练集构建技能库并在域内和域外数据上测试；在线模式则将每个基准视为流式任务序列，技能库在交互中动态更新。对比方法包括医疗专家模型、无记忆ReAct智能体、检索增强反思方法（如Reflexion、CRITIC）以及自我改进记忆智能体（如Voyager、DILU、ExPeL、GM、Memp、SkillWeaver、AWM、Agent KB、Evolver、DC、MobileE、CFM、GSEM）。主要结果：在离线域内评估中，SkeMex在DeepSeek-V3.2上将ReAct从48.20%提升至56.08%（+7.88点），在Qwen3.6-Plus上从48.63%提升至59.22%（+10.59点），均优于所有基线。在线模式中，SkeMex从epoch@1的76.39%持续提升至epoch@3的78.56%，而最强基线Evolver仅达76.97%。消融实验表明，缓冲区门控和技能编码质量对表现至关重要，完整SkeMex平均得分为53.22%，而去除缓冲区门控后降至47.56%。指标包括精确匹配准确率和基于临床标准的评分。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于技能记忆的泛化性高度依赖环境反馈的质量和一致性。当前框架通过上下文依赖效用评估筛选经验，但在真实临床场景中，反馈可能稀疏、延迟或包含噪声（如医生偏好差异），导致效用估计偏差。未来可探索以下方向：1）引入主动学习机制，在不确定状态下主动询问专家以获得高价值反馈，加速效用收敛；2）设计跨任务技能抽象层，将动作-状态轨迹映射为高阶语义模式（如“鉴别诊断策略”），降低对底层环境特征的敏感度；3）结合元学习，使技能存储的“写入-评估”过程自身具备可进化能力，例如通过重放缓冲区的优先级采样动态调整效用阈值。此外，当前多分支仓库的固定结构可能阻碍异构经验整合，可借鉴动态路由机制让代理自主生成分支拓扑，从而适应新型临床推理范式。

### Q6: 总结一下论文的主要内容

SkeMex提出了一个无需更新模型权重的后部署自我进化框架，旨在解决现有医疗代理系统中记忆机制存在的冗余、噪声和实用性评估缺失问题。其核心贡献在于将交互轨迹蒸馏为结构化技能，并组织成包含通用、任务特定和动作级别的多分支知识库。SkeMex通过从环境反馈中估算上下文相关的效用值，实现价值感知的技能检索和库治理，并引入“读-写-评估-治理”闭环生命周期来持续促进有用记忆、淘汰有害条目。实验表明，该方法在多种临床任务中一致优于现有基于记忆的代理，并能跨模型主干泛化，支持可转移的技能记忆，为开发无需重训练就能持续进化的医疗人工智能系统提供了新方案。
