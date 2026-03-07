---
title: "ArgLLM-App: An Interactive System for Argumentative Reasoning with Large Language Models"
authors:
  - "Adam Dejl"
  - "Deniz Gorur"
  - "Francesca Toni"
date: "2026-02-27"
arxiv_id: "2602.24172"
arxiv_url: "https://arxiv.org/abs/2602.24172"
pdf_url: "https://arxiv.org/pdf/2602.24172v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Human-Agent Interaction"
relevance_score: 5.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Human-Agent Interaction"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "ArgLLM (Argumentative LLMs), QBAF (Quantitative Bipolar Argumentation Frameworks)"
  primary_benchmark: "N/A"
---

# ArgLLM-App: An Interactive System for Argumentative Reasoning with Large Language Models

## 原始摘要

Argumentative LLMs (ArgLLMs) are an existing approach leveraging Large Language Models (LLMs) and computational argumentation for decision-making, with the aim of making the resulting decisions faithfully explainable to and contestable by humans. Here we propose a web-based system implementing ArgLLM-empowered agents for binary tasks. ArgLLM-App supports visualisation of the produced explanations and interaction with human users, allowing them to identify and contest any mistakes in the system's reasoning. It is highly modular and enables drawing information from trusted external sources. ArgLLM-App is publicly available at https://argllm.app, with a video demonstration at https://youtu.be/vzwlGOr0sPM.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLMs）在决策任务中缺乏可靠的可解释性和可争议性的问题。随着LLMs在各类场景中展现出强大的零样本知识应用能力，它们被广泛视为决策支持的有力工具。然而，现有LLMs通常作为“黑箱”运作，其输出过程不透明，当模型犯错时，用户既难以理解其推理依据，也无法有效地对错误结论提出质疑或修正，这限制了其在需要高可靠性和透明度的关键决策场景中的应用。

针对这一不足，论文基于已有的“论证性大型语言模型”（ArgLLMs）框架，提出并实现了一个名为ArgLLM-App的交互式系统。ArgLLMs的核心思想是利用LLMs构建定量的双极论证框架（QBAFs），并通过形式化推理（如渐进语义）来支持决策，从而生成结构化的、可解释的论证过程。本文要解决的核心问题是如何将这一理论框架转化为一个实用、灵活且支持人机交互的系统，以服务于任意的二元决策任务（如声明验证）。具体而言，ArgLLM-App不仅可视化展示生成的论证图谱（QBAF）和解释，还允许用户通过直接调整论证图谱（如修改论证的置信度、添加攻击者或支持者）或通过聊天界面间接交互，来识别并挑战系统推理中的任何错误。此外，系统高度模块化，支持集成外部可信来源（如PDF文档）以增强论证生成的信息基础，体现了检索增强生成（RAG）的理念。因此，本文实质上是为弥补LLMs在可解释性与可交互性方面的缺陷，提供了一个端到端的系统解决方案。

### Q2: 有哪些相关研究？

本文的研究背景主要涉及基于大语言模型的可解释性决策系统、计算论证理论以及人机交互界面设计。相关工作可归纳为以下几类：

**方法类**：核心基础是计算论证中的定量双极论证框架（QBAF），该框架将论证建模为带有攻击与支持关系的图结构，并利用渐进语义（如DF-QuAD）计算论证强度。ArgLLM-App直接继承了ArgLLMs的方法，将LLM与QBAF结合生成可解释的决策树。与早期基于规则或符号的论证系统相比，本文利用LLM自动生成论证内容与置信度，提升了灵活性与可扩展性。

**应用类**：现有研究已探索将论证框架用于司法、医疗等领域的决策支持，但多依赖结构化知识库。本文的系统专注于二元分类任务，并通过模块化设计支持接入外部可信数据源，增强了实用性。与纯文本生成的解释方法不同，本文强调结构化、可视化的论证图输出，使推理过程更透明。

**评测与交互类**：以往可解释AI系统多侧重于静态解释，而ArgLLM-App突出了交互性，允许用户对论证图中的错误进行质疑与修正。这与近期“人在回路”的可解释AI研究趋势一致，但本文通过限定论证树深度与广度（深度≤2）避免了信息过载，在可解释性与用户体验间做了权衡。

综上，本文在ArgLLMs的理论基础上，重点贡献了一个支持可视化、交互与模块化的实际应用系统，推动了可解释论证从理论方法向实用工具的转化。

### Q3: 论文如何解决这个问题？

论文通过构建一个高度模块化、可交互的Web系统来解决基于论证的决策可解释性与可争议性问题。其核心方法是结合大型语言模型（LLMs）与计算论证理论，形成一个名为ArgLLM-App的交互式平台。

整体框架采用基于论证的LLM（ArgLLM）智能体来处理二元决策任务。系统主要模块包括：1）**论证生成模块**：利用LLM根据任务和外部知识（如用户上传的PDF文档）自动生成支持或攻击特定主张的论证节点，构建起一个形式化的定量双极论证框架（QBAF）。2）**论证评估与可视化模块**：系统集成多种渐进语义（如DF-QuAD、Euler-based和Quadratic Energy），根据用户配置的深度（1或2层）和广度（每论证最多4个支持者和4个攻击者）计算论证的强度，并以图形化界面直观展示论证网络及其置信度。3）**高度交互的修正模块**：这是系统的关键创新点。用户不仅是被动接收解释，还能主动干预系统的推理过程。具体技术包括：通过滑块直接调整证据或论证的“基础置信度”；使用“添加”按钮为已有论证引入新的支持者或攻击者；在聊天中提供额外信息，系统能自动将其转化为相关论证的攻防节点。

其架构设计实现了从“静态解释”到“动态协作论证”的范式转变。主要创新在于将LLM的生成能力、计算论证的形式化评估与人的直觉判断置于一个闭环交互系统中。用户可以通过多种直观方式（调整参数、修改置信度、增删论证节点、补充文档或文本信息）来识别并质疑系统推理中的任何错误，从而使最终决策不仅是“可解释的”，更是“可辩论与可修正的”，显著增强了人机协作决策的可靠性与信任度。

### Q4: 论文做了哪些实验？

论文通过ArgLLM-App系统进行了交互式论证推理实验。实验设置上，系统允许用户自定义多项参数，包括论证框架的深度（1或2层）、广度（每个论证最多4个支持者和4个攻击者）以及渐进语义（DF-QuAD、基于欧拉和二次能量三种选择）。系统支持用户通过滑块调整证据的基础置信度、手动添加支持者或攻击者，并可通过上传PDF文档或直接在聊天中提供信息来增强LLM的知识库。

数据集/基准测试方面，论文未明确提及使用特定公开数据集，而是以系统演示和用户交互为核心，通过实际案例（如二进制决策任务）展示功能。对比方法上，ArgLLM-App作为现有ArgLLM方法的实现，重点在于其交互性和模块化设计，而非与传统模型进行量化比较。

主要结果体现在系统功能的实现和可视化上：ArgLLM-App成功生成了可解释的论证结构，允许用户识别和质疑推理中的错误，并支持从外部可信源获取信息。关键数据指标包括可配置的深度（1-2层）、广度（最多4个支持者/攻击者）以及三种渐进语义选项，这些参数共同确保了系统的灵活性和可定制性。系统已公开上线，并通过视频演示展示了其交互能力。

### Q5: 有什么可以进一步探索的点？

该论文提出的ArgLLM-App系统在可解释性人机交互方面具有创新性，但仍存在多方面的局限性，为未来研究提供了丰富的探索空间。首先，系统目前仅支持深度为2的论证图，限制了复杂推理场景的表达能力；未来可研究动态深度控制机制，在保证用户认知负荷可控的前提下，支持更深层次的论证结构。其次，系统依赖单一LLM提供商（OpenAI）且仅使用单个模型，未来可引入多模型协作框架，让不同特长的LLM代理针对子任务进行辩论，提升决策的鲁棒性。此外，当前的检索增强生成（RAG）功能尚未完全集成，若能实现自动从可信外部源发现并提取论据，将大幅提升论证的知识覆盖面。交互层面，系统目前仅支持单用户对单一二元决策的辩论，未来可扩展至多用户协同辩论场景，并支持多决策或开放域问答任务。最后，基础置信度计算方法和文档格式支持（如非PDF文件）的改进，也是提升系统实用性的关键方向。这些扩展不仅将增强系统的普适性，还能推动可解释AI在复杂现实决策中的应用。

### Q6: 总结一下论文的主要内容

该论文提出了一个名为ArgLLM-App的交互式系统，旨在通过结合大型语言模型（LLMs）与计算论证技术，实现可解释且可争议的二元决策任务。系统核心贡献在于将ArgLLM方法具体化为一个高度模块化的网络应用，允许用户可视化论证过程并与之交互，从而提升决策的透明度和可靠性。

论文首先指出LLMs在决策中存在解释性不足和难以纠正错误的局限性，而ArgLLMs通过构建定量双极论证框架（QBAFs）来形式化推理，以生成可解释的决策依据。ArgLLM-App系统实现了基于ArgLLM的智能体，支持用户通过图形界面或聊天接口修改论证框架（如调整论据置信度或添加攻击/支持关系），并能整合外部可信来源（如PDF文档）以增强论证生成。

主要结论是，该系统不仅有效应用于如声明验证等二元任务，还通过交互设计使人类能够识别和挑战推理中的错误，从而推动可信AI的发展。ArgLLM-App的公开可用性进一步促进了该技术在实践中的探索与应用。
