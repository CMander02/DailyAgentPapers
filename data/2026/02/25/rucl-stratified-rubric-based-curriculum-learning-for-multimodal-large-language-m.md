---
title: "RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning"
authors:
  - "Yukun Chen"
  - "Jiaming Li"
  - "Longze Chen"
  - "Ze Gong"
  - "Jingpeng Li"
  - "Zhen Qin"
  - "Hengyu Chang"
  - "Ancheng Xu"
  - "Zhihao Yang"
  - "Hamid Alinejad-Rokny"
  - "Qiang Qu"
  - "Bo Zheng"
  - "Min Yang"
date: "2026-02-25"
arxiv_id: "2602.21628"
arxiv_url: "https://arxiv.org/abs/2602.21628"
pdf_url: "https://arxiv.org/pdf/2602.21628v1"
categories:
  - "cs.CL"
tags:
  - "强化学习"
  - "多模态大语言模型"
  - "Agent推理"
  - "课程学习"
  - "奖励设计"
  - "视觉推理"
  - "基准评测"
relevance_score: 7.5
---

# RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning

## 原始摘要

Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a prevailing paradigm for enhancing reasoning in Multimodal Large Language Models (MLLMs). However, relying solely on outcome supervision risks reward hacking, where models learn spurious reasoning patterns to satisfy final answer checks. While recent rubric-based approaches offer fine-grained supervision signals, they suffer from high computational costs of instance-level generation and inefficient training dynamics caused by treating all rubrics as equally learnable. In this paper, we propose Stratified Rubric-based Curriculum Learning (RuCL), a novel framework that reformulates curriculum learning by shifting the focus from data selection to reward design. RuCL generates generalized rubrics for broad applicability and stratifies them based on the model's competence. By dynamically adjusting rubric weights during training, RuCL guides the model from mastering foundational perception to tackling advanced logical reasoning. Extensive experiments on various visual reasoning benchmarks show that RuCL yields a remarkable +7.83% average improvement over the Qwen2.5-VL-7B model, achieving a state-of-the-art accuracy of 60.06%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态大语言模型在强化学习微调过程中，因奖励设计不当而导致的“奖励黑客”和训练效率低下的核心问题。研究背景是，当前主流的“基于可验证奖励的强化学习”范式虽然避免了训练昂贵奖励模型的成本，但其仅依赖最终答案正确性的粗粒度奖励信号，容易使模型学习到虚假的推理模式（例如生成矛盾的中间步骤却巧合地得到正确答案），损害了推理过程的可靠性。

现有方法的不足主要体现在两个方面：第一，近期提出的基于评估准则的方法虽然能提供细粒度的监督信号，但为每个训练实例生成独特的准则计算成本高昂；第二，更关键的是，现有方法在整个训练过程中平等地对待所有评估准则，忽略了不同准则在可学习性上存在显著差异。这导致模型在尚未掌握基础感知技能时，就因复杂的逻辑错误而受到惩罚，产生了噪声梯度信号，阻碍了高效收敛。

因此，本文要解决的核心问题是如何设计一种高效且结构化的奖励机制，以引导模型循序渐进地掌握从基础感知到高级逻辑的完整推理能力。为此，论文提出了基于分层准则的课程学习框架，其创新点在于将课程学习的焦点从传统的数据选择转移到奖励设计本身，通过构建通用准则、依据模型能力对其进行分层，并在训练中动态调整各层准则的权重，从而系统性地提升模型的推理性能与训练效率。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：多模态大语言模型的后训练方法、基于量规的奖励方法以及课程学习。

在多模态大语言模型（MLLM）的后训练方面，早期方法如LLaVA-Reasoner、MPO和Insight-V依赖于原理蒸馏、人类偏好或迭代DPO，但存在监督成本高、可扩展性低的问题。随后，基于可验证奖励的强化学习（RLVR）范式成为主流，它通过验证最终答案来提升推理能力，相关研究包括Vision-R1、DeepScaler、Light-R1以及VL-Rethinker、SRPO、GThinker等。然而，这些方法依赖稀疏的结果监督，容易导致模型通过虚假推理模式进行“奖励黑客”行为。本文提出的RuCL框架同样属于RLVR范式，但旨在通过更精细的奖励设计来解决上述问题。

在基于量规的奖励方法方面，近期研究通过结构化量规来评估中间推理过程，为强化学习提供更丰富的奖励信号，并在医疗推理、代码生成等领域得到应用。LLM-as-a-Judge框架是典型代表。然而，现有方法通常为每个实例生成特定的量规，并将所有量规视为同等可学习的，缺乏对推理技能异质难度的考量。本文的RuCL则生成了具有广泛适用性的通用量规，并依据难度对其进行分层，从而与这些工作区别开来。

在课程学习方面，传统方法如Kwai Keye-VL和VL-Contigo主要在数据层面组织“由易到难”的训练课程，例如通过多阶段训练或在线难度加权。本文的RuCL创新性地将课程学习应用于奖励设计层面，通过动态调整不同难度量规的权重来引导模型学习，实现了从数据选择到奖励设计的焦点转移，这是与先前课程学习方法的核心区别。

### Q3: 论文如何解决这个问题？

论文通过提出分层式基于量规的课程学习框架来解决多模态大语言模型推理中存在的奖励黑客和训练效率低下问题。其核心方法是将课程学习的重点从数据选择转向奖励设计，通过构建通用量规、按难度分层，并动态调整奖励权重来引导模型学习。

整体框架包含两个主要阶段：量规构建与分层阶段，以及混合奖励与课程调度阶段。在量规构建阶段，首先通过教师大语言模型生成一个通用的量规候选集，而非为每个训练实例生成特定量规，这大幅降低了计算开销（从O(N)降至O(1)）。随后，通过一个专门的评估机制在采样数据上进行“适用性感知评估”，为每个量规计算适用率和通过率。基于通过率这一统计上可解释的难度代理指标（通过率低意味着梯度估计噪声大），将量规分为基础层和高级层。基础层量规（如视觉存在性、实体提取）通过率高，提供稳定、低噪声的监督信号；高级层量规（如步骤连贯性、证据扎根）通过率低，针对复杂的逻辑推理。

在训练阶段，采用混合奖励机制，结合了基于规则的最终答案验证和分层量规的过程评估。课程调度的核心创新在于“性能触发的课程调度”。它定义了一个课程系数λ_t来动态混合基础奖励和高级奖励。训练开始时，λ_t=0，模型仅通过基础层量规进行优化，专注于巩固感知等基础技能。只有当模型在基础奖励上的表现达到并保持稳定（通过滑动窗口内的奖励均值判断）后，才进入过渡阶段，逐步增加λ_t以引入高级层量规的监督。最终，λ_t达到预设最大值，模型全面学习所有推理技能。这种方法确保了优化过程从易到难、从稳定到挑战，避免了不同难度监督信号相互干扰导致的噪声梯度和低效训练。

该方法的创新点在于：1) 将课程学习应用于奖励函数设计本身，而非传统的数据编排；2) 提出数据驱动的、基于统计指标的量规通用化构建与分层方法，兼顾了监督信号的细粒度和计算效率；3) 设计了基于模型当前能力的稳定性感知课程调度机制，使训练动态更高效。实验表明，该方法在多个视觉推理基准上取得了显著的性能提升。

### Q4: 论文做了哪些实验？

论文在实验设置上，以Qwen2.5-VL-7B-Instruct作为基础模型，使用ViRL-39K数据集进行训练。评估涵盖多模态数学推理（MathVista、MathVerse、MATH-Vision、WeMATH）和通用视觉推理（LogicVista、Super-CLEVR Counting、MMMU）两大类基准。对比方法包括三类基线模型：专有模型（如GPT-4o、Claude-3.5-Sonnet）、开源通用模型（如Qwen2.5-VL系列、InternVL2.5系列）以及开源推理专用模型（如MM-Eureka-7B、ThinkLite-VL-7B等）。技术配置方面，使用Gemini 3 Pro生成评分准则候选，Qwen3-VL-235B-A22B-Instruct作为奖励评判模型，并设置了滑动窗口大小K=20、熟练度阈值τ_th=0.9、奖励平衡系数α=0.7等关键参数。

主要结果显示，RuCL方法在多个基准上取得了显著提升。相比基础模型Qwen2.5-VL-7B，平均性能提高了7.83%，在全部七个任务上达到了60.06%的最新先进平均准确率。具体关键指标包括：在WeMATH上提升12.97%（从58.52%到71.49%），在MathVerse上提升5.16%（从48.98%到54.14%），在LogicVista上提升10.40%（从39.26%到49.66%），在Counting任务上达到85.50%的准确率。消融实验证实了分层课程学习策略的有效性，其中Sigmoid分层调度策略优于线性调度和均匀平均策略。敏感性分析表明，奖励平衡系数α=0.7时性能最优，滑动窗口大小w=20为最佳设置。

### Q5: 有什么可以进一步探索的点？

该论文提出的RuCL框架虽在奖励设计和分层课程学习上取得进展，但仍存在若干局限和可拓展方向。首先，其分层标准（基础感知与高级逻辑）依赖人工预设，可能无法全面覆盖复杂推理任务的连续能力谱，未来可探索基于模型训练动态的自动化分层机制，例如利用强化学习中的优势函数或不确定性估计来实时调整分层边界。其次，论文仅验证了7B参数规模模型，对于更大规模MLLM（如百亿参数以上），奖励信号的稀疏性和训练稳定性问题可能加剧，需研究如何将分层奖励与模型缩放律结合，设计参数高效的课程学习策略。此外，当前方法侧重于视觉推理任务，未来可延伸至多模态决策、具身推理等需时序交互的场景，其中分层奖励需融合环境反馈与内部认知状态。最后，在线构建动态评估准则（online rubric construction）虽被提及，但具体实现尚未展开，可结合大模型自我反思能力，让模型在训练中自主生成并迭代优化评估准则，形成更自适应、可解释的课程学习循环。

### Q6: 总结一下论文的主要内容

该论文针对多模态大语言模型推理训练中存在的奖励黑客问题，提出了一种基于分层评分的课程学习框架RuCL。核心问题是传统基于结果的强化学习容易导致模型学习虚假推理模式，而现有基于评分的方法则存在计算成本高且训练效率低下的缺陷。RuCL的方法创新在于将课程学习的重点从数据选择转向奖励设计：它首先生成具有广泛适用性的通用评分规则，然后根据模型当前能力将这些规则分层，并在训练中动态调整各层评分的权重，从而引导模型从掌握基础感知能力逐步过渡到解决高级逻辑推理。主要结论是，RuCL在多个视觉推理基准测试上显著提升了性能，在Qwen2.5-VL-7B模型上实现了平均7.83%的改进，达到了60.06%的先进准确率。其核心贡献在于通过分层的、动态的奖励设计机制，更高效地利用细粒度监督信号，推动了多模态大模型推理能力的稳健提升。
