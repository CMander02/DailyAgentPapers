---
title: "MM-WebAgent: A Hierarchical Multimodal Web Agent for Webpage Generation"
authors:
  - "Yan Li"
  - "Zezi Zeng"
  - "Yifan Yang"
  - "Yuqing Yang"
  - "Ning Liao"
  - "Weiwei Guo"
  - "Lili Qiu"
  - "Mingxi Cheng"
  - "Qi Dai"
  - "Zhendong Wang"
  - "Zhengyuan Yang"
  - "Xue Yang"
  - "Ji Li"
  - "Lijuan Wang"
  - "Chong Luo"
date: "2026-04-16"
arxiv_id: "2604.15309"
arxiv_url: "https://arxiv.org/abs/2604.15309"
pdf_url: "https://arxiv.org/pdf/2604.15309v1"
categories:
  - "cs.CV"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Multimodal Agent"
  - "Web Agent"
  - "Hierarchical Planning"
  - "Self-Reflection"
  - "AIGC Integration"
  - "Benchmark"
  - "UI/UX Generation"
relevance_score: 7.5
---

# MM-WebAgent: A Hierarchical Multimodal Web Agent for Webpage Generation

## 原始摘要

The rapid progress of Artificial Intelligence Generated Content (AIGC) tools enables images, videos, and visualizations to be created on demand for webpage design, offering a flexible and increasingly adopted paradigm for modern UI/UX. However, directly integrating such tools into automated webpage generation often leads to style inconsistency and poor global coherence, as elements are generated in isolation. We propose MM-WebAgent, a hierarchical agentic framework for multimodal webpage generation that coordinates AIGC-based element generation through hierarchical planning and iterative self-reflection. MM-WebAgent jointly optimizes global layout, local multimodal content, and their integration, producing coherent and visually consistent webpages. We further introduce a benchmark for multimodal webpage generation and a multi-level evaluation protocol for systematic assessment. Experiments demonstrate that MM-WebAgent outperforms code-generation and agent-based baselines, especially on multimodal element generation and integration. Code & Data: https://aka.ms/mm-webagent.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动化生成包含多模态元素（如图像、视频、图表）的网页时，由于元素孤立生成所导致的风格不一致和全局协调性差的问题。随着人工智能生成内容（AIGC）工具的快速发展，按需创建视觉素材已成为现代网页设计的灵活范式，但直接将此类工具集成到自动化网页生成流程中，往往会使各元素在风格、几何尺寸和语义上与整体布局脱节，从而破坏页面的视觉一致性与整体连贯性。

现有方法通常采用检索或占位符来填充多模态元素，随后独立生成或插入资源。这种处理方式存在明显不足：首先，不同元素之间容易出现风格不一致；其次，生成的媒体内容与预留的页面槽位在尺寸、比例上可能不匹配；最后，当各种资源组合成最终页面时，整体布局常常缺乏协调性与美感。

因此，本文的核心问题是：如何通过一个结构化的规划与优化过程，协调全局布局决策与局部资源生成，以生产出视觉一致、布局协调且多模态元素无缝集成的网页。为此，论文提出了MM-WebAgent这一分层智能体框架，它通过分层规划来协同基于AIGC的元素生成，并借助分层自反思机制进行迭代优化，从而实现对网页全局布局、局部多模态内容及其整合效果的联合优化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：**方法类**、**应用类**和**评测类**。

在**方法类**研究中，现有工作主要通过两种方式整合视觉信息：一是从网页截图解析视觉元素并重建为可执行代码（如UICopilot、ScreenCoder、DesignCoder），二是为网页生成引入外部检索的视觉素材。这些方法提升了布局保真度和代码正确性，但将多模态素材视为静态或外部提供，无法生成新颖、语义对齐且风格一致的内容。此外，代码智能体（如OpenHands、Bolt.diy、ReCode）通过规划、工具使用和环境交互来编排设计流程，WebGen-Agent则引入渲染页面的视觉反馈进行迭代优化。然而，这些方法的层次结构仍局限于推理或代码粒度。**本文的MM-WebAgent与之区别在于，将层次结构定义在“设计抽象”层面，实现了从以代码为中心的编排，转向以设计抽象驱动、并带有结构化跨模态优化的多模态生成。**

在**应用类**研究中，相关工作主要集中在网页UI领域，但缺乏对原生多模态内容创建质量的关注。

在**评测类**研究中，现有基准可分为三类：一是仅关注HTML/CSS正确性的纯代码基准；二是评估从截图重建网页的图像到代码基准，强调布局保真而非意图驱动的多模态生成；三是提供静态图像作为占位符的任务，忽略了生成内容的质量与一致性。**本文指出，现有基准均未能充分评估生成的原生素材与全局页面语义的对齐度，因此专门引入了新的基准和分层评估协议来系统性地填补这一空白。**

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MM-WebAgent的分层多模态智能体框架来解决网页生成中风格不一致和全局连贯性差的问题。其核心方法是模拟人类设计师的工作流程，将网页生成建模为一个包含分层规划、元素生成和迭代自反思的结构化过程。

整体框架包含四个关键步骤：任务规划、分层生成、多级评估和迭代反思。在规划阶段，系统首先构建一个全局布局计划，定义章节层次、空间组织和页面级样式属性，并嵌入多模态元素的占位符及其位置、大小等先验信息。随后，针对每个多模态元素制定局部元素计划，包含上下文信息（如所属章节、功能角色）和元属性（如视觉风格、色彩色调），并指定应调用的生成工具。

生成阶段，全局布局计划首先被转换为HTML/CSS结构，创建章节和多模态元素占位符。然后，各局部元素计划由指定的生成工具（如图像、视频或图表生成器）并行执行，生成相应资产并插入网页中。

关键的创新点在于其分层自反思机制，该机制在三个互补层级上迭代改进生成的网页：1) **局部细化**：评估并修正每个多模态元素的内在质量（如图像修复、图表标签修正）；2) **上下文细化**：分析HTML片段，调整元素与周围布局的集成问题（如错位、间距不一致），通过CSS补丁或块调整确保视觉一致性和空间连贯性；3) **全局细化**：评估整个网页的布局和样式一致性，对HTML和页面结构进行针对性编辑，以增强视觉平衡和结构连贯性。

此外，论文还引入了包含120个多样化网页的评估基准和多级评估协议，从全局（布局正确性、风格连贯性、美学质量）和局部（元素内在质量及集成度）两个层面进行系统评估，并通过基于惩罚和分级评分的策略将定性评估转化为定量分数。

### Q4: 论文做了哪些实验？

论文实验设置方面，MM-WebAgent 使用 GPT-5.1 作为分层规划器，并调用 GPT-Image-1、Sora-2 等 AIGC 工具生成图像、视频和图表。默认启用分层反思机制，由 GPT-5.1 作为评判者，最多进行 3 轮迭代。实验在作者提出的多模态网页生成基准上进行，并对比了三种范式：基于代码的一次性生成、基于代码的智能体生成以及多模态网页智能体生成。对比方法包括使用多种大语言模型（如 OpenAI GPT 系列、Qwen 系列、Gemini-2.5-Pro）实现的上述范式，其中基于代码的智能体基线通过 bolt.diy 或 Openhands 框架实现。

主要结果方面，MM-WebAgent 在六个评估维度上均取得最佳或接近最佳性能。关键数据指标显示，在全局指标（布局、风格、美观度）和局部指标（图像、视频、图表）上，MM-WebAgent（使用 GPT-5.1）平均得分达 0.75，显著优于其他范式。特别是在多模态元素生成与集成上优势明显，其图像、视频、图表得分分别为 0.88、0.75 和 0.54。相比之下，纯代码一次性生成的最佳平均分仅为 0.47，纯代码智能体范式最佳为 0.46。消融实验证实了分层规划和分层反思的必要性，移除它们会导致性能显著下降（例如，无分层规划时平均分降至 0.42）。此外，在 WebGen-Bench 上的实验也表明该方法具有竞争力，取得了 55.4% 的准确率和 3.9 的外观分数。成本分析显示，MM-WebAgent 平均每任务耗时 155.8 秒，虽货币成本较高，但时间成本与基线相当。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于对外部AIGC工具的依赖以及框架的静态性。未来研究可以从以下几个方向深入探索：首先，可以设计动态工具编排机制，使代理能根据任务需求实时选择和组合不同的生成工具，甚至集成新兴的多模态模型，以提升灵活性和鲁棒性。其次，当前训练无关的编排方式虽便于分析，但引入学习机制（如强化学习或模仿学习）来优化分层规划、反思和工具调用策略，有望在长期交互中提升性能与泛化能力。此外，评估基准可扩展至更复杂的交互式网页场景，并纳入更细粒度的美学与一致性指标。最后，探索跨领域、跨风格的适应性生成，以及减少对提示工程的依赖，开发更自主的决策模块，也是值得推进的方向。

### Q6: 总结一下论文的主要内容

论文针对现有AIGC工具直接用于自动化网页生成时，常导致风格不一致和全局协调性差的问题，提出了MM-WebAgent这一分层多模态网页智能体框架。其核心贡献在于通过分层规划和迭代自反思来协调基于AIGC的元素生成，从而联合优化全局布局、局部多模态内容及其整合，以生成连贯且视觉一致的网页。方法上，它包含规划阶段来组织全局布局和指定局部元素，以及分层反思阶段来迭代调整局部元素和全局布局。此外，论文还引入了一个用于多模态网页生成的基准测试和多层次评估协议。实验结果表明，该方法在生成多样且连贯的多模态网页方面，优于基于代码生成和基于智能体的基线方法，特别是在多模态元素生成与整合上表现突出。
