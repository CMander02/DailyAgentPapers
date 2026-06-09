---
title: "Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents"
authors:
  - "Tianxiang Fei"
  - "Mingyang Song"
  - "Mao Zheng"
  - "Xiang Yu"
date: "2026-06-08"
arxiv_id: "2606.09483"
arxiv_url: "https://arxiv.org/abs/2606.09483"
pdf_url: "https://arxiv.org/pdf/2606.09483v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "记忆系统"
  - "双过程理论"
  - "认知架构"
  - "长期记忆"
  - "自我进化"
  - "信念追踪"
  - "模式抽象"
relevance_score: 9.2
---

# Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents

## 原始摘要

Long-term memory for an LLM agent is more than retrieving the right passage at the right time. Current memory systems collapse belief revision, causal coupling, and cross-domain abstraction into a single retrieval surface tuned for surface recall, and consequently struggle on implicit personalisation that requires reasoning over how a user has evolved. We propose DCPM, which reorganises agent memory along a cognitive capability hierarchy ascending from raw inputs and atomic facts, through diachronic belief trajectories and identity, to domain schemas, latent intentions and cross-domain patterns. The hierarchy is driven by two processes inheriting the architectural split of dual-process theory: a synchronous daytime writer (System1) that records belief revisions as doubly linked supersedes chains, and an asynchronous nighttime engine (System2) that induces schemas and intentions and sweeps for cross-domain collisions abstracted into higher-level core schemas. On LongMemEval, PersonaMem and PersonaMem-v2, enabling System2 contributes most where the benchmark rewards implicit cross-session inference (up to +5.20 on PersonaMem-v2) and least on span recall, matching the architectural prediction.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前LLM代理长期记忆系统在认知能力上的根本性缺陷。现有记忆系统，如向量数据库、时序知识图谱等，本质上是将记忆等同于检索，把信念修正、因果耦合和跨领域抽象等复杂认知功能全部压缩到单一的检索平面，只擅长表面的事实回忆。这导致代理无法处理隐式个性化查询，例如无法理解用户信念的演变过程、偏好为何发生转变，以及不同生活领域行为之间的潜在关联模式。问题根源在于混淆了存储型记忆与认知型记忆。本文提出的DCPM系统，基于双过程认知理论和心理理论，构建了一个从原始输入到跨领域核心模式的分层认知记忆架构。其核心是通过分离同步的“日间写入器”（系统1，负责记录信念演变为双向链条）和异步的“夜间引擎”（系统2，负责归纳模式、意图并发现跨领域碰撞），来实现记忆能力的逐步递进，从而解决现有系统无法进行隐式跨会话推理和认知演化的核心问题。

### Q2: 有哪些相关研究？

在相关工作中，本文从三个层面进行了梳理。第一类是**存储与图组织方法**：如MemGPT模拟操作系统页面缓存、Mem0采用原地更新与可选图结构、Zep构建时序知识图谱、A-MEM结合Zettelkasten卡片盒方法、MemoryBank引入遗忘曲线、HippoRAG加入海马体索引。DCPM与这些工作的核心区别在于，它不再局限于存储层或图拓扑，而是沿着认知阶段轴重新组织记忆，在事实层之上引入了历时指针和归纳抽象。第二类是**自演化方法**：包括TSUBASA、SEARL、FileGram以及经验压缩谱系。本文认为DCPM与之正交，因为其核心创新在于通过双过程架构（System1的同步写入与System2的异步演化）实现认知层级跃迁。第三类是**认知架构与评测**：如Generative Agents、Voyager、Reflexion、CoALA等将记忆组织为工作记忆、情景记忆与程序性记忆；DCPM则提出长期记忆内的抽象层级。在评测方面，本文与LongMemEval、PersonaMem等基准测试的区别在于，其设计专门验证了System2对隐式跨会话推理的提升，而非简单的事实召回。

### Q3: 论文如何解决这个问题？

论文提出了DCPM（双过程认知记忆系统），通过模拟人类认知的双过程理论来解决现有记忆系统在隐性个性化推理上的不足。核心架构是两层异步处理机制：同步的System1（日间写入器）和异步的System2（夜间引擎），共享同一个向量数据库和知识图谱。

System1负责实时处理add_memory请求，包含四个步骤：首先将原始输入持久化存入向量存储保证零损耗；然后使用提取LLM（M_e）从当前对话和近期历史中抽取身份项和原子事实；接着用调和LLM（M_r）比较新项与Top-K近邻，决定执行ADD、SUPERSEDE或UPDATE操作；最后批量嵌入更新，并为SUPERSEDE项建立双向supersedes指针链。这种设计实现了时间连贯性，在读取时仅需O(k)遍历即可恢复完整进化弧。

System2在空闲时段异步运行，包含三个阶段：阶段一无LLM预处理，对未纳入图谱的新事实进行两阶段DBSCAN聚类；阶段二使用配备四个工具的归纳代理M_a为每个聚类创建模式（行为规律）或意图（潜在关注点），并添加证据边；阶段三跨域扫描器通过行为抽象和碰撞检测，识别行为相似但语义不同的跨域模式对，诱导出更高级的核心模式。

创新点包括：双层认知能力层次结构（从原始输入到原子事实、信念轨迹、身份、域模式、意图和跨域模式）；双向supersedes链实现版本追踪而非常规原地更新；无LLM的读取路径（仅向量搜索和图遍历）。实验表明System2在隐性跨会话推理任务上贡献最显著（PersonaMem-v2提升达+5.20），而对简单召回任务影响最小。

### Q4: 论文做了哪些实验？

论文在三个长时记忆基准测试上进行了实验：LongMemEval（评估回忆、时间推理、知识更新和弃权）、PersonaMem（32k，评估跨会话的人格一致性响应选择）和PersonaMem-v2（32k，评估隐式偏好推理，是最具区分度的基准）。对比方法包括：(B1) 长上下文智能体（完整对话历史放入上下文窗口），(B2) Mem0（有无图后端），(B3) Zep/Graphiti（时态知识图）。系统配置包括仅使用System1白天写入器（原始、事实和身份存储，带继承链）的DCPM-Lite，以及额外启用System2夜间引擎（模式、意图和跨域核心模式层）的DCPM-Full。使用deepseek-v4-flash和kimi-2.5作为提取/推理模型对，采用无思考评估协议。主要结果（准确率%）：在PersonaMem-v2上，DCPM-Full达到最佳性能（deepseek: 49.36, kimi: 59.30），System2的增益最大（+2.51/+5.20），符合双过程理论预测。消融实验显示，跨域核心模式碰撞贡献约4.1分，模式/意图诱导贡献约1.1分，继承机制贡献约2.9分。DCPM-Full在LongMemEval kimi列上超过长上下文基线5.53分，归因于结构化内存避免中间丢失效应。

### Q5: 有什么可以进一步探索的点？

论文的主要局限在于当前系统设计对特定场景存在明显适应性瓶颈。双空间阈值依赖离线调优而非学习，缺乏自适应能力，未来可探索元学习或在线贝叶斯更新实现阈值动态调整。自然语言表示的schema节点虽可解释但不支持代数运算，一个自然的改进是引入混合表示，将自然语言摘要与结构化槽位结合，从而支持偏好向量的集合运算。对于跨域模式挖掘，当前二次方双空间扫描在领域多样性高时成为计算瓶颈，可考虑图神经网络或注意力机制高效聚合同类模式。此外，系统2的异步引擎带来离线开销，未来可设计增量式schema更新减少冗余计算。更重要的是，当前认知分层编码了跨域核心schema的归纳偏置，对于单领域占主导的用户获益有限，可引入领域权重自适应调整机制。最后，扩展到多语言、具身智能或不确定用户身份等更开放场景将是重要方向。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为DCPM的双过程认知记忆系统，旨在解决当前大规模语言模型（LLM）智能体长期记忆系统仅依赖表面检索，难以处理需要推理用户信念演变的隐式个性化问题。DCPM的核心创新在于将智能体记忆组织在从原始输入到领域模式的认知能力层级上，并借鉴双过程理论设计了两个分离过程：同步的System1记录信念修正链，异步的System2在夜间归纳领域模式、意图并检测跨领域冲突。该方法无需LLM参与的读取路径，实现了高效检索。在LongMemEval、PersonaMem和PersonaMem-v2上的实验表明，System2对隐式跨会话推理任务贡献最大（在PersonaMem-v2上提升高达+5.20），而对跨度回忆任务贡献最小，验证了层级架构的设计预测。这项工作推动了从“记忆即检索”到“记忆即认知”的范式转变，为构建自我进化的智能体提供了新框架。
