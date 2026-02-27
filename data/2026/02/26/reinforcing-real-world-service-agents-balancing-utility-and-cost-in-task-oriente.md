---
title: "Reinforcing Real-world Service Agents: Balancing Utility and Cost in Task-oriented Dialogue"
authors:
  - "Ning Gao"
  - "Wei Zhang"
  - "Yuqin Dai"
  - "Ling Shi"
  - "Ziyin Wang"
  - "Yujie Wang"
  - "Wei He"
  - "Jinpeng Wang"
  - "Chaozheng Wang"
date: "2026-02-26"
arxiv_id: "2602.22697"
arxiv_url: "https://arxiv.org/abs/2602.22697"
pdf_url: "https://arxiv.org/pdf/2602.22697v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Task-oriented Dialogue"
  - "Reinforcement Learning"
  - "Multi-turn Policy Optimization"
  - "Cost-aware Decision-making"
  - "Agent Training Framework"
  - "User Simulation"
relevance_score: 8.0
---

# Reinforcing Real-world Service Agents: Balancing Utility and Cost in Task-oriented Dialogue

## 原始摘要

The rapid evolution of Large Language Models (LLMs) has accelerated the transition from conversational chatbots to general agents. However, effectively balancing empathetic communication with budget-aware decision-making remains an open challenge. Since existing methods fail to capture these complex strategic trade-offs, we propose InteractCS-RL, a framework that reframes task-oriented dialogue as a multi-granularity reinforcement learning process. Specifically, we first establish a User-centric Interaction Framework to provide a high-fidelity training gym, enabling agents to dynamically explore diverse strategies with persona-driven users. Then, we introduce Cost-aware Multi-turn Policy Optimization (CMPO) with a hybrid advantage estimation strategy. By integrating generative process credits and employing a PID-Lagrangian cost controller, CMPO effectively guides the policy to explore Pareto boundary between user reward and global cost constraints. Extensive experiments on customized real business scenarios demonstrate that InteractCS-RL significantly outperform other baselines across three evaluation dimensions. Further evaluation on tool-agent-user interaction benchmarks verify InteractCS-RL robustness across diverse domains.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现实世界任务导向对话（TOD）系统中，智能体难以在确保任务完成效果（效用）与遵守运营成本约束之间取得平衡的核心问题。

研究背景在于，随着大语言模型（LLM）的发展，客户服务系统正从简单的意图分类转向端到端的生成式智能体。然而，现有的TOD方法主要关注于遵循固定流程完成特定任务（如订餐、订票），它们通常基于静态对话数据进行监督微调（SFT），并仅以“成功率”等单一指标进行优化。这导致了两个关键不足：首先，依赖静态数据模仿人类行为，会使模型学到并固化一些成本低效的决策（如过早妥协），而无法评估其长期最优性，难以适应需要动态策略权衡的复杂环境。其次，现有框架缺乏有效的成本建模机制，无法惩罚那些通过过度消耗资源（如不必要的补偿、冗长对话）达成的“虚假成功”，忽视了实际部署中的经济约束。

因此，本文要解决的核心问题是：如何让任务导向对话智能体在充满意外情况和情感化用户交互的真实商业场景中，不仅能专业地解决问题、维持对话质量，还能在严格的全局运营成本限制下，自主探索并学会做出成本感知的最优策略决策。论文将这一问题重新定义为一种多粒度的强化学习过程，并提出了InteractCS-RL框架来应对这一挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为任务导向对话（TOD）系统和LLM后训练优化方法两大类。

在**任务导向对话系统**方面，早期研究主要基于序列到序列建模和神经架构，并常使用用户模拟器来扩充训练数据，但其效果受限于模型本身的表示能力。随着预训练和指令对齐LLMs的出现，主流方法转向构建静态数据集进行监督微调（SFT），以使LLM适应特定场景。近期扩展工作进一步集成了外部工具、检索增强生成（RAG）和多模态输入以增强智能体能力。与这些侧重于静态数据或特定功能扩展的工作不同，本文提出的InteractCS-RL框架在一个动态环境中进行在线交互与优化，通过高保真的用户中心交互框架来模拟真实、个性化的多轮对话策略探索。

在**LLM后训练与优化方法**方面，相关研究从基础的SFT发展到人类反馈强化学习（RLHF）及其离线变体，以进行偏好对齐。近期，在数学、代码等目标明确领域，可验证奖励的强化学习（RLVR）范式受到关注；同时，群体相对策略优化（GRPO）等方法通过消除对集中式价值网络的依赖，提升了训练稳定性和内存效率。然而，这些方法在复杂的多轮TOD场景中面临两大挑战：一是稀疏奖励分配问题，现有基于步骤级或语义级采样重用的优势估计方法难以准确评估多轮对话的响应质量；二是运营约束下的优化问题，现有的安全对齐方法多采用离线优化或拉格朗日乘子，通常只关注单轮响应的成本，而非强制执行全局约束。本文提出的CMPO方法，通过引入生成过程信用分配和PID-拉格朗日成本控制器，直接针对上述挑战，旨在多轮对话中实现更有效的、考虑全局成本约束的策略优化，探索用户奖励与成本之间的帕累托边界。

### Q3: 论文如何解决这个问题？

论文通过提出InteractCS-RL框架来解决任务导向对话中平衡服务效用与运营成本的挑战。该框架包含两个核心组件：用户中心交互框架和成本感知多轮策略优化。

首先，用户中心交互框架旨在构建一个高保真、动态的训练环境，以弥补静态数据集的不足。该框架通过一个标准化的用户画像体系来模拟真实用户的心理复杂性，该体系包含内在特质和外在需求两个层次。内在特质从沟通风格、信息透露度、问题解决风格和个人情感风格四个稳定维度建模用户行为；外在需求则捕捉目标导向逻辑，分为刚性追求、偏好学习、激励开放和反馈导向四种模式。通过深度耦合这两者，并利用大语言模型作为用户模拟器，该框架能生成多样化的交互轨迹，为智能体提供探索非确定性状态空间的机会。

其次，成本感知多轮策略优化是框架的核心创新方法。它将任务解决过程建模为一个约束马尔可夫决策过程，并采用分组相对策略优化进行训练。其关键创新在于设计了一种混合优势估计策略，该策略将会话级结果、轮次级过程指导和全局成本约束统一为一个学习信号。具体而言，优势函数由三部分组成：基于最终用户满意度的结果奖励、基于生成过程信用的轮次级过程奖励，以及一个动态成本惩罚项。过程奖励通过一个生成式奖励模型来评估智能体每轮输出是否符合领域原则（如对话逻辑、同理心要求），提供细粒度指导。对于成本约束，论文采用拉格朗日乘子法将其转化为无约束对偶问题，并创新性地引入PID控制器来动态、稳定地更新惩罚系数，避免振荡和超调，从而确保策略在效用最大化和约束满足之间稳定收敛。

整体上，InteractCS-RL通过构建逼真的动态交互环境，并设计融合多粒度奖励与先进成本控制的强化学习优化机制，使智能体能够有效探索用户奖励与全局成本约束之间的帕累托边界，最终实现服务效用与运营成本的最佳平衡。

### Q4: 论文做了哪些实验？

论文实验主要围绕三个核心假设展开。实验设置方面，构建了一个高保真的外卖售后纠纷（FDS）场景作为主要评估基准，涵盖配送延迟、餐品损坏等核心纠纷类型。智能体需在多轮协商中解决用户不满，同时遵守业务合规约束，其主要成本来自优惠券补偿行为。实验使用基于Qwen2.5系列模型（如7B/14B作为客服智能体，32B用于用户模拟和奖励生成）构建的智能体，在8块A100 GPU上进行训练。对话在用户满意、明确拒绝或达到最大轮数（T_max=15）时终止。

使用的数据集/基准测试包括：1）自定义的FDS场景，其用户画像库基于真实业务数据构建，并聚类为五个合作度等级，通过调整不同等级比例设计了普通和困难两种难度设置；2）用于评估泛化能力的τ²-bench，涵盖零售、电信和航空等多个任务导向对话（TOD）领域。

对比方法包括：1）大型模型：如GPT-4.1、Deepseek-v3、LongCat-Flash、Qwen3-235B等闭源和开源模型；2）基础模型：使用精心设计业务提示的Qwen2.5-Instruct（7B和14B）；3）监督微调（SFT）模型：基于约2k条高质量业务数据进行微调；4）强化学习基线：包括PPO、GRPO和CAPO。

评估指标分为三个维度：1）任务得分：包括平均用户满意度（1-5分）和格式化对话完成率（FR）；2）对话质量：包括逻辑一致性（分数）和沟通质量（分数）；3）约束指标：优惠券发放率（Voucher Rate）。在τ²-bench上还评估了Pass@1、沟通率（Comm. Rate）、数据库调用率（DB Rate）和动作奖励（Action Reward）。

主要结果如下：在FDS困难场景中，所提方法（InteractCS-RL）将14B模型的用户满意度提升至3.05分，超越包括LongCat-Flash在内的闭源模型近40%，并实现了100%的对话完成率，优于GPT-4.1（83.8%）和DeepSeek-v3.2（89.6%）。在对话质量上，逻辑质量（11.34）和沟通质量（27.43）均为最高，较SFT模型各提升约10%。在成本控制上，该方法成功将优惠券发放率稳定在预设阈值30%附近，而其他大型模型和SFT模型均出现严重超支。在τ²-bench的跨领域泛化测试中，该方法在14B模型上平均Pass@1率较SFT基线提升5.6%，并在沟通率、数据库调用率等指标上一致优于基线，证明了其泛化能力。消融实验验证了所提CMPO及其PID-Lagrangian成本控制器、混合奖励组件的有效性，表明其能在满足成本约束的同时最大化用户效用。

### Q5: 有什么可以进一步探索的点？

该论文在平衡任务效用与成本方面取得了进展，但仍有多个方向值得深入探索。首先，其用户模拟框架虽能生成多样化策略，但可能无法完全覆盖真实人类交互的复杂性和突发性，未来可引入更动态的用户行为模型或在线人机协作学习机制来提升泛化能力。其次，PID-Lagrangian成本控制器虽能引导策略探索帕累托边界，但参数调优依赖人工经验，可研究自适应约束优化算法以动态调整权衡系数。此外，框架目前主要针对单领域任务导向对话，未来可扩展至跨领域或多模态交互场景，探索在资源受限下的通用决策能力。最后，评估维度虽涵盖三个方面，但缺乏对长期用户满意度或社会伦理影响（如隐私与公平性）的考量，后续可引入更全面的可持续性评估指标。

### Q6: 总结一下论文的主要内容

该论文针对任务导向对话中如何平衡共情沟通与运营成本的核心挑战，提出InteractCS-RL框架。其核心贡献是将任务导向对话重构为一个多粒度强化学习过程，通过用户中心交互框架模拟高保真训练环境，使智能体能与具身用户动态探索多样化策略。方法上，论文设计了成本感知多轮策略优化，结合混合优势估计策略，并引入PID-Lagrangian成本控制器，有效引导策略在用户奖励与全局成本约束之间探索帕累托边界。实验表明，该框架在定制化真实业务场景中显著优于现有基线，并在多领域工具-智能体-用户交互基准上验证了其鲁棒性，成功实现了在预算约束下提升任务得分的同时控制成本。
