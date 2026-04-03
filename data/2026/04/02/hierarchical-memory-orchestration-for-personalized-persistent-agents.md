---
title: "Hierarchical Memory Orchestration for Personalized Persistent Agents"
authors:
  - "Junming Liu"
  - "Yifei Sun"
  - "Weihua Cheng"
  - "Haodong Lei"
  - "Yuqi Li"
  - "Yirong Chen"
  - "Ding Wang"
date: "2026-04-02"
arxiv_id: "2604.01670"
arxiv_url: "https://arxiv.org/abs/2604.01670"
pdf_url: "https://arxiv.org/pdf/2604.01670v1"
categories:
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Personalization"
  - "Long-Term Memory"
  - "Hierarchical Architecture"
  - "Efficiency Optimization"
  - "Retrieval-Augmented Generation"
  - "User Persona"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# Hierarchical Memory Orchestration for Personalized Persistent Agents

## 原始摘要

While long-term memory is essential for intelligent agents to maintain consistent historical awareness, the accumulation of extensive interaction data often leads to performance bottlenecks. Naive storage expansion increases retrieval noise and computational latency, overwhelming the reasoning capacity of models deployed on constrained personal devices. To address this, we propose Hierarchical Memory Orchestration (HMO), a framework that organizes interaction history into a three-tiered directory driven by user-centric contextual relevance. Our system maintains a compact primary cache, coupling recent and pivotal memories with an evolving user profile to ensure agent reasoning remains aligned with individual behavioral traits. This primary cache is complemented by a high-priority secondary layer, both of which are managed within a global archive of the full interaction history. Crucially, the user persona dictates memory redistribution across this hierarchy, promoting records mapped to long-term patterns toward more active tiers while relegating less relevant information. This targeted orchestration surfaces historical knowledge precisely when needed while maintaining a lean and efficient active search space. Evaluations on multiple benchmarks achieve state-of-the-art performance. Real-world deployments in ecosystems like OpenClaw demonstrate that HMO significantly enhances agent fluidity and personalization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能代理在长期交互中因记忆数据不断累积而导致的性能瓶颈问题。随着大型语言模型和智能代理的发展，用户期望代理能够记住历史交互以提供连贯、个性化的体验。然而，现有方法通常将记忆视为扁平的存储库，采用简单的线性扩展策略，导致检索噪声增加、计算延迟上升，尤其在资源受限的个人设备上，这会拖慢推理速度并破坏交互的流畅性。

现有研究主要聚焦于提升检索精度或通过强化学习、思维链等技术增强推理能力，但这些方法往往忽略了对记忆库本身的组织与个性化管理。它们要么需要高昂的计算成本进行模型微调，要么在推理时引入显著延迟，且未能根据用户身份和场景的动态变化来区分记忆的重要性。这种“一刀切”的管理方式使得关键记忆被无关信息淹没，代理不得不搜索臃肿的数据空间，从而影响效率和用户体验。

本文的核心问题是：如何设计一个高效、个性化的记忆管理框架，以在有限资源下维持智能代理的历史感知能力与响应速度。为此，论文提出了分层记忆编排（HMO）框架，通过三层分级结构（主缓存、次级层和全局归档）来组织交互历史，并利用动态演进的用户画像驱动记忆的优先级分配与存储位置调整，从而在保证检索准确性的同时，保持活跃搜索空间的精简与高效。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕基于大语言模型的智能体记忆系统展开，可归类为方法类研究。

在方法类工作中，早期研究侧重于通过架构修改或外部存储来扩展上下文，例如MemGPT的分页机制和Mem0用于实体追踪的持久层。这些系统虽有效，但通常将记忆视为扁平、不断扩展的存储库，随着搜索空间增长，面临检索精度与计算效率之间的权衡。近期的管理策略则多依赖扁平化的向量数据库或图结构来存储对话关系，这容易导致搜索空间膨胀和检索延迟高。为缓解此问题，一些框架采用显式删除策略，但存在数据丢失风险；而参数化方法则涉及高昂的微调成本。

与上述工作不同，本文提出的分层记忆编排（HMO）框架采用多层级架构，其核心区别在于依据记忆的效用并以用户画像为中心来组织历史交互数据。HMO通过三层目录结构，动态地将记忆记录重新分配到不同活跃层级，既避免了数据丢失和重训练成本，又能确保检索的精准与高效，从而在维持长期一致性的同时，显著提升了智能体的流畅度与个性化水平。

### Q3: 论文如何解决这个问题？

论文通过提出分层记忆编排（HMO）框架来解决长期记忆积累导致的性能瓶颈问题。其核心方法是构建一个由用户画像驱动的三层记忆目录，通过动态评分与智能编排，在保证个性化服务的同时维持高效、精简的活跃搜索空间。

整体框架包含四个关键阶段：自主摄取、分层再分配、自适应评分和增量演化。系统将每次用户查询与智能体响应捕获为一个记忆片段，并针对内容长度选择存储原始对话或经多模态大语言模型压缩的认知表示。随后，一个基于MLLM的评估器会结合当前用户画像，为记忆片段生成初始重要性评分。每个记忆记录都会初始化一个包含评分、与画像的语义相似度、调用次数和最后访问时间等元数据的头部信息。

记忆根据其综合评分被分配到三个逻辑层级：第一层（缓存）存储最近会话和最关键的记忆，确保智能体推理与用户即时行为特征对齐；第二层（缓冲区）容纳高评分但未进入缓存的记录，作为次级缓存拦截检索请求；第三层（存档）存储全部历史交互，仅在活跃层无法满足查询时才被访问。检索时，系统按层级顺序进行搜索，若缓存层无法满足查询，则触发递归搜索机制，逐层向下查找。

关键技术创新点主要体现在三个方面：首先，设计了非线性的自适应持久性评分函数，该函数融合了初始重要性、动态画像对齐度、调用频率和时间衰减因子，并通过数学建模使高效用记忆即使久未访问也能保持较高活跃度。其次，引入了惰性更新策略，仅对活跃层（第一、二层）进行常规评分更新，对存档层记录仅在首次被访问时才计算评分并参与重排，避免了全局计算的巨大开销。最后，提出了基于锚点画像的漂移门机制，仅当用户画像变化超过预设阈值时才触发活跃层的全局评分更新，从而将高频的画像细化与昂贵的后台排序解耦，在动态适应个性化演变的同时保障了系统效率。

### Q4: 论文做了哪些实验？

论文在实验部分进行了全面的评估。实验设置方面，作者使用text-embedding-small进行向量化，GPT-4o-mini进行响应生成，并设置了分层存储的超参数（如主层大小S=5，K=50，次层容量H=200）。实验在两个代表性基准测试上进行：LoCoMo（包含10个不同用户群体的多轮对话）和LongMemEval-S（包含500个专门用于评估长期记忆处理能力的对话）。对比方法包括九个代表性的记忆与检索框架，如MemoryBank、Mem0、A-MEM、MemoryOS、MemVerse等。

主要结果如下：在LongMemEval-S上，HMO取得了最先进的性能，Recall@5达到81.1%，准确率（Acc.）达到86.4%，NDCG@5为85.6%。这些指标显著超过了基于Llama-3.1-70B的QRRetriever（Recall@5为80.4%）和另一个70B基线（准确率66.7%）。在LoCoMo上，HMO的总体F1分数达到45.65，优于MemVerse（43.44）和MemoryBank（31.42）等基线。消融实验表明，完整的三层配置（w/ Tier 1, 2）在推理时间（12.88分钟）和准确率（86.4%）之间取得了最佳平衡，相比无分层搜索（w/o Tier 1, 2，准确率88.8%，时间56.05分钟）实现了77%的速度提升，且准确率仅下降2.4%。此外，在更大规模的LongMemEval-M上，HMO将搜索时间从1453.21秒减少到195.75秒（减少86.5%），同时保持了63.0%的召回率。系统部署评估（如在OpenClaw上）也证实HMO能显著降低推理延迟并加速任务完成。

### Q5: 有什么可以进一步探索的点？

该论文提出的分层记忆编排框架虽在效率和个性化方面取得进展，但仍存在可深入探索的方向。其局限性主要体现在：用户画像的构建仍依赖历史交互数据，可能无法捕捉动态变化的短期兴趣或突发情境需求；三层存储结构的划分标准较为固定，缺乏对复杂任务中多维度记忆关联性的灵活适配；此外，系统未充分考虑跨设备、跨平台场景下记忆同步与隐私保护的平衡问题。

未来研究可朝以下方向拓展：一是引入轻量化在线学习机制，使画像能实时融合即时反馈与环境上下文，增强记忆调取的情境感知能力；二是探索自适应分层策略，允许记忆层级根据任务复杂度或用户活跃度动态调整，例如通过强化学习优化存储迁移阈值；三是结合边缘计算与差分隐私技术，在分布式设备网络中实现安全高效的个人记忆联邦管理，进一步提升系统可扩展性与用户信任度。

### Q6: 总结一下论文的主要内容

该论文针对智能体长期记忆管理中因数据累积导致的检索噪声、计算延迟和推理能力受限问题，提出了分层记忆编排（HMO）框架。核心贡献在于首次利用动态演化的用户画像来主导记忆的整个生命周期，通过三层分级存储结构（紧凑主缓存、高优先级次级层和全局归档）组织交互历史，依据用户中心的情境相关性对记忆进行动态重分布。方法上，HMO将近期关键记忆与用户画像耦合，确保推理与个体行为特征对齐，同时通过顺序检索和高效映射维持精简的活跃搜索空间，避免冗余数据移动。实验表明，该框架在多个基准测试中达到最先进性能，并在OpenClaw等实际部署中显著提升了智能体的交互流畅度和个性化水平。
