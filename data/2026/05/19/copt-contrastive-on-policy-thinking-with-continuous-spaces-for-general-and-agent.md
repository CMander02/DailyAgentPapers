---
title: "CopT: Contrastive On-Policy Thinking with Continuous Spaces for General and Agentic Reasoning"
authors:
  - "Dachuan Shi"
  - "Hanlin Zhu"
  - "Xiangchi Yuan"
  - "Wanjia Zhao"
  - "Kejing Xia"
  - "Wen Xiao"
  - "Wenke Lee"
date: "2026-05-19"
arxiv_id: "2605.20075"
arxiv_url: "https://arxiv.org/abs/2605.20075"
pdf_url: "https://arxiv.org/pdf/2605.20075v1"
github_url: "https://github.com/sdc17/CopT"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent推理"
  - "思维链改进"
  - "推理效率优化"
  - "不确定性估计"
  - "对比学习"
  - "LLM推理"
  - "无训练改进"
relevance_score: 8.5
---

# CopT: Contrastive On-Policy Thinking with Continuous Spaces for General and Agentic Reasoning

## 原始摘要

Chain-of-thought (CoT) is a standard approach for eliciting reasoning capabilities from large language models (LLMs). However, the common CoT paradigm treats thinking as a prerequisite for answering, which can delay access to plausible answers and incur unnecessary token costs even when the model is able to identify an answer before extended thinking, a behavior known as performative reasoning. In this paper, we introduce CopT, a reformulated reasoning pipeline that reverses the usual order of thinking and answering. Instead of thinking before answering, CopT first elicits a draft answer and then invokes subsequent on-policy thinking conditioned on its own draft answer for reflection and correction. To assess whether the draft answer should be trusted, CopT recasts continuous embeddings as inference-time contrastive verifiers. Specifically, it contrasts the model's support for the same generated tokens under discrete-token inputs and continuous-embedding inputs, yielding a sequence-level reverse KL estimator for answer reliability. Our analysis shows that under certain assumptions, the expected estimate equals the mutual information between the unresolved latent state and the emitted answer token, explaining why it captures answer-relevant uncertainty rather than arbitrary uncertainty in the latent state. When the answer is deemed insufficiently reliable, CopT performs further on-policy thinking, where a second KL estimator dynamically controls draft-answer visibility, preserving useful partial information while reducing the risk of being misled by unreliable content. Across mathematics, coding, and agentic reasoning tasks, CopT improves peak accuracy by up to 23% and reduces token usage by up to 57% at comparable or higher accuracy, without any additional training. The code is available at https://github.com/sdc17/CopT.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有链式思维（CoT）推理范式中的“表演性推理”问题。当前主流的CoT方法将“思考”作为“回答”的必经前置步骤，即模型必须先生成完整的推理链才能给出答案。然而，近期研究发现，对于许多查询，模型在内部其实已经能提前识别出可行答案，但仍会强制完成冗长的推理过程。这种行为不仅延迟了答案的获取，还导致大量不必要的token消耗，降低了效率。为克服这一不足，本文提出了CopT，一种全新的“先回答、后反思”推理范式。其核心是改变传统顺序：模型首先生成一个初步答案，再基于该答案进行后续的“策略性思考”以进行反思和修正。这带来了两个关键挑战：一是如何判断模型是否应该信任其生成的草稿答案，二是在后续思考中如何有效利用这个草稿。本文的创新在于将“连续嵌入”重新定义为推理时的对比验证器，通过对比模型在离散token输入和连续嵌入输入下对相同生成token的支持度，来估计草稿答案的可靠性，并动态控制其在后续思考中的可见性。该方法无需额外训练即可提升推理的准确性和token效率。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要可分为两类：

1. **推理LLMs与显式推理**：早期工作通过提示工程引导模型生成显式推理链（CoT）。近期如DeepSeek-R1、Qwen3等模型通过强化学习或多阶段后训练获得推理能力，但都遵循“先思考后回答”的标准顺序。本文CopT的创新在于反转这一顺序，先产生草稿答案，再根据其可靠性触发后续有策略思考。

2. **连续空间中的潜在推理**：这类方法在连续嵌入空间中进行推理，避免离散解码的信息损失。代表工作包括Soft-Thinking、SwiReasoning等。与传统潜在推理将连续嵌入作为生成媒介不同，CopT将其重新用作推理时的对比验证器，通过对比离散与连续输入下模型对同一生成token的支持度，构建序列级反向KL估计器来衡量答案可靠性。

此外，论文还涉及**功利主义推理**相关讨论，指出传统CoT在模型已能确定答案时仍强制进行冗长思考，导致“表演性推理”和token浪费。CopT通过动态控制草稿答案的可见性，既保留了部分有用信息，又减少了被不可靠内容误导的风险。

综上，CopT在方法上融合了显式推理的可读性和潜在推理的uncertainty捕捉能力，在应用上覆盖数学、编程和智能体推理任务，在评测上节省了高达57%的token消耗。

### Q3: 论文如何解决这个问题？

CopT通过反转传统思考-回答流程来解决大语言模型中的表演性推理和token浪费问题。其核心方法分为三个阶段：草稿答案生成、可靠性估计和基于策略的思考。

**整体框架**：首先强制模型直接输出答案令牌，跳过思考阶段生成草稿答案；然后通过对比离散令牌输入和连续嵌入输入下的模型支持度，计算序列级反向KL散度估计器来评估草稿可靠性；当可靠性不足时，触发后续的基于策略思考阶段，并动态控制草稿答案在思考过程中的可见性。

**主要模块**：
1. **草稿答案生成**：强制模型在输入后立即输出</think>令牌，直接进入回答模式，快速生成初步答案。
2. **可靠性估计模块**：为每个生成的草稿令牌缓存两个信息——选择令牌概率p_t和概率加权连续嵌入e_t。通过计算κ_a = (1/T_a)Σ[log p_θ(a_t|q,a_<t) - log p_θ(a_t|q,e_<t)]，在单次前向传播中比较离散前缀分布与连续前缀分布，该估计量是无偏的序列级反向KL散度估计，能捕获答案相关的不确定性而非任意潜在状态不确定性。
3. **基于策略思考模块**：当κ_a超过阈值τ_a时，激活思考过程。将思考序列划分为大小为C的块，对每个块计算κ_r^(k)来评估当前思考块的稳定性，当κ_r^(k)<τ_r时允许下一个块看到草稿答案，否则屏蔽草稿，从而动态平衡利用有益信息和避免误导。

**创新点**：一是在推理时通过对比离散和连续嵌入实现无训练的可信度估计器；二是动态可见性控制机制，在思考过程中基于块级稳定性自适应决定草稿可见性。该方法无需额外训练，在数学、编程和智能体推理任务中，峰值准确率提升高达23%，token使用量减少57%。

### Q4: 论文做了哪些实验？

CopT 在四个领域、10个基准上进行了实验：数学与STEM推理（GSM8K、Math500、AIME 2024/2025、GPQA Diamond）、代码推理（HumanEval、MBPP、LeetCode-Contest）以及单/多轮智能体推理（BFCL v4、ZebraArena）。模型涵盖Qwen3（2B/8B/35B）和Qwen3.5（2B/35B）系列。对比方法为标准CoT、贪心CoT以及使用连续嵌入的无训练方法Soft-Thinking和SwiReasoning。主要结果：(1) 在Qwen3-8B上，CopT在提升精度的同时显著减少token消耗：在GSM8K上精度提升+0.23%且token减少55.1%，在Math500上精度提升+0.20%且token减少27.6%，在AIME24/25上分别获得+3.34%和+2.92%的精度提升；代码任务中HumanEval精度提升+3.66%、LeetCode-Contest提升+6.67%；GPQA Diamond提升+2.02%。(2) 对比SwiReasoning，CopT在GSM8K、AIME25、HumanEval、GPQA上精度分别提升+0.30%/0.42%/0.61%/0.51%，token减少18.3%/8.0%/36.4%/18.0%。(3) 智能体任务中，在ZebraArena大分集上精度提升高达+23.03%，token减少19.6%。(4) 消融实验证实了草稿可靠性估计器κa能有效识别错误草稿，且可见性控制κr能提升纠错率。

### Q5: 有什么可以进一步探索的点？

论文提出的 CopT 范式主要在离散 token 和连续 embedding 输入之间进行对比来估计答案可靠性，但其对比机制依赖于模型内部隐状态的 KL 散度，这在复杂多模态或长程推理任务中可能因序列耦合导致估计偏差。未来可探索的方向包括：1) 将对比验证器扩展为多层级（如跨层、跨头注意力对齐），以捕获不同推理阶段的语义分歧；2) 设计自适应 draft 长度控制策略，避免因过短的 draft 丢失关键推理线索；3) 引入参数化置信度校准模块，在无需训练的前提下通过少量推理样本学习更鲁棒的可靠性阈值；4) 将 CopT 与检索增强生成（RAG）结合，使 draft 生成能主动调用外部知识库，从而提升初始答案质量。这些改进有望在保持零训练成本的同时，进一步缓解“表演性推理”导致的资源浪费。

### Q6: 总结一下论文的主要内容

CopT提出了一种新的LLM推理流程，颠覆了传统的“先思考后回答”模式。该方法首先让模型生成一个草稿答案，然后在该答案的基础上进行后验的“政策内思考”，以进行反思和修正。核心贡献在于将连续嵌入重新用作推理时的对比验证器：通过比较同一生成token在离散token输入和连续嵌入输入下的模型支持度，计算序列级别的逆向KL散度作为答案可靠性的估计。理论分析表明，该估计量等价于未解析潜在状态与发射答案token之间的互信息。当草稿答案不可靠时，CopT会进行后续推理，并由第二个KL估计量动态控制草稿的可见性。在数学、编程和智能体推理任务上，CopT最高提升了23%的峰值准确率，并在达到相当或更高准确率的同时减少了最多57%的token消耗，且无需任何额外训练。这项工作为更经济高效的LLM推理提供了实用路径。
