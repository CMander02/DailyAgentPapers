---
title: "From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM Agents"
authors:
  - "Yiqi Wang"
  - "Jiaqi Zhang"
  - "Taotao Cai"
  - "Zirui Liu"
  - "Qingqiang Sun"
  - "Zequn Sun"
  - "Zhangkai Wu"
  - "Mingkai Zhang"
  - "Yanming Zhu"
date: "2026-06-03"
arxiv_id: "2606.04990"
arxiv_url: "https://arxiv.org/abs/2606.04990"
pdf_url: "https://arxiv.org/pdf/2606.04990v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "LLM Agent的可信度"
  - "证据溯源"
  - "执行溯源"
  - "Agent审计与调试"
  - "工具使用溯源"
  - "Agent安全与鲁棒性"
  - "基准与评估"
relevance_score: 8.0
---

# From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM Agents

## 原始摘要

Large language model (LLM)-based agents increasingly solve complex tasks by interacting with external tools, retrieval systems, memory modules, environments, and other agents. These capabilities expand agent autonomy, but also make agent behavior harder to verify, debug, and audit. Final-answer accuracy alone cannot explain how an output was produced, which evidence supported each claim, whether tool calls were justified, how memory influenced later decisions, or where execution failures originated. Evidence tracing and execution provenance address this gap by modeling how retrieved evidence, tool outputs, memory items, environment observations, intermediate claims, actions, and final answers are connected throughout agent execution. This survey provides a systematic review and conceptual framework for evidence tracing and execution provenance in LLM agents. We organize related work around a unified provenance perspective that connects retrieval grounding, claim support, tool-use safety, memory lineage, observability, debugging, audit, and recovery. We introduce a taxonomy covering trace sources, evidence and execution units, provenance relations, tracing granularity and timing, representation forms, and trust functions. We review key methodological directions, including provenance representation, evidence attribution, tool-use provenance, runtime guardrails, provenance-bearing memory, trace-based observability, and failure diagnosis. We also map existing benchmarks, datasets, and evaluation metrics to provenance-related capabilities, and discuss how evaluation can move from final-answer correctness toward process-level accountability. Finally, we outline open challenges, including unified trace schemas, claim-level and semantic provenance, provenance-aware safety mechanisms, realistic execution-trace benchmarks, recovery-oriented evaluation, and privacy-aware audit infrastructure.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于大语言模型（LLM）的智能体在执行复杂任务时，其行为难以验证、调试和审计的问题。研究背景指出，现代LLM智能体能够与外部工具、检索系统、记忆模块、环境及其他智能体交互，其自主性不断增强。然而，现有方法仅依赖最终答案的准确性来评估智能体，这无法揭示输出是如何产生的、每个声明由哪些证据支持、工具调用是否合理、记忆如何影响后续决策，以及执行失败的具体根源。这种“过程级问责缺失”导致了信任鸿沟。具体而言，现有不足包括：检索增强生成（RAG）研究主要集中在文档到答案的归因，而忽略了工具调用、参数、执行结果、记忆读写、环境观察、中间推理步骤及多智能体消息流等更广泛的溯源需求；工具使用安全研究侧重于不当行为，但缺乏系统的信息流追踪；记忆系统被视作被动存储，未能充分体现其作为可溯源证据源的角色。因此，本文的核心问题是：如何构建一个统一的证据追踪与执行溯源框架，以系统性地记录、连接和推理智能体执行过程中的证据、工具、记忆、观测、声明、动作及智能体交互，从而弥合智能体执行与下游信任功能（如验证、调试、审计、安全与恢复）之间的鸿沟，将评估从最终答案正确性提升至过程级可问责性。

### Q2: 有哪些相关研究？

基于上述论文，相关研究主要包括以下几类：**方法类** 和 **评测与基准类**。

在**方法类**中，相关工作聚焦于证据追踪与执行溯源的表示、归因和安全机制。例如，关于**检索增强生成（RAG）** 的研究探讨了如何将检索到的证据与最终答案连接，本文在RAG基础上扩展了更广泛的工具调用和记忆溯源。**工具调用溯源**工作（如函数调用链追踪）被本文吸收，并强调了其安全性和可审计性。**记忆溯源**研究关注记忆项如何影响后续决策，本文将其纳入统一框架。此外，**运行时防护**和**失败诊断**方法（如基于trace的异常检测）也是本文归类的重要方向。本文与这些工作的主要区别在于，它提供了一个统一的“溯源视角”（Provenance Perspective），将分散的检索、工具使用、记忆、观察等环节整合进一个连贯的执行图，而不仅仅是解决某个子问题。

在**评测与基准类**中，相关研究包括现有的**LLM Agent基准**（如WebArena、MINT、ToolBench等），但这些基准主要评估最终任务准确率。本文指出，现有评测缺乏对**过程级问责**（Process-level Accountability）的评估。因此，本文规划了专门针对执行溯源能力的基准和数据集，旨在衡量证据归因、溯源路径完整性和恢复能力，从而将评估焦点从“答案正确性”转向“过程可解释性”。

### Q3: 论文如何解决这个问题？

论文提出了一种面向LLM Agent的证据追踪与执行溯源概念框架，以解决Agent行为难以验证、调试和审计的问题。核心方法是对Agent执行过程中产生的各类痕迹进行系统化建模与关联。

整体框架基于一个统一的溯源视角，将检索 grounding、声明支持、工具使用安全、记忆谱系、可观测性、调试、审计和恢复等方向串联起来。其核心是作者提出的五维分类法(Taxonomy)：
1.  **痕迹来源 (Trace Sources)**：识别产生可追溯痕迹的组件，包括推理、检索、工具使用、记忆、环境交互和多Agent通信。每个来源都贡献不同类型的证据和执行记录，并引入不同的故障模式。
2.  **证据与执行单元 (Evidence & Execution Units)**：区分两类基本单元。**证据单元**（如文档、段落、观察、工具输出、记忆、声明）提供语义支持；**执行单元**（如推理步骤、检索调用、工具调用、参数、记忆操作、动作）记录程序化步骤。一个有用的溯源表示需要覆盖这两类单元。
3.  **溯源关系 (Provenance Relations)**：定义了连接痕迹单元的关系类型，超越了传统的W3C PROV-DM。为了应对LLM Agent的语义证据使用、工具介导的动作、记忆更新等，定义了支持、派生、依赖、矛盾、无效化、触发、更新、使用、生成等关系。
4.  **追踪粒度与时机**：粒度从运行级、步骤级、工具调用级到声明级与令牌级；时机包括预执行、运行时、事后与持续。
5.  **信任函数 (Trust Functions)**：明确了证据溯源服务于验证、归因、调试、安全执行、审计和恢复等下游信任目的。

关键技术包括：通过Provenance Representation结构化存储溯源图；通过Evidence Attribution将声明确切链接到支持/矛盾的证据；记录Tool-Use Provenance以链接工具调用、参数、输出及后续影响；设计Runtime Guardrails利用运行时痕迹进行安全策略执行；以及实现Provenance-bearing Memory使记忆操作可追溯等。

### Q4: 论文做了哪些实验？

本文未进行新的实验，而是系统性地调研和综述了LLM Agent中的证据追踪与执行溯源领域。论文对现有方法、基准和评估指标进行了全面梳理，重点给出了该领域的方法论分类和评估现状。

在基准与评估方面，论文指出当前评估主要依赖最终答案正确性，如HotpotQA、FEVER等事实验证数据集用于评估证据归因；ToolBench等工具使用基准用于评估工具溯源；AgentBench、WebArena等环境用于评估可观测性和调试。论文还提到，目前缺乏专门的执行轨迹基准，现有数据集如AgentInstruct、AgentTrajectories等有限体现了轨迹层面的评估。

对比方法上，论文综述了多个方向：在溯源表示方面，比较了W3C PROV、OpenTelemetry等标准；在证据归因方面，对比了基于检索的归因、基于注意力机制的归因、以及基于生成式自解释的方法；在工具使用溯源上，比较了工具调用日志、中间输出记录和可视化追踪方法。论文强调，现有评估多数集中于最终准确率（如F1、EM、Acc），而非过程级别的可信度指标。

主要发现是，现有方法在追踪粒度上存在局限：多数只能做到步骤级或语句级追踪，缺乏细粒度的语义级溯源；在运行时防护方面，现有guardrails多关注内容安全，极少集成代码溯源；在记忆溯源方面，大多数Agent系统不记录记忆的来源和影响关系。论文指出，未来的评估需要从最终答案正确性转向过程级问责性，并呼吁建立统一的追踪模式、丰富的执行轨迹基准、以及隐私感知的审计基础设施。

### Q5: 有什么可以进一步探索的点？

论文的局限和未来方向集中在几个关键点：1）当前缺乏统一的trace schema，不同代理系统生成的执行轨迹格式各异，难以跨系统比较和重用工具调用记录；2）现有归因方法多停留在文档或段落级，对句子级甚至子句级的细粒度证据追踪能力不足，且语义级provenance（如抽象推理路径）仍未解决；3）多数安全防护机制独立于provenance，未来可将provenance嵌入运行时护栏，实现基于证据链的实时干预；4）缺乏包含真实执行故障、工具误用和错误传播路径的高质量trace基准；5）恢复导向评估尚未被重视，未来应不仅关注最终正确性，更要衡量代理从失败中恢复并调整provenance的能力。此外，隐私保护的审计基础设施也是一个值得探索的方向，例如在保留执行provenance的同时对敏感工具输出进行差分隐私处理。

### Q6: 总结一下论文的主要内容

这篇论文系统性地探讨了大语言模型(LLM)智能体的证据追溯与执行溯源问题。随着智能体通过与外部工具、检索系统、记忆模块和环境交互来解决复杂任务，其行为验证、调试和审计变得日益困难，仅靠最终答案的准确性无法解释输出是如何产生的。该论文的核心贡献在于，首次将证据追溯和执行溯源确立为LLM智能体的系统级问责层。方法上，论文构建了一个统一的概念框架，围绕统一的溯源视角组织相关工作，引入了一个涵盖溯源来源、证据和执行单元、溯源关系、追溯粒度和时机、表示形式及信任函数的分类体系。主要结论表明，从最终的答案正确性评估转向过程级问责对于构建可信赖的智能体系统至关重要，并指出了统一溯源模式、语义溯源、面向恢复的评估等未来方向，对提升LLM智能体的透明度、可审计性和安全性具有重要指导意义。
