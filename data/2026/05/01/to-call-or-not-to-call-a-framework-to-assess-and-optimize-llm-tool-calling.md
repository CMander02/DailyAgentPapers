---
title: "To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling"
authors:
  - "Qinyuan Wu"
  - "Soumi Das"
  - "Mahsa Amani"
  - "Arijit Nag"
  - "Seungeon Lee"
  - "Krishna P. Gummadi"
  - "Abhilasha Ravichander"
  - "Muhammad Bilal Zafar"
date: "2026-05-01"
arxiv_id: "2605.00737"
arxiv_url: "https://arxiv.org/abs/2605.00737"
pdf_url: "https://arxiv.org/pdf/2605.00737v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "工具使用"
  - "决策优化"
  - "智能体架构"
  - "Web搜索"
relevance_score: 9.5
---

# To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling

## 原始摘要

Agentic AI architectures augment LLMs with external tools, unlocking strong capabilities. However, tool use is not always beneficial; some calls may be redundant or even harmful. Effective tool use, therefore, hinges on a core LLM decision: whether to call or not call a tool, when performing a task. This decision is particularly challenging for web search tools, where the benefits of external information depend on the model's internal knowledge and its ability to integrate potentially noisy tool responses. We introduce a principled framework inspired by decision-making theory to evaluate web search tool-use decisions along three key factors: necessity, utility, and affordability. Our analysis combines two complementary lenses: a normative perspective that infers true need and utility from an optimal allocation of tool calls, and a descriptive perspective that infers the model's self-perceived need and utility from their observed behaviors. We find that models' perceived need and utility of tool calls are often misaligned with their true need and utility. Building on this framework, we train lightweight estimators of need and utility based on models' hidden states. Our estimators enable simple controllers that can improve decision quality and lead to stronger task performance than the self-perceived set up across three tasks and six models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决LLM在智能体架构中调用外部工具（特别是网络搜索工具）时决策次优的问题。研究背景是，虽然调用工具能增强LLM能力，但并非总是有益——冗余调用浪费资源，甚至可能引入噪声、损害性能。现有方法仅通过聚合准确率粗粒度评估工具调用的整体效果，缺乏对调用决策细粒度质量的评估框架，例如何时真正需要、调用能否带来收益、成本是否合理。因此，核心问题是：如何系统性地评估和优化LLM自主决策“是否调用工具”的能力？论文提出一个基于决策理论的框架，从三个关键维度分析：**必要性**（模型是否真正缺乏内部知识需要外部帮助）、**效用**（调用工具能否提升性能）和**可负担性**（收益是否超过成本）。通过区分“真实”与“模型自感知”的必要性和效用，论文发现LLM的自我感知与实际情况存在严重错位，导致调用决策远未达到最优。最终目标是利用模型隐藏状态训练轻量级估计器，以校准调用决策，提升任务性能。

### Q2: 有哪些相关研究？

在工具增强大语言模型（LLMs）的相关研究中，主要可分为以下几类：

1. **工具增强与成本感知类**：早期工作如Toolformer和ART将工具使用集成到推理过程中，近期方法通过接地、执行反馈和强化学习优化自主工具使用。同时，成本感知规划（如预算约束扩展）研究工具调用的延迟与API开销。本文的不同之处在于，现有方法主要依据下游任务成功或全局成本-性能权衡来评估工具调用，而本文首次从单个工具调用层面诊断其是否必要、有益、冗余或有害，并引入了基于决策理论的必要性、效用和可负担性三维度评估框架。

2. **搜索与检索增强生成（RAG）类**：如Adaptive RAG系统通过不确定性估计（如语义熵、自评估置信度）来决定何时检索。然而，这些方法仅在调用前建模必要性，而效用仅在检索后评估。本文提出的框架通过结合规范性和描述性视角，能够**在工具调用之前**同时评估其预期效用，从而更精准地判断调用价值，并利用隐状态训练轻量级评估器来优化决策。

### Q3: 论文如何解决这个问题？

该论文提出了一种基于决策理论的框架来评估和优化LLM的工具调用决策，核心方法是将问题分解为三个视角：规范视角（定义最优决策）、描述视角（观察实际行为）和处方视角（优化决策）。整体框架首先通过三种策略（自动决策、不使用工具、强制使用工具）获取模型在不同条件下的表现分数，据此定义三个关键指标：真实需求（N*）、真实效用（U*）和真实可负担性（Δ*），作为规范视角的基准。

主要创新点在于利用模型隐藏状态训练轻量级估计器：潜在需求估计器（LNE）和潜在效用估计器（LUE）。LNE基于不使用工具时的隐藏状态预测是否需要调用工具，LUE则基于隐藏状态预测工具调用是否会产生正向收益。这些估计器采用简单的多层感知机（MLP）架构，将模型内部表征映射到规范标签上。

关键技术包括：通过比较不使用工具和强制使用工具的性能分数来确定规范标签，从模型自身提示和自动决策行为中提取感知标签，以及利用LUE的置信度分数在预算约束下对实例进行排序，选择最值得调用工具的前K个实例。最终，这种处方视角的控制器能够弥合描述决策与规范决策之间的差距，显著提升工具调用的决策质量。

### Q4: 论文做了哪些实验？

论文在三个数据集上进行了实验：Entity任务（实体描述生成）、InVivoQuery任务（事实性问答）和BFCL任务（伯克利函数调用排行榜）。实验使用六种开源模型，涵盖3B到120B参数，包括指令微调和推理变体，工具为Web搜索（通过FastMCP服务器调用Google Search API）。实验设置采用两阶段框架：模型先决定是否调用工具，再根据搜索结果生成回答。主要实验包括：(1) 规范性视角分析：通过比较不使用工具（notool）和使用工具（withtool）的性能，测量真实需求（True Need）和真实效用（True Utility），发现在真实需求区域（notool性能低）工具调用有51%带来收益，而在模型已表现良好时（notool性能高）工具调用有34%造成负效用；(2) 描述性视角分析：通过三种提示变体测量感知需求（Perceived Need），通过自动设置下的工具调用行为测量感知效用（Perceived Utility），发现模型感知与真实需求/效用之间存在系统性的不对齐；(3) 预算约束实验：在10000美元总预算下变化允许调用工具的比例K（1%-100%），比较理想和实际效用增益，结果显示所有模型在工具调用决策上均存在次优性，Gemma和GPT-OSS效率较高，Llama和Mistral则较低效。

### Q5: 有什么可以进一步探索的点？

论文提出的框架虽然系统性地评估了LLM工具调用的必要性、效用和可负担性，但仍存在若干可进一步探索的方向。首先，当前分析主要聚焦于网络搜索工具，未来可扩展到代码执行、数据库查询等其他工具类型，探索不同工具的特性如何影响决策框架的普适性。其次，轻量级估计器的训练依赖隐藏状态，但模型间的架构差异可能导致迁移性受限，可研究跨模型通用的表示学习或知识蒸馏方法。此外，框架的“最优分配”假设基于理想化场景，未充分考虑实时工具返回噪声的动态分布——未来可引入强化学习，让控制器在任务过程中自适应调整决策阈值。另一个值得深挖的点是工具调用的因果影响：当前仅观察相关性，但可设计反事实推理实验，量化某次调用是“必要”还是“冗余”。最后，框架中“可负担性”仅考虑计算成本，可纳入延迟、能耗等更实际的资源约束，并探索多工具协同时的联合优化策略，从而提升在复杂工作流中的实用性。

### Q6: 总结一下论文的主要内容

这篇论文提出一个评估和优化大语言模型工具调用决策的框架，主要针对网络搜索工具。问题定义：大语言模型何时应该调用外部工具，以及如何评估调用决策的质量。方法概述：基于理性选择理论，从必要性（模型是否需要外部帮助）、效用（调用工具是否提升性能）和可负担性（成本是否合理）三个维度评估工具调用决策。通过规范视角（基于真实需求与效用确定最优调用）和描述视角（分析模型自感知需求与效用）两种互补视角分析。核心发现：模型自感知的需求和效用与真实情况存在显著错位，导致次优调用决策。基于此，研究者训练轻量级估计器，利用模型隐藏状态预测真实需求与效用，从而改善决策质量。实验覆盖六个开源模型和三个问答任务，显示该框架能提升任务性能，但完全弥合差距需要更好的工具行为模型。
