---
title: "Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling"
authors:
  - "Yucheng Li"
  - "Huiqiang Jiang"
  - "Yang Xu"
  - "Jianxin Yang"
  - "Yi Zhang"
  - "Yizhong Cao"
  - "Yuhao Shen"
  - "Fan Zhou"
  - "Rui Men"
  - "Jianwei Zhang"
  - "An Yang"
  - "Bowen Yu"
  - "Bo Zheng"
  - "Fei Huang"
  - "Junyang Lin"
  - "Dayiheng Liu"
  - "Jingren Zhou"
date: "2026-06-10"
arxiv_id: "2606.12370"
arxiv_url: "https://arxiv.org/abs/2606.12370"
pdf_url: "https://arxiv.org/pdf/2606.12370v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "agent加速训练"
  - "多token预测"
  - "拒绝采样"
  - "RL训练优化"
  - "端到端TV损失"
  - "speculative decoding"
  - "MTP"
  - "推理加速"
relevance_score: 9.5
---

# Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling

## 原始摘要

Reinforcement learning (RL) has become a key component in modern large language models, yet the rollout stage remains the key bottleneck in RL training pipelines. Although Multi-Token Prediction (MTP) offers a natural solution to accelerate rollouts through speculative decoding, many studies have observed that MTP acceptance rates degrade significantly during RL training, leading to limited speedup performance. To address this bottleneck, we present Bebop, a systematic study of MTP in LLM post-training, and offer practical recipes to integrate MTP into large-scale RL pipelines. First, we reveal that the MTP acceptance rate is fundamentally bounded by the fluctuation of model entropy, which demonstrates a clear negative linear relationship with the rise of entropy in the RL stage. Second, we show that probabilistic rejection sampling largely alleviates the disturbance introduced by entropy in RL compared to greedy draft sampling. We further identify that the conventional MTP training objectives (cross-entropy or KL) are suboptimal in such settings, and therefore we propose a novel end-to-end TV loss that directly optimizes multi-step rejection sampling acceptance rate, yielding ~10% acceptance rate improvements, achieving up to 95% acceptance rates and up to 25% extra inference throughput gains across mathematical reasoning, code generation, and agentic tasks. Third, we test various online MTP training strategies during RL and show that pre-RL MTP training with e2e TV loss and rejection sampling achieves a consistent acceptance rate and speedup throughout the entire RL, eliminating the need for costly online MTP updating. We provide extensive experiments and analysis that validate our findings. Experimental results show our method achieves up to 1.8x end-to-end acceleration in async RL training of Qwen3.5, Qwen3.6, and Qwen3.7 models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在大语言模型强化学习（RL）训练中，多令牌预测（MTP）加速效率严重下降的问题。研究背景是，RL训练已成为现代LLM的关键环节，但其中的推理（rollout）阶段是主要计算瓶颈。MTP通过推测解码（speculative decoding）天然可以加速rollout，但现有研究发现，在RL训练过程中，MTP的接受率会显著下降，导致加速效果有限。现有方法存在两个关键不足：其一，RL训练中模型为了鼓励探索，往往保持较高或逐渐上升的熵（entropy），这使得MTP模块难以准确预测草稿令牌，从而降低接受率；其二，RL过程中策略模型的权重更新会导致其与冻结的MTP模块之间存在分布不匹配。本文的核心问题是：如何克服RL训练中模型熵的波动对MTP接受率的根本性限制，从而实现稳定且高效的加速。具体而言，论文要解决传统贪心草案采样在熵升高时接受率被最大概率 \(\max_y p(y)\) 所束缚的问题，以及现有MTP训练目标（如交叉熵或KL散度）未能直接优化拒绝采样接受率的问题。论文提出Bebop方法，通过引入概率拒绝采样和一种端到端的总变差（TV）损失函数，来直接提升多步拒绝采样下的接受率，并探究了RL训练前进行轻量级MTP训练的策略，以期在不进行在线MTP更新的情况下，在整个RL训练过程中保持一致的加速效果。

### Q2: 有哪些相关研究？

相关研究主要分为以下几类：

**1. 推测解码方法类：** 本文基于Multi-Token Prediction (MTP)框架，这是一种通过轻量级草稿头预测多个未来token来加速自回归生成的推测解码方法。与早期的投机解码工作相比，MTP将草稿与验证集成在单一模型中，而非使用独立的草稿模型。本文的核心贡献在于首次系统研究了MTP在强化学习（RL）训练过程中的退化机制，发现熵的波动是导致接受率下降的主导因素，突破了传统“分布不匹配”的认知。

**2. 加速LLM训练类：** 本文聚焦于RL训练中的rollout瓶颈，该阶段是RL流水线中最耗时的部分。虽然有异步RL、部分rollout等方法来缓解长尾轨迹带来的开销，但本文是第一篇将MTP作为端到端加速方案引入RL训练的工作，提出了实用的训练策略（如预RL阶段的MTP训练、端到端TV损失），实现了高达1.8倍的端到端加速。

**3. 采样与验证方法类：** 本文比较了两种接受方法：Target-Only Sampling（贪婪草稿）和Rejection Sampling（概率接受）。关键发现是，在RL训练中，Rejection Sampling能有效缓解熵变化带来的扰动，因为它直接优化了总变差距离(TV distance)。本文进一步提出端到端TV损失来直接优化多步接受率，而非传统的交叉熵或KL散度，这是与现有工作在训练目标上的本质区别。

**4. 在线训练策略类：** 实验表明，采用预RL阶段的MTP训练（结合TV损失和Rejection Sampling），可以在整个RL训练过程中保持稳定的接受率和加速比，消除了昂贵的在线MTP更新需求。这与那些需要在RL训练中持续更新草稿模型的方法形成了鲜明对比。

### Q3: 论文如何解决这个问题？

论文的核心方法是Bebop框架，旨在解决强化学习训练中多令牌预测接受率因模型熵波动而显著下降的问题。整体框架围绕三个关键部分展开：首先是揭示熵对接受率的根本性约束，证明在目标模型熵增加时，基于贪婪采样和交叉熵/KL散度训练的草稿模型的接受率会线性下降；其次是提出关键技术，即端到端总变差损失；最后是设计高效的无在线更新的MTP适配策略。

在架构设计上，Bebop包含一个主模型和一个轻量级草稿头。主模型生成目标分布p，草稿头生成草稿分布q。传统方法使用交叉熵或KL散度训练草稿头，但论文通过梯度分析指出，这些损失函数会导致均匀的令牌级不匹配，在高熵时总变差距离随有效支持集大小指数增长，从而产生熵依赖。创新的核心是端到端TV损失，它直接优化拒绝采样接受率对应的总变差距离：L_TV = 1 - Σ_v min(p(v), q(v))。该损失函数的梯度与q_j成正比，自然实现尾部抑制，仅关注与接受决策相关的高概率令牌，从而产生概率比例不匹配。理论证明，在批量受限下，TV损失训练使总变差距离有与熵无关的上界，将熵-接受率斜率降低95%以上。此外，针对多步MTP的乘积结构，论文进一步提出端到端TV损失，通过动态步进权重优化期望接受长度，自动侧重当前限制接受的步骤。

基于上述机制，论文通过分解分析证明，在拒绝采样下，RL权重更新引起的草稿-目标不匹配几乎为零，因此无需在线更新MTP。只需在RL前进行一次带有TV损失的预适配，即可在整个RL训练中保持稳定的高接受率，消除额外内存和计算开销。实验表明，该方法在数学推理、代码生成等任务上达到95%接受率，实现高达1.8倍异步RL训练加速。

### Q4: 论文做了哪些实验？

论文进行了三组实验。**实验设置**：主要基于Qwen3.5-35A3B模型，使用混合RFT数据，学习率3.5e-5，采用Megatron框架，全局批大小256，序列长度256K，MTP步数为5，评估时γ=3（即目标模型一次验证4个token）。**对比方法**包括CE Loss、KL Loss、Reverse KL Loss、单步TV Loss和作者提出的端到端多步TV Loss（e2e TV Loss），同时对比了贪心草稿采样和概率拒绝采样。**主要结果**：(1) 在SFT阶段，e2e TV Loss在拒绝采样下持续提升接受率3-8%（数学+3.0%，代码+3.3%，SWE+8.0%，Agent+6.7%），在OOD的MT-Bench上也提升2.3%。(2) 在RL阶段，拒绝采样结合TV Loss相比贪心采样和CE Loss能维持更高且稳定的接受长度，端到端加速达1.8倍。(3) 模型规模扩展实验中，Qwen3.7-Max在Agent任务上接受率达94.6%，且TV Loss在后续MTP步骤优势更明显（Step 3高出约5%）。RL实验在数学推理（HMMT25、AIME25）、代码（LiveCodeBench）和SWE任务（SWE-Verified）上进行，生成长度达64K-128K tokens。

### Q5: 有什么可以进一步探索的点？

未来的探索可以从以下几点展开：首先，论文只验证了单层MTP，多层MTP能否在熵波动下通过rejection sampling维持高速率值得研究，且TV loss是否对更深层更鲁棒需进一步分析。其次，在线MTP更新虽被指出不必要，但若RL训练分布大幅偏移，静态MTP可能失效，可探索自适应调整策略（如周期性重训练MTP头部或动态调整采样温度）。第三，TV loss直接优化拒绝采样接受率，但可能牺牲生成多样性，未来可引入多样性正则化项（如熵奖励）。最后，当前方法仅在数学、代码等任务验证，在对话、指令遵循等熵变化更剧烈的场景下性能尚未明确，需扩展至更多任务并量化加速比与熵的关系。此外，将MTP与Flash Attention等推理优化结合，有望进一步突破吞吐瓶颈。

### Q6: 总结一下论文的主要内容

强化学习（RL）已成为大型语言模型训练的关键范式，但推理阶段的高计算成本构成主要瓶颈。本论文提出Bebop，系统研究多token预测（MTP）在RL训练中的应用。首先，论文揭示MTP接受率受到模型熵波动的根本限制，两者呈现清晰的负线性关系。其次，相比贪婪采样，概率拒绝采样能显著缓解熵波动对接受率的干扰。论文进一步指出现有MTP训练目标（交叉熵或KL散度）在此场景下是次优的，因此提出端到端全变差（TV）损失函数，直接优化多步拒绝采样接受率，实现约10%的提升，使接受率达到95%，并通过提升2.5%推理吞吐量加速RL训练。最后，实验表明在RL训练前使用端到端TV损失和拒绝采样进行轻量级MTP训练，即可在整个RL过程中保持一致的接受率和加速效果，无需昂贵的在线MTP更新。在数学推理、代码生成和智能体任务上，使用Qwen3.5/3.6/3.7模型，Bebop实现了异步RL训练端到端最高1.8倍的加速。
