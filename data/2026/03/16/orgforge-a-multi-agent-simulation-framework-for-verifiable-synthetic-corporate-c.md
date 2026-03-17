---
title: "OrgForge: A Multi-Agent Simulation Framework for Verifiable Synthetic Corporate Corpora"
authors:
  - "Jeffrey Flynt"
date: "2026-03-16"
arxiv_id: "2603.14997"
arxiv_url: "https://arxiv.org/abs/2603.14997"
pdf_url: "https://arxiv.org/pdf/2603.14997v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.IR"
tags:
  - "多智能体模拟"
  - "合成数据生成"
  - "RAG评估"
  - "框架"
  - "可验证性"
  - "组织行为模拟"
relevance_score: 7.5
---

# OrgForge: A Multi-Agent Simulation Framework for Verifiable Synthetic Corporate Corpora

## 原始摘要

Evaluating retrieval-augmented generation (RAG) pipelines requires corpora where ground truth is knowable, temporally structured, and cross-artifact properties that real-world datasets rarely provide cleanly. Existing resources such as the Enron corpus carry legal ambiguity, demographic skew, and no structured ground truth. Purely LLM-generated synthetic data solves the legal problem but introduces a subtler one: the generating model cannot be prevented from hallucinating facts that contradict themselves across documents.We present OrgForge, an open-source multi-agent simulation framework that enforces a strict physics-cognition boundary: a deterministic Python engine maintains a SimEvent ground truth bus; large language models generate only surface prose, constrained by validated proposals. An actor-local clock enforces causal timestamp correctness across all artifact types, eliminating the class of timeline inconsistencies that arise when timestamps are sampled independently per document. We formalize three graph-dynamic subsystems stress propagation via betweenness centrality, temporal edge-weight decay, and Dijkstra escalation routing that govern organizational behavior independently of any LLM. Running a configurable N-day simulation, OrgForge produces interleaved Slack threads, JIRA tickets, Confluence pages, Git pull requests, and emails, all traceable to a shared, immutable event log. We additionally describe a causal chain tracking subsystem that accumulates cross-artifact evidence graphs per incident, a hybrid reciprocal-rank-fusion recurrence detector for identifying repeated failure classes, and an inbound/outbound email engine that routes vendor alerts, customer complaints, and HR correspondence through gated causal chains with probabilistic drop simulation. OrgForge is available under the MIT license.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决企业环境中检索增强生成（RAG）系统评估所面临的数据集难题。研究背景是，RAG已成为企业部署大语言模型（LLM）应用的主流模式，但现有的评估基础设施严重滞后。当前的基准测试通常要么孤立地评估检索质量，要么在静态的维基百科式文本上进行端到端问答评估，这些都无法捕捉真实企业知识库的关键特性：跨系统相互引用的文档、随时间演变的事实、以及同时在多种类型工作产物（如Slack消息、JIRA工单）中留下痕迹的事件。广泛使用的真实数据集如Enron语料库，存在法律模糊性、数据过时、组织背景单一且缺乏结构化真实标注等问题。

现有方法的不足主要体现在两方面：一是真实数据集（如Enron）在法律、时效性和标注完整性上存在缺陷；二是纯粹由LLM生成的合成数据虽然规避了法律问题，却引入了更隐蔽的“幻觉”问题——生成模型无法保证在不同文档间生成的事实保持一致（例如，关于同一事件的发生时间在不同记录中可能矛盾），导致合成的语料库内部不一致，从而会 silently corrupt（悄无声息地破坏）基于其进行的RAG评估。

因此，本文要解决的核心问题是：如何创建一个**可验证的、内部一致的、具有时序结构和跨工件属性的合成企业语料库**，以支持对企业级RAG管道进行可靠且全面的评估。为此，论文提出了OrgForge框架，其核心创新在于建立严格的“物理-认知”边界：由一个确定性的仿真引擎掌控所有事实真相（即“真实总线”），而LLM仅负责在已验证提案的约束下生成表面文本，从而从根本上防止了LLM幻觉污染语料库的一致性，并确保了跨多种输出工件（邮件、聊天、工单等）的时间线因果正确性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**现有评测数据集**、**纯LLM生成方法**和**基于仿真的方法**。

在**评测数据集**方面，经典的Enron邮件数据集因法律模糊性、人口统计偏差和缺乏结构化事实而受限。近期工作如MultiHop-RAG专注于多跳推理，但基于新闻文章，缺乏组织结构；FRAMES提供了事实性、时序性和多文档问题，但并非基于可控仿真。企业级RAG基准通常不公开。

在**纯LLM生成方法**中，利用大模型直接生成合成数据虽避免了法律问题，但会导致文档间事实矛盾（幻觉），无法保证跨文档一致性，因此难以作为可靠评测基准。

在**基于仿真的方法**中，社会网络仿真等传统研究多用于信息传播分析，但尚未与NLP评测所需的文档语料生成相结合。

本文提出的OrgForge框架与上述工作的核心区别在于：它通过**多智能体仿真**构建了一个具有严格“物理-认知”边界的确定性事实引擎（SimEvent总线），LLM仅受约束地生成表面文本，从而确保了**可追溯的真实性、时序结构、跨文档一致性**和**可配置复杂性**，弥补了仿真方法与语料生成之间的空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个严格区分“物理”与“认知”层的多智能体仿真框架来解决合成企业语料库中事实不一致和幻觉污染的问题。其核心方法是建立一个确定性的、以事件日志为唯一事实来源的仿真引擎，而大型语言模型仅负责生成受约束的表面文本，从而确保语料库的可验证性和时间一致性。

**整体框架与主要模块：**
框架的核心是离散时间仿真，每天依次执行规划、执行和日终总结三个阶段。系统被形式化定义为元组 M = (S, P, V, E)：
1.  **状态 (S)**：一个包含所有可变仿真变量的Pydantic模型，如系统健康度、团队士气、活跃事件和工程师压力分数。
2.  **规划器 (P)**：一组基于LLM的部门智能体，它们观察状态和事件历史，生成当天活动的结构化JSON提案。它们影响叙事方向，但不能直接修改状态或事件日志。
3.  **验证器 (V)**：一个确定性函数 V: ProposedEvent × S × E → {0, 1}，在执行前对每个提案进行准入或拒绝检查。
4.  **事件 (E)**：SimEvent日志——一个持久化、仅追加的权威事实记录，即“事实总线”。LLM通过混合向量搜索从中检索上下文，但从不写入。

**关键技术设计与创新点：**
1.  **严格的物理-认知边界**：这是防止幻觉污染语料库的根本设计。验证器 (V) 作为边界，将确定性的“物理”层（状态 S、事件日志 E、图动态）与生成性的“认知”层（规划器 P）分离。所有重要行动都产生一个结构化的SimEvent记录，作为唯一事实来源。LLM生成的文本（如Slack消息、邮件）必须基于此记录。
2.  **确定性的图动态子系统**：该系统独立于LLM，通过三个机制驱动组织行为演化，确保状态变化的可预测性和可追溯性：
    *   **压力传播**：基于节点中介中心性识别“关键人物”，当其压力超过阈值时，压力会按社交关系权重比例传播给其邻居。
    *   **边权重衰减与增强**：社交关系图中的边权重会随时间衰减，并通过协作活动（如联合事件响应、代码评审）得到增强，模拟真实组织动态。
    *   **基于Dijkstra算法的升级路由**：将事件升级路径建模为在“成本图”（边成本为关系强度的倒数）上的最短路径问题，确保升级路径反映真实的沟通网络拓扑。
3.  **提案-验证循环**：验证器对LLM提案执行五项有序检查（演员完整性、事件类型审查、状态合理性、冷却窗口、士气门控），拒绝不合理的提案并生成审计事件，防止“幽灵员工”、时间线矛盾或情境不一致的幻觉。
4.  **因果链追踪与复发检测**：`CausalChainHandler` 会为每个事件累积一个按时间顺序排列的工件ID链（如Slack警报、JIRA票据、Confluence页面），所有下游工件都被追加到链中，实现跨工件事件的可追溯性。`RecurrenceDetector` 使用基于向量搜索和文本搜索的混合互惠排名融合方法，自动识别具有相似根本原因的历史事件。
5.  **跨组织边界的邮件引擎**：模拟三类外部邮件（技术供应商入站、客户投诉、HR信函），并通过概率丢弃模拟和门控因果链将其反馈到内部的事件处理系统，扩展了仿真的真实性和交互复杂性。
6.  **时间一致性保障**：通过统一的演员本地时钟和确定性的状态更新顺序，确保所有类型工件（Slack线程、JIRA票据等）的时间戳在因果上是正确的，消除了传统方法中因每个文档独立采样时间戳而导致的时间线不一致问题。

总之，OrgForge通过将LLM的文本生成能力严格约束在一个由确定性引擎维护的可验证事实框架内，创造了一个既丰富又可靠的合成企业语料库，为评估RAG管道等任务提供了理想的测试平台。

### Q4: 论文做了哪些实验？

论文实验主要包括对OrgForge框架生成的数据集进行评估，以验证其作为RAG（检索增强生成）评估基准的实用性。

**实验设置**：运行了一个为期22个工作日（约30个日历日）的模拟，模拟了一个包含8个部门、43人的合成组织。整个模拟过程使用了953次LLM调用（模型为openai.gpt-oss-120b-1），总耗时约3小时4分钟，消耗了约5.04亿输入token和3.49亿输出token，总成本估算约为285.30美元。模拟生成了一个包含1079个文档和83个评估问题的语料库。

**数据集/基准测试**：实验的核心是使用OrgForge内置的评估流水线对生成的合成语料库进行系统评估。该流水线从确定性的SimEvent日志中提取因果线程，并自动生成8类问题（如RETRIEVAL、CAUSAL、TEMPORAL等），每类问题都带有难度标签和证据链。

**对比方法与主要结果**：论文在生成的语料库上运行了两种检索基线方法进行对比评估：
1.  **BM25**：在文档正文字段上使用Okapi BM25算法。
2.  **Dense Retrieval**：使用Stella 1.5B模型（通过Ollama）生成嵌入，进行余弦相似度检索。

**关键数据指标**：主要报告了BM25基线在各类问题上的MRR@10（平均倒数排名）和Recall@10（召回率）结果。例如：
*   **总体**：MRR@10为0.2830，Recall@10为0.4659（N=83）。
*   **RETRIEVAL类问题**：MRR@10为0.3548，Recall@10为0.6429（N=28）。
*   **CAUSAL类问题**：MRR@10为0.5417，Recall@10为0.5500（N=20）。
*   **GAP_DETECTION类问题**：MRR@10为0.5000，Recall@10为0.8889（N=3）。
这些结果表明，生成的语料库能够支持对检索系统进行细粒度的、基于证据的评估，并揭示了不同问题类型对检索方法的挑战性差异。

### Q5: 有什么可以进一步探索的点？

该论文提出的OrgForge框架虽在构建可验证合成企业语料方面有显著创新，但仍存在一些局限性和值得深入探索的方向。首先，框架依赖确定性Python引擎维护“地面实况”，其模拟的组织行为和交互模式可能过于理想化，难以完全捕捉真实企业环境中非理性、模糊或突发的复杂动态，例如突发危机下的非正式沟通或政治性决策。其次，系统虽通过图动态子系统（如压力传播、时间衰减）来驱动组织行为，但这些机制基于预设的图算法，可能无法充分建模组织学习、文化演变等长期适应性过程。

未来研究可朝以下方向拓展：一是引入更细粒度的“人因模型”，例如为智能体赋予个性特质、情绪状态或认知偏见，从而生成更具人类行为多样性的交互数据；二是探索“混合真实性”数据生成，将部分真实匿名日志与模拟事件融合，以提升合成数据在边缘案例上的逼真度；三是扩展跨平台交互的复杂性，例如模拟加密通讯工具或新型协作软件中的多模态数据（如语音、草图），以应对更广泛的RAG评估场景。此外，框架可集成强化学习机制，使智能体能够根据历史事件动态调整行为策略，从而生成包含组织演进轨迹的时序语料，这对研究组织变革的检索增强系统尤为重要。

### Q6: 总结一下论文的主要内容

该论文提出了OrgForge，一个用于生成可验证合成企业语料库的多智能体仿真框架。核心问题是现有RAG评估缺乏具有明确、时态结构化且跨文档关联的真实标注数据，而现有真实数据集（如Enron）存在法律和偏见问题，纯LLM生成的数据则存在内部事实矛盾。

论文的核心贡献是设计了一个严格区分“物理-认知”边界的仿真架构：一个确定性的Python引擎维护着包含所有事实的SimEvent“真实总线”，而大型语言模型仅基于已验证的提案生成表面文本，从而防止幻觉污染语料库。方法上，框架通过三个形式化定义的图动态机制（压力传播、边权重衰减和Dijkstra升级路由）来确定性驱动组织行为，并引入了参与者本地时钟来保证所有产出物（如Slack线程、JIRA问题单）时间戳的因果一致性。此外，框架还集成了因果链追踪、混合检索的重复故障检测以及模拟外部邮件收发等子系统。

主要结论是，OrgForge能够生成跨系统、时间锚定且内部一致的合成企业语料库，其产出物与共享的不可变事件日志可追溯，为评估RAG系统在真实企业场景下的跨文档推理能力提供了可靠、可配置且可复现的基础设施。
