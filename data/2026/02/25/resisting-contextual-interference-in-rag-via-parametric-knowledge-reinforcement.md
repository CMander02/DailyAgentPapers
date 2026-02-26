---
title: "Resisting Contextual Interference in RAG via Parametric-Knowledge Reinforcement"
authors:
  - "Chenyu Lin"
  - "Yilin Wen"
  - "Du Su"
  - "Hexiang Tan"
  - "Fei Sun"
  - "Muhan Chen"
  - "Chenfu Bao"
  - "Zhonghou Lyu"
date: "2025-06-05"
arxiv_id: "2506.05154"
arxiv_url: "https://arxiv.org/abs/2506.05154"
pdf_url: "https://arxiv.org/pdf/2506.05154v4"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.IR"
tags:
  - "Agent 推理"
  - "工具使用"
  - "检索增强生成"
  - "强化学习"
  - "知识冲突"
  - "鲁棒性"
relevance_score: 7.5
---

# Resisting Contextual Interference in RAG via Parametric-Knowledge Reinforcement

## 原始摘要

Retrieval-augmented generation (RAG) improves performance on knowledge-intensive tasks but can be derailed by wrong, irrelevant, or conflicting retrieved text, causing models to rely on inaccurate evidence and cascade errors. We propose Knowledgeable-R1, a reinforcement-learning framework that explicitly trains large language models to use parametric knowledge (PK) to resist contextual interference while still exploiting external context when it is reliably helpful. Knowledgeable-R1 introduces a joint sampling scheme that generates paired responses with and without retrieval, and learns both local advantages (within each decoding regime) and global advantages under the same input to quantify when to ignore misleading context versus adopt it. We employ an asymmetric advantage transformation that amplifies exploratory behaviors toward parametric knowledge. Experiments show that Knowledgeable-R1 significantly improves robustness and reasoning accuracy in knowledge conflict scenarios and general RAG scenarios, outperforming SOTA baselines by +22.89% in counterfactual scenarios, and without degradation when the retrieved context is fully accurate.Our code are available at https://github.com/lcy80366872/knowledgeable-R1.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决检索增强生成（RAG）系统中一个关键问题：当检索到的外部上下文信息存在错误、不相关或与模型内部参数知识冲突时，大型语言模型（LLMs）会过度依赖这些不可靠的上下文，导致性能下降和错误级联，即所谓的“上下文主导”现象。

研究背景是，RAG通过整合外部知识来增强LLMs，减少幻觉和事实错误，已成为处理知识密集型任务的主流方法。然而，现有方法存在明显不足：1）提示工程方法需要手动引导模型验证或过滤上下文，缺乏通用性且增加计算复杂度；2）基于解码的方法通过调整生成过程中的令牌分布来缓解冲突，但同样缺乏可推广的决策规则；3）微调方法（如Self-RAG）训练模型隐式学习知识利用规则，但通常依赖复杂的数据标注流程，限制了灵活性和可扩展性。这些方法都未能系统性地教导模型在何时应忽略误导性上下文并回退到可靠的内部参数知识。

因此，本文要解决的核心问题是：如何设计一个强化学习框架，使LLMs能够明确学习并权衡利用参数知识和上下文知识，特别是在上下文具有干扰性或冲突时，能主动抵抗干扰、依靠自身知识做出正确判断，同时在上下文可靠时又能有效利用它。论文提出的Knowledgeable-R1框架通过联合采样、局部与全局优势评估以及非对称优势转换等技术，旨在实现这一目标，提升RAG系统在知识冲突和一般场景下的鲁棒性与推理准确性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、评测类和强化学习应用类。

在方法类研究中，已有工作针对RAG中检索到无关或对抗性段落的问题，提出了噪声注入训练、注意力掩码和对抗性过滤等方法，或在检索前后进行段落级过滤与加权。然而，这些方法缺乏在生成过程中主动抑制有害上下文的内在机制。本文提出的Knowledgeable-R1框架则通过强化学习，在解码层面动态训练模型依据参数知识抵抗误导性上下文，是对现有方法的重要补充。

在评测类研究中，近期基准测试已开始系统性地关注知识冲突场景，为评估模型鲁棒性提供了基础。本文的实验正是在此类场景下验证了方法的有效性。

在强化学习应用类研究中，已有工作利用RL引导模型的推理过程（如生成内部原理或稳定思维链），但主要聚焦于推理结构优化。本文的创新在于将RL应用于协调参数知识与上下文知识的学习，使模型能自主判断何时依赖内部知识、何时采纳外部检索结果，从而拓展了RL在LLM知识管理中的应用方向。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Knowledgeable-R1的多目标强化学习框架来解决RAG中因检索到错误、不相关或冲突文本而导致的上下文干扰问题。其核心思想是显式训练大语言模型，使其能够利用参数知识来抵抗误导性上下文，同时在外部上下文可靠时有效利用它。

整体框架基于强化学习，定义了三种不同的解码策略（或称策略分支）来分别优化三个目标：参数知识分支（PK）在仅输入查询时生成基于参数知识的答案；上下文感知分支（CK）在输入查询和检索上下文时生成利用上下文的答案；鲁棒参数知识分支（RPK）在输入查询和检索上下文时，仍生成与参数知识一致的答案。RPK的实现是关键创新：它并非独立生成答案，而是先通过PK分支采样一个参数知识答案轨迹，然后在相同的查询+上下文输入下重新评估该轨迹的概率，并通过奖励机制鼓励模型在面对误导性上下文时仍能维持参数知识答案。

关键技术包括创新的优势计算方案和非对称优势变换。优势计算结合了局部优势和全局优势。局部优势在同一策略分支和输入类型内部比较轨迹，确保各分支自身优化。全局优势则针对相同的查询+上下文输入，将CK和RPK的轨迹放在一个统一的池中比较，从而量化何时应忽略上下文（选择RPK）或采纳上下文（选择CK）。这种设计使模型能在同一输入状态下进行跨知识源的决策。

非对称优势变换是针对训练中CK路径通常获得更高奖励、导致模型过度依赖上下文的问题而设计的。它对RPK路径的优势值进行调制：当优势值为正（RPK表现好）时保持不变；当优势值为负（RPK表现相对较差）时，则用一个小于1的系数β进行缩放，从而减轻对RPK的惩罚，鼓励模型在必要时仍将参数知识作为可行的回退选项。系数β还能根据CK与RPK的性能差距动态调整，以平衡对两种知识源的探索。

在训练目标上，采用PPO风格的更新，为PK、CK和RPK分别构建目标函数，并进行加权求和作为总目标进行优化。整个方法使单一模型能够根据上下文可靠性，自适应地在参数知识和外部上下文之间做出权衡，最终在上下文冲突或噪声场景中显著提升鲁棒性和推理准确性，同时在上下文完全准确时性能不下降。

### Q4: 论文做了哪些实验？

论文在五个逐步困难的上下文场景中进行了实验，以评估模型在外部上下文干扰下利用参数知识产生准确答案的能力。实验设置方面，模型使用了Qwen2.5-3B/7B/14B-Instruct和Llama3.1-8B-Instruct，对比方法包括仅查询提示、RAG提示、Astute-RAG、CK-PLUG、SFT以及GRPO w/ RAG。训练时所有方法使用相同总量数据训练一个epoch，采用全局批次大小128、rollout批次大小32、rollout温度1和学习率1e-6，并在8块H100 GPU上运行。评估指标为精确匹配（EM）。

使用的数据集/基准测试包括：针对正确与错误上下文（S1, S2）的ConFiQA（包含PC-QA/MR/MC和NC-QA/MR/MC子集）；针对冲突上下文（S3）的自建SC数据集；针对无关上下文（S4）的ExplainPE医学QA数据集；以及针对部分相关上下文（S5）的HotpotQA、2WikiMultiHopQA和MuSiQue。这些数据集用于模拟真实检索中可能出现的误导性上下文。

主要结果显示，Knowledgeable-R1在具有挑战性的干扰场景（S2-S5）中显著提升了鲁棒性和推理准确性，同时在正确上下文（S1）中性能未下降。关键数据指标包括：在对抗性上下文（S2）中，Qwen2.5-7B-Instruct在NC-MR/MC/QA上相比RAG提示分别提升了+30.47%、+29.28%和+18.09个百分点；在冲突上下文（S3）中，该模型达到63.77%的准确率；在无关上下文（S4）的ExplainPE上达到67.57%；在部分相关上下文（S5）的2WikiMultiHopQA上达到37.52%。特别是在参数知识可回答的子集上，该方法在错误或混合上下文中的平均表现比GRPO w/ RAG提升了22.89%。这些结果验证了该方法能有效选择可靠证据并忽略误导信息。

### Q5: 有什么可以进一步探索的点？

该论文提出的Knowledgeable-R1框架在缓解检索上下文干扰方面取得了显著进展，但仍存在一些局限性和可进一步探索的方向。首先，其训练依赖于成对的带检索与不带检索的响应生成，这在计算成本和数据准备上可能带来挑战；未来可研究更高效的采样策略或离线强化学习方法以降低训练开销。其次，当前方法主要针对知识冲突场景，但在动态知识更新或多模态检索增强生成（RAG）中的泛化能力尚未验证；可探索如何将框架扩展至时序知识库或跨模态检索场景。此外，论文中的“非对称优势变换”虽然鼓励模型依赖参数知识，但可能在某些边缘案例中过度抑制有用上下文；未来可引入更精细的置信度校准机制，动态权衡参数知识与检索证据。最后，该框架未深入探讨模型参数知识本身的局限性（如知识陈旧性），结合持续学习或知识编辑技术来更新参数知识，可能是提升长期鲁棒性的关键方向。

### Q6: 总结一下论文的主要内容

该论文针对检索增强生成（RAG）中检索到的错误、无关或冲突文本会误导模型、导致错误传播的问题，提出了一种名为Knowledgeable-R1的强化学习框架。其核心贡献是训练大语言模型主动利用其内部参数知识来抵抗上下文的干扰，同时在外部检索内容可靠时仍能有效利用它。

方法上，论文设计了联合采样方案，为同一输入生成带检索和不带检索的成对响应，并学习局部优势（在每种解码机制内）和全局优势，以量化何时应忽略误导性上下文或采纳有用上下文。此外，通过引入非对称优势变换，放大了模型探索和依赖参数知识的行为。

实验结果表明，该方法在知识冲突场景和一般RAG场景中显著提升了鲁棒性和推理准确性，在反事实场景下比现有最佳基线性能提升22.89%，且在检索上下文完全准确时性能不会下降。这项工作增强了RAG系统对不可靠检索的抵抗力，推动了更稳健的检索增强生成技术的发展。
