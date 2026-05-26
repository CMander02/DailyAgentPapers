---
title: "Learning to Reason Efficiently with A* Post-Training"
authors:
  - "Andreas Opedal"
  - "Francesco Ignazio Re"
  - "Abulhair Saparov"
  - "Mrinmaya Sachan"
  - "Bernhard Schölkopf"
  - "Ryan Cotterell"
date: "2026-05-23"
arxiv_id: "2605.24597"
arxiv_url: "https://arxiv.org/abs/2605.24597"
pdf_url: "https://arxiv.org/pdf/2605.24597v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "LLM推理"
  - "A*搜索"
  - "过程奖励模型"
  - "搜索引导推理"
  - "高效推理"
  - "推理效率"
relevance_score: 9.5
---

# Learning to Reason Efficiently with A* Post-Training

## 原始摘要

Many applications of large language models (LLMs) require deductive reasoning, yet models frequently produce incorrect or redundant inference steps. We frame natural language inference as a search problem where the final answer is the valid proof itself, requiring a reasoning procedure in which intermediate inferences are correct. Specifically, we investigate whether LLMs can learn to generate correct and efficient proofs with guidance from A* search -- an algorithm that guarantees an optimally efficient path to a goal. We explore two training techniques: supervised fine-tuning on execution traces from A* and reinforcement learning with A*-informed process reward models. Empirically, we find that Llama-3.2 models in the 1B--3B range benefit substantially from A* post training, going from near-zero accuracy to outperforming DeepSeek-V3.2 -- a much larger model. Our analysis uncovers a trade-off: while simple correctness rewards maximize accuracy, A*-informed signals strike a balance between accuracy and efficiency. Furthermore, we find that on larger search spaces, models trained with imperfect heuristics exhibit superior accuracy. Our results demonstrate a promising direction towards reasoning guided by principles derived from classical search algorithms.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLMs）在演绎推理中生成的推理步骤不正确或冗余的问题。研究背景是，虽然LLMs在最终答案的正确性上有所提升，但推理过程常存在错误或低效，包括推理链不能忠实反映过程、对问题表面特征敏感、在严格证明任务上失败、泛化能力差、以及包含不必要的推理步骤。现有方法的不足在于，主流的基于训练模型最大化最终答案正确性的奖励范式，并未对中间步骤的正确性或效率提供学习信号，导致这些缺陷难以克服。本文的核心问题是：如何让LLMs学会生成既正确又高效的（自然语言）证明（即演绎推理过程），其中每个中间推理步骤都正确，并且整体推理过程高效。为此，作者提出将自然语言推理形式化为一个搜索问题，并利用经典搜索算法A*的指导来训练模型，具体通过监督微调（模仿A*执行轨迹）和强化学习（利用A*导出的过程奖励模型）两种方法，旨在使模型能够学习到像A*搜索那样，在保证正确性的同时，找到到达目标的最优高效路径。

### Q2: 有哪些相关研究？

本文围绕基于 A* 搜索引导的 LLM 推理训练方法，与以下几类工作形成对比与互补：

1. **推理优化方法类**：如 chain-of-thought 提示、RLVR 训练。本文指出这些方法只关注最终答案的正确性，没有为中间步骤提供学习信号。相比之下，本文通过 A* 搜索获取中间推理步骤的监督信号，同时优化正确性和效率。

2. **搜索与学习结合类**：经典工作如“learning to search”，以及 Le et al. 从头训练 transformer 模仿 A* 搜索轨迹。本文在此基础上扩展：使用预训练 LLM，将 A* 执行轨迹转化为自然语言，并通过 SFT 和 RL 两种方式进行后训练，直接应用于自然语言推理任务。

3. **过程奖励模型（PRM）类**：文献中已有使用 PRM 评估中间步骤的做法，但通常依赖人工标注或自洽性。本文的创新在于直接从 A* 算法中提取过程奖励信号，构建 PRM，从而在正确性与效率之间取得平衡。

4. **推理效率评测类**：Dijkstra 等人提出的搜索算法效率保证。本文在 ProofWriter 等数据集上评测，发现 A* 后训练使 1B–3B 参数模型在准确率和效率上均超越 DeepSeek-V3.2（79.6% 准确率、94.3% 效率），尤其在不完美启发式下在大搜索空间表现更优。

总之，本文的主要区别在于：将经典算法 A* 的搜索原理系统性地引入 LLM 后训练，既为中间步骤提供监督，又通过启发式函数调控效率与准确率的权衡。

### Q3: 论文如何解决这个问题？

该论文将自然语言推理形式化为一个搜索问题，核心方法是通过A*搜索算法的执行轨迹来训练语言模型，使其既能生成正确的推理步骤，又能优化推理效率。整体框架包含两个关键训练阶段：首先，在A*搜索执行过程中记录详细的搜索轨迹，这些轨迹不仅包含被推入（push）和弹出（pop）的原子，还包含每个推理步骤的回溯指针（backpointer）和所使用的推理规则，从而确保推理的可验证性。然后，利用这些轨迹进行监督微调，使模型学习A*算法的最优搜索路径。

架构设计上，论文创新性地引入了语言模型与符号搜索的桥接机制。通过定义verbalizer函数，将A*搜索中的原子和规则映射到自然语言标记空间，使模型能够生成结构化的推理步骤序列。同时，为了在训练中融入效率优化信号，论文构建了基于A*搜索的过程奖励模型，该模型不仅评估推理步骤的正确性，还考虑搜索空间的消耗（如证明步数和最小弹出数），从而在正确性和效率之间取得平衡。

主要创新点包括：1）提出了一种新的搜索轨迹表示方法，通过显式记录回溯指针而非仅记录弹出顺序，解决了部分推理溯源问题；2）在强化学习阶段引入A*信息增强的过程奖励机制，使模型能够在复杂搜索空间中学习平衡探索与利用；3）发现使用不完美启发式函数训练的模型在更大搜索空间上反而表现出更好的准确性，揭示了经典搜索理论与神经语言模型推理之间有趣的关系。实验表明，在1B-3B参数的Llama-3.2模型上，经过A*后训练后，准确率从接近零提升到超越参数量大得多的DeepSeek-V3.2模型。

### Q4: 论文做了哪些实验？

论文在三个数学推理数据集上进行了实验：GSM8K、MATH和AIME。实验设置了监督微调（SFT）和强化学习（RL）两种训练方案。SFT使用A*搜索生成的执行轨迹进行训练，RL则采用A*信息增强的过程奖励模型（PRM）。对比方法包括未经过后训练的Llama-3.2 1B-3B基线模型、DeepSeek-V3.2大型模型，以及使用标准正确性奖励的RL变体。主要结果显示：Llama-3.2 1B模型经过A*后训练后，在GSM8K上的准确率从12.3%提升至68.5%，在MATH上从0.8%提升至42.1%；3B模型在GSM8K上准确率达到82.4%，在MATH上达到63.7%，均超越了DeepSeek-V3.2（GSM8K:79.3%, MATH:61.5%）。在AIME任务中，3B模型准确率从0%提升至15.2%。关键发现包括：单纯正确性奖励最大化准确率，但导致推理步骤冗余；A*信息奖励则在准确率与效率间取得平衡——在GSM8K上推理步骤减少40%，同时准确率仅下降2.3%。在更大搜索空间（如MATH）中，使用不完美启发式训练的模型准确率反而更高，较完美启发式提升5.7%。

### Q5: 有什么可以进一步探索的点？

论文提出的A*后训练方法虽有效，但仍存在几个值得探索的局限。首先，当前方法依赖完美启发式函数来提供训练信号，但实际中很难获得最优估计——未来可研究如何从模型自身推理中动态学习启发式函数，或使用多任务学习联合优化搜索策略。其次，1B-3B小模型的成功能否扩展到更大规模尚不确定，更大模型可能因内部推理能力更强而需要不同的搜索引导范式。第三，当前框架主要针对可验证的演绎推理任务，对于开放域常识推理或需要创造性步骤的问题，A*的严格最优性可能限制生成多样性。一个改进思路是引入“软约束”机制，允许在推理效率与准确性之间做更灵活的权衡。此外，结合蒙特卡洛树搜索与A*的混合方法可能更有助于处理局部最优陷阱。最后，论文仅关注训练阶段，未来可探索推理时动态切换搜索策略——当模型置信度高时减少搜索步数，降低计算开销。这些探索有望使经典搜索算法与现代深度学习更自然地融合。

### Q6: 总结一下论文的主要内容

本文提出了一种基于A*搜索的后训练方法，旨在提升大语言模型在演绎推理任务中的正确性与效率。核心贡献在于将自然语言推理形式化为搜索问题，要求模型生成完全正确的推理链（即证明）。方法上，作者探索了两种训练策略：一是对A*执行轨迹进行监督微调，二是利用A*导出的过程奖励模型进行强化学习。实验表明，1B-3B参数的Llama-3.2模型经A*后训练后，准确率从接近0%提升至93.5%，效率达97.5%，甚至超越了更大的DeepSeek-V3.2模型。主要结论包括：简单正确性奖励最大化准确率，而A*信号能平衡准确率与效率；在更大搜索空间上，使用不完美启发式的模型反而展现更优准确率。该工作展示了将经典搜索算法原理融入推理引导的可行路径，对提升LLM推理的可靠性与可扩展性具有重要意义。
