---
title: "KARL: Knowledge Agents via Reinforcement Learning"
authors:
  - "Jonathan D. Chang"
  - "Andrew Drozdov"
  - "Shubham Toshniwal"
  - "Owen Oertell"
  - "Alexander Trott"
date: "2026-03-05"
arxiv_id: "2603.05218"
arxiv_url: "https://arxiv.org/abs/2603.05218"
pdf_url: "https://arxiv.org/pdf/2603.05218v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 9.0
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "Enterprise & Workflow"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "iterative large-batch off-policy RL, agentic synthesis pipeline"
  primary_benchmark: "KARLBench"
---

# KARL: Knowledge Agents via Reinforcement Learning

## 原始摘要

We present a system for training enterprise search agents via reinforcement learning that achieves state-of-the-art performance across a diverse suite of hard-to-verify agentic search tasks. Our work makes four core contributions. First, we introduce KARLBench, a multi-capability evaluation suite spanning six distinct search regimes, including constraint-driven entity search, cross-document report synthesis, tabular numerical reasoning, exhaustive entity retrieval, procedural reasoning over technical documentation, and fact aggregation over internal enterprise notes. Second, we show that models trained across heterogeneous search behaviors generalize substantially better than those optimized for any single benchmark. Third, we develop an agentic synthesis pipeline that employs long-horizon reasoning and tool use to generate diverse, grounded, and high-quality training data, with iterative bootstrapping from increasingly capable models. Fourth, we propose a new post-training paradigm based on iterative large-batch off-policy RL that is sample efficient, robust to train-inference engine discrepancies, and naturally extends to multi-task training with out-of-distribution generalization. Compared to Claude 4.6 and GPT 5.2, KARL is Pareto-optimal on KARLBench across cost-quality and latency-quality trade-offs, including tasks that were out-of-distribution during training. With sufficient test-time compute, it surpasses the strongest closed models. These results show that tailored synthetic data in combination with multi-task reinforcement learning enables cost-efficient and high-performing knowledge agents for grounded reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何高效训练能够进行“有据推理”的企业级知识智能体的问题。所谓“有据推理”，是指智能体需要执行多步骤信息收集，并基于收集到的外部证据进行复杂推理的任务，这在金融、法律、医疗等依赖海量专有数据的企业场景中具有极高价值。

研究背景在于，尽管当前已有一些针对“深度研究”的智能体，但它们主要依赖公开网络数据和黑盒搜索工具，其能力是否能在更广泛、更专有的有据推理任务上泛化尚不明确。现有方法存在几个关键不足：首先，缺乏一个全面评估智能体多维度有据推理能力的基准测试套件，现有基准往往只覆盖有限的行为模式。其次，为单一任务优化的系统无法保证在其他任务上的能力，缺乏通用的训练方法。最后，传统的训练数据生成方法（如单纯提示或静态合成代理）难以产生足够多样、有据且高难度的数据，而在线强化学习训练在大规模模型上又存在训练与推理引擎不匹配导致的稳定性问题。

因此，本文试图解决的核心问题是：如何系统地构建和训练一个能够在多样化的、难以验证的企业级有据推理任务上，实现高性能、高成本效益且具备强大泛化能力的知识智能体。为此，论文提出了四个核心贡献来应对上述挑战：构建一个涵盖六种不同搜索机制的多能力评估套件（KARLBench）；证明跨异构搜索行为训练能带来更好的泛化性；开发一个能自主探索语料库以生成高质量、有据训练数据的智能体合成管道；并提出一种基于迭代大批量离策略强化学习的新后训练范式，该范式样本高效、对训练-推理差异鲁棒，并能自然扩展到多任务训练与分布外泛化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测基准、数据合成方法和强化学习训练范式。

在**评测基准**方面，已有工作如HotpotQA、BrowseComp-Plus和FinanceBench等，但它们通常只针对特定类型的搜索或推理任务（如多跳问答、网页浏览或金融数值推理），覆盖的“基于证据的推理”能力范围有限。本文提出的KARLBench则整合了六种不同的搜索机制，形成了一个更全面、异构的多能力评估套件，旨在更系统地评估智能体在多样化、真实企业场景下的综合推理能力。

在**数据合成方法**上，传统方法多依赖静态提示或固定的合成代理来生成训练数据，其多样性和难度有限。本文提出的“智能体合成”管道，让智能体通过向量搜索动态探索语料库，生成基于检索证据的、高质量且多样化的问答对，并利用性能提升后的智能体进行迭代自举，实现了数据的持续优化。

在**强化学习训练范式**方面，针对大规模模型（尤其是MoE模型）的在线GRPO训练通常需要复杂的稳定性技巧。本文提出的OAPL（迭代大批次离线策略RL）范式，通过在设计目标函数时直接接纳离线策略性，降低了对训练与推理引擎一致性的依赖，简化了基础设施设计，并能自然地扩展到多任务训练，展现出良好的分布外泛化能力。

### Q3: 论文如何解决这个问题？

论文通过一个结合了智能体数据合成、离线策略强化学习（RL）和多任务训练的综合性框架来解决训练高性能知识智能体的问题。其核心方法分为三个主要部分：智能体数据合成管道、基于OAPL的离线策略RL后训练范式，以及通过多任务RL实现泛化。

首先，**智能体数据合成管道**旨在生成高质量、多样化的训练数据。该管道分为两个阶段：1) **问题-答案合成**：一个合成智能体利用向量搜索工具探索文档语料库，并基于检索到的文档生成新颖且具有挑战性的问题-答案对，确保数据的“接地性”。随后通过去重智能体过滤掉与示例重复的内容。2) **解决方案合成**：多个求解器智能体独立尝试解答第一阶段生成的问题，并根据通过率（正确尝试的比例）过滤掉过易或过难的问题。最后，质量过滤器智能体筛查剩余数据，剔除存在歧义或参考答案错误的问题-答案对，从而保留学习信号最丰富的合成数据用于RL训练。

其次，**后训练范式**采用了名为OAPL（基于最优优势的策略优化）的新型**离线策略RL方法**。其核心是使用大批次迭代的离线数据，优化一个KL正则化的目标函数。该方法从参考模型（如基础模型）采样生成多组轨迹（rollouts），然后通过最小化一个最小二乘回归损失来学习最优策略，该损失函数关联了策略对数比与估计的“优势”函数（即奖励减去基线值）。这种方法计算高效，能稳定训练大规模模型（如MoE），且避免了在线RL的复杂性和高昂成本。训练过程是迭代的：用更新后的策略作为新的参考模型重新生成数据并再次优化。

最后，为实现**分布外泛化**，论文将上述框架应用于**多任务RL**。具体而言，它选择两个具有不同能力需求的任务（如需要深度搜索和广度搜索的任务）作为分布内训练任务，在训练时简单地将它们的损失结合，并平衡来自各任务的数据量。论文发现，这种多任务RL方法在保持分布内性能的同时，比基于蒸馏的多专家方法展现出更好的分布外泛化能力。

整体框架的创新点在于：1) 一个两阶段的、基于工具使用的智能体数据合成流程，能自动生成高质量且难度适中的训练数据；2) 提出了一种样本高效、稳健且易于扩展到多任务的大批次迭代离线策略RL算法（OAPL）；3) 通过简单的多任务RL数据平衡策略，有效提升了模型在未见任务上的泛化性能，从而实现了在成本-质量和延迟-质量权衡上的帕累托最优。

### Q4: 论文做了哪些实验？

论文在KARLBench基准上进行了全面的实验，该基准包含六个异构的搜索任务：BrowseComp-Plus（约束驱动实体搜索）、TREC-Biogen（跨文档报告合成）、FinanceBench（长文档遍历与表格数值推理）、QAMPARI（百科全书式穷举实体搜索）、FreshStack（技术文档过程推理）和PMBench（内部企业笔记事实聚合）。实验设置上，为控制变量并专注于评估检索与推理能力，所有任务均限制代理仅使用向量搜索工具，并尽可能保留原始文档结构和分块，避免针对特定数据集的预处理优化。

主要对比方法包括顶尖闭源模型Claude 4.6和GPT 5.2。实验结果显示，KARL在成本-质量和延迟-质量的权衡上实现了帕累托最优，包括在训练时分布外的任务上。关键数据指标方面，在测试时计算（TTC）增强策略下，KARL性能进一步提升。论文探索了两种TTC策略：1）并行思考（Parallel Thinking），即模型并行生成N个独立轨迹并聚合答案，实验发现该通用策略能全面提升性能，例如在PMBench任务上，使用5个并行轨迹时，有23.7%的情况聚合器能生成优于所有单个轨迹的答案；2）价值引导搜索（Value-Guided Search, VGS），该方法训练一个基于奖励信号的小型价值模型（使用Qwen3-4B）来指导并行树搜索，通过选择预测价值最高的候选步骤进行推理。实验表明，通过增加并行搜索数量N来扩展测试时计算，能有效提升模型表现，在足够测试计算资源下，KARL超越了最强的闭源模型。这些结果验证了其提出的合成数据管道与多任务强化学习后训练范式的有效性。

### Q5: 有什么可以进一步探索的点？

基于论文内容，可以进一步探索的点包括：首先，论文提出的并行思维和价值引导搜索等测试时计算策略虽然有效，但主要依赖并行计算以控制延迟，未来可研究更高效的序列化推理方法，例如通过动态规划或蒙特卡洛树搜索来平衡性能与成本。其次，价值模型的训练目前基于二元奖励信号，未来可探索更细粒度的奖励设计，如分步奖励或基于人类反馈的强化学习，以提升搜索过程的精确性。此外，论文中的多任务训练虽展示了良好的泛化能力，但未深入探讨不同搜索机制间的知识迁移机制，未来可研究如何通过元学习或课程学习进一步优化跨任务泛化。最后，合成数据生成管道虽能自举高质量数据，但其多样性和真实性仍有提升空间，可结合真实用户交互数据或对抗性生成方法来增强数据的覆盖范围和可靠性。

### Q6: 总结一下论文的主要内容

该论文提出了一种通过强化学习训练企业搜索智能体（KARL）的系统，旨在解决基于外部知识的“落地推理”任务。核心贡献包括：第一，构建了KARLBench评估套件，涵盖约束驱动实体搜索、跨文档报告合成、表格数值推理等六种异构搜索任务，以全面评估智能体的多能力。第二，提出了一种智能体合成管道，通过长程推理和工具使用动态生成多样化、高质量且基于检索证据的训练数据，并利用能力提升的模型进行迭代自举。第三，设计了一种基于迭代大批量离策略强化学习（OAPL）的后训练范式，该方法样本高效、对训练-推理引擎差异鲁棒，并能自然扩展到多任务训练，实现分布外泛化。实验表明，在KARLBench上，KARL在成本-质量和延迟-质量的权衡中均达到帕累托最优，性能优于Claude 4.6和GPT 5.2等模型，甚至在训练分布外的任务上也能泛化。结论指出，结合定制化合成数据与多任务强化学习，能够高效训练出在多样化落地推理任务上表现优异的低成本知识智能体。
