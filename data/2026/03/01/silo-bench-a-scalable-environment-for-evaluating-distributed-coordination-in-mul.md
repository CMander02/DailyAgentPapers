---
title: "Silo-Bench: A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems"
authors:
  - "Yuzhe Zhang"
  - "Feiran Liu"
  - "Yi Shan"
  - "Xinyi Huang"
  - "Xin Yang"
date: "2026-03-01"
arxiv_id: "2603.01045"
arxiv_url: "https://arxiv.org/abs/2603.01045"
pdf_url: "https://arxiv.org/pdf/2603.01045v1"
categories:
  - "cs.MA"
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Reasoning & Planning"
relevance_score: 8.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Reasoning & Planning"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "Silo-Bench"
  primary_benchmark: "Silo-Bench"
---

# Silo-Bench: A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems

## 原始摘要

Large language models are increasingly deployed in multi-agent systems to overcome context limitations by distributing information across agents. Yet whether agents can reliably compute with distributed information -- rather than merely exchange it -- remains an open question. We introduce Silo-Bench, a role-agnostic benchmark of 30 algorithmic tasks across three communication complexity levels, evaluating 54 configurations over 1,620 experiments. Our experiments expose a fundamental Communication-Reasoning Gap: agents spontaneously form task-appropriate coordination topologies and exchange information actively, yet systematically fail to synthesize distributed state into correct answers. The failure is localized to the reasoning-integration stage -- agents often acquire sufficient information but cannot integrate it. This coordination overhead compounds with scale, eventually eliminating parallelization gains entirely. These findings demonstrate that naively scaling agent count cannot circumvent context limitations, and Silo-Bench provides a foundation for tracking progress toward genuinely collaborative multi-agent systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多智能体大语言模型系统中，智能体在分布式信息环境下进行有效协同计算的核心能力缺失问题。研究背景在于，尽管大语言模型在单任务上表现出色，但其有限的上下文窗口难以处理大规模全局信息，而通过多智能体系统分布式处理信息被视为突破这一瓶颈的潜在途径。然而，现有方法存在明显不足：当前的多智能体基准测试要么预设了固定的通信结构，要么侧重于社会模拟而非计算协作，这引入了归纳偏差，并且未能检验智能体能否为分布式计算问题自主发现并执行有效的协调策略。

因此，本文要解决的核心问题是：在“信息孤岛”（即每个智能体仅持有部分信息）的约束下，现有的基于大语言模型的智能体能否通过自由形式的通信与协作，可靠地整合分布式状态以完成全局计算任务，而非仅仅进行信息交换。论文通过引入Silo-Bench这一可扩展的基准测试环境，系统地评估了智能体在分布式协调中的表现，揭示了其存在的根本性缺陷——通信与推理的脱节。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**上下文限制与分布式推理**以及**多智能体架构与角色无关性**。

在**上下文限制与分布式推理**方面，现有研究主要关注通过扩展上下文窗口或检索增强生成（RAG）来处理大规模信息。例如，SCROLLS、LongBench 和 ∞Bench 等基准测试专注于评估单智能体的长文本检索与理解能力。然而，这些工作主要集中于集中式处理范式，未能衡量多个智能体如何通过分布式协作来整合分散的信息并进行全局推理。本文提出的 Silo-Bench 则填补了这一空白，旨在专门评估多智能体系统在分布式信息下的协同计算能力，而不仅仅是信息交换。

在**多智能体架构与角色无关性**方面，早期工作如 CAMEL 和 MetaGPT 通常依赖于为智能体分配特定的语义角色（如“经理”、“程序员”）并嵌入固定的层次化工作流程中。这类方法虽然在某些领域（如软件工程）有效，但将推理能力与角色先验紧密耦合，难以分离出通信架构本身的贡献。其他研究如基于辩论的系统或混合智能体（Mixture-of-Agents）则常常预设静态的通信拓扑，限制了信息的动态流动。与之不同，Silo-Bench 是一个**角色无关、可配置**的评估环境，它不预设固定角色或通信脚本，而是通过提供高层次任务提示，观察智能体能否动态形成有效的协调协议，从而专注于评估分布式协调机制本身。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Silo-Bench的可配置、可扩展的评估环境来解决多智能体大语言模型系统中分布式协调能力的评测问题。其核心方法是创建一个基于通信复杂性理论的任务空间，通过系统化的实验设计来量化并诊断智能体在分布式计算中的协作瓶颈。

整体框架是一个模块化的执行流水线，包含四个主要阶段：数据分区、智能体初始化、协作执行和指标计算。环境由三个正交维度定义：智能体规模N、通信协议P和语言模型M。任务空间包含30个算法任务，并依据其最优通信复杂性分为三个级别：I级（聚合任务，O(N)通信）、II级（网状网络任务，O(N)通信）和III级（全局重排任务，O(N log N)到O(N^2)通信）。每个任务实例由一个独立的Python生成器程序化地产生随机输入和精确的真实答案，确保可复现性和无限的新实例生成。

关键技术包括：1）**基于通信复杂性的任务分类**：将任务难度根植于严谨的理论基础（如Yao的通信复杂性理论），使得观察到的性能差距可归因于协调需求而非临时性的任务选择。2）**互补的评估指标**：设计了四个核心指标来全面衡量协作效果。成功率（S）衡量收敛到正确答案的智能体比例；部分正确性分数（P）是一个连续度量，用于捕捉部分进展，其与S的差距（P - S）可量化在“推理-整合”阶段而非通信阶段损失的性能；令牌消耗（C）量化每轮通信的计算成本；通信密度（D）捕捉智能体间的交互强度。3）**可配置的协作协议**：支持不同的通信协议（如SFS协议），并在评估流水线中模拟了并行、多轮的交互过程，消息在写入后的下一轮才可见。

创新点在于：首先，提出了“通信-推理鸿沟”这一核心发现，即智能体能自发形成合适的协调拓扑并积极交换信息，但系统性地无法将分布式状态合成为正确答案，且失败定位于推理整合阶段。其次，Silo-Bench环境本身是一个可扩展的基础设施，能够系统地探索智能体规模、协议和模型对协作性能的影响，揭示了协调开销随规模扩大而加剧，最终完全抵消并行化收益的规律。这为追踪迈向真正协作的多智能体系统的进展提供了量化基础。

### Q4: 论文做了哪些实验？

论文实验设置采用三因素析因设计，系统评估了多智能体协调能力。实验在Silo-Bench基准上进行，该基准包含30个算法任务，分为三个通信复杂度等级（Level I、II、III）。实验变量包括：智能体规模（N ∈ {2, 5, 10, 20, 50, 100}）、通信协议（P2P点对点、BP广播、SFS共享文件系统）和语言模型（DeepSeek-V3.1、GPT-OSS-120B、Qwen3-Next-80B-A3B），共构成54种配置，总计1620次实验。所有模型在本地部署，使用默认温度参数和128K上下文窗口。

主要对比方法为单智能体基线（N=1），即单个智能体接收完整全局输入直接作答，用以区分任务固有难度与协调开销。评估指标包括成功率（SR）、部分正确性分数（PCS）、相对协调成本（RCC）、令牌消耗和通信密度。

关键结果如下：
1.  **整体性能**：DeepSeek-V3.1平均成功率最高（36.9%），其次为GPT-OSS-120B（16.9%）和Qwen3（8.2%）。即使最强模型失败率也接近三分之二。
2.  **协调开销主导性能差距**：通过RCC量化，发现协调失败是主因。例如，GPT-OSS-120B在N=2时已损失15-49%的单智能体性能；在N=50时，Level-II和III任务的RCC高达80-100%，表明性能崩溃源于协调失败而非任务本身更难。
3.  **信息整合失败**：PCS与SR出现显著分歧。例如，DeepSeek-V3.1在Level-I任务上平均PCS为88.0%，但SR仅62.0%，差距26个百分点，表明智能体收集了足够信息却无法正确整合。在N≥50的Level-III任务中，SR降至0%而PCS仍有8-16%，进一步证实推理-整合阶段是瓶颈。
4.  **规模与复杂度的乘性恶化**：性能随智能体数量和任务复杂度增加而显著下降。DeepSeek-V3.1的成功率从Level-I的62%降至Level-III的12%；Level-III任务在N≥50时成功率为零，而Level-I任务在N=100时仍高于40%。通信密度随规模扩大而降低，显示协调稀疏化。
5.  **协议偏好差异**：不同模型对通信协议有不同适应性。DeepSeek-V3.1在BP广播下表现最佳（成功率40.4%），GPT-OSS-120B在P2P点对点下最优（20.3%），而SFS共享文件系统在多数情况下表现最差，表明瓶颈在于对共享状态的推理而非通信量。

### Q5: 有什么可以进一步探索的点？

基于论文分析，未来研究可从以下三个方向深入探索。首先，需开发机制使智能体能够自主判断信息完备性，避免“过早提交”问题。论文指出这是最主要的失败模式（37.2%），智能体常在未收集足够数据时便仓促作答。可探索基于置信度估计或动态信息阈值的学习方法。其次，应设计显式的共识协议与同步检查点。研究发现成功案例中往往存在隐式的验证行为，若能将其形式化为轻量级共识算法（如迭代投票或梯度一致性检测），可有效缓解“共识失败”（29.9%）。最后，需实现任务自适应的协作协议优化。智能体虽能自发形成近似最优的通信拓扑（如星型、链式），但常伴随负载不均与冗余通信。未来可结合任务结构分析与模型能力评估，动态选择或生成协作策略，尤其需解决规模扩展时协调开销抵消并行增益的核心矛盾。此外，论文未深入探讨的异质智能体分工、长程推理中的状态维护、以及通信延迟与错误容忍机制，亦是值得拓展的方向。

### Q6: 总结一下论文的主要内容

论文《Silo-Bench》提出了一个可扩展的基准测试环境，用于评估多智能体大语言模型系统中的分布式协调能力。其核心贡献在于揭示了当前多智能体系统存在“通信-推理鸿沟”：智能体虽能自发形成适合任务的协调拓扑并积极交换信息，却无法有效整合分布式状态以得出正确答案。问题定义为探究智能体能否可靠地进行分布式计算，而不仅仅是交换信息。方法上，Silo-Bench 设计了30个算法任务，涵盖三个通信复杂度级别，并通过1,620次实验评估了54种配置。主要结论表明，智能体的失败集中在推理整合阶段，协调开销随规模增加而加剧，最终完全抵消并行化收益，且自发出现的领导者反而会损害复杂任务性能。这一发现证明，单纯增加智能体数量无法突破上下文限制，该研究为开发真正协作的多智能体系统提供了评估基础。
