---
title: "FOCAL: Filtered On-device Continuous Activity Logging for Efficient Personal Desktop Summarization"
authors:
  - "Haoran Yin"
  - "Zhiyuan Wen"
  - "Jiannong Cao"
  - "Bo Yuan"
  - "Ruosong Yang"
date: "2026-04-21"
arxiv_id: "2604.19541"
arxiv_url: "https://arxiv.org/abs/2604.19541"
pdf_url: "https://arxiv.org/pdf/2604.19541v1"
categories:
  - "cs.MA"
  - "cs.HC"
tags:
  - "Multi-Agent System"
  - "On-Device AI"
  - "Efficiency Optimization"
  - "Personal AI Assistant"
  - "Desktop Interaction"
  - "Vision-Language Model"
  - "Privacy-Preserving"
  - "Task Attribution"
  - "Context Management"
relevance_score: 7.5
---

# FOCAL: Filtered On-device Continuous Activity Logging for Efficient Personal Desktop Summarization

## 原始摘要

Desktop interaction streams provide a continuous, privacy-sensitive record of interleaved user tasks. Transforming these streams into task-organized personal logs on-device faces two main challenges: exhaustive Vision-Language Model (VLM) processing strains local resources, and global stream processing causes cross-task context pollution. We present FOCAL (Filtered On-device Continuous Activity Logging), a privacy-first multi-agent system utilizing a unified filter-plan-log architecture. It cascades a lightweight Filter Agent for noise suppression, a text-only Brain Agent for task attribution, a Record Agent for selective visual reasoning, and a task-isolated Memory Agent for context-coherent summarization. Experiments on DesktopBench (comprising 2,572 screenshots across 420 complex sessions) show FOCAL reduces total token consumption by 60.4% and VLM call count by 72.3% versus a baseline, while boosting Key Information Recall (KIR) from 0.38 to 0.61. Crucially, under $A{\to}B{\to}A$ task interruptions, FOCAL maintains Task Acc 0.81 and KIR 0.80, whereas the baseline collapses to Task Acc 0.03. FOCAL pioneers the efficient, on-device summarization of instruction-free desktop streams into multi-perspective personal logs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在个人桌面环境下，如何高效、隐私安全地将连续、多模态的桌面交互流实时自动归纳总结为按任务组织的个人日志这一核心问题。

研究背景是，桌面交互流（如屏幕截图、GUI操作）连续记录了用户交织进行的多项任务（如写文档、查资料、调试代码），将其转化为结构化的日志有助于生产力评估和知识检索。然而，这类数据包含大量敏感信息（邮件、聊天、文档等），因此必须在设备本地进行处理以保护隐私。现有基于大语言模型（LLM）和视觉语言模型（VLM）的方法虽在移动或可穿戴场景有所进展，但尚未有效应用于桌面场景。现有方法主要存在两大不足：一是**资源消耗问题**，即对桌面流进行详尽的VLM处理会给本地计算资源（GPU、CPU、内存）带来巨大负担，导致延迟和资源争用；二是**上下文污染问题**，即现有方法通常将整个交互流视为全局上下文进行处理，当用户在多个并发任务间频繁切换时，会导致不同任务的语义信息在共享内存中相互混杂，造成总结混乱。

因此，本文要解决的核心问题是：在**没有预先指令或任务标注**的连续桌面交互流中，如何设计一种**设备本地的、隐私优先的机制**，既能**高效筛选**出值得进行视觉推理的关键时刻以降低计算开销，又能**准确地将观察到的信息归因并路由到正确的任务特定上下文中**，从而在资源受限的设备上，实现非侵入式、且能抵抗任务切换干扰的高质量多视角任务总结。FOCAL系统即是为了填补这一“指令无关的推理前选择与路由机制”的空白而提出的。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 个人体验记录与生活日志**：早期系统如MyLifeBits和SenseCam专注于连续记录与检索，而近期研究（如AutoLife）转向利用大语言模型（LLM）将被动记录（如智能手机轨迹）转化为结构化叙事日志。这些工作推动了从原始数据捕获到语言介导的结构化个人记忆的转变。然而，它们主要依赖物理世界信号，缺乏针对桌面活动所需的**应用层语义理解**，难以处理跨多个窗口、应用和目标的复杂交错任务流。

**2. 图形用户界面（GUI）理解与任务导向智能体**：近期GUI系统探索多模态模型对界面的语义理解。例如，GUI-Narrator生成GUI操作的自然语言描述；AutoDroid、AppAgent v2、UI-Hawk等任务导向智能体通过结构化历史、检索或时序建模来改进基于指令的执行。此外，如MovieChat和MA-LMM等长上下文多模态系统强调了时序记忆的重要性。但这些系统主要设计用于**执行或基于查询的推理**，通常假设明确的用户目标、有限轨迹或以执行为中心的全局记忆，**不适用于无指令、回顾性的连续日志记录场景**。

**3. 隐私敏感的多模态学习**：视觉生活日志 inherently 涉及隐私风险，近期研究也强调将个人视觉数据发送至云端服务的风险。这对于可能暴露私人文档、聊天和凭证的桌面截图记录尤为突出。

**本文与这些工作的关系和区别**：
FOCAL系统针对上述研究空白，专注于**桌面环境下的无指令、连续活动记录**。它与生活日志研究的区别在于，专门处理具有丰富应用层语义的桌面交互流；与GUI智能体研究的区别在于，其核心目标是**隐私优先的本地回顾性摘要生成**，而非任务执行。为此，FOCAL创新性地提出了统一的过滤-规划-记录架构，通过轻量级过滤、纯文本任务归因、选择性视觉推理和**任务隔离的记忆机制**，解决了现有系统在资源消耗、跨任务上下文污染及频繁任务切换下性能崩溃的问题，从而实现了高效、稳健的本地桌面摘要。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为FOCAL的多智能体系统来解决高效、隐私优先的桌面活动流摘要问题，其核心是“过滤-规划-记录”的统一架构。该系统将任务感知的控制逻辑前置到昂贵的视觉推理之前，从而在资源受限的本地设备上，有效应对了全量视觉语言模型处理带来的计算负担以及全局流处理导致的跨任务上下文污染问题。

整体框架由五个职责严格分离的智能体组成，按处理流程串联运作：
1.  **过滤智能体**：作为前端模块，负责从原始桌面环境状态中获取并验证动作，丢弃无效或噪声数据，为下游处理提供干净的动作序列。
2.  **大脑智能体**：这是系统的核心规划器。它仅基于动作的元数据序列进行一次性的、纯文本的规划。其输出是一个会话计划，为每个动作解析出三项关键决策：分配的任务ID、该动作是继续现有任务还是初始化新任务、以及是否需要对该动作进行视觉采样。这一设计创新性地将任务路由和采样决策与视觉计算解耦，在调用VLM之前就完成了关键控制。
3.  **记录智能体**：仅当大脑智能体判定需要视觉采样时，该智能体才被激活。它接收对应的屏幕截图、元数据以及当前任务相关的局部记忆，调用VLM生成基于记忆的语义描述。其创新在于，视觉推理是条件触发的、高度选择性的。
4.  **记忆智能体**：作为唯一拥有持久化跨步骤任务状态读写权限的管理器。它根据大脑智能体的路由决策，将记录智能体生成的描述追加到对应的、任务隔离的记忆存储中。这确保了每个任务的上下文证据被严格分离，避免了交叉污染。
5.  **摘要智能体**：在会话结束时运行，读取所有已完成的、相互隔离的任务记忆存储，为每个任务生成摘要，并最终拼接成任务组织的会话级摘要。

关键技术与创新点包括：
*   **元数据优先的规划**：大脑智能体仅使用应用名和窗口标题等轻量级文本元数据进行全局规划，极大减少了计算开销。
*   **条件视觉采样**：通过规划决定是否调用昂贵的VLM，实现了对视觉计算的动态过滤，这是降低资源消耗的关键。
*   **任务隔离的记忆**：为每个任务维护独立的证据链，确保在用户频繁切换任务时，每个任务的摘要上下文保持纯净和连贯。
*   **严格的模块化与状态隔离**：每个智能体具有受限的观察、输出和状态访问权限，通过明确的接口交互，形成了高效、可控的流水线。这种设计将控制逻辑、感知推理和状态管理分离，是系统在保证摘要质量的同时显著降低成本（减少60.4%的总token消耗和72.3%的VLM调用）并在任务中断场景下保持稳健性能的核心原因。

### Q4: 论文做了哪些实验？

实验在MacBook（Apple M4芯片，16GB统一内存）的本地资源受限环境下进行，使用qwen3:8b作为核心语言模型。数据集为DesktopBench，包含420个复杂会话的2,572张屏幕截图，分为多任务（Multi-task）和任务中断（Interruption，A→B→A模式）两个子集。

对比方法包括两个消融基线：1) **Naive LLM Agent**：对会话中每个动作调用VLM生成无上下文视觉描述，然后由LLM生成单一会话级摘要，无自适应采样和任务隔离记忆；2) **FOCAL-GM**：保留FOCAL的Brain Agent和自适应采样，但将任务隔离记忆替换为全局共享记忆池。

评估维度包括计算效率和摘要质量。效率指标：**VLM调用次数（VCC）**和**每会话令牌消耗（TCS）**。质量指标：**关键信息召回率（KIR，λ=2）**、**任务数量准确率（Task Acc）**、**BERTScore F1（BS-F1）**和基于GPT-5的**G-Eval**（从准确性、覆盖度、简洁性、一致性和清晰度五个维度评分，1-5分）。

主要结果：在多任务数据集上，FOCAL相比Naive基线将VCC降低72.3%（17.3→4.8次/会话），TCS降低60.4%（45,240→17,913令牌/会话），VLM令牌消耗减少69.8%；相比FOCAL-GM，TCS进一步降低15.7%。在摘要质量上，FOCAL的KIR达到0.61，G-Eval达到4.16，分别比Naive基线提升0.23和1.20，比FOCAL-GM提升0.19和0.75。在中断数据集上，FOCAL保持稳健性能（Task Acc 0.81，KIR 0.80，G-Eval 4.12），而Naive基线的Task Acc崩溃至0.03。消融实验表明，Brain Agent主导效率提升（移除后TCS增加58.7%），而任务隔离记忆是关键质量提升来源（从全局记忆改为任务隔离记忆时，KIR提升0.19，G-Eval提升0.75）。案例研究显示FOCAL能正确恢复连贯的任务跨度，而Naive基线会产生过度分割。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在评估范围较窄，仅基于特定硬件（Apple M4）和单一本地模型（qwen3:8b）进行验证，其普适性和在不同资源约束设备上的效能尚不明确。未来研究可首先扩展评估体系，在更多硬件平台（如移动端、边缘设备）和不同规模的本地模型上进行测试，尤其关注参数量更小但指令遵循能力强的模型，以验证架构的广泛适用性。

结合论文方向，进一步的探索点包括：第一，**系统功能的演进**，从被动的日志记录转向主动的轻量级辅助，如实现任务中断后智能恢复、自动化进度追踪，或在保护隐私的前提下构建个人记忆检索系统。第二，**深入量化实际部署成本**，需要对更长连续会话进行监测，并系统性地测量延迟、能耗等关键指标，这对移动设备的电池续航至关重要。第三，**架构与算法的优化**，可探索更高效的过滤与规划机制，例如利用增量学习动态更新任务模型，或研究跨任务的有限、可控知识共享机制，以在避免“上下文污染”的同时提升连贯性。这些方向将推动个人计算系统向更高效、智能且实用的方向发展。

### Q6: 总结一下论文的主要内容

这篇论文提出了FOCAL系统，旨在解决在个人设备上对连续的桌面交互流进行高效、隐私保护的自动化任务日志总结所面临的两大挑战：资源受限设备上全量视觉语言模型处理带来的计算负担，以及全局流处理导致的不同任务间上下文污染。其核心贡献是设计了一个隐私优先的多智能体系统，采用统一的“过滤-规划-记录”架构。该方法首先通过轻量级过滤代理抑制噪声，然后利用纯文本的大脑代理进行任务归因，接着由记录代理执行选择性视觉推理，最后通过任务隔离的记忆代理生成上下文连贯的总结。实验基于包含420个复杂会话的DesktopBench数据集进行，结果表明，相比基线方法，FOCAL将总令牌消耗降低了60.4%，VLM调用次数减少了72.3%，并将关键信息召回率从0.38提升至0.61。特别是在A→B→A任务中断场景下，FOCAL能保持0.81的任务准确率和0.80的关键信息召回率，而基线方法则崩溃至0.03的任务准确率。该工作率先实现了无需指令、在设备端高效地将桌面流总结为多视角个人日志。
