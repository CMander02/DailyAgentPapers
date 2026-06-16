---
title: "CODA-BENCH: Can Code Agents Handle Data-Intensive Tasks?"
authors:
  - "Yuxin Zhang"
  - "Ju Fan"
  - "Meihao Fan"
  - "Shaolei Zhang"
  - "Xiaoyong Du"
date: "2026-06-13"
arxiv_id: "2606.15300"
arxiv_url: "https://arxiv.org/abs/2606.15300"
pdf_url: "https://arxiv.org/pdf/2606.15300v1"
github_url: "https://github.com/ruc-datalab/CoDA-Bench"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Data-intensive Agent"
  - "Code Agent"
  - "Kaggle Sandbox"
  - "Autonomous Engineering"
relevance_score: 9.5
---

# CODA-BENCH: Can Code Agents Handle Data-Intensive Tasks?

## 原始摘要

Advanced agents are increasingly demonstrating the potential to operate as autonomous engineers, creating a growing demand for evaluation benchmarks that capture the complexity of real-world development. Such environments typically involve both complex code and large-scale data (i.e., file system). However, existing benchmarks usually evaluate code-centric or data-centric capabilities in isolation, leaving a clear gap with real development scenarios. In this paper, we bridge this gap by introducing CODA-BENCH, the first benchmark to jointly evaluate code and data intelligence in a data-intensive environment. We construct a data-intensive Linux sandbox based on the Kaggle ecosystem (containing hundreds of datasets), where agents must actively explore complex file hierarchies to identify relevant resources and generate code for data-driven analytical tasks. CODA-BENCH comprises 1,009 tasks spanning 31 communities, with each task environment containing an average of 980 files, simulating realistic data scale and noise. Evaluations of advanced agents reveal that even top-performing systems struggle to effectively integrate data discovery with code execution, achieving a success rate of only 61.1%. These results highlight a substantial gap in current agentic capabilities for data-intensive tasks and point to promising directions for future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有基准测试在评估AI智能体（Agent）能力时，未能同时衡量其“代码智能”与“数据智能”协同作用的问题。研究背景是：当前先进智能体正从对话助手向自主工程师演进（如Claude Code、Cursor等），但在真实开发场景中，智能体必须能处理包含大规模数据（如文件系统中成百上千个文件）的复杂环境，既需要编写正确代码，也需要在复杂数据层级中主动探索、定位并利用相关数据源。然而，现有基准测试存在明显不足：代码中心型基准（如软件工程维护）忽略了真实世界中海量、异构数据的挑战；数据中心型基准（如用代码处理给定数据）则依赖孤立的Python脚本，忽视了在shell环境中发现和访问大规模数据的必要性。这种孤立的评估范式导致基准性能与现实效用之间存在鸿沟。为弥合这一差距，本文提出了CODA-BENCH，首个在数据密集型环境中联合评估代码与数据智能的基准。其核心问题正是：当前最先进的代码智能体能否真正整合代码理解与数据发现能力，自主完成需要从数据探索到代码执行的全流程数据密集型任务？

### Q2: 有哪些相关研究？

根据论文内容，相关工作主要分为两类：

1. **代码中心基准（Code-centric Benchmarks）**：以SWE-bench及其变体为代表，评估LLM在真实软件工程场景中的代码生成和修复能力，另有一些交互式环境基准（如web、桌面和终端级交互）。这些基准假设任务所需数据已准备好，忽略了代理需先在复杂数据环境中自主发现信息的过程。

2. **数据中心基准（Data-centric Benchmarks）**：如DA-Code、DABstep、KramaBench、DataSciBench、DAComp、ScienceAgentBench和DiscoveryBench，评估代理在数据科学任务中的能力（数据整理、机器学习等）。但所有相关数据文件都已显式提供，且大多仅涉及简单操作（如代码生成），很少要求代理通过环境与大规模数据集交互。

本文与上述工作的区别在于：首次联合评估代码和数据智能，构建了基于Kaggle生态系统、包含数百数据集的Linux沙箱环境，其中代理必须主动探索复杂文件层次以发现资源，并生成代码完成数据分析。与现有方法相比，每个任务平均含980个文件，模拟了真实数据规模和噪声。实验显示顶尖代理在数据发现与代码执行整合上成功率仅61.1%，揭示了当前能力的显著差距。

### Q3: 论文如何解决这个问题？

CODA-BENCH提出了一个系统化的基准构建框架，核心是联合评估代码智能和数据智能。整体框架包括三个关键阶段：环境构建、任务构建和对抗进化。

在环境构建阶段，论文提出了基于图的**数据关系建模**。利用Kaggle生态系统中笔记本与数据集的共现模式，构建加权图，边权重表示两个数据集在同一笔记本中共同出现的频率。然后使用Leiden算法将图划分为**社区**，每个社区包含语义相关的数据集。对于目标任务，选择目标数据所在社区的全部数据（平均980个文件）作为评估环境，社区内其他数据作为**同分布干扰项**，迫使代理进行细粒度语义推理而非表面特征匹配。

在任务构建阶段，创新性地提出**基于解决方案的逆向构建**方法。从Kaggle笔记本中提取可验证的数值结果作为"锚点"，通过静态分析追踪锚点的数据来源和变换序列，逆向生成反映真实需求的问题，并由人工审核确保质量。

最关键的是**对抗进化框架**，将任务难度优化建模为生成器与判别器之间的二人博弈。生成器最大化任务难度，判别器（由多个LLM组成的集成）尝试求解。通过迭代迭代，当解率过高时生成器增加难度，过低时诊断并修复任务缺陷，最终产生既有挑战性又可求解的高质量任务。该框架保证了基准的有效性和可扩展性。

### Q4: 论文做了哪些实验？

论文在CODA-BENCH上对多种前沿代码智能体进行了全面实验评估。实验环境基于Kaggle生态构建的数据密集型Linux沙箱，包含1009个任务、31个社区，每个任务环境平均包含980个文件。评估采用两个核心指标：数据发现准确率（DA）和执行准确率（EA）。对比方法分为两类：原生CLI工具（Claude Code搭配多个模型，Codex CLI搭配GPT-5.5）和框架型智能体（OpenHands搭配GPT-5.5、Claude-Opus-4.7、Kimi-K2.6、DeepSeek-V4-Pro，以及Mini-SWE-Agent搭配GPT-5.5）。主要结果如下：在完整基准上，Mini-SWE-Agent（GPT-5.5）以61.1%的EA最高，OpenHands（GPT-5.5）以59.7%次之；但最佳DA仅83.0%，表明在大型非结构化数据中发现文件仍是挑战。在更难的CODA-BENCH-hards上，所有模型性能显著下降，Mini-SWE-Agent的EA降至49.6%，Claude Code（Opus-4.6）的DA达68.4%但EA仅45.4%。成本方面，Claude Code（Sonnet-4.6）性价比最优，EA为53.8%，每任务仅0.11美元。此外，实验分析了环境特征影响：信噪比与准确率显著正相关（ρ=0.466, p<0.01），数据量则显著负相关（ρ=-0.461, p<0.01），表明语义干扰和I/O瓶颈是主要挑战。

### Q5: 有什么可以进一步探索的点？

从论文分析来看，CODA-BENCH揭示了当前agent在数据密集型任务中的瓶颈，但仍有几个值得探索的方向。首先，数据发现环节的失败主要源于语义歧义，未来可探索**知识增强的检索策略**，例如结合任务描述与文件内容的语义嵌入，或使用分层探索来优先筛选高潜力文件，而非依赖当前的线性遍历。其次，尽管提供oracle数据后代码生成环节仍有29%的失败率，这暗示**多源异构模式融合**是核心挑战，可以研究基于schema对齐的自动化预处理流水线，或引入领域知识图谱进行语义消歧。此外，当前agent在低信噪比环境下表现差，可能缺乏**主动降噪策略**（如基于统计特征的异常检测），未来可设计自适应代码生成框架，在生成前先通过数据质量评估过滤无关文件。最后，大文件体积导致的性能瓶颈提示需要优化**分块读取与流式处理**能力，避免一次性加载过量数据。这些方向有望弥合当前agent与真实开发场景之间的鸿沟。

### Q6: 总结一下论文的主要内容

CODA-BENCH提出了一个联合评估代码智能与数据智能的新基准，旨在弥合现有基准与现实开发场景之间的差距。问题定义：当前基准要么孤立评估代码编程能力，要么评估数据给定情况下的处理能力，无法反映真实开发中需同时处理大规模数据和复杂代码的挑战。方法概述：基于Kaggle生态系统构建数据密集型Linux沙箱环境，包含1,009个跨31个社区的任务，每个环境平均包含980个文件，模拟真实数据规模和噪声；利用数据共现图构建语义一致的环境，并通过对抗性验证确保任务质量。主要结论：顶尖代码代理（如Codex CLI、Claude Code）在该基准上的执行准确率仅达61.1%（困难子集为49.6%），表明当前系统在数据发现与代码执行的整合能力上存在显著不足。该工作为评估未来自主代码代理在真实数据密集型场景中的表现提供了关键测试平台，并揭示了重要的研究方向。
