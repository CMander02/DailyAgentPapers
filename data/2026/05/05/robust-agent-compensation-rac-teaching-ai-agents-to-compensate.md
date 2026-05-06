---
title: "Robust Agent Compensation (RAC): Teaching AI Agents to Compensate"
authors:
  - "Srinath Perera"
  - "Kaviru Hapuarachchi"
  - "Frank Leymann"
  - "Rania Khalaf"
date: "2026-05-05"
arxiv_id: "2605.03409"
arxiv_url: "https://arxiv.org/abs/2605.03409"
pdf_url: "https://arxiv.org/pdf/2605.03409v1"
categories:
  - "cs.AI"
tags:
  - "Agent可靠性"
  - "Agent异常恢复"
  - "日志恢复"
  - "智能体架构"
  - "LangChain"
  - "Agent评测"
relevance_score: 8.5
---

# Robust Agent Compensation (RAC): Teaching AI Agents to Compensate

## 原始摘要

We present Robust Agent Compensation (RAC), a log-based recovery paradigm (providing a safety net) implemented through an architectural extension that can be applied to most Agent frameworks to support reliable executions (avoiding unintended side effects). Users can choose to enable RAC without changing their current agent code (e.g., LangGraph agents). The proposed approach can be implemented in most existing agent frameworks via their existing extension points. We present an implementation based on LangChain, demonstrate its viability through the $τ$-bench and REALM-Bench, and show that when solving complex problems, RAC is 1.5-8X or more better in both latency and token economy compared to state-of-the-art LLM-based recovery approaches.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决AI Agent在执行过程中因自身或工具故障导致的“无意的副作用”问题，即系统在部分操作成功而整体失败后遗留的不一致状态。当前，大语言模型驱动的Agent（如ReAct模式或Plan-and-Execute模式）具有高度动态性，执行路径在运行时决定，这使得难以提前编写恢复代码。现有方法存在不足：手动编写恢复代码无法穷举所有可能路径；而基于LLM的恢复方案（如SagaLLM）在处理复杂问题时，会因规划循环或幻觉导致高延迟和高token消耗，甚至引发不必要或错误的补偿行为。为此，本文提出鲁棒Agent补偿机制（RAC），它是一种基于日志的确定性恢复范式，通过可扩展的架构实现，能够独立于Agent的具体行为进行补偿式恢复。RAC的核心目标是确保无论执行结果如何，Agent都不会留下任何无意的副作用，从而在动态场景下实现可靠的Agent执行，并在延迟和token经济性上显著优于现有方案。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要围绕补偿模型、恢复机制和评测基准展开。首先，在补偿模型类工作中，ACID事务和两阶段提交协议是经典方法，但难以处理长时间运行或高并发的系统；Saga模式通过将事务分解为子事务并定义补偿操作来撤销副作用（如Colombo等人），这为RAC的补偿模型奠定了基础。然而，Saga模式主要针对微服务或Web服务（如Weerawarana等人），而本文聚焦于动态的AI Agent场景。其次，在恢复机制类工作中，Unruh等人（2005）提出通过重试和补偿恢复Agent系统，但依赖开发者编写恢复逻辑；SagaLLM则基于Saga模式接受任务提示并生成带事务保障的Agent工作流，但其依赖LLM生成代码和补偿操作，易受幻觉影响且不支持静态代码Agent。相比之下，RAC通过架构扩展基于日志实现无需修改现有Agent代码的恢复，并在延迟和令牌经济性上比基于LLM的方法提升1.5-8倍。最后，在评测基准方面，Wang等人的"High or Hell Water"和Appworld仅含只读操作，无法评估副作用；τ²-bench和REALM-Bench则提供了真实工具故障和调度场景，本文不仅在其上验证可行性，还扩展了REALM-Bench以包括不可解场景，从而更全面地测评鲁棒性。

### Q3: 论文如何解决这个问题？

RAC通过架构扩展实现日志驱动的恢复范式，核心包含三个模块：工具拦截器、恢复补偿管理器（RCManager）和补偿对注册机制。工具拦截器嵌入到Agent框架的扩展点中，记录每个工具调用的事件（开始、完成、错误）到持久化事务日志，当检测到错误时触发handleFailure()方法。RCManager的handleFailure()采用三层恢复策略：首先通过错误码和LLM判断是否为临时错误并执行带退避的重试；若失败则尝试用LLM寻找替代工具调用；若均失败则调用Rollback()完全回滚。Rollback()从事务日志重建执行图，通过拓扑排序按依赖顺序反向执行补偿操作。补偿对的发现采用三级优先级：开发者通过框架API显式定义（如LangGraph的compensation_pairs参数）、工具通过MCP协议注解声明（如x-compensation-tool字段）、最后通过LLM推导。创新点包括：（1）将补偿信息与工具定义解耦，支持零代码迁移；（2）通过将回滚摘要注入Agent上下文，使ReAct代理能处理更复杂场景（失败时上下文携带补偿报告，ReAct无需直接处理错误）；（3）支持语义错误检测，可通过用户定义提示词识别非平台级错误。实验表明在τ-bench和REALM-Bench上，RAC相比基于LLM的恢复方法在延迟和token消耗上提升1.5-8倍。

### Q4: 论文做了哪些实验？

在实验中，论文首先在 **τ²-bench**（涵盖航空、零售、电信三个客户服务领域）和 **REALM-Bench**（涵盖调度、路由、物流、救灾、供应链五个复杂规划类别）上进行评估。实验设置包括：使用 LangGraph ReAct Agent 作为基础框架，对比方法包括 Vanilla ReAct Agent (LG)、带提示工程的 ReAct Agent (LG(PE)) 以及 SOTA 方法 SagaLLM。硬件为 M3 Pro CPU/18GB RAM，LLM 默认使用 gemini-2.5-flash。每个问题重复 3 次，测量执行时间、token 效率和目标完成率（成功率和完全完成率）。主要结果：在 τ²-bench 中，RAC 成功率（97-100%）与 SagaLLM 相当，但在零售和电信领域延迟更低（如零售：22s vs 65s）且 token 更省（66k vs 71k）；在电信领域，RAC 完全完成率为 99%，远超其他方法（≤2%）。在 REALM-Bench 中，RAC 成功率几乎全满，token 消耗（9k-33k）远低于 SagaLLM（52k-250k），延迟（14-32s）也显著优于 SagaLLM（106-646s）。此外，论文还设计了三个动态失败场景（P12-P14），结果显示 LG 全部失败，LG(PE) 仅通过 P12，SagaLLM 部分失败，而 RAC 在 P12 和 P13 中全部成功，P14 成功 2/3。在额外测试中，SagaLLM 在无限制下消耗 500 万 token 和 20 倍时间，而 RAC 仍高效。消融实验使用 GPT-5.4 高推理模型进一步验证了 RAC 的鲁棒性。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在RAC目前仅支持基于日志的补偿策略，对于需要实时感知环境变化或动态调整目标的场景可能不够灵活。未来研究方向包括：1) 引入预测性补偿机制，通过分析历史错误模式预判潜在失败点并主动调整；2) 结合强化学习优化补偿策略选择，使系统能从历史补偿案例中自适应学习最优恢复路径；3) 探索多智能体协同补偿框架，当单个agent补偿成本过高时通过任务再分配降低开销。此外，当前评估主要聚焦于确定性任务，对开放域环境的鲁棒性尚未验证，可考虑引入对抗性测试用例生成和不确定性量化方法。改进思路包括将RAC与基于LLM的因果推理结合，在补偿前先分析故障根因而非仅恢复程序状态，以及利用扩散模型生成合规性更强的补偿序列。

### Q6: 总结一下论文的主要内容

本论文提出鲁棒智能体补偿（RAC），一种基于日志的恢复范式，通过架构扩展为AI智能体提供安全网，确保可靠执行并避免意外副作用。问题定义：现有AI智能体在执行动态任务（如ReAct模式）时，工具或智能体自身可能失败，且执行顺序在运行时才确定，导致开发者难以预先编写恢复代码；失败后残留的副作用（如已预订的机票和酒店）无法被撤销，造成系统不一致。方法概述：RAC通过日志记录所有已执行动作，并利用补偿机制（定义动作的逆向操作）实现确定性恢复；其架构扩展可无缝集成到LangGraph等现有智能体框架，无需修改用户代码；基于Model Context Protocol（MCP）的扩展点实现补偿对的互操作发现。主要结论：在τ-bench和REALM-Bench评测中，相比最先进的基于LLM的规划恢复方法（如SagaLLM），RAC在复杂问题上实现1.5-8倍以上的延迟降低和令牌经济性提升；解耦恢复逻辑使ReAct智能体能处理更困难的问题，避免规划方法中昂贵的重规划循环和幻觉风险。核心贡献在于提供了一种高效、可靠的确定性补偿恢复方案，显著提升智能体执行鲁棒性。
