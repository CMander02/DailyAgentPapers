---
title: "EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents"
authors:
  - "Weixian Xu"
  - "Shilong Liu"
  - "Mengdi Wang"
date: "2026-06-09"
arxiv_id: "2606.11182"
arxiv_url: "https://arxiv.org/abs/2606.11182"
pdf_url: "https://arxiv.org/pdf/2606.11182v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "test-time prompt learning"
  - "LLM agent"
  - "self-improving agents"
  - "multi-dataset"
  - "router-prompt co-evolution"
  - "cross-dataset interference"
relevance_score: 8.5
---

# EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents

## 原始摘要

In this paper, we propose EEVEE, the first multi-dataset test-time prompt learning framework for LLM agents, enabling test-time prompt learning under real-world task streams. Existing methods are largely designed for single-dataset settings, while real-world applications require models to handle heterogeneous input streams drawn from multiple datasets, domains, and task distributions, limiting their practical applicability. To mitigate cross-dataset interference, EEVEE introduces a router that partitions incoming inputs into task clusters and assigns them to suitable prompt configurations. This design is optimized via a router-prompt co-evolution strategy, which employs interleaved router and prompt learning phases to address their mutual dependency. Experiments across multiple datasets demonstrate that the framework improves robustness under heterogeneous data streams while maintaining single-benchmark learning capability and efficiency. Specifically, EEVEE improves average multi-benchmark scores by 10.38 and 24.32 points over Qwen3-4B-Instruct and DeepSeek-V3.2, surpassing SOTA methods GEPA and ACE by up to 37.2% and 48.2%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有测试时提示学习方法在真实多数据集场景下适应性不足的问题。研究背景是，测试时提示学习作为一种轻量级适配机制，能通过在线更新提示词来提升大语言模型在部署后的表现，尤其适用于自我改进型智能体。然而，现有方法（如GEPA、ACE）大多设计用于单一数据集或基准测试，忽略了真实世界中输入流往往来自多个不同领域、任务格式和能力分布这一事实。这导致一个核心问题：跨数据集干扰。当处理来自不同领域的混合输入流时，基于单一提示词的更新会对之前学习过的其他领域任务产生负面影响，造成灾难性遗忘和性能退化。本文提出EEVEE，第一个面向多数据集测试时提示学习的框架。其核心思路是引入一个路由模块，将输入流智能地划分为不同的任务簇，并为每个簇分配专属的提示配置。为了解决路由器和提示学习相互依赖的困境（路由影响提示学习样本，提示性能反馈路由策略），EEVEE还设计了路由-提示协同进化策略，通过三个阶段的训练过程实现两者联合优化，从而在保持模型效率的同时，显著提升在异构数据流下的鲁棒性和多任务保留能力。

### Q2: 有哪些相关研究？

相关研究主要分为两个方向。在提示学习方面，现有方法如GEPA使用自然语言反思和帕累托前沿选择，ACE将上下文视为自适应剧本，Combee通过并行轨迹聚合扩展提示学习；但这些方法都针对单数据集或单任务分布优化。在自我改进智能体方面，Self-Refine和Reflexion利用自然语言反馈或语言记忆，Voyager维护长期记忆或技能库，进化发现智能体应用于科学搜索并支持协同进化。本文EEVEE与上述工作的核心区别在于：1）现有提示学习方法（GEPA/ACE/Combee）均不支持多数据集混合流，而EEVEE通过路由器将输入划分为任务集群并分配不同提示配置；2）不同于反射型智能体和进化发现智能体仅优化限定程序，EEVEE首次实现了路由器与提示的协同进化机制；3）对比GEPA/ACE等单数据集适配方法，EEVEE在多基准混合流场景下的性能提升达37.2%和48.2%。

### Q3: 论文如何解决这个问题？

EEVEE提出了一种多数据集测试时提示学习框架，核心方法是通过路由-提示协同演化（Router-Prompt Co-Evolution）解决真实世界任务流中的跨数据集干扰问题。整体框架包括三个主要阶段：初始化、探索和收敛。

初始化阶段首先对混合训练集进行提示学习，构建一个帕累托前沿池（Pareto-front pool），通过基于覆盖度的贪婪选择算法，挑选出行为可区分的专业化提示集合，为后续路由学习提供可用的行为基础。

探索阶段交替进行路由演化和提示演化。路由演化固定当前提示集，通过变异（mutation）、分析、反思（reflection）和评分机制搜索更好的路由策略。路由评分综合考虑下游准确率、一致性和平衡性三个指标，并采用退火机制，早期侧重多样性和平衡性，后期侧重准确率。提示演化为每个路由槽位独立优化专用提示，同样使用变异和反思，并通过帕累托前沿池保留多样化且有效的提示。两者交替优化，解决路由与提示之间的相互依赖问题。

收敛阶段在路由策略稳定后，固定最优路由，重新分配数据，并在每个槽位投入更大的预算进行提示优化，从而在稳定分区下获得强提示。

关键技术包括：基于正确性向量的行为感知路由评分函数、帕累托前沿池维护多样化提示、以及三阶段训练策略（初始化-探索-收敛）以平衡效率和鲁棒性。

### Q4: 论文做了哪些实验？

论文在多数据集测试时提示学习设置下进行了实验，采用四个基准测试：GPQA Diamond（闭卷知识问答）、Formula（数学推理）、TheoremQA（符号推理）和HumanEval（代码生成）。实验设置从混合训练流中学习，在留出测试样本上评分，并报告三次运行的平均值。对比方法包括未适应的目标模型基线、GEPA和ACE。主要结果：在Qwen3-4B-Instruct上，EEVEE平均得分为51.75，比基线提升10.38分，超过GEPA（14.02分）和ACE（16.83分）；在DeepSeek-V3.2上，EEVEE平均得分64.07，比基线提升24.32分，超过GEPA（8.24分）。消融实验表明，完整方法比默认路由器（43.58）、手动路由器（37.18）和无共进化变体（42.88）分别高出8.17、14.57和8.87分。在单基准测试中，EEVEE与GEPA和ACE竞争力相当；随着任务混合增加，GEPA和ACE保留率下降至负值，而EEVEE保持正累积保留率+41.53。跨模型泛化中，Qwen3学到的提示将DeepSeek-V3.2平均分从39.75提升至54.10；跨任务泛化中，EEVEE在MBPP上提升至70.42，优于GEPA和ACE。令牌成本方面，EEVEE平均使用4.32k总令牌，低于ACE的21.30k。诊断测试显示，代码和公式任务提升显著，而GPQA Diamond出现轻微下降。

### Q5: 有什么可以进一步探索的点？

论文的主要局限在于：1) 随机搜索导致性能无法精确复现；2) 依赖真实标签或规则标签，尚未实现纯反思式学习；3) 需要预准备适应集而非完全在线流。未来可探索以下方向：第一，引入确定性进化策略或对比学习机制，减少随机性对复现的影响。第二，开发弱监督或自监督的反馈信号，如基于LLM自身一致性或任务成功率的自我评估，逐步脱离对人工标签的依赖。第三，设计动态聚类与遗忘机制，使路由器能处理长期非平稳分布漂移。此外，可尝试将提示学习与元学习结合，使模型在异构流中快速适应未见任务分布。改进思路包括：采用贝叶斯优化替代随机搜索以提升稳定性，以及利用检索增强生成为每类输入动态构建初始化提示，降低跨任务干扰。这些方向将推动EEVEE向真正无需标注、在线自适应的通用Agent框架演进。

### Q6: 总结一下论文的主要内容

本文提出了EEVEE，首个面向真实世界任务流的LLM智能体多数据集测试时提示学习框架。问题定义：现有方法仅适用于单数据集设置，而真实应用需处理来自多个数据集、领域和任务分布的异构输入流，存在跨数据集干扰。方法概述：EEVEE引入路由器将输入划分为任务集群并分配适合的提示配置，通过路由器-提示协同进化策略（三阶段：初始化提示、探索耦合更新、稳定路由器下细化提示）优化相互依赖关系。主要结论：实验表明，在混合数据集场景下，EEVEE相比基线方法提升显著，多基准平均得分在Qwen3-4B-Instruct和DeepSeek-V3.2上分别提升10.38和24.32分，超越SOTA方法GEPA和ACE最高达37.2%和48.2%。该框架增强了异构数据流的鲁棒性，同时保持单基准学习能力和效率，为真实世界测试时提示学习提供了实用方法和实证视角。
