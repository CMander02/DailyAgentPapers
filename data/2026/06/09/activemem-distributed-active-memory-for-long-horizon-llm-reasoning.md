---
title: "ActiveMem: Distributed Active Memory for Long-Horizon LLM Reasoning"
authors:
  - "Yunhan Jiang"
  - "Wenbin Duan"
  - "Shasha Guo"
  - "Liang Pang"
  - "Xiaoqian Sun"
  - "Huawei Shen"
date: "2026-06-09"
arxiv_id: "2606.10532"
arxiv_url: "https://arxiv.org/abs/2606.10532"
pdf_url: "https://arxiv.org/pdf/2606.10532v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Memory"
  - "Long-Horizon Reasoning"
  - "Multi-Agent Framework"
  - "Distributed Memory"
relevance_score: 9.0
---

# ActiveMem: Distributed Active Memory for Long-Horizon LLM Reasoning

## 原始摘要

Memory is essential for enabling large language model (LLM) agents to handle long-horizon reasoning tasks. Existing memory mechanisms are largely centralized, typically organizing retrieved information and interaction history within a single model context. This design imposes a fundamental trade-off: scaling reasoning trajectories risks context overload, whereas aggressive content pruning may result in irreversible information loss. Seeking a better trade-off, we draw inspiration from human cognitive systems, especially the functional complementarity between the prefrontal cortex (executive control) and the hippocampus (memory management), suggesting that such a trade-off need not be inherent, but may instead stem from centralized memory organization. To this end, we propose ActiveMem, a heterogeneous framework that decouples agent memory from the core reasoning process. Specifically, a high-level Planner utilizes distilled semantic gists to execute reasoning, while a lightweight, distributed memory system operates in parallel to actively accumulate and consolidate these gists throughout the task. Experiments on BrowseComp-Plus and GAIA show that ActiveMem achieves state-of-the-art accuracy with significantly reduced overhead, demonstrating the effectiveness of distributed active memory for long-horizon reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）代理在长时推理任务中面临的核心瓶颈：记忆管理。当前，大多数LLM推理系统采用集中式记忆架构，将检索到的信息和交互历史都存储在单一模型上下文中。这种设计导致了根本性的权衡：随着推理轨迹的延长，上下文窗口会过载，引发“丢失在中间”现象，损害推理性能；而为了控制上下文长度，采用内容修剪或压缩策略则会导致不可逆的信息丢失，使记忆内容永久退化且无法恢复。论文指出，这种权衡并非不可避免，其根源在于集中式记忆组织方式。受人类大脑中前额叶皮层（执行控制）与海马体（记忆管理）功能互补的启发，论文提出了一种新的解耦范式。核心问题是：如何设计一种记忆架构，使其既能支持长推理轨迹的扩展，又能避免信息丢失，从而打破集中式设计中轨迹规模与记忆保真度之间的固有矛盾。ActiveMem框架通过将记忆从核心推理过程中分离出来，构建一个轻量级、分布式的并行记忆系统，以实现这一目标。

### Q2: 有哪些相关研究？

相关研究主要分为两大类。第一类是**集中式记忆方法**，这是当前主流，又细分为三种：一是**原始集中式记忆**，如ReAct类智能体，直接将原始轨迹或检索证据回传给单一模型上下文；二是**基于摘要的集中式记忆**，如A-MEM、Mem0、Context-Folding、AgentFold、MemAgent等，通过压缩或摘要替代原始历史，但存在不可逆信息丢失的缺陷；三是**结构化集中式记忆**，如HiAgent和MemoBrain，对工作记忆进行层次或图结构组织，但记忆与推理仍紧密耦合于同一推理节点，面临保留细节与推理效率的权衡。第二类是**分布式记忆方法**，相关工作较少，典型代表是MIRIX，它采用模块化多智能体记忆系统，按记忆类型（如情节、语义、程序）分配记忆整合，但其组织方式基于记忆分类而非推理过程的信息需求，记忆模块不能主动根据规划器下发的子查询蒸馏任务相关信息。本文与上述工作的核心区别在于，ActiveMem通过将记忆形成过程与核心推理过程解耦，实现了分布式主动记忆：并行记忆器在规划器查询驱动下处理原始文档并生成条件化记忆摘要，持久化存储于记忆分片中，并选择性返回给规划器，从而避免了集中式方法中的信息丢失和效率问题，也比MIRIX等现有分布式方法更适配长程推理任务对动态文档选择的需求。

### Q3: 论文如何解决这个问题？

ActiveMem通过去中心化的异构框架解决长时推理中上下文过载与信息丢失的矛盾。其核心是将记忆管理与推理过程解耦：高层规划器（Planner）维护一个紧凑的推理状态，仅保留最近K步交互记录，丢弃的历史信息已通过语义要点（gist）形式存储在分布式记忆中。系统包含三个关键模块：记忆分片（Memory Shards）作为持久化存储层，每个分片以键值对形式存储文档及其对应要点和查询历史；并行记忆器（Memorizers）受海马体功能启发，根据规划的查询条件对检索文档进行查询条件式蒸馏，过滤无关信息并生成结构化要点；操作器（Operator）作为协调层，管理路由、记忆复用和异步合并。创新点在于：通过语义相似度判断实现记忆复用，避免重复蒸馏；异步合并机制在不阻塞推理流程的情况下将多角度要点融合为更丰富的条目；同时训练了轻量级专用记忆器（基于4B参数模型），通过从真实智能体轨迹中采集12000对查询-文档数据，利用教师模型蒸馏进行监督微调，确保生成简洁且内容锚定的要点。整体架构使规划器始终在清洁的压缩上下文中工作，而记忆系统持续并行积累和巩固语义知识。

### Q4: 论文做了哪些实验？

论文在BrowseComp-Plus和GAIA两个基准上进行了实验。BrowseComp-Plus包含150个样本，按Easy/Medium/Hard分设；GAIA使用WebSearch验证集（106个样本）。对比方法分为两类：Vanilla ReAct LLMs（包括Kimi-K2.5、Qwen3.5-397B-A17B、GLM-5.1、DeepSeek-V3.2）和Centralized Memory Agents（包括Context-Folding、AgentFold、MemoBrain、MemAgent）。所有模型统一采用Qwen3.5-397B-A17B作为骨干。评估指标包括LasJ（答案正确性）、PFLOPs（计算开销）和ACT（准确性-开销权衡）。

主要结果：ActiveMem在两个基准上均取得最优的准确性-成本权衡。在BrowseComp-Plus上，ActiveMem的总体LasJ达0.79，ACT为0.785，均最高；在GAIA上，LasJ为0.62，计算开销最低（187 PFLOPs）。相比最佳基线，在Medium分集上准确率提升0.10（至0.94），Hard分集提升0.08（至0.44）。消融实验表明，移除Memory Shards导致LasJ降至0.750，Memorizer PFLOPs增加至1739。

### Q5: 有什么可以进一步探索的点？

## 局限性与未来研究方向

本文的核心局限在于评估维度不完整：未能可靠测量端到端延迟和货币成本，因为并行Memorizer的调度开销、外部API响应波动以及商用/开源模型的混合计费体系使得公平比较难以实现。此外，Memorizer仅在BrowseComp-Plus的限定事实问答数据上通过监督微调训练，这限制了其泛化能力。

未来可从以下方向深入探索：**第一**，在完全本地化的环境下进行延迟与成本基准测试，设计统一的度量标准；**第二**，研究Memorizer的在线自适应学习机制，使其能在任务执行过程中持续提升gist蒸馏质量，而非一次性训练；**第三**，探索异构记忆系统的扩展性，例如引入分层记忆结构或与外部知识图谱动态交互。值得进一步思考的是，如何让Planner主动感知记忆状态并动态调整推理策略，形成"记忆-推理"的闭环反馈，这可能比单纯的并行化带来更大的效率提升。

### Q6: 总结一下论文的主要内容

ActiveMem 提出了一种神经科学启发的分布式主动记忆框架，旨在解决大语言模型（LLM）智能体在长程推理中的记忆瓶颈。现有集中式记忆机制面临上下文过载与信息丢失之间的根本权衡。受人类前额叶皮层（执行控制）与海马体（记忆管理）功能互补的启发，ActiveMem 将记忆从核心推理过程中解耦。其方法包括：高层Planner利用精简语义摘要进行推理，而轻量级分布式记忆系统并行运行，主动积累和整合这些摘要。在BrowseComp-Plus和GAIA等基准测试中，ActiveMem以显著降低的计算开销实现了最先进的准确率。该工作证明了分布式主动记忆机制是长程推理的高效可扩展基础，有效缓解了集中式设计的固有限制。
