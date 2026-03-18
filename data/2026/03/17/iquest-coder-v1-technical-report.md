---
title: "IQuest-Coder-V1 Technical Report"
authors:
  - "Jian Yang"
  - "Wei Zhang"
  - "Shawn Guo"
  - "Zhengmao Ye"
  - "Lin Jing"
  - "Shark Liu"
  - "Yizhi Li"
  - "Jiajun Wu"
  - "Cening Liu"
  - "X. Ma"
  - "Yuyang Song"
  - "Siwei Wu"
  - "Yuwen Li"
  - "L. Liao"
  - "T. Zheng"
  - "Ziling Huang"
  - "Zelong Huang"
  - "Che Liu"
  - "Yan Xing"
  - "Renyuan Li"
date: "2026-03-17"
arxiv_id: "2603.16733"
arxiv_url: "https://arxiv.org/abs/2603.16733"
pdf_url: "https://arxiv.org/pdf/2603.16733v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.SE"
tags:
  - "Code Agent"
  - "Agent Training"
  - "Tool Use"
  - "Multi-Stage Training"
  - "Reasoning"
  - "Software Engineering"
  - "Model Architecture"
  - "Benchmark Performance"
relevance_score: 8.0
---

# IQuest-Coder-V1 Technical Report

## 原始摘要

In this report, we introduce the IQuest-Coder-V1 series-(7B/14B/40B/40B-Loop), a new family of code large language models (LLMs). Moving beyond static code representations, we propose the code-flow multi-stage training paradigm, which captures the dynamic evolution of software logic through different phases of the pipeline. Our models are developed through the evolutionary pipeline, starting with the initial pre-training consisting of code facts, repository, and completion data. Following that, we implement a specialized mid-training stage that integrates reasoning and agentic trajectories in 32k-context and repository-scale in 128k-context to forge deep logical foundations. The models are then finalized with post-training of specialized coding capabilities, which is bifurcated into two specialized paths: the thinking path (utilizing reasoning-driven RL) and the instruct path (optimized for general assistance). IQuest-Coder-V1 achieves state-of-the-art performance among competitive models across critical dimensions of code intelligence: agentic software engineering, competitive programming, and complex tool use. To address deployment constraints, the IQuest-Coder-V1-Loop variant introduces a recurrent mechanism designed to optimize the trade-off between model capacity and deployment footprint, offering an architecturally enhanced path for efficacy-efficiency trade-off. We believe the release of the IQuest-Coder-V1 series, including the complete white-box chain of checkpoints from pre-training bases to the final thinking and instruction models, will advance research in autonomous code intelligence and real-world agentic systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前代码大语言模型在复杂、长周期软件工程任务中能力不足的问题。研究背景是，尽管通用大语言模型通过领域专业化能显著提升能力，但在代码智能领域，开源模型与顶尖闭源模型（如Claude 4.5 Sonnet）之间仍存在明显差距，尤其在长程推理和处理多文件复杂代码库方面表现薄弱。

现有方法的不足主要体现在：传统代码LLM的训练多基于静态代码表示，缺乏对软件逻辑动态演化的捕捉；训练流程往往较为单一，未能有效整合推理、智能体轨迹和长上下文代码数据；此外，模型在部署时也面临容量与效率难以兼顾的挑战。

本文要解决的核心问题是：如何通过一种创新的训练范式，系统性地提升代码LLM在智能体软件工程、竞技编程和复杂工具使用等关键维度的性能，并优化其部署效率。为此，论文提出了“代码流”多阶段训练范式，该范式通过预训练、中训练（整合推理与智能体轨迹）和分叉后训练（分为“思考路径”和“指导路径”）的动态流程，来捕捉软件逻辑的演变。同时，论文还通过引入循环机制变体，探索在模型能力与部署资源占用之间取得更优权衡的架构增强路径。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕代码大语言模型的训练方法、架构优化和评测基准展开，可分为以下几类：

**1. 代码大语言模型的训练范式**：相关工作如CodeLlama、StarCoder等，主要采用静态代码数据进行预训练，随后进行指令微调。本文提出的“代码流多阶段训练范式”与之不同，强调捕捉软件逻辑的动态演化，通过专门的“中期训练”阶段整合推理和智能体轨迹，以构建更深的逻辑基础，超越了静态表示。

**2. 模型架构与效率优化**：为应对部署限制，已有研究如DeepSeek-Coder-V2采用MoE架构。本文的IQuest-Coder-V1-Loop变体则引入了一种循环机制，旨在优化模型能力与部署开销之间的权衡，提供了一条不同的架构增强路径。

**3. 代码智能评测基准**：本文的评估涉及多个关键维度，如智能体软件工程、竞技编程和复杂工具使用。相关评测基准包括HumanEval、MBPP（针对代码生成）以及SWE-bench、APPS等（针对更复杂的软件工程和编程任务）。本文模型在这些基准上取得了领先性能，并与Claude等闭源领先模型进行对比，旨在缩小开源与闭源模型之间的差距。

**4. 专业化后训练路径**：许多模型采用统一的指令微调。本文则在后训练阶段提出了分叉的专业化路径：“思维路径”（利用推理驱动的强化学习）和“指令路径”（针对通用辅助优化），这区别于传统的单一后训练方法。

### Q3: 论文如何解决这个问题？

论文通过提出“代码流多阶段训练范式”来解决静态代码表示无法捕捉软件逻辑动态演化的问题。其核心方法是一个包含预训练、中训练和后训练的三阶段进化式管道，旨在让模型掌握代码从基础事实到复杂推理，再到实际工程应用的完整生命周期。

在整体架构上，首先进行**预训练**，构建多语言代码语料库，并利用编程语言间的协同效应提升模型鲁棒性。关键技术包括：基于抽象语法树的深度分析以确保代码结构完整性；使用领域特定的代理分类器进行高质量数据筛选；以及通过“三元组构建策略”来学习仓库演化模式，即从项目成熟阶段选取 `(旧状态, 补丁信息, 新状态)` 作为训练样本，使模型理解真实的代码迭代过程。此外，通过文件级和仓库级的“填空中间”格式数据来增强代码补全能力。

**中训练阶段**是关键创新，采用两阶段方法（32K和128K上下文）来构建深度逻辑基础。该阶段整合了推理问答和智能体轨迹数据。推理问答作为“推理运行时”，鼓励结构化问题分解和一致性检查；智能体轨迹数据则提供完整的“行动-观察-修正”循环反馈，教授模型“闭环智能”，使其能够在长上下文中处理复杂任务、从错误中恢复并维持连贯计划。128K上下文阶段专门扩展了仓库级推理能力。

最后的**后训练阶段**将模型转化为专门的代码智能系统，并分化为两条路径：“思维路径”和“指导路径”。该阶段采用监督微调和强化学习。创新点包括：1) 使用模型在环合成与基于执行的验证来生成高质量指令数据；2) 实施大规模监督微调，其数据处理规模接近预训练，并采用三阶段课程学习（从基础指令遵循到对抗样本）以确保稳定收敛；3) 引入强化学习，例如在竞争性编程任务上使用GRPO算法和clip-Higher策略，以及基于可扩展沙箱的SWE-RL框架，将现实软件工程任务公式化为交互式RL环境，奖励基于测试套件通过率和效率正则化，从而涌现出自我调试、跨语言迁移等能力。

此外，针对部署限制，论文还提出了IQuest-Coder-V1-Loop变体，引入了循环机制，以在模型容量和部署足迹之间取得更优权衡，提供了架构增强的效能-效率权衡路径。

### Q4: 论文做了哪些实验？

论文在多个代码智能维度上进行了全面的实验评估。实验设置上，作者将IQuest-Coder-V1系列模型（7B/14B/40B/40B-Loop的Instruct和Thinking变体）与当前最先进的代码大语言模型进行对比，包括Anthropic Claude、OpenAI GPT-5.1、Google Gemini、阿里Qwen、深度求索DeepSeek-Coder、Mistral CodeStral等开源和闭源模型。

使用的数据集和基准测试覆盖了代码生成、理解、推理和代理任务等多个方面：
1.  **代码生成与功能正确性**：使用EvalPlus（包含HumanEval+和MBPP+）、BigCodeBench、LiveCodeBench和CrossCodeEval（用于跨文件代码补全）。
2.  **代码推理**：使用CRUXEval，评估正向执行（I2O）和逆向推理（O2I）能力。
3.  **代码效率**：使用Mercury基准，在256个Python问题上评估代码运行时的效率，报告Pass@1和Beyond@1指标。
4.  **文本到SQL**：使用Spider和BIRD基准，评估在复杂数据库场景下的语义解析和SQL生成能力，报告执行准确率。
5.  **代理与软件工程**：使用Terminal-Bench（评估终端工作流完成能力）、SWE-bench Verified（评估真实软件问题修复）以及Mind2Web和BFCL V3（评估通用工具使用）。

主要结果方面，IQuest-Coder-V1模型在多个任务上展现出强大性能。例如，在Mercury效率任务上，40B-Instruct模型取得了83.6的Beyond@1和95.3的Pass@1。在文本到SQL任务上，40B-Instruct模型在BIRD和Spider上的执行准确率分别达到70.5%和92.2%。在代理任务上，14B-Instruct模型在Terminal-Bench上达到36.3分，在SWE-bench Verified上达到66.2分。总体而言，模型在代码效率、复杂SQL生成和端到端软件工程工作流方面表现优异，尤其在较大参数规模（40B）上达到了与顶级闭源模型竞争的水平。

### Q5: 有什么可以进一步探索的点？

该论文提出的代码流多阶段训练范式虽具创新性，但其局限性与未来探索方向可从多个维度展开。首先，其“动态演化”的捕捉主要依赖预设的阶段性数据，而非真正实时的、交互式的代码生成与调试闭环，未来可探索集成真实IDE环境反馈的在线强化学习，使模型能在执行中即时调整逻辑。其次，128k上下文虽能处理仓库级代码，但对超大规模、跨仓库的软件项目理解仍有不足，需研究更高效的长上下文建模与代码依赖图神经网络结合的方法。再者，Thinking与Instruct路径的分化可能造成能力割裂，可探索动态路径选择机制，让模型根据任务复杂度自主切换推理模式。最后，Loop变体的循环机制在效率与性能平衡上仍有优化空间，例如引入自适应循环深度、与稀疏化专家混合模型结合等。总体而言，未来工作可聚焦于更细粒度的代码状态追踪、跨模态（代码-文档-日志）联合训练，以及面向实际部署的轻量化架构创新。

### Q6: 总结一下论文的主要内容

该论文介绍了IQuest-Coder-V1系列代码大语言模型，其核心贡献是提出了“代码流多阶段训练范式”，以捕捉软件逻辑的动态演化过程。研究问题在于如何超越静态代码表示，构建能处理复杂软件工程任务的智能模型。方法上，采用进化式管道：首先进行包含代码事实、仓库和补全数据的初始预训练；随后进入专门的中期训练阶段，在32k上下文中整合推理与智能体轨迹，并在128k上下文中处理仓库级数据以奠定深层逻辑基础；最后通过后训练分化为两条专门路径——“思维路径”（利用推理驱动的强化学习）和“指导路径”（针对通用辅助优化）。主要结论显示，该模型在智能体软件工程、竞争性编程和复杂工具使用等关键维度上达到了最先进的性能。此外，论文还提出了IQuest-Coder-V1-Loop变体，通过引入循环机制在模型能力与部署成本间取得优化平衡。该系列模型的完整白盒化发布有望推动自主代码智能和现实世界智能体系统的研究进展。
