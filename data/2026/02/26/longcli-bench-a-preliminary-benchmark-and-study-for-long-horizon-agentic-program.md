---
title: "LongCLI-Bench: A Preliminary Benchmark and Study for Long-horizon Agentic Programming in Command-Line Interfaces"
authors:
  - "Yukang Feng"
  - "Jianwen Sun"
  - "Zelai Yang"
  - "Jiaxin Ai"
  - "Chuanhao Li"
  - "Zizhen Li"
  - "Fanrui Zhang"
  - "Kang He"
  - "Rui Ma"
  - "Jifan Lin"
  - "Jie Sun"
  - "Yang Xiao"
  - "Sizhuo Zhou"
  - "Wenxiao Wu"
  - "Yiming Liu"
  - "Pengfei Liu"
  - "Yu Qiao"
  - "Shenglin Zhang"
  - "Kaipeng Zhang"
date: "2026-02-15"
arxiv_id: "2602.14337"
arxiv_url: "https://arxiv.org/abs/2602.14337"
pdf_url: "https://arxiv.org/pdf/2602.14337v2"
categories:
  - "cs.SE"
  - "cs.MA"
tags:
  - "Agent Benchmark"
  - "Agent Evaluation"
  - "Long-horizon Planning"
  - "Tool Use"
  - "Command-Line Interface"
  - "Software Engineering"
  - "Human-Agent Collaboration"
relevance_score: 8.5
---

# LongCLI-Bench: A Preliminary Benchmark and Study for Long-horizon Agentic Programming in Command-Line Interfaces

## 原始摘要

Recent advances in AI-assisted programming have empowered agents to execute complex workflows via command-line interfaces, however, existing benchmarks are limited by short task horizons, data contamination from GitHub scraping, and a lack of fine-grained evaluation metrics, fail to rigorously evaluate the long-horizon planning and execution capabilities essential for realistic software engineering. To address these gaps, we introduce LongCLI-Bench, a comprehensive benchmark designed to evaluate agentic capabilities across long-horizon, realistic tasks. We curated 20 high-quality, long-horizon tasks from over 1,000 computer science assignments and real-world workflows, covering four engineering categories: from scratch, feature addition, bug fixing, and refactoring. We propose a dual-set testing protocol for LongCLI-Bench, which measures requirement fulfillment (fail-to-pass) and regression avoidance (pass-to-pass), and incorporates step-level scoring to pinpoint execution failures. Extensive experiments reveal that even state-of-the-art agents achieve pass rates below 20% in LongCLI-Bench. Step-level analysis further indicates that the majority of tasks stall at less than 30% completion, highlighting that critical failures often occur in the early stages. Although self-correction offers marginal gains, human-agent collaboration through plan injection and interactive guidance yields significantly higher improvements. These results highlight that future research must emphasize the development of synergistic human-agent workflows alongside advances in agents' planning and execution capabilities to overcome key challenges in long-horizon task performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI辅助编程领域在评估智能体（Agent）长周期、复杂任务执行能力方面的基准测试不足问题。研究背景是，随着AI编程代理（如SWE-agent）的发展，它们已能通过命令行界面（CLI）执行类似人类工程师的复杂工作流，但现有的评估基准（如HumanEval、SWE-bench）存在明显局限：它们通常只关注短周期、单一类别的任务（如代码片段生成或简单仓库级修改），且数据多来自GitHub爬取，容易导致数据污染，缺乏对现实软件工程中长周期规划与执行能力的严格评估。现有方法无法有效模拟真实开发中常见的、具有连续需求和依赖关系的长周期任务，也缺少细粒度的评估指标来诊断失败模式。

因此，本文的核心问题是：如何构建一个能全面、真实地评估智能体在命令行环境中处理长周期、多类别工程任务能力的基准。为此，作者提出了LongCLI-Bench，一个从1000多个计算机科学作业和真实工作流中精心筛选出的20个高质量长周期任务基准，涵盖从零构建、功能添加、缺陷修复和代码重构四大工程类别。该基准通过双集测试协议（分别评估需求实现和回归避免）和步骤级评分，旨在精准衡量智能体的长期规划、上下文维持及复杂工作流执行能力，以推动面向实际软件工程的AI代理研究发展。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三大类：**智能体框架与模型**、**代码生成评测基准**以及**命令行界面（CLI）评估**。

在**智能体框架与模型**方面，相关工作包括专为代码优化的LLM（如DeepSeek-Coder、Qwen3-Coder）、能与真实仓库交互的SWE-agent、提供端到端框架的OpenHands，以及探索结构化定位修复、多智能体优化和规划编码等不同路径的系统。商业CLI助手（如Codex）则集成了通用工具使用和自我修正机制。本文与这些工作的关系在于，其评估对象正是这些先进的模型和智能体框架，但区别在于本文重点关注它们在**长视野、多步骤命令行任务**上的能力，而非一般的代码生成或问题修复。

在**代码生成评测基准**方面，早期工作侧重于函数级或类级任务（如HumanEval），后来扩展到更复杂的仓库级挑战（如SWE-bench系列），以及需要跨文件推理、面向新鲜度评估或涉及功能/测试生成的基准。本文与这些工作的共同目标是评估智能体的编程能力。关键区别在于，本文指出现有基准（包括SWE-bench）大多从GitHub挖掘，存在数据污染风险，且任务视野较短、评估粒度粗糙（多为二进制通过/失败）。为此，本文提出的LongCLI-Bench专门针对**高质量、长视野的真实工作流**，并引入了步骤级评分和双集测试协议，以进行更精细的分析。

在**CLI特定评估**方面，最直接的相关工作是Terminal-Bench，它提供了一个标准化沙箱来评估智能体的终端能力。本文继承了其环境交互评估的思路，但明确指出Terminal-Bench局限于短时任务和二元反馈，无法揭示长任务中的失败细节。LongCLI-Bench则通过设计更复杂、连续的长视野任务，并采用步骤级评估，旨在克服这些限制，填补了现有基准在评估**长程规划与执行能力**方面的空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为LongCLI-Bench的综合性基准测试来解决现有基准在评估命令行界面（CLI）中智能体长程任务执行能力方面的不足。其核心方法是围绕五个设计原则（长程性、污染控制、需求清晰、可解性、隔离环境）精心构建一个高质量、无污染的评估体系。

整体框架与主要模块包括：1）**任务构建流水线**：从计算机科学课程作业和真实世界工作流中人工筛选和设计任务，避免从GitHub直接抓取以控制数据污染。对每个任务，并行构建解决方案和测试套件。2）**双集合测试协议**：包含“失败到通过”（F2P）测试以评估需求完成度，以及“通过到通过”（P2P）测试以评估回归避免能力，这是许多现有基准所忽略的。3）**步骤级评分**：通过解析测试输出或手动将需求分解为子任务来提供细粒度的执行失败定位。4）**严格的验证机制**：采用迭代闭环验证程序，确保每个任务在初始代码库上F2P测试失败、在解决方案代码库上通过，且P2P测试在两者上都通过，否则经专家审查后修正或丢弃。

架构设计上，每个任务由初始代码库、任务需求文档、隔离的Docker环境、人工编写的解决方案代码库、双集合测试套件、评分解析器和元数据组成。评估时，智能体在隔离环境中接收需求并执行，结束后运行测试并计算通过率和步骤分数。该基准还支持多轮尝试和利用测试反馈的自我修正等可选评估模式。

关键创新点在于：首先，提出了**双集合测试协议**，同时衡量功能实现和系统稳定性。其次，引入了**步骤级评分**，能精准定位长链任务中早期失败的关键瓶颈。再者，通过**人工密集型策展和并行构建**确保了任务的高质量、长程性和低污染风险，平均每个任务包含超过15,000行代码和104个文件，远超现有基准。最后，对任务进行了系统分类（从零创建、功能添加、错误修复、重构）并覆盖多个技术领域，使得评估能全面反映智能体在软件工程全生命周期中的规划与执行能力。

### Q4: 论文做了哪些实验？

论文在LongCLI-Bench基准上进行了广泛的实验。实验设置方面，评估了商业CLI助手（如Codex系列、Claude Code系列）和使用OpenHands框架的开源模型（如DeepSeek-V3.1、GLM-4.6、Qwen3-235B-A22B）。采用统一的系统提示，并对每个任务进行三次独立运行取平均结果。

数据集为论文提出的LongCLI-Bench，包含从1000多个计算机科学作业和真实工作流中精选的20个高质量、长视野任务，涵盖从零开始、功能添加、错误修复和重构四个工程类别。评估协议采用双集测试：需求满足测试（F2P）和回归避免测试（P2P），并引入步骤级评分来精确定位执行失败。主要指标包括整体通过率（Pass Rate）、Pass@3、F2P/P2P通过率、F2P/P2P步骤得分以及执行时间。

主要结果如下：在单轮设置下，所有智能体在LongCLI-Bench上都面临极大挑战，整体通过率普遍低于15%，表现最好的Claude-Opus-4.6也仅为16.7%。商业系统在需求完成（F2P步骤得分）上显著优于开源框架。尽管所有模型的平均P2P步骤得分都很高（>98%），但P2P通过率（70.0%至88.3%）明显更低，表明智能体在修改时经常引入回归错误。步骤得分分布分析显示，大多数任务失败发生在早期阶段（<30%完成度），凸显了长视野规划的关键瓶颈。

论文还测试了多轮自我纠正和两种人机协作模式（静态计划注入和动态交互指导）。自我纠正带来了通过率提升，但边际收益递减，且后期可能引入新的回归风险。人机协作，特别是计划注入与交互指导结合的模式，取得了最佳效果。例如，Claude-Opus-4.6在“计划与交互”模式下通过率达到61.7%，F2P步骤得分为69.3%，显著高于基线（16.7%，50.7%）。这表明预先建立正确计划和动态人工干预能有效弥补智能体在规划和执行上的缺陷。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在任务创建依赖大量人工，导致数据集规模有限，且评估指标未能全面涵盖代码质量与执行效率。未来研究可从以下方向深入：首先，探索自动化或半自动化的任务生成方法，例如利用合成数据或程序合成技术，以低成本扩展任务多样性与规模。其次，需开发更细粒度的评估体系，纳入代码可读性、资源消耗及时间效率等维度，并结合人类专家评分，以全面衡量智能体在长周期任务中的综合表现。此外，论文指出智能体在早期阶段易失败，未来可研究更鲁棒的规划算法，如分层任务分解或动态环境适应机制，并结合人机协同框架（如实时干预与反馈循环）来提升任务完成度。最后，可探索跨领域任务迁移与泛化能力，以推动智能体在复杂真实场景中的应用。

### Q6: 总结一下论文的主要内容

该论文针对现有AI编程代理评估基准在任务长度、数据质量和评估粒度上的不足，提出了LongCLI-Bench这一专注于长视野命令行界面（CLI）智能体编程的基准。其核心贡献在于从1000多个真实计算机科学作业和工作流中精心筛选出20个高质量、长视野任务，覆盖了从零构建、功能添加、错误修复和重构四大工程类别。方法上，论文设计了双集测试协议，不仅评估需求满足度（从失败到通过），还评估回归避免能力（从通过到保持通过），并引入了步骤级评分以精确定位执行失败点。主要结论显示，即使最先进的智能体在该基准上的通过率也低于20%，且多数任务在完成度不足30%时便停滞，表明失败常发生在早期阶段。研究同时发现，自我纠正仅带来有限提升，而通过计划注入和交互式指导实现的人机协作能显著提高性能。这强调了未来研究在提升智能体自主规划与执行能力的同时，必须重视发展协同的人机工作流，以克服长视野任务中的关键挑战。
