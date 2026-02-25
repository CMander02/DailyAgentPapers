---
title: "Proximity-Based Multi-Turn Optimization: Practical Credit Assignment for LLM Agent Training"
authors:
  - "Yangyi Fang"
  - "Jiaye Lin"
  - "Xiaoliang Fu"
  - "Cong Qin"
  - "Haolin Shi"
  - "Chang Liu"
  - "Peilin Zhao"
date: "2026-02-22"
arxiv_id: "2602.19225"
arxiv_url: "https://arxiv.org/abs/2602.19225"
pdf_url: "https://arxiv.org/pdf/2602.19225v1"
categories:
  - "cs.AI"
tags:
  - "Agent Training"
  - "Credit Assignment"
  - "Policy Optimization"
  - "Multi-Turn Agent"
  - "LLM Agent"
  - "Reinforcement Learning"
  - "Sample Efficiency"
relevance_score: 9.0
---

# Proximity-Based Multi-Turn Optimization: Practical Credit Assignment for LLM Agent Training

## 原始摘要

Multi-turn LLM agents are becoming pivotal to production systems, spanning customer service automation, e-commerce assistance, and interactive task management, where accurately distinguishing high-value informative signals from stochastic noise is critical for sample-efficient training. In real-world scenarios, a failure in a trivial task may reflect random instability, whereas success in a high-difficulty task signifies a genuine capability breakthrough. Yet, existing group-based policy optimization methods rigidly rely on statistical deviation within discrete batches, frequently misallocating credit when task difficulty fluctuates. To address this issue, we propose Proximity-based Multi-turn Optimization (ProxMO), a practical and robust framework engineered specifically for the constraints of real-world deployment. ProxMO integrates global context via two lightweight mechanisms: success-rate-aware modulation dynamically adapts gradient intensity based on episode-level difficulty, while proximity-based soft aggregation derives baselines through continuous semantic weighting at the step level. Extensive evaluations on ALFWorld and WebShop benchmarks demonstrate that ProxMO yields substantial performance gains over existing baselines with negligible computational cost. Ablation studies further validate the independent and synergistic efficacy of both mechanisms. Crucially, ProxMO offers plug-and-play compatibility with standard GRPO frameworks, facilitating immediate, low-friction adoption in existing industrial training pipelines. Our implementation is available at: \href{https://anonymous.4open.science/r/proxmo-B7E7/README.md}{https://anonymous.4open.science/r/proxmo}.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多轮LLM智能体训练中的**信用分配**问题。现有方法（如GRPO）在训练智能体处理复杂交互任务时，通常依赖组内统计偏差（如z-score归一化）来分配学习信号。然而，在实际部署场景中，任务难度差异巨大，导致结果（成功或失败）所蕴含的信息价值高度依赖于上下文背景。例如，在一个高成功率任务中的失败可能只是随机噪声，而在一个低成功率任务中的成功却可能代表能力突破。现有方法忽略了这种上下文依赖性，仅基于统计位置均等地分配优势值，从而错误地分配了信用，降低了训练效率。

具体而言，论文指出了两个层面的问题：1) **在回合层面**，传统方法无法区分相同统计偏差下不同成功率任务所蕴含的不同信息价值；2) **在步骤层面**，基于硬边界（如精确匹配或相似度阈值）的分组方法存在固有缺陷：严格标准会导致单例组而无法比较，宽松标准则会对语义不相关的状态进行平等加权。

为此，论文提出了ProxMO框架，通过两个轻量级机制引入全局上下文信息来改进信用分配：在回合层面，**成功率感知调制**根据任务难度动态调整梯度强度；在步骤层面，**基于邻近度的软聚合**通过连续的语义加权来估计基线，取代了硬边界划分。该方法旨在更准确地区分高价值信号与随机噪声，实现更高效的样本训练。

### Q2: 有哪些相关研究？

本文的研究与多智能体强化学习中的信用分配问题密切相关。相关工作主要分为两类：一是基于组的策略优化方法，如GRPO（Group Relative Policy Optimization），它通过组内轨迹回报的统计偏差（如均值和标准差）来计算优势函数，无需价值网络，具有高效和可扩展的优点。然而，这类方法在任务难度波动时，容易因组内统计偏差的刚性而错误分配信用。二是更传统的基于价值函数或评论家网络的方法（如PPO、A2C），它们能提供更细粒度的信用评估，但计算成本高且训练不稳定，不适用于大规模LLM智能体训练。

本文提出的ProxMO框架直接建立在GRPO的基础上，旨在解决其核心局限。ProxMO通过引入两个轻量级机制来整合全局上下文：1）成功率感知调制，根据回合级难度动态调整梯度强度；2）基于邻近度的软聚合，在步骤级通过连续语义加权推导基线。因此，本文与GRPO的关系是改进与扩展，它保留了GRPO无需评论家网络、内存高效的优点，同时通过融入难度感知和语义邻近性，实现了更鲁棒和精确的信用分配，从而提升了在多变任务场景下的样本效率和性能。

### Q3: 论文如何解决这个问题？

论文提出的ProxMO框架通过两个层次化的轻量级机制来解决多轮LLM智能体训练中的信用分配问题，核心是动态适应任务难度并消除离散分组边界。

在情节层面，设计了**成功率感知的优势调制**机制。传统GRPO方法对同一批次内所有轨迹的回报进行z-score归一化，无论任务难易，优势值幅度相同。ProxMO引入极化信号控制器，根据情节组的经验成功率\(p\)动态调整梯度强度。对于成功轨迹（R=1），在低成功率组（难度高）中放大其优势信号，以巩固罕见的突破；对于失败轨迹（R=0），在高成功率组（难度低）中衰减其优势信号，以减少随机噪声带来的惩罚。通过一个基于Sigmoid函数的权重\(w(R, p)\)对标准化的优势值进行调制，实现了对任务难度的自适应。

在步骤层面，提出了**基于邻近度的软聚合**机制。传统方法通过精确匹配或相似度阈值进行硬边界分组，容易产生单例组或混淆语义差异大的状态。ProxMO摒弃离散分组，为每个状态\(s_t^{(i)}\)计算其后续折扣回报\(R_t^{(i)}\)，然后通过语义邻近度加权聚合所有同任务状态下的回报，形成软基线\(B_t^{(i)}\)。具体使用TF-IDF向量表示状态并计算余弦相似度，再通过温度缩放softmax计算权重\(w_{ij}\)。步骤级优势\(A^S\)即为当前回报与软基线之差。该方法实现了连续、平滑的信用分配，能更精细地区分同一轨迹内不同动作的质量。

最后，将调制后的情节级优势\(\tilde{A}^E\)与步骤级优势\(A^S\)通过加权求和结合，形成统一优势信号用于PPO策略优化。该方法计算开销小，且与现有GRPO框架即插即用，在ALFWorld和WebShop基准测试中显著超越了现有基线。

### Q4: 论文做了哪些实验？

论文在ALFWorld和WebShop两个多轮交互基准上进行了实验。实验设置方面，使用Qwen2.5-1.5B/7B-Instruct模型作为骨干，对比了闭源LLM（GPT-4o、Gemini-2.5-Pro）、提示型智能体（ReAct、Reflexion）以及强化学习训练方法（GRPO、GiGPO）等基线。

主要结果：ProxMO在所有基线和任务类型上均取得了一致的性能提升，尤其在需要精确信用分配的长视野任务（如Look、Cool、Pick2）中优势显著。训练后的小模型（1.5B/7B）在性能上匹配甚至超越了领先的闭源LLM。

此外，论文进行了消融研究，验证了其两个核心机制（episode-level modulation和step-level aggregation）各自的有效性与协同效应；超参数敏感性分析表明ProxMO在广泛的参数配置下保持稳定高性能；计算效率对比显示，ProxMO仅带来约1.09%的额外开销，几乎不影响训练吞吐量；案例研究则通过一个复杂的多对象任务，直观展示了ProxMO在避免目标漂移和错误级联方面的优势。

### Q5: 有什么可以进一步探索的点？

本文提出的ProxMO方法在资源受限的工业部署场景（如1.5B和7B模型）中验证有效，但其主要局限性在于尚未在更大规模的基础模型（如百亿或千亿参数级别）上进行测试。未来研究的一个关键方向是，将ProxMO框架扩展到这些超大模型上，以严格验证其性能增益和核心机制（如基于成功率的梯度调制和基于语义邻近的软聚合）在不同模型容量谱系中的普适性与可扩展性。此外，虽然论文在ALFWorld和WebShop基准上进行了评估，但未来可探索该方法在更复杂、开放域的多轮对话或具身智能任务中的表现，以进一步检验其鲁棒性。另一个潜在方向是探究如何将任务难度评估与更细粒度的步骤级奖励信号相结合，以优化信用分配。

### Q6: 总结一下论文的主要内容

这篇论文提出了ProxMO框架，旨在解决多轮LLM智能体训练中的信用分配难题。其核心贡献在于通过两个轻量级机制引入全局上下文信息，以更精准地区分任务表现中的有效信号与随机噪声。具体而言，在回合层面，框架根据任务成功率动态调整梯度强度，对高成功率任务组抑制噪声，对低成功率任务组则放大突破性进展；在步骤层面，它采用基于语义邻近度的连续加权进行软聚合，取代了传统基于离散批次的硬边界方法，从而避免了单一样本偏差。实验表明，该框架在ALFWorld和WebShop基准测试上显著提升了性能，且计算开销极小。其重要意义在于，ProxMO具备即插即用特性，能无缝集成到现有的工业级训练流程中，为实际部署中的多轮强化学习提供了更稳定、高效的优化方案。
