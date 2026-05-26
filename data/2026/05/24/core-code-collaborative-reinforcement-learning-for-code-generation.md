---
title: "CoRe-Code: Collaborative Reinforcement Learning for Code Generation"
authors:
  - "Zhihao Dou"
  - "Qinjian Zhao"
  - "Zhongwei Wan"
  - "Xiaoyu Xia"
  - "Sumon Biswas"
date: "2026-05-24"
arxiv_id: "2605.24812"
arxiv_url: "https://arxiv.org/abs/2605.24812"
pdf_url: "https://arxiv.org/pdf/2605.24812v1"
categories:
  - "cs.AI"
tags:
  - "多智能体协作"
  - "代码生成"
  - "强化学习"
  - "角色专业化"
  - "GRPO"
  - "规划-编码范式"
  - "协调对齐"
relevance_score: 9.0
---

# CoRe-Code: Collaborative Reinforcement Learning for Code Generation

## 原始摘要

Large language models (LLMs) have achieved strong performance in code generation, but most methods rely on autoregressive decoding without global planning, often leading to locally coherent yet globally suboptimal solutions (e.g., failing test cases or inefficient complexity). While recent approaches such as Chain-of-Thought (CoT) and multi-agent systems (MAS) introduce planning, their limited role specialization and coordination hinder performance on complex tasks. To address the challenges of coordination and specialization in multi-agent code generation, we propose Collaborative Reinforcement Code (CoRe-Code), a framework for role specialized LLM agents that enhances inter-agent coordination to generate more accurate and efficient code. CoRe-Code adopts a simple Planner-Coder paradigm, where the Planner produces high-level plans and the Coder executes them to generate code. We further introduce a collaboration-aware reinforcement learning stage based on Group Relative Policy Optimization (GRPO) to enhance role specialization and alignment. Experiments show that CoRe-Code outperforms a wide range of existing RL-based and multi-agent methods. In addition, we demonstrate that CoRe-Code can generalize to other multi-agent frameworks (e.g., Retrieval and Debugging agents), highlighting its flexibility and scalability. We evaluate CoRe-Code on multiple benchmarks of varying difficulty using three base models. Compared to existing baselines, the results show consistent improvements in accuracy, while also achieving higher efficiency in terms of execution time and memory usage, demonstrating the effectiveness and practicality of CoRe-Code.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在代码生成中缺乏全局规划与多智能体协作不足的问题。现有方法（如自回归解码）在生成时仅关注局部token的连贯性，常导致代码全局视角下的次优解，例如无法通过全部测试用例或算法复杂度不理想。尽管链式思维和多智能体系统引入了规划机制，但存在角色分工不明确、协作增益有限等局限性——例如辅助智能体对编码器的实际帮助常为负增益，尤其在复杂任务中表现不稳定。本文聚焦于多智能体协作中协调与专业化的双重挑战，提出CoRe-Code框架：采用“规划器-编码器”范式，由规划器负责生成高层算法思路，编码器将其转化为代码；并引入基于组相对策略优化的协作感知强化学习阶段，通过可验证的代码执行结果作为奖励，间接训练规划器生成更优规划，同时促进编码器对规划的对齐执行。实验表明该方法在精度、执行效率上显著优于现有RL与多智能体基线，且可扩展至检索、调试等更多智能体角色。

### Q2: 有哪些相关研究？

相关研究可分为三类。**方法类**工作中，CoT、检索增强提示和提示组合等方法虽引入了规划，但缺乏多智能体间的深度协调；多智能体系统如AgentConductor通过难度感知拓扑优化协作，但角色专化不足。本文提出Planner-Coder范式，并首次将GRPO引入多智能体代码生成的协作强化学习，与RECRL、SecCoderX等训练时RL方法相比，更强调角色对齐而非单纯优化单智能体奖励。**应用类**工作如ChatUniTest、CodeT利用自生成测试提升代码质量，但需额外验证步骤；本文的协作RL在训练阶段自动实现规划与执行的一致性，推理时更高效。**评测类**基准如MBPP、HumanEval主要衡量生成代码通过率，本文额外关注执行时间和内存效率，弥补了现有研究对生成代码效率评估的不足。与基线相比，CoRe-Code通过智能体角色专化和协作感知RL训练，在复杂任务上取得了更优的准确率与效率平衡。

### Q3: 论文如何解决这个问题？

CoRe-Code通过协作感知的强化学习框架解决多智能体代码生成中的协调与专业化问题。整体采用Planner-Coder双角色范式，设计"算法思维"(Algorithmic Thought)结构化规划模板，将规划输出规范化为输入输出定义、线性流程、条件逻辑和迭代循环四个编程语义组件，使规划与代码执行语义对齐。

核心创新在于提出协作式GRPO算法，分两阶段联合优化两个智能体：第一阶段冻结Coder，通过下游代码执行的可验证信号（测试用例通过率）间接评估Planner规划质量，并引入时间复杂度奖励鼓励高效规划；第二阶段冻结Planner，利用训练好的规划指导Coder生成代码，在准确性奖励基础上增加空间效率奖励（基于psutil监控内存消耗），约束实现细节。两者通过协作增益(Collaboration Gain)指标量化互增强效果，该指标衡量Coder在有无辅助条件下的通过率提升比率。

关键技术包括：使用sigmoid加权方案对多候选代码进行判别性奖励分配，避免简单平均导致的信息损失；通过执行反馈实现可验证奖励替代人工评价；采用分阶段参数更新策略，先优化规划能力再提升代码生成对齐度。实验证明该方法在多个基准和模型上实现准确率与效率的持续提升，可泛化至检索、调试等智能体框架。

### Q4: 论文做了哪些实验？

论文在三个开源基座模型（Qwen2.5-7B-Coder-Instruct、Qwen2.5-14B-Coder-Instruct 和 Qwen3-4B）上进行了实验，使用四个基准测试：LiveCode、MBPP（基础函数级任务）和 CodeContests、CodeForces（竞赛级复杂任务）。对比方法包括四种基于强化学习的基线（GRPO、Focused-DPO、CURE、CodeRL+）和三种多智能体方法（SCoT、Reflexion、MapCoder）。主要评估指标为代码生成的 Pass@1、Pass@5 和平均通过率（APR），同时在附录中考察了效率（运行时间、内存占用）和可维护性（圈复杂度、失败率）。

主要结果显示，CoRe-Code 在所有基准测试上均一致优于所有基线。例如，在 Qwen2.5-14B-Coder-Instruct 模型上，CoRe-Code 在 LiveBench 上达到 Pass@1 48.4%（对比 GRPO 的 45.5%），在 CodeForces 上达到 APR 22.4%（对比 CodeRL+ 的 21.7%）。消融实验表明，联合优化 Planner 和 Coder 两个智能体（完整 CoRe-Code）相比移除任一智能体 RL 组件均带来显著提升（如 MBPP 上 APR 从 77.8% 升至 83.7%）。扩展实验证明 CoRe-Code 可迁移至 MapCoder 框架，独立强化检索智能体或调试智能体均带来性能提升（例如调试智能体在 CodeForces 上 APR 达 14.2%，优于原始 MapCoder 的 13.7%）。此外，超参数敏感度分析显示增加 GRPO 的 rollout 数量（从 2 到 4）能进一步提升所有基准的 Pass@1。

### Q5: 有什么可以进一步探索的点？

论文在Planner和Coder的协作上取得了显著进展，但仍存在几个值得深入探索的方向。首先，当前框架的规划粒度较为固定，未来可以探索动态调整规划层级，如根据任务复杂度自适应地生成更细或更粗的计划，以提高灵活性。其次，Planner生成计划后，Coder的执行缺乏对计划质量的反向反馈机制，引入迭代优化循环或基于执行结果的稀疏奖励来调优规划策略将提升鲁棒性。此外，GRPO虽能增强角色对齐，但多智能体间的信用分配问题尚未充分解决，可借鉴价值分解或反事实推理方法实现更精确的协同强化。最后，将框架扩展到更多异构角色（如结合检索、调试或测试生成智能体）时，如何平衡角色分工与通信开销也是重要的研究方向，例如设计层次化协调或门控通信机制来提升可扩展性。

### Q6: 总结一下论文的主要内容

这篇论文提出CoRe-Code，一个基于协作强化学习的代码生成框架，旨在解决现有方法因缺乏全局规划或角色协调不足而导致生成代码局部合理但全局次优的问题。核心贡献在于采用“规划器-编码器”双智能体架构：规划器生成高层计划，编码器执行计划生成代码，并引入基于组相对策略优化的协作感知强化学习阶段，以增强角色专门化和智能体间的对齐。通过在多个不同难度的基准测试上使用三种基础模型进行评估，实验结果表明，CoRe-Code在准确率上持续优于现有基于强化学习和多智能体的方法，同时在执行时间和内存使用方面亦展现出更高的效率。该研究不仅验证了其有效性和实用性，还证明了框架可泛化至其他多智能体系统（如检索、调试智能体），突出了其在复杂代码生成任务中的灵活性和可扩展性，对推动智能体协作与自动化编程具有重要意义。
