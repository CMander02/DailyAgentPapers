---
title: "AgentTrace: Causal Graph Tracing for Root Cause Analysis in Deployed Multi-Agent Systems"
authors:
  - "Zhaohui Geoffrey Wang"
date: "2026-03-16"
arxiv_id: "2603.14688"
arxiv_url: "https://arxiv.org/abs/2603.14688"
pdf_url: "https://arxiv.org/pdf/2603.14688v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.SE"
tags:
  - "多智能体系统"
  - "故障诊断"
  - "根因分析"
  - "因果图"
  - "可解释性"
  - "系统可靠性"
  - "部署后分析"
relevance_score: 8.0
---

# AgentTrace: Causal Graph Tracing for Root Cause Analysis in Deployed Multi-Agent Systems

## 原始摘要

As multi-agent AI systems are increasingly deployed in real-world settings - from automated customer support to DevOps remediation - failures become harder to diagnose due to cascading effects, hidden dependencies, and long execution traces. We present AgentTrace, a lightweight causal tracing framework for post-hoc failure diagnosis in deployed multi-agent workflows. AgentTrace reconstructs causal graphs from execution logs, traces backward from error manifestations, and ranks candidate root causes using interpretable structural and positional signals - without requiring LLM inference at debugging time. Across a diverse benchmark of multi-agent failure scenarios designed to reflect common deployment patterns, AgentTrace localizes root causes with high accuracy and sub-second latency, significantly outperforming both heuristic and LLM-based baselines. Our results suggest that causal tracing provides a practical foundation for improving the reliability and trustworthiness of agentic systems in the wild.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决已部署多智能体系统中故障诊断困难的问题。随着基于大语言模型的多智能体系统在自动化客服、DevOps修复等实际场景中的广泛应用，系统故障因其级联效应、隐藏依赖和冗长执行轨迹而变得难以诊断。传统调试方法通常孤立地检查单个组件，无法捕捉导致系统级故障的跨智能体因果依赖关系，使得人工调试既缓慢又不可靠。

现有方法主要依赖启发式规则或基于大语言模型的推理进行故障定位，前者难以处理复杂的因果链，后者则需在调试时进行昂贵的LLM推理，延迟高且成本大。这些方法在应对由早期规划错误经多步执行传播而引发的下游故障时效果有限。

本文的核心问题是：如何在不依赖调试时LLM推理的情况下，快速、准确地定位已部署多智能体工作流中的根本原因。为此，论文提出了AgentTrace框架，通过从执行日志重建因果图、从错误表现点向后追踪，并利用可解释的结构和位置特征对候选根因进行排序，从而实现高效的事后故障诊断。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为四类：多智能体系统、AI系统调试、分布式追踪和根因分析。

在多智能体系统方面，AutoGen、MetaGPT等框架推动了智能体协作的发展，但通常缺乏系统化的调试支持，主要依赖人工检查日志。本文的AgentTrace旨在为此类系统提供自动化的故障诊断工具。

在AI系统调试领域，先前研究集中于神经网络内部或单智能体推理链的可解释性。基于LLM的自我调试方法需要昂贵的推理调用，且难以处理跨智能体问题。AgentTrace则无需在调试时调用LLM，通过分析执行日志构建因果图，实现了轻量级、低延迟的分析。

分布式追踪方面，Jaeger、Zipkin等工具为微服务架构提供了成熟的追踪方案。本文借鉴了其核心思想，但将其应用于多智能体LLM系统，关键区别在于智能体间的“消息”承载了语义内容，而不仅仅是请求元数据。

在根因分析领域，传统方法多采用统计或图算法。近期研究探索了使用LLM智能体进行云系统根因分析，但这些方法并非针对多智能体工作流的结构特点设计。AgentTrace则专门针对多智能体工作流的因果依赖和错误传播模式，利用可解释的结构与位置信号进行候选根因排序，从而更精准地定位问题源头。

### Q3: 论文如何解决这个问题？

论文通过构建一个轻量级的因果图追踪框架来解决多智能体系统故障根因定位的难题。其核心方法是从执行日志中重构因果图，并基于可解释的结构与位置特征对候选根因进行排序，整个过程无需在调试时调用大语言模型（LLM）进行推理。

整体框架分为三个主要阶段：因果图构建、反向追踪和候选节点排序。首先，系统将执行轨迹建模为一个有向无环图 \(G = (V, E)\)，其中节点 \(V\) 代表智能体的各种动作（如工具调用、消息传递、决策），边 \(E\) 代表动作间的因果依赖关系。边通过分析日志自动识别，分为三类：**顺序边**（同一智能体内连续动作）、**通信边**（不同智能体间的消息发送与接收）以及**数据依赖边**（通过变量引用追踪识别的生产与消费关系）。

给定错误显现节点 \(v_{error}\)，框架执行**广度优先反向追踪**算法，从该节点出发，沿因果边反向遍历其祖先节点，收集在指定深度限制内的所有候选节点，形成候选集 \(C\)。

最关键的一步是**候选节点排序**。AgentTrace 采用一个加权线性组合模型对候选节点进行评分：\(\text{score}(v) = \sum_{i \in \{p, s, c, f, e\}} w_i \cdot F_i(v)\)。其中，权重 \(w_i\) 通过网格搜索在验证集上确定，\(F_i(v)\) 是各组特征的归一化均值。特征分为五组：
1.  **位置特征**（权重 0.70）：包括节点在轨迹中的归一化位置、到错误节点的跳数距离、在追踪中的深度，旨在捕捉“早期决策点”。
2.  **结构特征**（权重 0.20）：基于图拓扑，包括节点的出度、中介中心性、以及可到达节点的比例（扇出比），用于识别图中影响广泛的关键节点。
3.  **内容特征**（权重 0.05）：分析节点内容的语义线索，如是否包含“错误”、“失败”等关键词，或“可能”、“不确定”等不确定性标记，以及内容长度异常。
4.  **流转特征**（权重 0.03）：关注智能体交互模式，如节点是否涉及跨智能体通信，以及执行智能体角色的关键性。
5.  **置信度特征**（权重 0.02）：利用模型报告的显式置信度分数或隐含的不确定性语言（如含糊其辞）。

该方法的创新点在于：1) **完全基于日志的轻量级分析**，无需昂贵的运行时LLM调用，实现了亚秒级延迟；2) **融合了因果图结构与语义内容**的多维度特征排序模型，特别是赋予位置和结构特征极高权重，这与根因通常是早期关键决策点的直觉相符；3) 设计了**可解释的特征体系**，使排序结果具有可追溯性，提升了诊断过程的可靠性与可信度。

### Q4: 论文做了哪些实验？

论文在550个多智能体故障场景的基准测试上进行了实验，旨在评估AgentTrace在根因定位上的准确性和效率。实验设置包括从执行日志中重建因果图，并利用结构和位置等可解释特征对候选根因进行排序，无需在调试时调用大语言模型（LLM）进行推理。

使用的数据集是一个精心设计的多样化基准，涵盖了反映常见部署模式的故障场景，包括技术（软件、DevOps）、业务（交易、金融）、服务（客户、医疗）、知识（研究、法律、教育）和规划等多个领域组，共计550个场景。

对比方法包括：随机选择节点（Random）、始终选择第一个节点（First Node）、选择错误前紧邻的节点（Last Node）以及使用GPT-4并结合完整执行轨迹和提示工程的LLM分析方法（LLM Analysis）。

主要结果如下：AgentTrace在根因定位准确率上显著优于所有基线方法。具体关键指标为：Hit@1达到94.9%，Hit@3达到98.4%，平均倒数排名（MRR）为0.97。而LLM分析的对应指标分别为68.5%、81.4%和0.74。统计检验（McNemar's test）证实了AgentTrace的显著优势（p < 0.001），与LLM分析相比的效应量（Cohen's h）为0.77，表明存在巨大的实际差异。消融研究显示，单独使用位置特征（Position only）的Hit@1为87.3%，证明了错误位置模式的高度预测性。此外，AgentTrace的平均处理时间仅为0.12秒，相比基于LLM分析的8.3秒，实现了69倍的加速，支持交互式调试工作流。在不同领域组上，性能表现一致，技术领域和知识领域略优。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在：1）当前评估集中于单一根因的合成场景，而实际多智能体系统故障常涉及多个相互作用的复杂因果结构；2）假设执行日志准确完整，但实际生产环境中可能存在日志缺失或噪声问题。这些局限为未来研究提供了明确方向。

未来可探索的方向包括：首先，开发能够处理多根因并发故障的因果推理模型，结合概率图模型或因果发现算法来识别复杂依赖关系。其次，研究在部分可观测或噪声日志下的鲁棒性方法，例如通过日志补全技术或不确定性建模来提升诊断可靠性。此外，可探索实时而非事后分析框架，将因果追踪集成到运行时监控中，实现故障预警。最后，结合领域知识（如特定工作流的约束规则）增强解释性，使根因分析不仅能定位问题，还能提供修复建议，从而形成从诊断到自愈的闭环系统。

### Q6: 总结一下论文的主要内容

该论文提出了AgentTrace框架，用于在多智能体系统发生故障时进行根因分析。核心问题是：在真实部署的多智能体工作流中，由于级联效应、隐藏依赖和长执行轨迹，故障诊断变得异常困难。方法上，AgentTrace通过执行日志重建因果图，从错误表现向后追踪，并利用可解释的结构和位置特征对候选根因进行排序，无需在调试时调用大语言模型进行推理。主要结论显示，在涵盖常见部署模式的多智能体故障场景基准测试中，AgentTrace能以亚秒级延迟高精度定位根因，显著优于启发式和基于大语言模型的基线方法。其意义在于为实际部署的智能体系统提供了一个轻量、实用且可解释的诊断工具，有助于提升系统的可靠性和可信度。
