---
title: "Search More, Think Less: Rethinking Long-Horizon Agentic Search for Efficiency and Generalization"
authors:
  - "Qianben Chen"
  - "Tianrui Qin"
  - "King Zhu"
  - "Qiexiang Wang"
  - "Chengjun Yu"
  - "Shu Xu"
  - "Jiaqi Wu"
  - "Jiayu Zhang"
  - "Xinpeng Liu"
  - "Xin Gui"
  - "Jingyi Cao"
  - "Piaohong Wang"
  - "Dingfeng Shi"
  - "He Zhu"
  - "Tiannan Wang"
  - "Yuqing Wang"
  - "Maojia Song"
  - "Tianyu Zheng"
  - "Ge Zhang"
  - "Jian Yang"
date: "2026-02-26"
arxiv_id: "2602.22675"
arxiv_url: "https://arxiv.org/abs/2602.22675"
pdf_url: "https://arxiv.org/pdf/2602.22675v1"
categories:
  - "cs.CL"
tags:
  - "Agent 架构"
  - "Agent 数据合成"
  - "Agent 规划/推理"
  - "工具使用"
  - "强化学习"
  - "Agent 评测/基准"
  - "效率优化"
  - "长视野任务"
relevance_score: 9.5
---

# Search More, Think Less: Rethinking Long-Horizon Agentic Search for Efficiency and Generalization

## 原始摘要

Recent deep research agents primarily improve performance by scaling reasoning depth, but this leads to high inference cost and latency in search-intensive scenarios. Moreover, generalization across heterogeneous research settings remains challenging. In this work, we propose \emph{Search More, Think Less} (SMTL), a framework for long-horizon agentic search that targets both efficiency and generalization. SMTL replaces sequential reasoning with parallel evidence acquisition, enabling efficient context management under constrained context budgets. To support generalization across task types, we further introduce a unified data synthesis pipeline that constructs search tasks spanning both deterministic question answering and open-ended research scenarios with task appropriate evaluation metrics. We train an end-to-end agent using supervised fine-tuning and reinforcement learning, achieving strong and often state of the art performance across benchmarks including BrowseComp (48.6\%), GAIA (75.7\%), Xbench (82.0\%), and DeepResearch Bench (45.9\%). Compared to Mirothinker-v1.0, SMTL with maximum 100 interaction steps reduces the average number of reasoning steps on BrowseComp by 70.7\%, while improving accuracy.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度研究智能体在长视野搜索任务中面临的效率与泛化性双重挑战。当前，基于大语言模型的智能体主要通过增加推理深度和工具调用次数来提升任务性能，但这导致了高昂的推理成本和延迟，尤其在搜索密集型场景中。同时，现有研究任务主要分为两类：一类是具有明确标准答案的确定性问答任务（如BrowseComp、GAIA），另一类是开放式研究问题（如DeepResearch Bench），两者优化目标和评估标准差异巨大。这使得为单一任务类型训练的智能体难以泛化到另一类型，缺乏一个能同时兼顾高效执行与跨任务泛化能力的统一智能体。

针对现有方法依赖线性、顺序推理导致的效率瓶颈，以及任务类型单一导致的泛化性不足，本文提出了“多搜索、少思考”框架。其核心是设计一种并行的智能体工作流，用并行证据获取替代顺序推理，并结合结构化的上下文管理，以在有限的上下文预算内实现高效的长视野推理。此外，论文构建了一个统一的数据合成管道，自动生成涵盖确定性与开放式场景的多样化搜索任务，旨在减少数据冗余并从根本上提升模型的跨任务泛化能力。通过监督微调和强化学习的端到端训练，该方法在多个基准测试上实现了性能与效率的显著提升。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为**智能体框架与系统**和**合成数据管道**两大类。

在**智能体框架与系统**方面，主流研究通过外部编排器增强大语言模型，使其具备规划、多步工具使用和环境交互能力，以处理搜索密集型任务。相关工作包括采用控制器分解查询、调度工具并聚合结果的商业深度研究系统，以及如WebWeaver、OAgents等采用规划-研究/执行流程的结构化框架。开源生态也提供了可复用的编排模板和多智能体工作流。然而，这些现有工作普遍通过加深**顺序推理**和延长交互步骤来提升性能，导致计算资源大量消耗在模型推理而非有效的外部证据获取上。本文提出的SMTL框架与这些工作的核心区别在于，它用**并行证据获取**替代了顺序推理，旨在提升信息获取效率，而非单纯增加推理深度。

在**合成数据管道**方面，高质量训练数据的生成是关键。现有方法主要包括基于知识图谱的生成（如WebSailor）和由易到难的扩展范式（如WebShaper、ASearcher）。这些方法虽证明了工具在环生成的有效性，但主要关注增加任务难度或上下文长度，而非显式塑造高效的信息搜索与验证行为。此外，现有管道主要围绕确定性问答或结构受限的任务设计，对需要灵活信息聚合与跨源验证的**开放式研究任务**支持有限。本文的贡献在于提出了一个**统一的数据合成管道**，能够构建涵盖确定性问答和开放式研究场景的多样化搜索任务，并配以相应的评估指标，从而更好地支持智能体在不同任务类型间的泛化。

### Q3: 论文如何解决这个问题？

论文通过提出“多搜索，少思考”（SMTL）框架来解决长视野智能体搜索中的效率与泛化问题。其核心方法是用并行证据获取取代传统的顺序推理，从而在有限的上下文预算下实现高效的信息管理与任务执行。

整体框架是一个端到端的并行智能体工作流，主要包含三个关键模块：初始计划构建、并行执行与工具协调、动态计划精炼。首先，给定一个复合搜索任务，智能体通过问题分解生成一个初始任务计划图，将任务拆分为一系列相互关联但部分独立的子任务，从而早期暴露可并行执行的路径。其次，系统在每个时间步从待处理子任务集中选择可执行的子任务进行并行处理，利用外部工具（如网络搜索、页面爬取）并发地获取信息和执行推理，并将所有并行执行的行动与观察聚合到一个统一的推理状态中，以加速任务完成并减少顺序瓶颈。最后，系统周期性地根据当前执行状态（如已完成子任务、待处理子任务和推理状态）对任务计划进行动态精炼，更新计划以移除已完成任务、解决未决依赖或引入新子任务，确保计划能适应进展并保持效率。

在架构设计上，该工作流明确支持子任务间的并发执行与结构化协调，通过迭代的计划-执行-精炼循环实现高效搜索。关键技术创新点在于：1）**并行化工作流设计**：突破了传统智能体顺序推理的范式，通过并行执行显著减少了推理步骤（如在BrowseComp上比Mirothinker-v1.0减少70.7%），提升了效率；2）**动态计划精炼机制**：使智能体能根据收集到的证据自适应调整任务结构，增强了在复杂长视野任务中的鲁棒性；3）**统一的训练与评估管道**：论文还引入了一个统一的数据合成流程，构建涵盖确定性问答与开放式研究场景的搜索任务，并采用监督微调与强化学习相结合的方式训练智能体，从而支持跨任务类型的泛化，在多个基准测试中取得了先进性能。

### Q4: 论文做了哪些实验？

论文在实验部分进行了全面的评估，主要涵盖以下几个方面：

**实验设置与模型实现**：研究以 Qwen3-30B-A3B-Instruct-2507 为骨干模型，采用监督微调和强化学习两阶段训练。监督微调阶段训练3.5个周期，批量大小为128，初始学习率为1.4e-5，最大序列长度为65,536个token。强化学习阶段学习率为1e-6，批量大小为32，每个问题生成8个在线轨迹，最大序列长度为128k token，最多120个交互轮次。推理时使用vLLM，上下文窗口为128K token，并采用周期性计划精炼（默认每5步）和溢出触发压缩的上下文管理策略。实验主要评估了最大交互步数为100（SMTL-100）和300（SMTL-300）的两种配置。

**数据集与基准测试**：评估在两大类基准上进行。深度搜索（Deep Search）基准包括 BrowseComp、GAIA、XBench-DeepSearch、WebWalkerQA、FRAMES 和 SEAL-0。深度研究（Deep Research）基准使用 Deep Research Bench RACE，该基准评估长篇开放式研究报告，并给出整体分数及四个细粒度指标：全面性、洞察深度、指令遵循和可读性。

**对比方法**：与三大类系统进行了比较：1) 具备工具使用能力的基础模型，包括闭源模型（Claude-4.5-Sonnet, GPT-5, Gemini-2.5-Pro）和开源模型（GLM-4.5, Minimax-M2等）；2) 深度研究系统，如 OpenAI DeepResearch、Gemini DeepResearch、Perplexity Deep Research 等；3) 开源智能体模型，如 WebSailor-32B、WebDancer-QwQ、MiroThinker-v1.0-30B 等。

**主要结果与关键指标**：SMTL 在多个基准上取得了优异性能。在深度搜索任务中，SMTL-300 在 BrowseComp 上达到 48.6% 的准确率，在 GAIA 上达到 75.7%，在 XBench-DeepSearch 上达到 82.0%。与基线 MiroThinker-v1.0-30B 相比，SMTL-100 在 BrowseComp 上将平均推理步数减少了 70.7%，同时提升了准确率。在深度研究基准 RACE 上，SMTL-100 整体得分为 45.9%，在四个细项上分别为：全面性 42.1%、洞察深度 45.6%、指令遵循 49.6%、可读性 45.5%，其表现超越了多数同规模开源智能体模型。结果表明，SMTL 在效率和泛化性上均具有优势，其并行证据获取和计划精炼机制使其在长视野任务中能更高效地收敛。

### Q5: 有什么可以进一步探索的点？

本文提出的SMTL框架在效率和泛化性上取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其并行证据获取机制虽然提升了效率，但对工具调用的协调和结果整合提出了更高要求，当前方法可能未充分处理并行调用间的依赖关系或冲突信息。其次，尽管通过统一数据合成管道提升了跨任务泛化能力，但其在更复杂、动态的真实世界研究场景（如涉及多模态信息或实时数据流）中的适应性仍有待验证。未来研究可探索更智能的并行规划策略，例如引入动态优先级机制，根据子任务不确定性和信息增益动态调整并行调用的数量和顺序。此外，可考虑将元学习或课程学习引入训练过程，使智能体能更快适应新领域或新型研究任务。另一个重要方向是降低对大规模合成数据的依赖，探索小样本或自监督学习方法，以提升在资源有限或数据稀缺场景下的实用性。最后，当前评估主要基于静态基准，未来需在更开放、交互式的环境中测试智能体的长期决策稳健性和对错误信息的鲁棒性。

### Q6: 总结一下论文的主要内容

该论文针对现有深度研究智能体在搜索密集型场景中因过度依赖深度推理而导致高计算成本和延迟的问题，提出了“多搜索、少思考”（SMTL）框架，旨在提升长视野智能体搜索的效率和泛化能力。核心贡献在于用并行证据获取替代传统的顺序推理，从而在有限的上下文预算下实现高效的信息管理。为增强跨任务泛化性，论文设计了一个统一的数据合成流程，构建了涵盖确定性问答和开放式研究场景的多样化搜索任务及相应评估指标。方法上，作者通过监督微调和强化学习训练了一个端到端智能体。实验表明，SMTL在BrowseComp、GAIA等多个基准测试中取得了优异性能，甚至达到最先进水平，同时在BrowseComp上将平均推理步骤减少了70.7%，显著提升了效率。主要结论是，通过优化搜索策略而非单纯增加推理深度，可以更高效地实现复杂任务的高精度求解，为智能体设计提供了新的方向。
