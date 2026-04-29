---
title: "JURY-RL: Votes Propose, Proofs Dispose for Label-Free RLVR"
authors:
  - "Xinjie Chen"
  - "Biao Fu"
  - "Jing Wu"
  - "Guoxin Chen"
  - "Xinggao Liu"
  - "Dayiheng Liu"
  - "Minpeng Liao"
date: "2026-04-28"
arxiv_id: "2604.25419"
arxiv_url: "https://arxiv.org/abs/2604.25419"
pdf_url: "https://arxiv.org/pdf/2604.25419v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "RLVR"
  - "形式化验证"
  - "推理增强"
  - "标签无关训练"
  - "多智能体投票"
relevance_score: 9.5
---

# JURY-RL: Votes Propose, Proofs Dispose for Label-Free RLVR

## 原始摘要

Reinforcement learning with verifiable rewards (RLVR) enhances the reasoning of large language models (LLMs), but standard RLVR often depends on human-annotated answers or carefully curated reward specifications. In machine-checkable domains, label-free alternatives such as majority voting or LLM-as-a-judge remove annotation cost but can introduce false positives that destabilize training. We introduce JURY-RL, a label-free RLVR framework that decouples answer proposal from reward disposal: votes from model rollouts propose a candidate answer, and a formal verifier determines whether that candidate can receive positive reward. Concretely, only rollouts matching the plurality-voted answer are rewarded when that answer is successfully verified in Lean. When verification is inconclusive, we invoke ResZero (Residual-Zero), a fallback reward that discards the unverified plurality proposal and redistributes a zero-mean, variance-preserving signal over the residual answers. This design maintains a stable optimization gradient without reinforcing unverifiable consensus. Across three backbone models trained on mathematical data, JURY-RL consistently outperforms other label-free baselines on mathematical reasoning benchmarks and transfers competitively to code generation and general benchmarks. It attains pass@1 performance comparable to supervised ground-truth training, with superior generalization demonstrated by higher pass@k and response diversity.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决强化学习中的可验证奖励（RLVR）在缺乏人工标注时面临的标签效率与训练稳定性矛盾。现有方法主要分为两类：一方面，基于多数投票的自监督奖励虽然无需人工标注，但容易强化错误共识，导致假阳性反馈和奖励黑客行为；另一方面，LLM作为评判者的方法存在提示敏感、计算开销大且易继承模型偏见的问题。这些方法的共同缺陷在于无法同时满足可扩展性、与真理对齐（即奖励真实正确性而非表面共识）和优化稳定性三个关键性质。核心问题在于：当没有人工标注的正确答案时，如何设计一种奖励机制，既能避免对错误共识的错误强化，又能保证逆向传播时的梯度稳定性？具体而言，多数投票带来的假阳性信号会破坏训练，而完全依赖形式化验证又因成本过高难以规模化。本文提出的JURY-RL框架通过解耦答案提议与奖励分配来解决这一矛盾：用模型生成的多数投票作为候选答案提议，但仅当形式化验证器（如Lean）确认该答案正确时才分配正向奖励；当验证无结论时，引入ResZero回退奖励机制，抛弃未验证的多数答案并对剩余答案分配零均值方差保持的信号，从而在不强化可疑共识的前提下维持优化梯度稳定。

### Q2: 有哪些相关研究？

LLM推理方面，现有方法如思维链和自我一致性虽能提升平均准确率，但缺乏外部校验时易放大错误。本文通过引入可验证奖励（RLVR）解决这一问题。无标签RLVR方面，已有工作采用多数投票、LLM-as-a-Judge等自监督信号替代人工标注，但容易因假阳性导致奖励破解和训练崩溃。JURY-RL与之区别在于，它通过Lean形式验证器作为最终奖励分配机制，避免强化不可验证共识的乐观偏差。验证器方面，现有基于验证的训练（如代码执行、单元测试或Lean/Coq等形式证明）在验证失败时通常不提供学习信号，限制了稳定性和样本效率。JURY-RL通过将提案与奖励裁决解耦，在验证成功时基于多数投票分配正奖励，失败时采用ResZero回退奖励（零均值、保持方差的重分布信号），从而维持稳定优化梯度。此外，与依赖学习型判别的过程奖励模型或混合验证器不同，JURY-RL的自动形式化管道是部署验证系统的一部分，其缺陷仅影响候选答案能否被认证，而非独立学习监督信号。

### Q3: 论文如何解决这个问题？

JURY-RL通过解耦答案提议与奖励分配来解决标签缺失下的RLVR不稳定问题。整体框架采用“投票提议-证明处置”的双阶段流水线：首先在提议阶段，针对问题生成G条轨迹并解析答案，通过多数投票选出单个候选答案；在处置阶段，仅对该候选答案调用一次Lean形式验证器，生成二进制门控信号。奖励分配由该门控信号决定：若验证通过，仅奖励与证明正确答案匹配的轨迹，将学习信号锚定在可验证的正确性上；若验证不成功，则启用ResZero（残差零均值）回退奖励机制。核心创新包括：第一，形式验证门控设计，只对多数投票候选进行单次验证，保持计算可行性同时消除虚假正例；第二，ResZero回退奖励，为维持优化稳定性而设计，当验证不确定时，它惩罚无法验证的多数答案，并在剩余答案上构造零均值方差保持信号。具体实现中，ResZero根据多数份额α动态缩放，对剩余答案放大奖励信号，对多数答案施加惩罚，总奖励严格归零以配合GRPO优化器。该设计确保了三个特性：方差保持、零均值构造和自适应经济性。最终，JURY-RL只需单次验证即可实现稳定的无标签强化学习，在数学推理基准上持续优于其他无标签基线，性能接近监督训练水平。

### Q4: 论文做了哪些实验？

论文在多种设置下进行了全面实验。实验使用Qwen3-1.7B-Base、Llama-3.2-3B-Instruct和Qwen2.5-7B三种骨干模型，涵盖基础和指令微调版本。训练采用VeRL框架，在8×NVIDIA A100 GPU上进行，从MATH数据集训练集中选取7,500个问题，使用GRPO算法，每步采样128个问题并生成8个rollout，学习率3e-6，KL惩罚系数0.005。评估基准涵盖数学推理（AIME24/25、MATH-500、GSM8K、AMC）、代码生成（LiveCodeBench、CRUX）和通用能力（IFEval、MMLU-Pro）。对比方法包括监督基线GT-Reward和LLM-KD，以及无监督基线Majority-Voting、Self-Certainty、Entropy minimization、CoReward和LLM-as-a-Judge。主要结果是JURY-RL在所有三个骨干模型上均优于所有无标签基线：Qwen3-1.7B上平均35.40%（GT-Reward为35.56%），Llama-3.2-3B上31.85%，Qwen2.5-7B上43.90%（与GT-Reward的43.90%持平）。在数学推理任务中，JURY-RL在pass@k上超越GT-Reward达+4.05pp（Qwen3-1.7B），在pass@1上达+4.00pp（Qwen2.5-7B）。

### Q5: 有什么可以进一步探索的点？

JURY-RL的局限性主要体现在对形式化验证环境的依赖（Lean），这限制了其在非机器可验证领域（如开放式问答、创意写作）的应用。未来可探索的方向包括：1）将形式验证器扩展到半结构化领域（如法律条文、科学实验记录），通过领域特化规则替代通用证明系统；2）ResZero的零均值信号在长尾分布场景中可能过于激进，可设计基于置信度的自适应分配策略，例如利用预测熵动态调节奖励方差。此外，当前框架假设投票多数即为正确答案，但在对抗性示例或歧义问题中可能失效，可引入不确定性量化机制（如贝叶斯投票）来缓解。从训练稳定性看，结合渐进式验证难度（先易后难）可能进一步提升泛化能力。

### Q6: 总结一下论文的主要内容

JURY-RL是一种无标签的RLVR框架，旨在解决标准RLVR依赖人工标注答案或精心设计的奖励规范的问题。核心贡献是解耦答案提议与奖励处置：通过模型rollout投票产生候选答案，再用形式验证器（Lean）决定该候选答案能否获得正奖励。当验证成功时，仅与多数投票答案匹配的rollout获得奖励；验证不成功时，引入ResZero（残差零均值）回退奖励，丢弃未验证的多数答案，并在剩余答案上重新分配一种零均值、保持方差的信号，从而维持优化梯度的稳定性，避免强化虚假共识。实验在三个骨干模型（Qwen3-1.7B、Llama-3.2-3B、Qwen2.5-7B）上，针对数学推理、代码生成和通用基准进行测试。主要结论是：JURY-RL持续优于其他无标签基线，在pass@1性能上与有监督的真实奖励训练相当，并展现出更好的泛化能力（更高的pass@k和响应多样性）。
