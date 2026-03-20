---
title: "ProRL Agent: Rollout-as-a-Service for RL Training of Multi-Turn LLM Agents"
authors:
  - "Hao Zhang"
  - "Mingjie Liu"
  - "Shaokun Zhang"
  - "Songyang Han"
  - "Jian Hu"
  - "Zhenghui Jin"
  - "Yuchi Zhang"
  - "Shizhe Diao"
  - "Ximing Lu"
  - "Binfeng Xu"
  - "Zhiding Yu"
  - "Jan Kautz"
  - "Yi Dong"
date: "2026-03-19"
arxiv_id: "2603.18815"
arxiv_url: "https://arxiv.org/abs/2603.18815"
pdf_url: "https://arxiv.org/pdf/2603.18815v1"
categories:
  - "cs.AI"
tags:
  - "Agent 基础设施"
  - "强化学习训练"
  - "多轮对话 Agent"
  - "系统架构"
  - "开源工具"
  - "软件工程 Agent"
  - "代码生成"
  - "数学推理"
relevance_score: 8.0
---

# ProRL Agent: Rollout-as-a-Service for RL Training of Multi-Turn LLM Agents

## 原始摘要

Multi-turn LLM agents are increasingly important for solving complex, interactive tasks, and reinforcement learning (RL) is a key ingredient for improving their long-horizon behavior. However, RL training requires generating large numbers of sandboxed rollout trajectories, and existing infrastructures often couple rollout orchestration with the training loop, making systems hard to migrate and maintain. Under the rollout-as-a-service philosophy, we present ProRL Agent , a scalable infrastructure that serves the full agentic rollout lifecycle through an API service. ProRL Agent also provides standardized and extensible sandbox environments that support diverse agentic tasks in rootless HPC settings. We validate ProRL Agent through RL training on software engineering, math, STEM, and coding tasks. ProRL Agent is open-sourced and integrated as part of NVIDIA NeMo Gym.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多轮大型语言模型（LLM）智能体进行强化学习（RL）训练时，在基础设施层面存在的系统耦合与可扩展性瓶颈问题。

研究背景是，随着LLM智能体从单轮任务转向解决复杂的多轮交互任务（如软件工程、网页浏览），强化学习成为优化其长期行为的关键技术。然而，训练过程需要生成大量在沙盒环境中的“推演”轨迹来评估和优化策略。现有方法（如现有的一些智能体RL训练框架）通常将负责环境交互、工具执行的智能体推演生命周期，紧密耦合在RL训练器的代码和进程内部。这种设计存在明显不足：首先，它导致系统需求冲突，因为推演是I/O密集型、长时异步的任务，而策略训练是GPU密集型、同步计算的任务，二者耦合会造成资源干扰和效率低下；其次，它使得系统难以迁移和维护，任何对推演基础设施（如支持新环境）或训练后端（如更换RL库）的改动都会相互牵连，增加了迭代复杂度和长期维护成本。

因此，本文要解决的核心问题是：如何设计一个可扩展、易维护的基础设施，以高效支持多轮LLM智能体的RL训练。为此，论文提出了“推演即服务”的设计哲学，并推出了ProRL Agent系统。其核心解决方案是将智能体的完整推演生命周期（从环境初始化到结果评估）封装为一个独立的HTTP API服务，从而与RL训练器完全解耦。这使得训练器只需提交任务并获取完成的轨迹，而无需管理推演过程，实现了计算资源的隔离、系统的可移植性以及更好的可扩展性。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕多轮LLM智能体的强化学习训练基础设施展开，可分为以下几类：

**多轮智能体RL方法研究**：已有研究成功将强化学习应用于数学、逻辑、编程等单轮推理任务，并进一步扩展到多轮交互式智能体场景。这些工作将多轮智能体建模为部分可观测马尔可夫决策过程（POMDP），智能体通过工具调用产生动作并接收环境观测。然而，随着任务复杂度增加，在多步、多样化环境（如代码库、浏览器、操作系统）中生成和管理大规模模拟轨迹（rollout）成为RL训练的主要瓶颈。本文的ProRL Agent正是为了系统性地解决这一规模化挑战而设计。

**智能体RL训练框架**：现有框架（如SkyRL-Agent、VeRL-Tool、Agent Lightning、rLLM、GEM等）已开始支持可扩展的RL训练，包括工具集成、环境抽象和轨迹调度。但如论文表格对比所示，这些框架普遍存在一个关键局限：**模拟轨迹的编排（包括环境生命周期管理、工具执行、轨迹收集与评估）与训练循环紧密耦合**，通常作为训练进程内的库实现。这种设计导致更换训练后端时往往需要重写整个模拟栈，增加了工程复杂性和维护成本。本文提出的ProRL Agent的核心创新在于**彻底解耦了模拟轨迹生命周期与训练堆栈**，将其通过API服务提供（即“模拟即服务”），使研究人员能专注于算法与智能体设计。

**智能体沙箱环境**：多轮智能体训练需要具备隔离性、可复现性和安全性的沙箱环境。现有平台主要依赖Docker，但其需要守护进程访问和root等效权限，在共享的Slurm管理的高性能计算集群上往往不可用。这迫使实践者要么维护独立的基础设施，要么在受限系统上承担特权容器运行时的运维复杂性。ProRL Agent通过基于Singularity构建沙箱基础设施，实现了**无需root权限的执行和与Slurm的原生集成**，从而支持在共享HPC环境中进行大规模、安全的训练。

综上，本文与相关工作的关系是：**继承并整合了多轮智能体RL的问题形式化与方法目标，但通过架构创新（解耦的API服务、rootless沙箱、训练框架无关性）系统解决了现有基础设施在可扩展性、可移植性和部署便利性上的核心痛点**。

### Q3: 论文如何解决这个问题？

论文通过提出“Rollout-as-a-Service”的设计理念，构建了一个名为ProRL Agent的可扩展基础设施，以解决传统RL训练中rollout轨迹生成与训练循环紧密耦合、导致系统难以迁移和维护的问题。其核心方法是将rollout编排完全从训练过程中分离出来，作为一个独立的API服务。

整体框架由三个主要组件构成：
1. **可扩展的沙盒环境**：每个rollout在一个SingularityRuntime容器中执行，由AgentHandler进行编排。AgentHandler定义了三个核心生命周期方法：init()用于环境设置，run()用于执行多轮智能体交互并收集轨迹，eval()用于根据真实结果评分并返回奖励信号。这种抽象接口设计使得添加新任务只需实现相应的handler插件，无需修改训练代码。沙盒环境采用rootless的HPC兼容容器运行时，支持在无特权访问的高性能计算集群上大规模执行隔离的任务。

2. **ProRL Agent服务器**：这是一个HTTP服务，负责管理rollout的全生命周期。其关键创新是采用了一个异步的三阶段流水线（INIT → RUN → EVAL），每个阶段对应独立的worker池。这种设计允许不同阶段（如容器初始化、智能体执行、结果评估）在多个任务上并行重叠执行，避免了单一worker顺序执行所有阶段导致的资源利用率低下问题。服务器还维护了一个最小堆结构的LLM后端池，支持动态注册和检查点交换，使训练框架能灵活控制推理资源。

3. **RL训练器**：任何训练框架（如veRL、NeMo RL）都仅通过HTTP接口与ProRL Agent服务器交互。训练器通过POST /process提交任务实例，并通过/add_llm_server等端点管理后端；服务器执行完整的rollout后，将完成的轨迹和奖励返回给训练器以更新策略。这种解耦使得训练器和rollout逻辑可以独立开发和部署，rollout节点和训练节点也能分别优化以提升吞吐量。

关键技术包括：
- **任务特定逻辑的插件化**：通过AgentHandler接口封装，使服务器核心与具体任务解耦。
- **高性能沙盒运行时**：使用Singularity容器实现rootless、便携的隔离执行；通过优化工具后端（如用ptyprocess替代tmux提升Bash效率、采用IPython内核的进程内API减少延迟、使用Unix域 sockets替代TCP进行进程间通信）显著降低工具调用延迟，防止其成为高并发下的瓶颈。
- **动态资源管理API**：提供轻量级的HTTP管理端点，使训练框架能在运行时控制任务提交、取消、LLM后端注册等，无需与服务器内部紧密耦合。

总之，ProRL Agent通过rollout级解耦、异步流水线架构和标准化的可扩展沙盒，提供了一个灵活、高效且易于维护的基础设施，支持多轮LLM智能体在多样任务上进行RL训练。

### Q4: 论文做了哪些实验？

论文在软件工程、数学、STEM和编程等多类任务上进行了强化学习训练实验，以验证ProRL Agent系统的有效性。

**实验设置**：实验基于ProRL Agent的“训练-推演解耦”架构。推演过程通过HTTP API服务进行，包含三个异步阶段（初始化、运行、评估），每个阶段由独立的线程池处理。沙箱环境采用SingularityRuntime容器，确保在无root权限的HPC环境中安全、可移植地执行。系统优化了关键工具后端，包括使用ptyprocess提升Bash效率、通过进程内API连接IPython内核以减少延迟，以及采用Unix域套接字进行进程间通信。

**数据集/基准测试**：实验涵盖了多样化的智能体任务，包括软件工程（如代码生成与修复）、数学推理、STEM问题求解以及编程挑战。这些任务需要多轮交互和工具使用，以评估系统处理长期、复杂行为的能力。

**对比方法与主要结果**：论文将ProRL Agent与传统的、将推演逻辑紧密耦合在训练循环中的系统进行对比。主要结果表明，ProRL Agent通过服务化设计，显著降低了工程开销，使任务切换、训练框架更换和智能体框架修改更加便捷。关键数据指标包括：推演吞吐量（通过异步管道和独立资源池实现高效并发）、任务部署的灵活性（仅需在服务器端实现处理插件，无需改动训练代码）以及工具执行延迟的降低（通过三项后端优化，确保其在高并发下不成为瓶颈）。系统已开源并集成至NVIDIA NeMo Gym。

### Q5: 有什么可以进一步探索的点？

该论文提出的ProRL Agent系统将rollout过程服务化，有效解耦了轨迹生成与训练循环，但在实际应用中仍存在一些可探索的方向。首先，系统目前主要依赖标准化的沙箱环境，对于更开放、动态的真实世界任务（如实时网络交互或物理机器人控制）支持有限，未来可研究如何将服务化架构扩展到非确定性和高延迟的环境。其次，论文未深入讨论多智能体协同场景下的rollout服务化，这在分布式任务中尤为重要，可探索如何高效管理跨智能体的轨迹同步与冲突解决。此外，rollout服务的性能优化（如异步并行、轨迹缓存与复用机制）仍有提升空间，特别是在长序列任务中可能面临内存与计算瓶颈。最后，该架构可结合课程学习或元强化学习，动态调整rollout难度与分布，从而提升训练效率与智能体泛化能力。

### Q6: 总结一下论文的主要内容

本文针对多轮LLM智能体强化学习训练中存在的瓶颈，提出了一种创新的“Rollout-as-a-Service”基础设施——ProRL Agent。核心问题是现有框架将环境交互轨迹生成与RL训练循环紧密耦合，导致系统资源效率低下、难以迁移和维护。为解决此问题，论文设计了ProRL Agent，其核心方法是将完整的智能体交互生命周期（包括环境初始化、工具使用和结果评估）封装为一个独立的HTTP API服务，从而与GPU密集型的训练过程解耦。该方法还引入了token级轨迹通信以避免重编码偏差，提供了可扩展的沙盒环境，并支持在无root权限的高性能计算集群中部署。实验表明，该基础设施在软件工程、数学、STEM和编码等任务上能有效支持不同规模模型的RL训练，并在SWE-Bench Verified等基准上取得了显著提升。该工作的主要贡献在于通过服务化设计，解决了智能体RL训练系统的可扩展性、可维护性和资源隔离问题。
