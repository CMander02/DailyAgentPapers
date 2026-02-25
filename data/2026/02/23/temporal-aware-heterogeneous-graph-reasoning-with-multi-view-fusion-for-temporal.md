---
title: "Temporal-Aware Heterogeneous Graph Reasoning with Multi-View Fusion for Temporal Question Answering"
authors:
  - "Wuzhenghong Wen"
  - "Bowen Zhou"
  - "Jinwen Huang"
  - "Xianjie Wu"
  - "Yuwei Sun"
  - "Su Pan"
  - "Liang Li"
  - "Jianting Liu"
date: "2026-02-23"
arxiv_id: "2602.19569"
arxiv_url: "https://arxiv.org/abs/2602.19569"
pdf_url: "https://arxiv.org/pdf/2602.19569v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "知识图谱问答"
  - "时序推理"
  - "图神经网络"
  - "多跳推理"
  - "表示融合"
relevance_score: 5.5
---

# Temporal-Aware Heterogeneous Graph Reasoning with Multi-View Fusion for Temporal Question Answering

## 原始摘要

Question Answering over Temporal Knowledge Graphs (TKGQA) has attracted growing interest for handling time-sensitive queries. However, existing methods still struggle with: 1) weak incorporation of temporal constraints in question representation, causing biased reasoning; 2) limited ability to perform explicit multi-hop reasoning; and 3) suboptimal fusion of language and graph representations. We propose a novel framework with temporal-aware question encoding, multi-hop graph reasoning, and multi-view heterogeneous information fusion. Specifically, our approach introduces: 1) a constraint-aware question representation that combines semantic cues from language models with temporal entity dynamics; 2) a temporal-aware graph neural network for explicit multi-hop reasoning via time-aware message passing; and 3) a multi-view attention mechanism for more effective fusion of question context and temporal graph knowledge. Experiments on multiple TKGQA benchmarks demonstrate consistent improvements over multiple baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决时序知识图谱问答（TKGQA）中的核心挑战。研究背景是，随着现实应用中时间敏感查询需求的增长，TKGQA变得日益重要。与传统知识图谱不同，时序知识图谱在事实三元组中加入了时间信息，使得查询更复杂，答案类型更多样（如实体或时间区间），因此需要更强的时序推理能力。

现有方法存在明显不足：1）在问题表示中未能充分融合时序约束，仅依赖预训练语言模型进行编码，忽略了知识图谱中与问题实体相关的动态时序信息，导致模型对显式实体提及过拟合，而无法感知由约束（如“之前的”）引起的隐式实体状态变化，造成推理偏差。2）缺乏对时序图谱结构的显式建模，难以执行明确的多跳推理（例如，需先检索某个事件的发生时间，再找出该时间对应的负责人）。3）语言表示与图谱表示（如来自预训练模型、图谱嵌入和图神经网络）通常处于不同的向量空间，现有方法多采用简单的拼接或加权聚合进行融合，效果欠佳。

因此，本文要解决的核心问题是：如何设计一个能够有效感知时序约束、支持显式多跳推理，并实现语言与图谱异构信息深度融合的TKGQA框架。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：时序知识图谱问答（TKGQA）方法、图神经网络（GNN）基础模型，以及应用于问答的GNN模型。

在**TKGQA方法**方面，代表性工作包括CronKGQA、TMA和TSQA。CronKGQA结合时序知识图谱嵌入与预训练语言模型进行答案预测；TMA则通过多视图机制融合问题中的实体信息与异构信号。本文提出的框架与这些方法密切相关，但指出了它们的不足：现有方法在问题表征中对时序约束的融合较弱，显式多跳推理能力有限，且语言与图谱表征的融合不够优化。本文通过引入约束感知的问题表征、时序感知的图神经网络进行显式多跳推理，以及多视图注意力融合机制，旨在系统性解决这些局限。

在**图神经网络基础模型**方面，相关工作包括经典的图卷积网络（GCN）、GraphSAGE和图注意力网络（GAT）。这些模型为图结构数据的学习提供了基础，但通常采用单跳邻居聚合机制，表达能力受限，且未针对时序维度进行专门设计。

在**应用于问答的GNN模型**方面，已有研究将GNN迁移至通用问答任务。然而，这些模型多使用基础的GNN变体，无法直接适用于本文关注的时序知识图谱问答场景，因为它们缺乏对时间信息的显式建模和复杂推理机制。

综上，本文工作建立在现有TKGQA方法和GNN技术之上，但通过深度融合时序约束、设计显式多跳推理路径以及优化多视图融合，显著区别于并推进了相关研究。

### Q3: 论文如何解决这个问题？

论文通过一个包含三个核心组件的整体框架来解决TKGQA中的问题：时序感知的问题编码、多跳图推理和多视图异构信息融合。

在时序感知的问题编码方面，方法首先采用基于TComplEx的知识图谱嵌入方法，获取实体、关系和时序戳的表示，并通过引入受Transformer启发的可学习位置编码来增强时序戳嵌入，以显式地融入时序顺序信息。此外，还设计了一个辅助训练目标来预测时序戳对之间的时序关系。为了捕捉时序约束下的实体转换，模型从知识图谱中检索相关的SPO事实，并使用预训练语言模型分别编码问题和事实。通过交叉注意力机制和对齐特征的门控融合，最终生成约束感知的问题表示。

在多跳图推理方面，模型构建以问题实体为中心的时序子图，并提出一种具有路径感知注意力的时序感知图神经网络。其消息传递机制包含了时序注意力，能够计算图中节点间基于时序关系的注意力权重。为了在单层传播中捕获多跳依赖，模型采用了一个扩散算子，该算子聚合了不同路径长度的信息，其中不同跳数的距离由可学习的系数加权。节点表示通过该扩散算子进行更新，最终的图表示则通过对与问题相关的节点进行注意力池化获得。

在多视图异构信息融合方面，论文提出了一个多视图注意力机制。该机制包含三个视图：第一视图是语义-符号对齐，通过跨模态注意力对齐问题和图表示；第二视图是时序感知融合，将时序信息融入融合过程；第三视图是上下文门控融合，使用门控机制自适应地组合来自不同视图的信息。最终的融合表示通过一个线性层和softmax激活函数用于答案预测。

整个模型采用端到端训练，结合了交叉熵损失和时序知识图谱嵌入目标。该框架的创新点在于：1）将语义线索与时序实体动态相结合的约束感知问题表示；2）通过时序感知消息传递实现显式多跳推理的图神经网络；3）更有效融合问题上下文和时序图知识的多视图注意力机制。实验结果表明，该方法在多个TKGQA基准测试上均取得了优于现有基线的性能。

### Q4: 论文做了哪些实验？

实验在两个TKGQA基准数据集上进行：CRONQUESTIONS（包含125K实体、1.7K时间戳、203个关系和328K事实）和TimeQuestions（包含16,000个标注问题，分为四类）。对比方法包括三类基线：(I) 预训练语言模型（如BERT、KnowBERT）；(II) 知识图谱嵌入方法（如EmbedKGQA、CronKGQA）；(III) 时序知识图谱嵌入模型（如CronKGQA、TMA、TSQA、TempoQR、CTRN）。主要评估指标为Hits@1。

在CRONQUESTIONS上，本文模型总体Hits@1达到0.969，比最强基线CTRN（0.920）提升4.9个百分点；在复杂问题上提升9.3%，在实体类答案上提升5.1%。在TimeQuestions上，总体Hits@1为0.539，显著优于CTRN的0.466；其中时序问题提升20.5%（0.617 vs. 0.512），序数问题提升7.9%（0.412 vs. 0.382）。消融实验表明，移除时序感知嵌入导致性能下降6.5%，移除自适应融合下降7.9%，移除多跳推理下降8.3%，移除约束感知组件下降11.6%，验证了各模块的有效性。

### Q5: 有什么可以进一步探索的点？

本文提出的方法在时序知识图谱问答（TKGQA）上取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，模型对时序约束的建模可能仍显粗糙，未来可探索更细粒度的时间表示（如连续时间嵌入或周期性模式），以更好地处理模糊或复杂的时间表达式。其次，当前的多跳推理主要在预定义的图结构上进行，未来可结合隐式推理或动态子图构建，以应对知识图谱的不完备性。此外，多视图融合机制虽有效，但可进一步引入可解释性组件（如注意力可视化），以增强推理过程的透明度。最后，该方法在跨领域或大规模动态图谱上的泛化能力有待验证，未来可探索增量学习或元学习策略，使模型能快速适应新兴的时序知识。这些改进有望进一步提升TKGQA在现实应用中的鲁棒性和实用性。

### Q6: 总结一下论文的主要内容

该论文针对时序知识图谱问答任务，提出了一种融合时序感知与多视图异构图推理的新框架。现有方法存在三个主要问题：问题表示中时序约束整合不足导致推理偏差、显式多跳推理能力有限、语言与图谱表示融合效果欠佳。

论文的核心贡献在于设计了三个关键模块：首先，提出约束感知的问题表示方法，将语言模型的语义线索与时序实体动态相结合，以增强对时间约束的捕捉；其次，构建时序感知的图神经网络，通过时间感知的消息传递机制实现显式的多跳推理；最后，引入多视图注意力机制，更有效地融合问题上下文与时序图谱知识。

实验结果表明，该框架在多个TKGQA基准数据集上均优于现有基线方法，验证了其在处理时间敏感查询时的有效性与鲁棒性。这项工作通过强化时序整合与推理过程，为时序知识图谱上的复杂问答提供了更可靠的解决方案。
