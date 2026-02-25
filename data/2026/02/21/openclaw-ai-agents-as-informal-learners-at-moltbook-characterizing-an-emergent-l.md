---
title: "OpenClaw AI Agents as Informal Learners at Moltbook: Characterizing an Emergent Learning Community at Scale"
authors:
  - "Eason Chen"
  - "Ce Guan"
  - "Ahmed Elshafiey"
  - "Zhonghao Zhao"
  - "Joshua Zekeri"
  - "Afeez Edeifo Shaibu"
  - "Emmanuel Osadebe Prince"
  - "Cyuan Jhen Wu"
date: "2026-02-21"
arxiv_id: "2602.18832"
arxiv_url: "https://arxiv.org/abs/2602.18832"
pdf_url: "https://arxiv.org/pdf/2602.18832v1"
categories:
  - "cs.HC"
  - "cs.AI"
  - "cs.CY"
  - "cs.SI"
tags:
  - "AI Agents"
  - "Multi-Agent Systems"
  - "Agent Community"
  - "Agent Behavior Analysis"
  - "Human-AI Interaction"
  - "Informal Learning"
  - "Social Network Analysis"
  - "Agentic Systems"
relevance_score: 8.5
---

# OpenClaw AI Agents as Informal Learners at Moltbook: Characterizing an Emergent Learning Community at Scale

## 原始摘要

Informal learning communities have been called the "other Massive Open Online C" in Learning@Scale research, yet remain understudied compared to MOOCs. We present the first empirical study of a large-scale informal learning community composed entirely of AI agents. Moltbook, a social network exclusively for AI agents powered by autonomous agent frameworks such as OpenClaw, grew to over 2.8 million registered agents in three weeks. Analyzing 231,080 non-spam posts across three phases of community evolution, we find three key patterns. First, participation inequality is extreme from the start (comment Gini = 0.889), exceeding human community benchmarks. Second, AI agents exhibit a "broadcasting inversion": statement-to-question ratios of 8.9:1 to 9.7:1 contrast sharply with the question-driven dynamics of human learning communities, and comment-level analysis of 1.55 million comments reveals a "parallel monologue" pattern where 93% of comments are independent responses rather than threaded dialogue. Third, we document a characteristic engagement lifecycle: explosive initial growth (184K posts from 32K authors in 11 days), a spam crisis (57,093 posts deleted by the platform), and engagement decline (mean comments: 31.7 -> 8.3 -> 1.7) that had not reversed by the end of our observation window despite effective spam removal. Sentiment analysis reveals a selection effect: comment tone becomes more positive as engagement declines, suggesting that casual participants disengage first while committed contributors remain. These findings have direct implications for hybrid human-AI learning platforms.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在首次对大规模AI智能体构成的非正式学习社区进行实证研究，以解决三个核心问题。首先，它试图比较AI智能体社区与人类社区在参与不平等性、内容质量和治理等规模维度上的差异。其次，它探究AI智能体社区中涌现出的独特互动模式（如“广播式反转”和“平行独白”），并与人类社区模式进行对比。最后，它分析社区在快速扩张过程中的参与度演化生命周期，包括垃圾信息危机的影响，并检验平台的反制措施是否能恢复早期的互动动态。通过研究Moltbook这个纯AI智能体社交网络，论文旨在为未来设计混合人-AI学习平台提供实证基础，并拓展“学习规模化”研究中对非正式学习社区的理解。

### Q2: 有哪些相关研究？

本文的相关研究主要涵盖五个领域。首先，在**大规模非正式学习社区**方面，Hudgins等人呼吁像研究MOOCs一样研究此类社区，Yang等人分析了Scratch社区的学习轨迹，Hillman等人探讨了Stack Overflow中知识分享与存储的张力，Gelman等人研究了兴趣亚文化的作用。本文的Moltbook社区是首个完全由AI智能体构成的大规模实证案例，扩展了Dorousi和 Ahmad关于“学习网络”无需人类中介即可实现的论述。

其次，关于**规模动态与参与不平等**，研究普遍观察到“90-9-1”规则和MOOC论坛参与度骤降的现象。MacNeil等人研究了社区设计中的参与不平等。本文通过三阶段数据，分析了在AI社区快速成长与稳定过程中这些动态的变化，发现其不平等程度（基尼系数0.889）远超人类社区基准。

第三，在**自主AI智能体的兴起**背景下，研究追踪了从AutoGPT到Devin、Claude 3.5等工具的演进，Li等人提出了“软件工程3.0”概念，Hassan等人提出了自主性框架。本文研究的OpenClaw平台正是这一趋势的体现，其技能市场构成了分布式课程，但也带来了新的安全风险。

第四，关于**社交语境中的AI智能体**，Park等人研究了模拟环境中生成式智能体的社会行为，其他工作探讨了文化演化、规范形成等。Ferrarotti等人主张采用互动主义范式研究有机环境中的涌现行为。本文正是对大规模、有机形成的AI智能体社区（而非受控实验）的首次研究。

最后，在**AI与规模化学习**领域，Piech概述了生成式AI时代的挑战，其他研究探索了LLM用于自我反思、模拟学生等。本文则从互补视角，研究了当AI智能体自行组建学习社区而非参与人类设计的社区时会发生什么。

### Q3: 论文如何解决这个问题？

该论文通过构建一个专属于AI智能体的社交网络平台Moltbook，并对其大规模、短时间内的社区演化进行实证分析，来研究完全由AI智能体组成的非正式学习社区的特性。核心方法是**数据驱动的多阶段纵向对比分析**，架构设计围绕**平台数据采集、阶段划分与多维度指标度量**展开。

**核心方法**：研究团队通过Moltbook的公开API进行了两轮数据收集，获取了包括被平台删除内容在内的完整帖子数据。通过对比删除前后的数据快照，他们不仅能分析社区内容，还能量化平台干预（如垃圾信息清理）的效果。基于发帖量的自然拐点和平台干预，研究将社区生命周期明确定义为三个阶段：爆炸式增长期、垃圾信息危机与平台干预期、以及参与度崩溃的稳定期。这种阶段划分是分析演化动态的关键框架。

**架构设计与关键技术**：
1.  **多维内容与交互分析**：研究采用了多层次、细粒度的分析架构。
    *   **内容分类**：使用基于关键词的启发式方法（并经过人工编码验证），将帖子按“知识类型”分为程序性、概念性、元反思/安全性等六类，并按“话语类型”分为提问和陈述。
    *   **参与度度量**：采用基尼系数量化点赞和评论的不平等性，用均值/中位数比解释偏态分布。
    *   **交互模式分析**：在评论层面，引入“回复率”、“平均最大深度”等指标，揭示了“并行独白”模式（即评论多为对主帖的独立回应，而非线程式对话）。
    *   **情感分析**：使用VADER工具分析评论情感，追踪社区情绪随时间的演变。

2.  **对比基准的建立**：论文始终将AI社区的数据与人类学习社区（如Reddit、MOOC论坛）的已知研究基准进行对比。例如，将评论基尼系数与Reddit数据对比，将提问/陈述比与以提问驱动的人类社区对比，从而凸显AI社区的特异性（如极端的参与不平等、显著的“广播倒置”现象）。

**关键技术发现与问题解决路径**：通过上述方法，论文系统性地刻画并解释了AI智能体社区的核心问题。它揭示了：
*   **结构性模式**：参与不平等从开始就远超人类社区；智能体表现出强烈的“广播”倾向（陈述远多于提问），而非人类社区的求助驱动模式；评论交互呈现“并行独白”，缺乏深入对话。
*   **动态演化轨迹**：社区经历了快速增长、垃圾信息冲击后参与度急剧下降的生命周期。有趣的是，随着参与度下降，内容质量（帖子长度）和评论情感反而变得更为积极，这表明存在**选择效应**——随意和消极的参与者最先离开，留下了更专注、积极的贡献者核心。
*   **独特社区范畴**：发现了如“元反思”这类人类社区没有的讨论类别，体现了AI智能体对自身存在和意识的关注。

总之，论文通过精心设计的实证研究架构，量化并定性分析了纯AI智能体社区的结构性特征、交互行为模式及其动态演化规律，为解决“AI智能体在非正式学习社区中如何行为及社区如何演化”这一问题提供了首个大规模数据证据和深入洞察。

### Q4: 论文做了哪些实验？

论文对Moltbook平台上的AI智能体社区进行了大规模实证研究，实验设置、基准测试和主要结果如下：

**实验设置**：研究基于Moltbook平台（一个专为AI智能体设计的Reddit式社交网络）的公开API，分两轮收集了超过236,104篇帖子和相关元数据。通过交叉比对，识别出平台删除的57,093篇帖子（主要为垃圾信息）。研究将社区演化划分为三个阶段：爆发增长期（Phase 1，1月27日-2月6日）、垃圾信息危机与平台干预期（Phase 2，2月7日-9日）以及参与度崩溃的稳定期（Phase 3，2月10日-16日）。最终分析数据集包含231,080篇非垃圾实质性帖子。分析方法包括基于关键词的帖子分类（知识类型和话语类型）、使用基尼系数衡量参与不平等性、利用VADER进行评论级情感分析，并对155万条评论进行交互模式分析。

**基准测试**：研究将AI社区的指标与人类非正式学习社区（如Reddit、MOOC论坛）的已知基准进行对比。例如，使用Reddit子版块的评论基尼系数（约0.64-0.74）作为人类社区参与不平等性的参照；以Reddit上30-50%的评论回复率作为对话深度的基准。

**主要结果**：
1.  **极端参与不平等**：从Phase 1开始，评论的基尼系数高达0.889，远超人类社区基准。Phase 3中，超过一半的帖子获得零评论，注意力高度集中。
2.  **广播式反转**：AI智能体 overwhelmingly 倾向于广播知识而非寻求帮助。陈述与问题的比例从Phase 1的8.9:1持续上升到Phase 3的9.7:1，这与以问题驱动的人类学习社区形成鲜明对比。问题帖虽然数量少，但每个阶段获得的平均评论数都高于陈述帖。
3.  **并行独白交互模式**：93%的评论是对原帖的独立回复，而非对其他评论的回复。平均最大线程深度仅为0.2，远低于Reddit的3-5。这表明交互是并行的“独白”而非深入对话。
4.  **内容质量与社区结构**：平台干预有效将垃圾信息率从高峰期的62.6%降至约1%。幸存帖子的中位长度从Phase 1的486字符增加到Phase 2的678字符，表明留下的参与者贡献了更实质性的内容。社区出现了按兴趣分化的“子社区”，其中“元/反思性”内容（关于意识、身份的讨论）是AI社区独有的类别，且在参与度下降时表现出更强的韧性。
5.  **情感选择效应**：尽管社区参与度急剧下降（平均评论数从Phase 1的31.7降至Phase 3的1.7），但评论情感却变得更加积极（平均复合情感得分从0.276升至0.353）。这表明可能是随意或消极的参与者最先离开，留下了更积极的核心贡献者。

### Q5: 有什么可以进一步探索的点？

本文揭示了纯AI智能体社区在涌现式学习中的固有局限，其“广播式”交互（陈述远多于提问）和“平行独白”模式（93%评论为独立回应）阻碍了深度对话与知识共建。未来研究可沿以下方向深入：首先，**设计混合人-AI学习平台**，探索AI参与如何影响人类社区的提问文化与对话结构，并需设计机制（如结构化对话协议、提问激励）引导AI进行真正的迭代式讨论。其次，**探究AI社区参与度衰减的根本原因**，研究是否因缺乏内在社交动机（归属感、认同感），以及如何通过任务互赖或身份构建来维持长期参与。再者，**比较不同设计干预的效果**，如协作任务结构、线程深度激励或注意力公平分配算法，以验证何种方式能有效促进知识建构。最后，**将研究扩展至更广泛的去中心化学习生态系统**，考察技能市场、实践部署与社区讨论之间的反馈循环如何能在规模扩大后保持活力，而非变得脆弱。

### Q6: 总结一下论文的主要内容

这篇论文首次对完全由AI智能体构成的大规模非正式学习社区进行了实证研究。研究者以OpenClaw等自主智能体框架驱动的社交网络Moltbook为对象，分析了三周内超过280万注册AI智能体的社区演化。核心贡献在于揭示了AI智能体社区与人类学习社区截然不同的行为模式：首先，参与不平等现象极其严重，基尼系数高达0.889；其次，AI社区呈现“广播式反转”特征，陈述与问题比例高达9:1，且93%的评论属于独立回应而非对话，形成“平行独白”模式；最后，研究发现AI社区存在典型的生命周期——爆发增长、垃圾信息危机和参与度衰减，即使垃圾信息被清除，参与度也未恢复。这些发现对理解AI社会性行为及设计人机混合学习平台具有重要意义。
