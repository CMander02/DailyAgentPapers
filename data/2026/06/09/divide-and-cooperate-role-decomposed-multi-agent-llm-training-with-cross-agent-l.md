---
title: "Divide and Cooperate: Role-Decomposed Multi-Agent LLM Training with Cross-Agent Learning Signals"
authors:
  - "Jaewan Park"
  - "Solbee Cho"
  - "Jay-Yoon Lee"
date: "2026-06-09"
arxiv_id: "2606.10684"
arxiv_url: "https://arxiv.org/abs/2606.10684"
pdf_url: "https://arxiv.org/pdf/2606.10684v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Multi-Agent Framework"
  - "Role Decomposition"
  - "Credit Assignment"
  - "LLM Training"
  - "Knowledge-Intensive QA"
  - "Cross-Agent Learning"
  - "Parameter-Efficient Fine-Tuning"
  - "Search and Reasoning"
relevance_score: 9.5
---

# Divide and Cooperate: Role-Decomposed Multi-Agent LLM Training with Cross-Agent Learning Signals

## 原始摘要

Modern language agents which perform multi-step reasoning have shown strong performance in knowledge-intensive question answering. However, existing approaches typically couple evidence acquisition and answer generation within a single policy. This forces a single model to play multiple potentially conflicting roles, inducing a combinatorial explosion in the policy space and hindering efficient exploration. It also introduces a credit assignment problem during training: a search action that retrieves sufficient evidence may still be penalized when generation fails, and vice versa. We propose DAC (Divide and Cooperate), a role-decomposed multi-agent training framework that divides agentic search into two cooperative subtasks, each handled by a dedicated agent trained with role-specific learning signals. The generator serves a dual role as both an answer producer and an evidence sufficiency verifier, abstaining when retrieved evidence is insufficient. This abstention signal is incorporated into the search agent's reward, providing structured cross-agent learning signals that improve credit assignment. Conversely, the searcher exposes the generator to diverse and challenging evidence environments by hard-positive evidence augmentation, improving its robustness. Experiments on general and multi-hop QA benchmarks show that DAC, implemented via parameter-efficient LoRA modules over a shared backbone, achieves strong performance against prior baselines that rely on full fine-tuning of monolithic models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多步推理语言代理系统中存在的角色耦合与探索效率低下的问题。研究背景是，面对知识密集型问答任务，现有方法通常将证据获取与答案生成功能捆绑在同一个推理策略中。这种单一模型需要同时扮演“搜索者”和“生成者”两个潜在冲突的角色，导致策略空间呈组合爆炸式增长，阻碍了高效探索。同时它还带来了严重的信用分配难题：在训练中，一个能够成功检索到充分证据的搜索动作，可能因为后续生成步骤的失败而受到错误惩罚；反之，一个糟糕的搜索也可能因为偶然的正确答案而被错误奖励。针对这些不足，本文提出的核心方法是构建一个“分而治之”的多智能体训练框架（DAC），将智能搜索任务分解为两个合作的子任务，分别由专用的代理（搜索者与生成者）处理。引入角色专用的学习信号，特别是让生成者同时充当答案产出者和证据充足性验证者，当证据不足时选择拒绝回答。这种“弃权信号”被结构性地融入搜索者的奖励中，从而改善了跨智能体的信用分配，解决了旧框架中因角色耦合而导致的激励错位。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为三类：**方法类**、**训练类**和**评测类**。
- **方法类**：主流工作如ReAct、Iter-RetGen等将证据检索与答案生成耦合在单一策略中，导致策略空间爆炸与信用分配问题。本文的DAC框架通过角色分解，分别训练搜索与生成两个专用智能体，并利用生成器的“弃权信号”作为搜索器的结构化跨智能体学习信号，解决了信用分配难题。
- **训练类**：现有工作如STaR、RLRR等大多使用全模型微调，对计算资源要求高。本文采用共享骨干网络上的参数高效LoRA模块，实现分离角色训练，同时通过硬正例证据增强提升生成器的鲁棒性，这是与以往训练方式的核心区别。
- **评测类**：相关基准包括HotpotQA、2WikiMultihop等通用与多跳问答数据集。DAC在这些评测上超越仅使用全微调单体模型的前沿基线方法，证明了角色分解与跨智能体信号的有效性。

### Q3: 论文如何解决这个问题？

该论文提出DAC（Divide and Cooperate）框架，将传统单智能体的多步推理拆分为两个独立协作的子任务，分别由专门的智能体处理。整体架构基于共享骨干网络（如LLaMA），通过参数高效的LoRA模块为每个智能体实现角色特化，避免全参数微调的高成本。

核心方法包括两大模块：搜索智能体（Searcher）负责证据检索，通过强化学习优化搜索策略；生成智能体（Generator）同时承担答案生成和证据充分性验证的双重角色。当检索到的证据不足时，生成智能体可主动“弃权”（abstain）并触发额外搜索，这一弃权信号被编码为结构化的跨智能体学习信号，直接反馈给搜索智能体的奖励函数，从而解决传统方法中搜索与生成之间的信用分配难题——即使搜索行为正确，若生成失败也不会被错误惩罚。

关键技术方面，DAC引入硬正例证据增强（Hard-Positive Evidence Augmentation），让搜索智能体暴露于多样化且具有挑战性的证据环境，提升生成智能体的鲁棒性。两个智能体通过交叉学习信号（cross-agent learning signals）相互协作：弃权信号优化搜索策略，而增强证据则强化生成能力。实验表明，在通用和多跳问答基准上，该方法优于依赖全参数微调单体的基线模型，证明了角色分解与协作训练的有效性。

### Q4: 论文做了哪些实验？

论文在 General QA 和 Multi-hop QA 两类基准上进行了实验。实验设置包括：使用 Llama-3-8B-Instruct 作为共享骨干，通过 LoRA 微调实现角色解耦的搜索代理和生成代理。对比方法包括：直接 Prompt 的 CoT、CoT-SC、ReAct，以及全参数微调的 LLM 基线如 FIMO、SKR、IRCoT、Search-and-Study 等。主要结果如下：1) **General QA (NQ, TriviaQA, WebQ)** 上，DAC 以 40.7 的 F1 在 NQ 上超过全参数微调的 FIMO (38.8) 和 Search-and-Study (36.4)；在 TriviaQA 上 F1 达到 53.2，显著高于所有基线。2) **Multi-hop QA (HotpotQA, 2WikiMultiHopQA, MuSiQue)** 上，DAC 在 HotpotQA 的 F1 达 43.8，超越 ReAct (28.2) 和 IRCoT (39.5)；在 MuSiQue 上以 18.7 的 F1 领先所有方法。3) **消融实验** 证实了角色解耦、硬正例证据增强和跨代理学习信号的每项贡献，移除任一组件均导致性能下降。4) **鲁棒性分析** 显示 DAC 在低搜索预算下仍保持优势，其生成代理能有效检测证据不足并触发正确拒答。

### Q5: 有什么可以进一步探索的点？

该论文虽通过角色解耦解决了多步推理中的信用分配问题，但仍存在若干局限和可探索方向。首先，其参数高效微调（LoRA）虽节省资源，但共享骨干可能限制各角色的专业能力上限，未来可探索独立参数与混合专家架构。其次，生成器作为证据充分性的仲裁者其自身判断可能不准确，引入外部验证器或自我反思机制可增强可靠性。第三，当前仅将生成器的弃权信号作为搜索代理的反馈，但搜索代理缺乏对生成过程的细粒度奖励，可引入过程奖励模型提供步骤级反馈。最后，该方法主要针对单跳和多跳问答，在需要更复杂推理（如数学证明或多步规划）的领域需调整解耦策略，建议构建基于动态角色切换的元学习框架以适应广泛任务。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为DAC（Divide and Cooperate）的角色分解多智能体训练框架，旨在解决知识密集型问答中单一模型同时承担证据检索和答案生成导致的多角色冲突与信用分配问题。DAC将智能体搜索分解为两个协作子任务：搜索智能体负责收集证据，生成智能体负责生成答案并兼任证据充分性验证者。当检索证据不足时，生成智能体可主动弃权，并将弃权信号作为结构化学习信号反馈给搜索智能体以优化信用分配；同时搜索智能体通过困难正样本增强，提升生成智能体在多样复杂证据环境中的鲁棒性。实验表明，DAC基于共享骨干网络的参数高效LoRA模块实现，在通用和多跳问答基准上性能优于依赖全参数微调单一大模型的基线方法，验证了角色分解和跨智能体学习信号的有效性。
