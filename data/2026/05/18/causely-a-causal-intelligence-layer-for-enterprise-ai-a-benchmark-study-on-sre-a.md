---
title: "Causely: A Causal Intelligence Layer for Enterprise AI A Benchmark Study on SRE and Reliability Workflows"
authors:
  - "Dhairya Dalal"
  - "Endre Sara"
  - "Ben Yemini"
  - "Christine Miller"
  - "Shmuel Kliger"
date: "2026-05-18"
arxiv_id: "2605.18327"
arxiv_url: "https://arxiv.org/abs/2605.18327"
pdf_url: "https://arxiv.org/pdf/2605.18327v1"
categories:
  - "cs.AI"
tags:
  - "AI Agent"
  - "Causal Intelligence"
  - "SRE Workflows"
  - "LLM-based Agent"
  - "Tool Use"
  - "Benchmark Study"
  - "Agent Diagnosis"
relevance_score: 9.5
---

# Causely: A Causal Intelligence Layer for Enterprise AI A Benchmark Study on SRE and Reliability Workflows

## 原始摘要

AI agents deployed into SRE workflows currently derive their understanding of environment state from raw observability telemetry at query time, paying a semantic-interpretation tax in tokens, latency, and inferential reliability. We propose Causely, a causal intelligence layer that maintains a structured representation of environment topology, attribute dependencies, and causal relationships that are anchroed to a ontological representation of the managed environment. Causely transforms raw telemetry into a live, queryable model providing the semantic and causal foundation AI agents require to diagnose, evaluate impact, and act safely in production. We evaluate this value proposition through a benchmark study conducted in a controlled setting with injected faults in a 24-microservice OpenTelemetry demo application. Our experiments compare four agent configurations (Claude Code, OpenAI Codex, HolmesGPT with Sonnet and Gemini backends). Experiments are run with and without access to Causely under two scenarios: an active incident and a healthy baseline. On the active-fault scenario, causal grounding reduces mean time-to-diagnosis by 63\%, mean token consumption by 60\%, and mean tool-call count by 78\%, compressing the investigation footprint by 4.8$\times$ and lowering direct API cost per run by 57\%; root-cause-diagnosis accuracy rises from 75\% to 100\%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决的是AI代理在SRE（站点可靠性工程）工作流程中处理原始可观测性数据时面临的语义理解效率低下和高成本问题。当前，AI代理依赖原始遥测日志、指标等数据来理解环境状态，但每次查询都需要从零开始对原始数据进行语义解释和上下文构建，导致显著的“语义解释税”——即大量的token消耗、延长的延迟以及推理可靠性下降。此外，现有方法缺乏对动态环境拓扑、属性依赖和因果关系的持久结构化表示，使得代理在分析时频繁调用工具重新获取数据，错误诊断率较高，并且随着上下文变长，模型性能会退化。随着AI提供商逐步转向基于token消耗的计费模式，这种低效还将直接转化为高昂的成本。

为解决这些问题，本文提出了Causely——一个因果智能层。它维护一个持续更新的结构化环境模型，包括环境拓扑、属性依赖、实时遥测和因果关系，并将其锚定在领域本体表示上。Causely将原始遥测数据转化为一个可实时查询的活模型，为AI代理提供所需的语义和因果基础，从而使其能够更准确、高效地诊断故障、评估影响并采取安全行动。核心研究问题是验证这种因果智能层能否在SRE任务中显著提升AI代理的性能。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及三类工作：

1. **基础设施自动运维方法类**：传统SRE工作流中，AI Agent依赖原始可观测性遥测数据（如指标、日志、链路追踪），通过查询时实时语义解释理解环境状态，导致高token消耗和推理延迟。本文提出的Causely通过维护环境拓扑、属性依赖和因果关系的结构化表示，将原始数据转化为实时的、可查询的因果模型，显著区别于传统方法。

2. **因果推理在AI系统中的应用类**：先前工作如HolmesGPT等将大语言模型用于故障诊断，但缺乏对环境因果结构的显式建模。Causely创新地将因果智能层作为AI Agent的“基础”，提供语义和因果锚定，使Agent能更准确地进行根因分析，实验显示在活动故障场景下根因诊断准确率从75%提升至100%。

3. **基准评估方法类**：本文在24微服务的OpenTelemetry演示应用中通过注入故障进行受控实验，对比四种Agent配置（Claude Code、OpenAI Codex、HolmesGPT与Sonnet/Gemini后端）。对比无Causely的基线，该系统使诊断时间缩短63%、token消耗减少60%、工具调用次数降低78%，压缩调查足迹4.8倍，单次API成本降低57%，体现了因果层在效率与准确性上的显著优势。

### Q3: 论文如何解决这个问题？

Causely通过构建因果智能层来解决AI代理在SRE工作流中面临的核心问题。其核心方法是将原始可观测性遥测数据转换为一个实时、可查询的结构化模型，为AI代理提供语义和因果基础，从而消除从原始遥测中每轮推理语义的开销。

整体框架由四个核心组件构成：1) **拓扑图 (Topology Graph)**，它是一个实时模型，捕获环境中的实体（如微服务、数据库）及它们之间的连接、分层和组成关系，作为所有推理的骨架。2) **因果知识库 (Causal Knowledge Base)**，一个环境无关的全局知识库，编码了云环境中常见故障模式的领域知识，包括根因、症状及其传播规则。3) **因果图 (Causality Graph)**，是因果知识库在特定环境中的实例化，通过将知识库的传播规则应用于拓扑图，生成一个有向无环图，其中每个边关联了根因导致症状的条件概率，支持溯因推理。4) **属性依赖图 (Attribute Dependency Graph)**，捕获可测量性能属性（如延迟、吞吐量）之间的功能依赖关系，以连续值分析补充离散因果推理。

主要创新点在于，Causely将环境状态的结构化表示（拓扑、属性、因果关系）直接作为结构化上下文提供给AI代理。这种方式消除了代理在每次查询时从原始遥测中推断拓扑、依赖和因果关系的“语义解释税”，从而显著减少了标记消耗、延迟和推理负担。实验表明，在有故障场景下，这种因果基础化使平均诊断时间减少63%，标记消耗减少60%，工具调用次数减少78%，诊断准确率从75%提升至100%。

### Q4: 论文做了哪些实验？

论文在OpenTelemetry Astronomy Shop这个包含24个微服务的Demo应用上进行了实验。实验设置了两种场景：主动故障场景（在payment服务注入代码级缺陷）和健康基线场景（无故障）。实验使用了四种Agent配置（Claude Code、OpenAI Codex、HolmesGPT结合Sonnet和Gemini后端），每个配置在有无Causely因果智能层的条件下各运行6个主动故障查询和3个健康基线查询，共72次运行。主要实验结果：在主动故障场景下，因果层使平均诊断时间降低63%，平均Token消耗降低60%，平均工具调用次数减少78%（调查开销压缩4.8倍），每次运行的API直接成本降低57%，根因诊断准确率从75%提升至100%。在健康基线场景下，HolmesGPT (Claude Sonnet)的幻觉故障率从67%降至0%，Codex从67%降至33%。此外，基线Agent在健康场景上消耗的时间和Token比故障场景多出最多7.2倍，而因果层通过提供"无活动根因"的一级信号反转了这一异常模式。

### Q5: 有什么可以进一步探索的点？

论文的主要局限性体现在实验环境的简化性上：仅基于24个微服务的演示应用、单一注入故障和可控条件，这与生产环境中动辄数百服务的复杂拓扑、并发故障、动态依赖和噪声数据相去甚远。未来研究方向应包括：在更大规模、更真实的微服务系统上进行验证，测试并发故障和渐进式故障场景；扩展因果关系表示以适应动态拓扑变更、配置漂移和云原生特性如自动扩缩容；探索与强化学习的结合以优化诊断策略的决策效率；解决安全性与隐私问题，因因果层需访问敏感拓扑和依赖数据；以及研究如何将人类专家反馈纳入持续改进机制，以维护因果模型的时效性和准确性。此外，因果层的通用性尚待考证——其在不同领域或异构系统间的迁移能力、跨故障类型的鲁棒性、以及与现有可观测性工具的深度集成成本，都是值得探索的方向。

### Q6: 总结一下论文的主要内容

该论文提出了Causely，一个因果智能层，旨在解决AI代理在站点可靠性工程（SRE）工作流中因直接从原始可观测数据推断环境状态而导致的高延迟、高Token消耗和低推理可靠性问题。Causely将原始遥测数据转化为一个包含拓扑图、因果知识库、因果图和属性依赖图的实时、可查询结构化模型，为AI代理提供语义和因果基础。通过在24个微服务的基准测试中注入故障，实验比较了四种AI配置在有/无Causely支持下的表现。主要结论是：在主动故障场景下，Causely使平均诊断时间减少了63%，Token消耗降低60%，诊断准确率从75%提升至100%。该研究量化证明了结构化因果信息能显著提升AI代理在可靠性任务上的效率与准确性，其核心贡献在于形式化定义了因果智能层并实证了其价值。
