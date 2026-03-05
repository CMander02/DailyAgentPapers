---
title: "WebDS: An End-to-End Benchmark for Web-based Data Science"
authors:
  - "Ethan Hsu"
  - "Hong Meng Yam"
  - "Ines Bouissou"
  - "Aaron Murali John"
  - "Raj Thota"
  - "Josh Koe"
  - "Vivek Sarath Putta"
  - "G K Dharesan"
  - "Alexander Spangher"
  - "Shikhar Murty"
  - "Tenghao Huang"
  - "Christopher D. Manning"
date: "2025-08-02"
arxiv_id: "2508.01222"
arxiv_url: "https://arxiv.org/abs/2508.01222"
pdf_url: "https://arxiv.org/pdf/2508.01222v2"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Tool Use"
  - "Web Interaction"
  - "Data Science"
  - "Multi-step Reasoning"
  - "Agent Evaluation"
relevance_score: 8.0
---

# WebDS: An End-to-End Benchmark for Web-based Data Science

## 原始摘要

Many real-world data science tasks involve complex web-based interactions: finding appropriate data available on the internet, synthesizing multimodal data from different locations, and producing summarized analyses. Existing web benchmarks often focus on simplistic interactions and often do not require diverse tool-using capabilities. Conversely, traditional data science benchmarks typically concentrate on static, highly structured datasets and do not assess end-to-end workflows that encompass data acquisition, cleaning, analysis, and insight generation. In response, we introduce WebDS, the first end-to-end web-based data science benchmark. It comprises 870 web-based data science tasks across 29 diverse websites from structured government data portals to unstructured news media, challenging agents to perform complex, multi-step, tool-based operations, across heterogeneous data formats, to better reflect the realities of modern data analytics. Evaluations of current SOTA LLM agents indicate significant performance gaps in accomplishing these tasks. For instance, Browser Use, which accomplishes $80\%$ of tasks on WebVoyager, completes only 15% of tasks in WebDS, which our analysis suggests is due to new failure modes, such as poor information grounding, repetitive behavior and shortcut-taking that agents performing WebDS's tasks display. By contrast, humans achieve around 90% accuracy, highlighting a substantial gap between current agents and human performance. By providing a more robust and realistic testing ground, WebDS sets the stage for significant advances in the development of practically useful LLM-based data science.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI智能体（LLM Agents）在真实世界数据科学任务中表现不足的问题，尤其是在需要结合网络浏览、多源异构数据获取与综合分析的端到端工作流方面。

研究背景是，尽管具备网络浏览和工具使用能力的大语言模型智能体在利用网络知识方面展现出潜力，但真实的数据科学任务通常始于在复杂动态的网页上寻找数据，并需要跨多个站点整合多模态信息以产生分析见解。然而，现有的评估基准存在明显局限：一方面，现有的网络智能体基准（如WebVoyager、WebArena）主要关注遵循指令完成简单的网页操作（如发帖、购物），并未评估其数据理解和处理能力，且常因使用实时网站而影响可复现性；另一方面，传统的数据科学基准则侧重于在静态、结构化数据集（如代码环境、电子表格）上进行数据操作或查询，完全忽略了从网络获取数据这一关键初始环节。这导致现有方法无法全面评估智能体在“从网络获取数据到生成分析洞察”这一完整、现实流程中的能力。

因此，本文的核心问题是：缺乏一个能够真实、全面评估智能体执行端到端、基于网络的数据科学工作流能力的基准。为此，作者提出了WebDS基准，它包含870个跨29个多样化网站的真实任务，要求智能体执行复杂的多步骤、工具化操作，以完成从数据发现、清洗、分析到报告生成的全流程，从而填补现有评估体系的空白，并为开发真正实用的、基于LLM的数据科学智能体设定新的挑战和目标。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为数据科学分析基准和网络智能体基准两大类。

在数据科学分析基准方面，已有SQuAD、HotpotQA等评估语言模型对结构化数据推理能力的基准，以及InfiAgent-DABench、DSBench、DA-Code、Spider 2.0等专门针对数据科学工作流（如代码生成、文本转SQL）的评测集。然而，这些基准大多聚焦于静态、结构化的数据集（如CSV文件），未能评估包含数据发现、获取、清洗和分析在内的端到端现实工作流，特别是缺乏对网络交互和工具使用能力的考察。

在网络智能体基准方面，相关工作包括VirtualHome、Mind2Web等早期基于动作序列表面形式对比的评估，以及更注重功能正确性评估的WebArena。近期，WebVoyager等研究利用大模型进行评估，但在复杂任务中仍主要依赖最终截图进行二元成败判定，缺乏对完整任务轨迹的细粒度分析。

本文提出的WebDS基准与上述工作的核心区别在于，它首次将端到端数据科学工作流与真实的、基于网络的交互环境相结合。WebDS要求智能体在29个多样化的真实网站（从结构化数据门户到非结构化新闻媒体）上执行多步骤、多工具操作，处理异构数据格式，从而更全面地反映现代数据分析的现实挑战。与现有基准相比，WebDS不仅评估最终结果，还对完整任务轨迹进行细粒度分析，以识别智能体在信息定位、重复行为、走捷径等方面的新失败模式。

### Q3: 论文如何解决这个问题？

论文通过设计并构建一个名为WebDS的端到端基准测试来解决现有基准在评估基于网络的数据科学任务上的不足。其核心方法是创建一个全面、可复现且细粒度的测试环境，以模拟真实世界数据科学工作流的复杂性。

整体框架围绕一个包含870个任务的基准测试集展开，这些任务覆盖了29个来自10个高风险领域（如政府数据、新闻媒体）的网站。架构设计的关键在于其任务定义源于对领域专家（如记者、数据科学家）的访谈，从而确保任务反映真实需求。任务被分为两大类：一类最终产生下游产品（如报告），另一类旨在回答关键分析问题。这些任务涉及多种数据模态（结构化表格、非结构化文本与图形）、多跳推理、多网站数据整合以及复杂的工具使用。

主要模块/组件包括：1）**任务与领域选择**：精心挑选的网站需满足公开、包含常用数据且具有独特数据表征等标准，以确保任务的多样性和挑战性。2）**动作空间**：不固定动作集合，允许灵活集成现有抽象（如BrowserGym），支持研究者启用或禁用各种工具（Python、Bash、SQL等），降低了适配摩擦。3）**状态与观察空间**：状态由网页页面和可访问数据构成，观察则包括HTML、DOM、截图或AXTrees。任务从固定入口URL开始，智能体需自主导航发现相关页面并下载、操作数据。4）**可复现性与真实性**：通过双轨制评估实现——WebDS-live让智能体与实时网站交互，捕捉真实环境的动态复杂性；WebDS-dockerized则通过容器化部署冻结网站内容，确保实验的确定性和精确复现。5）**评估粒度**：创新性地沿三个维度提供细粒度评估：按专业领域（如人口统计、体育）、按任务属性（如多跳、基于动作）以及按任务难度（简单、中等、困难）。6）**发布策略与完整性**：为防止过拟合，公开发布470个任务的验证集，并保留400个任务的私有测试集。排行榜使用私有测试集的轮换子集进行评估，通过Huggingface平台接收预测进行评分，并可能定期更新测试池。

创新点主要体现在：首次构建了专注于完整数据科学工作流（从数据获取、清洗到分析与洞察生成）的网络基准；通过双轨评估机制平衡了真实性与科学严谨性；以及引入了多维度的细粒度评估体系，能够更精准地诊断智能体在不同挑战类型上的性能差距。

### Q4: 论文做了哪些实验？

论文的实验设置包括自动化和主观评估相结合的综合评估框架。自动化评估针对有参考真实值的任务（如提取统计数据），通过语言模型比较智能体输出与真实值，给出“成功/失败”的二元标签。主观评估则基于LLM-as-a-Judge范式，对开放式任务（如生成包含统计数据的Reddit帖子）进行1-5分的评分，并扩展了方法：提供更细粒度的分数及理由，且基于完整轨迹（观察-行动-下一观察三元组）而非仅最终状态进行评估。评估工具的稳定性经过验证，五次运行的平均LLM评分标准差仅为0.005，状态一致性和分数一致性分别达96.3%和91.3%。

数据集/基准测试为WebDS，包含来自29个多样化网站（如政府数据门户、新闻媒体）的870项基于网络的数据科学任务，涵盖端到端工作流程（数据获取、清洗、分析、洞察生成）。

对比方法包括九种最先进的网络智能体：通用模型GPT-4o、GPT-4o-mini、Claude Sonnet-3.5、Claude Haiku-3.5、Qwen2.5-72B-Instruct、Claude Sonnet-4.5、GPT-5.1（均使用可访问性树作为观察空间）；多模态模型Qwen2.5-VL-72B-Instruct（使用全页面截图）；开源智能体AgentOccam（WebArena的SOTA）；以及BrowserUse（WebVoyager的SOTA，通过Qwen2.5-VL-72B-Instruct和GPT-4o评估）。同时，招募了六名有数据科学经验的人类参与者作为对比，在相同环境下完成任务。

主要结果显示，当前智能体性能存在显著差距。例如，BrowserUse在WebVoyager上能完成80%的任务，但在WebDS上仅完成15%，分析表明这是由于智能体在新任务中表现出信息基础不牢、重复行为和走捷径等失败模式。相比之下，人类参与者的准确率约为90%，凸显了智能体与人类性能之间的巨大差距。关键数据指标包括：人类验证显示评估工具与人工评估的状态一致性达93%；智能体评估中，BrowserUse在WebDS的成功率仅15%，而人类达90%。

### Q5: 有什么可以进一步探索的点？

本文提出的WebDS基准测试虽然全面，但仍有局限。其任务主要基于公开网站，可能无法完全模拟企业内部或需要登录、付费访问的复杂数据环境，且对实时数据流和API动态调用的覆盖有限。未来研究可探索几个方向：一是开发能处理更动态、权限受限数据源的智能体，增强其身份验证与合规操作能力；二是设计更细粒度的评估指标，不仅看任务完成率，还需评估数据质量、分析逻辑的严谨性及可解释性；三是研究如何减少智能体的“捷径行为”与重复操作，通过改进规划机制或引入强化学习来提升其信息溯源与多步骤推理的鲁棒性。此外，可考虑将领域知识更深度融入智能体，使其能进行更专业的判断与数据融合，从而向实用化迈进。

### Q6: 总结一下论文的主要内容

该论文提出了WebDS，首个端到端的基于网络的数据科学基准测试，旨在解决现有基准在模拟真实数据科学工作流程方面的不足。现有网络基准通常交互简单且工具使用能力单一，而传统数据科学基准则多关注静态结构化数据集，缺乏对从数据获取、清洗、分析到见解生成的全流程评估。WebDS包含来自29个多样化网站（如政府数据门户和新闻媒体）的870个任务，要求智能体执行跨异构数据格式的复杂多步骤工具操作，以更真实地反映现代数据分析的实际挑战。评估显示，当前最先进的LLM智能体在此基准上表现显著不足，例如Browser Use模型在WebVoyager上能完成80%的任务，但在WebDS上仅完成15%，主要失败原因包括信息基础不牢、行为重复和走捷径等新问题模式。相比之下，人类准确率可达90%，突显了当前智能体与人类能力间的巨大差距。WebDS通过提供一个更稳健和真实的测试环境，为开发具有实际应用价值的基于LLM的数据科学智能体奠定了重要基础。
