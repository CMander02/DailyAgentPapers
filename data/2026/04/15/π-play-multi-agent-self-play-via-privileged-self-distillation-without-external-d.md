---
title: "$π$-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Data"
authors:
  - "Yaocheng Zhang"
  - "Yuanheng Zhu"
  - "Wenyue Chong"
  - "Songjun Tu"
  - "Qichao Zhang"
  - "Jiajun Chai"
  - "Xiaohan Wang"
  - "Wei Lin"
  - "Guojun Yin"
  - "Dongbin Zhao"
date: "2026-04-15"
arxiv_id: "2604.14054"
arxiv_url: "https://arxiv.org/abs/2604.14054"
pdf_url: "https://arxiv.org/pdf/2604.14054v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "Multi-Agent"
  - "Self-Play"
  - "Self-Distillation"
  - "Privileged Information"
  - "Training Framework"
  - "Search Agent"
  - "Data-Efficient Learning"
relevance_score: 8.5
---

# $π$-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Data

## 原始摘要

Deep search agents have emerged as a promising paradigm for addressing complex information-seeking tasks, but their training remains challenging due to sparse rewards, weak credit assignment, and limited labeled data. Self-play offers a scalable route to reduce data dependence, but conventional self-play optimizes students only through sparse outcome rewards, leading to low learning efficiency. In this work, we observe that self-play naturally produces a question construction path (QCP) during task generation, an intermediate artifact that captures the reverse solution process. This reveals a new source of privileged information for self-distillation: self-play can itself provide high-quality privileged context for the teacher model in a low-cost and scalable manner, without relying on human feedback or curated privileged information. Leveraging this insight, we propose Privileged Information Self-Play ($π$-Play), a multi-agent self-evolution framework. In $π$-Play, an examiner generates tasks together with their QCPs, and a teacher model leverages QCP as privileged context to densely supervise a student via self-distillation. This design transforms conventional sparse-reward self-play into a dense-feedback self-evolution loop. Extensive experiments show that data-free $π$-Play surpasses fully supervised search agents and improves evolutionary efficiency by 2-3$\times$ over conventional self-play.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度搜索智能体在复杂信息寻求任务中训练效率低下的问题。研究背景是，尽管基于大语言模型和外部搜索引擎的深度搜索智能体在信息获取方面展现出潜力，但其训练面临三大挑战：稀疏奖励导致信号不足、多轮搜索中信用分配困难，以及依赖大量标注数据或专家轨迹成本高昂。现有方法中，自我对弈（self-play）虽能通过模型自主生成任务来减少数据依赖，但学生模型仅通过稀疏的结果奖励进行优化，学习效率低下；而自我蒸馏（self-distillation）虽能利用特权信息提供密集监督以改善信用分配，却通常依赖人工反馈或更强模型来构建特权信息，难以规模化。

本文的核心问题是：如何在不依赖外部数据或人工干预的情况下，高效地利用自我对弈过程中自然产生的中间信息，将稀疏奖励优化转化为密集反馈，从而提升搜索智能体的训练效率和最终性能。为此，论文提出利用自我对弈中自然产生的问题构建路径（QCP）——它记录了从答案反向构建问题的多步搜索过程——作为一种内在的、高质量的特权信息。通过设计一个名为Privileged Information Self-Play（π-Play）的多智能体自进化框架，让考官生成任务及QCP，教师模型利用QCP作为特权上下文对学生模型进行密集的令牌级蒸馏监督，从而构建一个密集反馈的自进化循环，显著提升进化效率。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：方法类、应用类和评测类。

在方法类中，相关工作包括：1）深度搜索智能体，它结合大语言模型与外部搜索引擎进行多轮检索分析，但训练受限于稀疏奖励和有限标注数据；2）自博弈方法，如R-Zero、SSP和Dr.Zero，通过让智能体自主生成并解决任务来减少对人工标注的依赖，但通常仅依赖稀疏的结果奖励进行优化，学习效率较低；3）自蒸馏方法，其中教师模型利用特权信息为学生模型提供细粒度监督，但传统方法依赖人类专家或更强模型来构造特权信息，可扩展性受限。

在应用类中，相关工作如Search-R1、R1-Searcher等，通过强化学习提升智能体的问答能力，但仍受训练数据规模的约束。

本文提出的π-Play框架与这些工作的关系和区别在于：它创新性地将自博弈与自蒸馏相结合。与仅依赖稀疏奖励的自博弈不同，π-Play利用自博弈过程中自然产生的问题构建路径作为特权信息，提供给教师模型，从而为学生提供密集的令牌级监督。这既克服了传统自博弈的稀疏奖励问题，又避免了自蒸馏对外部特权信息的依赖，实现了无需外部数据的高效自我进化。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Privileged Information Self-Play（π-Play）的多智能体自进化框架来解决深度搜索智能体训练中的稀疏奖励、信用分配困难和数据依赖问题。其核心方法是将传统的稀疏奖励自博弈转化为一个具有密集反馈的自蒸馏循环，从而显著提升学习效率。

整体框架包含三个核心模块：出题者（Examiner）、教师（Teacher）和学生（Student）。三者均基于同一个基础大语言模型初始化，并仅依赖搜索工具获取外部知识，严格遵循无外部训练数据的设定。

出题者的核心创新在于其任务生成过程。它不仅生成问题-答案对，还会自然产生一个记录逆向解题过程的“问题构建路径”。出题者通过一个难度奖励函数进行优化，该函数利用学生对生成问题的成功率作为反馈，旨在生成对学生当前能力而言难度适中、可验证且非平凡的问题。具体而言，奖励函数惩罚学生完全失败或轻易成功的情况，鼓励生成恰好有一部分答案正确的题目，从而形成动态演进的课程。

教师模型的关键创新在于利用出题者提供的“问题构建路径”作为特权信息。这使得教师能够在拥有额外上下文的情况下生成更准确的推理轨迹，从而为学生提供密集的、令牌级别的指导。为了避免教师与学生差异过大，教师的目标函数在最大化答案正确率的同时，还包含一个KL散度项来约束其输出分布与学生分布（在无特权信息下）的差异。在实际优化中，为了平衡效果与计算开销，教师参数通过学生参数的指数移动平均来更新，使其既能保持相对稳定，又能跟随学生共同进化。

学生模型通过一个混合目标进行训练：一方面，它通过基于答案正确性的结果奖励（采用分组相对策略优化GRPO）来学习；另一方面，它通过一个蒸馏损失项来对齐教师模型的输出分布。这个蒸馏损失使学生能够从教师基于特权信息生成的优质轨迹中学习，实现了从稀疏结果奖励到密集令牌级指导的转变，从而更高效地进行信用分配和策略改进。

整个系统通过一个交替优化循环协同工作：出题者生成带构建路径的题目；学生尝试解题并获得结果奖励及教师指导；教师通过EMA与学生软对齐；出题者再根据学生的表现调整题目难度。这种设计形成了一个共生的反馈循环：更强的学生促使出题者生成更具挑战性的题目，而教师的密集指导又加速了学生的进化。实验表明，这种无需外部数据的方法在多项搜索任务上超越了完全监督的基线，并将进化效率较传统自博弈提升了2-3倍。

### Q4: 论文做了哪些实验？

论文在三个不同规模的Qwen-3系列模型（Qwen3-4B、Qwen3-4B-Instruct-2507和Qwen3-8B）上进行了实验。实验评估使用了七个问答基准数据集，包括三个单跳问答基准（NQ、TriviaQA、PopQA）和四个多跳问答基准（HotpotQA、2WikiMQA、MuSiQue、Bamboogle）。所有模型在统一的搜索引擎（E5-base）和知识库（英文维基百科）设置下，使用精确匹配分数进行评估。

对比方法包括三类基线搜索智能体：免训练的ReAct、有监督强化学习方法（Search-R1和ToolForge）以及自博弈方法（Dr.Zero和SQLM*）。主要结果如下：π-Play在无需任何外部训练数据的情况下，整体性能显著优于基础大语言模型和所有基线方法。具体而言，在平均性能上，π-Play相比有监督的Search-R1方法，在三个模型上分别提升了6.2%、5.2%和14.5%。与自博弈方法Dr.Zero相比，π-Play在多个模型规模和迭代轮次中均取得更高分数，尤其在需要多步推理的多跳问答基准上优势更为明显。关键数据指标显示，在Qwen3-8B模型上，经过三轮迭代后，π-Play在七个数据集上的总分达到280.3，高于Dr.Zero的274.9。此外，学习动态分析表明，π-Play的学生模型在第一轮迭代后性能即达到或超过Dr.Zero三轮迭代后的收敛水平，进化效率提升了2-3倍，并且奖励和熵指标在第三轮迭代后趋于收敛。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来研究可从以下几个方向深入探索。首先，论文的核心是利用自我对弈中自然产生的问题构建路径作为特权信息进行蒸馏，但QCP的生成质量和完整性是关键。当前方法可能依赖于特定的任务结构，未来可研究如何将QCP的概念泛化到更广泛的任务类型，例如开放域对话或复杂决策问题，其中“反向解构过程”可能不那么明确。其次，审查者与学生的协同进化机制虽然有效，但动态平衡的稳定性有待加强。例如，审查者生成问题的难度提升曲线可能导致学生陷入局部最优，未来可引入课程学习或自适应难度调整策略，使任务生成更符合学生的当前能力。此外，论文中的蒸馏过程主要基于监督信号，未来可探索结合强化学习中的内在奖励或好奇心驱动机制，进一步提升学生在稀疏奖励环境下的探索效率。最后，该方法目前未利用外部数据，但现实场景中可能存在少量人类反馈或高质量种子数据，研究如何以半监督方式融合这些资源，可能进一步提升性能并加速收敛。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为Privileged Information Self-Play（π-Play）的多智能体自进化框架，旨在解决深度搜索智能体训练中存在的稀疏奖励、信用分配困难和标注数据有限等挑战。其核心贡献在于发现并利用自博弈过程中自然产生的问题构建路径（QCP）作为特权信息，从而将传统的稀疏奖励自博弈转变为密集反馈的自进化循环。

方法上，π-Play构建了一个多智能体系统：一个“考官”生成任务及其对应的QCP（即反向解题过程），一个“教师”模型利用QCP作为特权上下文，通过自我蒸馏的方式对“学生”模型进行密集监督。这种方法无需依赖外部数据或人工反馈，低成本地生成了高质量的监督信号。

主要结论是，实验表明，这种无需外部数据的π-Play框架性能超越了完全监督的搜索智能体，并且将进化效率相比传统自博弈提升了2-3倍。这为高效、可扩展地训练复杂信息寻求任务智能体提供了一条新路径。
