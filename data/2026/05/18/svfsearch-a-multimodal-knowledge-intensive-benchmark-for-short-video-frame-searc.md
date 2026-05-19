---
title: "SVFSearch: A Multimodal Knowledge-Intensive Benchmark for Short-Video Frame Search in the Gaming Vertical Domain"
authors:
  - "Lingtao Mao"
  - "Huangyu Dai"
  - "Xinyu Sun"
  - "Zihan Liang"
  - "Ben Chen"
  - "Chenyi Lei"
  - "Wenwu Ou"
date: "2026-05-18"
arxiv_id: "2605.17946"
arxiv_url: "https://arxiv.org/abs/2605.17946"
pdf_url: "https://arxiv.org/pdf/2605.17946v1"
categories:
  - "cs.AI"
  - "cs.CV"
  - "cs.LG"
tags:
  - "多模态Agent基准"
  - "检索增强生成(RAG)"
  - "短期视频搜索"
  - "游戏知识"
  - "工具使用"
  - "规划-行动-再规划管线"
  - "Agent评估"
  - "多模态大语言模型"
relevance_score: 9.5
---

# SVFSearch: A Multimodal Knowledge-Intensive Benchmark for Short-Video Frame Search in the Gaming Vertical Domain

## 原始摘要

Multimodal large language models are increasingly used as agent backbones that understand multimodal inputs, plan retrieval actions, invoke external tools, and reason over retrieved information. Yet existing benchmarks rarely evaluate this ability in short-video applications, where a paused frame is often visually ambiguous and answering requires vertical, long-tail, and fast-evolving domain knowledge. We introduce SVFSearch, the first open benchmark for short-video frame search in the Chinese gaming domain. SVFSearch contains 5,000 four-choice test examples and 4,198 auxiliary training examples, each centered on a paused game scene from a real short-video clip. To support fair and reproducible evaluation, SVFSearch provides a frozen offline retrieval environment with a game-domain text corpus, a topic-linked image gallery, and text, image, and multimodal retrieval interfaces, avoiding reliance on uncontrolled web search APIs. We evaluate representative paradigms ranging from direct QA and RAG workflow to Plan-Act-Replan agents and learned search models. Results reveal a large gap between model-only answering, practical agentic search, and oracle knowledge: the best open-source direct-QA model reaches 66.4%, the best practical agent achieves 79.1%, and oracle knowledge reaches 95.4%. Further analysis exposes bottlenecks in visual grounding, retrieval quality, evidence-grounded reasoning, and tool-use behavior, including over-search, answer-only shortcuts, and retrieval-induced misleading.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

该论文旨在解决现有基准在短视频帧搜索这一特定但日益普遍的多模态检索场景中的缺失问题。研究背景是，多模态大模型正从被动预测器转变为主动智能体，能够理解多模态输入、规划检索动作并整合外部知识。然而，现有基准测试很少评估模型在短视频应用中的这种能力。现有方法的不足在于：当用户暂停一个短视频帧时，该帧本身往往是视觉模糊的，且答案通常需要垂直、长尾且快速演变的领域知识（如游戏场景识别、角色装备、版本内容等），而现有的百科全书式视觉问答（VQA）和通用多模态搜索基准并未联合处理这种视觉和文本证据的检索。因此，本文要解决的核心问题是：构建第一个面向中文游戏领域、基于真实短视频剪辑的开放式多模态检索基准SVFSearch，以系统评估并揭示从直接问答、RAG流程到复杂智能体范式在暂停帧搜索中的性能差距，并暴露视觉理解、检索质量、证据推理和工具使用行为（如过度搜索、答案捷径和检索误导）中的关键瓶颈。

### Q2: 有哪些相关研究？

相关研究主要分为三类：第一类是**通用多模态搜索基准**，如VisualWebSearch、WikiSeek和MMSearch-R1等，它们评估模型在图像或网页搜索场景中的检索增强能力，但主要面向百科知识或通用视觉内容，缺乏对垂直领域、长尾知识的专门设计。本文的SVFSearch聚焦于短视频暂停帧这一特殊场景，并针对中文游戏领域构建了含5,000测试例的领域知识库，与上述通用基准有本质区别。第二类是**游戏领域视觉问答**，如GQA、GameQA等，它们通常基于静态游戏截图进行单模态推理，不涉及外部知识检索。本文要求模型同时理解游戏画面、用户问题并主动调用文本/图像检索工具获取垂直领域知识，更接近多模态智能体任务。第三类是**检索增强生成方法**，包括RAG工作流、LangGraph智能体和MMSearch-R1等。本文不仅评价了这些范式在游戏帧搜索中的性能（最佳智能体79.1% vs 直接QA 59.9%），还通过错误分析揭示了视觉定位、检索质量、证据推理和工具使用行为（如过度搜索、捷径推理）等瓶颈，而现有基准较少系统性关注此类失败模式。

### Q3: 论文如何解决这个问题？

SVFSearch通过构建一个多模态、知识密集型、可复现的离线基准测试环境来解决短-视频帧搜索问题。其核心方法包括三个阶段的基准构建：首先，以游戏领域核心元素（角色、装备、技能等）为锚点，从网络收集超过26万条结构化知识文本块；其次，通过短-视频检索和MLLM视觉验证，建立43,130个核心元素-图像强视觉关联对；最后，利用8B和32B参数模型生成并筛选出9,198个高质量四选一问答实例。架构上，SVFSearch提供了冻结的离线检索环境，包含文本知识库（45K条目）、主题关联图像集（34K图像）及四种检索接口：基于DINOv3微调的图像检索、BM25词法检索、多模态嵌入检索。关键技术方面，采用聚类感知对比学习训练图像检索编码器，针对同一核心元素的不同视觉变体进行聚类正样本采样。在评估范式上，除了固定RAG流程和Plan-Act-Replan智能体，还创新性地引入了MMSearch-R1-Game模型，通过GRPO训练将搜索与回答内化为生成过程，并设计了针对性的奖励函数（惩罚无搜索的错误回答、奖励有效搜索轨迹）。整体框架支持从直接问答到自主智能体的多层级评估，揭示了模型在视觉定位、检索质量、证据推理和工具使用上的关键瓶颈。

### Q4: 论文做了哪些实验？

论文在SVFSearch基准测试的5000样本测试集上进行了全面实验。实验设置包括五种评估范式的对比：直接QA（无检索工具）、RAG工作流（固定图文检索）、Plan-Act-Replan（PAR）智能体（基于LangGraph的自适应检索）、MMSearch-R1学习型搜索模型（通过RL训练生成工具调用），以及Oracle知识（提供真实知识作为上界）。所有检索增强设置均使用相同的冻结检索资源以确保公平。

主要结果如下：
- **直接QA**：最强开源模型Qwen3.5-27B达66.4%，闭源Gemini-3.1-Pro达77.5%。
- **RAG工作流**：Qwen3.5-27B达69.4%，较直接QA提升3个百分点。
- **PAR智能体**：Qwen3.5-9B达79.1%最佳，超越所有直接QA基线，搜索率100.0%。
- **MMSearch-R1**：任务自适应训练的MS-R1-Game（Qwen3-VL-8B）达64.5%，搜索率68.2%；而原始MS-R1训练几乎消除了工具使用（搜索率0.02%），说明多选设置下仅靠结果奖励会导致模型绕过搜索。
- **Oracle知识上界**：Qwen3.5-27B达95.4%，与最佳实用智能体（79.1%）之间存在16.3个百分点的差距，表明视觉定位、检索质量和证据推理仍是瓶颈。

工具使用分析显示，PAR智能体的表现不取决于工具调用次数，而依赖于多通道协调（图像、文本、BM25、多模态）。Qwen3.5-9B以较少的调用次数（13444次，3.69轮）实现了最佳性能，而Qwen3.5-2B过度搜索（19379次，4.88轮）反而效果较差。

### Q5: 有什么可以进一步探索的点？

该基准聚焦于中文游戏领域的短视频帧搜索，主要在受限的4选1问答和固定检索环境下评估，未能覆盖开放问答、多源信息融合（如标题、OCR、ASR）及动态知识库场景。未来可从三方面拓展：一是引入开放式生成任务，要求模型综合多模态证据输出自由文本答案，避免“捷径”式猜题；二是整合视频侧元数据（如OCR文本、ASR转录）与帧图像联合推理，探索跨模态对齐和冲突消解策略；三是构建可随时间更新的游戏垂直知识库，模拟真实世界中的长尾知识演变。此外，当前检索工具过度使用或误导模型的问题可通过自适应检索规划（如设定检索置信度阈值）或因果推理干预来缓解，并借鉴反事实解释机制提升证据链的鲁棒性。最终，将该范式推广至电商、教育等同样面临视觉歧义与领域知识快速迭代的垂直领域，验证方法的通用性。

### Q6: 总结一下论文的主要内容

SVFSearch提出了一个针对中文游戏领域短视频帧搜索的多模态知识密集型基准测试。该基准包含5000个四选一测试样本和4198个辅助训练样本，每个样本围绕真实短视频中的暂停游戏场景。为支持公平可复现评估，SVFSearch提供了冻结的离线检索环境，包括游戏领域文本语料库、主题链接图像库以及文本、图像和多模态检索接口。实验评估了直接问答、RAG工作流、规划-行动-重新规划智能体以及学习型搜索模型等多种范式，结果显示：最佳开源直接问答模型达到66.4%准确率，最佳实用智能体达到79.1%，而理论最优知识可达95.4%。分析进一步揭示了视觉基础、检索质量、基于证据的推理和工具使用行为等方面的瓶颈，包括过度搜索、仅依赖答案捷径以及检索导致的误导。该工作为研究基于短视频暂停帧的检索增强和智能体多模态搜索提供了实用测试平台。
