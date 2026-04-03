---
title: "ByteRover: Agent-Native Memory Through LLM-Curated Hierarchical Context"
authors:
  - "Andy Nguyen"
  - "Danh Doan"
  - "Hoang Pham"
  - "Bao Ha"
  - "Dat Pham"
  - "Linh Nguyen"
  - "Hieu Nguyen"
  - "Thien Nguyen"
  - "Cuong Do"
  - "Phat Nguyen"
  - "Toan Nguyen"
date: "2026-04-02"
arxiv_id: "2604.01599"
arxiv_url: "https://arxiv.org/abs/2604.01599"
pdf_url: "https://arxiv.org/pdf/2604.01599v1"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "记忆增强"
  - "知识管理"
  - "上下文管理"
  - "检索策略"
  - "文件系统存储"
  - "实验验证"
  - "无外部依赖"
relevance_score: 9.5
---

# ByteRover: Agent-Native Memory Through LLM-Curated Hierarchical Context

## 原始摘要

Memory-Augmented Generation (MAG) extends large language models with external memory to support long-context reasoning, but existing approaches universally treat memory as an external service that agents call into, delegating storage to separate pipelines of chunking, embedding, and graph extraction. This architectural separation means the system that stores knowledge does not understand it, leading to semantic drift between what the agent intended to remember and what the pipeline actually captured, loss of coordination context across agents, and fragile recovery after failures. In this paper, we propose ByteRover, an agent-native memory architecture that inverts the memory pipeline: the same LLM that reasons about a task also curates, structures, and retrieves knowledge. ByteRover represents knowledge in a hierarchical Context Tree, a file-based knowledge graph organized as Domain, Topic, Subtopic, and Entry, where each entry carries explicit relations, provenance, and an Adaptive Knowledge Lifecycle (AKL) with importance scoring, maturity tiers, and recency decay. Retrieval uses a 5-tier progressive strategy that resolves most queries at sub-100 ms latency without LLM calls, escalating to agentic reasoning only for novel questions. Experiments on LoCoMo and LongMemEval demonstrate that ByteRover achieves state-of-the-art accuracy on LoCoMo and competitive results on LongMemEval while requiring zero external infrastructure, no vector database, no graph database, no embedding service, with all knowledge stored as human-readable markdown files on the local filesystem.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前记忆增强生成（MAG）系统中存在的核心架构缺陷。研究背景是，尽管大型语言模型（LLMs）能力强大，但其有限的上下文窗口和注意力稀释等问题，使其难以进行长期记忆和推理。为此，MAG系统通过为智能体（Agent）配备外部记忆模块来扩展其能力。

然而，现有方法普遍采用“外部服务”范式，即将记忆视为一个独立于智能体的外部服务。智能体将数据发送给一个独立的处理流水线（进行分块、嵌入、实体提取或图构建），该流水线负责存储，但本身并不理解数据。这种架构分离导致了三个关键不足：1）**语义漂移**：智能体意图存储的内容与流水线实际捕获的内容之间出现偏差，导致检索结果不准确；2）**丢失协调上下文**：当多个智能体共享外部记忆时，它们共享数据但丢失了背后的推理、意图和行动背景，导致理解断层；3）**恢复脆弱性**：当智能体在任务中途崩溃时，它难以从外部服务中准确重建状态，恢复过程脆弱且复杂。

因此，本文要解决的核心问题是：如何设计一种**智能体原生（agent-native）** 的记忆架构，从根本上消除“理解者”（智能体）与“存储者”（流水线）之间的分离。论文提出的ByteRover系统，其核心思想是让执行推理的同一个LLM来直接负责知识的整理、组织和检索，从而实现记忆操作与智能体认知的无缝集成，确保记忆的语义保真度、上下文完整性和系统鲁棒性。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕记忆增强生成（MAG）系统展开，这些系统旨在为大型语言模型提供外部记忆以支持长上下文推理。根据论文背景部分介绍的分类法，相关工作可分为四类：

**1. 轻量级语义记忆**：这类方法将记忆视为独立的文本单元，通过嵌入向量空间并基于相似性进行检索（如top-k检索）。它们不包含显式的结构关系，是许多检索增强生成（RAG）系统的基础。本文的ByteRover与之区别在于，它摒弃了外部分离的嵌入和向量数据库，由智能体自身来理解和组织记忆。

**2. 以实体为中心和个性化记忆**：这类工作围绕显式实体（如人物、物品）来组织信息，通常使用结构化记录或属性-值对。它们能提供更精准的关联，但依然依赖外部管道进行实体提取和存储。ByteRover则通过智能体原生地定义和管理实体及其关系，避免了语义漂移。

**3. 情景式与反思性记忆**：这类研究引入时间抽象，将交互组织成情景片段或更高层次的摘要，以支持长期连贯性。它们通常涉及额外的总结或反思步骤。ByteRover与之的关联在于也关注记忆的长期演化（通过自适应知识生命周期），但区别在于其层次化结构（上下文树）是由执行任务的同一LLM动态构建和管理的，而非一个独立的总结模块。

**4. 结构化和层次化记忆**：这类方法通过图结构、层次化分层或策略优化的管理，对存储的信息施加显式组织。它们与ByteRover的目标最为接近，都追求有组织的记忆。然而，现有系统普遍采用“智能体-内存服务”的API交互模式，记忆的存储、处理（分块、嵌入、构图）与智能体的理解是分离的。**本文的核心创新点正是颠覆了这一范式**：ByteRover提出了一种“智能体原生”的内存架构，让进行任务推理的同一个LLM来负责知识的整理、结构和检索，从而解决了因架构分离导致的语义漂移、协调上下文丢失和故障恢复脆弱等问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ByteRover的“智能体原生”内存架构来解决传统外部内存服务导致的语义漂移、协调上下文丢失和故障恢复脆弱等问题。其核心方法是颠覆传统管道，让进行任务推理的同一个大语言模型（LLM）来负责知识的整理、组织和检索，从而实现存储系统对知识的理解。

整体框架采用三层逻辑设计。**智能体层**是LLM推理循环，其中记忆操作（整理、查询）是与文件I/O、代码执行并列的一等工具，而非对外部服务的API调用。**执行层**包含一个顺序任务队列，处理整理和查询操作。整理操作在一个沙箱环境中运行，LLM生成的代码通过ToolsSDK接口受控访问知识层。顺序队列无需文件锁即可消除写-写冲突。**知识层**的核心是上下文树、MiniSearch全文索引和查询缓存，所有存储均基于本地文件系统，无需外部数据库或服务。

核心数据结构是**上下文树**，这是一个基于文件的层次化知识图谱，组织为域、主题、子主题和条目。每个条目是一个独立的Markdown文件，包含明确的关系集、原始概念（来源）、叙述性解释、代码片段以及生命周期元数据。关系通过显式的@引用注解声明，构成明确的语义连接边，并维护双向引用索引以实现O(1)查找。

关键技术包括：1) **自适应知识生命周期**：每个条目具有重要性分数、成熟度层级（草案、已验证、核心）和时效性衰减分数，通过复合检索分数将生命周期信号与搜索相关性结合，动态管理知识价值。2) **原子化整理操作**：支持ADD、UPDATE、UPSERT、MERGE、DELETE五种原子操作，并提供一个关键的有状态反馈循环。每次整理调用返回每个操作的成功/失败状态及原因，使智能体能实时感知错误并进行适应性恢复，这是外部服务无法实现的。3) **五层渐进式检索策略**：旨在最小化LLM调用。第0-1层从缓存（精确匹配和模糊匹配）直接返回结果；第2层利用MiniSearch进行BM25全文检索，仅当结果置信度足够高时直接返回；只有新颖或模糊的查询才会升级到第3层（单次优化LLM调用，附带预取上下文）或第4层（完整的多轮智能体推理循环）。大部分查询可在亚100毫秒内、无需调用LLM的情况下解决。

创新点在于其彻底的“智能体原生”理念：将记忆作为智能体的内在能力而非外部服务，通过统一的LLM进行知识的生成与消费，消除了语义鸿沟；采用纯文件系统存储，实现了零外部基础设施依赖、人类可读且可版本控制的知识库；以及通过顺序任务队列和原子写操作确保了系统的一致性和故障恢复的鲁棒性。

### Q4: 论文做了哪些实验？

论文在LoCoMo和LongMemEval-S两个长对话基准上进行了全面实验，以评估ByteRover的推理有效性和系统性能。

**实验设置与数据集**：实验使用LLM-as-a-Judge作为主要评估指标，采用Gemini 3 Flash作为评判模型，Gemini 3.1 Pro作为答案生成模型。评估在两个数据集上进行：1) LoCoMo，包含平均约20K tokens的超长对话，用于评估长程时序和因果检索；2) LongMemEval-S，包含500个问题，上下文平均长度超过100K tokens，用于压力测试记忆保持和可扩展性。

**对比方法**：在LoCoMo上，与Mem0、Zep、Hindsight、HonCho、Memobase和OpenAI Memory共六个记忆系统进行了直接比较。在LongMemEval-S上，对比了Hindsight、HonCho以及已发表结果的Chronos、SmartSearch、Memora、TiMem、Zep和全上下文基线。

**主要结果与关键指标**：
1.  **准确性**：在LoCoMo上，ByteRover取得了96.1%的整体准确率，显著优于次优的HonCho（89.9%）。在Multi-Hop（93.3%）和Temporal（97.8%）类别上优势尤其明显。在LongMemEval-S上，ByteRover整体准确率为92.8%，优于Chronos-Low（92.6%），在Knowledge Update（98.7%）、Temporal Reasoning（91.7%）和Single-Session Preference（96.7%）类别上领先。
2.  **延迟**：在包含23,867个文档的LongMemEval-S上，ByteRover的查询延迟中位数（p50）为1.6秒，p95为2.3秒，表现出良好的可扩展性。
3.  **消融实验**：在LongMemEval-S上的消融研究表明，**分层检索机制（Tiered Retrieval）** 至关重要，禁用后整体准确率下降29.4个百分点至63.4%。而禁用**关系图（Relation Graph）** 或**域外检测（OOD Detection）** 仅导致准确率轻微下降0.4个百分点，表明在静态评估中，经过精心构建的上下文树本身已提供较强的语义连贯性。

### Q5: 有什么可以进一步探索的点？

基于论文所述，ByteRover的局限性主要集中在写入开销、检索延迟、模型依赖性、存储扩展性和并发处理方面。未来研究可探索以下方向：首先，针对写入成本高的问题，可研究混合架构，将高频流数据的机械式分块与LLM的深度理解相结合，例如引入轻量级模型进行初步筛选，仅在必要时触发完整推理。其次，为降低新颖查询的延迟，可优化缓存策略，利用强化学习动态预测代理的查询模式，提前预热索引。此外，模型依赖性方面，可设计更鲁棒的提示工程或微调方案，提升开源模型在知识结构化任务上的准确性，减少格式错误。存储扩展性上，可研究分布式文件索引机制，在保持人类可读格式的同时支持大规模知识库的分片管理。最后，针对并发写入瓶颈，可探索异步任务队列或并行化处理方案，平衡一致性与吞吐量。这些改进有望在保持代理原生优势的同时，提升系统的实用性和可扩展性。

### Q6: 总结一下论文的主要内容

该论文提出了ByteRover，一种新型的智能体原生记忆架构，旨在解决现有记忆增强生成（MAG）方法中因记忆存储与智能体推理分离而导致的语义漂移、协调上下文丢失和故障恢复脆弱等问题。其核心贡献在于颠覆了传统MAG范式：让执行任务的同一大型语言模型（LLM）直接负责知识的整理、构建与检索，而非依赖外部服务。

方法上，ByteRover将知识组织为分层的上下文树，包含领域、主题、子主题和条目等级别，每个条目均带有明确关系、来源和自适应知识生命周期管理。其检索采用五层渐进策略，多数查询可在无需调用LLM的亚100毫秒延迟内解决，仅对新颖问题才升级至智能体推理。实验表明，在LoCoMo基准上取得了最先进精度，在LongMemEval上也具有竞争力。

主要结论是，ByteRover通过将记忆操作深度整合进智能体推理循环，实现了状态反馈闭环，消除了语义漂移，保持了跨智能体的协调上下文，并支持优雅的故障恢复。该系统无需任何外部基础设施（如向量数据库或嵌入服务），所有知识均以人类可读的Markdown文件形式存储在本地文件系统中，兼具高效性与实用性。
