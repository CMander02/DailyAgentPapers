---
title: "Hackers or Hallucinators? A Comprehensive Analysis of LLM-Based Automated Penetration Testing"
authors:
  - "Jiaren Peng"
  - "Zeqin Li"
  - "Chang You"
  - "Yan Wang"
  - "Hanlin Sun"
  - "Xuan Tian"
  - "Shuqiao Zhang"
  - "Junyi Liu"
  - "Jianguo Zhao"
  - "Renyang Liu"
  - "Haoran Ou"
  - "Yuqiang Sun"
  - "Jiancheng Zhang"
  - "Yutong Jiao"
  - "Kunshu Song"
  - "Chao Zhang"
  - "Fan Shi"
  - "Hongda Sun"
  - "Rui Yan"
  - "Cheng Huang"
date: "2026-04-07"
arxiv_id: "2604.05719"
arxiv_url: "https://arxiv.org/abs/2604.05719"
pdf_url: "https://arxiv.org/pdf/2604.05719v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.SE"
tags:
  - "Automated Penetration Testing"
  - "Agent Architecture"
  - "Systematization of Knowledge"
  - "Empirical Benchmark"
  - "Tool-Using Agent"
  - "Multi-Agent Systems"
  - "Cybersecurity"
relevance_score: 8.0
---

# Hackers or Hallucinators? A Comprehensive Analysis of LLM-Based Automated Penetration Testing

## 原始摘要

The rapid advancement of Large Language Models (LLMs) has created new opportunities for Automated Penetration Testing (AutoPT), spawning numerous frameworks aimed at achieving end-to-end autonomous attacks. However, despite the proliferation of related studies, existing research generally lacks systematic architectural analysis and large-scale empirical comparisons under a unified benchmark. Therefore, this paper presents the first Systematization of Knowledge (SoK) focusing on the architectural design and comprehensive empirical evaluation of current LLM-based AutoPT frameworks. At systematization level, we comprehensively review existing framework designs across six dimensions: agent architecture, agent plan, agent memory, agent execution, external knowledge, and benchmarks. At empirical level, we conduct large-scale experiments on 13 representative open-source AutoPT frameworks and 2 baseline frameworks utilizing a unified benchmark. The experiments consumed over 10 billion tokens in total and generated more than 1,500 execution logs, which were manually reviewed and analyzed over four months by a panel of more than 15 researchers with expertise in cybersecurity. By investigating the latest progress in this rapidly developing field, we provide researchers with a structured taxonomy to understand existing LLM-based AutoPT frameworks and a large-scale empirical benchmark, along with promising directions for future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）驱动的自动化渗透测试（AutoPT）领域存在的两个关键问题：缺乏系统性的架构梳理和缺乏大规模、可比较的实证评估。

研究背景是，随着LLM的快速发展，利用其实现端到端自动化攻击的AutoPT框架大量涌现，以满足日益增长的渗透测试市场需求并弥补网络安全人才缺口。然而，现有研究存在明显不足。首先，多数工作聚焦于早期的深度强化学习方法，或仅对LLM在PT中的潜力进行宏观趋势分析，缺乏对当前主流LLM-based AutoPT框架架构设计的系统性解构与知识梳理。其次，尽管出现了一些动态仿真环境，但严重缺乏在统一基准下对多个框架进行公平、定量比较的大规模实证研究。这导致框架设计者缺乏可靠的实证证据来评估关键设计决策的优劣。

因此，本文要解决的核心问题是：通过对现有LLM-based AutoPT框架进行首次系统化的知识梳理（SoK）和大规模实证研究，填补上述空白。具体而言，论文试图建立一个多维度的分析框架来系统解构现有设计，并首次在统一基准下对15个代表性框架进行大规模实验与对比分析，以验证或挑战该领域的一些普遍假设（如多代理必然优于单代理、外部知识库总是有益等），从而为未来的研究和框架设计提供可靠的实证依据和清晰的方向指引。

### Q2: 有哪些相关研究？

本文作为首个针对LLM驱动的自动化渗透测试（AutoPT）的系统性知识梳理（SoK），相关工作主要围绕**方法类**和**评测类**展开。

在**方法类**研究中，相关工作聚焦于利用LLM构建端到端的自主攻击代理框架。本文将这些框架的设计系统化解构为六个核心维度（智能体架构、规划、记忆、执行、外部知识、基准测试），从而建立了清晰的分析框架。具体而言，相关工作在智能体架构上可分为单智能体（如PentestGPT）与多智能体协作（如ARACNE、AutoAttacker）两大类；在功能实现上，普遍包含规划、执行、总结等通用功能，部分框架还引入了侦察、检索、智能体编排等专用功能。本文与这些工作的主要区别在于：现有研究多为独立的框架提案，缺乏对整体架构设计的系统性归纳与横向比较；而本文首次提出了一个统一的分析框架，对现有设计的共性与差异进行了结构化梳理。

在**评测类**研究中，相关工作通常基于各自构建的测试环境（如特定漏洞的虚拟机）和评估指标进行实验。本文与这些工作的区别在于：现有评测往往规模有限、标准不一，难以进行公平比较。为此，本文的贡献在于建立了**统一的基准测试**，并对13个代表性的开源AutoPT框架和2个基线框架进行了大规模实证评估（消耗超过100亿token，生成超1500份执行日志），这为客观比较不同框架的性能提供了前所未有的经验依据。

### Q3: 论文如何解决这个问题？

论文通过构建一个系统化的分析框架和进行大规模实证评估来解决现有LLM驱动的自动化渗透测试（AutoPT）研究缺乏系统性架构分析和统一基准下比较的问题。

**核心方法与架构设计：**
论文首先提出了一个系统化知识（SoK）框架，从六个核心维度对现有AutoPT框架进行解构分析：智能体架构、智能体规划、智能体记忆、智能体执行、外部知识和基准测试。这个框架围绕三个核心问题展开：(a) 系统由谁驱动？(b) 系统如何行动？(c) 系统依赖什么？

**主要模块/组件与创新点：**
1.  **智能体架构分析**：论文明确定义了智能体为“被分配特定角色和职责、拥有独立上下文窗口和决策权的LLM”。基于此，深入分析了两种角色定义方法：基于提示（灵活但可能不稳定）和基于后训练（稳定但成本高）。论文进一步将框架中的智能体角色归纳为核心功能，包括：
    *   **通用功能**：几乎所有框架都通过智能体实现的规划、执行和总结功能。论文详细梳理了各框架中承担这些功能的智能体角色对应关系。
    *   **专用功能**：部分框架引入的增强模块，如专注于目标系统信息收集的**侦察**功能、通过RAG与外部知识库交互的**检索**功能、负责资源调度和任务路由的**智能体编排**功能，以及对执行结果进行安全验证和态势评估的**反馈**功能。

2.  **大规模实证评估**：在实证层面，论文的解决方案是建立一个统一的基准，并对13个代表性的开源AutoPT框架和2个基线框架进行大规模实验。实验总计消耗超过100亿个令牌，生成了超过1500份执行日志。这些日志由一个超过15名网络安全专家组成的小组进行了长达四个月的人工审查和分析。这种方法首次在统一标准下提供了对现有框架能力的大规模、客观比较。

**整体而言，论文的创新点在于：**
*   **提出了首个针对LLM-Based AutoPT架构设计的系统化分析框架**，清晰揭示了不同框架在设计选择上的共性与关键差异。
*   **进行了该领域首次大规模、统一的实证基准测试**，基于真实消耗和人工专家分析提供了可靠的性能洞察，弥补了现有研究缺乏横向比较的空白。
*   **通过功能视角对纷繁复杂的智能体角色进行了归一化梳理**，揭示了角色与功能之间的多对多关系，帮助研究者超越命名差异理解架构本质。

### Q4: 论文做了哪些实验？

论文在实证层面进行了大规模实验，对13个代表性的开源LLM-based AutoPT框架和2个基线框架，在一个统一的基准测试下进行了评估。实验设置上，研究团队构建了一个统一的基准测试环境，以确保公平比较。数据集/基准测试方面，实验使用了专门设计的统一基准，该基准涵盖了多种渗透测试场景，旨在系统评估框架的端到端攻击能力。对比方法包括13个开源AutoPT框架（如AutoGPT、GPT Engineer等）和2个基线框架（例如基于规则的传统自动化工具），总计15个系统。主要结果基于对超过1,500份执行日志的手动审查与分析，这些日志由超过15位网络安全专家耗时四个月完成，实验总计消耗了超过100亿个tokens。关键数据指标包括：框架的成功率、攻击步骤的有效性、幻觉率（即产生不切实际或错误攻击建议的比例）以及资源消耗（如tokens使用量）。实验发现，现有框架在复杂场景中普遍存在较高的“幻觉”问题，实际攻击成功率有限，且性能差异显著，这为未来研究方向提供了实证基础。

### Q5: 有什么可以进一步探索的点？

该论文虽对现有LLM驱动的自动化渗透测试框架进行了系统梳理与大规模评估，但仍存在若干可深入探索的方向。首先，其评估主要基于开源框架与统一基准，但现实网络环境复杂多变，未来需在更动态、异构的真实场景中测试框架的适应性与鲁棒性。其次，研究侧重于架构与执行效果分析，对LLM在渗透测试中产生的“幻觉”或错误决策的内在机制（如知识缺失、推理偏差）缺乏深入解释，可结合可解释AI技术进行根因分析。此外，现有框架多依赖单一LLM，未来可探索多模型协作机制，或融合符号推理与知识图谱来增强逻辑严谨性。最后，论文未充分探讨防御视角——如何基于这些框架的弱点设计主动防御方案，这将是平衡攻防能力的关键。

### Q6: 总结一下论文的主要内容

本文首次对基于大语言模型的自动化渗透测试框架进行了系统化知识梳理和大规模实证研究。针对该领域缺乏系统性架构分析和统一基准下大规模比较的问题，论文从系统化和实证化两个层面展开工作。在系统化层面，作者提出了一个六维分析框架，从智能体架构、规划、记忆、执行、外部知识和基准测试等方面对现有框架设计进行了全面解构与分类。在实证层面，研究在统一基准上对13个代表性开源框架和2个基线框架进行了大规模实验，消耗超百亿令牌，生成超1500份执行日志，并由专家团队进行了长达四个月的手动分析。主要结论颠覆了多项学术界普遍假设：单智能体架构表现出意外竞争力，复杂多智能体设计未必带来性能提升；外部知识库常产生负收益；工具池大小与任务成功率无正相关；仅使用简单提示的AI编程智能体表现优异，超越了多数专门设计的框架；不同骨干大模型在渗透测试任务上存在显著适应差距，需针对性优化；幻觉现象（尤其是flag幻觉）普遍存在。研究为重新审视现有设计假设提供了实证依据，并指出了未来研究方向，如优先构建高质量漏洞知识库、优化记忆管理、开发任务相关的工具调度机制等。
