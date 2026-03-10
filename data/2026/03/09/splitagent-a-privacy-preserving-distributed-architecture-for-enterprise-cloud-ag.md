---
title: "SplitAgent: A Privacy-Preserving Distributed Architecture for Enterprise-Cloud Agent Collaboration"
authors:
  - "Jianshu She"
date: "2026-03-09"
arxiv_id: "2603.08221"
arxiv_url: "https://arxiv.org/abs/2603.08221"
pdf_url: "https://arxiv.org/pdf/2603.08221v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Privacy-Preserving"
  - "Enterprise Agent"
  - "Tool Use"
  - "Distributed Systems"
  - "Differential Privacy"
  - "Context-Aware"
relevance_score: 8.0
---

# SplitAgent: A Privacy-Preserving Distributed Architecture for Enterprise-Cloud Agent Collaboration

## 原始摘要

Enterprise adoption of cloud-based AI agents faces a fundamental privacy dilemma: leveraging powerful cloud models requires sharing sensitive data, while local processing limits capability. Current agent frameworks like MCP and A2A assume complete data sharing, making them unsuitable for enterprise environments with confidential information. We present SplitAgent, a novel distributed architecture that enables privacy-preserving collaboration between enterprise-side privacy agents and cloud-side reasoning agents. Our key innovation is context-aware dynamic sanitization that adapts privacy protection based on task semantics -- contract review requires different sanitization than code review or financial analysis. SplitAgent extends existing agent protocols with differential privacy guarantees, zero-knowledge tool verification, and privacy budget management. Through comprehensive experiments on enterprise scenarios, we demonstrate that SplitAgent achieves 83.8\% task accuracy while maintaining 90.1\% privacy protection, significantly outperforming static approaches (73.2\% accuracy, 79.7\% privacy). Context-aware sanitization improves task utility by 24.1\% over static methods while reducing privacy leakage by 67\%. Our architecture provides a practical path for enterprise AI adoption without compromising sensitive data.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决企业在采用云端AI智能体时面临的核心隐私困境：如何既能利用强大云端模型的能力，又能保护企业内部的敏感数据不被泄露。研究背景是，随着大语言模型的快速发展，AI智能体为企业自动化带来了巨大潜力，但最先进的能力通常部署在云端，需要企业上传数据，这与保护客户信息、财务记录、知识产权和合规文件等机密数据的需求直接冲突。

现有方法存在明显不足。当前主流的智能体协作框架，如Anthropic的模型上下文协议和谷歌的智能体间协议，都建立在参与者完全信任和完全数据共享的假设之上，无法适用于企业数据敏感、云端不可信的协作场景。这迫使企业做出二元选择：要么将所有处理限制在本地，牺牲AI能力；要么将全部数据上传云端，牺牲隐私安全。此外，现有的数据脱敏方法往往是静态和一刀切的，无法根据不同的任务语义（如合同审查、代码审计、财务分析）进行差异化、精细化的隐私保护，导致在保护隐私的同时严重损害了任务效用。

因此，本文要解决的核心问题是：设计一种隐私保护的分布式架构，使得企业端的隐私智能体与云端推理智能体能够安全、高效地协作。具体而言，论文提出了SplitAgent架构，其核心创新在于实现**基于任务语义的上下文感知动态脱敏**，即根据任务类型动态调整数据保护策略，在最大化任务效用的同时提供形式化的隐私保证，从而在隐私保护与AI能力之间取得更优的平衡。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：隐私保护技术、企业AI应用框架以及现有智能体协议。

在**隐私保护技术**方面，相关工作包括差分隐私（为数据或查询添加噪声提供形式化保证）、联邦学习（支持去中心化协作训练）、安全多方计算（允许在不暴露私有输入的情况下进行联合计算）以及同态加密（支持密文计算）。此外，文本匿名化和PII检测工具也是基础技术。然而，这些方法通常需要在效用或性能上做出牺牲，或带来显著的计算开销。本文的SplitAgent则专注于在保持企业任务高效用前提下的实用隐私保护，并引入了上下文感知的动态脱敏机制。

在**企业AI应用框架**方面，已有研究探索了数据保险库架构、机密计算和结构化透明性等方法，以应对数据治理、合规性等独特挑战。传统方法如数据防泄漏工具和访问控制，对于需要广泛数据访问的AI系统往往不足。本文工作提供了一个实用的折中方案，在满足企业隐私要求的同时利用云端AI能力。

在**现有智能体协议与框架**方面，相关工作包括Anthropic的模型上下文协议、Google的Agent-to-Agent协议以及微软的AutoGen框架。这些框架依赖于标准化通信协议，支持智能体间的协调与协作，但均假设智能体间完全信任，缺乏隐私保护机制，所有数据共享均为明文传输。本文工作（SplitAgent）的关键区别与贡献在于，它扩展了这些现有协议，通过引入差分隐私保证、零知识工具验证和隐私预算管理等隐私保护原语，实现了企业侧隐私代理与云端推理代理之间的隐私保护协作，同时保持了兼容性。

### Q3: 论文如何解决这个问题？

论文通过提出名为SplitAgent的新型分布式架构来解决企业-云协作中的隐私困境。其核心方法是采用“分割式”设计，将数据处理与复杂推理分离，分别部署在企业侧（隐私代理）和云侧（推理代理），两者通过安全协议协作。

整体框架包含两大主要组件：企业侧的**隐私代理**和云侧的**推理代理**。隐私代理作为企业敏感数据的守护者，包含多个关键模块：**数据控制器**负责管理所有敏感数据的访问；**上下文净化器**是实现创新的核心，它根据任务语义动态应用净化策略，而非静态规则；**本地RAG引擎**在企业内部完成文档检索与摘要生成，避免原始文档外泄；**隐私预算管理器**跟踪和管理交互中的累积隐私消耗；**工具执行器**在本地运行敏感操作。云侧的推理代理则专注于对净化后的抽象数据进行高级分析，其模块包括**任务规划器**、**逻辑推理器**、**策略生成器**和**抽象合成器**，它们利用大语言模型进行规划、因果分析和生成建议，但全程不接触原始数据。

关键技术及创新点主要体现在**上下文感知的动态净化**算法上。该算法根据任务类型（如合同审查、代码审查、财务分析）动态调整净化策略，在移除或抽象化敏感实体（如姓名、金额、日期）的同时，最大限度地保留任务所需的语义结构和功能关系。例如，合同审查会保留法律条款关系但抽象具体方和金额；代码审查会保留语法和API模式但移除凭证。此外，架构还集成了差分隐私保证、零知识工具验证和隐私预算管理等技术，在协议层面进行了扩展。通过这种任务语义驱动的、动态的隐私-效用权衡机制，SplitAgent在保护隐私的同时显著提升了任务完成的准确性和实用性。

### Q4: 论文做了哪些实验？

实验设置方面，论文构建了包含合同、代码库、财务文档和客服记录等企业数据的合成数据集，文档大小从1KB到100KB不等。评估了六种企业场景：合同审查、代码审计、财务分析、客户支持、风险评估和合规检查。对比方法包括：全云端（无隐私保护）、全本地（能力受限）、静态分割（固定脱敏规则）以及本文提出的SplitAgent（上下文感知动态脱敏）。

主要结果如下：SplitAgent在任务准确率和隐私保护之间取得了最佳平衡，达到83.8%的准确率和90.1%的隐私保护率，显著优于静态方法（73.2%准确率，79.7%隐私保护）。上下文感知脱敏相比静态正则表达式方法将任务效用提升了24.1%，相比静态NER方法提升了15.2%，并在客户支持任务中取得最高效用（94.2%）。在隐私预算管理方面，SplitAgent的智能分配策略实现了34.2的总效用和96%的任务完成率，优于朴素分配（24.3效用）。攻击抵抗测试显示，SplitAgent将平均攻击成功率降至11%，相比静态掩码降低了89%，尤其在可链接性攻击上成功率仅为6.7%。此外，实验确定了隐私效用权衡的最优点在ε=0.5，此时准确率为83.4%，隐私保护率为94.5%。在不同企业场景中，SplitAgent平均保持了84.8%的任务完成率、86.6%的质量和89.6%的隐私保护。

### Q5: 有什么可以进一步探索的点？

该论文提出的SplitAgent架构在隐私保护与任务效用间取得了良好平衡，但仍存在若干局限性和可深入探索的方向。局限性方面：首先，系统假设企业侧隐私代理环境绝对安全，若其被攻破则整体隐私保护失效，存在单点故障风险；其次，即使采用上下文感知的脱敏，仍导致8-15%的效用损失，对于需要细粒度细节的分析任务（如精确的财务欺诈检测）可能影响较大；此外，200-500毫秒的脱敏延迟虽对多数工作流可接受，但制约了实时性要求高的应用。

未来研究方向可围绕以下几点展开：一是**增强隐私技术融合**，探索将同态加密或安全多方计算与现有动态脱敏结合，在更强隐私保证下减少效用损失。二是**发展自适应隐私预算机制**，不仅基于任务语义，还可结合查询历史、数据敏感度动态调整差分隐私参数，实现更精细的管控。三是**拓展多方协作场景**，研究多个企业（如供应链上下游）在异构隐私要求下的代理协作协议与信任机制。四是**推进形式化验证**，为隐私保证和安全属性提供数学证明，增强系统可信度。此外，可探索利用联邦学习等技术在保护隐私的同时提升云端推理模型对脱敏数据的理解能力，以进一步缩小效用差距。

### Q6: 总结一下论文的主要内容

本文针对企业采用云端AI代理时面临的隐私困境，提出了一种名为SplitAgent的新型分布式架构。核心问题是现有代理框架要求完全共享数据，无法满足企业处理敏感信息时的隐私需求。该架构的核心贡献在于实现了企业端隐私代理与云端推理代理之间的隐私保护协作，其关键创新是引入了基于任务语义的上下文感知动态脱敏机制，能够根据合同审查、代码审查或财务分析等不同任务动态调整隐私保护强度。方法上，SplitAgent扩展了现有代理协议，整合了差分隐私保证、零知识工具验证和隐私预算管理。实验结果表明，该架构在保持90.1%隐私保护水平的同时，实现了83.8%的任务准确率，显著优于静态方法。上下文感知脱敏将任务效用提升了24.1%，同时将隐私泄露降低了67%。该研究为企业在不泄露敏感数据的前提下利用云端强大AI能力提供了一条可行的技术路径。
