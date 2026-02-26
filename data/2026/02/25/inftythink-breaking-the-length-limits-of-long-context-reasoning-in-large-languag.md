---
title: "InftyThink: Breaking the Length Limits of Long-Context Reasoning in Large Language Models"
authors:
  - "Yuchen Yan"
  - "Yongliang Shen"
  - "Yang Liu"
  - "Jin Jiang"
  - "Mengdi Zhang"
  - "Jian Shao"
  - "Yueting Zhuang"
date: "2025-03-09"
arxiv_id: "2503.06692"
arxiv_url: "https://arxiv.org/abs/2503.06692"
pdf_url: "https://arxiv.org/pdf/2503.06692v5"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "长上下文推理"
  - "计算效率"
  - "LLM推理能力"
  - "迭代推理"
  - "模型训练"
relevance_score: 5.5
---

# InftyThink: Breaking the Length Limits of Long-Context Reasoning in Large Language Models

## 原始摘要

Advanced reasoning in large language models has achieved remarkable performance on challenging tasks, but the prevailing long-context reasoning paradigm faces critical limitations: quadratic computational scaling with sequence length, reasoning constrained by maximum context boundaries, and performance degradation beyond pre-training context windows. Existing approaches primarily compress reasoning chains without addressing the fundamental scaling problem. To overcome these challenges, we introduce InftyThink, a paradigm that transforms monolithic reasoning into an iterative process with intermediate summarization. By interleaving short reasoning segments with concise progress summaries, our approach enables unbounded reasoning depth while maintaining bounded computational costs. This creates a characteristic sawtooth memory pattern that significantly reduces computational complexity compared to traditional approaches. Furthermore, we develop a methodology for reconstructing long-context reasoning datasets into our iterative format, transforming OpenR1-Math into 333K training instances. Experiments across multiple model architectures demonstrate that our approach reduces computational costs while improving performance, with Qwen2.5-Math-7B showing 3-11% improvements across MATH500, AIME24, and GPQA_diamond benchmarks. Our work challenges the assumed trade-off between reasoning depth and computational efficiency, providing a more scalable approach to complex reasoning without architectural modifications.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在长上下文推理任务中面临的核心瓶颈问题。研究背景是，以OpenAI o1、DeepSeek-R1等为代表的先进推理模型虽然在复杂任务上表现出色，但其依赖的长上下文推理范式存在严重不足。现有方法主要问题在于：首先，解码器架构的计算复杂度随序列长度呈二次方增长，导致生成长推理链时计算和内存开销巨大；其次，推理过程受限于模型的最大上下文长度，常导致推理被截断而无法完成；再者，当推理长度超出模型预训练时的上下文窗口时，性能会显著下降。目前的主流解决方案，如压缩推理链或训练模型进行更简洁的推理，本质上仍是在传统的、单一连续推理链的范式内进行优化，只是试图使其更紧凑，并未从根本上解决计算复杂度随长度急剧增长这一核心可扩展性问题。

因此，本文要解决的核心问题是：能否通过改变模型固有的推理范式，而非在单一长推理链的约束内进行优化，来同时提升模型在复杂任务上的准确性和计算效率？为此，论文提出了InftyThink范式，其核心思想是将整体式的长推理过程，转化为一个包含中间总结的迭代过程。通过将推理分解为多个相互关联的短片段，并在每个片段后进行简洁的进度总结，该方法形成了类似锯齿状的内存使用模式。这使得推理深度在理论上可以无限延伸，同时将计算成本控制在有界范围内，从而打破了推理深度与计算效率之间固有的权衡。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：针对长上下文推理效率优化的方法、针对推理链压缩的技术，以及用于训练和评估的数据集与基准。

在**方法类**工作中，现有研究主要试图在传统单轮长推理范式内进行优化。例如，Chain-compression（如CoT-Valve）尝试在训练时预设压缩比来缩短推理链，但推断时缺乏灵活性；TokenSkip通过评估令牌重要性来跳过冗余令牌，但可能损害推理性能；LightThinker则使用特殊令牌将思维链动态压缩为潜在表示，但无法自适应确定每一步的压缩需求。这些方法的共同点是仍将推理视为一个连续、整体的长序列，主要致力于使其更紧凑，而未从根本上解决计算复杂度随序列长度二次增长的核心问题。本文提出的InftyThink与这些工作有本质区别：它彻底改变了推理范式，将整体推理分解为多个交替的短推理段和摘要，形成迭代过程，从而在理论上支持无限深度推理，同时将计算成本控制在有界范围内。

在**应用与评测类**方面，相关研究体现在推动长上下文推理的模型（如OpenAI o1、DeepSeek-R1）和基准数据集上。本文使用了由DeepSeek-R1蒸馏得到的开源数据集OpenR1-Math进行方法验证，并将其重构为适应InftyThink迭代格式的训练数据。在评测上，本文沿用了MATH500、AIME24和GPQA_diamond等数学与复杂推理基准，与主流长上下文推理模型进行性能对比。本文的工作与这些应用和评测研究是协同与改进的关系：它不改变模型架构，而是通过新的推理数据组织和训练范式，在相同的模型和基准上实现了效率与性能的提升。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为InftyThink的新型推理范式来解决长上下文推理中的计算复杂度高和上下文长度受限问题。其核心方法是将传统的单次长序列推理过程分解为多个迭代步骤，每个步骤包含有限长度的推理段和中间摘要，从而在保持计算成本有界的同时实现理论上无限的推理深度。

整体框架采用迭代式架构，主要包含三个关键模块：首先是**迭代推理机制**，将推理过程划分为多个相连的段落，每个段落由推理段和摘要组成；其次是**数据重构流水线**，将现有长上下文推理数据集转换为适合迭代训练的格式；最后是**训练实例构造**，基于重构后的数据对模型进行监督微调。

具体而言，每个推理迭代遵循固定模式：对于首次迭代，模型基于用户查询生成第一段推理内容（RP₁）及其摘要（S₁）；后续迭代则以前一次摘要（Sᵢ₋₁）作为历史上下文，生成新的推理段（RPᵢ）和摘要（Sᵢ）；最终迭代生成结论而非摘要，标志推理完成。这种设计形成了独特的“锯齿形”内存模式，显著降低了计算复杂度。

关键技术包括：1）**语义感知的分割算法**，在自然断点处将原始推理过程划分为语义连贯的段落，确保每个段落不超过预设的令牌长度阈值η；2）**摘要生成机制**，利用大型基础模型为每个推理段生成简洁摘要，摘要不仅基于当前段，还考虑所有先前段落以保持连续性；3）**灵活的训练实例构造**，根据迭代位置动态构建三种类型的训练样本，分别对应初始、中间和最终步骤。

创新点主要体现在三个方面：一是**范式转变**，将整体式推理重构为迭代过程，突破了传统方法中推理深度与计算效率的固有权衡；二是**可扩展性**，通过中间摘要实现无限推理深度，同时将计算复杂度从二次方降低到线性级别；三是**数据重构方法**，开发了系统化的流水线将现有数据集转换为迭代格式，无需修改模型架构即可实现高效训练。实验表明，该方法在多个基准测试上提升性能的同时显著降低了计算成本。

### Q4: 论文做了哪些实验？

实验设置方面，论文采用指令微调来验证所提出的推理范式和数据集。具体在五个不同规模的基础模型（Qwen2.5-Math-1.5B、Qwen2.5-Math-7B、Qwen2.5-14B、Qwen2.5-32B 和 Meta-Llama-3.1-8B）和两个指导模型（Qwen2.5-Math-1.5B-Instruct 及 DeepSeek-R1-Distill-Qwen-1.5B）上进行训练。训练使用了原始 OpenR1-Math 数据集（用于传统方法）和新构建的 OpenR1-Math-Inf 数据集（用于 InftyThink 方法），超参数设置中 η 为 4k，最大迭代次数为 10。

评估使用的数据集和基准测试主要包括数学推理任务：MATH500、AIME24 和 GPQA_diamond，并在附录中补充了 AIME25、Math Odyssey、AMC23 以及代码任务（如 HumanEval 和 MBPP）的评估。

对比方法为传统的“Vanilla”推理范式与提出的“InftyThink”迭代推理范式。主要结果通过采样16次（温度0.7）获得，关键指标包括平均准确率（ACC，%）、平均生成令牌数（TOK，K）和平均推理耗时（LAT，秒）。

主要结果显示，InftyThink 在所有模型规模和架构上均一致优于传统方法。以 Qwen2.5-Math-7B 为例，在 MATH500、AIME24 和 GPQA_diamond 上的准确率分别从 89.51%、32.92%、43.94% 提升至 91.29%、43.96%、52.97%，实现了 3-11% 的性能提升。同时，该方法通常能降低推理延迟（LAT），例如 Qwen2.5-Math-1.5B 在 MATH500 上的耗时从 1.42 秒降至 0.80 秒。实验还发现，模型规模越小，性能提升相对越显著，表明该方法能部分补偿小模型的能力限制。

### Q5: 有什么可以进一步探索的点？

基于论文分析，可进一步探索的点包括：首先，InftyThink 依赖人工设定的分段参数 η，其最优值可能随任务和模型动态变化，未来可研究自适应分段策略，例如基于内容复杂度或模型置信度动态调整分段长度。其次，论文主要评估数学推理任务，该方法在需要多模态信息或跨文档检索的复杂场景（如科学文献分析）中的泛化能力尚不明确，需扩展验证。此外，中间摘要的生成可能引入信息损失或偏差，未来可探索更精细的摘要机制（如基于关键实体或逻辑结构的压缩）以提升信息保真度。从系统优化角度，当前方法未充分利用硬件并行性，可结合推测解码等技术减少迭代延迟。最后，该方法与现有长上下文扩展技术（如滑动窗口）的互补性值得研究，例如在超长序列中混合使用分段摘要与局部注意力，以平衡效率与全局连贯性。

### Q6: 总结一下论文的主要内容

论文提出了一种名为InftyThink的新范式，旨在突破大语言模型在长上下文推理中的长度限制。核心问题是传统长上下文推理存在计算复杂度随序列长度呈二次方增长、受限于最大上下文边界以及超出预训练窗口后性能下降等瓶颈。现有方法多侧重于压缩推理链，未能从根本上解决计算扩展性问题。

为此，InftyThink将整体式推理转化为一个包含中间总结的迭代过程。其方法概述是：通过将短推理片段与简洁的进展摘要交错进行，该方法在保持计算成本有界的同时，实现了无限制的推理深度。这形成了一种特有的锯齿状内存模式，相比传统方法显著降低了计算复杂度。此外，论文还开发了一种将长上下文推理数据集重构为迭代格式的方法，并将OpenR1-Math数据集转化为33.3万个训练实例。

主要结论是，该方法在多种模型架构上的实验表明，它在降低计算成本的同时提升了性能。例如，Qwen2.5-Math-7B模型在MATH500、AIME24和GPQA_diamond基准测试上实现了3%到11%的性能提升。这项工作的核心贡献和意义在于，它挑战了推理深度与计算效率之间固有的权衡假设，为无需修改模型架构即可实现更可扩展的复杂推理提供了一条新路径。
