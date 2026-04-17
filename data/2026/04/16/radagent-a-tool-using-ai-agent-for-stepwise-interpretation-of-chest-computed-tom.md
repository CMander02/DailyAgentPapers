---
title: "RadAgent: A tool-using AI agent for stepwise interpretation of chest computed tomography"
authors:
  - "Mélanie Roschewitz"
  - "Kenneth Styppa"
  - "Yitian Tao"
  - "Jiwoong Sohn"
  - "Jean-Benoit Delbrouck"
  - "Benjamin Gundersen"
  - "Nicolas Deperrois"
  - "Christian Bluethgen"
  - "Julia Vogt"
  - "Bjoern Menze"
  - "Farhad Nooralahzadeh"
  - "Michael Krauthammer"
  - "Michael Moor"
date: "2026-04-16"
arxiv_id: "2604.15231"
arxiv_url: "https://arxiv.org/abs/2604.15231"
pdf_url: "https://arxiv.org/pdf/2604.15231v1"
categories:
  - "cs.AI"
tags:
  - "Tool-Using Agent"
  - "Medical AI"
  - "Interpretability"
  - "Vision-Language Model"
  - "Stepwise Reasoning"
  - "Report Generation"
relevance_score: 7.5
---

# RadAgent: A tool-using AI agent for stepwise interpretation of chest computed tomography

## 原始摘要

Vision-language models (VLM) have markedly advanced AI-driven interpretation and reporting of complex medical imaging, such as computed tomography (CT). Yet, existing methods largely relegate clinicians to passive observers of final outputs, offering no interpretable reasoning trace for them to inspect, validate, or refine. To address this, we introduce RadAgent, a tool-using AI agent that generates CT reports through a stepwise and interpretable process. Each resulting report is accompanied by a fully inspectable trace of intermediate decisions and tool interactions, allowing clinicians to examine how the reported findings are derived. In our experiments, we observe that RadAgent improves Chest CT report generation over its 3D VLM counterpart, CT-Chat, across three dimensions. Clinical accuracy improves by 6.0 points (36.4% relative) in macro-F1 and 5.4 points (19.6% relative) in micro-F1. Robustness under adversarial conditions improves by 24.7 points (41.9% relative). Furthermore, RadAgent achieves 37.0% in faithfulness, a new capability entirely absent in its 3D VLM counterpart. By structuring the interpretation of chest CT as an explicit, tool-augmented and iterative reasoning trace, RadAgent brings us closer toward transparent and reliable AI for radiology.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI辅助医学影像解读中存在的“黑箱”问题，尤其是在胸部计算机断层扫描（CT）报告生成领域。研究背景是，尽管三维视觉语言模型（VLM）在报告生成任务上表现出色，但它们通常直接输出最终报告，而不展示其内部推理过程（如如何识别病变、依据何种证据、如何整合中间观察结果）。这使得临床医生只能被动接受结果，无法对AI的决策进行审查、验证或修正，严重限制了AI系统的透明度和可信度，而在CT解读这类高风险、劳动密集型的临床任务中，这种可解释性和可验证性至关重要。

现有方法，如CT-Agent和CTPA-Agent等训练免费的智能体系统，试图通过多步骤、基于工具的工作流来模拟放射科医生的推理过程。然而，这些方法存在明显不足：首先，它们假设驱动智能体策略的大语言模型（LLM）已具备足够的医学知识来设计相关、完整且基于医学的诊断计划，但这在实践中往往不成立；其次，它们预设LLM编排器能正确使用工具，但在需要复杂动态工具工作流的临床环境中，智能体可能难以理解复杂的工具规范和约束，导致性能受限。

因此，本文要解决的核心问题是：如何构建一个能够进行**逐步、可解释、且可验证推理**的AI智能体，以生成胸部CT报告。具体而言，论文提出了RadAgent，这是一个**基于强化学习（RL）训练、能够使用工具**的AI智能体。它通过一个明确的、工具增强的迭代推理轨迹来结构化CT解读过程，使智能体能够自动发现有效的工具使用策略，并生成附带完整中间决策和工具交互轨迹的报告，从而让临床医生能够审查报告结论的推导过程，实现更高的透明度、可靠性和临床实用性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**方法类**、**应用类**和**评测类**。

在**方法类**工作中，近期医学智能体系统旨在模仿放射科工作流程的多步骤、迭代式推理过程。例如，CT-Agent 框架将视觉数据同时分配给十个专门的分析工具，每个工具负责特定解剖区域；CTPA-Agent 则针对CT肺动脉造影，采用先分类异常、再通过预定义查询获取信息、最后总结的多步设置。这些方法均属于**免训练范式**，其智能体策略由系统提示设计或预定义的工具调用序列决定。本文提出的 RadAgent 与这些工作的核心区别在于，它**采用基于强化学习的训练范式**，而非免训练方式。这使得智能体能够通过与环境的交互，自动学习有效的工具使用策略，从而适应需要复杂动态工具工作流的临床环境。

在**应用类**工作中，现有研究主要基于大型语言模型和视觉语言模型生成最终报告，但缺乏对推理过程的揭示，形成了“黑箱”。本文的 RadAgent 则通过生成**可检查的中间决策与工具交互轨迹**，致力于提供透明和可解释的推理过程，这是其与多数现有报告生成模型的关键不同。

在**评测类**方面，相关工作多关注报告生成的准确性。本文不仅评估了临床准确性（如F1分数），还引入了对抗条件下的**鲁棒性**以及**忠实性**这一新评估维度，以衡量模型输出与中间证据的一致性，这是其3D VLM基线所不具备的能力。

### Q3: 论文如何解决这个问题？

RadAgent通过构建一个基于工具使用和分步推理的智能体系统来解决传统医学影像AI模型缺乏可解释性、无法让临床医生参与验证的问题。其核心方法是采用ReAct（推理-行动）模式，将胸部CT解读转化为一个可检查、可追溯的迭代决策过程。

**整体框架与架构设计**：系统以一个大语言模型（Qwen3-14B指令微调版）作为核心策略模型（Agent），负责协调整个推理流程。该Agent被部署在一个计算节点上，并通过MCP协议与部署在另一节点（配备四块GPU）上的专用工具集进行通信。工作流程始于调用报告生成工具（基于CT-Chat模型）产生初始报告草稿，然后Agent依据一份诊断检查清单（由AI生成并经放射科医生审核）进行逐步验证和细化。在每一轮迭代中，Agent自主决定调用哪个工具来调查特定发现，或决定结束调查并生成最终报告。整个过程产生的所有中间决策、工具调用及结果构成完整的、可供审查的推理轨迹。

**主要模块与关键技术**：
1.  **多功能工具集**：这是系统的基石，包含十类专用工具：
    *   **视觉问答**：包括基于CT-Chat的3D容积VQA工具和基于Gemma-3-27B的2D切片VQA工具，支持从整体到局部的多层级图像查询。
    *   **疾病分类**：基于CT-CLIP的病理筛查工具，可对18种胸部病变进行概率估计，辅助生成初步假设。
    *   **报告生成**：基于CT-Chat的自动报告起草工具，用于生成初始草案。
    *   **分割**：基于TotalSegmentator的解剖结构与积液分割工具，实现精准的解剖与病理定位。
    *   **切片选择**：包含多种策略的工具，能从3D容积中提取最具代表性的2D切片（如最大异常区域切片、等距多切片），为2D VQA提供输入。
    *   **窗宽窗位调整**：提供标准预设（如肺窗、骨窗），增强图像的可解释性，优化视觉证据的呈现。

2.  **可扩展的分布式部署**：工具按功能分组部署在多块GPU上，最大化利用计算资源，且工具箱设计为可扩展，便于集成新模型或功能。

**创新点**：
1.  **可解释的智能体范式**：将端到端的“黑箱”报告生成，重构为基于工具调用的、分步的、可追溯的推理过程，使临床医生能够审查结论的推导路径。
2.  **工具增强的迭代推理**：Agent并非一次性生成报告，而是通过主动、迭代地调用一系列专业工具（VQA、分类、分割等）来收集证据、验证假设、修正草案，模拟了放射科医生的审阅逻辑。
3.  **评估维度的拓展**：除了报告准确性（F1分数），论文特别强调了**鲁棒性**（在对抗性提示下保持正确预测的能力）和**忠实性**（在决策中明确承认外部提示影响的能力）的量化评估，后者是其底层3D VLM完全不具备的新能力。实验证明，RadAgent在这三个维度上均显著优于其基础的3D VLM（CT-Chat）。

### Q4: 论文做了哪些实验？

论文在胸部CT报告生成任务上进行了全面的实验评估。实验设置方面，RadAgent是一个基于强化学习（GRPO算法）训练的智能体，配备包含10个开源3D CT分析工具的工具箱（如器官分割、分类、CT窗宽调整、2D切片提取以及2D/3D视觉语言模型问答工具）和一个结构化的诊断检查清单（涵盖9个常规评估类别）。其核心是一个14B的语言模型作为工具调用和流程编排的策略模型。

使用的数据集包括：CT-RATE（作为训练、验证和分布内测试集）和RadChestCT（用于外部评估）。评估主要基于从报告中自动提取的病理标签，计算宏平均F1和微平均F1分数。CT-RATE包含18种常见病理标签，RadChestCT包含82种，但为保持可比性，评估时同样聚焦于那18种病理。

对比方法主要是作为基线的3D视觉语言模型CT-Chat（它也被集成到RadAgent中用于生成初始报告草稿）。实验还比较了RadAgent的多个变体：经过强化学习训练的全系统、未经强化学习训练的版本（仅使用相同工具和检查清单），以及在不同奖励函数设计下的训练效果（如混合奖励、无序列奖励、从一开始就使用序列奖励）。

主要结果如下：在CT-RATE测试集上，RadAgent相比CT-Chat基线，宏平均F1提高了6.0个百分点（相对提升36.4%），微平均F1提高了5.4个百分点（相对提升19.6%）。在外部数据集RadChestCT上也观察到一致的性能提升。在对抗性提示扰动下的鲁棒性实验中，RadAgent的鲁棒性达到83.7%，比CT-Chat（58.9%）高出24.7个百分点。在忠实性（faithfulness）方面，RadAgent达到了37.0%，而CT-Chat为0.0%，这体现了RadAgent可追溯的决策过程能区分证据支持的发现与提示驱动的干扰。此外，消融实验表明，强化学习训练和精心设计的复合奖励课程对于实现高性能、检查清单遵从性和工具调用连贯性至关重要。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性及未来研究方向可从多个维度进一步探索。首先，系统计算成本较高，依赖多GPU运行多个专用工具，未来可研究模型轻量化、工具动态调度或知识蒸馏技术，将习得的智能体策略固化为固定工作流，以提升在资源受限环境中的部署可行性。其次，智能体的工具使用策略针对训练时的固定工具集优化，当工具库更新或扩展时性能可能下降，未来可探索持续学习或元学习机制，使智能体能自适应新工具，而无需完全重新训练。此外，尽管报告忠实度（faithfulness）提升至37%，仍有很大改进空间，未来可结合更细粒度的奖励设计、引入不确定性量化或增强与领域知识的对齐，进一步提升推理链条的可信度。从临床整合角度看，可深入开发人机协同交互界面，让医生不仅能审查中间决策轨迹，还能实时修正或引导智能体的推理步骤，实现动态的人机互馈。最后，将RadAgent框架扩展至其他医学影像模态或临床决策场景，并探索其与更广泛医疗工具生态的集成，有望突破通用性与专科性能之间的传统权衡。

### Q6: 总结一下论文的主要内容

该论文针对当前基于视觉语言模型（VLM）的医学影像（如CT）解读系统缺乏可解释性、无法让临床医生参与验证的问题，提出了RadAgent——一个利用工具的分步式可解释AI智能体。其核心贡献在于将胸部CT报告的生成过程构建为一个明确的、工具增强的迭代推理轨迹，使医生能够完整检查中间决策与工具交互，从而验证和优化最终报告。

方法上，RadAgent采用工具使用（tool-using）的智能体架构，通过分步、可检查的流程生成报告，每一步的推理和工具调用都形成可追溯的记录。实验表明，相比其基础的3D VLM模型CT-Chat，RadAgent在三个维度上显著提升：临床准确性（宏观F1提升6.0点，相对提升36.4%）、对抗条件下的鲁棒性（提升24.7点，相对41.9%），并实现了37.0%的忠实度（faithfulness），这是基础模型完全不具备的新能力。

该研究的结论是，通过引入可解释的、工具辅助的逐步推理机制，RadAgent推动了放射学AI向更透明、可靠的方向发展，使AI从“黑箱”输出转变为临床医生可以审查、验证和协作的主动工具。
