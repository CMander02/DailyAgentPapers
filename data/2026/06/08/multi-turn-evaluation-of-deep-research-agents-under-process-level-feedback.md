---
title: "Multi-Turn Evaluation of Deep Research Agents Under Process-Level Feedback"
authors:
  - "Rishabh Sabharwal"
  - "Hongru Wang"
  - "Amos Storkey"
  - "Jeff Z. Pan"
date: "2026-06-08"
arxiv_id: "2606.09748"
arxiv_url: "https://arxiv.org/abs/2606.09748"
pdf_url: "https://arxiv.org/pdf/2606.09748v1"
github_url: "https://github.com/sabharwalrishabh/Multi-Turn-Evaluation-of-DRAs"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Deep Research Agent"
  - "Multi-Turn Evaluation"
  - "Process-Level Feedback"
  - "Self-Reflection"
  - "Research Gap Inference"
relevance_score: 8
---

# Multi-Turn Evaluation of Deep Research Agents Under Process-Level Feedback

## 原始摘要

Existing benchmarks for deep research agents (DRAs) assess only single-shot outputs, ignoring a key question: can DRAs improve their reports when guided by feedback? To investigate this, we conduct a multi-turn evaluation of DRAs under two feedback settings: self-reflection, in which the agent revises its report without any external diagnostic signal, and process-level feedback, in which the agent receives guidance targeting gaps in its research strategy. To enable process-level feedback, we design Research Gap Inference (RGI), a method that analyzes patterns of satisfied and unsatisfied rubric criteria to infer research-process gaps. Our analysis reveals three key findings: (i) under self-reflection, agents incorporate and regress on rubric criteria at nearly equal rates, yielding negligible net improvement; (ii) a single round of process-level feedback yields substantial gains, raising the normalized score by approximately $8$-$15$ points and yielding a roughly $35$-$40\%$ incorporation rate; (iii) these gains do not compound over subsequent turns, as agents regress on up to $24\%$ of previously satisfied criteria when rewriting the full report to address remaining gaps. Even with targeted guidance, reliable multi-turn improvement remains out of reach for the DRA architectures we evaluate. Our code and results are publicly available at https://github.com/sabharwalrishabh/Multi-Turn-Evaluation-of-DRAs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前深度研究智能体（DRA）评估中的一个关键缺失：现有基准仅衡量单次输出，忽略了智能体能否根据反馈迭代改进其研究报告。研究背景是，实际应用中用户很少将初稿视为最终版，而会通过多轮反馈不断修正，因此多轮评估对于准确衡量DRA能力至关重要。现有方法的不足主要体现在两方面：一是简单的自我反思（self-reflection）方式缺乏外部诊断信号，已被证明LLMs在自我纠错时往往不可靠，甚至可能退步；二是已有的准则级反馈虽然能针对特定内容缺口提出修正请求，但容易忽略更深层的研究过程缺陷，如不恰当的来源选择、过窄的框架或遗漏相关子主题。核心问题在于，尚未有研究探索在流程级反馈（process-level feedback）下，DRA能否在后续回合中调整其搜索策略、资源选择和论述框架，从而持续提升报告质量。为此，论文设计了研究缺口推断方法（RGI），通过分析满足与未满足的评分准则模式，推断研究过程中的不足并提供策略指引，以系统性地评估DRA在多轮交互中的实际改进能力与局限性。

### Q2: 有哪些相关研究？

该论文的相关研究可分为三类：

1. **深度研究评测基准**: 相关工作包括DeepResearch Bench、DRACO、DeepResearch Bench II和ResearchRubrics。这些基准主要评估单次输出，而本文首次引入多轮反馈评估，弥补了交互式迭代改进的缺失。区别于这些工作，本文关注过程级反馈下的迭代优化。

2. **交互式与多轮深度研究**: 代表工作为IDRBench和一项多轮修订研究。IDRBench利用参考用户模拟器评估交互过程。最相关的工作分析了基于单个标准失败的反馈，本文则研究基于满足与未满足标准模式推断的过程级反馈，并引入表示级诊断（如网络搜索活动、源覆盖）作为补充。

3. **LLM自我修正**: 已有研究指出LLM在没有外部信号时难以自我修正（瓶颈在检测而非修正）。本文的自反思设置验证了这一结论在深度研究报告场景中的适用性，并证明过程级外部反馈能显著提升修正效果，但在多轮中该收益不会累积。

### Q3: 论文如何解决这个问题？

论文通过设计一个多轮评估框架和名为“研究差距推理”（Research Gap Inference, RGI）的方法，来解决深度研究智能体（DRA）在单次输出评估中无法反映其根据反馈改进能力的问题。核心方法是将单轮任务扩展为多轮交互：智能体在每一轮（t>1）接收原始查询、上一轮报告和基于上一轮报告评估生成的反馈，并重新生成完整报告。所有报告均使用包含事实准确性、分析广度和深度、呈现质量和引用质量四个维度的专家制定的评分细则进行评估，以量化改进和退步。

架构上，论文采用了开源的模块化多智能体框架LC-ODR，该框架将研究任务分解为规划、分解、研究和报告四个阶段，并通过完整重写机制实现迭代。关键技术在于RGI反馈生成器：它分析评分细则中达标与未达标标准的模式，特别是跨不同维度（如事实准确性、分析广度和深度）的关联，来推断研究过程中的根本性差距。RGI不简单列举失败点，而是将达标标准作为对比信号，结合引用质量等上游诊断证据，识别出如研究深度不足或广度覆盖不全等流程性问题。随后，它将诊断结果转化为围绕二至三个研究主题的简洁反馈，指导智能体应深化哪些调查领域或优先寻找何种证据，从而提供过程级反馈而非仅针对结果的修正。这一方法的创新在于通过分析评分模式推断研究流程漏洞，并生成结构化、具有指导性的抽象反馈，而非罗列具体失败条款。

### Q4: 论文做了哪些实验？

为了评估深度研究智能体在过程级反馈下的多轮改进能力，论文设计了基于50个DRACO任务的实验。实验设置了两种反馈条件：(1) 自反思：智能体仅凭固定提示修改报告，无外部诊断信号；(2) 过程级反馈 (RGI) ：通过分析未满足的评估标准来推断研究过程的缺陷并给出引导性反馈。对比方法包括GPT-4.1-mini、GPT-4.1和DeepSeek-V4-Flash三个模型，所有模型均使用LC-ODR框架。主要结果如下：

- **自反思** 效果微弱：GPT-4.1-mini的归一化分数仅提升+2.42，GPT-4.1提升+0.09，DeepSeek-V4-Flash反而下降-0.54。这是因为智能体以几乎相同的比例纳入和失去评估标准（例如GPT-4.1的纳入率15.58% vs. 回归率14.74%）。

- **第一轮过程级反馈 (RGI Turn 2)** 带来显著提升：GPT-4.1-mini提升+15.35（归一化分数达53.11），GPT-4.1提升+11.42（达56.19），DeepSeek-V4-Flash提升+8.15（达65.35）。纳入率高达35%-40%。

- **第二轮过程级反馈 (RGI Turn 3)** 收益不叠加：GPT-4.1分数下降-4.97，GPT-4.1-mini仅微增+1.34，只有DeepSeek-V4-Flash保持了+4.01的增长，因其回归率仅8.96%（GPT模型为18.59%-23.57%）。智能体在重写完整报告时会丧失高达24%的先前已满足标准。

轴级分析显示，RGI的最大提升体现在“广度与深度(BD)”和“事实准确性(FA)”上，而“演示质量(PQ)”无改善。案例研究进一步表明，反馈能有效驱动对具体法规、量化数据等的恢复，但当目标证据超出检索能力时，反馈无法引发恢复，且全文重写会放大回归风险。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要体现在以下几个方面。首先，研究仅基于LC-ODR框架下的三个模型和DRACO中的50个任务，未来应扩展到更多框架（如多智能体流水线和单智能体架构）以及完整的DRACO基准测试，以验证结论的泛化性。其次，过程级反馈与标准级反馈的直接比较尚未完成，因为两者在反馈粒度上存在差异，这为设计对比实验提供了空间。最关键的探索方向在于解决“改进无法复合”的瓶颈：由于当前DRA架构采用全重写范式，导致在修正新问题时容易回归先前已满足的标准。未来可以设计显式的多轮感知架构，引入内容保留机制，如增量式报告修改而非全盘重写，或利用分层记忆模块来维持已达标部分。此外，自适应反馈策略值得深入研究，例如根据每轮剩余改进空间动态调整反馈粒度和类型，从而更高效地引导迭代优化。

### Q6: 总结一下论文的主要内容

本文针对当前深度研究代理（DRA）评估仅关注单次输出、忽略反馈修正能力的问题，提出了一种多轮评估框架。研究在两种反馈设置下进行：一是无外部诊断信号的自省反思，二是基于过程级反馈的指导。为提供过程级反馈，作者设计了研究间隙推理方法，通过分析评分标准满足与未满足的模式来推断研究过程中的漏洞。主要发现包括：自省反思导致代理在纳入与放弃评分标准间近乎持平，净改进可忽略；单轮过程级反馈可使标准化分数提升约8-15分，纳入率约35-40%；但后续轮次的改进无法叠加，代理在重写报告时对已满足标准的退化率高达24%。研究表明，当前DRA架构即使有针对性指导，仍无法实现可靠的多轮改进。该工作首次系统评估了DRA在反馈下的迭代能力，揭示了其自我修正能力的局限性，对构建更鲁棒的智能研究助手具有重要指导意义。
