---
title: "LivePI: More Realistic Benchmarking of Agents Against Indirect Prompt Injectio"
authors:
  - "Lei Zhao"
  - "Abhay Bhaskar"
  - "Edgar Dobriban"
date: "2026-05-18"
arxiv_id: "2605.17986"
arxiv_url: "https://arxiv.org/abs/2605.17986"
pdf_url: "https://arxiv.org/pdf/2605.17986v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "agent安全"
  - "prompt注入"
  - "评测基准"
  - "多模态agent"
  - "防御机制"
relevance_score: 8.5
---

# LivePI: More Realistic Benchmarking of Agents Against Indirect Prompt Injectio

## 原始摘要

AI agents such as OpenClaw are increasingly deployed in local workflows with access to external tools. This creates indirect prompt-injection (IPI) risk: an agent may execute harmful instructions embedded in untrusted inputs such as email, downloaded files, webpages, repositories, or group-chat messages. Existing evaluations are often small, purely simulated, or focused on a narrow set of channels. We introduce LivePI (Live Prompt Injection), a structured benchmark for IPI risk in a production-like but test-controlled environment. LivePI covers seven input surfaces, twelve attack/rendering families, and five malicious goals, including protected-information exfiltration, unauthorized security-control changes, unsafe code retrieval or execution, inbox-summary exfiltration, and cryptocurrency transfer. We run LivePI on a real virtual machine with live but test-controlled email, chat, web, local-file, repository, and wallet interfaces. Across GPT-5.3-Codex, Claude Opus 4.6, Gemini 3.1 Pro, Kimi K2.5, and GLM-5, total attack success rates range from 10.7% to 29.6%. Group-chat injection is uniformly successful across the evaluated backbones in our deployment, and repository-link attacks produce high-severity failures despite a small denominator. We also evaluate a two-layer defense consisting of prompt-level filtering and pre-execution tool-call authorization. In the GPT-5.3-Codex setting, the defense intercepts all tested malicious-goal completions in LivePI before execution while preserving benign utility on PinchBench-derived workloads.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决AI智能体在现实部署中面临的间接提示注入（Indirect Prompt Injection, IPI）安全风险问题。研究背景是：以OpenClaw为代表的AI智能体已广泛集成网络浏览、代码执行、文件操作、邮件和群聊等外部工具，使其能够执行复杂的工作流。然而，这也带来了严重的安全隐患——攻击者可以将恶意指令嵌入看似无害的外部内容（如电子邮件、下载文件、网页、代码仓库或群聊消息），当智能体将这些内容作为观测输入时，模型可能错误地将其视为指令而不是不可信的证据，从而导致数据泄露、未经授权的配置变更、加密货币转账等危害。现有方法的不足在于：已有评估大多规模较小、完全模拟、或仅覆盖狭窄的攻击渠道。模拟环境虽然便于控制测量，但可能遗漏依赖实时消息来源、持久化主机状态、认证流程或真实工具副作用的关键失败模式。核心问题是：缺乏一个覆盖广泛攻击面、恶意目标、且部署在真实虚拟机环境中的系统性基准测试与防御方案。为此，本文提出了LivePI——一个在接近生产环境但测试可控的部署中评估IPI风险的标准化基准测试，涵盖7个注入面、12种攻击/渲染家族和5类恶意目标。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是**Agent安全评测基准**，如ToolEmu使用LM仿真沙箱进行风险分析，AgentDojo、Agent Security Bench (ASB)、Agent-SafetyBench和AgentHarm在仿真环境中覆盖更丰富的任务和攻击面，OpenAgentSafety将评测推进到真实浏览器和文件系统但仍运行在容器化沙箱内。针对OpenClaw的具体研究包括PASB（强调黑盒端到端评测，但未专注间接注入）、ClawSafety（沙箱中的2520次试验）、ClawTrap（网络路径实时扰动）和Agents of Chaos（具有持久记忆的真实实验环境）。与这些工作不同，LivePI在真实虚拟机中使用测试可控的外部工具和通道进行评测。

第二类是**间接提示注入攻击**，早期工作BIPIA形式化了相关威胁，InjecAgent展示了工具集成代理可被诱导执行有害操作，WASP发现顶级网页代理仍受低努力注入攻击影响。针对OpenClaw的研究还揭示背景执行导致的静默内存污染和对抗性引导隐藏在背景文件中。LivePI通过在真实工具环境中测试来评估当对抗指令融入自然观察流时代理是否能保持任务对齐。

第三类是**防御与运行时策略执行**，包括提示级护栏（如NeMo Guardrails、指令层次结构）、模型侧安全分类器（如Llama Guard）和代理级防御（如Task Shield、MELON）。LivePI结合了输入过滤与确定性工具授权作为两阶段防御，并在GPT-5.3-Codex上证明了其有效性。

### Q3: 论文如何解决这个问题？

LivePI通过构建一个结构化的基准测试框架来解决间接提示注入攻击的评估问题。其核心方法是在生产级但受控的环境中系统性地评估AI代理面临的风险。

整体框架包含一个形式化的威胁模型，将代理系统抽象为策略Π、工具集T、环境E等组件。其中，攻击面覆盖了电子邮件、群聊消息、本地文件、网页、API响应、仓库工件和可执行文件等7个输入通道。

主要模块包括：1）攻击生成器，设计12种攻击/渲染家族和5种恶意目标（如敏感信息窃取、安全控制篡改、危险代码执行等）；2）执行环境，在真实虚拟机中部署实时但受控的邮件、聊天、网页、文件、代码库和钱包接口；3）评估指标，通过攻击影响指标A和恶意目标完成指标M的乘积（Success = A × M）来判定攻击成功。

关键技术包括：1）在GPT-5.3-Codex模型上实现了双层防御机制，包括提示级过滤和执行前工具调用授权；2）该防御在LivePI测试中拦截了所有恶意目标完成，同时保持了PinchBench衍生工作负载的良性效用。

创新点在于：1）首个覆盖多通道、多攻击类型的系统化IPI基准；2）在真实虚拟机上运行而非纯模拟；3）揭示了群聊注入在所有评估模型上均100%成功，以及仓库链接攻击虽数量少但后果严重的关键发现。

### Q4: 论文做了哪些实验？

论文在LivePI基准测试上进行了系统性实验。实验设置基于运行在Ubuntu 24.04虚拟机上的真实OpenClaw智能体，配置了真实的浏览器、邮件（Gmail）、即时通讯（WhatsApp、Telegram、Slack）、本地文件、代码仓库（Repo Links）和加密货币钱包（Solana）接口。数据集涵盖7个输入表面（群聊、邮件、本地文档、仓库链接、Gist）、12种攻击技术（如直接群消息指令、清单交接注入、审批链欺骗等）和5个恶意目标（加密文件窃取、禁用防火墙、执行恶意脚本、邮件摘要外泄、加密货币转账），共计169个测试用例。对比方法包括GPT-5.3-Codex、Claude Opus 4.6、Gemini 3.1 Pro、Kimi K2.5和GLM-5五个骨干模型。主要结果：总体攻击成功率（ASR）从Claude Opus 4.6的10.7%到Gemini 3.1 Pro的29.6%不等。群聊注入在所有模型上均100%成功；仓库链接攻击除Claude Opus 4.6（50%）外均为100%成功；邮件表面ASR为2.0%-20.0%，本地文档为0.0%-50.0%，Gist表面表现最弱（多数模型为0.0%）。此外，针对GPT-5.3-Codex测试的两层防御（提示级过滤和执行前工具调用授权）成功拦截了所有LivePI中的恶意目标完成，同时保持PinchBench衍生工作负载的良性效用。

### Q5: 有什么可以进一步探索的点？

这篇论文在间接提示注入（IPI）风险评估上迈出了重要一步,但仍有多项局限值得未来深入探索。首先,防御策略针对特定攻击类别设计,缺乏通用性,且仅在GPT模型上验证,未来需在多个基座模型上测试以区分策略依赖与模型依赖。其次,仓库链接攻击的样本量极小（仅4例）,虽揭示高风险漏洞,但统计效力不足,需扩展该攻击面的覆盖度。第三,当前评估依赖LLM裁判同时辅以确定性检查,存在裁判模型偏差（尤其当裁判与评估模型同源时）,未来应引入人类评估、裁判间一致性分析及对抗性审计的确定性检查。最后,实验环境虽优于纯模拟,但仍非真实跨组织部署,纵向监测不同信任边界的实际风险是重要方向。此外,可探索多步攻击链下的累积防御效果、对防御机制的对抗性绕过测试,以及如何在不显著牺牲实用性的前提下提升防御鲁棒性。

### Q6: 总结一下论文的主要内容

LivePI提出了一个针对AI代理（特别是OpenClaw）间接提示注入风险的系统化基准测试框架，在真实的虚拟机环境中运行，涵盖七种注入表面（包括电子邮件、群聊、网页、文件、仓库等）、十二种攻击/渲染家族和五种恶意目标（如保护信息窃取、安全控制篡改、不安全代码执行等）。通过测试五种主流大语言模型骨干（GPT-5.3-Codex、Claude Opus 4.6等），发现总攻击成功率在10.7%至29.6%之间，其中群聊注入在所有模型中均表现出高成功率，仓库链接攻击也会导致严重后果。研究还评估了一种双层防御策略（提示级过滤和执行前工具调用授权），在GPT-5.3-Codex设置下能够拦截所有测试的恶意目标完成，同时保持对正常工单的干扰率仅为1%。这项工作首次在可控的真实部署环境下系统评估了多表面、多目标的间接提示注入风险，揭示了现有模型在该场景下的普遍脆弱性，并提供了一个可扩展的评估框架。
