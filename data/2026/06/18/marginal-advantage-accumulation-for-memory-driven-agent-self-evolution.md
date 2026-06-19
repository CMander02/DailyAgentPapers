---
title: "Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution"
authors:
  - "Mingyu Yang"
  - "Keye Zheng"
  - "Congchao Cheng"
  - "Yujie Liu"
  - "Xingkang Lu"
  - "Fan Jiang"
  - "Yefei Zheng"
date: "2026-06-18"
arxiv_id: "2606.20475"
arxiv_url: "https://arxiv.org/abs/2606.20475"
pdf_url: "https://arxiv.org/pdf/2606.20475v1"
categories:
  - "cs.LG"
tags:
  - "Agent自我进化"
  - "内存驱动"
  - "边际优势累积"
  - "批式轨迹蒸馏"
  - "信号积累机制"
  - "语义身份合并"
  - "Agent架构创新"
relevance_score: 9.0
---

# Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution

## 原始摘要

In batch-style trace distillation, the same memory operation may receive contradictory feedback across different batches. Existing methods lack a cross-batch, operation-level evidence accumulation mechanism, making it impossible to distinguish stably effective operations from accidental hits. This paper formalizes the requirement as two structural conditions, alignability and comparability, and proposes Marginal Advantage Accumulation (MAA). MAA constructs differential signals to make them comparable across batches, accumulates signed evidence per operation via EMA, and ensures cross-batch traceability through semantic identity merging. As a post-processing architecture, MAA achieves the best results in 14 out of 16 settings across 4 benchmarks and 4 target models, consistently outperforming existing batch-level distillation baselines and matching or surpassing online alternatives in most settings, while reducing optimization-phase token consumption by approximately 75%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决批式记忆蒸馏中，跨批次操作级证据积累缺失导致的“局部有效、全局不稳定”问题。在研究背景上，LLM智能体在持续使用中需要自我进化，非参数化范式下的轨迹蒸馏是关键，它从执行轨迹中压缩出可复用的记忆库（如技能、经验）。然而，工业部署面临两个硬约束：一是无法进行线上重评估（成本过高），只能依赖廉价代理信号（如LLM评判）；二是轨迹集合远超单次LLM上下文窗口，迫使蒸馏必须以批次为单位进行。

现有方法（如SkillOpt、Trace2Skill）仅在单个批次内做局部优化，导致同一优化操作在不同批次中可能收到矛盾的反馈（例如，为二维图表添加轴标签的操作在热图批次中反而导致错误）。由于缺乏跨批次证据积累机制，系统无法区分“稳定有效”的操作与“偶然命中”的操作。因此，该论文的核心问题是：如何设计一种跨批次、操作级别的证据积累机制，使得系统能基于历史批次中积累的一致性证据，而非单次批次的局部信号，来做出更可靠的记忆优化决策。论文将此需求形式化为两个结构性条件：对齐性（跨批次识别同一操作）和可比性（确保不同批次信号具有一致尺度）。

### Q2: 有哪些相关研究？

相关研究主要分为在线和离线两大类。本文提出的MAA属于离线架构，其核心区别在于跨批次操作级证据积累机制。

**1. 单次蒸馏与离线层次蒸馏类：** 包括Reflexion、Self-Refine、ExpeL、Voyager、AWM（单次提取）以及Trace2Skill（层次归纳）。这些方法仅执行一次蒸馏，优点是避免了MAA所解决的“可对齐性”和“可比性”问题，但缺点是无法利用多批次证据抵消来过滤虚假操作，一旦写入错误建议便无法修正。MAA通过跨批次EMA累积证据，实现了后续批次的纠正能力。

**2. 响应式可进化记忆类：** 如A-MEM、Evo-Memory、MEMO、MemGPT等，支持add/edit/remove等更新原语，但每个编辑决策仅基于当前批次的局部视角，缺乏跨批次的操作标识。这导致同一操作在不同批次中被视为不同实体，无法对齐正负证据，且无法分离“操作质量”与“批次难度”的混淆效应。MAA通过语义身份合并和差分信号构建，确保了跨批次的可追溯性和可比性。

**3. 在线优化类：** 包括SkillOpt、SkillGrad（在线部署）以及OPRO、APE、DSPy、TextGrad等（提示/文本梯度优化）。在线方法从真实环境中获得高方向可靠性信号，但每次滚动的代价高昂；而提示级方法的状态积累停留在版本层面，无跨批次操作级证据。MAA与它们不同，仅基于现有轨迹（无需环境交互），并借用了“将编辑组织为优化过程”的思想，但通过逐操作EMA实现了跨批次的证据累积与校正。

**4. 强化学习类：** 如PPO、GRPO、DPO等，通过模型权重的梯度更新实现进化，与MAA的修改对象（上下文注入内容）正交。RL需要GPU训练且存在灾难性遗忘风险，而MAA无需训练且不修改未触发的记忆项，两者可结合部署。

### Q3: 论文如何解决这个问题？

MAA提出了一个后处理架构，核心是构建跨批次、操作级别的证据积累机制。整体框架分为三个模块：可寻址记忆库、边际优势信号构造和跨批次累积。

首先，将记忆库M抽象为可寻址的文本块集合，每个块有唯一id。对记忆的修改通过add和modify两种操作单元（op）实现，每个op由(type, anchor)和内容向量唯一标识。为解决不同批次中语义等价但表述不同的操作，引入语义身份合并机制：使用轻量嵌入模型计算op的语义向量，仅当type、anchor相同且余弦相似度≥0.85时合并为同一累积单元，避免身份碎片化。

关键技术在于边际优势信号构造。直接对记忆打分会混合批次难度和操作质量，MAA通过同批次基线差分构建差分信号δ_i = u(M_t^{(i)}, B_t) - u(M_t, B_t)，将绝对判断转化为局部比较，满足可比性要求。Score通道对基线和所有候选状态进行并排估值，随机打乱顺序消除位置偏差。δ_i的符号稳定性是累积有效性的前提。

跨批次累积机制是核心创新。对每个op，使用指数移动平均(EMA)聚合多个批次的边际优势：m_{k,t} = β·m_{k,t-1} + (1-β)·δ_{k,t}，并加入偏差修正项。EMA同时实现非平稳适应（指数衰减使近期证据快速主导）和振幅保留（区分“显著改进”和“轻微改进”），复杂度O(1)。累积量\hat{m}_{k,t}作为候选池管理和更新决策的统一依据：低于阈值m_{floor}=-50的丢弃，超过容量上限20的按累积量排序截断，超过max_age=10步未选中的淘汰。每步的更新预算k_t由线性衰减的比率r_t控制，使早期探索充分、后期更新保守，最终选取累积量大于0的top-k_t操作执行。

### Q4: 论文做了哪些实验？

论文围绕四个研究问题展开实验。实验设置：采用5个独立随机种子，报告均值±标准差。数据集包括ScienceAgentBench（科学Agent，高复杂度，代码通过率）、ALFWorld（具身Agent，中高复杂度，任务成功率）、HotpotQA（多跳QA，低复杂度，精确匹配）、SpreadsheetBench（电子表格，中复杂度，准确率），每个数据集使用500条训练轨迹。对比方法包括：Frozen（无记忆基线）、Single-shot（ExpeL/Trace2Skill风格一次性蒸馏）、Reactive Update（无累积消融）、Trace2Skill（离线层级蒸馏）、SkillOpt（在线技能优化）和MAA（本文方法）。目标模型覆盖Qwen3.7-Max（强模型）、Qwen3.6-Flash（弱模型）、DeepSeek-V4-Flash（跨系列弱模型）和GPT-5.4（跨系列强模型）。

主要结果：MAA在16个设置中14个取得最佳。在Qwen3.7-Max上，MAA全面超越SkillOpt：ScienceAgentBench 30.7% vs 30.3%，ALFWorld 89.4% vs 88.1%，SpreadsheetBench 58.5% vs 56.2%，HotpotQA 77.2% vs 76.9%。在GPT-5.4上也全面领先。在弱模型上，MAA在除ScienceAgentBench外的任务上最优。消融实验验证了差分信号和连续幅度的必要性：从Reactive Update到Abs-score EMA再到Counting-δ EMA最后到Continuous-δ EMA（MAA），性能逐步提升。符号诊断显示，δ符号一致性超过88.7%，方向准确性约61.5%-73.8%。MAA相比SkillOpt减少了约75%的优化阶段token消耗（8.5M vs 33.3M）和约1/5的训练时间。

### Q5: 有什么可以进一步探索的点？

论文的局限性与未来方向如下：MAA目前依赖于语义身份合并和EMA累积，这在大规模、动态变化的环境下可能面临遗忘或特征冲突问题。未来可以探索动态调整EMA衰减系数，或引入概率图模型来建模操作间的因果关系。另一个不足是MAA仅作为后处理架构，未能与模型训练过程完全耦合，未来可研究端到端的学习方式，使记忆更新与梯度传播协同。此外，当前方法主要针对同质化反馈，对于存在异质性、延迟奖励或长尾操作的情况处理不足。可以尝试结合强化学习中的信用分配机制，如反事实推理或时序差分学习，来提升对稀疏和非稳定反馈的鲁棒性。最后，跨设备或分布式场景下的MAA扩展也是一个有前景的方向，需要解决通信开销与一致性问题。

### Q6: 总结一下论文的主要内容

这篇论文针对批处理式轨迹蒸馏中的一个关键缺陷——同一操作在不同批次中可能收到矛盾反馈，而现有方法缺乏跨批次、操作级别的证据积累机制——提出了边际优势积累方法。作者首先形式化定义了跨批次操作需要满足的两个结构性条件：可对齐性和可比性。方法核心在于，通过语义身份合并实现操作跨批次追踪，利用差分信号构建跨批次可比的有界优势值，并采用指数移动平均（EMA）累加同一操作在多个批次的证据。该后处理架构无需重新部署agent，即可在优化阶段减少约75%的token消耗。在4个基准和4个目标模型共16个设置中，MAA有14个取得最佳结果，一致超越现有批处理蒸馏基线，并在多数设置中匹敌或超越在线方法。工作的重要意义在于揭示了将局部编辑选择转化为跨批次证据积累是提升非参数神经自进化能力的关键设计空白。
