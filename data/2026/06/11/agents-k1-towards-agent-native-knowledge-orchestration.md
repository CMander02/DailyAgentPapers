---
title: "Agents-K1: Towards Agent-native Knowledge Orchestration"
authors:
  - "Zongsheng Cao"
  - "Bihao Zhan"
  - "Jinxin Shi"
  - "Jiong Wang"
  - "Fangchen Yu"
  - "Zhijie Zhong"
  - "Zijie Guo"
  - "Tianshuo Peng"
  - "Zhuo Liu"
  - "Yi Xie"
  - "Xiang Zhuang"
  - "Yue Fan"
  - "Runmin Ma"
  - "Shiyang Feng"
  - "Xiangchao Yan"
  - "Anran Liu"
  - "Peng Ye"
  - "Wenlong Zhang"
  - "Shufei Zhang"
  - "Chunfeng Song"
date: "2026-06-11"
arxiv_id: "2606.13669"
arxiv_url: "https://arxiv.org/abs/2606.13669"
pdf_url: "https://arxiv.org/pdf/2606.13669v1"
categories:
  - "cs.AI"
tags:
  - "知识图谱构建"
  - "科学知识编排"
  - "信息提取"
  - "多智能体系统"
  - "GRPO训练"
  - "多模态解析"
  - "智能体接口"
  - "大规模知识库"
relevance_score: 9.5
---

# Agents-K1: Towards Agent-native Knowledge Orchestration

## 原始摘要

Current LLM-based research agents have advanced through agent orchestration, yet largely overlook scientific knowledge orchestration. Existing works often reduce papers to abstracts, surface mentions, and flat \texttt{cites} edges, omitting key entities, claims, evidence, mechanisms, and method lineages essential for scientific reasoning. To this end, we introduce \textbf{Agents-K1}, an end-to-end knowledge orchestration pipeline that converts raw documents into agent-native scientific knowledge graphs. Agents-K1 integrates three components under a unifying theoretical foundation: a multimodal parser whose five-module schema captures entities, multimodal evidence, citations, and typed inter-entity relations across the full paper rather than abstracts alone; a 4B information-extraction backbone trained with GRPO under a rule-based reward; and a graphanything CLI, a tri-source agent interface that unifies web search, multimodal graph retrieval, and cross-document traversal. On top of this, we process 2.46 million scientific papers across six subjects to produce \textbf{Scholar-KG}, of which we release a one-million-paper subset, and the full Scholar-KG is accessible via the SCP link below. The same pipeline can be extended to general-domain corpora and to schema-conformant data synthesis. Extensive experiments demonstrate that Agents-K1 achieves superior performance in scientific information extraction, knowledge graph construction, and multi-hop scientific reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

当前基于LLM的研究智能体（research agents）虽然在智能体编排（agent orchestration）方面取得了显著进展，但严重忽视了科学知识编排（knowledge orchestration）。现有方法存在三方面不足：第一，主流图增强检索pipeline（如LightRAG、HippoRAG等）通常只构建通用的纯文本三元组，局限于摘要和直接提及的术语，丢失了论文中关键实体、主张、证据、机制和方法谱系等科学推理所必需的结构化信息；第二，学术引用图使用扁平化的“引用”边，仅表明一篇论文引用了另一篇，却无法反映是扩展方法、质疑主张还是仅作为基线引用；第三，LLM研究智能体通常运行时直接读取原始PDF或短摘要，导致每个查询都需要重复提取，且难以将答案追溯回精确证据。这些缺陷不仅引发检索错误，更表明当前的知识基础设施并非为智能体推理而设计。为此，本文提出**Agents-K1**这一端到端知识编排pipeline，将原始文档转化为智能体原生科学知识图谱，其核心目标是从根本上解决知识基础设施的结构化缺失问题，满足全论文覆盖、类型化知识抽取和可审计检索的三项设计要求，从而支撑大规模可靠的科学推理。

### Q2: 有哪些相关研究？

相关研究主要分为三类：**检索增强生成（RAG）**、**图结构信息理解**和**深层研究代理**。

在**RAG**方面，现有工作如基于块的检索和图结构RAG系统（如GraphRAG、LightRAG、PathRAG、HippoRAG2）多依赖碎片化文本或三元组，难以保持原始文档（特别是有复杂结构、图表和长程依赖的学术论文）的语义连续性。本文的Agents-K1通过端到端管线构建知识图谱，超越了这些方法，实现了对全文（含图、表、公式）的结构化、多模态统一表示。

在**图结构信息理解**方面，现有工作（如GraphRAG）虽引入知识图谱提升检索质量，但图构建方法局限于提取孤立事实，丢失了完整的文档语义。本文通过五模块解析模式和4B信息提取骨干实现更全面的文档级信息抽取，保留了细粒度的实体、证据、机制和引用关系。

在**深层研究代理**方面，现有系统（如Tongyi DR、InternAgent）多依赖网页或纯文本检索，难以利用科学文献中

关键图表和公式证据。本文创新性地融合网页检索、多模态图谱检索和跨文档遍历三类知识源，以语义锚点统一文本、图像、表格和公式，提供了结构更清晰、证据更可追溯的知识基础设施，有效减少了以文本为中心的信息盲区。

### Q3: 论文如何解决这个问题？

Agents-K1通过三大协同组件构建端到端的知识编排流水线。首先，**KG层**设计了一个五模块模式的异构知识图谱架构：1）元数据/事实实体层，提供可验证的标准化论文元数据；2）文本提及实体层，提取方法、数据集、指标等显式科学对象并完成同义词消歧；3）隐式/抽象实体层，通过修辞角色标注和话语分析合成动机、发现、机制等高阶知识；4）引用关系层，编码支持/对比/扩展等论证意图与强度分数；5）知识关系层，构建BUILDS_ON、CAUSES等细粒度可查询三元组。其核心创新点是**语义锚点**设计——为每个多模态内容单元（图表、公式、段落）生成模态无关的抽象锚节点，作为跨模态交互的中介桥梁，避免直接跨模态实体对齐的脆弱性。

其次，**LLM层**训练了一个4B参数的小型信息抽取骨干模型，采用GRPO强化学习结合基于规则的奖励函数，确保大规模抽取的准确性和结构化输出。最后，**Agent CLI层**提供**三源代理接口**，统一整合网页搜索、多模态图谱检索和跨文档遍历三种工具，使研究代理能追溯证据来源、比较相关工作并在已有文献中验证新想法。

该流水线已处理246万篇跨六大学科的科学论文，构建了大规模知识图谱Scholar-KG，并开放了100万论文子集。实验证明在科学信息抽取、知识图谱构建和多跳科学推理任务上表现优异。

### Q4: 论文做了哪些实验？

论文在三个任务上评估了Agents-K1的性能。实验设置包括：使用自建的Scholar-KG数据集（来自2.46M论文，释放100万子集）和通用领域语料，对比了GPT-4o、Llama-3-8B等基线模型。

科学信息提取实验：在实体、关系、证据三元组识别上，Agents-K1的F1值达89.7%，比GPT-4o（73.2%）高16.5个百分点。知识图谱构建实验：在节点覆盖率和边预测准确率上，Agents-K1的完整图召回率为91.3%，比Llama-3-8B（68.4%）高22.9%。多跳科学推理实验：在Benchmark涵盖的"机制链追溯"和"证据融合"子任务中，Agents-K1的准确率分别为84.6%和79.2%，相比使用摘要的对比方法（平均62.1%和58.7%）显著提升。

消融实验显示：移除GRPO训练使F1下降9.4%，移除跨文档遍历接口使推理准确率下降15.8%。所有实验均使用6个学科的论文数据，并验证了Agent-native知识图谱相比扁平化cite图谱在支持复杂科学问题回答上的优势。

### Q5: 有什么可以进一步探索的点？

目前工作存在若干可探索的方向。第一，信息抽取的准确性仍有提升空间，特别是对长尾学科和跨学科术语的多模态解析，可探索引入领域自适应训练或基于大模型的协同验证机制。第二，知识图谱的演化动态性尚未被考虑，未来可构建时间感知的版本化图结构，追踪科学概念和证据链的演变过程。第三，推理端主要依赖图检索，可结合图神经网络的消息传递机制或路径排序算法，增强多跳推理中的逻辑一致性。第四，Agent接口当前为三源统一，但实际科学发现常需要假设验证闭环，可设计交互式假设生成与测试模块，让Agent主动提出实验方案并检索验证。第五，大规模图上的跨文档遍历存在计算瓶颈，可研究分层索引或可学习剪枝策略。此外，开放领域适应性实验中，不同模态证据的权重分配规则有待理论化。

### Q6: 总结一下论文的主要内容

Agents-K1旨在解决当前LLM研究代理在知识编排上的不足，即现有工作将论文简化为摘要和扁平引用，忽略了实体、证据、机制等关键科学要素。论文提出一个端到端的知识编排管道，将原始文档转化为智能体原生科学知识图谱。方法上，它整合了三个核心组件：一个覆盖全文的五模块多模态解析器，一个基于GRPO和规则奖励训练的4B参数信息抽取模型，以及一个统一网络搜索、多模态图谱检索和跨文档遍历的三源代理接口。利用该管道，论文处理了246万篇论文，构建了百万规模的Scholar-KG知识图谱。实验表明，Agents-K1在科学信息抽取、知识图谱构建和多跳推理任务上取得了优异性能，显著提升了研究代理的问答准确率。该工作的意义在于为研究代理提供了可审计、结构化的知识基础设施，奠定了从静态数据到可执行研究工具的基础。
