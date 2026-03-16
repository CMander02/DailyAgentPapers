---
title: "Test-Time Strategies for More Efficient and Accurate Agentic RAG"
authors:
  - "Brian Zhang"
  - "Deepti Guntur"
  - "Zhiyang Zuo"
  - "Abhinav Sharma"
  - "Shreyas Chaudhari"
  - "Wenlong Zhao"
  - "Franck Dernoncourt"
  - "Puneet Mathur"
  - "Ryan Rossi"
  - "Nedim Lipka"
date: "2026-03-12"
arxiv_id: "2603.12396"
arxiv_url: "https://arxiv.org/abs/2603.12396"
pdf_url: "https://arxiv.org/pdf/2603.12396v1"
categories:
  - "cs.IR"
  - "cs.AI"
tags:
  - "Agentic RAG"
  - "检索增强生成"
  - "多跳问答"
  - "推理效率"
  - "测试时优化"
  - "上下文集成"
  - "去重模块"
  - "Search-R1"
relevance_score: 7.5
---

# Test-Time Strategies for More Efficient and Accurate Agentic RAG

## 原始摘要

Retrieval-Augmented Generation (RAG) systems face challenges with complex, multihop questions, and agentic frameworks such as Search-R1 (Jin et al., 2025), which operates iteratively, have been proposed to address these complexities. However, such approaches can introduce inefficiencies, including repetitive retrieval of previously processed information and challenges in contextualizing retrieved results effectively within the current generation prompt. Such issues can lead to unnecessary retrieval turns, suboptimal reasoning, inaccurate answers, and increased token consumption.
  In this paper, we investigate test-time modifications to the Search-R1 pipeline to mitigate these identified shortcomings. Specifically, we explore the integration of two components and their combination: a contextualization module to better integrate relevant information from retrieved documents into reasoning, and a de-duplication module that replaces previously retrieved documents with the next most relevant ones. We evaluate our approaches using the HotpotQA (Yang et al., 2018) and the Natural Questions (Kwiatkowski et al., 2019) datasets, reporting the exact match (EM) score, an LLM-as-a-Judge assessment of answer correctness, and the average number of turns.
  Our best-performing variant, utilizing GPT-4.1-mini for contextualization, achieves a 5.6% increase in EM score and reduces the number of turns by 10.5% compared to the Search-R1 baseline, demonstrating improved answer accuracy and retrieval efficiency.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决检索增强生成（RAG）系统在处理复杂、多跳问题时面临的效率与准确性问题。研究背景是，现有的代理式框架（如Search-R1）通过迭代检索和生成来应对复杂查询，但在实际应用中暴露出明显不足。现有方法的缺陷主要包括：在迭代过程中可能重复检索已处理过的信息，导致计算资源浪费；同时，难以将检索到的文档信息有效地整合到当前生成提示中，这会影响推理质量，造成不必要的检索轮次、次优推理、答案不准确以及令牌消耗增加等问题。

本文的核心问题是：如何在测试阶段对Search-R1这类代理式RAG流程进行改进，以同时提升其回答准确性和检索效率。为此，论文提出了两种测试时策略模块：一是上下文整合模块，旨在更好地将检索文档中的相关信息融入推理过程；二是去重模块，用新的相关文档替换已检索过的内容，避免重复。通过结合这些模块，研究试图减少无效检索轮次、优化推理路径，从而在准确率和效率之间取得更好平衡。实验在HotpotQA和Natural Questions数据集上进行，最终最佳变体在准确率和检索轮次上均显著优于基线，验证了所提策略的有效性。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提升检索增强生成（RAG）系统处理复杂问题的能力展开，可分为方法类和应用评测类。

在**方法类**研究中，核心是应对多跳问答的挑战。传统的单轮检索RAG在处理此类问题时效果有限，因此出现了迭代式的智能体框架，如本文的基线系统Search-R1（Jin et al., 2025）。这类方法通过多轮检索与推理来分解复杂问题，但如本文所指出的，它们容易导致信息重复检索和上下文整合不佳的效率问题。本文的工作直接建立在此类智能体RAG框架之上，旨在通过测试时（test-time）的改进模块来优化其效率与准确性，而非提出一个全新的架构。

在**应用评测类**方面，相关研究为评估提供了标准。本文使用HotpotQA和Natural Questions这两个经典的多跳问答与开放域问答数据集进行评测，这延续了该领域主流的评估范式。同时，本文采用精确匹配（EM）分数和基于LLM的评判来评估答案正确性，这也是相关工作中常见的评估指标。本文的创新在于，在沿用这些标准评测设置的基础上，额外将“平均检索轮次”作为一个关键的效率指标进行报告和分析，突出了对智能体RAG运行成本的关注。

综上，本文与相关工作的关系是继承与优化。它基于现有的智能体RAG框架（如Search-R1），并针对其已知的效率缺陷，提出了具体的上下文整合与去重模块进行改进，在公认的评测基准上验证了其在效果与效率上的提升。

### Q3: 论文如何解决这个问题？

论文针对Search-R1等智能体化RAG系统在复杂多跳问题处理中存在的检索效率低下和上下文整合不足问题，提出在测试时对原有流程进行改进，核心方法是集成两个关键模块：上下文整合模块与去重模块。

整体框架沿袭Search-R1的迭代检索-生成流程，但在每次迭代中嵌入新模块。主要组件包括：1）**上下文整合模块**：在生成答案前，对当前检索到的文档进行提炼和重组，提取与问题最相关的信息，并将其结构化地融入生成提示中，以提升推理的连贯性和准确性。该模块使用LLM（如GPT-4.1-mini）实现，通过对检索文档进行摘要、关键信息抽取或重写，帮助模型更有效地利用已有信息。2）**去重模块**：在每次检索时，识别并过滤掉与之前迭代中已检索文档高度相似的内容，转而获取次优但新颖的文档，以避免信息重复和冗余检索。这通过计算文档间的相似度（如基于嵌入的余弦相似度）来实现，确保每次迭代都能引入新信息。

创新点在于将这两个模块协同工作：上下文整合优化了信息利用质量，而去重则提高了检索过程的效率。两者结合后，系统在保持甚至提升答案准确率（EM分数提升5.6%）的同时，显著减少了平均迭代轮次（降低10.5%），从而降低了计算开销和令牌消耗。该方法在HotpotQA和Natural Questions数据集上验证了其有效性，体现了在测试时通过轻量级修改提升智能体RAG性能的实用策略。

### Q4: 论文做了哪些实验？

论文的实验主要围绕改进Search-R1代理框架的效率与准确性展开。实验设置上，作者在Search-R1流程中集成了两种测试时模块：一是上下文整合模块，旨在将检索到的文档信息更有效地融入推理提示；二是去重模块，用于替换已检索过的文档，引入新的相关文档。这些模块被单独及组合测试。

数据集方面，研究使用了HotpotQA（用于复杂多跳问题）和Natural Questions（用于开放域问答）两个基准测试。对比方法以原始的Search-R1作为基线。

评估指标包括：精确匹配分数、基于LLM-as-a-Judge的答案正确性评估，以及平均检索轮次。关键结果显示，最佳变体（使用GPT-4.1-mini进行上下文整合）相比Search-R1基线，在精确匹配分数上提升了5.6%，同时将检索轮次减少了10.5%，有效证明了其在提升答案准确性和检索效率方面的优势。

### Q5: 有什么可以进一步探索的点？

该论文的探索点主要集中在通过上下文整合与去重模块优化迭代式RAG的测试时效率，但仍存在以下局限性与未来方向：首先，其模块设计依赖特定LLM（如GPT-4.1-mini），在不同模型或开源架构上的泛化能力未经验证；其次，去重策略仅基于文档替换，未考虑对已检索信息的动态压缩或摘要化处理，可能遗漏关键细节。未来可探索更细粒度的记忆管理机制，例如引入向量缓存或语义相似度阈值，避免冗余检索的同时保留信息完整性。此外，研究可扩展至多模态或跨领域问答，测试模块在复杂推理场景（如需结合文本与表格数据）中的适应性。最后，将训练时优化与测试时策略结合，通过强化学习动态调整检索决策，可能进一步提升端到端效率与准确性。

### Q6: 总结一下论文的主要内容

本文针对迭代式智能体RAG框架（如Search-R1）在处理复杂多跳问题时存在的检索效率低下和上下文整合不佳的问题，提出在测试时对流程进行优化。核心方法是在原有流水线中集成两个模块：一是上下文整合模块，旨在将检索到的文档信息更有效地融入生成提示以改善推理；二是去重模块，用新的相关文档替换已检索过的内容以避免重复。研究在HotpotQA和Natural Questions数据集上评估了这些策略，采用精确匹配分数、LLM作为评判者的答案正确性评估以及平均检索轮次作为指标。实验结果表明，最佳方案（使用GPT-4.1-mini进行上下文整合）相比Search-R1基线，在精确匹配分数上提升了5.6%，同时将检索轮次减少了10.5%。这证实了所提方法能显著提高答案准确性并增强检索效率，为优化智能体RAG系统的实际部署提供了有效策略。
