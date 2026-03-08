---
title: "LiveCultureBench: a Multi-Agent, Multi-Cultural Benchmark for Large Language Models in Dynamic Social Simulations"
authors:
  - "Viet-Thanh Pham"
  - "Lizhen Qu"
  - "Thuy-Trang Vu"
  - "Gholamreza Haffari"
  - "Dinh Phung"
date: "2026-03-02"
arxiv_id: "2603.01952"
arxiv_url: "https://arxiv.org/abs/2603.01952"
pdf_url: "https://arxiv.org/pdf/2603.01952v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "World Modeling & Simulation"
relevance_score: 8.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "World Modeling & Simulation"
  domain: "Social & Behavioral Science"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "LiveCultureBench"
  primary_benchmark: "LiveCultureBench"
---

# LiveCultureBench: a Multi-Agent, Multi-Cultural Benchmark for Large Language Models in Dynamic Social Simulations

## 原始摘要

Large language models (LLMs) are increasingly deployed as autonomous agents, yet evaluations focus primarily on task success rather than cultural appropriateness or evaluator reliability. We introduce LiveCultureBench, a multi-cultural, dynamic benchmark that embeds LLMs as agents in a simulated town and evaluates them on both task completion and adherence to socio-cultural norms. The simulation models a small city as a location graph with synthetic residents having diverse demographic and cultural profiles. Each episode assigns one resident a daily goal while others provide social context. An LLM-based verifier generates structured judgments on norm violations and task progress, which we aggregate into metrics capturing task-norm trade-offs and verifier uncertainty. Using LiveCultureBench across models and cultural profiles, we study (i) cross-cultural robustness of LLM agents, (ii) how they balance effectiveness against norm sensitivity, and (iii) when LLM-as-a-judge evaluation is reliable for automated benchmarking versus when human oversight is needed.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）作为自主智能体进行评估时存在的评估维度单一和可靠性不足的问题。研究背景是，随着LLM越来越多地被部署为自主运行的智能体，现有的评估体系主要聚焦于智能体是否成功完成具体任务（如信息检索、指令遵循），而严重忽视了其在复杂社会互动中行为是否符合特定社会文化规范，以及自动化评估工具（如“LLM即评委”）本身的可靠性。

现有方法的不足在于，它们通常缺乏动态、多文化的社会情境模拟，无法系统性地评估智能体在跨文化环境中的适应性和行为得体性。同时，依赖LLM作为自动评估者（judge）的可靠性尚未得到充分检验，这可能导致评估结果存在偏差或不确定性。

因此，本文要解决的核心问题是：如何构建一个更全面、可靠的基准来评估作为智能体的LLM。具体而言，论文提出了LiveCultureBench这一基准，它通过创建一个模拟多文化小镇的动态社会仿真环境，让具有不同人口统计和文化背景的合成居民（由LLM驱动）进行互动。该基准旨在同时评估LLM智能体的任务完成度和对社会文化规范的遵守情况，并系统研究三个关键方面：LLM智能体的跨文化鲁棒性；它们在任务有效性与规范敏感性之间的权衡能力；以及“LLM即评委”这种自动化评估方法在何种情况下可靠、何时又需要人类监督。

### Q2: 有哪些相关研究？

本文的研究主要涉及多智能体社会模拟、文化感知评估以及大语言模型作为评判者这三个相关领域。

在**多智能体社会模拟与基准测试**方面，相关工作包括Socratic Models、Generative Agents和AgentBench等。这些工作将LLM作为智能体置于模拟环境中，但评估重点通常是任务完成度。LiveCultureBench与这些工作的主要区别在于，它首次系统性地将**文化规范遵从度**作为核心评估维度，并构建了包含多样化人口统计和文化背景的合成居民，以研究智能体在动态社会互动中的跨文化鲁棒性。

在**文化感知与规范评估**方面，现有研究如CultureBank、CulturaX和CValues侧重于从静态数据集或价值观层面对LLM进行文化对齐评估。本文的LiveCultureBench则向前推进了一步，它在一个**动态、交互式的社会模拟**中评估智能体行为是否符合特定文化情境下的社会规范，从而能更真实地研究任务有效性与规范敏感性之间的权衡。

在**LLM作为评判者**方面，相关工作广泛探讨了使用LLM进行自动评估的可行性（LLM-as-a-judge）。本文的贡献在于，它在一个复杂的多智能体文化模拟场景中，系统地研究了这种自动化评估方法的**可靠性边界**，明确了其何时可信、何时需要人工监督，这为未来自动化基准测试的设计提供了重要洞见。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为LiveCultureBench的动态多智能体社会模拟基准测试平台来解决评估LLM智能体文化适应性与任务效能平衡的问题。其核心方法是创建一个模拟小镇，将LLM作为具有不同文化背景的居民智能体嵌入其中，并设计了一套系统的评估框架。

整体框架基于**地点图**构建虚拟城镇环境，其中包含具有多样化人口统计特征和文化背景的合成居民。每个模拟情景中，指定一位居民拥有每日目标，其他居民则提供社会情境。关键创新在于引入了**基于LLM的验证器**，该模块自动生成对智能体行为是否违反社会文化规范以及任务进展的结构化判断。这些判断被聚合成量化指标，用以捕捉任务完成与文化规范遵守之间的权衡关系，并衡量验证器自身判断的不确定性。

主要技术组件包括：1）**多文化智能体模拟引擎**，驱动动态社会互动；2）**结构化评估生成模块**，由LLM验证器输出标准化评判；3）**多维度度量体系**，综合评估任务效能、文化敏感性和验证可靠性。该方法的核心创新点在于首次在动态社会模拟中系统量化了LLM智能体的跨文化鲁棒性，揭示了其在效率与规范敏感性之间的平衡行为，并实证分析了LLM作为自动评估工具的可靠性边界，明确了何时需要引入人工监督。

### Q4: 论文做了哪些实验？

该研究构建了一个名为LiveCultureBench的动态多智能体社会模拟基准测试，用于评估大语言模型作为智能体时的跨文化适应性和任务表现。实验设置上，研究团队模拟了一个小型城市作为位置图，其中包含具有多样化人口统计特征和文化背景的合成居民。每个实验片段会为一位居民设定一个日常目标（如“购买杂货”），其他居民则提供社会背景。核心评估由一个基于LLM的验证器执行，该验证器对智能体的行为是否违反社会文化规范以及任务进度生成结构化判断。

数据集与基准测试方面，LiveCultureBench本身即是一个多文化动态基准。研究使用该基准测试了多个大语言模型（如GPT-4、Claude等）在不同文化背景下的表现。对比方法主要围绕模型自身在不同文化配置下的行为差异，以及任务完成度与文化规范遵守之间的权衡。

主要结果与关键指标包括：1）**跨文化鲁棒性**：研究发现LLM智能体在不同文化背景下的表现存在显著差异，揭示了其文化偏见和适应性不足。2）**任务-规范权衡**：研究通过聚合验证器的判断，生成了量化指标来捕捉模型在“任务有效性”与“规范敏感性”之间的平衡关系。3）**评估器可靠性**：实验分析了“LLM即评委”这一自动化评估方法的可靠性边界，指出了其在某些涉及复杂文化细微差别的情境下不可靠，从而明确了需要人类监督的场景。这些指标共同表明，当前LLM智能体在动态社会模拟中，其行为在文化适宜性方面仍有很大提升空间。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度展开。首先，LiveCultureBench依赖LLM作为评判者，其评估本身可能带有模型自身的文化偏见，这影响了基准的客观性。未来可探索融合人类专家评估与多模型共识机制，以提升评判的可靠性。其次，模拟环境中的“居民”文化背景虽多样，但仍是基于预设的静态标签，未能充分体现文化内部动态演变与个体差异。未来可引入强化学习，让代理在长期互动中自适应调整行为，从而研究文化规范的习得与变迁过程。此外，基准主要关注任务与规范的权衡，但未深入探究代理在复杂冲突情境下的道德推理能力。可设计涉及跨文化伦理困境的进阶场景，以评估模型的深层价值对齐。最后，将此类社会模拟从封闭小镇扩展至开放网络环境，研究代理在信息流冲击下的行为演化，也是一个极具潜力的方向。

### Q6: 总结一下论文的主要内容

这篇论文提出了LiveCultureBench，一个用于评估大语言模型在动态社会模拟中表现的多智能体、多文化基准测试。其核心问题是现有评估主要关注任务成功率，而忽略了文化适宜性和评估者可靠性。该基准模拟了一个小型城市，居民拥有多样化的人口统计和文化背景，通过位置图构建动态社交环境。方法上，每个模拟片段为一位居民设定日常目标，其他居民提供社会背景，并基于LLM的验证器生成对规范违反和任务进展的结构化判断，进而聚合成衡量任务与规范权衡及验证器不确定性的指标。主要结论显示，该基准能有效研究LLM智能体的跨文化鲁棒性、效率与规范敏感性的平衡，以及LLM作为评估者在自动化基准测试中的可靠性边界，指出何时需要人工监督。其意义在于推动了LLM代理评估向更贴近真实社会复杂性的方向发展。
