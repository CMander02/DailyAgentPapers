---
title: "UniDoc-RL: Coarse-to-Fine Visual RAG with Hierarchical Actions and Dense Rewards"
authors:
  - "Jun Wang"
  - "Shuo Tan"
  - "Zelong Sun"
  - "Tiancheng Gu"
  - "Yongle Zhao"
  - "Ziyong Feng"
  - "Kaicheng Yang"
  - "Zhiwu Lu"
date: "2026-04-16"
arxiv_id: "2604.14967"
arxiv_url: "https://arxiv.org/abs/2604.14967"
pdf_url: "https://arxiv.org/pdf/2604.14967v2"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Visual RAG"
  - "Reinforcement Learning"
  - "Hierarchical Decision-Making"
  - "Active Perception"
  - "Document Understanding"
  - "Multi-Modal Agent"
relevance_score: 8.0
---

# UniDoc-RL: Coarse-to-Fine Visual RAG with Hierarchical Actions and Dense Rewards

## 原始摘要

Retrieval-Augmented Generation (RAG) extends Large Vision-Language Models (LVLMs) with external visual knowledge. However, existing visual RAG systems typically rely on generic retrieval signals that overlook the fine-grained visual semantics essential for complex reasoning. To address this limitation, we propose UniDoc-RL, a unified reinforcement learning framework in which an LVLM agent jointly performs retrieval, reranking, active visual perception, and reasoning. UniDoc-RL formulates visual information acquisition as a sequential decision-making problem with a hierarchical action space. Specifically, it progressively refines visual evidence from coarse-grained document retrieval to fine-grained image selection and active region cropping, allowing the model to suppress irrelevant content and attend to information-dense regions. For effective end-to-end training, we introduce a dense multi-reward scheme that provides task-aware supervision for each action. Based on Group Relative Policy Optimization (GRPO), UniDoc-RL aligns agent behavior with multiple objectives without relying on a separate value network. To support this training paradigm, we curate a comprehensive dataset of high-quality reasoning trajectories with fine-grained action annotations. Experiments on three benchmarks demonstrate that UniDoc-RL consistently surpasses state-of-the-art baselines, yielding up to 17.7% gains over prior RL-based methods.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视觉检索增强生成（Visual RAG）系统中存在的关键挑战。研究背景是，随着大型视觉语言模型（LVLMs）的发展，RAG范式被扩展到视觉领域，使模型能够利用外部视觉知识（如图表、扫描报告）进行推理。然而，视觉文档信息密集且常包含大量冗余背景噪声，使得视觉RAG比纯文本RAG更为困难。

现有方法存在三方面主要不足。首先，在检索环节，现有系统通常依赖解耦的架构和通用相似度评分（如现成检索器），这些评分虽能进行粗粒度过滤，但往往无法捕捉复杂推理所需的细粒度、任务特定语义，且无法适应查询语义或对话上下文，在多轮交互中尤为受限。其次，在视觉利用上，先前方法多采用被动视觉消费范式，直接将完整图像编码到模型上下文中，忽视了视觉理解的层次性，保留了大量无关背景内容，浪费了上下文容量。最后，在优化方面，现有的基于强化学习（RL）的方法主要使用仅基于最终结果的稀疏奖励，这种监督方式无法对检索、裁剪等中间决策提供明确的信用分配，导致优化过程近似黑箱，难以有效改进模型内部决策过程。

因此，本文要解决的核心问题是：如何构建一个统一的、端到端的视觉RAG框架，以协同优化从粗粒度检索到细粒度推理的整个决策链条。具体而言，论文提出了UniDoc-RL框架，通过引入层次化的动作空间（从文档检索到图像选择再到主动区域裁剪）来模拟从粗到精的视觉信息获取过程，并设计密集的多奖励机制为每个决策阶段提供任务感知的监督，从而同时应对精确检索、有效视觉利用和合理优化奖励这三个关键挑战，最终提升复杂视觉推理任务的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：视觉检索增强生成（Visual RAG）和用于多模态推理的强化学习（RL）。

在**视觉检索增强生成**方面，早期方法如ColPali和VisRAG主要依赖基于嵌入的检索来对齐文本查询与视觉文档。近期研究则转向智能体框架，利用外部工具进行更精确的信息提取。其中，VRAG-RL率先将强化学习引入视觉感知动作。本文提出的UniDoc-RL与这些工作一脉相承，但关键区别在于设计了一个从粗到细的“检索-选择-感知”分层动作空间，旨在弥合通用检索与细粒度推理之间的语义鸿沟，使模型能渐进式过滤噪声并聚焦关键视觉证据。

在**强化学习用于多模态推理**方面，RL已被成功应用于提升大语言模型和多模态大模型的推理能力。然而，现有RL框架通常依赖基于最终结果的稀疏奖励，难以有效指导检索、裁剪等中间步骤。本文的核心创新在于设计了一套针对检索相关性、选择准确性和裁剪精度的**密集多奖励方案**，为流程中的每个阶段提供明确监督，从而协同优化整个系统。这解决了传统RL在视觉RAG任务中的信用分配难题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为UniDoc-RL的统一强化学习框架来解决现有视觉RAG系统忽视细粒度视觉语义的问题。其核心方法是将视觉信息获取建模为一个具有分层动作空间的序列决策过程，并采用密集多奖励方案进行端到端训练。

整体框架基于“思考-行动-观察”范式。模型作为智能体，根据查询和历史交互生成思考与行动，执行行动后从外部环境获得观察，迭代进行直至收集到足够信息生成最终答案。框架包含三个层次化的主要动作模块：1) **图像搜索**：智能体生成文本搜索查询，从大规模图像库中粗粒度检索一组候选图像；2) **精确选择**：智能体基于语义评估候选图像的相关性，筛选出最相关的图像以去除噪声；3) **视觉感知**：智能体在选定的图像上定位并裁剪出信息密集的关键区域，实现细粒度的视觉关注。

关键技术包括：**分层动作空间设计**，实现了从粗到细的视觉证据渐进式提炼；**密集多奖励机制**，为每个动作阶段提供细粒度监督。具体包含五个奖励：基于NDCG的图像搜索奖励、基于准确选择的精确选择奖励、基于IoU的视觉感知奖励、确保输出格式正确的模式奖励，以及评估最终答案质量的模型结果奖励。这些奖励通过加权求和形成总奖励，指导策略优化。训练采用**分组相对策略优化**方法，无需单独的价值网络，即可使智能体行为与多目标对齐。

创新点主要体现在：1) 将检索、重排、主动视觉感知和推理统一在一个强化学习框架内进行联合优化；2) 设计了模拟人类信息处理习惯的“搜索-选择-感知”分层决策流程；3) 提出了针对每个决策阶段的密集奖励函数，解决了传统RL方法依赖稀疏奖励信号的问题；4) 在交互过程中，将环境返回的视觉观察以“用户”身份插入对话历史，这更符合大视觉语言模型的预训练数据分布，有利于模型有效处理新视觉信息。

### Q4: 论文做了哪些实验？

论文的实验设置包括：首先，通过整合多个公开基准（SlideVQA、Double Bench、VisR-Bench、DocBench、DUDE）并经过严格过滤，构建了包含12,621个SFT样本和5,537个RL样本的训练数据集。使用Qwen3-VL-235B作为教师代理合成高质量推理轨迹，并通过布局分析和Mineru工具生成候选边界框以支持视觉感知动作。模型训练分为两步：先在llama-factory上进行全参数SFT以初始化基础能力，再使用Group Relative Policy Optimization（GRPO）结合多奖励系统进行强化学习微调，实验在8张NVIDIA A100 80G GPU上完成。

评估在三个视觉丰富的基准测试上进行：ViDoSeek、SlideVQA和MMLongBench，使用评估模型对生成答案进行二值评分，以整体准确率作为指标。对比方法包括：（1）Vanilla RAG（直接检索后推理）、（2）ReAct（迭代查询重写与推理）、（3）Search-R1(-VL)（适配的搜索基线）、（4）VRAG-RL（基于RL的视觉感知基线）。

主要结果：在Qwen2.5-VL-3B模型上，UniDoc-RL在SlideVQA单跳任务达到82.2%、多跳63.1%，ViDoSeek提取任务78.6%、逻辑任务75.9%，MMLongBench整体71.0%，显著优于基线。例如，在3B模型上比VRAG-RL提升17.5%，在7B模型上提升17.7%。关键数据指标显示，UniDoc-RL在视觉密集型任务（如MMLongBench的图表、布局子任务）和复杂推理任务上均表现最优，验证了其分层动作设计与密集奖励机制的有效性。

### Q5: 有什么可以进一步探索的点？

本文提出的UniDoc-RL框架在视觉RAG的层次化决策和密集奖励设计上取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其分层动作空间（文档检索→图像选择→区域裁剪）虽然结构清晰，但可能过于刚性，未来可探索更灵活、可学习的动作抽象层级，或引入软性注意力机制来动态调整粒度。其次，密集多奖励机制依赖于精心设计的人工奖励函数，这可能导致奖励偏差和泛化能力受限；未来可研究基于逆强化学习或从人类反馈中自动学习奖励函数的方法。此外，模型在训练时依赖高质量标注轨迹数据集，成本较高；探索更高效的离线强化学习或自监督预训练方法来减少数据依赖是一个重要方向。最后，当前工作主要关注静态图像，未来可扩展至视频或多模态时序数据的复杂推理任务，并进一步研究模型在开放世界场景中的零样本泛化能力。

### Q6: 总结一下论文的主要内容

本文提出了UniDoc-RL，一个用于视觉检索增强生成（RAG）的强化学习框架。其核心问题是现有视觉RAG系统依赖通用检索信号，忽略了复杂推理所需的细粒度视觉语义。为解决此问题，论文将视觉信息获取建模为一个具有分层动作空间的序列决策问题。方法上，UniDoc-RL让一个大视觉语言模型（LVLM）智能体联合执行检索、重排序、主动视觉感知和推理，通过从粗粒度文档检索到细粒度图像选择及主动区域裁剪的渐进式过程来提炼视觉证据。为有效训练，论文引入了密集多奖励方案，为每个动作提供任务感知监督，并基于组相对策略优化（GRPO）对齐多目标，无需单独的价值网络。主要结论是，在三个基准测试上的实验表明，UniDoc-RL一致超越现有最佳基线，相比之前基于RL的方法取得了最高17.7%的性能提升。其意义在于通过分层动作和密集奖励实现了更精细、高效的视觉知识获取与推理。
