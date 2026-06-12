---
title: "Reward Modeling for Multi-Agent Orchestration"
authors:
  - "King Yeung Tsang"
  - "Zihao Zhao"
  - "Vishal Venkataramani"
  - "Haizhou Shi"
  - "Zixuan Ke"
  - "Semih Yavuz"
  - "Shafiq Joty"
  - "Hao Wang"
date: "2026-06-11"
arxiv_id: "2606.13598"
arxiv_url: "https://arxiv.org/abs/2606.13598"
pdf_url: "https://arxiv.org/pdf/2606.13598v1"
github_url: "https://github.com/Wang-ML-Lab/OrchRM"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
  - "cs.MA"
tags:
  - "Multi-Agent Systems"
  - "Reward Modeling"
  - "Orchestration"
  - "Self-Supervised Learning"
  - "LLM"
  - "Test-Time Scaling"
relevance_score: 9.5
---

# Reward Modeling for Multi-Agent Orchestration

## 原始摘要

Multi-Agent Systems (MAS) built on Large Language Models (LLMs) require effective orchestration to coordinate specialized agents, yet training such orchestrators is hindered by limited supervision and high computational cost. We propose Orchestration Reward Modeling (OrchRM), a self-supervised framework for evaluating orchestration quality without human annotations. OrchRM leverages intermediate artifacts from multi-agent executions to construct win-lose pairs for Bradley-Terry reward model training. Unlike existing MAS test-time scaling and orchestrator training frameworks that rely on costly sub-agent rollouts, OrchRM operates directly at the orchestration level, enabling efficient and high-performing reward-guided orchestrator training and MAS test-time scaling. OrchRM improves training efficiency by up to 10x in token usage while improving MAS test-time scaling performance by up to 8% in accuracy. These gains consistently transfer across multiple domains, including mathematical reasoning, web-based question answering, and multi-hop reasoning, demonstrating orchestration-level reward modeling as a scalable direction for robust multi-agent orchestration. Code will be available at https://github.com/Wang-ML-Lab/OrchRM.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

随着大语言模型（LLM）驱动的多智能体系统（MAS）在复杂任务中展现出潜力，自动编排（orchestration）成为协调专业智能体的关键。然而，现有方法面临两大核心挑战：一是训练编排器需要大量高质量人工标注，由于编排策略、任务类型和子智能体能力之间高度耦合，人工标注不仅成本高昂且难以获取；二是训练过程计算开销极大，例如MAS-Orchestra框架采用GRPO训练，仅100步更新就消耗超过10亿token，这源于多智能体工作流的复杂性和完整子智能体 rollout 带来的累积方差。

针对上述问题，本文提出编排奖励建模（OrchRM）框架。核心思路是绕过昂贵的人工标注，利用多智能体执行过程中产生的中间产物（如模型检查点和生成轨迹），通过多维度分组策略自动构建获胜-失败对，训练 Bradley-Terry 奖励模型来评估编排质量。与现有依赖子智能体 rollout 的测试时扩展和训练方法不同，OrchRM 直接在编排层面操作，实现了高效且高性能的奖励引导式编排器训练及MAS测试时扩展。实验表明，该方法在token使用上实现了最高10倍的训练效率提升，在数学推理、网页问答等多领域测试时扩展精度提升达8%。

### Q2: 有哪些相关研究？

1. **LLM-based多智能体系统**：相关工作包括MAS-Orchestra，它通过将智能体协调建模为函数调用强化学习问题实现了高效的训练时编排，但其依赖稀疏的最终答案奖励，需要执行完整的多智能体展开才能获得反馈，计算开销大。本文提出的OrchRM通过利用中间训练产物构建自监督奖励模型，无需完整子智能体执行即可直接评估编排计划，训练效率提升达10倍。

2. **奖励建模**：传统单智能体奖励模型（如基于Bradley-Terry优化的PILAF）无法处理多智能体系统中动态的角色和对话轮次带来的信用分配问题。近期方法如MARTI和OrchMAS虽然针对协作MAS设计了奖励机制，但它们依赖静态外部预言机或确定性计算结果，无法自动从分布式展开中构建偏好对。OrchRM的创新在于能从中间模型检查点原生提取赢-输对，训练一个独立的奖励模型，为训练时编排提供可扩展的评估信号，填补了自动构建偏好对的空白。

### Q3: 论文如何解决这个问题？

论文提出Orchestration Reward Modeling (OrchRM)框架，核心创新在于将奖励建模从完整的MAS执行轨迹层面提升到编排层面，直接对编排方案进行评估，无需人工标注和完整子代理执行。

整体框架包含三个主要模块：**数据构建**、**奖励模型训练**和**下游应用**。在数据构建上，OrchRM利用现成的MAS编排器训练过程中产生的中间产物，自动构造两种偏好对：(1) **专业化优于基础**：比较训练好的编排器与基础模型生成的编排轨迹；(2) **正确优于错误**：根据最终答案正确性对同一编排器的采样轨迹进行标注。两类数据以3:1比例混合训练。

奖励模型采用Bradley-Terry目标函数进行训练：$\mathcal{L}_{OrchRM}(\phi) = -\mathbb{E}_{\mathcal{D}}[\log \sigma(r_\phi(x, z_w) - r_\phi(x, z_l))]$，其中$z$表示编排而非完整执行轨迹。

在**应用层面**，OrchRM支持两种场景：(1) **测试时扩展**：通过奖励模型从$N$个并行的编排方案中选出最优$z^* = \arg\max_{z \in Z} \{r_\phi(x, z)\}$，仅对选中的编排执行完整子代理推理，避免昂贵的子代理重复执行；(2) **编排器训练**：使用GRPO算法，以奖励模型分数作为监督信号计算优势函数$A_n = r_\phi(x, z_n) - \frac{1}{N}\sum_{j=1}^N r_\phi(x, z_j)$，在编排级别提供密集反馈，无需完整轨迹展开。

技术关键点在于：奖励模型仅在编排层面运作，直接评估高层计划质量，实现10倍令牌效率提升和8%准确率增益。

### Q4: 论文做了哪些实验？

论文进行了广泛的实验。实验设置上，以Qwen2.5-7B-Instruct为编排策略，GPT-OSS-120B为子智能体骨干模型，从Skywork-Reward-LLaMA-3.1-8B初始化编排级奖励模型进行微调。基准测试采用AIME 24&25（数学推理）、BrowseComp（基于网页的问答）和HotpotQA（多跳推理），并额外使用GPQA评估跨领域鲁棒性。

对比方法方面，测试时扩展基线包括GPT-4.1-mini等LLM-as-a-Judge方法、log概率和多种Skywork-Reward模型等奖励信号，以及无奖励模型、Pass@N和多数投票。编排器训练基线包括拒绝采样微调（RFT）和基于完整轨迹正确性的GRPO，以及使用GPT-5-mini作为奖励信号的编排级训练和DPO。

主要结果：在Best-of-8测试时扩展中，OrchRM在AIME上达到68.33%准确率（使用2.38M令牌，优于所有编排级方法），在BrowseComp上达14.00%，HotpotQA上42.50%，显著优于GPT-5-mini编排级方法（AIME 65.00%，BrowseComp 10.50%，HotpotQA 40.50%）。训练效率提升高达10倍令牌使用量，测试时扩展准确率提升达8%。消融实验显示3:1的“专用-基础”与“正确-错误”数据混合比效果最佳。这些收益在数学推理、网页问答和多跳推理等多个领域一致迁移。

### Q5: 有什么可以进一步探索的点？

论文提出的OrchRM框架虽在效率上取得突破，但仍存在若干值得深化的方向。首先，其奖励模型基于中间产物构建胜负对，可能忽视了最终输出与过程质量的非线性关联，未来可引入对比学习或逆强化学习来捕捉更复杂的偏好信号。其次，当前方法依赖固定agent配置，未考虑动态任务中agent角色或知识库的实时调整，可探索在线自适应奖励建模，结合强化学习中的经验回放机制。此外，跨领域泛化性尚存不足，例如在需要多模态交互的医疗诊断或具身推理场景中，中间产物的语义一致性更难保证。改进思路包括：设计层次化奖励结构，融合局部（子任务）与全局（最终结果）反馈；利用大模型蒸馏知识辅助奖励模型初始化，减少冷启动偏差；或引入因果推断中的反事实推理，增强对异质agent协作模式的鲁棒性。

### Q6: 总结一下论文的主要内容

该论文提出Orchestration Reward Modeling (OrchRM)框架，旨在解决基于LLM的多智能体系统中编排器训练面临监督不足、计算成本高的问题。现有方法依赖大量人工标注或昂贵子智能体交互，而OrchRM采用自监督方式，通过收集多智能体执行过程中的中间产物（如模型检查点与轨迹）构建胜负对，训练Bradley-Terry奖赏模型来评估编排质量。该方法可在编排层级运行，避免子智能体重复交互，使训练token消耗效率提升高达10倍，同时测试时扩展的准确率提高8%。实验覆盖数学推理、基于Web的问答和多跳推理等多个领域，证明OrchRM在推理时能选出优于多数投票的轨迹，在训练时能有效指导编排器持续优化甚至从零开始训练逼近教师模型性能。该工作为多智能体编排提供了一种可扩展的奖赏建模方案，兼顾高效训练与稳健测试时扩展。
