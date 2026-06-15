---
title: "See What I See, Know What I Think: Dense Latent Communication Across Heterogeneous Agents"
authors:
  - "Siyi Chen"
  - "Xiaoyan Zhang"
  - "Meng Wu"
  - "Jonathan Tremblay"
  - "Valts Blukis"
  - "Stan Birchfield"
  - "Rene Vidal"
  - "Alvaro Velasquez"
  - "Sijia Liu"
  - "Qing Qu"
date: "2026-06-11"
arxiv_id: "2606.13594"
arxiv_url: "https://arxiv.org/abs/2606.13594"
pdf_url: "https://arxiv.org/pdf/2606.13594v1"
categories:
  - "cs.MA"
tags:
  - "多智能体通信"
  - "KV-cache通信"
  - "异构智能体对齐"
  - "跨模型表示学习"
  - "高效通信"
relevance_score: 8.5
---

# See What I See, Know What I Think: Dense Latent Communication Across Heterogeneous Agents

## 原始摘要

Multi-agent systems communicate mostly through text, paying a lossy and expensive decode and re-encode cost. KV-cache communication is a promising alternative, yet most prior work is homogeneous, using duplicate copies of the same model, and avoids the central challenge of cross-model latent alignment; existing heterogeneous methods are also restrictive, typically assuming shared input and using transferred caches mainly for steering. We study a more fundamental question: can heterogeneous agents be aligned well enough to perform real "mind reading" and transfer both what one agent sees and how it thinks? Our information-structure analysis reveals a duality: context-aware transfer is driven by sparse reasoning signals, while context-unaware transfer, where the receiver sees no input, requires dense contextual knowledge preservation. Motivated by this, we propose dense alignment for heterogeneous KV-cache communication via a lightweight cross-model cache transformation and two-phase training: reconstruction followed by generation. Across all six directions of {Qwen3-4B, 8B, 14B} and six in-domain and out-of-domain benchmarks, our method outperforms prior heterogeneous baselines, matches or exceeds text communication in context-aware settings at roughly 2 to 3 times lower compute, and remains effective in context-unaware transfer where prior methods collapse.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多智能体系统中异构模型之间高效、无损的潜在通信问题。当前基于大语言模型的多智能体系统主要依赖文本进行通信，这需要频繁的解码-重编码过程，不仅计算开销大，还会引入信息损失，且无法利用模型内部的丰富潜在表征。虽然KV缓存通信作为一种高效的潜在通信方式出现，但现有工作存在两大局限：第一，大部分研究集中于同构智能体（即使用相同模型的副本），因为异构模型在层深度、注意力头结构、通道几何和位置编码等方面存在差异，导致其潜在空间难以自然对齐；第二，现有方法主要在“上下文感知”场景下评估（接收方保留原始输入），此时传输的潜在信号仅作为推理引导，信息可以是有损的。本文要解决的核心问题是：能否让异构智能体实现真正的“读心术”，即通过密集对齐其潜在空间，不仅传递推理信号（“如何思考”），还能传递完整的输入上下文信息（“看到了什么”）。特别是在更具挑战性的“上下文无关”场景下（接收方完全依赖发送方的潜在表征进行推理），该方法需保持有效性，而现有方法在此场景下完全失效。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是**同构智能体间的潜在空间通信**，其核心利用相同模型架构的KV缓存可直接复用的特性，实现零样本状态共享。本文指出这类方法因假设模型参数完全一致，无法处理异构模型间的潜空间不对齐问题，是其研究出发点。第二类是**异构智能体的潜空间对齐**，现有工作存在明显局限：一些方法仅在简单的文本嵌入空间学习投影模块，而非更密集的表达性KV缓存；另一些使用缓存融合网络但假设所有智能体处理相同输入，缺乏通用性；还有方法依赖激进压缩或稀疏化来简化对齐，虽在上下文感知场景中可传递高层推理信号，但会丢弃KV缓存天然承载的密集上下文信息，导致不高效。第三类是**不同通信范式的分析**，本文首次区分了上下文感知（接收方仍可访问原始输入，缓存主要提供推理信号）和上下文无关（接收方仅依赖缓存，必须同时携带上下文证据和推理状态）两种模式。与仅关注前者的现有工作不同，本文揭示了后者的核心挑战——需要密集对齐以保留完整任务知识。基于此，本文提出轻量级跨模型缓存变换和两阶段训练方法，在密集对齐上显著优于现有异构基线。

### Q3: 论文如何解决这个问题？

该论文提出了一种面向异构智能体的密集潜在通信方法，核心是学习一个轻量级的跨模型缓存变换器，实现从发送方KV缓存到接收方兼容缓存的映射，从而在异构模型间进行“读心”式的密集信息传递。

整体框架分为两阶段训练：第一阶段是接收方缓存重建，对同一输入分别运行发送方和接收方模型获取各自KV缓存，然后训练变换器使发送方缓存能重建接收方自身的KV缓存，通过L2损失最小化两者差异，从而学习将发送方信息表达为接收方的“潜在语言”；第二阶段是生成导向通信，将变换后的缓存用于下游生成，联合优化上下文感知（接收方有输入）和上下文无关（接收方无输入）两种场景的生成损失，使同一通道既能提供稀疏推理信号，又能作为密集的上下文替代。

架构设计上，关键技术包括：1）位置解耦变换，先移除旋转位置编码（RoPE）在无位置空间中对齐内容，再恢复接收方位置约定；2）跨层对齐，通过单调的深度保持映射将发送方层与接收方层配对；3）KV组变换，利用每个KV组专用的MLP（含16倍隐藏维度扩展）和可学习门控权重进行键值变换。创新点在于直接学习异构密集对齐接口而非同构压缩扩展，且门控机制在保留密集知识的同时能突出稀疏推理子空间。

### Q4: 论文做了哪些实验？

论文在Qwen3-4B、8B和14B三种异构模型组成的全部六个单向通信方向上进行了实验。训练数据使用GSM8K、MATH（代数子集）和ARC-Challenge的混合集，分两阶段训练：第一阶段学习配对发送方和接收方的缓存状态对齐，第二阶段使用接收方自身的推理轨迹进行监督。评估在三个领域内任务（GSM8K、MATH-500、ARC-C）和三个领域外多选题基准（MMLU-Redux、MedQA、OpenBookQA）上进行。对比方法包括：仅接收方单智能体基线、文本通信基线（T2T）和基于缓存的稀疏引导基线（C2C）。实验分为上下文感知和上下文不可知两种场景。在上下文感知场景下，所提方法在所有领域内任务上匹配或超过T2T（GSM8K提升0.16至4.85个百分点，MATH-500提升6.00至20.40个百分点，ARC-C提升1.34至3.94个百分点），且在领域外任务上与T2T差距在5个百分点以内，同时计算成本仅为T2T的1/2到1/3。在上下文不可知场景下（接收方仅靠通信信号），T2T性能大幅下降（如4B→8B在GSM8K仅51.63%），C2C几乎崩溃（多方向接近0%），而所提方法保持高准确率（如8B→4B在GSM8K达91.36%，OpenBookQA达90.00%），验证了密集对齐对上下文不可知传输的关键作用。

### Q5: 有什么可以进一步探索的点？

这篇论文在异构智能体间通过KV-cache实现“读心”式通信方面取得了显著进展，但仍有几个值得进一步探索的方向。首先，当前方法在训练时假定了一组固定的、大小相近的模型对，其泛化性在跨更大规模或更小模型（如从0.5B到70B）上尚未验证，未来可研究更普适的轻量化适配器。其次，论文主要依赖重建损失进行对齐，这种监督信号可能过于稠密，限制了模型学习到真正的“推理模式”抽象。未来可以探索引入对比学习或互信息最大化，以捕获跨模型通用的推理结构而非表层表示。此外，在内容无关的设置下，接收方完全依赖“读心”令牌，这对长程连贯性要求极高。一个改进方向是引入动态的注意力掩码或门控机制，让接收方能根据任务复杂度自适应地决定依赖通信信号还是自身知识。最后，将这种通信机制扩展到更复杂的多步协作任务（如具身智能体规划）将是检验其生态位与效率的关键一步。

### Q6: 总结一下论文的主要内容

这篇论文研究了异构智能体之间通过键值缓存（KV-cache）进行潜在通信的问题。问题定义在于，现有文本通信存在信息丢失和计算开销，而多数潜在通信方法局限于同构模型，跨模型对齐面临结构差异挑战。论文提出了一种密集对齐框架，通过轻量跨模型缓存转换器、位置解耦和细粒度逐头变换，结合两阶段训练（先重建后生成）来实现异构模型间的KV缓存直接传输。主要结论是：信息结构分析揭示了上下文感知传输（接收者可见输入）依赖稀疏推理信号，而上下文不可知传输（接收者无输入）需要密集上下文知识保留。在Qwen3-4B/8B/14B六个模型的6个域内外基准测试中，所提方法超越现有异构基线，在上下文感知场景下匹配或优于文本通信且计算量降低2-3倍，并在基准方法失效的上下文不可知场景中保持有效性。核心贡献在于首次实现异构智能体间的“读心”式密集潜在通信。
