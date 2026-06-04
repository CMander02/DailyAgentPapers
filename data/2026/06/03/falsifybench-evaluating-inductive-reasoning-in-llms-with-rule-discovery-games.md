---
title: "FALSIFYBENCH: Evaluating Inductive Reasoning in LLMs with Rule Discovery Games"
authors:
  - "Leonardo Bertolazzi"
  - "Katya Tentori"
  - "Raffaella Bernardi"
date: "2026-06-03"
arxiv_id: "2606.04751"
arxiv_url: "https://arxiv.org/abs/2606.04751"
pdf_url: "https://arxiv.org/pdf/2606.04751v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "评估基准"
  - "归纳推理"
  - "假设验证"
  - "科学推理"
  - "多智能体"
relevance_score: 8.5
---

# FALSIFYBENCH: Evaluating Inductive Reasoning in LLMs with Rule Discovery Games

## 原始摘要

Large language models (LLMs) are increasingly deployed as autonomous agents in scientific tasks. Yet whether these systems can effectively engage in forms of inductive reasoning relevant to scientific discovery remains an open question. In this work, we introduce FALSIFYBENCH, an evaluation framework for hypothesis-driven reasoning inspired by the classic Wason 2-4-6 task, in which agents must discover hidden semantic properties by iteratively proposing examples and receiving feedback. This task captures key elements of scientific reasoning: hypothesis generation, evidence gathering, and belief revision in response to both confirming and disconfirming evidence. Our evaluation of 12 LLMs across model families and scales shows that reasoning models are generally stronger scientific reasoners than instruction-tuned models, although no model comes close to optimal performance. The primary driver of success is the capacity for negative testing: models that actively seek to falsify their hypotheses consistently outperform those that primarily seek confirmation. Moreover, a fine-grained turn-level analysis, neglected in previous work, reveals that failure is tied to identifiable patterns in how models navigate the hypothesis space.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前大型语言模型（LLMs）在科学推理中归纳推理能力的评估问题。研究背景是LLMs被越来越多地部署为科学任务的自主智能体，但它们在科学发现所需的假设生成、证据收集和信念修正等核心归纳推理能力上仍存在疑问。现有方法的不足在于缺乏专门针对假设驱动推理（尤其是证伪能力）的评估框架。传统的Wason 2-4-6任务虽然广泛用于研究人类推理，但未被系统用于LLMs的评估，且以往工作忽略了细粒度的回合级行为分析。本文的核心问题是：LLMs是否能像科学家一样，通过迭代提出例子和接收反馈来发现隐藏的语义规则？特别地，当最优策略是进行负性测试（主动寻求证伪当前假设）而非确认性测试时，模型能否有效执行这种与科学发现密切相关的推理？为解决此问题，论文提出了FALSIFYBENCH框架，将Wason任务泛化到语义分类领域，通过构建强调H⊂R关系（负性测试最优）的游戏，系统评估12个LLMs的归纳推理表现，并首次进行回合级行为分析以揭示失败的识别模式。

### Q2: 有哪些相关研究？

关于FALSIFYBENCH的相关研究主要可分为评测类和方法类。在评测类工作中，早期研究通过合成基准测试LLM的归纳推理能力，例如ARC（抽象推理语料库）要求模型从少量输入-输出对推断网格变换规则；另有工作测试模型从命令到动作序列的映射学习能力。近年来研究转向理解推理过程：有些发现思维链不一定提升归纳推理，有的工作通过分离归纳与演绎步骤来评估推理过程，还有研究将模型策略映射至人类特质并关联科学发现。本文最密切相关的是基于Wason 2-4-6任务的两项工作：WILT使用布尔函数作为隐藏规则；另一工作研究数字属性规则并明确探讨确认偏差。区别在于：这些工作未采用规范框架——既不从目标规则的严格子集采样三元组，也不追踪每轮假设与目标规则的关系。本文通过从R的严格分类后代节点采样三元组，使证伪策略成为识别规则的最佳方式，从而克服了这一局限。

### Q3: 论文如何解决这个问题？

FALSIFYBENCH基于经典的Wason 2-4-6任务，构建了一个评估LLM归纳推理能力的框架。核心设计是让LLM同时扮演两个角色：发现隐藏语义规则的“玩家”和提供反馈的“先知”。每一轮，玩家提出三个词汇、当前假设和选择理由，先知根据目标规则R返回“符合”或“不符合”。当玩家确信时提交最终猜测，错误则继续收集证据，直到正确或达到20轮上限。任务使用WordNet中的语义分类（如“动物”“植物”）而非数字序列，避免了LLM对经典任务的记忆效应，并允许构建层次丰富的概念空间。研究者从17905个游戏中精选100个覆盖5个分类的样例。

该框架的关键创新在于定量化“确认偏误”——玩家执行的阳性测试比例（提出假设内的例子）。由于初始例子来自R的子类，玩家假设通常过窄，阳性测试总返回“符合”，无法推进；只有阴性测试才能揭示规则范围更广，促使假设泛化。通过贝叶斯混合效应逻辑回归分析1200场游戏，发现确认偏误是成功率的最强负向预测因子，而“先知”的反馈错误影响可忽略。这表明提升归纳推理的关键在于促进模型的“证伪”行为，即主动寻求否定性证据。这种细粒度的轮次分析超越了过去仅关注最终结果的评估，揭示了LLM在假设空间导航中的典型失败模式。

### Q4: 论文做了哪些实验？

论文在FALSIFYBENCH框架下对12个LLM进行了评估。实验设置要求模型通过迭代提出数字序列并接收反馈，逐步发现隐藏的语义规则，模拟科学推理中的假设生成、证据收集和信念修正。

数据集/基准测试方面，使用的是FALSIFYBENCH，受Wason 2-4-6任务启发，包含多个基于语义规则的发现游戏。对比方法涵盖了不同模型家族和规模的指令微调模型（如Llama-4-Maverick、GPT-5-Nano）与推理模型（如GPT-OSS-20B、GPT-OSS-120B、GPT-5.2-Chat）的对比。

主要结果如下：
1. **整体表现**：推理模型普遍优于指令微调模型，但均未接近最优性能。
2. **深层错误分析**：通过标注每轮测试中当前假设H与目标规则R的关系，发现大多数情况下H是R的真子集，此时否定测试（寻求证伪）是最优策略。模型在否定测试上的表现与成功验证率强负相关（Spearman ρ = -0.937, p < 0.001）。结论性证伪率最高的是GPT-OSS-20B（59.2%）、GPT-OSS-120B（53.4%）和GPT-5.2-Chat（49.5%），最低的是Llama-4-Maverick（18.0%）和GPT-5-Nano（26.6%）。
3. **失败模式**：失败游戏更频繁地出现H与R部分重叠或不相交的情况，且失败游戏中模型更倾向于关注表面语言特征（如数字的字面属性）。

### Q5: 有什么可以进一步探索的点？

可以进一步探索的点包括：首先，论文使用WordNet作为语义知识代理存在局限性，未来可引入更全面的知识图谱或多语言资源来提升评估的普适性。其次，当前人类标注仅覆盖每场游戏的一个Test轮和一个Guess轮，导致oracle误差被简化为二元变量，未来可增加标注密度或采用自动化误差检测方法。此外，论文聚焦于Wason任务中的假说驱动推理，但未覆盖科学发现中的其他关键环节如实验设计或跨领域迁移，可扩展至更复杂的科学推理场景。改进思路上，可以结合主动学习策略让模型自主决定何时验证假说，并引入元认知机制监控模型在假设空间中的搜索模式。未来研究还可探索将否定测试能力作为训练目标，通过强化学习奖励假说证伪行为，或集成多模型协作以模拟科学共同体的推理过程。最终，需在更大规模模型和跨语言数据上验证结论的稳健性。

### Q6: 总结一下论文的主要内容

FALSIFYBENCH是一个评估大语言模型（LLMs）归纳推理能力的基准，它基于经典的Wason 2-4-6任务扩展而来。该任务要求智能体通过迭代提出示例并接收反馈，自主发现隐藏的语义规则，从而模拟科学推理中的假设生成、证据收集和信念修正过程。通过对12个不同规模和系列的LLM进行评估，研究发现推理模型在科学推理任务上普遍优于指令微调模型，但没有任何模型接近最优性能。核心贡献在于揭示了成功的主要驱动力是“否定测试”能力：那些主动寻求证伪其假设的模型，其表现始终优于寻求确认的模型。此外，细粒度的回合级分析表明，失败与模型如何探索假设空间的可识别模式相关，例如模型倾向于提出基于词语表面属性而非语义类别的规则。这项工作系统地评估了LLM的假设驱动推理能力，并指出了当前模型的显著不足。
