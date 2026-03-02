---
title: "Radiologist Copilot: An Agentic Framework Orchestrating Specialized Tools for Reliable Radiology Reporting"
authors:
  - "Yongrui Yu"
  - "Zhongzhen Huang"
  - "Linjie Mu"
  - "Shaoting Zhang"
  - "Xiaofan Zhang"
date: "2025-12-02"
arxiv_id: "2512.02814"
arxiv_url: "https://arxiv.org/abs/2512.02814"
pdf_url: "https://arxiv.org/pdf/2512.02814v2"
categories:
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Tool Use"
  - "Planning"
  - "Multi-stage Workflow"
  - "Medical AI"
  - "Vision-Language Model"
relevance_score: 9.0
---

# Radiologist Copilot: An Agentic Framework Orchestrating Specialized Tools for Reliable Radiology Reporting

## 原始摘要

In clinical practice, radiology reporting is an essential yet complex, time-intensive, and error-prone task, particularly for 3D medical images. Existing automated approaches based on medical vision-language models primarily focus on isolated report generation. However, real-world radiology reporting extends far beyond report writing, which requires meticulous image observation and interpretation, appropriate template selection, and rigorous quality control to ensure adherence to clinical standards. This multi-stage, planning-intensive workflow fundamentally exceeds the capabilities of single-pass models. To bridge this gap, we propose Radiologist Copilot, an agentic system that autonomously orchestrates specialized tools to complete the entire radiology reporting workflow rather than isolated report writing. Radiologist Copilot enables region image localization and region analysis planning to support detailed visual reasoning, adopts strategic template selection for standardized report writing, and incorporates dedicated report quality control via quality assessment and feedback-driven iterative refinement. By integrating localization, interpretation, template selection, report composition, and quality control, Radiologist Copilot delivers a comprehensive and clinically aligned radiology reporting workflow. Experimental results demonstrate that it significantly outperforms state-of-the-art methods, supporting radiologists throughout the entire radiology reporting process. The code will be released upon acceptance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决临床实践中放射学报告生成这一复杂、耗时且易出错的问题，尤其是针对三维医学影像。研究背景在于，放射学报告不仅是简单的文本生成，而是一个包含图像定位、详细分析、模板选择和质量控制的多阶段规划密集型工作流。现有方法，如基于医学视觉-语言模型的自动化工具（例如CT2Rep），主要聚焦于孤立的报告生成环节，忽略了实际临床工作流中必需的图像观察、结构化解读、标准化模板适配以及报告质量审核等关键步骤。这种单次生成模型的局限性在于无法模拟放射科医生完整的决策链条，导致生成的报告可能缺乏临床准确性、完整性和可追溯性。

因此，本文的核心问题是：如何构建一个能够自主协调多步骤、覆盖放射学报告全流程的自动化系统，以弥补当前方法在临床对齐性和工作流完整性方面的不足。为此，作者提出了Radiologist Copilot，这是一个基于智能体（agentic）的框架，利用大语言模型作为推理核心，协同调用专用工具，实现从图像区域定位、分析规划、模板选择、报告撰写到质量控制的完整工作流。该系统不仅生成报告文本，还提供关键图像切片参考，使报告具备可追溯的影像证据，从而提升报告的可靠性和临床实用性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**自动化报告生成方法**、**医学视觉语言模型**以及**医学AI智能体**。

在**自动化报告生成方法**方面，CT2Rep和Reg2RG等工作专注于从3D医学图像（如胸部CT）生成报告，但它们通常只处理报告撰写这一孤立环节，缺乏对完整临床工作流（如模板选择和质量控制）的考虑。本文提出的Radiologist Copilot则旨在编排多个工具来完成包含图像定位、分析规划、模板选择、报告撰写和质量控制的全流程。

在**医学视觉语言模型**领域，RadFM、M3D-LaMed、Merlin、CT-CHAT、Med3DVLM和Hulu-Med等模型在统一处理2D/3D医学数据和多模态理解方面取得了进展，为报告生成提供了基础能力。然而，这些模型多为单次前向的生成模型，难以执行需要多步骤规划和工具协调的复杂临床任务。

在**医学AI智能体**方面，MMedAgent、MedRAX和CT-Agent等工作展示了利用工具进行自主推理以完成特定医疗任务（如胸片报告生成或CT视觉问答）的潜力。但它们通常依赖单一工具或缺乏工具间的深度协作。本文的Radiologist Copilot与这些工作的核心区别在于，它设计了一个能够**协调多种专用工具**的智能体框架，通过区域定位、分析规划、策略性模板选择和迭代式质量评估等工具的协同，实现了对完整、标准化放射学报告工作流的可靠支持。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为“放射科医生助手”的智能体框架来解决传统单一模型无法覆盖的、多阶段、规划密集的完整放射学报告工作流问题。其核心方法是利用大型语言模型作为推理中枢，通过自主的多步骤规划和执行，协调调用一系列专门化工具，模拟放射科医生的完整工作流程。

整体框架基于智能体架构，主要包括行动规划器、行动执行器和记忆模块。规划器负责制定高层解决方案并选择下一步要使用的工具；执行器则生成并执行具体命令；记忆模块记录所有行动和结果，用于验证任务完成情况。系统根据环境状态、观察和历史轨迹进行动态决策。

关键技术体现在其精心设计的专用工具库中，包含几个主要创新模块：
1.  **区域分析规划**：首先使用预训练分割模型定位感兴趣区域，提取器官和病灶掩膜。关键创新在于提出了“区域分析规划”，它能识别区域特定的分析项（如解剖结构和临床特征），并自适应地决定是否需要分析病灶特征，从而引导3D医学视觉-语言模型进行细致、针对性的图像解读。
2.  **策略性模板选择**：为了解决标准化报告书写中常被忽视的模板选择问题，该方法基于当前分析结果，从历史报告聚类得到的候选模板中，由LLM选择最相关的模板作为参考。报告生成不仅依据分析结果，还能融入质量控制的反馈意见进行迭代修订，生成的报告包含发现、印象和关键切片参考三部分。
3.  **报告质量控制**：这是一个关键创新点，通过一个专门的质量控制器工具实现。它利用LLM对生成报告进行全面的质量评估，涵盖格式、内容、语言和表达四个方面。如果评估未通过，则生成具体的反馈意见，驱动报告进行自适应的迭代精炼，直至达到合格标准。

总之，该方案的核心创新在于将定位、解读、模板选择、报告撰写和质量控制等多个关键阶段整合到一个由智能体协调的统一框架中，超越了单一的报告生成，实现了与临床实践对齐的、完整可靠的自动化放射学报告工作流。

### Q4: 论文做了哪些实验？

论文在肝脏放射学报告任务上进行了全面的实验验证。实验设置方面，系统基于OctoTools智能体框架实现，采用Qwen3-32B作为大语言模型进行推理，利用TotalSegmentator进行图像分割，并集成3D医学视觉语言模型Hulu-Med进行CT分析，最大执行步数设置为10。数据集采用公开的3D CT数据集AMOS-MM，从中筛选出包含肝脏描述的报告，最终使用1149个CT扫描作为训练集，367个作为验证集。

实验包括三个主要部分：智能体层面评估、任务层面评估和消融研究。对比方法涵盖了当前先进的3D医学视觉语言模型，包括RadFM、M3D、Merlin、CT-CHAT、Med3DVLM和Hulu-Med。主要结果如下：在任务层面评估中，Radiologist Copilot在自然语言生成和临床效能指标上均显著优于所有基线模型。关键数据指标包括：BLEU-1达到0.4025，ROUGE-L为0.3222，METEOR为0.4560，BERTScore为0.7024，F1-RadGraph为0.2585，GREEN为0.4379，全面超越最佳基线模型Hulu-Med（其对应指标分别为0.1867, 0.1723, 0.2380, 0.5947, 0.1209, 0.2163）。智能体层面评估采用LLM-as-a-Judge（GPT-5.2），在问题分析、行动规划、行动执行和整体工作流四个维度上，得分主要集中在4（良好）和5（优秀），证明了其工作流程的有效性和可靠性。消融研究证实了区域分析规划和战略模板选择两个核心组件对报告质量至关重要，移除任一组件都会导致多数指标显著下降；报告质量控制组件虽对最终指标影响相对较小，但对确保报告符合临床标准提供了重要保障。此外，实验还表明，即使集成不同的底层VLM（如RadFM或CT-CHAT），该智能体框架仍能保持稳健的性能提升。

### Q5: 有什么可以进一步探索的点？

该论文提出的“放射科医生副驾驶”系统在整合多工具、实现自动化工作流方面取得了显著进展，但其局限性和未来探索方向仍值得深入。首先，系统目前主要针对CT肝脏报告，虽可扩展至胸腹部，但跨模态（如MRI、超声）和跨病种的泛化能力尚未验证，未来需研究更通用的医学视觉-语言模型以适应多样化的临床场景。其次，系统依赖大型语言模型（LLM）作为推理核心，可能存在“幻觉”或事实性错误风险，尤其在医学严谨性要求下；未来可探索结合医学知识图谱或检索增强生成（RAG）技术，提升报告的准确性和可解释性。此外，工作流中的质量控制模块虽能迭代优化，但缺乏实时人工干预机制，在关键病例中可能受限；可引入人机协同框架，允许放射科医生在关键节点提供反馈，形成动态学习循环。最后，系统的计算效率与临床实时性需求之间的平衡需进一步优化，例如通过轻量化模型或边缘部署来降低延迟。总体而言，未来研究应聚焦于泛化性、安全性、人机交互及工程落地，以推动此类智能体从实验性工具向可靠临床助手的转变。

### Q6: 总结一下论文的主要内容

该论文提出了Radiologist Copilot，一个面向放射学报告全流程的智能体系统。针对现有方法仅孤立生成报告、无法覆盖临床实践中复杂的多阶段工作流（包括图像观察、解读、模板选择和质量控制）的问题，该框架通过智能体自主编排专用工具来应对。其核心方法整合了区域图像定位与区域分析规划以支持细粒度视觉推理，采用策略性模板选择实现标准化报告撰写，并通过质量评估与反馈驱动的迭代优化进行严格质量控制。实验表明，该系统在CT肝脏等放射学报告生成任务上显著优于现有先进方法，能够可靠地支持放射科医生完成从图像分析到报告定稿的完整流程，提升了临床工作效率与报告质量。
