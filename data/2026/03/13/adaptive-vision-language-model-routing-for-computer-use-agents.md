---
title: "Adaptive Vision-Language Model Routing for Computer Use Agents"
authors:
  - "Xunzhuo Liu"
  - "Bowei He"
  - "Xue Liu"
  - "Andy Luo"
  - "Haichen Zhang"
  - "Huamin Chen"
date: "2026-03-13"
arxiv_id: "2603.12823"
arxiv_url: "https://arxiv.org/abs/2603.12823"
pdf_url: "https://arxiv.org/pdf/2603.12823v1"
github_url: "https://github.com/vllm-project/semantic-router"
categories:
  - "cs.CL"
  - "cs.CV"
tags:
  - "Agent 架构"
  - "模型路由"
  - "工具使用"
  - "GUI Agent"
  - "效率优化"
  - "多模型系统"
  - "视觉语言模型"
  - "成本-精度权衡"
relevance_score: 8.5
---

# Adaptive Vision-Language Model Routing for Computer Use Agents

## 原始摘要

Computer Use Agents (CUAs) translate natural-language instructions into Graphical User Interface (GUI) actions such as clicks, keystrokes, and scrolls by relying on a Vision-Language Model (VLM) to interpret screenshots and predict grounded tool calls. However, grounding accuracy varies dramatically across VLMs, while current CUA systems typically route every action to a single fixed model regardless of difficulty. We propose \textbf{Adaptive VLM Routing} (AVR), a framework that inserts a lightweight semantic routing layer between the CUA orchestrator and a pool of VLMs. For each tool call, AVR estimates action difficulty from multimodal embeddings, probes a small VLM to measure confidence, and routes the action to the cheapest model whose predicted accuracy satisfies a target reliability threshold. For \textit{warm} agents with memory of prior UI interactions, retrieved context further narrows the capability gap between small and large models, allowing many actions to be handled without escalation. We formalize routing as a cost--accuracy trade-off, derive a threshold-based policy for model selection, and evaluate AVR using ScreenSpot-Pro grounding data together with the OpenClaw agent routing benchmark. Across these settings, AVR projects inference cost reductions of up to 78\% while staying within 2 percentage points of an all-large-model baseline. When combined with the Visual Confused Deputy guardrail, AVR also escalates high-risk actions directly to the strongest available model, unifying efficiency and safety within a single routing framework. Materials are also provided Model, benchmark, and code: https://github.com/vllm-project/semantic-router.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决计算机使用智能体（CUAs）在执行图形用户界面（GUI）操作时，因固定使用单一大型视觉语言模型（VLM）而导致的成本高昂和效率低下的问题。研究背景是，随着CUAs的发展，它们能够通过VLM解析屏幕截图并执行点击、键入等工具调用，从而完成多步骤计算机任务。然而，现有方法通常为每个操作步骤都调用同一个前沿VLM（如GPT-4o），这带来了显著的成本和延迟开销，因为每次迭代都需要处理包含截图和上下文的巨大多模态输入，一个任务可能累积数十万输入令牌，使得大规模部署成本过高。

现有方法的不足主要体现在两个方面：首先，固定使用单一模型忽略了不同GUI操作难度差异巨大这一事实，例如点击大按钮很容易，而定位密集工具栏中的小图标则很困难，这导致大型模型在处理简单操作时资源浪费，而小型模型又可能无法处理复杂操作；其次，研究表明，不同VLM在GUI基础任务上的准确率差异很大，且模型规模的增加并不总是带来性能的线性提升，存在收益递减现象。

因此，本文要解决的核心问题是：如何根据每个具体GUI操作的难度，动态且智能地为CUAs选择最经济且足够准确的VLM，从而在保证任务可靠性的前提下，大幅降低推理成本。为此，论文提出了自适应VLM路由（AVR）框架，通过轻量级的语义路由层，估计操作难度、探测小型模型置信度，并结合智能体的交互记忆上下文，将每个工具调用路由至能满足目标可靠性阈值的最廉价模型，从而实现成本与准确性的权衡优化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为四类：GUI 定位与计算机使用智能体、大语言模型路由、CUA 安全性以及记忆增强智能体。

在 **GUI 定位与计算机使用智能体**方面，相关工作（如 SeeClick、CogAgent、ScreenSpot-Pro 等）专注于通过视觉语言模型理解界面截图并预测操作。它们共同指出，GUI 定位性能在不同模型和应用间差异巨大，且不遵循简单的“越大越好”规律。这直接启发了 AVR 的核心前提：应根据具体操作和界面上下文动态选择模型，而非固定使用单一骨干模型。

在 **大语言模型路由**方面，FrugalGPT、HybridLLM 等方法研究了为降低成本而进行的模型级联或路由，但主要针对纯文本任务（如聊天、问答）。AVR 与这些工作的区别在于，它专门面向多模态的计算机使用操作，其路由决策必须综合考虑语义难度、视觉定位的不确定性、屏幕复杂性和操作风险等多重因素。

在 **CUA 安全性**方面，OS-Harm、CUA-Harm 等工作对智能体操作的有害性和安全失败进行了评估，Visual Confused Deputy 则提出了基于嵌入的护栏来检测风险操作。AVR 的不同之处在于，它将安全信号集成到路由决策本身中，使高风险操作能自动升级到更强的模型进行处理，而非仅仅作为一个事后过滤器。

在 **记忆增强智能体**方面，MemoryBank 等代表性工作研究如何利用记忆来提高任务完成度或长期一致性。AVR 对记忆的利用方式不同：其主要目的不是提升单一模型的最终答案质量，而是利用检索到的上下文来缩小大小模型之间的能力差距，从而让更多操作可以由更便宜的模型可靠处理，即将记忆用作一种成本感知的模型选择机制。

### Q3: 论文如何解决这个问题？

论文通过提出自适应视觉语言模型路由（AVR）框架来解决计算机使用代理（CUA）中固定使用单一VLM导致效率与准确性无法平衡的问题。其核心方法是**在CUA编排器与VLM池之间插入一个轻量级语义路由层**，根据每个工具调用的预估难度和小模型置信度，动态选择成本最低且能满足目标可靠性阈值的模型执行动作。

**整体框架与主要模块**：AVR作为透明代理运行，包含三个核心组件。1) **多模态嵌入器**：使用紧凑的模型（120M参数）将动作描述的文本和以预测坐标为中心的屏幕截图裁剪区域嵌入到共享的384维空间。2) **语义路由器**：这是决策中枢，它首先通过嵌入向量与预定义的难度知识库（包含易、难UI元素的原型嵌入）进行相似度比较，从视觉复杂度和语义复杂度两个通道计算出保守的难度估计值。然后，对于非简单动作，它会**探测小型VLM（如7B参数）**，通过计算输出令牌的平均对数概率来获得归一化置信度。3) **记忆存储**：针对“热”代理（有历史交互记忆），通过向量相似性搜索检索相关记忆（如成功点击目标、工具栏布局）并注入到小模型的提示中，显著提升其置信度。

**关键技术流程与创新点**：路由决策遵循一个流程图。首先进行**安全检查**，如果视觉混淆副手护栏识别为高风险动作，则直接升级到最大模型（如72B）并启用护栏验证。对于安全动作，则依据难度分类：简单动作直接路由至小模型；中等及以上难度动作则触发对小模型的置信度探测。路由决策最终结合了**难度自适应的置信度阈值**：对于易、中、难动作，分别设置由低到高的阈值，仅当小模型置信度达到或超过该阈值时，才使用小模型，否则升级到大模型。

**核心创新**体现在三方面：1) **分层路由策略**：形成了成本与能力递增的三层路由（小模型、大模型、大模型+护栏），实现了效率与安全的统一。2) **难度与置信度双重驱动**：利用轻量级嵌入进行难度先验估计，再通过实际探测小模型获得精确置信度，使路由决策既高效又可靠。3) **利用记忆缩小能力差距**：创新性地发现记忆注入对小模型的性能提升远大于大模型，使得“热”代理能更多地将动作保留在低成本小模型上，形成“越用越省”的良性循环。实验表明，该框架能在保持与全大模型基线精度相差2个百分点以内的同时，将推理成本降低高达78%。

### Q4: 论文做了哪些实验？

论文的实验主要基于三个来源的证据进行分析和评估。实验设置围绕提出的自适应视觉语言模型路由（AVR）框架，旨在通过轻量级语义路由层，根据动作难度和模型置信度，将计算机使用代理（CUA）的工具调用动态路由到不同规模的VLM池中，以权衡成本与准确性。

数据集和基准测试方面，主要使用了ScreenSpot-Pro进行VLM的GUI grounding准确性评估，以及OpenClaw代理基准测试进行基于置信度的路由验证。ScreenSpot-Pro包含26个专业应用程序，评估元素级坐标预测准确性（预测坐标落入目标边界框内即为正确）。OpenClaw基准测试则包含5个代表性文本代理任务（共20个LLM轮次），用于分析置信度分布和成本结构。

对比方法包括固定使用单一大型模型（如Qwen2.5-VL-72B）的基线，以及AVR在不同场景下的路由策略：无记忆的“冷”路由、有记忆的“暖”路由，以及结合难度分类的“暖”路由。实验还整合了Visual Confused Deputy安全护栏，用于检测高风险动作。

主要结果和关键数据指标如下：在ScreenSpot-Pro上，不同模型的grounding准确率差异显著，例如GPT-4o（约1.8T参数）准确率仅0.8%，而专用模型OS-Atlas-7B（7B参数）达到18.9%。在Qwen2.5-VL系列中，模型从3B扩展到72B（参数增加24倍），准确率从24.2%提升至43.6%（仅1.8倍），表明规模收益递减。基于OpenClaw的投影分析显示，AVR在CUA场景中，冷路由（35%动作升级到72B模型）可实现52%的成本节约，有效准确率42.1%（较全72B基线的43.6%低1.5个百分点）；暖路由（15%升级）节约70%，准确率41.3%；结合难度分类的暖路由（10%升级）节约高达78%，准确率42.8%（仅比基线低0.8个百分点）。安全方面，Visual Confused Deputy护栏在ScreenSpot-Pro上达到F1分数0.889（仅图像）和0.915（图像+文本融合）。实验表明，记忆注入能显著提升小模型置信度（如OpenClaw中7B模型平均置信度从0.83升至0.96），减少升级需求，从而在文本任务中实现高达86%的成本节约且无质量下降，这为CUA场景中的部分模型均衡化提供了依据。

### Q5: 有什么可以进一步探索的点？

本文提出的自适应路由框架在效率和安全性方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，当前的成本节约主要基于数据组合的“预测”而非端到端实测，未来需要在OSWorld等真实交互环境中进行验证，以确认其在实际部署中的表现。其次，对于超短任务（如仅含2-3个动作），探测开销可能抵消收益，因此需研究更轻量的探测机制或动态跳过策略。此外，记忆冷启动问题限制了初期效能，未来可探索利用应用UI文档或少量示范动作进行预暖启动，减少对人工标注的依赖。  

从方法改进角度看，当前的难度分类仍依赖启发式信号，未来可尝试基于智能体交互轨迹进行端到端的路由策略学习，使模型能更精准地评估动作复杂性与风险。同时，可扩展至更大规模的异构模型池（如三层级3B/7B/72B），并综合考虑延迟、成本与安全的联合优化。另一个有趣的方向是探索截图token的压缩或选择性编码技术，以降低视觉输入的固定开销，进一步提升路由效率。最后，将AVR与更复杂的多模态推理框架结合，使其能适应动态变化的界面条件与用户意图，也是值得探索的前沿方向。

### Q6: 总结一下论文的主要内容

本文针对计算机使用代理（CUAs）中视觉语言模型（VLM）调用成本高昂且性能不稳定的问题，提出了自适应VLM路由（AVR）框架。核心问题是：现有CUA系统通常为所有交互步骤固定使用单一大型VLM，导致推理成本高，且不同难度任务与模型能力不匹配。AVR通过在CUA编排器与VLM池之间插入轻量级语义路由层来解决该问题。其方法主要包括：基于多模态嵌入的动作难度分类、通过小型VLM置信度探测进行路由决策，以及利用记忆（历史交互上下文）增强小型模型能力以减少向大型模型的升级。实验表明，AVR在ScreenSpot-Pro和OpenClaw基准测试中，能在保持与全大型模型基线准确率差距2个百分点以内的前提下，将推理成本降低52%（冷启动）至78%（热启动）。此外，AVR可与Visual Confused Deputy安全护栏结合，将高风险动作直接路由至最强模型，统一了效率与安全。该工作将CUA推理重新定义为动态资源分配问题，为构建高效可靠的具身智能体提供了重要框架。
