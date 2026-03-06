---
title: "Jagarin: A Three-Layer Architecture for Hibernating Personal Duty Agents on Mobile"
authors:
  - "Ravi Kiran Kadaboina"
date: "2026-03-05"
arxiv_id: "2603.05069"
arxiv_url: "https://arxiv.org/abs/2603.05069"
pdf_url: "https://arxiv.org/pdf/2603.05069v1"
categories:
  - "cs.AI"
  - "cs.HC"
  - "cs.MA"
tags:
  - "Agent Architecture"
  - "Mobile Agent"
  - "Personal Agent"
  - "Agent Deployment"
  - "On-Device AI"
  - "Agent Wake/Sleep"
  - "Agent Communication"
  - "Agent-Centric Design"
relevance_score: 8.5
---

# Jagarin: A Three-Layer Architecture for Hibernating Personal Duty Agents on Mobile

## 原始摘要

Personal AI agents face a fundamental deployment paradox on mobile: persistent background execution drains battery and violates platform sandboxing policies, yet purely reactive agents miss time-sensitive obligations until the user remembers to ask. We present Jagarin, a three-layer architecture that resolves this paradox through structured hibernation and demand-driven wake. The first layer, DAWN (Duty-Aware Wake Network), is an on-device heuristic engine that computes a composite urgency score from four signals: duty-typed optimal action windows, user behavioral engagement prediction, opportunity cost of inaction, and cross-duty batch resonance. It uses adaptive per-user thresholds to decide when a sleeping agent should nudge or escalate. The second layer, ARIA (Agent Relay Identity Architecture), is a commercial email identity proxy that routes the full commercial inbox -- obligations, promotional offers, loyalty rewards, and platform updates -- to appropriate DAWN handlers by message category, eliminating cold-start and removing manual data entry. The third layer, ACE (Agent-Centric Exchange), is a protocol framework for direct machine-readable communication from institutions to personal agents, replacing human-targeted email as the canonical channel. Together, these three layers form a complete stack from institutional signal to on-device action, without persistent cloud state, continuous background execution, or privacy compromise. A working Flutter prototype is demonstrated on Android, combining all three layers with an ephemeral cloud agent invoked only on user-initiated escalation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决个人AI代理在移动设备上部署时面临的根本性矛盾：持续后台运行会耗尽电量并违反平台沙盒策略，而纯粹被动响应的代理又会错过有时效性的义务，直到用户想起来询问。研究背景是，尽管个人AI代理管理日常义务（如保险续订、处方补充）的前景被广泛认可，但现有系统存在严重不足。

现有方法主要基于截止日期的简单提醒，未能回答“此刻不行动对特定用户的具体成本是什么”这一核心问题。其不足体现在四个方面：1) **执行模型不匹配**：持续后台代理违反移动操作系统（如iOS App Nap、Android Doze）的节能限制，而现有框架未能在系统允许的唤醒窗口内智能决策何时行动有价值；2) **冷启动依赖**：智能代理需要结构化的义务数据，但用户不会手动输入这些信息，导致代理缺乏推理基础；3) **通信层不匹配**：机构通信（如邮件）为人类设计，代理无法从中自动提取截止日期、最优操作窗口等机器可读信息；4) **对齐错位**：由机构部署的代理优先考虑机构利益而非用户价值，且多个独立代理会无协调地争夺用户注意力。

因此，本文要解决的核心问题是：如何设计一个移动个人代理架构，使其能在不持续后台运行、不依赖手动数据输入、不损害隐私的前提下，主动且适时地管理用户的时效性义务，并真正以用户价值为优化目标。论文通过提出名为Jagarin的三层架构来系统性地解决上述所有问题。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕移动个人代理的部署挑战展开，可分为以下几类：

**1. 移动代理执行与唤醒机制**：现有移动平台（如Android的WorkManager、iOS的BGTaskScheduler）提供了受控的后台任务调度框架，但缺乏对“何时唤醒代理执行任务最具价值”的建模。Jagarin的DAWN层在此基础上，引入了多信号启发式算法（如义务类型窗口、用户行为预测），动态计算唤醒紧迫性，解决了纯截止日期提醒的不足。

**2. 义务数据自动获取与处理**：传统个人代理依赖用户手动输入结构化义务数据，导致冷启动问题。ARIA层通过商用邮箱身份代理，自动分类并路由商业邮件（如续订通知、促销信息），与依赖人工录入或单一应用内数据的方案相比，实现了零配置的义务发现。

**3. 人机通信协议与代理对齐**：现有机构通信（如HTML邮件）面向人类设计，机器可读性差。ACE层提出了直接面向代理的通信协议框架，区别于传统电子邮件或API（如日历协议），旨在实现机构到个人代理的结构化信息传递。同时，Jagarin强调用户侧部署与价值对齐，与机构自建的代理（如银行或零售应用内代理）形成对比，后者往往以机构利益为中心且缺乏跨代理协调。

**4. 系统架构与隐私保护**：Jagarin采用分层、无持久云状态的架构，与依赖持续云端后台执行的个人代理方案不同，它通过本地计算与按需唤醒来平衡功能与隐私、能耗及平台限制，体现了在移动设备资源约束下的新颖设计思路。

### Q3: 论文如何解决这个问题？

论文通过一个名为Jagarin的三层架构来解决移动设备上个人AI代理的部署悖论。该架构的核心思想是让代理在大部分时间处于休眠状态，仅在必要时被智能唤醒，从而平衡了持久执行的需求与设备资源限制之间的矛盾。

整体框架由三个垂直集成但可独立分离的层次构成：DAWN、ARIA和ACE。DAWN层是一个部署在设备端的启发式引擎，作为系统的“大脑”。它通过计算一个综合紧急度分数来决定何时唤醒休眠的代理。这个分数综合了四个关键信号：基于任务类型的最佳行动窗口、用户行为参与度预测、不作为的机会成本以及跨任务批量处理的协同效应。DAWN采用自适应的用户特定阈值来判断是向用户发出轻量提醒，还是需要将任务升级处理。其设计确保了极低的开销，由设备调度器每15分钟唤醒一次，推理过程耗时少于50毫秒，完全避免了持续的后台执行。

ARIA层是一个商业电子邮件身份代理，充当了系统的“感知器官”。它解决了代理的冷启动和数据输入问题。该组件将用户的完整商业收件箱（包括义务通知、促销优惠、忠诚度奖励和平台更新）按消息类别路由到相应的DAWN处理器。这自动化了数据摄取过程，无需用户手动输入，并为代理提供了丰富的上下文信息。

ACE层则是一个面向未来的协议框架，旨在成为机构与个人代理之间机器可读通信的规范通道，以取代传统的人类目标电子邮件。它代表了从源头改进信号质量的长期解决方案。

该架构的关键创新点在于其整体的隐私和效率设计：所有任务状态都加密存储在设备本地，没有持久的云端状态；云端代理仅在用户显式点击“升级”时才会被调用，确保了没有用户操作就不会上传数据；同时，整个系统完全遵守iOS和Android的平台后台任务限制。这三个层次共同构成了一个从机构信号到设备端行动的完整技术栈，在无需持续后台运行或牺牲隐私的前提下，实现了代理的“结构化休眠”和“按需唤醒”。

### Q4: 论文做了哪些实验？

论文在Android平台上实现了一个名为Jagarin的研究原型系统，并进行了功能演示和性能评估。实验设置包括：移动端使用Flutter/Dart开发，DAWN引擎为纯Dart实现；后台执行采用Android WorkManager（15分钟周期任务）和Firebase云消息（即时唤醒）；数据存储使用Hive加密数据库。ARIA后端用Python/FastAPI构建，包含关键词解析和Gemini 2.5 Flash模型进行邮件结构化提取。云端智能体仅在用户点击“升级到云端智能体”时被无状态调用。

数据集/基准测试方面，系统处理了来自商业收件箱的真实义务邮件，实现了12种义务类型（如保险续保、处方补充、车辆服务等）。通过ARIA代理将邮件按类别路由至相应处理器，消除了冷启动问题。

对比方法主要针对传统持续后台执行的个人智能体方案。Jagarin通过结构化休眠和按需唤醒机制，避免了持续后台执行导致的电量消耗和平台沙箱策略违规。

主要结果和关键指标包括：DAWN引擎每次完整评估周期耗时小于50毫秒；系统在无持久云状态、无持续后台执行、不泄露隐私的前提下，实现了从机构信号到设备端行动的完整栈。用户界面可清晰展示义务的三态列表（休眠/提醒/立即行动）及DAWN分数分解。云端智能体在仅接收义务上下文的情况下，能生成推荐、行动点和草稿消息，并在交付响应后自我终止。

### Q5: 有什么可以进一步探索的点？

该论文提出的三层架构在解决移动端智能体持续运行与资源消耗的矛盾方面具有创新性，但其局限性和未来探索方向仍值得深入。首先，DAWN层的启发式引擎依赖规则化的参与度预测模型，个性化训练需要足够的用户交互历史，存在冷启动问题。未来可探索利用联邦学习或小样本学习技术，在保护隐私的前提下加速模型个性化。其次，ARIA层依赖商业邮件代理，虽解决了数据输入问题，但可能受限于邮件格式的标准化程度。未来可扩展支持更多通信协议（如即时消息、API回调），并研究自然语言处理技术以更精准地解析非结构化义务信息。此外，ACE协议框架的落地依赖机构方的采纳，需进一步探索激励机制或行业标准推广策略。从系统优化角度，可研究动态资源调度算法，使DAWN的唤醒决策不仅基于义务紧急度，还能结合设备实时电量、网络状态等上下文。最后，论文强调用户对齐的设计理念，但如何确保复杂场景下（如多代理协作）的用户控制与透明度，仍需设计更细粒度的授权与解释机制。

### Q6: 总结一下论文的主要内容

论文针对移动端个人AI代理面临的后台持续运行耗电与平台沙盒策略限制的矛盾，提出Jagarin三层架构，通过结构化休眠与按需唤醒实现高效运行。核心贡献在于：第一，DAWN层作为设备端启发式引擎，综合任务类型最佳行动窗口、用户行为预测、不作为机会成本及跨任务批量共振四个信号计算紧迫度，以自适应阈值决定代理何时提醒或升级处理；第二，ARIA层作为商业邮件代理，将收件箱邮件按类别路由至对应DAWN处理器，消除冷启动与手动输入；第三，ACE层定义机构与个人代理间机器可读通信协议，旨在取代传统邮件。三者构成从机构信号到设备端行动的完整栈，无需持久云状态、连续后台运行或隐私妥协。论文通过Android原型验证了架构可行性，为下一代个人AI代理提供了可部署的解决方案。
