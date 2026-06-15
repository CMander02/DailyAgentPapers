---
title: "Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows"
authors:
  - "Shikun Liu"
  - "Mufei Li"
  - "Dongqi Fu"
  - "Haoyu Wang"
  - "Yinglong Xia"
  - "Hong Li"
  - "Hong Yan"
  - "Pan Li"
date: "2026-06-12"
arxiv_id: "2606.14672"
arxiv_url: "https://arxiv.org/abs/2606.14672"
pdf_url: "https://arxiv.org/pdf/2606.14672v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "多智能体协作"
  - "KV Cache"
  - "并行计算"
  - "Agent框架"
  - "效率优化"
relevance_score: 7.5
---

# Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows

## 原始摘要

Large language models increasingly serve as execution engines for agentic systems, yet they still consume context through a sequential text interface. This creates a mismatch with modern structured agent workflows, in which independent branches explore subtasks, retrieve evidence, or generate candidate solutions before a final synthesis step. Existing systems typically merge these branches by concatenating their textual outputs, which discards the parallel structure and incurs redundant prefill computation. In this work, we introduce Parallel-Synthesis, a plug-and-play framework that enables a synthesizer to directly consume the KV caches produced by parallel worker agents. Parallel-Synthesis combines a cache mapper that calibrates independently generated branch caches with a fine-tuned synthesizer adapter that enables generation from this non-sequential cache interface. We train Parallel-Synthesis using data that exposes the synthesizer to parallel cache contexts, teaches aggregation across cached branches, and distills reasoning behavior from standard text-concatenation-based synthesis. Across nine downstream datasets spanning math, science QA, code generation, GAIA, and multi-agent database diagnosis, Parallel-Synthesis matches or outperforms text-based synthesis on seven datasets and remains close on the other two. It also reduces time-to-first-token by 2.5x-11x, suggesting that direct cache-based synthesis is a promising interface for more native and efficient synthesis over parallel agent branches.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型（LLM）在代理（Agent）工作流中处理并行分支时存在的效率与结构不匹配问题。研究背景是，LLM作为代理系统的核心执行引擎，但其输入输出接口本质上是顺序文本的序列化，即所有代理状态（消息历史、工具输出、中间推理等）都必须线性拼接成单一文本前缀。然而，现代结构化代理工作流常采用“并行执行-最终合成”（parallel-then-synthesize）的模式，例如多个独立分支同时探索子任务、检索证据或生成候选方案，最后再由一个合成器（synthesizer）汇总。现有方法的不足在于，合成器必须将各分支的文本输出重新拼接成一个超长的文本提示（prompt）进行再次编码，这不仅丢弃了原始工作流的有向无环图（DAG）结构，还造成了大量冗余的预填充计算（prefill cost），因为分支在生成时已经完成了编码。因此，本文提出的核心问题是：设计一种新的接口，让合成器代理能够直接消费并行工作分支的潜在状态（即KV缓存），而非依赖拼接后的纯文本输出，从而在保持甚至提升合成质量的同时，大幅减少冗余计算并提高效率。

### Q2: 有哪些相关研究？

在相关研究中，本文主要涉及两类工作。首先是**基于LLM的多智能体系统（MAS）**，这类系统将智能体计算组织为结构化工作流（如DAG），其中“并行-合成”模式常见于三种形式：并行化解决方案生成（通过投票、辩论等方法聚合）、并行化工具使用与开放探索（由主导智能体合成观察结果）、以及并行化输入上下文处理（将长文档分块处理后聚合）。本文与这些工作的核心区别在于，不依赖文本拼接的中间表示，而是直接在KV缓存层面进行合成。其次是**多智能体系统中的隐式通信**，已有研究探索了利用潜在表示作为紧凑的思维级消息，或将KV缓存作为可传输的执行状态，实现智能体间的顺序或成对状态传递。本文的独特之处在于聚焦“多对一”收敛模式（多个分支缓存由下游合成器联合解释），而非顺序传递。此外，虽然近期有工作研究并行分支投票选择的可复用潜在原语，但本文专注于训练通用的并行智能体合成器。与现有文本拼接方法相比，本文通过缓存映射器和微调合成适配器，直接利用并行分支的KV缓存进行高效合成，在保持性能的同时显著降低了首词延迟。

### Q3: 论文如何解决这个问题？

该论文提出的Parallel-Synthesis框架解决了大语言模型在智能体工作流中处理并行分支时效率低下的问题。其核心创新在于让合成器直接消费并行工作智能体生成的KV缓存，而不是将文本输出拼接成序列。

整体框架包含三个主要组件：位置重编码、缓存映射器和合成器LoRA适配器。位置重编码通过重新计算旋转位置编码（RoPE），将所有工作智能体的输出对齐到共享分支点后的同一位置区间，保持各分支输出的并行结构，消除序列拼接带来的位置偏差。缓存映射器是一个可学习的MLP，它根据每个工作智能体的输出长度和分支数量等元数据，对位置重编码后的键值缓存进行逐元素仿射变换，以校准独立生成的缓存，使其更接近顺序编码的效果。合成器LoRA适配器与缓存映射器联合训练，帮助基础模型学会理解和推理来自多个并行缓存的上下文。

训练过程分为两个互补的轨道。轨道1进行通用适配，使用多轮对话数据和可分解为独立语义块的任务数据（如工具使用、上下文学习、多文档问答），让模型学会从非序列化缓存中生成和主动整合跨分支信息。轨道2通过从传统文本拼接合成路线中蒸馏推理轨迹来提升高层次推理能力。两个轨道的检查点通过加权平均合并，以避免顺序训练导致的能力遗忘。关键技术在于将并行分支的KV缓存进行位置校准和可学习映射后，直接作为合成器的前缀缓存，使解码从共享位置开始，从而避免了冗余的预填充计算。

### Q4: 论文做了哪些实验？

论文在大规模多领域实验中评估了Parallel-Synthesis，实验覆盖9个数据集，分为4个领域：数学推理（AIME 2024/2025、GSM8K）、科学问答（GPQA、MedQA）、代码生成（HumanEval-Plus、MBPP-Plus）以及多智能体工具使用（GAIA三个等级、MARBLE数据库任务）。实验采用Qwen3-14B作为主干模型，对比方法分为三组：单轨迹与投票基准（Single、Voting）、基于文本的合成方法（Text-Serialization）、基于缓存的合成方法（APE、CacheBlend、KVLINK）。主要结果显示：在9个数据集中，Parallel-Synthesis在7个上匹配或超越Text-Serialization，仅剩两个存在微小差距；与纯文本方法相比，时间到首令牌(TTFT)加速2.5倍至11倍。关键数据指标包括：AIME 2024准确率63.33%（与Text-Serialization持平）、AIME 2025准确率46.67%（比Text-Serialization高23.34%）、GSM8K准确率94.69%、MARBLE数据库正确数36/100（Text-Serialization为33/100）。消融实验验证了后训练的必要性（无训练时AIME 2024仅10%），并表明包含可学习缓存映射器和合成器LoRA的完整模型优于任何单一组件。进一步分析显示，在大语言模型智能体工作流中，合并后的并行Worker轨迹缓存能有效传递中间推理状态，避免冗余预填充计算。

### Q5: 有什么可以进一步探索的点？

1.  **当前局限与扩展方向**：论文主要针对结构相对固定的“并行-合成”工作流，但真实多智能体系统中常有更复杂的动态拓扑（如嵌套并行、条件分支或异步循环）。未来可探索支持**层级化或非对称的缓存结构**，例如合成器需在部分分支未完成时动态调整注意力，或处理不同分支间长度、语义密度严重不平衡的场景。

2.  **基础模型与对齐难题**：框架依赖对合成器的微调来适配并行缓存，但基础大模型的缓存格式和注意力机制可能限制泛化能力。一个潜在改进是设计**更通用的缓存对齐协议**（如将分支缓存视为独立键值头并引入交叉注意力），或使用轻量适配器（如LoRA）动态映射多源缓存，从而无需为每种工作流重训练整个合成器。

3.  **质量控制与可解释性**：当前方法主要蒸馏基于文本拼接的推理，但缺乏对合成过程中分支信息贡献度的显式建模。后续可结合**分支重要性评估**，让合成器在生成时对不同缓存区域施加可学习的软掩码，或引入回溯机制验证各分支内容的一致性，避免因缓存压缩或对齐误差导致事实性错误。

### Q6: 总结一下论文的主要内容

这篇论文提出了 Parallel-Synthesis 框架，旨在解决 LLM Agent 工作流中并行分支合成效率低下的问题。传统方法需将并行分支的文本输出串联后重新编码，导致大量重复计算。该框架的核心创新是让合成器直接重用并行工作 Agent 生成的 KV 缓存，而非重新处理文本。为此，研发了缓存映射器校准独立分支的缓存，并微调合成器适配器使其能从此非序列缓存接口生成。通过在数学、科学问答、代码生成等9个数据集上评估，该方法在7个数据集上匹配或超越基于文本的合成，同时将首 token 生成时间降低2.5至11倍。主要结论是，直接基于缓存的合成是更高效且竞争力强的并行分支合成方案，但其在高度复杂结构化的流程中仍有局限。这项工作的意义在于，它为 DAG 结构的 Agent 工作流提供了更原生的执行与合并方式，显著减少了计算冗余。
