---
title: "NTILC: Neural Tool Invocation via Learned Compression"
authors:
  - "Andrew Krikorian"
  - "Yayuan Li"
  - "Jason J. Corso"
date: "2026-06-04"
arxiv_id: "2606.06566"
arxiv_url: "https://arxiv.org/abs/2606.06566"
pdf_url: "https://arxiv.org/pdf/2606.06566v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "工具调用"
  - "工具选择"
  - "检索增强"
  - "嵌入空间"
  - "函数调用"
  - "上下文节约"
  - "延迟优化"
relevance_score: 9.5
---

# NTILC: Neural Tool Invocation via Learned Compression

## 原始摘要

Agentic tool-calling language models depend on large registries of callable APIs, functions, and local actions. Placing full tool specifications directly in the prompt incurs a cost that scales linearly with the size of the tool registry, rapidly consuming the context budget. As the registry grows, this leads to higher latency and degrades selection accuracy, particularly due to interference from irrelevant tools. We overcome these limitations by introducing NTILC, a neural tool selection and invocation framework that replaces in-context registry look-up with learned latent retrieval. NTILC maps both user intent and tool specifications into a shared embedding space, enabling tool selection via external retrieval rather than in-context lookup. The language model is conditioned only on the selected tool schema, allowing for precise, constrained argument generation. Central to our approach is a signature-aware composite objective, which augments semantic similarity with constraints derived from tool signatures (e.g., argument schema, type compatibility, and return types). By combining Circle Loss with a Functional Margin Loss, the model enforces separation between tools that are semantically similar but incompatible under their execution signatures. We evaluate NTILC on public tool-selection and function-calling datasets and report context token usage, retrieval accuracy, and selection latency metrics. Across these settings, NTILC reduces context window consumption by over 95% and inference latency by up to 74% compared to long-context ICT baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型在智能体工具调用场景中面临的一个核心瓶颈：随着可调用工具注册表规模的线性增长，传统的“上下文内工具调用”（ICT）方法会导致显著的token消耗、推理延迟和准确性下降。研究背景是，现代智能体将LLM作为推理核心，并依赖包含大量API、函数和本地动作的工具注册表。现有方法的不足在于，在每次推理时将所有工具定义直接插入到上下文中，其token成本与工具数量呈O(N)线性关系。当工具注册表很大时（如5000个工具），仅工具描述就需要约60万token，这不仅消耗了宝贵的上下文预算，还因无关工具的干扰导致工具选择准确率下降。本文要解决的核心问题是：如何在不牺牲选择精度的前提下，大幅降低工具调用中的上下文消耗和推理延迟。为此，论文提出了NTILC框架，通过将工具注册表压缩到潜在嵌入空间，并用外部检索替代上下文内查找，将工具选择的上下文消耗从O(N)降至常数级O(1)。同时，为了克服“语义模糊”——即工具描述相似但执行签名不兼容导致的选择错误，NTILC引入了一种签名感知的复合目标函数，通过结合Circle Loss和Functional Margin Loss来强化语义相似性与功能兼容性之间的解耦。

### Q2: 有哪些相关研究？

### 相关研究

论文将相关工作分为三类：

1. **上下文工具调用（ICT）与提示方法**：传统方法在系统提示中直接嵌入完整工具描述，但随工具集扩大，线性消耗上下文窗口、增加延迟及干扰。NTILC 通过将完整注册表从提示中移除来解决此问题。

2. **检索增强工具选择**：为应对大规模工具库，现有方法采用稀疏或密集检索动态获取Top-k候选工具。然而，它们仍将工具文本注入LLM提示，且易受语义相似但功能不兼容的干扰工具影响。NTILC 的突破在于将检索视为决策本身——仅将选定工具的模式暴露给解码器，而非将注册表注入提示。

3. **效率与上下文优化**：近期工作涵盖内存压缩、提示缓存和长上下文模型，虽能缩短提示长度，但未改变上下文工具注册表随工具规模线性增长的本质。NTILC 与之互补，可在减少残余提示开销的同时彻底消除注册表占用。

### Q3: 论文如何解决这个问题？

NTILC通过一个两阶段框架解决了大规模工具注册表导致的上下文开销和选择精度下降问题。核心思路是将工具选择从上下文内检索转换为潜在空间检索。整体框架包括:离线构建工具索引和使用轻量级编码器进行在线检索。主要模块包括:1)编码器模块,使用all-MiniLM-L6-v2骨干网络(22.7M参数)加两层MLP投影头,将文本渲染的工具架构映射到128维L2归一化嵌入空间;2)工具索引模块,离线构建查询无关的向量索引,支持增量更新;3)检索模块,对用户输入先经LLM生成计划块,分解为独立意图后编码为查询向量,通过最近邻搜索检索最匹配工具;4)参数生成模块,利用Outlines库将检索到的工具架构转换为有限状态机约束,确保LLM生成的参数符合工具签名要求。关键技术在于签名感知复合目标函数:将Circle Loss与功能间隔损失结合。Circle Loss实现查询-工具的语义对齐,功能间隔损失则根据工具签名(参数名称、类型、必需字段等)计算兼容性分数作为连续权重,对语义相似但功能不兼容的"硬负样本"施加排斥力,迫使嵌入空间区分这些易混淆的工具。最终将这两个损失加权组合(最优权重λ1=1.0,λ2=2.0)进行训练。这种方法使上下文令牌消耗减少95%以上,推理延迟降低74%。

### Q4: 论文做了哪些实验？

论文在五个公开工具选择和函数调用数据集（ToolBench, API-Bank, BFCL, ToolEyes, MetaTool）上评估了NTILC，工具注册表规模从199到16,464不等。实验设置包括：使用Qwen3-27B进行约束参数生成，对比方法为ICT基线（Qwen3-27B, Ministral 3, Kimi Moonlight, ChatGPT 5, Gemini 2.5 Flash, Claude Sonnet 4.6）。主要结果：NTILC在所有数据集上均将注册表token消耗降为0，生成token大幅减少（如ToolEyes从2303降至115），Top-1准确率保持94%-98%的竞争力，且推理延迟降低高达74%（如ToolEyes从4609ms降至1127ms）。消融实验分离了检索组件，使用BM25、Qwen3-Embedding-8B、仅Circle Loss和NTILC（含Functional Margin Loss）对比。关键数据：NTILC的语义模糊准确率达75.0%，功能错误率降至8.7%，相比仅Circle Loss（70.8%准确率，10.1%错误率）有4.2%的绝对提升，证明Functional Margin Loss在解决语义相似但不兼容工具混淆上的有效性。

### Q5: 有什么可以进一步探索的点？

NTILC的局限性主要体现在工具索引的静态性上：它要求工具注册表预先索引，面对动态变化的工具文档（如状态相关的API）需要频繁重索引，缺乏在线增量更新能力。未来可探索混合检索机制，对静态部分使用预索引，动态部分通过轻量级查询实时抓取签名摘要。另一个可改进点是NTILC仅聚焦于工具选择，没有深入处理参数生成的约束与执行安全性。可以考虑将工具签名中的执行上下文（如权限、副作用标签）纳入检索空间的度量学习，例如在Functional Margin Loss中增加安全约束项。此外，当前相似性度量限于参数名和原始类型，未来可设计更丰富的功能距离度量（如类型继承、嵌套参数结构），以提升对语义模糊子集的区分度。在大规模动态注册表场景下，还可探索检索索引的在线更新机制，结合高效哈希或级联索引减少重索引开销。

### Q6: 总结一下论文的主要内容

NTILC 提出了一种神经工具调用框架，旨在解决大型工具注册表导致的长上下文消耗和选择精度下降的问题。核心贡献在于将工具注册表压缩为嵌入空间，通过外部检索替代上下文内查找，从而将提示令牌消耗从O(N)降至O(1)。方法上，NTILC将用户意图和工具规范映射到共享嵌入空间，并设计了签名感知复合目标函数，结合Circle Loss与Functional Margin Loss，对语义相似但签名兼容性低的工具施加排斥力，解决“语义模糊”问题。主要结论显示，在多个公开数据集上，NTILC相比长上下文基线方法，上下文窗口消耗减少超95%，推理延迟降低高达74%，显著提升了大规模工具注册场景下的效率和准确性。该工作为构建可扩展的智能体工具调用系统提供了新范式。
