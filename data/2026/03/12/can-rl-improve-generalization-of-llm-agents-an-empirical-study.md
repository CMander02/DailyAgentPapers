---
title: "Can RL Improve Generalization of LLM Agents? An Empirical Study"
authors:
  - "Zhiheng Xi"
  - "Xin Guo"
  - "Jiaqi Liu"
  - "Jiazheng Zhang"
  - "Yutao Fan"
  - "Zhihao Zhang"
  - "Shichun Liu"
  - "Mingxu Chai"
  - "Xiaowei Shi"
  - "Yitao Zhai"
  - "Xunliang Cai"
  - "Tao Gui"
  - "Qi Zhang"
  - "Xuanjing Huang"
date: "2026-03-12"
arxiv_id: "2603.12011"
arxiv_url: "https://arxiv.org/abs/2603.12011"
pdf_url: "https://arxiv.org/pdf/2603.12011v1"
categories:
  - "cs.AI"
tags:
  - "强化学习微调"
  - "智能体泛化性"
  - "经验性研究"
  - "多环境训练"
  - "决策智能体"
  - "迁移学习"
  - "遗忘分析"
relevance_score: 8.5
---

# Can RL Improve Generalization of LLM Agents? An Empirical Study

## 原始摘要

Reinforcement fine-tuning (RFT) has shown promise for training LLM agents to perform multi-turn decision-making based on environment feedback. However, most existing evaluations remain largely in-domain: training and testing are conducted in the same environment or even on the same tasks. In real-world deployment, agents may operate in unseen environments with different background knowledge, observation spaces, and action interfaces. To characterize the generalization profile of RFT under such shifts, we conduct a systematic study along three axes: (1) within-environment generalization across task difficulty, (2) cross-environment transfer to unseen environments, and (3) sequential multi-environment training to quantify transfer and forgetting. Our results show that RFT generalizes well across task difficulty within an environment, but exhibits weaker transfer to unseen environments, which correlates with shifts in both semantic priors and observation/action interfaces. In contrast, sequential training yields promising downstream gains with minimal upstream forgetting, and mixture training across environments improves the overall balance. We further provide detailed analyses and deeper insights, and hope our work helps the community develop and deploy generalizable LLM agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在系统性地探究强化学习微调（RFT）如何影响大语言模型（LLM）智能体的泛化能力，特别是在面对真实世界部署中常见的、与训练环境不同的新环境时的表现。研究背景是，RFT作为一种后训练范式，在提升LLM智能体完成复杂交互任务（如网页导航、软件工程）方面显示出潜力，但现有评估大多局限于同领域内，即在相同环境甚至相同任务上进行训练和测试。然而，现有方法的不足在于，现实部署中智能体常会遇到未见过的环境，这些环境在背景知识、观察空间和动作接口等方面都可能存在差异，而现有研究对这些分布偏移下的泛化性能缺乏深入理解。

本文要解决的核心问题是：RFT所带来的性能提升能否泛化到训练分布之外？具体而言，论文通过三个维度系统性地刻画RFT的泛化特性：1）在同一环境内，针对不同难度任务的泛化能力；2）跨环境迁移到未见环境的能力；3）通过顺序多环境训练来量化迁移与遗忘效应。研究发现，RFT在环境内跨任务难度泛化良好，但向未见环境的迁移能力较弱，且这种迁移与语义先验及观察/动作接口的变化相关。相比之下，顺序训练能在最小化上游遗忘的同时带来可观的下游收益，而混合训练则能提升整体平衡性。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：强化学习在LLM训练中的应用、LLM代理的决策能力研究，以及后训练策略对泛化与遗忘的影响。

在方法层面，强化学习已被广泛用于LLM训练，例如基于人类反馈的强化学习（RLHF）和基于可验证奖励的强化学习（RLVR），这些方法在提升指令遵循、推理准确性和行为对齐方面效果显著。近期研究进一步将强化学习扩展到LLM代理，以增强其多步决策、长程规划及与环境交互的能力。

在应用层面，已有工作表明强化学习能帮助代理分解复杂任务、协调推理与行动，并通过环境反馈调整策略，从而更有效地进行信息收集、自我修正和工具使用。然而，这些研究大多在领域内进行评估，即训练和测试在相似的任务分布和接口中进行，其策略在跨任务或未知环境中的泛化能力尚未充分探索。

在评测层面，近期研究开始关注后训练策略如何影响LLM的泛化与遗忘行为。例如，监督微调（SFT）虽能提升领域内性能，但容易导致过度专门化和通用能力退化；而RL（尤其是RLVR）通过优化轨迹级目标，能更好地保留预训练表示，实现更稳健的跨任务迁移。不过，RL也可能引发负向干扰和“赢者通吃”动态，导致行为覆盖减少和推理边界收缩。与现有研究多关注静态单轮任务不同，本文首次将后训练泛化与遗忘的研究扩展到多轮LLM代理，并系统评估了在不同观察和行动空间环境中的效果。

### Q3: 论文如何解决这个问题？

论文通过一个系统的实证研究框架来解决强化微调（RFT）后LLM智能体的泛化能力问题。其核心方法是沿着三个维度设计实验，以全面刻画RFT在不同场景下的泛化特性：1）同一环境内跨任务难度的泛化；2）向未见环境的跨环境迁移；3）跨多个环境的顺序训练，以量化迁移与遗忘。

整体架构基于标准的ReAct交互范式，将任务形式化为一个元组，包括指令、状态、动作、观察空间以及状态转移和奖励函数。研究使用Qwen2.5-3B/7B-Instruct模型作为策略网络，在AgentGym-RL框架下进行RFT训练，并采用GRPO算法优化策略梯度目标，以最大化期望累积奖励。

关键技术和方法创新点包括：
1.  **分层实验设计**：研究不是单一测试，而是构建了三个递进的评估轴心。首先，在同一环境（如WebShop、AlfWorld）内，将任务按难度分为简单和困难子集，评估RFT策略在不同难度任务间的迁移能力。其次，进行严格的跨环境零样本评估，即在一个环境训练后，直接在其余四个未见环境测试，计算“域内提升”和“域外提升”指标。最后，设计顺序训练实验，让智能体依次在多个环境上训练，观察其对上游任务的遗忘程度和对下游任务的适应能力。
2.  **详尽的对比与分析**：对于每个研究问题，都设置了精细的对照实验。例如，在难度泛化中，对比了仅用简单任务训练、仅用困难任务训练、混合训练以及不同顺序课程学习的效果。在跨环境泛化中，系统地遍历了所有可能的“训练环境-测试环境”组合，并用热图直观展示性能变化。在顺序训练中，不仅进行两两环境的顺序训练，还扩展到五个环境的完整序列，并与混合所有数据的联合训练进行对比。
3.  **深入的归因分析**：研究不仅报告性能数据，还结合具体环境特性（如动作空间、反馈稀疏性、背景知识依赖）对结果进行解释。例如，发现BabyAI环境因提供每一步的有效动作列表，导致训练出的智能体过度依赖此信息，损害了长程推理能力，从而在迁移到其他环境时出现严重的性能下降。同时，研究指出跨环境泛化的成功与否与环境间的语义先验、观察/动作接口的相似度高度相关。

最终，论文通过这一系列严谨的实验得出了核心结论：RFT在环境内跨任务难度泛化表现强劲，并能通过“由易到难”的课程学习进一步优化；但在跨环境零样本迁移中表现较弱，且性能提升与下降与环境特性紧密关联；而顺序训练能在最小化上游遗忘的同时获得可观的下游性能增益，其效果可与混合训练相媲美，为开发可泛化的LLM智能体提供了重要见解。

### Q4: 论文做了哪些实验？

论文围绕强化微调（RFT）对LLM智能体泛化能力的影响，进行了系统性的实验研究，主要涵盖三个维度：**同一环境内跨任务难度泛化**、**跨环境迁移到未见环境**以及**跨环境顺序训练中的迁移与遗忘**。

**实验设置**：研究采用AgentGym-RL框架，基于Qwen2.5-3B-Instruct和Qwen2.5-7B-Instruct模型，遵循ReAct交互范式进行RFT训练。每个任务采样8条轨迹，最大响应长度为8192令牌。评估时，主要指标为avg@8（基于8次采样的平均成功率），并辅以平均交互轮次和生成令牌数来衡量效率。

**数据集/基准测试**：使用了五个代表性的智能体环境：WebShop（网络购物）、SearchQA（搜索增强问答）、TextCraft（Minecraft物品合成）、AlfWorld（家庭环境探索）和BabyAI（网格世界模拟器）。任务指令数据来源于AgentGym，并根据Qwen2.5-7B-Instruct模型的性能将任务划分为简单（$\mathcal{U}_easy$）和困难（$\mathcal{U}_hard$）两个难度等级。

**对比方法与主要结果**：
1.  **同一环境内跨难度泛化**：实验对比了在不同难度数据（仅简单、仅困难、混合）上训练后的模型性能。结果显示，RFT在同一环境内表现出强大的跨难度泛化能力。例如，在WebShop上，使用7B模型在简单任务上训练后，其在困难测试集上的性能提升了60.1个百分点。此外，课程学习（先易后难）能进一步提升性能，如在BabyAI上，$\mathcal{U}_easy+\mathcal{U}_hard$顺序训练比单独使用$\mathcal{U}_easy$或$\mathcal{U}_hard$分别高出2.0和3.3个百分点。RFT还显著提升了探索效率，例如在BabyAI中训练3B模型后，平均交互轮次从10.76降至4.19，轨迹长度从624.58令牌降至160.60令牌。

2.  **跨环境迁移**：实验通过在单一环境训练，然后在其他环境测试来评估零样本迁移能力。关键指标包括$\Delta$Held-In（训练环境内的性能提升）、$\Delta$Held-Out（未见环境上的性能提升）和$\Delta$Overall（总体平均提升）。结果发现，模型在训练环境（held-in）上提升显著（如在AlfWorld上3B模型提升78.62分），但在未见环境（held-out）上迁移能力有限且不稳定（3B和7B模型平均仅提升约3.3-3.4分）。存在正迁移（如SearchQA训练对WebShop测试有提升）和负迁移（如BabyAI训练导致WebShop性能从28.59骤降至10.25）。泛化效果高度依赖目标环境特性。

3.  **顺序训练与遗忘**：实验进行了两阶段和五阶段的跨环境顺序训练，并与在混合数据上进行联合训练的方法对比。结果显示，顺序训练在适应下游新环境的同时，能很好地保持在上游环境中的性能（抗遗忘），且能达到与联合训练相当的性能水平。例如，先在WebShop训练再在TextCraft训练，下游TextCraft性能从基线80.88提升至82.50，而上游WebShop性能仅从86.5微降至86.32。训练顺序对泛化性能有显著影响，符合“由易到难”课程学习的顺序通常效果更好。

### Q5: 有什么可以进一步探索的点？

该论文揭示了RFT在跨环境泛化上的核心局限：其能力高度依赖于训练环境与测试环境在语义先验、观察/行动接口上的一致性。当环境差异较大时，代理容易出现确认偏误、猜测虚构、状态不一致等系统性失败模式，这暴露了当前方法在元认知（如自我验证、反思）和工具泛化使用上的根本不足。

基于此，未来可从多个维度深入探索：首先，**提升环境感知与接口适应能力**。可以研究如何让代理动态识别新环境的观察/行动空间结构，并快速调整策略，例如通过少量演示或环境描述进行快速接口对齐。其次，**增强元认知与稳健决策机制**。针对普遍的确认偏误和逻辑缺陷，可设计内在奖励或辅助任务，激励代理进行假设检验、信息溯源和计划一致性维护。最后，**开发更高效的跨环境训练范式**。论文中混合训练已显示出平衡潜力，可进一步探索课程学习、基于环境特征的课程编排，或引入对抗性环境生成来主动暴露泛化弱点，从而构建更鲁棒的代理。这些方向旨在突破当前代理对训练分布的高度依赖，迈向真正的开放世界泛化。

### Q6: 总结一下论文的主要内容

该论文系统研究了强化学习微调（RFT）对大型语言模型（LLM）智能体在多轮决策任务中泛化能力的影响。核心问题是评估RFT训练出的智能体在面临环境变化时的泛化性能，而非仅限于同域测试。

研究通过三个维度展开实证分析：同一环境内不同任务难度的泛化、向未知环境的跨环境迁移，以及顺序多环境训练中的迁移与遗忘。主要结论表明，RFT在环境内部能良好泛化至不同难度任务，但在跨环境迁移时表现较弱，其性能下降与语义先验及观察/行动接口的变化相关。同时，顺序训练能在最小化上游遗忘的前提下带来下游收益，而混合训练则有助于提升整体平衡性。

论文的核心贡献在于首次系统刻画了RFT的泛化特性，为在实际部署中开发具有可靠泛化能力的LLM智能体提供了实证依据与实用指导。
