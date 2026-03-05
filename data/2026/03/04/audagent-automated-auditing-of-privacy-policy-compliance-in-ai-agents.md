---
title: "AudAgent: Automated Auditing of Privacy Policy Compliance in AI Agents"
authors:
  - "Ye Zheng"
  - "Yimin Chen"
  - "Yidan Hu"
date: "2025-11-03"
arxiv_id: "2511.07441"
arxiv_url: "https://arxiv.org/abs/2511.07441"
pdf_url: "https://arxiv.org/pdf/2511.07441v5"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent 安全"
  - "Agent 评测/基准"
  - "工具使用"
  - "隐私合规"
  - "运行时监控"
relevance_score: 7.5
---

# AudAgent: Automated Auditing of Privacy Policy Compliance in AI Agents

## 原始摘要

AI agents can autonomously perform tasks and, often without explicit user consent, collect or disclose users' sensitive local data, which raises serious privacy concerns. Although AI agents' privacy policies describe their intended data practices, there remains limited transparency and accountability about whether runtime behavior matches those policies. To bridge this gap, we present AudAgent, a tool that continuously monitors AI agents' data practices in real time and guards compliance with their stated privacy policies.
  AudAgent comprises four components for automated privacy auditing of AI agents. (i) Policy formalization: a novel cross-LLM voting mechanism that ensures high-confidence parsing of privacy policies into formal models. (ii) Runtime annotation: a lightweight Presidio-based analyzer that detects sensitive data and annotates data practices based on the AI agent's context and the formalized privacy policy model. (iii) Compliance auditing: ontology graphs and automata-based checking that link the privacy policy model with runtime annotations, enabling on-the-fly compliance verification. (iv) User interface: an infrastructure-independent implementation that visualizes the real-time execution trace of AI agents alongside detected privacy violations, providing user-friendly transparency and accountability.
  We evaluate AudAgent on AI agents built with mainstream frameworks, demonstrating its effectiveness in detecting and visualizing privacy policy violations. Using AudAgent, we further find that many privacy policies lack explicit safeguards for highly sensitive data such as SSNs, whose misuse violates legal requirements, and that many agents, including those powered by Claude, Gemini, and DeepSeek,do not refuse to process such data via third-party tools. AudAgent proactively blocks operations on such data, overriding the agents' original privacy policies and behavior.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI智能体（AI agents）在运行过程中，其数据处理行为是否与声明的隐私政策保持一致的问题。随着基于大语言模型的智能助手和工作流自动化工具日益普及，AI智能体能够自主执行各种任务，但常常在未经用户明确同意的情况下收集或披露用户的本地敏感数据，引发了严重的隐私担忧。尽管这些智能体平台通常提供描述其数据实践的隐私政策，但用户缺乏有效手段来验证其运行时行为是否真正符合这些政策，这种不透明性因复杂的第三方集成（如外部API和服务）而进一步加剧，可能导致意外的数据收集和披露。

现有方法存在明显不足。一方面，针对AI智能体隐私安全的研究多集中于通过静态分析或沙盒测试来防范恶意攻击和基准测试漏洞，而非从终端用户角度持续审计其日常数据实践是否符合隐私政策。另一方面，现有的合规性审计研究主要面向移动应用和网络服务等领域，缺乏专门针对AI智能体动态、自治特性的实时审计工具。此外，自然语言撰写的隐私政策与低层、无序的运行时数据实践之间存在语义鸿沟，使得自动化、高效的合规性验证面临挑战。

因此，本文的核心问题是：如何让终端用户能够对其AI智能体的运行时数据实践进行审计，以验证其是否遵循智能体声称或用户期望的隐私政策。具体而言，论文提出了AudAgent工具，旨在通过自动化、实时的方式，弥合高层隐私政策与底层数据实践之间的差距，为用户提供透明度和问责机制，从而增强对AI智能体的信任。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及方法类、应用类和评测类工作，具体如下：

**方法类**：在隐私政策形式化方面，已有研究利用自然语言处理技术解析隐私政策，但通常依赖单一模型，准确率有限。本文提出的跨LLM投票机制通过集成多个大语言模型的输出，提高了形式化模型的置信度。在运行时数据标注方面，现有工具（如Presidio）能检测敏感数据，但缺乏结合具体上下文和隐私政策进行细粒度标注的能力。AudAgent的标注器在此基础上，依据形式化策略模型对数据实践进行动态注解。

**应用类**：针对AI代理的隐私合规监控，现有工作多集中于静态分析或事后审计，缺乏实时、持续的运行时监控能力。例如，一些可视化工具（如LangChain的调试工具）能追踪代理执行过程，但主要关注功能流程而非隐私数据流。AudAgent则实现了对数据收集、处理、披露和保留实践的实时跟踪与合规性验证。

**评测类**：在隐私政策合规性审计方面，传统方法依赖于手动检查或基于规则的匹配，难以适应AI代理动态、多轮交互的复杂场景。本文基于本体图和自动机的检查方法，能够关联策略模型与运行时注解，实现动态的合规性验证，相比静态规则引擎更具灵活性和准确性。

总体而言，AudAgent整合了上述多个方向的技术，通过端到端的自动化审计流程，填补了AI代理运行时行为与声明隐私政策之间缺乏透明度和问责机制的空白。

### Q3: 论文如何解决这个问题？

AudAgent 通过一个包含四个核心组件的自动化审计框架，实时监控 AI 代理的数据实践并确保其符合声明的隐私政策。

**整体框架与主要模块：**
1.  **策略形式化**：采用基于多 LLM 投票的创新机制。多个不同的 LLM 独立解析自然语言隐私政策文档，生成结构化策略模型。系统通过语义等价性检查和多数投票聚合输出，仅保留超过预设阈值票数的元素，形成最终的高置信度策略模型。该方法不仅提升了准确性，还通过投票数提供了结果可信度的量化度量。
2.  **运行时标注**：采用轻量级、模型引导的数据标注方法。核心使用 Presidio（一个本地的敏感数据识别器）实时检测 AI 代理执行过程中涉及的敏感数据类型（如姓名、邮箱）。随后，系统根据形式化策略模型的指导，为每个检测到的数据实例添加上下文相关的元数据标注，包括收集条件（直接来自用户或间接通过工具）、处理目的（与任务相关或无关）、披露条件和保留期限。
3.  **合规性审计**：通过本体图（ontology graph）和自动机（automata）实现实时审计。本体图用于对齐策略模型中的术语与运行时观察到的数据在层次粒度上的不匹配。形式化的策略模型被编译成直观的状态机，系统将运行时标注的数据流与这些状态机进行比对，从而实现动态的合规性验证。
4.  **用户界面**：设计了一个独立于 AI 代理框架和操作系统的可视化层。通过 HTTP 分析捕获代理的数据交互，利用 WebSocket 流式传输标注数据和审计结果，并在基于浏览器的前端实时展示 AI 代理的执行轨迹及检测到的隐私违规行为，为用户提供透明的问责视图。

**关键技术及创新点：**
*   **高置信度策略解析**：多 LLM 投票机制是核心创新，它通过模拟多参与者决策过程，利用模型间的多样性提升解析准确性和结果置信度，克服了单一 LLM 可能存在的偏差或错误。
*   **模型引导的轻量级标注**：将通用的敏感数据检测器（Presidio）与形式化策略模型提供的具体上下文要求相结合，实现了低开销、高特异性的实时数据标注。
*   **动态合规性检查**：结合本体对齐和自动机理论，将复杂的策略合规性问题转化为可实时执行的状态匹配问题，实现了“运行时”审计。
*   **框架无关的透明化**：通过拦截和分析网络流量（HTTP/WebSocket）来监控代理行为，无需修改代理本身代码，确保了工具的通用性和部署的便捷性，同时为用户提供了直观的违规可视化。

### Q4: 论文做了哪些实验？

论文的实验设置主要围绕评估AudAgent在检测AI代理隐私政策违规方面的有效性。实验使用了基于主流框架（如Claude、Gemini、DeepSeek等）构建的AI代理作为测试对象。数据集或基准测试涉及这些代理在实际运行时的数据交互行为，特别是对敏感数据（如SSN）的处理过程。

对比方法方面，论文将AudAgent的自动化审计能力与现有方法（如依赖单一LLM解析隐私政策或缺乏实时监控的工具）进行对比，突出了其多LLM投票机制和实时合规性验证的优势。

主要结果包括：1）AudAgent能够有效实时检测并可视化隐私政策违规行为；2）通过多LLM投票机制，隐私政策形式化的置信度显著提升（例如，在4个LLM、单个准确率α=0.8的条件下，3票共识可将置信度从0.8提高到约0.94）；3）实验发现许多隐私政策对高敏感数据（如SSN）缺乏明确保护措施，且多个代理未拒绝通过第三方工具处理此类数据；4）AudAgent能够主动阻止对此类数据的操作，覆盖代理原有策略和行为。关键数据指标包括：多LLM投票的置信度提升公式（Pr[e ∈ P*] = (1 + ((1-α)/α)^(2m-M))⁻¹）、Presidio分析器的延迟（平均低于100毫秒）以及投票阈值τ的应用。

### Q5: 有什么可以进一步探索的点？

该论文提出的 AudAgent 系统在实时审计 AI 代理隐私政策合规性方面具有创新性，但仍存在一些局限性和值得深入探索的方向。

首先，系统对隐私政策的解析依赖于多个 LLM 的投票机制，虽然提升了置信度，但 LLM 本身可能存在共有的训练数据偏差或对复杂法律条款的误解风险。未来可探索结合符号逻辑或领域知识图谱来增强政策形式化的准确性与可解释性。其次，数据标注主要基于 Presidio 进行敏感信息识别，对于非结构化或上下文隐含的隐私数据（如通过推理得出的信息）检测能力有限。可研究引入更细粒度的语义理解模型，以识别间接数据收集与使用意图。

此外，合规性审计目前侧重于实时阻断违规操作，但缺乏对长期、跨会话隐私风险的模式分析与预测。未来可构建时序审计框架，对代理行为进行趋势分析，并生成隐私风险报告。最后，系统主要针对文本交互，对多模态数据（如图像、音频）的隐私审计支持不足。结合跨模态敏感信息检测技术将是一个重要的扩展方向。这些改进有望使隐私审计从被动监控转向主动风险治理。

### Q6: 总结一下论文的主要内容

该论文针对AI智能体在运行中可能未经用户明确同意即收集或披露敏感本地数据的隐私风险，提出了一种自动化隐私审计工具AudAgent。核心问题是智能体的实际数据操作常与其声明的隐私政策不一致，缺乏透明度和问责机制。

AudAgent通过四个组件实现自动化审计：首先，采用跨大语言模型投票机制将隐私政策高置信度地解析为形式化模型；其次，基于Presidio的轻量级运行时分析器检测敏感数据并依据上下文和政策模型标注数据实践；再次，通过本体图和自动机检查将政策模型与运行时标注关联，实现实时合规验证；最后，提供独立于基础设施的用户界面，可视化智能体执行轨迹及隐私违规行为。

主要结论表明，AudAgent能有效检测并可视化主流框架构建的智能体的隐私政策违规行为。评估进一步发现，许多隐私政策对高度敏感数据（如社会安全号码）缺乏明确保护，且包括Claude、Gemini和DeepSeek在内的智能体未拒绝通过第三方工具处理此类数据。AudAgent能主动阻止此类数据操作，超越原有政策约束，增强隐私保护的实际执行力。
