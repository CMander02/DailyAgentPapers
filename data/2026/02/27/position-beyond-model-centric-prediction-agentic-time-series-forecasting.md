---
title: "Position: Beyond Model-Centric Prediction -- Agentic Time Series Forecasting"
authors:
  - "Mingyue Cheng"
  - "Xiaoyu Tao"
  - "Qi Liu"
  - "Ze Guo"
  - "Enhong Chen"
date: "2026-02-02"
arxiv_id: "2602.01776"
arxiv_url: "https://arxiv.org/abs/2602.01776"
pdf_url: "https://arxiv.org/pdf/2602.01776v2"
categories:
  - "cs.LG"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 5.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "Survey/Position Paper"
attributes:
  base_model: "N/A"
  key_technique: "Agentic Time Series Forecasting (ATSF)"
  primary_benchmark: "N/A"
---

# Position: Beyond Model-Centric Prediction -- Agentic Time Series Forecasting

## 原始摘要

Time series forecasting has traditionally been formulated as a model-centric, static, and single-pass prediction problem that maps historical observations to future values. While this paradigm has driven substantial progress, it proves insufficient in adaptive and multi-turn settings where forecasting requires informative feature extraction, reasoning-driven inference, iterative refinement, and continual adaptation over time. In this paper, we argue for agentic time series forecasting (ATSF), which reframes forecasting as an agentic process composed of perception, planning, action, reflection, and memory. Rather than focusing solely on predictive models, ATSF emphasizes organizing forecasting as an agentic workflow that can interact with tools, incorporate feedback from outcomes, and evolve through experience accumulation. We outline three representative implementation paradigms -- workflow-based design, agentic reinforcement learning, and a hybrid agentic workflow paradigm -- and discuss the opportunities and challenges that arise when shifting from model-centric prediction to agentic forecasting. Together, this position aims to establish agentic forecasting as a foundation for future research at the intersection of time series forecasting.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决传统时间序列预测范式在现实自适应、多轮次场景下的局限性问题。研究背景是，时间序列预测在能源、医疗、金融等关键领域是决策的核心依据，其价值不仅在于预测精度，更在于如何有效支持动态、不确定环境下的决策过程。然而，现有方法主要遵循“模型中心”范式，将预测简化为一个静态、单次执行的监督学习问题，即用固定模型将历史观测值映射为未来值。该范式虽推动了模型架构和表示学习的进步，但其根本不足在于与真实预测实践存在“结构性错配”。现实中的预测往往是自适应、多轮次的，涉及特征提取、推理、迭代修正和持续演化等多个步骤，而传统范式将这些环节隐含或割裂，仅聚焦于最终预测模型的性能。

因此，本文要解决的核心问题是：如何超越单一的“模型中心”预测，构建一个能更好地匹配现实预测活动动态性、交互性与演进性的新范式。为此，论文提出了“智能体化时间序列预测”（ATSF）这一概念性重构，将预测重新定义为一种由感知、规划、行动、反思和记忆等环节组成的智能体过程。ATSF的核心是强调将预测组织为一个能与工具交互、融入结果反馈、并通过经验积累不断演进的智能体工作流，从而将研究焦点从模型执行转向过程组织，以支撑未来在不确定和变化环境中的有效决策。

### Q2: 有哪些相关研究？

本文提出的“代理化时间序列预测”（ATSF）与多个领域的研究相关，主要可归纳为以下几类：

**1. 大规模与基础模型研究**：近年来，以大规模预训练模型为代表的研究显著提升了预测模型的表征和学习能力。然而，这些模型通常遵循**单次执行范式**，即一次性输入历史数据并输出预测。ATSF与模型规模是正交的，它并不旨在替换这些预测模型，而是**将预测重新定义为一种显式的、包含多环节的决策过程**（如规划、反思、记忆），从而在**不改变底层预测模型**的情况下，实现预测行为的动态演进和适应。

**2. 复杂预测流程与自动化工作流**：传统的时间序列预测流程通常由**静态的执行图**定义，包含一系列预定义的操作步骤。ATSF与此类工作流有相似之处，但核心区别在于其**动态性和决策自主性**。ATSF将预测视为一个动态决策过程，能够根据情境自适应地控制上下文选择、工具使用和结果修正，这依赖于迭代式的规划和反思，而非固定的流程图。

**3. 在线学习与自适应建模**：这类方法主要关注数据分布非平稳性，通过**增量更新模型参数**来实现自适应。ATSF与这些方法是**互补关系**。ATSF的侧重点不在于模型参数的在线调整，而在于通过引入**显式的记忆和反思机制**，实现**经验积累、策略修订和行为层面的整体适应**，其适应单元是整个预测过程而不仅仅是模型参数。

综上，ATSF并非替代现有模型或方法，而是一种**概念上的重构**。它将预测从单一的模型中心任务，提升为一个由代理驱动的、可交互、可迭代、可积累经验的**系统性工作流程**，为应对自适应、多轮次的复杂预测场景提供了新的基础框架。

### Q3: 论文如何解决这个问题？

论文通过提出“智能体化时间序列预测”这一全新范式来解决传统模型中心预测在自适应、多轮次场景下的不足。其核心方法是将预测重构为一个由感知、规划、行动、反思和记忆组成的迭代决策过程，而非单一的静态映射函数。

整体框架围绕上述五个核心组件构建一个闭环的工作流。感知模块负责从原始异构数据中动态提取与当前任务相关的信息，形成内部表征，其创新点在于将感知视为一个依赖于上下文和任务的适应性认知过程，而非固定预处理。规划模块则基于感知到的上下文，动态制定预测目标、分解复杂任务并确定高层策略，其关键特性是支持动态重规划以响应新信息。行动模块是决策的执行层，通过自主调用各类预测工具（如统计模型、机器学习方法）来准备证据和生成预测，其创新在于将预测本身视为行动空间中的一种操作，并区分了并行（高效探索）与序列（审慎推理）两种执行模式。反思模块作为内部自我评估机制，对预测结果进行质量评估、不确定性分析，并触发修正需求，从而支持预测的迭代优化。记忆模块则实现跨实例的经验积累与持续演化，通过动态更新和分层检索（实例级、任务级、领域级）机制，使系统能够利用历史经验指导未来决策。

论文进一步阐述了三种具体的实现范式。基于工作流的设计通过预定义的有向无环图或标准操作流程来显式组织上述认知步骤，优点是高可解释性和稳定性，但灵活性有限。智能体强化学习范式将预测决策过程建模为强化学习问题，通过试错和奖励反馈来优化规划、行动选择等行为，能自主演化出新颖策略，但存在训练不稳定和样本效率低的挑战。混合智能体工作流范式则融合了前两者的优势，在保持整体工作流结构明确和可解释的同时，在关键决策点（如上下文选择、策略切换）嵌入局部强化学习进行自适应调整，从而在稳定性与灵活性之间取得平衡。这些范式共同的核心创新是从根本上将研究焦点从模型设计转向预测过程的组织与协调，强调通过智能体的认知循环和与环境的多轮交互来实现持续适应与改进。

### Q4: 论文做了哪些实验？

论文提出了三种代理时间序列预测（ATSF）的实现范式，并进行了概念性的比较分析，而非基于具体数据集的传统实验。实验设置侧重于从机制层面对比不同范式的核心原理与特性。研究通过一个对比表格，系统评估了工作流范式、代理强化学习范式和混合代理工作流范式这三种策略。

在数据集/基准测试方面，论文未使用特定的时间序列数据集进行实证性能评测，而是将不同范式本身作为“测试对象”，在概念层面分析其适应不同预测场景的潜力。

对比方法即上述三种实现范式。主要结果通过对比表格呈现，总结了各范式的核心机制、优势与弱点。关键数据指标体现在定性分析上：工作流范式具有高可解释性、稳定性和易调试性；代理强化学习范式能自主演化并发现新策略，但存在训练不稳定、样本效率低和难以解释的问题；混合代理工作流范式旨在平衡稳定性与适应性，支持持续改进，但其架构复杂且难以调优。

因此，实验的核心结果是论证了从模型中心预测转向代理预测时，不同实现路径在灵活性、稳定性、可解释性等方面存在的权衡，为后续研究奠定了概念基础。

### Q5: 有什么可以进一步探索的点？

基于论文提出的“代理式时间序列预测”新范式，其局限性与未来研究方向可从多个维度进一步探索。首先，在系统设计层面，如何设计高效且可泛化的记忆机制以支持经验的积累与迁移仍是一个核心挑战。未来的研究可以探索分层或图结构的记忆网络，结合元学习来提升跨场景的适应能力，并引入遗忘或置信度机制来防止过时经验的干扰。其次，在工具集成与标准化方面，当前缺乏统一的工具接口与语义规范，导致系统脆弱且难以扩展。可借鉴软件工程中的模块化思想，建立开放、可验证的工具库，并设计领域特定的描述语言来提升互操作性。此外，在多智能体协同中，角色分配、信用评估与冲突消解等问题尚未解决，可引入博弈论或基于学习的协调策略，并结合可解释性技术来明晰各代理的贡献。最后，在可靠性与部署层面，需开发不确定性感知的推理框架，使代理能动态权衡探索与利用，并在计算效率与预测质量间取得平衡。例如，可设计轻量级触发机制，仅在关键决策点激活深度推理，从而兼顾实时性与自适应性。这些方向共同指向从封闭的模型优化转向开放、协同且可信的智能预测生态系统。

### Q6: 总结一下论文的主要内容

本文提出了一种新的时间序列预测范式——智能体化时间序列预测（ATSF），旨在超越传统以模型为中心的静态、单次预测框架。传统方法将预测视为从历史观测值到未来值的直接映射，但在需要自适应、多轮交互的现实场景中，这种范式在特征提取、推理、迭代优化和持续适应方面存在不足。ATSF将预测重构为一个由感知、规划、行动、反思和记忆组成的智能体过程，强调将预测组织为一种能与工具交互、整合结果反馈并通过经验积累进化的智能工作流。论文概述了三种代表性实现范式：基于工作流的设计、智能体强化学习以及混合智能体工作流范式，并讨论了从模型中心预测转向智能体预测所面临的机遇与挑战。核心结论是，ATSF能够构建更灵活、可解释且与决策过程对齐的预测系统，为时间序列预测的未来研究奠定了新的方向。
