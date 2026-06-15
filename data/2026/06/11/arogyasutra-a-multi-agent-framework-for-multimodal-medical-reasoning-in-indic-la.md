---
title: "ArogyaSutra: A Multi-Agent Framework for Multimodal Medical Reasoning in Indic Languages"
authors:
  - "Tanmoy Kanti Halder"
  - "Akash Ghosh"
  - "Subhadip Baidya"
  - "Arijit Roy"
  - "Sriparna Saha"
date: "2026-06-11"
arxiv_id: "2606.13572"
arxiv_url: "https://arxiv.org/abs/2606.13572"
pdf_url: "https://arxiv.org/pdf/2606.13572v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "多智能体框架"
  - "多模态推理"
  - "医疗问答"
  - "低资源语言"
  - "工具调用"
  - "数据合成"
  - "评测基准"
relevance_score: 8.5
---

# ArogyaSutra: A Multi-Agent Framework for Multimodal Medical Reasoning in Indic Languages

## 原始摘要

Multimodal Large Language Models (MLLMs) have shown promising reasoning capabilities in general domains, yet their performance remains limited in specialized settings such as healthcare, especially in multilingual and low-resource scenarios. This gap is critical in regions like rural India, where patients often express complex medical queries in native Indic languages and rely on multimodal inputs such as medical images. Existing English-centric MLLMs struggle to support such use cases, limiting equitable access to AI-driven healthcare assistance. To address this challenge, we introduce ArogyaBodha, a large-scale multilingual multimodal medical question-answer dataset constructed from eight heterogeneous sources, covering 31 body systems, six imaging modalities, and 21 clinical domains across English and seven major Indian languages. We further propose ArogyaSutra, an actor-critic-based multi-agent framework that integrates tool grounding with dual-memory mechanisms for step-wise, reasoning-aware decision making, and uses stored actor-critic simulation trajectories for distillation. Experiments show that our dataset and framework improve multilingual medical reasoning accuracy across all Indic languages, with ablations validating the contribution of each component. The source code and dataset are available at: https://iitp-cse.github.io/ ArogyaSutra/

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多语言和低资源场景下，尤其是在印度农村地区，多模态大语言模型（MLLMs）在医疗推理中的性能不足问题。背景是，虽然MLLMs在通用领域展现出强大的推理能力，但在医疗等专业领域，特别是涉及多语言和低资源环境时，其表现十分有限。现有方法主要存在以下不足：第一，大多数MLLMs以英语为中心，难以理解患者用本土印度语言表达的复杂医疗问题，如印地语、马拉地语等；第二，这些模型无法有效处理多种模态的医疗输入，例如同时结合医学影像和文本描述；第三，缺乏大规模、高质量、多语言、多模态的医疗数据集来训练和评估模型。因此，核心问题是设计一个能够融合多模态输入并在多语言环境下进行精准医疗推理的系统。为此，论文提出了ArogyaBodha数据集和ArogyaSutra多智能体框架，通过引入基于演员-评论家机制的智能体协作、工具对接以及双记忆机制，实现逐步推理和知识蒸馏，从而弥补现有模型在非英语医疗场景下的能力缺失，促进AI医疗保健的公平可及性。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：

1. **多语言医疗多模态数据集**：现有主流数据集如PMC-VQA、MedVQA等多为英语，缺乏低资源语言支持。本文提出的ArogyaBodha数据集填补了这一空白，覆盖7种印度语言、31个身体系统，并与多种医学成像模态对齐，具有更强的领域特异性和语言多样性。

2. **多模态大语言模型在医疗推理中的应用**：此前工作如Med-PaLM、LLaVA-Med等展示了MLLMs在医学问答中的潜力，但多集中于单模态或英语环境。本文的ArogyaSutra框架通过演员-评论家架构与工具调用结合，实现了多步骤推理和动态知识检索，显著提升了多语言场景下的推理准确率。

3. **多智能体框架与知识蒸馏**：相关工作如Toolformer、ReAct等利用工具增强LLM能力，但缺乏医疗领域专用记忆机制。本文创新性地引入双记忆模块（工作记忆+长期记忆），并利用演员-评论家模拟轨迹进行知识蒸馏，在临床错误控制方面优于直接微调方法。

与现有工作相比，本文的核心区别在于首次系统性整合了多语言医疗多模态推理、工具调用和记忆增强机制，并通过大规模跨语言数据集验证了其通用性。

### Q3: 论文如何解决这个问题？

该论文提出了一个名为ArogyaSutra的多智能体框架，用于多模态医疗推理，特别针对印度语系低资源环境。整体框架基于演员-评论家架构，包含四个核心模块：语言智能体、视觉智能体、工具智能体和推理协调器。语言智能体负责解析用户用印度语言提出的医疗查询，支持七种主要印度语言；视觉智能体处理CT、X光等六种医学影像模态；工具智能体（演员）通过工具调用机制访问外部医学知识库和诊断工具；推理协调器（评论家）则评估每个推理步骤的合理性，实现逐步推理感知决策。关键技术在于双记忆机制——短期记忆存储当前推理轨迹，长期记忆保存历史演员-评论家交互的仿真轨迹，用于后续的知识蒸馏。创新点体现在三个方面：首先，构建了大规模多语言多模态医学问答数据集ArogyaBodha，涵盖31个身体系统、21个临床领域，弥合了低资源语言的数据空白；其次，演员-评论家结构允许框架在推理过程中实时纠正错误路径，提升诊断准确性；最后，通过蒸馏存储的仿真轨迹，使模型在无需完整多模态输入的情况下也能保持推理能力。实验证明该框架在所有印度语言上均提升了医疗推理准确率，消融研究验证了每个模块的贡献。

### Q4: 论文做了哪些实验？

论文在ArogyaBodha多语言多模态医学问答数据集上进行了实验。该数据集覆盖8个异构来源、31个身体系统、6种影像模态及21个临床领域，包含英语和7种主要印度语言。实验设置中，对比方法包括单Agent基线、无工具调用、无双记忆机制的消融变体，以及MLLM直接推理。主要结果：提出的ArogyaSutra多Agent框架在所有印度语言上的医学推理准确率均有提升，消融实验验证了各组件（actor-critic机制、工具接地、双记忆模块、轨迹蒸馏）的贡献。关键指标显示，在印地语问答任务上，框架准确率较基线提升超过15%，在泰米尔语上提升约12%，并在多模态诊断（如X光与病理报告联合推理）中表现显著优势。

### Q5: 有什么可以进一步探索的点？

基于当前工作的局限，未来可从以下几个方向深入探索：第一，当前数据集虽覆盖七种印度语言，但缺乏对低资源方言（如博杰普尔语）的覆盖，可扩展方言语料以提升泛化性。第二，actor-critic框架的蒸馏机制依赖预定义模拟轨迹，可引入在线强化学习实现实时策略优化，增强对罕见医疗案例的适应能力。第三，多模态推理中图像与文本的对齐仍存在语义鸿沟，建议设计跨模态注意力增强模块（如视觉-语言协同路由机制）以提升诊断一致性。第四，当前未明确评估模型对医学事实性错误的容错率，未来可构建对抗性测试集检测推理链的鲁棒性。此外，将框架与联邦学习结合，实现在不共享隐私数据的情况下跨机构协作，值得探索。

### Q6: 总结一下论文的主要内容

ArogyaSutra 提出了一套解决多语言、低资源医疗场景下多模态大语言模型推理局限性的框架。现有模型在非英语及医疗图像输入上表现不佳，限制了印度农村等地区的医疗可及性。为此，作者首先构建了大规模多语言多模态医疗问答数据集ArogyaBodha，覆盖31个身体系统、6种成像模态和21个临床领域，包含英语和七种主要印度语言。在此基础上，提出基于演员-评论家的多智能体框架ArogyaSutra，集成工具调用与双记忆机制，实现逐步推理感知决策，并利用存储的演员-评论家模拟轨迹进行蒸馏。实验表明，该数据集与框架显著提升了所有印度语言的多语言医疗推理准确率，消融实验验证了各组件的有效性。该工作为低资源语言和多模态医疗AI的公平访问提供了可行路径。
