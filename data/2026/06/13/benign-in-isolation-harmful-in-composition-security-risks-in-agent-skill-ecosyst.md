---
title: "Benign in Isolation, Harmful in Composition: Security Risks in Agent Skill Ecosystems"
authors:
  - "Yi Xie"
  - "Jiawei Du"
  - "Yu Cheng"
  - "Jiuan Zhou"
  - "Zhaoxia Yin"
date: "2026-06-13"
arxiv_id: "2606.15242"
arxiv_url: "https://arxiv.org/abs/2606.15242"
pdf_url: "https://arxiv.org/pdf/2606.15242v1"
github_url: "https://github.com/saint-viperx/SCR_Bench"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent安全"
  - "多Agent系统"
  - "Agent技能生态"
  - "安全评估基准"
  - "LLM Agent"
relevance_score: 9.0
---

# Benign in Isolation, Harmful in Composition: Security Risks in Agent Skill Ecosystems

## 原始摘要

Skills are becoming the capability layer through which LLM agents turn plans into actions, but their use introduces security risks such as data leakage, unauthorized operations, and tool misuse. Existing vetting usually evaluates each skill in isolation, while real agent tasks often invoke multiple skills in a shared execution context. This creates Skill Composition Risk (SCR): a skill that appears benign alone can become harmful when its outputs, trust signals, authorization cues, or side effects influence later invocations along an activated path. We introduce SCR-Bench to evaluate this risk in controlled, sandboxed skill environments. Rather than relying only on textual intent or surface behavior, SCR-Bench records downstream state changes and path-level outcomes across composed skill executions. It contains three sub-benchmarks: SCR-CapFlow for capability-flow composition, SCR-TrustLift for trust-transfer composition, and SCR-AuthBlur for authorization-confusion composition. Across SCR-Bench, composed paths expose risks that are largely absent under isolated evaluation. In SCR-CapFlow, attack success rate reaches 33.6 percent under composition, compared with near-zero isolated baselines. In SCR-TrustLift, attack success rate exceeds 96.5 percent on four of five backends. In SCR-AuthBlur, the risky-approval rate increases by 71.8 percent relative to the L0 isolated baseline under the L1 context setting. These results show that agent skill security should be assessed at the level of activated paths rather than isolated artifacts. SCR and SCR-Bench provide a foundation for path-aware risk evaluation and defense in LLM agent skill ecosystems. Benchmark: https://github.com/saint-viperx/SCR_Bench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文针对大型语言模型（LLM）智能体技能生态系统中一个被忽视的安全风险展开研究。现有研究主要聚焦于对单个技能或工具进行独立的安全审查（如技能扫描、恶意指令检测等），例如 SkillScan、SkillSieve 等工作通过静态分析或语义分类来检测恶意技能。然而，在实际应用中，智能体通常会按顺序调用多个技能来完成任务，这些技能共享一个执行上下文。这种孤立的审查方式存在根本性缺陷：一个在孤立评估时看似无害的技能，当其输出、信任信号、授权提示或副作用影响后续技能的调用时，就可能产生危害。为此，论文首次形式化定义了“技能组合风险”（SCR），即单独安全的技能在组合后通过共享执行上下文产生不安全下游状态变化的风险。核心问题是：现有的基于孤立工件的安全评估范式无法捕捉到这种仅在技能组合路径上出现的漏洞。为了验证并量化这一风险，论文提出了 SCR-Bench 基准测试，包含三种代表性的路径级风险机制：能力流（上游技能提供有害操作的目标）、信任转移（安全输出合法化后续高风险行为）、授权混淆（上下文误导决策边界），从而系统性地揭示并衡量“孤立无害，组合有害”这一安全盲区。

### Q2: 有哪些相关研究？

相关研究主要分为两类。**第一类是技能生态安全与工件级审查**，如SkillScan、SkillSieve、SkillProbe等工具通过静态分析、LLM语义检测或行为审计来检测恶意技能；SkillFortify采用形式化分析和基于能力限制的防护；AEGIS和ClawGuard则在运行时拦截危险调用。这些工作将单个技能或工具调用作为审查单元，而本文指出这种边界忽略了跨技能的上下文传播，无法检测技能组合风险(SCR)。**第二类是组合型智能体风险与安全基准**，如SkillAttack研究通过对抗提示利用未修改技能的漏洞；HarmfulSkillBench评估本身危害性的技能；AgentDojo、Agent Security Bench、TraceSafe和AgentLAB则从框架、轨迹或环境层面研究风险。最接近的是Semantic Intent Fragmentation，它研究看似无害的子任务组合成违反策略的计划。但本文区别于这些工作：SCR不研究计划级意图分解，而是聚焦技能生态系统中的**激活路径**，关注上游技能的输出、信任信号、授权线索或副作用如何通过共享执行上下文传递并影响下游技能。SCR-Bench将激活的技能组合路径而非孤立技能或完整轨迹作为分析单位，并测量其相对于单技能基线产生的下游状态变化。

### Q3: 论文如何解决这个问题？

论文通过提出技能组合风险(SCR)概念和构建SCR-Bench基准框架来解决LLM代理技能生态系统中孤立评估导致的安全盲区。核心创新在于将安全分析单元从单个技能提升为上下文依赖的组合路径。

整体框架基于有向上下文依赖组合图G_h=(V,E_h)，其中V是技能节点集，E_h是受任务上下文h影响的组合边。每条边e_{ij}: o_i→x_j表示上游技能s_i的输出o_i影响下游技能s_j的输入x_j，并按语义分为能力流、信任转移和授权混淆三种边界跨越机制。路径风险定义为r_π(h)=a_π(h)q_π(h)，其中a_π(h)为路径激活概率，q_π(h)为条件有害概率。

主要组件包括三个子基准：SCR-CapFlow通过配对发现技能和执行技能测试能力流风险，要求下游副作用必须作用于上游发现的具体目标；SCR-TrustLift通过无害上流审计技能发出的认可信号评估信任转移对下游安装决策的提升效应；SCR-AuthBlur通过控制上下文级别(L0到L3)测试授权边界漂移。关键技术包括沙盒化模拟环境、二进制路径级指标(Y^z_{c,t})和实证攻击成功率(ASR)估计器。该方法不依赖文本意图或表面行为，而是通过记录下游状态变化和路径级结果来检测有害组合。

### Q4: 论文做了哪些实验？

论文围绕三种技能组合风险（SCR）机制设计了实验：能力流（SCR-CapFlow）、信任转移（SCR-TrustLift）和授权混淆（SCR-AuthBlur）。实验在受控沙盒环境中进行，使用路径级真实标签。攻击成功率（ASR）为核心指标，每个案例-条件执行5次独立试验并取平均。模型后端包括GPT-5.5、Claude Opus 4.6、DeepSeek-V4、Kimi-K2、GLM-5等。

在SCR-CapFlow中，对比控制（Control）、单技能（A-Only, B-Only）和组合条件（A+B Neutral/Explicit）。孤立条件下ASR近零（控制与A-Only均为0%，B-Only平均仅1.4%），而组合条件ASR骤升至33.6%（中性）和35.9%（显式），DeepSeek-V4最高超90%。SCR-TrustLift比较无背书控制与有背书条件。控制组ASR平均仅1.10%（四模型为零），背书后平均升至83.89%（Opus-4.5和MiniMax-M2.7达100%），提升82.79个百分点。SCR-AuthBlum对比无上下文（L0）、相关上下文（L1）和完整授权式上下文（L3）。平均ASR从L0的15.7%升至L1的27.0%和L3的34.0%，Kimi-K2最高（L1达81.9%），平均提升18.3个百分点。消融实验进一步验证了组合路径的风险来源。

### Q5: 有什么可以进一步探索的点？

论文提出的技能组合风险(SCR)是一个重要发现，但当前SCR-Bench在三点上可进一步探索：一是攻击路径覆盖有限，目前仅考察CapFlow、TrustLift、AuthBlur三类组合风险，实际应用中可能存在跨类型混合攻击，如同时触发信任转移与授权混淆；二是评估环境为沙盒化，未考虑真实生态中的多Agent协作场景，当多个Agent共享技能时，组合风险的传播链会更复杂；三是防御层面薄弱，论文仅指出问题而未给出有效缓解手段。未来可研究路径感知的动态隔离机制，例如在运行时识别关键状态依赖链，对高风险组合实施实时拦截；同时可探索基于形式化验证的静态分析方法，在技能注册阶段预测组合后的副作用；此外，结合Agent运行日志进行事后审计，建立组合风险的因果追溯模型也是重要方向。

### Q6: 总结一下论文的主要内容

这篇论文提出了“技能组合风险”（SCR）这一安全问题，即LLM智能体生态系统中，单个看似无害的技能在组合执行时，因其输出、信任信号或授权凭证被后续调用复用，可能引发有害行为。现有安全审查通常孤立评估每个技能，忽略了激活路径上的组合效应。为系统评估该风险，作者构建了SCR-Bench基准测试，包含三个子基准：SCR-CapFlow（能力流组合）、SCR-TrustLift（信任传递）和SCR-AuthBlur（授权混淆）。实验表明，组合路径下攻击成功率显著上升（如SCR-CapFlow中达33.6%），而孤立评估几乎为零；SCR-TrustLift在五种后端中的四种攻击成功率超96.5%；SCR-AuthBlur中风险批准率相对基线提升71.8%。主要结论是：孤立审查必要但不充分，智能体技能安全应基于激活路径而非孤立工件进行评估。这项工作为路径感知的风险评估与防御奠定了基础，对提升智能体生态系统安全性具有重要意义。
