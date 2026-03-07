---
title: "Super Research: Answering Highly Complex Questions with Large Language Models through Super Deep and Super Wide Research"
authors:
  - "Yubo Dong"
  - "Nianhao You"
  - "Yuxuan Hou"
  - "Zixun Sun"
  - "Yue Zhang"
date: "2026-02-28"
arxiv_id: "2603.00582"
arxiv_url: "https://arxiv.org/abs/2603.00582"
pdf_url: "https://arxiv.org/pdf/2603.00582v2"
categories:
  - "cs.CL"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 8.0
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "Super Research (structured decomposition, super wide retrieval, super deep investigation)"
  primary_benchmark: "Super Research Benchmark (300 expert-written questions)"
---

# Super Research: Answering Highly Complex Questions with Large Language Models through Super Deep and Super Wide Research

## 原始摘要

While Large Language Models (LLMs) have demonstrated proficiency in Deep Research or Wide Search, their capacity to solve highly complex questions-those requiring long-horizon planning, massive evidence gathering, and synthesis across heterogeneous sources-remains largely unexplored. We introduce Super Research, a task for complex autonomous research tasks that integrates (i) structured decomposition into a research plan, (ii) super wide retrieval for diverse perspectives, and (iii) super deep investigation to resolve uncertainties through iterative queries. To evaluate this capability, we curated a benchmark of 300 expert-written questions across diverse domains, each requiring up to 100+ retrieval steps and 1,000+ web pages to reconcile conflicting evidence. Super Research produces verifiable reports with fine-grained citations and intermediate artifacts (e.g., outlines and tables) to ensure traceable reasoning. Furthermore, we present a graph-anchored auditing protocol that evaluates Super Research along five dimensions: Coverage, Logical Consistency, Report Utility, Objectivity and Citation Health. While super-complex questions may be infrequent in standard applications, Super Research serves as a critical ceiling evaluation and stress test for LLM capabilities. A model's proficiency within Super Research acts as a powerful proxy for its general research competence; success here suggests the robustness necessary to navigate nearly any subordinate research task. Leaderboard is available at: https://cnsdqd-dyb.github.io/Super-Research-Benchmark/

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在处理高度复杂、开放式研究性问题时能力不足的核心挑战。研究背景是，随着LLM从静态知识库发展为能够进行工具调用和信息检索的“推理引擎”，出现了专注于垂直深入探究的“深度研究”和侧重于大规模信息收集的“广度搜索”范式。然而，现有方法存在明显不足：无论是深度研究还是广度搜索，其操作规模通常限于10-20次检索迭代和约100个网页，它们难以应对那些需要**长程规划、海量证据收集以及跨异构来源综合**的“超级复杂”问题，例如涉及多目标权衡和矛盾证据的科学发现或战略规划问题。

因此，本文要解决的核心问题是：如何定义、实现并系统评估LLM执行此类“超级研究”任务的能力。具体而言，论文提出了“超级研究”这一新任务框架，它通过**结构化分解、超级广度检索和超级深度调查**三大支柱，将复杂问题拆解为可执行的研究计划，并协调超过100次检索步骤和1000多个网页的信息，以生成带有细粒度引用和可追溯推理过程的验证性报告。同时，为了填补现有评估方法（如不准确的LLM-as-a-Judge、浅层事实召回指标、成本高昂的人工评估等）在衡量此类复杂探究时的空白，论文还引入了一个基于知识图谱锚定的自动化审计协议，从覆盖度、逻辑一致性、报告效用、客观性和引用健康度五个维度进行全面评估。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕大语言模型（LLM）在复杂研究任务上的能力展开，可分为方法类、评测类和任务/基准类。

**方法类**：核心相关工作是**深度研究**和**广度搜索**。深度研究强调垂直探索，通过链式推理和递归搜索深入特定证据链以解决细致问题。广度搜索（或当前范式）侧重于大规模信息采集，以覆盖尽可能多的数据源。本文提出的“超级研究”是对这两者的综合与超越，它不仅要求**结构化分解**（将复杂问题拆解为多层研究计划），还结合了**超级广度检索**（确保覆盖多元视角）和**超级深度调查**（通过迭代查询解决不确定性），旨在处理需要超长规划、海量证据收集和跨异构来源合成的“超级复杂”问题。

**评测类**：现有评估方法存在局限，例如依赖不准确的LLM-as-a-Judge、侧重于浅层事实回忆的指标、成本高昂的人工评估，以及忽视对不确定性的合理表达。本文与之区别在于，它提出了一种**基于图锚定的审计协议**，通过将生成报告映射到专家构建的知识图谱上，从覆盖度、逻辑一致性、报告效用、客观性和引用健康五个维度进行结构化、可解释且可扩展的评估。

**任务/基准类**：现有基准（通常针对深度研究或广度搜索）的复杂度和规模有限，通常涉及10-20次检索迭代和约100个网页。本文则构建了一个包含300个专家编写问题的**新基准**，其问题复杂度极高，需要管理100+检索步骤和合成1000+网页的证据，以此作为对LLM能力的“天花板”评估和压力测试。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Super Research的综合性研究框架来解决高度复杂问题，该框架整合了结构化分解、广泛检索与深度调查，并辅以系统化的评估协议。其核心方法围绕“Super Wide”和“Super Deep”的双重平衡展开，旨在测试智能体在非结构化、高熵信息环境中进行长程规划、海量证据收集与跨异构源综合推理的极限能力。

整体框架采用分阶段流水线设计，主要包括四个关键阶段：1）分层任务分解与检索：通过规划智能体将复杂查询分解为有向无环图（DAG）结构的研究任务，研究器与总结器在依赖感知的顺序中协作执行子任务，并利用动态记忆迭代注入上下文，确保全局推理的连贯性。2）研究图构建：将非结构化子报告转化为结构化研究图，提取锚定于URL的原子“事实”与衍生“洞察”，并采用人机协同流程，由专家精炼图结构，自底向上构建高阶洞察与事实节点的严格连接，再通过LLM驱动的代码沙盒与搜索工具进行自动计算与事实核查。3）报告合成与专家编辑：基于结构化研究图和细粒度子报告，写作智能体分章节迭代生成最终报告，同时通过实时人机交互仪表板，由领域专家验证逻辑合理性并进行动态修正。4）自动评估指标构建：利用研究图与最终报告生成全面的问答对集合，特别包含用于评估报告中立性与客观性的“偏差校准”查询，确保合成主观或冲突信息时的公正性。

主要创新点体现在：一是提出了融合广度覆盖与深度推理的双平衡基准构建原则，强调前沿特异性、搜索密集型复杂性与专业精确性；二是引入了认知等级约束专家模拟框架，利用高级LLM在严格负约束下生成高复杂度研究计划，再经专家审核确保真实性与可解性；三是设计了图锚定审计协议，从覆盖率、逻辑一致性、报告效用、客观性与引用健康度五个维度系统评估研究能力，为LLM的极限研究性能提供了可追溯、可验证的评估标准。

### Q4: 论文做了哪些实验？

论文在SuperResearch Benchmark上对12个代表性研究系统进行了全面评估。实验设置将方法分为三大类：深度研究系统（如Gemini Deep Research、Sonar Deep Research）、原生搜索集成智能体（如Kimi-k2、Grok-4-1-fast）和搜索增强基线（使用LangGraph框架集成DeepSeek-r1、Claude-3.5-sonnet等模型）。评估使用了一个包含300个专家编写问题的基准测试，这些问题涵盖多个领域，需要多达100+检索步骤和1000+网页来处理冲突证据。

主要结果通过五个核心维度衡量：覆盖率（Coverage, $\mathcal{R}_{weighted}$）、逻辑一致性（Consistency, $\mathcal{C}_{logic}$）、报告效用（Utility, $\mathcal{U}_{qa}$）、客观性（Objectivity, $\mathcal{O}_{bias}$）以及引用健康度（包括来源主导性$\mathcal{D}_{src}$和叙事垄断性$\mathcal{M}_{mono}$）。关键数据显示，表现最佳的Gemini Deep Research总体得分（Overall）为28.62，其覆盖率（33.15）和客观性（35.43）突出，但逻辑一致性（22.92）仍显不足。原生搜索集成智能体Kimi-k2在逻辑一致性上表现最佳（24.80）。相比之下，搜索增强基线模型得分普遍在16-23之间，表明与顶级商业系统存在差距。

实验还进行了评估方法的敏感性分析，比较了提出的图度量与标准LLM Judge。在扰动实验中，图度量对质量变化的响应率（57.4%至79.6%）显著高于LLM Judge（14.8%至22.2%），且在不同LLM评估器间表现出更高的一致性（例如，客观性维度的归一化标准差仅为1.07%，而LLM Judge为7.82%）。这些结果证实了超级复杂问题对现有系统仍构成严峻挑战，并揭示了检索广度与推理深度之间的正相关关系。

### Q5: 有什么可以进一步探索的点？

该论文提出的Super Research范式虽在复杂问题研究上设定了新标杆，但仍存在多方面局限和探索空间。首先，其依赖大规模检索（超宽检索）和深度迭代查询，计算成本和耗时极高，难以实用化，未来需研究更高效的证据筛选与融合机制，例如通过强化学习动态调整检索深度与广度。其次，基准问题虽复杂但领域覆盖仍有限，需扩展至更多动态领域（如实时科技、金融）以检验泛化性。此外，评估维度中的“客观性”和“逻辑一致性”仍依赖人工审计，可探索自动化评估框架，结合事实核查与逻辑推理模型。从方法层面看，当前系统在冲突证据合成上表现不足，未来可引入多智能体辩论机制或不确定性量化技术，提升推理的稳健性。最后，该任务作为“天花板测试”虽能评估模型极限，但如何将其能力迁移至日常研究场景（如教育、科普）亦是重要方向，需设计渐进式任务难度与适应性学习策略。

### Q6: 总结一下论文的主要内容

该论文提出了“超级研究”任务，旨在解决大语言模型在处理高度复杂问题时的局限性。这类问题通常需要长程规划、海量证据收集以及跨异构信息源的深度综合。论文的核心贡献是定义了一个集成结构化分解、超广检索和超深调查的新型研究框架，并构建了包含300个专家级问题的基准测试集，每个问题可能涉及上百次检索和上千个网页以整合冲突证据。

方法上，超级研究将复杂问题分解为可执行的研究计划，通过超广检索获取多元视角，并利用超深调查迭代查询以消除不确定性。系统最终生成带有细粒度引用和中间产物（如大纲和表格）的可验证报告，确保推理过程可追溯。此外，论文提出了一种基于图的审计协议，从覆盖度、逻辑一致性、报告效用、客观性和引用健康五个维度评估研究质量。

主要结论指出，超级研究虽在常规应用中不常见，但可作为评估大语言模型能力上限的关键压力测试。模型在此任务上的表现是其综合研究能力的强有力指标，成功完成意味着具备处理几乎所有次级研究任务的鲁棒性。该工作为推进AI自主研究设立了新的高标准和评估体系。
