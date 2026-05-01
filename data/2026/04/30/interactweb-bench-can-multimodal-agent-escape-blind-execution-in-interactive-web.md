---
title: "InteractWeb-Bench: Can Multimodal Agent Escape Blind Execution in Interactive Website Generation?"
authors:
  - "Qiyao Wang"
  - "Haoran Hu"
  - "Longze Chen"
  - "Hongbo Wang"
  - "Hamid Alinejad-Rokny"
  - "Yuan Lin"
  - "Min Yang"
date: "2026-04-30"
arxiv_id: "2604.27419"
arxiv_url: "https://arxiv.org/abs/2604.27419"
pdf_url: "https://arxiv.org/pdf/2604.27419v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "多模态Agent"
  - "网站生成Agent"
  - "Agent交互评估"
  - "交互式执行环境"
  - "意图识别"
  - "代码合成Agent"
  - "基准测试"
relevance_score: 8.5
---

# InteractWeb-Bench: Can Multimodal Agent Escape Blind Execution in Interactive Website Generation?

## 原始摘要

With the advancement of multimodal large language models (MLLMs) and coding agents, the website development has shifted from manual programming to agent-based project-level code synthesis. Existing benchmarks rely on idealized assumptions, especially for well-structured, information-rich inputs and static execution settings. In contrast, real-world development is constrained by a critical bottleneck: the semantic misalignment between ambiguous, low-quality instructions from non-expert users and model understanding, which results in a failure mode that we term blind execution. To address this gap, we introduce InteractWeb-Bench, the first multimodal interactive benchmark for website generation under non-expert low-code user conditions. InteractWeb-Bench introduces four types of user agents and persona-driven instruction perturbations to systematically simulate diverse user behaviors, including ambiguity, redundancy, and contradiction, grounded in requirement engineering defect taxonomies. We develop an interactive execution environment for agents, featuring a unified action space comprising Clarify, Implement, Verify, and Submit, enabling iterative intent refinement, code synthesis, and visual feedback-based validation. Extensive experiments and analysis reveal that frontier MLLM-based agents remain trapped in blind execution, exposing limitations in intent recognition and adaptive interaction.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态大模型（MLLM）驱动的网站生成代理在非专业用户低代码交互场景中普遍存在的“盲执行”问题。研究背景是，随着MLLM和编码代理的发展，网站开发正从手动编程转向基于代理的代码合成，降低了专业门槛。然而，现有基准测试依赖于理想化假设，例如结构清晰、信息丰富的输入和静态执行环境。现实世界中，非专业用户提供的指令往往模糊、碎片化、充满冗余甚至矛盾，这导致语义错配。现有代理的不足在于，它们会盲目采纳并执行这些有缺陷的指令，缺乏主动澄清意图、进行动态推理和验证的能力，最终引发任务失败、UI渲染异常和功能幻觉。本文的核心问题是：开发一个多模态交互式基准测试（InteractWeb-Bench），通过模拟四种典型用户角色（如极简、冗余、矛盾等）及指令扰动来复现真实用户的复杂行为，并设计一个包含“澄清、实现、验证、提交”四个统一动作的交互执行环境，从而评估并促进代理从被动的指令执行者转变为能够主动识别意图、进行自适应交互的协作伙伴，最终摆脱盲执行陷阱。

### Q2: 有哪些相关研究？

基于论文内容，相关研究主要分为三类：**网站生成基准**、**意图澄清与用户交互**以及**交互式智能体与执行环境**。

在网站生成基准方面，相关工作如 Design2Code、Web2Code 和 WebGen-Bench 评估了模型将设计稿或详尽文本指令转换为静态或动态网站的能力。这些工作依赖于高度标准化、信息完整的输入。本文的区别在于，首次针对非专业用户常见的模糊、冗余和矛盾的低质量指令，通过引入人物驱动的指令扰动，模拟真实世界中的语义偏差。

在意图澄清与用户交互方面，ClarifyCoder、HumanEvalComm 和 Persona2Web 等工作探索了模型应对模糊需求或从浏览历史中被动推断意图的能力。然而，它们局限于纯文本或被动推理。本文的创新在于，要求智能体主动进行语言层面的需求澄清，并融合视觉渲染反馈进行验证，从而弥补了视觉前端工程领域中交互式意图理解的空白。

在交互式智能体与执行环境方面，SWE-agent、OpenHands 及 SWE-bench 等构建了基于终端或编辑器反馈的多轮交互环境，但重点在于通过客观测试。本文则专注于人机协作过程，通过设计包含澄清、实施、验证和提交的统一动作空间，迫使智能体超越单纯的代码执行，主动识别并满足用户未言明的真实意图。

### Q3: 论文如何解决这个问题？

InteractWeb-Bench通过构建一个多模态交互式基准框架来解决问题，核心方法是模拟非专业用户的真实行为，并迫使智能体在动态交互中主动澄清需求，而非盲目执行指令。

整体框架由两大核心模块构成：**角色驱动的用户智能体模块**和**交互式执行环境**。用户智能体模块基于需求工程缺陷分类学和格莱斯会话准则，设计了四种用户角色（P-MIN、P-RAM、P-INT、P-CON），分别模拟信息不足、噪音干扰、语义模糊和需求矛盾，通过变异算子对原始清晰指令进行扰动生成测试用例。交互式执行环境为智能体定义了统一的动作空间，包括**Clarify（澄清）**、**Implement（实现）**、**Verify（验证）**和**Submit（提交）**，支持智能体自主切换。关键技术包括：1）**两阶段用户响应机制**，防止用户泄露完整信息，并保持角色风格一致性；2）**GUI多模态反馈循环**，在Verify动作中提供失败截图、控制台错误和推理轨迹；3）**双边界约束机制**，防止无限调试循环。创新点在于将需求工程理论引入基准设计，系统评估了智能体在模糊指令下的需求获取、意图识别和迭代修正能力。

### Q4: 论文做了哪些实验？

论文实验评估了多种多模态大模型（如Qwen3.6-Plus、Kimi-K2.5、GPT-4.1等）在交互式网站生成任务上的表现。实验设置基于bolt.diy框架将模型实例化为网站生成智能体，交互环境使用Playwright浏览器内核实现动态渲染和GUI验证，用户智能体由DeepSeek-V3.2模拟。数据集/基准采用InteractWeb-Bench，包含四种用户角色（P-MIN缺失、P-RAM冗余、P-INT矛盾、P-CON综合扰动）和三个难度等级。对比方法包括不同模型家族及规模。主要结果以任务完成率（TCR）和幻觉率（Hallu. Rate）为指标：最佳模型Qwen3.6-Plus仅达38.78% TCR，且所有模型在P-MIN场景下表现最差（如24.96%）。进一步分析意图对齐分数（IAS>3.90）和澄清命中率（CHR<40%）发现，智能体虽能粗理解意图，但很少主动澄清模糊需求，陷入“盲目执行”。此外，GPT-4.1-mini平均澄清次数最高（0.94次），但其TCR仅29.39%，幻觉率23.5%。

### Q5: 有什么可以进一步探索的点？

基于实验结果，该研究揭示了当前多模态智能体在交互式网页生成中的主要局限：虽然整体意图理解得分（IAS）较高，但澄清命中率（CHR）普遍低于40%，表明智能体深陷“盲执行”困境。未来可从以下几个方向深入探索：

1. **增强主动澄清能力**：模型需学会识别指令中的模糊、冗余或矛盾点，并在执行前主动提问。可设计专门的“澄清策略模块”，结合强化学习优化提问时机与质量。

2. **改进交互循环机制**：当前Clarify→Implement→Verify→Submit的循环中，Verify环节依赖视觉反馈，但模型对视觉结果的理解仍浅。可引入多轮对话式反馈，让用户或环境提供结构化的修正信号。

3. **鲁棒性训练**：针对P-MIN（信息缺失）等低性能场景，可构建对抗性训练数据，使模型学会从残缺指令中推理隐含需求，减少对完美输入假设的依赖。

4. **轻量化与开源模型提升**：小模型如Qwen3.5-9B幻觉率高达53.7%，需平衡模型大小与推理能力，探索知识蒸馏或检索增强生成（RAG）来弥补不足。

### Q6: 总结一下论文的主要内容

这篇论文提出了InteractWeb-Bench，一个用于评估多模态大语言模型驱动的智能体在非专家用户低代码环境下生成网站能力的交互式基准。核心问题是现实世界中用户指令常存在歧义、冗余和矛盾，导致智能体陷入“盲目执行”（Blind Execution）的失败模式，即被动适应有缺陷的查询，无法主动澄清意图或进行动态交互验证。方法上，该基准基于需求工程缺陷分类学，构建了四种典型用户角色和指令扰动，模拟多样化的用户行为。同时，它设计了一个包含澄清、实现、验证和提交的统一动作空间，使智能体能够迭代优化意图、合成代码并基于视觉反馈验证。实验表明，现有最先进的MLLM智能体仍难以摆脱盲目执行，在意图识别和自适应交互方面存在显著局限。该工作首次系统评估了智能体在网站生成任务中的交互能力，对推动智能体从被动指令执行者向意图对齐的协作者进化具有重要意义。
