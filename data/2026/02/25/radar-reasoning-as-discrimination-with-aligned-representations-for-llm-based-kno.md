---
title: "RADAR: Reasoning as Discrimination with Aligned Representations for LLM-based Knowledge Graph Reasoning"
authors:
  - "Bo Xue"
  - "Yuan Jin"
  - "Luoyi Fu"
  - "Jiaxin Ding"
  - "Xinbing Wang"
date: "2026-02-25"
arxiv_id: "2602.21951"
arxiv_url: "https://arxiv.org/abs/2602.21951"
pdf_url: "https://arxiv.org/pdf/2602.21951v1"
categories:
  - "cs.CL"
tags:
  - "知识图谱推理"
  - "LLM应用"
  - "判别式推理"
  - "强化学习"
  - "表示学习"
  - "泛化能力"
relevance_score: 6.5
---

# RADAR: Reasoning as Discrimination with Aligned Representations for LLM-based Knowledge Graph Reasoning

## 原始摘要

Knowledge graph reasoning (KGR) infers missing facts, with recent advances increasingly harnessing the semantic priors and reasoning abilities of Large Language Models (LLMs). However, prevailing generative paradigms are prone to memorizing surface-level co-occurrences rather than learning genuine relational semantics, limiting out-of-distribution generalization. To address this, we propose RADAR, which reformulates KGR from generative pattern matching to discriminative relational reasoning. We recast KGR as discriminative entity selection, where reinforcement learning enforces relative entity separability beyond token-likelihood imitation. Leveraging this separability, inference operates directly in representation space, ensuring consistency with the discriminative optimization and bypassing generation-induced hallucinations. Across four benchmarks, RADAR achieves 5-6% relative gains on link prediction and triple classification over strong LLM baselines, while increasing task-relevant mutual information in intermediate representations by 62.9%, indicating more robust and transferable relational reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的知识图谱推理中存在的泛化能力不足问题。研究背景是知识图谱通常不完整，需要推理缺失事实。传统基于嵌入的方法虽能利用图结构，但在数据稀疏时效果受限，且难以捕捉超越局部拓扑的细粒度关系语义。因此，近期研究转向利用大语言模型的语义先验和推理能力。

现有方法，尤其是主流的大语言模型生成式范式，将知识图谱推理形式化为序列建模，通过优化序列化三元组的下一词元似然进行训练。这种方法的不足在于，它鼓励模型走“捷径”：模型倾向于记忆实体名称与关系之间的表层共现统计规律，而非学习真正的关系条件化有效性。这导致模型在分布内数据上表现良好，但在遇到训练时未见的实体-关系组合（即分布外泛化）时，由于共现统计失效，性能会显著下降。监督微调进一步加剧了这一问题，其交叉熵目标强化了词元级模仿，而非关系推理。

因此，本文要解决的核心问题是：如何突破基于表层共现的生成式模式匹配的局限，使大语言模型能够进行真正可泛化的关系推理。论文提出的RADAR方法通过将知识图谱推理重新定义为判别式实体选择任务，将学习信号从词元级模仿转向对正确答案与困难干扰项之间的相对可分离性优化，从而迫使模型学习更具鲁棒性的关系语义，以实现更好的分布外泛化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于嵌入的方法、基于LLM的生成式推理方法，以及判别式推理方法。

在**基于嵌入的方法**（如TransE、RotatE）中，模型通过将实体和关系映射到低维向量空间来学习图结构，但这类方法通常难以捕捉细粒度的语义信息，且在数据稀疏时表现受限。本文指出，这些方法主要依赖局部拓扑结构，而未能充分利用丰富的语义先验。

在**基于LLM的生成式推理方法**中，近期研究将知识图谱推理视为序列生成任务，通过监督微调（SFT）让LLM直接生成实体名称。然而，本文批判性地指出，这类方法（如KG-BERT、StAR等）容易陷入“表面共现捷径”：模型仅记忆实体与关系在文本中的共现模式，而非学习真正的条件关系语义，导致分布外泛化能力差。本文的RADAR方法正是为了克服这一根本缺陷而提出。

在**判别式推理方法**方面，已有一些工作将推理视为分类或排序问题（例如在候选实体中进行选择）。本文的RADAR与这类思路有相似之处，但关键区别在于：RADAR通过强化学习（而非传统的交叉熵损失）来优化实体间的相对可分离性，并将训练目标与基于表示空间的推理方式严格对齐，从而避免了生成范式带来的幻觉问题，实现了从“模式匹配”到“关系推理”的范式转变。

### Q3: 论文如何解决这个问题？

论文通过提出RADAR框架，将知识图谱推理从生成式模式匹配重构为判别式关系推理，以解决现有生成式方法易记忆表层共现而非学习真实关系语义的问题。其核心方法、架构设计和关键技术如下：

**整体框架与核心方法**：RADAR将链接预测和三元组分类任务重新定义为在受限候选空间内的判别式实体选择。给定查询三元组（h, r, ?），模型不再生成文本序列，而是从一个包含正例（真实尾实体）和负例（干扰实体）的候选集合中选出正确答案。这一重构迫使模型必须明确区分正负样本，从而优化过程聚焦于关系有效性驱动的判别性潜在结构，而非依赖表层共现的捷径。

**主要模块与训练范式**：
1.  **分层任务难度设计**：沿两个维度构建渐进式挑战：a) 答案基数（单答案 vs. 可变数量答案），以涵盖一对一和一对多关系；b) 负样本硬度，使用预训练知识图谱嵌入模型对负候选实体进行评分并分层（易、中、难），以逐步提升模型的关系推理能力。
2.  **两阶段训练**：
    *   **第一阶段：监督微调**：为每个训练实例构建包含思维链推理的提示，模型学习生成包含推理过程和最终答案的序列，以初步建立输出结构。
    *   **第二阶段：强化学习**：采用分组相对策略优化，专注于监督微调失败的实例。定义复合奖励函数，结合格式遵循奖励和基于F1分数的准确率奖励，以优化策略。这使学习信号从词元似然转向全局结果有效性，促进真正的判别能力。

**推理机制创新**：为避免自回归解码可能引入的幻觉与训练目标不匹配，RADAR在表示空间直接进行推理。对于三元组分类，从微调模型中间层的最终词元位置提取隐藏状态，并训练一个轻量级二元分类器来评估三元组的合理性。对于链接预测，采用“检索-重排序”策略：先用轻量级KGE模型检索top-n候选实体，再用学到的分类器对每个候选进行评分和排序。

**关键技术亮点**：
*   **任务自适应互信息度量**：为量化模型内部表示中捕获的判别性关系信号，提出一种新的互信息度量。它利用已训练的分类器权重矩阵来定义投影方向，聚焦于对KGR任务最具有判别性的子空间，从而更准确地评估表示中任务相关信息的丰富程度。

综上，RADAR通过任务重构、分层难度训练、两阶段优化（SFT+RL）以及表示空间直接推理，系统性地引导大语言模型学习并利用判别性关系语义，实现了更鲁棒和可泛化的知识图谱推理。

### Q4: 论文做了哪些实验？

论文在四个基准数据集上进行了链接预测和三元组分类实验。实验设置方面，以LLaMA为骨干模型，采用可变答案设置和Tier 2负采样。数据集包括用于链接预测的FB15K-237和FB15K-237N，以及用于三元组分类的WN18RR、UMLS和FB15K-237N。对比方法分为两类：知识图谱嵌入模型（如TransE、DistMult、ComplEx、RotatE、ConvE、TuckER）和基于语言模型的方法（如KG-BERT、SimKGC、CSPromp-KG、COSIGN、KG-LLAMA、FLAME、KoPA等）。评估指标包括链接预测的平均倒数排名（MRR）和Hits@k（k=1,3,10），以及三元组分类的准确率。

主要结果显示，RADAR在链接预测任务上取得了最佳性能。在FB15K-237上，MRR达到0.377，比之前最佳模型COSIGN相对提升2.4%；在更具挑战性的FB15K-237N上，MRR为0.415，相对提升5.3%。在三元组分类任务上，RADAR在WN18RR和FB15K-237N上准确率最高（分别为95.3%和81.6%），在UMLS上为91.7%，仅次于KoPA。与仅使用LLM的基线（KG-LLAMA和FLAME）相比，RADAR在三个数据集上平均相对提升约6%。

消融实验表明，将推理范式从生成式转换为判别式（Discriminative-SFT-Extraction）比序列化SFT基线平均提升3.9%；结合两阶段训练（Discriminative-Full-Extraction）后，相对提升达6.5%。此外，中间表示的任务自适应互信息提升了62.9%，表明表示空间包含了更丰富的任务相关信息。在不同LLM骨干（如Pythia-6.9B、Qwen3-8B）上的实验也验证了方法的鲁棒性，例如在Qwen3-8B上MRR相对提升6.0%。归纳泛化实验显示，在实体不相交设置下，RADAR对未见实体三元组的分类性能显著优于基线，尤其在归纳率为40%时表现更稳定。

### Q5: 有什么可以进一步探索的点？

该论文提出的RADAR方法虽然提升了知识图谱推理的泛化能力，但仍存在两个主要局限性：一是采用“检索-重排”范式，受限于候选实体检索的召回率瓶颈，可能遗漏正确答案；二是基于强化学习的判别式对齐训练成本较高，效率低于常规微调。未来研究可从以下方向深入：首先，可探索无需检索的端到端推理机制，例如通过更精细的表示学习直接建模全局实体关系，避免召回限制。其次，可研究更高效的训练方法，如利用课程学习或蒸馏技术降低强化学习复杂度，或结合对比学习增强表示的可分性。此外，论文强调提升了任务相关互信息，未来可进一步验证所学表示的跨任务迁移能力，例如应用于少样本或零样本场景，以检验其语义泛化的鲁棒性。最后，可考虑将判别式推理与生成式方法的优势结合，构建混合框架，在复杂推理路径中灵活切换模式，以处理更动态的知识图谱。

### Q6: 总结一下论文的主要内容

该论文提出RADAR框架，将基于大语言模型的知识图谱推理从生成式范式重构为判别式关系推理。核心问题是传统生成方法容易记忆表面共现而非学习真实关系语义，导致分布外泛化能力受限。方法上，RADAR将知识图谱推理重新定义为判别式实体选择任务，利用强化学习增强实体表示的可分离性，使推理直接在表示空间中进行，避免生成过程中的幻觉问题。实验表明，RADAR在四个基准上实现了链接预测和三重分类5-6%的相对性能提升，同时中间表示的任务相关互信息增加62.9%，证明了其学习更鲁棒、可迁移关系语义的能力。该工作的意义在于为基于大语言模型的知识图谱推理提供了一条更可靠、可泛化的新路径。
