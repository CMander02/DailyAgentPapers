---
title: "FlowCompile: An Optimizing Compiler for Structured LLM Workflows"
authors:
  - "Junyan Li"
  - "Zhang-Wei Hong"
  - "Maohao Shen"
  - "Yang Zhang"
  - "Chuang Gan"
date: "2026-05-13"
arxiv_id: "2605.13647"
arxiv_url: "https://arxiv.org/abs/2605.13647"
pdf_url: "https://arxiv.org/pdf/2605.13647v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent Workflow"
  - "多智能体系统"
  - "编译优化"
  - "延迟-准确性权衡"
  - "设计空间探索"
  - "架构搜索"
relevance_score: 9.0
---

# FlowCompile: An Optimizing Compiler for Structured LLM Workflows

## 原始摘要

Structured LLM workflows, where specialized LLM sub-agents execute according to a predefined graph, have become a powerful abstraction for solving complex tasks. Optimizing such workflows, i.e., selecting configurations for each sub-agent to balance accuracy and latency, is challenging due to the combinatorial design space over model choices, reasoning budgets, and workflow structures. Existing cost-aware methods largely treat workflow optimization as a routing problem, selecting a configuration at inference time for each query according to the accuracy-latency objective used during training. We argue that structured LLM workflows can also be optimized from a compilation perspective: before deployment, the system can globally explore the workflow design space and construct a reusable set of workflow-level configurations spanning diverse accuracy-latency trade-offs. Drawing inspiration from machine learning compilers, we introduce FlowCompile, a structured LLM workflow compiler that performs compile-time design space exploration to identify a high-quality, reusable trade-off set. FlowCompile decomposes a workflow into sub-agents, profiles each sub-agent under diverse configurations, and composes these measurements through a structure-aware proxy to estimate workflow-level accuracy and latency. It then identifies diverse high-quality configurations in a single compile-time pass, without retraining or online adaptation. Experiments across diverse workflows and challenging benchmarks show that FlowCompile consistently outperforms heuristically optimized workflow configurations and routing-based baselines, delivering up to 6.4x speedup. The compiled configuration set further serves as a reusable optimization artifact, enabling flexible deployment under varying runtime preferences and supporting downstream selection or routing.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决结构化大语言模型工作流优化中的核心难题。随着多步推理任务日益复杂，结构化工作流（由多个专用子代理按预定义图执行组成）已成为解决复杂任务的有效抽象。现有方法普遍采用基于路由的范式，在推理时为每个查询选择配置，但其优化视角存在根本局限：**现有方法主要将工作流优化视为推理时的路由问题**，即根据训练时设定的精度-延迟目标，在运行时为每个查询选择单一配置。这种方法的不足在于：(1) 组合设计空间巨大——涉及模型选择、推理预算和工作流结构，穷举搜索不可行；(2) 路由策略通常针对单个权衡点，无法适应部署时多样化的精度-延迟偏好；(3) 需要针对不同目标重复训练或在线优化，缺乏可复用性。本文受机器学习编译器启发，提出将工作流优化视为**编译期问题**：在部署前系统性地全局探索工作流设计空间，构建覆盖多样精度-延迟权衡点的可复用配置集合。核心创新在于通过结构感知的组合代理，将子代理配置文件提升为工作流级性能估计，实现一次编译即可生成可复用、高质量、涵盖多权衡点的配置集，无需重新训练或在线适配。

### Q2: 有哪些相关研究？

相关工作主要分为两类。第一类是结构化LLM工作流优化，代表方法包括MaAS、MasRouter、DAAO等，它们采用基于路由的范式，在推理时为每个查询选择配置。LLMSELECTOR与本文最为相关，它也利用模块级评估优化多模块工作流，但选择的是最大化准确率的单一静态配置，未显式建模成本。DSPy也将LM管道优化视为编译，但主要优化提示和示例以提高准确率。本文与这些方法互补，创新点在于采用编译器风格的编译时全局设计空间探索，无需重训练或在线自适应即可生成一组可复用的配置，覆盖准确率-延迟权衡。第二类是机器学习编译器，如TVM、AutoTVM和Ansor，它们通过分解计算图并搜索实现选择来优化系统级指标。本文借鉴这种编译器式分解思想，但针对不同的目标：这些编译器保持模型输出质量不变，仅优化延迟；而本文同时优化准确率和延迟，输出是一组操作点而非单一实现，并使用多目标优化指标评估权衡质量。

### Q3: 论文如何解决这个问题？

FlowCompile通过一个三阶段编译器式管道解决结构化LLM工作流的组合优化问题。首先,对于每个子代理,编译器使用工作流跟踪记录并采用LLM-as-a-judge过滤,从验证集诱导出子代理级数据集作为伪标签,然后遍历所有模型和推理预算组合进行性能剖析,记录每个配置的准确率和延迟,形成可复用的成本模型。其次,FlowCompile提出一种轻量级、训练无关的结构感知代理来估计工作流级性能:准确率根据工作流图的结构语义(串行乘积、并行OR/AND组合、条件分支等规则)递归计算,延迟则在边缘部署顺序执行模型下依据执行概率加权求和。最后,编译器执行设计空间探索:先对子代理内配置进行帕累托剪枝,保留非支配配置,再枚举剩余组合,用代理估计性能并应用非支配排序得到覆盖准确率-延迟权衡前沿的编译配置集。该配置集可直接用于延迟约束、偏好或路由场景下的部署选择,无需重新编译。

### Q4: 论文做了哪些实验？

论文进行了全面的实验验证。实验在单H100 GPU上使用vLLM推理引擎，评估指标包括任务准确率和端到端延迟，并采用期望效用作为偏好感知标量评估指标。设计空间覆盖模型大小（Qwen-3系列0.6B-14B）、推理预算（10-16000 tokens）和工作流结构（基于AFlow）三个维度。数据集包括数学推理（GSM8K、MATH-500）、多跳问答（HotpotQA）和代码推理（LiveCodeBench）四个基准，构建了互斥的配置分析集和评估集。对比方法分为三类：单模型基线（Qwen3-32B、QwQ-32B）、固定工作流基线和路由基线（KNN Router、MaAS等），还有两个偏好感知路由基线。主要结果：（1）代理质量验证：代理估计与实测前沿高度一致，平均Spearman相关系数达0.96（延迟）和0.92（准确率），平均成对一致性0.95（延迟）和0.90（准确率）；（2）准确率-延迟权衡：FlowCompile在可比或更高准确率下实现更低延迟，准确率优先配置平均获得3.4倍加速（LiveCodeBench达6.4倍），延迟优先配置平均获得12.7倍加速；（3）偏好感知评估：在异构偏好设置下，FlowCompile在所有基准上取得最高期望效用（平均85.5），超越最强基线7.9分；（4）跨基准迁移实验显示子代理配置可复用；（5）消融实验表明扩展设计空间（模型+预算+结构）持续提升性能，而代理质量对参考模型选择具有鲁棒性。

### Q5: 有什么可以进一步探索的点？

FlowCompile在编译时全局搜索工作流配置，但在面对动态变化的任务分布或实时反馈时，其静态的编译优化可能无法快速适应。未来研究可探索在线自适应机制，例如结合轻量级路由或细粒度动态调整，在运行时根据具体查询特征选择或微调预编译的配置。此外，当前方法将子代理的配置视为独立的选择，忽略了子代理间可能存在的深层交互（如输出质量依赖和错误传播）。可以通过引入更复杂的依赖建模（如概率图或因果模型）来更精确地估计工作流级性能。另一个方向是扩展到非结构化或异构代理的组合，以及支持多目标优化（如内存、能耗与延迟的权衡），从而增强编译器在处理复杂真实场景时的泛化性和鲁棒性。

### Q6: 总结一下论文的主要内容

FlowCompile针对结构化LLM工作流（由多个专业子代理按预定义图执行）的优化问题，提出了一种编译优化方法。现有方法通常将工作流优化视为推理时的路由问题，在组合复杂的设计空间（包括模型选择、推理预算和工作流结构）中难以平衡准确性和延迟。FlowCompile将工作流优化视为编译问题：在部署前全局探索工作流设计空间，构建可重用的工作流级配置集，覆盖不同的准确性-延迟权衡。它通过将工作流分解为子代理、在多种配置下分析每个子代理，并使用结构感知代理组成这些测量结果来估计工作流级准确性和延迟，从而在一次编译过程中识别多样化的高质量配置，无需重新训练或在线适应。实验表明，FlowCompile在多个工作流和基准测试中一致优于启发式优化配置和基于路由的基线，实现高达6.4倍的加速。其编译配置集可作为可重用的优化产物，支持在不同运行时需求下灵活部署和下游选择。该工作为未来LLM应用提供了工作流编译的系统抽象，有效管理效率、可控性和适应性。
