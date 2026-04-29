---
title: "Your Reviews Replicate You: LLM-Based Agents as Customer Digital Twins for Conjoint Analysis"
authors:
  - "Bin Xuan"
  - "Jungmin Hwang"
  - "Hakyeon Lee"
date: "2026-03-06"
arxiv_id: "2604.22756"
arxiv_url: "https://arxiv.org/abs/2604.22756"
pdf_url: "https://arxiv.org/pdf/2604.22756v1"
categories:
  - "cs.IR"
  - "cs.AI"
tags:
  - "LLM-based Agents"
  - "Customer Digital Twins"
  - "Conjoint Analysis"
  - "RAG"
  - "Preference Modeling"
  - "Marketing Research"
relevance_score: 8.5
---

# Your Reviews Replicate You: LLM-Based Agents as Customer Digital Twins for Conjoint Analysis

## 原始摘要

Conjoint analysis is a cornerstone of market research for estimating consumer preferences; however, traditional methods face persistent challenges regarding time, cost, and respondent fatigue. To address these limitations, this study proposes a framework that utilizes large language model (LLM)-based "customer digital twins (CDT)" as virtual respondents. We identified active users within the Reddit community and aggregated their comprehensive review histories to construct individualized vector databases. By integrating retrieval-augmented generation (RAG) with prompt engineering, this study developed customer agents capable of dynamically retrieving and reasoning upon their specific past preferences and constraints. These customer agents, called CDTs, performed pairwise comparison tasks on product profiles generated via fractional factorial design, and the resulting choice data was analyzed to estimate part-worth utilities by logistic regression. Empirical validation demonstrates that these CDTs predict the preferences of actual users with 87.73% accuracy. Furthermore, a case study on the computer monitor category successfully quantified trade-offs between attributes such as panel type and resolution, deriving preference structures consistent with market realities. Ultimately, this study contributes to marketing research by presenting a scalable alternative that significantly improves both agility and cost-efficiency to traditional methods.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决传统联合分析（conjoint analysis）在市场研究中所面临的根本性限制。传统方法严重依赖人工受访者，导致高成本、耗时、受访者疲劳以及在某些目标群体（如B2B市场或专家人群）中难以招募到合适受访者的问题。这些限制使得联合分析难以迭代和敏捷地应用于快速决策的产品开发环境。为应对这些挑战，论文提出利用基于大语言模型（LLM）的“客户数字孪生（Customer Digital Twins, CDT）”作为虚拟受访者。通过构建能够模拟真实消费者偏好系统的CDT，论文旨在提供一个可扩展、低成本且高效的替代方案，从而克服对人工受访者的依赖，并支持迭代性的市场分析。

### Q2: 有哪些相关研究？

论文的相关研究涵盖两个主要领域：联合分析方法和基于LLM的虚拟受访者。在联合分析方面，论文回顾了从传统评级方法到选择式联合分析（CBC）、自适应联合分析（ACA）等方法的演进，强调了这些方法在提高生态效用和效率方面的努力，但仍受限于人工参与。在LLM作为虚拟受访者方面，论文将现有研究分为群体级和个体级方法：群体级方法通过提示工程模拟特定人群的平均响应；个体级方法旨在重现个人独特的偏好系统，常通过检索增强生成（RAG）技术提供个人历史数据来克服提示长度限制。本文与这些工作的关系在于，它扩展了个体级方法，创新性地使用公开可访问的在线社区评论数据（而非访谈或调查数据）来构建CDT，并将其应用于联合分析。这直接解决了传统方法的数据收集瓶颈，并实现了对个人偏好异质性的捕获。

### Q3: 论文如何解决这个问题？

论文提出一个框架，将LLM-based Agent作为客户数字孪生（CDT）集成到联合分析工作流中。该框架分为两个主要阶段：CDT创建和联合分析工作流。在CDT创建阶段，首先从Reddit等在线社区识别活跃用户，并收集其全面的评论历史（不限于特定产品类别，以捕获潜在上下文信号）。这些评论数据被转换为向量嵌入并存储在个体向量数据库中，形成RAG系统的核心。通过精心设计的提示工程，定义CDT的角色和决策因素，使其能基于RAG动态检索的相关评论进行推理，从而构建反映用户特定偏好系统的CDT。在联合分析工作流阶段，CDT池执行成对比较任务：产品配置文件基于正交设计（如L16正交数组）生成，以高效估计主要效应；每个CDT比较两个产品配置文件，并基于RAG提供的历史偏好模式做出选择。收集的二元选择数据通过逻辑回归分析，估计各属性水平的部分效用（part-worth utilities）和属性重要性。关键技术包括：RAG实现个性化记忆和推理，提示工程确保角色一致性，正交设计减少比较数量以提高效率。

### Q4: 论文做了哪些实验？

论文进行了两项主要实验：初步验证和案例研究。初步验证旨在评估CDT模拟实际用户偏好的准确性。使用Reddit r/Monitors社区的200个活跃用户数据，提取了163条包含明确属性比较的评论作为真实偏好基准（ground truth）。为避免信息泄露，CDT仅能访问评论撰写时间之前的历史数据。验证结果显示，CDT的预测准确率达到87.73%（149/163正确），远高于随机选择的50%基线，表明CDT能有效学习用户特定的偏好系统。案例研究则演示了框架的实用价值。针对电脑显示器产品，定义了5个属性（如屏幕尺寸、面板类型、分辨率等），每个属性两个水平。通过正交设计生成16个产品配置文件，并构建16个成对比较问题。200个CDT（基于同一用户集）参与任务，产生的3200个响应数据通过逻辑回归分析。结果表明，面板类型（重要性32.9%）和分辨率（29.2%）是最重要的属性，与市场现实一致。此外，论文还探索了问题设计（成对比较 vs. 排名式 vs. CBC）、模型温度参数（0, 0.5, 1）的影响以及RAG系统的作用，验证了成对比较的稳定性和RAG对个性化响应的关键性。

### Q5: 有什么可以进一步探索的点？

论文承认了若干局限性，为未来研究指明了方向。首先，最根本的限制是缺乏与真实用户的直接验证：CDT的选择是否准确重现了其数据来源用户的实际偏好，仍需专门研究确认。其次，数据来源仅限于Reddit平台，其用户可能在人口统计或技术涉入度上与一般消费者有差异，限制了结果的可推广性；未来需跨平台（如其他社交网络或电商评论）验证。第三，案例仅针对技术产品（显示器），需扩展到时尚、食品等其他产品类别以评估框架通用性。第四，LLM技术发展迅速，本研究结果可能局限于特定模型和时间点，需探索不同LLM（如开源模型）的性能。最后，方法层面可进一步优化：改进RAG机制（如更精准的检索策略）、探索更复杂的提示工程以捕获长期偏好演变，或结合其他数据源（如购买历史）增强CDT的保真度。这些探索将有助于提升框架的鲁棒性和实用性。

### Q6: 总结一下论文的主要内容

本文提出了一个创新框架，利用基于LLM的客户数字孪生（CDT）作为虚拟受访者，以解决传统联合分析依赖人工受访者所带来的成本、时间和可访问性限制。核心方法结合检索增强生成（RAG）和提示工程，从Reddit等在线社区的用户评论历史中构建个性化CDT，使其能动态检索和推理特定偏好模式。CDT通过执行基于正交设计的成对比较任务来模拟消费者选择，其产生的数据经统计分析可估计属性级部分效用和重要性。实验验证显示，CDT能准确预测实际用户偏好（87.73%准确率），案例研究成功量化了产品属性权衡（如面板类型和分辨率为显示器购买关键因素）。论文贡献在于：为市场研究提供了一个可扩展、低成本的替代方案，推动了LLM-based Agent在个性化偏好建模中的应用，并探索了Agent设计原则（如问题格式选择和RAG的关键作用）。尽管存在局限性，但研究为利用LLM进行敏捷市场分析奠定了基础。
