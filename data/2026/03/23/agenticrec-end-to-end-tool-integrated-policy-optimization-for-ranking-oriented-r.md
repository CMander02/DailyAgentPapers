---
title: "AgenticRec: End-to-End Tool-Integrated Policy Optimization for Ranking-Oriented Recommender Agents"
authors:
  - "Tianyi Li"
  - "Zixuan Wang"
  - "Guidong Lei"
  - "Xiaodong Li"
  - "Hui Li"
date: "2026-03-23"
arxiv_id: "2603.21613"
arxiv_url: "https://arxiv.org/abs/2603.21613"
pdf_url: "https://arxiv.org/pdf/2603.21613v1"
categories:
  - "cs.IR"
  - "cs.AI"
tags:
  - "Recommender Agent"
  - "Tool Use"
  - "Policy Optimization"
  - "ReAct"
  - "Ranking"
  - "Preference Learning"
  - "End-to-End Training"
relevance_score: 8.5
---

# AgenticRec: End-to-End Tool-Integrated Policy Optimization for Ranking-Oriented Recommender Agents

## 原始摘要

Recommender agents built on Large Language Models offer a promising paradigm for recommendation. However, existing recommender agents typically suffer from a disconnect between intermediate reasoning and final ranking feedback, and are unable to capture fine-grained preferences. To address this, we present AgenticRec, a ranking-oriented agentic recommendation framework that optimizes the entire decision-making trajectory (including intermediate reasoning, tool invocation, and final ranking list generation) under sparse implicit feedback. Our approach makes three key contributions. First, we design a suite of recommendation-specific tools integrated into a ReAct loop to support evidence-grounded reasoning. Second, we propose theoretically unbiased List-Wise Group Relative Policy Optimization (list-wise GRPO) to maximize ranking utility, ensuring accurate credit assignment for complex tool-use trajectories. Third, we introduce Progressive Preference Refinement (PPR) to resolve fine-grained preference ambiguities. By mining hard negatives from ranking violations and applying bidirectional preference alignment, PPR minimizes the convex upper bound of pairwise ranking errors. Experiments on benchmarks confirm that AgenticRec significantly outperforms baselines, validating the necessity of unifying reasoning, tool use, and ranking optimization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的推荐智能体（Recommender Agents）在面向排序任务时存在的两个核心缺陷。研究背景是，LLM凭借其强大的自然语言理解和推理能力，为推荐系统提供了新的范式，能够进行语义匹配和复杂意图理解。然而，推荐本质上是一个基于大规模隐式反馈和协同信号的排序问题，仅靠语言先验知识难以直接捕获。现有方法，无论是通过微调将推荐视为下一个令牌预测，还是采用训练即用的智能体框架（如ReAct循环结合工具），都存在明显不足。首先，现有智能体的中间推理、工具调用行为与最终的排序结果反馈之间存在脱节。这些行为通常由通用的语言先验或手工设计的提示启发式驱动，并未在推荐反馈（如列表级排序效用）的指导下进行端到端优化，导致证据获取与最终决策可能不协调。其次，现有方法缺乏有效机制来解析细粒度的用户偏好。在隐式反馈稀疏的监督下，对于排名靠前、高度相似的候选项目，仅靠粗粒度的列表级信号难以纠正细微的偏好差异，导致智能体在具有挑战性的案例中表现脆弱。

因此，本文要解决的核心问题是：如何构建一个面向排序的推荐智能体框架，能够端到端地优化包含多步推理、工具调用和最终排序列表生成的整个决策轨迹，并在此过程中有效捕捉和细化用户的细粒度偏好。论文提出的AgenticRec框架正是为了弥合推理与排序反馈之间的鸿沟，并解决细粒度偏好模糊性问题。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两大类：**基于大语言模型的推荐系统**和**推荐智能体**。

在**基于大语言模型的推荐系统**方面，相关工作可进一步细分。首先是基于提示的通用推荐方法，如Chat-REC和LLMRank，它们直接利用LLM的指令遵循能力，但存在目标不匹配和对推荐信号不敏感的问题。其次是为推荐任务微调LLM的方法，如P5（统一文本生成范式）、TALLRec（通过点击预测对齐隐式反馈）和LLaRA（融入协同表示），旨在使模型更适应推荐目标。最后是推理增强的推荐方法，通过多步推理或强化学习优化推理过程。这些工作主要提升了单次预测或表征质量，但缺乏在推理时基于列表级监督来渐进优化决策的机制，这是本文要解决的关键差距。

在**推荐智能体**方面，研究旨在为LLM配备决策循环、工具和记忆，以实现交互式推荐。现有工作可分为三类：模拟导向（模拟用户行为）、交互导向（进行对话式偏好获取与解释）以及推荐导向（通过规划、推理和工具使用来提升推荐策略）。本文属于推荐导向的智能体。然而，现有智能体存在两大局限：一是过度依赖LLM先验和提示驱动推理，难以有效融入隐式反馈、协同关系等推荐特定信号；二是工具使用通常是静态的、由预定义流程驱动，未在列表级排序奖励下进行显式优化。本文提出的AgenticRec通过端到端策略优化，将工具调用与列表级排序优化联合学习，从而实现了与真实排序反馈对齐的、结果驱动的动态工具使用。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AgenticRec的端到端框架来解决推荐智能体中推理过程与最终排序反馈脱节、以及难以捕捉细粒度偏好的问题。其核心方法是将交互式推理与结果驱动学习相统一，整体架构基于ReAct范式，并引入了创新的优化技术。

**整体框架与主要模块**：AgenticRec采用两阶段训练。在第一阶段，智能体在给定用户历史 \(x_u\) 和候选集 \(\mathcal{C}\) 后，进入一个ReAct风格的循环：交替生成“思考”(Think)令牌，并可选地执行“行动”(Act)来调用工具，接收工具“观察”(Obs)结果，最终输出一个有效的Top-K排序列表 \(r_K\)。工具调用被视作决策轨迹的一部分，受到严格预算约束（最多10次），以避免过度依赖和延迟。框架集成了四类推荐专用工具：1) 用户画像工具，用于获取用户摘要和持久偏好；2) 物品信息工具，用于查询物品详细属性；3) 行为统计工具，用于提取用户行为特征；4) 协同信息工具，通过轻量级序列推荐器提供用户协同（U2U）和物品协同（I2I）信号。这些工具为智能体提供了基于证据的推理能力，而非仅依赖语言先验。

**关键技术一：列表级分组相对策略优化 (list-wise GRPO)**。这是解决稀疏隐式反馈下优化多步工具调用轨迹的关键。智能体最终输出的排序列表被结构化为文本令牌，其策略似然度在整个生成轨迹（包括思考、行动、排序令牌）上计算。奖励设计综合了排序质量、格式约束和工具使用激励：主要采用NDCG@K作为列表级排序奖励；若输出格式无效则给予固定负奖励；若达成Hit@1且调用了工具则给予小额奖励。GRPO算法通过为每个训练实例采样G条独立轨迹，计算组内相对优势 \(\hat{A}^{(g)} = R^{(g)} - \frac{1}{G}\sum_{j} R^{(j)}\)，并以此优化策略目标函数。这种方法利用组内相对比较显著降低了方差，并将列表级奖励通过整个轨迹传播，实现了对复杂工具使用轨迹的稳定信用分配。

**关键技术二：渐进式偏好细化 (PPR)**。此阶段在列表级GRPO训练之后进行，旨在解决列表级奖励在细粒度偏好区分上的不足。其创新点在于通过自举方式从智能体自身排序违规中挖掘困难负例，并应用双向偏好对齐。具体而言，对于每个输入，检查正例物品 \(c^+\) 是否被排在首位。若未排第一，则将从排序高于 \(c^+\) 的物品中随机采样一个作为困难负例 \(c^-\)，构成偏好对 \((c^+, c^-)\)。随后进行双向偏好推理训练：正向任务要求智能体识别用户更可能交互的物品（\(c^+\)）；创新的负向任务则要求智能体明确识别用户更不可能选择的物品（\(c^-\)）。这两个对称的视角提供了互补的学习信号，共同作用以最小化成对排序误差的凸上界，从而锐化细粒度的偏好边界。

**创新点总结**：1) **工具集成与决策轨迹统一优化**：将推荐专用工具嵌入ReAct循环，并通过强化学习端到端优化工具调用策略，使其结果驱动而非静态。2) **理论无偏的列表级GRPO**：提出新的策略优化方法，直接最大化列表级排序效用，并对多步工具使用轨迹实现精确信用分配。3) **自举的渐进式偏好细化**：通过从排序违规中挖掘困难负例和双向偏好对齐，有效解决了细粒度偏好模糊性问题，无需额外标注。

### Q4: 论文做了哪些实验？

论文在四个Amazon 2023基准子集（CDs、Instruments、Office、Games）上进行了实验，任务是生成Top-10推荐列表，候选集包含1个正样本和19个负样本。

实验设置方面，训练方法采用两阶段范式，分别训练3轮和1轮，组大小为8，批次大小为64，学习率为1e-6。评估指标为NDCG@K和Hit Ratio@K（K=1,5,10）。

对比方法分为三组：1）序列推荐方法（Caser, GRU4Rec, SASRec, ReaRec）；2）免训练的LLM方法（LLMRank, InteRecAgent）；3）可训练的LLM方法（TALLRec, LLaRA, S-DPO, ReRe）。为公平比较，可训练方法均以Qwen3-4B-Instruct为骨干模型。

主要结果显示，AgenticRec在所有数据集和指标上均取得最佳性能。关键数据指标上，在Office数据集上，其H@10达到约0.85，显著优于基线。分析表明，传统序列方法性能有限；免训练的LLM方法中，InteRecAgent因依赖外部工具（SASRec）而受限；可训练的LLM方法虽优于前两组，但因缺乏工具集成推理能力，性能仍次于AgenticRec。AgenticRec通过端到端优化决策轨迹和渐进式偏好细化，有效提升了排名效果。

### Q5: 有什么可以进一步探索的点？

本文提出的AgenticRec框架在整合推理、工具使用与排序优化方面取得了显著进展，但其仍存在一些局限性和值得深入探索的方向。首先，框架依赖于离线策略优化，在动态变化的用户偏好和实时反馈场景下可能不够灵活，未来可研究在线学习或混合优化策略，以更好地适应实时交互环境。其次，当前工具集虽针对推荐设计，但扩展性和通用性有限；可探索更模块化的工具架构，支持动态工具发现与组合，以处理跨领域或复杂多模态推荐任务。此外，方法对稀疏隐式反馈的处理虽引入理论无偏优化，但在极端稀疏场景下的稳健性仍需验证；结合因果推断或对比学习来增强偏好挖掘能力，可能是有效的改进思路。最后，框架的计算开销较大，未来工作可聚焦于轻量化模型设计或分布式训练策略，以提升可扩展性。这些方向有望进一步推动智能体推荐系统向更高效、自适应和实用的方向发展。

### Q6: 总结一下论文的主要内容

本文提出AgenticRec，一个面向排序的智能推荐代理框架，旨在解决现有基于大语言模型的推荐代理中存在的中间推理与最终排序反馈脱节、难以捕捉细粒度偏好的问题。其核心贡献在于通过端到端的策略优化，将推理、工具使用和排序生成统一到隐式反馈下的决策轨迹优化中。

方法上，首先设计了一套集成在ReAct循环中的推荐专用工具，支持基于证据的推理。其次，提出了理论上无偏的列表级分组相对策略优化方法，以最大化排序效用，确保对复杂工具使用轨迹进行准确的信用分配。最后，引入渐进式偏好细化机制，通过从排序违规中挖掘困难负例并进行双向偏好对齐，最小化成对排序误差的凸上界，从而解析细粒度的用户偏好。

实验结果表明，AgenticRec在基准测试上显著优于基线方法，验证了将推理、工具使用和排序优化进行统一优化的必要性。该框架为构建更精准、可解释的推荐智能体提供了有效的端到端解决方案。
