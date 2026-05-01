---
title: "Heterogeneous Scientific Foundation Model Collaboration"
authors:
  - "Zihao Li"
  - "Jiaru Zou"
  - "Feihao Fang"
  - "Xuying Ning"
  - "Mengting Ai"
  - "Tianxin Wei"
  - "Sirui Chen"
  - "Xiyuan Yang"
  - "Jingrui He"
date: "2026-04-30"
arxiv_id: "2604.27351"
arxiv_url: "https://arxiv.org/abs/2604.27351"
pdf_url: "https://arxiv.org/pdf/2604.27351v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "LLM Agent"
  - "Multi-Agent System"
  - "Scientific Foundation Model"
  - "Heterogeneous Agent"
  - "Reasoning Interface"
  - "Task Orchestration"
  - "Domain-Specific Agent"
relevance_score: 8.5
---

# Heterogeneous Scientific Foundation Model Collaboration

## 原始摘要

Agentic large language model systems have demonstrated strong capabilities. However, their reliance on language as the universal interface fundamentally limits their applicability to many real-world problems, especially in scientific domains where domain-specific foundation models have been developed to address specialized tasks beyond natural language. In this work, we introduce Eywa, a heterogeneous agentic framework designed to extend language-centric systems to a broader class of scientific foundation models. The key idea of Eywa is to augment domain-specific foundation models with a language-model-based reasoning interface, enabling language models to guide inference over non-linguistic data modalities. This design allows predictive foundation models, which are typically optimized for specialized data and tasks, to participate in higher-level reasoning and decision-making processes within agentic systems. Eywa can serve as a drop-in replacement for a single-agent pipeline (EywaAgent) or be integrated into existing multi-agent systems by replacing traditional agents with specialized agents (EywaMAS). We further investigate a planning-based orchestration framework in which a planner dynamically coordinates traditional agents and Eywa agents to solve complex tasks across heterogeneous data modalities (EywaOrchestra). We evaluate Eywa across a diverse set of scientific domains spanning physical, life, and social sciences. Experimental results demonstrate that Eywa improves performance on tasks involving structured and domain-specific data, while reducing reliance on language-based reasoning through effective collaboration with specialized foundation models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前大语言模型（LLM）驱动的智能体系统在处理科学领域任务时面临的根本性局限。研究背景是，基于LLM的智能体系统虽然在感知、规划、推理和决策方面表现出强大能力，但其核心依赖“自然语言”作为通用接口。然而，在科学任务中（如物理、生命、社会科学），数据往往是符号公式、结构化时间序列等非语言模态的专门化数据。现有方法的不足在于：一方面，单纯用自然语言描述这些专门数据会丢失关键信息，成为性能瓶颈；另一方面，虽然针对特定科学领域已涌现许多专用的基础模型（如预测模型），但这些模型通常不具备自然语言接口，无法直接融入以语言为中心的智能体协作系统。因此，本文要解决的核心问题是：**如何让异构的科学基础模型（非语言模态专家）与语言智能体有效协作，参与更高层次的推理和决策过程**。为此，论文提出了Eywa框架，通过为领域专用模型构建一个基于语言模型的推理接口（类似“Tsaheylu神经连接”），使其能以模态原生（而非完全翻译成语言）的方式与LLM智能体协作，从而克服语言接口的瓶颈，并提升科学任务处理的性能与效率。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：**语言智能体系统**、**科学基础模型**和**多智能体协作框架**。

1. **语言智能体系统**：这是当前的研究热点（如ReAct、AutoGPT、OpenAI Agents），它们通过大语言模型（LLM）进行通用推理，但受限于语言作为唯一接口。本文指出，这类方法无法有效处理科学领域的非语言模态数据（如分子结构、基因序列）。本文的Eywa框架通过为领域专用模型附加语言接口，将传统语言智能体扩展到科学领域，是对此类系统的直接扩展。

2. **科学基础模型**：针对特定科学领域（如蛋白质结构预测的AlphaFold、气候模拟的FourCastNet）的预训练模型。现有方法通常独立使用这些模型，缺乏与语言模型的协作。本文的关键区别在于，Eywa并非替代或重复训练这些模型，而是将其作为“工具”集成到智能体系统中，使它们能在高层次推理中被语言模型直接调用。

3. **多智能体系统（MAS）**：已有研究（如ChatDev、MetaGPT）探索了多智能体协作。本文的EywaMAS和EywaOrchestra借鉴了此类拓扑结构，但核心创新在于引入了异构智能体——即部分智能体基于LLM，部分基于领域FM。通过规划器动态协调，使不同模态的智能体（语言型与预测型）能够协同解决复杂科学任务，这与传统同构MAS有本质区别。

此外，本文还在物理、生命和社会科学的多领域进行了系统评测，提供了跨学科验证，这区别于多数仅在单一领域评估的工作。

### Q3: 论文如何解决这个问题？

Eywa通过设计异构科学基础模型协作框架来解决传统语言智能体在科学领域处理非语言数据模态时的局限性。核心是引入Eywa异构智能体框架，包含三个层次：

首先，EywaAgent作为基础构建块，通过"Tsaheylu"双向通信接口将语言模型（LLM）与领域专用基础模型（FM）耦合。接口包含查询编译器φ_k（将任务状态转为结构化FM调用）和响应适配器ψ_k（将专业输出转为语言可理解的表示），形成"任务→LLM推理→φ_k→FM执行→ψ_k→LLM合成→输出"的流水线。通过模型上下文协议（MCP）实例化，FM作为远程服务暴露，控制策略C动态决定是否调用FM，实现通用推理与专业计算的灵活切换。

其次，EywaMAS扩展为多智能体系统，支持异构智能体（LLM智能体/EywaAgent）的即插即用组合，保持原有通信拓扑，通过并行专业化和跨域协作提升性能。

最后，EywaOrchestra引入动态编排机制，由"指挥者"（大语言模型实现）根据输入任务自适应选择：智能体角色类型、语言模型骨干、附加的领域FM、以及多智能体通信拓扑，从固定配置池中动态实例化异构系统。

创新点在于：（1）通过双向接口实现语言空间与专业计算空间的贯通；（2）证明EywaAgent在领域优势假设下严格优于纯语言智能体；（3）实现任务自适应的系统级动态编排，突破固定多智能体架构的性能上限。

### Q4: 论文做了哪些实验？

论文构建了Eywabench基准测试，涵盖物理、生命和社会科学三大领域，每个领域包含三个子领域（如材料、能量、空间等），任务涉及自然语言、时间序列和表格数据。实验对比了三大类方法：单智能体基线（GPT、Gemini、Claude等LLM）、同质LLM多智能体基线（Refine、Debate）、异质LLM多智能体基线（MoA、X-MAS）。提出的方法包括EywaAgent（单智能体）、EywaMAS（多智能体）和EywaOrchestra（动态编排）。主要结果：(a) EywaAgent相比单LLM基线，平均效用提升6.6%（从0.6154到0.6558），token消耗减少约30%（从4469到3137）；(b) EywaMAS在总体效用上达到最优（0.6761），超越Refine（0.6294）和Debate（0.6460）；(c) 异质LLM多智能体方法（如MoA为0.6273）未显著超越同质基线，表明跨模态异质性更关键；(d) 部分领域（如经济）单智能体已足够，复杂多智能体并非必要；(e) EywaOrchestra在无需专家配置下达到接近EywaMAS的效用（0.6746），且延迟和token消耗显著低于固定多智能体系统（如时间从72.11秒降低至48.16秒）。此外还进行了温度、提示设计的消融实验，验证了方法的鲁棒性。

### Q5: 有什么可以进一步探索的点？

论文在架构设计和实验评估上有亮点，但仍存在几个值得深入探索的局限。首先，当前仅集成了时序和表格两种非语言模态的基础模型，未来可扩展至更多科学领域专用模型，如蛋白质折叠、分子动力学或地球观测模型，以提升跨模态泛化能力。其次，动态编排器（Orchestra）的规划策略较为简单，未来可引入强化学习或元学习来自适应选择最优代理组合与参数，避免所有样本采用固定拓扑导致次优解。第三，实验仅评测了GPT系列语言模型，但不同科学任务可能更适合不同基座LLM，未来可研究语言模型与专业模型的最优配对策略。此外，当前统一效用函数可能掩盖细粒度任务差异，建议设计任务感知的损失函数或置信度校准机制。最后，可探索可解释性接口，让专业模型不仅输出结果，还能提供推理依据，增强人机协作信任度。

### Q6: 总结一下论文的主要内容

该论文提出了一个名为Eywa的异构科学基础模型协作框架，旨在解决大型语言模型（LLM）在处理非语言数据模态（如时间序列、表格数据）时能力受限的问题。核心思想是为领域特定的基础模型（如Chronos、TabPFN）配备一个基于语言模型的推理接口（称为“Tsaheylu”），使语言模型能够引导这些专业模型进行推理和决策。Eywa框架包含三种实现：EywaAgent（单一智能体集成）、EywaMAS（多智能体扩展）和EywaOrchestra（基于规划的动态编排）。在涵盖物理、生命和社会科学的EywaBench基准上，实验结果表明，Eywa不仅显著提升了处理结构化、领域特定数据任务的性能（平均效用提升约7%），还通过将计算委托给专业模型，减少了约30%的token消耗和约10%的执行时间。该工作的主要意义在于，它开创性地打通了语言智能与专业科学模型之间的协作通道，为构建能够处理复杂科学问题的异构智能体系统提供了有效范式。
