---
title: "Mind DeepResearch Technical Report"
authors:
  - "MindDR Team"
  - "Li Auto Inc"
date: "2026-04-16"
arxiv_id: "2604.14518"
arxiv_url: "https://arxiv.org/abs/2604.14518"
pdf_url: "https://arxiv.org/pdf/2604.14518v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent System"
  - "Agent Training Pipeline"
  - "Data Synthesis"
  - "Reinforcement Learning"
  - "Web Agent"
  - "Benchmark"
  - "Chinese Language Agent"
relevance_score: 8.0
---

# Mind DeepResearch Technical Report

## 原始摘要

We present \textbf{Mind DeepResearch (MindDR)}, an efficient multi-agent deep research framework that achieves leading performance with only \textasciitilde30B-parameter models through a meticulously designed data synthesis and multi-stage training pipeline. The core innovation of MindDR lies in a collaborative three-agent architecture (Planning Agent, DeepSearch Agent, and Report Agent) and a four-stage agent-specialized training pipeline comprising SFT cold-start, Search-RL, Report-RL and preference alignment. With this regime, MindDR demonstrates competitive performance even with \textasciitilde30B-scale models. Specifically, MindDR achieves 45.7\% on BrowseComp-ZH, 42.8\% on BrowseComp, 46.5\% on WideSearch, 75.0\% on xbench-DS, and 52.5 on DeepResearch Bench, outperforming comparable-scale open-source agent systems and rivaling larger-scale models. MindDR has been deployed as an online product in Li Auto. Furthermore, we introduce \textbf{MindDR Bench}, a curated benchmark of 500 real-world Chinese queries from our internal product user interactions, evaluated through a comprehensive multi-dimensional rubric system rather than relying on a single RACE metric. On MindDR Bench, MindDR achieves a state-of-the-art score of 51.8.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度研究智能体（Deep Research Agent）在实用化过程中面临的核心瓶颈：高昂的训练与推理成本。随着大语言模型从对话工具演变为能规划、推理、使用外部工具的自主智能体，深度研究智能体已成为一个重要的产品范式。然而，现有先进系统通常依赖于参数量巨大的基础模型（如>100B参数）和昂贵的训练范式（如大规模持续预训练），导致训练成本极高。在推理时，复杂的多步检索和长程推理会消耗大量计算资源，增加延迟和令牌消耗，并可能因上下文过长而稀释关键信息，损害用户体验。

现有开源努力虽有一定进展，但未能有效平衡性能与成本。因此，本文的核心问题是：**如何通过低成本的训练和推理，使用小规模模型（约30B参数）实现领先的深度研究性能和优异的用户体验**。

为此，论文提出了MindDR框架，其核心创新在于通过**推理阶段的任务分解**和**训练阶段的针对性优化**来解决上述问题。具体而言，在推理时采用规划、深度搜索和报告生成的三智能体协作架构，实现并行搜索与上下文隔离，提升效率；在训练时设计包含SFT冷启动、搜索强化学习、报告强化学习和偏好对齐的四阶段专用训练流程，避免昂贵的端到端训练，从而以较小模型规模达到与大模型相媲美的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕深度研究智能体的构建、训练与评估展开，可分为方法类、应用类与评测类。

在方法类研究中，现有工作聚焦于数据合成与信用分配。数据合成方面，知识图谱驱动方法（如WebSailor、DeepDive）能生成逻辑一致的数据，但覆盖有限；智能体模拟方法（如MiroThinker、Cognitive Kernel-Pro）提升了任务真实性，但计算成本高且难以区分关键检索步骤。信用分配方面，轨迹级强化学习（RL）方法奖励信号均匀，无法优化搜索效率；步级方法（如基于PPO或分支采样的ARPO、TreeRL）虽能提供细粒度监督，但依赖昂贵评论家模型或面临采样复杂度问题。本文的MindDR框架通过轻量级步级信用分配机制，在无需评论家或指数采样的前提下实现细粒度优势估计，从而同时优化检索准确性与搜索效率。

在应用类研究中，已有系统展示了不同架构与训练范式。专有系统（如Gemini Deep Research、OpenAI Deep Research）性能接近人类但不开源。开源替代方案中，Tongyi DeepResearch提出了端到端优化架构；MiroThinker通过RL训练模型处理大量工具调用；WebSailor专注于降低不确定性的网页导航；WebWeaver探索了开放式报告生成的双智能体架构；Nanbeige4.1-3B则证明了小模型通过专门训练也能具备竞争力。这些系统大多采用单一端到端RL目标优化检索准确性，训练复杂。本文则设计了协作的三智能体架构（规划、深度搜索、报告）与四阶段专业化训练流程（SFT冷启动、Search-RL、Report-RL、偏好对齐），以更高效的方式实现竞争性能。

在评测类研究中，评估框架与奖励设计是关键。经典评估采用RACE评分标准（涵盖全面性、洞察力等），其他多维评分框架（如WritingBench、ResearchRubrics、DEER）也支持沿事实准确性、结构连贯性等维度的可靠评估，并为RL算法提供奖励信号。然而，现有模型在超长上下文下的全局逻辑结构与事实保真度仍有不足，且较少纳入人类偏好反馈。本文为此引入了MindDR Bench基准（包含500个真实中文查询，采用多维评分系统），并通过基于RACE标准的奖励塑造与专门的偏好对齐阶段，直接优化报告的信息质量与用户体验。

### Q3: 论文如何解决这个问题？

论文通过设计一个高效的多智能体深度研究框架（MindDR）来解决复杂研究任务的问题，其核心方法、架构设计和关键技术如下：

**整体框架与主要模块**：MindDR采用一个紧密耦合的双组件架构。推理端是一个三智能体协作的流水线，包括**规划智能体**（负责意图分析和任务分解）、**深度搜索智能体**（以ReAct风格循环执行多源检索与推理）和**报告智能体**（进行全局信息聚合与结构化报告生成）。这三个智能体通过一个共享的**记忆机制**进行协调，该机制包含**扩展思维链（XoT）内存**和**工具调用内存**。XoT内存将推理轨迹跨智能体交互进行扩展，使得下游智能体（如报告智能体）能访问完整的检索信息溯源，从而生成更可信和依据充分的报告。

**四阶段训练流水线**：为解决多智能体系统所需多样能力（工具使用、多步推理、长文本生成、主观偏好对齐）的协同优化难题，论文提出了一个分阶段的课程学习训练管道，包含四个关键阶段：
1.  **监督微调（SFT）冷启动**：通过行为克隆专家轨迹，建立工具调用、格式遵循和多轮推理的基础能力，为后续强化学习提供稳定的策略起点。
2.  **搜索导向强化学习（Search-RL）**：使用在线强化学习（GRPO/GSPO框架）优化深度搜索智能体的长程推理和行动决策能力。其创新点在于**动态奖励调度**：奖励信号从工具调用正确性，渐进到过程级实体覆盖率，再到结果级答案准确性，从而实现能力的渐进式获取。
3.  **报告导向强化学习（Report-RL）**：专门优化报告智能体的长文本生成质量。使用基于RACE评估准则的LLM-as-Judge进行多维度（全面性、可读性、洞察力、指令遵循）优化，并辅以基于规则的引用和格式奖励。
4.  **偏好对齐**：采用基于策略的自改进框架（结合DPO和Self-SFT），对齐最终报告质量与人类期望，解决时间正确性、表格格式等用户体验问题，同时避免灾难性遗忘。

**核心创新点**：
1.  **协作式三智能体架构与XoT内存**：通过分工明确的智能体和跨交互的扩展思维链，实现了复杂研究任务的高效分解与证据整合。
2.  **分阶段、解耦的训练课程**：将端到端的复杂优化问题分解为四个目标明确的阶段，遵循奖励可处理性、能力依赖性和数据效率三大原则，有效解决了多目标联合优化中的信用分配难题。
3.  **动态奖励调度与训练平衡策略**：在Search-RL阶段引入动态奖励系数调整，平滑过渡不同能力目标；在SFT阶段精心设计数据课程和基于长上下文格式正确性的早停准则，在格式遵循与策略探索性之间取得最优平衡，使得约300亿参数的模型也能达到领先性能。

### Q4: 论文做了哪些实验？

论文在多个基准测试上进行了实验，评估了MindDR框架的性能。实验设置基于其提出的四阶段训练流程（SFT冷启动、Search-RL、Report-RL和偏好对齐），使用约30B参数的模型。

使用的数据集和基准测试包括：BrowseComp-ZH（中文网页浏览理解）、BrowseComp（英文网页浏览理解）、WideSearch（广泛搜索）、xbench-DS（深度搜索基准）以及作者新提出的MindDR Bench。MindDR Bench包含500个来自产品用户交互的真实中文查询，采用多维评估标准而非单一的RACE指标。

对比方法包括同规模的开源智能体系统以及一些更大规模的模型。

主要结果及关键数据指标如下：MindDR在BrowseComp-ZH上达到45.7%，在BrowseComp上达到42.8%，在WideSearch上达到46.5%，在xbench-DS上达到75.0%，在DeepResearch Bench上达到52.5分。这些成绩超越了可比规模的开源系统，并与更大规模模型相媲美。在自建的MindDR Bench上，MindDR取得了51.8分的先进水平得分。实验结果表明，通过精心设计的多智能体架构和分阶段训练，即使使用较小规模模型也能实现有竞争力的深度研究性能。

### Q5: 有什么可以进一步探索的点？

该论文的框架在模型规模受限（~30B参数）下取得了显著性能，但其局限性和未来探索方向值得深入。首先，其多智能体架构（规划、深度搜索、报告）的协同机制和内部决策过程仍是一个“黑箱”，未来可研究更透明的协作机制，例如引入可解释的通信协议或动态角色切换机制，以提升系统的可控性和可靠性。其次，训练流程依赖多阶段强化学习和偏好对齐，但合成数据的质量和多样性可能限制泛化能力；未来可探索更高质量的真实用户交互数据注入，或采用课程学习策略逐步提升任务复杂度。此外，评估基准虽覆盖多维度，但主要针对中文场景；未来需构建跨语言、跨文化领域的基准测试，并引入对事实一致性、推理链可信度等细粒度指标的评估。最后，在线部署中的实时性能优化和持续学习机制未充分探讨，可研究轻量级增量学习或模型蒸馏技术，以在资源受限环境下保持长期适应性。

### Q6: 总结一下论文的主要内容

该论文提出了MindDR，一个高效的多智能体深度研究框架，其核心在于通过精心设计的数据合成与多阶段训练流程，仅使用约300亿参数的模型即实现了领先性能。论文定义的核心问题是：如何在低成本训练和推理下，使用较小模型实现优异的深度研究性能与用户体验。

方法上，MindDR采用了两大创新。在推理阶段，设计了由规划智能体、深度搜索智能体和报告智能体组成的协同三智能体架构，实现了任务分解与并行执行，提升了效率。在训练阶段，提出了一个四阶段专业化训练流程：包括用于行为冷启动的监督微调、专门优化搜索智能体长程推理与搜索效率的Search-RL、专门优化报告智能体信息冲突解决与报告质量的Report-RL，以及基于人类反馈的偏好对齐。

主要结论显示，MindDR在多个基准测试（如BrowseComp、DeepResearch Bench）上超越了同规模开源系统，并与更大规模模型相媲美，例如在DeepResearch Bench上达到52.5分。此外，论文还贡献了MindDR Bench，一个包含500个真实中文查询的新基准及多维评估体系。该框架已在理想汽车产品中部署，证明了其实际应用价值。
