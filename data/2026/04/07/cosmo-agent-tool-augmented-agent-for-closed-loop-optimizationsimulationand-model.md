---
title: "COSMO-Agent: Tool-Augmented Agent for Closed-loop Optimization,Simulation,and Modeling Orchestration"
authors:
  - "Liyuan Deng"
  - "Shujian Deng"
  - "Yongkang Chen"
  - "Yongkang Dai"
  - "Zhihang Zhong"
  - "Linyang Li"
  - "Xiao Sun"
  - "Yilei Shi"
  - "Huaxi Huang"
date: "2026-04-07"
arxiv_id: "2604.05547"
arxiv_url: "https://arxiv.org/abs/2604.05547"
pdf_url: "https://arxiv.org/pdf/2604.05547v1"
categories:
  - "cs.AI"
  - "cs.GR"
tags:
  - "Tool-Augmented Agent"
  - "Reinforcement Learning"
  - "Closed-loop Optimization"
  - "CAD-CAE"
  - "Industrial Design"
  - "Constraint Satisfaction"
  - "Simulation"
relevance_score: 7.5
---

# COSMO-Agent: Tool-Augmented Agent for Closed-loop Optimization,Simulation,and Modeling Orchestration

## 原始摘要

Iterative industrial design-simulation optimization is bottlenecked by the CAD-CAE semantic gap: translating simulation feedback into valid geometric edits under diverse, coupled constraints. To fill this gap, we propose COSMO-Agent (Closed-loop Optimization, Simulation, and Modeling Orchestration), a tool-augmented reinforcement learning (RL) framework that teaches LLMs to complete the closed-loop CAD-CAE process. Specifically, we cast CAD generation, CAE solving, result parsing, and geometry revision as an interactive RL environment, where an LLM learns to orchestrate external tools and revise parametric geometries until constraints are satisfied. To make this learning stable and industrially usable, we design a multi-constraint reward that jointly encourages feasibility, toolchain robustness, and structured output validity. In addition, we contribute an industry-aligned dataset that covers 25 component categories with executable CAD-CAE tasks to support realistic training and evaluation. Experiments show that COSMO-Agent training substantially improves small open-source LLMs for constraint-driven design, exceeding large open-source and strong closed-source models in feasibility, efficiency, and stability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决工业设计优化中一个核心瓶颈问题：如何实现计算机辅助设计（CAD）与计算机辅助工程（CAE）之间的高效、自动化闭环迭代。研究背景是现代工业设计需要在满足多种相互耦合的物理、几何及经济约束下，反复搜索最优几何形状。当前，工程师必须手动将高维的仿真反馈（如应力场、位移等）转化为低维、结构化的CAD参数化编辑，这一过程被称为“CAD-CAE语义鸿沟”。现有自动化方法存在明显不足：基于无导数优化的方法通常无法处理模型可执行性约束和工具链随机故障；基于可微分或代理模型的方法常偏离实际生产流程，且无法直接生成与参数化历史一致的、可执行的CAD编辑指令；而近期基于大语言模型（LLM）的智能体方法，在面临模型再生失败、网格划分错误或求解器不收敛等复杂故障时，表现依然脆弱，且标准的指令微调或RLHF主要针对短视距模仿，而非由下游仿真结果驱动的长视距试错优化。

因此，本文要解决的核心问题是：如何构建一个能够稳定、可靠地自主完成“设计-仿真-反馈-修改”全闭环流程的智能系统，以应对实际工业环境中工具链的随机故障、硬性的可执行性约束以及长序列决策的挑战。为此，论文提出了COSMO-Agent框架，将CAD生成、CAE求解、结果解析和几何修订建模为一个交互式强化学习环境，通过设计一个鼓励可行性、工具链鲁棒性和输出结构有效性的多约束奖励函数，训练LLM学习协调外部工具并修订参数化几何，直至满足所有约束条件。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：CAD生成与操作、仿真自动化以及工具增强的智能体框架。

在**CAD生成与操作**方面，相关工作包括SketchGraphs、Fusion 360 Gallery和JoinABLe等，它们分别提供了大规模约束图、程序化CAD语言和装配体学习的数据与环境。近期研究如LLM4CAD、Text-to-CadQuery和OpenECAD，则利用大模型从文本或图像生成CAD程序或可编辑草图。工具增强的代理如CAD-Assistant通过CAD API迭代执行和修复命令。与这些工作不同，本文提出的COSMO-Agent不仅关注几何正确性、可编辑性或任务完成度，其核心创新在于将下游的CAE仿真反馈和工程验收约束整合到一个闭环优化目标中，并将真实CAD-CAE流程中的可执行性和故障恢复作为首要优化目标。

在**仿真自动化**方面，已有工作如MetaOpenFOAM、CFDagent、NL2FOAM和Foam-Agent等，将LLM与工程仿真器（如OpenFOAM）结合，用于自动生成求解器配置、调试并执行仿真。这些系统主要目标是完成或复现一个指定的仿真实例。与之相比，COSMO-Agent专注于**多轮次设计优化**，即基于仿真结果迭代修改几何，直到满足多个耦合的验收约束，这在真实且不稳定的工具链环境下是一个尚未充分探索的挑战。

在**工具增强的智能体框架**方面，ReAct、MRKL和SayCan等范式将推理与工具调用交织；后续研究通过训练提升了工具调用的时机和API调用保真度。近期框架如InternBootcamp、HybridFlow和MARTI，通过可验证反馈、高效rollout和多智能体训练来支持长视野任务。然而，这些框架并未直接解决闭环CAD-CAE优化问题，该问题要求智能体在硬性的可执行性约束、有限的工具调用/重试预算下，产生结构化的、历史一致的参数化编辑，并能对随机工具链故障保持鲁棒。COSMO-Agent通过引入明确的故障状态和基于下游CAE反馈与工程约束的多目标奖励函数来训练LLM策略，从而填补了这一空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为COSMO-Agent的、基于工具增强的强化学习框架来解决CAD-CAE语义鸿沟问题，实现从仿真反馈到有效几何修改的闭环优化。其核心方法是将整个设计-仿真迭代过程构建为一个交互式强化学习环境，让大语言模型学习如何编排外部工具并修改参数化几何体，直至满足所有设计约束。

整体框架是一个闭环迭代系统。用户输入设计需求、约束、初始几何参数和材料参数，构成任务实例。大语言模型根据输入生成逐轮更新的设计计划。在每一轮迭代中，模型根据当前设计状态（几何参数和材料选择）调用工具链，并接收仿真反馈的标量结果（最大位移、最大冯·米塞斯等效应力、成本）。模型利用这些数值反馈来验证设计是否满足位移、应力和成本约束。若不满足，则基于历史交互记录和最新反馈，输出更新后的设计参数和材料选择，触发下一轮CAD生成和CAE验证，直至所有约束满足或达到最大迭代轮数。

该框架的关键创新在于其精心设计的**MCP工具集**和**多约束奖励模块**。MCP工具集通过统一的结构化接口暴露CAD-CAE工具链，包含四个核心工具：1) **CAD生成器**：根据零件类别和参数向量生成可供下游求解器使用的实体几何文件，并输出用于边界条件分配的几何元数据（如锚点）；2) **CAE求解器**：对生成的几何体进行基于物理的有限元分析，利用几何元数据中的锚点实现自动化、一致的边界条件分配；3) **结果提取器**：从求解器结果文件中提取最大位移和最大等效应力等标量指标，用于约束检查；4) **成本计算器**：基于几何体积、材料密度和单价计算设计成本。

为了稳定、高效地训练模型学习工具使用策略，论文采用了**广义强化策略优化**，并设计了一个由三部分组成的综合奖励函数：1) **约束奖励**：根据最终设计满足的约束数量（位移、应力、成本）给予分段奖励，鼓励全面满足所有工程约束；2) **可行即停奖励**：惩罚在找到可行解后继续进行的冗余工具调用，鼓励高效性；3) **结构化输出一致性奖励**：要求模型最终输出结构化的JSON对象（包含类别、材料和几何参数），且内容需与产生最终结果的设计提案一致，以确保下游可执行性和仿真可复现性。这种奖励设计使模型能在一个训练目标中同时对齐满足工程约束、减少冗余调用和保持输出一致性等多个目标，且奖励计算仅依赖于轨迹日志，无需额外的CAE重评估，保证了训练与执行的一致性。

### Q4: 论文做了哪些实验？

实验基于Qwen3-8B模型，在Internbootcamp框架下进行训练，使用16块H200 GPU。训练采用GRPO方法，每个提示采样8条轨迹，最大交互轮次为15轮。CAD生成使用CADQuery库，CAE求解使用FreeCAD FEM后端（Gmsh网格划分、CalculiX求解器）。评估数据集为涵盖25个组件类别的工业对齐数据集，包含可执行的CAD-CAE任务。

对比方法包括开源模型（Qwen3-8B、Intern-S1-mini、Llama-4-Scout、Qwen3-30B、Qwen3-Next、Intern-S1）和闭源模型（Claude-Sonnet-4.5、Gemini-3-Flash）。评估指标包括全成功率（FSR）、位移满足率（DSR）、应力满足率（SSR）、成本满足率（CSR）、模型输出提取率（MEO）、平均得分（AS）和平均工具调用次数（ATC）。

主要结果显示，COSMO-Agent（8B）在测试集上取得74.5%的FSR，优于最佳开源基线Intern-S1（32.0%）和最佳闭源基线Gemini-3-Flash（67.5%）。其DSR、SSR、CSR分别为87.5%、76.0%、93.5%，MEO达100%。ATC为6.72，表明其以较少工具调用达成可行解，交互效率较高。在未见类别泛化集上，COSMO-Agent的FSR为75.0%，保持领先且MEO仍为100%。

消融实验表明，移除RL训练（w/o RL）会使FSR降至26.0%；移除基于交互日志的奖励（w/o Rollout Reward）会使FSR降至36.0%，且ATC降至2.62，证明RL训练和交互日志奖励对闭环优化性能提升至关重要。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于当前框架主要处理单一零件、线性材料及简单物理约束，尚未涵盖接触、装配、多部件耦合等复杂工业场景。未来可探索将COSMO-Agent扩展至非线性材料、多物理场耦合等更丰富的物理仿真环境，并支持多种CAD/CAE后端工具以提升通用性。此外，在更大动作空间、更严格计算预算及多样化故障模式下的可扩展性仍需深入研究。

可能的改进思路包括：设计更精细的课程学习策略，分阶段引入复杂约束以提升长周期任务的稳定性；结合世界模型或离线强化学习技术，减少对昂贵实时仿真的依赖；引入多智能体协作机制，让不同Agent分别负责几何编辑、仿真解析与约束验证，以应对更复杂的设计优化问题。这些方向有望进一步提升闭环设计优化的自动化程度与工业实用性。

### Q6: 总结一下论文的主要内容

该论文针对工业设计中CAD-CAE迭代优化的瓶颈问题，即仿真反馈难以转化为满足多重约束的有效几何编辑，提出了COSMO-Agent框架。其核心贡献是将闭环的CAD-CAE过程建模为一个包含异构工具、硬性可执行约束和随机故障状态的长周期序贯决策问题，并采用工具增强的强化学习方法训练大语言模型来协调外部工具并迭代修订参数化几何模型，直至满足约束。方法上，论文设计了多约束奖励函数，联合优化设计的可行性、工具链的鲁棒性以及输出结果的结构有效性，以防止奖励欺骗。此外，研究还贡献了一个涵盖25个组件类别、包含约2万个可执行任务的工业级基准数据集，用于训练和评估。实验表明，经过COSMO-Agent训练的中等规模开源模型在可行性、效率和稳定性方面均优于大型开源和闭源模型，证明了该框架在实现可靠、自动化的闭环设计-仿真优化方面的有效性和实用意义。
