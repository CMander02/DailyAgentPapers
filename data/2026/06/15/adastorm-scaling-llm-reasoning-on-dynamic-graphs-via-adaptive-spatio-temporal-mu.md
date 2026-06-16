---
title: "AdaSTORM: Scaling LLM Reasoning on Dynamic Graphs via Adaptive Spatio-Temporal Multi-Agent Collaboration"
authors:
  - "Bing Hao"
  - "Ruijie Wang"
  - "Haodong Qian"
  - "Yunlong Chu"
  - "Yuhang Liu"
  - "Yumeng Lin"
  - "Minglai Shao"
  - "Jianxin Li"
date: "2026-06-15"
arxiv_id: "2606.16328"
arxiv_url: "https://arxiv.org/abs/2606.16328"
pdf_url: "https://arxiv.org/pdf/2606.16328v1"
github_url: "https://github.com/irisorchid107/AdaSTORM"
categories:
  - "cs.AI"
tags:
  - "多智能体协作"
  - "动态图推理"
  - "图分区"
  - "推理扩展"
  - "LLM Agent"
relevance_score: 8.5
---

# AdaSTORM: Scaling LLM Reasoning on Dynamic Graphs via Adaptive Spatio-Temporal Multi-Agent Collaboration

## 原始摘要

Large Language Models (LLMs) demonstrate remarkable potential in dynamic graph reasoning, but suffer from a scaling bottleneck: current models can only handle graphs with tens of nodes, constrained by exponential reasoning overhead and finite context windows. While multi-agent systems (MAS) offer collective reasoning and topology-aware orchestration, capabilities naturally suited for graph-structured tasks, their application to dynamic graphs remains unexplored. This paper presents Scaling LLM Reasoning on Dynamic Graphs via Adaptive Spatio-Temporal Multi-Agent Collaboration (AdaSTORM), a framework that reformulates large-scale dynamic graph reasoning into two stages: (i) Adaptive Partitioning, partitioning large-scale dynamic graphs into subregions that match the model's reasoning capacity while minimizing inference cost; and (ii) Collaborative Reasoning, aligning graph partition topologies with a spatio-temporal decoupled multi-agent architecture. AdaSTORM is the first multi-agent framework tailored for dynamic graph reasoning. Extensive experiments show that AdaSTORM successfully breaks through the scaling bottleneck, scaling reasoning to thousand-node graphs with over 90% accuracy across several large-scale dynamic graph settings without external tools, significantly outperforms seven competitive baselines. Furthermore, it achieves state-of-the-art accuracy on existing benchmarks and generalizes robustly to real-world datasets. The source code is available at: https://github.com/irisorchid107/AdaSTORM/.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前大型语言模型在动态图推理中面临的扩展瓶颈问题。研究背景是，虽然LLMs在图结构数据推理上展现出潜力，尤其是在捕获关系数据时间演变的动态图推理这一关键前沿领域。现有方法（包括基准测试和方法开发）存在显著不足：它们只能处理数十个节点的中小规模图。这源于一个根本性的扩展瓶颈：随着图规模增长，结构复杂度迅速超出单模型自身的推理能力和上下文窗口上限，导致严重幻觉和性能灾难性崩塌。虽然多智能体系统（MAS）通过将复杂问题分解为协作子任务，突破了单LLM的推理能力和上下文窗口限制，且其通信架构天然模拟了图的结构特性，但标准的多智能体范式（如链式和辩论式）无法处理由图规模触发的组合爆炸，因为它们通常在全局处理整个图拓扑，缺乏大规模图分区机制。本文要解决的核心问题，就是如何使LLM的推理能力扩展到大规模动态图（千节点级别）。为此，论文提出了AdaSTORM框架，通过自适应分区和时空解耦的多智能体协作，将大规模动态图推理重构为两个阶段，从而突破扩展瓶颈。

### Q2: 有哪些相关研究？

相关研究可分为以下三类：

1. **LLMs for Graphs**：现有工作包括静态图基准（如GraphInstruct、GraphArena、GraphOmni）和动态图基准（如LLM4DyG、LLMTM）。方法上分为GNN增强的LLM（注入结构嵌入但跨任务泛化受限）和文本平铺LLM（将图序列化但受限于指数级推理开销）。AdaSTORM通过自适应多智能体编排突破了这些架构限制，首次将推理扩展到千节点动态图。

2. **多智能体系统（MAS）**：现有MAS已应用于软件开发、具身控制等领域，采用链、树或图等结构化拓扑编排专用智能体。AdaSTORM首次将这种拓扑对齐特性应用于动态图推理，提出时空解耦的多智能体架构，实现了集体推理与图拓扑的自然匹配。

3. **图分割**：传统方法将分割视为NP-hard离散优化（依赖启发式或近似），神经分割方法虽引入连续图割但依赖静态分区数。AdaSTORM提出自适应分割器，动态确定最优区域数量，在保持高质量结构分割的同时最小化推理成本，这是与现有工作的关键区别。

### Q3: 论文如何解决这个问题？

AdaSTORM将大规模动态图推理分解为两个阶段来解决扩展性问题。第一阶段是自适应分区，核心在于通过强化学习动态地将大规模图分解为与模型推理能力匹配的子区域，同时最小化推理成本。这包含三个关键模块：**容量估计器**通过多模态联合表示（融合LM编码的任务查询、模型语义概要、GNN拓扑编码和可学习隐向量）预测每个子区域能被目标模型成功解决的可行性；**成本估计器**通过程序化追踪多智能体执行过程来计算推理成本（即智能体调用次数）；**自适应分区器**则基于这两项反馈，通过策略网络选择区域拆分或节点迁移两种动作来优化分区，其奖励函数同时考虑成本降低、可行性改善以及惩罚过度分割和无效调整，并通过策略梯度进行训练。第二阶段是协同推理，将分区拓扑与时空解耦的多智能体架构对齐。**空间智能体**分配到各子区域处理静态局部拓扑推理和跨区域通信；**时间智能体**处理动态事件，强制执行时序约束，可充当搜索空间预过滤器或空间推理结果的后验证器。两者通过LangGraph维护的共享全局状态并行执行、交换结果并联合更新输出，实现无外部工具的准确高效推理。

### Q4: 论文做了哪些实验？

论文进行了三组实验。**实验设置**：使用 DeepSeek-R1-Distill-Qwen-7B/14B/32B 作为骨干，对比基线包括独立 LLM（DeepSeek-V4-Flash、GPT-4o mini 等）、链式/辩论式多智能体架构以及图推理专用框架（GraphWiz 等）。**数据集/基准测试**：在合成动态图（节点数 N=500/800/1000，基于 SBM 生成）和五个真实数据集（Wikipedia、Reddit、Enron、Flights、UNTrade）上评估。**主要结果**：
1. **大规模动态图任务**：AdaSTORM 突破缩放瓶颈，成功推理千节点图，在社区检测（N=500 时 71%）、连通分量（90%）、可达性（90%）和时序模体计数（100%）上远超基线；而基线模型在 N>100 时几乎完全失效。2. **小规模基准**：在现有图推理基准上达到 SOTA。3. **真实世界泛化**：在 Reddit 上社区检测 35%、连通分量 73%、可达性 65%、模体计数 100%；在 Enron 上连通分量达 95%。**消融实验**：容量估计器使准确率提升（N=500 从 61% 到 90%）并降低 token 消耗（33,756→16,723）；自适应分区器和时空解耦均验证了贡献。

### Q5: 有什么可以进一步探索的点？

针对AdaSTORM的局限性，未来可探索以下方向：首先，当前方法高度依赖子图分解与协作，对强语义依赖或模糊目标（如知识图谱问答、开放域推理）的适配性不足，可引入外部知识库或微调模块增强语义理解。其次，将LLM视为黑盒导致局部推理错误累积，建议设计可解释性中间验证机制（如动态置信度阈值），或采用轻量级代理模型进行路由与纠错。此外，分区的容量估计未考虑时序依赖的异质性，可融合图注意力网络或神经符号方法自适应调整粒度。最后，多智能体通信开销随规模超线性增长，可探索层次化协作或稀疏化信息传递策略。跨领域扩展（如金融时序图、生物分子网络）与性能-成本感知的动态资源分配，也是值得深化的方向。

### Q6: 总结一下论文的主要内容

该论文提出了AdaSTORM框架，旨在解决大语言模型在动态图推理中面临的规模瓶颈。当前模型仅能处理数十个节点的图，受限于指数级推理开销和有限上下文窗口。AdaSTORM通过两阶段方法实现突破：自适应分区阶段将大规模动态图划分为与模型推理能力匹配的子区域以最小化推理成本；协同推理阶段将图分区拓扑与时空解耦的多智能体架构对齐。这是首个专为动态图推理定制的多智能体框架。实验表明，AdaSTORM成功将推理能力扩展至数千节点图，在多个大规模动态图设置中达到超过90%的准确率，显著优于七种基线方法，并在现有基准上实现了最先进的准确率，同时展现了鲁棒的真实世界泛化能力。该工作证明了多智能体协作在动态图推理中的有效性，具有重要实践价值。
