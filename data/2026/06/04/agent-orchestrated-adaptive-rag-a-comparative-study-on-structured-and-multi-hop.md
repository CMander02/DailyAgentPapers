---
title: "Agent-Orchestrated Adaptive RAG: A Comparative Study on Structured and Multi-Hop Retrieval"
authors:
  - "Anuj Maharjan"
  - "Devinder Kaur"
  - "Richard Molyet"
date: "2026-06-04"
arxiv_id: "2606.05658"
arxiv_url: "https://arxiv.org/abs/2606.05658"
pdf_url: "https://arxiv.org/pdf/2606.05658v1"
categories:
  - "cs.IR"
  - "cs.AI"
tags:
  - "Agent-Orchestrated RAG"
  - "Adaptive Retrieval"
  - "Query Decomposition"
  - "Multi-Hop Reasoning"
  - "Self-Reflection"
  - "Agent for RAG"
relevance_score: 7.5
---

# Agent-Orchestrated Adaptive RAG: A Comparative Study on Structured and Multi-Hop Retrieval

## 原始摘要

Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by grounding their responses in external knowledge, but conventional pipelines rely on static, single-step retrieval that limits performance on complex queries. This paper presents an Agent-Orchestrated Adaptive RAG framework that introduces dynamic query decomposition, iterative retrieval, and a bounded self-reflective evaluation loop. We evaluate the system across two complementary datasets: a domain-specific DevOps knowledge base and the multi-hop reasoning benchmark MuSiQue. Using metrics that include overall score, citation accuracy, mean reciprocal rank, and topic coverage, we find that query decomposition yields consistent gains in the structured domain (overall score $+0.04$, MRR $+0.17$ on DevOps) but degrades ranking precision on the multi-hop benchmark, while the reflection mechanism improves citation accuracy at a substantial latency cost. These contrasting results show that agentic enhancements are not universally beneficial and must be applied selectively according to query and domain characteristics. Our findings argue for adaptive, cost-aware orchestration rather than uniformly aggressive reasoning pipelines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决传统检索增强生成（RAG）系统在处理复杂查询时的局限性。研究背景是，尽管大语言模型（LLM）能力强大，但存在事实幻觉和无法访问训练数据外知识的固有问题。RAG通过引入外部知识库缓解了这些问题，但传统Naive RAG采用静态的单步检索流程，仅能处理简单的事实查询，难以应对需要跨文档推理或链式中间结果的多跳复杂查询。现有研究的不足在于，大多只在单一领域评估Agentic RAG的增强效果，缺乏对跨领域通用性的理解。核心问题是：Agent增强的RAG机制（如查询分解、迭代检索、自反思）是否在不同领域和推理任务中表现一致？本文通过构建自适应RAG框架，在结构化领域（DevOps知识库）和多跳推理基准（MuSiQue）上进行对比评估，发现查询分解和自反思机制并非普遍有效——在结构化领域效果显著但会降低多跳基准的排序精度，且反思机制虽提升引用准确性却带来高延迟成本。因此，核心要解决的是如何根据查询和领域特征选择性地应用Agent增强，实现自适应、成本感知的RAG编排。

### Q2: 有哪些相关研究？

相关研究可分为方法类、应用类和评测类。方法类中，RAG基础工作包括Dense Passage Retrieval和Naive RAG，本文在此基础上引入动态查询分解与迭代检索。多跳推理方面，HotpotQA和MuSiQue是经典基准，本文以MuSiQue作为对比数据集。工具使用与推理轨迹方面，ReAct框架将推理与行动交替，Toolformer让模型学习调用工具，本文的多智能体分解架构与其相关但更强调显式分解。自我反思方面，Self-RAG引入选择性检索和批判信号，Corrective RAG增加检索修正步骤，Adaptive-RAG根据问题难度路由到不同复杂度策略，本文采用有界自反思评估循环。查询分解方法受Least-to-Most prompting启发，将复杂问题分解为子问题。与这些工作不同，本文创新性地在两个对比领域（结构化DevOps知识库和多跳推理MuSiQue）进行评估，发现同一机制在不同推理需求下效果迥异，强调应根据领域特征选择增强策略，而非统一采用激进推理流程。

### Q3: 论文如何解决这个问题？

该论文提出了一种**Agent编排的自适应RAG框架**，通过动态查询分解、迭代检索和有界的自我反思评估循环来解决静态单步检索的限制。核心架构由**编排器**作为中央控制器，根据**查询分类器**的输出决定路由策略：简单查询直接进入检索路径，复杂查询则触发分解管道。**查询分解器**将复杂多跳查询拆分为有序子查询，并独立检索后聚合为连贯响应。**答案评估器**从相关性、引用准确性、上下文支持和幻觉检测四个维度评估生成响应，当发现问题时触发**反思循环**（最多两次重试），通过优化提示或调整检索上下文来改进输出。

关键技术包括：使用**Docling**进行结构转换，保留表格头、层级列表等语义信息；通过**YAML frontmatter注入元数据**（文档类型、服务等），实现基于属性的过滤；采用**600令牌的语义分块**（100令牌重叠）平衡上下文窗口、检索精度和技术连贯性；使用**BGE编码器**生成嵌入，**FAISS**进行向量搜索，并结合余弦相似度进行排名。整个系统本地运行（Llama-3.1-8B-Instruct 4-bit量化），确保隐私安全。

创新点在于：将检索从单次查询转变为**顺序决策过程**，代理可根据推理步骤多次调用检索、调整过滤器和重新排序结果；通过**有界反思机制**在不显著增加成本的前提下提升引用准确性；证明了代理增强并非普遍有益，需要根据查询和领域特性选择性应用。

### Q4: 论文做了哪些实验？

实验在两个互补数据集上进行：一个是结构化的DevOps知识库，包含80份文档（Standard 5份、Architecture 10份、Runbooks 20份、Incidents 15份、Postmortem 15份、Onboarding 15份），平均词数100-200词；另一个是MuSiQue多跳推理基准。评估指标包括Overall Score、Critical Source Recall、MRR、Success@5、Citation Accuracy、Topic Coverage和Latency。实验对比了静态检索基线与动态查询分解、迭代检索和有界自反思评估循环等智能体增强策略。

主要结果呈现对比性：在DevOps领域，查询分解带来一致提升（Overall Score +0.04，MRR +0.17），但在MuSiQue多跳基准上排名精度下降；反思机制提升了Citation Accuracy但付出了显著Latency代价。这表明智能体增强并非普遍有益，需根据查询和领域特征选择性应用，支持自适应、成本感知的编排策略。

### Q5: 有什么可以进一步探索的点？

论文系统依赖静态启发式规则动态调整策略，这是主要局限。未来可将强化学习或元学习用于策略选择，让系统根据查询特征自动判断何时需要分解或反思，从而平衡质量与效率。当前反思机制带来六倍延迟但收益有限，可改进为细粒度错误检测与选择性重执行，只重跑失败组件而非整个流程，并设置置信度阈值提前终止。对于多跳数据中分解导致的排序精度下降，应生成语义更连贯的子查询并保留上下文依赖关系，或引入知识图谱等结构化表示来捕获跨步骤关系。系统还可扩展更多工具如实时API、符号推理引擎，以支持动态信息获取。最后需在大规模、噪声查询和并发负载等真实条件评估系统的鲁棒性与运营成本，推动从研究原型到生产部署的转化。

### Q6: 总结一下论文的主要内容

本文提出了一种Agent编排的自适应RAG框架，旨在解决传统RAG在复杂查询上的静态、单步检索局限性。该框架通过查询分类器、查询分解器、答案评估器和中心编排器实现动态查询分解、迭代检索和自反思评估循环。研究在两个互补数据集上评估：领域特定的DevOps知识库和多跳推理基准MuSiQue。主要发现包括：查询分解在结构化领域带来稳定增益（DevOps上总体得分+0.04，MRR+0.17），但会降低多跳基准的排序精度；反思机制能提升引用准确率但显著增加延迟。这些对比结果证明，代理增强并非普遍适用，必须根据查询和领域特征选择性应用。论文的核心贡献在于揭示了代理型RAG的领域依赖性，主张采用自适应、成本感知的编排策略，而非统一激进的推理流水线。
