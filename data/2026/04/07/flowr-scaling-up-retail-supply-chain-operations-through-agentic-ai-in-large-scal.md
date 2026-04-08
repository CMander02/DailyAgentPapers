---
title: "Flowr -- Scaling Up Retail Supply Chain Operations Through Agentic AI in Large Scale Supermarket Chains"
authors:
  - "Eranga Bandara"
  - "Ross Gore"
  - "Sachin Shetty"
  - "Piumi Siyambalapitiya"
  - "Sachini Rajapakse"
  - "Isurunima Kularathna"
  - "Pramoda Karunarathna"
  - "Ravi Mukkamala"
  - "Peter Foytik"
  - "Safdar H. Bouk"
  - "Abdul Rahman"
  - "Xueping Liang"
  - "Amin Hass"
  - "Tharaka Hewa"
  - "Ng Wee Keong"
  - "Kasun De Zoysa"
  - "Aruna Withanage"
  - "Nilaan Loganathan"
date: "2026-04-07"
arxiv_id: "2604.05987"
arxiv_url: "https://arxiv.org/abs/2604.05987"
pdf_url: "https://arxiv.org/pdf/2604.05987v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent System"
  - "Supply Chain Automation"
  - "Human-in-the-Loop"
  - "Workflow Decomposition"
  - "Domain-Specialized LLM"
  - "Enterprise AI"
relevance_score: 7.5
---

# Flowr -- Scaling Up Retail Supply Chain Operations Through Agentic AI in Large Scale Supermarket Chains

## 原始摘要

Retail supply chain operations in supermarket chains involve continuous, high-volume manual workflows spanning demand forecasting, procurement, supplier coordination, and inventory replenishment, processes that are repetitive, decision-intensive, and difficult to scale without significant human effort. Despite growing investment in data analytics, the decision-making and coordination layers of these workflows remain predominantly manual, reactive, and fragmented across outlets, distribution centers, and supplier networks. This paper introduces Flowr, a novel agentic AI framework for automating end-to-end retail supply chain workflows in large-scale supermarket operations. Flowr systematically decomposes manual supply chain operations into specialized AI agents, each responsible for a clearly defined cognitive role, enabling automation of processes previously dependent on continuous human coordination. To ensure task accuracy and adherence to responsible AI principles, the framework employs a consortium of fine-tuned, domain-specialized large language models coordinated by a central reasoning LLM. Central to the framework is a human-in-the-loop orchestration model in which supply chain managers supervise and intervene across workflow stages via a Model Context Protocol (MCP)-enabled interface, preserving accountability and organizational control. Evaluation demonstrates that Flowr significantly reduces manual coordination overhead, improves demand-supply alignment, and enables proactive exception handling at a scale unachievable through manual processes. The framework was validated in collaboration with a large-scale supermarket chain and is domain-independent, offering a generalizable blueprint for agentic AI-driven supply chain automation across large-scale enterprise settings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型连锁超市零售供应链运营中，决策与协调层高度依赖人工、效率低下且难以规模化的问题。研究背景是，尽管企业在数据分析和ERP系统上投入巨大，但供应链工作流（包括需求预测、采购、供应商协调和库存补货）的核心决策与跨部门协调仍主要依靠人工完成。这些流程具有重复性、时效性强、数据源异构等特点，导致现有方法存在明显不足：当前的零售AI应用多为孤立的点解决方案（如需求预测模型），它们虽能优化特定指标，却无法实现从需求感知到供应商确认的端到端工作流自动化，且缺乏将复杂流程分解为智能体可执行任务、并保持有效人类监督的 principled 框架。

因此，本文要解决的核心问题是：如何设计一个可信、可扩展的智能体AI框架，以自动化大型超市运营中端到端的零售供应链工作流，同时确保任务准确性、可解释性并维持必要的人类监督。论文提出的Flowr框架通过以下方式应对这一挑战：系统地将人工操作分解为承担特定认知角色的专用AI智能体；采用由中央推理LLM协调的、经过微调的领域专用LLM联盟来保证决策质量；并引入基于模型上下文协议（MCP）的人机协同编排模型，使供应链经理能在关键节点进行监督和干预，从而在提升自动化规模的同时，保持问责制和组织控制力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 供应链自动化与优化方法**：传统研究多集中于利用运筹学、统计模型（如时间序列预测）和规则引擎来优化供应链的特定环节（如库存管理、需求预测）。这些方法通常是确定性的、基于规则的，难以处理非结构化信息（如供应商沟通文本）和复杂的多环节协调。本文提出的Flowr框架则利用LLM的灵活推理能力，处理非结构化输入并进行多步骤决策，实现了从“工具辅助”到“工作流自动化”的范式转变。

**2. 基于大语言模型（LLM）的智能体（Agent）系统**：近期研究探索了将LLM作为核心推理引擎来构建自主智能体，以完成复杂任务（如AutoGPT、MetaGPT）。这些工作为多智能体协作提供了基础。本文的Flowr框架在此基础上，**专门针对零售供应链这一特定领域**，系统地设计了具有明确认知角色的专用智能体（如库存监控、供应商协调），并创新性地采用**由中央推理LLM协调的微调领域专家LLM联盟架构**，以提高任务准确性和决策可靠性。

**3. 人机协同与负责任AI（Responsible AI）**：在关键任务领域，确保AI系统的可解释性、可控性和人类监督至关重要。相关研究提出了可解释AI（XAI）技术和人在回路（Human-in-the-loop）范式。Flowr框架将这一理念深度融入其设计：通过**模型上下文协议（MCP）接口**实现人类对工作流各阶段的监督与干预，并要求智能体输出结构化推理轨迹，从而在提升自动化水平的同时，保持了组织的问责制和控制力。

**4. 领域适应与模型微调技术**：为了提高LLM在专业领域的表现，广泛采用监督微调（SFT）、低秩自适应（LoRA）等技术。本文应用了类似的参数高效微调流程（如QLoRA），但其独特之处在于构建了**专门针对零售供应链的精选数据集**进行微调，并强调在资源受限环境中的本地化部署，以满足企业运营对延迟和数据隔离的要求。

综上，Flowr框架并非孤立存在，它是对上述多个研究方向在**大规模零售供应链运营**这一具体、复杂场景下的综合集成与创新应用，其核心贡献在于提出了一套可泛化的、以智能体AI驱动、并严格嵌入人类监督的端到端工作流自动化蓝图。

### Q3: 论文如何解决这个问题？

论文通过设计并实现一个名为Flowr的智能体AI框架，来解决零售供应链中人工流程繁琐、难以规模化的问题。其核心方法是将端到端的手动供应链操作系统地分解为由多个专门化AI智能体协同执行的自动化工作流，并引入人机协同的监督机制确保责任与可控性。

**整体框架与主要模块**：Flowr框架将传统零售补货生命周期分解为六个专门化的AI智能体，每个智能体负责一个明确的认知角色，并通过模型上下文协议（MCP）服务器连接外部数据源和系统。这些智能体包括：
1.  **需求预测智能体**：持续分析销售数据、季节性需求等，使用微调的大语言模型（LLM）生成细粒度的SKU级需求预测。
2.  **库存监控智能体**：实时监控各门店和配送中心的库存水平，与需求预测对比，主动识别缺货或过剩风险。
3.  **采购与订单智能体**：基于库存信号和需求预测，计算最优订单量，并考虑供应商交货期、价格等因素生成采购订单草案。
4.  **供应商协调智能体**：管理与供应商网络的所有通信，包括订单传输、确认交货时间，并跟踪响应。
5.  **配送中心补货计划智能体**：根据确认的供应商交货计划和各门店库存，生成优化的库存分配和物流调度计划。
6.  **异常与警报智能体**：持续监控整个工作流，主动检测并上报需人工干预的异常情况（如交货延迟、需求激增）。

这些智能体通过结构化输出传递信息，共享工作流状态，从而实现跨全生命周期的协同推理，而非孤立执行任务。

**关键技术架构与创新点**：
1.  **基于LLM联盟的负责任AI决策架构**：这是Flowr的核心技术创新。每个操作智能体在执行任务（如生成订单、规划补货）时，其提示会被分发至多个经过微调、领域专门化的LLM（如Llama-3, Mistral等）。这些LLM从不同角度（如需求推理、物流优化）产生独立的推理输出。随后，一个中央推理LLM（如GPT-OSS）负责评估、比较并综合这些输出，形成最终的一致决策。这种机制通过多视角验证，降低了偏见和错误传播的风险，确保了决策的可靠性和可解释性。
2.  **人机协同编排模型**：框架通过MCP支持的统一自然语言界面，让供应链经理作为“人类编排者”在工作流的关键节点（如审核预测、批准订单、处理异常）进行监督和干预。这实现了自动化执行与人类监督的分离，在提升规模效率的同时，保留了人类在关键决策点的权威控制，确保了问责制和组织可控性。
3.  **模块化与可扩展的智能体设计**：每个智能体作为独立的工作流模块，可以单独优化、重新训练或扩展，而无需重新设计整个系统。这种模块化设计使系统能够灵活适应不断变化的业务需求、供应商网络或门店扩张。

综上所述，Flowr通过将手动流程分解为专门化智能体网络、采用LLM联盟确保负责任决策、并嵌入人机协同监督，成功地将一个依赖密集人工协调、顺序执行的流程，转变为一个可规模化、持续运行且受人类监督的自动化智能体系统。

### Q4: 论文做了哪些实验？

论文在真实的大规模超市链环境中进行了实验验证。实验设置方面，研究团队与一家大型超市连锁企业合作，将Flowr框架部署到其实际的零售供应链运营中，自动化从需求预测、采购、供应商协调到库存补货的端到端工作流。实验没有使用公开的基准数据集，而是基于该超市链的真实业务数据流和运营流程进行评估。

对比方法主要是传统的人工主导流程。主要结果和关键数据指标显示，Flowr框架显著减少了人工协调开销，具体量化指标未在摘要中给出，但指出其改善了供需匹配的准确性，并实现了在人工流程中无法达到的规模下进行主动的异常处理。这表明系统在提升操作效率和决策前瞻性方面效果显著。实验还验证了其人类在环的编排模型和基于模型上下文协议（MCP）的界面的有效性，确保了责任归属和组织控制。

### Q5: 有什么可以进一步探索的点？

该论文提出的Flowr框架在自动化零售供应链方面取得了显著进展，但其探索仍存在局限和可深化的方向。首先，框架高度依赖LLM的协调与决策，在极端或对抗性场景（如突发性供应链中断、数据恶意污染）下的鲁棒性和安全性未充分验证，未来需研究更具韧性的多智能体共识与回退机制。其次，当前的人机协同虽通过MCP接口实现监督，但干预节点可能滞后，可探索实时自适应调控，例如引入强化学习让智能体动态学习管理者的偏好与风险阈值。此外，框架的“领域无关”宣称需更多跨行业验证（如冷链、快时尚等对时效和损耗敏感的场景），其中智能体的专业化分工与知识迁移机制值得细化。最后，从成本效益角度，多个微调领域LLM的部署与维护开销较大，未来可研究轻量化模型或混合架构（如小型模型处理常规任务，大型模型仅处理异常），以提升大规模落地的经济可行性。

### Q6: 总结一下论文的主要内容

该论文提出了一个名为Flowr的新型智能体AI框架，旨在自动化大型超市连锁店中的端到端零售供应链工作流程。核心问题是解决传统零售供应链运营中依赖大量人工、反应式且碎片化的决策与协调层，这些流程难以规模化且效率低下。

Flowr的方法是将复杂的手工供应链操作系统地分解为多个专门的AI智能体，每个智能体承担明确的认知角色（如需求预测、库存监控、采购协调等）。这些智能体通过一个中心推理大语言模型协调的、经过微调的领域专用LLM联盟来驱动，以确保任务准确性和负责任AI原则。框架的关键是采用了人在回路的编排模型，供应链经理可通过基于模型上下文协议的接口进行监督和干预，从而保持问责制和组织控制。

主要结论是，Flowr在实际大型超市环境中的验证表明，它能显著减少人工协调开销，改善供需匹配，并实现主动的异常处理，其规模是人工流程无法达到的。该框架提供了可推广的蓝图，展示了智能体AI如何将人类角色从手动执行转向监督与战略决策，从而实现高效、可扩展且可信的供应链自动化。
