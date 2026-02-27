---
title: "Requesting Expert Reasoning: Augmenting LLM Agents with Learned Collaborative Intervention"
authors:
  - "Zhiming Wang"
  - "Jinwei He"
  - "Feng Lu"
date: "2026-02-26"
arxiv_id: "2602.22546"
arxiv_url: "https://arxiv.org/abs/2602.22546"
pdf_url: "https://arxiv.org/pdf/2602.22546v1"
categories:
  - "cs.AI"
tags:
  - "Human-AI Collaboration"
  - "Agent Architecture"
  - "Interactive Reasoning"
  - "Tool Use"
  - "Planning"
  - "Expert Knowledge"
relevance_score: 9.0
---

# Requesting Expert Reasoning: Augmenting LLM Agents with Learned Collaborative Intervention

## 原始摘要

Large Language Model (LLM) based agents excel at general reasoning but often fail in specialized domains where success hinges on long-tail knowledge absent from their training data. While human experts can provide this missing knowledge, their guidance is often unstructured and unreliable, making its direct integration into an agent's plan problematic. To address this, we introduce AHCE (Active Human-Augmented Challenge Engagement), a framework for on-demand Human-AI collaboration. At its core, the Human Feedback Module (HFM) employs a learned policy to treat the human expert as an interactive reasoning tool. Extensive experiments in Minecraft demonstrate the framework's effectiveness, increasing task success rates by 32% on normal difficulty tasks and nearly 70% on highly difficult tasks, all with minimal human intervention. Our work demonstrates that successfully augmenting agents requires learning how to request expert reasoning, moving beyond simple requests for help.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在专业领域任务中因缺乏长尾、隐性知识而频繁失败的问题。研究背景是，尽管LLM在通用推理上表现出色，但在依赖特定领域专长（如罕见事实或复杂策略）的任务中，其训练数据往往无法覆盖所需知识，导致泛化能力严重不足。现有方法存在明显缺陷：单纯通过微调增加数据难以涵盖所有实践性策略（如“向下挖掘寻找石头”这类情境化启发知识），而使用静态工具（如游戏维基）虽能提供事实规则，却无法根据智能体的具体执行上下文提供动态、针对性的战略建议。

因此，本文的核心问题是：如何有效且高效地桥接智能体与人类专家之间的协作，以弥补这种多层次的知识缺口？直接引入人类专家虽能提供所需知识，但原始的人类指导往往是非结构化且不可靠的，若被智能体直接使用，可能导致效率低下甚至引发新错误。关键在于，智能体不仅需要获取建议，更需要学会在何时请求帮助以及如何将非结构化的专家推理转化为可靠、可执行的行动计划。为此，论文提出了AHCE框架，其核心创新在于通过一个学习到策略的人类反馈模块（HFM），将人类专家视为一种交互式推理工具，主动引导结构化对话以提炼和合成专家知识，从而实现按需的、最小化人工干预的人机协同，最终提升智能体在复杂任务中的成功率和自主性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大方向。在方法层面，强化学习是增强大语言模型（LLM）能力的关键技术。其重要发展包括基于人类反馈的强化学习（RLHF），以及后续的改进方法如直接偏好优化（DPO）、模拟偏好优化（SimPO）和群体相对策略优化（GRPO）。近期也有研究开始探索利用强化学习来增强LLM使用工具进行推理的能力。本文与这些工作的关系在于，同样利用强化学习来优化策略，但核心区别在于将人类专家本身视为一个特殊的“交互式推理工具”来学习协作，而不仅仅是优化模型参数或使用静态工具。

在应用层面，特别是在Minecraft游戏智能体领域，相关研究经历了技术演进。早期工作采用分层强化学习、奖励塑形等方法；随后的大规模方法涉及视频数据预训练（VPT）、学习世界模型（DreamerV3），或使用语言对齐表征进行指令跟随（MineCLIP, Steve-1）。当前范式已转向使用LLM作为零样本规划器，并利用多模态大语言模型进行视觉感知。本文与这些应用研究的关系是共享Minecraft这一测试平台，但根本区别在于：现有工作主要致力于构建完全自主的智能体，其能力受限于模型固有的静态知识；而本文则背离这一趋势，提出让智能体在面对未知挑战时，能够主动寻求最小化的人类指导来弥补知识缺口，实现了从完全自主到按需人机协作的范式转变。

### Q3: 论文如何解决这个问题？

论文通过提出AHCE框架来解决LLM智能体在专业领域因缺乏长尾知识而失败的问题。其核心方法是构建一个按需人机协作系统，让智能体在遇到关键瓶颈时，能主动且高效地寻求人类专家的指导，而非被动请求完整解决方案。

整体框架在基线MP5-core上集成了三个关键模块：问题识别模块、人类反馈模块和查询执行模块。其创新架构设计遵循“先自主尝试，后寻求帮助”的原则，以最大化智能体自主性并最小化人类干预。工作流程始于智能体接收高级任务，由零样本LLM规划器分解为子任务。执行失败后，智能体首先进入自我纠正循环。仅当自我纠正反复失败时，PIM才激活人机协作协议。PIM采用基于子任务执行超时和累计失败次数的机制来判断是否“真正陷入困境”，其决策函数由可配置的超参数控制，实现了任务成功率与人类负担之间的权衡。

核心创新在于人类反馈模块。HFM将人类专家概念化为一个可学习的交互式工具，通过强化学习微调LLM，以掌握如何与专家协作推理。具体而言，HFM采用分组相对策略优化算法进行训练，优化其生成一系列思维和查询的能力，以引导并整合人类知识。在交互过程中，HFM通过特殊标签进行迭代式生成：在<think>标签内进行推理，当需要外部信息时，在<search>标签内生成查询以触发与专家的交互。专家回复被包装在<result>标签中并反馈给LLM，HFM据此继续推理，直至合成完整的最终计划并封装在<Answer>标签中。这种方法使智能体能主动将专家整合到其迭代推理过程中，从而合成结构化、可执行的纠正计划，避免了直接使用非结构化专家建议导致的不稳定结果。

最后，查询执行模块负责将HFM生成的高级文本指导转化为可执行的策略。它通过两种方式将人类专业知识转化为具体行动：对于规划层面的修正，它将建议动态注入规划器的系统提示中，实现情境学习；对于执行层面的死锁，它能解析文本并触发预定义的低级控制策略来帮助智能体脱离困境。通过这种协同指导，QEM确保了人类知识被有效转化为任务成功。

### Q4: 论文做了哪些实验？

该论文在Minecraft环境中进行了系统实验，以验证所提出的AHCE框架在提升LLM智能体处理复杂任务方面的有效性。实验设置基于MineDojo仿真环境，使用程序生成的世界以确保评估的泛化性。核心模块HFM基于Qwen-2.5-7B-Instruct和Qwen-2.5-32B-Instruct模型构建，并特意在MuSiQue多跳问答数据集上训练，以避免模型记忆游戏特定知识，专注于学习协作推理技能。

实验基准测试采用了MP5提出的开放世界、过程依赖型任务，共包含15个不同任务，按难度分为简单、中等和困难三类。主要对比方法包括：1) MP5-core（完全自主的基线智能体）；2) AHCE-log（去除HFM的消融版本，仅将行动日志直接提交给人类专家求助）。评估指标包括任务成功率、人类交互时间、总执行时间及人类参与时间占比。

主要结果显示，在中等难度任务中，AHCE-Qwen-32B-Instruct将成功率从MP5-core的64%提升至96%；在困难任务中，成功率从10%大幅提升至82%。同时，HFM显著降低了人类负担：在困难任务中，人类交互时间从AHCE-log的310.1秒减少至79.4秒，人类参与时间占比从20.5%降至6.3%。消融实验进一步表明，对于复杂任务（如制作石镐），过度增加智能体自主尝试次数（n_max）会导致成功率急剧下降，而适量的人类干预对克服核心知识缺口至关重要。

### Q5: 有什么可以进一步探索的点？

本文提出的AHCE框架在整合人类专家知识方面取得了显著进展，但其局限性和未来探索方向仍值得深入探讨。首先，框架在Minecraft环境中的验证虽具说服力，但尚未扩展到更复杂、开放的现实世界场景，其泛化能力有待检验。其次，依赖人类专家作为“交互式推理工具”可能面临可扩展性问题，尤其在需要多位专家或实时响应的场景中。此外，当前方法主要关注如何请求专家推理，但对专家反馈的质量评估与纠错机制涉及较少，若专家提供错误或模糊指导，可能影响整体决策。

未来研究方向可包括：1）开发自适应策略，使智能体不仅能请求帮助，还能评估专家反馈的可靠性，并学会在冲突建议中做出权衡；2）探索多专家协同机制，通过聚合不同领域专家的知识提升决策鲁棒性；3）将框架与外部知识库或工具调用结合，减少对人类干预的依赖，实现半自动化知识获取。此外，可研究如何将“协作推理”能力迁移到其他模态（如视觉、物理交互任务），推动智能体在医疗、科研等专业领域的应用。

### Q6: 总结一下论文的主要内容

该论文提出了AHCE框架，旨在解决大语言模型（LLM）智能体在依赖长尾知识的专业领域中表现不佳的问题。其核心问题是，虽然人类专家能提供缺失知识，但其指导往往非结构化且不可靠，难以直接整合到智能体的规划中。

论文的核心贡献是设计了一种按需人机协作方法。其核心是“人类反馈模块”，该模块通过学习一个策略，将人类专家视为一个交互式推理工具来主动调用，而非简单地请求帮助。该方法在《我的世界》游戏环境中进行了广泛实验验证。

主要结论表明，该框架能显著提升任务成功率：在普通难度任务上提高32%，在高难度任务上提升近70%，且所需人类干预极少。这证明了通过“学习如何请求专家推理”来增强智能体，比单纯求助更为有效，为人机协作智能体的发展提供了新思路。
