---
title: "Scalable Inference Architectures for Compound AI Systems: A Production Deployment Study"
authors:
  - "Srikanta Prasad S"
  - "Utkarsh Arora"
date: "2026-04-28"
arxiv_id: "2604.25724"
arxiv_url: "https://arxiv.org/abs/2604.25724"
pdf_url: "https://arxiv.org/pdf/2604.25724v1"
categories:
  - "cs.AI"
tags:
  - "Compound AI Systems"
  - "Production Deployment"
  - "Inference Architecture"
  - "Multi-Agent Workloads"
  - "Serverless Execution"
  - "Autoscaling"
  - "Enterprise Agent"
relevance_score: 8.5
---

# Scalable Inference Architectures for Compound AI Systems: A Production Deployment Study

## 原始摘要

Modern enterprise AI applications increasingly rely on compound AI systems - architectures that compose multiple models, retrievers, and tools to accomplish complex tasks. Deploying such systems in production demands inference infrastructure that can efficiently serve concurrent, heterogeneous model invocations while maintaining cost-effectiveness and low latency. This paper presents a production deployment study of a modular, platform-agnostic inference architecture developed at Salesforce to support compound AI use cases including Agentforce (autonomous AI agents) and ApexGuru (AI-powered code analysis). The system integrates serverless execution, dynamic autoscaling, and MLOps pipelines to deliver consistent low-latency inference across multi-component agent workflows. We report production results demonstrating over 50% reduction in tail latency (P95), up to 3.9x throughput improvement, and 30 to 40% cost savings compared to prior static deployments. We further present a novel analysis of compound-system-specific challenges including multi-model fan-out overhead, cascading cold-start propagation, and heterogeneous scaling dynamics that emerge uniquely when serving agentic workloads. Through detailed case studies and operational lessons, we illustrate how the architecture enables compound AI systems to scale model invocations in parallel, handle bursty multi-agent workloads, and support rapid model iteration - capabilities essential for operationalizing agentic AI at enterprise scale.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决企业级复合AI系统在生产部署中面临的推理基础设施挑战。随着AI从单一模型向复合系统演进（如Salesforce的Agentforce和ApexGuru），这类系统需要同时编排多个模型、检索器和工具，产生异构、并发的模型调用。现有基于静态GPU基础设施的部署方式存在四个关键不足：固定成本无法随流量动态调整，各模型组件无法独立扩缩容；多模型类型竞争同一GPU资源导致争用；单个组件冷启动会引发级联延迟，拖累整个Agent响应；部署流水线无法支持复合系统所需的快速模型迭代。因此，该论文的核心问题是：如何设计一种可扩展、平台无关的推理架构，以高效服务复合AI系统中并发、异构的模型调用，同时保持低延迟、高吞吐和成本效益。研究通过无服务器执行、动态自动缩放和MLOps流水线等机制，实现了相比静态部署尾延迟降低50%以上、吞吐量提升3.9倍、成本节约30-40%的效果，并系统分析了多模型扇出开销、级联冷启动传播和异构缩放动力学等复合系统特有的挑战。

### Q2: 有哪些相关研究？

相关研究主要分为以下几个类别：  
**方法类**：Zaharia等人提出了从单体模型向复合AI系统的转变，强调通过组合多个模型、检索器和工具提升性能；DSPy等框架为复合AI流水线提供了编程范式；vLLM（PagedAttention）和DJL Serving专注于推理优化，分别提升LLM内存管理和多框架批调度效率；Nvidia NIM将优化模型运行时打包为容器。  
**平台与基础设施类**：Amazon SageMaker提供基于专用实例的托管服务，但存在闲置成本且难以应对异构、突发的多智能体调用模式；Amazon Bedrock Custom Model Import引入类Lambda的无服务器推理模式，仅按用量收费；Salesforce的方案在供应商中立基础上针对复合工作负载进行了适配。  
**系统编排类**：ALTO优化流水线阶段间的网络通信，SGLang聚焦结构化生成。  
**本文与上述工作的区别**：现有研究主要关注模型训练扩展、编程框架或单模型推理优化，而本文首次系统性地探索复合AI系统在生产环境中的推理基础设施挑战，重点解决多模型扇出开销、级联冷启动传播和异构扩缩容等实际问题，并通过Salesforce的Agentforce和ApexGuru案例验证了在尾延迟（P95降低50%+）、吞吐量（提升3.9倍）和成本（降低30-40%）上的显著优势。

### Q3: 论文如何解决这个问题？

该论文通过设计一个模块化、平台无关的可扩展推理架构来应对复合AI系统的生产部署挑战。其核心架构采用分层设计：上层为编排层（Atlas推理引擎），基于事件驱动和发布-订阅模式实现多模型协同的认知工作流，将用户请求分解为并行执行的检索、规划、代码执行等功能节点；下层为推理服务层（Prediction Service），作为统一推理网关抽象底层模型基础设施，支持服务器无状态函数和持久化代理微服务两种部署模式。

关键技术包括：1) 动态缩放策略，通过独立跟踪每个模型的调用率而非聚合请求数，解决扇出放大问题（单个请求可能产生3-5个模型调用）；2) 请求优先级队列，根据模型延迟特征（如50ms的嵌入模型vs3-5秒的对话LLM）进行差异化调度；3) 级联冷启动管理，采用协调预预热（预热模型A时同步预热依赖链B和C）、分层预置并发（仅对关键路径模型预置资源）和基于流量信号的可预测预热策略；4) 动态路由机制，在专用实例和服务器后端之间自动溢出，确保延迟SLA。

创新点体现在：实现了复合AI系统特有的多模型缩放动力学；通过组件级A/B测试（可独立替换管道中的单个模型）将实验周期从周级缩短到小时级；采用电路 breaker 机制实现故障隔离，允许系统在单个模型失败时优雅降级。该架构在生产中实现了P95尾延迟降低50%、吞吐量提升3.9倍、成本降低30-40%的效果。

### Q4: 论文做了哪些实验？

论文在五个维度上评估了推理系统：单模型延迟/吞吐量、成本效率、复合系统开销、复合工作负载下的可靠性和下游质量影响。所有实验均使用生产工作负载和模型。部署规模涉及超过8000个企业用户，日均约722,000次LLM推理，峰值达140万次请求，跨21个全球生产推理区域，峰值容量为2250 RPS（135,000 RPM），2026年3月处理了1360亿个token。

对比方法包括静态端点部署和统一扩展的基线系统。主要结果：单模型方面，采用13B参数的ApexGuru模型，在低并发下P95延迟从约13-15秒降至约7-8秒（降低约45%），高并发下从约37秒降至约10-11秒（降低>50%），吞吐量从50-60 RPM提升至超过200 RPM（约3.9倍）。三个复合AI用例（Agentforce FAQ、ApexGuru Code、Atlas Reasoning Engine Tool Call）显示，P95延迟降低52.3%-57.4%，TPS提升2.5-3.2倍，成本降低4.8-6.1倍。在复合系统开销方面，多模型扇出开销平均为45-80毫秒，占总响应时间的<2%。通过协调预热，复合冷启动延迟从约180秒降至约65秒（降低65%）。在10倍流量突发下，非均匀扩展模型（如SQL执行器仅2-3倍扩展）避免了3-5倍的过度配置。采用按需付费后，ApexGuru成本降低了30-40%，且P95延迟保持在稳态的1.5倍以内。在合成高方差流量下，自动扩展系统在98%的时间内维持P95延迟在稳态的2倍以内，协调预热后将P95违规率降至<0.5%。下游质量方面，Atlas Reasoning Engine实现了2倍的响应相关性和33%的任务成功率提升；ApexGuru的P95分析延迟降至8秒以内。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要在于其架构优化高度依赖GPU池化与serverless混合部署的成熟云环境，对边缘计算或资源受限场景的适配性未作探讨。未来可探索的方向：一是针对复合系统中多模型级联冷启动的“乘法效应”，设计基于请求依赖图的预测性预加载策略，结合因果分析提前并行唤醒模型实例；二是开发跨模型流水线的“联合弹性伸缩”算法，解决对话LLM（高QPS）与工具模型（稀疏调用）在混合路由时的异步扩缩容冲突；三是将文中的Pipeline级可观测性扩展为端到端因果追踪，利用链路数据自动诊断哪一节点导致Agent级SLA违例。此外，可尝试将“渐进式降级”机制与强化学习结合，使系统在部分模型故障时自主选择最优替代路径。

### Q6: 总结一下论文的主要内容

这篇论文介绍了Salesforce为支持复合AI系统（如Agentforce和ApexGuru）而开发的一种模块化、平台无关的可扩展推理架构。生产部署结果显示，与之前的静态部署相比，该架构将尾延迟（P95）降低了50%以上，吞吐量提升了最多3.9倍，同时成本降低了30%至40%。论文还定量分析了复合系统特有的推理挑战，包括多模型扇出开销、级联冷启动传播和异构扩展动力学，并总结了12个月的生产运营教训。这些发现表明，复合AI系统需要根据实际调用模式独立扩展模型组件，而非聚合请求数，同时需要协调冷启动缓解、流水线级可观测性和组件级A/B测试。这项工作的意义在于为大规模部署企业级复合AI系统提供了实践指导，推动了从单一模型到多组件协同推理的基础设施演进。
