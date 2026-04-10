---
title: "EigentSearch-Q+: Enhancing Deep Research Agents with Structured Reasoning Tools"
authors:
  - "Boer Zhang"
  - "Mingyan Wu"
  - "Dongzhuoran Zhou"
  - "Yuqicheng Zhu"
  - "Wendong Fan"
  - "Puzhen Zhang"
  - "Zifeng Ding"
  - "Guohao Li"
  - "Yuan He"
date: "2026-04-09"
arxiv_id: "2604.07927"
arxiv_url: "https://arxiv.org/abs/2604.07927"
pdf_url: "https://arxiv.org/pdf/2604.07927v1"
categories:
  - "cs.AI"
tags:
  - "Web Agent"
  - "Tool Use"
  - "Multi-Agent System"
  - "Query Planning"
  - "Evidence Aggregation"
  - "Benchmark Evaluation"
relevance_score: 8.5
---

# EigentSearch-Q+: Enhancing Deep Research Agents with Structured Reasoning Tools

## 原始摘要

Deep research requires reasoning over web evidence to answer open-ended questions, and it is a core capability for AI agents. Yet many deep research agents still rely on implicit, unstructured search behavior that causes redundant exploration and brittle evidence aggregation. Motivated by Anthropic's "think" tool paradigm and insights from the information-retrieval literature, we introduce Q+, a set of query and evidence processing tools that make web search more deliberate by guiding query planning, monitoring search progress, and extracting evidence from long web snapshots. We integrate Q+ into the browser sub-agent of Eigent, an open-source, production-ready multi-agent workforce for computer use, yielding EigentSearch-Q+. Across four benchmarks (SimpleQA-Verified, FRAMES, WebWalkerQA, and X-Bench DeepSearch), Q+ improves Eigent's browser agent benchmark-size-weighted average accuracy by 3.0, 3.8, and 0.6 percentage points (pp) for GPT-4.1, GPT-5.1, and Minimax M2.5 model backends, respectively. Case studies further suggest that EigentSearch-Q+ produces more coherent tool-calling trajectories by making search progress and evidence handling explicit.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度研究智能体在进行开放式信息检索时，由于依赖隐式、非结构化的搜索行为而导致的效率低下和证据聚合脆弱的问题。研究背景是，随着大语言模型智能体的发展，深度研究（即需要迭代搜索、阅读和综合证据的开放式信息寻求）已成为重要应用，涌现出许多专有和开源系统。然而，现有方法通常将推理和规划任务留给后端大语言模型隐式处理，或采用固定工作流，缺乏在工具层面明确结构化这些过程，这容易造成冗余探索和证据处理的不稳定。

现有方法的不足在于，典型的深度研究智能体未能将规划和推理过程通过结构化工具显式化，导致搜索行为缺乏深思熟虑，中间决策不透明、不可审计，且与后续行动关联松散。这限制了智能体在复杂、模糊查询下高效、稳健地收集和综合信息的能力。

本文要解决的核心问题是：能否通过结构化的、工具介导的“思考”机制，使深度研究智能体的规划和推理过程变得显式化，从而提升其效率和鲁棒性？为此，论文受Anthropic“思考”工具范式的启发，提出了Q+工具集。Q+不直接获取外部信息，而是提供认知支架，通过专门的查询处理和证据处理工具，将查询规划、搜索进度监控和长网页证据提取等操作结构化、可检查化，使得中间决策明确、可审计，并直接关联后续行动。最终，通过将Q+集成到开源多智能体框架Eigent的浏览器子智能体中，构建了EigentSearch-Q+系统，旨在实现更连贯、高效的深度研究行为。

### Q2: 有哪些相关研究？

本文的相关工作主要涉及方法类和应用类。在方法类中，现有深度研究智能体通常采用两种主流范式：一种是类似ReAct的自由式推理，将推理与动作（如搜索、浏览）交错进行，代表工作包括Search-o1、Search-R1、Agent-R1和R1-Searcher；另一种是采用固定的规划工作流来管理推理过程，例如AvaTar、The AI Scientist和DeerFlow。本文提出的Q+工具集与这些方法不同，它受Anthropic“思考工具”范式的启发，通过专用的结构化推理工具来显式地引导智能体的认知过程，使搜索进度和证据处理变得明确和可控。

在应用类中，现有的开源深度研究智能体项目（如CoSearchAgent、Agentic Reasoning、OpenManus、AutoAgent、DeepResearcher等）主要为智能体配备外部能力工具，如网络搜索API、浏览器工具或编码工具，但缺乏专门用于引导结构化推理的工具。本文的Q+工具集填补了这一空白，它将传统信息检索（IR）中的查询生成、查询扩展和搜索前沿管理等算法概念（如伪相关性反馈）映射到智能体的工具空间中，从而将经典的IR策略转化为结构化的、模型驱动的工具调用。因此，Q+在方法上区别于现有的自由推理或固定工作流，在应用上引入了专用的推理工具来增强智能体的深度研究能力。

### Q3: 论文如何解决这个问题？

论文通过引入一套名为Q+的结构化推理工具集，来解决深度研究智能体中存在的隐性、非结构化搜索行为导致的冗余探索和脆弱证据聚合问题。该方法的核心是增强Eigent浏览器子代理，使其搜索过程更具规划性和显式化。

整体框架建立在开源的、面向计算机使用的多智能体工作流Eigent之上。Eigent本身包含浏览器代理、开发者代理、多模态代理和文档代理等多个专门子代理。其中，浏览器代理原本配备了搜索、浏览器导航、终端和笔记四个工具包，但其搜索行为直接且缺乏中间规划。

Q+工具集创新性地采用了Anthropic的“think”工具范式，即工具调用仅作为记录中间推理痕迹的接口，而不直接获取外部新信息。Q+主要包含两大模块：

1.  **查询处理工具**：旨在使查询生成和选择过程结构化。具体包括：
    *   `plan_next_searches`工具：负责查询规划。它通过识别知识缺口，并应用查询重写、扩展和分解等技术，生成后续候选查询。
    *   `select_query_and_search`工具：负责从候选查询队列（前沿集）中选择一个查询并执行搜索，以此替代原有的直接搜索行为。

2.  **证据处理工具**：旨在显式化地处理长网页内容并评估搜索进度。具体包括：
    *   `extract_relevant_details`工具：从浏览器工具包返回的长网页快照中，提取与问题或当前查询相关的具体细节，有效过滤无关信息。
    *   `analyze_search_progress`工具：评估已积累的证据是否足以回答原始问题，从而为停止搜索提供明确的决策依据。

此外，系统通过**搜索状态管理**引入了一个软约束机制，维护“前沿”（已生成未搜索）和“已探索”（已执行）两个查询集合，并阻止对已探索查询的重复搜索，从而减少了冗余。

其核心创新点在于，将原本内隐的搜索决策（如下一步搜什么、何时停止）外部化为一系列结构化的工具调用轨迹。这使得智能体的搜索过程变得可规划、可监控、可追溯，最终在多个基准测试上显著提升了答案准确率，并生成了更连贯、更显式的工具调用序列。

### Q4: 论文做了哪些实验？

论文在四个开源基准测试上进行了实验：SimpleQA-Verified（1000个简短事实性问题）、FRAMES（824个多跳推理问题）、WebWalkerQA（680个网页遍历问题）和X-Bench DeepSearch（100个深度搜索任务）。实验设置了四种智能体配置进行比较：直接生成（基线）、仅搜索（仅调用搜索工具）、Eigent浏览器智能体以及增强的EigentSearch-Q+系统。评估使用了四种大语言模型后端：GPT-4.1 mini、GPT-4.1、GPT-5.1和Minimax M2.5，温度均设为0，并使用GPT-4.1作为自动评判器。

主要结果显示，对于GPT系列模型，EigentSearch-Q+相比标准Eigent浏览器智能体在准确率上取得一致提升。具体而言，Q+将Eigent浏览器智能体在四个基准测试上的规模加权平均准确率分别提升了：GPT-4.1后端提升3.0个百分点，GPT-5.1后端提升3.8个百分点，Minimax M2.5后端提升0.6个百分点。对于GPT-4.1 mini，两者性能大致相当，但Q+在X-Bench上提升显著。对于Minimax M2.5，Q+在WebWalkerQA上表现稍逊，但在其他基准上均有所改进。案例研究进一步表明，Q+通过显式的查询规划、进度监控和证据提取，生成了更连贯、结构化的工具调用轨迹，避免了冗余探索和证据聚合的脆弱性。

### Q5: 有什么可以进一步探索的点？

本文的局限性及未来探索方向主要集中在以下几个方面。首先，作者指出需要更系统的对比研究，以厘清Q+工具提供的显式结构化推理与大型语言模型（LLM）内部固有推理能力之间的关系。具体而言，未来工作应设计受控实验，在“启用推理”与“禁用推理”的不同模型后端上进行广泛比较，明确Q+的增益是互补作用还是部分冗余。这有助于更精准地定位工具的价值。

其次，当前系统是无需训练的（training-free），这虽然降低了部署门槛，但也可能限制了性能上限。作者提到正在探索基于微调（fine-tuning）和强化学习（RL）的变体，这是一个重要的方向。通过让系统从交互数据中学习，可能可以进一步优化查询规划、进度监控和证据提取的策略，从而放大Q+带来的效果提升。

结合个人见解，可能的改进思路还包括：1）增强工具的适应性与泛化能力，使其能根据不同的任务类型（如事实核查、综合分析、创意生成）动态调整搜索和推理策略；2）探索多模态证据的处理，当前工作主要基于文本网页快照，未来可整合图像、图表等非结构化信息，使证据聚合更全面；3）引入对搜索过程本身的元认知评估机制，让智能体能实时评估已获证据的充分性与可靠性，从而更早地终止无效探索或转向新的查询方向，进一步提升效率与连贯性。

### Q6: 总结一下论文的主要内容

该论文针对深度研究智能体在开放性问题回答中存在的搜索冗余和证据整合脆弱性问题，提出了一种名为Q+的结构化推理工具集。核心贡献在于将信息检索领域的洞见与“思考”工具范式相结合，设计了一套显式的查询与证据处理工具，用于引导查询规划、监控搜索进度并从长网页快照中提取证据。方法上，作者将Q+集成到开源多智能体工作流Eigent的浏览器子智能体中，形成了EigentSearch-Q+系统。实验表明，在多个基准测试上，该系统显著提升了不同模型后端（如GPT-4.1、GPT-5.1等）的准确率，案例研究也证实其能产生更连贯的工具调用轨迹。论文结论强调，Q+的非侵入式模块化设计使其可作为可复用组件，增强其他深度研究智能体的鲁棒性和可解释性，为复杂多步骤信息检索任务提供了有效的结构化推理层。
