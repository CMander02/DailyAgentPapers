---
title: "MOSAIC: A Unified Platform for Cross-Paradigm Comparison and Evaluation of Homogeneous and Heterogeneous Multi-Agent RL, LLM, VLM, and Human Decision-Makers"
authors:
  - "Abdulhamid M. Mousa"
  - "Yu Fu"
  - "Rakhmonberdi Khajiev"
  - "Jalaledin M. Azzabi"
  - "Abdulkarim M. Mousa"
date: "2026-03-01"
arxiv_id: "2603.01260"
arxiv_url: "https://arxiv.org/abs/2603.01260"
pdf_url: "https://arxiv.org/pdf/2603.01260v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Architecture & Frameworks"
relevance_score: 8.0
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Architecture & Frameworks"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "IPC-based worker protocol, operator abstraction, deterministic cross-paradigm evaluation framework"
  primary_benchmark: "N/A"
---

# MOSAIC: A Unified Platform for Cross-Paradigm Comparison and Evaluation of Homogeneous and Heterogeneous Multi-Agent RL, LLM, VLM, and Human Decision-Makers

## 原始摘要

Reinforcement learning (RL), large language models (LLMs), and vision-language models (VLMs) have been widely studied in isolation. However, existing infrastructure lacks the ability to deploy agents from different decision-making paradigms within the same environment, making it difficult to study them in hybrid multi-agent settings or to compare their behaviour fairly under identical conditions. We present MOSAIC, an open-source platform that bridges this gap by incorporating a diverse set of existing reinforcement learning environments and enabling heterogeneous agents (RL policies, LLMs, VLMs, and human players) to operate within them in ad-hoc team settings with reproducible results. MOSAIC introduces three contributions. (i) An IPC-based worker protocol that wraps both native and third-party frameworks as isolated subprocess workers, each executing its native training and inference logic unmodified, communicating through a versioned inter-process protocol. (ii) An operator abstraction that forms an agent-level interface by mapping workers to agents: each operator, regardless of whether it is backed by an RL policy, an LLM, or a human, conforms to a minimal unified interface. (iii) A deterministic cross-paradigm evaluation framework offering two complementary modes: a manual mode that advances up to N concurrent operators in lock-step under shared seeds for fine-grained visual inspection of behavioural differences, and a script mode that drives automated, long-running evaluation through declarative Python scripts, for reproducible experiments. We release MOSAIC as an open, visual-first platform to facilitate reproducible cross-paradigm research across the RL, LLM, and human-in-the-loop communities.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体研究领域中的一个关键基础设施缺失问题：缺乏一个能够统一评估和比较来自不同决策范式（如强化学习、大语言模型、视觉语言模型和人类）的智能体在相同环境条件下的平台。研究背景是，尽管强化学习框架和LLM/VLM基准测试各自已相当成熟，且环境接口（如Gymnasium、PettingZoo）已实现标准化，但智能体侧却高度碎片化。现有方法存在明显不足：一方面，传统的RL框架仅支持基于张量观测和整数动作的RL策略，而LLM/VLM基准测试则专注于文本或视觉语言模型，它们彼此隔离，无法在统一环境中交互或对比；另一方面，现有的临时团队合作研究通常假设所有智能体共享相同的观测和动作表示，这无法应对现实中异构智能体（拥有不同模态接口）协同工作的复杂场景。因此，本文的核心问题是：如何构建一个开放、可复现的平台，以支持将异构的决策范式（RL、LLM、VLM、人类）无缝集成到相同的多智能体环境中，并在此基础之上，实现对这些不同范式智能体行为的公平、细粒度、可复现的比较与评估。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：强化学习框架、LLM/VLM基准测试平台，以及新兴的跨范式协作研究。

在**强化学习框架**方面，RLlib、CleanRL、Tianshou、Acme、XuanCe、OpenRL和Stable-Baselines3等成熟系统专注于训练和评估RL智能体，通常仅支持基于张量观测和离散/连续动作的RL策略，不支持LLM、VLM或人类玩家。Coach和BenchMARL等框架虽可能提供可视化界面，但仍局限于单一RL范式。

在**LLM/VLM基准测试平台**方面，BALROG、AgentBench、TextArena、GameBench和AgentGym等平台专为评估语言模型或视觉语言模型在特定任务（如文本游戏、棋类）上的表现而设计。它们通常支持LLM/VLM智能体，部分（如TextArena）支持人类参与，但普遍不支持原生RL智能体集成，或仅通过有限方式（如Collab-Overcooked）部分支持，缺乏统一的跨范式比较基础设施。

在**跨范式协作与评估**方面，临时团队合作（AHT）和零样本协调（ZSC）的研究关注智能体与未知队友的协作，但传统工作假设所有智能体共享相同的观测与动作表示。近期出现的Game Reasoning Arena、CREW、LLM-PySC2等框架开始探索RL与LLM的混合，但支持范围有限（如可能缺少VLM或人类支持），且往往需要修改第三方算法源码才能集成。

本文提出的MOSAIC平台与上述所有工作都不同。它首次在一个统一系统中完整支持RL、LLM、VLM和人类四种决策范式，允许它们在不修改原生源码的情况下作为隔离的“工作者”集成，并通过确定的、种子共享的评估框架进行公平比较。其核心创新在于通过“操作符”抽象提供统一的智能体接口，并具备平台GUI和声明式脚本评估能力，填补了现有基础设施在异构多智能体、跨范式协同与评测方面的空白。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为MOSAIC的统一平台来解决异构智能体在相同环境下难以协同与公平比较的问题。其核心方法是构建一个三层架构，将编排、通信与执行分离，并引入关键抽象来实现跨范式集成。

**整体框架与主要模块**：
平台采用三层架构：1）**编排层**：以Qt6主进程作为控制平面，负责启动并监控隔离的worker子进程、通过结构化IPC进行双向通信、路由命令（重置、步进、训练）、聚合实时遥测数据到SQLite数据库，并提供GUI界面进行可视化控制。2）**通信层**：基于轻量级JSON协议通过标准输入/输出与worker子进程通信，支持重置、步进、停止等命令及类型化响应。在批处理模式下，遥测代理（sidecar进程）会解析JSON行、验证版本化模式、转换为Protocol Buffer消息，并通过gRPC流转发给守护进程。3）**执行层**：由多个隔离的worker子进程构成，每个worker封装一个特定的决策框架（如CleanRL、XuanCe、RLlib、BALROG等），并在其原生环境中执行未修改的训练和推理逻辑。

**关键技术组件与创新点**：
1. **基于IPC的worker协议**：通过将不同框架封装为隔离的子进程worker，并使用版本化的进程间协议进行通信，实现了对原生库的零代码修改集成。每个worker通过周期性心跳维持活性，超时则触发故障恢复与检查点还原。
2. **操作员抽象**：通过OperatorLauncher将worker映射到环境中的智能体槽位，为RL策略、LLM、VLM及人类玩家提供统一的智能体级接口。OperatorController协议定义了select_action（顺序模式）和select_actions（并行模式）等方法，使得不同范式的智能体能够以一致的方式交互。
3. **确定性跨范式评估框架**：提供两种互补的评估模式：手动模式允许在共享随机种子下以锁步方式并行推进最多N个操作员，并通过GUI并排显示彩色标记的视口，便于细粒度行为差异的可视化检查；脚本模式则通过声明式Python脚本驱动自动化、长时间运行的评估，生成每步和每回合的JSONL遥测数据，确保实验的可复现性。

这些设计使得MOSAIC能够在一个统一平台中无缝集成异构智能体，支持在相同环境条件下进行公平比较与协同研究。

### Q4: 论文做了哪些实验？

论文通过构建MOSAIC平台，进行了跨范式异构智能体的部署与评估实验。实验设置上，平台采用基于IPC的worker协议，将不同框架（如RL策略、LLM、VLM、人类玩家）封装为隔离的子进程worker，并通过统一的operator抽象接口进行管理。评估框架提供两种模式：手动模式用于在共享随机种子下逐步执行并可视化行为差异；脚本模式则通过声明式Python脚本进行自动化、可重复的长时评估。

数据集与基准测试方面，平台整合了多种现有强化学习环境，例如文中提到的“MosaicMultiGrid-Soccer-2vs2-IndAgObs-v0”等26个环境家族，支持在网格世界、多智能体足球等场景中进行测试。

对比方法上，实验展示了异构智能体团队的配置，例如在一个2v2足球任务中，将训练好的MAPPO策略（RL智能体）与GPT-4o（LLM智能体）组队，对阵另一个RL智能体和一个随机基线策略，以研究跨范式协作。

主要结果与关键指标包括：平台通过了28+个测试文件，覆盖种子可重复性、训练/评估一致性、开销基准测试和动作空间正确性；文档达135+页，并提供了六个嵌入式演示视频，直观展示了跨范式评估过程。这些实验验证了MOSAIC在异构多智能体环境中实现公平、可重复比较的能力。

### Q5: 有什么可以进一步探索的点？

该论文提出的MOSAIC平台在异构智能体统一评估方面迈出了重要一步，但其仍存在一些局限性和值得深入探索的方向。首先，平台目前主要支持回合制或锁步推进的环境，对实时异步交互的复杂多智能体场景（如实时战略游戏、持续物理仿真）的支持有限，未来可扩展其协议以涵盖更广泛的时序模型。其次，评估框架虽强调确定性，但对LLM/VLM这类非确定性模型的严格控制仍具挑战性，例如如何在高层次保证提示工程或模型微调变动下的可比性，需进一步设计更细粒度的控制机制。此外，平台尚未深入涉及智能体间的直接通信与协作机制，未来可集成结构化通信接口，以研究混合范式下的涌现协作行为。从更广阔的视角看，该平台为构建“智能体基准测试生态”奠定了基础，但需推动社区共建更丰富的评估任务与指标，特别是在涉及人类与AI混合团队的场景中，如何量化团队效能、信任度与任务适应性，仍是开放问题。最后，将平台与课程学习、元学习等训练范式结合，实现跨范式的自适应智能体训练，也是一个富有潜力的方向。

### Q6: 总结一下论文的主要内容

该论文提出了MOSAIC平台，旨在解决异构多智能体系统中不同决策范式（如强化学习、大语言模型、视觉语言模型和人类玩家）无法在同一环境中公平比较和协同工作的核心问题。现有框架各自独立，缺乏统一的评估协议，难以在相同条件下进行跨范式的行为对比研究。

论文的核心贡献包括三点：一是设计了一个基于进程间通信的Worker协议，将不同框架封装为独立的子进程，使其无需修改源码即可通信；二是提出了Operator抽象层，为所有类型的智能体提供统一的接口；三是构建了一个确定性的跨范式评估框架，包含用于细粒度行为可视化的手动锁步模式和用于自动化可重复实验的脚本模式。

MOSAIC的意义在于首次实现了在共享环境实例和随机种子下，对异构智能体进行公平、可复现的评估与比较。它支持26种环境家族和8种Worker类型，通过标准化智能体端接口，弥补了Gymnasium等环境标准化工具的不足，为研究混合多智能体协作、零样本协调等提供了关键基础设施。
