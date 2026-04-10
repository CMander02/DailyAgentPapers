---
title: "MemCoT: Test-Time Scaling through Memory-Driven Chain-of-Thought"
authors:
  - "Haodong Lei"
  - "Junming Liu"
  - "Yirong Chen"
  - "Ding Wang"
  - "Hongsong Wang"
date: "2026-04-09"
arxiv_id: "2604.08216"
arxiv_url: "https://arxiv.org/abs/2604.08216"
pdf_url: "https://arxiv.org/pdf/2604.08216v1"
categories:
  - "cs.MA"
tags:
  - "推理增强"
  - "记忆机制"
  - "长上下文处理"
  - "测试时优化"
  - "CoT"
  - "检索增强生成"
relevance_score: 8.0
---

# MemCoT: Test-Time Scaling through Memory-Driven Chain-of-Thought

## 原始摘要

Large Language Models (LLMs) still suffer from severe hallucinations and catastrophic forgetting during causal reasoning over massive, fragmented long contexts. Existing memory mechanisms typically treat retrieval as a static, single-step passive matching process, leading to severe semantic dilution and contextual fragmentation. To overcome these fundamental bottlenecks, we propose MemCoT, a test-time memory scaling framework that redefines the reasoning process by transforming long-context reasoning into an iterative, stateful information search. MemCoT introduces a multi-view long-term memory perception module that enables Zoom-In evidence localization and Zoom-Out contextual expansion, allowing the model to first identify where relevant evidence resides and then reconstruct the surrounding causal structure necessary for reasoning. In addition, MemCoT employs a task-conditioned dual short-term memory system composed of semantic state memory and episodic trajectory memory. This short-term memory records historical search decisions and dynamically guides query decomposition and pruning across iterations. Empirical evaluations demonstrate that MemCoT establishes a state-of-the-art performance. Empowered by MemCoT, several open- and closed-source models achieve SOTA performance on the LoCoMo benchmark and LongMemEval-S benchmark.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在处理海量、碎片化长上下文进行因果推理时，普遍存在的严重幻觉和灾难性遗忘问题。研究背景是，尽管模型的上下文窗口已扩展到百万令牌级别，但模型在长程推理任务中仍表现不佳，经常遗忘早期信息、丢失远距离因果依赖，并在需要综合分散证据时产生幻觉。现有方法，如检索增强生成，通常将检索视为静态、单步的被动匹配过程。这导致两个根本瓶颈：一是“长上下文搜索建模困境”，静态知识库在关系建模中遭受严重的语义稀释；二是“上下文碎片化”，单一粒度的检索策略要么引入过多噪声，要么剥离关键背景信息，导致检索成功率与信息密度失衡。这些不足的根源在于当前机制将检索与推理割裂，视为被动匹配。

因此，本文的核心问题是：如何从根本上重新定义长上下文推理过程，以克服静态检索导致的语义稀释和上下文碎片化。论文提出的解决方案是MemCoT，这是一个测试时记忆扩展框架，其核心思想是将长上下文推理转化为一种迭代的、有状态的信息搜索过程，使记忆从被动数据仓库转变为驱动推理的引擎，从而实现可追溯、可修正的推理。

### Q2: 有哪些相关研究？

本文的相关工作主要集中在长时记忆机制与LLM智能体结合的领域，可大致分为以下几类：

**1. 基础架构与扩展方法**：早期工作如MemGPT，受操作系统启发，采用分页和分段管理长上下文。Mem0等可扩展架构通过动态整合记忆状态来突破固定上下文窗口的限制。这些方法侧重于静态存储与基础检索，而本文的MemCoT则将其重构为迭代的、有状态的信息搜索过程。

**2. 结构化与层次化记忆**：为提升记忆的主动性，研究转向层次化表示。例如，G-Memory使用三层图层次管理智能体协作，MemGAS提出动态多粒度路由以管理上下文噪声。Mnemis则将记忆转化为可导航的逻辑地图。本文的MemCoT与之有相似的结构化思想，但通过独特的“Zoom-In证据定位”与“Zoom-Out上下文扩展”多视角感知模块，更专注于因果推理中的证据定位与结构重建。

**3. 轻量化与高效利用**：针对复杂记忆构建的计算开销，CoM等框架倡导轻量存储与复杂利用相结合，将记忆片段组织成连贯的推理路径。本文的MemCoT通过任务条件化的双短时记忆系统（语义状态记忆和情景轨迹记忆）实现动态查询分解与剪枝，在高效迭代搜索方面进行了深化。

**4. 动态与自演化记忆**：最新趋势是记忆的动态生命周期管理。例如，CompassMem将持续体验组织成显式事件图并不断更新；MemoryBank依据艾宾浩斯遗忘曲线选择性强化记忆以保持长期一致性；MemGen、MemSkill和MemEvolve则将记忆重构为可学习的、与推理共演的生成状态或技能。本文的MemCoT与这一方向高度相关，其短时记忆系统记录历史搜索决策以动态引导过程，同样强调记忆在推理中的主动与演化角色，但更聚焦于测试时（test-time）通过记忆驱动思维链来实现规模扩展这一具体目标。

综上，MemCoT在吸收层次化、结构化、动态化记忆思想的基础上，创新性地将长上下文推理转化为迭代的状态搜索，并通过多视角长时感知与双短时记忆系统，专门针对缓解幻觉和灾难性遗忘问题，与同类工作形成区别。

### Q3: 论文如何解决这个问题？

MemCoT通过一个迭代的、状态感知的“记忆-推理”循环框架来解决大语言模型在长上下文因果推理中的幻觉和遗忘问题。其核心是将传统静态、单步的检索匹配过程，重新定义为动态、多步的主动信息搜索与状态演化过程。

整体框架是一个循环结构，每次迭代包含三个核心模块：感知模块、演化模块和判断模块。感知模块负责从长期记忆中深度提取信息；演化模块负责提炼高价值语义和轨迹信息，更新短期记忆状态；判断模块评估当前记忆状态是否足以回答问题，若不足则生成下一个子查询以开启新一轮循环。这有效地将复杂的多跳推理分解为可处理的子问题。

关键技术体现在两个核心设计上。首先是**多视角长期记忆感知模块**。它采用分层聚合策略：先通过“聚焦检索”定位最相关的细粒度文本块；再通过“上下文扩展”检索相邻窗口，恢复周围的因果结构语义；若涉及视觉记忆，则触发“全景视觉定位”模块，利用OCR等技术提取多模态宏观结构信息。这种“先聚焦再扩展”的方法，平衡了检索精度与上下文完整性。

其次是**任务条件化的双短期记忆系统**。短期记忆状态包含语义记忆和情景轨迹记忆。语义记忆存储从长期记忆中提取的事实信息；情景轨迹记忆则记录历史搜索决策和失败的查询路径。在判断模块中，系统会分析轨迹记忆中的失败路径，以理解推理缺口，并动态更新查询。更新操作主要包括两种：对复杂意图进行**分解**，将其拆分为原子子查询；以及对已解决的部分进行**剪枝**，聚焦于缺失证据。这确保了后续查询能精准对准推理缺陷，避免冗余搜索，最大化检索效能。

MemCoT的创新点在于：1）将检索从被动匹配转变为主动的、状态感知的搜索过程；2）通过“聚焦-扩展”的多视角感知机制，有效缓解了语义稀释和上下文碎片化；3）利用双短期记忆系统（特别是情景轨迹记忆）实现查询的动态分解与剪枝，引导推理状态高效演化。实验表明，该框架在多个基准测试上达到了最先进的性能。

### Q4: 论文做了哪些实验？

论文在LoCoMo和LongMemEval-S两个长上下文基准上进行了实验。实验设置方面，使用了闭源模型GPT-4o-mini和开源模型Qwen2.5-14B/Qwen2.5-7B作为基础响应器，检索模块采用LightRAG（Top-K=10），最大演化迭代次数J设为8，在LongMemEval-S上将相邻窗口大小W增至15以捕获多会话依赖。

对比方法包括：Full Context（全上下文）、RAG、A-Mem、EpMem、Mem0、MemoryOS、MemVerse、CompassMem、CAM、Zep、Nemori、EMem-G和Mnemis等基线。

主要结果：在LoCoMo基准上，MemCoT取得了SOTA性能。例如，使用Qwen2.5-7B时，MemCoT整体F1得分为52.01，显著超过最佳基线MemVerse（33.79），相对提升57.3%。在子任务上，单跳、多跳、开放域和时序推理的F1得分分别为63.99、36.34、33.08和40.06。使用GPT-4o-mini时，MemCoT整体F1达58.03，优于CompassMem（52.18）。在LongMemEval-S基准上，MemCoT使用GPT-4o-mini取得了88.0的整体得分（LLM-as-a-Judge评分），超越Mnemis（87.2）和EMem-G（77.9），在SSU（98.5）、MS（79.6）、TR（89.4）和SSA（100.0）等细分任务上表现优异。

消融实验验证了核心模块的重要性：移除zoom-out模块（ψ_z-o）导致整体F1从58.03降至53.89；移除视觉模块（ψ_vis）则降至56.19。超参数分析表明，相邻窗口大小W在4-8时性能最佳，过大（>8）会引入噪声；精细检索的Top-K值在10-15时效果最好。

### Q5: 有什么可以进一步探索的点？

MemCoT在长上下文推理中引入了动态记忆机制，但仍存在若干可探索的方向。首先，其多视图长时记忆感知模块依赖预定义的缩放策略，未来可研究自适应缩放机制，根据查询复杂度动态调整证据定位与上下文扩展的粒度。其次，短时记忆系统虽能记录搜索轨迹，但未显式建模记忆的置信度与不确定性，可能导致错误累积；引入贝叶斯推理或不确定性量化可提升决策鲁棒性。此外，框架的计算开销较大，尤其在迭代搜索中可能影响实时性，需探索轻量化记忆压缩或分布式检索优化。从应用层面看，MemCoT目前专注于问答式推理，未来可扩展至对话、规划等序列决策任务，并探索跨模态记忆整合（如视觉-语言上下文）。最后，论文未深入探讨记忆的遗忘与更新机制，如何平衡历史信息与新证据的动态权重，是实现“自进化”系统的关键挑战。

### Q6: 总结一下论文的主要内容

本文提出MemCoT框架，旨在解决大语言模型在长上下文因果推理中存在的幻觉和灾难性遗忘问题。现有方法通常将检索视为静态、单步的被动匹配过程，导致语义稀释和上下文碎片化。MemCoT的核心贡献是将长上下文推理重新定义为迭代的、有状态的信息搜索过程，通过记忆驱动实现测试时扩展。

方法上，MemCoT引入了多视图长期记忆感知模块，支持“聚焦”证据定位和“远观”上下文扩展，先确定相关证据位置，再重建推理所需的因果结构。同时，框架采用任务条件化的双短期记忆系统，包括语义状态记忆和情节轨迹记忆，动态记录历史搜索决策，指导查询分解与剪枝。

实验表明，MemCoT在LoCoMo和LongMemEval-S等基准测试中取得了最先进的性能，显著提升了多个开源与闭源模型的长上下文推理能力，为解决大模型在碎片化长文本中的记忆与推理瓶颈提供了有效方案。
