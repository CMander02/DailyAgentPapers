---
title: "Agent Capsules: Quality-Gated Granularity Control for Multi-Agent LLM Pipelines"
authors:
  - "Aninda Ray"
date: "2026-05-01"
arxiv_id: "2605.00410"
arxiv_url: "https://arxiv.org/abs/2605.00410"
pdf_url: "https://arxiv.org/pdf/2605.00410v1"
github_url: "https://github.com/aray-17/agent-capsules"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "Agent流水线优化"
  - "LLM调用效率"
  - "质量约束"
  - "自适应执行运行时"
  - "Agent压缩"
  - "缓存对齐提示"
  - "拓扑感知上下文注入"
relevance_score: 7.5
---

# Agent Capsules: Quality-Gated Granularity Control for Multi-Agent LLM Pipelines

## 原始摘要

A multi-agent pipeline with N agents typically issues N LLM calls per run. Merging agents into fewer calls (compound execution) promises token savings, but naively merged calls silently degrade quality through tool loss and prompt compression. We present Agent Capsules, an adaptive execution runtime that treats multi-agent pipeline execution as an optimization problem with empirical quality constraints. The runtime instruments coordination overhead per group, scores composition opportunity, selects among three compound execution strategies, and gates every mode switch on rolling-mean output quality. A controlled negative result confirms that injecting more context into a merged call worsens compression rather than relieving it, so the framework's escalation ladder (standard, then two-phase, then sequential) recovers quality by moving toward per-agent dispatch rather than by rewriting merged prompts. On LLM-judged quality, the controller matches a hand-tuned oracle on every measured (model, group, mode) cell: routing compound whenever the oracle would, and reverting to fine whenever quality would fail the floor, without per-model configuration. Against a hand-crafted LangGraph implementation of a 14-agent competitive intelligence pipeline, Agent Capsules uses 51% fewer fine-mode input tokens and 42% fewer compound-mode input tokens, at +0.020 and +0.017 quality respectively. Against a DSPy implementation of a 5-agent due diligence pipeline, the framework uses 19% fewer tokens than uncompiled DSPy at quality parity, and 68% fewer tokens than MIPROv2 at +0.052 quality. Even before compound mode fires, the runtime delivers efficiency through automatic policy resolution, cache-aligned prompts, and topology-aware context injection, matching both hand-tuned and compile-time baselines without training data or per-pipeline engineering.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多智能体LLM管道中的“复合执行问题”。研究背景是，当多智能体管道中每个代理独立运行时，每次都会产生昂贵的LLM调用开销。现有方法如将多个代理合并为单一调用的复合执行，虽然能节省token，但会带来严重问题：合并后的提示词会丢失工具访问能力，且小模型会将多代理指令压缩为浅层响应，导致输出质量无声地下降。现有的多代理框架对这一问题没有任何解决方案，它们将每个代理视为独立调度单元，无法自动进行批量化合并，成本-质量权衡完全依赖人工设计。

本文的核心问题是：何时可以安全地合并代理？当合并破坏了质量时，系统应该如何应对？为了解决这个问题，论文提出了Agent Capsules（AC），一个自适应执行运行时。它通过三个机制实现自动且安全的决策：基于运行时行为信号（协调开销、代理数量、工具调用密度、依赖深度）计算的组合分数来预测合并的安全性；一个质量门控机制，对复合输出进行影子评估并与细粒度基线比较，阻止不安全切换并在质量低于阈值时恢复；以及一个升级阶梯（标准→两阶段→顺序），当低层级策略未能通过质量门控时，逐步转向更多代理独立调用的方向来恢复质量，而不是重写合并提示词。

### Q2: 有哪些相关研究？

### 方法类相关工作
CrewAI、LangGraph、Google ADK、MetaGPT 和 AgentScope 提供了结构化多智能体管道，但缺乏对每组的协调开销进行量化、计算组合分数或基于经验质量阈值进行运行时执行模式切换的机制。Agent Capsules 意在封装这些系统而非替代它们。

DSPy 通过编译期提示优化（如 MIPROv2）减少 token 使用，而 LLMLingua 则压缩单个提示。这些方法聚焦内容优化，而 Agent Capsules 聚焦运行时结构优化，且与它们互补：在 5 智能体尽职调查管道中，相比 DSPy 节省 19% token 且质量持平，相比 MIPROv2 节省 68% token 且质量提升 0.052。

### 应用与调度类相关工作
FrugalGPT 和 RouteLLM 基于查询特征路由到不同模型，Agent Capsules 则基于组行为指纹选择如何调用固定模型，且通过质量门控与基线对比，两者可正交组合。

Orca、vLLM、FlashAttention 和 SGLang 优化单次请求的调度、缓存或注意力机制，在应用层之下工作；Agent Capsules 在应用层之上，减少请求数量与结构而非优化单次执行。

### 训练与编程模型类相关工作
Gorilla 和 ToolBench 训练模型有效使用工具，Agent Capsules 从执行优化角度测量工具调用稳定性。其基于组的编程模型借鉴了 Capsules 并行编程框架的动态可组合执行单元思想。

### Q3: 论文如何解决这个问题？

Agent Capsules通过一个自适应执行运行时（adaptive execution runtime）解决多智能体LLM管线的效率与质量权衡问题，核心是将管线执行建模为带经验质量约束的优化问题。

整体框架基于三层抽象：Agent（原子工作单元，声明角色、系统提示和工具）、Group（具名智能体集合，是控制器观察和适配的基本单元）和Pipeline（顶层容器）。框架通过拓扑分类器将Group内部依赖结构分为线性、扇出、钻石和并行收敛四种类型，并据此选择上下文注入策略，抑制无关的跨智能体上下文传递。

主要模块包括控制器策略对象、复合执行模式梯度和质量门控机制。核心创新点是组合分数（Composition Score），它是一个行为指纹，通过测量Fine模式下协调开销比率、智能体数量、平均工具调用和依赖链深度这四个结构信号的加权线性组合，来判别模型是否适合复合执行。控制器以此分数决定是否从Fine模式切换到复合模式。

执行模式梯度的关键技术包含三种策略：标准复合（合并为一个LLM调用，节省35-87% token）、两阶段复合（保留工具调用，仅合并推理步骤）和序列复合（按序执行独立调用，接近Fine模式质量）。控制器自动根据工具存在性、冗长观察和滚动质量门控选择并逐步升级策略。质量门控通过LLM评判器评估输出质量，在复合执行后计算滚动均值，低于阈值时自动触发模式升级，且包含影子门控和衰减窗口去升级机制。该框架无需训练数据或逐管线工程配置即可匹配手工调优方案。

### Q4: 论文做了哪些实验？

论文进行了多组实验评估Agent Capsules的性能。实验设置包括：在14-agent竞争情报流水线和5-agent尽职调查流水线上，对比手调LangGraph和DSPy（含MIPROv2编译）基线。采用LLM评委（Anthropic使用claude-opus-4-6，OpenAI/Gemini使用gpt-4o）对事实完整性、推理深度和连贯性进行0-1.0评分，检测阈值分别为0.030和0.065。

主要实验包括：1) 执行模式阶梯：在Sonnet上，research组标准模式达0.775，analysis组需sequential模式达0.783，synthesis组标准模式达0.833，均通过0.75质量门限。2) 自动输出引导：Sonnet节省63%输出token且质量中性，Gemini-flash仅节省3%避免质量下降0.160。3) 上下文注入策略：predecessor_only策略在长链中使Haiku质量+0.089。4) 预算结构化提示：Haiku质量+0.209，Gemini-flash+0.404。5) 缓存对齐提示：使Sonnet在尽职调查和代码审查流水线质量分别+0.044和+0.061。最终框架相较LangGraph节省51% fine模式输入token和42% compound模式输入token，质量分别+0.020和+0.017；相较DSPy节省19% token且质量持平，相较MIPROv2节省68% token且质量+0.052。

### Q5: 有什么可以进一步探索的点？

论文的主要局限在于质量门控机制依赖滚动平均输出质量，这可能对突发的质量波动反应滞后，且评分标准仍需人工设计。未来可探索以下方向：1) 引入动态质量阈值，利用贝叶斯方法或在线学习自适应调整门限，避免固定阈值在分布外场景失效；2) 研究跨组依赖的联合优化，当前独立控制每个CompoundCapsule，但实际多智能体流水线的信息传递可能产生跨组效应，可尝试用图神经网络建模全局质量-成本帕累托前沿；3) 改进工具保留机制，论文指出合并调用会导致工具遗漏，可设计工具感知的提示压缩算法（如结构化摘要或功能保留子图提取）；4) 探索强化学习框架，使控制器能从历史执行轨迹中自动学习模式切换策略，替代当前的手动质量评分规则。此外，当前评估局限于LLM评判质量，未来需在真实用户任务中验证质量保真度，并考虑多模态场景下的质量约束。

### Q6: 总结一下论文的主要内容

这篇论文提出了Agent Capsules（AC），一种用于多智能体LLM管道的自适应执行框架，旨在解决智能体合并（复合执行）带来的质量与成本权衡问题。当前多智能体管道运行中，每个智能体单独调用LLM（细粒度模式）开销大，而简单合并多个智能体为一个调用虽能节省token，但会导致工具丢失和提示压缩，严重降低输出质量。AC将此视为带经验性质量约束的优化问题：通过运行时测量的协调开销、智能体数量等行为信号计算组合分数，预测合并安全性；并引入质量门控机制，以滚动平均质量评估复合输出，当质量低于阈值时触发升级策略（标准→两阶段→顺序），逐步向每个智能体独立调度恢复质量，而非重写合并提示。在14智能体竞争情报管道和5智能体尽职调查管道上的实验表明，AC在匹配或超越手工调优和编译基线质量的同时，分别减少了51%和19%的细粒度输入token，复合模式下也节省42%和68%的token。核心贡献在于实现了无需手动配置或训练数据的自动、安全的多智能体执行粒度控制，为平衡成本与质量提供了实用方案。
