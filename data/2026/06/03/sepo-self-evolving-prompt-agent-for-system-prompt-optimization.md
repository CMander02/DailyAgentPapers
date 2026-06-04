---
title: "SePO: Self-Evolving Prompt Agent for System Prompt Optimization"
authors:
  - "Wangcheng Tao"
  - "Han Wu"
  - "Weng-Fai Wong"
date: "2026-06-03"
arxiv_id: "2606.04465"
arxiv_url: "https://arxiv.org/abs/2606.04465"
pdf_url: "https://arxiv.org/pdf/2606.04465v1"
github_url: "https://github.com/taowangcheng/SePO"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "System Prompt Optimization"
  - "Self-Evolution"
  - "Prompt Agent"
  - "Multi-Task Learning"
  - "Evolutionary Search"
relevance_score: 9.5
---

# SePO: Self-Evolving Prompt Agent for System Prompt Optimization

## 原始摘要

System prompt optimization improves agent behavior without modifying the underlying model, yielding human-readable, model-agnostic instructions. Existing methods build a prompt agent that refines task agents' system prompts, yet leave the prompt agent's own system prompt hand-engineered and fixed. We propose Self-Evolving Prompt Optimization (SePO), which treats the prompt agent's own system prompt as an optimization target alongside task agents' system prompts. SePO adopts a self-referential design. A single prompt agent improves both task agents' system prompts and its own under an open-ended evolutionary search that maintains an archive of candidate prompts as stepping stones. Training proceeds in two stages: pre-training evolves the prompt agent on a multi-task pool, and fine-tuning then applies it to a target task. Across five benchmarks spanning math (AIME'25), abstract reasoning (ARC-AGI-1), graduate-level science (GPQA), code generation (MBPP), and logic puzzles (Sudoku), SePO consistently outperforms Manual-CoT, TextGrad, and MetaSPO, improving the average accuracy by 4.49 points compared to Manual-CoT. The prompt optimization skill from pre-training also generalizes to tasks beyond the pre-training mixture, rather than memorizing per-task prompts.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决系统提示优化中的一个核心问题：提示优化器自身的提示无法被优化，从而限制了整体优化效果的提升。当前，许多方法（如TextGrad、MetaSPO）都通过一个“提示智能体”来优化任务智能体的系统提示，但该提示智能体自身的系统提示往往是手工设计的，且在整个过程中保持不变。这意味着，提示优化能力完全受限于人类的工程经验，无法随着处理更多任务而积累经验、自我提升。尽管PromptBreeder引入了元堆叠结构，但其顶层提示仍然是固定的，无法实现完整的自我优化闭环。为突破这一瓶颈，本文提出了自我演化提示优化框架。该框架的核心是一个自指设计：将提示智能体自身也视为一个特殊的任务智能体，从而使用同一套优化程序来同时改进任务智能体的提示和提示智能体自身的提示。通过开放式演化搜索和存档机制，SePO让提示智能体在持续优化任务智能体提示的过程中，也不断反思和优化自身的提示策略，最终将提示优化从一种固定的工具转变为一种可跨任务积累的学习技能。

### Q2: 有哪些相关研究？

主要相关研究可按方法类、自进化类和演化搜索类组织。

**方法类**：Prompt优化领域相关工作包括早期手工制作的链式思考提示、黑盒方法（基于反馈搜索）、演化方法（保持候选种群）、文本梯度框架（提供组件级反馈）和元学习（跨任务泛化）。其中，**PromptBreeder**是SePO最直接的先驱，它共同演化任务提示和生成它们的变异提示，但其自引用受限于固定手工编写的超变异提示，且每次演化是任务特定的。**MetaSPO**将提示优化表述为跨任务元学习，但其元优化器本身是手工编写且固定不变的。这些方法中驱动搜索的提示代理都是手工设计的，不会随任务增多而改进。SePO的创新在于将提示代理自身视为优化目标，采用自引用设计，使其在同一演化过程中同时改进任务代理和自身的系统提示。

**自进化类**：相关工作包括修改代理输出的方法（Self-Refine、Reflexion）、积累技能库的Voyager，以及最近修改代理代码和架构的方法（基于档案的演化搜索、ADAS）。SePO仅操作提示代理的自然语言系统提示，保持代码、权重和工具不变，相比修改输出、技能或架构更可解释且模型无关。

**演化搜索类**：FunSearch、Eureka、AlphaEvolve等系统将演化搜索应用于非代理制品（数学对象、奖励函数），但驱动搜索的代理是固定外部算子。SePO则将提示代理本身置于被搜索的种群中，使算子也成为优化目标，这是本质区别。

### Q3: 论文如何解决这个问题？

SePO通过一种自指涉的两阶段进化优化框架，同时优化任务智能体和提示智能体自身的系统提示。核心方法是开放进化搜索，维护一个候选提示档案库作为阶梯石，通过变异产生子代并基于评分准入。整体框架包括：预训练阶段在多任务池上进化优化提示智能体自身的系统提示，使其获得广泛优化能力；微调阶段将预训练得到的提示智能体应用于目标任务，优化任务智能体的系统提示。

主要组件包括：任务智能体（含系统提示p、基础模型M和工作流W）、提示智能体（含自身系统提示̃p、模型̃M和工作流̃W）、以及提示任务̃T（定义评估提示改进效果的评分函数̃S）。关键技术是自指涉闭合设计，将提示智能体自身的系统提示也作为优化变量，使其在预训练阶段能改进自身副本。每个进化迭代中，从档案库采样父代，通过提示智能体生成子代提示，评估其性能并决定是否加入档案库。

创新点在于：1)打破传统方法中提示智能体系统提示固定的局限，将其纳入优化循环；2)采用两阶段训练范式，预训练积累跨任务泛化能力，微调适配具体任务；3)开放进化搜索保持候选多样性，促进持续改进。这种方法在数学推理、抽象推理、科学问答、代码生成和逻辑谜题五个基准上平均提升4.49个百分点的准确率。

### Q4: 论文做了哪些实验？

论文在五个基准测试上进行了实验：AIME'25（数学）、ARC-AGI-1（抽象视觉推理）、GPQA（研究生级科学）、MBPP（代码生成）和Sudoku（数独）。实验设置了训练集和测试集，采用pass@1准确率（ARC-AGI-1为pass@3），使用DeepSeek-V3.2作为任务代理、Gemini 3.1 Pro Preview作为提示代理。对比方法包括：Manual-CoT（无优化基线）、TextGrad（文本梯度框架）和MetaSPO（元学习全局提示）。SePO采用两种配置：Specialist（单任务预训练+微调）和Generalist（多任务预训练+微调）。主要结果显示，SePO-Generalist在所有任务上取得最佳准确率，平均从Manual-CoT的71.89提升至76.38，超过TextGrad（70.39）和MetaSPO（71.32）。具体地，AIME'25达64.22、ARC-AGI-1达43.39、GPQA达78.18、MBPP达96.20、Sudoku达99.90。消融实验表明，去除自改进或开放搜索后平均准确率分别降至74.94和72.64。模型交换实验（Gemini Flash-Lite + Claude Opus）中，SePO仍优于Manual-CoT（70.08 vs 67.95）。成本方面，SePO-Generalist预训练摊销后每任务仅$7.43。

### Q5: 有什么可以进一步探索的点？

SePO虽然提出了自我指涉的提示优化框架，但其核心搜索机制仍依赖启发式的进化算法，缺乏对优化路径的深层理解。未来研究可以从几个方向突破：一是将强化学习引入演化搜索过程，让提示智能体不仅能更新提示内容，还能学习何时以及如何调整自身的优化策略。二是当前的两阶段训练（预训练+微调）在任务池构建上依赖人工选择，可探索自动任务生成或元学习任务采样机制，增强跨任务泛化能力。三是SePO目前仅针对系统提示优化，其自演化框架在逻辑上可扩展到工具调用、工作流编排和代理架构等更开放的决策空间，构建具有元认知能力的自改进系统。此外，评估体系也值得改进，现有基准侧重于准确率，缺乏对提示鲁棒性、可解释性和安全边界的系统度量。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为 SePO 的系统提示词优化方法。现有方法虽然能通过提示智能体优化任务智能体的系统提示，但其自身的系统提示仍然需要人工设计且固定不变。SePO 的核心创新在于采用“自指涉”设计，将提示智能体自身的系统提示也作为优化目标，与任务智能体的系统提示一同进行进化搜索。该方法分为两阶段训练：首先在多个任务上进行预训练，使提示智能体积累跨任务的通用提示优化能力；然后针对特定目标任务进行微调。在数学推理、抽象推理、研究生级别科学问题、代码生成和逻辑谜题五个基准测试上，SePO 均优于 Manual-CoT、TextGrad 和 MetaSPO 等基线方法，平均准确率相比 Manual-CoT 提升了 4.49 个百分点。该研究的意义在于将提示智能体从固定的人设组件转变为可学习的组件，为构建能够持续自我改进的自主智能体开辟了新方向。
