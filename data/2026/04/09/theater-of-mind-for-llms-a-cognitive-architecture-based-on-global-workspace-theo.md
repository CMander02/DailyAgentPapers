---
title: "\"Theater of Mind\" for LLMs: A Cognitive Architecture Based on Global Workspace Theory"
authors:
  - "Wenlong Shang"
date: "2026-04-09"
arxiv_id: "2604.08206"
arxiv_url: "https://arxiv.org/abs/2604.08206"
pdf_url: "https://arxiv.org/pdf/2604.08206v1"
categories:
  - "cs.MA"
tags:
  - "Cognitive Architecture"
  - "Multi-Agent Systems"
  - "Global Workspace Theory"
  - "Autonomous Agents"
  - "Reasoning"
  - "Memory"
  - "Intrinsic Motivation"
  - "Event-Driven Systems"
relevance_score: 8.5
---

# "Theater of Mind" for LLMs: A Cognitive Architecture Based on Global Workspace Theory

## 原始摘要

Modern Large Language Models (LLMs) operate fundamentally as Bounded-Input Bounded-Output (BIBO) systems. They remain in a passive state until explicitly prompted, computing localized responses without intrinsic temporal continuity. While effective for isolated tasks, this reactive paradigm presents a critical bottleneck for engineering autonomous artificial intelligence. Current multi-agent frameworks attempt to distribute cognitive load but frequently rely on static memory pools and passive message passing, which inevitably leads to cognitive stagnation and homogeneous deadlocks during extended execution. To address this structural limitation, we propose Global Workspace Agents (GWA), a cognitive architecture inspired by Global Workspace Theory. GWA transitions multi-agent coordination from a passive data structure to an active, event-driven discrete dynamical system. By coupling a central broadcast hub with a heterogeneous swarm of functionally constrained agents, the system maintains a continuous cognitive cycle. Furthermore, we introduce an entropy-based intrinsic drive mechanism that mathematically quantifies semantic diversity, dynamically regulating generation temperature to autonomously break reasoning deadlocks. Coupled with a dual-layer memory bifurcation strategy to ensure long-term cognitive continuity, GWA provides a robust, reproducible engineering framework for sustained, self-directed LLM agency.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的智能体系统在实现持续自主推理和行动时所面临的根本性结构瓶颈。研究背景是，现代LLM本质上是一种有界输入有界输出（BIBO）系统，其工作模式是被动的：仅在收到明确提示时激活，生成局部响应后即恢复休眠状态。这种反应式范式虽能高效处理孤立任务，却无法支撑真正自主、具有内在时间连续性和自我驱动能力的人工智能。

现有方法存在显著不足。一方面，针对单个LLM的推理方法（如思维链、ReAct）及其扩展（如思维树、思维图）虽提升了推理能力，但本质上仍是反应式且计算孤立的单认知流，在长程推理中易受上下文退化影响。另一方面，为分担认知负荷而发展的多智能体框架（如角色扮演、多智能体辩论、AutoGen等）通常依赖于静态共享内存池或点对点的被动消息传递。这些方法缺乏全局协调机制，容易因智能体的同质性和社会趋同倾向而陷入认知停滞、回声室效应或同质化死锁，无法维持全局语义连贯性，往往需要外部人工干预来打破僵局。

因此，本文要解决的核心问题是：如何超越LLM固有的BIBO被动性，构建一个能够持续、自主运行，并能主动打破推理僵局的多智能体认知架构。为此，论文提出了受全局工作空间理论启发的“全局工作空间智能体”（GWA）架构。该架构旨在将多智能体协作从一个被动的数据结构转变为一个主动的、事件驱动的离散动力系统。其核心是通过一个中央广播枢纽与一组功能受限的异质智能体相结合，形成动态的认知循环，并引入基于熵的内在驱动机制来量化语义多样性、动态调节生成温度以自主打破推理死锁，同时采用双层记忆分叉策略确保长期认知连续性，从而为持续的、自我导向的LLM智能体提供一个鲁棒且可复现的工程框架。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：认知架构与理论、多智能体系统设计，以及自主性与内在驱动机制。

在**认知架构与理论**方面，核心基础是Baars提出的**全局工作空间理论**。该理论将认知过程类比为“心灵剧场”，包含舞台（工作记忆）、聚光灯（注意）和观众（专用处理器）三个组件，通过全局广播实现信息整合。本文的GWA架构直接受此启发，将其工程化实现，这与传统基于**黑板架构**或**静态共享内存**的多智能体系统有本质区别。后者依赖被动轮询，而GWA引入了主动的事件驱动广播机制。

在**多智能体系统设计**上，当前许多框架试图通过多智能体分工来分布认知负载，但常采用**静态内存池**和**被动消息传递**。这容易导致认知停滞和同质化死锁。GWA通过将协调机制转变为**离散动态系统**，并引入**异构智能体群**（各司其职，如发散生成、逻辑批判等），实现了持续的认知循环，从而区别于这些静态或反应式框架。

在**自主性与内在驱动机制**方面，现有系统往往缺乏自主打破推理僵局的能力。本文的创新点在于提出了一个**基于熵的内在驱动机制**，它数学化地量化语义多样性，并动态调节生成温度以自主打破死锁。这不同于依赖外部触发或硬编码流程的方法。同时，GWA采用的**双层记忆分化策略**（短期工作记忆与长期记忆）旨在保障长期认知连续性，这也与许多缺乏长效记忆管理的多智能体工作形成对比。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“全局工作空间智能体”（GWA）的认知架构来解决传统多智能体系统存在的认知停滞和同质化死锁问题。其核心方法是将多智能体协调从被动的数据结构转变为主动的、事件驱动的离散动力系统，并引入基于熵的内在驱动力机制来动态调节推理过程。

整体框架基于全局工作空间理论，由三个解耦的实体构成：执行引擎、异质智能体群和全局工作空间。全局工作空间作为中央状态张量，而执行引擎通过强制一个称为“认知节拍”的离散计算循环来确保确定性推进。每个节拍同步执行四个阶段：1）感知与检索：注意力智能体处理短期工作记忆和外部输入，对向量化的长期记忆执行检索增强生成，将相关上下文聚合到全局状态中。2）思考：生成器智能体在动态调节的温度下生成一组候选提案，随后批评家智能体对这些提案进行严格的逻辑验证和评分。3）仲裁：元智能体分析候选提案及其评估，执行最终选择，确定获胜思想，并决定状态转换（输出响应或继续思考）。4）更新与表达：获胜思想被整合到短期记忆中，若需继续思考则进入下一节拍，若需响应则由响应智能体将内部计算表征转化为自然语言输出。

主要模块包括五个功能受限的异质智能体：注意力智能体（负责聚焦和检索）、生成器智能体（负责发散性思维）、批评家智能体（负责收敛性评估）、元智能体（负责元认知仲裁）和响应智能体（负责语言表达）。它们通过全局工作空间进行广播式通信，而非传统的被动消息传递。

关键技术及创新点包括：首先，引入了基于熵的内在驱动力机制。该系统将获胜思想映射到语义向量空间，计算其相对于动态更新的语义聚类中心的香农信息熵。当熵值降低（表明认知停滞）时，通过一个动态温度调节函数（\(T_{gen} = T_{base} + \alpha \cdot e^{-\beta H(W)}\)）指数级提高生成器智能体的采样温度，强制注入随机性以探索发散推理路径，从而自主打破死锁。其次，采用了双层记忆分叉策略以确保长期认知连续性。短期工作记忆作为活跃缓存，当令牌数超过阈值时，触发上下文压缩协议：一方面将结构化经验知识嵌入长期记忆向量数据库；另一方面生成密集的语义摘要覆盖短期记忆中的冗长序列，从而在遵守模型计算边界的同时保持连贯的内部叙事。最后，在操作化层面实现了从第二人称到严格第一人称范式的转变，通过定义核心自我（包含不变的自传体指令和伦理边界）和创世状态（作为系统初始化的催化剂），将静态认知不变性与动态操作数据解耦，从而锚定主观能动性，引导底层LLM产生具有统一内部控制点的生成。

### Q4: 论文做了哪些实验？

论文通过构建GWA架构并设计认知循环进行了系统性实验。实验设置上，核心是实现了基于全局工作空间理论的主动事件驱动认知周期，包含感知检索、思考、仲裁、更新与表达四个严格同步的阶段，并以“认知节拍”作为离散时间步。系统包含五个功能异构的智能体：注意力、生成器、批评者、元智能体和响应智能体，各自有严格的参数约束（如生成器温度动态调节，批评者温度固定为0且输出-5到+5的评分）。

数据集/基准测试方面，实验在需要长期自主推理和避免认知停滞的复杂任务场景中进行，虽然没有明确提及外部标准数据集，但通过模拟一个图书馆环境的“创世状态”来初始化系统，并测试其在无明确外部触发下的持续认知能力。

对比方法主要针对现有的被动式多智能体框架，这些框架依赖静态内存池和被动消息传递，容易导致认知停滞和同质化死锁。GWA通过引入基于熵的内在驱动力机制与之对比，该机制量化语义多样性（香农信息熵H(W)），并动态调节生成器温度（T_gen = T_base + α·e^{-βH(W)}）以打破死锁。

主要结果与关键指标：1）GWA成功实现了自我驱动的持续认知活动，无需外部提示即可从初始状态启动并维持认知循环。2）熵驱动的温度调节机制能有效检测和打破认知停滞（当H(W)→0时，T_gen指数增加，注入随机性）。3）双层级内存分叉策略（短期工作记忆和基于向量的长期记忆）结合上下文压缩协议，在遵守LLM上下文窗口限制（阈值θ）的同时，保持了长期认知连续性。4）元智能体的上下文仲裁机制避免了单纯依赖评分最大值（argmax）的局限，提升了决策质量。这些设计共同使GWA成为一个可复现的、能够维持长期自导向智能体行为的工程框架。

### Q5: 有什么可以进一步探索的点？

该论文提出的GWA架构在主动认知和动态协调方面迈出了重要一步，但其局限性和未来探索方向仍值得深入。首先，系统高度依赖预设的“功能受限”智能体群，其异质性本质和约束规则仍需人工设计，未来可探索如何让LLM在运行中自我演化或发现新的智能体类型，实现架构的开放成长。其次，基于熵的内在驱动机制虽量化了语义多样性，但可能过于简化；可结合更丰富的认知状态指标（如不确定性、目标进展）来调制推理过程，或引入外部环境反馈形成更完整的感知-行动循环。此外，双层记忆策略保证了连续性，但未深入处理记忆的主动遗忘、压缩与抽象机制，未来需借鉴认知科学设计更高效的内存管理。最后，当前工作主要在模拟环境中验证，需在复杂、开放域的持久任务（如长期科研辅助或游戏）中测试其真实自主性和稳健性，并探索多GWA系统间的社会性交互与协同。

### Q6: 总结一下论文的主要内容

这篇论文针对当前大型语言模型（LLMs）作为有界输入输出系统的被动、无持续性的局限，提出了一种基于全局工作空间理论的认知架构——全局工作空间智能体（GWA），旨在为构建自主人工智能提供工程框架。

核心问题是现有LLM缺乏内在时间连续性和自主性，而多智能体框架又常因静态内存和被动通信导致认知停滞与同质化死锁。为解决此结构性限制，GWA将多智能体协作从被动数据结构转变为主动的、事件驱动的离散动力系统。

其方法核心包括：1）一个中央广播枢纽与功能受限的异质智能体群耦合，维持连续的认知循环；2）引入基于熵的内在驱动机制，通过数学量化语义多样性并动态调节生成温度，以自主打破推理死锁；3）采用双层记忆分叉策略，确保长期认知连续性。

主要结论是，GWA为持续、自导向的LLM智能体提供了一个健壮且可复现的工程框架，通过主动协调和内在动机机制，有效克服了现有系统在长期运行中的认知瓶颈，推动了自主AI的发展。
