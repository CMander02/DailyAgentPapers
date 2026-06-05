---
title: "QueryAgent-R1: Bridging Query Generation and Product Retrieval for E-Commerce Query Recommendation"
authors:
  - "Dike Sun"
  - "Zheng Zou"
  - "Jingtong Zang"
  - "Qi Sun"
  - "Huaipeng Zhaoand Tao Luo"
  - "Xiaoyi Zeng"
date: "2026-06-04"
arxiv_id: "2606.05671"
arxiv_url: "https://arxiv.org/abs/2606.05671"
pdf_url: "https://arxiv.org/pdf/2606.05671v1"
categories:
  - "cs.CL"
tags:
  - "E-Commerce Agent"
  - "Query Recommendation"
  - "Memory-Augmented Agent"
  - "Reinforcement Learning"
  - "Agentic Framework"
relevance_score: 8.0
---

# QueryAgent-R1: Bridging Query Generation and Product Retrieval for E-Commerce Query Recommendation

## 原始摘要

Query recommendation in e-commerce search aims to proactively suggest queries that match users' potential interests. However, existing methods mainly optimize query-level relevance, while neglecting whether the retrieved products align with users' downstream preferences. This mismatch often leads to high query click through rates (CTR) but low product conversion rates (CVR). To bridge this gap, we propose QueryAgent-R1, a memory-augmented agentic framework that improves end-to-end alignment via chain-of-retrieval optimization. Our QueryAgent-R1 grounds query generation in real inventory retrieval, allowing the agent to validate and refine queries based on retrieved products. We also design a consistency reward in the agentic reinforcement learning (RL) process to jointly optimize query relevance and downstream engagement. In addition, we construct a memory abstraction module for efficient user profiling. To support offline evaluation, we construct two datasets based on both proprietary industrial data and public datasets, on which QueryAgent-R1 consistently outperforms strong baselines. Moreover, on a large scale production platform, QueryAgent-R1 improves Query CTR by 2.9% and guided CVR by 3.1% in online A/B tests.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决电商搜索中查询推荐（Query Recommendation）存在的“生成-检索”断层问题。具体来说，现有方法（如基于库存匹配的ItemCF、Swing，或基于独立语义检索的DSSM、LLM模型）主要优化查询与用户兴趣之间的“查询级相关性”，即推荐出的查询看起来够吸引人、语义上匹配。然而，这些方法忽略了关键的下游环节：该查询实际检索出的商品是否真的符合用户的深层意图（如购买意愿）。这导致了一个常见矛盾：推荐的查询点击率（CTR）很高，但用户点击后对检索出的商品不感兴趣，转化率（CVR）很低。核心问题是，现有方法将查询生成与商品检索过程分离，导致推荐结果在端到端转化链路上效果不佳。为此，本文提出QueryAgent-R1框架，其核心思路是通过“检索链优化”（Chain-of-Retrieval Optimization）将查询生成与真实库存检索紧密结合，让智能体在生成查询后能根据实际检索到的商品进行验证和修正，并在强化学习（RL）中引入一致性奖励（Consistency Reward），同时优化查询相关性和下游用户参与度，从而弥合生成与检索之间的鸿沟。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两类。**方法类**包括：基于共现匹配和语义检索的工业方法（如传统的协同过滤和向量检索），以及从隐式日志生成查询的序列到序列模型（如Seq2Seq、Transformer-based生成模型）。本文指出这些方法主要优化查询级别的相关性（如Query CTR），但忽略了生成查询的检索结果与用户下游偏好（如产品转化率CVR）的一致性。**评测与应用类**包括：现有的查询推荐基准数据集（如电商搜索日志）和在线A/B测试方法。本文与这些工作的核心区别在于：QueryAgent-R1首次引入**检索链优化**框架，将查询生成与实际商品检索结果实时对齐，并通过**记忆增强模块**存储用户行为抽象，在强化学习中设计**一致性奖励**，同时优化查询相关性和下游产品转化。这使得模型在离线数据集（自建工业数据+公开数据集）和在线生产环境中均显著优于基线，如Query CTR提升2.9%、CVR提升3.1%。

### Q3: 论文如何解决这个问题？

QueryAgent-R1通过一个基于记忆增强的智能体框架（Agentic Framework）和检索链优化（Chain-of-Retrieval Optimization）来解决查询生成与产品检索之间不对齐的问题。整体架构分为两个核心沙箱：记忆环境（Memory Environment）和产品检索沙箱（Product Retrieval Sandbox）。首先，记忆环境使用Qwen3-Next-80B-A3B对用户三个月内的超长行为序列进行异步压缩，生成包含最新意图、兴趣图谱和潜在身份的紧凑用户画像，并通过Fetch_Memory动作直接检索缓存画像，实现约10倍的序列压缩，同时保持个性化信息的时效性。其次，产品检索沙箱基于400万真实商品构建，采用混合检索策略（BM25稀疏检索与Qwen3-Embedding-0.6B密集检索）结合Qwen3-Rerank-0.6B交叉编码器重排序，使智能体在生成查询后能立即调用检索工具检查返回的商品，并据此修正查询，确保生成的查询既能吸引点击又能检索到可购买的商品。核心创新点在于设计了一致性奖励函数，通过强化学习联合优化查询相关性和下游商品匹配。该奖励由格式奖励（r_fmt）、工具调用奖励（r_tool）和命中奖励（r_hit）线性组合而成，其中r_hit进一步分解为查询奖励（r_q）和商品奖励（r_i），并引入硬/软组件（如精确匹配、ROUGE分数和标题级ROUGE）缓解奖励稀疏问题。优化使用GDPO（组解耦策略优化），相比GRPO对密集和稀疏信号进行解耦归一化，更适配本奖励设计。整体框架在离线数据集和在线大规模生产环境中均取得显著提升，查询点击率提升2.9%，引导转化率提升3.1%。

### Q4: 论文做了哪些实验？

论文在工业数据集（5.4万训练/5千测试用户，含搜索/点击行为的用户行为日志）和Amazon公开数据集（1.6万训练/1千测试，合并ESCI与Review数据）上进行了实验。对比方法分为两类：基于库存的检索方法（Swing、Qwen3-Emb-0.6B/4B）和LLM直接推理方法（Qwen3.6-plus、Gemini-3.1-pro、GPT-5.1、DeepSeek-v4-flash等）。主要评估指标包括Q_EM（查询精确匹配）、I_Hit@1（商品检索命中）和Cons@1（两者同时成立）。

离线实验结果显示，QueryAgent-R1在工业数据集上显著领先：Q_EM=0.177、I_Hit@1=0.261、Cons@1=0.117，远超最强的库存检索基线Qwen3-Emb-4B（0.057/0.114/0.041）和最强LLM基线Gemini-3.1-pro（0.054/0.096/0.029）。在Amazon数据集上，虽然Gemini-3.1-pro Q_EM更高（0.123），但QueryAgent-R1在I_Hit@1（0.144）和Cons@1（0.063）上全面领先，Cons@1较Gemini-3.1-pro（0.021）提升3倍。消融实验表明，单独增加检索或RL仅带来有限提升，而完整模型通过协同奖励机制将工业数据集Cons@1从单轮RL的0.021提升至0.117。在持续7天的大规模在线A/B测试中，QueryAgent-R1部署于1%流量后，查询CTR提升2.9%，引导CVR提升3.1%，最终GMV增长4.9%。

### Q5: 有什么可以进一步探索的点？

1.  **推理效率仍是核心瓶颈**：Agent框架的响应延迟较长，当前采用异步部署虽能满足生产需求，但增加了系统复杂度。未来可探索**轻量化推理**，例如通过知识蒸馏将RL-trained agent压缩为端到端模型，或利用缓存机制复用用户记忆模块中的向量检索结果，从而降低在线推理成本。
2.  **奖励信号设计的局限性**：一致性奖励仅依赖当次检索结果，未建模用户长期兴趣演化。可引入**多轮强化学习**，将用户会话中的连续查询-商品反馈序列作为状态，设计动态奖励函数（如预估长期转化率），使Agent具备策略规划能力。
3.  **冷启动与多样性不足**：记忆模块依赖历史行为，对新用户或长尾查询场景覆盖有限。未来可结合图神经网络构建**跨用户意图迁移模型**，或利用大语言模型知识注入来增强低频查询的商品相关性建模，缓解数据稀疏问题。

### Q6: 总结一下论文的主要内容

该论文提出QueryAgent-R1，一种用于电商搜索查询推荐的记忆增强型智能体框架。现有方法主要优化查询层面的相关性，忽略检索产品是否匹配用户下游偏好，导致高点击率但低转化率。该方法通过链式检索优化实现端到端对齐：将查询生成锚定在真实商品检索中，使智能体根据检索结果验证和优化查询；在智能体强化学习中设计一致性奖励，联合优化查询相关性和下游用户参与；构建记忆抽象模块实现高效用户画像。在工业数据和公开数据集上，QueryAgent-R1均优于强基线。线上A/B测试中，查询点击率提升2.9%，引导转化率提升3.1%。该工作弥合了查询生成与商品检索的鸿沟，将推荐与下游商业价值对齐，对电商搜索实践具有显著意义。
