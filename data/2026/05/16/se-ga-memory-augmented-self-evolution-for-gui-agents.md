---
title: "SE-GA: Memory-Augmented Self-Evolution for GUI Agents"
authors:
  - "Shilong Jin"
  - "Lanjun Wang"
  - "Zhuosheng Zhang"
date: "2026-05-16"
arxiv_id: "2605.16883"
arxiv_url: "https://arxiv.org/abs/2605.16883"
pdf_url: "https://arxiv.org/pdf/2605.16883v1"
github_url: "https://github.com/jinshilong-dev/SE-GA"
categories:
  - "cs.LG"
tags:
  - "GUI Agent"
  - "Memory-Augmented Self-Evolution"
  - "Hierarchical Memory"
  - "Test-Time Memory Extension"
  - "Self-Improvement"
relevance_score: 9.5
---

# SE-GA: Memory-Augmented Self-Evolution for GUI Agents

## 原始摘要

Autonomous Graphical User Interface (GUI) agents often struggle with multi-step tasks due to constrained context windows and static policies that fail to adapt to dynamic environments. To address these limitations, this work proposes the Self-Evolving GUI Agent (SE-GA), a novel framework that integrates hierarchical memory structures with an iterative self-improvement mechanism. At the core of our approach is Test-Time Memory Extension (TTME), which facilitates long-term planning by dynamically retrieving episodic, semantic, and experiential memories to provide salient contexts during inference. To ensure continuous learning, we introduce Memory-Augmented Self-Evolution (MASE), which is a training pipeline that adopts the data collected by TTME to stabilize and enhance the agent's foundational policy. Extensive evaluations across both offline and online benchmarks demonstrate SE-GA achieves state-of-the-art performance, reaching success rates of 89.0\% on ScreenSpot and 75.8\% on the challenging AndroidControl-High dataset. Furthermore, significant improvements on the AndroidWorld benchmark highlight the superior generalization to dynamic environments. Open source code: https://github.com/jinshilong-dev/SE-GA

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决自主图形用户界面（GUI）代理在多步任务中面临的两个核心挑战。研究背景是，尽管视觉语言模型（VLM）推动了GUI代理的发展，但现有方法在实际动态环境中表现不佳。现有方法的不足主要体现在两方面：第一，大多数方法仅依赖当前截图和有限的上下文窗口，无法精准维护完整的交互历史，导致在长程任务中因早期错误或遗忘关键上下文而引发错误累积，造成不可逆的失败。第二，当前代理通常基于固定数据集采用静态策略运行，或仅进行临时检索而缺乏统一的记忆组织，无法从过去的成功经验中提取和复用知识，从而阻碍了其对动态环境的泛化能力。因此，核心问题是缺乏一种统一的机制，将显式的历史经验编码为隐式的策略参数，使代理从静态的命令执行者转变为能通过持续交互不断自我进化的动态学习者。为此，本文提出SE-GA框架，通过集成分层记忆结构与迭代自我改进机制，来增强代理在长程任务中的可靠性和适应性。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类。**方法类**：包括基于VLM的GUI智能体（如早期利用独立模块进行静态屏幕解析的方法）和引入记忆机制的智能体（如ShowUI的分层记忆结构）。与这些工作不同，SE-GA提出了分层记忆（TTME）动态检索情景、语义和经验记忆，以解决长任务中关键信息遮挡和时间上下文缺失问题，而现有方法通常仅关注文本语义检索，缺乏对GUI空间和结构复杂性的处理。**训练范式类**：涉及SFT（行为克隆）、强化学习（如GRPO用于对齐人类意图）和自我进化技术。SE-GA的MASE通过记忆增强的训练管道，利用TTME收集的数据稳定并强化基础策略，克服了传统强化学习在多步任务中因稀疏奖励导致训练不稳定的缺陷。**评测类**：包括离线（ScreenSpot、AndroidControl-High）和在线（AndroidWorld）基准。SE-GA通过在这些动态环境中的卓越表现（如AndroidControl-High上75.8%成功率），证明了其相比仅依赖静态策略或短时观察的现有方法的显著优势。

### Q3: 论文如何解决这个问题？

SE-GA通过分层记忆架构和迭代自我进化机制解决GUI代理的上下文窗口限制和静态策略问题。核心方法包括两个组件：测试时记忆扩展（TTME）和记忆增强自我进化（MASE）。

TTME维护一个三层记忆仓库：情节记忆（M_EPI）通过滑动窗口存储近期动作轨迹，支持短期决策；语义记忆（M_SEM）用嵌入相似度检索通用交互规则（如登录流程），提供跨任务知识；经验记忆（M_EXP）采用混合检索机制结合语义和视觉特征，存储完整任务轨迹及其反思摘要。这三种记忆动态检索并提供给代理作为推理上下文。

MASE训练流水线包含两个阶段：首先通过监督微调（SFT）进行基础训练，最小化负对数似然以增强代理将指令转化为动作的能力；然后采用改进的GRPO进行自我进化训练，引入三项关键技术：1）令牌级重要性比率（来自DAPO）实现细粒度信用分配；2）自适应裁剪机制，使用余弦退火动态调整裁剪边界，避免过度约束高置信度正确令牌；3）层次化奖励设计，将格式正确性奖励和任务准确性奖励（进一步细分为动作类型和参数匹配奖励）加权组合，对点定位使用包含检测验，对滚动使用带阈值的IoU评估。

这种设计使SE-GA无需预定义任务或人工标注，仅通过与环境交互收集数据即可实现持续自我改进，在ScreenSpot和AndroidControl-High等基准上达到SOTA性能。

### Q4: 论文做了哪些实验？

论文在多个离线与在线基准上评估了SE-GA的性能。实验设置采用Qwen2.5-VL-7B作为基础模型，在4块NVIDIA A800 GPU上训练，数据集包含4000条轨迹，经过筛选和重标定后分为2000条用于基础训练、2000条用于自进化训练。评估基准包括：ScreenSpot（图文元素定位）、AndroidControl（低/高层任务）、GUIOdyssey（跨应用导航）和AndroidWorld（动态环境）。对比方法涵盖GPT-4o、Claude、Gemini等闭源模型，以及UI-TARS、OS-Atlas、Aguvis等开源或专用智能体。

主要结果：在ScreenSpot上，SE-GA以89.0%的平均准确率优于所有7B模型甚至部分大模型（如UI-TARS-72B的88.4%）；在AndroidControl-High上，成功率达75.8%，超过所有同尺寸模型；GUIOdyssey上步成功率为83.9%，动作类型准确率达96.5%，均为7B模型最佳；AndroidWorld上成功率为39.0%，显著领先对比方法。消融实验显示，去除TTME导致AndroidControl-High成功率从73.8%降至61.4%，去除MASE则从73.8%降至59.7%，验证了两个核心模块的有效性。

### Q5: 有什么可以进一步探索的点？

**局限性与未来方向：**

当前框架面临记忆检索效率瓶颈，随着交互数据累积，层次化记忆库（尤其经验记忆）规模持续增长，基于嵌入相似度与视觉特征的检索操作可能在推理时引入显著计算开销，影响实时性。未来可从三方面深化：

1. **数据规模与多样性**：目前仅基于4000条轨迹训练，需扩展至更大规模、涵盖更多任务类型的数据集，以验证鲁棒性并提升泛化能力。可考虑引入对抗性样本或跨领域合成数据。

2. **层次化任务分解**：虽TTME辅助长程规划，但显式引入子目标分解策略（如基于任务抽象的动作规划）可进一步优化超长序列的执行逻辑，降低错误传播风险。

3. **跨平台迁移学习**：现有方法未系统验证移动端、网页、桌面等不同GUI平台的适配性。未来可探索策略与记忆结构的轻量级迁移范式，如基于对比学习的平台无关表征对齐，或设计共享的跨平台元记忆模块。此外，可融入主动学习机制，让模型在低置信度场景下自主请求人工反馈，提升数据效率。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为 SE-GA 的自进化 GUI 智能体框架，旨在解决现有智能体在长程任务中因上下文窗口有限和静态策略导致的适应性不足问题。其核心贡献包括两个模块：一是测试时记忆扩展（TTME），通过分层检索情景、语义和经验记忆来提供长程规划所需的动态上下文；二是记忆增强自进化（MASE）训练流程，利用 TTME 收集的高质量交互数据对基础策略进行稳定增强。实验结果表明，SE-GA 在 ScreenSpot 和 AndroidControl-High 等基准上取得了最高成功率，并在动态环境中展现出优异的泛化能力，证明了记忆增强与自我进化机制在构建可靠 GUI 自动化系统方面的潜力。
