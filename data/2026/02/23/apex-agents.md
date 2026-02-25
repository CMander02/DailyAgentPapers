---
title: "APEX-Agents"
authors:
  - "Bertie Vidgen"
  - "Austin Mann"
  - "Abby Fennelly"
  - "John Wright Stanly"
  - "Lucas Rothman"
  - "Marco Burstein"
  - "Julien Benchek"
  - "David Ostrofsky"
  - "Anirudh Ravichandran"
  - "Debnil Sur"
  - "Neel Venugopal"
  - "Alannah Hsia"
  - "Isaac Robinson"
  - "Calix Huang"
  - "Olivia Varones"
  - "Daniyal Khan"
  - "Michael Haines"
  - "Austin Bridges"
  - "Jesse Boyle"
  - "Koby Twist"
date: "2026-01-20"
arxiv_id: "2601.14242"
arxiv_url: "https://arxiv.org/abs/2601.14242"
pdf_url: "https://arxiv.org/pdf/2601.14242v3"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent Benchmark"
  - "Agent Evaluation"
  - "Long-Horizon Tasks"
  - "Tool Use"
  - "Cross-Application"
  - "Agent Infrastructure"
relevance_score: 8.0
---

# APEX-Agents

## 原始摘要

We introduce the AI Productivity Index for Agents (APEX-Agents), a benchmark for assessing whether AI agents can execute long-horizon, cross-application tasks created by investment banking analysts, management consultants, and corporate lawyers. APEX-Agents requires agents to navigate realistic work environments with files and tools. We test eight agents for the leaderboard using Pass@1. Gemini 3 Flash (Thinking=High) achieves the highest score of 24.0%, followed by GPT-5.2 (Thinking=High), Claude Opus 4.5 (Thinking=High), and Gemini 3 Pro (Thinking=High). We open source the APEX-Agents benchmark (n=480) with all prompts, rubrics, gold outputs, files, and metadata. We also open source Archipelago, our infrastructure for agent execution and evaluation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI智能体评估领域存在的“模拟与现实差距”问题。研究背景是，随着企业开始大规模部署智能体系统，AI实验室也投入大量资源扩展智能体能力，人们期待AI智能体能够可靠地执行专业服务工作，从而深刻影响经济和社会。然而，现有的智能体评估方法存在明显不足：它们往往范围狭窄、高度人为设计、只包含简单任务，无法捕捉专业人士日常的真实工作方式，因此难以提供关于智能体在现实世界中如何帮助专业人士的有效信号。

基于此，本文的核心问题是：如何准确评估AI智能体执行高度复杂的专业服务工作的能力？为此，论文提出了APEX-Agents基准测试。该基准旨在填补现有评估的空白，通过创建由投资银行分析师、管理顾问和公司律师设计的、需要跨应用、长周期规划的真实任务，来评估智能体在模拟真实工作环境（包含文件和工具）中的表现，从而更可靠地衡量前沿AI在专业领域的实际应用潜力。

### Q2: 有哪些相关研究？

本文提出的APEX-Agents基准主要与以下几类相关研究有关：

**1. 智能体评测基准研究：**
本文属于AI智能体（Agent）能力评估领域的研究。相关工作包括评估智能体在特定领域（如编程、数学）或通用能力（如工具使用、多步推理）的基准测试，例如SWE-bench、AgentBench、ToolBench等。APEX-Agents与这些工作的主要区别在于其**任务来源和复杂性**：它并非基于现有公开数据集或合成任务，而是直接源于对227名投资银行分析师、管理顾问和律师等精英专业人士的实地调研，旨在评估智能体在**真实、长视野、跨应用**的专业工作流中的执行能力，模拟了包含文件和工具的真实工作环境。

**2. 面向专业领域的AI应用研究：**
在金融、法律、咨询等专业服务领域，已有大量研究探索AI的辅助应用，例如文档分析、预测模型、法律文本生成等。然而，这些研究通常聚焦于**单一、特定的子任务**。APEX-Agents的不同之处在于，它评估的是智能体**整合多种工具、处理多步骤、跨多个应用程序**来完成一个完整核心工作流程的能力，更贴近专业人士的实际复合型任务，而非孤立的原子任务。

**3. 智能体基础设施与评估框架研究：**
为运行和评估复杂智能体，需要相应的基础设施。本文开源了其执行与评估框架Archipelago，这与开源的智能体框架（如AutoGPT、LangChain相关项目）或评估平台（如MLCommons的评估方案）属于同类工作。APEX-Agents的贡献在于提供了一个**与特定高价值专业领域深度绑定的、包含完整提示、评分标准、黄金输出和元数据的标准化评测集**（共480个任务），为社区提供了可复现的评估基础。

综上，APEX-Agents在评测目标（基于真实专家工作的长程跨应用任务）、任务构建方法（源于大规模专业调研）和评估生态（配套开源基准与框架）上，与现有相关工作形成了区分和补充。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为APEX-Agents的综合性基准测试，并配套开发了名为Archipelago的执行与评估基础设施，来解决评估AI智能体在长视野、跨应用复杂任务中表现的问题。

其核心方法在于创建一个高度逼真、由领域专家构建的模拟工作环境（称为“世界”），并在此环境中设计具体任务。整体框架包含三个关键部分：**基准数据集构建**、**智能体执行环境**和**自动化评估系统**。

在**基准设计**方面，论文的创新点在于其数据集的构建方式。首先，来自投行、咨询和律所领域的专家（平均经验12.9年）基于真实项目经验，创建了33个包含完整背景、角色和约束的“项目场景”。每个场景构成一个“世界”，平均包含166个文件。专家们随后在这些模拟环境中扮演特定角色（如合伙人、分析师），通过使用日历、聊天、文档、电子表格、演示文稿等9大类共63个（部分世界多达250个）工具进行交互、研究和产出，从而自然衍生出480个长视野任务。这种“由内而外”的任务创建方式确保了任务的真实性、挑战性和多样性。每个任务都配有详细的评分标准（平均每个任务4.06条）和专家提供的“黄金输出”作为参考答案。

**执行与评估架构**是另一个关键。论文开源了Archipelago基础设施来运行智能体。智能体在受限环境中（关闭网络搜索）执行任务，最多允许250个步骤以避免陷入循环。评估环节采用了一个高度自动化的“法官模型”系统。该系统使用Gemini 3 Flash（思考模式设为低）作为核心评判模型，其创新之处在于评判依据不是智能体的完整行动轨迹，而是任务提示、智能体最终输出、由行动引发的变更日志以及具体的评分标准。此外，还使用一个辅助法官模型来根据“评分目标”识别需要评判的具体产出物（如控制台消息或编辑后的电子表格）。这种设计将评判重点放在最终结果是否符合专家定义的关键标准上，而非过程，提高了评估的客观性和可扩展性。经测试，该法官模型在人工标注的基准集上准确率达到98.5%。

最终，论文采用**Pass@1**（智能体单次运行通过所有标准的任务比例）作为排行榜核心指标，直接回答“随机运行一次任务并通过的概率”这一清晰问题。同时辅以Pass@8（八次尝试中至少成功一次）和Pass^8（八次尝试全部成功）等指标来全面衡量智能体的能力和一致性。通过这套从专家构建、模拟执行到自动化评估的完整闭环方案，论文为衡量AI智能体在复杂专业场景中的实际生产力提供了一个可靠、可复现的基准。

### Q4: 论文做了哪些实验？

该论文围绕APEX-Agents基准测试展开实验，旨在评估AI智能体执行跨应用、长周期复杂任务的能力。实验设置上，研究者构建了模拟真实工作环境的测试平台，要求智能体使用提供的文件和工具完成任务。评估采用Pass@1指标，即单次尝试的成功率。

数据集/基准测试方面，论文开源了APEX-Agents基准，包含480个任务，所有提示、评分标准、标准答案、相关文件和元数据均公开。这些任务由投行分析师、管理顾问和公司律师创建，具有高度真实性。

对比方法上，论文测试了八种不同的AI智能体模型，主要对比了Gemini 3 Flash、GPT-5.2、Claude Opus 4.5和Gemini 3 Pro等主流模型，并特别测试了它们在高强度思考（Thinking=High）模式下的表现。

主要结果与关键数据指标显示：Gemini 3 Flash (Thinking=High) 以24.0%的Pass@1得分位列榜首；GPT-5.2 (Thinking=High) 紧随其后；Claude Opus 4.5 (Thinking=High) 和 Gemini 3 Pro (Thinking=High) 也取得了较高分数。这些结果整体偏低，凸显了当前智能体处理此类复杂任务的挑战性。此外，论文还开源了用于智能体执行与评估的基础设施Archipelago。

### Q5: 有什么可以进一步探索的点？

该论文提出的APEX-Agents基准虽然具有开创性，但仍存在明显局限，为未来研究提供了多个探索方向。首先，基准任务主要基于投资银行、咨询和法律等特定专业领域，其普适性有待验证，未来可扩展至医疗、教育、工程等更多元化的真实工作场景。其次，评估主要依赖Pass@1和Pass@8等结果导向指标，缺乏对任务执行过程的细粒度分析（如决策逻辑、工具使用效率、错误恢复能力），未来可引入过程性评估框架。此外，当前智能体在长周期任务中表现出较高的不一致性（Pass@8到Pass^8分数显著下降），这提示需要研究提升智能体鲁棒性和稳定性的方法，例如通过强化学习优化任务规划、改进上下文管理机制，或设计更有效的反思与修正循环。最后，基准中的“世界”复杂度和工具交互深度仍较有限，未来可构建更动态、多模态（如加入语音、图像交互）的模拟环境，以更好地评估智能体在开放世界中的适应能力。

### Q6: 总结一下论文的主要内容

该论文提出了APEX-Agents基准，旨在评估AI智能体在真实工作场景中执行复杂、长周期、跨应用任务的能力。其核心问题是现有基准难以衡量智能体在模拟专业工作环境（涉及多文件与工具操作）下的实际生产力。为此，研究者构建了一个包含480个任务的测试集，任务由投行分析师、管理顾问和律师等专业人士设计，要求智能体在模拟的真实工作环境中导航并完成。

方法上，论文开源了完整的基准套件（包括提示、评分标准、标准答案、文件及元数据）以及名为Archipelago的智能体执行与评估基础设施。他们采用Pass@1指标对八个智能体进行了测试排名。

主要结论显示，当前顶尖模型在此类复杂任务上的表现仍有很大提升空间，表现最佳的Gemini 3 Flash（高思考模式）得分仅为24.0%。该工作的核心贡献在于创建了一个高质量、贴近实际的专业生产力评估基准，并提供了配套工具，为未来开发更强大、实用的AI智能体奠定了重要的评估基础。
