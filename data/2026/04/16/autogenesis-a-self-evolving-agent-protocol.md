---
title: "Autogenesis: A Self-Evolving Agent Protocol"
authors:
  - "Wentao Zhang"
date: "2026-04-16"
arxiv_id: "2604.15034"
arxiv_url: "https://arxiv.org/abs/2604.15034"
pdf_url: "https://arxiv.org/pdf/2604.15034v1"
categories:
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Multi-Agent Systems"
  - "Agent Protocol"
  - "Self-Improvement"
  - "Tool Use"
  - "Long-Horizon Planning"
  - "Benchmark Evaluation"
relevance_score: 8.5
---

# Autogenesis: A Self-Evolving Agent Protocol

## 原始摘要

Recent advances in LLM based agent systems have shown promise in tackling complex, long horizon tasks. However, existing agent protocols (e.g., A2A and MCP) under specify cross entity lifecycle and context management, version tracking, and evolution safe update interfaces, which encourages monolithic compositions and brittle glue code. We introduce \textbf{\textsc{Autogenesis Protocol (AGP)}}, a self evolution protocol that decouples what evolves from how evolution occurs. Its Resource Substrate Protocol Layer (RSPL) models prompts, agents, tools, environments, and memory as protocol registered resources\footnote{Unless otherwise specified, resources refer to instances of the five RSPL entity types: \emph{prompt}, \emph{agent}, \emph{tool}, \emph{environment}, \emph{memory} with agent \emph{outputs}.} with explicit state, lifecycle, and versioned interfaces. Its Self Evolution Protocol Layer (SEPL) specifies a closed loop operator interface for proposing, assessing, and committing improvements with auditable lineage and rollback. Building on \textbf{\textsc{AGP}}, we present \textbf{\textsc{Autogenesis System (AGS)}}, a self-evolving multi-agent system that dynamically instantiates, retrieves, and refines protocol-registered resources during execution. We evaluate \textbf{\textsc{AGS}} on multiple challenging benchmarks that require long horizon planning and tool use across heterogeneous resources. The results demonstrate consistent improvements over strong baselines, supporting the effectiveness of agent resource management and closed loop self evolution.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的智能体系统在实现**自主进化（self-evolution）** 时所面临的核心架构与标准化缺失问题。

**研究背景**：随着LLM智能体系统在处理复杂、长周期任务上展现出潜力，让智能体具备根据环境反馈自动调整策略、优化指令和更新工具的“自我进化”能力，已成为实现鲁棒自主性的关键方向。然而，当前的实现方式往往是零散和临时的。

**现有方法的不足**：论文指出，现有的智能体协议（如A2A和MCP）主要专注于解决**连接性**问题（如模型-工具调用或智能体间通信），但它们**严重缺乏对进化过程至关重要的原生支持**。具体不足体现在：1) **生命周期与状态管理缺失**：这些协议未明确定义实体（如提示词、工具）的创建、更新、销毁等生命周期和状态，导致进化过程难以安全实施；2) **版本追踪与审计能力不足**：缺乏版本控制和回滚机制，使得错误的更新可能引发不可恢复的系统故障；3) **架构耦合与脆弱性**：开发者被迫编写脆弱的“胶水代码”，导致系统趋于单体化、难以维护，且进化过程既不可组合也难审计。

**本文要解决的核心问题**：为了弥合从“连接”到“进化”的鸿沟，论文提出需要一种全新的协议，其核心是**将“进化什么”（资源）与“如何进化”（过程）进行解耦**，并系统性地解决三个关键问题：1) **解耦问题**：将提示、智能体、工具、环境、记忆等资源抽象为可独立管理的标准化实体，而非与核心逻辑紧耦合的代码块；2) **安全与可审计性问题**：引入严格的版本控制和回滚机制，确保每一步进化都可追溯、可逆转；3) **形式化问题**：定义一套标准化操作符来严格管控进化流程，将启发式的文本修改转变为严谨的控制循环。为此，论文引入了**Autogenesis协议（AGP）** 及其系统实现，旨在为下一代具备持续自主适应能力的智能体系统提供一个基础性的标准化范式。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、协议类和优化类。

在方法类研究中，现有的大语言模型（LLM）智能体系统通常将提示、工具和内存作为紧密耦合的内部组件嵌入，工具被视为固定的功能模块，限制了系统的复用和适应性演化。本文提出的AGP协议则将它们建模为具有明确接口和状态的协议注册资源，支持动态实例化和受控的演化。

在协议类研究中，Anthropic的模型上下文协议（MCP）和谷歌的智能体间（A2A）协议等，主要致力于标准化模型与工具交互以及智能体间通信的互操作性层面。然而，这些协议侧重于调用和消息传递的“如何交互”，并未定义资源生命周期管理、版本追踪或状态变更约束等机制。本文的AGP协议通过其资源基底协议层（RSPL）明确解决了这些不足，并额外引入了自我演化协议层（SEPL）来管理演化的闭环过程。

在优化类研究中，诸如TextGrad等方法将自然语言反馈视为梯度信号来迭代更新提示，而Reinforce++和GRPO等强化学习方法则利用评估信号作为奖励来优化策略。这些方法虽然能改进智能体行为，但通常应用于狭窄的范畴，缺乏管理异构组件的共享抽象，且更新过程缺少明确的生命周期控制或版本追踪。本文的Autogenesis提供了一个协议级抽象，将这些优化策略容纳进来，通过标准化的、可演化的资源接口和受控的操作接口来支持它们。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Autogenesis Protocol (AGP)的两层自演化协议来解决现有智能体系统在跨实体生命周期、上下文管理、版本跟踪和演化安全更新接口方面规范不足的问题。其核心方法是将“演化什么”与“如何演化”进行解耦，从而支持模块化、可追溯且安全的系统演化。

整体框架分为两个协议层：资源基底协议层（RSPL）和自演化协议层（SEPL）。RSPL定义了可演化的基底，将提示（Prompt）、智能体（Agent）、工具（Tool）、环境（Environment）和记忆（Memory）这五类实体建模为具有明确状态、生命周期和版本化接口的“协议注册资源”。每个资源实体通过注册记录进行管理，记录包含实体元组、版本字符串、实现描述符、实例化参数以及供LLM交互的导出表示。RSPL为每类资源绑定一个上下文管理器和一个服务器暴露接口。上下文管理器负责资源的生命周期控制、版本谱系维护以及生成统一的“合约”描述；服务器接口则封装内部复杂性，提供稳定的外部调用端点。此外，RSPL还包括模型管理器、版本管理器、动态管理器和追踪模块等跨领域服务，以确保可靠的演化。

SEPL层则定义了演化的控制逻辑，将智能体系统的持续改进形式化为一个在异构状态空间上的广义优化问题。其关键技术是“变量提升”，将离散的RSPL资源投影到一个统一的“可演化变量”表示上，并通过一个明确的“可学习掩码”严格界定可训练的子空间。SEPL通过五个原子操作符构成一个闭环演化循环：1) 反思（Reflect）：从执行轨迹中生成因果失败假设；2) 选择（Select）：根据假设生成具体的修改方案；3) 改进（Improve）：通过RSPL接口应用修改，产生候选状态；4) 评估（Evaluate）：根据目标规范评估候选状态的性能和安全性；5) 提交（Commit）：基于评估结果，在满足安全不变性和性能单调性的条件下，将候选状态提交为新的系统状态。

创新点主要体现在：1) 提出了一个清晰解耦的两层协议标准，使演化可组合、可审计、可互操作；2) 将提示、工具等外部化为具有版本化接口的一等资源，实现了智能体逻辑与任务特定组件的解耦；3) 引入了基于控制理论的严格形式化框架，将自演化过程定义为由原子操作符驱动的、可追溯且安全的状态转换，确保了演化的方向性和安全性。

### Q4: 论文做了哪些实验？

论文在多个具有挑战性的基准测试上进行了实验，以评估基于Autogenesis协议的自进化多智能体系统（AGS）的能力。

**实验设置与数据集**：实验使用了四个基准测试。GPQA-Diamond（198个问题）评估闭卷、无需检索的深度科学理解和推理能力。AIME（AIME24和AIME25各30个问题）评估长视野符号推理和算术精度。GAIA Test（300个任务）评估需要规划和工具使用的真实世界多步骤任务完成能力。此外，还构建了一个内部LeetCode编程基准（100个测试问题），评估多语言可执行代码生成。

**对比方法与主要结果**：在GPQA-Diamond、AIME24和AIME25上，为验证自进化能力，比较了三种进化策略（仅进化提示、仅进化解决方案、进化提示+解决方案），并与基础模型（vanilla）对比。使用了多个骨干模型，包括gpt-4o、gpt-4.1、claude-sonnet-4.5、gemini-3-flash-preview和grok-4.1-fast。主要结果包括：1）弱模型（如gpt-4.1）提升更大，强模型（如gemini-3-flash-preview）提升较小但稳定。例如，gpt-4.1在AIME24上准确率从23.34%提升至40.00%（相对提升71.38%），而gemini-3-flash-preview在AIME24上从83.33%提升至93.33%（相对提升12.00%）。2）组合进化策略（提示+解决方案）普遍优于单一策略。3）数学基准（AIME）比科学问答（GPQA）受益更显著。4）在性能接近饱和的基准上（如grok-4.1-fast在AIME24上达96.67%），进化收益有限。

在GAIA基准上，重点评估工具进化能力，系统采用分层多智能体架构（如规划器、工具生成器等），使用gemini-3-flash-preview作为骨干模型。与多个先进基线（如JoyAgent、Alita、DeSearch、AWorld等）对比。结果显示，AGS在GAIA Test上的平均任务完成率达到81.73%，优于对比方法（如DeSearch的78.07%，h2oGPTe-Agent的79.73%），尤其在Level 1任务上达到95.70%的高准确率。

**关键数据指标**：实验主要使用准确率（exact-match accuracy）和任务完成率（task success/completion）作为指标。具体数据包括：在GPQA-Diamond上，最佳结果（grok-4.1-fast结合进化）达89.34%；在AIME24上，最佳结果（grok-4.1-fast）达96.67%；在GAIA上，AGS平均完成率为81.73%（Level 1: 95.70%, Level 2: 81.13%, Level 3: 57.14%）。

### Q5: 有什么可以进一步探索的点？

本文提出的AGP协议在资源管理和自我演化机制上做出了有益探索，但仍存在一些局限和可拓展方向。首先，协议目前主要面向提示、工具、环境等离散资源，对于更复杂的“资源间动态依赖关系”和“演化过程中的冲突消解”缺乏明确规范，未来可引入更精细的依赖图模型和一致性校验机制。其次，评估演化效果的指标可能过于依赖任务成功率，忽略了计算开销、稳定性等维度，可设计多目标评估函数以平衡效率与性能。此外，系统目前依赖预设的演化操作接口，未来可探索让AI自主发现新的演化策略，实现“元演化”。从实践角度看，将AGP与真实世界的持续学习系统结合，研究在数据流和需求变化下的长期自适应能力，也是一个值得深入的方向。最后，协议的安全性与可控性需加强，例如引入人类反馈环节或演化边界约束，防止不可控的递归优化。

### Q6: 总结一下论文的主要内容

该论文提出了Autogenesis协议（AGP），旨在解决现有LLM智能体系统在跨实体生命周期管理、上下文处理、版本跟踪和演化安全更新等方面的不足。核心贡献是设计了一个双层协议框架：资源基底协议层（RSPL）将提示、智能体、工具、环境和记忆建模为具有明确状态、生命周期和版本化接口的注册资源；自演化协议层（SEPL）则定义了闭环操作接口，支持改进方案的提出、评估和提交，并具备可审计的谱系和回滚能力。基于AGP，作者构建了Autogenesis系统（AGS），这是一个自演化的多智能体系统，能够在执行过程中动态实例化、检索和优化协议注册的资源。实验表明，AGS在需要长程规划和异构资源工具使用的多个基准测试中均优于现有基线，验证了其资源管理和闭环自演化机制的有效性。该工作为构建更模块化、可维护和自适应演进的智能体系统提供了重要基础。
