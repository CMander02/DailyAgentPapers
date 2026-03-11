---
title: "EPOCH: An Agentic Protocol for Multi-Round System Optimization"
authors:
  - "Zhanlin Liu"
  - "Yitao Li"
  - "Munirathnam Srikanth"
date: "2026-03-10"
arxiv_id: "2603.09049"
arxiv_url: "https://arxiv.org/abs/2603.09049"
pdf_url: "https://arxiv.org/pdf/2603.09049v1"
categories:
  - "cs.AI"
tags:
  - "Agent Protocol"
  - "Multi-Round Optimization"
  - "Self-Improvement"
  - "Workflow Engineering"
  - "System Optimization"
relevance_score: 7.5
---

# EPOCH: An Agentic Protocol for Multi-Round System Optimization

## 原始摘要

Autonomous agents are increasingly used to improve prompts, code, and machine learning systems through iterative execution and feedback. Yet existing approaches are usually designed as task-specific optimization loops rather than as a unified protocol for establishing baselines and managing tracked multi-round self-improvement. We introduce EPOCH, an engineering protocol for multi-round system optimization in heterogeneous environments. EPOCH organizes optimization into two phases: baseline construction and iterative self-improvement. It further structures each round through role-constrained stages that separate planning, implementation, and evaluation, and standardizes execution through canonical command interfaces and round-level tracking. This design enables coordinated optimization across prompts, model configurations, code, and rule-based components while preserving stability, reproducibility, traceability, and integrity of evaluation. Empirical studies in various tasks illustrate the practicality of EPOCH for production-oriented autonomous improvement workflows.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前自主智能体在迭代优化系统时缺乏统一、可复现且适用于生产环境的协议问题。随着大语言模型系统的发展，智能体已能通过迭代执行和反馈来优化提示、代码和机器学习系统。然而，现有方法（如DSPy、Promptbreeder、AgentHPO等）通常是针对特定任务设计的优化循环或领域专用代理，而非一个统一的协议。这导致它们缺乏明确的角色分离、规范执行接口和跨轮次的状态追踪，难以在异构环境中协调优化多个组件（如提示、模型配置、代码和基于规则的部件）。  

研究背景显示，生产环境中的机器学习系统通常包含多个相互依赖的部件，系统性能取决于这些部件的协同作用。现有方法虽然能优化单个工件，但无法以可复现、可追踪的方式管理跨轮次、跨组件的优化循环，这在实际部署中可能引发稳定性、评估完整性和可追溯性问题。  

因此，本文的核心问题是：如何设计一个通用的代理协议，以支持异构环境下多轮系统优化的协调管理，同时确保稳定性、可复现性、可追踪性和评估完整性。为此，论文提出了EPOCH协议，它将优化过程分为基线构建和迭代自改进两阶段，并通过角色约束的阶段（规划、实施、评估）、规范命令接口和轮次级追踪来结构化每一轮优化，从而实现对多样化优化任务的统一管理。

### Q2: 有哪些相关研究？

本文EPOCH的研究背景与多种相关研究工作密切相关，主要可分为方法类和应用类。

在**方法类**工作中，本文提及了多个针对特定任务进行迭代自我优化的研究。例如，DSPy、Promptbreeder和GEPA专注于**提示优化**，AgentHPO研究**超参数搜索**，而RepairAgent则关注**自主软件修复**。这些工作的共同点是它们都设计了任务特定的优化循环或领域特定的智能体。EPOCH与这些工作的**关系**在于，它同样旨在利用大语言模型进行迭代优化。其核心**区别**在于，EPOCH并非针对单一任务或组件，而是提出了一个**统一的、协议化的决策循环框架**。它将优化过程抽象为两个阶段（基线构建与迭代自我改进），并引入了角色约束阶段、规范执行接口和轮次级状态跟踪，以管理异构环境下的多轮系统优化，弥补了现有方法缺乏可复现、面向部署的统一协议层的不足。

在**应用类**工作中，本文的研究与构建生产级机器学习系统的实践紧密相连。这些系统通常包含提示、模型配置、代码和基于规则的组件等多个相互关联的部分。EPOCH的提出正是为了应对在这种复杂、异构环境中进行**协调优化**的挑战，确保在优化过程中保持评估的完整性、可复现性和可追溯性，这是许多现有任务特定优化循环所未能系统化解决的。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为EPOCH的工程化协议来解决多轮系统优化中缺乏统一、可追踪和可复现框架的问题。其核心方法是将迭代优化视为一个结构化的协议，而非单一优化器，强调基线构建与迭代改进的分离、角色约束的阶段划分以及标准化的执行与追踪。

整体框架分为两个主要阶段。第一阶段是基线构建，将问题规格（自然语言描述或结构化配置）转化为一个可执行的、经过验证的基线系统。此阶段通常涉及两个角色：种子规划器分析任务并设计初始系统与评估接口；基线执行器则将其实现为可运行的代码，并生成首个被接受的性能指标。如果已有验证基线，此阶段可简化为验证步骤。

第二阶段是多轮自我改进，这是一个循环过程。每轮都从当前已接受的状态开始，围绕四个逻辑角色展开：协调器管理轮次控制流（如预算和状态转换）；调查员分析当前系统和可用证据，提出在任务约束下的改进假设；执行器在允许的操作空间内（如修改提示词、调整超参数、更新代码）实施变更；评审员则通过标准化的评估接口评估候选状态，并决定是否接受该变更。这种将假设生成、实施与评估分离的设计，保障了评估的完整性，防止数据泄露或评估不一致。

关键技术包括：1）**角色约束的阶段分解**：明确分离规划、实施与评估职责，确保过程可控。2）**标准化的规范命令接口**：从任务规格衍生出统一的执行和评估命令，确保跨轮次评估的可比性，减少评估漂移。3）**轮次级别的结构化追踪**：每轮都记录候选变更、动机证据、评估指标和决策结果，将优化过程转化为可审计的显式状态转换历史，支持可复现性和可追溯性。

创新点在于其**协议化与通用性**。EPOCH并非针对特定任务的优化循环，而是一个可配置的协议家族，能通过调整角色实现、约束和工件，统一协调提示词调优、超参数微调、基于规则的优化和代码改进等多种异构优化任务。它通过元级别的技能构建机制，根据自由形式的优化目标生成任务特定的协议实例，从而在保持核心结构稳定的同时适应不同部署环境的需求。

### Q4: 论文做了哪些实验？

论文在四个具体任务上对EPOCH协议进行了实证评估：代码改进、超参数微调、提示词优化和基于规则的优化。实验设置遵循统一的高级协议：每个实验运行都从一个任务规范开始，该规范定义了优化目标、最大轮次、重试限制、评估指标以及任务特定约束（如训练/评估数据分离、可见测试集或过拟合阈值）。对于有预留评估数据的任务，调查者角色仅能访问训练数据，而评审者角色基于评估数据做出接受/拒绝决定。

使用的数据集/基准测试根据任务而异，但核心是控制性的任务环境，旨在使轮次级别的行为可观察，以研究基线构建、迭代优化、拒绝与重试行为、评估完整性以及在不同操作约束下的自我终止机制。对比方法方面，论文的重点并非将EPOCH作为特定任务的最先进优化器进行比较，而是评估其作为组织迭代优化的通用协议层的实用性。因此，实验设计旨在测试同一协议核心控制结构能否支持异构的优化工作流。

主要结果和关键指标体现在协议对不同任务的适应性上：在代码改进中，系统在可见测试套件下优化程序逻辑，并在所有测试通过后转向性能优化；在超参数微调中，系统仅调整声明的超参数而保持模型架构固定；在提示词优化中，系统修改提示词构件，同时保持底层语言模型固定并执行泄漏检查；在基于规则的优化中，系统在训练/评估分离的条件下优化符号阈值和优先级关系。这些实验共同表明，EPOCH作为一个共享协议，能够在保持评估的稳定性、可复现性、可追溯性和完整性的同时，支持跨异构组件的协调优化。

### Q5: 有什么可以进一步探索的点？

本文提出的EPOCH协议为异构环境下的多轮系统优化提供了一个结构化的工程框架，但其局限性和未来探索空间依然显著。主要局限性在于当前协议主要针对单一目标的迭代优化，而现实生产系统往往是多组件、多目标协同的复杂系统。未来研究可重点探索将EPOCH扩展至多智能体协调领域，以支持跨训练管道、推理策略、部署监控等子系统的并行或分层优化。具体改进思路包括：设计支持多智能体通信与决策协调的协议扩展，引入系统级评估检查点和全局指标来协调不同智能体的行动；增强协议对动态环境和非稳态目标的适应性，例如允许优化过程中系统组件或评估标准发生变化；此外，可探索将协议与更强大的元优化能力结合，使系统不仅能优化给定组件，还能自主决定优化哪些组件、以何种顺序进行，从而实现从“工件级优化”到“系统级协调”的跨越。这些方向将推动智能体优化从封闭循环迈向开放、可审计的生产系统协同进化。

### Q6: 总结一下论文的主要内容

EPOCH是一种用于异构环境中多轮系统优化的工程协议，旨在解决现有自主代理方法通常局限于特定任务、缺乏统一优化框架的问题。其核心贡献是提出了一个结构化的两阶段协议：首先构建基线，然后进行迭代自我改进。该方法将每一轮优化分解为规划、实施和评估等角色约束阶段，并通过标准化命令接口和轮次跟踪来规范执行。这种设计使得系统能够跨提示词、模型配置、代码和基于规则的组件进行协调优化，同时确保评估的稳定性、可复现性、可追溯性和完整性。实证研究表明，EPOCH适用于生产导向的自主改进工作流，为建立基准和管理多轮自我优化提供了一个通用且实用的协议。
