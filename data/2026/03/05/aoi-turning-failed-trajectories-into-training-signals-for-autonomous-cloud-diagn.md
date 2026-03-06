---
title: "AOI: Turning Failed Trajectories into Training Signals for Autonomous Cloud Diagnosis"
authors:
  - "Pei Yang"
  - "Wanyi Chen"
  - "Asuka Yuxi Zheng"
  - "Xueqian Li"
  - "Xiang Li"
  - "Haoqin Tu"
  - "Jie Xiao"
  - "Yifan Pang"
  - "Dongdong Zhang"
  - "Fuqiang Li"
  - "Alfred Long"
  - "Bill Shi"
  - "Lynn Ai"
  - "Eric Yang"
date: "2026-03-03"
arxiv_id: "2603.03378"
arxiv_url: "https://arxiv.org/abs/2603.03378"
pdf_url: "https://arxiv.org/pdf/2603.03378v2"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Multi-Agent System"
  - "Agent Training"
  - "Agentic Reinforcement Learning"
  - "Agent Self-Evolution"
  - "Tool Use"
  - "Reasoning"
  - "AIOps"
  - "Autonomous Operations"
relevance_score: 8.5
---

# AOI: Turning Failed Trajectories into Training Signals for Autonomous Cloud Diagnosis

## 原始摘要

Large language model (LLM) agents offer a promising data-driven approach to automating Site Reliability Engineering (SRE), yet their enterprise deployment is constrained by three challenges: restricted access to proprietary data, unsafe action execution under permission-governed environments, and the inability of closed systems to improve from failures. We present AOI (Autonomous Operations Intelligence), a trainable multi-agent framework formulating automated operations as a structured trajectory learning problem under security constraints. Our approach integrates three key components. First, a trainable diagnostic system applies Group Relative Policy Optimization (GRPO) to distill expert-level knowledge into locally deployed open-source models, enabling preference-based learning without exposing sensitive data. Second, a read-write separated execution architecture decomposes operational trajectories into observation, reasoning, and action phases, allowing safe learning while preventing unauthorized state mutation. Third, a Failure Trajectory Closed-Loop Evolver mines unsuccessful trajectories and converts them into corrective supervision signals, enabling continual data augmentation. Evaluated on the AIOpsLab benchmark, our contributions yield cumulative gains. (1) The AOI runtime alone achieves 66.3% best@5 success on all 86 tasks, outperforming the prior state-of-the-art (41.9%) by 24.4 points. (2) Adding Observer GRPO training, a locally deployed 14B model reaches 42.9% avg@1 on 63 held-out tasks with unseen fault types, surpassing Claude Sonnet 4.5. (3) The Evolver converts 37 failed trajectories into diagnostic guidance, improving end-to-end avg@5 by 4.8 points while reducing variance by 35%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在企业级站点可靠性工程（SRE）自动化部署中面临的核心挑战。研究背景是，随着云基础设施日益复杂，利用具备工具使用和链式推理能力的LLM智能体实现自动化运维（AIOps）成为趋势。然而，现有方法存在三大不足：首先，企业出于数据隐私和安全考虑，通常无法将敏感的专有运维数据提供给云端大型闭源模型，只能依赖本地部署的、能力较弱的小规模开源模型，导致诊断精度不足；其次，在受严格权限管控的生产环境中，标准的自动化方案往往将系统的“读”（诊断）和“写”（修复）权限混在一起，存在执行不安全动作的风险；最后，现有的闭源或静态部署的系统缺乏从自身失败经验中持续学习和改进的能力，无法适应不断演化的云环境。

因此，本文要解决的核心问题是：**如何在满足企业级安全约束（数据隐私与执行权限分离）的前提下，构建一个能够持续从失败中学习、并不断提升诊断能力的可训练自主运维智能体框架**。具体而言，论文提出了AOI框架，试图通过一个可训练的多智能体架构，将自动化运维任务构建为一个安全约束下的结构化轨迹学习问题，从而同时攻克权限安全、小模型能力提升以及利用失败经验进行持续自适应这三个关键难题。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：AIOps领域的LLM智能体、安全智能体系统以及从失败中学习的方法。

在**AIOps领域的LLM智能体**方面，已有研究将大语言模型应用于日志分析、异常检测、根因分析和交互式诊断。例如，STRATUS框架采用了多智能体协作，但其将推理与执行紧密耦合，导致了安全问题和脆弱的长期行为。其他并发工作探索了检索增强诊断和思维链提示用于根因分析。本文提出的AOI框架与这些工作的主要区别在于，它通过架构层面的角色分离（如观察者、探测者和执行者）来强制实现安全性，而非依赖基于提示的防护措施。

在**安全智能体系统**方面，现有安全机制包括动作过滤、沙箱执行环境以及基于人类反馈的强化学习。这些方法通常将安全视为附加约束。本文则不同，它将安全性内置于系统架构之中，通过职责分离（如观察者不能直接执行命令）来设计安全，这一思路受到了经典操作系统安全原则的启发。

在**从失败中学习**方面，失败分析在软件工程中至关重要。近期研究利用失败的测试用例来指导程序修复，而Reflexion则让LLM智能体能从失败尝试的文本反馈中学习。在强化学习中， hindsight experience replay 会用已实现的目标重新标记失败轨迹。本文方法的独特之处在于，它将失败的诊断命令序列作为输入，交由一个纠正模型来生成改进计划，并采用无需评论家的GRPO进行优化，这符合基于强化学习的LLM对齐趋势。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AOI（自主运维智能）的可训练多智能体框架来解决自动化云诊断中的挑战。其核心方法是将自动化运维构建为一个在安全约束下的结构化轨迹学习问题。整体框架包含三个关键组件：一个可训练的诊断系统、一个读写分离的执行架构，以及一个失败轨迹闭环进化器。

在架构设计上，AOI运行时系统遵循三个原则：安全分离、上下文效率和长时程连贯性。系统由四个专门的智能体组成一个结构化的多智能体架构：
1.  **观察者（Observer）**：作为中央协调器，维护诊断任务队列、分析压缩证据以更新假设，并根据当前诊断状态调度探测器或执行器。它不直接与环境交互，只进行推理。
2.  **探测器（Probe）**：处理所有只读操作（如kubectl get, describe），支持多轮探索并实现重试机制。
3.  **执行器（Executor）**：管理状态更改操作，在执行前可调用探测器进行验证，所有命令都经过白名单过滤并实现两阶段错误恢复。
4.  **压缩器（Compressor）**：通过基于规则的重复数据删除和基于LLM的语义压缩，将原始输出转化为决策可用的压缩上下文，确保上下文效率。

安全性的实现源于智能体与三个内存存储（原始存储、任务存储、压缩存储）之间的严格访问控制。关键不变性包括：观察者不能读取原始输出；探测器和执行器可写入原始存储但不能读取；压缩器是无状态的。每个诊断迭代遵循一个四阶段管道：决策、交互、压缩、缓存，确保“原始证据→压缩→决策输入”的流程。

对于长时程诊断，系统通过**双时间尺度记忆**来保持连贯性：长期记忆存储所有过去迭代的语义摘要，短期记忆包含前一次迭代的完整压缩上下文。观察者在每次迭代中接收这两者，从而在有限上下文内保持推理连贯性。

在训练方法上，论文应用了**组相对策略优化（GRPO）** 来优化两个不同组件：
*   **观察者GRPO**：优化步骤级决策。它从观察者策略中采样一组候选动作，由LLM评判员根据六个维度（格式、摘要、动作、上下文指令、上下文命名空间、置信度）进行评分，计算组归一化优势度，并通过策略梯度更新来最大化期望优势度。这种方法支持基于偏好的学习，无需暴露敏感数据。
*   **进化器GRPO**：优化轨迹级生成。它解决了数据稀缺悖论，通过两种机制：将成功轨迹增强为多样化的诊断工作流变体，以及将失败轨迹修复为校正后的计划。对于失败轨迹，进化器学习生成改进的命令序列，提供对比性监督。它同样使用GRPO框架，对每个失败轨迹采样一组候选校正，通过奖励模型评估其有效性、完整性、正确性和效率，并计算组归一化优势度进行优化。校正后的计划以结构化提示的形式提供给观察者，作为诊断指导。

创新点在于：1) 通过读写分离的架构和严格的访问控制，在权限管控环境下实现安全的学习与执行；2) 利用GRPO在本地开源模型上提炼专家级知识，避免了敏感数据暴露；3) 独创性地通过轨迹进化器将失败轨迹转化为校正性监督信号，实现了持续的数据增强和系统自我改进，形成了一个从失败中学习的闭环。

### Q4: 论文做了哪些实验？

论文在 AIOpsLab 基准测试上进行了全面的实验评估，该基准包含在真实 Kubernetes 集群上运行的三个微服务应用的 86 个故障场景任务，涵盖检测（32）、定位（28）、根因分析（13）和缓解（13）四类。实验设置采用嵌套数据划分：使用全部 86 个任务（$\mathcal{D}^{all}$）进行运行时架构对比；从其中划分出由 Claude Sonnet 4.5 成功解决的 49 个任务作为 Evolver 的训练种子（$\mathcal{D}^{train}_{evolver}$）；再从中严格划出覆盖 11 种故障类型的 23 个任务用于 Observer 的 GRPO 训练（$\mathcal{D}^{train}_{obs}$）；并设置包含 15 种未见故障类型的 63 个任务作为 Observer 的测试集（$\mathcal{D}^{test}_{obs}$），其中包含 Sonnet 失败的 37 个轨迹用于评估 Evolver 的修复能力（$\mathcal{D}^{test}_{evolver}$）。基础模型为 Qwen3-14B，使用 LoRA 微调（rank=64，$\alpha$=128，学习率 $10^{-5}$），GRPO 组大小 $G$=4。

对比方法包括：基准参考的 ReAct 风格智能体 AOL-agent、具有专用模块的多智能体系统 STRATUS、以及使用 Claude Sonnet 4.5 的 AOL-agent（其轨迹作为训练种子）。主要结果如下：
1.  **运行时架构性能**：在全部 86 个任务上，AOI（Qwen3-14B）的 best@5 成功率达到 66.3%，显著超过 STRATUS（41.9%）24.4 个百分点，并优于 Claude Sonnet 4.5 + AOL-agent（57.0%）。分任务类别看，检测达到 100% best@5，根因分析相对 STRATUS 提升 150%（30.8% vs. 7.7%），缓解提升 3 倍（46.2% vs. 15.4%）。
2.  **Observer GRPO 训练效果**：在包含未见故障类型的 63 个测试任务上，经过 GRPO 训练的 Observer（avg@1 成功率为 42.9%）超越了 Claude Sonnet 4.5（41.3%），其中检测任务提升显著（90.9% vs. 54.5%）。
3.  **Evolver 组件消融与修复能力**：在 37 个 Sonnet 失败的任务上，结合 Observer-GRPO 与 Evolver 生成提示的方法取得了最高的平均成功率（33.8%，较未训练的 Base 提升 8.9 个百分点）。Evolver 通过将失败轨迹转化为诊断指导，使端到端的 avg@5 提升了 4.8 个百分点，同时将方差降低了 35%。分析表明，Evolver 提示提高了鲁棒性（best@5 与 avg@5 的差距从 29.2 个百分点缩小至 18.9 个百分点），尤其是在检测任务上，方差减半。

### Q5: 有什么可以进一步探索的点？

该论文提出的AOI框架在自动化云诊断方面取得了显著进展，但其局限性和未来研究方向也较为明确。首先，系统存在**任务特定的能力边界**，约三分之一的任务（如需要Helm专业知识或复杂因果推理的任务）在所有配置下均失败，这表明当前架构在特定领域知识整合和深度推理方面存在不足。未来可探索**模块化知识注入**或**与领域专家系统结合**，以突破这些系统性瓶颈。

其次，**速度与精度的权衡**问题突出：GRPO优化虽提升了异常检测速度，却牺牲了故障定位的精确性，尤其在需要多跳推理的任务中。这启示未来研究需设计**更精细化的奖励函数**，或许可引入分层奖励机制，分别激励检测、定位和修复阶段，或探索**课程学习**策略，逐步提升模型复杂度。

再者，**失败轨迹的利用效率**仍有提升空间。当前方法主要纠正“近似正确”的轨迹，但对于完全错误的轨迹挖掘不足。未来可研究**更强大的对比学习或因果发现技术**，从更广泛的失败模式中提取信号，甚至**合成对抗性失败案例**以增强鲁棒性。

最后，**安全约束与能力提升的协同机制**值得深入探索。论文发现读写分离等安全机制反而提升了诊断能力，这挑战了传统假设。未来可系统性地研究**不同安全护栏（如权限模型、回滚机制）对探索效率和最终性能的影响**，形成可理论化的安全-能力协同设计原则。此外，**采样多样性的收益递减**现象表明，简单的多次运行策略效益有限，未来或需开发**更智能的主动学习或贝叶斯优化策略**，以动态分配计算资源，实现成本效益最大化。

### Q6: 总结一下论文的主要内容

该论文提出了AOI框架，旨在解决大语言模型代理在自动化站点可靠性工程中面临的三大挑战：专有数据访问受限、权限环境下执行不安全以及封闭系统无法从失败中学习。核心贡献在于将自动化运维构建为一个安全约束下的结构化轨迹学习问题。方法上，AOI集成了三个关键组件：首先，采用分组相对策略优化，将专家知识提炼到本地开源模型中，实现基于偏好的学习且不暴露敏感数据；其次，通过读写分离的执行架构，将操作轨迹分解为观察、推理和行动阶段，确保安全学习并防止未授权状态变更；最后，设计失败轨迹闭环演化器，挖掘失败轨迹并将其转化为纠正性监督信号，实现持续数据增强。主要结论显示，在AIOpsLab基准测试中，AOI运行时在86项任务上达到66.3%的最佳前五成功率，显著优于之前的最佳方法；经过训练的本地140亿参数模型在63项未见故障任务上平均首位成功率超越Claude Sonnet 4.5；演化器成功将37条失败轨迹转化为诊断指导，提升了端到端性能并降低了方差。该研究为安全、可进化的企业级自动化运维提供了可行的数据驱动方案。
