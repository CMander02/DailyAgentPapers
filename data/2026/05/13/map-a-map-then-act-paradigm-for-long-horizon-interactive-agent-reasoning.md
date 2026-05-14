---
title: "MAP: A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning"
authors:
  - "Yuxin Liu"
  - "Ziang Ye"
  - "Yueqing Sun"
  - "Mingye Zhu"
  - "Jinwei Xiao"
  - "Zhuowen Han"
  - "Qi GU"
  - "Xunliang Cai"
  - "Lei Zhang"
date: "2026-05-13"
arxiv_id: "2605.13037"
arxiv_url: "https://arxiv.org/abs/2605.13037"
pdf_url: "https://arxiv.org/pdf/2605.13037v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Long-Horizon Planning"
  - "Cognitive Map"
  - "Environment Understanding"
  - "Interactive Agent"
  - "Map-then-Act"
  - "Framework"
  - "Benchmark"
  - "ARC-AGI"
relevance_score: 9.5
---

# MAP: A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning

## 原始摘要

Current interactive LLM agents rely on goal-conditioned stepwise planning, where environmental understanding is acquired reactively during execution rather than established beforehand. This temporal inversion leads to Delayed Environmental Perception: agents must infer environmental constraints through trial-and-error, resulting in an Epistemic Bottleneck that traps them in inefficient failure cycles. Inspired by human affordance perception and cognitive map theory, we propose the Map-then-Act Paradigm (MAP), a plug-and-play framework that shifts environment understanding before execution. MAP consists of three stages: (1) Global Exploration, acquiring environment-general priors; (2) Task-Specific Mapping, constructing a structured cognitive map; and (3) Knowledge-Augmented Execution, solving tasks grounded on the map. Experiments show consistent gains across benchmarks and LLMs. On ARC-AGI-3, MAP enables frontier models to surpass near-zero baseline performance in 22 of 25 game environments. We further introduce MAP-2K, a dataset of map-then-act trajectories, and show that training on it outperforms expert execution traces, suggesting that understanding environments is more fundamental than imitation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前基于大型语言模型（LLM）的交互式智能体在长时域任务中面临的**延迟环境感知**（Delayed Environmental Perception）问题。现有主流方法（如ReAct、CoT）普遍采用“目标条件化逐步规划”框架，其根本局限在于**将环境理解与任务执行耦合**：智能体只能在执行过程中通过试错被动地推断环境约束（如空间布局、物体动作可供性）。这导致两个关键失败模式：**目标漂移**（陷入局部最优）和**冗余试错**（重复违反环境逻辑的无效动作）。此外，该困境无法仅通过提升推理能力打破（例如在ARC-AGI-3基准上，前沿模型Claude 4.6在零知识交互环境中近乎零分），因为更强大的模型在相同范式下仍然只能从行动副产品中感知环境。

受吉布森的可供性理论（智能体应在行动前直接从空间布局感知动作可能性）和托尔曼的认知地图理论（通过主动探索构建结构化内部表征）启发，本文提出**先规划后行动范式（MAP）**，核心是解耦环境理解与任务执行：在执行前先主动探索并构建结构化的“认知地图”，再基于该地图制定行动，从而以“先环顾四周”替代“边做边想”的时序倒错，从根本上打破认知瓶颈。

### Q2: 有哪些相关研究？

**方法类相关研究**：
现有方法主要分为两类：一是基于专家轨迹模仿学习的数据驱动方法，如通过行为克隆提升决策能力；二是基于强化学习的经验回放方法，从环境交互中学习。本文提出的MAP范式与这些方法不同，它不依赖于外部资源（如专家数据或奖励信号），而是通过自主探索构建环境先验知识，从根本上改变了“先执行后感知”的固有流程。

**记忆机制类相关研究**：
相关工作包括存储历史轨迹的显式记忆、交互历史蒸馏的外部记忆，以及维护技能库检索可复用原语的方法。这些方法都聚焦于执行逻辑优化，而MAP强调认知地图的构建——通过专用映射阶段捕获空间布局和物体可供性，形成结构化的环境表征，解决了现有记忆机制难以组织成一致空间模型的问题。

**模型基强化学习类相关研究**：
虽然模型基方法试图学习环境动力学进行规划，但它们依赖参数化模拟器或潜在动力学模型，与语言智能体和开放环境的兼容性差。MAP则直接构建自然语言化的认知地图，更契合LLM的推理特性。该设计灵感来源于VLM领域证明的显式空间结构建模能提升推理能力的发现。

**评测类工作**：
论文贡献的MAP-2K数据集提供了映射-执行轨迹，实验证明基于该数据训练的模型优于直接学习专家执行轨迹，揭示了理解环境比简单模仿更具根本性。

### Q3: 论文如何解决这个问题？

MAP 通过提出一个“先地图后行动”(Map-then-Act) 的三阶段框架来解决该问题，其核心在于将环境理解与任务执行显式解耦，从而打破传统“边思考边行动”范式导致的认知瓶颈。整体架构包含三个主要阶段：

1.  **全局探索 (Global Exploration)**: 此阶段旨在跨任务发现环境通用规则。Agent 首先作为焦点分析器，从环境描述和少量手动轨迹中提取可操作的探索优先级。然后以探索者身份在训练任务上执行多轮“思考-行动”迭代，并通过反思器从失败中内省。最终，所有探索轨迹被蒸馏成结构化的全局知识库，包含动作语法、交互规则和错误模式，作为跨任务持久化的认知先验。

2.  **任务特定地图构建 (Task-Specific Mapping)**: 基于全局先验，此阶段为当前任务构建结构化认知地图。Agent 通过自适应探索，利用由知识增量和状态新颖性组成的双重内在奖励来减少认知不确定性。当双收敛停止准则（要求知识增量和探索多样性同时收敛）被触发时，关键信息提取器对探索轨迹进行结构化分析，生成包含空间布局、物体-动作可供性和游戏规则的任务特定认知地图。

3.  **知识增强执行 (Knowledge-Augmented Execution)**: 在最终执行阶段，Agent 的行动生成同时依赖于全局先验和任务特定认知地图，从而用基于结构化因果关系知识的主动推理替代了传统逐步范式中的被动试错模式。

该框架的关键技术包括：基于因果干预的双阶段去耦范式、结构化 RPP 提示协议、双重内在奖励驱动的自适应探索，以及一个用于内化能力的教师-学生蒸馏训练方法。其创新点在于通过因果视角提出“先理解环境再行动”原则，并构建了一个即插即用的三阶段系统，显著提升了智能体在长时域交互任务中的泛化能力。

### Q4: 论文做了哪些实验？

论文在四个基准上进行了实验：ALFWorld（家务任务）、TextCraft（合成制造）、ScienceWorld（科学推理）和ARC-AGI-3（抽象回合制游戏，无显式规则）。对比方法包括标准ReAct（逐步规划）、CoMAP（非分阶段的同时映射与执行）以及SFT-Execution（ACT-4B，在专家执行轨迹上微调）。主要结果如下：在ALFWorld、TextCraft和ScienceWorld上，MAP显著优于ReAct和CoMAP。例如，使用Qwen3-4B-Thinking时，MAP在ALFWorld上达71.5%（ReAct为58.5%，CoMAP为61.9%）；在TextCraft上达59.6%（ReAct为35.6%）；在ScienceWorld上达11.4%（ReAct为1.5%）。MAP-4B（在MAP-2K上微调）在ALFWorld上达87.1%，远优于ACT-4B的78.2%。在ARC-AGI-3上，ReAct近乎零基线，而MAP在22/25个游戏中取得正分（如TU93得3.34分，ReAct为0.00）。消融实验表明，移除阶段1（全局探索）或阶段2（任务映射）均会降低性能，且空间布局和物体-动作关联性均为必要组件。探索预算实验显示10步后性能稳定。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：第一，MAP框架在全局探索阶段仍依赖随机或简单启发式策略，在复杂动态环境中可能无法高效构建高质量认知地图；第二，当前仅验证了结构化环境（如游戏）中的有效性，对非结构化、部分可观测的真实物理世界（如机器人操作）的泛化能力尚未验证；第三，MAP-2K数据集规模有限，且任务特定映射阶段需要人工定义地图结构，限制了自动化程度。

未来可探索的方向包括：(1) 引入强化学习或元学习优化全局探索策略，实现自适应探索；(2) 将认知地图扩展为可进化结构，支持在线更新与多模态（视觉、语言、触觉）融合；(3) 探索地图压缩与抽象表示技术，降低长程任务中的记忆负担；(4) 研究地图构建与任务执行之间的互促进机制，例如利用执行反馈主动修正地图。(5) 将MAP与世界模型结合，使代理不仅能理解当前环境，还能预测环境变化，实现前瞻性推理。此外，将该范式扩展到多智能体协作场景，研究分布式认知地图的构建与融合也极具价值。

### Q6: 总结一下论文的主要内容

这篇论文提出了MAP（Map-then-Act）范式，旨在解决现有LLM智能体在长程交互推理中的“延迟环境感知”问题。传统范式将环境理解与任务执行耦合，导致智能体只能通过试错被动获取环境知识，形成认知瓶颈，表现为目标漂移和冗余试错。MAP受人类可供性感知和认知地图理论启发，将环境理解主动前置，包含三个阶段：全局探索（提取跨任务通用先验）、任务特定映射（构建结构化认知地图）和知识增强执行（基于地图进行决策）。实验表明，MAP无需参数更新即可在ALFWorld、TextCraft、ScienceWorld及ARC-AGI-3基准上一致提升成功率并减少交互步数，尤其在ARC-AGI-3的25个游戏环境中，22个场景从前沿模型近零基线获得显著提升。此外，基于MAP-2K数据集微调的MAP-4B模型性能优于传统专家轨迹训练模型。核心贡献在于证实了主动环境理解比模仿执行更为根本。
