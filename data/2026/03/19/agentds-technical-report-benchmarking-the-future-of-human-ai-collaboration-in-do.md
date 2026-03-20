---
title: "AgentDS Technical Report: Benchmarking the Future of Human-AI Collaboration in Domain-Specific Data Science"
authors:
  - "An Luo"
  - "Jin Du"
  - "Xun Xian"
  - "Robert Specht"
  - "Fangqiao Tian"
  - "Ganghua Wang"
  - "Xuan Bi"
  - "Charles Fleming"
  - "Ashish Kundu"
  - "Jayanth Srinivasa"
  - "Mingyi Hong"
  - "Rui Zhang"
  - "Tianxi Li"
  - "Galin Jones"
  - "Jie Ding"
date: "2026-03-19"
arxiv_id: "2603.19005"
arxiv_url: "https://arxiv.org/abs/2603.19005"
pdf_url: "https://arxiv.org/pdf/2603.19005v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "stat.ME"
tags:
  - "Benchmark"
  - "Human-AI Collaboration"
  - "Domain-Specific Agent"
  - "Data Science Agent"
  - "Evaluation"
relevance_score: 8.0
---

# AgentDS Technical Report: Benchmarking the Future of Human-AI Collaboration in Domain-Specific Data Science

## 原始摘要

Data science plays a critical role in transforming complex data into actionable insights across numerous domains. Recent developments in large language models (LLMs) and artificial intelligence (AI) agents have significantly automated data science workflow. However, it remains unclear to what extent AI agents can match the performance of human experts on domain-specific data science tasks, and in which aspects human expertise continues to provide advantages. We introduce AgentDS, a benchmark and competition designed to evaluate both AI agents and human-AI collaboration performance in domain-specific data science. AgentDS consists of 17 challenges across six industries: commerce, food production, healthcare, insurance, manufacturing, and retail banking. We conducted an open competition involving 29 teams and 80 participants, enabling systematic comparison between human-AI collaborative approaches and AI-only baselines. Our results show that current AI agents struggle with domain-specific reasoning. AI-only baselines perform near or below the median of competition participants, while the strongest solutions arise from human-AI collaboration. These findings challenge the narrative of complete automation by AI and underscore the enduring importance of human expertise in data science, while illuminating directions for the next generation of AI. Visit the AgentDS website here: https://agentds.org/ and open source datasets here: https://huggingface.co/datasets/lainmn/AgentDS .

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究和量化人工智能代理（AI Agents）与人类专家在特定领域数据科学任务上的能力差异，并评估人机协作模式的有效性。研究背景是，尽管大语言模型和AI代理在自动化代码生成和执行标准机器学习任务方面展现出强大能力，甚至能在某些通用竞赛中达到顶尖水平，但当前研究多集中于通用工作流的自动化，往往忽视了现实世界问题中至关重要的领域专业知识。现有方法的不足在于，当前的AI代理和基准测试通常无法有效利用特定领域的洞察力来处理复杂的实际问题，它们生成的解决方案往往是通用化的，难以应对需要深度领域知识进行特征工程、数据理解和策略决策的场景。

因此，本文要解决的核心问题是：在特定领域的数据科学任务中，人类专家在多大程度上以及哪些方面仍然优于自主运行的AI代理？为了系统地回答这个问题，论文引入了AgentDS基准测试和竞赛。该基准包含覆盖商业、食品生产、医疗保健等六个行业的17项挑战，其设计旨在奖励那些融入领域知识的解决方案，而非仅依赖现成算法的通用流程。通过组织有80名参与者参加的公开竞赛，论文得以系统比较纯AI基线方案与人机协作方案的性能。研究发现，当前AI代理在领域特定推理方面存在明显短板，而最强的解决方案均来自人机协作，这挑战了AI将实现完全自动化的叙事，强调了人类专业知识在数据科学中的持久价值，并为下一代AI的发展指明了方向。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**方法类、评测类和协作类**。

在**方法类**研究中，已有工作利用大语言模型（LLM）和AI智能体来自动化数据科学工作流，例如自动生成代码和执行常规机器学习任务，甚至有系统通过结构化推理达到了Kaggle大师级水平。然而，这些研究大多侧重于生成通用代码和执行标准流程，**缺乏对特定领域知识的整合**，而本文的AgentDS基准则明确要求并奖励领域特定的洞察力。

在**评测类**研究中，现有的AI智能体基准测试往往未能充分评估智能体在领域特定知识应用方面的能力，尤其是在处理非表格数据或需要跨模态信号理解的任务上。相比之下，**AgentDS专门设计了涵盖六个行业的17个挑战，其数据集经过精心构建，使得依赖通用流程的方法表现不佳，从而凸显了领域专业知识的重要性**。

在**协作类**研究中，关于人-AI协作在数据科学中的系统性评估相对有限。本文通过组织公开竞赛，直接比较了纯AI基线方案与人-AI协作方案的性能，**实证了最强解决方案源于人-AI协作，而非任何一方的单独工作**，这为未来设计支持有效协作而非完全自动化的系统指明了方向。

### Q3: 论文如何解决这个问题？

论文通过设计并实施一个名为AgentDS的基准测试和竞赛，来解决评估AI智能体与人类专家在领域特定数据科学任务上表现差异的问题。其核心方法是构建一个多领域、多模态、强调真实性的评估框架，并通过公开竞赛收集人类-AI协作与纯AI基线的系统对比数据。

整体框架基于三个核心原则：领域特定复杂性、多模态整合和现实世界合理性。基准涵盖了商业、食品生产、医疗保健、保险、制造和零售银行六个重要行业，共17项挑战。每个挑战不仅提供包含预测目标的主表格数据集，还额外提供图像、文本、结构化文件（如JSON、PDF）等多种模态的辅助数据，以此模拟真实数据科学项目中常见的异构数据环境。

主要模块包括精心设计的数据集生成流程和评估体系。数据集生成分为四个阶段：1）领域研究，确保问题定义和特征关系符合真实行业知识；2）数据生成，通过合成数据过程将影响预测的关键潜在变量嵌入到额外模态中，使得高性能解决方案必须依赖领域知识来有效提取这些信息；3）性能界限与难度校准，利用对数据生成过程的控制来确定理论上限，从而区分方法局限与根本限制；4）文档与验证，为每个领域提供详细的背景说明文档，并由领域专家验证挑战的合理性。

在评估方面，创新性地采用了分位数评分法。首先，每个挑战使用其领域特定的常用指标（如Macro-F1、RMSE）进行评估。然后，将参与者在每个挑战中的原始得分转换为分位数分数，使得不同指标和量纲的挑战成绩可以公平地归一化到[0,1]区间。最后，通过层级聚合（挑战→领域→整体）计算出一个综合得分，用于最终排名。

为了对比，论文设置了两个代表不同自主程度的纯AI基线：使用GPT-4o的直接提示基线和使用Claude Code的智能体编码基线。这些基线在完全无人干预的情况下处理相同挑战，其得分被插入到参赛者成绩池中计算分位数排名。结果显示，纯AI基线的表现接近或低于参赛者中位数，而顶尖成绩均来自人类-AI协作，这清晰地揭示了当前AI在领域推理上的不足，并凸显了人类专业知识不可替代的价值。

### Q4: 论文做了哪些实验？

论文通过AgentDS基准测试和竞赛，系统评估了AI代理与人类-AI协作在领域特定数据科学任务上的表现。实验设置包括：1）构建涵盖商业、食品生产、医疗保健、保险、制造和零售银行六个领域的17项挑战，每项挑战提供包含预测目标的主表格数据集及图像、文本、PDF等多模态辅助数据；2）举办公开竞赛，允许参赛团队自由使用AI工具，共有29支团队（80名参与者）提交有效结果；3）设立两种AI-only基线方法进行对比：基于GPT-4o的直接提示生成代码基线，以及基于Claude Code的非交互自主代理基线。

主要结果如下：GPT-4o基线总体分位数得分仅为0.143（29支团队中排名第17），低于参赛者中位数（0.156）；Claude Code代理基线得分显著提升至0.458（排名第10），但仍远低于顶尖人类团队。关键数据指标显示，GPT-4o在所有领域均处于或低于中位数水平，尤其在零售银行（得分0.000）和商业（0.021）领域表现薄弱；Claude Code在制造（0.573）、食品生产（0.532）和零售银行（0.553）领域表现较好，但仍在各领域落后于顶尖人类团队。

实验发现：AI代理在多模态信号利用、领域推理方面存在明显局限，倾向于依赖通用流程（如标准预处理和梯度提升模型），而人类专家通过战略问题诊断、领域知识注入、筛选AI建议及基于泛化风险的模型选择等机制，显著提升了解决方案性能。最终结论表明，当前AI代理无法完全替代人类，最高效的解决方案源于人类-AI协作，其中人类主导战略决策，AI加速迭代实现。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度拓展。首先，数据层面，当前基准依赖合成数据，虽模拟了现实关系，但缺乏真实数据的复杂性和噪声。未来可引入更多真实、脱敏的行业数据集，并探索跨领域数据迁移的挑战。其次，评估范围有限，仅涵盖六个行业，未来需扩展至能源、金融科技等更多垂直领域，以检验AI代理的泛化能力。此外，人类与AI的协作模式分析仍较初步，依赖竞赛报告和定性观察，缺乏受控实验。未来可设计系统性研究，量化不同协作策略（如提示工程、人类监督程度）对性能的影响，并探索动态任务分配机制。最后，随着AI能力快速演进，基准需持续更新，并考虑引入多模态数据或实时交互任务，以更全面评估未来人机协作的潜力。

### Q6: 总结一下论文的主要内容

该论文提出了AgentDS基准测试与竞赛，旨在评估AI智能体与人类专家在领域特定数据科学任务上的表现及协作效果。核心问题是探究当前AI智能体能否在需要领域知识的复杂数据科学任务中匹配人类专家，以及人机协作在哪些方面具有优势。

方法上，AgentDS构建了包含17个挑战任务、覆盖商业、医疗等六大行业的基准，并通过公开竞赛收集了29支团队的数据，系统比较了纯AI基线与人类-AI协作方案的性能。

主要结论显示，当前AI智能体在领域特定推理（尤其是多模态信号整合）上存在明显不足；纯AI方案表现仅接近或低于参赛者中位数，而最佳解决方案均来自人机协作，其中人类负责问题诊断、领域知识注入和策略决策，AI则加速编码与实验迭代。这表明数据科学的未来并非全自动AI，而是有效的人机协作，强调了人类专业知识的持续重要性，并为下一代AI的发展指明了方向。
