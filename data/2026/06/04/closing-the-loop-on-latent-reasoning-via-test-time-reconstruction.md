---
title: "Closing the Loop on Latent Reasoning via Test-Time Reconstruction"
authors:
  - "Xiaopeng Yuan"
  - "Haibo Jin"
  - "Ye Yu"
  - "Peng Kuang"
  - "Lijun Yu"
  - "Yushun Dong"
  - "Haohan Wang"
date: "2026-06-04"
arxiv_id: "2606.06252"
arxiv_url: "https://arxiv.org/abs/2606.06252"
pdf_url: "https://arxiv.org/pdf/2606.06252v1"
categories:
  - "cs.AI"
tags:
  - "Latent Reasoning"
  - "Test-Time Training"
  - "Self-Supervised Learning"
  - "Reasoning Optimization"
  - "LLM Agent"
relevance_score: 9.0
---

# Closing the Loop on Latent Reasoning via Test-Time Reconstruction

## 原始摘要

Recent work moves intermediate reasoning from natural-language traces into latent or cache-level representations to reduce token overhead and avoid a discrete communication bottleneck. However, this shift also removes a key advantage of textual reasoning: intermediate states are no longer inspectable, making it difficult to determine whether a latent state still preserves the constraints of the original query. As a result, latent reasoning typically operates in an open loop, where a latent state is produced and consumed without an input-anchored fidelity check. We propose ReLAT (Reconstruction-Guided Latent Reasoning At Test Time), a self-supervised test-time training method that closes this loop using the query itself as the reference. Our key observation is that if a latent state faithfully represents a query, the query should be recoverable from it; if the query cannot be recovered, the latent state has lost task-relevant information. ReLAT operationalizes this principle by constructing a differentiable Question -> Latent Thought -> Question cycle and optimizing query reconstruction loss through the latent thought before answer generation. This anchors opaque latent computation to the problem specification it is supposed to represent. Across mathematical reasoning, knowledge QA, and code generation benchmarks on the Qwen family, ReLAT consistently improves over single-model inference, text-based collaboration, open-loop latent collaboration, and alternative test-time training objectives. On Qwen3-8B, ReLAT raises AIME 2024 accuracy from 56.7% to 73.3%, a 16.6-point gain over the strongest open-loop latent baseline.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决潜在推理（latent reasoning）中的“开环”问题，即中间潜在状态缺乏与原始查询的保真度检查机制。

**研究背景**：近期研究将推理过程从自然语言痕迹转移到潜在或缓存级别的表征中，以减少token开销并避免离散通信瓶颈。传统的文本推理具有可检查性，其中间步骤是否偏离问题约束是可见的。

**现有方法不足**：在潜在推理中，中间状态变为不透明的潜在向量，无法被检查。现有的潜在推理方法都是“开环”的：系统产生一个潜在状态后，直接将其用于后续计算，而不验证该状态是否仍保留了原始查询中的关键约束信息。例如，一个潜在状态可能丢失了问题的某个条件，但下游计算无法察觉，将其与保真的状态等同处理，导致最终答案出错。

**本文核心问题**：如何为不透明的潜在推理状态提供一个可微分、自监督的保真度信号，使其锚定回原始查询？作者提出ReLAT方法，在测试时构建一个“问题→潜在思维→问题”的可微分循环，通过优化查询重建损失，将中间潜在计算与问题规格绑定，从而将潜在推理从开环转变为闭环。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：

1. **自然语言推理与通信**：早期方法如Chain-of-Thought、ReAct、Reflexion、Self-Refine等，通过显式的文本中间步骤实现推理和通信，优点是可检查，但存在token开销大和离散通信瓶颈的问题。本文与这些方法的区别在于，本文采用潜在表示而非自然语言，以减少开销并避免信息压缩。

2. **潜在推理与通信**：ThoughtComm、Cache-to-Cache、LatentMAS等工作探索使用潜在表示或缓存级表示进行中间推理和通信，以绕过文本瓶颈。但这些方法主要关注状态如何传递，而非如何验证其保真度，导致语义漂移难以检测。本文在此基础上引入重建验证机制，将开环潜在推理转变为闭环。

3. **测试时训练（TTT）**：现有TTT方法如Anti-CF、SYTTA、COME、QTTT等，通常优化熵最小化、一致性正则化或上下文适应，但缺乏对潜在推理状态保真度的直接检查。本文提出的ReLAT利用自监督重建损失，通过“问题→潜在思考→问题”循环，直接验证潜在状态是否保留了原查询约束，填补了这一空白。

### Q3: 论文如何解决这个问题？

为了解决开放式潜在推理中缺乏输入锚定保真度检查的问题，论文提出了ReLAT方法，通过测试时重建形成一个闭环。其核心思想是：如果潜在状态忠实地保留了查询中的约束，则原始查询应从该状态中可恢复；反之则丢失了关键信息。

整体框架是一个可微的“问题→潜在思考→问题”循环。系统由单个预训练语言模型和两个组件构成：**可微潜在思考生成器**与**问题重建模块**。

在关键技术方面，首先，为了建立可微分路径，ReLAT放弃了离散token选择，采用**连续松弛技术**。在潜在思考的每个步骤，模型输出logits后，通过带温度系数τ的softmax得到词表上的软分布，然后计算该分布与词嵌入矩阵的加权和，得到连续的潜在向量。这些向量保留了嵌入空间的语义，且整个过程可微。

其次，**测试时训练（TTT）**过程如下：在临时LoRA适配器的支持下，模型首先生成长度为K的连续潜在思考序列。随后，同一个模型（含当前的LoRA参数）尝试从该序列中重建原始输入问题。计算**掩码交叉熵损失**作为重建损失，该损失仅作用于问题token而排除格式模板。此损失通过反向传播仅更新LoRA参数，冻结骨干模型。经过N步优化后，使用更新后的模型直接从原始问题生成最终答案。每次推理后LoRA参数被重置，确保实例级训练。

ReLAT的关键创新在于将**自监督重建**作为保真度信号，将原本开环的潜在推理转变为**闭环**过程，使潜在状态在最终推理前锚定到输入问题，从而显著提升推理质量。

### Q4: 论文做了哪些实验？

论文在数学推理、代码生成和知识问答三大类基准上进行了实验。实验设置包括：数学推理使用AIME 2024/2025竞赛级数学问题；代码生成使用MBPP+（含增强测试用例）；知识问答使用GPQA-Diamond（专家级科学推理）和MedQA（专业医学知识）。对比方法包括：单模型推理（Single）、基于文本中间推理的TextMAS、以及开环潜在通信的LatentMAS。主要实验在Qwen3-4B、Qwen3-8B、Qwen3-14B和DeepSeek-R1-Distill-Qwen-7B四个骨干模型上进行。关键结果：在Qwen3-8B上，ReLAT将AIME 2024准确率从LatentMAS的56.7%提升至73.3%，AIME 2025从53.3%提升至63.3%；在平均准确率上，ReLAT在所有骨干模型上均取得最佳。此外，与替代测试时训练目标（COME、QTTT和直接重建TTT）对比，ReLAT在AIME 2025、MBPP+和GPQA-Diamond上分别达到63.3%、76.7%和48.0%，优于所有对比基线。与文本迭代方法Self-Refine相比，ReLAT在AIME 2025上仅用10,280.22个token即达到63.33%准确率，而Self-Refine需64,381.37个token才达53.33%，减少84.0% token消耗。消融实验显示，学习率2e-5和潜在思维长度K=16或32时效果最佳。

### Q5: 有什么可以进一步探索的点？

ReLAT通过重建约束显著提升了潜在推理的可靠性，但该方法仍存在若干值得探索的局限。首先，重建损失本质上是必要而非充分条件，一个能完美恢复输入查询的潜在状态仍可能包含错误推理路径，未来可探索结合过程监督或反事实推理来区分“忠实但错误”的潜在状态。其次，当前方法仅使用单一重建目标，可能无法捕获复杂推理中的多步约束，可考虑引入层次化重建（如重建中间子问题或关键步骤）来提供更细粒度的保真度信号。此外，ReLAT在测试时引入了额外计算开销，未来可研究如何通过知识蒸馏或缓存机制使其更高效，例如训练一个预测重建质量的轻量网络来跳过高质量潜在状态的优化。最后，将重建思想扩展到多模态推理或具有明确中间变量的结构化任务（如程序合成中的中间变量监督）可能进一步验证其通用性。

### Q6: 总结一下论文的主要内容

该论文提出了ReLAT，一种自监督的测试时训练方法，旨在解决潜层推理中的开环问题。现有潜层推理将中间推理过程转移到连续表示中，虽然减少了token开销，但也失去了可检查性，导致潜层状态可能偏离原始问题约束而不被发现。ReLAT通过构建可微的“问题→潜层思维→问题”重建循环来闭合此环路，利用原始问题本身作为参考，通过最小化从潜层思维中重建问题的损失，在生成最终答案前对潜层状态进行锚定和校正。实验表明，在数学推理、代码生成和知识问答等多个基准上，ReLAT一致地优于单模型推理、文本协作、开环潜层协作及其他测试时训练方法。例如，在Qwen3-8B模型上，ReLAT将AIME 2024的准确率从56.7%提升至73.3%。该工作为提升潜层推理的可靠性和可控性提供了一种有效方案。
