---
title: "Truncated Step-Level Sampling with Process Rewards for Retrieval-Augmented Reasoning"
authors:
  - "Chris Samarinas"
  - "Haw-Shiuan Chang"
  - "Hamed Zamani"
date: "2026-02-26"
arxiv_id: "2602.23440"
arxiv_url: "https://arxiv.org/abs/2602.23440"
pdf_url: "https://arxiv.org/pdf/2602.23440v1"
categories:
  - "cs.CL"
  - "cs.IR"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 8.0
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "SLATE (Step-Level Advantage estimation for Truncated Exploration), truncated step-level sampling, dense LLM-as-judge rewards"
  primary_benchmark: "N/A"
---

# Truncated Step-Level Sampling with Process Rewards for Retrieval-Augmented Reasoning

## 原始摘要

Training large language models to reason with search engines via reinforcement learning is hindered by a fundamental credit assignment problem: existing methods such as Search-R1 provide only a sparse outcome reward after an entire multi-step trajectory, making it infeasible to attribute success or failure to individual reasoning and retrieval decisions. Process-reward methods like StepSearch alleviate this by introducing step-level supervision, but rely on heuristic rewards such as TF-IDF overlap with gold documents, and still sample k complete trajectories per example, retaining high gradient variance. We propose SLATE, a framework built on two complementary ideas: (1) truncated step-level sampling, which generates k trajectories that share a common prefix and differ only at the next step, and (2) dense LLM-as-judge rewards, which replace heuristic scoring with a capable LLM evaluator that assesses the quality of each reasoning step, search query, and answer, providing richer and more reliable supervision. We theoretically prove that under the same dense reward structure, truncated sampling reduces the variance of advantage estimates by up to a factor of T compared to full-trajectory sampling for T-step trajectories, yielding lower-variance, better-targeted policy gradients. Experiments on seven QA benchmarks confirm that SLATE consistently outperforms both sparse-reward and process-reward baselines, with the largest gains on harder multi-hop tasks and smaller models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决使用强化学习训练大语言模型进行检索增强推理时面临的信用分配难题。现有方法如Search-R1仅在整个多步推理轨迹结束后提供稀疏的结果奖励，导致模型难以将成功或失败归因于具体的推理和检索决策。虽然StepSearch等过程奖励方法通过引入步骤级监督缓解了这一问题，但仍依赖TF-IDF重叠等启发式奖励，并且需要对每个示例采样k条完整轨迹，导致梯度估计方差较高。本文提出的SLATE框架通过两个核心创新应对这些不足：一是截断式步骤级采样，通过生成共享共同前缀、仅在下一步不同的k条轨迹，直接在步骤层面计算优势估计；二是密集的LLM-as-Judge奖励，用大语言模型评估器替代启发式评分，对每个推理步骤、搜索查询和答案进行细粒度评估。该方法在理论上证明了在相同密集奖励结构下，截断采样能将优势估计的方差降低至多T倍（T为轨迹步数），从而产生更低方差、更精准的策略梯度。实验在七个QA基准测试中验证了SLATE相对于稀疏奖励和过程奖励基线的持续优势，尤其在复杂多跳任务和小模型上提升显著。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：检索增强生成、强化学习用于LLM推理，以及搜索增强的强化学习。

在检索增强生成（RAG）方面，相关工作旨在将外部知识整合到LLM中。标准RAG方法适用于简单查询，但在需要迭代检索的多跳推理任务上存在局限。后续研究将搜索引擎视为工具，让LLM自主决定搜索时机和内容，但这些基于提示或监督微调的方法要么泛化能力不足，要么需要昂贵的轨迹标注。

在强化学习用于LLM推理方面，政策梯度方法（如PPO、GRPO）已被广泛用于训练推理模型。例如，GRPO通过从多个采样响应计算组内相对优势，避免了单独训练评论家模型。然而，将这些方法应用于搜索增强场景时，在奖励设计、信用分配和检索内容整合方面面临独特挑战。

在搜索增强的强化学习方面，Search-R1开创了在推理轨迹中穿插搜索引擎调用的RL训练范式，但仅使用基于最终结果的稀疏奖励（如精确匹配）。后续的R1-Searcher、ReSearch等工作均依赖此类稀疏全局奖励。StepSearch试图通过引入逐步奖励（如基于TF-IDF与黄金文档重叠的信息增益）来缓解奖励稀疏性问题，但仍需对每个示例采样完整的轨迹，且依赖对黄金中间文档的访问来计算启发式奖励。

本文提出的SLATE框架与上述所有工作的核心区别在于：1）采用了**截断的步级采样**，让多条轨迹共享前缀并仅在下一步产生差异，而非采样多条完整独立轨迹，这理论上大幅降低了优势估计的方差；2）使用**基于LLM评判器的密集奖励**来评估每一步推理、搜索查询和答案的质量，取代了StepSearch等依赖黄金文档的启发式奖励，从而提供了更丰富、更可靠的监督信号，且无需中间步骤的标注数据。

### Q3: 论文如何解决这个问题？

论文通过提出名为SLATE的框架来解决检索增强推理中的信用分配和梯度方差问题，其核心方法结合了截断的步级采样和密集的LLM作为评判者的奖励机制。

整体框架基于多轮搜索交互环境，将搜索引擎视为环境的一部分，语言模型策略生成与搜索调用交错的轨迹。主要模块包括：1）**截断步级采样**：在每一步t，基于共享的前缀轨迹τ<t，从策略中采样k个候选下一步动作（包括推理步骤和搜索查询），而非采样k条完全独立的完整轨迹。这确保了候选动作仅在当前步产生差异，从而显著降低了优势估计的方差。2）**密集LLM评判奖励**：使用一个能力强的LLM评估器来为每一步提供精细奖励，替代了基于启发式规则（如TF-IDF重叠）的奖励。奖励分为推理奖励、查询奖励和最终答案奖励，均采用三元评分（-1, 0, +1），并通过“先推理后评分”的提示协议提高可靠性。3）**优化集成**：将上述组件整合到改进的GRPO目标中。在每一步，计算k个候选动作的步级优势，并通过奖励加权采样选择动作以平衡探索与利用。策略梯度计算仅针对模型生成的令牌，并应用损失掩码和KL正则化。

创新点在于：第一，截断采样理论上能将T步轨迹的优势估计方差降低高达T倍，实现了更低方差、更精准的梯度更新；第二，密集的LLM评判奖励提供了更丰富、可靠的步级监督，无需依赖黄金文档；第三，框架引入了早期终止奖励，鼓励模型在获得足够信息后及时给出答案，避免冗余搜索。这些设计共同解决了稀疏结果奖励的信用分配难题和传统过程奖励方法的高方差问题。

### Q4: 论文做了哪些实验？

论文在七个问答基准数据集上进行了实验，涵盖通用问答（NQ、TriviaQA、PopQA）和多跳问答（HotpotQA、2WikiMultiHopQA、Musique、Bamboogle）。实验设置使用Qwen2.5-7B-Base和Qwen2.5-3B-Base模型，以2018年维基百科为知识源，E5为检索器，每查询检索前3个段落。训练数据合并了NQ和HotpotQA的训练集，使用GRPO作为基础RL算法，关键参数包括策略学习率1e-6、每步截断采样数k=5、裁剪比率ε=0.2等。奖励模型采用Gemma3-27B作为LLM评判器。主要对比方法包括无检索推理（直接生成、思维链）、检索增强推理（RAG、IRCoT、Search-o1）、微调方法（监督微调、无搜索的RL）以及搜索强化学习方法（SearchR、ZeroSearch、ReSearch、StepSearch）。

主要结果以精确匹配（EM）为指标。在7B模型上，SLATE平均EM为0.461，相比SearchR（0.431）绝对提升3.0%（相对提升7.0%），在所有数据集上均取得最佳性能。在3B模型上提升更显著（0.396 vs. 0.303，相对提升30.7%）。多跳任务上提升最大：在Musique（7B）上相比SearchR和StepSearch分别提升5.1%和3.1%；在Bamboogle（7B）上分别提升6.2%和2.7%。通用问答任务上也有稳定提升（1.3-1.9%）。消融实验表明，移除截断采样平均EM下降1.1%，移除LLM评判器奖励下降2.4%，仅使用最终步EM奖励则性能接近SearchR（0.368 vs. 0.361），证实两个组件的互补作用。训练动态显示SLATE收敛速度比StepSearch快约20%，且奖励更高更稳定。

### Q5: 有什么可以进一步探索的点？

该论文提出的SLATE框架在降低梯度方差和提供细粒度奖励方面取得了进展，但仍存在一些局限性和可进一步探索的方向。首先，其依赖的LLM-as-judge奖励机制可能引入评估偏差，因为作为评判者的LLM本身可能存在局限性或固有偏见，未来可研究如何通过多模型集成或更客观的指标来提升奖励的可靠性。其次，该方法在计算成本上仍有优化空间，例如通过动态调整采样数量k或引入更高效的价值函数近似来平衡效率与效果。此外，当前方法主要针对问答任务，未来可探索其在更复杂的多模态推理或交互式决策场景中的泛化能力。另一个方向是结合课程学习或元学习，让模型逐步适应从简单到复杂的检索推理任务，以提升训练稳定性和最终性能。最后，理论分析虽证明了方差降低，但实际训练中的探索-利用权衡仍需更细致的策略设计，例如引入不确定性感知的探索机制，以进一步提升策略优化的效果。

### Q6: 总结一下论文的主要内容

该论文针对检索增强推理任务中强化学习训练大语言模型时存在的信用分配问题，提出了一种名为SLATE的新框架。核心问题是稀疏的轨迹级奖励难以评估多步推理中每个决策的贡献，而现有过程奖励方法虽引入步骤级监督，但仍依赖启发式奖励且采样方差高。

SLATE的核心贡献包含两个互补思想：一是截断步骤级采样，它生成共享共同前缀、仅在下一步不同的多个轨迹，大幅减少了采样方差；二是密集的LLM作为评判员的奖励，用能力强的LLM评估器替代启发式评分，为每个推理步骤、搜索查询和答案提供更丰富可靠的监督。论文从理论上证明，在相同密集奖励结构下，对于T步轨迹，截断采样能将优势估计的方差降低多达T倍，从而得到方差更低、目标更明确的策略梯度。

实验在七个问答基准上进行，结果表明SLATE在性能上 consistently 优于稀疏奖励和过程奖励基线，尤其在更困难的多跳任务和较小模型上提升最为显著。该工作为高效训练检索增强推理模型提供了理论依据和有效方法。
