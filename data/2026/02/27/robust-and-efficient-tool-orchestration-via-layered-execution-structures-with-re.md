---
title: "Robust and Efficient Tool Orchestration via Layered Execution Structures with Reflective Correction"
authors:
  - "Tao Zhe"
  - "Haoyu Wang"
  - "Bo Luo"
  - "Min Wu"
  - "Wei Fan"
  - "Xiao Luo"
  - "Zijun Yao"
  - "Haifeng Chen"
  - "Dongjie Wang"
date: "2026-02-21"
arxiv_id: "2602.18968"
arxiv_url: "https://arxiv.org/abs/2602.18968"
pdf_url: "https://arxiv.org/pdf/2602.18968v2"
categories:
  - "cs.AI"
tags:
  - "工具使用"
  - "智能体架构"
  - "规划与推理"
  - "执行鲁棒性"
  - "错误纠正"
  - "工具编排"
relevance_score: 9.5
---

# Robust and Efficient Tool Orchestration via Layered Execution Structures with Reflective Correction

## 原始摘要

Tool invocation is a core capability of agentic systems, yet failures often arise not from individual tool calls but from how multiple tools are organized and executed together. Existing approaches tightly couple tool execution with stepwise language reasoning or explicit planning, leading to brittle behavior and high execution overhead. To overcome these limitations, we revisit tool invocation from the perspective of tool orchestration. Our key insight is that effective orchestration does not require precise dependency graphs or fine-grained planning. Instead, a coarse-grained layer structure suffices to provide global guidance, while execution-time errors can be corrected locally. Specifically, we model tool orchestration as learning a layered execution structure that captures high-level tool dependencies, inducing layer-wise execution through context constraints. To handle execution-time failures, we introduce a schema-aware reflective correction mechanism that detects and repairs errors locally. This design confines errors to individual tool calls and avoids re-planning entire execution trajectories. This structured execution paradigm enables a lightweight and reusable orchestration component for agentic systems. Experimental results show that our approach achieves robust tool execution while reducing execution complexity and overhead. Code will be made publicly available.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体系统中工具调用的可靠性与效率问题，尤其关注多工具协同执行时的失败风险。研究背景基于当前大语言模型（LLM）驱动的智能体系统日益复杂，需要调用多个外部工具来完成现实任务。行业趋势（如NVIDIA提出的混合架构）倾向于使用大模型进行高层规划、小模型（SLM）负责可扩展执行，此时核心挑战从单个工具调用转向多工具的长期可靠协调。

现有方法存在明显不足：一类是逐步反应式方法（如ReAct），缺乏全局结构指导，容易忽略隐式依赖，导致执行路径陷入死胡同或计算开销过高；另一类是“先规划后执行”方法（如HuggingGPT），虽提供全局计划，但对运行时偏差（如模式不匹配、格式错误）非常脆弱，通常依赖临时重试而非系统化修复。这些方法要么耦合了工具执行与逐步推理，要么依赖精细规划，导致行为脆弱、执行开销大，且难以适应小模型的有限上下文与容错能力。

本文要解决的核心问题是：如何在不依赖耗时的小模型微调前提下，实现兼具全局结构感知与局部错误恢复能力的工具编排。具体而言，论文提出通过分层执行结构（layered execution structure）与反射式修正（reflective correction）机制，将全局组织与本地执行解耦，从而在保证执行鲁棒性的同时降低复杂度。该方法旨在快速推断捕获工具间基本依赖关系的粗粒度执行草图，并在执行过程中通过模式感知的本地修复处理错误，避免错误级联传播，最终实现高效、可复用的工具编排组件。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：工具学习、规划范式以及高效工具学习。

在**工具学习**方面，早期研究如ToolBench构建了大规模基准测试和数据集，并提出了基于深度优先搜索的决策树（DFSDT）等方法进行多步工具调用。后续工作通过A*搜索剪枝、编译器并行执行或自我反思和偏好优化来提升效率与可靠性。本文与这些工作共享提升工具调用可靠性的目标，但指出幻觉和不稳定性问题依然存在，而本文通过分层执行结构和反射纠正机制来系统性地处理执行时错误。

在**规划范式**方面，相关工作可分为反应式方法和先规划后执行方法。反应式方法（如ReAct、Reflexion）交错进行推理与行动，灵活但缺乏全局依赖感知；先规划后执行方法（如HuggingGPT、Plan-and-Solve）先生成完整计划再执行，但规划与执行脱节导致难以应对运行时故障。本文桥接了这两种范式，通过轻量级模块预测粗粒度的分层结构来提供全局依赖指导，同时保持执行层面对运行时故障的局部适应性，避免了完整的重新规划。

在**高效工具学习**方面，针对小模型（SLMs）在工具编排上的挑战，先前工作（如DTA-Tool、GAP、ToolGen）主要通过微调将工具知识或依赖图结构内化到LLMs中。这些方法有效但涉及训练成本，且难以适应不断演化的工具集。本文则采取了不同路径，将规划卸载给外部轻量级模块，并利用上下文约束的执行来减轻现成SLMs每一步的推理负担，从而在不进行任何LLM微调的情况下实现有竞争力的性能。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为 **分层执行结构** 的轻量级工具编排框架来解决多工具调用中的脆弱性和高开销问题。其核心思想是将全局的粗粒度结构规划与局部的细粒度执行及错误处理解耦，从而在保证鲁棒性的同时降低执行复杂度。

**整体框架与主要模块**：
该方法包含三个核心组件，构成了一个“学习-执行-反思与修复”的闭环流程。
1.  **学习：分层执行草图**：这是全局规划模块。其目标不是预测精确的工具间依赖图，而是为每个候选工具分配一个执行层（Layer）。层序代表了粗略的执行顺序：高层工具可以依赖低层工具的输出，但同层工具可并行执行。该模块通过一个轻量级神经网络实现，它接收任务查询和工具描述的嵌入表示，经过投影、上下文编码（Transformer Encoder）后，通过序数回归预测每个工具所属的层。这种设计避免了枚举所有成对依赖关系的高昂成本，仅提供一个结构化的“脚手架”。
2.  **执行：上下文约束调用**：这是按层执行的模块。系统严格按照预测的层序，逐层执行工具。在每一层，小型语言模型（SLM）只能看到当前层工具的模式（Schema）以及之前所有层的工具执行结果（观察）。这种设计通过上下文约束，强制模型遵循预定的执行顺序，防止了因违反前提依赖关系而导致的下游错误，同时将长程推理分解为多个短视距决策，有效控制了上下文长度。
3.  **反思与修复：局部校正**：这是处理执行时错误的模块，旨在将错误隔离在单个工具调用层面，避免污染整个执行轨迹。它包含两个关键机制：
    *   **模式门**：在工具调用执行前，根据其JSON模式对参数进行轻量级验证（检查必填字段、类型、枚举值等）。无效调用会被直接拒绝并生成结构化错误诊断报告，防止错误信息进入主执行上下文。
    *   **修复机制**：对于被拒绝或执行失败的调用，系统在预设的预算内进行本地修复。修复过程分两级：首先尝试无需LLM的确定性编辑（如删除意外键）；若失败，则基于错误诊断信息，调用LLM进行参数修复。修复后的调用会重新通过模式门验证。此机制避免了代价高昂的全局重规划或整个轨迹的重试。

**创新点**：
1.  **结构解耦**：将复杂的工具编排问题分解为“粗粒度分层规划”和“层内约束执行”两个阶段，用轻量的结构预测器替代了传统方法中与推理紧密耦合的逐步规划或精细依赖图构建。
2.  **上下文约束执行**：通过分层限制工具可见性，强制模型遵循依赖顺序，这不仅提升了执行的鲁棒性，也显著降低了小型语言模型在长上下文中的推理负担。
3.  **模式感知的局部反射校正**：引入了“模式门”进行前置验证，并结合预算控制的、分层的本地修复循环。这种设计将错误处理局部化，有效防止了错误传播和上下文污染，同时避免了因单个工具失败而重启整个任务的开销。

### Q4: 论文做了哪些实验？

论文在StableToolBench数据集上进行了全面的实验评估，该数据集通过缓存系统和API模拟器来稳定评估环境，并包含指令、工具和类别三个维度的泛化测试，任务复杂度分为I1（单工具）、I2（类别内多工具）和I3（集合内多工具）三个递增场景。实验对比了三种执行策略：ReAct、DFSDT以及本文提出的“先规划后执行”方法（RETO），并使用了多种模型作为骨干，包括未进行工具调优的开源模型（Qwen2.5系列、LLaMA-3.1-8B）、经过工具调优的模型（ToolLLaMA-7B）以及闭源模型（GPT-3.5系列）作为参考。

主要评估指标为可解任务通过率（SoPR）和可解任务胜率（SoWR）。关键结果显示，本文方法显著提升了未调优模型的表现：例如，在Qwen2.5-7B上，RETO将SoPR从DFSDT的12.2%提升至49.5%，甚至超过了工具调优的ToolLLaMA-7B（47.1%）和GPT-3.5+ReAct基线（45.4%-48.3%）。在答案质量（SoWR）方面，RETO加持的Qwen2.5-7B与工具调优的ToolLLaMA+DFSDT表现相当，在多子集上胜率超过50%。消融实验证实，执行草图（约束工具子集）和反射修复模块均对性能有重要贡献，移除任一组件都会导致SoPR下降。效率方面，与ToolLLaMA+DFSDT相比，RETO在Qwen2.5-7B上大幅降低了令牌消耗和推理步数，在复杂任务（I3-Inst.）上令牌使用减少84.8%，步数减少69.6%。此外，模型规模实验表明，该方法在7B至1.5B的模型上均能保持较强性能，仅在0.5B模型上出现明显退化。层预测器的超参数敏感性实验显示，其性能在较大参数范围内保持稳定。

### Q5: 有什么可以进一步探索的点？

该论文提出的分层执行结构虽能降低复杂度，但层结构预测的准确性依赖训练数据质量，可能难以泛化到复杂或动态依赖的任务。其反思纠错机制仅针对单个工具调用，未考虑跨层错误的传播问题。未来可探索更动态的层结构生成方法，例如引入实时依赖感知机制，使层划分能随执行状态调整。同时，可将纠错模块扩展为跨层协同修复，通过全局轻量监控捕捉连锁错误。结合论文提到的轻量化训练，可研究小模型适配技术，如蒸馏层预测器或压缩反思模块，以提升资源受限场景的实用性。此外，探索与符号规划的结合，在保持粗粒度引导的同时嵌入关键依赖校验，可能进一步提升鲁棒性。

### Q6: 总结一下论文的主要内容

该论文针对智能体系统中工具调用常因组织与执行方式不当而失败的问题，提出了一种基于分层执行结构与反射校正的鲁棒高效工具编排方法。核心贡献在于将工具编排重新定义为学习一个捕获高层依赖关系的分层执行结构，通过上下文约束引导分层执行，而非依赖精确的依赖图或细粒度规划。方法上，首先构建粗粒度的分层结构提供全局指导，再引入模式感知的反射校正机制，在局部检测并修复执行时错误，从而将故障限制在单个工具调用内，避免重新规划整个执行轨迹。主要结论表明，这种结构化执行范式实现了轻量且可复用的编排组件，在实验中显著提升了工具执行的鲁棒性，同时降低了执行复杂度和开销。
