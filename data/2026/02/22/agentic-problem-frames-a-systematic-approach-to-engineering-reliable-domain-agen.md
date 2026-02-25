---
title: "Agentic Problem Frames: A Systematic Approach to Engineering Reliable Domain Agents"
authors:
  - "Chanjin Park"
date: "2026-02-22"
arxiv_id: "2602.19065"
arxiv_url: "https://arxiv.org/abs/2602.19065"
pdf_url: "https://arxiv.org/pdf/2602.19065v1"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "Agent 可靠性"
  - "系统工程"
  - "形式化规范"
  - "闭环控制"
  - "领域智能体"
  - "Agent 评测"
relevance_score: 9.0
---

# Agentic Problem Frames: A Systematic Approach to Engineering Reliable Domain Agents

## 原始摘要

Large Language Models (LLMs) are evolving into autonomous agents, yet current "frameless" development--relying on ambiguous natural language without engineering blueprints--leads to critical risks such as scope creep and open-loop failures. To ensure industrial-grade reliability, this study proposes Agentic Problem Frames (APF), a systematic engineering framework that shifts focus from internal model intelligence to the structured interaction between the agent and its environment.
  The APF establishes a dynamic specification paradigm where intent is concretized at runtime through domain knowledge injection. At its core, the Act-Verify-Refine (AVR) loop functions as a closed-loop control system that transforms execution results into verified knowledge assets, driving system behavior toward asymptotic convergence to mission requirements (R). To operationalize this, this study introduces the Agentic Job Description (AJD), a formal specification tool that defines jurisdictional boundaries, operational contexts, and epistemic evaluation criteria.
  The efficacy of this framework is validated through two contrasting case studies: a delegated proxy model for business travel and an autonomous supervisor model for industrial equipment management. By applying AJD-based specification and APF modeling to these scenarios, the analysis demonstrates how operational scenarios are systematically controlled within defined boundaries. These cases provide a conceptual proof that agent reliability stems not from a model's internal reasoning alone, but from the rigorous engineering structures that anchor stochastic AI within deterministic business processes, thereby enabling the development of verifiable and dependable domain agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的自主智能体（Agentic AI）在工业应用开发中存在的“无框架”（frameless）问题。具体而言，当前开发模式过度依赖模糊的自然语言指令，缺乏严谨的工程蓝图，导致智能体在部署时面临三大关键风险：1) **范围蔓延**：由于缺乏明确的职责边界，智能体可能越权操作或干涉无关领域，造成责任不清；2) **知识/现实脱节**：由于缺少领域知识作为基准来锚定用户意图，智能体可能基于幻觉或猜测制定错误计划；3) **开环失效**：缺乏系统性的反馈与验证机制，智能体错误地假设“执行即成功”，导致其内部状态与实际世界严重不匹配，且无法将执行结果转化为可验证的知识资产以优化后续行为。

为此，论文提出了一个系统性的工程框架——**Agentic Problem Frames**，其核心思想是将关注点从智能体内部不可控的、概率性的“黑箱”推理，转移到**智能体与其环境之间结构化的交互**上。该框架通过引入形式化规范工具**Agentic Job Description**来定义智能体的管辖边界、操作上下文和认知评估标准，并构建一个**Act-Verify-Refine闭环控制循环**，将执行结果转化为经过验证的知识，驱动系统行为渐近收敛于任务要求，从而将随机的人工智能锚定在确定性的业务流程中，最终实现可验证、高可靠的领域智能体。

### Q2: 有哪些相关研究？

本文的相关研究主要分为四大类，并与之形成互补或超越关系。

1.  **问题框架理论**：本文的理论基石是Michael Jackson和Pamela Zave提出的**问题框架理论**。该理论强调从机器内部设计转向对机器与外部世界交互的结构化建模。本文将其核心思想（如需求R是世界状态的改变、依赖领域知识K、通过分解隔离不确定性）应用于智能体领域，用以“驯服”大语言模型的随机行为，构建可靠的工程组件。

2.  **AI系统工程挑战**：研究指出，传统软件工程在应用于AI时面临核心瓶颈，即**“期望结果描述的模糊性”**。本文认同这一挑战，并提出通过**动态规约**和**Agentic工作描述**来明确界定智能体的职责边界，将问题从“初始正确性”转变为**动态 grounding 与验证**。

3.  **智能体推理与架构**：
    *   **Chain-of-Thought** 和 **ReAct** 框架是重要的先驱工作，它们分别增强了智能体的内部推理能力和与环境的交互式规划能力。本文认为这些方法在工程上存在不足，即对环境反馈的处理依赖于模型对自然语言的理解，易产生幻觉。因此，本文提出的**AVR循环**旨在用工程化的**闭环反馈**来补充这些以推理为中心的框架，通过验证函数将状态变化转化为可资产化的**已验证知识**，从而确保推理基于已验证的现实。

4.  **工具使用、反思与多智能体系统**：
    *   **Reflexion** 和 **Toolformer** 等研究探索了智能体通过反思或自主学习来使用工具和优化行为。本文指出，有效的反思和工具使用需要一个清晰的**参考点**（即对世界的 grounded 模型）。本文的AVR循环和AJD正是为此提供了结构化框架，将自适应过程导向对需求R的**渐近收敛**。
    *   **Generative Agents、AutoGen** 以及 **ChatDev、MetaGPT** 等多智能体系统研究了通过对话进行协作。本文认为，仅靠“基于聊天的共识”容易导致级联幻觉。因此，本文借鉴**单一职责原则**，强调通过AJD将随机模型转化为使命明确、边界清晰、可验证的**工程化组件单元**，从而为构建可靠、可扩展的智能体组织提供基础模块，实现从**非结构化协作**到**结构化组件化**的转变。

### Q3: 论文如何解决这个问题？

论文通过提出“Agentic Problem Frames (APF)”这一系统性工程框架来解决LLM智能体开发中因缺乏蓝图而导致的可靠性问题。其核心方法是将关注点从模型内部智能转移到智能体与环境的结构化交互上，旨在将随机模型转化为可靠的、面向任务的组件。

架构设计围绕三个核心实体展开：**Job Performer (M)** 和 **Workplace (W)**。M是执行概率推理的随机机器（如LLM），而W则是一个活跃的“工作场所”，被具体化为三个子域：1) **上下文与知识域 (W_Context)**，通过RAG等技术注入领域知识，将模糊的用户请求具体化为有界的执行规范(S_t)；2) **交互域 (W_Interaction)**，作为动态网关，支持智能体通过标准化协议（如MCP）主动使用工具，将规范(S_t)转化为实际行动(A)；3) **验证与批准域 (W_Verification)**，作为“认识论过滤器”，通过回调或用户确认等方式，验证行动结果是否符合原始意图，并生成确认知识(K_{t+1})。

关键技术是**Act-Verify-Refine (AVR) 闭环控制循环**。该循环将智能体执行建模为一个受控的状态演化过程：1) **Act（行动）**：结合触发事件(E_t)和管辖上下文(C_t)，具体化出执行规范(S_t)，随后在工作场所中执行行动，引发状态变化(W_{t+1})。2) **Verify（验证）**：通过验证函数观察W_{t+1}，提取出增量确认知识(K_Δ)。3) **Refine（精炼）**：将K_Δ与现有知识库(K_t)整合，更新为K_{t+1}，并立即将其作为下一循环的上下文(C_{t+1})。通过这种迭代，系统驱动智能体的行为**渐近收敛**于任务要求(R)。

整个执行过程被形式化为类似霍尔逻辑的工程边界：`{S_t} A {K_{t+1}}`。前置条件是通过上下文绑定将模糊意图具体化为明确的规范S_t，防止任务漂移；后置条件是通过验证将不确定的行动结果固化为可依赖的知识K_{t+1}。最终，可靠性并非源于模型内部推理，而是源于这种将随机AI锚定在确定性业务流程中的严格工程结构。

### Q4: 论文做了哪些实验？

论文通过两个对比性的案例研究来验证所提出的Agentic Problem Frames (APF)框架的有效性。实验设置并非传统的量化基准测试，而是采用概念验证和定性分析的方法，旨在展示APF和Agentic Job Description (AJD)如何系统地将智能体行为控制在预定边界内。

**实验设置**：
1.  **案例一：商务差旅的委托代理模型**：该场景涉及一个代表用户处理差旅预订（如机票、酒店）的智能体。研究应用AJD来形式化地定义其职责边界（如预算限制、公司政策）、操作上下文（如可访问的预订系统）以及认知评估标准（如如何确认预订成功）。
2.  **案例二：工业设备管理的自主监督模型**：该场景涉及一个监控和管理工业设备（如预测性维护、故障响应）的自主智能体。同样，通过AJD明确其管辖范围、可操作的工具（如传感器API、维护工单系统）和验证机制（如设备状态回调确认）。

**主要结果与分析**：
通过将基于AJD的规范和APF建模应用于这两个场景，分析表明：
*   **系统性控制**：操作场景（如处理模糊的用户请求或响应设备警报）能够被系统地控制在AJD定义的边界内。智能体的意图通过领域知识注入在运行时被具体化，其行动结果通过验证域（如确认邮件、设备状态反馈）转化为已验证的知识资产。
*   **可靠性来源**：案例研究从概念上证明，智能体的可靠性并非仅仅源于模型内部的推理能力，而是源于将随机性AI锚定在确定性业务流程中的严格工程结构。APF框架的核心——Act-Verify-Refine (AVR)循环作为一个闭环控制系统，驱动系统行为向任务要求渐近收敛。
*   **工程化验证**：实验验证了APF框架能够将概率模型转变为可靠、面向任务的组件，从而支持开发可验证、可信赖的领域智能体。

### Q5: 有什么可以进一步探索的点？

该论文提出的APF框架在提升Agent可靠性方面迈出了重要一步，但其局限性与未来方向值得深入探索。局限性在于：首先，框架高度依赖精确的领域知识注入和形式化规约（如AJD），这在知识难以结构化或快速变化的开放域场景中可能难以实施；其次，AVR闭环控制依赖于对执行结果的可靠验证，但在复杂环境中，验证标准本身可能难以形式化或存在歧义；最后，案例研究相对理想化，框架在更大规模、多智能体协作或对抗性环境中的可扩展性与鲁棒性尚未得到验证。

未来方向可从以下几方面展开：一是研究如何将框架与不确定性建模结合，使系统能处理模糊或冲突的领域知识；二是探索自适应规约学习，让Agent能在运行中动态调整AJD中的边界与评价标准；三是将APF与现有Agent架构（如ReAct、COT）深度集成，形成兼具工程严谨性与认知灵活性的混合范式；四是建立更全面的评估基准，不仅测试功能收敛，还需评估在规约意外缺失或环境剧变时的安全退化机制。最终目标是使APF从封闭域走向开放域，实现可靠性与泛化能力的平衡。

### Q6: 总结一下论文的主要内容

该论文针对当前基于大语言模型的自主智能体开发缺乏系统化工程方法的问题，提出了“智能体问题框架”（APF）这一系统性工程框架。其核心贡献在于将关注点从模型内部智能转移到智能体与环境的结构化交互上，旨在解决范围蔓延和开环故障等可靠性风险。APF框架建立了动态规范范式，通过运行时注入领域知识来具体化意图，并以“执行-验证-精炼”（AVR）闭环控制为核心，将执行结果转化为已验证的知识资产，驱动系统行为渐进收敛于任务要求。为实现该框架，论文引入了“智能体职责描述”（AJD）这一形式化规范工具，用于定义管辖边界、操作上下文和认知评估标准。通过商务差旅和工业设备管理两个对比性案例研究，论文验证了APF与AJD能有效将智能体的操作场景控制在既定边界内，论证了智能体的可靠性不仅源于模型推理，更依赖于将随机性AI锚定于确定性业务流程的严谨工程结构，从而为开发可验证、可信赖的领域智能体提供了方法论基础。
