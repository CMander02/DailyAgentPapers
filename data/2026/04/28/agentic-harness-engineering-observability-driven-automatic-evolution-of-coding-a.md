---
title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
authors:
  - "Jiahang Lin"
  - "Shichun Liu"
  - "Chengjun Pan"
  - "Lizhi Lin"
  - "Shihan Dou"
  - "Xuanjing Huang"
  - "Hang Yan"
  - "Zhenhua Han"
  - "Tao Gui"
date: "2026-04-28"
arxiv_id: "2604.25850"
arxiv_url: "https://arxiv.org/abs/2604.25850"
pdf_url: "https://arxiv.org/pdf/2604.25850v1"
categories:
  - "cs.CL"
  - "cs.SE"
tags:
  - "Code Agent"
  - "Agent Evolution"
  - "Observability"
  - "Coding Agent Harness"
  - "Automated Engineering"
  - "Autonomous Improvement"
relevance_score: 8.5
---

# Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses

## 原始摘要

Harnesses have become a central determinant of coding-agent performance, shaping how models interact with repositories, tools, and execution environments. Yet automating harness engineering is hard: a heterogeneous action space, sparse and noisy evaluation signal, multi-million-token trajectories, and edits whose effect is hard to attribute to the next round's outcomes. We introduce Agentic Harness Engineering (AHE), a framework that automates harness-level evolution by instrumenting the three stages of any engineering loop (component editing, trajectory inspection, and decision making) with matched observability pillars: (1) component observability gives every editable harness component a file-level representation so the action space is explicit and revertible; (2) experience observability distills millions of raw trajectory tokens into a layered, drill-down evidence corpus that an evolving agent can actually consume; and (3) decision observability pairs every edit with a self-declared prediction, later verified against the next round's task-level outcomes. Together, these pillars turn every edit into a falsifiable contract, so harness evolution proceeds autonomously without collapsing into trial-and-error. Empirically, ten AHE iterations lift pass@1 on Terminal-Bench 2 from 69.7% to 77.0%, surpassing the human-designed harness Codex-CLI (71.9%) and the self-evolving baselines ACE and TF-GRPO. The frozen harness transfers without re-evolution: on SWE-bench-verified it tops aggregate success at 12% fewer tokens than the seed, and on Terminal-Bench 2 it yields +5.1 to +10.1pp cross-family gains across three alternate model families, indicating the evolved components encode general engineering experience rather than benchmark-specific tuning. These results position observability-driven evolution as a practical pathway to keep coding-agent harnesses continually improving.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决的是编码智能体（coding agent）中“框架工程”（Harness Engineering）的自动化问题。研究背景是，当前编码智能体在完成复杂软件工程任务时，其性能不仅仅取决于底层语言模型（如大语言模型），更依赖于一个复杂的“框架”（harness），包括系统提示词、工具、中间件等组件。这些组件的设计直接决定了智能体如何与代码仓库、工具和执行环境交互，从而显著影响任务完成效果。然而，现有方法存在明显的不足：目前框架的设计和优化主要依赖人工进行，开发者需要手动检查运行轨迹、识别失败模式并修改组件。这个过程成本高昂、难以扩展，且无法跟上模型能力的快速演进。部分尝试自动化的研究主要局限于优化单一组件（如提示词），无法协同演进所有可编辑组件。同时，运行轨迹数据长且结构混乱，缺乏可供演化智能体使用的机器可读信号，导致演化过程容易退化为盲目的试错。

本文要解决的核心问题是：如何让一个演化智能体能够稳定地、可解释地同时优化编码智能体的所有框架组件，而不是仅仅局限于提示词编辑，从而跨越“手工工程”到“自主演化”的鸿沟。

### Q2: 有哪些相关研究？

本文与以下三类相关工作存在关联与区别：

- **方法类（Agent自动化优化）**：相关研究包括基于反馈循环修正输出的反思方法、优化提示与指令的Playbook及语义先验方法、以及通过变异进化程序结构和技能库的方法。AHE的创新在于将整个harness作为可组合的整体进行调优，而非仅编辑单一表面，使跨组件权衡对优化器可见，同时减少人工先验，让方法从实验中自主发现。

- **应用类（编码Agent系统工程）**：涉及工具、接口、记忆、执行约束和反馈回路的设计，以及用于仓库导航、文件编辑和命令执行的定制Agent-计算机接口。AHE建立的观测系统直接构建在这些基础设施之上，通过可复现、可追溯和可验证的执行来支持自动化演进。

- **评测类（编码Agent评估）**：从短视野函数级基准、仓库级可执行补丁解决到多小时终端驱动工作流，覆盖不同任务视野和环境真实性。AHE利用这些基准（如Terminal-Bench 2和SWE-bench-verified）验证其方法，并证明进化后的组件编码了通用工程经验而非基准特定调优。

### Q3: 论文如何解决这个问题？

Agentic Harness Engineering (AHE) 将优化过程构建为一个由另一个智能体驱动的闭环，核心思想是让闭环的每个阶段都可观测。它通过三种观测支柱实现：组件可观测性、经验可观测性和决策可观测性。

整体框架包括迭代循环，在每一轮中执行以下步骤：使用当前装备进行轨迹生成、清理数据、属性归因（从第二轮开始）、通过Agent Debugger进行分层蒸馏、由演化智能体进行编辑决策，以及最终提交和评估。

主要模块/组件方面：首先，组件可观测性由一个解耦的、文件级的装备组件系统实现。NexAU框架将装备分解为七个正交组件类型（如系统提示、工具描述、中间件、技能等），每个类型对应工作空间中的一个独立文件。这使得每个失败模式能映射到单一组件类，赋予演化智能体一个清晰且可回滚的动作空间。其次，经验可观测性通过Agent Debugger框架实现，它抽取原始轨迹中的洞察。该框架将轨迹组织成一个可导航的、基于文件的环境，生成每个任务的根因分析报告，并聚合成一个基准级别的概览，实现渐进式信息揭露以节省token。最后，决策可观测性要求演化智能体做出的每次编辑都附带一个自我声明的预测（预期的修复和可能的风险），并记录在一个版本化的清单（manifest）中。下一轮通过属性归因，将观察到的任务级性能变化与前一清单的预测进行比对，从而为每次编辑提供可证伪的契约。

创新点在于通过这三种可观测性将每个编辑转化为可证伪的契约，使装备演化自动化而不陷入试错，并能够跨模型家族传递通用工程经验。

### Q4: 论文做了哪些实验？

论文围绕三个研究问题（RQ1-RQ3）进行了实验。实验设置上，在Terminal-Bench 2的89个任务（4 easy、55 medium、30 hard）上驱动AHE进化，每个任务1小时超时；跨基准迁移在SWE-bench-verified的500个任务上评估。主要对比方法包括三种人工设计的harness（opencode、terminus-2、Codex）和两种自进化基线（ACE、TF-GRPO），所有方法共享NexAU₀种子，AHE执行10次迭代。

主要结果：
- 主实验：AHE在Terminal-Bench 2上pass@1达到77.0%，超越Codex（71.9%）、ACE（68.9%）和TF-GRPO（72.3%），但Hard难度略低于Codex。
- 跨基准迁移：AHE在SWE-bench-verified上以75.6%的aggregate success领先种子（75.2%），同时token消耗比种子减少12%（461k vs 526k）。
- 跨模型迁移：AHE在五个替代模型上均获得正向pass@1增益（+2.3至+10.1 pp），其中deepseek-v4-flash提升最大（+10.1 pp）。
- 组件消融：单一组件（memory、tool、middleware）分别带来+5.6、+3.3、+2.2 pp增益，但system prompt单独使用导致-2.3 pp；组件间存在非加性交互。
- 预测分析：fix精度33.7%、召回51.4%（约5倍随机基线），但regression精度仅11.8%、召回11.1%（约2倍随机基线）。

### Q5: 有什么可以进一步探索的点？

该论文的局限性和未来探索方向主要集中在以下几个方面：首先，当前评估仅局限于特定基准（Terminal-Bench），未来需在更多编码环境、编程语言和部署场景中验证AHE的泛化能力。其次，组件可编辑性虽带来灵活性，但也增加了过拟合基准的风险，可引入正则化或跨任务验证机制来缓解。第三，治理机制尚不完备，可探索更鲁棒的长周期回滚策略和多层次安全护栏，如自动检测有害编辑模式。此外，计算开销较大，未来可优化迭代效率，例如通过智能采样或增量式轨迹分析降低冗余执行。最后，当前“可伪造契约”机制依赖自我声明预测，可进一步结合因果推断或反事实推理，更精确地归因编辑效果与任务结果间的因果关系，从而提升进化稳定性。

### Q6: 总结一下论文的主要内容

这篇论文提出了Agentic Harness Engineering（AHE）框架，旨在解决编码智能体测试时自我进化中编排层（harness）的自动化工程难题。核心问题在于编排层动作空间异质、评估信号稀疏且存在噪音、轨迹长度达百万级token，以及编辑效果难以归因。AHE通过将工程循环的三个阶段（组件编辑、轨迹检查、决策）与三大可观测性支柱相匹配来解决该问题：(1) 组件可观测性，为每个可编辑组件提供文件级表示，使动作空间明确且可回退；(2) 经验可观测性，将原始轨迹提炼为分层证据语料库以供进化智能体使用；(3) 决策可观测性，为每次编辑附加预测声明，并通过下一轮结果验证。这些支柱将每次编辑转化为可证伪的契约，使编排层能自主进化而非试错。实验表明，十次AHE迭代使Terminal-Bench 2的pass@1从69.7%提升至77.0%，超越了人类设计的编排层Codex-CLI（71.9%）及自进化基线ACE和TF-GRPO。冻结的编排层无需重新进化即可迁移，在SWE-bench-verified上以少于种子12%的token实现更高成功率，在Terminal-Bench 2上为另三个模型家族带来+5.1至+10.1个百分点的增益，表明进化组件编码了通用工程经验而非基准特定调优。该工作将可观测性驱动的进化定位为持续改进编码智能体编排层的实用路径。
