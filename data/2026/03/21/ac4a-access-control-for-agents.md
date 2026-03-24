---
title: "AC4A: Access Control for Agents"
authors:
  - "Reshabh K Sharma"
  - "Dan Grossman"
date: "2026-03-21"
arxiv_id: "2603.20933"
arxiv_url: "https://arxiv.org/abs/2603.20933"
pdf_url: "https://arxiv.org/pdf/2603.20933v1"
github_url: "https://github.com/reSHARMA/AC4A"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.PL"
tags:
  - "Agent Security"
  - "Access Control"
  - "Agent Framework"
  - "Tool Use"
  - "API Interaction"
  - "Web Interaction"
  - "Autonomous Agents"
  - "Trust and Safety"
relevance_score: 7.5
---

# AC4A: Access Control for Agents

## 原始摘要

Large Language Model (LLM) agents combine the chat interaction capabilities of LLMs with the power to interact with external tools and APIs. This enables them to perform complex tasks and act autonomously to achieve user goals. However, current agent systems operate on an all-or-nothing basis: an agent either has full access to an API's capabilities and a web page's content, or it has no access at all. This coarse-grained approach forces users to trust agents with more capabilities than they actually need for a given task.
  In this paper, we introduce AC4A, an access control framework for agents. As agents become more capable and autonomous, users need a way to limit what APIs or portions of web pages these agents can access, eliminating the need to trust them with everything an API or web page allows. Our goal with AC4A is to provide a framework for defining permissions that lets agents access only the resources they are authorized to access. AC4A works across both API-based and browser-based agents. It does not prescribe what permissions should be, but offers a flexible way to define and enforce them, making it practical for real-world systems.
  AC4A works by creating permissions granting access to resources, drawing inspiration from established access control frameworks like the one for the Unix file system. Applications define their resources as hierarchies and provide a way to compute the necessary permissions at runtime needed for successful resource access. We demonstrate the usefulness of AC4A in enforcing permissions over real-world APIs and web pages through case studies. The source code of AC4A is available at https://github.com/reSHARMA/AC4A

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在访问外部资源时缺乏细粒度权限控制的问题。研究背景是，随着LLM从被动问答系统演变为能够通过API和网页浏览器与外部世界交互的主动智能体，它们能够执行预订旅行、管理日历等复杂任务，但当前的智能体系统在资源访问上采用“全有或全无”的粗放模式：智能体要么拥有对API全部功能或网页全部内容的完全访问权，要么完全无权访问。现有方法的不足在于，这种模式迫使用户必须授予智能体远超其完成任务实际所需的权限，导致过度信任和潜在的安全风险。例如，让智能体在日历中创建一个事件，就不得不授予其访问整个日历API的权限，这可能允许智能体查看、修改所有现有事件，或在任意时间创建事件；类似地，基于浏览器的智能体在查看日历时会获取整个页面的访问权，包括其他敏感条目和个人信息。本文要解决的核心问题是：如何为LLM智能体设计一个统一的访问控制框架，使其能够根据任务需要，以细粒度的方式限制智能体对API或网页特定部分的访问，从而在保障功能的同时最小化权限，降低资源滥用风险。为此，论文提出了AC4A框架，它允许应用程序以层次化结构定义资源，并在运行时计算和强制执行所需权限，为API驱动和浏览器驱动的智能体提供统一的权限管理基础设施。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕LLM智能体安全、访问控制机制以及现有智能体系统的局限性展开，可分为以下几类：

**1. 智能体安全与风险研究**：已有大量工作关注LLM智能体的安全挑战，如幻觉、提示注入攻击、恶意指令隐藏等。这些研究主要聚焦于模型层面的防御，与本文关注的**资源访问控制**不同。本文认为访问控制是解决其他安全问题的先决条件，而非直接缓解这些风险。

**2. 传统访问控制系统**：本文的设计灵感来源于成熟的访问控制框架，如Unix文件系统的权限模型。这些系统为传统软件提供了细粒度的资源管理，但并未针对LLM智能体的动态、交互式特性进行适配。本文的AC4A框架借鉴了其分层资源和权限表示的思想，并将其扩展到API和浏览器两种智能体环境。

**3. 现有智能体系统的权限管理**：当前主流的LLM智能体平台（如LangChain、AutoGPT等）在权限管理上通常采用“全有或全无”的粗粒度模式，即智能体要么拥有对某个API或网页的完全访问权，要么完全无法访问。本文明确指出，这种模式迫使用户授予智能体超出任务实际所需的权限，存在信任与安全风险。AC4A的核心贡献正是解决了这一局限，首次为浏览器智能体提供了资源级访问控制，并首次实现了API与浏览器智能体权限执行的统一框架。

**4. 新兴的智能体安全框架**：近期开始出现一些针对智能体安全的设计，但多集中于特定攻击的防御或可信执行环境等方面。AC4A与这些工作的区别在于，它专注于**通用的、可定义的权限基础设施**，不规定具体的权限策略，而是提供一个灵活的框架来定义和执行权限，从而能够实用地集成到现实系统中。

### Q3: 论文如何解决这个问题？

论文通过设计并实现一个名为AC4A的访问控制框架来解决LLM代理当前“全有或全无”的粗粒度权限问题。其核心方法是引入一个灵活、可定义的权限模型，该模型独立于具体应用语义，允许用户为代理授予细粒度的、仅满足任务所需的最小权限。

**整体框架与核心组件**：AC4A框架的核心是**权限（Permission）**，它由**资源值规范（Resource Value Specification）**和**操作（Action）**两部分组成。资源被组织成**资源类型树（Resource Type Tree）**，这是一种有向路径结构，根节点代表最广泛的资源集合，子节点代表更具体的子集。例如，日历资源可以按“年::月::日”的层次建模，文件系统可以按“目录::文件”递归建模。资源值规范则用于指定具体的资源实例或集合，支持使用通配符“?”。操作（如read、write、create）由应用自行定义，代表对资源的访问类型。

**关键技术机制**：
1.  **权限定义与建模**：应用开发者首先为其资源定义资源类型树和操作集。资源被建模为不透明的实体，AC4A不关心其具体语义，只关注其层次结构和包含关系。这种设计使得框架能适用于API和网页内容等多种代理环境。
2.  **权限检查算法**：当代理尝试访问资源时，系统需要判断其已被授予的权限是否覆盖访问所需权限。这是通过一个名为 **`resource_difference`** 的关键函数实现的。该函数由每个应用根据其资源模型自行实现，其功能是计算“所需资源集合”减去“已有资源集合”后“剩余的未满足资源集合”。
3.  **算法工作流程**：权限检查算法（如论文中Algorithm 1所示）为每个所需操作独立运行。它初始化一个剩余需求集合，然后遍历代理已被授予的对应权限，反复调用`resource_difference`函数，从剩余需求中减去已覆盖的部分。如果最终所有操作的剩余需求集合均为空，则访问被允许；否则被拒绝。

**创新点**：
*   **灵活的、声明式的权限模型**：借鉴Unix文件系统权限思想，但通过资源类型树和资源值规范提供了更通用和可定制的资源建模能力，支持层次化、区间化乃至递归的资源表示。
*   **应用定义的计算逻辑**：将权限覆盖判断的核心逻辑（`resource_difference`）下放给应用开发者，框架只提供执行引擎和保证安全性的约束（即函数输出不能超出原始需求范围）。这使得框架能适配各种复杂的、领域特定的资源语义（如时间区间、最近N笔交易等）。
*   **最小权限原则的实施**：通过上述机制，系统能够精确地判断一组授予的权限是否恰好满足（或超过）一次访问请求所需的最小权限集，从而在理论上实现了对代理访问能力的细粒度控制，避免了过度授权。

### Q4: 论文做了哪些实验？

论文通过案例研究（case studies）来验证AC4A框架在现实世界API和网页上实施权限控制的有效性。实验设置上，作者将AC4A应用于基于API的智能体（如日历、文件系统、信用卡交易）和基于浏览器的智能体（与网页内容交互）两种典型场景，以展示其通用性。

数据集/基准测试方面，实验并未使用标准化的公共基准，而是选取了具有代表性的实际应用场景作为案例。具体包括：1) 日历API（资源可按日期层次或Unix时间间隔建模）；2) 类Unix文件系统API（递归目录结构）；3) 信用卡信息模型（包含重叠的访问路径）；4) 网页内容（控制对特定DOM元素的访问）。这些案例覆盖了层次化、区间化、递归等多种资源类型。

对比方法主要针对当前智能体系统普遍采用的“全有或全无”（all-or-nothing）的粗粒度访问控制模式。AC4A的核心创新在于引入了细粒度的、基于权限声明的访问控制，因此实验重点是通过具体案例展示AC4A如何实现比现有模式更精细、更灵活的控制能力，而非与某个特定算法进行量化指标对比。

主要结果与关键数据指标：实验通过设计具体的权限策略并演示智能体的访问过程，定性证明了AC4A能够成功实施细粒度控制。例如，可以授予智能体仅读取“2026年1月所有信用卡交易”或“`/home`下任意子目录中名为`report.txt`的文件”的权限，而非整个API或网页的完全访问权。权限检查算法（Algorithm 1）利用应用定义的`resource_difference`函数，能正确判断授予的权限集是否覆盖访问所需权限集，从而决定允许或拒绝访问。框架的灵活性体现在支持通配符（`?`）、多种资源建模方式以及自定义操作（如read, write, create），且其实现是开源的。这些案例共同表明，AC4A提供了一种实用的框架，能够定义和执行细粒度权限，减少用户对智能体的过度信任。

### Q5: 有什么可以进一步探索的点？

该论文提出的AC4A框架为Agent的访问控制提供了重要基础，但仍存在一些局限性和可拓展方向。首先，其权限模型主要借鉴类Unix文件系统的层级结构，虽具通用性，但可能无法灵活适应动态、上下文相关的细粒度授权需求，例如基于会话状态或用户历史行为的临时权限。其次，框架侧重于静态权限定义与执行，缺乏对权限动态调整与风险自适应控制机制的支持，未来可引入实时监控与异常行为检测，实现风险感知的访问控制。此外，论文未深入探讨多Agent协作场景下的权限委托与联合授权问题，这在复杂工作流中尤为重要。从实践角度看，AC4A目前依赖应用层主动定义资源与权限计算逻辑，未来可探索自动化资源发现与权限策略生成技术，结合大语言模型理解API文档或网页结构，降低部署成本。最后，框架的安全性验证仍限于案例研究，需进一步进行形式化安全分析和大规模系统测试，以评估其在对抗性环境下的鲁棒性。

### Q6: 总结一下论文的主要内容

本文针对当前LLM智能体系统存在的访问控制问题，提出了一种名为AC4A的细粒度访问控制框架。当前系统通常采用“全有或全无”的粗粒度授权模式，导致用户不得不授予智能体超出任务实际需要的权限，存在资源滥用风险。AC4A旨在解决此问题，为智能体访问外部API和网页内容提供统一的权限管理机制。

该框架的核心方法是借鉴Unix文件系统的成熟设计，将应用程序资源组织为层次化结构，并允许在运行时动态计算访问所需权限。权限由资源标识和应用程序定义的操作（如读、写）组成。框架通过拦截智能体对API或网页的调用，仅在存在明确授权时才允许访问相应资源。AC4A不规定具体的权限策略，而是提供了一个灵活的定义和执行框架，可同时适用于基于API和基于浏览器的智能体。

论文通过案例研究验证了AC4A在实际API和网页权限控制中的有效性。其主要贡献在于首次为基于浏览器的智能体提供了资源级访问控制，并首次统一了两种智能体的权限执行机制。该框架为构建更安全、可信的自主智能体系统奠定了基础，使用户能够精确限制智能体的资源访问范围，而无需过度授权。
