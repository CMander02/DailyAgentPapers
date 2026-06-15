---
title: "HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry"
authors:
  - "Tingyang Chen"
  - "Shuo Lu"
  - "Kang Zhao"
  - "Weicheng Meng"
  - "Hanlin Teng"
  - "Tianhao Li"
  - "Chao Li"
  - "Xule Liu"
  - "Jian Liang"
  - "Zhizhong Zhang"
  - "Yuan Xie"
  - "Heng Qu"
  - "Kun Shao"
  - "Jian Luan"
date: "2026-06-12"
arxiv_id: "2606.14249"
arxiv_url: "https://arxiv.org/abs/2606.14249"
pdf_url: "https://arxiv.org/pdf/2606.14249v1"
categories:
  - "cs.AI"
tags:
  - "Agent Harness"
  - "Composable Agent Architecture"
  - "Multi-Agent Evolution"
  - "Trace-Driven Adaptation"
  - "Runtime Interface Optimization"
  - "Agent Benchmarks"
relevance_score: 9.5
---

# HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry

## 原始摘要

AI agent performance depends critically on the runtime harness, comprising the prompts, tools, memory, and control flow that mediate how a model observes, reasons, and acts. Yet today's harnesses remain largely hand-crafted and static: each new model or task still demands bespoke scaffolding, and the rich traces produced during execution are rarely distilled back into systematic improvement. We introduce HarnessX, a foundry for composable, adaptive, and evolvable agent harnesses. HarnessX assembles typed harness primitives via a substitution algebra, adapts them through AEGIS, a trace-driven multi-agent evolution engine grounded in an operational mirror between symbolic adaptation and reinforcement learning, and closes the harness-model loop by turning trajectories into both harness updates and model training signal. Across five benchmarks (ALFWorld, GAIA, WebShop, tau^3-Bench, and SWE-bench Verified), HarnessX yields an average gain of +14.5% (up to +44.0%), with gains largest where baselines are lowest. These results suggest that agent progress need not come from model scaling alone: composing and evolving runtime interfaces from execution feedback is an actionable and complementary lever. The complete codebase will be open-sourced in a future release.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI代理系统在运行时“支架”（harness）设计上的根本性缺陷。研究背景是，现代AI代理的性能不仅依赖于底层模型，更取决于其运行时支架（包括提示、工具、记忆和控制流）如何协调模型的观察、推理和行动。然而，现有方法存在三大不足：第一，支架是手工制作且静态的，当模型版本、工具或任务领域发生变化时，需要重新定制，缺乏基于经验自动改进的机制；第二，支架架构混杂，将提示模板、工具封装、重试策略和记忆等功能耦合在相同代码路径中，导致组件间相互影响，难以跨领域重用；第三，支架工程与模型训练完全独立，执行过程中产生的丰富轨迹数据被丢弃，无法用于系统性的改进。因此，本文要解决的核心问题是：如何将支架从静态、手工的附属物，转变为可与模型共同组合、自适应演化的一等对象。为此，作者引入了HarnessX，一个可组合、自适应且可演化的支架铸造厂，通过替代代数组装类型化的支架原语，利用基于轨迹的多智能体演化引擎AEGIS进行自适应，并闭环地将执行轨迹反馈到支架更新和模型训练中，从而在多个基准测试上实现了平均+14.5%的性能提升。

### Q2: 有哪些相关研究？

**方法类相关工作**：LangChain、LlamaIndex等提供基础构建模块但不支持整体编排；LangGraph、AutoGen等用状态图或角色模型实现可复用模式，但固定了控制流，难以跨任务迁移；DSPy、OPRO等将提示优化视为黑箱问题，但未涉及工具、记忆等系统级组件。

**评测与认知类**：SICA直接优化智能体源码；AHE、Life-Harness强调可观测性与源码重写，但缺乏统一理论框架。HarnessX的不同在于：它通过代入代数实现类型化组合，利用AEGIS引擎将运行时轨迹映射为RL奖励信号进行多轮自适应，并首次实现“编排-模型”闭环训练。

**前沿探索类**：Claude Code的动态工作流虽能生成任务脚本，但仅限单会话，无跨会话优化。HarnessX的进化引擎结合共享回放缓冲区与病理检测，在五个基准测试（如ALFWorld、SWE-bench）平均提升14.5%，尤其在基线弱的场景增益达44%，证明了从执行反馈编排运行接口是独立于模型规模的有效杠杆。

### Q3: 论文如何解决这个问题？

HarnessX通过三个核心创新解决了AI Agent运行时框架（harness）的手工构建与静态固化问题。首先，它提出了**可组合的Harness架构**：将harness定义为模型配置和框架配置的元组，其中框架配置由事件钩子索引的处理器列表和共享资源插槽组成。每个处理器是一个类型化原子组件，遵循统一的异步接口，通过类型安全的替换代数实现组合——处理器可以像乐高积木一样在八个预定义的生命周期钩子点插入、替换或移除，而不会破坏整体类型正确性。这一设计将harness暴露为一等公民，奠定了程序化演化的基础。

其次，**AEGIS多智能体演化引擎**将harness演化映射为符号空间的强化学习过程：harness配置视为状态、类型化编辑视为动作、执行轨迹与验证器分数构成反馈。AEGIS采用四阶段流水线（消化器、规划器、演化器、评审器），由同一个元智能体选择性调用。消化器压缩原始轨迹为结构化摘要，规划器构建跨越增量与结构性变化的适应景观，演化器生成类型安全的构建操作，评审器与确定性门控层联合防御奖励黑客与灾难性遗忘。这使harness能从执行反馈中自动改进。

最后，**框架-模型协同演化**打破单一维度天花板：系统维护共享重放缓冲区，同时驱动harness演化（AEGIS）与模型参数更新（跨框架GRPO）。模型在新演化出的框架下训练，框架为模型提供更优的执行环境，两者在同一迭代周期内互促优化。实验表明，这种三管齐下的方法在五个基准测试上平均提升14.5%，最高达44%，且对弱基线的改善最为显著，证明框架组成与演化与模型规模扩张同等重要。

### Q4: 论文做了哪些实验？

论文在五个基准测试上进行了实验，包括ALFWorld、GAIA、WebShop、tau³-Bench和SWE-bench Verified。实验设置主要评估了HarnessX框架中可组合、自适应和可进化的代理运行环境组件的效果。核心方法是AEGIS引擎，这是一个基于迹线的多智能体进化引擎，通过符号适应与强化学习之间的操作镜像来驱动运行环境自适应。

对比方法未明确列出，但从结果分析应是针对各基准的基线方法。主要结果显示，HarnessX在所有基准上平均提升了+14.5%的性能，最高提升达+44.0%，且增益最大的场景正是基线表现最差的场景。这表明HarnessX特别擅长弥补薄弱代理的不足。

关键数据指标包括：在各基准测试上的绝对性能提升百分比，以及平均增益+14.5%和最大增益+44.0%。实验通过将运行过程中的迹线转化为运行环境更新和模型训练信号，闭环了运行环境与模型之间的交互，从而实现了显著的性能改善。

### Q5: 有什么可以进一步探索的点？

论文提出的HarnessX框架展示了通过组合和进化运行时接口提升AI Agent性能的巨大潜力，但仍存在几个关键局限和可探索的方向。首先，当前AEGIS每次只提出一个离散的结构编辑，进化步长小且可能陷入局部最优。未来可以探索并行编辑或多目标进化策略，结合贝叶斯优化来更高效地搜索复杂的harness空间。其次，跨harness GRPO虽然新颖，但其依赖固定验证器（verifier），在开放域任务中设计通用、鲁棒的验证器本身就是一个悬而未决的难题，弱验证器会限制进化信号的质量。此外，共享经验回放缓冲区的FIFO策略可能过早丢弃含有重要失败经验的早期轨迹。一个改进思路是引入基于轨迹多样性或模型不确定性的优先级回放机制。最后，虽然论文提到co-evolution打破了单一改进的天花板，但硬件和计算成本会显著增加，未来需要研究如何通过异步更新、知识蒸馏或模型剪枝来平衡性能增益与开销，使其在资源受限的场景下实用化。

### Q6: 总结一下论文的主要内容

该论文提出HarnessX，一个可组合、自适应、可演化的智能体运行时框架生成系统。当前智能体框架存在三大问题：手工构建且静态、架构耦合、框架工程与模型训练脱节。HarnessX将框架视为一等对象，通过类型化的处理器和替换代数实现组合，利用基于轨迹的多智能体演化引擎AEGIS进行自适应，并建立框架-模型协同进化机制。在ALFWorld、GAIA等五个基准测试中，HarnessX平均提升14.5%（最高44.0%），且提升幅度与基线性能成反比。结果表明，智能体进步不仅依赖模型规模扩展，通过执行反馈来组合和演化运行时接口同样有效且互补。
