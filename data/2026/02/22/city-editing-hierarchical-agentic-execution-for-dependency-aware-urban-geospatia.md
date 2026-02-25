---
title: "City Editing: Hierarchical Agentic Execution for Dependency-Aware Urban Geospatial Modification"
authors:
  - "Rui Liu"
  - "Steven Jige Quan"
  - "Zhong-Ren Peng"
  - "Zijun Yao"
  - "Han Wang"
  - "Zhengzhang Chen"
  - "Kunpeng Liu"
  - "Yanjie Fu"
  - "Dongjie Wang"
date: "2026-02-22"
arxiv_id: "2602.19326"
arxiv_url: "https://arxiv.org/abs/2602.19326"
pdf_url: "https://arxiv.org/pdf/2602.19326v1"
categories:
  - "cs.MA"
  - "cs.AI"
tags:
  - "Agent 架构"
  - "多智能体系统"
  - "分层规划"
  - "工具使用"
  - "多模态推理"
  - "迭代执行"
  - "空间约束传播"
  - "城市计算"
relevance_score: 9.0
---

# City Editing: Hierarchical Agentic Execution for Dependency-Aware Urban Geospatial Modification

## 原始摘要

As cities evolve over time, challenges such as traffic congestion and functional imbalance increasingly necessitate urban renewal through efficient modification of existing plans, rather than complete re-planning. In practice, even minor urban changes require substantial manual effort to redraw geospatial layouts, slowing the iterative planning and decision-making procedure. Motivated by recent advances in agentic systems and multimodal reasoning, we formulate urban renewal as a machine-executable task that iteratively modifies existing urban plans represented in structured geospatial formats. More specifically, we represent urban layouts using GeoJSON and decompose natural-language editing instructions into hierarchical geometric intents spanning polygon-, line-, and point-level operations. To coordinate interdependent edits across spatial elements and abstraction levels, we propose a hierarchical agentic framework that jointly performs multi-level planning and execution with explicit propagation of intermediate spatial constraints. We further introduce an iterative execution-validation mechanism that mitigates error accumulation and enforces global spatial consistency during multi-step editing. Extensive experiments across diverse urban editing scenarios demonstrate significant improvements in efficiency, robustness, correctness, and spatial validity over existing baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决城市更新过程中，对现有城市规划进行高效、依赖感知的迭代式地理空间修改的自动化难题。传统城市规划方法多为从零生成完整方案，而现实中的城市更新往往需要对现有规划进行局部、精细化的调整，例如修改公园边界或调整道路网络。这种手动修改过程耗时费力，且需确保几何有效性和依赖一致性，现有计算方法（如生成式AI、优化方法或基于LLM的智能体）大多将城市规划视为一次性生成任务，缺乏对迭代修改过程中复杂依赖关系和中间状态错误的显式建模与处理。

为此，论文将城市更新形式化为一个基于GeoJSON结构化表示的“城市地理空间编辑”问题，并提出了一个分层智能体执行框架。该框架核心挑战包括：1）如何定义在现有规划上可执行的编辑操作；2）如何在迭代编辑中处理跨空间实体和几何层次（面、线、点）的依赖与约束；3）如何检测和纠正中间错误以避免累积。通过将自然语言编辑指令分解为分层几何意图，并协调不同层级智能体进行依赖感知的规划与执行，同时引入迭代执行-验证机制来保障全局空间一致性，从而实现对现有城市规划的可靠、自动化增量修改。

### Q2: 有哪些相关研究？

本文的相关研究主要涵盖三个方向：生成式城市规划模型、分层与功能感知规划模型，以及大语言模型与智能体AI系统。

在生成式城市规划模型方面，Wang等人（2020）提出了基于对抗学习的框架来自动生成土地利用配置，后续研究（Wang等人，2023）将其扩展为集量化、生成与评估于一体的统一框架。其他工作则探索了条件生成和变分生成模型以融入规划约束（Wang等人，2021），或引入基于流的生成模型以提高规划过程的可追溯性（Wang等人，2024）。这些方法专注于从零生成完整规划，而非对现有布局进行逐步编辑。

在分层与功能感知规划模型方面，研究强调了城市环境中的层次结构与功能依赖。例如，Wang等人（2023）提出了一个人类指令驱动的深度分层生成框架，将功能需求融入多级城市规划；另一项工作（Wang等人，2023）则利用分层强化学习建模区域间和街区间的依赖关系。这些方法虽能有效进行整体规划生成，但并非为现有城市布局的逐步、指令驱动式编辑而设计。

在大语言模型与智能体系统方面，LLM的进展（如GPT、LLaMA系列）显著提升了自然语言理解与指令遵循能力。在此基础上，智能体AI系统将语言模型嵌入支持规划、工具使用、执行与反馈的结构化框架中。相关研究也探索了构建可靠、可控的基于智能体的架构原则与实践。本文正是在此基础上，利用智能体系统将自然语言指令转化为结构化、多阶段的决策过程，以解决现有生成模型和分层规划模型未能处理的、依赖感知的逐步城市地理空间编辑问题。

### Q3: 论文如何解决这个问题？

论文通过一个层次化的智能体框架来解决城市地理空间编辑中的依赖感知和全局一致性问题。其核心方法包括四个关键组件：任务规划智能体、地理执行智能体、验证智能体和聚合智能体，它们协同工作形成一个分阶段的智能体工作流。

首先，**任务规划智能体**负责将自然语言编辑指令分解为结构化的、跨几何抽象层次（面、线、点）的编辑意图序列。每个意图明确规定了编辑范围、目标、子任务集和必须满足的约束条件。这种显式的分解将高层指令转化为机器可执行的计划，揭示了隐含的依赖关系，为后续的层次化执行奠定了基础。

其次，**地理执行智能体**采用**从粗到细的层次化执行策略**。编辑操作按照面、线、点的顺序依次执行。在每个几何层级内部，执行被建模为一个状态转移过程：执行器调用层级特定的地理空间工具（分为只读的信息查询工具和状态更新的几何编辑工具），顺序处理子任务，并将中间状态和观察结果传递给后续子任务。关键设计在于**跨层级交互**：较粗层级（如面）执行完成后产生的更新布局，会作为输入传递给下一个更细层级（如线）的执行器。这确保了细粒度的编辑始终在已反映高层结构决策的空间上下文中进行，从而维护了全局结构一致性。

为了应对错误累积和局部有效但全局无效的问题，论文引入了**自反思验证机制**。**验证智能体**与执行过程紧密耦合，在每一个子任务执行后立即介入。它根据几何有效性、依赖一致性和意图符合性等标准，对执行结果进行可接受性判定。只有被验证通过的结果才会被允许传播到后续执行步骤；若验证失败，则触发带有诊断反馈的重新执行。这种执行时验证充当了门控机制，将错误本地化，防止无效中间状态污染后续编辑。

最后，**聚合智能体**在所有执行阶段完成后，整合所有经过验证的编辑结果，生成最终更新后的城市计划（GeoJSON格式）以及一份包含执行轨迹、验证决策和元数据的详细摘要，确保了结果的可追溯性和透明度。

综上，该框架通过“意图分解 -> 层次化依赖执行 -> 迭代实时验证 -> 结果聚合”的闭环流程，系统性地解决了城市编辑中多步骤、跨层级、依赖复杂的修改难题，显著提升了编辑的效率、鲁棒性和空间有效性。

### Q4: 论文做了哪些实验？

论文在三个层次的几何编辑任务（点、线、面）上进行了全面的实验。实验设置方面，作者从OpenStreetMap收集了219个城市的城市地理空间数据，构建了包含点编辑（500个样本）、线编辑（500个样本）和面编辑（1500个样本）的数据集。评估指标包括衡量几何偏差的相对执行误差（REE）、衡量面积变化偏差的面积合规误差（ACE）以及衡量任务成功率的执行有效率（EVR）。

基准测试将提出的分层智能体框架（Agentic）与多种单次执行（Single-pass）基线模型进行了对比，这些基线模型基于闭源（如GPT-5-Mini/Nano）和开源（如DeepSeek-R1、Qwen、Llama系列）的大语言模型。主要结果显示，智能体框架在所有任务层级上均显著优于基线。具体而言，在点编辑任务上，智能体框架（使用LLaMA-3-8B-Instruct）取得了最低的REE（0.187）和次高的EVR（0.975）；在线编辑任务上，取得了最低的REE（0.319）和最高的EVR（0.947）；在面编辑任务上，取得了最低的ACE（0.081）和最高的EVR（0.979）。这表明随着任务复杂性增加，智能体框架的优势更加明显。

此外，论文还进行了消融实验、鲁棒性检查和参数敏感性分析。消融实验表明，移除任务规划器或验证器都会导致性能下降，验证了这两个组件的必要性。鲁棒性检查显示，在提示词中加入噪声扰动时，智能体框架仍能保持最佳性能。参数敏感性分析则表明，最大重试次数R主要影响执行成功率（EVR），而对几何精度（1-REE/1-ACE）的提升有限。案例研究进一步展示了该方法在真实城市更新场景（如绿地扩展）中的实用性和规划意识。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其规划约束相对基础，且缺乏与人类用户的交互反馈机制。未来可进一步探索的方向包括：首先，引入更丰富的规划约束，如社会经济指标、环境影响评估等，使系统能处理更复杂的多目标优化问题。其次，集成交互式人机协作机制，允许规划专家在关键决策点提供反馈或修正，以提升系统的实用性和可控性。此外，可研究将框架扩展至四维时空规划，动态模拟城市演变过程。最后，探索跨城市、跨尺度的知识迁移学习，以增强模型在新场景下的适应能力。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为“City Editing”的层次化智能体执行框架，旨在将城市更新任务自动化。其核心贡献在于将传统的、需要从头规划的生成式城市设计范式，转变为对现有结构化地理空间规划（如GeoJSON格式）进行依赖感知的增量式编辑。

论文首先形式化定义了“城市地理空间编辑”这一新问题，强调其依赖感知和迭代纠错的特性。为应对这一挑战，作者提出了一个层次化智能体框架。该框架将自然语言编辑指令分解为跨越多边形、线和点等多个几何层次的意图，并分配给专门的智能体执行。关键创新在于引入了显式的中间空间约束传播机制，使下游编辑能基于上游决策进行，从而协调跨空间元素和抽象层次的相互依赖编辑。此外，框架集成了一个迭代执行-验证机制，在每一步编辑后检查几何有效性、依赖一致性和约束满足情况，以缓解错误累积并确保全局空间一致性。

该工作的意义在于为现实世界中迭代、依赖复杂的城市更新工作流提供了可靠的计算支持，显著提升了编辑的效率、正确性和空间有效性，推动了城市智能从“一次性生成”向“可执行、可验证的增量式修改”的范式转变。
