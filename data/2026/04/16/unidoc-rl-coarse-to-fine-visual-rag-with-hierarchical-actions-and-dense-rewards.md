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
  - "Cewu Lu"
date: "2026-04-16"
arxiv_id: "2604.14967"
arxiv_url: "https://arxiv.org/abs/2604.14967"
pdf_url: "https://arxiv.org/pdf/2604.14967v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "视觉RAG"
  - "强化学习"
  - "分层决策"
  - "主动感知"
  - "文档理解"
  - "多目标奖励"
relevance_score: 8.0
---

# UniDoc-RL: Coarse-to-Fine Visual RAG with Hierarchical Actions and Dense Rewards

## 原始摘要

Retrieval-Augmented Generation (RAG) extends Large Vision-Language Models (LVLMs) with external visual knowledge. However, existing visual RAG systems typically rely on generic retrieval signals that overlook the fine-grained visual semantics essential for complex reasoning. To address this limitation, we propose UniDoc-RL, a unified reinforcement learning framework in which an LVLM agent jointly performs retrieval, reranking, active visual perception, and reasoning. UniDoc-RL formulates visual information acquisition as a sequential decision-making problem with a hierarchical action space. Specifically, it progressively refines visual evidence from coarse-grained document retrieval to fine-grained image selection and active region cropping, allowing the model to suppress irrelevant content and attend to information-dense regions. For effective end-to-end training, we introduce a dense multi-reward scheme that provides task-aware supervision for each action. Based on Group Relative Policy Optimization (GRPO), UniDoc-RL aligns agent behavior with multiple objectives without relying on a separate value network. To support this training paradigm, we curate a comprehensive dataset of high-quality reasoning trajectories with fine-grained action annotations. Experiments on three benchmarks demonstrate that UniDoc-RL consistently surpasses state-of-the-art baselines, yielding up to 17.7% gains over prior RL-based methods.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视觉检索增强生成（Visual RAG）系统中存在的关键挑战。研究背景是，随着大视觉语言模型（LVLMs）的发展，通过引入外部视觉知识（如图表、扫描报告）来增强模型推理能力变得日益重要。然而，视觉文档通常信息密集且包含大量冗余背景噪声，使得视觉RAG比纯文本RAG更为困难。

现有方法存在三方面主要不足：首先，在检索阶段，现有系统通常依赖解耦的架构和通用相似度评分进行粗粒度检索，这些评分无法捕捉复杂推理所需的细粒度任务语义，且难以适应查询语义或多轮对话上下文。其次，在视觉信息利用上，现有方法多采用被动范式，直接将完整图像编码到上下文，忽视了视觉理解的分层特性，保留了大量无关内容，浪费了上下文容量。最后，在优化方面，现有的基于强化学习的方法主要使用仅基于最终结果的稀疏奖励，无法为检索、裁剪等中间决策提供明确的信用分配，导致优化过程近似黑箱，难以有效改进模型的内部决策过程。

本文要解决的核心问题是：如何构建一个统一的端到端框架，以协同优化视觉RAG中的检索、重排序、主动视觉感知和推理等多个关键环节。为此，论文提出了UniDoc-RL框架，通过将视觉信息获取建模为一个具有分层动作空间的序列决策问题，实现从粗粒度文档检索到细粒度图像选择及主动区域裁剪的渐进式证据细化。同时，设计密集多奖励机制为每个动作提供任务感知的监督，并基于高质量标注轨迹数据集进行训练，从而系统性地提升视觉RAG在复杂推理任务上的准确性和效率。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为两大类：视觉检索增强生成（Visual RAG）和用于多模态推理的强化学习（RL）。

在**视觉检索增强生成**方面，早期方法如ColPali和VisRAG主要依赖基于嵌入的检索来对齐文本查询与视觉文档。近期研究则转向智能体框架，利用外部工具进行更精确的信息提取，其中VRAG-RL率先将强化学习引入视觉感知动作。本文提出的UniDoc-RL与这些工作一脉相承，但关键区别在于设计了一个从“检索”到“选择”再到“感知”的层次化、由粗到细的动作空间。这弥合了通用检索与细粒度推理之间的语义鸿沟，使模型能渐进式地过滤噪声并聚焦关键视觉证据。

在**强化学习用于多模态推理**方面，RL已被成功应用于提升大语言模型和多模态模型的推理能力。然而，现有RL框架通常依赖基于最终结果的稀疏奖励，难以有效指导检索、裁剪等中间步骤（信用分配问题）。本文的核心贡献在于设计了一种密集的多奖励方案，为检索相关性、选择准确性和裁剪精度等每个动作阶段提供明确的任务感知监督，从而实现整个管道的协同优化，避免了依赖独立价值网络的需求。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为UniDoc-RL的统一强化学习框架来解决现有视觉RAG系统依赖通用检索信号、忽视细粒度视觉语义的问题。其核心方法是将视觉信息获取建模为一个具有分层动作空间的序列决策问题，并采用密集多奖励方案进行端到端训练。

整体框架基于“思想-动作-观察”（T, A, O）范式。模型作为一个由策略π_θ参数化的智能体，在给定查询和交互历史后，生成思想（T_t）和动作（A_t），执行动作后从环境获得观察（O_t），如此迭代直至收集到足够信息生成最终答案。

主要模块与分层动作空间设计是其架构核心，包含三个由粗到细的渐进式动作：
1.  **图像搜索**：作为粗粒度检索步骤。智能体生成包含在<search>标签内的搜索查询q，调用外部检索函数Search(q, C)从大规模图像语料库C中获取一组候选图像作为观察O_t。
2.  **精确选择**：为解决外部检索工具可能无法捕捉复杂推理所需细粒度语义的问题，引入基于LVLM的选择机制。智能体评估候选图像的相关性，生成包含在<select>标签内的相关图像索引I，通过函数Select(O_t, I)过滤候选集，保留语义相关的图像，减少下游推理噪声。
3.  **视觉感知**：为使模型能主动定位并关注关键局部区域，智能体生成指定目标区域R的动作（由<bbox>标签界定）。通过感知函数VP(O_{t+1}, R)执行区域选择、裁剪和自适应缩放，提取出高分辨率、聚焦于查询的视觉观察，有效去除冗余内容。

关键技术在于其**密集多奖励机制**，为流程的每个阶段提供细粒度、任务感知的监督，而非仅依赖稀疏的结果奖励。具体包括：
*   **图像搜索奖励**：使用归一化折损累计增益（NDCG）评估检索质量。
*   **精确选择奖励**：基于所选图像是否属于真实相关图像集进行二元奖励。为处理候选集中无真实相关图像的情况，引入了伪监督策略，将初始检索中排名最高的候选作为伪正例目标，以提供区分性反馈。
*   **视觉感知奖励**：基于预测裁剪区域与真实边界框的交并比（IoU）来鼓励准确定位。
*   **模式奖励**：基于规则检查生成的轨迹是否符合预定义格式（如正确使用XML标签），确保动作有效可执行。
*   **结果奖励**：使用奖励模型评估最终生成答案的质量，使整个决策过程与最终推理目标对齐。
总奖励是上述各项的加权和。训练采用分组相对策略优化（GRPO）算法，无需依赖单独的价值网络即可使智能体行为与多个目标对齐。

创新点主要体现在：1）将视觉RAG构建为分层序列决策问题，实现了从文档检索到区域裁剪的渐进式视觉证据细化；2）设计了密集的多奖励方案，为每个关键动作提供针对性的监督信号；3）通过将环境观察以“用户”角色插入对话历史，适配了LVLM的预训练数据分布，使其能有效处理新视觉信息。此外，论文还构建了包含细粒度动作标注的高质量推理轨迹数据集以支持此训练范式。

### Q4: 论文做了哪些实验？

论文的实验设置包括：首先，通过聚合多个公开基准（SlideVQA、Double Bench、VisR-Bench、DocBench、DUDE）构建训练数据集，并经过多阶段过滤，最终得到12,621个SFT样本和5,537个RL样本。使用Qwen3-VL-235B作为教师代理合成推理轨迹，并通过布局分析工具Mineru生成候选边界框以构建视觉感知动作。训练分两步：先在llama-factory上进行全参数SFT作为冷启动，再使用Group Relative Policy Optimization（GRPO）结合多奖励系统进行强化学习微调，实验在8块NVIDIA A100 80G GPU上完成。

评估在三个视觉丰富的基准测试上进行：ViDoSeek、SlideVQA和MMLongBench，使用评估模型对生成答案进行二值评分，以整体准确率作为指标。对比方法包括：（1）Vanilla RAG（直接检索后推理）、（2）ReAct（迭代查询重写、检索和推理）、（3）Search-R1(-VL)（适配自Search-R1基线）、（4）VRAG-RL（同样基于RL的视觉感知方法）。

主要结果：在Qwen2.5-VL-3B模型上，UniDoc-RL在SlideVQA单跳任务达到82.2%，多跳63.1%；ViDoSeek提取任务78.6%，逻辑任务75.9%；MMLongBench整体71.0%，显著优于基线。在7B模型上，UniDoc-RL整体准确率达74.8%，比最强的RL基线VRAG-RL（57.1%）提升17.7%。关键数据指标显示，UniDoc-RL在各项任务中均取得最优性能，尤其在多跳推理和细粒度视觉任务上表现稳健，验证了其分层动作设计和密集奖励机制的有效性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性与未来研究方向可从多个维度展开。首先，UniDoc-RL 依赖于精心标注的轨迹数据集进行训练，这限制了其泛化到更广泛、开放域场景的能力。未来可探索弱监督或自监督方法，减少对人工标注的依赖。其次，其层次化动作空间虽提升了检索精度，但决策步骤增加可能导致推理延迟，在实时应用中面临挑战。未来可研究更高效的动作剪枝或并行化策略。此外，奖励函数的设计仍依赖人工先验，未来可结合逆强化学习或基于 LLM 的奖励模型，使奖励更贴合复杂任务需求。从技术融合角度看，可将动态外部知识库更新机制融入框架，使模型能持续适应新数据。最后，当前评估集中于静态基准，未来需在交互式、多轮对话场景中测试其鲁棒性，并探索跨模态（如结合音频）的扩展应用。

### Q6: 总结一下论文的主要内容

本文提出UniDoc-RL，一个用于视觉检索增强生成（RAG）的统一强化学习框架，旨在解决现有方法在复杂视觉推理中的局限性。核心问题是现有视觉RAG系统依赖通用检索信号，忽略了细粒度视觉语义，且检索、视觉利用和优化奖励三者常被孤立处理，导致整体效能受限。

方法上，UniDoc-RL将视觉信息获取建模为具有分层动作空间的序列决策问题。代理（LVLM）联合执行从粗到细的层次化操作：先进行粗粒度文档检索，再通过精确选择动作对候选进行语义重排序，最后通过主动视觉感知动作（如裁剪和缩放）聚焦信息密集区域，从而抑制无关内容。为有效训练，框架引入了密集多奖励方案，为每个动作提供任务感知的监督，并基于组相对策略优化（GRPO）进行端到端优化，无需单独的价值网络。此外，研究还构建了一个包含细粒度动作标注的高质量推理轨迹数据集以支持训练。

实验表明，UniDoc-RL在三个基准测试上 consistently 超越现有最先进方法，相比之前的基于RL的方法取得了高达17.7%的性能提升。其核心贡献在于统一建模了视觉RAG的关键决策阶段，并通过分层动作与密集奖励实现了更精准、高效的视觉知识获取与推理。
