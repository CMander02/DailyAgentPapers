---
title: "From Moderation to Mediation: Can LLMs Serve as Mediators in Online Flame Wars?"
authors:
  - "Dawei Li"
  - "Abdullah Alnaibari"
  - "Arslan Bisharat"
  - "Manny Sandoval"
  - "Deborah Hall"
date: "2025-12-02"
arxiv_id: "2512.03005"
arxiv_url: "https://arxiv.org/abs/2512.03005"
pdf_url: "https://arxiv.org/pdf/2512.03005v5"
categories:
  - "cs.AI"
tags:
  - "Human-Agent Interaction"
  - "Reasoning & Planning"
relevance_score: 5.5
taxonomy:
  capability:
    - "Human-Agent Interaction"
    - "Reasoning & Planning"
  domain: "Social & Behavioral Science"
  research_type: "Empirical Study/Analysis"
attributes:
  base_model: "N/A"
  key_technique: "mediation framework (judgment and steering subtasks)"
  primary_benchmark: "Reddit-based dataset (constructed)"
---

# From Moderation to Mediation: Can LLMs Serve as Mediators in Online Flame Wars?

## 原始摘要

The rapid advancement of large language models (LLMs) has opened new possibilities for AI for good applications. As LLMs increasingly mediate online communication, their potential to foster empathy and constructive dialogue becomes an important frontier for responsible AI research. This work explores whether LLMs can serve not only as moderators that detect harmful content, but as mediators capable of understanding and de-escalating online conflicts. Our framework decomposes mediation into two subtasks: judgment, where an LLM evaluates the fairness and emotional dynamics of a conversation, and steering, where it generates empathetic, de-escalatory messages to guide participants toward resolution. To assess mediation quality, we construct a large Reddit-based dataset and propose a multi-stage evaluation pipeline combining principle-based scoring, user simulation, and human comparison. Experiments show that API-based models outperform open-source counterparts in both reasoning and intervention alignment when doing mediation. Our findings highlight both the promise and limitations of current LLMs as emerging agents for online social mediation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探索大型语言模型（LLMs）能否从传统的“内容审核”角色转变为“冲突调解”角色，以应对在线讨论中持续存在的敌对行为（如“骂战”）问题。研究背景是，随着LLMs日益介入在线交流，其在促进数字社区共情、公平和建设性对话方面的潜力，已成为负责任AI研究的重要前沿。当前，大多数计算方法主要聚焦于“审核”，即通过检测毒性或标记有害内容进行事后处理（如删除或惩罚），这种方法是被动且反应式的，虽能抑制有害言论，却无法解决引发冲突的深层社会动态，可能导致敌意反复出现。

现有方法的不足在于其“治标不治本”：它们缺乏对多轮对话语境、情感演变和冲突升级模式的理解，无法主动引导对话走向和解。因此，本文要解决的核心问题是：LLMs能否不仅作为审核者，更能作为调解者，理解并化解在线冲突？具体而言，研究将调解任务分解为两个子任务：一是“判断”，即评估对话的公平性、情感动态和升级点；二是“引导”，即生成共情、降级的消息，引导参与者关注分歧根源而非相互攻击。通过构建大规模真实骂战数据集和设计多阶段评估流程，论文系统检验了LLMs在调解中的能力、效果与局限。

### Q2: 有哪些相关研究？

本文的相关工作主要涉及两个领域：AI for Social Good（人工智能向善）和在线冲突（Flame Wars）研究。

在AI for Social Good方面，已有大量研究将AI技术应用于解决社会问题，例如在教育领域利用LLMs进行阅读写作辅助、内容创作和自动反馈，在医疗健康领域用于医学问答和辅助诊断。这些工作展示了LLMs作为有益工具的潜力，但多集中于提供辅助或生成内容，而非主动介入并引导复杂的人际互动过程。

在在线冲突研究方面，现有计算工作主要集中在**内容审核（Moderation）**，即通过检测和过滤有毒言论来管理社区。这类方法通常是单向的、预防性的，旨在移除有害内容。然而，本文指出，对于“火焰战争”这种双方情绪投入、逐步升级的互动冲突，简单的过滤可能抑制合理的参与，且缺乏建设性。

本文的研究与上述工作的核心区别在于，它超越了被动的“审核”，提出了主动的“调解（Mediation）”框架。本文的LLM调解员被赋予双重任务：**判断**对话的公平性与情绪动态，以及**引导**生成共情、降级的消息以推动解决。这要求模型具备更深层的语境理解、心理推理和策略性沟通能力，旨在化解冲突而非仅仅屏蔽它，属于方法上的创新与深化。

### Q3: 论文如何解决这个问题？

论文通过提出一个将在线冲突调解分解为“判断”和“引导”两个子任务的框架来解决LLM作为调解者的问题。整体框架首先接收一个包含敌对或分歧的在线讨论线程作为输入，随后分两步处理：第一步是判断子任务，要求LLM对对话进行分析推理，生成一个解释性表征，用以识别不公平的主张、情绪触发点和升级点，并评估各方论点的公平性与相关性；第二步是引导子任务，LLM基于对话内容（并可选择性地结合判断结果）生成一个具有上下文感知能力、富有同理心的调解消息，旨在减少敌意、承认各方关切，并引导参与者走向建设性的解决方案。

核心架构设计围绕这两个主要模块展开。判断模块充当分析引擎，其关键技术在于让LLM进行深度的评估性推理，理解冲突的动态、情绪脉络和逻辑缺陷。引导模块则作为生成引擎，其创新点在于要求模型不仅生成文本，还需产出具备特定调解功能（如去升级化、共情、促进合作）的话语。两个模块可串联工作，形成“分析后干预”的流程，体现了从被动内容审核到主动对话引导的范式转变。

为评估该框架，论文构建了基于Reddit的大规模数据集，并提出了一个结合原则性评分、用户模拟和人工比较的多阶段评估流程。这种方法上的创新确保了调解质量的综合衡量。实验表明，基于API的模型在推理和干预对齐方面优于开源模型，这凸显了当前LLM在作为在线社交调解新兴智能体方面的潜力与局限性。整个方案的核心创新在于系统性地定义了LLM的调解能力，并将其操作化为可评估的连贯任务流程。

### Q4: 论文做了哪些实验？

论文实验围绕评估大语言模型作为在线冲突调解员的能力展开。实验设置方面，研究者评估了12个大语言模型，包括开源模型（如LLaMA-3.2-3B、Qwen2.5-7B等）和API模型（如Claude 3.5-Haiku、GPT-4.1等）。开源模型使用vLLM进行本地推理，API模型通过官方接口调用；所有实验在两块NVIDIA A100 GPU上运行。数据集基于Reddit构建，用于模拟在线争论场景。

评估采用多阶段流程，包括基于原则的评分、用户模拟和人工比较。基于原则的评分将调解分解为“判断”和“引导”两个子任务，从六个主题（游戏、生活方式、宗教、社会正义、体育、技术）进行衡量。关键指标显示，API模型在调解任务上普遍优于开源模型：例如，Claude 4.5-Haiku在判断和引导任务上的平均得分约为8.41，而开源模型如Qwen3-8B得分为8.23，LLaMA-3.1-8B为7.86。在敏感主题（如宗教、体育）上，模型得分较低（约7.8-8.2），而在中性主题（如游戏、生活方式）上表现更好（常超过8.4）。

用户模拟实验进一步评估了调解对对话特征的影响，包括毒性、大写使用、感叹号和争论性。结果显示，调解能有效降低毒性（如Qwen3-4B将毒性从39.92降至25.42）和感叹号使用，但对争论性影响较小。与人类调解相比，LLM生成的内容更长、词汇密度更高，但可读性较低，且代词使用更中性，体现出不同的语言风格。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估主要基于模拟环境和静态数据集，未能充分测试LLMs在实时、动态在线冲突中的实际表现。未来研究可探索以下方向：一是开发更复杂的多轮交互评估框架，模拟真实用户的情感变化和对抗性回应，以检验LLMs的长期调解效果；二是研究个性化调解策略，使LLMs能根据用户文化背景、语言风格和冲突历史动态调整干预方式；三是探索多模态调解能力，结合文本、语音甚至表情符号来增强共情表达。此外，可尝试将LLMs与人类调解员协作，构建混合智能系统，其中LLMs处理初步情绪识别和常规解旋，复杂案例则移交人类专家。最后，需深入解决伦理问题，如调解过程中的偏见放大、隐私保护及责任归属，这需要跨学科合作建立相关标准和监管框架。

### Q6: 总结一下论文的主要内容

该论文探讨了大型语言模型（LLM）在在线冲突中扮演调解者而非仅内容审核者的潜力。核心问题在于LLM能否理解并化解网络骂战，推动共情与建设性对话。作者提出一个将调解分解为“判断”与“引导”两阶段的框架：判断阶段评估对话的公平性与情绪动态，引导阶段生成共情、降级的消息以促进解决。为评估效果，研究构建了基于Reddit的大型数据集，并设计了结合原则评分、用户模拟和人工比较的多阶段评估流程。实验表明，基于API的模型在调解任务中，其推理和干预对齐能力均优于开源模型。结论指出，当前LLM作为在线社交调解新兴代理工具虽具前景，但仍存在局限性，这为负责任AI研究提供了重要方向。
