---
title: "Atropos: Improving Cost-Benefit Trade-off of LLM-based Agents under Self-Consistency with Early Termination and Model Hotswap"
authors:
  - "Naryeong Kim"
  - "Shin Yoo"
date: "2026-04-16"
arxiv_id: "2604.15075"
arxiv_url: "https://arxiv.org/abs/2604.15075"
pdf_url: "https://arxiv.org/pdf/2604.15075v1"
categories:
  - "cs.SE"
  - "cs.LG"
tags:
  - "Agent Efficiency"
  - "Cost Optimization"
  - "Self-Consistency"
  - "Early Termination"
  - "Model Hotswap"
  - "Graph Neural Networks"
  - "Software Engineering Agent"
relevance_score: 8.5
---

# Atropos: Improving Cost-Benefit Trade-off of LLM-based Agents under Self-Consistency with Early Termination and Model Hotswap

## 原始摘要

Open-weight Small Language Models(SLMs) can provide faster local inference at lower financial cost, but may not achieve the same performance level as commercial Large Language Models (LLMs) that are orders of magnitudes larger. Consequently, many of the latest applications of LLMs, such as software engineering agents, tend to be evaluated on larger models only, leaving the issue of improving the cost-benefit trade-off of such applications neglected. This paper proposes Atropos, a predictive early-termination analysis and hotswap technique that aims to improve the cost-benefit trade-off for LLM-based agents that use self-consistency. The core component of ATROPOS is a predictive model based on structural properties of LLM inferences: after merging multiple agentic inference paths into a graph representation, ATROPOS uses Graph Convolutional Network (GCN) to predict whether an ongoing inference will eventually succeed or not. If an agentic task instance running on the source LLM is predicted to fail, ATROPOS subsequently performs hotswapping, i.e., migrating the on-going inference context onto the more capable target LLM: this is feasible because LLM contexts are stateless. An empirical evaluation of ATROPOS using three recent LLM-based agents shows that ATROPOS can predict early termination of eventually failing inferences with the accuracy of 0.85 at the midpoint of the inference. Hotswapping LLMs for such inferences can convert up to 27.57% of them to be successful. Consequently, ATROPOS achieves 74.35% of the performance of closed LLMs with as low as only 23.9% of the cost.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大型语言模型（LLM）的智能体（Agent）在应用中面临的成本与效益权衡不佳的问题。研究背景是，随着LLM智能体（如用于软件工程任务的自动故障定位、程序修复等代理）的快速发展，其性能提升严重依赖大规模、高性能的商用闭源LLM，导致推理成本（包括财务、计算和通信开销）高昂。虽然开源的轻量级小语言模型（SLM）能提供低成本、低延迟的本地推理，但其能力通常较弱，直接使用会导致任务失败率增高，且失败往往在消耗完计算资源后才被发现，这造成了资源浪费。现有方法主要关注使用性能更强的LLM来提升效果，或单纯采用SLM来降低成本，但未能有效优化两者之间的权衡，尤其是在智能体普遍采用自我一致性（self-consistency，即多次采样推理以提高性能）策略时，成本问题进一步加剧。

本文的核心问题是：如何在不显著牺牲性能的前提下，大幅降低基于LLM的智能体（特别是采用自我一致性时）的推理成本？为此，论文提出了Atropos技术，它通过预测性早期终止分析和模型热切换（hotswap）来优化成本效益比。具体而言，Atropos将正在进行的多路径智能体推理构建为语义流图（SFG），并利用图卷积网络（GCN）实时预测当前在SLM上运行的推理是否最终会失败。如果预测为失败，则通过热切换技术将推理上下文无缝迁移到更强大的目标LLM（利用LLM查询的无状态特性），从而挽救部分原本会失败的任务，以较低成本获得接近高端LLM的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于LLM的智能体方法、用于提升智能体性能的技术，以及针对智能体行为的分析与预测方法。

在**方法类**研究中，本文重点涉及的ReAct和Self-Consistency是构建和增强LLM智能体的核心基础技术。ReAct通过交错生成推理轨迹与工具调用，使智能体能够执行多步任务；Self-Consistency则通过多次采样并聚合结果来提高答案的可靠性，但代价是计算成本高昂。本文提出的Atropos并非替代这些方法，而是旨在优化其成本效益，特别是针对采用Self-Consistency的智能体。

在**应用类**研究中，本文选取了三个具体的软件工程智能体作为评估对象：执行故障定位的AutoFL、自动程序修复的AutoCodeRover和RepairAgent。这些智能体均基于ReAct框架，通过迭代调用工具完成任务。现有工作通常直接在这些智能体上应用更大规模的LLM以追求性能，而本文则关注如何在保持性能的同时，通过动态切换模型来显著降低成本。

在**评测与分析类**研究中，与本文最直接相关的是Lachesis工作。Lachesis为AutoFL设计了语义流图（SFG）来表示推理轨迹，并预测已完成推理的正确性。**本文与Lachesis的主要关系和区别在于**：Atropos继承了SFG表示和基于图卷积网络（GCN）的预测思路，但进行了关键扩展。首先，Atropos的目标是**早期终止预测**，即对**进行中的部分推理**（而非已完成推理）做出成功与否的预测。其次，Atropos将框架**通用化**，通过设计不同的节点嵌入策略（如针对AutoFL/AutoCodeRover的确定性分组和针对RepairAgent的基于聚类的语义分组），使其能够支持多种智能体，而不仅限于AutoFL。最后，本文在预测基础上引入了**模型热交换**机制，这是Lachesis所不具备的，它允许在预测可能失败时将推理上下文迁移到更强大的LLM上，从而试图挽救任务，这是实现成本效益权衡的核心创新。

### Q3: 论文如何解决这个问题？

论文通过提出Atropos框架，旨在解决基于大语言模型（LLM）的智能体在自一致性（self-consistency）策略下成本与效益的权衡问题。其核心方法是结合**早期终止（early termination）** 与**模型热切换（hotswapping）** 技术，动态优化推理过程。

**整体框架**包含两个关键阶段：首先，在推理过程中实时预测任务是否会成功；若预测为失败，则触发第二阶段，将当前推理上下文无缝迁移到更强大的目标模型上继续执行。这种方法避免了传统级联（cascading）中必须等待初始推理完成再切换的浪费。

**主要模块与关键技术**如下：
1. **基于图卷积网络（GCN）的正确性预测模型**：这是Atropos的核心组件。系统将多个智能体推理路径合并为图结构（称为SFG），利用GCN进行图级别的二分类（成功/失败）。模型包含三层GCN，每层后接ReLU激活和Dropout层，最后通过全局平均池化生成图嵌入，再经线性层输出预测。该模型能够在中途（例如推理进行到一半时）以高准确率（如0.85）识别出最终将失败的推理，从而为早期终止提供依据。
2. **热切换机制**：当预测到失败时，系统执行热切换。这涉及将当前推理的上下文（已完成的前k-1步）从成本较低的源模型迁移到能力更强的目标模型，并从第k步开始在目标模型上继续生成后续轨迹。上下文迁移是无状态的，因此可行。热切换有两种模式：
   - **并行热切换**：在指定步骤k，对所有R个并行推理进行集体预测。若预测集体失败，则将所有活跃推理的上下文迁移至目标模型。
   - **顺序热切换**：当源模型生成的前k条完整轨迹被预测为失败时，剩余的执行（R-k条）直接由目标模型完成，无需迁移上下文，相当于动态切换至更强的模型集合。

**创新点**在于：
- 首次将图神经网络（GCN）用于LLM智能体推理过程的实时成功性预测，利用了推理路径的结构化特征。
- 提出了“热切换”概念，允许在推理中途切换模型并保留上下文，避免了传统级联中已产生成本的浪费，实现了成本节约与性能提升的兼得。
- 通过实证证明，该框架能以较低成本（仅约23.9%）达到闭源大模型74.35%的性能，并将高达27.57%的原本失败推理转化为成功。

### Q4: 论文做了哪些实验？

论文实验设置围绕四个研究问题展开。实验评估了Atropos在三个基于LLM的软件工程智能体上的效果：AutoFL、AutoCodeRover和RepairAgent。使用的数据集/基准测试包括D4J、BIP和SWE-bench，具体配置如表格所示，例如AutoFL使用D4J（353个样本）和BIP（500个样本），交互步数N=10，自洽样本大小R=10。源模型采用成本较低的开源小模型（如Llama-3-8B、Mixtral-8x7B）或GPT-3.5-turbo，目标模型为能力更强的商业大模型（如GPT-4o、GPT-4）。

对比方法包括：多数类基线、基于投票的置信度评分以及现有工作Lachesis。评估指标涵盖准确率、AUROC、AUPR和FPR@95。

主要结果如下：对于完整推理轨迹的正确性预测（RQ1），Atropos在大多数配置下优于基线。例如，在AutoCodeRover使用GPT-4且成功标准为Top-1时，Atropos的准确率达到0.93，FPR@95低至0.17。对于早期终止的有效性（RQ2），实验表明在推理中点（k=8）时，Atropos对最终失败推理的预测准确率可达0.85，AUROC为0.85，能够在节省成本的同时保持较高预测性能。热交换技术的有效性（RQ3）显示，通过将预测会失败的推理从源模型迁移到目标模型，最高可将27.57%的失败推理转化为成功，最终Atropos以仅23.9%的成本实现了闭源大模型74.35%的性能。消融研究（RQ4）验证了所提出的SFG图表示和FastText节点嵌入对预测性能的关键贡献。

### Q5: 有什么可以进一步探索的点？

本文提出的Atropos系统在提升LLM智能体成本效益方面取得了显著进展，但其仍有进一步探索的空间。首先，其核心预测模型基于图卷积网络（GCN）分析推理路径的结构特征，但可能忽略了时序动态、语义内容等关键信息，未来可融合多模态特征（如token置信度序列）以提升预测的早期性和准确性。其次，当前的“热切换”机制仅在预测失败时触发，未来可探索更动态、多级的模型调度策略，例如根据任务难度或当前路径的置信度，在多个不同规模的开放权重模型之间进行实时、自适应的切换，而非简单的“源-目标”两级切换。再者，系统评估集中于特定类型的软件工程智能体，其通用性有待验证；未来需在更广泛的智能体类型（如决策规划、多轮对话）和领域中进行测试。最后，成本模型目前主要考虑推理开销，未来可纳入延迟、能耗等更全面的系统指标，并探索与模型压缩、推测解码等技术的结合，以构建更精细化的成本效益优化框架。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为Atropos的技术，旨在优化基于大语言模型（LLM）的智能体在自洽性（self-consistency）方法下的成本效益权衡。核心问题是：开源小模型（SLMs）成本低但性能不足，而商用大模型（LLMs）性能强但成本高昂，现有研究多忽略两者间的平衡优化。

Atropos的核心方法包括早期终止预测与模型热切换。首先，它将智能体多条推理路径合并为图结构，利用图卷积网络（GCN）分析推理过程中的结构特征，以预测当前任务是否会成功；若预测为失败，则通过热切换技术将任务上下文无缝迁移到能力更强的目标LLM上继续执行，从而避免资源浪费。

主要结论显示：Atropos能在推理中点阶段以0.85的准确率预测失败任务；通过热切换，可将多达27.57%的失败推理转为成功。最终，该技术仅需23.9%的成本即可达到闭源LLM约74.35%的性能，显著提升了LLM智能体的实用性与经济性。
