---
title: "Scaling Self-Evolving Agents via Parametric Memory"
authors:
  - "Tao Ren"
  - "Weiyao Luo"
  - "Hui Yang"
  - "Rongzhi Zhu"
  - "Xiang Huang"
  - "Yuchuan Wu"
  - "Bingxue Chou"
  - "Jieping Ye"
  - "Jiafeng Liang"
  - "Yongbin Li"
  - "Yijie Peng"
date: "2026-06-03"
arxiv_id: "2606.04536"
arxiv_url: "https://arxiv.org/abs/2606.04536"
pdf_url: "https://arxiv.org/pdf/2606.04536v1"
categories:
  - "cs.AI"
tags:
  - "Agent 记忆"
  - "参数化记忆"
  - "在线学习"
  - "LoRA"
  - "强化学习"
  - "自我进化"
  - "LLM Agent"
relevance_score: 9.5
---

# Scaling Self-Evolving Agents via Parametric Memory

## 原始摘要

Existing memory-augmented LLM agents store past experience exclusively in prompt space, as textual summaries or retrieved passages, while keeping model parameters frozen throughout a rollout. Such agents can \emph{look up} what they have seen but cannot \emph{learn from} it: their policy is unchanged by experience, and any information dropped from the context is permanently lost. We introduce \texttt{TMEM}, a self-evolving parametric memory framework in which the agent not only compresses history into explicit memory but also absorbs distilled supervision into fast LoRA weights $Δ_t$ via lightweight online updates, genuinely altering its future behavior within a single episode. We formalize this as an agentic decision process with fast-weight rollout dynamics: actions are sampled from $π_{θ_0+Δ_t}$, while extraction actions produce supervision that updates $Δ_t$ for subsequent decisions. This view makes the extraction policy directly optimizable by RL: training $θ_0$ improves not only task actions but also the quality of the data used for online LoRA adaptation. We further propose SVD-based initialization of the LoRA subspace to accelerate online convergence. Experiments on LoCoMo, LongMemEval-S, multi-objective search, and CL-Bench show that \texttt{TMEM} consistently outperforms summary-based and retrieval-based baselines across different model scales.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有长时交互大语言模型（LLM）代理在记忆机制上的根本性缺陷：它们无法从经验中真正“学习”，而只能进行“查阅”。研究背景是在多轮对话、长序列工具使用等场景下，代理需要处理远超出单次上下文窗口的体验。现有方法主要通过两种方式在提示空间（prompt space）中存储经验：一是基于摘要的压缩，二是基于检索的索引。这些方法的共同不足在于，在整个执行过程中，模型参数始终保持冻结，其底层策略不会因经历而改变。任何被丢弃的上下文信息都会永久丢失，导致代理行为无法从历史经验中学习进化。更根本的是，即使信息被保留并重新放入提示中，代理也只是“看”到了它，而非将其“内化”为计算过程的一部分，这导致策略无法真正被经验塑造。为此，本文提出核心问题：能否让LLM代理在测试时直接将有用的经验写入自身参数，使得记忆能够改变后续决策的计算方式，而不仅仅是占据提示空间？即实现一种能够自我进化的参数化记忆机制，让代理通过在线轻量级参数更新来吸收反馈，从而在单个回合内改变其未来行为。

### Q2: 有哪些相关研究？

相关研究可归纳为四类。(1) **基于摘要的上下文管理**：如RecurrentGPT、MemAgent等通过压缩历史生成摘要。本文的区别在于摘要仅存在于提示空间，信息不可恢复，而TMEM将经验压缩到可更新的LoRA权重中，实现持续学习。(2) **检索增强的上下文管理**：如MemGPT、GraphRAG等通过外部存储检索相关记忆。本文指出检索依赖检索器质量且构建复杂，TMEM则通过在线参数更新直接改变策略，无需外部存储。(3) **测试时训练**：如TTT、Doc-to-LoRA等在推理时调整模型参数。但现有方法对整个上下文训练，更新成本高且未优化智能体记忆。TMEM仅从蒸馏记忆中更新快速权重，更高效且融入决策过程。(4) **自进化智能体**：如Reflexion、Voyager等通过跨回合经验积累进化。然而这些方法主要在回合间外部更新，TMEM实现单回合内参数自进化，使策略随经验实时变化。

### Q3: 论文如何解决这个问题？

论文提出了一种名为TMEM的参数化记忆框架，通过将历史经验压缩为显式记忆并同时吸收到快速LoRA权重中，使智能体能够在单次回合内真正从经验中学习并改变未来行为。核心方法形式化为一个具有快速权重展开的智能体决策过程：动作从自适应策略π_{θ₀+Δₜ}中采样，其中基础参数θ₀在回合内固定，而Δₜ通过轻量级在线SFT/LoRA更新（称为测试时训练TTT）动态演化。当工作上下文超过预设长度时，智能体会触发一个特殊提取动作，将当前会话中的信息蒸馏为结构化的SFT问答对（QA pairs）作为监督数据。这些QA对被用于快速在线LoRA更新，从而将经验直接写入参数空间，替代了传统方法中仅保留文本摘要或检索片段的做法。

在架构设计上，TMEM包含以下关键组件：1）混合记忆系统，同时维护显式文本记忆m_t和快速参数记忆Δₜ（LoRA权重）；2）基于上下文长度的提取触发机制，当上下文长度超过预算时自动进入提取模式；3）SVD初始化的LoRA子空间，利用预训练权重的奇异值分解初始化投影矩阵A（固定不变），仅在线更新系数矩阵B，从而在少量梯度步骤中快速收敛到当前任务所需的高能量子空间。整体框架将LoRA快速权重视为测试时记忆状态而非直接优化的RL参数，通过stop-gradient操作确保RL训练仅优化基础参数θ₀，使其能够生成更好的普通动作和提取动作，从而间接提升在线更新的质量。

创新点包括：1）首次将参数化记忆引入智能体展开过程，使策略能通过快速权重更新真正改变行为；2）将提取策略直接与RL优化相结合，使基础模型学会生成更适合后续LoRA适应的监督数据；3）SVD初始化的LoRA子空间，有效加速了在线测试时训练。实验表明TMEM在多个长期任务基准上显著优于基于摘要和检索的基线。

### Q4: 论文做了哪些实验？

论文在四个任务族上评估了TMEM框架：LoCoMo、LongMemEval-S、多目标搜索和CL-Bench。实验设置包括无记忆、基于摘要的记忆（MemAgent/MEM1）、基于检索的记忆（A-MEM）和TMEM四种记忆策略，以Qwen3-4B和Qwen3-8B为骨干模型。在对话记忆任务中，LoCoMo和LongMemEval-S使用token级F1和精确匹配(EM)指标。TMEM在LoCoMo上，Qwen3-4B和8B的F1分别为25.72和26.75，EM为15.40和20.24；在LongMemEval-S上，F1达41.24和41.87，EM为25.54和25.42，均优于其他基线。多目标搜索任务评估4目标和8目标场景，TMEM在有序答案列表上的F1/EM也最佳。CL-Bench用于上下文学习，使用过滤后的289个实例，以Qwen3-Max作为LLM评判评分，TMEM在各类别和总体准确率上均超越基线。所有实验均报告三次独立运行的平均值和标准差。

### Q5: 有什么可以进一步探索的点？

当前工作的核心局限在于LoRA权重的在线更新机制在长序列场景下的稳定性尚未充分验证，当任务复杂度增加时可能存在记忆污染或灾难性遗忘问题。未来可探索的方向包括：1) 引入元学习框架，让模型学会动态调整自适应速率，使Δ_t的更新幅度与任务需求自适应匹配；2) 设计层次化的参数记忆结构，将短期权重更新与长期可演化参数分离，避免单一权值矩阵承载过多冲突信息；3) 结合线性注意力机制优化LoRA更新的计算效率，将参数量化压缩与稀疏化技术结合以降低存储开销；4) 在提取策略中引入贝叶斯不确定性估计，使模型在知识积累不足时更倾向探索而非利用欠置信经验。值得特别关注的是，将在线参数记忆与离线元训练结合可能催生更接近人脑"睡眠巩固"机制的原型系统。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为TMEM的自演化参数记忆框架，解决了现有记忆增强型LLM代理只能查询历史但无法从经验中学习的问题。TMEM中，代理不仅将历史压缩为显式记忆，还通过轻量级在线更新将提炼的监督信号吸收到快速LoRA权重中，从而在单次回合内真正改变其未来行为。该方法将代理过程形式化为具有快速权重动态的决策过程，并通过强化学习优化基础模型，使其能生成高质量的在线适应数据。实验表明，TMEM在多个基准和模型规模上一致优于基于摘要和基于检索的基线方法。该工作的核心意义在于将记忆从被动存储转变为主动影响策略的参数化机制，为开发能持续演化学习的长周期LLM代理开辟了新方向。
