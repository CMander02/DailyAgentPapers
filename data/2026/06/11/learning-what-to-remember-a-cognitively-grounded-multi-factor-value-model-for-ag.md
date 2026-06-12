---
title: "Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory"
authors:
  - "Zhibao Chen"
  - "Qian Cheng"
date: "2026-06-11"
arxiv_id: "2606.12945"
arxiv_url: "https://arxiv.org/abs/2606.12945"
pdf_url: "https://arxiv.org/pdf/2606.12945v1"
categories:
  - "cs.AI"
tags:
  - "Agent记忆"
  - "记忆管理"
  - "多因子价值模型"
  - "认知启发"
  - "遗忘决策"
  - "LongMemEval"
  - "可解释性"
relevance_score: 9.5
---

# Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory

## 原始摘要

Long-running LLM agents accumulate interaction histories far larger than any context window, forcing a standing decision: what to encode deeply, what to forget, and what to retrieve under a fixed memory budget. Production systems answer with semantic similarity or recency -- both mis-specified for the forgetting decision, which is made at consolidation time before the future query is known. We propose a multi-factor memory value function V(m)=\sum_i w_i f_i(m) over seven interpretable factors (emotional intensity, goal relevance, value alignment, self/user relevance, task utility, reliability, and usage history) drawn from cognitive psychology, whose weights are learned from a downstream objective by a gradient-free optimiser, and whose single scalar uniformly controls encoding depth, forget risk, and retrieval rank. We make a methodological point: on LongMemEval, scoring goal relevance against the held-out evaluation question saturates gold-evidence retention at \approx 0.98 -- this measures retrieval, not forgetting. In the realistic blind regime, a learned multi-factor value retains 0.770 \pm 0.011 of gold evidence across 479 usable cases, versus 0.657 for uniform weights, 0.518 for the best single factor, and 0.368 for recency; every paired gap's 95% bootstrap CI is above zero, and a neural network over the same factors ties the linear model. The learned weights are interpretable -- reliability, emotional intensity, and self/user relevance dominate, while query-time goal similarity is correctly down-weighted for the forgetting decision. A controlled synthetic task with planted confounds confirms the learner recovers a separating weighting (1.00 retention) where uniform weighting fails (0.62). The substrate is open-source; all experiments run on a single CPU with no API calls.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长时间运行的LLM智能体在面对远超上下文窗口的历史交互记录时，如何进行有效记忆管理的问题。现有方法主要依赖两种单因素策略：一是基于语义相似度的检索增强系统，仅在查询时定义相似性；二是基于时间戳的滑动窗口方案，优先保留近期内容。这两种策略均存在根本缺陷：相似性无法在记忆整合（遗忘决策）时使用，因为未来查询未知；而时效性则倾向于保留近期无价值闲聊，却丢弃了老旧但重要的信息。核心矛盾在于，遗忘决策（编码什么、忘记什么）必须在未来查询出现之前做出，因此需要一种对记忆未来有用性的前瞻性评估。本文从认知心理学中汲取灵感，提出一个多因素记忆价值模型，通过七个可解释因子（如情绪强度、目标相关性、可靠性等）的加权组合来统一控制编码深度、遗忘风险和检索排序，并利用无梯度优化器从下游任务目标中学习权重，从而替代人工调参。其核心要解决的是：在无法预知未来查询的现实“盲”场景下，如何基于当前可用信息，学习一个最优的多因素价值函数，以最大化固定记忆预算下黄金证据的保留率，从而超越单因素策略的局限。

### Q2: 有哪些相关研究？

相关研究可分为四类：

**1. 智能体记忆系统**：MemGPT采用分页虚拟内存，基于最近性驱逐；Generative Agents提出多因素检索评分（融合近因、重要性、相关性），但重要性由LLM临时打分且权重固定，仅控制检索；MemoryBank引入艾宾浩斯遗忘曲线，但动态机制固定；MemOS将记忆视为操作系统资源，但未学习价值信号。本文差异在于学习多因素权重，且同一标量同时控制编码、遗忘和检索。

**2. 认知心理学中的价值保留**：价值导向记忆、加工层次理论、自我参照效应、情绪唤起调节巩固、理性遗忘分析等揭示了人类记忆保留的多因素决定。本文创新在于将多因素视角操作化为人工智能体的单个可学习标量，而非建模人类数据。

**3. 学习记忆策略**：强化学习框架用于拟合记忆策略。由于编码-遗忘-检索-回答流程不可微，本文使用无梯度黑盒优化器（而非反向传播）学习7个可解释权重，区别于端到端不透明的学习控制器。

**4. 记忆评估**：LongMemEval包含500个长对话查询问题。本文提出的方法论贡献在于：将查询相关性与检索保留混淆进行区分，并强调遗忘策略必须在盲注（未知未来查询）条件下评估。

### Q3: 论文如何解决这个问题？

论文通过提出一个基于认知心理学的多因素记忆价值模型来解决长期运行LLM代理在有限记忆预算下的遗忘和检索问题。核心方法是将每个记忆片段编码为一个7维可解释因素向量，通过线性加权得到单一标量值V(m)=∑w_i f_i(m)，该标量统一控制编码深度、遗忘风险和检索排序。

整体框架包括三个模块：1) 因素提取模块，从认知心理学中选取七个因素（情感强度、目标相关性、价值对齐、自我/用户相关性、任务效用、可靠性和使用历史），每个因素都有独立可计算的语义定义；2) 价值评估模块，通过可学习权重线性组合各因素，其中权重使用梯度无关的随机爬山算法优化，以适应不可微的下游目标；3) 三元记忆操作模块，编码深度根据归一化价值划分为四个层级，遗忘分数结合时间衰减、使用频率和价值抵抗，检索排序直接使用V(m)值。

关键技术创新包括：线性价值函数的设计选择，既匹配七维参数空间的容量需求，又保证可审计性；证明了多因素加权显著优于单一因素（如仅目标相关性）和近期性基线；在盲评估设置下，学习到的权重揭示可靠性、情感强度和自我/用户相关性占主导地位，而查询时目标相似度被适当降权。该方法在LongMemEval数据集上达到0.770±0.011的金证据保留率，且所有实验只需单CPU运行，无需API调用。

### Q4: 论文做了哪些实验？

论文主要进行了两组实验。首先是在合成数据集上验证梯度自由优化器能否恢复有用的权重：60个训练集和60个测试集，每个案例包含4个金标准项和16个干扰项。金标准项具有高目标相关性、任务效用和可靠性，而干扰项则混有高价值对齐、自我相关性和情绪噪声。结果显示，学习到的多因素价值函数保留了100%的金标准项，而均匀权重仅保留62%，纯情绪、纯自我和纯新近度策略完全失败（0%）。学习得到的最重要权重是可靠性（1.36）和任务效用（0.88），而价值对齐干扰因素被降至0.09。

其次是在真实基准测试LongMemEval-S上进行盲评估：使用479个有效案例（每个约500轮对话），保留前30%的记忆，评估金标准证据的保留率。在盲区（仅使用会话主题而非未来问题）中，学习到的多因素价值函数保留率为0.770±0.011，显著优于均匀权重（0.657）、最佳单因素（自我相关性0.518）、可靠性（0.497）、新近度（0.368）和目标相关性（0.286）。所有成对差异的95%自助法置信区间均高于零。学习到的盲模型权重表明可靠性（0.64）、情绪强度（0.55）和自我/用户相关性（0.23）占主导，而目标相关性被驱动至零。此外，用MLP替代线性模型效果相当（0.773 vs 0.770），证明线性模型已足够；不同保留比例下的优势在0.1-0.4的激进预算下持续存在。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要集中在五个方面：1）仅以证据保留率而非下游任务准确率为指标，未验证记忆策略对最终回答质量的影响；2）三个因子（价值对齐、任务效用、历史使用频率）因依赖外部API而处于惰性状态，实际仅使用四个因子；3）仅在单一基准（LongMemEval-S）和模态（多轮对话）上评估，缺乏工具使用、编程等场景验证；4）盲目标锚点（session用户轮次质心）并非最优，其他任务描述或目标堆栈可能携带更强信号；5）线性价值函数可能无法捕捉因子间的相互作用（如情感仅对自我相关项重要）。

未来可探索方向：引入神经网络或核方法建模因子交互，在API可用场景下激活所有七因子并验证任务效用因子的实际贡献；拓展到工具使用、代码生成等不同记忆模式的工作负载，学习特定于任务的可解释权重；改进盲目标锚点设计（如显式任务描述或动态目标跟踪）；最终将记忆保留率与下游任务准确率关联，验证价值函数对端到端性能的影响。

### Q6: 总结一下论文的主要内容

该论文针对长期运行的 LLM 智能体在固定记忆预算下，面对远超上下文窗口的交互历史，需要做出“该记住什么、遗忘什么、检索什么”的核心决策问题。目前主流系统依赖语义相似性或时间近因作为单一遗忘标准，但这些在遗忘决定时（即未来查询未知时）存在根本性缺陷。论文提出一个受认知心理学启发的多因素记忆价值函数 V(m)=Σ w_i f_i(m)，涵盖情感强度、目标相关性、价值对齐、自我/用户相关性等七个可解释因素，并通过无梯度优化器从下游任务目标（如证据保留率）中学习权重。该单一标量值统一控制编码深度、遗忘风险和检索排名。主要结论表明，在真实的盲遗忘场景下，学习到的多因素价值在 LongMemEval 的 479 个案例中保留了 0.770±0.011 的黄金证据，显著优于均匀权重（0.657）、最佳单因素（0.518）和时间近因（0.368）。研究还发现，可学习的权重具有可解释性，且该优势在考虑未来查询的理想化指标下会被掩盖，揭示了评估遗忘的必要方法区分。该工作为智能体记忆管理提供了认知驱动、学习导向的实用新范式。
