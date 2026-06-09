---
title: "SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks"
authors:
  - "Hongcheng Gao"
  - "Hailong Qu"
  - "Jingyi Tang"
  - "Jiahao Wang"
  - "Zihao Huang"
  - "Hengkang Qiao"
  - "Shihong Huang"
  - "Junming Yang"
  - "Yi Li"
  - "Hongyixuan Yuan"
  - "Wenjie Li"
  - "Bohan Zeng"
  - "Wenbo Li"
  - "Bo Wang"
  - "Jianhui Liu"
  - "Olive Huang"
  - "Haoyang Huang"
  - "Wentao Zhang"
  - "Guoqing Huang"
  - "Nan Duan"
date: "2026-06-08"
arxiv_id: "2606.09669"
arxiv_url: "https://arxiv.org/abs/2606.09669"
pdf_url: "https://arxiv.org/pdf/2606.09669v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "空间推理基准"
  - "多模态智能体"
  - "交互式理解"
  - "任务成功率"
  - "具身智能"
  - "主动探索"
  - "长期规划"
relevance_score: 9.5
---

# SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks

## 原始摘要

Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有空间推理基准无法有效评估多模态大语言模型（MLLM）在真实世界中交互式空间理解能力的问题。当前研究背景中，空间推理是MLLM感知和操作物理世界的基础能力，但现有基准主要采用被动评估范式，如静态视觉问答或预录视频理解，只能测试模型对空间关系、物体布局等基本理解，无法捕捉真实环境中交互式和动态的空间理解本质。此外，已有具身基准多围绕特定模拟器设计，其传感器假设、动作接口和执行流程与特定环境深度耦合，导致任务成功与否难以反映通用交互式空间推理能力，而更多是模型对特定模拟器或动作空间的适应。

本文要解决的核心问题是：构建一个统一、模拟器无关的基准，以严格评估离线多模态模型在仅有第一人称视觉观察、无额外传感器信息的情况下，通过文本动作接口进行主动探索和闭环决策，在多种异构3D环境中完成复杂真实世界任务的能力。该基准需具备视觉部分可观测性、MLLM原生文本动作空间、以及跨模拟器统一协议等关键属性，从而排除低级模拟器特性的干扰，真正聚焦于模型基于视觉观察和指令的主动探索与决策能力。

### Q2: 有哪些相关研究？

- **评测基准类**：相关工作包括基于被动视觉问答（VQA）的静态空间推理数据集（如SQA3D、ScanQA等）以及面向特定模拟器的交互式评测平台（如Habitat、AI2-THOR）。本文提出的SpatialWorld与这些工作的核心区别在于：1）摒弃被动评估，要求智能体在视觉部分可观测条件下主动探索并执行任务；2）提供统一的、与模拟器无关的协议，支持8种异构仿真后端，避免以往单一模拟器导致的泛化性不足。

- **方法与框架类**：多模态智能体相关工作包括改进底层模型（如视觉-语言对齐）和开发交互框架（如ReAct、SayCan）。本文不聚焦于单一方法，而是通过设计需要“主动探索”和“长程规划”的760个跨领域任务，暴露现有模型（如GPT-5成功率仅17.4%）在交互式空间推理中的瓶颈，为未来方法评估提供严格测试床。

- **应用与模拟器类**：3D仿真平台（如ThreeDWorld、iGibson）虽支持空间任务，但多限定在特定场景。SpatialWorld覆盖家庭、旅行、社交协作等多样化真实世界任务，并引入人类验证的初始状态、参考轨迹和终止状态验证器，确保评测的可靠性。

### Q3: 论文如何解决这个问题？

SpatialWorld通过构建统一的交互式基准框架来解决现有评估无法有效衡量多模态智能体在真实世界中主动空间推理能力的问题。核心是将任务形式化为纯视觉的部分可观测马尔可夫决策过程(POMDP)，智能体仅能接收第一人称的RGB图像作为观测量，无法获得深度图、地图等特权状态信息，这确保了评估完全基于视觉感知与推理的耦合。

在架构设计上，SpatialWorld提出了模块化的五组件系统。其关键创新是统一的观察-动作接口：观察接口将八个异构的仿真后端（如AI2-THOR、CARLA、3D游戏等）标准化为统一的单目RGB观察；动作接口则定义了四类高层符号化动作（导航、视角与姿态、交互、任务控制与协调），这些抽象动作通过映射模块转化为各仿真器特定的执行代码，使通用多模态大语言模型无需微调即可直接进行评估。

数据构建方面，SpatialWorld涵盖了家庭、工作、娱乐、旅行和社交协作五个场景类别，共760个人工标注任务。每项任务包含初始状态、参考轨迹和基于终端状态验证的成功条件。评估采用任务成功率(TSR)和步骤效率(SE)两个互补指标，前者验证最终目标是否达成，后者衡量成功任务中的执行效率。实验显示，最强模型GPT-5的TSR仅为17.4%，证明主动探索和长程规划仍是主要瓶颈。

### Q4: 论文做了哪些实验？

论文基于SpatialWorld基准进行了全面的实验评估。实验设置上，对15个前沿多模态大模型（包括Qwen、GLM、Kimi、Gemini、GPT及豆包系列）进行了零样本评估，不进行特定任务微调。模型在每一步仅接收第一人称RGB截图和自然语言任务描述，并使用统一的文本动作接口。评估采用了温度τ=1.0，保留最近30轮交互作为上下文，并设置了2g+10的动态步数预算。

实验使用了SpatialWorld基准的760个人工标注任务，覆盖了8个异构仿真环境，包括日常、工作、娱乐、旅行和社交等物理域，以及数字游戏域。对比方法即为上述15个模型。主要结果通过任务成功率（TSR）和解决方案效率（SE）两个指标报告。

核心结果表明，交互式空间推理对当前模型极具挑战性。最佳模型GPT-5的平均TSR仅为17.4%，而领先的开源模型Qwen-3.5-397B-A17B达到14.1%。分析还发现TSR与SE之间存在明显不匹配，如GPT-5.4（TSR 6.6%）的SE（0.569）高于Kimi-K2.5（TSR 9.2%的SE 0.486），说明后者依赖大量试错。此外，模型在不同领域表现差异显著，GPT-5在物理域室内场景领先（14.1%），而Gemini系列在室外导航更优（9.0%）；在需要精细操作与长期规划结合的任务（导航-交互模式）中，平均TSR低至4.2%，远低于纯交互任务（50.2%）。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在：静态VQA和模拟器特异性评估无法衡量真实交互场景中的空间推理能力。未来可探索以下几个方向：
1. 基于SpatialWorld的8个异构模拟后端框架，设计跨场景迁移学习策略，增强智能体对未知环境的泛化能力。
2. 针对GPT-5仅17.4%任务成功率暴露的主动探索缺陷，可尝试引入层级化空间记忆机制，结合拓扑地图与语义锚点来优化视觉导航路径。
3. 面向执行效率与任务成功度不匹配的问题，开发动态约束优化算法，在长时域规划中平衡探索深度与计算预算。
4. 考虑将本体知识图谱嵌入解耦式多模态架构，使语言模块与空间推理模块形成双向注意力协同，缓解领域特异性性能波动。

### Q6: 总结一下论文的主要内容

论文提出了SpatialWorld，一个专门评估多模态智能体在真实世界任务中的交互式空间推理能力的统一基准。现有基准依赖静态VQA或特定模拟器，无法测试通用的交互式空间理解。SpatialWorld整合了8种异构模拟器，包含760个人工标注任务，涵盖家务、旅行、社交等领域。智能体需要在仅视觉部分可观察条件下，通过原生文本动作接口主动收集证据并决策。每个任务配有经过验证的初始状态、参考轨迹和终点验证器。评估15个先进智能体发现：最强的GPT-5平均任务成功率仅17.4%，开源最好的Qwen-3.5达14.1%。分析揭示任务成功与执行效率不匹配，且存在显著领域差异。这些在主动探索和长程规划中的瓶颈将SpatialWorld定位为未来空间智能体的严格测试平台。
