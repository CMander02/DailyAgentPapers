---
title: "WebTestBench: Evaluating Computer-Use Agents towards End-to-End Automated Web Testing"
authors:
  - "Fanheng Kong"
  - "Jingyuan Zhang"
  - "Yang Yue"
  - "Chenxi Sun"
  - "Yang Tian"
  - "Shi Feng"
  - "Xiaocui Yang"
  - "Daling Wang"
  - "Yu Tian"
  - "Jun Du"
  - "Wenchong Zeng"
  - "Han Li"
  - "Kun Gai"
date: "2026-03-26"
arxiv_id: "2603.25226"
arxiv_url: "https://arxiv.org/abs/2603.25226"
pdf_url: "https://arxiv.org/pdf/2603.25226v1"
github_url: "https://github.com/friedrichor/WebTestBench"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.CL"
  - "cs.MA"
tags:
  - "Web Agent"
  - "Agent Benchmark"
  - "Agent Evaluation"
  - "Tool Use"
  - "Human-Computer Interaction"
  - "End-to-End Testing"
relevance_score: 7.5
---

# WebTestBench: Evaluating Computer-Use Agents towards End-to-End Automated Web Testing

## 原始摘要

The emergence of Large Language Models (LLMs) has catalyzed a paradigm shift in programming, giving rise to "vibe coding", where users can build complete projects and even control computers using natural language instructions. This paradigm has driven automated webpage development, but it introduces a new requirement about how to automatically verify whether the web functionalities are reliably implemented. Existing works struggle to adapt, relying on static visual similarity or predefined checklists that constrain their utility in open-ended environments. Furthermore, they overlook a vital aspect of software quality, namely latent logical constraints. To address these gaps, we introduce WebTestBench, a benchmark for evaluating end-to-end automated web testing. WebTestBench encompasses comprehensive dimensions across diverse web application categories. We decompose the testing process into two cascaded sub-tasks, checklist generation and defect detection, and propose WebTester, a baseline framework for this task. Evaluating popular LLMs with WebTester reveals severe challenges, including insufficient test completeness, detection bottlenecks, and long-horizon interaction unreliability. These findings expose a substantial gap between current computer-use agent capabilities and industrial-grade deployment demands. We hope that WebTestBench provides valuable insights and guidance for advancing end-to-end automated web testing. Our dataset and code are available at https://github.com/friedrichor/WebTestBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）驱动的“氛围编程”（vibe coding）范式下，自动化网页开发所面临的一个关键瓶颈问题：如何自动、可靠地验证所生成网页的功能实现质量，即**端到端自动化网页测试**。

**研究背景**：随着LLM的发展，非专业用户也能通过自然语言指令构建完整的网页应用，这极大地压缩了传统开发流程。然而，AI生成的网页应用往往存在功能缺陷或遗漏。对于缺乏工程经验的创建者而言，验证这些应用的可靠性成为障碍。因此，在代码生成高度自动化后，**自动化网页测试**已成为现代网页开发的关键瓶颈。

**现有方法的不足**：当前的研究和评估框架难以适应这一新兴范式。具体不足体现在：1. **评估方法局限**：许多工作源自网页生成任务，其评估依赖于静态视觉相似性或孤立的交互组件检查，不够全面。2. **依赖预定义清单**：更现实的方法会使用计算机使用代理（CUA）模拟用户进行动态功能评估，但严重依赖人工预定义的、僵化的测试清单，这在开放式的开发环境中实用性受限。3. **忽视逻辑约束**：现有工作普遍忽略了软件质量的一个基本方面——潜在的**内在逻辑约束**（例如，会议室预订系统中同一时段不能重复预订）。4. **代理不可靠性**：CUA在复杂网页环境中的交互不可靠性，也给功能评估过程带来了执行偏差。

**本文要解决的核心问题**：为了填补上述空白，本文提出了WebTestBench基准测试。其核心目标是建立一个**无需人工预定义测试项、支持端到端、长序列交互的自动化网页测试评估框架**。该基准要求测试代理能够自主生成测试清单并执行缺陷检测，特别强调了对功能、内容、交互以及以往被忽视的**潜在逻辑约束**等多个维度的综合评估，以更真实地反映AI驱动网页开发场景下的测试需求，并衡量当前计算机使用代理与工业级部署要求之间的能力差距。

### Q2: 有哪些相关研究？

相关研究主要分为计算机使用智能体（CUAs）和网页测试基准两类。

在计算机使用智能体方面，现有研究主要关注智能体在真实网页场景（如在线购物、论坛）中执行多步骤操作（导航、点击、输入）的成功率，其评估重点在于任务完成能力。然而，这些工作对智能体在软件质量保障，特别是缺陷检测方面的效能探索不足。

在网页测试基准方面，近期研究致力于评估自动化应用测试。例如，GTArena提出了一个自动化GUI测试评估框架，将过程分解为测试意图生成、测试任务执行和GUI缺陷检测，但其缺陷检测仅限于基于单步前后状态比较推断的原子级错误。GUITestBench则专注于探索性GUI缺陷发现。另有一些工作研究了将自动化网页智能体适配为自动化测试智能体的可行性，引入了评估其执行人工编写测试用例能力的基准，并进一步考察了智能体准确判断缺陷的能力。

本文提出的WebTestBench与上述工作的关系和区别在于：首先，现有基准大多依赖人工编写的检查清单或测试用例，这为非专业开发者设置了门槛，而本文旨在评估无检查清单的端到端自动化测试能力。其次，现有工作忽略了软件质量中一个至关重要的方面——潜在的逻辑约束。因此，WebTestBench旨在填补这些空白，专注于评估CUAs在真实场景下的端到端自动化网页测试能力，以弥补人机协作应用开发生命周期中的关键缺失环节。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为WebTester的基线框架来解决端到端自动化网页测试的挑战。该框架将测试过程分解为两个级联子任务：检查清单生成和缺陷检测，并设计了相应的智能体来执行这些任务。

整体框架由两个核心组件构成：检查清单生成智能体和缺陷检测智能体。首先，检查清单生成智能体接收用于合成目标网页应用的开发指令，将其分解为一个结构化的、可执行的测试检查清单。每个测试项被定义为一个三元组，包括测试内容的文本描述、需要在网页界面上执行的操作以及用于判定通过/失败的预期结果。这解决了现有方法依赖静态视觉相似性或预定义检查清单、难以适应开放环境的问题。

随后，缺陷检测智能体基于开发指令、生成的检查清单和目标网页应用，通过模拟人类与网页的交互来执行每个测试项，并为每个项目确定二元的执行状态。对于失败的测试项，该智能体还会生成描述所观察到的错误行为的缺陷报告。最终，框架输出一组结构化的测试结果和缺陷报告。

该方法的创新点在于其端到端的自动化流程设计和对“潜在逻辑约束”这一关键软件质量维度的关注。通过将自然语言指令自动转化为可执行的测试用例，并模拟真实用户交互进行验证，框架旨在更全面地评估网页功能，特别是那些隐藏在界面之下的逻辑规则。然而，论文评估也揭示了当前大语言模型在该框架下仍面临测试完整性不足、检测瓶颈和长程交互不可靠等严峻挑战，表明现有智能体能力与工业级部署需求之间存在显著差距。

### Q4: 论文做了哪些实验？

论文构建了基于Claude Code的智能体框架WebTester，并利用Playwright MCP实现浏览器自动化交互。实验评估了包括Claude Opus/Sonnet 4.5、GPT-5.2/5.1、GLM-5/4.7、Step-3.5-Flash、Qwen3-Coder-Next、MiMo-V2-Flash和Minimax-M2.1在内的多个闭源和开源大模型在WebTestBench基准上的端到端自动化网页测试性能。该基准涵盖展示、搜索、工具、商务、数据管理、工作流和用户生成内容等七类网页应用。

主要结果如下：所有模型在端到端测试中的F1分数均未超过30%，表现最佳的GPT-5.1 F1为26.4%（召回率33.3%），MiMo-V2-Flash F1为25.1%（精确率34.8%）。测试完整性不足，所有模型覆盖率均低于70%，即使最优模型也遗漏了至少三分之一的测试用例。检测瓶颈明显，多数模型精确率约30%，召回率低于25%，存在高误报或高漏报问题。长序列交互可靠性差，例如Step-3.5-Flash平均每个样本需57步交互和337万token，易出现状态跟踪失败。实验还对比了黄金检查清单的Oracle设置，显示检测性能显著提升（如GPT-5.1召回率升至63.4%），证实测试不完整性是端到端设置的主要瓶颈。此外，模型在数据管理类任务表现最佳（平均F1 26.5%），在搜索和用户生成内容类任务最差（平均F1约15.5%），且性能随网页复杂度（DOM节点数、交互元素数增加）而下降。自动评估与人工评判相关性高（Qwen3.5-27B的Pearson r达87.1%）。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在三个方面：基准构建成本高、评估协议覆盖不全以及应用场景多样性有限。未来研究可首先探索如何降低标注成本，例如利用LLM辅助生成测试用例和潜在逻辑约束，通过半自动化方式扩展基准规模。其次，评估方法需改进以识别超出预设检查表的有效测试用例，可引入基于LLM的适应性评分机制，动态判断生成测试的合理性。此外，需突破当前计算机使用代理（CUA）在动态内容感知上的瓶颈，研究融合多模态输入（如视频流、实时交互日志）的增强感知框架，以支持游戏、实时交互系统等高动态场景的测试。最后，可探索将测试生成与缺陷检测更深层次结合，构建具有自我迭代优化能力的闭环测试智能体，从而提升长程交互的可靠性与测试完备性。

### Q6: 总结一下论文的主要内容

该论文针对AI驱动的网页开发时代，提出了一种无需人工编写测试用例的端到端自动化网页测试新范式。核心问题是现有方法难以适应开放环境，且忽视了软件质量中的潜在逻辑约束。为此，作者构建了WebTestBench基准，涵盖多样化的网页应用类别，并将测试过程分解为清单生成和缺陷检测两个子任务，同时提出了一个基线框架WebTester。评估结果表明，当前大语言模型在测试完整性、缺陷检测能力和长序列交互可靠性方面存在严重不足，揭示了现有计算机使用代理能力与工业级部署需求之间的巨大差距。该工作的主要贡献在于为自动化网页测试提供了首个综合性评估基准，并指明了未来研究的关键挑战与方向。
