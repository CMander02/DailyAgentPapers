---
title: "Self-Augmenting Retrieval for Diffusion Language Models"
authors:
  - "Paul Jünger"
  - "Justin Lovelace"
  - "Linxi Zhao"
  - "Dongyoung Go"
  - "Kilian Q. Weinberger"
date: "2026-06-04"
arxiv_id: "2606.06474"
arxiv_url: "https://arxiv.org/abs/2606.06474"
pdf_url: "https://arxiv.org/pdf/2606.06474v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Retrieval-Augmented Generation"
  - "Diffusion Language Model"
  - "Dynamic RAG"
  - "Discrete Diffusion"
  - "Question Answering"
relevance_score: 8.5
---

# Self-Augmenting Retrieval for Diffusion Language Models

## 原始摘要

Discrete diffusion language models generate text by iteratively denoising an entire response in parallel. At each step, they predict tentative tokens for every masked position, committing the confident predictions to the output and discarding the unconfident ones. We show that the discarded tokens are in fact a useful lookahead signal for retrieval-augmented generation: even low-confidence tokens often surface salient entities early in the denoising trajectory, enabling retrieval of stronger evidence before the output is finalized. We exploit this through Self-Augmenting Retrieval for Diffusion Language Models (SARDI), a dynamic RAG framework that uses these lookahead tokens to guide retrieval during denoising. SARDI is training-free, retriever-agnostic, and applicable to any reasoning-capable discrete diffusion language model. Across five multi-hop QA benchmarks, SARDI outperforms current training-free diffusion and autoregressive retrieval baselines at up to $8\times$ higher throughput.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决检索增强生成（RAG）在多跳问答任务中的一个核心难题：静态检索的局限性。在传统方法中，检索通常仅基于初始问题，这无法处理需要逐步推理的多跳问题，因为中间推理步骤所需的证据（如桥梁实体）往往隐含在答案路径中，而非直接出现在问题里。此外，主流的自回归（AR）解码方式受限于从左到右的序列生成，不仅延迟高，且只能基于已生成的固定前缀进行检索，无法提前获取后续所需的信息。本文提出的SARDI框架利用了离散扩散语言模型（DLM）的独特优势来克服此问题。DLM通过并行去噪过程逐步完善整个输出，在早期步骤中，即使模型对部分预测置信度不高，这些“前瞻性”的中间状态也常常能提前揭示关键的桥梁实体。SARDI的核心创新在于：在去噪迭代过程中，动态地利用这些不稳定但包含未来信息的中间预测构建检索查询，从而提前检索到后续推理所需的证据，并在后续去噪步骤中融入更新后的上下文。该方法无需训练，兼容任何检索器，有效实现了在多跳问答中的动态检索，显著提升了生成质量与吞吐量。

### Q2: 有哪些相关研究？

在相关工作方面，本文主要涉及三类研究。

首先是检索增强生成（RAG）方法。早期RAG系统采用单次检索，从输入查询中一次性获取固定上下文，这在多跳问答任务中效果受限，因为后续推理所需的证据依赖于问题中未提及的桥梁实体。现有扩散语言模型的RAG方法均局限于这种单次检索范式。本文提出的SARDI是首个打破这一限制的扩散模型RAG框架。

其次是自回归语言模型中的动态与智能检索。这类工作通过将检索与生成过程交织来解决单次检索的局限，例如FLARE先生成暂定句子，再基于低置信度token进行检索。但与本文的SARDI相比，自回归解码的逐步生成方式会导致早期错误累积，产生幻觉查询；而SARDI通过并行预测所有暂定token，避免了错误传递。

最后是智能体检索系统，它们通过规划与自我反思生成显式搜索查询，但通常需要基于强化学习的专门训练，增加了工程复杂度。SARDI则无需训练，即插即用，不依赖任何学习得到的检索控制器或查询生成器。总结来说，本文创新性地利用扩散语言模型在去噪过程中的中间状态进行动态检索，是首个从扩散状态中提取信号以刷新检索证据的方法。

### Q3: 论文如何解决这个问题？

SARDI（Self-Augmenting Retrieval for Diffusion Language Models）的核心思想是利用离散扩散语言模型在去噪过程中产生的中间预测作为前瞻信号，动态指导检索。其整体框架是一个迭代循环，将检索与去噪过程交织在一起。每一步中，模型执行三个关键操作：解码、检索和提交。

具体架构上，SARDI从完全掩码状态开始。首先通过一次初始检索（仅基于问题）获得文档上下文。在每一步去噪中，模型为每个掩码位置预测一个token及其置信度。创新点在于设置了两个阈值：查询阈值（τ_q）和提交阈值（τ_c），且τ_q <= τ_c。这允许低置信度的预测token先被用于构建检索查询，即使它们还不足以被提交到最终输出。具体地，对于置信度大于τ_q的掩码位置，将其预测token填入“代理序列”；该序列去掩码后与问题拼接，形成增强后的检索查询。这个动态查询能捕获去噪早期浮现出的实体（如人名、日期、关系），而这些信息是原始问题中不包含的。然后使用新查询重新检索K个文档，替换旧文档上下文，用于下一步的去噪。在提交阶段，只有置信度超过τ_c的位置才会被提交并解除掩码；若没有位置达到τ_c，则提交最自信的一个以保证收敛。这种分离确保了即使是不确定的预测也能为检索提供早期线索，而对最终输出保持谨慎。

关键技术方面，SARDI是无需训练的，且与检索器无关（实验中使用了BM25）。它利用了扩散模型并行解码的优势，相比自回归模型可达到高达8倍的吞吐量。在五个多跳QA基准上，SARDI超越静态检索和多种无需训练的自回归基线。

### Q4: 论文做了哪些实验？

论文在五个多跳QA基准（2WikiMultiHopQA、HotpotQA、MuSiQue、CofCA、SynthWorlds-RM）上评估SARDI，使用精确匹配（EM）作为指标。实验设置包括：采用BM25稀疏检索（每轮K=7）和E5-base-v2密集检索，对比方法涵盖AR和扩散范式基线：静态检索（ARs、DLMs）、周期性检索（AR N=1/10）、FLARE、AdaptiveRAG、ReAct以及RL训练的Search-R1。主要结果：SARDI在2WikiMultiHopQA上将EM从DLM的44%提升至59%，在HotpotQA上从40%提升至49%，在CofCA上从43%提升至45%，在MuSiQue上从11%提升至21%。与静态扩散检索相比，SARDI在几乎所有基准上取得显著提升，并匹配或超越所有训练免费的AR基线，同时延迟更低（最高8倍吞吐量）。消融实验显示：更激进的查询阈值（τ_q≈0）获得最高EM，验证了低置信度token作为前瞻信号的有效性；SARDI在25%生成进度时召回率比AR基线高19个百分点；增益集中在多跳推理问题上（推理和组合问题EM提升超2.5倍），单跳问题不变；每步刷新检索可降低频率（每2步刷新仅损失1-2 EM）。

### Q5: 有什么可以进一步探索的点？

SARDI在以下方面值得深入探索：首先，扩散语言模型（DLM）目前无法仅通过提示词稳定产生推理链，需额外微调是主要限制。随着DLM向自回归模型成熟度发展，这一缺陷有望自然解决，届时SARDI可真正实现零训练应用。其次，每步去噪都刷新检索会带来文档编码开销，但相邻步骤间检索结果高度重叠，引入类似Fast-dLLM的块级KV缓存可显著提升效率。此外，DLM本质上支持并行解码，而SARDI的迭代检索机制可进一步优化为“检索-生成”交替框架，或在部分去噪步骤跳过检索以平衡效率与效果。将自增强检索拓展到潜在扩散语言模型是极具前景的方向，这类模型在连续空间操作，可能更易实现查询与文档的隐式对齐。最后，当前基准聚焦多跳问答，可评估SARDI在开放域对话、长文档摘要等更依赖语境更新的任务中的表现。

### Q6: 总结一下论文的主要内容

本文提出了一种名为SARDI的动态检索增强生成框架，利用离散扩散语言模型的去噪轨迹为多跳问答提供前瞻性检索信号。扩散语言模型在每一步去噪中会为所有掩码位置生成暂定预测，其中低置信度令牌常能提前暴露关键实体（如桥梁实体）。SARDI利用这一特性，在去噪过程中动态构建查询并检索证据，无需训练且与检索器无关。实验表明，基于检索的生成能显著降低令牌间互信息，促进并行解码。在五个多跳问答基准上，SARDI超越了静态检索和现有免训练扩散基线，推理速度提升高达8倍，实现了质量与延迟的帕累托最优。核心意义在于揭示了扩散模型去噪轨迹作为检索信号的潜力，为动态RAG提供了高效且轻量的新范式。
