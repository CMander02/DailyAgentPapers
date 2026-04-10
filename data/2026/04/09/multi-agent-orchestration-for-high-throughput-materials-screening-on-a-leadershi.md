---
title: "Multi-Agent Orchestration for High-Throughput Materials Screening on a Leadership-Class System"
authors:
  - "Thang Duc Pham"
  - "Harikrishna Tummalapalli"
  - "Fakhrul Hasan Bhuiyan"
  - "Álvaro Vázquez Mayagoitia"
  - "Christine Simpson"
  - "Riccardo Balin"
  - "Venkatram Vishwanath"
  - "Murat Keçeli"
date: "2026-04-09"
arxiv_id: "2604.07681"
arxiv_url: "https://arxiv.org/abs/2604.07681"
pdf_url: "https://arxiv.org/pdf/2604.07681v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent"
  - "Scientific Agent"
  - "HPC"
  - "Workflow Orchestration"
  - "Planning"
  - "Tool Use"
  - "Scalability"
  - "Materials Science"
relevance_score: 8.0
---

# Multi-Agent Orchestration for High-Throughput Materials Screening on a Leadership-Class System

## 原始摘要

The integration of Artificial Intelligence (AI) with High-Performance Computing (HPC) is transforming scientific workflows from human-directed pipelines into adaptive systems capable of autonomous decision-making. Large language models (LLMs) play a critical role in autonomous workflows; however, deploying LLM-based agents at scale remains a significant challenge. Single-agent architectures and sequential tool calls often become serialization bottlenecks when executing large-scale simulation campaigns, failing to utilize the massive parallelism of exascale resources. To address this, we present a scalable, hierarchical multi-agent framework for orchestrating high-throughput screening campaigns. Our planner-executor architecture employs a central planning agent to dynamically partition workloads and assign subtasks to a swarm of parallel executor agents. All executor agents interface with a shared Model Context Protocol (MCP) server that orchestrates tasks via the Parsl workflow engine. To demonstrate this framework, we employed the open-weight gpt-oss-120b model to orchestrate a high-throughput screening of the Computation-Ready Experimental (CoRE) Metal-Organic Framework (MOF) database for atmospheric water harvesting. The results demonstrate that the proposed agentic framework enables efficient and scalable execution on the Aurora supercomputer, with low orchestration overhead and high task completion rates. This work establishes a flexible paradigm for LLM-driven scientific automation on HPC systems, with broad applicability to materials discovery and beyond.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决将基于大语言模型（LLM）的智能体（Agent）工作流高效部署到现代高性能计算（HPC）系统，特别是百亿亿次（exascale）级别系统时所面临的规模化挑战。研究背景是人工智能与高性能计算的融合正推动科学工作流从静态、人工预设的管道向能够自主决策的自适应系统转变。LLM在其中扮演核心角色，能够理解复杂科学目标并动态调整执行策略。

然而，现有基于LLM的自主工作流方法存在明显不足。许多当前系统采用单智能体架构或顺序工具调用模式，在执行大规模模拟活动（如高通量材料筛选）时，这种迭代推理循环会引入严重的序列化瓶颈，导致任务执行效率低下，无法充分利用百亿亿次系统所提供的海量并行计算资源。这使得简单的LLM驱动工作流在性能上可能反而不如为并行执行而显式构建的传统工作流。

因此，本文要解决的核心问题是：如何设计一个可扩展的框架，以克服序列化瓶颈，使LLM智能体能够有效协调和利用HPC的大规模并行性，从而高效地执行计算密集型科学探索任务。为此，论文提出了一种可扩展的、分层的“规划者-执行者”多智能体编排框架。该框架通过分离高层推理与大规模任务执行，让中央规划智能体动态分解工作负载，并将子任务分配给一群并行的执行智能体异步处理，从而实现对百亿亿次资源的有效利用。论文以大气水收集领域的金属有机框架高通量筛选为案例，在Aurora超级计算机上验证了该框架的低编排开销和高任务完成率，为LLM驱动的HPC科学自动化建立了一个灵活范式。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：**基于LLM的自主智能体系统**、**科学工作流管理系统**以及**AI与HPC融合的框架**。

在**基于LLM的自主智能体系统**方面，ReAct框架提出了结合推理与工具执行的范式，并被ChemCrow、ChemGraph等系统采用，用于自动化科学任务。然而，这些系统主要针对交互式或小规模工作负载，其顺序工具调用模式在大规模HPC活动中会产生序列化瓶颈，无法充分利用百亿亿次级资源的并行能力。

在**科学工作流管理系统**方面，Parsl、FireWorks和Balsam等系统为HPC上的大规模科学工作流提供了可扩展的基础设施，能够管理资源、容错和数据依赖。但它们通常是静态的，工作流结构需要预先由人工定义，缺乏基于中间结果动态调整执行策略的语义推理能力。

在**AI与HPC融合的框架**方面，Colmena框架提出了“思考者”与“执行者”代理的分离，以交织AI推理与模拟任务，主要用于主动学习应用。此外，也有研究探索了将LangChain与Parsl结合，在超算上实现工具使用。

本文与这些工作的关系在于，它综合了LLM的推理能力、工作流管理系统的可扩展性以及多代理协调的思想。其区别与创新在于：提出了一种**分层的多智能体编排框架**，通过一个中央规划代理动态划分工作负载，并将子任务分配给大量并行执行代理，所有代理通过共享的MCP服务器与Parsl工作流引擎交互，从而实现了在领导级HPC系统上高效、可扩展的异步模拟任务调度，解决了现有LLM代理系统并发能力不足与传统工作流系统缺乏动态适应性的问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个可扩展的层次化多智能体编排框架来解决大规模模拟活动中LLM智能体部署的并行化瓶颈问题。其核心方法是采用“规划者-执行者”架构，将传统单智能体或顺序工具调用的串行模式转变为并行化、动态可扩展的工作流。

整体框架由四个主要模块组成：1）一个中央规划智能体，负责解析用户查询的科学目标，并将其动态分解为独立的模拟子任务；2）一个动态分配的执行者智能体池，每个执行者并行处理规划者分配的子任务，其数量可根据工作负载动态扩展；3）一个数据分析智能体，负责在模拟完成后聚合结果并生成最终响应；4）两个基于模型上下文协议（MCP）的服务器，作为智能体与外部工具和计算资源的统一接口。其中，化学MCP服务器暴露用于启动模拟的工具，数据工具MCP服务器提供数据聚合与材料排序功能。

关键技术包括：首先，利用MCP协议实现了智能体与工作流引擎（Parsl）及底层HPC资源的解耦与高效连接，所有工具均采用异步实现，允许多个执行者同时请求模拟而不会阻塞。其次，通过Parsl工作流引擎将每个模拟任务映射为可在计算节点上调度执行的应用程序，从而充分利用Aurora超级计算机的大规模并行计算资源。最后，采用动态扩展的执行者池设计，使智能体数量能够匹配工作负载，避免了资源闲置或过载。

创新点主要体现在三个方面：一是将多智能体协作范式引入科学计算工作流，通过层次化分工克服了单智能体的串行瓶颈；二是构建了基于MCP的通用工具接口层，使LLM智能体能够灵活、并发地调用高性能计算模拟工具；三是实现了从自然语言目标到大规模并行模拟任务的全自动化编排与执行，并在真实超算系统和大型材料数据库（CoRE MOF）上验证了其低编排开销和高任务完成率。

### Q4: 论文做了哪些实验？

论文实验围绕所提出的分层多智能体框架，在Aurora超级计算机上进行了高通量材料筛选的演示与性能评估。实验设置采用规划者-执行者架构：一个中央规划智能体解析自然语言查询，将科学目标分解为结构化任务，并通过共享的Model Context Protocol (MCP)服务器和Parsl工作流引擎，将子任务动态分配给并行执行智能体群；执行智能体调用模拟工具，随后数据分析智能体进行后处理与排名。

数据集/基准测试采用计算就绪实验金属有机框架数据库，针对大气水收集等应用进行筛选。对比方法涉及弱扩展和强扩展性能测试：弱扩展实验在1至256个节点上，每节点固定9个MOF结构，采用随机采样和嵌套采样两种策略；强扩展实验使用完整的5,591个MOF数据集，在8至256个节点上评估。

主要结果包括：1）框架成功自动化执行了数千个并行的巨正则蒙特卡洛模拟，例如对2,304个MOF进行水吸附筛选，识别出顶部20%的材料其水工作容量高达7.06 mol/kg。2）多目标筛选实验展示系统能根据自然语言指令动态生成工作流，并行评估水、CO₂和N₂吸附场景。3）扩展性能上，弱扩展的工作流持续时间在5,500至8,000秒之间保持稳定；强扩展在8至32节点接近线性加速，在256节点时强扩展效率为64.9%。关键数据指标：智能体开销（不含模拟）约60-90秒，总体任务成功率为84%（25次实验中出现4次失败）。

### Q5: 有什么可以进一步探索的点？

该论文展示了多智能体框架在材料高通量筛选上的成功应用，但其局限性和未来探索方向仍值得深入。首先，框架依赖的LLM（如gpt-oss-120b）在复杂科学推理中仍存在约16%的失败率，这提示需要进一步集成领域知识图谱或符号推理模块，以提升任务解析的准确性和可靠性。其次，当前架构虽实现了并行执行，但动态负载均衡和容错机制可能尚未充分优化，未来可探索基于实时性能预测的自适应任务分配策略，以更好地处理计算成本不均的任务。此外，框架与HPC系统的集成深度仍有拓展空间，例如直接嵌入资源感知调度器，使智能体能动态调整计算节点需求。从更广义看，该框架可扩展至跨领域科学工作流，如结合实验自动化机器人，实现“计算-实验”闭环。最后，开源模型虽具优势，但其科学专业能力仍需通过持续领域微调和人类反馈强化学习来提升，以完全满足自主科学发现的需求。

### Q6: 总结一下论文的主要内容

该论文提出了一种可扩展的分层多智能体框架，旨在解决大规模高性能计算（HPC）系统中基于大语言模型（LLM）的智能体部署难题。核心问题是传统单智能体架构或顺序工具调用在运行大规模模拟活动时，会成为串行化瓶颈，无法充分利用百亿亿次级（exascale）资源的巨大并行能力。

方法上，论文设计了一个规划者-执行者架构：一个中央规划智能体动态划分工作负载，并将子任务分配给一组并行执行智能体。所有执行智能体通过一个共享的模型上下文协议（MCP）服务器进行交互，该服务器利用Parsl工作流引擎来协调任务。这种设计实现了任务的高效并行分发与执行。

为验证框架，研究使用开源的gpt-oss-120b模型，在Aurora超级计算机上协调了对计算就绪实验金属有机框架（CoRE MOF）数据库的高通量筛选，以用于大气集水应用。主要结论表明，该智能体框架能以较低的管理开销和较高的任务完成率，在领导级HPC系统上实现高效、可扩展的执行。这项工作的核心贡献在于为HPC系统上的LLM驱动科学自动化建立了一个灵活范式，对材料发现等领域具有广泛适用性。
