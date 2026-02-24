---
title: "When AI Teammates Meet Code Review: Collaboration Signals Shaping the Integration of Agent-Authored Pull Requests"
authors:
  - "Costain Nachuma"
  - "Minhaz Zibran"
date: "2026-02-23"
arxiv_id: "2602.19441"
arxiv_url: "https://arxiv.org/abs/2602.19441"
pdf_url: "https://arxiv.org/pdf/2602.19441v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent 评测/基准"
  - "Agent 协作"
  - "软件工程"
  - "实证研究"
  - "代码审查"
  - "人机交互"
relevance_score: 7.5
---

# When AI Teammates Meet Code Review: Collaboration Signals Shaping the Integration of Agent-Authored Pull Requests

## 原始摘要

Autonomous coding agents increasingly contribute to software development by submitting pull requests on GitHub; yet, little is known about how these contributions integrate into human-driven review workflows. We present a large empirical study of agent-authored pull requests using the public AIDev dataset, examining integration outcomes, resolution speed, and review-time collaboration signals. Using logistic regression with repository-clustered standard errors, we find that reviewer engagement has the strongest correlation with successful integration, whereas larger change sizes and coordination-disrupting actions, such as force pushes, are associated with a lower likelihood of merging. In contrast, iteration intensity alone provides limited explanatory power once collaboration signals are considered. A qualitative analysis further shows that successful integration occurs when agents engage in actionable review loops that converge toward reviewer expectations. Overall, our results highlight that the effective integration of agent-authored pull requests depends not only on code quality but also on alignment with established review and coordination practices.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究自主编码智能体（AI Teammates）在参与实际软件开发协作时面临的核心挑战：如何有效融入人类主导的代码审查工作流。具体而言，研究关注两个关键问题：一是量化智能体提交的拉取请求（Pull Requests）的集成结果（如合并率、决策时间）现状；二是深入分析在审查过程中，哪些协作信号（如审阅者参与度、迭代强度、变更规模、协调稳定性等）真正影响智能体贡献的成功集成。论文指出，现有研究多关注智能体贡献的增长和整体合并率，但忽略了“集成”不仅关乎代码质量，更是一个受社会技术过程（如审查规范、协调实践）影响的结果。因此，本研究通过大规模实证分析，旨在揭示智能体若要成为有效的协作伙伴（而非孤立的补丁生成器），其行为如何与人类既定的审查和协调实践对齐，从而填补智能体在真实协作流程中行为与影响认知的空白。

### Q2: 有哪些相关研究？

相关研究主要分为两类：一是关于传统（人类）Pull Request（PR）集成过程的研究，二是关于AI编码代理的最新工作。

在传统PR研究方面，已有工作将PR评估视为一个社会技术过程，其集成结果不仅取决于代码质量等技术因素，也受到社交互动的影响。例如，研究表明变更规模（change size）会影响PR的接受率，而审查期间的互动（如讨论动态、评审员参与度）在集成决策中扮演核心角色，帮助评审者评估信任、协调成本和感知风险。这些研究为理解PR集成机制奠定了基础。

在AI编码代理方面，随着大语言模型的进步，自主编码代理开始大规模提交PR。AIDev数据集首次系统地记录了这一现象，提供了代理提交PR的采用模式和总体合并结果的数据。然而，现有研究大多将代理提交的PR视为单纯的技术产物，尚未深入探究它们如何融入既有的社会技术审查流程。

本文与这些工作的关系在于：它直接建立在上述两类研究之上。具体而言，本文以传统PR研究中揭示的“审查时协作信号”（如评审员参与度、协调实践）为理论框架，并利用AIDev数据集提供的实证基础，首次系统地探究了这些已知影响人类PR集成的社会技术因素，是否以及如何同样影响AI代理提交的PR的集成结果，从而填补了现有文献的空白。

### Q3: 论文如何解决这个问题？

论文通过定量建模与定性分析相结合的方法，探究了影响AI编码代理提交的Pull Request（PR）能否成功集成（合并）的关键因素。核心方法是：首先，将PR集成结果建模为二元结果（合并 vs. 未合并关闭），并利用逻辑回归模型，量化分析评审过程中的协作信号与合并决策之间的关联。模型控制了不同AI代理的差异，并聚焦于三类可观测的协作信号：1) **迭代与变更规模**（如代码变更行数、修改文件数）；2) **协调稳定性与流程信号**（如是否在评审期间进行了强制推送）；3) **评审者参与度**（如是否收到至少一次评审、首次评审等待时间）。其次，为了深入理解统计关联背后的机制，研究对60个AI提交的PR进行了定性分析，根据预定义的编码手册对每个PR的主要驱动因素进行分类。

研究发现，**评审者参与度是决定集成成功的最强关联因素**，获得评审关注的PR合并几率显著更高。然而，这种参与的有效性取决于其是否形成了**可操作的评审循环**，即评审者提供具体反馈，AI代理据此进行针对性修改，最终与评审期望达成一致。相反，**破坏协调稳定的行为**（如强制推送）和**较大的变更规模**会降低合并可能性，这与评审者评估人类PR时使用的风险启发式方法一致。定量模型还表明，单纯的迭代强度（提交次数）或添加测试文件，在考虑了评审参与和协调稳定性后，对集成结果的独立解释力有限。定性分析进一步证实，缺乏收敛的单纯迭代、设计理念冲突、解决方案不完整或流程策略问题，是导致PR被拒绝的主要原因。

因此，论文的解决方案明确指出：AI代理PR的成功集成不仅取决于代码质量，更关键的是其行为是否与既定的代码评审**社会规范和协作实践**保持一致。有效的集成需要AI代理能够参与稳定、目标一致的评审互动，通过反馈实现收敛，而非仅仅增加活动量。

### Q4: 论文做了哪些实验？

本研究基于AIDev数据集（包含33,596个由AI编码代理提交的Pull Request，PR），进行了两项核心实验。

**实验一（RQ1）：集成与解决基准分析。** 实验旨在建立AI代理提交的PR的集成结果（合并、未合并关闭、开放）和解决速度（决策时间）的基线。实验设置上，直接从GitHub时间戳推导PR状态，计算各代理的合并比例及决策时间（中位数和均值）。主要结果显示：总体合并率为71.5%，但不同代理差异显著，如OpenAI Codex合并率最高（82.6%），而Copilot较低（43.0%）。决策速度差异更大，OpenAI Codex的PR中位决策时间小于1小时，而Copilot和Devin则分别需要13小时和9小时。

**实验二（RQ2）：协作信号与集成关联分析。** 实验旨在探究哪些评审过程中的协作信号与AI代理PR的成功集成相关。实验设置上，采用逻辑回归模型（使用仓库聚类标准误），将合并与否作为二元因变量，自变量涵盖迭代与变更规模（如代码变更行数、修改文件数）、协调稳定性（如强制推送）和评审者参与度（如是否收到评审、首次评审时间）等维度，并控制代理身份。此外，对60个PR样本进行了定性分析，编码其评审过程的主要驱动因素。主要结果显示：**评审者参与度**（收到至少一次评审）与合并可能性呈最强正相关；**协调破坏行为**（如强制推送）和**较大的变更规模**则与较低的合并可能性相关；而单纯的迭代强度或添加测试文件，在控制其他因素后影响有限。定性分析进一步揭示，成功合并主要源于**可执行的评审循环**，即代理能根据具体反馈进行针对性修改并趋于收敛；而设计分歧、协调中断等问题则导致失败。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于主要依赖AIDev数据集进行回顾性分析，未能深入探究人类开发者对AI代理的心理接受度、团队信任建立过程，以及不同项目文化对集成结果的影响。未来研究可进一步探索以下方向：一是设计实验研究，主动部署AI代理到开源或企业团队中，实时观察协作动态与适应性策略；二是开发更细粒度的协作信号度量，如情感分析、沟通风格匹配度，以预测集成成功率；三是构建智能代理行为优化框架，使其能主动学习项目特定的评审规范，减少协调破坏行为；四是研究混合团队中的人类角色演变，如何通过培训或工具设计提升人机协作效率。

### Q6: 总结一下论文的主要内容

这篇论文通过分析AIDev数据集中的AI代理提交的GitHub拉取请求，探讨了其在人类主导的代码审查工作流中的集成情况。研究发现，AI拉取请求的集成成功率不仅取决于代码质量，更关键的是其与现有协作规范的契合度。具体而言，审查者的积极参与（如提供可操作的反馈）能显著提升合并概率，而较大的代码变更规模或破坏协作稳定的行为（如强制推送）则会降低集成可能性。相比之下，单纯的迭代次数对集成结果解释力有限。论文强调，要使AI代理成为有效的协作伙伴，而非孤立的代码生成器，必须使其行为符合代码审查中的社会技术实践，这为未来构建人机混合开发团队提供了重要洞见。
