---
title: "SODIUM: From Open Web Data to Queryable Databases"
authors:
  - "Chuxuan Hu"
  - "Philip Li"
  - "Maxwell Yang"
  - "Daniel Kang"
date: "2026-03-19"
arxiv_id: "2603.18447"
arxiv_url: "https://arxiv.org/abs/2603.18447"
pdf_url: "https://arxiv.org/pdf/2603.18447v1"
categories:
  - "cs.DB"
  - "cs.AI"
  - "cs.CL"
  - "cs.CV"
  - "cs.IR"
tags:
  - "Web Agent"
  - "Multi-Agent System"
  - "Information Extraction"
  - "Benchmark"
  - "Tool Use"
  - "Planning"
  - "Open Domain"
relevance_score: 8.0
---

# SODIUM: From Open Web Data to Queryable Databases

## 原始摘要

During research, domain experts often ask analytical questions whose answers require integrating data from a wide range of web sources. Thus, they must spend substantial effort searching, extracting, and organizing raw data before analysis can begin. We formalize this process as the SODIUM task, where we conceptualize open domains such as the web as latent databases that must be systematically instantiated to support downstream querying. Solving SODIUM requires (1) conducting in-depth and specialized exploration of the open web, which is further strengthened by (2) exploiting structural correlations for systematic information extraction and (3) integrating collected information into coherent, queryable database instances.
  To quantify the challenges in automating SODIUM, we construct SODIUM-Bench, a benchmark of 105 tasks derived from published academic papers across 6 domains, where systems are tasked with exploring the open web to collect and aggregate data from diverse sources into structured tables. Existing systems struggle with SODIUM tasks: we evaluate 6 advanced AI agents on SODIUM-Bench, with the strongest baseline achieving only 46.5% accuracy. To bridge this gap, we develop SODIUM-Agent, a multi-agent system composed of a web explorer and a cache manager. Powered by our proposed ATP-BFS algorithm and optimized through principled management of cached sources and navigation paths, SODIUM-Agent conducts deep and comprehensive web exploration and performs structurally coherent information extraction. SODIUM-Agent achieves 91.1% accuracy on SODIUM-Bench, outperforming the strongest baseline by approximately 2 times and the weakest by up to 73 times.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决领域专家在研究中面临的一个核心痛点：为了回答复杂的分析性问题，他们需要从开放网络（如各类官方网站、专业门户）中手动搜索、提取并整合分散在多层级、多来源网页中的原始数据，这一过程耗时耗力且难以自动化。研究背景是，尽管大语言模型和AI智能体在复杂推理和交互任务上取得了快速进展，但现有系统在处理这种需要深度、结构化探索开放网络以构建可查询数据库的任务时，仍存在明显不足。

现有方法的不足主要体现在三个方面：首先，现有的网络搜索工具和AI智能体（如WebVoyager）主要进行通用、浅层的网络探索，缺乏对特定专业网站进行深入、多层次导航的能力（即论文所述的“深度信息发现”能力C0）。其次，现有的信息检索或基于检索增强生成（RAG）的系统，其检索过程通常是独立进行的，忽略了不同数据项之间存在的结构性关联（如表格中行与列之间的依赖关系），未能利用这些规律来系统性地指导信息提取（即“利用跨单元格的结构相关性”能力E1）。最后，现有的基于LLM的数据管理系统通常假设输入数据已经是组织良好的结构化数据，从而绕过了从原始、异构的网络信息中整合并保证最终数据库内部一致性与可查询性的核心挑战（即“将信息组织成结构化数据库”能力E2）。

因此，本文要解决的核心问题是：如何自动化地将开放网络（视为潜在的数据库）中非结构化的、深度嵌套的数据，系统地实例化（Materialize）为结构化的、可查询的数据库实例，以支持下游分析。论文将此过程形式化为SODIUM任务，并开发了相应的基准测试SODIUM-Bench与智能体系统SODIUM-Agent来应对这一挑战。

### Q2: 有哪些相关研究？

本文提出的SODIUM任务主要与以下几类相关研究存在关联和区别：

**1. 信息检索与问答系统：**
传统的信息检索和开放域问答系统旨在直接回答用户问题，通常返回简短答案或相关文档片段。而SODIUM任务的目标是构建一个结构化的、可查询的数据库实例，这要求系统不仅能找到信息，还需进行深度探索、多源信息整合与结构化。本文的SODIUM-Agent通过深度网络探索和结构化信息提取，超越了传统问答的范畴。

**2. 网络信息提取与包装器生成：**
早期研究侧重于从特定网站（如产品列表页）提取结构化数据，通常依赖于预定义的包装器或模板。SODIUM任务面对的是开放域、深度嵌套且结构异构的网页（如政府统计网站），没有预定义的提取规则，要求系统能自主推理导航路径并发现相关数据源，其挑战性和自动化要求更高。

**3. 基于LLM的智能体与网络导航：**
近期工作探索了利用大型语言模型（LLM）驱动的智能体进行网络浏览和信息收集。本文评估的6个先进AI基线智能体即属此类。然而，这些现有系统在SODIUM-Bench上表现不佳（最强基线准确率仅46.5%），表明它们在处理需要深度、系统化探索和利用结构相关性进行优化的复杂任务时存在局限。SODIUM-Agent通过其多智能体架构、ATP-BFS算法以及对缓存资源和导航路径的原则性管理，显著提升了此类任务的性能。

**4. 基准测试与评估：**
在评测方面，现有基准多关注封闭域问答、表格理解或特定网站的简单提取任务。SODIUM-Bench则专注于从真实学术论文中衍生、需要跨多个深层网页进行探索和整合的复杂任务，涵盖了人口统计、经济学、体育等多个领域，从而为评估系统在开放网络环境中构建可查询数据库的能力提供了更贴近实际、更具挑战性的测试平台。

综上，SODIUM研究在任务定义、方法设计和评估基准上，与现有工作形成了明确的区分和推进，旨在解决从开放网络数据到可查询数据库的系统化、自动化构建这一更复杂的实际问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SODIUM-Agent的多智能体系统来解决从开放网络数据构建可查询数据库的问题。该系统由两个核心组件协同工作：**网络探索器**和**缓存管理器**，其整体框架设计类似于处理器-内存协同设计。

**核心方法与架构设计：**
1.  **整体框架**：系统以目标表格的单元格为单位进行填充。对于每个目标单元格，缓存管理器首先查询邻近单元格的缓存。若未命中，则从路径缓存中检索并生成一个排名的候选网页列表。网络探索器随后从这些初始网页出发，执行其核心算法进行探索和提取。
2.  **主要模块/组件**：
    *   **网络探索器**：作为系统的“处理单元”，负责执行主动的、深入的网页探索以提取信息。其核心是**ATP-BFS算法**，这是一种增强型广度优先搜索算法。该算法包含两个关键创新子模块：
        *   **页面探索器**：负责与单个网页交互。它能智能处理静态页面、动态页面（如含JavaScript、标签页、分页的页面）以及在线文档（PDF/图片）。对于动态页面，它采用多轮交互模式，通过`update_accessibility`和`click`等操作动态揭示隐藏内容，并具备**自我修正机制**以维护数据一致性。
        *   **链接处理器**：负责管理探索前沿。它实施“增强-选择-排序”三步策略：首先基于观察到的链接模式**增强**生成新的候选URL；然后在预算K内**选择**最相关的链接（平衡原始链接与增强链接）；最后根据查询、目标单元格和已有证据对链接进行**排序**，以确定下一层的探索顺序。
    *   **缓存管理器**：作为系统的“存储单元”，通过利用网站结构和单元格间的相关性来减少冗余计算。它维护两级缓存：
        *   **页面级缓存**：记录已成功提取值的源网页，便于同一页面信息的复用。
        *   **路径级缓存**：存储从根页面到目标页面的完整探索路径。当处理邻近单元格时，系统会检索并分析这些缓存路径，通过模式匹配和最小化编辑（如替换年份标识符）来生成新的候选起始URL，从而复用成功的导航模式。

**关键技术**：
*   **ATP-BFS算法**：结合了广度优先的覆盖性与基于增强、选择、排序的智能剪枝和导向，解决了传统BFS在网页探索中分支因子过大、目标深藏、链接无序等效率问题。
*   **动态页面交互机制**：通过构建页面特定的交互原语（MCP工具），使智能体能够系统地与复杂动态网页组件交互，以揭示全部内容。
*   **结构相关性利用**：缓存管理器深度挖掘并复用单元格间及网页间的结构依赖关系，将成功的局部探索路径推广到相似任务上，显著提升了探索的连贯性和效率。

**创新点**：
1.  将开放网络视为潜在数据库并系统化实例化的任务形式化（SODIUM任务）。
2.  提出了处理器-内存协同的多智能体架构，将主动探索（网络探索器）与经验复用（缓存管理器）解耦并紧密结合。
3.  设计了ATP-BFS算法及其内部的页面探索器与链接处理器，实现了对静态、动态及文档类网络资源的深度、全面且高效的探索。
4.  引入了基于结构相关性的两级缓存机制，特别是路径级缓存的复用，极大地优化了系统性能。

通过这些方法，SODIUM-Agent在SODIUM-Bench基准测试中取得了91.1%的准确率，远超现有基线系统。

### Q4: 论文做了哪些实验？

论文实验围绕SODIUM任务展开，旨在评估不同AI智能体从开放网络数据构建可查询数据库的能力。

**实验设置与数据集**：研究构建了SODIUM-Bench基准测试，包含从6个领域（如学术研究）的已发表论文中提取的105个任务。每个任务要求智能体探索开放网络，从多样化的来源收集和聚合数据，最终填充成一个结构化的表格。所有智能体（包括基线方法和提出的SODIUM-Agent）均在“逐单元格提取”的设置下运行，每次运行对应填充一个表格单元格，并提供已填充值作为上下文。实验使用GPT-5-2025-08-07作为提示模型，并为SODIUM-Agent设置探索宽度K=10。

**对比方法**：评估了6个具有先进网络搜索能力的先进AI智能体作为基线，包括：AG2、AutoGPT、AutoGen、OpenAI ResearchBot、Open Deep Research以及WebVoyager。这些基线方法代表了当前在模块化代理、自主目标分解、多代理对话、在线深度研究以及端到端网络导航等方面的前沿技术。

**主要结果与关键指标**：主要评估指标是任务级准确率（TaskAcc），即正确填充的单元格占表格总单元格数的百分比，并在所有任务上取平均。实验结果显示，现有基线系统在SODIUM任务上表现不佳，最强的基线（OpenAI ResearchBot）准确率仅为46.5%。相比之下，论文提出的SODIUM-Agent（一个由网络探索器和缓存管理器组成的多代理系统）取得了91.1%的准确率，性能约为最强基线的2倍，比最弱基线高出最多73倍。此外，论文还进行了组件分析和消融研究，以深入理解网络探索器和缓存管理器各自的贡献。

### Q5: 有什么可以进一步探索的点？

该论文提出的SODIUM任务和SODIUM-Agent系统在从开放网络构建可查询数据库方面取得了显著进展，但仍存在若干局限性和值得深入探索的方向。

首先，系统性能严重依赖大语言模型（如GPT-4o）作为语义判断和核心推理引擎，这带来了高计算成本、潜在偏差以及“黑箱”决策过程。未来研究可探索更轻量级、可解释的模型，或设计专门的模块来处理语义匹配和事实核查。

其次，SODIUM-Bench基准目前局限于6个学术领域，其任务和网络数据源可能无法完全代表现实世界中更嘈杂、动态且对抗性的网络环境（如社交媒体、暗网或商业网站）。未来的工作可以扩展基准的领域覆盖面和任务复杂度，例如纳入需要跨语言整合、处理多媒体内容或应对网站反爬机制的挑战性任务。

从方法学角度看，当前的ATP-BFS算法和缓存管理主要优化了探索的深度和广度，但对信息源的可靠性和时效性评估不足。一个重要的改进方向是引入可信度评估模块，对网络来源进行实时权威性、一致性和新鲜度评分，从而在数据集成时进行加权或过滤。此外，系统目前以构建静态表格为目标，而现实中的分析需求常常是动态的。未来可探索构建支持增量更新、版本管理和溯源查询的“活”数据库系统，使SODIUM-Agent能够持续监测数据变化并自动修订。

最后，多智能体间的协调机制仍有优化空间。当前架构相对固定，未来可研究更自适应、具备元认知能力的智能体，使其能根据任务难度动态调整探索策略，或在遭遇失败时自主诊断原因并切换解决方案。将这些能力与人类专家的反馈循环相结合，将能打造出更强大、更实用的网络数据助理。

### Q6: 总结一下论文的主要内容

该论文提出了SODIUM任务，旨在将开放网络数据自动转化为可查询的数据库，以支持领域专家的分析需求。核心贡献在于形式化了从开放网络探索到结构化数据整合的完整流程，并构建了SODIUM-Bench基准测试（包含6个领域的105个任务）来量化该任务的挑战性。论文指出现有AI系统在此任务上表现不佳，最强基线准确率仅为46.5%。

为解决此问题，作者开发了SODIUM-Agent多智能体系统，其方法主要包括：1）通过ATP-BFS算法进行深度、专业的网络探索；2）利用结构相关性进行系统化信息提取；3）通过缓存管理器优化已访问资源和导航路径的管理，以整合信息为连贯的可查询数据库实例。

主要结论显示，SODIUM-Agent在SODIUM-Bench上取得了91.1%的准确率，性能约为最强基线的两倍，显著优于现有系统。该研究的意义在于为自动化网络数据采集与结构化提供了系统化框架，并证明了通过算法优化和智能体协同可有效解决开放领域数据集成难题。
