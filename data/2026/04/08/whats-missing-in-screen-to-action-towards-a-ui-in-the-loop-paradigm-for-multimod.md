---
title: "What's Missing in Screen-to-Action? Towards a UI-in-the-Loop Paradigm for Multimodal GUI Reasoning"
authors:
  - "Songze Li"
  - "Xiaoke Guo"
  - "Tianqi Liu"
  - "Biao Yi"
  - "Zhaoyan Gong"
  - "Zhiqiang Liu"
  - "Huajun Chen"
  - "Wen Zhang"
date: "2026-04-08"
arxiv_id: "2604.06995"
arxiv_url: "https://arxiv.org/abs/2604.06995"
pdf_url: "https://arxiv.org/pdf/2604.06995v1"
categories:
  - "cs.AI"
tags:
  - "GUI Agent"
  - "Multimodal Agent"
  - "UI Understanding"
  - "Agent Reasoning"
  - "Benchmark"
  - "Human-Computer Interaction"
relevance_score: 7.5
---

# What's Missing in Screen-to-Action? Towards a UI-in-the-Loop Paradigm for Multimodal GUI Reasoning

## 原始摘要

Existing Graphical User Interface (GUI) reasoning tasks remain challenging, particularly in UI understanding. Current methods typically rely on direct screen-based decision-making, which lacks interpretability and overlooks a comprehensive understanding of UI elements, ultimately leading to task failure. To enhance the understanding and interaction with UIs, we propose an innovative GUI reasoning paradigm called UI-in-the-Loop (UILoop). Our approach treats the GUI reasoning task as a cyclic Screen-UI elements-Action process. By enabling Multimodal Large Language Models (MLLMs) to explicitly learn the localization, semantic functions, and practical usage of key UI elements, UILoop achieves precise element discovery and performs interpretable reasoning. Furthermore, we introduce a more challenging UI Comprehension task centered on UI elements with three evaluation metrics. Correspondingly, we contribute a benchmark of 26K samples (UI Comprehension-Bench) to comprehensively evaluate existing methods' mastery of UI elements. Extensive experiments demonstrate that UILoop achieves state-of-the-art UI understanding performance while yielding superior results in GUI reasoning tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有图形用户界面（GUI）自动化任务中，模型对界面元素理解不足的核心问题。研究背景是，随着多模态大语言模型（MLLMs）的发展，GUI智能体在网页浏览、移动应用等自动化场景中展现出潜力，但实际表现仍面临挑战。现有方法普遍遵循“屏幕到动作”的范式，即模型直接根据屏幕截图输出交互动作（如点击坐标）。这种范式存在明显不足：它像一个黑箱，决策过程缺乏可解释性；更重要的是，它忽略了对于UI元素（如按钮、文本框）的深入、全面理解，导致模型难以准确定位关键元素，也无法真正掌握其语义功能和使用方法，最终造成任务失败。

本文的核心问题是：如何弥补当前“屏幕到动作”范式中缺失的、对UI元素的系统性理解环节，从而提升GUI推理的准确性和可解释性。为此，论文提出了一个创新的“UI在循环中”范式。该范式将GUI推理重构为一个循环的“屏幕-UI元素-动作”过程，明确将UI元素作为从屏幕感知到执行动作的关键桥梁。通过让模型显式学习UI元素的定位、语义功能和实际用法，实现更精准的元素发现和可解释的推理。同时，为了推动该领域研究，论文还引入了更具挑战性的“UI理解”任务及相应的评估指标与大规模基准数据集。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：屏幕到动作的GUI智能体，以及UI元素增强的GUI智能体。

在**屏幕到动作的GUI智能体**方面，现有工作主要通过大规模预训练（如GUI-OWL）、监督微调（如Aguvis、CoCo-Agent）或强化学习（如UI-R1、InfiGUI-R1）来提升GUI推理能力，并构建了多种数据集（如AITW、OmniACT）进行训练。然而，这些方法将UI理解隐含在动作预测中，缺乏对UI元素的显式关注，导致可解释性不足。本文提出的UILoop范式（屏幕-UI元素-动作循环）则明确将UI元素理解作为核心环节，弥补了这一缺陷。

在**UI元素增强的GUI智能体**方面，相关研究（如SeeClick、ScreenSpot-Pro、UI-Vision）主要侧重于提升UI元素的定位能力，或通过外部检索（如GUI-explorer）获取UI信息。但它们普遍忽略了UI元素的语义功能（如按钮、滚动条的区别）和实际用法（如点击与拖拽），这可能导致交互错误。本文的UILoop不仅关注元素定位，更强调模型对元素语义功能和用法的显式学习，从而实现了更精准、可解释的推理。此外，本文还引入了更具挑战性的UI理解任务和对应的评测基准，以系统评估模型对UI元素的掌握程度。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“UI-in-the-Loop”（UILoop）的创新范式来解决现有GUI推理任务中缺乏可解释性和对UI元素理解不足的问题。其核心是将GUI推理任务重新定义为“屏幕-UI元素-动作”的循环过程，而非传统的端到端“屏幕到动作”映射。解决方案主要包括一个两阶段的框架：大规模基准构建和基于强化学习的微调。

在整体框架上，第一阶段是**数据构建与基准创建**。针对现有数据集缺乏细粒度UI元素信息的问题，论文设计了一个数据合成流水线，构建了包含26K样本的“UI Comprehension-Bench”基准。该过程首先利用现有GUI推理数据集（如Android Control、OmniAct等）作为源数据，其原始格式为（图像、屏幕描述、动作）。接着，使用标记模型（如OmniParser V2）识别并定位屏幕中所有UI元素的位置。然后，采用GPT-4o作为选择模型，根据用户指令筛选出关键的UI元素，并为其补充**语义功能**（该元素是什么、有何作用）和**实际用法**（如何用于推理和行动）的详细描述。最终形成（指令、屏幕描述、关键UI元素信息、动作）的数据格式，为模型提供了可解释的推理链条。

第二阶段是**模型训练与优化**，即“UI元素驱动的强化微调”。为了克服模型在理解与利用UI元素上的不足，论文设计了一种强化学习训练策略。其创新点在于设计了与新型评估任务“UI理解”完全对齐的奖励函数。该任务包含三个评估维度：定位（Locate）、语言化描述（Lingualize）和利用（Leverage）。相应地，训练中也设计了三种奖励：1）**定位奖励**：基于预测UI元素坐标与真实坐标的欧氏距离计算，鼓励模型准确定位；2）**语言化奖励**：基于预测与真实UI元素文本描述的语义相似度计算，鼓励模型准确理解元素功能；3）**利用奖励**：根据动作类型（如点击、输入等），判断模型是否正确地使用了预测的UI元素来执行动作。此外，还有一个**格式奖励**，确保模型输出结构化的推理过程（包含<ui>、<think>、<answer>等标签）。总体奖励是这些奖励的加权组合，其设计确保了模型优先学习定位和理解UI元素，再学习如何利用它们进行决策。

主要的技术创新点在于：1）提出了“UI理解”这一新的中间任务及其三维评估体系，使推理过程透明化；2）构建了首个包含细粒度、高质量UI元素标注的大规模基准UI Comprehension-Bench；3）提出了UI元素驱动的强化微调方法，通过精心设计的、与评估指标一致的奖励函数，显式地引导多模态大语言模型学习UI元素的定位、语义理解和实际运用，从而实现了更精准、更可解释的GUI推理。

### Q4: 论文做了哪些实验？

实验设置方面，研究以Qwen2.5-VL-3B和7B作为基础模型，在UI Comprehension-Bench的训练集上进行训练，并采用基于Verl的强化微调（RFT）直至奖励收敛（约3-6个周期），每次5个rollout。实验在8块A100 80G GPU上运行，关键参数α₁和α₂分别设为4和5，UI指示器阈值η为0.5。

使用的数据集和基准测试包括：用于评估高难度多步骤GUI推理的Android Control-High测试集、用于评估跨平台基础能力的ScreenSpot-Pro测试集，以及新提出的UI Comprehension-Bench（包含26K样本），用于全面评估模型对UI元素的掌握程度。

评估指标分为两类：对于GUI推理任务，使用动作类型准确率（Type）、点准确率（Ground Rate, GR）和步骤成功率（SR）；对于UI理解任务，使用定位（Locate）、语义化（Lingualization）和利用（Leverage）三个指标来分别评估UI元素的定位、语义理解和功能利用的准确率。

对比方法包括两大类：（1）零样本通用多模态大语言模型（如Claude-CU、GPT-4o、Qwen2.5-VL系列），它们未经专门GUI训练；（2）“屏幕到动作”训练模型，即在GUI数据集上训练后直接从屏幕输出动作的模型（如SeeClick、GUI-Owl、OS-Atlas系列、UI-R1、GUI-R1等）。

主要结果如下：在ScreenSpot-Pro基准上，UILoop-3B和7B模型在整体平均得分上分别超越了同尺寸的Qwen2.5-VL和GUI-R1模型，提升幅度分别为13.3%/2%和13.3%/3.2%。在Android Control-High上，UILoop-7B模型的步骤成功率（SR）达到了76.3%，显著超过了GUI专家模型OS-Atlas-7B、OS-Atlas-Pro-7B和GUI-OWL-7B，分别高出46.5%、58.0%和38.8%。在UI Comprehension-Bench上，UILoop-7B模型取得了26.1分的SOTA性能，而现有的“屏幕到动作”模型得分均低于10%。消融实验证实，定位、语义化和利用三个奖励机制均有效提升了推理性能，其中完整UILoop设置带来的提升最大。此外，案例研究表明UILoop能通过显式分析UI元素语义和功能，实现更准确、可解释的推理。

### Q5: 有什么可以进一步探索的点？

该论文提出的UILoop范式在细粒度UI元素理解上取得了进展，但仍存在明显局限。首先，方法主要关注单个UI元素的定位与语义，缺乏对多元素组成的粗粒度布局（如功能区块、页面结构）的建模，这限制了模型对复杂界面整体逻辑的把握。未来可探索分层级的UI表示方法，结合视觉与结构信息，使模型能同时理解元素细节与宏观布局。其次，实验仅基于Qwen2.5-VL模型，泛化性未得到验证。后续应在更多MLLMs（如GPT-4V、Gemini）上测试，并分析不同模型架构对UI推理的影响。此外，论文虽提出了UI理解评测基准，但任务类型仍较单一；可引入需多步推理、动态交互的复杂任务（如跨页面流程完成），以更全面评估GUI推理能力。从技术角度看，可进一步探索如何将UI布局知识显式注入模型训练，或利用强化学习优化动作决策的长期效果，推动“屏幕-动作”向更智能、可解释的人机协作范式发展。

### Q6: 总结一下论文的主要内容

该论文针对现有图形用户界面（GUI）推理任务中界面理解不足的问题，提出了一种创新的“UI-in-the-Loop”（UILoop）范式。核心贡献是将传统的“屏幕到动作”的直接决策模式，重构为“屏幕-UI元素-动作”的循环过程，通过让多模态大语言模型显式学习UI元素的定位、语义功能及实际用法，实现精确的元素发现与可解释推理。方法上设计了UI元素驱动的强化微调以提升理解能力，并引入了围绕UI元素理解的评估任务及包含2.6万样本的基准测试UI Comprehension-Bench。实验表明，UILoop在UI理解上达到最优性能，并显著提升了GUI推理任务的效果。
