---
title: "Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies"
authors:
  - "Siddhant Kulkarni"
  - "Yukta Kulkarni"
date: "2026-03-24"
arxiv_id: "2603.22651"
arxiv_url: "https://arxiv.org/abs/2603.22651"
pdf_url: "https://arxiv.org/pdf/2603.22651v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "多智能体架构"
  - "信息抽取"
  - "基准评测"
  - "成本-精度权衡"
  - "生产部署"
  - "金融文档处理"
  - "编排模式"
relevance_score: 7.5
---

# Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies

## 原始摘要

The adoption of large language models (LLMs) for structured information extraction from financial documents has accelerated rapidly, yet production deployments face fundamental architectural decisions with limited empirical guidance. We present a systematic benchmark comparing four multi-agent orchestration architectures: sequential pipeline, parallel fan-out with merge, hierarchical supervisor-worker and reflexive self-correcting loop. These are evaluated across five frontier and open-weight LLMs on a corpus of 10,000 SEC filings (10-K, 10-Q and 8-K forms). Our evaluation spans 25 extraction field types covering governance structures, executive compensation and financial metrics, measured along five axes: field-level F1, document-level accuracy, end-to-end latency, cost per document and token efficiency. We find that reflexive architectures achieve the highest field-level F1 (0.943) but at 2.3x the cost of sequential baselines, while hierarchical architectures occupy the most favorable position on the cost-accuracy Pareto frontier (F1 0.921 at 1.4x cost). We further present ablation studies on semantic caching, model routing and adaptive retry strategies, demonstrating that hybrid configurations can recover 89\% of the reflexive architecture's accuracy gains at only 1.15x baseline cost. Our scaling analysis from 1K to 100K documents per day reveals non-obvious throughput-accuracy degradation curves that inform capacity planning. These findings provide actionable guidance for practitioners deploying multi-agent LLM systems in regulated financial environments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决金融文档处理领域采用大型语言模型（LLM）进行结构化信息抽取时，面临的多智能体系统架构选择缺乏实证指导的核心问题。研究背景是金融服务业每年产生海量的监管文件（如SEC filings），传统基于规则或命名实体识别的抽取方法正被更通用的LLM系统所取代。然而，现有单提示（single-prompt）LLM抽取方法存在明显不足：上下文窗口限制导致文档分块会破坏跨引用依赖关系，幻觉率随抽取复杂性增加而升高，且缺乏验证机制使得错误检测困难。

尽管多智能体架构通过分解子任务、引入验证循环和动态资源分配来应对这些限制，但其编排模式的设计空间非常广阔。目前业界缺乏实证证据来指导不同架构模式（如顺序、并行、分层、反射式）在具体操作要求下的优劣选择。这种空白带来严重后果：金融机构在处理大量文档时，架构选择可能导致基础设施成本数量级差异，而监管义务又要求抽取精度必须超过特定阈值以确保审计可辩护性。错误的架构决策可能造成成本过高或错误率不可接受，且系统上线后难以逆转。

因此，本文要解决的核心问题是：系统性地评估和比较不同多智能体LLM编排架构在金融文档处理中的性能，为生产部署提供基于实证的、可操作的指导。具体聚焦于三大研究问题：不同编排模式在抽取精度、延迟和成本上的对比；跨架构和模型的成本-精度帕累托前沿及优势配置；以及处理规模从每日1K扩展到100K文档时架构性能特征的变化规律。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为多智能体协调框架、LLM系统评估方法、金融文档处理应用以及软件工程架构模式四大类。

在多智能体协调框架方面，相关研究包括奠定智能体推理基础的ReAct框架，以及实现不同抽象层次协调的AutoGen、CrewAI和LangGraph。MetaGPT则展示了结构化通信协议在减少幻觉传播上的作用。本文与这些工作的关系在于，它具体应用并系统比较了基于这些思想构建的四种编排架构（顺序、并行、分层、自反）。区别在于，先前研究多关注创意或编码任务，而本文专注于金融文档处理这一特定、受监管的领域。

在LLM系统评估方法方面，相关工作包括RAGAS、DSPy和HELM等通用评估框架，以及Document Understanding Benchmark和Financial NER等针对文档提取的基准。本文扩展了这些评估维度，将成本和延迟作为核心指标，并引入了摊销到每个提取字段的成本等新度量，以直接比较不同架构的令牌消耗模式。

在金融文档处理应用方面，相关研究有领域预训练的BloombergGPT、开源的FinGPT，以及Chen等人应用多智能体进行财务分析、Xie等人对SEC文件提取的基准测试。本文的不同之处在于，其比较焦点是编排架构而非单个模型，并首次在生产相关规模下纳入成本、延迟和吞吐量分析。

在软件工程架构模式方面，相关工作记录了思维链分解、Map-Reduce聚合等模式，以及Self-Refine、Reflexion等迭代自我改进方法。本文的分层和自反架构借鉴了这些模式，但将其专门适配于金融文档的结构化提取，并融入了领域特定的验证智能体和基于置信度的路由机制。

### Q3: 论文如何解决这个问题？

论文通过系统性地设计、实现和评估四种不同的多智能体编排架构来解决金融文档处理中的结构化信息提取问题。其核心方法是构建一个由多个专门化智能体组成的系统，这些智能体协同工作，并通过不同的编排模式来优化精度、成本、延迟和可扩展性之间的权衡。

**整体框架与主要模块**：所有架构都基于一组共同的原子智能体构建，包括文档解析器、字段提取器、表格分析器、交叉引用解析器、置信度评分器和输出格式化器。这些是系统的基本功能模块。论文的创新之处在于如何将这些模块组合成不同的编排模式，从而形成四种不同的系统架构。

**四种核心架构设计**：
1.  **顺序流水线**：智能体按固定顺序（解析→提取→分析→解析→格式化）执行，上下文信息逐级累积传递。其特点是执行顺序确定、延迟线性增长、无并行性，且上游错误会向下游传播。
2.  **并行扇出合并**：调度器根据文档内容将不同领域的提取任务（如财务指标、公司治理、高管薪酬）分发给多个并行的提取智能体，最后通过一个专门的合并/协调智能体汇总结果。这实现了任务并行，延迟取决于最慢的分支，且故障被隔离在各自分支内。
3.  **分层监督者-工作者**：引入一个监督者智能体进行动态任务规划和协调。它根据文档复杂度将任务分配给不同的工作者，并接收带有置信度评分的结果。对于低置信度的字段，监督者可以将其重新分配给其他工作者或更强的模型进行选择性重提取，从而在不过度增加成本的前提下提升精度。
4.  **反射式自校正循环**：在提取后引入一个验证智能体，对输出进行格式、跨字段一致性和来源依据的检查。如果验证失败，系统会进入一个由批判和校正智能体驱动的迭代修正循环（最多3次）。这种架构通过迭代精炼实现了最高的潜在精度，但成本和延迟变得不确定，且与文档复杂度相关。

**关键技术**：论文不仅比较了架构，还深入研究了多项优化技术，包括**语义缓存**（避免重复处理相似内容）、**模型路由**（将不同难度的任务分配给不同能力的LLM以优化成本）和**自适应重试策略**。研究表明，通过**混合配置**（例如在分层架构中结合选择性重试和模型路由），可以用仅比基线高15%的成本，恢复反射式架构89%的精度提升，从而找到成本-精度帕累托前沿上的最优点。此外，论文还进行了从每日处理1K到100K文档的扩展性分析，揭示了吞吐量与精度之间非显而易见的衰减曲线，为生产环境的能力规划提供了关键依据。

### Q4: 论文做了哪些实验？

论文实验系统评估了四种多智能体编排架构（顺序流水线、并行扇出合并、分层监督工作者、反射自校正循环）在金融文档信息抽取任务上的表现。实验设置上，使用包含10,000份SEC文件（10-K、10-Q和8-K表格）的语料库，涵盖25种抽取字段类型（公司治理、高管薪酬、财务指标）。评估了五种前沿或开源大语言模型（GPT-4o、Claude 3.5S、Gemini 1.5P、Llama3 70B、Mixtral 8x22B），并从五个维度进行度量：字段级F1分数、文档级严格准确率、端到端延迟、单文档成本和令牌效率。

主要结果包括：反射架构在Claude 3.5S上取得了最高的字段级F1（0.943），但成本是顺序基线的2.3倍（单文档0.430美元）；分层架构在成本-准确率帕累托边界上表现最佳（F1 0.921，成本为基线的1.4倍）；并行架构在延迟上降低了1.84倍，F1平均提升0.014。消融实验研究了语义缓存、模型路由和自适应重试策略，发现混合配置能以仅1.15倍基线成本恢复反射架构89%的准确率增益（优化后分层架构F1 0.924，成本0.148美元/文档）。扩展性分析显示，当日处理量从1K增至100K时，反射架构性能下降最快（100K时F1从0.943降至0.871），而顺序架构最具扩展弹性（F1仅下降0.017）。

### Q5: 有什么可以进一步探索的点？

该论文的局限性与未来研究方向主要体现在以下几个方面。首先，研究聚焦于金融文档（SEC filings），其格式相对规范，未来可探索架构在非结构化、多模态（如包含图表）或跨语言文档上的泛化能力。其次，实验基于特定LLM（如Claude 3.5），未充分探索开源模型与专有模型在成本-精度权衡上的动态组合策略，未来可研究更精细的模型路由机制。第三，评估指标虽全面，但未深入考虑现实生产环境中的动态因素，如文档流量的实时波动、模型API的速率限制与故障恢复，未来需纳入弹性与鲁棒性测试。

结合个人见解，可能的改进思路包括：1）引入强化学习动态优化架构选择与资源分配，根据文档复杂度与实时负载自适应切换流水线模式；2）探索知识蒸馏或模型缓存技术，将高成本“反思式”架构的自我纠正能力迁移至轻量级代理，以进一步压缩成本；3）将架构评估扩展至更复杂的任务链（如提取后推理、合规检查），研究多阶段任务中错误传播与累积效应。此外，可结合边缘计算研究混合部署策略，在本地与云端之间分配代理任务，以平衡延迟、成本与数据隐私。

### Q6: 总结一下论文的主要内容

该论文系统性地评估了四种多智能体大语言模型架构在金融文档处理任务中的性能，旨在为实际生产部署提供实证依据。研究问题聚焦于如何从SEC文件中高效、准确地提取结构化信息，并权衡不同架构在成本、准确性和延迟等方面的表现。

论文比较了四种编排架构：顺序流水线、并行扇出合并、分层监督-工作者和反射式自校正循环。方法上，研究在包含10,000份SEC文件的语料库上，使用五种前沿和开源大语言模型，对涵盖公司治理、高管薪酬和财务指标等25类提取字段进行了全面评估。评估维度包括字段级F1分数、文档级准确率、端到端延迟、单文档成本和令牌效率。

主要结论表明，反射式架构实现了最高的字段级F1分数（0.943），但成本是顺序基线的2.3倍；而分层架构在成本-准确性的帕累托前沿上占据最优位置（F1 0.921，成本为基线的1.4倍）。此外，研究通过对语义缓存、模型路由和自适应重试策略的消融实验证明，混合配置能以仅1.15倍基线成本恢复反射式架构89%的准确性提升。论文的规模化分析还揭示了从每日处理1K到100K文档时，吞吐量与准确性之间非线性的退化曲线，为产能规划提供了关键见解。这些发现为在受监管的金融环境中部署多智能体大语言模型系统提供了可操作的指导。
