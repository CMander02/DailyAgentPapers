---
title: "MEMTIER: Tiered Memory Architecture and Retrieval Bottleneck Analysis for Long-Running Autonomous AI Agents"
authors:
  - "Bronislav Sidik"
  - "Lior Rokach"
date: "2026-05-05"
arxiv_id: "2605.03675"
arxiv_url: "https://arxiv.org/abs/2605.03675"
pdf_url: "https://arxiv.org/pdf/2605.03675v1"
categories:
  - "cs.AI"
tags:
  - "Agent记忆"
  - "自主Agent架构"
  - "多级记忆系统"
  - "检索增强"
  - "长期Agent"
  - "智能体评测基准"
relevance_score: 9.0
---

# MEMTIER: Tiered Memory Architecture and Retrieval Bottleneck Analysis for Long-Running Autonomous AI Agents

## 原始摘要

Long-running autonomous AI agents suffer from a well-documented memory coherence problem: tool-execution success rates degrade 14 percentage points over 72-hour operation windows due to four compounding failure modes in existing flat-file memory systems. We present MEMTIER, a tripartite memory architecture for the OpenClaw agent runtime that introduces a structured episodic JSONL store, a five-signal weighted retrieval engine, an attention-attributed cognitive weight update loop, an asynchronous consolidation daemon promoting episodic facts to a semantic tier, and a PPO-based policy framework for adapting retrieval weights (infrastructure validated; performance gains pending camera-ready). On the full 500-question LongMemEval-S benchmark (Wu et al., 2025), MEMTIER achieves Acc=0.382, F1=0.412 with Qwen2.5-7B on a consumer 6GB GPU - a +33 percentage point improvement over the full-context baseline (0.050 -> 0.382, i.e., 5% -> 38%). With DeepSeek-V4-Flash fact pre-population, single-session recall reaches 0.686-0.714, exceeding the paper's RAG BM25 GPT-4o baseline (0.560) on those categories. Temporal reasoning rises to 0.323 and multi-session synthesis to 0.173, demonstrating that structured semantic pre-population qualitatively changes what lightweight retrieval can achieve. All phases run locally on a consumer laptop with a 6GB GPU.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文针对长期运行的自主AI智能体在记忆管理上面临的核心问题展开研究。研究背景是，LLM智能体的应用已从无状态聊天机器人转向需要持续运行多天、维护持久状态并执行工具调用的自主系统。现有方法的不足在于，主流记忆架构（如OpenClaw）仅采用扁平文件结构（20KB的MEMORY.md文件和按天追加的日志），专门为短会话检索设计，无法应对数周连续运行带来的知识积累和优先级排序需求。通过社区问题分析和72小时纵向测量，论文识别出四个复合故障模式：上下文崩溃（容量上限导致信息非优雅丢失）、压缩不连续性（62%的压缩事件导致行为断裂）、结构盲目性（无法区分实体关系与偶然共现）以及缺乏归因循环（工具执行结果从不反馈到记忆条目以改进检索质量）。本文提出的核心解决方案是MEMTIER，一个五阶段分层记忆架构，通过结构化情节JSONL存储、五信号加权检索引擎、注意力归因的认知权重更新循环、异步合并守护进程以及基于PPO的检索权重策略框架，系统性地解决上述四个故障模式，旨在显著提升长期运行智能体的记忆连贯性和任务成功率。

### Q2: 有哪些相关研究？

相关研究主要分为五个方向。**在分层记忆架构方面**，MemGPT借鉴OS分页模式，通过显式中断进行上下文与外部存储的切换；本文与其根本区别在于：（a）采用异步策略驱动的记忆固化而非中断触发；（b）检索策略通过强化学习自适应而非固定不变。H-MEM提出了长上下文推理的记忆层级结构，但未涉及工具增强的智能体场景或可学习的固化策略。**在高效记忆压缩方面**，SimpleMem通过摘要管道在LoCoMo基准上达到F1=0.432的最优token效率；本文确认了LoCoMo在对话具备上下文时对记忆架构不敏感，而采用更严格的LongMemEval-S基准，该基准要求跨53个会话的存储与检索。**在检索增强智能体方面**，RAG及变体采用BM25或密集检索；本文扩展出五信号加权评分函数、基于工具结果的认知权重信号，以及通过PPO从实时奖励中自适应信号权重的策略，而A-MEM仅使用静态评分函数。**在强化学习记忆管理方面**，Memory-R1将RL应用于对话记忆管理；本文将其扩展到智能体工具执行场景，奖励信号来自工具结果而非对话偏好评分，策略目标是检索权重向量。**在记忆评测基准方面**，LoCoMo评估30会话对话记忆，LongMemEval提供500个手动构建问题覆盖五种能力类型，MIRIX提出多智能体记忆系统但缺乏标准化基准评测。

### Q3: 论文如何解决这个问题？

MEMTIER通过三层记忆架构和检索瓶颈分析解决长期运行AI智能体的记忆一致性问题。整体框架采用三分结构：情景层（episodic tier）、语义层（semantic tier）和程序层（procedural tier），由异步合并守护进程（consolidation daemon）将情景事实提升至语义层，实现跨智能体知识共享。核心技术包括五个部分：

1. **结构化情景存储**：采用每日JSONL格式记录包含id、时间戳、会话id、项目、内容、令牌数、提升标志和认知权重（CW ∈ [-1,1]），支持追加写入和项目隔离。

2. **五信号加权检索引擎**：综合语义相似度、BM25相关性（k1=1.5, b=0.75，得分>2.0绕过衰减）、时间衰减（半衰期≈14天）、认知权重和层级提升因子（1.0/1.2/1.4），默认权重向量为[0, 0.35, 0.25, 0.25, 0.15]。

3. **二阶检索机制**：第一阶段用BM25在语义层提取前5个相关会话ID，第二阶段仅加载这些会话的情景条目并全公式评分，将检索池从所有条目缩小至聚焦子集。

4. **基于注意力的认知权重更新**：通过归因循环（attribution loop）在每次智能体会话后更新条目CW，成功调用积累正值，失败积累负值，无需人工标注。

5. **PPO策略框架**：使用近端策略优化自适应调整检索权重，初始15轮训练因循环奖励陷阱和零方差陷阱导致权重未收敛，后续改用直接任务成功奖励（正确+1，错误-1），并初始化σ=0.15强制探索。

创新点在于语义预填充实现164倍事实压缩（从509个降至3.1个/问题），以及在消费级6GB GPU上使用7B模型实现Acc=0.382，比全上下文基线提升33个百分点。消融实验显示语义预填充贡献最大（+0.128 Acc），二阶范围限定次之（+0.038），各信号贡献呈加性非冗余。

### Q4: 论文做了哪些实验？

论文在LongMemEval-S基准测试（500道题）和LoCoMo对话基准（200个QA对）上进行了实验。实验设置包括：使用Qwen2.5-7B模型在消费级6GB GPU上运行，对比方法包括全上下文基线（Full-context-7B）、仅BM25检索的MEMTIER、以及加入语义预填充的MEMTIER。主要结果如下：MEMTIER在LongMemEval-S上达到Acc=0.382、F1=0.412，相比全上下文基线（0.050）提升33个百分点。其中，单会话召回率达到0.686-0.714，超越RAG BM25 GPT-4o基线（0.560）。时间推理提升至0.323，多会话综合提升至0.173。消融实验显示：语义预填充是最关键组件（去除后Acc下降0.128）；最优检索条目数k=2（Acc=0.402）；600 tokens注入预算效果最佳（Acc=0.412）。PPO训练后权重未发生实质性变化（Acc仍为0.382），表明BM25检索架构是性能瓶颈。在LoCoMo上，MEMTIER与基线表现相同（F1=0.120 vs 0.125），证实该基准无法有效区分记忆架构。

### Q5: 有什么可以进一步探索的点？

MEMTIER的核心瓶颈在于BM25检索架构对多跳时序推理的约束。未来可探索以下方向：首先，用密集/混合检索替代稀疏BM25，如接入ColBERTv2或Contriever，使检索阶段能直接捕获语义相似性而非仅靠词项重叠，从而克服PPO权重被BM25分数主导的问题。其次，改进信号融合机制，将BM25分数严格归一化后再与衰减、认知权重等信号组合，或使用可学习的门控网络动态融合多源信号。第三，强化关系抽取：将当前启发式KV模式匹配替换为基于预训练语言模型的细粒度关系抽取器，生成如“happened_after”“caused_by”等结构化标签以提升语义Tier质量。最后，验证扩展性：在更长时间跨度（如7天）和更多Agent类型下测试记忆衰减曲线，并探索异步合并守护进程的非同步频率对检索性能的影响。

### Q6: 总结一下论文的主要内容

长期运行的自主AI代理存在记忆连贯性问题，在72小时运行周期内，由于扁平文件记忆系统的复合故障模式，工具执行成功率下降14个百分点。论文提出MEMTIER，一种为OpenClaw代理运行时设计的三层记忆架构，包含结构化事件JSONL存储、五信号加权检索引擎、注意力归因的认知权重更新循环、将事件事实提升至语义层的异步整合守护进程，以及基于PPO的检索权重自适应策略。在LongMemEval-S完整500题基准测试上，MEMTIER使用Qwen2.5-7B模型在消费级6GB GPU上达到Acc=0.382，F1=0.412，较全上下文基线提升33个百分点（0.05→0.382）。关键发现是存在三层不变性：无论将生成器扩展至284B MoE模型，还是通过PPO动态调优检索权重，性能上限始终受制于BM25检索架构。这表明高精度、结构隔离的记忆（事件层与语义层）是驱动代理长期成功的主要因素，而传统线性组合检索是当前瓶颈。未来工作将转向以召回优先的稠密检索，以解决多会话综合和时序推理难题。
