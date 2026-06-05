---
title: "From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws"
authors:
  - "Mengzhuo Chen"
  - "Junjie Wang"
  - "Zhe Liu"
  - "Yawen Wang"
  - "Qing Wang"
date: "2026-06-04"
arxiv_id: "2606.06324"
arxiv_url: "https://arxiv.org/abs/2606.06324"
pdf_url: "https://arxiv.org/pdf/2606.06324v1"
categories:
  - "cs.SE"
  - "cs.MA"
tags:
  - "LLM Agent 调试"
  - "Agent 框架"
  - "轨迹分析"
  - "Harness修复"
  - "自我改进"
relevance_score: 8.5
---

# From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws

## 原始摘要

LLM-based agents increasingly rely on harnesses that provide execution environments, tool interfaces, context, lifecycle orchestration, observability, verification, and governance. Existing self-improving agents and automatic harness evolution methods mainly improve agents through runtime supervision, prompt optimization, workflow search, or harness modification based on final outcomes. However, they often fail to diagnose where the responsible evidence lies in failed trajectories and which harness layer causes the unreliable behavior, resulting in broad, indirect, or poorly scoped changes. This paper proposes HarnessFix, a trace-guided framework for diagnosing agent failures and repairing agent harnesses. HarnessFix compiles raw execution traces and harness code into a Harness-aware Trace Intermediate Representation (HTIR), which normalizes fragmented trajectory evidence and captures step-level provenance and control-flow relations. It then attributes failures to responsible trajectory steps and harness layers, consolidates recurring diagnoses into actionable flaw records, and maps them to scoped repair operators. Finally, HarnessFix generates and validates harness patches under flaw-specific repair specifications to reduce target flaws without introducing unacceptable regressions. We evaluate HarnessFix on SWE-Bench Verified, Terminal-Bench 2.0 Verified, GAIA and AppWorld. Across these benchmarks, HarnessFix improves held-out test performance over the initial harnesses by 15.2%--50.0%, outperforms human-designed and self-evolution baselines, and reveals recurring harness-flaw patterns across ETCLOVG layers.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于LLM的智能体（agent）在执行复杂任务时，因“智能体框架”（harness）缺陷导致失败，而现有方法无法精准诊断和修复这些缺陷的问题。研究背景是，LLM智能体的可靠性不仅依赖于基础模型，更依赖于其运行时框架（harness），该框架包含执行环境、工具接口、上下文、生命周期、可观测性、验证和治理（ETCLOVG七层）等关键组件。现有方法的不足主要有两点：一是大多采用运行时监督或自适应修正等“临时绕过”策略，虽能提升表面性能，却未修复底层框架的根本缺陷；二是基于最终结果（如成功率）进行优化（如提示词优化或工作流搜索），缺乏对失败轨迹中关键证据的细粒度因果诊断，导致修改范围广泛、间接或定位不准。因此，本文提出的核心问题是：如何从失败的智能体执行轨迹出发，自动诊断出具体的故障证据位于哪个轨迹步骤、对应框架的哪一层，并据此进行有针对性且范围可控的框架修复，从而可靠地提升智能体在未见过任务上的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 自改进Agent与提示优化方法**：这类工作通过运行时监督、提示优化或工作流搜索来提升Agent性能，部分研究基于最终结果修改执行环境。与本文的关键区别在于，这些方法通常无法精准诊断失败轨迹中责任证据的具体位置以及导致不可靠行为的具体harness层，从而实施宽泛、间接或范围不当的修改。

**2. 自动Harness演化方法**：该类研究侧重于通过修改harness组件（如工具规范、代码适配器）来改进Agent。本文的主要区别在于，这些方法往往仅利用最终结果进行泛化调整，缺乏对失败轨迹的细粒度归因分析，容易在多轮、跨harness层的复杂失败场景中产生偏差。

**3. Agent评测与稳健性研究**：相关工作围绕基准测试（如SWE-Bench、GAIA）和Agent可靠性分析展开，但主要关注模型能力或任务失败模式，未系统性地将失败归因于harness层的具体缺陷。本文首次提出基于追踪的归因框架，将失败证据与ETCLOVG七层harness架构显式关联，并设计针对性的修复算子。

综上，本文的独特贡献在于提出HarnessFix框架，通过编译追踪中间表示（HTIR）实现step级归因，系统诊断并修复harness缺陷，在多个基准上显著优于现有方法。

### Q3: 论文如何解决这个问题？

HarnessFix提出了一种基于轨迹引导的框架，用于诊断代理故障并修复其运行支撑系统（Harness）。核心在于通过细粒度、轨迹驱动的故障诊断来驱动Harness修复，而非盲目修改。整体框架包含四个由LLM驱动的智能体：轨迹抽象智能体、诊断智能体、修复智能体和验证智能体。

关键技术包括：首先，轨迹抽象智能体将原始执行轨迹和Harness代码编译成“Harness感知轨迹中间表示”（HTIR）。HTIR由多个TraceStep节点（代表模型调用、工具操作等步骤）及其间的三类链接（时间链接、输入来源链接、控制流链接）构成，并为每个节点附加上下文、状态效果等本地化诊断证据，还将每个步骤映射到ETCLOVG层（执行环境、工具接口、上下文与记忆、生命周期与编排、可观测性、验证与评估）中，指明哪些Harness层与此步骤相关。其次，诊断智能体基于HTIR进行故障归因：从失败信号出发，通过证据回溯和候选步裁定，定位责任步骤及其对应的Harness层，生成结构化诊断记录。然后，诊断智能体汇总多次执行中的诊断记录，将具有相同根因的记录合并为“缺陷记录”，代表重复出现的Harness缺陷模式。最后，修复智能体将缺陷记录映射到预设的“修复算子”（如沙箱边界收紧、工具模式精简、循环保护等），并实例化为缺陷特定的修复规约，据此生成修复补丁。验证智能体则确保补丁不引发新的回归。创新点在于：通过HTIR实现了对异质轨迹的统一表示和局部化诊断证据组织，将故障精确归因到轨迹步骤和Harness层，并通过预定义的修复算子进行范围受限、可验证的自动修复。

### Q4: 论文做了哪些实验？

论文在四个基准测试上评估了HarnessFix：SWE-Bench Verified（代码修复）、Terminal-Bench 2.0 Verified（终端命令操作）、GAIA（开放研究问答）和AppWorld（应用自动化）。实验采用2:1:2的训练/验证/测试集划分（如SWE-Bench使用100/50/100个任务）。初始harness分别为mini-swe-agent、Harbor Terminus-2、open-deep-research和AppWorld官方agent。对比方法包括两类：人工设计的典型harness（如OpenHands、Trae-Agent、DeepResearchAgent等）和自演化/修复基线（GEPA、SCOPE、ReCreate）。在测试集上，HarnessFix将初始harness的通过率提升了15.2%-50.0%，并且持续优于所有基线，例如在SWE-Bench上，HarnessFix (35.0%) 显著超过最佳自演化基线ReCreate (24.0%) 和最佳人工基线OpenHands (29.0%)。消融实验评估了四个变体：无诊断、无修复、无HTIR、无迭代，结果证明所有组件对性能提升都是必要的，缺失任一组件均导致准确率明显下降。关键数据显示，HarnessFix在各基准上均展现出稳定的提升，并揭示了跨ETCLOVG层的常见harness缺陷模式。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要体现在以下几个方面。首先，HarnessFix目前依赖LLM进行诊断和修复，其上限受限于基础模型的推理能力，未来可探索将检索增强生成（RAG）或更结构化的知识库融入诊断流程，以提升对复杂、罕见错误的归因精度。其次，当前的修复操作符（repair operators）是从已有人工修改记录中提取的，可能覆盖不全新颖的夹具缺陷模式，未来可以研究自动化操作符发现方法，通过聚类历史修复代码或利用静态分析动态生成新的修复模板。此外，论文主要聚焦于单次失败轨迹的诊断，但实际应用中多个故障可能交互影响，探索多故障关联与联合修复策略是一个重要方向。另外，HTIR的构建严重依赖LLM对轨迹语义的理解，其准确性可能受噪声或非标准日志格式影响，可以尝试引入基于规则或较小模型的预过滤层来提升鲁棒性。最后，将HarnessFix扩展到多智能体协作场景或异步、分布式环境中也是很有价值的研究方向，因为这类场景下的因果链更复杂。

### Q6: 总结一下论文的主要内容

HarnessFix提出了一个基于轨迹引导的框架，用于诊断和修复LLM代理的“线束”（harness）缺陷。该框架首先定义了一个问题：现有方法常忽视失败轨迹中的责任证据，导致修复泛化或范围不当。方法上，HarnessFix通过四步流程解决：1) 将原始执行轨迹和线束代码编译为线束感知轨迹中间表示（HTIR），标准化证据并追踪控制流；2) 诊断代理将失败归因于具体轨迹步骤和线束层，聚合为可操作的缺陷记录；3) 修复代理根据缺陷记录生成受限的修复补丁；4) 验证代理确保补丁减少目标缺陷且不引入退化。在SWE-Bench、GAIA等基准上，HarnessFix使测试性能提升15.2%-50.0%，超越人工设计和基线方法。核心贡献在于将修复从结果驱动转向诊断驱动，揭示了跨线束层的通用缺陷模式，显著提升了代理在长期交互任务中的可靠性。
