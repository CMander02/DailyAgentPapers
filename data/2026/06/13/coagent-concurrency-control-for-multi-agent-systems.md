---
title: "CoAgent: Concurrency Control for Multi-Agent Systems"
authors:
  - "Hongtao Lyu"
  - "Dingyan Zhang"
  - "Mingyu Wu"
  - "Xingda Wei"
  - "Haibo Chen"
date: "2026-06-13"
arxiv_id: "2606.15376"
arxiv_url: "https://arxiv.org/abs/2606.15376"
pdf_url: "https://arxiv.org/pdf/2606.15376v1"
categories:
  - "cs.DC"
  - "cs.AI"
  - "cs.MA"
tags:
  - "Multi-Agent Systems"
  - "Concurrency Control"
  - "LLM Agents"
  - "Transaction Protocol"
  - "Tool Use"
  - "Coordination"
relevance_score: 9.5
---

# CoAgent: Concurrency Control for Multi-Agent Systems

## 原始摘要

Multi-agent LLM systems -- coding agents, devops agents, document agents -- now routinely run several agents in parallel against the same git tree, Kubernetes cluster, or document. As soon as two of them mutate shared state, they enter the regime classical concurrency control has studied for decades, but classical mechanisms fit LLM agents poorly. A single agent transaction spans minutes of inference, read sets are broad and opaque rather than statically inferable, and the live state agents act on admits neither fork nor buffer, so writes take effect the moment they execute. Locks block long inference intervals; OCC abort-and-retry discards minutes of work on every conflict.
  This paper builds concurrency control on a capability classical transactions lack: the LLM inside each agent can judge whether a conflicting write invalidates its plan, and can repair exactly the operations that depended on it. Control therefore turns advisory: the runtime informs, the agent repairs. Our protocol, MTPO (Monotonic Trajectory Pre-Order), fixes a serialization order at launch, serves each read the order-filtered value, and applies writes speculatively in place; a one-way notification asks an affected reader to re-judge and patch its plan, while the framework mechanically undoes and reorders misplaced writes through the saga-style inverse each tool registers in advance. At quiescence the run is serializable in the pre-decided order. We realize MTPO as CoAgent, toolcall middleware whose privileged ToolSmith grows footprint-declared, undoable tools online. On ten contended workloads, CoAgent stays within 5\% of serial correctness at a $1.4\times$ speedup and near-serial token cost, where 2PL and OCC surrender nearly all concurrency gains; on a bash-only target system, it grows a 25-tool library online and lifts the task pass rate from 45/71 to 63/71 at $0.80\times$ the time and $0.86\times$ the cost.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文《CoAgent: Concurrency Control for Multi-Agent Systems》试图解决多智能体系统中因并发访问共享状态（如同一个Git仓库、Kubernetes集群或文档）导致的数据一致性问题。研究背景是，当前多智能体LLM系统（如编码、运维、文档智能体）已普遍并行运行多个子智能体以提升效率，但这一做法复兴了经典并发控制问题：多个智能体同时对共享状态进行读写，若缺乏协调，会导致类似数据库中的“脏读”、“不可重复读”等异常，最终造成系统状态与任何串行执行结果均不等价。现有方法存在明显不足：串行执行损失并发优势；静态分区写入集合要求提前预知写入内容，不适用于动态规划的智能体；而“分支-合并”策略仅提供弱隔离（如读已提交），无法防止严重异常。因此，论文要解决的核心问题是：如何在多智能体系统中高效地实现可串行化（Serializability）这一理想的一致性属性，同时克服传统并发控制协议（两阶段封锁2PL和乐观并发控制OCC）在此场景下的功能与性能缺陷——2PL的锁持有时间长、阻塞严重，OCC的冲突重做成本高昂，且两者均无法处理已作用在外界状态（如K8s集群）上的写入操作。本文利用LLM的语义理解能力，提出了一种新的“咨询式”并发控制协议MTPO，旨在实现并发效率与数据正确性的平衡。

### Q2: 有哪些相关研究？

本文提出的CoAgent系统与多智能体系统中的并发控制方案密切相关，相关研究可分为以下类别：

1. **经典并发控制机制**：主要包括两阶段锁（2PL）和乐观并发控制（OCC）。2PL通过锁机制阻塞冲突事务，但会导致多智能体中长时间推理间隔的显著延迟；OCC采用“放弃-重试”策略，但在冲突时丢弃已完成的推理工作。CoAgent通过让LLM智能体自主判断冲突影响并进行修补，避免了这些方法的开销。

2. **可序列化与事务协议**：传统分布式系统中的可序列化协议（如严格两阶段锁定、快照隔离）假设事务短且读集可预测，而CoAgent基于MTPO协议，利用LLM的语义理解能力实现轻量级排序和修补，而非强制回滚。

3. **智能体协作与工具编排**：现有多智能体框架（如AutoGPT、MetaGPT）多关注任务分解与工具调用，但未处理并发写冲突。CoAgent通过ToolSmith中间件动态注册工具，记录其写集和逆操作，支持Saga风格的撤销与重排序。

4. **大语言模型推理优化**：相关工作如“自我调试”（Self-Debug）、“反思”（Reflection）等让智能体修正自身输出，CoAgent将此类能力扩展为并发控制机制，实现冲突感知的修补而非简单重试。

与这些工作相比，CoAgent的核心区别在于：将并发控制从“阻塞或放弃”转变为“告知与修补”，利用LLM的语义判断能力取代传统锁和放弃机制，在保持可序列化性的同时显著提升并发效率。

### Q3: 论文如何解决这个问题？

该论文提出的核心方法是MTPO (Monotonic Trajectory Pre-Order)协议，其整体框架基于三个关键创新点构建：预序、过滤读和通知修复。首先，在架构设计上，系统引入预序机制，在启动时为每个agent分配固定优先级σ，使冲突依赖形成有向无环图，彻底避免了无界广播导致的活锁问题。主要模块包括：轨迹管理单元（为每个对象维护按σ排序的写入轨迹T(o)）、工具注册框架（通过ToolSmith在线创建带足迹声明的可逆工具）以及通知引擎。关键技术体现在三个核心规则上：过滤读（Filtered Read）让agent只能读取轨迹中σ≤自身优先级的写入值，确保读取视图稳定；投机写（Speculative Write）允许写入立即生效，但当出现σ序与物理执行序不一致时，框架通过逆操作撤销并重排序错误写入的分段，类似于Saga模式的补偿机制；通知推送（Notification）仅在低σ写入者更新了高σ读取者已读对象时触发单向通知，agent通过自愈能力（A3假设）识别前提冲突并重写依赖操作。该协议在全局静默时保证实际状态与σ序串行执行状态一致，最终通过通知等价性和串行等价性两层证明实现可串行化。创新点在于将传统并发控制的阻塞和重做机制转变为advisor式合作，利用LLM的语义理解能力处理冲突。

### Q4: 论文做了哪些实验？

论文在10个高竞争负载的基准任务上评估了CoAgent系统，主要对比了2PL（两阶段锁）和OCC（乐观并发控制）方法。实验设置包括多智能体并行操作共享的Git仓库、Kubernetes集群或文档系统。核心指标是正确性（与串行执行相比）和加速比/开销。

主要结果：CoAgent在正确性上保持在串行执行的5%以内，同时实现了1.4倍的加速比和接近串行的token成本；而2PL和OCC几乎放弃了所有并发增益。在bash-only目标系统测试中，CoAgent在线扩展了25个工具库，任务通过率从45/71提升至63/71，时间成本降至串行的0.80倍，计算成本降至0.86倍。

实验通过设计包括读集宽泛、写操作实时生效的典型多智能体场景，验证了CoAgent结合LLM判断能力与工具级撤销机制的有效性，证明其在维持事务串行化顺序（MTPO协议）的同时，能避免经典并发控制的高额回滚和锁定开销。

### Q5: 有什么可以进一步探索的点？

这篇论文的局限性和未来探索方向包括几个关键点。首先，MTPO协议依赖LLM的自我修复能力来应对冲突，但LLM的判断准确性和修复质量存在不可预测性，尤其在复杂多步依赖中可能引入新错误。其次，工具注册的“saga式逆操作”要求每个工具预先定义撤销语义，这限制了动态扩展性且对缺乏明确逆操作的工具（如外部API）难以应用。未来可探索方向包括：设计更细粒度的冲突检测机制，例如利用LLM的嵌入表示自动推断读取集与写入集的语义重叠，而非依赖静态声明；开发自适应冲突解决策略，允许系统在“等待修复”与“智能合并”间动态权衡，减少LLM修复开销；引入混合并发控制，将MTPO与悲观锁结合用于关键路径上的短事务（如状态校验），避免长事务阻塞。此外，可尝试将MTPO推广至非事务性场景，如流式环境或部分持久化状态，评估其在线重构工具库时的性能边界。最后，探索多轮修复的收敛性保障，避免无限循环修复导致系统死锁。

### Q6: 总结一下论文的主要内容

这篇论文提出了CoAgent框架，用于解决多智能体LLM系统在执行过程中的并发控制问题。核心贡献在于利用LLM的语义理解能力，设计了一种新的乐观并发控制协议MTPO（单调轨迹偏序）。该协议的关键洞察是，当并发写入导致冲突时，LLM能够判断该冲突是否真正影响其计划，并仅修复依赖冲突数据的部分操作，而非像传统OCC那样全部回滚重试。对于已写入外部世界的错误操作，框架通过预注册的逆操作（saga模式）进行机械撤销和重排序。实验表明，在十个高争用工作负载上，CoAgent在实现接近串行正确性（5%以内）的同时，获得1.4倍加速和接近串行的token成本。相比之下，2PL和OCC几乎丧失了所有并发收益。此外，在一个仅暴露bash接口的目标系统上，CoAgent能在线构建包含25个工具的库，将任务通过率从45/71提升至63/71，同时降低时间和成本。这项工作为多智能体系统的高效、正确并发执行提供了新的范式。
