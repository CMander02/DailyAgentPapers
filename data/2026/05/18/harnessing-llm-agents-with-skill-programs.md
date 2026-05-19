---
title: "Harnessing LLM Agents with Skill Programs"
authors:
  - "Hongjun Liu"
  - "Yifei Ming"
  - "Shafiq Joty"
  - "Chen Zhao"
date: "2026-05-18"
arxiv_id: "2605.17734"
arxiv_url: "https://arxiv.org/abs/2605.17734"
pdf_url: "https://arxiv.org/pdf/2605.17734v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Skill Programs"
  - "Program Functions"
  - "Agent Architecture"
  - "Inference-time Intervention"
  - "Post-training"
  - "Self-improvement"
  - "Web Search"
  - "Math Reasoning"
  - "Code Generation"
relevance_score: 9.5
---

# Harnessing LLM Agents with Skill Programs

## 原始摘要

Equipping LLM agents with reusable skills derived from past experience has become a popular and successful approach for tackling complex and long-horizon tasks. However, such lessons are often encoded as textual guidance that remains largely advisory, lacking explicit mechanisms for when and how to intervene in the agent loop. To bridge the gap, we introduce HASP(Harnessing LLM Agents with Skill Programs), a new framework that upgrades skills into executable Program Functions (PFs). Rather than offering passive advice, PFs act as executable guardrails that activate on failure-prone states and modify the next action or inject corrective context. HASP is highly modular: it can be applied at inference time for direct agent-loop intervention, during post-training to provide structured supervision, or for self-improvement by evolving validated, teacher-reviewed PFs. Empirically, HASP drives substantial gains compared to both training-free and training-based methods on web-search, math reasoning, and coding tasks. For example, on web-search reasoning, inference-time PFs alone improve the average performance by 25% compared to (multi-loop) ReAct Agent, while post-training and controlled evolution achieve a 30.4% gain over Search-R1. To provide deeper insights into HASP, our mechanism analysis reveals how PFs trigger and intervene, how skills are internalized, and the requirement for stable skill library evolution.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有大语言模型（LLM）智能体在复用过往经验时存在的问题。研究背景是，LLM智能体已能有效完成复杂长时任务，但任务分布变化和交互累积常导致智能体重复犯类似错误（如过早终止、得出脆弱中间结论或重复无效动作）。现有方法通常将成功经验编码为文本形式的技能（如提示内注入、检索式建议或训练时的奖励塑造），但这种指导本质上是“建议性”的，缺乏明确的执行机制：文本技能无法精确指定在策略循环中何时激活、如何干预下一步决策，且模型在实践中往往忽略它们。

本文的核心问题正是要弥合“以语言表达的、可复用的经验”与“能可靠、显式控制智能体行为的、可执行的经验”之间的鸿沟。为此，论文提出了HASP框架，将技能升级为可执行的程序函数（Program Functions, PFs）。PFs不是被动建议，而是可执行的“护栏”：它们在运行时根据智能体状态自动激活，并通过修改下一步动作或注入纠正性上下文直接干预智能体循环。通过将技能从被动文本转化为主动、可触发、可干预的代码级模块，HASP旨在为智能体提供更可靠、更可控的经验复用机制。

### Q2: 有哪些相关研究？

论文将相关工作分为两大类别：

1. **后训练方法（Post-training for agent reasoning and tool use）**：包括Search-R1、ReSearch、ZeroSearch、StepSearch、VerlTool等专注于搜索与工具使用的训练方法，以及SimpleRL-reason、Open-Reasoner-Zero、General-Reasoner、ToRL、AceCoder、GRPO-based code training等推理与编码优化方法。本文与这些方法的区别在于，本文提出的HASP框架不预设单一训练范式，而是模块化地支持SFT、拒绝采样和在线策略蒸馏等多种训练方式。

2. **技能增强与自我改进方法（Skill-augmented and self-improving agents）**：如Reflexion、ExpeL、Voyager、MemSkill、SkillRL、EvolveR、SAGE等。这些方法将经验以提示文本或任务特定例程的形式存储。本文的创新在于将技能升级为可执行的程序函数（PFs），这些函数在智能体循环内部作为可执行的运行时控制机制主动触发，提供直接的状态-动作干预，而不仅仅是建议性指导。

通过对比表格可看出，HASP在技能/记忆形式、运行时控制、学习信号、策略训练和技能演化五个维度均提供了明确支持，而现有方法在这些维度上仅部分支持或不支持。

### Q3: 论文如何解决这个问题？

HASP通过将技能升级为可执行程序函数（PF），构建了一个模块化的智能体干预框架。核心设计包含三个层次：

第一层是技能表征创新。每个PF由两个可执行组件构成：should_activate函数（基于状态和原始动作判断是否触发）和intervene函数（实施具体修复）。相比自然语言提示，PF把"避免重复搜索"这类原则转化为精确的状态-动作映射规则，通过语法检查、接口验证和模拟执行确保可靠性。

第二层是推理时干预机制。在智能体每次动作生成后，外部的控制层会检索相关PF并执行两步操作：首先评估激活条件，然后通过干预算子Γ对原始动作进行修改（如重写过度约束的搜索查询）或注入修正上下文（如同名实体警告）。该设计实现了"提议-修正"分离——智能体维持原始策略，PF充当可执行的防护栏。当多个PF可触发时，可选的辅助教师模型辅助选择最优干预。

第三层是双向进化循环。每个干预事件被记录为包含状态、原始动作、修正动作和反馈信号的元组。这些轨迹数据通过四个信号（时机、模式、正确性、结果）加权评分，用于三方面：一是通过拒绝采样筛选优质轨迹进行训练（偏好中间步骤匹配PF修正的轨迹）；二是动态扩充技能库，定期从持续失败模式中提取新PF候选，经执行验证和教师评审后加入；三是支持SFT和在线蒸馏等不同训练策略。

### Q4: 论文做了哪些实验？

论文在三个任务上进行了实验：网页搜索推理、数学推理和代码生成。实验设置采用Qwen2.5-7B-Instruct作为骨干模型，使用训练池中反复出现的失败-修复模式构建初始技能库。在数据集方面，网页搜索推理使用HotpotQA、2Wiki和MuSiQue；数学推理使用AIME24、AMC23和GameOf24，由GPT-4o评判；代码生成使用HumanEval（Base, Plus）、MBPP（Base, Plus）和BigCodeBench（Full, Hard），以pass@1为指标。对比方法包括GPT-4o、GPT-4o-mini、ReAct Agent、Prompt-Only Skills、Search-R1、AgentFlow等训练无关和训练基线方法。主要结果：在网页搜索推理上，仅使用程序函数（PF）的推理时干预平均准确率达51.0%，较ReAct Agent提升25%；加入教师选择后达56.2%。训练后，HASP-Evolve + RS达60.3%，较Search-R1提升30.4%。在数学推理上，推理时PF干预达35.9%，训练后HASP-Evolve + RS达45.4%。在代码任务上，推理时PF干预平均pass@1为63.4%，训练后HASP-Evolve + RS达69.9%。此外，消融实验显示，固定库下OPD训练在网页搜索推理上达62.5%，闭环进化中RS表现最佳。

### Q5: 有什么可以进一步探索的点？

HASP将技能升级为可执行程序函数（PF），但其有效性高度依赖初始PF库的质量，且当前只验证了Web搜索、数学推理和编码三类任务，泛化性存疑。未来可探索**自动生成**PF的策略，例如让LLM Agent在探索失败时自行反思并提炼为PF，减少人工校验负担。另一个方向是**多Agent协同进化**：现有框架中PF库孤立演化，若引入跨Agent的PF共享与融合机制，可能加速技能累积并提升鲁棒性。此外，**PF的抽象层次**值得深究——当前PF偏向细粒度修复，能否构建层级化技能树（如高层策略PF调用底层执行PF）以应对更复杂的长程任务？最后，结合**对比学习**优化PF触发条件，使Agent在类似失败状态下更精准地激活对应PF，而非依赖人工定义的规则集。

### Q6: 总结一下论文的主要内容

该论文提出HASP框架，旨在解决LLM智能体可重用技能缺乏明确干预机制的问题。核心贡献在于将技能转化为可执行的程序函数（PFs），这些函数不再是被动建议，而是在运行时根据状态自动激活，通过修改下一步动作或注入修正上下文直接干预智能体循环。HASP具有高度模块化特性，支持推理时直接干预、训练后提供结构化监督，以及通过进化已验证的技能库实现自我改进。在网页搜索推理、数学推理和代码生成任务上，HASP相比无训练和有训练基线均有显著提升：例如在网页搜索任务中，推理时PF干预相比多循环ReAct Agent平均提升25%，训练后结合受控进化相比Search-R1提升30.4%。机制分析进一步揭示了PF如何触发和干预、技能如何内化以及技能库稳定进化的条件。
