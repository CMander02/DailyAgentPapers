---
title: "Sovereign Agentic Loops: Decoupling AI Reasoning from Execution in Real-World Systems"
authors:
  - "Jun He"
  - "Deying Yu"
date: "2026-04-24"
arxiv_id: "2604.22136"
arxiv_url: "https://arxiv.org/abs/2604.22136"
pdf_url: "https://arxiv.org/pdf/2604.22136v1"
categories:
  - "cs.CR"
  - "cs.LG"
tags:
  - "LLM Agent Safety"
  - "Agent Architecture"
  - "Execution Control"
  - "Policy Enforcement"
  - "Auditability"
relevance_score: 7.5
---

# Sovereign Agentic Loops: Decoupling AI Reasoning from Execution in Real-World Systems

## 原始摘要

Large language model (LLM) agents increasingly issue API calls that mutate real systems, yet many current architectures pass stochastic model outputs directly to execution layers. We argue that this coupling creates a safety risk because model correctness, context awareness, and alignment cannot be assumed at execution time. We introduce Sovereign Agentic Loops (SAL), a control-plane architecture in which models emit structured intents with justifications, and the control plane validates those intents against true system state and policy before execution. SAL combines an obfuscation membrane, which limits model access to identity-sensitive state, with a cryptographically linked Evidence Chain for auditability and replay. We formalize SAL and show that, under the stated assumptions, it provides policy-bounded execution, identity isolation, and deterministic replay. In an OpenKedge prototype for cloud infrastructure, SAL blocks 93% of unsafe intents at the policy layer, rejects the remaining 7% via consistency checks, prevents unsafe executions in our benchmark, and adds 12.4 ms median latency.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的自主智能体系统在现实世界执行中存在的核心安全问题。研究背景是，随着LLM智能体越来越多地通过API调用对真实系统进行修改（如软件部署、基础设施操作），当前许多系统架构将模型输出的随机性结果直接传递给执行层。现有方法的不足在于，这种紧密耦合的管道假设模型的推理结果在执行时刻是足够正确、上下文感知且与系统不变量一致的。然而，这一假设在实践中不可靠，因为LLM作为随机模型，可能因部分可观测性、上下文混淆或对齐不足而生成合理语法但却危险的指令（例如，错误地终止关键数据库节点）。事后日志或粗粒度权限边界无法在执行前验证行动的适当性。

因此，本文要解决的核心问题是：如何构建一种架构机制，将LLM的随机推理能力与系统执行权限进行解耦，从而在执行前对模型的提议进行验证，从根本上防止不安全、不合规的操作发生，而非依赖模型自身行为的可靠性。

### Q2: 有哪些相关研究？

本文的相关研究主要分为以下几类：

1. **智能体工具使用与推理框架**：如ReAct、Toolformer及OpenAI/Anthropic的函数调用API。这些工作专注于提升模型推理或工具接口能力，但通常假设生成的动作可直接执行，仅依赖语法验证。本文提出的SAL则通过结构化解耦，将模型输出视为“意图”而非命令，须在主权控制面中验证后才能执行。

2. **运行时护栏与预执行授权**：如AgentSpec（领域特定语言定义规则）、Pro2Guard（基于马尔可夫链的主动干预）、Open Agent Passport（预动作授权与加密审计）。这些方法仍以模型或动作为中心，不保证外部系统执行效果。SAL不同之处在于通过确定性评估函数基于真实系统状态强制执行安全策略，且不依赖模型对齐性。

3. **运行时验证与形式化方法**：如基于STPA的安全分析应用于MCP协议。此类方法假设系统模型已知，但智能体决策由随机模型驱动。SAL通过预执行决策边界与证据链补充了传统追踪验证，实现了确定性回放。

4. **访问控制与能力治理**：如RBAC、ABAC及Aethelgard（基于强化学习的动态能力限定）。传统方法依赖可信调用者身份，而SAL转向基于验证意图的动态授权，即使能力集受限，每次动作仍需策略评估。

5. **多智能体协调与安全**：如MAST（多智能体故障分类）、TAO（分层监督）。这些方法未提供预执行不变性层，SAL可作为任何智能体的执行边界控制面，防止错误通过基础设施突变传播。

6. **控制理论与隐私技术**：SAL通过将意图作为控制信号的反馈闭环结构恢复可控性，并通过混淆膜实现推理与基础设施状态的信息论隔离。现有方法仅解决单个方面，SAL则提供了端到端的执行治理统一框架。

### Q3: 论文如何解决这个问题？

该论文通过提出Sovereign Agentic Loops (SAL)架构来解决AI推理与执行耦合带来的安全风险。核心方法是将模型推理与系统执行解耦，引入一个主权控制平面来中介所有操作。

整体框架是一个四阶段的闭环：1) 推理Agent在模糊膜约束下生成结构化意图和自然语言理由；2) 主权控制平面使用确定性评估函数E对意图进行策略合规性检查(E_policy)和上下文一致性验证(E_consistency)；3) 只有通过验证的意图才通过受控执行操作符X执行；4) 所有步骤记录在加密链接的证据链中。

主要模块包括：**模糊膜**，它是一个投影映射函数Π，将真实系统状态S转换为模糊状态Ŝ，满足互信息I(S_id; Ŝ)=0，确保身份敏感信息不可恢复，同时保留结构信息用于推理。**控制平面**包含策略评估、上下文一致性检查和执行中介。**证据链**记录每个步骤的意图、理由、评估结果、执行动作和上下文快照，支持加密可审计性和确定性重放。

创新点包括：1) 形式化定义了解耦架构的数学基础，包括状态空间二分、模糊映射和信息隔离约束；2) 提出主权评估函数，在真实系统状态下验证意图，而非依赖模型可靠性；3) 设计加密证据链实现确定性重放，确保可审计性；4) 在OpenKedge原型中验证该方法能阻止所有不安全执行，仅增加12.4毫秒中位延迟。

### Q4: 论文做了哪些实验？

论文主要进行了两方面的实验：延迟开销和安全有效性。实验部署在AWS EC2 c6g.2xlarge实例上，使用Redis集群作为混淆膜的内存令牌映射，SHA-256实现证据链，Open Policy Agent作为策略引擎。数据集包含10,000条意图评估轨迹，分为7,500条良性工作负载（常规合规操作）和2,500条对抗性工作负载（红队模拟前沿模型生成的不安全意图）。对比方法为无中介的执行架构。

主要结果包括：1) 延迟方面，端到端评估中位延迟为12.4ms，95分位延迟为21.7ms，其中去混淆2.1ms，OPA策略评估6.8ms，一致性检查2.3ms，哈希与账本序列化1.2ms，表明开销低于典型网络抖动。2) 安全性方面，系统阻止了所有不安全意图（阻塞率100%）：2,325条（93.0%）被策略层拦截，剩余175条（7.0%）被一致性检查器拒绝。3) 可审计性方面，通过证据链对7,500条良性操作进行确定性重放，实现了100%的验证匹配率，无密码学失同步。实验证明SAL在增加约12.4ms中位延迟的情况下实现了操作安全性的显著提升。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于SAL作为控制平面架构，其安全保证高度依赖于策略定义和一致性检查的完备性，若策略存在漏洞或模型输出绕过检查，仍可能导致风险。未来可探索以下方向：首先，引入概率性风险评估机制，结合模型置信度动态调整策略阈值，而非二元拒绝/接受；其次，扩展证据链支持跨机构分布式审计，解决多方协作场景下的隐私与透明度冲突；此外，针对低延迟场景（如金融交易），优化混淆膜的轻量化设计，例如通过知识蒸馏减少身份敏感信息暴露而非完全遮蔽；最后，研究模型与策略的对抗性协同训练，让模型主动学习策略边界以自然减少无效意图生成。核心改进思路在于将静态策略验证扩展为动态、概率化的安全-效率权衡系统。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为“Sovereign Agentic Loops (SAL)”的控制平面架构，旨在解决大语言模型（LLM）智能体在现实系统中直接执行API调用所带来的安全风险。核心问题在于，当前架构常将随机模型输出直接传给执行层，而模型在正确性、上下文感知和对齐性方面并不可靠。SAL通过执行解耦（Execution Decoupling）的方法，要求模型首先输出结构化的意图及其理由，再由控制平面根据真实系统状态和策略进行验证，通过混淆膜限制模型接触身份敏感状态，并利用加密链接的证据链（Evidence Chain）确保可审计性和可重放性。主要贡献在于形式化证明了SAL能提供策略约束执行、身份隔离和确定性重放。在云基础设施原型OpenKedge上的实验表明，SAL可在策略层阻止93%的不安全意图，其余7%通过一致性检查被拒绝，有效防止了不安全执行，且仅增加12.4毫秒的中位延迟，证明了执行中介在低延迟自动化场景中的实用性。
