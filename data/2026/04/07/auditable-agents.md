---
title: "Auditable Agents"
authors:
  - "Yi Nian"
  - "Aojie Yuan"
  - "Haiyue Zhang"
  - "Jiate Li"
  - "Yue Zhao"
date: "2026-04-07"
arxiv_id: "2604.05485"
arxiv_url: "https://arxiv.org/abs/2604.05485"
pdf_url: "https://arxiv.org/pdf/2604.05485v1"
categories:
  - "cs.AI"
tags:
  - "Agent Security"
  - "Agent Accountability"
  - "Agent Auditing"
  - "Agent System Design"
  - "Agent Safety"
  - "Agent Governance"
  - "Agent Monitoring"
  - "Agent Logging"
relevance_score: 8.5
---

# Auditable Agents

## 原始摘要

LLM agents call tools, query databases, delegate tasks, and trigger external side effects. Once an agent system can act in the world, the question is no longer only whether harmful actions can be prevented--it is whether those actions remain answerable after deployment. We distinguish accountability (the ability to determine compliance and assign responsibility), auditability (the system property that makes accountability possible), and auditing (the process of reconstructing behavior from trustworthy evidence). Our claim is direct: no agent system can be accountable without auditability.
  To make this operational, we define five dimensions of agent auditability, i.e., action recoverability, lifecycle coverage, policy checkability, responsibility attribution, and evidence integrity, and identify three mechanism classes (detect, enforce, recover) whose temporal information-and-intervention constraints explain why, in practice, no single approach suffices. We support the position with layered evidence rather than a single benchmark: lower-bound ecosystem measurements suggest that even basic security prerequisites for auditability are widely unmet (617 security findings across six prominent open-source projects); runtime feasibility results show that pre-execution mediation with tamper-evident records adds only 8.3 ms median overhead; and controlled recovery experiments show that responsibility-relevant information can be partially recovered even when conventional logs are missing. We propose an Auditability Card for agent systems and identify six open research problems organized by mechanism class.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决LLM智能体系统在部署后因执行外部操作（如调用工具、触发副作用）而引发的责任追溯难题。研究背景是，随着智能体从单纯文本生成转向具备实际行为能力（如发送邮件、支付），其潜在风险已从内容安全问题升级为系统安全问题。现有方法主要关注对齐、对抗性评估和运行时防御，虽能降低有害行为概率，但无法确保事后对系统行为进行有效追溯、策略核查和责任认定。现有系统的日志记录往往不完整、缺乏关键操作路径（如错误处理、任务移交），且证据易被篡改，导致部署后出现问题时难以可靠回答“发生了什么、是否合规、谁应负责”这三个核心问题。

本文的核心主张是：智能体系统必须具备可审计性，这是实现问责制的前提。为此，论文系统性地定义了可审计性的五个维度（行动可恢复性、生命周期覆盖性、策略可检查性、责任可归因性、证据完整性），并指出仅靠单一技术机制（如检测、执行或恢复）无法同时满足所有维度。论文通过生态系统测量、运行时性能实验和恢复实验等多层次证据，论证了可审计性作为系统设计首要目标的必要性与可行性，最终提出“可审计性卡片”框架和开放研究问题，推动该领域建立系统的审计保障机制。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、评测类与安全类三大方向。在方法类研究中，现有工作集中于通过**检测（detect）**、**执行（enforce）** 和**恢复（recover）** 等机制来增强AI系统的安全性与可控性，例如使用护栏（guardrails）或运行时监控。本文与这些工作的核心区别在于，它首次系统性地提出了**可审计性（auditability）** 作为实现**问责制（accountability）** 的先决系统属性，并构建了包含五个维度的理论框架，而不仅仅是预防或检测单个有害行为。

在评测类研究中，已有基准测试多关注代理的任务完成能力或安全性。本文则通过实证测量（如对六个开源项目的安全漏洞分析）和可控实验（如信息恢复实验），提供了多层次证据，论证了当前生态在可审计性基础条件上的普遍缺失，这超越了传统性能评测的范畴。

在安全与应用类研究中，相关工作涉及安全日志、溯源和归因技术。本文的创新点在于明确了**证据完整性**和**责任归因**是可审计性的关键维度，并提出了结合防篡改记录与执行前仲裁的可行机制，其运行时开销较低（中位数仅8.3毫秒），展示了其实用化潜力。

### Q3: 论文如何解决这个问题？

论文通过提出一个五维度的审计性框架和三类互补的机制来解决智能体系统的可审计性问题，旨在使部署后的问责成为可能。

**核心方法与架构设计：**
论文的核心是构建了一个系统性的框架，而非单一技术。该框架包含两个关键部分：1) **五个审计性维度**，定义了可辩护审计所必需的证据条件；2) **三类时序机制**，解释了为何需要组合不同时间点的干预来满足所有维度。

**主要模块/组件与创新点：**
1.  **五维度审计性框架**：这是核心的概念贡献。框架定义了构成一个完整审计结论所必需的五个独立且相互依赖的维度：
    *   **行动可恢复性**：系统是否记录了与策略相关的行动（如工具调用）及其关键字段，以便事后重建“发生了什么”。
    *   **生命周期覆盖度**：记录是否涵盖了完整的执行上下文和阶段（如重试、审批、委派），而不仅仅是孤立的行动。
    *   **策略可检查性**：记录是否包含足够信息，能对行动是否符合既定策略做出机械化的判定（合规、违规或无法判定）。
    *   **责任归属**：能否追溯导致某个结果的责任链或交互子图，而不仅仅是识别直接执行者。
    *   **证据完整性**：审计记录本身是否具备防篡改保护（如仅追加、哈希链、数字签名）。

    这五个维度缺一不可，共同构成了“可审计性”的正式定义。其创新在于将抽象的问责需求分解为具体、可测量的系统属性。

2.  **三类时序机制**：论文指出，没有任何单一的时间点能提供满足所有五个维度的信息和干预能力。因此，必须结合三类机制：
    *   **检测**：在部署前，通过静态分析代码、配置和供应链工件，识别潜在的审计性缺陷（如缺少日志钩子）。它提供风险信号，但无法保证运行时行为。
    *   **执行**：在运行时，对产生副作用的行动进行实时拦截、策略评估，并生成受完整性保护的结构化记录。这是生成高质量审计证据的关键环节，直接支持前四个维度。
    *   **恢复**：在事后，从可能不完整、分散或已剥离元数据的幸存记录中，重建行为并分配责任。这是在现实多系统部署中最终确立问责的必要步骤。

**整体解决思路：**
论文的解决方案是体系化的。它首先通过五维度框架明确了“可审计系统”应达到的标准。然后，通过三类机制模型解释了在实践中必须采取的组合策略：**部署前检测以预防缺陷，运行时执行以生成可信证据，事后恢复以应对不完整数据**。这种分层、分时的设计承认了现实约束——证据的生成、保护和利用发生在系统生命周期的不同阶段，需要不同的技术来保障。论文通过生态系统测量、运行时开销实验和缺失日志恢复实验，分别验证了三类机制的可行性和现状，从而支持了这一组合方法的必要性。最终，可审计性（及由此衍生的问责）是这些维度和机制共同作用的结果。

### Q4: 论文做了哪些实验？

论文通过三个相互支撑的证据模块进行实验，以验证其关于智能体可审计性的观点。

**实验设置与数据集/基准测试**：
1.  **生态系统下限分析**：使用静态安全分析工具 `agent-audit`（包含53条检测规则）扫描了六个主流的开源智能体项目（OpenHands, Generative Agents, SWE-agent, Gorilla, MLAgentBench, CodeAct），作为当前智能体开发生态的样本。
2.  **运行时可行性验证**：基于名为Aegis的预执行防火墙进行测试。它拦截并评估智能体的工具调用。攻击测试集包含`\AttackCases`个精心策划的攻击实例（覆盖7个OWASP类别），良性测试集包含`\BenignCalls`个良性工具调用。
3.  **恢复边界探索**：采用隐式执行追踪（IET）方法，该方法通过密钥水印在生成过程中嵌入信号。实验在多样化的多智能体拓扑结构（链式、星型、树形，包含4-6个智能体）上进行，并模拟了身份信息移除、边界扰乱和内容脱敏三种日志退化条件。

**对比方法**：
在恢复实验中，IET方法与最佳基线方法进行了对比。生态系统扫描部分提到，通用静态分析工具（如Bandit, Semgrep）在特定漏洞上的召回率为0%，而`agent-audit`在精选的智能体漏洞基准测试上实现了3-4倍的更高召回率。

**主要结果与关键指标**：
1.  **生态系统安全现状**：在六个项目中总计发现 **617个** 安全漏洞，其中64%（397个）属于“工具滥用”类别。这揭示了当前生态在满足可审计性基本安全前提方面存在广泛差距。
2.  **运行时性能与效果**：Aegis成功拦截了所有`\AttackCases`个攻击案例，在良性调用上的误报率为 **0.6%**。其引入的运行时开销中位数仅为 **8.3毫秒**（P95: 14.7ms），相对于LLM推理延迟可忽略不计，证明了预执行控制点的工程可行性。
3.  **日志缺失下的恢复能力**：在传统日志缺失的情况下，IET方法仍能部分恢复责任相关信息：其恢复的行动片段与真实片段的重叠度（IoU）约为 **0.93**，令牌归属准确率接近 **0.95**，交互图拓扑恢复准确率（EdgeSim）接近 **0.96**。在身份信息完全移除的极端情况下，IET仍能保持23.8%的智能体级别归属准确率，而基线方法则近乎失效。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来可进一步探索的点主要集中在如何整合与强化三类机制以构建更完备的可审计性体系。论文明确指出，检测、执行和恢复三类机制各有其信息与干预的时空局限性，无法单独满足所有五个可审计性维度。因此，一个核心研究方向是设计跨生命周期的协同框架，使三类机制的证据能无缝衔接与互证，尤其是在复杂、多参与方的实际部署环境中。

具体改进思路包括：第一，研究如何将静态检测（如代码分析）发现的潜在风险点，动态转化为运行时执行策略的配置，实现风险预警到实时干预的闭环。第二，针对证据完整性，需探索更健壮的分布式审计追踪技术，确保行动记录在跨系统流转（如输出被复制到外部工单系统）时，关键元数据（如责任链）能得以保留或可验证恢复。第三，论文提到责任归属在运行时机制中仅能部分捕获，未来可研究如何通过更精细的意图追踪与委托链记录，在事后恢复中更准确地重构责任图谱。此外，可审计性卡片（Auditability Card）的标准化与自动化评估工具也是值得推进的方向，以帮助开发者系统地识别和弥补审计缺口。

### Q6: 总结一下论文的主要内容

本文《可审计智能体》针对LLM智能体在部署后可能产生外部副作用的问题，提出了可审计性应成为智能体系统的一级设计和评估要求。核心问题是：一旦智能体系统在现实世界中行动，如何确保其行为在事后可被追溯、核查并归责？

论文的核心贡献是定义了一个包含五个维度的智能体可审计性框架，这五个必要条件是：**行动可恢复性**（记录关键操作）、**生命周期覆盖**（记录完整执行上下文）、**策略可核查性**（支持基于记录的机械式合规判定）、**责任归属**（追溯责任链）以及**证据完整性**（防止记录被篡改）。论文指出，这五个维度缺一不可，共同构成事后问责的基础。

为实现这些维度，论文提出了三类在系统生命周期中互补的机制：**检测**（部署前静态分析）、**执行**（运行时拦截与策略执行并生成受保护记录）和**恢复**（事后从不完整证据中重建行为）。通过分层证据（对开源项目的安全扫描、运行时可行性实验、日志缺失下的恢复实验）证明，当前生态普遍缺乏可审计性的基本安全前提，但运行时执行机制的开销可控（中位数仅8.3毫秒），且即使在常规日志缺失的情况下，部分行为和责任信息仍可被恢复。

主要结论是：没有单一机制能完全满足所有审计维度，可审计性必须通过三类机制的协同来实现。论文最后提出了“可审计性卡片”作为系统评估工具，并指出了六个按机制分类的开放研究问题。
