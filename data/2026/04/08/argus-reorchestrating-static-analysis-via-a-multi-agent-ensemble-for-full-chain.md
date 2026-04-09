---
title: "Argus: Reorchestrating Static Analysis via a Multi-Agent Ensemble for Full-Chain Security Vulnerability Detection"
authors:
  - "Zi Liang"
  - "Qipeng Xie"
  - "Jun He"
  - "Bohuan Xue"
  - "Weizheng Wang"
  - "Yuandao Cai"
  - "Fei Luo"
  - "Boxian Zhang"
  - "Haibo Hu"
  - "Kaishun Wu"
date: "2026-04-08"
arxiv_id: "2604.06633"
arxiv_url: "https://arxiv.org/abs/2604.06633"
pdf_url: "https://arxiv.org/pdf/2604.06633v1"
categories:
  - "cs.CR"
  - "cs.CL"
  - "cs.SE"
tags:
  - "多智能体协作"
  - "工具使用"
  - "安全Agent"
  - "代码Agent"
  - "检索增强生成"
  - "ReAct"
  - "静态分析"
  - "漏洞检测"
  - "工作流编排"
relevance_score: 8.0
---

# Argus: Reorchestrating Static Analysis via a Multi-Agent Ensemble for Full-Chain Security Vulnerability Detection

## 原始摘要

Recent advancements in Large Language Models (LLMs) have sparked interest in their application to Static Application Security Testing (SAST), primarily due to their superior contextual reasoning capabilities compared to traditional symbolic or rule-based methods. However, existing LLM-based approaches typically attempt to replace human experts directly without integrating effectively with existing SAST tools. This lack of integration results in ineffectiveness, including high rates of false positives, hallucinations, limited reasoning depth, and excessive token usage, making them impractical for industrial deployment. To overcome these limitations, we present a paradigm shift that reorchestrates the SAST workflow from current LLM-assisted structure to a new LLM-centered workflow. We introduce Argus (Agentic and Retrieval-Augmented Guarding System), the first multi-agent framework designed specifically for vulnerability detection. Argus incorporates three key novelties: comprehensive supply chain analysis, collaborative multi-agent workflows, and the integration of state-of-the-art techniques such as Retrieval-Augmented Generation (RAG) and ReAct to minimize hallucinations and enhance reasoning. Extensive empirical evaluation demonstrates that Argus significantly outperforms existing methods by detecting a higher volume of true vulnerabilities while simultaneously reducing false positives and operational costs. Notably, Argus has identified several critical zero-day vulnerabilities with CVE assignments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的静态应用安全测试（SAST）方法在实际工业部署中效果不佳的核心问题。研究背景是软件漏洞数量激增，对数字生态系统构成严重威胁，而传统的SAST工具（如CodeQL）依赖符号或规则分析，虽能检测已知漏洞模式，但缺乏灵活性，难以发现新型或系统特定漏洞，且存在高误报率、对复杂代码库可扩展性不足、语义上下文理解有限等固有缺陷。

现有LLM增强方法试图将LLM作为专家直接用于漏洞分析，并与传统SAST工具结合，虽有一定改进，但仍存在三大不足：一是其工作流程仍以SAST工具为中心，LLM仅作为辅助，推理深度受限于单次推断，难以挖掘新漏洞；二是LLM的“幻觉”问题会引入额外误报；三是简单的LLM与工具组合未能有效解决数据流中断等可达性挑战，导致在面对新型漏洞和受限上下文时表现不佳。

因此，本文的核心问题是：如何设计一种能充分发挥LLM在漏洞检测中潜力的、LLM与SAST工具的整合新范式？为此，论文提出了一个根本性的范式转变，即从“以SAST工具为中心、LLM辅助”的工作流，重构为“以LLM为中心”的新工作流。具体解决方案是引入Argus——首个专为漏洞检测设计的多智能体框架。它通过三大创新来解决上述问题：1）全面的软件供应链分析，将代码库与其依赖项结合评估；2）协作式多智能体工作流，将SAST流程解耦并由不同智能体（如依赖扫描、信息收集、PoC生成等）分工协作；3）集成RAG和ReAct等先进技术，以最小化幻觉并增强深度推理能力，从而实现更通用、适应性强且稳健的漏洞检测。

### Q2: 有哪些相关研究？

相关研究主要可分为两大类：基于LLM的漏洞检测与发现，以及LLM智能体技术。

在**基于LLM的漏洞检测与发现**方面，已有研究探索了LLM直接识别源代码中常见漏洞模式（如CWE类别）的能力，特别是当结合提交信息等元数据时。另一些工作则利用LLM挖掘代码中的未知源或汇点，以支持更精确的静态污点分析。系统评估也表明，即使是基于提示工程的LLM也能提升漏洞检测率。然而，这些方法通常试图直接替代人类专家，未能与现有SAST工具有效整合，导致高误报、幻觉、推理深度有限和令牌消耗过大等问题。本文提出的Argus框架则实现了范式转变，从“LLM辅助”转向“以LLM为中心”的工作流，通过多智能体协同和整合现有工具链来系统性解决上述局限。

在**LLM智能体技术**方面，ReAct框架通过交错推理与行动执行，已成为支持复杂任务的智能体标准架构。检索增强生成（RAG）技术则使智能体能够利用外部知识库来增强响应的准确性和时效性。此外，规划器-执行器等模块化设计、思维链（CoT）提示及其变体（如自我反思、回退提示）也显著提升了智能体在多步骤推理任务中的可靠性和成功率。本文的Argus框架并非发明全新的智能体基础技术，而是创造性地将这些前沿技术（如ReAct、RAG）整合并应用于**全链漏洞检测**这一特定领域，设计了专门的多智能体协作工作流，并首次引入了全面的供应链分析，从而在降低幻觉、增强推理的同时实现了工业级实用性。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Argus的多智能体框架，从根本上重构了静态应用安全测试（SAST）的工作流程，从“LLM辅助”转变为“LLM中心化”，以解决现有LLM方法存在的误报率高、幻觉、推理深度有限和token消耗大等问题。

**整体框架与核心方法**：Argus框架包含两大核心组件：1）**RAG增强的完整供应链分析**，用于识别漏洞接收点（Sink）；2）**基于Re³方法的数据流分析**，用于构建从污染源（Source）到接收点的完整数据流。其工作流程是：首先解析代码库及其第三方依赖，检索相关的已知漏洞信息；然后为疑似漏洞生成概念验证（PoC）和修复方案；接着利用CodeQL进行接收点识别，并应用Re³方法进行全面的数据流提取；最终生成包含所有检测到的漏洞、数据流和验证细节的详细报告。

**主要模块与创新点**：
1.  **供应链分析与RAG智能体**：创新性地将依赖项解析和检索增强生成（RAG）深度整合。框架不仅分析项目源代码，还主动解析项目依赖（如pom.xml），并通过RAG智能体并行查询权威漏洞数据库（如NVD、OSV）和社区资源，汇总成结构化漏洞信息。这解决了传统方法忽视供应链安全的弊端。
2.  **PoC生成与验证智能体**：采用ReAct范式，引导LLM逐步推理漏洞根因、攻击场景，并生成可触发漏洞的源代码（PoC）及补丁。此过程不仅验证了已知漏洞的可利用性，其生成的PoC和上下文也为后续发现零日漏洞提供了关键启发。
3.  **Re³数据流分析工作流**：这是解决数据流分析中“隐蔽中断”问题的关键技术创新。它包含三个阶段：
    *   **检索**：首先使用CodeQL进行常规的前向数据流分析。
    *   **递归**：对于前向分析无法到达的接收点，引入“反向-前向”机制。从接收点开始反向追踪函数调用链直至最上游，将这些上游点作为新的代理接收点再进行前向分析，从而桥接因反射、多线程等高级语言特性导致的中断。
    *   **审查**：最后使用专用的LLM智能体对候选漏洞数据流进行两步审核：先进行端到端可达性分析，判断控制流或异常处理是否中断了数据流；再进行逐跳分析，细致验证每一步中污点是否被净化或编码。这极大地减少了误报。

**架构设计**：整个系统以多智能体协同工作为核心设计理念。不同的智能体（如RAG检索智能体、PoC生成智能体、审查智能体）各司其职，并通过结构化信息流进行协作，将LLM的上下文推理能力、外部知识库的准确信息以及传统静态分析工具（如CodeQL）的精确数据流挖掘能力有机融合，形成了一个高效、准确且可解释的漏洞检测流水线。

### Q4: 论文做了哪些实验？

该论文在静态应用安全测试（SAST）领域进行了全面的实验评估。实验设置以Java代码库为例，选取了七个流行且规模较大的开源项目作为评估数据集，包括PublicCMS、JeecgBoot、Ruoyi、JSPWiki、DataGear、Yudao-Cloud和KeyCloak。这些代码库的代码行数（LoC）均超过10万行，GitHub星标和提交数众多，具有工业级代表性。

对比方法选择了两个基线：专门针对Java的漏洞检测框架IRIS，以及知名的SAST工具CodeQL。评估指标主要包括检测到的漏洞数量（# Vuln.）、检测到的漏洞汇点数量（# Sinks）以及LLM API的令牌消耗量（Tokens），以衡量方法的有效性和计算效率。

主要结果如下：在端到端漏洞检测评估中，Argus显著优于基线。CodeQL在所有代码库中均未检测到任何漏洞（# Vuln. = 0）。IRIS仅在JSPWiki上检测到1个漏洞，在其他代码库上为0。而Argus（使用Claude-Sonnet-3.5或4.5）成功检测到了多个漏洞，例如在PublicCMS上检测到6个，在JSPWiki上检测到5个。关键数据指标显示，Argus检测到的漏洞总数远超基线。在令牌消耗方面，Argus虽然消耗更多令牌（例如在KeyCloak上消耗约44.2万令牌），但成功发现了漏洞（2个），而IRIS消耗较少令牌（约5.76万）却未发现任何漏洞，突显了Argus在有效性与成本间的优势。此外，消融研究表明，通过RAG机制发现的额外汇点（Extra Sinks）对漏洞检测有重要贡献，例如在DataGear上，RAG发现的1个额外汇点导致了3个漏洞的发现。

### Q5: 有什么可以进一步探索的点？

本文提出的Argus系统在静态污点分析方面表现出色，但仍有进一步探索的空间。局限性主要体现在两方面：一是仅依赖静态分析，未结合动态检测技术（如模糊测试），未来可探索静动态结合的混合分析方法，以提升漏洞检测的覆盖率和准确性；二是多智能体框架的优化潜力尚未充分挖掘，例如可通过强化学习对智能体进行微调，以漏洞发现准确性和数据流完整性作为奖励信号，提升协同效率。此外，结合领域知识图谱增强RAG的检索精度、设计轻量化模型以降低计算成本、拓展至更多漏洞类型（如逻辑漏洞）也是值得探索的方向。这些改进有望推动基于LLM的SAST工具在工业场景中的实际落地。

### Q6: 总结一下论文的主要内容

该论文提出了一种全新的静态应用安全测试范式，通过构建一个名为Argus的多智能体集成框架，将传统以LLM为辅助工具的流程重构为以LLM为中心的完整工作流。其核心贡献在于解决了现有LLM方法在漏洞检测中存在的误报率高、幻觉、推理深度有限和令牌消耗大等问题。Argus框架融合了三个关键创新：全面的软件供应链分析、协作式多智能体工作流，以及集成检索增强生成和ReAct等先进技术以增强推理并减少幻觉。实验表明，Argus能够显著超越现有方法，检测出更多真实漏洞（包括多个已获CVE编号的零日漏洞），同时有效降低误报率和运营成本，为工业级部署提供了实用高效的解决方案。
