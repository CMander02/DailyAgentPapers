---
title: "Select-then-Solve: Paradigm Routing as Inference-Time Optimization for LLM Agents"
authors:
  - "Heng Zhou"
  - "Zelin Tan"
  - "Zhemeng Zhang"
  - "Yutao Fan"
  - "Yibing Lin"
  - "Li Kang"
  - "Xiufeng Song"
  - "Rui Li"
  - "Songtao Huang"
  - "Ao Yu"
  - "Yuchen Fan"
  - "Yanxu Chen"
  - "Kaixin Xu"
  - "Xiaohong Liu"
  - "Yiran Qin"
  - "Philip Torr"
  - "Chen Zhang"
  - "Zhenfei Yin"
date: "2026-04-08"
arxiv_id: "2604.06753"
arxiv_url: "https://arxiv.org/abs/2604.06753"
pdf_url: "https://arxiv.org/pdf/2604.06753v1"
categories:
  - "cs.CL"
tags:
  - "推理范式"
  - "路由选择"
  - "推理时优化"
  - "基准评测"
  - "LLM智能体"
relevance_score: 8.5
---

# Select-then-Solve: Paradigm Routing as Inference-Time Optimization for LLM Agents

## 原始摘要

When an LLM-based agent improves on a task, is the gain from the model itself or from the reasoning paradigm wrapped around it? We study this question by comparing six inference-time paradigms, namely Direct, CoT, ReAct, Plan-Execute, Reflection, and ReCode, across four frontier LLMs and ten benchmarks, yielding roughly 18,000 runs. We find that reasoning structure helps dramatically on some tasks but hurts on others: ReAct improves over Direct by 44pp on GAIA, while CoT degrades performance by 15pp on HumanEval. No single paradigm dominates, and oracle per-task selection beats the best fixed paradigm by 17.1pp on average. Motivated by this complementarity, we propose a select-then-solve approach: before answering each task, a lightweight embedding-based router selects the most suitable paradigm. Across four models, the router improves average accuracy from 47.6% to 53.1%, outperforming the best fixed paradigm at 50.3% by 2.8pp and recovering up to 37% of the oracle gap. In contrast, zero-shot self-routing only works for GPT-5 at 67.1% and fails for weaker models, all trailing the learned router. Our results argue that reasoning paradigm selection should be a per-task decision made by a learned router, not a fixed architectural choice.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在推理时面临的一个核心问题：如何为不同的任务动态选择最合适的推理范式，以最大化模型性能。研究背景是，当前LLM智能体领域涌现了多种推理范式（如直接生成、思维链、ReAct、计划-执行、反思、ReCode等），它们通过不同的推理结构和工具调用方式来包装同一个基础模型。然而，现有方法通常孤立地提出和评估单一范式，缺乏在不同任务和模型上进行严格、受控的比较，导致无法明确回答一个基本问题：额外的推理结构在何时真正有益，在何时反而有害？

现有方法的不足主要体现在两方面：首先，以往研究往往在引入新范式时，同步更改模型、提示格式、工具集和评估基准，使得性能增益的来源难以厘清——究竟是模型本身的改进，还是推理范式的功劳？其次，社区普遍缺乏对不同范式互补性的系统认识，实践中通常为智能体固定选用一种推理范式，但论文通过大规模实验发现，没有单一范式在所有任务上占优；固定范式选择会导致性能损失，因为不同任务需要不同的推理结构（例如，ReAct在需要网络搜索的任务上大幅提升性能，而思维链在代码生成任务上可能损害表现）。

因此，本文要解决的核心问题是：如何根据具体任务特性，在推理时自动选择最优的推理范式。论文提出了“先选择后解决”的方法，通过一个轻量级的、基于嵌入的路由器，在回答每个任务前分析其内容并分派至最合适的范式。这本质上将推理范式的选择从固定的架构决策，转变为基于任务的学习型决策，从而在多样化的任务上实现更优且稳定的性能提升。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：推理范式、智能体评测以及路由与自适应推理。

在**推理范式**方面，相关工作包括：Chain-of-Thought（CoT）及其变体（如零样本CoT、自洽性）、工具增强范式（如ReAct）、基于规划的方法、自我反思方法以及以代码为中心的范式（如PAL、Program-of-Thoughts、ReCode）。本文与这些工作的关系在于，它系统性地比较了这些不同的推理范式，而非单独验证某一种。区别在于，以往研究多在特定任务上验证单一范式的优势，而本文在一个统一的框架下评估了多种范式在不同任务上的表现，并揭示了它们的互补性。

在**智能体评测**方面，已有基准如AgentBench、WebArena和MINT旨在真实环境中评估完整的智能体系统。本文与这些工作的关系是都关注评估，但区别在于：这些基准将范式选择与模型、提示、工具接口等多种系统决策混杂在一起，而本文的研究重点在于隔离并专门分析“推理范式”这一单一设计轴。

在**路由与自适应推理**方面，相关工作如RouteLLM、FrugalGPT等主要研究在不同模型之间进行路由选择，以优化成本或性能。本文的“选择-解决”方法与这些工作思路相似，但关键区别在于：本文的路由器是在**固定模型**下，为同一查询选择最合适的**推理范式**，而非在不同模型之间进行选择。这开辟了一个新的、此前 largely unexplored 的测试时优化维度。

### Q3: 论文如何解决这个问题？

论文通过提出“先选择后解决”的范式路由方法来解决不同推理范式在不同任务上表现互补、没有单一范式始终最优的问题。其核心思想是在执行每个任务前，先由一个轻量级的“范式选择器”动态选择最合适的推理范式，而非固定使用单一范式。

整体框架是一个两阶段流水线。第一阶段是**范式选择器**，它接收任务文本作为输入，从六个候选推理范式（Direct、CoT、ReAct、Plan-Execute、Reflection、ReCode）中选择一个。第二阶段是**执行器**，仅运行被选中的范式来生成答案。这种方法将范式选择视为一个在推理时进行的优化决策。

关键技术在于路由器的设计与训练。论文评估了三种路由策略：
1.  **基于手工特征的分类器**：使用22个手工制作的特征（如数据集标识、文本统计量、内容检测器），训练逻辑回归或两层MLP分类器。这本质上是一种按数据集多数投票的方法。
2.  **基于嵌入的分类器**：使用文本嵌入模型（text-embedding-3-small）将任务文本编码为1536维向量，并可选地与手工特征拼接，再训练分类器。这能直接利用任务语义进行更精细的判别。
3.  **零样本自路由**：直接提示大语言模型自身阅读任务并选择范式，无需训练。

主要创新点包括：
*   **将范式选择建模为可学习的路由问题**：通过数据驱动的方式，让路由器学习任务特征与最优范式之间的映射，从而自动适应不同任务需求。
*   **轻量级、低成本的实现**：基于嵌入的路由器仅需一次嵌入API调用，且由于能选择更高效的范式（如常选Direct），平均token成本远低于始终使用复杂范式（如ReAct）。
*   **揭示了范式选择是一种独立的元推理能力**：实验表明，即使模型能执行某个范式，也未必能正确选择何时使用它。零样本自路由仅在最强模型（GPT-5）上有效，在较弱模型上会严重失效（如过度选择ReAct），而学习型路由器能为不同能力的模型生成适配的范式分布，显著且稳定地提升性能。

最终，结合嵌入与手工特征的逻辑回归路由器取得了最佳效果，平均准确率从直接回答的47.6%提升至53.1%，优于最佳固定范式（50.3%），并恢复了高达37%的“预言家”性能差距。这证明了学习型范式路由作为推理时优化方案的有效性。

### Q4: 论文做了哪些实验？

论文进行了大规模实验以评估不同推理范式在LLM智能体上的效果。实验设置上，研究者构建了一个统一的BaseAgent框架，可灵活切换推理策略模块，并将每个任务结果缓存为JSON文件以便复现和分析。实验共涉及约18,000次运行，每个模型-范式组合评估761个任务。

数据集/基准测试涵盖了十个多样化任务：HumanEval（代码生成）、MATH500和AIME（数学推理）、HotpotQA和NQ（问答）、MMLU（知识评测）、GAIA和SEAL（需要工具使用的复杂任务）、HLE（高阶推理）以及τ-bench（工作流执行）。评估方法因数据集而异，包括代码执行、数值匹配、文本匹配和选项提取。

对比方法包括六种推理范式：Direct（直接生成）、CoT（思维链）、ReAct（推理与行动结合）、Plan-Execute（先规划后执行）、Reflection（自我反思）和ReCode（代码式推理）。实验在四个前沿LLM上进行：GPT-5、Gemini-Flash、Qwen3-Max和Qwen3-30B。

主要结果显示，不同范式在不同任务上表现差异显著。例如，在GAIA上，ReAct比Direct提升44个百分点（pp），而在HumanEval上CoT比Direct降低15pp。没有任何单一范式在所有任务上占优，任务级别的Oracle选择（即每个任务选择最佳范式）比最佳固定范式平均高出17.1pp。关键数据指标包括：在GPT-5上，ReAct在GAIA达到72%准确率，Direct在NQ为37%；Oracle分析显示，平均准确率从最佳固定范式的49.0%提升至Oracle的69.4%。此外，计算成本差异明显，Reflection的令牌使用量是Direct的9.4倍，而ReAct为4.0倍。实验还发现，推理范式对较弱模型（如Qwen3-30B）的补偿作用更显著，如在HumanEval上CoT带来46pp提升。这些结果揭示了推理范式的任务条件性互补，为后续的范式路由方法提供了依据。

### Q5: 有什么可以进一步探索的点？

基于论文内容，可以进一步探索的点包括：首先，论文的局限性在于其路由器的训练依赖于特定任务和模型的离线数据，泛化到新任务或新模型的能力尚不明确，且仅评估了六种固定范式，未考虑更动态或混合的范式组合。其次，未来研究方向可聚焦于开发更轻量、自适应的实时路由器，例如利用LLM自身进行元认知推理或在线学习，以降低对标注数据的依赖；同时，探索任务特征的更细粒度表示，如结合问题语义和模型内部状态，以提升路由精度。此外，可研究范式本身的优化，例如允许路由器在推理过程中动态切换或组合不同范式，以应对复杂多步任务。最后，将这一框架扩展到多模态或具身智能场景，验证其在不同领域的适用性，也是一个有潜力的方向。

### Q6: 总结一下论文的主要内容

该论文研究了不同推理范式对LLM智能体性能的影响，并提出了一种基于学习的动态选择方法。核心问题是：智能体性能提升究竟源于模型本身还是其外部的推理范式？研究发现，六种推理范式（如CoT、ReAct等）在不同任务上的效果差异显著，没有单一范式能始终最优，而针对每个任务进行理想选择（Oracle）能带来平均17.1个百分点的性能提升。

基于这种互补性，论文提出了“先选择后解决”的方法：在回答每个任务前，通过一个轻量级的基于嵌入的路由器自动选择最合适的推理范式。实验表明，该路由器将平均准确率从47.6%提升至53.1%，优于最佳固定范式2.8个百分点，并恢复了高达37%的理想选择差距，且计算成本仅为始终使用ReAct的一半。相比之下，零样本自我路由仅对最强模型有效，而较弱模型则无法实现，说明范式选择本身是一种独立的元推理能力。

论文的主要结论是：推理范式的选择应成为由学习型路由器做出的按任务动态决策，而非固定的架构选择。这为构建高效LLM智能体提供了新方向，即智能体无需总是依赖复杂框架，而应学会在适当场景选用适当范式。
