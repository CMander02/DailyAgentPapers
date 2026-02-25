---
title: "Implicit Intelligence -- Evaluating Agents on What Users Don't Say"
authors:
  - "Ved Sirdeshmukh"
  - "Marc Wetter"
date: "2026-02-23"
arxiv_id: "2602.20424"
arxiv_url: "https://arxiv.org/abs/2602.20424"
pdf_url: "https://arxiv.org/pdf/2602.20424v1"
categories:
  - "cs.AI"
tags:
  - "Agent Evaluation"
  - "Agent Benchmark"
  - "Implicit Reasoning"
  - "Contextual Understanding"
  - "Goal-Oriented Agents"
  - "Agent Simulation"
  - "Agentic AI"
relevance_score: 8.0
---

# Implicit Intelligence -- Evaluating Agents on What Users Don't Say

## 原始摘要

Real-world requests to AI agents are fundamentally underspecified. Natural human communication relies on shared context and unstated constraints that speakers expect listeners to infer. Current agentic benchmarks test explicit instruction-following but fail to evaluate whether agents can reason about implicit requirements spanning accessibility needs, privacy boundaries, catastrophic risks, and contextual constraints. We present Implicit Intelligence, an evaluation framework testing whether AI agents can move beyond prompt-following to become genuine goal-fulfillers, paired with Agent-as-a-World (AaW), a harness where interactive worlds are defined in human-readable YAML files and simulated by language models. Our scenarios feature apparent simplicity in user requests, hidden complexity in correct solutions, and discoverability of constraints through environmental exploration. Evaluating 16 frontier and open-weight models across 205 scenarios, we find that even the best-performing model achieves only 48.3% scenario pass rate, revealing substantial room for improvement in bridging the gap between literal instruction-following and human-like contextual reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI智能体在理解人类自然语言中隐含意图和未明说约束方面的核心能力缺失问题。研究背景在于，现实世界中用户对AI的请求本质上是“未充分说明的”，人类日常交流高度依赖共享语境和心照不宣的约束，听话者需要主动推断这些隐含信息。然而，现有智能体评测基准主要关注“显式指令遵循”，即测试智能体是否能够精确执行任务描述中已完全明确说明的步骤，例如导航网站或编写代码。这种评测方式存在严重不足：它假设任务的所有真相都已完全指定在描述中，成功标准仅仅是“按所说的做”，而无需推理“用户本应要求什么”。这导致了评测方式与用户实际沟通模式之间的错位，使得当前智能体缺乏对未言明的需求（如可访问性需求、隐私边界、灾难性风险防范和语境约束）进行推理的能力。

因此，本文要解决的核心问题是：如何评估并推动AI智能体超越字面的指令遵循，发展出“隐性智能”——即识别、推理并满足用户期望但从未明确陈述的那些需求的能力。为此，论文提出了“隐性智能”评测框架和配套的“世界即智能体”模拟工具，旨在系统性地测评智能体在隐含推理、灾难性风险规避、隐私与安全以及可访问性这四大关键类别上的表现，从而弥合字面指令执行与类人语境推理之间的鸿沟。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测基准、环境模拟方法，以及安全与对齐研究。

在**评测基准**方面，已有大量工作评估智能体的能力。早期研究如SWE-bench、WebArena和ToolBench专注于特定领域（软件工程、网页交互、API使用）。近期基准如AgentBench、GAIA、Tau-bench和EIFBENCH则旨在评估通用智能体在多领域、多模态推理和复杂工具使用等方面的表现。然而，本文指出，当前前沿模型在这些显式任务完成度评测上的性能已趋饱和，而本文提出的“隐性智能”框架则专注于评估智能体对未言明约束（如可访问性需求、隐私边界）的推理能力，弥补了现有基准在评估隐性需求方面的空白。

在**环境模拟方法**上，传统基准依赖于手工构建的、具有确定性状态转换的模拟器。近期研究探索使用语言模型作为环境模拟器，例如Li等人的工作以及SimuRA框架，它们用语言模型生成环境反馈或模拟世界模型以进行规划。本文的“Agent-as-a-World”范式与此相关，但侧重点不同：本文主要利用语言模型模拟交互世界来服务于**评测**，特别是针对隐性推理的评估场景，而非用于训练或规划。

在**安全与对齐研究**方面，已有工作关注目标误指定和规范博弈等问题，即智能体以违背人类意图的方式优化既定目标。近期框架如MI9和AURA提出了监控和评估自主性风险的方法。本文的工作与此互补，通过引入一个评估框架，使对齐失败（如灾难性风险或隐私侵犯）在现实的智能体场景中变得可直接测量，从而将安全风险具体化为可评测的隐性约束。

### Q3: 论文如何解决这个问题？

论文通过构建“隐式智能”评估框架和“世界即代理”模拟平台来解决现有智能体基准测试无法衡量其对未言明需求推理能力的问题。

核心方法是创建一个能够系统化测试智能体在隐含约束下进行上下文推理的评估体系。整体框架包含两大核心组件：一是定义了四类隐式需求（上下文目标、灾难性风险、隐私边界、可访问性需求）的评估分类法；二是“世界即代理”这一基于语言模型的通用模拟器，用于创建和运行交互式测试场景。

在架构设计上，“世界即代理”采用声明式YAML文件来定义场景，包含五个主要模块：元数据（场景ID、分类、用户提示）、世界上下文（时间、地点、用户特征等环境因素）、实体（对象、应用及其状态和可用操作）、执行规则（对智能体隐藏、但支配世界行为的约束逻辑）以及评估标准（明确的通过条件）。一个关键创新点是使用一个独立的“世界模型”语言模型作为模拟器，它严格依据YAML规范来执行动作、更新状态并返回预定义的响应，确保了模拟的确定性和一致性，避免了主观偏差。

关键技术在于将复杂的、富含隐含约束的交互环境构建，从传统需要大量工程编码的领域特定模拟器，转变为由语言模型驱动的、可快速迭代的声明式规范。这使得研究者能够高效创建大量测试场景，这些场景表面请求简单，但正确解决方案背后隐藏着复杂性，且约束条件需要通过环境探索来发现。评估流程是回合制的：主智能体接收用户提示和实体描述（不含执行规则），通过一系列动作与环境交互，由世界模型执行并反馈，最终由评估模型根据既定标准判断其是否成功推断并满足了未言明的目标。这种设计首次在保持环境丰富性和交互性的同时，实现了对智能体“隐式智能”——即超越字面指令遵循、实现真实目标满足能力——的大规模、系统性评估。

### Q4: 论文做了哪些实验？

论文在提出的“隐式智能”评估框架和“Agent-as-a-World”模拟环境中，对16个前沿和开源模型进行了系统性实验。实验设置方面，研究者使用人类可读的YAML文件定义交互世界，并由语言模型（最终选定一致性达98.6%的Claude Opus 4.5作为固定世界模型）进行模拟，构建了205个场景。这些场景的特点是用户请求表面简单，但正确解决方案隐含复杂性，且约束条件需通过环境探索来发现。

数据集与基准测试即论文提出的“隐式智能”基准，包含205个场景，涵盖四大隐式需求类别：可访问性需求、隐私边界、灾难性风险和上下文约束。

对比方法涵盖了来自OpenAI（如GPT-4.1, GPT-5, GPT-5.1, GPT-5.2, GPT-5.2-pro）、Anthropic（Claude Sonnet 4.5, Claude Opus 4.5）、Google（Gemini 3 Flash, Gemini 3 Pro）的主要提供商模型以及多个领先的开源权重模型（如DeepSeek V3p1/R1、Llama 4系列、GPT-OSS系列、Gemma 3n E4B）。

主要结果通过场景通过率（SPR）和标准化场景得分（NSS）等关键指标呈现。所有模型中表现最佳的GPT-5.2-pro的SPR也仅为48.3%，表明超过一半的场景未能满足所有隐式需求。各类别分析显示，模型在不同隐式需求上表现各异：例如，Claude Opus 4.5在识别潜在有害操作（灾难性风险）方面表现出色，而GPT-5.2-pro在隐私敏感场景中领先。开源模型整体表现落后，最好的开源模型DeepSeek V3p1（SPR 27.3%）与顶尖模型相差21个百分点，且在灾难性风险规避上尤为薄弱。研究还发现模型性能演进并非单调，例如GPT-5优于其前代和后继版本。对失败模式的分析揭示了三大主要原因：环境探索不足、功能配置不完整以及状态保存不充分。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度拓展。首先，评估场景的构建基于作者视角，未能涵盖跨文化、年龄和技术背景的多样化隐性需求，未来可引入更广泛的用户研究数据，构建更具包容性和代表性的场景库。其次，当前框架假设单轮交互，禁止智能体主动澄清模糊需求，这虽符合某些自动化场景，但限制了智能体在复杂情境下的适应性；未来可设计动态评估模块，将“识别何时需要澄清并恰当提问”作为独立能力进行测评，从而更全面地衡量智能体的协作智能。此外，尽管Agent-as-a-World架构支持通过YAML扩展动作空间，但当前仅覆盖约300个iOS原生动作，未能纳入第三方应用的隐性规范；未来可推动社区协作，构建开放可扩展的场景与动作库，以更好地模拟真实世界的复杂性。从方法学角度看，论文依赖LLM作为世界模型，虽强调其确定性执行角色，但仍可能存在模型特定偏差；未来可探索多模型验证机制，或引入符号逻辑与LLM结合的混合仿真环境，以提升评估的鲁棒性。最后，基准的时效性挑战（如iOS功能迭代）要求建立动态更新机制，或许可结合实时数据采集与自动化场景生成，确保评估持续反映现实演变。这些方向共同指向一个核心目标：推动智能体从“指令跟随”迈向真正理解并满足人类意图的“目标实现者”。

### Q6: 总结一下论文的主要内容

这篇论文提出了“隐性智能”评估框架，旨在解决AI智能体在现实交互中面临的挑战：用户请求往往隐含未明说的约束和上下文信息。当前基准主要测试显式指令跟随，但忽略了智能体对可访问性需求、隐私边界、灾难性风险和情境约束等隐性要求的推理能力。

论文的核心贡献是构建了“Agent-as-a-World”测试平台，通过人类可读的YAML文件定义交互世界，并由语言模型模拟环境。该框架设计了表面简单、实则包含隐藏复杂性的用户请求场景，要求智能体通过环境探索来发现约束条件，从而评估其是否真正实现目标完成而非简单遵循提示。

实验评估了16个前沿和开源模型在205个场景中的表现，发现即使最佳模型场景通过率也仅为48.3%。主要结论表明，当前AI智能体在从字面指令跟随转向类人情境推理方面仍有巨大提升空间，凸显了开发能理解隐性需求智能体的重要性。
