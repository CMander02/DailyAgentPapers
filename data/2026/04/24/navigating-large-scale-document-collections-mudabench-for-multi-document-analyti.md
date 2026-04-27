---
title: "Navigating Large-Scale Document Collections: MuDABench for Multi-Document Analytical QA"
authors:
  - "Zhanli Li"
  - "Yixuan Cao"
  - "Lvzhou Luo"
  - "Ping Luo"
date: "2026-04-24"
arxiv_id: "2604.22239"
arxiv_url: "https://arxiv.org/abs/2604.22239"
pdf_url: "https://arxiv.org/pdf/2604.22239v1"
github_url: "https://github.com/Zhanli-Li/MuDABench"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Multi-Document QA"
  - "RAG"
  - "Multi-Agent Workflow"
  - "Benchmark"
  - "Information Extraction"
relevance_score: 7.5
---

# Navigating Large-Scale Document Collections: MuDABench for Multi-Document Analytical QA

## 原始摘要

This paper introduces the task of analytical question answering over large, semi-structured document collections. We present MuDABench, a benchmark for multi-document analytical QA, where questions require extracting and synthesizing information across numerous documents to perform quantitative analysis. Unlike existing multi-document QA benchmarks that typically require information from only a few documents with limited cross-document reasoning, MuDABench demands extensive inter-document analysis and aggregation. Constructed via distant supervision by leveraging document-level metadata and annotated financial databases, MuDABench comprises over 80,000 pages and 332 analytical QA instances. We also propose an evaluation protocol that measures final answer accuracy and uses intermediate-fact coverage as an auxiliary diagnostic signal for the reasoning process. Experiments reveal that standard RAG systems, which treat all documents as a flat retrieval pool, perform poorly. To address these limitations, we propose a multi-agent workflow that orchestrates planning, extraction, and code generation modules. While this approach substantially improves both process and outcome metrics, a significant gap remains compared to human expert performance. Our analysis identifies two primary bottlenecks: single-document information extraction accuracy and insufficient domain-specific knowledge in current systems. MuDABench is available at https://github.com/Zhanli-Li/MuDABench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决的是大规模半结构化文档集合上的分析型问答（Analytical QA）问题。研究背景是：当前基于大语言模型和检索增强生成的主流问答范式，主要处理从少量松散文档中检索片段的多跳推理任务（如HotpotQA）或长上下文任务（如LongBench），这些方法通常假设所有相关文档能装入单一上下文窗口，且只需从少数文档中提取信息。然而，在许多真实场景（如金融监管者分析数百份公司年报、ESG披露等）中，问题需要从大量文档（平均15份、总计超8万页）中提取并合成信息，进行定量分析；遗漏任何相关文档或误读单个表格都可能导致结论失效。现有基准的不足在于：多跳数据集文档量少且无结构化元数据，长上下文基准针对单一长文档，金融基准（如FinanceBench）聚焦单文档QA，而像Aryn和DocETL等系统虽提出多步工作流但未发布大规模基准。因此，本文核心要解决的是：构建一个全新的大规模多文档分析型QA基准MuDABench，其特点包括文档数量多（平均14.8份）、页面量大（平均149.7页/问题）、具备结构化元数据，并要求跨文档聚合与定量分析，以填补现有基准无法评估这类复杂推理任务的空白，并揭示现有RAG及长上下文方法的严重不足。

### Q2: 有哪些相关研究？

相关工作主要涵盖文档QA的三个方面：文档元素QA、单文档QA和多文档QA。在文档元素QA领域，FigureQA和DocVQA关注图表与文档图像理解，TabIS和TableBench则评估表格推理能力，这些工作依赖OCR和多模态模型，但MuDABench侧重于非图像形式的纯文本分析。单文档QA方面，FinanceBench等展示了长上下文模型和RAG系统的有效性，但MuDABench要求跨文档聚合而非单文档检索。多文档QA中，大多数基准（如M3DocVQA、FinAgentBench）将多文档视为信息源拼凑上下文，或仅限于短文档的多跳推理（如维基百科基准）。Loong和RULER揭示了长上下文模型的局限，但未专门面向分析型查询。MuDABench与这些工作的核心区别在于：首次提出针对大规模文档集合的分析型问答基准，要求模型执行多步骤定量分析（如总和、分组统计），且文档量远超单模型上下文窗口。此外，MuDABench通过远程监督构建了8万页数据与332个实例，并提出了包含中间事实覆盖率的评估协议。本文还提出了多智能体工作流（规划-提取-代码生成），而现有RAG将文档视为扁平池，缺乏结构化处理能力。

### Q3: 论文如何解决这个问题？

论文提出了一套多智能体分析问答工作流（Multi-Agent Analytic QA Workflow），以解决大规模半结构化文档集合上的定量分析问题。整体框架包含四个核心模块：

1. **可扩展规划智能体（Scalable Planning Agent）**：该智能体不直接检索文档，而是将全局问题Q分解为针对单个文档的查询模板（query templates），并利用文档的元数据（如股票代码、财年、文档类型）对模板进行填充，从而将大规模检索转化为高效的元数据引导式提取，避免上下文溢出。

2. **文档级信息提取器（Document-Level Information Extractor）**：针对每个文档，根据元数据实例化查询模板，并调用标准RAG系统进行针对性提取，生成中间文本证据。这一过程可并行处理，支持数千文档的扩展。

3. **可扩展规范化智能体（Scalable Norm Agent）**：为支持后续程序化推理，该模块将非结构化提取文本分批转换为结构化JSON记录。首先从小样本中定义统一模式（schema），然后采用批迭代策略逐步规范化所有记录，避免单次处理时的上下文溢出。

4. **可扩展代码智能体（Scalable Code Agent）**：该智能体不直接向LLM输入全部提取信息，而是仅提供模式部分示例，自主生成Python程序，对整个结构化JSON数据集执行分析计算，最终得到答案。

创新点包括：元数据感知的查询模板分解策略，将检索与推理解耦；批迭代规范化方法实现任意规模文档的结构化转换；代码合成机制绕过LLM的上下文长度限制并提升数值计算可靠性。实验表明，该工作流在过程准确率和最终准确率上显著优于标准RAG（如GPT-4o），尤其当分块数为5时，简单/复杂问题的过程准确率分别达0.5888/0.5749，最终准确率达0.2243/0.1619，但仍远低于人类专家表现（0.8334/0.7334）。

### Q4: 论文做了哪些实验？

实验在 MuDABench 基准上进行，该基准包含超过 80,000 页文档和 332 个分析性 QA 实例。实验对比了标准 RAG 系统（使用 GPT-4o，分有无元数据提示两种变体，检索块数量从 |D| 到 2.5×|D|）和提出的多智能体工作流（使用 DeepSeek-R1 规划、DeepSeek-Chat 归一化、GPT-4o 和 GPT-4.1-mini 执行）。主要结果包括：标准 RAG 性能较差，元数据注入仅有有限提升；增加检索块数能提高过程覆盖度，但无法可靠转化为最终答案准确率（简单问题准确率波动，复杂问题持续低）。多智能体工作流显著优于 RAG，在简单和复杂问题上最终答案准确率分别为（如表所示四个独立步骤准确率：规划 86.7%/93.3%，提取 40.0%/20.0%，归一化 100%/100%，代码 93.3%/93.3%），但提取（主要瓶颈，尤其是长文档，准确率仅 25.9%）和领域知识不足导致与人类专家仍有差距。鲁棒性分析表明，注入 0.5×|D| 无关文档会降低复杂问题的准确率。

### Q5: 有什么可以进一步探索的点？

该论文在金融领域的局限性限制了其向其他领域的泛化能力，未来可探索医疗、法律等半结构化文档密集领域的数据构建方法。当前数据规模仅332个QA实例，虽通过远程监督可扩展，但需要更高效的自动化标注策略来平衡规模与质量。论文指出的两个瓶颈中，单文档信息抽取可通过引入多模态文档解析（如表格、图表识别）和改进长文本理解模型来优化；领域知识不足则可通过检索增强的预训练或微调领域专用大模型缓解。此外，当前多智能体流程中规划、抽取与代码生成的模块间缺乏反馈循环，可设计迭代纠错机制。对于原子事实的粒度与等价性问题，建议开发基于语义等价检测的动态评估框架，替代当前依赖人工标注的静态评价体系。

### Q6: 总结一下论文的主要内容

本文提出MuDABench，一个面向大规模半结构化文档集合的多文档分析问答基准。现有基准仅需从少数文档中提取信息，而MuDABench要求跨大量文档进行综合定量分析，定义了更复杂的任务。基准通过远程监督利用文档元数据和金融数据库构建，包含8万多页和332个分析问答实例。评估协议不仅衡量最终答案准确性，还使用中间事实覆盖率作为推理过程的诊断信号。实验表明，将文档视为扁平检索池的标准RAG系统表现不佳。为此，作者提出了一种多智能体工作流，协调规划、提取和代码生成模块，显著提升了过程和结果指标，但与人类专家表现仍有差距。分析识别出两大瓶颈：单文档信息提取准确性和领域知识不足。MuDABench为可扩展文档分析系统提供了严格的测试平台。
