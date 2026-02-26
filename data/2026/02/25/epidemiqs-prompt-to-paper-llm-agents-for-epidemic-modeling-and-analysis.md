---
title: "EpidemIQs: Prompt-to-Paper LLM Agents for Epidemic Modeling and Analysis"
authors:
  - "Mohammad Hossein Samaei"
  - "Faryad Darabi Sahneh"
  - "Lee W. Cohnstaedt"
  - "Caterina Scoglio"
date: "2025-09-24"
arxiv_id: "2510.00024"
arxiv_url: "https://arxiv.org/abs/2510.00024"
pdf_url: "https://arxiv.org/pdf/2510.00024v2"
categories:
  - "cs.SI"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "Agent 架构"
  - "Agent 规划与推理"
  - "LLM 应用于 Agent 场景"
  - "Agent 工具使用"
  - "Agent 评测/基准"
  - "Agent 自动化研究"
relevance_score: 8.5
---

# EpidemIQs: Prompt-to-Paper LLM Agents for Epidemic Modeling and Analysis

## 原始摘要

Large Language Models (LLMs) offer new opportunities to accelerate complex interdisciplinary research domains. Epidemic modeling, characterized by its complexity and reliance on network science, dynamical systems, epidemiology, and stochastic simulations, represents a prime candidate for leveraging LLM-driven automation. We introduce EpidemIQs, a novel multi-agent LLM framework that integrates user inputs and autonomously conducts literature review, analytical derivation, network modeling, mechanistic modeling, stochastic simulations, data visualization and analysis, and finally documentation of findings in a structured manuscript, through five predefined research phases. We introduce two types of agents: a scientist agent for planning, coordination, reflection, and generation of final results, and a task-expert agent to focus exclusively on one specific duty serving as a tool to the scientist agent. The framework consistently generated complete reports in scientific article format. Specifically, using GPT 4.1 and GPT 4.1 Mini as backbone LLMs for scientist and task-expert agents, respectively, the autonomous process completes with average total token usage 870K at a cost of about $1.57 per study, successfully executing all phases and final report. We evaluate EpidemIQs across several different epidemic scenarios, measuring computational cost, workflow reliability, task success rate, and LLM-as-Judge and human expert reviews to estimate the overall quality and technical correctness of the generated results. Through our experiments, the framework consistently addresses evaluation scenarios with an average task success rate of 79%. We compare EpidemIQs to an iterative single-agent LLM, benefiting from the same system prompts and tools, iteratively planning, invoking tools, and revising outputs until task completion. The comparisons suggest a consistently higher performance of EpidemIQs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决利用大型语言模型（LLM）自动化复杂、跨学科的流行病学建模研究的问题。研究背景是，尽管LLM在科学和工程领域展现出巨大潜力，但其在真实世界复杂任务中仍存在局限，这催生了能够使用外部工具、进行思维链推理和自我迭代改进的LLM智能体。然而，现有方法在流行病学这一高度复杂的领域尚未得到充分应用。流行病建模，特别是基于网络的方法，需要综合随机过程理论、网络科学、流行病学和计算模拟等多学科专业知识，组建和协调具备如此多样性的研究团队非常困难。

现有方法的不足在于，它们未能有效应对这种深度跨学科研究的自动化挑战。尽管已出现多智能体系统来模拟跨学科研究环境，但专门针对网络流行病建模的、端到端的自动化研究框架仍然缺失。

因此，本文要解决的核心问题是：如何设计一个能够以最小人力干预、自主执行从问题理解到最终成稿全流程的LLM多智能体框架，以加速网络流行病学建模与分析。论文提出的EpidemIQs框架，通过科学家智能体与任务专家智能体的协作，将整个研究过程划分为文献综述、分析推导、网络建模、机制建模、随机模拟、数据可视化分析及结构化文档撰写五个阶段，从而自动化地完成这项复杂的跨学科研究任务。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和特定领域类。

**方法类**：早期研究如Automated Mathematician和DENDRAL，旨在通过启发式规则自动化科学研究。近期，基于自回归大语言模型（LLMs）的智能体（Agents）通过集成外部工具使用、思维链提示和迭代自我改进等能力得以发展，为复杂任务自动化提供了基础。本文提出的EpidemIQs框架属于多智能体LLM系统，与单智能体迭代方法（如文中作为基线对比的迭代单智能体）形成对比，其创新在于通过科学家代理和任务专家代理的分工协作，实现了更高的任务成功率和端到端工作流可靠性。

**应用类**：LLM智能体已在软件工程、网络安全、医学诊断、化学、材料科学、计算生物学等多个领域得到应用。多智能体系统如Agent Laboratory、Virtual Lab、ChemCrow、ResearchAgent和The AI Scientist等，模拟了跨学科的人类研究环境。本文工作与这些研究一脉相承，但将应用焦点专门对准了尚未被充分开发的、高度复杂的**流行病学建模领域**。

**特定领域（流行病学）类**：传统的网络流行病建模研究依赖于网络科学、动力系统、流行病学和随机模拟等多学科专业知识，通常需要跨学科团队合作。本文的EpidemIQs框架旨在自动化这一复杂流程，其与现有流行病学研究的区别不在于提出新的流行病学模型，而在于**首次构建了一个能自主执行从文献回顾、分析推导、网络建模、机制建模、随机模拟、数据可视化到最终生成结构化论文的全流程多智能体系统**。这弥补了现有LLM智能体在高度跨学科的流行病学领域应用不足的缺口。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为EpidemIQs的多智能体LLM框架来解决复杂流行病建模与分析任务的自动化问题。其核心方法是模拟一个完整的流行病学研究实验室，将整个工作流程分解为五个预定义的研究阶段：发现、建模、仿真、分析和报告撰写，并通过分层架构和专门化的智能体协作来执行。

整体框架基于四层功能架构构建：1）**多智能体编排层**：负责任务分配与智能体间的同步协作；2）**骨干LLM层**：作为核心推理引擎，分析证据、形成假设并规划行动序列；3）**感知层**：将多样化输入（如文献、网络数据）转化为统一的语义表示；4）**行动层**：自主调用并执行各类工具（如随机仿真器、RAG、API）。

框架的核心创新在于设计了两种智能体类型：**科学家智能体**和**任务专家智能体**。科学家智能体作为中央协调者，包含三个关键模块：**规划模块**（自由解析和分解用户查询为子任务计划）、**ReAct模块**（基于当前计划进行推理和工具调用）和**反思模块**（评估中间输出的错误与逻辑一致性，生成结构化JSON反馈以迭代改进）。它通过ReAct-反思循环迭代执行，直至满足条件。任务专家智能体则作为科学家智能体的专用工具，每个专注于一个原子任务（如文献检索、数学推导、网络建模），确保执行效率和质量。

在五个研究阶段中，各有专门的智能体团队协作。例如，在发现阶段，由发现科学家协调在线检索专家、文献检索专家和数学专家，通过多跳问答范式收集和精炼数据；在建模阶段，网络科学家、模型科学家和参数科学家分别负责构建接触网络、定义机制模型和计算参数；仿真阶段使用FastGEMF进行随机仿真并由视觉专家验证；分析阶段由数据科学家协调团队计算指标并解读可视化结果；最终报告阶段通过专家智能体自动生成结构化学术手稿。

关键技术包括：1）**结构化输出约束**：强制每个团队输出预定义结构（如JSON模式），以确保数据传递的可靠性和自动验证；2）**双模式运行**：支持全自动和协同（人类在环）两种模式，增强灵活性；3）**记忆机制**：科学家智能体具备短期记忆（存储当前对话和交互）和长期记忆（存储历史对话数据库），支持基于上下文的检索；4）**多模态集成**：通过视觉语言模型处理视觉数据，并结合API实现自主数据获取。该框架通过模块化分解、结构化协调和迭代反思，显著提升了处理复杂跨学科任务的自动化能力与可靠性。

### Q4: 论文做了哪些实验？

论文设计了全面的实验来评估EpidemIQs框架。实验设置方面，使用GPT-4.1作为科学家智能体骨干模型，GPT-4.1 Mini作为任务专家智能体骨干模型，并配置了重试机制和工具超时等参数。

数据集与基准测试方面，实验采用了五个复杂度递增的流行病学问题作为评估场景，覆盖网络拓扑、时间结构、多层网络、竞争病原体和网络感知干预等关键方面。其中前两个问题用于框架设计测试，后三个为未知挑战。此外，还使用了DSBench数据科学基准进行消融研究。

对比方法上，论文构建了一个强大的迭代式单智能体基线，该基线使用相同的系统提示、工具集（包括视觉专家工具）和结构指导，并采用GPT-4.1和o3两种大上下文LLM。为避免角色混淆，移除了多智能体特定的角色指定，并实施了记忆强化机制。

主要结果如下：
- **工作流完成率**：EpidemIQs在100次试验中达到100%，单智能体基线（GPT-4.1和o3）分别为78%和80%。
- **任务成功率**：EpidemIQs整体平均为79%。具体到五个问题：问题1和2约90%，问题3为65%，问题4为75%，问题5为80%。单智能体基线的任务成功率显著较低（GPT-4.1为22%，o3为26%），尤其在复杂问题上表现不佳。
- **质量评估**：LLM-as-Judge（GPT-4o）为EpidemIQs生成结果的平均评分为9.04/10；人类专家（四位博士生和一位教师）平均评分为7.98/10。单智能体基线的人类评分显著较低（GPT-4.1为5.06，o3为5.68）。
- **计算成本与效率**：EpidemIQs平均每次研究总token使用量为870K，成本约1.57美元，总耗时约1190秒（低于30分钟）。估计等效人工工作量约为38.4小时。
- **消融研究**：在DSBench上，完整的科学家智能体架构（包含规划、ReAct工具使用和5步反思）达到51.71%的准确率，相比纯LLM设置（29.76%）提升了73%，证实了各模块的有效性。

### Q5: 有什么可以进一步探索的点？

该论文的框架在自动化流行病建模方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其任务成功率（平均79%）表明在复杂场景（如时序网络分析）中表现仍有不足，这主要受限于预定义工具集与任务需求的匹配度。未来可探索更灵活的工具调用机制，使智能体能动态扩展或组合工具以应对未预见的挑战。

其次，评估主要依赖LLM-as-Judge和有限的人工评审，可能存在偏差。未来需建立更严谨的跨学科评估基准，结合领域专家的深度评审，并量化生成结果的科学可靠性（如模型假设的合理性、仿真结果的统计显著性）。

从技术角度看，当前多智能体架构依赖固定角色划分（科学家与任务专家），未来可研究自适应协作机制，让智能体根据任务复杂度动态调整职责。此外，生成报告存在冗长和术语非常规的问题，可引入强化学习优化写作风格，使其更符合学术规范。

最后，该框架尚未充分利用实时数据（如最新疫情数据）或与专业仿真平台（如EpiModel）深度集成。未来可探索混合智能系统，将LLM的推理能力与领域专用计算引擎结合，提升复杂机制建模的精度与效率。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为EpidemIQs的多智能体大语言模型框架，旨在自动化流行病建模与分析这一复杂跨学科研究过程。其核心问题是利用LLM加速需要整合文献综述、网络科学、动力学系统与随机模拟等多个环节的流行病学研究。

方法上，框架设计了两种智能体：负责整体规划、协调与最终成果生成的“科学家”智能体，以及专注于特定任务（如文献检索、模型推导、可视化等）的“任务专家”智能体。它们协作完成从用户输入到结构化科研论文生成的五个预定义研究阶段。

主要结论表明，该框架能稳定生成完整科学报告，平均每项研究消耗约87万token，成本约1.57美元，任务平均成功率达79%。与使用相同提示和工具的迭代式单智能体方法相比，EpidemIQs表现出更优性能。其意义在于为复杂科学工作流提供了高效、低成本的自动化范例，展示了多智能体LLM在推动跨学科研究自动化方面的潜力。
