---
title: "Achieving Olympia-Level Geometry Large Language Model Agent via Complexity Boosting Reinforcement Learning"
authors:
  - "Haiteng Zhao"
  - "Junhao Shen"
  - "Yiming Zhang"
  - "Songyang Gao"
  - "Kuikun Liu"
  - "Tianyou Ma"
  - "Fan Zheng"
  - "Dahua Lin"
  - "Wenwei Zhang"
  - "Kai Chen"
date: "2025-12-11"
arxiv_id: "2512.10534"
arxiv_url: "https://arxiv.org/abs/2512.10534"
pdf_url: "https://arxiv.org/pdf/2512.10534v3"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Agent Architecture"
  - "Mathematical Reasoning"
  - "Tool Use"
  - "Reinforcement Learning"
  - "Agentic RL"
  - "Planning"
  - "Memory"
  - "Agent Evaluation"
relevance_score: 9.0
---

# Achieving Olympia-Level Geometry Large Language Model Agent via Complexity Boosting Reinforcement Learning

## 原始摘要

Large language model (LLM) agents exhibit strong mathematical problem-solving abilities and can even solve International Mathematical Olympiad (IMO) level problems with the assistance of formal proof systems. However, due to weak heuristics for auxiliary constructions, AI for geometry problem solving remains dominated by expert models such as AlphaGeometry 2, which rely heavily on large-scale data synthesis and search for both training and evaluation. In this work, we make the first attempt to build a medalist-level LLM agent for geometry and present InternGeometry. InternGeometry overcomes the heuristic limitations in geometry by iteratively proposing propositions and auxiliary constructions, verifying them with a symbolic engine, and reflecting on the engine's feedback to guide subsequent proposals. A dynamic memory mechanism enables InternGeometry to conduct more than two hundred interactions with the symbolic engine per problem. To further accelerate learning, we introduce Complexity-Boosting Reinforcement Learning (CBRL), which gradually increases the complexity of synthesized problems across training stages. Built on InternThinker-32B, InternGeometry solves 44 of 50 IMO geometry problems (2000-2024), exceeding the average gold medalist score (40.9), using only 13K training examples, just 0.004% of the data used by AlphaGeometry 2, demonstrating the potential of LLM agents on expert-level geometry tasks. InternGeometry can also propose novel auxiliary constructions for IMO problems that do not appear in human solutions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在解决国际数学奥林匹克（IMO）级别几何问题上的能力不足问题。研究背景是，尽管LLM智能体在数学和编程等领域已展现出强大的通用问题解决能力，甚至能借助形式化证明系统解决IMO难题，但在几何问题上，其潜力尚未被充分挖掘。几何问题通常证明步骤极长，不仅需要组合多种几何定理，更依赖于启发式线索薄弱、需要多次试错的创造性辅助构造。

现有方法的不足主要体现在：当前最先进的方法（如AlphaGeometry 2）主要依赖专家模型，这些模型通过大规模合成数据进行训练，并依赖符号引擎进行大规模搜索来寻找证明。这种方法数据需求极大，且本质上更偏向于数据驱动的搜索，而非类似人类专家的渐进式推理与试错学习。

因此，本文要解决的核心问题是：能否利用LLM智能体的交互与反思能力，构建一个更高效、更具泛化能力的模型来解决高难度几何问题？具体而言，论文试图克服几何证明中辅助构造的弱启发式难题，并减少对海量合成数据的依赖。为此，论文提出了InternGeometry，一个通过长程LLM-工具交互（包括提议、验证、反思）和动态记忆机制来逐步探索和积累几何性质，从而攻克难题的智能体。同时，为了高效训练该智能体，论文引入了复杂度提升强化学习框架，通过分阶段提升合成问题的复杂度来逐步培养模型解决专家级任务的能力。最终目标是构建一个仅需少量训练数据，就能达到甚至超越IMO金牌选手平均水平的几何问题求解LLM智能体。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：数学领域的强化学习智能体、课程学习在智能体中的应用，以及自动几何定理证明。

在数学强化学习智能体方面，现有工作主要分为两类：一类是基于非形式化证明的智能体（如OR、PR方法），利用Python等通用工具解决问题；另一类是基于交互式定理证明器（ITP）的智能体，在miniF2F等基准上表现优异。然而，这些研究很少专门针对几何问题。本文的InternGeometry填补了这一空白，专注于构建交互式几何证明智能体。

在课程学习方面，现有方法如Voyager依赖手动设计的课程，WebRL使用奖励模型自动评估任务复杂度，但大多局限于高度结构化的任务类型。本文提出的复杂度提升强化学习（CBRL）实现了完全自动化、可动态调整难度的大规模问题合成，尤其在处理高复杂度任务时更具灵活性和无偏性。

在自动几何定理证明领域，当前主流方法（如AlphaGeometry、SeedGeometry）属于专家模型，通常将问题分解为辅助构造预测和形式推理两个步骤，依赖大规模合成数据进行训练和搜索。近期也有研究探索使用大语言模型进行几何推理，但主要针对初级问题。本文的InternGeometry则首次构建了奖牌级别的LLM智能体，通过迭代提议与符号引擎交互，以极少的训练数据（仅AlphaGeometry 2的0.004%）实现了IMO级几何问题的求解，并能够提出人类解答中未出现的新颖辅助构造。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为InternGeometry的智能体来解决几何问题中启发式辅助构造能力弱的问题。其核心方法是一个结合了大型语言模型（LLM）与交互式符号证明引擎的迭代推理框架，并引入了复杂度提升强化学习（CBRL）进行高效训练。

**整体框架与主要模块**：
InternGeometry采用一个多轮交互的闭环架构。智能体（基于InternThinker-32B模型）在每一轮中执行“思考-行动-反馈”的循环：
1.  **思考（Think）**：基于当前问题描述和压缩后的历史信息，进行自然语言的链式思考（P_t）。
2.  **行动（Action）**：输出结构化的行动代码（A_t），使用领域特定语言（DSL）来指定几何构造、添加辅助点或提出待验证的命题。
3.  **执行与反馈**：行动代码被提交给一个基于Newclid开发的交互式几何证明引擎（名为\enginename）执行。引擎维护着几何配置、已知事实和证明状态，并返回执行结果（O_t）作为环境反馈。
4.  **动态记忆管理（𝔚）**：这是一个关键模块，负责压缩可能长达数百轮的交互历史（H_t）。它保留核心的行动输出和关键反馈，同时总结早期的详细交互，从而为智能体提供关于其行动历史与结果的精炼概述，极大地提升了处理长视野任务时的上下文效率。

**关键技术细节与创新点**：
1.  **长视野推理与防崩溃机制**：为解决长序列推理中可能出现的行动崩溃（如重复输出），论文设计了一种基于规则的拒绝采样方法（PassCheck）。它在推理时检查输出，避免出现与历史重复的行动、过长的无停止思考、无效行动或连续过多轮使用同类型行动等问题。
2.  **复杂度提升强化学习（CBRL）**：这是训练方法上的核心创新。训练过程始于在小规模合成数据上进行监督微调（SFT），使模型初步掌握任务范式。随后进入CBRL迭代循环：
    *   **课程学习**：CBRL的核心思想是动态控制训练任务的难度。论文将几何问题的复杂度（κ）定义为符号引擎（DDAR）所需的证明步数。在每一轮RL训练中，系统从数据合成管道𝔛中采样特定复杂度κ的问题。
    *   **奖励设计**：采用简单的二元奖励。轨迹的最终奖励（r）是结果奖励（r^o，问题完全解决为1，否则为0）与步骤有效性奖励（r^s）的逻辑与。步骤有效性奖励根据行动类型判定：对于命题验证步骤，若命题被引擎成功证明则r^s为1；对于辅助构造步骤，若构造被成功添加并最终用于证明问题，则r^s为1。
    *   **策略优化与难度调整**：使用基于GRPO的PPO算法进行策略优化，并包含KL散度正则化以防止策略偏离初始模型过多。在一轮训练后，系统会评估模型在当前难度下的平均绝对优势（A(X,y)），并据此更新复杂度κ（例如，向能产生最大平均绝对优势的难度水平调整），从而形成“学习-评估难度-提升难度”的闭环，使智能体能够循序渐进地掌握解决复杂问题所需的技能。
3.  **数据合成**：通过一个可控难度的数据合成管道为CBRL提供训练数据。该管道能够生成具有统计先验复杂度的几何问题，并利用引擎过滤有效的构造和目标，最终构建出难度（以证明步数衡量）分布符合训练需求的合成问题集。

综上所述，InternGeometry通过**交互式证明引擎与LLM智能体的紧密耦合**、**动态记忆管理**支持的超长序列交互、以及创新的**CBRL训练范式**，系统地解决了几何证明中辅助构造的启发式难题，最终使用极少量的训练数据（13K）达到了国际数学奥林匹克金牌级别的解题能力。

### Q4: 论文做了哪些实验？

实验设置方面，论文以InternThinker-32B为骨干模型构建了InternGeometry智能体。默认最大推理步数为200步，推理超参数为温度0.9和top-p 0.9。测试时采用pass@K=256的采样设置。

数据集与基准测试方面，主要测试集为IMO 50，包含2000年至2024年国际数学奥林匹克竞赛的所有几何问题。此外，还单独在IMO 2025的几何问题上进行了评估。对比方法选择了基于专家模型的最先进几何证明方法AlphaGeometry 2和SeedGeometry。

主要结果与关键指标如下：在IMO 50测试集上，InternGeometry解决了44道问题，超过了AlphaGeometry 2的42道和SeedGeometry的43道，且平均分超过了金牌得主平均分（40.9）。其训练数据仅需13K个示例，分别是AlphaGeometry 2（300M）和SeedGeometry（230M）的0.004%和0.006%，数据效率极高。在包含IMO 2025问题的51道题扩展集中，InternGeometry解决了45道。消融实验表明，长时程交互（最大步数）、慢思考（Slow Thinking）和上下文压缩（Context Compression）等组件对性能至关重要；移除长时程组件后，解决题数从44道分别降至35道、23道和20道。论文还引入了复杂度提升强化学习（CBRL），消融显示使用CBRL的性能（44/50）显著优于仅用简单数据（29/50）、仅用困难数据（24/50）或无课程安排（38/50）的设置。此外，研究分析了智能体与符号引擎的长时程交互效应，发现增加交互步数能显著提升证明成功率，且延长轨迹长度比单纯增加采样次数更有效。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其方法高度依赖符号引擎进行验证和反馈，这可能导致推理效率较低，且对引擎的准确性有严格要求。未来研究可探索更高效的交互机制，减少对符号引擎的调用次数，或集成轻量级验证模块以加速推理。此外，模型在非几何数学领域的泛化能力未经验证，可扩展至更广泛的数学问题，如代数或组合数学，以测试其通用性。从方法改进角度，CBRL的复杂度提升策略可进一步优化，例如引入自适应难度调整或结合课程学习，以更精细地控制训练过程。另外，动态内存机制虽支持多步交互，但可能引入冗余信息，未来可研究更智能的记忆压缩或检索方法，提升决策效率。最后，模型生成的辅助构造虽新颖，但可解释性有限，可结合可视化或自然语言解释增强其可理解性，促进人机协作求解。

### Q6: 总结一下论文的主要内容

本文提出了InternGeometry，这是首个达到国际数学奥林匹克（IMO）金牌水平的几何问题求解大语言模型（LLM）智能体。针对几何问题求解中辅助构造启发式弱、依赖大规模数据合成与搜索的挑战，论文通过设计长程交互与强化学习框架来克服。

核心方法包括：1）构建InternGeometry-DDAR符号引擎作为验证工具；2）设计智能体与引擎的长程交互机制，通过自然语言思考提出命题或辅助构造，用形式语言验证并反思反馈，并利用动态记忆管理探索历史；3）提出复杂度提升强化学习（CBRL）训练框架，通过多阶段课程学习，逐步提升合成问题的复杂度以高效训练模型。

实验表明，基于InternThinker-32B的InternGeometry仅使用1.3万训练样本（仅为AlphaGeometry 2数据量的0.004%），便在2000-2024年的50道IMO几何题中解出44题，超过金牌选手平均分（40.9）及AlphaGeometry 2（42分）。研究证实了长程试错交互对实现弱启发式到强启发式转换的关键作用，CBRL对训练收敛的促进效果，并展示了模型能够提出超越人类解答的新颖辅助构造，体现了LLM智能体在专家级几何任务上的潜力与创造性。
