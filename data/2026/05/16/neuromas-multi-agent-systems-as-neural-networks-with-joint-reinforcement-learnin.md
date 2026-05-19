---
title: "NeuroMAS: Multi-Agent Systems as Neural Networks with Joint Reinforcement Learning"
authors:
  - "Haoran Lu"
  - "Luyang Fang"
  - "Wenxuan Zhong"
  - "Ping Ma"
date: "2026-05-16"
arxiv_id: "2605.16757"
arxiv_url: "https://arxiv.org/abs/2605.16757"
pdf_url: "https://arxiv.org/pdf/2605.16757v1"
categories:
  - "cs.AI"
  - "cs.MA"
  - "stat.ME"
  - "stat.ML"
tags:
  - "多智能体系统"
  - "神经网络架构"
  - "联合强化学习"
  - "LLM智能体"
  - "可扩展性"
  - "层次化分解"
relevance_score: 9.0
---

# NeuroMAS: Multi-Agent Systems as Neural Networks with Joint Reinforcement Learning

## 原始摘要

Multi-agent language systems are often built as hand-designed workflows, where agents are assigned semantic roles and communication protocols are specified in advance. We propose NeuroMAS, a method that first treats a multi-agent language system as a trainable and scalable neural-network-like architecture with LLM agents as nodes and intermediate textual signals as edges. In NeuroMAS, agent nodes are role-free but structure-aware: the topology only determines how information can flow in general, while reinforcement learning training determines how nodes communicate, specialize, and coordinate. This formulation shifts multi-agent design from workflow engineering toward architecture design, where depth, width, connectivity, and growth protocol become scalable sources of capability. Further, we provide a theoretical perspective showing why such modular textual computation is more parameter-efficient when tasks admit hierarchical decompositions. Experiments show that NeuroMAS improves significantly over both inference-time and trained multi-agent baselines. We further find that organizational scaling is path-dependent: larger systems can be challenging to train from scratch, but become feasible when grown progressively from smaller trained systems. These results suggest that learned neural multi-agent systems are a promising scaling axis for LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文提出了一种名为NeuroMAS的框架，旨在解决当前基于大语言模型的多智能体系统中组织方式与智能体参数优化脱节的问题。研究背景是，LLM虽在多种任务中表现优异，但面对长程执行、复杂推理和领域自适应时仍显不足，且单纯扩大模型规模代价高昂。现有方法如基于提示或工作流的多智能体系统，通常由人工指定智能体的角色（如规划者、求解者等）和通信协议，形成了固定的工作流，但组织本身并未作为可扩展、可优化的对象。尽管有研究尝试优化工作流或拓扑，但大多将组织设计与智能体训练分离，缺乏统一优化的框架。本文核心要解决的是：如何将多智能体系统的组织结构与智能体内的可训练参数作为一个整体进行端到端的联合优化，使得智能体的交流、专业分工和协调能够通过强化学习自动涌现，从而将多智能体设计从手工工作流工程转变为可扩展的神经拓扑设计，开辟一种新的能力扩展维度。

### Q2: 有哪些相关研究？

相关工作可分为四类。**结构化单模型推理**方面，CoT、Self-Consistency等方法通过改变测试时计算提升推理，但其结构是人工指定且仅用于推理；NeuroMAS则在可扩展网络架构中训练多语言策略交换文本状态。**工程化多智能体工作流**如AutoGen、MetaGPT等依赖人工指定角色、提示和通信协议；NeuroMAS将智能体模块作为可训练组件，而非固定工作流中的参与者。**智能体组织优化**方面，GPTSwarm、MASS等优化提示或拓扑，但底层LLM保持冻结；NeuroMAS在给定拓扑下训练智能体模块为随机语言策略，并研究不同拓扑族的性能变化。**训练多智能体协作**中，MALT、CoLLM-CC训练特定管道（如生成器-验证器-精炼器），但NeuroMAS的节点无角色语义（非生成器/验证器等固定身份），且架构支持不同深度、宽度和增长协议，而非固定角色管道。总之，NeuroMAS结合了可训练的智能体内语言策略与可扩展的多智能体拓扑设计，区别于冻结智能体工作流、外部组织优化或固定角色协作训练。

### Q3: 论文如何解决这个问题？

NeuroMAS将多智能体语言系统重构为一种可训练、可扩展的类神经网络架构。其核心方法是将LLM智能体视为节点，中间生成的文本信号作为边，构建一个前馈式的分层拓扑结构。架构设计上，所有节点是“无角色”但“结构感知”的：不预先分配如规划者、求解者等语义角色，节点仅知道自身在拓扑中的层数和位置以及消息格式要求。训练过程通过共享的终端奖励（最终答案的奖励）对全部节点进行联合强化学习优化，使用REINFORCE算法计算每个节点输出文本的对数概率梯度，节点参数（通过LoRA适配器实现）分别更新，但共享同一系统级目标。关键技术包括：参数高效的节点实例化——所有节点共享同一个冻结的基座LLM，仅通过各自的LoRA适配器参数实现差异化；以及渐进式增长协议——将已训练的小型拓扑通过复用已有节点参数并初始化新节点，逐步扩展为更大系统，从而解决大型系统从头训练困难的问题。该方法的创新点在于将多智能体系统设计从手工流程工程转向架构设计，让拓扑结构（深度、宽度、连接性）成为可扩展的能力来源，并通过训练自组织地涌现出节点间的专业分工与协作。

### Q4: 论文做了哪些实验？

论文通过三组实验评估NeuroMAS。首先，在六个基准测试上比较推理、领域知识和代码生成性能：ARC-Challenge（科学问答）、Navigate（空间推理）、MMLU的三个子集（抽象代数、大学物理、专业医学）和HumanEval（代码生成）。使用Qwen3-0.6B作为冻结骨干模型，通过LoRA适配器引入可训练参数，并用REINFORCE优化。对比方法分为固定骨干基线（直接提示、Self-Refine、Self-Check、MoA、GoA、AgentNet、GPTSwarm）和训练骨干基线（单LLM强化学习、MALT、CoLLM-CC）。主要结果显示，NeuroMAS-3（3次LLM调用，6.9M参数）在所有六项任务上均优于最强固定骨干基线，例如ARC提升10.5个百分点（56.5% vs 46.0%），大学物理提升18.6%（44.1% vs 25.5%）；相比单LLM强化学习，NeuroMAS-3提升10.5-19.6个百分点；在NeuroMAS变体中，NeuroMAS-3在ARC、物理和医学上最佳，NeuroMAS-7在导航、代数和HumanEval上最佳。其次，更换骨干为Gemma-3-1B-IT在ARC上验证鲁棒性，NeuroMAS-3以44.5%准确率（3次调用）超越所有固定基线（GPTSwarm为43.0%，11次调用）和训练基线。最后，研究组织缩放：更大拓扑（NeuroMAS-5、NeuroMAS-7）需逐步从较小已训练系统生长才能有效，直接从头训练较困难。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于其假设任务具有可分解的层次结构，这在现实复杂开放场景中未必成立。未来可探索以下方向：1) 引入动态拓扑学习，使网络结构能随任务需求自适应调整，而非固定静态拓扑；2) 研究跨任务的知识迁移与持续学习机制，避免每次训练从头开始；3) 设计更高效的联合训练算法，以应对大规模节点带来的组合爆炸和信用分配难题；4) 探索多模态信号作为节点间通信媒介，突破纯文本的信息瓶颈；5) 结合因果推断与可解释性分析，理解节点如何形成专业化分工与协作策略。此外，将NeuroMAS与外部工具、知识库或记忆模块集成，可能进一步增强其复杂推理能力。这些方向有望推动神经多智能体系统从理论原型迈向实用化部署。

### Q6: 总结一下论文的主要内容

NeuroMAS提出了一种将多智能体语言系统视为可训练、可扩展的类神经网络架构的方法。传统多智能体系统依赖人工设计的角色和通信协议，而NeuroMAS将LLM智能体作为节点，中间文本信号作为边，构成一个结构感知但角色无关的拓扑网络。关键创新在于：拓扑结构仅决定信息流动的通用方式，而节点间的通信、专业化和协调行为通过联合强化学习自动涌现。该方法将多智能体系统设计从工作流工程转向架构设计，深度、宽度、连通性和增长协议成为可扩展的能力来源。理论分析表明，对于具有层次分解结构的任务，这种模块化文本计算更参数高效。实验结果显示，NeuroMAS在推理和代码生成任务上显著优于推理时方法及训练过的多智能体基线，并发现组织缩放具有路径依赖性：从零训练大规模系统困难，但从训练好的小系统渐进式增长则可行。这项工作的意义在于证明了围绕固定语言模型的组织方式本身可以成为可训练的能力来源，为LLM扩展提供了新维度。
