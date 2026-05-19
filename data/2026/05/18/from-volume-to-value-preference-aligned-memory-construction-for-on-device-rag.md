---
title: "From Volume to Value: Preference-Aligned Memory Construction for On-Device RAG"
authors:
  - "Changmin Lee"
  - "Jaemin Kim"
  - "Taesik Gong"
date: "2026-05-18"
arxiv_id: "2605.18271"
arxiv_url: "https://arxiv.org/abs/2605.18271"
pdf_url: "https://arxiv.org/pdf/2605.18271v1"
github_url: "https://github.com/UbiquitousAILab/EPIC"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.IR"
  - "cs.LG"
tags:
  - "On-Device Agent"
  - "Personal AI Agent"
  - "RAG"
  - "Memory Management"
  - "Preference Alignment"
relevance_score: 7.5
---

# From Volume to Value: Preference-Aligned Memory Construction for On-Device RAG

## 原始摘要

With the rapid emergence of personal AI agents based on Large Language Models (LLMs), implementing them on-device has become essential for privacy and responsiveness. To handle the inherently personal and context-dependent nature of real-world requests, such agents must ground their generation in device-resident personal context. However, under tight memory budgets, the core bottleneck is what to store so that retrieval remains aligned with the user. We propose EPIC (Efficient Preference-aligned Index Construction), which focuses on user preferences as a compact and stable form of personal context and integrates them throughout the RAG pipeline. EPIC selectively retains preference-relevant information from raw data and aligns retrieval toward preference-aligned contexts. Across four benchmarks covering conversations, debates, explanations, and recommendations, EPIC reduces indexing memory by 2,404 times, improves preference-following accuracy by 20.17 percentage points, and achieves 33.33 times lower retrieval latency over the best-performing baseline. In our on-device experiment, EPIC maintains a memory footprint under 1 MB with 29.35 ms/query latency in streaming updates.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决在资源受限的个人设备上构建个性化RAG（检索增强生成）系统时面临的核心瓶颈问题。研究背景是随着大语言模型（LLM）驱动的个人AI代理兴起，出于隐私和响应速度的考虑，需要在设备本地部署。这些代理需要利用设备上的个人上下文（如浏览记录、对话历史）来生成符合用户个性化需求的回答。

现有方法的不足主要有两点：一是传统RAG倾向于存储所有数据，但个人设备上数据异构且持续增长，在严格的内存预算（如1MB以下）下，全量存储既不可行也会浪费宝贵资源；二是标准检索器通常忽略用户偏好，检索到的内容虽与查询相关，但可能与用户的实际偏好（如饮食限制、价值取向）相冲突，导致生成的回答“答非所问”。

因此，本文要解决的核心问题是：**在设备端极有限的内存和隐私约束下，应当存储什么信息，才能构建一个既紧凑又能与用户偏好高度一致的记忆，从而在检索阶段准确对齐用户的实际偏好**。为此，论文提出了EPIC框架，通过优先选择性存储与用户偏好相关的信息，并对查询进行偏好引导，从根本上解决资源约束与个性化需求之间的矛盾。

### Q2: 有哪些相关研究？

相关工作主要分为三类。第一类是传统RAG系统，如基于BM25、DPR、Contriever等检索器的方法，以及构建层次或图结构索引的RAPTOR、HippoRAG等。这些方法假设语料库静态或集中管理，关注固定索引下的检索质量，而本文面向设备端持续增长的非结构化数据，将瓶颈从“如何检索”转向“存储什么”，提出了偏好对齐的记忆构建。

第二类是记忆侧个性化RAG，代表作包括EMG-RAG（将设备记忆组织为可编辑图）和PEARL（选取用户创作内容以捕获风格与价值观）。它们从已有的用户数据出发，侧重检索时如何利用个人信号；而本文处理的是原始异构数据，需要在索引构建阶段就决定存储哪些内容。

第三类是查询侧个性化RAG，如Cognitive Personalized Search和PBR（基于LLM的查询重写与扩展）。这些工作通过改写查询融入用户上下文，但未优化存储本身。本文的核心区别在于：在极低内存预算下（<1MB），同时优化索引构建与检索，使记忆既紧凑又偏好对齐，而非仅依赖查询时处理。

### Q3: 论文如何解决这个问题？

EPIC (Efficient Preference-aligned Index Construction) 通过一个三阶段框架将用户偏好深度集成到RAG流程中，以解决设备上个人AI Agent的内存瓶颈与偏好对齐问题。首先，**语义粗筛**阶段利用共享编码器(如Contriever)将数据项和用户偏好嵌入同一语义空间，通过余弦相似度与阈值τ快速过滤掉大部分与偏好无关的内容，仅保留高召回率的候选集。随后，**偏好对齐细验证**阶段引入两个协同模块：决策模块利用语言模型严格判断候选项是否应保留，并输出决策依据；指令生成器为保留项生成偏好条件化的使用指令，形成“指令-项”对。这一设计将原始数据转化为紧凑的显式指令，实现了指令级的内存索引而非原始文本索引，大幅压缩存储。最后，**偏好引导查询转向**模块在检索时将用户查询的嵌入向量朝向最相关偏好的方向进行动态插值融合，生成转向后的查询嵌入，并使用FAISS在指令嵌入空间进行近邻搜索，从而在不修改底层LLM的情况下确保检索结果与用户偏好一致。核心创新在于将个性化重构为一个“选择性记忆构建”问题，通过偏好驱动的粗筛-细验-查询转向流程，实现了2404倍的内存压缩、20.17个百分点的偏好遵循准确率提升以及33.33倍的检索延迟降低，并在流式更新场景下将内存控制在1MB以内。

### Q4: 论文做了哪些实验？

论文在四个基准测试（PrefWiki、PrefRQ、PrefEli、PrefEval）上评估了EPIC系统，涵盖对话、辩论、解释和推荐任务。实验设置包括：对比方法分为三类——标准RAG（BM25、Contriever、NV-Embed-v2）、索引增强RAG（RAPTOR、HippoRAG、HippoRAG 2）和偏好条件RAG（Pref-QR、PBR）。评估指标包括偏好遵循准确率、内存占用、检索延迟和索引延迟，使用LLaMA 3.3 70B-Instruct作为评估器。主要结果：EPIC在所有基准和三种LLM后端（Qwen3-4B、Llama-3.1-8B、gpt-oss-20b）上一致取得最高准确率，相比NV-Embed-v2平均提升20.17个百分点。效率方面，EPIC将索引内存减少2404倍，检索延迟降低33.33倍。消融实验显示，语义粗过滤（C）主要节省内存（3.95-77.68倍压缩），偏好对齐细验证（F）提升准确率13.22-33.69个百分点，偏好引导查询导向（S）额外提升0.78-4.03个百分点且不增加存储。在Jetson Orin Nano 8GB上的流式实验中，EPIC维持低于1MB内存占用，检索延迟29.35ms/查询，索引延迟102.67ms/项，并在偏好漂移下保持高准确率。与HippoRAG 2集成的实验表明EPIC组件可即插即用于结构化RAG管道。

### Q5: 有什么可以进一步探索的点？

EPIC通过将用户偏好作为核心索引单元，显著压缩了信息但可能丢失了重要但非偏好相关的上下文，例如在医疗咨询中用户偏好的治疗方式之外，潜在的紧急症状信息可能被过滤。未来可探索动态偏好权重机制，根据检索任务自动调整偏好与通用信息的保留比例。当前方法假设偏好相对稳定，但用户兴趣会随时间演变（例如从关注咖啡测评转向茶道），需要引入增量式偏好退化建模。此外，EPIC仅基于显式偏好对齐，可进一步融合隐性行为序列（如应用使用时长、点击模式）构建多维偏好图谱。在设备端部署时，可考虑联邦学习框架让多个设备协同更新通用偏好模板，同时本地保持个性化差异，以缓解冷启动问题。

### Q6: 总结一下论文的主要内容

随着大型语言模型驱动的个人AI代理兴起，设备端部署对隐私与响应速度至关重要。这些代理需基于设备本地个人上下文生成回复，但严格的内存限制使得核心瓶颈从“如何使用检索信息”转变为“存储什么”。论文提出EPIC框架，聚焦用户偏好这一紧凑且稳定的个人上下文形式，贯穿检索增强生成（RAG）全流程。EPIC通过语义粗过滤快速剔除无关数据，再利用偏好对齐精验证确保语义一致性，最后通过查询引导将查询向量向偏好方向偏移，实现高效对齐。在涵盖对话、辩论、推荐等四个基准上，EPIC将索引内存缩减2404倍，偏好遵循准确率提升20.17个百分点，检索延迟降低33.33倍。设备端实验中内存占用低于1MB，流式更新时每次查询仅需29.35毫秒。该工作证明了在严格资源约束下，通过偏好导向的存储构建可显著提升个性化RAG的实用性与效率，为设备端个人AI代理奠定了技术基础。
