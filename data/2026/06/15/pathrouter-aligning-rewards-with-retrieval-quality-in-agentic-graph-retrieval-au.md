---
title: "PathRouter: Aligning Rewards with Retrieval Quality in Agentic Graph Retrieval-Augmented Generation"
authors:
  - "Bo Wang"
  - "Heyan Huang"
  - "Yaolin Li"
  - "Wei Tang"
  - "Yuan Zhang"
  - "Wenbo Li"
  - "Mingze Gao"
  - "Ge Shi"
  - "Chong Feng"
date: "2026-06-15"
arxiv_id: "2606.16409"
arxiv_url: "https://arxiv.org/abs/2606.16409"
pdf_url: "https://arxiv.org/pdf/2606.16409v1"
categories:
  - "cs.CL"
tags:
  - "Agentic RAG"
  - "训练方法"
  - "路径对齐"
  - "GRPO"
  - "强化学习"
  - "图检索增强生成"
  - "多跳推理"
relevance_score: 9.5
---

# PathRouter: Aligning Rewards with Retrieval Quality in Agentic Graph Retrieval-Augmented Generation

## 原始摘要

Agentic GraphRAG trains language-model agents to iteratively retrieve and reason over graph-structured evidence, enabling more accurate and context-aware decision-making by efficiently navigating complex information networks. However, outcome-only reinforcement learning suffers from \textit{\textbf{answer-path reward aliasing}}, where correct answers may come from shortcuts rather than useful evidence paths. It also exhibits \textit{\textbf{search-update ambiguity}}, as scalar trajectory-level feedback does not indicate which retrieval actions to adjust. To mitigate these shortcomings, we present PathRouter, a path-aware training framework for agentic GraphRAG. PathRouter jointly evaluates each trajectory along answer correctness and evidence-path overlap, yielding four trajectory categories with differentiated GRPO advantage scaling that suppresses shortcut reinforcement while preserving evidence-seeking behavior. For evidence-poor trajectories, a frozen gold-evidence teacher provides token-level KL guidance on reasoning and search-query tokens, excluding answer tokens to avoid direct response imitation. Experiments on six QA benchmarks across three model sizes show that PathRouter consistently improves answer F1 and evidence-path overlap, achieving average F1 gains of 3.1 on 3B and 4.9 on 7B models compared to a strong baseline.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于图检索增强生成（GraphRAG）的智能体训练中存在的两个核心问题。研究背景是，现有方法通过强化学习训练语言模型智能体，使其能够迭代检索和推理图结构证据，以实现更准确的决策；但传统的奖励设计仅依据最终答案的正确性来评估轨迹，忽略了检索质量与答案之间的对应关系。

这导致了两个关键缺陷：第一，“答案-路径奖励混淆”（answer-path reward aliasing），即智能体可能通过参数记忆中的捷径而非检索到的有效证据路径得到正确答案，但该行为获得了与高质量检索同样的奖励，从而被错误强化；第二，“搜索-更新歧义”（search-update ambiguity），即标量的轨迹级奖励无法告知智能体具体哪些检索动作需要调整，导致策略更新缺乏细粒度的指导。

因此，本文提出PathRouter框架，核心目标是解决奖励混淆和更新歧义问题。具体地，通过同时评估答案正确性和证据路径重叠度来区分轨迹类型，并对不同轨迹实施差异化的分组相对策略优化（GRPO）优势缩放，以抑制捷径学习并鼓励证据导向的行为；同时，对证据不足的轨迹引入冻结的“黄金证据”教师模型，提供词元级KL散度监督来引导检索和推理词的优化，从而在不对最终答案进行直接模仿的前提下，使智能体获得可操作的检索策略改进信号。

### Q2: 有哪些相关研究？

基于论文内容，相关研究可分为三类：**方法类**包括RAG和GraphRAG方法（如基于实体关系图的路径选择、剪枝遍历等），这些方法主要优化图构建和检索策略，但未直接训练生成器与证据路径对齐；而本文PathRouter将证据路径重叠作为训练信号，实现检索质量与答案正确性的对齐。**强化学习类**包括GRPO、Search-R1、R1-Searcher、Graph-R1等，它们依赖结果级奖励，存在将检索质量与参数知识混淆、强化虚假捷径的问题；本文引入证据路径重叠作为第二诊断轴，形成2×2轨迹分类，并根据路径质量调节优势权重。**知识蒸馏与样本路由类**包括SRPO、GiGPO、RLSD等，这些方法通常按答案正确性路由样本或均匀应用教师信号；本文则根据证据路径覆盖度条件化蒸馏，对证据不足的轨迹冻结教师模型，仅对推理和查询标记提供KL引导，减少了答案标记泄露并针对性解决搜索-更新模糊性问题。

### Q3: 论文如何解决这个问题？

论文提出了PathRouter框架，通过路径感知训练解决智能体图检索增强生成中的答案-路径奖励混淆和搜索-更新模糊问题。核心方法包括：首先定义轨迹评估指标，计算答案正确性C_i（基于精确匹配或F1阈值）和证据路径重叠度P_i（检索内容与黄金支持段落集合的平均F1），将轨迹分为四类——C↑P↑（正确且证据充分）、C↑P↓（正确但证据不足，可能存在捷径）、C↓P↑（证据充分但答案错误，可能仅最终推理失败）、C↓P↓（两者均差）。在此基础上创新性地设计路由条件优势缩放，对不同类别轨迹赋予差异化权重：对C↑P↓采用降低权重以抑制捷径强化，对C↓P↑采用衰减权重避免过度惩罚有用检索行为，而对其他两类保持满权重。为处理证据不足轨迹（P_i<θ_P）的搜索-更新模糊问题，引入选择性黄金证据教师模型：冻结参考模型作为教师，在教师提示中附加黄金支持段落，对学生轨迹中推理和搜索查询令牌（排除最终答案和检索观察）进行令牌级前向KL散度蒸馏，采用Top-K词汇约束降低计算成本。最后将路由GRPO损失与教师KL损失联合优化，并设计线性预热机制逐步施加教师约束，同时通过奖励函数整合答案F1、证据路径重叠及探索形状项（多轮探索奖励、单步懒惰惩罚、超时惩罚和冗余惩罚）。整体框架实现了答案准确性与证据忠实性的联合对齐。

### Q4: 论文做了哪些实验？

论文在六个QA基准测试上进行了实验，包括多跳数据集（HotpotQA、2WikiMultiHopQA、MuSiQue，提供黄金支持事实用于评估路径忠实度）和单跳数据集（NQ、PopQA、TriviaQA）。对比方法包括：GPT-4o-mini基方法（GraphRAG、LightRAG等）、非检索方法（NaiveGeneration、SFT、R1）、基于块的检索方法（StandardRAG、Search-R1、R1-Searcher）以及基于图的代理检索方法Graph-R1。评估指标包括答案质量的F1、EM和G-E，以及路径忠实度的SF-F1和UAR。主要结果表明，PathRouter在所有模型规模上均优于Graph-R1：在7B模型上，平均F1从57.82提升至62.74，EM从48.57提升至53.26，G-E从76.23提升至78.72；在3B和1.5B模型上，平均F1分别提升3.1和3.2。消融实验显示，路径奖励、探索奖励和懒惰惩罚对多步证据搜索至关重要，而教师KL指导在证据匮乏轨迹上效果最佳。路由分析表明，PathRouter将轨迹分布从捷径和失败模式转向忠实成功和存在证据的推理失败模式，提升了检索质量。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三方面：首先，PathRouter引入了路由超参数和教师调度策略，在小型模型或新领域应用时需额外调参，可能影响泛化性；其次，路径感知奖励在训练中鼓励更多探索步骤，加上教师模型的逐token KL正则化会增加计算开销，牺牲了训练效率；最后，当前仅依赖固定的“黄金证据路径”作为教师，可能无法覆盖多样化的正确推理路径。

未来可在以下方向深入探索：一是设计自适应超参数调节机制，如基于agent探索动态性自动调整路由策略，减少人工干预；二是探索更轻量的教师模型替代方案，例如通过对比学习蒸馏减少前向传播成本；三是引入多路径集成判断机制，允许模型从多个有效证据路径中学习，避免单一黄金路径的约束。此外，将PathRouter与更高效的图采样策略结合，或尝试在训练中动态剪枝无效搜索动作，有望进一步平衡性能与效率。

### Q6: 总结一下论文的主要内容

本文提出PathRouter，一种针对智能体图检索增强生成(Agentic GraphRAG)的路径感知训练框架。核心问题在于仅基于结果的强化学习存在两大缺陷：一是"答案-路径奖励混淆"，即正确答案可能来自捷径而非有效证据路径；二是"搜索-更新模糊"，即标量轨迹级反馈无法指示应调整哪些检索动作。PathRouter通过联合评估轨迹的答案正确性和证据路径重叠度，将轨迹划分为四类，并采用差异化GRPO优势缩放，抑制捷径强化同时保留证据探索行为。对于证据不足轨迹，冻结的金证教师模型提供令牌级KL指导，但排除答案令牌以避免直接模仿。在三个模型规模的六个QA基准上，PathRouter相比强基线平均F1提升3.1(3B模型)和4.9(7B模型)。该工作通过路径条件化设计实现了比统一蒸馏或纯结果强化更精准的策略优化，解决了智能体检索中的信用分配难题。
