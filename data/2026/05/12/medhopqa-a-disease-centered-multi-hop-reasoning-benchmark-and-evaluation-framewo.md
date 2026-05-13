---
title: "MedHopQA: A Disease-Centered Multi-Hop Reasoning Benchmark and Evaluation Framework for LLM-Based Biomedical Question Answering"
authors:
  - "Rezarta Islamaj"
  - "Robert Leaman"
  - "Joey Chan"
  - "Nicholas Wan"
  - "Qiao Jin"
  - "Natalie Xie"
  - "John Wilbur"
  - "Shubo Tian"
  - "Lana Yeganova"
  - "Po-Ting Lai"
  - "Chih-Hsuan Wei"
  - "Yifan Yang"
  - "Yao Ge"
  - "Qingqing Zhu"
  - "Zhizheng Wang"
  - "Zhiyong Lu"
date: "2026-05-12"
arxiv_id: "2605.12361"
arxiv_url: "https://arxiv.org/abs/2605.12361"
pdf_url: "https://arxiv.org/pdf/2605.12361v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.IR"
tags:
  - "Multi-Hop Reasoning"
  - "Biomedical QA"
  - "LLM Evaluation Benchmark"
  - "Open-Ended Generation"
  - "LLM-as-a-Judge"
  - "Concept-Level Evaluation"
  - "Dataset Construction Framework"
relevance_score: 9.0
---

# MedHopQA: A Disease-Centered Multi-Hop Reasoning Benchmark and Evaluation Framework for LLM-Based Biomedical Question Answering

## 原始摘要

Evaluating large language models (LLMs) in the biomedical domain requires benchmarks that can distinguish reasoning from pattern matching and remain discriminative as model capabilities improve. Existing biomedical question answering (QA) benchmarks are limited in this respect. Multiple-choice formats can allow models to succeed through answer elimination rather than inference, while widely circulated exam-style datasets are increasingly vulnerable to performance saturation and training data contamination. Multi-hop reasoning, defined as the ability to integrate information across multiple sources to derive an answer, is central to clinically meaningful tasks such as diagnostic support, literature-based discovery, and hypothesis generation, yet remains underrepresented in current biomedical QA benchmarks. MedHopQA is a disease-centered multi-hop reasoning benchmark consisting of 1,000 expert-curated question-answer pairs introduced as a shared task at BioCreative IX. Each question requires synthesis of information across two distinct Wikipedia articles, and answers are provided in an open-ended free-text format. Gold annotations are augmented with ontology-grounded synonym sets from MONDO, NCBI Gene, and NCBI Taxonomy to support both lexical and concept-level evaluation. MedHopQA was constructed through a structured process combining human annotation, triage, iterative verification, and LLM-as-a-judge validation. To reduce leaderboard gaming and contamination risk, the 1,000 scored questions are embedded within a publicly downloadable set of 10,000 questions, with answers withheld, on a CodaBench leaderboard. MedHopQA provides both a benchmark and a reusable framework for constructing future biomedical QA datasets that prioritize compositional reasoning, saturation resistance, and contamination resistance as core design constraints.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

现有的生物医学问答（QA）基准存在四个主要局限：一是多数采用多项选择格式，允许模型通过排除法而非推理得出答案，难以区分真正的推理与模式匹配；二是性能饱和，前沿LLM已在MedQA等基准上达到95%以上，接近天花板，不再具有区分度；三是训练数据污染，主流LLM的预训练语料中包含了大量公开的医学试题和PubMed摘要，高分可能反映记忆而非推理；四是推理深度有限，多数基准仅需单跳检索，而临床上重要的任务（如诊断支持、文献发现、假设生成）要求多步合成跨源信息。MedHopQA旨在填补多跳推理基准的空白，通过设计开放答案、防污染、可区分的评测框架来更可靠地评估LLM的生物医学推理能力。

### Q2: 有哪些相关研究？

相关工作可归纳为几类：经典生物医学QA基准，如BioASQ、PubMedQA、BioRead，多采用是非/事实型或填空格式，现已面临饱和与污染问题。临床医学基准包括MedQA（USMLE）、MedMCQA、MMLU Medical等，均以多项选择为主，存在答案线索和泄漏风险。近年出现了更丰富的评估形式：HealthBench使用医生撰写的场景和基于准则的评分，K-QA评测完整性和幻觉，LongHealth和ClinIQLink分别测试长上下文聚合和多跳推理。在多跳推理方面，通用领域的HotpotQA、MuSiQue、2WikiMultiHopQA奠定了方法基础但领域不匹配；生物医学中MedHop（使用MedlinePlus）采用多项选择仍存在答案提示，BioHopR基于PrimeKG知识图谱测试显式多跳但答案集受限。MedHopQA相比这些工作：改用开放答案消除线索，使用维基百科作为源材料（更易获取且出现在预训练中但问题仍具挑战性），通过同义词集支持概念级评估，并以隐藏问题减轻污染。

### Q3: 论文如何解决这个问题？

论文通过一个多阶段人工-AI流水线构建了MedHopQA数据集。首先，从维基百科疾病页面（约5000个）出发，通过超链接配对形成候选页面对，限定生物医学相关类别（疾病、症状、基因、化学物等）。16位具有医学/生物信息学背景的标注员手动选择页面对并撰写多跳问题，要求满足五个准则：医学相关性、事实性、稳定性、真正双跳、答案唯一。同时，利用o1模型基于已有问答对生成更多候选，通过盲审（标注员不知道问题来源）确保质量。所有问答对进入公共分诊池，经两轮独立评审（第一轮分诊，第二轮验证）通过后才被接受。此外，设计了一个LLM-as-judge辩论框架，从语法、概念正确性、答案有效性、唯一性四个角度评估每一对，并由人工审核报告进行修正。最后，为每个标准答案从MONDO、NCBI Gene、NCBI Taxonomy等本体收集同义词，经人工筛选后形成评估集。评估时采用词汇匹配（标准化同义词比较）和概念级匹配（MedCPT嵌入投影到本体概念再比较）两种方法，并设计了下拉式评测（1000题嵌入10000题中，答案隐藏）来提升防污染能力。

### Q4: 论文做了哪些实验？

论文在零样本设置下评估了四个前沿LLM：GPT-4o、GPT-5.1、Claude Sonnet 4.5、Gemini 2.5 Pro。每个模型只接收问题和简短指令，不提供支持文档。总体准确率：GPT-5.1最高（83.4%），Gemini 2.5 Pro（79.7%），Claude Sonnet 4.5（77.1%），GPT-4o（66.3%）。按答案类型分析：化学类性能最稳定（约84-89%），解剖类较好（71-83%），疾病类（63-81%）和基因/蛋白类（60-81%）变异性大且区分度强，数值类和染色体位置类因格式要求难度较高。在问题层面，534题被所有模型答对，77题全部答错，表明存在一个共享的“易核心”和持续的难子集。此外进行了概念级验证（MedCPT），在200个随机抽样上的手动审查显示75.5%的准确率，错误以假阴性为主（57.1%），表明同义词覆盖和标准化仍有提升空间，但概念级评估对基因/蛋白、解剖、症状等实体类效果很好（>93%）。

### Q5: 有什么可以进一步探索的点？

局限性包括：1) 仅使用维基百科作为知识源，未来可扩展到PubMed、临床指南等，以增加领域深度；2) 当前问题规模（1000题）仍有限，可通过扩大页面对和自动化生成增大题库；3) 同义词集依赖人工审核，覆盖可能不完整，导致假阴性，未来可利用更丰富的本体和聚合检索自动扩充；4) 评估仅涉及零样本设置，未探索检索增强（RAG）或多步推理链的可解释性分析；5) LLM-as-judge验证框架本身依赖于另一LLM，可能引入偏差，未来可加入多轮人工对抗验证；6) 概念级评估的阈值（0.7）和嵌入模型通用性有待进一步验证。此外，可探索将多跳推理分解为子步骤以解释模型行为，以及将该框架迁移到其他专业领域（如法律、科学文献）。

### Q6: 总结一下论文的主要内容

MedHopQA是一个以疾病为中心的多跳推理基准和评估框架，专为基于LLM的生物医学问答设计。其核心贡献包括：1) 一个包含1000个人工精选、开放答案的多跳问答对数据集，每个问题要求综合两个不同维基百科文章的信息；2) 一个可复现的多阶段构建流水线，融合人类标注、AI增强、盲审、迭代验证和LLM-as-judge质量把关；3) 一套灵活的评估机制，包括词汇匹配和基于MedCPT的概念级匹配，并同义集增强；4) 通过在大规模语料中嵌入隐藏问题的方式，减轻了污染和排行榜博弈。零样本评估四个前沿LLM表明多跳推理仍然是重大挑战，且不同类型问题的难度差异可提供有意义的诊断信号。该框架具有通用性，可推广到其他生物医学子领域。
