---
title: "Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning"
authors:
  - "Yanxi Chen"
  - "Weijie Shi"
  - "Yuexiang Xie"
  - "Boyi Hu"
  - "Yaliang Li"
  - "Bolin Ding"
  - "Jingren Zhou"
date: "2026-06-18"
arxiv_id: "2606.20002"
arxiv_url: "https://arxiv.org/abs/2606.20002"
pdf_url: "https://arxiv.org/pdf/2606.20002v1"
github_url: "https://github.com/agentscope-ai/Trinity-RFT"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "强化学习"
  - "长周期Agent"
  - "跨域泛化"
  - "环境学习"
  - "Agent训练框架"
  - "GRPO"
relevance_score: 9.0
---

# Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning

## 原始摘要

This work presents a general framework for training large language models (LLMs) to "Connect the Dots" (CoD), a meta-capability required by long-lifecycle agents: as an LLM-based AI agent gets deployed in an environment, it solves a long sequence of tasks while continuously exploring the environment, learning from its own experiences, and iteratively self-updating its context about the environment, thereby achieving progressively better performance on future tasks conditioned on the updated context. Major components of the CoD framework include: (1) algorithm design and infrastructure for end-to-end reinforcement learning (RL) with long rollout sequences interleaving solve-task and update-context episodes; (2) tasks and environments for incentivizing and eliciting the targeted meta-capability in LLMs during training, as well as for faithfully measuring progress during evaluation. We present proof-of-concept implementations of the CoD framework, including a GRPO-style RL algorithm with fine-grained credit assignment, as well as tasks and environments tailored to the targeted meta-capability (rather than domain-specific LLM capabilities or standard task-by-task RL). Empirical results validate the efficacy of end-to-end RL training in the CoD setting, and demonstrate the potential for out-of-distribution generalization -- within the training domains, across different domains, and from CoD to Ralph-loop settings -- of the elicited meta-capability. Our investigation of CoD connects several lines of prior works, and opens up new opportunities for advancing LLMs and AI agents. To facilitate further research and applications, we release our implementations at \url{https://github.com/agentscope-ai/Trinity-RFT/tree/research/cod/examples/research_cod}.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何训练大语言模型（LLM）获得"连点成线"（CoD）这一元能力的问题。在现实应用中，AI agent需要长期部署在环境中，连续解决一系列不同但相关的任务，同时主动探索环境、从自身经验中学习并迭代更新对环境上下文的认知，从而在后续任务中取得更好表现。然而，当前的前沿LLM在这一元能力上存在明显不足：它们容易在欠规范的环境中迷失方向，往往需要人工设计的复杂代理脚手架才能稳定运行较长时间。现有方法中，标准按任务训练的强化学习（RL）本质上是让LLM从零开始逐个解决每个任务，这与长期部署所需的CoD元能力不匹配。因此，本文的核心问题是如何设计专门的端到端强化学习训练框架，使LLM在长序列的"求解任务"与"更新上下文"交替的交互过程中，学会主动探索环境并自我更新上下文，从而在未来任务中表现更好。

### Q2: 有哪些相关研究？

相关问题研究可分为三类。首先是**长期智能体（Lifelong Agent）研究**，如Hermes-Agent等框架通过记忆库或技能库实现环境适应，但现有工作缺乏对智能体元能力的专用后训练，往往依赖人工设计的复杂组件，且前沿LLM在非确定性环境中表现欠佳。本文提出的CoD框架通过端到端RL训练，使LLM同时掌握任务求解与上下文自更新能力，区别于仅优化上下文或仅更新模型权重的现有方法。

其次是**元强化学习（Meta RL）**，特别与RL²范式相关。关键区别在于：LLM比循环神经网络具有更强的计算表达能力和跨域泛化潜力。类似工作如LaMer、MAGE和Orbit采用不同RL算法，但存在共同局限——假设重复环境状态可识别或使用粗粒度信用分配。CoD通过细粒度信用分配的GRPO风格RL算法，克服了这些限制，可有效训练更长的动作序列。

第三是**LLM推理扩展（Inference Scaling）**，如Ralph循环等测试时推理方法。CoD部署可视为推理扩展的特例（任务序列为同一任务重复），但现有方法在训练时移除反射或技能等额外上下文，而CoD明确训练LLM基于持续更新的上下文适应新环境。

### Q3: 论文如何解决这个问题？

论文通过提出“Connect the Dots”（CoD）框架解决长生命周期智能体在跨域泛化中的元能力训练问题。核心方法基于端到端强化学习（RL），设计了独特的trajectory结构：每个训练轨迹交替包含“解决任务”（solve-task）和“更新上下文”（update-context）两种episode，模拟智能体在环境中连续学习的过程——先执行任务积累经验，再主动压缩并更新上下文信息（如环境映射、探索策略），从而在后续任务中取得更好表现。

在架构上，采用GRPO-style算法并改进credit assignment：通过动态规划思想，将每个episode的return定义为当前奖励与未来solve-task奖励的均值，同时基于同位置episode组进行advantage计算，配合自适应样本加权缓解训练不稳定。为支持长序列RL，基于Trinity框架构建模块化基础设施，定义环境级元工作流，支持灵活插入不同任务。关键技术包括：设计专用环境（如FrozenLake with Obscurity和Alchemy with Random Mappings）驱动元能力——环境设置随机化的映射规则或配方，迫使智能体仅能通过跨episode自探索积累上下文信息，以此诱导出“连接点”的元能力。实验表明，CoD训练后的模型不仅能在更难场景和更长任务序列中提升性能，还能零样本泛化到未见领域（如Terminal任务）和Ralph-loop重复求解场景，验证了端到端RL对元能力的有效激发和跨域泛化潜力。

### Q4: 论文做了哪些实验？

论文设计了三个实验环境：FrozenLake with Obscurity (FLObs)、Alchemy with Randomness (AlchRand) 和 Terminal。实验采用两种训练设置：设置A仅在FLObs域训练，设置B在FLObs和AlchRand混合域训练，均使用Qwen-8B模型和GRPO风格的强化学习算法，任务序列长度为4。评估时，模型在更难的域内实例（更大地图/更多元素）和更长的任务序列（长度8）上测试域内泛化，同时在未见过的域（如Terminal）和Ralph-loop设置上测试跨域泛化。主要结果包括：在设置A中，FLObs训练奖励从位置0的0.18增长至0.45，位置3的0.28增长至0.76，且域内评估表现类似；同时，在AlchRand和Terminal的Ralph-loop设置中观察到跨域性能提升，如Terminal的Ralph-loop评估中后期 episodes 获得更高奖励。设置B的结果与A相似，但AlchRand训练稳定性稍差。实验验证了端到端RL训练在CoD框架下的有效性，并展示了该元能力在域内、跨域及Ralph-loop设置中的分布外泛化潜力。

### Q5: 有什么可以进一步探索的点？

论文在连接长生命周期AI代理所需元能力方面展示了前景，但仍存在显著局限性。当前GRPO风格RL算法依赖启发式增强，缺乏理论严谨性，未来可探索更严格的信用分配机制（如基于值函数的梯度估计）以提升稳定性。环境多样性不足（仅Flobs和Alchrand），需设计包含非平稳动态、长期依赖的复杂场景（如持续变化的任务分布或部分可观测环境）。现有上下文管理仅支持简单重写“提示”，可扩展至记忆衰减机制或结构化知识图谱，并引入分层滚动模式（如局部探索与全局策略更新交替）。此外，与现有LLM后训练流水线（如指令微调、领域特定RL）的整合是开放问题，建议通过两阶段训练或模型蒸馏实现元能力与专用能力的协同泛化。未来还需验证超长序列（如千轮交互）下的计算效率与灾难性遗忘风险，以及多模态感知等更实际的应用场景。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个用于训练大语言模型元能力“Connect the Dots (CoD)”的通用框架，旨在使AI智能体在长期部署中能主动探索环境、积累经验并更新上下文，从而持续提升未来任务表现。核心问题是在长周期任务序列中，智能体需在求解任务与自我更新上下文之间穿插执行。方法上，论文设计了一种端到端强化学习框架，采用类似GRPO的算法并实现细粒度信用分配，同时构造了特定的任务与环境来激励和评估该元能力。实验结果表明，端到端强化学习能有效激发CoD能力，例如在任务成功率上从28%显著提升至76%，并展现出在训练域内、跨域以及向Ralph-loop设置的泛化潜力。该工作的贡献在于将CoD视为通用元能力进行系统训练，连接了终身智能体、元强化学习等多项前期工作，为提升LLM智能体的长期自主性和环境适应性提供了新路径。
