---
title: "VideoTemp-o3: Harmonizing Temporal Grounding and Video Understanding in Agentic Thinking-with-Videos"
authors:
  - "Wenqi Liu"
  - "Yunxiao Wang"
  - "Shijie Ma"
  - "Meng Liu"
  - "Qile Su"
date: "2026-02-08"
arxiv_id: "2602.07801"
arxiv_url: "https://arxiv.org/abs/2602.07801"
pdf_url: "https://arxiv.org/pdf/2602.07801v2"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Perception & Multimodal"
  - "Tool Use & API Interaction"
relevance_score: 8.0
taxonomy:
  capability:
    - "Perception & Multimodal"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "VideoTemp-o3 (unified agentic thinking-with-videos framework with unified masking mechanism and dedicated RL rewards)"
  primary_benchmark: "N/A"
---

# VideoTemp-o3: Harmonizing Temporal Grounding and Video Understanding in Agentic Thinking-with-Videos

## 原始摘要

In long-video understanding, conventional uniform frame sampling often fails to capture key visual evidence, leading to degraded performance and increased hallucinations. To address this, recent agentic thinking-with-videos paradigms have emerged, adopting a localize-clip-answer pipeline in which the model actively identifies relevant video segments, performs dense sampling within those clips, and then produces answers. However, existing methods remain inefficient, suffer from weak localization, and adhere to rigid workflows. To solve these issues, we propose VideoTemp-o3, a unified agentic thinking-with-videos framework that jointly models video grounding and question answering. VideoTemp-o3 exhibits strong localization capability, supports on-demand clipping, and can refine inaccurate localizations. Specifically, in the supervised fine-tuning stage, we design a unified masking mechanism that encourages exploration while preventing noise. For reinforcement learning, we introduce dedicated rewards to mitigate reward hacking. Besides, from the data perspective, we develop an effective pipeline to construct high-quality long video grounded QA data, along with a corresponding benchmark for systematic evaluation across various video durations. Experimental results demonstrate that our method achieves remarkable performance on both long video understanding and grounding.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长视频理解任务中，传统方法因均匀采样导致关键视觉证据缺失、性能下降以及产生幻觉的问题。研究背景是，尽管多模态大语言模型（MLLMs）取得了进展，但其内部知识在训练后是静态的，难以处理动态环境中的复杂任务。为此，近期出现了“agentic thinking-with-videos”范式，采用“定位-裁剪-回答”的流程，即模型主动识别相关视频片段，进行密集采样后生成答案。然而，现有方法存在不足：一是流程复杂，依赖多个专门模型分别进行时间定位和视频问答，导致推理开销大；二是定位不精确，缺乏评估或优化定位结果的机制；三是流程僵化，通常盲目裁剪一次视频后立即回答，无法根据视频长度灵活调整，也缺乏对长视频场景中迭代优化定位的支持。

本文的核心问题是：如何设计一个统一、高效的框架，以协同建模视频时间定位和问答，从而提升长视频理解的准确性和可靠性。为此，论文提出了VideoTemp-o3框架，它整合了定位与问答功能，支持按需裁剪和迭代优化定位，并通过改进的训练策略（如统一的掩码机制和定制化强化学习奖励）以及高质量的数据构建流程，来增强模型的定位能力和视频理解性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**智能体化多模态大模型**和**长视频理解**。

在**智能体化多模态大模型**方面，相关研究旨在提升模型利用外部工具解决现实问题的能力。例如，OpenAI-o3 提出了“thinking-with-images”范式，通过调用裁剪、缩放等工具来增强对图像的细粒度感知。受此启发，Thyme 和 DeepEyesV2 利用代码生成作为通用接口进行灵活的图像操作。近期，“thinking-with-videos”范式被提出，将这种细粒度感知从空间维度扩展到了时间维度。本文的 VideoTemp-o3 正是这一范式下的工作，但与之不同的是，它提出了一个统一的框架来联合建模视频定位与问答，而非依赖多智能体协作或僵化的多阶段流程。

在**长视频理解**方面，传统方法如 VideoChat-R1 采用基于强化学习的策略，但常受限于为控制计算成本而采用的均匀帧采样，容易遗漏关键信息。为此，一些工作如 LongVA 通过长上下文微调来扩展处理长度，另一些则采用视觉令牌压缩。近期，作为补充方案，智能体化“thinking-with-videos”范式兴起，其核心是“定位-剪辑-回答”的流程。例如，VideoExplorer 依赖多智能体分工协作，VITAL 采用 SFT-RL 两阶段训练，REVISOR 采用先定位后回答的两阶段推理，LongVT 则设计了 SFT-RL-RFT 三阶段训练策略。本文与这些工作目标一致，但指出它们存在效率低下、定位能力弱、流程僵化等问题。VideoTemp-o3 通过统一的联合建模框架、创新的训练机制（如统一的掩码机制和针对性的奖励设计）以及高质量的数据构建流程，旨在更高效、灵活且强健地解决长视频理解与定位任务。

### Q3: 论文如何解决这个问题？

论文通过提出VideoTemp-o3这一统一的智能体视频思考框架来解决长视频理解中关键视觉证据捕捉不足、现有方法效率低下、定位能力弱且流程僵化的问题。其核心方法是将时序定位（Temporal Grounding）和视频问答（VideoQA）联合建模，形成一个灵活的“定位-裁剪-回答”迭代过程。

整体框架上，模型首先以低采样率快速浏览视频，然后进行多轮交互。在每一轮中，模型生成文本推理，并输出一个时序区间或最终答案。如果输出区间，外部裁剪模块会以更高采样率提取对应片段，并将其加入上下文供下一轮使用。交互在输出答案或达到最大轮数时终止。该框架支持三个关键特性：1) **按需裁剪**：对于短视频可直接回答，避免不必要的裁剪；2) **反思机制**：允许模型对初始不准确的定位进行多轮细化修正；3) **任务统一**：使用相同对话格式同时支持视频问答和时序定位任务，增强了模型内在的定位能力。

在训练策略上，论文采用了监督微调（SFT）和强化学习（RL）两阶段方法。SFT阶段的关键创新是**统一掩码策略**：在收集的多工具调用数据中，只有最后两轮（包含正确时序区间和最终答案）的响应被用于计算损失，而之前轮次的生成和用户输入均被掩码，避免了不精确的中间定位标签引入噪声。RL阶段采用GRPO算法，并设计了专门的奖励系统以联合优化答案正确性、格式遵循和时序定位质量。该奖励系统包含：**准确性奖励**（鼓励答案正确）、**格式奖励**（确保遵循多轮对话格式）以及**带惩罚的IoU奖励**（用于评估时序定位质量，当IoU低于阈值时施加惩罚，有效缓解了奖励黑客行为，促使模型产生可靠的定位而非随意猜测）。

此外，论文还从数据角度构建了高质量的长视频时序定位问答数据及相应基准，用于系统评估。实验结果表明，该方法在长视频理解和定位任务上均取得了显著性能提升。

### Q4: 论文做了哪些实验？

论文实验设置以Qwen2.5-VL-7B为骨干模型，基于ms-swift和vLLM构建训练流程，并支持多轮工具调用交互。实验在多个公开基准上评估了三个核心任务：长视频理解（MLVU、VideoMMMU、VideoMME、LVBench）、时序定位（Charades-STA、ActivityNet-MR）以及视频时序问答（NextGQA、ReXTime）。此外，论文还引入了自建的VideoTemp-Bench，用于系统分析不同视频时长下的性能。

主要对比方法包括VTimeLLM-7B、Momentor-7B、ChatVTG-7B、TimeMaker-8B、ZoomV-7B、VideoChat-R1-7B等。实验结果显示，VideoTemp-o3在长视频理解任务上取得了最先进的性能，例如在VideoMME和LVBench上分别提升了2.4%和1.7%。在时序定位任务中，强化学习后的模型在Charades-STA上达到R@0.7为33.0%，mIoU为57.8%；在ActivityNet-MR上R@0.7为26.7%，mIoU为45.3%，性能接近专家定位模型。在视频时序问答任务上，模型在NextGQA和ReXTime上均取得领先，例如ReXTime的mIoU达到29.5%，准确率达到74.4%。

消融实验验证了关键设计：移除定位数据或统一掩码机制会导致性能显著下降（如ReXTime的mIoU分别下降16.5%和10.7%）；使用原始IoU奖励会引发奖励黑客行为，导致定位质量下降；而移除惩罚感知奖励或IoU奖励均会造成性能退化。在VideoTemp-Bench上的分析表明，模型能根据视频长度进行按需工具调用，且视频越长，定位越具挑战性（如>20分钟视频的mIoU仅为4.0%）。不同任务类型性能差异显著，计数与识别任务间存在约40%的差距。

### Q5: 有什么可以进一步探索的点？

本文提出的VideoTemp-o3框架在长视频理解与时间定位的统一方面取得了进展，但仍存在一些局限性和值得深入探索的方向。首先，模型虽然支持按需裁剪和反思机制，但其定位能力仍依赖于训练数据的质量与广度，在极端复杂或模糊的时间边界场景中可能表现不稳定。未来研究可探索更细粒度的时空感知模块，例如结合光流或场景分割技术，以提升对快速动作转换或细微视觉线索的捕捉能力。

其次，当前框架主要针对预裁剪的视频片段进行处理，未充分利用视频的全局时序结构信息。未来可引入层次化或图结构的视频表示，使模型能同时建模局部片段与整体叙事逻辑的关系，从而减少因忽略长程依赖而产生的幻觉。此外，强化学习中的奖励设计虽缓解了奖励黑客问题，但可能未完全覆盖多模态对齐的复杂性，可考虑引入基于视觉-文本语义一致性的自适应奖励机制。

从应用拓展角度看，论文提到可整合外部工具（如搜索引擎），这提示了构建多智能体协作系统的潜力。例如，可设计专精于特定子任务（如人物识别、事件检测）的辅助智能体，与主框架协同工作，以处理开放域或实时更新的视频内容。最后，当前基准测试虽涵盖不同时长视频，但缺乏对超长视频（如数小时）或跨视频推理任务的评估，未来需构建更挑战性的数据集以推动领域发展。

### Q6: 总结一下论文的主要内容

该论文针对长视频理解中传统均匀采样方法难以捕捉关键视觉证据、导致性能下降和幻觉增多的问题，提出了一种名为VideoTemp-o3的新型智能体化“视频思维”框架。其核心贡献在于将视频时间定位与问答任务统一建模，摒弃了以往“定位-剪辑-回答”的僵化流程，实现了更高效、灵活且精准的长视频理解。

方法上，VideoTemp-o3支持按需剪辑并能迭代优化不准确的定位。在监督微调阶段，作者设计了统一的掩码机制，以鼓励模型探索同时防止噪声干扰；在强化学习阶段，则引入了专门的奖励设计来缓解奖励黑客问题。此外，论文还从数据角度提出了一套构建高质量长视频定位问答数据的流程，并建立了相应的基准测试集，用于系统评估不同视频时长的任务。

主要结论显示，VideoTemp-o3在长视频理解和时间定位任务上均取得了卓越性能，显著提升了定位能力与问答准确性，为智能体与长视频交互提供了更强大的统一解决方案。
