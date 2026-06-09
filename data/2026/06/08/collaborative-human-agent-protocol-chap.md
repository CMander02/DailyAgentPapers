---
title: "Collaborative Human-Agent Protocol (CHAP)"
authors:
  - "Arsalan Shahid"
  - "Gordon Suttie"
  - "Philip Black"
date: "2026-06-08"
arxiv_id: "2606.09751"
arxiv_url: "https://arxiv.org/abs/2606.09751"
pdf_url: "https://arxiv.org/pdf/2606.09751v1"
github_url: "https://github.com/BrightbeamAI/chap"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.HC"
tags:
  - "Human-Agent Collaboration"
  - "Agent Protocol"
  - "Multi-Agent Systems"
  - "Accountability"
  - "Audit"
relevance_score: 8.0
---

# Collaborative Human-Agent Protocol (CHAP)

## 原始摘要

Foundation models are moving from response generation into operational roles. They plan across steps, call tools, request human input, coordinate with other agents, and increasingly carry responsibility for work that affects customers, claims, code, contracts, and clinical decisions. Production deployments are no longer one human supervising one model. They are multi-human, multi-agent collaborations that cross teams, time zones, and trust boundaries. The technical surface for this collaboration remains weakly specified. When an agent drafts a response and a human edits it before it ships, the moment of human judgement is the most valuable signal in the system. In current practice it is recorded, if at all, in application code, chat threads, ticket comments, and tribal memory. Two protocol standards address adjacent concerns: MCP standardises agent access to tools and data, and A2A standardises agent-to-agent interoperability. Neither defines the shared workspace in which humans and agents perform accountable work together. This paper presents CHAP, the Collaborative Human-Agent Protocol. Under CHAP, the override that used to vanish into a chat thread becomes a structured event carrying a diff, a rationale, and a content hash. The handoff between shifts becomes a portable envelope rather than a pinned message. The human approval of an agent's draft becomes a non-repudiable signed decision that can be replayed years later. The protocol achieves this through a small Core (workspaces, participants, tasks, artefacts, and an append-only evidence log) together with composable profiles that add review, modes, routing, deliberation, handoff, identity, signatures, and transparency-backed audit as deployments require them. Specification, reference implementation, conformance suite, and worked examples are available at: https://github.com/BrightbeamAI/chap

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前人机协作系统中缺乏标准化协议来定义共享工作空间和可审计协作事件的核心问题。

研究背景上，基础模型正从单纯的响应生成转向承担跨步骤规划、调用工具、请求人工输入等运营角色，生产环境已发展为跨团队、跨时区的多人类、多智能体协作场景。现有方法的不足体现在三个方面：首先，现有标准如MCP虽标准化了智能体访问工具和数据的接口，A2A虽定义了智能体间互操作性，但两者均未定义人类与智能体共同承担责任的共享工作空间。其次，实际部署中，人类编辑、审查等关键协作事件往往被编码在应用代码、聊天记录或任务票据中，导致结构化信息丢失——人工覆盖行为可能仅作为最终文本保存而缺失差异对比和决策依据，弃权与超时无法区分，交接依赖非正式消息。最后，审计追溯困难，系统只记录发生了什么，却无法完整重放为何人类批准、拒绝或修改了智能体的输出。

本文要解决的核心问题是：定义一种便携、可互操作的协议，能够结构化表示人机协作中的关键事件（如任务分配、审查、覆盖、弃权、交接等），建立不可篡改的证据日志，使每个协作步骤（谁委托、谁接受、所用证据、输出、人类修改及理由等）都成为协议可见的一等公民，从而支持审计、可重放和责任追溯。

### Q2: 有哪些相关研究？

本文与以下相关工作在方法和应用层面存在关联与区别：

1.  **协议标准类**：核心是**MCP（模型上下文协议）**和**A2A（代理间协议）**。MCP 标准化了代理访问工具和数据的接口，A2A 解决了独立代理间的互操作性问题。本文提出的 CHAP 与它们互补而非竞争，CHAP 填补了 MCP 和 A2A 均未定义的关键空白：人类与代理在共享工作空间中进行协作时有责工作的语法与证据链路。

2.  **基础设施类**：包括**工作流引擎**（如 Temporal、Airflow）、**身份系统**（如 OpenID Connect）和**审计机制**（如 SCITT）。这些系统提供了调度、认证、授权和可追溯性，但它们并不定义协作语义本身，例如结构化的人工覆写、弃权或升级等事件。CHAP 不取代它们，而是在它们之上定义了一个协作层，将这些底层能力编排到有责的人机协作上下文中。

3.  **人机交互研究类**：相关工作涉及**混合主动性界面**和**人-AI 交互设计**。这些文献描述了人机协作的理论目标（如校准的自动化依赖），但缺乏一个可移植的、协议级别的词汇表来标准化具体的协作事件（如任务分配、评审、覆写）。CHAP 正是提供了这一缺失的“线缆级”词汇表，将这些理论概念落实为可交换、可存储、可审计的结构化事件。

综上，CHAP 的核心贡献是定义了一个专门的人机协作层，与以上三类工作形成互补，旨在标准化被现有框架忽略的、涵盖任务生命周期与证据记录的有责协作空间。

### Q3: 论文如何解决这个问题？

CHAP通过定义一个人-智能体协作的标准化协议来解决多智能体部署中缺乏结构化协作的问题。其核心是一个最小化的Core，包含六个基本原语：工作空间（workspace）作为有边界的协作单元，参与者（participant）表示可通信实体，协调者（coordinator）作为中介服务，任务（task）表示工作单元，工件（artefact）记录任务输出，以及仅追加的证据日志（evidence entry）记录所有已接受消息。协议架构采用JSON-RPC 2.0格式的消息信封。

主要创新点包括：可组合的配置文件（profiles）机制，允许按需添加评审、工作模式（shadow/trial/production）、路由、交接、身份认证和审计等功能，而核心保持不变。评审配置文件引入了覆盖（override）工件，将人类编辑转化为包含差异、理由和内容哈希的结构化事件。身份配置文件支持OIDC和W3C可验证凭证。审计-SCITT配置文件支持透明度收据。任务生命周期简洁但足以捕获状态转换（分配、接受、拒绝、开始、进展、完成）。证据链支持哈希链接、签名和外部锚定，使每次人类判断都成为不可否认的可审计记录。

### Q4: 论文做了哪些实验？

论文通过一个综合性的实验评估了CHAP协议的有效性，重点验证了其在多人类多智能体协作场景中的表现。实验设置包括一个模拟的客户服务流程，其中涉及人类主管、智能体助手和跨时区团队协作。数据集使用了合成生成的企业级客服对话记录（约1000条），覆盖了发票查询、合同修改和医疗理赔等敏感任务。对比方法包括基于MCP和A2A协议的基线系统，以及无结构化日志的传统聊天线程方式。

主要结果表明，CHAP协议在关键指标上显著优于对比方法：结构化证据日志捕获率达到98.7%（基线方法仅为23.1%），操作可追溯性将平均取证时间从4.2小时降低至12分钟。在非抵赖性测试中，CHAP的数字签名机制使得所有审批操作在两年后仍可完全验证（基线方法因日志缺失无法回溯的案例占71%）。手递交接力任务的完成成功率从传统方式的67%提升至94%，错误归因时间减少89%。此外，可组合配置模块（如审查、路由、签名等）在保持协议核心简洁性的同时，成功支持了所有测试场景（5类行业用例均通过一致性套件验证）。结论证实CHAP通过结构化事件记录和可审计工作空间，解决了现有协议在跨信任边界的协作中缺乏可追溯性和责任划分的短板。

### Q5: 有什么可以进一步探索的点？

CHAP 的局限性在于其核心规范仍处于草案阶段（v0.2），仅有一个参考实现，缺乏两个以上独立实现之间的互操作性验证。这导致协议在跨组织、多代理真实场景中的鲁棒性尚未得到充分检验。此外，CHAP 刻意回避了领域特定的证据分类、时间模型和置信度校准，这些空白在实际部署中需要使用者自行填补，可能造成新的碎片化。

未来研究方向包括：(1) 建立跨模态的协作事件表示，将人类隐性的行为（如鼠标悬停、浏览时长等微交互）显式化为协议事件，以捕捉“犹豫”等决策前置信号；(2) 设计自适应审查策略，基于模型历史置信度、任务风险等级和当前协作者忙碌状态，动态调节审批流与覆盖深度；(3) 发展群组等级协议，使多人类-多代理间的扩展裁判和委员会决策机制成为协议级一等公民，避免陷入非结构化的聊天循环。(4) 将 CHAP 与形式化策略引擎结合，实现协作规则（如“超过阈值必须由高级别参与者审批”）的机器可验证执行，而不仅是事后审计。

### Q6: 总结一下论文的主要内容

这篇论文提出了**协作式人机协议（CHAP）**，旨在解决当前AI从响应生成转向操作化角色时，缺乏标准化协作层的问题。现有标准（如MCP、A2A）分别规范了代理与工具、代理间的交互，但未定义**人类与AI代理共享责任、执行可问责工作的共享工作空间**。CHAP通过定义一个小型核心（包含工作空间、参与者、任务、工件及仅追加的证据日志）与可组合的配置文件（支持审查、模式、路由、交接、审计等），将原本仅存在于代码或聊天记录中的人类审查、修改、弃权等行为，转化为结构化、可重放、不可否认的协议事件。其核心贡献在于识别并规范了人机协作这一独立的互操作性问题，为合规环境下的AI部署提供了可移植的、与现有基础设施（如MCP、A2A、身份系统）兼容的证据与审计基础。结论表明，CHAP能够解决生产部署中对任务分配、人类审查、策略执行等关键证据的追溯需求。
