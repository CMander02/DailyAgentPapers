---
title: "Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization"
authors:
  - "Yu Li"
  - "Sizhe Tang"
  - "Tian Lan"
date: "2026-04-08"
arxiv_id: "2604.07165"
arxiv_url: "https://arxiv.org/abs/2604.07165"
pdf_url: "https://arxiv.org/pdf/2604.07165v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent Policy Optimization"
  - "Multi-turn Reasoning"
  - "Reinforcement Learning"
  - "Reward Shaping"
  - "Tree-based Reasoning"
  - "Self-Rectification"
  - "Cognitive Tree"
  - "Surgical Policy Optimization"
relevance_score: 9.0
---

# Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization

## 原始摘要

Reinforcement learning for Large Language Model agents is often hindered by sparse rewards in multi-step reasoning tasks. Existing approaches like Group Relative Policy Optimization treat sampled trajectories as independent chains, assigning uniform credit to all steps in each chain and ignoring the existence of critical steps that may disproportionally impact reasoning outcome. In this paper, we propose T-STAR(Tree-structured Self-Taught Agent Rectification), a framework that recovers the latent correlated reward structure across seemingly independent trajectories. Specifically, we consolidate trajectories into a unified Cognitive Tree by identifying and merging functionally similar steps/nodes. It enables an Introspective Valuation mechanism that back-propagates trajectory-level rewards through the tree to obtain a new notion of variance-reduced relative advantage at step-level. Using the Cognitive Tree, we also develop In-Context Thought Grafting to synthesize corrective reasoning by contrasting successful and failed branches at critical divergence points/steps. Our proposed Surgical Policy Optimization then capitalizes on the rich policy gradient information concentrated at these critical points/steps through a Bradley-Terry type of surgical loss. Extensive experiments across embodied, interactive, reasoning, and planning benchmarks demonstrate that T-STAR achieves consistent improvements over strong baselines, with gains most pronounced on tasks requiring extended reasoning chains.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型智能体在多步推理任务中强化学习面临的稀疏奖励问题。现有方法如GRPO将采样的轨迹视为独立的推理链，对每条链中的所有步骤赋予统一的奖励，忽略了不同步骤对最终结果的影响可能存在关键差异。研究背景是，在多轮推理任务（如网页导航、具身控制）中，智能体通常采用ReAct框架，轨迹可能包含数十个决策步骤，而奖励仅在轨迹结束时稀疏地给出。现有方法的不足在于：首先，它们未能识别轨迹间潜在的关联奖励结构，导致功能相似的步骤因出现在不同轨迹中获得不一致的奖励，而功能不同的步骤在同一轨迹中却被同等对待，这使得智能体难以区分关键决策步骤与常规执行步骤。其次，丰富的策略梯度信息可能集中在那些对推理结果有不成比例影响的关键决策点上，而现有方法未能有效利用这些信息，导致策略更新次优。

本文要解决的核心问题是：如何从有限的轨迹样本和稀疏奖励中提取更丰富的策略梯度信息，以优化多轮智能体的策略。为此，论文提出了T-STAR框架，通过将轨迹整合为统一的认知树来恢复潜在的相关奖励结构，从而实现对关键决策步骤的精准信用分配和策略优化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类。

在方法类研究中，相关工作主要围绕**大语言模型智能体的强化学习（RL for LLM Agents）**和**推理中的自我改进（Self-Improvement in Reasoning）**展开。对于前者，PPO等方法因需要价值网络而在长上下文任务中计算成本高昂；GRPO及其变体（如DAPO、GiGPO）通过组内优势估计消除了价值网络，提升了训练效率，但它们通常将采样的轨迹视为独立的推理链，并为其所有步骤分配均匀的信用，忽略了关键步骤可能对结果产生不成比例影响的问题。本文提出的T-STAR框架正是为了克服这一局限，通过构建认知树来恢复不同轨迹间潜在的、相关的奖励结构。对于后者，针对长视野任务中的稀疏奖励问题，现有方法包括依赖昂贵人工标注的过程奖励模型（Process Reward Models），以及基于蒙特卡洛估计或推理时树搜索（如Tree-of-Thoughts, MCTS）的自动监督方法。然而，这些结构性方法主要优化的是推理过程而非训练动态。此外，还有如Reflexion（推理时口头反馈）、STaR（引导原理）和迭代RL更新等旨在实现持久能力提升的自我改进范式。本文指出，现有方法通常只在粗粒度的轨迹层面或严格在推理阶段操作。T-STAR通过**内省评估（Introspective Valuation）**和**上下文思维嫁接（In-Context Thought Grafting）**，在训练阶段实现了跨轨迹的细粒度信用分配和自我纠正，从而与这些工作区分开来。

在应用类研究中，论文虽未在“相关工作”章节详细列举具体应用，但其摘要和实验部分表明，本文方法在具身智能、交互、推理和规划等多个基准测试上进行了广泛验证，这暗示其研究与这些具体应用领域的智能体任务密切相关。

### Q3: 论文如何解决这个问题？

论文提出的T-STAR框架通过构建认知树、内省估值与思想嫁接、以及外科手术式策略优化三个核心支柱，系统性地解决了多步推理任务中强化学习面临的稀疏奖励问题。

**整体框架与核心方法**：T-STAR基于ReAct框架，代理在“思考-行动-观察”的多轮循环中与环境交互。其核心创新在于，不再将采样得到的多条独立轨迹视为互不关联的链，而是通过节点合并将它们整合成一个统一的**认知树**。该树结构揭示了不同轨迹间共享的决策前缀和关键的分歧点。

**主要模块与关键技术**：
1.  **认知树构建**：通过两个兼容性谓词（功能等价性和历史兼容性）识别并合并不同轨迹中功能相似的步骤（节点）。功能等价性通过比较节点在给定状态下策略输出的KL散度来判断；历史兼容性则确保节点拥有相同的、已执行的状态修改操作历史。合并后形成的树中，拥有多个子节点的位置即为**关键分歧点**，不同推理选择在此处导致不同结果。
2.  **内省估值与思想嫁接**：
    *   **Q树估值**：在构建的认知树上，通过贝尔曼方程反向传播轨迹级别的稀疏奖励，为每个树节点计算Q值。基于此，节点级别的优势值被定义为该节点Q值与组内平均奖励的归一化差值。理论分析表明，对于被k条轨迹共享的节点，其优势估计的方差降至传统GRPO方法的1/k，实现了**方差缩减**。
    *   **思想嫁接**：在识别出的关键分歧点（子节点Q值差异大的节点），代理进行自我修正。它观察成功分支与失败分支的思考-行动对，然后基于共享的父上下文，生成一个融合了成功逻辑的**修正性思考**。这过程仅需少量额外采样，却能从稀疏的轨迹奖励中合成出密集的、步骤级别的监督信号（偏好对）。
3.  **外科手术式策略优化**：策略更新采用混合损失函数，结合了轨迹级别的GRPO损失和步骤级别的外科手术损失。外科手术损失基于思想嫁接产生的偏好对，采用Bradley-Terry模型进行优化。关键设计在于，其梯度被“掩码”仅影响关键分歧点对应的单个时间步，而GRPO损失提供全时间步的学习信号，从而实现了**精准、有针对性的策略更新**，避免了对非关键步骤的干扰。

**创新点**：1) **树形结构整合与方差缩减**：通过构建认知树显式建模轨迹间的结构关联，显著降低了共享推理段落的优势估计方差。2) **基于对比的自我修正**：在关键分歧点通过对比成功与失败分支，主动合成修正性推理，将稀疏的结局奖励转化为步骤级别的监督信号。3) **精准的策略梯度更新**：利用认知树定位关键决策点，并设计外科手术式损失，将策略梯度集中在这些对最终结果影响最大的步骤上，提升了学习效率与稳定性。

### Q4: 论文做了哪些实验？

论文在具身交互、问答和逻辑规划三大类任务上进行了广泛的实验。实验设置方面，T-STAR方法被应用于Qwen2.5-3B-Instruct和Phi-4-mini-instruct-3.8B两个模型，所有方法均采用ReAct框架并配备搜索工具，训练160步，使用EMA更新的参考策略进行评估。

使用的数据集和基准测试包括：1）具身与交互环境：ALFWorld（基于文本的家庭任务，如拾取、清洁、加热、冷却）和WebShop（电子商务导航，涉及产品搜索和属性验证）；2）搜索增强问答：单跳数据集（Natural Questions, TriviaQA, PopQA）和多跳数据集（HotpotQA, 2WikiMultiHopQA, MusiQue, Bamboogle）；3）逻辑规划任务：Sokoban（不同难度等级）和Blocksworld（堆叠操作）。

对比方法包括三类基于组的强化学习方法：GRPO、DAPO和GiGPO，以及提示方法（ReAct, Reflexion）和闭源模型（GPT-4o, Gemini-1.5-Pro）。T-STAR作为增强模块应用于各RL基线之上。

主要结果显示，T-STAR在所有任务类别和基线方法上均取得一致提升。关键数据指标包括：在交互和具身任务上，ALFWorld提升3.0-3.8%，WebShop提升3.2-5.8%；在搜索增强问答中，多跳推理任务提升显著，如HotpotQA提升2.8-7.5%，2WikiMultiHopQA提升2.8-6.9%，而单跳任务提升相对较小（1.9-3.5%）；在逻辑规划任务中，Sokoban简单难度提升5.5-7.5%，中等难度提升4.5-8.5%，即使困难实例也提升3.0-4.0%。消融实验表明，移除思维嫁接导致性能下降11.6%，移除Q树估值下降7.3%，移除手术式优化下降2.6%，验证了各组件的重要性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要集中在三个方面：一是基于KL散度的功能等价性判据依赖蒙特卡洛近似，在高熵动作分布的状态下可能引入噪声；二是思维嫁接的有效性依赖于基础模型识别和表达推理差异的能力；三是当前评估仅限于基于文本的离散动作环境。未来可进一步探索的方向包括：开发更鲁棒的功能等价性度量方法，如引入自适应采样策略或基于语义的相似性评估；增强基础模型的对比分析和自我纠正生成能力，可能通过多任务预训练或引入外部知识库；将框架扩展到连续动作空间和多模态观察环境，这需要设计新的状态表示和嫁接机制。此外，可以探索认知树结构的动态优化，以及将手术策略优化与更复杂的奖励塑形方法结合，以进一步提升在长链推理任务中的样本效率和性能。

### Q6: 总结一下论文的主要内容

本文针对多步推理任务中强化学习因奖励稀疏而面临的挑战，提出T-STAR框架。现有方法常将采样轨迹视为独立链，对所有步骤均匀分配信用，忽略了关键步骤对推理结果的重大影响。T-STAR通过将轨迹整合为统一的认知树，识别并合并功能相似的步骤/节点，从而恢复看似独立轨迹间潜在的关联奖励结构。该方法引入内省评估机制，将轨迹级奖励通过树反向传播，获得方差缩减的步骤级相对优势新度量。利用认知树，框架还开发上下文思维嫁接技术，通过对比成功与失败分支在关键分歧点的差异，合成纠正性推理。最后，通过基于Bradley-Terry模型的外科手术式策略优化，集中利用关键点/步骤蕴含的丰富策略梯度信息。实验表明，T-STAR在具身、交互、推理和规划任务上均优于基线，尤其在需要长推理链的任务中提升显著。其核心贡献在于揭示了独立轨迹中潜在的可共享结构，可用于方差缩减和针对性修正，为序列决策提供了新思路。
