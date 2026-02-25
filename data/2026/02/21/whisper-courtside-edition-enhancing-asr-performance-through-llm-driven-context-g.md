---
title: "Whisper: Courtside Edition Enhancing ASR Performance Through LLM-Driven Context Generation"
authors:
  - "Yonathan Ron"
  - "Shiri Gilboa"
  - "Tammuz Dubnov"
date: "2026-02-21"
arxiv_id: "2602.18966"
arxiv_url: "https://arxiv.org/abs/2602.18966"
pdf_url: "https://arxiv.org/pdf/2602.18966v1"
categories:
  - "cs.CL"
tags:
  - "多智能体系统"
  - "LLM应用"
  - "工具使用"
  - "领域适应"
  - "自动语音识别"
relevance_score: 7.5
---

# Whisper: Courtside Edition Enhancing ASR Performance Through LLM-Driven Context Generation

## 原始摘要

Domain-specific speech remains a persistent challenge for automatic speech recognition (ASR), even for state-of-the-art systems like OpenAI's Whisper. We introduce Whisper: Courtside Edition, a novel multi-agent large language model (LLM) pipeline that enhances Whisper transcriptions without retraining. The pipeline intercepts Whisper's initial transcript, applies specialized LLM agents for domain context identification, named entity recognition, and jargon detection, and generates compact prompts that guide Whisper's decoder. Evaluated on 421 NBA basketball commentary segments (a domain characterized by dense proper nouns and technical terminology) our best pipeline achieves a statistically significant 17.0% relative reduction in word error rate (WER; from 0.217 to 0.180, p<0.001). Improvements are observed in 40.1% of segments with degradation in only 7.1%, substantially outperforming direct transcript post-editing. These results demonstrate that prompt-based augmentation can deliver scalable domain adaptation for ASR, offering a practical alternative to costly model fine-tuning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决通用自动语音识别（ASR）系统（如OpenAI的Whisper）在处理领域特定语音时性能显著下降的问题。具体而言，当语音内容包含密集的专有名词、技术术语、特定口音或快速语境化表达时，即使是最先进的ASR模型也会产生系统性错误，导致转录文本的语义完整性受损。

论文以NBA篮球解说这一极具挑战性的领域作为焦点案例。该场景的语音特点包括：大量球员/教练姓名（易被替换为发音相似的常见词）、专业的篮球术语、多样的口音以及嘈杂的背景音和快速解说。这些因素使得Whisper等通用模型在该领域的词错误率（WER）较高（基线为0.217），严重影响了转录结果的实用性。

因此，论文的核心目标是：在不重新训练ASR模型的前提下，提出一种高效、可扩展的领域自适应方法，以显著提升Whisper在特定领域（如体育解说）的转录准确性。其解决方案是设计一个由大型语言模型驱动的多智能体流程，通过识别领域上下文、纠正实体和术语，并生成紧凑的提示词来引导Whisper的解码过程，从而将领域知识注入识别环节，而非仅仅进行后处理修正。

### Q2: 有哪些相关研究？

相关工作主要涉及三个方向：自动语音识别（ASR）的领域自适应、LLM增强的ASR以及多智能体系统。

在**ASR领域自适应**方面，传统方法依赖于声学模型微调或语言模型适应，需要大量标注数据和重新训练，成本高昂。近期出现了上下文偏置方法，例如CB-Whisper通过关键词注入来引导解码，但仍需修改和重新训练模型。本文提出的方法与之形成对比，它完全避免了重新训练，仅通过智能提示生成来实现领域适应，提供了一种更轻量、可扩展的替代方案。

在**LLM增强ASR**方面，已有研究利用LLM对ASR转录结果进行后处理，以修正拼写或语法错误，但这类方法无法纠正因音频误听导致的根本性错误。另一些工作探索了使用LLM生成提示来改善命名实体识别或进行上下文预置，但评估范围较窄。本文工作推进了这一方向，通过系统性地协调生成针对多种错误类型（如专有名词、行话、上下文）的提示，实现了在完整领域规模上的稳健性能提升。

在**多智能体系统**方面，现有框架（如AutoGPT）展示了将复杂任务分解并由专门智能体协作处理的优势。本文受此启发，首次将多智能体LLM架构应用于通过Whisper提示机制增强语音识别的任务，通过分配主题检测、实体规范化等子任务给不同智能体，实现了对ASR错误模式的精准靶向处理。

### Q3: 论文如何解决这个问题？

论文通过设计一个多智能体LLM流水线，利用Whisper模型自带的`initial_prompt`机制，在不重新训练模型的情况下，实现了对特定领域（如NBA篮球解说）语音识别性能的增强。其核心方法是拦截Whisper的初次转录文本，通过一系列 specialized LLM 智能体进行分析和上下文生成，并将生成的紧凑提示词反馈给Whisper的解码器，以在第二次解码过程中引导其偏向正确的领域词汇。

**核心架构与流程**：流水线包含六个核心智能体模块。首先，**主题分类智能体**识别音频的领域上下文（如“NBA篮球解说”）。接着，**命名实体识别智能体**从初稿中提取人名，并与完整的NBA球员名单进行模糊匹配（使用Levenshtein距离等），以校正拼写。**行话提取智能体**则结合关键词提取算法（如RAKE, YAKE）和篮球术语词典，识别领域特定术语。为确保质量，后续的**决策过滤逻辑**（由多个验证智能体组成）至关重要，它通过置信度阈值（如NER相似度≥0.85）和语义连贯性检查，防止过度校正，并确保最终提示长度不超过Whisper的224个token限制。**候选选择器**负责整合并修剪来自各模块的候选项目，**句子构建器**则将筛选出的主题、校正后的人名和行话组合成一个简洁、自然的句子作为最终提示。

**关键技术**：该方法的关键在于巧妙利用了Whisper模型的**初始提示机制**。该机制允许在解码器的输入序列前添加上下文文本，且模型仅关注最后≤224个token。因此，流水线生成的提示句子被精心设计，将最有价值的词汇（如罕见球员名、专业术语）放置在句子末尾，以最大化其对解码过程的偏置影响。与直接使用LLM进行转录后编辑（P2变体）相比，这种“提示注入”方法能让Whisper在结合音频证据的同时进行解码，从根本上纠正因发音相似或词汇生僻导致的错误。

**流水线演进**：论文通过四个渐进的变体（P1到P4）验证了设计的有效性。从仅提供主题（P1），到加入人名（P3），最终到包含所有智能体及过滤决策的完整多智能体流水线（P4），性能逐步提升。P4通过严格的验证和过滤，在提供丰富领域上下文的同时，有效避免了无关词汇的引入，从而在显著降低词错误率的同时，将性能退化片段的比例控制在最低水平。

### Q4: 论文做了哪些实验？

论文在421段NBA篮球解说片段上进行了实验评估。实验设置以Whisper的原始转录作为基线，对比了四种不同的多智能体LLM流程变体：P1（仅主题识别）、P2（LLM直接后编辑修正）、P3（增强版命名实体识别）和P4（完整多智能体流程）。基准测试使用词错误率作为核心指标，并辅以片段级改进分析和统计显著性检验（Wilcoxon符号秩检验）。

主要结果显示，完整多智能体流程（P4）取得了最佳性能：平均WER从基线的0.217显著降低至0.180，实现了17.0%的相对降低（p<0.001）。在片段层面，40.1%的片段得到改善，而性能下降的片段仅占7.1%。其他流程变体效果有限或甚至有害：P1（仅主题）使WER上升至0.238；P2（后编辑）与基线持平；P3（命名增强）虽有改善（WER 0.210），但退化率较高（20.7%）。错误分析表明，流程成功纠正了专有名词（如“anteto kumbo”转为“Antetokounmpo”）和战术术语，主要失败模式是过度校正和超范围术语。

### Q5: 有什么可以进一步探索的点？

基于论文提出的未来工作方向，可以进一步探索的点包括：**跨领域验证**，将方法应用于医疗、法律、学术等更多专业领域以检验其通用性；**实时性优化**，通过智能体并行化、部署本地轻量模型或与流式ASR系统集成，以满足低延迟场景（如直播）的需求；**多模态增强**，结合视频信息（如球员识别、比赛状态）为体育解说等场景提供更丰富的上下文，从而进一步消除语音歧义；以及**自适应学习机制**，引入用户反馈闭环，使系统能够动态更新领域知识和智能体行为，实现持续优化。

当前方法的局限性在于其性能提升严重依赖外部LLM生成的高质量提示，且处理流程可能引入额外延迟，难以直接用于实时应用。未来可探索更高效的上下文压缩与注入机制，并研究如何在不依赖庞大LLM的情况下实现轻量、自适应的领域知识获取与集成。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为“Whisper: Courtside Edition”的创新方法，用于提升自动语音识别（ASR）在特定领域的性能。其核心贡献在于设计了一个无需重新训练ASR模型的多智能体大语言模型（LLM）流水线。该流水线首先截取Whisper模型的初始转录文本，然后利用多个专门的LLM智能体进行领域上下文识别、命名实体识别和术语检测，最终生成精炼的提示词来引导Whisper的解码器进行修正。

在包含421段NBA篮球评论（具有大量专有名词和技术术语）的数据集上评估，该方法实现了17.0%的词错误率相对降低，且性能提升具有统计显著性。结果表明，基于提示的增强方法为ASR的领域自适应提供了一种可扩展且实用的替代方案，避免了成本高昂的模型微调。这项工作展示了ASR与LLM协作的潜力，通过模块化的多智能体架构，结合声学建模与上下文推理能力，为复杂AI应用提供了新思路。
