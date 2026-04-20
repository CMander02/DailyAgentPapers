---
title: "Mind DeepResearch Technical Report"
authors:
  - "MindDR Team"
  - "Li Auto Inc"
date: "2026-04-16"
arxiv_id: "2604.14518"
arxiv_url: "https://arxiv.org/abs/2604.14518"
pdf_url: "https://arxiv.org/pdf/2604.14518v2"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent System"
  - "Agent Training Pipeline"
  - "Agent Architecture"
  - "Tool Use"
  - "Benchmark"
  - "Web Search"
  - "Data Synthesis"
  - "Reinforcement Learning"
  - "Preference Alignment"
  - "Deployment"
relevance_score: 8.0
---

# Mind DeepResearch Technical Report

## 原始摘要

We present Mind DeepResearch (MindDR), an efficient multi-agent deep research framework that achieves leading performance with only ~30B-parameter models through a meticulously designed data synthesis and multi-stage training pipeline. The core innovation of MindDR lies in a collaborative three-agent architecture (Planning Agent, DeepSearch Agent, and Report Agent) and a four-stage agent-specialized training pipeline comprising SFT cold-start, Search-RL, Report-RL and preference alignment. With this regime, MindDR demonstrates competitive performance even with ~30B-scale models. Specifically, MindDR achieves 45.7% on BrowseComp-ZH, 42.8% on BrowseComp, 46.5% on WideSearch, 75.0% on xbench-DS, and 52.5 on DeepResearch Bench, outperforming comparable-scale open-source agent systems and rivaling larger-scale models. MindDR has been deployed as an online product in Li Auto. Furthermore, we introduce MindDR Bench, a curated benchmark of 500 real-world Chinese queries from our internal product user interactions, evaluated through a comprehensive multi-dimensional rubric system rather than relying on a single RACE metric. On MindDR Bench, MindDR achieves a state-of-the-art score of 51.8.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前深度研究智能体（Deep Research Agent）面临的核心瓶颈：在保持高性能的同时，大幅降低模型训练和推理的成本，以实现高效、实用的用户体验。

研究背景是，随着大语言模型从对话工具演变为能规划、推理、使用外部工具的自主智能体，深度研究智能体已成为一个极具代表性的产品范式。以Google和OpenAI的系统为代表，它们展现了在科学研究和金融分析等领域接近人类水平的能力。然而，现有方法，尤其是开源方案，存在显著不足：顶尖系统通常依赖参数量巨大（例如超过1000亿）的基础模型和计算成本高昂的训练范式（如大规模持续预训练）。在推理时，复杂的多步搜索和工具调用会导致极高的令牌消耗和系统延迟，且不加优化的搜索可能产生大量冗余信息，反而稀释关键发现，损害用户体验。

因此，本文要解决的核心问题是：**如何通过低成本的训练和推理，使用小规模模型（约300亿参数）来实现领先的深度研究性能和优秀的用户体验**。为此，论文提出了MindDR框架，其核心创新在于通过**推理阶段的任务分解**（规划、深度搜索、报告生成三智能体协作架构）和**训练阶段的针对性优化**（包含SFT冷启动、搜索强化学习、报告强化学习和偏好对齐的四阶段训练流程），在多个基准测试上达到了与更大规模模型相竞争的性能，并已成功部署为在线产品。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕深度研究智能体的架构、训练与评估展开，可分为方法类、应用类和评测类。

在方法类研究中，相关工作聚焦于提升智能体的检索推理与报告生成能力。例如，Tongyi DeepResearch 提出了端到端的智能体训练优化架构；MiroThinker 通过强化学习实现“交互式扩展”，训练模型处理数百次工具调用；WebSailor 专注于降低不确定性的网络导航，而 WebWeaver 探索了双智能体架构用于开放式报告生成。这些工作大多采用整体端到端的强化学习目标来优化检索准确性，但训练复杂度高。MindDR 与它们的关键区别在于，提出了一个协作的三智能体架构（规划、深度搜索、报告）和四阶段专项训练流程，并引入了轻量级的步级信用分配机制，从而在仅约300亿参数规模下实现了高效训练与竞争性性能。

在应用类研究中，现有系统如 Gemini Deep Research 和 OpenAI Deep Research 展示了在复杂调查任务上的近人类性能，但其闭源性质限制了可复现性。开源替代方案如 Nanbeige4.1-3B 证明了小模型通过专项训练也能具备竞争力。MindDR 与这些工作的关系是提供了另一个高效的开源多智能体框架，并已作为在线产品在理想汽车部署，体现了其实用价值。

在评测类研究中，传统评估主要依赖 DeepResearch Bench 的 RACE 评分标准（包括全面性、洞察力等）。其他多维评估框架如 WritingBench、ResearchRubrics 和 DEER 也被提出，用于基于大模型即评委的可靠评估。MindDR 与这些工作的联系是引入了自行构建的 MindDR Bench 基准，该基准包含500个真实中文查询并使用多维评分体系，而非单一 RACE 指标。在此基础上，MindDR 通过基于 RACE 标准的奖励塑造和专门的偏好对齐阶段，直接优化报告的信息质量和用户体验，以应对现有模型在超长上下文下全局逻辑结构和事实保真度方面的不足。

### Q3: 论文如何解决这个问题？

论文通过一个精心设计的多智能体协作架构和分阶段训练流程来解决高效深度研究的问题。其核心方法围绕一个由三个功能智能体（规划智能体、深度搜索智能体、报告智能体）组成的推理管道，以及一个包含四个阶段的专业化训练管道。

在整体框架上，推理管道采用紧密耦合的多智能体协作。用户查询首先由**规划智能体**处理，进行意图分析和任务分解，生成结构化的子任务规范。每个子任务被分配给一个独立的**深度搜索智能体**实例并行执行。该智能体采用ReAct风格的循环，迭代调用搜索工具进行多源检索、证据整合和中间推理，并维护一个**扩展思维链（XoT）** 作为跨智能体交互的共享推理记忆。最后，**报告智能体**接收所有子报告，生成层级大纲，并进行全局信息聚合与结构化组织，输出格式规范的Markdown研究报告。**内存机制**（包括XoT内存和工具调用内存）是关键技术，它使下游智能体能够访问完整的推理轨迹和信息来源，确保报告的可追溯性和准确性。

训练管道是另一大创新，它遵循奖励可处理性、能力依赖性和数据效率三原则，将复杂的端到端优化分解为四个渐进阶段：
1.  **监督微调（SFT）阶段**：提供行为冷启动，通过模仿专家轨迹，建立工具调用、ReAct格式遵循和多轮推理的基础能力。
2.  **搜索强化学习（Search-RL）阶段**：使用在线RL和真实工具执行，优化深度搜索智能体的长程推理和行动决策。采用统一的GRPO/GSPO框架，并动态调度奖励（从工具调用正确性，到过程级实体覆盖，再到结果级答案准确性），实现渐进式能力提升。
3.  **报告强化学习（Report-RL）阶段**：针对报告智能体的长文本生成质量进行优化。利用基于RACE评估准则的LLM-as-Judge进行奖励，优化报告的全面性、可读性、洞察力和指令遵循，并辅以基于规则的引用和格式奖励。
4.  **偏好对齐阶段**：采用基于策略的自改进框架（结合DPO和Self-SFT），对齐最终报告质量与人类期望，解决时间准确性、表格格式等用户体验问题，同时避免灾难性遗忘。

这种架构和训练设计的关键创新在于：1）通过三智能体分工与XoT内存实现高效、可追溯的深度研究流程；2）通过四阶段课程学习，将复杂的多目标优化问题分解为可处理的子问题，使用针对性的算法和数据，在仅约300亿参数模型上实现了领先性能。

### Q4: 论文做了哪些实验？

论文的实验设置围绕其提出的多智能体深度研究框架MindDR展开，通过一个四阶段的智能体专项训练流程（SFT冷启动、Search-RL、Report-RL和偏好对齐）进行。实验使用了混合数据集，包括基于知识图谱（百度百科和英文维基百科）合成的多跳推理查询，以及从理想汽车在线产品用户交互日志中挖掘的真实用户查询，两者按比例混合以平衡可控性和生态效度。

在基准测试方面，论文在多个公开基准上评估性能，包括BrowseComp-ZH、BrowseComp、WideSearch、xbench-DS和DeepResearch Bench。此外，论文还专门引入了自建的MindDR Bench基准，该基准包含500个从真实用户日志中筛选的中文深度研究查询，覆盖汽车、旅行、科技、金融等16个领域，并采用了一个细粒度的多维评估系统（涵盖推理轨迹、工具调用、大纲生成和报告生成四个模块）而非单一的RACE分数进行评估。

对比方法方面，论文主要与规模相当的开源智能体系统以及更大规模的模型进行性能比较。

主要结果方面，MindDR仅使用约300亿参数的模型就取得了领先性能：在BrowseComp-ZH上达到45.7%，在BrowseComp上达到42.8%，在WideSearch上达到46.5%，在xbench-DS上达到75.0%，在DeepResearch Bench上达到52.5分。在自建的MindDR Bench上，MindDR取得了51.8分的先进水平。这些结果表明，其性能优于同等规模的开源系统，并能与更大规模的模型竞争。关键数据指标包括上述各基准的具体得分，以及长上下文数据增强后128K上下文格式正确率从72%提升至94%。

### Q5: 有什么可以进一步探索的点？

该论文提出的MindDR框架在效率和性能上取得了显著成果，但其局限性和未来探索方向仍值得深入。首先，框架高度依赖精心设计的数据合成与多阶段训练流程，这可能导致泛化能力受限，未来可研究如何减少对合成数据的依赖，增强在多样化、未见过查询上的鲁棒性。其次，虽然30B参数模型已表现出色，但智能体间的协作机制（如规划、搜索、报告代理）可能仍有优化空间，例如引入动态角色调整或更细粒度的知识共享机制，以提升复杂任务下的协同效率。此外，评估基准MindDR Bench虽聚焦中文场景，但覆盖领域和查询类型可能有限，未来可扩展至多语言、跨文化语境，并探索更全面的评估维度（如创造性、可解释性）。从技术角度看，结合大模型的前沿进展（如思维链、自我反思）可能进一步提升搜索深度与报告质量。最后，作为在线产品，实际部署中的实时性、成本控制与用户交互反馈闭环尚未充分讨论，这些工程与实践层面的优化也是关键探索方向。

### Q6: 总结一下论文的主要内容

本文提出了MindDR，一个高效的多智能体深度研究框架，其核心在于通过精心设计的数据合成与多阶段训练流程，仅使用约300亿参数规模的模型即实现了领先的性能。MindDR的主要创新包括一个协作的三智能体架构（规划智能体、深度搜索智能体、报告智能体）和一个专为智能体设计的四阶段训练流程（SFT冷启动、搜索强化学习、报告强化学习、偏好对齐）。该方法将复杂的深度研究任务在推理阶段分解给不同智能体并行执行，提升了效率并缓解了长上下文处理负担；在训练阶段则针对不同智能体的职责进行定向优化，例如通过搜索强化学习显著提升搜索效率并减少冗余令牌消耗。实验表明，MindDR在BrowseComp、WideSearch、DeepResearch Bench等多个基准测试中超越了同类规模的开源系统，并与更大规模的模型性能相当。此外，论文还引入了基于真实用户查询构建的MindDR Bench评估基准及一套多维度的综合评估体系。MindDR已作为在线产品在理想汽车部署，证明了其在实际应用中的有效性与高效性。
