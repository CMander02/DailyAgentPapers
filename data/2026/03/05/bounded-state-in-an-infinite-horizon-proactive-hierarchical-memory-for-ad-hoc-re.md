---
title: "Bounded State in an Infinite Horizon: Proactive Hierarchical Memory for Ad-Hoc Recall over Streaming Dialogues"
authors:
  - "Bingbing Wang"
  - "Jing Li"
  - "Ruifeng Xu"
date: "2026-03-05"
arxiv_id: "2603.04885"
arxiv_url: "https://arxiv.org/abs/2603.04885"
pdf_url: "https://arxiv.org/pdf/2603.04885v1"
categories:
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Streaming Dialogue"
  - "Memory Benchmark"
  - "Bounded-State Reasoning"
  - "Hierarchical Memory"
  - "Ad-Hoc Recall"
  - "Infinite Horizon"
relevance_score: 7.5
---

# Bounded State in an Infinite Horizon: Proactive Hierarchical Memory for Ad-Hoc Recall over Streaming Dialogues

## 原始摘要

Real-world dialogue usually unfolds as an infinite stream. It thus requires bounded-state memory mechanisms to operate within an infinite horizon. However, existing read-then-think memory is fundamentally misaligned with this setting, as it cannot support ad-hoc memory recall while streams unfold. To explore this challenge, we introduce \textbf{STEM-Bench}, the first benchmark for \textbf{ST}reaming \textbf{E}valuation of \textbf{M}emory. It comprises over 14K QA pairs in dialogue streams that assess perception fidelity, temporal reasoning, and global awareness under infinite-horizon constraints. The preliminary analysis on STEM-Bench indicates a critical \textit{fidelity-efficiency dilemma}: retrieval-based methods use fragment context, while full-context models incur unbounded latency. To resolve this, we propose \textbf{ProStream}, a proactive hierarchical memory framework for streaming dialogues. It enables ad-hoc memory recall on demand by reasoning over continuous streams with multi-granular distillation. Moreover, it employs Adaptive Spatiotemporal Optimization to dynamically optimize retention based on expected utility. It enables a bounded knowledge state for lower inference latency without sacrificing reasoning fidelity. Experiments show that ProStream outperforms baselines in both accuracy and efficiency.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现实世界对话以无限流形式展开时，现有记忆机制无法有效支持按需即时回忆（ad-hoc recall）的核心问题。研究背景是，尽管大语言模型在对话系统中取得了进展，但其长期记忆机制大多仍基于“先读取后思考”的范式，该范式假设上下文是静态且完全可访问的。然而，在实际的流式对话场景中，对话内容持续无限地流入，系统需要在对话展开的任何时刻，都能根据即时的推理需求，主动、高效地检索特定的历史信息。

现有方法的不足主要体现在两个方面：一方面，基于检索的方法为了控制计算成本，通常只使用片段的上下文，这导致了信息不完整和推理保真度下降；另一方面，试图维护完整上下文的模型则面临计算成本剧增和延迟无限增长的问题，无法满足实时性要求。这构成了一个关键的“保真度-效率困境”。

因此，本文要解决的核心问题是：如何在无限时间范围的流式对话中，设计一种具有有界状态的内存机制，使其既能支持高保真度的按需记忆回忆（满足感知、时序推理和全局意识的要求），又能保持高效率（低延迟），从而实现可扩展的实时部署。为此，论文提出了ProStream框架，通过主动的、层次化的记忆组织与动态优化来应对这一挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：对话记忆评测基准和长时记忆方法。

在**评测基准**方面，已有工作从单轮对话转向长时对话理解。早期研究评估基于长聊天历史的个性化回复生成，后续则采用问答范式量化记忆准确性，代表性工作包括MemoryBank、LoCoMo和PerLTQA。近期，LongDialQA引入了响应延迟约束，LongMemEval和ConvoMem则评估了推理、知识更新等能力。然而，这些基准均采用静态的“读取-思考”范式，与真实世界中动态、持续增长的对话流不符。本文提出的STEM-Bench是首个专注于**流式评估**的基准，支持在对话流展开时进行即时记忆检索，突破了现有工作的局限。

在**记忆方法**方面，相关研究旨在为智能体装备长时记忆。主要技术路线包括：直接扩展上下文窗口、使用可微分记忆架构，以及将记忆视为上下文压缩（如通过内部状态、离散令牌或RAG进行检索）。近期研究趋向结构化记忆，例如LiCoMemory和SGMem利用层次或图索引捕获多粒度关联，RMM和MemGAS结合在线强化学习和自适应检索。然而，这些方法本质仍是检索中心化和批处理的，无法满足流式场景对即时回忆的需求。本文提出的ProStream框架将记忆重构为**在线层次化状态维护**，通过主动的时空压缩实现高保真保留与低延迟推理，从而解决了流式对话中的核心挑战。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ProStream的主动分层记忆框架来解决无限流式对话中的有界状态记忆问题。其核心方法是将无限输入流转化为有限的知识拓扑结构，在保证推理保真度的同时实现低延迟的按需记忆检索。

整体框架是一个四阶段流水线。首先，**主动语义流感知**模块通过短时感知缓冲区（STSB）累积原始交互单元，并利用编码器嵌入和余弦相似度进行在线边界检测，将连续流分割为离散的语义块。其次，**分层多粒度蒸馏**模块将语义块构建为三层树状拓扑：场景层（粗粒度主题聚类）、事件层（时序上下文分割）和原子记忆单元层（细粒度事实保留）。这通过双路径机制实现：使用指令调优模型递归生成事件和场景摘要，同时利用GLiNER解析关系三元组作为原子节点，并通过新颖性检查将其整合到树中。

关键技术在于第三阶段的**自适应时空优化**。该模块将记忆维护形式化为一个在严格容量约束下的“召回概率最大化”问题。它基于理性记忆分析，为树中每个节点定义一个随时间衰减的效用值，该值综合了访问频率和时效性。当记忆容量超限时，系统采用一个近似最优的贪婪边际效用策略进行动态优化，包括：1）**最小遗憾剪枝**，剔除单位成本效用最低的节点；2）**语义合并**，合并相似节点以压缩特征空间；3）**级联抽象**，递归清理无叶节点的父节点以保持层次一致性。

最后，**概率证据基础推理**模块负责响应生成。它通过分层检索从记忆树中获取最相关的证据路径，检索分数结合了语义相关性和节点的时效效用。生成时，模型综合短时缓冲区、待处理记忆和树检索结果作为统一上下文，以自回归方式生成答案，确保严格的证据基础。

该框架的创新点在于：1）将流式记忆重新定义为有界状态演化过程；2）提出了多粒度分层蒸馏来结构化流数据；3）设计了基于效用的在线优化策略，动态管理记忆以平衡保真度与效率。实验表明，ProStream在准确性和效率上均优于基线模型。

### Q4: 论文做了哪些实验？

论文在自建的STEM-Bench基准（包含超过1.4万个对话流QA对）上进行了实验，评估模型在无限时域约束下的感知保真度、时序推理和全局意识。实验设置方面，ProStream的关键参数包括：漂移阈值0.7、缓冲区容量5、短期感知相似度窗口10；层次蒸馏相似度阈值0.85；自适应优化中频率权重α=0.6、近因权重β=0.4；生成阶段检索top-5场景和top-10事件，最终输出基于综合相关性分数筛选的top-3记忆单元，最小相似度0.5。

对比方法涵盖两类范式：（1）传统检索与摘要基线：标准RAG、全上下文（Full-Context）、滚动摘要及增强变体（如RQ-RAG、RAPTOR、GraphRAG、HippoRAG2）；（2）智能体记忆系统：MemoRAG、A-Mem、MemGAS。

主要结果显示，ProStream在推理保真度与延迟间取得了帕累托最优平衡。它甚至超越了全上下文基线，挑战了“更多上下文更好”的假设。在高阶推理（使用Gemini评估）和生成质量（BLEU-4）上领先，但在表面指标（如证据相似度）上偶尔落后于MemoRAG等检索密集型基线，这体现了设计权衡：优先语义抽象而非原始文本获取，以牺牲微小词汇重叠换取更优推理能力和实时可扩展性。消融实验证实了各组件（短期感知缓冲区、层次树、待定缓冲区）的必要性，移除任一均导致性能显著下降。

扩展实验表明，ProStream在不同骨干模型规模（Qwen-3B/7B/14B）上呈现正向缩放趋势，相对准确率增益随模型增大而提升；在不同上下文复杂度（以GPT-2交叉熵损失量化）下均保持优于全上下文基线的准确率和效率。案例研究进一步展示了其通过层次记忆整合纠正局部上下文缺陷的能力。错误分析则揭示了合规性偏见和隐式上下文解耦困难两大局限。

### Q5: 有什么可以进一步探索的点？

该论文在解决无限对话流中的记忆召回问题上取得了进展，但仍存在一些局限性和可进一步探索的方向。首先，ProStream框架依赖于多粒度蒸馏和自适应优化，但其蒸馏策略可能丢失细粒度信息，未来可研究更精细的信息压缩与保留机制，例如引入可学习的记忆单元或基于注意力的动态摘要。其次，实验主要在模拟的对话流上进行，未来需在真实场景（如客服、社交互动）中验证其鲁棒性和泛化能力。此外，论文未深入探讨记忆的长期演化问题，例如如何处理记忆冲突或过时信息的淘汰机制，这可以结合神经符号方法或因果推理来增强记忆的稳定性。最后，当前框架侧重于单模态文本，未来可扩展至多模态流（如语音、视频），并探索跨模态的记忆对齐与检索，以应对更复杂的现实应用。

### Q6: 总结一下论文的主要内容

本文针对无限流对话场景中的即时记忆召回问题，提出了首个流式记忆评估基准STEM-Bench和一种新型记忆框架ProStream。核心贡献在于解决了流式对话中的“保真度-效率困境”：传统检索方法仅使用片段上下文导致信息不全，而全上下文模型则带来无限延迟。ProStream通过分层蒸馏对连续流进行多粒度信息提炼，并结合自适应时空优化动态管理记忆保留，实现了有界知识状态。该方法支持按需即时记忆召回，在保证推理保真度的同时将推理延迟与流长度解耦，达到恒定时间效率。实验表明，ProStream在准确性和效率上均优于基线模型，验证了结构化记忆拓扑优于原始嘈杂的全上下文输入。
