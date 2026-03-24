---
title: "Counterfactual Credit Policy Optimization for Multi-Agent Collaboration"
authors:
  - "Zhongyi Li"
  - "Wan Tian"
  - "Yikun Ban"
  - "Jinju Chen"
  - "Huiming Zhang"
  - "Yang Liu"
  - "Fuzhen Zhuang"
date: "2026-03-23"
arxiv_id: "2603.21563"
arxiv_url: "https://arxiv.org/abs/2603.21563"
pdf_url: "https://arxiv.org/pdf/2603.21563v1"
github_url: "https://github.com/bhai114/ccpo"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent Collaboration"
  - "Credit Assignment"
  - "Reinforcement Learning"
  - "Policy Optimization"
  - "Counterfactual Reasoning"
  - "LLM Training"
  - "Mathematical Reasoning"
  - "Logical Reasoning"
relevance_score: 8.5
---

# Counterfactual Credit Policy Optimization for Multi-Agent Collaboration

## 原始摘要

Collaborative multi-agent large language models (LLMs) can solve complex reasoning tasks by decomposing roles and aggregating diverse hypotheses. Yet, reinforcement learning (RL) for such systems is often undermined by credit assignment: a shared global reward obscures individual contributions, inflating update variance and encouraging free-riding. We introduce Counterfactual Credit Policy Optimization (CCPO), a framework that assigns agent-specific learning signals by estimating each agent's marginal contribution through counterfactual trajectories. CCPO builds dynamic counterfactual baselines that simulate outcomes with an agent's contribution removed, yielding role-sensitive advantages for policy optimization. To further improve stability under heterogeneous tasks and data distributions, we propose a global-history-aware normalization scheme that calibrates advantages using global rollout statistics. We evaluate CCPO on two collaboration topologies: a sequential Think--Reason dyad and multi-agent voting. Across mathematical and logical reasoning benchmarks, CCPO mitigates free-riding and outperforms strong multi-agent RL baselines, yielding finer-grained and more effective credit assignment for collaborative LLM training. Our code is available at https://github.com/bhai114/ccpo.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体大语言模型协作训练中的信用分配问题。研究背景是，尽管多智能体协作（如角色分解或投票聚合）能提升复杂推理任务的性能，但现有的强化学习方法在训练此类系统时面临根本性挑战：团队共享的全局奖励掩盖了个体贡献，导致更新方差大、鼓励“搭便车”行为，从而损害训练效果。

现有方法的不足主要体现在三个方面。首先，在LLM推理任务中，奖励通常是稀疏且延迟的（如最终答案对错），难以追溯哪个智能体的行为真正影响了结果。其次，简单的奖励共享机制会诱发“搭便车”，即智能体即使输出冗余或有害内容也可能获得正向更新，导致梯度有偏且噪声大。再者，协作模式具有角色和结构依赖性（如非对称的“思考-推理”流水线与对称的投票机制），而现有方法（如为连续控制设计的值分解方法）无法灵活适应这种异构性，且难以在LLM的长序列离散生成空间中高效计算信用。

因此，本文要解决的核心问题是：如何在有限的计算预算下，为协作式多智能体LLM推理任务，设计一种准确、稳定且对协作角色敏感的**反事实信用分配方法**。具体而言，论文提出的CCPO框架试图通过估计每个智能体的边际贡献（即假设移除该智能体贡献时的反事实团队表现），来生成个体化的学习信号，从而精准分配信用、抑制“搭便车”，并适配不同的协作拓扑结构，最终实现更有效的多智能体联合训练。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多智能体强化学习中的信用分配、语言模型强化学习优化方法，以及面向大语言模型的多智能体协作训练。

在**多智能体强化学习信用分配**方面，主流方法包括基于价值分解的方法（如QMIX）和基于反事实估计的方法。前者通过假设单调性将团队价值分解为个体效用，但难以适应语言协作中非单调且高度上下文依赖的交互；后者通过比较实际结果与假设情景（如Shapley值）来估计边际贡献，但计算开销巨大，尤其不适用于生成长序列的LLM场景。本文提出的CCPO框架属于反事实方法，但通过构建轻量级、角色感知的反事实基线，显著降低了计算成本，避免了额外重采样，从而解决了现有方法在实用性与精确性之间的张力。

在**语言模型强化学习优化**方面，经典策略梯度方法（如REINFORCE、PPO）及其在LLM微调中的改进（如GRPO、HA-DW等）主要关注单策略优化中的优势估计稳定性问题。这些方法通常缺乏对多智能体场景中信用分配的结构性考虑。CCPO建立在GRPO式的群体统计优势估计基础上，关键创新在于将共享的团队奖励转化为基于反事实的、智能体特定的优势信号，从而在无需昂贵价值网络的情况下实现稳定更新。

在**多智能体协作训练**方面，现有研究可分为推理时协作（如辩论、角色分配）和训练时学习。近期工作如ILR、MAGRPO等开始通过多智能体RL目标鼓励合作，但多依赖共享奖励或启发式信用分配，未能显式隔离边际因果贡献，导致搭便车等问题。CCPO将信用分配视为协作LLM训练的核心瓶颈，通过反事实基线显式估计每个智能体的边际贡献，为异构协作拓扑提供了一种通用且可扩展的机制。

### Q3: 论文如何解决这个问题？

论文通过提出“反事实信用策略优化”（CCPO）框架来解决多智能体协作中的信用分配问题。其核心方法是利用反事实轨迹来估计每个智能体的边际贡献，从而为每个智能体生成针对其角色的、细粒度的学习信号，而非依赖模糊的全局共享奖励。

整体框架基于策略梯度方法。其主要模块与关键技术包括：
1.  **反事实基线生成**：这是CCPO的核心创新点。对于每个智能体，框架会动态构建一个“反事实基线”，即模拟在该智能体不做出贡献（例如，其输出被替换为默认或平均行为）的情况下，整个系统的预期回报。通过比较实际轨迹的回报与反事实基线，可以计算出该智能体专属的优势函数。这直接量化了其个体行为对团队成功的具体影响，有效区分了贡献者与“搭便车”者。
2.  **角色敏感的策略优化**：利用上述计算出的智能体专属优势函数，对每个智能体的策略进行独立更新。这确保了学习信号与智能体的具体角色和行为直接相关，实现了更精准的信用分配。
3.  **全局历史感知归一化**：为了应对异构任务和数据分布带来的训练不稳定问题，CCPO引入了另一项关键技术。该方法利用全局的历史回合统计数据（如所有智能体在所有回合中优势值的均值和方差）来校准每个智能体的优势值。这种归一化操作稳定了更新尺度，提高了学习过程的鲁棒性。

在架构设计上，CCPO被应用于两种典型的协作拓扑进行验证：顺序执行的“思考-推理”二人组和并行多智能体投票。其实验表明，该方法能有效缓解搭便车现象，在数学和逻辑推理基准测试上超越现有的多智能体强化学习基线。其根本创新在于将经济学中的“边际贡献”概念与反事实推理相结合，为协作型大语言模型的训练提供了更精细、更有效的信用分配机制。

### Q4: 论文做了哪些实验？

本文在两个多智能体协作拓扑结构上进行了实验：双智能体“思考-推理”协作模型和三智能体投票协作模型。

**实验设置与数据集**：对于“思考-推理”模型，配置两个角色不同的智能体，分别负责生成思考过程和推断最终答案。模型参数分别使用 qwen2.5-1.5b-instruct 和 llama3.1-8b-instruct 初始化，以验证算法在不同框架和参数规模下的有效性。训练和评估使用数学推理数据集 MATH 7.5k（训练集），其中 MATH500 作为分布内测试样本，AMC23、Gaokao2023en 和 MinervaMath 作为分布外测试样本。对于三智能体投票模型，配置三个独立推理的智能体，同样使用上述不同参数的 LLMs 初始化，在 LogiQA 数据集上训练并在 LogiQA-test 上评估。

**对比方法与主要结果**：主要对比方法包括使用思维链（CoT）策略的双智能体基线、以及同领域的多智能体强化学习基线 ReMA（使用联合奖励）。关键数据指标如下：
1.  **数学推理**：当双智能体均使用 qwen2.5-1.5b-instruct 时，CCPO 相比 CoT 策略平均准确率提升 4.6%，相比 ReMA 提升 1.8%。在分布外样本上，分别优于 CoT 和 ReMA 3.0% 和 2.1%。
2.  **逻辑推理（LogiQA）**：当三智能体均使用 qwen2.5-1.5b-instruct 时，CCPO 相比仅使用联合奖励的基线方法准确率提升 1.5%。
3.  **消融与验证实验**：
    *   **协作有效性验证**：通过将训练后 Agent 1 的输出替换为空内容，发现双智能体协作（实验1）的准确率显著高于 Agent 2 单独作答（实验2），证明了协作机制的有效性，缓解了“懒惰智能体”问题。
    *   **奖励分配合理性**：通过箱线图可视化发现，共享奖励在答案正确时会给两个智能体均分配奖励 1，可能导致搭便车；而反事实奖励能更合理地区分贡献，为能力更强的 Agent 2 分配更高信用。
    *   **计算开销**：实验测量了训练一个周期的时间与 GPU 资源使用。虽然 CCPO 因需计算反事实轨迹比 ReMA 耗时更长，但能获得更高的性能上限。

综上所述，实验从性能提升、协作机制验证、奖励分配合理性和计算开销多角度证明了 CCPO 的有效性。

### Q5: 有什么可以进一步探索的点？

该论文提出的CCPO框架在解决多智能体协作中的信用分配问题上取得了进展，但其仍有进一步探索的空间。局限性在于当前方法主要依赖全局团队奖励的反事实估计，可能无法充分捕捉复杂、动态的协作模式中更细粒度的贡献，例如在非结构化或开放域任务中，智能体间的交互可能更加微妙和多样化。此外，实验集中在数学和逻辑推理基准上，尚未验证在更广泛的实际应用场景（如创意生成或复杂决策）中的泛化能力。

未来研究方向包括：扩展CCPO到更丰富的交互图结构，如循环或分层协作网络，以支持更复杂的多智能体系统；引入过程级奖励或内在动机机制，以在稀疏奖励环境下提供更及时的学习信号；探索在异构或不可靠协作环境中的鲁棒性，例如当部分智能体表现不稳定时如何调整信用分配。改进思路上，可以结合元学习或自适应机制，动态调整反事实基线的计算方式，以更好地适应任务变化；同时，将CCPO与基于语言的信用沟通机制结合，可能进一步提升协作的透明度和效率。这些方向有望推动多智能体LLM训练向更高效、可扩展的方向发展。

### Q6: 总结一下论文的主要内容

本文针对协作式多智能体大语言模型训练中的核心挑战——在稀疏和延迟的团队奖励下进行信用分配——提出了反事实信用策略优化框架。其核心贡献在于通过构建反事实基线来估计每个智能体的边际贡献，从而将全局团队结果转化为针对特定智能体的优势信号，有效缓解了“搭便车”问题并产生了与异构协作动态更匹配的角色敏感学习信号。方法上，CCPO在非对称顺序协作和多智能体投票两种拓扑结构中实例化，并结合了基于全局历史信息的归一化方案以稳定训练。实验表明，在数学和逻辑推理基准上，CCPO在准确性和收敛稳定性上均优于联合奖励基线及其他多智能体强化学习方法。该研究将可扩展的反事实归因确立为训练协作式LLM系统的关键基础，为未来扩展到更丰富的交互图、过程级奖励及异构协作场景奠定了基础。
