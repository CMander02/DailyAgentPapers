---
title: "TopoPilot: Reliable Conversational Workflow Automation for Topological Data Analysis and Visualization"
authors:
  - "Nathaniel Gorski"
  - "Shusen Liu"
  - "Bei Wang"
date: "2026-03-26"
arxiv_id: "2603.25063"
arxiv_url: "https://arxiv.org/abs/2603.25063"
pdf_url: "https://arxiv.org/pdf/2603.25063v1"
categories:
  - "cs.HC"
  - "cs.AI"
  - "cs.GR"
  - "cs.LG"
tags:
  - "Agent Architecture"
  - "Workflow Automation"
  - "Scientific Agent"
  - "Tool Use"
  - "Reliability & Verification"
  - "Multi-Agent System"
  - "Human-AI Interaction"
relevance_score: 7.5
---

# TopoPilot: Reliable Conversational Workflow Automation for Topological Data Analysis and Visualization

## 原始摘要

Recent agentic systems demonstrate that large language models can generate scientific visualizations from natural language. However, reliability remains a major limitation: systems may execute invalid operations, introduce subtle but consequential errors, or fail to request missing information when inputs are underspecified. These issues are amplified in real-world workflows, which often exceed the complexity of standard benchmarks. Ensuring reliability in autonomous visualization pipelines therefore remains an open challenge. We present TopoPilot, a reliable and extensible agentic framework for automating complex scientific visualization workflows. TopoPilot incorporates systematic guardrails and verification mechanisms to ensure reliable operation. While we focus on topological data analysis and visualization as a primary use case, the framework is designed to generalize across visualization domains. TopoPilot adopts a reliability-centered two-agent architecture. An orchestrator agent translates user prompts into workflows composed of atomic backend actions, while a verifier agent evaluates these workflows prior to execution, enforcing structural validity and semantic consistency. This separation of interpretation and verification reduces code-generation errors and enforces correctness guarantees. A modular architecture further improves robustness by isolating components and enabling seamless integration of new descriptors and domain-specific workflows without modifying the core system. To systematically address reliability, we introduce a taxonomy of failure modes and implement targeted safeguards for each class. In evaluations simulating 1,000 multi-turn conversations across 100 prompts, including adversarial and infeasible requests, TopoPilot achieves a success rate exceeding 99%, compared to under 50% for baselines without comprehensive guardrails and checks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的智能体系统在自动化复杂科学可视化工作流（特别是拓扑数据分析和可视化）中存在的可靠性不足问题。研究背景是，当前如VizGenie、ChatVis等智能体系统已能根据自然语言生成科学可视化，降低了使用门槛，但它们在真实复杂工作流中面临严峻的可靠性挑战。现有方法的不足主要体现在：1）大语言模型的随机性可能导致系统执行无效操作或看似有效但语义错误的操作，产生误导性结果；2）现有系统多关注简单任务（如表面渲染），难以可靠处理涉及多阶段预处理、特征提取和工具协调的复杂工作流；3）对于像拓扑分析这类本身复杂、流程严谨的领域，现有智能体系统缺乏针对性设计，容易在代码生成、参数选择和工作流编排上出错，且难以验证和约束。本文要解决的核心问题是：如何构建一个可靠、可扩展的智能体框架，以自然语言交互的方式自动化执行复杂的科学可视化工作流（以拓扑分析为典型用例），通过系统性的保障和验证机制，显著降低错误率，确保工作流的结构有效性和语义一致性，从而将领域科学家从繁琐的技术细节中解放出来。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. AI驱动的可视化生成系统**：许多研究利用LLM（如ChatGPT）直接生成可视化代码（如Matplotlib、Vega-Lite脚本），或构建多智能体框架来生成和优化可视化。例如，ChatVis和VizGenie采用多智能体与RAG或视觉反馈来生成并迭代修正ParaView等脚本；AVA、NLI4VolVis等则专注于特定科学可视化任务（如体绘制）。这些系统虽灵活，但普遍依赖代码生成，易产生语法或语义错误，且对模糊提示的处理不足（常自行推断而非请求澄清）。本文的TopoPilot避免直接生成代码，转而通过编排原子化后端操作来构建工作流，并引入验证机制，从而提升可靠性。

**2. 可靠性提升方法**：在通用AI领域，已有大量研究致力于减少LLM的幻觉和提升推理准确性。但在智能体系统中，针对多步工作流错误的系统性研究较少。一些工作通过将任务分解为树或图结构（类似本文的节点树表示）来提升可靠性，或通过动态知识注入、形式化方法约束工具调用来改善准确性。本文的独特之处在于采用极简的双智能体架构（编排器与验证器分离），并对原子操作进行确定性执行，从而在降低协调复杂性的同时确保正确性。

**3. 科学可视化与拓扑数据分析专用工具**：在科学可视化领域，T2TF、FlowNL等系统设计了针对特定任务（如传递函数设计、流场可视化）的自然语言接口与领域专用语法。这些工具虽在各自领域有效，但难以泛化到复杂的多步骤分析工作流。相比之下，TopoPilot以后端模块化和可扩展性为核心，支持跨领域的复杂工作流自动化，并针对拓扑数据分析（如临界点、等高线树等描述符的应用）进行了重点优化。

**4. 可靠性评估实践**：现有智能体可视化系统大多缺乏严格的可靠性评估。仅少数（如VizGenie、ChatVis）报告了故障率，但测试规模小（数十次），且未涵盖多轮对话或不可行请求等真实场景。本文则通过大规模模拟（1000次多轮对话）和对抗性测试，系统性评估了多种故障模式下的表现，证明了其高成功率（>99%）。

**本文与相关工作的核心区别**在于：TopoPilot通过“编排-验证”分离的架构、模块化后端、原子化操作执行以及针对故障模式的系统性防护机制，实现了对复杂科学可视化工作流的高可靠自动化，弥补了现有系统在可靠性、可扩展性和对模糊/复杂场景处理能力上的不足。

### Q3: 论文如何解决这个问题？

论文通过一个以可靠性为中心的双智能体架构和模块化设计来解决自主可视化工作流中的可靠性问题。其核心方法是分离“工作流规划”与“验证”职责，并引入系统化的防护机制和类型检查。

**整体框架与主要模块：**
系统采用双智能体架构：
1.  **编排器智能体**：作为主智能体，负责与用户对话，将自然语言提示转化为由原子化后端操作组成的工作流。这些操作对应一个称为“节点树”的内部数据结构中的节点。
2.  **验证器智能体**：在编排器准备执行可视化前，对提议的工作流进行独立验证。它接收完整的聊天历史和用于重建节点树的Python代码，通过回答一系列预设的是/否问题来评估工作流的结构有效性和语义一致性。只有验证通过，工作流才会被执行。

**关键技术组件与创新点：**
1.  **模块化节点树与类型系统**：所有计算和可视化操作都被封装为独立的、可复用的“节点”类，并组织成树形结构（节点树）。每个节点声明其输入和输出数据类型，系统内置类型系统在节点连接时强制执行类型兼容性检查，从根本上防止语义无效的工作流组合（如将向量场操作误用于标量场）。
2.  **原子化工具与防护机制**：后端功能通过一系列定义明确的“工具”暴露给LLM，每个工具对应一个原子操作（如计算关键点）。关键创新在于为这些工具自动或定制化地附加“防护机制”。防护机制通过三种方式确保可靠性：在工具描述中明确要求特定行为（如必须先询问用户是否应用持久性简化）；在工具调用参数中强制要求智能体确认已执行该行为；并由验证器最终检查防护机制是否被满足。这有效防止了参数缺失、无效参数值等错误。
3.  **系统化的失效模式应对**：论文提出并针对性缓解了六类失效模式，体现了其可靠性设计的系统性：
    *   **澄清失败**：通过防护机制阻止创建节点，直到从用户处获得必要信息。
    *   **能力混淆**：在全局提示中明确列出系统能力边界，指示编排器拒绝不可行请求。
    *   **无效参数化**：节点创建时进行参数验证，并为每个参数提供合理的默认值，防护机制强制使用默认值除非用户明确覆盖。
    *   **无效工作流**：通过上述类型系统和嵌入类型可视化规则来防止。
    *   **目标错位**：依赖验证器的反馈，并通过防护机制强制实施符合用户真实意图的工作流结构（例如，确保“应用持久性简化并计算关键点”被执行为对简化后的场进行计算）。
    *   **错误执行**：节点树的执行是完全确定性的，其正确性依赖于正确构建的节点树和后端实现的正确性。

**总结**：TopoPilot 的创新在于将可靠性内置于架构核心，通过职责分离（编排与验证）、强约束（类型系统、防护机制）以及对已知失效模式的系统性缓解，构建了一个可扩展且高可靠（评估中成功率超99%）的科学可视化工作流自动化框架。其模块化设计使得无需修改核心系统即可集成新的描述符和领域特定工作流。

### Q4: 论文做了哪些实验？

论文通过案例研究和系统评估进行实验。实验设置方面，TopoPilot采用模块化架构，包含编排器（Orchestrator）和验证器（Verifier）双智能体，前者将用户提示转换为原子后端操作组成的工作流，后者在执行前评估工作流的结构有效性和语义一致性。数据集/基准测试主要基于拓扑数据分析和可视化任务，涉及标量、矢量和张量场数据，具体包括飓风伊莎贝尔（Hurricane Isabel）风速数据集等，用于演示持久图计算与简化等工作流。对比方法为缺乏全面防护和检查的基线系统。主要结果：在模拟100个提示下的1000轮多轮对话评估中（包含对抗性和不可行请求），TopoPilot的成功率超过99%，而基线系统的成功率低于50%。关键数据指标包括：成功率（TopoPilot >99%，基线 <50%），验证了其防护机制对可靠性的显著提升。

### Q5: 有什么可以进一步探索的点？

基于论文信息，未来可进一步探索的点包括：1）**数据与格式扩展**：目前系统主要支持VTK格式，未来可扩展至更多科学数据格式（如HDF5、NetCDF），并增强对非结构化或流式数据的处理能力。2）**动态工作流优化**：当前节点树参数不可变，限制了交互式调整的灵活性；可探索增量计算或参数动态更新机制，以支持实时工作流迭代。3）**多模态与领域泛化**：系统虽设计为可泛化，但验证机制仍依赖特定领域规则；需研究跨可视化领域的通用验证框架，并整合多模态输入（如草图、图表）以提升自然语言交互的鲁棒性。4）**错误恢复与解释性**：现有验证代理仅提供布尔反馈，未来可增强其解释能力，生成可操作的修复建议，并设计从错误中自主学习的机制。5）**分布式与高性能计算**：对于大规模时变数据，可探索节点树的分布式执行与缓存策略，以提升计算效率。这些方向将推动自主可视化系统向更灵活、可靠和通用的方向发展。

### Q6: 总结一下论文的主要内容

本文针对当前基于大语言模型的智能体系统在生成科学可视化工作流时存在的可靠性不足问题，提出了TopoPilot框架。其核心贡献是设计了一个以可靠性为中心的双智能体架构，用于自动化复杂的科学可视化流程，并以拓扑数据分析和可视化作为主要用例。

问题在于现有系统在执行复杂、开放领域的真实工作流时，容易产生无效操作、细微错误或无法处理信息缺失的输入。为解决此问题，TopoPilot采用了一个编排器智能体将用户指令解析为由原子后端操作组成的工作流，并由一个独立的验证器智能体在执行前评估工作流的结构有效性与语义一致性。这种解释与验证的分离降低了代码生成错误。此外，其模块化架构隔离了组件，便于无缝集成新的描述符和领域特定工作流。

主要结论是，通过引入故障模式的分类法并为每类实施针对性保障，TopoPilot在包含对抗性和不可行请求的评估中，成功率达到99%以上，显著优于缺乏全面保障的基线系统（低于50%）。该框架的意义在于为构建可靠、可扩展的自动化科学可视化管道提供了系统性的解决方案。
