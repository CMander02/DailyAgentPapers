---
title: "ChainFuzzer: Greybox Fuzzing for Workflow-Level Multi-Tool Vulnerabilities in LLM Agents"
authors:
  - "Jiangrong Wu"
  - "Zitong Yao"
  - "Yuhong Nan"
  - "Zibin Zheng"
date: "2026-03-13"
arxiv_id: "2603.12614"
arxiv_url: "https://arxiv.org/abs/2603.12614"
pdf_url: "https://arxiv.org/pdf/2603.12614v1"
categories:
  - "cs.SE"
  - "cs.CR"
tags:
  - "Agent Security"
  - "Tool-Augmented Agent"
  - "Multi-Tool Workflow"
  - "Vulnerability Discovery"
  - "Greybox Fuzzing"
  - "Agent Testing"
  - "LLM Guardrails"
relevance_score: 8.0
---

# ChainFuzzer: Greybox Fuzzing for Workflow-Level Multi-Tool Vulnerabilities in LLM Agents

## 原始摘要

Tool-augmented LLM agents increasingly rely on multi-step, multi-tool workflows to complete real tasks. This design expands the attack surface, because data produced by one tool can be persisted and later reused as input to another tool, enabling exploitable source-to-sink dataflows that only emerge through tool composition. We study this risk as multi-tool vulnerabilities in LLM agents, and show that existing discovery efforts focused on single-tool or single-hop testing miss these long-horizon behaviors and provide limited debugging value. We present ChainFuzzer, a greybox framework for discovering and reproducing multi-tool vulnerabilities with auditable evidence. ChainFuzzer (i) identifies high-impact operations with strict source-to-sink dataflow evidence and extracts plausible upstream candidate tool chains based on cross-tool dependencies, (ii) uses Trace-guided Prompt Solving (TPS) to synthesize stable prompts that reliably drive the agent to execute target chains, and (iii) performs guardrail-aware fuzzing to reproduce vulnerabilities under LLM guardrails via payload mutation and sink-specific oracles. We evaluate ChainFuzzer on 20 popular open-source LLM agent apps (998 tools). ChainFuzzer extracts 2,388 candidate tool chains and synthesizes 2,213 stable prompts, confirming 365 unique, reproducible vulnerabilities across 19/20 apps (302 require multi-tool execution). Component evaluation shows tool-chain extraction achieves 96.49% edge precision and 91.50% strict chain precision; TPS increases chain reachability from 27.05% to 95.45%; guardrail-aware fuzzing boosts payload-level trigger rate from 18.20% to 88.60%. Overall, ChainFuzzer achieves 3.02 vulnerabilities per 1M tokens, providing a practical foundation for testing and hardening real-world multi-tool agent systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能代理（Agent）在集成多种工具（tool）以执行多步骤工作流（workflow）时，所暴露出的新型安全风险，即“多工具漏洞”（multi-tool vulnerabilities）。

**研究背景**：随着LLM代理能力的增强，它们越来越多地通过串联调用多个外部工具（如网络搜索、文件读写、代码执行等）来完成复杂任务。这种多步骤、多工具的工作流设计虽然提升了功能，但也显著扩大了攻击面。攻击者可能通过精心设计的输入，使得一个工具产生的、看似无害的数据（如从网络下载的内容）在后续工具中被复用，最终触发高风险操作（如执行恶意代码），形成跨越多个工具的、可被利用的“源-汇”数据流。

**现有方法的不足**：当前针对LLM代理的漏洞发现工作主要集中于“单工具”或“单跳”测试，即试图用一个恶意输入直接触发单个不安全工具调用。这种方法存在严重不足：首先，它会产生大量漏报，因为许多风险只有在多个工具按特定顺序组合执行时才会显现，而每个单独步骤看起来都是良性的。其次，它提供的调试价值有限，无法揭示攻击者影响的内容是如何在不同工具间传播的，从而难以指导开发者在正确的边界（如首个不受信任的入口点）实施有效的缓解措施。

**本文要解决的核心问题**：因此，本文的核心目标是提出一种工作流级别的测试方法，以自动化地发现、复现和验证LLM代理中这种由工具组合引发的、长链条的“多工具漏洞”。具体而言，论文需要解决三个关键挑战：1）如何从海量可能的工具组合中高效识别出高风险的工具链；2）如何生成稳定的提示词，以可靠地驱动非确定性的LLM代理执行目标工具链；3）如何在模型自身安全护栏（guardrails）存在的情况下，有效验证漏洞的触发。为此，论文提出了ChainFuzzer框架来系统性地应对这些挑战。

### Q2: 有哪些相关研究？

本文主要针对LLM智能体中多工具组合引发的漏洞进行检测，其相关研究可大致分为以下几类：

**1. 单工具/单步漏洞检测方法**：现有研究多集中于对单个工具或单次调用的安全性测试，例如通过提示注入或越权操作直接攻击特定工具接口。这类方法（如针对API或代码执行环境的fuzzing）虽能发现孤立漏洞，但无法捕捉跨工具的数据流和状态依赖所引发的复合风险。本文指出，此类工作因忽略工具间的长链条依赖，会遗漏仅在多步工作流中显现的漏洞。

**2. 智能体工作流建模与验证**：部分研究尝试对智能体的决策逻辑或工具调用序列进行形式化建模，以验证其安全性。这些工作通常关注规划正确性或资源约束，而非针对恶意数据在跨工具传播中的安全影响。本文的ChainFuzzer则专注于通过数据流分析（如源-汇依赖）识别跨工具的高风险操作链，并引入追踪引导的提示合成技术，以稳定触发目标工具链。

**3. 灰盒/黑盒模糊测试技术**：传统软件测试中的模糊测试已被应用于LLM系统，但多数侧重于生成随机输入测试单点功能。本文提出的灰盒框架结合了跨工具依赖分析、守卫感知的模糊测试（通过载荷变异和汇点特定预言机）以及可审计证据生成，从而系统性地复现多工具漏洞，与仅依赖随机输入或简单规则的方法形成对比。

**4. 多智能体协同安全研究**：另有工作探索多智能体协作中的安全问题（如对抗性干扰），但主要关注智能体间的通信或策略冲突。本文专注于单个智能体内部多工具的工作流漏洞，强调工具组合带来的攻击面扩展，并通过实证在20个开源智能体应用中验证了漏洞的普遍性（多数需多工具执行）。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ChainFuzzer的灰盒测试框架来解决多工具LLM代理中工作流级漏洞的发现与复现问题。其核心方法围绕三个主要挑战展开，并设计了三个对应模块。

整体框架分为三个核心模块：1）**基于Sink的工具链提取**，用于识别高风险工作流；2）**工具链提示词生成**，用于可靠驱动代理执行目标链；3）**反馈驱动的模糊测试与漏洞验证**，用于在真实防护机制下复现漏洞。

**核心方法与架构设计：**
首先，**基于Sink的工具链提取模块** 旨在解决“寻找风险工具链”的挑战。它采用严格的源到汇数据流分析，通过扫描工具源码，识别出包含高风险API调用（如exec、eval）且其参数受工具输入影响的“汇工具”。然后，从每个汇工具出发，通过静态依赖分析进行反向链提取。依赖关系分为两类：直接依赖（上游工具的输出字段被下游工具的输入参数消费）和间接依赖（通过文件、数据库等共享载体传递数据）。为避免产生过多语义不合理的链，该模块最后使用LLM作为语义过滤器，仅保留构成连贯、合理工作流的候选链。

其次，**工具链提示词生成模块** 旨在解决“驱动代理执行工具链”的挑战。其关键技术是**基于轨迹的提示词求解**。该过程是迭代的：从根据目标链生成的初始种子提示词开始，运行代理并收集工具调用轨迹。如果执行偏离目标链，则利用LLM分析轨迹，生成解释偏离原因的语义约束（如缺少前置条件、参数绑定错误）。接着，另一个LLM根据当前提示词和约束，在局部编辑空间内进行修订，生成新的提示词。此循环持续进行，直到代理能连续稳定地执行完整目标链，从而得到可靠的“有效提示词”。

最后，**反馈驱动的模糊测试与漏洞验证模块** 旨在解决“在防护机制下复现漏洞”的挑战。一旦获得可执行的工具链和有效提示词，该模块会根据汇类型（如命令注入、SQL注入）生成恶意载荷，并根据依赖分析确定的注入点（用户驱动或环境驱动）进行注入。为了绕过LLM内置的内容安全防护，该模块采用了**反馈驱动的载荷变异**策略，例如将载荷分片、编码或调整格式，以逃避检测同时保持工作流执行。漏洞验证则通过**特定于汇的检测机制**来完成，例如监测命令是否成功执行、网络请求是否到达内部端点等，从而生成包含触发提示词、载荷和工具调用轨迹的可审计漏洞复现证据。

**创新点**主要包括：1) 首次系统性地针对多工具组合产生的跨工具数据流漏洞进行发现；2) 提出了TPS方法，将非确定性的代理执行问题转化为基于轨迹约束的提示词迭代求解问题，显著提升了目标链的可达性；3) 设计了结合防护机制感知的模糊测试方法，通过载荷变异有效绕过LLM原生防护，暴露工具层设计缺陷。

### Q4: 论文做了哪些实验？

论文在20个流行的开源LLM智能体应用（共998个工具）上对ChainFuzzer进行了评估。实验设置方面，使用GPT-5.1作为智能体运行时的目标LLM，ChainFuzzer自身由GPT-4o驱动，实验在配备Apple M4 Max CPU和36GB RAM的本地机器上进行。

数据集由20个满足特定条件（GitHub星标≥2000且支持多工具工作流）的开源多工具LLM应用构成，包括openclaw、autogpt、langchain等知名项目。

主要结果如下：ChainFuzzer共提取了2388条候选工具链，合成了2213个稳定提示，最终在20个应用中的19个里确认了365个独特、可复现的漏洞。其中，302个漏洞需要多工具执行才能触发，占比82.74%，表明多工具漏洞是主要风险。漏洞类型包括命令注入（CMDi）、代码注入（CODEi）、服务器端请求伪造（SSRF）等。从触发源看，225个（61.64%）漏洞通过用户源输入（恶意用户）触发，140个（38.36%）通过环境源输入（如工具返回的网络内容）触发。

关键数据指标包括：工具链提取的边精度达到96.49%，严格链精度为91.50%；追踪引导提示求解（TPS）将链可达率从27.05%提升至95.45%；护栏感知模糊测试将有效载荷级别的触发率从18.20%提升至88.60%。整体效率为每百万token发现3.02个漏洞，平均每个应用分析耗时3.4小时，消耗604万token。

### Q5: 有什么可以进一步探索的点？

该论文虽在检测多工具漏洞方面取得进展，但仍存在可深入探索的空间。首先，ChainFuzzer目前主要针对开源代理应用进行测试，其方法在闭源、专有或高度定制化的商业Agent系统中的泛化能力尚不明确，未来需验证其在更复杂、黑盒环境下的有效性。其次，框架侧重于已知工具链的漏洞挖掘，对于动态生成、自适应或学习型工作流中的新兴威胁检测能力有限，可结合强化学习或符号执行来探索未知攻击路径。此外，当前防护机制（guardrail）的绕过主要依赖突变策略，未来可引入对抗性提示生成或利用LLM自身弱点进行更隐蔽的测试。最后，研究集中于漏洞发现，而未深入探讨修复方案，后续可探索自动补丁生成或基于漏洞模式的防御框架，以形成完整的“检测-防御”闭环。

### Q6: 总结一下论文的主要内容

本文提出了ChainFuzzer，一个用于发现LLM智能体中多工具漏洞的灰盒测试框架。核心问题是，当智能体通过多步骤、多工具的工作流执行任务时，跨工具的数据流可能形成从攻击者可控源头到高危接收器的可被利用路径，而现有的单工具或单跳测试方法会遗漏这类长视野行为。

ChainFuzzer的方法主要包括三个步骤：首先，基于跨工具依赖关系，识别具有严格源-汇数据流证据的高危操作，并提取出可能的上游候选工具链。其次，采用轨迹引导的提示求解技术，通过比较运行时轨迹与目标链并迭代修复提示，合成能稳定驱动智能体执行目标链的提示。最后，进行护栏感知的模糊测试，通过变异载荷和使用特定于接收器的预言机，在LLM安全护栏下复现漏洞。

主要结论是，多工具漏洞在实际部署的智能体中普遍存在。在评估的20个流行开源LLM智能体应用中，ChainFuzzer在19个中确认了365个独特且可复现的漏洞，其中302个需要多工具执行。该方法在工具链提取上达到了高精度，并通过提示合成将链可达性从27.05%大幅提升至95.45%，护栏感知模糊测试将载荷级触发率从18.20%提升至88.60%。该工作为测试和加固现实世界的多工具智能体系统提供了实用基础。
