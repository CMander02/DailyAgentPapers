---
title: "Stateless Decision Memory for Enterprise AI Agents"
authors:
  - "Vasundra Srinivasan"
date: "2026-04-22"
arxiv_id: "2604.20158"
arxiv_url: "https://arxiv.org/abs/2604.20158"
pdf_url: "https://arxiv.org/pdf/2604.20158v1"
github_url: "https://github.com/vasundras/stateless-decision-memory-enterprise-ai-agents"
categories:
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Enterprise AI"
  - "Decision-Making"
  - "Determinism"
  - "Auditability"
  - "Retrieval-Augmented Generation"
  - "Long-Horizon Tasks"
  - "System Properties"
relevance_score: 7.5
---

# Stateless Decision Memory for Enterprise AI Agents

## 原始摘要

Enterprise deployment of long-horizon decision agents in regulated domains (underwriting, claims adjudication, tax examination) is dominated by retrieval-augmented pipelines despite a decade of increasingly sophisticated stateful memory architectures. We argue this reflects a hidden requirement: regulated deployment is load-bearing on four systems properties (deterministic replay, auditable rationale, multi-tenant isolation, statelessness for horizontal scale), and stateful architectures violate them by construction. We propose Deterministic Projection Memory (DPM): an append-only event log plus one task-conditioned projection at decision time. On ten regulated decisioning cases at three memory budgets, DPM matches summarization-based memory at generous budgets and substantially outperforms it when the budget binds: at a 20x compression ratio, DPM improves factual precision by +0.52 (Cohen's h=1.17, p=0.0014) and reasoning coherence by +0.53 (h=1.13, p=0.0034), paired permutation, n=10. DPM is additionally 7-15x faster at binding budgets, making one LLM call at decision time instead of N. A determinism study of 10 replays per case at temperature zero shows both architectures inherit residual API-level nondeterminism, but the asymmetry is structural: DPM exposes one nondeterministic call; summarization exposes N compounding calls. The audit surface follows the same one-versus-N pattern: DPM logs two LLM calls per decision while summarization logs 83-97 on LongHorizon-Bench. We conclude with TAMS, a practitioner heuristic for architecture selection, and a failure analysis of stateful memory under enterprise operating conditions. The contribution is the argument that statelessness is the load-bearing property explaining enterprise's preference for weaker but replayable retrieval pipelines, and that DPM demonstrates this property is attainable without the decisioning penalty retrieval pays.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决一个核心矛盾：尽管学术界已提出众多复杂的状态化记忆架构（如分层整合、图记忆等），但在受监管的企业级长程决策代理（如核保、理赔裁决、税务审查）的实际部署中，简单但性能较弱的检索增强生成（RAG）管道却占据主导地位。研究背景是，企业级AI系统在受监管领域部署时，不仅需要决策准确性，还必须满足一系列关键的系统属性：决策过程需支持确定性重放（以便复现和验证）、提供可审计的推理轨迹、确保多租户数据隔离，以及具备无状态性以实现水平扩展。现有复杂的状态化记忆架构在设计中通常会违反这些属性（例如，共享可变状态会阻碍重放和扩展），而RAG因其架构简单，反而能天然满足这些要求，但代价是决策能力较弱。

因此，本文要解决的核心问题是：能否设计一种记忆架构，既能像RAG一样满足企业级部署所需的确定性、可审计性、隔离性和无状态性等系统属性，又能避免RAG在决策质量上的损失，甚至达到或超越现有状态化记忆架构（如基于摘要的记忆）的决策性能？为此，论文提出了确定性投影记忆（DPM），其核心思想是将交互轨迹视为仅追加的不可变事件日志，在决策时仅执行一次任务条件投影（在零温度下进行结构化信息提取），从而在保证上述系统属性的同时，评估其是否会在决策质量上做出妥协。

### Q2: 有哪些相关研究？

本文的相关研究可分为以下几类：

**1. 状态记忆架构方法类**：包括MemGPT（采用操作系统风格的分层管理内存）、HyMem（划分检索与摘要寻址内存）、H-MEM（多级摘要树）、GAM（图结构存储与遍历）、TiMem（时序层次记忆）、MIRIX（多智能体记忆协调）、MEM1（记忆与推理协同训练）以及A-Mem（智能体记忆操作符）。这些工作均属于**状态性（stateful）架构**，其内部记忆表示随任务轨迹演进，决策时状态依赖于历史更新路径。本文提出的DPM（确定性投影记忆）在架构理念上与之正交：它**摒弃了运行时可变状态**，采用仅追加的事件日志加决策时一次性投影的**无状态（stateless）设计**，虽在表达能力上较弱（不支持智能体在轨迹中编辑自身记忆），但旨在满足企业部署所需的系统属性。

**2. 检索增强生成（RAG）与应用类**：源自REALM等工作，专注于通过检索外部知识库来增强生成模型。以往研究多关注检索质量、幻觉减少和延迟等问题。本文则强调RAG的**无状态架构特性**（不可变文档索引、纯查询函数）是其被企业采纳的关键驱动力。DPM继承了RAG的无状态、纯投影等核心架构属性，但通过事件日志+投影的模式，旨在弥补RAG在决策质量上的不足。

**3. 事件溯源与系统模式类**：DPM的“日志+投影”结构直接借鉴了分布式系统中的**事件溯源（event sourcing）模式**，该模式以不可变追加日志为权威状态，所有衍生视图均为纯投影。这一模式已是受监管金融系统的工程基础。本文的贡献在于将这一模式应用于智能体记忆，以解决状态记忆的决策质量优势与检索架构的企业可部署性之间的张力。

**4. 智能体记忆评测类**：包括MemoryAgentBench、LoCoMo、LongMemEval、AMA-Bench等基准，主要评估记忆召回率和任务成功率。本文指出，这些工作均未涵盖企业部署关心的**运行属性**，如确定性重放、可审计性、多租户安全性和共享状态下的可扩展性。

**5. 企业可信AI需求类**：行业报告反复强调可审计溯源、决策确定性重建、跨租户安全和水平扩展的无状态性等需求。本文将此类需求操作化为可评估的架构轴线。

**本文与相关工作的核心区别**在于：它并非追求更强大的记忆表达能力，而是论证**无状态性**是解释企业偏好较弱但可重放检索流程的关键负载属性，并证明DPM能在不牺牲决策质量的前提下实现这一属性，从而弥合了状态记忆与检索管道在企业部署中的鸿沟。

### Q3: 论文如何解决这个问题？

论文通过提出确定性投影记忆（DPM）架构来解决企业级AI智能体在受监管领域部署时面临的核心挑战，即如何在满足确定性重放、可审计性、多租户隔离和无状态水平扩展这四项关键系统属性的同时，不牺牲决策性能。

其核心方法基于一个极其简洁的两组件设计：首先是一个**仅追加的不可变事件日志**，按顺序记录所有原始事件（如文档块、工具输出、用户消息），作为轨迹的唯一持久化表示，绝不进行编辑或摘要。其次是一个**任务条件化投影函数**，仅在决策时刻被调用一次。该函数以完整事件日志、任务描述和内存预算作为输入，通过一次温度设置为零的大语言模型调用，生成一个结构化的、预算约束的内存视图。该视图严格分为**事实**（可验证的锚点，如金额、日期）、**推理**（简短的推断链）和**合规注释**（相关监管条款）三个部分，并要求模型为每个主张引用事件索引，对数字锚点进行逐字保留。

整体框架的创新点在于其彻底的“无状态”和“按需投影”哲学。与传统的状态化记忆架构（在轨迹中持续维护和更新记忆状态）不同，DPM在轨迹运行期间完全不维护记忆对象，所有记忆操作延迟到决策时刻一次性完成。这种设计带来了多重优势：1）**确定性重放**：由于决策输出仅依赖于事件日志、任务和预算这三个明确输入以及一次LLM调用，只要后端确定，重放即可实现字节级一致，将重放面从传统架构的N次调用减少到1次。2）**最小化审计面**：每个决策仅对应两次LLM调用（一次投影生成记忆视图，一次基于该视图的最终决策），审计日志清晰简单。3）**结构化的多租户隔离**：每个任务的事件日志是投影函数的显式参数，不存在跨租户的共享内存状态。4）**高效性**：在内存预算紧张时，DPM通过单次调用完成信息压缩，相比基于摘要的、需要多次调用进行渐进压缩的方法，速度提升7-15倍，并且在高压缩比下能显著提升事实精确度和推理连贯性。

因此，DPM的本质是通过架构设计，将企业所需的负载属性（特别是无状态性）内化，用一次确定性的、结构化的投影操作，替代了传统状态化记忆中复杂的、具有累积不确定性的多步记忆操作，从而在满足严苛部署要求的同时，避免了检索增强管道通常带来的决策性能损失。

### Q4: 论文做了哪些实验？

论文在受监管的企业决策场景下，对提出的确定性投影记忆（DPM）与基于增量摘要的记忆架构（Summ-only）进行了头对头对比实验。

**实验设置与数据集**：实验使用LongHorizon-Bench（LHB）基准测试，包含两个受监管的决策领域（抵押贷款资格审核和保险理赔裁决），共10个案例（各5个）。每个案例轨迹规模约为26,000-28,000字符，包含82-96个离散事件。评估围绕四个决策对齐轴心：事实精确度（FRP）、推理连贯性（RCS）、决策准确性（EDA）和合规性重建（CRR）。

**对比方法与预算**：主要对比两种架构：作为状态化基线的“Summ-only”（增量摘要）和“DPM”（仅决策时进行一次投影）。实验在三个内存预算（即压缩比）下进行：紧张（20倍压缩，1,338字符）、中等（5倍压缩，5,352字符）和宽松（2倍压缩，13,381字符）。

**主要结果与关键指标**：在紧张预算（20倍压缩）下，DPM相比Summ-only基线取得显著优势：事实精确度提升+0.52（Cohen‘s h=1.17， p=0.0014），推理连贯性提升+0.53（h=1.13， p=0.0034）。DPM在绑定预算时速度提升7-15倍，因其在决策时仅需1次LLM调用，而Summ-only需要N次。确定性研究发现，两种架构都存在API层面的残余非确定性，但DPM仅暴露1次非确定性调用，而Summ-only暴露N次复合调用。审计追踪方面，DPM每个决策仅记录2次LLM调用，而Summ-only在LHB基准上记录83-97次。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从以下几个层面深入探索。首先，在技术层面，DPM虽将非确定性调用从N次降为1次，但未根本解决底层API的残差非确定性问题；未来需研究在自托管模型或更严格推理后端上实现字节级确定性重放。其次，当前投影算子受上下文窗口限制，需设计分层投影架构以支持超长轨迹（如百万级token），但这可能重新引入非确定性与审计复杂性，需权衡设计。再者，论文实证基于特定领域（贷款、理赔）和模型（Claude Haiku），未来需验证TAMS启发式方法在更长时程、对抗性环境或不同模型族中的泛化能力。此外，论文仅对比了摘要式记忆，未来可探索DPM与更复杂状态架构（如动态检索、模式锚定）在多样化企业场景下的性能边界。最后，从系统视角，可研究如何将DPM的无状态性与水平扩展、多租户隔离深度整合，并开发自动化工具来量化审计表面与合规成本，推动其在强监管领域的落地。

### Q6: 总结一下论文的主要内容

论文针对企业AI智能体在受监管领域（如核保、理赔裁定、税务审查）部署时，长期偏好使用检索增强流水线而非更先进的有状态记忆架构的现象，提出了核心问题：这是由于企业部署负载依赖于确定性重放、可审计推理、多租户隔离和无状态水平扩展这四个系统属性，而有状态架构本质上违背了这些要求。为此，论文提出了确定性投影记忆（DPM）方法，它由一个仅追加的事件日志和在决策时进行一次任务条件投影构成。实验表明，在三种记忆预算下对十个受监管决策案例进行评估，DPM在宽松预算下与基于摘要的记忆方法性能相当，但在预算受限时显著优于后者：在20倍压缩比下，DPM将事实精确度提升了0.52，推理连贯性提升了0.53。同时，DPM在受限预算下的决策速度快7-15倍，仅需一次大语言模型调用而非N次。确定性研究表明，两种架构都残留API层面的非确定性，但DPM仅暴露一次非确定性调用，而摘要方法则暴露N次复合调用，审计开销同样呈现“一 versus N”的模式。论文最终提出了TAMS架构选择启发式方法，并分析了有状态记忆在企业运营条件下的失败原因。其核心贡献在于论证了无状态性是解释企业偏好可重放检索流水线的关键负载属性，并且DPM证明了无需像检索那样付出决策性能代价即可实现这一属性。
