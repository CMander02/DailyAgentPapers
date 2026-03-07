---
title: "Confidence-Calibrated Small-Large Language Model Collaboration for Cost-Efficient Reasoning"
authors:
  - "Chuang Zhang"
  - "Zizhen Zhu"
  - "Yihao Wei"
  - "Bing Tian"
  - "Junyi Liu"
date: "2026-03-04"
arxiv_id: "2603.03752"
arxiv_url: "https://arxiv.org/abs/2603.03752"
pdf_url: "https://arxiv.org/pdf/2603.03752v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Learning & Optimization"
relevance_score: 7.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "Llama-3.1-8B, Llama-3.1-70B, Qwen-2.5-7B, Qwen-2.5-72B"
  key_technique: "COREA (Collaborative REAsoner) with RL-based confidence calibration"
  primary_benchmark: "GSM8K, MATH, ARC, MMLU, BBH"
---

# Confidence-Calibrated Small-Large Language Model Collaboration for Cost-Efficient Reasoning

## 原始摘要

Large language models (LLMs) demonstrate superior reasoning capabilities compared to small language models (SLMs), but incur substantially higher costs. We propose COllaborative REAsoner (COREA), a system that cascades an SLM with an LLM to achieve a balance between accuracy and cost in complex reasoning tasks. COREA first attempts to answer questions using the SLM, which outputs both an answer and a verbalized confidence score. Questions with confidence below a predefined threshold are deferred to the LLM for more accurate resolution. We introduce a reinforcement learning-based training algorithm that aligns the SLM's confidence through an additional confidence calibration reward. Extensive experiments demonstrate that our method jointly improves the SLM's reasoning ability and confidence calibration across diverse datasets and model backbones. Compared to using the LLM alone, COREA reduces cost by 21.5% and 16.8% on out-of-domain math and non-math datasets, respectively, with only an absolute pass@1 drop within 2%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在复杂推理任务中性能优越但推理成本高昂，而小型语言模型（SLM）成本较低但推理能力不足之间的矛盾。研究背景是，随着思维链（CoT）等技术的应用，LLM的推理能力显著提升，但其生成冗长推理步骤导致了极高的计算开销，阻碍了大规模实际部署。现有方法存在明显不足：一方面，通过知识蒸馏训练SLM虽能降低成本，但其固有能力上限导致在复杂任务上准确率不足；另一方面，在单一模型内部进行自适应计算或动态推理等优化，虽能提升效率，但受限于模型本身容量且常需修改架构。此外，基于路由的方法试图将问题分配给不同规模的模型，但通常依赖外部分类器或启发式规则，难以准确捕捉模型内在的推理置信度。

因此，本文要解决的核心问题是：能否设计一种协作系统，有效结合SLM的成本效益与LLM的准确性和鲁棒性，从而在保持高整体准确率的同时显著降低运营成本？具体而言，论文提出了名为COREA的协作推理系统，其核心挑战在于使SLM能够“自知”——即准确评估自身能力边界，并基于量化的置信度决定是否将难题推迟给LLM处理。这需要解决SLM当前“不知其知，亦不知其不知”的关键缺陷，实现成本与精度之间的高效平衡。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕高效推理和置信度校准两大方向展开，可分为以下几类：

**1. 高效推理方法**：主要包括单模型优化、小模型增强和模型协作。单模型优化通过自适应计算或动态推理来减少开销，但需要修改架构且受限于模型能力。小模型增强通过知识蒸馏或微调来提升效率，但蒸馏后的小模型在复杂问题上仍表现不佳且容易过度自信。模型协作（如查询级路由或细粒度级联）将任务在大小模型间分配，但通常依赖外部分类器或引入额外采样开销。本文提出的COREA系统属于模型协作范畴，但通过直接校准小模型内部置信度进行路由，无需外部模块。

**2. 置信度校准研究**：由于小模型常存在校准不足问题，相关研究旨在提升其自我评估能力。早期工作通过提示工程让模型表达不确定性，但校准效果受任务和模板影响大。基于自省的方法利用隐藏状态或辅助分类器检测错误，但泛化到分布外任务较难。训练校准方法将校准目标（如Brier分数）融入学习过程。本文采用类似的训练思路，但提出了多种不同的校准奖励设计，并进行了全面比较，以强化小模型的置信度与准确性的对齐。

本文与这些工作的核心区别在于：它通过强化学习训练，将置信度校准直接整合到小模型的训练目标中，从而实现更可靠的路由决策，在降低成本的同时保持较高的推理精度，且无需依赖外部分类器或复杂采样机制。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为COREA的级联协作系统来解决大语言模型成本高与小语言模型能力不足之间的矛盾。其核心方法是让小语言模型（SLM）先尝试解题，并输出答案及一个量化的置信度分数；只有当置信度低于预设阈值时，才将问题转交给大语言模型（LLM）处理，从而在保证整体准确率的同时显著降低调用昂贵LLM的频率。

整体框架采用级联架构，主要包含两个模块：SLM作为第一级处理器，LLM作为第二级备用处理器。SLM被设计为生成包含推理步骤、最终答案以及一个介于0.0到1.0之间的置信度分数的结构化输出。系统通过一个固定的置信度阈值进行决策：若置信度高于阈值，则直接采纳SLM的答案；否则，问题被传递给LLM。

关键技术在于对SLM的强化学习训练算法，称为“带置信度校准的强化学习”。该方法在传统的可验证奖励（用于提升推理正确性）基础上，引入了额外的置信度校准奖励和格式奖励。复合奖励函数由三部分组成：答案正确性奖励（二元判断）、格式奖励（确保输出结构符合要求）以及置信度奖励。置信度奖励的核心创新在于，它鼓励SLM输出的置信度分数与其实际正确概率对齐，通过计算负距离（如L1距离、L2距离或KL散度）来实现。由于真实正确概率未知，论文采用组级估计法：对同一问题采样多个SLM回答，用该组回答的准确率作为概率估计值，并统一用于组内所有样本的置信度奖励计算。这种方法与依赖单个样本正确性的样本级估计形成对比，旨在实现更稳定的置信度校准。

最终，该系统通过这种协同设计和专门的训练机制，在多个数据集上同时提升了SLM的推理能力和置信度校准质量，实现了成本（降低16.8%-21.5%）与性能（准确率下降控制在2%以内）的高效平衡。

### Q4: 论文做了哪些实验？

论文在多个数据集上进行了广泛的实验，以评估所提出的COREA系统在平衡推理准确性与成本方面的有效性。

**实验设置**：核心是级联系统，其中小型语言模型（SLM）首先尝试回答问题并输出答案及置信度分数，若置信度低于预设阈值，则问题被推迟给大型语言模型（LLM）处理。SLM主要使用Qwen2.5-7B-Instruct，并在消融研究中评估了Qwen2.5-1.5B-Instruct和Llama3.1-8B-Instruct；LLM使用Qwen2.5-32B-Instruct。训练基于强化学习（使用GRPO框架），通过置信度校准奖励来对齐SLM的置信度。

**数据集/基准测试**：使用DeepMath-103K构建训练集（DeepMath16K）和领域内评估集（DeepMath500）。领域外（OOD）评估包括数学推理数据集（Math500、GSM8K、OlympiadBench）和非数学推理数据集（GPQA、CommonsenseQA）。评估指标包括准确率（Pass@1）、平均成本（Avg Cost）、LLM使用百分比（LLM%），以及针对SLM的预期校准误差（ECE）和AUROC。

**对比方法**：包括独立模型（原始SLM、经过RLVR/Brier/L1奖励训练的SLM、基线LLM）和多种协作系统（如SLM-Verb、RLVR-SLM-Verb、RLVR-SLM-AvgProb、RLVR-SLM-Probe、Router+RLVR-SLM、Brier-SLM-Verb等），这些系统在SLM和置信度生成方法上有所不同。

**主要结果与关键指标**：在将置信度阈值设置为基线LLM的Pass@1（如0.69）时，所提出的方法（L1-SLM-Verb，即COREA）在保持准确性的同时显著降低了成本。具体而言，在DeepMath500、OOD数学和OOD非数学数据集上，与单独使用LLM相比，成本分别降低了6.7%、21.5%和16.8%，而Pass@1的绝对下降控制在2%以内（例如，在OOD数学数据集上，Pass@1从基线LLM的79.6%降至77.9%）。此外，该方法在SLM的置信度校准方面表现优异，在全部数据集上平均取得了最低的ECE（0.12）和较高的AUROC（0.72）。消融实验表明，该方法在不同模型骨干和滚动大小下均有效，且L1置信度奖励在准确性与校准间取得了良好平衡。

### Q5: 有什么可以进一步探索的点？

该论文提出的协作框架存在几个关键局限，为未来研究提供了明确方向。首先，小模型输出的置信度虽经强化学习校准，但仍呈离散化，导致在调整阈值时准确率与成本的过渡不平滑。未来可探索更精细的置信度建模方法，例如引入概率分布输出或基于模型内部特征的连续置信度估计，以提升系统调控的灵活性。其次，强化学习训练过程存在稳定性问题，各奖励分量可能未同步收敛。可研究分层优化策略或动态奖励加权机制，确保推理能力与置信度校准的均衡提升。此外，论文未深入探索不同规模模型组合的影响。未来可系统分析模型参数量级差、能力差距与成本效益的关系，并扩展至多模型动态路由场景，例如根据问题复杂度自适应选择模型，或引入中等规模模型作为中间层，进一步优化效率。最后，该框架目前主要面向单轮推理任务，如何将其扩展至需要多步交互的复杂推理场景（如代码生成、多轮对话）也是一个值得探索的方向。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为COREA的协作推理框架，旨在通过结合小型语言模型（SLM）和大型语言模型（LLM）来平衡复杂推理任务中的准确性与成本。核心问题是LLM虽推理能力强但成本高，而SLM成本低但准确性不足。为此，COREA采用级联方法：先由SLM尝试回答问题并输出答案及置信度分数，若置信度低于预设阈值，则将问题推迟给LLM处理。方法上引入了基于强化学习的训练算法（RLCC），通过置信度校准奖励来对齐SLM的置信度估计。实验表明，该方法能同时提升SLM的推理能力和置信度校准效果，并在多个数据集和模型骨干上验证了其泛化性。主要结论是，COREA相比单独使用LLM，在数学和非数学推理任务上分别实现了21.5%和16.8%的成本降低，而准确率下降控制在2%以内，证明了校准置信度在实现高效SLM-LLM协作中的实用价值。
