---
title: "PowerLens: Taming LLM Agents for Safe and Personalized Mobile Power Management"
authors:
  - "Xingyu Feng"
  - "Chang Sun"
  - "Yuzhu Wang"
  - "Zhangbing Zhou"
  - "Chengwen Luo"
  - "Zhuangzhuang Chen"
  - "Xiaomin Ouyang"
  - "Huanqi Yang"
date: "2026-03-20"
arxiv_id: "2603.19584"
arxiv_url: "https://arxiv.org/abs/2603.19584"
pdf_url: "https://arxiv.org/pdf/2603.19584v1"
categories:
  - "cs.AI"
  - "eess.SY"
tags:
  - "Mobile Agent"
  - "Multi-Agent Architecture"
  - "Tool Use & Reasoning"
  - "Personalization"
  - "Safety & Constraint"
  - "System Implementation"
  - "Energy Management"
relevance_score: 7.5
---

# PowerLens: Taming LLM Agents for Safe and Personalized Mobile Power Management

## 原始摘要

Battery life remains a critical challenge for mobile devices, yet existing power management mechanisms rely on static rules or coarse-grained heuristics that ignore user activities and personal preferences. We present PowerLens, a system that tames the reasoning power of Large Language Models (LLMs) for safe and personalized mobile power management on Android devices. The key idea is that LLMs' commonsense reasoning can bridge the semantic gap between user activities and system parameters, enabling zero-shot, context-aware policy generation that adapts to individual preferences through implicit feedback. PowerLens employs a multi-agent architecture that recognizes user context from UI semantics and generates holistic power policies across 18 device parameters. A PDL-based constraint framework verifies every action before execution, while a two-tier memory system learns individualized preferences from implicit user overrides through confidence-based distillation, requiring no explicit configuration and converging within 3--5 days. Extensive experiments on a rooted Android device show that PowerLens achieves 81.7% action accuracy and 38.8% energy saving over stock Android, outperforming rule-based and LLM-based baselines, with high user satisfaction, fast preference convergence, and strong safety guarantees, with the system itself consuming only 0.5% of daily battery capacity.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决移动设备电池管理中存在的静态、粗粒度且缺乏个性化的问题。研究背景是，尽管智能手机已成为核心计算平台，但其电池续航仍是持久痛点。现有方法主要包括硬件级动态调频、操作系统级启发式策略（如Android自适应电池）以及基于学习的方案。这些方法存在明显不足：硬件级方案仅响应瞬时负载，忽视整体用户活动语义；OS级机制依赖应用使用频率等粗粒度指标，无法理解特定应用功能需求（如导航需要高精度GPS）或用户个人偏好；而学习型方法通常需要大量训练数据、泛化能力差，且基于低层数值信号，缺乏对用户活动的语义理解。

本文的核心问题是：如何实现安全、个性化且能感知上下文的移动设备电源管理。具体而言，需要解决三个关键挑战：1) **上下文感知的策略生成**：需要联合推理用户活动、应用需求和设备能力，以生成适应不同场景（如导航与音乐播放对资源需求截然不同）的节能策略，避免“一刀切”规则造成的能源浪费（可达19-50%）或体验下降。2) **从隐式反馈中学习个性化偏好**：用户很少明确设置电源偏好，其偏好主要通过手动覆盖系统设置（如调亮被系统调暗的屏幕）来隐式表达，且这种模式因人而异。3) **安全且可验证的执行**：直接使用大语言模型（LLM）生成策略可能导致超过20%的问题操作（如禁用导航时的GPS），存在安全风险。

为此，论文提出了PowerLens系统，其核心思路是利用LLM的常识推理能力，弥合用户活动语义与系统参数之间的鸿沟，实现零样本、上下文感知的策略生成，并通过隐式反馈自适应个人偏好。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为移动电源管理机制和基于LLM的移动任务自动化两大类。

在**移动电源管理机制**方面，相关工作包括：1）底层动态电压频率调节（DVFS）机制，如schedutil和GearDVFS，它们根据负载动态调整CPU频率，但无法区分不同用户活动的语义；2）操作系统级机制，如Android的Adaptive Battery（通过应用待机分组限制后台活动）和Doze模式（在空闲时严格限制后台活动）。这些机制均缺乏对用户活动语义的理解，无法根据具体场景（如区分视频通话与后台索引）进行细粒度优化。

在**基于LLM的移动任务自动化**方面，相关工作包括：AutoDroid（无需训练即可规划多步操作）、MobileGPT（利用任务记忆处理重复任务）和AutoIOT（桥接自然语言意图与底层设备操作）。这些研究证明了LLM具备语义理解、常识推理和组合规划能力，为电源管理提供了基础。然而，系统级资源管理面临独特挑战：操作是连续的而非离散的UI点击、后果具有延迟性、安全约束严格（如错误的GPS设置可能导致导航失败）。

**本文与这些工作的关系和区别**在于：PowerLens首次将LLM的推理能力系统性地应用于移动电源管理这一安全关键领域。它超越了现有静态规则或粗粒度启发式方法，通过多智能体架构实现零样本、上下文感知的策略生成。与现有LLM自动化工作不同，PowerLens引入了基于PDL的约束框架确保执行前验证，并通过双层记忆系统从隐式反馈中学习个性化偏好，从而在保证安全性的同时实现个性化节能。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为PowerLens的系统来解决移动设备电源管理缺乏个性化和安全性的问题。其核心方法是利用大型语言模型（LLM）的常识推理能力，构建一个多智能体闭环控制系统，实现零样本、上下文感知且安全的个性化策略生成。

**整体框架与主要模块**：
系统分为紧密耦合的两个子系统：Android系统层和电源管理循环。Android系统层提供设备分析器（枚举可调参数及其有效范围）和辅助功能框架（将前台应用GUI转换为结构化UI XML）。电源管理循环则协调四个智能体，形成一个闭环控制：
1.  **活动智能体**：负责上下文识别。它接收UI树、设备上下文和近期应用历史，利用LLM识别用户的高层活动类型（如导航、视频观看）和细粒度子活动，并构建一个紧凑的上下文签名用于高效记忆检索。
2.  **策略智能体**：负责生成个性化电源策略。它接收设备上下文、活动识别结果、记忆偏好和安全约束，通过仲裁三个记忆源（短期记忆中的用户锁定、长期记忆中基于上下文的规则、长期记忆中的通用用户档案）来生成结构化的策略动作集合。安全约束在生成阶段即被要求遵守。
3.  **执行智能体**：作为LLM策略与物理设备间的桥梁。它通过两次独立的LLM调用，依次进行**合法性验证**（检查动作是否符合设备能力范围和PDL安全约束）和**Shell命令生成**（将批准的动作翻译成可执行的Android根命令），最后同步设备状态。
4.  **反馈智能体**：通过确定性的状态差分机制检测用户干预（如手动调整亮度），而无需调用LLM。它将检测到的手动覆盖记录为强反馈信号，并写入短期记忆作为活动约束，同时记录原始事件供后续分析。

**关键技术**：
*   **双层记忆系统**：包含**短期记忆**（STM，会话范围，存储活动约束和原始事件日志）和**长期个人记忆**（LPM，持久化，存储提炼的规则和偏好），由异步的**提取器**连接。提取器在设备空闲时运行，使用LLM分析用户意图，并通过基于置信度的衰减-奖励机制对候选规则进行评分和提炼，最终将高置信度规则推广并存入LPM。
*   **基于PDL的安全约束框架**：在策略生成和执行验证两个阶段独立检查动作，确保不违反安全不变式，提供双重防御。
*   **零样本个性化策略生成**：LLM利用其常识直接根据当前上下文生成策略，无需针对每个用户或场景进行预训练。个性化通过从用户隐式反馈（手动覆盖）中学习实现，无需显式配置。
*   **模块化多智能体架构**：将复杂任务分解为专门化的智能体，支持独立测试和更新、通过回退策略实现优雅降级，并提高了系统的可解释性。

**创新点**：
1.  **利用LLM推理桥接语义鸿沟**：首次利用LLM的常识理解能力，将用户活动语义与底层系统参数直接关联，实现上下文感知的电源管理。
2.  **基于隐式反馈和置信度提炼的个性化学习**：通过双层记忆系统和异步提取器，从用户手动覆盖中无感学习个性化偏好，并在3-5天内收敛。
3.  **安全优先的验证架构**：通过PDL约束框架和执行前的独立LLM验证，确保所有动作安全，解决了LLM直接控制设备的核心安全隐患。
4.  **高效的分层记忆检索与仲裁机制**：通过紧凑的上下文签名和渐进松弛的检索策略，实现高效且灵活的规则匹配，并采用严格的优先级仲裁（用户锁定 > 上下文规则 > 通用档案）来协调不同记忆源。

### Q4: 论文做了哪些实验？

论文的实验设置包括在已获取root权限的OnePlus ACE 5手机（搭载骁龙8 Gen 3处理器，运行Android 15系统）上部署PowerLens应用，该系统服务使用Gemini-2.5-Flash作为大语言模型（LLM）骨干，每个决策周期的总管道延迟为12.2秒。功耗测量通过Android Battery Historian工具进行应用级能耗归因。

实验对比了四个基线方法：（1）原生Android系统（无干预，节能基准为0%）、（2）Android内置的省电模式（采用一刀切的限制策略）、（3）基于规则的静态策略（按应用类别设定规则，无LLM推理）、（4）单智能体LLM方法（使用相同的Gemini-2.5-Flash模型）。

主要实验结果如下：PowerLens在动作准确性上达到81.7%，相较于原生Android系统实现了38.8%的节能效果，超越了所有基线方法。系统本身仅消耗每日电池容量的0.5%。通过基于置信度蒸馏的两层记忆系统，PowerLens能够在无需显式配置的情况下，仅用3-5天即完成个性化偏好的收敛，并获得了较高的用户满意度与强大的安全保证。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其验证环境为已获取 root 权限的 Android 设备，这限制了其在普通用户设备上的直接部署与普适性。此外，系统依赖 UI 语义进行上下文识别，可能无法全面捕捉后台进程或传感器层面的复杂功耗场景。

未来研究方向可从以下几方面深入：一是探索在非 root 环境下的轻量化部署方案，例如通过与操作系统厂商合作集成权限接口。二是增强多模态感知能力，结合传感器数据（如 GPS、加速度计）更精准地推断用户状态。三是研究跨设备的个性化迁移学习，使用户偏好能在手机、平板等设备间同步。四是考虑动态环境下的长期适应性，当前系统在 3-5 天内收敛，但用户习惯可能随时间变化，需引入持续学习机制防止策略僵化。

可能的改进思路包括设计分层安全验证框架，在 LLM 生成策略后加入基于强化学习的模拟环境测试，进一步降低风险；同时可探索联邦学习架构，在保护隐私的前提下聚合匿名数据以提升模型泛化能力。

### Q6: 总结一下论文的主要内容

PowerLens 提出了一种基于大型语言模型（LLM）的智能体系统，旨在解决移动设备电池管理中静态规则或启发式方法忽略用户活动和个性化偏好的问题。其核心贡献是利用LLM的常识推理能力，弥合用户活动与系统参数之间的语义鸿沟，实现零样本、上下文感知的个性化电源管理。

该系统采用多智能体架构：一个智能体从UI语义中识别用户上下文，另一个则据此生成覆盖18个设备参数的全局电源策略。为确保安全，系统设计了基于PDL的约束框架，在执行前验证所有动作；并通过双层记忆系统，从用户隐式覆盖操作中学习个性化偏好，利用基于置信度的知识蒸馏实现无需显式配置、3-5天内快速收敛的学习机制。

实验表明，PowerLens在已获取Root权限的Android设备上实现了81.7%的动作准确率和38.8%的节能效果（相较于原生系统），优于基于规则和LLM的基线方法。系统在保证高用户满意度、快速偏好收敛和强安全性的同时，自身仅消耗每日电池容量的0.5%，为安全、个性化的移动电源管理提供了新颖有效的解决方案。
