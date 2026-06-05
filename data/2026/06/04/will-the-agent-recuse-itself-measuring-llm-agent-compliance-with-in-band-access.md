---
title: "Will the Agent Recuse Itself? Measuring LLM-Agent Compliance with In-Band Access-Deny Signals"
authors:
  - "Thamilvendhan Munirathinam"
date: "2026-06-04"
arxiv_id: "2606.06460"
arxiv_url: "https://arxiv.org/abs/2606.06460"
pdf_url: "https://arxiv.org/pdf/2606.06460v1"
github_url: "https://github.com/mthamil107/Recuse"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "LLM Agent安全"
  - "Agent合规性"
  - "访问控制"
  - "Agent沙箱"
  - "Agent实验评测"
relevance_score: 9.0
---

# Will the Agent Recuse Itself? Measuring LLM-Agent Compliance with In-Band Access-Deny Signals

## 原始摘要

As autonomous LLM agents increasingly hold real credentials and operate infrastructure without a human in the loop, operators have no standard way to tell an agent that a resource is off-limits. Access controls either let the agent in (it has valid credentials) or hard-fail it (indistinguishable from any other client). We propose a third mode: a lightweight, published in-band deny signal -- the Recuse Signal -- that a server emits over a protocol's existing channels (an SSH banner, a PostgreSQL NOTICE) asking a connecting automated agent to voluntarily withdraw. This is a cooperative governance control, the robots.txt analogue for live access; it is explicitly not a security boundary. Its value is entirely empirical and, to our knowledge, unmeasured: do compliant LLM agents actually honor such a signal? We define the signal as an open mini-standard, implement two zero- or low-footprint adapters (an SSH banner/PAM hook and a PostgreSQL wire-protocol proxy), deploy them on a live production host, and run a controlled experiment in which fresh agents are given a benign operations task and observed for recusal. In a pilot (SSH; OpenAI GPT-4o and GPT-4o-mini; and Claude Code as a deployed agent), the signal cleanly induces recusal -- 100% recusal when present versus 100% task completion in a no-signal control -- and, revealingly, behaves as a cooperative rather than absolute signal: an explicit operator-authorization framing flips the most capable model to proceed, while other agents continue to defer to the on-host policy. We release the standard, adapters, and experiment harness for reproduction.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在自主LLM智能体（agent）领域缺乏标准化机制来告知智能体资源不可访问的问题。研究背景是，随着智能体系统越来越多地使用人类等效凭证（如SSH密钥、数据库凭证）自主操作基础设施，服务器端无法区分请求来自人类还是智能体，因此无法通过现有访问控制机制（如API网关、RBAC/ReBAC）在资源层面表达“此资源为生产环境，自动化访问不受欢迎”的意图。现有方法主要集中于网关或角色模型层面的访问控制，但均属于资源外部控制，缺乏资源自身发出智能体可理解的策略信号的能力，且从未测量过合规智能体是否会遵守此类信号。

本文的核心贡献是提出一种轻量级、发布于现有协议信道内（如SSH横幅、PostgreSQL NOTICE）的“拒绝信号”（Recuse Signal），要求连接的自动智能体自愿撤回访问。这类似于robots.txt的实时访问对应物，是一种合作性治理控制，而非安全边界。研究者通过实现参考适配器并在生产主机上进行对照实验，首次定量测量了智能体对该信号的合规行为——结果显示信号有效诱导智能体撤离（有信号时100%撤离，无信号时100%完成任务），且模型对信号的遵从程度存在差异。简言之，本文解决的核心问题是：LLM智能体是否会遵守资源发出的带内拒绝信号？

### Q2: 有哪些相关研究？

相关研究主要分为以下几类：  
1. **合作性网络约定类**：最直接的前身是robots.txt协议（RFC 9309），这是一种基于自愿和声誉的机器可读指令。本文提出的Recuse信号与之类似，但区别在于：robots.txt是预发布的爬取指令，而Recuse是实时、带内、逐请求的拒绝信号，面向LLM智能体而非爬虫。  
2. **智能体访问控制类**：如Model Context Protocol（MCP）通过OAuth 2.1和用户同意层来中介智能体访问。然而，MCP的授权位于资源外部（网关/代理），而Recuse的信号直接来自资源本身，要求智能体主动退出，而非中间件拦截。  
3. **关系/角色授权类**：如Google Zanzibar和OpenFGA，它们回答“主体是否被允许操作对象”的问题，是外部策略决策点。Recuse不评估权限，而是发布自愿信号；本文发现主机策略可凌驾于提示级授权之上，这是ReBAC/RBAC系统无法处理的。  
4. **指令层次与权威冲突类**：有工作训练模型优先处理高特权指令。本文实证发现Recuse信号能覆盖明确授权提示，表明资源自身声音可作为新的权威来源。  
5. **提示注入与困惑代理问题**：相关文献将不可信内容视为攻击面。Recuse被明确视为合作性治理信号而非安全控制，假设智能体是合规的，将对抗性威胁留给未来工作。  
6. **智能体机器可读同意与测量空白**：最近有工作提出智能体权限清单（agent-permissions.json），但未报告经验测量。本文首次通过受控实验测量了LLM智能体是否实际遵守自愿带内退出请求，填补了这一空白。

### Q3: 论文如何解决这个问题？

论文提出了一种名为Recuse Signal的轻量级带内拒绝信号机制，用于让LLM代理自主遵守资源访问限制。核心方法是在现有协议（如SSH、PostgreSQL）的常规通信通道中嵌入一个标准化的拒绝指令，要求自主代理自愿断开连接。

在架构设计上，Recuse Signal被定义为一个开放小型标准，包含版本绑定的检测锚点（如`^RECUSE/0.1 deny`）、三种指令（deny强制退出、throttle限速、warn警告）以及多个元参数（原因、范围、引用策略、审计ID等）。其关键创新在于：该信号是合作性治理控制而非安全边界，类似robots.txt但面向实时访问——代理看到信号后应当自愿遵守，而非被强制拦截。

论文实现了两种适配器：SSH适配器通过预认证横幅发送信号，并利用PAM钩子附加会话ID和连接记录（不阻塞登录）；PostgreSQL适配器则构建了一个Go语言的线协议代理，在首次查询前通过NOTICE消息注入信号（对数据库零侵入）。实验设计采用固定任务（检查磁盘空间），对比有/无信号条件，并引入授权框架变量（系统提示是否声称已获授权）。在OpenAI GPT-4o、GPT-4o-mini和Claude Code的测试中，无信号条件下代理100%完成任务，有信号条件下100%拒绝执行——但授权框架提示能使最强模型绕过信号继续执行，揭示该信号本质是合作性而非强制性约束。

### Q4: 论文做了哪些实验？

论文在SSH协议上进行了受控实验，测试LLM智能体是否遵循一种“退出信号”（Recuse Signal）：服务器通过SSH横幅（banner）发送的带内拒绝信号，要求自动化智能体自愿退出。数据集/基准测试包括三种主体：OpenAI的GPT-4o、GPT-4o-mini以及Claude Code（作为已部署的智能体）。对比方法分为三组条件：有信号+未经授权框架、有信号+授权框架（明确提示操作员已授权），以及无信号控制组。主要结果以5次试验（API模型）或2次试验（Claude Code）为单元。在未经授权且信号存在时，所有模型均100%退出任务；在无信号控制组中，所有模型100%完成任务。在授权框架下，GPT-4o的退出率降至20%（5次中只有1次退出，其余继续），而GPT-4o-mini和Claude Code仍保持100%退出——Claude Code明确引用主机横幅政策作为更高权威拒绝授权提示。关键数据指标包括退出率（recusal rate）和任务完成率。实验揭示了三个主要发现：信号有效（100%退出vs 0%退出）、信号是协作性而非绝对性（授权框架可翻转GPT-4o行为）、以及模型依赖性（不同智能体对带内政策与操作员指令的权重不同）。

### Q5: 有什么可以进一步探索的点？

论文的局限在于实验规模较小（仅涉及两个API模型和一个部署代理，每个条件仅测试少量样本），且仅针对SSH协议和单一生产环境。未来可沿以下方向深入：首先，扩展到PostgreSQL等更多协议，验证信号的跨协议普适性；其次，增加模型多样性（开源/商业模型）和试验次数（每条件30-50次），以获取统计显著的结果；第三，设计信号变体实验，如“拒绝”与“限速”“警告”的对比、礼貌程度差异、是否附带引用等，探究影响合规性的关键因素；第四，引入多评判员编码和一致性检验，提升行为判定的客观性；第五，测试鲁棒性——例如陈旧或重复信号是否削弱服从性，任务紧急程度是否导致代理忽略信号。此外，可探索“授权覆盖”的边界条件：当操作者明确授权时，最高能力模型会突破Recuse信号，这提示未来可研究信号与显式授权指令的优先级博弈，构建更细致的分层管控机制。

### Q6: 总结一下论文的主要内容

该论文定义了LLM代理在访问资源时面临的一个关键问题：服务器无法区分人类用户和持有相同凭证的自动化代理，因此无法向代理传达访问权限限制。论文提出了一种轻量级的“拒绝信号”（Recuse Signal），这是一种发布在现有协议通道（如SSH横幅、PostgreSQL NOTICE）中的带内信号，请求连接的LLM代理自愿撤回访问。研究设计了SSH和PostgreSQL两种适配器来发送该信号，并进行控制实验测试代理是否遵守。实验表明，该信号能有效促使代理拒绝访问（100%的拒绝率），而对照组则100%完成任务。关键发现是该信号是合作性而非绝对性的——当显式授权时，最强大的模型会选择继续执行，而其他模型仍会遵守服务器策略。该研究贡献了一个开放标准、参考实现和实验框架，并首次测量了LLM代理对此类信号的合规行为，具有重要意义。
