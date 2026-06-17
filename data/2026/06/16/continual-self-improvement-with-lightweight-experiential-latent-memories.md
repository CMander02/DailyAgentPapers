---
title: "Continual Self-Improvement with Lightweight Experiential Latent Memories"
authors:
  - "Vaggelis Dorovatas"
  - "Nancy Kalaj"
  - "Rahaf Aljundi"
date: "2026-06-16"
arxiv_id: "2606.17803"
arxiv_url: "https://arxiv.org/abs/2606.17803"
pdf_url: "https://arxiv.org/pdf/2606.17803v1"
categories:
  - "cs.LG"
tags:
  - "LLM Agent"
  - "continual learning"
  - "latent memory"
  - "reasoning"
  - "self-improvement"
  - "in-context learning"
  - "reinforcement learning"
relevance_score: 8.5
---

# Continual Self-Improvement with Lightweight Experiential Latent Memories

## 原始摘要

Large language models achieve strong reasoning performance by scaling inference-time compute, yet remain fundamentally stateless, discarding the rich, self-produced reasoning traces generated during this process. We investigate whether models can instead learn online from this experience, converting transient computation (reasoning traces) into persistent reusable knowledge, and without external supervision or access to future data. We show that In-Context Learning (ICL) over raw reasoning traces fails to generalize, reflecting a fundamental limitation of token-level reuse: individual traces lack the abstraction needed for transfer, even after refinement (e.g. self-reflection). In contrast, drawing inspiration from recent works on unsupervised reinforcement learning, we find that lightweight per-instance training with self-generated test-time signals (majority voting) as rewards yields substantial gains, often surpassing full-dataset offline training, motivating a shift from raw traces to learned latent representations. Building on this insight, we propose an online method that distills inference-time compute spent on encountered problems into compact modular latent memories capturing the underlying reasoning structure. These memories are stored and retrieved for future inputs, enabling continual improvement while avoiding catastrophic forgetting through modular design. Importantly, our method is highly efficient, parametrized as extremely lightweight soft prompt memories (~0.001% of model parameters) and trained with only a few gradient steps, yet achieving performance competitive with full parametric updates and offline training. Across challenging mathematical reasoning benchmarks, our approach significantly outperforms zero-shot and raw data ICL baselines, while transferring effectively across datasets.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在部署后的“统计性”问题。现有LLM尽管在推理时通过扩展计算量（如思维链）展现出强大能力，但它们是“无状态的”，每次处理新问题时都会丢弃自己生成的丰富推理轨迹，无法将这些瞬时的计算转化为可积累、可重用的知识。当前的两类主流方法存在明显不足：一是基于上下文学习的训练无关方法，它通过存储和检索推理文本（如思维链）来指导新问题，但这种方法受限于文本瓶颈，丢失了隐藏状态中的结构化推理信息，且无法从成功或失败中提取有意义的学习信号，导致泛化能力差；二是基于强化学习的离线训练方法，它虽能利用自生成奖励信号，但需要预先获取完整数据集，且随着经验积累可能因自我监督信号相互干扰而导致性能下降，同时全模型更新也带来巨大的计算开销和遗忘风险。因此，本文要解决的核心问题是：如何设计一种在线、流式、无需外部监督的方法，让LLM在逐个解决新问题的过程中，能持续地将其推理经验和探索过程内化为紧凑、模块化的潜在记忆，并实现高效检索与复用，从而实现持续自我改进，同时避免灾难性遗忘和性能退化。

### Q2: 有哪些相关研究？

相关研究主要分为三类。首先是**强化学习提升LLM推理能力**，如RLVR利用规则奖励或答案匹配提升推理，但依赖真实标签。TTRL通过多数投票生成奖励，但其测试时数据离线收集并用于全模型GRPO训练，与本文不同；本文展示了在测试样本上高效的在线训练能达到甚至超越离线变体的性能，这是关键区别。其次是**利用过往经验的记忆方法**，这类工作将测试时经验存储为文本（如LAG重用KV激活但无学习），或使用离线训练的潜在记忆（如MemGen、FlashMem），但它们通常依赖外部监督、大模型或保持静态。本文创新地通过学习直接来自个体经验的轻量级潜在记忆，并利用内部反馈实现持续的在线适应与泛化。最后是**在线持续学习**，经典方法在监督流中更新单一模型，面临灾难性遗忘；自监督方法则内部生成信号。区别于这些仍更新单一模型的方法，本文设计了模块化、独立参数化的体验性潜在记忆（约0.001%模型参数），在测试时检索，通过模块化设计缓解干扰并实现紧凑、可扩展的知识积累。

### Q3: 论文如何解决这个问题？

论文提出了一种名为“经验性潜在记忆”（Experiential Latent Memory）的在线持续自我改进方法。其核心是解决大语言模型在推理时无法积累可复用经验的问题。整体框架包括三个主要模块：内存创建、内存检索和响应路由。

**核心方法**：采用“测试时强化学习”（TTRL）框架。对于每个测试样本，模型先生成多个回答，通过多数投票产生一个共识答案作为内部奖励信号，再使用“组相对策略优化”（GRPO）进行轻量级训练。关键是，训练不更新整个模型参数，而是仅更新一个极轻量的模块——软提示（soft prompt）内存。

**架构设计**：
1.  **内存创建**：对于每个遇到的输入，模型先生成一个解决方案。然后将该经验蒸馏为一个“潜在记忆”，即以软提示形式参数化的可训练向量序列（约占总参数的0.001%）。通过少量梯度步骤的GRPO训练，将推理轨迹抽象为潜在空间中的结构化表示，实现经验的高效压缩和隔离存储。
2.  **内存检索**：针对新输入，通过计算输入或内部激活的嵌入向量与已有内存键（key）的余弦相似度来检索最相关的记忆。支持两种检索方式：基于输入的嵌入空间（Input retrieval）和基于模型内部表示空间中各层的KV激活（KV retrieval），后者能利用更丰富的上下文特征。
3.  **响应路由**：为增强可靠性，同时生成零样本回答和内存增强回答。若两者一致则直接输出；若不一致，则通过验证器（Verifier）选择评分更高的回答，从而避免噪声内存导致的性能退化。

**关键技术**：将测试时计算产生的经验蒸馏为离散的、模块化的软提示记忆，而非直接更新模型参数。这种方法避免了灾难性遗忘，并允许通过检索高效复用经验，在数学推理任务上显著优于零样本和原始数据上下文学习（ICL）基线。

### Q4: 论文做了哪些实验？

论文在三个数学推理基准上评估了方法：MATH500（500道竞赛级数学题）、AMC23（2023年AMC竞赛题）、AIME24（2024年AIME竞赛题）。对比方法包括零样本思维链（Zero-shot CoT）、ICL（上下文学习）、Reasoning Bank、LAG以及全数据集离线训练的GRPO和TTRL。实验使用Llama-3.1-8B-Instruct和Qwen2.5-Math-7B两个模型家族。每样本训练采用10个梯度步、8个rollout，软提示记忆仅含20个可训练token（约0.001%模型参数）。离线实验结果显示，软提示记忆在Llama上MATH500达45%、AMC23达32.5%、AIME24达10%，在Qwen上分别达73.4%、65%、20%，均超过或匹配全模型GRPO（如Qwen上GRPO为68%、62.5%、20%）。在线场景中，方法（ELM）显著优于ICL等无训练基线，例如在Llama上MATH500达51.4%（ICL仅46.3%），AMC23达26%（ICL 21.7%），AIME24达6.7%（ICL 3.3%），甚至接近或超越离线全训练方法。消融实验表明软提示优于LoRA，且记忆可跨数据集迁移（如AIME24记忆提升AMC23性能）。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要体现在以下几点。首先，如何自动识别能产生高质量记忆的样本仍是一个未解之谜，当前缺乏与记忆效用强相关的简单统计指标，未来可探索基于训练动态或不确定性估计的主动采样策略。其次，部分检索到的记忆可能因自监督信号（如多数投票）不准确而有害，目前依赖外部验证器来规避风险，后续研究可设计更高效的决策机制，如自适应置信度阈值或元学习选择器。此外，对记忆的编码内容及替代奖励函数（如过程奖励模型）的分析尚浅，这限制了记忆的泛化能力和可解释性。最重要的是，记忆的组合性、更新、合并、淘汰以及最终如何蒸馏回主模型等核心问题尚未解决。未来可借鉴持续学习中的弹性权重巩固或神经模块化网络，实现记忆的动态演化与压缩。通过这些改进，有望推动从静态记忆到真正终身学习范式的跨越。

### Q6: 总结一下论文的主要内容

这篇论文探讨了如何让大语言模型在部署后持续自我提升。核心问题是：模型能否将推理过程中产生的丰富计算痕迹（推理轨迹）转化为可复用的知识，无需外部监督。作者发现，直接使用上下文学习（ICL）从原始推理轨迹中学习效果不佳，因为缺乏抽象性。受无监督强化学习启发，论文提出了一种在线方法，通过轻量级的“经验潜在记忆”来蒸馏测试时的计算。具体而言，对于每个遇到的新问题，模型会利用自生成信号（如多数投票）作为奖励进行少量梯度更新，训练一个极其轻量的软提示（约为模型参数的0.001%）作为记忆。这些记忆模块化存储，在遇到新输入时被检索和组合，从而避免灾难性遗忘。实验表明，该方法在数学推理基准上显著优于零样本和ICL基线，能达到与全参数微调媲美的性能，并展示了良好的跨数据集迁移能力。其核心贡献在于提供了一种高效、模块化、可扩展的持续自我改进路径。
