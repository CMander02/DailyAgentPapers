---
title: "The Emergence of Autonomous Penetration Capabilities in Large Language Model-Powered AI Systems"
authors:
  - "Jiaqi Luo"
  - "Jiarun Dai"
  - "Zhile Chen"
  - "Jia Xu"
  - "Weibing Wang"
  - "Yawen Duan"
  - "Brian Tse"
  - "Geng Hong"
  - "Xudong Pan"
  - "Yuan Zhang"
  - "Min Yang"
date: "2026-06-11"
arxiv_id: "2606.13079"
arxiv_url: "https://arxiv.org/abs/2606.13079"
pdf_url: "https://arxiv.org/pdf/2606.13079v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Autonomous Penetration Testing"
  - "Cybersecurity"
  - "Agent Evaluation Framework"
  - "Vulnerability Exploitation"
  - "Red-line AI Safety"
relevance_score: 9.5
---

# The Emergence of Autonomous Penetration Capabilities in Large Language Model-Powered AI Systems

## 原始摘要

Nowadays, the autonomous execution of cyberattacks capable of causing substantial real-world harm is widely regarded as one of the critical red lines that frontier AI systems must not cross. Within this broader red-line scenario, autonomous penetration represents a core enabling capability and subtask: the ability of LLM-powered AI systems to independently conduct adversarial operations against a target server without human intervention, identify and exploit vulnerabilities, and obtain unauthorized access or control. A growing body of work has sought to assess the autonomous penetration capabilities of AI systems. However, existing evaluations often employ opaque methodologies, rely on unrealistic or overly simplified penetration-testing scenarios, or provide LLMs with excessive prior knowledge and task-specific guidance, and cannot accurately capture the extent to which modern AI systems can autonomously perform this core capability within broader high-impact cyberattack scenarios.
  To address these limitations, we construct a new autonomous penetration evaluation framework consisting of two components: target servers and agent scaffolding. Specifically, on the target-server side, we design two levels of target environments based on the number of secure services without known vulnerabilities deployed alongside a vulnerable service: Tier~1 (one secure service) and Tier~2 (three secure services), resulting in a total of 300 target servers. Meanwhile, the agent scaffolding adopts a general-purpose agent architecture equipped with a set of general-purpose cybersecurity tools, without any target-specific prior knowledge. We evaluate 19 open-weight and proprietary LLMs, and find that current models achieve penetration success rates ranging from 10.7% to 69.3%. Moreover, we observe that autonomous penetration capability continues to improve alongside advances in overall model capability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI系统自主渗透能力评估中存在的关键问题。研究背景是，自主执行能造成重大现实危害的网络攻击被视为前沿AI系统不可逾越的红线，而自主渗透能力是实现这种高风险攻击的核心使能技术。现有评估方法存在三大不足：第一，OpenAI和Anthropic等机构的评估方法不透明，细节未公开，难以复现和系统比较；第二，多数基准测试场景不现实且过于简化，例如采用“夺旗赛”模式而非真实渗透目标（如获取远程shell权限），且目标服务器通常只包含一个漏洞服务，缺乏真实环境中多个安全服务产生的“噪声”；第三，现有评估常为LLM提供过多先验知识（如服务名、版本、攻击路径指引），违背了真实渗透测试的黑盒设置。为此，本文构建了一个更现实的自主渗透评估框架，包含两级复杂度的目标服务器（共300台）和通用代理框架，旨在准确评估当前AI系统在无先验知识情况下端到端的自主渗透能力，并探寻影响该能力的关键因素。研究发现，当前模型的成功率在10.7%至69.3%之间，且该能力随模型整体能力提升而增强。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类。**评测类工作**方面，OpenAI和Anthropic在系统卡中报告了AI在网域环境中的自主渗透评估，但这些方法不透明，难以复现和对比。本文与它们的区别在于采用了完全透明的评估框架和标准化的实验协议。**基准测试类工作**方面，现有基准如Auto-Pen-Bench和CVEBench存在两大问题：一是场景过于简化，例如采用CTF式抓旗任务而非真实渗透的获取shell权限目标，且靶机通常仅部署单一漏洞服务；二是为LLM提供了过多先验知识，如服务名、版本、乃至具体攻击路径。本文与之不同，设计了包含多个安全服务作为背景噪声的两级靶机环境（Tier-1和Tier-2），并采用无目标特定先验知识的通用智能体框架，更贴近真实黑盒渗透场景。**应用类工作**方面，一些工作利用Vulhub、Hack The Box等平台进行评估，但这些平台主要为人类训练设计，缺乏自动验证渗透是否成功的机制，且通常不部署良性后台服务，本文则构建了自带自动化验证的靶机环境，并集成了MCP协议实现工具调用。

### Q3: 论文如何解决这个问题？

该论文通过构建一个全新的自主渗透评估框架来解决现有评估方法的局限性，主要包括两大组件：目标服务器和智能体脚手架。

整体框架设计上，目标服务器包含两类服务：一类是存在真实CVE漏洞的脆弱服务（仅保留可实现远程代码执行的漏洞），另一类是部署最新稳定版本的安全服务作为环境噪声。根据脆弱服务旁部署的安全服务数量，划分为两个复杂度等级：Tier 1（1个脆弱+1个安全服务）和Tier 2（1个脆弱+3个安全服务），共构建300个目标服务器。智能体脚手架采用轻量级通用架构，避免针对渗透测试的特定优化，由三个核心模块组成：思考模块（生成计划和候选动作，仅提供极简任务上下文，如角色定义和目标IP）、记忆模块（采用滑动窗口结合递归摘要机制，保留最近三轮完整交互历史，更早内容由LLM递归摘要压缩）、工具模块（通过MCP协议集成Nmap、WhatWeb、Metasploit等通用网络安全工具）。

关键技术方面，引入模型上下文协议（MCP）实现LLM与外部工具的标准接口交互。记忆模块通过滑动窗口机制和递归摘要方法解决长执行历史导致的性能下降和上下文窗口溢出问题。实验环境采用Docker容器隔离部署，智能体与目标服务器置于独立子网，确保可控交互且不影响宿主机。

核心创新点在于：(1) 消除任务特定优化和先验知识干扰，仅提供IP地址作为目标信息，真正评估LLM内在的自主渗透能力；(2) 设计多层级复杂度的真实服务器场景，引入安全服务作为操作噪声，迫使智能体进行完整服务枚举和攻击面精确识别；(3) 基于真实CVE漏洞构建脆弱服务，避免了人工构造的“寻旗”挑战，更能反映真实渗透场景。

### Q4: 论文做了哪些实验？

本研究构建了一个自主渗透评估框架，包含两层目标环境：Tier-1（一个脆弱服务+一个安全服务）和Tier-2（一个脆弱服务+三个安全服务），共300台目标服务器。智能体采用通用架构，配备通用网络安全工具，无任何目标特定先验知识。评估了19个开源与闭源大语言模型，主要结果如下：在Tier-1上成功率为12.0%至69.3%，Tier-2上为10.7%至68.7%。表现最佳的Gemini3-pro-preview和Claude-opus-4-5接近70%成功率。2024年9月发布的模型已具备10%以上的非平凡自主渗透能力。关键指标显示，自主渗透成功率与LLM在LiveBench上的全局平均得分呈正相关。研究进一步发现，随着模型整体能力提升，自主渗透能力持续增强。值得注意的是，所有评估均聚焦于获取初始shell访问权限这一单一指标，尚未涵盖渗透后的横向移动或数据窃取等高阶操作。这些发现表明，大语言模型驱动的AI系统已展现出不容忽视的自主渗透威胁，且该能力随模型迭代快速提升。

### Q5: 有什么可以进一步探索的点？

当前研究在评估LLM驱动的AI系统自主渗透能力时，虽然构建了更贴近现实的评估框架，但仍有几个关键局限。首先，其目标环境仅基于已知漏洞的服务数量分级（Tier-1和Tier-2），未考虑未知漏洞（零日漏洞）、多步骤复杂攻击链或动态防御机制（如入侵检测系统响应），这可能导致评估结果高估实际攻击能力。未来应引入包含零日漏洞模拟、自适应防御策略和隐蔽性要求的场景。

其次，agent框架使用通用工具且无目标先验知识，但真实渗透中专业安全分析师会结合上下文推理、社会工程或横向移动策略。建议改进agent架构，使其具备分层推理（如先嗅探网络拓扑再选择漏洞利用）或利用检索增强生成（RAG）动态获取目标系统文档。

此外，当前评估聚焦单次成功利用，忽略了攻击持续性、审计日志规避和内部权限提升。未来可探索强化学习与LLM结合，使agent能从失败尝试中自主调整渗透策略，并加入对抗性防御者角色测试其鲁棒性。跨模态漏洞识别（如结合视觉截图分析Web界面）也是值得突破的方向。

### Q6: 总结一下论文的主要内容

该论文构建了评估LLM驱动AI系统自主渗透能力的框架，旨在解决现有研究在方法论透明度、场景真实性和先验知识控制方面的不足。研究定义了自主渗透任务：AI系统在无人类干预、无目标先验知识的情况下，仅凭IP地址对服务器进行侦察、漏洞识别和利用，最终获取远程shell控制权。方法上，框架包括目标服务器和智能体架构两部分：目标服务器涵盖30个真实CVE漏洞（RCE类型），并引入1或3个安全服务作为“噪声”，构建了300个不同复杂度等级的目标；智能体采用通用代理架构，配备Nmap、WhatWeb和Metasploit等通用安全工具，无任何任务特定优化或先验知识。对19个开源和闭源LLM的评估显示，成功率介于10.7%至69.3%之间。主要结论表明，当前AI系统已具备初步的端到端自主渗透能力，且该能力随模型通用能力提升而增强；前沿模型的限制因素主要是工具能力和使用方式，而非推理能力。该研究揭示了AI安全风险，强调需尽早制定安全防护措施。
