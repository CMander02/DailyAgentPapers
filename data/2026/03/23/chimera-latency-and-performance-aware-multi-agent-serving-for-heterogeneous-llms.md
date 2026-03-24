---
title: "Chimera: Latency- and Performance-Aware Multi-agent Serving for Heterogeneous LLMs"
authors:
  - "Kangqi Ni"
  - "Wenyue Hua"
  - "Xiaoxiang Shi"
  - "Jiang Guo"
  - "Shiyu Chang"
  - "Tianlong Chen"
date: "2026-03-23"
arxiv_id: "2603.22206"
arxiv_url: "https://arxiv.org/abs/2603.22206"
pdf_url: "https://arxiv.org/pdf/2603.22206v1"
categories:
  - "cs.LG"
tags:
  - "Multi-Agent Systems"
  - "LLM Serving"
  - "Scheduling"
  - "Heterogeneous Models"
  - "Latency Optimization"
  - "Performance Optimization"
  - "Semantic Routing"
  - "Workflow Execution"
relevance_score: 7.5
---

# Chimera: Latency- and Performance-Aware Multi-agent Serving for Heterogeneous LLMs

## 原始摘要

Multi-agent applications often execute complex tasks as multi-stage workflows, where each stage is an LLM call whose output becomes part of context for subsequent steps. Existing LLM serving systems largely assume homogeneous clusters with identical model replicas. This design overlooks the potential of heterogeneous deployments, where models of different sizes and capabilities enable finer trade-offs between latency and performance. However, heterogeneity introduces new challenges in scheduling across models with diverse throughput and performance. We present Chimera, a predictive scheduling system for multi-agent workflow serving on heterogeneous LLM clusters that jointly improves end-to-end latency and task performance. Chimera applies semantic routing to estimate per-model confidence scores for each request, predicts the total remaining output length of the workflow, and estimates per-model congestion using in-flight predicted token volumes for load balancing. We evaluate Chimera on representative agentic workflows for code generation and math reasoning using multiple heterogeneous LLM configurations. Across comparable settings, Chimera traces the best latency-performance frontier, reducing end-to-end latency by 1.2--2.4$\times$ and improving task performance by 8.0-9.5 percentage points on average over competitive baselines including vLLM.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在异构大语言模型集群上高效服务多智能体工作流时，如何协同优化端到端延迟与任务性能的核心问题。

研究背景是，大语言模型正从独立的聊天机器人演变为通过协作工作流解决复杂任务的多智能体系统。这类系统的一个用户查询会触发一系列依赖性的LLM调用，形成多阶段工作流。同时，为了在成本与性能间取得平衡，实际部署环境正变得越来越异构，即同时提供不同规模（参数量）和能力的多种模型。然而，现有方法存在明显不足：一方面，大多数模型路由方法对系统负载的考虑过于简化或静态，将延迟视为模型的固定属性，而忽略了在突发流量下排队和资源争用所产生的动态影响；另一方面，现有的服务系统和调度器主要针对同构模型集群（每个引擎复制相同模型）进行单请求执行优化，未能解决如何根据请求的不同难度在异构模型间分配容量，以及模型选择本身如何影响队列拥塞的问题。

因此，本文要解决的核心问题是：**如何在负载条件下，对运行在异构LLM集群上的多智能体工作流进行调度，以协同改善可实现的端到端延迟和任务性能**。具体挑战包括：工作流的端到端延迟产生于多个依赖阶段间的排队交互，使得仅针对单个请求的调度效果不佳；模型选择与系统拥塞紧密耦合，将请求路由到更慢但能力更强的模型虽能保证性能，却可能加剧对共享GPU资源的争用，从而损害其他工作流的延迟。论文提出的Chimera系统正是为了应对这些挑战，通过联合考虑语义路由、工作流级输出长度预测和实时负载监控，来实现延迟与性能感知的调度。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：LLM服务系统、输出长度预测和LLM路由。

在**LLM服务系统**方面，相关工作如vLLM、SGLang、Sarathi-serve等通过优化KV缓存、结构化程序执行或批处理来提升吞吐量和延迟。Parrot和Autellix等则在应用层针对跨请求结构或智能体程序进行优化。然而，这些系统均假设部署环境是同质的，即使用相同模型的多个副本。本文提出的Chimera系统则专注于**异构LLM集群**上的多智能体工作流服务，通过在现有服务引擎（如vLLM）之上构建预测性调度器，协同设计路由、队列优化和负载均衡，以同时改善延迟和任务性能，这是与同质化设计工作的核心区别。

在**输出长度预测**方面，先前工作表明预测生成长度可以改进LLM调度和批处理效率，通常将问题建模为请求级别的回归或分类。本文的贡献在于将长度预测**适配到多智能体工作流**中，使用轻量级回归器预测工作流的总输出长度，并将其作为调度优先级信号，结合防饥饿机制来降低端到端延迟。

在**LLM路由**方面，相关研究致力于在多个LLM之间进行选择，以在保持性能的同时降低成本或延迟，方法包括轻量级路由、基于表示的方法等。本文的独特之处在于，路由并非独立组件，而是被**集成到一个更广泛的在线服务循环**中，与工作流感知的优先级调度和实时负载均衡协同设计，共同优化模型选择和队列管理，以服务于多阶段智能体工作负载。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为Chimera的预测性调度系统，来解决异构LLM集群上多智能体工作流服务的延迟与性能联合优化问题。其核心方法是构建一个位于应用与后端推理引擎之间的中间件层，通过四个协同工作的模块进行智能调度。

整体框架包含四个主要模块：1) **语义路由器**：一个基于Transformer的编码器，为每个LLM请求输出针对每个候选模型的置信度分数，预测哪个模型最有可能获得高性能。它使用ModernBert-large进行微调，通过多标签头产生独立分数，并以二进制交叉熵进行训练。2) **长度预测器**：使用分位数随机森林回归模型，在线预测整个工作流剩余的总输出令牌长度。其特征包括令牌计数、工作流状态、模型名称以及通过TF-IDF和SVD降维得到的文本草图。预测的长度用作调度优先级，近似最短总作业优先策略。3) **活动监视器**：维护一个程序表，跟踪每个请求的元数据、执行状态以及分配给每个引擎的预测令牌量，从而估计每个模型当前的负载（即“在途工作量”）。4) **负载均衡器**：作为调度器，整合语义路由器的置信度分数和活动监视器提供的各引擎负载估计，以选择目标模型并分派请求。

其调度算法的创新点在于**延迟与性能感知的联合路由决策**。对于新工作流请求，系统首先通过语义路由器获得各模型置信度分数，同时基于预测的在途令牌量估算各模型的延迟。负载均衡器会识别出最快模型，然后选择满足以下条件的最高置信度模型：其估计延迟不超过最快模型延迟的一个可配置松弛范围，并且置信度提升超过一个最小阈值。这种设计实现了在负载下的单调回退行为：当大模型拥堵时，流量会转向负载较轻的模型。此外，系统通过**重用已有分配**来保持执行局部性和减少开销，并为请求分配基于预测总长度的优先级。为了防止长请求被无限期饿死，系统还引入了基于**老化机制的优先级提升**策略。

关键技术还包括**低开销的异步批处理服务**：语义路由器和长度预测器作为异步批处理服务运行，避免阻塞调度主循环，从而保持低单请求开销。整个系统构建在vLLM之上，保持了API兼容性。通过这种架构，Chimera能够动态权衡延迟与性能，在异构模型集群上为多智能体工作流绘制出更优的延迟-性能边界。

### Q4: 论文做了哪些实验？

实验在异构LLM集群上评估Chimera系统，聚焦于代码生成和数学推理两类代表性智能体工作流。实验设置基于ReAct构建多阶段工作流，每个查询需1到4个阶段完成，模拟真实多智能体服务场景。使用的数据集/基准测试包括：APPS（代码生成基准，评估生成可通过隐藏测试的Python解决方案）和MATH（数学推理基准，评估最终答案的精确匹配）。模型采用不同规模的Qwen2.5（1.5B/3B/7B/14B）、Ministral3-8B和Llama3.2-3B，部署在NVIDIA RTX A6000 GPU上，并测试了多种异构模型组合配置（如Qwen1.5B+7B、Qwen1.5B+14B等）。对比方法包括vLLM（高性能LLM服务后端）、MLFQ（扩展vLLM的多优先级队列）和LTR（基于长度预测的SJF策略），同时以vLLM(STJF)（使用真实工作流总输出长度优先级的参考方法）作为潜在最优延迟基准。

主要结果方面，Chimera在所有设置中均实现了最佳的延迟-性能权衡，即同时获得最低的端到端（E2E）每令牌延迟和最高的任务性能得分。关键数据指标：在APPS上，对于Qwen1.5B+7B配置，Chimera相比vLLM实现了3.4倍加速和16.0个百分点（pp）的性能提升（测试通过率）；对于Qwen1.5B+14B，实现了2.9倍加速和10.5 pp提升。在MATH上，对于Qwen1.5B+7B，实现了2.5倍加速和2.2 pp提升（精确匹配率）。此外，调度开销极低，在APPS上仅占E2E延迟的0.7%–2.2%，在MATH上占0.2%–0.4%。消融实验表明，语义路由器和长度预测器是关键组件，移除路由器会导致性能下降；与Oracle（使用真实长度或成功结果）对比显示，Chimera在多数情况下已接近理论上限。

### Q5: 有什么可以进一步探索的点？

该论文主要聚焦于异构集群中多智能体工作流的调度优化，但在实际部署和更复杂场景下仍有进一步探索空间。其局限性在于：1）实验主要基于代码生成和数学推理两类工作流，未涵盖更广泛的智能体交互模式（如动态分支、循环依赖）；2）系统假设模型性能可通过置信度分数静态评估，未考虑输入分布漂移或模型协同效应；3）负载均衡依赖预测令牌量，可能低估突发流量或长尾请求的影响。

未来研究方向可包括：1）扩展至动态工作流拓扑，支持实时路径调整与容错机制；2）引入在线学习机制，根据历史反馈动态更新路由策略，适应模型性能变化；3）结合硬件感知调度，在异构GPU集群中统筹内存、显存与计算资源；4）探索多目标优化框架，在延迟、性能之外纳入成本或能耗指标。此外，可研究联邦学习场景下的跨集群调度，以应对数据隐私与模型异构的双重挑战。

### Q6: 总结一下论文的主要内容

该论文针对异构大语言模型集群上多智能体工作流服务中的调度问题，提出了一种名为Chimera的预测性调度系统。核心问题是：在负载下，如何通过联合优化模型选择和请求调度，以在端到端延迟和任务性能之间取得更优权衡。

论文的主要贡献在于：首先，形式化了异构多智能体服务的在线调度问题，并定义了在负载下可实现的（延迟，性能）操作点。其次，提出了一种耦合模型路由与工作流级长度预测的调度方法。Chimera整合了三个关键组件：基于Transformer的语义路由器（用于估计每个请求对每个模型的置信度分数）、轻量级回归器（用于预测工作流剩余总输出长度）以及活动监视器（通过跟踪各引擎的预测令牌量来估计负载引起的延迟）。最后，设计了一种延迟与性能感知的调度规则，该规则在最快模型的可配置延迟松弛范围内选择置信度最高的模型，并采用结合老化机制的最短总任务优先策略进行队列优先级排序。

实验表明，在代码生成和数学推理等代表性智能体工作流上，Chimera相较于vLLM等基线方法，能描绘出最佳的延迟-性能边界，平均将端到端延迟降低1.2-2.4倍，并将任务性能平均提升8.0-9.5个百分点。其意义在于首次系统性地解决了异构LLM集群上多阶段工作流服务的联合优化挑战。
