---
title: "Step-wise Rubric Rewards for LLM Reasoning"
authors:
  - "Weichu Xie"
  - "Haozhe Zhao"
  - "Wenpu Liu"
  - "Yongfu Zhu"
  - "Liang Chen"
  - "Minghao Ye"
  - "Zirong Chen"
  - "Yuqi Xu"
  - "Shuai Dong"
  - "Ziyue Wang"
  - "Xinbo Xu"
  - "Kean Shi"
  - "Ruoyu Wu"
  - "Xiaoying Zhang"
  - "Wenqi Shao"
  - "Baobao Chang"
  - "Nan Duan"
  - "Jiaqi Wang"
date: "2026-05-17"
arxiv_id: "2605.17291"
arxiv_url: "https://arxiv.org/abs/2605.17291"
pdf_url: "https://arxiv.org/pdf/2605.17291v1"
github_url: "https://github.com/akarinmoe/SRaR"
categories:
  - "cs.LG"
tags:
  - "LLM推理"
  - "过程监督"
  - "奖励模型"
  - "强化学习"
  - "数学推理"
  - "自我纠正"
relevance_score: 7.5
---

# Step-wise Rubric Rewards for LLM Reasoning

## 原始摘要

Reinforcement Learning with Verifiable Rewards (RLVR) is widely used to improve reasoning in large language models, but rewards only final-answer correctness with no supervision over intermediate steps. Rubric-based methods such as Rubrics as Rewards (RaR) introduce finer-grained supervision by scoring rollouts against structured criteria, yet the rubric scores are still aggregated into a single scalar applied to the entire response, causing three weaknesses: loss of multi-criterion structure, uniform supervision of correct and incorrect steps, and reward hacking through unbounded self-correction. On 1,000 problems, we find 18.2% of steps in correct-answer responses are wrong yet positively rewarded, while 49.9% of steps in incorrect-answer responses are correct yet penalized. We introduce Step-wise Rubrics as Rewards (SRaR), an RLVR framework that (i) uses an LLM judge to attribute each rubric item to a specific reasoning step, (ii) normalizes per-step rubric scores across rollouts so only steps whose quality varies produce a learning signal, and (iii) combines the per-step reward with the outcome reward through a decoupled advantage estimator that keeps the outcome baseline stable. We further build a 16K-problem rubric dataset by contrastively distilling rubric items from correct and flawed reasoning paths sampled from a strong model. Across six mathematical reasoning benchmarks, SRaR improves average accuracy over RaR by 3.57 points on Qwen3-8B and 2.75 points on Qwen3-32B, raises the Faithful Reasoning Rate on AIME 2025 from 34.5% to 46.7%, and reduces self-correction looping from 48.1% to 26.5%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文尝试解决在大型语言模型推理强化学习中，现有基于检查表（rubric）的奖励方法存在的结构性缺陷。具体来说，研究背景是使用可验证奖励的强化学习（RLVR）已被广泛用于提升大模型推理能力，但其仅基于最终答案正确性提供奖励，缺乏对中间推理步骤的监督。为此，近期工作如基于检查表的奖励（RaR）等引入了更细粒度的检查表评分，但这些方法仍将所有检查项的分数聚合为一个单一的、应用于整个回复的标量奖励，导致三个关键不足：第一，丢失了多准则结构，无法区分不同类型的检查项（如标准推理、常见错误、优异洞察），且奖励信号不分步骤；第二，给正确和错误步骤提供统一的监督信号，导致实验发现18.2%的正确答案中的错误步骤被正向奖励，而49.9%的错误答案中的正确步骤被惩罚；第三，模型可通过过度自我修正等表面行为进行奖励黑客攻击。因此，本文的核心问题是：如何设计一种既具解释性又细粒度的奖励信号，以监督模型推理过程，从而同时提升最终答案准确性和中间推理步骤质量。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：

1. **方法类**：RLVR with GRPO和DAPO仅提供稀疏的二值最终答案信号，缺乏对中间步骤的指导。过程奖励模型（PRMs）虽能逐步评分，但需要大量人工标注且输出不透明的标量。GRPO-VPS通过测量策略在每一步边界上的正确答案条件概率来避免辅助模型，但信号仍是单一的、不可解释的标量。本文提出的SRaR通过将每个评分项归因到特定推理步骤，并在步骤级别归一化奖励，有效解决了这些问题。

2. **基于评分准则的方法**：Rubric-based方法如LLM-Rubric、RaR和RGR-GRPO使用可解释的评分准则作为强化学习奖励。但所有现有方法都将分数聚合成单一轨迹级标量，导致失败轨迹中正确步骤被惩罚、成功轨迹中错误步骤被强化。SRaR首次通过步骤级归因和归一化解决了这一被忽视的问题，并构建了16K问题的对比蒸馏评分数据集。

3. **评测类**：本文在六个数学推理基准上评估了SRaR，与RaR相比在Qwen3-8B上平均提升3.57分，在Qwen3-32B上提升2.75分，并将AIME 2025上的忠实推理率从34.5%提升到46.7%，自我修正循环从48.1%降至26.5%。

### Q3: 论文如何解决这个问题？

论文通过引入Step-wise Rubrics as Rewards (SRaR)框架解决RLVR中缺乏中间步骤监督的问题。核心方法包含三个协同设计：

1. **步骤归因的规则评判**：利用LLM裁判将每个规则项（SUGGEST/PITFALL/BONUS）关联到具体推理步骤，而非对整个响应打分。政策被要求输出结构化步骤格式（"### Step N: ..."），通过分词器偏移映射获取步骤token跨度，裁判返回每个规则项的二元判定$s_j$及其评价步骤$k_j$。

2. **跨采样的每步token分配与归一化**：将规则项转化为带符号delta值（按类型预算分配），同一步骤的delta求和得到原始步骤规则奖励$d_{k,i}$。对同一问题所有采样的相同步骤进行组归一化：$\bar{d}_{k,i} = (d_{k,i} - \mu_k)/(\sigma_k + \epsilon)$，使质量一致的步骤信号趋近零，差异显著的步骤获得强学习信号。归一化后的$\bar{d}_{k,i}$广播到该步骤所有token。

3. **解耦优势估计器**：将优势分解为两部分——结果优势$A_{base,i}$（基于最终答案正确性和格式的GRPO标准优势）和规则偏移$\tilde{r}_i^{(t)}$（上述步骤级归一化信号）。两者分别归一化后相加，防止规则噪声污染组基线，消除自我修正循环的奖励黑客行为。

整体框架在标准GRPO中替换token级优势为$\hat{A}_i^{(t)}$，并通过对比蒸馏从GPT-5采样正确/错误路径构建16K问题规则数据集。该方法在6个数学推理基准上平均提升RaR 3.57点（Qwen3-8B），将AIME 2025忠实推理率从34.5%提升至46.7%，自我修正循环从48.1%降至26.5%。

### Q4: 论文做了哪些实验？

论文在多个数学推理基准上进行了实验。**实验设置**：策略模型为Qwen3-8B-Non-Thinking和Qwen3-32B-Non-Thinking，使用8块NVIDIA H200 GPU训练，主要超参数包括rubric预算R_SUG=0.8、R_PIT=-1.0、R_BON=1.0和格式权重λ=0.1。评估配置采用温度0.7、top-p 0.8、最大长度10240 tokens。

**数据集/基准测试**：训练集基于DAPO math数据集构建，评估使用AIME 2024/2025、AMC 2023、MATH500、Minerva Math和Olympiad Bench六个基准。AIME和AMC报告Avg@32，其余使用单次生成。

**对比方法**：包括GRPO、DAPO、RaR、GRPO-VPS和RGR-GRPO，均在相同训练方案下重新实现以公平比较。rubric法官使用GPT-OSS-20B，并用Qwen3-30B-A3B-Instruct验证鲁棒性。

**主要结果**：在8B尺度上，SRaR平均准确率72.53，比最强基线RaR提高3.57点；在32B尺度上平均75.81，提高2.75点。具体地，8B在AIME 2025提升5.83、Olympiad Bench提升5.64、AMC 2023提升4.53。Step准确性分析显示，SRaR在AIME 2025上达到85.2%步准确率和46.7%回答准确率，忠实推理率从34.5%提升至46.7%，循环率从48.1%降至26.5%。消融实验表明，移除跨rollout步骤归一化导致性能崩溃至56.76，移除解耦优势估计则降至72.06。

### Q5: 有什么可以进一步探索的点？

首先，论文依赖外部LLM裁判进行逐步归因和评分，其误差会污染奖励信号。未来可研究如何结合自洽性检查或集成多个裁判来提升归因鲁棒性。其次，逐步推理监督引入了额外推理成本，可探索知识蒸馏或轻量级代理模型替代裁判，或设计主动采样策略只对关键步骤打分。第三，实验限于数学推理，需验证在代码生成、科学推理等复杂多步任务上的有效性，并需针对不同领域调整规则生成管线。第四，规则蒸馏依赖GPT-5等强模型，弱模型场景下的可用性存疑，可尝试用自生成规则或课程式规则进化来自适应。最后，要求模型输出显式步骤标题限制了泛化性，未来可结合隐式步骤边界检测（如语义分割）或无监督步骤发现方法，使框架适应自由格式推理。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为SRaR（Step-wise Rubrics as Rewards）的强化学习框架，用于提升大型语言模型的推理能力。现有方法（如RaR）仅对最终答案进行奖励，且对中间步骤缺乏细粒度监督，导致即使包含错误步骤的正确答案也会获得正奖励，而正确答案中的错误步骤则会被错误惩罚。SRaR的核心贡献在于：通过LLM裁判将每条评分标准归因到具体推理步骤，在多次采样中对每步得分进行归一化以聚焦于方差大的步骤，并使用解耦优势估计器将每步奖励与结果奖励结合，从而提供细粒度的步骤级监督。在六个数学推理基准上，SRaR相比RaR在Qwen3-8B上提升了3.57个百分点的平均准确率，在Qwen3-32B上提升了2.75个百分点。此外，它将AIME 2025上的忠实推理率从34.5%提升至46.7%，并将自我修正循环从48.1%降低至26.5%。该工作表明，监督的粒度与应用的内容同样重要。
