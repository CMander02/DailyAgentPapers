---
title: "Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents"
authors:
  - "Seyed Moein Abtahi"
  - "Rasa Rahnema"
  - "Hetkumar Patel"
  - "Neel Patel"
  - "Majid Fekri"
  - "Tara Khani"
date: "2026-04-23"
arxiv_id: "2604.22085"
arxiv_url: "https://arxiv.org/abs/2604.22085"
pdf_url: "https://arxiv.org/pdf/2604.22085v1"
categories:
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Long-Horizon Agent"
  - "Semantic Memory"
  - "Information Retrieval"
  - "Multi-Session Agent"
  - "Memory Architecture"
  - "Production Agent Systems"
relevance_score: 9.5
---

# Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents

## 原始摘要

The transition from stateless language model inference to persistent, multi session autonomous agents has revealed memory to be a primary architectural bottleneck in the deployment of production grade agentic systems. Existing methodologies largely depend on hybrid semantic graph architectures, which impose substantial computational overhead during both ingestion and retrieval. These systems typically require large language model mediated entity extraction, explicit graph schema maintenance, and multi query retrieval pipelines. This paper introduces Memanto, a universal memory layer for agentic artificial intelligence that challenges the prevailing assumption that knowledge graph complexity is necessary to achieve high fidelity agent memory. Memanto integrates a typed semantic memory schema comprising thirteen predefined memory categories, an automated conflict resolution mechanism, and temporal versioning. These components are enabled by Moorcheh's Information Theoretic Search engine, a no indexing semantic database that provides deterministic retrieval within sub ninety millisecond latency while eliminating ingestion delay. Through systematic benchmarking on the LongMemEval and LoCoMo evaluation suites, Memanto achieves state of the art accuracy scores of 89.8 percent and 87.1 percent respectively. These results surpass all evaluated hybrid graph and vector based systems while requiring only a single retrieval query, incurring no ingestion cost, and maintaining substantially lower operational complexity. A five stage progressive ablation study is presented to quantify the contribution of each architectural component, followed by a discussion of the implications for scalable deployment of agentic memory systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前面向长时间任务自主智能体（Long-Horizon Agents）的记忆系统所面临的核心瓶颈——即“记忆税”（Memory Tax）问题。研究背景是，随着大语言模型从无状态推理向需要持久化状态的多会话自主智能体演进，记忆架构已成为部署生产级智能体系统的主要瓶颈。现有方法（如Mem0、Zep、Letta等）高度依赖混合语义图架构，这些架构虽然性能尚可，但在数据摄取和检索过程中引入了巨大的计算开销、高延迟和系统复杂性。具体来说，现有系统通常需要大语言模型进行实体提取、维护显式的图模式（Graph Schema），并采用多查询检索流水线。本文要解决的核心问题是：能否在不依赖知识图谱和复杂LLM驱动摄取流程的前提下，构建一个高精度、低延迟且操作简单的通用智能体记忆层。为此，论文提出了Memanto，它通过集成一种包含13个预定义类别的类型化语义记忆模式、自动冲突解决机制、时间版本控制，以及基于信息论的无索引语义检索数据库，来挑战“知识图谱复杂性是获得高保真度记忆的必要条件”这一普遍假设，旨在以极低的运营复杂度实现顶尖的检索准确率。

### Q2: 有哪些相关研究？

相关研究可从以下几个类别进行梳理：

**1. 认知科学启发的记忆框架：**
- 借鉴Tulving的情景、语义、程序记忆划分和Baddeley的工作记忆模型，许多工作强调了情景记忆对长程Agent的重要性。例如，ENGRAM通过三种记忆类型和统一路由机制提升了性能，而Memanto进一步细化为13个类别。

**2. 混合图-向量架构（主流方法）：**
- MemGPT/Letta采用操作系统式的虚拟内存，但递归摘要可能引入延迟和信息失真。
- Mem0采用三层记忆层次（用户、会话、Agent），结合向量检索和知识图谱，但消融实验显示图谱带来的提升有限，且插入过程复杂耗时。
- Zep/Graphiti通过时间版本化和双时态索引支持审计，但同步提取管线导致写入延迟。
- A-MEM采用Zettelkasten笔记式设计，每次插入都需要完整推理，成本较高。

**3. 反思与多阶段检索方法：**
- Hindsight等框架通过多阶段检索和迭代推理取得高准确率，但系统复杂度显著高于单查询方法。

**4. 简化高效的方法：**
- Merrill等人证明简单检索系统可比复杂层次结构表现更好，挑战了架构复杂性的必要性。
- Memanto本身融合了13类记忆模式、冲突解决和时间版本化，但通过Moorcheh信息论搜索引擎实现无索引确定性检索，在无摄入延迟和单次查询下达到SOTA，验证了无需知识图谱复杂度即可取得高保真记忆。

**5. 评测基准：**
- LongMemEval（500题，6类，百万token级多会话）和LoCoMo（长程多轮对话，含单跳、多跳等推理）是主要评估套件。其他如MemoryBank、PerLTQA等进一步扩展了评测场景，但近期分析指出随着模型上下文窗口增长，基准性能越来越反映LLM推理能力而非记忆架构本身。

### Q3: 论文如何解决这个问题？

Memanto通过创新的类型化语义记忆架构和信息论检索机制解决长时程智能体记忆问题。整体架构分为前端和后端两层：前端包含Agent生态系统（IDE集成、自定义Agent、本地仪表盘）和Memanto网关（CLI引擎和FastAPI服务器），后端包括共享服务层和Moorcheh.ai云层。

核心组件包括：(1) 类型化语义记忆模式，包含13个预定义记忆类别（如情景记忆、语义记忆、程序性记忆），支持自动分类和标签；(2) 自动化冲突解决机制，检测新信息与现有记忆的矛盾并标记而非静默覆盖；(3) 时间版本管理，记录记忆的时间戳和演化历史。

关键技术是Moorcheh的信息论搜索引擎（ITS），取代了传统的HNSW+余弦相似度范式。三大创新算法包括：最大信息二值化（MIB）将高维浮点嵌入压缩为二进制表示（32倍压缩无信号损失）；高效距离度量（EDM）使用信息论距离替代余弦相似度；信息论评分（ITS）提供标准化的[0,1]范围相关性分数。

该系统实现零索引延迟（消除摄入开销）、单一查询检索（无需多查询流水线）、亚90毫秒确定性检索。通过五个阶段的消融研究量化每个组件的贡献，在LongMemEval和LoCoMo基准上分别达到89.8%和87.1%的SOTA准确率。

### Q4: 论文做了哪些实验？

论文对Memanto系统在LongMemEval和LoCoMo两个基准上进行了五阶段逐步消融实验。实验设置如下：LongMemEval包含500个手工问题（约115K tokens/50个会话），评估信息提取、多会话推理、时序推理、知识更新和弃权能力；LoCoMo是多模态对话基准（平均35个会话、300轮、9K tokens），涵盖单跳、多跳、开放域和时序推理。所有评估使用Claude Sonnet 4作为LLM评判器，主要对比混合图系统和向量系统的性能。

消融实验分五阶段进行：（1）基线配置（k=10，阈值0.15）在LongMemEval和LoCoMo上准确率分别为56.6%和76.2%；（2）召回扩展（k=10→40，阈值0.10）带来最大提升，LongMemEval上涨20.4个百分点至77.0%，LoCoMo上涨6.6个百分点至82.8%；后续阶段逐步引入类型语义记忆、冲突解决和时间版本控制等组件。

最终配置下，Memanto在LongMemEval达到89.8%、在LoCoMo达到87.1%的SOTA准确率，超越了所有混合图和向量系统（包括基线方法），且仅需单次检索查询，零摄入成本。研究还量化了各架构组件的独立贡献，并分析了替代架构的操作开销。

### Q5: 有什么可以进一步探索的点？

基于当前研究，未来可探索以下方向：首先，Memanto依赖13个预定义记忆类型，可进一步研究动态生成或自适应记忆类别，以提升对非结构化任务的泛化能力。其次，信息论检索虽避免了索引开销，但面对超大规模知识库时，其去重与冲突解决机制可能带来隐式计算成本，需要更高效的近似匹配策略。此外，当前评估仅覆盖对话型任务，可扩展至多模态记忆场景（如视觉、工具调用痕迹）。最后，其时序版本控制虽支持回溯，但缺乏错误记忆的自动修正机制，可引入基于强化学习的记忆衰减或重评策略，提升长期任务中的鲁棒性。

### Q6: 总结一下论文的主要内容

Memanto提出了一种用于长周期AI智能体的类型化语义记忆系统,核心贡献在于挑战了知识图谱复杂度对高保真记忆的必要性假设。该方法采用13个预定义语义类别构成类型化记忆架构,结合自动冲突解决和时间版本机制,并基于Moorcheh的信息论搜索引擎实现无索引语义数据库,在亚90毫秒延迟内提供确定性检索,且不产生任何引入延迟。在LongMemEval和LoCoMo基准测试中分别达到89.8%和87.1%的准确率,超越所有混合图与向量系统,并显著降低了操作复杂度。结论表明,通过结构化记忆类型和优化语义检索,无需图谱架构和多查询流水线即可实现生产级记忆系统。
