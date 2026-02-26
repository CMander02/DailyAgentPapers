---
title: "The Art of Efficient Reasoning: Data, Reward, and Optimization"
authors:
  - "Taiqiang Wu"
  - "Zenan Xu"
  - "Bo Zhou"
  - "Ngai Wong"
date: "2026-02-24"
arxiv_id: "2602.20945"
arxiv_url: "https://arxiv.org/abs/2602.20945"
pdf_url: "https://arxiv.org/pdf/2602.20945v2"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "高效推理"
  - "强化学习"
  - "奖励塑形"
  - "思维链"
  - "推理优化"
  - "长度适应"
  - "Agent推理"
relevance_score: 7.5
---

# The Art of Efficient Reasoning: Data, Reward, and Optimization

## 原始摘要

Large Language Models (LLMs) consistently benefit from scaled Chain-of-Thought (CoT) reasoning, but also suffer from heavy computational overhead. To address this issue, efficient reasoning aims to incentivize short yet accurate thinking trajectories, typically through reward shaping with Reinforcement Learning (RL). In this paper, we systematically investigate the mechanics of efficient reasoning for LLMs. For comprehensive evaluation, we advocate for more fine-grained metrics, including length distribution conditioned on correctness and performance across a wide spectrum of token budgets ranging from 2k to 32k. First, we reveal that the training process follows a two-stage paradigm: length adaptation and reasoning refinement. After that, we conduct extensive experiments (about 0.2 million GPU hours) in a unified protocol, deconstructing training prompts and rollouts, reward shaping, and optimization strategies. In particular, a key finding is to train on relatively easier prompts, ensuring the density of positive reward signals and thus avoiding the length collapse. Meanwhile, the learned length bias can be generalized across domains. We distill all findings into valuable insights and practical guidelines, and further validate them across the Qwen3 series, ranging from 0.6B to 30B, demonstrating the robustness and generalization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLMs）在采用链式思维（CoT）推理时面临的计算效率问题。研究背景是，尽管扩展的CoT推理显著提升了LLMs的推理能力，但过长的思维轨迹也带来了沉重的计算开销和高延迟，这阻碍了模型在实际场景中的部署。现有方法主要通过强化学习（RL）进行奖励塑造来激励模型生成“简短而准确”的推理路径，但其关注点几乎完全集中在奖励设计上，而忽视了更广泛的训练方案，包括数据构成和优化策略等关键因素。

因此，本文要解决的核心问题是：如何系统地理解和优化高效推理（efficient reasoning）的训练机制，而不仅仅是设计奖励函数。论文试图全面探究在统一实验协议下，数据、奖励和优化策略如何共同影响模型学习高效推理的过程。具体而言，研究旨在揭示训练动态的本质（如发现其遵循“长度适应”和“推理精炼”的两阶段范式），提出更细粒度的评估指标，并通过大量实验解构训练提示数据、 rollout 数量、奖励分配和优化策略等各个组件的影响，最终提炼出具有鲁棒性和泛化性的实用训练指南。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕高效推理方法展开，可分为以下几类：

**方法类**：主流方法通过监督微调（SFT）或强化学习（RL）训练模型将长思维链（CoT）缩短。同时，也有研究探索架构创新，如在潜在空间中进行推理或设计更高效的解码策略。本文与这些工作的核心区别在于，不提出新架构，而是聚焦于基于RL的效率优化机制，系统剖析其内部运作原理。

**奖励设计类**：奖励塑形的核心哲学是激励模型生成简短而准确的推理轨迹。常见原则包括：在正确答案中奖励更短的响应、惩罚更长的响应，或对错误答案中的长轨迹进行惩罚。也有相反观点主张鼓励生成长错误轨迹以促进探索。本文指出，现有研究常孤立地评估奖励函数，而本文则在统一实验框架下进行比较，并选择了最简单的截断策略进行深入分析。

**评测类**：现有评测往往不够细致。本文倡导采用更细粒度的评估指标，例如基于正确性的长度分布分析，以及在从2k到32k的广泛令牌预算范围内的性能评估，从而对高效推理进行更全面的衡量。

总体而言，本文通过大规模实验，在统一的协议下系统解构了训练提示、推理轨迹、奖励塑形和优化策略，旨在为高效推理提炼出普适的见解和实践指南。

### Q3: 论文如何解决这个问题？

论文通过系统性的实验分析，提出了一套优化大语言模型（LLM）高效推理（Efficient Reasoning）的完整方法框架，核心目标是激励模型生成简短而准确的思维链（CoT），以降低计算开销。其解决方案围绕数据、奖励和优化策略三个维度展开，整体架构基于强化学习（RL），并采用细粒度的评估协议。

**核心方法与架构设计**：
研究以DeepSeek-R1-Distill-Qwen-1.5B为骨干模型，使用Group Relative Policy Optimization（GRPO）进行RL训练。基本流程是：给定输入提示（prompt），策略模型生成N个推理轨迹（rollouts），然后根据奖励信号通过策略梯度更新模型。关键创新在于对训练数据、奖励函数和优化过程的精细控制。

**主要模块/组件与创新点**：
1.  **两阶段训练范式**：研究发现训练动态遵循明确的“长度适应”和“推理精炼”两阶段。第一阶段，模型在长度惩罚驱动下快速缩短输出至目标长度（如从~6k降至~2k）；第二阶段，长度稳定后，模型专注于在预算内提升推理准确性，通过增加每个令牌的信息密度来恢复或提升性能。
2.  **数据策略：使用相对简单的提示**：通过将训练提示（DeepScaleR数据集）按通过率分为简单和困难子集，发现仅在困难提示上训练会导致灾难性失败——由于正奖励信号稀疏，模型过度拟合长度惩罚，导致“推理崩溃”（长度过早塌缩，性能下降）。相反，在简单提示上训练能确保充足的正奖励信号密度，使长度适应平稳，且在困难任务（如AIME'25）上性能与使用全数据集相当甚至更优。这是关键的数据选择创新。
3.  **奖励工程：避免“短即正确”的陷阱**：对负样本（不正确或过长的正确轨迹）的奖励处理至关重要。论文对比了多种奖励塑造策略：
    *   **截断策略基线**：正确且短于目标长度\(L_T\)的轨迹获得奖励1，否则为0。
    *   **关键发现**：简单地惩罚过长的正确轨迹（-L&C策略）或屏蔽所有不正确轨迹（-I策略）会误导模型建立“短=正确”的错误因果，导致模型为满足长度而放弃推理，引发崩溃。
    *   **更优策略**：采用“在目标长度采样”（即设置rollout最大长度\(L_R\)等于目标长度\(L_T\)）。这避免了显式的长度偏见陷阱，因为正样本（短且正确）天然短于负样本（在\(L_T\)内但不正确），隐式鼓励了“短而准”，取得了更好的帕累托前沿（性能与长度权衡）。
4.  **优化策略：探索与稳定的平衡**：
    *   **增加Rollout数量（N）**：在计算资源允许下，增加每个提示的采样轨迹数（如从8增至24）能加速长度适应阶段，并带来更稳健的推理精炼，提升最终性能。
    *   **离策略（Off-policy）优化**：引入一定程度的陈旧性（staleness）可以显著加速训练收敛，但高陈旧性（如S=16）会带来策略熵爆炸和长度反弹等不稳定性风险。论文建议对更大、更脆弱的LLM采用更稳定的在策略（on-policy）训练。

**整体框架与验证**：上述发现被提炼为实用的训练指南，并在Qwen3系列模型（0.6B到30B）上验证了其鲁棒性和泛化性。评估采用细粒度协议，包括基于正确性的长度分布监控，以及在2k到32k宽频谱令牌预算下的性能评估，确保了方法在不同约束下的有效性。

### Q4: 论文做了哪些实验？

论文进行了系统性实验以探究高效推理的训练机制，主要围绕训练提示、奖励分配和优化策略展开。实验设置方面，研究在统一的协议下进行，使用了DeepScaleR数据集，并根据通过率将其划分为简单（DeepScaleR-Easy）和困难（DeepScaleR-Hard）子集。基准测试包括AMC、Olympiad Bench、AIME'25和LiveCodeBench（LCB）等数学与代码生成任务，评估指标涵盖在2k至32k不同token预算下的性能，以及长度分布与正确性的细粒度度量，如Mean@8、Pass@8和平均响应长度。

对比方法上，研究分析了多种奖励策略（如Vanilla、-I、-L&C等）和优化策略（如不同rollout数量N、离策略优化中的不同陈旧度S）。主要结果包括：1）训练提示难度至关重要，仅在困难提示上训练会导致策略熵激增和长度崩溃，性能显著下降；而在简单提示上训练则能稳定学习，获得最佳性能。2）增加rollout数量N（如从8增至24）能加速长度适应阶段并提升推理精炼效果，但计算开销更大。3）奖励策略分析表明，不惩罚过长但正确的rollouts（-L&C策略）能获得更高性能但输出略长；而将rollout限制与目标长度对齐（L_R=L_T）能通过避免“短即正确”的偏见实现更好的权衡。4）离策略优化能加速收敛，但会引入不稳定性（如熵增和长度反弹）。关键数据指标显示，在Qwen3系列模型（0.6B至30B）上的广泛验证中，所提方法显著提升了性能并压缩了长度，例如在Qwen3-0.6B上，Mean@8从13.33提升至24.58，平均长度从14.9k降至8.9k；在Qwen3-4B-Instruct-2507上，Mean@8从45.42提升至46.67，长度从9.1k压缩至4.8k。这些结果证实了方法的鲁棒性和泛化性。

### Q5: 有什么可以进一步探索的点？

基于论文的局限性与未来工作章节，可以进一步探索的点包括：首先，**领域泛化性**是核心局限，当前研究仅在数学和代码领域验证，未来需扩展到创意写作、科学推理等更多样化的任务，并探究跨领域训练是否能提升模型通用推理效率。其次，**自适应推理长度**是关键方向，当前使用固定长度限制可能不够灵活，未来可设计动态机制，根据问题难度和模型状态实时调整推理步长，以平衡效率与准确性。再者，**更大规模模型验证**有待推进，由于算力限制，研究未在千亿参数级别模型上充分测试，未来需探索高效推理方法在超大模型上的缩放规律与潜在优势。此外，**更精细的监督与工具使用**是重要拓展，当前工作侧重于奖励塑形，但未对推理链内部结构进行细化优化；未来可引入人类类似的外部工具（如计算器、笔记）辅助推理，并研究如何让模型学会创建和复用工具，从而进一步提升推理效率与质量。最后，结合个人见解，可探索**多模态高效推理**，将当前文本推理框架扩展至图像、音频等多模态输入，并研究跨模态间的协同压缩与加速机制。

### Q6: 总结一下论文的主要内容

该论文系统研究了大型语言模型（LLM）的高效推理机制，旨在解决思维链（CoT）推理带来的计算开销过大的问题。核心贡献在于揭示了高效推理训练遵循两阶段范式：长度适应和推理精炼，并提出了更细粒度的评估指标（如基于正确性的长度分布和不同token预算下的性能）。方法上，论文通过大量实验（约20万GPU小时）在统一协议下解构了训练提示、rollout策略、奖励塑造和优化策略的影响。关键发现是：在相对简单的提示上进行训练，可以确保正向奖励信号的密度，避免长度崩溃；同时，学习到的长度偏好能够跨领域泛化。主要结论表明，这些见解可提炼为实用指南，并在Qwen3系列模型（0.6B至30B）上验证了其鲁棒性和泛化性，为提升LLM推理效率提供了重要指导。
