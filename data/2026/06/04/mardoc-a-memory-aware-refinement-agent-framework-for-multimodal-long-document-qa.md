---
title: "MARDoc: A Memory-Aware Refinement Agent Framework for Multimodal Long Document QA"
authors:
  - "Kaifeng Chen"
  - "Hongtao Liu"
  - "Qiyao Peng"
  - "Jian Yang"
  - "Yongqiang Liu"
  - "Xiaochen Zhang"
  - "Qing Yang"
date: "2026-06-04"
arxiv_id: "2606.05749"
arxiv_url: "https://arxiv.org/abs/2606.05749"
pdf_url: "https://arxiv.org/pdf/2606.05749v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "多模态长文档QA"
  - "Agent架构"
  - "记忆管理"
  - "检索-推理Agent"
  - "结构化记忆"
  - "反思Agent"
relevance_score: 9.5
---

# MARDoc: A Memory-Aware Refinement Agent Framework for Multimodal Long Document QA

## 原始摘要

Iterative retrieval-reasoning agents have recently shown promise for multimodal long-document question answering. However, most existing systems maintain a single growing context that mixes retrieval traces, observations, and intermediate reasoning. As interactions accumulate, key evidence becomes scattered and diluted, making multi-hop reasoning noisy. We propose MARDoc, a Memory-Aware Refinement Agent framework that decouples long-document QA into three specialized agents: an Explorer for multi-granularity multimodal retrieval, a Refiner for distilling interaction traces into structured evidence and reasoning memories, and a Reflector for checking evidence sufficiency and providing targeted feedback. Across iterations, the agents rely on a dynamically updated structured memory rather than a full accumulated interaction history. This design reduces context noise while preserving answer-critical facts and their logical dependencies. Experiments on MMLongBench-Doc and DocBench show that MARDoc achieves strong results, outperforming same-backbone baselines and demonstrating the effectiveness of structured memory for agentic document QA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多模态长文档问答中，现有迭代式检索-推理代理方法存在的两个核心问题：**上下文稀释**和**错误累积**。

**研究背景**：多模态长文档QA在许多真实场景（如财报分析、科学文献理解）中至关重要。这些文档中信息以文本、布局、表格、图表等多种模态呈现，且支撑证据往往稀疏分布在大量页面中，导致检索和跨页推理困难。

**现有方法的不足**：早期方法（如OCR端到端模型）难以扩展至长文档；检索增强方法虽缩短了输入长度，但难以关联跨页面、跨模态的证据。最新的**代理式方法**引入了迭代检索与推理，但其采用“**单一增长上下文流**”范式：每次交互都将新的检索结果和中间推理追加到同一上下文中。随着轮次增加，大量无关历史会稀释关键证据，压缩模型的有效推理空间。此外，这些方法缺乏基于记忆的质量控制，导致早期错误（如遗漏证据、误解图像）会在多跳推理中持续积累和放大。

**核心问题**：MARDoc旨在通过引入**动态更新的结构化记忆**来替换单一的上下文流，将长文档QA解耦为探索、提炼、反思三个专用代理，从而保持推理状态紧凑，减少噪音干扰，并实现基于记忆的证据充分性检查与定向反馈，最终解决上下文稀释和错误累积问题。

### Q2: 有哪些相关研究？

在相关研究中，本文分别从多模态文档问答和智能体记忆机制两个方向总结了相关工作。

**方法类**：多模态文档问答方面，早期方法依赖OCR流水线融合文本与视觉特征，或利用端到端MLLM直接处理文档图像，但严格受限于上下文窗口。RAG方法虽能检索多模态片段，却常忽略文档结构且在多跳推理中表现不佳。近期，DocAgent等代理方法通过构建结构化文档树并配备工具实现高效检索；DocDancer则利用合成数据提升代理的工具使用能力。与这些方法不同，本文指出它们因采用单一累积式上下文，导致关键证据在长交互中分散和稀释，降低了多跳推理的有效性。

**记忆机制类**：在智能体记忆方面，已有研究表明结构化记忆能通过缓解信息丢失来提升长程推理的性能与稳定性。例如，Agentic Reasoning和A-Mem将工具调用轨迹建模为结构化推理记忆；ReasoningBank则从历史调用中提取可迁移的工具使用模式。这些方法面向通用智能体，聚焦于压缩交互历史或积累跨任务经验。本文受此启发，但专门为文档问答设计了结构化记忆，通过迭代地从交互轨迹中蒸馏答案关键事实与推理链，直接解决了文档推理中的信息碎片化、逻辑连接弱及上下文爆炸问题。

### Q3: 论文如何解决这个问题？

MARDoc的核心创新在于通过“Explore-Refine-Reflect”三智能体架构和结构化记忆机制，将多模态长文档问答中的检索、精炼和反思解耦，以解决传统单一大上下文范式下关键证据分散、多跳推理噪声大的问题。

整体框架包含四个关键组件：首先，文档大纲构建模块利用MinerU解析器生成保留布局和视觉信息的细粒度语义节点，并借助多模态大模型为视觉元素生成描述，形成统一的结构化索引。然后，三个智能体迭代协作：1）探索者（Explorer）基于ReAct框架，使用多粒度工具从结构化大纲中检索文本和视觉信息，并生成推理链与候选答案，其输入包括查询、大纲、来自精炼者的历史记忆和来自反思者的反馈指令。2）精炼者（Refiner）在每个探索迭代结束后，将探索者的交互轨迹压缩为两种结构化记忆：证据记忆（记录与查询最相关的核心事实及来源）和推理记忆（提取推理路径并标注证据依赖关系，形成证据链），而非保留所有交互细节。3）反思者（Reflector）检查精炼后的结构化记忆，判断证据是否充分；若不足或存在错误，则生成针对性的启发式反馈指令（如“缺少总数”），引导探索者更高效地检索，避免重复错误。记忆通过迭代更新替代完整的历史积累，从而显著降低上下文噪声。

### Q4: 论文做了哪些实验？

论文在MMLongBench-Doc（135份文档，平均47.5页，含1082个问题，34%需跨页推理）和DocBench（229份文档，1102个问题）两个多模态长文档QA基准上进行了实验。对比方法包括三类基线：MLLM基线（如GPT-4o、Qwen3-VL-8B-Instruct）、RAG基线（如VisRAG、BOOKRAG）和Agent基线（如DocAgent、DocDancer）。主要结果：MARDoc采用Qwen3-VL-30B-A3B-Instruct在MMLongBench-Doc上达到57.1% ACC和54.6 F1，在DocBench上达到82.1 LasJ，超越所有同骨干基线，其中ACC比DocAgent（GPT-4o）高5.3个百分点。消融实验显示：移除Refiner后ACC骤降至45.9%，同时移除Refiner和Reflector后为50.2%，证实结构化记忆的重要性。随证据页数增加，MARDoc性能下降幅度显著小于对比方法。在迭代次数分析中，K=3时性能最佳，单跳ACC达61.6%，多跳43.8%。Token和延迟消耗：MARDoc平均每样本122.8k tokens和65.3秒，较DocAgent多22.5k tokens和15.9秒，但ACC提升7.8个百分点。

### Q5: 有什么可以进一步探索的点？

首先，MARDoc 当前完全依赖 prompt engineering 构建智能体，缺乏任务特定微调。未来可探索将检索、精炼和反思模块进行端到端训练，或引入强化学习优化记忆更新策略，以提升答案精确性。其次，框架仅在 Qwen3-VL 上验证，其通用性存疑。需要在更多多模态大模型（如 GPT-4V、LLaVA）上测试，并研究不同架构下记忆表示的适配性。再次，迭代式 Explore-Refine-Reflect 循环导致高延迟。可引入早停机制，基于记忆置信度动态决定是否提前终止；或设计并行化检索-推理流程，减少串行等待。此外，当前结构记忆对证据的时序依赖关系建模有限，可尝试引入图神经网络来显式编码多跳推理路径。最后，针对极端长文档（如数百页PDF），内存管理可借鉴稀疏注意力或层次化摘要预检索以进一步压缩噪声。

### Q6: 总结一下论文的主要内容

论文提出MARDoc框架，解决多模态长文档问答中多跳推理证据分散和噪声累积的问题。现有方法在迭代检索中混合同一增长上下文，导致关键证据被稀释。MARDoc将任务解耦为三个专门智能体：Explorer负责多粒度多模态检索，Refiner将交互轨迹蒸馏为结构化证据和推理记忆，Reflector检查证据充分性并提供针对性反馈。智能体间依赖动态更新的结构化记忆而非完整历史交互，从而降低上下文噪声并保留关键事实及其逻辑依赖。在MMLongBench-Doc和DocBench上的实验表明，MARDoc优于同骨干基线，验证了结构化记忆对智能体文档问答的有效性。该工作通过记忆感知的多智能体协作，显著提升了长文档多跳推理的准确性和鲁棒性。
