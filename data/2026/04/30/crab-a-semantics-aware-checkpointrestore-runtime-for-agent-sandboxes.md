---
title: "Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes"
authors:
  - "Tianyuan Wu"
  - "Chaokun Chang"
  - "Lunxi Cao"
  - "Wei Gao"
  - "Wei Wang"
date: "2026-04-30"
arxiv_id: "2604.28138"
arxiv_url: "https://arxiv.org/abs/2604.28138"
pdf_url: "https://arxiv.org/pdf/2604.28138v1"
categories:
  - "cs.OS"
  - "cs.AI"
tags:
  - "Agent沙箱"
  - "检查点恢复"
  - "OS-Agent语义鸿沟"
  - "eBPF"
  - "故障容错"
  - "Agent运行时"
relevance_score: 9.5
---

# Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes

## 原始摘要

Autonomous agents act through sandboxed containers and microVMs whose state spans filesystems, processes, and runtime artifacts. Checkpoint and restore (C/R) of this state is needed for fault tolerance, spot execution, RL rollout branching, and safe rollback-yet existing approaches fall into two extremes: application-level recovery preserves chat history but misses OS-side effects, while full per-turn checkpointing is correct but too expensive under dense co-location. The root cause is an agent-OS semantic gap: agent frameworks see tool calls but not their OS effects; the OS sees state changes but lacks turn-level context to judge recovery relevance. This gap hides massive sparsity: over 75% of agent turns produce no recovery-relevant state, so most checkpoints are unnecessary. Crab (Checkpoint-and-Restore for Agent SandBoxes) is a transparent host-side runtime that bridges this gap without modifying agents or C/R backends. An eBPF-based inspector classifies each turn's OS-visible effects to decide checkpoint granularity; a coordinator aligns checkpoints with turn boundaries and overlaps C/R with LLM wait time; and a host-scoped engine schedules checkpoint traffic across co-located sandboxes. On shell-intensive and code-repair workloads, Crab raises recovery correctness from 8% (chat-only) to 100%, cuts checkpoint traffic by up to 87%, and stays within 1.9% of fault-free execution time.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决自主智能体在沙箱环境中高效进行检查点与恢复（C/R）所面临的“智能体-操作系统语义鸿沟”问题。研究背景是，现代AI智能体从单轮聊天演进为多步自主执行，通过容器或微虚拟机沙箱进行编译、运行命令等复杂操作，其状态跨越对话历史、文件系统和进程等OS级工件。C/R对于保障容错、抢占式执行、强化学习分支和安全回滚至关重要。现有方法存在两个极端：应用层面的恢复（如仅保存聊天或文件）虽然开销低，但会丢失安装的包、后台进程等OS侧状态，导致恢复后环境不一致，实验显示正确率仅8-13%；而OS/VM层面的全量逐轮检查点虽然正确，但代价高昂，尤其是在密集部署场景下，会因I/O争用导致高达数秒的延迟，无法扩展。本文的核心问题是：需要一种既能保证恢复正确性（捕获所有OS级状态），又低开销且能支持大规模高密度部署的C/R方案。其关键挑战在于，智能体层能看到工具调用却不知其OS效果，OS层能看到状态变化却缺乏上下文判断其恢复相关性，从而无法有效决定哪些轮次真正需要检查点。

### Q2: 有哪些相关研究？

相关研究可分为方法类和应用类。方法类方面，现有C/R方案存在两极分化：一是应用层方法（如LangGraph、Claude Code的聊天记录恢复）仅保留对话历史和文件状态，无法恢复OS运行时状态，导致恢复后环境不一致（本文实验显示Chat-only仅6%成功率，Chat+FS最高48%）；二是OS/VM层方法（如基于Firecracker的E2B、ZFS+CRIU）虽能完整捕获状态，但逐轮全量检查点开销巨大（单次CRIU dump可达秒级，高并发下超47秒），且忽略状态稀疏性。应用类方面，Agent沙箱场景包括故障恢复（FaultRecover）、抢占实例迁移（Spot）、树状RL分支（TreeRL）和投机执行（SpecAct），它们都依赖高效C/R但现有系统无法满足。本文的突破在于：通过eBPF探针在OS层实时检测每轮交互的恢复相关状态变化，利用75%以上轮次无状态变更的稀疏性，实现选择性检查点。相比现有工作，Crab既不像应用层方案忽略OS副作用，也不像系统级方案无差别全量checkpoint，而是构建了弥合agent-OS语义鸿沟的运行时，在shell密集型任务中将恢复正确率从8%提升至100%，同时降低87%的检查点流量。

### Q3: 论文如何解决这个问题？

Crab的核心方法是通过一个宿主级运行时桥接代理与操作系统之间的语义鸿沟，实现语义感知的检查点/恢复。架构包含三个关键组件：协调器（Coordinator）、检查器（Inspector）和检查点/恢复引擎（C/R Engine）。整体框架围绕三个设计原则：语义驱动的检查点、异步检查点执行和宿主级协调。

**核心方法**：通过理解每个turn产生的OS级状态变化，决定是否需要检查点以及所需粒度，并利用LLM推理的等待时间异步执行检查点操作。

**架构设计**：
1. **协调器（Coordinator）**：位于代理与LLM服务之间的控制路径上，作为HTTP反向代理。它拦截代理向LLM的请求以识别turn边界，在转发请求后立即触发检查点决策，并在LLM响应返回时进行完成门控（如果检查点没完成则延迟释放响应）。它还支持紧急信令，将暴露在关键路径上的检查点任务提升优先级。

2. **检查器（Inspector）**：通过eBPF提供OS级语义信号。采用"净变化语义"（net-change semantics），只报告从上一次检查点以来的持久性变化（忽略瞬态效应）。文件系统状态通过eBPF监控系统调用跟踪文件创建、删除、写入等操作；进程状态通过cgroup和内核软脏页跟踪机制检测进程创建/退出和内存修改。

3. **检查点/恢复引擎（C/R Engine）**：包含调度器（Scheduler）、工作者（Workers）和管理器（Manager）。调度器采用反应式调度策略，维护正常和优先级两个队列；工作者使用CRIU和OpenZFS作为后端；管理器维护版本化清单（manifest），将部分检查点组合成可恢复的快照版本，类似git版本历史。

**创新点**：1) 首次实现了turn粒度的语义感知检查点，避免75%以上不必要的检查点；2) 利用LLM推理时间窗口异步执行检查点，隐藏延迟；3) 宿主级协调调度，支持密集沙箱共置场景。

### Q4: 论文做了哪些实验？

论文进行了以下实验：

**实验设置**：基于eBPF的检查点/恢复运行时Crab，运行在Linux容器沙箱上。

**数据集/基准测试**：使用shell密集型和代码修复两类代理工作负载。对比方法包括：仅聊天恢复（应用级）和完整逐轮检查点（系统级）。

**主要结果**：
1. **恢复正确性**：Crab从仅聊天恢复的8%提升至100%完全正确恢复。
2. **检查点流量**：相比完整逐轮检查点，Crab减少了高达87%的检查点流量（因为75%以上的代理轮次不产生需要恢复的状态）。
3. **性能开销**：Crab将检查点与恢复操作与LLM等待时间重叠，最终执行时间仅比无故障执行多1.9%（即性能开销控制在1.9%以内）。
4. **可扩展性**：在密集共置场景下，Crab通过主机级调度引擎有效管理多个沙箱的检查点流量，保持低延迟。

关键数据指标：恢复正确率100%、检查点流量减少87%、性能开销<1.9%。

### Q5: 有什么可以进一步探索的点？

尽管Crab在语义感知的检查点恢复方面取得了显著进展，但其当前设计仍存在若干可探索的方向。首先，eBPF inspector的规则集是静态预定义的，未来可引入自适应的效果分类器，例如通过在线学习动态识别新型工具调用的OS级副作用。其次，当前方案假设所有检查点最终都需要完整的OS状态，但在多分支场景下，可探索差异增量检查点，只记录每个分支相对于公共基线的变化。第三，密集共置场景的调度策略目前仅考虑流量整形，未充分利用LLM等待时间的预测性——可结合请求到达时间预估，实现接近零开销的透明检查点。最后，安全隔离的微虚拟机场景下，建议扩展eBPF监视到guest内核，或利用VMM向host暴露的日志接口，以消除对微内核修改的依赖。这些改进有望在保持100%正确性的同时，进一步将开销压缩到1%以内。

### Q6: 总结一下论文的主要内容

Crab是一个专门为AI Agent沙箱设计的语义感知检查点/恢复运行时系统。论文首先指出当前Agent沙箱状态恢复面临的核心问题：应用层方法（如聊天记录恢复）虽然轻量但会遗漏操作系统级状态（如进程、文件系统），而操作系统级全量检查点虽然正确但成本过高，在密集部署场景下不可扩展。作者揭示了Agent-OS语义鸿沟是根本原因——Agent框架能看到工具调用但看不到OS影响，OS能看到状态变化但缺乏turn级上下文。

Crab的核心贡献是通过三层设计桥接这一鸿沟：1）基于eBPF的Inspector在每个turn结束时检测OS可见效应，判断是否需要检查点及所需粒度；2）Coordinator作为HTTP代理驻留在Agent-LLM路径上，将检查点工作与LLM等待时间重叠；3）C/R引擎在主机范围内调度检查点流量，避免I/O竞争。实验表明，Crab在shell密集型工作负载上实现了100%恢复正确性（相比聊天记录恢复的8%），减少高达87%的检查点流量，且与无故障执行时间相比仅增加1.9%的开销。这项工作为Agent系统的容错、抢占式执行和RL回滚等场景提供了高效的基础设施支持。
