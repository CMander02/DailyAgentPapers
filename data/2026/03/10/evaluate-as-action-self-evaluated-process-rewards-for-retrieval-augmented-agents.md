---
title: "Evaluate-as-Action: Self-Evaluated Process Rewards for Retrieval-Augmented Agents"
authors:
  - "Jiangming Shu"
  - "Yuxiang Zhang"
  - "Ye Ma"
  - "Xueyuan Lin"
  - "Jitao Sang"
date: "2026-03-10"
arxiv_id: "2603.09203"
arxiv_url: "https://arxiv.org/abs/2603.09203"
pdf_url: "https://arxiv.org/pdf/2603.09203v1"
categories:
  - "cs.AI"
tags:
  - "Retrieval-Augmented Generation"
  - "Multi-Step Reasoning"
  - "Process Reward"
  - "Reinforcement Learning"
  - "Question Answering"
  - "Self-Evaluation"
  - "Agent Architecture"
relevance_score: 8.5
---

# Evaluate-as-Action: Self-Evaluated Process Rewards for Retrieval-Augmented Agents

## 原始摘要

Retrieval-augmented agents can query external evidence, yet their reliability in multi-step reasoning remains limited: noisy retrieval may derail multi-hop question answering, while outcome-only reinforcement learning provides credit signals that are too coarse to optimize intermediate steps. We propose \textsc{EvalAct} (Evaluate-as-Action), which converts implicit retrieval quality assessment into an explicit action and enforces a coupled Search-to-Evaluate protocol so that each retrieval is immediately followed by a structured evaluation score, yielding process signals aligned with the interaction trajectory. To leverage these signals, we introduce Process-Calibrated Advantage Rescaling (PCAR), a GRPO-based optimization method that rescales advantages at the segment level according to evaluation scores, emphasizing reliable segments while updating uncertain ones conservatively. Experiments on seven open-domain QA benchmarks show that \textsc{EvalAct} achieves the best average accuracy, with the largest gains on multi-hop tasks, and ablations verify that the explicit evaluation loop drives the primary improvements while PCAR provides consistent additional benefits.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决检索增强智能体在多步推理任务中可靠性不足的核心问题。研究背景是，尽管大型语言模型（LLM）智能体能够通过检索增强生成（RAG）利用外部证据进行开放域问答，但随着任务从单跳事实查询转向复杂的多跳推理，智能体在冗长且充满噪声的交互序列中导航、验证和综合证据的能力成为关键瓶颈。

现有方法主要存在两大不足。首先，现有基线方法（如交织检索与推理的提示方法，或基于强化学习的搜索智能体）主要依赖模型内部的隐式推理来进行噪声抑制和自我纠正。这导致错误传播问题：由于缺乏对检索证据进行显式、即时验证的机制，单个不相关文档就可能误导后续推理，在多跳场景中造成不可逆的轨迹漂移。其次，信用分配过于粗糙：标准的强化学习优化（如基于PPO的RLHF或仅依赖最终答案正确性的结果奖励方法）通常使用与最终答案正确性绑定的稀疏奖励信号。这种仅基于结果的监督无法区分长轨迹中有信息量的检索步骤与冗余或误导性的动作，导致优化器几乎均匀地强化或惩罚整个轨迹，从而降低了样本效率，并在任务复杂性增加时导致性能饱和。

因此，本文要解决的核心问题是：如何为检索增强智能体提供更精细、与推理过程对齐的监督信号，以缓解错误传播并实现更优的中间步骤信用分配，从而提升其在多步推理，尤其是多跳问答任务中的可靠性和性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：检索增强生成（RAG）、用于训练智能体的强化学习（RL）方法，以及将隐式行为显式化的动作空间扩展研究。

在**检索增强生成（RAG）**方面，早期研究致力于通过稠密编码器或神经重排序器提升检索质量。近期工作则将检索直接集成到推理过程中，实现迭代查询。Self-RAG通过特殊令牌评估检索效用，但这仍是隐式信号。本文的EvalAct在此基础上，将检索评估转化为一个能产生离散分数的**显式、结构化动作**，从而提供训练信号。

在**强化学习（RL）训练智能体**方面，Search-R1等工作表明，仅使用结果奖励的纯RL可以训练有效的检索策略，但在多步推理中存在信用分配困难的问题。过程奖励模型（PRMs）通过提供步骤级监督来解决此问题，但通常依赖昂贵的人工标注或可能与目标策略不一致的外部验证器。LeTS设计了基于知识冗余和精确匹配的检索专用过程奖励，但依赖于可能泛化性不足的启发式方法。本文提出的PCAR方法则通过基于评估分数在片段级别重新调整优势值，实现了细粒度的信用分配，且无需显式的校准训练。

在**扩展动作空间**方面，MemAct将工作记忆管理（如上下文删除和插入）制定为策略动作。本文的EvalAct共享这种以动作为中心的视角，但针对的是**检索质量评估**这一不同行为，将其从自由形式推理中的隐式部分，转化为能产生过程信号的显式动作，以优化中间步骤。

### Q3: 论文如何解决这个问题？

论文通过提出 **EvalAct（Evaluate-as-Action）** 框架及其配套的 **PCAR（Process-Calibrated Advantage Rescaling）** 优化方法，系统性地解决了检索增强智能体在多步推理中因噪声检索和粗粒度奖励信号导致的可靠性问题。

**核心方法与架构设计**：  
整体框架将多跳问答建模为部分可观测的序列决策过程（POMDP）。智能体的动作空间包括推理令牌、工具动作（检索与评估）和终止回答动作。EvalAct 的核心创新在于引入了 **耦合的“搜索→评估”协议**：每次执行检索动作 `Search(q)` 后，智能体必须立即执行一个显式的评估动作 `Evaluate(c, z)`，其中 `c` 是文本评估，`z` 是 0-10 的置信度分数。这一设计将隐式的检索质量评估转化为可执行的、由策略选择的具体动作，从而为每个检索步骤生成即时的、与交互轨迹对齐的过程信号。

**关键技术模块**：  
1. **评估动作与环境反馈**：环境不解析评估内容，而是将置信度分数 `z` 通过映射函数 `Φ(z)` 转换为离散的控制提示（低、中、高），并追加到上下文中，以指导后续决策。这使得智能体能在无外部监督的情况下，根据自评估分数进行推理控制。  
2. **过程校准的优势重缩放（PCAR）**：这是基于 GRPO（Group Relative Policy Optimization）的优化方法。首先，对轨迹中每个检索-评估段的自评估分数进行组内标准化，得到相对可靠性信号。然后，根据分数计算每个段的缩放增益，并用于重缩放 GRPO 计算的优势值。具体地，属于段 `k` 的令牌的优势值被调整为 `Â = A · clamp(1 + λ·z̃, δ, ∞)`，其中 `A` 是原始组归一化优势，`λ` 是分数相关的增益，`z̃` 是标准化后的可靠性信号。这种重缩放强调可靠段（高置信评估）的更新，而对不确定段（低置信评估）进行保守更新。  
3. **门控结果奖励**：奖励函数结合了答案质量（F1分数）和协议遵守性（确保每个 Search 后紧跟 Evaluate），以同时优化最终答案和中间过程的可靠性。

**创新点**：  
- **显式评估循环**：将评估作为可执行动作，强制形成搜索与评估的紧耦合，为多步推理提供细粒度的过程监督信号。  
- **过程校准的优化机制**：PCAR 利用自评估分数在段级别重缩放策略梯度，实现了更精细的信用分配，增强了学习稳定性，并有效区分了可靠与不可靠的中间步骤。  
- **完全自监督**：整个框架无需外部评估器或人工标注，仅依赖智能体自身的评估分数和最终答案奖励进行训练。  

实验表明，EvalAct 在多跳任务上提升显著，且消融研究验证了显式评估循环是性能提升的主要驱动力，而 PCAR 则提供了持续的额外增益。

### Q4: 论文做了哪些实验？

实验在七个开放域问答基准上进行，涵盖单跳和多跳任务。单跳数据集包括Natural Questions (NQ)、PopQA和TriviaQA；多跳数据集包括HotpotQA、2WikiMultihopQA、MuSiQue和Bamboogle。实验使用公开的ASearcherBase35K语料库进行训练，并经过轻量过滤得到27k个样本用于强化学习。此外，通过提示DeepSeek-V3.2合成2k条符合协议轨迹用于监督预热。

对比方法包括：直接生成（Direct Generation）、朴素检索增强生成（Naïve RAG）、IRCoT（交织检索与思维链）、Search-o1、Search-R1以及AutoRefine（迭代精炼基线）。所有检索方法使用相同的检索环境（基于2018年12月维基百科转储的BM25检索器，返回top-k=3文档，搜索调用上限为20次）。实验使用Qwen2.5-3B-Instruct和Qwen2.5-7B-Instruct作为骨干模型，在8张NVIDIA A100 GPU上进行全参数优化。主要评估指标为精确匹配（EM）。

主要结果显示，EvalAct在平均EM上达到最佳：EvalAct-3B为44.0%，EvalAct-7B为47.1%，分别比次优基线AutoRefine高出3.5和1.6个百分点。在多跳任务上优势显著，例如在2WikiMultihopQA上，EvalAct-3B比AutoRefine高10.6分（50.0% vs 39.4%）；在Bamboogle上高13.6分（48.0% vs 34.4%）。在单跳任务上，EvalAct保持竞争力但未全面超越AutoRefine，例如在NQ上EvalAct-7B为38.5%，低于AutoRefine的48.4%。实验表明，显式评估循环对多步推理任务提升明显，而过程校准优势重缩放（PCAR）提供了稳定的额外收益。

### Q5: 有什么可以进一步探索的点？

该论文提出的EvalAct框架虽在检索增强智能体上取得进展，但仍存在局限性与可拓展方向。首先，其强制性的“检索后必评估”耦合机制虽能提供密集过程信号，但限制了智能体的自主决策能力。未来可探索动态评估触发机制，让智能体学会在不确定性高时自主启动评估，实现更灵活的资源分配。其次，当前验证仅局限于开放域问答任务，在更复杂的场景（如网页导航、代码生成）中，状态空间和动作依赖关系更为复杂，需进一步验证其样本效率与泛化能力。此外，实验仅基于7B参数模型，未来需研究该方法在更大规模开源模型或闭源大模型上的迁移效果。结合个人见解，可能的改进包括：引入元学习机制让智能体自适应学习评估策略；将过程奖励与分层强化学习结合，以处理更长期的任务规划；探索多模态环境下的评估动作设计，以支持更广泛的智能体应用场景。

### Q6: 总结一下论文的主要内容

该论文针对检索增强智能体在多步推理中因检索噪声和粗粒度奖励信号导致的可靠性问题，提出了EvalAct框架。其核心贡献是将隐式的检索质量评估转化为显式的评估动作，并强制采用“检索后即评估”的协议，从而为每一步交互生成结构化的过程奖励信号。方法上，论文设计了基于GRPO的优化方法PCAR，它依据评估分数在片段层级重新调整优势函数，以强调可靠片段并保守更新不确定部分。实验在七个开放域QA基准上进行，结果表明EvalAct取得了最佳平均准确率，尤其在多跳任务上提升显著。主要结论是，将中间评估转化为可训练的动作，能为多步检索增强推理提供更精细的过程监督，从而有效提升智能体的性能和可靠性。
