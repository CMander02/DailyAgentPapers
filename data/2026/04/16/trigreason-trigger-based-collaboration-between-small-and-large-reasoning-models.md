---
title: "TrigReason: Trigger-Based Collaboration between Small and Large Reasoning Models"
authors:
  - "Yi Zhao"
  - "Yajuan Peng"
  - "Cam-Tu Nguyen"
  - "Zuchao Li"
  - "Xiaoliang Wang"
  - "Xiaoming Fu"
  - "Hai Zhao"
date: "2026-04-16"
arxiv_id: "2604.14847"
arxiv_url: "https://arxiv.org/abs/2604.14847"
pdf_url: "https://arxiv.org/pdf/2604.14847v1"
github_url: "https://github.com/QQQ-yi/TrigReason"
categories:
  - "cs.AI"
tags:
  - "推理加速"
  - "模型协作"
  - "计算效率"
  - "推理风险"
  - "选择性干预"
  - "边缘计算"
relevance_score: 8.0
---

# TrigReason: Trigger-Based Collaboration between Small and Large Reasoning Models

## 原始摘要

Large Reasoning Models (LRMs) achieve strong performance on complex tasks through extended chains of thought but suffer from high inference latency due to autoregressive reasoning. Recent work explores using Small Reasoning Models (SRMs) to accelerate LRM inference. In this paper, we systematically characterize the capability boundaries of SRMs and identify three common types of reasoning risks: (1) path divergence, where SRMs lack the strategic ability to construct an initial plan, causing reasoning to deviate from the most probable path; (2) cognitive overload, where SRMs fail to solve particularly difficult steps; and (3) recovery inability, where SRMs lack robust self-reflection and error correction mechanisms. To address these challenges, we propose TrigReason, a trigger-based collaborative reasoning framework that replaces continuous polling with selective intervention. TrigReason delegates most reasoning to the SRM and activates LRM intervention only when necessary-during initial strategic planning (strategic priming trigger), upon detecting extraordinary overconfidence (cognitive offload trigger), or when reasoning falls into unproductive loops (intervention request trigger). The evaluation results on AIME24, AIME25, and GPQA-D indicate that TrigReason matches the accuracy of full LRMs and SpecReason, while offloading 1.70x - 4.79x more reasoning steps to SRMs. Under edge-cloud conditions, TrigReason reduces latency by 43.9\% and API cost by 73.3\%. Our code is available at \href{https://github.com/QQQ-yi/TrigReason}{https://github.com/QQQ-yi/TrigReason}

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型推理模型在复杂任务中因自回归生成长思维链而导致的高推理延迟问题。研究背景是，尽管大型推理模型通过扩展的思维链在数学推理、代码生成等领域取得了卓越性能，但其生成大量中间推理步骤会带来显著的响应延迟。现有方法主要聚焦于通过强化学习、监督微调或提示工程来精简思维链，但这些方法可能因限制推理令牌预算而跳过关键步骤或妨碍自我修正。另一种思路是利用小型推理模型来加速推理，例如SpecReason采用推测式验证机制，但其存在两个主要不足：一是大型模型对单个步骤的评判不可靠且具有主观性；二是其基于轮询的设计需要在每一步都调用大型模型进行验证，导致在边缘-云协作场景下产生显著开销，效率低下。

本文的核心问题是：如何更高效、更智能地实现小型与大型推理模型之间的协作，以在保持高准确性的同时，大幅降低推理延迟和成本。具体而言，论文首先系统分析了小型模型的能力边界，识别出其三种常见的推理风险：路径发散（缺乏构建初始计划的策略能力）、认知超载（无法解决特别困难的步骤）以及恢复无能（缺乏自我反思和纠错机制）。针对这些挑战，本文提出了TrigReason框架，其核心创新在于将大型模型的干预从连续的轮询验证转变为基于特定触发器的选择性介入。该框架让小型模型自主进行大部分推理，仅当三种特定情况发生时（初始战略规划、检测到异常高置信度、或推理陷入无效循环）才触发大型模型干预，从而在保证准确率的前提下，将更多推理步骤卸载给小型模型，显著提升效率。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕大模型推理加速和大小模型协作范式展开，可分为方法类和应用/评测类。

在**方法类**研究中，以**推测推理（Speculative Reasoning）** 为代表的工作探索了利用小推理模型（SRM）来加速大推理模型（LRM）的推理。本文重点讨论了其中的**SpecReason**方法，它采用“LRM-as-a-Judge”框架，即LRM对SRM生成的每一步进行评分，决定是否接受。本文指出该方法存在两大关键局限：一是LRM判断不可靠，因其自身偏见和评估中间步骤的困难，导致对正确步骤的误拒率高；二是基于轮询（polling-based）的执行效率低下，每一步都需LRM介入，带来了巨大的通信和计算开销，尤其在边缘-云协作场景下，反而可能增加延迟和成本。

在**应用/评测类**研究中，相关工作主要关注如何评估和利用大小模型在不同复杂任务上的能力边界。本文的工作正是在系统性地刻画SRM能力边界（识别出路径发散、认知过载、恢复无能三类风险）的基础上展开的。

**本文与这些工作的关系和区别在于**：本文提出的TrigReason框架，是对现有推测推理方法（特别是SpecReason）的改进。它摒弃了连续轮询和LRM作为每一步“法官”的范式，转而采用**基于触发的选择性干预**机制。仅在初始战略规划、检测到异常高置信度或陷入无意义循环等关键时刻才激活LRM，从而在保持LRM级别精度的同时，将更多推理步骤卸载给SRM，显著提升了效率并降低了成本。

### Q3: 论文如何解决这个问题？

论文通过提出TrigReason这一基于触发器的协作推理框架来解决小推理模型（SRM）在加速大推理模型（LRM）推理时存在的三种核心风险：路径发散、认知过载和恢复无能。其核心方法是摒弃传统的持续轮询验证，转而采用选择性干预策略，即让SRM承担大部分推理步骤，仅在有明确风险信号时触发LRM介入。

整体框架是一个SRM与LRM的协作执行流程。主要包含三个关键触发模块，分别针对三种风险设计：
1.  **战略启动触发器**：用于应对路径发散风险。在推理开始时，先由LRM生成前n个推理步骤（战略规划或问题分解），为SRM提供一个已验证的、连贯的推理起点，之后控制权移交SRM继续执行后续步骤。这确保了推理路径初始方向的正确性。
2.  **认知卸载触发器**：用于应对认知过载风险。该模块通过监测SRM生成推理步骤时的“异常过度自信”信号来触发LRM干预。具体地，它计算每个推理步骤中词元级困惑度低于阈值τ的比例（低困惑度比例r_s）。当r_s超过覆盖阈值ρ时，表明SRM可能因认知过载而陷入机械的模式补全，此时触发器激活，由LRM重新生成当前步骤。
3.  **干预请求触发器**：用于应对恢复无能风险。该模块通过检测SRM推理链中出现的语言犹豫标记（如“wait”、“hmm”等）来识别推理停滞或陷入无效循环的迹象。当连续k个步骤都检测到犹豫标记时，触发器激活，控制权转移给LRM，由LRM执行后续m个步骤以评估当前状态、识别不一致并重新校正推理路径，之后再将控制权交还SRM。

创新点在于：首先，系统性地识别并刻画了SRM相对于LRM的三种能力边界风险，为针对性干预提供了理论基础；其次，设计了基于客观事件信号（启动步骤、过度自信、语言犹豫）的稀疏触发机制，替代了低效的每一步或周期性轮询，大幅减少了LRM调用次数；最后，通过这种解耦设计（LRM负责关键规划与校正，SRM负责常规执行），在保持与全LRM相当准确性的同时，显著提升了推理效率并降低了成本。

### Q4: 论文做了哪些实验？

实验设置方面，论文使用了具有思维链推理能力的大模型（LRM）和小模型（SRM）进行组合测试，具体包括QwQ-32B、Qwen3-30B-A3B-Thinking-2507作为LRM，以及DeepSeek-R1-1.5B和Qwen3-0.6B作为SRM，共评估了四种SRM-LRM配对。实验在8张NVIDIA RTX 4090 GPU上使用SGLang推理引擎进行，默认生成参数为temperature=0.6，top_p=0.95，默认token预算为8192。

数据集和基准测试主要使用了三个需要复杂推理的数学和科学问答数据集：AIME24、AIME25（高中数学竞赛题）和GPQA Diamond（研究生级多学科选择题）。此外，在附录中还补充了在Big-Bench Hard（BBH）和AI2 Reasoning Challenge（ARC）上的逻辑与常识推理实验。

对比方法包括：（1）仅使用SRM或仅使用LRM的独立推理基线；（2）基于轮询的协作方法SpecReason。

主要结果和关键指标如下：在准确性上，TrigReason在三个主数据集上平均达到了LRM性能的105.8%（AIME24）、104.7%（AIME25）和99.6%（GPQA Diamond），匹配甚至在某些配置下（如Qwen3-0.6B + Qwen3-30B-A3B-Thinking在AIME24上）超过了LRM基线（达到119.3%）。在效率上，TrigReason相比SpecReason，将更多的推理步骤卸载给了SRM，SRM生成的token比例（SMT百分比）平均提高了1.70倍至4.79倍。在模拟的边缘-云部署场景中（SRM本地运行，LRM通过API调用），TrigReason将59.4%的推理token卸载给SRM，仅使用LRM生成40.6%的步骤，在AIME24上相比完全使用LRM的准确率仅绝对下降2.49%，同时降低了43.9%的延迟和73.3%的API成本。消融实验验证了三个触发器的必要性，并确定了关键超参数：战略启动步数n=20、认知过载阈值ρ（DeepSeek-R1-1.5B为0.85，Qwen3-0.6B为0.75）和干预修正步数m=1。在BBH和ARC上的扩展实验也显示TrigReason取得了优于SRM和SpecReason的准确率（BBH: 0.687，ARC: 0.948），甚至略超LRM。

### Q5: 有什么可以进一步探索的点？

本文提出的TrigReason框架在提升推理效率方面具有显著优势，但其触发机制的设计仍存在局限性，为未来研究提供了多个探索方向。首先，当前触发条件（如过度自信）依赖于启发式标准，其与真实推理错误之间的关联机制尚不明确，未来可深入研究更精准、可理论解释的触发信号，例如结合模型内部表征或不确定性量化。其次，该方法以减少延迟为主要目标，但引入了小模型的额外内存开销，在资源受限的边缘设备上部署可能受限，未来可探索模型压缩、动态加载等轻量化技术以平衡效率与资源消耗。此外，框架目前主要针对特定推理任务，其泛化性到多模态、开放式对话等复杂场景仍需验证。结合个人见解，可能的改进包括：设计自适应触发阈值，使系统能根据任务难度动态调整干预策略；探索多智能体协同机制，允许多个小模型分工协作，进一步降低对大模型的依赖；或将触发逻辑与强化学习结合，通过环境反馈优化干预决策，实现更智能的协作推理。

### Q6: 总结一下论文的主要内容

该论文针对大型推理模型推理延迟高的问题，提出了一种基于触发机制的大小模型协作推理框架TrigReason。核心贡献在于系统分析了小型推理模型的能力边界，识别出路径发散、认知过载和恢复无力三类常见风险，并设计了相应的选择性干预触发机制。该方法将大部分推理步骤委托给小型模型，仅在初始战略规划、检测到异常高置信度或陷入无效循环等关键节点触发大型模型介入。实验表明，TrigReason在多个基准测试上达到了与纯大型模型相当的精度，同时将更多推理步骤卸载给小型模型，显著降低了延迟和API成本，实现了精度、效率与成本之间的更好权衡。
