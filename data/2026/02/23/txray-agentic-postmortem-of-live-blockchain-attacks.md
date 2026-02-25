---
title: "TxRay: Agentic Postmortem of Live Blockchain Attacks"
authors:
  - "Ziyue Wang"
  - "Jiangshan Yu"
  - "Kaihua Qin"
  - "Dawn Song"
  - "Arthur Gervais"
  - "Liyi Zhou"
date: "2026-02-01"
arxiv_id: "2602.01317"
arxiv_url: "https://arxiv.org/abs/2602.01317"
pdf_url: "https://arxiv.org/pdf/2602.01317v5"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent 架构"
  - "工具使用"
  - "Agent 评测/基准"
  - "Agent 安全"
  - "多智能体系统"
  - "LLM 应用于 Agent 场景"
relevance_score: 8.5
---

# TxRay: Agentic Postmortem of Live Blockchain Attacks

## 原始摘要

Decentralized Finance (DeFi) has turned blockchains into financial infrastructure, allowing anyone to trade, lend, and build protocols without intermediaries, but this openness exposes pools of value controlled by code. Within five years, the DeFi ecosystem has lost over 15.75B USD to reported exploits. Many exploits arise from permissionless opportunities that any participant can trigger using only public state and standard interfaces, which we call Anyone-Can-Take (ACT) opportunities. Despite on-chain transparency, postmortem analysis remains slow and manual: investigations start from limited evidence, sometimes only a single transaction hash, and must reconstruct the exploit lifecycle by recovering related transactions, contract code, and state dependencies.
  We present TxRay, a Large Language Model (LLM) agentic postmortem system that uses tool calls to reconstruct live ACT attacks from limited evidence. Starting from one or more seed transactions, TxRay recovers the exploit lifecycle, derives an evidence-backed root cause, and generates a runnable, self-contained Proof of Concept (PoC) that deterministically reproduces the incident. TxRay self-checks postmortems by encoding incident-specific semantic oracles as executable assertions.
  To evaluate PoC correctness and quality, we develop PoCEvaluator, an independent agentic execution-and-review evaluator. On 114 incidents from DeFiHackLabs, TxRay produces an expert-aligned root cause and an executable PoC for 105 incidents, achieving 92.11% end-to-end reproduction. Under PoCEvaluator, 98.1% of TxRay PoCs avoid hard-coding attacker addresses, a +22.9pp lift over DeFiHackLabs. In a live deployment, TxRay delivers validated root causes in 40 minutes and PoCs in 59 minutes at median latency. TxRay's oracle-validated PoCs enable attack imitation, improving coverage by 15.6% and 65.5% over STING and APE.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决去中心化金融（DeFi）生态系统中，针对链上攻击事件进行事后分析（Postmortem）时存在的严重滞后性和缺乏标准化、可复现数据集两大核心问题。

研究背景是，DeFi 的无需许可特性使其成为价值“洼地”，但也暴露了“任何人皆可获取”（ACT）的攻击机会，导致巨额资金损失。尽管区块链交易公开透明，理论上任何攻击都可被追溯和复现，但现有的分析方法存在明显不足。首先，**事后分析严重依赖人工、缓慢且易错**：调查往往从有限的证据（如单个交易哈希）开始，需要专家手动重建攻击生命周期、合约代码和状态依赖，导致根因分析严重滞后（如论文中Balancer案例延迟近3小时），且在初期可能给出错误结论，误导社区并延误防御。其次，**缺乏高质量、标准化的可复现攻击数据集**：现有的公共事件追踪平台（如DeFiHackLabs）记录质量参差不齐，多为手动整理，其概念验证（PoC）代码的完整性、可执行性和标准化程度不一，无法系统性地用于评估检测工具、训练AI代理或进行一致的根因研究。

因此，本文的核心问题是：**如何自动化、快速且可靠地将单个链上攻击事件（通常仅从少量种子交易出发）转化为结构化的、可执行的分析成果，以克服事后分析滞后并构建标准化的可复用漏洞数据集**。为此，论文提出了TxRay系统，这是一个基于大语言模型（LLM）的智能体（Agent）事后分析系统，能够自动重建攻击生命周期、推断证据支持的根因，并生成可独立运行、参数无关的PoC测试代码，从而实现对攻击的确定性复现。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：区块链安全分析、自动化攻击检测与响应，以及基于LLM的智能体系统。

在**区块链安全分析与事后分析（Postmortem）**方面，已有大量研究关注DeFi攻击的分类、检测和调查。例如，许多工作系统性地研究了DeFi攻击向量和MEV（最大可提取价值）行为。当前的行业实践通常依赖于入侵检测系统（如BlockSec Phalcon、Hypernative等实时监控平台）进行初步警报，但后续的根因分析和概念验证（PoC）生成仍高度依赖人工，过程缓慢且易出错。本文的TxRay系统则旨在自动化这一“事后重建”阶段，从有限的交易哈希开始，自动重构攻击生命周期并生成可执行的PoC，这与传统手动分析形成鲜明对比。

在**自动化攻击检测与响应（模仿/反制）**方面，已有系统如APE和STING专注于在交易待处理时（MEV时间）进行攻击模仿或反制。APE依赖程序执行轨迹和污点分析，而STING结合了启发式方法（如资金来源、合约验证状态）来识别敌对合约。TxRay虽然主要目标是在攻击发生后进行事后分析，但其生成的、经过预言机验证的PoC可直接用于此类广义攻击模仿，实验表明其在覆盖范围上超越了STING和APE。

在**基于LLM的智能体与评估系统**方面，随着大语言模型的发展，出现了将其用于区块链异常检测等任务的研究。TxRay的核心创新在于构建了一个LLM驱动的智能体系统，通过工具调用来自主进行链上数据检索、推理和PoC生成。此外，本文还提出了独立的智能体评估系统PoCEvaluator，用于自动评估PoC的正确性和质量，这为自动化安全分析的质量保障提供了新思路。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为TxRay的LLM智能体系统来解决区块链攻击事后分析效率低下的问题。该系统采用多智能体协作框架，将攻击重现过程自动化，从有限的种子交易出发，最终生成可验证的根因分析和可独立运行的漏洞复现（PoC）。

**整体框架与核心方法**：
TxRay的核心是一个由**中央协调器（Orchestrator）** 管理的多智能体工作流。协调器控制整个分析流程，并在一个**共享工作空间（Workspace）** 中协调六个专业子智能体的执行。工作流分为两大阶段：根因分析和PoC生成与验证，两者均在迭代预算和验证反馈机制下运行。

**主要模块与组件**：
1.  **根因分析阶段（组件1-3）**：
    *   **链上数据收集器**：根据种子交易，通过查询区块浏览器API、RPC端点（如获取交易收据、执行追踪）等工具，收集交易元数据、执行轨迹和状态差异等证据。若合约未验证，则回退到字节码层面的分析。
    *   **根因分析器**：将收集的证据合成为根因报告草案。它会将种子交易扩展为覆盖攻击全生命周期（如资金准备、攻击合约部署、漏洞利用、利润提取）的交易集，并确保每个论断都有链上证据（如追踪、状态差异）支持。
    *   **根因挑战器**：对报告草案进行验证，检查其是否遗漏生命周期步骤、与证据矛盾或包含未确定的论断。若拒绝，则提供结构化反馈，促使协调器触发重新分析或数据收集。

2.  **PoC生成与验证阶段（组件4-6）**：
    *   **PoC预言机生成器**：将已验证的根因转化为**语义预言机**定义。该定义包含实体变量、预检查以及硬/软约束（如权限变更、关键状态不变性、攻击者利润阈值等），用于编码攻击机制的核心语义，而非具体执行细节。
    *   **PoC重现器**：创建一个自包含的Foundry测试项目。它在事件发生时的链状态分叉上，使用全新的攻击者地址重新创建资金、部署和攻击生命周期，并将语义预言机编码为测试断言，**避免硬编码原始攻击者的地址或调用数据**。
    *   **PoC验证器**：运行Foundry测试，检查预言机约束是否满足，并评估PoC代码质量（如可读性、自包含性）。失败则反馈原因，触发重现器修改。

**关键技术及创新点**：
*   **证据优先与迭代验证**：系统严格坚持所有分析基于链上证据，并通过挑战器进行多轮验证，确保结论的可靠性。
*   **语义预言机**：这是关键创新。它将攻击机制抽象为可执行的断言（硬约束和带容忍度的软约束），使PoC能够验证攻击的**语义正确性**，而不仅仅是比特级重放，从而生成通用、高质量的复现。
*   **自包含与去身份化的PoC生成**：PoC重现器能独立复现攻击条件，且不依赖原始攻击者的任何身份信息（地址、合约），提升了PoC的通用性和教育价值。
*   **多智能体协同架构**：通过中央协调器与专业子智能体的分工协作，将复杂的分析任务模块化，实现了从数据收集到报告生成的全流程自动化。

总之，TxRay通过一个集成了证据收集、分析、挑战和自动化代码生成的多智能体系统，将原本耗时、手动的攻击事后分析，转变为高效、可验证且能产出高质量复现用例的自动化过程。

### Q4: 论文做了哪些实验？

论文实验主要围绕评估TxRay系统在区块链攻击事后分析中的性能。实验设置上，研究者使用DeFiHackLabs数据集中的114个真实安全事件作为基准，以社区现有的DeFiHackLabs分析报告作为主要对比基线。实验通过四个研究问题展开评估：RQ1（保真度）考察系统从种子交易中识别“任何人可获取”（ACT）机会并生成与专家判断一致的根因报告的能力；RQ2（可复现性）评估系统为已对齐案例生成可执行、自包含且满足预言机验证的PoC（概念证明）的比例。

关键数据指标显示，TxRay在114个事件中，对105个事件生成了专家一致的根因报告和可执行PoC，端到端复现率达到92.11%。通过独立的PoCEvaluator评估器进行质量检验，TxRay生成的PoC中有98.1%避免了硬编码攻击者地址，相比DeFiHackLabs基线提升了22.9个百分点。在实时部署测试中，TxRay生成已验证根因报告的中位延迟为40分钟，生成PoC的中位延迟为59分钟。此外，TxRay通过预言机验证的PoC支持攻击模拟，在覆盖范围上相比STING和APE工具分别提升了15.6%和65.5%。

### Q5: 有什么可以进一步探索的点？

本文提出的TxRay系统在自动化分析区块链攻击方面取得了显著进展，但其局限性和未来探索方向仍值得深入。首先，系统高度依赖历史攻击数据进行训练和评估，对于新型或复杂组合攻击的泛化能力有待验证。其次，当前分析主要基于公开链上数据，难以涵盖涉及链下预言机操纵、治理攻击或社交工程等混合型漏洞。此外，系统生成的PoC虽然可执行，但可能无法完全模拟攻击发生时的网络状态或MEV竞争环境。

未来研究方向可包括：1）引入多模态学习，结合代码审计报告、社区讨论等文本信息，提升根因分析的深度；2）开发实时监测模块，在攻击发生初期进行干预预警，而不仅限于事后分析；3）探索对抗性测试框架，通过模拟攻击变种来评估系统的鲁棒性。从实践角度，可考虑将系统与智能合约形式化验证工具结合，实现“漏洞检测-攻击模拟-修复验证”的闭环。这些改进有望使自动化安全分析从事后追溯转向主动防御，真正降低DeFi生态的系统性风险。

### Q6: 总结一下论文的主要内容

该论文提出了TxRay系统，旨在利用大语言模型（LLM）驱动的智能体，自动化地对区块链上的“任何人皆可获取”（ACT）攻击进行事后分析。核心问题是现有的事后分析依赖人工，从有限的初始证据（如单个交易哈希）出发，重构攻击生命周期、定位根本原因并生成可复现的概念验证（PoC）的过程缓慢且费力。

TxRay的方法是从一个或多个种子交易开始，通过调用工具自动追溯相关交易、合约代码和状态依赖，从而重建完整的攻击生命周期。系统不仅推断出有证据支持的根本原因，还能生成一个独立、可运行的PoC来确定性复现攻击。其关键创新在于引入了特定于事件的语义预言机作为可执行断言，用于自我验证事后分析的正确性。

论文的主要贡献和意义在于：1）实现了攻击分析的自动化与加速，在真实部署中，中位延迟下可在40分钟内提供已验证的根本原因，59分钟内生成PoC；2）通过独立的PoCEvaluator评估器验证，在114个历史事件中，TxRay实现了92.11%的端到端复现成功率，且98.1%的PoC避免了硬编码攻击者地址，质量显著优于现有基准；3）其生成的经过预言机验证的PoC可用于攻击模拟，相比STING和APE等工具，分别将覆盖率提升了15.6%和65.5%，为区块链安全防御提供了强大工具。
