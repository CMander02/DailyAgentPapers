---
title: "TerraBench: Can Agents Reason Over Heterogeneous Earth-System Data?"
authors:
  - "Dat Tien Nguyen"
  - "Thao Nguyen"
  - "Fadillah Adamsyah Maani"
  - "Huy M. Le"
  - "Muhammad Umer Sheikh"
  - "Numan Saeed"
  - "Muhammad Haris Khan"
  - "Salman Khan"
date: "2026-06-11"
arxiv_id: "2606.13148"
arxiv_url: "https://arxiv.org/abs/2606.13148"
pdf_url: "https://arxiv.org/pdf/2606.13148v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Science Agent"
  - "Tool Use"
  - "Benchmark"
  - "Earth Science"
  - "Multi-modal"
  - "ReAct"
relevance_score: 9.0
---

# TerraBench: Can Agents Reason Over Heterogeneous Earth-System Data?

## 原始摘要

Climate and environmental decision-making increasingly requires reasoning across heterogeneous inputs, including gridded physical data, satellite imagery, geospatial context, and simulator outputs. Weather and climate foundation models can forecast well, but do not reason interactively in language, while large language models (LLMs) reason in language but cannot operate directly on high-dimensional Earth-system data. As a result, real scientific workflows in Earth-science remain underserved. We introduce TerraBench, a benchmark for grounded Earth-science reasoning, built on TerraAgent, a ReAct-style executable framework that interleaves reasoning, tool calls, and observations to couple LLM planning with scientific tools for environmental retrieval, geospatial processing, simulation, and artifact-backed computation. TerraBench unifies analysis of Earth observation imagery, gridded data, GIS reasoning and simulation in a single executable interface, whereas prior benchmarks isolate these capabilities into narrow individual tasks. It is also the first in this space to pair process-level tool-use metrics with tolerance-aware numeric scoring. The benchmark comprises 403 extensive agentic tasks across three tracks (Fundamentals, Simulator-Grounded, and Document-Grounded Verification) and eight application domains with 24,500 verified execution steps. These results indicate that reliable Earth-science agents must go beyond tool access to coordinate heterogeneous workflows, parameterize tools precisely, and preserve artifact provenance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前地球科学人工智能领域中一个关键缺失：缺乏能够统一推理异构地球系统数据的通用基准和可执行框架。现有方法存在明显不足：天气预报和气候基础模型虽能进行高精度数值预测，但无法以语言交互形式进行复杂推理；而大语言模型虽然具备语言推理能力，却无法直接处理高维地球系统数据，如卫星图像、网格化物理数据、地理空间上下文和模拟器输出。此外，现有的地理空间和地球观测基准（如OpenEarthAgent、ThinkGeo）大多将任务割裂为独立的、窄领域的子任务，无法评估智能体在统一工作流中联合推理多种异构信息源的能力，也缺乏对过程级工具使用和数值容忍度的精细评估。因此，该论文的核心问题是：如何构建一个可执行的基准，以系统评估大语言模型智能体在真实地球科学工作流中，协同规划、调用多领域科学工具（如气候数据检索、地理信息系统操作、模拟器运行及文档验证），并生成可追溯、容错的数值结果的能力。通过TerraBench，作者首次在单一可执行接口下统一了多种异构数据与任务类型，并提出了将过程与结果解耦的评估协议。

### Q2: 有哪些相关研究？

相关研究可分为两类。**多模态智能体基准**方面，ReAct开创了推理-行动-观察范式，后续有HuggingGPT、Visual ChatGPT、MM-ReAct等扩展了工具增强推理；基准工作如ToolBench、API-Bank、VisualWebArena、GAIA等关注工具调用与长程执行。这些工作与TerraBench的评估理念一致，但未针对气候领域的地球观测图像、网格化环境数据、GIS推理与模拟的组合。**地球科学智能体基准**方面，Terra、WeatherQA、UnivEARTH等聚焦气象或遥感推理，AutoClimDS、Zephyrus连接气候数据集与模拟器，ThinkGeo、GeoBenchX展示地理空间工具使用。它们通常专业化于单一能力，而TerraBench首次统一了地球观测图像、网格化环境数据、GIS推理、模拟及文档验证，并引入过程级工具使用指标与容差数值评分，而非仅依赖最终答案评估。

### Q3: 论文如何解决这个问题？

该论文通过提出TerraBench基准和TerraAgent框架来解决地球系统科学中的异构数据推理问题。核心方法是将大语言模型的语言规划能力与专业科学工具的执行能力分离，构建一个可执行、可审计的工作流框架。

TerraAgent整体架构围绕一个按领域组织的工具注册表设计，涵盖再分析/环境数据检索、卫星遥感处理、GIS/OpenStreetMap分析、天气预报（如Pangu-Weather、Aurora）、确定性模拟（如AquaCrop作物模型、DSSAT作物系统、CLIMADA灾害评估、EnergyPlus建筑能耗分析、SUMO交通模拟）等77个子工具。主要创新点包括：（1）采用ReAct风格的规划-执行循环，模型负责协调工作流，而定量输出必须来自工具调用而非语言模型直接生成；（2）设计分层推理体系，将Pearl因果层级（关联、干预、反事实）与观测基础层（Level 0）结合，确保智能体先掌握时空坐标解析、异构数据网格对齐等预备能力；（3）引入双轨评估机制——过程层面用ToolUseScore（结合指令有效性、工具选择、参数正确性等6项指标）衡量推理质量，答案层面用NumScore（基于容差感知的指数衰减评分）对数值输出提供部分信用。该基准包含403个多步骤任务，覆盖8个应用领域，并通过人工验证确保科学工作流的完整性和可审计性。

### Q4: 论文做了哪些实验？

论文在TerraBench上进行了全面的实验。该基准测试包含403个智能体任务，分为基础、模拟器验证和文档验证三个轨道，涉及八个应用领域，共24,500个验证步骤。实验对比了多种前沿模型（如GPT-5.4、GPT-5.5、Gemini 3.1 Pro Preview、Claude Haiku 4.5、Claude Sonnet 4.6）、基线智能体（Qwen3.5-9B）和开源模型（如Qwen3系列、Gemma 4、Mistral 7B、Llama 3.1、InternVL3等）。

主要结果通过工具使用指标（ToolAcc、CategoryF1、ArgAcc、OrderScore、ToolUseScore）和答案分数（NumScore、Hit@tol）评估。最强模型Claude Sonnet 4.6仅达到59.22 ToolUseScore、28.44 NumScore和22.88 Hit@tol，表明任务极具挑战性。研究发现，工具使用流程质量普遍高于最终答案质量（如Qwen3.5-9B的ToolUseScore为31.18，但NumScore仅1.30）。主要失败模式包括数值超出容差（84.6%-99.3%）和错误参数值（69.5%-96.8%）。强模型工具使用更广泛，而弱模型倾向于使用有限的工具子集，模拟和可视化工具使用率极低。

### Q5: 有什么可以进一步探索的点？

根据论文结论部分的局限性讨论，未来研究可从以下方向推进：一是改进基准测试的**扩展性与自动化**，当前严格的人工审核和确定性验证导致构建成本高，可探索半自动化流水线，如利用合成数据生成或弱监督学习来扩展任务规模，同时需保证专家引导的科学性。二是**数值容错机制**的细化，当前基于确定性工作流的严格验证可能限制对模型近似推理能力的评估，未来可设计更灵活的分级容错评分，区分工具调用精度与最终答案正确性的权重。三是**多模态协同的鲁棒性**，所有模型在工具调用与答案正确性间存在显著差距，可尝试引入自适应策略，如根据任务复杂度动态调整规划步数或参数化精度。此外，论文未讨论模型对物理因果关系的理解，可结合知识图谱或物理约束层强化推理的可解释性。

### Q6: 总结一下论文的主要内容

这篇论文提出了TerraBench基准和TerraAgent框架，用于解决地球科学领域需要跨异构数据源（如网格化物理数据、卫星图像、地理空间信息和模拟器输出）进行推理的问题。核心贡献在于：首次在统一的可执行接口下整合了地球观测图像、网格环境数据、GIS推理、确定性模拟和文档验证等任务，并通过403个复杂任务（约24,500个执行步骤）和77个子工具进行评估。方法上，TerraAgent采用ReAct风格，交替进行推理、工具调用和观察，生成可审计的推理链和构件（如NetCDF、GeoTIFF）。主要结论是，尽管前沿模型（如Claude Sonnet 4.6）在工具使用得分（59.2）上优于开源模型，但在最终数值正确性（命中容忍度22.9）上存在显著差距，表明可靠的地球科学智能体不仅需要工具访问，还需协调异构工作流、精确参数化工具并保留构件来源。该工作为开发科学严谨的LLM智能体提供了可复现的测试平台。
