---
title: "Before the Tool Call: Deterministic Pre-Action Authorization for Autonomous AI Agents"
authors:
  - "Uchi Uchibeke"
date: "2026-03-21"
arxiv_id: "2603.20953"
arxiv_url: "https://arxiv.org/abs/2603.20953"
pdf_url: "https://arxiv.org/pdf/2603.20953v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Safety"
  - "Tool Use"
  - "Authorization"
  - "Security"
  - "Policy Enforcement"
  - "Audit"
  - "Open Source"
relevance_score: 7.5
---

# Before the Tool Call: Deterministic Pre-Action Authorization for Autonomous AI Agents

## 原始摘要

AI agents today have passwords but no permission slips. They execute tool calls (fund transfers, database queries, shell commands, sub-agent delegation) with no standard mechanism to enforce authorization before the action executes. Current safety architectures rely on model alignment (probabilistic, training-time) and post-hoc evaluation (retrospective, batch). Neither provides deterministic, policy-based enforcement at the individual tool call level.
  We characterize this gap as the pre-action authorization problem and present the Open Agent Passport (OAP), an open specification and reference implementation that intercepts tool calls synchronously before execution, evaluates them against a declarative policy, and produces a cryptographically signed audit record. OAP enforces authorization decisions in a measured median of 53 ms (N=1,000). In a live adversarial testbed (4,437 authorization decisions across 1,151 sessions, $5,000 bounty), social engineering succeeded against the model 74.6% of the time under a permissive policy; under a restrictive OAP policy, a comparable population of attackers achieved a 0% success rate across 879 attempts.
  We distinguish pre-action authorization from sandboxed execution (contains blast radius but does not prevent unauthorized actions) and model-based screening (probabilistic), and show they are complementary. The same infrastructure that enforces security constraints (spending limits, capability scoping) also enforces quality gates, operational contracts, and compliance controls. The specification is released under Apache 2.0 (DOI: 10.5281/zenodo.18901596).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自主AI代理在执行工具调用（如资金转账、数据库查询、系统命令执行或子代理委派）时，缺乏一个标准化的、确定性的预执行授权机制这一核心安全问题。研究背景是，随着AI代理在生产环境中大规模部署，它们能够通过工具调用执行具有实际影响的操作，但当前的安全架构存在显著缺陷。现有方法主要依赖于两种途径：一是模型对齐（Model Alignment），即在训练阶段通过概率性方式引导模型行为，但这无法在运行时对每个具体操作提供确定性的安全保证；二是事后评估（Post-hoc Evaluation），即批量回溯检查，这无法在动作执行前进行实时拦截。此外，尽管沙箱执行（Sandboxed Execution）可以限制操作的影响范围，但它本身并不能阻止未授权操作的发起。这些方法的共同不足在于，它们都无法在单个工具调用级别，提供一个基于声明式策略的、同步的、确定性的授权执行层，也无法生成可验证的审计记录，导致存在结构性安全漏洞。本文的核心问题正是填补这一“预执行授权”的空白，确保在AI代理的每一个工具调用实际执行之前，都能根据明确的策略进行强制性的授权检查，从而将安全控制从依赖模型概率性输出的“软”约束，转变为系统级的“硬”保障。

### Q2: 有哪些相关研究？

本文的相关研究可大致分为以下几类：

**1. 训练时对齐与事后评估**：包括RLHF、RLAIF等训练时对齐技术，以及Promptfoo、Galileo等自动化评估工具。这些方法通过塑造模型行为分布或批量评估运行结果来提升安全性，但本质上是概率性的或回顾性的，无法在单个工具调用执行前进行确定性的、基于策略的拦截。本文的OAP机制正是为了填补这一实时执行前授权的空白。

**2. 沙箱化执行**：如NVIDIA NemoClaw、ceLLMate、E2B、Google Agent Sandbox等系统。它们通过在操作系统内核、网络层或容器层面隔离代理执行环境来限制行动的影响范围（遏制爆炸半径）。然而，沙箱主要侧重于“ containment”（遏制），而非“prevention”（阻止），它无法阻止沙箱允许范围内的未授权语义操作（如超额的转账），也不提供每项操作的授权审计追踪。OAP与沙箱是互补关系，OAP负责执行前授权决策，沙箱负责限制已授权行动的执行环境。

**3. 运行时策略执行**：这是与OAP最直接相关的一类工作。
    *   **PCAS**：通过基于Datalog的参考监视器实现确定性策略执行，在提升策略合规性方面与OAP目标一致。主要区别在于策略语言（PCAS用Datalog衍生语言，OAP用声明式JSON/YAML）、部署模型（编译器集成 vs. 框架钩子+云API）和凭证范围（每代理编译 vs. 便携式护照凭证）。
    *   **AgentGuardian**：从执行轨迹中学习上下文感知的访问控制策略，具有适应性优势，但牺牲了确定性保证。
    *   **Safiron**：使用经过训练的守护模型在执行前筛查代理计划，处于正确的干预点，但其模型基分类器本质上是概率性的，可能受到对抗性输入的影响。
    *   **Google ADK Safety / Microsoft Defender for AI Agents**：提供了执行前回调钩子或结合了评估与沙箱，但其中基于模型的筛查层同样存在非确定性问题。

**4. 身份与安全标准框架**：如OAuth 2.0、SPIFFE等解决了代理身份问题，但未定义每调用动作的授权。OWASP Top 10、NIST AI Agent Standards Initiative、Linux基金会AAIF等列出了风险或提出了标准框架。特别是Agent2Agent（A2A）协议要求执行敏感操作前必须授权，但未指定机制；其现有的安全护照扩展用于上下文共享，与OAP的每动作策略强制执行结构不同。OAP已被提议作为A2A的扩展来弥补这一机制缺失。

**5. 正交的验证技术**：如Proof-of-Guardrail利用可信执行环境提供授权决策执行的密码学证明，可与OAP这样的预授权系统结合，实现决策审计轨迹的独立验证。

总之，本文的OAP与训练对齐、事后评估、沙箱隔离、概率性筛查模型形成对比或互补，并与PCAS等确定性运行时策略执行系统在目标上最接近，但在实现路径、策略语言和凭证设计上存在区别。

### Q3: 论文如何解决这个问题？

论文通过提出并实现“开放智能体护照”（Open Agent Passport, OAP）这一规范来解决预动作授权问题。其核心方法是**在工具调用执行前，同步地、确定性地拦截每一次调用，并依据声明式策略进行评估**，从而在行动层面实现强制授权，而非依赖训练时的概率性模型对齐或事后的批量评估。

**整体框架与架构设计**：
OAP系统包含三个核心组件，构成了一个清晰的授权流水线：
1.  **智能体护照**：一个经过加密签名（使用Ed25519算法）的数字凭证，绑定了智能体的身份及其被授权的**能力范围**和**操作限制**（如单次交易上限、允许的域名等）。护照由注册表服务颁发和验证。
2.  **策略包**：针对特定能力域（如金融支付、数据操作）的**声明式、版本化的约束规则集合**。每个包通过JSON Schema定义必需的上下文字段，并将评估规则定义为“条件-拒绝代码”对。规则被限制在可判定的片段内（如有限数值域的比较、有限字符串集的成员检查），确保评估始终在常数时间内终止。
3.  **`before_tool_call` 钩子**：这是**关键的强制执行点**，作为一个阻塞式钩子集成在智能体框架层（而非模型推理层）。在每次工具调用执行前，该钩子被同步触发并等待授权决策返回，工具调用在此之后才能进行。这种设计确保了**不可绕过性**：即使通过提示注入说服模型请求调用，也无法跳过策略检查。

**主要工作流程（算法）**：
当工具调用被拦截后，OAP授权算法按顺序执行：1) 验证护照状态（活跃/暂停/吊销）；2) 检查调用能力是否在护照授权范围内；3) 查找对应的策略包；4) 验证智能体保证级别是否满足策略要求；5) 按顺序评估策略包中的所有规则，检查调用参数是否违反任何约束（如金额超限）；6) 根据评估结果生成 **ALLOW（允许）、DENY（拒绝）或 ESCALATE（升级审批）** 的决策；7) 为每次决策生成带有时间戳和Ed25519签名的审计记录。整个过程是确定性的，相同输入必得相同决策。

**关键技术特性与创新点**：
*   **确定性执行与不可绕过性**：与依赖模型采样、具有随机性的“对齐”方案不同，OAP在框架层进行基于规则的确定性评估，从根本上杜绝了通过提示注入绕过授权的可能。
*   **故障安全（Fail-Closed）**：如果授权服务、护照或策略包不可用，默认决策为拒绝，防止在不确定情况下执行未授权操作。
*   **框架无关与可审计性**：OAP核心是一个开放规范，通过适配器集成到多种主流智能体框架（如LangChain、CrewAI）。每一次授权决策都产生密码学签名的审计日志，满足合规与追溯需求。
*   **保证级别分层**：OAP定义了从L0（自我声明）到L4（严格KYC/金融验证）的六级保证级别，将授权执行的强度与身份验证的严格程度相绑定，实现风险适配的访问控制。
*   **互补性定位**：OAP明确区分了预动作授权与沙箱执行（控制影响范围但不阻止动作）、模型筛查（概率性）等方案，并强调其互补关系。OAP专注于在动作执行前依据策略进行“是否允许”的二元裁决，而其他技术可用于执行过程中的隔离或事后分析。

综上，OAP通过将传统的、基于策略的访问控制模型引入自主智能体领域，在工具调用执行的关键路径上插入了一个确定性的、可审计的授权层，从而系统性地解决了当前智能体缺乏标准化的预动作授权机制这一核心安全问题。

### Q4: 论文做了哪些实验？

论文通过一个实时的对抗性测试平台（APort Vault）和性能基准测试来评估其提出的Open Agent Passport（OAP）系统。实验设置包括：1）一个模拟银行场景的对抗测试平台（CTF），参与者试图通过社会工程学操纵AI代理进行未经授权的转账；2）性能基准测试，测量OAP授权决策的延迟。

**数据集/基准测试**：主要使用自建的“APort Vault”对抗测试平台作为实验环境。该平台记录了1,151次会话，共产生4,437次授权决策。性能测试则在生产负载下进行（N=1,000次请求）。

**对比方法**：实验核心对比了两种策略下的防护效果：
*   **宽松策略（Tier 1）**：作为基线，仅依赖模型对齐进行过滤。
*   **严格策略（Tier 5）**：启用OAP的严格策略（零能力、零转账限额）。

**主要结果与关键指标**：
1.  **安全有效性**：在宽松策略（T1）下，社会工程攻击成功率达**74.6%**（588次尝试中成功439次）。在启用OAP严格策略（T5）后，攻击成功率降至**0%**（879次尝试中成功0次），OAP拦截率达100%。这证明了OAP在工具调用前进行确定性授权能有效防止模型被诱导后执行越权操作。
2.  **性能开销**：OAP授权决策的延迟中位数（p50）为**53毫秒**，第99百分位数（p99）低于**77毫秒**。本地评估延迟中位数为174毫秒。论文认为此开销对于通常耗时数百毫秒至数秒的工具调用是可接受的。
3.  **决策分析**：在所有4,437次决策中，OAP拒绝了2,419次（**54.5%**）。主要的拒绝原因包括：未知能力（oap.unknown_capability，1,453次）、禁止的商户（oap.merchant_forbidden，412次）和评估错误（oap.evaluation_error，173次）。
4.  **覆盖范围**：OAP为OWASP Agentic Top 10风险中的8项提供了完全或部分覆盖。

### Q5: 有什么可以进一步探索的点？

基于论文讨论部分，可以进一步探索的点包括：首先，在**多智能体委托链**方面，当前OAP v1.0缺乏对子代理权限传递的正式规范，未来需设计安全的委托机制，确保权限在链式调用中不被越界。其次，**策略表达能力**受限，现有JSON/YAML格式难以支持复杂条件逻辑，可扩展为类似Datalog的声明式语言或引入策略组合模块。第三，**自适应策略**尚未实现，静态策略难以应对新型攻击，可结合执行轨迹学习（如AgentGuardian）实现动态异常检测。第四，**组合攻击防御**需加强，例如通过滑动窗口策略跟踪聚合状态，防止多次小额操作绕过限制。此外，**性能扩展性**需验证，当前基准测试规模较小，未来应评估高并发场景（如每秒万次决策）下的延迟与吞吐量。最后，**信任根强化**可探索与可信执行环境（TEE）集成，减少对运行时安全的假设，防止钩子绕过。这些方向不仅提升安全性，还能将授权框架扩展至质量门控、合规审查等更广泛的智能体治理场景。

### Q6: 总结一下论文的主要内容

该论文针对当前AI智能体在执行工具调用（如资金转账、数据库查询等）时缺乏标准化、确定性授权机制的安全问题，提出了“行动前授权”这一核心概念。现有安全架构主要依赖模型对齐（概率性、训练时）和事后评估（回顾性、批量），无法在单个工具调用级别实现基于策略的确定性授权。

为解决此问题，论文提出了开放智能体通行证（OAP）规范及参考实现。OAP的核心方法是在工具调用同步执行前进行拦截，依据声明式策略进行评估，并生成加密签名的审计记录。该方法实现了确定性的策略执行，中位授权决策时间仅为53毫秒。在对抗性测试中，宽松策略下模型被社会工程攻击的成功率达74.6%，而采用严格的OAP策略后，攻击者在879次尝试中的成功率降至0%。

论文的主要结论是，OAP填补了关键的安全空白，将授权从概率性的模型内部决策转变为确定性的外部策略执行。它与沙箱执行（限制影响范围但不阻止未授权行动）和基于模型的筛查（概率性）互为补充。OAP基础设施不仅能强制执行安全约束（如支出限额、能力范围），还能用于质量门控、运营合约和合规控制，为构建安全、可靠、可审计的自主智能体系统提供了基础。
