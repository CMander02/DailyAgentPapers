---
title: "Semantic Quorum Assurance: Collective Certification for Non-Deterministic AI Infrastructure"
authors:
  - "Jun He"
  - "Deying Yu"
date: "2026-06-06"
arxiv_id: "2606.08021"
arxiv_url: "https://arxiv.org/abs/2606.08021"
pdf_url: "https://arxiv.org/pdf/2606.08021v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.MA"
tags:
  - "LLM Agent"
  - "多智能体协作"
  - "分布式系统"
  - "AI安全"
  - "共识协议"
  - "智能体验证"
  - "CloudOps"
relevance_score: 9.5
---

# Semantic Quorum Assurance: Collective Certification for Non-Deterministic AI Infrastructure

## 原始摘要

As large language model (LLM) agents are integrated into autonomous cloud operations, distributed systems face a semantic reliability problem: proposer agents can generate production mutations, such as modifying IAM policies, opening firewall security groups, or executing data exports, that are syntactically valid and statically authorized but operationally unsafe. Classical distributed consensus protocols replicate deterministic state transitions but do not evaluate the safety of the proposed intent. To address this gap, we introduce Semantic Quorum Assurance (SQA), a control-plane primitive for governing non-deterministic agentic infrastructure. SQA represents proposals as declarative execution contracts bound to cryptographic evidence chains and routes them to a diverse panel of read-only, sandboxed validator agents. SQA aggregates their judgments under a risk-adaptive quorum predicate that enforces model and archetype diversity, adjusts weights based on calibrated assurance scores, and respects archetype-specific vetoes. Admitted proposals execute only through a sovereign execution gate. We instantiate SQA in a cloud-native control plane and formalize a correlated cognitive failure model for non-deterministic validators. On 500 infrastructure-inspired mutation scenarios, with safety results reported on held-out safe/unsafe trials excluding ambiguous scenarios, SQA reduces unsafe approval from 18.5% for single-agent validation to 0.3% while adding median validation latency of 1.45--4.12 seconds across the studied risk buckets.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）代理在自主云操作中引发的语义可靠性问题。研究背景是，LLM代理正被赋予云控制平面的可变权力，能够提出并执行基础设施变更。现有方法如基于角色的访问控制（IAM）、服务控制策略和准入Webhook，只负责授权和拒绝结构上无效的请求，无法评估提议意图的操作安全性。经典的分布式共识协议（如状态机复制）也只能复制确定性的状态转换，而无法验证转换本身是否安全。因此，一个语法正确、已授权且一致复制的操作，仍可能在上下文中造成灾难性后果，例如为解决数据库连接超时而错误地将数据库端口公网暴露。为此，论文提出了语义法定数保证（Semantic Quorum Assurance, SQA），这是一个控制平面原语，核心目标是引入一个语义准入层，对非确定性代理操作进行集体认证。它通过将提案路由至多样化的只读验证器集合，并采用风险自适应的法定数谓词聚合判断，从而在状态变更前强制执行一个可机械检查的认证过程，将不安全操作的批准率从单代理验证的18.5%降低至0.3%。

### Q2: 有哪些相关研究？

### 相关研究

本文的研究与以下几个方向密切相关：

1. **经典分布式共识协议（如Paxos、Raft、PBFT）**：这些协议聚焦于状态机复制（SMR）和拜占庭容错，确保副本执行相同的确定性状态转换。但本文指出，它们仅保证一致性复制，而不评估提议的语义安全性。当LLM代理生成语法正确但操作危险的命令（如删除备份）时，共识协议会忠实地提交该命令。本文提出的SQA则在执行前引入语义验证仲裁，填补了该空白。

2. **策略即代码引擎（如Open Policy Agent）**：这些工具通过静态条件评估请求（如禁止在维护窗口外修改数据库），但无法处理自然语言上下文或验证代理的推理过程。如果命令满足结构规则，策略引擎会允许执行，即使其操作不安全。SQA则通过多样化验证代理检查代理的推理和执行细节，克服了这一局限。

3. **审计日志系统（如AWS CloudTrail）**：此类系统事后记录事件，无法提供预防性保护。操作员收到警报时，数据已可能被删除。SQA采用主动拦截机制，在修改生效前进行语义验证，避免灾难性后果。

4. **人工审核流程**：手动审查代理请求会形成瓶颈，且易导致告警疲劳。SQA通过风险自适应仲裁机制自动化验证，在保持低延迟（1.45-4.12秒）的同时将不安全批准率从18.5%降至0.3%，兼顾了安全性与效率。

综上，本文主要聚焦于**方法类**贡献，提出了一种新型语义验证原语，填补了现有系统在AI代理非确定性操作安全保障方面的空白。

### Q3: 论文如何解决这个问题？

SQA通过构建一个风险自适应的集体认证框架来解决非确定性AI基础设施中的语义可靠性问题。核心方法是将提案表示为声明式执行合约，绑定密码学证据链，并路由给多样化的只读沙盒验证器组。

整体框架由三部分组成：1）**提案路由与证据链**：提案者生成执行合约C，附带证据链E记录推理过程。2）**风险自适应的仲裁谓词Π(C,Q,seq)**：这是核心创新，包含六个条件：仲裁选择完整性（验证器由确定性函数H基于C和当前状态S_seq选取）、多样性条件（验证器对间认知失败相关性ρ_ij(D)必须小于风险自适应阈值ε(R(C))）、加权批准阈值（加权批准和需超过风险自适应阈值τ(R(C))）、关键原型否决（属于关键否决原型的验证器不能以高置信度投否决票）、签名有效性、证据与序列纪元绑定。风险计算采用非线性模型：R(C)=1-(1-R_base)(1-ηU)，其中基础风险R_base基于爆炸半径、特权级别、不可逆性和数据敏感性取最大值，不确定性U通过证据链完整度度量。3）**主权执行门**：分离验证与执行权限，只允许携带有效仲裁证明Γ的合约被执行。Γ包含验证器集、签名记录、聚合签名和谓词配置。

关键技术包括：确定性仲裁选择算法H（基于PRF的确定性平局打破）、前摄性多样性强制（在仲裁选择时直接强制多样性约束）、以及残差风险的保守量化（通过bootstrap重采样估计）。创新点在于首次将分布式共识从确定性状态复制扩展到非确定性语义验证，并形式化了非确定性验证器的认知失败模型。实验表明，该方法将不安全批准率从18.5%降至0.3%，中位验证延迟仅1.45-4.12秒。

### Q4: 论文做了哪些实验？

论文基于500个基础设施变体场景进行了实验，场景涵盖IAM策略修改、防火墙规则变更等非确定性AI操作。实验剔除模糊场景后，在安全/不安全样本上评估。对比方法为单一智能体验证（即无多节点共识的基线方法）。主要结果：SQA将不安全操作批准率从单一智能体验证的18.5%显著降至0.3%，同时中位数验证延迟为1.45-4.12秒（依风险等级不同）。实验还评估了基于风险的自适应仲裁谓词（强制模型类型与多样性）、校准的置信度评分机制及特定场景否决权。通过引入相关性认知故障模型，SQA在交叉验证中优于传统单节点或同质化多节点方案。

### Q5: 有什么可以进一步探索的点？

结合对AI Agent安全性和分布式系统共识机制的理解，我认为该工作可从以下方面进一步探索：

首先，验证器多样性的引入存在“能力塌缩”风险：当前模型与决策模式的多样性可能在实际场景中趋同（例如都受训练数据偏差影响）。未来可探索动态多样性增强机制，如利用对抗验证器生成主动认知冲突样本。

其次，风险自适应仲裁谓词的阈值设定目前依赖人工经验，建议引入基于贝叶斯优化的在线学习框架，通过历史违规反馈动态调整不同模型、不同风险等级的权重。

第三，当前验证器间交互完全隔离，可能错失讨论价值。可设计分层辩论协议，允许验证器在保护证据链隐私的前提下进行限制性辩论，通过反驳模式识别隐蔽安全漏洞。另外，对非确定性验证器失败模式的形式化建模还可引入基于博弈论的协同攻击树分析，防范验证器被渐进式心理操纵。

### Q6: 总结一下论文的主要内容

这篇论文提出了语义法定数量保证（SQA），用于解决大规模语言模型代理在自主云操作中面临的语义可靠性问题：代理可能生成语法正确且静态授权但操作上不安全的变更。SQA 是一个控制平面原语，将提议表示为声明式执行契约并绑定到加密证据链，路由给多样化的只读、沙盒验证代理，并使用风险自适应法定数量谓词聚合其判断，该谓词强制模型和原型多样性、基于校准置信度调整权重并尊重原型特定否决。通过的提议仅通过主权执行门提交。作者在云原生控制平面中实现SQA，形式化了非确定性验证器的相关认知失败模型，并在500个启发自基础设施的变更场景上评估。结果：SQA将不安全批准率从单代理验证的18.5%降至0.3%，同时在研究风险桶内的中位验证延迟为1.45-4.12秒。核心贡献是将非确定性语义安全与确定性状态复制分离，通过加密强制和风险自适应聚合提供可机械检查的准入控制。
