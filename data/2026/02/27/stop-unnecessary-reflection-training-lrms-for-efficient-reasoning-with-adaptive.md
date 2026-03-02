---
title: "Stop Unnecessary Reflection: Training LRMs for Efficient Reasoning with Adaptive Reflection and Length Coordinated Penalty"
authors:
  - "Zewei Yu"
  - "Lirong Gao"
  - "Yuke Zhu"
  - "Bo Zheng"
  - "Junbo Zhao"
  - "Sheng Guo"
  - "Haobo Wang"
date: "2026-02-12"
arxiv_id: "2602.12113"
arxiv_url: "https://arxiv.org/abs/2602.12113"
pdf_url: "https://arxiv.org/pdf/2602.12113v2"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Reasoning"
  - "Efficiency"
  - "Reinforcement Learning"
  - "Chain-of-Thought"
  - "Training Framework"
relevance_score: 7.5
---

# Stop Unnecessary Reflection: Training LRMs for Efficient Reasoning with Adaptive Reflection and Length Coordinated Penalty

## 原始摘要

Large Reasoning Models (LRMs) have demonstrated remarkable performance on complex reasoning tasks by employing test-time scaling. However, they often generate over-long chains-of-thought that, driven by substantial reflections such as repetitive self-questioning and circular reasoning, lead to high token consumption, substantial computational overhead, and increased latency without improving accuracy, particularly in smaller models. Our observation reveals that increasing problem complexity induces more excessive and unnecessary reflection, which in turn reduces accuracy and increases token overhead. To address this challenge, we propose Adaptive Reflection and Length Coordinated Penalty (ARLCP), a novel reinforcement learning framework designed to dynamically balance reasoning efficiency and solution accuracy. ARLCP introduces two key innovations: (1) a reflection penalty that adaptively curtails unnecessary reflective steps while preserving essential reasoning, and (2) a length penalty calibrated to the estimated complexity of the problem. By coordinating these penalties, ARLCP encourages the model to generate more concise and effective reasoning paths. We evaluate our method on five mathematical reasoning benchmarks using DeepSeek-R1-Distill-Qwen-1.5B and DeepSeek-R1-Distill-Qwen-7B models. Experimental results show that ARLCP achieves a superior efficiency-accuracy trade-off compared to existing approaches. For the 1.5B model, it reduces the average response length by 53.1% while simultaneously improving accuracy by 5.8%. For the 7B model, it achieves a 35.0% reduction in length with a 2.7% accuracy gain. The code is released at https://github.com/ZeweiYu1/ARLCP .

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型推理模型在复杂任务中因过度反思导致的推理效率低下问题。研究背景是，以OpenAI o1、DeepSeek-R1等为代表的大型推理模型通过长链思维和自我反思机制，在复杂推理任务上表现出色，但它们在推理过程中常常生成过长的思维链，包含大量重复的自我提问和循环反思，这不仅消耗大量计算资源、增加延迟，而且对于较小的模型而言，这种过度反思并不能提升准确性，反而可能降低性能。现有方法主要分为两类：一是在推理阶段进行训练无关的优化，如提前退出或模型切换，但这些方法仅优化生成过程，对冗余模型或复杂任务的效率提升有限；二是通过监督微调或强化学习引入长度惩罚来训练模型，但这类方法往往简单抑制反思或丢弃整个思维过程，损害了推理质量，导致准确率下降。因此，现有方法难以在保持准确性的同时有效提升推理效率。本文要解决的核心问题是：如何动态平衡推理效率与解答准确性，减少不必要的反思步骤，同时保留关键的推理过程。为此，论文提出了自适应反思与长度协调惩罚框架，通过强化学习动态调整反思惩罚和基于问题复杂度的长度惩罚，以鼓励模型生成更简洁、高效的推理路径，从而在降低计算开销的同时维持或提升模型性能。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕大型推理模型及其高效推理方法展开，可分为两大类。

在**大型推理模型（LRMs）**方面，相关工作包括基于详细奖励和搜索的方法，例如模型间的相互学习、示例引导搜索，以及集成蒙特卡洛树搜索的自对弈以进行自我纠正推理。DeepSeek-R1的发布进一步推广了仅使用简单基于规则奖励即可实现多步推理和自我反思的“R1风格”模型。本文的研究背景与这些工作一致，但明确指出这些模型普遍存在因过度反思（如重复自问和循环推理）导致推理链过长、效率低下的问题。

在**LRMs的高效推理**方面，现有方法主要致力于减少响应令牌数，可分为几类：1）**无需训练的方法**，如使用令牌预算进行提示、模型切换和早期退出机制；2）**基于监督微调的方法**，使用压缩的思维链数据或通过采样与后处理得到的长度筛选数据；3）**基于强化学习的方法**，通常结合基于长度的奖励或其他奖励。本文指出，这些现有方法虽各有不同，但均未能根据问题内在复杂性动态调整响应长度，也未能有效抑制模型的过度反思倾向。本文提出的ARLCP框架通过引入自适应的反思惩罚和与问题复杂度协调的长度惩罚，动态平衡推理效率与准确性，从而弥补了这一研究空白。

### Q3: 论文如何解决这个问题？

论文提出的ARLCP（自适应反思与长度协调惩罚）框架，通过强化学习方法，动态平衡推理效率与答案准确性，以解决大型推理模型（LRMs）因过度反思（如重复自问和循环推理）导致生成长链思维、增加计算开销和延迟的问题。

**核心方法与架构设计**：
整体框架基于策略梯度强化学习。模型接收输入提示后，生成多个候选推理轨迹（rollouts）。每个轨迹包含思考阶段（含反思）和最终解答阶段。框架的核心是计算一个复合奖励函数，该函数同时考虑答案正确性、反思惩罚和长度惩罚。

**主要模块与关键技术**：
1.  **问题复杂度估计模块**：首先，通过分析模型生成的多个候选回答中的反思令牌计数（RTC，基于关键词匹配），将每个问题的复杂度动态划分为三个等级（简单、中等、困难），并分配不同的权重（λ1, λ2, λ3）。这构成了自适应惩罚的基础。
2.  **自适应反思惩罚**：根据估计的问题复杂度（λ）确定反思惩罚系数α1。对于每个候选回答，其反思惩罚值f(RTC)通过将其RTC与同一批数据中所有**正确**回答的RTC均值和标准差进行标准化（使用Sigmoid函数）来计算。复杂度越高，允许的反思越多（惩罚系数可能更宽松），反之则施加更强惩罚以抑制不必要的反思。
3.  **协调长度惩罚**：为了全面抑制冗余内容（包括非反思性的冗长），引入了基于总令牌数（LEN）的长度惩罚f(LEN)，其计算方式与反思惩罚类似，也是基于正确回答的长度进行标准化。其惩罚系数α2由总惩罚系数α与α1的差值决定（α2 = α - α1），从而实现了两种惩罚的协调与权重分配。
4.  **复合奖励函数与训练**：最终的奖励函数为：r = 正确性指标 × (1 - α1 * f(RTC) - α2 * f(LEN))。正确性指标是二元的（答案对/错）。模型通过策略梯度更新，最大化此奖励，从而学习生成既正确又简洁（反思和总长度均受控）的推理路径。

**创新点**：
1.  **动态自适应惩罚**：不同于静态惩罚，ARLCP根据每个问题预估的复杂度动态调整反思惩罚的强度，实现了精细化的控制。
2.  **反思与长度惩罚的协调**：创新性地将总惩罚预算（α）在反思惩罚（α1）和长度惩罚（α2）之间进行分配，确保即使在反思较少的情况下，整体响应长度也能受到约束，解决了单一反思惩罚的局限性。
3.  **基于正确回答分布的标准化**：反思和长度惩罚均以当前批次中正确回答的统计量（均值和标准差）为基准进行标准化，使得惩罚尺度能够适应模型当前的能力和数据分布，更具鲁棒性。

通过上述方法，ARLCP引导模型在简单问题上减少不必要的反思，在复杂问题上保留必要的推理，同时控制整体响应长度，最终在多个数学推理基准上实现了准确率提升与令牌消耗大幅降低的双重优化。

### Q4: 论文做了哪些实验？

论文在DeepSeek-R1-Distill-Qwen-1.5B和7B两个模型上进行了实验。实验设置基于VeRL框架，采用REINFORCE Leave One Out (RLOO)策略优化方法，在8张NVIDIA A100 GPU上运行，关键参数包括学习率2e-6、批次大小128、上下文长度16K。

使用的数据集为DeepScaleR（40K数学问题对）进行训练，并在五个数学推理基准上评估：GSM8K（1319题）、MATH500（500题）、AMC2023（40题）、AIME 2024和AIME 2025（各30题）。评估指标包括准确率（pass@1）和响应长度。

对比方法包括：Vanilla（原始模型）、NoThinking（直接生成答案的下界）、SFT_Shortest（基于最短正确响应的监督微调）、DPO_Shortest（基于最短与最长响应对的DPO微调）、O1-Pruner（基于预采样的离线RL微调）、TLMRE（带长度惩罚的在线RL）、AdaptThink（自适应选择思考模式的在线RL）以及LASER（基于统一RL视图的自适应长度奖励塑造方法）。

主要结果显示，ARLCP在效率和准确率之间取得了优越的权衡。对于1.5B模型，平均响应长度降低了53.1%（ΔLength = -53.05%），同时准确率提升了5.8%（ΔAcc = 5.81）；对于7B模型，长度减少35.0%（ΔLength = -34.96%），准确率提升2.7%（ΔAcc = 2.69）。在复杂任务（如AIME 2024）上，ARLCP表现尤为突出，1.5B模型在AIME 2024准确率达到34.17%，显著优于基线。消融实验证实了自适应反射惩罚和长度惩罚的协同作用，移除任一组件均会导致性能下降。

### Q5: 有什么可以进一步探索的点？

该论文提出的ARLCP框架在平衡推理效率与准确性方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其反射惩罚和长度惩罚的协调机制依赖于对问题复杂度的估计，目前这种估计可能较为粗略，未来可以探索更精细、更自适应的复杂度量化方法，例如利用模型自身的中间表示或注意力模式来动态评估推理难度。其次，当前方法主要针对数学推理任务进行验证，其泛化能力有待在其他复杂推理领域（如代码生成、科学问答）进行检验，不同任务可能对“必要反思”的定义不同，需要任务自适应的惩罚策略。此外，框架依赖于强化学习训练，计算成本较高，未来可研究更高效的轻量化训练方案，例如通过蒸馏或课程学习来迁移控制能力。从更广阔的视角看，可以探索将这种“反思控制”机制与推理模型的架构设计相结合，例如设计具有明确反思门控模块的模型，或开发能够在线学习何时停止反思的元控制策略，从而从根本上提升推理效率。

### Q6: 总结一下论文的主要内容

该论文针对大型推理模型在复杂任务中因过度反思（如重复自问和循环推理）导致推理链冗长、计算开销大且准确率未提升的问题，提出了一种自适应反思与长度协调惩罚的强化学习框架。核心贡献是设计了ARLCP方法，包含两个关键创新：一是自适应反思惩罚机制，动态削减不必要的反思步骤而保留关键推理；二是根据问题复杂度校准的长度惩罚项。两者协同促使模型生成更简洁高效的推理路径。实验在五个数学推理基准上使用1.5B和7B模型进行验证，结果表明ARLCP在效率与准确率间取得了更优平衡：1.5B模型平均响应长度降低53.1%且准确率提升5.8%，7B模型长度减少35.0%且准确率提高2.7%。该方法显著提升了小规模模型的推理效率与实用性。
