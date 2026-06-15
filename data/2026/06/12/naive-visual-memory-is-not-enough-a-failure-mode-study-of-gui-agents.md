---
title: "Naive Visual Memory is Not Enough: A Failure-Mode Study of GUI Agents"
authors:
  - "Seoyoung Choi"
  - "Minseok Ko"
  - "Hyunseok Lee"
  - "Kunwoong Kim"
  - "Woomin Song"
  - "Chanseok Jeon"
  - "Jinwoo Shin"
date: "2026-06-12"
arxiv_id: "2606.14106"
arxiv_url: "https://arxiv.org/abs/2606.14106"
pdf_url: "https://arxiv.org/pdf/2606.14106v1"
categories:
  - "cs.MA"
  - "cs.CV"
tags:
  - "GUI Agent"
  - "视觉记忆"
  - "Agent记忆机制"
  - "失败模式分析"
  - "OSWorld基准"
  - "智能体推理"
relevance_score: 8.5
---

# Naive Visual Memory is Not Enough: A Failure-Mode Study of GUI Agents

## 原始摘要

Graphical User Interface (GUI) agents are increasingly used to automate complex computer tasks across applications, websites, and operating systems. To improve their reliability, recent work has introduced experiential memory, where agents retrieve prior trajectories to guide decision-making in similar states. More recent approaches further extend this idea to visual memory by storing and retrieving screenshots from past interactions, providing agents with richer contextual information than text-only memories. However, the effect of visual memory in GUI agents remains insufficiently understood: it is unclear which failures visual memory mitigates, or which failures it exacerbates. To systematically analyze the effect of visual memory, we introduce a taxonomy of four GUI agent failures (i.e., cognitive failure, visual state misunderstanding, hidden operation blindness, and grounding error) that map to distinct stages of the perception-reasoning-action pipeline. We find that prepending full-image memory has a divergent effect on the failure distribution: it reduces state-level failures but worsens action-level ones, and increases hidden operation blindness and grounding error. Motivated by this finding, we propose Action-Grounded Visual Memory (AGMem), an action-grounded memory framework for GUI agents. The core idea of AGMem is to store image crops that capture the local GUI region closely related to a successful action or a recovery, rather than storing full screenshots. Experiments on OSWorld show that AGMem improves task success rates by 33.3 % over full-image memory. These results demonstrate that AGMem is an effective representation for visual memory in GUI agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决图形用户界面（GUI）智能体在引入视觉记忆后如何影响其失败模式的问题。研究背景是，GUI智能体被广泛用于自动化跨应用、网页和操作系统的复杂计算机任务，但即使是最前沿的模型（如GPT、Claude、Gemini）在非平凡任务中仍频繁失败。现有方法如经验记忆和视觉记忆通过存储和检索历史轨迹或截图来提供更丰富的上下文信息，从而提升可靠性。然而，现有方法的不足在于：对视觉记忆的效果缺乏系统性理解，不清楚它到底缓解了哪些失败、又加剧了哪些失败。针对这一问题，本文的核心贡献是：首先，建立了一个涵盖GUI智能体四种失败模式（认知失败、视觉状态误解、隐藏操作盲视和接地错误）的分类体系，这些模式对应感知-推理-行动管线的不同阶段。接着，通过实证分析发现，直接预置全屏图像的视觉记忆会带来矛盾效应：它减少了状态级失败（如视觉状态误解），但加剧了行动级失败（如隐藏操作盲视和接地错误）。基于此，本文提出要解决的核心问题是：如何设计一种更有效的视觉记忆表示，既能保留对决策有益的局部视觉线索，又能避免全屏图像中任务无关信息的干扰，从而全面提升GUI智能体的可靠性。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为以下几类：

1. **Agent内存方法类**：Synapse将过去的计算机控制轨迹存储为文本示例，并在类似任务中检索；Agent Workflow Memory从成功轨迹中提取可复用工作流；MemP构建由步骤级和脚本级轨迹摘要组成的过程记忆；A-Mem将记忆组织为可随时间更新的关联笔记；ExpeL从成功和失败对中提取文本洞察；ReasoningBank存储推理策略。本文提出的Action-Grounded Visual Memory（AGMem）与这些方法的关键区别在于，它专门关注视觉记忆（存储截图）而非纯文本记忆，并通过存储动作相关的局部截图区域来克服全图记忆的局限性。

2. **GUI代理与压缩方法类**：论文提到了多模态代理的压缩方法。AGMem与这些方法的关系在于，它通过动作接地（action-grounded）的方式对视觉记忆进行选择性压缩，将存储从全截图缩减为与成功动作或恢复相关的局部图像裁剪。

本文的创新在于：系统分析了全图视觉记忆在GUI代理中“双刃剑”效应——减少状态级失败但加剧动作级失败，并据此设计了针对性的动作接地存储策略。

### Q3: 论文如何解决这个问题？

论文提出Action-Grounded Visual Memory (AGMem)框架来解决全屏视觉记忆导致GUI代理动作级失败加剧的问题。核心思想是通过存储与动作相关的局部截图区域来替代全屏截图，从而减轻视觉记忆的副作用。

整体框架包含三个主要组件：(1) 动作相关视图：通过比较连续截图(o_t, o_{t+1})，自动裁剪出动作a_t产生影响的GUI局部区域C_t，生成紧凑的记忆条目m_t = (s_j, a_t, C_t)，其中s_j是子任务标签。这避免了存储包含大量无关内容的全屏截图。(2) 两级检索：首先在轨迹层面使用Sentence-Transformer选择与当前子任务列表最相关的k条记忆轨迹，然后在步骤层面使用CLIP编码器计算当前状态（当前子任务和上一步视图）与记忆步骤的相似度，返回top-5作为检索结果。这显著缩小了搜索空间。(3) 恢复感知记忆：专门构建恢复记忆库，存储从错误状态恢复到正确状态的示范步骤。当检测到错误时，系统切换检索路径到恢复记忆，帮助代理从故障状态中恢复。

创新点在于：提出动作导向的记忆条目表示，通过局部裁剪聚焦于任务相关区域；设计两级检索机制降低噪声；引入错误恢复记忆解决错误传播问题。实验表明，AGMem在OSWorld上比全屏记忆方法提升33.3%的任务成功率。

### Q4: 论文做了哪些实验？

论文在OSWorld、WebForge和AgentNet三个基准上进行了实验，使用GPT-5.4-mini作为基础模型。实验设置包括：（1）失败模式分析，在OSWorld上比较四种失败类型（认知失败、视觉状态误解、隐藏操作盲区、接地错误）的分布；（2）端到端性能对比，与Vanilla Agent和全图像记忆基线比较。

主要结果：
- 在OSWorld上，AGMem将任务成功率从18.3%提升至27.2%，比全图像记忆（20.4%）提高33.3%。
- 失败模式分析显示：AGMem全面降低所有失败模式，其中视觉状态误解从73.1%降至32.3%（降低40.8个百分点），隐藏操作盲区从67.1%降至52.5%，接地错误从27.5%降至22.5%。相比之下，全图像记忆反而恶化了隐藏操作盲区（78.8%）和接地错误（36.1%）。
- 在AgentNet上，AGMem的步骤准确率从25.8%提升至28.8%，里程碑准确率从24.2%提升至34.6%。
- 在WebForge上，所有方法准确率均为2.0%，无明显差异。

消融实验表明：仅使用裁剪（Crop）而不进行子任务对齐检索，视觉状态误解仍高达68.3%，而AGMem将其降至32.3%，验证了子任务对齐检索的关键作用。案例研究进一步证明了AGMem通过动作接地裁剪和恢复感知记忆机制的有效性。

### Q5: 有什么可以进一步探索的点？

这篇论文清晰地揭示了"朴素的全图视觉记忆"在GUI智能体中可能导致动作级失败增加的问题，未来有几个重要的探索方向。首先，论文提出的Action-Grounded Visual Memory (AGMem) 通过裁剪局部图像改善了性能，但其裁剪策略依赖于历史动作的成功与否，未来可以研究更智能的感知机制，例如利用视觉语言模型自动识别并提取交互界面上最关键的视觉信息，避免剪裁遗漏或冗余。其次，论文仅考虑了单一状态的图像记忆，未来的工作可以探索如何构建动态的结构化视觉记忆库，比如结合场景图或对象级表示来记录界面元素的演变关系，以同时缓解“隐藏操作盲区”和“基础错误”。此外，还可以研究多模态记忆融合：将AGMem与文本记忆（如自然语言描述的操作意图）进行对齐，以弥补纯视觉记忆在抽象推理上的不足。最后，当前的评测主要基于OSWorld，未来需要在更复杂、任务链更长的Web或移动端GUI环境中验证泛化性，并分析AGMem在不同GUI框架下的鲁棒性。

### Q6: 总结一下论文的主要内容

论文提出了GUI代理的四种失败模式分类：认知失败、视觉状态误解、隐藏操作盲区和定位错误，这些失败对应感知-推理-执行管道的不同阶段。研究发现，将完整截图作为视觉记忆存在矛盾效应——能减少状态级失败（如视觉状态误解下降3.5%），但会加剧动作级失败（隐藏操作盲区上升11.7%，定位错误上升8.6%）。基于此，论文提出动作锚定视觉记忆框架，核心是存储与成功操作密切相关的局部裁剪区域而非完整截图，并构建子任务对齐的检索系统和恢复记忆模块。在OSWorld基准上，该方法将任务成功率从完整记忆的20.4%提升至27.2%，同时显著降低所有四种失败模式，特别是视觉状态误解降低40.8%。该工作首次系统分析了视觉记忆对GUI代理失败分布的影响，证明了紧凑、动作相关的视觉表示比完整截图更有效。
