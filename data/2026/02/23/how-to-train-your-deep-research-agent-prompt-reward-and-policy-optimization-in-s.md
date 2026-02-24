---
title: "How to Train Your Deep Research Agent? Prompt, Reward, and Policy Optimization in Search-R1"
authors:
  - "Yinuo Xu"
  - "Shuo Lu"
  - "Jianjie Cheng"
  - "Meng Wang"
  - "Qianlong Xie"
  - "Xingxing Wang"
  - "Ran He"
  - "Jian Liang"
date: "2026-02-23"
arxiv_id: "2602.19526"
arxiv_url: "https://arxiv.org/abs/2602.19526"
pdf_url: "https://arxiv.org/pdf/2602.19526v1"
categories:
  - "cs.CL"
tags:
  - "Agent 架构"
  - "Agentic 强化学习"
  - "工具使用"
  - "Agent 评测/基准"
  - "多轮检索"
  - "决策生成"
relevance_score: 9.0
---

# How to Train Your Deep Research Agent? Prompt, Reward, and Policy Optimization in Search-R1

## 原始摘要

Deep Research agents tackle knowledge-intensive tasks through multi-round retrieval and decision-oriented generation. While reinforcement learning (RL) has been shown to improve performance in this paradigm, its contributions remain underexplored. To fully understand the role of RL, we conduct a systematic study along three decoupled dimensions: prompt template, reward function, and policy optimization. Our study reveals that: 1) the Fast Thinking template yields greater stability and better performance than the Slow Thinking template used in prior work; 2) the F1-based reward underperforms the EM due to training collapse driven by answer avoidance; this can be mitigated by incorporating action-level penalties, ultimately surpassing EM; 3) REINFORCE outperforms PPO while requiring fewer search actions, whereas GRPO shows the poorest stability among policy optimization methods. Building on these insights, we then introduce Search-R1++, a strong baseline that improves the performance of Search-R1 from 0.403 to 0.442 (Qwen2.5-7B) and 0.289 to 0.331 (Qwen2.5-3B). We hope that our findings can pave the way for more principled and reliable RL training strategies in Deep Research systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在系统性地研究并解决深度研究智能体（Deep Research Agent）在强化学习训练中存在的配置碎片化和效果不明确的问题。深度研究智能体通过多轮检索和决策生成来处理知识密集型任务，虽然强化学习被证明能提升其性能，但具体哪些训练组件（如提示模板、奖励函数、策略优化算法）真正驱动性能提升，以及它们如何影响预测准确性、训练稳定性和推理成本，此前缺乏深入理解。为此，论文将训练流程解耦为三个关键维度进行剖析：提示模板设计、奖励函数构建和策略优化算法选择。通过实验，论文揭示了现有常用方法（如Slow Thinking模板、F1奖励、PPO/GRPO算法）的局限性，并提出了改进方案（如Fast Thinking模板、加入动作级惩罚的F1奖励、使用REINFORCE算法）。最终，基于这些发现集成了名为Search-R1++的强化基线，显著提升了模型性能。该研究的核心目标是厘清强化学习在深度研究系统中的具体作用，为构建更原则化、可靠的训练策略提供指导。

### Q2: 有哪些相关研究？

相关工作主要围绕深度研究智能体的不同训练范式展开，可分为三类：

1.  **基于提示的智能体**：通过结构化提示（如ReAct框架）显式引导智能体进行迭代推理和检索，相关工作包括Self-RAG、Interleaving等。本文在此基础上对比了“快思考”与“慢思考”提示模板的效果。
2.  **基于监督微调（SFT）的方法**：通过模仿人类或规则生成的搜索轨迹来学习检索时机、查询内容和证据整合，代表工作有Toolformer、Chain-of-RAG等。本文的RL训练是在类似架构上进行的优化，但目标不同。
3.  **基于强化学习（RL）的方法**：将深度研究视为序列决策问题，直接优化长程交互中的搜索与回答策略，如DeepResearcher、R1、ZeroSearch等。本文以Search-R1为基准框架，系统解构并评估了其中提示模板、奖励函数和策略优化三个核心维度，揭示了现有RL训练方案中配置碎片化的问题，并提出了改进方案Search-R1++。

本文与这些工作的关系在于：它并非提出全新范式，而是对当前流行的RL训练路径进行系统性剖析，厘清各组件贡献，旨在为深度研究系统建立更原则、可靠的RL训练策略提供实证基础。

### Q3: 论文如何解决这个问题？

论文通过系统性地解构并优化强化学习训练的三个核心维度——提示模板、奖励函数和策略优化算法，来解决深度研究智能体训练中的稳定性与性能问题。

在提示模板方面，研究发现传统的“慢思考”模板（强制要求在每个决策前进行显式推理）会诱导模型通过堆砌无用的 `<think>` 标签来“刷取”奖励，导致推理过程失控和训练崩溃。因此，论文提出了“快思考”模板，它移除了强制性的显式推理步骤，直接让模型根据问题决定是否搜索和生成答案。这种设计限制了无效推理的膨胀，将策略更新的焦点集中在搜索和回答等关键决策上，从而获得了更稳定的训练过程和更高的最终准确率。

在奖励函数方面，论文发现单纯基于结果（如F1分数）的奖励会导致智能体采取“回避回答”的捷径策略，因为不回答和答错获得的奖励相同（均为零），这引发了训练崩溃。为解决此问题，论文在F1奖励的基础上引入了动作级别的惩罚项（F1+），对未执行搜索或未生成答案的行为施加轻微惩罚。这种简单的动作监督有效遏制了回避行为，稳定了训练，并使优化F1奖励的模型性能最终超越了使用严格精确匹配（EM）奖励的基线。

在策略优化算法方面，论文在固定其他条件的情况下比较了REINFORCE、PPO和GRPO。研究发现，REINFORCE凭借其直接基于累计回报进行策略更新、不依赖外部基线估计（如价值函数或组内平均）的特性，避免了因基线估计不准或噪声引入的偏差与不稳定。因此，REINFORCE实现了最稳定的训练、最高的整体性能，并且学会了最紧凑的策略（搜索次数最少）。相比之下，PPO因在稀疏奖励下难以准确拟合价值函数，导致搜索成本高且缺乏适应性；GRPO则因在长轨迹中组内优势估计方差大而表现出最差的稳定性。

综合以上发现，论文构建了Search-R1++这一强基线，它整合了“快思考”模板、F1+奖励函数和REINFORCE算法，显著提升了原有Search-R1框架的性能。

### Q4: 论文做了哪些实验？

论文围绕提示模板、奖励函数和策略优化三个维度进行了系统性实验。实验设置基于Search-R1框架，使用Qwen2.5-3B和Qwen2.5-7B模型，通过PPO或REINFORCE等强化学习算法训练。检索使用E5模型在2018年维基百科上检索top-3相关段落。评估在七个基准数据集上进行，分为单跳问答（NQ、TriviaQA、PopQA）和多跳问答（HotpotQA、2WikiMultiHopQA、Musique、Bamboogle），使用精确匹配（EM）作为主要指标。

在提示模板实验中，比较了“快速思考”（无显式推理标签）和“慢速思考”（带<think>标签）模板。结果显示，快速思考模板训练更稳定，平均准确率更高（Qwen2.5-7B从0.403提升至0.422），且能避免因推理标签激增导致的训练崩溃。

在奖励函数实验中，比较了EM、F1以及加入动作惩罚的F1+奖励。发现单纯F1奖励因答案回避导致训练不稳定且性能较差（Qwen2.5-7B平均EM 0.391），而F1+奖励通过惩罚无搜索或无答案行为，实现了更稳定的训练并超越了EM基线（Qwen2.5-7B平均EM 0.429）。

在策略优化实验中，比较了REINFORCE、PPO和GRPO算法。REINFORCE表现出最佳的稳定性和最高的平均准确率（Qwen2.5-7B整体平均0.437），同时搜索次数最少（平均1.35次），效率更高；PPO搜索次数固定且较高；GRPO稳定性最差。

最终，基于上述发现构建的Search-R1++（快速思考模板+REINFORCE+F1+奖励）在Qwen2.5-7B和Qwen2.5-3B上分别将平均准确率提升至0.442和0.331，显著优于原始Search-R1基线。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其研究维度（提示模板、奖励函数、策略优化）虽已系统解耦，但实验主要基于特定模型（Qwen2.5）和搜索增强型研究任务（Search-R1），其结论在其他任务领域（如代码生成、长程规划）和不同规模/架构的基座模型上的泛化能力仍需验证。此外，对训练崩溃（如答案回避）的机制分析仍较现象层面，缺乏更深入的理论解释。

未来方向可从以下几点深入探索：1）**奖励设计**：研究更精细的多目标奖励塑造（如平衡检索成本、信息新颖性、事实准确性），并探索离线偏好学习或基于LLM的奖励模型是否优于人工设计指标。2）**策略优化**：针对GRPO等方法的稳定性问题，可结合熵正则化或课程学习进行改进，并系统比较不同策略梯度算法在Agent训练中的样本效率与收敛特性。3）**泛化评估**：将Search-R1++框架扩展至更复杂的多步骤决策环境（如科学文献综述、竞争性多智能体场景），检验其鲁棒性与可扩展性。4）**训练机制**：探索将强化学习与监督微调、自演进数据合成等方法更深度结合，以降低训练方差并提升策略的泛化能力。

### Q6: 总结一下论文的主要内容

这篇论文对深度研究智能体（Deep Research Agent）中的强化学习应用进行了首次系统性研究。核心贡献在于从三个解耦维度（提示模板、奖励函数和策略优化方法）深入剖析了RL训练的关键设置如何影响智能体的性能、稳定性和推理成本。

研究发现：1）相比先前工作使用的“慢思考”模板，“快思考”模板能带来更好的稳定性和性能；2）基于F1的奖励函数会因答案回避导致训练崩溃，表现不如精确匹配奖励，但通过加入动作级惩罚可以缓解此问题并最终超越后者；3）在策略优化方法中，REINFORCE优于PPO且所需搜索动作更少，而GRPO稳定性最差。

基于这些发现，论文提出了一个名为Search-R1++的强基线方法，它采用“快思考”模板并结合经改进的F1+奖励函数与REINFORCE算法进行训练，显著提升了两个模型版本的性能。这项工作为深度研究系统乃至更广泛的LLM长程推理任务，提供了更原则、可靠的RL训练策略指导。
