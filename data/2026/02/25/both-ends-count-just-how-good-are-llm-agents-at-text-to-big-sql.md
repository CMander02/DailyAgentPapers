---
title: "Both Ends Count! Just How Good are LLM Agents at \"Text-to-Big SQL\"?"
authors:
  - "Germán T. Eizaguirre"
  - "Lars Tissen"
  - "Marc Sánchez-Artigas"
date: "2026-02-25"
arxiv_id: "2602.21480"
arxiv_url: "https://arxiv.org/abs/2602.21480"
pdf_url: "https://arxiv.org/pdf/2602.21480v1"
categories:
  - "cs.DB"
  - "cs.CL"
  - "cs.IR"
tags:
  - "Agent评测/基准"
  - "工具使用"
  - "LLM应用于Agent场景"
  - "Text-to-SQL"
  - "数据库Agent"
  - "执行效率"
  - "成本分析"
relevance_score: 7.5
---

# Both Ends Count! Just How Good are LLM Agents at "Text-to-Big SQL"?

## 原始摘要

Text-to-SQL and Big Data are both extensively benchmarked fields, yet there is limited research that evaluates them jointly. In the real world, Text-to-SQL systems are often embedded with Big Data workflows, such as large-scale data processing or interactive data analytics. We refer to this as "Text-to-Big SQL". However, existing text-to-SQL benchmarks remain narrowly scoped and overlook the cost and performance implications that arise at scale. For instance, translation errors that are minor on small datasets lead to substantial cost and latency overheads as data scales, a relevant issue completely ignored by text-to-SQL metrics.
  In this paper, we overcome this overlooked challenge by introducing novel and representative metrics for evaluating Text-to-Big SQL. Our study focuses on production-level LLM agents, a database-agnostic system adaptable to diverse user needs. Via an extensive evaluation of frontier models, we show that text-to-SQL metrics are insufficient for Big Data. In contrast, our proposed text-to-Big SQL metrics accurately reflect execution efficiency, cost, and the impact of data scale. Furthermore, we provide LLM-specific insights, including fine-grained, cross-model comparisons of latency and cost.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决传统文本到SQL（Text-to-SQL）评估方法在面向大数据（Big Data）实际应用场景时的严重不足。研究背景是，随着大语言模型（LLM）和智能体（Agent）技术的发展，Text-to-SQL系统在跨领域泛化能力上取得显著进步，并越来越多地被集成到大规模数据处理和交互式分析等大数据工作流中，形成了所谓的“文本到大数据SQL”（Text-to-Big SQL）场景。

现有方法的主要不足在于，传统的Text-to-SQL基准测试（如使用简单的二元正确性指标）范围狭窄，仅关注小规模关系数据库上的查询翻译准确性。它们完全忽略了当数据规模急剧扩大时，SQL生成与执行两端所引发的关键性能与成本问题。例如，一个在小数据集上无关紧要的翻译错误（如多投影了一个不必要的列），在大数据引擎上执行可能导致巨大的计算资源浪费、数据扫描量和财务成本。此外，现有评估也忽视了基于LLM的智能体在生成SQL过程中的推理延迟、工具编排开销，以及这些开销与后续查询执行时间之间的相互影响。

因此，本文要解决的核心问题是：如何对应用于大数据环境的Text-to-SQL智能体进行有效评估。具体而言，论文致力于填补现有研究的空白，提出一套新颖的、具有代表性的评估框架和指标，以联合衡量从自然语言到最终在大数据引擎上执行的全链路性能。这包括同时考量智能体行动、推理延迟、生成查询的部分正确性，以及在大数据系统上执行的实际效率与成本，从而更真实地反映“文本到大数据SQL”系统的综合表现。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：文本到SQL方法、大数据系统评估以及智能体架构。

在**文本到SQL方法**方面，已有大量研究利用LLM提升自然语言到SQL查询的翻译能力，并关注跨领域泛化性能。传统评估基准（如Spider）多聚焦于翻译准确率等孤立指标，但本文指出这些工作在评估时往往忽略了查询在大数据环境下的实际执行成本与性能影响。

在**大数据系统评估**领域，现有研究通常独立评估大数据引擎（如Amazon Athena）的查询执行效率与成本，或进行TPC-H等基准测试。然而，这些工作很少将前端的文本到SQL生成过程与后端的大数据执行结合起来进行端到端的综合考量。

在**智能体架构**方面，ReAct等框架被广泛用于构建任务导向的LLM智能体，通过工具调用与迭代推理来增强文本到SQL系统的适应性。但现有研究缺乏对这种智能体在文本到SQL场景中，其推理开销、工具编排延迟与最终大数据查询执行效率之间相互影响的深入评估。

本文与上述工作的核心区别在于，它首次系统性地将“文本到SQL”生成端与“大数据”执行端联合评估，提出了全新的“文本到大数据SQL”评估框架与指标。这些指标不仅考虑查询的部分正确性，还综合衡量了智能体行动、推理延迟以及查询在大数据引擎上执行的成本效益，从而揭示了传统文本到SQL评估在大数据场景下的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一套新的评估指标和设计一个适配的AI智能体系统来解决“Text-to-Big SQL”的评估挑战。其核心在于认识到传统Text-to-SQL指标（如精确匹配、执行准确率）在面向大数据场景时存在严重不足，因为它们只关注“全有或全无”的正确性，而忽略了在大规模数据下，即使是部分正确的查询（如包含多余列）也会导致显著的执行成本、延迟和资源开销。

**核心方法与创新指标**：
论文的核心方法是引入了一系列新颖的、具有代表性的评估指标，以全面衡量Text-to-Big SQL系统的表现。这些指标创新性地将**执行效率、成本和数据规模的影响**纳入考量。
1.  **VES***：这是对标准有效效率分数（VES）的扩展。它引入了**列级精度** \( P(S, \hat{S}) \) 来惩罚生成查询中包含的多余列（情况C），因为这些列虽然不影响结果有效性，但会浪费处理资源。同时，它使用**端到端时间** \( T_{e2e} \)（涵盖LLM交互、工具执行和查询运行总时间）与黄金查询执行时间 \( T_{gold} \) 的比率来评估效率。最终，VES* 是结果有效性指示函数、列精度和相对执行效率三者的乘积平均值。
2.  **VCES**：在VES*的基础上，进一步引入了**端到端执行成本** \( C_{e2e} \)，形成了面向成本的评估指标，特别适用于云部署场景。
3.  **CVQ**：**每次有效查询的预期成本**。该指标基于几何分布，量化了在“重试直至成功”策略下获得一个有效结果所需的平均预期成本，直接关联了单次尝试的有效率 \( p \) 和单次尝试成本 \( C_{e2e} \)。

**智能体架构与设计**：
为了在新的指标下进行评估，论文采用了一个基于**ReAct（推理+行动）框架**的AI智能体。
*   **整体框架**：系统由**控制器**（负责推理的LLM）和**执行器**（管理执行循环的程序）组成。控制器遵循ReAct的“思考-行动-观察”循环来完成任务。
*   **主要模块/工具**：控制器通过四个预定义的工具与下游的**Spark SQL**查询引擎（代表大数据处理系统）交互：
    1.  `list_tables`: 列出可用表。
    2.  `get_schema`: 获取表结构，并可选择获取样本行。
    3.  `check_query`: 使用一个LLM检查器验证查询语法。
    4.  `run_query`: 在Spark会话中执行SQL查询。
*   **关键设计决策**：
    *   **工具使用**：所有工具规格以零样本方式注入LLM上下文。
    *   **执行控制**：为防止在大数据环境中因无限循环纠正查询而导致资源耗尽或成本激增，智能体在**第一次执行`run_query`后立即终止**，这是一个关键的安全与成本控制设计。
    *   **实现基础**：基于LangChain Spark SQL Toolkit构建，并移植到LangGraph上，以利用其成熟的研究基线地位。

**总结**：论文的解决方案是双管齐下的：一方面，从**评估体系**上创新，提出了VES*、VCES、CVQ等一系列紧密结合大数据执行特征（效率、成本、部分正确性）的量化指标；另一方面，从**系统设计**上，采用了一个精简但功能完备的ReAct智能体，并针对大数据场景做了关键优化（如单次执行终止），从而为客观、全面地评估LLM智能体在“Text-to-Big SQL”任务上的真实能力提供了方法论和实验框架。

### Q4: 论文做了哪些实验？

论文实验主要分为三部分，旨在评估LLM智能体在“文本到大数据SQL”场景下的表现，并证明传统文本到SQL指标的不足。

**实验设置与数据集**：实验在AWS m5.xlarge实例上进行。使用了两个基准测试：1) **BIRD**，一个专注于评估现实数据库翻译准确性的文本到SQL基准；2) **TPC-H**，一个经典的数据分析基准，支持数据规模的确定性扩展，用于评估大数据场景。评估对象为来自不同提供商的一系列前沿LLM模型（如GPT-4o、Gemini系列、Claude Opus系列等），均通过官方API调用，并采用标准化的采样超参数（如温度、top-p）和低延迟推理配置。成本基于各模型的按令牌计价计算。

**对比方法与主要结果**：
1.  **传统文本到SQL指标的有效性分析**：在从BIRD数据集中选取的8个所有模型平均执行准确率（EX）≥0.85的查询上，实验表明，仅凭EX和端到端执行时间无法有效区分模型。例如，GPT-4o比Gemini 3 Flash快27.79%，但准确率不完美（EX 0.93 vs 1.00），在错误查询成本高的情况下，后者可能更优。新模型（如Opus 4.6）在零样本智能体文本到SQL任务中并未全面超越旧模型（如GPT-4o），可能在完美准确率的同时带来更长的执行时间（增加92.37%）。执行时间分解显示，“检查查询”阶段在所有模型中均占主导，但不同模型在各阶段时间占比差异显著（如GPT-5与GPT-5.2相差23%），提示了按阶段进行模型选择的优化潜力。
2.  **文本到大数据SQL指标的优越性**：论文提出了VES*（考虑精度和智能体执行时间）和VCES（进一步纳入成本）等新指标。实验显示，在区分模型方面，VES*的离散范围（809.09%）远优于仅考虑查询执行时间和准确率的VES（54.93%）。VES*将GPT-4o排名最高，同时揭示了Opus模型虽执行时间长但因完美准确率而获益的细微差别。成本评估中，VCES指标识别出Gemini 3 Flash因每令牌成本最低而成为最具成本效益的选项，其每次查询成本（CVQ）为0.0044美元，而GPT-4o的成本（0.0107美元）是其两倍以上，部分归因于较低准确率导致更多失败查询和令牌消耗。
3.  **数据规模影响的量化**：在TPC-H基准上，选取了模型处理有困难的查询（1, 17, 18, 21）进行研究。实验表明，随着数据规模因子（SF）增加，智能体性能的相对重要性下降，而SQL执行变得更重要。关键发现是，查询失败的成本随数据规模急剧放大：例如，在相同集群上执行无效的TPC-H Query 21，在SF 1000时的成本是SF 10时的13.30倍。文本到SQL指标（如VES）在不同规模下呈现模型间的恒定关系，而提出的SVQ指标能更好地捕捉模型在不同规模下的潜在成本损失，突显了即使较小的准确率差距（如Opus 4.5与GPT-5.2相差10%）在更大规模下也会被显著放大。

### Q5: 有什么可以进一步探索的点？

本文提出的“Text-to-Big SQL”框架虽具开创性，但仍存在若干局限与可拓展方向。首先，其核心挑战在于如何将语义优化与物理执行成本深度结合。当前研究虽引入VCES、CVQ等指标，但优化过程仍依赖历史执行轨迹，缺乏对动态数据分布与集群状态的实时感知。未来可探索集成在线学习机制，使Agent能根据运行时反馈（如数据倾斜、资源竞争）动态调整查询计划。

其次，论文提及的近似查询与UDF支持尚处概念阶段。实际生产中，用户对“快速运行”的需求往往伴随精度容忍度的模糊表述，需开发更细粒度的意图理解模型，将自然语言QoS描述转化为具体的优化约束（如最大延迟、最小采样率）。同时，UDF的生成需突破纯SQL范式，可结合代码生成与API检索技术，实现SQL与DataFrame等混合代码的联合优化。

最后，Agent内部阶段的模型调度策略仍有优化空间。当前“快模型”与“便宜模型”的静态分配忽略了查询复杂度与数据规模的关联性。未来可构建多目标强化学习框架，在延迟、成本、准确性间实现动态权衡，并探索轻量级物理计划优化器，以适配交互式分析的秒级响应需求。这些方向将推动Text-to-Big SQL从实验性指标走向生产级系统。

### Q6: 总结一下论文的主要内容

该论文聚焦于“文本到大数据SQL”这一被忽视的领域，即文本到SQL系统与大数据工作流（如大规模数据处理或交互式数据分析）的集成。研究指出，现有文本到SQL基准测试范围狭窄，忽略了数据规模扩大时产生的成本和性能影响，例如在小数据集上微小的翻译错误在数据量增大后会导致显著的延迟和成本开销。

为此，论文提出了专门针对“文本到大数据SQL”的新评估指标，以捕捉执行效率、成本及数据规模效应。通过评估前沿的生产级LLM智能体，研究证明了传统文本到SQL指标在大数据场景下的不足，而新提出的指标能更准确地反映实际性能与成本。主要结论是，这些指标为评估“文本到大数据SQL”的性能和成本提供了有效框架，并揭示了LLM在延迟和成本方面的细粒度差异，为未来研究和实际应用奠定了基础。
