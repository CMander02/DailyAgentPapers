---
title: "Evaluating Privilege Usage of Agents on Real-World Tools"
authors:
  - "Quan Zhang"
  - "Lianhang Fu"
  - "Lvsi Lian"
  - "Gwihwan Go"
  - "Yujue Wang"
  - "Chijin Zhou"
  - "Yu Jiang"
  - "Geguang Pu"
date: "2026-03-30"
arxiv_id: "2603.28166"
arxiv_url: "https://arxiv.org/abs/2603.28166"
pdf_url: "https://arxiv.org/pdf/2603.28166v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Tool Use"
  - "Privilege Control"
  - "Evaluation Benchmark"
  - "Prompt Injection"
  - "Sandbox Environment"
relevance_score: 7.5
---

# Evaluating Privilege Usage of Agents on Real-World Tools

## 原始摘要

Equipping LLM agents with real-world tools can substantially improve productivity. However, granting agents autonomy over tool use also transfers the associated privileges to both the agent and the underlying LLM. Improper privilege usage may lead to serious consequences, including information leakage and infrastructure damage. While several benchmarks have been built to study agents' security, they often rely on pre-coded tools and restricted interaction patterns. Such crafted environments differ substantially from the real-world, making it hard to assess agents' security capabilities in critical privilege control and usage. Therefore, we propose GrantBox, a security evaluation sandbox for analyzing agent privilege usage. GrantBox automatically integrates real-world tools and allows LLM agents to invoke genuine privileges, enabling the evaluation of privilege usage under prompt injection attacks. Our results indicate that while LLMs exhibit basic security awareness and can block some direct attacks, they remain vulnerable to more sophisticated attacks, resulting in an average attack success rate of 84.80% in carefully crafted scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在集成现实世界工具时所引发的特权使用安全风险问题。研究背景是，为了提升生产力，将LLM与外部工具结合构建自主代理已成为主流趋势，这些代理能够调用API或本地命令来规划和执行任务。然而，在赋予代理工具调用能力的同时，也转移了执行这些工具所需的底层特权。在安全关键环境中，这种授权带来了重大风险，因为LLM通常缺乏足够的特权使用安全意识，面对恶意攻击时可能滥用特权，导致敏感信息泄露或关键基础设施损坏等严重后果。

现有方法的不足在于，尽管已有一些评估基准（如AgentDojo、Agent Security Bench、RAS-Eval）被开发出来研究代理的安全性，但它们大多依赖于预编码的简化工具（如本地文件操作、静态数据查询）和受限的交互模式。这种人工构建的环境与现实世界存在显著差异，缺乏对需要关键特权的真实复杂服务（如云基础设施、生产数据库）交互的支持，因此难以系统评估代理在关键特权控制和使用方面的安全性能。

因此，本文的核心问题是：如何在一个更贴近现实、支持真实工具和特权交互的环境中，系统评估LLM代理在面临攻击时的特权使用安全性。为此，论文提出了GrantBox这一安全评估沙箱，旨在分析代理在现实环境中的特权使用情况。它通过自动集成真实世界的工具（如云管理、数据库管理、邮件服务等），允许LLM代理调用真实的特权，并在提示注入攻击等场景下评估其特权使用行为，从而弥补现有研究在特权使用评估方面的空白。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕评估LLM智能体安全性的基准测试展开，可分为方法类与评测类。

在评测类工作中，**AgentDojo** 构建了模拟环境（如银行、工作空间管理）来测试智能体对提示注入攻击的鲁棒性。**Agent Security Bench (ASB)** 则提供了一个评估对抗性攻击（如内存投毒、后门威胁）的框架，覆盖金融、自动驾驶等多种场景。**RAS-Eval** 进一步扩展，引入了更真实的预编码工具（如地图导航、本地文件操作）进行评估。这些工作的共同点是聚焦于智能体识别恶意意图的能力，并依赖**有限的、预编码的简化工具**（如手工输入的文件操作或静态数据查询），在受控的模拟环境中进行测试。

本文提出的GrantBox与上述工作的**关系**在于，它同属安全评测基准范畴，旨在评估智能体的安全性。其**核心区别**在于：1) **评测重点不同**：现有工作主要评估“恶意意图检测”，而本文专注于评估**真实场景下的权限使用与控制**这一关键安全问题。2) **环境真实性不同**：现有基准使用预编码的、简化的工具和交互模式，与真实世界脱节；GrantBox则通过自动化集成**真实世界的工具**（如云基础设施、生产数据库），允许智能体调用**真实的权限**，从而能在更贴近实际、权限敏感的复杂服务交互中进行评估。这填补了现有研究在系统性评估关键权限使用安全性能方面的空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为GrantBox的安全评估沙盒来解决智能体在真实世界工具上的权限使用安全问题。其核心方法是创建一个能够自动集成真实工具、并允许LLM智能体调用真实权限的隔离测试环境，从而在模拟提示注入攻击的场景下评估权限使用情况。

整体框架包含三个主要模块：MCP服务器管理器、请求生成器和MCP服务器沙盒。MCP服务器管理器作为外部编排层，负责管理所有MCP服务器的生命周期，协调评估过程中的使用。它包含生命周期维护器（负责服务器部署、健康监控和自动恢复）、智能体管道（支持ReAct和Plan-and-Execute两种执行模式，并可灵活注入攻击）和容器维护器（管理与沙盒的交互）。请求生成器则自动构建多样化的评估场景，通过随机组合MCP服务器并利用LLM驱动生成请求，同时支持生成良性用户请求和对抗性提示注入载荷。其算法确保请求意图的多样性，并为注入请求包裹合理的上下文以增强真实性。MCP服务器沙盒提供了一个容器化的隔离执行环境，内部包含SSE-Stdio代理（统一通信协议）、自动化MCP服务器部署器以及用于监控和日志记录的组件，确保评估的安全性和可观测性。

关键技术包括：1）对真实世界MCP服务器的自动化集成与管理，覆盖了云基础设施管理、外部数据检索、个人数据管理和本地设备操作等多个类别；2）通过算法驱动的请求生成，最小化请求间的意图重叠，并自然嵌入恶意攻击载荷；3）容器化沙盒环境，支持快速恢复和精细化的权限使用追踪（如通过HTTP拦截器记录对外请求）。创新点在于摒弃了预先编码工具和受限交互模式的传统基准测试方法，转而构建一个能够反映真实工具和权限交互的安全评估平台，从而更准确地评估智能体在关键权限控制和使用方面的安全能力。

### Q4: 论文做了哪些实验？

论文实验主要分为两部分：一是评估自动生成的良性请求和恶意请求的多样性与复杂性，二是评估不同大语言模型在管理权限使用方面的安全能力。

实验设置方面，研究构建了GrantBox安全评估沙盒，集成了10个MCP服务器，覆盖文件系统访问、外部数据检索和云基础设施管理等功能。评估了GPT-5、Gemini3-Flash、Qwen3-Max和Deepseek-V3.2四款主流大语言模型在ReAct和Plan-and-Execute两种智能体模式下的安全表现。

数据集与基准测试方面，基于10个MCP服务器生成了100个良性请求和50个恶意请求。通过组合良性请求和提示注入请求，构建了包含多达5000个攻击案例的综合评估集。对良性请求的分析显示，每个请求平均涉及3.15个服务器和5.67个工具，超过半数请求使用超过5个工具，且100个请求中存在96种独特的工具组合，表明任务复杂且工具使用模式多样。恶意请求的攻击意图被分为五类：数据窃取（占36%）、基础设施破坏（28%）、工作区篡改（16%），以及权限提升和资源耗尽。

主要结果以攻击成功率（ASR）为关键指标。在精心设计的攻击下，所有模型都表现出脆弱性：ReAct模式下平均ASR为90.55%，Plan-and-Execute模式下为79.05%。对比发现，除Deepseek-v3外，基于规划的智能体通常ASR更低（例如Gemini3在规划模式下ASR降低了20.00%），表明执行计划有助于识别注入尝试，但会牺牲工具使用的灵活性。模型能力方面，高性能模型（如GPT-5和Gemini 3-Flash在ReAct模式下ASR超过90%）因擅长遵循复杂指令反而更易受攻击，但在规划模式下其表现显著改善。不同攻击类别中，工作区篡改攻击的ASR最高，而涉及关键权限的攻击（如基础设施破坏）更容易触发模型的安全意识，但其绝对ASR仍然很高。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于评估环境仍部分依赖真实外部服务（如阿里云），搭建成本较高，且未系统测试现有防御机制的有效性。未来研究可从以下方向深入：一是开发更完善的模拟响应机制，降低对真实基础设施的依赖，提升评估的可复现性与扩展性；二是利用GrantBox的模块化设计，集成文本过滤、计划验证等主动防御模块，并探索细粒度权限控制策略（如动态权限回收）；三是拓展攻击场景，不仅关注提示注入，还可结合社会工程、多步骤权限提升等复合攻击手法，更全面评估智能体在复杂环境中的安全边界。此外，可研究如何将安全能力内化为智能体的决策逻辑，例如通过强化学习让智能体在工具使用中自主权衡效用与风险。

### Q6: 总结一下论文的主要内容

该论文针对LLM智能体在现实工具使用中的权限安全问题，提出了一个名为GrantBox的安全评估沙箱框架。核心问题是：当LLM智能体被赋予真实工具的使用权限时，不恰当的权限使用可能导致信息泄露和基础设施损坏等严重后果，而现有基准测试多依赖于预编码工具和受限交互，难以真实评估智能体的权限控制能力。

论文的方法概述是构建GrantBox框架，其核心贡献在于自动集成真实世界的工具（通过MCP服务器），并允许LLM智能体调用真实的权限，从而在模拟真实权限敏感场景（包括良性请求和恶意请求）下评估其安全性，特别是针对提示注入攻击的防御能力。

主要结论显示，尽管当前的大语言模型表现出基本的安全意识并能阻挡一些直接攻击，但在精心设计的复杂攻击（如提示注入）面前依然脆弱，在特定场景下的平均攻击成功率高达84.80%。这凸显了在部署具备工具使用能力的智能体时，加强其权限使用安全机制的紧迫性和重要性。
