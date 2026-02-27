---
title: "Both Ends Count! Just How Good are LLM Agents at \"Text-to-Big SQL\"?"
authors:
  - "Germán T. Eizaguirre"
  - "Lars Tissen"
  - "Marc Sánchez-Artigas"
date: "2026-02-25"
arxiv_id: "2602.21480"
arxiv_url: "https://arxiv.org/abs/2602.21480"
pdf_url: "https://arxiv.org/pdf/2602.21480v2"
categories:
  - "cs.DB"
  - "cs.CL"
  - "cs.IR"
tags:
  - "LLM Agent"
  - "工具使用"
  - "评测基准"
  - "Text-to-SQL"
  - "数据库交互"
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

这篇论文旨在解决传统文本到SQL（Text-to-SQL）评估方法在应对大数据（Big Data）场景时的局限性问题。研究背景是，随着大语言模型（LLM）和智能体（Agent）技术的发展，Text-to-SQL系统在实际生产中常被集成到大数据工作流（如大规模数据处理或交互式数据分析）中，形成了所谓的“文本到大数据SQL”（Text-to-Big SQL）。然而，现有Text-to-SQL基准测试（如Spider、BIRD）通常局限于中小型关系数据库，主要关注查询翻译的准确性（如二元正确性指标），而忽视了大数据环境下的关键挑战。

现有方法的不足主要体现在三个方面：首先，它们忽略了查询执行的成本和性能影响。在大数据系统中，即使是微小的翻译错误（如多投影一个不必要的列），也可能导致扫描海量数据，从而产生巨大的计算资源和金钱成本，而传统二元正确性指标无法反映这种部分正确性或代价差异。其次，现有评估未充分考虑智能体框架（如ReAct）中LLM推理、工具调用与查询执行之间的交互效率。在交互式分析中，如果SQL生成过程（包括模式检查、语法验证）的延迟超过物理查询执行时间，系统响应性将大打折扣。最后，传统基准未能联合评估查询生成端与执行端的整体表现，而大数据环境恰恰要求两端并重。

因此，本文要解决的核心问题是：如何为Text-to-Big SQL场景设计一个全面的评估框架，以弥补现有基准的不足。具体而言，论文提出新的评估指标和方法，旨在同时衡量智能体行动、推理延迟、生成查询的成本效益以及部分正确性，从而更准确地反映在大数据引擎上实际运行查询时的效率、成本和规模影响。通过系统评估前沿LLM在统一ReAct式智能体架构中的表现，研究揭示了超越准确性的洞察，例如某些模型虽正确率高，却因推理或工具协调开销而导致交互性下降。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：传统文本到SQL（Text-to-SQL）方法、大数据库系统与查询执行评估、以及基于LLM的智能体系统。

在**传统Text-to-SQL方法**方面，已有大量研究致力于通过序列到序列模型、语义解析或基于LLM的方法，将自然语言问题转换为SQL查询。这些工作通常使用Spider、WikiSQL等基准进行评估，重点关注翻译准确率等孤立指标。然而，这些基准大多针对中小规模的关系型数据库，评估指标（如二元正确性）往往忽略部分正确性，且未考虑查询在大数据环境下的执行成本与性能影响。本文指出，这种传统评估方式在“Text-to-Big SQL”场景下是不充分的，因为即使微小的翻译错误（如多余列）在数据量极大时也会导致显著的资源浪费和延迟。

在**大数据库系统与执行评估**领域，研究通常关注TPC-H等基准下查询引擎的性能优化、成本模型及执行效率。但这些工作很少与自然语言接口结合，未能考察从文本生成SQL这一环节对整体工作流的影响。本文则强调必须将SQL生成端与大数据执行端共同作为“一等公民”进行考量，提出了同时涵盖部分正确性、执行成本和延迟的新型评估指标，以反映实际生产环境中规模扩展带来的影响。

在**基于LLM的智能体系统**方面，ReAct等框架通过工具调用、推理步骤和反馈循环来增强LLM的任务完成能力。已有研究将此类智能体应用于Text-to-SQL任务，以提升跨领域适应性和查询修正能力。然而，现有评估缺乏对智能体推理延迟、工具编排开销与大数据查询执行之间相互作用的深入分析。本文通过在一个统一的ReAct式智能体架构中系统评估前沿LLM，揭示了模型在追求高准确率时可能引入的交互性下降问题（如推理开销过大），填补了该领域的空白。

综上，本文与相关工作的核心区别在于：首次将Text-to-SQL与大数据执行环境紧密结合，提出了一套专为“Text-to-Big SQL”设计的新型评估框架与指标，重点关注LLM智能体在零射击场景下的端到端性能、成本效益及规模扩展影响，突破了传统基准的局限。

### Q3: 论文如何解决这个问题？

论文通过提出一套新的评估指标和设计一个适配的AI智能体系统来解决“Text-to-Big SQL”场景下现有文本到SQL评估指标的不足。其核心在于认识到传统指标（如精确匹配、执行准确率）仅关注查询结果的绝对正确性，而忽视了在大数据规模下，部分正确或包含冗余的查询所带来的巨大执行成本与延迟开销。

**核心方法与架构设计**：
研究采用了一个基于ReAct（推理+行动）框架的AI智能体作为评估平台。该智能体结构简洁，包含两个核心组件：**控制器**（由生产级大语言模型担任）和**执行器**（负责连接工具并管理执行循环）。控制器遵循ReAct的“思考-行动-观察”循环进行推理，决定如何使用工具并生成最终SQL。执行器则负责调用工具并处理循环逻辑。下游查询引擎选用广泛应用的Spark SQL来处理大规模数据。

智能体通过四个定义明确的工具与Spark会话交互：
1.  **list_tables**: 列出可用表。
2.  **get_schema**: 获取表结构，并可选择性地获取样本行。
3.  **check_query**: 使用一个LLM“检查器”验证查询语法。
4.  **run_query**: 在Spark中执行SQL查询。

一个关键的设计决策是，为防止在大数据环境中无限制的循环执行导致资源浪费或成本激增，智能体在首次执行`run_query`后立即终止，不进行迭代修正。

**关键技术指标与创新点**：
论文的主要创新在于提出了一套全新的“Text-to-Big SQL”评估指标，以弥补传统指标的缺陷：
1.  **VES***：在标准有效效率分数（VES）基础上进行了扩展。它引入了**列级精度**（P）来惩罚结果中包含的无关（冗余）列，因为这些列虽不影响用户手动验证结果，却会增加处理开销和成本。同时，它综合考虑了**端到端时间**（Te2e），涵盖了LLM与智能体交互、工具执行以及大数据引擎查询运行的全部时间。VES* 是正确性指示函数、列精度和相对于黄金查询执行时间的效率比三者的乘积平均值。
2.  **VCES**：在VES* 的基础上，进一步纳入了**端到端执行成本**（Ce2e），形成了一个面向成本的度量标准，特别适用于云部署场景。
3.  **CVQ**：定义了“每个有效查询的预期成本”，它基于几何分布，量化了在“重试直至成功”策略下获得一个有效结果所需的预期成本，与单次尝试的有效率（p）相关。

总之，论文的解决方案是双重的：在**系统层面**，设计了一个基于ReAct的、工具化的LLM智能体来模拟真实的大数据SQL生成与执行流程；在**评估层面**，创造性地提出了VES*、VCES和CVQ这一组指标，将查询结果的“部分正确性”（特别是冗余列）、执行时间、资源成本以及数据规模的影响共同纳入评估体系，从而更全面、真实地反映LLM智能体在“Text-to-Big SQL”任务中的实际效能与经济效益。

### Q4: 论文做了哪些实验？

论文实验主要分为三个部分，旨在评估LLM智能体在“文本到大数据SQL”场景下的表现，并验证其提出的新指标的有效性。

**实验设置**：实验在AWS m5.xlarge EC2实例上进行。评估对象为来自不同提供商的一系列前沿大语言模型（如GPT-4o、Gemini系列、Claude Opus系列等），均通过官方API调用，并采用低延迟推理配置。采样超参数（如温度、top-p）在各API间进行了标准化。

**数据集与基准测试**：使用了两个基准测试：
1.  **BIRD**：一个专注于文本到SQL的基准，用于评估在真实数据库上的翻译准确性。
2.  **TPC-H**：一个经典的数据分析基准，用于衡量关系数据上复杂即席业务查询的数据库性能。其数据可确定性缩放，非常适合评估大数据场景。

**对比方法与主要结果**：
1.  **揭示传统文本到SQL指标的不足**：在BIRD数据集上选取了所有测试模型（除GPT-5.2外）平均执行准确率（EX）均不低于0.85的8个查询。结果显示，仅凭EX和端到端执行时间无法有效区分模型。例如，GPT-4o比Gemini 3 Flash快27.79%但准确率不完美；Claude Opus 4.6达到完美准确率但执行时间比GPT-4o长92.37%。对执行时间的细分显示，“检查查询”阶段耗时占比最高，但不同模型间差异显著（如GPT-5与GPT-5.2相差23%），表明按阶段进行模型选择具有优化潜力。
2.  **验证文本到大数据SQL新指标的优越性**：提出了VES*（考虑代理交互效率和投影开销）和VCES（进一步纳入成本）等新指标。在BIRD查询上的实验表明，VES*比仅考虑查询执行时间和结果准确率的VES具有更好的区分度（离散范围809.09% vs. 54.93%），能更清晰地区分“快”与“慢”的模型类别。VCES指标则识别出Gemini 3 Flash是成本效益最高的模型，其每次查询成本（CVQ）为0.0044美元，而GPT-4o为0.0107美元，揭示了延迟最优与成本最优模型之间的权衡。
3.  **量化数据规模的影响**：在TPC-H基准上，选取了模型准确率较差的查询（Q1, Q17, Q18, Q21），并在不同数据规模因子（SF）下进行测试。结果显示，数据规模是关键因素：在小规模下，智能体交互主导总执行时间；在大规模下（如从SF10扩展到SF1000，TPC-H Q21执行时间增加13.3倍），查询执行时间成为瓶颈。实验表明，传统VES指标在不同规模下呈现恒定关系，而CVQ指标能更好地捕捉模型在不同规模下的潜在成本损失——不准确的模型（如Gemini 3 Pro）在大规模下因查询错误会导致成本大幅增加。

### Q5: 有什么可以进一步探索的点？

本文指出了现有文本到SQL研究在应对大数据场景时的局限性，即过度关注翻译准确性而忽视了执行成本、延迟及数据规模的影响。未来可探索的方向包括：第一，**智能体内部优化**，研究如何为生成、执行等不同阶段动态分配“快而省”的专用模型，但需解决现有物理计划优化方法延迟过高、难以满足交互式分析需求的问题。第二，**面向大规模执行的查询优化**，需突破语法正确但执行低效的瓶颈，例如利用历史执行轨迹与性能指标进行语义匹配与成本预估，实现查询重写；或引入近似查询（如采样聚合）在满足意图的前提下大幅降低成本，并可结合用户提供的QoS标注进行引导。第三，**支持用户自定义函数（UDF）**，大数据引擎常依赖UDF，因此需扩展文本到Big SQL框架，使其能生成兼容UDF的混合代码（如SQL结合Spark DataFrames），这超越了传统文本到SQL的范畴。此外，如何将物理计划与成本模型融入优化过程，以实现感知数据规模的动态优化，而非静态翻译，也是一个关键挑战。

### Q6: 总结一下论文的主要内容

本文针对“文本到大数据SQL”这一研究不足的领域，探讨了现有文本到SQL基准在评估与大数据引擎集成时的局限性。论文核心贡献在于首次提出了一套新颖且具有代表性的“文本到大数据SQL”评估指标。传统文本到SQL指标范围狭窄，忽略了数据规模扩大时产生的成本和性能影响，例如轻微翻译错误在小数据集上无关紧要，但在大数据量下会导致显著的延迟和成本开销。

为此，作者评估了前沿的生产级LLM智能体，这是一个与数据库无关、可适应多样化需求的系统。研究表明，传统文本到SQL指标不足以评估大数据场景，而新提出的指标能准确反映执行效率、成本以及数据规模的影响。论文还提供了针对LLM的深入洞察，包括跨模型在延迟和成本方面的细粒度比较。主要结论是，这项工作为“文本到大数据SQL”建立了一个有效的评估框架，揭示了新的现实挑战，并指导了该领域的未来研究方向。
