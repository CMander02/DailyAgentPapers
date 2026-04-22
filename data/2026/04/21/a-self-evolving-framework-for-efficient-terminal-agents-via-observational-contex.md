---
title: "A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression"
authors:
  - "Jincheng Ren"
  - "Siwei Wu"
  - "Yizhi Li"
  - "Kang Zhu"
  - "Shu Xu"
  - "Boyu Feng"
  - "Ruibin Yuan"
  - "Wei Zhang"
  - "Riza Batista-Navarro"
  - "Jian Yang"
  - "Chenghua Lin"
date: "2026-04-21"
arxiv_id: "2604.19572"
arxiv_url: "https://arxiv.org/abs/2604.19572"
pdf_url: "https://arxiv.org/pdf/2604.19572v1"
categories:
  - "cs.CL"
tags:
  - "Terminal Agent"
  - "Context Compression"
  - "Self-Evolving Framework"
  - "Long-Horizon Reasoning"
  - "Token Efficiency"
  - "Agent Architecture"
  - "Benchmark Evaluation"
relevance_score: 8.5
---

# A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression

## 原始摘要

As model capabilities advance, research has increasingly shifted toward long-horizon, multi-turn terminal-centric agentic tasks, where raw environment feedback is often preserved in the interaction history to support future decisions. However, repeatedly retaining such feedback introduces substantial redundancy and causes cumulative token cost to grow quadratically with the number of steps, hindering long-horizon reasoning. Although observation compression can mitigate this issue, the heterogeneity of terminal environments makes heuristic-based or fixed-prompt methods difficult to generalize. We propose TACO, a plug-and-play, self-evolving Terminal Agent Compression framework that automatically discovers and refines compression rules from interaction trajectories for existing terminal agents. Experiments on TerminalBench (TB 1.0 and TB 2.0) and four additional terminal-related benchmarks (i.e., SWE-Bench Lite, CompileBench, DevEval, and CRUST-Bench) show that TACO consistently improves performance across mainstream agent frameworks and strong backbone models. With MiniMax-2.5, it improves performance on most benchmarks while reducing token overhead by around 10%. On TerminalBench, it brings consistent gains of 1%-4% across strong agentic models, and further improves accuracy by around 2%-3% under the same token budget. These results demonstrate the effectiveness and generalization of self-evolving, task-aware compression for terminal agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决终端智能体（Terminal Agent）在处理长周期、多轮次任务时，因环境反馈信息冗余导致的上下文膨胀和推理效率低下的核心问题。研究背景是，随着代码大语言模型的发展，软件工程智能体在终端任务（如代码调试、编译、环境交互）中展现出潜力，但现有方法通常直接将原始终端输出（包含大量冗余日志、重复构建痕迹等）完整保留在交互历史中，以供后续决策参考。这导致累积的令牌成本随步骤数呈二次增长，不仅增加计算开销，还掩盖了关键信号，阻碍了长周期推理。

现有方法的不足主要体现在两方面：一是基于启发式规则或固定提示的静态压缩策略难以泛化，因为终端环境高度异构，压缩模式随仓库、命令和执行状态差异很大，导致效果有限或不稳定；二是基于训练的方法（如SWE-Pruner）虽能过滤无关信息，但需要额外训练且通常针对特定任务设计，适用性受限，无法灵活适应广泛的终端环境。

因此，本文的核心问题是：如何为终端智能体设计一种能自适应不同环境、无需训练、且能持续优化的上下文压缩方法。论文提出TACO框架，通过自动从交互轨迹中发现和精炼压缩规则，并利用全局规则池实现跨任务知识复用，从而在提升任务性能的同时显著降低令牌开销，实现高效的长周期推理。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：终端与代码智能体、上下文压缩方法，以及自进化智能体框架。

在**终端与代码智能体**方面，研究已从代码片段生成转向仓库级和基于终端的软件工程任务，相关评测基准如SWE-bench、Multi-SWE-bench和本文使用的TerminalBench推动了该领域发展。同时，出现了如SWE-Agent、OpenHands等更强的智能体框架和扩展策略。本文工作TACO旨在提升此类终端智能体的效率，与它们是应用与增强的关系。

在**上下文压缩方法**上，现有方法主要依赖截断、人工启发式规则、通用大模型摘要或上下文管理工具。学习型方法如SWE-Pruner虽更具自适应性，但需额外微调且针对SWE任务定制，难以泛化至多样化的终端环境。TACO同样致力于解决终端交互中的上下文冗余问题，但区别在于它提出了一种无需训练、可自动发现和优化压缩规则的自进化机制，具有更好的泛化性和即插即用特性。

在**自进化智能体框架**中，现有工作分为参数更新（如强化学习、微调）和无训练的记忆增强两类。前者计算成本高且存在灾难性遗忘风险；后者（如Memento-Skills、SAGE）通过优化结构化文本构件或保留可复用技能实现进化。TACO属于无训练范式，但其创新点在于将自进化机制**专门应用于终端观察压缩**，动态演化一组结构化压缩规则，从而缓解终端环境中的上下文饱和瓶颈，与此前聚焦于进化行动计划或技能的研究有所不同。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为TACO的即插即用、自演化的终端智能体压缩框架来解决终端环境中观察历史冗余导致令牌成本二次增长的问题。其核心方法是动态地发现和优化压缩规则，而非依赖固定的启发式或提示方法。

整体框架包含三个关键组件：1) **终端输出压缩模块**：在智能体执行的每一步，应用当前任务特定的规则集对原始终端输出进行压缩，但会保留包含明确错误或失败信号的“关键”输出，确保决策所需的关键信息不丢失。2) **任务内规则集演化模块**：在单个任务执行过程中动态更新规则。当遇到未被现有规则覆盖的输出时，会调用大语言模型生成新规则；同时，通过智能体后续行为（如请求完整输出、重复命令）作为隐式反馈，来识别过度压缩的规则并对其进行抑制或替换为更保守的变体。3) **全局规则池演化模块**：作为一个跨任务共享的知识库，存储结构化的压缩规则。规则包含触发模式、保留模式、移除模式等参数，并通过一个固定的规则执行器实例化为具体的过滤行为，从而将自演化约束在一个安全、可重用的规则空间内。

关键技术在于其**双层演化机制**和**基于反馈的规则优化**。在任务开始时，系统会根据任务描述从全局规则池中检索并精炼出最相关的规则来初始化任务特定规则集。在任务执行中，规则会根据覆盖情况和隐式反馈进行增删改。任务完成后，被证明有效的规则及其置信度会被写回全局规则池，并更新其全局置信度和使用计数。全局规则池中的规则通过一个综合了置信度和累计成功应用次数的分数进行排名，以支持后续检索。

创新点主要体现在：**自演化能力**：系统能够从交互轨迹中自动发现和迭代改进压缩规则，适应终端环境的异构性。**即插即用设计**：TACO可以作为适配器集成到不同的终端智能体框架中，无需修改原有智能体核心。**保守且安全的压缩**：通过结构化规则和保留关键输出的设计，在压缩冗余信息的同时，最大程度避免丢失关键信息。**知识积累与共享**：通过全局规则池实现跨任务的压缩知识积累和复用，使得系统性能能够持续提升。实验表明，该框架在多种基准测试上都能在降低令牌开销的同时，提升智能体的任务性能。

### Q4: 论文做了哪些实验？

实验设置方面，论文在TerminalBench（TB 1.0和TB 2.0）以及四个额外的终端相关基准（SWE-Bench Lite、CompileBench、DevEval、CRUST-Bench）上评估了TACO框架。使用了多种骨干大语言模型，包括闭源模型（Claude、GPT、Gemini系列）和开源模型（MiniMax、DeepSeek、GLM、Kimi-K2-Instruct、Nex-N1系列以及多个参数少于400亿的Qwen3系列模型）。并采用两种代表性智能体框架：Terminus-2（用于TB、CompileBench、DevEval和CRUST-Bench）和Mini-SWE-Agent（用于SWE-Bench Lite）。

主要对比方法为未使用TACO压缩的基线智能体。关键数据指标显示，在TB基准上，TACO为强大的智能体模型带来了1%-4%的稳定性能提升。例如，Qwen3-Coder-480B和Qwen3-32B-Instruct在TB 1.0上分别获得1.00和2.88分的提升，在TB 2.0上分别提升1.96和3.56分。在相同token预算下，准确率进一步提升约2%-3%。对于超过2000亿参数的大模型（如Qwen3-Coder-480B、DeepSeek-V3.2），TACO将每步token成本降低约10%，而不会改变平均步数。对于参数少于400亿的小模型，TACO通过增强环境理解使其能执行更多步骤，从而提升了任务成功率，但总token消耗可能增加。

在多个下游基准的迁移实验中，以MiniMax-2.5为骨干模型，TACO在大多数基准上提升了性能，同时减少了token开销（约10%）。例如，在SWE-Bench Lite上准确率从56.30%提升至57.12%，总token从307.61M降至270.53M。消融实验表明，移除TACO的任一进化组件（任务内规则集进化或全局规则池进化）都会导致性能下降，证明了自进化机制的有效性。此外，在固定token预算和pass@k评估中，TACO均一致优于基线。

### Q5: 有什么可以进一步探索的点？

该论文提出的TACO框架在终端智能体观测压缩方面取得了显著效果，但其局限性及未来探索方向可从以下几方面展开：首先，当前压缩规则主要基于历史轨迹自动发现，但缺乏对规则可解释性和安全性的深入验证，未来可引入形式化验证或规则置信度评估机制，避免压缩导致关键信息丢失。其次，框架依赖离线轨迹生成规则，难以适应动态变化的环境，可探索在线自适应压缩机制，结合实时反馈调整规则粒度。此外，实验集中于代码和终端任务，未来需验证在更广泛的交互式环境（如机器人控制、游戏）中的泛化能力。从技术角度看，可结合轻量化神经网络对观测进行语义编码，替代纯规则压缩，以提升对复杂场景的适应性。最后，当前压缩以节省token为主要目标，未来可探索多目标优化，平衡压缩率、推理延迟与任务性能的帕累托最优。

### Q6: 总结一下论文的主要内容

这篇论文提出了TACO，一个即插即用、自演化的终端智能体压缩框架，旨在解决长视野、多轮次终端中心智能体任务中，因完整保留原始环境反馈而导致的令牌成本二次增长和冗余问题。其核心问题是：如何在异构的终端环境中，高效压缩交互历史中的观察信息以支持长期推理，同时避免启发式或固定提示方法的泛化性不足。

方法上，TACO框架能够自动从智能体的交互轨迹中发现并优化压缩规则，为现有的终端智能体提供任务感知的压缩能力，而无需手动设计规则。

主要结论是，在TerminalBench等多个终端相关基准测试上的实验表明，TACO能持续提升主流智能体框架和骨干模型的性能，在显著降低令牌开销（约10%）的同时，提高任务准确率（在相同令牌预算下提升约2%-3%）。这证明了自演化、任务感知的压缩方法对于提升终端智能体效率和泛化能力的有效性与重要意义。
