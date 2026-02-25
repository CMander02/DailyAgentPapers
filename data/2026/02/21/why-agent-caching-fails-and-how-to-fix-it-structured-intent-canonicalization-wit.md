---
title: "Why Agent Caching Fails and How to Fix It: Structured Intent Canonicalization with Few-Shot Learning"
authors:
  - "Abhinaba Basu"
date: "2026-02-21"
arxiv_id: "2602.18922"
arxiv_url: "https://arxiv.org/abs/2602.18922"
pdf_url: "https://arxiv.org/pdf/2602.18922v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "Agent 数据合成"
  - "Agent 评测/基准"
  - "工具使用"
  - "成本优化"
  - "意图识别"
  - "缓存机制"
  - "结构化表示"
  - "少样本学习"
relevance_score: 8.5
---

# Why Agent Caching Fails and How to Fix It: Structured Intent Canonicalization with Few-Shot Learning

## 原始摘要

Personal AI agents incur substantial cost via repeated LLM calls. We show existing caching methods fail: GPTCache achieves 37.9% accuracy on real benchmarks; APC achieves 0-12%. The root cause is optimizing for the wrong property -- cache effectiveness requires key consistency and precision,
  not classification accuracy. We observe cache-key evaluation reduces to clustering evaluation and apply V-measure decomposition to separate these on n=8,682 points across MASSIVE, BANKING77, CLINC150, and NyayaBench v2, our new 8,514-entry multilingual agentic dataset (528 intents, 20 W5H2 classes, 63 languages). We introduce W5H2, a structured intent decomposition framework. Using SetFit with 8 examples per class, W5H2 achieves 91.1%+/-1.7% on MASSIVE in ~2ms -- vs 37.9% for
  GPTCache and 68.8% for a 20B-parameter LLM at 3,447ms. On NyayaBench v2 (20 classes), SetFit achieves 55.3%, with cross-lingual transfer across 30 languages. Our five-tier cascade handles 85% of interactions locally, projecting 97.5% cost reduction. We provide risk-controlled selective prediction guarantees via RCPS with nine bound families.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决个人AI代理因重复调用大语言模型（LLM）而产生的高昂成本和延迟问题。现有缓存方法（如基于语义相似性的GPTCache或基于关键词提取的APC）在真实场景中效果很差（准确率分别仅为37.9%和0-12%），因为它们优化了错误的属性：它们追求分类准确性，而有效的缓存需要**缓存键的一致性和精确性**。具体来说，语义缓存会将意图不同但语义相近的查询（如“查看邮件”和“发送邮件”）错误匹配，而关键词方法则因查询过短而失效。

因此，论文的核心问题是：**如何为个人AI代理设计一个高效、准确且跨语言的意图缓存机制，以大幅降低LLM调用成本和延迟**。为此，论文提出了W5H2结构化意图规范化框架，将查询分解为结构化字段（如What、Where），并以此构建语言无关的缓存键。通过结合Few-Shot学习和级联架构，该方法在提升缓存准确率（在MASSIVE数据集上达91.1%）的同时，实现了极低的延迟（约2毫秒），从而有望将API成本降低97.5%。

### Q2: 有哪些相关研究？

相关研究主要涵盖以下几个方向：

1. **LLM语义缓存**：如GPTCache（基于嵌入相似性缓存LLM响应）、RAGCache（扩展至检索增强生成场景）、LangCache（通过微调领域特定嵌入优化语义缓存）以及vCache（引入自适应相似度阈值的验证缓存）。这些方法均依赖嵌入相似度，面临精度与召回率的固有权衡，而本文指出缓存有效性更需关注键的一致性与精确性。

2. **智能体规划缓存**：APC（Agent Plan Caching）通过提取关键词缓存工具使用规划，与本文目标最为接近。但APC仅针对英语网页导航任务，且未形式化区分一致性与准确性，而本文提出结构化意图分解框架W5H2，支持多语言并明确优化缓存键属性。

3. **结构化分解缓存**：SemanticALLI独立验证了在智能体系统中对推理过程（而非仅响应）进行缓存的有效性，证实查询的结构化分解能提升缓存性能，与本文的分解思路相互印证。

4. **少样本分类技术**：SetFit（基于对比学习微调句子Transformer）和原型网络是少样本分类的代表方法。本文首次将SetFit应用于智能体规划缓存，仅需每类8个示例即可实现高效意图分类。

5. **查询规范化技术**：借鉴数据库（预处理语句指纹）、编译器（哈希一致化）、搜索引擎（查询归一化）等领域的规范化思想，本文首次将智能体意图缓存明确界定为规范化问题，突破了以往NLP/智能体研究的局限。

6. **意图识别基础**：联合意图与槽填充模型（如JointBERT）、DIET分类器以及MASSIVE数据集为意图识别提供了技术基础。本文将这些技术与智能体规划缓存直接结合，构建了从意图识别到缓存生成的完整桥梁。

本文与这些工作的关系在于：现有研究大多孤立优化缓存的某一维度（如相似度、关键词或嵌入），缺乏对缓存键本质属性的统一框架。本文通过形式化缓存键生成作为规范化问题，并引入V-measure分解量化一致性与精确性，系统性地解决了现有缓存方法失效的根本原因。

### Q3: 论文如何解决这个问题？

论文通过重构问题本质、提出结构化意图规范化框架W5H2，并设计五级级联缓存架构来解决智能体缓存失效问题。核心方法是将意图识别从分类问题重新定义为规范化问题：关键不是预测准确的地面真实标签，而是确保相同意图的查询始终映射到相同的缓存键，即追求键的一致性和精确性，而非分类准确率。为此，论文形式化了安全规范化目标，在保证桶内意图纯度（安全性）的前提下最大化缓存复用率（完整性）。

W5H2框架将用户请求分解为七个结构化字段（Who、What、When、Where、Why、How、How Much），并仅使用规范化的（What, Where）对作为缓存键，而将变量参数（如实体、时间、数量）分离出来在执行时注入。这种设计确保了参数变化不会导致缓存碎片化，且支持跨语言规范化。

关键技术包括采用基于Few-Shot学习的SetFit对比模型进行意图规范化，该模型仅需每类8个示例，在约2ms内达到91.1%的准确率，显著优于传统缓存方案。为确保安全性，论文引入了风险控制的选择性预测（RCPS），通过置信度阈值和多种边界族（如Hoeffding、LTT、Empirical Bernstein）提供统计保证，控制不安全缓存命中的风险。

架构上，论文设计了五级级联缓存：第0层（查询指纹，<1ms）、第1层（监督分类器，~5-10ms）、第2层（SetFit分类，~2-10ms）、第3层（廉价LLM）和第4层（深度智能体）。本地层（0-2层）可处理85%的请求，实现零边际成本，结合风险控制机制，在保证安全性的同时将成本降低97.5%。整个方案通过结构化分解、轻量级学习和级联决策，有效平衡了缓存效率、安全性与成本。

### Q4: 论文做了哪些实验？

论文在四个基准数据集上进行了实验：MASSIVE（8个意图类）、BANKING77（77个类）、CLINC150（150个类）以及新构建的多语言Agent数据集NyayaBench v2（20个W5H2超类，源自528个细粒度意图，涵盖63种语言）。实验对比了多种方法：零样本自然语言推理模型（MiniLMv2、mDeBERTa）、基于规则的W5H2方法、少样本对比学习模型SetFit（包括22M参数的英文版和118M参数的多语言版）、相似性基线（模拟GPTCache的嵌入K-Means聚类和APC关键词提取）以及LLM基线（GPT-oss-20b的零样本和少样本提示）。评估指标包括分类准确率、缓存命中率、延迟、V-measure（分解为同质性h和完整性c）和调整互信息（AMI）。

主要结果显示：在真实的Agent数据NyayaBench v2上，SetFit-EN以每类8样本训练达到55.3%的准确率和98.3%的命中率，显著优于GPTCache KMeans的49.1%；在MASSIVE上，SetFit-EN达到91.1%的准确率，远超GPT-oss-20b零样本的68.8%（延迟降低700倍以上）。V-measure分析表明，缓存键评估本质上是聚类评估，SetFit在一致性和精确性上均优于基线。此外，仅用英文数据训练的SetFit-Multi在30种语言上实现了平均37.7%的零样本跨语言迁移，其中印欧语系语言迁移效果最佳。实验还验证了五级级联策略，可本地处理85%的交互，预计降低97.5%的成本。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于：W5H2框架依赖预定义的意图结构（如W5H2类），可能难以泛化到更开放、动态的智能体任务；其few-shot学习在极端低资源或未见意图类别上性能可能下降；当前评估集中于特定领域数据集，在复杂、多轮对话或需要深度推理的智能体场景中的有效性尚未验证。  
未来可探索的方向包括：1）开发自适应意图结构，使框架能动态扩展或调整类别以应对开放域任务；2）结合大模型的零样本能力与高效的小模型缓存，构建更鲁棒的混合系统；3）将方法扩展到多智能体协作场景，研究意图一致性在跨智能体缓存中的挑战；4）探索强化学习或在线学习机制，使缓存策略能根据用户反馈持续优化。

### Q6: 总结一下论文的主要内容

这篇论文的核心贡献是揭示了现有AI智能体缓存方法（如GPTCache）效果不佳的根本原因，并提出了创新的解决方案。作者指出，传统方法追求分类准确率，但缓存有效的关键在于缓存键的一致性和精确性。为此，他们提出了W5H2结构化意图规范化框架，将用户查询分解为Who、What、When等七个维度，将缓存问题转化为聚类评估问题。通过在包含63种语言的新数据集NyayaBench v2等基准上的实验，论文证明，使用轻量级Few-Shot学习模型SetFit（每类仅需8个示例）即可实现超过91%的高精度和约2毫秒的极低延迟，显著优于大语言模型和现有缓存方案。最终，论文设计了一个五级级联系统，可本地处理85%的交互，预计能降低97.5%的成本，并通过风险控制预测选择方法为系统可靠性提供了理论保证。这项研究为构建高效、低成本、可靠的个人AI智能体提供了重要的理论依据和实用框架。
