---
title: "MemoryDocDataSet: A Benchmark for Joint Conversational Memory and Long Document Reasoning"
authors:
  - "Qiyang Xie"
  - "Jialun Wu"
  - "Xinjie He"
  - "Su Liu"
  - "Shuai Xiao"
  - "Zhiyuan Lin"
  - "Weikai Zhou"
date: "2026-06-03"
arxiv_id: "2606.04442"
arxiv_url: "https://arxiv.org/abs/2606.04442"
pdf_url: "https://arxiv.org/pdf/2606.04442v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Long Document Reasoning"
  - "Multi-session Conversation"
  - "RAG"
  - "Benchmark"
  - "LLM Agent Evaluation"
relevance_score: 8.0
---

# MemoryDocDataSet: A Benchmark for Joint Conversational Memory and Long Document Reasoning

## 原始摘要

AI systems increasingly need to combine two demanding capabilities: navigating multi-session conversation history and performing deep reading comprehension within long documents. Yet no existing benchmark evaluates both simultaneously. We introduce MemoryDocDataSet, a synthetic benchmark of 50 micro-worlds and 1,000 QA pairs in which each instance comprises 3-5 personas, a temporal event graph spanning months of activity, 3-5 real long documents (20,000-50,000 tokens each sourced from the Caselaw Access Project), multi-session conversations grounded on those documents, and 20 question-answer pairs across five reasoning categories. The defining feature is the Hybrid source tag: questions requiring a system to first navigate conversation history to identify which document is relevant, then extract the answer from within that document. Hybrid questions account for 75.1% of the dataset. Dataset quality is characterised through a prompt-sensitivity self-consistency analysis using LLM-as-judge, yielding a median Cohen's $κ= 0.634$ across all 50 micro-worlds. We evaluate six baseline configurations spanning truncated context, long-context LLMs, retrieval-augmented generation (RAG), and memory systems. The best baseline (RAG-Both) achieves 0.358 overall F1 and 0.342 on Hybrid. Document-only retrieval (RAG-Doc) collapses to 0.267 on Hybrid despite achieving 0.453 on Doc-only questions, demonstrating a clear joint-retrieval gap that motivates architectures unifying conversational memory with long-document navigation. We release the dataset, generation pipeline, and all baseline implementations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有AI系统中两个关键能力的评估盲区：长期会话记忆（multi-session conversation memory）与长文档深度阅读理解（long document reasoning）的联合推理。研究背景是当前缺乏同时测试这两种能力的基准数据集。现有基准存在明显不足：记忆类基准（如LoCoMo、LongMemEval）专注于多轮对话中的事实记忆，但完全不含长文档，系统仅需记住对话历史即可获得高分；长文档推理基准（如L-Eval、ZeroSCROLLS）要求处理数十万token的书籍或报告，但缺乏会话结构，系统只需扩展上下文窗口，无需记忆能力。然而实际应用（如法律助手多轮咨询中需回溯过往对话定位合同再精读条款）要求系统必须同时具备两者。因此，本文核心问题是：构建一个能评估系统联合运用会话记忆与长文档导航能力的基准测试。论文通过提出MemoryDocDataSet——包含50个微型世界、1000个QA对的合成基准——专门设计了“Hybrid”类型问题（占75.1%），要求模型先通过会话历史定位相关文档，再在该文档中深度阅读提取答案，从而填补了这一评估空白。

### Q2: 有哪些相关研究？

本文的相关工作可分为以下三类：

1. **多会话对话记忆评测**：包括Beyond Goldfish Memory（MSC数据集，侧重短期人格一致性）、LoCoMo（长对话与时序推理）、LongMemEval（跨会话记忆问答）、MemBench（记忆操作套件）。这些工作均不涉及长文档，仅依赖会话内事实记忆即可得分。

2. **长文档阅读理解评测**：包括L-Eval和ZeroSCROLLS（书籍级多文档阅读，无对话成分）、HotpotQA（短段落多跳推理，无长文档与会话结构）。它们将阅读视为静态任务，缺少对话交互。

3. **检索增强生成（RAG）与记忆系统**：标准RAG索引静态文档，未建模对话时序与文档导航关系；Mem0、Zep等记忆系统跟踪实体但无法进行深度长文档阅读。

本文的核心区别是**首次要求模型联合处理多会话对话历史与长文档**，通过Hybrid源标记（占75.1%问题）强制系统先导航会话定位相关文档，再从中提取答案，暴露了现有方法在混合检索上的关键缺口（RAG-Both F1仅0.342 vs. RAG-Doc在纯文档问题上的0.453）。

### Q3: 论文如何解决这个问题？

该论文通过构建一个名为MemoryDocDataSet的合成基准数据集，并设计六种基线系统进行对比实验，系统性地评估联合对话记忆与长文档推理的能力。核心方法包含一个七阶段全自动生成管道：首先从哈佛法律数据库采集真实长文档（2-5万tokens），然后基于文档生成3-5个角色和包含5-10个时间事件的DAG事件图，再据此生成5轮多会话对话（40%以上需引用文档），接着生成5类问答对（75.1%为“混合型”，即需先检索对话历史定位文档，再从文档中提取答案），最后通过质量验证和数据集分片。架构设计上，六种基线覆盖了截断上下文、长上下文LLM（60k tokens）、三种RAG方案（仅对话、仅文档、联合检索）和基于事实抽取的记忆系统。关键技术创新点包括：Hybrid源标签的引入（强制要求系统同时驾驭对话记忆和文档检索）、LLM-as-judge自一致性评估协议（用Cohen's κ=0.634衡量数据集质量）、以及通过RAG-Doc在混合型问题上的F1骤降0.267（对比其文档类0.453）明确揭示出“联合检索鸿沟”——当前架构无法有效整合跨会话历史与长文档导航，这一发现为未来研发统一记忆-检索架构提供了基准测试和明确指标。

### Q4: 论文做了哪些实验？

论文实验设置了六组基线系统，涵盖当前主流方法：Base LLM（截断上下文，4096 tokens）、Long-Context LLM（完整上下文，60000 tokens）、RAG-Conv（对话检索）、RAG-Doc（文档检索）、RAG-Both（联合检索）和Memory System（图记忆系统）。数据集MemoryDocDataSet包含1000个QA对，来自50个微世界，每个微世界涉及3-5个人物、时间事件图、多篇长法律文档（每篇20k-50k tokens）及多轮对话。问题分为五种推理类型，其中Hybrid问题（需先定位对话中的相关文档再从中提取答案）占75.1%。测试集使用160个QA对，主要指标为Token-level F1和Abstention Accuracy。

关键结果：RAG-Both总体F1最高（0.358），Hybrid F1为0.342，显著高于RAG-Doc的0.267（文档检索仅聚焦文档，缺乏对话导航能力）。RAG-Doc在Doc-only问题上F1达0.453，但Hybrid表现崩溃，体现“联合检索鸿沟”。Long-Context LLM虽获完整上下文，总体F1仅0.323，且abstention准确率最低（0.844），表明扩展窗口无法替代结构化检索。Memory System总体F1为0.325，Doc-only表现良好（0.459）。实验揭示了现有方法缺乏“两步式”检索策略的关键缺陷。

### Q5: 有什么可以进一步探索的点？

论文的局限性与未来研究方向主要集中在以下几个方面。首先，文档语料仅来自美国法院意见，存在领域偏差，未来可扩展至更多文档类型和领域以提升泛化性。其次，对话由LLM生成，可能缺乏真实对话中的隐式指代、语用推理等自然语言现象，后续可引入真实对话数据或采用更复杂的对话生成策略。自动生成的QA对可能存在答案唯一性不足、干扰项不够真实等问题，需要人工标注验证，尤其应测量人类在Hybrid问题上的表现作为上界。此外，LLM-as-judge验证存在自我宽松偏差，未来可引入不同模型家族的评判器或人工评估。关键架构缺陷是现有方法均未实现分步检索策略——先用对话上下文定位相关文档，再从中提取答案，这导致Hybrid难题的解决效率低下。改进方向可设计显式的引用图或记忆系统，将对话会话与文档引用编码为图边，并实现条件化检索；或探索结构化知识图谱与检索增强生成（RAG）的融合方案。当前固定30% Hybrid问题阈值源自设计而非真实任务分布，未来需通过用户研究确定更合理的比例。最后，长上下文模型“迷失在中间”的问题提示可考虑分层注意力或复合索引结构来优化长文本的检索与推理效率。

### Q6: 总结一下论文的主要内容

本文提出MemoryDocDataSet基准，旨在填补现有AI评估中同时测试跨会话记忆与长文档推理能力的空白。现有记忆基准（如LoCoMo）或长文档基准（如L-Eval）均未结合这两项任务。该基准包含50个微观世界和1000个QA对，每个实例整合3-5个角色、时间事件图、3-5篇真实长文档（每篇2-5万token）及多会话对话。核心创新是混合源标签：75.1%的问题需先通过对话历史确定相关文档，再深入文档提取答案。评估六种基线配置，最佳方案（RAG-Both）在混合问题上的F1仅0.342，而纯文档检索策略（RAG-Doc）因结构缺陷在该类问题中F1仅0.267。研究表明现有系统存在明显的联合检索差距，亟需在架构层面统一会话记忆与长文档导航能力。该数据集首次量化了这一挑战，并为后续研究提供了完整工具链。
