---
title: "MALLVI: A Multi-Agent Framework for Integrated Generalized Robotics Manipulation"
authors:
  - "Iman Ahmadi"
  - "Mehrshad Taji"
  - "Arad Mahdinezhad Kashani"
  - "AmirHossein Jadidi"
  - "Saina Kashani"
  - "Babak Khalaj"
date: "2026-02-18"
arxiv_id: "2602.16898"
arxiv_url: "https://arxiv.org/abs/2602.16898"
pdf_url: "https://arxiv.org/pdf/2602.16898v3"
categories:
  - "cs.RO"
  - "cs.AI"
  - "cs.CV"
  - "cs.LG"
tags:
  - "多智能体系统"
  - "机器人操作"
  - "具身智能"
  - "闭环规划"
  - "视觉语言模型"
  - "任务分解"
  - "错误恢复"
  - "零样本泛化"
relevance_score: 9.0
---

# MALLVI: A Multi-Agent Framework for Integrated Generalized Robotics Manipulation

## 原始摘要

Task planning for robotic manipulation with large language models (LLMs) is an emerging area. Prior approaches rely on specialized models, fine tuning, or prompt tuning, and often operate in an open loop manner without robust environmental feedback, making them fragile in dynamic settings. MALLVI presents a Multi Agent Large Language and Vision framework that enables closed-loop feedback driven robotic manipulation. Given a natural language instruction and an image of the environment, MALLVI generates executable atomic actions for a robot manipulator. After action execution, a Vision Language Model (VLM) evaluates environmental feedback and decides whether to repeat the process or proceed to the next step. Rather than using a single model, MALLVI coordinates specialized agents, Decomposer, Localizer, Thinker, and Reflector, to manage perception, localization, reasoning, and high level planning. An optional Descriptor agent provides visual memory of the initial state. The Reflector supports targeted error detection and recovery by reactivating only relevant agents, avoiding full replanning. Experiments in simulation and real-world settings show that iterative closed loop multi agent coordination improves generalization and increases success rates in zero shot manipulation tasks. Code available at https://github.com/iman1234ahmadi/MALLVI .

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决机器人操作任务规划中，如何将抽象的自然语言指令在动态环境中转化为鲁棒、闭环反馈驱动的执行问题。研究背景是，随着大语言模型（LLMs）的兴起，机器人任务规划领域开始利用其强大的推理和问题分解能力。然而，现有方法存在明显不足：它们通常依赖于单一的专业模型、微调或提示工程，并以开环方式运行，缺乏对环境反馈的鲁棒整合。这使得系统在动态场景中非常脆弱，错误容易累积，且可能产生看似合理但实际无法执行的“幻觉”计划。此外，现有方法在面临开放词汇指令、新物体或新环境时，其语义理解和适应性有限，而依赖单一模型也造成了瓶颈，并可能引发安全担忧。

本文要解决的核心问题是：如何构建一个能够进行闭环反馈、具备强泛化能力且能安全高效地从错误中恢复的机器人任务规划框架。为此，论文提出了MALLVI，一个多智能体大语言与视觉框架。其核心创新在于摒弃单一模型，转而协调多个专门化的智能体（如分解器、定位器、思考器、反射器等）来分别管理感知、定位、推理和高级规划，并通过一个反射器智能体利用视觉语言模型（VLM）持续评估环境反馈，实现闭环控制。该框架能够仅在相关智能体被激活的情况下进行针对性的错误检测与恢复，避免了代价高昂的完全重新规划，从而在零样本操作任务中提升泛化能力和成功率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于大语言模型的机器人任务规划方法、融入视觉反馈的闭环规划方法，以及多智能体协作框架。

在**基于LLM的任务规划方法**中，早期工作如Code-as-Policies将LLM视为将自然语言转换为API调用或代码的翻译器。Inner Monologue引入了环境反馈（成功/失败报告）来指导规划。LLM-Planner和Tree-Planner则利用LLM进行少样本规划或将高级目标分解为可执行的子任务序列。这些方法的核心局限在于其开环规划性质，初始计划一旦生成便缺乏对环境动态的适应能力。

为引入闭环反馈，**视觉反馈驱动的规划方法**应运而生。例如，Replan结合LLM进行初始规划，并利用视觉语言模型（VLM）评估执行成功与否，在失败时触发重新规划。ReplanVLM、LERa、Look Before You Leap以及CoPAL等工作也类似地使用VLM来检测视觉错误、验证前后条件，或进行自我批判与动作修正。然而，这些系统大多是单体式架构，将规划、感知和执行紧密耦合，缺乏模块化和任务感知的分解能力。

在**多智能体协作框架**方面，RoCo开创了多个由LLM控制的机器人进行辩证协作以完成任务规划的先例。Wonderful Team提出了一个多智能体VLLM框架，让多个智能体从视觉场景和任务描述中联合生成动作序列。MALMM则采用了规划器、编码器和监督器三个LLM智能体来执行零样本操作任务，并融入实时反馈和重新规划。这些方法展示了多智能体在复杂问题解决中的潜力。

MALLVI与上述工作的关系和区别在于：它继承了多智能体协作的思想，但通过设计专门化的智能体（分解器、定位器、思考器、反思器等）构建了一个高度模块化的闭环框架。与大多数单体式闭环方法不同，MALLVI的反思器支持针对性的错误检测与恢复，仅重新激活相关智能体，避免了完整的重新规划，从而实现了更高效和鲁棒的感知-推理-执行集成。此外，它整合了开放词汇检测（如OWL-ViT）和通用分割（如SAM）等基础模型，并融入了情境感知的 grounding 能力，以解决指代模糊等问题，超越了单纯依赖基础感知模型的方法。

### Q3: 论文如何解决这个问题？

MALLVI通过构建一个多智能体、闭环反馈驱动的框架来解决动态环境中机器人操作任务规划的鲁棒性和泛化性问题。其核心方法是摒弃单一模型，转而协调多个功能专一的智能体进行模块化协作，并通过视觉语言模型（VLM）进行实时环境评估与迭代修正。

整体框架是一个顺序与闭环结合的流水线。主要模块包括：
1.  **Decomposer（分解器）**：接收高层自然语言指令，将其分解为一系列原子化的子任务序列，每个子任务对应一个基本动作（如移动、抓取），并附有包含对象身份、位置等参数的内存标签。
2.  **Descriptor（描述器，可选）**：与分解器并行运行，使用VLM生成环境的粗粒度空间表示（如图），识别物体及其空间关系，为后续模块提供关键的场景上下文。
3.  **Perceptor（感知器）**：从指令中识别任务相关对象，并标记非目标物体，同时优化抓取策略。
4.  **Grounder（定位器）**：负责物体在图像中的精确定位。它创新性地融合了多个检测器（如GroundingDINO和OwlV2）的输出，并采用基于置信度和与描述器空间图一致性的选择机制，确保即使在部分检测失败时也能提供可靠的边界框。
5.  **Projector（投影器）**：作为工具模块，它将2D视觉感知转化为可执行的3D抓取点。它利用Segment Anything Model (SAM)提取候选抓取点，应用物体特定启发式规则进行选择，并通过深度图和相机模型将其投影到3D空间，最终生成机器人可执行的目标。
6.  **Thinker（思考器）**：一个大型语言模型（LLM），负责将子任务信息转化为具体的可执行参数。它根据内存标签和场景表示，确定抓取/放置的3D位置和旋转。
7.  **Actor（执行器）**：接收思考器的参数，通过预定义API在真实或仿真环境中执行具体的机械臂操作动作。
8.  **Reflector（反射器）**：框架实现闭环反馈的关键创新组件。它是一个VLM，在每个子任务执行后，根据实时视觉反馈评估成功与否。若成功，则继续下一子任务；若失败，则触发重试机制。其创新点在于，它不仅进行简单重试，还能生成失败的自然语言解释、更新共享内存状态，并**选择性重新激活相关的失败智能体**（例如，仅重新运行定位器或思考器），而非进行完整的任务重规划。只有在多次失败后，才会触发描述器进行完整的场景重分析。

该架构的创新点在于：**1）模块化多智能体协同**：将复杂的操作任务分解为由专家智能体处理的子问题，减少了单一模型的幻觉问题，保持了任务专注度和连贯性。**2）基于置信度融合的鲁棒感知**：定位器的多模型融合与置信度加权机制提升了动态非结构化环境下的感知可靠性。**3）靶向错误恢复机制**：反射器能够进行有界的、针对性的恢复，通过选择性重启部分智能体来高效处理错误，避免了代价高昂的全局重规划，从而显著提高了系统的成功率和在零样本任务上的泛化能力。

### Q4: 论文做了哪些实验？

论文在仿真和真实世界环境中进行了实验评估。实验设置方面，MALLVI框架接收自然语言指令和环境图像，通过分解器、定位器、思考器和反射器等专用智能体生成可执行的原子动作，并在动作执行后利用视觉语言模型进行环境反馈评估，形成闭环。

使用的数据集和基准测试包括：1）8项真实世界操作任务（如放置食物、堆叠积木、购物清单等），每项任务重复20次；2）VIMABench基准的4个分区（简单操作、新概念、视觉推理、视觉目标达成），共12项任务，每项重复100次；3）RLBench基准的5项模拟任务（如放入保险箱、堆叠杯子等），每项重复100次。

对比方法包括：MALMM、VoxPoser、ReKep（真实任务）；Wonderful Team、CoTDiffusion、PERIA（VIMABench）；PerAct（RLBench）。此外，论文还进行了消融实验，包括单智能体版本、无反射器版本以及使用不同开源大模型（如Qwen、LLaMA系列）作为骨干的版本。

主要结果与关键数据指标如下：在真实世界任务中，MALLVI在8项任务上的平均成功率最高（如堆叠积木90%、放置食物100%），显著优于基线（如ReKep在堆叠积木为75%）。在VIMABench上，MALLVI在“新概念”和“视觉推理”分区分别达到95%和90%的成功率，优于PERIA的78%和76%。在RLBench上，MALLVI在“放入保险箱”任务达到92%，远超PerAct的44%。消融实验表明，移除反射器会导致性能显著下降（如在RLBench堆叠杯子任务中从83%降至63%），而单智能体版本在多项任务上成功率极低（如真实世界“整理物体”任务为0%），验证了多智能体协调与闭环反馈机制的有效性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其执行层依赖于预定义的原子动作，这限制了机器人在面对未预见的运动学约束、接触动力学或高度动态环境时的适应性。这反映了高层多智能体推理与底层灵活控制之间的权衡。

未来研究方向可以从几个层面展开。在架构层面，可以探索将自适应执行机制（如强化学习或模仿学习控制器）与现有多智能体推理框架深度融合，使原子动作能在部署时实时调整，而非固定不变。在感知层面，引入更先进的感知与 grounding 模块，以提升在包含新物体、复杂纹理或动态场景任务中的性能。此外，当前框架的“反思-恢复”循环虽能激活相关智能体，但如何更精细地定义错误类型并触发更具针对性的恢复策略，也是一个值得探索的点。

结合个人见解，一个可能的改进思路是构建一个“分层自适应”系统：高层保持多智能体分工协作的闭环规划优势，底层则引入一个可学习的“技能库”或“策略模块”。该底层模块能够根据高层指令和环境反馈，在线合成或微调具体的运动轨迹，从而弥合高层符号规划与底层连续控制之间的鸿沟。同时，可以研究如何利用视觉语言模型（VLM）的反馈不仅用于判断任务步骤完成与否，还能用于直接指导底层动作的参数调整，形成更紧密的感知-行动耦合。

### Q6: 总结一下论文的主要内容

该论文提出了MALLVI框架，旨在解决基于大语言模型的机器人任务规划在动态环境中因缺乏环境反馈而表现脆弱的问题。其核心贡献是设计了一个多智能体协同的闭环反馈系统，通过分解任务、感知环境、推理决策和反思调整，实现了更鲁棒的零样本机器人操作。

方法上，MALLVI将任务分解为四个专门智能体：分解器（Decomposer）解析自然语言指令，定位器（Localizer）识别目标物体，思考器（Thinker）生成原子动作，反射器（Reflector）通过视觉语言模型评估执行结果并触发局部恢复而非全局重规划，可选描述器（Descriptor）提供初始状态视觉记忆以增强上下文。

实验表明，这种基于迭代闭环的多智能体协调机制，在模拟和真实场景中均能提升任务成功率和泛化能力，为动态环境下的通用机器人操作提供了可扩展的解决方案。
