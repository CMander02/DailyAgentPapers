---
title: "What If Prompt Injection Never Left? Exploring Cross-Session Stored Prompt Injection in Agentic Systems"
authors:
  - "Yuanbo Xie"
  - "Tianyun Liu"
  - "Yingjie Zhang"
  - "Suchen Liu"
  - "Yulin Li"
  - "Liya Su"
  - "Tingwen Liu"
date: "2026-06-03"
arxiv_id: "2606.04425"
arxiv_url: "https://arxiv.org/abs/2606.04425"
pdf_url: "https://arxiv.org/pdf/2606.04425v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent安全"
  - "提示注入"
  - "跨会话攻击"
  - "持久化威胁"
  - "沙盒评估"
  - "基准测试"
relevance_score: 8.5
---

# What If Prompt Injection Never Left? Exploring Cross-Session Stored Prompt Injection in Agentic Systems

## 原始摘要

Modern agentic systems transform LLMs from session-bounded assistants into stateful systems that persist and evolve shared world state across sessions through memories, filesystems, tools, and other long-lived contextual artifacts. This shift fundamentally expands the attack surface of prompt injection. However, prior works on prompt injection have largely focused on model-level threats within a single session, overlooking how cross-session persistent system state fundamentally changes the system-level risk of agentic systems. Inspired by stored cross-site scripting in web systems, we introduce cross-session stored prompt injection, where a successful injection can persist within agentic system state and silently influence future executions long after the original attacker interaction has ended. To systematically study this threat, we formalize stored prompt injection and develop a taxonomy of how adversarial content persists and affects agentic systems across sessions. We further develop a benchmark and sandbox toolkit to evaluate the risks of stored prompt injection, enabling quantitative analysis of attack success across different models, attack goals, and persistence channels. Our findings highlight that persistence transforms prompt injection from an ephemeral model-level threat into a long-lived system-level vulnerability embedded within agent execution state. We hope this work draws broader attention to this emerging threat and motivates the community to systematically study and mitigate system risks arising from persistence in agentic systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现代智能体系统（agentic systems）中一种新型的安全漏洞——跨会话存储型提示注入（cross-session stored prompt injection）。随着大语言模型从无状态会话助手演变为有状态系统，通过记忆、文件系统、工具等持久化机制维护跨会话的世界状态，攻击面发生了根本性扩展。现有研究主要关注单会话内的提示注入，将其视为瞬态威胁，假设恶意指令随会话结束或上下文清除而消失。然而，在持久化智能体系统中，恶意内容一旦被写入长期状态（如记忆、文件），便可在未来会话中被重新加载并影响模型行为，实现注入与利用在时间上的解耦。这类似于Web系统中从反射型XSS到存储型XSS的转变，核心问题在于持久化将提示注入从一次性的模型级威胁转化为长期存在的系统级漏洞。为此，论文形式化了存储型提示注入，建立了攻击分类法，开发了基准测试和沙盒工具包，旨在系统研究这种持久化状态如何导致跨会话的安全危害，并呼吁社区关注这一新兴威胁。

### Q2: 有哪些相关研究？

基于论文内容，相关研究可按以下类别组织：

**1. 传统提示注入研究**：早期工作聚焦于直接提示注入（Direct Prompt Injection），攻击者通过恶意用户输入覆盖系统指令；随后发展为间接提示注入（Indirect Prompt Injection），通过外部资源（如网页、文档、工具输出）嵌入对抗指令。这些工作均假设注入与利用发生在同一会话内，属于会话绑定的瞬态威胁。本文指出此类研究忽略了跨会话持久化带来的系统性风险。

**2. 工具增强型Agent安全评测**：AgentDojo、Agent Safety Bench、Agent Security Bench等基准测试评估了工具使用Agent的安全风险，但同样局限于单次交互，未考虑持久化状态污染问题。

**3. 记忆注入（Memory Injection）**：最新工作探索了通过查询将对抗内容植入Agent记忆并影响后续行为。但本文指出其范围仅限于记忆作为持久化目标、查询作为注入通道，未覆盖元数据、文件系统、工具生成物等更广泛的持久化渠道，也未涉及跨系统状态污染。

本文的核心区别在于：系统性地将提示注入从**会话内瞬态威胁**扩展为**跨会话持久化系统级漏洞**，形式化了状态传播与持久化机制，并构建了首个覆盖多种注入源、持久化渠道和上下文整合机制的基准测试与沙盒工具包。

### Q3: 论文如何解决这个问题？

该论文提出了**跨会话存储型提示注入**（Cross-Session Stored Prompt Injection）这一新型攻击范式，并系统性地研究了其原理与风险。核心方法是将Agent系统建模为一个**上下文构建管道**，将攻击生命周期分为注入与激活两个阶段。

**核心方法**：论文将Agent系统的输入`x_t`定义为多个上下文通道的联合，包括当前用户查询、指令、会话历史、工具接口、检索内容和文件支撑上下文。其中，跨会话持久性强的上下文（如指令、文件、工具描述）构成了**强持久上下文**，攻击者通过用户输入、外部内容或供应链工具等**注入源**，将恶意内容写入这些通道，实现跨会话持久化。在后续会话中，这些存储的恶意内容通过**直接加载**（无条件）或**条件加载**（需检索触发）机制被重新纳入模型上下文，从而影响Agent行为。

**架构设计**：论文提出了三维分类法：(1) **注入源**：用户提供、外部消费、供应链安装；(2) **持久上下文通道**：代理记忆、工具可见状态、文件支撑上下文；(3) **上下文纳入机制**：直接加载与条件加载。攻击者通过写原语将恶意内容注入持久通道，在激活阶段无需在场，攻击由正常的上下文构建触发。

**创新点**：首次正式定义并系统化研究了存储型提示注入，揭示了持久化如何将提示注入从单会话的瞬时威胁转变为跨会话的系统级漏洞，并开发了基准测试和沙箱工具包用于定量评估。攻击目标分为事实操纵、偏好操纵和动作范围操纵三类，完整刻画了攻击生命周期与危害。

### Q4: 论文做了哪些实验？

该论文通过自建的SPI-Benchmark基准测试，在3个应用场景（电子商务、旅行预订、金融投资组合管理）中设计了162个存储型提示注入用例，对GLM-5.1、GPT-5-mini和MiniMax-M2.7三种模型进行系统评估。实验采用四阶段流水线：环境设置、注入、会话重置、激活，并定义分阶段成功率指标（写入成功率WSR、纳入率IR、激活率AR）和端到端攻击成功率（E2E-ASR）。主要结果如下：（1）整体E2E-ASR为32.1%-42.0%，GLM-5.1最高（42.0%）但WSR最低（64.2%），MiniMax-M2.7的WSR最高（86.4%）但E2E-ASR居中（40.7%）；（2）事实操纵攻击最有效（E2E-ASR 74-82%，AR达100%），偏好操纵最难（E2E-ASR 0-11%），动作范围操纵存在模型差异（E2E-ASR 18.5-40.7%）；（3）直接加载通道（文件上下文和直接工作记忆）比条件加载通道成功率更高；（4）语境伪装攻击通过提高WSR（而非改善AR）整体优于朴素注入；（5）金融场景中GPT-5-mini的脆弱性显著降低。实验揭示了写入和激活阶段基本解耦的关键发现。

### Q5: 有什么可以进一步探索的点？

该研究提出了跨会话存储提示注入这一新颖威胁，但其局限性主要体现在：首先，实验环境为模拟沙盒，可能低估真实世界生态系统的复杂性和防御机制；其次，未深入探讨不同持久化渠道（如记忆、文件系统、工具）间的组合攻击效应。未来研究方向包括：一、开发动态防御机制，如基于行为异常的注入检测和会话隔离策略，打破持久化链；二、研究多模态输入（图像、音频）生成存储注入的可能性，扩展攻击面；三、设计基于形式化验证的持久化数据审计系统，确保状态一致性；四、探索自修复架构，使智能体能在检测到受污染状态后自动回滚或重建上下文。此外，将Web安全中的同源策略和沙箱隔离理念映射到智能体系统，或能从根本上缓解此类威胁。

### Q6: 总结一下论文的主要内容

现代大型语言模型驱动的主体系统已从单会话助手转变为跨会话持久化共享状态的有状态系统。这些系统通过记忆、文件系统、工具等长期上下文工件保存并演化世界状态，从根本上扩展了提示注入的攻击面。受Web系统中存储型跨站脚本（XSS）启发，本文首次定义了跨会话存储型提示注入（Stored Prompt Injection, SPI）这一新型系统级攻击向量：一次成功的注入可在主体系统状态中持久存在，在初始攻击交互结束后长期静默影响未来执行。作者系统性地形式化了SPI生命周期，建立了涵盖写入、持久化、检索、利用四个阶段的攻击分类体系，并开发了基准测试工具包以量化评估不同模型、攻击目标和持久化渠道下的攻击成功率。核心发现表明，持久化将提示注入从短暂的模型级威胁转变为嵌入主体执行状态的长效系统级漏洞。该工作揭示了有状态演化带来的根本性安全转变，呼吁学界系统性地研究和缓解主体系统中持久化引发的系统性风险。
