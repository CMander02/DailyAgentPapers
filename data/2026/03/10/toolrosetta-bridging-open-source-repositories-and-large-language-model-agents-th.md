---
title: "ToolRosetta: Bridging Open-Source Repositories and Large Language Model Agents through Automated Tool Standardization"
authors:
  - "Shimin Di"
  - "Xujie Yuan"
  - "Hanghui Guo"
  - "Chaoqian Ouyang"
  - "Zhangze Chen"
  - "Ling Yue"
  - "Libin Zheng"
  - "Jia Zhu"
  - "Shaowu Pan"
  - "Jian Yin"
  - "Min-Ling Zhang"
  - "Yong Rui"
date: "2026-03-10"
arxiv_id: "2603.09290"
arxiv_url: "https://arxiv.org/abs/2603.09290"
pdf_url: "https://arxiv.org/pdf/2603.09290v1"
categories:
  - "cs.SE"
  - "cs.CE"
  - "cs.MA"
tags:
  - "Tool Standardization"
  - "Automated Tool Synthesis"
  - "Model Context Protocol (MCP)"
  - "Code Repository Integration"
  - "Tool-Using Agent"
  - "Agent Framework"
  - "End-to-End Task Completion"
  - "Security Inspection"
  - "Scientific Computing"
relevance_score: 8.5
---

# ToolRosetta: Bridging Open-Source Repositories and Large Language Model Agents through Automated Tool Standardization

## 原始摘要

Reusing and invoking existing code remains costly and unreliable, as most practical tools are embedded in heterogeneous code repositories and lack standardized, executable interfaces. Although large language models (LLMs) and Model Context Protocol (MCP)-based tool invocation frameworks enable natural language task execution, current approaches rely heavily on manual tool curation and standardization, which fundamentally limits scalability. In this paper, we propose ToolRosetta, a unified framework that automatically translates open-source code repositories and APIs into MCP-compatible tools that can be reliably invoked by LLMs. Given a user task, ToolRosetta autonomously plans toolchains, identifies relevant codebases, and converts them into executable MCP services, enabling end-to-end task completion with minimal human intervention. In addition, ToolRosetta incorporates a security inspection layer to mitigate risks inherent in executing arbitrary code. Extensive experiments across diverse scientific domains demonstrate that ToolRosetta can automatically standardize a large number of open-source tools and reduce the human effort required for code reproduction and deployment. Notably, by seamlessly leveraging specialized open-source tools, ToolRosetta-powered agents consistently improve task completion performance compared to commercial LLMs and existing agent systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在调用外部工具时面临的核心瓶颈：现有大量有价值的开源代码库和API接口缺乏标准化、可执行的工具化封装，导致工具调用成功率低，且人工进行标准化封装成本高昂、难以扩展，严重限制了基于LLM的智能体系统的规模化应用。

研究背景是，随着LLM的发展，让其调用外部工具来完成复杂任务已成为新范式，特别是基于模型上下文协议（MCP）的工具调用框架，能够降低使用门槛。然而，当前绝大多数实用的工具都深嵌在GitHub等平台的异构代码仓库中，存在接口不一、依赖复杂等问题，LLM直接调用成功率低。现有的MCP工具几乎完全依赖人工逐个封装，这种重度依赖人力的模式从根本上制约了工具生态的扩展性。

现有方法的不足在于，无论是提供代码理解环境还是依赖固定、人工整理的工具集，都未能自动化地将海量、异构的现有代码资源转化为LLM可直接可靠调用的标准化工具。这导致构建工具链的过程又回到了代码工程原有的痛点：成本高、复用慢。

因此，本文要解决的核心问题是：如何实现自动化、可扩展的开源工具标准化，以桥接海量开源仓库与LLM智能体。具体而言，论文提出了ToolRosetta框架，其核心目标是自动将开源代码库和API转换为MCP兼容的工具，并能够根据用户任务自动规划工具链、识别相关代码库、完成转换与安全审查，从而实现端到端的任务自动化完成，极大减少人工干预，突破工具标准化与规模化应用的瓶颈。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和标准化协议类。

在**方法类**研究中，早期工作如HuggingGPT、ToolFormer和ToolLLM致力于让大语言模型（LLM）调用外部工具来完成任务，但它们通常依赖于预定义的工具集。后续面向科学领域的智能体，如ChemCrow、Coscientist和SciToolAgent，进一步探索了跨学科的工具调用。然而，这些方法大多需要人工筛选和封装工具，可扩展性受限。本文提出的ToolRosetta与这些工作的核心区别在于，它实现了从开源代码库到可执行工具的**全自动化标准化转换**，无需人工干预，从而解决了规模化瓶颈。

在**应用与平台类**研究中，存在如GitHub Codespaces这类提供可执行开发环境的平台，以及GitMCP、GitHub MCP Server等帮助模型理解仓库内容的系统。但这些方案仍停留在代码理解层面，并未自动将代码转化为可供LLM直接调用的标准化工具。ToolRosetta则向前迈进了一步，完成了从“理解代码”到“生成可调用工具服务”的自动化流程。

在**标准化协议类**方面，Model Context Protocol (MCP) 已成为由OpenAI等机构推动的工具调用新范式，催生了如Manus、OpenClaw等基于MCP的系统。这些系统虽然降低了使用门槛，但其工具库的构建依然严重依赖人工封装。ToolRosetta的贡献在于，它正是针对MCP这一新兴范式，提供了**自动化、规模化生成MCP兼容工具**的解决方案，从而填补了海量非标工具与有限人工封装能力之间的根本矛盾。此外，ToolRosetta还引入了现有工作中较少强调的**安全审查层**，以规避自动化过程中执行任意代码的风险。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为ToolRosetta的自动化框架来解决开源代码库与LLM智能体之间工具标准化和调用的问题。其核心方法是构建一个端到端的系统，能够自动将分散、异构的开源代码仓库转化为标准化、可执行的工具，并集成到基于模型上下文协议（MCP）的LLM智能体框架中，从而实现任务的自动化规划与执行。

**整体框架与主要模块**：
ToolRosetta的架构围绕三个核心智能体组件进行设计：
1.  **工具搜索智能体（Tool-search Agent）**：负责从海量开源库中自动发现与用户查询相关的工具。其工作流程包括：（1）**查询解析与主题生成**：利用LLM对用户查询进行语义解析，提取关键词用于搜索。（2）**仓库检索与查询优化**：调用GitHub API搜索相关仓库，若结果不佳则通过LLM优化查询以提升召回率。（3）**仓库有效性评估**：对候选仓库进行结构化评估，检查代码完整性（如环境配置、依赖描述）和功能相关性，筛选出最合适的仓库。
2.  **MCP构建智能体（MCP-construction Agent）**：这是实现自动标准化的核心模块，负责将选定的GitHub仓库转换为统一的MCP服务。它遵循一个多节点的自动化流水线：
    *   **下载节点（Download Node）**：克隆仓库到本地。
    *   **分析节点（Analysis Node）**：利用DeepWiki等工具对源代码和README进行深度语义分析，生成结构化的**代码报告（Code Report）**，明确模块功能与调用关系。
    *   **环境节点（Env Node）**：自动识别并配置Python运行环境及依赖包。
    *   **生成节点（Generate Node）**：基于代码报告，利用LLM生成完整的MCP服务代码文件（如`main.py`, `mcp_service.py`）。其关键设计是将核心业务逻辑封装在**适配器模块（Adapter）** 中，并重构为异步格式以支持并发；MCP工具层则保持轻量，仅负责参数转发。
    *   **代码检查节点（Code_check Node）**、**运行节点（Run Node）**、**审查节点（Review Node）** 等后续节点负责代码安全检查、服务测试与功能验证，确保生成的工具可靠可用。
3.  **规划智能体（Planning Agent）**：在工具标准化后，该组件负责针对用户任务，自动规划调用这些MCP工具的执行链（toolchains），以完成端到端的任务。

**创新点与关键技术**：
1.  **全自动化的工具标准化流水线**：这是最核心的创新。系统无需人工干预，即可完成从仓库发现、分析、环境配置到MCP服务代码生成与测试的全过程，从根本上解决了手动标准化带来的可扩展性瓶颈。
2.  **深度代码语义理解与结构化报告生成**：通过DeepWiki等技术对代码库进行细粒度分析，生成包含功能、依赖和逻辑关系的结构化代码报告，为后续的自动代码生成提供了精确的蓝图。
3.  **安全的适配器封装与异步化设计**：将原始仓库代码的核心功能封装在独立的适配器模块中，并进行异步化重构。这种设计既隔离了原始代码的执行风险，又通过MCP标准接口提供了轻量、高效的调用方式，同时提升了系统并发处理能力。
4.  **集成安全审查层**：在整个MCP构建流程中嵌入了代码检查和运行验证节点，用于缓解执行任意代码的潜在安全风险，增强了系统的可靠性。

综上所述，ToolRosetta通过整合智能搜索、自动化代码理解与转换、以及安全执行机制，构建了一个能够将庞大而杂乱的开源生态无缝接入LLM智能体系统的桥梁，显著降低了代码复用与部署的人力成本。

### Q4: 论文做了哪些实验？

论文实验主要包括自动化工具转换性能评估和下游任务解决能力评估两部分。

**实验设置与数据集**：在工具转换评估中，使用来自RosettaEval基准的122个GitHub仓库，涵盖物理科学、地球与环境科学、生物科学、健康科学、科学社区与社会以及计算机科学六大领域的35个子学科。在下游任务评估中，使用包含387个任务的RosettaEval基准，覆盖相同的领域和子学科。

**对比方法**：在转换实验中，对比了ToolRosetta（首轮转换）、人类编码工程师以及仅生成MCP_service.py的GPT-4o服务基线。在下游任务实验中，对比了四个代表性的智能体系统：SciToolAgent（专家策划工具集）、ChemCrow（化学领域专用）、RepoMaster和OpenAgents（直接理解与执行仓库）。

**主要结果与关键指标**：
1.  **工具转换性能**：ToolRosetta的首轮转换成功率为53.0%（122个仓库），低于人类的82.9%，但高于GPT-4o服务基线的49.6%。若要求GPT-4o端到端生成完整栈，成功率骤降至3.3%。ToolRosetta在健康科学（70.9%）和计算机科学（66.7%）领域表现最佳。其转换速度极快，平均每个仓库约210.1秒，相比人类的1589.4秒（26.5分钟）减少了86.8%，提速7.6倍。通过Review-Revise-Fix修复机制，三轮修复后成功率从53.0%提升至68.4%。
2.  **下游任务性能**：ToolRosetta在六大科学领域的宏观平均任务完成准确率为55.6%，在35个子学科的平均准确率为52.1%。在六个类别中的五个（物理科学65.8%、地球与环境科学62.2%、健康科学61.0%、科学社区与社会60.4%、计算机科学44.0%）排名第一，仅在生物科学（40.2%）略低于SciToolAgent（47.3%）。其在21个分布外子学科的优势尤为明显，平均准确率达57.4%，远超其他基线（SciToolAgent 11.7%， ChemCrow 3.3%等）。
3.  **工具标准化效益**：将ToolRosetta转换的工具注入RepoMaster和OpenAgents后，两者性能均获提升：RepoMaster宏观平均类别准确率从24.2%升至34.8%（+10.6%），OpenAgents从22.0%升至35.4%（+13.4%）。

此外，论文还通过中风分析、物种预测和钙钛矿材料发现三个实际科学案例展示了系统的实用性。

### Q5: 有什么可以进一步探索的点？

本文提出的ToolRosetta框架在自动化工具标准化方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，框架目前主要支持Python代码库，而科学计算中广泛使用的R、C++等语言尚未覆盖，这限制了其应用范围。未来研究可扩展后端适配层，实现对多语言生态系统的支持，例如通过容器化或子进程桥接等方式集成其他语言的工具。

其次，环境重建是自动化转换的主要障碍，尤其是处理破损的远程依赖、平台特定配置和隐式系统状态假设时。当前的迭代自我修正无法完全解决这些问题，因为它们需要超越代码库本身的推理。未来可以探索结合更强大的代码理解模型、依赖关系图谱分析，甚至引入少量人类专家反馈的混合方法，以提高复杂环境的重建成功率。

此外，安全风险是开放生态工具引入的核心挑战。尽管论文提出了基于CIA三要素的防御机制，但如何平衡自动化效率与安全保证仍需进一步研究。例如，可以探索更细粒度的动态权限控制、基于形式化验证的接口安全性证明，或利用LLM进行漏洞代码的检测与修复。

最后，工具链的自动规划与组合优化仍有提升空间。当前框架在工具选择与序列生成上可能依赖相对简单的策略，未来可以集成更复杂的任务分解与规划算法，甚至利用强化学习来优化多步骤任务执行的可靠性与效率。这些改进将进一步提升智能体在开放世界任务中的自主性与实用性。

### Q6: 总结一下论文的主要内容

这篇论文提出了ToolRosetta框架，旨在解决大语言模型（LLM）智能体在调用开源代码工具时面临的标准化难题。核心问题是：大量实用工具嵌入在异构的代码仓库中，缺乏统一、可执行的接口，导致代码复用成本高、不可靠。现有基于MCP等框架的方法严重依赖人工进行工具的整理与标准化，限制了其扩展性。

为解决此问题，ToolRosetta设计了一个自动化框架。其主要方法是：给定用户任务后，框架能自动规划工具链，识别相关代码库，并将其自动转换为符合MCP标准的、可执行的服务。整个过程实现了端到端的任务完成，并包含安全审查层以降低执行任意代码的风险。

论文的核心贡献在于实现了从异构代码到标准化工具的自动“翻译”，显著减少了代码复现和部署所需的人力。实验表明，该框架能自动标准化大量开源工具，并且通过无缝利用这些专业工具，由ToolRosetta驱动的智能体在任务完成性能上持续优于商用大语言模型和现有智能体系统。其意义在于为构建可扩展、自动化的LLM工具调用生态系统提供了关键基础设施。
