---
title: "ResearchPilot: A Local-First Multi-Agent System for Literature Synthesis and Related Work Drafting"
authors:
  - "Peng Zhang"
date: "2026-03-15"
arxiv_id: "2603.14629"
arxiv_url: "https://arxiv.org/abs/2603.14629"
pdf_url: "https://arxiv.org/pdf/2603.14629v1"
categories:
  - "cs.IR"
  - "cs.AI"
tags:
  - "Multi-Agent System"
  - "Literature Synthesis"
  - "Tool Use"
  - "Research Assistant"
  - "Systems Engineering"
  - "Local-First"
relevance_score: 7.5
---

# ResearchPilot: A Local-First Multi-Agent System for Literature Synthesis and Related Work Drafting

## 原始摘要

ResearchPilot is an open-source, self-hostable multi-agent system for literature-review assistance. Given a natural-language research question, it retrieves papers from Semantic Scholar and arXiv, extracts structured findings from paper abstracts, synthesizes cross-paper patterns, and drafts a citation-aware related-work section. The system combines FastAPI, Next.js, DSPy, SQLite, and Qdrant in a local-first architecture that supports bring-your-own-key model access and remote-or-local embeddings. This paper describes the system design, typed agent interfaces, persistence and history-search mechanisms, and the engineering tradeoffs involved in building a transparent research assistant. Rather than claiming algorithmic novelty, we present ResearchPilot as a systems contribution and evaluate it through automated tests and end-to-end local runs. We discuss limitations including external API rate limits, abstract-only extraction, incomplete corpus coverage, and the lack of citation verification.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决科研人员在文献综述阶段面临的高耗时和认知负担问题。研究背景是，进入新领域的研究者需要手动完成检索、阅读、归纳和写作等一系列复杂任务，而现有的大语言模型（LLM）虽然能辅助总结和起草，但通常采用“一次性提示”的方式，导致检索与推理过程模糊、中间证据不透明、合成主张的来源难以追溯，使得系统更像一个不透明的答案生成器，而非可审查的辅助工具。

现有方法的不足在于：单次提示的文献综述方法往往混淆了不同子任务（如检索、提取、综合和写作），缺乏结构化的中间输出，用户无法干预或验证过程，且系统通常依赖云端服务，在数据隐私和定制化方面存在限制。

本文要解决的核心问题是：如何设计一个透明、可审查、本地优先的多智能体系统，将文献综述分解为明确的阶段化流程，从而提供可追溯的中间结果，帮助研究者高效地从研究问题生成结构化的相关工作报告。具体而言，系统通过四个约束模块（论文检索、每篇论文的结构化提取、跨论文综合、引用感知的草稿生成）来实现这一目标，强调工程化实现中的可配置性、可自托管性以及过程的可视化，而非追求算法层面的创新。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为方法类、系统框架类和数据源/应用类。在方法层面，检索增强生成（RAG）通过检索外部上下文增强语言模型生成，是本文工作的基础范式。但ResearchPilot与之不同，它在检索和生成之间插入了结构化的提取与综合阶段，而非直接将检索文档输入最终提示。近期的大语言模型系统探索了多智能体任务分解，如AutoGPT和MetaGPT采用规划与执行分离的工作流。本文同样分解复杂任务，但采用了固定的顺序流水线，而非动态规划的智能体，这反映了文献综述任务结构相对稳定的特点。

在系统框架层面，LangChain和LlamaIndex提供了链接LLM调用、工具和检索组件的通用抽象。本文选择使用DSPy，因为其强调声明式签名和类型化字段描述，能自然地将智能体边界映射为结构化的输入输出契约，这契合了系统对透明度和可检查性的设计目标。

在数据源与应用层面，Semantic Scholar和arXiv提供了可访问的学术搜索基础。目前已有许多托管式文献综述工具，体现了市场对AI辅助文献分析的需求。然而，许多现有系统不暴露中间推理阶段或可编程的结构化输出。ResearchPilot则明确设计为一个开放、可审查、可自托管系统，以此与这些工具区分开来，贡献在于其系统实现与工程权衡。

### Q3: 论文如何解决这个问题？

论文通过构建一个本地优先、模块化的多智能体系统来解决文献综述自动化问题。其核心方法是一个由四个智能体组成的顺序处理流水线，每个智能体负责特定任务，并通过明确的接口和数据契约进行协作。

**整体框架与架构设计**：系统采用分层架构，包括Next.js前端、FastAPI后端、DSPy编排的四智能体流水线，以及由SQLite和Qdrant组成的持久化层。前端提交研究问题并接收实时执行状态流；后端负责流水线编排、事件流推送和报告持久化；持久化层不仅存储报告，还利用Qdrant向量数据库支持对历史报告的语义搜索。

**主要模块与关键技术**：
1.  **SearchAgent**：异步查询Semantic Scholar和arXiv，通过DOI或标题去重，并设计为容错机制，允许单一数据源因速率限制失败时仍能返回可用论文列表。
2.  **ExtractionAgent**：使用DSPy签名对每篇论文摘要进行独立处理，提取结构化的JSON输出，包括主张、方法、数据集、结果和局限性五个数组。此设计保持了较小的上下文窗口并支持细粒度进度报告。
3.  **SynthesisAgent**：整合所有提取结果，生成跨论文的综合分析，输出共识、矛盾和开放缺口三个字段，专注于识别跨文献的模式与分歧，而非独立总结单篇论文。
4.  **WriterAgent**：基于综合分析和参考文献列表，生成带有内联引用标签（如[R1]）的Markdown格式相关工作初稿，并自动生成参考文献映射部分。

**创新点与工程权衡**：
- **接口设计**：每个智能体实现为具有明确输入输出字段的DSPy模块或签名，围绕数据契约而非大型手写提示模板构建，便于更换模型提供商。
- **流式响应与实时反馈**：后端通过流式响应发射生命周期事件（如队列中、智能体开始、进度、完成），前端实时显示执行状态，提升了交互透明度和用户体验。
- **本地优先与灵活性**：支持自带API密钥的模型访问、远程或本地嵌入，以及运行时覆盖配置（如提供商、模型、API密钥），无需重启后端，增强了系统的可定制性和隐私控制。
- **持久化与历史搜索**：结合SQLite和Qdrant，不仅存储报告，还支持对历史运行结果进行语义检索，便于知识复用。

系统通过这种模块化、流式、契约驱动的设计，在透明度、可控性和工程实用性之间取得了平衡，旨在作为可自托管的研究辅助工具，而非追求算法层面的绝对新颖性。

### Q4: 论文做了哪些实验？

论文的实验主要围绕系统原型的功能验证和端到端运行测试展开，而非与传统方法进行性能比较。实验设置上，系统在本地环境中运行，使用FastAPI、Next.js、DSPy、SQLite和Qdrant构建，支持用户自带API密钥访问模型，并可选择远程或本地嵌入。数据集和基准测试方面，系统从Semantic Scholar和arXiv检索论文，但未使用标准基准数据集；测试查询包括检索增强生成、长文本事实性、扩散模型用于时间序列预测以及图神经网络用于分子属性预测等主题。对比方法方面，论文未与其他系统进行直接比较，而是通过自动化测试和端到端运行来评估系统自身功能。

主要结果包括：自动化测试覆盖了后端API流式传输、错误处理、报告搜索、配置安全、论文去重、嵌入模式选择等核心行为，共11项后端测试和1项前端测试通过。端到端运行中，一个关于“检索增强生成在问答中的近期趋势”的查询在12.47秒内成功完成，返回10篇论文、10项结构化提取结果、包含4个共识项、2个矛盾点和3个开放缺点的综合报告，以及2046字符的相关工作草稿；但其他查询因外部模型提供商的令牌速率限制而失败。关键数据指标包括：成功查询的完成时间（12.47秒）、检索论文数（10篇）、综合报告中的共识项（4个）、矛盾点（2个）和开放缺口（3个）。实验还识别了常见故障模式，如Semantic Scholar的HTTP 429速率限制、模型JSON输出异常等，并提供了相应的缓解措施，如部分故障容忍和本地嵌入回退。整体上，实验验证了系统的基本功能和鲁棒性，但强调了外部API限制对可靠性的影响。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在数据源、处理深度、验证机制和评估方法四个方面。未来可探索的方向包括：首先，扩展检索范围至PubMed、IEEE Xplore等专业数据库，并开发可插拔的领域适配器，以支持医学、工程等封闭文献库。其次，实现全文PDF解析，利用多模态技术提取图表、实验设置等关键信息，提升内容深度。再者，引入“声明验证智能体”，通过交叉引用核对或事实核查模型，确保生成内容与引文严格对应。此外，可设计增量学习机制，允许系统复用历史分析结果作为上下文，提高连续查询效率。从系统优化角度，可研究异步并发控制策略，平衡API调用速率与处理吞吐量。最后，需建立包含人工评估的基准测试集，量化生成文本的学术严谨性、结构连贯性及实用价值，推动此类工具从原型向可信研究助手演进。

### Q6: 总结一下论文的主要内容

论文提出并实现了一个名为ResearchPilot的开源、可自托管的多智能体系统，旨在辅助文献综述工作。其核心问题是解决传统单一、不透明的提示方法在文献综合和相关工作草拟中的局限性。方法上，系统将整个流程分解为搜索、提取、综合和草拟四个明确阶段，每个阶段由具有类型化接口的模块化智能体负责，并采用本地优先的架构，结合了FastAPI、Next.js、DSPy、SQLite和Qdrant等技术，支持用户自带API密钥和灵活的嵌入模型选择。主要结论是，这种透明、可分解的多阶段流水线设计，相较于单一黑箱模型，更易于检查、调试、持久化和扩展。论文的核心贡献并非算法创新，而是提供了一个注重可检查性和自托管能力的实用系统架构，为未来AI辅助文献分析研究奠定了有价值的基线。同时，论文也指出了系统在外部API速率限制、仅基于摘要提取、语料库覆盖不全以及缺乏引用验证等方面的局限性。
