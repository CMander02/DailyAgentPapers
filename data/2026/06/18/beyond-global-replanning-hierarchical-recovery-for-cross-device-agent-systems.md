---
title: "Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems"
authors:
  - "Shu Yao"
  - "Yuhua Luo"
  - "Qian Long"
  - "Jingru Fan"
  - "Zhuoyuan Yu"
  - "Yuheng Wang"
  - "Lin Wu"
  - "Yufan Dang"
  - "Huatao Li"
  - "Chen Qian"
date: "2026-06-18"
arxiv_id: "2606.20487"
arxiv_url: "https://arxiv.org/abs/2606.20487"
pdf_url: "https://arxiv.org/pdf/2606.20487v1"
categories:
  - "cs.CL"
tags:
  - "Multi-Device Agent"
  - "Hierarchical Replanning"
  - "Agent Recovery"
  - "Cross-Device Execution"
  - "Failure Robustness"
  - "Benchmark"
  - "H-RePlan"
  - "HeraBench"
relevance_score: 9.5
---

# Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems

## 原始摘要

Real-world computer-use tasks often span multiple applications and devices, requiring agents to coordinate heterogeneous environments under dynamic runtime failures. Existing multi-device agent systems support task decomposition and cross-device assignment, but recovery remains largely coarse-grained: when execution fails, they typically retry the same strategy, reassign the subtask, or revise the global plan, without systematically modeling the device-local strategy space. This limits their ability to distinguish failures that can be repaired within the current device from those that require cross-device replanning. We propose \textbf{H-RePlan}, a hierarchical replanning framework for multi-device agents with unified API--CLI--GUI execution. H-RePlan equips each device with interchangeable execution strategies and separates device-local strategy recovery from orchestrator-level global replanning through a compact cross-layer failure abstraction. To evaluate this capability, we introduce \textbf{HeraBench}, a fault-injected benchmark that constructs cross-device workflows over Linux and Android devices and injects strategy- and device-level failures. Experiments show that H-RePlan substantially outperforms single-strategy and coarse-grained multi-device baselines, achieving higher completion, instruction adherence, and perfect-pass rates while reducing the token cost required for reliable end-to-end success. These results demonstrate that scope-aware hierarchical recovery is essential for robust multi-device agent execution.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决跨设备智能体系统在动态运行时故障下的恢复问题。随着实际计算机使用任务常跨越多个应用和设备，现有系统支持任务分解和跨设备分配，但其故障恢复机制是粗粒度的：当执行失败时，它们通常只会重试相同策略、重新分配子任务或修改全局计划。这种方法的根本缺陷在于，系统未能系统性地建模每个设备内部的策略空间（如API、CLI、GUI等执行方式），因此无法区分故障范围——那些可以在当前设备内通过切换执行策略修复的局部故障，与那些必须触发跨设备重新规划的全局故障。这导致要么将局部策略失败错误地升级为跨设备重新规划，造成不必要的开销和上下文丢失；要么放任故障无法解决。本文提出H-RePlan框架，其核心在于引入一种与平台无关的统一策略控制抽象，为每个设备配备可互换的执行策略，并通过紧凑的跨层故障抽象将设备本地策略恢复与调度器级别的全局重新规划明确分离。同时，论文构建了HeraBench基准测试集，注入策略级和设备级故障以评估分层恢复能力，目标是实现更高效、更鲁棒的跨设备任务执行。

### Q2: 有哪些相关研究？

本文研究跨设备智能体的层级重规划，相关工作可分为两类：

1. **执行策略与重规划方法**：现有研究涵盖反馈驱动的动作修正、失败示例反思、计划精炼、失败感知分解、GUI智能体重规划及测试时规划分配。这些工作表明执行反馈可修复动作、修订计划并协调智能体。H-RePlan在此基础上，针对多设备场景进行扩展——同一设备内允许多种执行策略共存，且失败不仅影响本地执行，还影响跨设备任务分配。

2. **多设备智能体与恢复评估**：跨设备智能体系统如CRAB和UFO³支持任务分解、跨设备分配及运行时计划更新。但恢复机制仍较粗粒度，主要依赖重试、任务更新或设备级重新分配，未系统建模设备本地策略空间。H-RePlan的层级恢复区分了策略级失败（本地处理）和设备级失败（升级处理）。现有基准（如Web、OS、移动、混合控制等）未明确按恢复范围参数化多设备场景中的失败。HeraBench填补此空白，通过注入策略级和设备级失败评估恢复能力。

### Q3: 论文如何解决这个问题？

H-RePlan通过层次化重规划框架解决跨设备代理系统中粗粒度恢复的问题，核心方法是将设备级策略恢复与编排器级全局重规划分离。整体架构由三个关键组件构成：编排器、策略规划器和策略执行代理。

编排器负责全局计划，包含三种操作模式：任务创建时将用户指令分解为有序子任务链；信息追加在子任务成功后提取结果并注入下游依赖子任务；全局重规划在子任务失败时，基于跨层故障抽象重写剩余任务链。策略规划器是设备级规划者，在创建、进度检查和重规划三个状态间切换，能够选择API、CLI或GUI执行策略，并在本地可恢复时切换策略，不可恢复时向上升级失败信息。

关键技术包括跨层故障抽象，这是一种紧凑的面向规划的失败抽象，包含失败子任务标识、源设备、故障类型分类、本地策略尝试摘要和升级原因，在不过载全局上下文的前提下提供可操作证据。三个互补的执行代理覆盖完整设备策略空间：API代理负责结构化服务，CLI代理处理本地计算和文件操作，GUI代理用于用户界面交互。

创新点在于通过层次化恢复分离可设备内修复与需跨设备重规划的失败类型，显式建模设备本地策略空间，并通过跨层故障抽象实现设备执行与系统规划间的有效信息桥接，从而提升跨设备代理系统的鲁棒性和执行效率。

### Q4: 论文做了哪些实验？

论文构建了HeraBench基准测试，包含23个种子任务扩展为174个评估变体，在包含两台Linux和两台Android设备的四设备环境下执行。实验注入设备本地故障、全局故障及混合故障三种类型。对比方法包括CRAB（GUI和API版本）和UFO³（GUI和API版本），所有方法共享30分钟超时限制。主要质量指标包括任务完成率、指令遵循率和完美通过率，效率指标为平均每轮token消耗及每个完美通过案例的期望token成本。H-RePlan在混合执行模式下取得了最优结果：完成率75.84%、指令遵循率77.72%、完美通过率36.78%，对比最强的UFO³-GUI仅达到13.79%的完美通过率。效率方面，H-RePlan每个完美通过案例仅需约193万token，较UFO³-GUI的1051万token提升约5.44倍。消融实验显示，移除全局重规划导致完成率降至41.25%，移除策略规划器使指令遵循率降至45.58%，移除跨层故障抽象使完成率降至63.97%，移除API策略使完成率降至59.28%，证明各组件对系统性能均有重要贡献。

### Q5: 有什么可以进一步探索的点？

首先，论文的故障注入基准HeraBench主要针对Linux和Android设备间的协同任务，未来可扩展至更异构的设备生态（如Windows、macOS及物联网设备），并引入更复杂的故障类型（如网络波动、权限突变），以验证H-RePlan的泛化能力。其次，当前的分层恢复机制依赖于预定义的策略空间，可以通过强化学习或在线学习动态优化设备本地策略的切换决策，减少人工设计成本。此外，跨层故障抽象目前为离散化的失败类型，可探索连续隐空间表征（如利用图神经网络建模设备间依赖关系），以实现更细粒度的故障诊断。最后，当前框架在极低资源设备（如智能手表）上的轻量化适配尚未验证，可考虑模型剪枝或蒸馏技术，在保持恢复鲁棒性的同时降低部署门槛。

### Q6: 总结一下论文的主要内容

跨设备代理系统在执行多应用、多设备任务时，面临运行时动态故障，现有方法的重规划粒度粗，无法区分设备内策略故障与跨设备规划故障。为此，论文提出H-RePlan，一种分层重规划框架，为每个设备提供统一的API-CLI-GUI策略空间，并通过紧凑的跨层故障抽象，将设备内策略恢复与编排器全局重规划分离。同时构建了HeraBench基准，在Linux和Android设备上注入策略级和设备级故障以评估恢复能力。实验表明，H-RePlan显著优于单策略和粗粒度多设备基线，在任务完成率、指令遵循率和完美通过率上表现更佳，同时大幅降低了实现端到端成功所需的token成本。该工作证明了显式建模设备内策略空间与跨设备编排对于鲁棒的多设备代理执行至关重要。
