---
title: "LightThinker++: From Reasoning Compression to Memory Management"
authors:
  - "Yuqi Zhu"
  - "Jintian Zhang"
  - "Zhenjie Wan"
  - "Yujie Luo"
  - "Shuofei Qiao"
  - "Zhengke Gui"
  - "Da Zheng"
  - "Lei Liang"
  - "Huajun Chen"
  - "Ningyu Zhang"
date: "2026-04-04"
arxiv_id: "2604.03679"
arxiv_url: "https://arxiv.org/abs/2604.03679"
pdf_url: "https://arxiv.org/pdf/2604.03679v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.IR"
  - "cs.LG"
  - "cs.MM"
tags:
  - "Agent Reasoning"
  - "Memory Management"
  - "Thought Compression"
  - "Long-Horizon Tasks"
  - "Efficiency Optimization"
  - "Training Pipeline"
relevance_score: 9.0
---

# LightThinker++: From Reasoning Compression to Memory Management

## 原始摘要

Large language models (LLMs) excel at complex reasoning, yet their efficiency is limited by the surging cognitive overhead of long thought traces. In this paper, we propose LightThinker, a method that enables LLMs to dynamically compress intermediate thoughts into compact semantic representations. However, static compression often struggles with complex reasoning where the irreversible loss of intermediate details can lead to logical bottlenecks. To address this, we evolve the framework into LightThinker++, introducing Explicit Adaptive Memory Management. This paradigm shifts to behavioral-level management by incorporating explicit memory primitives, supported by a specialized trajectory synthesis pipeline to train purposeful memory scheduling. Extensive experiments demonstrate the framework's versatility across three dimensions. (1) LightThinker reduces peak token usage by 70% and inference time by 26% with minimal accuracy loss. (2) In standard reasoning, LightThinker++ slashes peak token usage by 69.9% while yielding a +2.42% accuracy gain under the same context budget for maximum performance. (3) Most notably, in long-horizon agentic tasks, it maintains a stable footprint beyond 80 rounds (a 60%-70% reduction), achieving an average performance gain of 14.8% across different complex scenarios. Overall, our work provides a scalable direction for sustaining deep LLM reasoning over extended horizons with minimal overhead.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLMs）在复杂推理任务中，因生成冗长的思维链（thought traces）而导致的计算和内存开销激增的问题。随着LLMs从“快速思考”模式（如标准生成）演进到“慢速思考”模式（如思维链提示、o1式多步推理），性能提升的同时也产生了大量中间令牌，使得基于Transformer架构的模型面临注意力计算复杂度二次增长和KV缓存线性增长的压力，严重制约了其在长文本生成和复杂、长程任务中的实际效率。

现有方法主要分为两类：一类是通过提示工程或专门训练，让模型在推理时生成更少甚至零中间令牌，但这通常需要精细的数据构造和迭代优化；另一类是在推理时进行实时令牌级干预，选择性保留重要的KV缓存，但这会因重要性评估的计算开销引入显著的推理延迟。两类方法在效率、通用性或延迟方面存在不足。

本文的核心问题是：如何在不显著损害推理质量的前提下，动态且高效地管理LLMs推理过程中不断增长的上下文，以维持其深度推理能力。为此，论文首先提出了LightThinker方法，通过训练LLMs将冗长的思维步骤压缩成紧凑的语义表示（即“要点令牌”），从表示层面实现压缩。然而，这种静态压缩在复杂推理中可能导致不可逆的信息丢失，形成逻辑瓶颈。为了克服这一局限，论文进一步提出了LightThinker++框架，引入了显式的自适应内存管理范式。该框架转向行为层面的管理，通过引入显式的内存原语（如提交、展开、折叠），使模型能够根据逻辑需要自主地将思维归档为语义摘要或检索原始细节，从而在标准推理和长程智能体任务中都确保鲁棒性和高效性。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提升大语言模型推理效率的方法展开，可归纳为以下几类：

**1. 推理方法与思维链扩展研究**  
以**Chain-of-Thought (CoT)** 为代表的逐步推理方法，通过分解问题提升复杂任务性能。进一步发展的 **o1-like 思维模式** 引入了试错、反思、回溯等行为，显著提升了推理能力，但生成了更长的思维轨迹，导致计算与内存开销大幅增加。本文的 LightThinker 系列工作在此基础上，重点关注如何压缩和管理这些冗长的中间思维，以降低开销。

**2. 推理效率优化技术**  
针对长序列生成带来的挑战，已有研究指出 **KV 缓存** 的内存负担和注意力计算的二次增长是主要瓶颈。相关优化工作通常集中于模型架构改进或缓存管理。本文则另辟蹊径，从**语义压缩**和**记忆管理**的行为层面入手，通过动态压缩中间思维为紧凑表示，并引入显式记忆原语进行自适应管理，从而直接减少峰值令牌使用和推理时间。

**3. 记忆与状态管理研究**  
在智能体或长视野任务中，如何有效维护和利用历史信息是关键。现有方法可能隐式地保留全部状态或进行简单截断。本文提出的 **LightThinker++** 与之区别在于，它实现了**显式的自适应记忆管理**，通过专门轨迹合成管道训练有目的的记忆调度，从而在长期任务中稳定内存占用并提升性能。

**总结**：本文与相关工作的核心关系是，在继承并旨在缓解 o1-like 长思维模式低效问题的基础上，提出了从静态压缩到动态行为级记忆管理的演进路径，在压缩率、推理加速和长任务性能稳定性方面提供了新的解决方案。

### Q3: 论文如何解决这个问题？

论文通过提出LightThinker和LightThinker++两个渐进式框架来解决大语言模型在复杂推理中因思维轨迹过长导致的认知开销激增和效率下降问题。其核心方法是从隐式的表示层压缩演进到显式的行为层内存管理，旨在动态压缩中间思维，仅保留对未来推理预测性强的信息。

整体框架分为两部分。LightThinker采用隐式隐藏状态压缩，其架构设计包括：1）**数据重构**：将原始推理轨迹分段，并在段间插入特殊令牌（如可选的压缩触发信号<w>、固定数量的要点令牌C和恢复生成令牌[o]），形成包含压缩过程的训练序列。2）**基于思维的注意力掩码构造**：在训练时强制施加特定的注意力依赖结构。在压缩阶段，要点令牌C仅能关注问题、先前压缩内容和当前思维段，以学习将当前段信息蒸馏到C中；在生成阶段，恢复令牌[o]仅能基于问题和压缩历史生成下一段，从而学会基于压缩摘要进行后续推理。3）**训练与推理**：训练目标是最大化重构序列的似然，模型学习压缩感知的推理，而无需预测插入的特殊令牌。推理时，模型动态地用少量压缩令牌替换已完成的思维跨度，从而大幅减少上下文长度。

LightThinker++则引入了**显式自适应内存管理**以增强鲁棒性，其关键创新在于：1）**显式内存管理框架**：将推理历史形式化为有序的推理实体序列，每个实体是双形式容器，包含原始推理R和语义摘要Z。模型通过一组内存原语（提交commit、扩展expand、折叠fold、终止answer）主动管理其上下文内存。推理时，模型操作于一个被管理的上下文，其中每个历史步骤根据其可见性状态被动态投射为摘要Z（存档状态）或原始推导R（活动状态）。这实现了粒度感知的控制，允许模型在遇到逻辑瓶颈时通过扩展重新检查细节，随后折叠以保持高信号上下文。2）**环境感知的轨迹合成**：为了训练模型掌握这些行为，设计了一个在线思维合成框架。它使用强教师模型在模拟内存受限的环境中生成高质量推理轨迹，轨迹中交织着显式内存动作。当教师模型发出提交调用时，环境会动态修改下一次迭代的提示，隐藏原始推理并提供摘要，迫使教师在真正的内存压缩状态下继续演绎，从而创建出交织着推理、归档和按需检索的高保真轨迹。3）**行为剪枝与质量控制**：对合成轨迹实施严格的内存生命周期约束进行过滤，确保微调数据反映的是有目的的上下文管理而非随机工具使用。标准包括生命周期完整性、对称性约束（折叠操作前必须有对同一步骤的扩展）以及抗抖动启发式规则（如限制操作密度、禁止连续相同操作等）。

核心创新点在于：从信息瓶颈原则出发，构建了从隐式表示蒸馏到显式行为管理的层次化框架；提出了基于注意力掩码的隐式压缩训练方法，以及通过内存原语和闭环轨迹合成实现的显式、可控制的内存管理机制，使模型能自主调度信息保留与再激活，从而在保证效率的同时，显著提升了长视野复杂推理和智能体任务的性能与稳定性。

### Q4: 论文做了哪些实验？

论文在通用推理和长视野智能体任务上进行了广泛的实验。实验设置方面，主要基于Qwen2.5-7B和Llama3.1-8B两个骨干模型，并使用了从Bespoke-Stratos-17k和DeepScaleR采样的高质量蒸馏数据集进行微调。评估数据集包括GSM8K、MMLU、GPQA和BBH（后两者使用了随机采样子集）。对比方法包括：作为性能上限的Vanilla模型（全参数指令微调）、两种免训练的加速方法（H2O和SepLLM）、一种基于训练的方法（AnLLM）、以及两种思维链基线（基于指令调优模型和R1-Distill模型）。对于LightThinker++，还引入了TokenSkip和Base Prompting作为额外基线。

主要结果体现在三个维度：
1.  **LightThinker在通用推理上的效率与性能**：在Qwen模型上，与Vanilla相比，LightThinker以仅1%的准确率损失，换取了26%的推理时间节省、70%的峰值令牌使用量降低以及78%的累积依赖降低，对应4.5倍的压缩率。在Llama模型上，以6%的准确率损失，换取了1%的推理时间节省、70%的峰值令牌降低和74%的累积依赖降低，对应3.9倍压缩率。具体数据上，LightThinker在Qwen模型上的平均准确率为62.80%，推理时间为10.17小时，峰值令牌为1289。
2.  **LightThinker++在标准推理上的表现**：在相同上下文预算下追求最大性能时，LightThinker++能将峰值令牌使用量降低69.9%，同时带来+2.42%的准确率增益。
3.  **LightThinker++在长视野智能体任务上的表现**：在超过80轮的交互中能保持稳定的内存占用（降低了60%-70%），并在不同复杂场景下平均实现了14.8%的性能提升。

关键数据指标包括：准确率（Acc）、推理时间（Time，单位小时）、峰值令牌数（Peak）和累积依赖（Dep，单位百万）。实验还表明，思想级分割（LThinker_tho）在性能上 consistently 优于令牌级分割（LThinker_tok）。

### Q5: 有什么可以进一步探索的点？

本文提出的LightThinker++框架在动态压缩思维痕迹和管理记忆方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其记忆管理机制依赖于特定的轨迹合成管道进行训练，这可能导致其泛化能力受限，未来可研究如何设计更通用、无需任务特定训练的自适应记忆调度算法。其次，当前方法主要关注推理过程中的token压缩，而未深入探讨不同压缩粒度（如概念级、规则级）对复杂逻辑保持的影响，未来可探索多尺度语义表示与重建机制。此外，框架在极端长程任务（如数百轮交互）中的稳定性仍有待验证，需研究更高效的内存淘汰与回忆策略。从系统角度看，可结合外部知识库或视觉模块，实现跨模态推理的轻量化。最后，将此类动态管理思想应用于模型微调或持续学习场景，以降低长期部署中的认知负荷，也是一个有潜力的方向。

### Q6: 总结一下论文的主要内容

该论文提出了LightThinker++框架，旨在解决大语言模型在复杂推理中因长思维链导致认知开销过大的问题。核心问题是如何高效压缩和管理推理过程中的中间思维，以降低计算资源消耗同时保持或提升推理性能。

方法上，论文首先引入LightThinker，通过动态压缩中间思维为紧凑语义表示来减少token使用。针对静态压缩在复杂推理中可能造成信息不可逆丢失的局限，论文进一步升级为LightThinker++，其核心贡献是提出了“显式自适应记忆管理”范式。该方法在行为层面进行管理，引入了显式的内存操作原语，并设计了一个专门的轨迹合成流程来训练模型进行有目的的记忆调度。

主要结论显示，该框架在三个维度上效果显著：LightThinker能降低70%的峰值token使用和26%的推理时间，且精度损失极小；LightThinker++在标准推理任务中，在相同上下文预算下，能减少69.9%的峰值token使用并带来2.42%的准确率提升；在长视野智能体任务中，其能在超过80轮对话中保持稳定的内存占用（降低60%-70%），并在不同复杂场景下平均获得14.8%的性能提升。这项工作为在扩展视野下以最小开销维持深度LLM推理提供了一个可扩展的方向。
