---
title: "AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution"
authors:
  - "Yutao Yang"
  - "Junsong Li"
  - "Qianjun Pan"
  - "Bihao Zhan"
  - "Yuxuan Cai"
  - "Lin Du"
  - "Jie Zhou"
  - "Kai Chen"
  - "Qin Chen"
  - "Xin Li"
  - "Bo Zhang"
  - "Liang He"
date: "2026-03-01"
arxiv_id: "2603.01145"
arxiv_url: "https://arxiv.org/abs/2603.01145"
pdf_url: "https://arxiv.org/pdf/2603.01145v2"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "Agent 自演化"
  - "Agent 记忆"
  - "个性化"
  - "技能学习"
  - "终身学习"
  - "经验驱动"
  - "模型无关"
relevance_score: 9.5
---

# AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution

## 原始摘要

In practical LLM applications, users repeatedly express stable preferences and requirements, such as reducing hallucinations, following institutional writing conventions, or avoiding overly technical wording, yet such interaction experience is seldom consolidated into reusable knowledge. Consequently, LLM agents often fail to accumulate personalized capabilities across sessions. We present AutoSkill, an experience-driven lifelong learning framework that enables LLM agents to automatically derive, maintain, and reuse skills from dialogue and interaction traces. AutoSkill abstracts skills from user experience, supports their continual self-evolution, and dynamically injects relevant skills into future requests without retraining the underlying model. Designed as a model-agnostic plugin layer, it is compatible with existing LLMs and introduces a standardized skill representation for sharing and transfer across agents, users, and tasks. In this way, AutoSkill turns ephemeral interaction experience into explicit, reusable, and composable capabilities. This paper describes the motivation, architecture, skill lifecycle, and implementation of AutoSkill, and positions it with respect to prior work on memory, retrieval, personalization, and agentic systems. AutoSkill highlights a practical and scalable path toward lifelong personalized agents and personal digital surrogates.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在现实应用中难以将重复的用户交互经验（如稳定偏好和操作要求）转化为可重用、可积累的个性化能力的问题。研究背景是，随着LLM智能体从基准测试走向实际部署，用户经常在不同会话中反复表达相似的需求（例如减少幻觉、遵循特定写作风格），但现有方法未能有效将这些经验固化为持久的技能。

现有方法存在明显不足：参数更新或自演化方法虽能通过反馈优化模型行为，但成本高昂且难以精细控制；基于记忆的方法（如检索增强）主要将历史交互作为文本存储和召回，而非可操作的行为模式；现有的智能体框架或技能学习方法则往往将技能隐含在提示词或策略中，缺乏显式、可维护的表示。这些方法都未能系统地将重复的交互经验转化为显式、可复用且可长期演化的技能。

因此，本文的核心问题是：如何设计一个机制，能够自动从LLM智能体与用户的对话和交互轨迹中抽象、维护和复用“技能”，从而实现持续、低成本的生命周期学习，使智能体能够积累个性化能力，而无需重新训练基础模型。AutoSkill框架即针对此问题提出，它通过将经验转化为结构化的技能表示，支持技能的自我演化与动态注入，旨在弥合短期交互与长期能力发展之间的鸿沟。

### Q2: 有哪些相关研究？

本文的相关研究主要可归纳为以下四类：

**1. 经验驱动的终身学习**：这类研究关注智能体如何从持续交互中积累可复用的知识、策略或策略，使过往经验能支持未来任务。代表性工作包括ELL框架及其基准StuLife。AutoSkill与其目标一致，但区别在于知识表示方式：AutoSkill将可复用能力具体化为显式的、可版本化演进的SKILL.md文件，而非隐式的记忆或策略适应，从而提升了可解释性和人工编辑能力。

**2. 大语言模型的自进化方法**：这类方法旨在通过自我反思、迭代重写、反馈驱动优化或自主数据构建来改进模型行为。代表工作包括SELF、RISE、SEC和UPO等。AutoSkill与此类研究互补，它不更新模型参数，而是将可复用行为外化为结构化技能文件，并通过显式的修订、合并和版本控制来支持其进化，使改进过程更透明可控。

**3. 语言智能体的长期记忆机制**：这类工作包括检索增强生成（RAG）及其扩展（如REALM、RETRO），以及面向长期存储和跨会话管理的系统（如MemoryBank、MemGPT、生成式智能体架构）和相关评测基准（如LoCoMo）。AutoSkill借鉴了检索可激活有用经验的洞见，但超越了传统的文本片段记忆，通过显式的技能抽象、检索和维护，更适合保存那些难以用原始文本片段表示的稳定偏好、风格约束和重复性工作流。

**4. 面向推理与行动的技能学习**：这类研究关注LLM智能体获取可复用的推理模式、工具使用流程和行动策略。代表性方法包括ReAct、Toolformer、ART、Voyager等，以及相关评测环境（如WebShop、AgentBench）。AutoSkill针对现有方法中技能通常隐式存在于提示、轨迹或潜在策略中的局限，将技能视为一等公民，支持从交互经验中显式提取、由用户编辑、跨迭代合并、版本化管理并动态注入未来任务，实现了可控的持续技能进化。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AutoSkill的免训练终身学习框架来解决LLM智能体难以积累和复用个性化交互经验的问题。其核心方法是：将用户对话中稳定的偏好和需求抽象为可版本化的“技能”，通过两个耦合的循环（技能增强的响应生成与技能演化）实现技能的持续积累与复用，而无需更新底层模型参数。

整体框架由五个基于提示词驱动的模块和一个嵌入模型组成，形成一个模块化的推理时组合系统。主要模块包括：查询重写模型、对话响应模型、技能提取模型、技能管理判断模型、技能合并模型以及用于技能向量化的嵌入模型。这些模块均通过特定提示词调用通用LLM实现，确保了框架的模型无关性和灵活性。

关键技术细节与创新点体现在以下几个方面：
1.  **技能表示与检索**：每个技能被标准化表示为包含名称、描述、可执行指令提示、触发词集合、标签集、示例集和版本号的元组。检索时，系统首先对用户查询进行重写以突出检索关键约束，然后结合稠密语义相似度（通过嵌入模型计算）和词法BM25分数进行混合检索，筛选出相关技能注入响应生成上下文。
2.  **训练免费的技能演化循环**：技能提取阶段仅以用户查询序列（而非模型回复）为证据，通过提取提示识别可复用的持久性知识（如偏好、流程、约束），生成技能候选。随后，系统通过管理判断模型，将候选技能与技能库中检索到的最相似现有技能进行比较，决定“添加”、“合并”或“丢弃”。若选择“合并”，则通过合并模型进行版本化更新，整合新约束或细节，实现技能的迭代精化。
3.  **模块化与可扩展性**：所有功能均通过提示工程实现，不同模块可共享同一骨干LLM。这种设计使系统无需重新训练即可更换响应模型、提取模型或嵌入模型，具备高度灵活性。
4.  **经验外显与共享**：该框架将瞬时的交互经验转化为显式、可复用、可组合的技能单元，并通过标准化的技能表示支持跨智能体、用户和任务的技能共享与迁移。

总之，AutoSkill通过构建一个外部的、可动态演化的技能记忆库，并设计一套完整的基于提示词的技能生命周期管理流程，实现了LLM智能体在持续交互中积累和复用个性化能力的目标，为构建终身个性化智能体提供了一条实用且可扩展的路径。

### Q4: 论文做了哪些实验？

论文的实验主要围绕验证AutoSkill框架在从对话历史中提取、维护和重用技能的有效性展开。实验设置上，作者构建了一个包含多语言、多模型对话历史的数据集，用于离线评估技能提取的规模和质量。数据集基于真实用户与GPT-3.5和GPT-4的对话，分为中文和英文子集，总计包含超过22,000个对话和约60万条消息。实验没有明确提及与其他方法的直接量化对比，但通过分析提取出的技能来评估系统能力。

主要结果通过多个表格和图表展示。关键数据指标包括：从四个数据子集中共提取了1858个技能，其中编程与软件开发类最多（482个），其次是写作与内容创作（363个）以及数据与AI/ML（354个）。技能提取的密度约为每1000条消息产生3-4个技能。此外，对技能标签的分析显示了高频的领域关键词，如“python”（98次）、“javascript”（38次）等，表明系统能捕捉到具体的技术偏好。技能类别分布图进一步证实了提取技能覆盖了广泛的实用领域。这些实验结果表明，AutoSkill能够从海量、杂乱的对话历史中自动抽象出大量、高质量、可分类的持久化技能，验证了其作为终身学习层的可行性。

### Q5: 有什么可以进一步探索的点？

该论文提出的AutoSkill框架在技能自动提取与复用方面具有创新性，但仍存在若干局限和可拓展方向。首先，技能抽象的质量高度依赖交互数据的质量和规模，在稀疏或噪声较多的场景下可能难以生成可靠技能。其次，当前技能演化机制可能缺乏对长期技能效用和冲突的评估，未来可引入基于反馈的强化学习来优化技能选择与组合策略。此外，框架尚未充分考虑多模态交互中的技能迁移，例如从文本对话中提取的规则能否适用于视觉或语音场景。另一个重要方向是跨用户的隐私保护型技能共享，如何在加密或联邦学习环境下实现技能的安全交换仍需探索。最后，将技能系统与因果推理结合，使技能不仅基于关联还能理解用户需求背后的因果机制，可进一步提升个性化适应的深度和可解释性。

### Q6: 总结一下论文的主要内容

论文《AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution》针对大型语言模型（LLM）代理在长期交互中难以积累和复用个性化能力的问题，提出了一个经验驱动的终身学习框架。核心问题是用户在多轮对话中反复表达的稳定偏好（如减少幻觉、遵循特定写作风格）未被有效转化为可重用的知识，导致代理无法跨会话持续提升。

AutoSkill的核心贡献在于将交互经验视为技能形成的来源，而非仅作为记忆存储。方法上，它设计了一个模型无关的插件层，通过技能生命周期（包括从对话中提取候选技能、将其总结为结构化的SKILL.md工件、迭代精炼以及在未来请求中动态注入相关技能）来实现技能的自动衍生、维护和复用。该方法无需重新训练底层模型，支持技能的检查、编辑和版本控制，提高了透明度和可控性。

主要结论是，AutoSkill将短暂的交互经验转化为显式、可组合、可重用的能力，为构建终身个性化代理和个人数字替身提供了一条实用且可扩展的路径。其结构化技能表示还支持跨代理、用户和任务的技能共享与迁移，在研究和系统部署层面均有重要意义。
