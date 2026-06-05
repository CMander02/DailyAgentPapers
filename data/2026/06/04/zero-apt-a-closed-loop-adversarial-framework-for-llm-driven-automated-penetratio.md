---
title: "ZERO-APT: A Closed-Loop Adversarial Framework for LLM-Driven Automated Penetration Testing under Intelligent Defense"
authors:
  - "Anlan Zheng"
  - "Tiantian Zhu"
date: "2026-06-04"
arxiv_id: "2606.05567"
arxiv_url: "https://arxiv.org/abs/2606.05567"
pdf_url: "https://arxiv.org/pdf/2606.05567v1"
categories:
  - "cs.CR"
  - "cs.MA"
tags:
  - "LLM Agent"
  - "Automated Penetration Testing"
  - "Adversarial Framework"
  - "Multi-Agent"
  - "Cybersecurity"
  - "Planning and Execution"
  - "Agent Benchmarking"
relevance_score: 8
---

# ZERO-APT: A Closed-Loop Adversarial Framework for LLM-Driven Automated Penetration Testing under Intelligent Defense

## 原始摘要

LLM-driven automated penetration testing agents are typically evaluated against static targets that neither detect nor respond to attacks, so their behavior under intelligent defense remains untested. The causal consistency of multi-step attack chains likewise hinges on unstable LLM reasoning, and agent decisions remain opaque to human analysts. These three shortcomings, in realism, consistency, and auditability, are usually patched in isolation. We present ZERO-APT, a turn-based attacker-defender-judge framework that addresses them within a single architecture. For realism, ZERO-APT embeds a configurable LLM Defender that consumes Sysmon telemetry and detects attacks in real time, exposing the attacker to a live opponent rather than a passive target. For consistency, three architectural mechanisms move causal consistency from unstable LLM reasoning into enforced system architecture: separation of planning from execution, multi-dimensional ReAct feedback, and a hard-constraint-filtered action library. For auditability, a dedicated Judge agent adjudicates each round, maintains global state, and emits structured post-hoc CTI reports that make every decision traceable. We evaluate a Windows Server 2022 post-exploitation prototype across five scenarios with three Defender configurations. ZERO-APT reaches 79\% attack success rate (Aurora 22\%, PentestGPT 39\%), a Causal Consistency Score of 0.860 (Aurora 0.930, Claude Code 0.520), and end-to-end decision auditability through structured CTI reports. We release the benchmark to support evaluation of penetration agents under intelligent defense.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决当前基于大语言模型（LLM）的自动化渗透测试代理在三个关键维度上存在的共同缺陷：现实性不不足、因果一致性差以及可审计性缺失。

研究背景方面，现有的LLM驱动的渗透测试工具通常部署在静态目标上，这些目标既不会检测攻击也不会做出响应，导致代理与智能防御的交互行为完全未经测试。此外，多步攻击链的因果一致性高度依赖于LLM不稳定的推理能力，而代理的决策过程对人工分析师来说仍然是不透明的。现有研究往往孤立地修补这些缺陷，缺乏统一解决方案。

具体而言，现有方法的不足包括：第一，缺乏能够实时检测攻击的主动防御对手，导致测试环境缺乏现实感；第二，多步攻击链的因果一致性无法通过架构保证，完全依赖LLM推理稳定性；第三，决策过程不可审计，无法生成标准化的追踪报告。本文提出的ZERO-APT框架通过一个回合制的“攻击方-防御方-裁判方”闭环架构，首次将真实性、一致性和可审计性纳入统一系统，解决了这些核心问题。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为以下几类：

**方法类相关工作：**
- **LLM驱动的自动化渗透测试代理**：如Aurora、PentestGPT、Claude Code等。本文提出的ZERO-APT与这些工作的核心区别在于：现有系统通常在静态目标上评估（不检测/响应攻击），而ZERO-APT引入了智能防御者（LLM Defender），使攻击者面对实时响应的对手，显著提高了测试的现实性。此外，现有系统在因果一致性上依赖不稳定的LLM推理，ZERO-APT通过分离规划与执行、多维ReAct反馈、硬约束过滤动作库等架构机制强制保证一致性。

**评测类相关工作：**
- **渗透测试评估基准**：大多数现有基准仅提供静态环境，缺乏对攻击-防御交互的评估。ZERO-APT不仅提供了包含智能防御的基准，还引入了专门的裁判（Judge）智能体进行回合裁决、全局状态维护，并输出结构化的CTI报告，解决了现有系统决策不透明、无法审计的问题。

**应用类相关工作：**
- **网络安全中的AI防御系统**：如基于Sysmon遥测的检测系统。本文不是简单整合现有防御，而是构建了可配置的LLM Defender，使其能实时消耗系统遥测数据检测攻击，形成闭环攻防框架。

综上所述，ZERO-APT在一个统一架构中同时解决了现实性、一致性和可审计性三个独立短板，这是与现有工作的根本差异。

### Q3: 论文如何解决这个问题？

ZERO-APT通过一个三体对抗框架（攻击者-防御者-裁判者）将真实性、一致性与可审计性统一解决。其核心架构基于回合制交互闭环，关键技术包括三个层面：

在真实性层面，引入可配置的LLM驱动的防御者模块。该模块持续消费Sysmon系统监控遥测数据，能实时检测攻击行为，使攻击者面对的不是静态靶标，而是具备动态检测与响应能力的活体对手。防御者的检测强度可通过参数调节，从而模拟不同安全水平的防御环境。

在因果一致性层面，通过三项架构机制将原本依赖LLM不稳定推理的因果逻辑固化到系统架构中：其一，规划与执行分离，将攻击者拆分为规划器（制定策略）和执行器（执行具体动作），避免推理链条断裂；其二，多维度ReAct反馈，在攻击每一步提供环境反馈、防御者检测状态、因果约束检查等多源信号，辅助规划器修正决策；其三，硬约束过滤动作库，通过预定义的安全规则和状态机约束，过滤掉可能破坏因果链的一致性的动作。

在可审计性层面，设计独立的裁判者智能体。裁判者在每一轮对抗后裁决攻击效果、维护全局状态（如已失陷节点、已触发告警），并最终生成结构化的CTI（网络威胁情报）报告，使每一步决策的因果链条和对抗结果都可追溯。

创新点在于：用统一的对抗框架替代以往孤立的补丁式修复；通过架构机制而非LLM推理保证因果一致性；以及引入实时防御方提升评估生态效度。

### Q4: 论文做了哪些实验？

论文基于Windows Server 2022后渗透测试原型，在五个场景中进行了实验。实验设置了三类防御者配置：无防御（Baseline）、基于Sysmon遥测的实时检测防御（LLM Defender）以及混合防御。对比方法包括Aurora、PentestGPT和Claude Code等现有自动化渗透测试系统。主要评估指标包括攻击成功率（ASR）、因果一致性得分（CCS）和端到端决策可审计性。实验结果显示，ZERO-APT在LLM Defender防御下达到79%的攻击成功率（Aurora为22%，PentestGPT为39%），因果一致性得分为0.860（Aurora为0.930，Claude Code为0.520）。决策可审计性通过结构化CTI报告实现，使每个攻击步骤可追溯。此外，实验还验证了攻击者与防御者对抗的回合制交互效果，ZERO-APT在智能防御下仍能保持较高攻击效率，而基线方法在遇到主动防御时性能显著下降。这些结果证实了ZERO-APT框架在提升现实主义（实时对抗）、因果一致性（分离规划与执行、多维ReAct反馈、硬约束动作库）和可审计性方面的有效性。

### Q5: 有什么可以进一步探索的点？

论文提出了LLM驱动的自动化渗透测试框架ZERO-APT，但仍存在若干可探索的方向。首先，当前框架依赖Sysmon作为唯一遥测源，未来可融合EDR、网络流量等多模态数据，提升防御方检测能力。其次，Causal Consistency Score虽达0.860，但低于Aurora的0.930，说明规划-执行分离后的长链因果推理仍依赖LLM稳定性，可引入因果图或符号推理增强一致性。第三，防御者仅具备实时检测能力，缺乏主动诱捕或反制策略，可构建动态蜜罐环境使攻击者策略失效。此外，框架在Windows后渗透场景验证，需扩展至Linux、云原生等异构环境。审计报告目前为结构化CTI报告，可探索自然语言叙事生成以降低分析师理解门槛。最后，当前回合制交互效率低下，可设计并行化攻击-防御博弈机制加速评估。

### Q6: 总结一下论文的主要内容

ZERO-APT提出了一种闭环对抗框架，用于在智能防御场景下评估LLM驱动的自动化渗透测试代理。现有评估通常针对静态目标，缺乏对智能防御的适应性、多步攻击链的因果一致性以及决策可审计性。该框架包含攻击者、防御者和裁判三个角色：防御者利用Sysmon遥测实时检测攻击，增强真实性；通过计划与执行分离、多维ReAct反馈和硬约束过滤动作库，将因果一致性从不可靠的LLM推理转移到系统架构中；裁判代理负责裁决每轮交互、维护全局状态并生成结构化CTI报告，确保可审计性。在Windows Server 2022后渗透测试中，ZERO-APT达到79%的攻击成功率（Aurora 22%，PentestGPT 39%），因果一致性得分0.860，并实现了端到端决策可审计。该工作通过统一架构解决了真实性、一致性和可审计性三大挑战，为智能防御下渗透代理评估提供了新基准。
