---
title: "ScrapMem: A Bio-inspired Framework for On-device Personalized Agent Memory via Optical Forgetting"
authors:
  - "Jiale Chang"
  - "Yuxiang Ren"
date: "2026-05-05"
arxiv_id: "2605.03804"
arxiv_url: "https://arxiv.org/abs/2605.03804"
pdf_url: "https://arxiv.org/pdf/2605.03804v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Memory Management"
  - "On-Device Agent"
  - "Multimodal Agent"
  - "Storage Efficiency"
  - "Personalized Agent"
relevance_score: 8.5
---

# ScrapMem: A Bio-inspired Framework for On-device Personalized Agent Memory via Optical Forgetting

## 原始摘要

Long-term personalized memory for LLM agents is challenging on resource-limited edge devices due to high storage costs and multimodal complexity. To address this, we propose ScrapMem, a framework that integrates multimodal data into "Scrapbook Page." ScrapMem introduces Optical Forgetting, an optical compression mechanism that progressively reduces the resolution of older memories, lowering storage cost while suppressing low-value details. To maintain semantic consistency, we construct an Episodic Memory Graph (EM-Graph) that organizes key events into a causal-temporal structure. Extensive experiments on the multimodal ATM-Bench showcase that ScrapMem provides three main benefits: (1) strong performance, achieving a new state-of-the-art with a 51.0% Joint@10 score; (2) high storage efficiency, reducing memory usage by up to 93% via optical forgetting; and (3) improved recall, increasing Recall@10 to 70.3% through structured aggregation. ScrapMem offers an effective and storage-efficient solution for on-device long-term memory in multimodal LLM agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在资源受限的边缘设备上，为基于大型语言模型（LLM）的智能体构建长期、个性化多模态记忆时面临的核心挑战。研究背景是，边缘设备上的个性化智能体需要持续整合用户的静态数据（如照片、邮件）和动态交互历史（如多轮对话），以实现长期推理和个性化服务。然而，现有方法存在明显不足：参数化记忆（如微调）容易遭受灾难性遗忘且缺乏可解释性；而基于检索的记忆（如向量数据库或知识图谱）则难以在统一语义空间中对齐文本、图像等异构模态，导致因果和时序推理能力弱。更重要的是，多模态记忆的存储成本极高，对于内存和计算能力有限的边缘设备来说是不可承受的。因此，本文要解决的核心问题是如何在边缘设备上设计一个既高效存储又具备强性能的多模态长期记忆系统，以克服现有方法在存储效率、多模态对齐和长程推理方面的局限性，最终实现低存储开销下的高性能个性化记忆。

### Q2: 有哪些相关研究？

在相关研究中，本文主要从三个类别进行对比：**方法类**、**检索类**和**结构化记忆类**。首先，在方法类中，传统工作如NextMem通过混合架构缓解遗忘，依赖参数微调（如LoRA）实现个性化，但难以适配多模态和低资源设备；而ScrapMem采用光学压缩（Optical Forgetting）渐进降低旧记忆分辨率，实现了高达93%的存储节省，无需额外训练。其次，检索类研究如MemoryBank和Agentic Unlearning基于文本嵌入存储历史，但面对多模态数据时对齐困难；最近基于视觉记忆的AgentOCR、MemOCR和OCR-Memory利用VLM编码文本为图像，提升了效率，但本文指出它们以文本为中心、依赖强化学习优化且缺乏时间因果建模。ScrapMem通过将多模态数据统一为“剪贴簿页面”克服了这些局限。最后，结构化记忆系统如Generative Agents、MemGPT、A-MEM和AgenTEE采用图或控制器组织知识，但计算开销大，不适合端侧部署。本文提出的Episodic Memory Graph（EM-Graph）以轻量级因果-时间结构提升召回率至70.3%，同时保持高效。综上，ScrapMem在存储效率、多模态统一和时序推理上显著超越了现有视觉记忆框架。

### Q3: 论文如何解决这个问题？

ScrapMem通过一个三阶段的生物启发框架解决边缘设备上LLM代理长期个性化记忆的高存储成本和多模态复杂性挑战。其核心方法包括：

1.  **Scrapbook Page整合与感知**：首先将异构多模态数据（图像、视频、文本）在时间上整合为统一的“剪贴簿页面”表示。然后通过光学感知管道，利用视觉编码器提取视觉token，并结合OCR模块提取文本内容，通过视觉到文本的转换（如图像描述）将视觉token映射为文本描述，从而实现对页面内容的多模态统一处理，建立索引与内容分离的混合节点集。

2.  **情节记忆图（EM-Graph）构建**：将提取的混合节点组织成事件结构化的情节记忆图。图中关键组件是**情节记忆路径（EM-Path）**，它捕捉单一时间页面内的事件因果链（如诊断 → 治疗 → 康复），形成多跳推理的基本单元。通过二进制的节点-路径关联矩阵（Q矩阵）显式编码节点与路径的归属关系，实现高效的查询-路径匹配，能够基于节点重叠度检索最相关的记忆证据。

3.  **光学遗忘机制**：受生物认知启发的渐进式压缩机制。通过时间依赖的退化算子，逐步降低陈旧记忆的视觉分辨率和文本细节，使低价值信息变得不可访问。这导致原始混合节点集收缩为核心语义节点，并修剪相应的情节记忆路径，保留了高层的因果结构和语义骨架，同时显著降低存储开销（最高达93%）。该机制既节省了存储与计算资源，又充当了原生认知过滤机制，使下游检索聚焦于长期稳定的记忆模式。

### Q4: 论文做了哪些实验？

论文在ATM-Bench数据集上进行了实验，该数据集包含四年跨模态真实个人数据（邮件、图片、视频）。实验评估了ScrapMem框架的主要结果，对比了两类基线：记忆智能体（A-Mem、Mem0）和RAG系统（HippoRAG2、Self-RAG、ATM-RAG），并设置了oracle上限。主要指标包括QS、Recall@10、Joint@10，以及Number(N)、List Recall(R)、Open-ended(O)细粒度准确率。结果显示，ScrapMem(No-Forget)取得了SOTA：Joint@10达51.0%，R@10达70.3%（唯一超70%的系统），List Recall达50.4%，显著优于HippoRAG2（46.9%/39.3%）和ATM-RAG（48.6%/32.4%）。启用光学遗忘后（Timed-Gentle配置），存储从4302.9 MiB降至299.5 MiB（节省93.0%），同时Joint@10仅降至46.9%，R@10保持66.1%，仍超越多数基线。不同遗忘策略（Very_Soft、Softer_Old、Boundary_365等）的Recall@K曲线高度一致，表明性能对视觉退化不敏感。Pareto前沿分析验证了存储-性能的高效权衡，支持边缘设备部署。

### Q5: 有什么可以进一步探索的点？

1. **光学遗忘的鲁棒性**：当前机制在极端低分辨率或高混乱度多模态布局下可靠性不足，可探索自适应分辨率衰减策略，例如结合注意力机制动态判断关键记忆区域并保留其细节。
2. **事件图构建的噪声**：依赖LLM进行语义提取时可能存在关系误连，可引入对比学习或图神经网络对EM-Graph进行后处理去噪，或利用记忆检索反馈来优化节点连接权重。
3. **开放世界适应性**：框架仅针对固定设备场景，未考虑连续工具调用和动态环境反馈。未来可设计动态记忆分层架构，结合环境状态向量更新记忆重要性，并支持跨设备记忆迁移。此外，可尝试神经符号方法将光学遗忘与符号化知识库融合，减少对高算力模型的依赖。

### Q6: 总结一下论文的主要内容

ScrapMem提出了一种受生物启发的边缘设备记忆框架，解决了多模态大语言模型智能体在资源受限设备上长期个性化记忆的高存储成本和多模态复杂性挑战。该框架将多模态数据整合为“剪贴簿页面”，并通过光学遗忘机制（光学压缩）逐步降低旧记忆的分辨率，在抑制低价值细节的同时大幅降低存储成本。为维持语义一致性，研究构建了情节记忆图，将关键事件组织为因果-时序结构。在ATM-Bench多模态基准上的实验表明，该方法取得了SOTA性能（Joint@10达51.0%），通过光学遗忘减少了93%的存储使用，并通过结构化聚合将Recall@10提升至70.3%。该工作为资源受限设备上隐私保护的长期个性化智能体记忆提供了高效解决方案，兼具存储效率与推理鲁棒性。
