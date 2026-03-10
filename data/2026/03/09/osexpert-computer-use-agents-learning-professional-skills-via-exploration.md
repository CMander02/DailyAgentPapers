---
title: "OSExpert: Computer-Use Agents Learning Professional Skills via Exploration"
authors:
  - "Jiateng Liu"
  - "Zhenhailong Wang"
  - "Rushi Wang"
  - "Bingxuan Li"
  - "Jeonghwan Kim"
  - "Aditi Tiwari"
  - "Pengfei Yu"
  - "Denghui Zhang"
  - "Heng Ji"
date: "2026-03-09"
arxiv_id: "2603.07978"
arxiv_url: "https://arxiv.org/abs/2603.07978"
pdf_url: "https://arxiv.org/pdf/2603.07978v1"
categories:
  - "cs.AI"
tags:
  - "Computer-Use Agent"
  - "GUI Interaction"
  - "Exploration"
  - "Skill Learning"
  - "Curriculum Learning"
  - "Action Primitives"
  - "Benchmark"
  - "OSExpert-Eval"
relevance_score: 8.5
---

# OSExpert: Computer-Use Agents Learning Professional Skills via Exploration

## 原始摘要

General-purpose computer-use agents have shown impressive performance across diverse digital environments. However, our new benchmark, OSExpert-Eval, indicates they remain far less helpful than human experts. Although inference-time scaling enables adaptation, these agents complete complex tasks inefficiently with degraded performance, transfer poorly to unseen UIs, and struggle with fine-grained action sequences. To solve the problem, we introduce a GUI-based depth-first search (GUI-DFS) exploration algorithm to comprehensively explore and verify an environment's unit functions. The agent then exploits compositionality between unit skills to self-construct a curriculum for composite tasks. To support fine-grained actions, we curate a database of action primitives for agents to discover during exploration; these are saved as a skill set once the exploration is complete. We use the learned skills to improve the agent's performance and efficiency by (1) enriching agents with ready-to-use procedural knowledge, allowing them to plan only once for long trajectories and generate accurate actions, and (2) enabling them to end inference-time scaling earlier by realizing their boundary of capabilities. Extensive experiments show that our environment-learned agent takes a meaningful step toward expert-level computer use, achieving a around 20 percent performance gain on OSExpert-Eval and closing the efficiency gap to humans by around 80 percent

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前通用计算机使用智能体在复杂、真实世界任务中表现远逊于人类专家的问题。研究背景是，尽管基于大型多模态模型的智能体已在多种数字环境中展现出通用能力，但在专业软件操作等需要高度技能的场景中，其帮助性仍然有限。作者提出的新基准OSExpert-Eval揭示了现有方法的几大不足：1）在完成复杂、长视野任务时成功率急剧下降；2）对未见过的用户界面（UI）设计泛化能力弱；3）难以执行需要精确控制的细粒度操作序列；4）依赖高失败率的试错探索，导致效率极低，延迟远高于人类。

本文认为，根本原因在于现有智能体的训练范式：它们主要通过在约100个数字环境中进行大规模人类演示的行为克隆和强化学习来训练，但未能有效掌握环境特定的程序性知识，且所学知识难以迁移到演变的真实界面和工作流中。即使是在熟悉环境中，智能体也常通过逐步规划来解决问题，而非直接运用可靠流程，这带来了巨大的计算开销和错误累积。

因此，本文要解决的核心问题是：如何让计算机使用智能体像人类专家一样，通过自主环境交互来学习结构化的专业技能，从而在复杂任务中实现接近专家水平的鲁棒性、泛化能力和效率。为此，论文提出了OSExpert这一环境学习范式，其核心创新在于让智能体通过系统探索（如GUI-DFS算法）自主发现环境的单元功能，并利用技能的组合性自我构建课程以学习复合任务，同时通过细粒度动作原语库来支持精确操作，最终形成可复用的技能集，以提升性能与效率。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为两大类：通用计算机使用智能体和自我演进的GUI智能体。

在**通用计算机使用智能体**方面，相关研究利用LLMs和MLLMs，从文本交互环境发展到处理真实网页、桌面和移动应用。它们通过人类演示数据进行训练，学习感知屏幕、生成自然语言计划并执行动作序列。然而，现有研究表明，这类智能体在处理日常简单任务时性能接近人类，但在效率上仍落后，且难以泛化到复杂的专业工作流。例如，OSWorld-Human评估了智能体在OSWorld上的效率，发现其在规划阶段存在显著延迟；OSUniverse则指出当前智能体难以解决最复杂的任务层级。Anthropic近期也提出“不要构建智能体，而是构建技能”的观点。**本文与这些工作的关系在于，同样关注提升智能体在数字环境中的性能与效率；区别在于，本文不依赖大规模训练数据扩展，而是提出让智能体在目标环境中通过探索自动构建技能集。**

在**自我演进的GUI智能体**方面，相关研究旨在解决GUI环境庞大且多变导致人工标注不可行的问题，让智能体通过交互自主获取应用特定知识。例如，WebEvolver通过协同进化世界模型以改进自训练和前瞻规划，UI-Evol通过回溯交互轨迹并批判/精炼外部化知识以更好地对齐执行，Mobile-Agent-E则将经验提炼为可复用的“提示”和“快捷方式”以处理复杂移动任务。**本文与这些工作的共同目标是实现智能体的自主能力提升；但本文的创新点在于引入了基于GUI的深度优先搜索探索算法，以系统性地探索和验证环境的单元功能，并利用单元技能的组合性自构建课程学习，从而更高效地学习复合任务和精细动作序列。**

### Q3: 论文如何解决这个问题？

论文通过提出一个名为OSExpert的框架来解决计算机使用代理在复杂任务中效率低下、泛化能力差和难以执行细粒度操作的问题。其核心方法是让代理通过自主探索数字环境来学习可验证的技能，并构建一个持续更新的技能集，从而在推理时实现高效、准确的执行。

整体框架基于一个**GUI深度优先搜索算法**。该算法让代理在目标数字环境中进行系统性探索，以自底向上的方式发现并验证环境中的单元级功能。探索过程由三个协调模块驱动：**规划模块**负责生成假设和计划；**动作模块**执行交互和界面分析；**反馈模块**评估状态并分类。算法从一个初始界面状态开始，将顶层UI元素作为探索节点压入DFS栈，然后以“后进先出”的顺序进行迭代探索。对于每个弹出的节点，环境被重置并重放动作序列以恢复状态，然后执行下一步计划。反馈模块将新状态分类为**中间状态**、**终止状态**或**错误状态**。终止状态对应的已验证计划和动作序列被浓缩为**单元功能技能**并存入技能集；错误状态则触发针对性的批判和重试。

在探索完成后，框架通过两个关键创新来提升推理时的性能与效率。首先，利用学习到的技能集，训练一个**轻量级的LoRA微调规划器**，使其能够单次前向传播就生成完整任务计划，避免了逐步规划的高延迟。其次，引入**技能边界检查**机制：技能集中记录了探索中反复尝试仍失败的单元功能，当新查询映射到这些标记为失败的技能时，代理会提前停止并报错，避免了在推理时进行徒劳的尝试和无效的扩展。

对于细粒度操作难题，论文预先整理了一个**细粒度动作原语数据库**。当探索中触发错误状态并识别出需要精细操作时，反馈模块会根据当前上下文从数据库中检索合适的动作原语模板（例如精确选择文本、像素级拖拽）。如果该原语能成功解决当前问题，则将其验证后的操作流程作为新技能加入技能集，并附上简短的调用条件描述。这种方法大大降低了对大规模人工标注和监督训练的依赖。

此外，框架鼓励代理基于已发现的单元功能，自主提出符合真实用户需求的**复合任务课程**，并将成功完成的复合技能也加入技能集，从而不断扩展其能力。技能集以持续更新的方式组织，支持在后台学习新查询，而非在推理时学习。最终，OSExpert通过这种环境学习范式，使代理具备了即用式的程序性知识，显著提升了任务完成率和效率。

### Q4: 论文做了哪些实验？

论文在OSExpert-Eval基准上进行了广泛的实验评估。实验设置方面，使用了六个交互式GUI环境：LibreOffice Writer、Calc、Impress、GIMP、基于Web的Tableau Public以及内部开发的轻量级文本编辑环境MiniWord。评估时，为所有智能体设置了统一的交互预算，每个任务回合上限为30个交互步骤。

对比方法涵盖了三大类代表性计算机使用智能体：(i) 专用系统（如OpenCUA-7B、Computer-Use-Preview），(ii) 通用多模态大语言模型（如Qwen-3-VL-8B），以及(iii) 智能体框架（如CoAct-1、Agent-S3 w/ GPT-5）。论文提出的OSExpert框架在探索阶段使用了两种配置：1) GPT-5作为高级规划器和反馈模块，UI-TARS-1.5-7B作为动作模块；2) Qwen-3-VL-8B用于所有模块。推理阶段则使用构建的技能集和快速规划器（Qwen-3-4B）。

主要结果以任务平均成功率和平均完成时间衡量。在性能上，现有智能体在复杂任务上表现不佳，成功率多在0%到10%之间。而OSExpert智能体取得了显著提升，在长视野复合技能、未见UI泛化和细粒度动作执行等任务上，成功率提升至约20%-30%（例如，在GIMP上达到0.33，在MiniWord上达到0.37），相比基线实现了约20%的性能增益。在效率上，现有智能体完成任务的时间是人类的5到50倍，而OSExpert智能体大幅缩小了效率差距，将差距减少了约80%。例如，在GIMP的长视野任务中，OSExpert（使用Qwen-3-VL-8B探索）的完成时间为32±0秒，远低于基线智能体（如OpenCUA-7B的169±5秒），接近人类专家的18±5秒。消融实验表明，细粒度动作技能、快速规划器和技能边界检查都对性能与效率提升有贡献。此外，在ScreenSpot-Pro基准的困难子集上，论文的接地细化方法将Qwen-3-VL的单次点击GUI接地能力从0.30提升至0.37。

### Q5: 有什么可以进一步探索的点？

该论文提出的GUI-DFS探索和技能自构建方法虽有效，但仍存在明显局限。首先，其探索过程依赖深度优先搜索，在复杂或动态界面中可能效率低下，且探索范围受初始状态影响，难以保证覆盖所有关键功能单元。其次，技能库的构建基于静态环境探索，缺乏对新界面或任务变化的在线适应能力，迁移性有限。此外，方法未充分考虑多模态交互（如语音、手势）在真实计算机使用中的价值。

未来可探索的方向包括：引入基于强化学习的主动探索策略，使代理能根据任务需求动态调整探索重点；设计增量式技能学习机制，允许代理在任务执行中持续更新和优化技能库；结合大语言模型的世界知识，提升对未知界面的推理和泛化能力。另外，可研究人机协作模式，让代理从人类演示中高效学习复杂技能，从而更接近专家水平。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为OSExpert的计算机使用智能体，旨在通过学习专业操作技能来缩小与人类专家在复杂数字任务上的差距。研究首先定义了一个新基准OSExpert-Eval，揭示了现有通用智能体在任务效率、界面泛化能力和细粒度动作执行上的不足。

为解决这些问题，论文的核心方法是引入GUI深度优先搜索探索算法，让智能体系统地探索环境中的基础功能单元，并利用技能的组合性自构建复合任务课程。同时，通过构建动作原语数据库，智能体在探索中可发现并保存细粒度操作技能。

实验表明，该方法使智能体获得了即用的程序性知识，能一次性规划长轨迹并生成准确动作，同时通过明确能力边界提前终止低效探索。最终，OSExpert在OSExpert-Eval上实现了约20%的性能提升，并将与人类的效率差距缩小了约80%，标志着向专家级计算机使用迈出了重要一步。
