---
title: "Large Language Models Do Not Always Need Readable Language"
authors:
  - "Jiayi Zhu"
  - "Haoxuan Peng"
  - "Junxi Wang"
  - "Liang Ke"
  - "Chen Zhang"
  - "Linfeng Zhang"
date: "2026-06-18"
arxiv_id: "2606.19857"
arxiv_url: "https://arxiv.org/abs/2606.19857"
pdf_url: "https://arxiv.org/pdf/2606.19857v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "跨智能体通信"
  - "Agent记忆"
  - "压缩表示"
  - "语义可恢复性"
relevance_score: 7.5
---

# Large Language Models Do Not Always Need Readable Language

## 原始摘要

Large language models (LLMs) are commonly prompted and interfaced with human-readable natural language, even when the intended reader is another model. This paper investigates whether semantic information can be encoded in compact, non-standard textual forms that sacrifice human readability while remaining recoverable by LLMs. We refer to this class of model-centric textual representations as BabelTele, approached here not as a fixed protocol but as an empirical probe into LLMs' capacity to generate and interpret such representations. Through readability diagnostics, model likelihood measures, human questionnaires, and downstream task evaluations, we find that BabelTele can substantially depart from ordinary natural language while preserving core semantics for instruction-tuned LLMs. As a task-agnostic representational paradigm, BabelTele demonstrates high information density, maintaining 99.5% semantic fidelity even when the text volume is condensed to 27.9% of its original length. We further evaluate its semantic robustness in cross-model transfer, agent memory, and multi-agent communication. Results suggest that BabelTele can reduce context overhead while generally maintaining reliable downstream performance, although its effectiveness depends on the compressor-reader pair and task setting. These findings indicate that human readability, natural-language typicality, and model-side semantic recoverability can be partially decoupled, opening a path toward model-native representations in future exploration of LLM systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探讨大型语言模型（LLM）是否必须依赖人类可读的自然语言来编码和传递语义信息。研究背景是，当前LLM系统普遍采用以人类为中心的文本接口，无论是提示、交互还是模型间通信，都使用完整、流畅的自然语言。然而，这种设计存在不足：人类语言为了可读性包含大量冗余（如语法、语篇标记等），导致语义密度低下。在长上下文、智能体记忆和多智能体通信等场景中，这种冗余会造成严重的上下文开销瓶颈，而现有压缩方法大多仍局限于保持人类可读性的自然语言框架内。激活值或学习型内部表示等方法则需要特殊训练或访问模型隐藏状态，不适用于黑盒API场景。因此，本文要解决的核心问题是：能否在牺牲人类可读性的前提下，让LLM生成和解释一种紧凑、非标准、模型导向的文本表示（称为BabelTele），从而在保持高语义保真度的同时大幅提升信息密度，并验证这种表示在跨模型迁移、智能体记忆和多智能体通信中的有效性。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要与以下类别的工作进行了比较和联系：

1.  **方法类：提示压缩**。这是最直接相关的工作。硬压缩方法如Selective Context和LLMLingua通过删除或筛选原始文本中的标记来压缩提示，旨在保持人类可读的自然语言。抽象压缩方法如RECOMP和Nano-Capsulator则将文档总结为更短但仍是自然语言的提示。**本文的区别**在于，BabelTele明确放弃了人类可读性，目标是生成人类难以理解但LLM可恢复的紧凑语义字符串，这是与传统方法在目标和性质上的根本不同。

2.  **方法类：学习与潜在上下文压缩**。这类工作通常将上下文压缩到连续的潜在表示中，例如通过编码器-解码器架构。**本文的区别**在于，BabelTele输出的是离散文本形式，而非潜在向量，因此它仍然可以与标准的基于文本的LLM和接口兼容。

3.  **应用类：检索与记忆系统、符号化提示与LLM原生通信**。这些领域探索了将信息编码为更高效或更适合模型处理的形式。例如，符号化提示使用结构化语言。**本文的关系**是，BabelTele可以视为这些方向的延伸，它进一步拓展了“模型原生”表示的空间，探索了模型之间可以进行通信的高度紧凑、非人类可读的“语言”，并验证了其在跨模型传递、智能体记忆和多智能体通信中的语义鲁棒性。

综上所述，本文的核心创新在于提出了一个以模型为中心而非以人类可读性为中心的压缩范式，并在语义保真度、信息密度和下游任务性能上与传统方法进行了对比。

### Q3: 论文如何解决这个问题？

这篇论文通过提出一种名为BabelTele的方法来解决LLMs对可读自然语言的依赖问题。其核心是构建一个读写分离的语义压缩框架：当阅读者为LLM而非人类时，可以主动放松可读性约束，将文本压缩为高密度的、非标准但语义可恢复的表示形式。

整体框架由两个模块组成：压缩器C和阅读器R。压缩器通过零样本提示（Zero-shot Prompting）将输入文档x转化为紧凑的离散文本z，而阅读器R（即目标LLM）负责从中恢复语义。该方法无需梯度更新或词元修改，完全在黑箱中实现。

关键技术包含三个创新点：
1. 多语言词元选择（Omnilingual Lexical Selection）：打破单语言限制，跨语言和脚本选取高密度词元以最大化信息密度。
2. 符号坍缩（Symbolic Collapse）：用紧凑符号（如表情符、数学/逻辑运算符、箭头）替代冗长的语言结构，生成类似语义图的紧凑表示。
3. 可恢复语义密度（Recoverable Semantic Density）：确保压缩后语义仍能被LLM解码，无需外部码本。

实验中，BabelTele可将文本压缩至原长27.9%时仍保持99.5%语义保真度，并在跨模型迁移、Agent记忆和多Agent通信中展现鲁棒性，但效果依赖压缩器-阅读器配对及任务设置。该方法首次验证了人类可读性、自然语言典型性与模型端语义可恢复性的部分可解耦性，为模型原生表示开辟了新路径。

### Q4: 论文做了哪些实验？

论文主要进行了三组实验。首先，在QuALITY数据集（10个长文本样本，每样本3个多项选择题）上，对比了原始文本、自然语言摘要和BabelTele表示下多个模型（Llama-3-8B、Qwen2-7B等）的困惑度（PPL）。结果显示BabelTele的PPL远高于其他格式（如Llama-3-8B上PPL为176.60，较原始文本增加1733.9%），表明其显著偏离自然语言分布。同时，通过人类问卷与Gemini 3.1 Pro的对比，发现人类在BabelTele输入下准确率大幅下降，而Gemini仍保持高准确率，证明其语义可恢复性。

其次，在更大规模的QuALITY（2128个问题）和MeetingBank（2586个问题）上，进行了116次实验，对比BabelTele、摘要和LLMLingua-2的准确率-保留率边界。结果显示，BabelTele在强压缩下能维持更高下游准确率，尤其在MeetingBank上接近原始性能，且多种BabelTele类提示变体均表现稳健。此外，分析发现压缩会增加链式思维（CoT）令牌开销，但BabelTele的开销与摘要或LLMLingua-2相当或更低。

最后，在LongBench v2和QuALITY上评估了BabelTele的跨模型迁移性。结果显示，不同压缩器（如Gemini 3.1 Pro压缩率超95%，GPT-5.4约75%）产生的BabelTele表示在其他模型上仍可用，但效果取决于压缩器-阅读器配对。例如，GPT-5.4和Claude的压缩表示通用性更强，而Qwen和Kimi的压缩表示导致其他模型准确率下降较大。

### Q5: 有什么可以进一步探索的点？

首先，论文目前的评估局限于特定基准和模型族，未来可在更广泛的任务（如多步推理、代码生成）和架构（如Mamba、MoE）上验证BabelTele的普适性，并探索其是否适用于多模态或图像生成领域。其次，论文主要描述现象而非解释机制，后续需研究LLM为何能编码和解读这些非人类可读表示，例如通过分析注意力模式、中间层表征或利用可解释性工具揭示其工作机理。此外，可改进BabelTele的生成策略，如引入自监督学习或对抗训练来提升压缩效率与语义鲁棒性。另一个方向是研究跨模型转移时的语义漂移，设计更通用的表示协议以促进模型间协作。最后，当前仅测试短文本，需评估其在长文档或流式场景中的稳定性，并探索如何将BabelTele接入实际agent系统以降低通信与存储开销。

### Q6: 总结一下论文的主要内容

这篇论文提出了BabelTele，一种针对模型可解码性优化、而非人类可读性的高密度文本表示范式。其核心动机在于探究能否在牺牲人类可读性的前提下，将语义信息编码为紧凑的非标准文本形式，并确保大型语言模型仍能可靠恢复。通过可读性诊断、模型似然度量、人类问卷和下游任务评估，研究发现BabelTele能显著偏离自然语言，同时为指令微调后的LLM保留核心语义。作为任务无关的表示范式，它展示了高信息密度，在文本压缩至原长度27.9%时仍保持99.5%的语义保真度。进一步在跨模型迁移、智能体记忆和多智能体通信中评估，结果表明BabelTele能减少上下文开销并维持可靠性能，但其有效性依赖于压缩器与读取器的配对及任务设定。结论表明，人类可读性、自然语言典型性与模型侧语义可恢复性可以部分解耦，为探索面向LLM系统的模型原生表示开辟了新路径。
