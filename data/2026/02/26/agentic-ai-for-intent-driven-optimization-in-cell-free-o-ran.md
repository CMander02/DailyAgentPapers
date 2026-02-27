---
title: "Agentic AI for Intent-driven Optimization in Cell-free O-RAN"
authors:
  - "Mohammad Hossein Shokouhi"
  - "Vincent W. S. Wong"
date: "2026-02-26"
arxiv_id: "2602.22539"
arxiv_url: "https://arxiv.org/abs/2602.22539"
pdf_url: "https://arxiv.org/pdf/2602.22539v1"
categories:
  - "cs.AI"
  - "eess.SP"
tags:
  - "Agent Architecture"
  - "Multi-Agent System"
  - "LLM-based Agent"
  - "Agent Coordination"
  - "Agent Memory"
  - "Parameter-Efficient Fine-Tuning"
  - "Network Optimization"
relevance_score: 7.5
---

# Agentic AI for Intent-driven Optimization in Cell-free O-RAN

## 原始摘要

Agentic artificial intelligence (AI) is emerging as a key enabler for autonomous radio access networks (RANs), where multiple large language model (LLM)-based agents reason and collaborate to achieve operator-defined intents. The open RAN (O-RAN) architecture enables the deployment and coordination of such agents. However, most existing works consider simple intents handled by independent agents, while complex intents that require coordination among agents remain unexplored. In this paper, we propose an agentic AI framework for intent translation and optimization in cell-free O-RAN. A supervisor agent translates the operator intents into an optimization objective and minimum rate requirements. Based on this information, a user weighting agent retrieves relevant prior experience from a memory module to determine the user priority weights for precoding. If the intent includes an energy-saving objective, then an open radio unit (O-RU) management agent will also be activated to determine the set of active O-RUs by using a deep reinforcement learning (DRL) algorithm. A monitoring agent measures and monitors the user data rates and coordinates with other agents to guarantee the minimum rate requirements are satisfied. To enhance scalability, we adopt a parameter-efficient fine-tuning (PEFT) method that enables the same underlying LLM to be used for different agents. Simulation results show that the proposed agentic AI framework reduces the number of active O-RUs by 41.93% when compared with three baseline schemes in energy-saving mode. Using the PEFT method, the proposed framework reduces the memory usage by 92% when compared with deploying separate LLM agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决开放无线接入网（O-RAN）中，如何利用智能体人工智能（Agentic AI）来处理复杂运营商意图并实现网络自主优化的问题。研究背景是，O-RAN作为6G的关键使能技术，其开放架构允许部署智能应用（如rApps、xApps）来实现网络智能化。传统RAN管理复杂，而基于AI的自主RAN允许运营商用自然语言表达高层意图（如节能、保障速率），由AI代理自动执行。现有方法大多利用基于大语言模型（LLM）的独立代理处理简单、可分解且互不重叠的意图，但存在两大不足：一是对于需要多个代理协同完成的复杂意图（例如同时满足节能和最低速率保障），现有研究尚未深入探索；二是通常为每个代理部署独立的LLM，导致内存消耗大，可扩展性受限。因此，本文要解决的核心问题是：在无蜂窝O-RAN场景下（每个用户由多个O-RU协同服务），设计一个可扩展的智能体AI框架，以处理需要跨代理协作的复杂运营商意图，并将其高效翻译和优化为具体的网络控制参数（如用户预编码权重、激活的O-RU集合），同时通过参数高效微调技术降低部署开销。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**基于AI/LLM的意图驱动O-RAN优化方法**、**O-RAN中的节能与资源管理应用**以及**高效LLM部署技术**。

在**意图驱动优化方法**方面，已有工作利用LLM智能体解释运营商意图并匹配调度器，或将意图分解为子任务调用专用智能体执行。例如，有研究通过管理器智能体将意图分解为功率控制和资源分配子意图。然而，这些工作大多假设意图可分解为独立智能体处理的不重叠目标，未深入探索需要智能体间协作的复杂意图。本文则针对此类复杂意图，提出了一个包含监控与协调机制的多智能体协作框架。

在**节能与资源管理应用**方面，已有研究提出O-RU开关控制rApp和O-CU/O-DU功能放置xApp以降低能耗，或通过xApp调整用户权重保障最低速率。本文的框架整合了类似目标，但进一步引入了基于多智能体深度强化学习的O-RU管理智能体，并与其他智能体协同工作，在保证服务质量的同时实现能效优化。

在**高效LLM部署技术**方面，现有方案常为每个智能体部署独立LLM，导致内存开销大、可扩展性受限。本文采用参数高效微调方法，使多个智能体共享同一个基础LLM，并通过QLoRA适配器保持其专用性，显著降低了内存占用，提升了框架的实用性。

### Q3: 论文如何解决这个问题？

论文通过提出一个基于智能体人工智能（Agentic AI）的框架来解决无蜂窝O-RAN中意图驱动的优化问题，其核心是设计多个基于大语言模型（LLM）的智能体进行协同推理与决策。整体框架遵循O-RAN架构，在非实时RAN智能控制器（non-RT RIC）中部署监督智能体（Supervisor Agent），在近实时RAN智能控制器（near-RT RIC）中部署用户权重智能体（User Weighting Agent）、O-RU管理智能体（O-RU Management Agent）和监控智能体（Monitoring Agent）。

核心方法是将复杂的运营商意图（如能效优化）分解并转化为具体的优化目标与约束。监督智能体负责意图翻译，输出优化目标（如聚合效用最大化或节能）和用户最低速率要求。用户权重智能体根据历史数据（存储在记忆模块中）和当前约束，通过计算效用函数导数和更新拉格朗日乘子，确定用于预编码的用户优先级权重α_k。若意图包含节能目标，O-RU管理智能体则被激活，采用多智能体近端策略优化（MAPPO）这一深度强化学习（DRL）算法，以分布式方式决策各无线单元（O-RU）的激活状态z_l。监控智能体持续监测用户速率，并在约束不满足时协调调整α_k和违规惩罚系数λ_k，直至所有最低速率要求得到满足。

关键技术包括：1）针对混合整数规划问题，采用块坐标下降法交替优化预编码矩阵和O-RU激活状态；2）为高效解决大规模O-RU激活问题，设计了基于MAPPO的分布式DRL算法，每个O-RU作为智能体依据局部观测（大尺度衰落、速率违规、自身前一状态）进行决策，并通过共享评论家（critic）进行协同；3）提出检索增强的系数调优方法，利用自动编码器将环境特征嵌入为键，存储并检索相似历史场景下的优化系数，以加速收敛；4）为提升可扩展性并降低内存开销，采用参数高效微调（PEFT）方法QLoRA，将同一底层LLM量化后，通过适配器微调用于不同智能体任务，大幅减少内存占用。

创新点主要体现在：通过多LLM智能体协同处理复杂意图，实现了意图翻译、优化决策与动态监控的闭环；将DRL与优化理论结合，以分布式方式解决O-RU激活难题；引入记忆模块与检索机制实现经验复用；利用QLoRA技术实现轻量级多智能体部署，在保证性能的同时显著提升了框架的实用性与可扩展性。

### Q4: 论文做了哪些实验？

论文在仿真环境中评估了所提出的智能体AI框架。实验设置了一个包含50个开放无线单元（O-RU）的Cell-Free O-RAN网络，覆盖500平方米，用户设备最多由8个O-RU服务。智能体基于GPT-5（监督智能体）和不同规模的Qwen 2.5模型（近实时智能体）构建，并采用了参数高效微调（PEFT）方法。

实验主要在两个基准测试上进行：一是节能模式下激活的O-RU比例，二是不同部署设置下的内存使用量。对比方法包括三种基线方案：1）DRL+梯度上升（GA）算法；2）贪婪算法；3）全功率模式（所有O-RU始终激活）。

主要结果显示，在节能模式下，所提框架（使用7B或14B模型）相比贪婪算法最多减少了41.93%的活跃O-RU数量。在内存使用方面，通过联合应用4位量化（FP4）和LoRA适配器，与部署三个独立的全精度（FP16）LLM相比，内存使用量减少了92%（例如，14B模型下从88.2 GB降至7.4 GB）。此外，实验还演示了框架如何动态协调智能体以满足不同运营商意图（如节能和效用最大化）下的用户最低速率要求。

### Q5: 有什么可以进一步探索的点？

该论文提出的框架在意图翻译和能效优化方面取得了显著效果，但其局限性和未来探索方向值得深入思考。首先，框架目前主要处理相对结构化的运营商意图（如节能、最低速率保障），对于更复杂、动态或模糊的意图（如“在保障用户体验的前提下最大化网络经济效益”）的解析与分解能力尚未验证，未来可探索更高级的意图理解与动态任务规划机制。其次，智能体间的协调目前依赖于监控智能体的集中式协调，在更大规模或更分布式的场景下可能存在瓶颈，未来可研究去中心化的智能体协作与协商机制，例如基于多智能体强化学习或市场博弈理论的协调策略。此外，论文虽采用了参数高效微调（PEFT）来提升扩展性，但智能体的决策仍严重依赖历史经验记忆，对于未知或快速变化的网络环境（如突发流量、移动性剧增）的适应性与在线学习能力不足，未来可结合在线元学习或联邦学习来增强智能体的泛化与实时适应能力。最后，框架目前仅模拟验证，实际部署时还需考虑O-RAN接口的实时性约束、智能体决策的可解释性以及与传统网络控制逻辑的融合问题，这些都是迈向实际应用的关键研究方向。

### Q6: 总结一下论文的主要内容

本文提出了一种用于无小区O-RAN中意图驱动优化的智能体AI框架，旨在解决现有研究中智能体独立处理简单意图、而缺乏对需要多智能体协作的复杂意图进行探索的问题。其核心贡献在于设计了一个多智能体协作系统，将运营商的高级业务意图自动转化为具体的网络优化目标与约束。

方法上，框架包含多个基于大语言模型（LLM）的智能体：监督智能体在非实时RIC中将运营商意图解析为优化目标和最低速率要求；用户权重智能体在近实时RIC中从记忆模块检索先验经验以确定用户优先级权重；若意图包含节能目标，则激活O-RU管理智能体，采用多智能体深度强化学习算法决定激活的无线单元集合；监控智能体负责测量用户数据速率并协调其他智能体确保满足最低速率要求。为提升可扩展性，论文采用参数高效微调方法，使同一底层LLM能适配不同智能体，大幅降低内存占用。

主要结论显示，该框架在节能模式下相比三种基线方案，能将活跃O-RU数量减少41.93%；同时，采用的轻量化LLM部署策略使内存使用量比部署独立LLM智能体减少了92%。这验证了所提框架在实现复杂意图驱动优化、提高能效以及降低系统开销方面的有效性与优越性。
