---
title: "From Industry Claims to Empirical Reality: An Empirical Study of Code Review Agents in Pull Requests"
authors:
  - "Kowshik Chowdhury"
  - "Dipayan Banik"
  - "K M Ferdous"
  - "Shazibul Islam Shamim"
date: "2026-04-03"
arxiv_id: "2604.03196"
arxiv_url: "https://arxiv.org/abs/2604.03196"
pdf_url: "https://arxiv.org/pdf/2604.03196v1"
categories:
  - "cs.SE"
tags:
  - "Code Agent"
  - "Code Review"
  - "Empirical Study"
  - "Pull Request"
  - "Human-Agent Collaboration"
  - "Software Engineering"
relevance_score: 7.5
---

# From Industry Claims to Empirical Reality: An Empirical Study of Code Review Agents in Pull Requests

## 原始摘要

Autonomous coding agents are generating code at an unprecedented scale, with OpenAI Codex alone creating over 400,000 pull requests (PRs) in two months. As agentic PR volumes increase, code review agents (CRAs) have become routine gatekeepers in development workflows. Industry reports claim that CRAs can manage 80% of PRs in open source repositories without human involvement. As a result, understanding the effectiveness of CRA reviews is crucial for maintaining developmental workflows and preventing wasted effort on abandoned pull requests. However, empirical evidence on how CRA feedback quality affects PR outcomes remains limited. The goal of this paper is to help researchers and practitioners understand when and how CRAs influence PR merge success by empirically analyzing reviewer composition and the signal quality of CRA-generated comments. From AIDev's 19,450 PRs, we analyze 3,109 unique PRs in the commented review state, comparing human-only versus CRA-only reviews. We examine 98 closed CRA-only PRs to assess whether low signal-to-noise ratios contribute to abandonment. CRA-only PRs achieve a 45.20% merge rate, 23.17 percentage points lower than human-only PRs (68.37%), with significantly higher abandonment. Our signal-to-noise analysis reveals that 60.2% of closed CRA-only PRs fall into the 0-30% signal range, and 12 of 13 CRAs exhibit average signal ratios below 60%, indicating substantial noise in automated review feedback. These findings suggest that CRAs without human oversight often generate low-signal feedback associated with higher abandonment. For practitioners, our results indicate that CRAs should augment rather than replace human reviewers and that human involvement remains critical for effective and actionable code review.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决业界对代码审查代理（CRAs）效能的乐观宣称与实证证据不足之间的差距问题。研究背景是，随着OpenAI Codex等自主编码代理在短时间内生成海量拉取请求（PRs），CRAs已成为开发工作流程中常规的“守门员”。行业报告（如Qodo 2025）声称，CRAs能在无需人工干预的情况下处理开源仓库中80%的PRs，并提升开发效率和质量。

然而，现有实证研究揭示了CRAs的局限性：其采用受信任问题和缺乏项目特定上下文的制约；大规模分析发现，人工评论的被采纳率（60%）远高于CRA评论（0.9%至19.2%），表明自动反馈中存在大量噪声。同时，CRAs常审查来自同一提供者的代码，可能引发闭环偏差。噪声评论可能导致PRs更高的废弃率，进而产生技术债务。但此前研究尚未系统量化CRA评论的信噪比，或将其与PR结果（如合并成功率）直接关联。

因此，本文的核心问题是：在没有人工参与的情况下，CRAs是否能有效审查PRs？其生成的噪声反馈是否与PR废弃相关？具体而言，论文通过实证分析审查者构成和CRA生成评论的信号质量，探究CRAs何时以及如何影响PR合并成功，重点关注两个研究问题：比较人工审查与CRA审查的PR合并率差异，以及低信噪比如何导致CRA审查的PR合并率降低。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：代码代理在PR中的行为研究、代码审查代理（CRA）的应用与评估研究，以及审查上下文与交互研究。

在代码代理行为研究方面，已有工作如Watanabe等关注代理PR在重构、文档等维护任务中的应用，Horikawa等分析代理的重构操作，Twist研究其依赖管理行为。这些研究侧重于代理作为代码提交者的行为，而非其作为审查者的影响。

在CRA应用与评估方面，Wessel等发现CRA能减少人工工作但可能引入噪音；Ramesh等和Vijayvergiya等研究了LLM辅助工具在工业界的采纳与开发者观感；Lin等通过CodeReviewQA指出LLM在理解审查意图上存在局限。这些工作多聚焦工具采用、开发者感知或模型能力，而非审查反馈质量对PR结果的实际影响。

在审查上下文与交互方面，Chatlatanagulchai等探讨了开发者提供的上下文信息，TiCoder研究了结构化交互如何提升AI代码评估。这些工作涉及审查流程的辅助因素，但未直接关联到审查者构成与PR结局。

本文与上述研究的区别在于，首次从实证角度系统分析了审查者构成（纯人工vs纯CRA）及CRA生成评论的信号质量如何影响PR的合并与放弃率，填补了现有研究在审查效果与结果关联上的空白。

### Q3: 论文如何解决这个问题？

论文通过实证研究方法，系统分析了代码审查代理在拉取请求中的实际效果。核心方法是基于AIDev平台的19,450个PR数据，筛选出3,109个处于“已评论”状态的独特PR，重点比较纯人工审查与纯CRA审查的差异。

整体框架分为两个主要研究问题：首先评估CRA对PR合并成功率的影响，其次分析CRA生成评论的信号质量与PR废弃的关系。关键技术包括：1）审查者分类系统，将PR按评论者类型分为五类（纯CRA、纯人工、混合等）；2）PR状态分类机制，依据审查状态（批准、驳回、请求更改、已评论）和合并属性确定最终结果（已合并、已关闭、停滞）；3）信号噪声比分析框架，通过关键词分级（Tier1关键信号如运行时错误，Tier2重要信号如架构问题）量化评论质量。

主要模块包括数据过滤模块（专注“已评论”状态PR）、统计分析模块（使用卡方检验验证显著性）和质性分析模块（通过开放式编码技术分类评论，评分者间一致性系数为0.75）。创新点在于首次大规模实证揭示CRA单独审查的局限性：纯CRA审查的PR合并率仅45.20%，较纯人工审查低23.17个百分点，且废弃率显著更高。信号分析显示60.2%的关闭PR信号比低于30%，13个CRA中有12个平均信号比不足60%，表明自动化反馈存在大量噪声。

该方法通过量化指标连接了行业宣称（如CRA可处理80%PR）与实证现实，最终得出结论：CRA应作为人工审查的补充而非替代，人类参与对生成可操作的代码审查至关重要。

### Q4: 论文做了哪些实验？

本研究基于AIDev平台，从19,450个拉取请求（PR）中筛选出3,109个处于“已评论”状态的PR进行实证分析，重点比较纯人工评审与纯代码评审代理（CRA）评审的效果。

**实验设置与数据集**：研究分析了2,456个处于“已评论”状态的PR，根据评审者类型（纯CRA、纯人工用户、混合类型）进行分类。特别地，针对98个已关闭的纯CRA评审PR，进行了信噪比分析，以评估CRA生成评论的质量。

**对比方法**：主要比较了不同评审者类型下的PR合并结果与关闭（即废弃）率。评审者类型包括：纯CRA、纯人工用户、以及以CRA主导、人工主导或平衡的混合评审。

**主要结果与关键指标**：
1.  **合并成功率**：纯CRA评审的PR合并率为45.20%（281个中127个合并），而纯人工评审的合并率为68.37%（1176个中804个），两者相差23.17个百分点。卡方检验证实此差异具有统计显著性（χ² = 83.0319， p < 0.001）。
2.  **废弃率**：纯CRA评审的PR关闭（废弃）率高达34.88%（281个中98个），显著高于纯人工评审的21.60%（1176个中254个）。
3.  **评论质量（信噪比）**：在分析的98个已关闭纯CRA评审PR中，60.2%的PR其评论信号比处于0-30%的低质量区间。在涉及的13个CRA中，有12个（92.31%）的平均信号比低于60%，表明自动生成的评审反馈中存在大量“噪声”。评论数量本身与质量无关，关键是有用反馈的比例。

这些结果表明，缺乏人工监督的CRA倾向于生成低信号质量的反馈，这与更高的PR废弃率相关。

### Q5: 有什么可以进一步探索的点？

该论文揭示了当前代码审查代理（CRA）在独立工作时存在反馈噪声高、合并率低的问题，这为未来研究提供了多个探索方向。首先，可以深入研究CRA反馈噪声的具体来源，例如是模型本身的理解偏差、训练数据不足，还是缺乏对代码库上下文和业务逻辑的把握。其次，论文提到专用型CRA（如安全漏洞检测）表现更好，未来可探索如何设计更细粒度的、领域特定的审查代理，或开发混合系统，让多个专用代理协同工作，再结合人类进行高层次决策。此外，可以研究如何通过改进提示工程、引入代码库的向量化记忆或实时学习机制，来提升CRA反馈的信号质量。最后，论文强调了人工监督的重要性，未来可探索更智能的人机协作流程，例如让CRA优先筛选高置信度问题或自动分类反馈类型，从而降低开发者的认知负荷，而非完全替代人工。这些方向有助于推动CRA从“生成大量评论”转向“提供精准、可操作的洞察”。

### Q6: 总结一下论文的主要内容

本文对代码审查代理在拉取请求中的实际效果进行了实证研究。针对业界关于CRA可独立处理80%PR的宣称，论文通过分析AIDev平台19,450个PR中的3,109个已评论PR，对比了纯人工审查与纯CRA审查的差异。研究发现，纯CRA审查的PR合并率仅为45.20%，较人工审查低23.17个百分点，且废弃率显著更高。通过对98个已关闭纯CRA审查PR的信噪比分析，发现60.2%的PR信号值处于0-30%低区间，13个CRA中有12个平均信号比低于60%，表明当前CRA生成的反馈存在大量噪声且可操作性低。核心结论指出，缺乏人工监督的CRA会产生低价值反馈并增加PR废弃风险，因此CRA应作为人工审查的补充而非替代。论文建议未来从三方面改进：开发量化审查信号的新指标、分析审查工作量以优化CRA设计、建立基于历史性能的自动化审查决策模型。
