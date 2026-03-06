---
title: "MOOSEnger -- a Domain-Specific AI Agent for the MOOSE Ecosystem"
authors:
  - "Mengnan Li"
  - "Jason Miller"
  - "Zachary Prince"
  - "Alexander Lindsay"
  - "Cody Permann"
date: "2026-03-05"
arxiv_id: "2603.04756"
arxiv_url: "https://arxiv.org/abs/2603.04756"
pdf_url: "https://arxiv.org/pdf/2603.04756v1"
categories:
  - "cs.AI"
  - "cs.CE"
  - "cs.SE"
tags:
  - "工具使用"
  - "检索增强生成"
  - "领域特定智能体"
  - "工作流自动化"
  - "智能体架构"
  - "智能体评测"
relevance_score: 8.0
---

# MOOSEnger -- a Domain-Specific AI Agent for the MOOSE Ecosystem

## 原始摘要

MOOSEnger is a tool-enabled AI agent tailored to the Multiphysics Object-Oriented Simulation Environment (MOOSE). MOOSE cases are specified in HIT ".i" input files; the large object catalog and strict syntax make initial setup and debugging slow. MOOSEnger offers a conversational workflow that turns natural-language intent into runnable inputs by combining retrieval-augmented generation over curated docs/examples with deterministic, MOOSE-aware parsing, validation, and execution tools. A core-plus-domain architecture separates reusable agent infrastructure (configuration, registries, tool dispatch, retrieval services, persistence, and evaluation) from a MOOSE plugin that adds HIT-based parsing, syntax-preserving ingestion of input files, and domain-specific utilities for input repair and checking. An input precheck pipeline removes hidden formatting artifacts, fixes malformed HIT structure with a bounded grammar-constrained loop, and resolves invalid object types via similarity search over an application syntax registry. Inputs are then validated and optionally smoke-tested with the MOOSE runtime in the loop via an MCP-backed execution backend (with local fallback), translating solver diagnostics into iterative verify-and-correct updates. Built-in evaluation reports RAG metrics (faithfulness, relevancy, context precision/recall) and end-to-end success by actual execution. On a 125-prompt benchmark spanning diffusion, transient heat conduction, solid mechanics, porous flow, and incompressible Navier--Stokes, MOOSEnger achieves a 0.93 execution pass rate versus 0.08 for an LLM-only baseline.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决使用MOOSE（多物理场面向对象模拟环境）框架进行科学计算时，用户面临的高门槛和低效率问题。MOOSE是一个强大的高性能多物理场模拟框架，广泛应用于核工程等领域，但其模拟案例需要通过严格的HIT格式“.i”输入文件来配置。由于MOOSE拥有庞大的对象目录和严格的语法规则，新用户学习曲线陡峭，即使是经验丰富的用户，在初始设置、语法调试以及确保输入文件语义正确性方面也需耗费大量时间，这严重阻碍了快速建立有效、可信的基准模型的工作流程。

现有的一些AI辅助科学计算工具（如MetaOpenFOAM）和基于大语言模型（LLM）的代码助手，虽然展示了通过自然语言交互和检索增强生成（RAG）来简化工作流程的潜力，但针对MOOSE生态系统的解决方案仍处于初级阶段。这些方法通常过度依赖RAG和提示工程，缺乏与MOOSE领域知识的深度、确定性集成。例如，它们可能无法有效处理MOOSE特有的HIT语法结构，或难以将模拟执行过程中的具体错误诊断转化为迭代修复动作，导致实用性有限。

因此，本文的核心问题是：如何构建一个深度集成、工具使能的领域专用AI智能体（Agent），以显著降低MOOSE模拟的设置与调试门槛，并提升整体工作效率。具体而言，MOOSEnger试图通过一个对话式工作流，将用户的自然语言意图直接转化为可运行的MOOSE输入文件。它不仅要利用RAG从文档和示例中获取知识，更要深度融合MOOSE感知的确定性工具链（包括HIT解析、语法保留的文件处理、基于语法的修复、对象类型验证等），并能在循环中调用MOOSE运行时进行验证和冒烟测试，将求解器诊断信息反馈给Agent以进行迭代修正。最终目标是实现“意图驱动建模”，帮助用户快速获得第一个成功运行的模拟，从而让工程师更专注于物理分析和探索，而非繁琐的手动配置与排错。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**方法类、应用类和评测类**。

在**方法类**中，相关工作主要围绕检索增强生成（RAG）和基于LLM的智能体。RAG被广泛用于将领域文档和示例作为上下文，以提高响应的准确性和减少幻觉，这是许多科学计算助手的基础技术。同时，像Claude Code和Codex这样的编码助手展示了通过迭代操作项目文件（如代码、测试）来将用户意图转化为可运行工件的交互模式。本文的MOOSEnger借鉴了这些核心思想，但与之区别在于，它并非仅依赖RAG和提示，而是强调与特定领域（MOOSE生态系统）的**深度集成**。它构建了一个包含确定性解析、验证和执行工具的完整工具链，实现了更紧密的“语言推理-仿真动作”闭环。

在**应用类**中，已有研究探索了AI智能体在科学计算软件中的具体应用。例如，MetaOpenFOAM和OpenFOAM-GPT用于计算流体动力学（CFD），将自然语言描述转化为OpenFOAM案例；AutoFLUKA用于辐射输运领域，简化蒙特卡罗输入准备。这些工作与MOOSEnger的目标相似，都是自动化工作流中的部分设置。本文明确提到了MooseAgent，它是一个用于自动化MOOSE仿真的多智能体框架。MOOSEnger与MooseAgent的主要区别在于**架构设计和集成深度**：MOOSEnger采用**单智能体、对话式设计**，强调在用户监督下的交互；它更深入地集成了MOOSE原生工具（如HIT解析器），并设计了专门的输入预检和修复管道，从而能更直接地利用领域结构进行迭代纠错。

在**评测类**中，相关工作通常关注任务完成度。本文不仅报告了端到端的执行成功率，还系统性地引入了**RAG质量指标**（如忠实度、相关性、上下文精确率/召回率），以评估检索和生成的质量，这为智能体在专业领域的可靠性评估提供了更细致的维度。

### Q3: 论文如何解决这个问题？

论文通过一个“核心+领域”的架构设计来解决MOOSE输入文件创建与调试困难的问题。其核心方法是将可复用的智能体基础设施与领域特定能力解耦，并构建一个结合检索增强生成（RAG）、确定性解析验证与执行的对话式工作流。

**整体框架与主要模块**：
系统采用分层架构。**核心层**提供稳定的运行时基础，包括插件加载器与注册表、提示词管理器、工具运行时、带标签的RAG管理器、工作区与会话状态管理。**领域插件层**（此处为MOOSE插件）则注入领域知识，包括提示词包、智能体配置文件、专用工具、技能以及数据导入管道。这种设计使得添加新领域无需修改核心代码。

**关键技术流程与创新点**：
1.  **MOOSE感知的文档导入与检索**：针对HIT格式的“.i”输入文件，创新性地使用`pyhit`解析器进行**语法保持的分块**。它将每个`[Block] ... []`语法块作为一个独立的检索单元，避免了传统文本分割导致的块结构断裂。同时，自动为每个块生成包含语法树信息的元数据，并利用LLM生成基于语法结构的输入文件摘要，极大提升了RAG的精准性和上下文相关性。

2.  **输入预检与修复管道**：这是一个关键创新，在运行模拟前对LLM生成的输入进行多层验证和修复：
    *   **确定性清理**：移除隐藏的格式字符。
    *   **语法感知的类型相似性搜索**：当输入中出现无效的MOOSE对象类型名时，系统会从应用语法注册表中进行相似性搜索，提供纠正建议。
    *   **语法约束的循环修复**：使用一个受限于HIT语法的循环来修复结构不良的输入。
    *   **复合预检工作流**：将上述步骤与语义检查串联，并可选择通过**MCP支持的后端执行**（备有本地回退方案）进行“冒烟测试”，将求解器诊断信息反馈给智能体进行迭代验证与修正。

3.  **工具化与执行集成**：智能体通过结构化工具调用来操作。MOOSE插件提供了领域专用工具，如输入解析、修复、检查和执行。执行被抽象到MCP后端，使得同一智能体循环能够验证、网格划分或运行输入，而无需更改核心运行时。

4.  **可观测性与评估**：系统内置评估功能，不仅报告RAG指标（如忠实度、相关性、上下文精确率/召回率），还通过实际执行来度量端到端的成功率，确保了解决方案的实用性和可靠性。

综上所述，MOOSEnger通过其创新的“核心+领域”架构、语法保持的RAG、多阶段输入预检修复管道以及与运行时深度集成的工具化执行，系统性地将自然语言意图转化为可正确运行的MOOSE输入，从而高效解决了MOOSE生态系统上手和调试慢的难题。

### Q4: 论文做了哪些实验？

论文在五个MOOSE物理问题家族（扩散、瞬态热传导、固体力学、多孔介质流动、不可压缩Navier-Stokes）上进行了实验，共包含125个自然语言提示。实验设置对比了两种模式：一是MOOSEnger的完整智能体模式，它结合了检索增强生成（RAG）以及MOOSE专用的输入文件清理、修复、验证工具和MCP执行后端；二是纯LLM基线模式，生成过程中不调用任何工具。评估的核心指标是端到端执行成功率，即最终生成的输入文件通过MOOSE运行时执行后退出码为0的比例。

主要结果显示，MOOSEnger取得了0.93（93%）的极高执行通过率，而纯LLM基线的通过率仅为0.08（8%），性能提升非常显著。除了这个关键指标，论文还报告了RAG相关的内部评估指标，包括忠实度、相关性、上下文精确率和召回率，以衡量生成过程的可靠性。实验过程具体展示了MOOSEnger的工作流程：它将自然语言请求分解为必要的输入块，起草输入文件，并通过其预处理流水线（清理隐藏格式、修复HIT结构、纠正无效对象类型）进行修正，再经MCP工具验证并执行轻量级试运行，最终返回可运行文件和建模选择的简要解释。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其高度领域特定性，目前主要针对MOOSE生态的HIT输入文件。其未来研究方向可首先拓展至更广泛的科学计算与工程仿真领域，例如支持FEniCS、OpenFOAM等其他框架，构建通用的科学计算智能体范式。其次，在技术层面，当前的语法修复与验证流程虽有效但可能效率受限，未来可探索更高效的纠错机制，例如引入强化学习进行迭代优化，或利用更细粒度的代码语法树分析。此外，评估基准虽包含多物理场案例，但可进一步增加复杂耦合场景与真实用户交互日志的测试，以提升智能体的鲁棒性与实用性。最后，可探索将智能体与交互式可视化、参数优化循环深度集成，形成从自然语言描述到仿真结果分析与优化的端到端自动化工作流。

### Q6: 总结一下论文的主要内容

该论文提出MOOSEnger，一个专为MOOSE多物理场仿真生态系统设计的AI智能体。核心问题是MOOSE输入文件（HIT格式）语法严格、对象库庞大，导致用户编写和调试效率低下。方法上，MOOSEnger采用“核心+领域插件”架构：核心层提供可复用的智能体基础设施（如工具调度、检索服务），MOOSE插件则集成领域专用的解析、验证与修复工具。其工作流程结合检索增强生成（RAG）与确定性工具链，首先通过语法约束循环和相似性搜索修复输入文件结构，再借助MCP执行后端进行验证与试运行，将求解器诊断反馈用于迭代修正。主要结论显示，在涵盖扩散、瞬态热传导、固体力学等125个提示的测试集上，MOOSEnger的端到端执行通过率达0.93，显著优于纯LLM基线的0.08。该研究的贡献在于为复杂仿真领域提供了可定制、工具增强的AI代理范式，有效提升了专业工作流的自动化与可靠性。
