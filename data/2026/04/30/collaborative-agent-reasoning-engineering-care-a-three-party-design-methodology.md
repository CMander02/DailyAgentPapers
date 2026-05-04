---
title: "Collaborative Agent Reasoning Engineering (CARE): A Three-Party Design Methodology for Systematically Engineering AI Agents with Subject Matter Experts, Developers, and Helper Agents"
authors:
  - "Rahul Ramachandran"
  - "Nidhi Jha"
  - "Muthukumaran Ramasubramanian"
date: "2026-04-30"
arxiv_id: "2604.28043"
arxiv_url: "https://arxiv.org/abs/2604.28043"
pdf_url: "https://arxiv.org/pdf/2604.28043v1"
categories:
  - "cs.AI"
tags:
  - "Agent设计方法论"
  - "LLM Agents"
  - "结构化工程化"
  - "人机协作"
  - "科学Agent"
  - "NASA"
  - "Earth Science"
relevance_score: 7.5
---

# Collaborative Agent Reasoning Engineering (CARE): A Three-Party Design Methodology for Systematically Engineering AI Agents with Subject Matter Experts, Developers, and Helper Agents

## 原始摘要

We present Collaborative Agent Reasoning Engineering (CARE), a disciplined methodology for engineering Large Language Model (LLM) agents in scientific domains. Unlike ad-hoc trial-and-error approaches, CARE specifies behavior, grounding, tool orchestration, and verification through reusable artifacts and systematic, stage-gated phases. The methodology employs a three-party workflow involving Subject-Matter Experts (SMEs), developers, and LLM-based helper agents. These helper agents function as facilitation infrastructure, transforming informal domain intent into structured, reviewable specifications for human approval at defined gates. CARE addresses the "jagged technological frontier", characterized by uneven LLM performance, by bridging the gap between novice and expert analysts regarding domain constraints and verification practices. By generating concrete artifacts, including interaction requirements, reasoning policies, and evaluation criteria, CARE ensures agent behavior is specifiable, testable, and maintainable. Evaluation results from a scientific use case demonstrate that this stage-gated, artifact-driven methodology yields measurable improvements in development efficiency and complex-query performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

该论文聚焦于大型语言模型（LLM）驱动的智能体（Agent）在科学和工程领域中工程化过程缺乏系统性和可重复性的问题。当前，构建LLM Agent主要依赖于“试错法”的提示词迭代，这种做法产生的问题是：Agent的行为（包括推理、工具使用、领域约束等）难以被明确指定、测试和长期维护；同时，由于LLM性能的不均匀性（即“锯齿状技术前沿”），专家和新手在利用Agent时的效果差距巨大。论文指出，当Agent设计依赖于临时性的提示词调整时，很容易产生“静默失败”（即输出看似合理但违背领域规则）和性能退化。因此，论文的核心目标是提出一种结构化的、阶段门控的工程方法论——CARE，通过将SME（领域专家）、开发者和LLM辅助Agent三方协作引入设计流程，将非正式的领域意图转化为显式、可审查、可复用的工件，使得Agent的行为可指定、可测试和可维护，从而缩小专家与新手的差距，提升Agent在科学数据发现等知识密集型任务中的可靠性和性能。

### Q2: 有哪些相关研究？

相关研究可以归纳为以下几个方向：1) **LLM在知识工作中的能力与局限**：Dell'Acqua等人的工作（[1]）通过实验证实LLM性能不均匀，且用户技能（如任务分解和验证能力）显著影响产出质量，这直接构成了CARE的动机——通过结构化工程来降低对个体用户技能的依赖。2) **Agentic系统实现**：已有大量工作证明通过任务分解、迭代求精和工具使用可以实现多步骤工作流（如[4][5][6]），但这些系统主要关注可行性，没有系统性地说明如何“设计”和“工程化”这些Agent行为。3) **提示词工程模式**：White等人（[2]）提出了提示模式目录，但这些模式通常应用于非固定的试错式迭代，缺乏明确的工件和门控机制来确保可维护性和可审查性。4) **需求工程与参与式设计**：传统软件工程方法已被用于知识捕获，但LLM Agent的行为会随模型版本、提示更新等变化，传统方法无法直接应对这种“确定性不足”。CARE在这些基础上，借鉴了加速知识发现（AKD）框架（[7]）中利用AI增强科学家认知的思想，并将其前置到Agent的设计工程阶段，使用LLM辅助Agent作为“促进基础设施”来加速需求捕获和工件生成。本文的独特贡献在于提出了一个专门针对LLM Agent的三方协作、工件驱动的系统工程方法论，并提供了具体的NASA案例验证。

### Q3: 论文如何解决这个问题？

CARE（Collaborative Agent Reasoning Engineering）提出了一种“阶段门控”的工程方法论，将Agent构建重构为三方协作的工程过程：领域专家（SME）、开发者和LLM辅助Agent共同工作，通过生成和审查显式的（而非隐式的）工件来指定Agent行为。核心流程分为五个阶段：1) **范围与分解**：定义目标工作流、用户和约束，将Agent拆解为交互策略、领域接地、工具编排和评估/验证四个设计目标。2) **关键信息捕获**：通过辅助Agent的引导性问题，系统地收集工具信息、上下文需求（如检索策略、记忆边界）和输出格式要求。3) **推理策略与护栏**：显式规定Agent的交互策略（如何分解任务、处理不确定性）和安全行为（禁止行为、升级规则）。4) **提示架构与工具编排实现**：根据批准的工件，利用提示模式目录生成工程化的提示词，包括角色设定、规划提示、验证提示和工具使用模板。5) **基准测试与验证**：定义如何构建真实场景的基准测试（包括失败模式目录和判断标准）。该方法的创新在于：引入了“辅助Agent”作为促进基础设施，它们通过在每个阶段提出结构化的引导性问题，将非正式的SME意图转化为清晰、一致的Markdown工件，供人审查和批准。工件版本化（存储在GitHub中）以支持可审计性和长期维护。人类（SME和开发者）在阶段门控处保留最终批准权，从而确保领域真相和实现可行性始终由人类掌控。

### Q4: 论文做了哪些实验？

论文通过一个NASA地球科学数据发现Agent的案例研究来评估CARE。该Agent的任务是将自然语言科学数据需求转化为对NASA通用元数据仓库（CMR）API的检索步骤，返回数据集概念ID。为了隔离方法论本身的影响，实验比较了两个Agent：**cmr_care_v1**（基于CARE工件构建）和 **cmr_simple**（基线Agent，使用相同的底层模型和CMR工具接口，但不采用CARE的结构化设计过程）。评估采用“双门”基准测试策略：**第一门**（合成基准）快速生成621个可自动化的查询，每个查询针对一个特定数据集，主要指标为Recall@1；**第二门**（黄金基准）包含43个SME手动构建的与真实科研论文关联的查询，评估Recall@1、Recall@3和Recall@5。主要结果显示：在合成基准上，CARE Agent的Recall@1为71.7%，显著高于基线的69.1%。在SME黄金基准上，CARE Agent在Recall@5上达到27.2%，高于基线的20.2%；在Recall@3上也优胜（22.6% vs 15.6%）；仅在Recall@1上略低（7.8% vs 9.7%）。论文指出，SME通常关注top 5结果，因此Recall@5是更有意义的指标。这些结果表明，CARE在快速合成场景和专家验证场景下均能带来可测量的检索性能提升。

### Q5: 有什么可以进一步探索的点？

论文自身提出了多个明确的局限性，并指向后续探索方向：1) **多领域复制与迁移性评估**：当前案例仅覆盖NASA地球科学数据发现，未来需在多个科学和工程领域（如生物信息学、气象学、材料科学等）复制CARE流程，评估其在不同查询分布和工具生态下的泛化能力。2) **基准泄漏与过度拟合风险**：CARE的工件迭代可能无意中“教给测试集”，特别是辅助Agent引导的问题可能有偏差。未来需设计“留出法”验证（即使用在CARE流程中从未见过的基准）来评估方法的稳健性。3) **人工与辅助Agent的质量依赖**：CARE的有效性高度依赖于辅助Agent提问的完整性和SME/开发者的经验。未来需研究如何量化“辅助Agent质量”对其产出工件质量的影响，以及如何优化辅助Agent的提示来减少遗漏。4) **长期维护与模型漂移**：LLM和工具的更新可能改变Agent行为，未来可探索如何利用CARE的版本化工件和阶段门控自动化定期再验证流程。

### Q6: 总结一下论文的主要内容

该论文提出了CARE（Collaborative Agent Reasoning Engineering），一种结构化的、阶段门控的LLM Agent工程方法论。核心思路是：Agent构建不应是试错式提示迭代，而应是SME、开发者和LLM辅助Agent三方协作的工程过程，通过生成显式、可审查的工件（如交互策略、领域接地规范、工具编排计划和评估标准）来指定Agent行为。论文将Agent解构为交互策略、领域接地、工具编排和评估/验证四个设计目标，并将其映射到CARE的五个阶段（范围、信息捕获、推理与护栏、提示实现、基准测试）中。辅助Agent作为促进基础设施，负责将非正式的SME意图转化为结构化工件，而人类在阶段门控处保留批准权。通过NASA地球科学数据发现Agent案例，实验表明CARE设计的Agent在Recall@1（合成基准）和Recall@5（专家黄金基准）上均优于相同模型和工具访问的基线，验证了该方法能提升检索性能和工程可维护性。论文强调CARE是一种可重复、可审计、可维护的工程规范，而不只是一个运行时框架。
