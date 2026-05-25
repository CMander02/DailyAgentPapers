---
title: "GraphFlow: A Graph-Based Workflow Management for Efficient LLM-Agent Serving"
authors:
  - "Ao Li"
  - "Shangpeng Yang"
  - "Fahao Chen"
  - "Tianheng Xu"
  - "Peng Li"
  - "Zhou Su"
date: "2026-05-21"
arxiv_id: "2605.22566"
arxiv_url: "https://arxiv.org/abs/2605.22566"
pdf_url: "https://arxiv.org/pdf/2605.22566v1"
categories:
  - "cs.LG"
tags:
  - "LLM Agent"
  - "Workflow Management"
  - "图管理系统"
  - "KV Cache优化"
  - "自适应工作流生成"
relevance_score: 8.0
---

# GraphFlow: A Graph-Based Workflow Management for Efficient LLM-Agent Serving

## 原始摘要

Large Language Model (LLM)-based agents demonstrate strong reasoning and execution capabilities on complex tasks when guided by structured instructions, commonly referred to as workflows. However, existing workflow-assisted agent serving systems typically rely on predefined templates and shallow matching mechanisms, which limit their ability to capture deep semantic relationships and generalize to previously unseen tasks. To address these limitations, we propose a new workflow management paradigm that represents workflows using a unified graph, termed wGraph, where each node corresponds to an atomic operation. wGraph serves as a shared substrate from which task-specific workflows are dynamically instantiated. Building on wGraph primitives, we introduce GraphFlow, a system that efficiently integrates workflows into agent serving through two key designs. First, adaptive workflow generation dynamically constructs workflows from wGraph based on task semantics and constraint requirements. Second, workflow state management exploits wGraph structure to efficiently manage Key-Value (KV) caches, reducing redundant computation during agent serving. Extensive experiments across five benchmark datasets show that GraphFlow consistently outperforms state-of-the-art methods, yielding an average performance improvement of approximately 4.95 percentage points, while achieving an approximately 4$\times$ reduction in memory footprint.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决现有基于工作流的 LLM 智能体系统中存在的两个核心问题。首先，现有方法的工作流构建方式过于静态和受限，主要依赖预定义模板或基于语义相似度的检索匹配。这种方式将工作流视为粗粒度的固定模板，无法捕捉任务需求与执行过程结构之间的细粒度对应关系，导致在处理未见过的或组合型任务时缺乏泛化能力。其次，现有系统在工作流状态管理中存在严重的冗余问题。由于不同工作流会反复调用相同的原子操作（如工具调用、推理步骤），但系统却以单个工作流为粒度管理 KV 缓存，导致相同操作的中间状态被重复存储，造成大量内存浪费，限制了系统的可扩展性。

针对上述不足，本文提出了一种基于图的工作流管理框架 GraphFlow。其核心创新是设计了一个统一的全局操作图（wGraph），将不同工作流中的原子操作及其依赖关系整合到一个结构化表示中。基于此，论文进一步提出了两个关键技术：一是利用图神经网络实现自适应的、任务相关的工作流动态生成，而非简单检索；二是基于 wGraph 拓扑结构的 KV 缓存管理机制，通过将每个操作的 KV 状态分解为上下文无关的基础部分和稀疏的上下文相关残差，并引入路径剪枝策略，从而显著减少冗余计算和内存占用。核心目标是构建一个更具通用性、灵活性和高效性的 LLM 智能体服务系统。

### Q2: 有哪些相关研究？

在相关研究中，LLM Agents方面，CoT和ToT探索推理路径，ReAct和LATS结合环境反馈优化执行，而Reflexion和MemGPT引入记忆机制。本文的GraphFlow通过统一图结构（wGraph）管理原子操作，区别于这些依赖固定推理轨迹的方法，能动态生成工作流并共享执行前缀。在Agentic Workflows方面，MetaGPT和ChatDev使用预定义SOP，TaskWeaver和LLM-Compiler将工作流编程化或图结构化，但均存在扩展性瓶颈。本文通过wGraph实现操作级结构复用，避免检索式方法（如Voyager）的独立规划检索。在系统层面，vLLM减少KV缓存碎片，但现有系统为每个工作流实例维护独立KV状态。GraphFlow利用wGraph结构管理KV缓存，实现共享前缀的缓存复用，显著减少内存冗余（约4×），这是与PagedAttention等通用优化技术的核心区别。

### Q3: 论文如何解决这个问题？

GraphFlow通过两种核心设计解决现有工作流系统无法捕捉深层语义和泛化到新任务的问题。整体框架基于一个统一的全局操作图（wGraph），这是一个有向无环图，其中每个节点代表原子操作（如工具调用或推理步骤），边表示依赖关系。wGraph作为共享基板，从中动态实例化任务特定工作流。

第一个核心组件是任务自适应工作流生成。该方法将工作流合成视为条件子图生成问题。首先，向wGraph添加一个虚拟任务节点，并通过双向边将其与所有操作节点连接，形成任务条件图。使用图神经网络（GNN）编码节点特征和结构依赖关系，生成任务感知的节点嵌入。然后，基于多层感知机（MLP）计算每对候选操作边（由wGraph允许）的兼容性分数，从任务节点开始逐步选择最高分数的边，同时强制执行结构有效性约束，最终形成连通的工作流子图。

第二个核心组件是拓扑感知状态管理，解决KV缓存效率问题。该方法采用差分KV缓存设计：为每个操作节点预计算一个独立的“基础KV缓存”，并只为高频执行路径存储稀疏的“前缀特定残差”（表示前缀诱导的差异）。通过基础缓存加残差重建完整的上下文感知KV状态。此外，基于执行统计进行有效路径剪枝，只存储高频转换的残差，对罕见路径则回退到实时计算。这实现了约4倍的内存占用减少，同时保持执行正确性。

### Q4: 论文做了哪些实验？

GraphFlow在Qwen-2.5-7B、Llama-3.1-8B和Gemma-2-9B三个LLM骨干上，使用GSM8K、MATH（数学推理）、HumanEval、MBPP（代码生成）和HotpotQA（复杂问答）五个基准数据集进行实验。对比方法包括Vanilla（无工作流）、MetaGPT（基于角色模板）、LLMCompiler（编译器式规划）、TaskWeaver（检索+组合）、AgentKB（知识增强）、AutoFlow（自动归纳）和AFlow（计算图搜索）。主要结果：GraphFlow在所有任务和模型上平均性能提升约4.95个百分点的同时，P90推理延迟降低了约12.7%（如Qwen-2.5-7B上从14.06秒降至12.25秒），尤其HumanEval的pass@1从78.1%提升至86.2%。在记忆效率实验中，相比有状态KV管理，平均内存占用降低约4倍（如GSM8K从50GB降至11GB），同时保持接近的性能；在不同批处理规模下，内存增长显著低于有状态方法，保持0.5GB以下。路径剪枝模块进一步减少3-5GB内存。

### Q5: 有什么可以进一步探索的点？

从该论文出发，未来的探索可从以下几方面展开。首先，**工作流图（wGraph）的构建与演化机制**：当前wGraph主要基于预定义原子操作，未来可探索如何利用LLM自主生成或动态更新原子节点，以应对更复杂、非结构化的任务。其次，**跨任务泛化与迁移能力**：论文侧重相同任务域内的优化，可验证工作流能否在不同领域间高效复用，并研究元学习或图对比学习以提升迁移效率。再次，**缓存策略的细粒度优化**：当前KV缓存管理基于图结构，但未考虑节点间计算依赖的权重差异，未来可引入注意力权重或操作流行度实施分层缓存，平衡内存与计算。另外，**多智能体协作场景**：现有工作聚焦单智能体任务，可拓展至分布式多智能体场景，研究wGraph在通信同步、任务分解中的角色。最后，**评估体系的完善**：增加对长尾任务、对抗性指令及延迟敏感场景的基准测试。改进方向包括引入增量式图细化和基于强化学习的自适应剪枝，以提升系统鲁棒性与吞吐量。

### Q6: 总结一下论文的主要内容

GraphFlow提出了一种基于图的工作流管理新范式，旨在解决现有LLM代理系统中依赖预定义模板和浅层匹配、缺乏语义泛化能力的问题。其核心贡献是将多样化的代理任务统一表示为一种名为wGraph的共享操作图，每个节点代表原子操作，从而支持动态实例化任务特定工作流。方法上包括两大关键设计：一是基于任务语义和约束的自适应工作流生成，从wGraph动态构建子图；二是利用wGraph拓扑结构进行状态管理，通过差分KV缓存策略显著减少冗余计算。实验表明，在五个基准数据集上，GraphFlow相比最先进方法平均性能提升约4.95个百分点，同时内存占用降低约4倍。该工作将代理编排从静态工作流检索推进到动态子图构建，为复杂任务下的高效、可扩展LLM代理服务提供了重要范式转变。
