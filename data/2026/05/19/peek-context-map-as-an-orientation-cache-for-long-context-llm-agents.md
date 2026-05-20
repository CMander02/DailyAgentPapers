---
title: "PEEK: Context Map as an Orientation Cache for Long-Context LLM Agents"
authors:
  - "Zhuohan Gu"
  - "Qizheng Zhang"
  - "Omar Khattab"
  - "Samuel Madden"
date: "2026-05-19"
arxiv_id: "2605.19932"
arxiv_url: "https://arxiv.org/abs/2605.19932"
pdf_url: "https://arxiv.org/pdf/2605.19932v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "long-context LLM agents"
  - "context map"
  - "orientation cache"
  - "agent memory"
  - "code agent"
  - "tool use"
  - "efficiency"
  - "architecture innovation"
relevance_score: 9.5
---

# PEEK: Context Map as an Orientation Cache for Long-Context LLM Agents

## 原始摘要

Large language model (LLM) agents increasingly operate over long and recurring external contexts, like document corpora and code repositories. Across invocations, existing approaches preserve either the agent's trajectory, passive access to raw material, or task-level strategies. None of them preserves what we argue is most needed for repeated same-context workloads: reusable orientation knowledge (e.g., what the context contains, how it is organized, and which entities, constants, and schemas have historically been useful) about the recurring context itself. We introduce PEEK, a system that caches and maintains this orientation knowledge as a context map: a small, constant-sized artifact in the agent's prompt that gives it a persistent peek into the external context. The map is maintained by a programmable cache policy with three modules: a Distiller that extracts transferable knowledge from inference-time signals, a Cartographer that translates it into structured edits, and a priority-based Evictor that enforces a fixed token budget. On long-context reasoning and information aggregation, PEEK improves over strong baselines by 6.3-34.0% while using 93-145 fewer iterations and incurring 1.7-5.8x lower cost than the state-of-the-art prompt-learning framework, ACE. On context learning, PEEK improves solving rate and rubric accuracy by 6.0-14.0% and 7.8-12.1%, respectively, at 1.4x lower cost than ACE. These gains generalize across LMs and agent architectures, including OpenAI Codex, a production-grade coding agent. Together, these results show that a context map helps long-context LLM agents interact with recurring external contexts more accurately and efficiently.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在处理重复性长外部上下文（如文档库、代码仓库）时，缺乏可复用的“方向性知识”的问题。现有方法虽然各有侧重，但都存在不足：直接使用长上下文窗口成本高昂且效率低；检索增强生成（RAG）和上下文卸载仅提供对原始材料的被动访问，不保留关于上下文本身的结构化知识；提示学习（Prompt Learning）则主要积累任务级策略，而非关于重复性外部上下文的可复用知识。这些方法都未能保留核心的“方向性知识”——即一个人类分析师在多次阅读语料后会记住的内容，例如语料包含什么、如何组织、哪些实体和模式曾被证明有用等。本文提出的核心问题是：能否在智能体的系统提示中维护一个固定大小的“上下文地图”，使其能够持续缓存并更新这类可复用的方向性知识，从而帮助智能体更准确、更高效地理解和利用大型外部上下文，避免每次交互都从头探索或依赖冗长的历史轨迹。简单来说，论文试图解决当前LLM智能体在重复性长上下文工作中缺乏一种持久、结构化、可管理的上下文感知缓存机制的问题。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕大语言模型代理的上下文管理方法，可分为以下几类：

**方法类**：相关研究包括提示学习（prompt learning）、代理技能（agent skills）、计划缓存（agentic plan caching）和语义缓存（semantic caching），这些方法主动维护与任务相关的状态（如策略、计划或答案）。本文与之区别在于，PEEK专注于维护关于**外部上下文本身**的重用性方向知识，而非任务执行状态。

**被动状态类**：包括共享聊天（shared chat）和历史压缩（history compaction），它们被动地携带或压缩代理执行记录以维持当前任务。RAG（检索增强生成）、上下文卸载（context offloading）和MemAgent等被动外部上下文方法则通过检索、外化或压缩来处理外部上下文。PEEK的关键区别在于主动维护一个常驻提示的小型上下文图，捕捉外部上下文的结构、实体和模式，而非被动访问或压缩原始材料。

**评测类**：与ACE等提示学习框架对比，PEEK在长上下文推理和信息聚合任务上提升6.3-34.0%，使用迭代次数减少93-145次，成本降低1.7-5.8倍；在上下文学习上，解决率提升6.0-14.0%，评分准确率提升7.8-12.1%，成本仅为ACE的1.4倍。这些结果证明了主动维护上下文图的价值。

### Q3: 论文如何解决这个问题？

PEEK通过构建和维护一个上下文地图（context map）来解决长上下文LLM代理在重复性外部上下文（如文档库、代码仓库）中交互效率低下的问题。该地图是一个常驻代理提示中的小型、固定大小的记忆神器，提供对上下文的持久“一瞥”。

核心方法包含两个耦合机制：1）**恒定的上下文地图**，位于系统提示中，存储关键方向知识（如关键实体、常量、结构和规划路径），分为多个结构化部分（默认两核心部分：上下文路线图提供导航索引，上下文理解提供高层描述；可选部分包括领域常量、可复用结果和解析模式）。地图完全通过交互自动生成，无需预填充。2）**可编程的缓存管理策略**，由三个模块组成，在每次查询后更新地图：

- **Distiller（蒸馏器）**：分析执行轨迹（推理步骤、工具调用、观察），生成诊断（识别哪些工作是面向上下文的，哪些是任务特定的以及卡住或成功之处）、为现有地图条目打标签（有用/有害/中性/过时）、识别可迁移的缓存候选（仅保留可复用的上下文知识，过滤掉任务特定规则）。它不依赖最终答案，仅靠执行信号。
- **Cartographer（制图师）**：将蒸馏器的输出转化为结构化编辑操作（添加、删除或替换），利用地图中每项的稳定ID保持更新局部性和可追踪性，并去重以最小化编辑集。
- **Evictor（驱逐器）**：基于优先级实施硬性令牌预算。如果地图超限，按蒸馏器累计分数从低到高驱逐条目，分数相同时先移除旧条目；且遵循部分价值层级（先驱逐解析模式、可复用结果，最后保护核心两个部分）。

地图更新仅在初始查询（m≤n）执行，完成蒸馏和压缩后即可冻结，后续仅复用。该方法在长上下文推理和上下文学习中比基线提升显著，同时降低成本和迭代次数，并泛化到多种模型和Agent架构。

### Q4: 论文做了哪些实验？

论文在两类长上下文任务上进行了实验：**(1) 长上下文推理与信息聚合**，使用 **OOLONG 基准测试**的三个最困难子集 (trec_coarse, agnews, yahoo)，采用分数指标 (0.75^{|y-ŷ|}) 和精确匹配；**(2) 上下文学习**，使用 **CL-bench 基准测试**，报告解决率（粗粒度）和评分标准准确率（细粒度）。基础模型为 GPT-5-mini，运行在 RLM 代理上。

对比方法包括: 基础 RLM、RLM + Shared Chat、RLM + RAG (使用 text-embedding-3-small)、RLM + Compaction Agent (MemAgent)、以及当前最先进的提示学习框架 RLM + ACE。

**主要结果**：PEEK 在所有指标上均优于基线。在 OOLONG 上，PEEK 比 ACE 提高 7.8-15.0%，比基础 RLM 提高 22.9-34.0%（具体：trec_coarse 58.1 比 30.3，agnews 69.4 比 46.5，yahoo 57.0 比 23.0）。在 CL-bench 上，PEEK 比 ACE 提高 6.0% 解决率和 9.9% 评分准确率。PEEK 迭代次数比 ACE 少 93-145 次，成本低 1.7-5.8 倍。此外，PEEK 在替换模型（GPT-5.5、Qwen3-Coder-Next-FP8）和代理架构（OpenAI Codex）时仍保持性能提升。

### Q5: 有什么可以进一步探索的点？

PEEK的“上下文地图”有效性高度依赖交互过程中可提取的可重用知识量，若代理与上下文的交互仅产生任务特定信号而非通用知识（如频繁变化的临时实体或低信息量日志），缓存的价值会显著下降。未来可探索混合缓存策略，动态权衡任务独立知识（如文档结构）与任务相关信号（如最近查询的实体）的比例，以适应不同交互模式。此外，当前设计仅针对单一外部上下文的重复使用，未考虑多上下文切换或动态更新的场景（如实时API返回结果）。可扩展其框架至多层级地图（如全局结构+局部热点），并引入增量更新机制，以支持流式数据或知识库的持续演化。另一个方向是结合分层蒸馏（粗粒度结构+细粒度实体频率），以更高效地捕获跨会话的长期模式，避免低价值信息的缓存开销。

### Q6: 总结一下论文的主要内容

这篇论文提出PEEK系统，旨在解决长上下文LLM代理在重复交互同一外部环境时缺乏可复用定位知识的问题。核心贡献是设计了“上下文地图”（context map）这一常量大小的提示内缓存，存储关于外部上下文的内容、组织方式和历史有用的实体/常量/模式等可迁移知识。方法上，PEEK包含三个模块：Distiller从推理信号中提取可迁移知识，Cartographer将其转化为结构化编辑，Evictor基于优先级策略在固定token预算内进行驱逐。实验结果表明，在长上下文推理与信息聚合任务上，PEEK相比强基线提升6.3-34.0%，且迭代次数减少93-145次，成本降低1.7-5.8倍；在上下文学习任务上，求解率与评分准确率分别提升6.0-14.0%和7.8-12.1%。这些增益在多个语言模型和代理架构上通用。该工作证明，上下文地图能使长期上下文LLM代理更准确高效地交互重复外部环境。
