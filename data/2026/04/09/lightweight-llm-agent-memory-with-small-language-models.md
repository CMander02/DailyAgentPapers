---
title: "Lightweight LLM Agent Memory with Small Language Models"
authors:
  - "Jiaquan Zhang"
  - "Chaoning Zhang"
  - "Shuxu Chen"
  - "Zhenzhen Huang"
  - "Pengcheng Zheng"
  - "Zhicheng Wang"
  - "Ping Guo"
  - "Fan Mo"
  - "Sung-Ho Bae"
  - "Jie Zou"
  - "Jiwei Wei"
  - "Yang Yang"
date: "2026-04-09"
arxiv_id: "2604.07798"
arxiv_url: "https://arxiv.org/abs/2604.07798"
pdf_url: "https://arxiv.org/pdf/2604.07798v1"
categories:
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Memory Architecture"
  - "Small Language Models (SLMs)"
  - "Long-Horizon Interaction"
  - "Multi-User Support"
  - "Retrieval-Augmented Generation (RAG)"
  - "Efficiency"
  - "System Design"
relevance_score: 8.5
---

# Lightweight LLM Agent Memory with Small Language Models

## 原始摘要

Although LLM agents can leverage tools for complex tasks, they still need memory to maintain cross-turn consistency and accumulate reusable information in long-horizon interactions. However, retrieval-based external memory systems incur low online overhead but suffer from unstable accuracy due to limited query construction and candidate filtering. In contrast, many systems use repeated large-model calls for online memory operations, improving accuracy but accumulating latency over long interactions. We propose LightMem, a lightweight memory system for better agent memory driven by Small Language Models (SLMs). LightMem modularizes memory retrieval, writing, and long-term consolidation, and separates online processing from offline consolidation to enable efficient memory invocation under bounded compute. We organize memory into short-term memory (STM) for immediate conversational context, mid-term memory (MTM) for reusable interaction summaries, and long-term memory (LTM) for consolidated knowledge, and uses user identifiers to support independent retrieval and incremental maintenance in multi-user settings. Online, LightMem operates under a fixed retrieval budget and selects memories via a two-stage procedure: vector-based coarse retrieval followed by semantic consistency re-ranking. Offline, it abstracts reusable interaction evidence and incrementally integrates it into LTM. Experiments show gains across model scales, with an average F1 improvement of about 2.5 on LoCoMo, more effective and low median latency (83 ms retrieval; 581 ms end-to-end).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在长程交互中，其外部记忆系统面临的效率与效果难以兼顾的核心问题。研究背景是，为了超越上下文窗口限制、维持跨轮次对话一致性并积累可复用信息，LLM智能体通常需要外部记忆系统。现有方法主要分为两类：一类是基于检索的外部记忆系统，其在线开销低，但由于查询构建和候选过滤能力有限，检索准确性不稳定；另一类则是在外部记忆基础上引入LLM来在线执行记忆的读写和控制操作，虽然能提升准确性，但反复调用大模型会累积显著的延迟，尤其在长程交互中开销巨大。这构成了一个效率与效果的权衡困境。

本文的核心问题是：如何设计一个既高效（低延迟）又有效（高检索准确性）的轻量级智能体记忆系统。为此，论文提出了LightMem系统，其核心思路是利用小型语言模型（SLMs）来驱动记忆操作，并通过模块化设计和在线-离线处理分离来优化这一权衡。具体而言，系统将记忆操作模块化（检索、写入、长期整合），并将高频率的在线处理（如查询改写、候选筛选）交给轻量的SLMs执行，而将繁重的抽象与整合任务推迟到离线阶段由大模型处理。这样，在线路径得以保持轻量化和可控，同时通过两阶段检索（向量粗检索+语义一致性重排序）来提升准确性，从而在有限的在线计算预算下，实现低延迟和高精度的记忆调用。

### Q2: 有哪些相关研究？

本文相关研究主要可分为检索式记忆和LLM驱动式记忆两大类。

在检索式记忆方面，MemoryBank通过存储总结的用户事件实现个性化长期对话，并采用遗忘机制控制增长；MemGPT将上下文窗口视为虚拟内存，在提示词与外部存储间进行分页交换，支持运行时逐出和按需检索；ReadAgent则依赖外部缓存的检索，索引压缩后的要点并在需要时查找证据。这些方法在线开销低，但受限于查询构建和候选过滤，准确性不稳定。

在LLM驱动式记忆方面，HiAgent通过将轨迹分块为子目标并用LLM总结过去步骤来管理试验内工作记忆；A-MEM进一步通过LLM驱动的笔记记录和自动链接构建自组织记忆网络，但通常未在资源约束下强调严格的在线/离线解耦。这类方法准确性更高，但依赖重复的大模型调用，在长程交互中延迟累积。

本文提出的LightMem系统旨在解决上述轻量但嘈杂的检索式记忆与有效但昂贵的LLM驱动在线操作之间的权衡。其关键区别在于：采用小语言模型（SLM）进行轻量级在线控制与过滤，在固定计算预算下实现高效记忆调用；通过模块化设计分离在线处理与离线整合，并引入短、中、长期记忆分层结构，支持多用户场景下的独立检索与增量维护。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为LightMem的轻量级内存系统来解决LLM智能体在长程交互中内存操作效率与准确性难以兼顾的问题。其核心方法是利用小型语言模型（SLMs）模块化地处理内存操作，并将在线检索与离线整合分离，从而在有限计算资源下实现高效、准确的内存调用。

整体框架包含在线和离线两条路径。在线路径负责实时内存检索与写入，离线路径则负责将中期记忆（MTM）中的高价值信息整合到长期记忆（LTM）中。内存被组织为三层结构：短期记忆（STM）作为对话上下文的工作缓冲区；中期记忆（MTM）存储带有用户标识符、可重用的交互摘要，是个人化情景记忆的唯一载体；长期记忆（LTM）则存储从MTM提炼出的、去身份化的语义知识，并以图结构组织以支持多跳推理和跨任务知识共享。

主要模块与关键技术包括：
1.  **检索控制器（SLM-1）**：这是一个轻量级规划模块。它将原始输入转换为结构化的检索计划，包括生成一组假设查询（HQs）、指定元数据过滤器（如用户ID、时间窗口）以及设定固定的Top-K返回预算。这实现了查询重写、路由和预算控制，而非直接检索。
2.  **两阶段检索器（SLM-2）**：执行具体的检索操作。第一阶段在元数据约束下，对每个假设查询进行向量相似性粗检索，汇总固定数量（2K）的候选记忆。第二阶段由SLM-2对这批固定大小的候选集进行语义一致性检查和相关性判断，执行“二选一”压缩，最终输出不超过K个最相关的记忆。这种方法在保证计算稳定性的同时，实现了超越向量相似度的语义精炼。
3.  **记忆写入器（SLM-3）**：在生成响应后，从当前交互中提取可重用的用户相关信息，压缩成简洁的记忆项写入MTM。系统通过合并重复项、处理冲突信息以及实施容量上限（B）来管理MTM，避免冗余和噪声积累。
4.  **离线整合模块**：由一个大语言模型（LLM）周期性执行，与在线操作严格解耦。它仅处理增量批次（新写入或重新激活的MTM项），将情景证据抽象为去身份化的知识候选，通过相似性搜索在LTM图谱中找到语义锚点，并进行增量插入和链接。此过程还应用置信度衰减来实现自然遗忘，维持LTM的轻量与时效性。

创新点主要体现在：1）利用多个专用SLM模块化协同，分离在线轻量查询与离线深度整合；2）提出基于固定预算的两阶段检索机制，结合向量粗筛与语义重排，兼顾效率与稳定性；3）设计三层记忆架构与用户标识符，支持多用户场景下的独立检索和增量维护；4）采用图结构LTM与增量整合策略，实现知识的持续演化与高效推理。

### Q4: 论文做了哪些实验？

论文在实验部分主要评估了所提出的LightMem系统在长对话记忆任务上的有效性、泛化能力和效率。实验设置方面，研究使用了两个数据集：LoCoMo（专注于长对话逻辑推理，平均9K tokens，涵盖单跳、多跳、时序、开放域和对抗性五类任务）和DialSim（源自电视剧的多方长时会话数据集）。对比方法选取了LoCoMo、ReadAgent、MemoryBank、MemGPT和A-MEM等代表性记忆系统基线。为了公平比较，所有方法在相同骨干模型和固定检索预算下进行评估。骨干模型涵盖了多种规模的LLM，包括GPT-4o、GPT-4o-mini、Qwen2.5（1.5B和3B）以及Llama 3.2（1B和3B），以检验泛化性。响应质量评估结合了词法重叠指标（如F1、BLEU-1）和语义指标（如ROUGE-L、METEOR、SBERT相似度）。为隔离记忆系统的影响，统一使用GPT-4o-mini作为响应生成器。LightMem的控制平面使用本地部署的量化小语言模型（SLM），分别负责查询生成与路由、语义重排序与压缩、在线写入与中期记忆维护；离线整合则由大上下文LLM处理。向量检索使用all-MiniLM-L6-v2编码，粗检索Top-10，中期记忆容量上限为10^4项。

主要结果显示，在LoCoMo基准上，LightMem在多数任务类别和模型规模上取得了最佳或接近最佳的整体性能。例如，使用GPT-4o-mini时，LightMem在单跳、多跳、时序、开放域和对抗性任务上的F1分数分别为45.80、28.85、46.20、13.50和54.50，普遍优于基线（如A-MEM）。特别是在多跳和时序推理任务上优势明显。在DialSim数据集上，LightMem在GPT-4o-mini上取得了F1 4.12、BLEU-1 3.95、ROUGE-L 4.20、ROUGE-2 4.15、METEOR 2.48和SBERT相似度23.40的全面领先结果，表明其提升不仅在于词法重叠，更在于语义一致性。效率方面，LightMem在GPT-4o-mini上的检索延迟中位数（P50）为83毫秒，端到端延迟中位数为581毫秒，显著低于A-MEM（检索856毫秒，端到端914毫秒），在保持低延迟的同时实现了性能增益。消融实验证实了各组件（如语义重排序、假设查询路由、中期记忆、离线整合和图结构）的必要性。总体而言，LightMem在多个模型规模上平均带来约2.5的F1提升，并在长时交互中实现了高效且有效的记忆管理。

### Q5: 有什么可以进一步探索的点？

本文提出的LightMem系统在轻量级记忆管理上取得了进展，但其设计仍存在一些局限性和可拓展方向。首先，系统依赖于特定的小语言模型（SLMs）驱动，其性能受限于所选SLMs的能力，未来可探索更高效或专门优化的轻量模型架构。其次，论文未充分探讨不同的记忆整合策略与控制策略的影响，例如如何动态调整短期、中期、长期记忆之间的转换阈值，或引入自适应机制以优化检索精度与延迟的平衡。此外，系统在多用户场景下虽支持独立检索，但未深入处理用户间记忆的潜在交互与冲突问题，未来可研究跨用户知识共享与隐私保护的权衡机制。从更广阔的视角看，可结合强化学习或元学习来优化记忆的写入与淘汰策略，使系统能在长期交互中更智能地积累和演化知识，进一步提升Agent在复杂任务中的持续学习能力。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为LightMem的轻量级外部记忆系统，旨在解决大型语言模型（LLM）智能体在长期交互中面临的内存管理挑战。核心问题是现有检索式内存系统精度不稳定，而在线重复调用大模型则导致高延迟。LightMem的创新在于采用小型语言模型（SLM）驱动，将内存操作模块化，并分离在线处理与离线整合以提升效率。

方法上，系统将内存分为短期记忆（STM）、中期记忆（MTM）和长期记忆（LTM），支持多用户隔离。在线阶段，它在固定检索预算下，通过向量粗检索和语义一致性重排序的两阶段流程选择记忆；离线阶段则抽象可重用交互证据并整合至LTM。实验表明，该系统在LoCoMo和DialSim基准上均带来性能提升（如LoCoMo平均F1提高约2.5），同时保持低延迟（检索中位数83毫秒，端到端581毫秒），证明了其有效性与高效性。
