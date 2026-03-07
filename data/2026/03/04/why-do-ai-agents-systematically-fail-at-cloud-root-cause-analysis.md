---
title: "Why Do AI Agents Systematically Fail at Cloud Root Cause Analysis?"
authors:
  - "Taeyoon Kim"
  - "Woohyeok Park"
  - "Hoyeong Yun"
  - "Kyungyong Lee"
date: "2026-02-10"
arxiv_id: "2602.09937"
arxiv_url: "https://arxiv.org/abs/2602.09937"
pdf_url: "https://arxiv.org/pdf/2602.09937v2"
categories:
  - "cs.AI"
  - "cs.DC"
tags:
  - "Multi-Agent Systems"
  - "Reasoning & Planning"
relevance_score: 8.0
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Reasoning & Planning"
  domain: "Enterprise & Workflow"
  research_type: "Empirical Study/Analysis"
attributes:
  base_model: "Gemini 2.5 Pro, GPT-5 mini, GPT-OSS 120B, Solar Pro 2, Claude Sonnet 4"
  key_technique: "Process-level failure analysis methodology and pitfall taxonomy"
  primary_benchmark: "OpenRCA"
---

# Why Do AI Agents Systematically Fail at Cloud Root Cause Analysis?

## 原始摘要

Failures in large-scale cloud systems incur substantial financial losses, making automated Root Cause Analysis (RCA) essential for operational stability. Recent efforts leverage Large Language Model (LLM) agents to automate this task, yet existing systems exhibit low detection accuracy even with capable models, and current evaluation frameworks assess only final answer correctness without revealing why the agent's reasoning failed. This paper presents a process level failure analysis of LLM-based RCA agents. We execute the full OpenRCA benchmark across five LLM models, producing 1,675 agent runs, and classify observed failures into 12 pitfall types across intra-agent reasoning, inter-agent communication, and agent-environment interaction. Our analysis reveals that the most prevalent pitfalls, notably hallucinated data interpretation and incomplete exploration, persist across all models regardless of capability tier, indicating that these failures originate from the shared agent architecture rather than from individual model limitations. Controlled mitigation experiments further show that prompt engineering alone cannot resolve the dominant pitfalls, whereas enriching the inter-agent communication protocol reduces communication-related failures by up to 15 percentage points. The pitfall taxonomy and diagnostic methodology developed in this work provide a foundation for designing more reliable autonomous agents for cloud RCA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体（Agent）在自动化云系统根因分析（RCA）任务中系统性失败的根本原因问题。研究背景是，大规模云系统故障会导致巨大经济损失，因此自动化RCA至关重要。尽管近期研究利用LLM智能体来自动化此任务，但现有系统即使采用能力强大的模型，其检测准确率仍然很低。现有评估框架通常只评估最终答案的正确性，而无法揭示智能体在推理、协作或与环境交互过程中具体为何失败，这使得开发者难以确定改进方向——究竟是该换用更强模型、优化提示词，还是重新设计智能体架构。

针对现有方法的不足，本文的核心问题是：**如何超越结果评估，从过程层面系统性诊断LLM智能体在云RCA任务中失败的根本原因，并识别出导致这些失败的共性架构缺陷。** 为此，论文通过大规模实验（在OpenRCA基准上运行5个LLM模型，产生1675次智能体运行），对失败过程进行细粒度分析，将观察到的故障归类为涵盖智能体内推理、智能体间通信以及智能体-环境交互三大维度的12种缺陷类型。研究发现，最普遍的缺陷（如幻觉数据解读和不完全探索）在所有模型中均持续存在，这表明失败根源在于共享的智能体架构设计，而非单个模型的能力限制。这一发现将问题从“模型不够强”转向了“架构有缺陷”，为设计更可靠的自主RCA智能体奠定了基础。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于LLM的云RCA方法、多智能体系统框架以及智能体评估方法。

在**基于LLM的云RCA方法**方面，已有研究利用大语言模型自动化根因分析任务，例如OpenRCA等基准测试和基线智能体框架。本文与这些工作的关系在于，它直接在这些现有基线（如OpenRCA基准）上进行实验和分析。区别在于，现有工作主要关注最终答案的正确性，而本文则深入剖析智能体在推理、协作和交互过程中的系统性失败原因。

在**多智能体系统框架**方面，相关研究致力于设计智能体架构以实现复杂任务。本文与这类工作的关联在于，它研究的对象正是此类多智能体系统在云RCA中的应用。本文的核心区别在于，它通过实证分析发现，当前智能体架构（如交互协议）的固有缺陷，而非单个模型的能力限制，是导致性能低下的主因。

在**智能体评估方法**方面，现有评估框架通常只评估最终输出。本文与此类工作的关系是，它承认并基于这种“仅结果评估”的现状。本文的贡献在于超越了这种评估方式，提出了一种过程级的失败分析方法和包含12种陷阱类型的分类法，从而能够系统性地诊断智能体在推理、通信和交互各环节的故障。

### Q3: 论文如何解决这个问题？

论文通过构建一个系统化的诊断框架来解决AI代理在云根因分析中系统性失败的问题。该框架的核心方法是对代理执行过程进行细粒度的失败分析，而非仅评估最终答案的正确性。其架构设计围绕三个关键接口展开：智能体内部推理、智能体间通信以及智能体与环境交互。

整体框架是一个分析流水线，用于处理在OpenRCA基准测试上运行的1675个代理任务。主要模块包括：1）一个基于LLM（Claude Opus 4.5）的分析代理，负责对代理运行日志进行初步探索和分类；2）一个人机协同验证环节，确保分类的准确性；3）一个包含12种具体陷阱类型的分类法，作为诊断标准。

关键技术在于将失败根源归类到上述三个架构层面。在智能体内部推理层面，识别出七种陷阱，如“幻觉性数据解读”（核心问题：编造叙事）和“不完整探索”（核心问题：范围收窄），这是最普遍的两类失败。在智能体间通信层面，识别出三种陷阱，如“指令-代码不匹配”（核心问题：实现差距），源于控制器与执行器之间的协作问题。在智能体-环境交互层面，则识别出资源耗尽等执行环境限制。

创新点主要体现在三个方面：首先，提出了首个针对RCA代理失败原因的系统性分类法，揭示了失败源于共享的代理架构设计，而非单一模型的能力限制。其次，开发了可扩展的诊断方法论，结合了自动化分析与人工验证，确保了分类的可靠性。最后，通过控制实验验证了缓解措施的有效性，发现仅靠提示工程无法解决主要陷阱，而增强智能体间通信协议能将相关失败降低多达15个百分点，为设计更可靠的自主代理提供了实证基础。

### Q4: 论文做了哪些实验？

论文在OpenRCA基准测试上进行了大规模实验，涉及五个LLM模型（Claude Sonnet 4、GPT-5 mini、Gemini 2.5 Pro、Solar Pro 2和GPT-OSS 120B），共执行了1,675次智能体运行。实验设置包括对智能体失败案例进行细粒度分类，将其归为12种陷阱类型，涵盖智能体内推理、智能体间通信和智能体-环境交互三个层面。

主要对比了不同模型在共享智能体架构下的失败模式分布，并进行了受控的缓解实验。关键数据指标显示，最普遍的陷阱是“解释性幻觉”（Hallucination in Interpretation），发生率达71.2%，以及“不完整探索”（Incomplete Exploration），发生率为63.9%。所有模型在这两类陷阱上的发生率均超过53%和66%，表明失败源于共享架构而非单个模型限制。在代码生成错误率上，模型间差异显著，Gemini 2.5 Pro最低（1.8%），Claude Sonnet 4最高（65.5%）。

缓解实验包括针对智能体内陷阱的提示工程（假设驱动和陷阱感知提示）以及针对智能体间通信的协议增强。结果发现，提示工程虽能扩大探索范围（如使之前被忽略的内存利用率KPI类别出现），但无法显著减少幻觉陷阱；而通过丰富通信协议（如让执行器返回生成的Python代码和完整执行输出），可将通信相关失败率降低高达15个百分点（例如GPT-5 mini和Claude Sonnet 4分别提升约14和15个百分点），并在银行领域任务中提高完美检测数量（如GPT-5 mini从0增至2）。此外，通过集成内存监视器消除了所有内存不足（OOM）故障。

### Q5: 有什么可以进一步探索的点？

该论文揭示了基于LLM的RCA智能体在云根因分析中的系统性缺陷，其局限性与未来研究方向可从以下方面深入探索。首先，实验仅针对Bank领域子集进行缓解措施验证，未来需扩展至更多样化的云故障场景，以检验缺陷分类和缓解策略的普适性。其次，当前诊断流程依赖半自动化分类和人工验证，限制了可扩展性，未来可开发全自动的持续监控管道，实时识别并归类智能体运行中的失败模式。此外，论文发现提示工程无法解决核心的“解释性幻觉”问题，这指向了智能体架构的根本性缺陷。未来可探索引入验证模块，通过交叉检查原始数据与智能体解读来减少幻觉，或设计结构化状态共享机制以改善智能体间协作。另一个方向是自适应任务分解，使智能体能动态调整探索深度，避免“不完整探索”。最后，智能体与环境的交互优化，如更精细的资源监控（如内存观察器），可进一步提升系统稳定性。这些改进不仅适用于云RCA，也为构建更可靠的自主智能体系统提供了通用设计原则。

### Q6: 总结一下论文的主要内容

该论文针对基于大语言模型（LLM）的智能体在云系统根因分析（RCA）任务中系统性失败的问题进行了深入研究。现有方法虽利用LLM智能体自动化RCA，但检测准确率低，且评估框架仅关注最终答案，无法揭示推理失败原因。

论文核心贡献在于首次从过程层面系统分析了LLM智能体在RCA中的失败模式。作者在完整OpenRCA基准上对五个LLM模型进行了1,675次智能体运行，将观察到的失败归类为12种陷阱类型，涵盖智能体内推理、智能体间通信以及智能体-环境交互三个层面。分析发现，最普遍的陷阱（如幻觉数据解读和不完整探索）在所有模型中均存在，与模型能力层级无关，表明失败根源在于共享的智能体架构缺陷，而非单个模型限制。

通过受控缓解实验，论文进一步证明仅靠提示工程无法解决主要陷阱，而增强智能体间通信协议可将通信相关失败降低多达15个百分点。这项工作提出的陷阱分类法和诊断方法，为设计更可靠的云RCA自主智能体奠定了基础。
