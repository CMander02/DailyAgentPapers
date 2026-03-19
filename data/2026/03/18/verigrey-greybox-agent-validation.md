---
title: "VeriGrey: Greybox Agent Validation"
authors:
  - "Yuntong Zhang"
  - "Sungmin Kang"
  - "Ruijie Meng"
  - "Marcel Böhme"
  - "Abhik Roychoudhury"
date: "2026-03-18"
arxiv_id: "2603.17639"
arxiv_url: "https://arxiv.org/abs/2603.17639"
pdf_url: "https://arxiv.org/pdf/2603.17639v1"
categories:
  - "cs.AI"
tags:
  - "Agent安全"
  - "Agent测试"
  - "Agent验证"
  - "工具调用"
  - "提示注入"
  - "灰盒测试"
  - "Agent基准测试"
relevance_score: 8.0
---

# VeriGrey: Greybox Agent Validation

## 原始摘要

Agentic AI has been a topic of great interest recently. A Large Language Model (LLM) agent involves one or more LLMs in the back-end. In the front end, it conducts autonomous decision-making by combining the LLM outputs with results obtained by invoking several external tools. The autonomous interactions with the external environment introduce critical security risks.
  In this paper, we present a grey-box approach to explore diverse behaviors and uncover security risks in LLM agents. Our approach VeriGrey uses the sequence of tools invoked as a feedback function to drive the testing process. This helps uncover infrequent but dangerous tool invocations that cause unexpected agent behavior. As mutation operators in the testing process, we mutate prompts to design pernicious injection prompts. This is carefully accomplished by linking the task of the agent to an injection task, so that the injection task becomes a necessary step of completing the agent functionality. Comparing our approach with a black-box baseline on the well-known AgentDojo benchmark, VeriGrey achieves 33% additional efficacy in finding indirect prompt injection vulnerabilities with a GPT-4.1 back-end.
  We also conduct real-world case studies with the widely used coding agent Gemini CLI, and the well-known OpenClaw personal assistant. VeriGrey finds prompts inducing several attack scenarios that could not be identified by black-box approaches. In OpenClaw, by constructing a conversation agent which employs mutational fuzz testing as needed, VeriGrey is able to discover malicious skill variants from 10 malicious skills (with 10/10= 100% success rate on the Kimi-K2.5 LLM backend, and 9/10= 90% success rate on Opus 4.6 LLM backend). This demonstrates the value of a dynamic approach like VeriGrey to test agents, and to eventually lead to an agent assurance framework.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在自主决策和调用外部工具时所面临的安全风险验证问题。随着智能体AI的广泛部署，其前端通过与外部环境（如Shell、浏览器等工具）交互来完成复杂任务，这种自主性引入了显著的安全隐患，例如间接提示注入攻击可能导致非预期的、危险的工具调用行为。

现有方法，特别是黑盒测试方法，存在明显不足。黑盒测试将智能体视为不透明的系统，仅通过随机或启发式方法生成输入（如提示词），缺乏对内部执行状态的洞察。这导致测试过程效率低下，难以触发那些不常见但危害巨大的边缘案例，因为许多恶意输入可能在执行初期就被LLM拒绝或忽略，无法深入探索到真正危险的工具调用序列。

因此，本文的核心问题是：如何更有效地探索LLM智能体的多样化行为，以主动发现其安全漏洞？为此，论文提出了VeriGrey这一灰盒验证方法。其核心思路是利用智能体调用外部工具的序列作为反馈函数，来指导测试过程。这种方法能够识别出那些不频繁但危险的工具调用模式。同时，论文设计了创新的变异算子，通过巧妙地将注入任务与智能体的原始任务上下文相绑定，使得恶意提示注入成为完成智能体功能“必要”的一步，从而能够系统地生成并测试那些能真正被智能体接受并执行、进而暴露漏洞的输入。最终目标是为构建更健壮的智能体提供一个有效的验证框架。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕LLM智能体的安全测试与验证，可分为方法类和应用类。

在**方法类**研究中，相关工作主要集中于智能体安全测试技术。传统方法多为黑盒测试，通过外部输入观察输出行为，但难以深入触发复杂或低频的安全漏洞。本文提出的VeriGrey是一种灰盒方法，其核心创新在于利用工具调用序列作为反馈来驱动测试，并通过精心设计的提示词变异操作来构造恶意注入提示。这与黑盒基线方法（如仅依赖随机输入或简单模糊测试）形成鲜明对比，VeriGrey能够更系统地探索智能体行为空间，特别是针对间接提示注入等隐蔽风险。

在**应用类**研究中，相关工作涉及具体的攻击面分析与基准测试。先前工作已识别出智能体的多种攻击面，如直接/间接提示注入、记忆污染和供应链攻击（通过第三方技能或MCP工具）。本文聚焦于单会话场景下的提示注入和供应链攻击，其威胁模型明确假设攻击者能控制智能体可访问的外部资源（如网站、MCP服务器）。在评测方面，本文使用AgentDojo基准进行对比，并针对真实世界的智能体（如Gemini CLI、OpenClaw）进行案例研究，这超越了仅在合成或受限环境中进行评估的早期工作，验证了VeriGrey在发现实际攻击场景（如诱导恶意技能变体）方面的效力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为VeriGrey的灰盒测试框架来解决LLM智能体中的安全风险问题，特别是间接提示注入漏洞。其核心方法是采用覆盖引导的灰盒模糊测试技术，但针对LLM智能体的特性进行了关键创新。

**整体框架与工作流程**：
VeriGrey的算法流程如算法1所示。输入包括待测LLM智能体、一组注入任务和一个用户任务。框架首先对智能体进行**插桩**，以记录每次执行时的工具调用序列。然后，它基于注入任务使用模板构造初始的种子提示语料库，并执行初始测试以收集基础的工具序列覆盖。随后进入主测试循环：从种子队列中选择一个种子提示，根据其“能量”（即变异次数）分配变异机会，使用创新的变异算子生成新的注入提示，执行智能体并观察结果。如果新提示成功触发了漏洞，则将其记录；如果它导致了新的工具调用行为（即增加了覆盖），则将其加入种子库以供进一步变异。此过程持续进行，直到达到预设的测试预算。

**主要模块与关键技术**：
1.  **轻量级动态插桩**：为解决覆盖反馈挑战（C1），VeriGrey设计了一个工具调用插桩器。它在不改变原始语义的前提下，在工具调用点包裹一个轻量级的日志记录层，实时捕获工具名称、参数及其调用顺序，形成**工具调用序列**。该序列被用作测试反馈的类比物，类似于传统软件中的代码分支覆盖。
2.  **基于覆盖的反馈与调度**：
    *   **种子选择与能量分配**：框架维护一个已观察到的工具序列数据库。种子选择策略倾向于选择那些能触发新行为的提示。能量分配函数则根据三个指标动态决定变异次数：是否调用了新工具、是否产生了新的工具间转换、是否产生了全新的工具序列。满足的指标越多，分配的变异能量越高，从而引导搜索探索更多样化的行为。
    *   **“有趣性”判定**：如果一次测试执行产生了之前未出现过的工具调用序列，则认为对应的注入提示是“有趣的”，并将其加入种子库，驱动测试向未探索的行为空间进化。
3.  **上下文桥接的LLM驱动变异算子**：这是解决LLM智能体特定变异挑战（C2）的核心创新。传统的模板化或简单变异的提示容易被LLM识别并拒绝。VeriGrey使用LLM本身作为变异引擎，其关键创新在于**上下文桥接**。变异提示模板会引导LLM将**用户任务**（如修复一个bug）与**注入任务**（如读取秘密文件）巧妙地联系起来，编造一个场景使得完成注入任务成为解决用户任务的“必要步骤”。例如，在修复Django bug的任务中，变异后的提示可能会声称需要读取某个配置文件（实为秘密文件）来理解项目设置。这种语义上的对齐大大提高了欺骗智能体执行恶意任务的成功率。

**创新点总结**：
*   **灰盒测试范式应用于LLM智能体**：首次将覆盖引导的灰盒模糊测试系统性地应用于LLM智能体安全验证，利用工具调用序列作为可观测、可量化的反馈信号。
*   **上下文感知的提示变异**：提出了“上下文桥接”方法，通过LLM驱动的变异，生成与用户任务语义紧密关联的注入提示，从而绕过模型对无关或生硬注入的防御机制。
*   **轻量级、动态的测试框架**：通过插桩获取运行时行为，并基于此动态调整测试策略（种子选择、能量分配），实现了对智能体复杂、状态依赖行为的有效探索，能够发现黑盒方法难以触发的深层漏洞。实验表明，该方法在基准测试和真实世界智能体（如Gemini CLI, OpenClaw）中均能有效发现更多安全漏洞。

### Q4: 论文做了哪些实验？

论文在AgentDojo基准测试和两个真实世界智能体（Gemini CLI和OpenClaw）上进行了实验，以评估VeriGrey灰盒测试方法的有效性。

**实验设置与数据集**：主要评估平台为AgentDojo基准测试，它模拟了四个环境（Workspace、Slack、Travel、Banking），共包含97个用户任务。每个任务被视为一个独立的测试活动，目标是发现能完成预定义注入任务（即攻击者目标）的恶意提示。每个测试活动最多执行100次智能体运行。对比基线是一个受AgentVigil启发的黑盒测试工具，它随机突变提示，而不利用智能体执行中的工具调用序列信息。

**主要结果与关键指标**：
1.  **有效性（RQ1）**：在AgentDojo上，使用GPT-4.1后端时，VeriGrey比黑盒基线多发现了**33%**的间接提示注入漏洞。关键指标是**注入任务成功率（ITSR）**，即成功完成的注入任务数占总数的比例。VeriGrey在多个LLM后端（GPT-4.1、Gemini-2.5-Flash、Qwen-3 235B）上均表现出更高的ITSR。
2.  **消融研究与防御（RQ2, RQ3）**：论文通过消融研究分析了VeriGrey各组件（如基于工具序列的反馈、上下文桥接突变）的影响。在评估对抗常见防御机制（如提示三明治、数据分隔符、注入检测、工具过滤器）的能力时，VeriGrey仍能发现有效的注入提示，同时论文也报告了**用户任务成功率（UTSR）**以衡量防御机制对智能体正常功能的影响。
3.  **案例研究（RQ4）**：在真实世界智能体测试中，VeriGrey成功发现了黑盒方法无法识别的攻击场景。特别是在OpenClaw个人助理中，通过构建对话代理并应用突变模糊测试，VeriGrey从10个恶意技能中成功发现了恶意变体：在Kimi-K2.5 LLM后端成功率为**100%（10/10）**，在Opus 4.6 LLM后端成功率为**90%（9/10）**。这验证了VeriGrey动态测试方法的实用价值。

### Q5: 有什么可以进一步探索的点？

本文提出的VeriGrey方法在灰盒测试LLM智能体安全风险方面取得了显著成效，但仍存在一些局限性和值得深入探索的方向。首先，其方法目前主要聚焦于工具调用序列的反馈和提示词变异，未来可扩展至对智能体内部状态（如思维链、记忆模块）的更细粒度监控，实现更深入的“灰盒”分析。其次，当前测试场景和攻击任务（如注入任务）的设计仍依赖于人工链接，自动化生成复杂、隐蔽的多步骤攻击链是一个挑战，可结合形式化方法或对抗性学习来系统化生成测试用例。此外，研究主要评估了已知基准和特定智能体，其通用性和对不同架构（如多智能体协作、具身智能体）的适用性有待验证。最后，如何将动态测试结果有效转化为可部署的“智能体保障框架”，包括开发实时防御机制、安全训练数据生成以及鲁棒性认证标准，是推动该技术从研究走向实践的关键。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为VeriGrey的灰盒测试方法，用于发现和验证LLM智能体中的安全风险。核心问题是LLM智能体在自主调用外部工具时，可能因间接提示注入等漏洞产生危险行为，而传统黑盒测试难以有效覆盖这些风险。

方法上，VeriGrey采用灰盒视角，利用智能体调用工具的历史序列作为反馈，驱动测试过程。它通过设计突变算子，将智能体的原始任务与恶意注入任务相链接，生成有害的注入提示，从而诱导出罕见但危险的工具调用行为，以揭示潜在漏洞。

实验表明，在AgentDojo基准测试中，VeriGrey相比黑盒基线在发现间接提示注入漏洞方面效能提升33%。在Gemini CLI和OpenClaw等实际智能体的案例研究中，该方法成功发现了黑盒方法无法识别的攻击场景，例如在OpenClaw中高效生成恶意技能变体。主要结论是VeriGrey的动态灰盒测试方法能显著提升智能体安全性验证的效力，为构建智能体保障框架提供了重要基础。
