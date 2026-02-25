---
title: "Right to History: A Sovereignty Kernel for Verifiable AI Agent Execution"
authors:
  - "Jing Zhang"
date: "2026-02-23"
arxiv_id: "2602.20214"
arxiv_url: "https://arxiv.org/abs/2602.20214"
pdf_url: "https://arxiv.org/pdf/2602.20214v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.OS"
tags:
  - "AI Agent"
  - "Agent Security"
  - "Verifiable Execution"
  - "Agent Governance"
  - "Agent Logging"
  - "System Architecture"
  - "Capability-based Security"
  - "Merkle Tree"
  - "AI Regulation"
  - "Sovereignty Kernel"
relevance_score: 8.5
---

# Right to History: A Sovereignty Kernel for Verifiable AI Agent Execution

## 原始摘要

AI agents increasingly act on behalf of humans, yet no existing system provides a tamper-evident, independently verifiable record of what they did. As regulations such as the EU AI Act begin mandating automatic logging for high-risk AI systems, this gap carries concrete consequences -- especially for agents running on personal hardware, where no centralized provider controls the log. Extending Floridi's informational rights framework from data about individuals to actions performed on their behalf, this paper proposes the Right to History: the principle that individuals are entitled to a complete, verifiable record of every AI agent action on their own hardware. The paper formalizes this principle through five system invariants with structured proof sketches, and implements it in PunkGo, a Rust sovereignty kernel that unifies RFC 6962 Merkle tree audit logs, capability-based isolation, energy-budget governance, and a human-approval mechanism. Adversarial testing confirms all five invariants hold. Performance evaluation shows sub-1.3 ms median action latency, ~400 actions/sec throughput, and 448-byte Merkle inclusion proofs at 10,000 log entries.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI代理（AI agents）在代表人类执行行动时，缺乏一个防篡改、可独立验证的完整历史记录的问题。随着欧盟《人工智能法案》等法规开始强制要求对高风险AI系统进行自动日志记录，这一缺失已从设计漏洞演变为具体的监管责任。研究背景是AI代理正日益广泛地代表人类执行发送邮件、修改文件、调用API等操作，但现有系统无法提供密码学证明，来证实具体执行了哪些操作、由谁授权、以及代理是否越界。

现有方法存在明显不足。操作系统层面的审计机制（如auditd、eBPF追踪）工作在系统调用粒度，无法将行动归因于代理层面的语义，也不支持人机协同治理。透明的日志系统（如证书透明、Trillian）提供了密码学工具，但从未被应用于记录AI代理行动。此外，现有监管框架通常假设存在一个由中心化提供商控制的日志服务器，而当代理运行在个人硬件上时，这一前提不复存在，导致无人能保证记录的完整性、存在性和不可篡改性。

因此，本文要解决的核心问题是：如何为在个人硬件上运行的AI代理，构建一个能够确保**完整、可验证、防篡改**的行动历史记录的系统。论文将这一需求提炼为“历史权”原则，并通过形式化模型和系统实现来填补现有研究的空白。具体而言，论文提出了一个包含五个系统不变量的形式化框架，并实现了名为PunkGo的“主权内核”，它统一了Merkle树审计日志、基于能力的隔离、能量预算治理和人工批准机制，旨在从系统架构层面保障这一权利。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和法规驱动类。

在**方法类**研究中，现有AI代理框架（如AIOS、LangGraph、OpenAI SDK）主要关注策略层（如调度、权限管理、人工审批开关），但缺乏生成持久、防篡改且可独立验证的行动记录的证据层。这些系统无法提供密码学证据或审计日志，与本文构建可验证执行记录的核心目标形成直接对比。

在**应用类**研究中，密码学领域已为类似问题提供了成熟方案。例如，证书透明度（Certificate Transparency）使用Merkle树追加日志来公开记录TLS证书颁发，其数据结构（如Crosby等人的防篡改日志方案）可实现高效的小规模证明。Attested Append-Only Memory (A2M) 进一步将追加原语嵌入可信计算基。这些工作证明了可验证日志范式的可行性，但均未应用于操作系统层面的AI代理行为审计。本文的PunkGo系统正是将这一范式从记录证书/密钥扩展到记录代理行动。

在**法规驱动类**研究中，欧盟《人工智能法案》明确要求高风险AI系统具备自动事件记录、人工监督和日志保留能力。现有合规讨论通常假设集中式服务提供商场景，而本文针对个人硬件上运行的代理（缺乏中心化日志控制者）这一新兴用例，提出了“历史权”原则，将日志要求从合规负担转化为用户权利，填补了现有数据主权研究（关注数据所有权）与计算历史所有权之间的空白。

### Q3: 论文如何解决这个问题？

论文通过设计并实现一个名为PunkGo的“主权内核”系统来解决AI代理行为缺乏防篡改、可独立验证记录的问题。其核心方法是构建一个三层架构的、以内核为可信计算基（TCB）的集中式提交点，确保所有代理行为都必须经过内核的验证、记录和证明，从而生成一个完整且可验证的日志。

**整体框架与主要模块**：
系统采用三层架构：1) **内核层（TCB）**：作为唯一的提交点，由Rust实现，包含事件日志（基于Merkle树）、能量账本、边界检查器、负载验证器和审计证明器等核心模块。2) **代理层**：负责LLM推理、工具调用等，但只能通过提交动作与内核交互，不能直接访问系统资源。3) **客户端层**：提供用户界面（如仪表盘、审批界面），通过远程协议（如Matrix）与代理层通信，不与内核直接交互。这种设计使内核与命令来源无关，确保了审计的一致性。

**关键技术**：
1. **基于Merkle树的防篡改事件日志**：采用RFC 6962标准的Merkle哈希树结构（与Google tlog算法一致）来存储所有事件。每个事件作为叶子节点，其哈希值被纳入树中，生成可公开验证的根哈希。这提供了O(log n)大小的包含证明和一致性证明，确保日志的**完整性**和**仅追加**特性，任何篡改都会导致根哈希不匹配。
2. **基于能力的边界隔离模型**：遵循最小权限原则。每个行动者（actor）拥有一个可写集合（writability set），定义了其可操作的目标和动作类型。内核的**边界检查器**在验证步骤中强制执行此策略，确保行动者只能在其授权范围内行动（**边界执行**），未经授权的动作将被拒绝且不记录。
3. **能量预算治理模型**：引入“能量”作为资源核算机制，用于防御拒绝服务攻击并约束行为。能量基于硬件计算能力（如TOPS）持续生产，并按份额分配给行动者。每个动作类型（观察、创建、变更、执行）都有预定义的成本函数（成本递增）。行动者执行动作前需预留足够能量，否则动作被拒绝。这确保了系统的可持续性（**能量守恒**）。
4. **人工审批（Hold）机制**：当代理尝试执行敏感操作（匹配信封中预定义的hold规则）时，内核会**短路**正常流程：在验证步骤内部原子化地完成成本报价、能量预留，并立即将一个`hold_request`事件追加到日志中，然后返回等待审批状态。人类用户可批准、拒绝或等待超时。批准后，原始动作会带着重放保护标记重新提交，走完完整管道；拒绝或超时则会结算一部分“承诺成本”（如预留能量的20%）并记录结果。该机制在提供人工监督的同时，通过成本约束了恶意代理的边界探测。
5. **单一提交者（Sole Committer）设计**：内核作为唯一提交者，将所有动作线性化并确定性地排序到日志中。这简化了单机场景下的日志一致性，并通过确定的七步同步管道（验证->报价->预留->验证负载->结算->追加->回执）确保每个被边界检查和能量资助的动作都会被**完整**地记录。

**创新点**：
- **理论形式化与系统不变性**：论文首次将“历史权”原则形式化为五个系统不变性（仅追加、完整性、边界执行、反抵赖、能量守恒），并提供了结构化的证明草图，为可验证AI代理执行建立了严谨的理论基础。
- **主权内核的集成设计**：PunkGo创新性地将Merkle树审计日志、能力安全

### Q4: 论文做了哪些实验？

论文进行了两类核心实验：对抗性测试和性能评估。

**实验设置与数据集/基准测试**：
实验在搭载Apple M2芯片的MacBook Pro上运行，使用PunkGo内核的参考实现。性能评估通过一个合成的基准测试程序进行，该程序模拟了典型的AI代理工作负载，包括不同比例的状态变更操作（如`execute`）和只读操作（如`read`）。对抗性测试则通过专门设计的攻击向量来验证系统不变量的鲁棒性。

**对比方法**：
性能方面，论文将PunkGo与一个“基线”系统进行了对比。该基线系统模拟了不具备PunkGo完整验证和隔离功能的、简单的直接日志记录方式，用以量化引入安全机制带来的开销。

**主要结果与关键指标**：
1.  **对抗性测试**：成功确认了论文提出的五个系统不变量（INV-1至INV-5）在设计的攻击下均能保持成立，证明了其篡改证据和可验证记录的核心安全属性。
2.  **性能评估**：
    *   **延迟**：操作（action）提交的**中位数延迟低于1.3毫秒**，证明了内核处理的高效性。
    *   **吞吐量**：系统可持续处理约**每秒400个操作**。
    *   **证明大小**：当事件日志达到10,000条条目时，生成的Merkle包含证明（inclusion proof）大小仅为**448字节**，确保了验证数据的简洁性。
    *   **开销分析**：与基线系统相比，PunkGo因进行边界检查、能量记账和Merkle树更新而产生的额外开销在可接受范围内，验证了其设计在实际中的可行性。

### Q5: 有什么可以进一步探索的点？

该论文提出的主权内核系统在确保AI代理执行历史的可验证性方面迈出了重要一步，但其局限性和未来探索空间依然显著。首先，系统目前主要聚焦于个人硬件上的单机代理，未来需扩展至分布式或云端环境，这涉及跨节点日志同步与一致性验证的挑战。其次，虽然采用了默克尔树和能量预算等机制，但对抗更复杂的攻击（如侧信道攻击、合谋攻击）的鲁棒性有待进一步验证。此外，当前的人类批准机制可能成为效率瓶颈，未来可探索更细粒度的策略（如基于风险的动态批准阈值）以平衡安全与自动化需求。从更广阔的视角看，该框架可结合零知识证明等技术，在保证可验证性的同时增强隐私性（如隐藏敏感操作细节）。最后，如何将该“历史权”原则与现有法律法规（如GDPR、AI法案）具体对接，设计出标准化的审计接口与合规框架，也是推动其落地的关键方向。

### Q6: 总结一下论文的主要内容

本文提出“历史权”原则，主张个人有权获得在其自有硬件上运行的AI代理行为的完整、可验证记录，以应对高风险AI系统强制日志记录（如欧盟AI法案）的需求。核心贡献是设计并实现了一个主权内核PunkGo，通过五个系统不变量的形式化确保日志防篡改与独立可验证。方法上，PunkGo整合了RFC 6962默克尔树审计日志、基于能力的隔离、能量预算治理及人工批准机制，在对抗性测试中验证了所有不变量的可靠性。性能评估显示，其中位操作延迟低于1.3毫秒，吞吐量约400次/秒，在1万条日志条目下默克尔包含证明仅需448字节。该研究为在去中心化环境中实现可审计的AI代理执行提供了可行方案，强化了个人对AI代理行为的控制与问责。
