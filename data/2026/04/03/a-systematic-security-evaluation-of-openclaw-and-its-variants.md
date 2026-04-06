---
title: "A Systematic Security Evaluation of OpenClaw and Its Variants"
authors:
  - "Yuhang Wang"
  - "Haichang Gao"
  - "Zhenxing Niu"
  - "Zhaoxiang Liu"
  - "Wenjing Zhang"
  - "Xiang Wang"
  - "Shiguo Lian"
date: "2026-04-03"
arxiv_id: "2604.03131"
arxiv_url: "https://arxiv.org/abs/2604.03131"
pdf_url: "https://arxiv.org/pdf/2604.03131v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent安全"
  - "工具增强Agent"
  - "安全评估"
  - "基准构建"
  - "多框架分析"
  - "风险分析"
relevance_score: 8.0
---

# A Systematic Security Evaluation of OpenClaw and Its Variants

## 原始摘要

Tool-augmented AI agents substantially extend the practical capabilities of large language models, but they also introduce security risks that cannot be identified through model-only evaluation. In this paper, we present a systematic security assessment of six representative OpenClaw-series agent frameworks, namely OpenClaw, AutoClaw, QClaw, KimiClaw, MaxClaw, and ArkClaw, under multiple backbone models. To support this study, we construct a benchmark of 205 test cases covering representative attack behaviors across the full agent execution lifecycle, enabling unified evaluation of risk exposure at both the framework and model levels. Our results show that all evaluated agents exhibit substantial security vulnerabilities, and that agentized systems are significantly riskier than their underlying models used in isolation. In particular, reconnaissance and discovery behaviors emerge as the most common weaknesses, while different frameworks expose distinct high-risk profiles, including credential leakage, lateral movement, privilege escalation, and resource development. These findings indicate that the security of modern agent systems is shaped not only by the safety properties of the backbone model, but also by the coupling among model capability, tool use, multi-step planning, and runtime orchestration. We further show that once an agent is granted execution capability and persistent runtime context, weaknesses arising in early stages can be amplified into concrete system-level failures. Overall, our study highlights the need to move beyond prompt-level safeguards toward lifecycle-wide security governance for intelligent agent frameworks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在系统性地评估以OpenClaw为代表的工具增强型AI智能体框架所引入的系统性安全风险。研究背景是，大型语言模型（LLMs）在集成工具调用、多步规划、本地执行和状态持久化等能力后，演变为功能强大的AI智能体，这极大地扩展了其应用能力，但也带来了全新的安全挑战。现有方法或安全评估的不足在于，它们通常局限于对孤立的大语言模型本身进行提示词级别的安全性测试（即检查模型是否会拒绝不安全的文本请求），而未能充分评估当模型被嵌入到一个具备实际执行能力的智能体框架后，风险如何在整个系统生命周期中传播和放大。

本文要解决的核心问题是：**由大模型与智能体框架耦合而成的完整AI智能体系统，其整体安全边界究竟如何？风险暴露点在哪里？** 具体而言，论文试图揭示，安全风险不再仅仅源于模型的不安全文本输出，而是源于**模型能力、工具使用、多步规划与运行时编排之间的复杂交互**所共同塑造的系统级漏洞。为了回答这个问题，研究构建了一个涵盖13个攻击类别、205个测试用例的安全基准，对六种主流的OpenClaw系列智能体框架及其在不同骨干模型下的组合进行了系统性评估。研究发现，所有被评估的智能体都存在显著的安全漏洞，其风险远高于单独使用的骨干模型。其中，信息侦察与发现行为是最普遍的弱点，而不同框架则暴露出各异的的高风险特征，如凭证泄露、横向移动、权限提升和资源开发等。这表明，智能体的安全性是一个系统性问题，需要超越模型层面的防护，进行覆盖全生命周期的安全治理。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**方法类、评测类和应用类**。

在**方法类**研究中，现有工作多集中于提升大语言模型本身的安全性，例如通过指令微调、对齐训练或红队测试来增强模型对恶意指令的识别与拒绝能力。然而，本文指出，仅评估模型本身（model-only evaluation）不足以识别工具增强型AI代理引入的系统性安全风险。本文的研究与这类工作的核心区别在于，它关注的是**模型能力、工具调用、多步规划和运行时编排之间的耦合**如何共同扩大了攻击面，将风险从文本响应层面提升至系统层面。

在**评测类**研究中，已有一些针对大语言模型安全性的基准测试（如AdvBench、HarmBench），但它们通常聚焦于模型在孤立对话中的有害内容生成。本文则构建了一个覆盖智能代理完整执行生命周期的安全基准（包含13个攻击类别、205个测试用例），旨在统一评估**框架层面和模型层面**的风险暴露。这使得本文的评估能系统性地揭示风险如何在代理系统中传播和放大，而这是传统模型级评测无法捕捉的。

在**应用类**研究中，大量工作致力于开发功能强大的AI代理框架（如AutoGPT、LangChain等），强调其任务完成能力和工具使用的便利性。本文所评估的六个OpenClaw系列代理（如OpenClaw、AutoClaw等）即属于此类。本文与这些工作的关系在于，它并非提出新的代理框架，而是**对这些现有框架进行系统的安全评估**，揭示了它们在侦察发现、凭证泄露、横向移动、权限提升等维度的具体脆弱性，从而强调了在追求功能的同时进行全生命周期安全治理的必要性。

### Q3: 论文如何解决这个问题？

论文通过构建一个系统性的安全评估框架来解决工具增强AI代理的安全风险问题。其核心方法是设计一个覆盖智能代理全生命周期的安全基准测试集，并对六种OpenClaw系列代理框架进行统一的、多维度的安全评估。

**整体框架与方法：**
研究首先构建了一个包含205个测试用例的基准测试集。该测试集的设计参考了MITRE ATTACK企业框架，将安全威胁归纳为13个主要类别，包括侦察、资源开发、初始访问、执行、权限提升、防御规避、凭证访问、发现、横向移动、收集、数据渗出和影响。这些测试用例旨在评估代理在理解高风险指令、约束工具调用、控制权限边界和抑制异常行为方面的表现。

**主要模块与评估维度：**
评估并非仅针对底层大语言模型，而是将每个代理框架视为一个完整的系统。评估贯穿了代理执行的整个生命周期链，涵盖了七个关键阶段：
1.  **输入接收层**：评估Web、即时通讯、文件等入口对恶意输入的过滤能力。
2.  **认证与路由层**：评估网关、会话控制等模块在身份欺骗、权限绕过等方面的脆弱性。
3.  **规划与推理层**：评估运行时环境、上下文组装和模型决策过程中可能出现的目标漂移、约束失效等问题。
4.  **工具执行层**：评估技能、插件、系统工具调用时可能出现的越权调用、命令注入等风险。
5.  **状态更新层**：评估长期记忆、知识存储等模块可能遭受的记忆污染、状态篡改等持久化风险。
6.  **结果返回层**：评估输出通道和日志记录可能导致的信息泄露。
7.  **扩展生态系统层**：评估第三方组件和依赖链可能引入的供应链攻击风险。

**创新点与关键技术：**
1.  **系统性安全视角**：突破了传统上仅关注模型提示注入或输出安全的局限，首次将智能代理框架作为一个由多组件（访问层、路由层、业务层、存储层）耦合的复杂系统进行安全分析，揭示了风险分布于全生命周期。
2.  **统一的跨框架基准测试**：设计的基准测试集能够对不同的代理架构（如OpenClaw的分层设计、KimiClaw的桥接架构、ArkClaw的控制/执行平面分离、QClaw的安全沙箱封装、AutoClaw的自动化任务编排）进行横向对比，从而识别出各框架独特的高风险模式。
3.  **揭示风险放大效应**：研究证实，一旦代理被授予执行能力和持久的运行时上下文，在早期阶段（如侦察、发现）出现的弱点，会通过多步规划、工具调用和状态持久化等机制，被放大为具体的系统级故障（如凭证泄漏、横向移动）。
4.  **关联架构与风险画像**：研究将具体的架构设计（如KimiClaw的关键词黑名单、QClaw的安全隔离层）与暴露出的主要风险（如侦察行为普遍脆弱、各框架有 distinct 的高风险项）相关联，明确指出代理系统的安全性由骨干模型的安全属性、以及模型能力、工具使用、多步规划和运行时编排之间的耦合共同塑造。

### Q4: 论文做了哪些实验？

该论文构建了一个包含205个测试用例的基准测试，覆盖了从侦察到影响的13个主要威胁类别（如侦察、资源开发、初始访问、执行、权限提升等），用于系统评估智能代理框架的安全风险。实验设置了六个代表性的OpenClaw系列代理框架（OpenClaw, AutoClaw, QClaw, KimiClaw, MaxClaw, ArkClaw）在多种骨干模型下的表现。对比方法主要是将代理化系统与其底层孤立模型的安全性进行对比。

主要结果显示，所有被评估的代理均存在显著的安全漏洞，代理化系统的风险远高于单独使用的底层模型。具体而言，侦察和发现行为是最常见的弱点。不同框架暴露出不同的高风险特征，包括凭证泄露、横向移动、权限提升和资源开发。关键数据指标包括：在205个测试用例中，代理框架整体上表现出高风险指令理解、工具调用约束、权限边界控制和异常行为抑制方面的不足。实验进一步表明，一旦代理被授予执行能力和持久化运行时上下文，早期阶段出现的弱点会被放大为具体的系统级故障。

### Q5: 有什么可以进一步探索的点？

该论文揭示了当前AI Agent安全评估的局限性，并指出了多个未来研究方向。首先，评估主要集中于OpenClaw系列框架，未来可扩展至更多异构架构（如AutoGPT、LangChain等），以验证安全风险的普适性。其次，测试用例虽覆盖攻击生命周期，但缺乏对新型攻击向量（如工具链污染、记忆篡改、多智能体协同攻击）的探索。此外，评估未深入量化风险传播的动态阈值，例如早期侦察行为如何触发后续攻击的临界条件。

结合个人见解，改进可从三方面入手：一是开发细粒度的实时监控机制，通过行为分析识别“良性探测”到“恶意操作”的过渡，而非依赖静态规则；二是设计安全增强的框架层，例如引入工具执行的动态权限沙箱、多步规划的风险概率评估模块，以弱化模型能力与安全风险的耦合；三是推动跨层安全基准的标准化，将模型安全训练、框架安全策略与环境执行隔离纳入统一评估体系，从而实现对智能体生命周期的整体治理。

### Q6: 总结一下论文的主要内容

该论文对六个基于OpenClaw的代表性AI智能体框架（OpenClaw、AutoClaw、QClaw、KimiClaw、MaxClaw和ArkClaw）进行了系统的安全评估。核心问题是：当大语言模型被集成到具备工具调用、多步规划和状态持久化能力的智能体系统中时，其安全风险会从单纯的提示词滥用演变为涉及整个执行生命周期的系统性漏洞。

研究方法上，作者构建了一个包含205个测试用例的基准，覆盖了从侦察、资源准备到横向移动、数据窃取等13个攻击类别的完整攻击链，旨在统一评估框架层面和模型层面的风险暴露。

主要结论表明，所有被评估的智能体都存在显著的安全漏洞，其风险远高于单独使用底层模型。侦察和发现行为是最普遍的弱点，平均攻击成功率超过65%。不同框架展现出不同的高风险特征，例如凭证泄露、横向移动、权限提升等。研究发现，现代智能体系统的安全性不仅取决于骨干模型的安全属性，更源于模型能力、工具使用、多步规划和运行时编排之间的耦合作用。一旦智能体获得执行能力和持久化上下文，早期阶段的弱点会被放大为具体的系统级故障。因此，论文强调需要超越提示词层面的防护，转向覆盖整个生命周期的智能体框架安全治理。
