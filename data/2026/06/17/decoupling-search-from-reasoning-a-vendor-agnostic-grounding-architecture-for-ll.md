---
title: "Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architecture for LLM Agents"
authors:
  - "Emmanuel Aboah Boateng"
  - "Kyle MacDonald"
  - "Amardeep Kumar"
  - "Siddharth Kodwani"
  - "Sudeep Das"
date: "2026-06-17"
arxiv_id: "2606.18947"
arxiv_url: "https://arxiv.org/abs/2606.18947"
pdf_url: "https://arxiv.org/pdf/2606.18947v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.IR"
  - "cs.MA"
tags:
  - "Agent Grounding"
  - "Search Integration"
  - "LLM Agent Architecture"
  - "Production Agent"
  - "Cost Optimization"
  - "Multi-Agent Systems"
  - "Caching"
  - "Model-Agnostic"
relevance_score: 8.5
---

# Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architecture for LLM Agents

## 原始摘要

Production LLM agents increasingly depend on real-time search, yet native search grounding bundles retrieval policy, provider choice, evidence injection, cost, latency, and generation behavior behind a single model-provider boundary. This coupling makes grounding hard to inspect, tune, reuse, or port, and can trigger Search-Induced Verbosity that breaks strict output contracts. We present Decoupled Search Grounding (DSG), a vendor-agnostic boundary that moves grounding outside the reasoning model through an MCP-compatible gateway, exposing provider routing, source-aware context rendering, configured fallback, retrieval-depth control, and exact plus semantic caching as first-class controls. Across five frontier models on SimpleQA, FreshQA, and HotpotQA, native search leads on recency-sensitive FreshQA, but DSG exposes a stronger frontier when control matters: on SimpleQA it nearly matches native accuracy (86.1% vs. 87.7%) at 91% lower search cost, preserves concise answer contracts, and reaches a 99.4% warm-cache hit rate with 68% lower latency. Deployed as a shared production grounding layer for large-scale agentic workloads with interchangeable models, DSG matches or slightly exceeds native-search accuracy on an e-commerce query-understanding (QIU) workload while cutting search cost by over 98%. Real-time grounding is best treated as an optimizable interface boundary, not a fixed model feature.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）在Agent任务中利用实时搜索进行“搜索接地”（search grounding）时，因原生搜索集成方式带来的系统耦合问题。研究背景是，生产环境中的LLM Agent日益依赖实时搜索来获取新鲜证据，但当前主流的原生搜索接地将检索策略、供应商选择、证据注入、成本、延迟以及生成行为全部捆绑在单个模型-供应商的边界内。这种耦合带来的不足包括：导致模型与搜索供应商锁定、操作不透明（如成本和延迟）、难以进行调优和复用，并引入了一种被称为“搜索诱导冗余”（Search-Induced Verbosity）的新故障模式，即模型即使收到严格的简洁输出指令（例如“仅输出最终答案实体”），也会因原生搜索的介入而输出解释性段落，从而破坏下游严格的输出合约（如JSON解析）。本文要解决的核心问题是：如何设计一种供应商无关的、可解耦的搜索接地架构，将检索过程从推理模型中分离出来，使供应商选择、缓存、上下文渲染、成本控制和输出行为成为显式、可控的一阶系统决策，从而提升接地过程的可用性、可迁移性和鲁棒性。

### Q2: 有哪些相关研究？

本文的相关研究主要分为方法类和应用类。在方法类方面，Toolformer、ReAct、API-Bank、ToolLLM、WebGPT等研究确立了LLM使用外部工具和API的能力，但本文关注的是搜索接口在模型栈中的生产级位置而非能力本身。RAG相关研究（如FLARE、RARR、Self-RAG、Adaptive-RAG、IRCoT）聚焦于事实性提升与动态检索，本文的DSG则通过固定推理接口并保持模型可互换性与之互补。在评测类方面，本文采用了SimpleQA、HotpotQA、FreshQA等评测基准，与Dynabench等动态评估方法一致，并使用LLM-as-judge、G-Eval、RAGAs等评估方法。在应用类方面，工业界的多类别电商意图理解、企业支持、动态向量存储等研究探讨了部署中的检索权衡，而本文独特贡献在于将实时搜索接地本身作为可控的、供应商无关的接口，衡量其与专有原生搜索在成本、延迟、缓存和输出契约方面的权衡。与这些工作不同，本文不研究模型能力或检索策略本身，而是解耦搜索与推理，通过MCP兼容网关暴露供应商路由、源感知上下文渲染等控制，并进行跨模型和生产工作负载的系统性评估。

### Q3: 论文如何解决这个问题？

论文提出了一种名为解耦搜索基础（Decoupled Search Grounding, DSG）的架构，通过将搜索功能与推理模型解耦来解决原生搜索耦合带来的问题。核心方法是在应用和推理模型之间引入一个与MCP兼容的网关，作为独立的搜索基础层。该网关充当基础控制平面，将检索策略、提供商选择、成本、延迟和生成行为从模型内部剥离，成为可配置的一等控制项。

整体框架由三个主要模块构成：**MCP兼容网关**、**提供商注册表（Provider Registry）**和**搜索智能层（Search Intelligence Layer）**。网关负责拦截模型发出的搜索工具调用，将查询转发到后端的搜索提供商，并标准化返回的结构化结果，包括证据来源URL，为模型提供明确的出处线索。提供商注册表将不同搜索服务（如Serper、BrightData、Firecrawl、Exa）标准化，通过YAML适配器或专用适配器实现即插即用，并支持配置回滚链，以应对单个提供商故障。搜索智能层是核心创新点，引入了一种分层决策策略：先进行精确缓存查找，若命中则直接返回；其次进行语义缓存重用，通过计算查询嵌入与缓存项的余弦相似度，当相似度超过阈值时复用兼容证据；最后对于全新查询，才执行配置的提供商回滚链执行实时搜索。缓存层针对不同提供商进行隔离，并设置基于领域的时间衰减，在保持高缓存命中率的同时保证结果的时效性。

关键创新在于将搜索本身变成了一个可度量、可调优的接口边界。这包括将搜索策略、检索深度、提供商选择和回放策略从代码硬编码转变为配置，并提供结构化遥测数据（如提供商、延迟、成本）用于归因和监控。由此，系统能以更低成本、更低延迟和更一致的输出契约达到甚至超越原生搜索的准确性，实现了搜索基础的可复用于不同模型和应用。

### Q4: 论文做了哪些实验？

论文在SimpleQA、FreshQA、HotpotQA三个公开基准以及一个电商查询理解（QIU）生产级数据集上进行了实验。静态事实性采用SimpleQA，时效敏感性采用FreshQA，多跳推理采用HotpotQA，QIU包含零售（N=7,988）和长尾合成（N=2,335）两类。对比方法包括无搜索、原生搜索、DSG+BrightData和DSG+Serper，覆盖五个前沿模型（QIU仅用Gemini Flash）。主要结果：在SimpleQA上，五个模型平均原生搜索准确率87.7%（成本$20.00/1K查询），DSG+BrightData达到86.1%（成本$1.80），几乎持平但成本降低91%；DSG+Serper达83.3%（成本$0.67）。FreshQA上原生搜索领先（72.6%），DSG较低（68.0%），体现时效敏感性差异。QIU零售任务中DSG+Serper达93.90%准确率（$0.110/1K查询），超越原生搜索93.40%（$7.90），成本降低超98%；长尾任务中DSG+Serper达87.79%（$0.146），同样超越原生搜索87.62%（$10.37）。缓存实验显示，DSG热缓存命中率达99.4%，延迟从4,570ms降至1,465ms，几乎消除边际搜索成本。结果表明DSG在控制成本、延迟和输出契约的同时，能匹配或超越原生搜索准确率。

### Q5: 有什么可以进一步探索的点？

DSG在解耦搜索与推理方面取得了显著进展，但其局限性指明了几个关键探索方向。首先，当前架构对第三方搜索API的强依赖是一个脆弱点，未来可研究自适应路由策略，根据任务复杂度、预算和延迟要求，动态选择或轮换供应商，甚至在自有索引与外部API间切换，以构建更鲁棒的资源层。其次，论文指出DSG在HotpotQA等复杂多跳推理任务上增益有限，这暗示单纯解耦检索与推理不足以解决深层推理，应探索迭代式检索与推理的闭环，例如让智能体在推理过程中动态决定何时调用搜索、如何整合多源证据，并结合规划或反思机制。此外，搜索诱导的冗长问题虽被识别，但缺乏系统性度量，未来可设计合同感知的验证器，在边界处强制输出格式，并利用用户反馈学习风险模式。最后，评估方法上，LLM评判存在偏见，未来可引入强化学习或人类反馈闭环，让系统从实际使用中自动调整检索深度、缓存策略和提示模板，实现持续优化。

### Q6: 总结一下论文的主要内容

这篇论文提出了解耦搜索接地（DSG）架构，用于解决生产环境中LLM智能体将搜索与推理耦合带来的问题。该耦合导致搜索策略、提供商选择、成本、延迟和输出行为捆绑在单一模型-提供商边界内，难以检查、调整或复用，并可能引发“搜索诱导的冗长”问题，即原生搜索会改变响应风格，破坏严格输出契约。DSG通过一个与MCP兼容的网关，将搜索接地从推理模型中解耦出来，将提供商路由、源感知上下文渲染、配置回退、检索深度控制以及精确和语义缓存作为第一类控件暴露。在SimpleQA、FreshQA、HotpotQA及电商查询理解等基准测试中，DSG在准确性上接近甚至略超原生搜索，同时将搜索成本降低90%以上，并保持严格的简洁输出契约（如99.4%热缓存命中率）。核心贡献在于将实时接地定义为一个可优化的接口边界，而非固定的模型特性，使提供商选择、策略和输出控制成为显式、可控的决策。结论表明，DSG在成本、延迟和输出契约控制方面具有显著优势。
