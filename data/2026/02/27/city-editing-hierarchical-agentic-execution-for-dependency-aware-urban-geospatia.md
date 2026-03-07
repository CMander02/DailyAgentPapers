---
title: "City Editing: Hierarchical Agentic Execution for Dependency-Aware Urban Geospatial Modification"
authors:
  - "Rui Liu"
  - "Steven Jige Quan"
  - "Zhong-Ren Peng"
  - "Zijun Yao"
  - "Han Wang"
date: "2026-02-22"
arxiv_id: "2602.19326"
arxiv_url: "https://arxiv.org/abs/2602.19326"
pdf_url: "https://arxiv.org/pdf/2602.19326v2"
categories:
  - "cs.MA"
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "hierarchical agentic framework with iterative execution-validation mechanism"
  primary_benchmark: "N/A"
---

# City Editing: Hierarchical Agentic Execution for Dependency-Aware Urban Geospatial Modification

## 原始摘要

As cities evolve over time, challenges such as traffic congestion and functional imbalance increasingly necessitate urban renewal through efficient modification of existing plans, rather than complete re-planning. In practice, even minor urban changes require substantial manual effort to redraw geospatial layouts, slowing the iterative planning and decision-making procedure. Motivated by recent advances in agentic systems and multimodal reasoning, we formulate urban renewal as a machine-executable task that iteratively modifies existing urban plans represented in structured geospatial formats. More specifically, we represent urban layouts using GeoJSON and decompose natural-language editing instructions into hierarchical geometric intents spanning polygon-, line-, and point-level operations. To coordinate interdependent edits across spatial elements and abstraction levels, we propose a hierarchical agentic framework that jointly performs multi-level planning and execution with explicit propagation of intermediate spatial constraints. We further introduce an iterative execution-validation mechanism that mitigates error accumulation and enforces global spatial consistency during multi-step editing. Extensive experiments across diverse urban editing scenarios demonstrate significant improvements in efficiency, robustness, correctness, and spatial validity over existing baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决城市更新过程中，对现有城市规划进行高效、依赖感知的迭代式地理空间修改这一核心问题。研究背景是，随着城市发展，交通拥堵、功能失衡等问题日益突出，通常需要通过修改现有规划而非完全重新设计来进行城市更新。然而，当前实践中，即使是微小的修改也需要大量人工重新绘制地理空间布局，导致迭代规划和决策过程缓慢。

现有方法存在明显不足。生成式AI方法侧重于从零生成完整规划，假设目标可以一次性达成；优化方法将规划视为具有预定义目标的序列决策问题，但依赖于对规划操作的简化抽象；基于大语言模型的智能体方法能协调规划动作和工具使用，但主要关注规划合成，缺乏对中间决策依赖关系的显式建模。这些方法的共同根本局限在于，它们将城市规划视为一个整体生成问题，而非支持现实世界中城市更新所特有的、迭代且依赖感知的修改过程。

因此，本文要解决的核心问题是：如何构建一个计算框架，将高层次的城市更新意图转化为可执行动作，并在保持空间约束的前提下迭代应用这些动作，从而实现现有城市规划的自动化、可靠和增量式精修。具体而言，论文致力于应对三大挑战：1）如何将城市更新形式化为一个在现有结构化地理空间表示（如GeoJSON）上可执行的编辑任务；2）如何在迭代修改中处理跨城市实体和几何层次的复杂依赖关系，并通过显式推理机制传播约束以保持全局结构一致性；3）如何系统地进行中间错误检测与纠正，防止错误在多步编辑中累积并损害最终规划的有效性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：生成式城市规划模型、分层与功能感知规划模型，以及大语言模型与智能体AI系统。

在生成式城市规划模型方面，已有研究将城市规划视为生成式学习问题，例如采用对抗学习框架自动生成土地利用配置，或将量化、生成与评估整合为统一生成框架，还有工作探索条件生成与变分模型以融入规划约束。这些方法专注于从零生成完整规划，而本文则专注于对现有结构化规划进行逐步的指令驱动编辑。

在分层与功能感知规划模型方面，相关研究强调城市环境中的层次结构与功能依赖，例如提出融入功能需求的多层次生成框架，或利用分层强化学习建模区域与街区间的依赖关系。这些方法虽能处理整体生成，但并非为逐步编辑现有布局而设计。本文提出的分层智能体框架则明确针对具有空间依赖关系的多步骤编辑任务。

在大语言模型与智能体系统方面，LLM的进展提升了自然语言理解与指令遵循能力，而智能体AI系统则将LLM嵌入支持规划、工具使用与反馈的结构化框架中。本文正是基于此，将自然语言指令转化为对结构化地理空间数据的多阶段、层次化编辑过程，并引入了迭代执行-验证机制以确保全局一致性，这与传统生成或规划模型有显著区别。

### Q3: 论文如何解决这个问题？

论文通过提出一个层次化的智能体框架来解决城市地理空间编辑问题，该框架将自然语言指令分解为结构化的几何意图，并采用从粗到细的执行策略，同时引入迭代验证机制以确保全局一致性。核心方法包括四个关键组件：任务规划智能体、地理执行智能体、验证智能体和聚合智能体。

整体框架采用分阶段的智能体工作流。首先，任务规划智能体解析自然语言指令，生成一个结构化的编辑计划，该计划明确了涉及的多边形、线和点等几何抽象层次，以及各层次上的编辑意图、子任务和约束条件。这一规划步骤将高层指令转化为机器可执行的意图，显式地组织了跨层次的依赖关系。

执行阶段采用从粗到细的层次化流程。地理执行智能体负责在特定几何层次上执行编辑意图。它按顺序调用层次依赖的地理空间工具来处理子任务：对于信息性子任务，执行只读查询并保留观察结果作为上下文；对于状态更新子任务，则直接修改地理布局。执行从多边形级别开始，其输出作为线级别的输入，线级别的输出再作为点级别的输入。这种设计确保细粒度编辑尊重粗粒度层次做出的结构决策。

为确保可靠性，框架引入了自反思验证机制。验证智能体与每个执行步骤紧密耦合，在每次子任务后评估结果的几何有效性、依赖一致性和约束符合性。验证结果决定是否接受该中间结果并继续执行，若拒绝则触发带诊断反馈的重试。这防止了无效状态的传播和错误累积。

最后，聚合智能体整合所有已验证的编辑结果，生成最终的更新后的GeoJSON城市计划，并生成包含执行轨迹、验证决策和元数据的详细摘要，以支持追溯和评估。

创新点主要体现在：1) 将城市更新任务形式化为机器可执行的分层编辑流程；2) 提出从粗到细的层次化执行策略，显式传播空间约束；3) 设计迭代执行-验证循环，在子任务级别进行准入控制，有效缓解错误累积；4) 整个框架实现了依赖感知的编辑，兼顾了局部修改与全局空间一致性。

### Q4: 论文做了哪些实验？

论文实验部分主要包括整体性能对比、消融研究、鲁棒性检查和参数敏感性分析。实验设置方面，研究构建了一个城市地理空间数据集，从OpenStreetMap收集了219个城市的数据，组织成约1公里×1公里的空间区域块。具体为点编辑任务收集500个样本，线编辑任务500个样本，面编辑任务1500个样本。对比方法为单次执行范式，即LLM直接生成完整编辑操作序列，而论文提出的方法为分层智能体框架。评估指标包括相对执行误差、面积合规误差和执行有效率。

主要结果：在点、线、面三个层次的编辑任务中，论文提出的智能体框架均优于单次执行基线。关键数据指标显示，使用LLaMA-3-8B-Instruct作为骨干模型时，智能体框架在点编辑任务上取得L1-REE 0.187±0.235和L1-EVR 0.975±0.019；线编辑任务上L2-REE 0.319±0.396和L2-EVR 0.947±0.042；面编辑任务上L3-ACE 0.081±0.105和L3-EVR 0.979±0.017，全面领先于基线模型。

消融研究表明，移除任务规划器或验证器都会导致性能下降，尤其在复杂任务中差距更明显，验证了分层规划和迭代验证的重要性。鲁棒性检查通过向提示注入受控噪声，发现该方法在提示扰动下仍保持最佳性能。参数敏感性分析显示，最大重执行尝试次数R主要影响执行有效率，对几何精度改善有限。案例研究则展示了该方法在实际城市绿地扩展场景中处理复杂约束的能力。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其约束和交互机制尚不完善。未来研究可进一步探索以下方向：首先，引入更丰富的规划约束，如社会经济指标、环境影响评估等，使系统能综合考虑多维城市要素。其次，增强交互性，允许规划者实时提供反馈并修正中间结果，形成人机协同的迭代优化循环。此外，可探索跨尺度编辑的泛化能力，将方法扩展至建筑室内布局或区域规划等不同粒度场景。从技术角度看，可结合强化学习让智能体自主探索编辑策略，或利用扩散模型提升几何生成的多样性与合理性。最后，建立更全面的评估体系，引入专业规划师的主观评价，以衡量编辑结果的实际可用性。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为“City Editing”的分层智能体框架，用于实现依赖感知的城市地理空间修改。其核心问题是将城市更新任务形式化为机器可执行的迭代过程，以修改结构化地理空间格式（如GeoJSON）表示的现有城市规划，从而避免完全重新规划所需的高昂人工成本。

方法上，论文将自然语言编辑指令分解为跨越多边形、线和点层级的层次化几何意图。为解决空间元素和抽象层级间的相互依赖编辑问题，作者设计了一个分层智能体框架，该框架联合执行多层级规划与执行，并显式传播中间空间约束。此外，引入迭代执行-验证机制，以减轻多步编辑中的错误累积并强制保证全局空间一致性。

主要结论和贡献在于，通过广泛的实验验证，该方法在多种城市编辑场景下，相较于现有基线，在效率、鲁棒性、正确性和空间有效性方面均有显著提升。其意义在于为自动化、高效且可靠的城市规划迭代与决策支持提供了新的解决方案。
