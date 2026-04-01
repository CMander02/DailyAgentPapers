---
title: "REFINE: Real-world Exploration of Interactive Feedback and Student Behaviour"
authors:
  - "Fares Fawzi"
  - "Seyed Parsa Neshaei"
  - "Marta Knezevic"
  - "Tanya Nazaretsky"
  - "Tanja Käser"
date: "2026-03-31"
arxiv_id: "2603.29142"
arxiv_url: "https://arxiv.org/abs/2603.29142"
pdf_url: "https://arxiv.org/pdf/2603.29142v1"
categories:
  - "cs.AI"
  - "cs.HC"
tags:
  - "Multi-Agent System"
  - "Interactive Agent"
  - "Tool Use"
  - "LLM-as-a-Judge"
  - "Educational Agent"
  - "Human-AI Interaction"
  - "System Evaluation"
relevance_score: 7.5
---

# REFINE: Real-world Exploration of Interactive Feedback and Student Behaviour

## 原始摘要

Formative feedback is central to effective learning, yet providing timely, individualised feedback at scale remains a persistent challenge. While recent work has explored the use of large language models (LLMs) to automate feedback, most existing systems still conceptualise feedback as a static, one-way artifact, offering limited support for interpretation, clarification, or follow-up. In this work, we introduce REFINE, a locally deployable, multi-agent feedback system built on small, open-source LLMs that treats feedback as an interactive process. REFINE combines a pedagogically-grounded feedback generation agent with an LLM-as-a-judge-guided regeneration loop using a human-aligned judge, and a self-reflective tool-calling interactive agent that supports student follow-up questions with context-aware, actionable responses. We evaluate REFINE through controlled experiments and an authentic classroom deployment in an undergraduate computer science course. Automatic evaluations show that judge-guided regeneration significantly improves feedback quality, and that the interactive agent produces efficient, high-quality responses comparable to a state-of-the-art closed-source model. Analysis of real student interactions further reveals distinct engagement patterns and indicates that system-generated feedback systematically steers subsequent student inquiry. Our findings demonstrate the feasibility and effectiveness of multi-agent, tool-augmented feedback systems for scalable, interactive feedback.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大规模教育场景中提供及时、个性化、可交互的形成性反馈的难题。研究背景是，虽然反馈对学习至关重要，但在大班教学中，教师难以提供高质量的个性化反馈。近年来，研究者开始利用大语言模型（LLM）自动生成反馈，以扩大覆盖范围。然而，现有方法存在明显不足：首先，多数系统将反馈视为静态、单向的信息输出，缺乏对学生解读、澄清和后续追问的支持，这可能导致反馈与学生的实际理解和应用脱节；其次，现有方法主要依赖大型闭源模型，存在成本、隐私和可部署性等问题；再者，即使采用复杂的提示工程或多阶段流水线，生成的反馈在关键问题的识别和优先级排序上仍常不及专家教师，且这些方法通常需要大量计算资源或偏好数据，实用性受限。

本文的核心问题是：如何构建一个可本地部署、基于小型开源模型的多智能体交互式反馈系统，以支持高质量的、符合教学原理的反馈生成，并允许学生通过后续对话进行澄清和延伸，从而真正促进学生对反馈的主动参与和应用。为此，论文提出了REFINE系统，它通过一个基于教学理论的反馈生成智能体（结合了基于人类对齐的“LLM即法官”的迭代优化循环来提升反馈质量）和一个支持工具调用的交互式智能体（用于回答学生的后续问题）来共同实现一个动态的、双向的反馈过程。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**方法类**、**应用类**和**评测类**。

在**方法类**研究中，已有工作探索利用大语言模型（LLM）自动生成形成性反馈。早期方法多为基于提示的静态、单向反馈生成，虽能产生流畅的反馈，但在识别关键问题、提供可操作指导方面常不及专家教师。后续研究引入了更复杂的多阶段提示管道，结合检索增强生成（RAG）和思维链（CoT）等技术，以提高反馈的准确性和事实性。另一些工作则采用基于优化的方法，如直接偏好优化（DPO），利用专家或大模型的偏好数据来提升较小开源模型的反馈质量，但这通常需要大量数据和计算资源。**本文的REFINE系统与这些方法相关但存在区别**：它同样基于LLM，但创新性地采用了一个**多智能体、工具增强的交互式架构**，将反馈视为一个动态过程，并结合了基于人类对齐评判的迭代优化循环，而不仅仅是单次生成或静态优化。

在**应用类**研究中，多数LLM反馈系统被设计为任务完成后交付的静态产物，缺乏对学生后续澄清、理解和跟进的支持，这可能导致反馈与学习吸收之间的脱节。**本文的REFINE系统与此类工作的主要区别在于其强调交互性**，它专门设计了一个工具调用的交互式智能体，支持学生提出后续问题，从而促进对反馈的主动参与和意义建构。

在**评测类**研究中，先前工作多在受控环境中评估反馈的流畅性或与人工反馈的相似性。**本文与之相关但扩展了评测维度**：不仅通过自动评估衡量反馈质量（如通过评判引导的再生提升效果），还通过真实的课堂部署，分析学生的互动模式，研究生成的反馈内容如何引导后续对话，从而在更贴近实际的教育场景中评估系统的有效性和影响。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为REFINE的本地可部署、多智能体交互式反馈系统来解决规模化、个性化、交互式反馈的挑战。其核心方法是将反馈视为一个动态、双向的交互过程，而非静态的单向输出。

**整体框架与主要模块**：系统采用两阶段、多智能体架构。第一阶段专注于生成高质量的初始反馈，由**基于教学理论的反馈生成智能体**和**反馈LLM评判员引导的优化循环**构成。该智能体基于“目标-现状-下一步”的教学反馈理论，生成结构化的反馈报告，包含任务澄清、现状诊断、任务级/策略级下一步建议、自我调节学习支持和表扬。随后，反馈LLM评判员（一个与人类专家对齐的模型）依据细粒度的教学评估准则（如清晰度、诊断准确性、建议针对性等）对报告各组件进行二元评判。对于未达标的组件，评判员会提供针对性的修订解释，反馈生成智能体据此进行迭代修订，直至满足所有准则或达到迭代上限，从而显著提升反馈质量。

第二阶段处理学生的后续追问，由**工具调用的交互式反馈智能体**负责。该智能体以优化后的反馈报告和学生问题为输入，进行多步骤、自我反思式的推理。它能够调用一个外部**教学工具集**，该工具集支持基于检索获取课程资源（如教材、讲义）、查询先修知识依赖图，以及进行行为维度（如努力程度、一致性）的推理与解释。智能体通过一个闭环推理过程，动态规划工具调用序列，整合工具返回的观察结果，并能从执行错误中恢复，最终生成情境感知、可操作的回答。该智能体通过一个两阶段的LoRA微调流程进行训练，以掌握多步骤推理和工具使用能力。

**关键技术及创新点**：1. **教学理论驱动的结构化反馈生成**：将经典反馈理论具体化为可操作的LLM提示，确保反馈覆盖多个教学层次，兼具系统性和可解释性。2. **评判员引导的迭代优化机制**：引入与人类对齐的LLM作为评判员，实现基于明确准则的、组件级的自动化反馈评估与修订，提升了开源小模型生成反馈的质量。3. **工具增强的交互式问答**：通过微调使智能体具备自主调用多样化教学工具进行多步推理的能力，将静态反馈扩展为动态、情境化的对话，并能从工具调用错误中学习恢复。4. **本地化与开源模型部署**：整个系统基于小型开源LLM构建，强调本地可部署性，为实际教育场景中的规模化、隐私安全的应用提供了可行性。

### Q4: 论文做了哪些实验？

论文实验分为离线评估和真实课堂部署两部分。实验设置上，反馈生成和交互代理均基于开源模型（如Qwen3-8B/30B）构建，并与GPT-5等闭源模型对比。

数据集与基准测试包括：1）反馈生成使用离散数学证明任务数据集$\mathcal{D}_{fb}$（177个学生解答）；2）交互代理使用$\mathcal{D}_{int}^{train}$（约7000条交互轨迹）和测试集$\mathcal{D}_{int}^{test}$（192个问题）；3）真实部署收集了课堂研究数据集（$\mathcal{D}_{study}^{feedback}$、$\mathcal{D}_{study}^{int}$，39名学生）和考前自由使用数据集（$\mathcal{D}_{prep}^{feedback}$含362份报告、$\mathcal{D}_{prep}^{int}$含99次对话）。

对比方法涵盖：反馈生成中比较Qwen3-8B REFINE、Qwen3-30B-Thinking与GPT-5；交互代理对比Qwen3-8B（无推理）、Qwen3-8B Thinking、GPT-5与微调后的Qwen3-8B REFINE。

主要结果与关键指标：1）反馈质量通过法官引导再生显著提升，人类-法官一致性均值$\kappa=0.95$（各维度0.77-1.00）；2）交互代理在测试集上表现与GPT-5相当，人类对齐法官评估其在相关性、可操作性等维度得分高；3）工具使用效率高，生成最终响应所需推理步骤和工具调用次数少；4）课堂调查显示学生对反馈正确性、清晰度的感知评分高（5点李克特量表）；5）学生参与分析识别出15个主题（如任务理解、解决方案修复、反馈协商），标注者间一致性$\kappa=0.73$；6）反馈吸收分析中，反馈内容与任务表现的标注一致性适中（$\kappa=0.665$）。部署时模型推理速度达~20词元/秒（单A100 GPU），支持实时交互。

### Q5: 有什么可以进一步探索的点？

基于论文讨论与结论部分，该研究在交互式反馈系统的探索上取得了进展，但仍存在若干局限性和值得深入探索的方向。首先，研究仅在单一课程和机构中部署，其普适性有待验证；同时，研究侧重于交互行为的证据，未能直接测量学习成效的提升，未来需建立从交互痕迹到学习成果的因果链条。其次，为满足实时性约束，反馈迭代仅针对部分评分标准，可能低估了系统在未迭代维度上的性能，这提示未来可开发自适应、可调控的迭代策略，根据学生需求和教学意图动态选择优化维度。

可能的改进思路包括：将系统扩展至更多学科领域，整合更丰富的工具和内容资源，以验证其跨场景适用性；设计长期追踪实验，量化反馈互动对学生知识掌握与技能迁移的影响；进一步优化多智能体协作机制，例如引入个性化学生模型，使反馈生成更贴合个体学习状态与认知特点。此外，可探索轻量级单次反馈与深度交互模式的智能切换机制，以支持更自然、高效的学习过程。

### Q6: 总结一下论文的主要内容

该论文提出了REFINE系统，旨在解决大规模教育中个性化、互动式反馈的难题。核心贡献是设计了一个基于小型开源大语言模型、可本地部署的多智能体反馈框架，将反馈重构为动态交互过程而非静态单向输出。

问题定义聚焦于现有自动化反馈系统通常缺乏互动性，难以支持学生澄清与追问。方法上，REFINE整合了三个关键组件：基于教学规则的反馈生成智能体、利用人类对齐评判器引导的再生循环（LLM-as-a-judge），以及支持学生后续提问的具自反思能力的工具调用交互智能体。

主要结论显示，通过课堂实际部署与实验评估，评判器引导的再生显著提升了反馈质量；交互智能体能产生与顶尖闭源模型相当的高效回应；对学生互动行为的分析进一步揭示，系统反馈能有效引导学生后续提问的主题方向，证明了多智能体工具增强系统在实现可扩展互动反馈方面的可行性与有效性。
