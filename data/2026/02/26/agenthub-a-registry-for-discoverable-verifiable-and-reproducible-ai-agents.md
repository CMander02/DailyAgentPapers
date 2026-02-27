---
title: "AgentHub: A Registry for Discoverable, Verifiable, and Reproducible AI Agents"
authors:
  - "Erik Pautsch"
  - "Tanmay Singla"
  - "Parv Kumar"
  - "Wenxin Jiang"
  - "Huiyun Peng"
  - "Behnaz Hassanshahi"
  - "Konstantin Läufer"
  - "George K. Thiruvathukal"
  - "James C. Davis"
date: "2025-10-03"
arxiv_id: "2510.03495"
arxiv_url: "https://arxiv.org/abs/2510.03495"
pdf_url: "https://arxiv.org/pdf/2510.03495v2"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent Registry"
  - "Agent Discovery"
  - "Agent Governance"
  - "Agent Ecosystem"
  - "Agent Sharing"
  - "Agent Evaluation"
  - "Agent Infrastructure"
  - "LLM-as-Judge"
relevance_score: 8.0
---

# AgentHub: A Registry for Discoverable, Verifiable, and Reproducible AI Agents

## 原始摘要

LLM-based agents are rapidly proliferating, yet the infrastructure for discovering, evaluating, and governing them remains fragmented compared to mature ecosystems like software package registries (e.g., npm) and model hubs (e.g., Hugging Face). Existing efforts typically address naming, distribution, or protocol descriptors, but stop short of providing a registry layer that makes agents discoverable, comparable, and governable under automated reuse. We present AgentHub, a registry layer and accompanying research agenda for agent sharing that targets discovery and workflow integration, trust and security, openness and governance, ecosystem interoperability, lifecycle transparency, and capability clarity with evidence. We describe a reference prototype that implements a canonical manifest with publish-time validation, version-bound evidence records linked to auditable artifacts, and an append-only lifecycle event log whose states are respected by default in search and resolution. We also provide initial discovery results using an LLM-as-judge recommendation pipeline, showing how structured contracts and evidence improve intent-accurate retrieval beyond keyword-driven discovery. AgentHub aims to provide a common substrate for building reliable, reusable agent ecosystems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体（Agent）在快速发展和广泛应用过程中，其共享、发现和重用基础设施严重不足的问题。研究背景是，LLM智能体正迅速进入从科学发现到软件工程等各类工作流，它们具有自主性、动态组合工具、持续演进和规模化运行等特点，这与静态的软件包或预训练模型有本质区别。然而，现有的基础设施生态是碎片化的：成熟的软件包注册中心（如npm、PyPI）和模型中心（如Hugging Face）虽然提供了结构化元数据、依赖管理和来源追溯等宝贵经验，但并未针对智能体的动态、自治和持续演化特性进行设计；而新兴的智能体协议（如MCP、ANS）主要关注连接性和命名，缺乏一个统一的注册层来支持自动化的发现、比较和治理。

现有方法的不足在于，它们要么缺少标准化的能力描述和验证证据，使得智能体难以被机器自动发现和可靠集成；要么缺乏对智能体全生命周期（如状态、更新、撤销）的透明管理；同时，跨协议的互操作性以及默认的安全与治理保障也普遍缺失。这限制了智能体的研究进展和实际应用中的可靠复用。

因此，本文要解决的核心问题是：如何构建一个名为AgentHub的注册层，为智能体共享提供一个可发现、可验证、可复现且可治理的公共基础。它致力于通过规范化的清单、版本绑定的证据记录、仅追加的生命周期事件日志等机制，使智能体具备机器可检查的能力契约和证据，实现生命周期可见性、跨协议互操作性，并内置安全与治理保障，从而支持自动化、可靠的重用，推动形成健壮、可复用的智能体生态系统。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**软件与模型注册表**、**代理专用协议与目录**以及**商业应用市场**。

在**软件与模型注册表**方面，编程语言包注册表（如npm、PyPI）提供了结构化元数据、依赖图管理和签名验证等成熟经验，但主要面向静态代码。模型中心（如Hugging Face）通过模型卡分享AI模型，但其依赖声明不规范，不利于自动化复现。本文的AgentHub借鉴了前两者的元数据结构和信任机制，但针对智能体动态、可交互的特性，提出了更严格的模式化能力声明、版本绑定证据和全生命周期事件日志，旨在实现超越代码包和静态模型的**可发现、可验证、可复现**的智能体管理。

在**代理专用协议与目录**方面，相关研究如Agent Name Service (ANS) 提供了类似DNS的命名与发现服务，Agent Capability Negotiation and Binding Protocol (ACNBP) 关注安全的能力协商，NANDA Index 则构建了去中心化的能力验证索引。这些工作为智能体间的互操作提供了基础协议，但主要解决命名、发现或双边协商问题。本文认为，这些能力对于注册表用例是必要的，但**并不充分**。AgentHub旨在构建一个更高层次的**注册表层**，整合并超越这些协议，提供全面的搜索、比较、治理和工作流集成支持。

在**商业应用市场**方面，如ChatGPT插件商店或Alexa技能商店，展示了在政策约束下构建可信生态系统的可能性。它们通常依赖人工审核和中心化治理。AgentHub吸收了其通过声誉信号（如使用统计、审计）建立信任的思路，但更强调通过**机器可读的标准化合约和自动化验证**来实现开放性与安全性的平衡，并支持“智能体制造智能体”等更复杂的自动化复用场景。

### Q3: 论文如何解决这个问题？

论文通过提出并实现一个名为AgentHub的注册表层来解决AI Agent的发现、验证和可复现性问题。其核心方法是构建一个集中式的注册中心，为Agent提供结构化的元数据、可验证的证据以及透明的生命周期管理，以支持自动化、跨协议的可重用性。

整体框架上，AgentHub是一个注册表层，而非运行时环境。它包含发布、索引、搜索、解析、验证和演化等核心操作。系统设计强调**可变元数据与不可变工件**的分离：Agent条目以版本化快照形式存储，其核心清单（manifest）通过内容哈希进行不可变存储，而注册表维护可变的元数据（如索引、生命周期状态、证据摘要）。

主要模块与关键技术包括：
1.  **规范化清单（Canonical Manifest）**：这是系统的核心交付物。清单定义了支持自动化和可复现性所需的最小字段集，包括：稳定标识符、声明的能力与I/O模式、协议绑定、运行时权限与前提条件、SBOM风格的依赖引用、显式的生命周期状态以及证据策略。清单在发布时经过严格模式验证、确定性规范化，并存储为不可变的数据块。这种设计遵循了“一种模式，多种方言”的原则，在保持稳定核心的同时，允许协议特定的描述符存储在扩展空间中。
2.  **证据记录（Evidence Records）**：为解决能力声明可信度问题，系统定义了与特定Agent版本绑定的证据记录。每条记录包含：产生证据的方法/配方、输入、作为不可变工件的输出哈希以及可选的第三方证明。证据被不可变地存储和引用，使第三方能够复现或独立重新运行检查，从而将发现信号从单纯依赖流行度转向结构化、可验证的证据。
3.  **生命周期事件日志（Lifecycle Event Log）**：生命周期被建模为一个**仅追加的事件日志**，而非单一的可变标志。Agent版本在明确的状态（如活跃、弃用、退役、撤销）间迁移，每次状态转换都附带时间戳和理由记录。注册表的默认行为（如搜索和解析）必须尊重这些状态，确保过时或不安全的条目不会被默认返回，这对于自动化重用环境下的安全治理和快速撤销至关重要。
4.  **互操作性适配器（Interoperability Adapters）**：为支持跨协议操作，系统通过声明式适配器将原生协议描述符（如MCP工具描述符、A2A Agent卡片）映射到核心清单并反向转换。这确保了语义在不同协议间转换时不丢失，并通过往返一致性测试进行验证。
5.  **以证据为导向的发现机制（Evidence-Forward Discovery）**：发现被实现为注册表的核心关注点。它提供对清单字段和证据信号的编程式搜索，以及将稳定标识符和版本范围解析为具体版本和协议端点的接口。排名机制旨在优先考虑证据，根据结构化元数据的相关性、证据覆盖范围与新鲜度、生命周期状态和兼容性约束来返回候选者，从而直接应对“关键词搜索和流行度偏见”的挑战。

创新点在于：将成熟的软件/模型注册表设计原则系统性地应用于AI Agent领域；提出了一个结合不可变清单、版本绑定证据和仅追加生命周期日志的完整注册表模型；强调发现机制与自动化工作流（如规划、编排）的深度集成，使Agent自身也能成为注册表的程序化用户；通过结构化合约和证据提升意图匹配的检索精度，超越了传统的关键词驱动发现。

### Q4: 论文做了哪些实验？

论文进行了初步评估实验，重点测试了AgentHub在智能体发现方面的效果。实验设置了一个两阶段推荐流程：第一阶段基于文本检索从注册的智能体卡片中筛选候选，第二阶段通过结构化访谈验证智能体的实际能力。评估使用了八个基于A2A的智能体作为实时服务器，并故意将它们组织成四对能力重叠但各有侧重的组合，以模拟实际发现中的模糊场景。数据集包含24个半模糊的自然语言查询，每个查询对应多个可能处理的智能体，但仅有一个被指定为最佳匹配（基于领域专家标注的真实标签）。

对比方法包括三种检索策略：词法检索（BM25）、语义嵌入检索以及混合方法。主要结果以Precision@1、Recall@3和延迟时间为关键指标。仅使用检索时，混合方法表现最佳（Precision@1为83.33%，Recall@3为95.83%，延迟0.57秒）。而完整的两阶段流程（混合检索加访谈）在保持高Recall@3（98.61% ± 1.97%）的同时，延迟显著增加至101.30秒 ± 7.25秒，表明访谈阶段主要用于生成证据而非单纯提升排名。实验证实结构化合约和证据能提高意图准确的检索效果，超越仅依赖关键词的发现方式。

### Q5: 有什么可以进一步探索的点？

本文提出的AgentHub系统在构建可发现、可验证、可复现的智能体注册表方面迈出了重要一步，但其仍存在一些局限性，并为进一步探索提供了多个方向。

首先，当前评估主要基于小规模精选数据集，未来需扩展到大规模、异构的智能体生态中进行验证，以检验系统的可扩展性和通用性。其次，论文虽强调了证据记录和审计追踪，但对于智能体在动态环境中的行为安全性、对抗性攻击的鲁棒性，以及多智能体协作时可能出现的涌现风险，尚未建立系统的治理框架。此外，现有“LLM-as-judge”的推荐机制可能受模型偏见影响，需探索更客观、可量化的评估指标。

可能的改进思路包括：1）引入形式化验证或运行时监控技术，增强智能体的可信保证；2）设计去中心化的声誉机制，让社区参与智能体的质量评估；3）开发跨平台的标准接口，以支持不同框架智能体的无缝集成。这些方向将有助于推动智能体生态系统向更开放、可靠的方向发展。

### Q6: 总结一下论文的主要内容

该论文提出了AgentHub，一个面向AI Agent的注册中心，旨在解决当前AI Agent生态中基础设施碎片化的问题。核心问题是现有平台缺乏一个统一的注册层，使得Agent难以被发现、验证、比较、复用和治理。

论文的核心贡献是设计了一个注册层架构及研究议程，其方法基于一个规范的清单（manifest）实现。该清单支持发布时验证，并链接到可审计的版本化证据记录；同时采用仅追加的生命周期事件日志，确保状态可追溯，并默认影响搜索和解析过程。此外，论文还展示了一个基于LLM作为评判员的推荐流程，证明结构化的合约和证据能比单纯的关键词检索更准确地匹配用户意图。

主要结论是，AgentHub通过提供可发现、可验证、可复现的共享机制，为构建可靠、可互操作、可治理的Agent生态系统奠定了共同基础，其设计强调了工作流集成、信任安全、开放治理和生命周期透明度等关键维度。
