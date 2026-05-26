---
title: "Hera: Learning Long-Horizon Coordination for Device-Cloud Collaborative LLM Agents"
authors:
  - "Yuxin Zhang"
  - "Mengxue Hu"
  - "Zheng Lin"
  - "Xiaoyi Fan"
  - "Fan Xie"
  - "Zihan Fang"
  - "Jing Yang"
  - "Wenjun Zhu"
  - "Zhiwen Chen"
  - "Chengfei Lv"
  - "Zhe Chen"
date: "2026-05-23"
arxiv_id: "2605.24598"
arxiv_url: "https://arxiv.org/abs/2605.24598"
pdf_url: "https://arxiv.org/pdf/2605.24598v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "Device-Cloud Collaboration"
  - "LLM Agent Coordination"
  - "Long-Horizon Tasks"
  - "Reinforcement Learning"
  - "Imitation Learning"
  - "Step-Level Routing"
  - "Multi-Agent Systems"
  - "Performance-Cost Trade-off"
relevance_score: 9.5
---

# Hera: Learning Long-Horizon Coordination for Device-Cloud Collaborative LLM Agents

## 原始摘要

Large language model (LLM) agents excel at solving complex long-horizon tasks through autonomous interaction with environments. However, their real-world deployment faces a fundamental device--cloud dilemma: on-device models are efficient but often brittle, while cloud models are stronger but costly in computation. State-of-the-art LLM device--cloud routers usually make coarse task-level decisions, which cannot adapt to the changing difficulty of multi-step agent interactions. To address this issue, we present Hera, a step-level device--cloud LLM agent coordinator for long-horizon tasks achieving a strong performance--cost Pareto frontier. Hera adopts a novel two-stage training paradigm: (1) imitation learning for cold-start, followed by (2) reinforcement learning that jointly optimizes task success and cloud usage efficiency. The first stage casts step-level routing as a supervised classification problem: the device agent is replayed on cloud trajectories, with each state labeled by the agreement between device and cloud actions. In the second stage, we perform cost-aware reinforcement learning by grouping identical states across trajectories and updating Hera with labels favoring higher expected return and fewer future cloud calls. We evaluate Hera on ALFWorld, WebShop, and AppWorld, where it consistently outperforms prior methods, achieving 92.5% of the cloud-only success rate with cloud use in only 46.3% of steps.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决设备-云端协同的大语言模型（LLM）智能体在长周期任务中面临的核心困境：设备端小模型在复杂推理和多步规划中表现脆弱（易出错、缺乏长期连贯性），而云端大模型虽然性能强大，但会引入高延迟和昂贵的计算成本。现有方法（如任务级路由器）通常将每个请求视为原子单元，在任务启动前一次性决定整个任务由设备还是云端执行。这种粗粒度的路由策略无法适应长周期智能体交互场景中任务难度随环境状态动态变化的特性，导致要么浪费云端资源（处理简单步骤），要么因设备端能力不足而失败。

为弥补这一不足，本文提出了Hera，一个**步骤级别的设备-云端智能体协调器**。其核心创新在于将路由决策细化到每个交互步骤，通过识别关键步骤并仅将少量“困难步骤”卸载到云端，便能在达到接近纯云端成功率的条件下显著降低云端调用成本。Hera的设计直面长周期任务中步骤间依赖性强、难度动态变化的挑战，通过一个两阶段训练范式（先模仿学习冷启动，后强化学习联合优化任务成功率和云端使用效率），实现了性能和成本之间的强帕累托最优边界。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为两类：

**1. LLM智能体研究：** 本文关注通过监督微调和强化学习使LLM智能体能够从环境交互中学习，从而执行复杂长时任务。与这些工作相比，Hera专注于解决设备-云协同场景下的长时任务协调问题，而非单一智能体的训练或推理优化。

**2. 设备-云LLM协同研究：** 现有方法如FrugalGPT、Hybrid LLM、Eagle和RouteLLM，主要通过请求级路由或基于历史相似性/偏好预测来选择模型，以平衡输出质量与成本。MinionS则采用更紧密的协同，让云端分解或验证子任务，设备端执行。然而，这些方法均基于粗糙的任务级或请求级路由，难以适应长时任务中环境动态变化和步骤难度差异。与它们不同，Hera提出了步骤级协调方案，通过两阶段训练（模仿学习+成本感知强化学习）实现了更细粒度的决策，能在步骤层面动态分配设备或云端模型，从而在任务成功率和云使用成本间取得更优的Pareto前沿。

### Q3: 论文如何解决这个问题？

Hera的核心方法是通过**步骤级设备-云端协调**解决长程任务中设备端与云端模型之间的性能-成本权衡问题。其架构设计围绕一个二阶段训练范式展开，整体框架包含设备端Agent、云端Agent和一个协调器Hera，后者负责在每一步决策设备是否调用云端。

第一阶段是**模仿学习的冷启动**。Hera将步骤级路由建模为监督分类问题：在云端执行轨迹上回放设备Agent，对每个状态标注设备动作与云端动作的一致性。如果设备动作与云端一致，则标记为“本地执行”；否则标记为“需云端调用”。这使Hera能从专家轨迹中学习初始策略。

第二阶段是**成本感知强化学习**。Hera通过分组相同状态（跨轨迹中状态编码相同的点），对这些状态组更新标签，优先选择能获得更高期望回报且未来云端调用次数更少的决策。具体地，对于每个状态组，若选择本地执行带来的累计奖励>云端执行，则倾向本地；否则倾向云端。奖励函数同时考虑任务成功（+1分）和云端调用成本（每步调用扣减一定惩罚）。这种分组更新机制避免了传统RL的采样低效问题，使Hera能高效优化长期协调策略。

关键技术包括：状态编码（通过设备Agent的隐藏层输出生成，确保状态-动作映射一致性）、动态标签更新（根据全局回报比较调整决策边界）、以及步骤级微调（仅对协调器参数进行少量更新，保持设备Agent和云端Agent权重冻结）。实验表明，Hera在ALFWorld、WebShop等基准上达到92.5%的云端成功率，但仅使用46.3%的步骤调用云端，显著优于任务级路由方法。

### Q4: 论文做了哪些实验？

论文在三个长周期任务基准（ALFWorld 3,827个任务、WebShop 12k指令、AppWorld 750个任务）上评估了Hera。对比基线包括设备-only、云端-only、随机步级路由（cloud概率0.3-0.5）、以及Eagle、FrugalGPT、HybridLLM、RouteLLM等最新路由方法。设备模型为Qwen2.5-7B-Instruct，云端为Qwen-Max，路由器基于Qwen2.5-0.5B（494M参数）训练。主要结果显示：Hera在ALFWorld/WebShop/AppWorld上分别达到云端的86.1%/34.1%/19.7%成功率，而随机路由（0.5概率）仅为79.1%/27.6%/5.4%；Hera仅调用46.3%的云端步骤，却实现了云端92.5%的平均成功率。消融实验表明：仅有模仿学习的Hera（w/o RL）比随机路由提升0.8%-3.8%成功率并减少云调用；仅有强化学习的Hera（w/o IL）因缺乏冷启动表现较差；两阶段联合训练使成功率和云效率最优。微基准测试显示：Hera每步仅增加61ms开销，在更复杂任务中（如AppWorld）识别关键状态提升性能，其路由模式比RouteLLM更清晰区分难易步骤。

### Q5: 有什么可以进一步探索的点？

Hera在step-level路由上取得了显著进展，但现有训练依赖离线轨迹的固定状态分组，忽略了在线环境中状态分布的动态变化，可能导致泛化能力不足。未来可探索基于在线强化学习的自适应路由更新机制，让Hera能实时从新轨迹中学习并调整决策边界。此外，当前模型将设备端和云端行动的一致性作为硬标签，未考虑设备模型自身能力的持续提升——例如通过知识蒸馏或微调，设备端能力可能随时间增强。因此，设计一个动态能力感知的路由策略，将设备端的实时置信度或渐进式学习进度纳入决策，可进一步提高协同效率。最后，多步依赖的博弈性尚未被充分建模，可尝试引入层次化强化学习，将任务分解为子目标，并让路由决策与子目标完成度耦合，避免短视的局部最优。

### Q6: 总结一下论文的主要内容

本文针对长时域LLM智能体在设备-云端协同部署中面临的性能-成本权衡问题，提出了一种名为Hera的轻量级步级协调器。现有方法仅在任务级别进行粗粒度路由决策，无法适应多步交互中动态变化的难度。Hera采用两阶段训练范式：首先通过模仿学习对设备智能体在云端轨迹上进行回放，将步级路由建模为基于设备-云端动作一致性的监督分类问题实现冷启动；随后通过强化学习对相同状态进行分组，利用偏好标签联合优化任务成功率和云端调用成本。在ALFWorld、WebShop和AppWorld等基准测试中，Hera以仅46.3%的云端步数实现了云端全量执行92.5%的成功率，显著优于现有方法。这是首个实现步级设备-云端协调的工作，为长时域智能体任务提供了性能-成本帕累托最优解。
