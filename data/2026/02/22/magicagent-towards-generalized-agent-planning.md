---
title: "MagicAgent: Towards Generalized Agent Planning"
authors:
  - "Xuhui Ren"
  - "Shaokang Dong"
  - "Chen Yang"
  - "Qing Gao"
  - "Yunbin Zhao"
  - "Yongsheng Liu"
  - "Xinwei Geng"
  - "Xiang Li"
  - "Demei Yan"
  - "Yanqing Li"
  - "Chenhao Huang"
  - "Dingwei Zhu"
  - "Junjie Ye"
  - "Boxuan Yue"
  - "Yingnan Fu"
  - "Mengzhe Lv"
  - "Zezeng Feng"
  - "Boshen Zhou"
  - "Bocheng Wang"
  - "Xuanjing Huang"
date: "2026-02-22"
arxiv_id: "2602.19000"
arxiv_url: "https://arxiv.org/abs/2602.19000"
pdf_url: "https://arxiv.org/pdf/2602.19000v1"
categories:
  - "cs.AI"
  - "cs.HC"
tags:
  - "Agent 架构"
  - "Agent 数据合成"
  - "Agent 规划"
  - "工具使用"
  - "Agentic 强化学习"
  - "多任务训练"
  - "基础模型"
relevance_score: 9.5
---

# MagicAgent: Towards Generalized Agent Planning

## 原始摘要

The evolution of Large Language Models (LLMs) from passive text processors to autonomous agents has established planning as a core component of modern intelligence. However, achieving generalized planning remains elusive, not only by the scarcity of high-quality interaction data but also by inherent conflicts across heterogeneous planning tasks. These challenges result in models that excel at isolated tasks yet struggle to generalize, while existing multi-task training attempts suffer from gradient interference. In this paper, we present \textbf{MagicAgent}, a series of foundation models specifically designed for generalized agent planning. We introduce a lightweight and scalable synthetic data framework that generates high-quality trajectories across diverse planning tasks, including hierarchical task decomposition, tool-augmented planning, multi-constraint scheduling, procedural logic orchestration, and long-horizon tool execution. To mitigate training conflicts, we propose a two-stage training paradigm comprising supervised fine-tuning followed by multi-objective reinforcement learning over both static datasets and dynamic environments. Empirical results demonstrate that MagicAgent-32B and MagicAgent-30B-A3B deliver superior performance, achieving accuracies of $75.1\%$ on Worfbench, $55.9\%$ on NaturalPlan, $57.5\%$ on $τ^2$-Bench, $86.9\%$ on BFCL-v3, and $81.2\%$ on ACEBench, as well as strong results on our in-house MagicEval benchmarks. These results substantially outperform existing sub-100B models and even surpass leading closed-source models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体（Agent）规划能力的泛化问题。当前，大型语言模型（LLM）正从被动文本处理器演变为自主智能体，规划能力是其核心。然而，实现**通用化规划**面临两大挑战：一是高质量交互数据的稀缺；二是不同规划任务（如任务分解、工具使用、多约束调度等）之间存在内在冲突，导致模型在单一任务上表现优异却难以泛化，而简单的多任务训练又会因梯度干扰引发“跷跷板效应”（即一个任务性能提升导致其他任务性能下降）。

为此，论文提出了MagicAgent系列基础模型。其解决方案包括：1）设计了一个轻量级、可扩展的合成数据框架，用于生成覆盖多种规划任务的高质量轨迹数据；2）提出了一种两阶段训练范式，结合监督微调（SFT）与多目标强化学习（RL），以协同利用异构静态数据集并缓解训练冲突，从而提升在静态数据集和动态稀疏奖励环境中的泛化能力。最终，模型在多个基准测试上取得了超越现有百亿参数以下模型乃至部分领先闭源模型的性能。

### Q2: 有哪些相关研究？

相关研究主要围绕三个方向展开。首先，在**大语言智能体模型**方面，已有大量工作利用LLM构建面向特定应用的智能体，例如工具使用（如AutoAct、ToolLLM）、具身规划、网页浏览和软件工程。然而，这些方法多专注于孤立领域，缺乏泛化能力。数据稀缺是核心瓶颈，为此有研究通过模拟环境（如TaskCraft、Agentic in Environment）或与真实API交互来合成行为轨迹数据，但这些方法通常耗时且任务多样性有限。本文的MagicAgent通过一个轻量级、可扩展的合成数据框架来生成跨多种规划任务的高质量轨迹，旨在解决数据稀缺和多样性不足的问题。

其次，在**智能体模型训练范式**方面，主流方法包括监督微调（SFT）和强化学习（RL）。SFT工作（如AgentTuning、Agent-FLAN）利用指令数据或轨迹对模型进行适配；RL方法（如AgentGym、WebRL）则通过环境反馈或奖励模型来优化策略。此外，也有研究探索多目标奖励或高效微调技术。但这些范式往往各自为政，缺乏有效整合。本文提出了一种两阶段训练范式，结合了SFT和基于静态数据集与动态环境的多目标强化学习，以解决多任务训练中的梯度冲突问题，追求更强的鲁棒性和泛化能力。

最后，在**混合专家模型训练与稳定性**方面，MoE架构被用于降低推理成本，但传统的负载均衡方法（如辅助损失、容量限制）在应对智能体多领域任务时，可能抑制专家的专业化。近期研究（如引入正交损失、ERC损失）试图增强专家特异性。本文的研究背景与之相关，因为需要为异构的规划任务训练MoE模型，但文中未详细描述其具体如何解决MoE的负载均衡与专业化平衡问题，这可能是其方法的一个组成部分或未来方向。

### Q3: 论文如何解决这个问题？

MagicAgent 通过一个轻量级、可扩展的合成数据生成框架与一个两阶段训练范式，系统性地解决了高质量智能体规划数据稀缺以及异构任务间训练冲突的问题。

**核心方法：合成数据生成框架**
论文的核心创新在于构建了一个系统化的合成数据生成管道，旨在覆盖智能体规划的主要范式，包括：分层任务分解、工具增强规划、多约束调度、程序逻辑编排和长视野工具执行。针对“分层任务分解”，该方法首先从大量开源和内部API中收集工具并构建两个图结构：有向的工具依赖图（建模因果流）和无向的参数共享图（建模逻辑协同）。基于此，定义了三种“原子计划”作为最小语义单元：孤立计划（单个工具）、串行计划（两个有依赖的工具）和并行计划（两个逻辑相关但执行独立的工具）。随后，通过连接、添加、分组、掩码、转换和拆分等操作符，将这些原子计划组合成复杂、高熵的规划轨迹，以模拟真实世界的交互复杂性。生成的数据经过去重、模式验证和语义验证三重质量过滤，确保高质量。

**架构设计与关键技术**
1.  **数据生成的多智能体系统**：对于“工具增强规划”，框架构建了一个端到端的多智能体系统来生成完整的交互轨迹（思考 `e_t`，行动 `a_t`，观察 `o_t`）。具体包括：
    *   **推理智能体**：基于对话历史和预定的“黄金”工具调用，以“事后推理”的方式生成每一步的思考过程。
    *   **规划器**：执行从分层分解阶段得到的黄金行动序列。
    *   **模拟器智能体**：一个虚拟化的API模拟器，为工具调用生成确定性的、语义一致的环境观察，避免了实时API调用的不稳定性和延迟问题。
2.  **支持条件规划**：框架定义了静态连接（固定执行顺序）和动态连接（基于前一步观察的条件分支）两种任务间拓扑关系，以模拟更复杂的现实应用场景。
3.  **两阶段训练范式**：为了缓解多任务训练中的梯度冲突，MagicAgent采用了两阶段训练：
    *   **第一阶段**：在静态的合成数据集上进行监督微调，让模型学习基础的规划能力。
    *   **第二阶段**：在静态数据集和动态环境上，进行多目标强化学习，进一步优化和泛化模型的规划性能。

总之，MagicAgent通过精心设计的、可控的合成数据生成流程，大规模创造了多样且高质量的规划轨迹，并结合两阶段训练策略，有效提升了智能体在多种规划任务上的泛化能力。

### Q4: 论文做了哪些实验？

论文的实验设置主要包括在多个基准测试上评估MagicAgent模型的性能。使用的基准测试包括：Worfbench、NaturalPlan、τ²-Bench、BFCL-v3、ACEBench以及内部构建的MagicEval。实验对比了不同规模的MagicAgent模型（如32B和30B-A3B参数版本）与现有规模在100B参数以下的模型以及领先的闭源模型。

主要结果显示，MagicAgent-32B和MagicAgent-30B-A3B在各项基准上均取得了优异表现。具体而言，在Worfbench上准确率达到75.1%，在NaturalPlan上为55.9%，在τ²-Bench上为57.5%，在BFCL-v3上为86.9%，在ACEBench上为81.2%。这些结果显著超越了现有的百亿参数以下模型，甚至在某些任务上超过了领先的闭源模型，证明了其在异构规划任务上的强大泛化能力。

### Q5: 有什么可以进一步探索的点？

该论文提出的MagicAgent在通用智能体规划上取得了显著进展，但仍有多个方向值得深入探索。局限性方面，其两阶段训练范式虽缓解了梯度冲突，但多目标强化学习的动态平衡机制、不同规划任务间的知识迁移效率仍有优化空间；合成数据框架的多样性和真实性有待进一步提升，以覆盖更复杂的现实世界不确定性。

未来可探索的方向包括：1) 研究更高效的多任务学习架构，如模块化或课程学习策略，以从根本上解决异构任务间的干扰；2) 将规划能力与更丰富的世界模型结合，使智能体能进行基于物理或社会常识的推理；3) 扩展智能体的元规划能力，使其能自主评估任务并动态调整规划策略；4) 探索在低资源或边缘设备上的轻量化部署方案，推动实际应用落地。

### Q6: 总结一下论文的主要内容

这篇论文提出了MagicAgent系列基础模型，旨在解决智能体实现**通用化规划**的核心难题。其核心贡献在于两点：首先，设计了一个轻量级、可扩展的**合成数据框架**，能够自动生成涵盖任务分解、工具规划、多约束调度等多种异构规划任务的高质量交互轨迹，解决了高质量训练数据稀缺的问题。其次，为了克服多任务训练中的梯度冲突，论文提出了一种**两阶段训练范式**：先进行监督微调，再利用多目标强化学习在静态数据集和动态环境中进行优化，从而有效协调不同规划目标。实验表明，MagicAgent模型在多个权威基准测试上取得了卓越性能，显著超越了现有的百亿参数以下模型，甚至部分领先于闭源模型。这项工作的意义在于为构建具备强大泛化能力的通用规划智能体提供了系统的数据生成和训练方法学路径。
