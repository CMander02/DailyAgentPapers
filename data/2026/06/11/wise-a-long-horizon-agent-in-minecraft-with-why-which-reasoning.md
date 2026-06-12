---
title: "WISE: A Long-Horizon Agent in Minecraft with Why-Which Reasoning"
authors:
  - "Renmin Cheng"
  - "Changhao Chen"
date: "2026-06-11"
arxiv_id: "2606.12852"
arxiv_url: "https://arxiv.org/abs/2606.12852"
pdf_url: "https://arxiv.org/pdf/2606.12852v1"
categories:
  - "cs.AI"
tags:
  - "Minecraft"
  - "Embodied Agent"
  - "Hierarchical Agent"
  - "Long-Horizon Planning"
  - "Causal Reasoning"
  - "Episodic Memory"
  - "Task Scheduling"
  - "LLM-Augmented Agent"
relevance_score: 8.5
---

# WISE: A Long-Horizon Agent in Minecraft with Why-Which Reasoning

## 原始摘要

Rapid advances have been made in developing general-purpose embodied agent in environments like Minecraft through the adoption of LLM-augmented hierarchical approaches. Despite their promise, low-level controllers often become performance bottlenecks due to repeated execution failures. We argue that a key limitation is not only the lack of episodic memory, but also the decoupling of \textit{what-where-when} memory from \textit{which-why} reasoning. To address this, we propose \textbf{WISE} (Which-Why Informed Semantic Explorer), a long-horizon agent framework with an enhanced low-level controller equipped with a Causal Event Graph that augments episodic memory with explicit causal structure linking observations to task relevance. Unlike prior work such as MrSteve, which relies on feature similarity for retrieval, WISE enables robust recall under viewpoint changes and supports opportunistic task reordering through causal reasoning. Building on this memory, we propose an Opportunistic Task Scheduler that dynamically re-prioritizes subtasks when causally relevant opportunities are detected. We further equip WISE with a multi-scale progressive exploration strategy to provide spatially comprehensive observations for downstream reasoning. Experiments show that WISE largely improves task success and efficiency on long-horizon sparse tasks, particularly in settings requiring adaptive decision-making.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的层次化具身智能体在处理长期任务（如Minecraft中的“获得牛肉”）时，低层控制器频繁成为性能瓶颈的问题。研究背景是，现有方法主要关注高层规划，而低层控制器存在两个关键不足：一是缺乏能够结合因果推理的语义记忆，现有的“什么-哪里-何时”记忆（如MrSteve的PEM）仅依赖视觉相似性进行检索，在视角变化时鲁棒性差，且无法理解观察的因果含义（如看到奶牛对“获得牛肉”任务的意义）；二是探索、记忆和规划模块相互脱节，低层控制器只能机械执行固定子目标序列，无法根据新信息动态调整优先级（如遭遇奶牛时不能立刻抓住机会）。为此，论文提出WISE框架，核心是通过因果事件图增强低层控制器，使其不仅能记忆观察，还能通过VLM提取的因果结构进行“为什么-哪个”推理，并引入机会主义任务调度器，根据因果相关性动态重排子任务优先级。最终目标是提升长期稀疏奖励任务的成功率和效率，实现自适应的决策。

### Q2: 有哪些相关研究？

- **方法类相关工作**：早期工作如VPT、Steve-1、GROOT等聚焦于从视频或文本中学习简单任务的策略模型。近期STEVE系列、Odyssey、LARM等探索了分层架构与规划粒度。ADAM和Steve-Evolving通过因果图或执行诊断提升控制器能力。本文的**Causal Event Graph**区别于ADAM的高层知识积累，专门将低层级观察与高层目标通过因果边显式关联，且集成于低层级控制器的动态调度中，而非仅用于知识存储。
- **记忆系统相关工作**：Voyager、GITM、JARVIS-1等主要存储高层规划经验（如可复用技能或成功计划），Optimus-1则混合存储多模态轨迹。MrSteve的**Place Event Memory (PEM)** 首个面向低控制器的记忆系统，但基于原始视觉特征检索，无法应对视角变化。本文在其上构建**因果事件图**，支持基于因果关系的检索，显著提升对任务相关机会的感知与重调度能力。
- **探索策略相关工作**：基于计数的探索存在覆盖间隙，基于边界的方法忽略内部区域，NovelCraft等对生成世界中的新物体适应不足。本文的**多尺度渐进探索**首次在Minecraft中融合四叉树索引（全局效率）、边界评分（边界感知）与Voronoi分解（局部完备性），综合解决了现有方法的缺陷。

### Q3: 论文如何解决这个问题？

WISE的核心方法是通过构建因果事件图来增强低级控制器的记忆与推理能力，从而实现长时域任务中的自适应决策。整体框架包含三个主要模块：记忆模块、求解器模块和机会任务调度器。记忆模块由两部分组成：一是短期几何记忆，使用MineCLIP编码视觉特征并通过DP-Means聚类形成事件簇，基于视觉相似性进行快速检索；二是因果事件图，这是一种创新的语义知识图谱，通过混合关键帧提取策略（结合聚类和熵方法）选择代表性观察帧，然后利用VLM（如GPT-4o）分析关键帧，提取实体、推断因果关系（如“牛→可以获得→牛肉”）和空间共现关系，从而将观察转化为结构化语义知识。求解器模块中的模式选择器根据记忆检索结果在探索和执行模式间切换。创新点在于机会任务调度器，它集成当前观察、待办子目标和因果记忆，通过优先级评分函数（包含紧迫性、导航成本和因果相关性）动态重排序子任务，其中因果相关性权重最高。当检测到因果相关的机会时（如遇到牛而任务中有获取牛肉），调度器可中断当前任务立即执行更有价值的子任务，从而避免冗余移动。此外，多尺度渐进探索策略为下游推理提供全面的空间观察。

### Q4: 论文做了哪些实验？

论文在Minecraft中通过MineRL平台进行了四组实验。实验设置采用四块NVIDIA RTX 4080 GPU，使用GPT-4o作为视觉语言模型，MineCLIP作为语义特征提取器。

**大规模探索性能评估**：测试多尺度探索策略的有效性。主要对比Steve-1和MrSteve，结果显示WISE在探索覆盖率和效率上显著优于基线。

**稀疏任务完成实验**：设置了ABA-Sparse（顺序任务）和ABC-Sparse（非顺序任务）两个场景，评估记忆检索和自适应规划能力。WISE在任务成功率上大幅领先：在ABA-Sparse中WISE达78.3%，MrSteve为45.2%；在ABC-Sparse中WISE达71.5%，MrSteve仅38.1%。同时WISE的完成步数也更少。

**消融实验**：对比WISE与两个消融变体——WISE(PEM+Graph)（去除探索和调度器）和WISE(Quadtree-Based)（仅用全局探索）。结果显示完整WISE在所有指标上最优，验证了各组件的重要性。PEM+Graph变体表现优于MrSteve，证明因果事件图的有效性。

所有方法均基于纯视觉观察，排除了Voyager、JARVIS-1等具有API特权的智能体。

### Q5: 有什么可以进一步探索的点？

论文的主要局限性在于：（1）因果事件图依赖GPT-4o进行语义构建，成本高且可能引入幻觉；（2）多尺度探索策略虽能获取全面观察，但区域划分的粒度缺乏自适应机制；（3）主动式任务调度器的机会检测依赖于预定义规则，在高度动态场景下可能错过突发性机会。

未来可探索方向包括：1）引入在线学习机制使因果图能够自主演化，例如结合强化学习信号自动更新因果权重；2）设计基于好奇心驱动的动态探索策略，根据当前知识状态自动调整区域扫描密度；3）扩展到其他视觉输入或非结构化环境（如厨房操作任务）；4）探索更轻量级的视觉-语言模型替代方案，并验证其在弱计算平台上的迁移能力。此外，将因果推理与分层强化学习结合，可能进一步解开机会检测的时间尺度依赖问题。

### Q6: 总结一下论文的主要内容

WISE提出了一种针对Minecraft等环境中长时域具身智能体任务的新框架，核心解决低层控制器因重复执行失败导致的性能瓶颈问题。问题定义在于现有方法缺乏情节记忆，且将“是什么-在哪里-什么时间”的记忆与“哪一个-为什么”的推理割裂。方法上，WISE引入了因果事件图增强情节记忆的显式因果结构，链接观察与任务相关性，相比MrSteve等依赖特征相似度检索的方法，能在视角变化下实现鲁棒召回。基于此记忆，WISE设计了机会主义任务调度器，在检测到因果相关的机会时动态调整子任务优先级，并采用多尺度渐进探索策略获取空间上全面的观察。主要结论是，WISE在长时域稀疏任务上显著提升了任务成功率和效率，尤其在需要自适应决策的场景中表现突出，贡献在于提出了因果推理与记忆结合的框架，推动了具身智能体在复杂开放世界中的规划能力。
