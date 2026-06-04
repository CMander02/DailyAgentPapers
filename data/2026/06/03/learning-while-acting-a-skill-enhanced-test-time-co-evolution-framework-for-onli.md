---
title: "Learning While Acting: A Skill-Enhanced Test-Time Co-Evolution Framework for Online Lifelong Learning Agents"
authors:
  - "Bo Mao"
  - "Jie Zhou"
  - "Yutao Yang"
  - "Xin Li"
  - "Xian Wei"
  - "Qin Chen"
  - "Xingjiao Wu"
  - "Liang He"
date: "2026-06-03"
arxiv_id: "2606.04815"
arxiv_url: "https://arxiv.org/abs/2606.04815"
pdf_url: "https://arxiv.org/pdf/2606.04815v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Lifelong Learning"
  - "Test-Time Adaptation"
  - "Skill Learning"
  - "Reinforcement Learning"
  - "Online Learning"
relevance_score: 9.5
---

# Learning While Acting: A Skill-Enhanced Test-Time Co-Evolution Framework for Online Lifelong Learning Agents

## 原始摘要

Lifelong learning is essential for Large Language Model (LLM) agents operating in dynamic, interactive environments. However, existing lifelong learning agents for long-horizon tasks typically depend on discrete skill or past experiences retrieval with static parameters during inference, which prevents them from continuously internalizing test-time feedback like human learners. To bridge this gap, we propose Skill-enhanced Test-Time Co-Evolution (\texttt{LifeSkill}), a two-stage reinforcement learning framework for Online Lifelong Learning Agents. Specifically, we design Verifier-Guided Skill Learning that addresses the lack of direct supervision for skill extraction by rewarding candidate skills according to the average verifier success of multiple skill-conditioned policy rollouts, encouraging the model to generate skills that are useful for solving tasks rather than merely plausible in text. Furthermore, we introduce Online Skill Internalization, which continuously improves the policy model during test-time interaction by transforming skill-conditioned trajectories into reward signals. This enables the agent to directly internalize reasoning capabilities into its parameters, avoiding the context bloat of experience retrieval. Experiments on LifelongAgentBench show that LifeSkill improves average performance by 7 absolute points by comparing with existing lifelong agent baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在线终身学习LLM代理在动态交互环境中无法像人类一样持续从测试时反馈中学习并内化技能的问题。现有的终身学习代理主要依赖离散技能检索或过往经验，在推理时保持参数静态，因此无法在部署过程中持续改进。具体而言，现有方法面临三个核心不足：第一，大多数代理在测试时固定模型参数，仅依靠外部记忆提升性能，阻止了真正的持续适应；第二，尽管先前工作能总结轨迹或生成反思，但如何从交互反馈中提取可复用技能仍缺乏基于执行结果的可靠监督；第三，获取的知识通常以离散的外部文本形式存在，难以被模型内化为参数化知识并进行组合与泛化。针对这些限制，本文提出LifeSkill框架，旨在通过两阶段强化学习实现代理在测试时的技能增强与策略进化。核心目标是让代理不仅能在失败中提取有用技能，还能将这些技能直接内化为模型参数，从而将测试时交互的反馈转化为持久的能力增长，避免外部记忆的上下文膨胀问题。实验表明，该方法在LifelongAgentBench上相比现有基线实现了7个百分点的平均性能提升。

### Q2: 有哪些相关研究？

相关研究可分为四类。**自演进LLM Agent**（如采用外部记忆或经验库的工作）通过轨迹范例、工作流记忆等增强Agent，但增益留在参数外，导致检索开销和上下文膨胀；本文通过在线参数更新内化能力，避免了上述问题。**测试时学习**方法（如分解、修订、搜索）通过增加推理计算提升性能，但收益是暂时的，无法持续吸收策略；本文保留测试时探索优势，但将其转化为未来能力的监督信号。**技能抽象**研究（如代码模块、工具调用）强调可复用行为的组合性与可解释性，但多依赖手动设计接口或离线积累；本文将技能作为中间学习接口，引导探索后内化回策略。**在线持续学习**（如正则化、回放、测试时适应）聚焦参数级知识保留与获取，但本文环境需在线交互且监督来自任务验证器而非偏好标签。此外，指令对齐与推理自我改进方法（如策略优化、基于验证器的学习）也相关，但本文更强调环境交互中的在线参数更新。LifeSkill的创新在于：通过执行验证器反馈学习技能提取、部署时在线更新参数、将技能引导的行为内化至原任务输入。

### Q3: 论文如何解决这个问题？

LifeSkill提出了一种两阶段强化学习框架，通过在线协同进化实现终身学习。整体框架包含两个同构但参数独立的模型：策略模型πθ和执行任务，技能提取模型πφ从失败交互中提炼可复用技能。两个模型通过两种强化学习机制耦合。核心创新点包括两个组件：第一是验证器引导的技能学习（VGSL），它解决技能提取缺乏直接监督的问题。具体做法是，当策略模型首次尝试任务失败后，技能提取模型采样多个候选技能，然后为每个技能执行多次技能条件策略展开，使用环境验证器的平均成功率作为技能质量的奖励信号。该奖励通过DAPO目标函数优化技能提取模型，使其生成能实际改进策略执行效果的技能，而非仅文本上合理的描述。第二是在线技能内化（OSI），它将技能条件轨迹转化为参数更新。对于验证成功的技能条件轨迹，OSI移除输入中的技能提示，仅保留原始任务查询，然后使用验证器奖励加权最大化策略模型在当前任务输入下生成该轨迹的对数似然。这样，有用的行为被直接吸收到模型参数中，避免了外部经验检索导致的上下文膨胀。两个组件形成协同进化循环：VGSL提升在线技能探索质量，OSI将发现的技能持久化为参数知识，使代理能在连续任务流中边执行边学习。实验显示LifeSkill在LifelongAgentBench上平均性能提升7个绝对点。

### Q4: 论文做了哪些实验？

论文在 LifelongAgentBench 基准上进行实验，该基准包含 Database (DB)、Operating System (OS) 和 Knowledge Graph (KG) 三个交互环境。对比方法分为两类：无训练方法（Vanilla、Self-Refine、Reasoning Bank、Group Self-Consistency、AWM）和基于训练的方法（RFT、SkillRL、DAPO），所有方法均使用 Llama-3.1-8B-Instruct 骨干网络。LifeSkill 采用双模型架构（策略模型与技能抽取模型），使用 LoRA 适配器（rank=32, α=64），在线更新时采用 DAPO token 级裁剪目标（裁剪范围0.2-0.28），学习率2e-5。

主要结果：LifeSkill 在三个环境平均准确率达0.59，优于最强无训练方法10个绝对点（Group Self-Consistency 0.49）和最强训练方法7个点（RFT 0.52）。具体地，LifeSkill 在 DB 达0.82（超过 RFT 的0.70），OS 达0.64（超过 DAPO 的0.53），但在 KG 上略低于 Group Self-Consistency (0.32 vs 0.36)。消融实验表明，Verifier-Guided Skill Learning 替代为 LLM-Judge 后 DB/OS 降至0.70/0.62；移除技能抽取模型性能下降最大（DB 0.64, OS 0.53）；禁用在线技能内化后 DB/OS 降至0.79/0.60。超参数分析显示，候选技能数 Ks 和轨迹数 Kτ 设为4时性能最佳，窗口大小 B 在 DB 设为4、OS 设为6最优。

### Q5: 有什么可以进一步探索的点？

该论文在在线终身学习智能体方面取得了进展，但仍存在若干值得探索的局限。首先，框架依赖验证器引导的技能学习，但在稀疏奖励的长时序任务中，验证器信号本身可能不可靠或延迟，导致技能提取质量下降，未来可研究如何结合内在动机或分层奖励塑造技术来缓解。其次，在线技能内化过程需要多次技能条件策略展开，测试时计算成本较高，可探索更高效的采样方法，如重要性采样或模型蒸馏来减少开销。此外，当前技能提取主要基于成功率的平均验证，忽略了技能间的协同效应和可组合性，未来可引入结构化技能库，利用图神经网络或元学习实现技能的动态重组与泛化。最后，模型仅内化成功轨迹，未有效处理失败经验中的负面信息，可设计基于对比学习的双向反馈机制，使智能体能同时从错误中避免重复。这些改进有望提升框架在真实复杂环境中的鲁棒性和可扩展性。

### Q6: 总结一下论文的主要内容

论文提出LifeSkill框架，解决在线终身学习智能体在动态环境中缺乏持续适应能力的问题。现有方法依赖固定参数推理和外部记忆检索，无法像人类学习者在测试时内化反馈。LifeSkill是一个两阶段强化学习框架，包含验证器引导的技能学习（VGSL）和在线技能内化（OSI）。VGSL通过在失败尝试后采样候选技能，并依据技能条件化策略rollout的平均验证器奖励来优化技能提取模型，解决技能提取缺乏直接监督的问题；OSI则将成功的技能引导轨迹中的技能文本移除，仅基于原始任务输入更新策略模型，使有用行为内化为参数知识，避免上下文膨胀。在LifelongAgentBench上的实验表明，LifeSkill平均性能提升7个绝对点，显著优于基于记忆和强化学习的基线方法，证明了执行驱动的技能提取与在线参数适应相结合的有效性。
