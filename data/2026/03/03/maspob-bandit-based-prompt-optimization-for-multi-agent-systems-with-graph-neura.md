---
title: "MASPOB: Bandit-Based Prompt Optimization for Multi-Agent Systems with Graph Neural Networks"
authors:
  - "Zhi Hong"
  - "Qian Zhang"
  - "Jiahang Sun"
  - "Zhiwei Shang"
  - "Mingze Kong"
date: "2026-03-03"
arxiv_id: "2603.02630"
arxiv_url: "https://arxiv.org/abs/2603.02630"
pdf_url: "https://arxiv.org/pdf/2603.02630v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Learning & Optimization"
relevance_score: 8.0
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "MASPOB (Multi-Agent System Prompt Optimization via Bandits)"
  primary_benchmark: "N/A"
---

# MASPOB: Bandit-Based Prompt Optimization for Multi-Agent Systems with Graph Neural Networks

## 原始摘要

Large Language Models (LLMs) have achieved great success in many real-world applications, especially the one serving as the cognitive backbone of Multi-Agent Systems (MAS) to orchestrate complex workflows in practice. Since many deployment scenarios preclude MAS workflow modifications and its performance is highly sensitive to the input prompts, prompt optimization emerges as a more natural approach to improve its performance. However, real-world prompt optimization for MAS is impeded by three key challenges: (1) the need of sample efficiency due to prohibitive evaluation costs, (2) topology-induced coupling among prompts, and (3) the combinatorial explosion of the search space. To address these challenges, we introduce MASPOB (Multi-Agent System Prompt Optimization via Bandits), a novel sample-efficient framework based on bandits. By leveraging Upper Confidence Bound (UCB) to quantify uncertainty, the bandit framework balances exploration and exploitation, maximizing gains within a strictly limited budget. To handle topology-induced coupling, MASPOB integrates Graph Neural Networks (GNNs) to capture structural priors, learning topology-aware representations of prompt semantics. Furthermore, it employs coordinate ascent to decompose the optimization into univariate sub-problems, reducing search complexity from exponential to linear. Extensive experiments across diverse benchmarks demonstrate that MASPOB achieves state-of-the-art performance, consistently outperforming existing baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体系统（MAS）中提示词优化的难题。随着大语言模型（LLMs）被广泛部署为多智能体系统的认知核心，通过精心设计的提示词来协调复杂工作流已成为提升系统性能的关键。然而，在实际应用中，由于工作流往往经过专家审核和安全验证而难以修改，优化每个智能体的提示词成为主要的性能提升手段。现有方法存在明显不足：单智能体提示优化方法（如OPRO）忽略了智能体间因工作流拓扑结构而产生的耦合效应；而多阶段优化方法（如MIPRO）虽考虑多智能体设置，但通常隐式处理依赖关系，对拓扑结构不敏感，且在评估成本高昂和组合搜索空间巨大的情况下样本效率低下。

本文要解决的核心问题是如何在严格的评估预算限制下，进行样本高效且感知拓扑结构的多智能体系统提示词组合优化。具体挑战包括：（1）评估成本极高，每次尝试都需要端到端运行整个MAS；（2）拓扑结构导致的耦合，即上游提示词的改动会改变下游智能体的输入分布，使优化目标不可分离；（3）组合搜索空间随智能体数量指数级爆炸，使穷举搜索不可行。为此，论文提出了MASPOB框架，通过集成上下文赌博机（利用上置信界平衡探索与利用）、图神经网络（显式编码工作流拓扑以建模耦合效应）和坐标上升法（将组合搜索分解为线性复杂度的子问题）来应对这些挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：提示优化方法、多智能体系统工作流研究，以及样本高效的优化技术。

在**提示优化方法**方面，相关工作从手动启发式工程发展到自动化优化。早期方法如APE和OPRO利用大语言模型自身作为优化器；后续出现了进化搜索（如PromptBreeder、EvoPrompt）、梯度启发或基于梯度的方法（如TextGrad、ProTeGi），以及基于编辑的搜索和强化学习。这些方法大多针对单智能体场景。对于多阶段流程，MIPRO基于DSPy框架，通过贝叶斯优化对模块化程序进行多阶段指令和少样本示例优化，是本文的一个直接基线。然而，通用多阶段优化器难以处理多智能体系统中由拓扑结构引发的依赖关系，即上游提示的微小变化会改变下游智能体的输入分布，导致级联效应和非平稳的优化环境。本文的MASPOB通过图神经网络显式建模拓扑先验，并利用bandit框架实现高效探索，从而区别于这些方法。

在**多智能体系统工作流**方面，现有框架如AutoGen、MetaGPT等支持构建复杂协作流程。近期研究关注结构搜索（如GPTSwarm、AFlow、DyLAN），旨在动态发现有效的交互图与团队组成。然而，许多高风险的工业应用要求工作流遵循专家验证的固定拓扑以确保合规性，这使得结构搜索不适用。与本文最接近的工作是MAPRO，它将多智能体提示优化表述为最大后验推理问题，并提出了语言引导的信念传播变体。MAPRO虽然考虑了智能体间依赖并提供了理论框架，但其复杂的推理过程在大规模组合空间中可能存在效率问题，且未充分考虑评估成本瓶颈。本文则针对固定拓扑场景，通过bandit框架和坐标上升法直接应对样本效率与搜索空间组合爆炸的挑战。

在**样本高效优化技术**方面，上下文bandit方法（如LinUCB）提供了样本效率高的解决方案，但现有算法通常是“结构盲”的，将搜索空间视为独立向量，忽略了多智能体系统中的拓扑先验。尽管图神经网络已在组合优化中展现出强大的结构建模能力，但如何将其与bandit方法结合以导航固定拓扑多智能体系统的结构化搜索空间仍是空白。本文的MASPOB正是填补了这一空白，通过集成图神经网络来捕获结构先验，并利用上置信界平衡探索与利用，从而在严格有限的评估预算内实现高效优化。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MASPOB的样本高效框架来解决多智能体系统（MAS）提示优化中的三大挑战。其核心方法结合了上下文老虎机、图神经网络和坐标上升法，旨在以有限的评估预算高效地搜索最优提示组合。

整体框架包含三个关键组件。首先，为了处理拓扑结构引发的提示间耦合问题，论文设计了一个基于图注意力网络（GAT）的拓扑感知代理模型。该模型将每个智能体的提示通过预训练文本编码器嵌入为节点特征，并将MAS工作流依赖关系编码为邻接矩阵。GAT通过注意力机制进行消息传递，学习节点（即智能体）间的非对称影响，最终通过图级表示和MLP预测整个系统的性能。这使模型能够捕获由工作流拓扑结构决定的智能体间交互，从而提供更准确的性能预测。

其次，为了在昂贵的评估成本下实现样本效率，论文将提示搜索建模为上下文老虎机问题，并采用线性上置信界（LinUCB）算法来平衡探索与利用。具体而言，算法为每个候选提示组合计算一个UCB得分，该得分由GAT预测的性能（利用信号）和一个不确定性奖励项组成。不确定性通过维护一个信息矩阵来量化，该矩阵累积已评估组合的嵌入信息，对新颖或未充分探索的组合赋予更高的探索价值。这种机制确保了在严格有限的评估预算内最大化收益。

最后，为了应对搜索空间的组合爆炸，论文采用坐标上升法将联合优化问题分解为一系列单智能体子问题。算法从当前最佳组合出发，依次优化每个智能体的提示，同时固定其他智能体的提示。这种方法将每次迭代的搜索复杂度从指数级（与智能体数量成乘积关系）降低到线性级（与智能体数量成求和关系），使得在组合空间中的高效导航成为可能。

创新点主要体现在三者的有机结合：利用GNN编码结构先验以处理耦合，利用老虎机框架实现样本高效的探索-利用权衡，并利用坐标上升法将组合优化分解以应对维度灾难。整个流程迭代进行，在每次评估后更新信息矩阵并重新训练GAT模型，逐步逼近最优提示组合。

### Q4: 论文做了哪些实验？

论文在六个广泛使用的公开基准测试上进行了实验，包括HotpotQA、DROP、HumanEval、MBPP、GSM8K和MATH，涵盖了问答、代码生成和数学推理任务。实验设置上，使用Qwen3-Embedding-8B作为文本嵌入模型，GPT-4o-mini作为骨干LLM执行代理任务。为确保公平，所有提示优化方法均被赋予相同的50次验证预算来选择最佳提示组合，随后在测试集上评估三次并报告平均准确率。

对比方法分为三类：无需提示优化的单代理方法（IO、CoT、ReAct）、单代理提示优化方法（PromptBreeder、Instinct）以及多代理系统方法（AFlow和MIPRO）。主要结果显示，MASPOB在所有基准测试上均取得了最佳性能，平均准确率达到80.58%。具体关键指标上，在HotpotQA、DROP、HumanEval、MBPP、GSM8K和MATH上的准确率分别为75.43%、82.28%、94.15%、80.65%、93.90%和57.05%。与基线方法相比，MASPOB的平均准确率比IO、AFlow和MIPRO分别提升了12.02%、2.06%和1.71%。

此外，论文还进行了消融实验，将GNN替换为MLP后平均准确率下降了2.31%，验证了GNN在捕捉拓扑结构先验中的关键作用。在更复杂的多代理结构上的实验表明，MASPOB仍保持最佳性能（平均82.02%），证明了其鲁棒性。收敛性分析显示，MASPOB在约35轮评估后即可在测试集上达到稳定性能，体现了其样本高效性。最后，在更换骨干模型为Qwen-3-32B的实验中，MASPOB同样取得了最优的平均结果（83.43%），展示了良好的泛化能力。

### Q5: 有什么可以进一步探索的点？

该论文在基于多智能体系统的提示优化方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，MASPOB 假设工作流拓扑固定，但实际应用中智能体间的交互结构可能动态变化，未来可研究自适应拓扑的提示优化方法。其次，当前方法主要关注准确率等单一指标，而多智能体系统常需权衡效率、鲁棒性、可解释性等多目标，可引入多目标优化框架。此外，GNN 对拓扑先验的编码依赖人工设计的提示语义表示，未来可探索端到端的联合学习，使语义表示与优化过程更紧密耦合。从计算效率看，坐标上升法虽降低搜索复杂度，但可能陷入局部最优，结合元启发式算法或贝叶斯优化可能进一步提升全局搜索能力。最后，实验集中于模拟环境，未来需在真实复杂场景（如长期部署、人类反馈集成）中验证方法的泛化性和稳定性。

### Q6: 总结一下论文的主要内容

该论文针对基于大语言模型的多智能体系统（MAS）提出了一种高效的提示优化框架MASPOB。核心问题是：在无法修改预设工作流拓扑、且端到端评估成本高昂的约束下，如何通过优化各智能体的输入提示来提升整体系统性能。主要挑战包括样本效率要求高、拓扑结构导致的提示间耦合以及搜索空间组合爆炸。

MASPOB的创新方法结合了多臂老虎机、图神经网络和坐标上升算法。它利用LinUCB风格的老虎机框架平衡探索与利用，以有限评估预算最大化收益；通过图神经网络编码工作流拓扑，学习提示语义的结构化表示以处理耦合效应；并采用坐标上升将组合优化问题分解为线性复杂度的单变量子问题。

实验表明，在多个基准任务上，MASPOB在相同评估预算下均优于现有基线。其主要结论是：在不改变工作流设计的前提下，显式编码拓扑结构并进行不确定性感知的探索能显著提升多智能体系统的提示优化效果。该框架为实际部署提供了高效、可复现的优化基础，突出了在有限预算下利用工作流结构的重要性。
