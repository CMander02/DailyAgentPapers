---
title: "MARS$^2$: Scaling Multi-Agent Tree Search via Reinforcement Learning for Code Generation"
authors:
  - "Pengfei Li"
  - "Shijie Wang"
  - "Fangyuan Li"
  - "Yikun Fu"
  - "Kaifeng Liu"
  - "Kaiyan Zhang"
  - "Dazhi Zhang"
  - "Yuqiang Li"
  - "Biqing Qi"
  - "Bowen Zhou"
date: "2026-04-16"
arxiv_id: "2604.14564"
arxiv_url: "https://arxiv.org/abs/2604.14564"
pdf_url: "https://arxiv.org/pdf/2604.14564v1"
github_url: "https://github.com/TsinghuaC3I/MARTI"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Multi-Agent"
  - "Reinforcement Learning"
  - "Tree Search"
  - "Code Generation"
  - "Collaboration"
  - "Search Enhancement"
relevance_score: 8.0
---

# MARS$^2$: Scaling Multi-Agent Tree Search via Reinforcement Learning for Code Generation

## 原始摘要

Reinforcement learning (RL) paradigms have demonstrated strong performance on reasoning-intensive tasks such as code generation. However, limited trajectory diversity often leads to diminishing returns, which constrains the achievable performance ceiling. Search-enhanced RL alleviates this issue by introducing structured exploration, which remains constrained by the single-agent policy priors. Meanwhile, leveraging multiple interacting policies can acquire more diverse exploratory signals, but existing approaches are typically decoupled from structured search. We propose \textbf{MARS$^2$} (Multi-Agent Reinforced Tree-Search Scaling), a unified RL framework in which multiple independently-optimized agents collaborate within a shared tree-structured search environment. MARS$^2$ models the search tree as a learnable multi-agent interaction environment, enabling heterogeneous agents to collaboratively generate and refine candidate solutions within a shared search topology. To support effective learning, we introduce a path-level group advantage formulation based on tree-consistent reward shaping, which facilitates effective credit assignment across complex search trajectories. Experiments on code generation benchmarks show that MARS$^2$ consistently improves performance across diverse model combinations and training settings, demonstrating the effectiveness of coupling multi-agent collaboration with tree search for enhancing reinforcement learning. Our code is publicly available at https://github.com/TsinghuaC3I/MARTI.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决强化学习（RL）在代码生成等推理密集型任务中，由于探索受限导致的性能瓶颈问题。研究背景是，以GRPO为代表的RL方法通过基于结果反馈直接优化策略，在单样本评估下显著提升了响应质量，但其改进仍受限于单智能体的探索行为。在独立同分布采样假设下，有效探索空间隐式地受限于模型自身的先验分布，导致轨迹多样性不足、过早收敛于局部最优，从而形成难以突破的性能天花板。

现有方法存在两大不足。首先，搜索增强的RL（如TreeRL）通过引入蒙特卡洛树搜索等结构化探索机制来缓解探索瓶颈，但整个搜索树仍由单一策略分布驱动，搜索动态根本上受限于共享先验。随着训练进行，搜索行为越来越集中于少数高概率分支，难以持续扩展探索前沿，导致搜索收益递减（挑战一：单一策略先验下探索收益递减）。其次，多智能体强化学习（MARL）被视为克服单策略探索局限的有前途途径，但现有的多智能体推理框架（如MAPoRL）主要依赖多轮对话、辩论或投票等简单交互范式，将智能体协作视为轻量级协调机制，而非结构化探索过程。这导致多智能体协作与底层搜索动态基本脱节，缺乏对分支、回溯或探索资源分配的原生支持，限制了其在深度、多分支推理任务中的应用（挑战二：多智能体协作中缺乏结构化搜索集成）。

本文要解决的核心问题是：如何将多智能体协作与结构化树搜索有效结合，以克服单策略探索瓶颈，并实现更高效、稳定的强化学习训练。为此，论文提出了MARS²框架，将多个独立优化的智能体置于共享的树结构搜索环境中进行协作，把搜索树建模为可学习的多智能体交互环境，并通过基于路径的组优势函数和树一致奖励塑形实现有效的信用分配，从而提升探索多样性和训练稳定性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于强化学习的代码生成、搜索增强的强化学习，以及多智能体协作推理。

在**基于强化学习的代码生成**方面，以GRPO（Group Relative Policy Optimization）为代表的方法通过结果级反馈直接优化策略，在单样本评估下提升了响应质量。然而，这类方法受限于单一智能体的探索行为，轨迹多样性不足，容易陷入局部最优。MARS² 同样采用强化学习范式，但通过引入多智能体与树搜索来突破单一策略先验的探索瓶颈。

在**搜索增强的强化学习**方面，如TreeRL等方法将蒙特卡洛树搜索（MCTS）集成到训练中，通过结构化探索增加候选解的多样性。但现有方法通常由单一策略驱动整个搜索树，搜索行为仍受限于该策略的先验，随着训练进行，探索收益容易递减。MARS² 的核心创新在于将搜索树构建为一个**可学习的多智能体交互环境**，允许多个异构智能体在共享的树形拓扑中协作生成和优化候选解，从而将结构化搜索与多智能体协作深度融合，超越了单一策略搜索的局限。

在**多智能体协作推理**方面，如MAPoRL等工作展示了在训练中引入多智能体交互能带来比仅在推理时使用多智能体协议更稳定的性能提升。然而，现有框架多依赖于对话、辩论或投票等简单交互范式，将智能体协作视为轻量级的协调机制，**缺乏与底层搜索动态的结构化整合**，无法有效支持分支、回溯或探索资源的分配。MARS² 则明确地将多智能体协作置于结构化树搜索环境中，并设计了基于路径的组优势函数与树一致的奖励塑形机制，以实现复杂搜索轨迹上的有效信用分配，解决了多智能体协作与结构化搜索脱节的问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MARS²的统一强化学习框架来解决代码生成任务中因轨迹多样性有限而导致的性能瓶颈问题。该框架的核心思想是将多智能体协作与树形搜索结构相结合，将搜索树本身建模为一个可学习的多智能体交互环境。

在整体架构设计上，MARS²让多个独立优化的智能体在一个共享的树形搜索环境中协作。每个智能体拥有自己的策略，它们共同扩展一棵共享的搜索树，树中的每个节点代表一个候选解决方案。框架的关键机制包括：1）**智能体-节点选择**：将每一步的扩展建模为一个多臂老虎机问题，通过维护Beta先验分布并使用Thompson采样，依次选择最有潜力的智能体及其关联的可扩展节点。2）**动态扩展策略**：定义了两种节点类型——生成节点和精炼节点。选择生成节点会进行“水平扩展”，即由智能体生成全新的候选解；选择精炼节点则进行“垂直精炼”，即在现有路径上选择子节点进行改进。这实现了在利用高质量轨迹和探索多样性之间的动态平衡。

其核心创新点在于引入了**基于树结构一致性的奖励塑形机制**，以解决多智能体在结构化搜索中的信用分配难题。传统的组相对优势（Group-Relative Advantage）在树搜索中无法捕捉节点间的层次依赖关系。为此，论文为每个非根节点v设计了一个混合基线b(v)，它综合了父节点奖励和兄弟节点平均奖励。通过计算节点奖励与该基线的差值得到“结构一致性增益”，并将其以可控强度叠加到原始奖励上，形成塑形后的奖励。这一机制明确鼓励了两种行为：子节点对父节点的改进（垂直提升），以及同一父节点下子节点间的竞争（横向择优），从而促进了智能体在共享树中的有效协作与专业化。

最终，训练目标建立在GRPO（Group Relative Policy Optimization）框架之上，但将优化单元从平行的轨迹扩展到树中的所有节点。每个智能体使用其在树中生成节点所收集的、经过上述塑形的奖励进行独立优化。优势估计器则结合了树级别的组相对优势和奖励塑形结果，确保了训练信号既能反映全局表现，又能体现层次化的协作关系。

### Q4: 论文做了哪些实验？

实验在代码生成任务上验证了MARS²框架的有效性。实验设置方面，使用DeepCoder发布的开源代码生成数据集作为强化学习训练数据，经过筛选后得到7,992个提示。模型方面，采用了8B和14B参数规模的开源大语言模型，包括代码专用模型AReaL-boba-2 8B/14B、DeepCoder-14B-Preview以及通用模型Qwen3 8B/14B，以评估方法的通用性。对比方法包括单智能体强化学习基线Vanilla GRPO以及单智能体树搜索方法RS²。所有方法在训练样本数和优化步数上保持一致，并在推理时统一采用基于MCTS的框架，固定搜索预算为60个节点。

评估基准为LiveCodeBench (v6)，使用三个互补指标：Pass@1（单次采样正确率）、Pass@1(MCTS)（基于MCTS搜索选择最优解的正确率）以及Pass@N（N个解中至少一个正确的概率）。主要结果显示，MARS²在不同模型组合和训练设置下均能持续提升性能。例如，在单模型能力上，Qwen3-8B使用MARS² (Q+A)训练后，Pass@1达到58.3%，相比基线（50.3%）绝对提升8.0%，也优于GRPO（52.5%）和RS²（55.4%）。在系统层面，由Qwen3-8B和AReaL-8B组成的异构系统使用MARS²后，Pass@1(MCTS)达到61.7%，相比基础系统（57.2%）提升4.5个百分点，且显著优于GRPO（56.0%）和RS²（57.2%）。14B规模模型也观察到类似趋势。此外，MARS²在Pass@N指标上也有一致提升，表明其在固定推理预算下能有效增强系统级协作和搜索效率。实验还通过引入性能较弱的DeepCoder-14B进行了鲁棒性分析，发现虽然个体增益有所减少，但MARS²在智能体能力不均衡的场景下仍能保持有效性。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于训练效率。多智能体在树结构中顺序交互，降低了并行性，增加了训练时间，这源于树结构顺序扩展的本质，而非计算或数据量的增加。虽然这种结构对于实现协调探索和结构化推理至关重要，但如何在保持其优势的同时提升效率，是未来研究的关键方向。

未来可进一步探索的点包括：1）**高效搜索机制**：研究异步或并行的树扩展策略，例如允许智能体在部分完成的子树中同时进行探索，或设计轻量级的树结构表示以减少通信开销。2）**智能体协作模式的优化**：当前框架中智能体独立优化但协同工作，未来可探索动态角色分配或分层协作机制，使智能体能根据任务阶段自适应调整策略，进一步提升探索多样性与推理深度。3）**奖励塑形与信用分配的深化**：论文提出了基于路径的组优势函数，但可进一步结合课程学习或逆强化学习，更精细地引导多智能体在复杂搜索轨迹中的协作，尤其是在解决更长序列或更模糊的代码生成任务时。4）**扩展到更广泛领域**：将MARS²框架应用于数学推理、规划或创意生成等需要结构化探索的任务，验证其通用性，并可能催生新的多智能体搜索理论。

### Q6: 总结一下论文的主要内容

该论文提出了MARS²框架，旨在通过多智能体协作增强强化学习在代码生成等推理任务中的性能。核心问题是传统强化学习在搜索过程中因轨迹多样性有限而遇到性能瓶颈，而现有方法未能有效结合多智能体交互与结构化树搜索。MARS²将搜索树建模为可学习的多智能体环境，使多个独立优化的异质智能体在共享树结构中协同生成和优化候选解。方法上引入了基于树一致奖励塑造的路径级群体优势计算，以在复杂搜索轨迹中实现有效的信用分配。实验表明，该框架在不同模型组合与训练设置下均能提升性能，验证了多智能体协作与树搜索结合对增强强化学习推理能力的有效性，为扩展推理系统提供了可扩展且稳健的新方向。
