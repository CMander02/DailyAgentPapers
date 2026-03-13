---
title: "Speak or Stay Silent: Context-Aware Turn-Taking in Multi-Party Dialogue"
authors:
  - "Kratika Bhagtani"
  - "Mrinal Anand"
  - "Yu Chen Xu"
  - "Amit Kumar Singh Yadav"
date: "2026-03-12"
arxiv_id: "2603.11409"
arxiv_url: "https://arxiv.org/abs/2603.11409"
pdf_url: "https://arxiv.org/pdf/2603.11409v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "对话智能体"
  - "多轮对话"
  - "上下文感知"
  - "监督微调"
  - "基准测试"
relevance_score: 8.0
---

# Speak or Stay Silent: Context-Aware Turn-Taking in Multi-Party Dialogue

## 原始摘要

Existing voice AI assistants treat every detected pause as an invitation to speak. This works in dyadic dialogue, but in multi-party settings, where an AI assistant participates alongside multiple speakers, pauses are abundant and ambiguous. An assistant that speaks on every pause becomes disruptive rather than useful. In this work, we formulate context-aware turn-taking: at every detected pause, given the full conversation context, our method decides whether the assistant should speak or stay silent. We introduce a benchmark of over 120K labeled conversations spanning three multi-party corpora. Evaluating eight recent large language models, we find that they consistently fail at context-aware turn-taking under zero-shot prompting. We then propose a supervised fine-tuning approach with reasoning traces, improving balanced accuracy by up to 23 percentage points. Our findings suggest that context-aware turn-taking is not an emergent capability; it must be explicitly trained.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多参与者对话场景中，基于大语言模型的语音助手在轮次转换（turn-taking）方面存在的根本性缺陷。现有语音助手通常将检测到的每一次停顿都视为发言邀请，这在双人对话中尚可接受，但在多人对话（如会议、群聊）中，停顿频繁且含义模糊，导致助手要么频繁打断对话（在不应发言时发言），要么在被明确需要时保持沉默。论文将这一问题形式化为“上下文感知的轮次转换”任务：在每一次检测到的停顿处，给定完整的对话上下文，模型需要决策目标发言者（即AI助手）是应该“发言”还是“保持沉默”。核心目标是提升AI助手在复杂社交对话中的参与时机判断能力，使其行为更符合人类社交规范，从而变得有用而非干扰。

### Q2: 有哪些相关研究？

相关研究主要分为几个方向：1) **双人对话轮次转换**：传统研究聚焦于从语言线索预测轮次边界，或利用语音活动投影进行信号级预测。近期工作也探讨了LLM在识别“转换关联位置”方面的困难，但均局限于两人交互。2) **多人对话子问题**：包括说话人感知的话语解析、受话人识别以及在多人结构下的回复选择。这些研究解决了孤立的结构性子问题，但未整合为助手在每个停顿处需要做出的综合决策。3) **多人智能体参与决策**：例如MultiLIGHT数据集研究了角色扮演环境中的参与决策，但其源于幻想游戏，未能捕捉自然口语对话的动态。此外，MuPaS等工作关注预测下一个发言者，而非针对特定参与者的二元决策。本文工作与这些研究的区别在于：首先，将任务形式化为针对特定参与者（AI助手）的二元决策；其次，构建了基于自然多领域对话语料的大规模细粒度标注基准；最后，系统评估了最新LLM的零样本能力，并提出了结合推理追踪的监督微调方法，取得了显著提升。

### Q3: 论文如何解决这个问题？

论文通过构建大规模基准、系统评估和提出新的训练方法来解决该问题。**核心方法**包括：1) **问题形式化与基准构建**：将上下文感知轮次转换定义为监督预测任务。从AMI会议语料库、Friends电视剧剧本和SPGISpeech金融电话三个多参与者公开语料库中，构建了超过12万个标注决策点的大规模基准。每个决策点根据目标发言者是否在下一句发言，标注为“发言”或“沉默”，并进一步细分为四个类别：明确被提及、上下文干预、无提及、被提及但非受话，以捕捉不同的社交情境。2) **大规模模型评估**：在零样本提示下评估了8个最新的开源和闭源LLM，发现所有模型在该任务上都表现不佳，普遍存在“发言”偏见，表明上下文感知轮次转换并非LLM的涌现能力。3) **监督微调与推理蒸馏**：提出使用LoRA对开源模型进行监督微调。创新性地引入了两种训练模式：仅输出决策的“决策模式”和先输出推理再输出决策的“推理+决策模式”。为了获得训练所需的推理轨迹，采用标签条件蒸馏技术，使用教师模型根据真实标签为每个样本生成一句解释性理由。训练时采用四类别平衡批次采样以避免数据不平衡。实验表明，这种结合显式推理生成的微调方法能显著提升模型性能。

### Q4: 论文做了哪些实验？

论文进行了三项核心实验：1) **零样本提示实验**：在构建的基准测试集上评估了GPT-5.2、Gemini 3.1 Pro以及六个开源模型。使用准确率、类别平均F1分数和平衡准确率作为指标。结果显示，所有模型表现均不理想，最佳模型Gemini 3.1 Pro在SPGI数据集上的平衡准确率仅为64.45%，开源模型接近随机水平。模型在需要保持沉默的S1和S2类别上准确率极低，证实了零样本的失败。重复系统提示仅带来边际改善。2) **监督微调实验**：对开源模型进行LoRA微调。结果显示，除GPT-OSS-20B外，所有模型性能均大幅提升，平衡准确率最高提升23个百分点。性能提升主要来自需要语用推理以保持沉默的S1和S2类别。3) **消融分析与人类评估**：**消融实验**表明，“推理+决策”训练模式比“仅决策”模式性能更优；LoRA秩为32时效果最佳；合并所有数据集进行训练得到的单一模型，其跨领域泛化性能与领域特定微调模型相当。**人类评估**在Friends数据集子集上进行，三位标注者的平衡准确率在60-66%之间，在S2类别上表现尤其不佳，且标注者间一致性仅为中等。这表明任务本身具有挑战性和主观性。值得注意的是，经过微调的最佳模型达到了甚至超过了人类水平的平衡准确率。

### Q5: 有什么可以进一步探索的点？

论文指出了几个有前景的未来方向：1) **融入多模态线索**：当前工作仅基于文本转录。在实际语音交互中，语调、重音、停顿时长、眼神接触和手势等非语言线索对轮次转换至关重要。未来的研究可以整合音频和视觉模态，构建更鲁棒的实时决策系统。2) **增强跨领域与零样本泛化**：虽然合并数据集训练显示了初步的泛化能力，但如何让模型更好地适应训练数据未覆盖的全新领域或对话风格，仍需探索。这可能涉及元学习、提示工程或更高效的知识迁移技术。3) **实时部署与延迟优化**：为了应用于真实语音助手，模型需要在极低延迟下运行，并处理流式对话输入。研究高效的模型压缩、缓存策略和增量上下文处理是关键。4) **更复杂的决策与主动参与**：当前任务是二元决策。未来可以扩展为预测最佳发言时机、生成适当的反馈词或决定发言内容（而不仅仅是是否发言），使助手能进行更自然、主动的对话管理。5) **探索模型失败的根本原因**：进一步分析为何某些模型架构（如推理导向模型）从SFT中获益有限，有助于设计更适合社交推理任务的模型或适配器。

### Q6: 总结一下论文的主要内容

本论文系统地研究并解决了基于LLM的语音助手在多人对话场景中“何时发言”的核心难题。其主要贡献有三点：首先，明确定义了“上下文感知轮次转换”任务，并构建了一个包含12万样本、覆盖三个领域、具有细粒度四类别标注的大规模基准数据集。其次，通过对八个前沿LLM的零样本评估，首次实证表明上下文感知轮次转换能力并非当前LLM的涌现属性，它们普遍存在严重缺陷。最后，论文提出了一种创新的监督微调方法，通过结合标签条件蒸馏生成的推理轨迹进行训练，显著提升了模型性能，平衡准确率最高提升23个百分点，甚至达到了人类水平。这项工作不仅为评估和提升对话智能体的社交智能提供了重要的基准和方法，也明确指出，要构建在复杂多人交互中行为得体的AI助手，需要进行针对性的、数据驱动的训练。
