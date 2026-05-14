---
title: "R^2-Mem: Reflective Experience for Memory Search"
authors:
  - "Xinyuan Wang"
  - "Wenyu Mao"
  - "Junkang Wu"
  - "Xiang Wang"
  - "Xiangnan He"
date: "2026-05-13"
arxiv_id: "2605.13486"
arxiv_url: "https://arxiv.org/abs/2605.13486"
pdf_url: "https://arxiv.org/pdf/2605.13486v1"
categories:
  - "cs.CL"
tags:
  - "Agent记忆"
  - "反思学习"
  - "Agent自我改进"
  - "搜索Agent"
  - "经验蒸馏"
relevance_score: 8.5
---

# R^2-Mem: Reflective Experience for Memory Search

## 原始摘要

Deep search has recently emerged as a promising paradigm for enabling agents to retrieve fine-grained historical information without heavy memory pre-managed. However, existing deep search agents for memory system repeat past error behaviors because they fail to learn from the prior high- and low-quality search trajectories. To address this limitation, we propose R^2-Mem, a reflective experience framework for memory search systems. In the offline stage, a Rubric-guided Evaluator scores low- and high-quality steps in historical trajectories, and a self-Reflection Learner distills the corresponding abstract experience. During the online inference, the retrieved experience will guide future search actions to avoid repeated mistakes and maintain high-quality behaviors. Extensive experiments demonstrate that R^2-Mem consistently improves both effectiveness and efficiency over strong baselines, improving F1 scores by up to 22.6%, while reducing token consumption by 12.9% and search iterations by 20.2%. These results verify that R^2-Mem provides a RL-free and low-cost solution for self-improving LLM agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有深度搜索代理在记忆系统中重复错误行为的问题。研究背景是，大型语言模型驱动的AI代理需要有效的记忆系统来整合信息，而现有方法如预管理记忆图、压缩记忆单元或启发式结构，以及端到端强化学习优化，都存在丢失细粒度历史细节和高计算成本的不足。最近提出的深度搜索范式通过在运行时进行迭代规划、搜索和反思来检索记忆，避免了预先管理，但现有代理将每条搜索轨迹孤立处理，未能跨轨迹累积可复用经验，导致重复无效的规划和反思行为、冗余探索、检索质量下降以及推理成本增加。更关键的是，每条轨迹包含混合质量的步骤，成功轨迹可能含无效动作，失败轨迹也可能有有用部分，因此整体判定好坏不可靠。本文的核心问题是：如何以细粒度方式识别历史轨迹中的高、低质量步骤，并从中累积可复用的抽象经验，从而指导未来搜索行为，避免重复错误并维持高质量行为，且不依赖强化学习或高昂成本。为此，作者提出R²-Mem框架，通过离线阶段的评估和蒸馏构建经验库，在线阶段检索经验来改进搜索。

### Q2: 有哪些相关研究？

相关工作主要分为三类：

1. **深度搜索记忆系统**：近期研究从预管理记忆系统转向迭代深度搜索，动态进行多步规划、搜索和反思以提取细粒度历史信息。本文在此基础上，进一步利用历史搜索轨迹中的高质量和低质量行为，通过反思性经验框架提升后续搜索质量，弥补了现有系统仅将轨迹用于当前检索、未将其转化为可复用指导的不足。

2. **经验学习方法**：现有工作通过外部化成功轨迹、言语反思或可复用技能构建经验库，使LLM智能体无需昂贵的端到端策略重训练即可自我进化。但这些方法通常以完整轨迹或任务为单元，粒度较粗，不适用于深度记忆搜索中依赖细粒度规划与反思行为的场景。本文提出步骤级别的反思性经验蒸馏，从中间行为中提取可复用指导，实现更精准的纠错。

3. **量规驱动（rubric-based）监督**：量规被用于分解输出质量并提供结构化监督，但主要集中于最终结果评估或强化学习对齐，较少涉及长多步轨迹中的过程质量诊断。本文创新性地引入量规指导的评估器，识别步骤级别的高/低质量搜索行为，从而在迭代记忆搜索场景中稳定地提取反思经验。

### Q3: 论文如何解决这个问题？

R²-Mem通过**反思性经验优化框架**解决现有深度搜索代理在记忆系统中重复错误行为的问题，核心在于无需强化学习即可实现自我改进。整体框架分为**离线构建**和**在线推理**两个阶段。

在离线阶段，框架由两个核心模块协同工作：**Rubric引导评估器**和**自我反思学习器**。评估器首先对历史搜索轨迹进行多维度、细粒度的步骤级打分（例如根据规划质量和反思质量），每个步骤获得一个综合分数、评估理由和可操作建议。随后，学习器基于评估结果进行自我反思，将高分（优质）和低分（劣质）轨迹中的关键步骤提炼为抽象经验，并按**质量标签**（好/坏）和**功能标签**（规划/反思）分类存储到对应的**经验库**中。例如，规划经验库储存关于如何分解问题、生成工具使用动作的指导；反思经验库则储存关于如何评估信息充分性、决定下一步搜索方向的教训。

在线推理时，当代理执行新的记忆搜索时，会首先利用**条件-情境抽象机制**将当前状态（如当前问题、临时记忆）转化为高层情境表示，然后从经验库中检索最相似的Top-K条相关经验。这些检索到的经验会被注入深度搜索循环：规划经验用于指导问题分解和动作生成，反思经验则用于支持充分性评估和下一步决策。通过这种**检索增强的反馈机制**，代理能够主动避免过去的低质量行为（如过早停止或无效跳转），并持续模仿高质量行为（如精准分解问题），从而在提升搜索效果（F1最高提升22.6%）的同时显著降低令牌消耗和搜索迭代次数。

### Q4: 论文做了哪些实验？

论文在三个数据集上进行了实验：LoCoMo（长期对话数据集，需多跳和时间推理）、HotpotQA（基于维基百科的多跳问答）和NarrativeQA（全书或脚本推理）。对比方法包括四类：(1) 无记忆检索（vanilla RAG）；(2) 结构化记忆管理（A-Mem, MemoryOS, LightMem）；(3) 基于强化学习的记忆（Memory-R1）；(4) 深度搜索记忆（GAM）。使用Qwen2.5（3B/7B/14B）和Llama3.1-8B作为主干模型，F1和BLEU1作为评价指标。

主要结果：在LoCoMo上，R²-Mem在Qwen2.5-7B上总体F1达51.35，BLEU达44.91，超越所有基线，相比最强基线GAM提升12.2% F1。在Qwen2.5-3B上总体F1提升22.6%（从32.00到39.24），同时token消耗减少12.9%，搜索迭代减少20.2%。在NarrativeQA和HotpotQA上，R²-Mem在Qwen2.5-7B上F1分别提升10.37%和10.89%。消融实验表明，移除评估器或学习者均导致性能下降，低质量经验比高质量经验贡献更大，规划经验和反思经验缺一不可。超参数分析显示，在合理范围内，评分阈值和检索数量k对性能影响不敏感。

### Q5: 有什么可以进一步探索的点？

R^2-Mem在反思机制与记忆搜索结合上取得了进展，但仍有若干待探索方向。首先，当前框架依赖离线阶段的Rubric评估器，这需要人工设计细粒度评分标准，未来可探索利用LLM本身或强化学习中的奖励模型实现自动化的步骤质量评估，减少人工干预。其次，反思经验以文本形式存储和检索，其抽象程度和泛化能力有限，可研究将经验压缩为紧凑的向量表示或结构化规则，提升跨任务迁移的效率。此外，该方法虽声称无需强化学习，但在复杂长尾场景下，经验库可能迅速膨胀导致检索成本上升，未来可引入记忆遗忘机制或分层索引。最后，当前实验仅在单轮搜索任务进行，可拓展至多轮对话规划、工具使用等更复杂的Agent场景，验证其能否有效避免错误链式传播。

### Q6: 总结一下论文的主要内容

论文提出了一种名为R^2-Mem的反思经验框架，用于解决深度记忆搜索系统中代理重复历史错误行为的问题。现有系统依赖结果级监督，缺乏从搜索轨迹中学习高质量与低质量步骤的能力。R^2-Mem在离线阶段通过规则引导评估器对历史轨迹的步骤进行评分，并由自我反思学习器提炼抽象经验；在线推理时，检索到的经验会引导未来搜索动作，避免重复错误并保持高质量行为。实验表明，R^2-Mem在多个基线上持续提升有效性和效率，F1分数最高提升22.6%，同时减少12.9%的令牌消耗和20.2%的搜索迭代次数。这一无强化学习、低成本的方案为LLM代理的自我改进提供了新路径，强调了过程级监督对构建高效可靠记忆增强型代理的重要性。
