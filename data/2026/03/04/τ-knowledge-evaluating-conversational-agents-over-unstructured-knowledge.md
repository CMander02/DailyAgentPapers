---
title: "$τ$-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge"
authors:
  - "Quan Shi"
  - "Alexandra Zytek"
  - "Pedram Razavi"
  - "Karthik Narasimhan"
  - "Victor Barres"
date: "2026-03-04"
arxiv_id: "2603.04370"
arxiv_url: "https://arxiv.org/abs/2603.04370"
pdf_url: "https://arxiv.org/pdf/2603.04370v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.IR"
tags:
  - "Tool Use & API Interaction"
  - "Reasoning & Planning"
relevance_score: 8.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Reasoning & Planning"
  domain: "Finance & Trading"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "τ-Knowledge (extension of τ-Bench)"
  primary_benchmark: "τ-Knowledge (τ-Banking domain)"
---

# $τ$-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge

## 原始摘要

Conversational agents are increasingly deployed in knowledge-intensive settings, where correct behavior depends on retrieving and applying domain-specific knowledge from large, proprietary, and unstructured corpora during live interactions with users. Yet most existing benchmarks evaluate retrieval or tool use independently of each other, creating a gap in realistic, fully agentic evaluation over unstructured data in long-horizon interactions. We introduce $τ$-Knowledge, an extension of $τ$-Bench for evaluating agents in environments where success depends on coordinating external, natural-language knowledge with tool outputs to produce verifiable, policy-compliant state changes. Our new domain, $τ$-Banking, models realistic fintech customer support workflows in which agents must navigate roughly 700 interconnected knowledge documents while executing tool-mediated account updates. Across embedding-based retrieval and terminal-based search, even frontier models with high reasoning budgets achieve only $\sim$25.5% pass^1, with reliability degrading sharply over repeated trials. Agents struggle to retrieve the correct documents from densely interlinked knowledge bases and to reason accurately over complex internal policies. Overall, $τ$-Knowledge provides a realistic testbed for developing agents that integrate unstructured knowledge in human-facing deployments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前对话智能体在知识密集型实际部署场景中缺乏综合性评估基准的问题。研究背景是，对话智能体越来越多地被应用于需要与大型、专有、非结构化知识库进行实时交互的场景（如金融客服），其正确行为依赖于从这些知识库中检索信息并协调工具使用。然而，现有评估方法存在明显不足：大多数基准测试要么孤立地评估检索能力（如问答），要么孤立地评估工具使用能力，未能模拟真实世界中长程交互、目标模糊、用户意图动态演变，且需要将非结构化知识检索与工具输出进行协调的复杂情境。这导致评估与现实部署需求之间存在巨大差距。

因此，本文要解决的核心问题是：如何构建一个更真实、全面的评估框架，以测试智能体在依赖非结构化知识库的长程对话中，能否有效地检索、推理并应用知识来执行可验证的、符合策略的状态变更操作。为此，论文提出了τ-Knowledge基准及其τ-Banking领域，模拟了包含约700份相互关联文档的金融客服工作流，要求智能体在工具未被预先告知的情况下，通过探索知识库来发现工具、理解策略，并最终解决复杂的用户请求。该研究揭示了即使是最先进的模型，在此类任务上的成功率也极低（约25.5%），且可靠性随尝试次数急剧下降，凸显了智能体在从密集互连的知识库中精准检索以及对复杂策略进行准确推理方面面临的根本性挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测基准、检索与知识中心评估、以及人机交互模拟。

在**评测基准与工具使用**方面，现有工作（如各类工具使用基准）主要评估智能体将任务分解为多步计划、调用外部工具和执行结构化程序的能力，但通常假设工具接口完全给定，且未模拟交互式用户或对话动态。τ-Bench 通过引入目标导向、部分可观察的对话环境来弥补这些不足，但工具和流程仍基本预先提供。τ-Knowledge 在此基础上更进一步，要求智能体通过从自然语言语料库中检索来获取程序性知识，包括从文档中发现可用工具。

在**检索与知识中心评估**方面，大量研究通过跨领域的查询-文档匹配来评估嵌入质量，但未能衡量知识访问如何影响决策、工具使用或长程任务成功率。其他工作将检索集成到任务导向或多轮问答中，但这些基准大多仍以事实性为主，对文档的推理需求较低。τ-Knowledge 通过将知识访问抽象为与自然语言语料库的交互，并评估知识使用对任务完成度和可靠性的影响，统一了基于检索、长上下文和工具增强的方法。

在**模拟人机交互**方面，现有研究包括基于角色的模拟器、教育环境中的人类错误模拟以及目标导向的人机交互模拟，但许多用户模拟器会无意中通过提示向智能体透露未来的对话状态或结果，充当了“预言家”角色。τ-Knowledge 则采用基于流程的用户模拟，其条件仅依赖于当前环境状态，并引入了可通过知识库发现的用户工具，使智能体能在共享环境中将行动委托给模拟用户，从而实现指令跟随而不暴露未来状态的特权信息。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为τ-Knowledge的评估框架来解决对话智能体在非结构化知识环境中协调检索与工具使用的难题。其核心方法是扩展τ-Bench，创建一个名为τ-Banking的模拟金融科技客服领域，智能体需在长程交互中，基于约700份相互关联的自然语言知识文档，执行工具调用来完成账户状态变更，并确保操作符合内部政策。

整体框架是一个端到端的评估环境，包含三个主要模块：1）**知识环境**：τ-Banking领域模拟了真实的客服工作流，知识以非结构化的自然语言文档形式存在，文档间具有密集的互连引用关系，增加了检索和推理的复杂性。2）**智能体交互接口**：智能体通过终端命令与模拟系统交互，可以执行搜索、检索工具以及调用各种账户操作工具，系统状态会随之改变。3）**评估机制**：通过验证智能体行为是否产生正确的、符合政策的状态变化来评分，重点关注其能否协调外部知识检索与工具输出来达成目标。

关键技术包括：**密集互连知识库的设计**，这迫使智能体必须理解文档间的复杂关系才能精准检索；**工具使用与知识检索的耦合评估**，而非独立测试，更贴近实际部署场景；**长程、多轮交互的测试设置**，考察智能体的持续可靠性和决策一致性。创新点在于首次提供了一个在真实、动态环境中，对智能体整合非结构化知识、工具使用和策略推理能力进行**一体化、全流程评估**的测试平台，揭示了即使前沿大模型在协调检索与行动、处理复杂政策推理时仍存在显著缺陷（成功率仅约25.5%）。

### Q4: 论文做了哪些实验？

论文在τ-Knowledge基准上进行了系统实验，评估了当前知识增强智能体在非结构化知识库中协调检索与工具使用的能力。

**实验设置与数据集**：核心实验在τ-Banking领域进行，该领域模拟了真实的金融科技客服工作流，智能体需导航约700份相互关联的知识文档，并执行工具介导的账户更新。评估采用pass@k指标（k≤4），重点关注单次尝试成功率（pass@1）和跨多次尝试的可靠性。

**对比方法与配置**：实验比较了多种知识检索/访问方式：(1) **密集检索**：使用text-embedding-3-large和Qwen3-embedding-8B两种嵌入模型进行语义搜索，返回top-10文档；(2) **稀疏检索**：使用BM25进行词法搜索；(3) **终端使用**：将知识库作为文件系统，智能体可使用grep、cat等Unix命令自由探索；(4) **黄金检索器**：直接将完成任务所需的黄金文档置于上下文中，以隔离检索与推理能力的影响。此外，还设置了**无知识**和**长上下文**（直接提供全部知识库）基线。评估的模型包括GPT-5.2、Claude-4.5-Opus/Sonnet、Gemini-3-Pro/Flash等前沿模型，并区分了高推理预算与无/低推理预算配置。

**主要结果与关键指标**：
1.  **任务难度高**：最佳配置（GPT-5.2高推理+终端使用）的pass@1仅为25.52%。即使提供黄金文档，最佳模型（Claude-4.5-Opus）的pass@1也仅39.69%，pass@4降至26.80%，表明复杂推理是主要挑战。
2.  **检索方式影响**：平均而言，终端使用配置（pass@1平均19.20%）显著优于密集检索（16.88%-17.11%）和稀疏检索（17.04%），但收益主要集中在近期的高推理模型上。终端使用导致搜索更频繁（平均每任务28.8次调用），任务耗时更长（中位数回合时间增加6.6秒）。
3.  **模型差异**：模型在可靠性和效率上分化明显。例如，GPT-5.2（高推理）的pass@4最高（13.4%），而Claude模型能以更少的工具调用（如Claude-4.5-Opus平均8.7次检索调用 vs GPT-5.2的18.5次）和更短的持续时间达到相近性能。
4.  **失败归因分析**：文档召回率分析显示，检索质量不仅取决于检索器本身，还受智能体构建查询能力的影响（如同为text-embedding-3-large，与Opus配对召回率57%，与无推理GPT-5.2配对仅28%）。无知识配置平均pass@1仅~2%，验证了任务对检索的依赖。

### Q5: 有什么可以进一步探索的点？

基于论文分析，其局限性及未来可探索的方向主要集中在以下几个方面：

首先，**用户模拟的真实性不足**。当前的用户仿真基于LLM，未能充分体现真实人类交互的复杂性，如用户专业水平的差异、口语化或本地化表达、以及语法不完善或模糊的输入。未来研究可以构建更贴近真实人类行为和心理的模拟器，或引入人类在环的评估，以提升测试生态的逼真度。

其次，**搜索与推理机制的效率与约束场景**。论文在完全开放的搜索设定下进行评估，而实际系统常受单次或少量搜索的限制。未来可探索在严格查询次数约束下的智能体性能，这要求更精准的检索策略和更高效的单次信息利用能力。同时，智能体在长视野任务中普遍存在搜索效率低下和随意假设的问题，需设计更好的内部状态跟踪、笔记工具或知识重组机制来辅助复杂推理。

再者，**错误模式的深入分析与针对性改进**。定性分析揭示了智能体在复杂政策互依性、隐式任务排序、过度信任用户陈述等方面的失败模式。未来可针对这些具体弱点，开发专门的训练方法（如基于失败轨迹的强化学习）或架构改进（如显式依赖关系建模模块），以提升在密集互连知识库中的多跳推理和策略遵从能力。

最后，**评估维度的扩展**。当前评估侧重于任务成功率，而对用户体验（如对话流畅性、澄清能力）的衡量不足。结合人工评估或更细粒度的自动化指标（如困惑度、澄清频率）来评估交互质量，将是推动智能体面向实际部署的关键。此外，将评估领域从金融客服扩展到医疗、法律等更多高风险、知识密集型场景，也能检验智能体能力的通用性。

### Q6: 总结一下论文的主要内容

该论文针对当前对话智能体在知识密集型场景中面临的评估不足问题，提出了τ-Knowledge评估框架。其核心贡献是构建了一个名为τ-Banking的金融科技客服模拟领域，要求智能体在长程对话中，从约700份相互关联的非结构化知识文档中检索信息，并协调工具输出来完成可验证的、符合政策的状态变更任务，从而填补了现有基准在真实、完全自主的非结构化知识整合评估方面的空白。

方法上，论文通过一个结构化到非结构化的生成流程构建了内部一致的知识库，并设计了支持多种检索机制（如基于嵌入的检索、基于终端的搜索）的评估环境。主要结论显示，即使是最先进的模型在高推理预算下，最佳通过率也仅约25.5%，且在重复试验中可靠性急剧下降。即使提供关键文档（黄金检索器设置），最高通过率也不到40%，表明瓶颈不仅在于检索，更在于对复杂政策、跨文档依赖和动态状态的推理。研究还揭示了不同模型与检索配置在性能和效率上的显著权衡，并强调面向人类的智能体发展需同时关注任务成功率和解决效率（如最小化时间、工具调用和对话回溯）。τ-Knowledge为研究知识驱动型智能体中搜索、推理与效率的相互作用提供了一个现实的测试平台。
