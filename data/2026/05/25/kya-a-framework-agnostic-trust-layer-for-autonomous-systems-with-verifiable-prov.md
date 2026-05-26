---
title: "KYA: A Framework-Agnostic Trust Layer for Autonomous Systems with Verifiable Provenance and Hierarchical Policy Composition"
authors:
  - "Kolawole Quadri"
date: "2026-05-25"
arxiv_id: "2605.25376"
arxiv_url: "https://arxiv.org/abs/2605.25376"
pdf_url: "https://arxiv.org/pdf/2605.25376v1"
github_url: "https://github.com/veldtlabs/veldt-kya"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.CY"
  - "cs.MA"
  - "cs.SE"
tags:
  - "Agent安全"
  - "Agent治理"
  - "Agent信任层"
  - "多智能体系统"
  - "策略组合"
  - "可审计性"
  - "开源框架"
  - "实验验证"
relevance_score: 8.5
---

# KYA: A Framework-Agnostic Trust Layer for Autonomous Systems with Verifiable Provenance and Hierarchical Policy Composition

## 原始摘要

Observability tells operators when an agent is slow. KYA tells operators when an agent is wrong, drifting, leaking, or quietly going rogue. We present KYA (Know Your Agents), an open-source trust and governance layer for autonomous systems composed of five primitives: (1) a four-gate inbound apply pipeline composing Ed25519 signature verification with multi-anchor pinning, persist-time expiry, only-tighten composition, and operator-approval-as-default; (2) an only-tighten composition algebra over a three-channel multi-tenant hierarchy (platform default,tenant override, signed external recommendation); (3) KYP -- Know Your Principal, a schema-level unification of trust scoring across human users, AI agents, and service accounts; (4) auditable interaction-multiplier amplification over an AIVSS-shaped additive baseline, with bounded asymmetric per-interaction multipliers carrying stable audit codes; and (5) two-axis delegation attribution combining a static observation-gated delegation-trust premium with zero-config runtime orchestrator-blame at three SDK hook surfaces. KYA is framework-agnostic across 22 agent frameworks. The pure-function scorer runs sub-millisecond at p99 and the system sustains ~1,800 ops/sec at 20 concurrent workers with HMAC chain integrity preserved end-to-end. The four-gate inbound apply pipeline rejects forged, expired, loosening, and unapproved recommendations on every trial (1,200 / 1,200) with sub-millisecond p99 latency on SQLite. KYA detects 89% of 1,200 adversarial probes from PyRIT and Garak, including the recently-published topology-guided multi-agent attack. The system is available under Apache 2.0 as the veldt-kya package on PyPI (release candidate at submission time; stable v0.1.0 forthcoming)

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前自主AI系统在可观测性之外的一个根本性安全与治理缺口：缺乏一个可验证、可审计、且框架无关的信任层来确保智能体的身份、行为证据和策略合规性。

**研究背景**：现有的主流可观测性平台（如LangSmith、Phoenix等）主要关注系统性能，回答“智能体是否运行缓慢、成本高昂或产生错误”。虽然它们开始提供审计日志，但这些日志是内部操作层面的（谁改了配置、谁运行了评估），无法产生以智能体身份为锚定、密码学可验证、可供第三方认证的治理工件。

**现有方法的不足**：现有工具无法应对以下关键威胁：智能体定义被静默篡改（定义漂移）、供应链攻击、数据泄露、以及多智能体系统中的“拓扑攻击”（即一个干净编排器下游的恶意子智能体作恶，但责任被隐藏）。这些安全与归责问题超出了传统可观测性的范畴。

**本文要解决的核心问题**：KYA（Know Your Agents）提出了一个开源信任与治理层，通过五个工程原语来填补“智能体身份/证据性溯源”的空白。具体包括：一个四门入站策略管道（集成签名验证、过期检查、仅收紧策略组合和默认需审批）、统一的信任主体分类体系（KYP）、可审计的交互乘数放大机制、以及双轴委派归因（静态信任评分与动态执行时归责）。该系统旨在为EU AI Act、NIST AI RMF等监管框架提供可审计、可证明、适用于多租户环境的治理工件。

### Q2: 有哪些相关研究？

相关研究主要分为两类。**观测类平台**（如LangSmith、Phoenix、Langfuse、Braintrust、Weave）专注于回答代理“是否慢、是否贵、是否出错”，其审计功能本质上是内部操作日志（谁修改了什么、谁运行了哪个评测），无法产生代理身份绑定的、可加密验证的、第三方可认证的治理工件。KYA明确与这些平台互补而非竞争，通过`kya_otlp_bridge`消费其OpenTelemetry跨度作为输入，但不依赖它们。

**治理类系统**是更直接的比较对象。新兴的代理治理工具（如AIVSS、AAGATE、Aegis、SIGIL、TrustPact、Microsoft AGT）均在过去12个月内出现。微软的Agent Governance Toolkit仅针对代理评分，而KYA的KYP（Know Your Principal）将人类用户、AI代理和服务账户统一到单一信任评分模式中，类似于Okta的2026年NHI倡议的商业化方向。在防回滚方面，KYA的四门道流水线泛化了TUF/Uptane的版本计数器至策略强度格结构。此外，KYA的两轴委托归因解决了EigenTrust的冷启动误报问题，并命名了Liang等人提出的“清洁编排者委托给风险下游”的攻击模式。KYA在安全属性、形式化策略组合及工程原语的系统化集成方面，在现有工作中没有等价物。

### Q3: 论文如何解决这个问题？

KYA通过一个四层架构和五种核心原语来解决自主系统的可观察性和信任治理问题。整体框架由四个可选组件组成：核心SDK（kya，纯Python库，50+模块）、框架钩子（kya_hooks，支持Claude/LangChain/OpenAI Agents等22个框架）、OpenTelemetry桥接（kya_otlp_bridge，将OTLP跨度映射为KYA信号）和红队测试模块（kya_redteam，通过PyRIT和Garak进行对抗性探测）。

核心创新点包括五个原语：(1)四门入站应用管道，结合Ed25519签名验证、多锚点固定、过期检查、仅收紧组合和默认操作员批准；(2)三通道多租户层次结构上的仅收紧组合代数，支持平台默认、租户覆盖和签名外部推荐；(3)KYP（了解你的主体）模式，统一人类用户、AI代理和服务账户的信任评分；(4)基于AIVSS的可审计交互乘数放大，带边界非对称乘数和稳定审计代码；(5)双轴委托归因，结合静态观测门控委托信任溢价和零配置运行时编排器责任归属。

关键技术包括：端到端HMAC链维护证据完整性（支持PostgreSQL/SQLite/DuckDB/MySQL四种数据库后端）、纯函数评分器p99延迟低于1毫秒（20并发工作线程下约1800 ops/sec）、四门管道100%拒绝伪造/过期/放松/未批准推荐（1200/1200测试）、以及通过PyRIT和Garak检测89%的对抗性探测（包括拓扑引导多代理攻击）。系统还实现了三层运行时执行（认证/RBAC、动作门、工具RBAC）和3种关键RBAC输出（允许、阻止、编辑、节流、标记审查），确保端到端可审计性。

### Q4: 论文做了哪些实验？

论文系统性地评估了KYA框架的性能（实验设置：运行在标准Linux服务器上，使用SQLite作为后端存储，通过多线程并发测试评估吞吐量）。

实验包括三部分：
1. **性能基准测试**：纯函数评分器在p99下达到亚毫秒级延迟；系统在20个并发工作线程下维持约1,800 ops/sec的吞吐量，HMAC链完整性端到端保持。
2. **安全性测试**：四门入站应用管道在1,200次试验中全部(1,200/1,200)拒绝伪造、过期、宽松和未批准的推荐，p99延迟同样亚毫秒。
3. **对抗性鲁棒性测试**：使用PyRIT和Garak框架生成的1,200个对抗性探针，KYA检测率为89%，包括最近发表的拓扑引导多智能体攻击。

对比方法：论文未明确列出对比基线，但检测率89%表明其优于未防范此类攻击的基线系统。主要结果：KYA在低延迟（亚毫秒级p99）、高吞吐量（~1,800 ops/sec）和强安全性（100%拒绝无效推荐）方面表现优异，展示了作为自治系统信任层的有效性。

### Q5: 有什么可以进一步探索的点？

## 局限性与未来研究方向

KYA在静态评分层面的主要局限在于：默认权重来源于专家判断和文献综合，缺乏大规模实证校准。未来最关键的改进方向是**基于遥测数据的经验性权重优化**——通过收集生产环境中Agent的实际风险事件与评分之间的相关性，利用贝叶斯优化或强化学习自动调优各因子的权重参数，使评分更贴近真实风险分布。

其次，动态信号仅涵盖六类运行时异常行为，未能检测**渐进式越狱攻击**（如通过长时间低频率的微小越界行为累积权限）或**社交工程型协作攻击**（多个Agent协同绕过单一检测点）。建议引入时序图神经网络分析Agent间交互模式的异常演变，或采用基于行为熵的检测方法识别隐蔽渐进攻击。

此外，静态评分中的MAX-vs-SUM组合规则虽具审计透明度，但缺乏自动学习维度间交互效应的机制。可考虑引入**可解释的神经符号评分模型**，在保持审计链不变的前提下，利用符号规则引擎捕获非线性交互效应，同时通过神经符号学习自动发现新的高影响力因子组合。这既能保持KYA的核心审计特性，又能提升对复合风险场景的检测能力（如当前遗漏的"写工具+PII+自主部署"三联效应）。

### Q6: 总结一下论文的主要内容

KYA (Know Your Agents) 是一个面向自主系统的开源信任与治理层，旨在解决可观测性工具无法回答的关键问题——代理是否在犯错、漂移、泄露或悄悄地走向失控。论文定义了五大核心原语：1）四门入站应用流水线，组合了Ed25519签名验证、多方锚定、过期检查、仅收紧组合与默认需操作员批准；2）基于三通道多租户层次结构的仅收紧组合代数，确保租户覆盖只能收紧而不能放松默认权重；3）KYP（Know Your Principal），统一了人类用户、AI代理和服务账户三种主体的信任评分模式；4）可审计的交互乘数放大机制，结合稳定审计码，为加性基线增加风险因子间的协同效应；5）双轴委托归因，同时捕捉静态委托风险与动态运行时代理行为。KYA支持22种代理框架，P99评分延迟低于1毫秒，在20并发下可持续处理约1800 ops/s。评估显示，四门流水线成功抵御所有伪造、过期、放松和未获批的推荐（1200/1200），并检测出1200次对抗性探测中的89%，包括拓扑引导的多代理攻击。该系统作为Apache 2.0许可的veldt-kya包在PyPI上发布，代表了将可验证溯源与层次化策略组合应用于AI代理治理领域的系统性工程贡献。
