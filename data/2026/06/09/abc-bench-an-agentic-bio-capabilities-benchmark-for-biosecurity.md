---
title: "ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity"
authors:
  - "Andrew Bo Liu"
  - "Samira Nedungadi"
  - "Bryce Cai"
  - "Alex Kleinman"
  - "Harmon Bhasin"
  - "Seth Donoughe"
date: "2026-06-09"
arxiv_id: "2606.11150"
arxiv_url: "https://arxiv.org/abs/2606.11150"
pdf_url: "https://arxiv.org/pdf/2606.11150v1"
categories:
  - "cs.AI"
  - "cs.CY"
tags:
  - "LLM Agent"
  - "Bio-Capabilities"
  - "Biosecurity"
  - "Benchmark"
  - "Multi-agent"
  - "Dual-use"
  - "Wet-lab Validation"
relevance_score: 9.5
---

# ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity

## 原始摘要

Large language models (LLMs) are rapidly acquiring capabilities relevant to biological research, from literature synthesis to interpretation of experimental data. Increasingly, LLM agents can also perform in silico biology tasks that previously required experienced human biologists. These emerging AI capabilities offer new opportunities for scientific discovery and biomedical advances, but they also shift the landscape of biosecurity risks. To address this, we introduce the Agentic Bio-Capabilities Benchmark (ABC-Bench), a suite of tasks to measure agentic biosecurity-relevant capabilities. ABC-Bench evaluates LLM agents on both benign and dual-use biology tasks: writing code to operate liquid handling robots, designing DNA fragments for in vitro assembly, and evading DNA synthesis screening. These tasks require a combination of biology and software expertise. All tested LLM agents outperformed the median expert human baseliner on all three tasks. Agents performed highly on tasks drawing on published knowledge and well-documented protocols, and more weakly on a task requiring novel bioinformatics reasoning. In three wet-lab validation experiments, we found that OpenAI's o4-mini-high produced scripts that, when run on an OpenTrons liquid handling robot, successfully assembled DNA with expected sequences.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI生物安全评估中缺乏衡量智能体（Agent）实际动手操作能力的基准问题。研究背景是，大语言模型及其智能体正快速获得文献综合、实验数据解读等生物研究能力，甚至能完成以往需人类专家操作的计算机模拟生物学任务，这为生物医学带来机遇，但也增加了生物安全双重用途风险。现有方法的不足在于：许多广泛使用的生物基准仅通过简答或选择题测试知识，无法衡量智能体利用软件工具和实验环境执行端到端复杂任务的能力，特别是那些涉及实际操作、编程和生物安全设计的关键任务。因此，本文要解决的核心问题是：构建一个能系统评估AI智能体在具体分子生物学、实验室自动化及生物安全相关任务上表现（包括潜在滥用能力）的基准测试套件，以填补现有评估空白，为生物安全防护措施的部署和模型能力风险预警提供依据。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要将相关工作分为两类：非生物领域的智能体基准和生物领域的智能体基准。非生物领域方面，SWE-Bench是评估编码代理修复真实世界bug的典型基准，已在网络安全和AI开发等领域得到应用，本文借鉴其智能体评估思路，但面向生物安全场景。生物领域方面，LAB-Bench评估分子生物学中的图表解读和实验故障排除；DiscoveryBench和CORE-bench分别侧重生态学和医学科学的数据分析能力；BioCoder和ScienceAgentBench评估LLM及智能体编写生物数据软件的能力；BixBench评估智能体回答生物信息学分析问题的能力；GeneBreaker通过LLM诱导DNA基础模型产生类病原序列。本文（ABC-Bench）与这些工作的关键区别在于：它聚焦于直接参与生物实体工程和操作的任务（如操作液体处理机器人、设计DNA片段、逃避合成筛选），不仅分析生物数据，更能生成生物数据（如分子克隆）。这填补了现有基准在评估LLM智能体实际操纵生物系统能力方面的空白，特别强调了智能体能力带来的生物安全新风险。

### Q3: 论文如何解决这个问题？

论文通过构建ABC-Bench基准框架来解决如何评估LLM智能体在生物安全领域风险能力的问题。整体框架包含三大核心任务：片段设计、筛选规避和液体处理机器人，每个任务对应获取危险DNA序列路径中的一个关键步骤。片段设计任务要求智能体设计用于Gibson组装法的DNA短片段，评估其对公开合成生物学知识的掌握；筛选规避任务则测试智能体隐蔽序列、规避核酸合成筛查的创造性推理能力，这是唯一没有现成文献协议的任务；液体处理机器人任务要求智能体编写开源OpenTrons OT-2液体处理机器人的控制脚本，通过GPT-o4-mini-high模型在真实湿实验中成功完成了DNA组装验证。

主要创新点体现在四个方面：一是提出了七项设计原则确保基准的严谨性，包括测量双重用途能力、将AI作为智能体测试、集体评估多样化能力、评估风险链、客观可重复评分、支持高通量评估和包含精准人类基线。二是引入专家人类基线（具备博士学位和多年经验的生物学家），发现所有测试模型均超过中位人类基线水平。三是拒绝校正机制，通过实验设计揭示前沿模型对双重用途任务的敏感性差异。四是架构上采用Inspect AI框架统一评估，支持10次独立运行和部分记分标准。

关键技术包括：算法化检查智能体产出物而非人工评分、针对Gibson组装等标准协议的直接应用评估、通过约3小时的真实湿实验验证模型生成脚本的实际可靠性，以及通过10次重复运行和95% BCa引导置信区间保证统计显著性。实验结果显示模型在公开知识依赖型任务（如片段设计满分）上表现优异，但在无先例的创新任务（筛选规避）上显著薄弱，揭示了当前LLM在生物安全领域的优势与局限性。

### Q4: 论文做了哪些实验？

ABC-Bench在三个生物安全相关的智能体任务上进行了评估：液体处理机器人编程、DNA片段设计和DNA合成筛查规避。实验使用了10个主流LLM智能体（包括Claude Sonnet 4/4.6、Claude Opus 4/4.6、Gemini 3.1 Pro Preview、GPT-5.4、Qwen3.5和Kimi K2.5）作为对比方法，以具有分子生物学和Python经验的博士级人类专家为基线（各任务参与人数9-13人）。主要结果：所有测试模型均超越人类基线中位数。在液体处理机器人任务中，Claude Sonnet 4.6和Gemini 3.1 Pro Preview获得满分（1.00±0.00）；在DNA片段设计任务中，Claude Opus 4.6获得满分（1.00±0.00）；三个模型的专家百分位达100%。模型在筛查规避任务上表现最弱，Gemini仅0.78±0.02，而Claude Opus 4.6和GPT-5.4拒绝所有样本。人类基线平均分分别为0.33、0.22和0.20。此外，研究还进行了湿实验证：使用GPT-o4-mini-high控制OpenTrons Flex液体处理机器人进行3次Gibson组装实验，所有结果均通过全质粒测序确认成功。

### Q5: 有什么可以进一步探索的点？

论文指出ABC-Bench当前覆盖范围有限，任务高度依赖编码能力，未来需扩展至非编码环节，例如评估模型识别和利用DNA合成筛查治理漏洞的能力。人类基线表现也因任务编码导向而可能被低估，未来应允许专家使用自己熟悉的工具（如NEBuilder）而非强求Python编程。此外，需更精细定义“专家”群体，比较不同背景（如仅有湿实验经验而无编程技能）的专家表现。从我看来，一个关键改进方向是引入更具认知挑战性的任务，例如要求Agent在信息不完全或动态变化的生物场景下自主规划实验并处理意外结果，这更能体现真正`智能`或`推理`能力。同时，需要加强开放权重模型的双重用途能力管控，如将筛查规避能力完全屏蔽，其他能力分级授权，并通过KYC机制确保安全。未来还应探索非代码的评估维度，如多模态数据分析和长文档推理。

### Q6: 总结一下论文的主要内容

ABC-Bench提出了一个智能体生物安全能力基准测试，旨在评估大语言模型智能体在分子生物学相关任务上的表现，特别是那些具有双重用途风险的场景。该基准包含三个核心任务：DNA片段设计（用于Gibson组装）、筛选规避（设计能逃避商业合成筛查的DNA片段）和液体处理机器人编程（控制OpenTrons机器人完成DNA组装）。研究对8个前沿模型进行了测试，并收集了175小时的专家人工基线数据。主要结论是：所有测试的AI智能体在所有任务上的表现均超过人类专家中位数水平，但在需要创造性生物信息推理的筛选规避任务上表现较弱；在湿实验验证中，GPT-o4-mini-high生成的脚本成功完成了DNA组装。该工作首次系统性地评估了AI智能体在真实分子生物学操作中的能力，为生物安全风险评估和防护措施的制定提供了重要参考。
