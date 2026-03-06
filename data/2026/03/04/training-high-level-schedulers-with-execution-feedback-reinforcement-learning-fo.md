---
title: "Training High-Level Schedulers with Execution-Feedback Reinforcement Learning for Long-Horizon GUI Automation"
authors:
  - "Zehao Deng"
  - "Tianjie Ju"
  - "Zheng Wu"
  - "Zhuosheng Zhang"
  - "Gongshen Liu"
date: "2025-11-27"
arxiv_id: "2511.22235"
arxiv_url: "https://arxiv.org/abs/2511.22235"
pdf_url: "https://arxiv.org/pdf/2511.22235v2"
github_url: "https://github.com/hehehahi4/CES"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "Agent架构"
  - "任务规划"
  - "状态管理"
  - "强化学习"
  - "GUI自动化"
  - "长视野任务"
relevance_score: 9.0
---

# Training High-Level Schedulers with Execution-Feedback Reinforcement Learning for Long-Horizon GUI Automation

## 原始摘要

The rapid development of large vision-language model (VLM) has greatly promoted the research of GUI agent. However, GUI agents still face significant challenges in handling long-horizon tasks. First, single-agent models struggle to balance high-level capabilities and low-level execution capability, facing prevalent issues of responsibility coupling and capability conflicts. Second, agents lack awareness of the task state, leading to progress loss in long-horizon tasks. To address these challenges, we propose a staged execution-feedback reinforcement learning algorithm. Unlike training a unified policy model, we focus on training high-level scheduling models. Specifically, we propose and train two agents: a Coordinator, responsible for the strategic planning and task decomposition; and a State Tracker, responsible for context compression and information management to maintain the task's state and coherence. Based on this, we built the Coordinator-Executor-State Tracker (CES) multi-agent framework, which can be integrated with any low-level Executor model, assisting the Executor in solving long-horizon tasks through task scheduling and state management. Experiments on long-horizon task benchmarks demonstrate that CES significantly enhances the system's planning and state management capabilities. Furthermore, analysis confirms that our trained high-level scheduling module is a generalizable, plug-and-play module that significantly enhances the long-horizon capabilities of various Executors. Code can be available at https://github.com/hehehahi4/CES.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决图形用户界面（GUI）智能体在执行长周期任务时面临的核心挑战。研究背景是，尽管大型视觉语言模型（VLM）的发展推动了GUI智能体的研究，但现有方法在应对需要多步骤、长时间交互的复杂任务时仍存在显著不足。

现有方法的不足主要体现在两个方面：首先，主流方法通常采用单智能体端到端架构，试图将高层能力（如任务规划、进度跟踪）和低层能力（如界面元素定位、动作执行）耦合在一个统一的策略网络中。这种设计导致模型参数有限，难以同时精通异构能力，随着任务复杂度增加，容易引发责任耦合和能力冲突，甚至导致模型能力崩溃。其次，现有智能体缺乏有效的任务状态感知能力。它们主要依赖历史动作序列或当前屏幕截图来推断进度，但这些低层动作或视觉信息语义不足、不可靠，使得智能体在长周期任务中难以准确判断当前进展，容易出错或丢失进度。

因此，本文要解决的核心问题是：如何通过一种新的框架和训练方法，有效解耦GUI智能体的高层规划与低层执行能力，并增强其对任务状态的感知与管理，从而提升其在长周期任务中的鲁棒性和性能。为此，论文提出了分阶段的执行反馈强化学习算法，并构建了协调器-执行器-状态跟踪器（CES）多智能体框架，专注于训练可插拔的高层调度模块（协调器和状态跟踪器），以协助任何低层执行器模型更好地处理长周期任务。

### Q2: 有哪些相关研究？

本文的相关研究可分为方法类和应用类。在方法类中，传统方法依赖规则或意图驱动的API，但泛化性差。随着视觉语言模型（VLM）的发展，研究转向纯视觉范式，早期常用监督微调（SFT），但其依赖标注数据且泛化不足。近期研究转向强化学习（RL），如采用GRPO算法的GUI-R1，以增强决策能力，但这些单智能体方法仍存在能力过载和优化冲突问题。在应用类中，多智能体系统通过分工协作处理复杂任务，例如Mobile-Agent-v3和MobiAgent，但它们通常基于提示工程分配角色，缺乏对各角色的深度优化，且常忽视长视野任务中的状态管理。

本文与这些工作的关系在于，它继承了RL增强决策和多智能体分工的思路，但关键区别在于：1）针对单智能体能力耦合问题，本文通过架构创新，彻底解耦高层规划与底层执行，提出专有的协调器和状态跟踪器；2）相比现有多智能体系统仅用提示工程，本文采用执行反馈的RL专门训练高层调度模块，实现深度优化；3）引入了专门的状态跟踪器进行信息压缩和管理，解决了长视野任务中进度丢失的问题。因此，本文的CES框架是一个可插拔的通用高层调度模块，显著提升了执行器的长视野任务能力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为CES（Coordinator-Executor-State Tracker）的多智能体框架，并采用分阶段的执行反馈强化学习算法来解决长视野GUI自动化任务中的挑战。核心方法是将复杂的端到端决策过程分解为结构化的多智能体协作循环，从而分离高层规划与底层执行，并增强任务状态感知。

整体框架包含三个主要模块：**Coordinator**（协调器）、**Executor**（执行器）和**State Tracker**（状态跟踪器）。它们以循环信息流方式协作：协调器基于状态跟踪器提供的状态进行规划，生成原子指令；执行器严格遵循该指令在界面上执行操作；状态跟踪器则根据执行结果更新压缩后的任务状态，供下一轮规划使用。这种设计灵感来源于现代操作系统，协调器充当“CPU”负责战略规划，执行器作为“I/O设备”负责精确动作，状态跟踪器则作为“动态内存”管理任务状态。

关键技术包括：1）**模块化职责分离**：协调器专注于将用户高级指令分解为可执行的原子步骤，并能在出错时反思和重规划；执行器被设计为冻结、可替换的组件，仅负责将原子指令转化为界面操作，无需理解长期意图；状态跟踪器通过语言模型动态压缩历史上下文，将高维视觉状态转化为低维、高语义的自然语言摘要，有效解决长任务中的上下文丢失问题。2）**分阶段执行反馈强化学习**：采用两阶段训练策略优化高层调度模型。第一阶段使用冻结的执行器和真实标注的状态，通过执行反馈奖励（Execution-Feedback Reward）单独训练协调器的规划能力；第二阶段冻结训练好的协调器，利用同样的奖励信号专门优化状态跟踪器的状态演化能力，使其生成对协调器决策最有用的状态信息。奖励函数基于执行器的动作结果客观计算，避免了直接评估抽象中间输出的困难。3）**通用性与即插即用**：框架允许集成任何强大的预训练GUI模型作为执行器，而协调器和状态跟踪器作为可训练的高层调度模块，能显著提升不同执行器在长视野任务上的性能。

创新点在于：提出了一个受操作系统启发的多智能体架构，彻底解耦了规划与执行；设计了基于执行反馈的分阶段RL算法，使高层智能体的训练目标与最终任务成功对齐；并通过状态跟踪器的自然语言状态压缩，有效维持了长任务中的连贯性与进度感知。实验表明，该框架能显著提升系统在多个长视野任务基准上的规划与状态管理能力。

### Q4: 论文做了哪些实验？

论文在三个长视野GUI任务基准测试（AITZ、AMEX和GUI-Odyssey，平均步骤数分别为7.5、12.8和15.3）上进行了实验，评估了所提出的CES多智能体框架。实验设置方面，Coordinator和State Tracker分别基于Qwen2.5-VL-7B和Qwen3-4B模型，采用分阶段的执行反馈强化学习进行训练（包括SFT预热和RL优化），并使用GUI-R1-7B作为执行器来计算奖励函数。

主要对比方法包括：1) 基线方法（直接使用执行器模型）；2) CES-P（通过提示让同一基础模型扮演CES中的所有角色）；3) 完整的CES框架（使用专门训练的Coordinator和State Tracker）。评估指标包括动作类型预测准确率（Type）、点击点预测准确率（GR）和任务成功率（SR）。

关键结果显示，CES框架显著提升了性能。在GUI-R1-7B执行器基础上，CES将Type准确率平均提升了10.38%。消融实验表明，移除Coordinator会导致GUI-Odyssey上的SR下降12.77%，移除State Tracker或仅使用SFT（无RL）也会导致性能显著下降。此外，框架展现了良好的通用性：当使用不同规模的执行器模型（如UI-R1-3B、GUI-Owl-7B和GUI-Owl-32B）时，CES均带来了稳定且大幅的性能提升。例如，在GUI-Odyssey上，CES将GUI-Owl-32B的SR从39.60%提升至56.75%，将GUI-Owl-7B的SR从37.53%提升至46.65%。失败案例分析进一步显示，CES框架几乎完全消除了状态丢失错误（从14%降至2%）和规划错误（从12%降至4%），将性能瓶颈转移到了执行器本身的感知能力上。

### Q5: 有什么可以进一步探索的点？

本文提出的CES框架在解耦高层规划与底层执行、引入状态跟踪器方面取得了显著进展，但其探索空间依然广阔。局限性在于：1）高层调度器与底层执行器的训练仍是分离的，未能实现端到端的协同优化，可能限制整体策略的收敛效率；2）状态跟踪器依赖于人工设计的反馈信号进行训练，在更复杂的动态环境中可能无法充分捕捉任务进度的细微变化。

未来研究方向可包括：1）探索高层调度器与底层执行器的联合训练机制，通过共享表征或交替优化，使多智能体系统能更协同地适应复杂任务流；2）增强状态跟踪器的泛化能力，例如引入基于世界模型的预测模块，使其能主动推断未观测到的任务状态变化；3）将框架扩展至多模态交互场景（如结合语音指令），并探索在资源受限设备上的轻量化部署方案。此外，如何让系统从少量人类示范中快速学习新任务，也是提升实用性的关键。

### Q6: 总结一下论文的主要内容

该论文针对GUI智能体在长周期任务中面临的挑战，提出了一种基于执行反馈强化学习的高层调度器训练方法。核心问题是单一智能体难以兼顾高层规划与底层执行能力，且缺乏任务状态感知，导致长任务中责任耦合与进度丢失。为解决这些问题，作者设计了Coordinator-Executor-State Tracker（CES）多智能体框架：Coordinator负责战略规划与任务分解，State Tracker负责上下文压缩与信息管理以维持任务状态连贯性，而底层Executor则专注于具体动作执行。方法上，论文采用分阶段的执行反馈强化学习，重点训练高层调度模型（Coordinator和State Tracker），而非统一的策略模型，使该框架能与任意底层Executor模型集成。实验表明，CES显著提升了系统在长周期任务基准上的规划与状态管理能力，且训练出的高层调度模块具有通用性和即插即用特性，能有效增强不同Executor的长周期任务处理能力。
