---
title: "Scepsy: Serving Agentic Workflows Using Aggregate LLM Pipelines"
authors:
  - "Marcel Wagenländer"
  - "Otto White"
  - "Britannio Jarrett"
  - "Pedro Silvestre"
  - "Yanda Tao"
  - "Guo Li"
  - "Huanzhou Zhu"
  - "Llúis Vilanova"
  - "Peter Pietzuch"
date: "2026-04-16"
arxiv_id: "2604.15186"
arxiv_url: "https://arxiv.org/abs/2604.15186"
pdf_url: "https://arxiv.org/pdf/2604.15186v1"
categories:
  - "cs.DC"
  - "cs.AI"
tags:
  - "Agentic Workflows"
  - "LLM Serving"
  - "System Optimization"
  - "GPU Scheduling"
  - "Latency/Throughput Prediction"
  - "Cluster Management"
  - "Aggregate LLM Pipeline"
relevance_score: 9.0
---

# Scepsy: Serving Agentic Workflows Using Aggregate LLM Pipelines

## 原始摘要

Agentic workflows carry out complex tasks by orchestrating multiple large language models (LLMs) and tools. Serving such workflows at a target throughput with low latency is challenging because they can be defined using arbitrary agentic frameworks and exhibit unpredictable execution times: execution may branch, fan-out, or recur in data-dependent ways. Since LLMs in workflows often outnumber available GPUs, their execution also leads to GPU oversubscription.
  We describe Scepsy, a new agentic serving system that efficiently schedules arbitrary multi-LLM agentic workflows onto a GPU cluster. Scepsy exploits the insight that, while agentic workflows have unpredictable end-to-end latencies, the shares of each LLM's total execution times are comparatively stable across executions. Scepsy decides on GPU allocations based on these aggregate shares: first, it profiles the LLMs under different parallelism degrees. It then uses these statistics to construct an Aggregate LLM Pipeline, which is a lightweight latency/throughput predictor for allocations. To find a GPU allocation that minimizes latency while achieving a target throughput, Scepsy uses the Aggregate LLM Pipeline to explore a search space over fractional GPU shares, tensor parallelism degrees, and replica counts. It uses a hierarchical heuristic to place the best allocation onto the GPU cluster, minimizing fragmentation, while respecting network topology constraints. Our evaluation on realistic agentic workflows shows that Scepsy achieves up to 2.4x higher throughput and 27x lower latency compared to systems that optimize LLMs independently or rely on user-specified allocations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在自管理的GPU集群上高效部署和调度多LLM智能体工作流（agentic workflows）的挑战。随着大语言模型（LLMs）在复杂任务中的应用日益广泛，开发者通过编排多个不同规模的LLMs和外部工具来构建智能体工作流，以提升能力与成本效益。然而，在中小型机构的自托管环境中，高效服务这类工作流面临严峻问题：首先，工作流可以使用任意框架（如LangChain）定义，执行过程因数据依赖的分支、扇出和循环而具有高度不可预测的延迟；其次，工作流中LLM数量常超过可用GPU数，导致GPU资源过度订阅与利用率低下；再者，现有方法存在明显不足——专注于单LLM优化的服务系统无法处理多LLM间的耦合与瓶颈转移，而依赖用户手动分配GPU或仅进行请求级调度的方案（如Kubernetes或某些多路复用系统）则因缺乏对工作流整体结构的感知而导致性能低下。

本文的核心问题是：如何为任意多LLM智能体工作流自动寻找最优的GPU资源分配策略，在满足目标吞吐量的同时最小化延迟，并高效地将分配方案部署到GPU集群上。为此，论文提出了Scepsy系统，其关键洞察是：尽管工作流端到端执行时间变化大，但每个LLM在总执行时间中所占的“份额”在多次执行中相对稳定。基于此，Scepsy通过分析聚合的LLM需求份额，构建了一个轻量级的“聚合LLM管道”模型来预测不同GPU分配下的性能，进而在一个综合考虑了数据并行、张量并行以及分数GPU份额的搜索空间中，联合优化吞吐量与延迟，最后通过拓扑感知的启发式方法将分配方案映射到实际GPU集群上，以最小化资源碎片化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：服务于多LLM的系统，以及专门针对智能体工作流的系统。

**1. 多LLM服务系统**：这类系统将工作流中的每个LLM视为独立服务进行优化，主要分为两种。**自动扩缩容系统**（如基于资源指标或SLO的策略）通过动态调整副本数来满足资源需求，但在处理具有数据依赖的智能体工作流时，容易因级联效应导致GPU分配振荡。**多路复用系统**则通过时空复用技术在固定GPU集上共置多个LLM，但其固定的复用策略无法适应智能体工作流中LLM调用次数和时间的剧烈波动，导致性能下降。这两类系统的共**同局限**在于，它们都忽略了LLM调用间的依赖关系和执行的不确定性，因此无法进行工作流级别的性能优化。

**2. 智能体工作流服务系统**：这类系统利用工作流层面的知识进行优化，也可分为两类。**静态分析系统**（如Parrot、Ayo）通过自定义编程抽象来构建静态数据流图，并应用图感知批处理、流水线等优化。然而，其自定义抽象**限制**了支持的编程模型，无法有效支持如波束搜索这类具有动态控制流的常见工作流。**基于预测的调度系统**（如Autellix、JITServe）将工作流形式化为动态图，利用工作流级统计信息（如累计执行时间、响应长度估计）来预测请求完成时间并进行调度。但它们通常**要求工作流中的所有智能体使用相同的LLM**，且将每个LLM的资源分配决策留给用户，无法自动优化异构LLM的资源配置。

**本文与这些工作的关系和区别**：Scepsy属于第二类（智能体工作流服务系统），但解决了现有系统的关键缺陷。与静态分析系统不同，它不限制编程模型，能支持任意框架编写的动态工作流。与基于预测的调度系统不同，它专门支持**异构多LLM**工作流，并引入了**自动GPU分配**机制。其核心创新在于发现了尽管工作流端到端延迟波动大，但**每个LLM所占执行时间的比例相对稳定**。基于此，Scepsy构建了“聚合LLM流水线”作为轻量级性能预测器，并以此在分式GPU份额、张量并行度和副本数构成的搜索空间中，自动寻找满足目标吞吐量且延迟最优的GPU分配方案，从而实现了工作流级别的联合优化。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为Scepsy的新型智能体工作流服务系统来解决多LLM工作流在目标吞吐量下低延迟服务的挑战。其核心方法是利用“智能体工作流虽然端到端延迟不可预测，但其中每个LLM执行时间占总时间的比例相对稳定”这一关键洞察，构建一个**聚合LLM流水线（Aggregate LLM Pipeline， ALP）**作为轻量级的性能预测器，并基于此进行高效的GPU资源调度与放置。

**整体框架与主要模块**：
系统工作流程分为四个主要步骤：
1.  **工作流剖析与追踪**：以与框架和引擎无关的方式（通过HTTP代理）执行一系列代表性工作流请求，捕获LLM级别的请求/响应内容、时间戳及依赖关系，形成执行轨迹。
2.  **构建聚合LLM流水线（ALP）**：这是系统的核心创新。首先进行**统计工作流聚合**，为每个LLM提取两个关键统计量：每个工作流请求的平均调用次数（\(n_m\)）和平均请求级并行度（\(p_m\)），以此捕捉循环、分支、扇出等动态行为。接着进行**LLM性能剖析**，通过重放所有轨迹中的LLM请求，在不同到达率和张量并行度（TP）下，获取每个LLM的吞吐量-延迟曲线。最后**合成ALP**，将工作流抽象为一个由唯一LLM阶段组成的流水线，并使用公式 \(L_w(\lambda_w) = \sum_{m} L_m(\lambda_w \cdot n_m) \cdot \frac{n_m}{p_m}\) 和 \(T_w = \min_{m} \frac{T_m}{n_m}\) 将LLM级性能指标转换为工作流级指标，从而能够快速预测任意资源分配下的工作流端到端延迟与吞吐量。
3.  **基于ALP的GPU调度**：调度器的目标是在满足目标工作流到达率的前提下，寻找能最小化延迟的GPU资源分配（包括GPU份额、张量并行度、副本数）。它利用ALP进行快速性能预测，并通过分层启发式方法在巨大的搜索空间中进行高效枚举和剪枝：
    *   **GPU份额枚举**：根据从ALP中提取的LLM延迟比例（作为计算需求的代理）对LLM排序，优先为高延迟LLM分配更多GPU份额，并施加基于模型参数和KV缓存的最小份额下限进行剪枝。
    *   **份额打包到GPU**：将计算出的连续GPU份额映射到具体的物理GPU上。
    *   **确定并行配置**：根据每个LLM占用的GPU数量，枚举可行的张量并行度与副本数组合，确保GPU利用率最大化并避免高通信开销。
    *   支持多工作流调度，通过额外层级决定各工作流的GPU分配。
4.  **拓扑感知的分数化放置**：将调度器决定的资源分配方案实际部署到GPU集群。采用**分层放置算法**：首先在节点间放置，优先放置大的张量并行实例以利用NVLink域；然后在节点内放置，将GPU分数打包到已占用的GPU上以最小化碎片。最终通过扩展的Kubernetes设备插件和Nvidia MPS来强制执行分数化GPU资源限制。

**关键技术创新点**：
1.  **聚合LLM流水线（ALP）模型**：创新性地使用稳定的统计量（调用次数、并行度）和LLM剖析数据，将动态、不可预测的工作流转换为一个可预测性能的抽象流水线，使快速、准确的资源分配探索成为可能。
2.  **联合、分数化的GPU资源调度**：不同于独立优化每个LLM，系统联合优化工作流中所有LLM的资源分配。引入**分数化GPU分配**，允许不同大小的LLM共享GPU，细粒度地匹配其差异化的计算需求（如将小嵌入模型与大生成模型共置）。
3.  **分层搜索与剪枝策略**：面对巨大的资源分配搜索空间，设计了基于延迟比例排序、连续性分配、并行度限制等多重剪枝策略，并结合拓扑感知的放置启发式方法，在合理时间内找到近似最优解。
4.  **框架与引擎无关性**：通过通用的请求追踪和性能重放机制，支持任意智能体框架和LLM服务引擎，提升了系统的通用性。

### Q4: 论文做了哪些实验？

论文在评估部分设计了详尽的实验来验证Scepsy系统的性能。实验设置方面，作者在GPU集群上部署了Scepsy，并与多个基线系统进行对比，包括独立优化每个LLM的系统（如Kubernetes默认调度）以及依赖用户指定GPU分配的方法。实验使用了多种具有代表性的智能体工作流作为基准测试，例如RAG（检索增强生成）与重排序器（Reranker）组合的工作流、多智能体辩论（Multi-Agent Debate）以及包含循环或分支的复杂工作流（如带有工具调用的ReAct范式）。这些工作流模拟了实际应用中常见的模式，其执行路径和数据流具有不可预测性。

主要对比方法包括：1）传统的基于Kubernetes的调度，将每个LLM视为独立服务进行资源分配；2）用户手动指定的静态GPU分配策略。实验在4、8、16颗GPU的不同集群规模下进行，以目标吞吐量（如每秒查询数QPS）为约束，评估系统在满足该吞吐量下的端到端延迟（P99延迟）以及所能达到的最大吞吐量。

关键数据指标与结果显示：Scepsy在多数测试场景下显著优于基线。例如，在RAG+重排序器工作流中，相比Kubernetes调度，Scepsy在16 GPU配置下实现了高达2.4倍的吞吐量提升，并将P99延迟降低了27倍。对于多智能体辩论工作流，Scepsy通过其聚合LLM流水线预测和分层启发式放置，在满足目标QPS的同时，将延迟降低了数倍至一个数量级。这些结果证明了Scepsy利用LLM执行时间份额的稳定性进行联合调度和资源分配的有效性，能够最小化延迟、提高吞吐量并减少GPU资源碎片。

### Q5: 有什么可以进一步探索的点？

该论文提出的Scepsy系统在调度和资源分配方面取得了显著进展，但其局限性和未来探索方向仍值得深入。首先，系统依赖于对LLM执行时间份额的稳定性假设，这在动态、高度不确定的复杂工作流中可能不成立，未来可研究更自适应、在线学习的方法来应对执行模式的突变。其次，Scepsy主要优化GPU资源，但未充分考虑内存带宽、跨节点通信开销或异构计算资源（如CPU、专用加速器）的协同调度，扩展支持多资源类型可进一步提升效率。此外，系统假设工作流结构已知，但现实场景中任务可能动态生成或演化，因此探索在线工作流推断与实时重调度机制将是一个重要方向。最后，当前启发式搜索可能陷入局部最优，结合强化学习或贝叶斯优化进行自动化资源调配，有望在更大搜索空间中找到更优解，同时降低调度本身的开销。

### Q6: 总结一下论文的主要内容

该论文提出Scepsy系统，旨在高效调度由多个大语言模型（LLM）和工具组成的智能体工作流到GPU集群上。核心问题是：智能体工作流因执行路径不确定（如分支、扩展或递归）且LLM数量常超过可用GPU数，导致难以在目标吞吐量下实现低延迟服务，并引发GPU资源过度占用。

Scepsy的核心贡献在于利用“尽管工作流端到端延迟不可预测，但其中各LLM执行时间占比相对稳定”这一洞察，设计了基于聚合时间占比的调度方法。系统首先分析不同并行度下LLM的性能数据，构建轻量级的“聚合LLM流水线”模型，用以预测资源分配下的延迟和吞吐量。随后，通过在GPU份额、张量并行度和副本数量的组合空间中搜索，找到满足目标吞吐量且最小化延迟的资源分配方案，并采用分层启发式方法将分配映射到GPU集群，以降低碎片化并满足网络拓扑约束。

实验表明，相较于独立优化LLM或依赖用户指定分配的系统，Scepsy在典型智能体工作流中可实现最高2.4倍的吞吐量提升和27倍的延迟降低，显著提升了复杂多LLM工作流的服务效率与资源利用率。
