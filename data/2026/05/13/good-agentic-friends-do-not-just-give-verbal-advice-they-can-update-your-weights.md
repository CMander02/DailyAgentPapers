---
title: "Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights"
authors:
  - "Wenrui Bao"
  - "Huan Wang"
  - "Jian Wang"
  - "Zhangyang Wang"
  - "Kai Wang"
  - "Yuzhang Shang"
date: "2026-05-13"
arxiv_id: "2605.13839"
arxiv_url: "https://arxiv.org/abs/2605.13839"
pdf_url: "https://arxiv.org/pdf/2605.13839v1"
categories:
  - "cs.CL"
tags:
  - "Multi-agent System"
  - "Agent Communication"
  - "Weight-space Communication"
  - "Low-rank Adaptation"
  - "LoRA"
  - "Efficient Inference"
  - "LLM Agent"
relevance_score: 9.5
---

# Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights

## 原始摘要

Multi-agent LLM systems usually collaborate by exchanging natural-language messages. This interface is simple and interpretable, but it forces each sender's intermediate computation to be serialized into tokens and then reprocessed by the receiver, thereby increasing the generated-token cost, prefill overhead, and KV-cache memory. We study an alternative communication interface: instead of appending a sender's message to the receiver's context, compile the sender's hidden states into a transient, receiver-specific weight perturbation. We introduce TFlow (Thought Flow), a weight-space communication framework for a known and fixed receiver architecture. For each query, frozen role-prompted sender agents process the input, and a learned parameter generator maps their internal activations into low-rank LoRA perturbations targeting the receiver's modules. These perturbations are fused and applied only during the receiver's generation, enabling instance-level adaptation without permanently changing the model or enlarging the receiver's text context. With three Qwen3-4B agents, TFlow improves over a standalone receiver by up to 8.5 accuracy points across five benchmarks while reducing processed tokens by up to 32.69%. Compared with a text-based three-agent baseline, it reduces total processed tokens by up to 83.27% and the wall-clock inference time by up to 4.6$\times$, while maintaining competitive accuracy on four of five benchmarks. These results suggest that transient low-rank weight perturbations can serve as an executable communication medium for efficient multi-agent LLM collaboration.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决传统多智能体LLM系统中智能体间通信成本高昂的问题。当前主流的多智能体系统采用自然语言文本作为通信接口，这种设计虽然简单可解释，但效率低下：发送者需要将内部状态序列化为文本token，接收者又必须重新编码这些token，导致额外的预填充（prefill）开销、KV缓存增长和生成token数量增加。尤其是在多个智能体或多轮通信场景下，这种“写-读”循环会严重消耗计算资源。

现有的一些改进方法尝试让智能体交换连续表示（如隐藏状态或嵌入），但这类方法要求接收者能直接理解发送者的表征空间，通常需要共享架构或精心训练的适配器，通用性受限。

本文提出一种全新的“权重空间通信”范式——TFlow（Thought Flow）。其核心思想是：不将发送者的信息以文本形式附加到接收者上下文中，而是将发送者的隐藏状态通过一个学习到的参数生成器，编译成针对接收者模型的低秩LoRA扰动（ΔW）。这些扰动是瞬时的、查询特定的，仅在接收者生成答案时临时注入，推理完毕后立即移除，恢复冻结的基座模型。这样，信息传递不再依赖文本，而是通过修改接收者的计算路径来实现高效的智能体协作。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：

1.  **多智能体协作范式**：早期工作如 **CAMEL** 和 **Generative Agents** 通过角色扮演对话实现协作。后续 **MetaGPT**、**ChatDev**、**AutoGen** 等则聚焦于工程化框架。此外，**多智能体辩论**（如 **ReConcile**）和 **Mixture-of-Agents** 通过聚合不同模型输出来提升性能。本文与上述工作的核心区别在于，这些方法均依赖自然语言作为通信媒介，而 TFlow 采用权重空间通信。

2.  **智能体间通信机制**：除自然语言外，近期研究探索了非文本信道。例如 **CIPHER** 使用概率加权输出嵌入通信，**Interlat** 和后续工作则通过压缩的隐状态或激活空间进行通信。本文提出的权重空间通信是一种互补范式，它将发送方的计算直接转化为接收方参数的扰动。

3.  **权重空间结构与静态合并**：如 **Task Vector** 模型和 **Model Soups**、**TIES-Merging** 等模型合并方法。这些方法都是静态的，合并系数固定，无法针对每个输入实例自适应。TFlow 则动态地为每个实例生成权重扰动。

4.  **低秩适配与动态权重生成**：包括 **LoRAHub**、**LoRA-Flow** 等动态适配器选择方法，以及使用超网络根据上下文（如任务嵌入、文档）直接生成适配器参数的方法。TFlow 是这一方向的延伸，但它动态地从多个发送智能体的推理状态生成适配器参数，而非基于静态文档。

### Q3: 论文如何解决这个问题？

TFlow（Thought Flow）提出了一种全新的多智能体通信范式，核心思想是将发送者的隐藏状态编译为接收者模型上的瞬态低秩权重扰动，替代传统的自然语言消息交换。整体框架包含三个主要组件：首先是**隐藏状态聚合模块**，每个发送者智能体（由角色提示和查询驱动）通过冻结的骨干网络进行一次前向传播，提取各层隐藏状态，并通过可学习的层聚合（温度缩放softmax）生成每个发送者的条件表示。其次是**参数生成器**，这是核心创新，采用多轴Transformer架构：它利用可学习的网格查询与条件表示进行交叉注意力初始化，然后通过堆叠的块进行三种互补的注意力操作——跨层自注意力捕获层间依赖、层内自注意力传播模块与秩槽信息、以及条件交叉注意力重新锚定到发送者表示，最后通过线性头将精炼的网格解耦为低秩LoRA因子。最后是**瞬态注入与融合机制**，多个发送者生成的LoRA因子通过轻量级标量门控进行软max融合，作为低秩偏移临时应用到接收者的指定线性模块中，推理完成后立即移除，确保每个查询独立且不改变模型权重。关键技术包括：基于缓存向量的多样性正则化损失（防止坍塌为查询无关LoRA），以及端到端训练仅更新参数生成器而保持骨干网络完全冻结。该方法在五个基准上提升了准确率，同时显著减少了处理token数（最多减少83.27%）和推理时间（最高4.6倍），证明瞬态低秩权重扰动可作为高效的多智能体协作通信媒介。

### Q4: 论文做了哪些实验？

论文在五个基准测试上评估了TFlow方法：GSM8K（数学推理）、MATH（数学）、MMLU-Redux（多学科知识）、HumanEval+（代码生成）和MBPP+（代码生成），均采用零样本思维链设置。对比方法包括单智能体基线（直接使用Qwen3-4B）和文本协作多智能体基线TextMAS（三个智能体通过文本通信）。骨干网络为冻结的Qwen3-4B，TFlow使用三个角色智能体（策略分析、知识检索、问题求解），并通过参数生成器将智能体内状态映射为低秩LoRA扰动（rank=4）注入求解智能体。主要结果：相比单智能体，TFlow在五个基准上准确率提升7.13至8.53个百分点，同时处理令牌减少5.35%至32.69%（如GSM8K：92.12% vs. 84.99%，令牌减少32.69%）。相比TextMAS，TFlow处理令牌减少71.73%至83.27%，推理速度提升2.31至4.58倍，但准确率在四个任务上略低1.32至4.53个百分点（HumanEval+例外，低9.76个百分点）。消融实验表明，实例条件化的LoRA（TFlow）优于静态LoRA（平均提升4.29点），且匹配样本扰动显著优于随机或跨任务扰动，验证了权重空间通信的实例级适应性。

### Q5: 有什么可以进一步探索的点？

这篇工作的核心局限在于对显式架构依赖的鲁棒性尚存隐忧——TFlow要求接收方模型完全固定且已知，参数生成器也需针对特定接收器进行预训练，限制了跨架构泛化；文本协同智能体虽可灵活适应不同模型，但TFlow的性能在部分并未反超传统方案。未来可探索将扰动正则化为结构无关的“通信原语”，比如解耦接收器特征空间的层级意义，训练通用型生成器。此外，目前仅探索了LoRA式低秩扰动，可尝试稀疏扰动或梯度校正等更高效的隐性信道，或让智能体学习动态选择通讯时机（何时言语、何时改权重）以权衡精度与计算成本。另一种方向是融合离散与连续介质——将部分推理路径“压缩”为扰动，保留可解释接口供必要回溯，或许能兼顾效率与可审计性。

### Q6: 总结一下论文的主要内容

多智能体LLM系统通常通过自然语言消息进行协作，虽然简单可解释，但强制序列化发送者的中间计算为token并被接收者重新处理，带来了高昂的token生成、预填充开销和KV缓存内存成本。为解决此问题，本文提出TFlow（Thought Flow），一种基于权重空间通信的新型协作范式。其核心方法是将发送者智能体的隐藏状态，通过一个学习的参数生成器，编译成针对接收者模型的瞬态、低秩LoRA扰动。这些扰动在接收者生成答案时融合并临时注入，实现了实例级适应，既不永久改变模型，也不增加接收者的上下文长度。在五个基准测试上，使用三个Qwen3-4B智能体的TFlow相比独立接收者准确率最高提升8.5个百分点，同时处理token减少最多32.69%；与基于文本的三智能体基线相比，处理token减少最多83.27%，推理延迟降低最高4.6倍，且在五个基准中的四个上保持了有竞争力的准确率。研究结果表明，瞬态低秩权重扰动可作为高效的多智能体LLM协作的可执行通信介质。
