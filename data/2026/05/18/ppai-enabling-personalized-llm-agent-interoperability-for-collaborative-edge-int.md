---
title: "PPAI: Enabling Personalized LLM Agent Interoperability for Collaborative Edge Intelligence"
authors:
  - "Zile Wang"
  - "Qianli Liu"
  - "Kaibin Guo"
  - "Haodong Wang"
  - "Jian Lin"
  - "Zicong Hong"
  - "Song Guo"
date: "2026-05-18"
arxiv_id: "2605.18067"
arxiv_url: "https://arxiv.org/abs/2605.18067"
pdf_url: "https://arxiv.org/pdf/2605.18067v1"
categories:
  - "cs.CL"
tags:
  - "Personalized LLM Agent"
  - "Multi-Agent Collaboration"
  - "Edge Intelligence"
  - "Agent Interoperability"
  - "Query-Agent Matching"
  - "Bayesian Game"
  - "Load Balancing"
  - "Peer-to-Peer Network"
relevance_score: 9.5
---

# PPAI: Enabling Personalized LLM Agent Interoperability for Collaborative Edge Intelligence

## 原始摘要

Deploying large language model (LLM) on edge device enables personalized LLM agents for various users. The growing availability of diverse personalized agents presents a unique opportunity for peer-to-peer (P2P) collaboration, wherein each user can delegate tasks beyond the local agent's expertise to remote agents more suited for the specific query. This paper introduces PPAI, the first personalized LLM agent interoperability system, which enables users to collaborate with each other based on agent specialization. However, the ever-changing pool of agents and their interchangeable capacity introduce new challenges when it comes to matching queries to agents and balancing loads, compared with existing P2P systems. Therefore, we propose a scalable query-agent pair scoring mechanism based on prototypes to identify suitable agents within a P2P network with churn. Moreover, we propose a multi-agent interoperability Bayesian game to balance local demand and global efficiency, when changes in remote agent load occur too quickly to be observed. Finally, we implement a prototype of PPAI and demonstrate that it substantially broadens the range of tasks that could be carried out while maintaining load balance. On average, it achieves an accuracy improvement of up to 7.96% across multiple tasks, while reducing latency by 16.34% compared to the baseline.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决如何实现个性化大语言模型（LLM）代理在边缘设备上的协作互通问题。研究背景是：将LLM部署在边缘设备上可以为不同用户提供个性化代理，但这些代理的能力受限于本地资源和训练数据，因此单个代理可能无法应对超出其专长的查询任务。现有方法的不足在于：传统点对点（P2P）系统通常假设节点能力相对稳定且可预测，而个性化LLM代理池中的代理会不断变化（如新代理加入、旧代理退出），且每个代理的能力可互换、负载动态波动，这使得查询与代理的匹配以及负载均衡面临挑战。本文的核心问题是：如何在这样一个高动态、代理能力异构且负载变化快速的边缘环境中，设计一套系统实现代理间的有效协作，从而扩展单个代理的任务范围，同时保持全局负载平衡。为此，论文提出了PPAI，第一个个性化LLM代理互通系统，通过基于原型的可扩展查询-代理评分机制来识别合适的代理，并引入多代理互通贝叶斯博弈来平衡本地需求与全局效率。

### Q2: 有哪些相关研究？

本文相关研究主要围绕三大类：LLM Agent应用、边缘设备部署优化和Multi-Agent路由聚合机制。在LLM Agent应用方面，像Mind2Web、SWE-agent和MetaGPT展现了Agent在特定任务中的能力。在边缘侧，Mobile-Agent-v2和MobileSteward等研究了移动设备上的Agent协作，但大多聚焦于单一设备或固定服务器架构，而本文PPAI首次提出面向P2P个性化Agent的互操作性系统，突破了传统集中式架构限制。

在系统优化方面，相关工作通过流水线并行、多GPU协调、量化（如GPTQ）和知识蒸馏等技术提升推理效率，这些技术正交于PPAI，可用于系统内部加速。本文关注的核心挑战在于动态变化的Agent池与不可观察的负载变化，这与传统P2P系统不同。

在Multi-Agent路由方面，现有工作如基于对比学习的Agent路由、成本感知决策和后排名机制等，通常假设多个模型驻留在同一设备上，专注于选择最佳的本地模型，而不适用于P2P跨设备场景。PPAI的创新在于提出了基于原型的可扩展查询-Agent匹配评分机制，并设计了贝叶斯博弈来平衡本地需求与全局效率，从而在负载快速变化时仍然实现良好性能，显著拓展了可执行任务范围并维持负载均衡。

### Q3: 论文如何解决这个问题？

PPAI的核心方法是设计了一个双层协作架构，将查询与智能体匹配和负载调度解耦。整体框架包括一个基于原型锚定的可扩展查询-智能体对评分模块和一个多智能体互操作贝叶斯博弈调度器。

首先，为解决动态智能体池中的匹配问题，PPAI引入了一个原型锚定语义空间。该空间通过一个名为QAGate的轻量级投影器，将查询和智能体能力都映射到一组共享的原型上。查询被投影为稀疏的相关性向量，智能体的能力则通过其在各原型对应任务上的性能向量进行表征。智能体加入、离开或更新时，通过Gossip协议传播其能力向量更新，无需重新训练模型，从而实现了对动态变化的自适应。查询与智能体的兼容性通过这两个向量的余弦相似度计算得出。

其次，为了平衡局部需求与全局效率，PPAI将调度问题形式化为一个多智能体互操作贝叶斯博弈。由于智能体的实时负载难以被其他节点直接观测，每个用户为其他智能体维护一个关于其服务率和查询到达率的信念分布。当收到查询时，用户会从评分模块得到的候选智能体列表中选择调度目标。它会请求候选智能体的状态信息并利用贝叶斯规则更新信念，然后根据更新后的信念计算期望队列负载和委派成本，最终选择最大化语义相关性（来自评分模块）与委派成本（包括负载、推理和传输延迟）加权和（即效用函数）的智能体。该博弈被证明是精确势博弈，存在贝叶斯纳什均衡，且贝叶斯价格竞争比有上界。

创新点在于：1) 提出了原型锚定的可扩展评分机制，实现了对动态智能体池的零训练适应；2) 设计了基于贝叶斯博弈的调度器，在不完全信息下结合语义匹配与负载感知进行决策；3) 整个系统在保持负载均衡的同时，显著提升了任务准确率并降低了延迟。

### Q4: 论文做了哪些实验？

论文在基于vLLM和libp2p的平台上进行了实验。实验设置包括5个异构LLM代理：Qwen2.5-7B-Instruct（编程/数学）、DeepSeek-R1-Distill-Qwen-7B（推理）、OpenCodeReasoning-Nemotron-7B（代码推理）、HuatuoGPT-o1-7B（医疗推理）和Meta-Llama-3-8B-Instruct（对话）。每个代理从ShareGPT数据集中获得先验知识。为评估可扩展性，实验扩展到50、100、500和1000个代理。数据集包括MMLU（57个任务）、GSM8K（数学）、MedQA（医学）、ARC-C（科学）和AGIEval（作为OOD基准）。用户请求遵循泊松分布，请求到达率λ=10。对比方法包括单代理（本地代理）和多代理基线：多数投票、RouterDC和KABB。主要指标为平均准确率和平均处理时间。结果显示，PPAI在多数任务上平均准确率提高7.96%，处理延迟降低16.34%。在MMLU上，当λ超过40时，单代理处理时间急剧上升，而PPAI保持最低延迟。与KABB相比，在重负载下PPAI更具优势，且准确率表现一致。此外，PPAI在MMLU所有任务类别中实现了均匀的高准确率。

### Q5: 有什么可以进一步探索的点？

基于PPAI系统的讨论部分，未来可深入探索以下方向：

1. **安全性与鲁棒性增强**：当前系统假设P2P环境中所有代理可信，但实际场景中可能存在恶意代理发起拒绝服务攻击、返回错误输出或通过自适应查询窃取隐私数据。未来可引入信任与声誉管理机制、异常检测及速率限制策略，并研究模型反演与成员推断攻击的防御方法。

2. **激励与公平性机制设计**：系统面临“搭便车”问题——理性代理可能只管消费而不贡献资源，导致公地悲剧。可探索基于博弈论或区块链的激励方案，根据贡献度与可靠性分配奖励，并设计声誉驱动的合作优先级策略，使主动协作成为理性代理的占优策略。此外，针对负载快速变化场景，可进一步优化贝叶斯博弈模型的均衡求解效率。

### Q6: 总结一下论文的主要内容

该论文提出PPAI系统，首个支持个性化LLM代理互操作性的框架，旨在解决边缘设备上不同用户私有LLM代理间的协作问题。核心挑战是动态代理池中查询匹配与负载均衡的冲突。方法上，提出基于原型的可扩展查询-代理评分机制以识别P2P网络中的合适代理，并设计多代理互操作性贝叶斯博弈模型，在代理负载快速变化且不可观测时平衡本地需求与全局效率。实验表明，PPAI在提升多任务准确率最高达7.96%的同时，将延迟降低16.34%，显著拓展了边缘设备可处理的任务范围并保持负载均衡，为个性化AI代理的分布式协作提供了新范式。
