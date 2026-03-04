---
title: "BeyondSWE: Can Current Code Agent Survive Beyond Single-Repo Bug Fixing?"
authors:
  - "Guoxin Chen"
  - "Fanzhe Meng"
  - "Jiale Zhao"
  - "Minghao Li"
  - "Daixuan Cheng"
  - "Huatong Song"
  - "Jie Chen"
  - "Yuzhi Lin"
  - "Hui Chen"
  - "Xin Zhao"
  - "Ruihua Song"
  - "Chang Liu"
  - "Cheng Chen"
  - "Kai Jia"
  - "Ji-Rong Wen"
date: "2026-03-03"
arxiv_id: "2603.03194"
arxiv_url: "https://arxiv.org/abs/2603.03194"
pdf_url: "https://arxiv.org/pdf/2603.03194v1"
categories:
  - "cs.CL"
  - "cs.SE"
tags:
  - "代码智能体"
  - "基准测试"
  - "工具使用"
  - "推理"
  - "多仓库任务"
  - "代码生成"
  - "代码修复"
relevance_score: 8.5
---

# BeyondSWE: Can Current Code Agent Survive Beyond Single-Repo Bug Fixing?

## 原始摘要

Current benchmarks for code agents primarily assess narrow, repository-specific fixes, overlooking critical real-world challenges such as cross-repository reasoning, domain-specialized problem solving, dependency-driven migration, and full-repository generation. To address this gap, we introduce BeyondSWE, a comprehensive benchmark that broadens existing evaluations along two axes - resolution scope and knowledge scope - using 500 real-world instances across four distinct settings. Experimental results reveal a significant capability gap: even frontier models plateau below 45% success, and no single model performs consistently across task types. To systematically investigate the role of external knowledge, we develop SearchSWE, a framework that integrates deep search with coding abilities. Our experiments show that search augmentation yields inconsistent gains and can in some cases degrade performance, highlighting the difficulty of emulating developer-like workflows that interleave search and reasoning during coding tasks. This work offers both a realistic, challenging evaluation benchmark and a flexible framework to advance research toward more capable code agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前代码智能体（Code Agent）评估体系过于局限，无法反映其真实世界软件工程能力的问题。研究背景是，随着大语言模型的快速发展，能够自主处理复杂软件工程任务的代码智能体不断涌现，但评估这些智能体能力的基准测试却相对滞后。现有主流基准（如SWE-bench及其变体）主要聚焦于在单个代码仓库（Single-Repo）内进行局部、函数级别的错误修复任务。这些方法存在明显不足：它们将任务范围局限在单个仓库内，且通常不要求利用代码库之外的外部知识。这与现实世界中软件工程师面临的复杂挑战严重脱节，例如需要跨多个仓库进行推理、解决特定领域（如生物信息学）的专业问题、因上游依赖变更而驱动的大规模代码迁移，以及根据自然语言描述生成完整可用的代码仓库等。

因此，本文要解决的核心问题是：**当前的代码智能体能否应对超越单仓库错误修复的、更广泛且真实的软件工程挑战？** 为了系统地探究这个问题，论文引入了BeyondSWE这一综合性基准测试。该基准从“解决范围”（从局部函数修复到全局仓库重构与生成）和“知识范围”（从仅限当前代码库到需要整合跨仓库、领域知识或网络信息）两个关键维度扩展了评估边界，并据此构建了包含500个真实实例的四个具体评估场景（跨仓库问题修复、领域特定问题修复、依赖驱动迁移、文档到仓库生成）。通过这一基准，论文揭示了现有先进模型成功率低于45%的巨大能力缺口，并进一步通过构建一个集成深度搜索与编码能力的框架（SearchSWE），探究了外部知识整合的效用与挑战，指出当前模型在搜索与推理交替进行的类开发者工作流方面仍存在显著不足。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为评测基准和智能体框架两大类。

在**评测基准**方面，SWE-bench及其变体是当前评估代码智能体在真实GitHub问题上修复能力的标准工作。后续研究在此基础上进行了扩展，例如增加多语言支持、持续更新以缓解数据污染、以及提升任务复杂度。然而，这些现有基准主要局限于**单个代码仓库内的局部缺陷修复**。本文提出的BeyondSWE基准正是为了填补这一关键空白，它从**解决范围**（从局部补丁到全仓库代码生成）和**知识范围**（从仓库内知识到跨仓库、跨领域知识）两个维度进行扩展，从而能更全面地评估智能体应对实际软件工程中复杂挑战的能力。

在**智能体框架**方面，近期研究从数据和架构两个角度推进了代码智能体的发展。数据侧的工作集中于构建训练数据以提升在SWE-bench上的性能；架构侧则提出了多种智能体框架，其中OpenHands成为一个被广泛采用的支持多样化架构的框架。本文采用OpenHands作为主要评估框架，并在此基础上构建了SearchSWE（一个集成了深度网络搜索与代码操作的统一基线），以系统研究外部信息检索对智能体在BeyondSWE上能力的影响。这与以往侧重于单一仓库内修复的框架形成了对比。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为BeyondSWE的综合性基准测试，并开发一个名为SearchSWE的集成框架来解决现有代码智能体评估范围狭窄的问题。

**核心方法与架构设计**：
论文的核心方法是沿“解决范围”和“知识范围”两个维度扩展评估边界，构建了包含四个任务的BeyondSWE基准。这四个任务分别是：需要跨仓库推理的CrossRepo、需要领域专业知识（如量子计算）的DomainFix、涉及全仓库依赖迁移的DepMigrate，以及从零生成完整仓库的Doc2Repo。每个任务实例都包含问题描述、预配置的Docker运行环境和用于验证的测试套件。

为了支撑这一基准，论文设计了一套严谨的**基础设施**。关键创新在于采用基于智能体（Gemini 3 Pro）的方法自动构建可复现的Docker环境。该智能体在一个基础容器中通过“运行-错误-修复”的循环，动态安装依赖（甚至系统级库），直至通过现有测试，最后将其操作历史蒸馏为最小化的Dockerfile。此过程辅以严格的环境稳定性检查（五次运行测试）和专家审核，确保评估的可靠性。此外，为防止数据泄露，论文对原始Pull Request描述进行了去解决方案化处理，并清除了评估环境中的未来git历史信息。

**关键技术组件与创新点**：
1.  **任务设计创新**：BeyondSWE首次系统性地将评估从单仓库缺陷修复，扩展到跨仓库推理、领域知识融合、大规模迁移和全仓库生成，更贴近真实开发场景。
2.  **环境构建自动化**：提出的基于LLM智能体的环境构建方法，有效解决了因依赖过时而难以复现历史提交环境的“依赖衰减”难题，超越了静态依赖安装脚本的能力。
3.  **评估协议与隔离**：设计了严格的评估流程，将智能体的工作环境与最终验证环境完全隔离。通过提取`git diff`补丁并应用到全新的干净容器中进行测试，防止了缓存或配置污染对结果的影响。
4.  **集成搜索的框架（SearchSWE）**：为了系统研究外部知识的作用，论文开发了SearchSWE框架。该框架在传统代码智能体（拥有本地Docker容器上下文）的基础上，增加了**全局上下文**，通过搜索工具和浏览器工具访问外部资源（如文档、论坛）。智能体自主决定何时进行搜索。框架的关键安全机制是**阻止列表**，通过正则表达式阻止智能体直接访问目标仓库的相关URL和Git操作，强制其从间接资源中综合解决方案，而非直接获取答案。
5.  **质量保障体系**：结合了多轮自动化稳定性检查、跨领域专家（科学计算、软件工程）的独立人工审核以及测试套件审计，确保了基准中每个实例的高质量和挑战性。

总之，论文通过构建一个更全面、更真实的基准测试（BeyondSWE）和提供一个用于探索搜索与编码结合的研究框架（SearchSWE），系统地揭示并尝试解决当前代码智能体在复杂现实任务中能力不足的问题。

### Q4: 论文做了哪些实验？

论文在BeyondSWE基准上进行了系统实验，评估了当前代码智能体在超越单仓库错误修复的复杂任务上的能力。实验设置上，作者使用了两种框架：一是当前最先进的代码智能体框架OpenHands作为基线，二是其提出的SearchSWE框架，该框架集成了网络搜索能力，以探索搜索与复杂代码推理结合的效果。评估涵盖了四个任务场景：跨仓库推理（CrossRepo）、领域专项修复（DomainFix）、依赖驱动迁移（DepMigrate）和全仓库生成（Doc2Repo），共包含500个真实世界实例。

测试模型包括一系列前沿和代码专用模型，如Gemini 3 Pro、GPT-5.2、DeepSeek-V3.2、Kimi-K2、GLM-4.7、MiniMax-M2.1、Seed-Coder、Qwen3-Coder-Plus和Qwen3-235B-A22B-Instruct-2507。主要结果通过成功率（%Resolved）等指标衡量。实验发现，即使是最先进的模型，在BeyondSWE上的平均成功率也低于45%，与在SWE-bench Verified上80%以上的表现形成鲜明对比。具体而言，在OpenHands框架下，Gemini 3 Pro在DepMigrate任务上表现最佳（41.81%），Seed-Coder在CrossRepo上领先（44.72%），DeepSeek-V3.2在Doc2Repo的通过率最高（54.99%），但没有单一模型在所有任务上占优。DomainFix任务最具挑战性，所有模型的解决率很少超过36%。

引入SearchSWE框架后，搜索增强的效果不一致：在某些情况下带来提升（如Gemini 3 Pro在DomainFix上提升+7.5%），但在其他情况下可能导致性能下降（如Seed-Coder在CrossRepo上从44.72%降至38.89%）。分析表明，搜索频率与性能增益不直接相关，例如Gemini 3 Pro搜索调用较少（每实例0.8-1.1次）但获得最稳定的改进（平均+2.0%），而DeepSeek-V3.2搜索最频繁（每实例4.2-5.4次）却收益不稳定（平均-0.2%）。这些结果揭示了当前模型在有效整合搜索与代码推理方面存在显著能力缺口。

### Q5: 有什么可以进一步探索的点？

该论文揭示了当前代码智能体在跨仓库推理、依赖迁移等复杂场景中的显著能力瓶颈，其提出的BeyondSWE基准虽拓展了评估维度，但仍存在若干局限与可探索方向。首先，基准任务虽基于真实问题，但可能未覆盖更广泛的领域特异性任务（如硬件相关编程或遗留系统适配），未来可纳入多语言、低资源或安全关键型代码的生成与修复场景。其次，SearchSWE框架表明搜索增强的效果不稳定，这提示单纯的信息检索与代码生成的简单组合不足；未来需探索更精细的交互机制，例如动态规划搜索时机、引入验证反馈循环，或构建领域知识图谱来结构化外部信息。此外，实验发现模型在不同任务类型上表现不一致，说明单一模型架构可能无法兼顾各类需求，可研究模块化设计或任务感知的适配策略。最后，当前评估侧重于功能正确性，未来应加入效率、可维护性、安全合规性等软件工程指标，以推动智能体在真实开发流程中的实用化。

### Q6: 总结一下论文的主要内容

该论文针对现有代码智能体评测基准局限于单一代码库内错误修复的不足，提出了BeyondSWE基准，旨在评估代码智能体在更复杂真实场景下的能力。核心问题是现有评估未能涵盖跨仓库推理、领域专业问题解决、依赖驱动迁移及全仓库生成等关键挑战。

论文的主要贡献包括：1）构建了BeyondSWE基准，从解决范围和知识范围两个维度扩展评估边界，包含500个真实世界实例和四种任务设置；2）通过实验发现，即使前沿模型的成功率也低于45%，且没有模型能在所有任务类型上表现一致，揭示了显著的能力差距；3）提出了SearchSWE框架，将深度搜索与编码能力结合，以系统研究外部知识的作用。实验表明，搜索增强带来的性能提升并不稳定，有时甚至会导致性能下降，这凸显了在编码任务中模拟开发者交织搜索与推理的工作流程十分困难。

这项工作的意义在于提供了一个更真实、更具挑战性的评估基准，并提供了一个灵活的研究框架，推动代码智能体向更强大的方向发展。
