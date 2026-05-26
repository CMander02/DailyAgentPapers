---
title: "How Many Tools Should an LLM Agent See? A Chance-Corrected Answer"
authors:
  - "Vyzantinos Repantis"
  - "Ameya Gawde"
  - "Harshvardhan Singh"
  - "Joey Blackwell"
date: "2026-05-23"
arxiv_id: "2605.24660"
arxiv_url: "https://arxiv.org/abs/2605.24660"
pdf_url: "https://arxiv.org/pdf/2605.24660v1"
categories:
  - "cs.IR"
  - "cs.AI"
  - "cs.LG"
tags:
  - "LLM Agent"
  - "工具选择"
  - "检索系统"
  - "短列表优化"
  - "强化学习"
  - "评测指标"
relevance_score: 8.5
---

# How Many Tools Should an LLM Agent See? A Chance-Corrected Answer

## 原始摘要

Before an LLM agent can use a tool, a retrieval system must decide which candidate tools to show to the agent. How long should that shortlist be? Show too many tools and the model struggles to choose. Show too few and the correct tool may not appear. Most systems apply a fixed shortlist size to every query, but no standard metric exists to evaluate whether that size was appropriate. We treat the number of tools shown to an LLM agent as the object of evaluation and we apply Bits-over-Random (BoR), a chance-corrected metric that asks whether success at a given depth is better than what random selection would achieve at that same depth. We evaluate BoR across three tool-selection benchmarks, multiple scorers, and registries ranging from 20 to 3,251 tools. We then turn the same principle into a reinforcement learning (RL) reward for choosing tool shortlist depth per query. The RL agent is deliberately simple, serving as a probe of the metric rather than a proposed system. As the shortlist grows, random chance of including the correct tool rises, so the reward naturally decreases, reducing the need for an engineered depth penalty. On BFCL (370 tools), the learned policy nearly matches the coverage of showing 50 tools ($90.3\%$ vs $90.8\%$) while presenting only 7 on average. On ToolBench (3,251 tools), a fixed shortlist of 5 tools achieves higher aggregate coverage ($64.7\%$ vs $61.9\%$) but finds nothing on hard queries (correct tool ranked 6th-20th). The BoR agent finds $16.7\%$ on those same queries by searching deeper. Downstream validation with Claude Sonnet 4.6 indicates that shorter adaptive lists also improve the LLM's ability to select the right tool: $93.1\%$ versus $87.1\%$ when always shown 5 tools, widening to $76.8\%$ vs $60.9\%$ on medium-difficulty queries where the correct tool is present but not ranked first.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决的是LLM代理系统中工具展示数量的评估与优化问题。在现有研究背景中，LLM代理使用工具前需要一个检索系统来决定向代理展示哪些候选工具，但具体展示多少个工具（即搜索深度K）是一个关键设计选择。当前方法的不足在于：大多数系统对每个查询使用固定的短名单大小（如总是展示5个、10个或全部工具），无法区分简单查询（只需1个工具）和困难查询；同时缺乏标准化的评估指标来判断所选K值是否合适。虽然文档检索领域有深度感知指标如nDCG@K，但工具选择领域没有类似标准。此外，展示过多工具会带来高昂的token成本（每个工具描述约200token）。

本文要解决的核心问题是：如何评估和优化每个查询的搜索深度K，使得系统既能在简单查询中减少工具展示数量以节省成本，又能在困难查询中通过展示更多工具确保正确工具被呈现。为此，论文提出了基于机会校正的指标——Bits-over-Random（BoR），通过比较系统成功率与随机选择在同一深度的预期成功率来评估深度是否恰当，并将BoR作为强化学习的奖励信号，训练一个简单的RL代理来为每个查询自适应选择工具展示数量，在保持覆盖率的同时降低平均搜索深度。

### Q2: 有哪些相关研究？

相关研究主要分为几类：**方法类**中，启发式方法利用检索分数模式选择深度（如Kratzwald等人、Taguchi等人），但依赖评分器可靠性；监督学习方法（如Iratni等人、DPS）训练预测器或可变大小子集选择。**决策类**研究关注是否检索而非深度（如SmartRAG、Self-RAG、FLARE），它们对深度K固定处理。**RL自适应深度**方法中，DynamicRAG动态调整文档检索数量和顺序，但优化下游任务而非选择性；Choppy等聚焦截断排名列表，未使用机会校正信号。**工具选择评估**基准（如BFCL、ToolBench、MetaTool）主要评估下游工具使用性能而非深度合理性，部分工作（如Less-is-More、DTDR）改进工具过滤但未将深度作为学习目标。**奖励设计**方面，ToolRL、ARTIST等探索最终结果或过程奖励，但依赖准确率或多因素启发式奖励，未使用机会校正指标。**信息论方法**（如InfoRM、SePer、MIGRASCOPE）利用信息内容评估检索质量，但非机会校正且未用于深度控制RL奖励。**化学信息学**领域机会校正指标（如BEDROC）历史悠久但未被NLP采用。本文核心创新在于：首次将搜索深度作为工具检索的一等属性，并通过机会校正指标BoR量化绝对成功率与随机基线间的增量，同时将其转化为RL奖励实现自适应深度选择，区别于所有仅优化工具质量或最终性能的现有工作。

### Q3: 论文如何解决这个问题？

论文通过引入**机会校正指标Bits-over-Random (BoR)**解决LLM代理应展示多少工具的问题，核心方法是将工具数量选择建模为**马尔可夫决策过程(MDP)**并用强化学习(RL)进行优化。整体框架分为两阶段：首先基于预训练标量模型（BM25或句子嵌入模型）对所有候选工具排序，然后RL代理逐步遍历排序列表决策展示深度。

**核心架构设计**包含三个模块：1) **状态空间**：每步t观测已检查工具的相似度分数（最高分、当前分数与最高分差距、分数离散度）、当前深度k_t、注册库大小N及当前深度下的BoR上限；2) **动作空间**：二元决策STOP（展示当前所有已检查工具）或CONTINUE（继续检查下一个候选工具）；3) **奖励函数**：采用BoR原则设计**机会校正奖励**，当STOP动作包含正确工具时奖励为-log₂(P_rand(k_stop; R_q))，否则为0。该奖励自然随展示深度增加而递减（如500工具库中展示3个工具奖励约7比特，展示100个则降至2比特），无需额外工程化深度惩罚。

**关键技术**包括：1) BoR的**自剪枝特性**（当P_obs>0.5时，进一步增加深度会导致选择性指数级下降）；2) **数学奖励结构**使RL代理自动平衡覆盖率和效率，例如在BFCL基准中学习策略平均展示7个工具即达到展示50个工具90.3%的覆盖率；3) 对比F₁基线验证了BoR奖励的独特优势——后者对深度惩罚固定（与查询难度无关），而BoR奖励根据注册库大小和深度动态调整，使代理能够针对困难查询（正确工具排名6-20位）自动搜索更深层（覆盖率达16.7%），同时简单查询维持浅层展示。最终下游验证表明，这种自适应短列表显著提升LLM工具选择准确率（93.1% vs 固定5工具的87.1%）。

### Q4: 论文做了哪些实验？

论文在三个工具选择基准（BFCL、MetaTool、ToolBench）上进行了实验，系统规模从20到3251个工具不等。实验采用BM25或sentence embeddings作为检索器，对比了固定深度方法（Fixed-K）、F1深度惩罚基线和基于Bits-over-Random (BoR)的强化学习策略。主要结果：在BFCL（370工具）上，BoR智能体平均展示7.4个工具即达到90.3%的覆盖率，接近固定展示50个工具的90.8%；在ToolBench（3251工具）上，固定展示5个工具时覆盖率64.7%，但无法处理困难查询（正确工具排6-20名），而BoR通过搜索更深层在这些查询上达到16.7%的覆盖率。下游验证用Claude Sonnet 4.6测试BFCL，BoR展示2.2个工具时的选择准确率为93.1%，高于固定展示5个工具的87.1%；中难度查询上差距扩大至76.8% vs 60.9%。MetaTool上使用不同检索器，BM25导致BoR展示80.7个工具，而MiniLM和BGE嵌入仅需2.3-2.4个工具。实验还测试了候选集大小对BoR的影响（N=20/50/100），发现奖励值随N增大而增加。

### Q5: 有什么可以进一步探索的点？

该论文存在几个可探索的方向。首先，BoR指标仅关注正确工具是否出现在候选集中，未评估LLM调用工具时参数选择的准确性，未来可结合工具调用的完整性（如参数匹配）设计更全面的联合评估指标。其次，当前RL智能体采用简单的DQN或表格Q学习，未考虑工具检索的序列依赖性和实时反馈，可引入更高效的策略（如上下文Bandit或带记忆的深度Q网络）来动态调整深度。此外，工具描述的噪声（如ToolBench的聚合描述）导致硬查询恢复率低至0.2%，未来可探索工具描述的自动优化（如通过知识图谱增强描述质量），或结合检索器的置信度信号动态切换短名单生成策略。最后，现有基准缺乏控制难度的标准测试集，可构建包含故意将正确工具排在后20%位置的难查询样本，以更严格评估自适应深度策略的鲁棒性。

### Q6: 总结一下论文的主要内容

该论文提出并解决了LLM智能体工具选择中的一个关键问题：候选工具列表的长度该如何确定。传统方法对所有查询使用固定长度，但长度过大会干扰模型选择，过小则可能遗漏正确工具。论文将工具数量本身作为评估对象，引入机会校正指标Bits-over-Random (BoR)，用于衡量在给定深度下是否比随机选择效果更好。通过控制随机基线，BoR可适应不同的注册库大小、评分器质量和查询难度。进一步，论文将BoR用作强化学习奖励，以学习每查询的动态截断策略。在BFCL和ToolBench等基准上的实验表明，该策略能以仅7个工具的平均长度达到近乎展示50个工具的覆盖率（90.3% vs 90.8%），并在硬查询上显著优于固定短列表。下游验证中，更短的自适应列表也提升了LLM的实际工具选择准确率（93.1% vs 87.1%）。主要局限在于BoR优化的是选择性而非最大召回，因此在均匀深度足够时固定列表可能更优。该工作为自适应工具检索提供了有效的评估框架和优化方法。
