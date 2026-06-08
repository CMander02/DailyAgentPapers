---
title: "OpenSkill: Open-World Self-Evolution for LLM Agents"
authors:
  - "Zhiling Yan"
  - "Dingjie Song"
  - "Hanrong Zhang"
  - "Wei Liang"
  - "Yuxuan Zhang"
  - "Yutong Dai"
  - "Lifang He"
  - "Philip S. Yu"
  - "Ran Xu"
  - "Xiang Li"
  - "Lichao Sun"
date: "2026-06-04"
arxiv_id: "2606.06741"
arxiv_url: "https://arxiv.org/abs/2606.06741"
pdf_url: "https://arxiv.org/pdf/2606.06741v1"
github_url: "https://github.com/OpenLAIR/OpenSkill"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Self-Evolution"
  - "Open-World Agent"
  - "Skill Acquisition"
  - "Verification Anchors"
  - "Transferable Skills"
  - "Agent Training"
  - "No-Supervision Learning"
relevance_score: 9.5
---

# OpenSkill: Open-World Self-Evolution for LLM Agents

## 原始摘要

Self-evolving agents requires adaptation after deployment, but existing approaches assume a usable learning loop, such as curated skills, successful trajectories, or verifier signals. Real open-world deployments may provide none of these, offering only a task prompt. In this work, we study open-world self-evolution, where an agent must build both its skills and its own verification signals from scratch, using open-world resources but no target-task supervision. We propose OpenSkill, a framework that bootstraps this loop: it acquires grounded knowledge and verification anchors from documentation, repositories, and the web, synthesizes them into transferable skills, and refines those skills against self-built virtual tasks grounded in the anchors rather than in target answers. The open world thus supplies both the knowledge to be learned and a supervision-independent practice environment, with target-task supervision reserved for final evaluation. Across three benchmarks and two target agents, OpenSkill attains the best automated pass rate while satisfying the no-supervision constraint. Analysis shows its skills transfer across models without model-specific adaptation, and its self-built verifier aligns with ground-truth outcomes despite never accessing them.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决开放世界中LLM智能体的自我进化问题，即智能体在部署后，仅凭一个任务提示和开放世界资源（如文档、代码库、网页等），**从零开始构建自己的技能和验证信号**，而完全不依赖任何目标任务的监督信号（如人工标注的技能、成功的轨迹、奖励函数或验证器输出）。

现有方法的不足在于它们都假设了一个可用的学习循环，例如依赖人工编写的技能、模型生成的知识、或从成功轨迹中蒸馏的技能，以及依赖任务级反馈或验证器输出来改进行为。然而，在真实的开放世界部署中，这些资源往往不可得，智能体无法获得任何初始技能或用于判断改进效果的验证器。这导致当前的自我进化方法在面临真实、开放、且只有任务提示的部署环境时，因缺乏构建高质量技能和可靠自我验证信号的能力而失效。

因此，本文要解决的核心问题是：**一个LLM智能体能否在不依赖任何目标任务监督的情况下，仅通过利用开放世界资源实现自我进化？**具体而言，智能体需要自主完成两个耦合的关键任务：一是从开放世界中获取知识并构建可迁移的技能；二是同时构建一个独立于目标答案的验证信号（即虚拟测试环境），用于在没有隐藏答案的情况下迭代优化这些技能。

### Q2: 有哪些相关研究？

基于论文内容，相关研究可分为以下几类：

1.  **自我进化/技能学习方法**：如Self-Gen、CoT、Skill Creator、AutoSkill、Memento等方法，它们通过反思、探索、蒸馏等方式积累技能。与本文的区别在于：这些方法或依赖于任务轨迹、成功解决方案或验证信号，或技能与模型绑定（如强化学习方法），不具备跨模型迁移性。**OpenSkill**则强调在无监督下从零开始构建技能，且技能是显式、可迁移的工件。

2.  **检索增强与开放世界知识利用**：如RAG、浏览器辅助、深度研究等智能体。它们检索信息以完成单一任务，而**OpenSkill**则将检索作为合成持久、可复用技能和构建自我验证信号的基石，而非仅用于即时回答。

3.  **无监督验证与自我评判**：之前工作有多路径聚合、自我反馈、LLM作为评判者，或在代码领域使用自生成测试。技能中心方法会在推理时合成技能并验证，或将技能与验证器共同进化。但这些信号仍依赖于模型自身先验或任务本身，存在监督泄露风险。**OpenSkill**通过创建基于开放世界事实的“虚拟任务”作为验证锚点，使验证信号完全独立于目标任务监督，从而避免了这一问题。

### Q3: 论文如何解决这个问题？

OpenSkill通过一个三阶段流水线解决开放世界自我进化问题，在无初始技能、演示、奖励或验证信号的情况下，仅利用任务提示和开放世界资源构建并优化技能。该方法的核心在于知识获取与自监督验证的分离，避免目标任务监督泄露。

整体框架包含三个阶段：
1. **开放世界知识获取**：基于任务描述，从文档、代码仓库、网页等开放资源中检索相关知识（如API文档、领域惯例）和验证知识（如数据集统计量、预期输出格式）。检索过程过滤基准名称等标识符，确保无目标监督泄露。
2. **虚拟任务驱动的技能优化**：首先，基于任务信息和检索知识生成结构化技能计划（指定技能架构和关键流程）。然后，LLM代理生成初始技能集，并进入迭代优化循环：在每轮中，技能在沙箱中执行，并由基于验证知识构建的虚拟测试套件（如pytest断言）进行评估。若未全通过，则诊断失败原因（实现错误或知识缺口），触发针对性检索补充知识，并据此修正技能。迭代最多3轮，直至虚拟测试全通过。
3. **零样本部署**：将最终技能集作为显式工件（而非模型权重）部署到目标代理，直接用于执行目标任务，并通过隐藏的真实测试集评估性能。由于技能是便携的，可在不同模型间迁移。

创新点包括：用开放世界知识（而非模型参数知识）构建技能；以独立可验证的虚拟测试（而非目标测试）作为优化代理；通过诊断驱动的迭代修正实现自监督闭环，且全程不接触真实测试集。

### Q4: 论文做了哪些实验？

论文在三个基准上进行了实验：SkillsBench（11个任务领域）、SocialMaze（社交推理）和ScienceWorld（交互式科学）。实验使用两个目标智能体：Opus 4.6 (Claude Code) 和 GPT 5.2 (Codex)。对比方法包括7个闭源基线：No Skill、Self-Gen、CoT、Skill Creator、AutoSkill、Memento，以及在ScienceWorld上额外对比了SkillNet，并设置了人工上限作为参考。所有方法均遵循开放世界协议，测试集在构建时隐藏，仅在最终评估时使用。

主要结果：在SkillsBench上，OpenSkill在两个智能体上均取得最佳自动化通过率——Opus 4.6为43.6%（比最强基线Skill Creator高8.9个百分点），GPT 5.2为42.1%（比最强基线CoT高8.8个百分点），仅比人工上限（44.5%/44.8%）低1-3个百分点。在Opus 4.6上，OpenSkill在11个领域中有8个取得最佳或并列最佳，在Health（69.6%）和Software（59.9%）领域提升显著。在SocialMaze上，OpenSkill达到82.7%（Opus）和70.7%（GPT）；在ScienceWorld上达到90.0%（Opus）和85.3%（GPT），均为所有自动化方法中的最优结果。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：一是开放世界资源（如网页、代码库）可能包含噪声、过时或矛盾信息，导致知识获取质量不稳定；二是自建虚拟任务可能无法匹配真实目标任务的难度分布，若任务过于简单会高估技能效果，若通过隐藏答案或验证器行为构建则可能引入目标任务监督；三是相比封闭世界场景，开放世界流程增加了计算成本和延迟。未来探索方向包括：设计更鲁棒的知识溯源和验证机制，如引入多源交叉验证或动态优先级排序；研究虚拟任务难度自适应调整策略，例如基于技能执行反馈逐步接近真实分布；探索成本优化方案，如通过知识蒸馏减少每次技能合成所需的数据量，或利用预训练模型减少开源资源依赖。此外，技能迁移虽已初步验证，但其在跨领域、跨语言场景的泛化能力仍需系统评估。

### Q6: 总结一下论文的主要内容

这篇论文研究了大语言模型智能体的开放世界自进化问题。在真实部署场景中，智能体无法获得精心设计的技能、成功轨迹或验证信号，只能依赖任务提示。作者提出OpenSkill框架，通过从文档、代码库和网络中获取基础知识和验证锚点，将其合成为可迁移技能，并基于自构建的虚拟任务（而非目标任务答案）进行技能优化。在三个基准测试和两个目标智能体上，OpenSkill在满足无监督约束条件下取得了最佳自动通过率。分析表明，其技能无需特定模型适配即可跨模型迁移，且自构建的验证器与未接触的真实结果高度一致。该工作为部署后持续进化的智能体开发提供了无监督学习的新路径。
