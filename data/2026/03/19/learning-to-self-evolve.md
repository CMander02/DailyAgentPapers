---
title: "Learning to Self-Evolve"
authors:
  - "Xiaoyin Chen"
  - "Canwen Xu"
  - "Yite Wang"
  - "Boyi Liu"
  - "Zhewei Yao"
  - "Yuxiong He"
date: "2026-03-19"
arxiv_id: "2603.18620"
arxiv_url: "https://arxiv.org/abs/2603.18620"
pdf_url: "https://arxiv.org/pdf/2603.18620v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "强化学习"
  - "测试时优化"
  - "上下文学习"
  - "自我进化"
  - "模型训练"
  - "Text-to-SQL"
  - "MMLU"
relevance_score: 8.5
---

# Learning to Self-Evolve

## 原始摘要

We introduce Learning to Self-Evolve (LSE), a reinforcement learning framework that trains large language models (LLMs) to improve their own contexts at test time. We situate LSE in the setting of test-time self-evolution, where a model iteratively refines its context from feedback on seen problems to perform better on new ones. Existing approaches rely entirely on the inherent reasoning ability of the model and never explicitly train it for this task. LSE reduces the multi-step evolution problem to a single-step RL objective, where each context edit is rewarded by the improvement in downstream performance. We pair this objective with a tree-guided evolution loop. On Text-to-SQL generation (BIRD) and general question answering (MMLU-Redux), a 4B-parameter model trained with LSE outperforms self-evolving policies powered by GPT-5 and Claude Sonnet 4.5, as well as prompt optimization methods including GEPA and TextGrad, and transfers to guide other models without additional training. Our results highlight the effectiveness of treating self-evolution as a learnable skill.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）在部署后无法根据测试时经验进行自我适应和改进的问题。研究背景是，当前LLM的训练（包括强化学习微调）在部署后即停止，模型在测试时面对新问题时，其策略是静态的，无法利用已解决问题的反馈来持续优化自身表现，这与人类通过经验积累不断进化的智能能力形成差距。

现有方法（如自动提示优化、自指更新和智能体记忆系统）主要依赖于LLM固有的推理能力，让模型自行分析反馈并修改上下文（提示）以提升后续表现。然而，这些方法从未对模型进行针对“自我进化”这一特定任务的显式训练。其不足在于，自我进化本质上是一个涉及信用分配、梯度估计和探索-利用权衡的复杂过程，而现有方法要求模型仅通过自然语言推理隐式地完成所有这些任务，这可能导致效率低下和效果不佳。

本文要解决的核心问题是：如何让LLM在测试时具备高效、可学习的自我进化能力。为此，论文提出了“学习自我进化”（LSE）框架，将多步进化问题简化为单步强化学习目标，显式地训练一个LLM作为自我进化策略。该策略根据当前上下文和性能反馈生成改进后的上下文，其奖励基于下游性能的提升幅度（而非绝对分数）。在测试时，结合树引导的进化循环来探索和回溯不同的上下文路径。通过这种方式，LSE旨在使自我进化成为一种可学习的技能，从而弥补静态部署与动态适应之间的鸿沟。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕“自我进化”这一概念展开，可归纳为训练时自我进化与测试时自我进化两大类。

在**训练时自我进化**方面，现有工作利用大模型生成自身训练数据和学习信号。例如，基于强化学习（RL）的后训练方法优化模型生成的推理轨迹以符合可验证的奖励；自举方法（如STaR）迭代生成候选原理并微调正确的部分；自我奖励方法进一步将模型自身作为奖励信号；而Absolute Zero则极端地让单一模型在无外部数据下自我提议和解决任务，仅依赖代码执行器作为奖励来源。这些方法旨在训练出更强大的模型，但训练结束后策略即固定不变。本文的工作是互补的，专注于让策略在测试时能持续改进。

在**测试时自我进化**方面，研究旨在使模型能基于部署后的经验自我更新。这又可分为两类：一是**单次任务内方法**，如Reflexion通过反思失败尝试并重试、SCoRe用RL训练自我纠正、TTRL直接在测试时应用RL以多数投票作为代理奖励，以及TTT-Discover在测试时通过RL继续训练以寻找最佳解。这些方法以计算成本换取单个问题实例的准确性，但知识无法跨问题迁移。二是**跨任务方法**，积累已完成任务的经验并应用于新任务。这包括：1. 自动提示优化，如GEPA和TextGrad利用自然语言反馈迭代突变和重写提示；2. 自指代智能体，修改自身代码或指令，如ExpeL从成败轨迹中提取可迁移经验、PromptBreeder通过突变和交叉进化提示，以及ADAS和Darwin Gödel Machine等系统递归地重新设计自我进化策略本身；3. 智能体记忆系统，如Voyager在《我的世界》中积累可重用技能库，MemGen和Mem0等维护跨任务持续演化的记忆存储。这些方法都依赖大模型固有的推理能力来分析反馈并提出改进。本文同样属于测试时自我进化的跨任务范畴，但关键区别在于：不依赖模型的涌现能力，而是通过强化学习显式训练自我进化策略，将其转化为可学习的技能。

### Q3: 论文如何解决这个问题？

论文通过提出“学习自我进化”（LSE）这一强化学习框架来解决测试时自我进化问题。其核心方法是将多轮进化问题简化为单步强化学习目标，并采用树引导的进化循环来优化上下文。

整体框架包含两个关键组件：**行动策略**（一个参数固定的基础大语言模型，负责根据当前上下文生成任务输出）和**自我进化策略**（一个可训练的LLM，负责根据历史表现反馈生成更新后的上下文）。在测试时，系统执行多轮进化：每轮从任务分布中采样一批问题，由行动策略生成答案并获得奖励反馈；自我进化策略则基于当前上下文和本轮表现摘要，生成一个改进后的新上下文。

架构设计的创新点主要体现在两个方面。首先，**树引导的进化循环**取代了简单的线性进化链。系统维护一个进化树，每个节点存储一个上下文及其在固定验证集上的平均奖励。每轮使用上置信界（UCB）公式选择节点进行扩展，从而允许系统回溯并探索历史上更有潜力的进化路径，避免陷入局部最优。

其次，**LSE训练框架**的核心是设计了一个基于改进幅度的单步RL目标。具体而言，训练自我进化策略时，其奖励信号定义为更新后上下文与更新前上下文在验证集上性能的差值（即改进量），而非更新后的绝对性能。这直接激励策略产生有效的改进，而不受初始上下文性能高低的影响。在策略梯度优化中，改进前的性能作为一个已知的、与动作无关的基线，无需训练额外的价值网络或进行分组归一化，简化了训练并稳定了梯度更新。为了模拟测试时的多轮进化场景，训练数据通过运行多轮树搜索来构建，并从中随机采样节点作为训练起始点，使策略学会改进由自身先前编辑产生的各种上下文。

关键技术还包括**基于提示的更新机制**，即自我进化策略仅修改上下文中的指令部分，而保持模型参数和其他上下文组件冻结。这避免了测试时的梯度计算和灾难性遗忘问题，并将进化任务转化为可训练的自然语言推理任务。

### Q4: 论文做了哪些实验？

论文在文本到SQL生成和通用问答两个任务领域进行了实验。实验设置方面，主要使用Qwen3-4B-Instruct作为动作策略（生成最终答案的模型）和自我进化策略（优化上下文的模型）。在文本到SQL任务中，使用BIRD数据集，并在其训练集上训练，在BIRD-SQL Mini-Dev中随机选取的五个数据库（金融、毒理学、代码库、一级方程式、卡牌游戏）上评估。在通用问答任务中，使用SuperGPQA进行训练，并在MMLU-Redux的十个学科主题（如商业伦理、哲学、经济学等）上评估。对比方法包括：1）前沿闭源模型（GPT-5和Claude Sonnet 4.5）作为自我进化策略；2）两种提示优化方法GEPA（基于反射和进化搜索）和TextGrad（基于文本梯度下降）。主要结果显示，在BIRD上，LSE方法的平均执行准确率达到67.3%，优于GPT-5（65.2%）、Claude Sonnet 4.5（64.5%）、GEPA（62.8%）和TextGrad（63.1%）。在MMLU-Redux上，LSE平均准确率为73.3%，与GEPA（73.0%）相当，优于GPT-5（72.5%）、Claude Sonnet 4.5（72.0%）和TextGrad（69.1%）。消融实验表明，基于改进的奖励设计（$A_{LSE}$）比标准GRPO优势（$A_{GRPO}$）在BIRD上带来4.3%的性能提升；树搜索（UCB）策略比线性链策略在BIRD和MMLU-Redux上分别提升2.4%和2.2%。此外，实验还证明训练后的LSE策略可以迁移，用于指导另一个专门模型（Arctic-Text2SQL-R1-7B），使其在BIRD上的平均准确率从57.7%提升至64.4%。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度进一步探索。首先，LSE将多步进化问题简化为单步RL目标，将探索完全委托给测试时的树搜索算法。未来可研究多步轨迹的联合优化，以学习更强大的策略，但需解决信用分配和计算成本增加的挑战。其次，当前为每个任务领域训练了独立的策略，开发能跨多样化任务泛化的单一策略是自然延伸，但这可能需要大规模跨领域训练数据。第三，进化被限制在上下文的指令字段，未来可探索整合工具、技能库和外部记忆等组件，甚至将LSE框架与潜在空间或参数空间的更新相结合。此外，训练和评估环境的规模相对较小，构建有效的测试时自进化环境本身是一个开放问题，需要既有足够反馈的问题，又需问题间共享足够结构以使进化有意义。因此，开发更原则化、可扩展的环境构建与评估方法是关键方向。最后，可探索将自进化技能与模型的其他元学习能力结合，形成更通用的自我改进系统。

### Q6: 总结一下论文的主要内容

该论文提出了“学习自我进化”（LSE）这一强化学习框架，旨在训练大型语言模型（LLM）在测试时自主优化其上下文提示。其核心问题是解决现有方法依赖模型固有推理能力、未对其进行显式训练以完成“测试时自我进化”任务（即模型根据已见问题的反馈迭代改进上下文，以提升新问题上的表现）的不足。

LSE的核心方法是将多步进化问题简化为单步强化学习目标：每次对上下文的编辑都根据下游任务性能的提升获得奖励，并辅以树引导的进化循环来实施。该方法使模型学习将自我进化作为一种可习得的技能。

主要结论是，在文本到SQL生成（BIRD）和通用问答（MMLU-Redux）任务上，一个仅40亿参数的LSE训练模型，其性能超越了由GPT-5和Claude Sonnet 4.5驱动的自我进化策略，也优于GEPA、TextGrad等提示优化方法，并且无需额外训练即可迁移以指导其他模型。这证明了通过训练让模型掌握自我进化技能的有效性和优越性。
