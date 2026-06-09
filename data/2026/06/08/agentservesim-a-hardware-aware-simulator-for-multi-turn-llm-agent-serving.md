---
title: "AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving"
authors:
  - "Rakibul Hasan Rajib"
  - "Mengxin Zheng"
  - "Qian Lou"
date: "2026-06-08"
arxiv_id: "2606.09613"
arxiv_url: "https://arxiv.org/abs/2606.09613"
pdf_url: "https://arxiv.org/pdf/2606.09613v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "多轮LLM Agent服务"
  - "硬件感知模拟器"
  - "KV缓存管理"
  - "工具调度"
  - "服务调度策略"
  - "系统优化"
relevance_score: 9.5
---

# AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving

## 原始摘要

Multi-turn LLM agents interleave model calls with external tool invocations, shifting serving from stateless request processing to stateful program execution. Serving these workloads requires scheduling, KV-cache management, and routing policies that use program-level context, including turn dependencies, tool-induced gaps, and reusable KV state. Evaluating such policies directly on real systems is costly, since each design point may require dedicated accelerator time across arrival rates, model scales, serving-instance counts, and memory hierarchies. Simulation offers a scalable alternative, but existing LLM serving simulators target stateless request-level workloads and therefore omit the core dynamics of agent serving: multi-turn program execution, cross-turn cache locality, and KV-cache residency during tool gaps. We present AGENTSERVESIM, a hardware-aware simulator for multi-turn LLM agent serving. AGENTSERVESIM evaluates serving policies at program granularity through composable modules: a Program Orchestrator preserves program identity and turn order, a Tool Simulator materializes tool-induced gaps, a Session-Aware Router maintains program-to-instance affinity for cache-aware dispatch, and a KV Residency Model tracks policy-defined KV placement across HBM, host DRAM/CXL, and eviction. Across real serving deployments and hardware configurations, AGENTSERVESIM reproduces real-system behavior within 6% error across key performance metrics while running entirely on commodity CPUs. These results show that AGENTSERVESIM enables controlled, repeatable exploration of agent-serving policies without requiring exhaustive deployment on costly accelerators.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多轮LLM智能体服务系统中的性能评估瓶颈问题。研究背景是LLM部署正从单轮无状态查询转向多轮智能体系统，如自动编码助手、函数调用流水线等。这些智能体作为有状态程序运行，将多个LLM调用与外部工具调用交织在一起。现有方法存在明显不足：真实系统评估成本极高，每个设计点都需要在多种负载率、模型规模和服务实例数量下消耗大量加速器时间；而现有的LLM服务模拟器（如Vidur、APEX、LLMServingSim）主要针对无状态请求级工作负载设计，缺乏智能体服务所需的核心抽象，包括程序身份、工具调用间隙以及跨轮KV重用。本文要解决的核心问题是：如何构建一个硬件感知的模拟器，能够准确评估多轮LLM智能体服务中的调度、KV缓存管理和路由策略，同时避免在真实硬件上进行昂贵且耗时的部署。该模拟器需要在程序粒度上捕捉智能体执行的关键动态，包括多轮程序执行、跨轮缓存局部性和工具间隙中的KV驻留状态。

### Q2: 有哪些相关研究？

相关研究可分为三类。第一是**服务系统类**，包括Autellix、Continuum和InferCept，它们分别从调度、KV缓存管理、路由维度提出优化策略，但仅解决局部问题，无法联合评估跨层策略的耦合效应。第二是**仿真器类**，如Vidur、APEX和LLMServingSim，它们虽能建模细粒度硬件特性（如异构加速器、多级内存）和批处理策略，但仅适用于无状态请求级负载，缺乏程序身份、工具调用间隙、跨轮缓存复用等Agent服务核心动态。第三是**工作负载差异**：本文与现有仿真器的根本区别在于将执行单元从独立请求扩展为多轮程序，需模拟工具间隙中的KV驻留决策、程序亲和性路由等新维度。本文提出的AGENTSERVESIM通过程序编排器、工具模拟器、会话感知路由器和KV驻留模型等模块，首次在仿真层面联合建模这些耦合维度，且误差不超过6%。

### Q3: 论文如何解决这个问题？

AGENTSERVESIM通过五个核心模块的协同设计来解决多轮LLM Agent服务中的硬件感知仿真问题。整体框架以程序为执行单元，将调度、路由和KV缓存管理作为可组合的策略接口，在算子图执行和硬件建模之上叠加Agent感知语义。

核心组件包括：1) **Program Orchestrator**：维护每个Agent程序的四事件状态机（New Turn、Turn Complete、Invoke Tool、Tool Complete），通过程序标识和工具标志位强制轮次顺序，确保多轮程序的端到端延迟可以精确测量。2) **Tool Simulator**：支持两种模式——回放模式使用捕获的真实工具调用时间戳保证与真实系统一致，生成模式从按工具类型（如grep、python）条件采样的分布中生成假想持续时间，用于反事实实验。3) **Session-Aware Router**：维护程序到模型服务组的亲和性表，默认将同一程序的连续轮次路由到同一引擎，当主引擎超载时支持等待、迁移（通过系统模拟器计算KV传输代价）或重预填充三种降级策略。4) **Program-Aware Batch Scheduler**：基于程序标识进行队列排序，通过可插拔策略钩子支持程序级FCFS、已获服务优先等顺序决策，并为每轮输出KV处置决策（保留、交换、丢弃）。5) **KV Residency Model**：为每个程序的KV节点设置策略定义的截止时间，跨越HBM、主机DRAM/CXL和淘汰三个层级管理，在工具间隙期间通过截止时间感知的驻留控制器保留KV状态，支持自适应TTL设置和中断感知的交换到主机操作。

创新点在于将Agent程序的轮次依赖、工具间隙和跨轮缓存局部性这些核心动态特征显式建模为可仿真的系统对象，在真实部署和硬件配置下实现了关键指标6%以内的误差。

### Q4: 论文做了哪些实验？

论文在三个NVIDIA GPU平台（RTX 3090 24GB、H100-SXM 80GB、B200 180GB）上，使用SWE-Bench Verified trace作为数据集，以Poisson到达（JPS=0.02-0.1）的50个程序为负载，对四种服务策略进行了实验：vLLM-FCFS（请求级FCFS，回合结束时KV驱逐）、Autellix（程序级达到服务调度）、InferCept（中断感知KV管理）和Continuum（程序级FCFS，成本模型导向KV保留）。实验通过对比真实系统（vLLM）和模拟器AGENTSERVESIM的每程序完成时间（JCT）和瞬时吞吐量来验证模拟器精度。主要结果显示：在80个（配置×策略）单元中，JCT平均相对误差均低于5%（如B200/Llama-3.1-8B下+2.6%至+4.2%，H100/Llama-3.1-8B下-4.5%至-4.8%），瞬时吞吐量误差低于2%。此外，论文进行了硬件感知设计空间探索，包括多实例路由（会话感知路由达到96.26%前缀命中率，优于轮询和最少负载）、前缀复用率η扫描（η≥0.5时策略选择影响显著，如η=0.9时InferCept比Autellix快3.3倍）以及工具延迟缩放（k=1时Continuum降低26.7% JCT）。

### Q5: 有什么可以进一步探索的点？

论文的主要局限在于其对网络和算子性能的简化建模，继承了现有LLM服务仿真器的假设，这可能导致在高通信压力或非典型硬件拓扑下精度下降。未来工作可从三方面展开：一是引入更细粒度的网络争用模型，例如模拟NVLink或跨机通信的突发拥塞，以提升对大规模分布式部署的保真度；二是针对工具调用非确定性，可探索基于LLM的小样本预测方法，动态生成工具调用序列分布，而非仅依赖固定trace回放；三是扩展对MoE架构的支持，其稀疏激活模式会改变KV缓存驻留与路由策略，需重新设计内存层级模型。此外，当前仿真器未考虑agent端自主思维链带来的可变延迟，未来可将agent的思考时间纳为随机变量，实现端到端的负载生成。

### Q6: 总结一下论文的主要内容

这篇论文介绍了一个名为AGENTSERVESIM的硬件感知模拟器，用于解决多轮LLM代理服务中的关键问题。核心问题在于，多轮LLM代理工作负载将无状态请求处理转变为有状态程序执行，包含轮次依赖、工具间隙和可重用KV状态，直接在真实系统上评估调度和缓存策略成本高昂。AGENTSERVESIM通过可组合模块（程序编排器、工具模拟器、会话感知路由器和KV驻留模型）从程序粒度评估服务策略，能保留程序标识和轮次顺序、模拟工具延迟、保持程序到实例的亲和性以及跟踪KV状态在HBM、主机DRAM/CXL和驱逐中的位置。在真实部署和硬件配置上，该模拟器在关键性能指标上的误差控制在6%以内，且无需GPU即可运行。其主要意义在于，它为代理服务策略提供了可控、可重复的探索工具，避免了在昂贵硬件上进行全面部署，从而降低了研究成本并加速了创新。
