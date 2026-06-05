---
title: "Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems"
authors:
  - "Yingzhuo Liu"
date: "2026-06-04"
arxiv_id: "2606.05711"
arxiv_url: "https://arxiv.org/abs/2606.05711"
pdf_url: "https://arxiv.org/pdf/2606.05711v1"
categories:
  - "cs.CL"
tags:
  - "多智能体系统"
  - "潜在通信"
  - "LLM智能体通信协议"
  - "统一框架"
  - "智能体架构"
  - "推理效率"
relevance_score: 9.5
---

# Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems

## 原始摘要

Multi-agent systems built on large language models (LLMs) have become a prevailing paradigm for tackling complex reasoning, planning, and tool-use tasks. The dominant communication protocol in such systems is natural language: agents exchange messages token-by-token, verbalising their internal reasoning so that peers can read, verify, and respond. While convenient and interpretable, this protocol suffers from three structural drawbacks -- high inference cost, irreversible information loss during discretization, and ambiguity/redundancy of natural language. A growing body of work therefore explores an alternative protocol -- latent communication -- in which agents exchange continuous representations (embeddings, hidden states, or KV-caches) directly, bypassing the bottleneck of text generation. This paper presents a unified framework for organising the rapidly expanding literature on latent communication. We analyse existing methods along three orthogonal axes: (1) WHAT information is communicated (Embeddings, Hidden States, KV-Caches, or other continuous state); (2) WHICH sender-receiver alignment is used (latent-space alignment and layer alignment); and (3) HOW the communicated information is fused into the receiver (concatenation, prepending, mathematical operations, cross-attention, or cache restoration). Under this 3-axis framework, we systematically categorise eighteen representative methods proposed between 2024 and 2026, identify five major design patterns, and surface a set of open challenges -- including cross-architecture alignment, security of latent channels, compression for edge deployment, and the relationship between latent communication and latent chain-of-thought. We hope that this framework both lowers the barrier to entry for new researchers and provides a vocabulary for comparing future work.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决基于大语言模型的多智能体系统中，使用自然语言作为通信协议带来的三大结构性缺陷。研究背景是，当前多智能体系统普遍采用自然语言通信，智能体之间通过生成和解析离散的token序列来交换信息，这一范式虽然可解释性强，但存在显著不足。现有方法的不足包括：1）高推理成本，每次通信都需要发送者解码和接收者重新编码，导致大量额外计算开销；2）离散化过程中的信息损失，连续的高维隐藏状态被压缩成有限的token，丢失了数十万比特的语义信息；3）自然语言本身的歧义性和冗余性，语言优化追求流畅性而非信息密度，导致语义模糊或信息冗余。因此，本文要解决的核心问题是：如何设计一个统一框架来系统化组织新兴的潜在通信（latent communication）方法——即让智能体直接交换连续向量表示（如嵌入、隐藏状态、KV缓存），从而绕过文本生成瓶颈。该框架从三个正交维度（传输什么、发送-接收对齐方式、信息融合方式）对现有方法进行分类，旨在为研究者提供清晰的比较范式，并揭示跨架构对齐、潜在通道安全等开放挑战。

### Q2: 有哪些相关研究？

基于论文内容，相关研究主要围绕替代传统自然语言通信的潜在通信方法展开，可归类如下：

**方法类**：论文重点分析了18种代表性方法（2024-2026年），包括传递嵌入（embedding）、隐藏状态（hidden state）或KV缓存（KV-cache）的协议。例如，有些方法直接传输嵌入或隐藏状态以绕过文本生成瓶颈，另一些则利用KV缓存保留更多注意力信息。本文通过提出的三维框架（传输内容WHAT、发送-接收对齐WHICH、信息融合方式HOW）对这些方法进行系统分类，揭示了五种主要设计模式，并指出KV缓存信息量更大但更依赖架构。

**应用类**：相关研究涉及多智能体系统中的推理、规划、代码生成、科学问答和工具编排等任务。与本文关系在于，这些工作通常采用自然语言通信，而本文指出其在推理成本、信息离散化损失和语义歧义方面的结构性缺陷，并倡导潜在通信作为替代方案。

**评测类**：论文调查了实证结果，并识别出六个开放挑战，包括跨架构对齐、潜在通道安全性、边缘部署压缩、以及潜在通信与潜在思维链的统一。这些挑战为未来研究提供了方向。

本文与现有工作的主要区别在于：首次提出了统一框架来组织碎片化的文献，从三维度正交分解设计空间，并系统总结了可推广的设计权衡。通过对比，本文更强调潜在通信在信息密度（隐藏状态约40000比特 vs 单token约15比特）和推理效率上的优势，同时指出其缺乏可解释性的缺点，因此主张采用混合视图（自然语言用于人类监督、潜在通信用于智能体间中间信号传递）。

### Q3: 论文如何解决这个问题？

这篇论文通过提出一个统一的三轴框架（WHAT/WHICH/HOW）来系统化梳理LLM多智能体系统中的潜通信方法。核心方法是用连续表示（嵌入、隐藏状态、KV缓存等）替代自然语言代币作为智能体间的通信载体，从而规避文本生成的高推理成本、离散化信息损失和语言歧义。

整体框架围绕三个正交维度展开：
1. **WHAT（通信内容）**：智能体发送的信息类型，包括嵌入（如CIPHER模型的加权嵌入，编码完整词汇分布）、隐藏状态（如AC、Interlat传递中间层隐藏状态，编码推理过程）和KV缓存（如KVComm、Cache-to-Cache传递完整键值对，保留完整上下文信息）。不同类型在信息丰富度、传输成本和架构依赖性上呈阶梯式排列（KV缓存>隐藏状态>嵌入）。
2. **WHICH（对齐方式）**：发送方与接收方的空间对齐策略。包括潜在空间对齐（同构模型无需对齐，异构模型需学习投影层或通用视觉编解码器）和层对齐（最后层→首层、全层对应或选定层对应）。对于异构架构（如Llama与Qwen），需通过Mixture of Thought中的交互层或Vision Wormhole的通用视觉通道进行对齐。
3. **HOW（融合方式）**：接收方整合信息的方法，包括拼接（如CIPHER将发送方嵌入与接收方提示拼接）、前置（KV缓存类方法将发送方缓存附加到接收方缓存前）、数学运算（如AC的隐藏状态加法）、交叉注意力（MoT中主专家通过交叉注意力聚合多个专家信息）和缓存恢复（如RelayCaching直接移植缓存避免重计算）。

**创新点**：该框架揭示了潜通信设计中45种理论可能组合（3×3×5），而现有18种方法仅覆盖约17种，表明设计空间远未饱和。同时识别出五大设计模式和开放挑战（跨架构对齐、潜在通道安全、边缘部署压缩），为研究者提供了系统化的比较语言和工具。

### Q4: 论文做了哪些实验？

论文围绕基于大语言模型的多智能体系统中的潜在通信机制进行了实验评估。实验涵盖多种基准测试，包括推理、问答和数学任务。研究系统性地对比了18种代表性方法（2024-2026年），这些方法沿三个轴分类：通信内容（嵌入、隐藏状态、KV缓存或状态增量）、发送-接收对齐（潜在空间或层对齐）以及融合方式（拼接、添加、交叉注意等）。主要对比基线为自然语言通信（NL-Comm）以及各类潜在通信方法，如CIPHER、AC、Interlat、SDE、ThoughtComm、MoT、KVComm和C2C。关键实验结果包括：AC方法在推理基准上相比NL-Comm实现了约27%的准确率提升；Interlat在长上下文任务中实现高达24倍的延迟减少；MoT在同分布和域外基准上均超越先前最先进方法，准确率分别提升0.38%和2.92%。此外，SDE在复杂推理任务上达到最先进水平，而C2C因传输完整KV缓存而获得最强信息量但成本最高。实验设置兼顾同构与异构架构，部分方法（如Interlat和MoT）需学习投影或路由器，而CIPHER、AC等则为无训练方法。代码在arXiv链接中公开。

### Q5: 有什么可以进一步探索的点？

未来可进一步探索的方向包括：1）**跨架构对齐**：当前方法多假设同构模型间通信，如何实现不同架构（如LLaMA与GPT）间的有效潜空间映射仍待解决；2）**安全与隐私**：潜信道可能被注入对抗性扰动或泄露内部状态，需发展基于差分隐私或加密机制的鲁棒通信协议；3）**压缩与边缘部署**：KV-cache等连续状态存储开销大，可研究自适应量化或稀疏化策略以适配资源受限设备；4）**潜空间思维链**：将潜通信与隐式推理结合，探索无需离散化的端到端推理路径。此外，当前评估缺乏标准化基准（如通信效率-任务精度帕累托前沿），建议构建多维度测试平台。最后，可借鉴神经科学中的“工作记忆”机制，设计动态融合规则以实现更灵活的上下文感知通信。

### Q6: 总结一下论文的主要内容

本文提出一个统一框架，系统性梳理了基于大语言模型的多智能体系统中新兴的“潜在通信”范式。传统基于自然语言的通信存在高推理成本、离散化信息损失和歧义冗余三个结构性缺陷。潜在通信通过直接交换连续表示（如嵌入、隐藏状态或KV缓存）来绕过文本生成瓶颈。论文定义了三个正交分析轴：通信内容类型（WHAT）、发送者-接收者对齐方式（WHICH）和信息融合策略（HOW）。基于此框架，论文系统分类了2024至2026年间提出的十八种代表性方法，识别出五种主要设计模式，并揭示了跨架构对齐、潜在通道安全、边缘部署压缩及潜在通信与潜在思维链关系等开放性挑战。该框架为研究者提供了统一的术语和比较基准，降低了该碎片化领域的研究门槛。
