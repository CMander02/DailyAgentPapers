---
title: "Don't Retrieve, Navigate: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG"
authors:
  - "Yiqun Sun"
  - "Pengfei Wei"
  - "Lawrence B. Hsieh"
date: "2026-04-16"
arxiv_id: "2604.14572"
arxiv_url: "https://arxiv.org/abs/2604.14572"
pdf_url: "https://arxiv.org/pdf/2604.14572v1"
categories:
  - "cs.IR"
  - "cs.AI"
  - "cs.CL"
  - "cs.MA"
tags:
  - "Agent Architecture"
  - "Retrieval-Augmented Generation (RAG)"
  - "Knowledge Navigation"
  - "Enterprise QA"
  - "Hierarchical Planning"
  - "Document Corpus Distillation"
  - "Agentic RAG"
relevance_score: 8.5
---

# Don't Retrieve, Navigate: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG

## 原始摘要

Retrieval-Augmented Generation (RAG) grounds LLM responses in external evidence but treats the model as a passive consumer of search results: it never sees how the corpus is organized or what it has not yet retrieved, limiting its ability to backtrack or combine scattered evidence. We present Corpus2Skill, which distills a document corpus into a hierarchical skill directory offline and lets an LLM agent navigate it at serve time. The compilation pipeline iteratively clusters documents, generates LLM-written summaries at each level, and materializes the result as a tree of navigable skill files. At serve time, the agent receives a bird's-eye view of the corpus, drills into topic branches via progressively finer summaries, and retrieves full documents by ID. Because the hierarchy is explicitly visible, the agent can reason about where to look, backtrack from unproductive paths, and combine evidence across branches. On WixQA, an enterprise customer-support benchmark for RAG, Corpus2Skill outperforms dense retrieval, RAPTOR, and agentic RAG baselines across all quality metrics.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决传统检索增强生成（RAG）系统在处理复杂查询时存在的结构性局限。研究背景是，企业知识库通常包含大量异构文档，传统RAG通过向量检索获取相关片段来增强大语言模型（LLM）的生成，虽然能减少幻觉，但将LLM视为检索结果的被动消费者。现有方法的不足在于：传统RAG采用扁平化检索，LLM无法感知知识库的整体组织结构，难以回溯或整合分散的证据；而现有的代理式RAG或层次化方法（如RAPTOR）虽允许迭代搜索或构建摘要层次，但在查询时仍依赖嵌入相似性搜索，其层次结构对LLM不可见，导致代理在探索时缺乏“地图”指引，只能盲目猜测搜索词。本文要解决的核心问题是：如何让LLM主动、有结构地探索整个知识库，而非被动接收检索结果。为此，论文提出了Corpus2Skill框架，其核心思想是将知识库“编译”成一个可导航的技能层次结构，使LLM能像人类浏览文件系统一样，通过概览、深入、回溯等方式主动导航，从而系统性地定位和整合证据，以更有效地回答涉及多主题的复杂查询。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 基于聚类的文档组织方法**：Scatter/Gather 提出了通过预计算的聚类组织进行导航的范式，而非依赖相似性匹配。与需要用户手动交互选择聚类的 Scatter/Gather 不同，本文的 Corpus2Skill 将导航任务完全委托给 LLM 智能体，由其根据各级聚类摘要进行自主推理。

**2. 用于检索的分层摘要方法**：RAPTOR 通过递归聚类和摘要将文本块组织成树状结构进行检索。本文与之共享了“嵌入-聚类-摘要”的离线编译循环，但关键区别在于将层次结构物化为可导航的文件，并用智能体导航取代了固定的遍历检索。GraphRAG 和 HiRAG 等方法则构建了知识图谱，需要在服务时依赖图数据库或图检索，而本文采用基于文件的导航。

**3. 检索增强生成（RAG）及其变体**：传统 RAG 及其改进方法（如 Self-RAG、IRCoT）侧重于优化检索过程或让模型参与检索决策。本文则采取了不同的路径：它并非改进检索，而是用智能体在预编译的层次结构上进行文件导航，完全取代了基于嵌入向量的搜索。

**4. 结构感知与智能体驱动的 RAG**：StructRAG、BookRAG、A-RAG、SPD-RAG、NaviRAG、HCAG 等方法都尝试在推理时引入结构化视图或多智能体协作，以增强 RAG 的推理能力。它们的共同点是**在服务时仍保留某种形式的检索或搜索基础设施**。本文的核心区别在于，它将层次结构物化为静态的技能文件系统，并让单个智能体通过文件浏览和文档查找（而非向量搜索）进行确定性导航。

**5. 工具使用智能体与技能构建**：本文借鉴了 Toolformer 和 ReAct 等研究的工具使用范式，但将其应用于特定的、只读的文件浏览工具。在技能构建方面，Voyager、SkillX 等方法是从智能体行动轨迹中提炼技能，而本文是从文档语料库通过聚类和摘要生成技能，输入模态根本不同。

**总结而言**，本文与相关工作的核心关系是借鉴了分层聚类、智能体导航等思想，但其根本区别在于提出了一种**完全基于文件系统导航、无需在线检索**的新范式，通过将知识库预编译为可导航的技能目录，实现了更可控、可解释的智能体问答过程。

### Q3: 论文如何解决这个问题？

论文通过提出Corpus2Skill框架来解决传统RAG系统中LLM被动消费检索结果、缺乏对知识库整体结构和未检索内容可见性的问题。其核心方法是将文档知识库离线编译成可导航的技能树，并在在线服务时让LLM智能体主动导航该结构，从而将不透明的检索过程转变为透明、可引导的探索过程。

整体框架分为离线编译和在线服务两个阶段。在编译阶段，系统通过四个步骤构建层次化的技能森林：首先对文档进行嵌入表示；接着通过迭代的层次化聚类（使用K-Means算法）构建多级簇结构，并在每一级利用LLM生成描述该簇主题覆盖范围、可回答问题类型及关键术语的摘要；然后为每个非叶节点生成简短的文件系统安全标签；最后将层次结构物化为专为智能体导航设计的文件系统。其中，根簇对应顶级技能目录（包含skill.md文件），子簇对应子目录（包含index.md文件），而完整文档则存储于外部的文档库中，通过文档ID引用。这种导航元数据与文档内容的分离是关键架构设计，使得导航文件保持小巧，显著降低了智能体每一步的令牌开销。

在线服务阶段，智能体借助两个工具进行导航：code_execution（用于浏览skill.md和index.md文件）和get_document（用于按ID检索完整文档）。智能体以渐进式披露的方式工作：初始时仅预加载技能名称和简短描述，获得知识库的鸟瞰图；然后根据查询，自主选择并深入相关技能分支，逐级阅读更精细的摘要文件，最终定位并检索具体的文档来生成答案。

该方法的创新点主要体现在：1) **将知识库结构显式化**：通过离线构建的层次化技能树，使智能体在推理时能“看到”知识库的整体组织，从而能够进行有依据的路径选择、从无效路径回溯以及跨分支证据整合。2) **导航驱动的交互范式**：用智能体的主动导航替代了黑盒检索函数，赋予了模型对信息寻找过程的控制权和可见性。3) **高效的令牌利用**：通过摘要文件和完整文档的分离，以及渐进式披露机制，智能体可以低成本地扫描大量文档摘要，仅在必要时才调用高成本的完整文档读取，优化了资源使用。这些设计共同使系统在保持答案依据性的同时，提升了推理的灵活性和效率。

### Q4: 论文做了哪些实验？

论文在WixQA企业客户支持问答基准上进行了实验评估。实验设置方面，作者将提出的Corpus2Skill方法与多种基线方法进行了对比。数据集使用Wix知识库构建的WixQA，包含6,221篇支持文章，评估集为200个专家编写的问题。对比方法涵盖了三种检索范式：稀疏检索（BM25）、稠密检索（使用Qwen3-Embedding-0.6B模型和FAISS索引）、混合检索（BM25与稠密检索的 Reciprocal Rank Fusion）、分层树检索方法RAPTOR，以及一个具有迭代访问多种检索工具能力的智能体基线（Agentic）。评估指标包括词法重叠指标（Token F1、BLEU、ROUGE-1、ROUGE-2）和LLM评判指标（事实性Factuality、上下文召回率Context Recall），同时统计了输入令牌使用量和每查询成本。

主要结果显示，Corpus2Skill在所有质量指标上均取得最佳性能。具体关键数据为：Token F1达到0.460，相比智能体基线（0.388）提升19%，相比稠密检索（0.363）提升27%；事实性得分为0.729，高于智能体基线（0.724）和RAPTOR（0.675）；上下文召回率为0.652，显著优于RAPTOR（0.616）和智能体基线（0.481）。这些结果表明基于导航的方法能更有效地定位相关内容。然而，Corpus2Skill的每查询成本为0.172美元，输入令牌约53,487个，成本较高，主要源于导航文件内容被包含在每次API调用中。消融实验探讨了聚类结构、智能体探索预算和服务LLM选择的影响，发现较窄的分支比（p=5）能略微提升质量，探索预算对质量影响较小，而使用更便宜的模型（Claude Haiku）可将成本减半至0.088美元/查询，且上下文召回率提升至0.705，展现了可行的成本-质量权衡。

### Q5: 有什么可以进一步探索的点？

基于论文的局限性分析，未来研究可以从以下几个方向深入探索：

**成本优化与架构改进**：当前方法因每次调用都需载入导航文件内容，导致输入令牌成本较高。未来可探索更高效的上下文管理机制，例如动态加载部分层级摘要，或开发轻量级索引结构。结合提示缓存与会话级复用策略，能显著降低高频查询场景的开销。此外，可研究将技能目录压缩为向量表示，在保持导航能力的同时减少令牌占用。

**聚类与路由机制的增强**：论文指出“硬单路径聚类”是主要错误来源，文档的多主题特性导致路由瓶颈。未来可探索软聚类或多父节点分配方案，允许文档出现在多个分支，通过元数据或交叉引用链接来避免内容冗余。也可引入强化学习，让智能体在导航过程中动态调整路径选择，结合用户反馈优化路由准确性。

**系统扩展性与实时更新**：当前框架受限于技能API的文件数与大小约束，且不支持增量更新。未来需设计可伸缩的分层架构，例如引入分布式技能存储或动态子树加载。编译流程可改进为增量式，通过局部重聚类与摘要更新来降低文档增删时的重新编译成本，这对企业知识库的持续演进至关重要。

**多模态与跨领域泛化**：当前工作聚焦文本QA，未来可将导航框架扩展至多模态知识（如图表、代码库），让智能体在异构数据中跨模态检索。此外，在不同领域（如学术文献、医疗指南）验证方法的通用性，并探索与工具调用、工作流自动化等智能体能力的结合，以支持更复杂的决策任务。

### Q6: 总结一下论文的主要内容

这篇论文提出了Corpus2Skill方法，旨在解决传统检索增强生成（RAG）将大语言模型（LLM）视为检索结果被动消费者的问题。传统RAG限制了模型理解语料库组织结构、回溯或整合分散证据的能力。

论文的核心贡献是设计了一种将企业文档语料库离线编译成可导航技能目录的新范式。该方法通过迭代聚类文档、在每一层级生成LLM撰写的摘要，最终构建出一个树状结构的可导航技能文件目录。在服务时，智能体能够获得语料库的全局视图，通过逐层细化的摘要深入主题分支，并根据ID检索完整文档。

主要结论显示，在WixQA企业客户支持基准测试中，Corpus2Skill在各项质量指标上均优于密集检索、RAPTOR和智能体RAG基线方法。其意义在于通过显式的层次结构，使智能体能够主动推理搜索路径、从无效路径回溯并跨分支整合证据，从而更有效地利用企业知识进行问答和RAG任务。
