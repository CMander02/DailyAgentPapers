---
title: "Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimodal Policy Optimization"
authors:
  - "Shizhe Xiang"
  - "Ke An"
  - "Wenlong Yu"
  - "Yue Liu"
  - "Jian Luan"
  - "Pei Fu"
  - "Qilong Wang"
date: "2026-06-05"
arxiv_id: "2606.07000"
arxiv_url: "https://arxiv.org/abs/2606.07000"
pdf_url: "https://arxiv.org/pdf/2606.07000v1"
categories:
  - "cs.AI"
tags:
  - "LVLM推理优化"
  - "策略蒸馏"
  - "多模态推理"
  - "RLVR"
  - "Token级监督"
  - "奖励稀疏性"
  - "教师-学生框架"
  - "上下文学习"
relevance_score: 7.5
---

# Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimodal Policy Optimization

## 原始摘要

Recent post-training methods, particularly Reinforcement Learning with Verifiable Rewards (RLVR), have significantly enhanced the reasoning ability of Large Vision-Language Models (LVLMs). However, the sparse nature of verifiable rewards provides little token-level supervision for failed rollouts, often leading to inefficient exploration in complex multimodal reasoning tasks. Although policy distillation can offer dense guidance, external teacher based methods introduce substantial computational overhead, while answer conditioned tuning methods may expose answer-level information and induce shortcut-like generation behavior. To address these limitations, we propose PTD-PO, a Privileged Tutoring Distillation Policy Optimization framework for RLVR that provides dense guidance without exposing the answer to the student policy. Specifically, PTD-PO constructs structured privileged hints from spatial attention guidance and intermediate textual reasoning steps, and uses them through in-context learning to produce step-wise token-distribution supervision. The student is still optimized under the original answer-free context, and its failed rollouts are aligned with the hint-augmented reference model at the token-distribution level. To further stabilize distillation under the distribution shift between guided and unguided contexts, we introduce a Top-K Jensen-Shannon divergence objective that focuses alignment on informative token probabilities while reducing memory overhead. Experiments on LVLMs ranging from 2B to 8B parameters show that PTD-PO consistently outperforms RLVR and distillation baselines, mitigates entropy collapse, and improves complex multimodal reasoning performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型视觉语言模型（LVLM）在多模态推理任务中，通过可验证奖励强化学习（RLVR）进行后训练时面临的核心问题：奖励稀疏性导致的探索困难和策略退化。

**研究背景**：RLVR通过最终答案的二元正确性提供奖励信号，能有效提升LVLM的推理能力，但该奖励仅在最终输出时给出，对于失败的推理轨迹，模型无法获得中间步骤（如视觉定位、推理逻辑）的具体错误反馈，导致信用分配困难，在复杂的推理空间中低效探索甚至失败。

**现有方法的不足**：为缓解奖励稀疏，现有方法引入密集的标记级监督，如在线策略蒸馏（OPD）或条件化自蒸馏。OPD依赖外部教师模型在线推理，计算开销大且存在词表不匹配问题；而基于答案或完整解决方案的条件化自蒸馏虽然高效，但会暴露最终答案信息，诱导模型走“答案捷径”，产生过于确定性的轨迹、加剧策略熵崩溃（entropy collapse），抑制了对替代推理路径的探索。

**本文要解决的核心问题**：提出一种既高效又非答案暴露的密集监督形式——特权指导蒸馏（PTD-PO）。该方法通过构造不包含具体答案的“特权提示”（融合空间注意力引导与中间推理步骤），在冻结的参考模型上生成标记级分布监督，用以纠正学生策略的失败轨迹。同时，为解决非对称蒸馏（有提示的教师 vs 无提示的学生）带来的分布偏移和内存开销，论文设计了基于Top-K詹森-香农散度（JSD）的稳定对齐目标。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可分为以下几类：

1. **方法类**：本文主要与**强化学习与可验证奖励（RLVR）** 相关，RLVR 利用结果级反馈替代人工偏好标注，但存在奖励稀疏问题。本文提出 PTD-PO，通过特权蒸馏提供密集的令牌级指导，弥补 RLVR 在失败轨迹上信息不足的缺陷。与**在线策略蒸馏（OPD）** 不同，OPD 需要外部教师模型在线推理，计算开销大且可能带来分词器不匹配，本文采用自蒸馏方式，避免额外计算负担。此外，**上下文自蒸馏**方法（如使用正确答案或完整解决方案作为条件）虽能提供密集监督，但可能暴露答案级信息，诱导捷径学习并降低探索性。PTD-PO 则使用无答案的特权提示（视觉空间注意线索和中间推理步骤）作为教学信号，不暴露最终答案。

2. **应用类**：相关工作包括**多模态推理**中的视觉定位和多步推断，以及**解释引导的视觉-语言学习**和**逐步推理蒸馏**。本文将这些技术结合，通过特权信息（视觉线索和推理指导）提升多模态推理性能，适用于 2B 到 8B 参数的大视觉语言模型。

3. **评测类**：本文在复杂多模态推理基准上评估，与 RLVR 和蒸馏基线对比，验证了 PTD-PO 在提升推理性能、缓解熵崩溃和降低内存开销方面的优势。

### Q3: 论文如何解决这个问题？

PTD-PO 通过结合GRPO和特权辅导蒸馏来解决多模态强化学习中的稀疏奖励问题。整体框架由两个并行优化路径构成：一是标准的GRPO路径，在原始无答案上下文下采样响应组并计算组内相对优势；二是失败轨迹定向蒸馏路径，仅在采样组准确率低于阈值（默认1.0）时激活。核心创新在于结构化特权提示构建模块：对每个问题，通过强模型逆向工程生成包含空间注意力引导（如高亮相关区域、对象和干扰物）和文本推理步骤引导（如高层级推理方向）的提示，但仍遵循零剧透原则避免暴露最终答案。关键技术包括不对称上下文蒸馏：冻结参考模型接收包含特权提示的扩展上下文（x^h）生成教师分布，而学生策略保持原始无提示上下文（x），由KL散度损失对齐两者。为稳定分布偏移情况下的蒸馏，引入Top-K JSD目标，保留教师和学生Top-K token的联合支撑集，并将剩余概率聚合成尾桶，将内存复杂度从O(BTV)降至O(BTK)。最终损失函数为GRPO负期望损失与权重为λ的PTD正则项之和，通过失败轨迹的token级分布对齐提供密集的步进级监督信号。

### Q4: 论文做了哪些实验？

论文在Qwen3-VL-Thinking系列模型（2B、4B、8B参数）上进行了实验。**实验设置**方面，使用ViRL39K（38,870个可验证视觉语言问答样本）作为训练语料，以PAPO多模态推理基准套件作为评估基准，涵盖通用和视觉依赖两大类推理任务，包括MathVista、MathVerse、MMMU-Pro、LogicVista等数据集。**对比方法**包括SFT、OPSD、GRPO、HDPO（基于真实答案的条件自蒸馏）和PAPO（感知感知策略优化）。**主要结果**显示，PTD-PO在所有模型规模上均取得最佳总体平均性能（Overall AVG）：2B模型达61.21%，4B模型达71.23%，8B模型达71.86%。消融实验表明，使用结构化特权提示（包含空间注意力和中间推理步骤）优于非结构化提示；通过Top-K Jensen-Shannon散度进行蒸馏时，激活阈值τ=1.0（对所有失败轨迹应用PTD）效果最佳。在困难问题上，特权提示比GT答案提示能恢复更多失败案例为部分成功，同时避免捷径式生成行为。

### Q5: 有什么可以进一步探索的点？

该论文的局限性和未来研究方向包括：1) 特权提示（privileged hints）依赖外部教师模型生成，增加了训练前的计算开销和数据质量控制成本，未来可探索学生模型自生成提示的蒸馏范式；2) 结构化提示设计虽有效但视觉空间引导的构建规则较手工化，可能无法覆盖所有复杂推理场景，可尝试将提示生成端到端地融入训练过程；3) Top-K JS散度仅基于概率值选择Token，未考虑语义重要性差异，可引入任务或策略价值感知的Token选择机制；4) 当前仅在生成式奖励场景验证，对于判别式或偏好型奖励任务的泛化能力待检验；5) 实验仅在ViRL39K数据集训练，可扩展到更多样化的知识密集型或长视频推理任务；6) 推测特权提示本质是提供“隐式过程监督”，未来可与过程奖励模型或蒙特卡洛树搜索结合，实现更细粒度的推理路径优化。

### Q6: 总结一下论文的主要内容

该论文提出了一种面向多模态推理的教师蒸馏框架 PTD-PO，旨在解决强化学习中使用可验证奖励（RLVR）时奖励稀疏导致的探索效率低下问题。现有方法中，外部教师蒸馏计算开销大，而基于答案的蒸馏会导致捷径学习并抑制探索。PTD-PO 的核心创新在于引入“特权指导”范式：通过构建空间注意力和中间推理步骤构成的无答案提示，让参考模型在提示增强上下文中生成密集的逐令牌分布监督，而学生策略仍在原始无答案上下文中优化。为缓解分布偏移带来的不稳定问题，论文进一步设计了基于 Top-K Jensen-Shannon 散度的损失函数，专注于对齐高信息量令牌概率。在 2B 至 8B 参数的多模态大模型上的实验表明，PTD-PO 在复杂推理任务上持续优于 RLVR 和各类蒸馏基线，能有效缓解熵崩溃并提升模型从失败轨迹中恢复的能力，且兼容不同 RLVR 优化器，具有显著的泛化价值。
