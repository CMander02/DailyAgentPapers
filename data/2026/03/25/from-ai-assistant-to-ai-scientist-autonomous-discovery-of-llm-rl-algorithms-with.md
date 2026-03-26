---
title: "From AI Assistant to AI Scientist: Autonomous Discovery of LLM-RL Algorithms with LLM Agents"
authors:
  - "Sirui Xia"
  - "Yikai Zhang"
  - "Aili Chen"
  - "Siye Wu"
  - "Siyu Yuan"
  - "Yanghua Xiao"
date: "2026-03-25"
arxiv_id: "2603.23951"
arxiv_url: "https://arxiv.org/abs/2603.23951"
pdf_url: "https://arxiv.org/pdf/2603.23951v1"
categories:
  - "cs.CL"
tags:
  - "Agent 框架"
  - "自动化算法发现"
  - "策略优化"
  - "LLM 驱动的 Agent"
  - "闭环系统"
  - "强化学习"
  - "数学推理"
relevance_score: 8.5
---

# From AI Assistant to AI Scientist: Autonomous Discovery of LLM-RL Algorithms with LLM Agents

## 原始摘要

Discovering improved policy optimization algorithms for language models remains a costly manual process requiring repeated mechanism-level modification and validation. Unlike simple combinatorial code search, this problem requires searching over algorithmic mechanisms tightly coupled with training dynamics while reusing empirical evidence across iterations. We propose POISE, a closed-loop framework for automated discovery of policy optimization algorithms for language models. POISE maintains a structured, genealogically linked archive linking proposals, executable implementations, standardized evaluations, and natural-language reflections to support evidence-driven iteration. In mathematical reasoning experiments starting from GRPO, POISE evaluates 64 candidate algorithms and discovers improved mechanisms, including analytic-variance scaling and validity masking. The best variant improves weighted Overall from 47.8 to 52.5 (+4.6) and increases AIME25 pass@32 from 26.7% to 43.3%, demonstrating the feasibility of automated policy optimization discovery while supporting interpretable design principles.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）强化学习（RL）后训练中，策略优化算法设计成本高昂且依赖人工经验的问题。研究背景是，RL已成为LLM重要的后训练范式，但现有策略优化算法（如PPO、GRPO）的改进通常需要研究人员反复手动修改核心机制（如损失设计、优势估计、正则化），并进行耗时的训练与评估，整个过程计算资源消耗大、效率低下。

现有自动化研究方法（如组合代码搜索、自动化机器学习）的不足在于，它们通常将问题视为对离散程序组件的组合搜索。然而，策略优化算法的发现是一个更为复杂的任务，其核心机制与训练动态紧密耦合，微小的设计选择（如引入裁剪目标、修改优势归一化）都可能显著影响优化行为和训练稳定性。此外，算法发现不仅需要提出实现方案，还需识别哪些机制真正带来性能提升，哪些在实证评估中失败，以及如何利用累积的证据来指导后续假设。这要求一个能够系统地将实证反馈转化为可重用证据、并在迭代中传承这些证据的搜索过程。

因此，本文要解决的核心问题是：能否利用LLM自身的推理与规划能力，实现一个自动化的、证据驱动的闭环框架，以自主发现针对语言模型的、性能更优的策略优化算法，从而降低人工成本，提升发现效率，并从中提炼出可解释的设计原则。论文提出的POISE框架正是为了应对这一挑战。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为两大类：LLM驱动的科学发现和面向大语言模型的策略优化算法研究。

在**LLM驱动的科学发现**方面，相关研究致力于利用大语言模型的知识、推理和执行能力，自动化部分科研流程。该领域已从基础的实验自动化，发展到复杂的算法设计。近期出现的“AI科学家”智能体，旨在构建涵盖文献综述、编码和实验的端到端流程。此外，在想法生成的质量控制方面也取得了进展。LLM已在程序优化、定理证明、架构搜索和自动化机器学习工程等领域的明确搜索空间中展现出有效的探索能力。然而，将自动化发现扩展到语言模型策略优化的强化学习算法设计更具挑战性，因为搜索空间是组合式的、反馈是延迟且随机的，且验证需要昂贵的分布式训练。本文提出的POISE框架属于这一范畴，但它专注于解决策略优化算法设计这一特定、高成本的挑战，通过构建一个迭代进化的系统来指导LLM进行设计、验证和精炼。

在**面向大语言模型的策略优化算法**方面，相关研究旨在通过PPO及其计算高效变体GRPO等算法训练LLM以提升其推理能力。近期研究通过改进特定算法组件来增强这些基线方法，例如DAPO中的解耦裁剪、SAPO中的软自适应门控、ASPO中的非对称加权以及GMPO中的几何平均聚合。这些工作证明了针对性组件级改进的价值，但探索此类机制的组合设计空间仍主要依赖人工迭代。与这些通常手动精炼单个组件的研究不同，本文方法引入了一个LLM驱动的进化系统，旨在标准化的设置下自主发现并组合算法改进，从而实现对整个算法设计空间的自动化探索。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为POISE的闭环框架来解决自动化发现语言模型策略优化算法的问题。该框架将算法发现构建为一个证据驱动的、基于认知进化搜索的过程，其核心在于维护一个结构化的、具有谱系关联的档案库，并通过三个主要阶段循环迭代。

整体框架由三个紧密衔接的阶段构成。**第一阶段（提案生成）**：基于历史档案证据、外部文献先验和谱系信息，通过提案操作符（由大语言模型驱动）生成候选算法变体。该阶段的关键创新是“谱系优先化”机制，它通过一个综合考虑帕累托前沿强度、性能、多样性和基于高斯过程的“后代潜力”估计的获取函数来选择有潜力的父节点，避免短视地仅关注当前性能。**第二阶段（实现、验证与评估）**：通过一个标准化的评估管道，将抽象提案转化为可执行代码，并进行一致性验证和标准化评估，确保观测到的性能差异源于算法本身而非实现偏差。**第三阶段（反思分析与档案更新）**：评估后，反思分析操作符（同样由大语言模型驱动）将训练动态和指标结果转化为机制层面的诊断报告（如将KL散度尖峰与优势估计的不稳定性关联）。最后，档案更新操作符将新算法的完整记录（包括提案、实现、证据和反思）存入结构化档案，并更新谱系链接。

该框架的主要创新点在于其**认知进化搜索**范式和**结构化反思档案**。它不同于简单的组合搜索，而是通过档案持续积累关于“何种设计有效/无效及其上下文”的机制性知识，并将这些知识（以自然语言反思和结构化证据的形式）反馈给提案生成阶段，形成证据驱动的闭环。这使得搜索过程能够进行不确定性推理，并重用跨迭代的实证证据。最终，POISE从GRPO基线出发，通过评估64个候选算法，成功发现了如“解析方差缩放”和“有效性掩码”等改进机制，在数学推理任务上取得了显著性能提升，验证了自动化策略优化发现的可行性。

### Q4: 论文做了哪些实验？

论文的实验设置基于POISE框架，使用统一的VERL训练流水线，以GRPO为基线算法，采用Gemini-3-pro-preview作为智能体推理引擎，并选用Qwen2.5-Math-1.5B作为策略模型以加速迭代。训练数据来自MATH数据集3-5级的5000个样本子集，超参数固定（学习率10^-6，全局批次大小256，组大小G=8，训练8轮），使用8块80GB A100 GPU。

评估在六个数学推理基准上进行：AIME24、AIME25、AMC、MATH-500、Minerva和OlympiadBench。对于AIME系列和AMC，报告温度1.0下的pass@32；对于较大数据集，报告确定性生成的acc@1。最终计算加权Overall分数（AIME系列权重0.2，其他0.15）以衡量整体性能。

主要结果方面，研究评估了64种算法（GRPO及63种进化变体）。最佳变体VM-AV-GRPO将加权Overall从47.8提升至52.5（+4.6），其中AIME25的pass@32从26.7%大幅提升至43.3%。此外，搜索还发现了针对特定基准的优化变体，如AV-GRPO在AIME24上达到56.7，MSA-GRPO在AIME25上匹配43.3，SVE-LNA-GRPO在AMC上达到89.2。

实验还测试了通过自然语言指令引导搜索的能力，例如引入长度压缩约束。在此约束下，10个变体中有6个降低了平均响应长度，其中4个（如DACE-GRPO）在缩短响应的同时提升了Overall分数。DACE-GRPO将平均输出长度从473.6词降至335.7词（减少29.1%），Overall提升至51.7（+3.9），展示了在精度-长度权衡空间中有效引导搜索的可行性。

### Q5: 有什么可以进一步探索的点？

本文提出的POISE框架在自动化搜索强化学习算法方面展现了潜力，但仍存在一些局限和值得深入探索的方向。首先，计算成本高昂是主要瓶颈，每个候选算法都需要端到端训练和评估，限制了搜索的广度与深度。未来可探索更高效的评估方法，例如利用课程学习、元学习或构建轻量级代理环境进行快速预筛选，以在有限预算内探索更复杂的算法空间。其次，当前验证集中于数学推理任务，其泛化能力有待检验。未来需将发现机制迁移到代码生成、开放域对话等多样场景，并研究不同模型规模下的表现，以验证其普适性。再者，机制解释仍基于相关性分析，缺乏严格的因果验证。可引入更精细的消融实验或因果推断框架，明确各组件对性能增益的具体贡献。此外，搜索空间的设计本身可能受限，未来可结合符号回归或神经架构搜索技术，自动生成更新颖的算法组件，超越当前基于GRPO的变体。最后，框架的自主性可进一步提升，例如让智能体自主定义评估指标或设计多目标优化策略，实现从“算法发现”到“科学发现”的跨越。

### Q6: 总结一下论文的主要内容

该论文提出了POISE框架，旨在将语言模型策略优化算法的发现过程从手动试错转变为结构化的自动化闭环流程。核心问题是自动发现改进的策略优化算法，以降低人工设计的高成本和重复性。POISE通过维护一个包含提案、可执行实现、标准化评估和自然语言反思的谱系关联档案，支持证据驱动的迭代搜索，从而在紧密耦合训练动态的算法机制空间中高效探索。

方法上，POISE组织为提案、实现、验证、评估和反思的循环，利用LLM智能体自主生成和评估候选算法。在数学推理实验中，从GRPO基线出发，框架评估了64个候选算法，发现了分析方差缩放和有效性掩码等改进机制。主要结论显示，最佳变体将加权Overall分数从47.8提升至52.5，AIME25 pass@32从26.7%提高到43.3%，验证了自动化发现的可行性。此外，框架揭示了信号解耦、条件归一化和正确性优先效率塑造等可解释设计原则，表明算法设计可部分转化为证据驱动的迭代过程，补充了传统手动设计。
