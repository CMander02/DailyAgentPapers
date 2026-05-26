---
title: "Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-horizon Agents"
authors:
  - "Yeonjun In"
  - "Wonjoong Kim"
  - "Sangwu Park"
  - "Kanghoon Yoon"
  - "Chanyoung Park"
date: "2026-05-25"
arxiv_id: "2605.25535"
arxiv_url: "https://arxiv.org/abs/2605.25535"
pdf_url: "https://arxiv.org/pdf/2605.25535v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent记忆系统"
  - "个性化记忆策略"
  - "长期记忆基准"
  - "会话级存储门控"
  - "多域长期交互"
relevance_score: 9.5
---

# Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-horizon Agents

## 原始摘要

Existing large language model (LLM) based memory systems apply universal, static policies that overlook a fundamental reality: the contexts that are worth storing in memory are different across users. This misalignment wastes limited memory budget on transient interactions while failing to preserve critical context for long horizon tasks. To address this gap, we investigate an underexplored question: can LLM based memory systems learn personalized memory policies? We introduce PerMemBench, the first benchmark for evaluating personalized memory systems, featuring multi year, multi domain interaction histories across diverse user personas. We further present the first empirical study of memory personalization, proposing session level storage gating, a lightweight framework that selectively bypasses memory operations for transient sessions. Our study confirms that personalization yields substantial retention gains under perfect gating, yet reveals that accurate gating remains an open and critical challenge.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要探讨了基于大语言模型（LLM）的记忆系统中存在的个性化缺失问题。在现有研究中，记忆系统通常采用“一刀切”的通用静态策略，即对所有用户应用相同的标准来判断哪些上下文信息值得存储。然而，这种做法忽视了不同用户在长期和短期任务使用模式上存在根本性差异这一现实。例如，对于某些用户而言，“食谱建议”可能是一项需要长期追踪的持续性任务，而对其他用户则仅是临时性咨询。这种通用策略导致记忆预算被浪费在临时性交互上，同时却无法为关键的长期任务保留必要上下文，造成了资源错配。为了填补这一研究空白，本文提出了一个核心问题：LLM记忆系统能否学习个性化的记忆策略？为此，论文构建了首个针对个性化记忆评估的基准数据集PerMemBench，该数据集包含来自不同用户角色的多年多领域交互历史。通过分析，本文首次对记忆个性化进行了实证研究，并提出了“会话级存储门控”这一轻量级框架，旨在通过识别会话的长期或临时性质，选择性跳过对临时会话的记忆操作。研究发现，理想的门控能显著提升记忆留存率，但精确的门控决策仍然是一个开放且严峻的挑战。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涵盖两个方向。第一个方向是**基于LLM的智能体记忆系统**。现有工作主要关注如何通过学习记忆策略来选择性提取和存储交互中的信息，例如通过聚类、图或树结构来建模记忆单元以提高检索准确性。本文与这些工作的核心区别在于，它批评了现有方法采用统一、静态的策略，忽略了用户间“值得存储”的信息存在根本差异。为此，本文提出了会话级存储门控（session-level storage gating）这一新范式，学习为每个用户识别其“有价值的会话”，并有选择地跳过那些短暂交互的记忆操作。第二个方向是**智能体记忆系统的评测**。现有基准如LoCoMo和HalluMem等主要专注于单一领域的日常对话，并假设用户表现出同质性。本文指出这些评测忽略了多领域交互历史和用户行为异质性（如使用模式差异）。为此，本文提出了PerMemBench基准，它包含跨多年、多领域的交互历史，并显式建模了多样化的用户角色和异质行为，从而提供了更真实、更具挑战性的评测环境。因此，本文在研究方法上强调了个性化，在评测上加入了多领域和行为异质性，弥补了现有工作的关键空白。

### Q3: 论文如何解决这个问题？

论文通过提出一个轻量级的“会话级存储门控”框架来解决现有记忆系统缺乏个性化的问题。核心思想是：在每次对话会话结束后，由一个门控模块判断该会话是否属于长期任务，若不是则直接跳过其存储操作，从而将有限的记忆预算集中在真正需要长期积累的场合。

整体框架是一个无需修改底层记忆系统的外挂式模块，主要包括三个主要组件：
1. **贪婪门控**：仅基于当前会话的对话内容，由LLM预测该会话是长期还是瞬时的。方法简单但缺乏历史信号。
2. **上下文感知门控**：在贪婪方法基础上，为每个会话生成一段摘要，并通过滑动窗口将最近K个摘要作为判断当前会话的上下文，从而利用序列模式。
3. **结构感知门控**：显式建模会话间的结构化关系。它维护一个“结构笔记”，该笔记定期更新，包含“项目”和“孤立会话”列表。项目结构会跨时间窗口传递，允许系统回溯性地重新分配会话（例如将之前孤立的会话归属到后续发现的项目中）。这是唯一接近领域级用户模式推断的方法。

创新点在于：
- 首次提出并系统研究了LLM记忆系统的个性化问题，揭示了“统一静态策略”与“用户间存储需求差异”的根本性错配。
- 提出了会话级存储门控这一通用且轻量的个性化框架，能够无缝集成到现有系统中。
- 通过实验发现，结构感知门控在稳态下表现良好（F1达0.844），但在用户使用模式切换时因过度依赖已有项目结构而失效，而贪婪方法虽整体准确率低但在切换时更稳健，这为未来结合两者优势的鲁棒门控设计指明了方向。

### Q4: 论文做了哪些实验？

论文围绕个性化记忆系统进行了多组实验。实验设置包括两个数据集：PerMemBench^s（静态，20位用户，26-78会话，跨度15-20个月）和PerMemBench^d（动态，62-148会话，跨度25-32个月），并采用Memory Retention Rate（RR）作为主要评估指标，衡量参考记忆单元在所需生命周期内持续保留在记忆库中的一致性。

实验比较了三种记忆系统（Mem0、Memory-R1、RMM）在不同存储门控方法下的表现：Universal（无门控）、Oracle（完美门控）、Greedy（仅基于当前会话）、Context-aware（基于滑动窗口的历史摘要）和Structure-aware（建模会话间关系结构）。主要结果包括：

1. **门控分类性能**：Structure-aware方法在PerMemBench^s上使用Qwen3-14B达到最高F1值0.844（FNR 0.115，FPR 0.280），在gpt-5-mini上达0.795（FNR 0.018，FPR 0.652）。但它难以检测用户行为模式转变（如长期→短期任务切换）。
2. **记忆保留率**：Oracle门控相比Universal在所有系统上显著提升RR，尤其在较小记忆预算（100或200条目）下增益最大；预算500时仍有意义增益。
3. **当前门控的局限性**：Greedy和Context-aware门控的RR低于Universal，Structure-aware仅带来边际改进，与Oracle之间存在较大差距，表明现有门控方法远未实现个性化潜力。

### Q5: 有什么可以进一步探索的点？

论文的局限性与未来探索方向主要包括：第一，基准规模仅涵盖20个用户，虽然自动化构建管道可扩展，但仍需在更多样化的用户群体中验证。第二，用户使用画像建模较为简单，仅考虑领域参与度和记忆必要性两个维度，未来应引入更细粒度的行为模式，如用户偏好变化规律。第三，个性化策略仅针对存储环节，缺乏对已存储记忆的纠错机制，未来可设计个性化的删除策略以动态清理无用的记忆。第四，会话级门控的准确性仍不理想，这是当前最关键的技术挑战。我认为可以从两方面改进：一是采用强化学习或在线模仿学习，让门控模块通过与环境的交互持续优化；二是将记忆存储与检索建模为端到端的可控策略，利用用户反馈信号进行后训练，从而真正实现“因人而异”的记忆管理闭环。

### Q6: 总结一下论文的主要内容

现有基于大语言模型的记忆系统采用统一的静态策略，忽略了不同用户“值得存储”的上下文存在根本差异，导致在有限记忆预算下浪费资源。为弥补这一不足，论文首次提出个性化记忆评估基准PerMemBench，包含多用户、多年份、多领域的交互历史。在此基础上，论文开展了首个关于记忆个性化的实证研究，提出了会话级存储门控框架，通过识别并跳过短时会话的记忆操作来优化存储。研究表明，在完美门控下个性化能显著提升记忆保持率，尤其在记忆预算紧张时效果更明显。但当前门控方法的准确性仍不成熟，实现精确的门控是未来亟待解决的关键挑战。
