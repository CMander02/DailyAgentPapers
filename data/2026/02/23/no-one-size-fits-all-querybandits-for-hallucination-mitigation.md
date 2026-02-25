---
title: "No One Size Fits All: QueryBandits for Hallucination Mitigation"
authors:
  - "Nicole Cho"
  - "William Watson"
  - "Alec Koppel"
  - "Sumitra Ganesh"
  - "Manuela Veloso"
date: "2026-02-23"
arxiv_id: "2602.20332"
arxiv_url: "https://arxiv.org/abs/2602.20332"
pdf_url: "https://arxiv.org/pdf/2602.20332v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent 评测/基准"
  - "Agent 安全"
  - "LLM 应用于 Agent 场景"
  - "幻觉缓解"
  - "查询优化"
  - "上下文赌博机"
  - "在线学习"
  - "模型不可知"
relevance_score: 7.5
---

# No One Size Fits All: QueryBandits for Hallucination Mitigation

## 原始摘要

Advanced reasoning capabilities in Large Language Models (LLMs) have led to more frequent hallucinations; yet most mitigation work focuses on open-source models for post-hoc detection and parameter editing. The dearth of studies focusing on hallucinations in closed-source models is especially concerning, as they constitute the vast majority of models in institutional deployments. We introduce QueryBandits, a model-agnostic contextual bandit framework that adaptively learns online to select the optimal query-rewrite strategy by leveraging an empirically validated and calibrated reward function. Across 16 QA scenarios, our top QueryBandit (Thompson Sampling) achieves an 87.5% win rate over a No-Rewrite baseline and outperforms zero-shot static policies (e.g., Paraphrase or Expand) by 42.6% and 60.3%, respectively. Moreover, all contextual bandits outperform vanilla bandits across all datasets, with higher feature variance coinciding with greater variance in arm selection. This substantiates our finding that there is no single rewrite policy optimal for all queries. We also discover that certain static policies incur higher cumulative regret than No-Rewrite, indicating that an inflexible query-rewriting policy can worsen hallucinations. Thus, learning an online policy over semantic features with QueryBandits can shift model behavior purely through forward-pass mechanisms, enabling its use with closed-source models and bypassing the need for retraining or gradient-based adaptation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）中普遍存在的“幻觉”（即生成与事实不符的内容）问题，尤其是在无法访问模型内部权重和参数的闭源模型场景下的缓解难题。

研究背景在于，随着LLM推理能力日益强大，其产生幻觉的频率和严重性也随之增加。然而，现有的主流缓解方法（如基于logits、token概率或内部表征编辑的技术）主要针对开源模型设计，严重忽视了在现实机构部署中占主导地位的闭源模型。此外，现有方法通常采用“一刀切”的静态查询改写策略（如固定地进行释义或扩展），缺乏根据具体查询的语义特征进行动态、自适应调整的能力，这可能导致某些情况下幻觉问题反而恶化。

因此，本文要解决的核心问题是：**如何为无法进行内部修改的闭源LLM，设计一种无需重新训练、仅通过前向传递即可在线自适应缓解幻觉的通用框架**。具体而言，论文提出了名为“QueryBandits”的上下文赌博机框架，其核心思想是：**不存在一种适用于所有查询的最优改写策略**。该框架将每次查询的17维语言学特征向量作为上下文，在线学习一个策略，为每个独特的查询动态选择最优的查询改写策略（如释义、简化、扩展等），以主动引导LLM生成更事实性的回答，从而在模型不可知的前提下，纯粹通过输入层的干预来优化模型行为。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：社会影响与模型类型、幻觉缓解方法，以及语言学特征的应用。

在社会影响与模型类型方面，现有研究指出LLM幻觉会侵蚀社会信任，并被视为一种新的认知失败模式。有分析认为，训练和评估过程鼓励模型猜测而非承认不确定性，导致了幻觉。尽管有报告指出先进推理模型（如o3, o4-mini）的幻觉率在增加，且其法律风险已被案例证实，但大多数缓解研究集中于开源模型，针对闭源模型的研究非常缺乏。本文正是瞄准了这一未被充分探索的空白。

在幻觉缓解方法上，相关研究已从事后检测和迭代纠正，扩展到预防性 grounding 和查询重构。例如，有工作通过查询扰动在生成前估计幻觉风险，或在RAG管道中采用“重写-检索-阅读”策略。手动、基于规则的重写也被广泛使用。然而，这些方法通常依赖于原始提示或静态启发式规则，而非根据原始查询的上下文信号进行引导式重写。本文提出的QueryBandits框架则是一种与模型无关的上下文赌博机方法，它在线自适应学习，以选择最优的查询重写策略，从而超越了这些静态或启发式方法。

在语言学特征的应用方面，已有研究表明预训练语言模型能够在少量样本设置下恢复语言属性。本文在此基础上，利用LLM为每个查询识别17个关键语言学特征，这些特征选自现有LLM文献和传统语言学，优先考虑已知会影响人类和模型理解的属性。这些特征作为赌博机策略的上下文，实现了基于特征条件的查询重写，而非“一刀切”的规则，这与先前工作中对原始提示或静态规则的依赖形成了区别。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为QueryBandits的模型无关的上下文多臂老虎机框架来解决大语言模型（LLM）中的幻觉缓解问题，特别是针对无法进行参数编辑的闭源模型。其核心思想是：没有一个单一的查询改写策略适用于所有查询，因此需要根据查询的语义特征，在线自适应地选择最优的改写策略。

**整体框架与核心方法**：
该框架将查询改写问题形式化为一个**上下文多臂老虎机**问题。在每个回合 `t`，系统会观察到一个代表查询语义特征的**上下文向量** `x_t`（一个17维的二进制特征向量，捕捉影响理解的语法属性），然后从**动作空间** `A` 中选择一个“臂”（即一种特定的查询改写策略）。执行改写后，系统会收到一个标量**奖励** `r_t`，用于评估改写的效果。算法的目标是通过在线学习，最大化累积奖励。

**主要模块/组件**：
1.  **动作空间（改写策略）**：定义了五种不同的查询改写策略（即五个“臂”），包括：`Paraphrase`（释义）、`Simplify`（简化）、`Disambiguate`（消歧）、`Expand`（扩展）和`Clarify Terms`（澄清术语）。每种策略都通过特定的提示词指令，利用一个LLM（如GPT-4o）来实现。
2.  **上下文特征**：为每个查询提取一个17维的二进制特征向量，这些特征基于语言学动机，用于描述查询的属性，为策略选择提供依据。
3.  **奖励模型**：这是一个关键创新点。奖励 `r_t` 是一个在[0,1]范围内的复合值，由三个互补的正确性信号**凸组合**而成：
    *   `s_llm`：基于GPT-4o的评估器给出的二进制正确性判断。
    *   `s_fuzz`：基于RapidFuzz的软字符串重叠相似度。
    *   `s_bleu`：基于BLEU-1的单语精确度（带单位上限）。
    通过网格搜索和帕累托前沿分析，论文确定了最优权重组合为 `(α, β, γ) = (0.6, 0.3, 0.1)`。这种设计既利用了LLM作为评判者的语义判断能力，又通过模糊匹配和BLEU提供了更丰富、渐进的奖励信号，避免了单一指标的缺陷和奖励分布的退化，有利于探索-利用的平衡。
4.  **学习算法**：框架支持多种上下文老虎机算法，包括线性UCB（LinUCB）、跟随正则化领导者（FTRL）和**汤普森采样**。实验表明，汤普森采样表现最佳。

**创新点**：
1.  **问题定位与模型无关性**：专注于解决闭源LLM的幻觉问题，提出了一种纯**前向传播机制**的解决方案。它不依赖于模型参数访问、微调或梯度更新，因此完全适用于黑盒闭源模型。
2.  **自适应策略选择**：核心创新是认识到“没有一种改写策略适合所有查询”，因此采用上下文老虎机框架，根据查询的**语义特征（上下文）** 动态学习选择最优策略，而非使用零样本的静态策略。
3.  **经验验证的复合奖励函数**：设计并严格验证了一个结合了语义、模糊匹配和词汇层面信号的奖励函数。该函数高度 discriminative（ROC-AUC > 0.97），且对权重扰动鲁棒，为在线学习提供了稳定、有效的指导信号。
4.  **实证有效性**：在16个QA场景上的实验表明，最好的QueryBandit策略（汤普森采样）相对于“不改写”基线取得了87.5%的胜率，并且显著优于任何

### Q4: 论文做了哪些实验？

论文实验设置了一个基于上下文多臂老虎机（Contextual Bandit）的在线学习框架QueryBandits，用于动态选择最优查询改写策略以减轻大语言模型的幻觉。实验流程包括：对查询提取17维二元语言特征向量，老虎机根据特征选择改写策略（共5种，包括不改写、释义、扩展等），将改写后的查询提交给GPT-4o-2024-08-06生成回答，并通过校准的奖励函数评估回答质量（奖励值r_t∈[0,1]），最后更新老虎机状态。

实验在16个问答场景（基于13个多样化QA基准数据集）上进行，每个场景采样约1050个查询。查询需满足两个条件：原始查询能被GPT-4o正确回答，且其1-3个语义不变但词汇扰动的变体会导致错误回答，以此规避模型对常见基准的提示记忆问题。实验对比了3种非上下文老虎机、6种线性上下文老虎机、零样本静态改写策略以及不改写基线。总评估轮次约252,000次（15种算法×16场景×1050查询），超参数通过网格搜索在验证集上优化。

主要结果：表现最佳的上下文Thompson Sampling老虎机相比不改写基线取得了87.5%的胜率，并分别超越零样本静态释义（Paraphrase）和扩展（Expand）策略42.6%和60.3%。所有上下文老虎机在所有数据集上均优于普通老虎机，且特征方差越大，策略选择方差也越大，证实了“没有单一改写策略适用于所有查询”的核心发现。此外，某些静态策略的累积遗憾（cumulative regret）甚至高于不改写基线，表明僵化的改写策略可能加剧幻觉。关键指标包括：特征标注稳定性达97.4%-99.7%，奖励评估基于校准函数，最终性能以累积奖励和胜率为衡量标准。

### Q5: 有什么可以进一步探索的点？

该论文提出的QueryBandits框架虽在缓解幻觉方面效果显著，但仍存在一些局限和可拓展方向。首先，其依赖的语义特征提取和奖励函数校准可能受限于特定领域或任务，在更复杂的多轮对话或专业领域（如法律、医疗）中的泛化能力有待验证。其次，框架目前主要针对单次查询优化，未考虑用户反馈的长期累积效应或动态环境变化，未来可探索结合强化学习进行更长期的策略优化。此外，研究仅关注了查询重写策略，未与其他幻觉缓解技术（如检索增强生成、不确定性量化）深度融合，集成多种方法可能进一步提升效果。从实践角度看，如何降低在线学习中的计算和延迟开销，以适用于实时系统，也是关键挑战。最后，论文未深入探讨不同闭源模型内部机制差异对策略选择的影响，未来可研究模型无关特征与模型特定特征的结合，以实现更精细的自适应控制。

### Q6: 总结一下论文的主要内容

这篇论文针对大语言模型（LLM）在推理过程中产生的幻觉问题，特别是闭源模型缺乏有效缓解手段的现状，提出了一个名为QueryBandits的模型无关解决方案。其核心问题是：如何在不依赖模型内部参数或重新训练的情况下，动态地为不同查询选择最优的查询重写策略，以减轻幻觉。

方法上，论文提出了一个上下文赌博机框架。该框架将不同的查询重写策略（如改写、扩展）视为“臂”，通过在线学习，根据查询的语义特征（上下文）和经过校准的奖励函数（用于评估回答质量），自适应地选择能最大化回答准确性的策略。其核心思想是“没有一种策略适合所有查询”。

主要结论和贡献在于：1）实验表明，基于汤普森采样的QueryBandits在16个QA场景中显著优于无重写基线及所有静态策略，证明了自适应策略的必要性和优越性。2）研究发现，僵化的静态重写策略有时比不重写产生更严重的幻觉（更高的累积遗憾）。3）该方法完全通过前向传递机制改变模型行为，无需访问梯度或重新训练，因此特别适用于无法修改的闭源模型，为实际部署中的幻觉缓解提供了实用且有效的新途径。
