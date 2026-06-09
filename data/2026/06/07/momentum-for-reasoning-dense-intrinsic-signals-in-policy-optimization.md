---
title: "Momentum for Reasoning: Dense Intrinsic Signals in Policy Optimization"
authors:
  - "Hao Chen"
  - "Zhanming Shen"
  - "Liyao Li"
  - "Yanyu Chen"
  - "Xuhang Zhu"
  - "Xiaomeng Hu"
  - "Qi Zhang"
  - "Ru Peng"
  - "Xiaoyu Shen"
  - "Haobo Wang"
  - "Junbo Zhao"
date: "2026-06-07"
arxiv_id: "2606.08815"
arxiv_url: "https://arxiv.org/abs/2606.08815"
pdf_url: "https://arxiv.org/pdf/2606.08815v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "LLM Agent"
  - "Reasoning Agent"
  - "Policy Optimization"
  - "Reinforcement Learning"
  - "Training Methodology"
relevance_score: 8.5
---

# Momentum for Reasoning: Dense Intrinsic Signals in Policy Optimization

## 原始摘要

Reinforcement learning with verifiable rewards (RLVR) has emerged as a powerful paradigm for eliciting long-chain reasoning in large language models. However, existing methods based on Group Relative Policy Optimization (GRPO) rely on a binary outcome reward, which induces two structural failure modes: Zero-Advantage Collapse, in which all rollouts in a group share the same outcome and the gradient vanishes, and Hallucinated Certainty, in which the model becomes increasingly confident on incorrect rollouts late in training. We address both modes by densifying the reward with intrinsic signals computed entirely from the policy's own conditional probabilities, and propose ISPO (Intrinsic Signal Policy Optimization, which combines a sequence-level signal measuring how informative the thinking trajectory is for the final answer, with a token-level directional reward whose hallucinated-certainty hinge penalizes confidently-wrong predictions at critical decision tokens. Across three base models and five mathematical reasoning benchmarks, ISPO consistently outperforms competitive baselines, with the largest gains on the hardest benchmarks where zero-advantage collapse is most frequent, and training-dynamics diagnostics confirm that both failure modes are decreased.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于二元结果奖励（如正确/错误）的策略优化（如GRPO）在训练大语言模型进行长链推理时存在的两个结构性失败模式。研究背景是，RLVR方法虽然有效，但现有方法依赖单一的二元结果奖励，这导致模型缺乏过程信号。第一个问题“零优势崩溃”发生在同一组的多个采样结果完全相同时，所有轨迹的优势都被归零，梯度消失，学习停滞。第二个问题“幻觉确定性”出现在训练后期，模型在错误轨迹的关键决策词元上，预测熵降低，自信地“固化”了错误答案。这两个问题的根本原因都在于二元奖励只告诉模型“是否成功”，而没有提供“如何成功”的过程信息。因此，本文要解决的核心问题是：如何在不依赖外部奖励模型或过程标注的情况下，通过从策略自身条件概率中提取密集的内在信号，来弥补二元奖励的稀疏性，从而消除零优势崩溃和幻觉确定性这两种失败模式，在困难基准上持续提升模型推理能力。

### Q2: 有哪些相关研究？

相关工作按类别组织如下：

**1. 方法类：强化学习与密集奖励塑造**
现有工作主要基于GRPO等算法，通过二进制结果奖励训练推理模型。为缓解奖励稀疏问题，研究引入策略内在信号，如步骤级置信度增长、低概率令牌置信度、熵趋势或关键决策点的熵门控。ISPO与这些优化器层面的改进正交，且首次在序列级信号中引入精确的信息论等价关系（Conditional IFD = Conditional KL），将原本用于监督数据选择的指标扩展至在线RL。

**2. 应用类：令牌级信用分配与零优势干预**
令牌级方法通过跨rollout方差或对显著令牌的选择性长度惩罚利用梯度重尾分布。数据筛选方向通过层级提示、动态重采样或提示复杂度调度处理零优势批次。好奇驱动探索和内在动机也为模型内部密集奖励提供了理论渊源。ISPO通过策略自身的内在信号恢复每个批次内的梯度，不改变rollout流程，与这些干预正交组合。

**3. 评测类：数学推理基准**
本文在五个数学推理基准上评估，特别关注零优势崩溃频率最高的困难基准。结果证实ISPO在缓解零优势崩溃和幻觉确定性两种故障模式上有效，且收益在困难任务上最显著。

### Q3: 论文如何解决这个问题？

ISPO（Intrinsic Signal Policy Optimization）通过引入两种密集的内在信号来克服GRPO中二元结果奖励导致的两种结构性失败模式。核心方法是在GRPO框架基础上，用复合奖励替换原有的二元结果奖励，该复合奖励由三部分组成：原始二元结果奖励、序列级内在信号和令牌级内在信号。

序列级信号使用条件IFD（Instruction Following Difficulty）指标，计算策略给定思考轨迹后预测答案的对数概率与不给定思考轨迹时预测答案的对数概率之差，衡量思考轨迹对最终答案的信息量。这解决了零优势崩溃问题：即使在所有rollout结果相同的情况下，条件IFD仍能提供组内方差，从而维持梯度信号。

令牌级信号作用于关键决策令牌子集，该子集通过熵过滤器（选择高熵令牌）和漂移过滤器（选择策略分布相对于基模型发生显著变化的令牌）的交集获得。对于正确rollout，奖励低困惑度以强化正确推理；对于错误rollout，使用包含熵和铰链惩罚项的组合，惩罚低熵（即过于自信）的错误预测，直接针对幻觉确定性模式。

两个内在信号都完全由策略自身的条件概率计算，并且与结果奖励正交组合：序列级信号乘以(2R_o-1)实现结果条件化，令牌级信号根据结果分别计算正负奖励。整个复合奖励替换GRPO中的结果奖励用于优势估计，不修改其他训练流程。实验证明ISPO在三个基模型和五个数学推理基准上持续优于基线，尤其在困难基准上提升最大，训练动力学诊断也证实两种失败模式均被有效缓解。

### Q4: 论文做了哪些实验？

论文在Qwen2.5-Math-1.5B、Qwen2.5-Math-7B和Qwen2.5-7B三个基座模型上进行实验，使用DAPO-Math（约17K可验证数学题）作为训练数据。评估基准包括AIME 2024、AIME 2025、AMC 2023、MATH-500和OlympiadBench，采用Pass@1（贪心解码）和avg@16/pass@32（T=0.6）指标。对比方法包括Base模型、vanilla GRPO、Dr.GRPO、ProGRPO、Scaf-GRPO、PACR和PREPO。主要结果：ISPO在所有基座模型上平均准确率最佳，在1.5B、7B数学版和7B通用版上分别比最强基线高+5.7、+4.1和+4.6个点，在AIME24/25等难题上提升最大（如7B数学版AIME24达48.9% vs GRPO的30.0%）。消融实验显示：IFD单独贡献+5.7点，token奖励额外+5.1点；关键token选择采用交集A∩C_Δ最优（55.4% vs 并集53.6%）；方向性奖励中，移除不对称性损失6.9点，移除幻觉确定性hinge损失3.2点，证实两者均不可或缺。

### Q5: 有什么可以进一步探索的点？

ISPO的局限性首先在于其对可验证结果任务的依赖，未来可探索引入学习型验证器或替代性结果奖励函数，将框架扩展至开放生成任务。其次，实验仅基于Qwen2.5数学推理领域，需在代码、科学推理等跨领域及Llama/DeepSeek等更多基座模型上验证泛化性。此外，可研究更细粒度的内在信号设计，如融合过程监督或分层奖励稀释策略，以应对复杂推理链中的稀疏奖励问题。在算法层面，可探索将动量思想与动态正则化结合，避免训练后期模型对错误轨迹的过度自信。最后，建议深入分析序列级与词元级信号的协同效应，或设计自适应权重机制平衡两者贡献，从而进一步提升长链推理的鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文针对基于二元结果奖励的强化学习方法（如GRPO）在长链推理中的两个结构性失效模式：零优势崩溃（同一组奖励完全相同导致梯度消失）和幻觉确定性（模型对错误推理逐步过度自信），提出了ISPO（内在信号策略优化）方法。ISPO通过从策略模型自身的条件概率中提取密集的内在信号来增强奖励：序列层面采用条件IFD信号评估推理轨迹对最终答案的信息量，并利用精确的条件KL恒等式保证零优势崩溃时梯度非零；token层面使用方向性奖励配合幻觉确定性惩罚，抑制关键决策token上的错误自信预测。在三个基础模型和五个数学推理基准上的实验表明，ISPO一致优于强基线，在难度最高、零优势崩溃最频繁的AIME级基准上提升最大。训练动力学诊断证实两种失效模式均得到缓解。该方法的核心贡献在于揭示了当结果奖励稀疏时，模型自身的概率曲面往往包含足够的信息来维持学习动量。
