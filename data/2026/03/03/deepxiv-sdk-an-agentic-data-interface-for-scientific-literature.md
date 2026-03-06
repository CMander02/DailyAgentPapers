---
title: "DeepXiv-SDK: An Agentic Data Interface for Scientific Literature"
authors:
  - "Hongjin Qian"
  - "Ziyi Xia"
  - "Ze Liu"
  - "Jianlyu Chen"
  - "Kun Luo"
  - "Minghao Qin"
  - "Chaofan Li"
  - "Lei Xiong"
  - "Junwei Lan"
  - "Sen Wang"
  - "Zhengyang Liang"
  - "Yingxia Shao"
  - "Defu Lian"
  - "Zheng Liu"
date: "2026-02-14"
arxiv_id: "2603.00084"
arxiv_url: "https://arxiv.org/abs/2603.00084"
pdf_url: "https://arxiv.org/pdf/2603.00084v2"
github_url: "https://github.com/DeepXiv/deepxiv_sdk"
categories:
  - "cs.DL"
  - "cs.AI"
  - "cs.CL"
  - "cs.IR"
tags:
  - "Agent Tools"
  - "Agent Data Interface"
  - "Scientific Literature"
  - "Agent Efficiency"
  - "Agentic Workflow"
  - "Data Retrieval"
relevance_score: 8.0
---

# DeepXiv-SDK: An Agentic Data Interface for Scientific Literature

## 原始摘要

LLM-agents are increasingly used to accelerate the progress of scientific research. Yet a persistent bottleneck is data access: agents not only lack readily available tools for retrieval, but also have to work with unstrcutured, human-centric data on the Internet, such as HTML web-pages and PDF files, leading to excessive token consumption, limit working efficiency, and brittle evidence look-up. This gap motivates the development of \textit{an agentic data interface}, which is designed to enable agents to access and utilize scientific literature in a more effective, efficient, and cost-aware manner.
  In this paper, we introduce DeepXiv-SDK, which offers a three-layer agentic data interface for scientific literature. 1) Data Layer, which transforms unstructured, human-centric data into normalized and structured representations in JSON format, improving data usability and enabling progressive accessibility of the data. 2) Service Layer, which presents readily available tools for data access and ad-hoc retrieval. It also enables a rich form of agent usage, including CLI, MCP, and Python SDK. 3) Application Layer, which creates a built-in agent, packaging basic tools from the service layer to support complex data access demands.
  DeepXiv-SDK currently supports the complete ArXiv corpus, and is synchronized daily to incorporate new releases. It is designed to extend to all common open-access corpora, such as PubMed Central, bioRxiv, medRxiv, and chemRxiv. We release RESTful APIs, an open-source Python SDK, and a web demo showcasing deep search and deep research workflows. DeepXiv-SDK is free to use with registration.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于LLM的智能体（AI Agent）在科学研究场景中访问和利用科学文献时面临的数据接口瓶颈问题。研究背景是，LLM智能体正被广泛用于加速科研进程，其核心工作流程依赖于对学术文献的可靠访问，包括快速识别相关论文、导航长文档以及检索可验证的证据。然而，现有方法存在明显不足：当前常见的流程是临时性地使用通用搜索引擎，获取PDF或HTML格式的论文，再启发式地提取文本，并将大段非结构化内容喂给智能体。这种方法效率低下且脆弱，因为它需要反复进行大量解析，依赖于文档特定的格式，缺乏跨领域和出版物的标准化接口，导致中间表示难以跨任务复用，并且智能体必须在没有明确结构、成本或证据范围概念的情况下处理噪声文本。

因此，本文要解决的核心问题是：如何为科研智能体设计一个**智能化的数据接口**，以更有效、高效且具有成本意识的方式访问和利用科学文献。具体而言，该接口需要实现三个目标：一是提供**结构化、规范化**的表示，使智能体能够通过一致的协议访问元数据、文档结构和证据；二是支持**渐进式披露**，提供从粗到细的数据视图，让智能体在支付完整上下文成本之前决定阅读内容和深度，从而降低认知负担和不必要的token消耗；三是具备**面向检索和条件过滤**的能力，使智能体能够根据多属性组合约束定位和筛选论文，并路由到最相关的部分。为此，论文提出了DeepXiv-SDK系统，通过数据层、服务层和应用层的三层架构来实现这一智能数据接口，以提升智能体在科研任务中的工作效率和输出质量。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和平台类。

在方法类工作中，随着LLM智能体日益依赖工具使用和多步交互，数据访问成为能力扩展的瓶颈。因此，一系列研究主张将原始的网页、PDF等非结构化数据，转化为具有规范化模式、可控视图和溯源信息的结构化、可被智能体调用的接口，以减少临时解析并提高可靠性。

在应用类工作中，针对科学文献领域，已有许多研究专注于开发智能体框架或网络平台，旨在提升文献综述效率。这些工作通常实现了“先搜索后阅读”的工作流、迭代式总结或多文档问答等功能，但它们普遍没有提供一个可复用的、智能体能在不同任务中确定性调用的数据接口API。

在平台类工作中，与本文理念最接近的是ar5iv和AlphaXiv。它们通过将arXiv论文转换为可读的HTML格式并提供增强视图，改善了用户的浏览体验。然而，这些系统本质上被视为面向人类浏览的高级arXiv镜像，而非专为智能体设计的、可通过可复用API进行扩展、支持渐进式且预算可控访问的“智能体数据接口”。

本文提出的DeepXiv-SDK与上述工作的核心区别在于，它明确设计了一个三层级的智能体数据接口，不仅将数据标准化为JSON格式，还提供了即用型工具和内置智能体，并特别强调了渐进式、预算感知的访问模式，使智能体能够进行低成本筛选、选择性阅读和按需验证。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为DeepXiv-SDK的三层智能体数据接口来解决科学文献数据访问的瓶颈问题。其核心方法是**将非结构化、面向人类的文献数据（如PDF/HTML）转化为规范化、结构化的JSON表示，并提供渐进式访问、混合检索和可直接调用的工具**，从而提升智能体处理文献的效率、效果和成本可控性。

**整体框架与主要模块**：
系统包含三个紧密协作的层次：
1.  **数据层**：负责数据的规范化、结构化和信号富集。其处理流水线是确定性的：给定arXiv ID，首先通过OAI-PMH获取官方元数据，然后获取HTML或PDF源文件，并使用MinerU等工具将其统一转换为以文本为中心的Markdown格式。接着，通过检测标题线索和格式规律，恢复文档结构，构建有序的章节清单，并将文本分割为章节级有效载荷。最终输出一个具有固定模式的规范JSON对象，包含论文级字段和显式的章节映射。在此基础上，该层还计算并物化了多种信号，包括用于成本控制的**预算提示**（如全局和章节级的token/长度统计）、轻量级语义信号（如论文预览摘要和章节摘要）、通过正则表达式和LLM验证提取的**资源链接**，以及可选的**学术上下文**（如引用数据）和**社会关注度**信号。这些内容被物化为三种视图：用于筛选和路由的**概览视图**、用于章节寻址导航的**章节视图**，以及用于验证的包含完整内容的**证据视图**。

2.  **服务层**：将数据层的产物转化为稳定、成本可控的接口供智能体调用。它通过统一的REST服务暴露核心能力：一是支持**渐进式访问**，提供信息密度和成本递增的结构化视图（概览、预览、章节、全文）；二是提供**混合检索**（词法+稠密）并支持属性条件过滤，使智能体能在深度阅读前构建和精炼候选论文集。该层还通过Redis缓存、按需加载和用量端点来确保性能和可审计性。为了降低集成摩擦，服务层提供了三种绑定到同一REST协议的轻量级客户端：**Python SDK**、**MCP连接器**（将端点注册为智能体运行时的工具原语）和**CLI**。

3.  **应用层**：将服务层的原语打包成面向开发者和智能体的工具。它提供了一个轻量级Python SDK，封装了检索和渐进式阅读的确定性调用。更重要的是，它内置了一个**专用于论文深度研究的智能体**。该智能体可以自动执行检索候选、通过低成本视图筛选、路由到相关章节、仅在需要验证时才升级到证据级阅读的完整工作流。该层具体展示了两个典型工作流：侧重于通过混合检索和元数据进行候选集构建、过滤和排序的**深度搜索**，以及侧重于通过迭代式章节阅读来提取实验设置和结果、并生成跨论文的证据链接摘要或对比表的**深度研究**。

**创新点**：
*   **结构化与信号富集**：将异构文献源统一为模式稳定的、章节可寻址的规范JSON表示，并预计算了预算提示、摘要、资源链接等多类机器可消费信号，从根本上避免了每个智能体流水线重复解析。
*   **渐进式与成本可控访问**：设计了从低成本的概览/预览，到章节级，再到完整证据级的显式升级路径，使智能体能根据任务需要精确控制阅读成本和token消耗。
*   **协议化与多模态接口**：通过统一的REST协议和Python SDK、MCP、CLI三种客户端，使接口兼具模块化、可重用性和易集成性。
*   **内置智能体与示范工作流**：不仅提供底层接口，还封装了一个能自动执行复杂文献处理流程的内置智能体，并通过“深度搜索”和“深度研究”两个端到端工作流具体展示了其能力。

### Q4: 论文做了哪些实验？

论文进行了三类实验：1）多约束条件下的智能体论文检索；2）深度研究（复杂证据问答）；3）服务延迟与缓存基准测试。

**实验设置与数据集**：针对检索任务，构建了包含50个多条件查询的评估集，每个查询对应唯一目标论文。针对深度研究任务，构建了47个需要聚合和验证论文证据的复杂问答查询（例如涉及时间范围的最新基准结果问题）。延迟测试则基于1,000个arXiv ID，并发数为16。

**对比方法**：在检索任务中，对比了Google Scholar、Google Scholar Labs、alpXiv、PASA和ASTA五个具备智能体搜索能力的学术平台。在深度研究任务中，对比了传统的“搜索+阅读”流程（使用Google Search检索和Jina Reader阅读全文）与基于DeepXiv-SDK的流程（使用属性条件检索和渐进式访问）。

**主要结果与关键指标**：
- **检索任务**：DeepXiv在Recall@1和Recall@10上均优于基线，且延迟显著更低。具体而言，其智能体深度搜索的端到端延迟远低于依赖全文验证的系统（如PASA和alpXiv）。
- **深度研究任务**：基于DeepXiv的流程在降低成本和延迟的同时，提高了答案质量。它通过渐进式访问（先使用低成本的头信息/预览信号筛选，仅在必要时读取具体章节或证据）避免了默认的全文摄入，从而减少了令牌消耗和运行时间。
- **延迟与缓存**：服务在负载下保持交互性。缓存提供了可靠的加速，例如预览端点的本地缓存加速比达到3.36倍。与传统的“获取+解析”基线（每篇论文平均7.20秒）相比，DeepXiv-SDK实现了显著的端到端加速，例如，对于缓存的json端点访问，本地加速54.6倍，远程加速39.6倍。关键延迟数据包括：本地暖缓存下，json端点平均延迟131.89毫秒，预览端点30.39毫秒；远程暖缓存下，json端点181.63毫秒。

### Q5: 有什么可以进一步探索的点？

该论文提出的DeepXiv-SDK在结构化科学文献数据、提供分层接口方面具有创新性，但仍存在一些局限性和可进一步探索的方向。首先，其当前主要覆盖arXiv，虽计划扩展至其他开放获取库，但如何统一处理不同学科、不同出版格式（如专利、数据集文档）的异构数据仍具挑战性。其次，系统依赖于预定义的结构化JSON表示，可能无法灵活适应未来新型文献元素（如交互图表、动态内容）。未来研究可探索自适应数据模式，使接口能动态学习并纳入新的文献结构。此外，论文强调效率与成本，但未深入讨论多智能体协作场景下的数据访问控制、版本一致性及溯源机制，这在分布式科研环境中至关重要。另一个方向是增强接口的“主动性”，例如通过预测智能体的信息需求，主动推送相关证据或矛盾观点，而不仅是被动响应查询。最后，评估目前侧重于检索和问答任务，未来可测试其在更复杂工作流（如假设生成、实验设计）中的效用，并探索与实验数据平台、代码仓库的深度集成，以构建端到端的科研智能体生态系统。

### Q6: 总结一下论文的主要内容

该论文针对LLM智能体在科学研究中面临的数据访问瓶颈问题，提出了DeepXiv-SDK这一面向科学文献的智能体数据接口。核心问题是现有流程通常将论文视为原始的PDF/HTML文件，导致全文摄入成本高昂且证据查找脆弱。论文的核心贡献是设计了一个三层架构的接口：数据层将非结构化的人类中心数据转换为规范化的JSON格式表示，实现渐进式访问；服务层提供即用的数据访问和即席检索工具，支持CLI、MCP和Python SDK等多种智能体使用方式；应用层则内置了一个封装基础工具的智能体，以支持复杂的数据访问需求。主要结论是，DeepXiv-SDK通过将论文表示为可工具调用的对象，并结合混合属性条件检索，能够实现更经济的筛选、更有选择性的章节阅读以及按需验证，从而在AI4Science工作流中提高了效率并增强了证据基础。该系统已支持完整的arXiv语料库并每日同步，旨在未来扩展到其他开放获取资源。
