---
title: "Benchmarking the Limits of In-Context Reinforcement Learning for Ad-Hoc Teamwork"
authors:
  - "Yuheng Jing"
  - "Kai Li"
  - "Ziwen Zhang"
  - "Jiajun Zhang"
  - "Zeyao Ma"
  - "Jiaxi Yang"
  - "Lei Zhang"
  - "Zhe Wu"
  - "Jinmin He"
  - "Junliang Xing"
  - "Jian Cheng"
date: "2026-05-23"
arxiv_id: "2605.24423"
arxiv_url: "https://arxiv.org/abs/2605.24423"
pdf_url: "https://arxiv.org/pdf/2605.24423v1"
categories:
  - "cs.AI"
tags:
  - "In-Context Reinforcement Learning"
  - "Ad-Hoc Teamwork"
  - "LLM/VLM Agent"
  - "多智能体协作"
  - "环境交互 Agent"
  - "Agent 评测基准"
  - "算法蒸馏"
  - "决策预训练 Transformer"
relevance_score: 9.0
---

# Benchmarking the Limits of In-Context Reinforcement Learning for Ad-Hoc Teamwork

## 原始摘要

In-Context Reinforcement Learning (ICRL) has enabled foundation agents to adapt instantaneously to novel tasks, yet its efficacy in Ad-Hoc Teamwork (AHT)-where coordination with unknown partners is required-remains unexplored. To rigorously evaluate this, we introduce a large-scale benchmark ICRL4AHT, built upon a high-throughput JAX implementation of Overcooked-V2. Our benchmark includes a large, diverse teammate suite spanning both RL and heuristic policies, enabling controlled train-test shifts, and provides a reproducible end-to-end pipeline for teammate generation, learning-history collection, dataset construction, and online multi-episode evaluation. We evaluate representative history-conditioned ICRL algorithms, including Algorithm Distillation (AD) and Decision-Pretrained Transformer (DPT), across millions of transitions. Results reveal notable limitations: contrary to their success in single-agent domains, these baselines fail to exhibit robust test-time adaptation in multi-agent settings. Specifically, these methods frequently underperform random baselines across both unseen teammate and unseen layout tracks, with no clear in-context improvement over long horizons. These findings highlight the challenges of strategic inference under partial observability within the OvercookedV2 AHT protocol, establishing our benchmark as a critical testbed for next-generation coordination algorithms.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在系统性地评估现有序列模型驱动的上下文强化学习（In-Context Reinforcement Learning, ICRL）方法在临时团队合作（Ad-Hoc Teamwork, AHT）场景中的极限。研究背景方面，ICRL通过将交互历史作为序列模型的提示，实现了无需梯度更新的快速适应，在单智能体领域取得了突破。然而，现实部署中智能体需要与未知的、异构的合作伙伴进行实时协调，这正是AHT研究的核心挑战。现有工作的不足在于：一方面，多智能体领域缺乏像单智能体领域那样具备大规模量级（百万级转换）和战略多样性的标准化基准测试；另一方面，已有的AHT基准测试通常使用同质或少量合作伙伴，无法施加严苛的分布偏移来检验真正的泛化能力，导致观察到的性能混淆了任务能力和对特定合作伙伴的过拟合。为填补这一空白，本文提出了大规模基准测试ICRL4AHT，通过高吞吐量的OvercookedV2实现，构建了涵盖多种强化学习策略和启发式策略的多样化队友库，并设计了“队友泛化”和“布局泛化”两个评估轨道。其要解决的核心问题是：验证当前代表性的ICRL算法（如AD和DPT）是否能在多智能体AHT设定下，面对不可见的合作伙伴和布局时展现出稳健的测试时在线适应能力，还是说它们会因战略推理的不足而失败，从而揭示ICRL在协作场景中的根本性局限。

### Q2: 有哪些相关研究？

相关研究主要可分为三类。在ICRL方法类中，核心基线包括Algorithm Distillation（AD）和Decision-Pretrained Transformer（DPT）。AD通过按回报递增顺序排列多轮历史轨迹来诱导上下文学习，而DPT则基于贝叶斯推理近似，利用专家动作监督的上下文进行任务推断。本文发现这两种方法在单智能体任务中表现优异，但在AHT场景下难以鲁棒适应未知队友，经常低于随机基线，揭示了多智能体ICRL的独特挑战。在AHT方法类中，主流范式包括多样性种群学习、伙伴建模、域随机化和质量-多样性训练，本文通过将AHT重新定义为基于交互历史的上下文适应而非重新训练，并构建标准化在线评估协议，与这些工作形成鲜明区别。在评测基准类中，现有工作如Overcooked-AI、Hanabi、Melting Pot 2.0等虽支持AHT评估，但普遍缺乏可控队友多样性、混淆队友与环境泛化、或未提供标准化的学习历史数据集。ICRL4AHT通过提供包含可重复队友池、解耦的队友和布局泛化轨道、以及端到端ICRL评测管线，填补了这一空白。

### Q3: 论文如何解决这个问题？

该论文通过构建一个大规模基准测试框架ICRL4AHT来解决临时团队协作中的上下文强化学习评估问题。核心方法包括三个关键阶段：首先是规范说明与队友生成，通过版本控制的JSONL清单精确定义评估方案、布局配置和队友策略分配，确保跨不同计算环境的可重复性；队友库涵盖RL训练策略（如FCP、BRDiv等）和启发式策略（按协作性从H1到H4排序），形成从低到高不同协作难度的行为谱系。其次是高通量数据收集与存储，采用JAX原生并行rollout引擎生成超过11.9亿条转换数据，通过轨迹过滤筛选高质量学习历史（约1.5亿条），并以分块HDF5格式序列化存储，配合JSON索引实现高效元数据查找。最后是标准化ICRL训练与评估，支持AD和DPT等算法，通过上下文窗口采样分析适应能力，并设计两个评估方案：队友泛化（在熟悉环境中应对未见过的队友）和布局泛化（同时面对新环境和新队友）。

在架构设计上，论文将对手策略视为环境的内在组成部分，通过定义有效转移动力学来隔离单边上下文适应的挑战。创新点包括：首次将ICRL应用于临时团队协作场景、构建包含80个独特队友的大规模多样化队友套件、实现端到端的可复现评估流程、并通过严格的分布偏移测试揭示了现有方法在多智能体环境中适应能力的局限性。

### Q4: 论文做了哪些实验？

论文在 ICRL4AHT 基准上进行了两个核心实验。**实验设置**基于JAX加速的Overcooked-V2，使用包含RL和启发式策略的多样化队友池（H1-H4），并设计了可控的训练-测试分布偏移。**Track 1（队友泛化）**：在6个训练布局上训练模型，测试时面对未见过的启发式队友。**Track 2（布局+队友联合泛化）**：在未见过的布局（如`asymm adv right`和`cramped down`）上测试，队友同样未见。**对比方法**包括Algorithm Distillation (AD)、Decision-Pretrained Transformer (DPT)和随机基线（Rnd）。**主要结果**显示：Track 1中，AD和DPT的在线适应曲线呈平坦状，未见上下文学习带来的提升；Track 2中，随机基线在多个设置下匹配或超越ICRL方法。例如，在`asymm adv right`布局上，DPT平均得分为13.2，仅略高于随机基线的11.7，而AD仅得4.4；在`cramped down`布局上，随机基线平均4.3，显著高于AD的0.8和DPT的0.6。**消融实验**进一步显示，将队友动作作为条件输入（+TA）未能解决核心缺陷，如在`test wide`布局上，AD+TA对H1的得分从-18.0提升至-2.2，但仍远低于随机基线的0.0。这些结果表明当前ICRL方法在多智能体临时团队协作中存在严重局限性。

### Q5: 有什么可以进一步探索的点？

论文揭示了当前ICRL方法在AHT任务中的严重缺陷：AD和DPT在未见过的队友和布局上表现甚至不及随机基线，且长序列未见上下文学习改善。这一发现表明现有历史条件策略无法有效从交互历史中提取队友的意图和策略模式。未来可探索的方向包括：1）设计更有效的队友建模机制，例如引入显式的信念状态或递归推理模块，让agent能在线更新对队友策略的估计；2）结合元学习或探索奖励，在ICRL训练框架中注入主动信息获取的激励，而非仅依赖被动观察；3）改进回放缓冲区的采样策略，使经验更集中于关键交互边界或策略切换点；4）尝试多智能体视角下的联合训练范式，让ICRL agent在训练时与不同类型队友交互，并利用反事实推理解耦自身与队友贡献。此外，可引入分层架构，让高层选择交互策略，低层执行动作，以缓解部分可观测性带来的策略不确定性。

### Q6: 总结一下论文的主要内容

本文针对多智能体协作中的临时团队合作（AHT）问题，首次系统评估上下文强化学习（ICRL）方法的泛化极限。当前ICRL在单智能体领域表现优异，但其对未知伙伴的协调能力尚未验证。为此，论文提出了大规模基准ICRL4AHT，基于JAX实现的OvercookedV2平台构建高效数据处理流水线，包含由强化学习与启发式策略组成的多样化队友库，并设计队友泛化与布局泛化两条严格评估轨道。实验使用算法蒸馏和决策预训练Transformer等主流ICRL方法，在数百万状态转移数据上训练与测试。核心发现如下：这些方法不仅在不同队友与布局场景下频繁低于随机基线，且在长时间交互过程中未观察到预期的上下文学习曲线提升。研究表明现有序列化ICRL模型在部分可观测环境下难以进行有效的策略推理与伙伴自适应。该基准为下一代协作算法提供了关键测试平台，揭示了AHT场景下ICRL面临的本质性挑战。
