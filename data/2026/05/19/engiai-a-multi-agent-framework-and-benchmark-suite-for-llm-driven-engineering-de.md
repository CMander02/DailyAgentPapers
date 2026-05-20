---
title: "EngiAI: A Multi-Agent Framework and Benchmark Suite for LLM-Driven Engineering Design"
authors:
  - "Gioele Molinari"
  - "Florian Felten"
  - "Soheyl Massoudi"
  - "Mark Fuge"
date: "2026-05-19"
arxiv_id: "2605.19743"
arxiv_url: "https://arxiv.org/abs/2605.19743"
pdf_url: "https://arxiv.org/pdf/2605.19743v1"
categories:
  - "cs.AI"
  - "cs.LG"
  - "cs.MA"
tags:
  - "Multi-Agent System"
  - "Engineering Design"
  - "Benchmark Suite"
  - "Retrieval-Augmented Generation"
  - "Workflow Orchestration"
  - "High Performance Computing"
  - "Supervisor Architecture"
  - "LLM Agent Evaluation"
  - "Tool Use"
  - "Conditional Reasoning"
relevance_score: 9.5
---

# EngiAI: A Multi-Agent Framework and Benchmark Suite for LLM-Driven Engineering Design

## 原始摘要

Large Language Model (LLM) agents are increasingly applied to engineering design tasks, yet existing evaluation frameworks do not adequately address multi-agent systems that combine simulation, retrieval, and manufacturing preparation. We introduce a benchmark suite with three evaluation dimensions: (1) a workflow benchmark with seven prompt styles targeting distinct cognitive demands-including direct tool use, semantic disambiguation, conditional branching, and working-memory tasks; (2) a Retrieval-Augmented Generation (RAG) benchmark with gated scoring isolating retrieval contributions to parameter selection; and (3) an High Performance Computing (HPC) benchmark evaluating end-to-end ML training orchestration on a SLURM cluster. Alongside the benchmark we present EngiAI, a Multi-Agent System (MAS) reference implementation built on LangGraph that operationalizes the benchmark by coordinating seven specialized agents through a supervisor architecture, unifying topology optimization, document retrieval, HPC job orchestration, and 3D printer control. Across four LLM backends and two EngiBench problems, proprietary models achieve 96-97% average task completion on Beams2D, while open-source 4B-parameter models reach 55-78%, with clear generational improvement. Conditional branching proves most challenging, with task completion dropping to 20-53% for the conditional style on Photonics2D. RAG gating confirms near-perfect retrieval-augmented scores ($\approx 1.0$) versus near-zero without retrieval, validating the evaluation design. On HPC orchestration, one model completes all pipeline steps in 100% of runs while another drops to 50%, revealing that multi-step instruction following degrades over long-running workflows.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）代理在工程设计中应用时面临的评估框架缺失与多智能体系统协同能力不足的问题。研究背景指出，工程设计涉及概念布局、仿真驱动优化和制造准备等复杂环节，依赖专业软件和迭代过程。现有方法通常采用机器学习模型（如逆设计和代理模型）生成设计方案，但这些模型常作为“黑箱”存在，缺乏灵活性，难以被非ML专家交互或解释。同时，尽管LLM代理（如ChatGPT）能通过自然语言界面简化用户操作，但现有评估体系（如单一任务基准）并未充分涵盖结合仿真、检索和制造准备的多智能体系统。本文核心问题是：如何设计一个覆盖工作流执行、检索增强生成（RAG）参数选择以及高性能计算（HPC）训练编排三个维度的基准套件，以系统评估LLM驱动工程设计中的认知需求（如条件分支、语义消歧）、跨模型鲁棒性以及多步指令遵循的可靠性？为此，论文提出了EngiAI框架作为参考实现，通过监督架构协调七个专用代理，以验证不同LLM后端在工程设计任务中的表现差异。

### Q2: 有哪些相关研究？

本文的相关研究可分为工程AI系统和评测基准两类。在工程AI系统方面，DSG-MAS、MechAgents、FEAGPT、DUCTILE等系统聚焦于拓扑优化和有限元分析等仿真能力，但缺乏制造导出和RAG支持；LLM3DPrint关注3D打印控制，但未整合仿真和RAG；AMGPT仅支持RAG，不具备多智能体编排和仿真能力；Wang等人虽结合仿真与多智能体，但缺乏HPC和制造导出。相比之下，EngiAI是首个同时整合多智能体编排、RAG、物理仿真、制造导出（STL）和HPC编排的统一框架。在评测基准方面，EngiBench/EngiOpt提供标准工程问题API但只评估单任务；FDM-Bench评估LLM在3D打印任务上的表现；AgentBench、τ-bench等通用基准侧重单智能体推理。这些评测均未涉及结合仿真、检索和HPC的多智能体协同工作流。EngiAI的基准套件专门设计了工作流提示风格（如条件分支、工作记忆）、RAG门控评分和SLURM集群端到端训练编排三个维度，能暴露现有基准无法捕获的故障模式。

### Q3: 论文如何解决这个问题？

EngiAI通过一种分层监督式多智能体架构来解决工程设计中的LLM应用问题。其核心是 Supervisor 智能体，它接收用户请求，进行意图分类，然后路由到七个专业智能体之一。每个专业智能体都作为自包含的 LangGraph 状态机运行，拥有自己的专用工具集，这避免了LLM在大量工具中陷入选择困境。例如，若用户需要论文参数，Supervisor 会先路由到 RAG 智能体进行检索，再路由到工程智能体执行优化。

整个架构分为四层：用户接口、编排层（Supervisor）、专业层（七个智能体）和执行层（外部服务/工具）。七个智能体覆盖了设计到制造的全生命周期：工程智能体（核心，驱动拓扑优化、ML逆设计及STL导出）、信息检索智能体（RAG、ArXiv、Web搜索）和基础设施智能体（HPC作业管理、CLI命令执行、Prusa 3D打印控制）。创新点在于其评估基准设计，通过七种提示风格（如W-Derived测试运算推导、W-Cond测试条件分支、W-Multi测试工作记忆）系统性地评估LLM在数值保真度、语义消歧和有状态推理三个认知维度上的能力，并通过门控评分（RAG基准）和分层加权评分（工作流基准）精确隔离各模块贡献。此外，HPC基准测试了端到端ML训练编排能力，揭示了长指令链的退化问题。

### Q4: 论文做了哪些实验？

论文围绕 EngiAI 框架进行了三个维度的实验：工作流基准、RAG 基准和 HPC 基准。实验设置使用四个LLM后端（GPT-5-mini、Gemini-3-Flash、Qwen3-4B、Qwen3.5-4B）在 EngiBench 的两个问题（Beams2D、Photonics2D）上评估。工作流基准包含七种提示风格，测量任务完成率（TC）和综合得分（CO）。主要结果：在Beams2D上，GPT-5-mini平均TC为0.96，Gemini-3-Flash为0.97，Qwen3-4B为0.55，Qwen3.5-4B为0.78。条件分支（W-Cond）最具挑战性，Photonics2D上TC降至20-53%。RAG基准采用门控评分，RAG开启时得分接近1.0，无RAG时接近0。HPC基准评估端到端ML训练编排，一个模型100%完成所有流水线步骤，另一个模型仅50%，表明多步骤指令遵循在长工作流中会退化。对比方法主要关注不同LLM后端间的性能差异。

### Q5: 有什么可以进一步探索的点？

该论文提出的框架在工程设计的AI自动化方面取得了显著进展，但仍存在几个可深入探索的方向。首先，条件分支任务完成率仅20-53%揭示了当前LLM在处理复杂逻辑判断时的根本弱点，未来可研究将形式化验证或符号推理模块集成到多智能体系统中，例如通过约束求解器预处理条件分支。其次，HPC编排性能退化表明长链工作流中的注意力衰减问题，可以探索分层任务分解与记忆压缩机制，类似于人类专家将长流程拆解为可管理的子任务。此外，当前基准仅覆盖拓扑优化等有限场景，未来应扩展至更广泛的工程设计领域如电路设计、控制算法开发，并引入多模态数据（如CAD图纸解析）。最后，RAG门控得分接近1.0但实际工程参数选择仍需领域专家验证，建议加入不确定性量化机制，使系统能主动请求人工确认低置信度参数推荐。

### Q6: 总结一下论文的主要内容

本论文介绍了一个名为EngiAI的多智能体系统及其配套基准套件，用于评估LLM驱动的工程设计流程。问题定义：当前缺乏针对多智能体系统在工程设计中的综合评估框架。方法概述：提出了包含三个维度的基准套件——工作流基准（七种提示风格测试不同认知需求）、RAG基准（门控评分隔离检索对参数选择的贡献）、HPC基准（评估SLURM集群上的端到端ML训练编排）。同时，开发了基于LangGraph的参考实现EngiAI，通过监督架构协调七个专业智能体，统一拓扑优化、文档检索、HPC作业编排和3D打印机控制。主要结论：在Beams2D任务上，专有模型达到96-97%的平均任务完成率，而4B参数开源模型仅达55-78%；条件分支是最具挑战性的认知需求，Photonics2D上任务完成率降至20-53%；RAG门控有效隔离了检索贡献，验证了评估设计的有效性；HPC编排显示多步骤指令跟随能力在长流程中退化。该项工作的核心意义在于填补了现有基准无法评估多智能体系统在工程设计综合流程的空白，为LLM驱动的工程设计提供了标准化评估框架和可复现的参考实现。
