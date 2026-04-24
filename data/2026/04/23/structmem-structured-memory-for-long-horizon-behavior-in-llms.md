---
title: "StructMem: Structured Memory for Long-Horizon Behavior in LLMs"
authors:
  - "Buqiang Xu"
  - "Yijun Chen"
  - "Jizhan Fang"
  - "Ruobin Zhong"
  - "Yunzhi Yao"
  - "Yuqi Zhu"
  - "Lun Du"
  - "Shumin Deng"
date: "2026-04-23"
arxiv_id: "2604.21748"
arxiv_url: "https://arxiv.org/abs/2604.21748"
pdf_url: "https://arxiv.org/pdf/2604.21748v1"
github_url: "https://github.com/zjunlp/LightMem"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.IR"
  - "cs.LG"
  - "cs.MA"
tags:
  - "LLM Agent Memory"
  - "Hierarchical Memory"
  - "Temporal Reasoning"
  - "Multi-hop QA"
  - "Conversational Agent"
  - "Long-horizon Agent"
  - "Structured Memory"
relevance_score: 8.5
---

# StructMem: Structured Memory for Long-Horizon Behavior in LLMs

## 原始摘要

Long-term conversational agents need memory systems that capture relationships between events, not merely isolated facts, to support temporal reasoning and multi-hop question answering. Current approaches face a fundamental trade-off: flat memory is efficient but fails to model relational structure, while graph-based memory enables structured reasoning at the cost of expensive and fragile construction. To address these issues, we propose \textbf{StructMem}, a structure-enriched hierarchical memory framework that preserves event-level bindings and induces cross-event connections. By temporally anchoring dual perspectives and performing periodic semantic consolidation, StructMem improves temporal reasoning and multi-hop performance on \texttt{LoCoMo}, while substantially reducing token usage, API calls, and runtime compared to prior memory systems, see https://github.com/zjunlp/LightMem .

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长时对话代理（long-horizon conversational agents）在记忆系统中面临的核心困境：如何在高效存储信息的同时，支持对事件间时序关系和多跳推理（multi-hop reasoning）的结构化理解。现有方法存在一个根本性的权衡：**平面记忆（flat memory）** 虽效率高，但将事实或摘要作为独立单元存储，无法建模事件间的关联，导致长历史检索退化为浅层相似度匹配；而 **图记忆（graph memory）** 虽可通过实体关系提取恢复结构化关系，但其构建成本高昂、依赖级联推理且易因噪声提取产生错误累积。论文指出，这些不足的根源在于 **记忆单元选择不当**——孤立的事实或三元组无法承载因果关系和交互语境。为此，本文提出 **StructMem**，一种以“事件”（event）为核心的分层记忆框架。它通过**双重视角提取**在时间上下文中保留事件内容与交互关系，并利用**周期性语义合并**在跨事件层面高效诱导高阶结构，从而在不依赖显式模式设计或符号图遍历的前提下，兼顾结构化推理能力与计算效率。

### Q2: 有哪些相关研究？

相关研究可分为三类：

**1. 扁平记忆方法**  
早期工作将历史对话外部化为向量数据库，通过语义匹配检索。本文指出其根本缺陷：将互动历史视为无序命题集合，丢失时间顺序、因果关系和事件间关联，导致多跳推理退化为表面相似度搜索（如“Lost-in-the-Middle”问题）。即使结合反思机制（如Reflective Reasoning）或闭环控制，仍受限于扁平表征的固有约束。

**2. 结构化记忆方法（知识图谱类）**  
- **静态图**：如GraphRAG、HippoRAG采用层次社区检测和PageRank实现全局推理  
- **动态图**：Mem0^g、Zep通过演化模式捕捉用户交互流变  
- **轻量图**：通过实体-关系索引提升多智能体协作（如Entity-relation Indexing）  

本文指出这类方法存在三元组压缩导致语义损失、关系提取不稳定引入幻觉噪音、持续图维护带来实时计算负担等根本性权衡。

**3. 中间态方法（结构化压缩类）**  
- HiMem：按对话轮次边界组织层次化文本段  
- TiMem：逐轮附加反思思维链（但带来持续开销）  
- PREMem：预推理用户偏好再存储  
- EMem：保留原始事件片段依赖检索被动整合  
- MemWeaver：轻量实体抽取组织会话级经验  

本文提出的StructMem与上述方法的关键区别在于：通过双重时间视角锚定和周期语义压缩，在不依赖显式图结构的前提下同时保留事件级绑定和跨事件关联，在LoCoMo任务上实现时间推理和多跳性能提升，同时显著降低token消耗与API调用次数。

### Q3: 论文如何解决这个问题？

StructMem通过层次化记忆架构解决长时对话中关系建模的难题。其核心设计分为两层：事件级绑定和跨事件整合。

事件级绑定：输入对话时，模型对每条语句同时提取事实内容（如具体事件）和关系内容（如人际互动、因果依赖），两者均以自然语言形式保留，避免三元组结构化带来的实体解析开销。所有条目通过原始时间戳锚定，构成事件级单元，这样在检索时能将事实和关系重新绑定为一体。这种双视角提取确保了事件内依存关系的完整保留。

跨事件整合：采用周期性语义触发机制。当缓冲事件积累超过阈值时，将缓冲上下文编码为聚合查询，从历史记忆中检索top-K个语义相似的种子条目。对每个种子，恢复其完整时间戳对应的事件上下文（包括同一时刻的事实与关系），与当前缓冲事件共同构成跨事件结构。最后通过语言模型进行综合合成，生成跨事件关系假设，形成补充抽象层。该结构既保持原始记忆的保真度，又通过显式合成支持多跳推理。

创新点：1）用自然语言保持事件结构而非刚性三元组，降低构建代价；2）语义触发式检索避免全局遍历；3）合成操作重构事件间关系而非直接压缩。实验显示，该方法仅用1.5M输入token、1056次API调用即达76.82%总体性能，远优于同类结构记忆系统。

### Q4: 论文做了哪些实验？

论文在 LoCoMo 基准测试上评估了 StructMem 的性能。实验设置采用 LLM-as-a-judge 评估有效性，并通过 token 使用量、API 调用次数和运行时间衡量效率。对比方法涵盖三类：RAG 系统（OpenAI, FullContext, MiniRAG, LightRAG）、扁平记忆方法（LangMem, A-Mem, Mem0）以及结构化记忆方法（MemoryOS, Mem0^g, Zep, Memobase），所有方法均以 gpt-4o-mini 为骨干、text-embedding-3-small 为嵌入模型。主要结果显示，StructMem 在 LoCoMo 上取得最优综合性能，在多领域（68.77）和时间推理（81.62）任务上显著领先于扁平记忆（66.31 / 78.50）和图记忆（66.67 / 76.64），且效率大幅提升：通过缓冲式语义整合，将跨事件操作从逐事件处理降为周期性批量处理，显著减少了 token 消耗和 API 调用。消融实验进一步揭示，扁平检索性能在 60 条记录时达到平台期，而引入跨事件连接（K>0）带来了显著增益，验证了层级化结构对跨时间因果关系的重建能力。

### Q5: 有什么可以进一步探索的点？

StructMem的局限性主要体现在两方面：一是双视角提取质量高度依赖提示词设计，次优提示会导致关系信息捕获不完整，未来可探索自动化提示优化或引入可学习的指令模板；二是缺乏显式的冲突解决与记忆更新机制，面对长期对话中用户事实或偏好的演变，历史摘要可能与新信息矛盾。未来可考虑加入记忆衰减或基于置信度的覆写策略，使层级结构动态反映最新交互状态。此外，现有框架的语义合并周期是固定的，可研究自适应合并频率机制，例如根据对话复杂度或时间跨度动态调整。更长远看，结合神经符号方法，让结构化记忆支持反事实推理或因果链推断，可能进一步突破当前在时间推理上的瓶颈。

### Q6: 总结一下论文的主要内容

结构化记忆（StructMem）是一种面向大语言模型长程对话的层次化记忆框架。现有记忆系统面临根本性权衡：扁平记忆高效但缺乏关系建模能力，图记忆能支持结构化推理但构建成本高且易累积错误。该工作的核心贡献在于提出以“时间锚定关系事件”为基本记忆单元，替代传统的事实或三元组。方法上，StructMem通过双视角抽取构建结构化情节，保留事件内容与交互关系；同时利用时间局部性对语义相关事件进行周期性整合，诱导出高层次关系结构。在LoCoMo基准上的实验表明，StructMem在时序推理和多跳问答任务上取得更优表现，同时显著降低了令牌消耗、API调用次数和运行时间。这项工作突破了效率与结构化表达能力之间的权衡，为构建长期对话智能体的持久记忆系统提供了可行方案。
