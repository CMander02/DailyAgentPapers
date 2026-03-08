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
relevance_score: 8.5
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

这篇论文旨在解决大语言模型（LLM）在处理高度复杂研究性问题上的能力瓶颈。研究背景是，随着LLM从静态知识库发展为能够进行工具调用和信息检索的“推理引擎”，出现了专注于纵向深入探索的“深度研究”（Deep Research）和侧重于横向广泛信息收集的“广度搜索”（Wide Search）两种范式。然而，现有方法存在明显不足：深度研究虽能深入挖掘特定线索，但可能忽略全局视角和多元证据；广度搜索虽能收集大量信息，但缺乏对信息深度验证和综合推理的能力。两者通常只能处理10-20次检索迭代和约100个网页的规模，难以应对需要长程规划、海量证据收集以及跨异构信息源综合的真正“超级复杂”问题。

本文要解决的核心问题，正是如何让LLM具备执行“超级研究”（Super Research）的能力，以回答那些需要极端深度和极端广度结合的、极其复杂的问题。这类问题（例如涉及多目标权衡、存在矛盾证据的专业领域问题）通常需要超过100次检索步骤和1000多个网页的证据来合成答案。为此，论文提出了一个集成三大核心支柱的新框架：结构化分解、超级广度检索和超级深度调查。同时，为了评估这种超越现有范式的能力，论文创建了一个包含300个专家编写问题的基准测试，并设计了一套基于知识图谱投影的五维自动化评估协议，以解决现有评估方法在衡量复杂推理、逻辑一致性和不确定性表达等方面的缺陷。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、评测类和应用类。

在方法类上，相关工作包括**深度研究**和**广度搜索**。深度研究强调对特定线索进行垂直、迭代的深入探究，以解决具体、细致的问题，通常依赖于思维链提示和递归搜索循环。广度搜索（或当前范式）则侧重于大规模信息获取，旨在覆盖尽可能多的数据节点和网络来源。本文提出的“超级研究”是对这两类范式的超越与整合。它通过**结构化分解、超级广度检索和超级深度调查**三个核心支柱，系统性地解决了需要长程规划、海量证据收集和跨异构信息源综合的超级复杂问题。与通常仅需10-20次检索迭代和约100个网页的现有方法相比，超级研究旨在处理需要100+检索步骤和1000+网页的更高阶复杂性。

在评测类上，现有评估范式存在局限，例如依赖不准确的“LLM即法官”进行报告间比较、使用侧重原子事实回忆的浅层指标、依赖昂贵且难以扩展的人类评估，以及忽视对不确定性表达的评估。本文针对超级研究任务，提出了一个结构化的**五维评估协议**（覆盖度、逻辑一致性、报告效用、客观性和引用健康度），并引入了基于**知识图谱锚定的自动化审计工具**，以实现结构化声明验证、可解释的错误追踪和可复现的评分，从而弥补了现有评测方法在规模和细微差别上的不足。

在应用类上，虽然超级复杂问题在日常应用中不常见，但超级研究作为一个**前沿压力测试和高上限评估框架**，对于衡量LLM的通用研究能力和智能体鲁棒性具有关键意义。它通过暴露模型在长程规划和上下文管理中的潜在弱点，为其在情报分析、科学发现和战略规划等专业领域的应用潜力提供了评估基准。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为“SuperResearch”的基准测试框架来解决评估大语言模型处理高度复杂研究任务能力的问题。其核心方法是设计一个集成“超广检索”和“超深研究”的双重平衡评估体系，模拟专家级研究流程，以压力测试模型的极限能力。

整体框架是一个四阶段的、人机协同的基准构建管道。主要模块与关键技术包括：
1.  **分层任务分解与检索（Phase 1）**：针对复杂问题，由一个“规划者”智能体将其分解为结构化的有向无环图研究任务。研究者和总结者智能体在协作循环中工作：研究者按依赖顺序执行子任务，总结者则将结果持续合成到“动态记忆”中，并注入后续步骤，确保全局上下文随执行过程演进。这解决了信息广度和逻辑依赖的挑战。
2.  **研究图构建（Phase 2）**：这是一个关键创新点，将非结构化的子报告转化为结构化的研究图。系统首先从子报告中提取锚定在具体URL的原子“事实”和衍生的“见解”。随后，在专家指导下，以人机协同方式精炼图结构，构建一个自底向上的拓扑，确保高层见解与支撑性事实节点严格关联。此过程还利用LLM驱动的代码沙箱和搜索工具进行自动计算和事实核查。最后，专家和LLM遍历此图以识别证据集群，迭代生成连接不同子报告的全局见解。
3.  **报告合成与专家编辑（Phase 3）**：利用结构化的研究图和细粒度子报告，一个“写作者”智能体迭代构建最终报告。此过程整合了实时的人机协同工作流：领域专家通过仪表板验证逻辑合理性，并在文本生成过程中进行即时干预和修正，确保报告质量。
4.  **自动化评估指标构建（Phase 4）**：基于研究图和最终报告，生成一套全面的问答对作为评估的基准真值。其创新点在于，除了标准事实检索问题外，还特别设计了“偏见校准”查询，用于评估报告叙述的中立性和客观性，确保在综合主观或冲突信息时保持公正。

该方法的创新性体现在将复杂的认知工作流程化为可操作、可验证的图结构，并通过严格的人机协同设计协议（前沿级特异性、搜索密集型复杂性、专业精确性）来构建高质量的基准数据集，从而实现对模型“超研究”能力的多维度、可追溯的评估。

### Q4: 论文做了哪些实验？

论文在SuperResearch Benchmark上对12个代表性的研究智能体系统进行了全面评估。实验设置将方法分为三大类：1) **深度研究系统**，包括Gemini Deep Research、Sonar Deep Research、Tongyi Deep Research以及OpenAI的o3和o4-mini Deep Research，这些是专为长程规划、多步证据收集和综合而优化的商业代理；2) **原生搜索集成代理**，评估了具备实时网络访问能力的Kimi-k2和Grok-4-1-fast；3) **搜索增强基线**，使用LangGraph框架和统一的Tavily Search检索工具，集成了DeepSeek-r1、Claude-3.5-sonnet、Minimax-m2.1、Llama-3.3-70B和Qwen-2.5-72B等基础模型。

**数据集/基准测试**：使用作者构建的SuperResearch Benchmark，包含300个跨领域的专家级复杂问题，每个问题可能需要超过100次检索步骤和1000多个网页来调和冲突证据。

**主要结果与关键指标**：评估围绕五个核心维度进行。总体得分上，深度研究系统表现最佳，Gemini Deep Research以28.62分领先，Sonar Deep Research以27.04分紧随其后。原生搜索代理Kimi-k2（26.16分）和Grok-4-1-fast（24.55分）表现优异，甚至超过了部分深度研究系统。搜索增强基线模型得分集中在16-23分区间。
关键数据指标显示：在**覆盖率**上，Gemini Deep Research最高（33.15）；在**逻辑一致性**上，Kimi-k2表现最好（24.80）；在**报告效用性**上，Sonar Deep Research领先（26.50）；在**客观性**上，Sonar Deep Research得分最高（36.50）。**引用健康度**方面，Claude-3.5-sonnet的源主导度最低（2.08），表明引用分布最均衡；而o3 Deep Research的叙事垄断度最低（32.33），说明叙事多样性较好。

实验还通过扰动测试验证了评估方法的可靠性，结果表明论文提出的图锚定评估协议相比传统的LLM Judge方法，对质量波动具有更高的敏感性和一致性。

### Q5: 有什么可以进一步探索的点？

该论文提出的Super Research范式虽具开创性，但其局限性和未来探索空间仍十分广阔。首先，当前任务设定依赖大量人工检索和网页证据，计算成本极高，且对实时性、动态变化信息的处理能力未经验证。其次，评估虽通过图锚定审计覆盖五个维度，但“报告效用”和“客观性”等主观指标仍依赖人工评分，未来需开发更自动化、可量化的评估协议。

未来研究方向可包括：1）优化检索与推理的效率，引入分层检索或证据压缩技术，降低千级网页依赖；2）增强对冲突证据与不确定性的动态决策能力，例如引入贝叶斯推理或多智能体辩论机制；3）拓展任务场景至实时信息流（如新闻、学术更新），测试系统在动态环境中的持续研究能力；4）探索跨模态证据融合（如图表、音视频），以应对更复杂的真实世界问题。此外，可将该“天花板测试”与现有基准结合，构建从简单到超级复杂的研究能力光谱，更细致地评估模型能力边界。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在解决高度复杂问题上的局限性，提出了“超级研究”任务与评估框架。核心问题是现有模型虽能进行深度研究或广度搜索，但难以处理需要长程规划、海量证据收集及跨异构信息综合的复杂问题。为此，作者定义了超级研究任务，其方法整合了三个关键部分：将问题结构化分解为研究计划、执行超广度检索以获取多元视角、以及通过迭代查询进行超深度调查以消除不确定性。为评估该能力，研究构建了一个包含300个跨领域专家级问题的基准，每个问题可能需要超过100次检索步骤和上千个网页来调和矛盾证据。系统最终生成带有细粒度引用和中间产物（如大纲和表格）的可验证报告，以确保推理可追溯。主要结论是，超级研究可作为评估大语言模型研究能力的“天花板”式压力测试，其表现是模型通用研究能力的强有力代理指标。这项工作不仅为评估模型的复杂问题解决能力提供了系统化的基准和审计协议（涵盖覆盖率、逻辑一致性、报告效用、客观性和引用健康五个维度），也指明了未来增强LLM在长链条、高不确定性任务中稳健性的方向。
