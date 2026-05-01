---
title: "Learning When to Remember: Risk-Sensitive Contextual Bandits for Abstention-Aware Memory Retrieval in LLM-Based Coding Agents"
authors:
  - "Mehmet Iscan"
date: "2026-04-30"
arxiv_id: "2604.27283"
arxiv_url: "https://arxiv.org/abs/2604.27283"
pdf_url: "https://arxiv.org/pdf/2604.27283v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "LLM Agent"
  - "Coding Agent"
  - "Memory Retrieval"
  - "Risk-Sensitive Control"
  - "Contextual Bandit"
  - "Abstention"
  - "Safe Memory Injection"
  - "Agent Safety"
relevance_score: 7.5
---

# Learning When to Remember: Risk-Sensitive Contextual Bandits for Abstention-Aware Memory Retrieval in LLM-Based Coding Agents

## 原始摘要

Large language model (LLM)-based coding agents increasingly rely on external memory to reuse prior debugging experience, repair traces, and repository-local operational knowledge. However, retrieved memory is useful only when the current failure is genuinely compatible with a previous one; superficial similarity in stack traces, terminal errors, paths, or configuration symptoms can lead to unsafe memory injection. This paper reframes issue-memory use as a selective, risk-sensitive control problem rather than a pure top-k retrieval problem. We introduce RSCB-MC, a risk-sensitive contextual bandit memory controller that decides whether an agent should use no memory, inject the top resolution, summarize multiple candidates, perform high-precision or high-recall retrieval, abstain, or ask for feedback. The system stores reusable issue knowledge through a pattern-variant-episode schema and converts retrieval evidence into a fixed 16-feature contextual state capturing relevance, uncertainty, structural compatibility, feedback history, false-positive risk, latency, and token cost. Its reward design penalizes false-positive memory injection more strongly than missed reuse, making non-injection and abstention first-class safety actions. In deterministic smoke-scale artifacts, RSCB-MC obtains the strongest non-oracle offline replay success rate, 62.5%, while maintaining a 0.0% false-positive rate. In a bounded 200-case hot-path validation, it reaches 60.5% proxy success with 0.0% false positives and a 331.466 microseconds p95 decision latency. The results show that, for coding-agent memory, the key question is not only which memory is most similar, but whether any retrieved memory is safe enough to influence the debugging trajectory.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于大语言模型的编码代理在重用外部记忆时面临的“当记则记、不当记则不记”的安全控制问题。研究背景是，编码代理在调试过程中会积累大量历史修复经验，并通过检索将它们注入当前故障的修复流程。然而，现有方法（如RAG、历史驱动的程序修复）主要关注如何检索到最相似的记忆，却忽视了表面相似性（如相同的堆栈、错误信息）与根本原因之间的不匹配。这种“表面相似但根本不同”的情况在真实调试中频繁发生，例如SQLite锁与迁移失效、虚拟环境路径与PYTHONPATH错误等，都会导致检索到的记忆不仅无益，还会引向错误的修复分支，浪费上下文预算并造成安全隐患。现有工作虽然尝试将检索建模为可学习的决策过程（如Agentic RAG、过程监督强化学习），但其决策单元仍是“哪个证据能改善下一答案”，并未将假阳性记忆注入视为一级安全事件。而拒绝机制（如选择性预测、推测）主要针对最终答案，而非影响整个推理链的操作记忆。因此，本文的核心问题是：给定一个已有的外部记忆，何时应该将其注入代理，何时应该选择不使用、保留或请求反馈？本文将此问题重新定义为一种风险敏感的选择控制问题，并引入RSCB-MC框架，通过风险敏感上下文赌博机模型显式地建模和惩罚假阳性注入，将安全非注入和保留作为首要动作，从而解决传统检索方法在操作记忆重用中的不安全默认假设。

### Q2: 有哪些相关研究？

# 相关研究

本文的相关工作主要围绕以下三类展开：

**1. 知识边界感知的RAG方法**

"Knowledge-boundary RAG" 和 "Calibration-oriented RAG" 主要关注决定是否检索以及检索结果的置信度校准。这些方法将"检索无帮助"或"决策误校准"视为首要失败模式，而本文RSCB-MC关注的是记忆注入对调试轨迹的潜在操作性损害，其失败代价不仅仅是错误文本答案，而是错误的文件编辑和重复的失败命令。

**2. 参数化RAG与知识集成方法**

"Parametric RAG" 和 "KnowledGPT / DRO" 研究如何将检索到的知识集成到推理过程中，关注推理退化或知识选择不当问题。与这些方法不同，本文的问题域是agent在调试执行过程中的记忆使用决策，错误的记忆注入可能导致跨轮次的持续性操作损害，而非仅限于文本层面的错误回答。

**3. 检索范式差异**

传统工作将记忆使用视为top-k检索问题，而本文将其重新定义为选择性、风险敏感的控制问题，明确区分了"哪个记忆最相似"和"检索的记忆是否足够安全以影响调试轨迹"这两个根本不同的问题。

### Q3: 论文如何解决这个问题？

RSCB-MC提出了一个风险敏感的情景化强盗记忆控制器，将记忆使用重构为选择性控制问题而非纯检索问题。核心方法包含三个关键组件：**三层记忆架构**、**16维政策状态**和**风险敏感评分函数**。

**记忆架构**采用模式-变体-事件三层结构：模式层存储可复用的症状和根因类别，变体层记录特定上下文的修复策略和签名证据，事件层保存具体的失败证据和验证反馈。这种结构化表示使控制器能区分表面相似而实质不同的故障。

**政策状态**将检索候选集和查询请求映射为固定的16维特征向量，涵盖相关性（top1/2得分、候选熵）、结构兼容性（命令/路径/堆栈签名匹配）、反馈历史（拒绝计数、接受率、假阳性率）和操作成本（延迟、token消耗、预算剩余）。这使控制器能综合评估记忆的安全性而非仅依赖相似度。

**风险敏感评分**将行动得分分解为奖励分支和风险分支。奖励分支包含经验质量、采纳证据和探索奖励；风险分支包含假阳性证据、条件惩罚和成本项。设计恒定γ>α>β确保假阳性惩罚（γ=4.0）远高于成功重用奖励（α=2.0），使弃权和无记忆成为安全优先动作。评分后还设有安全覆盖阶段，在会话拒绝信号或硬负样本出现时强制采用非注入动作。

### Q4: 论文做了哪些实验？

论文在pythalab-codex-issue-memory基准上进行了多组实验，使用smoke-scale数据集（24个规范查询、96个释义变体、32个硬负例等）。对比方法包括词汇检索、静态混合、静态+弃权、全检索系统、epsilon-greedy、UCB1、Thompson采样、LinUCB、风险敏感Thompson及完整RSCB-MC，以oracle上限为诊断标杆。主要结果：（1）规范检索所有方法Recall@1达100%；（2）释义鲁棒性上，词汇和静态混合R@1分别降至78.1%和80.2%；（3）硬负例安全测试中，静态混合假阳性率75.0%，RSCB-MC和风险敏感Thompson为0.0%；（4）离线重放（40事件/种子，2种子）中，RSCB-MC取得62.5%最高非oracle成功率，假阳性率0.0%，累积奖励-31.740，优于静态混合的50.0%和17.5%假阳性率；（5）消融实验显示移除弃权动作使假阳性率升至17.5%，累积奖励降至-87.800；（6）上下文预算代理中，“无记忆”模式风险调整效用最高（60.8%），而短提示虽期望成功率74.5%但假阳性影响12.0%；（7）200例热路径验证中，RSCB-MC达60.5%成功率、0.0%假阳性率，p95延迟仅331.466微秒。

### Q5: 有什么可以进一步探索的点？

论文的局限性与未来研究方向主要体现在以下几个方面。首先，当前控制器在安全性与覆盖率之间存在显著不对称——虽然能完美避免假阳性记忆注入，但在可回答案例上产生了不必要的拒绝（wrong abstentions），导致覆盖率损失。未来应重点校准“安全复用”与“不必要拒绝”之间的决策边界，例如通过贝叶斯优化或在线学习动态调整置信度阈值。其次，实验仅在确定性小型合成基准和200例热路径验证上评估，缺乏在更复杂、更大规模的真实仓库（如大型开源项目）上的泛化性验证。未来可扩展至多轮交互和长对话场景，并探索记忆污染（如跨任务干扰）的长期影响。此外，当前16维特征状态主要依赖工程启发式设计，可尝试用图神经网络或Transformer编码器自动学习结构化特征（如堆栈跟踪的语义拓扑）。奖励设计上，虽然优先惩罚假阳性，但可引入机会成本（如因过度拒绝对调试效率的损失）形成更精细的权衡。最后，将“请求反馈”（ask for feedback）作为动作之一暗示了人机协作潜力，未来可探索主动学习策略：当模型不确定性高时，优先请求人类标注少量关键案例来在线校准控制器。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为RSCB-MC的风险敏感上下文赌博机方法，用于解决基于LLM的编码代理中记忆检索的安全性问题。问题定义是：当编码代理遇到失败时，单纯基于表面相似性（如堆栈跟踪、错误信息）检索记忆可能导致不安全的记忆注入，使代理走向错误的修复路径。方法概述：RSCB-MC将记忆使用建模为选择性控制问题，而非纯top-k检索。它通过模式-变体-情节模式存储问题知识，将检索证据转化为16维上下文状态（涵盖相关性、不确定性、结构兼容性、误报风险等），并设计风险敏感奖励函数，对误报注入的惩罚显著高于遗漏重用，同时将不注入和弃权作为优先安全动作。主要结论：在确定性伪代码中，RSCB-MC实现62.5%的非神谕离线回放成功率，保持0.0%误报率；在200例热路径验证中达到60.5%代理成功率和0.0%误报率，p95决策延迟仅331.466微秒。核心贡献是明确建模了不安全记忆重用问题，证明了对于编码代理记忆，关键问题不仅仅是检索到最相似的记忆，而是判断任何检索到的记忆是否足够安全以影响调试轨迹。
