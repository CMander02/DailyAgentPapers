---
title: "P^2O: Joint Policy and Prompt Optimization"
authors:
  - "Xinyu Lu"
  - "Kaiqi Zhang"
  - "Jinglin Yang"
  - "Boxi Cao"
  - "Yaojie Lu"
  - "Hongyu Lin"
  - "Min He"
  - "Xianpei Han"
  - "Le Sun"
date: "2026-03-23"
arxiv_id: "2603.21877"
arxiv_url: "https://arxiv.org/abs/2603.21877"
pdf_url: "https://arxiv.org/pdf/2603.21877v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "强化学习"
  - "提示优化"
  - "策略优化"
  - "LLM推理"
  - "训练方法"
  - "泛化能力"
relevance_score: 8.0
---

# P^2O: Joint Policy and Prompt Optimization

## 原始摘要

Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a powerful paradigm for enhancing the reasoning capabilities of Large Language Models (LLMs). However, vanilla RLVR suffers from inefficient exploration, particularly when confronting "hard samples" that yield nearzero success rates. In such scenarios, the reliance on sparse outcome rewards typically results in zero-advantage estimates, effectively starving the model of supervision signals despite the high informational value of these instances. To address this, we propose P^2O, a novel framework that synergizes Prompt Optimization with Policy Optimization. P^2O identifies hard samples during training iterations and leverages the GeneticPareto (GEPA) prompt optimization algorithm to evolve prompt templates that guide the model toward discovering successful trajectories. Crucially, unlike traditional prompt engineering methods that rely on input augmentation, P^2O distills the reasoning gains induced by these optimized prompts directly into the model parameters. This mechanism provides denser positive supervision signals for hard samples and accelerates convergence. Extensive experiments demonstrate that P^2O not only achieves superior performance on in-distribution datasets but also exhibits strong generalization, yielding substantial improvements on out-of-distribution benchmarks (+4.7% avg.).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决强化学习与可验证奖励（RLVR）范式在提升大语言模型（LLMs）推理能力时，因探索效率低下而导致的“困难样本”学习瓶颈问题。研究背景是，RLVR利用基于结果的确定性反馈来对齐模型的推理轨迹，使其能超越模仿学习的限制，自主探索解空间。然而，现有方法（即标准的RLVR）在处理训练数据中混合的“简单样本”和“困难样本”时存在严重不足：对于模型在多次尝试中成功率近乎为零的困难样本，稀疏的结果奖励通常导致优势估计为零，使得模型无法获得有效的梯度反馈，从而过度依赖简单样本的信号。这导致模型陷入局部最优，即擅长简单任务但无法解决复杂推理问题。

现有缓解探索挑战的方法，如课程学习和奖励塑造，分别存在需要启发式且计算昂贵的进度安排，或依赖领域专家知识的问题。近期提示优化方法的成功提供了一种新思路，表明即使模型在标准策略下无法解决难题，一个精心优化的提示往往能引导出正确的推理路径，说明解决方案存在于模型的潜在搜索空间中，但标准梯度上升无法触及。

因此，本文要解决的核心问题是：如何克服RLVR在困难样本上的探索瓶颈，使模型不仅能借助外部提示临时“跳”出局部最优，还能将这些能力内化到模型参数中。为此，论文提出了P^2O框架，它协同进行策略优化和提示优化，通过识别困难样本并利用遗传帕累托算法进化提示模板来引导模型发现成功轨迹，然后将这些优化提示所引发的推理增益直接“蒸馏”到模型参数中，从而为困难样本提供更密集的正监督信号，加速收敛，并最终提升模型在分布内和分布外任务上的性能与泛化能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大方向。在方法类中，强化学习与可验证奖励（RLVR）和群体相对策略优化（GRPO）是LLM推理对齐的主流方法，它们通过群体基线和结果验证来稳定训练，但在稀疏或误导性奖励场景中探索效率低下。DAPO等方法通过剪枝特定准确率的提示来提升稳定性，但仍局限于在固定的任务提示（即固定流形）上优化策略。另一类方法是基于提示或引导的策略，如使用强模型引导、经验回放数据、专家解决方案或Critique-GRPO利用反馈信号来辅助推理。然而，这些方法通常依赖启发式获取的提示或从数据集中提取的专家轨迹片段，其引导本身是静态的，缺乏优化过程。

本文提出的P^2O与上述工作的核心区别在于，它将任务提示本身视为可优化的参数，通过遗传帕累托（GEPA）算法动态进化提示模板，从而主动引导模型发现成功轨迹，并将由此获得的推理收益蒸馏到模型参数中。这实现了策略优化与提示优化的协同进化，突破了现有方法仅优化策略或依赖静态引导的局限，为处理困难样本提供了更密集的监督信号，并增强了泛化能力。

### Q3: 论文如何解决这个问题？

P^2O通过联合优化策略和提示来解决RLVR中因稀疏奖励导致的探索效率低下问题，特别是针对成功率近乎为零的“困难样本”。其核心思想是将提示模板视为动态隐变量，与策略参数协同优化，形成一个交替最大化框架。

整体框架分为两个交替进行的阶段：策略优化与上下文蒸馏，以及进化式提示优化。在策略优化阶段，模型固定当前提示模板集，通过上下文蒸馏技术将优化提示所激发的推理能力内化到策略参数中。具体而言，对于困难样本，模型使用采样到的提示模板生成增强输入来引导轨迹生成，但策略梯度更新时却基于原始输入计算。这种“解耦”迫使模型学习独立于辅助提示的内在推理能力，实现了从“教师”分布到“学生”分布的知识蒸馏。同时，该阶段会动态挖掘困难样本集，为下一阶段的提示优化提供目标。

在进化式提示优化阶段，模型固定策略参数，使用GEPA算法优化提示模板集以攻克新识别的困难样本。GEPA的创新之处在于其“反思式进化”机制：它利用一个参考模型作为变异算子，基于失败预测和真实答案生成反馈，从而在语义空间中进行“梯度下降”以产生改进的候选提示。此外，算法采用帕累托优化在开发集上维护一个多样化的非支配候选模板集合，而非只保留单一最优模板。最后通过贪心集合覆盖策略选择最小帕累托集，并为每个困难样本分配特定的模板，用于下一轮训练。

该框架的关键技术创新点包括：1) 将提示作为隐变量的联合优化公式，将原始问题转化为一个双层优化问题；2) 上下文蒸馏机制，使模型最终摆脱对推理时提示的依赖，提升了泛化能力；3) 基于遗传帕累托的反思式提示进化算法，能高效生成多样且有针对性的提示模板。通过这两个阶段的迭代循环，P^2O建立了一个自我改进的良性循环：策略吸收提示诱导的能力而增强，进化出的新提示又能针对策略剩余的弱点进行精准打击，从而有效破解了困难样本上的探索瓶颈，提供了更密集的正监督信号，加速了收敛。

### Q4: 论文做了哪些实验？

论文在数学推理任务上进行了全面的实验验证。实验设置方面，以Qwen3-4B为骨干模型，结合GRPO与一步离策略方法进行训练，最大学习率为1e-6，批次大小为128，共训练5个周期。生成长度上限为12k tokens，在rollout阶段使用温度0.6，每个提示采样K=6条轨迹。研究对比了P^2O框架的两种变体：使用参考模型自身进行反思的P^2O_{Self-Ref}和使用更强外部模型Kimi-K2提供反馈的P^2O_{Teacher-Ref}。

使用的数据集包括两个各含5,000个样本的数学数据集：从DeepScaler随机采样的子集，以及从DeepMath中选取难度≥7的样本构成的子集。评估在六个具有挑战性的数学基准上进行：AIME24、AIME25、AMC、MATH500、Minerva和Olympiad。采用严格的二元奖励机制，仅当答案格式正确且与真实答案一致时才给予奖励1。

主要对比方法包括骨干模型Qwen3-4B、GRPO基线以及P^2O的不同变体。关键结果显示，在DeepScaler-5K数据集上，P^2O_{Teacher-Ref}取得了最佳平均准确率65.2%，相比GRPO基线（60.5%）提升了4.7%。在DeepMath-5K数据集上，P^2O_{Self-Ref}取得了61.7%的平均准确率，相比GRPO基线（54.8%）提升了6.9%。在高难度任务上提升尤为显著，例如在AIME24和AIME25基准上，P^2O相比GRPO分别提升了12.9%和11.7%。

消融实验证实了上下文蒸馏和组内提示多样性的重要性。移除上下文蒸馏会导致性能严重下降至55.6%，甚至低于GRPO基线。而使用单一模板的变体（64.2%）也低于使用多样模板的完整P^2O（65.2%），尤其是在高难度任务上差异明显。学习曲线分析表明，优化的提示能持续维持更高的训练奖励，并转化为验证准确率的稳定提升。

### Q5: 有什么可以进一步探索的点？

该论文提出的P^2O框架在联合优化提示与策略方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其依赖遗传算法进行提示演化，计算成本较高，且可能陷入局部最优；未来可探索更高效的提示搜索方法，如基于梯度的提示优化或元学习技术，以加速演化过程并提升泛化能力。其次，当前方法主要针对数学推理任务，在其他复杂领域（如代码生成或多模态推理）的适用性有待验证；扩展至多任务或跨模态场景将是一个重要方向。此外，框架对“困难样本”的识别依赖启发式规则，可能不够精准；结合不确定性估计或主动学习机制，可更动态地定位训练瓶颈。最后，提示优化的收益蒸馏到模型参数的过程仍较粗糙，未来可设计更精细的知识固化机制，例如分层蒸馏或渐进式融合，以进一步提升收敛效率和稳定性。这些改进有望增强框架的扩展性和实用性。

### Q6: 总结一下论文的主要内容

该论文针对强化学习与可验证奖励（RLVR）范式在训练大语言模型时面临的探索效率低下问题，尤其是面对成功率极低的“困难样本”时，稀疏的结局奖励导致优势估计为零，模型缺乏有效监督信号。为此，作者提出了P^2O框架，将提示优化与策略优化协同进行。其核心方法是：在训练迭代中识别困难样本，并利用遗传帕累托（GEPA）算法进化提示模板，以引导模型发现成功轨迹。关键创新在于，P^2O并非依赖传统的输入增强式提示工程，而是将这些优化提示所引发的推理收益直接“蒸馏”到模型参数中。这为困难样本提供了更密集的正向监督信号，加速了收敛。实验表明，P^2O不仅在分布内数据集上表现更优，还具有强大的泛化能力，在分布外基准上平均提升4.7%。该工作的主要贡献在于通过联合优化提示与策略，有效解决了RLVR在困难样本上的探索瓶颈，提升了训练效率和模型性能。
