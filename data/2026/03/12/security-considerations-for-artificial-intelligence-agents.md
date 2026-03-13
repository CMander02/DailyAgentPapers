---
title: "Security Considerations for Artificial Intelligence Agents"
authors:
  - "Ninghui Li"
  - "Kaiyuan Zhang"
  - "Kyle Polley"
  - "Jerry Ma"
date: "2026-03-12"
arxiv_id: "2603.12230"
arxiv_url: "https://arxiv.org/abs/2603.12230"
pdf_url: "https://arxiv.org/pdf/2603.12230v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CR"
tags:
  - "Agent Security"
  - "Multi-Agent Systems"
  - "Risk Management"
  - "Attack Surfaces"
  - "Defense Mechanisms"
  - "Policy & Standards"
relevance_score: 7.5
---

# Security Considerations for Artificial Intelligence Agents

## 原始摘要

This article, a lightly adapted version of Perplexity's response to NIST/CAISI Request for Information 2025-0035, details our observations and recommendations concerning the security of frontier AI agents. These insights are informed by Perplexity's experience operating general-purpose agentic systems used by millions of users and thousands of enterprises in both controlled and open-world environments. Agent architectures change core assumptions around code-data separation, authority boundaries, and execution predictability, creating new confidentiality, integrity, and availability failure modes. We map principal attack surfaces across tools, connectors, hosting boundaries, and multi-agent coordination, with particular emphasis on indirect prompt injection, confused-deputy behavior, and cascading failures in long-running workflows. We then assess current defenses as a layered stack: input-level and model-level mitigations, sandboxed execution, and deterministic policy enforcement for high-consequence actions. Finally, we identify standards and research gaps, including adaptive security benchmarks, policy models for delegation and privilege control, and guidance for secure multi-agent system design aligned with NIST risk management principles.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决前沿人工智能（AI）代理所面临的新型安全挑战。研究背景是AI代理系统（尤其是通用型代理）的快速发展和广泛应用，它们被数百万用户和数千家企业用于受控和开放环境。然而，传统的安全假设（如代码与数据分离、权限边界清晰、执行可预测）在代理架构中被打破，导致机密性、完整性和可用性方面出现新的失效模式。现有方法往往基于传统软件安全模型，未能充分应对代理特有的攻击面，例如工具、连接器、托管边界和多代理协调中的漏洞，特别是间接提示注入、权限混淆代理行为以及长时工作流中的级联故障等问题。

因此，本文的核心问题是：如何系统性地识别、评估和防御AI代理架构引入的安全风险。论文通过映射主要攻击面，分析现有防御措施（如输入层和模型层缓解、沙箱执行、高后果行动的确定性策略执行）的不足，并指出标准与研究空白，旨在为设计安全的AI代理系统提供实践观察和建议，以应对其独特的安全威胁。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及AI Agent安全领域，可从方法、应用与评测等角度梳理。

**方法类研究**主要关注传统软件安全机制在AI Agent环境中的适用性。例如，针对代码与数据分离原则，传统研究集中于防范SQL注入、跨站脚本等攻击，但本文指出AI Agent进一步模糊了代码与数据的界限（如提示词即代码），导致传统防御机制失效。此外，传统安全机制（如沙箱、最小权限原则）多基于确定性和可预测的行为假设，而AI Agent的自主性和非确定性行为需要新的安全抽象和动态权限控制模型。

**应用类研究**聚焦于实际系统中的安全漏洞与攻击案例。例如，文中提及的OpenClaw安全事件（CVE-2026-25253等）揭示了AI Agent在文件访问、消息平台集成中的风险。相关研究也涉及多智能体系统中的攻击面扩展，如间接提示注入、权限混淆攻击（confused-deputy）和级联故障。本文在此基础上系统化分析了攻击面（工具、连接器、多智能体协调等），并强调长时工作流中的风险传播。

**评测与标准类研究**则关注安全基准和风险管理框架。本文呼应NIST风险管理原则，指出当前缺乏针对AI Agent的自适应安全基准、委托策略模型以及多智能体系统安全设计指南。相关研究多集中于传统AI模型安全（如对抗样本），而本文强调需针对Agent的动态工作流和复杂交互制定专项评测标准。

本文与这些工作的关系在于：**整合了实践经验与理论分析**，基于Perplexity在开放和受控环境中的运营经验，系统梳理了Agent特有的安全威胁（如机密性、完整性、可用性失效模式），并提出了分层防御框架（输入/模型级缓解、沙箱执行、确定性策略执行）。其区别在于：**更强调Agent架构对核心安全假设的根本性改变**（如代码数据分离、权限边界、执行可预测性），并突出了多智能体协调中的新型风险，而非仅关注单一Agent或传统AI模型的安全问题。

### Q3: 论文如何解决这个问题？

论文通过构建一个纵深防御（Defense-in-Depth）的多层技术框架来解决AI智能体系统的安全问题，其核心思路是结合多种互补的防御机制，而非依赖单一方案。整体框架包含三个主要防御层级：输入级防御、模型级防御以及系统级防御（包括执行监控和确定性最后防线）。

**1. 输入级防御**：作为第一道防线，旨在恶意输入被AI模型处理前进行检测或缓解。具体方法包括：检测攻击（如通过计算输入困惑度、查询LLM自身或验证响应有效性）、训练专用检测器识别恶意提示，以及采用“聚光灯”（spotlighting）和“三明治”（sandwiching）等技术修改输入以降低攻击影响。然而，该层面临误报率高（由于良性输入远多于恶意输入）、计算成本高以及在实时智能体工作流中累积延迟等挑战，因此无法单独提供可靠保护。

**2. 模型级防御**：重点在于增强模型自身对攻击的抵抗力，试图重建代码与数据的分离。关键创新点在于利用“指令层次结构”（instruction hierarchy），通过训练使LLM对不同角色（如系统、用户、助手）的指令赋予不同优先级。更先进的方法（如Wu等人的研究）在嵌入层对角色进行编码，为不同输入段分配独立嵌入，从而在底层强化权限层次。但论文指出，角色边界仍是学习到的约定而非硬性安全保证，容易受到对抗性影响，且模型存在近因偏差和服从性偏差，因此模型级防御也无法独立构成完整解决方案。

**3. 系统级防御**：该层包括两个关键组件。首先是**执行监控与沙箱化**，通过沙箱环境运行智能体，并基于策略控制资源访问和交互。例如，CaMeL框架采用特权LLM处理可信用户查询并生成计划，同时使用隔离LLM处理不可信外部数据，并通过能力感知的数据流跟踪确保受污染变量不影响特权操作。这体现了最小权限和完全中介等安全原则。其次是**确定性最后防线**，作为硬性保护边界，使用可验证的传统代码（如工具调用白名单/黑名单、敏感操作速率限制、参数正则表达式验证）来阻断禁止行为，无论LLM输出为何。这一层不依赖于模型的统计特性，提供了确定性的安全保障。

**创新点与整体架构**：论文的创新在于系统性地将经典安全原则（如Saltzer-Schroeder原则）适配于AI智能体领域，并明确提出一个分层协同的防御体系。三层防御各司其职：输入级减少攻击量，模型级提高攻击成功门槛，系统级强制执行硬性限制以控制后果。这种组合策略针对智能体架构带来的代码-数据分离模糊、权限边界弱化和执行不可预测性等新假设，有效应对了间接提示注入、权限混淆和级联故障等新兴威胁。论文最终倡导基于此框架建立分层防御参考架构，以指导安全实践。

### Q4: 论文做了哪些实验？

论文围绕AI智能体系统的安全实践，重点探讨了针对间接提示注入攻击的多层防御措施。实验设置主要基于理论分析和现有研究综述，未描述具体的独立实验，但引用了多项相关研究来支撑论点。

在数据集/基准测试方面，论文提及了Liu等人的研究，他们评估了多种提示注入检测策略，包括测量输入困惑度、查询LLM本身以及验证响应的有效性。此外，还引用了Wu等人的工作，他们通过在嵌入层面编码角色区分来强化指令层次结构。这些研究通常使用包含恶意和良性提示的混合数据集进行评估，但论文未具体说明基准名称。

对比方法涵盖了输入级、模型级和系统级三个防御层级。输入级防御包括检测攻击（如基于困惑度、专用检测器或内部模型信号）、移除恶意内容或使用聚光灯/三明治等技术修改输入。模型级防御侧重于通过指令层次结构或角色嵌入训练模型增强抵抗力。系统级防御则涉及沙箱执行（如CaMeL框架）和确定性策略执行（如工具允许列表、速率限制）。

主要结果指出，当前防御措施的成熟度各异：输入级检测和模型级防御处于学术研究早期，虽有初步部署，但单独使用均不可靠；而系统级的确定性执行机制（如工具允许列表、人工确认）已在生产系统中广泛部署，最为成熟。关键结论是，任何单层防御都不足以应对自适应攻击，必须采用深度防御策略，结合输入级（减少攻击量）、模型级（提高攻击门槛）和系统级（硬性限制后果）三层，才能实现当前最鲁棒的防护。论文建议NIST和CAISI制定分层防御参考架构，供实践者参考。

### Q5: 有什么可以进一步探索的点？

该论文指出了当前AI智能体安全实践的几大局限性，为未来研究提供了明确方向。首先，在技术标准层面，现有的智能体通信协议（如MCP、A2A）主要关注底层认证和传输安全，缺乏对自主多智能体环境中高级安全挑战（如安全委托、跨智能体信任边界、权限管理）的系统性解决方案。开发框架的安全模型也尚不成熟，尤其在智能体间的权限分离、交互授权和委托链控制方面存在明显缺口。

未来研究应聚焦几个关键领域。一是建立动态、对抗性的安全评估基准。当前静态测试集容易高估系统安全性，亟需能模拟开放环境中多步骤、自适应攻击路径的评估方法，以真实衡量智能体系统的韧性。二是在访问控制模型方面，需设计适合智能体系统的确定性策略执行层。结合角色访问控制（RBAC）与风险自适应控制，形成可扩展的混合授权模型，能在保持灵活性的同时实施可靠的聚合风险限制。三是人机协同治理机制。当前依赖人工确认的“安全阀”设计存在可用性与安全性的根本矛盾，容易导致用户疲劳而削弱防护效果。未来需探索基于风险感知的自主决策框架，让智能体根据用户预设的风险容忍度动态请求确认，或通过学习用户偏好减少不必要的打断，同时通过定期透明报告（如行动摘要、风险快照）维持用户的态势感知，从而实现安全与自动化效率的平衡。

### Q6: 总结一下论文的主要内容

该论文基于Perplexity公司的实践经验，系统探讨了前沿AI智能体的安全挑战与防御策略。核心问题是智能体架构打破了传统代码与数据分离、权限边界和执行可预测性等假设，引发了新的机密性、完整性和可用性风险。论文方法上全面映射了攻击面，包括工具、连接器、托管边界和多智能体协调等层面，重点分析了间接提示注入、权限混淆和长时工作流中的级联故障等新型威胁。防御策略被构建为分层体系，涵盖输入级与模型级缓解、沙箱化执行以及对高影响行动的确定性策略强制执行。主要结论指出，未来需建立自适应安全基准、适用于委托与权限控制的策略模型，并依据NIST风险管理原则设计安全的多智能体系统。该研究为AI智能体的安全工程化提供了系统化框架，对行业实践与标准制定具有重要指导意义。
