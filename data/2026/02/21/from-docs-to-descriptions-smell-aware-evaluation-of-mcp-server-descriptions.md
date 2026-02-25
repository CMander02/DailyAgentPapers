---
title: "From Docs to Descriptions: Smell-Aware Evaluation of MCP Server Descriptions"
authors:
  - "Peiran Wang"
  - "Ying Li"
  - "Yuqiang Sun"
  - "Chengwei Liu"
  - "Yang Liu"
  - "Yuan Tian"
date: "2026-02-21"
arxiv_id: "2602.18914"
arxiv_url: "https://arxiv.org/abs/2602.18914"
pdf_url: "https://arxiv.org/pdf/2602.18914v1"
categories:
  - "cs.SE"
tags:
  - "Agent 评测/基准"
  - "工具使用"
  - "Agent 安全"
  - "MCP"
  - "软件工程"
relevance_score: 7.5
---

# From Docs to Descriptions: Smell-Aware Evaluation of MCP Server Descriptions

## 原始摘要

The Model Context Protocol (MCP) has rapidly become a de facto standard for connecting LLM-based agents with external tools via reusable MCP servers. In practice, however, server selection and onboarding rely heavily on free-text tool descriptions that are intentionally loosely constrained. Although this flexibility largely ensures the scalability of MCP servers, it also creates a reliability gap that descriptions often misrepresent or omit key semantics, increasing trial-and-error integration, degrading agent behavior, and potentially introducing security risks. To this end, we present the first systematic study of description smells in MCP tool descriptions and their impact on usability. Specifically, we synthesize software/API documentation practices and agentic tool-use requirements into a four-dimensional quality standard: accuracy, functionality, information completeness, and conciseness, covering 18 specific smell categories. Using this standard, we conducted a large-scale empirical study on a well-constructed dataset of 10,831 MCP servers. We find that description smells are pervasive (e.g., 73% repeated tool names, thousands with incorrect parameter semantics or missing return descriptions), reflecting a "code-first, description-last" pattern. Through a controlled mutation-based study, we show these smells significantly affect LLM tool selection, with functionality and accuracy having the largest effects (+11.6% and +8.8%, p < 0.001). In competitive settings with functionally equivalent servers, standard-compliant descriptions reach 72% selection probability (260% over a 20% baseline), demonstrating that smell-guided remediation yields substantial practical benefits. We release our labeled dataset and standards to support future work on reliable and secure MCP ecosystems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决模型上下文协议（MCP）生态系统中一个关键但尚未被系统研究的问题：MCP服务器工具描述的质量缺陷（即“描述异味”）及其对系统可用性和可靠性的负面影响。MCP作为连接AI智能体与外部工具的事实标准，其工具描述采用自由文本形式且约束宽松，这虽然保证了灵活性和可扩展性，但也导致了严重问题：描述常常错误表示或遗漏关键语义（如参数含义错误、缺少返回值说明）。这种“代码优先，描述最后”的模式使得用户和智能体在选择与集成服务器时严重依赖这些可能不准确或不完整的描述，从而增加了试错成本，降低了智能体行为效果，甚至可能引入安全风险。为此，论文首次对MCP工具描述中的异味进行了系统性研究，通过构建一个涵盖准确性、功能性、信息完整性和简洁性四个维度、18类具体异味的质量标准，并基于大规模数据集进行实证分析，量化了这些异味的存在普遍性及其对LLM工具选择行为的显著影响，最终证明了基于异味指导的描述修复能带来实质性的竞争优势。

### Q2: 有哪些相关研究？

本文的研究背景主要涉及大模型智能体（LLM-based agents）的工具使用（Tool Use）和模型上下文协议（Model Context Protocol, MCP）生态系统。相关工作可分为以下几类：

1.  **智能体工具使用与规划**：大量研究关注如何让LLM智能体有效调用外部工具，例如ReAct、Toolformer等工作探索了工具调用与推理的结合。本文聚焦于工具调用流程中一个更前置但关键的问题——**工具描述的质量**，这是现有研究较少系统探讨的。

2.  **API与工具描述标准化**：在传统软件工程中，API文档质量（如OpenAPI规范）和“代码异味”（code smell）研究已很成熟。同时，为LLM设计的工具调用框架，如OpenAI的函数调用格式、LangChain和Microsoft的Semantic Kernel，都定义了工具描述的元数据格式。本文的贡献在于，**首次将软件工程中的“异味”概念系统性地引入并适配到MCP工具描述领域**，建立了针对智能体工具选择的四维质量标准。

3.  **MCP生态系统研究**：MCP作为一种新兴的、开放的工具协议标准，其生态系统规模快速增长，但相关的学术研究尚处早期。本文是**首个对MCP生态系统进行大规模实证分析的研究**，构建了包含上万个服务器的数据集，揭示了实践中“代码优先，描述滞后”的普遍模式及其对工具选择可靠性的影响。

4.  **提示工程与描述优化**：已有工作研究如何为LLM编写有效的指令或提示（Prompt Engineering）。本文与之相关但视角不同，它关注的是**工具描述本身的质量缺陷（即“描述异味”）如何直接影响LLM的工具选择性能**，并通过受控实验量化了不同维度异味的影响。

综上，本文在智能体工具调用和软件工程文档质量的交叉领域做出了贡献。它借鉴了相关领域的理念，但针对MCP这一特定、开放且快速发展的生态系统，首次系统性地定义了描述异味、进行了大规模评估，并实证证明了优化描述对提升智能体工具选择准确性的显著价值。

### Q3: 论文如何解决这个问题？

论文通过构建一个系统性的MCP描述质量评估标准与实证研究来解决工具描述不可靠的问题。核心方法分为三个步骤：首先，通过文献综述与实证分析相结合的方式，建立了一个四维度的质量标准（准确性、功能性、信息完整性、简洁性），并细分为18种具体的“异味”类别。这一标准融合了传统软件工程原则（如ISO/IEC标准、API文档研究）和面向LLM智能体的独特需求（如机器可读性、上下文窗口限制）。

其次，研究团队构建了一个大规模数据集，包含10,831个真实世界的MCP服务器。他们通过AST（抽象语法树）模式匹配技术，从源代码中提取工具的描述与实现代码，形成“描述-代码”对，为分析提供了基础。

关键技术在于采用了一种**基于LLM的增量式卡片分类算法**来从海量数据中归纳问题模式。该算法迭代地处理每个“描述-代码”对：首先使用LLM识别描述与代码之间的具体不一致或遗漏问题；然后将每个识别出的问题与已有的问题类别进行语义相似度匹配；若相似度超过阈值，则归入现有类别，否则创建新的问题类别。这个过程将零散的、异质的问题系统化地归纳为可分类的“描述异味”税目。

最终，通过这一标准对大规模数据集进行实证分析，揭示了“代码优先，描述后补”的普遍模式及其对LLM工具选择性能的显著负面影响。研究表明，遵循该标准修复描述异味能大幅提升智能体选择的准确率，在竞争性场景下选择概率可从20%的基线提升至72%，验证了该解决方案的实用价值。

### Q4: 论文做了哪些实验？

该论文进行了两项核心实验。首先，研究者构建了一个包含10,831个MCP服务器的大型数据集，并基于提出的四维质量标准（准确性、功能性、信息完整性、简洁性）及其下的18个具体问题类别，对这些服务器的工具描述进行了大规模实证分析。实验发现描述“异味”普遍存在，例如73%的服务器存在工具名重复问题，数千个服务器存在参数语义错误或缺失返回值描述，反映出“代码优先、描述最后”的开发模式。

其次，论文通过一项受控的基于突变的实验，量化了这些描述异味对LLM工具选择的影响。实验设置是让LLM在功能等效的竞争性服务器中进行选择。结果显示，描述异味显著影响LLM的选择，其中功能性和准确性维度的缺陷影响最大，分别导致选择正确率变化+11.6%和+8.8%（p < 0.001）。主要结果是，符合标准的描述在竞争环境中的选择概率达到72%，相比20%的基线提升了260%，证明了消除描述异味能带来巨大的实际效益。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其评估标准主要基于静态文档分析，未能深入考察动态使用场景下描述缺陷的实际影响。例如，未测试不同LLM对同一缺陷的敏感度差异，也未研究智能体在多次试错后是否能自适应地绕过描述缺陷。此外，当前研究聚焦于描述本身的质量，未充分探讨自动化修复这些缺陷的技术路径。

未来方向可包括：1）开发自动化工具，能够从代码或API文档中直接生成高质量、无缺陷的MCP服务器描述，实现“描述即代码”；2）构建动态评估框架，在智能体实际工作流中量化描述缺陷对任务成功率、效率和安全性的实时影响；3）研究描述缺陷与智能体规划、推理能力的交互，探索能否通过增强智能体的元认知能力来缓解描述不准确带来的问题；4）将研究范围扩展到多智能体协作场景，考察描述质量如何影响服务器在复杂系统中的可靠集成与协同。

### Q6: 总结一下论文的主要内容

这篇论文首次系统性地研究了MCP（模型上下文协议）服务器工具描述中的“异味”问题及其对可用性的影响。作者将软件/API文档实践与智能体工具使用需求结合，提出了一个四维质量标准（准确性、功能性、信息完整性和简洁性），涵盖18类具体异味。通过对10,831个MCP服务器的大规模实证分析，研究发现描述异味普遍存在（如73%存在重复工具名、大量参数语义错误或缺失返回描述），反映出“代码优先、描述最后”的模式。通过受控的基于突变的研究，论文证明这些异味显著影响LLM的工具选择，其中功能性和准确性维度影响最大。在功能等效服务器的竞争环境中，符合标准的描述选择概率可达72%，远超基线。该研究为构建可靠、安全的MCP生态系统提供了重要标准和数据集，有助于减少集成试错、提升智能体行为并降低安全风险。
