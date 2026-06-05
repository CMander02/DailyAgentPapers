---
title: "EMBER: Efficient Memory via Budgeted Evidence Retention for Long-Horizon Agents"
authors:
  - "Yilong Li"
  - "Suman Banerjee"
  - "Tong Che"
date: "2026-06-04"
arxiv_id: "2606.05894"
arxiv_url: "https://arxiv.org/abs/2606.05894"
pdf_url: "https://arxiv.org/pdf/2606.05894v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent Memory"
  - "Long-Horizon Agent"
  - "Evidence Retention"
  - "Memory Management"
  - "Agent Architecture"
relevance_score: 8.5
---

# EMBER: Efficient Memory via Budgeted Evidence Retention for Long-Horizon Agents

## 原始摘要

Long-horizon agents can archive large histories, but future answers still incur retrieval, rereading, and context costs. When retained memory misses answer-relevant evidence, the system must return to larger portions of the raw history. We study budgeted evidence survival: before the query is known, which source evidence should be retained so that it remains recoverable and usable under a fixed retained source-evidence token budget? We instantiate this setting as Budgeted Pre-Query Retention, where memory is written during ingestion and later read without access to the full raw stream. We introduce EMBER, a learned retention policy that constructs a compact, source-backed evidence state. EMBER stores evidence capsules: verbatim source excerpts paired with retrieval keys and update metadata, preserving both grounding and read-time access. Post-query outcome feedback trains the writer to preserve evidence across the ingestion-retrieval-answer chain. On LongMemEval-RR, our LongMemEval-derived retained-evidence protocol, EMBER-14B reaches 0.3017 F1 at the 8192-token retained-evidence comparison point, compared with 0.1765 for the strongest non-EMBER budgeted baseline. Across retained source-evidence budgets, EMBER improves F1, Retain-Recall, and Read-Recall, indicating that long-horizon memory depends on retaining evidence within the budget rather than rereading larger histories.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决长程智能体在长期交互中的预算化证据留存问题。研究背景是，长程智能体虽能存档大量历史数据，但未来回答仍需承担检索、重读和上下文成本。现有方法的不足体现在三个方面：首先，原始日志RAG虽保留全量数据，但阅读时需消耗大量计算资源；其次，查询可见的智能体（如MemAgent）需在看到目标查询后才决定记忆写入，这在未来查询未知时无法应用；最后，持久化智能体在数据摄入时就必须决定保留哪些证据，而未来查询是未知的，且完整原始流在查询时无法保持可用。本文要解决的核心问题是：在查询未知时，如何在固定的保留证据token预算（B_ret）下，选择并留存那些对将来问题回答可恢复且可用的源证据。为此，论文形式化了预算化证据留存问题，提出了预算化预查询留存协议，并引入EMBER方法，通过学习在摄入时写入紧凑的、基于源证据的证据胶囊，并利用回答时结果反馈训练写入策略，从而在有限的预算内最大化证据的存活率和可用性。

### Q2: 有哪些相关研究？

相关工作可分为三类：（1）**智能体记忆与学习型记忆操作**：最相关的是 MemAgent 和 Memory-R1，它们将记忆写入视为可学习的操作。但本文聚焦于查询未知时的源证据留存问题，而非直接对记忆条目进行改写或更新。（2）**RAG与分层记忆系统**：TierMem 可通过摘要逐级路由并回退完整日志，而 EMBER 假设完整日志在查询时不可用，因此必须在摄入阶段决策哪些证据进入有限预算的记忆，这是关键区别。（3）**查询预测与上下文压缩**：文档扩展、自提问等方法通过预测查询或效用信号改进检索；抽取式摘要虽有长度预算约束，但优化目标通常是文档覆盖或已知查询相关性。EMBER 不仅存储源摘录，还附加检索键和更新元数据，使留存证据在查询时仍可恢复且保持可读性，从而在固定预算下提升 F1、Retain-Recall 和 Read-Recall 指标。

### Q3: 论文如何解决这个问题？

EMBER通过一个预算化的证据留存策略来解决长时程代理中的记忆效率问题。其核心思想是在预查询阶段，在固定的留存证据token预算下，智能地决定保留哪些原始证据片段。

整体框架分为写入和读取两个阶段。在写入阶段，系统采用了一个**可学习的留存策略**。主要组件包括：
1. **可回答性探针**：在摄入数据流时，每个数据块会通过一个探针判断其未来是否可能对解答问题有用。探针不仅基于主题相关性，还识别具体需要的事实、关系、日期或更新。
2. **证据胶囊**：对于判断为有用的数据块，系统将其组织成“证据胶囊”。每个胶囊包含：
   - 与源数据完全一致的**真实原文摘录**（source-backed excerpt），确保答案的可追溯性。
   - **检索键**，包括实体、日期、表面/意图关键词，使胶囊在未来能被高效查询。
   - **更新元数据**，指定插入、合并、覆盖或跳过等更新模式。
3. **预算层**：一个确定性会计模块，根据预算约束对所有提议的证据胶囊进行接纳、合并或拒绝，确保最终留存集合的Token数不超过预算。

在读取阶段，系统仅从留存集合中检索证据。读者先生成简短查询，从中筛选出Top-k的候选胶囊，然后由选择器选择最终用于回答的证据。

关键创新点在于**答案门控的证据链训练目标**。训练时，系统在随机采样的预算下模拟完整的“留存-读取-回答”流程。奖励函数将最终的答案质量与留存覆盖率、检索排名、选择纯度等辅助指标相乘，形成门控信号。只有那些确实有助于最终答案的证据留存决策才会获得正向奖励，同时系统还会对超出预算的行为进行惩罚。这使得写入策略学会了在严格的预算约束下，优先保留对下游任务最关键、最有可能被需要的证据，从而在固定预算下显著提升了F1、留存召回率和读取召回率。

### Q4: 论文做了哪些实验？

论文在三个基准上进行了实验。**实验设置**：微调Qwen2.5-7B/14B作为记忆策略骨干，分三阶段训练（RULER-HotpotQA→MuSiQue/2WikiMultiHopQA→硬例），预算从{512,1024,2048,4096,8192} tokens中采样，查询在写入时隐藏。**数据集/基准**：1) **LongMemEval-RR**（主要评估，固定预算预查询保留协议）；2) **RULER-HotpotQA**（受控多跳QA压力测试）；3) **MultiQ-LongMemEval-RR**（多查询覆盖测试）。**对比方法**包括全日志系统、查询可见记忆体（MemAgent、Memory-R1）和预算化基线（Recency、Reservoir、Dense MMR、Hybrid salience、TierMem-BudgetRaw）。**主要结果**：在LongMemEval-RR的8192 token预算点上，EMBER-14B F1达**0.3017**，较最佳非EMBER基线（0.1765）提升+0.125；在512 token紧预算下，EMBER-7B达**0.2413** F1，超过非EMBER基线的8192 token结果。在RULER-HotpotQA的28K token点上，EMBER-14B达**0.8412** F1，优于最强Vanilla RAG（0.7772）。在MultiQ测试中，EMBER-14B以10%预算达**0.2767** F1，远高于最强启发式基线（0.0824）。消融实验显示，移除答案探针、检索键或结果RL均导致F1显著下降，验证了各组件的关键作用。

### Q5: 有什么可以进一步探索的点？

首先，论文的评估主要基于受控的LongMemEval-RR基准，未在真实部署的助手系统中验证。未来可探索在用户特定历史、偏好漂移、隐私约束和记忆漂移等动态环境下，EMBER的泛化能力和鲁棒性。其次，当前的保留策略通过查询后结果反馈进行训练，但未考虑多跳推理或需要跨多个证据片段组合的证据场景。一个改进方向是引入因果或反事实学习，使保留机制能捕捉证据间的依存关系。第三，论文仅使用了7B和14B的模型，更大的模型可能带来更好的策略，但也可能引入更高的计算成本。可探索利用知识蒸馏或模型压缩，在保持效果的同时降低推理开销。最后，当前的“证据胶囊”设计主要依赖检索-阅读链，并未主动缓解隐私风险。未来可结合差分隐私或可解释性手段，确保保留的证据既是可审计的，又能尊重用户对敏感信息的删除意图。

### Q6: 总结一下论文的主要内容

这篇论文研究了长周期智能体的记忆管理问题，即如何在有限的证据预算下，在未知未来查询前保留最关键的源证据。作者将问题形式化为"预算化预查询保留"：在数据摄入阶段将记忆写入紧凑的证据胶囊（包含原文摘录、检索键和更新元数据），在查询时仅基于该胶囊进行检索和回答，无法访问完整历史。核心贡献是提出EMBER系统，通过学习型保留策略构建源证据支持的紧凑记忆状态，并通过查询后的结果反馈训练写入器，优化从摄入到检索再到回答的整个链路。在基于LongMemEval构建的LongMemEval-RR协议上，EMBER-14B在8192令牌的保留证据比较点上达到0.3017的F1分数，远超最强非EMBER基线（0.1765）。主要结论是：长周期记忆的关键不在于重读更大历史，而在于在预算内有效保留证据。该工作使记忆质量可审计，可直接检查保留状态携带或丢失了哪些源证据。
