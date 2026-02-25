---
title: "From Logs to Language: Learning Optimal Verbalization for LLM-Based Recommendation in Production"
authors:
  - "Yucheng Shi"
  - "Ying Li"
  - "Yu Wang"
  - "Yesu Feng"
  - "Arjun Rao"
  - "Rein Houthooft"
  - "Shradha Sehgal"
  - "Jin Wang"
  - "Hao Zhen"
  - "Ninghao Liu"
  - "Linas Baltrunas"
date: "2026-02-24"
arxiv_id: "2602.20558"
arxiv_url: "https://arxiv.org/abs/2602.20558"
pdf_url: "https://arxiv.org/pdf/2602.20558v1"
categories:
  - "cs.AI"
  - "cs.IR"
tags:
  - "LLM应用"
  - "推荐系统"
  - "强化学习"
  - "上下文构建"
  - "数据合成"
  - "Agent架构"
relevance_score: 7.5
---

# From Logs to Language: Learning Optimal Verbalization for LLM-Based Recommendation in Production

## 原始摘要

Large language models (LLMs) are promising backbones for generative recommender systems, yet a key challenge remains underexplored: verbalization, i.e., converting structured user interaction logs into effective natural language inputs. Existing methods rely on rigid templates that simply concatenate fields, yielding suboptimal representations for recommendation. We propose a data-centric framework that learns verbalization for LLM-based recommendation. Using reinforcement learning, a verbalization agent transforms raw interaction histories into optimized textual contexts, with recommendation accuracy as the training signal. This agent learns to filter noise, incorporate relevant metadata, and reorganize information to improve downstream predictions. Experiments on a large-scale industrial streaming dataset show that learned verbalization delivers up to 93% relative improvement in discovery item recommendation accuracy over template-based baselines. Further analysis reveals emergent strategies such as user interest summarization, noise removal, and syntax normalization, offering insights into effective context construction for LLM-based recommender systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）应用于生成式推荐系统时的一个核心挑战：如何将结构化的用户交互日志有效地转化为自然语言输入，即“言语化”问题。研究背景是，尽管LLM在推荐系统中展现出巨大潜力，从作为特征提取器到端到端推理引擎均有应用，但现有方法大多依赖基于模板的言语化方式，即机械地拼接交互日志中的各个字段（如时间戳、设备、项目ID等）。这种方法的不足在于，它假设LLM能有效解析和推理这种原始表示，但实际上这存在根本性的错配。具体来说，直接将异构、细粒度的原始日志输入LLM会带来几个问题：一是解析这些非结构化信息会消耗模型的计算容量；二是日志中并非所有交互都具有同等重要的预测信号，噪声会影响效果；三是缺乏项目语义上下文（如元数据），迫使LLM仅从行为模式进行推理，这尤其损害了对冷启动项目的推荐质量。

因此，本文要解决的核心问题是：能否为基于LLM的推荐系统“学习”一种最优的言语化方法，而不是将其视为固定的预处理步骤？为此，论文提出了一种数据中心的框架，将推荐流程解耦为两个可学习的专门组件：一个“言语化器”负责将原始交互序列转化为优化的自然语言描述（学习过滤噪声、添加相关元数据并重组信息），一个“推理器”则根据言语化后的上下文进行偏好预测。其关键创新在于，利用推荐准确性作为训练信号，通过强化学习（具体采用组相对策略优化，GRPO）来优化言语化器，从而学习如何构建最能提升下游推荐性能的文本上下文。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及三大类别：LLM用于推荐、提示优化，以及强化学习在LLM中的应用。

在**LLM用于推荐**方面，现有研究主要探索了多种范式：一是利用LLM生成文本特征或嵌入来增强传统推荐模型；二是通过上下文学习，直接将LLM作为推荐器，将用户历史和候选项目格式化为提示；例如P5提出了一个统一的文本到文本框架，将各种推荐任务表述为自然语言生成。此外，还有研究探索参数高效微调方法或结合LLM推理与传统协同信号的混合方法。本文工作属于生成式推荐范畴，但关键区别在于：不同于将提示构建视为固定的工程选择，本文通过端到端学习来优化**表述化**函数。

在**提示优化**方面，已有广泛研究，包括离散提示搜索、连续提示调优以及基于强化学习的方法，近期还有基于梯度的优化和LLM驱动的提示优化。这些研究启发了本文：既然提示可以为任务性能而优化，那么作为基于LLM的推荐器核心输入的用户交互数据表述化也应可优化。然而，现有方法侧重于具有固定输入-输出映射的任务级优化，而推荐需要依赖用户的实例级表述化。本文工作将提示优化扩展到学习直接最大化推荐准确率的实例特定表述化。

在**强化学习用于LLM**方面，本文的训练方法基于RL-based LLM对齐的最新进展。虽然近端策略优化（PPO）被广泛采用，但其需要学习价值函数会带来计算开销。组相对策略优化（GRPO）通过组级奖励统计估计优势，提供了高效替代方案，本文将其适配用于表述化和推理优化。

### Q3: 论文如何解决这个问题？

论文通过一个数据中心的强化学习框架来解决基于LLM的推荐系统中“如何将结构化用户交互日志最优地转化为自然语言输入（即verbalization）”这一核心问题。其核心方法是训练一个独立的“Verbalizer”智能体，学习将原始交互历史转化为优化的文本上下文，以提升下游“Reasoner”推荐模型的准确性。

整体框架包含两个主要组件：Verbalizer（表达器）和Reasoner（推理器），采用两阶段训练流程。Verbalizer是一个生成式语言模型，负责将原始交互历史（如物品ID、时间戳等）转化为文本。论文探索了两种架构变体：1）基于动作的变体，为每条交互输出离散的“保留/丢弃”和“是否添加元数据”决策；2）基于重写的变体，直接生成对交互历史的完整文本重述。实验表明，重写方法性能显著更优，因为它能涌现出聚合重复模式（如“观看了X剧的5集”）和生成用户兴趣摘要（如“表现出对黑暗惊悚片的强烈偏好”）等高级策略，因此被选为主要方法。

训练的关键挑战在于没有“最优表达”的标注数据。为此，论文将其构建为强化学习问题。核心创新点在于使用一个强大的闭源LLM作为“先知Reasoner”来提供奖励信号：Verbalizer生成一组不同的文本表达，由先知Reasoner基于这些表达做出推荐预测，仅当预测命中真实目标物品时，对应的表达才获得奖励。这种方法利用了更强模型的判别能力来引导Verbalizer学习，避免了同时训练两个组件的不稳定性，并有助于学习到能捕捉真实偏好信号、而非利用弱模型缺陷的表达策略。

训练采用分组相对策略优化（GRPO）。奖励结合了准确性奖励和长度奖励，后者通过一个平台函数鼓励将历史压缩至目标比例范围，防止信息丢失或表达冗长。在Verbalizer训练收敛后，将其冻结，再在由其产生的表达数据分布上训练最终的Reasoner模型，使其适应学习到的表达模式。通过这种数据中心的、以推荐准确性为最终训练信号的学习框架，系统能够自动发现并应用有效的表达策略，从而显著提升推荐性能。

### Q4: 论文做了哪些实验？

论文在实验设置上，使用了一个来自主流流媒体平台的工业级数据集，包含三个月的用户观看交互记录，每条记录有时间戳、项目ID、标题、交互类型和观看时长。实验任务为给定用户交互历史（最多100条近期记录）和10个候选项目，预测用户下一个实际交互的项目。核心评估指标是Discovery场景下的Recall@1，即对用户未观看过的新项目的召回率。

对比方法包括：1) 模板基线，直接拼接交互字段；2) 零样本方法，使用启发式提示让LLM进行言语化；3) 基于动作的方法，训练言语化代理执行过滤和丰富操作，但不进行完整重写。实验模型采用Qwen-3系列的8B和32B参数模型，主要结果基于8B模型。

主要结果显示，学习到的言语化策略带来了显著提升。与模板基线相比，零样本言语化已带来5.3%的相对提升；基于重写的言语化代理进一步提升至12.5%；最终的两阶段全流程（言语化代理+训练后的推理器）实现了92.9%的相对提升，表明言语化优化与推理器训练具有强协同效应。消融实验进一步验证了各组件贡献：仅训练推理器（使用原始模板输入）的改进为42.8%，与全流程相差50.1个百分点，凸显了学习言语化的独立价值。关键数据指标包括：Discovery Recall@1相对提升百分比（模板基线为0%，零样本+5.3%，动作基+10.7%，重写言语化+12.5%，全流程+92.9%）。分析还发现，言语化代理涌现出了用户兴趣总结、噪声去除和语法规范化等策略。

### Q5: 有什么可以进一步探索的点？

该论文的框架虽在工业流式推荐场景中验证有效，但仍存在若干局限和可拓展方向。首先，其强化学习训练依赖下游推荐准确率作为奖励信号，这可能导致学习过程不稳定且计算成本较高；未来可探索更高效的优化目标或结合离线策略学习。其次，框架主要针对历史交互日志的文本化，未深入整合多模态信息（如图像、视频内容），在商品推荐等场景中潜力未完全释放。此外，论文未系统讨论不同LLM基座对verbalization策略敏感性的影响，未来可研究如何使verbalization模块与特定LLM协同优化。从实际部署看，尽管提及了蒸馏与缓存，但动态用户兴趣漂移时verbalizer的稳定性仍需更多验证。最后，该框架可扩展至对话推荐、跨领域推荐等更复杂场景，探索如何让verbalizer主动生成引导性提示或适应用户实时反馈，将是富有前景的方向。

### Q6: 总结一下论文的主要内容

该论文针对基于大语言模型（LLM）的生成式推荐系统中一个关键但未被充分探索的挑战——**言语化**（verbalization），即如何将结构化的用户交互日志有效转化为自然语言输入。现有方法通常依赖简单拼接字段的固定模板，导致次优的表示。为此，作者提出了一个**以数据为中心的框架**，将言语化视为一个可学习的组件，而非固定的预处理步骤。

其核心方法是采用**强化学习**，训练一个言语化智能体，以推荐准确性作为训练信号，将原始交互历史转化为优化的文本上下文。该智能体学习过滤噪声、融入相关元数据并重组信息，以提升下游预测。方法上采用了两阶段基于GRPO的训练流程，将上下文言语化与偏好推理解耦，实现了对各组件的专门优化。

主要结论显示，在大规模工业流式数据集上的实验表明，学习到的言语化策略在发现性物品推荐准确率上，相比基于模板的基线获得了**高达93%的相对提升**。定性分析进一步揭示了该框架涌现出的策略，如语法规范化、噪声过滤和用户兴趣总结，这凸显了言语化是当前LLM推荐系统的关键瓶颈。论文的意义在于指出，随着推荐系统越来越多地采用LLM作为主干，传统的特征工程将让位于言语化工程，并最终走向完全可学习的言语化。
