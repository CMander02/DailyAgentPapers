---
title: "Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks"
authors:
  - "Wilson Y. Lee"
date: "2026-02-22"
arxiv_id: "2602.19008"
arxiv_url: "https://arxiv.org/abs/2602.19008"
pdf_url: "https://arxiv.org/pdf/2602.19008v1"
categories:
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent Reliability"
  - "Tool Use"
  - "Agent Failure Analysis"
  - "Long-Horizon Tasks"
  - "Agent Evaluation"
  - "Agent Architecture"
  - "Agent Planning"
relevance_score: 9.0
---

# Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks

## 原始摘要

Why do language agents fail on tasks they are capable of solving? We argue that many such failures are reliability failures caused by stochastic drift from a task's latent solution structure, not capability failures. Every well-defined tool-use task imposes a canonical solution path (i.e., a convergent set of tool invocations shared across successful runs) and agent success depends critically on whether a trajectory stays within this path's operating envelope. We establish this causally using a natural experiment that holds model capability and task difficulty fixed by construction. We analyze trajectories from the Toolathlon benchmark: 22 frontier models each attempt 108 real-world tool-use tasks across 3 independent runs, yielding 515 model$\times$task units where the same model succeeds on some runs and fails on others due to LLM sampling stochasticity alone. Within these units, successful runs adhere significantly more closely to the canonical solution path than failed runs ($+$0.060 Jaccard, $p<0.0001$, $n=488$ units, 95% CI [+0.043, +0.077]). This result survives six robustness checks including cross-model-family leave-one-out validation. Critically, the causal mechanism is gradual and self-reinforcing: the adherence gap is statistically indistinguishable from zero through the first 50% of the trajectory, ruling out early-branching selection bias, and each off-canonical tool call raises the probability that the next call is also off-canonical by 22.7 percentage points ($\hatβ=+0.227$, $p<0.0001$), more than doubling the baseline rate. These findings imply that agent reliability cannot be improved by capability scaling alone, but offer a highly actionable intervention: a simple monitor that restarts the bottom tercile of runs based on mid-trajectory canonical adherence lifts success rates by $+$8.8 percentage points among intervened runs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决一个核心问题：为什么语言智能体（Language Agent）在它们本有能力解决的长周期任务中会失败？作者挑战了主流观点——即失败主要源于智能体的能力不足（如知识、推理或工具使用技能的欠缺）。他们通过实证观察发现，同一个前沿模型在相同条件下多次尝试同一任务时，有时成功有时失败，这种“混合结果”表明存在能力之外的失败原因。

论文提出，许多失败本质上是**可靠性失败**，而非能力失败。其核心论点是：任务存在一个潜在的**规范解决路径**（即成功运行中共同遵循的一系列工具调用集合），智能体的成功关键取决于其执行轨迹是否保持在该路径的操作范围内。失败是由于LLM采样随机性导致智能体逐渐偏离这条规范路径，而非缺乏解决问题的能力。

为了因果性验证这一机制，论文利用了一个“自然实验”：分析Toolathlon基准测试中，同一模型在同一任务上产生不同结果（纯由采样随机性导致）的案例。研究发现，成功运行比失败运行显著更贴近规范路径，且这种偏离是渐进、自我强化的过程——早期的偏离并不明显，但每一次偏离规范的工具调用都会大幅增加后续继续偏离的概率。

因此，论文旨在阐明智能体失败的一种因果机制（规范路径偏离），并指出仅提升模型能力无法解决可靠性问题，需要通过执行过程中的监控与约束（如中期检测并重启偏离轨迹）来提升智能体的可靠表现。

### Q2: 有哪些相关研究？

本文的相关研究主要涵盖以下几个方向：

1. **LLM智能体评测基准**：如WebAgent、WebArena、SWE-bench、AgentBench等，主要评估智能体的**能力**（如pass@1或pass@k），并将失败归因于能力不足。一个重要的例外是τ-bench，它引入了P^k指标来衡量模型在多次独立尝试中的一致性，揭示了能力与可靠性之间的差距。本文的工作为这种“同一模型在同一任务上表现不一致”的现象提供了因果机制解释，即偏离规范路径是导致可靠性失败的结构性根源。

2. **LLM随机性与采样**：现有研究（如自洽性解码、多数投票解码、Pass@k指标）通常将LLM采样的随机性视为一种可**利用的资源**，通过聚合多次运行结果来提高准确性。本文则从一个新视角出发，将随机性视为**可靠性失败的来源**，并研究了其对任务执行轨迹质量的结构性影响。本文首次刻画了随机采样如何导致有能力的智能体失败的具体机制。

3. **定义正确执行**：部分工作通过专家设计的参考计划来定义正确的智能体执行，例如AssetOpsBench。本文的方法不同，它通过跨模型成功运行的共识（CF-LOO方法）**经验性地推导出规范路径**，无需专家标注，使得框架能够扩展到新任务而无需领域知识。

4. **智能体失败分析**：已有研究对LLM智能体的失败模式进行了分类学分析（如推理错误、工具误用、上下文丢失等），这些工作主要是**描述性**的。本文的贡献是**因果性**的，它识别了一个具体机制（规范路径偏离），并提供了因果证据证明该机制决定了模型×任务单元内的成功与否。

5. **规划与任务结构**：一些研究指出了LLM智能体与经典AI规划之间的联系，纽厄尔的“问题空间假说”为本文的规范路径概念提供了理论基础。本文的延伸在于首次为LLM工具使用任务提供了解决方案路径的**实证化操作**，并证明了其因果相关性。

6. **可靠性工程**：工程学中早已区分能力与可靠性，例如佩罗的“正常事故理论”描述了复杂系统中随机扰动如何累积导致失败。本文将这一视角应用于LLM智能体，表明工具选择的随机错误会在智能体轨迹中逐渐累积，这与佩罗关于漂移导致失败的论述一致。

**本文与这些研究的关系**：本文整合了来自评测基准、随机性分析、失败分类和可靠性工程等多个领域的见解，但其核心创新在于通过一个精心设计的“自然实验”，首次**因果性地证明**了“规范路径偏离”是导致有能力智能体在长视野任务中可靠性失败的根本机制。它超越了τ-bench对可靠性差距的现象描述，揭示了其内在结构原因；也超越了描述性的失败分类，提供了可量化、可干预的因果机制。

### Q3: 论文如何解决这个问题？

论文通过定义“规范解路径”并量化智能体轨迹对其的“遵循度”，揭示了智能体在长视野任务中失败的核心因果机制是“渐进式、自我强化的路径偏离”，而非能力不足。其核心方法、架构设计和关键技术如下：

**1. 核心概念定义与量化方法：**
论文首先为每个任务定义了“规范工具集”，即所有成功轨迹中超过50%都使用的工具集合。这是一个描述性的、基于成功经验共识的结构化“操作范围”，而非严格的必要充分条件。通过计算任意轨迹的工具集与规范工具集之间的**杰卡德相似度**，论文量化了该轨迹对规范路径的“遵循度”。这种方法对称地惩罚了“遗漏必要工具”和“使用非规范工具”两种偏离模式。

**2. 因果识别与稳健性验证架构：**
为了确立遵循度与成功间的因果关系，论文设计了一个巧妙的“自然实验”：聚焦于同一模型在同一任务上因采样随机性而产生的“混合结果单元”（即部分运行成功，部分失败）。在此设定下，模型能力和任务难度被固定，成功与失败的差异只能归因于轨迹层面的变化。分析显示，成功运行的遵循度显著高于失败运行（平均差距+0.060杰卡德）。为确保结论稳健，论文进行了六项鲁棒性检验：
- **排除循环定义**：采用留一法定义规范路径，避免自我贡献带来的偏差。
- **排除模型族偏差**：采用跨模型族留一法，确保规范路径是任务属性而非特定模型族的产物。
- **排除领域明显工具**：仅使用通用工具名进行分析，效应依然显著。
- **控制轨迹长度**：对遵循度进行长度残差化处理，排除长度混杂因素。
- **排除任务杠杆效应**：通过留一任务法验证效应非由少数任务驱动。
- **检验阈值敏感性**：改变规范工具集的共识阈值（40%-70%），效应保持稳定。

**3. 揭示渐进式偏离的微观机制：**
论文通过精细的时序分析，驳斥了“早期分支”假说（即一次早期错误导致必然失败）。数据显示，在轨迹的前50%，成功与失败运行的遵循度差距在统计上无法区分，差距仅在后期（75%、100%）才变得显著。这支持了**渐进式累积漂移**机制。进一步的微观分析发现，**每次偏离规范的工具调用，都会使下一次调用也偏离规范的概率增加22.7个百分点**，这比基线概率翻倍还多，形成了自我强化的“漂移复合”效应。这种机制在最终失败的运行中表现得比最终成功的运行更强，说明失败是漂移持续累积直至无法挽回的结果。

**4. 跨模型族的普适性与失败类型诊断：**
效应在11个被测模型族中的10个都呈现正值，其中5个达到统计显著性，表明规范路径遵循是跨模型的普遍任务结构属性。此外，通过分析不同结果类型单元（全成功、全失败、混合结果）内部的遵循度方差，论文区分了“能力失败”与“可靠性失败”：全失败单元方差中等，代表模型能力不足、 consistently 走错路；混合结果单元方差最高，代表模型有能力但受随机漂移影响，处于成败的随机边界，这正是可靠性问题的特征。

**总结**，论文通过构建“规范解路径”这一结构性概念，并设计严谨的因果推断与鲁棒性检验框架，系统性地证明了智能体在有能力任务上的失败，主要源于轨迹在解决过程中逐步、自我强化地偏离了成功的共识结构。这一发现指出，提升智能体可靠性不能仅靠扩展模型能力，而需针对路径偏离进行干预（如论文末尾提出的简单监控重启机制）。

### Q4: 论文做了哪些实验？

论文基于Toolathlon基准数据集设计了一个自然实验，以探究智能体在长视野任务中失败的原因。实验设置如下：使用22个前沿语言模型，每个模型在108个真实世界工具使用任务上独立运行3次，共产生约7000条轨迹。任务涵盖网页导航、文件操作、代码执行等多个领域，平均每个任务需要约20个工具调用步骤。研究聚焦于515个“混合结果单元”，即同一模型在同一任务上部分运行成功、部分失败的情况，从而控制模型能力和任务难度，将结果差异归因于LLM采样随机性导致的轨迹行为变异。

基准测试方面，核心是计算“规范路径遵从度”（使用Jaccard相似度衡量轨迹工具集与任务成功运行共有的规范工具集之间的重叠程度）。主要结果包括：1) 成功运行的规范路径遵从度显著高于失败运行（平均差距+0.060 Jaccard，p<0.0001），且该结果通过了六项稳健性检验（如排除循环定义、家族偏差、轨迹长度混淆等）。2) 通过分析轨迹不同完成点（10%、25%、50%、75%、100%）的遵从度差距，发现差距在轨迹前半段（50%前）统计上不显著，而在后半段显著增大，这反驳了“早期分支”假说，支持了“渐进漂移”机制。3) 微观机制分析表明，一次偏离规范的工具调用会使下一次调用也偏离规范的概率增加22.7个百分点，证实了漂移的自我强化特性。4) 跨模型家族分析显示，11个模型家族中有10个呈现正向遵从度差距，其中5个达到统计显著性，表明该现象具有普遍性。5) 基于上述发现，论文提出了一种简单干预措施：在轨迹中期对遵从度最低的三分之一运行进行重启，可使干预运行的成功率提升8.8个百分点。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于：每个模型-任务单元仅包含三次运行，限制了单元内估计的精度；使用的Jaccard相似度指标基于无序工具集，未能捕捉序列顺序信息；工具路径定义在工具名称层面，未分析参数细节；且假设成功运行收敛于单一主导策略，可能忽略了多模态的有效解法。

未来可进一步探索的方向包括：增加每个单元的重复运行次数以验证效应强度；开发能捕捉工具调用顺序的序列相似度指标；在更细粒度的参数层面分析解决方案结构；研究存在多个同等有效策略的任务，并定义多模态规范路径；将“规范路径偏离”的因果机制与理论（如问题空间假说）更深入结合；探索更复杂的运行时干预策略（如动态调整而非简单重启）；并将该可靠性分析框架扩展到更广泛的智能体任务和基准测试中。

### Q6: 总结一下论文的主要内容

这篇论文的核心贡献在于揭示了语言智能体在长程任务中失败的关键因果机制：并非能力不足，而是可靠性问题导致的“规范路径偏离”。作者提出，每个明确定义的工具使用任务都存在一条“规范解决方案路径”（即成功运行中共享的工具调用序列），智能体的成功与否取决于其执行轨迹是否始终处于这条路径的操作范围内。

通过分析Toolathlon基准测试中22个前沿模型在108个真实世界工具使用任务上的表现，论文利用自然实验设计（固定模型能力和任务难度）发现：在同一模型×任务单元中，成功运行比失败运行显著更贴近规范路径（Jaccard相似度高出0.060）。更重要的是，作者揭示了这一偏离的渐进性与自我强化特性：轨迹前50%的偏离程度几乎为零，但一旦发生偏离，后续调用继续偏离规范路径的概率将增加22.7个百分点。

这项研究的意义在于指出，仅靠提升模型能力无法根本解决智能体可靠性问题，并提出了可操作的干预方案——通过监控轨迹中期的规范路径贴合度，对表现最差的运行进行重启，可将成功率提升8.8个百分点。这为改进智能体系统的设计提供了新的理论视角和实践路径。
