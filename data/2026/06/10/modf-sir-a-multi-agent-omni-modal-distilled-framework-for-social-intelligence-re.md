---
title: "MODF-SIR: A Multi-agent Omni-modal Distilled Framework for Social Intelligence Reasoning"
authors:
  - "Shang Ma"
  - "Jisheng Dang"
  - "Wencan Zhang"
  - "Yifan Zhang"
  - "Bimei Wang"
  - "Hong Peng"
  - "Bin Hu"
  - "Qi Tian"
  - "Tat-Seng Chua"
date: "2026-06-10"
arxiv_id: "2606.12018"
arxiv_url: "https://arxiv.org/abs/2606.12018"
pdf_url: "https://arxiv.org/pdf/2606.12018v1"
github_url: "https://github.com/eeee-sys/MODF-SIR"
categories:
  - "cs.AI"
tags:
  - "多智能体协作"
  - "社会智能推理"
  - "知识蒸馏"
  - "多模态大模型"
  - "长尾事件提取"
  - "推理增强"
  - "LoRA微调"
relevance_score: 8.0
---

# MODF-SIR: A Multi-agent Omni-modal Distilled Framework for Social Intelligence Reasoning

## 原始摘要

We propose a multi-agent collaborative framework built upon a lightweight Multimodal Large Language Model (MLLM), specifically designed for social intelligence reasoning. A key feature of our approach is that both the training and inference phases are augmented via knowledge distillation. Within this architecture, multi-modal data pertinent to social intelligence is precisely localized. Furthermore, relevant long-tail events are identified, extracted, and rendered as formatted, explicit text. This formatting strategy prevents critical long-tail information from being overshadowed by head events and environmental noise during the tokenization process. Specifically, we integrate Test-Time Adaptation (TTA) across the entire reasoning pipeline, encompassing the extraction and representation of long-tail events, Chain-of-Thought (CoT) prompting, and self-reflection. This TTA mechanism is also distillation-enhanced, utilizing Low-Rank Adaptation (LoRA) to fine-tune the foundation model exclusively for instance-level reasoning. Extensive evaluations against various open-source and proprietary AI models across multiple benchmarks demonstrate the effectiveness of the proposed framework. With around 30% of training data from IntentTrain, we achieve state-of-the-art results. Codes are available at https://github.com/eeee-sys/MODF-SIR, demo is available at https://huggingface.co/spaces/Harry-1234/MODF-SIR, LoRA is available at https://huggingface.co/Harry-1234/MODF-SIR and the dataset for training router is available at https://huggingface.co/datasets/Harry-1234/IntentRouterTrain.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决社交智能推理中多模态信息理解与长尾事件处理的难题。研究背景指出，人类交流常依赖隐含意图、情感及社会规范，而非显式指令，这对AI系统提出了超越表面感知、理解深层心理动态的要求。现有方法的不足主要体现在：传统方法采用黑箱推理范式，易产生幻觉，且在处理多模态数据（如语言、面部表情、动作）时，长尾关键事件容易被主导性的头部事件或环境噪声淹没，导致推理不准确；同时，现有模型难以动态适应不同复杂度的输入，计算资源分配效率低，且缺乏样本级的适应能力。本文提出的MODF-SIR框架，核心问题正是要构建一个轻量级、基于多智能体协作的跨模态蒸馏框架，以显式化推理步骤，突出长尾事件，并通过引入测试时自适应（TTA）和知识蒸馏技术，实现高效且准确的社交智能推理，从而在动态交互中建模人类意图和心理状态。

### Q2: 有哪些相关研究？

本文的相关研究可以分为三类：时序定位与推理方法、模型细化与自我反思方法、以及参数高效微调技术。

在时序定位与推理方面，现有工作如视频字幕、视频问答和视频文本检索主要关注语义层面的理解（如视频理解、时序定位），但缺乏细粒度的时间对齐和可解释推理。本文提出的MODF-SIR通过多代理协作和长尾事件显式文本化，增强了复杂视频中的时序定位与推理能力。

在模型细化方面，早期工作如自一致性、工具增强推理和结构化搜索通过推理时迭代改进输出，还有工作利用强化学习（RL）优化多步推理（如自我反思、推理时细化）。然而，这些方法大多依赖视觉任务，忽略了全模态信息。本文通过集成测试时适应，并在整个推理管道中融入知识蒸馏，实现了连续细化。

在参数高效微调方面，LoRA等技术提供了低计算开销的模型更新方式（如LoRA、参数高效微调），但主要用于离线适应。本文创新的将LoRA集成到迭代推理框架中，用于实例级推理微调，填补了在线细化与参数高效微调结合的空缺。

### Q3: 论文如何解决这个问题？

该论文提出了MODF-SIR框架，一个面向社会智能推理的多智能体全模态知识蒸馏框架，核心是通过多智能体协作与知识蒸馏增强轻量级多模态大模型的训练与推理。整体框架包含五个主要智能体模块：**内源长尾检索器**作为系统1模块，快速扫描下采样后的视频和音频输入，将细微的长尾事件（如微表情、情绪变化）显式转化为文本描述，避免关键信息在分词过程中被主要事件和噪声淹没；**非对称知识蒸馏路由智能体**利用一个30B参数教师模型产生的伪标签训练一个7B轻量学生模型，根据检索器输出的文本判断查询是显式还是隐式、事件是头部还是长尾，从而动态路由到不同推理路径；**GRPO接地智能体**在需要复杂意图分析的路径B中被激活，采用GRPO策略对视频段进行时空定位，通过组相对奖励优化候选片段，缩小下游推理的搜索空间；**全模态长尾意图理解推理器**作为系统2模块，对定位后的长尾事件进行链式思维推理，逐步解析用户查询；**测试时适应修正智能体**评估推理器输出，若答案不理想则通过情节式LoRA对基础模型进行实例级微调以修正逻辑不一致或幻觉，并在生成满意答案后立即丢弃LoRA修改以防止灾难性遗忘。关键技术包括非对称知识蒸馏实现认知压缩、GRPO强化接地训练、以及测试时适应与LoRA结合的动态修正机制，使框架在不依赖昂贵人工标注的情况下实现高效社会智能推理。

### Q4: 论文做了哪些实验？

论文在三个基准测试上进行了实验：Daily-Omni、IntentBench 和 WorldSense。  
**实验设置**：使用7B参数量的轻量级多模态大模型作为基座，通过知识蒸馏增强训练和推理，并集成了测试时自适应（TTA）和LoRA微调。  
**数据集/基准测试**：  
- **Daily-Omni**：评估多维度能力，包括音视频事件对齐、对比理解、上下文理解、事件序列、推理等。  
- **IntentBench**：评估社交意图推理，分为Why、How、When、Who/Which等子任务。  
- **WorldSense**：评估世界知识，涵盖科技、文化、日常生活、影视等多个领域。  
**对比方法**：与GPT-4o、Gemini 2.0 Flash等闭源模型，以及Unified-IO-2、VideoLLaMA2、Qwen2.5-Omni、Ola、MiniCPM-o、HumanOmniV2等开源模型对比。  
**主要结果**：  
- **Daily-Omni**：MODF-SIR平均分64.9%，超越所有开源模型（如HumanOmniV2的58.5%），接近Gemini 2.0 Flash的67.8%。  
- **IntentBench**：平均分70.3%，优于HumanOmniV2（69.3%）和Qwen2.5-Omni（64.2%）。  
- **WorldSense**：平均分51.5%，超过HumanOmniV2（47.1%）和Qwen2.5-Omni（45.4%）。  
仅使用约30%的IntentTrain数据即达到SOTA，验证了框架的高效性。

### Q5: 有什么可以进一步探索的点？

论文中MODF-SIR框架虽在社交智能推理上取得了SOTA，但仍存在若干可探索的局限与方向。首先，框架依赖知识蒸馏和LoRA微调，可能受限于教师模型的质量与领域覆盖，未来可探索自蒸馏或多教师蒸馏策略，以增强对罕见社交场景的泛化能力。其次，长尾事件的提取与格式化文本表示依赖预定义解析规则，在动态社交交互中可能遗漏细粒度语义，可引入自适应事件检测机制（如基于图注意力的场景编码）来提升事件表示的鲁棒性。此外，当前TTA仅针对实例级推理，未考虑跨场景的持续学习，建议设计元学习或增量蒸馏框架，使模型能在多轮交互中自适应调整策略。最后，框架在轻量级MLLM上运行，但多智能体协作的通信开销仍存在瓶颈，可尝试稀疏化注意力或通信剪枝来平衡效率与推理深度。这些改进有望推动社交智能系统在真实动态场景中的实用化。

### Q6: 总结一下论文的主要内容

本文提出MODF-SIR，一个针对社会智能推理的轻量级多智能体全模态蒸馏框架。问题定义：现有模型在处理隐含意图、长尾事件等社会智能信号时，易受头部事件和噪声干扰，产生幻觉。方法概述：框架采用双阶段检索机制，粗粒度检索（ELT Retriever Agent）指导路由决策，细粒度检索（OMLT Reasoner Agent）支撑推理。通过GRPO Grounder精确定位相关数据片段，减少搜索开销。推理过程由OMLT Reasoner和TTA Reviser协作，结合知识蒸馏的测试时自适应，使用LoRA动态优化模型参数。关键创新包括动态路由策略、显式提取长尾事件并文本化，及迭代自修正机制。主要结论：仅用约30%的IntentTrain训练数据，在IntentBench、Daily-Omni、WorldSense基准上超越GPT-4o等模型，证明了多智能体协作与蒸馏增强在社会智能推理中的有效性。
