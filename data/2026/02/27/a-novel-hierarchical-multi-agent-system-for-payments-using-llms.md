---
title: "A Novel Hierarchical Multi-Agent System for Payments Using LLMs"
authors:
  - "Joon Kiat Chua"
  - "Donghao Huang"
  - "Zhaoxia Wang"
date: "2026-02-27"
arxiv_id: "2602.24068"
arxiv_url: "https://arxiv.org/abs/2602.24068"
pdf_url: "https://arxiv.org/pdf/2602.24068v1"
categories:
  - "cs.MA"
  - "cs.CL"
tags:
  - "Multi-Agent Systems"
  - "Tool Use & API Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Tool Use & API Interaction"
  domain: "Finance & Trading"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "Hierarchical Multi-Agent System for Payments (HMASP)"
  primary_benchmark: "N/A"
---

# A Novel Hierarchical Multi-Agent System for Payments Using LLMs

## 原始摘要

Large language model (LLM) agents, such as OpenAI's Operator and Claude's Computer Use, can automate workflows but unable to handle payment tasks. Existing agentic solutions have gained significant attention; however, even the latest approaches face challenges in implementing end-to-end agentic payment workflows. To address this gap, this research proposes the Hierarchical Multi-Agent System for Payments (HMASP), which provides an end-to-end agentic method for completing payment workflows. The proposed HMASP leverages either open-weight or proprietary LLMs and employs a modular architecture consisting of the Conversational Payment Agent (CPA - first agent level), Supervisor agents (second agent level), Routing agents (third agent level), and the Process summary agent (fourth agent level). The CPA serves as the central entry point, handling all external requests and coordinating subsequent tasks across hierarchical levels. HMASP incorporates architectural patterns that enable modular task execution across agents and levels for payment operations, including shared state variables, decoupled message states, and structured handoff protocols that facilitate coordination across agents and workflows. Experimental results demonstrate the feasibility of the proposed HMASP. To our knowledge, HMASP is the first LLM-based multi-agent system to implement end-to-end agentic payment workflows. This work lays a foundation for extending agentic capabilities into the payment domain.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决一个具体且未被充分探索的问题：如何利用基于大语言模型（LLM）的多智能体系统（MAS）实现端到端的、由智能体驱动的支付工作流。当前，像OpenAI的Operator或Anthropic的Claude Computer Use这样的LLM智能体虽然能自动化许多工作流，但无法处理实际的支付任务。现有的研究要么停留在支付网络的边界（例如，作为虚拟助手导航支付应用），要么面临传统支付基础设施（如反机器人机制、多因素认证、PCI DSS合规要求）和LLM自身幻觉风险带来的集成挑战。因此，该领域缺乏一个能够协调多个LLM智能体、安全可靠地完成从用户请求到最终支付确认全过程的参考框架。本文提出的HMASP（用于支付的层次化多智能体系统）正是为了填补这一空白，其核心研究问题是：能否设计一个框架，让外部LLM智能体能够以最小的集成开销，使用自然语言进行对话并完成支付？

### Q2: 有哪些相关研究？

相关研究主要分为两个方向：LLM驱动的多智能体系统（MAS）和LLM在支付领域的应用。在LLM驱动的MAS方面，已有大量研究探索了多智能体协作的结构与策略，例如基于角色的协议（如MetaGPT），将智能体组织成具有特定专长的角色以提升协作性能。同时，研究也指出LLM幻觉和系统设计缺陷是导致智能体工作流不可靠的关键原因，强调了架构设计对可靠性的重要性。在支付领域应用方面，已有工作利用LLM作为虚拟助手帮助用户操作支付应用（如LLMPA用于支付宝），或利用LLM增强支付交易中的欺诈检测。然而，这些现有方案均未实现端到端的支付处理，它们要么不涉及实际的支付网络交互，要么仅作为辅助工具停留在支付流程的边界。本文的HMASP正是在这些研究基础上，首次将基于角色的多智能体架构思想应用于支付这一特定、高要求的领域，并引入了专门的架构模式来应对支付场景下的安全、确定性和集成挑战，从而实现了从对话到支付执行的全流程自动化。

### Q3: 论文如何解决这个问题？

论文提出了一个名为HMASP（Hierarchical Multi-Agent System for Payments）的层次化、模块化多智能体框架。其核心解决方案包括以下几个关键部分：
1. **层次化角色架构**：系统定义了四个层级的智能体角色：
   - **对话支付智能体（CPA）**：第一层，作为中央入口点，处理所有外部请求并进行初始协调。
   - **监督者智能体**：第二层，作为决策者和协调者，管理特定领域（如支付、卡片）的工作流。
   - **路由智能体**：第三层，位于每个具体任务工作流中，决定是否触发该工作流。
   - **过程总结智能体**：第四层，生成任务结果的总结报告并向上传递。
   这种层级结构实现了任务的模块化分解与分布式执行。
2. **状态与信息处理机制**：
   - **基于角色的状态**：定义了不同的状态（如PayAgentState, CardsState, PaymentState），每个智能体和模块只能访问其被分配的状态，确保信息隔离。同时，通过共享状态变量（如用户ID）在需要时传递必要信息。
   - **解耦的消息状态**：每个智能体拥有独立的、基于角色的消息状态，只能解释与其角色相关的消息，减少了不必要的令牌消耗和信息暴露风险。
3. **结构化交接协议**：利用LangGraph框架实现智能体之间的结构化交接，使请求能够沿着层级被无缝传递到正确的处理节点。
4. **确保可靠执行的确定性设计**：
   - **中断（人在回路）机制**：在需要收集敏感信息（如卡号）时，触发中断暂停工作流，等待用户输入并进行验证（如Luhn校验），验证通过后才恢复执行。
   - **状态变量用于确定性**：关键的用户输入和工作流输出被存储在状态变量中，后续步骤直接从变量中读取，而非依赖LLM生成或传递，从而将支付处理与生成过程解耦，避免了幻觉风险，确保了信息的确定性和持久性。
5. **支付工作流子图**：具体的支付功能模块（如授权3DS）被封装在独立的LangGraph子图中，由路由智能体调用，实现了敏感操作的安全隔离。

### Q4: 论文做了哪些实验？

论文在一个模拟环境中对HMASP进行了可行性验证实验，主要评估任务成功率和智能体交接可靠性。
**实验设置**：
- **数据集**：使用了由Mastercard提供的包含1000个数据点的专有数据集，涵盖四个任务类别：卡片注册相关输入（T1）、卡片检索相关输入（T2）、支付处理相关输入（T3）以及与支付无关的输入（T4）。每个类别250个样本。
- **模型**：评估了多款开源模型（包括Qwen系列、Mistral系列、Llama系列）与专有模型GPT-4.1（作为基线）。所有HMASP中的智能体使用同一模型。开源模型在配备NVIDIA H100 GPU的本地环境中运行。
- **模拟环境**：支付模块通过函数模拟，以体现智能体层与底层支付API的架构解耦。
**评估指标**：
1. **任务成功率**：衡量运行中（i）触发正确工作流且（ii）正确保存或检索所需信息的比例。对于无关输入（T4），成功意味着未触发任何工作流。
2. **智能体交接F1分数**：通过比较实际交接与预期交接来评估。对于相关输入（T1-T3），评估从CPA到监督者、以及从监督者到相关工作流的交接。对于无关输入（T4），预期是CPA直接拒绝请求而不触发监督者，评估CPA层面的决策。
**主要结果**：
- **任务成功率**：GPT-4.1表现最佳（T1-T3接近100%，T4为100%）。在开源模型中，Qwen2.5:32b表现相对最好，在所有任务上成功率≥95.6%。其他模型表现不一，例如Llama3.1:8b在相关任务上成功率很低（≤10.4%），但所有模型基本都能正确拒绝无关输入（T4成功率接近100%）。
- **智能体交接F1分数**：GPT-4.1平均F1分数达99.9%，Qwen2.5:32b达到98.9%。Llama3.1模型在拒绝无关输入（T4）时表现较差，其CPA经常将请求交接给监督者而非直接拒绝。
- **新颖性分析**：通过对比表格指出，HMASP是首个支持完整端到端支付处理的基于LLM的多智能体系统。

### Q5: 有什么可以进一步探索的点？

论文指出了几个未来可以深入探索的方向：
1. **数据集扩展与复杂性**：当前用于验证的研究数据集规模较小（1000个数据点），可能无法完全捕捉真实世界中所有支付工作流的复杂性和用户行为的多样性。未来工作可以使用更大、更复杂的数据集进行测试，以评估HMASP的鲁棒性和泛化能力。
2. **安全性与合规性深化**：实现智能体支付是一个涉及多领域的复杂问题。未来研究需要专注于开发针对智能体支付的、以支付为中心的安全护栏（guardrails），并探索如何在状态变量中安全地令牌化（tokenize）敏感信息，以进一步满足PCI DSS等合规要求。
3. **架构与协议比较研究**：可以对不同的智能体架构（如非层次化、联邦式）和智能体间协作协议（如不同的通信或协商机制）在支付处理场景下的效果进行系统的比较研究，以找到更优的设计模式。
4. **模型异构性与优化**：当前实验中所有智能体使用同一LLM。未来可以探索不同层级的智能体使用不同规模或专长的模型（异构模型），以在性能和成本之间取得平衡。此外，也可以研究针对支付领域进行模型微调或提示工程优化的效果。
5. **真实环境集成与延迟评估**：当前实验在模拟环境中进行。未来的重要步骤是将HMASP与真实的支付网关和认证系统集成，并评估在生产环境复杂因素（如发卡行认证、PCI-DSS验证）下的实际性能、延迟和可靠性。

### Q6: 总结一下论文的主要内容

本文提出了一种新颖的、基于大语言模型的层次化多智能体系统（HMASP），首次实现了端到端的、由智能体驱动的支付工作流。针对现有LLM智能体无法处理实际支付任务、且缺乏相关参考框架的现状，HMASP通过一个包含对话支付智能体（CPA）、监督者、路由智能体和过程总结智能体的四层模块化架构，将支付任务分解并协调执行。其核心创新在于引入了一系列确保安全性、可靠性和确定性的架构模式：基于角色的状态管理实现信息隔离与必要共享；解耦的消息状态减少信息暴露；结构化交接协议实现流程协调；以及关键的中断（人在回路）机制和利用状态变量存储确定性信息来有效缓解LLM幻觉风险。实验在模拟环境中使用专有数据集验证了HMASP的可行性，结果表明，使用合适的开源模型（如Qwen2.5:32b）可以达到与GPT-4.1相媲美的性能。这项工作为将智能体能力扩展到高要求、高安全性的支付领域奠定了重要的基础，并指明了未来在数据集、安全护栏和架构比较等方面的研究方向。
