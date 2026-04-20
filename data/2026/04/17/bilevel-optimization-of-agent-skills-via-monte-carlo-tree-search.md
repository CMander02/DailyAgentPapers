---
title: "Bilevel Optimization of Agent Skills via Monte Carlo Tree Search"
authors:
  - "Chenyi Huang"
  - "Haoting Zhang"
  - "Jingxu Xu"
  - "Zeyu Zheng"
  - "Yunduan Lin"
date: "2026-04-17"
arxiv_id: "2604.15709"
arxiv_url: "https://arxiv.org/abs/2604.15709"
pdf_url: "https://arxiv.org/pdf/2604.15709v1"
categories:
  - "cs.AI"
tags:
  - "Agent Skill Optimization"
  - "Bilevel Optimization"
  - "Monte Carlo Tree Search"
  - "Tool Use"
  - "Instruction Tuning"
  - "Operations Research"
relevance_score: 8.5
---

# Bilevel Optimization of Agent Skills via Monte Carlo Tree Search

## 原始摘要

Agent \texttt{skills} are structured collections of instructions, tools, and supporting resources that help large language model (LLM) agents perform particular classes of tasks. Empirical evidence shows that the design of \texttt{skills} can materially affect agent task performance, yet systematically optimizing \texttt{skills} remains challenging. Since a \texttt{skill} comprises instructions, tools, and supporting resources in a structured way, optimizing it requires jointly determining both the structure of these components and the content each component contains. This gives rise to a complex decision space with strong interdependence across structure and components. We therefore represent these two coupled decisions as \texttt{skill} structure and component content, and formulate \texttt{skill} optimization as a bilevel optimization problem. We propose a bilevel optimization framework in which an outer loop employs Monte Carlo Tree Search to determine the \texttt{skill} structure, while an inner loop refines the component content within the structure selected by the outer loop. In both loops, we employ LLMs to assist the optimization procedure. We evaluate the proposed framework on an open-source Operations Research Question Answering dataset, and the experimental results suggest that the bilevel optimization framework improves the performance of the agents with the optimized \texttt{skill}.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在执行复杂任务时，其核心组件“技能”（skills）的系统化优化难题。研究背景是，随着LLM智能体在代码生成、数据分析等领域的广泛应用，通过结构化文件夹（包含指令、工具和资源）组织的“技能”已成为实现任务专业化的关键。现有方法主要依赖人工设计或经验性调整，但实证表明技能设计对任务性能影响显著且差异巨大，而当前缺乏系统化的优化策略。现有方法的不足在于：技能具有高度异质性（混合了指令、脚本、文档等多种组件），组件间存在强相互依赖，且优化空间是离散、组合式的，受模式要求、令牌预算等约束，这使得优化问题不仅求解困难，甚至难以被形式化为一个结构良好的优化问题。

因此，本文要解决的核心问题是：如何将技能优化这一复杂决策过程（涉及组件结构配置与具体内容生成）形式化并有效求解。论文将技能表示为结构（θ）与内容（φ）的元组，并将其建模为一个双层优化问题：外层通过蒙特卡洛树搜索（MCTS）在离散、序列化的结构空间中进行探索，利用延迟评估反馈引导搜索；内层则在给定结构下，利用LLM辅助对内容进行迭代精化。这一框架将结构搜索与内容优化解耦，明确了优化过程中的反馈归属，从而系统化地提升智能体在特定任务上的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**基于树搜索的LLM智能体方法**和**智能体技能（agent skills）的相关工作**。

在**树搜索方法**方面，一系列研究利用树状结构提升LLM推理与决策能力。例如，Tree of Thoughts通过探索多步推理路径进行前瞻与回溯；Reasoning via Planning将LLM作为世界模型和推理智能体融入MCTS框架；Language Agent Tree Search则首次通过MCTS统一了推理、行动与规划。在数学推理领域，MCTSr和rStar-Math也成功应用了MCTS。与本文最相关的是AFlow，它将智能体工作流优化视为对代码化工作流的搜索问题，并使用MCTS进行迭代优化。本文与AFlow的**关键区别**在于：1) 本文优化的是包含指令、工具、资源等异质组件的**技能包**，而非单一的代码化工作流；2) 本文采用**双层优化**框架，显式分离结构搜索与内容优化，而AFlow是单层表示；3) 本文内层循环采用基于动作族的细化策略与保守选择规则，而非统一的代码修改过程。

在**智能体技能**方面，相关研究可分为两个方向。一是**提升智能体能力**的可重用模块研究，如Voyager在Minecraft中构建可自动生成与验证的技能库；Reflexion通过语言自我反思进行强化学习；SAGE利用强化学习让智能体自主构建与优化技能库。这些工作奠定了通过优化可重用模块（而非底层模型）来提升智能体性能的原则。二是将技能视为**可移植的系统组件**，关注其规范、编排与评估。例如，Anthropic提出了以SKILL.md文件为中心的结构化技能规范；AgentSkillOS设计了类操作系统框架来组织与编排技能；SkillsBench则提供了评估技能泛化能力的大规模基准。本文与这些工作的**关系**在于，它直接针对“技能”这一核心构件进行系统优化，旨在解决技能设计中结构与内容相互依赖的联合优化难题，而现有工作尚未直接涉及对此类结构化技能包的优化问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个双层优化框架来解决智能体技能优化问题，该框架将技能优化建模为一个结构（组件组织方式）与内容（组件具体实例）相互耦合的决策问题。核心方法是将外层循环设计为基于蒙特卡洛树搜索（MCTS）的结构搜索，内层循环则对给定结构下的内容进行细化优化，两者均利用大语言模型（LLM）辅助决策。

整体框架包含一个一次性的理解阶段和后续的双层优化循环。理解阶段将原始种子技能转换为优化就绪的初始化表示，包括提取初始结构θ₀、对齐内容φ₀，并构建技能档案P以指导搜索空间。随后，双层优化开始：外层循环在离散组合的结构空间Θ中进行搜索，内层循环则在固定结构下优化内容空间Φ(θ)。

主要模块包括：1）**MCTS外层循环**：将结构搜索建模为树状序列决策过程。每个节点存储结构θ、对齐内容φ及搜索统计量（访问次数、价值估计）。其行动空间A由可行的结构编辑操作（如增删、重组组件）构成。循环遵循选择、扩展、评估、回溯四步骤：选择阶段采用UCB或混合概率策略选取父节点；扩展阶段通过LLM引导的三阶段推理（分析、诊断、提议）生成新结构候选；评估前会进行结构验证，确保候选满足格式与令牌预算约束；通过验证的候选送入内层循环进行内容细化与下游任务评估，获得奖励R；最后奖励沿路径回溯更新节点统计。2）**内层循环**：负责在固定结构下优化内容。首先通过“桥接”操作将现有内容对齐到新结构，得到初始内容φ₀(θ')。随后根据结构编辑类型，将细化任务分派到不同的“细化族”（如元数据更新、指令文本修订、脚本编辑等），每个族由LLM驱动进行有限次的内容优化尝试。最终对细化结果进行悲观评估，选择最优内容返回外层循环。

创新点主要体现在：1）**双层优化建模**：将技能优化分解为结构决策与内容决策两个层次，外层比较结构，内层评估各结构下可达到的最佳内容，从而处理两者间的强耦合关系。2）**LLM引导的MCTS**：在MCTS的扩展阶段集成LLM进行状态分析、诊断与行动提议，提升搜索效率；同时内层循环利用LLM执行内容细化。3）**技能档案引导的搜索**：通过技能档案P定义搜索先验，缩小结构搜索空间并提供任务对齐的上下文，使搜索更聚焦。4）**细化族机制**：根据结构编辑类型动态选择内容优化策略，实现针对性细化。该框架在实验中被验证能有效提升智能体在任务中的性能。

### Q4: 论文做了哪些实验？

论文在Operations Research Question Answering (ORQA) 数据集上进行了实验，这是一个包含1,513个实例的多选题问答基准，涉及20个应用领域。实验设置采用双层优化框架：外层使用蒙特卡洛树搜索（MCTS）优化技能结构，内层使用LLM细化组件内容。实验将数据集划分为搜索集（用于优化评估）、确认集（用于模型选择）和测试集（用于最终评估），并采样了120个问题以控制成本。对比方法包括两种MCTS配置：配置A（保守，3轮搜索，确定性UCB1选择）和配置B（探索性，6轮搜索，混合概率选择）。主要结果显示，优化后的技能性能显著提升。在测试集上，初始种子技能的精确匹配分数为0.90625，而配置B产生的优化技能分数达到0.9375，提升了0.03125。关键数据指标包括：搜索集峰值奖励为0.9434（两者相同），确认集平均分数配置A为0.8571，配置B为0.8857（后者胜出）。结构上，优化技能将关键问题类型指导从参考文件移至主SKILL.md文件，并增加了专用检查清单；内容上，优化技能提供了更明确的步骤和约束，减少了模糊性。

### Q5: 有什么可以进一步探索的点？

该论文提出的双层优化框架虽在技能优化上取得进展，但仍存在若干局限与可拓展方向。首先，其评估仅基于单一领域（运筹学问答）数据集，缺乏跨任务、跨领域的泛化性验证，未来需在更复杂、多样的现实场景中测试。其次，框架依赖蒙特卡洛树搜索（MCTS）进行结构搜索，计算成本较高，且可能陷入局部最优；可探索更高效的搜索策略（如基于梯度的神经架构搜索）或引入元学习加速优化过程。此外，内外层循环均使用LLM，但未深入探讨不同模型规模或提示工程对优化效果的影响，未来可研究更精细的LLM协同机制与知识蒸馏技术。从方法论看，当前技能组件内容的优化较为孤立，未能显式建模技能间的迁移与组合关系，可引入图神经网络或因果推理来学习技能间的依赖，实现动态技能库的构建与复用。最后，该工作未考虑多智能体协作场景中技能的分布式优化问题，这为未来研究提供了重要拓展空间。

### Q6: 总结一下论文的主要内容

该论文针对LLM智能体技能优化问题，提出了一种双层优化框架。技能包含指令、工具和资源的结构化组合，其设计直接影响任务表现，但优化过程面临结构与内容相互依赖的复杂决策挑战。为此，作者将技能优化形式化为双层优化问题：外层通过蒙特卡洛树搜索确定技能结构，内层则在给定结构下优化各组件内容。两个层级均利用LLM辅助搜索与生成。实验在开源运筹学问答数据集上进行，结果表明该框架能有效提升智能体在任务中的性能。核心贡献在于将技能优化建模为结构-内容协同的双层决策问题，并融合蒙特卡洛树搜索与LLM能力，为系统化改进智能体技能提供了新方法。
