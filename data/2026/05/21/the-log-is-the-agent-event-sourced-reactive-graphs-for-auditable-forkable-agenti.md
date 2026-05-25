---
title: "The Log is the Agent: Event-Sourced Reactive Graphs for Auditable, Forkable Agentic Systems"
authors:
  - "Yohei Nakajima"
date: "2026-05-21"
arxiv_id: "2605.21997"
arxiv_url: "https://arxiv.org/abs/2605.21997"
pdf_url: "https://arxiv.org/pdf/2605.21997v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "事件溯源"
  - "反应式图"
  - "可审计性"
  - "可分叉性"
  - "Agent运行时"
  - "确定性重放"
  - "源线追踪"
relevance_score: 9.5
---

# The Log is the Agent: Event-Sourced Reactive Graphs for Auditable, Forkable Agentic Systems

## 原始摘要

Most agent frameworks are built around the language model: a conversation loop comes first, then tools, then rules, and finally a logging layer bolted on for observability, with state persisted as retrievable "memory." We describe ActiveGraph, a runtime that inverts this arrangement. The append-only event log is the source of truth; the working graph is a deterministic projection of that log; and behaviors--ordinary functions, classes, LLM-backed routines, or logic attached to typed edges--react to changes in the graph and emit new events. No component instructs another; coordination happens entirely through the shared graph. This single design decision yields three properties that retrieval-and-summarization memory systems do not provide: deterministic replay of any run from its log, cheap forking that branches a run at any event without re-executing the shared prefix, and end-to-end lineage from a high-level goal down to the individual model call that produced each artifact. We present the architecture, a determinism contract that makes replay sound, and a worked diligence example whose full causal structure is reconstructable from the log alone. We discuss--without claiming to demonstrate--why this substrate is unusually well suited to self-improving agents, and how it extends the BabyAGI lineage and prior graph-memory research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前主流大语言模型（LLM）智能体框架中一个根本性的架构问题：**日志被当作计算过程的副产品，而非系统的核心基础**。现有的智能体构建模式通常从对话循环开始，逐步添加工具、规则和日志记录，最终将状态持久化为可检索的“记忆”。这种“由模型驱动”的设计存在几个显著缺陷：首先，日志与智能体的实际计算相分离，导致审计追踪和因果溯源困难；其次，传统记忆系统（如摘要和向量检索）是“有损”的，无法提供确定性的重放能力，即无法从日志完美重建任意时刻的智能体状态；最后，这种架构难以支持低成本的分支（fork）操作，使得探索“如果当初做出不同选择会怎样”的反事实分析变得复杂或不可能。

为此，论文提出了**ActiveGraph**运行时系统，其核心思想是“日志即智能体”。它颠倒了传统架构，将**仅追加的事件日志**作为唯一的事实来源，所有智能体状态（包括目标、规则、工具调用、推理轨迹和输出内容）都被统一表示为日志中的事件。智能体的行为（包括普通函数、类、LLM支持的程序或逻辑）被建模为对某种图结构变化的**反应**，这些反应会发出新的事件。这种设计将智能体的整个生命周期转化为一个**可审计、可分叉、可完美重放**的持久化制品。简而言之，本文要解决的核心问题是：**如何通过事件溯源和反应式图计算，构建一个以日志为中心、具备确定性重放、低成本分叉和端到端因果溯源能力的智能体系统架构，以克服传统记忆系统在这方面的不足**。

### Q2: 有哪些相关研究？

1. **记忆系统类**：MemGPT/Letta引入操作系统式虚拟内存管理，Zep和Graphiti维护时序知识图谱作为内存，Mem0聚焦生产级记忆提取，Hindsight提出记忆作为“一等公民”并区分观测与推理。本文与之区别在于：上述系统将记忆视为叠加于智能体之上的派生状态，且上下文来源仅部分可追溯；而ActiveGraph以事件日志为唯一事实来源，所有记忆视图均为日志投影，实现完全溯源与精确重放。
2. **事件溯源与响应式数据流类**：借鉴事件溯源（CQRS）和增量响应式数据流，但创新点在于将其应用于包含非确定性模型调用的智能体系统，通过内容寻址响应缓存处理模型调用不确定性。
3. **黑板架构类**：1970年代的黑板系统通过共享知识结构协调独立知识源，但因知识源脆弱且控制逻辑需手工编写而未能扩展。本文利用大语言模型化解这些限制：自然语言定义行为，协调逻辑可由模型生成。ActiveGraph是事件溯源版的黑板系统，增加了可重放、可分支、可完全追踪的特性。
4. **BabyAGI系列**：ActiveGraph是BabyAGI的直接架构继承者。区别在于BabyAGI通过全局列表和循环维护状态，ActiveGraph则将状态作为仅追加日志的投影，保留任务生成特性同时使每个步骤持久化、可检查、可重放。

### Q3: 论文如何解决这个问题？

ActiveGraph通过将事件日志作为唯一真相源（source of truth）来重构智能体系统的核心架构。其核心方法是：将工作图（working graph）定义为事件日志的确定性投影，行为（behavior）则作为对图状态变化的反应。具体而言：

整体框架采用事件溯源循环：追加写的事件日志（append-only event log）是底层持久化存储，每次执行都通过重放（replay）操作将事件折叠（fold）成图结构（包含类型化对象和关系的集合）。行为以订阅模式注册，当图结构匹配订阅条件时（如Cypher子句描述的模式），运行时触发行为体，行为体可创建对象、调用工具或大模型，所有操作都被记录为新的日志事件。

主要组件包括：事件（events）携带ID、类型、载荷、执行者、因果指针和时间戳；行为（behaviors）支持四种形态——普通函数、类、LLM支持的例程和关系行为（将逻辑附加到类型化边上）；缓存系统采用内容寻址（content-addressed）机制存储模型和工具响应，确保重放时的一致性。

关键技术创新包括：1）确定性重放（deterministic replay）通过记录而非假设LLM输出可重现，在严格模式下逐事件比对证明完整可重现性；2）廉价分叉（cheap forking）通过共享前缀避免重新执行历史事件，仅需重放从分叉点开始的新事件，所有模型调用从缓存读取；3）结构差分（structural diff）基于图拓扑而非扁平键值对进行比较，精确定位对象、关系和补丁的差异。这种架构使所有协调决策都成为事件而非程序计数器位置，从而实现完全的审计追踪和因果管线（causal lineage）。

### Q4: 论文做了哪些实验？

论文通过内置的"尽职调查包"进行了完整的系统验证实验。实验设置采用ActiveGraph运行时，对三家公司（Northwind Robotics、Stellar Logistics、Pinecone Bio）执行投资尽职调查流程，从公司名称开始，依次生成研究问题、检索文档、提取声明、检测矛盾、识别风险并综合备忘录。数据集使用录制好的固定数据（fixtures），无需API密钥，确保完全离线运行和字节级确定性。

实验对比了传统Agent框架（以语言模型为中心、日志作为后加组件）与ActiveGraph的逆架构设计。主要结果：整个运行产生671个事件、93个对象（包括3家公司、24个问题、9个文档、25条声明、25个证据项、1个矛盾、3个风险和3份备忘录）和76个关系，共调用103次模型和48次工具，且无需任何编排代码——行为完全基于图上的对象变化反应式触发。关键指标：两次运行产生字节完全相同的日志，整个流程在三十秒内完成。核心发现是每条声明均可溯源，例如"Northwind第三季度营收同比增长28%至4200万美元"这一声明携带完整溯源块，记录创建它的行为（document_researcher）、触发事件和具体模型请求事件，通过类型化关系链接到问题、来源文档和支持证据，证明了从日志单独重建从目标到输出的完整因果结构的可行性。

### Q5: 有什么可以进一步探索的点？

**局限性与未来探索方向**：当前架构存在若干明确局限：replay成本随日志长度线性增长，缺乏大规模长尾运行中的检查点与压缩机制；外部工具副作用仅能通过记录响应实现重放安全，首次执行仍会修改外部世界；schema演化需依赖迁移工具，存在运维负担；多agent并发的写入排序问题未解决。此外，确定性合约仅通过动态检查实现，行为开发者易在重放时发现违规，缺乏静态验证手段。未来最关键的探索方向是构建真正的自改进系统——利用fork-and-diff原语实现廉价反事实评估：将规则、提示等行为本身作为日志事件，通过分叉运行对比改进效果，共享前缀的缓存可避免重复计算历史。这要求解决自修改的审计与回滚机制，以及如何基于因果结构自动生成改进提议。另一重要方向是混合化持久层：对极长运行采用日志快照与增量检查点，同时保留完全确定性重放能力。建议探索通过类型系统或形式化方法加固确定性合约，例如将LLM调用语义嵌入事件结构，使行为边界的意外触发可在编译期被部分检测。

### Q6: 总结一下论文的主要内容

本文提出ActiveGraph，一种基于事件溯源的反应式图运行时系统，反转了传统LLM智能体框架以语言模型为中心的架构。其核心贡献在于将追加式事件日志作为智能体的唯一真实来源，运行图状态是日志的确定性投影，所有行为（函数、类、LLM例程等）都响应图状态变化并产生新事件，而非直接指令其他组件。系统通过确定性重放机制实现任何运行的可复现，支持廉价分叉以在任意事件点分支运行而无需重执行共享前缀，并提供从高层目标到具体模型调用的端到端溯源。实验通过投资尽职调查案例验证了其逻辑结构的完全可重建性。该架构为构建可审计、可复现、可修正的长时间运行智能体系统提供了基础支撑，特别适用于需要解释、复现和修订智能体行为的场景。
