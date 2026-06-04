---
title: "Streaming Communication in Multi-Agent Reasoning"
authors:
  - "Zhen Yang"
  - "Xiaogang Xu"
  - "Wen Wang"
  - "Cong Chen"
  - "Xander Xu"
  - "Ying-Cong Chen"
date: "2026-06-03"
arxiv_id: "2606.05158"
arxiv_url: "https://arxiv.org/abs/2606.05158"
pdf_url: "https://arxiv.org/pdf/2606.05158v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "流式通信"
  - "推理加速"
  - "大规模语言模型"
  - "智能体推理"
  - "流水线架构"
  - "步骤级缩放定律"
relevance_score: 9.0
---

# Streaming Communication in Multi-Agent Reasoning

## 原始摘要

Multi-agent reasoning systems adopt a "generate-then-transfer" paradigm that forces end-to-end latency to scale linearly with pipeline depth. We introduce StreamMA, a multi-agent reasoning system that streams each reasoning step to downstream agents as soon as it is generated, pipelining adjacent agents and thus reducing latency. Surprisingly, this pipelining also improves effectiveness: because multi-step reasoning quality is non-uniform and early steps are more reliable than later ones, working with these reliable early steps instead of the full chain prevents error-prone late steps from misleading downstream agents. We formalize both advantages with the first closed-form joint analysis of stream, serial, and single protocols, deriving the effectiveness ordering, speedup upper bound, and cost ratio. Across eight reasoning benchmarks spanning mathematics, science, and code, two frontier LLMs (Claude Opus 4.6 and GPT-5.4), and three topologies (Chain, Tree, Graph), StreamMA outperforms both baselines (avg. +7.3 pp, max +22.4 pp on HMMT 2026; Claude Opus 4.6-high). Beyond these contributions, we discover a "step-level scaling law": increasing per-agent steps consistently improves both effectiveness and efficiency, a new scaling dimension orthogonal to and composable with agent-count scaling.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体推理系统中现有通信协议存在的延迟高和效果受限问题。研究背景是，当前的多智能体系统普遍采用“生成-传输”范式，上游智能体必须完成完整响应后才传递给下游，这强制下游智能体空闲等待，导致端到端延迟与流水线深度成正比增长。现有方法的不足在于：这种串行协议不仅造成计算资源浪费，而且多步推理的质量具有非均匀性，早期步骤通常更可靠，而后期的步骤易出错。将整个响应（包含错误倾向的后半部分）传给下游，反而可能误导下游智能体的推理方向。本文提出的StreamMA系统引入了一种基于推理步骤的流式通信协议，将传输单位从完整响应细化为每个生成的推理步骤，从而通过流水线化相邻智能体降低延迟。更关键的是，这种机制意外提升了推理效果：由于下游智能体可以基于最可靠的前缀步骤独立展开推理轨迹，减少了后期错误步骤的干扰。论文形式化证明了流式协议在延迟加速比和有效性上的理论优势，并通过实验验证了跨数学、科学、代码等领域的显著提升。

### Q2: 有哪些相关研究？

在相关研究工作方面，本文主要涉及三类研究：

**1. 多智能体推理与通信**：现有工作沿着三个正交方向推进：通信拓扑、交换内容（如中间推理或KV缓存）以及智能体规模。但这些方法都共享"生成-传输"假设——上游智能体必须完成完整响应后才能启动下游智能体，导致顺序等待和无法流水线并行。本文通过将通信粒度从完整响应细化为推理步骤，暴露了每个智能体步骤数量这一新的设计维度，与智能体数量缩放正交。

**2. 逐步推理质量**：逐步推理已成为标准范式，但现有工作（如Self-Refine、Reflexion和多智能体辩论）仅利用步骤位置依赖性来验证或训练单模型的推理链。本文首次将此性质引入协议设计，给出了Single、Serial和Stream三种模式的闭式有效性排序及最优条件。

**3. 流水线并行与流式推理**：现有的流式推理主要作为加速机制（如推测解码、Group Think等），有效性提升仅是附带效应。本文的Stream在推理步骤粒度上运行于任意多智能体DAG，比token或固定块更粗，比预分解骨架更细，且不受拓扑限制。本文首次证明流式传输不仅能加速，还能提升有效性。

### Q3: 论文如何解决这个问题？

StreamMA的核心方法是提出流式通信协议，改变了传统多智能体系统中"先生成再传输"的范式。在整体框架上，StreamMA采用链式拓扑（可扩展到任意有向无环图），每个智能体产出一系列推理步骤。关键技术是流水线并行：上游智能体每生成一个推理步骤就立即推送到下游代理的队列中，下游代理无需等待完整响应即可开始处理，从而实现相邻代理的流水线作业。系统架构包括三个主要组件：流式LLM调用器（streaming call）、队列管理器（queue）和并发执行引擎（所有代理同时启动）。

论文的关键创新点体现在三个方面：第一，流式通信不仅降低延迟（理论上界可达AS/(S+A-1)倍加速），还能提升效果——因为多步推理质量不均匀，早期步骤更可靠，流式协议让下游代理优先处理这些可靠步骤，避免错误后期步骤误导。论文通过封闭形式联合分析（定理1）严格刻画了流式、串行和单代理三种协议的效果排序，将其归因于步级正确率的头加权、尾加权和均匀均值与阈值p*的关系。第二，发现"步级缩放定律"：增加每个代理的推理步数能同时提升效果和效率，这是一个与代理数量正交的新缩放维度。第三，通过KV缓存复用（共享前缀自然形成）进一步优化成本和延迟，在解码主导定价场景下，流式协议相比串行协议可节省成本。

### Q4: 论文做了哪些实验？

论文在8个推理基准测试上进行了实验，涵盖数学（AIME 2025/2026、HMMT 2026）、科学（GPQA-Diamond、HLE）和程序理解（LiveCodeBench的代码生成、执行、测试输出三个子任务）。对比方法包括Single（单智能体基线）和Serial（串行管道），使用Claude Opus 4.6 (High)和GPT-5.4 (Medium)两个前沿大模型，在Chain、Tree、Graph三种拓扑结构上评估。主要结果：StreamMA在所有平均指标上均优于两个基线，在Claude Opus 4.6上平均准确率提升+7.3个百分点（最高在HMMT 2026的Chain拓扑上达+22.4个百分点）。具体数据：Claude Opus 4.6的Chain拓扑中，StreamMA平均准确率81.70% vs Serial 73.48%；Tree拓扑中StreamMA 82.81% vs Serial 79.43%；Graph拓扑中StreamMA 83.34% vs Serial 72.92%。GPT-5.4上也呈现一致趋势。此外，通过步骤级扰动实验揭示：当尾部步骤被扰动时StreamMA优势明显（+24%），而头部步骤被扰动时StreamMA劣势（-34%），验证了其通过利用可靠早期步骤、过滤不可靠后期步骤的机制。

### Q5: 有什么可以进一步探索的点？

论文存在以下可进一步探索的方向：首先，StreamMA的"逐步传输"策略假设早期推理步骤更可靠，但未考虑任务类型差异——某些复杂推理（如多步代码调试）可能后期步骤更关键，未来可设计**自适应传输策略**，根据实时置信度动态决定何时传输中间结果。其次，"步骤级扩展定律"仅验证了同质化agent的链式拓扑，可探索**异构agent**场景（如混合专长模型）下步骤数分配的非线性收益，以及Tree/Graph拓扑中分支同步开销的优化。此外，当前速度提升依赖于理想化流水线，未考虑网络延迟波动和agent计算速度差异，可引入**动态负载均衡**机制。最后，论文未分析**长期上下文窗口**的影响——流式传输累积的历史步骤可能超出模型上下文限制，需要研究压缩或遗忘机制来平衡记忆与性能。

### Q6: 总结一下论文的主要内容

该论文提出StreamMA，一种基于流式通信的多智能体推理系统。现有系统采用“先生成后传递”的序列协议，导致延迟随流水线深度线性增长。StreamMA将传输单元从完整响应细化为推理步骤，每个步骤生成后立即流式传递给下游智能体，实现流水线执行。核心发现是，这种设计不仅降低延迟，还能提升推理效果：多步推理中早期步骤更可靠，而后期步骤易出错；下游智能体基于可靠前缀形成独立推理轨迹，可避免错误后期步骤的误导。作者在数学、科学和代码等8个推理基准上，使用Claude Opus 4.6和GPT-5.4两种前沿大模型，在链、树、图三种拓扑下验证了StreamMA的有效性（平均提升7.3个百分点，最高达22.4个百分点）。论文还首次给出了串行、流式、单智能体三种协议的封闭形式联合分析，推导了效果排序、加速上限和成本比。此外，发现了一个与智能体数量正交的“步骤级缩放律”：增加每智能体推理步骤数可同时提升效果和效率。
