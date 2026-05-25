---
title: "Metacognition as Reward: Reinforcing LLM Reasoning via Knowledge and Regulation Signals"
authors:
  - "Sirui Chen"
  - "Lei Xu"
  - "Yuying Zhao"
  - "Yutian Chen"
  - "Yu Wang"
  - "Beier Zhu"
  - "Hanwang Zhang"
  - "Shengjie Zhao"
  - "Chaochao Lu"
date: "2026-05-22"
arxiv_id: "2605.23384"
arxiv_url: "https://arxiv.org/abs/2605.23384"
pdf_url: "https://arxiv.org/pdf/2605.23384v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "LLM reasoning"
  - "reinforcement learning"
  - "reward design"
  - "metacognition"
  - "process reward model"
  - "RLVR"
  - "reasoning trajectory optimization"
relevance_score: 7.8
---

# Metacognition as Reward: Reinforcing LLM Reasoning via Knowledge and Regulation Signals

## 原始摘要

Recent RL methods have substantially improved the reasoning abilities of LLMs. Existing reward designs mainly follow two paradigms: (1) Reinforcement learning with verifiable rewards (RLVR) derives outcome signals from executable checks or ground-truth answers, but provides limited guidance for intermediate reasoning behaviors. (2) Rubrics-as-reward (RaR) goes beyond final-answer checking by using natural-language rubrics to assess reasoning quality and task compliance, but often requires instance-specific rubrics and substantial design effort. To address these issues, we introduce Metacognition-as-Reward (MaR), a metacognition-inspired RL framework that guides LLM reasoning through two general process dimensions: i) metacognitive knowledge, which identifies task-relevant information without hand-crafted instance-specific rubrics, and ii) metacognitive regulation, which plans and adjusts the reasoning process to provide reward guidance beyond final-answer outcomes. MaR scaffolds model rollouts into explicit metacognitive components and optimizes them with a trajectory-level reward over task knowledge coverage, regulation fidelity, and final-answer correctness. In this way, MaR extends reward feedback to reasoning trajectories while grounding the reward signals in general metacognitive dimensions. Experiments on 22 benchmarks show that MaR consistently improves model performance, achieving up to a 7.7% gain over the base model and up to an 11.0% gain over vanilla DAPO. Notably, Qwen3.5-9B + MaR narrows the gap to frontier models, surpassing GPT-OSS-120B on overall average and outperforming stronger models on several individual benchmarks. Process-level analysis further shows substantial improvements in reasoning process quality. MaR also generalizes to out-of-domain datasets, where MaR-trained models improve over their corresponding base models on average.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有强化学习方法在提升大语言模型（LLM）推理能力时，奖励信号设计上的核心局限。研究背景是，近期强化学习虽然显著增强了LLM的推理能力，但现有的奖励设计主要遵循两种范式，且各有不足：一是基于可验证结果的强化学习（RLVR），它依赖于最终答案的检查或可执行验证来提供奖励，但这种“结果导向”的奖励无法有效约束和指导模型在得出答案前的中间推理过程；二是基于标准评估的奖励（RaR），它使用自然语言标准来评估推理质量，但这些标准往往需要针对特定实例进行大量人工设计，缺乏泛化性，且无法明确指出哪些通用推理维度应被鼓励。因此，本文要解决的核心问题是：能否定义一种更普适、能引导中间推理过程的奖励目标，从而克服上述两种范式在奖励信号上的局限性——即RLVR缺乏过程指导，而RaR依赖实例特定设计且通用性不足。论文提出了一种受元认知启发的框架（MaR），通过将元认知知识（识别任务相关信息）和元认知调节（计划与调整推理过程）作为通用的过程维度来设计奖励，希望在不依赖人工定制的前提下，为模型的整个推理轨迹提供更丰富、更结构化的反馈信号。

### Q2: 有哪些相关研究？

在相关研究中，本文主要涉及两个类别：元认知推理和大语言模型推理的奖励设计。

1. **元认知推理类**：现有工作或通过提示（如结构化自我评估、反思性提示）来激发LLM的元认知能力，但未能将其内化为模型能力；或使用多智能体强化学习、分层元认知RL框架来诱导元认知行为（如反思、回溯）。本文的区别在于，它不只关注如何激发或组织这些行为，而是首次提出了“高质量元认知过程”的通用训练目标，并作为奖励信号直接优化推理轨迹。

2. **奖励设计类**：现有范式主要有两种：基于可验证结果的RLVR（RL with Verifiable Rewards）和基于自然语言规则的RaR（Rubrics-as-Reward）。RLVR对中间推理过程指导有限，且不适用于开放生成任务；RaR虽能评估推理质量，但通常需要任务实例特定的规则，设计成本高。本文提出的MaR框架是这两者的结合与升华——它通过两个通用元认知维度（知识识别与过程调节）提供过程奖励，无需实例特定规则，同时兼顾最终答案正确性和推理轨迹质量，从而在22个基准上取得了显著性能提升。

### Q3: 论文如何解决这个问题？

论文提出了一套名为元认知作为奖励（MaR）的强化学习框架，通过将推理过程结构化为可观测、可奖励的组件，来解决现有方法中奖励信号稀疏或依赖人工设计的问题。核心方法是将模型生成过程分解为三个明确阶段：元认知知识（MK）、元认知调节（MR）和可选的回溯步骤（LOOKBACK），最后产出最终答案。在架构上，整个框架形成一个三阶段循环：首先，策略模型根据专有提示生成包含上述组件的结构化展开；然后，一个LLM评分器（grader）对每个展开沿着三个维度打分：知识监控奖励（KMR）衡量模型识别和恢复任务所需知识单位的比例；调节监控奖励（RMR）通过检查模型实际推理过程与其自述计划的一致性、并惩罚绕过计划的捷径行为来评估；正确性奖励（CR）判断最终答案是否与真实答案匹配。最终奖励是这三个分项奖励之和。在技术上，MaR的关键创新点包括：通过索引化原子知识项使知识覆盖可检查；通过计划和回退机制暴露模型的调节过程；采用DAPO算法，基于组内的归一化优势值优化策略，提升高元认知奖励展开的似然。这使得奖励信号能从单纯的最终答案正确性扩展到对整个推理轨迹的细粒度反馈，且不需要实例级的人工规则设计，实现了通用性。

### Q4: 论文做了哪些实验？

论文进行了全面的实验验证。实验设置上，使用VeRL框架基于DAPO算法对Qwen3.5-4B和9B模型进行后训练，训练数据来自RaR-Medicine和RaR-Science（约32K样本），并以GPT-5.1生成金标准知识，使用XXL-Qwen作为评判模型提供奖励，λ设为0.3。

在22个基准测试集上评估，涵盖科学（GPQA-Diamond等6个）、医学（MedGUIDE等4个）、长上下文推理（DocQA-RL-1.6K等3个）、数学推理（AIME 2024/2025/2026等7个）和逻辑推理（FOLIO等2个）五大类，共约16K测试样本。对比方法包括Qwen系列、OSS、DeepSeek、GLM、Kimi等前沿模型以及DAPO基线。

主要结果：MaR在科学和医学基准上持续提升性能，在Qwen3.5-9B上最高提升7.7%，比纯DAPO提升高达11.0%。Qwen3.5-9B+MaR总体平均超越OSS-120B。在长上下文OOD任务上，KMR、RMR、CR组件分别平均提升17.2%、10.7%和9.8%。消融实验表明，更强大的评判模型效果更好（XXL-Qwen达67.6%），且移除任何奖励组件都会导致性能下降。Spearman相关分析显示KMR和RMR与最终正确性正相关且提供非冗余监督。

### Q5: 有什么可以进一步探索的点？

论文提出的MaR框架通过元认知知识（识别任务相关信息）和元认知调节（规划与调整推理过程）两个维度来指导LLM推理，避免了手动构造实例级评分标准。然而，该方法仍存在几个局限：首先，元认知知识信号目前主要依赖“任务信息覆盖率”来评估，可能无法准确区分哪些信息对推理真正关键，未来可探索基于信息论或因果推断的细粒度知识重要性评估机制。其次，轨迹级奖励函数将任务知识覆盖、调节忠诚度和最终答案正确性线性组合，权重设置依赖经验，可考虑自适应权重学习或基于偏好对齐的优化策略。此外，实验仅在数学推理和科学问答上验证，但在多跳推理、长文本推理或需要常识与形式化知识交互的任务上泛化性尚不明确。一个可能的改进方向是将MaR与过程监督的潜在变量模型结合，通过元认知预测器在推理过程中动态调节搜索步数和回溯策略，从而在保持通用性的同时提升奖励信号的即时性和精准度。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个名为Metacognition-as-Reward (MaR) 的强化学习框架，旨在解决现有LLM推理强化学习中奖励信号设计不足的问题。现有方法要么仅依赖最终答案正确性（RLVR），缺乏对中间推理过程的约束；要么需要人工设计的特定任务评分标准（RaR），泛化性差。MaR受人类元认知启发，定义了两种通用奖励维度：元认知知识（识别任务相关信息）和元认知调节（规划与调整推理过程）。该框架将模型生成过程显式分解为元认知知识、元认知调节及最终答案等组件，并通过轨迹级奖励函数优化这些组件，鼓励模型不仅答案正确，还具备良好的过程质量。在22个基准测试上的实验表明，MaR在多个领域（科学、医学、长文本推理等）上持续提升性能，最高可带来11%的提升，且表现出良好的跨任务泛化能力。核心贡献在于将元认知理论引入奖励设计，为提升LLM推理质量提供了一个通用、无需人工特定设计的有效方案。
