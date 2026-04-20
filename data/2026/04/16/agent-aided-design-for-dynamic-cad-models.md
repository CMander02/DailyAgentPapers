---
title: "Agent-Aided Design for Dynamic CAD Models"
authors:
  - "Mitch Adler"
  - "Matthew Russo"
  - "Michael Cafarella"
date: "2026-04-16"
arxiv_id: "2604.15184"
arxiv_url: "https://arxiv.org/abs/2604.15184"
pdf_url: "https://arxiv.org/pdf/2604.15184v1"
categories:
  - "cs.AI"
tags:
  - "Agent-Aided Design"
  - "Tool Use"
  - "Visual Feedback"
  - "Code Generation"
  - "CAD"
  - "Iterative Refinement"
  - "Constraint Solver"
  - "3D Assembly"
relevance_score: 7.5
---

# Agent-Aided Design for Dynamic CAD Models

## 原始摘要

In the past year, researchers have started to create agentic systems that can design real-world CAD-style objects in a training-free setting, a new variety of system that we call Agent-Aided Design. Generally speaking, these systems place an agent in a feedback loop in which it can write code, compile that code to an assembly of CAD model(s), visualize the model, and then iteratively refine its code based on visual and other feedback. Despite rapid progress, a key problem remains: none of these systems can build complex 3D assemblies with moving parts. For example, no existing system can build a piston, a pendulum, or even a pair of scissors. In order for Agent-Aided Design to make a real impact in industrial manufacturing, we need a system that is capable of generating such 3D assemblies. In this paper we present a prototype of AADvark, an agentic system designed for this task. Unlike previous state-of-the-art systems, AADvark captures the dynamic part interactions with one or more degrees-of-freedom. This design decision allows AADvark to reason directly about assemblies with moving parts and can thereby achieve cross-cutting goals, including but not limited to mechanical movements. Unfortunately, current LLMs are imperfect spatial reasoners, a problem that AADvark addresses by incorporating external constraint solver tools with a specialized visual feedback mechanism. We demonstrate that, by modifying the agent's tools (FreeCAD and the assembly solver), we are able to create a strong verification signal which enables our system to build 3D assemblies with movable parts.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI辅助CAD设计系统无法生成具有可动部件的复杂三维装配体这一核心问题。研究背景是，随着大语言模型和智能体系统的发展，研究者开始探索无需训练即可设计现实世界CAD对象的智能体辅助设计系统。这些系统通常让智能体处于一个反馈循环中：编写代码、编译为CAD模型、可视化模型，并根据视觉和其他反馈迭代优化代码。

然而，现有方法存在明显不足。尽管这些系统在静态CAD模型生成上取得了先进成果，但它们均无法处理带有关节和运动部件的动态装配体。例如，现有系统无法创建一个功能性的剪刀模型——它们能生成刀片和手柄的静态三维模型，却无法建模使刀片实现剪切运动的旋转关节。这种局限性严重阻碍了智能体辅助设计在工业制造中的实际应用。

因此，本文要解决的核心问题是：如何构建一个能够生成具有可动部件的动态三维装配体的智能体系统。具体挑战包括：系统需要指定连接装配体各部分的关节及其自由度，以支持动态部件交互；同时，当前视觉语言模型的空间推理能力有限，且现有的开源三维装配约束求解器并非为智能体设计，其反馈信息对智能体不够友好。为此，论文提出了AADvark系统原型，通过引入外部约束求解器工具和专门的视觉反馈机制，增强智能体的空间推理能力，并改进工具链以提供更强的验证信号，从而实现对动态CAD模型的生成与验证。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**AI驱动的计算机辅助设计（CAD）** 和**AI系统的验证与优化**。

在**AI驱动的CAD**领域，早期研究利用生成模型从点云、边界表示或图像等输入生成参数化CAD模型，但这些方法严重依赖难以获取且覆盖有限的标注数据集，限制了生成复杂或分布外对象的能力。随后，研究转向利用预训练大语言模型（LLMs），如CAD-LLama和CAD-GPT，通过微调生成可编译为3D模型的代码，但仍需构建训练数据集。最新的进展是采用智能体（Agent）方法实现免训练生成，如CADCodeVerify、CAD-Assistant等系统，它们将多模态LLM置于反馈循环中，迭代编写代码、编译、可视化并根据反馈进行修正。本文的AADvark系统属于此类，但与之关键区别在于，AADvark专门专注于设计**具有运动部件的复杂3D装配体**（如活塞、剪刀），而先前系统（如最相似的CAD-Assistant）主要生成静态模型，无法处理动态交互。

在**验证与优化**领域，近期研究强调通过强验证器为智能体系统提供反馈以提升性能，例如在数学和编程问题中使用自动评分器或单元测试，或利用标注数据和LLM进行评估优化（如DSPy）。本文AADvark借鉴了这一范式，通过集成外部约束求解器和专门的视觉反馈机制来弥补LLM空间推理的不足，但其应用领域（3D CAD模型生成）与这些工作在具体任务和验证信号上存在显著差异。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为AADvark的智能体辅助设计系统来解决动态CAD模型生成问题。其核心方法是将大型语言模型（LLM）置于一个包含代码生成、编译、可视化和反馈的迭代循环中，并引入外部约束求解器和增强的可视化反馈机制来克服LLM空间推理能力的不足。

整体框架是一个迭代的智能体执行循环。系统以目标物体的图像和/或文本描述作为输入。智能体（如Gemini 3 Flash）的核心任务是生成描述3D装配体的JSON文件。这些JSON文件定义了构成装配体的各个零件（parts）以及连接它们的关节（joints）。一个装配体文件包含三个主要部分：引用的零件定义、零件实例（links）的列表，以及连接这些实例的关节集合。关节定义需详细指定连接的两个实例、关节类型、连接的具体面、自由度（固定或自由）及其运动范围。

系统的关键创新点在于两个经过专门改造的工具，它们构成了强大的验证反馈机制：
1. **增强的3D装配约束求解器**：系统采用并改进了开源的OndselSolver。主要改进包括：a) 用四元数替代欧拉角来表示方向，避免了零件反平行放置的歧义；b) 即使在编译出错时（如零件干涉），也强制更新FreeCAD中的零件位置，使智能体能“看到”错误；c) 提供更具信息量的错误消息，并通过消除牛顿法求解中的随机性来源使求解过程更确定。这为智能体提供了关于设计物理可行性的强验证信号。
2. **扩展的FreeCAD可视化工具**：为解决VLMs空间推理不精确及不同零件实例在渲染中外观相似的问题，系统对FreeCAD进行了关键修改。它为每个零件实例的每个面和边计算并分配了唯一的颜色和纹理（如实线与虚线）。这样，智能体在定义关节时，可以通过指定要连接的两个面的颜色和纹理来精确定位，极大提高了关节指定的准确性。这种增强的可视化反馈是系统能成功生成复杂动态装配体的关键。

通过这一架构，AADvark使智能体能够直接对具有一个或多个自由度的动态零件交互进行推理和设计，从而首次实现了能生成包含运动部件（如剪刀、活塞）的复杂3D装配体的Agent-Aided Design系统。

### Q4: 论文做了哪些实验？

论文通过两个主要实验验证了AADvark系统在动态和静态CAD模型生成上的能力。

实验设置上，系统被置于一个反馈循环中，通过编写代码、编译为CAD模型、可视化模型，并基于视觉和其他反馈迭代优化代码。系统集成了外部约束求解器工具和专门的视觉反馈机制，以弥补大语言模型在空间推理上的不足。

在数据集/基准测试方面，实验使用了特定对象的图像作为输入。对于动态模型，以剪刀为例，提供了其在闭合和打开两种状态下的图像。对于静态模型，测试集包括幼儿床、椅子、茶几、车棚和立式白板等物体，每个物体提供1-3张输入图像，并额外使用LLM生成的幼儿床设计文档来测试自然语言规格的处理能力。

对比方法方面，论文指出此前最先进的系统无法构建具有活动部件的复杂3D装配体，而AADvark是首个针对此任务设计的智能体系统原型。

主要结果和关键数据指标如下：
1.  **动态模型生成（剪刀）**：系统成功构建了包含旋转关节以实现剪切运动的剪刀模型。经过20次迭代后完成，最终为手柄添加了手指孔。整个过程耗时4.14小时，成本15.85美元，处理了1820万输入token和220万输出token，进行了468次LLM调用。平均每次迭代耗时745秒，成本0.79美元，处理91.4万输入token和11.1万输出token，进行23.4次LLM调用。
2.  **静态模型生成**：系统成功为所有测试对象生成了CAD模型，迭代次数在4到34次之间。对于车棚、茶几和白板，系统在1-3次迭代内就能生成与输入相似的3D装配体。对于结构更复杂的幼儿床和椅子，则需要更多迭代。实验发现，只有在装配体渲染中为每个零件实例的不同面和边添加独特颜色后，系统才能成功构建幼儿床模型。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要体现在几何形状和关节类型的单一性（仅支持矩形棱柱和旋转关节），以及智能体执行的非确定性可能导致设计过程陷入停滞。未来研究可首先扩展系统支持的零件库和关节类型，以覆盖更广泛的机械结构。其次，需深入分析智能体“卡住”的根本原因，例如引入更精细的状态监控或回溯机制来提升鲁棒性。此外，结合更强大的空间推理模型（如视觉语言模型）或物理仿真反馈，可能减少对外部求解器的依赖，增强对复杂动态交互的自主理解。长远来看，若能整合生成式3D建模技术，系统有望实现从概念到可制造装配体的端到端设计，真正推动工业应用的变革。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个名为AADvark的智能体辅助设计系统，旨在解决现有AI设计系统无法构建具有可动部件的复杂三维CAD装配体的问题。其核心贡献是首次实现了能够直接处理多自由度动态零件交互的智能体系统，从而能够设计如活塞、剪刀等包含机械运动的装配体。

方法上，AADvark将智能体置于一个反馈循环中：智能体编写生成CAD模型的代码，编译并可视化模型，然后基于视觉和其他反馈迭代优化代码。针对大语言模型空间推理能力的不足，系统创新性地整合了外部约束求解器工具和专门的视觉反馈机制。通过改造智能体使用的工具（FreeCAD和装配求解器），系统生成了强大的验证信号。

主要结论是，AADvark原型成功证明了通过结合约束求解与针对性视觉反馈，智能体系统能够有效推理并生成包含可动部件的三维装配体。这项工作推动了智能体辅助设计向实际工业制造应用迈出了关键一步，实现了该领域处理动态机械装配能力的突破。
