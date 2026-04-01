---
title: "MemRerank: Preference Memory for Personalized Product Reranking"
authors:
  - "Zhiyuan Peng"
  - "Xuyang Wu"
  - "Huaixiao Tou"
  - "Yi Fang"
  - "Yi Gong"
date: "2026-03-31"
arxiv_id: "2603.29247"
arxiv_url: "https://arxiv.org/abs/2603.29247"
pdf_url: "https://arxiv.org/pdf/2603.29247v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent Personalization"
  - "Memory"
  - "Product Reranking"
  - "Reinforcement Learning"
  - "E-commerce Agent"
  - "Benchmark"
relevance_score: 7.5
---

# MemRerank: Preference Memory for Personalized Product Reranking

## 原始摘要

LLM-based shopping agents increasingly rely on long purchase histories and multi-turn interactions for personalization, yet naively appending raw history to prompts is often ineffective due to noise, length, and relevance mismatch. We propose MemRerank, a preference memory framework that distills user purchase history into concise, query-independent signals for personalized product reranking. To study this problem, we build an end-to-end benchmark and evaluation framework centered on an LLM-based \textbf{1-in-5} selection task, which measures both memory quality and downstream reranking utility. We further train the memory extractor with reinforcement learning (RL), using downstream reranking performance as supervision. Experiments with two LLM-based rerankers show that MemRerank consistently outperforms no-memory, raw-history, and off-the-shelf memory baselines, yielding up to \textbf{+10.61} absolute points in 1-in-5 accuracy. These results suggest that explicit preference memory is a practical and effective building block for personalization in agentic e-commerce systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的购物智能体在个性化商品重排序任务中，如何有效利用用户历史购买记录的问题。研究背景是，随着LLM从被动文本生成器演变为具备规划、记忆和工具调用能力的智能体，推荐系统正朝着“智能体化”方向发展。这类系统依赖分层记忆（如工作记忆、情景记忆和语义记忆）来支持个性化交互。然而，现有方法通常简单地将原始购买历史或多轮对话记录直接附加到LLM提示中，这种做法存在明显不足：原始历史记录包含大量噪声、长度过长容易超出上下文窗口限制，并且其内容与当前查询的相关性不匹配，导致个性化效果有限甚至性能下降。

本文要解决的核心问题是：如何从冗长、嘈杂的原始用户历史中，提炼出简洁、结构化且与查询独立的用户偏好记忆信号，以有效提升下游个性化商品重排序的性能。为此，论文提出了MemRerank框架，该框架将用户购买历史蒸馏为结构化的购物偏好记忆，特别是捕捉品类内和跨品类的行为模式，并采用强化学习方式训练记忆提取器，直接以重排序性能作为监督信号进行优化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：基于LLM的排序方法（方法类）和基于LLM的智能体记忆机制（架构/应用类）。

在**基于LLM的排序方法**方面，相关工作主要分为三类：逐点式（Pointwise）、成对/集合式（Pairwise/Setwise）以及列表式（Listwise）。这些方法或为每个查询-文档对打分，或比较文档间优劣，或直接生成完整排序列表。本文并未改变排序器本身，而是选择了一种集合式排序器作为高效的基础，其核心创新在于**通过改进排序器的输入（即偏好记忆）来提升性能**，而非设计新的排序算法。

在**智能体记忆机制**方面，相关研究旨在为LLM提供长期记忆以支持复杂推理。例如，Mem0作为一个通用记忆层动态管理用户信息；MemAgent通过强化学习选择性更新固定长度记忆；MR.Rec等推荐框架则训练LLM优化记忆利用和推荐推理。这些系统多侧重于维持对话连贯性或支持通用推理任务。**本文与这些工作的主要区别在于其特定性**：MemRerank并非通用记忆框架，而是专门为**下游产品重排序任务量身定制**的偏好记忆系统。它从原始购买历史中提炼出简洁、独立于查询的信号，并直接使用下游重排序性能作为监督信号，通过强化学习来训练记忆提取器，从而更直接、高效地服务于个性化电商推荐这一具体应用目标。

### Q3: 论文如何解决这个问题？

论文通过提出MemRerank框架来解决个性化产品重排序问题，其核心是构建一个偏好记忆系统，将冗长且嘈杂的用户购买历史提炼为简洁、独立于查询的偏好信号，以提升重排序效果。

整体框架分为两个阶段：偏好记忆提取和下游重排序。在记忆提取阶段，记忆提取器（如大语言模型）接收用户的购买历史（包括同类别和跨类别历史），生成结构化的文本摘要作为偏好记忆，并封装在预定义标签中。这一步骤的关键创新在于将原始历史压缩为可重用的稳定偏好表示，避免了直接将原始历史附加到提示中导致的噪声和长度问题。

在下游重排序阶段，提取的记忆与用户查询和候选产品集一起插入到重排序提示中，由重排序器执行“5选1”任务，即从五个候选产品中选择最相关的一个。这一任务被设计为集合重排序的基本操作，可扩展至更大候选池。

关键技术包括使用强化学习训练记忆提取器。论文采用GRPO方法，将记忆生成视为策略优化问题。奖励函数由两部分组成：格式奖励确保输出符合结构要求（如正确标签）；重排序奖励则基于下游“5选1”任务的准确性，即重排序器选择正样本产品时给予正奖励。通过采样多个响应并平均准确率，使奖励平滑，从而直接优化记忆对重排序任务的实际效用。

创新点主要体现在：1）提出显式的偏好记忆框架，将历史行为蒸馏为可复用的个性化信号；2）通过强化学习以端到端方式训练记忆提取器，无需昂贵的标注数据；3）构建了基于“5选1”任务的基准和评估框架，同时衡量记忆质量和下游重排序效果。实验表明，该方法在多个基线方法中取得显著提升，验证了偏好记忆在个性化电商系统中的实用性和有效性。

### Q4: 论文做了哪些实验？

论文在“电子产品”类别数据上构建了一个端到端的基准测试和评估框架，核心任务是基于LLM的“5选1”选择任务，以评估记忆质量和下游重排序效用。实验设置方面，作者使用GPT-4.1-mini和o4-mini作为重排序器，并比较了多种基线方法：无记忆、基于原始产品上下文的基线（如同类别产品、跨类别产品）、基于现成LLM提取的记忆基线（如使用未训练的Qwen2.5-7B-Instruct基础提取器、GPT-5.2提取的记忆），以及外部记忆基线（MR.Rec和Mem0）。主要对比方法是提出的MemRerank，即使用经过强化学习训练的Qwen2.5-7B-Instruct作为记忆提取器，并评估了结合显式推理标签的变体。

主要结果显示，MemRerank在所有设置中均取得最佳性能。关键数据指标为“5选1”准确率：对于GPT-4.1-mini重排序器，无记忆基线准确率为32.47%，而MemRerank提升至38.14%（绝对增益+5.67），结合推理标签后达到39.07%（+6.60）。对于o4-mini重排序器，无记忆基线为31.86%，MemRerank提升至40.72%（+8.86），结合推理标签后达到42.47%（+10.61），这是论文报告的最高增益。其他基线方法表现相对较弱，例如原始产品上下文方法增益有限（最高+2.99），现成LLM提取的记忆方法效果不一（GPT-5.2记忆在GPT-4.1-mini上仅+1.45），而外部记忆基线（MR.Rec和Mem0）在GPT-4.1-mini上甚至出现性能下降。实验还分析了记忆提取提示设计的影响，发现半结构化、基于证据的提示（v3）结合RL训练能带来最大性能提升，并探讨了原始购买历史长度对重排序的影响，表明单纯增加历史数据可能引入噪声，而MemRerank通过提取浓缩的记忆信号有效解决了这一问题。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在两方面：一是实验仅聚焦于电子产品类别，且仅使用产品元数据进行偏好提取，未能验证方法在其他商品领域（如服装、食品）或融入更丰富信号（如用户评论、点击流）时的泛化能力；二是研究局限于离线“五选一”的重排序任务，未探索更大规模（如Top 100商品）的检索场景，也未考虑在线交互中的动态偏好更新问题。

未来研究方向可包括：1）跨领域与多模态扩展，探索如何融合图像、文本描述等多源数据构建更鲁棒的偏好记忆；2）规模化与效率优化，设计轻量级记忆模块以支持实时大规模商品检索；3）动态记忆机制，引入增量学习或强化学习使记忆能随用户交互实时演化；4）可解释性增强，通过可视化或自然语言解释提升用户对推荐理由的信任度。此外，结合因果推断区分偶然购买与长期偏好，或利用课程学习逐步提炼用户兴趣层次，也是值得探索的改进思路。

### Q6: 总结一下论文的主要内容

该论文提出了MemRerank框架，旨在解决基于LLM的购物智能体在个性化产品重排序中面临的历史数据噪声、长度和相关性不匹配问题。其核心贡献在于设计了一种偏好记忆机制，能够从用户原始购买历史中提炼出简洁、独立于查询的偏好信号，以提升个性化重排序效果。

方法上，作者构建了一个端到端的基准评估框架，围绕LLM执行“5选1”任务来评估记忆质量和下游重排序效用。通过强化学习训练记忆提取器，并以下游重排序性能作为监督信号，优化记忆提取过程。

实验结果表明，MemRerank在两种基于LLM的重排序器上均显著优于无记忆、原始历史及现有记忆基线方法，在5选1准确率上最高提升10.61个百分点。研究证实，显式的购物偏好记忆能够有效将历史行为转化为可操作的个性化信号，为电商搜索系统的智能体个性化提供了实用且高效的构建模块。
