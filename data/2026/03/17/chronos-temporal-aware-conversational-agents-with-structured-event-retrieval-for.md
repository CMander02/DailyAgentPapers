---
title: "Chronos: Temporal-Aware Conversational Agents with Structured Event Retrieval for Long-Term Memory"
authors:
  - "Sahil Sen"
  - "Elias Lumer"
  - "Anmol Gulati"
  - "Vamse Kumar Subbiah"
date: "2026-03-17"
arxiv_id: "2603.16862"
arxiv_url: "https://arxiv.org/abs/2603.16862"
pdf_url: "https://arxiv.org/pdf/2603.16862v1"
categories:
  - "cs.CL"
tags:
  - "Agent Memory"
  - "Long-Term Memory"
  - "Temporal Reasoning"
  - "Structured Retrieval"
  - "Event Representation"
  - "Tool Use"
  - "Multi-Hop Reasoning"
  - "Conversational Agent"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# Chronos: Temporal-Aware Conversational Agents with Structured Event Retrieval for Long-Term Memory

## 原始摘要

Recent advances in Large Language Models (LLMs) have enabled conversational AI agents to engage in extended multi-turn interactions spanning weeks or months. However, existing memory systems struggle to reason over temporally grounded facts and preferences that evolve across months of interaction and lack effective retrieval strategies for multi-hop, time-sensitive queries over long dialogue histories. We introduce Chronos, a novel temporal-aware memory framework that decomposes raw dialogue into subject-verb-object event tuples with resolved datetime ranges and entity aliases, indexing them in a structured event calendar alongside a turn calendar that preserves full conversational context. At query time, Chronos applies dynamic prompting to generate tailored retrieval guidance for each question, directing the agent on what to retrieve, how to filter across time ranges, and how to approach multi-hop reasoning through an iterative tool-calling loop over both calendars. We evaluate Chronos with 8 LLMs, both open-source and closed-source, on the LongMemEvalS benchmark comprising 500 questions spanning six categories of dialogue history tasks. Chronos Low achieves 92.60% and Chronos High scores 95.60% accuracy, setting a new state of the art with an improvement of 7.67% over the best prior system. Ablation results reveal the events calendar accounts for a 58.9% gain on the baseline while all other components yield improvements between 15.5% and 22.3%. Notably, Chronos Low alone surpasses prior approaches evaluated under their strongest model configurations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长期对话智能体中，记忆系统难以对跨越数月、随时间演变的时序性事实和用户偏好进行推理，以及缺乏对长对话历史中多跳、时间敏感查询的有效检索策略的问题。

研究背景是，随着大语言模型的发展，对话智能体已能进行持续数周或数月的多轮交互。现有方法主要分为两类：一类是构建全面的知识图谱，在信息摄入时提取所有事实和关系，并整合时间元数据，但这会导致知识库庞大，且在查询仅需部分信息时产生开销和上下文熵；另一类是更简单的轮次级检索方法，直接对对话轮次进行混合搜索，避免了上述开销，但缺乏结构化的时间表示，难以处理涉及日期计算或跨会话事件聚合的时间敏感查询。此外，近期系统引入了通过离线“推理”生成衍生事实和模式的背景推理管道，但这些与查询无关的推导在知识不相关时也会引入噪声。

现有方法的不足在于，全面的记忆构建会因过度结构化而引入开销和噪声，而纯粹的轮次级检索又缺乏时序基础以支持时间敏感推理。没有现有方法能实现以查询为条件的选择性提取，即仅结构化与回答特定问题相关的时序信息，同时保留对话上下文以进行语义理解。

本文要解决的核心问题是：设计一个既能保持检索简单性，又能进行选择性时序事件提取的对话记忆框架，以精确支持对长期对话历史中时序信息的推理和检索。为此，论文提出了Chronos框架，它将原始对话分解为带有解析日期时间范围和实体别名的“主-谓-宾”事件元组，并将其与保留完整对话上下文的轮次日历一同索引在结构化的事件日历中。在查询时，通过动态提示生成定制的检索指导，引导智能体决定检索内容、跨时间范围过滤以及通过迭代工具调用进行多跳推理，从而实现对时序信息的精准、高效利用。

### Q2: 有哪些相关研究？

相关研究主要围绕对话记忆的四个主题展开：短期与长期记忆的区分、知识积累策略、检索架构以及摘要与事实提取。本文与这些工作的关系和区别如下：

**1. 记忆类型与评测基准**：现有研究区分了短期（会话内）和长期（跨会话）记忆。长期记忆的评测基准如LongMemEvalS和LoCoMo，但它们在评估知识更新和时序推理方面存在局限，且未专门考察时序结构的作用。Chronos则通过结构化的事件日历和时序解析，直接针对跨会话的时序推理进行优化。

**2. 知识表示方法**：相关工作在知识表示上分为结构化（如知识图谱）和非结构化（如原始对话或摘要）两类，或采用混合方法。这些方法通常在信息摄入时预计算表示，可能无法适应查询时的具体需求。Chronos的创新在于**选择性结构化**：仅将时序事件分解为主题-动词-对象元组并解析时间范围，同时保留原始对话上下文，实现了时序精准检索与语义灵活查询的平衡。

**3. 检索架构**：现有检索技术包括稀疏检索（如BM25）、密集检索及其混合方法，并发展了查询重写、分解等预处理技术。更先进的系统采用智能体驱动的检索（Agentic RAG），通过工具调用进行多步推理。然而，这些架构缺乏对检索策略的**查询条件化适应**，即不同查询（如时序过滤、多跳推理）可能需不同检索方式。Chronos通过动态提示生成定制的检索指导，针对每个问题决定检索内容、时间过滤方式和多跳推理步骤，实现了检索策略的灵活适配。

**4. 信息压缩技术**：相关方法包括摘要（如递归摘要、基于事件的表述）和事实提取（如实体关系三元组、带时间戳的观察）。多数系统在摄入时进行提取，与查询无关。Chronos同样在摄入时进行结构化提取，但其独特之处是**专注于时序事件**的提取和索引，而非全面提取所有事实，从而在保持精度的同时减少了信息冗余。

总之，Chronos通过引入时序感知的结构化事件日历与动态检索指导，填补了现有工作在**显式时序表示**和**查询自适应检索**方面的空白，在长期对话记忆任务上取得了显著性能提升。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Chronos的、具有时间感知能力的记忆框架来解决长期对话中时间推理和检索的难题。其核心方法是构建一个双日历（事件日历和对话轮次日历）的混合结构化记忆系统，并采用动态提示生成与工具调用循环相结合的智能检索策略。

整体框架包含四个主要组件：
1.  **事件提取流水线**：从原始对话中识别具有时间戳的事件，将其分解为〈主体-动词-客体〉三元组。关键创新在于**多分辨率时间归一化**，将自然语言时间表达（如“上个月”）转换为精确的ISO 8601时间范围（开始和结束时间），而非单点估计，从而支持精确的时间过滤。此外，系统为每个事件生成2-4个使用完全不同词汇的**词汇别名**（如将“买了Fitbit”改写为“买了一个健身追踪器”），以提升基于文本检索的召回率。

2.  **动态提示系统**：针对每个用户查询，使用一个小型高效的LLM分析问题结构，生成定制的**检索指导**。该指导以指令形式（如1-5个要点）明确告诉代理需要检索什么信息、如何进行时间过滤以及采取何种推理模式。这取代了静态提示或分类器，使系统能灵活适应从时间过滤到偏好回忆等多样化的长期记忆查询。

3.  **初始检索阶段**：在代理开始工具推理前，首先从**对话轮次日历**中为查询提供语义相关的上下文。该阶段采用三阶段流水线：基于向量的**稠密检索**获取Top-100候选对话轮次；使用交叉编码器进行**重排序**以提升相关性；最后对选中的Top-15轮次进行**上下文扩展**（包含前后各一轮对话），并按会话日期组织成层次化的自然语言块，为代理提供丰富的背景信息。

4.  **Chronos代理**：这是一个具备原生工具调用能力的LLM代理，遵循ReAct（推理-行动）模式进行迭代推理。代理可以调用针对两个日历的**向量搜索工具**和**基于grep的文本搜索工具**。代理能够根据动态提示和已有上下文，决定是直接回答、调用工具进行语义检索，还是使用grep进行精确关键词匹配。通过工具调用的循环，代理可以逐步收集信息，执行跨时间范围过滤、交叉引用事件与原始对话等多跳推理。

创新点在于：
*   **选择性结构化**：仅对时间敏感的事件进行结构化（存入事件日历），同时保留完整的原始对话（存入对话轮次日历），在结构化开销与语义完整性间取得平衡。
*   **时间范围编码与别名生成**：增强了事件在时间维度和表述多样性上的可检索性。
*   **查询特定的动态检索指导**：使代理的检索行为能根据问题动态调整，无需为不同问题类型预设模板。
*   **混合检索与迭代工具调用**：结合了基于向量的语义检索、精确关键词匹配以及代理驱动的、可约束时间范围的迭代搜索，共同实现了对长期、多跳、时间敏感查询的可靠推理。

### Q4: 论文做了哪些实验？

论文在LongMemEval基准测试上进行了全面实验，该基准包含500个问题，涵盖知识更新追踪（KU）、多轮会话聚合（MS）、单轮会话助理回忆（SSA）、单轮会话偏好回忆（SSP）、单轮会话用户回忆（SSU）和时序推理（TR）六个类别。实验设置包括两种配置：Chronos Low使用GPT-4o作为生成模型，以公平对比现有系统；Chronos High使用Claude Opus 4.6以探索更高模型能力下的性能。对比方法包括EmergenceMem Internal、Honcho、Mastra、Zep、Supermemory和Hindsight等最先进的会话记忆系统。

主要结果显示，Chronos Low在整体准确率上达到92.60%，较最佳基线系统EmergenceMem Internal（86%）提升7.67%，并在KU（96.15%）、MS（91.73%）和TR（90.23%）等类别上取得显著优势。Chronos High整体准确率进一步提升至95.60%，在KU、SSA和SSP类别达到100%准确率。消融实验表明，事件日历对性能贡献最大，在Chronos Low配置下移除事件索引导致准确率下降34.5个百分点（从93.1%降至58.6%），占总增益的58.9%；动态提示、初始检索、重排序和日期过滤等其他组件分别带来15.5%至22.3%的性能提升。关键数据指标包括：Chronos Low在MS类别相对Honcho提升7.97%，在TR类别较基线提升4.52%；Chronos High在SSP类别从Chronos Low的80%提升至100%。实验验证了结构化事件检索与时间感知机制在长期对话记忆任务中的有效性。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于存储开销、离线计算成本和查询时的推理复杂度。未来研究可以从以下几个方向深入：首先，探索更高效的混合索引结构，例如将事件与对话轮次在统一向量空间中进行联合编码，或采用可学习的压缩表示来降低存储需求。其次，事件提取的准确性和效率是关键，可研究轻量级专用模型或迭代式提取方法，在保证时序关系解析精度的同时减少对大型模型的依赖。此外，检索策略可进一步优化，例如引入时序感知的检索排序机制，或开发自适应检索路径规划，使智能体能动态决定何时查询事件日历、何时回溯完整对话。最后，本文框架尚未充分探索用户偏好和情感的动态演化，未来可考虑将情感状态或意图变化也建模为时序事件，从而提升长期对话的个性化与连贯性。

### Q6: 总结一下论文的主要内容

本文针对长期对话中现有记忆系统难以处理时间敏感查询和动态偏好演化的问题，提出了Chronos框架。其核心贡献是设计了一种双日历结构：事件日历将原始对话分解为带明确时间范围的主谓宾事件元组并进行结构化索引，而轮次日历则保留完整的对话上下文。在查询时，系统通过动态提示生成检索指导，引导智能体在双日历上进行迭代式工具调用，以执行跨时间过滤和多跳推理。实验表明，Chronos在LongMemEvalS基准测试中达到了92.60%至95.60%的准确率，显著优于先前最佳系统7.67%，尤其在多会话聚合和时间推理任务上表现突出。结论指出，该方法证明了无需构建完整知识图谱，仅通过结构化细粒度时间事件并保留对话上下文，即可实现高精度的长期记忆，为持续对话智能体提供了有效解决方案。
