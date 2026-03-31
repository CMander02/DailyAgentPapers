---
title: "Dynamic Dual-Granularity Skill Bank for Agentic RL"
authors:
  - "Songjun Tu"
  - "Chengdong Xu"
  - "Qichao Zhang"
  - "Yaocheng Zhang"
  - "Xiangyuan Lan"
  - "Linjing Li"
  - "Dongbin Zhao"
date: "2026-03-30"
arxiv_id: "2603.28716"
arxiv_url: "https://arxiv.org/abs/2603.28716"
pdf_url: "https://arxiv.org/pdf/2603.28716v1"
categories:
  - "cs.AI"
tags:
  - "Agentic RL"
  - "Skill Learning"
  - "Memory"
  - "Experience Reuse"
  - "Decision Support"
  - "Error Correction"
  - "Hindsight Learning"
  - "Policy Optimization"
  - "ALFWorld"
  - "WebShop"
relevance_score: 8.5
---

# Dynamic Dual-Granularity Skill Bank for Agentic RL

## 原始摘要

Agentic reinforcement learning (RL) can benefit substantially from reusable experience, yet existing skill-based methods mainly extract trajectory-level guidance and often lack principled mechanisms for maintaining an evolving skill memory. We propose D2Skill, a dynamic dual-granularity skill bank for agentic RL that organizes reusable experience into task skills for high-level guidance and step skills for fine-grained decision support and error correction. D2Skill jointly trains the policy and skill bank through paired baseline and skill-injected rollouts under the same policy, using their performance gap to derive hindsight utility signals for both skill updating and policy optimization. Built entirely from training-time experience, the skill bank is continuously expanded through reflection and maintained with utility-aware retrieval and pruning. Experiments on ALFWorld and WebShop with Qwen2.5-7B-Instruct and Qwen3-4B-Instruct-2507 show that D2Skill consistently improves success rates over skill-free baselines by 10-20 points. Further ablations and analyses show that both dual-granularity skill modeling and dynamic skill maintenance are critical to these gains, while the learned skills exhibit higher utility, transfer across evaluation settings, and introduce only modest training overhead.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体强化学习（Agentic RL）中，如何更有效地积累、管理和利用可重用经验（技能）来提升长期决策任务性能的问题。

**研究背景**：基于语言的智能体强化学习在处理网页交互、研究等长视野决策任务时面临严峻挑战。由于环境通常以文本界面交互，智能体只能依赖有限的历史观察和动作，这导致了严重的部分可观测性问题，使得信用分配困难，尤其在奖励稀疏和动作空间大的情况下，孤立学习每个任务效率极低。因此，需要机制来积累可跨任务转移的复用知识。

**现有方法的不足**：现有基于技能的方法主要存在两个局限。首先，它们大多从完整轨迹中提取技能，侧重于任务层面的反思，这虽然能提供高层指导，但对于纠正交互过程中细粒度的单步错误效果不佳。其次，随着训练进行，技能库不断膨胀，缺乏对技能进行评估和修剪的原则性机制，导致冗余或无效的技能可能污染检索到的指导信息，反而阻碍策略优化。

**本文要解决的核心问题**：针对上述不足，本文提出了动态双粒度技能库（D2Skill）。其核心是同时维护任务粒度和步骤粒度两种技能：任务技能提供高层任务规划指导，步骤技能则在交互过程中提供细粒度的决策支持和局部错误纠正。此外，论文设计了一个联合训练范式，使策略和技能库协同进化，并通过基于效用的检索与修剪机制动态维护技能库，确保其在整个训练过程中保持紧凑、信息丰富且有益。最终目标是构建一个能持续学习、高效管理并精准应用经验的框架，以显著提升智能体在复杂任务中的成功率和学习效率。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕增强智能体适应性的外部记忆与可重用经验抽象两大方向展开，可归类如下：

**1. 外部记忆与持续适应方法**：这类研究旨在通过外部记忆库存储交互历史，以弥补大语言模型训练后适应性不足的问题。相关工作涉及记忆的保留与遗忘、结构化更新与组织、检索感知优化以及分层或生成式记忆构建。本文的D2Skill技能库可视为一种结构化、可动态维护的外部记忆，但区别于单纯存储原始轨迹，它进一步将经验抽象为不同粒度的可重用技能。

**2. 经验抽象与重用方法**：另一类研究专注于从经验中提炼可重用知识，例如推理策略、可复用工作流、分层经验库以及持续经验精炼。本文与之共享“抽象与重用”的核心思想，但特别聚焦于“技能”这一抽象形式。与近期同样利用自演化经验提升智能体强化学习性能的RetroAgent、Complementary RL等工作相比，D2Skill避免了它们对复杂提示流程和验证阶段信息的依赖，其技能完全在训练过程中生成与管理，降低了系统复杂性和提示依赖性。

**3. 技能导向的强化学习方法**：最直接相关的工作是SkillRL。两者都利用技能库指导策略。但关键区别在于：SkillRL的技能本质上是任务级别的，其“双重性”主要体现在任务分类上，且每个任务仅在开始时检索并使用同一技能。而D2Skill则提出了**动态双粒度技能库**，同时维护用于高层指导的“任务技能”和用于细粒度决策支持与纠错的“步技能”，并在每个交互步骤都进行检索，从而提供了更灵活、精细的决策支持。此外，D2Skill的技能构建完全基于训练经验，无需特权验证信息。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为D2Skill的动态双粒度技能库框架来解决智能体强化学习中可重用经验利用不足的问题。其核心方法是将可重用经验组织成两种粒度的技能：任务技能提供高层指导，步骤技能提供细粒度的决策支持和错误纠正。

整体框架将强化学习训练与一个动态技能库紧密耦合。主要包含三个核心组件：1) 带技能注入的RL训练，2) 反思驱动的技能生成，3) 技能检索与库管理。

在训练过程中，核心机制是并行采样基线组和技能注入组的轨迹。技能组在决策时从技能库中检索相关技能并注入到策略上下文中。两组之间的性能差距被用来构建事后信号，用于策略优化和技能效用更新。具体而言，任务级技能共享基于组成功率差距的效用更新信号，而步骤技能则根据其所在轨迹的个体表现（相对于基线组平均成功率）进行更新。此外，论文引入了事后内在奖励来鼓励有效使用技能，并将此奖励与原始回报结合，通过组归一化计算优势函数，用于GRPO等策略优化算法。

当某个任务组的性能低于阈值时，反思模块被触发。它分析代表性的失败（和成功）轨迹，利用外部LLM生成新的任务技能和步骤技能。新技能经过去重和规范化后存入技能库，并关联检索键（任务技能对应任务标识符，步骤技能对应任务标识符和失败观测）。

在交互时，采用两阶段检索机制：首先基于查询键（任务或当前观测）与技能键的语义相似度进行初选，然后结合归一化相似度、技能效用以及一个鼓励探索的UCB式奖励来计算综合选择分数，选出最相关的技能注入策略。

为了管理技能库规模，系统会定期基于效用进行剪枝。每个技能池设有容量上限，通过计算一个包含效用和探索奖励的“驱逐分数”，移除分数最低的旧技能（新创建的技能在一定保护期内免于被移除），从而保持一个高效且规模有界的技能记忆。

创新点主要体现在：1) 双粒度技能建模，同时提供高层任务指导和局部纠错支持；2) 利用基线组与技能组的性能差距构建统一的事后信号，联合优化策略和技能效用；3) 动态的、基于反思和效用的技能库生命周期管理（生成、检索、更新、剪枝），使技能库能持续演化。

### Q4: 论文做了哪些实验？

论文在ALFWorld和WebShop两个LLM智能体基准测试上进行了实验，评估了D2Skill方法。实验设置方面，默认训练160步，每5步在128个验证任务上评估，报告整个训练过程中的最佳性能。使用了Qwen2.5-7B-Instruct和Qwen3-4B-Instruct-2507作为基础模型，其中Qwen2.5-7B-Instruct使用了SFT初始化以确保技能使用的可靠性。

对比方法包括：无技能的强化学习基线（GRPO）、先前的记忆增强方法（Mem0+GRPO, SimpleMem+GRPO）和技能增强方法（SkillRL），以及闭源模型（Gemini-3-Flash, O3）作为参照。主要结果如下：在ALFWorld上，使用Qwen2.5-7B-Instruct时，D2Skill取得了90.6%的整体成功率，比GRPO（75.0%）高出15.6个百分点，也超过了SkillRL（89.1%）。在WebShop上，D2Skill最佳变体取得了91.1的分数和84.4%的成功率，优于GRPO（86.0/72.6）和SkillRL（85.2/72.7）。使用较小的Qwen3-4B-Instruct-2507模型时，D2Skill将ALFWorld的整体成功率从GRPO的53.9%提升至69.6%（使用Gemini-3-Flash生成技能）和72.7%（使用O3生成技能）。即使在经过SFT初始化的强策略上，D2Skill在训练40步后就能达到92.2%的成功率，接近GRPO训练120步的结果（92.9%），并在训练120步后进一步提升至95.3%。

消融实验分析了关键组件的作用：移除任务技能或步骤技能均导致性能下降（验证成功率分别降至62.7%和60.2%），移除技能管理（禁用剪枝）性能降至57.8%，表明双粒度技能建模和动态维护至关重要。分析还显示，D2Skill学习的技能具有较高的效用和跨评估环境的可迁移性，且训练开销仅比GRPO增加约20%（25.6小时 vs. 20.8小时），远低于SkillRL（49.2小时）。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在评估范围较窄（仅限ALFWorld和WebShop两个基准）以及对额外反思模型（reflector）的依赖。未来研究可从以下几个方向深入：首先，将框架扩展到更复杂、开放的环境（如具身智能或3D虚拟世界），验证其泛化能力；其次，探索如何将反思机制内化到智能体策略中，减少对外部模型的依赖，例如通过元学习或自监督方式生成技能效用信号。此外，技能库的动态维护机制（如效用感知的检索与剪枝）可进一步优化，例如引入多目标权衡（如技能多样性 vs. 效用）或自适应扩展阈值。从方法融合角度看，可将技能粒度从“任务-步骤”二元结构扩展为多层级体系，以支持更灵活的层次化决策；同时，研究技能在跨任务迁移中的组合性与可解释性，可能提升智能体的零样本适应能力。最后，训练开销虽已控制，但在大规模环境中如何实现高效并行技能学习与更新，仍是工程与算法结合的挑战。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为D2Skill的动态双粒度技能库方法，旨在提升智能体强化学习（Agentic RL）中经验复用的效率。核心问题是现有基于技能的方法多局限于轨迹级指导，缺乏动态维护技能记忆的机制。为此，D2Skill将可重用经验组织为两种粒度：任务技能提供高层指导，步骤技能则用于细粒度决策支持和错误纠正。

方法上，D2Skill通过在同一策略下并行执行基线推演和技能注入推演，联合训练策略和技能库。利用两者性能差距生成事后效用信号，同时驱动技能更新与策略优化。技能库完全从训练经验中构建，通过反思机制持续扩展，并借助效用感知的检索与剪枝进行动态维护。

实验在ALFWorld和WebShop环境中使用Qwen系列模型进行，结果表明D2Skill相比无技能基线持续提升成功率10-20个百分点。消融分析证实双粒度技能建模与动态维护均至关重要，所学技能展现出更高效用、良好的跨场景迁移能力，且仅引入适度的训练开销。该工作为构建可进化、可复用的技能记忆系统提供了系统化框架。
