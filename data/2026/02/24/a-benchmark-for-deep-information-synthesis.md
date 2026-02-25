---
title: "A Benchmark for Deep Information Synthesis"
authors:
  - "Debjit Paul"
  - "Daniel Murphy"
  - "Milan Gritta"
  - "Ronald Cardenas"
  - "Victor Prokhorov"
  - "Lena Sophia Bolliger"
  - "Aysim Toker"
  - "Roy Miles"
  - "Andreea-Maria Oncescu"
  - "Jasivan Alex Sivakumar"
  - "Philipp Borchert"
  - "Ismail Elezi"
  - "Meiru Zhang"
  - "Ka Yiu Lee"
  - "Guchun Zhang"
  - "Jun Wang"
  - "Gerasimos Lampouras"
date: "2026-02-24"
arxiv_id: "2602.21143"
arxiv_url: "https://arxiv.org/abs/2602.21143"
pdf_url: "https://arxiv.org/pdf/2602.21143v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.IR"
  - "cs.LG"
tags:
  - "Agent Benchmark"
  - "Information Synthesis"
  - "Tool Use"
  - "Reasoning"
  - "Evaluation"
relevance_score: 8.0
---

# A Benchmark for Deep Information Synthesis

## 原始摘要

Large language model (LLM)-based agents are increasingly used to solve complex tasks involving tool use, such as web browsing, code execution, and data analysis. However, current evaluation benchmarks do not adequately assess their ability to solve real-world tasks that require synthesizing information from multiple sources and inferring insights beyond simple fact retrieval. To address this, we introduce DEEPSYNTH, a novel benchmark designed to evaluate agents on realistic, time-consuming problems that combine information gathering, synthesis, and structured reasoning to produce insights. DEEPSYNTH contains 120 tasks collected across 7 domains and data sources covering 67 countries. DEEPSYNTH is constructed using a multi-stage data collection pipeline that requires annotators to collect official data sources, create hypotheses, perform manual analysis, and design tasks with verifiable answers. When evaluated on DEEPSYNTH, 11 state-of-the-art LLMs and deep research agents achieve a maximum F1 score of 8.97 and 17.5 on the LLM-judge metric, underscoring the difficulty of the benchmark. Our analysis reveals that current agents struggle with hallucinations and reasoning over large information spaces, highlighting DEEPSYNTH as a crucial benchmark for guiding future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）智能体在复杂、真实世界任务中评估不足的问题。研究背景是，尽管基于LLM的智能体在工具使用（如网页浏览、代码执行）方面展现出处理复杂任务的潜力，并被应用于信息搜索，但现有评估基准大多聚焦于浅层的事实检索、单一来源（如维基百科）的问答，或是人为设计的信息寻找问题。这些基准未能充分评估智能体在需要从多源信息中综合推理并生成新见解的真实任务上的能力，也忽视了全球不同地区、语言和信息生态的多样性。

现有方法的不足在于，它们无法有效衡量智能体完成“信息综合”这一核心认知任务的表现，即收集多个来源的信息，进行推理，最终形成连贯见解的能力。例如，回答“哪些非东盟国家在疫情后到访新加坡的游客量恢复显著？”这类问题，需要识别国家、从不同数据源提取并分析游客到达数据，这超出了简单检索的范畴。

因此，本文要解决的核心问题是：缺乏一个能够真实评估智能体在耗时、多步骤、需跨多源信息进行综合与推理的现实任务上性能的基准。为此，论文引入了DEEPSYNTH基准，它包含120个跨7个领域和67个国家的任务，要求智能体进行信息收集、综合和结构化推理以产生可验证的见解。该基准的构建模拟了真实分析过程，旨在揭示当前智能体在处理大信息空间时的幻觉和推理缺陷，为未来研究提供关键的评估指引。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测基准类、智能体方法类以及信息合成任务类。

在**评测基准类**工作中，现有基准如WebArena、WebShop和BIRD等，主要评估智能体在网页导航、工具使用或数据库查询等单一环境下的信息检索能力。这些基准通常聚焦于事实查找或基于已知源（如维基百科）的简单问答，任务相对孤立且语境有限。本文提出的DEEPSYNTH则截然不同，它专门设计用于评估智能体在真实、耗时任务中进行**跨多源信息收集、综合与结构化推理**以产生新见解的能力，其任务覆盖全球67个国家、7个领域，并强调对非英语及非主流信息源的整合，从而填补了现有基准在评估深度信息合成与跨域推理方面的空白。

在**智能体方法类**研究中，近期涌现的深度研究智能体（如o3-deep-research、smolagents、OWL）以及先进的大语言模型（如GPT-4、Gemini、DeepSeek-R1）均在复杂任务规划、工具调用和网络交互方面取得了进展。然而，本文的实验表明，这些现有智能体在DEEPSYNTH上表现不佳，最高F1分数仅8.97（智能体）和6.25（纯LLM），暴露出它们在处理大规模信息空间时普遍存在的**幻觉问题、导航错误以及合成推理缺陷**，尤其是在涉及非洲等代表性不足地区的数据时性能骤降。这说明当前方法虽提升了信息获取能力，但尚未解决深度信息合成这一核心挑战。

最后，在**信息合成任务**本身的研究中，传统工作多关注文本摘要或多文档问答，但通常依赖于预先收集、结构良好的文档集。DEEPSYNTH则模拟了更真实的开放世界分析流程：要求智能体主动浏览全网，从非结构化文本和结构化表格中动态提取信息，并进行假设检验与洞察生成。其通过专家人工构建包含黄金标准推理链的任务，确保了评估的严谨性与现实相关性，从而将评测重点从“信息寻找”转向了“信息合成与洞察创造”。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为DEEPSYNTH（在论文中称为\ourdata）的新型基准测试来解决现有评估基准无法充分衡量智能体在真实、复杂任务中信息综合与深度推理能力的问题。其核心方法是设计一个多阶段的数据收集流程，以创建需要多源信息合成、基于现实世界灵感、答案可验证、多样化且能抵御记忆的复杂任务集合。

整体框架与主要模块包括四个关键步骤：1) **数据源识别**：由16位专家从7个领域（社会经济、金融、环境等）和67个国家中筛选出223个官方可信的数据源，确保任务具有现实基础和实用性。2) **假设生成**：针对每个数据源，专家提出一个或两个需要深入分析才能验证的假设（例如“英国各地区空气质量与肺炎相关死亡是否存在线性关系”），旨在超越简单事实检索，鼓励深度推理。3) **假设验证**：专家对数据源进行详细分析，验证假设是否成立，并确保能从中推导出可验证的答案，此步骤过滤或修正了不满足要求的假设。4) **任务构建**：基于验证后的假设，专家构建具体的任务问题，并提供中间推理步骤、支持证据（如URL）、所需工具（如代码解释器）和最终答案（以结构化JSON格式输出）。所有任务还经过第二轮独立标注验证，确保答案一致性，最终得到120个高质量任务。

创新点主要体现在：首先，**构建流程的创新**：不同于从已知事实反向设计问题的常见做法，该研究采用从真实数据源出发、通过假设生成与分析来正向构建任务的方法，确保答案无法通过简单检索或记忆获得，从而强制要求系统进行多步骤规划和推理。其次，**任务设计的综合性**：任务不仅要求信息收集（平均需浏览4.2个网页），更强调信息合成操作，如趋势检测、相关性分析、异常识别和比较排名等（统计显示合成操作类型多样），模拟了现实世界中决策者（如政策制定者、旅行顾问）所需的深度分析。最后，**评估目标的针对性**：基准测试专门用于揭示当前智能体在大型信息空间中的幻觉和推理缺陷，其极低的评估分数（最佳F1分数仅8.97）凸显了现有技术的不足，为未来智能体在复杂信息合成与推理能力的研究提供了关键的评估方向和挑战。

### Q4: 论文做了哪些实验？

论文在DEEPSYNTH基准上进行了全面的实验评估。实验设置方面，评估了五款前沿大语言模型（如o4-mini、GPT-4.1、GPT-5、Gemini-2.5-Pro、DeepSeek-R1）以及三个深度研究智能体框架（o3-deep-research、smolagents、OWL）。所有模型使用统一指令提示，并评估了其工具使用能力（如网页浏览、搜索、代码解释器）。评估指标包括严格的精确匹配、基于键值对正确率的F1分数（含精确率、召回率），以及使用LLM-as-a-judge的软性评分。

数据集为论文提出的DEEPSYNTH基准，包含7个领域、覆盖67个国家的120个任务，要求智能体从多源信息中综合推理得出结构化见解。主要对比了上述模型与智能体框架的性能。

主要结果显示，所有系统表现均不佳。在基础LLM中，GPT-5.2-Pro的F1分数最高（8.70），LLM-judge评分最高为6.67（GPT-5.2-Pro和DeepSeek-R1-Reasoner）。智能体框架中，o3-deep-research表现最佳，F1分数为8.97，LLM-judge评分为17.5。严格的精确匹配指标下，几乎所有模型得分接近零。消融实验表明，移除搜索工具导致性能下降最大（F1下降1.81点），而提供推理中间步骤能显著提升表现（如Smolagent的F1从3.75升至10.50）。此外，Best-of-N实验显示，多次尝试（Best@5）可提升LLM-judge准确率至25%，但自一致性投票结果很差（5%），表明当前智能体输出方差大、缺乏可靠性。

### Q5: 有什么可以进一步探索的点？

基于论文分析，未来研究可从以下几个方向深入探索：首先，针对模型在复杂多步推理上的不足，可开发更强大的规划与推理模块，例如引入显式的符号推理或分层任务分解机制，以提升对长链条任务的执行能力。其次，当前智能体在信息导航与合成上错误频发，需优化工具使用与信息检索策略，比如增强网页交互能力或集成更精准的文档解析工具。此外，基准测试中涉及的地域数据不均衡（如非洲任务表现极差）揭示了模型可能存在的偏见与泛化局限，未来应扩充多样化、低资源地区的数据集以提升鲁棒性。最后，可探索人机协作模式，将人类反馈融入智能体的学习循环，逐步修正幻觉与逻辑错误，推动智能体向更可靠、深度的信息合成能力演进。

### Q6: 总结一下论文的主要内容

该论文针对当前大语言模型智能体在解决复杂现实任务时评估不足的问题，提出了一个名为DEEPSYNTH的新型基准测试。其核心贡献是构建了一个专注于评估智能体深度信息综合能力的评测集，该能力涉及从多源信息中收集、整合并进行结构化推理以产生新见解，而非简单的事实检索。

论文首先定义了现有基准在评估复杂、耗时且需综合推理的现实任务上的局限。为此，方法上，作者通过一个多阶段数据收集流程构建了DEEPSYNTH，涵盖7个领域、67个国家的120个任务。该流程要求标注者收集官方数据源、提出假设、进行手动分析并设计具有可验证答案的任务。

主要结论是，在DEEPSYNTH上评估的11个先进大语言模型及深度研究智能体表现不佳，最高F1分数仅为8.97和17.5，凸显了该基准的难度。分析表明，现有智能体在处理大规模信息空间时存在幻觉和推理困难。因此，DEEPSYNTH作为一个关键的评估工具，揭示了当前模型的不足，并为未来研究指明了方向。
