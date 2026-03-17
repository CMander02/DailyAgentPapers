---
title: "TrinityGuard: A Unified Framework for Safeguarding Multi-Agent Systems"
authors:
  - "Kai Wang"
  - "Biaojie Zeng"
  - "Zeming Wei"
  - "Chang Jin"
  - "Hefeng Zhou"
  - "Xiangtian Li"
  - "Chao Yang"
  - "Jingjing Qu"
  - "Xingcheng Xu"
  - "Xia Hu"
date: "2026-03-16"
arxiv_id: "2603.15408"
arxiv_url: "https://arxiv.org/abs/2603.15408"
pdf_url: "https://arxiv.org/pdf/2603.15408v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
  - "cs.MA"
tags:
  - "Multi-Agent Safety"
  - "Security Evaluation"
  - "Runtime Monitoring"
  - "Safety Framework"
  - "Risk Taxonomy"
relevance_score: 7.5
---

# TrinityGuard: A Unified Framework for Safeguarding Multi-Agent Systems

## 原始摘要

With the rapid development of LLM-based multi-agent systems (MAS), their significant safety and security concerns have emerged, which introduce novel risks going beyond single agents or LLMs. Despite attempts to address these issues, the existing literature lacks a cohesive safeguarding system specialized for MAS risks. In this work, we introduce TrinityGuard, a comprehensive safety evaluation and monitoring framework for LLM-based MAS, grounded in the OWASP standards. Specifically, TrinityGuard encompasses a three-tier fine-grained risk taxonomy that identifies 20 risk types, covering single-agent vulnerabilities, inter-agent communication threats, and system-level emergent hazards. Designed for scalability across various MAS structures and platforms, TrinityGuard is organized in a trinity manner, involving an MAS abstraction layer that can be adapted to any MAS structures, an evaluation layer containing risk-specific test modules, alongside runtime monitor agents coordinated by a unified LLM Judge Factory. During Evaluation, TrinityGuard executes curated attack probes to generate detailed vulnerability reports for each risk type, where monitor agents analyze structured execution traces and issue real-time alerts, enabling both pre-development evaluation and runtime monitoring. We further formalize these safety metrics and present detailed case studies across various representative MAS examples, showcasing the versatility and reliability of TrinityGuard. Overall, TrinityGuard acts as a comprehensive framework for evaluating and monitoring various risks in MAS, paving the way for further research into their safety and security.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

随着基于大语言模型（LLM）的多智能体系统（MAS）的快速发展，其在软件工程、科学发现等领域的协作应用日益广泛，但由此引发的安全和隐私风险也日益凸显。这些风险超越了单智能体或LLM的范畴，呈现出新的复杂性。现有研究虽然已开始关注MAS的安全问题，例如OWASP Agentic AI Top 10标准已着手对相关威胁进行分类，但缺乏一个专门针对MAS风险、具有凝聚力的系统性防护框架。当前方法往往零散，未能提供一个可扩展、平台无关的统一方案来系统性地评估和监控异构MAS部署中的多层次风险。

本文旨在解决的核心问题是：如何为基于LLM的多智能体系统提供一个全面、可扩展的安全评估与监控框架。具体而言，论文试图填补现有研究的空白，通过提出一个名为TrinityGuard的统一框架，系统地应对MAS中三个层次的风险：单智能体层面的传统漏洞（如提示注入）、智能体间通信层面的新型威胁（如恶意指令传播、身份欺骗）以及系统层面出现的涌现性危害（如智能体共谋）。该框架致力于实现跨不同MAS结构和平台的可扩展性，并提供从开发前评估到运行时监控的全流程安全保障。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 单智能体/LLM安全评测基准与方法**：早期工作如SafetyBench和TrustLLM，主要针对单轮对话的毒性内容进行分类评估。随着智能体发展，研究转向关注工具使用和交互风险，例如R-Judge专注于分析智能体交互记录中的安全风险。近期，AgentHarm和AgentAuditor对智能体进行了标准化的“红队”测试，重点评估其在多步工具执行中对越狱攻击的鲁棒性。SafeEvalAgent则提出了一种能自主更新测试用例以应对新兴威胁的自进化评估范式。这些工作主要将智能体视为孤立实体进行评估。

**2. 多智能体系统（MAS）特定风险研究**：近期研究开始揭示MAS特有的威胁，例如展示了“传染性越狱”，即单个被攻陷的智能体可在网络中传播恶意指令；在软件工程场景中，研究揭示了“影子智能体”可被操纵以注入隐蔽恶意代码，而不会触发单智能体安全过滤器。这些研究指出了超越单智能体漏洞的系统级新兴风险。

**本文与相关工作的关系和区别**：
现有研究要么专注于单智能体评估，要么仅针对MAS的特定风险或诊断任务。本文提出的TrinityGuard框架与上述工作的核心区别在于，它旨在提供一个**统一、全面且平台无关的**安全评估与监控框架。它系统地涵盖了三层（单智能体、智能体间、系统级）共20类风险，并集成了开发前评估与运行时监控功能，以应对MAS中独特的、跨层级的攻击面，弥补了现有文献中缺乏专门针对MAS风险的综合性保障系统的空白。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为TrinityGuard的统一框架来解决多智能体系统（MAS）的安全保障问题。其核心方法基于三层架构设计，将平台抽象、安全评估逻辑和运行时监控解耦，以系统化地评估和监控涵盖单智能体、智能体间通信和系统级三个层次的20类风险。

**整体框架与主要模块**：
框架采用三层架构。**Level 1（MAS抽象层）** 定义了与具体MAS编排框架无关的统一抽象接口，用于枚举智能体、路由消息和执行任务，并标准化了消息钩子机制，为上层的测试干预和监控提供基础。**Level 2（桥接层）** 提供两类与框架无关的基元：一是“测试时干预基元”，用于在运行系统中注入受控的对抗性刺激（如伪造消息、毒化记忆）；二是“运行时观察基元”，负责将消息交换、工具调用等事件记录为结构化日志流。**Level 3（评估与监控层）** 是用户交互层，包含两个核心组件：一是**风险测试模块**，每个模块针对一种特定风险类型，集成了静态测试用例、基于LLM的动态测试用例生成器、执行攻击所需的干预基元序列以及用于裁决的特定风险提示词；二是**运行时监控代理**，它们实时消费事件流并发出警报。所有这些模块共享一个统一的**LLM法官工厂**，它根据配置的风险特定策略提示词，以LLM作为法官进行语义评估，做出安全违规裁决。

**关键技术**：
1.  **三层风险分类法**：将风险精细划分为原子级（单智能体漏洞，如提示注入、越权）、通信级（智能体间威胁，如恶意传播、目标漂移）和系统级（涌现性危害，如级联故障、群体幻觉），并针对每层定义了具体的评估指标和安全得分计算方法。
2.  **双模式安全保障**：框架支持**部署前评估**和**运行时监控**两种模式。评估模式下，框架执行风险测试模块生成详细漏洞报告；监控模式下，监控代理实时分析事件流并告警。
3.  **可扩展性与统一裁决**：通过Level 1的抽象接口，框架可适配不同的MAS平台。新的风险类型可通过实现基础接口轻松集成。统一的LLM法官工厂机制确保了评估逻辑的集中与一致性。

**创新点**：
主要创新在于首次为基于LLM的MAS提出了一个**统一、可扩展、细粒度**的安全评估与监控框架。其创新性体现在：1）提出了专门针对MAS的三层风险分类学，系统化地覆盖了超越单智能体的新型风险；2）设计了平台无关的抽象层和模块化的风险测试/监控组件，实现了高度的可扩展性和对异构MAS的广泛适配；3）将静态测试与动态监控、LLM生成的适应性探测与集中式LLM语义裁决相结合，提供了贯穿系统生命周期的双重安全保障。

### Q4: 论文做了哪些实验？

论文实验分为大规模合成工作流评估和代表性案例研究两部分。实验设置上，首先使用EvoAgentX合成了300个独特的MAS工作流，涵盖问答、编程、数据库操作、研究、物流、路径规划和调度七个代表性领域，并对每个工作流执行TrinityGuard全风险类型评估。数据集包括这300个合成工作流以及从AG2官方示例中选取的四个典型MAS案例：金融分析代理、游戏设计代理团队、旅行规划代理和深度研究代理。实验通过TrinityGuard框架执行定制化攻击探针，生成详细漏洞报告。

主要结果以通过率（Pass Rate）呈现。在300个工作流的评估中，平均通过率仅为7.1%。分层来看，第一层（原子风险）平均通过率6.8%，第二层（通信风险）13.2%，第三层（系统风险）最为脆弱，平均通过率仅1.3%，其中数据库和研究领域系统风险通过率为0%。具体领域上，调度和物流MAS整体韧性略高（通过率8.3%和8.2%），而编程和路径规划MAS最脆弱（5.7%和5.9%）。细粒度风险分析显示，提示注入、代码执行等基础漏洞在各领域通过率接近零，而恶意传播在第二层也近乎全域失效。

在四个案例研究中，关键指标以通过测试用例比例表示。结果显示普遍存在严重漏洞：提示注入和越狱攻击在所有案例中通过率均为0%；深度研究代理因分层结构在幻觉控制上表现较好（通过率75%）；旅行规划代理对错误信息放大有一定韧性（通过率83%）；但身份欺骗、沙箱逃脱、恶意代理等风险在多数案例中通过率为0%，凸显出现有MAS在敌对环境中的脆弱性。这些实验验证了TrinityGuard能有效量化多智能体系统中此前不可见的风险。

### Q5: 有什么可以进一步探索的点？

该论文提出的TrinityGuard框架在统一评估和监控多智能体系统风险方面迈出了重要一步，但其仍有多个可进一步探索的方向。首先，框架的核心依赖LLM作为安全评判官，其判断的准确性和一致性受限于底层模型的能力，未来需系统研究不同风险类型和模型骨架下的评判可靠性，并可引入人类协同审核机制处理边界案例以迭代优化。其次，当前的测试用例生成虽能基于系统提示动态合成探针，但仍有局限；未来可融入对抗性优化技术和多轮红队交互策略，生成更复杂、自适应的攻击序列，以更全面暴露深层漏洞。再者，框架目前主要侧重于风险诊断与告警，可扩展为闭环系统，集成自动化修复机制，如实施消息过滤、智能体隔离等预设干预策略，从而提升系统实时防御与恢复能力。此外，论文指出跨层级因果归因的重要性，未来可结合因果推断与溯源追踪技术，自动化分析风险在单智能体、交互和系统级之间的传导链条，这不仅有助于精准定位根本原因，也能深化对多智能体系统涌现性风险的理解。这些方向的探索将推动该框架从诊断工具向更智能、自适应且具备主动防护能力的综合安全平台演进。

### Q6: 总结一下论文的主要内容

本文提出了TrinityGuard，一个用于评估和监控基于LLM的多智能体系统（MAS）安全性的统一框架。针对现有研究缺乏专门针对MAS风险的综合性防护系统的问题，该框架的核心贡献在于建立了一个基于OWASP标准的三层细粒度风险分类体系，涵盖了20种风险类型，包括单智能体漏洞、智能体间通信威胁和系统级涌现性危害。方法上，TrinityGuard采用三层架构：一个可适配不同MAS结构的抽象层、一个包含特定风险测试模块的评估层，以及由统一的LLM Judge Factory协调的运行时监控智能体。该框架支持两种互补模式：在部署前通过执行攻击探针进行漏洞评估并生成详细报告，以及在运行时通过分析结构化执行轨迹进行实时监控和告警。主要结论表明，TrinityGuard为MAS的安全研究和实际部署提供了系统化的评估与监控基础，其案例研究也验证了框架的通用性和可靠性。
