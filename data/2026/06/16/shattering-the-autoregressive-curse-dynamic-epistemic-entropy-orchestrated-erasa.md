---
title: "Shattering the Autoregressive Curse: Dynamic Epistemic Entropy Orchestrated Erasable Reinforcement Learning for LLMs"
authors:
  - "Ziliang Wang"
  - "Kang An"
  - "Faqiang Qian"
  - "Jialu Cai"
  - "Cijun Ouyang"
  - "Yuhang Wang"
  - "Qibing Ren"
  - "Yichao Wu"
date: "2026-06-16"
arxiv_id: "2606.17735"
arxiv_url: "https://arxiv.org/abs/2606.17735"
pdf_url: "https://arxiv.org/pdf/2606.17735v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "强化学习"
  - "数学推理"
  - "长序列推理"
  - "纠错机制"
  - "KV缓存"
relevance_score: 8.5
---

# Shattering the Autoregressive Curse: Dynamic Epistemic Entropy Orchestrated Erasable Reinforcement Learning for LLMs

## 原始摘要

Although reinforcement learning (RL) has expanded the cognitive boundaries of large language models (LLMs), it often remains vulnerable to the autoregressive curse in long-horizon logical reasoning: small epistemic perturbations introduced early in generation can propagate irreversibly along the Markov decision process flow, triggering cascading failures that drive the reasoning trajectory toward collapse. To overcome this autoregressive cascade, in which a single early mistake can compromise all subsequent reasoning steps, we propose dynamic epistemic entropy orchestrated erasable reinforcement learning ($\text{E}^3\text{RL}$). $\text{E}^3\text{RL}$ eliminates reliance on external signals by grounding the model's endogenous local autoregressive cross-entropy as an intrinsic coordinate of epistemic uncertainty. By introducing segment-level adaptive dynamic thresholds and advantage allocation, $\text{E}^3\text{RL}$ enables the model to precisely excise localized logical defects while reusing historical key-value (KV) cache streams, thereby endowing the reasoning process with a self-healing capability. We train $\text{E}^3\text{RL}$ on the DeepMath-103k dataset. Experimental results show that $\text{E}^3\text{RL}$ reshapes the exploration efficiency of long-sequence reasoning and improves sample efficiency while maintaining linear memory overhead. On mathematical reasoning benchmarks such as AIME, $\text{E}^3\text{RL}$ achieves substantial performance gains, with the 4B and 8B parameter models surpassing previous state-of-the-art (SOTA) results by 5.349\% and 6.514\%, respectively. These findings suggest that $\text{E}^3\text{RL}$ shatters the autoregressive curse in long-sequence reasoning and establishes a theoretical and systems-level foundation for the next generation of self-healing artificial general intelligence (AGI).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLMs）在长序列逻辑推理中面临的“自回归诅咒”（Autoregressive Curse）问题。研究背景是，当前LLMs依赖于自回归生成范式，将复杂问题求解转化为序列预测，但在处理长序列推理时，这种严格遵循时间因果箭头、缺乏时空回退和局部纠错能力的单向生成结构存在严重缺陷。现有方法的不足主要体现在两方面：一是引入外部过程奖励模型（PRM）进行逐步评分，这面临高昂的数据标注成本和严重的分布偏移问题，容易引发系统级的奖励攻击；二是全局重采样方法必须等待完整序列生成后才能判定，会因局部计算偏差而丢弃包含大量正确前缀的整个序列，这不仅破坏了细粒度信用分配，还导致计算和内存开销呈指数级爆炸，使得在千亿参数模型上高效扩展不可行。本文提出的核心问题是如何打破这种自回归诅咒，即克服早期微小认知扰动沿马尔可夫决策流不可逆传播并级联放大的缺陷，赋予推理过程自我纠错能力，而无需依赖外部信号或全局重采样。

### Q2: 有哪些相关研究？

在强化学习优化大语言模型推理能力方面，相关工作可归纳为方法类和评测类。方法类中，GRPO 移除 PPO 中的 critic 模型，通过组级相对奖励估计优势，降低了推理模型的训练成本；DAPO 通过解耦裁剪、动态采样和令牌级策略梯度损失等方法缓解熵坍缩并提升训练稳定性；GSPO 用序列级似然比替代令牌级重要性比，使策略优化更稳定；SAPO 以平滑温度控制缩放替代硬裁剪，实现更稳定的策略更新；BAPO 研究离线 RL，通过平衡自适应裁剪保持策略熵并稳定优化；DisCO 将推理 RL 重构为判别式约束优化，缓解组级目标的难度偏差。这些工作虽提升了 LLM 推理能力，但均未有效解决生成早期微小扰动在马尔可夫决策过程中传播导致的长程推理崩溃问题。本文提出的 E³RL 与此类方法的核心区别在于：引入动态认知熵作为内在不确定性坐标，通过分段自适应动态阈值和优势分配实现局部逻辑缺陷的精确切除，并重用 KV 缓存流赋予模型自修复能力。在评测方面，DeepMath-103k 数据集被用于训练，AIME 等数学推理基准上的实验显示，E³RL 在 4B 和 8B 模型上分别超越此前 SOTA 达 5.349% 和 6.514%，验证了其在长序列推理中打破自回归诅咒的有效性。

### Q3: 论文如何解决这个问题？

E³RL通过将传统的一次性自回归生成重构为带检查点的迭代分段生成过程，来解决长程推理中的自回归诅咒问题。核心方法包括：首先将输出序列划分为N个非重叠段，每个段作为独立的局部决策窗口，从而将原本不可逆的决策链分解为可干预的局部步骤。关键技术在于构建了一个动态认知熵系统：对每个token计算认知熵H_t，通过滑动窗口平滑得到段级基不确定性Ñ_n，同时提取段内最大熵ð_n_max和熵变率Δð_n捕捉局部认知危机，三者加权组合为综合不确定性度量U_n。

在架构上，E³RL扩展了GRPO到段级优化：通过组采样计算每个段的群体均值和标准差，形成宏观动态基线β_n^macro；引入随擦除次数指数增长的惩罚因子Γ(e_n)和基于历史熵的调制函数φ，生成自适应擦除阈值Θ_n(e_n)。当段的不确定性U_n超过阈值时，非马尔可夫擦除算子执行回滚重试，否则接受当前段。此外，通过因果回溯注意力分配将最终序列奖励分解到各段，实现段级优势函数和策略优化目标。

创新点包括：1）无需外部信号，仅基于模型内生自回归交叉熵作为认知不确定性坐标；2）段级自适应动态阈值与优势分配，精准切除局部逻辑缺陷并复用KV缓存；3）显式的回滚-重试机制赋予推理过程自我修复能力。该方法在DeepMath-103k上训练，以线性内存开销实现了长序列推理的探索效率和样本效率提升。

### Q4: 论文做了哪些实验？

论文基于DeepMath-103k数据集（选取51k样本）进行强化学习训练，在Qwen3-4B和Qwen3-8B两种参数规模上，对比了Vanilla、GRPO、DAPO、GSPO、SAPO等主流方法。评测基准涵盖AMC 2023、AIME 2024/2025/2026、MATH 500、Minerva、OlympiadBench七个数学推理基准，采用Avg@32和Pass@32指标。

主要实验包括：（1）主对比实验：E³RL在4B/8B模型上均取得最佳Avg@32，在AIME 2024上分别达0.506和0.575，相较于SOTA提升5.349%和6.514%，同时Pass@32指标也普遍领先。（2）认知熵消融实验：去除基础不确定性（w/o base uncertainty）导致性能大幅下降（如AIME 2026从0.485降至0.426），仅保留梯度异常或极值偏差效果最差。（3）机制消融实验：去除组动态（w/o group dynamics）和因果分配（w/o causal allocation）均导致显著退化，仅用频率惩罚（ow frequency penalty）在AIME 2024/2025上分别降至0.467和0.386。（4）擦除数量实验：Erase@5优于Erase@1和Erase@3。（5）分段长度实验：16×512配置在AIME 2024上取得最佳Avg@32（0.583）。训练动态和Pass@k曲线分析显示E³RL具有更高的训练准确率和更稳定的多采样恢复能力。

### Q5: 有什么可以进一步探索的点？

E³RL的核心局限在于其对超参数的敏感性，特别是擦除次数和分段粒度。分析表明，Erase@5和16×512配置虽表现最优，但需大量手动调优以平衡计算开销与修正精度，且分段方案的语义有效性依赖任务特性，泛化性不足。未来研究可从三方面改进：其一，设计自适应分段机制，让模型根据输入复杂度动态调整分段长度，避免固定粒度导致的欠拟合或过度碎片化；其二，探索更细粒度的自纠错信号，例如结合上下文感知的贝叶斯不确定性估计替代当前基于交叉熵的固定阈值，降低对先验经验的依赖；其三，引入忆阻网络架构，将历史KV缓存与擦除决策进行可微分耦合，实现端到端的学习型纠错，而非当前启发式规则。此外，当前仅在数学推理上验证，需拓展至代码生成、多步规划等任务，并检验其在高维动作空间中是否仍能保持“自我修复”优势，避免因状态空间膨胀导致擦除策略退化。

### Q6: 总结一下论文的主要内容

该论文提出动态认知熵驱动的可擦除强化学习（E³RL），旨在解决大语言模型在长程逻辑推理中因早期微小认知扰动引发级联崩溃的“自回归诅咒”问题。该方法不再将生成视为不可逆的单次轨迹，而是通过模型内生的局部自回归交叉熵作为认知不确定性坐标，结合段级自适应动态阈值与优势分配，使模型能够精准切除局部逻辑缺陷，并复用历史KV缓存实现自愈。在DeepMath-103k数据集上训练后，E³RL在AIME等数学推理基准上显著提升性能，其中4B和8B参数模型分别超过先前最优5.349%和6.514%。实验表明，该方法在保持线性内存开销的同时重塑了长序列探索效率，为构建具有内生纠错能力的鲁棒自回归推理系统提供了理论与系统基础。
