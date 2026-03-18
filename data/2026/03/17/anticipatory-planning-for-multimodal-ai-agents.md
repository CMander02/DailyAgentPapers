---
title: "Anticipatory Planning for Multimodal AI Agents"
authors:
  - "Yongyuan Liang"
  - "Shijie Zhou"
  - "Yu Gu"
  - "Hao Tan"
  - "Gang Wu"
  - "Franck Dernoncourt"
  - "Jihyung Kil"
  - "Ryan A. Rossi"
  - "Ruiyi Zhang"
date: "2026-03-17"
arxiv_id: "2603.16777"
arxiv_url: "https://arxiv.org/abs/2603.16777"
pdf_url: "https://arxiv.org/pdf/2603.16777v1"
categories:
  - "cs.AI"
tags:
  - "Multimodal Agent"
  - "Planning"
  - "Reinforcement Learning"
  - "Tool Use"
  - "Anticipatory Reasoning"
  - "Trajectory Forecasting"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# Anticipatory Planning for Multimodal AI Agents

## 原始摘要

Recent advances in multimodal agents have improved computer-use interaction and tool-usage, yet most existing systems remain reactive, optimizing actions in isolation without reasoning about future states or long-term goals. This limits planning coherence and prevents agents from reliably solving high-level, multi-step tasks. We introduce TraceR1, a two-stage reinforcement learning framework that explicitly trains anticipatory reasoning by forecasting short-horizon trajectories before execution. The first stage performs trajectory-level reinforcement learning with rewards that enforce global consistency across predicted action sequences. The second stage applies grounded reinforcement fine-tuning, using execution feedback from frozen tool agents to refine step-level accuracy and executability. TraceR1 is evaluated across seven benchmarks, covering online computer-use, offline computer-use benchmarks, and multimodal tool-use reasoning tasks, where it achieves substantial improvements in planning stability, execution robustness, and generalization over reactive and single-stage baselines. These results show that anticipatory trajectory reasoning is a key principle for building multimodal agents that can reason, plan, and act effectively in complex real-world environments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态智能体在复杂、长视野任务中缺乏前瞻性规划能力的问题。研究背景是，尽管多模态智能体在图形用户界面交互和工具使用方面取得了显著进展，但现有系统大多是反应式的：它们仅基于当前观察决定下一步动作，缺乏对未来状态或长期目标的推理。这种“走一步看一步”的模式导致智能体在需要多步连贯操作的任务中容易偏离目标，难以可靠地完成高层次、多步骤的复杂任务。

现有方法主要有两种思路，但均存在不足。一是无模型强化学习，它通过设计子目标或最终结果的奖励来训练智能体，但难以定义能泛化到多样开放任务的、面向推理的奖励函数。二是基于模型的规划，它让智能体通过世界模型模拟未来动作序列和环境状态变化，但在视觉丰富且交互复杂的环境中构建准确的世界模型极其困难。

因此，本文要解决的核心问题是：如何高效地训练多模态智能体，使其能够针对复杂的长视野任务发展出自适应的前瞻性推理能力？为此，论文提出了TraceR1框架，其核心创新在于将长视野的轨迹推理与基于执行的精细化调整相结合。该框架通过两阶段强化学习，首先在轨迹层面进行优化，学习全局一致的动作序列规划，然后利用工具代理的执行反馈进行精细化微调，确保每个预测步骤的可行性和精确性，从而弥补了高层推理与底层执行之间的鸿沟。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在**方法类**研究中，相关工作主要包括两类。一是**智能体框架**，如Aria-UI、UGround、SeeClick等，它们通常采用结构化规划流程，依赖强大的专有模型（如o3或Claude 4）作为规划器来生成高层动作提案，而由特定领域模块负责在GUI界面上的具身化和执行。这些框架虽展现了多步推理能力，但其进展很大程度上取决于底层专有规划器，而非提升智能体内在的规划能力。它们强调基于指令的精确动作执行，而非轨迹级规划。本文的TraceR1则直接通过强化学习训练大模型，使其获得前瞻性规划能力。二是**通用智能体**，如UI-TARS、Magma、SeeAct、CogAgent等，它们基于大型视觉-语言模型构建，致力于在多样化GUI环境中实现统一的交互控制和推理。近期一些R1风格的方法也引入了强化信号来增强推理。与这些方法仍依赖具身化监督、强调训练中精确执行不同，本文方法纯粹聚焦于规划，并引入了一个更通用的训练框架来强化智能体规划、理解和预测未来状态的能力。

在**应用类**研究中，核心是**工具使用**能力。相关研究一方面通过大规模多模态指令微调，让模型从合成或整理的轨迹中学习工具选择和组合；另一方面构建端到端架构，将视觉-语言模型与真实可执行工具或交互环境耦合，实现逐步控制和自适应推理。这些方法显著提升了工具调用和多模态集成能力，但主要强调执行可靠性或反应式协调。相比之下，本文方法专注于通过训练模型预测和组织未来的工具使用行为来强化智能体的规划能力，仅将具身化反馈用于执行验证而非主要学习信号，从而实现更有效、更审慎的工具使用推理。

在**评测类**方面，现有研究建立了多个在线/离线计算机使用基准和多模态工具使用推理任务，本文正是在涵盖七项此类基准的评估中验证了所提框架的优越性。

### Q3: 论文如何解决这个问题？

论文通过一个名为TraceR1的两阶段强化学习框架来解决多模态智能体缺乏前瞻性规划和长期推理能力的问题。其核心方法是先进行轨迹层面的优化以提升全局一致性，再进行基于执行的微调以确保每一步的准确性和可行性。

整体框架是一个“规划-执行”循环。在推理时，智能体接收当前观测（如图形界面截图）和用户指令，首先预测一个未来多步的轨迹（包含动作类型和步骤指令），但只执行第一步；执行后获得环境反馈，再重新进行规划。这种迭代式的前瞻机制是其核心架构。

具体训练分为两个主要阶段：
1.  **第一阶段：前瞻性轨迹优化**。此阶段旨在解决传统监督微调（SFT）只优化单步似然而忽略全局一致性的问题。模型在给定当前状态和历史后，预测一个未来短视界的完整动作序列（轨迹）。训练使用轨迹级别的强化学习，奖励函数衡量预测轨迹与参考轨迹的整体对齐度。该奖励包含两部分：一是每一步预测动作与真实动作的对齐度（通过`sim`函数衡量），二是对轨迹中重复或循环动作的惩罚（`rep`函数）。通过组相对策略优化（GRPO）目标进行优化，使模型学会在执行前进行多步推理，生成全局更连贯的计划。

2.  **第二阶段：基于执行的强化微调**。此阶段旨在解决第一阶段可能产生的“纸上谈兵”问题，即规划虽连贯但具体执行可能失败。模型同样进行多步预测，但只将第一步预测的动作交给一个冻结的工具代理（如GUI执行器或API工具）去实际执行。然后，将工具执行的结果（如点击坐标、文本答案）与真实结果进行比较，计算一个基于执行的步骤级奖励（例如，坐标匹配或答案匹配）。同样使用GRPO进行微调，但奖励替换为这个接地气的执行奖励。这确保了模型在保持前瞻规划能力的同时，每一步的预测都更精确、更可执行。

关键创新点在于：
*   **两阶段解耦训练**：将“全局规划一致性”与“单步执行准确性”这两个目标分离并分别优化，避免了单一目标训练的冲突。
*   **轨迹级强化学习**：引入基于多步预测序列的奖励，强制模型进行短视界的前瞻性推理，这是实现连贯多步规划的关键。
*   **离线接地微调**：利用冻结的工具代理和离线轨迹数据，在无需在线环境交互的高成本下，实现对执行准确性的微调，提升了方法的实用性和鲁棒性。
*   **轻量级历史上下文**：使用最近K步的抽象化历史（而非原始截图），在提供必要时序信息的同时避免了冗余。

通过这种两阶段框架，TraceR1使智能体具备了“走一步，看多步”的能力，从而在复杂任务中实现了更稳定、更鲁棒的规划与执行。

### Q4: 论文做了哪些实验？

论文在实验部分设置了全面的评估，涵盖GUI智能体基准和工具使用基准。实验模型TraceR1基于Qwen3-VL-8B-Thinking初始化，采用EasyR1框架进行两阶段训练：第一阶段使用来自AgentNet、AndroidControl等数据集的轨迹进行轨迹级强化学习；第二阶段基于UI-TARS-7B等工具代理的执行反馈进行接地强化微调。

评估在7个基准上进行。在线GUI基准包括OSWorld-Verified（桌面操作）和AndroidWorld（移动端，116个任务），以任务成功率衡量；离线GUI基准包括AndroidControl-High、GUI-Odyssey（203个任务）和Multimodal-Mind2Web，以步骤成功率衡量。多模态工具使用与推理基准包括GTA（229个任务，评估感知、逻辑等）和GAIA（446个任务，分三个难度级别）。

对比方法包括三大类：专有模型（如GPT-4o、Claude）、结合专有模型的智能体系统（如OmniParser-v2.0 w/ GPT-4o）以及开源模型（如OS-Atlas、QwenVL系列、UI-TARS变体）。

主要结果：在在线基准上，TraceR1显著提升了基础模型的性能，例如将UI-TARS-1.5-7B在OSWorld-Verified上的成功率从27.4%提升至30.9%（相对提升12.8%）。在离线GUI基准上，TraceR1在AndroidControl-High上达到75.3%的步骤成功率，优于其他开源模型，相比GUI-R1等模型提升超过40%。在多模态基准上，TraceR1在GAIA上获得40.2%的答案准确率，超越GPT-4o（33.4%）和Qwen3-VL-8B（31.5%）；在GTA上获得56.7%的答案准确率、65.7%的工具准确率和87.4%的代码执行率，显示出强大的工具使用能力。消融实验表明，移除第二阶段训练会导致性能平均下降约6%，而预测轨迹长度和奖励设计组件（如重复惩罚λ_rep和时间折扣γ）对性能有重要影响。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其短视界轨迹预测主要提供局部修正，难以从根本上重塑智能体对长期任务可行性和结构的理解。未来研究可探索多轮或分层规划机制，将轨迹预测与记忆、内部状态或世界模型的更新相结合，使智能体能够动态修订和整合计划。此外，可将该框架扩展至具身或混合工具使用环境，其中成功行为需要在更长的时间尺度上协调感知、推理与行动。结合个人见解，可能的改进思路包括引入元认知机制，使智能体能够评估自身预测的可靠性并调整规划策略；或融合符号推理与深度学习，以提升抽象任务层面的规划连贯性。这些方向有望推动规划系统不仅预测未来结果，还能在多个抽象层次上组织预测，实现更鲁棒和可扩展的决策能力。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为TraceR1的两阶段强化学习框架，旨在解决现有多模态智能体在规划上存在的局限性。当前大多数系统是反应式的，仅孤立地优化单个动作，缺乏对未来状态和长期目标的推理，导致其难以可靠地完成高层次、多步骤的复杂任务。

论文的核心贡献是引入了“预期性规划”这一关键思想。其方法分为两个阶段：第一阶段进行轨迹层面的强化学习，通过奖励机制确保预测出的整个动作序列具有全局一致性；第二阶段进行基于执行的强化微调，利用冻结的工具智能体提供的执行反馈，来优化每一步动作的准确性和可执行性。

实验结果表明，TraceR1在涵盖在线/离线计算机使用以及多模态工具推理的七个基准测试中，均显著优于反应式和单阶段的基线模型。它在规划稳定性、执行鲁棒性和泛化能力上取得了实质性提升，证明了预期性轨迹推理是构建能够在复杂现实环境中有效推理、规划和行动的多模态智能体的关键原则。
