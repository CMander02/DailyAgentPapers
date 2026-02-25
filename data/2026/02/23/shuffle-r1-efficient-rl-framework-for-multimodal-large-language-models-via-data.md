---
title: "Shuffle-R1: Efficient RL framework for Multimodal Large Language Models via Data-centric Dynamic Shuffle"
authors:
  - "Linghao Zhu"
  - "Yiran Guan"
  - "Dingkang Liang"
  - "Jianzhong Ju"
  - "Zhenbo Luo"
  - "Bin Qin"
  - "Jian Luan"
  - "Yuliang Liu"
  - "Xiang Bai"
date: "2025-08-07"
arxiv_id: "2508.05612"
arxiv_url: "https://arxiv.org/abs/2508.05612"
pdf_url: "https://arxiv.org/pdf/2508.05612v5"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "强化学习"
  - "多模态大语言模型"
  - "后训练"
  - "推理能力"
  - "数据效率"
  - "训练优化"
  - "Agentic 强化学习"
relevance_score: 7.5
---

# Shuffle-R1: Efficient RL framework for Multimodal Large Language Models via Data-centric Dynamic Shuffle

## 原始摘要

Reinforcement learning (RL) has emerged as an effective post-training paradigm for enhancing the reasoning capabilities of multimodal large language model (MLLM). However, current RL pipelines often suffer from training inefficiencies caused by two underexplored issues: Advantage Collapsing, where most advantages in a batch concentrate near zero, and Rollout Silencing, where the proportion of rollouts contributing non-zero gradients diminishes over time. These issues lead to suboptimal gradient updates and hinder long-term learning efficiency. To address these issues, we propose Shuffle-R1, a simple yet principled framework that improves RL fine-tuning efficiency by dynamically restructuring trajectory sampling and batch composition. It introduces (1) Pairwise Trajectory Sampling, which selects high-contrast trajectories with large advantages to improve gradient signal quality, and (2) Advantage-based Trajectory Shuffle, which increases exposure of valuable rollouts through informed batch reshuffling. Experiments across multiple reasoning benchmarks show that our framework consistently outperforms strong RL baselines with minimal overhead. These results highlight the importance of data-centric adaptations for more efficient RL training in MLLM.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态大语言模型（MLLM）在强化学习（RL）后训练中存在的训练效率低下问题。研究背景是，RL已成为增强MLLM（如数学解题、代码生成等复杂推理任务）能力的一种有效后训练范式。然而，现有方法大多采用静态采样范式，即均匀地采样和处理所有轨迹，忽略了不同学习信号的信息价值存在差异且会动态变化。这种“一视同仁”的策略导致两个未被充分探索的突出问题：一是“优势坍缩”（Advantage Collapsing），即批次中大部分计算出的优势值集中在零附近，淹没了那些具有大幅值优势的轨迹所携带的信息性信号，导致梯度更新微弱甚至无效；二是“ rollout 静默”（Rollout Silencing），即随着训练进行，能贡献非零梯度的 rollout 比例持续下降，造成计算资源的灾难性浪费，未能充分利用信息丰富的样本。这些不足使得训练过程可能被噪声轨迹主导，而真正有用的信号未被充分使用，从而阻碍了长期学习效率。因此，本文要解决的核心问题是：能否通过动态地优先处理信息量更大的轨迹，来提供更丰富的梯度信息，从而实现更高效的RL训练？为此，论文提出了Shuffle-R1框架，其核心思想是进行以数据为中心的动态调整，通过动态重组轨迹采样和批次构成，来缓解上述两个问题，从而提升RL微调的效率。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提升大语言模型（尤其是多模态大语言模型）的推理能力展开，可分为以下几类：

**1. 推理能力增强方法**：早期研究通过在有复杂思维链的数据上进行监督微调（SFT）来提升推理表现，但这种方法可能仅让模型学会格式化输出而非真正学会推理。后续工作尝试控制模型生成结构化思维链，或使用蒙特卡洛树搜索（MCTS）等测试时扩展方法。近期，OpenAI o1/o3、DeepSeek-R1 等模型则利用强化学习（RL）来激发模型的自主探索与推理能力，其中 DeepSeek-R1-Zero 直接在预训练模型上使用可验证的结果奖励进行RL训练，取得了显著效果。

**2. RL在多模态与下游任务的应用**：随着DeepSeek-R1的成功，一系列研究将RL范式迁移到多模态大语言模型的训练中，并应用于开放词汇目标检测、推理分割、视频理解与定位等下游视觉任务。这些工作主要关注RL在不同任务上的适用性。

**3. RL训练过程的优化**：另一类研究深入RL机制本身，从多个角度优化训练过程，例如引入对比奖励机制、在rollout中主动加入反思令牌、优化RL目标函数与梯度更新机制，以及增加rollout的多样性等。其核心目标是提升RL训练的效率与效果。

**本文与这些工作的关系与区别**：本文同样聚焦于优化MLLM的RL训练效率，属于上述第三类研究。与关注奖励设计或目标函数优化的方法不同，本文从一个数据中心的视角，深入分析了训练中存在的“优势坍缩”和“Rollout静默”两个未被充分探索的效率瓶颈问题，并提出了通过动态重组轨迹采样与批次构成的Shuffle-R1框架。这区别于主要关注任务适用性或数据组织平衡的工作，为高效RL训练提供了一个新颖且轻量级的解决方案。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Shuffle-R1的数据中心化动态重组框架来解决强化学习（RL）微调多模态大语言模型（MLLM）时遇到的“优势坍缩”和“轨迹静默”两大效率瓶颈问题。其核心方法包含两个关键模块：成对轨迹采样（Pairwise Trajectory Sampling, PTS）和基于优势的批次重组（Advantage-based Batch Shuffle, ABS），整体架构旨在动态优化轨迹采样与批次构成，以提升梯度信号质量和数据利用效率。

整体框架工作流程如下：首先，对于每个查询，从旧策略中采样2N条响应轨迹，计算奖励和标准化优势值。随后，PTS模块介入，它并非孤立地评估轨迹，而是采用“最大-最小”配对原则，将优势值最高的轨迹与最低的配对，次高与次低配对，以此类推，从而构建出包含鲜明对比（正-负样本）的N个轨迹对。接着，PTS根据优势差异的绝对值大小，仅选取排名前k（由超参数α控制）的、最具信息量的轨迹对子集用于后续更新，这直接过滤了优势值接近零、梯度信号微弱的轨迹，有效缓解了优势坍缩问题。

然而，PTS筛选出的有价值轨迹在标准训练中可能仅被使用一次，随着训练进行，能提供有效更新的轨迹比例可能下降（即轨迹静默）。为此，ABS模块在PTS输出的批次基础上进行动态重组。它为每个轨迹对分配一个重要性权重，该权重等于其包含的两条轨迹的绝对优势值之和。基于此权重分布进行带权重的子采样，从原始批次中多次（有放回地）抽取固定大小的子批次，然后拼接成与原始批次大小相同的重组批次。这一过程使得高优势值的轨迹对被采样的概率更高，从而在单个训练周期内获得了更频繁的梯度更新曝光，打破了静态数据流的限制，显著缓解了轨迹静默问题。

该方法的创新点在于：1）**结构化对比采样（PTS）**：通过显式构建高对比度的轨迹对，从更广的探索空间中智能选择梯度信号强的样本，将RL微调的重点从均匀探索转向基于梯度信息的筛选。2）**动态优先级重组（ABS）**：引入基于优势权重的重采样机制，实现了训练批次内数据分布的软优先级重排，让高价值样本得到强化学习，提高了数据利用率。两者结合，以最小的计算开销实现了更高效、更稳定的RL训练。

### Q4: 论文做了哪些实验？

实验设置方面，论文以EasyR1为代码库，使用Qwen2.5-VL-3B/7B-Instruct作为基础模型，冻结视觉编码器参数。更新批次大小为128，rollout批次大小为512，学习率为1e-6，在8张80G GPU上进行。对于每个查询生成16个rollout，在提出的PTS方法中构建8个轨迹对并保留前4对（保留率α=0.5）；在ABS方法中，每个子采样批次包含256对轨迹，并进行8轮洗牌。评估解码温度为0.5，报告8次测试的平均pass@1准确率以减少随机性。

使用的数据集和基准测试包括：在有限资源下使用Geometry3K（2.1k训练样本）和MMK12子集（等量数据）进行实验；为评估扩展性，使用结合Geo3K全量和MM-Eureka中27k样本构成的30k训练集。评估涵盖领域内测试集（Geo3K、MMK12）和多个领域外视觉推理基准：MathVerse、MathVision、WeMath、MathVista、HallusionBench和ChartQA，覆盖数学推理、视觉感知和图表理解。使用MathRuler评估自由形式答案，使用Gemini-2.0-Flash-001评估多项选择题。

对比方法包括强化学习基线GRPO、DAPO和最新的GSPO，以及一系列开源RL训练模型（如R1-VL-7B、Vision-R1-7B、VLAA-Thinker-7B等）和闭源模型（GPT-4o、Claude-3.7-Sonnet等）。

主要结果和关键指标如下：在Geometry3K上，Shuffle-R1的3B模型达到47.88%准确率，超越GRPO 5.2%、DAPO 2.7%；7B模型达到55.89%，分别领先3.3%和1.4%。在K12数据集上，3B模型达到62.22%，超越GRPO 3.03%、DAPO 0.8%。在领域外数学推理任务（Math Avg.）上，3B模型达到48.70%，较GRPO提升1.96%；7B模型达到54.63%，提升1.5%。在HallusionBench和ChartQA上也观察到一致提升。在大规模MM-Eureka实验上，Shuffle-R1-7B在多个基准上超越开源RL竞争对手，例如在MathVerse达到53.9%、MathVista达到77.0%、ChartQA达到84.1%，平均准确率64.7%，优于其他7B RL模型。效率分析显示，Shuffle-R1仅增加4%~7.7%的GPU时间，在达到相同准确率时可减少约一半训练步骤和40%总时间。消融实验证实PTS和ABS均贡献显著性能提升。

### Q5: 有什么可以进一步探索的点？

该论文提出的Shuffle-R1框架虽有效缓解了优势值坍缩和轨迹沉默问题，但其局限性与未来探索方向仍值得深入。首先，方法主要依赖优势函数进行轨迹筛选与重组，而优势估计本身可能受价值函数误差影响，未来可研究更稳健的优势估计方法或引入不确定性量化来提升筛选可靠性。其次，当前框架在单轮训练中动态调整批次，但未考虑跨训练周期的课程学习机制，未来可探索如何根据模型学习阶段自适应调整采样策略，进一步提升长期训练稳定性。此外，实验集中于推理任务，对于需要复杂多轮交互的对话或具身任务，其动态重组机制是否依然高效尚待验证。从更广视角看，该工作凸显了数据中心化优化在RL微调中的潜力，未来可结合模型架构改进（如引入分层策略）或混合监督学习与RL的课程，以形成更通用的高效微调范式。最后，框架的计算开销虽低，但在超大规模模型或持续学习场景中，动态重组的频率与规模仍需更精细的设计权衡。

### Q6: 总结一下论文的主要内容

该论文针对多模态大语言模型强化学习后训练中存在的训练效率低下问题，提出了一个数据中心的动态重组框架Shuffle-R1。核心问题是优势值塌缩和轨迹沉默，前者导致批次内优势值集中在零附近，后者使得随时间推移能提供有效梯度的轨迹比例下降，从而造成梯度更新次优和长期学习效率低下。

方法上，Shuffle-R1通过动态重组轨迹采样和批次构成来提升效率。它包含两个关键设计：一是成对轨迹采样，选择优势值对比鲜明的高价值轨迹对，以提升梯度信号质量；二是基于优势值的轨迹重组，通过有信息的批次重排，增加有价值轨迹的曝光度。

实验表明，该框架在多个推理基准上能以极低开销持续超越现有强RL基线。其主要贡献在于揭示了RL训练中数据动态组织的重要性，为MLLM的高效微调提供了一种简单而有效的解决方案，推动了数据中心的RL优化思路。
