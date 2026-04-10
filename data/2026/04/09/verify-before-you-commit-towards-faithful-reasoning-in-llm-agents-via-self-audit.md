---
title: "Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing"
authors:
  - "Wenhao Yuan"
  - "Chenchen Lin"
  - "Jian Chen"
  - "Jinfeng Xu"
  - "Xuehe Wang"
  - "Edith Cheuk Han Ngai"
date: "2026-04-09"
arxiv_id: "2604.08401"
arxiv_url: "https://arxiv.org/abs/2604.08401"
pdf_url: "https://arxiv.org/pdf/2604.08401v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Reasoning"
  - "Faithfulness"
  - "Self-Verification"
  - "Long-Horizon Tasks"
  - "Reasoning Trajectory"
  - "Constraint-Guided Repair"
  - "Multi-Step Decision Making"
relevance_score: 9.0
---

# Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing

## 原始摘要

In large language model (LLM) agents, reasoning trajectories are treated as reliable internal beliefs for guiding actions and updating memory. However, coherent reasoning can still violate logical or evidential constraints, allowing unsupported beliefs repeatedly stored and propagated across decision steps, leading to systematic behavioral drift in long-horizon agentic systems. Most existing strategies rely on the consensus mechanism, conflating agreement with faithfulness. In this paper, inspired by the vulnerability of unfaithful intermediate reasoning trajectories, we propose \textbf{S}elf-\textbf{A}udited \textbf{Ve}rified \textbf{R}easoning (\textsc{SAVeR}), a novel framework that enforces verification over internal belief states within the agent before action commitment, achieving faithful reasoning. Concretely, we structurally generate persona-based diverse candidate beliefs for selection under a faithfulness-relevant structure space. To achieve reasoning faithfulness, we perform adversarial auditing to localize violations and repair through constraint-guided minimal interventions under verifiable acceptance criteria. Extensive experiments on six benchmark datasets demonstrate that our approach consistently improves reasoning faithfulness while preserving competitive end-task performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在长视野决策任务中，其内部推理轨迹可能缺乏“忠实性”的核心问题。研究背景是，随着LLM被广泛部署为自主智能体，它们通过多步推理（如思维链）来规划行动和更新记忆。这些推理轨迹通常被视为智能体内部信念的可信表征，并直接指导后续行动。然而，现有方法存在明显不足：一方面，当前主流策略（如自我一致性、多智能体辩论）依赖于“共识机制”，即通过多数投票从多个候选推理中选取答案。但这种方法错误地将“一致性”等同于“忠实性”，多个候选推理可能共享相同的隐含错误假设或推理模板，导致结构相关但不忠实的信念被反复选择并强化，形成系统性偏差。另一方面，现有方法多在表面文本层面进行重写，缺乏对推理步骤所违反的具体逻辑或证据约束进行识别和定位的能力，也没有可验证的接受标准来确保修正后的信念状态是可靠的。

因此，本文要解决的核心问题是：如何让LLM智能体在将内部推理信念付诸行动或写入记忆之前，能够不依赖于最终任务的成功或简单的多数共识，而是主动地验证并确保其推理过程的忠实性。这里的“忠实性”指推理需符合逻辑和证据约束，避免无根据的假设或无效推断。论文提出的SAVeR框架正是为了应对这一挑战，通过在行动承诺前对内部信念状态进行结构化验证、对抗性审计和最小化修复，旨在实现可信的推理，从而防止不忠实的信念在决策步骤中传播和放大，避免智能体系统出现行为漂移。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、评测类和智能体（Agent）特定研究三类。

在**方法类**研究中，相关工作主要围绕提升大语言模型（LLM）的推理能力展开，例如思维链（CoT）提示、基于程序的推理和最少到最多提示等。然而，这些方法旨在提高任务准确性，并不能保证推理过程的忠实性（faithfulness），生成的解释可能是事后合理化（post-hoc rationalizations）的结果。本文提出的SAVeR框架与这些工作的核心区别在于，它通过结构化的自我审计和验证，在行动承诺前主动确保中间推理步骤的忠实性，而非仅优化最终输出或依赖事后修正。

在**评测类**研究中，已有工作专注于评估LLM推理的忠实性，采用了反事实干预、因果探测和针对性诊断等方法。本文借鉴了这些评估视角，但将其重点从单纯的评估转向了**智能体决策过程中的主动验证与修复机制**。

在**智能体特定研究**中，新兴的研究将LLM视为能进行多步推理、规划和使用工具的智能体。然而，现有框架（如规划或工具使用）虽然暴露了显式的推理轨迹，但并未保证其忠实性，且缓解不忠实推理的方法多为事后（post-hoc）或结果驱动的，例如采样多条轨迹或应用外部评判器。这些方法通常停留在表面层面的轨迹重写或共识聚合，无法识别结构相关但无证据支持的信念状态。本文与这些工作的根本区别在于，它明确设计了在行动前对内部信念状态进行审计和验证的机制，通过对抗性审计定位违规并进行最小干预修复，从而防止不忠实的信念在长期决策中积累和传播，这是针对智能体系统特有挑战的专门解决方案。

### Q3: 论文如何解决这个问题？

论文提出的SAVeR框架通过一个结构化的自我审计与修复流程来解决LLM智能体中推理轨迹不忠实的问题。其核心方法是：在智能体执行动作并更新记忆之前，对其内部信念状态进行验证，确保推理的忠实性。

整体框架包含四个主要模块。首先，**基于角色的多样化信念生成**模块通过实例化多个具有不同推理偏好的“角色”，生成结构多样的候选信念。每个角色根据其特定的指令约束和推理模板，从输入任务中产生一个包含最终主张和完整推理轨迹的信念状态。这旨在暴露不同的推理模式和潜在的失败模式。

其次，**结构感知的信念选择**模块从生成的候选信念中，选取一个结构互补的子集用于后续审计。该模块定义了一个与忠实性相关的结构特征映射，包括推理步骤的粒度、假设管理、验证行为和全局结构类型等特征。通过结合轻量级质量评分函数，构建一个质量感知的多样性核矩阵，并采用k-确定性点过程进行采样，确保选出的信念子集覆盖尽可能多样的、不忠实的推理模式。

第三，**对抗性推理审计**模块对选中的信念进行严格审查，定位违反忠实性的具体推理步骤。审计员应用一系列互补的压力测试策略，从不同逻辑视角检查推理轨迹，并根据固定的模式输出结构化的审计证据。违反类型被归类为一个预定义的集合，包括缺失假设、无效前提、不合理的推断、循环论证、矛盾以及过度概括等。审计结果为每个信念轨迹生成一个违反实例集合和一个不忠实性特征剖面。

最后，**基于约束的最小干预修复**模块根据审计发现的违反实例，对原始推理轨迹进行局部化、最小化的编辑。每个违反实例都对应一个修复约束和明确的验证接受准则。修复过程旨在最小化一个目标函数，该函数同时惩罚对修复约束的违反以及修复后轨迹与原始轨迹之间的编辑距离。审计与修复过程迭代进行，直到没有违反实例为止。修复完成后，智能体综合考虑修复后信念的质量评分和剩余不忠实性特征，选择一个信念用于最终执行和记忆更新。

该方法的创新点在于：1) 通过角色化生成和结构感知选择，系统性地暴露多样化的不忠实推理模式，而非依赖共识机制；2) 将审计过程形式化为对抗性的、基于类型化违反的定位，而非简单的答案生成或聚合；3) 采用基于约束的最小干预修复原则，在纠正错误的同时最大程度保持原始推理的因果结构和可审计性，防止不必要的漂移。

### Q4: 论文做了哪些实验？

论文在六个基准数据集上进行了广泛的实验，以评估所提方法SAVeR在推理忠实性和任务性能上的表现。实验设置方面，研究在零样本推理环境下使用了多个骨干模型（如Qwen 2.5-7B、LLaMA-3.1-8B和LLaMA-3.2-3B），未进行任务特定微调。默认参数包括人物数量M=4，候选审核数K=2，并设置了最多10轮的审核-修复迭代。

使用的数据集涵盖三类推理任务：多跳问答（HotpotQA、2WikiMHQA、MuSiQue）、证据敏感问答（Natural Questions、FEVER）以及局部推理任务（Quoref）。对比方法包括：Vanilla LM（直接生成）、思维链（CoT）、多智能体辩论（MAD）、自我优化（Self-Refine）以及最佳二选一（B-2）。

评估指标分为任务级性能（精确匹配EM和F1分数）和推理忠实性指标。关键忠实性指标包括：平均违规次数（Avg Viol，越低越好）、无违规率（VFR，越高越好）、不忠实步骤率（USR，越低越好）以及修复后残留违规率（Post-Res，越低越好）。

主要结果显示，SAVeR在所有数据集上均显著提升了推理忠实性。例如，在LLaMA-3.1-8B模型上，HotpotQA数据集的Avg Viol从CoT的1.98降至0.37，VFR从24.89%提升至81.36%，USR从27.36%降至9.12%。同时，SAVeR保持了具有竞争力的终端任务性能（如HotpotQA上EM为43.7，F1为52.6）。消融实验进一步证实了各组件（如人物生成、k-DPP选择、审核与修复）对提升忠实性的必要性。可视化分析表明，SAVeR相比MAD能更快、更稳定地降低不忠实步骤率。

### Q5: 有什么可以进一步探索的点？

本论文提出的SAVeR框架在提升推理忠实性方面成效显著，但仍存在一些局限性和值得深入探索的方向。首先，其核心局限在于计算开销：维护多个候选信念状态并进行迭代式审计-修复循环，相比单次推理或轻量级优化策略成本更高，尤其在推理链较短的任务中可能得不偿失。其次，框架缺乏对任务难度的自适应机制，在简单场景中强制进行严格验证可能导致冗余操作。

未来研究方向可从以下几个维度展开：一是开发自适应审计策略，使系统能根据推理不确定性或任务复杂度动态调整验证深度，在忠实性与效率间实现智能权衡；二是探索更高效的信念状态表示与采样方法，例如利用知识蒸馏或稀疏化技术压缩候选空间，减少计算负担；三是将自审计机制与外部知识验证相结合，不仅检查内部逻辑一致性，还引入事实性核查，以应对证据不足或外部约束违反的问题；四是将该框架扩展至多模态或具身智能体场景，研究其在感知-行动循环中如何保证信念更新的可靠性。这些改进有望在更复杂的长期任务中实现更稳健、高效的忠实推理。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型智能体中推理轨迹可能违反逻辑或证据约束，导致不忠实信念在决策步骤间传播并引发系统性行为漂移的问题，提出了自我审计验证推理框架SAVeR。其核心贡献在于将“共识”与“忠实性”解耦，通过在行动执行前对内部信念状态进行显式验证来确保推理的忠实性。方法上，SAVeR首先在忠实性相关的结构空间中生成基于角色的多样化候选信念；接着通过对抗性审计定位违反约束之处，并在可验证的接受准则下进行约束引导的最小干预修复。实验表明，该框架在多个基准数据集上能显著提升推理忠实性，同时保持有竞争力的最终任务性能。这项工作强调了智能体系统中对中间推理进行验证的重要性，为防止不可靠信念的积累提供了有效途径。
