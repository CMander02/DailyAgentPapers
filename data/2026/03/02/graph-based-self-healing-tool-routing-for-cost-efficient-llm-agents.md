---
title: "Graph-Based Self-Healing Tool Routing for Cost-Efficient LLM Agents"
authors:
  - "Neeraj Bholani"
date: "2026-03-02"
arxiv_id: "2603.01548"
arxiv_url: "https://arxiv.org/abs/2603.01548"
pdf_url: "https://arxiv.org/pdf/2603.01548v1"
categories:
  - "cs.AI"
  - "cs.SE"
tags:
  - "Tool Use & API Interaction"
  - "Architecture & Frameworks"
relevance_score: 8.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Architecture & Frameworks"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "Self-Healing Router (parallel health monitors + cost-weighted tool graph with Dijkstra's algorithm)"
  primary_benchmark: "N/A"
---

# Graph-Based Self-Healing Tool Routing for Cost-Efficient LLM Agents

## 原始摘要

Tool-using LLM agents face a reliability-cost tradeoff: routing every decision through the LLM improves correctness but incurs high latency and inference cost, while pre-coded workflow graphs reduce cost but become brittle under unanticipated compound tool failures. We present Self-Healing Router, a fault-tolerant orchestration architecture that treats most agent control-flow decisions as routing rather than reasoning. The system combines (i) parallel health monitors that assign priority scores to runtime conditions such as tool outages and risk signals, and (ii) a cost-weighted tool graph where Dijkstra's algorithm performs deterministic shortest-path routing. When a tool fails mid-execution, its edges are reweighted to infinity and the path is recomputed -- yielding automatic recovery without invoking the LLM. The LLM is reserved exclusively for cases where no feasible path exists, enabling goal demotion or escalation. Prior graph-based tool-use systems (ControlLLM, ToolNet, NaviAgent) focus on tool selection and planning; our contribution is runtime fault tolerance with deterministic recovery and binary observability -- every failure is either a logged reroute or an explicit escalation, never a silent skip. Across 19 scenarios spanning three graph topologies (linear pipeline, dependency DAG, parallel fan-out), Self-Healing Router matches ReAct's correctness while reducing control-plane LLM calls by 93% (9 vs 123 aggregate) and eliminating the silent-failure cases observed in a well-engineered static workflow baseline under compound failures.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的工具使用智能体（Agent）在可靠性与成本之间面临的根本性权衡问题。当前主流方法存在两个极端：一是像ReAct这样的方法，将每个工具选择、错误恢复和控制流决策都交由LLM推理，这确保了正确性但带来了高昂的延迟和推理成本（O(n)次LLM调用）；二是像LangGraph这样的预编码工作流图方法，通过状态机消除LLM开销，成本低廉，但在面对未预见的、复合型工具故障（多个工具同时失效）时变得脆弱，可能导致系统静默跳过某些步骤而无法察觉。论文指出，大多数Agent决策本质上是结构化的、常规的，而非需要新颖推理的，例如在多个功能等效的工具（如Stripe vs Razorpay）中选择一个可用的。因此，论文提出了一个名为“自愈路由器”（Self-Healing Router）的故障容忍编排架构，其核心思想是将大部分Agent控制流决策视为路由问题而非推理问题，从而在保持高可靠性的同时，大幅降低对LLM的依赖和运营成本。

### Q2: 有哪些相关研究？

相关研究主要分为四类：1) **LLM Agent框架**：如ReAct确立了经典的“思考-行动-观察”循环，保证了灵活性但成本高；OpenAI和Anthropic的生产级Agent SDK在此基础上提供了结构化错误处理和重试逻辑，但继承了每决策必调用LLM的成本模式。Toolformer、LATS等工作专注于让LLM学习使用工具或进行更复杂的规划搜索，但未解决运行时故障恢复的成本问题。2) **基于图的工作流系统**：如LangGraph、LangChain允许开发者预定义节点（工具）和边（转移），构建确定性工作流，成本低但无法覆盖所有未预见的复合故障组合，存在静默失败风险。3) **基于图的工具编排系统**：如ControlLLM构建工具图并使用深度优先搜索寻找解决方案路径，但未实现基于实时状态的动态重路由和自动恢复。ToolNet使用有向加权图但依赖LLM驱动导航。NaviAgent结合了图规划和基于反馈的适应，但其恢复机制仍集成在LLM驱动的规划循环中。APBDA使用Dijkstra进行AI网络间的任务路由，但非用于单个Agent内部的工具故障恢复。4) **基础设施模式**：论文借鉴了服务网格（如Envoy, Istio）中的健康检查、断路器、负载均衡等模式，将其思想应用于语义层的工具编排。本文的贡献在于将图算法（Dijkstra）与并行健康监控相结合，为LLM Agent创建了一个确定性的、成本不变的运行时故障恢复机制，填补了现有工作在自动、低成本处理复合故障方面的空白。

### Q3: 论文如何解决这个问题？

论文提出了一个三层架构的“自愈路由器”（Self-Healing Router），将注意力分配、行动规划和推理解耦。核心方法结合了**并行健康监控器**和**成本加权工具图**。1) **并行健康监控器**：由多个轻量级模块（如意图分类器、风险检测器、工具健康检查器）组成，它们并行运行，为每个传入请求生成带优先级的信号（如工具故障信号优先级0.99）。通过简单的`max()`操作竞争，优先级最高的信号决定系统下一步关注点，替代LLM作为常规情况的决策者，成本极低。2) **成本加权工具图**：工具作为节点，连接作为带有成本权重的边。给定一个目标，系统使用**Dijkstra最短路径算法**在图中寻找成本最低的有效路径。这是处理“常规但上下文可变”决策的核心。3) **确定性的自愈恢复循环**：当工具在执行过程中失败时，健康监控器检测到并发出高优先级信号；编排器接收到信号后，将该失败工具所有关联边的权重设置为无穷大；随后立即重新运行Dijkstra算法。由于失效边权重无穷大，算法会自动避开并找到下一个成本最低的可用路径。整个过程在亚毫秒内完成，无需调用LLM。4) **LLM作为最后手段**：仅当Dijkstra算法找不到任何通往目标的有限成本路径（即所有替代方案均耗尽）时，才会调用LLM进行目标降级或升级推理（例如，“所有支付提供商都宕机了，最好的降级方案是什么？”）。这种设计确保了93%的常规决策（尤其是故障恢复）由高效的图算法处理，LLM只用于真正需要新颖推理的边界情况。此外，论文还提出了面向生产的运行时图校准机制，其中边权重是基础成本、延迟、可靠性、速率限制和可用性等实时遥测数据的复合函数，使得路径查找能持续优化。

### Q4: 论文做了哪些实验？

论文在三个具有不同图拓扑结构的领域（共19个场景）上进行了全面评估，以测试架构的通用性。1) **领域与场景**：客户支持（线性管道，7个场景）、旅行预订（依赖有向无环图DAG，6个场景）、内容审核（并行扇出，6个场景）。场景覆盖了简单快乐路径、单点故障、目标降级、风险中断、新颖的中途故障以及复杂的复合同时故障。2) **对比基线**：与**ReAct**（纯LLM每决策）、**生产级Agent SDK模式**（继承ReAct成本）、以及精心设计的**LangGraph静态工作流基线**（预编码了单故障回退边）进行对比。3) **评估指标**：主要衡量**正确性**（任务是否完成）、**控制平面LLM推理调用次数**、**使用的工具数量**、**恢复事件**处理方式以及**静默失败**情况。4) **主要结果**：自愈路由器在19个场景中实现了**100%正确性**（19/19），与ReAct持平，而LangGraph基线在3个涉及复合故障的场景中发生了静默失败（16/19）。在成本方面，自愈路由器仅需**9次LLM调用**，相比ReAct的**123次**减少了**93%**。所有13次故障恢复事件均通过Dijkstra重路由自动处理，零LLM参与。5) **复杂性分析**：论文形式化分析了恢复时间复杂度，指出自愈路由器的恢复复杂度（Dijkstra单次运行）**不随同时故障数量（K）增加而改变**，而ReAct的恢复时间与K线性相关，LangGraph对未预编码的复合故障无法恢复。6) **规模风险暴露分析**：通过模拟不同日任务量（1万到100万）和5%工具故障率，量化了各架构的累计恢复时间、额外LLM调用和潜在的静默失败数量，突显了自愈路由器在运营成本和可观测性上的优势。所有实验均在模拟工具和确定性模拟LLM的环境中进行，验证了架构的结构属性。

### Q5: 有什么可以进一步探索的点？

论文指出了几个重要的局限性和未来方向：1) **实验环境的局限性**：所有评估基于模拟工具和确定性LLM，验证了结构属性但未在真实API延迟、错误分布和生产级LLM准确性下测试。未来需要在真实或更复杂的模拟环境中进行验证。2) **图构建成本**：当前工具图需要为每个领域手动指定。一个 promising 的方向是研究如何从工具文档或使用模式中自动构建图，解决冷启动问题。3) **模块准确性**：评估假设健康监控器（如意图分类器、风险检测器）具有完美准确性。在实际生产中，这些模块可能是存在错误率的机器学习模型。需要系统评估模块错误如何传播并影响整体系统可靠性，优先级竞争机制虽能提供一定鲁棒性，但需进一步研究。4) **更丰富的故障模式**：当前场景主要测试工具完全宕机。未来需要测试部分故障（工具返回错误数据）、延迟退化、对抗性输入等更复杂的现实故障模式。5) **扩展到多智能体系统**：本文专注于单智能体架构。未来可以探索如何将健康监控信号和工具图在多个智能体实例间共享和协调，以实现全局性的故障感知和预防性重路由，这涉及分布式一致性协议等挑战。6) **生产就绪的校准机制**：论文第2.5节提出的复合权重函数和连续校准机制是架构建议，尚未经过实证测试。未来需要实现并评估这套机制在动态生产环境中的效果。

### Q6: 总结一下论文的主要内容

这篇论文针对LLM工具使用智能体面临的可靠性-成本权衡问题，提出了一种创新的、基于图的自愈路由架构。其核心贡献在于将大部分常规的Agent控制流决策（尤其是故障恢复）重新定义为图路由问题，而非LLM推理问题。该架构通过并行健康监控器竞争优先级信号，并结合成本加权工具图与Dijkstra最短路径算法，实现了确定性的、低成本的运行时故障恢复。当工具失败时，系统能自动、快速（亚毫秒级）地重新计算并切换到备用路径，无需调用LLM。LLM仅作为最后手段，用于处理所有图路径均不可行的、需要真正推理的边界情况。通过在三个不同拓扑结构的领域（线性、DAG、并行）共19个场景上的评估，论文证明该架构在达到与ReAct相同正确性的同时，将控制平面LLM调用减少了93%，并完全消除了精心设计的静态工作流在复合故障下可能出现的静默失败。这项工作为构建高可靠、低成本的生产级LLM Agent提供了一种新的、具有坚实理论基础和良好泛化能力的工程架构。
