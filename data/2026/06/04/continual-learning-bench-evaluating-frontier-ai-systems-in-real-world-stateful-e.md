---
title: "Continual Learning Bench: Evaluating Frontier AI Systems in Real-World Stateful Environments"
authors:
  - "Parth Asawa"
  - "Christopher M. Glaze"
  - "Gabriel Orlanski"
  - "Ramya Ramakrishnan"
  - "Benji Xu"
  - "Asim Biswal"
  - "Vincent Sunn Chen"
  - "Frederic Sala"
  - "Matei Zaharia"
  - "Joseph E. Gonzalez"
date: "2026-06-04"
arxiv_id: "2606.05661"
arxiv_url: "https://arxiv.org/abs/2606.05661"
pdf_url: "https://arxiv.org/pdf/2606.05661v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Continual Learning"
  - "LLM Agent Evaluation"
  - "Memory Systems"
  - "Multi-Domain Agent"
relevance_score: 9.5
---

# Continual Learning Bench: Evaluating Frontier AI Systems in Real-World Stateful Environments

## 原始摘要

Continual learning, the ability of AI systems to improve through sequential experience, has attracted substantial interest, but no high-quality benchmark exists to evaluate it. We introduce Continual Learning Bench (CL-Bench), the first difficult, expert-validated benchmark designed to measure whether LLM-based systems genuinely improve with experience. CL-Bench spans six diverse domains (software engineering, signal processing, disease outbreak forecasting, database querying, strategic game-playing, and demand forecasting), each validated by domain experts and designed so that tasks share a learnable latent structure (codebase layout, disease outbreak dynamics, opponent strategies) that a stateful system can discover online but a stateless one cannot. We evaluate frontier models across several agent architectures, from naive in-context learning (ICL) to dedicated memory systems, introducing a gain metric to isolate learning from prior capabilities. We find that these systems leave headroom for improved continual learning: agents frequently overfit to immediate observations or fail to reuse knowledge across instances, and dedicated memory systems do not fix this -- in fact, naive ICL outperforms systems dedicated to memory management. CL-Bench is the first benchmark to evaluate continual learning across diverse real-world domains with expert-validated tasks and isolate online learning from underlying model capability, showing a need for better continual learning systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI领域在评估持续学习能力方面的关键缺失。研究背景是，构建能通过顺序经验不断改进的LLM系统（即持续学习）已成为热点，涌现了大量基于记忆、上下文压缩和测试时训练的方法。然而，现有评估方法存在明显不足：它们只测试了记忆召回、长上下文问答或特定任务上的知识注入等代理指标，无法直接衡量系统是否能在真实、序列化的环境中，通过在线学习发现并利用环境特有的隐式潜在结构（如代码库布局、疾病爆发动态、对手策略等）来提升自身表现。因此，本文要解决的核心问题是：设计并验证首个能严格、公平地评测前沿AI系统是否具备真正持续学习能力的高质量基准。该基准通过六个领域、由专家验证的复杂任务，并引入“增益”指标来隔离系统本征能力与在线学习带来的提升，从而揭示出当前最先进系统（包括专用记忆系统）在这一核心能力上仍存在巨大缺陷，例如容易过拟合即时观察或无法跨实例复用知识，甚至简单的上下文学习就优于复杂的记忆系统。这表明可靠的在线适应能力仍是开放问题。

### Q2: 有哪些相关研究？

相关研究主要分为两类。第一类是评测语言模型持续学习能力的基准，传统方法使用监督任务序列评估保留、遗忘和迁移指标。近期交互式基准如ARC-AGI-3评估环境内技能获取，LifelongAgentBench和SkillLearnBench基于预定义技能分类（如SQL和Bash原语）评测技能复用，LoCoMo、LongHealth和MemoryBench测试长对话记忆精度。这些工作的共同缺陷是，系统需学习的内容要么是显式结构化的，要么基于通用能力，或局限于单一稳定环境，没有要求系统从经验中发现隐藏结构并利用其提升后续实例表现。SWE-Bench-CL最接近，但仅限于编码领域且因指标饱和未用前沿系统评估。本文构建了六个专家验证领域，隐藏结构是任务特有且无法从预训练中恢复的，因此只有正确利用先验经验才能提升性能。第二类是智能体基准，如SWE-bench、OSWorld、GAIA等主要评测编码、终端使用等离线能力，近年虽开始测量迭代场景性能，但同样不要求利用跨实例共享的隐藏结构。没有这种结构，更强的静态模型可能直接胜出，无法隔离持续学习能力。本文明确设计了存在共享隐藏结构的任务，该结构不是通用能力，从而奖励通过在线经验改进的系统。

### Q3: 论文如何解决这个问题？

这篇论文通过设计一个全新的基准测试框架CL-Bench来解决现有LLM系统缺乏严格持续学习评估的问题。其核心方法围绕三个关键设计准则展开：**学习头空间**、**共享潜在结构**和**学习机制**。每个任务都要求系统必须从序列经验中在线学习，而非依赖静态模型能力。

整体框架包含任务构建与验证流水线、多领域任务集和专门的评估指标。主要模块/组件包括：1）**任务生成器**：针对六个领域（软件工程、数据库查询、疾病爆发预测等）构建任务；2）**任务验证模块**：经两位作者审查和2-3位领域专家验证三个维度（现实性、可复用知识、学习改进）；3）**评估系统**：将系统分为无状态（仅依赖当前实例）和有状态（利用历史状态）两种模式进行评估。

创新点主要体现在：1) 提出了**增益指标**，通过比较系统在有状态和无状态模式下的性能差异，有效分离出学习带来的改进；2) 设计了**归一化增益**，将每个系统的学习改进标准化为其自身学习头空的比例；3) 所有任务包含概念漂移，确保仅靠通用知识无法获得高绩效。实验表明，即使专门设计的记忆系统也不如简单的上下文学习，且所有系统都存在过拟合近期经验和未能有效跨实例复用知识的问题。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估。实验设置中，CL-Bench包含6个多样化领域：软件工程、信号处理、疾病暴发预测、数据库查询、策略游戏和需求预测，每个领域的数据集由领域专家验证，任务共享隐式可学习结构（如代码库布局、疾病动态、对手策略）。对比方法包括多种智能体架构：原生上下文学习（ICL）、专用记忆系统等。主要评估指标为“增益度量”（gain metric），用于隔离在线学习与预训练能力的影响。关键结果有：（1）现有系统在持续学习上性能差距明显，留有很大改进空间；（2）智能体常过度拟合即时观察或无法跨实例复用知识；（3）专用记忆系统并未解决这一问题——实际上，原生ICL的持续学习表现优于专用记忆系统，显示当前记忆管理方法存在缺陷。CL-Bench是首个在多个真实领域、经专家验证的任务上评估持续学习，并能将在线学习与底层模型能力分离的基准测试。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：首先，虽然覆盖了六个领域，但未能完全代表真实世界中的持续学习场景；其次，任务序列仅包含数十个实例，远短于实际部署中的长期需求；最后，当前评估仅聚焦于基于上下文的记忆范式，未涉及参数化方法如测试时训练。未来探索方向包括：一是扩展领域覆盖和任务序列长度，以更贴近真实部署环境，但这需平衡验证难度与成本；二是引入参数化持续学习方法，例如基于梯度更新的在线微调或元学习策略，以突破当前记忆系统的性能瓶颈；三是改善知识重用机制，避免模型过度拟合即时观测，例如设计层次化记忆结构，将短期经验与长期规律解耦。此外，可探索混合架构，结合上下文记忆与参数更新的优势，在保持模型稳定性与可扩展性的同时提升跨实例学习效率。

### Q6: 总结一下论文的主要内容

该论文提出了连续学习基准(CL-Bench)，这是首个经过专家验证、用于评估大语言模型系统能否通过顺序经验真正改进的困难基准。问题在于现有基准无法有效衡量连续学习能力。CL-Bench涵盖软件工程、信号处理、疾病爆发预测、数据库查询、策略游戏和需求预测六个领域，每个任务共享可学习的潜在结构，但有状态系统可在线发现而静态系统则不能。研究通过引入增益指标来隔离学习与先验能力，并评估了从上下文学习到专用记忆系统的多种架构。主要结论表明，当前系统在连续学习上留有改进空间：代理常过拟合即时观察或无法跨实例复用知识，专用记忆系统并未解决该问题，朴素上下文学习反而表现更优。该基准的重要性在于它首次在多样化现实领域评估连续学习，并揭示当前系统能力的显著差距。
