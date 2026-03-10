---
title: "SPD-RAG: Sub-Agent Per Document Retrieval-Augmented Generation"
authors:
  - "Yagiz Can Akay"
  - "Muhammed Yusuf Kartal"
  - "Esra Alparslan"
  - "Faruk Ortakoyluoglu"
  - "Arda Akpinar"
date: "2026-03-09"
arxiv_id: "2603.08329"
arxiv_url: "https://arxiv.org/abs/2603.08329"
pdf_url: "https://arxiv.org/pdf/2603.08329v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.IR"
tags:
  - "Multi-Agent Systems"
  - "Retrieval-Augmented Generation"
  - "Long-Context QA"
  - "Hierarchical Architecture"
  - "Document-Level Specialization"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# SPD-RAG: Sub-Agent Per Document Retrieval-Augmented Generation

## 原始摘要

Answering complex, real-world queries often requires synthesizing facts scattered across vast document corpora. In these settings, standard retrieval-augmented generation (RAG) pipelines suffer from incomplete evidence coverage, while long-context large language models (LLMs) struggle to reason reliably over massive inputs. We introduce SPD-RAG, a hierarchical multi-agent framework for exhaustive cross-document question answering that decomposes the problem along the document axis. Each document is processed by a dedicated document-level agent operating only on its own content, enabling focused retrieval, while a coordinator dispatches tasks to relevant agents and aggregates their partial answers. Agent outputs are synthesized by merging partial answers through a token-bounded synthesis layer (which supports recursive map-reduce for massive corpora). This document-level specialization with centralized fusion improves scalability and answer quality in heterogeneous multidocument settings while yielding a modular, extensible retrieval pipeline. On the LOONG benchmark (EMNLP 2024) for long-context multi-document QA, SPD-RAG achieves an Avg Score of 58.1 (GPT-5 evaluation), outperforming Normal RAG (33.0) and Agentic RAG (32.8) while using only 38% of the API cost of a full-context baseline (68.0).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决复杂、真实世界查询中，需要从海量、异构的文档集合中综合分散信息以生成全面答案的问题。研究背景是，随着大语言模型（LLMs）和智能体系统在复杂信息搜索任务中的应用日益广泛，诸如跨多年财务报告评估公司风险或整合多篇科学论文发现等场景变得普遍。然而，现有方法存在明显不足：标准的检索增强生成（RAG）流程通常固定检索文档数量（K），当答案所需证据分散在众多文档中时，超出前K个结果的证据往往被丢弃，导致证据覆盖不全；而长上下文LLMs虽然扩展了上下文窗口，但实证表明，随着输入长度（如数十万token）的增加，其推理质量会显著下降，难以可靠地对海量输入进行推理。

因此，本文要解决的核心问题是：如何在保证可扩展性和成本效益的同时，实现对大规模、多文档语料库的**穷尽性、跨文档问答**，即确保不遗漏分散在各处的关键证据，并能可靠地综合这些信息。为此，论文提出了SPD-RAG框架，其核心创新在于**沿文档轴而非任务轴分解问题**，通过一个分层多智能体架构，为每个文档分配一个专用的文档级智能体进行深度分析，再通过中央协调器聚合部分答案，从而在异构多文档设置中提升答案质量和系统可扩展性。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为多智能体系统、长文档处理与多文档问答、以及相关评测基准三大类。

在多智能体系统方面，相关工作如MegaAgent和AgentOrchestra展示了通过分层任务分解实现大规模智能体协作的架构。本文的SPD-RAG采用了类似的中心化协调思想，但特别强调沿文档轴进行分解，为每个文档分配专属的文档级智能体，这不同于那些按功能或子任务划分智能体的通用框架。相关研究还量化了多智能体系统的扩展规律，指出中心化协调在并行任务上的优势以及独立智能体可能放大错误，这直接启发了本文基于协调器的设计。

在长文档处理与多文档问答领域，现有方法如LLM×MapReduce和ToM通过分块和递归策略处理长上下文，关注块间依赖与冲突。LongAgent针对单个长文档进行智能体分块与协调，而本文则专注于处理多个可能相互冲突的独立文档。GraphRAG等方法通过构建知识图谱进行全局感知和社区检测来聚合答案，而SPD-RAG则直接基于智能体生成的文本摘要进行操作，通过相似性引导的递归合成来整合信息，避免了显式知识图谱构建的复杂性。

在评测基准方面，LOONG基准专门评估“所有文档均相关”的长上下文多文档问答，其难度凸显了本文所解决问题的挑战性。其他基准如MoNaCo、MEBench等则从不同角度探究多文档推理，共同表明可扩展的多文档推理仍是一个开放挑战。本文正是在LOONG所强调的这种高要求场景下进行方法设计与评估。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SPD-RAG的分层多智能体框架来解决复杂跨文档问答中证据覆盖不全和长上下文模型推理不可靠的问题。其核心方法是沿文档轴分解问题，为每个文档分配一个专用的文档级智能体进行独立处理，并通过一个协调层进行任务分发与答案聚合，最终通过一个支持递归合并的合成层生成最终答案。

整体架构分为三层：协调层、并行检索层和合成层。协调层首先处理用户查询，将其分解为两个关键部分：一是共享指令集，即一系列原子化的、自包含的提取任务，明确指定需要从文档中提取的字段、实体或数值；二是合成指令，用于指导下游合成层如何优先处理和构建合并后的响应。这一步骤生成了一个结构化的任务列表。

并行检索层是核心创新模块。系统为语料库中的每个文档分配一个专属的子智能体。每个子智能体在其被分配的单一文档范围内，作为一个独立的RAG循环运行。它严格限制只能在自己的文档内进行检索，避免了跨文档干扰信息对本地提取的负面影响。子智能体接收原始查询、分配的文档名和共享指令集，然后进行迭代的“检索-推理”循环：它要么发起一个聚焦的搜索查询，要么发出终止信号并输出基于该文档的发现结果。检索过程结合了密集向量检索和重排序技术，以确保精度。

所有文档的子智能体任务通过LangGraph的并行发送API同时触发，实现了高效的并行处理。每个子智能体的输出包括一份自然语言的发现报告和一个相关性/置信度分数。

合成层负责递归地聚合和合成所有子智能体的发现。其关键技术是“基于相似性排序的合并与合成”算法。该层将所有的发现报告嵌入为向量，计算余弦相似度矩阵并转换为距离矩阵，然后使用层次聚类生成树状图。接着，它自底向上遍历合并树，贪婪地将语义最相似的报告分批组合，确保每批的总令牌数不超过预设的预算。对于每一批数据，调用大语言模型，结合原始查询和合成指令，生成一个聚合后的摘要。这些新的摘要成为下一轮迭代的输入。此过程递归进行，直到最终只剩下一个摘要，其大小在目标上下文窗口内，该摘要即为最终答案。这种设计使得系统能够处理远超单个模型上下文限制的海量文档语料。

主要创新点包括：1) **文档级专业化**：每个智能体专注于单一文档，实现了精准、深入的检索，避免了信息污染。2) **集中式协调与融合**：通过协调层统一任务分解和指令分发，并通过智能的、递归的合成层进行信息融合，兼顾了模块化和整体答案质量。3) **可扩展的递归合成机制**：合成层的动态Map-Reduce式流水线设计，使系统能够理论上处理任意规模的文档集合，具有良好的可扩展性。

### Q4: 论文做了哪些实验？

实验在LOONG基准测试上进行，该基准包含英文和中文的多文档问答实例，平均每个测试用例涉及11个文档，涵盖财务报告和学术论文两种真实场景。评估集共102个实例（40个学术论文，62个财务报告），任务类型包括聚焦定位、比较、聚类和推理链。实验对比了三种基于Gemini 2.5 Pro的系统：全上下文基线（将所有文档拼接后直接输入）、标准RAG（基于向量检索top-K片段）和智能体RAG（单智能体迭代检索）。SPD-RAG采用分层多智能体框架，每个文档由专用的Gemini 2.5 Flash子智能体处理，协调器使用Gemini 2.5 Pro进行任务分发和答案聚合。

主要结果如下：SPD-RAG在平均得分上达到58.1，显著优于标准RAG（33.0）和智能体RAG（32.8），完美率（PR）为18.6%，也高于智能体RAG的8.8%。尽管全上下文基线得分最高（68.0），但SPD-RAG仅以其37.9%的API成本实现了基线85.4%的性能，展现出优异的成本效益比。在任务类型分析中，SPD-RAG在聚类任务上比标准RAG高出40.5分，在推理链任务上比智能体RAG高出26.2分，表明其在需要跨文档聚合和推理的任务上优势明显。在学术论文领域，SPD-RAG将平均得分从标准RAG的15.2提升至60.0，显著缓解了传统RAG在长技术文档上的覆盖不足问题。成本效益方面，SPD-RAG的“得分/成本”比为564.1，优于全上下文基线的249.1，体现了其高效的成本质量权衡。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来探索方向主要集中在以下几个方面。首先，系统在查询时会产生较高的LLM调用次数（每个文档代理一次调用加最终合成步骤），虽然成本仍低于全上下文基线，但如何进一步优化代理的调用效率、减少冗余计算，是值得探索的改进点。例如，可以引入动态代理选择机制，仅对高度相关的文档启动深度处理，其余采用轻量级检索。

其次，协调器生成子任务的能力直接影响结果完整性，这在技术性学术论文案例中尤为明显。未来可研究更智能的任务分解方法，比如结合查询类型自适应调整任务粒度，或引入强化学习让协调器从历史错误中学习。

再者，实验仅基于学术论文和财务报告两个领域，未涵盖法律、医疗等具有复杂结构的专业文档。未来需要在更多元、异构的文档库上验证框架的泛化能力，并可能针对不同领域设计特定的文档预处理或代理微调策略。

最后，论文中设计的递归合成流程在实验中未被触发，因为所用模型上下文窗口足以一次性处理所有代理输出。其在大规模文档（数百至数千份）下的扩展性、答案质量与成本效益尚未得到实证检验。因此，构建一个包含海量文档的基准测试，以评估系统在真实大规模数据库场景下的性能，是至关重要的未来工作。此外，可探索分层聚类与合成策略的优化，以平衡效率与信息完整性。

### Q6: 总结一下论文的主要内容

论文针对跨文档复杂问答任务中，传统检索增强生成（RAG）存在证据覆盖不全、长上下文大语言模型（LLM）难以可靠推理大量输入的问题，提出了SPD-RAG这一分层多智能体框架。其核心贡献在于沿文档轴分解问题，为每个文档分配一个专用的文档级智能体进行聚焦检索与局部答案生成，并由一个协调器调度任务并聚合部分答案，最后通过一个令牌受限的合成层（支持递归Map-Reduce以处理海量语料）合并输出。该方法实现了文档级专业化与中心化融合，在异构多文档场景中提升了可扩展性与答案质量，并构建了模块化、可扩展的检索流程。在LOONG基准测试上的实验表明，SPD-RAG以显著优势超越传统RAG方法，并在需要深度跨文档合成的任务上表现尤为突出，同时大幅降低了API成本，证明了为每个文档提供专注的智能体处理是比单纯扩展单次上下文窗口更高效、经济且可扩展的策略。
