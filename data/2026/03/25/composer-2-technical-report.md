---
title: "Composer 2 Technical Report"
authors:
  - "Cursor Reseach"
  - ":"
  - "Aaron Chan"
  - "Ahmed Shalaby"
  - "Alexander Wettig"
  - "Aman Sanger"
  - "Andrew Zhai"
  - "Anurag Ajay"
  - "Ashvin Nair"
  - "Charlie Snell"
  - "Chen Lu"
  - "Chen Shen"
  - "Emily Jia"
  - "Federico Cassano"
  - "Hanpeng Liu"
  - "Haoyu Chen"
  - "Henry Wildermuth"
  - "Jacob Jackson"
  - "Janet Li"
  - "Jediah Katz"
date: "2026-03-25"
arxiv_id: "2603.24477"
arxiv_url: "https://arxiv.org/abs/2603.24477"
pdf_url: "https://arxiv.org/pdf/2603.24477v1"
categories:
  - "cs.SE"
  - "cs.LG"
tags:
  - "Agent Architecture/Training"
  - "Software Engineering Agent"
  - "Reinforcement Learning"
  - "Long-Horizon Planning"
  - "Tool Use"
  - "Benchmarking"
  - "SWE-bench"
relevance_score: 9.0
---

# Composer 2 Technical Report

## 原始摘要

Composer 2 is a specialized model designed for agentic software engineering. The model demonstrates strong long-term planning and coding intelligence while maintaining the ability to efficiently solve problems for interactive use. The model is trained in two phases: first, continued pretraining to improve the model's knowledge and latent coding ability, followed by large-scale reinforcement learning to improve end-to-end coding performance through stronger reasoning, accurate multi-step execution, and coherence on long-horizon realistic coding problems. We develop infrastructure to support training in the same Cursor harness that is used by the deployed model, with equivalent tools and structure, and use environments that match real problems closely. To measure the ability of the model on increasingly difficult tasks, we introduce a benchmark derived from real software engineering problems in large codebases including our own. Composer 2 is a frontier-level coding model and demonstrates a process for training strong domain-specialized models. On our CursorBench evaluations the model achieves a major improvement in accuracy compared to previous Composer models (61.3). On public benchmarks the model scores 61.7 on Terminal-Bench and 73.7 on SWE-bench Multilingual in our harness, comparable to state-of-the-art systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI辅助软件工程领域中，智能体（Agent）在应对复杂、长周期现实编码任务时存在的不足。研究背景是，随着大语言模型在代码生成方面取得进展，现有模型往往在交互式使用和解决简单即时问题上表现良好，但在需要长期规划、多步骤精确执行以及保持长程任务连贯性的真实软件工程场景中，其性能仍有显著差距。现有方法的不足主要体现在“训练-测试失配”上，即模型训练环境与最终部署所面对的真实、复杂的软件开发环境存在差异，导致模型在实际应用中的端到端编码性能，特别是在处理大型代码库中的实际问题时，表现不尽如人意。

本文要解决的核心问题是：如何训练一个专精于“智能体软件工程”的领域专用模型，使其能够像人类工程师一样，进行强推理、准确的多步骤执行，并连贯地处理长周期、现实世界的编码问题。为此，论文提出了Composer 2模型，其核心解决方案是通过两阶段训练流程（持续预训练+大规模强化学习）并在与部署环境高度一致的Cursor工具链中进行训练，以最小化失配，从而专门提升模型在真实软件工程任务中的规划与编码智能。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕代码生成与软件工程智能体展开，可分为以下几类：

**代码生成模型的发展**：早期工作聚焦于代码自动补全（如GitHub Copilot），随后通过指令微调发展为能响应用户请求的编码助手（如Codex、Code Llama）。这些模型主要在单轮代码片段生成上表现优异，但缺乏长期规划和自主执行能力。

**软件工程智能体**：近期研究致力于开发能自主操作代码库、解决复杂任务的智能体（如Devin、SWE-agent）。它们通过工具调用（如文件编辑、命令执行）与环境交互，完成多步骤任务。Composer 2属于此类，但强调通过强化学习提升端到端编码性能，并专注于在真实开发环境（Cursor工具链）中训练与部署。

**训练方法与评测**：方法上，本文采用两阶段训练（持续预训练+大规模强化学习），区别于仅依赖监督微调或在线学习的现有方案。评测方面，本文引入基于大型代码库真实问题的基准（如CursorBench），与公共基准（SWE-bench、Terminal-Bench）互补，更贴近实际软件工程场景。

本文与相关工作的核心区别在于：**紧密集成训练环境与部署环境**，使用与真实场景一致的工具和结构进行强化学习，以提升模型在长周期、复杂任务中的推理、执行一致性和探索能力。

### Q3: 论文如何解决这个问题？

论文通过一个两阶段的训练流程来解决提升智能体在软件工程领域能力的问题，其核心是**持续预训练**与**大规模强化学习**的结合，并辅以专门的基础设施和创新的训练技术。

**整体框架与主要模块**：
1.  **持续预训练阶段**：此阶段旨在夯实模型在编码领域的知识基础。以 Kimi K2.5 MoE 模型为基础，在大量代码数据上进行持续预训练。该阶段进一步分为三步：主体训练（32k上下文）、长上下文扩展（至256k）以及针对编码任务的简短监督微调。此阶段的关键在于，研究发现预训练后的交叉熵损失能有效预测下游强化学习的性能，确保了基础能力的有效迁移。此外，为了提升生产环境中的推理速度，模型还训练了**多令牌预测层**，通过自蒸馏技术学习主语言模型头的输出分布，以支持推测解码。

2.  **强化学习阶段**：这是提升模型端到端编码性能的核心。训练在高度模拟真实 Cursor IDE 会话的环境中进行，任务分布覆盖了真实软件工程中的各种场景。其关键技术包括：
    *   **策略梯度算法与稳定性保障**：采用基于策略梯度的算法，每个提示采样多个解决方案（rollout）进行组内比较。为了在高度异步的训练中保持稳定，系统实施了快速权重同步、滚动中更新权重以及重放MoE路由等策略，最小化采样策略与训练策略的差异。
    *   **创新的KL散度估计**：为避免传统估计器在策略差异大时方差爆炸的问题，选择了方差更稳定的标准估计器（\(k_1 = -\log r\)），从而确保了正则化的有效性。
    *   **自我总结技术**：继承自前代模型，允许模型在长视野任务中通过生成摘要来链式组织多轮响应，所有令牌共享最终奖励。这使模型能在有限上下文内处理更多信息，显著降低了错误率并提升了长程连贯性。
    *   **复合奖励设计**：除了任务完成度的主奖励，还引入了代码风格、沟通体验等辅助奖励。特别关键的是引入了一个**非线性长度惩罚**，鼓励模型在简单任务上快速响应，在复杂任务上深入思考，从而学习到高效的行为模式（如并行调用工具）。

**核心创新点**：
1.  **两阶段专业化训练流程**：将深度领域知识注入（持续预训练）与面向复杂任务执行的策略优化（强化学习）明确分离并有机结合，验证了预训练质量对RL性能的预测性。
2.  **高度逼真且可扩展的RL基础设施**：训练环境与最终部署的Cursor环境在工具和结构上保持等效，确保了技能的有效迁移。异步训练架构支持大规模、长上下文的智能体滚动生成。
3.  **针对智能体编码的强化学习优化**：通过稳定性控制、更优的KL估计、自我总结机制以及创新的非线性奖励设计，共同推动模型在保持输出多样性的同时，显著提升平均性能和最佳性能，避免了常见的能力塌缩问题，实现了在长视野、现实编码问题上的强推理与准确执行能力。

### Q4: 论文做了哪些实验？

论文的实验主要围绕评估Composer 2在真实软件工程任务上的性能展开。实验设置包括使用内部开发的CursorBench基准测试，该基准包含从工程团队实际编码会话中提取的任务，以解决公共基准测试存在的领域不匹配、提示过拟合、数据污染和评估范围狭窄等问题。CursorBench任务具有描述模糊（中位数390字符）和代码修改量大（中位数181行更改）的特点，更贴近真实场景。

数据集/基准测试方面，除了CursorBench，论文还使用了公共基准测试Terminal-Bench和SWE-bench Multilingual进行对比评估。对比方法包括之前的Composer模型以及前沿模型如GPT-5和Haiku 4.5。

主要结果方面，Composer 2在CursorBench上取得了61.3%的准确率，相比前代模型有显著提升。在公共基准测试上，其在Terminal-Bench得分为61.7%，在SWE-bench Multilingual得分为73.7%，与最先进系统性能相当。关键数据指标包括：CursorBench任务的中位描述长度（390字符）、中位代码更改行数（181行），以及SWE-bench Verified和Multilingual的对比数据（代码更改7-10行，描述长度1185-3055字符）。此外，论文还通过一系列针对性评估（如意图理解、指令遵循、代码质量等）来全面衡量模型的交互行为和质量。

### Q5: 有什么可以进一步探索的点？

这篇论文在面向智能体软件工程的模型训练上取得了显著进展，但其方法和评估仍存在一些局限性，为未来研究提供了多个探索方向。

首先，论文强调在模拟真实环境的Cursor框架中进行训练和评估，但其基准测试（CursorBench）主要基于自身代码库问题，这可能导致评估结果存在领域偏差，难以全面反映模型的泛化能力。未来研究可以构建更广泛、更多样化的开源软件基准，涵盖不同编程范式、领域和代码规模，以更公正地衡量模型的通用软件工程能力。

其次，模型采用“持续预训练+大规模强化学习”的两阶段范式，但论文对强化学习阶段的具体奖励函数设计、探索策略以及如何处理长期任务中的信用分配问题着墨不多。这是一个关键的技术黑箱。未来的改进可以探索更精细的奖励塑造机制，例如结合静态代码分析结果（如复杂度、可维护性）作为奖励信号，或者研究分层强化学习、课程学习等策略来更高效地解决长视野规划问题。

最后，Composer 2被定位为“领域专用模型”，其与通用大语言模型（如GPT-4）在软件工程任务上的协同潜力未被充分探讨。一个有趣的未来方向是研究“专用与通用模型的协作框架”，例如让Composer 2作为核心执行智能体，而由通用模型负责需求理解、非代码文件处理或更高层的系统设计决策，形成互补，以应对更复杂的端到端软件开发流程。此外，模型对工具使用的鲁棒性、在真实持续集成/部署环境中的表现，以及其决策过程的可解释性，也都是值得深入探索的重要维度。

### Q6: 总结一下论文的主要内容

Composer 2是一款专为智能体软件工程设计的专业模型，其核心目标是提升模型在长周期规划和编码智能方面的能力，同时保持高效解决交互式问题的性能。论文定义的问题是如何训练一个在复杂、现实的软件工程任务中表现卓越的领域专用模型。

方法上，模型训练分为两个阶段：首先进行持续预训练以增强模型的知识和潜在编码能力；随后进行大规模强化学习，旨在通过强化推理、精确的多步骤执行以及在长周期现实编码问题上的连贯性，来提升端到端的编码性能。一个关键原则是最大限度地模拟真实世界的用户挑战，以减少训练与测试的差异。为此，研究团队开发了基础设施，使训练能在与部署模型相同的Cursor框架中进行，并使用等效的工具和紧密匹配真实问题的环境。

论文的主要结论是，Composer 2达到了前沿水平的编码模型性能。在内部基准CursorBench上，其准确率（61.3）相比前代模型有显著提升；在公开基准如Terminal-Bench和SWE-bench Multilingual上，分别取得了61.7和73.7的分数，与当前最先进的系统表现相当。这证明了其训练强领域专用模型方法的有效性。
