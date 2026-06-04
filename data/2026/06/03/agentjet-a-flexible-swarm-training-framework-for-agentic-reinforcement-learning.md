---
title: "AgentJet: A Flexible Swarm Training Framework for Agentic Reinforcement Learning"
authors:
  - "Qingxu Fu"
  - "Boyin Liu"
  - "Shuchang Tao"
  - "Zhaoyang Liu"
  - "Bolin Ding"
date: "2026-06-03"
arxiv_id: "2606.04484"
arxiv_url: "https://arxiv.org/abs/2606.04484"
pdf_url: "https://arxiv.org/pdf/2606.04484v1"
categories:
  - "cs.AI"
  - "cs.LG"
  - "cs.MA"
tags:
  - "多智能体强化学习"
  - "分布式训练框架"
  - "异构多模型"
  - "工具学习"
  - "可扩展架构"
relevance_score: 9.5
---

# AgentJet: A Flexible Swarm Training Framework for Agentic Reinforcement Learning

## 原始摘要

We present AgentJet, a distributed swarm training framework for large language model (LLM) agent reinforcement learning. Unlike centralized frameworks that tightly couple agent rollouts with model optimization, AgentJet adopts a decoupled multi-node architecture in which swarm server nodes host trainable models and run optimization on GPU clusters, whereas swarm client nodes execute arbitrary agents on arbitrary devices. This design provides capabilities that are difficult to support in centralized frameworks: (1) heterogeneous multi-model reinforcement learning, enabling the training of heterogeneous multi-agent teams with multiple LLM as brains; (2) multi-task cocktail training with isolated agent runtimes; (3) fault-tolerant execution that prevents external environment failures from interrupting the training process; and (4) live code iteration, which allows agents to be edited during training by replacing swarm client nodes. To support efficient RL in multi-model, multi-turn, and multi-agent settings, AgentJet introduces a context tracking module with timeline merging, which consolidates redundant context and achieves a 1.5-10x training speedup. Finally, AgentJet introduces an automated research system that takes a research topic as input and autonomously conducts long-horizon, multi-day RL studies on large-scale clusters. By leveraging the swarm architecture, this system reproduces key exploratory workflows of RL researchers without human intervention during execution.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有的大语言模型（LLM）智能体强化学习训练框架在实际应用中的一系列核心局限。尽管已有通用RLHF框架（如OpenRLHF、veRL）和专用智能体RL框架（如Forge、AReaL）的出现，但它们普遍面临五个关键不足：第一，运行时脆弱性，大多数框架将智能体交互环境与模型训练耦合在同一集群中，任一外部环境（如代码沙箱、浏览器）的故障都可能导致整个训练流程崩溃并丢失进度；第二，调试困难，修改智能体代码或奖励函数需要重启整个训练流程，包括耗时的模型加载和vLLM初始化，导致5-10分钟的迭代周期；第三，多模型约束，现有系统主要优化单一策略模型，而真实应用越来越需要异构多智能体系统（例如7B模型执行、32B模型规划）；第四，冗余上下文，随着智能体与环境多轮交互，累积了大量冗余的系统提示、工具定义和观察历史，在策略梯度更新中造成计算浪费；第五，环境锁定，多任务鸡尾酒训练要求对不同任务环境进行强隔离，但单体架构难以实现。本文介绍AgentJet，通过彻底解耦智能体运行时与训练基础设施的客户端-服务器群架构，解决了上述问题。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可按以下类别组织：

1. **通用RLHF框架**：如OpenRLHF（基于Ray+vLLM的分布式架构）和veRL（HybridFlow，提出混合单控制器/多控制器编程模型）。这些框架主要用于扩展推理RL，但设计上针对单轮或短时交互，且假设训练-推理环境紧密耦合。本文的AgentJet通过完全解耦的多节点架构，支持异构多模型、多轮和长时任务中的RL训练，突破了这些限制。

2. **智能体原生RL框架**：包括Forge（MiniMax，引入中间件抽象和上下文管理）、AReaL（清华与蚂蚁集团，提出异步训练-推理解耦）、Agent Lightning（微软，将智能体经验转为状态-动作-奖励）、OpenTinker（RLaaS架构）、OpenClaw-RL（连续在线策略优化）。相比这些工作，AgentJet的优势在于：（1）全解耦的任意设备多对多拓扑；（2）异构多模型多智能体RL且无需参数共享；（3）架构级容错，客户端故障不中断训练；（4）时间线合并实现1.5-10倍加速；（5）零代码修改的黑盒智能体支持。

3. **自动化研究系统**：如AI Scientist（Sakana AI，端到端自动化研究）、AI Co-Scientist（Google DeepMind）、AI-Researcher（港大，NeurIPS 2025 Spotlight）、AgentRxiv（多智能体协作）。这些系统主要聚焦于生成论文或优化分钟级任务。AgentJet的自动化研究系统则针对一个互补且较少探索的问题：编排长时（数小时到数天）实验，通过集群调度和多阶段自适应实验设计来达成研究结论。

### Q3: 论文如何解决这个问题？

AgentJet通过解耦训练和部署平面的swarm架构解决传统集中式框架的耦合问题。整体框架包含两类独立节点：swarm server节点在GPU集群上托管模型并执行策略梯度优化，使用vLLM/SGLang推理引擎和上下文追踪模块；swarm client节点是轻量级CPU进程，可在任意设备上执行任意agent工作流、计算奖励并收集轨迹。

核心创新包括四个关键技术：第一，异构多模型强化学习，允许多个server节点同时训练不同LLM（如Qwen3-32B和Qwen3-14B），支持非共享参数的多agent团队训练；第二，多任务鸡尾酒训练，通过任务组织的样本池和5种采集策略（C1-C5）灵活控制批次组成，包括计数策略、任务计数策略、非虚拟任务计数策略、全客户端同意和任意客户端同意策略；第三，容错执行，客户端节点可随时加入/离开swarm而不中断训练，支持热插拔调试和实时代码迭代；第四，上下文追踪与时间线合并，每个episode的LLM调用被拦截并记录为独立时间线，包含消息块、token ID、log概率和loss掩码，合并时消除冗余上下文实现1.5-10倍训练加速。

此外，AgentJet支持黑盒agent训练，仅需替换agent的LLM base URL和API key即可兼容LangChain、AgentScope等任意HTTP通信框架，并构建了自动研究系统，可自主执行多日长周期RL实验。

### Q4: 论文做了哪些实验？

论文在狼人杀游戏中进行了多组实验。实验设置采用1服务器-1客户端的群集强化学习网络，服务器托管共享参数的Qwen2模型（7B或14B），对手由静态的Qwen3-235B-A22B模型控制。数据集为9人狼人杀游戏配置（3狼人、3村民、1预言家、1女巫、1猎人），这是一个部分可观察马尔可夫决策过程（POMDP）环境。

实验分为两类：共享参数训练和非共享参数训练。共享参数训练测试了7种配置，包括单独训练狼人（7B和14B）、单独训练村民阵营角色（预言家、女巫、猎人），以及组合训练。主要结果显示：训练狼人阵营增益最大，7B模型胜率从23.0%提升至47.2%，14B模型从40.9%提升至64.7%；训练单个预言家角色（38.5%→46.5%）优于女巫（38.8%→38.9%）和猎人（31.9%→34.5%）；联合训练三个特殊角色（22.9%→35.9%）和整个非狼人团队（23.9%→41.6%）也体现了性能提升。非共享参数训练使用多服务器配置训练独立模型，三种配置下胜率从22.0-40.8%提升至30.5-66.5%。此外，实验还展示了行为改进案例，如训练后的狼人学会了角色欺骗、社会欺骗策略和隐式协调。

### Q5: 有什么可以进一步探索的点？

AgentJet的分布式架构虽然解决了集中式框架的扩展性问题，但仍存在若干可探索的方向。首先，当前的多模型强化学习主要依赖静态的模型组合，未来可研究动态的模型协同机制，例如利用元学习让不同LLM在训练过程中自适应调整角色与决策权重。其次，多任务鸡尾酒训练虽隔离了运行时环境，但任务间的负迁移风险未被充分评估，可引入任务相似度度量与动态任务采样策略来缓解。此外，容错执行仅处理了外部环境故障，对模型参数更新过程中的梯度异常或通信延迟缺乏鲁棒性，可探索异步梯度聚合与冗余节点备份机制。最后，实时代码迭代虽提升了研究灵活性，但频繁替换客户端可能导致训练轨迹不连贯，建议开发智能版本控制模块，保持策略梯度与历史经验池的一致性。长期看，将AgentJet与人类反馈闭环结合，或能实现更高效的自适应研究系统。

### Q6: 总结一下论文的主要内容

AgentJet提出了一种灵活的分布式群智训练框架，用于解决大型语言模型智能体强化学习中的关键挑战。核心问题在于现有集中式框架存在运行脆弱性、调试困难、难以支持异构多模型和冗余上下文等问题。AgentJet采用解耦的多节点架构，将群智服务器节点（运行模型优化）与客户端节点（执行任意智能体）分离。该方法通过上下文跟踪模块与时间线合并技术，实现了1.5-10倍的训练加速。主要贡献包括：支持异构多模型强化学习、多任务鸡尾酒训练、容错执行、实时代码迭代等能力。实验表明，AgentJet能够实现智能体代码的热替换、自动化研究流程（如超参数优化）等高级工作流，并兼容LangChain等多种框架。该工作为构建灵活、可扩展的分布式智能体强化学习系统提供了全新范式。
