---
title: "BLAgent: Agentic RAG for File-Level Bug Localization"
authors:
  - "Md Afif Al Mamun"
  - "Gias Uddin"
date: "2026-05-18"
arxiv_id: "2605.17965"
arxiv_url: "https://arxiv.org/abs/2605.17965"
pdf_url: "https://arxiv.org/pdf/2605.17965v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Bug Localization"
  - "Agentic RAG"
  - "Code Repair Agent"
  - "SWE-bench"
  - "File-Level Localization"
  - "Multi-Stage Pipeline"
  - "Cost-Efficient Agent"
relevance_score: 9.5
---

# BLAgent: Agentic RAG for File-Level Bug Localization

## 原始摘要

Bug localization remains a key bottleneck in downstream software maintenance tasks, including root cause analysis, triage, and automated program repair (APR), despite recent advances in large language model (LLM)-based repair systems. File-level bug localization is especially critical in hierarchical pipelines, where errors can propagate to downstream stages such as statement-level localization or patch generation. While Retrieval-Augmented Generation (RAG) offers a promising direction for grounding LLMs in repository context, existing RAG pipelines rely on static retrieval and lack the reasoning needed to identify faulty code accurately. In this work, we present BLAgent, a novel agentic RAG framework for file-level bug localization that integrates three key ideas: (i) code structure-aware repository encoding with path-augmented AST-based chunking, (ii) dual-perspective query transformation capturing both structural and behavioral signals, and (iii) two-phase agentic reranking combining symbolic inspection with evidence-grounded reasoning. Unlike prior graph-based or multi-hop agentic approaches, BLAgent performs bounded reasoning over a compact candidate set, balancing accuracy and cost. On SWE-bench Lite, BLAgent attains over 78% Top-1 accuracy with open-source models and over 86% with a closed-source model, while being over 18x cheaper than the strongest baseline using the same model. When integrated into an APR framework, it improves end-to-end repair success by over 20%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决文件级错误定位（Bug Localization）这一软件维护中的核心瓶颈问题。研究背景是，尽管基于大语言模型（LLM）的自动程序修复（APR）系统取得了显著进展，但错误定位，尤其是文件级定位，仍然是关键环节。现有方法存在明显不足：传统的检索增强生成（RAG）管道通常依赖静态的、基于文本的检索，无法捕获代码的结构特性（如语法边界、语义单元），且缺乏对检索结果进行深层推理和判断的能力，导致检索质量不佳。同时，一些基于图的智能体方法虽然具备推理能力，但计算成本高昂，需要遍历整个仓库，且可能导致候选文件集过大，超出LLM的上下文窗口限制。本文提出的BLAgent框架要解决的核心问题是：如何设计一个在成本和准确性之间取得平衡的智能RAG框架，以实现高精度的文件级错误定位。该框架通过“路径增强的AST感知分块”、“双视角查询转换”和“两阶段智能体重排序”等关键技术，提升检索的语义相关性和推理的精准度，从而有效降低错误定位成本并提高下游APR的成功率。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及三类工作：

1. **基于检索增强生成（RAG）的缺陷定位方法**：现有RAG方法如Bug2Fix、CoCoNuT等使用静态检索，缺乏对代码结构的理解。本文提出的BLAgent通过路径增强的AST分块和双视角查询转换，实现了对代码结构更精细的感知，突破了静态检索的局限。

2. **基于图或智能体的缺陷定位方法**：像GraphCodeBERT、CODE-MVP等方法利用代码依赖图进行多跳推理，但计算成本高。BLAgent采用两阶段智能体重排序，结合符号检查和证据推理，在紧凑候选集上进行有限推理，比纯图方法更高效且成本更低。

3. **端到端自动程序修复（APR）方法**：如RepairLLaMA、DEAR等。本文将BLAgent作为APR流水线的前置模块，实验表明它能提升下游修复成功率超20%，证明了文件级定位对修复系统的重要性，而现有APR工作多直接进行语句级定位或补丁生成。

与上述工作的核心区别在于：BLAgent首次将智能体RAG引入文件级缺陷定位，通过结构感知编码、双视角查询和两阶段重排序三个创新点，在SWE-bench Lite上实现了78%-86%的Top-1准确率，同时成本比最强基线低18倍以上。

### Q3: 论文如何解决这个问题？

BLAgent 采用了一种结构化的 Agentic RAG 流水线来解决文件级缺陷定位问题，核心包含三大创新设计。

首先，**代码结构感知的仓库编码**：不同于传统基于字符或行数的文本分块，BLAgent 利用抽象语法树 (AST) 对源代码进行分块 (AST-based chunking)。这确保了生成的每个代码块都保持完整的语法和语义边界（如完整函数或类），避免了表达式被截断的问题。同时，每个分块会嵌入其文件路径（如 `src/core/utils/math.py`），通过路径增强，使得分块的向量表示能直接与 bug 报告中的模块引用或堆栈跟踪路径对齐，解决了词汇不匹配问题。

其次，**双视角查询变换**：为弥合自然语言 bug 描述与代码结构之间的语义鸿沟，BLAgent 将原始报告分解为两种互补的检索查询。一是**结构变换 (T0)**，专注于提取报告中的标识符、模块名和类名等静态结构信息；二是**行为变换 (T1)**，专注于描述观察到的运行时错误、预期行为与实际结果的差异。这两种查询分别从“代码定位”和“行为指向”两个角度增强检索效果。

最后，**两阶段智能体重排序**：针对每个变换，检索出的文件候选集被拼接并送入一个 LLM 代理。该代理通过两阶段进行精排：首先是**符号检查**，计算候选文件的静态特征（如编辑历史、文件大小、与 bug 关键字的精确匹配）；然后是**证据推理**，代理结合 bug 报告和检索到的代码块，进行多步推理以评估每个文件为“最可能错误文件”的证据强度。这个过程在紧凑的候选集上执行有界推理，平衡了精度和推理成本。

整个框架通过“精确编码-多维查询-智能重排”的流水线，系统性地缩小搜索空间，最终输出排序后的可疑文件列表。

### Q4: 论文做了哪些实验？

论文在SWE-bench-lite数据集（包含300个真实Python bug实例）上评估了BLAgent的文件级bug定位性能。实验设置包括：(1) 与专用定位方法（BugCerberus、CoSIL、LocAgent）及端到端APR框架中的定位组件（Agentless、AutoCodeRover、OpenHands）对比；(2) 消融分析传统RAG配置、Agentic重排序、查询转换及LLM变体的影响；(3) 控制相同LLM（Claude-4.6-Sonnet）下与最强基线LocAgent的对比；(4) 扩展至函数级定位。主要结果：BLAgent（GPT-OSS）达到Top-1 78.6%、MRR 0.851，优于LocAgent（Claude-3.5）的77.7%和Agentless（GPT-4o）的63.0%；在Claude-4.6控制实验中，BLAgent的Top-1达86.7%（MRR 0.900），比同模型的LocAgent（82.4%）高4.3个百分点；集成至APR框架后修复成功率提升超20%。关键发现：Agentic重排序相比传统RAG显著提升定位精度，查询转换进一步改善结果，且开源模型（GPT-OSS）性能接近闭源模型。

### Q5: 有什么可以进一步探索的点？

BLAgent的检索聚焦于度量指标（如TF-IDF相似度）和符号分析（如依赖图），但未显式建模源代码的时序语义（如版本历史、提交日志中的修复模式）。未来可探索融合版本库挖掘技术，例如利用Git Blame定位近期变更高频的代码块，或通过对比错误版本与修复版本的差分特征增强检索信号。此外，该框架依赖Reranking阶段进行两次排序（符号+推理），但仍存在候选集规模与推理成本的权衡问题——当项目规模扩展到数万文件时，双阶段重排序可能引入延迟瓶颈。一种改进思路是：在AST分块时引入动态剪枝策略，根据文件与栈轨迹中异常链的语义关联度（如变量传播路径）预先截断低相关性代码块。同时，当前查询转换仅覆盖结构（方法调用图）和行为（异常堆栈）信号，但未利用错误栈帧间的变量状态变化（如空指针的赋值路径），这可通过轻量级动态分析（如给定测试输入的执行轨迹切片）注入更细粒度的诊断信号，提升Top-1命中率。

### Q6: 总结一下论文的主要内容

本文提出BLAgent，一种针对文件级缺陷定位的智能检索增强生成（RAG）框架。问题定义上，文件级缺陷定位是分层流水线中的关键瓶颈，其错误会传播至下游阶段，且现有RAG方法依赖静态检索，缺乏推理能力。方法上，BLAgent集成三项核心创新：基于路径增强的AST感知代码库分块以保持语义完整性；将错误报告分解为结构查询和行为查询的双视角查询变换；结合符号检查与证据推理的两阶段智能重排序。该方法在紧凑候选集上进行有界推理，平衡了准确性与成本。主要结论：在SWE-bench Lite上，BLAgent使用开源模型达到78%以上的Top-1准确率，使用闭源模型超过86%，且成本比最强基线低18倍以上。当集成到自动程序修复框架中，端到端修复成功率提升超20%。该工作证明了智能RAG在文件级缺陷定位中的有效性，并显著推动了下游自动化修复性能。
