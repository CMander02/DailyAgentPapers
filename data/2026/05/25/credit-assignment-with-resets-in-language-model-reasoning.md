---
title: "Credit Assignment with Resets in Language Model Reasoning"
authors:
  - "Ankur Samanta"
  - "Akshayaa Magesh"
  - "Ayush Jain"
  - "Youliang Yu"
  - "Daniel Jiang"
  - "Kavosh Asadi"
  - "Daniel Jiang"
  - "Kaveh Hassani"
  - "Paul Sajda"
  - "Jalaj Bhandari"
  - "Yonathan Efroni"
date: "2026-05-25"
arxiv_id: "2605.25507"
arxiv_url: "https://arxiv.org/abs/2605.25507"
pdf_url: "https://arxiv.org/pdf/2605.25507v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "语言模型推理"
  - "强化学习"
  - "信用分配"
  - "策略优化"
  - "多步骤推理"
  - "自我重置"
relevance_score: 8.5
---

# Credit Assignment with Resets in Language Model Reasoning

## 原始摘要

Contemporary reinforcement learning with verifiable reward methods post-train language models on multi-step reasoning by assigning a single outcome reward uniformly across all tokens in a trajectory. Such uniform assignment ignores which steps contributed to success or failure. Improving credit assignment can address this limitation by enabling targeted refinement of faulty reasoning steps, rather than updating entire trajectories uniformly. Resets are one such simple mechanism, enabling more precise credit assignment by returning to an intermediate state and resampling counterfactual continuations, so that outcome differences can be attributed to decisions made at that point. We propose two such methods: Random-Reset Policy Optimization (RRPO), where reset states are drawn randomly from reasoning steps, and Self-Reset Policy Optimization (SRPO), where the model self-localizes the erroneous step in an incorrect trajectory and resets there. We analyze these methods within the Conservative Policy Iteration (CPI) framework. Extending CPI with a credit-assignment oracle that targets improvable states yields provable improvements over random resets. Across models and reasoning benchmarks, SRPO consistently outperforms standard GRPO and RRPO by sampling multiple suffix continuations at a self-localized reset and learning from their rewards, using only the model itself with no external supervision.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决语言模型在多步推理任务中训练时面临的信用分配问题。当前，基于可验证奖励的强化学习方法（RLVR）为整个推理轨迹中的所有token均匀分配单一的最终结果奖励，忽视了不同推理步骤对最终成败的实际贡献。这种粗粒度的信用分配导致模型无法精准识别并改进导致错误的关键步骤，而是对所有步骤进行无差别的更新，降低了学习效率。

为解决这一不足，论文提出了基于“重置”的信用分配机制。核心思想是：通过回溯到推理轨迹中的某个中间状态（即“重置”），并从该状态重新采样多个不同的后续推理路径（反事实续写），利用这些不同路径产生的结果差异，来精确归因于在该重置点所做出的决策。该方法旨在使模型能够针对有改进潜力的错误步骤进行精细化调整，而非对整个轨迹进行均匀更新。

论文提出了两种具体方法：随机重置策略优化和自重置策略优化。后者尤为关键，它让模型自身定位首次出错的位置作为重置状态，无需外部步骤级别的监督信号。本质上，论文要解决的核心问题是：如何在没有细粒度步骤奖励（仅依赖最终结果奖励）的情况下，通过设计有效的“重置”机制，实现更精确的信用分配，从而提升语言模型在复杂多步推理任务上的学习速度和最终性能。

### Q2: 有哪些相关研究？

相关研究主要分三类:

**方法类**: 将重置用于RL探索的工作虽多(如DR-PO、Go-Explore),但重置目标由外部启发式选择以扩展状态覆盖,而非用于归因失败步骤。SRPO则聚焦于信用分配,通过模型自定位错误步骤进行重置。值函数或过程奖励模型(PRM)虽能提供步骤级信号,但需额外训练和标注,SRPO利用推理中模型自定位首个错误思想实现免训。

**应用类**: SCoRe通过条件化二次尝试驱动修正,但改变首次分布;Critique-GRPO用批评条件化精炼并通过离策略校正,而SRPO仅从验证正确前缀采样后续,避免离策略校正。InT虽定位错误步骤但依赖人类参考解且用SFT;SPO-Tree用启发式(如token计数)选择切点,而非语义对齐的思想边界。ASTRO通过MCTS在生成时内联回溯,而SRPO仅将其用于训练时信用分配,推理时直接生成。

**评测类**: 本文在多模型和推理基准上系统评估,表明SRPO在信用分配上持续优于标准GRPO和RRPO。核心区别在于:SRPO仅需模型自身,无需外部监督或附加模型,通过自定位重置实现更精确的信用归因。

### Q3: 论文如何解决这个问题？

这篇论文通过引入基于重置(reset)的信用分配机制来解决语言模型推理中奖励稀疏且均匀分配的问题。核心方法是在Conservative Policy Iteration (CPI)理论框架下，提出两种策略优化方法：随机重置策略优化(RRPO)和自定位重置策略优化(SRPO)。

整体框架采用"思考MDP"（Thought MDP）抽象，将每个语义连贯的推理步骤视为原子动作。算法在每个训练步骤构建双组缓冲器：一组是标准GRPO从初始提示采样的G条轨迹，另一组是从重置状态共享前缀采样的G条轨迹。主要创新点包括：

1. **重置机制**：RRPO从失败种子轨迹中随机选择重置点进行均匀采样；SRPO则让模型自我定位第一个错误思考步骤，仅在该错误发生前的前缀状态处重置，实现精确信用分配。

2. **信用分配Oracle**：理论分析表明，通过识别可改进状态（即存在优势大于阈值τ的状态），能显著提升样本效率和迭代进步。SRPO通过模型自定位替代了降采样过程，实现了无外部监督的Oracle级信用分配。

3. **组归一化优势估计**：对两组轨迹分别进行组内归一化，仅对共享前缀组中的后缀token应用优势损失，通过前缀掩码确保信用信号精确作用于思考步骤而非所有token。

实验表明，SRPO在多个模型和推理基准上持续优于标准GRPO和RRPO，其优势在可改进状态概率低时最为显著。

### Q4: 论文做了哪些实验？

论文在三个实验场景评估了基于重置的信用分配方法。**实验设置**：使用Qwen2.5-14B-Instruct和OLMo-3-7B-Instruct两个模型，在NuminaMath-Olympiads的400道题上训练2个epoch，所有方法计算量匹配为每prompt 8次rollout，采用rank 64的LoRA微调。**数据集与基准测试**：使用10个基准测试（涵盖数学、科学、策略和常识推理），包括NuminaMath-Olympiads、HMMT Nov 2025、MATH Level-5、StrategyQA等，每项评估500个随机样本，报告3个种子的均值±标准差。对比方法包括GRPO、SCoRe、Cr-GRPO、SPO-Tree、RRPO和SRPO。**主要结果**：
1. **采样策略比较**：在固定预算下比较SRPO的三种配置（1×4、2×4、1×8），1×4（4个基础rollout+4个从自定位前缀重采样）在大多数任务上表现最佳。
2. **主实验**：SRPO在两个模型上均最强，在Qwen2.5-14B上7/10任务最佳，OLMo-3-7B上6/10最佳；RRPO与GRPO相当。例如OLMo-3-7B上，SRPO在HMMT达15.6±4.2，GRPO仅11.1±5.7。
3. **代码任务**：在LiveCodeBench v6 medium上，SRPO收敛到更高通过率，且达到同等表现比GRPO快2-3倍。
4. **自定位质量分析**：SRPO将重置集中在推理链早期，约50%定位在Claude Opus 4.5判断的失败步骤之前，干净前缀的修正成功率（28.7%）是错误前缀（16.3%）的近2倍。

### Q5: 有什么可以进一步探索的点？

**局限与未来方向**  
当前方法依赖明确多步推理任务和可验证奖励，在非结构化任务或无法提供中间奖励的场景中效果未知。自定位质量仍是性能瓶颈—错误前缀的修正成功率显著低于正确前缀，且无外部监督时自定位准确率与理想oracle存在差距。未来可从三方面突破：1）引入轻量级过程奖励模型（PRM）或对比学习增强自定位鲁棒性，或利用思维链的置信度信号辅助错误步骤识别；2）将重置机制扩展至开放性任务（如对话或创意生成），通过隐式状态表征或连续价值函数估计实现软重置；3）理论层面需推导有限样本下的收敛保证，并探索非CPI框架下的重置策略（如结合actor-critic的连续重置）。此外，跨模型规模（100B+）的扩展性及重置计算成本效率优化也值得关注。

### Q6: 总结一下论文的主要内容

该论文提出并分析了基于“重置”机制的语言模型推理中的信用分配方法。问题在于当前强化学习后训练方法（如GRPO）对轨迹中所有token均匀分配结果奖励，忽略了具体步骤的贡献。为此，作者提出两种方法：随机重置策略优化（RRPO）从推理步骤中随机选取重置状态，以及自我重置策略优化（SRPO）让模型自行定位错误步骤并在此重置。在保守策略迭代框架下，理论证明结合能定位可改进状态的信用分配oracle可以获得优于随机重置的改进。主要结论是，SRPO通过在自我定位的错误步骤采样多个后缀续连并学习其奖励，无需外部监督就持续优于标准GRPO和RRPO。该工作通过信用分配细化了语言模型推理中的学习过程，提高了后训练效率。
