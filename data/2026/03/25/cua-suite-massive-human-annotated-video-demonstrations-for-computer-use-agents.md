---
title: "CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents"
authors:
  - "Xiangru Jian"
  - "Shravan Nayak"
  - "Kevin Qinghong Lin"
  - "Aarash Feizi"
  - "Kaixin Li"
  - "Patrice Bechard"
  - "Spandana Gella"
  - "Sai Rajeswar"
date: "2026-03-25"
arxiv_id: "2603.24440"
arxiv_url: "https://arxiv.org/abs/2603.24440"
pdf_url: "https://arxiv.org/pdf/2603.24440v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CV"
tags:
  - "Computer-Use Agent"
  - "Dataset"
  - "Video Demonstrations"
  - "Benchmark"
  - "UI Grounding"
  - "Desktop Automation"
  - "Human-in-the-Loop Data"
relevance_score: 8.0
---

# CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents

## 原始摘要

Computer-use agents (CUAs) hold great promise for automating complex desktop workflows, yet progress toward general-purpose agents is bottlenecked by the scarcity of continuous, high-quality human demonstration videos. Recent work emphasizes that continuous video, not sparse screenshots, is the critical missing ingredient for scaling these agents. However, the largest existing open dataset, ScaleCUA, contains only 2 million screenshots, equating to less than 20 hours of video. To address this bottleneck, we introduce CUA-Suite, a large-scale ecosystem of expert video demonstrations and dense annotations for professional desktop computer-use agents. At its core is VideoCUA, which provides approximately 10,000 human-demonstrated tasks across 87 diverse applications with continuous 30 fps screen recordings, kinematic cursor traces, and multi-layerfed reasoning annotations, totaling approximately 55 hours and 6 million frames of expert video. Unlike sparse datasets that capture only final click coordinates, these continuous video streams preserve the full temporal dynamics of human interaction, forming a superset of information that can be losslessly transformed into the formats required by existing agent frameworks. CUA-Suite further provides two complementary resources: UI-Vision, a rigorous benchmark for evaluating grounding and planning capabilities in CUAs, and GroundCUA, a large-scale grounding dataset with 56K annotated screenshots and over 3.6 million UI element annotations. Preliminary evaluation reveals that current foundation action models struggle substantially with professional desktop applications (~60% task failure rate). Beyond evaluation, CUA-Suite's rich multimodal corpus supports emerging research directions including generalist screen parsing, continuous spatial control, video-based reward modeling, and visual world models. All data and models are publicly released.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决计算机使用智能体（CUAs）发展中的一个核心瓶颈问题：缺乏大规模、高质量、连续的人类演示视频数据。研究背景是，尽管计算机使用智能体在自动化复杂桌面工作流程方面潜力巨大，但现有方法主要依赖于稀疏的屏幕截图数据集（如最大的公开数据集ScaleCUA仅包含约200万张截图，相当于不到20小时的视频），这些数据丢失了人机交互中关键的连续时间动态和视觉反馈信息，导致智能体在专业桌面应用（如3D建模软件、IDE）中表现脆弱，任务失败率较高。现有方法的不足在于，它们要么是自动合成数据噪声大，要么是人工标注数据集只覆盖了部分问题（如仅有空间定位而无时序上下文），且普遍缺乏连续的视觉轨迹，这限制了智能体学习长时程规划、连续空间控制策略和构建视觉世界模型的能力。因此，本文要解决的核心问题是：通过构建一个名为CUA-Suite的大规模生态系统，提供包含连续视频、密集标注的人类专家演示数据，以填补高质量训练数据的空白，从而支持训练更鲁棒、通用的计算机使用智能体。其核心组件VideoCUA提供了约55小时、600万帧的30fps连续屏幕录制视频，覆盖87个应用中的1万个任务，并附带光标轨迹和多层推理标注，旨在完整保留人机交互的时序动态，为智能体的 grounding（定位）、planning（规划）和 continuous control（连续控制）提供全面的监督信号。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为视觉基础数据集、智能体评测基准、智能体架构以及视频轨迹学习四大类。

在**视觉基础数据集**方面，现有研究多集中于移动端和网页环境（如UGround），依赖可访问性树但难以处理桌面应用的像素级复杂性。针对桌面的数据集（如OS-ATLAS、JEDI）常存在标注框错位问题，而ScreenSpot-Pro等基准覆盖范围有限。本文的CUA-Suite通过提供大规模、人工标注的桌面UI元素基础数据（GroundCUA）来弥补这一缺陷。

在**智能体评测基准**方面，现有工作如MiniWoB++（网页）、AndroidWorld（移动）和OSWorld（桌面）侧重于通过执行反馈来评估智能体，但缺乏训练视觉-语言-动作模型所需的密集离线监督。本文贡献的UI-Vision基准则专注于评估智能体在桌面环境中的基础与规划能力。

在**智能体架构**方面，现有模型（如UI-TARS、ScaleCUA）主要基于静态截图-动作对进行训练，难以理解交互的时序动态。本文通过提供连续的、包含完整时序动态的人类演示视频（VideoCUA），旨在为训练更先进的架构提供支持。

在**视频轨迹学习**方面，近期研究（如VideoGUI、OmniACT、OpenCUA）开始强调连续观察和多样化轨迹数据的重要性。然而，现有视频数据集普遍缺乏将动作与具体UI元素关联起来的帧级基础标注。本文的CUA-Suite的核心贡献在于，首次大规模地同时提供了高帧率连续视频、广泛的桌面应用覆盖、人类演示轨迹以及丰富的多层推理标注，填补了现有资源的空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为CUA-Suite的大规模生态系统来解决计算机使用智能体（CUA）训练数据稀缺和质量不足的问题。其核心方法是系统性地收集、标注并处理高质量的人类专家视频演示，形成一个统一的数据引擎，并由此衍生出三个互补的数据集，以支持智能体在视觉感知、界面理解和动作规划等全方位能力的训练与评估。

整体框架以数据收集管道为基础。首先，精心选择了87个开源的专业桌面应用程序，涵盖软件开发、内容创作、办公生产等12个类别，确保了数据的多样性和现实代表性。其次，由人类专家设计并执行真实的工作任务，而非程序生成，从而保证了演示轨迹是连贯、有目标导向的真实行为。在录制阶段，系统以30帧/秒的连续视频捕捉完整的屏幕交互，并同步记录所有鼠标和键盘操作，生成了约55小时、600万帧的原始专家演示视频。这种连续视频流完整保留了人机交互的完整时间动态，是稀疏截图数据集所不具备的。

关键技术体现在其密集的UI标注流程和统一的数据处理上。从连续视频中，提取用户执行状态改变动作（如点击）前的关键帧作为标注基础。在这些关键帧上，标注员手动为每个可见的UI元素标注边界框，并提供文本标签（如元素名称或显示文本），同时使用OCR提取长文本。此外，约50%的元素还被分类到八个高级功能类别中，增加了语义结构。这些密集、高质量的标注构成了整个数据生态的基石。

基于这个统一的数据引擎，论文构建了三个主要模块/组件：
1.  **VideoCUA (ActCUA)**：核心的视频演示数据集，包含约1万个任务的连续视频轨迹，用于训练智能体执行复杂工作流。其数据量（帧数）是现有最大开源数据集ScaleCUA的2.5倍以上。
2.  **GroundCUA**：大规模界面理解数据集，包含5.6万张标注截图和超过360万个UI元素标注，用于训练智能体进行精细的视觉定位（Grounding）。其特点是规模大、分辨率高、标注密度高且经过人工验证。
3.  **UI-Vision**：一个严格的评估基准，包含450个任务演示，专门用于评估智能体的元素定位、布局理解和动作预测能力，以诊断其失败环节。

创新点在于：首次提供了大规模、连续帧率的人类专家桌面操作视频数据集，弥补了该领域的关键空白；通过统一的、以真实人类行为为中心的数据收集管道，同时支持了轨迹学习、界面理解和能力评估三个研究方向；其数据格式与现有主流框架（如OpenCUA）兼容，并能无损转换为所需格式，便于直接用于训练和推动下一代通用计算机使用智能体的发展。

### Q4: 论文做了哪些实验？

论文实验主要围绕CUA-Suite数据集的构建、评估与应用展开。实验设置包括：1）构建大规模专家视频演示数据集VideoCUA，涵盖87个专业桌面应用的约10,000个任务，以30fps连续录制，总时长约55小时（600万帧），同步记录光标轨迹与键盘操作；2）创建密集UI标注数据集GroundCUA，包含5.6万张标注截图及360万个UI元素标注，其中50%元素被分类为8种功能类别；3）设计评估基准UI-Vision，包含450个任务演示，用于测试智能体的元素定位、布局理解和动作预测能力。

数据集/基准测试方面，主要使用UI-Vision进行评测，并与现有数据集（如ScaleCUA、Mind2Web、AITW等）进行对比。对比方法包括多款先进多模态模型，如MAI-UI-32B/8B、OpenCUA系列（7B-72B）、Qwen3-VL-32B/8B、PhiGround-7B等。

主要结果与关键指标：在UI-Vision的元素定位任务中，MAI-UI-32B以平均47.7%的准确率领先（基础任务59.1%，功能任务57.1%，空间任务26.9%）。相比一年前的SOTA模型UI-TARS-72B（25.5%），性能提升近一倍。然而，空间推理任务仍是瓶颈，所有模型表现均较差（最高仅26.9%）。模型参数量扩大带来稳定增益，如OpenCUA从7B到72B提升7.6个绝对百分点。此外，PhiGround-7B配合o3规划器后，性能从27.2%提升至36.2%。实验还发现，当前基础动作模型在专业桌面应用上的任务失败率高达约60%。基于GroundCUA训练的GroundNext-3B模型在OS-World Verified基准上达到50.6分，展示了其实用性。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其核心贡献是构建了大规模、高质量的连续视频演示数据集CUA-Suite，以解决计算机使用智能体（CUA）训练数据稀缺的瓶颈。然而，该工作仍存在一些局限性和值得深入探索的方向。

**局限性及未来研究方向：**
1.  **数据规模与多样性**：尽管CUA-Suite在桌面应用领域是重大突破，但55小时的视频数据相对于训练一个真正通用的智能体而言，规模仍然有限。未来可探索如何高效地扩展数据规模，例如通过半自动化标注、合成数据生成或利用多模态大模型进行数据增强。
2.  **智能体能力瓶颈**：论文评估指出，当前模型在空间关系推理（Spatial Grounding）上表现显著落后，且任务失败率仍高。这表明模型对复杂UI布局和动态交互的理解不足。未来研究需设计更强大的视觉-语言-动作联合模型架构，专门提升对界面元素空间关系和时序动态的建模能力。
3.  **任务复杂性与泛化性**：数据集中于专家设计的离散任务，可能未能完全覆盖真实世界中开放、多步骤、需长期规划的复杂工作流。未来的探索方向包括如何让智能体从演示中学习抽象的技能和子目标规划，并能在未见过的应用或任务组合中灵活组合运用。

**可能的改进思路：**
1.  **开发视频预测与决策模型**：利用连续的帧序列数据，训练能够预测界面状态演变和用户意图的“视觉世界模型”。这有助于智能体进行更长期的规划，并理解动作的因果效应。
2.  **引入强化学习与交互学习**：仅靠模仿学习可能无法突破专家演示的边界。可结合离线强化学习从数据中挖掘更优策略，或设计安全的在线交互环境，让智能体通过试错进行自我改进。
3.  **构建分层技能库**：从密集标注的视频轨迹中自动解构和提取可复用的基本操作技能（如“点击下拉菜单”、“拖动滑块”），并学习如何根据高级指令组合这些技能，以提升解决新任务的效率和泛化能力。

### Q6: 总结一下论文的主要内容

该论文针对计算机使用智能体（CUA）发展受限于高质量连续视频演示数据稀缺的问题，提出了CUA-Suite大规模数据集生态系统。其核心贡献是构建了包含连续视频、密集标注和评估基准的完整资源，以支持通用桌面智能体的研发。

具体而言，论文首先明确了当前CUA在专业桌面应用上表现不佳的瓶颈在于缺乏包含完整时序动态的高质量人类演示数据。现有最大开源数据集ScaleCUA仅包含约20小时等效视频，且多为稀疏截图，丢失了连续交互信息。

为此，CUA-Suite的核心是VideoCUA，它提供了约55小时、600万帧的30fps连续屏幕录制视频，涵盖87个应用中的1万个专家演示任务，并附有光标运动轨迹和多层推理标注。这些连续视频保留了完整的人机交互时序动态，可无损转换为现有智能体框架所需格式。此外，系统还包含UI-Vision（用于评估CUA的定位与规划能力的基准）和GroundCUA（包含360万个UI元素标注的大规模定位数据集）。

初步评估显示，当前基础动作模型在专业桌面应用上任务失败率高达约60%。CUA-Suite的发布意义在于，其丰富的多模态语料不仅可用于模型评估，还将推动屏幕解析、连续空间控制、基于视频的奖励建模和视觉世界模型等新兴研究方向的发展。所有数据和模型均已开源。
