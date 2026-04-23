---
title: "EvoAgent: An Evolvable Agent Framework with Skill Learning and Multi-Agent Delegation"
authors:
  - "Aimin Zhang"
  - "Jiajing Guo"
  - "Fuwei Jia"
  - "Chen Lv"
  - "Boyu Wang"
  - "Fangzheng Li"
date: "2026-04-22"
arxiv_id: "2604.20133"
arxiv_url: "https://arxiv.org/abs/2604.20133"
pdf_url: "https://arxiv.org/pdf/2604.20133v1"
categories:
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Skill Learning"
  - "Multi-Agent Delegation"
  - "Hierarchical Planning"
  - "Memory"
  - "Closed-Loop Learning"
  - "Evaluation"
relevance_score: 8.0
---

# EvoAgent: An Evolvable Agent Framework with Skill Learning and Multi-Agent Delegation

## 原始摘要

This paper proposes EvoAgent - an evolvable large language model (LLM) agent framework that integrates structured skill learning with a hierarchical sub-agent delegation mechanism. EvoAgent models skills as multi-file structured capability units equipped with triggering mechanisms and evolutionary metadata, and enables continuous skill generation and optimization through a user-feedback-driven closed-loop process. In addition, by incorporating a three-stage skill matching strategy and a three-layer memory architecture, the framework supports dynamic task decomposition for complex problems and long-term capability accumulation. Experimental results based on real-world foreign trade scenarios demonstrate that, after integrating EvoAgent, GPT5.2 achieves significant improvements in professionalism, accuracy, and practical utility. Under a five-dimensional LLM-as-Judge evaluation protocol, the overall average score increases by approximately 28%. Further model transfer experiments indicate that the performance of an agent system depends not only on the intrinsic capabilities of the underlying model, but also on the degree of synergy between the model and the agent architecture.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）智能体在复杂专业领域（如外贸）中执行任务时面临的核心挑战：现有方法难以高效、低成本地获取并应用复杂技能，且多智能体协作框架缺乏自适应演化能力。

研究背景是，LLM智能体已成为在复杂开放环境中实现自主任务执行的核心范式。在软件工程、金融分析等专业领域，任务日益呈现多步骤、跨领域、高结构化的特点，其复杂性远超单一原子工具的能力范围。为此，研究者引入了“技能”作为更高层次的能力封装，以提供系统化、可复用的流程支持。

然而，现有方法存在明显不足。首先，技能获取严重依赖人工编写，成本高、可扩展性差，且难以保证跨领域质量一致性。其次，人工构建的技能流程可能与LLM的内在推理模式不匹配，导致在高度结构化领域性能下降。再者，现有的自我进化方法多聚焦于单个工具或提示的启发式优化，缺乏对复杂多文件技能包进行系统化迭代生成、优化和验证的机制。最后，许多自我改进框架依赖真实标注数据或密集专家反馈，这在现实部署中往往难以满足。同时，主流的多智能体框架通常采用静态角色定义和固定任务路由策略，缺乏基于历史经验动态演化委托逻辑、技能集和协作模式的自适应机制，且技能自我进化与分层多智能体任务委托之间的整合有限。

因此，本文要解决的核心问题是：如何构建一个可进化的智能体框架，以弥合上述差距。具体而言，论文提出了EvoAgent框架，其核心目标是**将自主技能学习与分层多智能体任务委托机制相集成**，从而在无需大量人工标注或专家干预的情况下，实现智能体在复杂现实场景中能力的持续、可控增长与优化。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为方法类、应用类和评测类，其中方法类又可细分为技能学习、多智能体协作和约束工程等方向。

在**技能学习**方面，相关研究主要关注如何从任务执行轨迹中抽象可复用的能力单元。例如，通过策略总结将成功任务步骤模板化，或通过反思机制分析失败轨迹以修正策略，以及采用检索增强记忆来调用历史成功案例。然而，这些方法通常依赖于固定的提示框架或预定义策略模式，缺乏对技能生命周期（生成、评估、固化、淘汰）的系统建模，且能力更新往往是隐式的，缺少结构化、可转移的技能表示。本文的EvoAgent则明确将技能建模为多文件结构化单元，并设计了由用户反馈驱动的闭环过程来实现技能的持续生成与优化，从而支持长期能力积累。

在**多智能体协作**方面，代表性工作如ReAct框架通过“推理-行动-观察”循环增强复杂任务处理能力；CAMEL通过角色化对话模拟协作；AutoGen提出了可编排的多智能体对话框架。这些方法通常采用预定义角色和固定通信协议，协作结构在系统设计时静态确定，难以基于历史交互结果持续优化，且角色专业化与可转移技能积累机制结合不深。EvoAgent通过分层子智能体委托机制和动态任务分解，旨在实现技能学习与系统架构扩展的协同进化。

在**约束工程（Harness Engineering）** 这一新兴范式中，研究强调通过外部结构化控制层来约束、引导和集成模型行为，构建稳定、可观测、可进化的智能体系统。相关论述提出了约束、可观测性和反馈循环三大支柱，以及指导/感知与计算/推理的分析矩阵。EvoAgent继承并扩展了这一范式，通过结构化分离在线执行循环与离线进化循环，在强约束执行与能力进化之间取得了工程平衡。

此外，在**自改进与经验反思**方面，如Reflexion、Voyager和Generative Agents等工作探索了反馈循环、技能库构建和长期记忆机制，但同样缺乏显式的结构化技能表示。本文的框架试图统一结构化流程控制、轻量级多角色协作和显式技能积累机制，以应对实际业务场景中对可持续进化与能力转移的需求。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为EvoAgent的可进化智能体框架来解决智能体在开放环境中持续学习和优化能力的问题。其核心方法是将结构化技能学习与分层委托机制相结合，并采用用户反馈驱动的闭环进化流程。

整体框架采用分层设计，包含API入口层、编排层、运行时层、工具与会话层以及持久层。核心架构创新在于**三层委托路由机制**和**共享运行时设计**，实现了高效的任务分发与上下文管理。系统基于ReAct循环进行推理与行动，并通过渐进式披露策略优化上下文使用。

关键技术包括：
1.  **结构化技能建模**：将技能定义为包含名称、描述、触发词、执行指令、参考文件和元数据（使用次数、成功率等）的多文件单元，支持懒加载和版本管理。
2.  **三阶段技能匹配策略**：依次进行关键词匹配、向量嵌入相似度匹配和LLM语义匹配，在保证准确性的同时兼顾效率。
3.  **双循环执行机制**：
    *   **在线执行循环**：实时响应用户请求，完成技能匹配、上下文装配、任务执行及动态历史压缩（生成“资产索引”以保持关键信息）。
    *   **离线进化循环**：在会话后异步运行，负责用户画像与记忆的更新（通过实时收集、初始引导、会话后分析等多维机制），并基于使用数据评估技能成熟度（分为萌芽、成长、成熟、精通四级），进而生成新技能或优化现有技能。
4.  **形式化MDP建模**：将进化过程建模为马尔可夫决策过程，状态空间包含对话历史、用户画像、技能库状态和压缩状态，奖励函数是技能成熟度、用户画像更新幅度和记忆更新幅度的加权组合，优化目标是最大化长期累积奖励。该理论目标通过上述隐式的双循环机制在工程上实现。

创新点在于提出了 **“用户反馈驱动（User-in-the-loop）”** 的进化范式，将明确的数值奖励最大化目标，编译为一个由在线可靠执行和离线深度优化协同的、稳定的异步进化循环，从而在无需显式编程或标注数据监督的情况下，实现智能体能力的自主积累与持续优化。

### Q4: 论文做了哪些实验？

论文实验围绕三个研究问题展开。实验设置上，以GPT5.2作为基础模型，并设计了一个基于ReAct的框架来支持外贸场景的复杂工作流。对比方法为直接调用GPT5.2与GPT5.2集成EvoAgent框架两种设置。

数据集方面，通过参数化脚本程序化生成了覆盖12个预定义外贸场景的高质量多轮对话样本，最终构建了包含172个评估实例的测试集，确保了评估的专业性和无偏性。

主要结果如下：在五维LLM-as-Judge评估中，集成EvoAgent后，GPT5.2在专业性（从2.703提升至4.762）、准确性（从2.907提升至4.238）、实用性（从3.744提升至4.709）和语言质量（从4.052提升至4.779）上均有显著提升，完整性保持稳定（4.331 vs 4.215）。整体平均分从3.547提升至4.541，增幅约28%（27.998%）。

模型迁移实验表明，EvoAgent的效果具有模型异质性。集成EvoAgent后，GPT4.1平均性能下降约13%，其整体性能约为EvoAgent增强版GPT5.2的75%；Qwen3.5-35B-A3B的性能降至其独立版本的约85%，约为增强版GPT5.2的74.5%。

系统性能测试显示，EvoAgent在420轮对话中仅触发6次压缩，无运行时错误；平均响应时间在早期约12秒，120轮后稳定在约24秒。

### Q5: 有什么可以进一步探索的点？

基于论文内容，EvoAgent框架在技能学习和多智能体委托方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其实验数据主要基于程序化生成的合成查询，虽力求结构公正，但分布仍与部署环境相关，未来需要在完全独立的外贸语料库上评估其跨分布泛化能力。其次，框架对不同基座模型（如GPT4.1、Qwen）表现出异构效应，性能提升不稳定，这提示智能体架构与模型本身的兼容性至关重要，未来需通过消融实验厘清提示工程、技能注入格式等因素的具体影响。此外，系统目前仅支持单技能调用，缺乏多技能编排与并行执行机制，限制了处理复杂交叉任务的能力；记忆模块也存在压缩导致信息丢失、缺乏自动剪枝等问题。从工程角度看，实时适应性不足是一个关键瓶颈——进化循环仅在会话结束后触发，无法在技能退化或意图转移时进行动态调整。未来可探索在线学习机制，实现实时技能优化与用户画像更新；同时，开发成本跟踪、监控仪表盘等企业级功能也将提升其落地实用性。最后，将框架扩展至更广泛的领域（如医疗、法律），并研究其与不同规模开源模型的协同优化，也是富有潜力的方向。

### Q6: 总结一下论文的主要内容

该论文提出了EvoAgent，一个面向现实世界外贸场景的可进化统一智能体框架。其核心贡献在于通过结构化技能表示、用户驱动的自进化机制和分层任务委派架构，构建了一个集技能学习、任务执行和长期记忆管理于一体的闭环系统。问题定义聚焦于如何使大语言模型智能体具备持续学习和适应复杂现实任务的能力。

方法上，EvoAgent将技能建模为具备触发机制和进化元数据的多文件结构化能力单元，并通过用户反馈驱动的闭环过程实现技能的持续生成与优化。框架结合三阶段技能匹配策略与三层记忆架构，以支持复杂任务的动态分解和长期能力积累。

主要结论显示，集成EvoAgent后，基础模型在专业性、准确性和实用性上均获得显著提升，在基于五维LLM-as-Judge的评估中平均得分提升约28%。研究进一步揭示，智能体系统的性能不仅取决于底层模型的内在能力，更关键地取决于模型与智能体架构之间的协同程度，这为构建具备持续成长能力的下一代自主智能体系统提供了理论视角与实践基础。
