---
title: "Emotion-LLaMAv2 and MMEVerse: A New Framework and Benchmark for Multimodal Emotion Understanding"
authors:
  - "Xiaojiang Peng"
  - "Jingyi Chen"
  - "Zebang Cheng"
  - "Bao Peng"
  - "Fengyi Wu"
  - "Yifei Dong"
  - "Shuyuan Tu"
  - "Qiyu Hu"
  - "Huiting Huang"
  - "Yuxiang Lin"
  - "Jun-Yan He"
  - "Kai Wang"
  - "Zheng Lian"
  - "Zhi-Qi Cheng"
date: "2026-01-23"
arxiv_id: "2601.16449"
arxiv_url: "https://arxiv.org/abs/2601.16449"
pdf_url: "https://arxiv.org/pdf/2601.16449v2"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Multimodal LLM"
  - "Emotion Understanding"
  - "Benchmark"
  - "Instruction Tuning"
  - "Human-Robot Interaction"
  - "Affective Computing"
relevance_score: 6.5
---

# Emotion-LLaMAv2 and MMEVerse: A New Framework and Benchmark for Multimodal Emotion Understanding

## 原始摘要

Understanding human emotions from multimodal signals poses a significant challenge in affective computing and human-robot interaction. While multimodal large language models (MLLMs) have excelled in general vision-language tasks, their capabilities in emotional reasoning remain limited. The field currently suffers from a scarcity of large-scale datasets with high-quality, descriptive emotion annotations and lacks standardized benchmarks for evaluation. Our preliminary framework, Emotion-LLaMA, pioneered instruction-tuned multimodal learning for emotion reasoning but was restricted by explicit face detectors, implicit fusion strategies, and low-quality training data with limited scale. To address these limitations, we present Emotion-LLaMAv2 and the MMEVerse benchmark, establishing an end-to-end pipeline together with a standardized evaluation setting for emotion recognition and reasoning. Emotion-LLaMAv2 introduces three key advances. First, an end-to-end multiview encoder eliminates external face detection and captures nuanced emotional cues via richer spatial and temporal multiview tokens. Second, a Conv Attention pre-fusion module is designed to enable simultaneous local and global multimodal feature interactions external to the LLM backbone. Third, a perception-to-cognition curriculum instruction tuning scheme within the LLaMA2 backbone unifies emotion recognition and free-form emotion reasoning. To support large-scale training and reproducible evaluation, MMEVerse aggregates twelve publicly available emotion datasets, including IEMOCAP, MELD, DFEW, and MAFW, into a unified multimodal instruction format. The data are re-annotated via a multi-agent pipeline involving Qwen2 Audio, Qwen2.5 VL, and GPT 4o, producing 130k training clips and 36k testing clips across 18 evaluation benchmarks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态情感理解领域的关键挑战，即如何构建一个能够同时进行情感识别与自由形式情感推理的端到端统一框架，并建立大规模、高质量的标准化基准以推动该领域的发展。

研究背景方面，情感理解在人机交互、医疗、教育等领域至关重要，它要求模型不仅能识别情感类别，还能推理其背后的原因和上下文表达。人类情感源自语音、面部表情、情境等多模态信号，这些信号异步、弱相关且受复杂因素影响，使得鲁棒且可泛化的情感理解一直是个开放难题。现有方法存在明显不足：早期单模态方法（如仅基于面部或语音）无法捕捉情感的跨模态整体性；后续多模态融合框架虽能提升识别性能，但大多局限于特征级关联建模，缺乏对统一语义表示和显式情感推理的支持。近年来，多模态大语言模型（MLLMs）在通用视觉-语言任务上表现出色，但由于其设计假设与情感信号特性不匹配，在情感理解上仍受限。具体而言，现有MLLMs难以直接处理编码副语言信息的原始音频流，对细微视觉线索（如微表情）不够敏感，且缺乏大规模、高质量的情感指令数据与标准化评估基准。作者团队先前提出的Emotion-LLaMA框架虽首次将指令调优引入多模态情感理解，但仍受限于显式人脸检测器、隐式融合策略、训练数据规模小且质量有限等问题，无法充分捕捉时序动态和复杂多模态依赖。

因此，本文的核心问题是：如何克服现有MLLMs在情感理解上的固有局限，并解决领域内缺乏大规模高质量指令数据与统一评估标准的问题。为此，论文提出了Emotion-LLaMAv2模型与MMEVerse基准。Emotion-LLaMAv2通过端到端多视图编码器（避免显式人脸检测）、Conv Attention预融合模块（实现局部与全局多模态特征交互）以及感知到认知的课程指令调优方案，统一了情感识别与推理。MMEVerse则整合了12个公开数据集，通过多智能体流程重新标注，提供了约13万训练和3.6万测试样本的标准化指令格式数据与18个评估基准，旨在为多模态情感理解研究提供可扩展、可复现的训练与评估基础。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：多模态情感理解、多模态大语言模型以及用于跨模态学习的指令微调。

在多模态情感理解领域，早期研究如IEMOCAP等数据集采用判别式建模，在受控环境下整合视觉、听觉和文本线索进行情感识别。后续工作扩展到电影、电视剧等非受控场景。传统方法通常提取单模态特征（如基于CNN的面部特征或HuBERT/Wav2Vec 2.0的声学特征），并通过特征拼接或基于注意力的融合机制进行整合。这些方法擅长分类任务，但难以支持需要解释情感推断的高层语义推理。近期，**涌现情感智能**范式强调超越表面分类的、基于语义的整体情感理解。基于此，Emotion-LLaMA首次引入了用于情感推理的指令微调多模态大语言模型。后续工作如AffectGPT采用Q-Former架构对齐多模态特征，HumanOmni和Omni-Emotion利用大规模视频语料进行训练以捕捉全模态交互，Audio-Reasoner和R1-Omni则分别通过以音频为中心的建模和强化学习策略提升推理性能。然而，现有评测基准在覆盖范围和评估协议上仍显碎片化。

在多模态大语言模型领域，LLaVA和LLaVA-NeXT等研究成功将指令微调范式扩展到视觉-语言任务，使模型能遵循基于视觉内容的自然语言指令。为增强推理能力，DeepSeek-R1和Visual-RFT等采用了偏好优化和强化学习策略。

在指令微调领域，自然语言处理中的开创性工作如InstructGPT、FLAN等证明了从多样化的指令-响应对中学习能显著改善零样本和少样本泛化能力。在情感计算领域，先前工作如EmoVIT和最初的MERR数据集主要依赖基于描述的指令生成，存在规模有限、模态覆盖受限、对推理监督支持弱等问题。R1-Omni将带有验证反馈的强化学习应用于情感推理以增强逻辑一致性。

**本文与这些工作的关系和区别在于**：1) 在方法上，本文提出的Emotion-LLaMAv2通过端到端多视图编码器、Conv Attention预融合模块以及感知到认知的课程指令微调方案，系统性地改进了其前身Emotion-LLaMA以及类似模型（如AffectGPT）在架构和数据上的限制。2) 在评测基准上，本文提出的MMEVerse整合了十二个公开数据集并进行了高质量重标注，解决了现有基准（如EmoBench、EmotionBench）碎片化、不一致的问题，为大规模训练和标准化评估提供了统一框架。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Emotion-LLaMAv2的端到端框架，并结合MMEVerse大规模标准化评测基准，系统性地解决了多模态情感理解中数据稀缺、评测标准不一以及模型能力有限的问题。

**整体框架与核心方法**：Emotion-LLaMAv2构建了一个层次化、模块化的统一架构，将多模态情感理解分解为四个紧密耦合的组件：1）多模态编码器用于感知；2）Conv-Attention预融合模块用于情感感知的跨模态交互；3）模态适配器用于表示对齐；4）基于LoRA微调的大语言模型用于联合情感识别与推理。该设计避免了将原始多模态融合任务过载给语言模型，实现了更稳定、可解释的推理。

**主要模块与创新点**：
1.  **端到端多视图编码器**：摒弃了传统依赖外部人脸检测器的做法。视觉处理上，通过一个全局视觉编码器（处理代表性静态帧）和一个时序视觉编码器（处理帧序列）组成的双编码器设计，从静态外观和动态演化中提取互补的情感表征。音频处理上，采用预训练的HuBERT或Whisper编码器来捕捉语调、节奏等韵律特征。这一设计实现了对细微情感线索的端到端、多尺度捕捉。
2.  **Conv-Attention预融合模块**：这是一个关键创新。该模块被设计在LLM主干网络外部，专门用于实现局部与全局并行的多模态特征交互。它能够建模情感相关的跨模态交互（如音频韵律与面部表情的对应关系），生成融合后的情感感知特征，再与各模态独立特征一同输入后续阶段。这显式地增强了模型对跨模态情感线索的整合能力。
3.  **感知到认知的课程指令微调方案**：在LLaMA2主干网络内，采用了两阶段指令微调策略。首先进行情感感知任务（如分类）的微调，使模型学会基础的情感概念；随后进行自由形式情感推理任务的微调。这种课程学习方式统一了情感识别与推理，引导模型从低级感知逐步过渡到高级认知。

**支持性工作——MMEVerse基准**：为了支撑大规模训练与可复现评估，论文构建了MMEVerse基准。它汇集了12个公开情感数据集（如IEMOCAP、MELD），并通过一个涉及Qwen2 Audio、Qwen2.5 VL和GPT-4o的多智能体流水线进行重新标注，将其统一转化为多模态指令格式，最终产生了13万训练片段和3.6万测试片段，覆盖18个评测基准，从根本上解决了高质量标注数据稀缺和评估标准不一的问题。

综上，论文通过**端到端多视图编码**、**外部Conv-Attention预融合**、**课程指令微调**三大关键技术革新，以及**大规模标准化基准MMEVerse**的构建，形成了一个从数据、模型到评估的完整解决方案，显著提升了多模态大语言模型在情感理解与推理方面的能力。

### Q4: 论文做了哪些实验？

论文的实验主要围绕提出的新框架Emotion-LLaMAv2和基准测试MMEVerse展开。实验设置包括使用MMEVerse数据集进行训练和评估，该数据集整合了12个公开可用的多模态情感数据集（如IEMOCAP、MELD、DFEW、MAFW等），并通过多智能体流程（涉及Qwen2 Audio、Qwen2.5 VL和GPT-4o）重新标注，最终包含约13万训练片段和3.6万测试片段，覆盖18个评估基准。对比方法包括现有的多模态大语言模型（MLLMs）及情感识别模型，但论文未明确列出具体对比模型名称。主要结果方面，Emotion-LLaMAv2在多个基准测试中表现出色，关键数据指标包括在基本情感、情感极性、多标签情感等任务上的准确率或F1分数提升，例如在MER2023、MELD-e等数据集上取得了优于基线模型的结果。此外，模型通过端到端多视图编码器、Conv Attention预融合模块和感知到认知课程指令调优方案，显著提升了情感推理的准确性和鲁棒性。

### Q5: 有什么可以进一步探索的点？

该论文提出的框架和基准在统一多模态情感理解方面迈出了重要一步，但仍存在一些局限性和值得深入探索的方向。首先，模型架构上，虽然引入了端到端多视图编码器和预融合模块，但其多模态交互机制仍相对传统，未来可探索更高效的跨模态注意力机制或引入扩散模型等新兴架构来更细腻地捕捉模态间的非线性情感关联。其次，在数据层面，MMEVerse整合了现有数据集，但情感标注仍依赖于大模型自动生成，可能存在噪声和偏差；未来需构建更具动态性和上下文感知的大规模人工标注数据集，并探索小样本或自监督学习以降低对标注数据的依赖。此外，当前工作主要关注视觉、听觉和文本模态，未来可纳入生理信号（如脑电、心率）或具身交互等多模态信息，以更全面理解复杂情感状态。最后，在应用层面，模型的可解释性和对微妙情感（如矛盾情感）的推理能力仍有待加强，需设计更细粒度的评估指标和对抗性测试基准来推动实用化发展。

### Q6: 总结一下论文的主要内容

该论文针对多模态情感理解领域存在的挑战，提出了一个名为Emotion-LLaMAv2的新框架和MMEVerse基准。核心问题是现有多模态大语言模型在情感推理方面能力有限，且领域内缺乏高质量、大规模的情感标注数据集和标准化评估基准。

论文的方法概述包含两大贡献。一是Emotion-LLaMAv2框架，它引入了三项关键技术：1）端到端多视图编码器，无需外部人脸检测，通过更丰富的时空多视图令牌捕捉细微情感线索；2）Conv Attention预融合模块，在LLM主干网络外部实现局部与全局多模态特征的同步交互；3）在LLaMA2主干内采用感知到认知的课程指令调优方案，统一了情感识别和自由形式的情感推理。二是构建了MMEVerse基准，它整合了12个公开情感数据集（如IEMOCAP、MELD等），并通过一个涉及Qwen2 Audio、Qwen2.5 VL和GPT-4o的多智能体流程进行重新标注，形成了包含13万训练片段和3.6万测试片段的统一多模态指令格式数据集，用于大规模训练和可复现评估。

主要结论是，该工作建立了一个从训练到评估的端到端管道和标准化评估环境，显著提升了多模态大语言模型在情感识别与推理任务上的能力，为后续研究提供了高质量的数据基础和统一的评测标准。
