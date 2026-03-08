---
title: "Securing the Floor and Raising the Ceiling: A Merging-based Paradigm for Multi-modal Search Agents"
authors:
  - "Zhixiang Wang"
  - "Jingxuan Xu"
  - "Dajun Chen"
  - "Yunfang Wu"
  - "Wei Jiang"
date: "2026-03-02"
arxiv_id: "2603.01416"
arxiv_url: "https://arxiv.org/abs/2603.01416"
pdf_url: "https://arxiv.org/pdf/2603.01416v1"
categories:
  - "cs.AI"
tags:
  - "Tool Use & API Interaction"
  - "Multi-Agent Systems"
relevance_score: 7.5
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Multi-Agent Systems"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "Optimal Brain Merging (OBM)"
  primary_benchmark: "InfoSeek, MMSearch"
---

# Securing the Floor and Raising the Ceiling: A Merging-based Paradigm for Multi-modal Search Agents

## 原始摘要

Recent advances in Vision-Language Models (VLMs) have motivated the development of multi-modal search agents that can actively invoke external search tools and integrate retrieved evidence through multi-step reasoning. While promising, existing approaches typically rely on large-scale supervised trajectories or expensive reinforcement learning (RL), leading to high training cost, instability, and a severe cold-start problem for standard VLMs. We propose a training-free paradigm to empower VLMs with autonomous search capabilities via cross-modal model merging. By fusing a text-based search agent with a base VLM, we show that multi-modal search capabilities can be effectively composed without any additional multi-modal training data. To mitigate parameter interference during cross-modal integration, we introduce Optimal Brain Merging (OBM), a saliency-aware merging algorithm that identifies task-critical parameters based on their impact on model loss using only a small set of calibration samples. Extensive experiments on search-intensive benchmarks (e.g., InfoSeek, MMSearch) reveal that: (1) Model merging secures a reasonable performance floor as a zero-shot agent, with OBM achieving superior search rates; (2) OBM significantly raises the performance ceiling as a warm-start strategy, achieving faster convergence and higher peak accuracy than standard VLM initialization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决构建多模态搜索代理（multi-modal search agents）时面临的高成本、不稳定性和冷启动问题。研究背景是，随着视觉-语言模型（VLMs）的发展，能够主动调用外部搜索工具并进行多步推理的多模态搜索代理成为新兴方向，在开放域视觉问答、事实验证等应用中至关重要。然而，现有方法通常依赖大规模监督轨迹或强化学习（RL），导致训练成本高昂、过程不稳定，且标准VLMs缺乏内在搜索行为，造成严重的冷启动问题——即模型需从零开始学习工具使用策略，限制了研究的可访问性和可复现性。

现有方法的不足在于：它们需要昂贵的端到端多模态训练数据或复杂的RL优化，而许多所需能力（如视觉感知和工具使用）实际上已分散在不同类型的预训练模型（如VLMs和大型语言模型）中，但缺乏有效整合这些能力的机制。因此，本文的核心问题是如何在不进行额外多模态训练的情况下，将视觉理解与复杂推理能力高效融合，构建出能自主搜索的多模态代理。为此，论文提出一种基于跨模态模型合并的训练免费范式，通过参数级融合将基于文本的搜索代理与基础VLM结合，并引入最优大脑合并（OBM）算法来缓解跨模态集成中的参数干扰，从而在零样本设置下建立更高的性能下限，并为下游RL提供热启动，提升训练效率和峰值性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：模型融合方法、多模态搜索代理的构建方法，以及算法理论基础。

在**模型融合方法**方面，早期工作如Task Arithmetic（TA）通过线性组合微调后的“任务向量”来融合模型能力。后续研究如TIES和DARE通过修剪、符号共识或随机稀疏化来解决参数干扰问题，但这些方法主要针对单模态（如文本）场景，依赖权重幅度或随机策略，可能不适用于需要精细对齐的跨模态架构。近期研究开始探索将大型语言模型（LLM）与视觉语言模型（VLM）融合以增强特定领域推理，但主要评估单轮推理任务，未考虑自主工具使用的复杂性。**本文与这些工作的区别在于**，首次将模型融合应用于构建**多模态搜索代理**，专注于无缝整合视觉感知与多步搜索推理逻辑，并提出了新的OBM算法来优化跨模态融合。

在**多模态搜索代理构建**方面，现有方法通常依赖大规模监督轨迹或昂贵的强化学习（RL），如MMSearch-R1框架通过微调VLM来执行搜索推理，而WebWatcher等大型系统利用海量数据和多种工具构建通用研究代理。**本文与这些工作的关系是**都旨在开发具备视觉感知和工具使用能力的代理，但**区别在于**本文提出一种无需训练的融合范式，通过组合现有任务专家来构建专用搜索代理，避免了高昂训练成本，并可作为后续RL的优质起点。

在**算法理论基础**上，本文提出的OBM算法灵感源于经典剪枝和量化文献，如Optimal Brain Damage（OBD）利用二阶泰勒展开（Hessian矩阵）识别对损失函数影响显著的参数，以及GPTQ等现代量化方法利用激活感知的Hessian信息。**本文与这些工作的关系是**借鉴了其显著性感知视角，但**区别在于**将这一思想适配到模型融合领域，基于参数对跨模态推理的实际贡献（而非简单数值大小）来识别任务关键参数。

### Q3: 论文如何解决这个问题？

论文通过一种基于模型融合的无训练范式，赋予视觉语言模型（VLM）自主搜索能力，核心方法是跨模态模型融合与创新的最优大脑融合（OBM）算法。

整体框架分为两步：首先，构建一个多模态搜索代理的基础架构。该方法基于一个关键观察：文本搜索代理（如Search-R1）和基础VLM（如Qwen2.5-VL）的语言模块共享同一个基础模型（Qwen2.5-7B）。因此，通过定义并融合两者的任务向量（即微调后参数与基础参数的差值），可以将文本搜索代理的推理能力“移植”到VLM上。具体而言，将VLM的视觉编码器和投影器直接接入融合后的系统，而语言模块的初始权重则通过任务算术进行线性组合：θ_merged = θ_B + λ_S δ_S + λ_V δ_V。这确保了模型既能处理视觉输入，又能继承工具调用和推理逻辑。

然而，简单的线性融合会因参数干扰导致性能下降。为此，论文提出了创新的OBM算法，这是一个包含两个阶段的显著性感知融合框架：
1.  **显著性驱动的稀疏化**：核心思想是剪枝对模型损失影响微小的任务向量参数。OBM通过二阶泰勒展开近似计算每个参数的重要性（显著性），但为避免计算完整海森矩阵的巨大开销，采用了基于层均方误差的近似方法。对于第l层线性层，其海森矩阵简化为H^l = 2X^l (X^l)^⊤，其中X^l是使用少量校准样本（多模态VQA数据用于δ_V，搜索推理数据用于δ_S）前向传播得到的输入激活。这一设计的关键在于，δ_V的显著性计算动态地捕获了语言骨干与冻结视觉模块之间的激活感知依赖关系，从而弥合了模态间的鸿沟。最终，每个任务向量仅保留显著性最高的前p%参数。
2.  **显著性加权的符号共识**：当两个任务向量的参数方向发生冲突时，传统方法仅比较幅度大小。OBM则引入加权共识机制，根据每个任务在该参数上的相对重要性（即显著性）来决定最终方向。共识方向由σ_i = sign( Σ s_i^(k) · sign(δ_i^(k)) ) 确定，并依此构建最终的融合任务向量，确保对“多模态协同”至关重要的参数以其正确的任务特定方向被保留。

主要创新点在于：1）提出了一种无需额外多模态训练数据、通过模型融合构建多模态搜索代理的新范式；2）设计了OBM算法，它利用少量校准数据高效计算参数显著性，解决了跨模态融合中的参数干扰问题，实现了更精准的能力组合。

### Q4: 论文做了哪些实验？

论文实验分为训练前（零样本）和训练后两个阶段，以评估基于模型融合的多模态搜索代理范式的性能。

**实验设置与基准**：实验在四个搜索密集型视觉问答基准上进行：FVQA-test、InfoSeek、MMSearch和LiveVQA。评估指标包括准确率（Acc）以及图像和文本搜索调用率（SR_img, SR_txt）。

**对比方法**：基线模型包括：直接回答的Qwen-VL（DA）、基于提示的零样本搜索代理（Qwen-VL-R1）、固定流程的检索增强生成（RAG）工作流，以及经过强化学习训练的MMSearch-R1。论文提出的融合方法包括TA、TIES、DARE以及其核心算法OBM（最优大脑融合），这些方法通过将一个基于文本的搜索代理（Search-R1）与基础视觉语言模型Qwen-VL融合来构建。

**主要结果与关键指标**：
1.  **零样本性能（保障下限）**：融合模型（特别是TA和OBM）显著优于仅靠提示的基线（Qwen-VL-R1）。例如，在MMSearch上，OBM的文本搜索率（SR_txt）高达78.94%，表明融合成功植入了搜索“本能”。OBM在多个数据集上缩小了与固定RAG流程的准确率差距。
2.  **训练后性能（提升上限）**：将融合模型作为强化学习的初始化起点，OBM展现出最快的收敛速度，仅需5步就达到其他模型1个epoch的性能。在峰值性能上，OBM在训练第44步达到最高平均准确率27.59%和平均搜索率77.77%，优于从原始Qwen-VL初始化的模型。
3.  **算法对比**：标准的单模态融合算法（如TIES和DARE）在跨模态场景下表现不佳，DARE甚至出现性能崩溃。而OBM通过基于显著性的参数融合，在保持模态对齐的同时实现了更好的泛化性能，尤其在分布外基准（如MMSearch）上表现稳健。

### Q5: 有什么可以进一步探索的点？

该论文提出的基于模型融合的无训练范式虽具创新性，但仍存在局限性，为未来研究提供了多个探索方向。首先，其核心方法OBM依赖于少量校准样本，其泛化能力在不同领域或更复杂的多模态任务中可能受限，未来可研究更鲁棒的显著性评估方法，或探索无需校准的无监督融合策略。其次，工作主要聚焦搜索工具调用，但现实场景中智能体需处理多种工具（如图像编辑、数据库查询等），未来可扩展至更广泛的工具组合与动态选择机制。此外，融合过程仅针对参数层面，未深入考虑多模态表征的对齐与交互；未来可结合轻量级适配器或引入因果干预技术，以更精细地调制跨模态信息流。最后，该范式作为RL的暖启动虽有效，但未与更先进的在线学习或元学习结合，后续可探索其在持续学习环境中的适应性，以构建更自主、通用的多模态智能体。

### Q6: 总结一下论文的主要内容

该论文提出了一种无需训练的多模态搜索智能体构建范式，通过跨模态模型融合将基于文本的搜索智能体能力迁移到视觉语言模型（VLM）中。核心问题是解决现有方法依赖大规模监督轨迹或强化学习所导致的高成本、不稳定及冷启动难题。其方法概述为：引入最优大脑融合算法，仅利用少量校准样本识别对任务损失影响显著的关键参数，从而在融合过程中减少参数干扰，实现文本搜索能力与基础VLM的有效组合。主要结论表明，该融合方法既能为零样本智能体提供可靠性能基础，又能作为热启动策略显著提升性能上限，在多个搜索密集型基准测试中实现了更高的搜索成功率和更快的收敛速度。其意义在于为多模态智能体的能力扩展提供了一种高效、低成本的免训练新路径。
