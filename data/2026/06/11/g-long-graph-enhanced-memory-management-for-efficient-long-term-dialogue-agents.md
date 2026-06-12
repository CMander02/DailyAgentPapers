---
title: "G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents"
authors:
  - "Minjun Choi"
  - "Yoonjin Jang"
  - "Sangwon Youn"
  - "Youngjoong Ko"
date: "2026-06-11"
arxiv_id: "2606.13115"
arxiv_url: "https://arxiv.org/abs/2606.13115"
pdf_url: "https://arxiv.org/pdf/2606.13115v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Long-term Dialogue Agent"
  - "Memory Management"
  - "Graph-Enhanced Memory"
  - "Small Language Model"
  - "Attention-Aware Importance Scoring"
  - "Retrieval-Augmented Generation"
  - "Open-Domain Dialogue"
relevance_score: 8.0
---

# G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents

## 原始摘要

While Large Language Models (LLMs) have advanced open-domain dialogue systems, maintaining long-term consistency remains a challenge due to inherent limitations in long-context reasoning and the inefficiency of processing extensive raw text. Existing approaches typically rely on either unstructured memory storage, which is prone to information loss, or computationally expensive LLMs that incur high latency. To address these limitations, we propose G-Long, a graph-enhanced framework that utilizes a fine-tuned small Language Model (sLM) for structured triplet extraction and associative retrieval, significantly reducing operational costs. Furthermore, we introduce the novel attention-aware importance scoring mechanism that leverages the intrinsic cross-attention signals of a T5 summarizer to identify salient memories. Extensive experiments across diverse benchmarks demonstrate that G-Long achieves state-of-the-art performance in both response generation and memory retrieval, yielding performance gains of up to 9.8% in response quality on MSC and 40.8% in retrieval recall on LME, while significantly minimizing computational overhead.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在长期对话系统中面临的长程一致性和效率挑战。研究背景是：虽然LLM提升了开放域对话系统的流畅性与上下文感知能力，但建立长期用户关系需要能够跨会话保持一致的人物特征和事件记忆。现有方法主要存在两点不足：1）基于非结构化文本（如段落摘要）的记忆存储容易丢失关键细节，例如将"深海钓鱼"泛化为"钓鱼"，导致实体关系模糊，标准稠密检索难以追踪精确事实；2）将冗长的非结构化摘要直接输入大型LLM进行记忆操作会消耗大量Token，带来高昂的计算开销和延迟。

为此，本文提出G-Long，一种基于图增强的高效长期对话记忆管理框架。核心创新包括：1）利用微调的小语言模型（sLM）进行结构化三元组抽取和关联检索，替代昂贵的大型LLM，将记忆维护成本降低4.9倍，Token消耗减少63%；2）设计基于注意力感知的重要性评分机制，利用T5摘要器的内在交叉注意力信号识别关键记忆，并采用结构化子图扩展进行多跳推理。实验表明，G-Long在MSC数据集上响应质量提升9.8%，在LME上检索召回率提升40.8%，实现了性能与效率的平衡。

### Q2: 有哪些相关研究？

在方法类相关工作中，现有研究主要分为两类。第一类如MemoryBank、FraCom和LD-Agent，通过人类遗忘机制、命题级分解或独立事件/人物模块来管理记忆，但它们过度依赖大型语言模型(LLM)进行记忆操作，导致可扩展性差，且非结构化表示限制了检索精度。第二类如GraphRAG、HippoRAG和LinearRAG，利用知识图谱结构化记忆，但主要面向静态文档语料库，无法适应对话中的人称代词、省略等动态演化特征。本文提出的G-Long与这些工作的关键区别在于：(1) 采用微调的小语言模型(sLM)进行结构化三元组提取和关联检索，避免了LLM的高昂计算成本；(2) 提出注意力感知重要性评分机制，通过T5摘要器的交叉注意力信号筛选关键记忆，克服了同类方法(如FraCom的命题级分解产生无信息片段、SGMem仍依赖LLM API)的局限性。在应用/评测类工作中，MSC、CC、LongMemEval、LoCoMo和CareCall等基准评估了长对话一致性，G-Long在这些基准上实现了SOTA性能，并在响应质量和检索召回率上分别提升了9.8%和40.8%。

### Q3: 论文如何解决这个问题？

G-Long通过一个图增强框架来解决长期对话中的记忆管理问题。整体架构包括四个核心组件：高效记忆构建、图记忆库、关联性记忆检索和响应生成。

首先，高效记忆构建通过两个模块实现。一是三元组提取模块，采用微调的小语言模型（sLM）将非结构化对话解析为(主语, 关系, 宾语)的结构化三元组，降低了计算成本。二是创新性的注意力感知重要性评分模块，利用T5摘要器的交叉注意力信号自动为每个三元组分配重要性分数，无需外部LLM开销。

其次，图记忆库采用双存储策略：实体节点使用MiniLM等预训练编码器生成稠密向量并存入向量数据库（如ChromaDB），支持语义模糊匹配；边被设计为属性丰富的容器，包含关系文本、重要性分数、创建和访问时间戳，实现了对语义、重要性和时效性的统一编码。

在关联性记忆检索阶段，采用从粗到精的流水线。先通过向量相似度识别锚点节点，再执行多跳子图扩展获取候选三元组。随后混合重排序过程首先基于语义相似度筛选，再结合重要性分数和指数衰减的时效性分数进行精排，最终选出Top-K个三元组。

响应生成时，将检索到的三元组序列化后与当前对话历史拼接，构成最终提示输入给LLM生成响应。这种方法在MSC数据集上实现了9.8%的响应质量提升，在LME数据集上实现了40.8%的检索召回率提升，同时显著降低了计算开销。

### Q4: 论文做了哪些实验？

论文在多个基准上进行了全面实验。**实验设置**方面，标准化的骨干模型为gpt-4o-mini，以隔离记忆机制的效果。**数据集/基准**包括：用于评估对话生成的多会话聊天（MSC）和对话编年史（CC）数据集，用于测试超长上下文可扩展性的LoCoMo数据集，以及用于直接评测检索性能的LongMemEval（LME）数据集。**对比方法**涉及两类基线：非结构化文本记忆（无历史、长上下文、MemoryBank、LD-Agent）和结构化图框架（FraCom、HippoRAG），仅HippoRAG因设计限制不参与生成评估。**主要结果**：在MSC上，G-Long的G-Eval平均分达4.846，优于MemoryBank的4.713和LD-Agent的4.673；BLEU-2比LD-Agent提升9.8%，ROUGE-L提升3.8%。在CC上，BLEU-2比LD-Agent提升8.9%，比MemoryBank提升24.6%。在LME检索中，G-Long的Recall@3达0.6286，Accuracy@3为0.5783，分别比最强基线LD-Agent提升40.8%和30.2%。消融实验显示，子图扩展深度L=1最优（Recall@3为0.6286），而L=2会导致性能下降（0.5314）。

### Q5: 有什么可以进一步探索的点？

首先，论文承认了将非结构化对话转为结构化三元组时，会损失微妙的情绪基调和文体风格等细粒度语义信息。未来可探索混合存储机制，将图节点链接到原始文本片段，在保持高效检索的同时保留丰富语境。其次，作为流水线框架，三元组提取模块的鲁棒性直接决定记忆质量，极端歧义或复杂共指仍可能引入噪声。可以引入自纠正机制，利用注意力重要性评分来验证图内事实一致性。此外，稀疏查询中的未解析指代（如指示代词）会导致检索断裂，而语义漂移问题（过度依赖字面关键词匹配）也反映出对全局对话意图的忽略。未来可设计动态上下文解析的混合方法，例如结合实体链接与指代消解技术，使图节点与对话上下文更紧密耦合，或利用时序感知的图注意力机制来缓解匹配偏移。

### Q6: 总结一下论文的主要内容

本文提出G-Long框架，旨在解决大语言模型在长期对话中的上下文推理局限和原始文本处理低效问题。核心贡献包括：利用微调小语言模型进行结构化三元组提取和关联检索，大幅降低计算成本；引入基于T5摘要器交叉注意力信号的重要性评分机制，实现关键记忆筛选。在MSC、CC、LoCoMo及LME基准测试中，G-Long在响应质量和检索召回率上均达到最优，分别提升9.8%和40.8%，且显著减少运算开销。该框架作为可扩展的即插即用方案，为资源受限环境下的长期对话代理提供了低成本的高效一致性维护方法。
