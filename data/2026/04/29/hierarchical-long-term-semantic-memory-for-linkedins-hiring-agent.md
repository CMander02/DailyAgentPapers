---
title: "Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent"
authors:
  - "Zhentao Xu"
  - "Shangjing Zhang"
  - "Emir Poyraz"
  - "Yvonne Li"
  - "Ye Jin"
  - "Xie Lu"
  - "Xiaoyang Gu"
  - "Karthik Ramgopal"
  - "Praveen Kumar Bodigutla"
  - "Xiaofeng Wang"
date: "2026-04-29"
arxiv_id: "2604.26197"
arxiv_url: "https://arxiv.org/abs/2604.26197"
pdf_url: "https://arxiv.org/pdf/2604.26197v1"
categories:
  - "cs.IR"
  - "cs.LG"
tags:
  - "长期记忆"
  - "层次化记忆"
  - "招聘代理"
  - "个性化"
  - "生产部署"
  - "商用Agent"
relevance_score: 8.5
---

# Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent

## 原始摘要

Large Language Model (LLM) agents are increasingly used in real-world products, where personalized and context-aware user interactions are essential. A central enabler of such capabilities is the agent's long-term semantic memory system, which extracts implicit and explicit signals from noisy longitudinal behavioral data, stores them in a structured form, and supports low-latency retrieval. Building industrial-grade long-term memory for LLM agents raises five challenges: scalability, low-latency retrieval, privacy constraints, cross-domain generalizability, and observability. We introduce the Hierarchical Long-Term Semantic Memory (HLTM) framework, which organizes textual data into a schema-aligned memory tree that captures semantic knowledge at multiple levels of granularity, enabling scalable ingestion, privacy-aware storage, low-latency retrieval, and transparent provenance; HLTM further incorporates an adaptation mechanism to generalize across diverse use cases. Extensive evaluations on LinkedIn's Hiring Assistant show that HLTM improves answer correctness and retrieval F1 significantly by more than 10%, while significantly advancing the Pareto frontier between query and indexing latency. HLTM has been deployed in LinkedIn's Hiring Assistant to power core personalization features in production hiring workflows.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决为大规模工业级LLM智能体（如LinkedIn的Hiring Assistant）设计长时语义记忆系统所面临的五重挑战。研究背景是，虽然现有工作（如MemGPT、GraphRAG、RAPTOR等）已通过显式记忆模块、图结构或分层结构增强了智能体的长上下文能力，但在生产环境中仍存在显著不足。现有方法的不足主要体现在五个方面：**1）可扩展性**：难以高效处理海量异构数据，缺乏并行化增量摄取的能力；**2）低延迟检索**：在线对话场景对检索速度要求严苛，但现有方法多将大量计算放在服务时，无法在开销与效果间取得良好平衡；**3）隐私约束**：企业级系统需满足GDPR等严格的数据隔离与删除政策，现有方案缺乏内置的跨租户隔离机制；**4）跨领域通用性**：现有记忆系统高度依赖手工制定的业务规则或特征管道，难以适应多变的产品需求和新查询模式；**5）可观测性与一致性**：无法有效追踪记忆来源，且当源数据更新时容易产生陈旧或矛盾记忆。因此，本文的核心问题是：如何设计一个兼具高吞吐摄取、低延迟检索、隐私安全、跨场景自适应以及数据溯源一致性的工业级长时语义记忆框架。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是记忆管理方法，如 **MemGPT** 采用 OS 式上下文与外部记忆的交换机制，**Mem0** 依赖语义搜索检索离散记忆项，**MemoryBank** 使用时间衰减强调近期性，**ReadAgent** 通过压缩长文档生成摘要并支持按需查找，**SCM** 则引入控制器自适应决定存储/更新/检索时机。这些方法大多缺乏面向隐私隔离的分区设计，且难用于生产。第二类是结构化表征方法，如 **GraphRAG** 构建知识图谱与社区摘要捕获实体关系，**HippoRAG** 借鉴海马体索引实现多跳推理与持续学习，**A-mem** 与 **G-Memory** 采用卡片笔记或图结构支持自主记忆演化。它们存在索引时 LLM 调用成本高或在线延迟大的问题，无法满足工业级需求。第三类是层次化检索方法，如 **RAPTOR**、**TreeRAG** 和 **MemTree** 使用分层树结构处理长上下文，提升下游 QA 性能，但通常依赖 LLM 世界知识聚合，缺乏领域控制力与可观察性。本文提出的 HLTM 针对上述不足，设计了模式对齐的记忆树结构，支持跨域泛化、隐私感知存储、低延迟检索，并具备透明的可溯源能力，在 LinkedIn 招聘助手中实现了超过 10% 的准确率与 F1 提升，且显著优化了索引和查询延时的帕累托前沿。

### Q3: 论文如何解决这个问题？

HLTM采用了一种新颖的分层架构来构建长期语义记忆。其核心是构建一个与业务模式对齐的树状索引结构，树的拓扑由企业数据模型和所有权边界决定（例如，叶子节点对应具体招聘项目，中间节点对应招聘人员，根节点对应组织账户），而非基于语义聚类。这带来了隐私隔离、局部增量更新和拓扑稳定三大优势。

每个节点不再存储原始数据，而是通过LLM生成三种紧凑的多视角记忆表示：**摘要（Summary）**、**方面（Facet，即键值对）**和**可回答QA对（Answerable-QA）**。这些表示分别服务于宽泛的总结查询、精确的约束过滤和类似用户意图的检索。

检索时，HLTM在**身份限定子树**内进行硬过滤以保证数据隔离。随后采用**多信号检索**策略，同时使用方面、答案和摘要三种检索器对候选节点进行评分和排序，并将结果作为上下文输入给LLM进行推理。此外，HLTM还引入了一个**周期性适应机制**，通过分析历史查询日志来识别高频查询模式和关键方面，从而指导记忆构建，确保记忆内容与生产查询模式保持对齐。

### Q4: 论文做了哪些实验？

论文在LinkedIn Hiring Assistant的真实使用日志上构建了人工标注的基准数据集，包含120个查询（70个总结型、50个检索型）和50份文档（平均每份约3500词），由领域专家提供黄金参考答案，每个答案由至少三名标注者独立标注并通过多数投票解决分歧。对比方法包括基础基线（全上下文提示、常规RAG）和高级RAG/记忆系统（A-Mem、HippoRAG、RAPTOR、GraphRAG、SimpleMem、Mem0、ReadAgent），固定使用text-embedding-3-large和gpt-4o-mini（部分实验使用GPT-5.2）。主要结果：在总结型查询上，HLTM的Token-F1（0.635）、BLEU-1（0.473）和语义正确性（0.798）均显著优于所有基线，比最强基线（常规RAG和HippoRAG）提升超过15%；在检索型查询上，HLTM的F1（0.712）超过最佳基线（常规RAG）10%以上。消融实验表明，去除树聚合导致总结型正确性下降约12分（0.798→0.678）、检索型F1下降约18分（0.712→0.534），去除适应性机制导致正确性下降约10分（0.798→0.701）。HLTM在查询延迟（约3.4秒）上处于Pareto前沿，并将查询时token使用量相比图基线减少至少50%。

### Q5: 有什么可以进一步探索的点？

论文提出的HLTM框架在内存层级间缺乏动态的剪枝与合并机制，长期运行可能累积冗余节点。未来可探索基于信息增益的自动树结构优化算法，结合用户反馈实现记忆节点的适应性压缩。当前隐私保护依赖静态数据脱敏，可引入差分隐私或联邦学习框架，在记忆写入时注入噪声，同时通过差分隐私预算追踪防止敏感信息重建。跨领域泛化方面，HLTM的schema对齐策略仍需要手动定义领域模版，可尝试利用大模型的元学习能力，从少量交互样本中自动生成层级化记忆骨架。另一个潜在方向是时间感知的记忆衰退与强化机制，将认知科学中的艾宾浩斯遗忘曲线引入记忆树的衰减权重计算，使高频更新的用户画像与低频的长周期记忆层级解耦。此外，当前评测仅关注单轮检索准确性，可设计多轮对话的长期记忆协作评估任务，检验记忆树在推理链中的拓扑影响。

### Q6: 总结一下论文的主要内容

这篇论文提出了层次化长期语义记忆（HLTM）框架，旨在解决工业级LLM智能体长期记忆系统面临的五大挑战：可扩展性、低延迟检索、隐私约束、跨领域泛化性和可观测性。HLTM的核心创新在于构建了一个与商业逻辑对齐的层级记忆树结构，将文本数据组织成包含摘要、分面、问答对的多视图表示，并通过自底向上的聚合实现跨节点知识融合。在检索时采用身份域过滤和多信号检索机制，支持隐私合规和低延迟响应。在LinkedIn招聘助手场景的实验中，相比现有最强基线，HLTM在概括式查询的语义正确性上提升超过15%，在检索式查询的F1值上提升超过10%，同时显著优化了查询与索引延迟的帕累托前沿。该框架已投入生产环境，支撑数百万文档的实时索引和个性化招聘工作流。
