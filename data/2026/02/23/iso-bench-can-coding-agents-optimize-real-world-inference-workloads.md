---
title: "ISO-Bench: Can Coding Agents Optimize Real-World Inference Workloads?"
authors:
  - "Ayush Nangia"
  - "Shikhar Mishra"
  - "Aman Gokrani"
  - "Paras Chopra"
date: "2026-02-23"
arxiv_id: "2602.19594"
arxiv_url: "https://arxiv.org/abs/2602.19594"
pdf_url: "https://arxiv.org/pdf/2602.19594v1"
categories:
  - "cs.LG"
tags:
  - "Agent Benchmark"
  - "Coding Agent"
  - "Inference Optimization"
  - "LLM Serving"
  - "Evaluation Metrics"
  - "Tool Use"
relevance_score: 7.5
---

# ISO-Bench: Can Coding Agents Optimize Real-World Inference Workloads?

## 原始摘要

We introduce ISO-Bench, a benchmark for coding agents to test their capabilities on real-world inference optimization tasks. These tasks were taken from vLLM and SGLang, two of the most popular LLM serving frameworks. Each task provides an agent with a codebase and bottleneck description, whereby the agent must produce an optimization patch evaluated against expert human solutions. We curated 54 tasks from merged pull requests with measurable performance improvements. While existing benchmarks heavily use runtime-based metrics, such approaches can be gamed to pass tests without capturing the actual intent of the code changes. Therefore, we combine both hard (execution-based) and soft (LLM-based) metrics to show that both are necessary for complete evaluation. While evaluating both closed and open-source coding agents, we find no single agent dominates across codebases. Surprisingly, agents often identify correct bottlenecks but fail to execute working solutions. We also show that agents with identical underlying models differ substantially, suggesting scaffolding is as important as the model.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前编码智能体（coding agents）在真实世界推理优化任务中能力评估不足的问题。现有基准（如SWE-bench）主要关注代码修复或功能实现，但缺乏对系统级性能优化任务的专门评测。优化任务（如提升LLM推理引擎的吞吐量）需要深入理解代码瓶颈、内存管理和调度策略，这对智能体提出了更高要求。

作者指出，现有基准大多依赖运行时指标（如执行速度），但这种单一指标容易被“钻空子”——智能体可能通过取巧方式通过测试，而未真正理解优化意图。因此，论文的核心目标是建立一个更全面的评估框架，不仅能衡量智能体是否成功优化，还能诊断其失败原因：是错误识别了瓶颈，还是理解了问题但实现能力不足。

为此，论文提出了ISO-Bench，一个包含54个真实优化任务（取自vLLM和SGLang流行推理框架）的基准，并设计了“硬指标”（基于执行性能）和“软指标”（基于LLM评判）相结合的双重评估体系。通过分析智能体在任务中的表现，论文试图揭示其核心缺陷（如“理解与执行之间的差距”），并为改进编码智能体在复杂系统优化场景下的能力提供方向。

### Q2: 有哪些相关研究？

相关研究主要围绕代码生成与优化的评测基准、智能体架构以及基于LLM的评估方法展开。

在**评测基准**方面，早期工作如HumanEval关注函数级代码的正确性。随后，SWE-bench等仓库级基准要求智能体在真实代码库中解决问题，但核心仍是功能正确性。针对**性能优化**，研究逐渐从正确性转向效率。KernelBench和TritonBench在GPU内核级别评估LLM生成高效代码的能力。在仓库级别，SWE-Perf、GSO和SWE-fficiency等近期研究开始构建从真实性能优化PR中提取的任务，评估智能体实现可量化加速的能力。**本文的ISO-Bench与这些效率驱动基准一脉相承，但专注于LLM推理服务框架（vLLM和SGLang）的优化任务，并强调结合硬性（执行）和软性（LLM评估）指标进行更全面的评估。**

在**智能体架构**方面，研究表明脚手架设计对性能影响巨大。SWE-Agent探索了智能体-计算机接口，OpenHands提供了开放式评估平台，TRAE-Agent则专注于仓库级任务的补丁生成与筛选。商业系统如Claude Code则集成了专有脚手架。**本文发现，即使底层模型相同，智能体表现也可能差异显著，这呼应了“脚手架与模型同等重要”的结论。**

在**LLM评估方法**方面，使用LLM作为评判员（如Judging LLM、ICE-Score、CodeJudge）已成为可扩展的评估手段，但也存在偏好长输出等偏差。**本文采用LLM-based的软性指标来评估智能体是否瞄准了正确的代码瓶颈，正是对此类方法的应用，同时也意识到了其潜在的偏见问题。**

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ISO-Bench的专门基准测试来解决评估编码智能体在真实世界推理优化任务中能力的问题。其核心方法、架构设计和关键技术如下：

**核心方法与架构设计：**
ISO-Bench的架构是一个端到端的评估流水线。它首先从两个广泛使用的生产级LLM服务框架（vLLM和SGLang）中，通过一个多阶段的筛选流程（关键词过滤、LLM分类、人工审核）收集了54个已验证的性能优化任务。每个任务为智能体提供两个输入：1) 优化前的代码库提交状态；2) 描述待解决性能瓶颈（但不透露解决方案）的任务说明。智能体需要生成一个优化补丁。

**关键技术：**
1.  **双重评估指标（Hard & Soft Metrics）**：这是ISO-Bench的核心创新。**硬指标**基于实际执行，使用原始拉取请求中开发者使用的相同基准测试工具，测量并比较智能体补丁与人类专家方案在“首令牌时间”和“吞吐量”上的性能差异，并以5%为阈值进行分类（超越、相似、更差、失败）。**软指标**则使用“LLM即法官”的方法，评估智能体补丁在“瓶颈定位”和“实现方法”两个维度上与人类方案的语义相似性，以判断其是否理解了真正的优化目标。
2.  **四象限分析框架**：通过将硬指标（性能好坏）和软指标（目标正确与否）相结合，将每次优化尝试分类到四个象限：Q1（真正成功：目标正确且性能好）、Q2（良好意图，糟糕执行：目标正确但性能差）、Q3（侥幸获胜：目标错误但性能好）、Q4（完全失败：目标错误且性能差）。该框架能清晰区分基于硬指标的“表面成功”和结合软指标的“真正成功”，揭示了智能体常能识别正确瓶颈但无法实现有效方案（Q2）等关键现象。
3.  **功能正确性验证**：对于所有通过硬指标显示成功的案例（Q1+Q3），论文额外使用LM评估工具链验证优化补丁是否保持了模型输出的准确性，防止智能体通过改变模型行为来“作弊”获得性能提升，这对于识别Q3（侥幸获胜）中的无效优化尤为关键。

综上，论文通过构建一个源自真实生产环境的任务集，并创新性地结合执行性能、语义理解和功能正确性的多层次评估体系，系统地解决了如何全面、可靠地评估编码智能体在复杂推理优化场景中实际能力的问题。

### Q4: 论文做了哪些实验？

论文在ISO-Bench基准上对多个编码智能体进行了系统性实验。实验设置包括：评估了三种不同架构的智能体（Claude Code、Codex CLI和基于TRAE框架并搭载不同底层模型的两个变体），每个智能体在包含54个真实优化任务（39个来自vLLM，15个来自SGLang）的代码库上工作。每个任务在独立的Docker容器环境中进行，智能体拥有120分钟的时间探索代码库、修改文件并提交优化补丁。

基准测试采用硬指标和软指标相结合的综合评估协议。硬指标在NVIDIA H100 GPU上执行，测量优化补丁相对于未优化基线和人类专家方案的TTFT和吞吐量性能提升。软指标则采用基于LLM的评判，分析智能体补丁与人类补丁在瓶颈定位和实施方法上的一致性。

主要结果显示：1）**性能表现差异显著**：没有单一智能体在所有代码库上占优。例如在vLLM上，Claude Code的“真实成功率”（True Success）最高（46.2%），但在SGLang上其成功率骤降至26.7%，而TRAE (GPT-5)在SGLang上达到86.7%的高成功率。2）**硬指标存在局限性**：实验揭示了“硬成功率”（Hard Success）与“真实成功率”之间的差距（最高达20%），表明智能体有时通过修改无关代码偶然获得性能提升，而软指标能有效识别此类“幸运获胜”（Lucky Wins）。3）**失败模式分析**：智能体常能正确识别瓶颈（良好意图），但无法产出有效解决方案（糟糕执行），这在vLLM任务中尤为明显。4）**智能体架构的重要性**：即使使用相同的底层模型（如Claude Sonnet 4.5），不同架构的智能体（Claude Code vs. TRAE (Sonnet)）因探索策略和决策逻辑不同，性能表现差异巨大。5）**功能正确性验证**：实验对所有获得性能提升的补丁进行了功能正确性测试，发现某些“幸运获胜”案例虽提升了速度，却严重破坏了模型输出准确性。

### Q5: 有什么可以进一步探索的点？

基于论文讨论，未来可进一步探索的点包括：**扩展数据集范围**，纳入更多推理系统（如TensorRT-LLM）和涉及多文件修改的架构级优化任务，以评估智能体在复杂系统级变更中的能力。**降低数据污染风险**，通过时间过滤、补丁改写或使用未公开代码库来减少模型记忆的影响。**提升软指标可靠性**，引入多模型评估和人工标注验证，增强评估结果的稳健性。**拓宽硬件支持**，将基准测试扩展到多GPU环境（如张量并行）和不同硬件平台（如AMD、TPU），检验优化方案的跨平台泛化性。此外，**改进智能体脚手架设计**以解决执行失败问题，并探索如何提升智能体在识别瓶颈后实际实现有效优化的能力。

### Q6: 总结一下论文的主要内容

这篇论文提出了ISO-Bench，一个专门用于评估代码智能体在真实世界推理优化任务中能力的基准测试。其核心贡献在于填补了现有评测的空白，将评估场景从传统的算法题或代码补全，转向了从主流LLM服务框架（vLLM和SGLang）的实际合并请求中提取的、具有明确性能提升目标的复杂优化任务。论文强调，仅依赖运行时指标的评测可能被“欺骗”，因此创新性地结合了基于执行的“硬指标”和基于LLM评估的“软指标”，以更全面地衡量代码修改是否真正符合优化意图。研究发现，当前没有智能体能主导所有任务，且它们常能识别瓶颈却无法产出有效方案，同时，相同的底层模型搭配不同的“脚手架”（如提示工程、工作流）会导致性能显著差异，这揭示了智能体系统设计中工程框架与模型能力同等重要。该工作为推进面向实际生产环境的智能编码代理研发提供了关键的评估工具和深刻洞见。
