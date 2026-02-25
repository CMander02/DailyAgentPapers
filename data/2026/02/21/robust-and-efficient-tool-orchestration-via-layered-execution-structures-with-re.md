---
title: "Robust and Efficient Tool Orchestration via Layered Execution Structures with Reflective Correction"
authors:
  - "Tao Zhe"
  - "Haoyu Wang"
  - "Bo Luo"
  - "Min Wu"
  - "Wei Fan"
  - "Xiao Luo"
  - "Zijun Yao"
  - "Haifeng Chen"
  - "Dongjie Wang"
date: "2026-02-21"
arxiv_id: "2602.18968"
arxiv_url: "https://arxiv.org/abs/2602.18968"
pdf_url: "https://arxiv.org/pdf/2602.18968v1"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "工具使用"
  - "规划"
  - "错误处理与鲁棒性"
  - "执行优化"
relevance_score: 9.0
---

# Robust and Efficient Tool Orchestration via Layered Execution Structures with Reflective Correction

## 原始摘要

Tool invocation is a core capability of agentic systems, yet failures often arise not from individual tool calls but from how multiple tools are organized and executed together. Existing approaches tightly couple tool execution with stepwise language reasoning or explicit planning, leading to brittle behavior and high execution overhead. To overcome these limitations, we revisit tool invocation from the perspective of tool orchestration. Our key insight is that effective orchestration does not require precise dependency graphs or fine-grained planning. Instead, a coarse-grained layer structure suffices to provide global guidance, while execution-time errors can be corrected locally. Specifically, we model tool orchestration as learning a layered execution structure that captures high-level tool dependencies, inducing layer-wise execution through context constraints. To handle execution-time failures, we introduce a schema-aware reflective correction mechanism that detects and repairs errors locally. This design confines errors to individual tool calls and avoids re-planning entire execution trajectories. This structured execution paradigm enables a lightweight and reusable orchestration component for agentic systems. Experimental results show that our approach achieves robust tool execution while reducing execution complexity and overhead. Code will be made publicly available.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于语言模型的智能体系统中，多工具协同调用（Tool Orchestration）的鲁棒性和效率问题。现有方法主要分为两类：一是逐步反应式（如ReAct），缺乏全局结构指导，容易忽略隐式依赖，导致执行链死锁或计算开销过大；二是先规划后执行式（如HuggingGPT），虽然提供高层规划，但对运行时偏差（如模式不匹配、格式错误）非常脆弱，且通常依赖临时重试而非系统性修复。这两种范式均未能同时提供**全局结构感知**和**本地错误恢复**能力，尤其对于上下文有限、恢复能力较弱的小语言模型（SLM）而言，问题更为突出。

论文的核心目标是设计一种既具备全局工具依赖意识，又能弹性应对执行时错误的结构化执行机制，避免耗时的小模型微调。具体挑战包括：1）如何快速推断出捕捉核心依赖关系的粗略执行草图，而无需详尽规划或工具特定规则；2）如何在既定结构下，有效识别执行错误并进行本地修复，防止错误在工具调用链中传播。为此，论文提出了一个基于分层执行结构与反射性校正的框架，通过解耦全局组织与本地执行，实现鲁棒且高效的多工具协同。

### Q2: 有哪些相关研究？

相关工作主要围绕三个方向展开。在**工具学习**方面，早期研究如ToolBench构建了大规模API基准并提出了基于深度优先搜索的多步调用方法，后续工作通过A*搜索剪枝、并行执行或自我反思来提升效率与可靠性，但幻觉和不稳定性问题依然存在。在**规划范式**方面，现有方法可分为两类：一是如ReAct和Reflexion的“反应式方法”，它交错推理与执行，灵活但缺乏全局依赖感知；二是如HuggingGPT和Plan-and-Solve的“先规划后执行”方法，它先生成完整计划，但规划与执行的脱节导致难以应对运行时故障。本文的工作旨在桥接这两种范式。在**高效工具学习与小模型**方面，已有研究通过将工具知识内化到LLM中进行微调（如DTA-Tool、GAP、ToolGen）来提升小模型的编排能力，但这会产生训练成本且难以适应工具集的演变。本文则另辟蹊径，将粗粒度的规划卸载到一个轻量级外部模块，并利用上下文约束执行来减轻现成小模型每一步的推理负担，从而无需微调即可实现高效、鲁棒的工具编排。

### Q3: 论文如何解决这个问题？

该论文通过引入一个分层的执行结构（Layered Execution Structure）与本地反射修正机制（Reflective Correction），来解决多工具调用中因组织与执行不当导致的失败问题。其核心方法是将全局的编排（orchestration）与局部的执行解耦，从而降低执行复杂度并提升鲁棒性。

**核心架构设计**包含三个关键组件：
1. **学习层执行草图（Learn: Layer Execution Sketch）**：模型首先预测每个工具所属的“执行层”，形成一个粗粒度的执行顺序。工具被分配到不同的层（例如第k层），并允许依赖前面层（<k层）的输出，但无需预测精确的依赖边。这一过程通过轻量级神经网络实现：将用户查询和工具文档编码后，经过投影、上下文编码（Transformer Encoder）和有序回归（ordinal regression）输出层分配。这种设计避免了构建完整依赖图的高昂成本，仅提供全局的脚手架。

2. **上下文约束调用（Execute: Context-Constrained Invocation）**：执行时按层顺序进行。在每一层，语言模型（LM）只能看到当前层工具的模式（schema）以及之前层的输出结果。这种约束防止了越层调用，保持了上下文简短，并将多步推理分解为每层的局部决策。执行完成后，模型基于所有观察结果合成最终答案，并强制进行完整性检查。

3. **本地反射与修正（Reflect and Repair: Local Correction）**：为了处理执行时的错误（如参数缺失、类型错误等），论文引入了“模式门（Schema Gate）”和修复机制。模式门在调用前验证参数是否符合工具模式，拒绝无效调用并生成结构化错误报告。对于被拒绝或失败的调用，系统在预算内进行分层修复：先尝试确定性编辑（如删除意外键），若失败则调用LLM进行基于错误信息的修复。修复后的调用重新验证，确保错误被隔离在单个工具调用内，避免污染全局上下文或触发重新规划。

**关键技术**包括：使用有序回归进行层预测以捕捉顺序依赖；通过上下文约束执行限制LM的可见工具集，降低推理负担；以及设计轻量、分级的修复策略，在保证效率的同时提升调用成功率。整体上，该方法将全局规划转化为轻量的结构预测，让小型LM专注于短视界的工具使用，并通过本地化错误处理实现鲁棒且高效的工具编排。

### Q4: 论文做了哪些实验？

论文在 StableToolBench 数据集上进行了全面的实验评估，该数据集包含不同泛化维度（未见指令、未见工具、未见类别）和不同任务复杂度（单工具、类别内多工具、集合内多工具）的场景。实验设置比较了三种执行策略（ReAct、DFSDT 和本文提出的 plan-then-execute 方法），并使用了多种模型作为骨干，包括未进行工具调优的开源模型（如 Qwen2.5-7B、LLaMA-3.1-8B）、工具调优模型（ToolLLaMA-7B）以及闭源模型（GPT-3.5）。评估指标采用 Solvable Pass Rate (SoPR) 和 Solvable Win Rate (SoWR)。

主要实验结果如下：首先，传统方法（ReAct、DFSDT）在未调优模型上表现不佳（如 Qwen2.5-7B 的 DFSDT SoPR 为 12.2%）。其次，本文方法显著提升了未调优模型的性能，将 Qwen2.5-7B 的 SoPR 提升至 49.5%，甚至超过了工具调优的 ToolLLaMA-7B（47.1%）和 GPT-3.5+ReAct 基线。在答案质量评估中，Qwen2.5-7B 结合本文方法在 SoWR 上与工具调优模型表现相当。消融实验表明，执行草图（execution sketch）和修复模块（repair）都是性能提升的关键组件。效率分析显示，本文方法相比 DFSDT 大幅减少了令牌消耗（最高减少 84.8%）和执行步骤（最高减少 69.6%）。此外，模型规模消融实验表明，该方法在 7B 到 1.5B 的模型上都能保持较强性能，仅在 0.5B 模型上出现明显下降。参数敏感性分析则证明层预测器对超参数选择不敏感，性能稳定。

### Q5: 有什么可以进一步探索的点？

本文提出的分层执行结构虽能提升鲁棒性和效率，但其层结构预测的质量仍有改进空间，未来可通过引入轻量级训练信号（如强化学习或对比学习）来优化分层准确性。其次，该方法目前依赖7B参数模型，未来可探索在更小、资源受限的模型上部署，以扩大应用场景。此外，反射纠错机制仅针对单个工具调用进行局部修复，未来可研究跨层错误的协同恢复机制，以处理更复杂的依赖故障。最后，当前框架主要关注工具调用，未来可探索与动态任务规划、多智能体协作的更深层次整合，进一步提升复杂场景下的自适应能力。

### Q6: 总结一下论文的主要内容

这篇论文的核心贡献是提出了一种名为“分层执行结构”的新型工具编排范式，旨在解决智能体系统中多工具调用时存在的脆弱性和高开销问题。其关键创新在于将工具编排建模为学习一个粗粒度的、捕获高层级工具依赖关系的分层结构，并通过上下文约束引导分层执行，而非依赖精确的依赖图或细粒度规划。同时，论文引入了模式感知的反射式校正机制，能在执行时局部检测并修复单个工具调用错误，从而将故障影响范围限制在局部，避免了重新规划整个执行路径的昂贵开销。这种设计将编排逻辑解耦为一个轻量级、可复用的组件，在实验中显著提升了工具执行的鲁棒性，同时降低了执行复杂度与开销。其意义在于为构建高效、可靠的智能体系统提供了一种新的结构化执行范式。
