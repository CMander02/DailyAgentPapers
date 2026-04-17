---
title: "Autonomous Evolution of EDA Tools: Multi-Agent Self-Evolved ABC"
authors:
  - "Cunxi Yu"
  - "Haoxing Ren"
date: "2026-04-16"
arxiv_id: "2604.15082"
arxiv_url: "https://arxiv.org/abs/2604.15082"
pdf_url: "https://arxiv.org/pdf/2604.15082v1"
categories:
  - "cs.AR"
  - "cs.AI"
tags:
  - "Multi-Agent"
  - "Tool Use"
  - "Code Generation"
  - "Self-Improvement"
  - "Autonomous Systems"
  - "EDA"
  - "LLM Agents"
relevance_score: 8.0
---

# Autonomous Evolution of EDA Tools: Multi-Agent Self-Evolved ABC

## 原始摘要

This paper introduces the first \emph{self-evolving} logic synthesis framework, which leverages Large Language Model (LLM) agents to autonomously improve the source code of \textsc{ABC}, the widely adopted logic synthesis system. Our framework operates on the \emph{entire integrated ABC codebase}, and the output repository preserves its single-binary execution model and command interface. In the initial evolution cycle, we bootstrap the system using existing prior open-source synthesis components, covering flow tuning, logic minimization, and technology mapping, but without manually injecting new heuristics. On top of this foundation, a team of LLM-based agents iteratively rewrites and evolves specific sub-components of ABC following our ``programming guidance`` prompts under a unified correctness and QoR-driven evaluation loop. Each evolution cycle proposes code modifications, compiles the integrated binary, validates correctness, and evaluates quality-of-results (QoR) on \emph{multi-suite benchmarks including ISCAS~85/89/99, VTR, EPFL, and IWLS~2005}. Through continuous feedback, the system discovers optimizations beyond human-designed heuristics, effectively \emph{learning new synthesis strategies} that enhance QoR. We detail the architecture of this self-improving system, its integration with \textsc{ABC}, and results demonstrating that the framework can autonomously and progressively improve EDA tool at full million-line scale.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决电子设计自动化（EDA）工具，特别是逻辑综合工具，在开发和演进过程中面临的根本性挑战。研究背景是，以ABC系统为代表的EDA工具是硬件设计的计算核心，集成了数十年的专家工程经验、算法创新和领域特定的启发式设计。然而，这些工具的开发和维护极其困难：其操作搜索空间是组合性的，算法组件交互方式微妙，且新的优化通常需要大量的重新设计工作。因此，EDA工具的进步根本上受限于其高度依赖人力、以启发式驱动的本质。

现有方法的主要不足体现在几个方面：首先，尽管有许多针对ABC的扩展研究（如基于切割的映射、布尔重写、流程调优算法等），但它们大多以外部原型、松散集成的脚本或临时二进制文件的形式存在，其能力难以被整合到ABC的单体式代码库中。其次，ABC代码库本身规模庞大（超过120万行C代码）、结构复杂且组件深度互联，修改影响深远，导致其难以演进。再者，即使在内置算法中，许多启发式规则（如切割选择、重构条件等）是由专家静态设计的，很少被重新审视，可能限制了潜在的性能（QoR）提升。此外，先前利用大型语言模型进行代码自主演进的研究（如AlphaEvolve、SATLUTION）主要针对孤立函数、小规模内核或数万行代码的仓库，其技术无法直接适用于ABC这种百万行级别、具有多目标优化需求的完整EDA工具。

本文要解决的核心问题是：能否构建一个可扩展的、基于多智能体LLM的框架，以自主地演进整个ABC逻辑综合系统的源代码，从而克服上述规模、复杂性和集成障碍，并发现超越人类设计启发式的新优化策略，最终实现EDA工具在完整仓库规模上的自主持续改进。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类，其中与本文工作关系最密切的是基于LLM的自主代码进化框架。

**方法类相关研究**：主要包括Google DeepMind的AlphaEvolve和NVIDIA的SATLUTION。AlphaEvolve首次展示了LLM智能体可以通过生成变体和评估行为来改进紧凑的算法内核（通常仅数百行代码），但其局限在于只能处理依赖关系极少的独立程序。SATLUTION则将自主代码进化扩展到仓库规模（数万行C/C++代码），通过规划与编码智能体的协调及严格的正确性检查（如DRAT证明验证），成功进化出超越人工设计的SAT求解器。本文工作与这两者的核心思想一脉相承，均采用“代码生成-执行-反馈”的迭代进化范式。然而，本文处理的对象——ABC逻辑综合系统（超过120万行C代码、4000多个源文件）——在规模和复杂性上远超前者。ABC内部模块高度耦合，且优化目标多元（面积、延迟、深度等），而非单一的运行时间指标，这使得直接套用现有框架不可行。因此，本文引入了多智能体协调、领域引导的结构化设计以及更严密的正确性与QoR驱动评估循环，以应对大规模EDA工具特有的挑战。

**应用类相关研究**：背景部分提及了逻辑综合领域的传统研究，特别是ABC系统本身所集成的数十年算法创新（如重写、重替代、重构和基于切割的映射等），以及其依赖的大量人工设计的启发式规则。这些构成了本文系统进化的初始代码基础和性能基准。本文框架并非从零开始创造算法，而是在此现有基础上，让智能体自主探索和修改启发式策略，其目标是发现超越人类手工设计、未被探索的优化可能性，从而实现工具的自我持续改进。这与传统依靠专家经验缓慢、迭代的人工开发模式形成了根本区别。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于大型语言模型（LLM）的多智能体自进化框架，来解决自动化改进EDA工具ABC源代码的问题。其核心方法是让多个专门的LLM智能体在统一的正确性和结果质量（QoR）驱动评估循环下，迭代地重写和进化ABC的特定子组件。

**整体框架与主要模块**：系统架构包含一个**规划智能体**和三个**编码智能体**，它们在一个共享的规则库和统一的评估管道下协同工作。规划智能体负责全局协调，解读QoR反馈，汇总各编码智能体的修改提议，并决定下一步进化哪个子系统。三个编码智能体分工明确：1）**流程智能体**：负责进化流程调度和过程编排层，工作在集成自FlowTune的模块（src/opt/flowtune/），专注于改进过程选择启发式、停止准则和条件流程步骤。2）**映射智能体**：负责技术映射子系统（src/map/mapper/），优化切割枚举、剪枝和成本评分的启发式参数。3）**逻辑最小化智能体**：负责技术无关的逻辑优化，工作在现有模块（src/base/abci/）及编排扩展部分。所有智能体的修改都严格限定在其指定的目录内，以避免冲突并保持ABC的架构不变性。

**关键技术流程（进化迭代循环）**：
1.  **规划**：规划智能体根据上一周期的QoR反馈和智能体提议，制定下一步进化策略。初始周期（Cycle 0）通过人工提供的结构化Markdown教程等进行引导，后续周期完全自主。
2.  **编码**：各编码智能体根据规划，在其负责的子系统内生成代码修改（diff文件）。
3.  **编译与正确性预检**：修改后的代码库被编译。编译成功后，立即使用ABC的组合等价性检查（CEC）引擎进行形式化验证，确保功能语义不变。任何不匹配都会导致迭代被拒绝。
4.  **基准评估与反馈集成**：通过分布在87个CPU节点上的大规模工作流，对进化后的ABC版本进行详尽评估。评估使用多套基准（ISCAS, VTR等）和八种不同的综合流程，收集包括STA时序、面积、AIG节点数、深度等在内的多维QoR指标。系统根据这些数据计算奖励，改进被纳入工具的“冠军”版本，性能回退则触发回滚。
5.  **自进化规则库**：一个核心创新点是**自进化规则库**，它管理多智能体协调并约束代码修改。规划智能体会根据QoR反馈中出现的模式，动态评估、提议放松或细化这些规则，使系统能从早期保守的稳定性优先，逐步转向后期更具探索性的结构修改。

**创新点**：
1.  **多智能体协同进化**：采用领域对齐的多个专门智能体，而非单一智能体，分别处理流程、映射和逻辑优化等不同子系统，实现了对百万行级代码库的协调、无冲突进化。
2.  **引导式自主启动与严格的形式化保障**：通过前期知识库探索（集成FlowTune等）为智能体提供高质量的初始代码和结构指导，并在每个迭代后强制执行CEC，从根本上防止了功能错误导致的虚假QoR改进和循环浪费。
3.  **动态自进化规则库**：规则本身可以根据进化过程中的反馈进行适应性调整，使系统具备从学习修改参数到学习修改策略的进化能力。
4.  **高密度、多维反馈驱动**：利用大规模分布式评估，在每次迭代中收集极其丰富的中间结构信号和最终QoR指标，为智能体提供了高分辨率的改进指导。

### Q4: 论文做了哪些实验？

实验在由87个AMD EPYC CPU节点组成的分布式集群上执行，使用企业版Cursor环境实现多智能体系统，所有智能体均基于Claude 4.5 Sonnet模型。每个进化周期中，评估使用ASAP7 7nm工艺库的八种综合流程，覆盖逻辑优化、映射、缓冲、门尺寸调整和静态时序分析等阶段。使用的基准测试套件包括ISCAS’85、ISCAS’89、ITC’99、EPFL、VTR DSP以及一系列算术模块。

实验对比了进化子系统与原始（Vanilla）子系统的不同组合，主要关注三个子系统：FlowTune（流程调优）、AIG Syn（逻辑综合编排）和Map（技术映射）。关键数据指标为归一化的平均结果质量（QoR，越低越好），以原始配置（Vanilla FT + Vanilla Orch + Vanilla Map）为基准1.000。

主要结果显示：单一子系统进化带来适度提升，如进化FlowTune使QoR降至0.962，进化AIG Syn降至0.957，进化Map降至0.988。两个子系统协同进化效果更显著：进化FlowTune与AIG Syn组合QoR为0.924，进化FlowTune与Map组合为0.939，进化AIG Syn与Map组合为0.942。当三个子系统全部进化时达到最佳结果，QoR为0.917，相对于原始基线整体提升约8.3%。此外，最差负时序裕量平均改善约8-9%，部分EPFL算术电路改善达12-15%；面积-延时积减少约8.3%；AIG节点数在算术密集型设计中减少3-8%，映射后深度因深度感知启发式规则减少4-6%。实验表明该系统能自主学习并重组综合流程，在多类电路上产生一致且有意义的QoR提升。

### Q5: 有什么可以进一步探索的点？

本文展示了利用LLM多智能体框架实现EDA工具自主进化的潜力，但仍有诸多可探索方向。局限性在于当前智能体的成功高度依赖领域知识的引导，且其进化建立在EDA社区数十年积累的算法与知识库基础上，尚未实现完全自主的“从零创造”。未来研究可朝以下方向深入：首先，探索如何降低对先验领域知识的依赖，让智能体通过更少的人工指导或更通用的编程规范自主发现优化策略。其次，可将进化框架扩展到其他EDA环节（如物理设计、验证）乃至更广泛的软件系统，验证其泛化能力。此外，当前评估集中于QoR指标，未来可纳入运行时、内存占用等多维目标，实现多目标优化进化。另一个有趣的方向是引入更复杂的智能体协作机制，如竞争或分层决策，以激发更高效的探索。最后，如何保障进化过程中代码的可解释性与安全性，避免陷入局部最优或产生不可控变更，也是实际部署前需解决的关键问题。

### Q6: 总结一下论文的主要内容

这篇论文提出了首个自演进的逻辑综合框架，通过利用大型语言模型（LLM）智能体，自主改进广泛使用的逻辑综合系统ABC的源代码。其核心问题是探索如何让EDA工具在无需人工手动注入新启发式规则的情况下，实现代码级的自主进化与性能提升。

方法上，该框架基于一个多智能体系统。它首先利用现有的开源综合组件进行初始化，覆盖流程调优、逻辑最小化和技术映射。随后，一组LLM智能体在“编程指导”提示下，遵循一个统一的正确性和结果质量驱动的评估循环，迭代地重写和进化ABC的特定子组件。每个进化周期包括：提出代码修改、编译集成二进制文件、验证正确性，并在包含ISCAS、VTR、EPFL和IWLS 2005等多套基准测试上评估结果质量。

主要结论和贡献在于，该框架成功实现了在百万行代码规模上对ABC工具的自主渐进式改进。通过持续的反馈循环，系统发现了超越人工设计启发式规则的优化方法，有效地学习了新的综合策略，从而提升了结果质量。这证明了基于LLM的多智能体系统能够自主演进复杂EDA工具的可行性，为EDA工具的自动化开发和优化开辟了新路径。
