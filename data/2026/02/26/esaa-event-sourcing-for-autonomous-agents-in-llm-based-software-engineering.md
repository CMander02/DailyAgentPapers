---
title: "ESAA: Event Sourcing for Autonomous Agents in LLM-Based Software Engineering"
authors:
  - "Elzo Brito dos Santos Filho"
date: "2026-02-26"
arxiv_id: "2602.23193"
arxiv_url: "https://arxiv.org/abs/2602.23193"
pdf_url: "https://arxiv.org/pdf/2602.23193v1"
categories:
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Multi-Agent System"
  - "Agent Planning"
  - "Agent State Management"
  - "Tool Use"
  - "Deterministic Execution"
  - "Event Sourcing"
  - "Software Engineering Agent"
relevance_score: 9.0
---

# ESAA: Event Sourcing for Autonomous Agents in LLM-Based Software Engineering

## 原始摘要

Autonomous agents based on Large Language Models (LLMs) have evolved from reactive assistants to systems capable of planning, executing actions via tools, and iterating over environment observations. However, they remain vulnerable to structural limitations: lack of native state, context degradation over long horizons, and the gap between probabilistic generation and deterministic execution requirements. This paper presents the ESAA (Event Sourcing for Autonomous Agents) architecture, which separates the agent's cognitive intention from the project's state mutation, inspired by the Event Sourcing pattern. In ESAA, agents emit only structured intentions in validated JSON (agent.result or issue.report); a deterministic orchestrator validates, persists events in an append-only log (activity.jsonl), applies file-writing effects, and projects a verifiable materialized view (roadmap.json). The proposal incorporates boundary contracts (AGENT_CONTRACT.yaml), metaprompting profiles (PARCER), and replay verification with hashing (esaa verify), ensuring the immutability of completed tasks and forensic traceability. Two case studies validate the architecture: (i) a landing page project (9 tasks, 49 events, single-agent composition) and (ii) a clinical dashboard system (50 tasks, 86 events, 4 concurrent agents across 8 phases), both concluding with run.status=success and verify_status=ok. The multi-agent case study demonstrates real concurrent orchestration with heterogeneous LLMs (Claude Sonnet 4.6, Codex GPT-5, Antigravity/Gemini 3 Pro, and Claude Opus 4.6), providing empirical evidence of the architecture's scalability beyond single-agent scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的自主智能体在软件工程应用中面临的核心系统性问题。研究背景是LLM智能体正从简单的对话助手演变为能够规划、使用工具执行动作并迭代处理环境观察的复杂系统，被应用于需要长期一致性的软件工程工作流中。然而，现有方法（如AutoGen、MetaGPT、LangGraph等多智能体框架）存在显著不足：它们通常依赖内存数据结构或数据库快照来管理状态，这导致智能体缺乏原生状态管理、在长周期任务中上下文信息会退化，并且概率性生成与确定性执行需求之间存在鸿沟。更具体地说，现有系统缺乏不可变的审计追踪和确定性回放保证，使得在真实的、复杂的软件工程场景（如处理大型代码库、修改多个具有交叉依赖的文件）中，难以审计智能体的行为、理解其决策原因，也无法进行精确的回滚，存在状态漂移和问责制缺失的风险。

本文要解决的核心问题，正是上述结构性缺陷。论文提出，关键不在于简单地“改进提示词”，而在于围绕可验证的不变性重构整个系统。为此，论文引入了ESAA架构，其核心思想是将智能体的认知意图与项目状态变更分离开来。它借鉴事件溯源模式，确保智能体仅输出结构化的意图（如验证过的JSON），而由一个确定性的编排器来验证、持久化事件到仅追加日志中，并应用文件写入等副作用，最终投射出一个可验证的物化视图。这样，系统的真相源不再是代码库的当前快照，而是一个记录了所有意图、决策和效果的不可变事件日志，当前状态可由此日志确定性地推导出来，从而实现了任务的不可变性和完整的法务可追溯性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类与评测类。

在**方法类**中，ReAct模式提出了LLM代理通过工具进行推理与行动的循环，但存在错误传播和上下文退化问题。近期多智能体框架如AutoGen、MetaGPT和LangGraph探索了角色分工与工作流协调，但它们通常采用可变的状态快照，缺乏完整的审计追踪和确定性重放机制。ESAA与这些工作的核心区别在于，它引入了事件溯源（Event Sourcing）作为基础状态管理范式，将智能体的认知意图与状态变更分离，通过仅追加的不可变事件日志和确定性协调器来确保可验证性与追溯性。

在**应用类**方面，SWE-bench等基准测试专注于要求代理在真实代码库中生成可通过测试的补丁，以评估其在软件工程任务中的能力。然而，这些评测并未解决对效果治理和审计追踪的需求。ESAA直接针对此缺口，通过边界合约和哈希验证的物化视图，为软件工程项目提供了可审计的执行框架。

此外，针对**长上下文退化**（如“迷失在中间”）和**结构化输出生成**的研究指出，LLM在长序列中会出现召回率下降，且其概率性生成与系统所需的确定性模式（如JSON、API调用）存在差距。ESAA通过强制智能体输出经过验证的结构化JSON意图，并利用约束解码等思想，旨在弥合这一“结构鸿沟”，从而提升系统的可靠性与一致性。

### Q3: 论文如何解决这个问题？

论文通过提出ESAA架构，核心是采用事件溯源模式，将LLM代理的启发式认知与系统的确定性执行严格分离，以解决传统自主代理缺乏原生状态、长程上下文退化以及概率生成与确定性执行要求不匹配等问题。

整体框架包含三个核心组件：LLM代理、确定性编排器和事件存储。代理不直接写入项目或事件存储，其唯一职责是发出符合边界合约的结构化意图（如`agent.result`或`issue.report`，以验证过的JSON格式）。编排器负责验证这些意图（通过JSON Schema），将事件持久化到仅追加日志（`activity.jsonl`）中，应用文件写入等副作用，并投影出一个可验证的物化视图（`roadmap.json`）。事件存储作为不可变的单一事实来源，记录所有有序事件。

主要模块与关键技术包括：1）**边界合约**（如`AGENT_CONTRACT.yaml`），明确定义每个任务类型（如需求、实现、测试）允许的操作、输出模式和硬性禁止项（如禁止代理直接写入文件），实现权限隔离。2）**元提示配置文件**（PARCER），通过定义角色、受众、规则、上下文、执行和响应六个维度，强制代理输出严格符合JSON信封格式，抑制自由格式输出，确保行为可控。3）**“追踪优先”模型**：在任何不可逆副作用发生前，事件首先作为事实被记录，允许审计和遏制控制，并遵循“已完成任务不可变”规则，缺陷通过新建`issue.report`事件进行热修复，而非重写历史。4）**重放验证与哈希**：通过确定性规范化物化视图并计算其SHA-256哈希（`projection_hash_sha256`），支持重现性验证（`esaa verify`），可检测投影与物化之间的分歧。5）**异构多代理编排**：利用事件存储的仅追加语义，编排器基于角色专业化分配任务，并通过关联ID跟踪各代理的认领与完成情况；并发执行在事件级别自然序列化，编排器在应用副作用前可检测冲突（如文件修改重叠）。

创新点在于将软件工程中的事件溯源模式系统性地引入LLM驱动的自主代理，实现了意图与状态变更的解耦，通过不可变日志和确定性编排保障了状态演进的可靠追溯与验证，并实证支持了多代理并发场景的扩展性。

### Q4: 论文做了哪些实验？

论文通过两个案例研究验证了ESAA架构。实验设置上，作者构建了两个不同复杂度的软件工程项目，并采用基于事件溯源模式的ESAA架构进行管理，其中智能体仅输出结构化意图（JSON格式），由确定性编排器验证、持久化事件并应用文件写入效果。

数据集/基准测试方面，使用了两个自建项目：1）一个简单的着陆页项目（CS1），包含9个顺序任务；2）一个复杂的临床仪表板系统（CS2），包含50个任务，涉及7个组件和15个阶段。关键数据指标包括：CS1产生49个事件，CS2产生86个事件；CS2中使用了4个异构LLM智能体（Claude Sonnet 4.6、Codex GPT-5等）进行并发执行，在1分钟内记录了6个并发任务认领。

对比方法主要体现在架构本身的验证上，通过与传统智能体可能存在的状态丢失、上下文退化等问题进行对比。主要结果是两个案例均以`run.status=success`和`verify_status=ok`结束，输出拒绝率为0。CS2成功展示了架构在并发多智能体场景下的可扩展性，62%的任务（31/50）已完成，并保持了完整的可追溯性。事件词汇从CS1的15种类型简化为CS2的5种核心类型，证明了协议的自然成熟。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其未来探索点可从其局限性与研究方向中提炼。论文已明确指出了几个方向：开发官方CLI工具、解决并发文件修改冲突、实现时间旅行调试、在SWE-bench等真实基准上进行系统评估，以及对编排器不变式进行形式化验证。这些方向旨在提升系统的工程化成熟度、鲁棒性和可验证性。

结合个人见解，可进一步探索的领域包括：首先，**智能冲突消解机制**。当前仅提及冲突检测，未来可研究基于语义理解的自动合并策略，或引入更细粒度的文件锁与版本管理，超越简单的“最后写入获胜”模式。其次，**动态合约与自适应编排**。目前的边界合约（AGENT_CONTRACT.yaml）是静态的。未来可探索合约的动态生成与演化，使系统能根据任务进展和代理表现，实时调整约束条件和权限，实现更灵活的自适应工作流。再者，**跨项目经验迁移与元学习**。事件日志（activity.jsonl）是宝贵的轨迹数据。可研究如何从中提取模式，形成可复用的“工作流模板”或“最佳实践”，用于初始化新项目或指导类似任务，提升代理的泛化能力和效率。最后，**安全与合规性的深度集成**。除了审计追踪，可将代码安全扫描（如SAST）、许可证合规检查等直接作为编排器中的验证步骤，使“确定性执行”管道同时成为“安全合规”管道，这对于企业级应用至关重要。

### Q6: 总结一下论文的主要内容

本文提出ESAA架构，旨在解决基于大语言模型的自主智能体在软件工程任务中面临的核心挑战：缺乏原生状态管理、长程任务中的上下文退化，以及概率性生成与确定性执行要求之间的鸿沟。受事件溯源模式启发，ESAA将智能体的认知意图与项目状态变更分离：智能体仅输出结构化意图（如JSON格式的`agent.result`或`issue.report`），由一个确定性编排器进行验证，并将事件持久化到仅追加日志中；随后应用文件写入等副作用，并生成可验证的物化视图。该方法引入了边界合约、元提示配置以及基于哈希的重放验证机制，确保已完成任务的不可变性和全流程可追溯性。通过两个案例研究（单智能体落地页项目与多智能体临床仪表板系统）验证了架构的有效性，均成功完成所有任务并通过验证。多智能体案例更展示了异构大模型并发编排的可行性，为架构超越单智能体场景的可扩展性提供了实证依据。
