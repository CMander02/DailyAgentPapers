---
title: "Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents"
authors:
  - "Tianshi Xu"
  - "Huifeng Wen"
  - "Meng Li"
date: "2026-05-21"
arxiv_id: "2605.22166"
arxiv_url: "https://arxiv.org/abs/2605.22166"
pdf_url: "https://arxiv.org/pdf/2605.22166v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Runtime Harness"
  - "Deterministic Environment"
  - "Agent-Environment Interface"
  - "Model-Agnostic Adaptation"
  - "τ-bench"
  - "AgentBench"
  - "Qwen3-4B-Instruct"
relevance_score: 9.0
---

# Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents

## 原始摘要

LLM agents are shaped not only by their language models, but also by the runtime harness that mediates observation, tool use, action execution, feedback interpretation, and trajectory control. While existing agent adaptation methods mainly update model parameters, many failures in deterministic, rule-governed domains stem from mismatches at the model--environment interface. We propose Life-Harness, a lifecycle-aware runtime harness that improves frozen LLM agents without changing model weights or evaluation environments. Life-Harness evolves from training trajectories by converting recurring interaction failures into reusable interventions across environment contracts, procedural skills, action realization, and trajectory regulation, and remains fixed during held-out evaluation. On seven deterministic environments from $τ$-bench, $τ^2$-bench, and AgentBench, Life-Harness improves 116 out of 126 model--environment settings across 18 model backbones, with an average relative improvement of 88.5%. Harnesses evolved only from Qwen3-4B-Instruct trajectories transfer to 17 other models, showing that Life-Harness captures reusable environment-side structure rather than model-specific behavior. These results position runtime interface adaptation as a complementary alternative to model-centric agent training. Code is available at GitHub.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决确定性规则驱动领域中，LLM代理失败的核心原因并非模型能力不足，而是模型与环境之间运行时接口（runtime harness）不匹配的问题。现有研究主要聚焦于模型自身的参数调整（如微调、强化学习、偏好优化等），这些方法将领域特定行为隐式地嵌入模型参数中，但在面对工具模式、API合约、反馈规则等存在于模型之外的确定性环境结构时，模型仍因接口层面的错误（如观测组织差、工具理解错、动作不可执行、反馈未被转化为恢复信号、轨迹陷入重复循环）而表现不佳。例如，模型在数学推理基准上得分高，却在具身交互任务中失败。因此，本文提出了一种名为Life-Harness的生命周期感知运行时系统，它不改变模型权重或评估环境，而是通过从训练轨迹中诊断并转化重复交互失败为可复用的干预措施，来适配模型与环境的接口层（包括环境合约、程序技能、动作实现和轨迹调控）。核心目标是证明：通过演化稳定的运行时接口，而非修改模型参数，可以显著提升冻结LLM代理在未见任务和新模型上的性能。

### Q2: 有哪些相关研究？

相关研究可归纳为三类。第一类是**运行时系统优化（Harness Optimization）**，包括AutoTTS、Workspace Optimization、Continual Harness、HARBOR、Meta-Harness和AHE等。这些工作与本文共享“冻结模型、优化外围系统”的前提，但差异显著：Meta-Harness和AHE聚焦于编程智能体场景下的自动化工程工具搜索或持续编辑，而本文面向家庭交互、网页购物、数据库任务等确定性领域，将运行时系统视为结构化接口，依据智能体交互生命周期组织适应，将训练轨迹中的失败模式映射为环境契约、程序技能、动作实现和轨迹调控四类固定干预，并在保留的测试集上评估。第二类是**提示适应方法（Prompt Adaptation Methods）**，如OPRO、ProTeGi、TextGrad、GEPA等，它们通过改写指令或示例来优化模型行为。本文与之互补：提示方法主要优化模型面对的文本，而本文适应更广泛的运行时接口，既包括提示相关的契约，也包括动作验证、反馈恢复、轨迹调控等执行机制。第三类是**模型侧适应（Model-side Adaptation）**，通过指令微调、工具微调、强化学习、蒸馏等方法改进模型自身。本文提供了一个互补范式：不改变模型权重，而是适应模型观察和执行所依赖的运行时接口。

### Q3: 论文如何解决这个问题？

Life-Harness通过四个生命周期感知的运行时层，在不修改模型权重或评估环境的前提下，自适应调整模型与环境的接口以解决确定性智能体的交互失败问题。

核心方法基于对冻结模型（如Qwen3-4B-Instruct）在训练任务上的失败轨迹分类，识别出四大失败模式：动作实现失败（意图无法被环境执行）、环境契约不匹配（动作符合语法但违反工具调用协议）、轨迹退化（重复或停滞）以及通用推理失败。基于此，Life-Harness设计了四个互补的干预层：

1. **环境契约层**（交互前）：将工具使用规则、策略约束和常见陷阱转化为增强的契约描述，替换原始契约提供给模型。
2. **程序化技能层**（任务条件化阶段）：从训练轨迹中蒸馏技能库，基于任务描述（如BM25）检索相关技能，将其插入系统提示提供非参决策引导。
3. **动作实现层**（模型输出后、环境执行前）：利用工具模式、参数约束等确定性环境证据，验证动作可行性并标准化接口错误，阻止必然会失败的动作。
4. **轨迹调控层**（环境反馈后）：监控轨迹的重复、停滞或预算耗尽模式，触发软恢复或强纠正指令。

这些层通过迭代演化机制从训练轨迹中自动生成：用代码代理分析交互轨迹，识别新的失败模式并更新各层规则，同时检测回归情况。整个框架保持模型和评估环境不变，仅在运行时调整接口，从而在18个模型骨干的126个设置中实现88.5%的平均相对改进。

### Q4: 论文做了哪些实验？

论文在三个基准套件（τ-bench、τ^2-bench 和 AgentBench）上进行了全面实验，涵盖 7 个任务场景：Airline、Retail、Telecom、ALFWorld、WebShop、OS 和 DBBench。实验设置上，使用 Qwen3-4B-Instruct 作为源模型演化运行时框架，然后在 18 个不同模型（包括 Qwen、Llama、xLAM 系列）上评估，温度设为 0.0，τ-bench 和 τ^2-bench 报告单次成功率 Pass@1 和三次全部成功的 Pass^3 指标，AgentBench 采用 Pass@1。

主要结果：Life-Harness 在 126 个模型-环境设置中改进了 116 个，平均相对提升 88.5%。具体地，AgentBench 上 ALFWorld 从 41.1% 提升至 75.7%（+84%），WebShop 从 31.4% 升至 44.0%（+40%）；τ-bench 的 Airline 任务 Pass@1 从 49.7% 升至 62.6%（+26%）；τ^2-bench 的 Telecom 任务 Pass@1 从 55.3% 升至 69.0%（+25%）。与仅提示演化相比，Life-Harness 平均相对提升 120%。消融实验显示所有四个生命周期层均不可或缺，且专用工具使用训练后应用框架仍能提升 6.8-28.9 个百分点。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在对确定性、规则驱动环境的依赖。作者明确指出，在完全开放式的智能体任务中，由于任务目标、工具接口和成功标准多变，难以构建稳定的运行时接口和可跨任务泛化的适配机制。未来可以探索将生命周期感知的运行时适配与在线学习结合，在开放环境中动态识别并记忆反复出现的交互失败模式。一个可能的改进思路是引入元学习框架，让适配器学会从少量交互示例中快速提取环境契约的隐含约束，从而在未见过的任务上也能生成有效的干预策略。另外，当前方法完全冻结模型参数，未来可以尝试极轻量级的参数微调（如LoRA）与运行时适配的互补组合，在不牺牲泛化性的前提下解决需要模型知识迁移的复杂边缘情况。最后，扩展评估环境到多轮对话和物理世界模拟等非结构化场景，检验"接口适应而非模型适应"的假设是否仍然成立，将是重要的下一步。

### Q6: 总结一下论文的主要内容

该论文针对确定性规则领域中大型语言模型（LLM）代理的故障问题，提出了一种名为Life-Harness的运行时机制适配方法。核心贡献在于，不同于传统方法更新模型参数，该方法在不改变模型权重或评估环境的前提下，从训练轨迹中学习并转化重复出现的交互失败为可复用的干预措施，涵盖环境契约、程序性技能、动作实现和轨迹调控四个方面。在来自τ-bench、τ²-bench和AgentBench的七个确定性环境及18种模型骨干上的实验表明，Life-Harness在126个模型-环境设置中改进了116个，平均相对提升达88.5%。更重要的是，仅从Qwen3-4B-Instruct轨迹演化出的机制可迁移至其他17种模型，证明其捕获的是可复用的环境端结构。结论有力地表明，运行时接口适配可作为模型中心化代理训练的有效补充。
