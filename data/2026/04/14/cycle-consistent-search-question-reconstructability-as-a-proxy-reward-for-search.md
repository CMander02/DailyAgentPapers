---
title: "Cycle-Consistent Search: Question Reconstructability as a Proxy Reward for Search Agent Training"
authors:
  - "Sohyun An"
  - "Shuibenyang Yuan"
  - "Hayeon Lee"
  - "Cho-Jui Hsieh"
  - "Alexander Min"
date: "2026-04-14"
arxiv_id: "2604.12967"
arxiv_url: "https://arxiv.org/abs/2604.12967"
pdf_url: "https://arxiv.org/pdf/2604.12967v1"
categories:
  - "cs.AI"
tags:
  - "Search Agent"
  - "Reinforcement Learning"
  - "Unsupervised Training"
  - "Reward Modeling"
  - "Information Retrieval"
  - "Question Answering"
relevance_score: 7.5
---

# Cycle-Consistent Search: Question Reconstructability as a Proxy Reward for Search Agent Training

## 原始摘要

Reinforcement Learning (RL) has shown strong potential for optimizing search agents in complex information retrieval tasks. However, existing approaches predominantly rely on gold supervision, such as ground-truth answers, which is difficult to scale. To address this limitation, we propose Cycle-Consistent Search (CCS), a gold-supervision-free framework for training search agents, inspired by cycle-consistency techniques from unsupervised machine translation and image-to-image translation. Our key hypothesis is that an optimal search trajectory, unlike insufficient or irrelevant ones, serves as a lossless encoding of the question's intent. Consequently, a high-quality trajectory should preserve the information required to accurately reconstruct the original question, thereby inducing a reward signal for policy optimization. However, naive cycle-consistency objectives are vulnerable to information leakage, as reconstruction may rely on superficial lexical cues rather than the underlying search process. To reduce this effect, we apply information bottlenecks, including exclusion of the final response and named entity recognition (NER) masking of search queries. These constraints force reconstruction to rely on retrieved observations together with the structural scaffold, ensuring that the resulting reward signal reflects informational adequacy rather than linguistic redundancy. Experiments on question-answering benchmarks show that CCS achieves performance comparable to supervised baselines while outperforming prior methods that do not rely on gold supervision. These results suggest that CCS provides a scalable training paradigm for training search agents in settings where gold supervision is unavailable.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决训练搜索智能体（search agents）时对“黄金监督”（gold supervision，如标准答案）的依赖问题。随着大语言模型的发展，搜索智能体能够通过迭代规划和工具使用在复杂信息环境中导航，强化学习已成为优化此类顺序决策过程的标准框架。然而，现有基于强化学习的搜索智能体通常依赖黄金监督来定义奖励信号，这在专业或快速演变的领域中构成了可扩展性瓶颈：获取此类监督往往成本高昂或难以实现，导致难以构建可靠的奖励来评估搜索轨迹。

现有方法的不足在于它们无法摆脱对昂贵人工标注（如标准答案）的依赖，限制了在缺乏监督数据场景下的应用。为此，本文提出了一种无需黄金监督的框架——循环一致搜索（Cycle-Consistent Search, CCS），其核心思想是利用搜索过程本身的结构来生成代理奖励。该方法的核心问题是：如何在不依赖外部黄金监督的情况下，有效评估和优化搜索轨迹的质量？论文假设高质量的搜索轨迹应能无损编码问题的意图，从而能够从中准确重建原始问题；反之，不充分或无关的轨迹则无法做到这一点。因此，重建质量可作为轨迹质量的代理奖励。

然而，直接应用循环一致性目标会面临信息泄漏的挑战：重建可能依赖于浅层的词汇线索（如查询与问题间的词汇重叠），而非真正的搜索过程质量。为了减少这种影响，论文引入了信息瓶颈技术，包括从轨迹中排除最终响应以及对搜索查询进行命名实体识别掩码，迫使重建过程依赖于检索到的观察结果和结构支架，从而确保奖励信号反映的是信息充分性而非语言冗余。通过这种方式，CCS 旨在为缺乏黄金监督的环境提供一种可扩展的搜索智能体训练范式。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、监督范式类和原理类。

**方法类：从多步检索到交互式搜索智能体**。早期研究集中于单次检索-阅读流程，随后发展为基于LLM的多步检索方法，如ReAct和IRCoT，它们通过迭代检索和推理处理复杂查询。这催生了交互式搜索智能体的研究，如Search-o1，通过提示工程进行迭代查询。近期工作进一步利用强化学习（RL）将搜索建模为序列决策过程，以优化端到端搜索行为。本文延续了这一范式，将搜索视为由智能体驱动的交互过程。

**监督范式类：超越黄金监督的搜索智能体训练**。许多RL搜索智能体依赖黄金监督（如标准答案）构建奖励信号，这限制了可扩展性。为减少标注依赖，近期研究探索了替代监督信号，例如：RLIF利用模型内部置信度作为奖励；基于规则的LLM评判员（Constitutional Judges）根据预设准则评分；TTRL等方法利用多个采样轨迹间的一致性作为代理信号。本文提出的CCS框架与这些工作目标一致，旨在摆脱黄金监督，但区别在于：CCS的奖励信号直接与搜索的核心目标——获取充分必要的外部证据——对齐，而非依赖模型置信度或外部评判规则。

**原理类：将循环一致性扩展到搜索轨迹**。循环一致性作为学习原则，在无监督机器翻译和图像转换等领域被广泛用于保持关键信息。相关重建目标也在检索增强预训练中有所探索。本文的创新在于将循环一致性应用于智能体搜索轨迹，将轨迹视为对源问题的信息保持编码。与先前应用的关键区别在于，本文通过引入信息瓶颈（如屏蔽最终响应和命名实体），解决了搜索场景中因词汇重叠导致的信息泄漏问题，确保重建质量真实反映搜索过程的信息充分性，而非表面冗余。

### Q3: 论文如何解决这个问题？

论文提出的Cycle-Consistent Search (CCS)框架通过一种无黄金监督的循环一致性方法，将搜索轨迹的质量与原始问题的可重构性关联起来，以此作为代理奖励来训练搜索智能体。其核心思想是：一个最优的搜索轨迹应能无损编码问题的语义意图，从而仅从轨迹本身就能高保真地重建出原始问题。

整体框架基于部分可观测马尔可夫决策过程（POMDP）建模搜索过程。智能体策略根据当前问题和历史生成搜索查询（动作）并接收搜索结果（观察），最终生成回答。CCS的关键创新在于构建了一个“问题→轨迹→重建问题”的循环，并利用重建质量作为轨迹的奖励信号。为避免智能体通过简单的词汇复制（例如在查询中重复问题词句）来“欺骗”重建器，从而绕过真正的搜索过程，论文引入了信息瓶颈约束。

主要模块与关键技术包括：
1.  **瓶颈变换函数ψ**：它对原始轨迹τ进行加工，生成用于重建的加工轨迹\(\tilde{\tau}\)。该函数由两个操作复合而成：
    *   **最终回答排除（\(\psi_{trace}\)）**：从轨迹中移除最终生成的回答\(a_T\)，仅保留搜索过程中的查询和观察序列。这防止了重建器利用最终回答中可能存在的对问题的复述来走捷径。
    *   **搜索查询的实体掩码（\(\psi_{mask}\)）**：使用命名实体识别（NER）技术识别每个搜索查询\(a_t\)中的实体（如人名、地点），并将其替换为通用类型标签（如[LOC]）。这大幅削弱了从查询到问题的直接词汇线索，迫使重建过程必须主要依赖观察\(o_t\)（即搜索结果）中的证据来推断被掩码的内容。

2.  **预训练重建器\(P_\phi\)**：这是一个固定的模型，负责从加工后的轨迹\(\tilde{\tau}\)重建原始问题\(q\)，其输出的重建问题\(\hat{q}\)与原始问题的语义相似度即构成奖励。

3.  **基于GRPO的策略优化**：使用强化学习优化智能体策略。对于每个问题，策略采样一组轨迹，计算每个轨迹经过瓶颈变换和重建后得到的奖励（即\(q\)与\(\hat{q}\)的语义相似度）。采用组相对策略优化（GRPO），通过组内奖励归一化计算相对优势，并以此更新策略，鼓励产生能获得更高重建保真度的搜索行为。

该方法的创新点在于，将无监督领域（如机器翻译）中成熟的循环一致性思想创造性地迁移到搜索智能体训练中，并设计了针对性的信息瓶颈（排除最终回答和实体掩码）来确保奖励信号真正反映搜索过程的信息充分性，而非语言冗余，从而实现了无需黄金监督的高效训练。

### Q4: 论文做了哪些实验？

论文在多个知识密集型问答任务上进行了实验评估。实验设置方面，研究使用了Qwen系列模型（Qwen2.5-7B-Instruct、Qwen3-4B-Instruct-2507和Qwen3-32B）作为策略模型，并采用Gemini 2.5 Flash作为评估模型以确保答案准确性评估的一致性。训练语料混合了NQ和HotpotQA的训练集，使用相同的搜索引擎接口，训练300步，全局批大小为512。

数据集/基准测试分为通用问答和多跳问答两类。通用问答包括Natural Questions (NQ)、TriviaQA和PopQA；多跳问答包括HotpotQA、2WikiMQA、MuSiQue和Bamboogle。其中NQ和HotpotQA作为领域内数据集，其余为领域外数据集。

对比方法涵盖三类：1) 仅模型推理方法：直接推理、零样本思维链、交错检索思维链、检索增强生成和Search-o1；2) 使用黄金监督的方法：监督微调和基于答案准确率使用强化学习的Search-R1；3) 无黄金监督的方法：RLIF、Constitutional Judge和TTRL。

主要结果显示，CCS在所有无黄金监督方法中取得了最佳平均性能。在Qwen2.5-7B-Instruct、Qwen3-4B-Instruct-2507和Qwen3-32B上，CCS相比最强的无黄金监督基线分别提升了4.5%、9.8%和6.1%。关键数据指标上，CCS在Qwen2.5-7B-Instruct上的平均准确率为0.606，在Qwen3-4B-Instruct-2507上为0.636，在Qwen3-32B上为0.662。值得注意的是，CCS与使用黄金监督的方法表现相当，在部分模型上甚至超越了Search-R1。消融实验进一步验证了信息瓶颈（如屏蔽最终响应和命名实体）对提升奖励信号质量的重要性。

### Q5: 有什么可以进一步探索的点？

该论文提出的CCS框架虽在无监督训练搜索智能体上取得了进展，但仍存在一些局限性和可探索的方向。首先，其核心假设——最优搜索轨迹能无损编码问题意图——在复杂、模糊或高度依赖上下文的问题上可能不成立，未来可研究更鲁棒的意图表示方法。其次，信息瓶颈的设计（如屏蔽最终响应和命名实体）虽能减少词汇捷径，但可能过度过滤有用信息，未来可探索自适应或更精细的瓶颈机制（例如基于语义相似度的动态掩码）。此外，实验主要基于特定基准（如ResearchRubrics），在更动态、多模态或实时交互的搜索环境（如网页导航或API调用）中的泛化能力有待验证。结合个人见解，可能的改进包括：引入多模态重建目标（如图像或表格的重建），以处理跨模态搜索任务；将CCS与少量黄金监督或人类反馈结合，形成半监督混合奖励；以及探索重建过程的因果解释性，使奖励信号更透明可控。这些方向有望进一步提升搜索智能体在开放域和复杂任务中的可扩展性与性能。

### Q6: 总结一下论文的主要内容

本文提出了一种无需黄金监督的搜索智能体训练框架——循环一致搜索（CCS）。其核心问题是，在复杂信息检索任务中，现有强化学习方法严重依赖难以大规模获取的黄金监督信号（如标准答案）。为解决此问题，CCS借鉴无监督机器翻译和图像转换中的循环一致性思想，将搜索轨迹视为对问题意图的编码，并假设高质量的搜索轨迹应能无损地重建原始问题，从而将重建质量转化为策略优化的奖励信号。然而，简单的循环一致性目标易受信息泄漏影响，例如模型可能仅依赖浅层词汇线索而非搜索过程进行重建。为此，CCS引入了信息瓶颈技术，包括排除最终答案响应以及对搜索查询进行命名实体识别掩码，迫使重建过程依赖于检索到的观察结果和结构骨架，确保奖励信号反映信息充分性而非语言冗余。实验表明，在多个问答基准测试中，CCS的性能与有监督基线方法相当，并优于其他无需黄金监督的方法。这证明了循环一致性为缺乏黄金监督的场景提供了一种可扩展且有效的搜索智能体训练范式。
