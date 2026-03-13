---
title: "Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections"
authors:
  - "Łukasz Borchmann"
  - "Jordy Van Landeghem"
  - "Michał Turski"
  - "Shreyansh Padarha"
  - "Ryan Othniel Kearns"
  - "Adam Mahdi"
  - "Niels Rogge"
  - "Clémentine Fourrier"
  - "Siwei Han"
  - "Huaxiu Yao"
  - "Artemis Llabrés"
  - "Yiming Xu"
  - "Dimosthenis Karatzas"
  - "Hao Zhang"
  - "Anupam Datta"
date: "2026-03-12"
arxiv_id: "2603.12180"
arxiv_url: "https://arxiv.org/abs/2603.12180"
pdf_url: "https://arxiv.org/pdf/2603.12180v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Document QA"
  - "Evaluation Protocol"
  - "Reasoning Analysis"
  - "Multimodal Agent"
  - "Retrieval-Augmented Generation"
relevance_score: 8.0
---

# Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections

## 原始摘要

Multimodal agents offer a promising path to automating complex document-intensive workflows. Yet, a critical question remains: do these agents demonstrate genuine strategic reasoning, or merely stochastic trial-and-error search? To address this, we introduce MADQA, a benchmark of 2,250 human-authored questions grounded in 800 heterogeneous PDF documents. Guided by Classical Test Theory, we design it to maximize discriminative power across varying levels of agentic abilities. To evaluate agentic behaviour, we introduce a novel evaluation protocol measuring the accuracy-effort trade-off. Using this framework, we show that while the best agents can match human searchers in raw accuracy, they succeed on largely different questions and rely on brute-force search to compensate for weak strategic planning. They fail to close the nearly 20% gap to oracle performance, persisting in unproductive loops. We release the dataset and evaluation harness to help facilitate the transition from brute-force retrieval to calibrated, efficient reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究多模态智能体在处理复杂文档密集型任务时，其行为本质是真正的战略性推理，还是仅仅是随机的试错搜索。研究背景在于，多模态智能体在自动化企业级文档工作流中展现出潜力，但现有评估方法存在局限：现有基准测试要么专注于单一文档或简单检索（如DocVQA），缺乏对多步骤、跨文档推理的评估；要么虽涉及多文档（如BRIGHT），但依赖HTML/文本格式，忽略了真实PDF文档的视觉布局理解需求；还有一些基准（如ViDoRE）使用模型生成的问题，可能导致数据偏差或污染。这些不足使得当前方法难以准确衡量智能体的战略性规划能力。因此，本文的核心问题是：智能体在复杂文档集合上进行信息检索和推理时，是否展现出类似人类的、高效的策略性导航能力，还是依赖于暴力搜索来弥补策略缺陷？为此，论文引入了MADQA基准，包含2250个人工撰写的问题和800份异构PDF文档，并设计了新的评估协议来衡量精度与努力程度的权衡，以推动智能体从暴力检索向校准高效推理的转变。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：文档问答基准、多模态检索增强生成（RAG）基准以及智能体研究基准。

在**文档问答基准**方面，相关工作包括DocVQA、InfographicVQA、TAT-DQA、DUDE、MP-DocVQA、SlideVQA、M-LongDoc和MMLongBench-Doc等。这些基准大多关注对单个文档或图像进行视觉问答。本文提出的MADQA与它们的区别在于，其问题基于一个异构的PDF文档集合，要求进行多步骤、跨文档的检索与推理，而不仅仅是针对单一文档的理解。

在**多模态RAG基准**方面，相关工作包括MuRAR、M²RAG、MR²-Bench、ViDoRE v3、DocBench、M3DocRAG、MMDocIR、FinRAGBench-V、VIMDoc、JINA-VDR和UniDoc-Bench等。这些基准虽然也使用文档集合，但本文指出它们存在方法上的局限：例如ViDoRE v3使用MLLM生成问答对，可能引入模型偏差；VIMDoc和DOUBLE-BENCH等回收利用旧数据集（如DocVQA）的文档，存在数据污染风险。MADQA则通过使用全新文档和完全由人工撰写的问题来确保数据完整性，并强调智能体所需的迭代规划能力。

在**智能体研究基准**方面，相关工作包括BRIGHT、Researchy Questions、ViDoSeek、DOUBLE-BENCH和MRMR。本文认为，像BRIGHT这样的基准虽然捕捉了“智能体研究”的复杂性，但其依赖HTML或纯文本，忽略了真实文档所需的视觉理解能力。而像FinRAGBench-V等垂直领域基准则范围过窄。MADQA综合了异构PDF集合的高布局多样性、广泛的领域覆盖以及多步骤推理要求，并通过引入一个衡量准确性与努力程度权衡的新评估协议，专门用于评估智能体的战略推理能力，而非随机的试错搜索。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为MADQA的综合性基准测试，并设计一套全新的评估协议来解决“智能体是进行战略性推理还是随机试错搜索”的核心问题。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块：**
1.  **基准数据集构建 (MADQA)**：创建了一个包含2,250个人工编写问题、基于800份异构PDF文档的数据集。其架构设计围绕六个核心属性展开：提取性、多跳推理、封闭世界、证据锚定、智能体性和视觉理解。这确保了任务需要真正的规划、导航和聚合能力，而非简单的检索。
2.  **严谨的数据构建与验证流程**：
    *   **文档收集**：从DocumentCloud等来源手动筛选相关文档簇，以支持跨文档的多跳问题。
    *   **人工标注协议**：聘请专业标注员，制定严格指南，确保问题可解、无歧义，且答案必须完全源自文档集，并标注最小证据页集合。
    *   **质量保证**：通过两阶段验证（如使用GPT-5配合完美上下文进行筛查）和专家同步监督，确保数据高质量。同时分析词汇重叠度、参数知识猜测率和视觉必要性，以验证基准确实衡量了语义理解、事实依据和视觉解析能力，而非表面特征。
3.  **基于经典测验理论的划分**：应用项目反应理论，根据问题的难度和区分度，将数据集划分为开发集、测试集和一个“哨兵池”。哨兵池包含当前模型无法解决的难题，保证了基准的长期挑战性和区分模型能力强弱的能力。
4.  **创新的评估协议**：
    *   **答案准确性**：采用基于LLM的评判员来评估答案正确性，在保证严格基于提取内容的同时，容忍语义正确但表面形式不同的回答，并与人工判断保持高度一致。
    *   **证据归因**：使用页面级F1分数和文档级F1分数，衡量智能体找到的引用页面与人类标注的最小证据集之间的重叠度，评估其导航和定位精度。
    *   **效率校准（核心创新）**：引入了基于累积差异方法和Kuiper统计量的新指标，用于量化“准确性-努力程度”的权衡关系。该指标通过分析智能体在不同努力程度（如工具调用步骤数）下的准确率偏离全局平均水平的程度，来揭示其行为是经过校准的高效推理，还是盲目的暴力搜索。高Kuiper值表明智能体在困难问题上耗费大量努力却依然失败，即存在效率低下和校准不良的问题。

**创新点：**
1.  **任务定义与基准设计**：首次系统性地定义了具备智能体性、多跳、视觉理解等综合属性的文档问答任务，并构建了完全由人工标注、文档新鲜且领域布局多样的大规模基准，避免了现有基准在格式、范围和数据完整性方面的局限。
2.  **效率感知的评估指标**：超越了传统的准确率衡量，开创性地提出了用于评估智能体努力校准程度的Kuiper指标，能够直接量化并揭示智能体是否进行战略性规划，抑或是依赖随机试错。
3.  **基于心理测量学的数据集划分**：将经典测验理论应用于基准构建，确保测试集具有高区分度，并特意保留“哨兵”问题以维持基准的长期有效性，这是一种方法论上的创新。
4.  **全面的实验分析框架**：通过该框架，论文不仅比较了智能体与非智能体系统（如静态RAG）的性能，还首次对比了人类与智能体的研究行为，揭示了智能体在达到相近准确率时，其成功的问题类型与人类不同，且严重依赖暴力搜索来弥补战略规划的不足，存在近20%的性能差距和效率鸿沟。

### Q4: 论文做了哪些实验？

论文实验围绕新提出的MADQA基准展开，旨在评估智能体在异构文档集合上的战略推理能力。实验设置上，作者构建了一个包含800份多样化PDF文档（涵盖金融、政府、法律等13个领域）和2,250个人工标注问答对的数据集。数据集设计强调多跳推理（约20%的问题需跨页面或跨文档）和视觉理解（58%的问题需利用表格、图表等布局或视觉元素），并通过古典测试理论筛选出具有高区分度的测试集，其中包含20%的“哨兵池”问题以确保基准的长期挑战性。

对比方法包括两大类系统：非智能体系统（如Gemini 3 Pro File Search、GPT-5.2 HEAVEN等基于静态检索增强生成的方法）和智能体系统（如Gemini 3 Pro BM25 Agent、Claude Sonnet 4.5 BM25 Agent等具备多步推理能力的智能体框架）。评估协议不仅测量准确率，还引入新颖的“准确率-努力权衡”指标，包括页面级F1（Page F1）、文档级F1（Doc F1）以及量化努力校准程度的Kuiper统计量（越低越好）。

主要结果显示，最佳智能体系统（Gemini 3 Pro BM25 Agent）在整体准确率达到82.2%，与非智能体最佳系统（Gemini 3 Pro File Search，78.6%）相比有所提升，但仍与Oracle性能存在近20%的差距。关键数据指标包括：智能体在跨文档推理（X-Doc）任务上，Claude Sonnet 4.5 BM25 Agent达到82.0%的准确率；但智能体的Kuiper值普遍较高（如GPT-5 Mini BM25 Agent为73.2），表明其努力与准确率关联性差，依赖暴力搜索而非战略规划。此外，页面级F1最高为79.1%（Claude Sonnet 4.5 BM25 Agent），显示智能体在精准定位证据方面仍有不足。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其基准测试（MADQA）虽能有效区分智能体能力，但主要评估静态文档集合上的问答，未涉及动态、流式或实时更新的文档环境，这限制了其对真实世界工作流的泛化能力。此外，评估协议侧重于准确率与努力程度的权衡，但未深入量化“战略推理”的具体认知成分（如规划深度、假设检验能力）。

未来研究方向可从三方面展开：一是开发更细粒度的评估指标，例如引入眼动或决策轨迹分析，以区分智能体是基于语义理解还是模式匹配进行导航；二是探索跨文档推理的强化学习框架，通过模拟人类“浏览-筛选-验证”的迭代过程，减少智能体的无效循环；三是将研究扩展至多轮交互场景，让智能体在不确定信息下进行动态查询优化，从而逼近人类在复杂检索中的自适应能力。改进思路上，可结合神经符号方法，为智能体嵌入显式的推理规则（如文档相关性链式推导），以降低随机搜索的依赖性。

### Q6: 总结一下论文的主要内容

本文针对多模态智能体在复杂文档处理任务中是否具备真正的战略推理能力，还是仅依赖随机试错搜索的问题，提出了MADQA基准和一套评估框架。核心贡献在于构建了一个包含2250个人工编写问题、覆盖800份异构PDF文档的基准，并基于经典测试理论设计，以最大化区分不同智能体能力。方法上，论文定义了任务的六个关键属性，并引入了一种新颖的评估协议，用于衡量智能体在准确性与努力程度之间的权衡。主要结论显示，尽管最佳智能体在原始准确率上能媲美人类搜索者，但它们成功解决的问题类型与人类不同，且严重依赖蛮力搜索来弥补战略规划的不足，无法弥合与理想性能之间近20%的差距，并常陷入无效循环。该研究为促进从蛮力检索到高效校准推理的转变提供了数据集和评估工具。
