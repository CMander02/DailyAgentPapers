---
title: "SAGA: Workflow-Atomic Scheduling for AI Agent Inference on GPU Clusters"
authors:
  - "Dongxin Guo"
  - "Jikun Wu"
  - "Siu Ming Yiu"
date: "2026-05-01"
arxiv_id: "2605.00528"
arxiv_url: "https://arxiv.org/abs/2605.00528"
pdf_url: "https://arxiv.org/pdf/2605.00528v1"
categories:
  - "cs.DC"
  - "cs.AI"
  - "cs.LG"
  - "cs.OS"
tags:
  - "Agent调度"
  - "GPU集群"
  - "KV缓存复用"
  - "工作流感知"
  - "多智能体"
  - "编程级调度"
  - "SAGA"
  - "SWE-bench"
  - "WebArena"
relevance_score: 9.5
---

# SAGA: Workflow-Atomic Scheduling for AI Agent Inference on GPU Clusters

## 原始摘要

AI agents execute tens to hundreds of chained LLM calls per task, yet GPU schedulers treat each call as independent, discarding gigabytes of intermediate state between steps and inflating end-to-end latency by 3-8x. We argue that this request-level abstraction is fundamentally mismatched to compound AI workloads, and propose a shift to program-level scheduling: treating the entire agent workflow (not individual inference calls) as the first-class schedulable unit. We present SAGA, a distributed scheduler that implements this abstraction through three mechanisms: (1) Agent Execution Graphs that capture workflow structure to predict KV cache reuse across tool-call boundaries, achieving within 1.31x of Bélády's optimal offline policy; (2) session-affinity batching with work stealing that co-locates correlated requests while maintaining global load balance; and (3) Agent Fair Share, a task-completion-time fairness metric with provable bounded-deviation guarantees. On a 64-GPU cluster serving SWE-bench coding agents and WebArena browser tasks, SAGA reduces task completion time by 1.64x (geometric mean, p < 0.001) over vLLM v0.15.1 with prefix caching and affinity routing, while improving GPU memory utilization by 1.22x and achieving 99.2% SLO attainment under multi-tenant interference. These latency gains come at a quantified cost: approximately 30% lower peak throughput than throughput-optimal batch scheduling, a tradeoff appropriate for the latency-sensitive interactive deployments that dominate compound AI usage. Our results demonstrate that workflow-aware scheduling is essential for efficient compound AI serving.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有 GPU 集群调度系统在处理 AI Agent 多步骤推理工作负载时存在的根本性效率问题。研究背景是：AI Agent 会执行包含数十到数百个连续 LLM 调用的复杂任务，而当前的推理框架（如 vLLM）将每个调用视为独立请求进行调度，忽略了工作流结构。现有方法的不足体现在三个方面：1）每次工具调用后都会丢弃高达 2-12GB 的 KV cache，导致下一调用必须完全重算，产生3-8倍的端到端延迟膨胀；2）GPU 内存利用率仅 42%，因为缓存分配是碎片化的；3）缺乏对会话内请求亲和性和任务完成时间的公平性保障。这篇文章要解决的核心问题是：如何将整个 Agent 工作流（而非单个推理请求）作为可调度的原子单元，通过感知工作流结构的调度策略，在保证公平性和多租户服务质量的前提下，显著减少 KV cache 重计算开销、提高 GPU 内存利用率，并缩短任务的端到端完成时间。

### Q2: 有哪些相关研究？

相关研究可分为三类：**方法类**、**系统类**和**应用框架类**。**方法类**中，vLLM、SGLang、Orca、TensorRT-LLM 等 LLM 服务系统采用连续批处理和 PagedAttention/RadixAttention 管理 KV 缓存，但将每次推理视为独立请求，LRU 逐出策略忽视工作流结构；SAGA 则提出程序级调度，通过 Agent Execution Graphs 预测跨工具调用的 KV 缓存复用，达到最优离线策略的 1.31x 内。**系统类**中，Llumnix 支持 KV 缓存实时迁移但反应式触发，SOLA 优化单请求延迟而非任务完成时间，DistServe 分离预填充与解码但缺乏工作流感知；SAGA 结合会话亲和批处理与工作窃取实现全局负载均衡，并引入 Agent Fair Share 公平性指标（有界偏差保证）。**应用框架类**中，LangChain、CrewAI、AutoGen 提供高层编排但委托调度给底层系统；KVFlow 提出工作流感知逐出但缺乏分布式调度与公平机制，Continuum 引入缓存 TTL 但无形式化保证。SAGA 是首个联合工作流结构预测、分布式调度与公平性保障的完整系统。

### Q3: 论文如何解决这个问题？

SAGA通过将整个AI Agent工作流（而非单个LLM调用）作为GPU调度的基本单元来解决现有调度器导致的高延迟问题。其核心架构分为三层：第一层为Agent接口层，负责接收来自LangChain、AutoGen等框架的请求，并构建Agent执行图（AEG）。AEG形式化地表示工作流结构，包含节点（LLM推理步骤）、有向边（执行依赖）、转移概率和工具类型映射。对于无法获得框架提示的情况，系统通过模式推理模块从请求序列中推断工作流结构，支持显式、隐式和冷启动三种可观测性层级。第二层为全局调度器，维护集群范围的会话到工作线程映射、负载信息和公平性指标。其核心组件包括：亲和性路由器，基于会话亲和性将相关请求调度到同一工作线程以最大化缓存局部性；工作窃取器，通过队列空闲阈值和负载比阈值实现负载均衡的同时避免震荡；以及Agent公平份额（AFS）引擎，提供以任务完成时间为公平性度量的机制，并具有可证明的有界偏差保证。第三层为工作线程池，每个工作线程运行扩展的vLLM实例，采用工作流感知的LRU（WA-LRU）缓存管理策略。WA-LRU结合归一化的最近使用时间、复用概率和会话大小三个因子进行驱逐决策，利用AEG预测近似Bélády最优离线策略，在工具调用边界间实现KV缓存复用，达到最优策略的1.31倍以内。系统还采用会话亲和批处理和工作窃取的协同机制，在保持缓存局部性的同时实现全局负载均衡。当AFS触发抢占时，迁移任务携带工作流感知的TTL状态，确保目标工作线程的WA-LRU能继续保留迁移的缓存。

### Q4: 论文做了哪些实验？

SAGA 在 64-GPU 集群上，使用 SWE-bench 编码智能体和 WebArena 浏览器任务进行了主实验。实验对比了 b) baseline vLLM v0.15.1（含前缀缓存和亲和性路由）和 SAGA。主要结果：(1) 任务完成时间降低 1.64×（几何平均，p<0.001）；(2) GPU 内存利用率提升 1.22×（从 42% 到 71%）；(3) 多租户干扰下 SLO 达标率达 99.2%。(4) SAGA 的 KV 缓存开销仅比最优离线 Bélády 策略高 1.31×。(5) 代价是峰值吞吐量比最优批处理调度低约 30%，但这个权衡对延迟敏感的交互式部署是可接受的。此外，在 32-GPU 集群的消融实验中，SAGA 将 KV 缓存重建时间从 vLLM 的 38% 降至 8%，端到端延迟从 vLLM 的 6.0×（归一化到纯推理时间）降至 1.5×，而仅加前缀缓存的 vLLM 为 3.5×。实验还展示了工作窃取能在突发请求下保持缓存局部性。所有关键结果均基于 10 次重复实验，标准差小于均值的 5%。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向包括：首先，SAGA在峰值吞吐量上比吞吐量最优的批处理调度低约30%，这是一个关键权衡，未来可探索混合调度策略，在延迟敏感型负载与高吞吐批量任务间动态切换。其次，当前工作流图预测依赖固定的ReAct模式，对于树状思维、并行分支等更复杂的agent拓扑结构，其KV缓存复用预测精度可能下降，可引入在线学习或图神经网络动态建模workflow结构。第三，公平性度量Agent Fair Share基于任务完成时间，但在异构模型、混合精度场景下的偏差界需要扩展。第四，当前系统未考虑GPU间异构性（如不同代际的显存带宽），可结合拓扑感知调度进一步优化缓存迁移开销。最后，与推测执行（如预计算下一邻接步骤）的结合是重要方向——SAGA的确定性调度与推测性预取可在不同置信度场景下互补，形成统一workflow优化框架。

### Q6: 总结一下论文的主要内容

AI Agent在执行多步推理任务时，传统的GPU调度器将每次LLM调用视为独立请求，导致KV缓存被丢弃并需在工具调用后重新生成，造成3-8x的端到端延迟膨胀。论文提出SAGA系统，将整个Agent工作流（而非单个推理请求）作为一阶可调度单元。其核心贡献包括：通过Agent执行图预测工作流结构，实现接近离线最优策略1.31倍的在线KV缓存管理；引入会话亲和批处理与工作窃取机制，在维持全局负载均衡的同时联合调度相关请求；提出Agent公平份额指标，提供任务完成时间公平性的可证明有界偏差保证。在64-GPU集群上运行SWE-bench编码Agent和WebArena浏览器任务，SAGA将任务完成时间降低1.64倍（几何平均），GPU内存利用率提升1.22倍，在多租户干扰下实现99.2%的SLO达标率。实验表明，工作流感知调度对于高效服务复合AI系统至关重要，该工作为AI Agent推理提出了从请求级到程序级调度范式的根本性转变。
