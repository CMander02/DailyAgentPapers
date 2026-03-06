---
title: "Agentic Multi-Persona Framework for Evidence-Aware Fake News Detection"
authors:
  - "Roopa Bukke"
  - "Soumya Pandey"
  - "Suraj Kumar"
  - "Soumi Chattopadhyay"
  - "Chandranath Adak"
date: "2025-12-24"
arxiv_id: "2512.21039"
arxiv_url: "https://arxiv.org/abs/2512.21039"
pdf_url: "https://arxiv.org/pdf/2512.21039v2"
categories:
  - "cs.IR"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "多智能体系统"
  - "工具使用"
  - "LLM 应用"
  - "Agent 评测/基准"
  - "证据推理"
  - "多模态处理"
relevance_score: 7.5
---

# Agentic Multi-Persona Framework for Evidence-Aware Fake News Detection

## 原始摘要

The rapid proliferation of online misinformation threatens the stability of digital social systems and poses significant risks to public trust, policy, and safety, necessitating reliable automated fake news detection. Existing methods often struggle with multimodal content, domain generalization, and explainability. We propose AMPEND-LS, an agentic multi-persona evidence-grounded framework with LLM-SLM synergy for multimodal fake news detection. AMPEND-LS integrates textual, visual, and contextual signals through a structured reasoning pipeline powered by LLMs, augmented with reverse image search, knowledge graph paths, and persuasion strategy analysis. To improve reliability, we introduce a credibility fusion mechanism combining semantic similarity, domain trustworthiness, and temporal context, and a complementary SLM classifier to mitigate LLM uncertainty and hallucinations. Extensive experiments across three benchmark datasets demonstrate that AMPEND-LS consistently outperformed state-of-the-art baselines in accuracy, F1 score, and robustness. Qualitative case studies further highlight its transparent reasoning and resilience against evolving misinformation. This work advances the development of adaptive, explainable, and evidence-aware systems for safeguarding online information integrity.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动化虚假新闻检测中存在的多模态内容整合、跨领域泛化以及模型可解释性不足等核心挑战。随着在线信息的快速传播，虚假新闻对公共信任和社会稳定构成严重威胁，而现有方法难以应对其复杂性和演化速度。

研究背景方面，虚假新闻检测已从早期基于文本的分类器发展到多模态和基于大语言模型（LLM）的方法。然而，现有技术存在明显局限：多模态方法往往采用固定的编码器和浅层融合策略，难以深入整合文本、图像和上下文信息；领域自适应方法依赖领域元数据，在未见过的领域上表现脆弱；而基于LLM的方法虽然提升了语义理解能力，但存在计算成本高、多模态整合能力弱、解释缺乏证据支撑等问题，且容易产生幻觉，限制了其在关键场景中的应用。

因此，本文的核心问题是：如何构建一个既可靠又可解释的自动化系统，以有效融合多模态证据并进行稳健的跨领域虚假新闻检测。为此，论文提出了AMPEND-LS框架，通过智能体多角色推理、跨模态证据检索与可靠性融合，以及LLM与轻量级小语言模型（SLM）的协同，旨在实现高精度、强鲁棒性且证据透明的虚假新闻检测。

### Q2: 有哪些相关研究？

本文在“相关工作”章节中，将现有假新闻检测研究归纳为三大类别，并阐述了本文工作与它们的区别和联系。

**1. 多模态假新闻分析方法**：早期方法（如EANN、MVAE）简单融合文本和视觉特征，后续研究通过关注跨模态一致性（如SAFE、CAFE）或引入对比学习（如StruACL、COOLANT）来改进。图神经网络（如HSEN、KAMP）和基于Transformer的架构进一步整合了语义和知识图谱。本文指出，这些方法大多依赖预训练编码器，计算成本高，且缺乏显式的、基于证据的推理和可解释性。**本文的AMPEND-LS框架通过结构化推理流程，显式整合文本、视觉和上下文证据，并引入可靠性融合机制，旨在提供更透明、证据驱动的分析。**

**2. 基于领域自适应的方法**：这类方法（如HFGD、MMDFND、BREAK）旨在处理数据分布变化，常采用分层或基于注意力的机制进行跨域适应。迁移学习（如MMHT）和生成模型（如MVAE、GSFND）也被用于特征对齐或数据增强。然而，它们通常依赖领域标签或用户参与信号，且可解释性不足。**本文工作不依赖于特定的领域标签，而是通过多角色智能体推理和上下文证据（如时效性）来增强对未知或动态领域的适应能力。**

**3. 基于先进语言模型的技术**：大语言模型通过增强推理（如GLPN-LLM、PCoT）和提升鲁棒性（如IMRRF、AdStyle）推动了该领域发展。检索与协作（如SR3）以及数据增强方法（如TripleFact）也被应用。但这些方法存在计算成本高、多模态整合较浅、易受数据污染等局限。**本文的AMPEND-LS框架通过LLM-SLM协同机制来应对这些挑战：利用LLM进行结构化、多角色的深度推理，同时引入轻量级SLM分类器来缓解LLM的不确定性和幻觉，从而在保持强推理能力的同时提升可靠性和可部署性。**

综上，本文提出的AMPEND-LS框架旨在综合解决现有方法在**证据推理、可解释性、领域泛化和计算效率**方面的不足，通过**智能体多角色推理、证据融合与LLM-SLM协同**，构建一个更稳健、可解释且适应动态环境的检测系统。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AMPEND-LS的智能体多角色证据驱动框架来解决假新闻检测问题，其核心是构建一个结构化的多模态推理管道，并利用大语言模型（LLM）与小语言模型（SLM）的协同作用来提升性能、可靠性和可解释性。

**整体框架与主要模块**：
AMPEND-LS的流程始于**预处理模块**，该模块对新闻的标题、正文和图像进行结构化处理，包括文本清洗、基于LLM的实体感知声明生成以及利用视觉API生成图像摘要，为后续分析提供语义丰富的输入。

随后是**证据检索与可信度评估模块**，这是方法的关键创新之一。它从多种来源检索证据：1）针对文本声明进行网络搜索，并采用BM25和BERT-Score的混合方法评估相关性；2）引入**领域可信度分析**，利用Media Bias/Fact Check数据库对信息来源进行评级并赋予权重，以优先选择可信来源；3）实施**时间证据过滤**，通过分析检索结果的中位发布时间来排除过时信息，确保证据的时效性；4）进行**反向图像搜索**以追溯图片来源和上下文；5）从知识图谱中查询实体关系事实作为结构化证据。这些证据的可靠性通过一个加权融合了语义相似性、领域可信度和时间一致性的综合分数进行排序和筛选。

框架的核心是**多步骤多角色智能体框架**。该模块设计了多个具有特定角色的LLM智能体（如监督员、记者、法律分析师、科学专家）和一个专门的回答智能体。这些智能体通过迭代的问答互动，从不同专业视角（如事实核查、法律合规、科学验证）对声明和证据进行分析。所有交互被记录在一个共享内存中，从而协调推理过程，生成最终的预测和可解释的论证链。对于不确定的案例，框架还会运用说服策略分析来提升标签质量。

最后，为了应对LLM可能存在的幻觉和不确定性，并提升推理效率，框架包含一个**SLM适应阶段**。该阶段将LLM生成的伪标签和推理过程提炼到一个轻量级模型中，从而在保持可解释性的同时实现快速、资源高效的推断，并增强了模型的泛化能力。

**创新点**：
1. **多角色智能体协同推理**：通过组织具有不同专业背景的LLM智能体进行结构化、迭代的问答，实现了多视角、证据驱动的深度分析，显著提升了检测的鲁棒性和可解释性。
2. **多维度证据可信度融合机制**：创新性地将语义相关性、领域可信度权重和时序上下文过滤相结合，构建了一个综合的证据可靠性评估体系，有效降低了不可靠或过时信息的影响。
3. **LLM-SLM协同设计**：利用LLM进行复杂的多模态推理和证据整合，同时通过SLM对推理过程进行提炼和加速，在保证高性能的同时，解决了LLM的不确定性、幻觉和效率问题，实现了优势互补。

### Q4: 论文做了哪些实验？

实验在配备PyTorch 2.5.1、CUDA 12.1、NVIDIA A100-SXM4-40GB GPU和AMD EPYC 7742 64核CPU（1 TB RAM）的系统上进行。实验使用了三个基准数据集：PolitiFact（政治事实核查）、GossipCop（娱乐八卦新闻）和MMCoVaR（COVID-19疫苗相关多模态信息）。数据按7:2:1划分训练集、验证集和测试集。

对比方法包括两类：基于LLM的方法（LMDD、FactAgent）和基于学习的方法（MFCL、BREAK、MGCA、EARAM、FakingRecipe）。评估指标包括准确率（Acc）、F1分数（F1）、精确率（Pre）和召回率（Rec），并计算了相对于次优基线的提升百分比。此外，为评估LLM生成理由的质量，采用了三个指标：效用（Utility）、泄漏调整模拟度（LAS）和基于条件V信息的理由评估（REV）。

主要结果显示，AMPEND-LS在所有数据集上均优于基线方法。在GossipCop上提升最显著，准确率和F1分数分别比最强基线高出6.17%和9.07%。在PolitiFact和MMCoVaR上也观察到稳定提升，表明模型在文本中心和多模态场景下均有良好泛化能力。AMPEND-LS在所有指标上表现均衡，未出现如某些基线方法那样的精确率-召回率失衡问题。例如，在MMCoVaR上，AMPEND-LS的准确率达到89.34%，F1分数为88.97%，均显著高于基线。这些结果证明了该框架在异构领域中的鲁棒性和稳定性。

### Q5: 有什么可以进一步探索的点？

该论文提出的AMPEND-LS框架虽然在多模态虚假新闻检测上取得了显著效果，但仍存在一些局限性和值得深入探索的方向。首先，框架严重依赖外部知识源（如反向图像搜索、知识图谱），其质量和覆盖范围直接影响系统性能，未来可研究如何动态评估和融合多源证据的可靠性，或构建领域自适应的知识库。其次，LLM与SLM的协同机制仍较简单，主要依赖SLM纠正LLM的不确定性，未来可探索更精细的交互模式，如迭代式相互验证或基于置信度的动态权重调整。此外，框架的实时性和可扩展性未充分讨论，面对海量社交媒体流数据时，复杂的多步骤推理可能成为瓶颈，未来需优化推理效率，例如引入轻量化模型或增量学习策略。最后，当前评估集中于静态数据集，未来应在动态、对抗性环境中测试其鲁棒性，并探索如何将用户反馈和社会网络上下文更有效地融入证据融合机制，以提升对新兴虚假新闻模式的适应能力。

### Q6: 总结一下论文的主要内容

本文提出了一种名为AMPEND-LS的新型智能体多角色框架，旨在解决多模态虚假新闻检测中存在的泛化能力不足、可解释性差等挑战。其核心贡献在于构建了一个证据驱动的、结合大语言模型（LLM）与小语言模型（SLM）协同工作的检测系统。

该框架的问题定义是提升虚假新闻检测在跨模态、跨领域场景下的准确性、鲁棒性和可解释性。方法上，AMPEND-LS通过一个结构化的LLM推理流程，整合文本、图像和上下文信号，并辅以反向图像搜索、知识图谱路径和说服策略分析来获取多源证据。为确保可靠性，它设计了融合语义相似度、领域可信度和时间上下文的可信度评估机制，并引入一个互补的SLM分类器来缓解LLM的不确定性和幻觉问题。

主要结论是，在三个基准数据集上的大量实验表明，AMPEND-LS在准确率、F1分数和鲁棒性上均持续优于现有先进方法。定性案例研究进一步验证了其透明的推理过程和对演化中虚假信息的抵御能力。这项研究推动了自适应、可解释且注重证据的在线信息完整性保护系统的发展。
