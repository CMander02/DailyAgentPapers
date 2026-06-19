---
title: "Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services"
authors:
  - "Mugeng Liu"
  - "Shuoqi Li"
  - "Yixuan Zhang"
  - "Yun Ma"
date: "2026-06-18"
arxiv_id: "2606.19992"
arxiv_url: "https://arxiv.org/abs/2606.19992"
pdf_url: "https://arxiv.org/pdf/2606.19992v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent工具使用"
  - "Agent规划"
  - "Agent执行优化"
  - "Agent接口设计"
  - "Web Agent"
  - "多步工作流"
  - "工具程序"
  - "基于LLM的Agent"
  - "函数调用"
  - "执行效率"
relevance_score: 9.5
---

# Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services

## 原始摘要

In the agentic web era, LLM-based agents increasingly invoke web services as tools, yet most interfaces remain \emph{static endpoints} that poorly express long-horizon workflows with loops, conditionals, joins, and retries. We present ToolPro, which represents an agent's tool intent as an \emph{executable tool program} that compactly encodes multi-step service interactions with explicit effect types. ToolPro combines constraint-guided program construction, effect-aware replay for exactly-once state-modifying calls, and a profile-driven policy that decides when program execution outperforms stepwise calling. We instantiate ToolPro over MCP-style services with WebAssembly sandboxing and evaluate it on diverse workflows of real-world applications. ToolPro reduces end-to-end latency by up to 53.4\% and client-side traffic by up to 96.1\%, with larger gains under higher network latency and workflow complexity.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前基于大语言模型（LLM）的智能体在调用Web服务时面临的核心瓶颈问题。研究背景是，LLM智能体越来越多地需要编排Web服务以完成长周期工作流，但现有服务接口大多是“静态端点”，即仅支持单次查询的API。当任务需要循环、条件判断、中间绑定等控制流时，智能体不得不将工作流拆解成脆弱的端点调用序列，并穿插多轮推理。现有方法的不足主要体现在三个方面：（1）扩展性差，每步都要进行客户端-服务端往返和智能体推理，导致延迟随步骤数线性增长；（2）数据过度获取或不足，因为控制逻辑在服务端外实现；（3）错误恢复脆弱，局部失败后的重试可能重复执行状态修改操作，造成副作用不一致。因此，本文旨在突破静态端点的表征瓶颈，提出将工具程序（Tool Programs）作为新的智能体-服务接口。核心问题是将多步骤交互封装成可执行、可优化且能安全重放的程序对象，以替代脆弱的端点调用序列，从而在保持服务行为不变的前提下，显著降低端到端延迟和客户端流量，并确保重试时的副作用安全。

### Q2: 有哪些相关研究？

本文的相关研究主要分为四个方面。在**接口与表示**方面，现有工作大多数采用逐步调用的静态端点，其中控制流隐含在代理策略的多轮推理中，导致网络轮次和延迟增加。本工作 ToolPro 则通过显式可执行的工具程序表达意图，包含约束表面和效果类型，支持编译、检查和优化。在**可执行交互逻辑**方面，RESTful 端点演进至 GraphQL 等灵活查询接口，但后者无法编码循环、条件、重试等过程逻辑；ORFA 使用 Wasm 模块作为图灵完备查询语言，但 ToolPro 聚焦于代理工作流中可执行性与重执行副作用问题，通过 LLM 合成、可修复的程序与效果类型契约实现重试安全语义。在**程序化代理与原地执行**方面，CodeAct 将可执行代码作为动作空间，AFlow 搜索代码表示的代理工作流，ToolPro 不同在于提交的程序是作为效果类型化的服务接口对象，运行时必须强制重放安全写行为；这也类似 eBPF 将逻辑移近执行边界，但 ToolPro 处理动态生成的工具程序，具有显式效果注解、沙箱执行和故障闭合回退。最后，**Wasm 沙箱**作为支撑基底提供安全执行环境。

### Q3: 论文如何解决这个问题？

ToolPro 将智能体的工具使用意图表示为可执行工具程序，以此替代传统的静态端点调用。其核心架构围绕三个关键技术设计。首先，采用**约束引导的程序构建**：系统接收智能体的高层次任务目标，通过一个程序合成器生成紧凑的工具程序，该程序将多步服务交互（包含循环、条件分支、连接和重试）编码为带有显式效果类型的可执行代码，从而压缩冗余的序列化调用。其次，引入**效果感知的重放机制**：由于工具程序可能包含状态修改操作（如数据库写入），ToolPro 利用效果类型（如只读、幂等、非幂等修改）实现“恰好一次”执行。当程序因网络中断或错误需要重试时，仅重放幂等或只读部分，对已执行的非幂等状态修改操作自动跳过，确保服务侧一致性。最后，**基于配置文件的策略**动态决策执行模式：系统维护一个即时更新的性能配置文件，通过轻量级在线学习比较工具程序整体执行与逐步骤调用在不同网络延迟和工作流复杂度下的时延及流量消耗。当程序执行预期优于逐步调用时（如高延迟场景下减少往返次数），策略才激活工具程序模式，否则回退到传统逐步骤调用，保证鲁棒性。整体上，ToolPro 在 MCP 风格服务上集成 WebAssembly 沙箱执行，实现了高达 53.4% 的端到端延迟降低和 96.1% 的客户端流量削减，尤其在复杂工作流和高网络延迟下优势显著。

### Q4: 论文做了哪些实验？

论文在Memos、Directus和MinIO三个开源应用上评估，每个应用构建了只读（.r）和读写（.w）两类工作流，通过参数N控制流程长度。主要对比了标准逐步调用基线（MWS）和两个消融变体：\sysname-step（仅意图引导的逐步调用）和\sysname-prog（始终执行程序模式）。在N=10且服务器悉尼-客户端北京配置下，\sysname将端到端延迟降低高达53.4%，客户端流量减少85.3%（复杂跨服务基准上达96.1%）。针对非确定性检索、分支、协调写入等四个复杂基准，\sysname将延迟从30.16s降至17.91s（降40.6%），准确率从0.60提升至0.93；跨服务基准延迟从52.68s降至24.54s（降53.4%），准确率从0.20升至0.80。网络条件实验（伦敦/悉尼/旧金山服务器+额外50-200ms延迟）显示RTT越大差距越明显，2000ms时程序模式比逐步模式快近13s。工作流复杂度实验（N=5至20）表明程序模式延迟近乎恒定（逐步模式线性增长），完整策略通过轮廓驱动模式选择实现最优性能。重放消融实验证实禁用重放使平均延迟增加19.7%（17.92s→21.45s），回退率升至3/15。

### Q5: 有什么可以进一步探索的点？

论文提出的ToolPro框架通过工具程序封装多步工作流，但仍存在若干探索方向。首先，当前基于profiling的执行决策策略依赖历史数据，在动态网络环境中可能过时，未来可引入在线强化学习实时调整策略。其次，对多Agent协作场景考虑不足，当多个代理共享同一工具程序时，效果类型系统需处理并发冲突和分布式事务。第三，工具程序生成依赖手工约束，可探索利用大模型自动从自然语言指令生成带类型约束的DSL。此外，文中假设服务接口稳定，但实际中Web服务可能动态变更，需研究程序缓存的失效检测与增量更新机制。最后，安全沙箱的WASM实现限制了复杂计算，可设计分层执行架构，将轻量逻辑运行在客户端而将重型计算委托至边缘节点。这些方向有望进一步降低跨域服务编排的通信开销与执行风险。

### Q6: 总结一下论文的主要内容

大型语言模型代理在执行多步骤网络服务工作流时，传统的静态API端点因无法表达循环、条件判断等控制流而成为瓶颈。本文提出ToolPro，将代理的工具意图表示为可执行的工具程序，紧凑地编码多步服务交互并显式区分读（READ）与写（WRITE）效果类型。该方法通过约束引导的程序构造提升可执行性，利用效果感知重放实现写操作的精确一次性语义以安全处理修复，并采用基于配置文件的自适应策略决定何时合并程序执行比逐步调用更优。在基于MCP风格服务与WebAssembly沙箱的实验中，ToolPro在真实应用工作流上将端到端延迟降低最高53.4%，客户端流量减少最高96.1%，且增益随网络延迟和工作流复杂度增加而扩大。这项工作为构建高效、灵活、可安全重试的智能体网络服务接口奠定了重要基础。
