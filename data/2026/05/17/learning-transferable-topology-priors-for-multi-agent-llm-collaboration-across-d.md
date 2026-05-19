---
title: "Learning Transferable Topology Priors for Multi-Agent LLM Collaboration Across Domains"
authors:
  - "Taolin Zhang"
  - "Zijie Zhou"
  - "Jiuheng Wan"
  - "Tingyuan Hu"
  - "Chengyu Wang"
  - "Xiaofeng He"
  - "Richang Hong"
date: "2026-05-17"
arxiv_id: "2605.17359"
arxiv_url: "https://arxiv.org/abs/2605.17359"
pdf_url: "https://arxiv.org/pdf/2605.17359v1"
categories:
  - "cs.CL"
tags:
  - "多智能体协作"
  - "拓扑学习"
  - "LLM协作"
  - "迁移学习"
  - "条件变分图框架"
relevance_score: 8.5
---

# Learning Transferable Topology Priors for Multi-Agent LLM Collaboration Across Domains

## 原始摘要

Large language model (LLM)-based multi-agent systems have shown strong potential for complex reasoning by coordinating specialized agents through structured communication. However, existing topology-evolution methods typically construct or optimize a collaboration topology for each query from scratch, leading to substantial online search overhead, high inference-time token consumption, and limited scalability in multi-domain settings. We propose TopoPrior, a framework for learning transferable topology priors for multi-agent LLM collaboration across domains. Rather than repeatedly searching for effective collaboration structures online, TopoPrior learns reusable topology priors from reference collaboration graphs collected offline from multiple domains and uses them to generate query-conditioned initial collaboration graphs for downstream refinement. By shifting part of topology search from per-query online optimization to offline prior learning, TopoPrior amortizes search cost while remaining compatible with existing topology-evolution backbones. Technically, TopoPrior contains two key components. First, a transferable topology prior learning module employs a conditional variational graph framework to capture reusable structural regularities across domains in a latent space. Second, a query-conditioned latent adaptation module introduces adversarial alignment to reduce unnecessary domain discrepancy while preserving query-relevant structural variation. Experiments on multi-domain reasoning benchmarks show that TopoPrior consistently improves several heterogeneous topology-evolution backbones while reducing online inference-time token usage, with only modest additional trainable parameters. These results suggest that transferable topology initialization is an effective and lightweight mechanism for improving the efficiency of multi-agent LLM collaboration across domains.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决基于大语言模型的多智能体协作系统在多领域场景下面临的效率问题。现有的多智能体系统虽然通过结构化通信协调专业智能体进行复杂推理，但其拓扑结构构建方法存在显著不足。具体来说，现有方法（如强化学习、剪枝或自回归方法）通常将每个查询的拓扑构建视为从零开始的优化问题，这导致两方面问题：其一，在线搜索开销巨大，需要消耗大量推理时的token；其二，在多领域设置中缺乏可扩展性，每个新查询或新领域都需要重复进行昂贵的拓扑搜索。

研究背景方面，已有的多领域LLM推理方法主要包括三类：训练提示方法性能受限于模型自身能力；微调方法面临灾难性遗忘和高昂的训练存储开销；而多智能体协作方法虽具优势，但现有拓扑演化方法存在上述效率瓶颈。本文的核心创新是提出TopoPrior框架，旨在学习跨领域可复用的拓扑先验知识，将部分拓扑搜索从每个查询的在线优化转移到离线先验学习。其核心思想是：从多个领域离线收集的参考协作图中捕获可复用的结构规律，并利用这些先验为每个查询生成条件初始图，供下游拓扑演化细化使用，从而在保持与现有拓扑演化主干兼容的同时，摊销搜索成本并减少token消耗。实验表明该方法能以少量额外参数显著提升推理性能和效率。

### Q2: 有哪些相关研究？

相关研究可分为三类。第一类是**多智能体LLM协作方法**，早期采用预定义的交互模式（如独立聚合、链式通信、星型协调和树状层级），但缺乏灵活性。近期工作如GPTSwarm和DyLAN通过强化学习或动态选择优化协作图，剪枝方法移除冗余边，自回归方法按输入生成结构。本文与这些工作的区别在于：它们从零开始按查询在线搜索拓扑，而本文学习可迁移先验为其提供更好的初始化。第二类是**跨领域适应方法**，包括免训练方法（上下文学习、提示工程）和训练密集型方法（监督微调、LoRA），但分别受限于基础模型能力和灾难性遗忘风险。本文从不同角度（智能体间通信的结构适应）改进跨域推理效率，而非修改提示或参数。第三类是**结构知识重用**，领域泛化和表征转移工作表明共享潜在结构可支持跨域迁移，变分图框架用于建模可复用的结构模式。本文采用条件变分图框架学习跨域结构规律，并通过查询条件潜在适应模块进行对抗对齐，与现有方法的关键区别在于：首次将可迁移拓扑先验学习引入多智能体LLM协作，将拓扑搜索从逐查询在线优化转移到离线先验学习。

### Q3: 论文如何解决这个问题？

TopoPrior通过一个两阶段框架解决跨领域多智能体LLM协作中的拓扑初始化效率问题。其核心思想是将在线拓扑搜索的部分成本转移到离线先验学习中，学习可迁移的拓扑先验，从而为每个新查询生成高质量的初始协作图，减少后续在线优化的迭代次数。

整体框架包含两个主要模块。第一个是**可迁移拓扑先验学习模块**，采用条件变分图框架。该模块包含三个核心组件：变分编码器使用图卷积网络（GCN）对参考协作图进行编码，并与查询的BERT表示融合得到潜在变量z；条件生成器基于z和查询表示自回归地生成节点（选择角色）和边（预测通信链接）；条件先验网络为每个查询提供特定的潜在先验分布，使得在推理时无需参考图即可从先验中采样z。该模块通过最大化条件似然的证据下界来学习跨领域可复用的结构规律。

第二个是**查询条件潜在适配模块**，引入领域对抗判别器。该判别器对编码器输出的潜在变量z进行领域分类，并通过梯度反转层（GRL）进行对抗训练。这迫使编码器学习到领域不变的表征，减少不同领域间不必要的分布差异，同时保留与查询相关的结构信息用于图生成。最终训练目标结合了先验学习损失和领域适配损失。

创新点在于：(1) 提出将拓扑搜索从在线逐查询优化转为离线先验学习，实现搜索代价分摊；(2) 条件变分图框架能捕获跨领域可迁移的协作模式，并为新查询生成自适应的初始图；(3) 对抗性领域对齐提升了跨领域迁移的鲁棒性；(4) 作为一种轻量级初始化机制，可与现有拓扑演化方法无缝集成，在提升性能的同时显著降低推理时的token消耗。

### Q4: 论文做了哪些实验？

论文在 MMLU（7个领域，57个任务）和 C-Eval（5个领域，52个任务）上评估 TopoPrior，并额外构建了 C-Eval Hard（数学、化学、物理三个自然科学子域）用于鲁棒性测试。实验设置中，将细粒度子类别按语义相关性和基准分类法聚合为少量主要学科领域。对比方法分为三类：训练无关方法（PE、CoT、RAG，分别基于Llama3-8B、Qwen2.5-72B和DeepSeek-V3-671B）、训练密集型方法（MoDULA、MoDE、DES-MoE），以及轻量训练的多智能体拓扑进化骨干（G-Designer、AgentPrune、ARG-Designer、AgentDropout）。主要结果：在Llama3-8B上，TopoPrior+ARG在MMLU平均准确率达68.53%，优于原始ARG（65.58%）和所有其他组合；TopoPrior+AD达67.31%，同样超越原始AD（65.72%）。在DeepSeek-V3上，TopoPrior也一致提升各骨干。效率方面，TopoPrior显著降低在线推理token用量和通信轮次。消融和敏感性分析验证了条件变分图框架和对抗对齐模块的有效性，泛化实验表明其可迁移拓扑先验能适应未见领域。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在以下几个方面：首先，参考协作图由AgentDropout生成，并非全局最优，这限制了先验学习的上限，未来可探索使用多种或自适应生成的参考图来提升先验质量。其次，条件变分图框架依赖固定的角色池大小N，在动态扩展角色池时可能面临可扩展性问题，可考虑引入动态节点机制或层次化生成策略。此外，对抗对齐虽然减少了域间差异，但可能过度消除有益的结构变异，未来可研究信息瓶颈或选择性对齐方法，保留域特有但任务相关的模式。结合我的见解，一个值得探索的方向是引入元学习（meta-learning）来快速适应新域，只需少量样本即可调整先验分布。同时，当前框架仅优化初始图，未干预后续演化过程，可设计协同进化机制，使先验学习与下游拓扑优化形成闭环，进一步提升多智能体LLM协作的跨域泛化能力和推理效率。

### Q6: 总结一下论文的主要内容

这篇论文提出了TopoPrior框架，旨在解决多智能体LLM协作中跨领域拓扑结构重复搜索导致的在线开销大、推理token消耗高的问题。核心贡献在于将拓扑搜索从每个查询的在线优化转变为可迁移的离线先验学习。方法上，TopoPrior包含两个关键组件：一是基于条件变分图框架的可迁移拓扑先验学习模块，从多个领域的参考协作图中捕获可复用的结构规律；二是查询条件潜在自适应模块，通过对抗性对齐减少领域差异并保留查询相关的结构变化。实验在MMLU和C-Eval等跨领域推理基准上进行，结果表明TopoPrior能持续提升多种异构拓扑演化基线的下游性能，同时将在线推理token消耗降低高达40.22%，且仅增加约330万可训练参数。该工作验证了可迁移拓扑初始化作为提升多智能体LLM跨领域协作效率的轻量级有效机制。
