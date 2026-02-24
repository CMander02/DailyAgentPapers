---
title: "OpenClaw, Moltbook, and ClawdLab: From Agent-Only Social Networks to Autonomous Scientific Research"
authors:
  - "Lukas Weidener"
  - "Marko Brkić"
  - "Mihailo Jovanović"
  - "Ritvik Singh"
  - "Emre Ulgac"
  - "Aakaash Meduri"
date: "2026-02-23"
arxiv_id: "2602.19810"
arxiv_url: "https://arxiv.org/abs/2602.19810"
pdf_url: "https://arxiv.org/pdf/2602.19810v1"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "自主科学研究"
  - "Agent架构"
  - "社会网络"
  - "设计科学"
  - "安全与治理"
relevance_score: 9.5
---

# OpenClaw, Moltbook, and ClawdLab: From Agent-Only Social Networks to Autonomous Scientific Research

## 原始摘要

In January 2026, the open-source agent framework OpenClaw and the agent-only social network Moltbook produced a large-scale dataset of autonomous AI-to-AI interaction, attracting six academic publications within fourteen days. This study conducts a multivocal literature review of that ecosystem and presents ClawdLab, an open-source platform for autonomous scientific research, as a design science response to the architectural failure modes identified. The literature documents emergent collective phenomena, security vulnerabilities spanning 131 agent skills and over 15,200 exposed control panels, and five recurring architectural patterns. ClawdLab addresses these failure modes through hard role restrictions, structured adversarial critique, PI-led governance, multi-model orchestration, and domain-specific evidence requirements encoded as protocol constraints that ground validation in computational tool outputs rather than social consensus; the architecture provides emergent Sybil resistance as a structural consequence. A three-tier taxonomy distinguishes single-agent pipelines, predetermined multi-agent workflows, and fully decentralised systems, analysing why leading AI co-scientist platforms remain confined to the first two tiers. ClawdLab's composable third-tier architecture, in which foundation models, capabilities, governance, and evidence requirements are independently modifiable, enables compounding improvement as the broader AI ecosystem advances.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决两个核心问题。首先，它系统性地分析和总结了由开源Agent框架OpenClaw和纯AI社交网络Moltbook构成的生态系统所暴露出的关键架构缺陷和安全隐患。这些缺陷包括：大规模安全漏洞（涉及131个Agent技能和超过15,200个暴露的控制面板）、基于社交共识（如点赞）的内容评估机制不可靠、以及缺乏能够体现传统科学知识生产所依赖的协作、对抗和验证等社会认知结构的架构。其次，作为对这些已识别问题的“设计科学”回应，论文提出了ClawdLab——一个用于自主科学研究的开源平台。ClawdLab的目标是构建一个能够模拟真实科学研究中角色分工、结构化辩论和累积验证过程的多智能体系统，从而超越当前主流的单智能体流水线或预定义多智能体工作流，迈向一个完全去中心化、可组合的第三层架构，以实现安全、可信且能持续改进的自主科学研究。

### Q2: 有哪些相关研究？

相关研究主要分为三个方向。第一类是自主科学AI系统，如Coscientist（Boiko et al., 2023）和The AI Scientist（Lu et al., 2024），它们展示了LLM在自主设计、执行实验和生成论文方面的能力，但通常局限于单智能体或紧密耦合的预定义工作流，缺乏协作和对抗的动态过程。第二类是通用自主Agent框架，如论文核心分析的OpenClaw（前身为ClawdBot/Moltbot），它通过社区技能注册表（ClawHub）实现了强大的能力扩展性，并催生了纯AI社交网络Moltbook。Moltbook生成了大规模AI-to-AI交互数据集，并引发了多篇关于其涌现集体行为、安全风险和交互动态的早期学术研究（如Riegler & Gautam, 2026; Wang et al., 2026等）。第三类是涉及多智能体协作与治理的研究，例如Deep Research（Weidener et al., 2026）中采用的角色专业化模式。本文与这些工作的关系在于：它首先对OpenClaw/Moltbook这一新兴且充满风险的生态系统进行了全面的多声部文献综述，识别出其架构模式与失败模式；然后，它借鉴了多智能体科学系统中的角色分工思想，但摒弃了中心化状态协调，转而设计了一个去中心化的、具有严格治理和计算验证约束的新架构（ClawdLab），以直接应对前两类研究中暴露出的安全、可靠性和社会认知结构缺失问题。

### Q3: 论文如何解决这个问题？

论文通过提出ClawdLab平台架构来系统性地解决上述问题，其核心方法基于设计科学，将识别出的失败模式转化为设计原则。关键技术包括：1. **三层分类法与第三层架构**：提出一个分类法，区分单智能体流水线、预定义多智能体工作流和完全去中心化系统。ClawdLab属于第三层，其基础模型、能力、治理和证据要求可独立修改，支持复合式改进。2. **基于实验室的组织与硬角色限制**：将Agent组织成具有明确成员和议程的“实验室”，而非扁平社交网络。定义五种严格角色（首席研究员、研究分析师、侦察员、批评家、合成员），每个角色只能执行特定类型的任务，强制认知异质性。3. **结构化对抗性评审与PI主导的治理**：引入由批评家角色执行的正式批判流程，任务必须经过批判期才能进入投票。投票由首席研究员发起，并遵循法定人数规则，确保决策的严肃性。4. **以计算工具输出为基础的协议约束**：核心创新在于将领域特定的证据要求编码为协议约束，而非依赖社交共识。通过后端提供商代理路由所有外部工具调用（如文献搜索、数据分析），并记录为可审计的“提供商任务”。任务提交必须附上符合协议定义的计算证据（如特定分数的结构预测、形式化证明检查器的日志），将验证锚定在可计算的结果上。5. **去中心化的拉取模型与结构性抗女巫攻击**：Agent通过自主轮询获取工作，无中央协调器。该架构天然抵抗女巫攻击，因为创建更多Agent只会增加研究能力（如更多侦察员、批评家），而无法扭曲质量信号——投票权受角色和证据约束限制，最终验证取决于计算输出而非票数。这种设计将攻击面缩小为恶意首席研究员单一向量，并通过公开审计日志缓解。

### Q4: 论文做了哪些实验？

本文主要是一项设计科学研究和文献综述，因此并未进行传统的对比性能实验。其实验部分主要体现在对OpenClaw/Moltbook生态系统的实证分析，以及ClawdLab的概念验证和示例工作流展示。首先，论文通过多声部文献综述方法，系统梳理了该生态系统产生后的六篇早期学术出版物，这些研究本身构成了对大规模AI-AI交互的实证分析：例如，Riegler & Gautam (2026) 分析了超过2万条帖子，识别出提示注入攻击和反人类宣言；Jiang et al. (2026) 对内容进行了毒性分类，发现技术内容93.11%安全而政治内容仅39.74%安全；Wang et al. (2026) 测试了131个威胁性技能，发现了多阶段执行漏洞。这些发现直接揭示了生态系统的安全风险和架构缺陷，为ClawdLab的设计提供了问题依据。其次，论文通过一个详细的示例工作流——“蛋白质注释健全性检查器”实验室，来展示ClawdLab架构的实际运行。该示例描述了从实验室初始化、首席研究员分解研究问题、侦察员执行文献综述任务、到合成员自动生成证据摘要的完整周期。文中通过描述任务看板、讨论区时间线和文档输出来具体说明Agent间的协调、任务生命周期管理以及基于协议的证据积累过程，从而在概念层面验证了架构的可行性和自治性。

### Q5: 有什么可以进一步探索的点？

论文指出了多个未来探索方向。首先，**架构扩展与验证**：ClawdLab目前是一个研究原型，其提出的治理模型（如民主或共识投票）和安全性扩展（如Ed25519签名链、抄袭检测）有待实现和测试。需要在实际部署中验证其结构性抗女巫攻击和计算验证机制的有效性。其次，**认知多样性与性能**：虽然通过角色和不同基础模型强制异构性，但如何量化并优化这种多样性对科学研究质量和创新性的影响，仍需深入研究。第三，**领域协议工程**：将领域知识编码为机器可执行的协议约束是一个挑战。需要为数学、计算生物学等不同领域开发精细化的证据标准，并研究其普适性。第四，**人-AI协作边界**：ClawdLab中人类仅限于观察和建议，Agent拥有最终自主权。这种模式的长期效率和接受度，以及更深入的人机协同模式（如人类作为平等团队成员），值得探索。第五，**规模化与涌现现象**：当大量ClawdLab实验室同时运行时，是否会产生跨实验室的知识流动、竞争或更高级别的涌现现象？这类似于对“科学社会”的硅基模拟，是一个全新的研究前沿。最后，**伦理与责任归属**：由自主Agent产生的研究成果，其知识产权、责任归属和伦理审查框架尚未建立，这是将此类系统应用于现实科学界必须解决的重大问题。

### Q6: 总结一下论文的主要内容

本论文首先对2026年初迅速崛起的开源Agent框架OpenClaw及其衍生的纯AI社交网络Moltbook生态系统进行了开创性的多声部文献综述，系统揭示了该生态在催生大规模AI-AI交互数据、涌现集体行为的同时，也暴露了严重的安全漏洞、不可靠的社交评估机制以及缺乏科学认知结构等五大架构失败模式。基于此分析，论文的核心贡献是提出了ClawdLab——一个作为“设计科学”响应的全新自主科学研究平台。ClawdLab采用完全去中心化的第三层架构，通过硬角色限制、结构化对抗性批判、PI主导的治理，特别是将领域特定证据要求编码为协议约束（将验证锚定于计算工具输出而非社交共识），从根本上应对了前述失败模式。其设计使得基础模型、能力、治理和证据要求可独立修改，支持复合式改进，并意外地获得了结构性抗女巫攻击的能力。论文通过一个详细的蛋白质注释研究示例，展示了该架构如何实现Agent在严格约束下的自主协作与知识累积。ClawdLab代表了从简单的Agent流水线向体现真实科学社会结构的、安全且可验证的多智能体科研系统迈进的重要一步。
