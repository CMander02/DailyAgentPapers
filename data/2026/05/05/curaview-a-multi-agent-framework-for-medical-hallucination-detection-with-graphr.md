---
title: "CuraView: A Multi-Agent Framework for Medical Hallucination Detection with GraphRAG-Enhanced Knowledge Verification"
authors:
  - "Severin Ye"
  - "Xiao Kong"
  - "Xiaopeng He"
  - "Guangsu Yan"
  - "Dongsuk Oh"
date: "2026-05-05"
arxiv_id: "2605.03476"
arxiv_url: "https://arxiv.org/abs/2605.03476"
pdf_url: "https://arxiv.org/pdf/2605.03476v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Multi-Agent Framework"
  - "Medical Hallucination Detection"
  - "GraphRAG"
  - "Knowledge Verification"
  - "LLM Agent"
  - "Clinical Documentation"
relevance_score: 8.5
---

# CuraView: A Multi-Agent Framework for Medical Hallucination Detection with GraphRAG-Enhanced Knowledge Verification

## 原始摘要

Discharge summaries require extracting critical information from lengthy electronic health records (EHRs), a process that is labor-intensive when performed manually. Large language models (LLMs) can improve generation efficiency; however, they are prone to producing faithfulness hallucinations, statements that contradict source records, posing direct risks to patient safety. To address this, we present CuraView, a multi-agent framework for sentence-level detection and evidence-grounded explanation of faithfulness hallucinations in discharge summaries. CuraView constructs a GraphRAG-based knowledge graph from patient-level EHRs and implements a closed-loop generation-detection pipeline with sentence-level evidence retrieval and classification spanning four evidence grades from strong support to direct contradiction (E1-E4), yielding structured and interpretable evidence chains.
  We evaluate CuraView on a subset of 250 patients from the Discharge-Me benchmark, with 50 patients held out for testing. Our fine-tuned Qwen3-14B detection model achieves an F1 of 0.831 on the safety-critical E4 metric (90.9% recall, 76.5% precision) and an F1 of 0.823 on E3+E4, representing a 50.0% relative improvement over the base model and outperforming RAGTruth-style and QAGS-style baselines. These results demonstrate that evidence-chain-based graph retrieval verification substantially improves the factual reliability of clinical documentation, while simultaneously producing reusable annotated datasets for downstream model training and distillation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLMs）在生成出院小结时产生的“忠实性幻觉”问题。研究背景是，出院小结需要从冗长的电子健康记录（EHRs）中提取关键信息，人工完成过程劳动密集。虽然LLMs能提高生成效率，但它们容易产生与源记录相矛盾的内容（忠实性幻觉），对患者安全构成直接风险。

现有方法存在四点不足：（1）缺乏系统性生成能力，现有基准依赖昂贵的人工标注，没有自动化生成多样化医学错误的框架。（2）缺少患者特定上下文，大多数研究基于通用语料库评估幻觉，无法验证患者级别的具体声明（如药物过敏）。（3）证据支持不足，检测方法很少提供结构化的、可解释的、基于具体EHR记录的说明。（4）仅关注评估，先前的工作仅测量幻觉率，未能提供用于操作环境中的生成、检测和解释的端到端系统。

因此，本文提出CuraView，一个多智能体框架，旨在实现出院小结中忠实性幻觉的句子级检测和基于证据的解释。核心问题是开发一个能够自动生成多样化医学错误、利用患者特定知识图谱进行证据验证、并提供结构化可解释证据链的完整检测系统，以跨越LLMs临床应用的最后信任障碍。

### Q2: 有哪些相关研究？

相关工作主要分为三类：**方法类**（如RAG与知识图谱增强）、**评测与应用类**（如医疗幻觉检测与临床摘要生成），以及**多智能体系统类**。  

**方法类**中，传统RAG（如RARR、MedRAG、BioRAG）采用扁平文档检索，无法建模患者多表EHR（如诊断、药物、实验室检查）间的结构化关系。Microsoft GraphRAG及Medical Graph RAG虽引入图结构检索增强多跳推理，但构建的是跨患者知识图谱。本文的核心区别在于**构建患者级隔离的知识图谱**，实现个体化证据验证，并设计**E1-E4四级证据等级**，提供结构化可解释的错误溯源链。  

**评测与应用类**中，Med-HALT关注问答场景中事实性幻觉，Asgari et al.与Williams et al.虽聚焦临床摘要句子级或文档级可靠性评估，但均未提供患者层面的结构化证据解释。RadFlag针对放射报告的黑盒句子级检测，而本文面向出院小结，整合多表EHR证据进行跨源关系推理与时间敏感性错误检测（如药物停用矛盾）。  

**多智能体系统类**中，MedAgents依赖通用医学知识库（如PubMed）进行零样本推理，无法利用患者个体化EHR且缺乏系统化幻觉检测机制。本文的生成-检测双智能体闭环设计（基于LangChain与Qwen3-14B）通过对抗样本生成与证据驱动验证，首次将多智能体系统专门用于临床文档质量控制的幻觉检测。

### Q3: 论文如何解决这个问题？

CuraView提出了一种多智能体框架，通过闭环生成-验证-检测流水线来解决医疗幻觉检测问题。核心方法包括三个主要组件：幻觉生成智能体、基于GraphRAG的知识图谱和幻觉检测智能体。

幻觉生成智能体基于LangChain构建，系统性地生成七种临床错误类型（如诊断错误、用药错误等），遵循医学合理性、类型多样性、可控采样和证据可追溯性四原则。它通过两阶段句子筛选：先评估句子是否适合重写（需包含可验证医学事实且能保持合理性），再基于患者EHR证据进行定向改写，并为每个输出标注E1-E4证据等级。其中六种直接冲突错误标注为E4，虚构事实标注为E3。

GraphRAG知识图谱模块从多表EHR中提取9种实体类型（患者、诊断、用药、检验、检查、手术、生命体征、症状、科室）和10种关系类型（如has_diagnosis、prescribed等），通过社区检测算法进行层级组织，形成可查询的关系结构。

幻觉检测智能体逐句查询知识图谱进行证据检索，基于四等级证据（E1强支持到E4直接矛盾）输出结构化判断。整个流程形成数据准备、知识图谱构建、幻觉生成、幻觉检测和比较评估五阶段闭环。创新点在于证据链驱动的图检索验证机制，既提升了事实可靠性（在E4指标上F1达0.831），又生成了可复用的标注数据用于下游模型训练和蒸馏。

### Q4: 论文做了哪些实验？

CuraView在Discharge-Me基准测试的子集上进行了实验，共使用250名患者数据，其中50名用于测试。实验设置了句子级别的忠实幻觉检测任务，采用四种证据等级（E1-E4）进行结构化分类：E1（强支持）、E2（弱支持）、E3（弱矛盾）和E4（直接矛盾）。对比方法包括基础Qwen3-14B模型以及RAGTruth-style和QAGS-style基线方法。主要结果：在安全关键的E4指标上，微调后的Qwen3-14B检测模型达到0.831的F1分数（90.9%召回率，76.5%精确率）；在E3+E4综合指标上取得0.823的F1分数，相比基础模型实现了50.0%的相对提升，同时显著优于两种对比基线方法。CuraView还构建了基于GraphRAG的知识图谱进行证据链检索验证，并通过闭环生成-检测流程生成结构化的可解释证据链，额外产出了可用于下游模型训练和蒸馏的可复用标注数据集。

### Q5: 有什么可以进一步探索的点？

CuraView在医学幻觉检测上取得了显著进步，但仍存在几个关键局限和探索方向。首先，其知识图谱的构建完全依赖结构化EHR，未来可探索将非结构化临床笔记（如医生手写记录、影像报告）动态融入GraphRAG，以提升对复杂医嘱的语义理解。其次，当前证据分类仅依赖句子级检索，未考虑跨实体、跨时间的逻辑矛盾，可设计多层图注意力机制捕捉病程发展与治疗方案的时序因果链。此外，虽然F1达到0.831，但在E4（直接矛盾）精度上（76.5%）仍有提升空间，可尝试引入主动学习策略，利用检测模型对低置信度证据进行二次专家标注。另一个思路是构建多模态图，将患者生命体征趋势图与文本诊断相结合，例如检测"心率持续下降"与"升压药医嘱"之间的隐含矛盾。最后，该框架对中文病历的泛化能力尚未验证，可针对中文术语分割、用药简称等特性开发领域适配的实体对齐模块。

### Q6: 总结一下论文的主要内容

CuraView是一个多智能体框架，针对出院小结生成中的事实性幻觉进行句子级检测和基于证据的解释。问题在于大模型生成的出院小结可能包含与原始电子健康记录矛盾的内容，直接威胁患者安全。该方法通过构建基于GraphRAG的患者特定知识图谱，实现闭环的生成-检测流程，包括句子级证据检索和四级证据等级分类（E1-E4，从强支持到直接矛盾）。在Discharge-Me基准的50名测试患者（1103条句子）上，微调的Qwen3-14B检测模型在安全关键的E4指标上达到0.831的F1值（召回率90.9%，精确率76.5%），相比基线模型提升50%，并优于RAGTruth和QAGS风格基线。核心贡献包括：提出临床导向的幻觉分类体系、实现端到端多智能体框架、开发GraphRAG患者特定知识图谱（减少75.8%实体数并实现全图连通性）、设计结构化输出可靠性管道，以及提供可复用的带注释数据集。该工作显著提升了临床文档的事实可靠性，为下游模型训练和蒸馏提供了基础。
