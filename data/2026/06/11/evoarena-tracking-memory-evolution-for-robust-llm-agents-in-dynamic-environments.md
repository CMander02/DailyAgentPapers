---
title: "EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments"
authors:
  - "Jundong Xu"
  - "Qingchuan Li"
  - "Jiaying Wu"
  - "Yihuai Lan"
  - "Shuyue Stella Li"
  - "Huichi Zhou"
  - "Bowen Jiang"
  - "Lei Wang"
  - "Jun Wang"
  - "Anh Tuan Luu"
  - "Caiming Xiong"
  - "Hae Won Park"
  - "Bryan Hooi"
  - "Zhiyuan Hu"
date: "2026-06-11"
arxiv_id: "2606.13681"
arxiv_url: "https://arxiv.org/abs/2606.13681"
pdf_url: "https://arxiv.org/pdf/2606.13681v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "评测基准"
  - "动态环境"
  - "记忆机制"
  - "智能体评估"
relevance_score: 8.5
---

# EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments

## 原始摘要

Large language model (LLM) agents have achieved strong performance on a wide range of benchmarks, yet most evaluations assume static environments. In contrast, real-world deployment is inherently dynamic, requiring agents to continually align their knowledge, skills, and behavior with changing environments and updated task conditions. To address this gap, we introduce EvoArena, a benchmark suite that models environment changes as sequences of progressive updates across terminal, software, and social domains. We further propose EvoMem, a patch-based memory paradigm that records memory evolution as structured update histories, enabling agents to reason about environmental evolution through changes in their memory. Experiments show that current agents struggle on EvoArena, achieving an average accuracy of 39.6% across evolving terminal, software, and social-preference domains. EvoMem consistently improves performance, yielding an average gain of 1.5% on EvoArena and also improving standard benchmarks such as GAIA and LoCoMo by 6.1% and 4.8%. Beyond individual tasks, EvoMem further improves chain-level accuracy by 3.7% on EvoArena, where success requires completing a consecutive sequence of related evolutionary subtasks. Mechanistic analysis shows that EvoMem improves evidence capture in the memory, indicating better preservation of complete evolving environment states. Our results highlight the importance of modeling evolution in both evaluation and memory for reliable agent deployment.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前LLM智能体在动态演化环境中部署时面临的重大挑战。当前研究大多假设静态环境，因此大多数基准测试只评估智能体在单一快照下的表现。然而，现实世界的应用场景（如终端工作流、软件仓库和个性化助手）是持续演化的：接口规则、代码状态、用户偏好等会随时间版本更新。现有方法即便引入了一些动态性（如刷新任务、异步事件），也未能系统性地测试“同一环境背景下的持续演化”，即一个环境界面、规则、任务目标发生变化后，智能体需要知道哪些更新是重要的，哪些旧知识仍适用，并做出相应调整。这种静态评估的局限性导致了“状态坍塌”这一主要失败模式：大多数记忆系统只维护一个“最新状态”的快照，当新信息过时或回滚时，系统会丢失原本有效的旧知识及相关上下文。为此，本文提出了两个核心贡献：EvoArena（一个包含终端、软件和社交三大领域渐进演化的基准套件）以及EvoMem（一种基于补丁的记忆范式）。EvoMem通过记录每次更新的前后状态、更新原因和证据，让智能体能对环境的演化历史进行显式推理，从而在动态环境中保持鲁棒性，解决的根本问题是评估并提升智能体在真实、持续演化的环境中的适应能力。

### Q2: 有哪些相关研究？

相关研究可分为评测类与方法类两类。评测方面，现有基准如WebArena、SWE-bench、GAIA、AgentBench等均假设静态环境，而最新动态基准如SWE-bench-Live、GAIA2和HorizonBench虽引入了任务刷新、异步事件或偏好变化，但通常仅支持单次更新而非多版本链条，且缺乏持久环境演化、隐式变化检测和链条评估能力。EvoArena填补了这一空白，通过将终端、软件工程和社交偏好领域静态基准转化为持续演化的版本链，评测智能体在保持旧版本有效行为的同时适应新变化的能力。方法方面，自进化智能体（如Reflexion、Voyager）聚焦于智能体侧能力提升，而非环境变化；记忆系统如结构化长期记忆、生产级持久记忆等虽能持续更新知识，但往往朝最新状态聚合，导致历史状态被覆盖。EvoMem的补丁式记忆范式创新性地将记忆更新视为证据，明确记录“什么变了、为何变、支持行为的环境版本”，从而既能适应环境演化，又保留完整版本历史，与上述方法形成互补。

### Q3: 论文如何解决这个问题？

EvoArena提出一个三维度演化基准来系统评估LLM Agent在动态环境中的能力，覆盖终端工作流演化、软件代码演化和用户偏好演化。终端演化中，将任务定义为有序的版本链，每个版本保持相同目标但改变指令、环境、文件、依赖、接口或测试规则，并通过继承机制确保later版本保留early版本的环境状态。软件演化则基于真实Git仓库，按时间顺序提取连续的commit范围并分组为里程碑，每个里程碑是一个局部、可测试的开发目标，评估时采用oracle状态推进（即应用参考补丁而非Agent预测补丁）以避免错误累积。偏好演化通过长对话模拟用户偏好的渐进式转变。EvoMem是本文提出的补丁式记忆范式，核心包括两个组件：补丁记录和补丁增强检索。补丁记录监测基础记忆系统从M_{t-1}到M_t的转变，只对非增量的更新（即修改、覆盖或重解读既有记忆的更新）生成补丁，每条补丁包含时间戳、变更前后内容、变更理由、语义摘要和支持证据，存储为追加式补丁历史。补丁增强检索在标准记忆检索基础上，额外从补丁历史中检索与查询相关的top-k补丁，提供版本化的历史证据，最终将最新记忆内容和相关补丁拼接作为推理上下文。这种设计使Agent既能从最新记忆行动，又能保留先前状态和版本感知推理能力，在EvoArena上平均提升1.5%的准确率，在GAIA和LoCoMo标准基准上也分别提升6.1%和4.8%。

### Q4: 论文做了哪些实验？

论文在EvoArena基准上系统评估了LLM代理在动态环境中的适应性。实验设置包括三个演化领域：可执行工作流演化（Terminal-Bench-Evo）、软件演化（SWE-Chain-Evo）和偏好演化（PersonaMem-Evo）。数据集方面，Terminal-Bench-Evo包含89个初始任务，构建了352个演化版本实例；SWE-Chain-Evo包含12个代码仓库的50条演化链，共493个链步实例和145个独特里程碑。对比方法包括基线代理及EvoMem方法。主要结果：当前代理在EvoArena上平均准确率仅39.6%，表现挣扎。EvoMem方法持续提升性能，在EvoArena上平均提升1.5%，在标准基准测试GAIA和LoCoMo上分别提升6.1%和4.8%。链级准确率方面，EvoMem在EvoArena上提升3.7%。机制分析显示，EvoMem通过改进记忆中的证据捕获，更好地保留了完整的演化环境状态，从而提升了代理在动态环境中的鲁棒性。

### Q5: 有什么可以进一步探索的点？

可以进一步探索EvoArena的以下几个方向：首先，当前环境变化设计尚基于人工预设规则，未来可引入更真实的动态性，如用户行为演化或突发系统故障，使评测更具挑战性。其次，EvoMem虽提升了证据捕获，但补丁式记忆可能引发冗余或遗忘关键早期信息，可探索基于重要性权重的动态记忆压缩或检索增强机制。第三，当前工作聚焦于单智能体记忆，多智能体协作场景下的集体环境演化推理值得研究，例如如何共享或对齐各智能体的演化记忆。最后，可引入主动探索策略，让智能体主动查询环境变化细节而非被动接收更新，以缓解上下文窗口限制带来的记忆失效问题。这些改进将推动LLM智能体在完全动态、开放世界中的鲁棒部署。

### Q6: 总结一下论文的主要内容

LLM代理在静态基准测试中表现良好，但实际部署环境是持续演变的。EvoArena是一个评估代理在动态环境中鲁棒性的基准套件，包含终端、软件和社交三个领域的渐进式演变任务。实验表明，现有代理在EvoArena上平均准确率仅39.6%，主要失败模式是“状态坍缩”——记忆系统只保留最新状态而丢失历史信息。为此提出EvoMem，一种基于补丁的记忆范式，它像Git一样记录记忆的更新历史（包括更新前后的状态、理由和证据），使代理能追溯和分析环境演变。EvoMem在EvoArena上平均提升1.5%的性能，在GAIA和LoCoMo等标准基准上分别提升6.1%和4.8%，并将EvoArena的链式任务准确率提升3.7%。机理分析表明，EvoMem通过更好地保留完整的环境演变证据来提升推理能力。这项工作的核心贡献是揭示了环境演变评估的重要性，并提出了版本感知记忆机制，为实现可靠的代理部署提供了新方向。
