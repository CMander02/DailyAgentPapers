---
title: "Search More, Think Less: Rethinking Long-Horizon Agentic Search for Efficiency and Generalization"
authors:
  - "Qianben Chen"
  - "Tianrui Qin"
  - "King Zhu"
  - "Qiexiang Wang"
  - "Chengjun Yu"
date: "2026-02-26"
arxiv_id: "2602.22675"
arxiv_url: "https://arxiv.org/abs/2602.22675"
pdf_url: "https://arxiv.org/pdf/2602.22675v1"
categories:
  - "cs.CL"
tags:
  - "Tool Use & API Interaction"
  - "Memory & Context Management"
relevance_score: 9.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Memory & Context Management"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "Search More, Think Less (SMTL)"
  primary_benchmark: "BrowseComp, GAIA, Xbench, DeepResearch Bench"
---

# Search More, Think Less: Rethinking Long-Horizon Agentic Search for Efficiency and Generalization

## 原始摘要

Recent deep research agents primarily improve performance by scaling reasoning depth, but this leads to high inference cost and latency in search-intensive scenarios. Moreover, generalization across heterogeneous research settings remains challenging. In this work, we propose \emph{Search More, Think Less} (SMTL), a framework for long-horizon agentic search that targets both efficiency and generalization. SMTL replaces sequential reasoning with parallel evidence acquisition, enabling efficient context management under constrained context budgets. To support generalization across task types, we further introduce a unified data synthesis pipeline that constructs search tasks spanning both deterministic question answering and open-ended research scenarios with task appropriate evaluation metrics. We train an end-to-end agent using supervised fine-tuning and reinforcement learning, achieving strong and often state of the art performance across benchmarks including BrowseComp (48.6\%), GAIA (75.7\%), Xbench (82.0\%), and DeepResearch Bench (45.9\%). Compared to Mirothinker-v1.0, SMTL with maximum 100 interaction steps reduces the average number of reasoning steps on BrowseComp by 70.7\%, while improving accuracy.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度研究智能体在长视野搜索任务中面临的效率与泛化性双重挑战。研究背景是，当前深度研究智能体主要通过增加推理深度和工具调用次数来提升性能，但这在搜索密集型场景中会导致高昂的推理成本和延迟。同时，现有方法在泛化性方面存在明显不足：现有的智能体搜索任务大致可分为两类，一类是具有明确标准答案的确定性问答任务（如BrowseComp、GAIA），另一类是无单一正确答案的开放式研究任务（如DeepResearch Bench）。这两类任务的优化目标和评估标准差异很大，导致针对一种设置训练的智能体难以泛化到另一种设置，缺乏一个能在两种场景中都表现良好的统一智能体。

本文要解决的核心问题有两个方面：一是如何突破现有深度研究智能体因依赖线性、顺序推理而导致的效率瓶颈，实现高效的长视野推理；二是如何克服智能体在不同类型任务间泛化能力差的问题。为此，论文提出了“多搜索，少思考”框架，其核心是用并行证据获取取代顺序推理，并通过结构化的上下文管理在受限的上下文预算下实现高效推理。同时，论文设计了一个统一的数据合成流程，构建涵盖确定性和开放式场景的多样化搜索任务，以支持跨任务类型的泛化能力。最终目标是训练一个端到端的智能体，在保证高性能的同时，显著提升执行效率。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为**智能体框架与系统**和**合成数据管道**两大类。

在**智能体框架与系统**方面，主流研究通过外部编排器增强大语言模型，使其具备规划、多步工具使用和环境交互能力，以处理搜索密集型任务。相关工作包括采用控制器分解查询、调度工具的商业深度研究系统，以及如WebWeaver、OAgents等采用规划-研究/执行流程的结构化框架。开源生态也提供了可复用的编排模板和多智能体工作流。然而，这些现有工作普遍通过加深**顺序推理**和延长交互步骤来提升性能，导致计算资源大量消耗在模型推理而非有效的外部证据获取上。本文提出的SMTL框架与这些工作的核心区别在于，它用**并行证据获取**取代了顺序推理，旨在信息效率和上下文管理上实现突破。

在**合成数据管道**方面，高质量训练数据对搜索智能体至关重要。现有方法主要包括基于知识图谱的生成（如WebSailor）和遵循由易到难扩展范式的生成（如WebShaper、ASearcher）。这些方法强调了工具在环生成的有效性，但主要关注增加任务难度或上下文长度，而非明确塑造信息高效的搜索与验证行为。此外，现有管道主要围绕确定性问答或结构严格的任务设计，对合成需要灵活信息聚合和跨源验证的开放式研究任务支持有限。本文的贡献在于提出了一个**统一的数据合成流程**，能够构建涵盖确定性问答和开放式研究场景的搜索任务，并配以相应的评估指标，从而更好地支持智能体在不同任务类型间的泛化。

### Q3: 论文如何解决这个问题？

论文通过提出“多搜索、少思考”（SMTL）框架来解决长视野智能体搜索中的效率与泛化问题。其核心方法是用并行证据获取替代传统的顺序推理，从而在有限的上下文预算下实现高效的信息管理和任务执行。

整体框架是一个并行的智能体工作流，主要包含三个关键模块：初始计划构建、并行执行与工具协调、动态计划精炼。首先，给定一个复合搜索任务，智能体通过问题分解构建一个初始任务计划图，将任务拆分为一系列相互关联但部分独立的子任务，这些子任务对应具体的信息检索或验证目标，旨在早期暴露可并行执行的路径。其次，系统在每个时间步从待处理子任务集中选择可执行的子任务进行并行处理，利用外部工具（如网络搜索和页面爬取）同时获取证据，并将所有并行执行的行动和观察聚合到一个统一的推理状态中，以此加速任务完成并减少顺序瓶颈。最后，系统周期性地根据当前执行状态（如已完成子任务、待处理子任务和推理状态）对任务计划进行动态精炼，更新计划以移除已完成任务、解决未决依赖或引入新子任务，确保计划能适应进展并保持效率。

在架构设计上，该工作流支持子任务的并发执行和结构化协调，通过明确的并行化机制和状态聚合函数来管理上下文。关键技术包括：1）并行证据获取机制，允许同时执行多个信息寻求子任务；2）动态计划精炼算法，使任务计划能随执行过程自适应调整；3）统一的推理状态表示，整合并行执行结果以支持后续决策。

创新点主要体现在两方面：一是效率上，通过并行化显著减少了推理步骤（如在BrowseComp基准上比Mirothinker-v1.0减少70.7%的平均推理步骤），降低了推理成本和延迟；二是泛化上，框架设计不依赖于特定任务类型，通过统一的数据合成流程支持跨确定性问答和开放式研究场景的泛化，从而在多个基准上实现了先进性能。

### Q4: 论文做了哪些实验？

论文在实验部分进行了全面的评估。实验设置方面，作者使用Qwen3-30B-A3B-Instruct-2507作为骨干模型，通过监督微调（3.5个epoch，批次大小128）和强化学习（学习率1e-6，批次大小32）进行训练。推理时使用vLLM，上下文窗口为128K token，并设置了最大100或300次交互步骤（SMTL-100和SMTL-300），以及每5步进行一次计划精炼的上下文管理策略。

数据集和基准测试涵盖了深度搜索和深度研究两类场景。深度搜索基准包括BrowseComp、GAIA、XBench-DeepSearch、WebWalkerQA、FRAMES和SEAL-0。深度研究评估则使用Deep Research Bench RACE，从全面性、洞察深度、指令遵循和可读性四个细粒度标准评估长篇研究报告。

对比方法分为三类：1）具备工具使用能力的基础模型（如Claude-4.5-Sonnet、GPT-5、GLM-4.5等）；2）深度研究系统（如OpenAI DeepResearch、Gemini DeepResearch、Perplexity Deep Research等）；3）开源智能体模型（如WebSailor-32B、MiroThinker-v1.0-30B等）。

主要结果方面，SMTL在多个基准上取得了领先或具有竞争力的性能。关键数据指标如下：在深度搜索任务中，SMTL-300在BrowseComp上达到48.6%，GAIA上达到75.7%，XBench-DeepSearch上达到82.0%，WebWalker-QA上达到76.5%。与基线模型MiroThinker-v1.0-30B相比，SMTL-100在BrowseComp上将平均推理步骤减少了70.7%，同时准确率更高（43.6% vs 41.2%）。在深度研究基准RACE上，SMTL-100总体得分为45.9%，在洞察深度（45.6%）、指令遵循（49.6%）和可读性（45.5%）方面表现均衡且强劲。这些结果表明SMTL在效率和泛化能力上均具有优势。

### Q5: 有什么可以进一步探索的点？

该论文提出的SMTL框架在效率和泛化性上取得了进展，但仍存在一些局限和可探索的方向。首先，其并行证据获取机制虽提升了效率，但在高度动态或信息相互依赖的复杂任务中，可能因缺乏对证据间关联性的深度推理而影响决策质量。未来可研究如何动态平衡“并行搜索”与“必要序列推理”，例如引入轻量级元认知模块，在关键决策点自动触发深度思考。

其次，论文的泛化性测试虽涵盖多类基准，但任务环境仍相对结构化。真实世界的研究任务往往涉及模糊目标、多模态信息和对抗性噪声。可探索将SMTL扩展至开放域动态环境，例如结合世界模型进行模拟演练，或设计针对信息冲突场景的置信度校准机制。

此外，训练依赖合成数据管道，虽提升了覆盖面，但可能与真实用户查询分布存在差距。未来可研究通过在线学习或人类反馈强化学习（RLHF）持续优化，使智能体能适应不断演化的搜索模式。最后，该框架的计算效率提升主要集中在推理阶段，未来可探索模型压缩、蒸馏等技术，进一步降低部署成本，推动其在边缘设备上的应用。

### Q6: 总结一下论文的主要内容

该论文针对现有深度研究智能体在搜索密集型场景中因过度依赖深度推理而导致的高计算成本和延迟问题，以及在不同研究设置间泛化能力不足的挑战，提出了“Search More, Think Less”框架。其核心贡献在于通过并行证据获取取代传统的顺序推理，从而在有限的上下文预算下实现高效的信息管理。为了提升跨任务类型的泛化能力，论文设计了一个统一的数据合成流程，能够构建涵盖确定性问答和开放式研究场景的多样化搜索任务，并配以相应的评估指标。方法上，作者结合监督微调和强化学习训练了一个端到端的智能体。实验结果表明，该智能体在BrowseComp、GAIA、Xbench和DeepResearch Bench等多个基准测试中取得了优异性能，部分达到领先水平。与基线模型相比，在保持甚至提升准确率的同时，显著减少了推理步骤，例如在BrowseComp上将平均推理步骤降低了70.7%，有效平衡了效率与性能。
