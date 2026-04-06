---
title: "Aligning Progress and Feasibility: A Neuro-Symbolic Dual Memory Framework for Long-Horizon LLM Agents"
authors:
  - "Bin Wen"
  - "Ruoxuan Zhang"
  - "Yang Chen"
  - "Hongxia Xie"
  - "Lan-Zhe Guo"
date: "2026-04-03"
arxiv_id: "2604.02734"
arxiv_url: "https://arxiv.org/abs/2604.02734"
pdf_url: "https://arxiv.org/pdf/2604.02734v1"
categories:
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Long-Horizon Planning"
  - "Neuro-Symbolic"
  - "Memory"
  - "Tool Use"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# Aligning Progress and Feasibility: A Neuro-Symbolic Dual Memory Framework for Long-Horizon LLM Agents

## 原始摘要

Large language models (LLMs) have demonstrated strong potential in long-horizon decision-making tasks, such as embodied manipulation and web interaction. However, agents frequently struggle with endless trial-and-error loops or deviate from the main objective in complex environments. We attribute these failures to two fundamental errors: global Progress Drift and local Feasibility Violation. Existing methods typically attempt to address both issues simultaneously using a single paradigm. However, these two challenges are fundamentally distinct: the former relies on fuzzy semantic planning, while the latter demands strict logical constraints and state validation. The inherent limitations of such a single-paradigm approach pose a fundamental challenge for existing models in handling long-horizon tasks. Motivated by this insight, we propose a Neuro-Symbolic Dual Memory Framework that explicitly decouples semantic progress guidance from logical feasibility verification. Specifically, during the inference phase, the framework invokes both memory mechanisms synchronously: on one hand, a neural-network-based Progress Memory extracts semantic blueprints from successful trajectories to guide global task advancement; on the other hand, a symbolic-logic-based Feasibility Memory utilizes executable Python verification functions synthesized from failed transitions to perform strict logical validation. Experiments demonstrate that this method significantly outperforms existing competitive baselines on ALFWorld, WebShop, and TextCraft, while drastically reducing the invalid action rate and average trajectory length.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）作为智能体在执行长视野决策任务时，经常陷入无效试错循环或偏离主要目标的核心问题。研究背景是，尽管LLM在具身操作和网络交互等长视野任务中展现出潜力，但在复杂环境中，智能体表现仍不稳定。现有方法通常试图用一个统一的范式（如单一的经验表示或框架）同时处理全局任务进展和局部动作可行性这两个挑战，但这存在根本性不足。因为这两个问题本质不同：全局进展对齐依赖于模糊的语义规划和从成功经验中泛化，而局部可行性对齐则要求严格的环境逻辑约束和状态验证。将二者强行耦合在单一范式中，往往导致神经网络在处理硬约束时产生“幻觉”，或使符号规则缺乏处理复杂语义的灵活性。

因此，本文要解决的核心问题是：如何明确地解耦语义进展引导与逻辑可行性验证，以协同应对长视野任务中交织的“全局进展漂移”和“局部可行性违反”这两个根本性错误。论文提出了一种神经-符号双记忆框架，旨在通过专门化的架构分别匹配这两种不同的推理需求，从而打破智能体在复杂环境中的失败循环，实现更稳定、高效的任务执行。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**LLM智能体**和**神经符号智能体**。

在**LLM智能体**方面，现有研究通常通过层次分解、检索增强、状态跟踪、工作流记忆和基于经验的自改进等技术，来提升智能体在长视野任务中的鲁棒性。这些方法的核心范式是在一个共享的语义记忆空间内，通过提示、检索或文本反思来复用轨迹、反思、阶段线索和纠正启发式规则。虽然这类方法在高层级的进度引导上有效，但其本质仍依赖于模糊的神经泛化能力，难以可靠地处理需要严格逻辑边界的局部可行性验证问题。本文提出的框架与这类工作的区别在于，它明确地将语义进度引导与逻辑可行性验证解耦，避免了用单一模糊范式处理两类本质不同的问题。

在**神经符号智能体**方面，相关研究（如SayCan、SayPlan、Re^2 Agent和WALL-E 2.0）旨在通过结合显式约束、结构化世界知识或神经符号控制机制，将决策过程“锚定”在可执行的基础上，以减少无效动作并确保行为可行性。这类方法通过故障抽象、动作规则和结构化场景表征来增强 grounding。然而，其控制逻辑往往受限于相对刚性的规则框架，在处理复杂多变的长视野任务时缺乏灵活性。本文框架与这类工作的关系在于，它同样重视符号逻辑验证以确保局部可行性；但区别在于，它并未用刚性规则完全约束全局规划，而是让神经记忆专门负责灵活的全局任务推进，从而在确保可行性的同时保持了处理复杂任务的灵活性。

### Q3: 论文如何解决这个问题？

论文通过提出一种神经-符号双记忆框架来解决长视野任务中智能体面临的全局进度漂移和局部可行性违规这两个根本性错误。其核心思想是将模糊的语义规划与严格的逻辑验证进行显式解耦，分别由两个独立的记忆模块负责。

整体框架分为离线构建和在线推理两个阶段。在离线阶段，系统通过基础智能体（采用ReAct策略）在训练任务上进行探索，收集轨迹数据。随后，系统从失败的交互中归纳出可执行的符号化验证规则，构建**符号可行性记忆**；同时，从成功的轨迹中提炼出以阶段为锚点的程序蓝图，构建**神经进度记忆**。

主要模块与关键技术包括：
1.  **符号可行性记忆**：该模块旨在防止局部可行性违规。其构建过程是：从所有失败的状态转移中，通过一个“归纳器智能体”对比正负样本，总结出导致失败的自然语言约束，并将其编译成可执行的Python验证函数。每个函数接收当前观察、重建的场景图和候选动作为输入，输出合法性判断、错误信息和修正建议。系统通过自动化验证和基于覆盖率的贪婪选择策略，筛选出一组零误拒（即不错误拦截成功交互）且能有效拦截失败案例的规则，形成最终的可行性记忆库。该模块在推理时充当严格的符号过滤器。

2.  **神经进度记忆**：该模块旨在缓解全局进度漂移。其构建过程是：从所有成功完成的轨迹中，通过一个“蒸馏器智能体”将每条轨迹沿时间维度解耦为一个严格有序的进度锚点序列，每个锚点对应任务推进中的一个关键语义节点，并同步提取出锚点对应的连续动作块。由此，成功经验被结构化为包含任务指令和一系列（进度锚点，动作块）对的形式。系统为任务指令和进度锚点分别构建了双层神经索引，支持任务级和阶段级的语义检索，从而能提供与当前阶段匹配的、更精准的演示，避免无关上下文的干扰。

3.  **双对齐推理循环**：在在线推理阶段，两个记忆模块同步调用，形成统一的决策循环。给定新任务，系统首先从进度记忆中检索相关蓝图，由“蓝图规划器智能体”生成当前任务的结构化进度锚点序列。在每个决策步，系统根据当前激活的进度锚点，从进度记忆中检索参考动作块，并由“执行器智能体”生成一个候选动作。**关键创新点在于**，此神经路径只负责生成符合进度语义的动作，而不进行硬性可行性检查。随后，符号可行性记忆介入，基于重建的场景图对候选动作进行严格的可行性验证和迭代修正，确保其符合环境逻辑约束后才执行。执行后，一个“进度监控器智能体”评估当前阶段是否完成，并决定是否推进到下一个进度锚点。

该框架的创新点在于明确地将长视野决策中的两个本质不同的挑战——依赖模糊语义泛化的全局进度引导和依赖严格逻辑验证的局部可行性约束——分配给神经和符号两种不同范式的子系统处理。这种解耦设计使得智能体既能利用神经网络的语义泛化能力保持任务推进方向，又能借助符号规则的精确性避免无效试错，从而在保持前进动力的同时确保局部行动的有效性。

### Q4: 论文做了哪些实验？

该论文在三个代表性的长视野智能体基准测试上进行了实验：ALFWorld（具身交互）、WebShop（基于网页的决策）和TextCraft（组合合成）。实验设置统一使用GPT-4o-2024-11-20作为骨干模型，温度设为0。对比方法包括ReAct、Reflexion、ADaPT、StateAct、ExpeL、WALL-E 2.0和AWM等主流长视野智能体方法，所有方法均使用相同的基础模型以确保公平性。

主要结果显示，所提出的神经符号双记忆框架在所有基准上均显著优于基线。在ALFWorld上，成功率从最佳基线AWM的88.81%提升至94.78%；在WebShop上，成功率从Reflexion的35%提升至51%，任务得分从WALL-E 2.0的0.5998提升至0.7132；在TextCraft上，成功率从ExpeL的88%提升至94%。此外，该方法还大幅降低了无效动作率（IAR）和平均轨迹长度（ATL），例如在ALFWorld上，完整模型的IAR为11.81%，ATL为14.60。

消融实验进一步验证了双记忆模块的互补性：移除可行性记忆会使IAR从11.81%升至26.33%，成功率降至85.82%；移除进度记忆则使ATL从14.60增至20.30，成功率降至90.30%。实验还表明，进度记忆的收益主要源于其结构化的阶段蓝图而非单纯的经验检索，而可行性记忆中最有效的机制是可执行的验证器规则，它在降低无效动作和维持全局进展之间取得了最佳平衡。

### Q5: 有什么可以进一步探索的点？

本文提出的神经-符号双记忆框架虽有效，但仍有局限。首先，其依赖离线轨迹数据构建记忆，在奖励稀疏或失败信号难以解释的环境中难以适用，未来可探索如何利用在线交互或弱监督信号进行记忆初始化与增量学习。其次，框架将进度与可行性解耦，但两者在动态环境中可能相互影响，未来可研究更灵活的交互机制，例如引入元控制器动态调整两者权重。此外，当前的符号验证基于预定义的Python函数，泛化能力有限，未来可结合程序合成或大语言模型本身生成更通用的约束逻辑。最后，该框架主要在模拟环境中验证，需进一步研究如何迁移到现实世界的不确定场景中，例如通过仿真到实物的迁移学习或引入不确定性建模来提升鲁棒性。

### Q6: 总结一下论文的主要内容

本文提出了一种神经符号双记忆框架，旨在解决大型语言模型（LLM）智能体在长视野决策任务（如具身操作和网页交互）中面临的挑战。核心问题是智能体容易陷入无休止的试错循环或偏离主要目标，作者将其归因于两种根本性错误：全局的“进度漂移”和局部的“可行性违反”。现有方法通常试图用单一范式同时解决这两个问题，但两者本质不同：前者依赖于模糊的语义规划，后者则要求严格的逻辑约束和状态验证。

为此，论文的核心贡献是明确地将语义进度引导与逻辑可行性验证解耦，设计了一个双记忆框架。在推理阶段，该框架同步调用两种记忆机制：一方面，基于神经网络的“进度记忆”从成功轨迹中提取语义蓝图，以指导全局任务推进；另一方面，基于符号逻辑的“可行性记忆”利用从失败转换中合成的可执行Python验证函数，执行严格的逻辑验证。

实验表明，该方法在ALFWorld、WebShop和TextCraft基准上显著优于现有基线，同时大幅降低了无效动作率和平均轨迹长度。其意义在于通过神经与符号方法的有效结合，为提升LLM智能体在复杂环境中的规划可靠性和执行效率提供了新思路。
