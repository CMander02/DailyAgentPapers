---
title: "MERRIN: A Benchmark for Multimodal Evidence Retrieval and Reasoning in Noisy Web Environments"
authors:
  - "Han Wang"
  - "David Wan"
  - "Hyunji Lee"
  - "Thinh Pham"
  - "Mikaela Cankosyan"
  - "Weiyuan Chen"
  - "Elias Stengel-Eskin"
  - "Tu Vu"
  - "Mohit Bansal"
date: "2026-04-15"
arxiv_id: "2604.13418"
arxiv_url: "https://arxiv.org/abs/2604.13418"
pdf_url: "https://arxiv.org/pdf/2604.13418v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.CV"
tags:
  - "Benchmark"
  - "Multimodal"
  - "Web Search"
  - "Retrieval-Augmented Generation"
  - "Tool Use"
  - "Reasoning"
  - "Evaluation"
relevance_score: 8.5
---

# MERRIN: A Benchmark for Multimodal Evidence Retrieval and Reasoning in Noisy Web Environments

## 原始摘要

Motivated by the underspecified, multi-hop nature of search queries and the multimodal, heterogeneous, and often conflicting nature of real-world web results, we introduce MERRIN (Multimodal Evidence Retrieval and Reasoning in Noisy Web Environments), a human-annotated benchmark for evaluating search-augmented agents. MERRIN measures AI agents' ability to identify relevant modalities, retrieve multimodal evidence, and perform multi-hop reasoning over noisy web sources. It differs from prior work in three important aspects: (1) using natural language queries without explicit modality cues, (2) incorporating underexplored modalities such as video and audio, and (3) requiring the retrieval of complex, often noisy or conflicting multimodal evidence during web search. We evaluate diverse search agents powered by ten models, including strong closed-source models (e.g., GPT-5.4-mini, Gemini 3/3.1 Flash/Pro) and open-weight models (Qwen3-4B/30B/235B), across three search settings (no search, native search, and agentic search). Our results show that MERRIN is highly challenging: the average accuracy across all agents is 22.3%, with the best-performing agent reaching only 40.1%. We further observe that while stronger agents like Gemini Deep Research achieve higher performance, gains are modest due to over-exploration; they take more steps and use more tools, but are often distracted by conflicting or partially relevant web content, leading to incorrect answers. Compared to humans, these agents consume more resources yet achieve lower accuracy, largely due to inefficient source selection and an overreliance on text modalities. These findings highlight the need for search agents capable of robust search and reasoning across diverse modalities in noisy web environments, making MERRIN a valuable testbed for evaluating such capabilities.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI智能体在真实、嘈杂的网络环境中进行多模态证据检索与多跳推理时所面临的评估瓶颈问题。研究背景是，网络知识天然具有多模态（文本、图像、视频、音频）、异构且充满噪声和冲突的特点，而用户向搜索增强型智能体提出的问题往往是定义模糊、需要多跳推理的。现有评估基准存在明显不足：许多基准在查询中包含了明确的模态提示（如“在以下图片中…”），这与真实用户提问方式不符；它们涵盖的模态通常局限于文本和图像，忽略了视频和音频等未被充分探索的模态；此外，现有研究主要关注纯文本环境下的噪声，在多模态设置中如何反映网络证据的嘈杂、冲突特性仍探索不足。

因此，本文的核心是提出并构建一个名为MERRIN的新基准，以更真实、更具挑战性地评估搜索增强型智能体。该基准旨在解决三个关键问题：1）要求智能体处理不含显式模态提示的自然语言查询，自主推断所需模态；2）纳入视频和音频等未被充分探索的模态，扩展多模态推理的评估范围；3）模拟真实网络搜索的复杂性，要求智能体从嘈杂、不完整甚至相互冲突的多模态证据中进行检索和推理。通过这一基准，论文揭示了当前先进智能体在此类任务上的性能局限（平均准确率仅22.3%），并分析了其失败模式（如推理错误、模态错误、检索错误），特别是智能体容易过度探索、被无关或冲突内容干扰、过度依赖文本模态等问题，从而为未来开发能在复杂网络环境中进行稳健搜索和跨模态推理的智能体指明了方向。

### Q2: 有哪些相关研究？

相关研究主要可分为两类：**多模态搜索评测基准**和**网络噪声下的推理评测基准**。

在多模态搜索评测方面，先前工作（如多模态检索增强评估基准）通常为搜索智能体提供多模态输入或明确的模态提示（例如指定检索图像或文本），这限制了评估智能体自主识别和选择合适模态（如音频、视频）的能力。此外，这些基准往往只涵盖文本和图像等有限模态，忽略了视频和音频等现实查询中常见的模态。本文提出的MERRIN基准则使用不含显式模态提示的自然语言查询，并纳入视频、音频等未被充分探索的模态，要求智能体在更广泛的模态范围内进行多跳推理。

在网络噪声下的推理评测方面，已有文本领域研究表明，模糊、冲突和不完整的多源信息会显著降低模型性能。多模态场景下的相关研究虽探讨了类似挑战，但大多基于合成噪声或在精心构建的多模态语料库中预设冲突，其噪声多样性和真实性不及开放网络环境。另有一些面向开放网络环境的搜索增强智能体基准，但未明确分析网络噪声如何影响推理或智能体的应对策略，且通常仅关注文本和图像等有限模态。相比之下，MERRIN基准明确引入了真实网络噪声，并要求智能体在包含视频、音频的多样模态中进行推理，更贴近实际网络环境的复杂性和异构性。

### Q3: 论文如何解决这个问题？

该论文通过构建一个名为MERRIN的基准测试来解决问题，其核心方法是创建一个模拟真实网络噪声环境的多模态证据检索与推理评估框架。整体架构设计围绕三个关键方面展开：首先，使用自然语言查询而不提供明确的模态提示，迫使智能体自主判断所需的信息类型；其次，纳入视频、音频等未被充分探索的模态，扩展了多模态推理的复杂性；最后，要求智能体在嘈杂的网络搜索结果中检索复杂、可能冲突的多模态证据，并进行多跳推理。

主要模块包括：1）数据收集与标注模块，基于真实网络环境构建包含文本、图像、视频、音频等多种模态且带有噪声和冲突信息的数据集；2）评估模块，设计了三种搜索设置（无搜索、原生搜索、智能体搜索）来测试不同智能体的性能；3）智能体测试平台，集成了十种模型，包括闭源模型（如GPT-5.4-mini、Gemini系列）和开源模型（如Qwen3系列），以全面评估现有技术的局限性。

创新点在于：MERRIN首次系统性地将未指定模态的自然查询、多样化模态（尤其是视频和音频）以及真实网络噪声（如冲突证据）整合到一个基准测试中，突出了现有智能体在模态识别、证据筛选和跨模态推理方面的不足。实验发现，即使性能最佳的智能体也仅达到40.1%的准确率，且普遍存在过度探索、依赖文本模态而忽略其他模态、以及易受冲突信息干扰等问题，从而揭示了多模态搜索智能体在噪声环境中实现稳健推理的关键挑战。

### Q4: 论文做了哪些实验？

实验评估了十种模型驱动的搜索增强智能体，包括闭源模型（如GPT-5.4-Nano/Mini、Gemini 3/3.1系列及Gemini Deep Research Agent）和开源模型（Qwen3的4B、30B、235B版本）。实验在三种搜索设置下进行：无搜索（仅依赖参数知识）、原生搜索（使用模型内置搜索工具）和智能体搜索（通过smolagents框架配备多模态工具）。数据集为MERRIN基准，包含需要多跳推理和跨模态证据检索的自然语言查询，并涉及文本、图像、视频和音频等模态。

主要结果如下：所有智能体的平均准确率仅为22.3%，最佳表现（Gemini-3.1-Pro结合智能体搜索）达到40.1%。无搜索设置下平均准确率为17.3%，表明仅凭参数知识无法解决任务。原生搜索提升至23.1%，智能体搜索进一步提升至33.7%，凸显了灵活多模态检索的重要性。关键数据指标包括：Gemini Deep Research Agent在原生搜索下准确率最高（33.3%）；智能体搜索中，闭源模型平均准确率比开源模型（Qwen系列）高约16.4个百分点；检索证据中文本占比高达87.7%，与数据集中31.4%的文本分布形成显著偏差。

实验还分析了搜索行为：搜索查询数量和访问网页数与准确率无强相关，甚至出现过度探索现象（如Gemini Deep Research在33.1%的问题上超时）。错误分析表明，多步检索中第一步失败占比57.7%，且智能体在需要同时处理非文本模态推理和答案生成时性能大幅下降（准确率28.0%）。这些结果揭示了当前智能体在噪声网络环境中进行跨模态检索和推理的挑战。

### Q5: 有什么可以进一步探索的点？

基于论文分析，可以进一步探索的点主要集中在以下几个方面：

**1. 提升多模态检索与推理能力**：当前智能体严重依赖文本模态（如Agentic系统文本使用率达87%），对视频、音频等模态利用不足。未来研究可探索更高效的多模态融合与检索机制，例如开发能自动识别查询隐含模态需求、并平衡利用不同模态证据的模型。论文中视频工具的实验表明，扩展模态访问能带来显著性能提升（平均5.7%），这提示了增强跨模态理解与对齐的重要性。

**2. 优化搜索策略与抗噪声能力**：智能体存在“过度探索”问题，搜索效率低下（URL精确率仅1.8%），且易受冲突或部分相关信息的干扰。未来可研究更智能的搜索规划与证据评估机制，例如模仿人类高效筛选来源的能力（人类URL精确率达38.1%），或引入对抗性训练以提升在噪声环境中的鲁棒性。论文中“黄金证据”实验表明，即使提供完美证据，智能体仍可能因依赖表面信息而推理失败，因此需加强深度内容分析与去芜存菁的能力。

**3. 突破推理瓶颈与时间利用效率**：即使提供黄金证据，最佳性能也仅达47.7%，说明推理能力是更紧迫的瓶颈。智能体在额外时间下性能提升有限（Agentic系统仅提升6.1%），而人类则可利用时间解决更复杂问题（提升12.2%）。未来可探索更高效的思维链机制、迭代细化策略，以及如何减少冗余计算，使智能体能像人类一样“深思熟虑”而非“盲目徘徊”。结合人类错误分析（错误多源于细节提取偏差），需重点提升细粒度多模态信息提取的精确性。

**4. 构建更全面的评估体系与任务设计**：MERRIN揭示了现有智能体与人类的巨大差距，未来可在此基础上设计更具挑战性的子任务，如冲突证据消解、长视频关键帧定位、跨模态事实核查等，以推动搜索增强智能体向更实用、鲁棒的方向发展。

### Q6: 总结一下论文的主要内容

该论文提出了MERRIN基准测试，旨在评估AI智能体在嘈杂网络环境中的多模态证据检索与推理能力。核心问题是解决现实网络搜索中查询模糊多跳、证据多模态且常含噪声或冲突的挑战。方法上，MERRIN通过人工标注构建数据集，其特点包括使用无明确模态提示的自然语言查询、纳入视频音频等未充分探索的模态，并要求在搜索中处理复杂噪声证据。论文评估了十种模型驱动的搜索智能体，涵盖闭源与开源模型，在三种搜索设置下的表现。主要结论显示，MERRIN极具挑战性：所有智能体平均准确率仅22.3%，最优配置仅达40.1%。智能体表现远逊于人类，存在过度探索、模态依赖文本、资源效率低等问题，突显了开发能在嘈杂多模态环境中稳健搜索推理的智能体的迫切需求，使MERRIN成为评估相关能力的宝贵测试平台。
