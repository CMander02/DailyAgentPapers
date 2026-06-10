---
title: "Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory"
authors:
  - "Suozhao Ji"
  - "Baodong Wu"
  - "Zehao Wang"
  - "Lei Xia"
  - "Qingping Li"
  - "Ruisong Wang"
  - "Wenbo Ding"
  - "Zhenhua Zhu"
  - "Boxun Li"
  - "Guohao Dai"
  - "Yu Wang"
date: "2026-06-09"
arxiv_id: "2606.10677"
arxiv_url: "https://arxiv.org/abs/2606.10677"
pdf_url: "https://arxiv.org/pdf/2606.10677v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM Agent记忆"
  - "长时记忆架构"
  - "记忆维护与检索"
  - "Agent推理"
  - "主题文档管理"
  - "迭代检索"
relevance_score: 9.5
---

# Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory

## 原始摘要

Long-term LLM agents need persistent memory that can track changing facts and provide relevant evidence across sessions. Existing memory systems often store observations as isolated records, summaries, or indexed fragments, which makes evidence aggregation, fact revision, and memory maintenance difficult. We propose Infini Memory, a maintainable text-based persistent memory architecture that treats agent memory as topic-structured documents. Each topic document serves as a semantic unit for collecting related evidence, preserving metadata, and revising facts over time. New observations are first staged in a buffer and periodically consolidated into coherent textual contexts. At inference time, an agentic retrieval procedure lets the LLM read memory through iterative tool calls rather than a single retrieval step. On MemoryAgentBench, Infini Memory achieves 64.7% overall score. Ablations show that topic-structured maintenance and iterative evidence inspection improve complementary aspects of long-term memory use.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决长期LLM代理在持久化记忆管理方面面临的核心问题。研究背景是LLM代理需要跨会话持续运行，而模型的上下文窗口只能处理单次输入，无法自主决定信息的保留、修订和组织。现有记忆系统通常采用独立记录、摘要或索引片段的形式存储观察结果，这些方法存在四个主要不足：一是记忆碎片化，关于同一用户或事件的证据分散在多个小记录中；二是记忆冲突，新旧观察结果共存且未调和；三是压缩损失，摘要化处理削弱了时间顺序和来源线索；四是检索不足，基于向量相似性或固定top-k的检索返回孤立片段，缺乏足够的多跳推理上下文。为了弥补这些不足，论文提出了Infini Memory，一种可维护的基于文本的持久化记忆架构。该架构将代理记忆视为主题结构化文档，每个主题文档作为一个语义单元来收集相关证据、保存元数据并随时间修订事实。新观察先存入缓冲区，再定期整合到连贯的文本上下文中，推理时通过迭代工具调用来检索记忆，而非单次检索步骤。核心目标是实现证据聚合、事实修订和记忆维护的可操作性，从而提升长期记忆使用的整体表现。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为以下几类：

1.  **持久记忆系统类**：以 MemGPT、MemoryBank、Mem0 为代表。这些系统通过虚拟上下文管理、遗忘曲线或动态提取来存储记忆，但通常将记忆存储为紧凑条目、摘要或索引片段，这导致后续的事实修订和证据重构困难。本文*Infini Memory*的不同之处在于，将记忆视为可维护的主题文档，便于事实修订和证据聚合。

2.  **结构化记忆组织类**：包括 HippoRAG-v2、REMem、A-MEM（受Zettelkasten方法启发）等。它们使用图结构、原子笔记或关联链接来改善记忆组织，但依赖原子笔记或图结构作为主要载体。本文*Infini Memory*则强调使用纯文本主题文档和显式的合并操作，更注重可解释性和基础设施的简洁性。LightMem 也按阶段处理记忆，但本文在强调离线维护的同时，更注重在线合并操作。

3.  **检索方法类**：传统方法依赖向量相似度或固定 top-k 检索，可能返回孤立片段且难以进行时态推理或矛盾解决。REMem 和 A-MEM 已采用更主动的检索流程（如代理检索器或动态创建链接）。*Infini Memory* 则进一步扩展了读取路径，允许LLM通过迭代调用工具、检查中间结果、扩展局部上下文来逐步组装证据。

4.  **评测基准类**：LoCoMo 和 LongMemEval 评估长上下文回忆和时态理解，但未完全隔离增量存储和检索的操作能力。MemoryAgentBench 更直接地评估了增量交互下的四项核心能力（准确检索、学习、长期理解、选择性遗忘），*Infini Memory* 以此作为主要评测基准。

### Q3: 论文如何解决这个问题？

Infini Memory通过将智能体持久记忆组织为主题化文本文档（Topic Documents）来解决长期记忆维护中的证据聚合、事实修订和记忆维护难题。其核心架构包含一个分阶段的内存管道，由四个关键组件构成：

首先，**主题文档**作为基本语义单元，每个文档包含元数据头（ID、摘要、时间戳等）和层次化正文（主题/子主题标题下的无序列表条目）。每条记忆条目携带序列号、时间戳和来源等元数据，支持显式的顺序更新和修订操作，避免了孤立记录缺乏上下文或单一时间线日志难以维护的问题。

其次，**写作与整合流程**引入CURRENT缓冲区作为短期记忆池，避免频繁的即时写入操作。新观察先追加到缓冲区，当达到token阈值或时间窗口时触发刷新，重写为结构化的REWRITE_CURRENT草稿，在此阶段完成局部条目的去重、合并和矛盾解决。随后，路由规划器决定将草稿块分配到现有主题文档或创建新文档，同时处理事实更新关系。

第三，**检索模块**提供混合和智能体两种变体。混合版本（H）结合LLM摘要选择与BM25分区检索；智能体版本（A）允许LLM通过迭代调用内存工具（全局搜索、文档内搜索、目录检查、行范围读取）进行多步证据收集。该设计支持从匹配条目扩展到所在块上下文，并通过终止条件（证据充分、迭代次数上限等）平衡计算开销。

最后，**结构化文本后端**作为默认存储，保持可读性、可编辑性和可移植性，同时允许扩展向量搜索、图谱遍历等专业检索后端。周期性合并分裂操作维持文档的适度规模，并刷新摘要元数据以支持后续路由和检索。该架构在MemoryAgentBench上达到64.7%的总体得分，消融实验表明主题化维护和迭代证据检查分别提升了长期记忆的互补方面。

### Q4: 论文做了哪些实验？

论文在MemoryAgentBench基准上评估了Infini Memory（简称\nickname{}），基准涵盖准确检索（AR）、测试时学习（TTL）、长程理解（LRU）和选择遗忘（SF）四种能力。使用gpt-5-mini作为基座模型，采用LLM-as-Judge协议以gpt-5进行二元正确性判断。对比方法包括RAPTOR、MemoRAG、HippoRAG-v2、Mem0、MemGPT、LightMem和REMem七种基线，均采用4096词块策略。主实验结果显示，\nickname{}-A（全量版）在MemoryAgentBench上取得64.7%的总分，比最强基线高出19.2个百分点，在四项能力上分别提升+12.5%（AR）、+4.4%（TTL）、+25.4%（LRU）、+26.5%（SF）。在LongMemEval消融实验中，混合版\nickname{}-H（61.3%）比纯摘要检索（41.7%）提升明显；移除结构维护（无split/merge）后准确率从76.0%降至69.3%，下降6.7个百分点；将检索从混合策略升级为智能体检索（\nickname{}-A）进一步增加3.3个百分点至79.3%。分割阈值实验显示，阈值设为5000词块时最优（76.0%），低于1000或高于9000均导致性能下降。多跳选择性遗忘测试中，单跳（FC-SH）和双跳（FC-MH）准确率分别为81.0%和35.0%，揭示了跨文档一致性的结构性局限。

### Q5: 有什么可以进一步探索的点？

基于该论文，未来可进一步探索的方向包括：首先，当前主题文档的生成和合并主要依赖LLM自身，缺乏对外部知识图谱或结构化记忆的整合，可以引入知识蒸馏或混合检索来提升证据聚合的准确性。其次，当交互轮次剧增时，缓冲区合并与主题拆分策略的复杂度会显著上升，未来可设计自适应的增量维护算法，平衡时效性与资源消耗。再者，当前评估仅覆盖图书阅读、对话等任务，扩展到多模态（如视觉、代码）和开放域决策场景将更具挑战。此外，迭代工具调用的推理成本较高，可探索基于模型置信度的早停机制或分层注意力剪枝。最后，长期事实修正与选择性遗忘的鲁棒性仍需更细粒度的实验验证，例如对抗性事实干扰下的记忆漂移问题。

### Q6: 总结一下论文的主要内容

Infini Memory提出了一种面向长期LLM智能体的可维护持久记忆架构，将智能体记忆建模为按主题组织的文本文档。核心问题是现有记忆系统将观察存储为孤立记录或摘要，导致证据聚合、事实修订和记忆维护困难。方法上，新观察先暂存于缓冲区，定期合并为连贯的文本上下文；推理时通过迭代工具调用实现智能体检索，使LLM能逐步读取记忆而非单步检索。在MemoryAgentBench基准上，该方法取得64.7%总体得分，其中准确检索子任务达81.2%，在事实回忆、测试时学习和选择性遗忘上有显著提升。消融实验表明，主题结构化维护和迭代证据检查分别改善了长期记忆使用的互补方面。该工作说明持久智能体记忆质量既依赖于记忆维护方式也依赖于证据检索策略。
