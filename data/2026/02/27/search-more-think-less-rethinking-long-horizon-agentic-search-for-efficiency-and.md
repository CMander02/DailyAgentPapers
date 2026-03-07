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
pdf_url: "https://arxiv.org/pdf/2602.22675v2"
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

这篇论文旨在解决深度研究智能体在长视野搜索任务中面临的效率与泛化性双重挑战。当前，基于大语言模型的智能体主要通过增加推理深度和工具调用次数来提升任务性能，但这导致了高昂的推理成本和延迟，尤其在搜索密集型场景中。现有方法通常依赖线性的、顺序的推理过程，这成为其扩展性的主要瓶颈。同时，现有研究任务主要分为两类：一类是具有明确标准答案的确定性问答任务（如BrowseComp、GAIA），另一类是开放式研究问题（如DeepResearch Bench），两者的优化目标和评估标准差异巨大。这导致针对单一任务类型训练的智能体难以泛化到另一类型，缺乏一个能在异构研究场景中均表现优异的统一智能体。

针对上述不足，本文的核心问题是：如何设计一个既能高效执行长视野推理，又能良好泛化到不同类型搜索任务的智能体框架？为此，论文提出了“多搜索，少思考”框架。该框架的核心创新在于，用并行的任务分解与证据获取机制取代传统的顺序推理，并结合结构化的上下文管理，以在有限的上下文预算下实现高效的长视野推理。此外，为了提升泛化能力，论文设计了一个统一的数据合成流程，能够自动构建涵盖确定性和开放式场景的多样化搜索任务，并配以相应的评估指标，从而训练出更具普适性的智能体。最终，通过监督微调和强化学习的端到端训练，该方法在多个基准测试上取得了优异性能，同时大幅提升了推理效率。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为**智能体框架与系统**和**合成数据管道**两大类。

在**智能体框架与系统**方面，主流研究通过外部编排器增强大语言模型，使其具备规划、多步工具使用和环境交互能力，以处理搜索密集型任务。相关工作包括采用控制器分解查询、调度工具的商用深度研究系统，以及如WebWeaver、OAgents等采用规划-研究/执行流程的结构化框架。开源生态也提供了可复用的编排模板。然而，这些工作普遍通过加深**顺序推理**和延长交互步骤来提升性能，导致计算资源大量消耗在模型推理而非有效的外部证据获取上，信息效率有限。本文提出的SMTL框架则**摒弃了顺序推理**，转向**并行证据获取**，旨在以有限的上下文预算实现更高效的上下文管理和更低的推理开销。

在**合成数据管道**方面，高质量训练数据对搜索智能体至关重要。现有方法主要包括基于知识图谱的生成（如WebSailor）和遵循由易到难扩展范式的生成（如WebShaper、ASearcher）。这些工作证明了工具在环生成的有效性，但主要关注增加任务难度或上下文长度，而非显式塑造信息高效的搜索与验证行为。此外，现有管道主要围绕**确定性问答**或结构严格的任务设计，对需要灵活信息聚合和跨源验证的**开放式研究任务**支持有限。相比之下，本文引入的统一数据合成管道，能够构建涵盖上述两类场景的搜索任务，并配以相应的评估指标，从而更好地支持智能体在不同任务类型间的**泛化**。

### Q3: 论文如何解决这个问题？

论文通过提出“Search More, Think Less”（SMTL）框架来解决长视野智能体搜索中的效率与泛化问题。其核心方法是用并行证据获取取代传统的顺序推理，从而在有限的上下文预算下实现高效的信息管理。

整体框架是一个并行的智能体工作流，主要包含三个关键模块：初始计划构建、并行执行与工具协调，以及动态计划精炼。首先，给定一个复合搜索任务，智能体通过问题分解生成一个初始任务计划图（\( G_{plan}^{0} \)），将任务拆分为一系列相互关联但部分独立的子任务（如检索事实、验证关系）。这个计划在设计上就暴露了可并行执行的路径，为后续的并发操作奠定基础。

在并行执行阶段，系统从待处理子任务集合（\( \mathcal{P}_t \)）中选择多个“准备就绪”的子任务，利用外部工具（如网络搜索、页面爬取）同时执行它们。这些并行执行的动作和观察结果被聚合到一个统一的推理状态（\( s_{t+1} \)）中，从而加速任务完成并减少顺序瓶颈。

为了确保计划能适应执行过程，系统会周期性地进行动态计划精炼。基于当前的执行状态、已完成和待处理的子任务，对任务计划图进行更新（\( G_{plan}^{t+\Delta} = \mathcal{R}(...) \)），例如移除已完成任务、检查未解决的依赖关系或引入新的子任务。这种动态调整确保了任务能灵活应对进展，维持高效率。

该方法的创新点在于：1）**并行化工作流设计**：显式支持子任务的并发执行与结构化协调，显著减少了推理步骤（如在BrowseComp基准上比Mirothinker-v1.0平均减少70.7%），提升了效率。2）**统一的训练与评估**：论文还引入了一个统一的数据合成流程，构建了涵盖确定性问答和开放式研究场景的多样化搜索任务，并配以相应的评估指标，这增强了智能体在不同任务类型间的泛化能力。最终，通过监督微调和强化学习进行端到端训练，SMTL在多个基准测试上取得了优异性能。

### Q4: 论文做了哪些实验？

论文在实验部分进行了全面的评估。实验设置方面，作者以Qwen3-30B-A3B-Instruct-2507为骨干模型，采用监督微调（SFT）和强化学习（RL）两阶段训练。SFT阶段训练3.5个epoch，RL阶段学习率为1e-6。推理时使用vLLM，上下文窗口为128K token，并引入了基于计划精炼的上下文管理机制（默认每5步精炼一次，并在上下文达到预算时触发强制压缩），以支持长轨迹任务。实验评估了两种交互步数上限的配置：SMTL-100（100步）和SMTL-300（300步）。

使用的数据集和基准测试涵盖深度搜索和深度研究两大场景。深度搜索基准包括BrowseComp、GAIA、XBench-DeepSearch、WebWalkerQA、FRAMES和SEAL-0。深度研究评估则使用Deep Research Bench RACE，该基准从全面性、洞察深度、指令遵循和可读性四个细粒度标准评估长篇研究报告。

对比方法分为三类：1）具备工具使用能力的基础模型（如Claude-4.5-Sonnet、GPT-5、GLM-4.5等）；2）深度研究系统（如OpenAI DeepResearch、Gemini DeepResearch、Perplexity Deep Research等）；3）开源智能体模型（如WebSailor-32B、MiroThinker-v1.0-30B等）。评估指标方面，深度搜索任务采用pass@1，深度研究任务采用LLM作为评判者进行多维度打分。

主要结果显示，SMTL在多个基准上取得了优异性能。在深度搜索任务中，SMTL-100在BrowseComp上达到43.6%，优于同规模开源模型；SMTL-300性能进一步提升，在BrowseComp上达到48.6%，在GAIA上达到75.7%，在XBench-DeepSearch上达到82.0%。与基线MiroThinker-v1.0相比，SMTL-100在BrowseComp上将平均推理步数减少了70.7%，同时提高了准确率。在深度研究基准RACE上，SMTL-100总体得分为45.9%，在四个细维度上也表现均衡且领先于多数开源基线。这些结果表明SMTL在效率和泛化性方面具有显著优势。

### Q5: 有什么可以进一步探索的点？

基于论文分析，SMTL框架在效率和泛化性上取得了进展，但仍存在局限性和可进一步探索的方向。首先，其并行证据获取机制虽提升了信息密度，但对工具调用的协调和结果整合依赖较强，在更复杂、动态的真实环境中（如信息源冲突或工具故障时）的鲁棒性有待验证。其次，框架在“失败案例倾向于耗尽所有交互步骤”这一现象表明，当前机制在遇到困难时缺乏有效的早期终止或求助策略，可能导致资源浪费；未来可探索自适应预算分配或引入不确定性评估来动态调整搜索深度。此外，实验显示检索宽度（top-k）显著影响性能，但扩大检索范围会增加计算开销，如何在有限上下文窗口内更智能地筛选和压缩检索结果是一个关键问题。最后，论文的统一数据合成管道覆盖了确定性和开放式任务，但现实中的研究任务往往更具领域特异性和演化性；未来可探索如何使智能体在少量示例或自我博弈中持续学习新任务模式，并进一步将效率优势扩展到多模态、具身交互等更广泛的智能体场景中。

### Q6: 总结一下论文的主要内容

该论文针对现有深度研究智能体在搜索密集型场景中因过度依赖深度推理而导致的高推理成本和延迟问题，以及跨异构研究环境泛化能力不足的挑战，提出了“Search More, Think Less”框架。其核心贡献在于通过并行证据获取取代顺序推理，在有限的上下文预算下实现高效的情境管理，从而显著提升效率。为了增强跨任务泛化能力，论文设计了一个统一的数据合成流程，构建了涵盖确定性问答和开放式研究场景的多样化搜索任务及相应评估指标。方法上，作者采用监督微调和强化学习训练了一个端到端的智能体。实验结果表明，该智能体在BrowseComp、GAIA等多个基准测试中取得了优异性能，同时在BrowseComp上将平均推理步骤减少了70.7%，实现了效率与精度的双重提升。
