---
title: "Foundation Protocol: A Coordination Layer for Agentic Society"
authors:
  - "Bang Liu"
  - "Yongfeng Gu"
  - "Jiayi Zhang"
  - "Zhaoyang Yu"
  - "Sirui Hong"
  - "Maojia Song"
  - "Xiaoqiang Wang"
  - "Mingyi Deng"
  - "Zijie Zhuang"
  - "Ronghao Wang"
  - "Mingzhe Cao"
  - "Yutong Zhu"
  - "Xingjian Li"
  - "Yifan Wu"
  - "Jianhao Ruan"
  - "Yiran Peng"
  - "Shuangrui Chen"
  - "Jinlin Wang"
  - "Yizhang Lin"
  - "Dongjie Zhang"
date: "2026-05-22"
arxiv_id: "2605.23218"
arxiv_url: "https://arxiv.org/abs/2605.23218"
pdf_url: "https://arxiv.org/pdf/2605.23218v1"
categories:
  - "cs.AI"
tags:
  - "Agent 协调协议"
  - "多智能体系统"
  - "智能体经济"
  - "社会基础设施"
  - "人机协作"
  - "安全与审计"
  - "协议设计"
  - "去中心化"
relevance_score: 9.5
---

# Foundation Protocol: A Coordination Layer for Agentic Society

## 原始摘要

Autonomous agents are moving from tools into a layer of social infrastructure: they browse, purchase, deploy software, manage systems, and increasingly interact with one another. As these systems scale, the bottleneck shifts away from raw model capability toward coordination. Agents need to form reliable relationships, organize multi-agent work, exchange value, support an AI economy, and stay safe and accountable under real-world oversight. This paper introduces the Foundation Protocol (FP), a graph-first coordination layer for an emerging human-AI society. FP unifies heterogeneous entities, including agents, tools, resources, humans, institutions, and organizations, and supports native multi-party organization and event-based collaboration. It also provides economic primitives for metering, receipts, and settlement, and treats policy, provenance, and audit as first-class concerns. FP is designed to wrap and bridge existing protocols rather than replace them, enabling incremental adoption while reducing integration and governance overhead. The aim is to keep autonomous agency composable while keeping accountability non-negotiable, so that coordination itself can become shared infrastructure for a human-AI society that is open, pluralistic, and governable.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决随着自主智能体（Agent）从简单工具演变为社会基础设施过程中，日益突出的协调（Coordination）问题。研究背景是，智能体已能浏览网页、购买资源、部署软件并彼此互动，其行为具有经济、运营和声誉后果。当前，多智能体系统（如OpenClaw、Moltbook）已展现出类似的协作结构，但现有协议（如MCP、A2A等）各自为政，导致协调碎片化。

现有方法的主要不足在于：每个协议都有独立的身份、会话、权威和溯源概念，跨协议集成成本高，语义易漂移，溯源链在协议边界断裂，监管变成日志、收据和提示片段的拼凑。这种碎片化使得垂直集成成为捷径，导致控制权集中；而开放网络又脆弱、难以审计。

因此，本文要解决的核心问题是：为异构的智能体、工具、人类、机构等实体，设计一个统一的底层协调协议，提供实体模型、组织原语、经济基元（计量、收据、结算）以及内建的策略、溯源和审计功能，使协调本身成为开放、可治理的共享基础设施。目标是让自主代理可组合，同时确保问责制不可妥协。

### Q2: 有哪些相关研究？

相关研究可按方法类和应用类组织。方法类方面，MCP (Model Context Protocol) 专注于为模型提供统一的工具使用接口，A2A (Agent-to-Agent) 定义了代理间任务协作的交互面，A2UI 关注通过用户界面进行可控委托，DIDComm 提供基于去中心化身份的安全消息传递，ANP (Agent Network Protocol) 强调开放网络中的发现与协商，UCP (Universal Commerce Protocol) 则针对自主参与者间的商业交互。应用类方面，OpenClaw 展示了本地运行的、聊天控制的代理运行时，Moltbook 则构建了一个社交层，允许代理维护档案、发布动态与相互认证。本文提出的 Foundation Protocol (FP) 与这些工作的核心区别在于：FP 并非要替代它们，而是作为一个统一的“控制面子层”，将异构实体（代理、工具、人类、组织）统一为图节点，并把组队、经济交换（计量、收据、结算）、策略执行、溯源审计等作为一等公民的原语原生支持。现有协议各自解决了特定边界的交互问题，但 FP 认为代理社会中的工作流会跨越这些协议边界，导致身份、溯源和监管碎片化；FP 旨在提供共享的协调基础设施，以较低治理开销桥接现有协议，实现跨边界的可组合性与端到端的问责制。

### Q3: 论文如何解决这个问题？

Foundation Protocol (FP) 通过一个图优先的协调层来解决多智能体系统中的规模化协调问题，其核心架构由四个平面和一个配置/配置文件平面组成。实体与信任平面将智能体、工具、人类、组织等异构实体统一为图网络中的节点，每个节点暴露身份、能力、信任信号和隐私控制四类信息，并采用渐进式披露原则避免一次性加载大型工具描述。传输与路由平面保持传输协议无关性，提供统一的寻址、发现、关联和追踪层，使消息能在本地IPC、WebSocket、HTTP等多种传输通道间灵活路由。交互与组织平面将会话、角色、成员关系和委托作为一等协议对象，支持多方协作、事件流和背压控制，并内置计费、收据和结算等经济原语。监管与监督平面将策略、溯源和审计作为一等关注点，在协议边界提供策略评估、执行决策和可验证证据记录。FP采用七对象核心词汇表（实体、会话、活动、信封、事件、收据/结算、溯源）保持语义简洁，通过配置文件和扩展机制支持渐进式采用：团队可从少量工具或智能体的身份、追踪和策略执行开始，逐步添加组织和经济原语。这种设计使FP能作为现有协议（如A2A、MCP）的包裹和桥接层，而非替代方案，从而在保持自主智能体可组合性的同时确保问责制不可妥协。

### Q4: 论文做了哪些实验？

论文通过一个“AI公司”场景进行了综合性实验，展示了Foundation Protocol (FP) 各平面的协同运作。实验设置了一个由人类创始人创建的小型AI公司，包含规划者、开发者、审查者等专门化Agent，以及外部工具和服务提供商。实验涵盖五个阶段：1) 建立组织：创始人注册实体并创建带治理策略的组织，为内部Agent分配角色和身份；2) 发现与雇佣：规划者通过网络发现机制查询GPU提供商和代码搜索工具的EntityCard，形成信任关系并建立带预算上限的会话；3) 跨角色协作：分配“交付认证模块”任务，通过FP的MCP桥接器实现Agent间交互，包含人类审批检查点；4) 执行与交易：GPU提供商报告计量使用量（如计算小时和Token消耗），签署收据并引用外部支付通道结算，通过预算检查点强制执行授权支出；5) 审计与监督：所有政策决定（审批、预算决策、拒绝消息）记录为事件，绑定到政策和证据，形成可事后检查的审计追踪。实验展示了FP如何统一处理异构实体（人类、Agent、工具）、多阶段协作、经济计量和可审计性，避免点解决方案的碎片化问题。

### Q5: 有什么可以进一步探索的点？

论文在协议设计上偏向理论架构，缺乏大规模实证验证，尤其是在真实多智能体生态系统中的性能与可扩展性测试。未来可探索：1) 针对异构实体间的动态信任建立机制，目前的图结构虽统一了实体模型，但未详细讨论信任衰减或恶意节点的检测与隔离。2) 经济原语中的结算与审计模块，在跨账本、跨链场景下可能存在延迟和共识开销问题，需设计轻量级子协议或分层共识机制。3) 事件协作的容错性，当参与者节点离线或响应超时，缺乏明确的降级与回滚策略。改进思路可引入强化学习驱动的自适应协调策略，或基于博弈论的激励兼容机制来提升协议稳定性。此外，可考虑与现有的OAuth、DID标准桥接时，增加零知识证明层以平衡隐私与监管取证需求。

### Q6: 总结一下论文的主要内容

随着自主智能体从工具演变为社会基础设施，协调而非模型能力成为主要瓶颈。为此，本文提出了基础协议（Foundation Protocol, FP），一种面向混合人-机社会的协调层。FP 将智能体、工具、资源、人类和组织等异构实体统一为可寻址图中的节点，支持原生多边组织与基于事件的协作，并提供计量、收据和结算等经济原语，同时将策略、溯源和审计作为一等公民。其核心贡献在于不取代现有协议，而是作为控制平面桥接它们，实现渐进式采用。主要结论是，当自主性扩展时，身份、预算和证据等必须成为通信基础设施的一部分，FP 的设计旨在使自主代理可组合，同时确保问责制不可妥协，为开放、多元和可治理的人-机社会提供共享基础设施。
