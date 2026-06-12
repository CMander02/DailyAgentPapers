---
title: "SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning"
authors:
  - "Seokju Cho"
  - "Ryo Hachiuma"
  - "Abhishek Badki"
  - "Hang Su"
  - "Byung-Kwan Lee"
  - "Chan Hee Song"
  - "Sifei Liu"
  - "Subhashree Radhakrishnan"
  - "Seungryong Kim"
  - "Yu-Chiang Frank Wang"
  - "Min-Hung Chen"
date: "2026-06-11"
arxiv_id: "2606.13673"
arxiv_url: "https://arxiv.org/abs/2606.13673"
pdf_url: "https://arxiv.org/pdf/2606.13673v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "LLM/VLM Agent"
  - "Spatial Reasoning"
  - "Code-Action Interface"
  - "Tool-Augmented Agent"
  - "Training-Free Framework"
relevance_score: 7.5
---

# SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning

## 原始摘要

Spatial reasoning, the ability to determine where objects are, how they relate, and how they move in 3D, remains a fundamental challenge for vision-language models (VLMs). Tool-augmented agents attempt to address this by augmenting VLMs with specialist perception modules, yet their effectiveness is bounded by the action interface through which those tools are invoked. In this work, we study how the design of this interface shapes the agent's capacity for open-ended spatial reasoning. Existing spatial agents either employ single-pass code execution, which commits to a full analysis strategy before any intermediate result is observed, or rely on a structured tool-call interface that often offers less flexibility for freely composing operations or tailoring the analysis to each task. Both designs offer limited flexibility for open-ended, complex 3D/4D spatial reasoning. We therefore propose SpatialClaw, a training-free framework for spatial reasoning that adopts code as the action interface. SpatialClaw maintains a stateful Python kernel pre-loaded with input frames and a suite of perception and geometry primitives, letting a VLM-backed agent write one executable cell per step conditioned on all prior outputs, enabling the agent to flexibly compose and manipulate perception results and adapt its analysis to both intermediate text and visual observations and the demands of each problem. Evaluated across 20 spatial reasoning benchmarks spanning a broad range of static and dynamic 3D/4D spatial reasoning tasks, SpatialClaw achieves 59.9% average accuracy, outperforming the recent spatial agent by +11.2 points, with consistent gains across six VLM backbones from two model families without any benchmark- or model-specific adaptation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视觉语言模型（VLM）在三维空间推理任务中面临的根本性挑战。空间推理涉及确定物体的位置、相互关系及在三维空间中的运动，尽管对人类而言轻而易举，但对现有VLM却十分困难，因为模型难以直接从像素中可靠地进行结构化几何分析。

现有方法是使用工具增强的智能体，即通过专门的感知模块（如检测器、深度估计器）来辅助VLM。然而，这些智能体的有效性严重受限于“动作界面”（action interface）——即调用这些工具的方式。当前主流存在两种界面设计：一是“单次代码执行”，要求智能体在观察到任何中间结果前就写好完整程序并一次性运行，缺乏灵活性；二是“结构化工具调用”，通过预定义的命名工具和参数接口来操作，虽然过程可控，但难以灵活组合工具或根据任务需求进行定制化分析。这两种设计都难以支持开放、复杂的3D/4D空间推理任务。

因此，本文要解决的核心问题是：如何设计一个更灵活、更具表达力的动作界面，使智能体能够根据中间观察结果动态地组合、调整和迭代其空间分析策略，从而真正胜任开放式的复杂空间推理。

### Q2: 有哪些相关研究？

本文相关研究主要分为三类。**方法类**：现有空间推理智能体主要依赖两种行动接口——单次代码执行（如ViperGPT、VisProg）和结构化工具调用（如MM-Navigator、LLaVA++）。单次代码执行会迫使模型在观察到任何中间结果前就制定完整策略，缺乏迭代调整能力；结构化工具调用通过预定义API（如JSON或XML）调用感知模块，难以灵活组合测试时才确定的操作。本文提出的SpatialClaw采用代码作为行动接口，通过状态化Python内核实现逐步迭代，弥补了前两者的不足。**应用类**：相关工作如MetaVL、SeePlan等专注于特定场景（如导航、问答），而SpatialClaw覆盖20个静态/动态3D/4D空间推理基准，更具通用性。**评测类**：本文在6种VLM骨干网络上系统比较不同接口的性能，指出现有智能体因接口限制导致中间视觉证据无法参与推理循环，而SpatialClaw通过代码生成实现灵活组合（如基于scipy.spatial.KDTree寻近邻物体），弥补了这一关键差距。

### Q3: 论文如何解决这个问题？

SpatialClaw通过将代码作为动作接口的核心设计，构建了一个无需训练的空间推理框架，核心在于持久性Python内核与五阶段智能体循环的组合。整体框架包括一个持久化的工作区（kernel）和一个外部的智能体循环。主要模块和组件为：首先，持久性内核预加载输入帧、元数据和解包后的`tools`模块，其中`tools`包含感知原语（如基于Depth Anything 3的`Reconstruct`重建深度、相机参数和点云，以及SAM3用于分割）和科学计算库（NumPy、SciPy、Matplotlib），以及`show()`函数用于将中间结果（如掩码、深度图）以图像形式嵌入下一上下文，和`vlm`用于向独立VLM会话发送文本查询。智能体每步生成一个可执行Python单元，该单元能创建掩码、点云、图表或数值摘要，其执行结果（文本输出、变量摘要、注册的图像）作为反馈被追加到上下文，智能体据此决定下一步动作，无需预先规划完整分析。外循环包含五个阶段：I，由独立LLM会话根据问题、元数据和工具文档生成分析计划（禁止代码）；II，主智能体结合问题、计划和历史轨迹生成带`purpose`, `reasoning`, `next goal`, `code`字段的响应；III，代码经AST静态检查后执行；IV，组装反馈（stdout、traceback、变量摘要和`show()`注册的图像）；V，通过`ReturnAnswer()`提交答案。创新点在于：以代码作为统一动作接口替代预定义工具调用，实现灵活的组合与逐步细化；通过持久化状态使智能体能够“构建-检查-修正”，即基于中间结果迭代优化分析；统一系统提示词引导智能体遵循证据交叉验证、优先度量计算、可视化检查等推理规范，无需针对特定基准或模型调整。

### Q4: 论文做了哪些实验？

在20个空间推理基准上进行的实验包括：单图像空间推理、多视图空间推理、通用空间推理、视频和4D推理以及通用视频理解。评估使用了Qwen3.5（122B-A10B和397B-A17B）、Qwen3.6（35B-A3B和27B）以及Gemma4（31B和26B-A4B）6个开源VLM骨干模型（覆盖122B到397B参数范围）。对于超过1000个样本的基准，采用上限采样，N_max设置为30。所有基准和骨干模型使用相同的超参数、系统提示和感知工具，无需任何基准或模型特定适配。

主要结果：SpatialClaw在所有6个骨干模型上均一致超越无工具基线。在视频和4D推理基准（如DSI-Bench）上平均提升+18.3个百分点，在多视图空间推理基准（如MindCube）上平均提升+14.3个百分点。与其他操作接口对比：SpatialClaw在所有基准上一致优于单次代码执行（生成完整代码后观察反馈）和结构化工具调用（JSON命令接口），在多步骤几何组合任务上提升最为显著。此外，对工具组件进行消融实验（移除感知工具SAM3/DA3、仅保留感知工具或仅保留效用函数），使用Gemma4-26B-A4B在15个基准子采样样本上验证了各组件的必要性。

### Q5: 有什么可以进一步探索的点？

该工作通过引入状态化代码执行接口，有效解决了传统结构化工具调用灵活性不足的问题。然而，当前框架仍存在若干可探索方向：首先，状态化Python内核的持久化内存管理可能成为处理长视频序列的瓶颈，尤其在需要跟踪数十个动态物体时，上下文窗口与计算资源开销需进一步优化。其次，代码执行依赖预定义的感知原语集合，若遇到模型未见过的空间变换（如流体形变或半透明物体）将暴露局限性，未来可引入可学习的符号化感知模块，通过零样本查询自适应生成新原语。此外，当前方案缺乏对置信度的显式建模，当多个视觉线索矛盾时（如深度估计与光流结果冲突），可考虑设计概率化融合机制。最后，将执行轨迹转化为可复用的程序库，通过元学习经验积累提升多步骤推理效率，可能是突破当前线性执行模式的新方向。

### Q6: 总结一下论文的主要内容

空间推理，即判断物体在3D空间中的位置、关系和运动的能力，是视觉语言模型（VLM）面临的根本挑战。现有工具增强型智能体通过调用感知模块（如检测器、深度估计器）来辅助VLM，但其效果受限于工具调用的“动作接口”设计。单次代码执行或结构化工具调用这两种主流接口，在需要灵活组合操作并基于中间结果动态调整推理的复杂3D/4D任务中表现不佳。为此，本文提出SpatialClaw，一种免训练框架，采用“代码即动作接口”的新范式。它维护一个持久的Python内核，预加载了输入帧和感知库，让VLM驱动的智能体逐步编写并执行代码，每一步都能灵活组合、操作感知结果，并根据中间输出（文本或图像）调整后续分析。在涵盖静态和动态空间的20个基准测试中，SpatialClaw取得了59.9%的平均准确率，较最新空间智能体提升11.2个百分点。该方法无需针对特定基准或模型进行适配，验证了更灵活的动作接口本身是驱动空间推理能力提升的关键因素，为设计更强智能体提供了新思路。
