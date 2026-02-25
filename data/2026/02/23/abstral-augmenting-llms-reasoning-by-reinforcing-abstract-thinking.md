---
title: "AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking"
authors:
  - "Silin Gao"
  - "Antoine Bosselut"
  - "Samy Bengio"
  - "Emmanuel Abbe"
date: "2025-06-09"
arxiv_id: "2506.07751"
arxiv_url: "https://arxiv.org/abs/2506.07751"
pdf_url: "https://arxiv.org/pdf/2506.07751v4"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.SC"
tags:
  - "Agent 推理"
  - "强化学习"
  - "抽象思维"
  - "分布外泛化"
  - "数学推理"
  - "数据合成"
  - "鲁棒性"
relevance_score: 7.5
---

# AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking

## 原始摘要

Recent studies have shown that large language models (LLMs), especially smaller ones, often lack robustness in grade school math (GSM) reasoning. In particular, they tend to experience performance drops when faced with distribution shifts, such as changes to numerical or nominal variables, or insertions of distracting clauses. A possible strategy to address this involves generating synthetic data to further "instantiate" reasoning problems on potential variations. In this work, we instead focus on the strategy of "abstracting" reasoning problems. This not only helps counteract distribution shifts but also facilitates the connection to symbolic tools for deriving solutions. Focusing on GSM, we find that this abstraction process is better acquired through reinforcement learning (RL) than just supervised fine-tuning, which often fails to produce faithful abstractions. Our method, AbstRaL -- which promotes abstract reasoning in LLMs using RL on granular abstraction data -- significantly mitigates performance degradation on recent GSM perturbation benchmarks. Besides, improving GSM robustness via AbstRaL is shown to also implicitly benefit LLMs' capabilities on OOD mathematical and general reasoning tasks, indicating that abstract thinking broadly enables better generalizability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLMs），尤其是较小规模模型，在数学推理任务中面对分布变化时表现脆弱、缺乏鲁棒性的问题。研究背景是，尽管LLMs在一般或特定领域（如数学）已展现出强大的推理能力，但在面对简单的分布偏移时，例如小学数学（GSM）问题中的数值或名义变量被替换，或者被插入无关的干扰性条件，模型的性能会出现显著下降。现有方法的一个可能策略是生成大量合成数据来“实例化”问题的各种变体，以增强模型对变化的适应能力，但这通常计算成本高昂。

本文的核心思路与上述“实例化”策略相反，它聚焦于“抽象化”策略。作者认为，直接教导模型学习推理问题背后的抽象表征，能够使其推理过程对具体的上下文分布变化保持“不变”，从而提升鲁棒性。这不仅有助于对抗分布偏移，还能更好地与符号计算工具连接以稳定求解。因此，本文要解决的核心问题是：如何有效地让LLMs学会生成对GSM问题的忠实、高质量的抽象表征，并利用这种抽象思维来显著提升模型在面对扰动和分布变化时的推理鲁棒性与泛化能力。为此，论文提出了AbstRaL框架，通过基于细粒度抽象数据的强化学习来促进模型的抽象推理能力，以克服仅用监督微调往往无法产生忠实抽象的问题。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：推理鲁棒性、抽象思维与规划、以及强化学习在LLMs中的应用。

在推理鲁棒性方面，先前研究通过数据增强和合成技术来应对分布偏移，但这通常增加了计算成本。本文则另辟蹊径，通过强化抽象思维来提升鲁棒性，而非依赖更多的具体实例化数据。

在抽象思维与规划方面，已有工作提出了多种促进抽象推理的格式，如基于自然语言的AoT、CoA，以及基于编程/形式语言的PoT、PAL和SyReLM。同时，规划方法如思维链（CoT）和问题分解也被广泛采用。本文的贡献在于提出了一种基于自然语言的、更好的抽象思维学习方案，并将其与规划能力相结合。

在强化学习方面，PPO和DPO等方法已被用于提升LLM的推理能力。本文采用了GRPO方法，利用无模型奖励和组相对优势，进一步简化了训练流程，避免了价值模型的训练。这与依赖预训练奖励模型或复杂优势估计的传统RL方法形成了区别。

### Q3: 论文如何解决这个问题？

论文通过一个名为AbstRaL的强化抽象学习框架来解决LLMs在小学数学推理中面对分布变化时鲁棒性不足的问题。该框架的核心思想是将具体问题“抽象化”，从而增强模型的抽象思维能力，以更好地应对数值、名称变化或干扰性条款插入等扰动。

整体框架包含四个步骤：首先，**条件识别**模块解析输入问题，识别用于回答的条件，并用抽象符号（如in0、in1）表示，构建出抽象问题XA。其次，**抽象推理**模块利用专门构建的细粒度抽象推理数据（AbstRaL数据）训练LLM，使其根据XA生成包含抽象符号的推理链YA。该数据格式将抽象推理与已有的苏格拉底式问题分解和思维链策略结合，使模型能逐步构建抽象。接着，**抽象检索**模块从YA中提取出去语境化的抽象表示A。最后，**符号推导**模块利用A和原始条件C，通过符号求解器（如SymPy）或神经符号推理器得出最终答案。

关键技术在于**数据构造**和**强化学习**。数据方面，论文利用强大的Oracle LLM（如Llama-3.3-70B）将现有的苏格拉底式思维链数据重写为格式一致的(XA, C, YA, A)四元组，并经过答案验证以确保正确性。训练方面，创新点在于发现仅靠监督微调（SFT）会使模型过度关注训练样本的具体语境，导致在新测试语境下生成不忠实的抽象。因此，论文在SFT基础上引入了**基于抽象奖励的强化学习**。奖励函数包括两部分：一是答案正确性奖励，检查模型生成的抽象Ã是否能结合条件C推导出正确答案；二是符号距离奖励，通过计算模型抽象Ã与标准抽象A之间的编辑距离，提供细粒度的对齐信号。这些奖励与GRPO算法结合，有效提升了模型生成忠实抽象的能力。

该方法的主要创新在于：1）提出了一个分解的、细粒度的抽象推理学习流程（X→XA→YA→A），降低了学习难度；2）设计了融合已有推理策略的抽象数据格式，贴近LLM的预训练分布；3）首创了针对抽象忠实性的强化学习奖励机制，显著提升了模型在面对分布变化时的泛化能力和鲁棒性。

### Q4: 论文做了哪些实验？

论文实验主要围绕评估AbstRaL方法在提升LLMs推理鲁棒性和泛化能力方面的效果。实验设置包括使用不同规模的模型（如Qwen2.5-0.5B-Instruct和Qwen2.5-Math-7B-Instruct）进行测试，并采用强化学习（RL）进行训练，对比方法包括CoT、PoT、CoA、AoT、SyReLM等基线。数据集/基准测试主要基于GSM-Symbolic和GSM-Plus，其中GSM-Symbolic包含原始问题（Origin 100）和数值与名称同时变化的扰动样本（Vary Both），GSM-Plus则涵盖数字扰动（Num. Pert.）、重述（Rephrase）、干扰子句（Distract）和原始问题（Original）等测试集。此外，还进行了零样本泛化实验，使用多个OOD数学数据集（如MATH、SVAMP、AQUA等）和通用推理数据集（如MMLU、BBH、ARC-Challenge等）。

主要结果显示，AbstRaL在GSM-Symbolic的Vary Both上显著提升了模型鲁棒性，例如Qwen2.5-0.5B-Instruct的准确率从基线最高36.8%提升至44.6%，且性能下降（Δ）从基线最低5.54%降至-1.27%（表示性能反而提升）。在GSM-Plus上，AbstRaL有效缓解了数字扰动导致的性能下降（Num. Pert.准确率达46.7%），并在干扰子句（Distract）上表现突出（36.5%），远超基线方法（如CoT的22.7%）。关键数据指标包括准确率（%）和标准差（std），例如在Vary Both上，AbstRaL的标准差最低（0.025），表明结果更稳定。消融实验证实，RL和细粒度抽象推理格式是关键因素，移除它们会导致性能大幅下降（如Qwen2.5-0.5B-Instruct在Distract上从36.5%降至23.6%）。零样本泛化实验中，AbstRaL在多数OOD数据集上优于基线，例如在MATH上达到34.7%（0.5B模型），在BBH上达到26.3%，显示了其泛化优势。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度进一步探索。首先，论文虽验证了抽象思维强化对小学数学（GSM）分布偏移的鲁棒性提升，但未形式化地建立“抽象化”与“泛化能力”之间的理论关联。未来可基于全局度理论等框架，量化抽象步骤如何缩小任务输入与输出的分布差距，并严格证明其对减少模型依赖浅层推理模式的贡献。

其次，当前方法依赖于对现有Socratic CoT数据的改写来构建抽象数据，这限制了其扩展到更复杂或领域特异性任务（如物理推理、逻辑谜题）的潜力。未来可探索如何自动生成或采集多样化的抽象推理数据，或结合课程学习策略，逐步增加抽象复杂度，以增强方法的普适性。

此外，论文发现LLMs即使经过代码训练，仍难以生成脱离上下文的抽象符号推理，这提示预训练数据中抽象格式的推理样本可能不足。未来可研究如何将抽象推理更有效地融入预训练阶段，例如设计针对符号推理的预训练目标，或构建融合自然语言与形式化符号的混合训练数据。

最后，AbstRaL目前主要针对数学推理，其强化学习框架在调整抽象粒度、平衡抽象与实例化方面仍有优化空间。可探索动态抽象机制，让模型根据问题复杂度自适应选择抽象层级，或结合神经符号方法，将抽象输出直接对接至外部符号求解器，以进一步提升推理的准确性和可解释性。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为 AbstRaL 的方法，旨在通过强化学习（RL）增强大型语言模型（LLMs）的抽象思维能力，以提升其在小学数学（GSM）推理任务中的鲁棒性。核心问题是 LLMs（尤其是较小模型）在面对数值、名义变量变化或干扰性从句插入等分布偏移时，性能会显著下降。传统方法侧重于生成具体变体的合成数据来“实例化”问题，而本文则转向“抽象化”策略，使推理步骤对表面形式变化更具不变性，并便于连接符号工具求解。

方法上，AbstRaL 采用基于模型无关奖励的 RL 框架，奖励信号来源于新设计的推理依据（融合了苏格拉底式思维链和增强的粒度），以促进对问题的去语境化和符号工具集成。实验表明，该方法在 GSM 扰动基准测试中有效缓解了由实例化和干扰性偏移引起的性能下降。主要结论是，通过强化抽象思维，不仅显著提升了 GSM 推理的鲁棒性，还在零样本设置下改善了 LLMs 在分布外数学及一般推理任务上的能力，表明抽象思维能广泛促进更好的泛化性，为未来扩展到更广泛领域提供了潜力。
