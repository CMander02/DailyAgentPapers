---
title: "MITS: Enhanced Tree Search Reasoning for LLMs via Pointwise Mutual Information"
authors:
  - "Jiaxi Li"
  - "Yucheng Shi"
  - "Xiao Huang"
  - "Jin Lu"
  - "Ninghao Liu"
date: "2025-10-04"
arxiv_id: "2510.03632"
arxiv_url: "https://arxiv.org/abs/2510.03632"
pdf_url: "https://arxiv.org/pdf/2510.03632v2"
github_url: "https://github.com/plusnli/MITS"
categories:
  - "cs.AI"
tags:
  - "推理"
  - "树搜索"
  - "信息论"
  - "计算效率"
  - "测试时优化"
  - "规划"
relevance_score: 8.5
---

# MITS: Enhanced Tree Search Reasoning for LLMs via Pointwise Mutual Information

## 原始摘要

Tree search has become as a representative framework for test-time reasoning with large language models (LLMs), exemplified by methods such as Tree-of-Thought and Monte Carlo Tree Search. However, it remains difficult to provide instant and reliable quantitative assessments of intermediate reasoning step quality, and extensive path exploration is computationally costly. To address this, we propose Mutual Information Tree Search (MITS), a novel framework that guides reasoning with information-theoretic principles. MITS introduces an effective scoring function based on pointwise mutual information (PMI), which enables step-wise evaluation of reasoning paths and search tree expansion via beam search without expensive look-ahead simulations, achieving superior reasoning performances while maintaining computational efficiency. The framework is complemented by an entropy-based dynamic sampling strategy that adaptively allocates computational resources to uncertain reasoning steps where exploration is most beneficial. For final prediction, MITS employs a weighted voting scheme that combines PMI scores with prediction consensus. Through comprehensive experiments on diverse reasoning benchmarks, MITS consistently surpasses baseline methods, establishing a principled and efficient framework for LLM reasoning. The code is available at https://github.com/plusnli/MITS.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在复杂多步推理任务中，如何高效且可靠地搜索最优推理路径的核心问题。研究背景是，尽管思维链（CoT）等提示技术能分解问题，但其生成的单一推理路径容易因错误累积或策略次优而失败。现有方法如蒙特卡洛树搜索（MCTS）虽能探索多条路径，但依赖大量前向模拟，计算成本高昂；而自评估方法难以对推理步骤质量提供即时、可靠的量化评估，往往只能进行二元判断或简单比较，无法区分通用推理与针对特定问题的有效推理。因此，本文的核心问题是：如何在避免昂贵计算开销的前提下，从指数级增长的推理路径空间中，高效地识别出最有可能产生正确答案的路径。为此，论文提出了基于点互信息（PMI）的互信息树搜索框架，旨在通过信息论原理指导推理，实现无需前瞻模拟的步骤级评估和资源自适应分配，从而兼顾推理性能与计算效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 提示工程与推理方法**：以Chain-of-Thought（CoT）为代表的一系列工作，通过设计指令和流程来激发大语言模型的推理能力。后续的Tree-of-Thought（ToT）和Monte Carlo Tree Search（MCTS）等方法将树搜索框架引入推理过程，允许模型探索多条推理路径。本文提出的MITS框架属于此类，但区别于ToT和MCTS需要昂贵的前向模拟或难以量化评估中间步骤，MITS利用点互信息（PMI）作为评分函数，无需前瞻模拟即可实现高效的束搜索。

**2. 搜索与规划算法**：传统基于树的搜索算法（如MCTS）在LLM推理中被广泛借鉴，但其计算成本高。本文的MITS通过基于信息论的PMI评分和基于熵的动态采样策略，在保证性能的同时显著提升了计算效率，这是一种算法层面的创新。

**3. 评估与决策机制**：许多方法依赖于LLM本身或额外训练的评价器来评估推理步骤。本文的核心贡献之一是提出了一个基于PMI的、无需训练的即时量化评估函数，用于步骤质量评估和路径选择。在最终预测阶段，MITS采用的加权投票方案结合了PMI分数和预测一致性，这也与单纯依靠自我一致性或多数投票的方法不同。

综上所述，本文在现有提示推理和树搜索方法的基础上，通过引入信息论原理，在中间步骤评估、资源动态分配和最终决策整合等方面做出了针对性改进，建立了一个更高效、更有原则的推理框架。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“互信息树搜索”（MITS）的新型框架来解决现有树搜索方法在评估中间步骤质量和计算成本高方面的问题。其核心方法是利用信息论原理，特别是点互信息（PMI），来指导推理树的构建和评估，从而在保证高效计算的同时提升推理性能。

整体框架包含三个主要组件。首先是**基于点互信息（PMI）的评分函数**。该方法将推理路径的质量评估定义为问题与解决方案之间的互信息。具体地，PMI评分公式为 \( \log \frac{p(S \mid q)}{p(S)} \)，其中 \( p(S \mid q) \) 衡量给定问题下推理路径的匹配度，而 \( p(S) \) 则惩罚那些与问题无关的通用推理路径。为了高效计算，论文采用了增量更新策略，使得每一步的PMI得分可以通过累加上一步的得分和当前步骤的增量信息增益来获得，无需从头重新计算。

其次是**搜索树的构建**。该过程结合了动态采样和PMI引导的束搜索。在每一步，生成模型基于问题和已有路径产生多个候选推理步骤。关键创新在于**基于熵的动态采样策略**：通过计算当前步骤生成时的令牌分布熵来量化不确定性，并利用历史熵值的分位数（如33%和67%）自适应地将熵划分为高、中、低三个区域，从而动态决定为下一步生成多少候选（例如，不确定性高的步骤分配更多采样资源）。随后，评估模型计算每个候选步骤的增量PMI贡献，并更新累积PMI得分。通过**PMI引导的束搜索**，系统仅保留累积PMI得分最高的前B条路径进行后续扩展，有效控制了计算开销并聚焦于最有希望的推理方向。

最后是**基于加权平均投票的输出选择**。搜索完成后，会得到一组候选推理链。论文没有简单地选择PMI得分最高的链，而是提出了一种加权投票方案以平衡置信度与共识。具体而言，从PMI得分最高的K条链中，根据每条链的最终预测答案的出现频率对其PMI得分进行加权（即 \( PMI^{*} = PMI \times \frac{频率}{K} \)），然后选择加权后得分最高的链作为最终输出。这种方法降低了因虚假相关性导致错误预测的风险。

综上所述，MITS的创新点在于：1) 引入PMI作为原则性、可解释的步骤级评估指标；2) 提出熵驱动的动态采样策略，自适应分配计算资源；3) 结合PMI引导的束搜索与加权投票，在效率与可靠性之间取得平衡。通过这些设计，MITS实现了无需前瞻模拟的高效、高性能推理。

### Q4: 论文做了哪些实验？

论文在多个推理基准上进行了全面的实验验证。实验设置方面，主要使用了Qwen2.5-3B/7B-Instruct和Phi-3.5/4-mini-Instruct等指令微调模型作为主干。数据集包括需要多跳隐式推理的StrategyQA、科学知识密集的ARC-Challenge以及依赖世界常识的CommonsenseQA。实现细节上，MITS采用基于点互信息（PMI）的评分函数，通过除以步数进行长度归一化以消除偏差；搜索树最大深度设为10，默认采样数N_base=3，束搜索宽度B=32；同时对比了完全展开搜索树的MITSfull变体。

对比方法涵盖三类：单链思维链提示（CoT）、多采样思维链自洽（CoT-SC，采样32次）以及树搜索方法（包括Tree-of-Thoughts-ToT、RAP和rStar，其中RAP和rStar使用蒙特卡洛树搜索并执行32次模拟）。主要结果如下：在推理性能上，MITS在所有数据集和模型规模上均一致超越基线。关键指标上，在StrategyQA（Qwen2.5-3B）上准确率达68.45%，较CoT提升21.11个百分点；在ARC-Challenge（Qwen2.5-7B）上达92.55%，较最强基线rStar提升5.31个百分点。在计算效率上，在StrategyQA（Qwen2.5-3B）上，MITS仅需64.41秒达到68.45%准确率，显著优于RAP（203.42秒，60.56%）和rStar（815.67秒，65.32%），实现了精度与效率的最佳权衡。消融实验表明，PMI的平均聚合优于累加聚合（在Qwen2.5-3B上提升2.56%），且加权投票中增大K值（如K=32）能进一步提升性能。此外，实验还验证了更强评估模型能带来更可靠的PMI估计，以及MITS在较少模拟次数下即可实现显著性能提升。

### Q5: 有什么可以进一步探索的点？

该论文提出的MITS框架虽然在效率和性能上有所提升，但仍存在一些局限性，为未来研究提供了方向。首先，其核心评分函数基于点间互信息（PMI），但PMI的计算依赖于语言模型本身生成的概率估计，这可能受模型校准误差影响，导致评分偏差。未来可探索更稳健的信息度量或结合外部知识验证来增强评估可靠性。其次，框架虽采用动态采样，但对“不确定性”的判定标准较为简单，未来可引入更精细的元认知机制，让模型能自我评估认知状态，从而更智能地分配资源。此外，MITS目前主要针对数学推理和常识问答任务，在需要多模态或长程依赖的复杂推理（如代码生成或科学问题求解）中效果未经验证，扩展其适用性是一个重要方向。最后，框架的搜索过程仍受限于束搜索的局部性，未来可结合蒙特卡洛树搜索的全局探索优势，设计混合策略，在效率与深度间取得更好平衡。

### Q6: 总结一下论文的主要内容

该论文提出了一种基于互信息树搜索（MITS）的新框架，旨在解决大语言模型在复杂多步推理任务中面临的挑战。核心问题是现有树搜索方法（如思维树、蒙特卡洛树搜索）难以对中间推理步骤进行即时可靠的量化评估，且广泛路径探索计算成本高昂。

MITS的核心贡献在于引入了一种基于点互信息（PMI）的评分函数。该方法通过信息论原理指导推理，量化推理路径与特定问题之间的相关性，从而有效过滤通用或虚假的推理模式，实现无需昂贵前瞻模拟的步骤级评估和束搜索扩展。此外，框架还包含一个基于熵的动态采样策略，能自适应地将计算资源分配到不确定性高的推理步骤以优化探索，并采用结合PMI分数与预测共识的加权投票方案进行最终预测，以降低选择高分但虚假路径的风险。

实验表明，MITS在多种推理基准测试中 consistently 超越基线方法，在保持计算效率的同时实现了卓越的推理性能，为LLM推理建立了一个原则性且高效的框架。
