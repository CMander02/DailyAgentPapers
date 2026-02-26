---
title: "Offline Reasoning for Efficient Recommendation: LLM-Empowered Persona-Profiled Item Indexing"
authors:
  - "Deogyong Kim"
  - "Junseong Lee"
  - "Jeongeun Lee"
  - "Changhoe Kim"
  - "Junguel Lee"
  - "Jungseok Lee"
  - "Dongha Lee"
date: "2026-02-25"
arxiv_id: "2602.21756"
arxiv_url: "https://arxiv.org/abs/2602.21756"
pdf_url: "https://arxiv.org/pdf/2602.21756v1"
categories:
  - "cs.IR"
  - "cs.LG"
tags:
  - "LLM应用"
  - "推荐系统"
  - "离线推理"
  - "可解释性"
  - "系统架构"
  - "效率优化"
relevance_score: 7.5
---

# Offline Reasoning for Efficient Recommendation: LLM-Empowered Persona-Profiled Item Indexing

## 原始摘要

Recent advances in large language models (LLMs) offer new opportunities for recommender systems by capturing the nuanced semantics of user interests and item characteristics through rich semantic understanding and contextual reasoning. In particular, LLMs have been employed as rerankers that reorder candidate items based on inferred user-item relevance. However, these approaches often require expensive online inference-time reasoning, leading to high latency that hampers real-world deployment. In this work, we introduce Persona4Rec, a recommendation framework that performs offline reasoning to construct interpretable persona representations of items, enabling lightweight and scalable real-time inference. In the offline stage, Persona4Rec leverages LLMs to reason over item reviews, inferring diverse user motivations that explain why different types of users may engage with an item; these inferred motivations are materialized as persona representations, providing multiple, human-interpretable views of each item. Unlike conventional approaches that rely on a single item representation, Persona4Rec learns to align user profiles with the most plausible item-side persona through a dedicated encoder, effectively transforming user-item relevance into user-persona relevance. At the online stage, this persona-profiled item index allows fast relevance computation without invoking expensive LLM reasoning. Extensive experiments show that Persona4Rec achieves performance comparable to recent LLM-based rerankers while substantially reducing inference time. Moreover, qualitative analysis confirms that persona representations not only drive efficient scoring but also provide intuitive, review-grounded explanations. These results demonstrate that Persona4Rec offers a practical and interpretable solution for next-generation recommender systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的推荐系统在实时部署时面临的高延迟问题。研究背景是，LLM凭借其强大的语义理解和上下文推理能力，为推荐系统带来了新的机遇，能够通过处理评论等文本信息来捕捉用户兴趣和物品特征的细微差别。当前，一种主流方法是将LLM用作重排器，在线推理时根据推断的用户-物品相关性对候选物品进行重新排序。然而，现有方法（如基于提示或微调的LLM重排器）存在明显不足：它们严重依赖在线阶段的耗时推理步骤，包括动态构建用户画像、生成物品画像以及进行基于推理的重排。由于用户历史行为不断变化，系统需要反复执行这些计算，导致推理延迟很高，严重阻碍了在实际需要实时响应的推荐场景中的部署。

因此，本文要解决的核心问题是：如何保留LLM语义推理优势的同时，大幅降低推荐系统的在线推理延迟，实现高效且可扩展的实时推荐。为此，论文提出了Persona4Rec框架，其核心思路是将耗时的LLM推理从在线阶段转移到离线阶段。具体而言，在离线阶段，利用LLM对物品评论进行推理，提取出解释不同用户可能喜欢该物品的多样化动机，并将其物化为可解释的“用户角色”表示，从而为每个物品构建多视角的、基于评论的角色画像索引。在线阶段，系统则通过一个轻量级编码器，将用户历史行为聚合的画像与物品侧最相关的角色进行对齐，从而将用户-物品相关性计算转化为高效的用户-角色相似度评分，完全避免了在线调用LLM进行复杂推理。这种方法不仅追求效率，也通过角色表示提供了直观的、基于评论的解释性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于LLM的推荐重排序方法、用户画像建模方法以及基于评论的推荐方法。

在**基于LLM的推荐重排序方法**方面，早期工作（如zero-shot LLM reranker）和后续改进（如采用pairwise或setwise提示的RankVicuna、TALLRec）均利用LLM在线推理用户-物品相关性进行重排，虽精度高但延迟大。本文提出的Persona4Rec与这些方法的核心区别在于将耗时的推理过程移至离线阶段，在线仅需轻量级计算，从而实现了低延迟和高可扩展性。

在**用户画像建模方法**方面，传统方法依赖静态人口统计或手工特征（如UPCSim），近期研究则利用LLM从交互历史中生成或丰富用户画像（如RLMRec、KAR）。这些工作多侧重于用户侧建模，且推理常在线进行。本文的独特之处在于，它同时利用LLM在离线阶段为物品构建多视角、可解释的“人物角色”画像，并通过学习用户画像与最相关物品角色之间的对齐来实现推荐。

在**基于评论的推荐方法**方面，如EXP3RT利用评论作为偏好证据来提升评分预测和重排序。本文同样以评论作为离线推理的基础数据源，但其创新点在于从评论中推理出多样化的用户动机，形成结构化的人物角色表示，这不仅服务于高效推荐，也提供了基于评论的直观解释。

### Q3: 论文如何解决这个问题？

论文通过提出Persona4Rec框架，将原本在线推理阶段昂贵的大型语言模型（LLM）推理过程转移到离线阶段，从而解决了LLM作为重排序器时在线推理延迟高的问题。其核心方法是预先为每个物品构建基于评论的、可解释的“人物角色”（Persona）表示，并在在线阶段进行轻量化的快速匹配。

整体框架分为离线和在线两个阶段。在离线阶段，系统执行三个关键步骤来构建人物角色索引并训练编码器。首先，在“人物角色构建”模块中，利用LLM分析物品元数据（如标题、描述）生成客观的物品摘要，并从用户评论中提取主观的方面（如购买目的、质量标准），然后将两者结合，为每个物品生成多个（通常2-7个）结构化的人物角色。每个人物角色包含名称、描述和偏好理由，代表了喜欢该物品的一类用户的动机。其次，在“用户档案-人物角色匹配”模块中，对于每个历史交互（用户，物品），使用LLM作为评判者，从该物品的人物角色集合中选出最能解释该用户为何与之交互的最相关角色，从而生成用户-人物角色对齐信号数据集。最后，在“编码器训练”模块中，利用该对齐数据集，通过对比学习训练一个轻量化的编码器，将用户档案和人物角色文本映射到共享的嵌入空间，使对齐的（用户，角色）对具有更高的相似度。训练完成后，将所有物品的人物角色预先编码并构建成“人物角色画像物品索引”。

在线阶段，当用户发起请求时，系统根据其最近的交互历史（包含物品摘要和评论方面）快速编码得到用户嵌入向量。对于每个候选物品，通过计算用户嵌入与该物品所有预存人物角色嵌入之间的相似度，取最大值作为最终的相关性分数，并据此进行重排序。匹配度最高的人物角色同时提供了可解释的推荐理由。

该方法的创新点在于：1）**架构创新**：通过“离线推理、在线匹配”的两阶段设计，将计算密集的LLM推理与低延迟的在线服务解耦。2）**表示创新**：用一组多视角、可解释的人物角色替代传统的单一物品向量，能更细致地捕捉物品吸引不同用户群体的多元动机。3）**对齐机制创新**：利用LLM生成高质量的对齐监督信号来训练轻量化编码器，将复杂的用户-物品相关性评估转化为高效的向量空间相似度计算，从而在保持推荐性能的同时大幅降低推理延迟。

### Q4: 论文做了哪些实验？

本论文在Amazon Books和Yelp两个真实世界数据集上进行了广泛的实验，以评估所提出的Persona4Rec框架。实验设置遵循典型的多阶段排序流程：首先使用BPR-MF或LightGCN等协同过滤模型生成初始候选集，然后由重排序器进行精排。主要对比方法包括基于LLM的重排序器ZS-LLM和TALLRec，以及最新的SOTA方法Expert。此外，还包含了基于评论的归因生成方法XRec和Expert进行可解释性对比。

主要实验结果如下：在Top-K推荐性能上，Persona4Rec（包括vanilla预训练版本和fine-tuned微调版本）在HR、MRR、NDCG等关键指标上均表现优异。具体数据上，在Amazon数据集上，当使用LightGCN作为生成器时，Persona4Rec (fine-tuned) 在@10的指标达到HR 0.1151、MRR 0.0462、NDCG 0.0622，显著优于基线。在Yelp数据集上，使用BPR-MF时，其@10指标为HR 0.0599、MRR 0.0214、NDCG 0.0303。实验表明，Persona4Rec的性能与最新的基于LLM的重排序器相当，甚至更优。

此外，论文还设计了针对冷启动/热启动用户以及热门/长尾物品的鲁棒性测试。例如，在Amazon数据集上，对于使用BPR-MF生成器的冷启动用户，Persona4Rec在NDCG@10上相比基线有+4.2%的提升；对于长尾物品，HR@10有+16.1%的提升。这些结果验证了该方法在数据稀疏场景下的有效性。论文也通过模拟无评论物品的实验，证明了其框架在仅使用元数据摘要时仍能保持性能。效率测试表明，该方法通过离线推理，大幅降低了在线推理延迟。

### Q5: 有什么可以进一步探索的点？

该论文的核心创新在于将耗时的LLM推理过程移至离线阶段，通过构建物品的“角色画像”来提升在线推理效率。然而，这带来了几个值得深入探索的方向。

首先，**离线推理的静态性与用户兴趣的动态演化之间存在矛盾**。论文中基于历史评论生成的角色画像本质上是静态的，难以捕捉实时或短期的兴趣漂移。未来研究可以探索如何设计一种**混合机制**，在保持高效索引的基础上，融入轻量级的在线更新模块，例如利用小型模型或增量学习来微调角色权重，以适应用户行为的变化。

其次，**角色画像的生成质量和多样性依赖于离线阶段LLM提示工程与评论数据**。这可能导致画像存在偏见或覆盖不全。一个改进思路是引入**多源信息融合**，不仅基于评论，也结合知识图谱、社交关系等结构化信息来共同推导更全面、更公平的角色画像。同时，可以研究**自动化提示优化**或**可控生成技术**，以确保生成的角色既多样又具有区分度。

最后，**效率与效果的精妙权衡**。当前方法为追求效率，将复杂的用户-物品匹配简化为用户与固定角色集的匹配，这可能损失部分语义细微度。未来可以探索**层次化或可配置的推理架构**，例如，为高价值用户或关键场景保留有限的在线深度推理能力，而对大多数请求使用高效的索引匹配，从而实现更灵活的资源分配与效果优化。

### Q6: 总结一下论文的主要内容

该论文提出了Persona4Rec框架，旨在解决基于大语言模型（LLM）的推荐系统在线推理延迟高的问题。其核心贡献是将耗时的LLM语义推理从在线阶段转移到离线阶段，从而实现高效且可解释的实时推荐。

具体而言，框架首先在离线阶段利用LLM分析物品评论，推理出不同用户可能喜欢该物品的多样化动机，并将这些动机实例化为多个人格化表征，为每个物品提供多个可解释的视角。在线阶段，系统则使用一个专用编码器学习将用户画像与最相关的物品侧人格表征对齐，将用户-物品相关性计算转化为更高效的用户-人格相关性计算，无需调用LLM。

实验表明，该方法在保持与先进LLM重排序模型相当性能的同时，大幅降低了推理时间。此外，人格表征本身提供了基于评论的直观解释。该工作为构建高效、可扩展且可解释的下一代推荐系统提供了一种实用方案。
