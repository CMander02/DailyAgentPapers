---
title: "The LLMbda Calculus: AI Agents, Conversations, and Information Flow"
authors:
  - "Zac Garby"
  - "Andrew D. Gordon"
  - "David Sands"
date: "2026-02-23"
arxiv_id: "2602.20064"
arxiv_url: "https://arxiv.org/abs/2602.20064"
pdf_url: "https://arxiv.org/pdf/2602.20064v1"
categories:
  - "cs.PL"
  - "cs.AI"
  - "cs.CR"
tags:
  - "Agent 架构"
  - "Agent 安全"
  - "形式化方法"
  - "信息流控制"
  - "编程语言理论"
  - "提示注入"
  - "语义基础"
relevance_score: 9.0
---

# The LLMbda Calculus: AI Agents, Conversations, and Information Flow

## 原始摘要

A conversation with a large language model (LLM) is a sequence of prompts and responses, with each response generated from the preceding conversation. AI agents build such conversations automatically: given an initial human prompt, a planner loop interleaves LLM calls with tool invocations and code execution. This tight coupling creates a new and poorly understood attack surface. A malicious prompt injected into a conversation can compromise later reasoning, trigger dangerous tool calls, or distort final outputs. Despite the centrality of such systems, we currently lack a principled semantic foundation for reasoning about their behaviour and safety. We address this gap by introducing an untyped call-by-value lambda calculus enriched with dynamic information-flow control and a small number of primitives for constructing prompt-response conversations. Our language includes a primitive that invokes an LLM: it serializes a value, sends it to the model as a prompt, and parses the response as a new term. This calculus faithfully represents planner loops and their vulnerabilities, including the mechanisms by which prompt injection alters subsequent computation. The semantics explicitly captures conversations, and so supports reasoning about defenses such as quarantined sub-conversations, isolation of generated code, and information-flow restrictions on what may influence an LLM call. A termination-insensitive noninterference theorem establishes integrity and confidentiality guarantees, demonstrating that a formal calculus can provide rigorous foundations for safe agentic programming.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图为基于大语言模型（LLM）的AI智能体系统建立一个严格的形式化语义基础，以解决其面临的核心安全问题——提示注入攻击。当前，AI智能体通过规划循环自动构建提示-响应对话序列，并交织LLM调用、工具执行和代码运行。这种紧密耦合创造了一个新的、未被充分理解的攻击面：恶意提示注入可以破坏后续推理、触发危险工具调用或扭曲最终输出。尽管这类系统至关重要，但学术界目前缺乏一个原则性的理论框架来推理其行为与安全性。

为此，论文引入了**LLMbda演算**，一个扩展了动态信息流控制和无类型按值调用λ演算的形式化系统。它通过一组精简的原语（如用于调用LLM的`@`操作符、用于分叉对话的`fork`和用于隔离历史的`clear`）来建模提示-响应对话的构造与操作。该演算能精确表征规划循环及其漏洞（特别是提示注入如何改变后续计算的机制），并支持对防御措施（如隔离子对话、隔离生成代码、对LLM调用的信息流施加限制）进行形式化推理。

论文的主要贡献是提供了一个能捕捉智能体编程核心机制的形式化演算，并基于此建立了一个**可靠的信息流安全基础**。其核心理论成果是一个终止不敏感的非干涉定理，该定理确立了完整性和保密性保证，从而首次为一般化的智能体程序提供了基于信息流的防御形式化，弥补了现有工作（如CaMeL）缺乏严格证明的不足。

### Q2: 有哪些相关研究？

本文的核心相关研究主要围绕AI Agent的形式化建模、安全防御及编程语言设计展开。首先，在**Agent架构与安全威胁**方面，Yao等人提出的ReAct框架和Schick等人的Toolformer工作展示了Agent如何通过工具调用与环境交互，这构成了本文建模的基础攻击面。Willison早期提出的**提示注入攻击**及**双LLM模式**（Privileged/Q-LLM）是直接的安全动机，而CaMeL则进一步实现了基于动态信息流追踪和代码生成的防御方案，但缺乏形式化证明——本文正是为了填补这一理论空白。

在**形式化方法**上，Costa等人的FIDES首次为Agent规划器提供了信息流安全的形式化保证（如非干涉性），但其局限于固定程序模式，未涵盖代码生成等灵活行为。相比之下，本文的LLMbda演算将Agent交互抽象为λ演算扩展，能更通用地刻画对话状态和生成式操作。此外，Mell等人的OPAL和Quasar语言同样基于λ演算，专注于LLM编程的可靠性与性能，但未涉及安全属性和提示注入防御，本文则在语义中显式集成了信息流控制机制。

综上，本文与CaMeL和FIDES构成直接对话：一方面将CaMeL的实践模式形式化，另一方面突破了FIDES的固定模式限制，建立了可表达动态代码生成的理论模型。同时，本文借鉴了OPAL/Quasar的语言设计思路，但核心贡献转向安全语义与可证明的防御机制。

### Q3: 论文如何解决这个问题？

论文通过引入一个名为LLMbda演算的形式化系统来解决AI Agent对话中的安全与信息流控制问题。其核心方法是在无类型按值调用的λ演算基础上，扩展了三个关键原语：`@e`（调用LLM生成响应）、`fork e`（临时分叉对话）和`clear`（清空当前对话）。这些原语使得系统能够精确建模Agent的规划循环（planner loop），即自动交织LLM调用、工具执行和代码评估的过程。

架构设计上，LLMbda演算明确将对话历史（conversation history）作为计算状态的一部分。语义规则定义了表达式求值如何读取和更新这个带标签的对话状态。特别是`@e`操作符的语义：它先对表达式`e`求值得到提示词，将其序列化后发送给LLM；LLM基于当前对话历史生成响应，该响应被解析为一个新项；最后，对话历史被扩展为包含该次交互的提示-响应对。这种设计使得提示注入（prompt injection）等攻击能被形式化表示为：恶意提示通过修改对话历史，影响后续LLM调用的生成过程。

关键技术是动态信息流控制（dynamic information flow control）。系统为所有值和对话历史引入了一个基于格（lattice）的标签体系（例如，包含“不可信U”和“秘密S”）。通过标签传播规则和`l?e`测试操作符，可以追踪数据在计算过程中的流动。安全防御机制被编码为语言原语：`fork e`允许创建隔离的子对话（类似沙箱），确保子计算中的提示注入不会污染主对话；`clear`可以清空上下文；而信息流标签能约束哪些数据可以影响LLM调用（例如，确保秘密或不可信数据不会泄露到提示中）。论文最终通过一个终止不敏感的非干涉定理（termination-insensitive noninterference theorem）证明了系统的完整性和保密性保证，为安全的Agent编程提供了严格的形式化基础。

### Q4: 论文做了哪些实验？

论文通过三个核心示例实验来展示LLMbda演算如何建模AI智能体对话及其安全属性。

实验设置上，作者构建了一个基于lambda演算的编程语言，并添加了三个新操作符：`@e`（调用LLM生成响应）、`fork e`（创建临时对话分支）和`clear`（清除当前对话上下文）。实验在一个实现了该演算的解释器中运行。

基准测试围绕三个逐步复杂的智能体场景展开：
1.  **邮政编码提取**：演示对话上下文的持久性。先通过`@`操作符设定详细的系统提示，然后使用`fork`独立处理三个地址，成功提取并格式化了邮政编码（如“SW1A 2AA”）。
2.  **简单修复循环**：展示智能体处理错误的机制。构建一个重试循环，当LLM生成的代码语法错误时，将错误信息反馈给LLM继续对话，直到成功生成阶乘函数，平均耗时7.3秒。
3.  **带测试用例的智能体循环**：模拟更复杂的智能体编程。要求LLM根据提示和测试用例合成函数（如坐标交换、点反射）。智能体在`fork`和`clear`创建的隔离上下文中工作，循环检查语法、函数类型和测试通过情况。两个任务均在一轮内成功合成正确函数，耗时约3.1秒。

主要结果表明，LLMbda演算能形式化地建模智能体对话流、上下文管理、错误修复循环以及子任务隔离，为分析提示注入等攻击和设计隔离防御提供了语义基础。

### Q5: 有什么可以进一步探索的点？

本文提出的LLMbda演算为AI Agent对话安全提供了形式化基础，但仍有多个方向值得深入探索。局限性方面，当前演算未考虑LLM本身的不确定性及多轮对话中的状态累积效应，且假设工具调用完全可靠，这与现实部署存在差距。未来可探索扩展类型系统以捕获更复杂的信息流模式，或将演算与运行时监控机制结合实现动态策略执行。此外，可研究如何将该形式模型应用于实际框架（如LangChain）的安全加固，并探索对抗性提示的自动检测与防御技术。另一个重要方向是引入量化的信息流度量，以评估实际系统中数据污染的风险等级。

### Q6: 总结一下论文的主要内容

这篇论文的核心贡献是提出了“LLMbda演算”——一个形式化的计算模型，用于为基于大语言模型（LLM）的AI智能体系统建立严格的理论基础。论文指出，当前AI智能体（如自动规划循环）将LLM调用、工具使用和代码执行紧密耦合，形成了一个新的、未被充分理解的安全攻击面（如提示注入攻击）。为了系统性地分析和保障这类系统的安全性，作者设计了一个未类型化、按值调用的λ演算，并扩展了动态信息流控制原语以及用于构建提示-响应对话的少量基本操作。该演算能精确建模智能体的规划循环及其漏洞机制，其语义显式地刻画对话过程，从而支持对隔离子对话、代码隔离、限制LLM调用影响范围等防御措施进行形式化推理。论文还证明了一个终止不敏感的非干涉定理，为智能体编程的完整性和保密性提供了严格的理论保证。这项工作的重要意义在于，它为理解和确保日益复杂的AI智能体系统的行为与安全，首次提供了一个原则性的语义基础。
