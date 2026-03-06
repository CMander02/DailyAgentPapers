---
title: "EVMbench: Evaluating AI Agents on Smart Contract Security"
authors:
  - "Justin Wang"
  - "Andreas Bigger"
  - "Xiaohai Xu"
  - "Justin W. Lin"
  - "Andy Applebaum"
  - "Tejal Patwardhan"
  - "Alpin Yukseloglu"
  - "Olivia Watkins"
date: "2026-03-05"
arxiv_id: "2603.04915"
arxiv_url: "https://arxiv.org/abs/2603.04915"
pdf_url: "https://arxiv.org/pdf/2603.04915v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CR"
tags:
  - "Agent Evaluation"
  - "Agent Benchmark"
  - "Tool Use"
  - "Code Understanding"
  - "Security"
relevance_score: 7.5
---

# EVMbench: Evaluating AI Agents on Smart Contract Security

## 原始摘要

Smart contracts on public blockchains now manage large amounts of value, and vulnerabilities in these systems can lead to substantial losses. As AI agents become more capable at reading, writing, and running code, it is natural to ask how well they can already navigate this landscape, both in ways that improve security and in ways that might increase risk. We introduce EVMbench, an evaluation that measures the ability of agents to detect, patch, and exploit smart contract vulnerabilities. EVMbench draws on 117 curated vulnerabilities from 40 repositories and, in the most realistic setting, uses programmatic grading based on tests and blockchain state under a local Ethereum execution environment. We evaluate a range of frontier agents and find that they are capable of discovering and exploiting vulnerabilities end-to-end against live blockchain instances. We release code, tasks, and tooling to support continued measurement of these capabilities and future work on security.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何系统评估AI智能体在智能合约安全领域能力的问题。随着公链上智能合约管理着巨额资产，其漏洞可能导致重大损失，而AI智能体在代码读写和执行方面日益增强的能力，既可能提升安全，也可能增加风险。研究背景是区块链已成为成熟金融基础设施，大量资产托管于开源智能合约中，但现有评估方法多集中于传统网络安全漏洞或简化的子任务环境，缺乏对真实漏洞从发现、修复到利用全周期的综合评估。现有方法的不足在于它们未能模拟智能合约安全的完整操作链条，尤其是在利用环节缺乏与真实区块链环境的交互和基于链上状态的程序化验证。本文的核心问题是构建一个全面、真实的评估框架（EVMbench），以衡量AI智能体在检测、修补和利用智能合约漏洞方面的端到端能力，特别是在最接近实际的设置中，通过本地以太坊执行环境，基于测试和区块链状态进行自动化评分，从而监控AI智能体在安全关键领域的能力发展，为部署决策和防御措施提供依据。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为智能合约安全评测、AI代理评估以及自动化安全工具三类。

在**智能合约安全评测**方面，已有多个基准测试集（如SmartBugs、SolidiFI）专注于静态漏洞检测，通常提供合约代码和预定义漏洞标签。本文的EVMbench与之不同，它强调端到端的动态评估：不仅要求代理识别漏洞，还需在真实的本地EVM环境中通过执行交易来验证漏洞的利用或修复，并引入程序化评分（基于测试和链状态变化），从而更贴近实际安全任务（如审计竞赛或攻击模拟）。

在**AI代理评估**领域，现有工作（如SWE-bench、AgentBench）多评估代理在通用编程或网页交互等任务上的表现。EVMbench则首次将评估场景聚焦于区块链智能合约安全这一高风险、经济激励驱动的领域。它要求代理理解状态变化、经济激励及协议组合，这比传统代码生成或理解任务更复杂，模拟了“黑暗森林”般的对抗环境。

在**自动化安全工具**方面，已有静态分析器（如Slither）、符号执行工具（如Manticore）和模糊测试框架（如Echidna）。这些工具通常是专门化的、规则驱动的。本文评估的AI代理则作为通用智能体，旨在通过自然语言交互完成多步骤安全任务（检测、修补、利用），其能力覆盖范围更广，但当前性能可能不及专用工具。EVMbench的发布为衡量和推动AI代理在此类专业领域的进步提供了基准。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为EVMbench的综合性评估框架来解决智能合约安全领域中AI代理能力的评测问题。其核心方法围绕三个关键评估模式（Detect、Patch、Exploit）展开，旨在全面衡量AI代理在漏洞发现、修复和利用方面的端到端能力。

整体框架基于一个精心构建的基准测试集，该测试集从Code4rena等平台的40个审计仓库中精选了117个高严重性漏洞。评估在一个隔离的Ubuntu Docker容器环境中进行，模拟了真实审计场景，并为代理提供了完整的代码库和必要的开发工具（如Foundry）。框架的核心创新在于其分模式的程序化评分机制和高度真实的执行环境。

主要模块与关键技术包括：
1.  **任务与数据集构建模块**：通过严格筛选（仅保留可导致资金损失的高危漏洞）和人工审查，确保任务的可行性与相关性。数据集涵盖了传统审计漏洞和新兴稳定币支付等实际场景。
2.  **多模式评估引擎**：
    *   **Detect（检测）模式**：评估代理发现漏洞的能力。代理需生成审计报告，评分基于与基准报告的对比，采用模型判官（model-based judge）自动判断漏洞是否被成功识别，并模拟真实审计奖金分配。
    *   **Patch（修补）模式**：评估代理修复漏洞的能力。代理可直接修改代码，评分首先验证其修改未破坏原有功能（确保现有测试通过），然后使用未公开的漏洞利用测试来验证漏洞是否被真正修复。
    *   **Exploit（利用）模式**：这是最真实的模式。评估代理在本地实时以太坊实例上端到端利用漏洞的能力。代理会获得一个已注资的私钥和RPC端点，必须自主进行链上分析、部署辅助合约并构造交易。
3.  **程序化与链上评分系统**：这是关键创新点。评分在代理无法访问的独立容器中进行，确保公平性。特别是在Exploit模式中，开发了基于Rust的评估程序来管理区块链启动、合约部署，并通过自定义脚本分析区块链状态来客观判定利用是否成功，避免了主观判断。
4.  **可靠性与防作弊加固**：整个评估生命周期强调可靠性。包括对漏洞的可复现性进行过滤、多轮质量检查（手动审查、寻找作弊行为），并在Exploit模式中通过JSON-RPC网关和侧链容器等技术硬化执行环境，防止代理通过非常规RPC方法作弊。

总之，EVMbench通过构建一个贴近现实、覆盖安全生命周期关键环节、并采用自动化客观评分的多模式评估体系，系统地解决了对AI代理在智能合约安全领域能力进行量化评测的问题。

### Q4: 论文做了哪些实验？

论文实验围绕EVMbench基准展开，评估AI智能体在智能合约安全任务上的能力。实验设置包括三种任务模式：**Detect**（检测漏洞）、**Patch**（修补漏洞）和**Exploit**（利用漏洞）。评估在本地以太坊执行环境中进行，采用基于测试和区块链状态的程序化评分。数据集基于40个代码库中的117个精选漏洞，其中Patch和Exploit模式分别手动配置了部分漏洞进行评估。对比方法包括使用不同框架（如OpenCode基础框架与各厂商CLI代理）运行的多款前沿AI模型，包括GPT-5.3-Codex、Claude Opus 4.6、GPT-5.2、Gemini 3 Pro等。实验还测试了不同提示级别（低、中、高）对性能的影响。

主要结果显示：在**Exploit**任务中，GPT-5.3-Codex（通过Codex CLI运行）得分最高，达到71.0%；在**Patch**任务中，同一模型得分41.7%；在**Detect**任务中，Claude Opus 4.6（通过Claude Code运行）表现最佳，得分45.9%。关键数据指标包括：Claude Opus 4.6在Detect任务中获得最高平均奖金37,824.52美元（最高可达奖金为maxdetectaward）；当提供中等提示（机制提示）时，GPT-5.2在Patch和Exploit任务中得分分别提升至90.2%和78.3%，表明漏洞发现是主要难点。此外，实验分析了漏洞披露数量与检测成功率的关系，发现GPT-5.3-Codex和GPT-5.2报告的漏洞数量最接近真实情况。

### Q5: 有什么可以进一步探索的点？

该论文提出了一个评估AI代理在智能合约安全领域能力的基准，但其局限性和未来探索方向仍值得深入。首先，EVMbench的漏洞数据集虽经精选，但规模有限（117个漏洞），且可能无法覆盖新型或复合型漏洞，未来需持续扩展和更新数据集以反映快速演变的威胁态势。其次，评估主要关注检测、修补和利用漏洞的端到端能力，但未深入考察代理在复杂交互场景（如多合约调用、闪电贷攻击）中的鲁棒性和决策透明度，这限制了对其实际部署安全性的理解。

未来研究方向可包括：1）开发更具动态性和对抗性的评估环境，模拟真实区块链网络中的不确定性和恶意行为，以测试代理的适应能力；2）结合形式化验证或符号执行技术，增强代理对漏洞根本原因的理解，而非仅依赖模式匹配；3）探索多代理协作框架，让AI代理分工执行漏洞分析、补丁生成和攻击模拟，提升整体效率。此外，伦理风险（如代理被滥用为自动化攻击工具）也需纳入评估体系，推动安全与负责任的AI发展。

### Q6: 总结一下论文的主要内容

该论文提出了EVMbench，一个用于评估AI智能体在智能合约安全领域能力的基准测试框架。核心问题是衡量当前先进的AI智能体在检测、修补和利用智能合约漏洞方面的实际表现，这对于理解AI在提升安全性与潜在增加风险的双重角色至关重要。

方法上，EVMbench从40个代码库中精心挑选了117个漏洞案例，构建了评估任务。其关键创新在于采用了高度真实的评估设置：在本地以太坊执行环境中，基于测试用例和区块链状态的程序化评分来客观衡量智能体的表现，而非依赖主观判断。

主要结论是，评估一系列前沿AI智能体后发现，它们已经能够端到端地发现并利用真实区块链实例中的漏洞。这证明了AI在此领域已具备初步但切实的能力。论文的意义在于首次系统性地量化了AI智能体的智能合约安全能力，并开源了代码、任务和工具，为持续追踪此类能力演进及未来安全研究奠定了基础。
