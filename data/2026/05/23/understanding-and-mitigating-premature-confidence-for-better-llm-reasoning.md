---
title: "Understanding and Mitigating Premature Confidence for Better LLM Reasoning"
authors:
  - "Jingchu Gai"
  - "Guanning Zeng"
  - "Christina Baek"
  - "Chen Wu"
  - "J. Zico Kolter"
  - "Andrej Risteski"
  - "Aditi Raghunathan"
date: "2026-05-23"
arxiv_id: "2605.24396"
arxiv_url: "https://arxiv.org/abs/2605.24396"
pdf_url: "https://arxiv.org/pdf/2605.24396v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent推理"
  - "思维链"
  - "置信度校准"
  - "强化学习"
  - "推理质量"
relevance_score: 7.5
---

# Understanding and Mitigating Premature Confidence for Better LLM Reasoning

## 原始摘要

Long chains of thought (CoT) from current language models frequently contain logical gaps and unjustified leaps, limiting the gains from additional test-time compute. Improving reasoning quality directly would require process reward models, but the step-level annotations needed to train them are expensive and scarce. We find such a signal in how the model's confidence evolves during reasoning: premature confidence, the tendency to commit to an answer early and use the remaining tokens to rationalize it, strongly predicts flawed reasoning across tasks and model scales. We exploit this in progressive confidence shaping, a reinforcement learning objective that trains models to update their confidence as they reason rather than commit early -- rewarding gradual confidence growth and penalizing early commitment, with no external labels or reward models. The method improves accuracy and reasoning quality from 1.5B to 8B parameters across arithmetic (Countdown), math (DAPO, AIME), and science (ScienceQA): on Countdown, accuracy improves 3.2x (+42.0pp) and flawed reasoning drops 48pp; on AIME, Pass@64 improves 6.6pp. Consistent with this mechanism, the method also improves faithfulness: on a safety benchmark, our models more transparently surface misleading content in their reasoning traces rather than concealing it. Controlled experiments reveal that the problem and its remedy scale together: premature confidence grows with model size and task difficulty, and so do the gains from addressing it.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型在长思维链推理中普遍存在的“过早自信”问题。研究背景是，虽然链式思维推理通过提示学习和强化学习推动了复杂推理任务的发展，但模型生成的长推理链中经常出现逻辑跳跃、矛盾等缺陷，导致额外的测试时计算未能带来应有收益。现有方法中，直接改进推理质量需要过程奖励模型来评估中间步骤，但此类模型依赖昂贵且稀缺的逐步标注数据；而基于结果奖励的强化学习虽然能优化答案，却无法改善推理过程本身，甚至可能加剧模型推理的不忠实性——模型实际计算过程与生成的推理链不一致。

本文的核心研究贡献在于：第一，通过实证发现“过早自信”现象——模型在推理链早期就确定了答案，后续只是为其辩护——能强烈预测推理中的逻辑缺陷，且这一现象在模型规模和任务难度增大时更为严重。第二，基于这一发现提出“渐进式信心塑造”方法，这是一种新的强化学习目标，通过探测模型在推理链各截断点的置信度轨迹，构建奖励信号来惩罚早期固化自信、奖励逐步增长的信心演化，从而无需外部标签或奖励模型。该方法在多个推理任务和模型规模上均显著提升了准确率和推理质量，同时增强了推理链的忠实性。

### Q2: 有哪些相关研究？

以下是与本文相关的研究工作，按类别组织：

**方法类：** 本文与过程奖励模型（PRM）紧密相关，PRM 通过为推理的中间步骤打分来提升推理质量，但需要昂贵的逐步标注。本文提出的渐进置信塑造（progressive confidence shaping）是一种替代方案，它利用模型自身的置信度轨迹作为免标注的强化学习信号，避免了 PRM 对外部标注的依赖。此外，本文基于 GRPO 强化学习框架，区别于仅使用结果奖励的常规 RL 方法，将置信度动态直接纳入优势函数。

**评测与分析类：** 相关工作包括对链式思维推理（CoT）中逻辑缺口、不忠实推理的研究。本文首次系统揭示了“过早自信”（premature confidence）现象，并证明其与逻辑缺陷的高度相关性。不同于先前工作仅通过外部监控器检测逻辑错误，本文从模型内在的置信度演化中提取信号。

**应用与扩展类：** 本文在算术、数学、科学推理及安全性基准上的实验表明，该方法能同时提升准确率和推理忠实度。尤其在安全任务中，模型更透明地暴露误导性内容，这区别于仅关注准确率的传统方法。本文还分析了“推理效用”与“推理可及性”两种竞争力量，解释了为什么大模型和难题上过早自信更严重，这与先验直觉（难题应促进谨慎推理）相反。

### Q3: 论文如何解决这个问题？

这篇论文通过提出“渐进式置信度塑形”（Progressive Confidence Shaping）方法，直接利用模型自身在推理过程中的置信度演化轨迹作为训练信号，来缓解大语言模型在长思维链中的“过早自信”问题。该方法摆脱了对过程奖励模型或昂贵步骤级标注的依赖。

其核心方法基于GRPO（分组相对策略优化）框架进行改造。整体框架是：在RL训练的每一步，对于模型生成的每个完整回答，在思维链上均匀选取K个截断点（论文使用6个点：0%, 20%, …, 100%）。在每个截断点处，让模型基于当前已生成的推理过程输出最终答案，并通过多次蒙特卡洛采样，计算该答案与真实标注一致的频率，以此作为该点的置信度得分，从而形成一个K维的置信度轨迹向量。

关键技术在于使用一个单调递减的评分向量w对置信度轨迹进行加权内积。w的权重设定为在早期截断点为正（惩罚过早达到高置信度），在后期截断点为负（鼓励渐进式置信度增长）。该内积结果乘以一个系数η后，作为“过早自信惩罚”项，从原始GRPO优势函数中减去，生成新的成形优势函数。通过这一机制，模型被迫学习在推理过程中不断更新并逐步建立信心，而非过早做出结论。

主要模块包括：GRPO基础RL框架、基于截断点的置信度轨迹提取模块、以及关键的置信度塑形惩罚项。创新点在于：1) 无需额外标注或外部模型，直接从模型自身行为中提取首个可量化的信号；2) 设计了灵活的评分向量w，可针对不同任务特性调整惩罚强度；3) 通过将置信度信号直接嵌入RL优势函数，同时实现了“对错误推理中部分正确进展的奖励”和“对正确但过早自信的惩罚”双重效果，有效提升了推理准确率和推理轨迹的忠实度。

### Q4: 论文做了哪些实验？

论文在三个推理领域进行了实验。**实验设置**：(1) 合成算术 (Countdown)，使用 Qwen2.5-3B，分简单 (4-10-50) 和困难 (4-30-100) 两种设置；(2) 数学问题求解 (DAPO, AIME)；(3) 科学问答 (SciQA)，使用 Qwen3-1.7B/4B/8B。**对比方法**为 vanilla GRPO 及 SELF 方法。**主要结果**：在 Countdown 困难设置下，Pass@1 从 19.1% 提升至 61.1% (3.2×)，推理缺陷比例从 93.5% 降至 45.5%；在 AIME 上，Pass@64 从 36.7% 提升至 43.3%；在 SciQA 上，1.7B 模型准确率从 68.5% 提至 72.6% (+4.1pp)，且逻辑捷径比例下降。**控制实验**验证了提前自信与推理缺陷的强相关性，在四种基准 (CSQA/GPQA/LSAT/MuSR) 上提前自信样本平均缺陷数分别是渐进自信样本的 2.8×/1.1×/1.3×/1.1× 倍；在安全基准上，提示认可率提升 (AIME: +7.0pp)。**消融实验**表明该相关性对阈值、正确样本、监控模型和量化方法均稳健。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在以下几点：首先，其提出的“推理效用”和“推理可得性”分析主要基于Countdown任务，结论的泛化性有待验证，尤其在真实复杂的多步推理任务中，二者的量化与相互作用可能更复杂。其次，该方法依赖预训练模型对置信度的内在表征，对于缺乏自省能力或置信度校准不佳的小模型可能效果有限。未来可探索的方向包括：(1) 将渐进置信塑造与更细粒度的过程奖励模型结合，利用置信度信号辅助生成更高质量的步骤级监督；(2) 研究该目标在多任务、多领域上的迁移性，特别是在幻觉率高或需要外部知识检索的生成任务中；(3) 从认知科学角度出发，探索通过提示工程或架构修改（如追加“反思”模块）来进一步抑制过早自信，并将其与强化学习目标形成互补；(4) 分析模型在不同概率阈值下的置信度分布，设计更精细的适应性惩罚函数，以针对不同难度任务动态调节过早自信的抑制强度。

### Q6: 总结一下论文的主要内容

该论文提出并研究了大型语言模型在长链推理（CoT）中存在的“过早自信”问题，即模型在推理早期就固定了答案，后续token仅用于合理化该答案，导致逻辑缺陷和推理不忠实。核心贡献是：1）首次实证发现“过早自信”与CoT中的逻辑缺陷（如错误结论、忽略证据）强相关，且这一现象在正确答案样本中依然存在；2）提出“渐进自信塑造”（Progressive Confidence Shaping），一种基于强化学习（GRPO）的无标注训练目标，通过探测模型在CoT不同截断点的置信度轨迹，并用固定递减评分向量计算优势值，奖励逐步增长的置信度，惩罚早期承诺。在算术、数学、科学推理等任务上（1.5B-8B参数），该方法显著提升了准确率（Countdown上+42.0pp）并降低了推理缺陷（下降48pp），同时增强了推理忠实性。研究还揭示了“推理效用”与“推理可及性”的动态竞争：在困难任务和大模型上，模型难以自然产生渐进自信的CoT，导致过早自信更严重，而该方法恰好在此类场景中获益最大。
