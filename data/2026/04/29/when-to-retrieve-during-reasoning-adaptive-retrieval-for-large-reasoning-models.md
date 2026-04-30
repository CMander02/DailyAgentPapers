---
title: "When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models"
authors:
  - "Dongxin Guo"
  - "Jikun Wu"
  - "Siu Ming Yiu"
date: "2026-04-29"
arxiv_id: "2604.26649"
arxiv_url: "https://arxiv.org/abs/2604.26649"
pdf_url: "https://arxiv.org/pdf/2604.26649v1"
categories:
  - "cs.IR"
  - "cs.AI"
  - "cs.CL"
tags:
  - "大推理模型"
  - "自适应检索"
  - "检索增强生成"
  - "推理中检索"
  - "不确定性检测"
  - "多跳推理"
relevance_score: 8.5
---

# When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models

## 原始摘要

Large reasoning models such as DeepSeek-R1 and OpenAI o1 generate extended chains of thought spanning thousands of tokens, yet their integration with retrieval-augmented generation (RAG) remains fundamentally misaligned. Current RAG systems optimize for providing context before reasoning begins, while reasoning models require evidence injection during multi-step inference chains. We introduce ReaLM-Retrieve, a reasoning-aware retrieval framework that addresses this mismatch through three key innovations: (1) a step-level uncertainty detector that identifies knowledge gaps at reasoning-step granularity rather than token or sentence level; (2) a retrieval intervention policy that learns when external evidence maximally benefits ongoing reasoning; and (3) an efficiency-optimized integration mechanism that reduces per-retrieval overhead by 3.2x compared to naive integration. Experiments on MuSiQue, HotpotQA, and 2WikiMultiHopQA demonstrate that ReaLM-Retrieve achieves on average 10.1% absolute improvement in answer F1 over standard RAG (range: 9.0-11.8% across the three benchmarks) while reducing retrieval calls by 47% compared to fixed-interval approaches like IRCoT (all improvements significant at p<0.01, paired bootstrap). On the challenging MuSiQue benchmark requiring 2-4 hop reasoning, our method achieves 71.2% F1 with an average of only 1.8 retrieval calls per question. Analysis shows that ReaLM-Retrieve also improves retrieval quality itself, achieving 81.3% Recall@5 with consistently higher precision and MRR than fixed-interval baselines on supporting evidence, establishing new state-of-the-art efficiency-accuracy trade-offs for reasoning-intensive retrieval tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型推理模型与检索增强生成（RAG）系统之间的根本性不匹配问题。研究背景是，DeepSeek-R1、OpenAI o1这类大型推理模型能生成数千token的扩展思维链，展现自我验证、回溯等高级推理行为，但在需要外部事实知识的任务上表现不佳，甚至出现事实准确率下降和幻觉增加的问题。现有RAG系统的核心缺陷在于时间错配：它们采用“先检索后生成”范式，假设单次检索在推理开始前提供上下文就足够，而推理模型在生成多步推理链的中间过程可能遇到无法预先预测的知识缺口。虽然IRCoT、FLARE等迭代检索方法尝试在生成中穿插检索，但它们是为标准语言模型设计的，与推理模型存在三大不兼容：①粒度不匹配，现有方法在词元或句子级别触发检索，而推理模型以逻辑推理步为单元；②信号不可用，依赖token概率或内部注意力状态的方法无法用于o1这类只输出结果的模型；③效率崩溃，固定间隔检索在长推理链上检索开销巨大。因此，本文要解决的核心问题是，设计一种推理感知的检索框架，能在推理步粒度自适应地检测知识缺口，学习何时检索能最大化收益，并通过高效集成减少检索开销，从而在提升答案准确性的同时降低检索成本。

### Q2: 有哪些相关研究？

相关研究可分为四类。**方法类**中，IRCoT采用固定间隔检索（每句话后检索），虽在短链推理有效，但面对数千token的推理链时检索开销过大；FLARE基于token概率触发检索，但无法用于仅输出完整推理链的模型；DRAGIN依赖注意力熵等内部状态，而Self-RAG通过微调学习特殊token，均不适用于黑盒或专有模型。本文ReaLM-Retrieve的独特之处在于以推理步骤粒度检测知识缺口，仅需低开销的言语化置信度与实体覆盖熵，无需模型内部状态或微调。**自适应策略类**中，Adaptive-RAG和Open-RAG在查询层面决定检索必要性，而本文在推理中动态决策；同步工作Dynamic Search-R1通过RL优化每个子查询的检索深度，与本文的检索时机优化正交且互补。**大推理模型类**中，Search-R1用RL训练模型决定何时搜索，但本文聚焦检索系统层面优化，而非模型训练。**不确定性估计类**中，语义熵、自一致性等方法采样开销大（5-20倍），本文设计了轻量级RSUS信号，结合言语化置信度与实体覆盖熵，计算开销低于1%。总体而言，本文在推理过程自适应检索的粒度（步骤级 vs 查询级）、系统兼容性（无需微调或内部状态）和效率（减少47%检索调用）上形成了差异化贡献。

### Q3: 论文如何解决这个问题？

ReaLM-Retrieve通过一个三阶段自适应检索框架解决大型推理模型在长链推理（12K-25K token）中知识缺口与检索时机错配的问题。核心方法包括三个创新组件：

1. **推理步骤分割与不确定性估计**：首先使用一个3层Transformer编码器（隐藏维度256，4注意力头）将推理链分割为语义连贯的推理步骤（平均每步127 token，比IRCoT的句子级分割长5倍），分割器在2,847条人工标注的DeepSeek-R1推理轨迹上训练，F1达94.2%。针对每个步骤计算Reasoning Step Uncertainty Score (RSUS)，由三个互补信号加权合成：U_verb（通过提示模型自评置信度或MLP代理，AUROC 0.71）、U_ent（基于命名实体的检索得分熵）、U_cons（对关键步骤采样3个替代推理链计算一致性），三者计算开销均低于推理成本的3%。

2. **学习式干预策略**：轻量级策略网络（带注意力机制的MLP）基于RSUS分数、步骤语义嵌入和推理阶段位置特征，判断是否触发检索。该策略在验证集上优化α, β, γ权重以最大化检索效益，实现自适应决策而非固定间隔检索。

3. **高效检索集成机制**：将检索结果压缩为语义摘要后，以3.2倍速度注入推理上下文，避免破坏推理连贯性。整体流程形成前瞻性检测循环：分段→RSUS评分→策略决策→检索集成。相比IRCoT的固定间隔检索，该方法检索调用减少47%（从3.4次降至1.8次），在MuSiQue等基准上F1平均提升10.1%。关键创新在于实现了步级粒度的知识缺口检测与学习式干预，首次将RAG与推理模型的时序结构对齐。

### Q4: 论文做了哪些实验？

论文在MuSiQue（2-4跳推理，24814个问题）、HotpotQA（完整维基百科设置，520万段落）和2WikiMultiHopQA（跨文档推理）三个多跳问答基准上进行了实验。对比方法包括：No Retrieval（闭式推理）、Single RAG（标准检索-生成）、IRCoT（固定间隔检索）、FLARE（基于令牌概率触发检索）、Self-RAG（自反思检索，使用Llama-2-13B微调模型）和Search-R1（强化学习检索决策）。主要使用DeepSeek-R1-Distill-Qwen-32B进行消融实验，用DeepSeek-R1-671B报告主要结果，检索器为ColBERTv2（k=5）。主要结果：在R1-32B上，ReaLM-Retrieve在MuSiQue达到71.2% F1（仅1.8次检索调用），比IRCoT（65.4% F1，3.4次调用）绝对提升5.8%（p<0.01），检索调用减少47%；在HotpotQA和2WikiMultiHopQA上分别达到71.8%和69.7% F1。在R1-671B上，MuSiQue达到77.8% F1，比Search-R1高4.4%（p<0.01）。效率方面，每查询1.8次检索调用，端到端延迟14.1秒（仅比无检索增加1.7秒），每次检索优化至0.66秒（比朴素交织快3.2倍），推理令牌数9489个。

### Q5: 有什么可以进一步探索的点？

ReaLM-Retrieve虽然在步级不确定性检测和自适应检索方面取得了显著进展，但仍存在若干可深入探索的方向。首先，当前的不确定性检测器依赖于统计启发式方法，未来可引入基于小型语言模型或轻量级分类器的动态评估，以更精确地识别推理中的知识缺口。其次，论文仅在2-4跳推理任务上验证，对于更长链条（如5跳以上）或开放域复杂推理，自适应策略的鲁棒性尚需测试，可能需要结合记忆机制或分层检索。此外，检索时机学习仅基于答案准确率，未考虑推理效率与解释多样性，可通过多目标优化（如兼顾延迟、召回率和逻辑一致性）来改进。最后，当前框架对检索器高度依赖，未来可探索混合源（如知识图谱、代码执行器）与推理模型的协同，并研究如何让模型在检索后动态修正中间推理路径，而非简单拼接证据。这些方向有望进一步提升自适应检索在深度推理中的实用性与泛化能力。

### Q6: 总结一下论文的主要内容

大型推理模型（如DeepSeek-R1）在长链推理中常遇知识缺口，而现有RAG系统仅在推理前检索，与多步推理过程不匹配。论文提出ReaLM-Retrieve框架，通过三项创新解决该问题：1）步级不确定性检测器（RSUS），在推理步骤粒度识别知识缺口；2）学习式检索干预策略，决定何时检索并优化查询与整合；3）效率优化机制，通过隐式压缩和投机缓存将单次检索开销降低3.2倍。在MuSiQue、HotpotQA和2WikiMultiHopQA三个多跳QA基准上，该方法平均F1提升10.1%（相对标准RAG），并比固定间隔策略（如IRCoT）减少47%的检索调用。例如在MuSiQue上以平均1.8次检索达到71.2% F1，建立了推理-检索效率与准确率的新帕累托前沿，证明更少但时机更精准的检索优于频繁检索。
