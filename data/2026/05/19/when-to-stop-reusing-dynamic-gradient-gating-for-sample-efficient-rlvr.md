---
title: "When to Stop Reusing: Dynamic Gradient Gating for Sample-Efficient RLVR"
authors:
  - "Yuchun Miao"
  - "Sen Zhang"
  - "Yuqi Zhang"
  - "Yaorui Shi"
  - "Qi Gu"
  - "Xunliang Cai"
  - "Lefei Zhang"
date: "2026-05-19"
arxiv_id: "2605.19425"
arxiv_url: "https://arxiv.org/abs/2605.19425"
pdf_url: "https://arxiv.org/pdf/2605.19425v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "强化学习"
  - "样本效率"
  - "梯度门控"
  - "RLVR"
  - "Agent训练"
relevance_score: 8.5
---

# When to Stop Reusing: Dynamic Gradient Gating for Sample-Efficient RLVR

## 原始摘要

Reinforcement Learning with Verifiable Rewards (RLVR) has become the dominant paradigm for advanced reasoning in Large Language Models (LLMs), but rollout samples are expensive to obtain, making sample efficiency a critical bottleneck. A natural remedy is to reuse each rollout batch for multiple gradient updates, a standard practice in classical RL. Yet in RLVR, this amplifies policy shift, leading to severe performance degradation. Detecting the onset of degradation early enough to stop reuse remains an open and challenging problem. We close this gap by identifying the \textit{Disproportionate Weight Divergence (DWD)} phenomenon: performance degradation is synchronized with a sharp surge in the \texttt{lm\_head} weight change, while intermediate layers remain stable. Empirically, we verify that DWD emerges consistently across diverse LLMs and tasks. Theoretically, we prove that (i) harmful gradients concentrate at the \texttt{lm\_head} while intermediate layers are structurally attenuated, and (ii) the \texttt{lm\_head} gradient norm lower-bounds the policy divergence. These results establish the \texttt{lm\_head} gradient norm as a principled, real-time signal of catastrophic policy shift. Guided by this insight, we propose \textit{Dynamic Gradient Gating (DGG)}, a lightweight intervention that monitors the \texttt{lm\_head} gradient norm in real time and intercepts harmful gradients before they corrupt the optimizer. DGG consistently matches or exceeds the standard single-use baseline, achieving up to $2.93\times$ sample efficiency and $2.14\times$ wall-clock speedup across math, ALFWorld, WebShop, and search-augmented QA tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在基于可验证奖励的强化学习（RLVR）中，对大规模语言模型（LLM）进行训练时存在的样本效率瓶颈问题。研究背景是，RLVR已成为提升LLM推理能力的主流框架，但生成训练所需的rollout样本代价高昂，消耗了超过80%的后训练GPU时间。虽然可以通过“样本复用”（即对同一批rollout数据进行多次梯度更新）来天然提升样本效率，但现有的方法存在严重不足：在RLVR中，直接复用样本会加剧更新策略与行为策略之间的策略偏移，导致训练崩溃，表现为性能急剧下降。因此，当前的生产化流程被迫采用保守的“单次使用”策略，严重浪费了昂贵样本的潜力，但如何及时检测到策略偏移的早期信号并停止复用，仍是一个未解决的难题。本文的核心问题正是如何可靠、实时地检测出样本复用可能引发灾难性训练崩溃的信号。为此，作者通过实证发现了“不成比例权重发散（DWD）”现象，即性能下降与语言模型头权重的急剧变化同步发生。通过理论分析证明有害梯度集中在语言模型头，且其梯度范数能够作为策略偏移的下界，从而提出动态梯度门控（DGG）机制，通过监控该梯度范数实现实时干预，在保持最终性能的同时，将样本效率提升至2.93倍、计算速度提升至2.14倍。

### Q2: 有哪些相关研究？

在相关研究方面，本文首先围绕**RLVR领域的样本效率**展开。现有方法主要针对**生成（rollout）阶段**进行优化，例如通过经验回放重塑生成分布，或根据提示难度和方差信号自适应分配生成资源。这些方法的核心局限在于，它们都严格遵循**单次使用原则**（single-use regime），即每个批次仅进行一次梯度更新，并未探索使用后的多轮利用。

本文的独特贡献在于开辟了一个全新的**更新阶段优化视角**：给定已生成的批次，如何安全地对其进行多次梯度更新以充分提取学习价值？与此相关的挑战是检测**灾难性策略偏移**，这在现有样本效率方法中鲜有研究。

在理论层面，本文与策略梯度中关于**梯度规范与策略偏移**的分析密切相关，但首次在LLM的RLVR场景中揭示了**不成比例权重发散（DWD）**现象：性能退化与`lm_head`层权重变化的急剧激增同步，而中间层保持稳定。本文从理论和实验两个层面证明了`lm_head`梯度范数可作为**灾难性策略偏移的实时信号**，并基于此提出**动态梯度门控（DGG）**方法：实时监控`lm_head`梯度范数，在有害梯度破坏优化器之前进行拦截。与现有单次使用基线（包括PPO等经典RL方法在LLM推理场景的变体）相比，DGG在数学、ALFWorld、WebShop和搜索增强QA等任务上实现了高达2.93倍的样本效率和2.14倍的加速。

### Q3: 论文如何解决这个问题？

论文通过识别“比例权重发散（DWD）”现象并基于此设计动态梯度门控（DGG）机制来解决RLVR中样本复用导致的性能退化问题。核心方法包含以下要点：

**DWD现象**：通过剖析Llama和Qwen系列（1.5B-8B参数）在数学推理、WebShop等任务上的训练动态，发现性能退化与lm_head层权重变化突增同步，而中间层保持稳定。理论证明（结构化梯度不对称定理）指出，有害梯度集中在lm_head层（因直接吸收误差信号E_i），中间层因雅可比投影J_i^T而被结构性衰减；且lm_head梯度范数下界约束策略偏移（皮尔逊χ²散度）。

**DGG架构**：基于Z-score检验的在线监测系统。实时计算lm_head梯度能量g_t及其增量Δg_t，维护均值和标准差运行估计，当瞬时Z分数超过阈值τ时触发两级干预：(1) 梯度丢弃——在Adam优化器前将梯度归零，防止污染动量估计；(2) 终止复用——退出复用循环并重新采样，打破策略漂移与重要性比率膨胀的正反馈。

**创新点**：首次从理论上建立lm_head梯度范数与灾难性策略偏移的数学认证关系，提出轻量级时序异常检测机制，仅需监控单层梯度即可实现实时拦截。实验表明DGG在数学推理、ALFWorld、WebShop和检索增强QA任务上，样本效率提升至单次基线的2.93倍，实际加速2.14倍。

### Q4: 论文做了哪些实验？

论文在多类任务上进行了系统实验。实验设置方面，使用Qwen3-4B-Instruct和Qwen2.5-7B-Instruct作为基座模型，最大重用次数K=4，异常阈值τ从{0.1, 0.5, 1.0}中选取。数学推理任务rollout分组大小为16，智能体任务为8。数据集/基准测试包括：数学推理用MATH500、AIME25、Minerva Math和Olympiad Bench，采用mean@16准确率；智能体任务涵盖ALFWorld、WebShop，以及基于HotpotQA、2Wiki、MuSiQue、Bamboogle的检索增强QA。对比方法为单次使用rollout的GRPO（标准基线）和固定重用的朴素GRPO。主要结果：DGG在所有16个设置中均能持续达到基线性能，实现2.00×–2.93×的rollout加速和1.31×–2.14×的壁钟时间加速（例如在Qwen2.5-7B数学任务上达2.93×和1.37×），且在最终性能上还有小幅提升。实验还验证了lm_head梯度范数作为监控信号的优越性——在崩溃时出现尖锐尖峰，而KL散度、裁剪比率和全局梯度范数均无此信号；DGG在所有固定重用机制中表现最佳，且超参数τ和K在广泛范围内均稳健有效。

### Q5: 有什么可以进一步探索的点？

该工作主要聚焦GRPO目标下的lm_head梯度，未来可探索以下方向：1) 验证DGG在标准PPO中的适用性，特别是value network collapse时value_head是否出现类似的结构性梯度异常；2) 将梯度门控机制推广到其他多步重用场景（如TRPO、off-policy RL）及更细粒度的层级（如中间层的注意力头部）；3) 当前方法依赖实时梯度监控，可尝试结合预测性剪枝或自适应重用步长，避免梯度计算开销；4) 在更复杂的多模态推理任务中验证DWD现象，并评估不同初始化下梯度分布的变化；5) 理论层面可进一步刻画单步梯度对策略偏移的“记忆效应”，建立更精确的复用次数上限估计，超越当前的经验式门控。

### Q6: 总结一下论文的主要内容

这篇论文聚焦于可验证奖励强化学习（RLVR）中样本效率低下的关键瓶颈问题。针对重复使用同批次样本进行多步梯度更新导致性能崩溃的现象，作者发现了一个名为“非比例权重发散”的结构性现象：性能恶化与语言模型头层权重的急剧变化同步发生，而中间层保持稳定。理论与实证均表明，有害梯度集中于lm_head，且该层梯度范数构成了策略散度的下界，因此可作为实时监测策略灾难性偏移的可靠信号。基于此，作者提出了动态梯度门控算法，通过实时监测lm_head梯度范数并在其异常激增时拦截有害梯度，防止优化器状态被破坏。实验证明，DGG在数学推理、代理任务等多个基准上能匹配或超越严格的单次使用基线，实现了高达2.93倍的样本效率和2.14倍的实际加速，显著提升了样本利用率。
