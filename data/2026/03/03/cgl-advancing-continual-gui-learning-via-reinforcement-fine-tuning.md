---
title: "CGL: Advancing Continual GUI Learning via Reinforcement Fine-Tuning"
authors:
  - "Zhenquan Yao"
  - "Zitong Huang"
  - "Yihan Zeng"
  - "Jianhua Han"
  - "Hang Xu"
date: "2026-03-03"
arxiv_id: "2603.02951"
arxiv_url: "https://arxiv.org/abs/2603.02951"
pdf_url: "https://arxiv.org/pdf/2603.02951v1"
categories:
  - "cs.LG"
  - "cs.CV"
tags:
  - "Learning & Optimization"
  - "Tool Use & API Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Learning & Optimization"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "Continual GUI Learning (CGL) framework, SFT proportion adjustment mechanism, gradient surgery strategy"
  primary_benchmark: "AndroidControl-CL"
---

# CGL: Advancing Continual GUI Learning via Reinforcement Fine-Tuning

## 原始摘要

Graphical User Interface (GUI) Agents, benefiting from recent advances in multimodal large language models (MLLM), have achieved significant development. However, due to the frequent updates of GUI applications, adapting to new tasks without forgetting old tasks in GUI continual learning remains an open problem. In this work, we reveal that while Supervised Fine-Tuning (SFT) facilitates fast adaptation, it often triggers knowledge overwriting, whereas Reinforcement Learning (RL) demonstrates an inherent resilience that shields prior interaction logic from erasure. Based on this insight, we propose a \textbf{C}ontinual \textbf{G}UI \textbf{L}earning (CGL) framework that dynamically balances adaptation efficiency and skill retention by enhancing the synergy between SFT and RL. Specifically, we introduce an SFT proportion adjustment mechanism guided by policy entropy to dynamically control the weight allocation between the SFT and RL training phases. To resolve explicit gradient interference, we further develop a specialized gradient surgery strategy. By projecting exploratory SFT gradients onto GRPO-based anchor gradients, our method explicitly clips the components of SFT gradients that conflict with GRPO. On top of that, we establish an AndroidControl-CL benchmark, which divides GUI applications into distinct task groups to effectively simulate and evaluate the performance of continual GUI learning. Experimental results demonstrate the effectiveness of our proposed CGL framework across continual learning scenarios. The benchmark, code, and model will be made publicly available.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决图形用户界面（GUI）智能体在持续学习（Continual Learning, CL）场景下面临的“稳定性-可塑性困境”，即如何让智能体在快速适应新任务或新界面时，避免遗忘已掌握的旧任务（灾难性遗忘）。研究背景是，得益于多模态大语言模型（MLLM）的发展，GUI智能体在自动化软件交互方面取得了显著进展。然而，现实世界的GUI应用（如手机App）频繁更新迭代，静态训练的智能体难以跟上这种动态变化。

现有方法主要依赖监督微调（SFT）或强化学习（RL，如GRPO），但各有不足。SFT虽然能快速适应新任务，但其激进的梯度更新会覆盖模型已学到的旧知识（即“知识覆写”），导致灾难性遗忘。RL方法（如GRPO）则展现出更强的稳定性，能保护已习得的交互逻辑不被轻易擦除，但其学习效率低、样本复杂度高，导致在新环境中的适应速度过慢，无法满足实际应用对效率的要求。

因此，本文要解决的核心问题是：如何设计一个持续学习框架，有效调和SFT的快速适应能力与RL的稳定记忆能力之间的矛盾，使GUI智能体在动态演化的环境中，既能高效学习新技能，又能稳固保持旧技能。为此，论文提出了持续GUI学习（CGL）框架，通过基于策略熵的动态SFT比例调整机制和专门的梯度手术策略，来协同优化适应效率与技能保留，并在新构建的AndroidControl-CL基准上验证其有效性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：持续学习方法和GUI智能体方法。

在**持续学习方法**方面，传统方法主要包括三类：基于正则化的方法（通过重要性量化约束关键参数更新，轻量但面临重要性度量和损失权重平衡的挑战）、动态架构方法（冻结旧参数并添加任务特定子网络，理论上避免遗忘但导致模型尺寸线性增长）和基于排练的方法（使用记忆缓冲区混合新旧任务数据，核心挑战在于平衡缓冲区大小）。针对视觉语言模型（VLM）的持续学习，现有方案包括多模态回放（MMRE，采用显式或隐式回放，分别受限于存储消耗和伪数据质量）、跨模态正则化（CREG，添加约束项以保留旧的跨模态关联，需平衡约束强度）和参数高效适应（PEA，使用轻量模块不修改核心参数以保留零样本能力，但可能因可调参数有限而难以处理复杂任务）。近期工作还提出了基于rollout的实例过滤方法（RIF-RFT）以增强VLM持续后训练的稳定性和效率。本文提出的CGL框架与这些方法不同，它并非直接采用上述任一范式，而是通过动态平衡监督微调（SFT）和强化学习（RL）来协同解决适应与遗忘问题，并引入了梯度手术等新策略。

在**GUI智能体方法**方面，现有工作主要遵循两种技术范式：一是以SFT为主导的数据驱动范式（如UI-TARS），通过在大型标注GUI语料库上微调专用多模态模型来映射UI状态到动作，虽在基准测试上表现强劲但泛化能力有限；二是基于RL的GUI智能体（受DeepSeek-R1启发），例如UI-R1和GUI-G1探索了类似R1-zero的视觉定位，GUI-G2引入了高斯奖励建模，而CRAFT-GUI则提出了课程强化方法以提升训练稳定性和准确性。这些现有研究均聚焦于静态任务场景，未解决GUI应用频繁更新所需的持续适应问题。本文则首次在GUI持续学习的动态设定下，分析了SFT、RL及其整合如何影响模型能力，并提出了首个专门针对此场景的框架（CGL）和评测基准（AndroidControl-CL），填补了这一空白。

### Q3: 论文如何解决这个问题？

论文提出的CGL框架通过协同监督微调（SFT）和强化学习（RL）来解决GUI持续学习中的灾难性遗忘问题。其核心方法是构建一个动态平衡适应效率与技能保留的联合训练框架，整体架构基于多模态大语言模型（MLLM）作为策略网络。

框架包含三个关键模块：首先，**错误感知路由**机制用于缓解RL探索中的奖励稀疏问题。当对给定指令采样所有轨迹均无法获得理想奖励时，系统判定RL探索失败，动态切换到SFT模式，利用真实演示数据提供监督信号，快速引导模型学习新交互模式，打破探索僵局。

其次，**熵调节调优**模块通过基于策略熵的动态权重因子λ来调控SFT与RL（采用GRPO算法）的损失贡献比例。其设计包含两个阶段：在初始“熵注入”阶段，线性增加λ，使SFT主导更新，通过向低概率的正确动作注入大幅正更新，打破模型对错误动作的病理偏置，增加策略熵以促进探索；在后续“熵衰减”阶段，当模型获得基本任务能力后，λ随熵值呈指数衰减，使GRPO更新主导优化。GRPO通过基于优势函数强化高概率、高优势动作，产生熵减效应，从而稳定策略并固化知识，实现长期保留。

最后，**梯度手术**策略用于解决SFT与GRPO更新间的显式梯度冲突。当检测到两者梯度余弦相似度为负（角度超过90度）时，将SFT梯度投影到与GRPO梯度正交的方向上，即移除SFT梯度中与GRPO目标相冲突的分量，仅保留正交部分参与更新；若无冲突，则直接使用原SFT梯度。这有效避免了梯度干扰导致的优化不稳定与知识覆盖。

创新点在于：1）揭示了SFT易导致知识覆盖而RL具有内在抗遗忘性的洞察，并据此设计协同框架；2）提出熵指导的动态比例调整机制，实现训练阶段的自适应切换；3）开发了针对性的条件梯度手术，显式化解梯度冲突。整体优化目标为加权损失函数ℒ = ℒ_GRPO + λ(ℋ, step)·ℒ_SFT，通过上述模块的协同工作，在持续学习场景中同时实现了高效适应与旧任务技能的稳固保留。

### Q4: 论文做了哪些实验？

论文实验设置基于两个不同规模的多模态大语言模型（QwenVL2.5-3b-Instruct 和 LLaVA-OneVision-0.5b），在自建的 AndroidControl-CL 基准上进行。该基准将 GUI 应用划分为购物、生产力、通信、旅行、工具、教育、娱乐等七个任务类别，并定义了三种不同的任务顺序以模拟持续学习场景。对比方法包括标准监督微调（SFT）、结合 KL 散度约束的 SFT（SFT+KL）、结合历史数据回放的 SFT（SFT+Replay）、基于约束强化学习的 GRPO 以及近期提出的持续后训练框架 RIF-RFT。

主要结果如下：在任务顺序 1 下，所提出的 CGL 框架在 QwenVL2.5-3b 上取得了最高的平均步骤准确率（82.33%）和轨迹准确率（38.03%），同时遗忘度量（FM）接近零（-0.02），显著优于所有基线。在 LLaVA-0.5b 上，CGL 也以 77.84% 的平均步骤准确率和 24.77% 的轨迹准确率领先，FM 为 -0.52。跨三种任务顺序的实验表明，CGL 在步骤准确率（≥82.33%）和轨迹准确率（≥38.03%）上均保持最优，且在任务顺序 2 中实现了罕见的正 FM（+0.13），表明其不仅避免了遗忘，还轻微提升了旧任务性能。消融实验验证了动态 SFT 比例调整机制和梯度手术策略的有效性，逐步引入各组件后，性能持续提升。关键数据指标包括：步骤准确率、轨迹准确率以及衡量遗忘程度的 FM（越小越好，负值表示遗忘）。

### Q5: 有什么可以进一步探索的点？

本文提出的CGL框架在持续GUI学习方面取得了进展，但仍存在一些局限性和值得深入探索的方向。首先，当前方法主要针对Android GUI环境，其泛化能力有待验证，未来可扩展至iOS、Web或桌面应用等更广泛的GUI平台，以检验其普适性。其次，框架依赖于任务组的明确划分，而在真实场景中任务边界可能模糊或动态变化，因此需要研究更灵活的任务感知与增量学习机制。此外，虽然引入了基于策略熵的调整机制和梯度手术策略，但两者间的协同优化可能还不够精细，未来可探索更自适应的权重分配算法，或引入元学习来动态调整学习策略。另一个方向是增强模型的解释性，例如可视化SFT与RL在不同任务上的贡献度，以更直观地理解知识保留与覆盖的过程。最后，当前基准测试虽已构建，但可引入更复杂的任务序列和长周期学习场景，以模拟真实应用中持续且频繁的界面更新，进一步挑战模型的长期适应与抗遗忘能力。

### Q6: 总结一下论文的主要内容

该论文针对图形用户界面（GUI）智能体在应用频繁更新时面临的持续学习问题，提出了一种名为CGL的持续GUI学习框架。核心问题是现有方法在适应新任务时容易遗忘旧任务，即存在灾难性遗忘。论文发现，监督微调（SFT）虽能快速适应新任务，但会导致知识覆盖；而强化学习（RL）则表现出更强的抗遗忘性。基于此，CGL框架的核心贡献在于动态协同SFT与RL，以平衡适应效率与技能保留。方法上，首先引入基于策略熵的SFT比例调整机制，动态分配SFT与RL的训练权重；其次，提出专门的梯度手术策略，通过将探索性SFT梯度投影到基于GRPO的锚定梯度上，显式地裁剪与GRPO冲突的SFT梯度分量。此外，论文还构建了AndroidControl-CL基准测试，将GUI应用划分为不同任务组以模拟和评估持续学习性能。实验结果表明，CGL框架在多种持续学习场景中均有效，显著缓解了遗忘问题并保持了整体性能。该工作为GUI智能体的长期适应性提供了新的解决方案和评估基准。
