---
title: "Scaling Retrieval-Augmented Reasoning with Parallel Search and Explicit Merging"
authors:
  - "Jiabei Liu"
  - "Wenyu Mao"
  - "Junfei Tan"
  - "Chunxu Shen"
  - "Lingling Yi"
  - "Jiancan Wu"
  - "Xiang Wang"
date: "2026-05-13"
arxiv_id: "2605.13534"
arxiv_url: "https://arxiv.org/abs/2605.13534"
pdf_url: "https://arxiv.org/pdf/2605.13534v1"
categories:
  - "cs.AI"
tags:
  - "检索增强生成"
  - "多查询检索"
  - "强化学习"
  - "推理优化"
  - "Agent架构"
relevance_score: 8.0
---

# Scaling Retrieval-Augmented Reasoning with Parallel Search and Explicit Merging

## 原始摘要

Deep search agents have proven effective in enhancing LLMs by retrieving external knowledge during multi-step reasoning. However, existing methods often generate a single query for retrieval at each reasoning step, limiting information coverage and introducing high noise. This may result in low signal-to-noise ratios (SNR) during search, degrading reasoning accuracy and leading to unnecessary reasoning steps. In this paper, we introduce MultiSearch, an RL-based framework that addresses these limitations through multi-query retrieval and explicit merging of retrieved information. At each reasoning step, MultiSearch generates queries from multiple perspectives and retrieves external information in parallel, expanding the scope of relevant information and mitigating the reliance on any single retrieval result. Then, the agent consolidates and refines retrieved information at the merging process, improving the SNR and ensuring more accurate reasoning. Additionally, we propose a reinforcement learning framework with a multi-process reward design to optimize agents for both multi-query retrieval and information consolidation. Extensive experiments on seven benchmarks demonstrate that MultiSearch outperforms baseline methods, enhancing the SNR of retrieval and improving reasoning performance in question-answering tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有深度搜索智能体在检索增强生成中的两个核心问题：**低信噪比** 和 **缺乏细粒度监督**。

**研究背景**：大型语言模型(LLM)在知识密集型任务中受限于静态内部知识。检索增强生成(RAG)通过引入外部知识缓解此限制，而深度搜索智能体在推理过程中进行多步检索，能应对更复杂的多跳问题。

**现有方法不足**：当前主流方法(如ReAct范式)在每个推理步骤仅生成单一查询进行检索。这导致两个问题：一是检索范围受限，单查询可能只捕获部分信息，尤其当查询模糊或与语料库不匹配时，会引入大量噪声，导致检索信号信噪比(SNR)低，降低推理精度或增加不必要的步骤；二是现有强化学习方法主要使用最终答案正确性等结果级奖励，缺乏对查询生成、信息筛选等中间行为的有效监督，无法引导模型提升检索质量和减少噪声。

**本文核心问题**：针对上述限制，论文提出**MultiSearch框架**，目的是通过**并行多查询检索**和**显式信息合并**机制，在每一推理步骤扩大信息覆盖面、提高检索信号的信噪比，并设计**多进程奖励机制**，对检索和合并过程进行细粒度监督，从而提升深度搜索智能体在问答任务中的推理准确性。

### Q2: 有哪些相关研究？

相关研究主要分为两类：

1. **深度搜索代理方法**：如Search-R1将搜索引擎作为环境并使用时序奖励引导搜索；R1-Searcher采用两阶段训练提升搜索格式与答案准确性；AutoRefine和EviNote-RAG关注检索后处理或任务特定奖励；还有基于原则的奖励模型提供中间监督。它们的共同局限是依赖单查询检索，限制了信息覆盖。本文提出的MultiSearch通过并行多查询检索和显式融合，在每个推理步骤从多角度生成查询并并行检索，扩大了相关信息范围，提升了信噪比。

2. **强化学习方法**：RLHF和PPO因稳定学习被广泛使用，但计算成本高。简化变体如DPO和GRPO被提出。早期RL多用于偏好对齐，近期如PPO和GRPO被用于检索增强推理场景。本文采用GDPO（Group reward-Decoupled Normalization Policy Optimization），它是GRPO的改进变体，专为处理多奖励目标设计，用以联合优化多查询生成与信息融合策略，实现更高效的强化学习训练。

### Q3: 论文如何解决这个问题？

MultiSearch通过并行多查询检索和显式信息合并机制来解决现有方法检索范围有限、噪声高和信噪比低的问题。其核心方法包括三个主要组件：多查询生成、显式合并和基于强化学习的训练框架。

在推理的每一步，代理使用三种查询生成策略——重新措辞、概念扩展和问题分解——从不同视角生成多个查询，并并行调用搜索引擎进行检索。重新措辞可以覆盖不同的词汇和句法表达，避免因措辞不匹配而遗漏信息；概念扩展通过添加同义词或上位词来扩大搜索范围；问题分解则将复杂问题拆解为子问题并行处理。这一设计有效拓展了信息覆盖面，减少了对单一检索结果的依赖。

检索到文档后，代理首先去除冗余和无关内容，然后显式地将关键信息提取并整合到`merge`模块中，形成更精确的证据支撑。这一显式合并过程提升了信息信噪比，为后续推理提供了更可靠的依据。

在训练阶段，MultiSearch引入了多粒度奖励机制，包括答案奖励（基于F1分数评估预测准确性）、多查询奖励（鼓励每步生成多个查询）和合并奖励（确保合并内容包含正确答案）。仅有答案正确时才会激活后两个奖励，体现了“结果导向”的训练策略。同时，论文提出了组奖励解耦归一化策略优化（GDPO），将不同奖励组件在组内独立归一化后再加权聚合，避免了传统GRPO直接求和导致的无差别对待问题，使模型能更精细地接收多种信号的优化反馈。通过这一完整框架，MultiSearch显著提升了检索增强推理的信噪比和最终答案准确性。

### Q4: 论文做了哪些实验？

论文在七个问答基准上进行了实验，包括单跳数据集（NQ、TriviaQA、PopQA）和多跳推理数据集（HotpotQA、2WikiMultiHopQA、Musique、Bamboogle）。使用Qwen2.5-3B/7B作为骨干模型，E5为搜索引擎，2018年Wikipedia为数据源，EM为评估指标。对比方法分为三类：无检索方法（Direct Generation、CoT、SFT、R1-finetuning）、单次静态检索（RAG）、多轮动态检索（Search-o1、IRCoT、ReSearch、Search-R1、AutoRefine、Dr.Zero、AdaSearch、CriticSearch等）。

主要结果：MultiSearch在3B和7B模型上均获得七项基准平均最佳成绩（3B-Instruct: 0.416, 3B-Base: 0.422; 7B-Base: 0.445）。消融实验显示，去除合并奖励、多查询奖励或合并步骤均导致性能下降（例如，在3B-Instruct上w/o all降为0.374）。查询策略实验表明，多种策略（重述、概念扩展、问题分解）混合优于单一策略，且简单多查询（无策略）性能最低（0.378）。超参数敏感性实验表明，查询数n_q=3、检索深度k=3时性能最佳。此外，对比GRPO和GDPO，GDPO因独立标准化各奖励成分而实现更鲁棒的优化和更好性能。

### Q5: 有什么可以进一步探索的点？

MultiSearch在提升检索信噪比和推理性能方面表现出色，但其局限性和未来探索方向值得深入。首先，方法依赖生成固定数量的并行查询，可能导致冗余或遗漏关键视角，未来可探索动态自适应查询生成，根据当前推理状态调整查询数量和方向，或使用强化学习优化查询生成的多样性。其次，显式合并过程可能受限于模型容量，对长上下文或矛盾信息处理能力不足，可引入图结构或注意力机制进行结构化合并，提升噪声过滤效率。此外，多进程奖励设计虽有效，但可能引入稀疏奖励问题，导致训练不稳定，未来可结合课程学习或偏好优化来改进。最后，当前仅在问答任务上验证，扩展到代码生成、科学论文检索等复杂场景的泛化能力尚待检验，也可探索与工具使用或记忆机制的协同作用。

### Q6: 总结一下论文的主要内容

这篇论文提出MultiSearch框架，旨在解决现有深度搜索代理在多步推理中依赖单一检索查询导致信息覆盖不足和噪声高的问题。其核心贡献在于通过强化学习实现多查询并行检索和显式信息合并。具体而言，在每个推理步骤，模型从重述、概念扩展、问题分解等不同视角生成多个查询并并行检索，以扩大相关信息范围；随后通过显式合并步骤整合和精炼检索信息，提高信噪比。为优化这一过程，论文设计了多进程奖励机制，包括最终答案正确性的结果奖励、鼓励多查询检索的奖励以及促进信息合并的奖励，并使用分组奖励解耦归一化策略优化策略。在七个问答基准上的实验表明，MultiSearch显著提升了检索信噪比和推理性能，验证了增强检索覆盖与信息合并对构建更高效深度搜索代理的重要性。
