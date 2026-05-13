---
title: "Overview of the MedHopQA track at BioCreative IX: track description, participation and evaluation of systems for multi-hop medical question answering"
authors:
  - "Rezarta Islamaj"
  - "Joey Chan"
  - "Robert Leaman"
  - "Jongmyung Jung"
  - "Hyeongsoon Hwang"
  - "Quoc-An Nguyen"
  - "Hoang-Quynh Le"
  - "Harikrishnan Gurushankar Saisudha"
  - "Ganesh Chandrasekar"
  - "Rustam R. Taktashov"
  - "Nadezhda Yu. Bizyukova"
  - "Sofia I. R. Conceição"
  - "Paulo R. C. Lopes"
  - "Reem Abdel Salam"
  - "Mary Adewunmi"
  - "Zhiyong Lu"
date: "2026-05-12"
arxiv_id: "2605.12313"
arxiv_url: "https://arxiv.org/abs/2605.12313"
pdf_url: "https://arxiv.org/pdf/2605.12313v1"
categories:
  - "cs.CL"
  - "cs.IR"
tags:
  - "多跳问答"
  - "生物医学问答"
  - "检索增强生成"
  - "大型语言模型"
  - "共享任务基准"
  - "多步推理"
  - "评估方法"
relevance_score: 7.5
---

# Overview of the MedHopQA track at BioCreative IX: track description, participation and evaluation of systems for multi-hop medical question answering

## 原始摘要

Multi-hop question answering (QA) remains a significant challenge in the biomedical domain, requiring systems to integrate information across multiple sources to answer complex questions. To address this problem, the BioCreative IX MedHopQA shared task was designed to benchmark in multi-hop reasoning for large language models (LLMs). We developed a novel dataset of 1,000 challenging QA pairs spanning diseases, genes, and chemicals, with particular emphasis on rare diseases. Each question was constructed to require two-hop reasoning through the integration of information from two distinct Wikipedia pages. The challenge attracted 48 submissions from 13 teams. Systems were evaluated using both surface string comparison and conceptual accuracy (MedCPT score). The results showed a substantial performance gap between baseline LLMs and enhanced systems. The top-ranked submission achieved an 89.30% F1 score on the MedCPT metric and an 87.30% exact match (EM) score, compared with 67.40% and 60.20%, respectively, for the zero-shot baseline. A central finding of the challenge was that retrieval-augmented generation (RAG) and related retrieval-based strategies were critical for strong performance. In addition, concept-level evaluation improved answer assessment when correct responses differed in surface form. The MedHopQA dataset is publicly available to support continued progress in this important area. Challenge materials: https://www.ncbi.nlm.nih.gov/research/bionlp/medhopqa and benchmark https://www.codabench.org/competitions/7609/

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文介绍了 BioCreative IX 的 MedHopQA 共享任务，旨在解决生物医学领域中的多跳问答（multi-hop QA）挑战。多跳问答要求系统整合多个来源的信息来回答复杂问题，而现有的生物医学问答数据集大多局限于单跳推理或局部证据。为此，论文构建了一个包含 1000 个涉及疾病、基因和化学物质的多跳问答对的新数据集，特别关注罕见疾病。每个问题需要两跳推理，通过整合来自两个不同维基百科页面的信息。论文还描述了评估方法（包括基于字符串匹配和基于概念准确性的两级评估）、参与系统的总结以及结果分析，以推动基于 LLM 的多跳推理能力的发展。

### Q2: 有哪些相关研究？

论文列举了多个生物医学问答相关工作和共享任务，包括 BioASQ（结合问答与文档/片段检索，但多为单跳）、PubMedQA（基于单篇摘要的 Yes/No 问答）、MedQA 和 MedMCQA（医学选择题，不要求显式多文档）、MultiMedQA（综合评估）、QAngaroo/MedHop（多跳阅读理解）、emrQA（电子病历问答）、MEDIQA（医学摘要和推理）和 TREC 临床决策支持（检索为主）。与这些工作相比，MedHopQA 的独特之处在于专门设计为需要跨两个文档进行显式多跳推理的问题，且答案形式包括实体和 Yes/No，并支持概念级等价评估。论文指出许多现有基准可被单跳检索解决，而 MedHopQA 要求系统进行组合推理，更贴近真实临床需求。

### Q3: 论文如何解决这个问题？

论文通过组织共享任务的方式解决多跳医学问答评估问题。首先，手动构建了一个包含 1000 个问答对的 MedHopQA 数据集，每个问题需从两个维基百科页面整合信息，覆盖疾病、基因、化学物质，特别关注罕见病。问题类型包括疾病名、基因/蛋白质、化学药物、Yes/No 等。为保护测试集完整性，将 1000 个问题嵌入到 10,000 个问题中（含诱饵问题）。评估采用两级策略：一是轻量级字符串匹配（使用同义词词表进行 Lexical Match），二是概念级匹配（使用 MedCPT 模型计算语义相似度）。基线系统使用零样本 GPT-4o（温度 0，输出限制 15 token）。在正式评估期间，13 个团队提交了 48 个系统，论文总结了这些系统的方法，包括多阶段 RAG 管道（DMIS Lab）、选择性分解（UETQuintet）、agentic 与非 agentic 管道对比（CLaC）、本地 RAG（OREKHOVICHI）、本体增强检索（lasigeBioTM）和微调（CaresAI）。最强系统组合了查询扩展、思路链子查询、网络搜索和决策模块。论文分析了整体性能、答案类别难度和问题共识度。

### Q4: 论文做了哪些实验？

论文通过共享任务进行实验评估。设置官方测试阶段（2025年5月27日至6月1日）和非官方阶段（6月10日至18日）。评估指标包括 Lexical Match（字符串匹配+同义词表）和 MedCPT（概念级匹配）。基线零样本 GPT-4o 达到 60.2% Lexical EM 和 67.4% MedCPT F1。最佳 DMIS Lab 系统达到 87.3% EM 和 89.3% MedCPT F1。UETQuintet 系统在非官方阶段提升至 88.1% EM 和 89.7% MedCPT F1。论文还按答案类型进行了细粒度分析，发现数字问题最难（平均 MedCPT 准确率 22.5%），染色体位置次之（47.2%），Yes/No 问题方差大（平均 56.3%，最佳 98.7%）。分析问题共识度显示，仅 30 个问题被 ≥90% 的答对，34 个问题被 ≤10% 答对，16 个问题没有任何系统答对。此外，论文比较了使用专有模型（GPT-4o、Gemini）与开源模型（Mistral、LLaMA、Qwen）的性能差异，发现专有模型+精细检索管道明显更强。

### Q5: 有什么可以进一步探索的点？

论文指出的局限和未来方向包括：1) 数据集目前仅包含两跳推理，未来可扩展到更多跳或更复杂的推理路径；2) 评估仅关注简短答案（一个词或短语），未来计划支持更长、可解释的答案并开发基于 agent 的评估管道；3) 概念级等价评估使用了 MedCPT，但该模型可能仍有偏差，未来可探索更全面的语义评估；4) 对于数字和染色体位置等困难类别，需要更好的格式化和规范化方法；5) 大部分成功系统依赖专有大型模型，如何在开源小模型上实现类似性能仍有挑战；6) 未来可结合结构化知识库（如知识图谱）丰富推理；7) 共享任务结果表明强大的 RAG 和 agentic 设计是关键，但不同组件的贡献需要进一步消融实验；8) 数据集仅基于维基百科，未来可引入更权威的医学文献和知识库。

### Q6: 总结一下论文的主要内容

本文是 BioCreative IX 中 MedHopQA 共享任务的概述。论文构建了一个包含 1000 个多跳医学问答对的新数据集，每个问题要求系统从两个维基百科页面整合信息，涵盖疾病、基因、化学物质和 Yes/No 类型。组织了国际竞赛，13 个团队提交了 48 个系统。评估采用两级策略：基于同义词表的字符串匹配和基于 MedCPT 的概念级匹配。结果显示，基于 RAG 和 agentic 管道的系统大幅超越零样本基线（GPT-4o 67.4% vs 最佳 89.3% F1）。论文分析了不同方法、答案类型和问题难度，指出数字化和染色体定位是最难的类别。最强系统结合了多源检索、查询分解和模型集成。MedHopQA 数据集公开发布，旨在推动生物医学领域多跳推理能力的发展，并为 LLM 在医学问答中的应用提供标准化评估平台。
