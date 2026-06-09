---
title: "Claw-R1: A Step-Level Data Middleware System for Agentic Reinforcement Learning"
authors:
  - "Daoyu Wang"
  - "Mingyue Cheng"
  - "Qingchuan Li"
  - "Shuo Yu"
  - "Jie Ouyang"
  - "Qi Liu"
date: "2026-06-08"
arxiv_id: "2606.09138"
arxiv_url: "https://arxiv.org/abs/2606.09138"
pdf_url: "https://arxiv.org/pdf/2606.09138v1"
github_url: "https://github.com/AgentR1/Claw-R1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "Agent训练数据管理"
  - "Agent强化学习"
  - "中间件系统"
  - "多智能体交互轨迹管理"
relevance_score: 8.5
---

# Claw-R1: A Step-Level Data Middleware System for Agentic Reinforcement Learning

## 原始摘要

Agentic reinforcement learning (RL) has become an important post-training paradigm for turning LLMs from static chatbots into interactive agents, giving rise to representative applications such as OpenClaw. Existing work mainly focuses on policy optimization algorithms and training frameworks, but pays less attention to the full data lifecycle of agent-environment interactions, from data production to training consumption. To bridge this gap, we present Claw-R1, an interactive step-level data middleware system for agentic RL. Claw-R1 connects heterogeneous agent runtimes with RL training backends through two core components: a Gateway Server and a Data Pool. The Gateway Server captures multi-turn interaction steps through a unified LLM API entry point, while the Data Pool organizes them into step-level records consisting of prompt IDs, response IDs, rewards and other metadata. In our demo, users can interactively inspect live trajectories, examine the state, action, and reward of each step, curate data by quality and readiness, and configure training-ready batches for different downstream RL algorithms. Overall, Claw-R1 treats agent interaction traces as managed data assets rather than temporary runtime logs. Through this demonstration, we hope to encourage the community to recognize the importance of data management in agentic RL. Our code is available at https://github.com/AgentR1/Claw-R1 and the demonstration video can be found at link https://youtu.be/Pw47dAOw6B0.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体强化学习（Agentic RL）领域中数据生命周期管理缺失的问题。随着大语言模型（LLM）从静态聊天机器人转向具备多轮执行、工具调用和交互反馈的智能体，Agentic RL成为重要的后训练范式。然而，现有研究主要集中在策略优化算法（如PPO、GRPO）和训练框架的改进上，对智能体与环境交互过程中产生的异构数据——从数据生成到训练消费的完整生命周期——关注不足。这导致了一个关键挑战：当智能体运行时变得日益复杂和异构（如编码智能体需管理长上下文、执行bash命令、编辑文件等），若将RL训练后端与特定运行时逻辑紧密耦合，每增加一个智能体就需要定制化接口，严重限制了系统的可扩展性。

为此，论文提出Claw-R1，一个步骤级的数据中间件系统。其核心创新在于从数据管理视角出发，通过网关服务器（Gateway Server）和数据池（Data Pool）两个组件，将异构智能体运行时与RL训练后端解耦。系统将智能体的交互轨迹视为可管理的训练数据资产，而非临时运行时日志，从而解决了智能体运行时复杂性与训练后端通用性之间的矛盾，使得大规模、多类型的智能体RL训练更加高效和可扩展。

### Q2: 有哪些相关研究？

相关工作可分为三类：**政策优化与训练框架类**、**数据合成类**以及**系统中间件类**。第一类是政策优化方法（如PPO、GRPO）及相应的训练框架，它们专注于提升LLM在偏好对齐、推理验证以及多轮交互中的目标设计、信用分配和步级优化。Claw-R1并不直接提出新的优化算法，而是聚焦于这些方法在执行过程中产生的数据生命周期的管理。第二类是数据合成研究，通过可扩展的合成流程（如交互式网络会话、多轮指令跟踪、多智能体轨迹）生成高质量的训练轨迹。本文与之互补：这些工作关注“如何产生”数据，而Claw-R1关心“如何管理”已经产生的异构交互数据。第三类是系统中间件工作，Claw-R1本身即属此类。它作为连接异构智能体运行时（如白盒、黑盒智能体或实时服务）与RL训练后端（如PPO、GRPO）的**步级数据中间件**，对交互轨迹进行采集、表示、筛选、优化并持久化，将其从临时日志转变为受管理的训练资产。现有系统较少系统性地关注这一数据全生命周期管理问题。

### Q3: 论文如何解决这个问题？

Claw-R1通过一套层级数据中间件系统连接异构智能体运行时和强化学习训练后端，核心包含两大组件：网关服务器（Gateway Server）和数据池（Data Pool）。网关服务器作为统一的数据采集入口，为白盒智能体提供显式的步骤提交接口（携带prompt ID、response ID、奖励和元数据），同时为黑盒智能体提供OpenAI兼容的API端点来捕获LLM调用并自动转换成交互步骤。数据池则作为数据管理核心，以持久化记录存储完整的token序列、奖励、轨迹关系、prompt分组、策略版本和来源元数据，并为prompt ID、轨迹、奖励状态等建立索引。整体架构遵循四项设计原则：低侵入式采集（无需修改现有智能体系统）、步骤原生表示（保留强化学习语义如状态-动作-奖励-下一状态）、异步解耦（数据收集与模型训练分离）、后端感知服务（通过轻量适配层暴露训练兼容的数据接口）。创新点包括：步骤级数据抽象将多轮交互从临时运行时日志转化为可管理的训练资产；前缀树合并优化利用同一prompt生成的多个轨迹共享前缀的特性，将具有相同token前缀的步骤合并为紧凑树结构，减少冗余长上下文计算；以及基于拉取的批量数据接口，允许训练后端按需获取已就绪的批次并按奖励、策略版本、轨迹完整性等条件过滤。此外，系统还提供交互式仪表盘，支持实时观察轨迹、检查每一步的状态和奖励、按质量与就绪状态筛选数据，并为不同下游强化学习算法配置训练批次。

### Q4: 论文做了哪些实验？

论文《Claw-R1》主要进行了用户演示实验，展示了其数据中间件系统的流程。实验设置围绕一个集成仪表盘展开，用户可在其中观察从数据收集到训练消耗的完整生命周期。数据集基于智能体强化学习环境中的交互轨迹，包括白盒rollout、黑盒服务及人类反馈流等异构来源。对比方法方面，论文未直接与其他系统对比，而是突显Claw-R1将交互追踪作为数据资产管理而非临时日志的方法。主要结果通过仪表盘功能呈现：1）在收集阶段，用户可观察交互轨迹的到达和来源贡献；2）处理阶段，交互被标准化为包含提示ID、响应ID、奖励和元数据的步骤级记录；3）组织阶段，提供基于轨迹长度、奖励状态、来源和难度水平的筛选与查询工具；4）优化阶段，通过前缀树合并减少冗余令牌计算，并展示令牌节省统计和注意力掩码；5）消耗阶段，可监控批次获取活动、已消耗步骤、策略版本及权重同步状态。实验关键指标包括步骤级奖励状态、轨迹长度、来源贡献率及令牌共享统计。

### Q5: 有什么可以进一步探索的点？

Claw-R1在数据管理方面有创新，但其局限性和未来方向值得深入探讨。首先，当前系统仅作为数据中间件，并未解决RL训练本身的核心问题，如稀疏奖励下的探索效率和多轮交互中的信用分配。系统虽支持步级记录，但对于复杂的长期规划任务（如需要数十步推理），基于步的奖励设计可能仍不够细化。其次，系统侧重于数据捕获和可视化，但缺乏主动的数据增强机制，例如通过合成数据或回放缓冲区中的优先级采样来提升训练效率。未来可以探索将数据池与自适应课程学习相结合，根据当前策略的弱点动态筛选或生成高价值轨迹。此外，引入反事实推理或逆RL技术，从失败轨迹中自动提取负面经验，也是提升样本效率的有前景方向。最后，跨智能体运行时的异构数据格式标准化和隐私保护机制也是值得关注的研究点。

### Q6: 总结一下论文的主要内容

本文提出了Claw-R1，一个专为智能体强化学习设计的步骤级数据中间件系统。该工作指出，现有研究主要关注策略优化算法和训练框架，忽视了从数据生成到训练消费的完整数据生命周期管理问题。Claw-R1通过两个核心组件——网关服务器和数据池——来解耦异构的智能体运行环境与RL训练后端。网关服务器通过统一的LLM API入口捕获多轮交互步骤，数据池则将这些步骤组织成包含提示ID、响应ID、奖励和元数据的步骤级记录。系统允许用户交互式监控实时轨迹、检查每一步的状态-行动-奖励、按质量和就绪程度筛选数据，并为不同下游RL算法配置训练批次。主要贡献在于将智能体交互轨迹视为可管理的数据资产而非临时运行时日志，凸显了数据管理在智能体强化学习中的重要性，为更可扩展的智能体开发和训练效率提升奠定了基础。
