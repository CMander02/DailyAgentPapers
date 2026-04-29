---
title: "Agentic retrieval-augmented reasoning reshapes collective reliability under model variability in radiology question answering"
authors:
  - "Mina Farajiamiri"
  - "Jeta Sopa"
  - "Saba Afza"
  - "Lisa Adams"
  - "Felix Barajas Ordonez"
  - "Tri-Thien Nguyen"
  - "Mahshad Lotfinia"
  - "Sebastian Wind"
  - "Keno Bressem"
  - "Sven Nebelung"
  - "Daniel Truhn"
  - "Soroosh Tayebi Arasteh"
date: "2026-03-06"
arxiv_id: "2603.06271"
arxiv_url: "https://arxiv.org/abs/2603.06271"
pdf_url: "https://arxiv.org/pdf/2603.06271v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "agentic reasoning"
  - "retrieval-augmented generation"
  - "model variability"
  - "radiology QA"
  - "collective reliability"
  - "clinical decision support"
relevance_score: 7.5
---

# Agentic retrieval-augmented reasoning reshapes collective reliability under model variability in radiology question answering

## 原始摘要

Agentic retrieval-augmented reasoning pipelines are increasingly used to structure how large language models (LLMs) incorporate external evidence in clinical decision support. These systems iteratively retrieve curated domain knowledge and synthesize it into structured reports before answer selection. Although such pipelines can improve performance, their impact on reliability under model variability remains unclear. In real-world deployment, heterogeneous models may align, diverge, or synchronize errors in ways not captured by accuracy. We evaluated 34 LLMs on 169 expert-curated publicly available radiology questions, comparing zero-shot inference with a radiology-specific multi-step agentic retrieval condition in which all models received identical structured evidence reports derived from curated radiology knowledge. Agentic inference reduced inter-model decision dispersion (median entropy 0.48 vs. 0.13) and increased robustness of correctness across models (mean 0.74 vs. 0.81). Majority consensus also increased overall (P<0.001). Consensus strength and robust correctness remained correlated under both strategies (\r{ho}=0.88 for zero-shot; \r{ho}=0.87 for agentic), although high agreement did not guarantee correctness. Response verbosity showed no meaningful association with correctness. Among 572 incorrect outputs, 72% were associated with moderate or high clinically assessed severity, although inter-rater agreement was low (\k{appa}=0.02). Agentic retrieval therefore was associated with more concentrated decision distributions, stronger consensus, and higher cross-model robustness of correctness. These findings suggest that evaluating agentic systems through accuracy or agreement alone may not always be sufficient, and that complementary analyses of stability, cross-model robustness, and potential clinical impact are needed to characterize reliability under model variability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要研究在模型变异性条件下，基于大语言模型（LLM）的智能体检索增强推理（agentic retrieval-augmented reasoning）管道如何影响集体可靠性。具体来说，论文聚焦于放射学问答场景，评估了34个异构LLM在169个专家策划的放射学问题上的表现。研究问题包括：智能体推理是否减少模型间的决策离散度、增强共识强度、提高正确性的跨模型鲁棒性，以及共识与正确性之间的耦合关系。此外，论文还探讨了输出冗长度作为正确性代理的可靠性，以及错误答案的临床严重性分布。核心目标是超越单模型准确率评估，从稳定性、鲁棒性和临床影响等多维度刻画系统在模型变化下的可靠性，为高风险临床应用提供更全面的评估框架。

### Q2: 有哪些相关研究？

论文的相关研究主要集中在以下几个领域：首先，检索增强生成（RAG）和多步推理管道在临床决策支持中的应用，例如RadioRAG和RaR研究，这些工作通过检索外部知识来提升LLM在医学任务上的性能。其次，关于LLM可靠性和变异性的研究，涉及模型间一致性、错误同步化以及集体行为分析。第三，临床AI评估方法，包括错误严重性标注和安全感知评估。本文与这些工作的关系在于：它扩展了现有RAG管道的评估，首次系统性地分析在模型变异性下智能体推理对集体可靠性的影响；引入了多维度评估框架（如决策熵、共识强度、鲁棒性），补充了传统准确率评估；并强调了临床严重性作为安全关键维度。论文与先前工作的区别在于，它不专注于提出新管道，而是通过控制实验深入探讨现有管道在异构模型环境下的行为特性。

### Q3: 论文如何解决这个问题？

论文通过设计一个控制实验框架来解决这个问题。首先，构建了一个标准化智能体检索增强推理管道，该管道从策划的放射学知识库中检索相关信息，并将其合成为结构化证据报告，然后所有LLM在相同条件下接收这份报告。实验比较了零样本推理（仅提供问题）和智能体推理（附加结构化证据）两种条件。核心方法包括：使用34个异构LLM（涵盖不同厂商、规模和医学适配模型）在169个放射学多选题上进行评估。数据集包括Benchmark-RadQA（104题）和Board-RadQA（65题）。分析从多个维度展开：决策稳定性（通过香农熵测量答案分布离散度）、共识强度（多数分数，即选择众数答案的模型比例）、正确性鲁棒性（选择正确答案的模型比例）、共识与正确性的耦合（斯皮尔曼相关）、冗长度与正确性的关联（通过克利夫德尔塔效应大小）、以及临床严重性（由三位放射科医师独立标注错误选项的潜在临床影响）。统计方法包括配对非参数检验和Bootstrap置信区间，以确保结果稳健。通过这种多维度分析，论文能够区分集体行为的结构性变化与正确性变化，并揭示智能体推理如何重塑可靠性。

### Q4: 论文做了哪些实验？

论文进行了全面的实验和统计分析。实验设置包括：34个LLM在169个放射学问题上，分别在零样本和智能体推理条件下回答，产生每模型每问题的离散答案。主要实验和结果包括：1. 决策稳定性分析：智能体推理显著降低模型间熵（中位熵从0.48降至0.13，P=5.6×10⁻⁹），表明决策更集中。2. 共识强度分析：多数分数增加（中位从0.85升至0.97，P=2.9×10⁻⁵），但共识增加并不总是与正确性一致（如11个问题中共识增加但多数错误）。3. 正确性鲁棒性分析：平均鲁棒性从0.74提高到0.81（P=5.6×10⁻⁹），但存在罕见的鲁棒性崩溃案例（如ΔR=-0.79）。4. 共识与正确性耦合：两者强相关（零样本ρ=0.88，智能体ρ=0.87），但高共识不一定保证正确性（如少数高共识低鲁棒性案例）。5. 冗长度分析：输出长度与正确性关联微弱或无意义（智能体下中位长度几乎相同）。6. 临床严重性评估：572个错误输出中72%为中度或高度严重，但评分者间一致性低（κ=0.02）。实验还包括单模型准确率变化分析，显示智能体推理对较小模型提升更显著。所有分析均使用配对检验和效应大小报告，确保结果可靠。

### Q5: 有什么可以进一步探索的点？

论文指出了几个局限性及未来方向。首先，评估基于有限数据集（169个问题），限制了细粒度子组分析和尾部风险统计能力，未来可扩展至更大、更多样的数据集，包括不同病理和难度级别。其次，评估仅为文本，未整合影像或多模态数据，而真实放射学工作流依赖图像和临床上下文，未来应将集体行为框架扩展至多模态设置。第三，智能体管道固定（检索和证据合成一致），可能限制架构多样性，未来需探索不同检索策略、证据多样性或报告结构对可靠性的影响。第四，所有模型接收相同检索上下文，这可能放大协调错误，未来可研究检索多样性或质量指示器来减少同步失败。第五，临床严重性标注主观性强，评分者一致性低，需开发更标准化的严重性评估方法。第六，集体可靠性评估可进一步结合不确定性量化、校准分析或用户信任研究，以全面理解实际部署中的风险。这些方向有助于改进智能体系统在高风险场景中的稳健性和安全性。

### Q6: 总结一下论文的主要内容

这篇论文研究了智能体检索增强推理管道在模型变异性下对集体可靠性的影响，特别是在放射学问答任务中。通过评估34个LLM在169个问题上的表现，论文比较了零样本推理和智能体推理条件，并引入多维度评估框架，包括决策稳定性、共识强度、正确性鲁棒性、共识-正确性耦合、冗长度关联和临床严重性。核心发现是：智能体推理显著减少模型间离散度、增强共识和提高跨模型正确性，但存在罕见的协调失败和临床严重错误。共识强度与正确性强相关，但高共识不保证正确性；冗长度作为正确性代理不可靠；错误输出中72%涉及中度或高度临床风险。论文强调，仅靠准确率或共识不足以评估可靠性，需综合稳定性、鲁棒性和临床影响。这些结果为设计安全可靠的智能体决策支持系统提供了重要见解，尤其在高风险医疗应用中。
