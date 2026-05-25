---
title: "DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback"
authors:
  - "Yunpeng Dong"
  - "Jingkai He"
  - "Yuze Hou"
  - "Dong Du"
  - "Zhonghu Xu"
  - "Si Yu"
  - "Yubin Xia"
  - "Haibo Chen"
date: "2026-05-21"
arxiv_id: "2605.22781"
arxiv_url: "https://arxiv.org/abs/2605.22781"
pdf_url: "https://arxiv.org/pdf/2605.22781v1"
categories:
  - "cs.OS"
  - "cs.AI"
tags:
  - "Agent Sandbox"
  - "Checkpoint/Rollback"
  - "OS-level Abstraction"
  - "State Exploration"
  - "LLM Agent Infrastructure"
relevance_score: 9.5
---

# DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback

## 原始摘要

LLM-powered AI agents require high-frequency state exploration (e.g., test-time tree search and reinforcement learning), relying on rapid checkpoint and rollback (C/R) of the complete sandbox state, including files and process state (e.g., memory, contexts, etc.). Existing mechanisms duplicate the entire state, causing hundreds of milliseconds to seconds of latency per C/R, which severely bottlenecks deep search and large-scale fan-outs.
  This paper observes that subsequent checkpoints in AI agents are highly similar. Therefore, instead of full duplication, a sandbox should only duplicate the changes between consecutive checkpoints (Key Insight). However, it is non-trivial to realize the idea, mainly due to the missing OS supports. This paper proposes a new OS-level abstraction, DeltaState, to enable the change-based transactional C/R for AI agents with two co-designed OS mechanisms. First, DeltaFS enables change-based filesystem C/R by organizing the file states into layers and dynamically freezing the writable layer and inserting a new one during checkpoint, reducing file updates to copy-on-write, and making rollback a simple layer switch. Second, DeltaCR enables change-based process state C/R using incremental dumps, and accelerates rollback by bypassing traditional pipelines to directly fork() from a frozen template process. We then present DeltaBox, a novel agent sandbox achieving millisecond level C/R through the two new mechanisms. Evaluations on SWE-bench and RL micro-benchmarks show DeltaBox completes checkpoint and rollback in millisecond-level latency (14ms and 5ms, respectively), empowering agents to explore substantially more nodes under fixed time budgets.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决LLM驱动的AI智能体在高频状态探索（如测试时树搜索和强化学习）过程中，由于沙箱环境完整状态（包括文件系统和进程状态）的检查点与回滚（C/R）操作延迟过高，严重制约深度搜索和大规模并行探索效率的问题。现有方法如Docker提交、CRIU进程快照、微型虚拟机快照等，均采用全量状态复制机制，导致每次C/R操作需要数百毫秒至数秒，成为系统瓶颈。论文的核心洞察在于，AI智能体工作负载中连续检查点之间的状态具有高度相似性，仅存在微小的增量变化。因此，本文提出不应复制整个状态，而应仅复制连续检查点之间的变更部分。为解决这一难题，论文提出了新的操作系统层抽象DeltaState，并设计了两个协同机制：DeltaFS实现基于变更的文件系统C/R，通过动态层切换将文件更新降级为写时复制；DeltaCR实现基于增量的进程状态C/R，利用冻结模板进程的fork()加速回滚。最终构建的DeltaBox沙箱系统实现了毫秒级的C/R延迟（检查点约14ms，回滚约5ms），使智能体在固定时间预算内能够探索更多节点。

### Q2: 有哪些相关研究？

相关研究主要分为方法类、应用类和系统类。

**方法类**：Git stash/branch 提供文件级语义版本控制，但无法处理二进制文件和进程状态；LangGraph Checkpointer 通过序列化 Python 图状态实现毫秒级逻辑检查点，但无法撤销文件修改等物理副作用，与 DeltaBox 是互补关系而非竞争。Firecracker VM 快照能捕获完整客户机状态，但粒度是整个虚拟机，导致大量无关内存被备份，延迟达 200ms-2s。

**系统类**：Docker commit + restart 和 shutil.copytree 仅提供文件系统快照，丢失进程内存状态，需重放完整历史。Btrfs/LVM 快照支持文件系统版本但缺少进程状态。DSec 通过 WAL 重放恢复，延迟与重放深度成正比。CubeSandbox 的快照延迟达 148-226ms 且未实现事件级回滚。DeltaBox 的关键区别在于观察到 AI agent 中连续检查点高度相似，因此仅复制变化量，通过 DeltaFS 和 DeltaCR 分别实现基于层的文件系统和基于增量转储的进程状态 C/R，达到 14ms 检查点和 5ms 恢复的毫秒级延迟，且写放大仅 4KB。

**应用类**：SWE-bench、OSWorld、AgentBench 等评测基准中，现有系统如 SWE-agent 仅用 Git 存储文件版本，OpenHands、Aider 等只能线性执行，缺乏中间状态回滚能力。MCTS 和 LATS 等搜索策略在进程状态环境中原需 OS 级 C/R 操作，DeltaBox 填补了这一空白。

### Q3: 论文如何解决这个问题？

论文通过引入DeltaBox系统，实现了毫秒级的沙箱检查点与回滚。核心方法是基于观察到的AI代理工作负载中连续检查点高度相似的特点，仅复制状态之间的变化而非完整复制。整体架构分为四层：第一层为基础存储层，采用支持reflink的XFS实现块级写时复制，避免写放大；第二层为DeltaFS文件系统层，扩展自Linux overlayfs，通过动态冻结可写层并插入新层来实现基于变化的文件系统检查点，回滚只需切换层栈；第三层为DeltaCR进程状态管理层，基于CRIU，采用增量转储和模板进程fork()加速回滚；最上层为状态管理器协调两层保证一致性。关键技术包括：DeltaFS的运行时层栈重配置、懒切换机制处理已打开文件；DeltaCR的双路径检查点（异步CRIU增量转储和模板创建fork()）、有界模板池管理、异步预热线程吸收写时复制故障、以及网络代理守护进程解耦LLM I/O。创新点在于实现了基于变化的原子事务性检查点/回滚，使检查点和回滚延迟分别降至14ms和5ms，在固定时间预算下使代理能探索更多节点。

### Q4: 论文做了哪些实验？

论文在SWE-bench和RL微基准测试上评估了DeltaBox。实验设置包括对比完整系统（克隆/迁移）和基于写时复制的文件系统（如overlayfs）。在SWE-bench上，DeltaBox实现了14ms的检查点和5ms的回滚延迟，而完整克隆需要数百毫秒到数秒。在RL微基准测试中，通过测试状态探索（树搜索和强化学习）的节点数，DeltaBox在固定时间预算下比基线系统探索了显著更多的节点。主要结果包括：检查点延迟从数百毫秒降低至14ms（约20-70倍提升），回滚延迟降至5ms；在SWE-bench任务中，DeltaBox的SWE-AGENT成功率与基线相当，但探索深度大幅增加。RL微基准测试显示，DeltaBox在相同时间内能完成超过1000次状态切换，而传统方法仅支持约50次。这些实验验证了基于增量状态捕获（DeltaState抽象）的毫秒级C/R能力，证明其能有效支持高频率状态探索场景。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在：当前系统仅支持单进程状态快照，对分布式Agent或多进程协作场景支持不足；change detection机制在文件频繁小改动场景下可能引入额外开销；rollback后的进程状态一致性验证机制缺失。未来研究方向包括：1) 扩展支持分布式Agent的协调式C/R，设计跨节点的原子性快照协议；2) 探索基于增量内存页粒度的更精细状态追踪，结合eBPF实现零拷贝差异检测；3) 通过预加载热数据和智能预判层切换策略，将C/R延迟压缩至亚毫秒级；4) 构建分层验证架构，在rollback后自动检测文件系统与进程状态的一致性冲突。此外，可结合预测性增量预取技术，在checkpoint时同步生成后续节点可能需要的差异数据，进一步降低多步回溯的累积延迟。

### Q6: 总结一下论文的主要内容

本文针对 AI 智能体在高频状态探索（如树搜索、强化学习）中由于沙箱完整状态检查点/回滚（C/R）耗时百毫秒至秒级而成为性能瓶颈的问题，提出了 DeltaBox 系统。核心洞察在于智能体工作负载中，后续检查点与前一状态高度相似，仅存在微小增量变化。基于此，论文提出“DeltaState”这一新的操作系统抽象，将文件系统和进程状态视为基于变更的事务性状态对，并设计了两种协同机制：DeltaFS 通过分层文件系统实现变更型文件状态 C/R，利用运行时热层切换将文件更新简化为写时复制，回滚等效于层切换；DeltaCR 通过增量转储和从冻结模板进程直接 fork() 绕过传统管线，实现毫秒级进程状态回滚。实验表明，DeltaBox 实现了 14ms 的检查点和 5ms 的回滚延迟，将状态管理开销从轨迹时间的 47-77% 降至 3-6%，显著提升了智能体在固定时间预算内的搜索节点数。该工作为可扩展的、有状态的 AI 智能体基础设施提供了新的路径。
