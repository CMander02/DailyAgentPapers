---
title: "RefLoRA: Refactored Low-Rank Adaptation for Efficient Fine-Tuning of Large Models"
authors:
  - "Yilang Zhang"
  - "Bingcong Li"
  - "Georgios B. Giannakis"
date: "2025-05-24"
arxiv_id: "2505.18877"
arxiv_url: "https://arxiv.org/abs/2505.18877"
pdf_url: "https://arxiv.org/pdf/2505.18877v3"
categories:
  - "cs.LG"
tags:
  - "模型微调"
  - "参数高效微调"
  - "LoRA"
  - "优化算法"
  - "大语言模型"
relevance_score: 5.5
---

# RefLoRA: Refactored Low-Rank Adaptation for Efficient Fine-Tuning of Large Models

## 原始摘要

Low-Rank Adaptation (LoRA) lowers the computational and memory overhead of fine-tuning large models by updating a low-dimensional subspace of the pre-trained weight matrix. Albeit efficient, LoRA exhibits suboptimal convergence and noticeable performance degradation, due to inconsistent and imbalanced weight updates induced by its nonunique low-rank factorizations. To overcome these limitations, this article identifies the optimal low-rank factorization per step that minimizes an upper bound on the loss. The resultant refactored low-rank adaptation (RefLoRA) method promotes a flatter loss landscape, along with consistent and balanced weight updates, thus speeding up stable convergence. Extensive experiments evaluate RefLoRA on natural language understanding, and commonsense reasoning tasks with popular large language models including DeBERTaV3, LLaMA-7B, LLaMA2-7B and LLaMA3-8B. The numerical tests corroborate that RefLoRA converges faster, outperforms various benchmarks, and enjoys negligible computational overhead compared to state-of-the-art LoRA variants.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大模型微调中低秩适应（LoRA）方法存在的收敛速度慢、性能下降明显的问题。随着大语言模型（LLMs）参数规模达到数十亿甚至万亿级别，传统的全参数微调在计算和内存上变得极其昂贵，使得参数高效微调（PEFT）方法成为必要。LoRA作为一种流行的PEFT方法，通过更新预训练权重矩阵的低秩子空间来降低开销，但其非唯一的低秩分解会导致权重更新不一致、不平衡，进而引发次优收敛和显著性能损失。

现有方法试图通过调整LoRA架构、动态分配秩或改进初始化策略来弥补不足，例如DoRA、AdaLoRA和PiSSA等方法。然而，这些方法要么需要精心设计梯度操作以稳定收敛，要么未能从根本上解决由低秩分解非唯一性引起的更新不一致问题。

本文的核心问题是：如何克服LoRA因非唯一分解导致的优化不稳定和性能下降。为此，论文提出了重构的低秩适应（RefLoRA）方法，其核心思想是在每一步微调中动态选择最优的低秩分解，该分解通过最小化损失函数的上界来确定。这种方法能促进更平坦的损失景观，实现一致且平衡的权重更新，从而加速稳定收敛，同时保持与先进LoRA变体相比可忽略的计算开销。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕高效微调大模型的方法展开，可分为以下几类：

**1. 参数高效微调（PEFT）方法**：LoRA（Low-Rank Adaptation）是代表性工作，通过低秩分解减少可训练参数量，降低计算和内存开销。后续出现了多种变体，如AdaLoRA（自适应调整秩）、LoRA+（采用不同学习率）等，旨在提升性能或效率。本文提出的RefLoRA属于此类改进方法，其核心区别在于解决了LoRA因低秩分解非唯一性导致的更新不一致和不平衡问题，通过每步寻找最优低秩分解来加速收敛并提升性能。

**2. 优化策略相关研究**：部分工作关注LoRA的优化动态，例如分析梯度不平衡（如$\mathbf{A}$和$\mathbf{B}$的更新幅度差异）对收敛的影响。本文与此类研究相关，但更进一步从理论上推导了损失上界，并据此设计重构策略，以促进更平坦的损失景观和平衡的权重更新，从而直接优化收敛稳定性。

**3. 大模型微调评测基准**：相关研究包括在自然语言理解、常识推理等任务上评估不同PEFT方法（如对DeBERTa、LLaMA系列模型的测试）。本文的实验设计与此类评测工作一致，通过对比RefLoRA与原始LoRA及其他先进变体，验证其在收敛速度和性能上的优势。

总体而言，RefLoRA在方法层面与LoRA及其变体直接相关，但通过引入基于理论保证的动态重构机制，解决了现有方法中更新不一致和梯度不平衡的根本局限，在保持低开销的同时实现了更优的收敛性和性能。

### Q3: 论文如何解决这个问题？

论文通过提出“重构低秩适应”（RefLoRA）方法来解决LoRA因低秩分解不唯一导致的权重更新不一致、不平衡，进而引发收敛次优和性能下降的问题。其核心思想是在每一步迭代中，动态寻找能最小化损失上界的最优低秩分解，从而获得更一致、更平衡的权重更新，并塑造一个更平坦的损失景观以加速稳定收敛。

**整体框架与核心方法**：
RefLoRA的整体框架建立在标准LoRA之上，即在微调时冻结预训练权重矩阵 \(\mathbf{W}\)，仅通过低秩矩阵 \(\mathbf{A}\) 和 \(\mathbf{B}\)（满足 \(\Delta \mathbf{W} = \mathbf{A} \mathbf{B}^\top\)）进行更新。其创新点在于，它认识到对于给定的低秩更新 \(\Delta \mathbf{W}_t = \mathbf{A}_t \mathbf{B}_t^\top\)，其分解 \((\mathbf{A}_t, \mathbf{B}_t)\) 并不唯一：任何满足 \(\mathbf{P}_t \in \text{GL}(r)\) 的变换 \((\mathbf{A}_t \mathbf{P}_t, \mathbf{B}_t \mathbf{P}_t^{-\top})\) 都产生相同的 \(\Delta \mathbf{W}_t\)。不同的 \(\mathbf{P}_t\) 对应不同的分解，但会影响梯度下降过程中 \(\mathbf{A}_t\) 和 \(\mathbf{B}_t\) 各自的更新路径，从而影响收敛效率。

**关键技术：最优重构矩阵 \(\mathbf{S}_t\) 的求解**
1.  **问题转化**：论文证明，权重更新 \(\Delta \tilde{\mathbf{W}}_t\) 本质上由一个对称正定（SPD）矩阵 \(\mathbf{S}_t := \mathbf{P}_t \mathbf{P}_t^\top\) 控制。因此，寻找最优分解转化为寻找最优的 \(\mathbf{S}_t\)。
2.  **损失上界构建与最小化**：直接最小化损失 \(\ell(\mathbf{W}_t + \Delta \tilde{\mathbf{W}}_t(\mathbf{S}_t))\) 不可行。论文在梯度 Lipschitz 连续的假设下，推导出一个关于 \(\mathbf{S}_t\) 的、可处理的损失上界。通过最小化这个上界，可以得到 \(\mathbf{S}_t\) 的闭式最优解。
3.  **闭式解**：最优解 \(\mathbf{S}_t^*\) 的核心是矩阵 \(\tilde{\mathbf{S}}_t\)，它是矩阵 \((\mathbf{A}_t^\top \mathbf{A}_t)^{-1}\) 和 \(\mathbf{B}_t^\top \mathbf{B}_t\) 的几何平均，即 \(\tilde{\mathbf{S}}_t = (\mathbf{A}_t^\top \mathbf{A}_t)^{-1} \# (\mathbf{B}_t^\top \mathbf{B}_t)\)。在大多数实际学习率 \(\eta\) 下，最优解就是 \(\tilde{\mathbf{S}}_t\)。这个选择能自动平衡低秩因子，使得 \(\tilde{\mathbf{A}}_t^\top \tilde{\mathbf{A}}_t = \tilde{\mathbf{B}}_t^\top \tilde{\mathbf{B}}_t\)。

**主要模块/组件与实现**：
*   **重构更新**：在每一步梯度下降中，不直接使用原始的 \((\mathbf{A}_t, \mathbf{B}_t)\) 进行更新，而是使用重构后的 \((\tilde{\mathbf{A}}_t = \mathbf{A}_t \mathbf{P}_t, \tilde{\mathbf{B}}_t = \mathbf{B}_t \mathbf{P}_t^{-\top})\)，其中 \(\mathbf{P}_t \mathbf{P}_t^\top = \tilde{\mathbf{S}}_t\)。
*   **与自适应优化器的兼容**：为了兼容

### Q4: 论文做了哪些实验？

论文进行了四类实验，涵盖低秩矩阵分解、自然语言理解、常识推理和图像生成任务。实验设置方面，使用了DeBERTaV3-base、LLaMA-7B、LLaMA2-7B和LLaMA3-8B等大模型，以及Stable Diffusion v1.4。数据集包括GLUE基准（包含CoLA、SST-2等8个子任务）、8个常识推理数据集（如BoolQ、PIQA等）和DreamBooth的图像生成数据。对比方法包括全参数微调（Full FT）、BitFit、多种LoRA变体（如DoRA、AdaLoRA、LoRA-Pro、LoRA-RITE、PrecLoRA、NoRA+）以及专为矩阵分解设计的ScaledGD。

主要结果如下：在低秩矩阵分解中，RefLoRA在两种学习率（0.01和0.03）下均比LoRA和ScaledGD收敛更快且更稳定。在GLUE任务上，RefLoRA（参数量1.33M）在8个数据集中5个表现最佳，平均得分达89.52，优于AdaLoRA（89.46）等其他方法；其轻量版RefLoRA-S平均得分89.19，仅下降0.33%。在LLaMA系列的常识推理任务中，RefLoRA在多数设置下领先，例如在LLaMA2-7B（r=32）上平均准确率达80.78%，高于DoRA（79.7%）和LoRA-RITE（80.1%）；在更低秩（r=16）时仍保持优势。在Stable Diffusion图像生成中，RefLoRA的微调损失（0.086）比LoRA、LoRA-Pro和LoRA-RITE分别降低14.0%、13.1%和9.5%，且生成图像细节更清晰。收敛性实验显示，RefLoRA损失下降更快更平稳，计算开销与先进LoRA变体相比可忽略。

### Q5: 有什么可以进一步探索的点？

本文提出的RefLoRA方法通过动态优化低秩分解来提升LoRA的收敛速度和性能，但仍存在一些局限性和值得探索的方向。首先，该方法在理论分析中依赖于损失上界的优化，但实际任务中该上界可能不够紧致，未来可结合更精确的理论框架（如信息几何或流形学习）来指导分解过程。其次，实验主要集中于自然语言理解任务，未来可扩展到多模态、强化学习或大规模视觉模型，验证其泛化能力。此外，RefLoRA的分解过程虽计算开销小，但在超大规模模型（如千亿参数）中动态调整的稳定性仍需验证，可探索自适应秩选择机制或与稀疏化技术结合，以进一步提升效率。最后，当前方法未充分考虑硬件异构环境下的部署优化，未来可研究轻量级实时重构算法，使其更适合边缘设备应用。

### Q6: 总结一下论文的主要内容

该论文针对低秩适应（LoRA）方法在微调大模型时存在的收敛次优和性能下降问题，提出了一种重构的低秩适应方法（RefLoRA）。核心问题是LoRA的非唯一低秩分解会导致权重更新不一致和不平衡，从而影响训练效果。为此，作者提出了一种新的优化方法：在每一步中寻找能够最小化损失上界的最优低秩分解。这种方法通过促进更平坦的损失景观，实现更一致和平衡的权重更新，从而加速稳定收敛。实验在DeBERTaV3、LLaMA等多个大语言模型上进行，覆盖自然语言理解和常识推理任务。结果表明，RefLoRA相比现有LoRA变体，收敛速度更快，性能更优，且计算开销几乎可忽略。其核心贡献在于从理论上优化了低秩分解过程，显著提升了微调的效率和效果。
