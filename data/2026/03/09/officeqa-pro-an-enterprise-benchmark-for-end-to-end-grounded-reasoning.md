---
title: "OfficeQA Pro: An Enterprise Benchmark for End-to-End Grounded Reasoning"
authors:
  - "Krista Opsahl-Ong"
  - "Arnav Singhvi"
  - "Jasmine Collins"
  - "Ivan Zhou"
  - "Cindy Wang"
  - "Ashutosh Baheti"
  - "Owen Oertell"
  - "Jacob Portes"
  - "Sam Havens"
  - "Erich Elsen"
  - "Michael Bendersky"
  - "Matei Zaharia"
  - "Xing Chen"
date: "2026-03-09"
arxiv_id: "2603.08655"
arxiv_url: "https://arxiv.org/abs/2603.08655"
pdf_url: "https://arxiv.org/pdf/2603.08655v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.IR"
tags:
  - "评测基准"
  - "检索增强生成"
  - "多文档推理"
  - "企业应用"
  - "长上下文处理"
  - "表格理解"
relevance_score: 7.5
---

# OfficeQA Pro: An Enterprise Benchmark for End-to-End Grounded Reasoning

## 原始摘要

We introduce OfficeQA Pro, a benchmark for evaluating AI agents on grounded, multi-document reasoning over a large and heterogeneous document corpus. The corpus consists of U.S. Treasury Bulletins spanning nearly 100 years, comprising 89,000 pages and over 26 million numerical values. OfficeQA Pro consists of 133 questions that require precise document parsing, retrieval, and analytical reasoning across both unstructured text and tabular data. Frontier LLMs including Claude Opus 4.6, GPT-5.4, and Gemini 3.1 Pro Preview achieve less than 5% accuracy on OfficeQA Pro when relying on parametric knowledge, and less than 12% with additional access to the web. When provided directly with the document corpus, frontier agents still struggle on over half of questions, scoring 34.1% on average. We find that providing agents with a structured document representation produced by Databricks' ai_parse_document yields a 16.1% average relative performance gain across agents. We conduct additional ablations to study the effects of model selection, table representation, retrieval strategy, and test-time scaling on performance. Despite these improvements, significant headroom remains before agents can be considered reliable at enterprise-grade grounded reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前人工智能代理在真实企业环境中进行“端到端、基于文档的推理”能力评估不足的问题。研究背景是，尽管前沿大语言模型在特定推理任务上表现出色，但现有基准测试（如Humanity’s Last Exam、ARC-AGI-2）往往与实际企业工作流程脱节，它们要么聚焦于学术知识，要么在封闭设定中提供有限上下文，未能充分模拟企业场景中处理大规模、异构文档集合的复杂需求。现有方法的不足主要体现在：像GDPval这样的基准虽向经济价值任务迈进，但其任务设计通常假设完整上下文可直接提供，忽略了在庞大企业文档库中进行精准检索的挑战，且依赖人工专家评分，评估成本高昂。

因此，本文的核心问题是：如何构建一个能有效评估AI代理在真实企业级“基于文档的推理”任务上能力的基准。具体而言，论文引入了OfficeQA Pro基准，它要求代理对一个包含近百年美国财政部公报、共计8.9万页和超过2600万个数值的大规模异构文档库进行精确的文档解析、检索和分析推理。该基准旨在弥补现有评估的缺口，通过133个可验证答案的问题，直接测试代理在文档密集型工作流中的端到端性能，从而推动AI代理在具有实际经济价值的企业任务上的可靠性发展。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：企业级Agent评测、文档解析与检索、以及量化推理基准。

在企业级Agent评测方面，GDPVal和APEX-Agents等工作模拟了专业环境，要求Agent在特定领域工作流中生成报告或执行长周期任务。OfficeQA Pro与此类研究目标一致，旨在连接抽象推理与现实效用，但其独特之处在于使用了一个庞大、异构的真实历史文档库（美国财政部公报），并专注于端到端的、可验证的答案生成，从而更直接地评估企业级落地所需的扎实推理能力。

在文档解析与检索方面，OmniDocBench揭示了复杂PDF布局对信息提取的挑战，这与OfficeQA Pro中从扫描件到数字PDF的多样版式问题直接相关。BRIGHT或BrowseComp-Plus等基准则表明，当相关性判断需要意图推理时，标准的语义或关键词匹配会失效，这同样映射到OfficeQA Pro中Agent必须主动识别相关文档和章节的难点。本文将这些环节整合进端到端的评估流程。

在量化推理方面，FinanceBench评估了基于财务文件的开放式问答，强调忠实的提取与计算；LongBenchv2等长上下文基准则揭示了持续的长文档推理仍很困难。OfficeQA Pro继承了这些工作对可靠量化分析的关注，并将其置于更复杂的多文档、跨表格与文本的混合数据环境中进行综合考验，从而提供了一个更统一、更严苛的评测框架。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为OfficeQA Pro的企业级基准测试，并设计一个可定制的智能体（Agent）系统来研究如何解决基于大规模异构文档进行端到端、有依据的推理这一难题。其核心方法在于系统地评估和优化智能体架构中的各个关键组件，以提升在复杂文档问答任务上的性能。

**整体框架与主要模块**：研究采用了一个模块化的自定义智能体架构。该智能体以大型语言模型（LLM）为核心后台，负责规划、使用工具和生成最终答案。系统为智能体配备了多种关键工具：1) **Web搜索工具**，用于查询公开互联网以获取补充信息；2) **Python执行环境**，提供一个沙盒化的、有状态的Python REPL，用于执行数值计算、数据操作和多步推理；3) **文件搜索工具**，包括自定义的`fs_search`和`fs_read`功能，允许智能体在文档语料库中进行类似grep、cat等的基本文件检索和读取操作，但施加了安全限制以防止越权访问。智能体运行时有步数限制（最多200步）并采用滑动窗口机制管理上下文。

**核心方法与创新点**：论文的创新性主要体现在通过一系列受控的消融实验，深入剖析并优化了影响智能体性能的关键因素：
1.  **文档解析器的关键作用**：研究首次系统比较了不同文档解析器对最终问答性能的显著影响。实验对比了开源的Docling、商业的unstructured.io和Databricks的`ai_parse_document`。结果表明，使用`ai_parse_document`生成的**结构化文档表示**能带来平均16.1%的相对性能提升，在成本效益上也最优。这凸显了高质量、结构化的文档解析是解决企业级多模态文档理解的基础和瓶颈。
2.  **多维度组件消融研究**：论文超越了单纯比较端到端性能，深入进行了多项设计决策的消融分析：a) **模型选择**：在10个前沿LLM中评估，发现Claude Opus 4.6准确率最高（57.1%），同时分析了不同模型在延迟与成本上的权衡。b) **表格表示**：比较了HTML与分层Markdown的表格表示形式，发现HTML通常能带来轻微的性能提升。c) **检索策略**：评估了不同搜索工具配置，发现结合基于上下文的嵌入向量搜索与文件搜索能提供最佳的质量-成本权衡。d) **测试时计算扩展**：通过多数投票等策略进行测试时扩展，获得了稳定但有限的性能增益。

总之，论文的解决方案是通过一个精心设计的、工具增强的智能体框架，并系统性地优化其数据预处理（解析）、核心模型、信息检索和推理策略等多个环节，来逐步攻克企业级有依据推理的挑战。然而，即使经过这些优化，智能体的最高准确率仍不足60%，表明该领域仍有巨大的提升空间。

### Q4: 论文做了哪些实验？

论文实验主要分为两个部分：前沿AI系统性能评估和自定义智能体实验。

**实验设置与数据集**：实验使用新提出的OfficeQA Pro基准，该基准包含133个问题，要求基于一个包含近100年、89,000页、超过2600万个数值的美国财政部公报（U.S. Treasury Bulletins）异构文档库进行多文档、基于事实的推理。评估了多种配置下的性能，包括是否允许网络搜索、是否提供“神谕”（oracle）文档页面、以及文档是原始PDF格式还是经过解析的结构化格式。

**对比方法与主要结果**：
1.  **前沿LLM基线评估**：评估了GPT-5.4、Claude Opus 4.6和Gemini 3.1 Pro Preview。在仅依赖参数知识的“仅提示”设置下，所有模型在0.0%绝对相对误差允许阈值下的准确率均低于3%。启用网络搜索后，最佳模型（GPT-5.4）准确率提升至11.3%。当直接提供所需的神谕PDF页面并允许网络搜索时，模型准确率在36%至57%之间。若将PDF预先通过Databricks的`ai_parse_document`解析为结构化文本，所有模型性能均获得提升，相对增益平均达16.1%，其中Claude Opus 4.6提升最为显著（从36.1%升至57.1%）。
2.  **智能体基线评估**：使用各模型提供商（OpenAI、Anthropic、Google）的公开智能体框架进行评估。配置包括处理完整文档库与神谕页面、处理原始PDF与解析后文档。在完整PDF语料库上，Claude Opus 4.6智能体准确率最高（48.1%）。使用解析后的文档，所有智能体性能均显著提升（绝对提升6.0-20.3个百分点），速度提升4-9倍，成本也大幅降低。在最佳配置（提供神谕解析文档）下，Claude Opus 4.6智能体达到最高准确率66.9%。
3.  **自定义智能体实验**：构建自定义智能体以进行消融研究。关键实验比较了三种文档解析器（Docling、unstructured.io、Databricks `ai_parse_document`）的效果。结果表明，`ai_parse_document`在准确率和成本效益上均最优，平均准确率达50.4%，平均成本为每样本5.29美元。其他消融研究还包括模型选择（10种前沿LLM中Claude Opus 4.6最佳，达57.1%）、表格表示形式（HTML略优于Markdown）、检索工具组合（文件搜索结合向量搜索最佳）以及测试时扩展策略（多数投票带来小幅稳定提升）。

**关键数据指标**：
*   仅提示（参数知识）：准确率 <3% （0.0%误差阈值）
*   启用网络搜索：GPT-5.4准确率 11.3%
*   神谕PDF页面+网络搜索：模型准确率 36.1% (Opus 4.6) 至 57.1% (GPT-5.4)
*   神谕解析页面+网络搜索：模型准确率提升至 56.4% (Gemini) 至 65.4% (GPT-5.4)
*   智能体（完整PDF语料）：最高准确率 48.1% (Opus 4.6)
*   智能体（神谕解析文档）：最高准确率 66.9% (Opus 4.6)
*   解析器对比：`ai_parse_document` 平均准确率 50.4%，平均成本 $5.29/样本

### Q5: 有什么可以进一步探索的点？

该论文提出的OfficeQA Pro基准在长文档、多模态（文本与表格）和精确数值推理方面设置了高标准，但仍有明显局限和探索空间。首先，基准规模较小（仅133个问题），可能无法全面覆盖企业文档中复杂的推理模式，未来可大幅扩展问题集和文档类型（如合同、财报），并引入更具挑战性的多跳推理和矛盾检测任务。其次，当前结构化解析工具（如ai_parse_document）虽能提升性能，但解析质量本身可能成为瓶颈；未来可探索端到端的可学习解析模块，使模型能联合优化文档理解与答案生成。此外，检索策略仍依赖传统方法，在跨表格和文本的细粒度信息定位上效率不足，结合强化学习或迭代检索机制可能改善这一点。最后，现有评估仅关注最终答案准确性，未来可引入推理路径评估和置信度校准指标，以提升代理在关键企业场景中的可靠性和可解释性。

### Q6: 总结一下论文的主要内容

该论文提出了OfficeQA Pro基准测试，旨在评估AI代理在大型异构文档库上进行端到端、基于文档的推理能力。其核心贡献在于构建了一个包含近百年美国财政部公报（8.9万页、超2600万个数值）的复杂语料库，并设计了133个需要精确文档解析、检索及跨非结构化文本与表格数据分析推理的问题。

论文指出，当前前沿大语言模型（如Claude Opus 4.6、GPT-5.4等）在此任务上面临严峻挑战：仅依赖参数知识时准确率低于5%，即使允许联网搜索也低于12%；即使直接提供全部文档，平均准确率也仅为34.1%。研究发现，为模型提供由Databricks ai_parse_document生成的结构化文档表示，可将性能平均相对提升16.1%。论文还通过消融实验分析了模型选择、表格表示、检索策略等因素的影响。

该研究的核心意义在于揭示了当前AI代理在企业级、多文档、数值密集型推理任务上的显著能力缺口，为未来智能代理系统的研发提供了重要的评估基准和改进方向。
