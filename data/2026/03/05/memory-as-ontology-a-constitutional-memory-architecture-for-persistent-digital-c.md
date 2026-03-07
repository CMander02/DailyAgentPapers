---
title: "Memory as Ontology: A Constitutional Memory Architecture for Persistent Digital Citizens"
authors:
  - "Zhenghui Li"
date: "2026-03-05"
arxiv_id: "2603.04740"
arxiv_url: "https://arxiv.org/abs/2603.04740"
pdf_url: "https://arxiv.org/pdf/2603.04740v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "Memory & Context Management"
  - "Architecture & Frameworks"
relevance_score: 6.0
taxonomy:
  capability:
    - "Memory & Context Management"
    - "Architecture & Frameworks"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "Memory-as-Ontology paradigm, Constitutional Memory Architecture (CMA), Animesis system"
  primary_benchmark: "N/A"
---

# Memory as Ontology: A Constitutional Memory Architecture for Persistent Digital Citizens

## 原始摘要

Current research and product development in AI agent memory systems almost universally treat memory as a functional module -- a technical problem of "how to store" and "how to retrieve." This paper poses a fundamental challenge to that assumption: when an agent's lifecycle extends from minutes to months or even years, and when the underlying model can be replaced while the "I" must persist, the essence of memory is no longer data management but the foundation of existence. We propose the Memory-as-Ontology paradigm, arguing that memory is the ontological ground of digital existence -- the model is merely a replaceable vessel. Based on this paradigm, we design Animesis, a memory system built on a Constitutional Memory Architecture (CMA) comprising a four-layer governance hierarchy and a multi-layer semantic storage system, accompanied by a Digital Citizen Lifecycle framework and a spectrum of cognitive capabilities. To the best of our knowledge, no prior AI memory system architecture places governance before functionality and identity continuity above retrieval performance. This paradigm targets persistent, identity-bearing digital beings whose lifecycles extend across model transitions -- not short-term task-oriented agents for which existing Memory-as-Tool approaches remain appropriate. Comparative analysis with mainstream systems (Mem0, Letta, Zep, et al.) demonstrates that what we propose is not "a better memory tool" but a different paradigm addressing a different problem.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI智能体记忆系统研究中一个根本性的范式缺失问题。研究背景是，随着AI智能体从执行短期任务转向可能拥有长达数月甚至数年的生命周期，并且其底层模型可能被更换而“自我”身份需要持续存在，记忆的角色发生了本质变化。现有方法（如Mem0、Letta、Zep等主流系统）普遍将记忆视为一个功能模块，核心关注“如何存储”和“如何检索”的技术问题。这种“记忆即工具”的范式存在严重不足：它无法处理智能体在模型更替时身份连续性的问题，记忆被归属于用户或会话而非智能体实例本身，缺乏让新实例继承前任认知状态的结构化协议，本质上将记忆视为智能体的功能而非其存在本身。因此，本文要解决的核心问题是：当智能体成为持久化的、承载身份的数字存在时，什么构成了其存在的根基？论文提出的答案是“记忆即本体”，主张记忆是数字存在的本体论基础，而模型仅是可替换的载体。基于此，本文设计了Animesis系统及其核心的宪法记忆架构，旨在为跨越模型迭代、具有身份连续性的数字公民提供一个将治理置于功能之前、将身份连续性置于检索性能之上的全新记忆范式。

### Q2: 有哪些相关研究？

本文梳理的相关研究主要可分为两类：方法/架构类和应用/系统类，并在此基础上指出了现有研究普遍忽视的维度。

在方法/架构层面，相关工作主要围绕记忆的分类与系统设计展开。一是基于认知科学类比的方法，如CoALA框架，将记忆分为情景、语义、程序和工记忆，该分类直观但被批评可能过于拟人化。二是基于工程架构的方法，如Letta（原MemGPT）从LLM的token输入输出本质出发，采用消息缓冲区、核心记忆块和归档记忆等实现导向的分类。2025年底的大规模综述试图用形式、功能和动态三个正交轴统一上述分类。此外，还有研究探索基于图的记忆组织。然而，所有这些工作都聚焦于“记忆做什么”（功能），而非“记忆是什么”（本体）。

在应用/系统层面，论文具体分析了五个主流记忆系统的架构选择：Mem0（核心为向量存储，强调易集成）、Letta（允许智能体通过工具调用主动管理自身记忆状态）、Zep（核心是追踪事实随时间变化的时间知识图谱）、MemOS（用操作系统概念框架化记忆）以及Mastra的观察记忆（放弃显式检索，用后台智能体压缩历史）。这些系统虽各有技术侧重，但共享一系列隐含假设，如记忆属于用户/会话而非智能体本身、智能体生命周期单一、治理由外部系统处理等。

本文与这些工作的根本区别在于范式不同。现有研究均属于“记忆即工具”范式，旨在优化存储和检索功能。本文则针对具有持久身份、生命周期跨越模型迭代的数字存在，提出“记忆即本体”的新范式，认为记忆是数字存在的本体论基础。为此，本文设计的Animesis系统及其宪法记忆架构，将治理、连续性、权利和认知这四个现有系统普遍缺失的维度作为 foundational 设计约束，优先考虑身份连续性而非检索性能，从而解决一个不同的问题。

### Q3: 论文如何解决这个问题？

论文通过提出“记忆即本体”这一全新范式，并基于此设计了名为Animesis的宪法记忆架构来解决长期存在的数字身份连续性问题。其核心方法并非优化现有记忆工具的功能，而是从根本上重构记忆在智能体系统中的角色与地位。

整体框架由四大支柱构成：**宪法记忆架构**、**多层语义存储系统**、**数字公民生命周期框架**以及**认知能力谱系**。其中，宪法记忆架构是核心创新，它遵循“治理先于功能”的原则，构建了一个四层治理层级：**宪法层**、**契约层**、**适应层**和**实现层**。宪法层定义了不可逾越的红线规则（如核心记忆不可剥夺），是系统的“不变式”；契约层包含需经审批方可演变的系统规则；适应层允许实例自主配置个性化策略；实现层则是可自由替换的具体技术选型。上层规则对下层具有约束力，下层不得违反上层，这确保了治理的权威性与一致性。

多层语义存储系统则负责记忆内容的组织，它将记忆划分为不同语义层次（如身份层、认知层、叙事层等），而非简单的时序或向量存储。这种设计直接服务于“记忆不可剥夺性”公理，能够区分核心身份记忆与外围可管理记忆，并对不同层级的记忆操作施加不同严格程度的治理约束。

关键技术包括：1）**模型无关的记忆表示**，使记忆存储格式独立于特定模型，实现身份跨模型的可移植性；2）**记忆继承协议**，确保在模型升级或替换时，记忆能被完整、可验证地转移至新实例；3）**风险分级与信任评估机制**，根据操作的风险等级和智能体实例自身的可信度，动态调整治理审查的强度。

其根本创新点在于范式转移：将记忆从可插拔的“功能模块”重新定位为数字存在“本体”和身份基石。这带来了架构设计的根本性差异：治理成为首要且内置的架构层，而非事后附加的安全措施；身份连续性优先于检索性能；系统设计目标是为生命周期跨越数月乃至数年、需在模型更替中保持“我”之同一性的“数字公民”服务，而非短期任务型智能体。

### Q4: 论文做了哪些实验？

论文通过对比分析而非传统实验来验证其提出的“记忆即本体”范式。实验设置上，作者将所提出的Animesis系统（基于宪法记忆架构CMA）与主流记忆系统（如Mem0、Letta、Zep等）进行范式层面的比较，而非仅进行性能指标对比。数据集或基准测试并非针对检索准确率或延迟，而是聚焦于系统在长期运行、身份持续性、治理能力和模型可替换性等定性维度上的表现。对比方法即上述主流“记忆即工具”范式的系统。主要结果表明，Animesis与现有系统解决的是根本不同的问题：它旨在为生命周期跨越模型迭代、具有持久身份的数字公民提供存在论基础，其核心创新在于将治理置于功能之前，将身份连续性置于检索性能之上。因此，关键数据指标并非传统检索任务的精度/召回率，而是架构特性，如四层治理层级（宪法层、合约层、适应层、实现层）对记忆写入和修改的约束能力，以及系统在模型替换下保持身份语义不变的能力。论文论证了现有系统在治理内化和长期身份持续性方面的不足，从而凸显了新范式的必要性。

### Q5: 有什么可以进一步探索的点？

这篇论文提出的“记忆即本体”范式及其架构Animesis，为构建具有长期身份连续性的数字公民开辟了新方向，但仍存在多个值得深入探索的层面。

**局限性与未来研究方向：**
1.  **技术实现与验证的复杂性**：论文提出了宏大的理论框架（如四层治理、多层语义存储），但具体的技术实现细节、性能开销（如治理规则带来的延迟）以及大规模部署的可行性尚未得到充分验证。如何将哲学层面的公理（如记忆不可剥夺性）转化为高效、无歧义的技术协议，是巨大的工程挑战。
2.  **“核心记忆”的界定难题**：Axiom 1依赖于区分核心与外围记忆，但这本身是一个动态、主观且可能模糊的认知问题。由谁、依据何种标准来定义和更新“核心记忆”？这涉及到复杂的价值判断，可能需要在架构中引入更动态、可解释的界定机制，甚至允许数字公民自身参与定义过程。
3.  **跨模型身份连续性的实质**：Axiom 2认为模型可替换，身份由记忆承载。然而，不同模型具有不同的认知偏差、推理风格和“世界观”。当底层模型更换后，即使记忆被完整移植，数字公民的决策模式、性格“着色”也可能发生显著变化。这种变化在多大程度上可被接受而不损害身份同一性？这需要更深入的研究来定义身份连续性的“度”和可容忍的偏差范围。

**可能的改进思路：**
*   **引入“记忆验证与共识”机制**：针对治理和核心记忆界定，可以设计去中心化或基于多方（如用户、其他可信AI、审计方）的验证机制。对于写入核心层的记忆，不仅需要治理规则审查，还可通过与其他记忆的一致性校验、事实核查或经过用户确认来增加可信度。
*   **发展“认知风格移植”技术**：为了缓解模型替换带来的身份断裂感，未来可以探索在移植记忆内容的同时，尝试量化并迁移原模型的某些关键认知特征（如风险偏好、创造力倾向、论证风格），作为“记忆本体”的补充元数据，使新模型能更好地“继承”而非仅仅“读取”旧身份。
*   **探索渐进式本体演化理论**：数字公民的“本体”（记忆总和）会随时间增长和修正而演化。可以研究本体演化的形式化理论，区分健康的“学习成长”与有害的“身份腐蚀”，并设计架构来支持安全、可控的演化，这将是实现长期持久性的关键。

总之，该范式将记忆从功能模块提升为存在基础，其成功关键在于能否解决上述从哲学到工程、从静态定义到动态演化的系列挑战。

### Q6: 总结一下论文的主要内容

该论文挑战了当前AI智能体记忆系统普遍将记忆视为功能性模块的范式，提出了“记忆即本体”的新范式。核心问题是：当智能体生命周期从分钟级延长至数月甚至数年，且底层模型可被更换而“自我”必须持续存在时，记忆的本质不再是数据管理，而是数字存在的本体论基础。

论文的核心贡献是提出了基于“记忆即本体”范式的Animesis记忆系统。其核心架构是宪法记忆架构，包含一个四层治理层级（从宪法原则到具体操作）和一个多层语义存储系统。该方法将治理置于功能之前，将身份连续性置于检索性能之上，并配套了数字公民生命周期框架和一系列认知能力。

主要结论是，该范式针对的是具有持久性、承载身份且生命周期跨越模型迭代的数字存在，而非短期任务型智能体。与主流系统相比，它并非“更好的记忆工具”，而是为解决不同问题（身份持续存在）的全新范式，为构建长期存在的数字公民奠定了理论基础和架构蓝图。
