---
title: "Exploring Interaction Paradigms for LLM Agents in Scientific Visualization"
authors:
  - "Jackson Vonderhorst"
  - "Kuangshi Ai"
  - "Haichao Miao"
  - "Shusen Liu"
  - "Chaoli Wang"
date: "2026-04-30"
arxiv_id: "2604.27996"
arxiv_url: "https://arxiv.org/abs/2604.27996"
pdf_url: "https://arxiv.org/pdf/2604.27996v1"
categories:
  - "cs.AI"
  - "cs.GR"
  - "cs.HC"
tags:
  - "LLM Agent"
  - "Scientific Visualization"
  - "Interaction Paradigm"
  - "Agent Evaluation"
  - "Benchmark"
relevance_score: 7.5
---

# Exploring Interaction Paradigms for LLM Agents in Scientific Visualization

## 原始摘要

This paper examines how different types of large language model (LLM) agents perform on scientific visualization (SciVis) tasks, where users generate visualization workflows from natural-language instructions. We compare three primary interaction paradigms, including domain-specific agents with structured tool use, computer-use agents, and general-purpose coding agents, by evaluating eight representative agents across 15 benchmark tasks and measuring visualization quality, efficiency, robustness, and computational cost. We further analyze interaction modalities, including code scripts and model context protocol (MCP) or API calls for structured tool use, as well as command-line interfaces (CLI) and graphical user interfaces (GUI) for more general interaction, while additionally studying the effect of persistent memory in selected agents. The results reveal clear tradeoffs across paradigms and modalities. General-purpose coding agents achieve the highest task success rates but are computationally expensive, while domain-specific agents are more efficient and stable but less flexible. Computer-use agents perform well on individual steps but struggle with longer multi-step workflows, indicating that long-horizon planning is their primary limitation. Across both CLI- and GUI-based settings, persistent memory improves performance over repeated trials, although its benefits depend on the underlying interaction mode and the quality of feedback. These findings suggest that no single approach is sufficient, and future SciVis systems should combine structured tool use, interactive capabilities, and adaptive memory mechanisms to balance performance, robustness, and flexibility.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有基于大语言模型（LLM）的科学可视化（SciVis）智能体缺乏系统性比较与设计指导的问题。研究背景是，LLM正从被动接口转变为主动执行工作流的智能体系统，但在SciVis领域，不同交互范式（如通过脚本或API调用实现结构化工具使用的领域专用智能体、通过图形用户界面（GUI）直接交互的计算机使用智能体、以及通过命令行生成代码的通用编码智能体）的性能差异和适用场景尚不明确。现有方法的不足包括：缺乏对长时程工作流中鲁棒性、一致性和失败模式的显式分析；现有基准测试未深入探讨交互范式如何影响这些关键特性；同时，对于持久记忆等自适应机制的实际效果也缺乏跨范式的对比评估。因此，本文的核心问题是：系统地比较不同交互范式在SciVis任务中的有效性、效率、鲁棒性和计算成本，并分析持久记忆对性能的影响，进而为未来SciVis智能体的设计提供指导。

### Q2: 有哪些相关研究？

相关研究可从三个类别梳理。**方法类**工作中，域特定代理（如ChatVis、ParaView-MCP、InferA）通过结构化API调用实现高效执行，但耦合度高；计算机使用代理（如AVA、NLI4VolVis、UFO系列）通过视觉反馈和低层动作增强灵活性，但计算成本高；通用编码代理（如Codex、Claude Code）端到端构建流程，灵活性最强但缺乏结构化保障。**评测类**工作包括CoDA、MatPlotBench、VisEval等提出互补指标，VisualWebArena、WindowsAgentArena等跨环境基准，以及SciVisAgentBench和SVLAT针对科学可视化的系统评估框架。**方法改进类**中，Agent-S、OS-Copilot探索持久记忆与反思机制，VizGenie实现可复用可视化技能。本文与上述工作的核心区别在于：首次系统比较三类交互范式在科学可视化任务中的表现，并深入分析了交互模态（CLI、GUI）和记忆机制的影响，揭示了跨范式的权衡关系，而现有基准未明确分析交互范式对长程工作流鲁棒性、一致性和失败模式的影响。

### Q3: 论文如何解决这个问题？

本论文通过系统比较三类LLM Agent交互范式在科学可视化任务中的表现来解决问题，具体包括：领域特定Agent（如ChatVis和ParaView-MCP，通过代码脚本或MCP/API调用实现结构化工具使用）、计算机使用Agent（如微软UFO系列和Open Interpreter，通过GUI与软件交互）、以及通用编码Agent（如Claude Code和Codex，主要通过CLI代码生成）。研究构建了基于SciVisAgentBench的15个ParaView任务基准，涵盖单步操作到多步可视化流水线，并采用完整任务评估和逐步分解评估两种方式。核心创新点在于：(1) 设计了多维度评估体系，包括可视化质量（基于LLM评分）、效率（token消耗和运行时间）、鲁棒性（10次重复试验的变异性和错误恢复能力）以及计算成本；(2) 引入了持久记忆机制的分析，在Agent-S和Letta上分别对比GUI和CLI环境下学习启用/禁用配置的效果；(3) 通过逐步评估方法隔离单个操作的正确性，同时控制错误传播。关键技术包括使用统一的任务规格和系统环境确保公平比较，通过pass@k和pass^k曲线分析多试次下的成功率分布，以及LLM Judge（Claude-Opus-4.6）自动评估可视化结果质量。研究揭示了不同范式的明确权衡：通用编码Agent任务成功率最高但计算成本大，领域特定Agent更高效稳定但灵活性不足，计算机使用Agent在单步操作上表现良好但多步工作流中受限于长程规划能力，而持久记忆的优势取决于底层交互模式和反馈质量。

### Q4: 论文做了哪些实验？

论文在15个SciVisAgentBench基准任务上评估了8个代表性智能体，涵盖三类交互范式：通用编码智能体（Codex CLI、Claude Code）、领域专用智能体（ChatVis、ParaView-MCP）和计算机使用智能体（UFO、Open Interpreter、Agent-S、Letta）。实验设置了全任务执行和逐步分解两种模式。主要结果包括：通用编码智能体表现最佳，Codex CLI获得最高总分（68.99±1.92）和100%完成率，但平均需774.52K输入token/任务，计算成本极高；领域专用智能体效率最高，ChatVis仅需8.17K输入token，完成率45.0%-50.7%；计算机使用智能体全任务完成率低于40%，但在逐步分解下单步通过率提升至60%-65%，token使用和运行时间显著降低。记忆机制对比显示，Letta启用记忆后总分从19.09提升至30.78，Agent-S从10.75提升至18.31，同时降低token消耗。实验揭示了范式间的明确权衡：通用编码智能体最大化任务完成但成本高，领域专用智能体优化效率但灵活性有限，计算机使用智能体受限于长程规划能力。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于当前各范式（通用编码、领域专用、计算机使用）存在根本性权衡，单一范式无法胜任复杂科学可视化任务。未来方向首先应探索混合架构，将确定性API执行（保证低级操作可靠性）与CLI推理（复杂流程生成）及GUI交互（感知接地）结合，并引入持久记忆机制以自适应调整策略。其次，关键挑战在于科学可视化专用自评估机制：可视化正确性常依赖感知和语义属性（如传递函数、相机视角、特征可见性），无法通过代码执行完全验证，因此需整合视觉反馈闭环，让智能体能迭代检查并修正中间状态。此外，LLM在长序列任务中的规划能力薄弱，可通过结构化工具调用流程（如Agent Skills）减少冗余探索，提升稳健性。最终目标是设计统一框架，在效率、稳健性和灵活性之间取得动态平衡。

### Q6: 总结一下论文的主要内容

该论文系统性地探索了大型语言模型（LLM）代理在科学可视化（SciVis）任务中的交互范式。问题定义是用户通过自然语言指令生成可视化工作流，需要比较不同代理类型的性能。研究方法包括对三种主要交互范式（领域特定代理、计算机使用代理、通用编码代理）进行评估，涉及8个代表性代理和15个基准任务，从可视化质量、效率、鲁棒性和计算成本四个维度进行测量。主要结论揭示了范式间的明确权衡：通用编码代理任务成功率最高但计算成本高；领域特定代理效率高且稳定但灵活性不足；计算机使用代理在单个步骤表现良好但受限于长程规划。此外，持久记忆有助于提升重复任务表现，但其效果依赖交互模式和反馈质量。该研究的核心贡献在于提供了对LLM代理在科学可视化中交互范式的系统比较，为设计结合结构化工具使用、交互能力和自适应内存机制的下一代系统提供了关键指导。
