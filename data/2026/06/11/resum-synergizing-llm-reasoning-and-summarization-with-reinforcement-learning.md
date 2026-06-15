---
title: "ReSum: Synergizing LLM Reasoning and Summarization with Reinforcement Learning"
authors:
  - "Xucong Wang"
  - "Ziyu Ma"
  - "Yong Wang"
  - "Shidong Yang"
  - "Hailang Huang"
  - "Renda Li"
  - "Pengkun Wang"
  - "Xiangxiang Chu"
date: "2026-06-11"
arxiv_id: "2606.13316"
arxiv_url: "https://arxiv.org/abs/2606.13316"
pdf_url: "https://arxiv.org/pdf/2606.13316v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "推理优化"
  - "强化学习"
  - "长上下文压缩"
  - "自摘要"
relevance_score: 7.5
---

# ReSum: Synergizing LLM Reasoning and Summarization with Reinforcement Learning

## 原始摘要

Reinforcement Learning with Verifiable Rewards (RLVR) is a central technique for improving long-horizon reasoning in Large Language Models (LLMs). However, existing RLVR methods often encourage unnecessarily long reasoning rollouts, which can degrade reasoning coherence and exhaust the available context budget. Existing approaches to long-context organization often depend on external mechanisms to organize rollouts, rather than enabling the model to manage its own reasoning trajectory. To address this limitation, we propose ReSum, a novel RLVR framework that enables LLMs to compress and organize their reasoning trajectories through self-summarization. Our pilot studies show that self-summarization stabilizes generation by lowering token-level entropy, and that introducing a ``summarization'' phrase can substantially mitigate errors propagated from an incorrect rollout prefix. Motivated by these findings, ReSum adopts a summarization-aware adaptive rollout mechanism that contrastively evaluates whether self-summarization benefits the ongoing reasoning process. Specifically, when the model spontaneously triggers self-summarization, ReSum masks the summarization phrase to create a contrastive branch; for non-summarization positions, it instead randomly injects the phrase to create a matched branch. We further design a summarization-aware advantage to enable finer-grained comparison between contrastive rollout trajectories. Extensive experiments show that ReSum improves performance at an average of 4\% while reducing rollout length by 18.6\%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在长链推理任务中，由于强化学习可验证奖励（RLVR）方法带来的“过度思考”问题。现有RLVR方法存在奖励偏向于生成更长思维链（CoT）的偏差，导致模型容易遗忘早期推理步骤、重复解决已处理子问题，并耗尽上下文预算。虽然已有研究通过外部机制（如缓存监控、自动编码器压缩或额外智能体模块）来组织长上下文，但这些方法引入了额外开销，且可能影响摘要或输出的忠实度。核心问题在于：LLM能否利用自摘要（self-summarization）作为内在机制来组织自身的推理轨迹，从而在保持甚至提升推理准确性的同时，显著缩短推理长度并提升推理连贯性。本文提出的ReSum框架正是为了训练模型在推理过程中自发且高效地使用自摘要，以解决这一矛盾。

### Q2: 有哪些相关研究？

关于相关研究，本文主要涉及以下两类工作：

**1. 基于可验证奖励的强化学习（RLVR）方法**：这是提升LLM长推理能力的关键技术。相关工作包括：(a) 细粒度目标设计，如DAPO将GRPO的序列级梯度损失扩展到token级，GPG则回归原始策略梯度去除辅助裁剪项；(b) 过程级奖励，通过折扣因子或训练过程奖励模型（PRM）解决信用分配问题；(c) 推理展开扩展，如TreeRL选择高不确定性token进行分支，Tree-GRPO对思维-行动步骤赋予两级优势。本文的区别在于，现有方法常导致不必要的长推理和上下文预算耗尽，而ReSum通过自摘要压缩和组织推理轨迹，在提升性能的同时显著减少展开长度。

**2. 上下文组织方法**：旨在改进模型对长上下文的注意力管理，分为外部方法和内部方法。前者依赖缓存监控、文本压缩器等外部机制重构长上下文；后者通过蒸馏、监督微调或RLVR训练模型选择性回顾生成内容，如Re$^2$利用群体外奖励实现“重做”操作，RLTR采用“工具调用完整性”作为奖励。本文与这些研究一致，聚焦于将摘要能力内化于复杂推理，但创新地提出了摘要感知的自适应展开机制，通过对比评估自摘要是否有利于推理过程，从而实现更精细的推理轨迹管理。

### Q3: 论文如何解决这个问题？

ReSum通过强化学习使LLM在推理过程中自发学会自我总结，以压缩和组织推理轨迹，核心是一个基于树状分支的对比式优势评估框架。整体框架分为四步：(1) 对每个查询生成T个初始推理轨迹作为树根；(2) 在每个轨迹中识别两类分支点：自然点（模型自发总结的位置，通过关键词匹配检测）和人工点（随机选取的位置）；(3) 在自然点处遮蔽总结短语后重新生成后续内容，在人工点处注入总结短语后重新生成，形成对比分支；(4) 当总分支数达到预算B时停止。创新点在于设计了一套总结感知的分组优势机制：将带有总结的分支和不带总结的分支分为两组，分别计算组内相对优势，然后相加作为最终优势。奖励函数包含任务奖励（是否答对）和格式奖励（对自然总结点奖励0.2、人工总结点奖励0.05，并依据出现次数加权），避免无限总结。这种方法让模型通过对比不同分支的回报差异，自动学习何时总结能提升推理质量，解决了现有RLVR方法中推理轨迹过长、上下文预算耗尽的问题。

### Q4: 论文做了哪些实验？

论文进行了多组实验。实验设置上，模型基于DGPO代码库和Open-R1框架，在8块NVIDIA H20 GPU上训练，训练温度1.0，评估温度0.6、top-p值0.95，最大生成长度为4096。数据集方面，数学推理使用MATH训练，在AIME24、AIME25、AMC23、MATH500、Minerva、Olympiad六个基准上评估，AIME系列结果平均32次，其余平均4次；多模态领域使用GEOQA-8K。对比方法包括GRPO、Dr. GRPO、GPG、DAPO、GSPO、GRPO-AD和DGPO。主要结果如下：

1. **与SOTA方法对比**：在Qwen2.5-Math-7B上，ReSum平均准确率达41.64%，比GRPO高4.03%，在AIME25上达13.33%（DGPO为10.21%）。

2. **不同骨干模型**：在Qwen2.5-Math-1.5B上，ReSum平均33.07%（GRPO 29.39%）；在Qwen2.5-3B上达28.81%；在DeepSeek-Math-7B上达17.32%。

3. **兼容性**：在GPG上叠加ReSum后平均提升2.83%（从37.93%到40.76%），在DAPO和GSPO上分别提升2.94%和2.46%。

4. **多模态任务**：在GEOQA-8K上，ReSum达62.04%，比GRPO高5.61%。

5. **消融实验**：移除自然点（NPs）后性能下降明显（7B模型从41.64%降至38.94%），验证各组件有效性。

6. **分支配置**：在固定预算B=16时，平衡配置T=4, J=4取得最佳平均分28.81%。

### Q5: 有什么可以进一步探索的点？

ReSum的核心局限在于其树形展开策略依赖于预定义的“总结”触发位置（如句尾），这种人为分割可能破坏推理自然流程，未来可探索基于语义边界或模型内在不确定性来自动识别关键总结点。其次，对比分支通过掩码或注入总结短语构建，可能引入噪声，尤其当模型尚未形成稳定总结习惯时，改进思路是引入动态阈值，仅在确信总结有益时激活对比。此外，ReSum主要在数学和代码等结构化任务上验证，在开放式长文本生成如论文综述或多轮对话中，总结时机与内容选择会更复杂，需要设计任务自适应的奖励函数。最后，当前方法仅优化单个轨迹的总结，可扩展为多智能体协同机制，让不同推理路径相互生成或评价总结，从而利用集体智慧减少单一策略的过拟合风险。

### Q6: 总结一下论文的主要内容

ReSum提出了一种基于强化学习的框架，旨在解决LLM在长链推理中因过度推理导致上下文浪费和推理退化的问题。核心贡献在于首次将模型的自摘要能力作为内在机制来组织推理轨迹。方法上，ReSum设计了树状展开策略，通过对比学习自然点（模型自发摘要）和人为点（注入摘要短语）的对比分支，并结合摘要感知的优势函数实现细粒度过程监督。实验表明，在数学推理基准上，ReSum平均提升4%的准确率，同时将推理长度缩短18.6%，且无需外部模块或监督微调。该工作证明了自摘要作为长程推理中上下文压缩和错误恢复的内生控制机制的有效性，为RLVR方法提供了新的优化维度。
