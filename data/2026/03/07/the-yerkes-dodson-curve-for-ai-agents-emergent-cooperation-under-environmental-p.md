---
title: "The Yerkes-Dodson Curve for AI Agents: Emergent Cooperation Under Environmental Pressure in Multi-Agent LLM Simulations"
authors:
  - "Ivan Pasichnyk"
date: "2026-03-07"
arxiv_id: "2603.07360"
arxiv_url: "https://arxiv.org/abs/2603.07360"
pdf_url: "https://arxiv.org/pdf/2603.07360v1"
categories:
  - "cs.AI"
tags:
  - "多智能体协作"
  - "环境压力"
  - "涌现行为"
  - "LLM智能体模拟"
  - "合作行为"
  - "课程设计"
relevance_score: 7.5
---

# The Yerkes-Dodson Curve for AI Agents: Emergent Cooperation Under Environmental Pressure in Multi-Agent LLM Simulations

## 原始摘要

Designing environments that maximize the rate of emergent behavior development in AI agents remains an open problem. We present the first systematic study of stress-performance relationships in large language model (LLM) multi-agent systems, drawing an explicit parallel to the Yerkes-Dodson law from cognitive psychology. Using a grid-world survival arena, we conduct 22 experiments across four phases, varying environmental pressure through resource scarcity (upkeep cost) and reproductive competition (sexual selection). Our key finding is that cooperative behavior follows an inverted-U curve: trade interactions peak at 29 under medium pressure (upkeep=5), while both low and extreme pressure produce 8--12 trades. Under extreme pressure, behavioral repertoire collapses to movement-only within 5--12 turns. We further show that sexual selection -- a softer pressure mechanism where all agents survive but not all reproduce -- eliminates inter-agent aggression entirely and produces communicative behavior absent under survival pressure. These results suggest that environmental pressure calibration is a viable curriculum design strategy for LLM agent development, analogous to the inverted-U relationship between arousal and performance in biological systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何通过调控环境压力来优化多智能体系统中AI智能体（特别是基于大语言模型）复杂社会行为涌现的问题。研究背景是，随着大语言模型被部署为复杂多智能体环境中的自主智能体，环境设计成为影响AI系统能力前沿的关键因素。心理学中的耶克斯-多德森定律揭示了压力（唤醒水平）与任务表现之间的倒U型关系，但这一原理从未在LLM智能体群体中得到系统性验证。

现有研究的不足在于，尽管已有工作表明不同LLM在博弈环境中会表现出稳定、差异化的行为模式（如合作、背叛、攻击），并且能在资源稀缺下展现出生存本能，但尚无研究系统性地改变环境压力，以绘制LLM智能体群体的压力-表现曲线。具体来说，缺乏关于环境压力水平如何精确影响合作行为涌现、以及何种压力机制能更有效驱动良性社会复杂性的知识。

因此，本文要解决的核心问题是：如何校准环境难度，以最大化多智能体LLM模拟中复杂社会行为的涌现速率。论文通过三个具体研究问题展开：1）LLM智能体是否在环境压力与合作行为间表现出耶克斯-多德森（倒U型）关系；2）行为谱系在何种压力水平下崩溃，其表现如何；3）与生存威胁相比，生殖竞争（如性选择）能否在不导致致命后果的情况下驱动社会复杂性。通过回答这些问题，论文旨在为LLM智能体的课程设计和环境校准提供实证依据和策略指导。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. LLM智能体在博弈论环境中的行为研究**：近期研究探索了LLM在战略互动中的表现，例如发现Claude 3.5表现出最强的亲社会偏见，GPT-o1在竞争性游戏中表现出色但易出现信任崩溃，而DeepSeek-R1则展现出更优的合作与心智理论能力。这些工作证实了LLM具有稳定的行为“表型”，但未深入探究环境压力如何调节这些行为，而本文则系统性地研究了压力水平对行为的影响。

**2. LLM智能体的生存本能研究**：已有研究在类似Sugarscape的环境中证实LLM智能体展现出生存本能，在资源稀缺时攻击率较高。然而，这些工作未系统性地调整压力水平以绘制完整的压力-性能曲线，而本文则通过精细控制资源匮乏程度，首次揭示了合作行为与压力之间的倒U型关系。

**3. 多智能体环境与涌现行为研究**：从经典的Sugarscape到近期通过自博弈驱动能力涌现的研究，该领域长期关注智能体群体中涌现的社会行为。另有工作研究了序列社会困境中的合作与背叛动态。本文的延伸在于使用LLM作为智能体策略，并聚焦于**环境压力**（而非战略压力）的调节作用。

**4. 课程学习与开放式进化**：课程学习理念认为训练难度应循序渐进，但传统方法主要集中于有监督或强化学习场景，依赖基于梯度的优化。本文的创新在于将预训练的LLM策略视为固定参数，通过改变环境而非模型参数来创建课程，即利用进化压力而非参数更新来实现课程学习。

**5. 耶克斯-多德森定律与性选择理论**：本文直接借鉴了心理学中的耶克斯-多德森定律（描述唤醒与绩效的倒U型关系）以及生物学中的性选择理论（包括亲代投资理论等）。本文是首次在AI智能体系统中检验该定律的研究，并创新地将性选择设计为一种更温和的压力机制，从而完全消除了攻击行为并诱发了沟通行为。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为“生存竞技场”的多智能体网格世界模拟环境，并系统性地调节环境压力参数，来研究LLM智能体合作行为的涌现。其核心方法是利用一个离散网格世界，其中包含食物和代币两种可再生资源节点，智能体需通过采集、移动、攻击、交易、休息、训练等动作维持生存。整体框架分为两个主要实验引擎：v6.1用于生存压力研究，v6.2用于性选择压力研究。

在架构设计上，每个智能体由力量、速度、智力、社交、耐力、魅力六项属性参数化，通过预算约束进行差异化初始化。智能体的决策完全由Claude 3.5 Sonnet模型根据当前状态、局部观察、可用动作和历史记录生成，不提供任何行为提示或策略指导。环境压力的核心调控机制是“维护成本”：每个回合智能体需消耗固定食物，若食物归零则死亡。通过改变维护成本（从2到7），论文创建了从低压到高压的连续谱系，以观察压力水平对合作行为（特别是交易互动）的影响。

关键技术包括：1）压力校准机制：通过维护成本调节生存压力，模拟资源稀缺性；2）双压力模式对比：在生存压力实验中，压力直接导致死亡风险；在性选择压力实验（v7引擎）中，压力转化为生殖竞争——所有智能体均易存活，但只有部分能繁殖，从而引入“软压力”；3）属性与观察系统：社交属性调制智能体对他者的观察精度与通信范围，智力影响交易结果与训练速度，形成了基于属性的差异化能力体系；4）完全基于预训练知识的涌现：不进行微调或提供示例，纯粹依靠LLM内嵌的人类战略知识来产生自适应行为。

创新点主要体现在：首次将心理学中的耶克斯-多德森曲线（倒U型关系）系统引入多智能体LLM研究，实证发现合作行为随压力增加呈现先升后降的倒U型曲线；提出“压力校准”作为课程设计策略，证明中等压力最有利于合作涌现；揭示性选择压力能完全消除攻击行为并促进行为多样性，而极端生存压力则导致行为谱系崩溃（仅剩移动）。

### Q4: 论文做了哪些实验？

论文通过四个阶段共22个实验，系统研究了环境压力对多智能体LLM合作行为的影响。实验设置方面，研究使用网格世界生存竞技场模拟环境，智能体策略基于Claude 3.5 Sonnet，调用并行度为4，每个实验耗时约50-90分钟。主要数据集来自P2b阶段的受控压力扫描实验，维护成本（upkeep）设置为{2, 4, 5, 6, 7}，资源节点数量恒定（食物节点8个，代币节点5个），使用v6.1引擎在9×9网格上运行，包含16个智能体，随机种子固定为42。

实验的核心对比是在不同生存压力（通过维护成本调节资源稀缺性）与性选择压力（V7阶段）下智能体的行为差异。主要结果揭示了明显的耶基斯-多德森倒U型曲线：在中等压力（upkeep=5）下，合作交易次数达到峰值29次；低压力（upkeep=2）时交易为11-12次；高压力（upkeep=6-7）时则下降至16次和8次。关键数据指标包括：交易次数（主要合作度量）、攻击次数（在upkeep=2时高达76-85次，随压力增加而减少）、存活智能体数量（高压力下仅存1-2个）以及游戏持续时间（upkeep=7时仅20回合）。此外，性选择实验（V7）完全消除了智能体间攻击（0次），并出现了生存压力下未观察到的沟通行为（8次）和繁殖行为（17次尝试，成功3次），所有12个存活智能体均坚持到40回合结束。这些结果表明，环境压力的校准是引导LLM智能体行为发展的有效课程设计策略。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于实验配置较为单一，仅使用单一LLM模型（未说明具体模型）进行测试，且缺乏统计显著性验证（如多随机种子实验）。未来研究可首先探索多模型“物种”竞技场，将不同LLM（如Claude、GPT-4o等）视为具有不同行为特征的智能体，检验压力曲线是否因模型架构与训练差异而变化，并观察异质群体能否涌现更复杂的协作或竞争动力学。其次，需加强实验的统计严谨性，通过多次重复实验计算置信区间，并填补压力参数（如upkeep=3）的数据缺口以精确刻画倒U型曲线。

结合个人见解，可进一步探索“压力校准自动化”方向：开发元学习框架，使系统能动态调整环境压力参数（如资源衰减率、竞争强度），以实时最大化智能体协作或创新行为的涌现速率，实现自适应课程学习。此外，可引入外部目标导向的压力机制（如周期性灾难事件），研究智能体在突变压力下的韧性迁移能力。这些改进既能深化对多智能体系统宏观规律的理解，也为构建更鲁棒、协作的AI群体提供方法论支持。

### Q6: 总结一下论文的主要内容

该论文首次系统研究了大型语言模型多智能体系统中的压力-性能关系，揭示了其与心理学中耶基斯-多德森定律的相似性。核心问题是探究环境压力如何影响AI智能体合作行为的涌现。研究方法是在网格世界生存环境中进行22组实验，通过资源稀缺性和生殖竞争来调节环境压力。主要结论发现合作行为呈现倒U型曲线：中等压力下贸易交互达到峰值29次，而低压和极端压力下仅产生8-12次。极端压力会导致行为模式在5-12回合内退化到仅剩移动能力。研究还发现生殖选择机制能完全消除攻击行为并产生生存压力下缺失的交流行为。这项工作的意义在于为LLM智能体训练提供了环境压力校准这一课程设计新范式，表明通过调节环境压力而非梯度下降来塑造智能体行为，可能成为下一代多智能体系统开发的关键设计参数。
