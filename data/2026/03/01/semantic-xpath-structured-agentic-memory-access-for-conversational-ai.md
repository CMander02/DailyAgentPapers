---
title: "Semantic XPath: Structured Agentic Memory Access for Conversational AI"
authors:
  - "Yifan Simon Liu"
  - "Ruifan Wu"
  - "Liam Gallagher"
  - "Jiazhou Liang"
  - "Armin Toroghi"
date: "2026-03-01"
arxiv_id: "2603.01160"
arxiv_url: "https://arxiv.org/abs/2603.01160"
pdf_url: "https://arxiv.org/pdf/2603.01160v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Memory & Context Management"
  - "Tool Use & API Interaction"
relevance_score: 8.0
taxonomy:
  capability:
    - "Memory & Context Management"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "Semantic XPath"
  primary_benchmark: "N/A"
---

# Semantic XPath: Structured Agentic Memory Access for Conversational AI

## 原始摘要

Conversational AI (ConvAI) agents increasingly maintain structured memory to support long-term, task-oriented interactions. In-context memory approaches append the growing history to the model input, which scales poorly under context-window limits. RAG-based methods retrieve request-relevant information, but most assume flat memory collections and ignore structure. We propose Semantic XPath, a tree-structured memory module to access and update structured conversational memory. Semantic XPath improves performance over flat-RAG baselines by 176.7% while using only 9.1% of the tokens required by in-context memory. We also introduce SemanticXPath Chat, an end-to-end ConvAI demo system that visualizes the structured memory and query execution details. Overall, this paper demonstrates a candidate for the next generation of long-term, task-oriented ConvAI systems built on structured memory.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决面向任务的长期对话AI（ConvAI）系统中，如何高效、准确地访问和更新结构化记忆的问题。研究背景是，随着对话AI越来越多地支持长期、多任务（如旅行规划、待办事项管理）的交互，智能体需要维护结构化的记忆来保存对话历史、修订记录以及任务产物的层次化组织。然而，现有方法存在明显不足：传统的“上下文内记忆”方法简单地将不断增长的完整对话历史附加到模型输入中，这受限于上下文窗口长度，导致扩展性差、令牌成本高、延迟增加，并可能引发推理能力下降和幻觉输出；而基于检索增强生成（RAG）的方法虽然能检索与当前请求相关的信息，但大多将记忆视为扁平的条目集合进行检索，忽略了记忆内在的层次化结构，这可能导致检索结果不精确（例如，在旅行规划中，用户要求“在会议安排最满的那天增加一个咖啡休息时间”，扁平RAG可能错误地从其他天检索出会议相关活动）。

因此，本文要解决的核心问题是：如何设计一种能够感知语义和结构的记忆访问机制，以支持对结构化对话记忆进行高效、准确的检索与更新。为此，论文提出了Semantic XPath，一个树状结构的记忆模块，它采用一种类XPath的查询语言，能够结合语义相关性和结构匹配，精准地检索和更新记忆中的相关子结构，从而克服现有方法在扩展性、成本和准确性方面的局限。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕对话AI的记忆机制展开，可分为以下几类：

**1. 外部语料库记忆与对话记忆**：早期研究常将记忆视为静态的外部文档集合，独立于对话过程。本文则聚焦于**对话记忆**，强调记忆作为任务执行中的动态工作状态，会随交互不断更新，更具实时性和可变性。

**2. 扁平化与结构化对话记忆**：传统方法多将交互历史记录为扁平化的文本或压缩摘要。近期研究开始引入**结构化记忆**，通过层次化组织信息以支持多层级交互。本文延续结构化方向，但进一步区分了层次类型。

**3. 抽象层次与组合层次的结构化记忆**：现有结构化记忆多采用**抽象层次**，即高层单元是底层内容的概括性摘要。本文则专注于**组合层次**，其结构更贴合任务导向对话的自然层级（如行程→日期→活动），每一层存储独特信息，而非简单摘要，从而更精准地反映任务的内在逻辑。

与上述工作相比，本文提出的Semantic XPath不仅采用了组合层次的结构化记忆，还创新性地引入了类似XPath的查询机制，实现了对树状记忆的高效、精准访问与更新。这区别于仅进行检索的扁平化RAG方法，也避免了上下文窗口限制下历史记录无限追加的问题。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为Semantic XPath的新型树状结构化记忆模块来解决对话AI中长时、面向任务交互的记忆访问与更新问题。其核心方法是设计一种类似XPath的查询语言，能够智能地检索和操作结构化的对话记忆，从而克服传统上下文拼接方法受限于上下文窗口以及扁平化检索增强生成（RAG）方法忽略记忆结构性的缺陷。

整体框架基于一个根树结构来表示结构化对话记忆，其中每个节点对应一个对话状态单元，并带有节点类型和文本属性。架构设计主要包括三个关键部分：1）一个由对话和任务信息自然层次衍生的模式，用于规范节点类型和属性；2）Semantic XPath查询语言，它允许通过组合轴导航器、节点选择器、位置选择器和语义相关性运算符来精确表达复杂的记忆访问意图；3）一个递归评估函数，用于执行查询并维护一个带权重的节点集合，以支持高效的记忆检索与更新。

主要模块/组件包括：轴导航器（如“/”选择子节点，“//”选择后代节点）、节点选择器（指定具体节点类型或通配符）、位置选择器（用于按位置筛选）以及创新的语义相关性运算符。该运算符可以计算本地语义相关性（如节点属性与查询字符串的匹配度）或聚合语义相关性（如对子节点得分进行平均、最小、最大或几何平均等聚合操作），从而实现对记忆内容的语义感知检索。

创新点在于首次将XPath风格的结构化查询与语义相关性评分深度融合，使得系统不仅能利用记忆的层次结构进行高效导航，还能基于语义内容动态评分和筛选节点。例如，在查询“为会议安排密集的一天添加咖啡休息”时，系统可以通过计算每天下属POI节点与“会议”相关性的平均值，来识别会议活动最密集的那一天。这种方法在显著提升性能（较扁平RAG基线提升176.7%）的同时，极大减少了令牌使用量（仅需上下文记忆方法的9.1%），为实现下一代长时、任务导向的对话AI系统提供了可行的结构化记忆解决方案。

### Q4: 论文做了哪些实验？

论文在单轮和多轮对话设置下进行了实验，评估了Semantic XPath与两种基线方法（上下文记忆和扁平RAG）的性能。实验设置方面，使用了GPT-5 mini和Gemini-3 flash作为LLM后端；对于扁平RAG，使用了Qwen3-Embedding-8B嵌入模型；对于Semantic XPath，则测试了基于语义相似度（使用Qwen3-Embedding-8B）和基于蕴涵关系（使用facebook/bart-large-mnli）的两种语义相关性评分器。

数据集涵盖了三个涉及结构化长期记忆的对话AI场景：旅行行程（7天计划）、待办事项列表（5个类别）和膳食套件推荐（7天家庭计划）。每个领域都有特定的模式，并包含20个单轮对话和5个多轮对话的交互集。

主要评估指标是平均通过率（系统检索正确结构化数据并满足约束的输出所占比例）和每请求的LLM令牌使用量。关键结果如下：在单轮评估中，Semantic XPath的通过率与上下文记忆方法相当，两者均显著优于扁平RAG基线（后者因缺乏层次推理而表现不佳）。在令牌使用方面，上下文记忆方法所需的令牌量约为其他两种方法的5倍。具体而言，Semantic XPath仅需使用上下文记忆方法9.1%的令牌，同时性能比扁平RAG基线提高了176.7%。在多轮评估中，上下文记忆方法在需要访问历史记录的请求上通过率下降，且令牌使用量随对话轮数增加而稳步上升；而Semantic XPath通过过滤无关信息，保持了接近单轮设置的通过率和稳定的令牌消耗。

### Q5: 有什么可以进一步探索的点？

本文提出的Semantic XPath在结构化记忆访问方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，论文实验主要集中于行程规划等特定任务导向场景，其方法在更开放、动态的多轮对话（如情感支持、创意协作）中的泛化能力有待验证。其次，当前树状结构可能无法充分捕捉对话中复杂的交叉引用和网络化关系，未来可探索图神经网络等更灵活的结构表示。此外，记忆的更新机制仍依赖预设规则，如何实现更自适应、基于对话语义的动态结构演化是一个关键挑战。从系统优化角度看，查询生成与执行的效率在极大规模记忆下可能成为瓶颈，需研究近似检索或索引优化技术。最后，将此类结构化记忆与世界知识、用户画像进行深度融合，构建更具人格化和上下文感知的智能体，是通向下一代对话系统的有前景的路径。

### Q6: 总结一下论文的主要内容

本文针对支持长期、任务导向交互的对话AI（ConvAI）系统，提出了结构化记忆访问方法Semantic XPath。现有方法存在局限：上下文记忆因窗口限制而扩展性差；基于检索增强生成（RAG）的方法多假设记忆为扁平集合，忽略了任务中常见的层次化结构。为此，作者将记忆组织为树形结构，并设计了一种类似XPath的查询语言，该语言结合语义相关性评分与结构匹配，能精准检索和更新记忆中的相关子结构。实验表明，该方法性能比扁平RAG基线提升176.7%，且仅需上下文记忆方法9.1%的令牌量。论文还展示了一个端到端的演示系统SemanticXPath Chat，可视化结构化记忆与查询执行过程。这项工作为构建基于结构化记忆的下一代长期任务型对话AI系统提供了有力候选方案。
