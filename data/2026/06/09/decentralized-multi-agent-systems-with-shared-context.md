---
title: "Decentralized Multi-Agent Systems with Shared Context"
authors:
  - "Yuzhen Mao"
  - "Azalia Mirhoseini"
date: "2026-06-09"
arxiv_id: "2606.10662"
arxiv_url: "https://arxiv.org/abs/2606.10662"
pdf_url: "https://arxiv.org/pdf/2606.10662v1"
categories:
  - "cs.MA"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "去中心化协调"
  - "共享上下文"
  - "LLM智能体"
  - "SWE-bench"
  - "LongBench"
  - "任务队列"
  - "测试时扩展"
relevance_score: 9.5
---

# Decentralized Multi-Agent Systems with Shared Context

## 原始摘要

Multi-agent systems (MAS) can scale large language model reasoning at test time by decomposing complex problems into parallel subtasks. However, most existing MAS rely on centralized orchestration, where a main agent assigns work, collects outputs, and merges results. As the number of subtasks grows, this controller becomes a communication and integration bottleneck. We propose Decentralized Language Models (DeLM), a MAS framework that decentralizes coordination through parallel agents, a shared verified context, and a task queue. Agents asynchronously claim subtasks, read accumulated progress, perform local reasoning, and write back compact verified updates. The shared context acts as a common communication substrate, enabling agents to build on one another's verified progress without routing every update through a central controller. Empirically, DeLM improves both software-engineering test-time scaling and long-context reasoning. On SWE-bench Verified, DeLM achieves the best performance across Avg.@1, Pass@2, and Pass@4, with gains of up to 10.5 percentage points over the strongest baseline, while reducing cost per task by roughly 50%. On LongBench-v2 Multi-Doc QA, DeLM achieves the highest average accuracy across four frontier model families, improving over the strongest baseline by up to 5.7 percentage points. The code is available on our project website at https://yuzhenmao.github.io/DeLM/.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有集中式多智能体系统在协调机制上的瓶颈问题。研究背景是，多智能体系统（MAS）通过将复杂问题分解为并行子任务来扩展大语言模型的测试时推理能力。然而，现有方法如Claude Code Subagents、Kimi Agent Swarm等大多依赖集中式编排，即由一个主智能体分配任务、收集输出并合并结果。这种方式的不足在于：第一，随着子任务数量增长，主智能体成为通信和集成的串行瓶颈，有用发现、失败或部分解决方案都必须返回主智能体再广播，导致进度共享效率低下；第二，主智能体在路由过程中可能稀释、遗漏或扭曲细节，造成重要进展丢失；第三，在长上下文推理中，主智能体需预先分配证据簇，若子智能体上下文不足则需要额外轮次交互，使协调更加缓慢。本文提出的DeLM框架旨在通过去中心化协调解决这些问题，其核心思想是让智能体通过共享已验证的上下文状态进行异步交互，而非依赖中央控制器进行同步分发-收集，从而将有用的中间进展直接积累为可复用的问题状态，避免主智能体的瓶颈效应。

### Q2: 有哪些相关研究？

本文的相关研究可分为以下几类：

1. **集中式多智能体系统（MAS）**：现有主流工作如AutoGen、ChatDev、MetaGPT等依赖中央控制器分配子任务并整合结果。本文的DeLM通过去中心化架构回避了这一瓶颈，允许智能体通过共享上下文直接协作。

2. **分散式协作框架**：类似SWARM、CrewAI等工作探索了非集中式智能体协调，但多需要显式通信协议或共享内存。DeLM的创新在于将共享已验证上下文作为唯一通信基板，结合任务队列实现异步更新，无需路由所有信息通过控制器。

3. **测试时扩展推理**：OpenAI的o1、DeepSeek-R1等关注单模型扩展，而DeLM通过并行智能体实现多模型协作扩展，在SWE-bench和LongBench上取得更优成本效益。

4. **软件工程与长文本评测**：与SWE-bench相关工具（如Agentless）和LongBench评测方案相比，DeLM不仅提升性能（多子任务并行度），还通过上下文验证机制降低通信开销，成本降低约50%。

核心区别在于：DeLM的上下文验证和异步读取-写入机制，使智能体能根据积累的已验证进展自主调整子任务，无需全局协调，这在实用性与扩展性上超越了传统集中式或简单分散式方案。

### Q3: 论文如何解决这个问题？

DeLM通过去中心化架构解决集中式MAS的通信与集成瓶颈。核心设计包含两个全局结构：共享上下文(s_ctx)和任务队列(t_que)，定义了智能体间的协调接口。整体框架分为五个阶段：1) 初始化阶段，将输入任务分解为初始子任务放入任务队列；2) 并行执行阶段，多个智能体异步从队列中认领子任务，并读取共享上下文中的已验证进展；3) 压缩验证阶段，智能体完成本地推理后，将结果压缩为紧凑gist（而非原始轨迹），并使用LLM验证器确保gist忠实反映关键发现、失败假设或约束，仅通过验证的gist被写入共享上下文；4) 动态任务生成阶段，当队列为空时，最近完成的智能体检查当前共享上下文是否足够，若不足则生成新子任务入队；5) 最终答案生成阶段，当不再需要子任务时从共享上下文中产出最终答案。

关键技术包括：分级压缩机制，对长源单元采用"原始内容→引用摘要→紧凑gist"的层次化路径（类似操作系统的分页存储），通过选择性展开机制按需检索细粒度证据；异步执行策略让智能体无需等待中央调度即可基于已验证进展进一步推理。创新点在于将共享上下文作为去中心化的通信基质，通过gist层实现轻量级全局状态视图，同时保留底层细节的按需访问能力，显著降低通信开销。

### Q4: 论文做了哪些实验？

论文在 SWE-bench Verified 和 LongBench-v2 两个基准上进行了实验。SWE-bench Verified 评估软件工程任务中的测试时扩展，通过运行每项任务 X 次（X=2,4）并报告 Avg.@1、Pass@2 和 Pass@4 指标。对比方法包括 Base、mini-SWE-agent、Claude Code、AOrchestra（集中式多智能体系统）及其并行变体 AOrchestra-Parallel。主要结果：在 Gemini 3 Flash 上，DeLM 的 Avg.@1 达 65.7%（超过最强基线 AOrchestra-Parallel 9.3 个百分点），Pass@2 为 72.9%，Pass@4 为 77.4%，同时每任务成本降至 $0.12（约降低 50%）。在 Claude Opus 4.6 上，DeLM 同样在三个指标上取得最佳性能（Avg.@1 78.0%、Pass@2 80.7%、Pass@4 82.5%）。LongBench-v2 多文档 QA 实验涵盖金融、政府、法律等 5 个领域共 125 个样本，对比方法包括 Base、ReadAgent、AOrchestra 等。DeLM 在 GPT-5.4、Claude Sonnet 4.6 等四个前沿模型家族上均取得最高平均准确率，较最强基线提升高达 5.7 个百分点。实验证实了通过共享上下文实现去中心化协调的有效性。

### Q5: 有什么可以进一步探索的点？

论文提出的DeLM框架在去中心化协调上取得了显著成效，但仍存在若干可探索的改进方向。首先，当前共享上下文作为通信基板虽避免了中心化瓶颈，但所有代理均需读取完整进度，当任务复杂度剧增时，上下文长度可能成为新瓶颈。未来可探索分层或摘要式上下文更新机制，仅传递关键变化而非常量全量数据。其次，代理间的协作完全基于任务队列的竞争式领取，缺乏优先级或依赖关系建模，在涉及子任务因果约束的复杂推理中可能效率低下。可引入动态任务依赖图或激励机制优化领取策略。此外，对于验证机制，论文未详细讨论错误传播的鲁棒性，若某代理的局部输出被误验证为正确，可能误导后续代理。探索自适应验证阈值或冗余投票策略能提升系统容错性。最后，将DeLM扩展到多模态或跨语言场景时，共享上下文的结构化表示需要重新设计，例如引入异构嵌入对齐层，以支持不同模态信息的有效融合。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为DeLM的去中心化多智能体系统框架，旨在解决传统集中式多智能体系统中的通信和集成瓶颈问题。在集中式系统中，主智能体负责分配子任务、收集输出并合并结果，随着子任务数量增长，这一控制器成为瓶颈。DeLM通过并行智能体、共享验证上下文和任务队列实现去中心化协调：智能体异步认领子任务，读取共享上下文中的累积进展，执行局部推理，并写回紧凑的已验证更新。共享上下文作为通用通信基质，使智能体能够基于彼此已验证的进展进行构建，无需通过中央控制器路由更新。实验表明，在SWE-bench Verified软件工程基准测试中，DeLM在Pass@4上达到77.4%的准确率，比最强基线高出10.5个百分点，同时将每任务成本降低约50%；在LongBench-v2多文档问答中，DeLM在四个前沿模型系列中取得最高平均准确率，比最强基线提升5.7个百分点。该框架有效解决了测试时扩展和长上下文推理中的协调问题，展示了去中心化协调在智能体系统中的显著优势。
