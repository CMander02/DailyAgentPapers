---
title: "EMS: Multi-Agent Voting via Efficient Majority-then-Stopping"
authors:
  - "Yiqing Liu"
  - "Hantao Yao"
  - "Wu Liu"
  - "Yongdong Zhang"
date: "2026-04-03"
arxiv_id: "2604.02863"
arxiv_url: "https://arxiv.org/abs/2604.02863"
pdf_url: "https://arxiv.org/pdf/2604.02863v1"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "投票聚合"
  - "推理效率"
  - "资源调度"
  - "置信度建模"
  - "动态更新"
relevance_score: 7.5
---

# EMS: Multi-Agent Voting via Efficient Majority-then-Stopping

## 原始摘要

Majority voting is the standard for aggregating multi-agent responses into a final decision. However, traditional methods typically require all agents to complete their reasoning before aggregation begins, leading to significant computational overhead, as many responses become redundant once a majority consensus is achieved. In this work, we formulate the multi-agent voting as a reliability-aware agent scheduling problem, and propose an Efficient Majority-then-Stopping (EMS) to improve reasoning efficiency. EMS prioritizes agents based on task-aware reliability and terminates the reasoning pipeline the moment a majority is achieved from the following three critical components. Specifically, we introduce Agent Confidence Modeling (ACM) to estimate agent reliability using historical performance and semantic similarity, Adaptive Incremental Voting (AIV) to sequentially select agents with early stopping, and Individual Confidence Updating (ICU) to dynamically update the reliability of each contributing agent. Extensive evaluations across six benchmarks demonstrate that EMS consistently reduces the average number of invoked agents by 32%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体大语言模型系统中多数投票机制存在的计算效率低下问题。研究背景在于，尽管多智能体系统通过聚合多样化的推理路径能够提升复杂任务的解决能力，但传统的多数投票方法通常要求所有智能体完成推理后才开始聚合，导致大量冗余计算。现有方法的不足在于，它们遵循“先推理、后聚合”的范式，一旦多数共识达成，后续智能体的推理就变得多余，这造成了显著的计算开销，尤其是在涉及大量智能体或昂贵的大语言模型推理时。

本文要解决的核心问题是如何在保持多数投票准确性的前提下，减少多智能体系统中的冗余推理。为此，论文将多数投票重新定义为一种可靠性感知的智能体调度问题，并提出了高效多数即停方法。该方法的核心思想是通过估计每个智能体在特定任务上的可靠性，优先查询高可靠性智能体，从而在达成多数共识时立即停止推理过程，避免不必要的计算。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及多智能体系统、高效多智能体推理以及多智能体投票与聚合三个类别。

在多智能体系统方面，以AutoGen为代表的框架通过角色分配和任务分解实现结构化协作，而多智能体辩论等方法则通过相互批判来提升输出质量。这些研究侧重于通过协作提升任务性能，但较少关注推理效率，特别是如何减少决策过程中的冗余智能体调用。

在高效多智能体推理方面，现有工作通过自适应路由、选择性调用或优化辩论中的通信来提升效率。例如，GroupDebate通过分组讨论共享中间结果来降低令牌成本，DOWN则仅在初始置信度低时才激活辩论。这些方法主要优化交互效率，但并未直接利用多数共识结构来实现提前终止。

在多智能体投票与聚合方面，多数投票因其简单有效而成为主流决策规则。近期研究表明，多数投票贡献了多智能体辩论中的主要性能增益，且对于推理类任务尤为有效。然而，现有方法通常遵循“先推理后聚合”的模式，导致大量计算浪费，因为共识往往在所有智能体完成推理前就已达成。

本文与上述工作的核心区别在于，它将多数投票重新定义为**一个可靠性感知的智能体调度问题**。本文提出的EMS方法通过智能体置信度建模、自适应增量投票和个体置信度更新三个组件，实现了基于任务感知可靠性的智能体优先级排序，并在达到多数共识时立即停止推理流程，从而直接解决了现有方法在计算效率上的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“高效多数即停”（EMS）的框架来解决传统多数投票中所有代理必须完成推理才能聚合所导致的计算冗余问题。该框架将多代理投票重新构建为一个可靠性感知的代理调度问题，其核心思想是优先调用高可靠性的代理，并在达到多数共识时立即停止推理流程，从而显著减少被调用的代理数量。

整体框架包含三个关键技术组件，形成一个动态的、自适应的投票循环：
1.  **代理置信度建模（ACM）**：此模块负责为每个查询计算每个代理的置信度分数，以确定投票顺序。它结合了两种策略：一是基于历史表现的“历史可靠性”，计算代理过往投票与最终共识一致的比例（\(S^{h}_{i,j} = c_j / v_j\)）；二是基于问题语义的“查询自适应语义可靠性”，通过对比当前查询嵌入与代理历史成功回答的查询嵌入的相似度来衡量（\(S^{q}_{i,j}\)）。这两种分数可以单独或结合使用，以生成一个按预期可靠性降序排列的代理序列 \(\hat{\mathcal{A}}_i\)。

2.  **自适应增量投票（AIV）**：这是执行投票的核心模块。它基于ACM提供的排序序列，以增量方式进行投票。首先，它调用前 \(\tau = \lceil (N+1)/2 \rceil\) 个代理（即构成多数所需的最小数量）进行初始投票。如果这些代理的回答完全一致，则立即达成共识并停止。否则，系统将按顺序继续调用下一个代理，并在每一步检查当前所有已收集的投票中是否有任何答案达到了多数票（\(\geq \tau\)）。一旦满足条件，投票立即终止，并输出该共识答案。若遍历所有代理仍未达成绝对多数，则退化为标准的多数票（或相对多数）决策。

3.  **个体置信度更新（ICU）**：在每次投票完成后，此模块动态更新参与投票的代理的置信度状态 \(\Phi_j = (c_j, v_j, \mathcal{H}_j)\)。具体地，增加代理的参与计数 \(v_j\)；如果其投票与最终共识一致，则增加正确计数 \(c_j\)，并将当前查询的语义嵌入存入其历史缓冲区 \(\mathcal{H}_j\)。这种在线更新机制使得ACM能够基于最新表现不断优化后续查询的代理排序，形成一个自我改进的闭环。

该方法的创新点在于：首先，将并行投票重构为**顺序决策问题**，并引入了**“多数即停”机制**，从根本上避免了冗余计算。其次，提出了**双视角的代理可靠性评估**（历史表现与语义适配），实现了任务感知的智能调度。最后，通过**动态状态更新**，使系统能够持续学习并优化代理调度策略。实验表明，EMS平均能减少32%的代理调用，在保证决策质量的同时显著提升了推理效率。

### Q4: 论文做了哪些实验？

论文在六个基准数据集上进行了实验：数学推理任务（AQuA、Math500、GSM8K）和通用知识任务（MMLU、GPQA Diamond、CommonsenseQA）。实验设置使用了一个包含9个异构大语言模型的代理池，涵盖OpenAI、Google、Anthropic、DeepSeek、Meta和Alibaba的模型，所有推理通过云悟API平台进行。对比方法包括：单代理思维链、自洽性采样、简单多数投票、基于历史权重的加权投票以及基于自信度的加权投票。论文提出的EMS框架包含两个变体：基于历史可靠性的EMS-Rel和基于查询语义相似性的EMS-Sim。

主要结果显示，所有多数投票方法均优于单代理推理。EMS变体在保持高准确率的同时显著提升了效率。具体而言，最佳EMS变体的平均准确率达到86.38%，仅略低于简单多数投票的最高准确率86.61%。关键效率指标方面，EMS-Rel和EMS-Sim将平均调用的代理数量从9.00个分别减少到6.10个和6.19个，降低了约32%。此外，消融实验验证了基于共识的早停机制的重要性：随机早停策略在保持相同准确率（86.38%）的同时将平均调用代理数降至6.52个，而未经共识检查的固定随机选择5个代理的策略则导致准确率下降至84.37%。代理排序策略分析表明，基于可靠性的排序能进一步减少调用次数，EMS-Rel的平均调用数最低（6.10个）。自适应增量投票的分析显示，在较简单任务上，初始投票阶段（前5个代理）已对大部分查询达成共识（例如GSM8K上为81.1%），从而减少了冗余计算。最后，代理池规模敏感性分析表明，当池大小从9增加到13时，准确率提升有限（GPQA上仅提高1.12%），但平均调用代理数增长受早停机制有效控制。

### Q5: 有什么可以进一步探索的点？

该论文提出的EMS框架虽然有效提升了多智能体投票的效率，但其局限性和未来探索方向值得深入挖掘。首先，当前智能体排序主要依赖历史表现和语义相似性等相对简单的信号，未来可探索更复杂的调度策略，例如引入在线学习机制，在投票过程中实时评估智能体对当前任务特定子问题的擅长程度，或结合元学习来预测智能体在新任务上的泛化可靠性。其次，框架假设智能体之间相互独立，未考虑协作与知识共享，未来可研究如何在提前终止的机制下融入智能体间的交互与辩论，以在达成多数共识的同时提升决策质量。此外，EMS的效率增益在智能体可靠性差异不大时可能受限，可探索动态阈值机制，根据任务难度和共识形成速度自适应调整停止条件。最后，将EMS扩展到更复杂的决策场景，如多轮对话或动态环境下的持续决策，也是值得探索的方向。

### Q6: 总结一下论文的主要内容

该论文针对多智能体投票中传统方法需等待所有智能体完成推理才进行聚合、导致计算冗余的问题，提出了一种高效的多数即停止（EMS）框架。其核心贡献是将多智能体投票重新定义为可靠性感知的智能体调度问题，旨在多数共识达成后立即终止推理流程，从而显著提升效率。方法上，EMS包含三个关键组件：智能体置信度建模（ACM）利用历史表现和语义相似度估计智能体可靠性；自适应增量投票（AIV）基于可靠性优先级顺序调用智能体并实现早期停止；个体置信度更新（ICU）动态更新参与智能体的可靠性估计。实验在六个基准测试上表明，EMS平均减少了32%的智能体调用数量，在保持决策准确性的同时大幅降低了计算开销。
