---
title: "Generalization in Online Reinforcement Learning for Mobile Agents"
authors:
  - "Li Gu"
  - "Zihuan Jiang"
  - "Zhixiang Chi"
  - "Huan Liu"
  - "Ziqiang Wang"
  - "Yuanhao Yu"
  - "Glen Berseth"
  - "Yang Wang"
date: "2026-03-08"
arxiv_id: "2603.07432"
arxiv_url: "https://arxiv.org/abs/2603.07432"
pdf_url: "https://arxiv.org/pdf/2603.07432v1"
github_url: "https://github.com/zihuanjiang/AndroidWorld-Generalization"
categories:
  - "cs.CV"
  - "cs.CL"
  - "cs.HC"
  - "cs.LG"
tags:
  - "Mobile Agent"
  - "GUI Agent"
  - "Reinforcement Learning"
  - "Vision-Language Model"
  - "Benchmark"
  - "Generalization"
  - "AndroidWorld"
relevance_score: 8.0
---

# Generalization in Online Reinforcement Learning for Mobile Agents

## 原始摘要

Graphical user interface (GUI)-based mobile agents automate digital tasks on mobile devices by interpreting natural-language instructions and interacting with the screen. While recent methods apply reinforcement learning (RL) to train vision-language-model(VLM) agents in interactive environments with a primary focus on performance, generalization remains underexplored due to the lack of standardized benchmarks and open-source RL systems. In this work, we formalize the problem as a Contextual Markov Decision Process (CMDP) and introduce \textbf{AndroidWorld-Generalization}, a benchmark with three increasingly challenging regimes for evaluating zero-shot generalization to unseen task instances, templates, and applications. We further propose an RL training system that integrates Group Relative Policy Optimization (GRPO) with a scalable rollout collection system, consisting of containerized infrastructure and asynchronous execution % , and error recovery to support reliable and efficient training. Experiments on AndroidWorld-Generalization show that RL enables a 7B-parameter VLM agent to surpass supervised fine-tuning baselines, yielding a 26.1\% improvement on unseen instances but only limited gains on unseen templates (15.7\%) and apps (8.3\%), underscoring the challenges of generalization. As a preliminary step, we demonstrate that few-shot adaptation at test-time improves performance on unseen apps, motivating future research in this direction. To support reproducibility and fair comparison, we open-source the full RL training system, including the environment, task suite, models, prompt configurations, and the underlying infrastructure \footnote{https://github.com/zihuanjiang/AndroidWorld-Generalization}.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在系统性地研究基于图形用户界面（GUI）的移动智能体在在线强化学习（RL）中的泛化能力问题。研究背景是，随着大视觉语言模型（VLM）的发展，移动智能体能够通过自然语言指令自动化操作移动设备，但现有方法主要关注在已知任务上的性能提升，而对其在动态、开放环境中处理未见场景（如新任务、新界面布局或新应用）的鲁棒性探索不足。

现有方法存在两个主要不足。首先，在评估方面，现有基准测试大多没有明确的训练集和测试集划分，导致研究要么在相同的评估任务上进行训练和测试（无法评估泛化），要么构建合成训练任务时无法确保训练-测试数据无泄漏，这使得系统化研究泛化变得困难。其次，在技术实现上，领域内缺乏一个面向真实移动环境的开源RL训练系统，现有工作要么闭源，要么仅发布模型权重，而智能体性能还严重依赖于提示模板、智能体逻辑和训练方案等未公开的细节。此外，构建可靠、高效的RL系统面临工程挑战，因为移动环境计算成本高、易延迟且易崩溃。

因此，本文要解决的核心问题是：如何在一个标准化的框架下，评估并提升移动智能体在在线强化学习中对**未见任务实例、任务模板和应用程序**的零样本泛化能力。为此，论文将问题形式化为上下文马尔可夫决策过程（CMDP），并引入了**AndroidWorld-Generalization**基准测试，该基准定义了三个难度递增的泛化场景。同时，论文开发了首个完全开源的RL训练系统，集成了GRPO算法与可扩展的模拟器交互基础设施，以支持可复现的研究和公平比较，从而填补该领域在系统性泛化研究和开源工具方面的空白。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于GUI的移动智能体、面向大语言模型智能体的强化学习，以及强化学习中的泛化评测基准。

在**基于GUI的移动智能体**领域，现有工作主要分为三类：基于提示工程的方法通过编排多个专有视觉语言模型构建决策流程，但成本高、适应性有限；离线方法通过在大型标注或合成轨迹数据上对单一模型进行后训练来编码领域能力，但其评估局限于单步准确性，无法衡量长程任务成功率；在线强化学习方法则允许智能体在动态环境中交互并通过奖励反馈优化策略，但现有评测基准缺乏标准化的训练环境和未见过的上下文，限制了系统性研究。

在**面向LLM智能体的强化学习**方面，RL已被证明能有效微调LLM处理推理任务，并扩展到多轮决策中。早期工作通过在线RL将LLM与文本具身环境对齐，近期研究则将RL引入更真实的基于GUI的环境（如网页和计算机操作）。然而，在移动智能体领域，相关工作仍较少：离线方法依赖静态数据集，无法捕捉完整环境动态；在线方法则探索基于交互的训练，但主要关注性能提升，忽视了在未见场景下的泛化能力。

在**强化学习的泛化评测基准**领域，泛化通常被形式化为上下文马尔可夫决策过程。现有基准通常采用程序化生成或可控的环境参数变化来实现系统评估。近期在网页导航、计算机使用等真实任务领域也提出了新基准，但它们主要提供评估集，缺乏标准化的训练-测试划分。尽管有工作尝试扩充测试集，但仍未能充分捕捉环境多样性。一项并行工作探讨了移动环境中图标位置、语言等多因素的泛化，但未涉及强化学习。

**本文与上述工作的关系与区别**在于：本文聚焦于移动智能体在线RL中的泛化问题，这在前述研究中被忽视。为此，本文提出了一个专门用于评估零样本泛化的标准化基准（AndroidWorld-Generalization），并构建了一个集成了GRPO和可扩展交互收集系统的完整RL训练框架。与仅关注性能或缺乏系统泛化评测的先前工作相比，本文首次在移动智能体领域系统性地形式化并研究了从实例到应用层级的泛化挑战。

### Q3: 论文如何解决这个问题？

论文通过构建一个集成了高效在线强化学习算法与可扩展交互数据收集系统的完整训练框架来解决移动智能体泛化能力不足的问题。其核心方法是将任务形式化为上下文马尔可夫决策过程，并采用分组相对策略优化算法进行训练。

整体框架包含两大核心部分：基于GRPO的智能体策略训练模块和可扩展的交互数据收集系统。主要组件包括：1）策略模型，采用Qwen2-VL-7B架构，并利用UI-TARS权重进行初始化，以注入领域先验知识；2）GRPO算法，作为在线强化学习的核心，它通过采样一组轨迹并计算归一化的轨迹级优势函数来更新策略，有效处理了仅有的二元终端奖励信号；3）容器化基础设施，每个Android环境运行在独立的Docker容器中，提供资源隔离和故障容错，并通过HTTP接口与策略模型解耦；4）异步交互机制，允许各个环境独立执行，消除了全局同步屏障，实现了环境执行与动作生成的流水线操作，大幅提升了GPU利用率和系统吞吐量。

关键技术细节和创新点在于：首先，论文创新性地将GRPO算法应用于移动智能体训练，通过计算组内归一化的轨迹级优势并广播到每个时间步，解决了稀疏奖励下的策略优化问题。其次，在系统设计上，通过容器化技术实现了环境与训练器的物理和逻辑解耦，避免了因单个环境崩溃而导致整个训练过程中断的问题，显著提升了训练的可靠性。最后，异步交互收集机制是关键的性能优化，它根据各环境执行速度动态调度，避免了快速环境的空闲等待，从而最大化单位时间内的智能体交互步数，为大规模训练提供了基础。这些方法共同构成了一个可靠且高效的训练系统，为系统性地研究移动智能体的泛化能力提供了必要的基础设施。

### Q4: 论文做了哪些实验？

论文实验围绕四个核心问题展开，旨在评估在线强化学习（RL）对移动智能体决策能力、泛化性能及训练效率的提升。

**实验设置**：实验在AndroidWorld-Generalization基准上进行，该基准包含三个泛化难度递增的测试体系：未见过的任务实例（Unseen Instance）、未见过的任务模板（Unseen Template）和未见过的应用程序（Unseen App）。基础模型为UI-Tars-7B-SFT，使用Android 13模拟器，每个任务实例生成8条轨迹（最多20步）。训练采用16个并行环境，使用Adam优化器（学习率1e-6），并在两个NVIDIA H100-80GB GPU上进行。

**数据集/基准测试**：主要使用AndroidWorld-Generalization基准。评估时，在“未见实例”体系中将评估集扩展到所有116个模板以保持与原始AndroidWorld及先前基线的可比性。

**对比方法**：将提出的RL训练方法（结合了课程学习的Group Relative Policy Optimization, GRPO）与多种基线进行比较，包括：(a) 基于提示的专有VLM智能体（如GPT-4o、Claude Computer Use）；(b) 在静态人类或合成演示上进行监督微调（SFT）的模型（如UI-TARS-7B-SFT、UI-TARS-72B-SFT）；(c) 其他近期RL方法。同时，也对PPO算法进行了评估以证明训练系统的算法无关性。

**主要结果与关键指标**：
1.  **决策能力提升（Q1）**：RL方法相比SFT基线在“未见实例”上实现了26.1%的平均成功率提升（从23.0%提升至49.1%）。在不同难度级别上均有一致提升：简单任务提升28.4%，中等任务提升26.8%，困难任务提升17.5%。该方法甚至超越了使用更大参数模型（如UI-TARS-72B-SFT）的基线。
2.  **泛化能力评估（Q2）**：在三个泛化体系上，RL均带来提升，但提升幅度随泛化难度增加而显著减小：在“未见实例”上提升21.8%，在“未见模板”上提升15.7%，在“未见应用”上仅提升8.3%。这表明泛化到新模板和应用仍然极具挑战。
3.  **测试时少样本适应（Q3）**：初步实验表明，在部署时使用有限的交互数据进行少样本微调，可以提升在“未见应用”上的性能，这为未来研究指明了方向。
4.  **训练系统效率（Q4）**：通过消融实验证明，所提出的异步轨迹收集系统相比朴素的AndroidWorld实现显著加速了RL训练（具体加速倍数在提供文本中未明确给出，但提及进行了量化评估）。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于，尽管在线强化学习（RL）在未见过的任务实例上取得了显著提升（26.1%），但在更具挑战性的泛化场景——未见过的任务模板（15.7%）和未见过的应用程序（8.3%）上——性能增益有限且很快达到瓶颈。这表明当前方法在跨任务结构和跨应用领域的技能迁移能力仍然不足。此外，实验主要基于7B参数模型，更大规模模型下的RL训练效率和泛化能力尚不明确。

未来研究方向可以从以下几个维度深入探索：
1.  **提升跨结构与跨领域泛化能力**：研究更高效的元学习、课程学习或模块化策略，使智能体能够从有限样本中快速抽象出可迁移的核心操作技能（如“识别-选择-确认”模式），以应对全新的应用界面和任务逻辑。
2.  **改进测试时自适应机制**：论文初步验证了测试时少量样本微调（few-shot adaptation）的有效性，未来可系统探索更高效的在线适应方法，例如基于演示的模仿学习、上下文策略优化或动态提示工程，使智能体能在部署中持续学习。
3.  **探索多模态表示与决策的协同优化**：当前基于VLM的智能体可能受限于视觉语言模型本身的泛化能力。未来可研究专为交互任务设计的表示学习方法，例如分离界面结构理解、对象功能语义和操作序列模式，从而提升决策的鲁棒性。
4.  **扩展基准与算法评估**：需要构建更复杂、多样化的移动环境基准，涵盖多轮对话、长 horizon 任务和异常恢复场景。同时，应系统比较不同RL算法（如PPO与GRPO）在泛化性能上的差异，并探索与模型规模、训练数据效率的关联。

### Q6: 总结一下论文的主要内容

该论文针对基于图形用户界面的移动智能体在泛化能力方面研究不足的问题，提出了一个形式化框架和系统性解决方案。核心贡献在于将移动任务自动化问题定义为情境马尔可夫决策过程，并构建了**AndroidWorld-Generalization**基准测试，该基准包含任务实例、模板和应用三个由易到难的零样本泛化评估体系。方法上，论文设计了一套集成群组相对策略优化的强化学习训练系统，配合容器化、异步执行的高效收集架构。实验表明，强化学习能使一个70亿参数的视觉语言模型智能体超越监督微调基线，在未见过的任务实例上性能提升26.1%，但在未见过的模板和应用上提升有限（分别为15.7%和8.3%），这揭示了更高层次泛化的严峻挑战。论文还初步验证了测试时少量样本适配能提升在未知应用上的表现，为未来研究指明了方向。其开源完整的训练系统为领域内的可复现性和公平比较奠定了基础。
