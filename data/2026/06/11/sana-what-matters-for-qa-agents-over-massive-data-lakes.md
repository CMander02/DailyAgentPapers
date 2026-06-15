---
title: "SANA: What Matters for QA Agents over Massive Data Lakes?"
authors:
  - "Austin Senna Wijaya"
  - "Jiaxiang Liu"
  - "Haonan Wang"
  - "Eugene Wu"
date: "2026-06-11"
arxiv_id: "2606.13904"
arxiv_url: "https://arxiv.org/abs/2606.13904"
pdf_url: "https://arxiv.org/pdf/2606.13904v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.DB"
tags:
  - "EQA Agent"
  - "Agent诊断/消融分析"
  - "Agent评测框架"
  - "Agent规划/搜索/数据分析"
  - "多组件Agent解耦"
relevance_score: 9.0
---

# SANA: What Matters for QA Agents over Massive Data Lakes?

## 原始摘要

Exploratory question answering (EQA) over data lakes requires an LLM agent to discover relevant sources, analyze retrieved data, and adapt its actions based on intermediate results. End-to-end accuracy alone cannot distinguish failures in search, planning, data analysis, or the agent's Action Policy: its decisions about what to do next and when to submit an answer. We present SANA (Search Agent Navigation Ablation framework), a diagnostic ablation framework that transforms EQA tasks into runtime profiles containing gold source sequence, sanitized subquestions, and execution records. SANA uses these profiles to construct idealized search, planning, and data-analysis tools, allowing each component to be ablated; the residual gap is diagnostic evidence for policy failures.
  To illustrate SANA as a reusable evaluation framework, we adapted two recent EQA benchmarks, LakeQA and KramaBench, and evaluated lightweight and mid-sized agents under fixed prompts, budgets, data lakes, and runtimes. Across both benchmarks, data analysis is a consistent bottleneck while planning is less so. Search is a major limitation in LakeQA's large data-lake setting, but less so for the smaller-scale KramaBench. SANA thus deconstructs end-to-end task accuracies into a diagnosis of where data-lake agents fail, and allows for systematic comparisons of progress in search, planning, data analysis, and agent design.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决探索式问答（EQA）任务中，端到端准确性无法区分失败根源的问题。研究背景是基于数据湖的探索式问答，需要一个LLM代理在庞大的数据湖中发现相关数据源、分析检索结果，并根据中间结果动态调整行动。现有方法虽在搜索、规划、工具使用等单项能力上有所进展，但缺乏一个系统框架来隔离评估搜索、规划、数据分析执行和代理策略（即决定下一步做什么、何时提交答案的决策过程）对最终准确率的贡献。因此，当代理回答错误时，究竟是数据缺失、规划不当、分析代码错误，还是代理策略本身（如过早提交答案、未验证中间证据）导致的，无法被区分。本文的核心问题是：如何诊断并量化EQA代理在端到端任务中，由不同组件（搜索、规划、数据分析）和代理策略各自贡献的性能瓶颈。为此，论文提出了SANA诊断框架，通过构建使用理想化组件（如基于真实数据的完美搜索和规划）的代理基线，然后逐一替换为标准实现进行消融实验，从而分离出每个组件的实际影响，并识别出即使组件都理想化后仍然存在的策略性失败（如错误决策或预算耗尽）。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要可以分为以下几类：

1. **评测类基准**：主要包括探索式问答基准，如 LakeQA 和 KramaBench，它们要求智能体在大型数据湖中搜索、检查、计算和综合信息。此外，还有像 HotpotQA、MuSiQue 等要求对异构数据类型进行多跳推理的基准，以及 DCI 和 Metadata Reasoner 等智能体数据发现评估。本文与这些工作的区别在于，SANA 不是简单地评测端到端准确率，而是将这些任务用于诊断 EQA 智能体中具体哪个部分（搜索、规划、执行）失败。

2. **组件方法类**：包括数据集发现系统（如 D3L、Starmie）、文本到SQL和数据智能体基准（如 BIRD、Spider 2.0），以及分解方法（如 DecompRC、DIN-SQL）。SANA 将这些组件视为相互交互的瓶颈而非孤立任务，强调分解必须指导发现，发现必须反馈分析，分析又必须指导后续发现，而现有工作往往仅优化单个组件。

3. **智能体RAG与导航类**：包括 ReAct、IRCoT、Self-RAG 等推理与行动方法，以及 MA-RAG、A-RAG 等多智能体或分层检索架构。这些系统虽然也面临与 EQA 类似的导航决策问题，但它们的评估常常混淆了模型策略、检索基础设施和工具设计等不同因素。SANA 通过固定任务和运行时，同时消融搜索、规划和执行组件，提供了受控的评估框架，从而能系统性地诊断失败原因。

### Q3: 论文如何解决这个问题？

SANA通过一个诊断性消融框架来解决EQA任务中的组件失效问题。核心方法是构建任务配置文件（profile），包含金标准源序列（gold source sequence）、清洁化子问题（sanitized subquestions）和执行记录（execution records）。基于这些profile，SANA为搜索、规划和数据分析三个主要组件分别创建理想化版本进行消融实验。

整体框架将EQA任务分解为三个可单独消融的组件：搜索、规划和数据分析。对于搜索消融，SANA用理想搜索工具 \(f^{ideal}\) 替换标准搜索工具，其搜索空间限制在金标准数据集 \(\mathcal{D}_{gold}\) 上，确保每次返回的结果都相关。对于规划消融，SANA提供清洁化的子问题序列 \(\widetilde{\mathcal{Q}}\)，明确告知任务分解顺序，但不泄露具体数据集名称。对于数据分析消融，SANA用理想分析工具 \(g^{ideal}\) 替换标准工具，当代理意图匹配执行记录中的分析意图时，直接返回金标准答案。

关键技术包括：1）基于意图的消融（intent-based ablation），提取每个工具调用的语义意图而非直接替换组件；2）任务配置文件自动构建，从LakeQA和KramaBench基准中提取所需信息；3）子代理（subagent）机制，用于匹配意图和选择相关数据集。创新点在于将端到端精度分解为搜索、规划、数据分析和策略（action policy）四个维度的失效诊断，使研究人员能够定位具体瓶颈，并支持对搜索、规划、数据分析和代理设计进展的系统比较。

### Q4: 论文做了哪些实验？

为了诊断数据湖问答（EQA）代理的失败原因，论文使用SANA框架在LakeQA和KramaBench两个基准上进行了消融实验。实验设置包括：固定提示、预算（搜索成本）、数据湖规模以及运行时，对比了轻量级和中型代理（具体模型未明确说明）在完全条件（Ablated condition，即SANA提供理想化组件）与基线条件（Natural condition，即代理自行完成所有步骤）下的表现。

主要结果通过端到端准确率（E2E accuracy）和组件级失败归因来呈现。在LakeQA（大规模数据湖）上，基线准确率约为16%，而理想搜索可达38%，理想数据分析+规划可达55%，理想所有组件可达56%。SANA诊断出：数据分析是持续瓶颈（造成约20-25个百分点的损失），规划问题较小（3-5个百分点），搜索是主要限制（约15-19个百分点）。在KramaBench（小规模数据湖）上，基线准确率约为25%，理想搜索约40%，理想数据分析+规划约55%，理想所有组件约60%。搜索局限较小（10-15个百分点），而数据分析仍是主要瓶颈（约20-25个百分点），规划影响依然最小。这些实验揭示了EQA代理在不同数据湖规模下的组件级失败模式。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其诊断框架SANA本身并未提供改进组件的具体方法，仅揭示了失败类型。未来可探索以下方向：1）将SANA的输出反馈给强化学习或动态规划模块，自动调整Agent的动作策略，例如当检测到搜索瓶颈时主动触发多轮检索；2）针对数据分析这一一致瓶颈，可引入代码执行验证或表格推理专用的图神经网络，增强结构化数据理解；3）在搜索环节，结合数据湖的图谱结构辅助向量检索，或使用可学习的终止条件判断何时停止检索。此外，当前框架假设的理想化组件（如黄金序列）在真实场景中难以获得，未来可研究如何从弱监督信号中近似这些基准，使诊断更加实用。

### Q6: 总结一下论文的主要内容

SANA提出一种名为"Search Agent Navigation Ablation"的诊断消融框架，用于分析大数据湖中探索式问答(EQA)智能体的失败原因。EQA任务要求智能体在数据湖中发现相关数据源、分析检索数据并动态调整行动，但端到端准确率无法区分搜索、规划、数据分析或行动策略层面的错误。SANA通过将EQA任务转化为包含真实数据源序列、标准化子问题和执行记录的运行时概要，创建理想化的搜索、规划和数据分析工具，通过消融各组件保留的残差来诊断策略失败。在LakeQA和KramaBench两个基准上的实验表明，数据分析执行是持续存在的瓶颈，搜索在LakeQA的大规模数据湖设置中成为主要限制，而规划影响相对较小。SANA的核心贡献在于将端到端任务准确率分解为对数据湖智能体失败环节的诊断，为系统比较搜索、规划、数据分析和智能体设计的进展提供了可复用的评估框架。
