---
title: "HISR: Hindsight Information Modulated Segmental Process Rewards For Multi-turn Agentic Reinforcement Learning"
authors:
  - "Zhicong Lu"
  - "Zichuan Lin"
  - "Wei Jia"
  - "Changyuan Tian"
  - "Deheng Ye"
  - "Peiguang Li"
  - "Li Jin"
  - "Nayu Liu"
  - "Guangluan Xu"
  - "Wei Feng"
date: "2026-03-19"
arxiv_id: "2603.18683"
arxiv_url: "https://arxiv.org/abs/2603.18683"
pdf_url: "https://arxiv.org/pdf/2603.18683v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "强化学习"
  - "奖励建模"
  - "信用分配"
  - "多轮决策"
  - "过程奖励"
  - "事后信息"
  - "语言模型对齐"
  - "Agent训练"
relevance_score: 8.0
---

# HISR: Hindsight Information Modulated Segmental Process Rewards For Multi-turn Agentic Reinforcement Learning

## 原始摘要

While large language models excel in diverse domains, their performance on complex longhorizon agentic decision-making tasks remains limited. Most existing methods concentrate on designing effective reward models (RMs) to advance performance via multi-turn reinforcement learning. However, they suffer from delayed propagation in sparse outcome rewards and unreliable credit assignment with potentially overly fine-grained and unfocused turnlevel process rewards. In this paper, we propose (HISR) exploiting Hindsight Information to modulate Segmental process Rewards, which closely aligns rewards with sub-goals and underscores significant segments to enhance the reliability of credit assignment. Specifically, a segment-level process RM is presented to assign rewards for each sub-goal in the task, avoiding excessively granular allocation to turns. To emphasize significant segments in the trajectory, a hindsight model is devised to reflect the preference of performing a certain action after knowing the trajectory outcome. With this characteristic, we design the ratios of sequence likelihoods between hindsight and policy model to measure action importance. The ratios are subsequently employed to aggregate segment importance scores, which in turn modulate segmental process rewards, enhancing credit assignment reliability. Extensive experimental results on three publicly benchmarks demonstrate the validity of our method.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在复杂、长视野的智能体决策任务中，现有强化学习方法存在的信用分配不可靠问题。研究背景是，尽管大语言模型在众多领域表现出色，但在需要完成多个子目标的长期智能体任务（如家庭助手）中，其决策能力仍然有限。当前主流方法主要通过设计有效的奖励模型，并利用多轮强化学习来提升性能，但这些方法存在明显不足。

现有方法的不足主要体现在两方面：一是基于结果的奖励模型仅在轨迹结束时给出单一奖励，由于奖励稀疏且延迟，难以将最终奖励有效回传到早期的关键动作，导致优化困难；二是基于轮次的流程奖励模型试图在轨迹内进行信用分配，但其中一类方法依赖昂贵且有噪声的人工或GPT-4标注的伪流程奖励，另一类则完全忽略过程信息（如动作重要性），导致信用分配缺乏重点。此外，这两种主流范式都在轮次粒度上分配奖励，这对于可能跨越多个轮次的子目标而言过于细粒度，使得奖励与任务子目标对齐不佳，最终导致信用分配不可靠。

因此，本文要解决的核心问题是：如何设计一种更可靠的奖励机制，以提升多轮智能体强化学习中的信用分配效果。具体而言，论文提出的HISR方法试图通过利用后见信息来调制分段过程奖励，使奖励与任务子目标紧密对齐，并突出轨迹中的重要片段，从而增强信用分配的可靠性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大方向，具体如下：

**方法类：LLM智能体训练方法**。相关工作主要分为两大主流：一是基于提示工程与监督微调的方法，通过行为克隆让LLM学习严谨的交互范式数据，例如交织推理与行动、引入反思机制以缓解幻觉和错误传播。这类方法虽有效，但难以实现实时环境交互且依赖高质量轨迹数据。二是基于多轮智能体强化学习的方法，通过优化轨迹累积奖励来提升决策能力，更适用于智能体任务。本文采用后者，并聚焦于改进奖励分配机制。

**方法类：多轮RL中的奖励模型**。早期研究采用基于结果的奖励模型，仅在轨迹结束时给予单一奖励，存在奖励延迟传播和信用分配困难的问题。为缓解此问题，后续工作提出了回合级过程奖励模型，可进一步分为两类：一类依赖有限MCTS或GPT-4标注伪过程奖励，但标注成本高且易引入噪声；另一类仅依赖轨迹结果间接监督信用分配，但完全忽略了过程信息，导致分配不够聚焦。此外，现有方法均在回合粒度分配奖励，可能过于细粒度，不利于跨多回合的子目标对齐。本文提出的分段过程奖励模型则与子目标紧密对齐，避免了过度细粒度的分配，并利用后见信息调制奖励，无需额外标注即可强调关键片段，从而提升了信用分配的可靠性。

### Q3: 论文如何解决这个问题？

论文通过提出HISR方法，解决多轮智能体强化学习中奖励稀疏、信用分配不可靠的问题。其核心是**利用后见信息调制分段过程奖励**，使奖励与子目标紧密对齐，并突出轨迹中的关键片段，从而提升信用分配的可靠性。

整体框架包含三个阶段：首先，通过行为克隆（Behavior Cloning）对基础大语言模型进行监督微调，使其获得任务规划和推理的基本能力，形成参考策略模型（π_ref），并收集多样化的交互轨迹。其次，构建两个关键模块：**分段过程奖励模型（SPRM）**和**后见模型（π_hind）**。SPRM在片段粒度（而非单轮粒度）上进行信用分配，每个片段通常对应任务分解的一个子目标；它通过在π_ref上附加一个轻量级MLP，预测每个片段对最终结果的贡献分数，并通过最小化片段贡献之和与最终奖励的均方误差来训练。后见模型则通过类似掩码语言建模的目标继续训练π_ref获得，其特点是能基于已知的轨迹结果（后见信息）来评估执行某个动作的偏好。

关键技术在于**后见信息调制机制**：通过计算后见模型与当前策略模型（π_policy）在动作序列生成概率上的比值，来衡量每个动作的重要性（z(a_k)）。比值大于1表明该动作在事后看来是推动任务完成的关键。将这些动作级重要性分数按所属片段聚合，得到片段级重要性分数（z_s）。随后，用z_s对SPRM预测的分段过程奖励（R̂）进行加权调制（即逐元素相乘并归一化），得到后见信息调制的分段奖励（R̂_him）。为了同时确保动作的可执行性，该方法还引入了一个二值的动作接地奖励（r̂^g），与调制后的奖励进行加权融合，形成最终用于强化学习优化的奖励信号（r̂_fuse）。

创新点主要体现在：1) **分段奖励设计**：避免了传统轮级奖励的过细粒度或完全忽略过程信息的问题，使奖励分配与任务子目标自然对齐。2) **后见信息调制**：创新性地利用后见模型与策略模型的似然比来量化动作重要性，从而自动突出轨迹中的关键片段，使过程奖励更加聚焦。3) **模块化协同**：将行为克隆、分段奖励估计、后见重要性评估与PPO算法结合，形成了一个完整的训练范式，显著提升了多轮决策任务中信用分配的准确性和学习效率。

### Q4: 论文做了哪些实验？

论文在三个公开的具身智能基准测试上进行了实验：Alfworld（具身家庭任务）、Virtualhome（虚拟家庭任务）和Webshop（网络导航任务）。实验设置中，智能体每回合接收环境观察并决定动作，直到任务完成或达到最大交互回合数，最终获得轨迹结果分数。

对比方法分为三类：(1) 提示工程（PE）：使用冻结的LLM（Llama3.2、GPT4o、Gemini2.5pro）进行零样本评估；(2) 行为克隆（BC）：包括监督微调（SFT）、拒绝采样微调（RFT）和直接偏好优化（DPO）；(3) 基于强化学习的微调（RL）：包括PPO、GRPO、Archer（基于结果奖励）、StepAgent、RAGEN、PRM4A和SPA（基于过程奖励）。

主要结果显示，HISR方法在三个基准测试上均取得了最佳性能。在Alfworld上，HISR的平均得分（Avg）为83.6%，显著优于最强基线SPA（79.1%）；在Virtualhome上，HISR得分为59.1%，优于SPA的53.4%；在Webshop上，HISR得分为69.1%，优于SPA的64.1%。关键数据指标包括Alfworld的六个子任务（PICK、CLEAN、HEAT、COOL、LOOK、PICK2）得分，其中HISR在LOOK和PICK2任务上分别达到100%和82.4%。

消融实验验证了核心设计的有效性：移除后见信息调制（-w/o HIM）导致性能下降（Alfworld Avg从83.6%降至80.6%）；移除分段过程奖励（-w/o SPR）也降低性能（Alfworld Avg降至82.1%）；同时移除两者（-w/o BOTH）性能最差（Alfworld Avg降至78.4%）。案例分析和统计结果进一步表明，分段奖励能更好对齐子目标，而后见信息调制能突出轨迹中的关键段。

### Q5: 有什么可以进一步探索的点？

本文的局限性及未来研究方向主要体现在三个方面。首先，轨迹分段依赖外部模型（如GPT-4o），增加了流程复杂性。未来可探索基于熵变化等指标的自动分段方法，实现端到端学习，降低对人工或外部模型的依赖。其次，后见模型在训练后固定，可能无法适应强化学习过程中数据分布的变化，限制了其动态调整能力。在线训练后见模型或采用元学习策略，使其能随策略演进同步更新，有望进一步提升性能。最后，现有分段过程奖励的先验过强（如对后续段赋予高奖励），导致后见信息的调制作用未能充分发挥。未来可研究直接利用后见信息指导过程奖励模型的训练，或设计更灵活的动态奖励调制机制，以更精准地突出关键决策段，优化信用分配。此外，将方法扩展至更复杂的多模态或跨领域任务，验证其泛化能力，也是一个值得探索的方向。

### Q6: 总结一下论文的主要内容

本文针对大型语言模型在复杂长视野智能体决策任务中表现受限的问题，提出了一种名为HISR的新方法。现有方法多集中于设计有效的奖励模型，但常面临稀疏结果奖励的延迟传播问题，以及基于回合的、过于细粒度且不聚焦的过程奖励导致的不可靠信用分配。

HISR的核心创新在于利用后见信息来调制分段过程奖励。具体而言，方法首先引入一个分段级别的过程奖励模型，为任务中的每个子目标分配奖励，避免了在单个回合层面进行过于细粒度的奖励分配。其次，设计了一个后见模型，该模型能够反映在已知轨迹结果的情况下对执行特定动作的偏好。利用这一特性，通过计算后见模型与策略模型之间的序列似然比来衡量动作的重要性，进而聚合得到分段重要性分数。这些分数随后被用来调制分段过程奖励，从而更可靠地突出轨迹中的关键片段，使奖励与子目标紧密对齐，显著提升了信用分配的可靠性。

在三个公开基准上的大量实验结果验证了该方法的有效性。其主要贡献在于通过结合后见信息和分段奖励机制，有效缓解了多轮强化学习中奖励延迟和信用分配不可靠的核心挑战，提升了智能体在长视野决策任务中的性能。
