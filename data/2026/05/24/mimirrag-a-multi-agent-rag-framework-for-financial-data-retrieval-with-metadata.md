---
title: "MimirRAG: A Multi-Agent RAG Framework for Financial Data Retrieval with Metadata Integration"
authors:
  - "Magnus Samuelsen"
  - "Wilmer Nyström"
  - "Somnath Mazumdar"
  - "Mansoor Hussain"
  - "Mikkel Strange"
date: "2026-05-24"
arxiv_id: "2605.25030"
arxiv_url: "https://arxiv.org/abs/2605.25030"
pdf_url: "https://arxiv.org/pdf/2605.25030v1"
categories:
  - "cs.LG"
tags:
  - "多智能体RAG"
  - "金融领域Agent"
  - "Agent工作流"
  - "元数据集成"
  - "查询规划"
relevance_score: 7.5
---

# MimirRAG: A Multi-Agent RAG Framework for Financial Data Retrieval with Metadata Integration

## 原始摘要

Retrieval-augmented generation (RAG) systems offer a promising approach to reduce hallucinations and improve answer accuracy in large language models (LLMs), a requirement for reliable, financial analysis where answers must be grounded in verifiable evidence from filings rather than generated from model priors. However, designing RAG systems that extract meaningful insights from mixed financial documents and integrate into analyst workflows remains challenging. This paper introduces MimirRAG (Metadata-Integrated Multi-Agent Information Retrieval), a multi-agent RAG system developed iteratively to address these challenges. MimirRAG features a modular pipeline encompassing structure-preserving parsing of PDF filings, table-aware chunking, metadata extraction, agent-based retrieval with query planning and hybrid search, validation, and context-aware generation with numerical reasoning support. Our ablation study identifies three key technical enablers for effective financial RAG: metadata integration, table-aware chunking, and an agentic workflow. MimirRAG was evaluated quantitatively using FinanceBench and qualitatively through expert validation with four financial analysts. The system achieved 89.3% accuracy on FinanceBench, outperforming the original benchmark baselines. Expert feedback highlighted that successful deployment also requires calibrated trust, comprehensive data integration, and user personalization. We conclude that combining multi-agent RAG architecture with human-centric design principles can improve the extraction of meaningful insights in financial analysis.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在金融分析领域应用大语言模型（LLM）时面临的核心挑战：**如何构建一个能够从混合型金融文档中提取可验证的洞察，并有效融入分析师工作流程的检索增强生成（RAG）系统**。

研究背景指出，虽然LLM在金融领域潜力巨大，但其在财务分析中会产生“幻觉”（即生成无依据或不准确的内容），这在金融领域可能造成严重的声誉、经济损失甚至法律后果。现有的RAG系统研究大多侧重于优化检索技术（如嵌入模型、分块策略），但忽略了两个关键不足：1）对金融数据中**元数据**（如公司名、报告类型、日期）的系统性利用不足，导致检索精度受限；2）缺乏从**金融分析师视角**出发的评估和设计，不了解用户如何感知和接纳这类系统。

因此，本文提出并开发了MimirRAG，这是一个多智能体RAG框架。其核心要解决的问题是：**如何通过整合元数据和设计模块化的多智能体工作流，提高RAG系统在金融问答任务（如事实查找、跨期对比、比率计算）上的准确性和可用性**。具体而言，它解决了如何在保留PDF文档结构（如表格、层级）的同时进行高效分块、检索与验证，并最终通过人工专家评估来揭示技术性能之外，影响系统成功部署的关键因素（如校准信任、数据集成和个性化）。

### Q2: 有哪些相关研究？

相关研究主要集中在以下三类：一是早期金融NLP的微调模型，如FinBERT、BloombergGPT、FinGPT及多智能体FinRobot，它们通过领域自适应提升性能，但未转向RAG架构。二是RAG系统各组件优化研究：包括嵌入模型测试（Iaroshev等）、元素级分块策略（Yepes等）、查询扩展与重排序（Lee等）、混合检索（Sarmah等结合向量与知识图谱）、元数据过滤（Sarmah等）等，但这些工作多聚焦单环节，缺乏对元数据在完整流程中系统整合的探索。表中大量工作（如Kim等、Setty等）明确未测试元数据影响或存在表格处理弱、计算成本高等局限。三是面向金融应用的多智能体RAG系统，如Chen等的混合智能体框架和FinRobot，它们虽通过多智能体协作模拟分析师流程，但缺乏针对真实分析师工作流的端到端评测与用户验证。

本文与这些工作的关键区别在于：1）首次将元数据（公司、日期、财政年度等）作为系统化组件贯穿RAG全流程（从解析分块到检索生成），而非仅用于过滤；2）在FinanceBench上完成端到端量化评估，并引入四位金融分析师进行质性专家验证，弥补现有研究缺乏专业用户反馈的空白；3）采用模块化多智能体架构，集成分块、混合搜索、验证与数值推理，在金融数据检索中达到89.3%准确率，优于原基准。

### Q3: 论文如何解决这个问题？

MimirRAG通过一个五智能体模块化流水线解决金融文档RAG的挑战：Extractor、Planner、Search、Validator和Writer，分为预检索、检索和后检索三个阶段。

**核心方法**是一个分层混合检索流程。预检索阶段首先使用Docling（集成DocLayNet布局分析、TableFormer表格提取和OCR）将PDF解析为保留标题、章节和表格的Markdown结构，然后采用Chonkie进行递归分块，并实现表格感知分块（当分块以表格行结尾时与下一块合并，最大3600字符）以保持表格完整性。接着Extractor智能体从文档前1024个token提取结构化元数据（标题、公司名、关键词、摘要、日期、报告类型），公司名通过本地FTS和SEC EDGAR/CVR API标准化。文档级和分块级嵌入（snowflake-arctic-embed-m v2.0）与BM25索引存储在LanceDB中。

检索阶段采用**智能体驱动的工作流**：Planner智能体将复杂查询分解为子问题（如将利润变化拆分为各年利润和差值查询）；Search智能体对每个子问题并行执行混合搜索，先应用元数据过滤器（公司、日期、报告类型）缩小文档范围，然后进行密集检索（k-NN）和稀疏检索（BM25 FTS），结果通过互惠排名融合（RRF）合并。Validator智能体验证分块相关性，无效时最多三次重试并重新规划查询。后检索阶段中，Writer智能体将验证后的分块按报告分组并标注来源，结合元数据和精度导向提示模板生成带内联引用的答案。

**架构创新**在于：松耦合智能体设计支持独立调优和并行执行；元数据集成实现分层过滤减少语义歧义；表格感知分块保留数值上下文；Pydantic模型确保智能体间类型安全的结构化通信和自动故障恢复。

### Q4: 论文做了哪些实验？

论文对MimirRAG系统进行了定量和定性两类实验。在定量实验中，使用FinanceBench作为基准数据集，MimirRAG系统取得了89.3%的准确率，显著超过了该基准的原始基线性能。实验通过消融研究（Ablation Study）识别出三个关键技术使能器：元数据整合（metadata integration）、表格感知分块（table-aware chunking）和智能体工作流（agentic workflow）。在定性实验中，邀请了四位金融分析师进行专家验证（expert validation），收集了关于系统部署的反馈意见。专家反馈指出，成功的部署还需要三个关键因素：校准的信任度（calibrated trust）、全面的数据集成（comprehensive data integration）以及用户个性化（user personalization）。这些实验共同验证了MimirRAG在多智能体RAG架构与以人为中心的设计原则结合后，能够有效提升金融分析中深层洞察的提取能力。

### Q5: 有什么可以进一步探索的点？

未来的探索可从以下几个方向展开：首先，当前元数据主要依赖人工定义规则提取，未来可引入自动化的元数据学习机制，适应不同文档结构的动态变化。其次，多智能体协作中的查询规划仍较保守，可通过强化学习优化智能体间的通信策略，提升对复杂财务问题的分解能力。此外，表格感知的切片策略在数值推理上存在局限，可结合图神经网络建模表格行/列间的语义关系，增强跨表格的数值合理解析。在评估方面，现有FinanceBench测试集覆盖范围有限，需构建包含多语言财报及非结构化附注的基准。专家反馈中提到的用户个性化需求也值得关注，例如构建可调节的信任校准接口，根据分析师风险偏好动态调整检索严谨度。最后，当前系统未考虑时间衰减效应，未来可集成事件驱动的时间线推理，防止过时数据影响决策质量。

### Q6: 总结一下论文的主要内容

MimirRAG是一个面向金融数据检索的多智能体RAG框架，旨在解决大语言模型在金融分析中的幻觉和信息过载问题。该框架通过结构化保留的PDF解析、表格感知分块、元数据提取、基于智能体的查询规划与混合检索、验证以及支持数值推理的上下文生成等模块化流程，实现了对混合金融文档的高效检索与分析。系统在FinanceBench基准上达到了89.3%的准确率，显著优于原始基线。通过消融实验，论文识别出元数据集成、表格感知分块和智能体工作流是金融RAG的三个关键技术要素。此外，从四名金融分析师的专家验证中，论文提炼出五个设计原则，并强调成功部署还需考虑校准信任、全面数据集成和用户个性化三个因素。该工作的核心贡献在于将多智能体RAG架构与以人为中心的设计原则相结合，为金融领域提取有意义洞察提供了有效方法。
