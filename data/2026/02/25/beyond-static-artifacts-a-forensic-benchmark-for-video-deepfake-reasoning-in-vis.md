---
title: "Beyond Static Artifacts: A Forensic Benchmark for Video Deepfake Reasoning in Vision Language Models"
authors:
  - "Zheyuan Gu"
  - "Qingsong Zhao"
  - "Yusong Wang"
  - "Zhaohong Huang"
  - "Xinqi Li"
  - "Cheng Yuan"
  - "Jiaowei Shao"
  - "Chi Zhang"
  - "Xuelong Li"
date: "2026-02-25"
arxiv_id: "2602.21779"
arxiv_url: "https://arxiv.org/abs/2602.21779"
pdf_url: "https://arxiv.org/pdf/2602.21779v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Vision-Language Models"
  - "Benchmark"
  - "Video Analysis"
  - "Deepfake Detection"
  - "Temporal Reasoning"
relevance_score: 4.0
---

# Beyond Static Artifacts: A Forensic Benchmark for Video Deepfake Reasoning in Vision Language Models

## 原始摘要

Current Vision-Language Models (VLMs) for deepfake detection excel at identifying spatial artifacts but overlook a critical dimension: temporal inconsistencies in video forgeries. Adapting VLMs to reason about these dynamic cues remains a distinct challenge. To bridge this gap, we propose Forensic Answer-Questioning (FAQ), a large-scale benchmark that formulates temporal deepfake analysis as a multiple-choice task. FAQ introduces a three-level hierarchy to progressively evaluate and equip VLMs with forensic capabilities: (1) Facial Perception, testing the ability to identify static visual artifacts; (2) Temporal Deepfake Grounding, requiring the localization of dynamic forgery artifacts across frames; and (3) Forensic Reasoning, challenging models to synthesize evidence for final authenticity verdicts. We evaluate a range of VLMs on FAQ and generate a corresponding instruction-tuning set, FAQ-IT. Extensive experiments show that models fine-tuned on FAQ-IT achieve advanced performance on both in-domain and cross-dataset detection benchmarks. Ablation studies further validate the impact of our key design choices, confirming that FAQ is the driving force behind the temporal reasoning capabilities of these VLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前视觉语言模型在深度伪造检测中忽视视频时序不一致性这一关键维度的问题。随着AIGC技术的快速发展，生成逼真的深度伪造内容变得愈发容易，引发了社会对其潜在风险的广泛担忧。虽然已有研究开始探索利用VLMs进行深度伪造检测，并取得了一些成果，但这些方法主要侧重于识别静态图像中的空间伪影（如面部感知层面的细微视觉异常），而未能有效利用视频伪造中动态的、跨帧的时序不一致线索。现有方法通常通过监督微调范式，使用从视频中抽取的静态图像和有限的问答模板进行训练，导致模型只能学习空间判别信息，无法捕捉和推理时间维度上的伪造痕迹。

因此，本文的核心问题是：如何有效地构建训练数据，以引导和增强VLMs发现并推理视频深度伪造中的时序不一致性，从而建立更全面、鲁棒的深度伪造检测基线。为此，论文提出了Forensic Answer-Questioning基准，通过构建一个包含三个渐进层次（面部感知、时序伪造定位、法证推理）的大规模多项选择题评测基准，将时序深度伪造分析任务形式化，旨在系统性地评估并提升VLMs利用动态线索进行法证推理的能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：传统深度伪造检测数据集、基于视觉语言模型（VLM）的可解释检测方法，以及面向深度伪造的问答（QA）数据集。

在**传统检测数据集**方面，早期工作如FaceForensics++、Celeb-DF、DeeperForensics和WildDeepfake等，专注于提供用于二元分类（真/假）的视频数据，并通过不同压缩级别、合成技术或真实网络收集来增强数据多样性与挑战性。然而，这些数据集通常不提供对伪造原因或位置的解释，导致训练出的模型缺乏可解释性和跨域推理能力，尤其忽略了视频中动态的时间不一致性线索。

在**基于VLM的可解释检测方法**上，近期研究如FakeShield、Huang等人的工作以及M2F2-Det，将深度伪造检测重新定义为结合视觉感知与文本解释的多模态推理任务。它们利用VLM生成可解释的文本推理或定位结果，超越了简单的二元分类。但这些方法大多将视频视为静态帧的集合，未能充分挖掘和利用**时间维度**上的操纵证据，而本文则专注于动态不一致性，并构建了时序定位与推理的问答对来增强VLM的时序分析能力。

在**QA数据集**方面，DD-VQA和VLFFD等率先引入了基于问答的格式，以提升检测的可解释性，关注点包括人脸感知异常或通过自动提示生成高质量问答对。Forensics-Bench则涵盖识别、定位和推理等多种任务，但主要针对静态图像或AI生成内容。相比之下，本文提出的FAQ基准**专门针对视频深度伪造**，通过精心设计的三层层次化问答任务（面部感知、时序深度伪造定位、法证推理），系统性地引导VLM学习并推理时序层面的伪造证据，弥补了现有工作对动态线索建模的不足。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为“法证问答”（FAQ）的大规模基准测试来解决视频深度伪造检测中时间不一致性分析不足的问题。其核心方法是将时序深度伪造分析构建为一个多项选择题任务，并设计了一个三层渐进式评估框架，以系统性地提升视觉语言模型（VLMs）的法证推理能力。

整体框架分为三个主要层级：第一层是“面部感知”，专注于评估模型识别静态视觉伪影（如面部扭曲、纹理异常）的能力；第二层是“时序深度伪造定位”，要求模型在连续帧中定位动态伪造伪影，例如不自然的面部运动或背景闪烁；第三层是“法证推理”，挑战模型综合前两层的证据，最终做出真实性判断。这种层级设计迫使模型不仅关注单帧特征，还需理解帧间时序关系。

关键技术包括：1）构建大规模、多样化的视频深度伪造数据集，涵盖多种伪造方法（如换脸、表情操纵）和场景；2）将每段视频与一系列结构化问答对配对，问题设计紧扣三层能力评估，答案以多项选择形式呈现；3）基于FAQ基准生成指令调优数据集FAQ-IT，用于微调VLMs，使其学会结合时空线索进行推理。

创新点在于首次将时序深度伪造分析系统化为一个多层级问答任务，突破了现有VLMs仅依赖静态伪影检测的局限。通过FAQ-IT的微调，模型能够整合动态不一致性证据，从而在领域内和跨数据集检测基准上取得先进性能。消融实验进一步验证了FAQ框架各层级设计对提升时序推理能力的关键作用。

### Q4: 论文做了哪些实验？

论文实验主要包括对提出的FAQ基准进行零样本评估、使用FAQ-IT数据集进行指令微调、消融研究以及跨数据集泛化能力测试。

**实验设置与数据集**：在提出的FAQ基准（包含面部感知、时序深度伪造定位和取证推理三个层级）上评估了13个开源和闭源VLM，包括InternVL、LLaVA、DeepSeek-VL、Qwen系列、GPT-4o和Gemini-2.5-Flash等。使用多项选择题（MCQ）准确率作为主要评估指标。生成了指令微调集FAQ-IT，并选择Qwen2.5-VL-7B和LLaVA-NeXT-7B进行有监督微调，训练时冻结视觉编码器，优化视觉连接器和LLM参数，使用AdamW优化器，批量大小为16，学习率1e-5。

**对比方法与主要结果**：
1.  **零样本评估**：所有模型在FAQ基准上表现不佳，平均准确率较低（最高为ShareGPT4V-7B的39.7%）。模型在Level 1（面部感知）有一定能力，但在Level 2和Level 3（时空定位和复杂推理）表现显著下降。具体数据：GPT-4o平均22.8%，Gemini-2.5-Flash平均27.8%，开源模型中ShareGPT4V-7B在Level 1达73.8%，Qwen3-VL-8B在Level 2达29.4%。
2.  **指令微调效果**：使用完整FAQ-IT微调后，模型性能大幅提升。Qwen2.5-VL平均准确率从21.6%提升至52.4%（+30.8%），LLaVA-NeXT从30.3%提升至53.7%（+23.4%）。仅使用静态数据（FAQ-IT♠）微调则提升有限。
3.  **下游深度伪造检测**：在FF++数据集上，微调后模型检测准确率显著提高。Qwen2.5-VL在五种伪造类型（FS、NT、F2F、DF、FSh）上的平均MCQ准确率从9.6%提升至41.5%，检测准确率从22.8%提升至73.8%。LLaVA-NeXT检测准确率从20.0%提升至69.3%。
4.  **鲁棒性分析**：测试了不同视频压缩级别（原始质量、c23、c40）下的性能。模型在原始质量和轻度压缩（c23）下保持较高准确率，但在重度压缩（c40）下性能显著下降。
5.  **跨数据集评估**：在未见过的Celeb-DF、DeeperForensics和WildDeepfake数据集上测试泛化能力。完整微调后，Qwen2.5-VL在三个数据集上的准确率分别达到73.3%、78.6%和65.9%；LLaVA-NeXT分别达到72.9%、77.8%和63.1%，相比零样本设置有大幅提升。

**关键指标**：主要使用MCQ准确率（%）和检测准确率（%）进行评估。消融研究证实完整FAQ数据是提升时序推理能力的关键。

### Q5: 有什么可以进一步探索的点？

该论文提出的FAQ基准主要关注视频深度伪造中时序不一致性的推理，但仍存在一些局限性和可拓展方向。首先，基准主要基于多选问答形式，未来可探索更开放的生成式任务，如要求模型直接描述伪造片段的时间位置和异常特征，以测试更细粒度的推理能力。其次，当前任务依赖人工标注的时序注释，可研究如何利用弱监督或自监督方法从大量未标注视频中学习动态伪造模式，降低标注成本并提升泛化性。此外，模型目前主要针对面部伪造，未来可扩展至全身动作、背景一致性等更复杂的时空伪造场景。另一个方向是结合多模态大模型的链式推理能力，设计分步骤的推理提示，让模型先定位可疑帧，再分析具体异常，最后综合判断，以提升可解释性。最后，跨数据集和跨伪造技术的泛化能力仍需加强，可通过引入更丰富的伪造方法（如神经辐射场重建）和真实世界干扰（如压缩、光照变化）来构建更鲁棒的评估体系。

### Q6: 总结一下论文的主要内容

该论文针对当前视觉语言模型在深度伪造检测中过度依赖空间伪影而忽视视频时序不一致性的问题，提出了一个名为“法证问答”的大规模基准测试。其核心贡献在于将时序深度伪造分析构建为多选题任务，并通过三层渐进式评估体系系统提升模型的法证推理能力：第一层关注面部感知，检测静态视觉伪影；第二层要求时序深度伪造定位，即跨帧定位动态伪造痕迹；第三层挑战模型进行法证推理，综合证据做出真实性判定。论文还生成了对应的指令微调数据集FAQ-IT，实验表明，经其微调的模型在领域内和跨数据集检测基准上均取得先进性能。该工作不仅填补了时序深度伪造分析评估的空白，也为增强视觉语言模型的动态推理能力提供了有效路径。
