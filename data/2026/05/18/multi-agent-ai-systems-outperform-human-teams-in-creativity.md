---
title: "Multi-agent AI systems outperform human teams in creativity"
authors:
  - "Tiancheng Hu"
  - "Yixuan Jiang"
  - "Haotian Li"
  - "José Hernández-Orallo"
  - "Xing Xie"
  - "Nigel Collier"
  - "David Stillwell"
  - "Luning Sun"
date: "2026-05-18"
arxiv_id: "2605.17885"
arxiv_url: "https://arxiv.org/abs/2605.17885"
pdf_url: "https://arxiv.org/pdf/2605.17885v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "LLM创造力"
  - "语义空间分析"
  - "对话动力学"
  - "创造性任务"
relevance_score: 8.5
---

# Multi-agent AI systems outperform human teams in creativity

## 原始摘要

Although artificial intelligence (AI) now matches or exceeds human performance across numerous cognitive tasks, creativity remains a highly contested frontier. As AI systems based on large language models (LLMs) are increasingly adopted in research and innovation, it is essential to understand and augment their creativity. Here we demonstrate that multi-agent LLM teams not only surpass single agents, but also substantially outperform human teams in creativity (Cohen's d=1.50) across 4,541 multi-agent LLM ideas and 341 human-team ideas on six diverse problem-solving tasks. This advantage is driven by novelty while maintaining comparable usefulness. To investigate the generative processes in both groups, we represent conversations as paths through semantic space using neural language model representations. Both LLM and human teams produce more creative ideas when conversations range widely rather than staying centered on a single theme (low global coherence). However, the additional patterns that predict creativity differ: LLM teams benefit from efficient exploration (high semantic spread, shorter paths), while human teams benefit from maintaining smooth conversational flow (high local coherence, frequent pivots). Additionally, we identify model choice and discussion structure as orthogonal design levers that together explain 26.8% of variance in LLM conversational dynamics, paving the way for systematic approaches to developing multi-agent systems with augmented creative capabilities.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探索多智能体AI系统在创造力任务中的表现是否优于人类团队，并揭示其背后的生成机制。研究背景是，尽管AI已在诸多封闭式认知任务上超越人类，但创造力长期被视为人类智能的“最后堡垒”，特别是围绕生成兼具新颖性与实用性的想法这一核心。现有方法的不足在于：一方面，单一大语言模型（LLM）的创造力有限，缺乏协同反思与迭代机制；另一方面，虽然多智能体系统在游戏等复杂任务中展现了超越单一智能体的潜力，但创造性任务中的横向对比（AI vs. 人类团队）仍是空白，且对于AI团队创意过程中语义探索模式的理解尚不充分。因此，本文要解决的核心问题是：多智能体LLM团队能否在创意生成上系统性地超越人类团队？其优势源自何处（新颖性还是实用性）？以及，两种团队产生高创造力想法时，其会话过程的语义空间探索路径有何不同？通过分析4541个AI想法与341个人类团队想法，作者发现AI团队在创造力上显著胜出（Cohen's d=1.50），且这种优势主要由新颖性驱动，同时实用性相当。进一步的轨迹分析揭示了关键差异：AI团队受益于高效的语义空间探索（高语义分散性、短路径），而人类团队则依赖于流畅的对话衔接（高局部连贯性、频繁转折）。这些发现为设计具备增强创造力的多智能体系统提供了可操作的杠杆。

### Q2: 有哪些相关研究？

相关研究主要分为三类：**方法类**、**现象分析类**和**评测类**。

方法类研究探索提升LLM创造力的途径，如单Agent提示工程（如温度参数调整、思维链）和多Agent协作框架。本文区别于这些工作，首次系统地比较了**多Agent系统**与**人类团队**的创造力差异，并发现了LLM与人类团队创造过程的深层区别。

现象分析类研究关注创造力内涵，通常区分新颖性和有用性。本文与之类似，但进一步揭示了LLM的创造力优势主要来源于**新颖性**的提升，且有用性持平，并开创性地使用语义空间轨迹分析对话动态。

评测类研究主要通过标准化任务（如替代用途测试）评估AI创造力。本文采用了六类多样化任务进行大规模对比（4541个AI想法 vs 341个人类团队想法），这在规模和广度上超越了此前的工作。此外，本文还识别出**模型选择**与**讨论结构**是影响LLM对话动态的独立设计杠杆，为系统性优化多Agent创造力提供了新视角。

### Q3: 论文如何解决这个问题？

该论文通过构建多智能体AI系统来解决创造力提升问题，核心方法是对比多智能体LLM团队与人类团队在创造性任务上的表现。整体框架包括实验任务设计、AI系统构建和语义空间分析三个层面。

在AI系统架构方面，论文构建了基于多种LLM模型的多智能体系统，使用GPT-4.1、o3-high、o3-low以及混合模型（DeepSeek-R1、Gemini-2.5-Pro、o3-default的组合）。系统设计了三个关键模块：团队规模模块（3或6个智能体）、角色分配模块（无角色、相同创造性角色、不同创造性角色）和讨论结构模块（开放型、指令型、迭代型、渐进型）。创新点在于系统性地操纵了模型类型和讨论结构这两个正交设计杠杆，它们共同解释了26.8%的对话动态方差。

关键技术包括：首先，通过神经语言模型表示将对话映射为语义空间中的路径，然后分析全局连贯性和局部连贯性等指标。论文发现，相比人类团队，LLM团队产生更创造性想法的机制不同：LLM团队受益于高效探索（高语义扩散、短路径），而人类团队受益于平滑对话流（高局部连贯性、频繁转向）。最终，多智能体LLM系统在4,541个AI想法与341个人类想法对比中，展现出显著优势（Cohen's d=1.50），这种优势主要由新颖性驱动，同时保持了可比的实用性。

### Q4: 论文做了哪些实验？

论文通过六个跨领域的创造性问题解决任务（包括塑料废物、教育不平等、供应链、员工离职等社会与商业问题，以及假想场景），对比了多智能体LLM团队（4541个创意）与人类团队（341个创意）的创造力。实验使用五名人类评分者盲评创意的新颖性和有用性，并以两者的乘积作为整体创造力指标。主要结果：多智能体LLM团队整体创造力显著优于人类团队（Cohen's d=1.50），其均值0.297（95% CI [0.295, 0.300]）远高于人类的0.151（95% CI [0.141, 0.160]）。这一优势主要由新颖性驱动（d=1.29），而有用性两者相当（d=0.08, p=0.14）。LLM团队在创意分布上整体右移，95百分位阈值（0.47）比人类（0.31）高53%，最佳创意（0.77）也比人类最佳（0.48）高58%。在团队讨论结构方面，GPT-4.1受益于迭代细化（M=0.308 vs. 无讨论0.212），而o3-high对各结构不敏感（M=0.322-0.345）。团队规模（3 vs. 6人）对创造力无显著提升。语义轨迹分析发现，两者创造力均与低全局连贯性相关（广泛探索），但LLM团队受益于高效探索（高语义传播、短路径），人类团队则受益于流畅对话（高局部连贯性、频繁转向）。模型类型和讨论结构共同解释了26.8%的轨迹特征方差。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向可从以下方面展开。首先，实验仅聚焦于文本创造力，未涉及视觉设计、音乐创作等多模态领域，后续可将语义轨迹框架拓展至图像或音频嵌入空间，探索创造性探索的跨模态共性。其次，人类与AI的协作模式未被纳入考量，未来可设计人机混合团队，研究实时协调、知识互补及动态任务分配如何影响创造力，并验证本文轨迹特征（如全局连贯性、最大语义距离）在协作场景中的预测能力。第三，模型层面存在天花板效应：推理模型（如o3）对结构干预的响应较弱，需探索新型对话机制（如异步反思、外部知识注入）以突破其内部推理的局限。此外，当前实验仅考虑固定团队规模与任务类型，可变团队动态（如自适应角色切换）或更具挑战性的开放性任务（如理论构建）可能揭示更多设计杠杆的交互效应。最后，研究指出可解释性局限：虽能通过轨迹几何量化探索-利用平衡，但LLM内部表征机制仍为黑箱。未来可结合注意力可视化或概念归因技术，直接追踪创意生成过程中的关键语义转化节点。

### Q6: 总结一下论文的主要内容

这项研究首次大规模比较了多智能体LLM团队与人类团队在创造性问题解决中的表现。在6个多样化任务中，分析了4541个LLM想法和341个人类想法，发现LLM团队不仅超越单个智能体，还显著优于人类团队（Cohen's d=1.50），主要优势体现在新颖性而非实用性上。通过神经语言模型将对话表示为语义空间路径，研究发现两组在创造性生成过程中存在差异：LLM团队受益于高效探索（高语义扩展、短路径），而人类团队依赖流畅的对话转换（高局部连贯性、频繁转向）。此外，模型选择和讨论结构是正交的设计杠杆，共同解释了26.8%的对话动态方差。该工作为理解多智能体系统创造力提供了量化框架，并指明了通过设计干预增强AI创造性的系统途径。
