---
title: "Toward Autonomous Long-Horizon Engineering for ML Research"
authors:
  - "Guoxin Chen"
  - "Jie Chen"
  - "Lei Chen"
  - "Jiale Zhao"
  - "Fanzhe Meng"
  - "Wayne Xin Zhao"
  - "Ruihua Song"
  - "Cheng Chen"
  - "Ji-Rong Wen"
  - "Kai Jia"
date: "2026-04-14"
arxiv_id: "2604.13018"
arxiv_url: "https://arxiv.org/abs/2604.13018"
pdf_url: "https://arxiv.org/pdf/2604.13018v1"
github_url: "https://github.com/AweAI-Team/AiScientist"
categories:
  - "cs.CL"
tags:
  - "Autonomous Agent"
  - "Long-Horizon Task"
  - "Hierarchical Orchestration"
  - "File-as-Bus"
  - "ML Research Engineering"
  - "System Design"
  - "Benchmark Evaluation"
relevance_score: 8.0
---

# Toward Autonomous Long-Horizon Engineering for ML Research

## 原始摘要

Autonomous AI research has advanced rapidly, but long-horizon ML research engineering remains difficult: agents must sustain coherent progress across task comprehension, environment setup, implementation, experimentation, and debugging over hours or days. We introduce AiScientist, a system for autonomous long-horizon engineering for ML research built on a simple principle: strong long-horizon performance requires both structured orchestration and durable state continuity. To this end, AiScientist combines hierarchical orchestration with a permission-scoped File-as-Bus workspace: a top-level Orchestrator maintains stage-level control through concise summaries and a workspace map, while specialized agents repeatedly re-ground on durable artifacts such as analyses, plans, code, and experimental evidence rather than relying primarily on conversational handoffs, yielding thin control over thick state. Across two complementary benchmarks, AiScientist improves PaperBench score by 10.54 points on average over the best matched baseline and achieves 81.82 Any Medal% on MLE-Bench Lite. Ablation studies further show that File-as-Bus protocol is a key driver of performance, reducing PaperBench by 6.41 points and MLE-Bench Lite by 31.82 points when removed. These results suggest that long-horizon ML research engineering is a systems problem of coordinating specialized work over durable project state, rather than a purely local reasoning problem.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自主AI在机器学习研究中进行长周期工程任务时所面临的挑战。研究背景是，尽管自动化科学研究已成为人工智能领域的重要目标，现有系统在辅助或自动化研究过程的某些环节（如文献综述、实验设计）上已取得进展，但涉及长时间跨度的端到端ML研究工程——包括理解任务、搭建环境、实现代码、运行实验和调试优化等一系列需持续数小时甚至数天的连贯操作——仍然非常困难。现有方法的不足在于，它们通常依赖对话式的任务传递，难以在长周期、多阶段的复杂工作中保持项目状态的连续性和一致性。早期决策（如环境配置、代码实现）可能仅在数小时后通过实验反馈才暴露出问题，而这些问题的根源往往难以追溯，导致智能体在迭代中容易丢失上下文，无法进行有效的调试和优化。例如，在严格的PaperBench基准测试中，现有最佳智能体仅能达到复制评分标准的21%，远低于人类专家41%的水平。

本文要解决的核心问题是：如何设计一个系统，使AI智能体能够自主、连贯地执行长周期的ML研究工程任务。这本质上是一个系统协调问题，而非单纯的局部推理问题。论文提出的AiScientist系统基于一个核心设计原则：长周期高性能需要结构化编排（orchestration）与持久化状态连续性（state continuity）的结合。具体而言，系统通过分层编排架构（一个顶层编排器管理阶段规划并委托给专业子智能体）来协调异构任务，同时通过“文件即总线”（File-as-Bus）协议，在权限限定的共享工作空间中，将项目状态（如分析、计划、代码、实验证据）持久化为文件工件进行传递和复用，而非依赖有损的对话式交接。这使得顶层控制保持轻量（基于简洁的阶段摘要和工作区映射），而详细的项目状态则作为厚实、持久的基石，供后续智能体反复 grounding，从而在整个长周期循环中维持决策的连贯性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：自动化科学发现、目标驱动的ML优化以及论文到代码任务。自动化科学发现研究如何让智能体生成想法、综合文献、运行实验并产出科学成果；目标驱动的ML优化关注智能体在明确目标下通过“提出-运行-评估”循环迭代改进模型；论文到代码任务则致力于将论文高保真地转化为代码库或初步实现。这些工作共同推动了自主AI研究的发展，但本文聚焦于一个更具操作挑战的场景：智能体需从模糊的论文出发，承担繁重的环境设置、解释延迟的实验反馈，并在多轮实现与调试中维持累积进展，从而要求将上述要素整合为连贯的研究工程流程。

在多智能体协调方面，经典框架如CAMEL、MetaGPT和ChatDev通过角色扮演、标准化流程和结构化通信提升了复杂任务的协作能力；近期系统将这些理念扩展到更广泛的智能体工作流和研究场景。然而，现有研究指出多智能体系统的瓶颈常在于协调失败、对齐偏差和交接验证，而非局部推理质量。本文在此基础上，将长视野性能视为协调与连续性的双重问题：不同于主要依赖对话交接来传递上下文，AiScientist通过“文件即总线”工作区将分析、计划、代码和实验证据外部化为持久化制品，使下游智能体能反复基于这些厚状态进行重锚定。因此，本文的贡献不仅是另一种分层多智能体架构，更是一种以制品为中介的连续性为核心、针对长视野ML研究工程的协调设计。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为AiScientist的系统来解决长周期机器学习研究工程中的自主性问题，其核心设计理念是“对厚重状态的轻量控制”。该系统将长周期任务视为一个系统性问题，而非纯粹的局部推理问题，强调在持久化项目状态上协调专业化工作。其解决方案主要基于两大支柱：分层编排和以文件为总线的工作空间协议。

整体框架采用三层分层编排架构。顶层是一个Tier-0编排器，它负责阶段级的控制，维护简洁的进度摘要和工作空间地图，并将具体工作委托给下一层。Tier-1由多个专业化智能体组成，分别对应机器学习研究工程的关键阶段：论文理解、任务优先级排序、代码实现、实验执行以及通用辅助。这些专家智能体在需要时，可以进一步调用Tier-2子智能体来处理高度聚焦的子任务（如环境设置、资源下载）。这种“智能体即工具”的设计使得编排器可以将专家智能体像普通工具一样调用，实现了选择性的、轻量的控制委托。

系统的关键技术是“以文件为总线”的工作空间设计。该工作空间是一个具有权限范围的文件系统，作为整个系统的记录核心。它被组织为三个主要区域：`paper_analysis/` 存储结构化的论文理解；`submission/` 存储可运行的代码库；`agent/` 存储计划、执行日志和实验结果等。所有中间产物（如分析、计划、代码、日志、证据）都以文件形式持久化保存在此，而非依赖智能体间传递的、易丢失的对话上下文。这实现了“渐进式披露”：智能体从工作空间地图开始，按需读取相关文件，执行任务后将输出（摘要和文件更新）写回工作空间。这样，项目状态得以在长时间跨度的迭代中持续积累和复用。

创新点主要体现在三个方面。首先，提出了“薄控制、厚状态”的核心系统原则，将轻量的控制逻辑与厚重的、外部化的项目状态分离，确保了长期决策的连贯性。其次，设计了基于文件的协调协议，将工作空间本身作为协调基质，使得智能体可以基于当前持久的工件状态重新进入任务，而非依赖历史推理链，这极大地增强了状态连续性和任务的可恢复性。最后，实现了证据驱动的研究-工程循环。系统运行一个自适应的“实现-运行-诊断-修补-再验证”循环，实验产生的证据（如失败记录、指标差距）被持久化记录，并直接驱动后续的代码修改和实验设计，使进展具有累积性。

实验表明，该架构在PaperBench和MLE-Bench Lite两个基准测试上均显著优于基线。消融研究进一步证实，“以文件为总线”协议是性能的关键驱动因素，移除后性能大幅下降，尤其是在需要多轮迭代优化的任务中。这证明了长周期机器学习研究工程的成功不仅需要更多的交互，更依赖于能够持久化和有效利用项目状态的系统化协调机制。

### Q4: 论文做了哪些实验？

论文在两个互补的基准上进行了实验，以评估AiScientist系统在长周期ML研究工程任务中的性能。

**实验设置与数据集/基准测试**：实验使用了两个基准。1) **PaperBench**：评估从头开始复现顶级会议论文的能力，包含20个任务，采用官方评估协议，使用GPT-5.4作为评分模型。2) **MLE-Bench Lite**：评估在竞赛式ML任务上持续进行实验改进的能力，以“Any Medal%”为主要指标。每个任务运行分配一个H20 GPU和24小时预算。

**对比方法**：在PaperBench上，与**BasicAgent**和**IterativeAgent**进行对比。在MLE-Bench Lite的受控评估中，对比了多种自主ML工程系统，包括**AIDE**、**ML-Master 2.0**和**LoongFlow**。论文还列出了官方排行榜结果作为背景参考，但强调这些并非匹配比较。

**主要结果与关键指标**：
- 在**PaperBench**上，AiScientist（论文方法）使用Gemini-3-Flash和GLM-5骨干模型时，平均得分分别为30.52和33.73，相比最佳匹配基线平均提升了9.92和11.15分。同时，其每任务成本（分别为15.67美元和12.20美元）显著低于IterativeAgent（分别为27.44美元和54.90美元）。
- 在**MLE-Bench Lite**的受控评估中，AiScientist在两种骨干模型下均取得了81.82%的Any Medal率，相比最强匹配基线分别提升了4.55和18.18个百分点。其“Above Median%”指标也 consistently 提升了9.09个百分点。
- **消融研究**表明，关键的“File-as-Bus”协议对性能至关重要。移除该协议导致PaperBench平均得分下降6.41分，MLE-Bench Lite的Any Medal率下降31.82个百分点。分析指出，该协议对后期迭代精炼的益处大于建立初始竞争性起点。此外，与简单的非分层基线（如BasicAgent和AIDE）相比，即使移除File-as-Bus的AiScientist变体仍表现出显著优势，表明分层编排设计对性能有实质性贡献。

### Q5: 有什么可以进一步探索的点？

该论文的核心创新在于通过“File-as-Bus”协议和分层编排实现长周期任务的持久状态连续性，但其探索仍存在局限。首先，系统在高度开放、定义模糊的真实世界研究问题上的泛化能力未经验证，当前基准测试（PaperBench, MLE-Bench Lite）虽具代表性，但任务范围和复杂度可能仍与前沿探索性研究有差距。其次，系统严重依赖文件系统作为状态总线，这可能成为性能瓶颈，且在需要频繁跨进程、跨服务协调的分布式实验环境中扩展性面临挑战。

未来研究方向可从以下几方面深入：一是增强系统的元认知与战略规划能力，使其能自主识别知识缺口、提出假设并设计探索性实验，而非仅按预设流程执行。二是探索更灵活的状态管理机制，如结合向量数据库或版本化对象存储来管理复杂的实验资产与依赖关系。三是引入“人机协同”模式，让AI能主动向人类研究员请求澄清或验证关键决策，形成混合主动的协作闭环。最后，可研究多智能体间更动态的协作协议，允许角色根据任务进展自主演化，而非固定分工，以更好地适应不可预测的长周期研究挑战。

### Q6: 总结一下论文的主要内容

该论文针对机器学习研究中自主AI进行长周期工程任务（如任务理解、环境搭建、实验调试等）的挑战，提出了一种名为AiScientist的系统。其核心问题是解决现有智能体在跨越数小时甚至数天的复杂研究流程中难以维持连贯进展的难题。论文的核心贡献在于提出并验证了一个关键原则：实现强大的长周期性能需要结构化编排与持久化状态连续性相结合。为此，AiScientist采用分层编排架构与一种创新的“文件即总线”工作空间协议。顶层编排器通过简洁摘要和工作空间地图进行阶段控制，而各专门智能体则持续基于持久的项目工件（如分析、计划、代码、实验证据）进行工作，而非主要依赖对话传递，从而实现了“对厚重状态的精细控制”。实验表明，AiScientist在两个互补基准测试（PaperBench和MLE-Bench Lite）上显著优于基线方法，消融研究进一步证实“文件即总线”协议是性能提升的关键驱动因素。主要结论是，长周期ML研究工程本质上是一个在持久项目状态上协调专门工作的系统问题，而非纯粹的局部推理问题。
