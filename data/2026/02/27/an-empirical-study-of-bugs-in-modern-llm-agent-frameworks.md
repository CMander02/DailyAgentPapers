---
title: "An Empirical Study of Bugs in Modern LLM Agent Frameworks"
authors:
  - "Xinxue Zhu"
  - "Jiacong Wu"
  - "Xiaoyu Zhang"
  - "Tianlin Li"
  - "Yanzhou Mu"
date: "2026-02-25"
arxiv_id: "2602.21806"
arxiv_url: "https://arxiv.org/abs/2602.21806"
pdf_url: "https://arxiv.org/pdf/2602.21806v3"
categories:
  - "cs.SE"
tags:
  - "Architecture & Frameworks"
relevance_score: 7.5
taxonomy:
  capability:
    - "Architecture & Frameworks"
  domain: "General Purpose"
  research_type: "Empirical Study/Analysis"
attributes:
  base_model: "N/A"
  key_technique: "Empirical study and taxonomy construction for LLM agent framework bugs"
  primary_benchmark: "N/A"
---

# An Empirical Study of Bugs in Modern LLM Agent Frameworks

## 原始摘要

LLM agents have been widely adopted in real-world applications, relying on agent frameworks for workflow execution and multi-agent coordination. As these systems scale, understanding bugs in the underlying agent frameworks becomes critical. However, existing work mainly focuses on agent-level failures, overlooking framework-level bugs. To address this gap, we conduct an empirical study of 998 bug reports from CrewAI and LangChain, constructing a taxonomy of 15 root causes and 7 observable symptoms across five agent lifecycle stages: 'Agent Initialization','Perception', 'Self-Action', 'Mutual Interaction' and 'Evolution'. Our findings show that agent framework bugs mainly arise from 'API misuse', 'API incompatibility', and 'Documentation Desync', largely concentrated in the 'Self-Action' stage. Symptoms typically appear as 'Functional Error', 'Crash', and 'Build Failure', reflecting disruptions to task progression and control flow.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体框架中存在的缺陷（bug）问题，其核心是填补当前研究在框架层面缺陷分析上的空白。随着LLM能力的提升，智能体范式被广泛应用于需要长期规划和使用工具的任务中，而LangChain、CrewAI等智能体框架为开发此类应用提供了关键支持。然而，当这些底层框架出现缺陷时，问题会向上层系统传播并放大，导致执行错误、资源滥用和安全风险，对整个LLM软件供应链构成严重威胁。

现有研究主要关注智能体层面的失败，例如在推理、规划或行动过程中的行为偏差，通常通过行为分析或基准测试进行评估。这些工作虽然增进了对智能体行为和模型局限性的理解，但很大程度上忽视了根植于底层智能体框架本身的缺陷。近期虽有研究开始分析智能体库的缺陷，但其方法侧重于映射静态组件（如数据预处理）的拉取请求，忽略了智能体动态执行和时序工作流的特点。因此，LLM智能体框架的缺陷在动态的智能体生命周期中如何表现，仍然是一个未被充分探索的领域。

针对这一不足，本文的核心问题是：系统地实证研究现代LLM智能体框架中缺陷的根本原因和可观察症状，并理解它们在智能体完整生命周期中的分布与关联。为此，研究收集并手动分析了来自CrewAI和LangChain的998份缺陷报告，构建了一个涵盖15种根本原因和7种症状的分类体系，并将其映射到“智能体初始化”、“感知”、“自我行动”、“相互交互”和“演化”这五个智能体生命周期阶段。通过回答“缺陷的根本原因是什么”以及“缺陷的症状是什么”这两个研究问题，本文揭示了框架缺陷主要源于“API误用”、“API不兼容”和“文档不同步”等问题，且集中出现在“自我行动”阶段，症状则主要表现为“功能错误”、“崩溃”和“构建失败”，反映了对任务进度和控制流的破坏。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在方法类研究中，现有工作主要关注智能体层面的失败，例如推理、规划和执行过程中的错误，通常通过行为分析或基准测试来评估。这些研究增进了对智能体行为和模型局限性的理解，但大多忽略了底层框架本身的缺陷。一篇近期研究开始分析智能体库的缺陷，通过将拉取请求映射到库的静态组件（如数据预处理），但该方法忽略了智能体的动态执行和时序工作流。

在应用类研究中，随着大语言模型在智能问答、自动化软件工程等领域的广泛应用，智能体框架（如LangChain）被开发出来以支持任务工作流定义、状态管理和工具协调。然而，框架层的缺陷可能向上层系统传播，导致错误执行和安全风险，但相关实证研究尚属空白。

在评测类研究中，现有工作缺乏对智能体框架缺陷的系统性分类和生命周期分析。本文通过实证研究填补了这一空白，首次从生命周期视角（包括智能体初始化、感知、自行动、互操作和演化五个阶段）构建了缺陷分类法，揭示了根因和症状的分布规律，与以往侧重于静态或行为层面的研究形成鲜明对比。

### Q3: 论文如何解决这个问题？

论文通过一个严谨的三步实证研究方法来解决对智能体框架层面缺陷缺乏理解的问题。其核心方法是系统性地收集、筛选和分类来自两个主流开源框架（CrewAI和LangChain）的缺陷报告，并构建一个以智能体生命周期为导向的分类体系。

整体框架分为三个主要步骤：1）**问题收集**：从GitHub官方仓库全面抓取两个框架的原始问题报告（共2773个），涵盖开放和关闭的问题以减少抽样偏差。2）**缺陷过滤**：采用两阶段过滤流程确保数据相关性。首先利用GitHub的“bug”标签进行初步筛选，保留1010个报告；随后进行人工审查，排除文档错字、使用问题、基础设施问题等无关报告，最终得到998个与框架缺陷直接相关的有效问题。3）**个体标注**：由两位研究者进行独立标注和交叉验证，过程又分为两个子阶段：先随机抽取100个报告构建初始分类法，归纳出15个根本原因和7个可观察症状类别；再将此分类法应用于剩余报告进行大规模标注，过程中仅在遇到无法归入现有类别的新模式时才引入新类别。

关键技术和创新点在于：**生命周期导向的分类体系**。研究没有孤立地看待缺陷，而是将根本原因和症状映射到智能体生命周期的五个阶段（“智能体初始化”、“感知”、“自我行动”、“相互交互”和“进化”），这为理解缺陷发生的上下文和影响提供了结构化基础。**互补框架选择**：选取设计侧重点不同的LangChain（成熟框架，侧重工具调用和执行管道）和CrewAI（侧重基于角色的多智能体协作），使得研究能够考察多样化的框架机制和缺陷模式，增强了发现的普适性。**严谨的标注流程**：通过独立标注、交叉核对、在线会议解决分歧以及仅在必要时引入新类别等程序，保证了分类的一致性和可靠性，使得从大量定性数据中归纳出的分类法具有坚实的实证基础。

### Q4: 论文做了哪些实验？

本研究对CrewAI和LangChain两个现代LLM智能体框架进行了实证分析，实验基于从这两个框架收集的998个真实bug报告。实验设置上，研究者对这些bug报告进行了系统的标注和分类，构建了一个涵盖15种根本原因和7种可观察症状的分类体系，并按照智能体生命周期的五个阶段（智能体初始化、感知、自主行动、相互交互、进化）进行分析。

数据集/基准测试即为来自CrewAI和LangChain开源项目的998个bug报告，构成了本次实证研究的基础。

对比方法方面，本研究是一项开创性的实证分析，旨在填补现有研究主要关注智能体层面失败、而忽视框架层面缺陷的空白，因此没有设置传统的基线模型对比，而是通过对大量现实缺陷进行系统分类和统计分析来揭示模式。

主要结果和关键数据指标如下：
1.  **根本原因分布**：识别出15类根本原因。其中“API误用”（329例，占32.97%）和“API不兼容”（223例，占22.34%）最为突出，合计超过总bug数的一半（55.3%），凸显了接口相关问题的主导地位。其他原因如“文档不同步”（75例）、“流式传输不稳定”（67例）等则相对较少。
2.  **症状分布**：识别出7类症状。“功能错误”最为常见（781例，占78.26%），其次是“崩溃”（100例，占10.02%）和“构建失败”（67例，占6.71%）。性能低下（10例）和未报告错误（4例）等症状则较为罕见。
3.  **生命周期阶段分布**：缺陷高度集中在“自主行动”阶段（882例），该阶段包含了绝大部分的“API误用”（289例）和“API不兼容”（211例）问题。相比之下，“感知”、“相互交互”和“进化”阶段的bug数量要少得多（分别为18、53、9例），表明大多数缺陷与执行阶段相关。症状在“自主行动”阶段也最多样，包括大量的功能错误（692例）、崩溃（91例）和构建失败（58例）。

### Q5: 有什么可以进一步探索的点？

该论文主要对现有LLM智能体框架的bug进行了实证分类，但研究范围局限于CrewAI和LangChain两个框架，未来可扩展至更多样化的框架（如AutoGen、Semantic Kernel等）以验证分类的普适性。此外，研究主要基于历史bug报告进行归纳，缺乏对bug动态产生和修复过程的深入分析，未来可结合实时监控或故障注入实验，探究bug在复杂多轮交互中的传播机制。

从改进角度看，可探索自动化检测工具的开发，例如基于现有分类构建静态分析或运行时验证器，提前预警API误用或文档不同步问题。同时，研究可进一步区分框架bug与底层LLM模型缺陷的耦合影响，例如设计实验剥离框架逻辑错误与LLM输出不确定性导致的故障。最后，可结合形式化方法对智能体生命周期阶段建模，为框架设计提供更严谨的可靠性保障。

### Q6: 总结一下论文的主要内容

该论文对现代LLM智能体框架中的缺陷进行了首次系统性实证研究，填补了现有研究主要关注智能体层面失败而忽略框架层面漏洞的空白。研究问题聚焦于识别和分析支撑智能体工作流执行与多智能体协作的底层框架中的错误模式。

方法上，作者从CrewAI和LangChain两个主流框架中收集了998份缺陷报告，构建了一个涵盖智能体生命周期五个阶段（智能体初始化、感知、自主行动、相互交互、进化）的分类体系，归纳出15种根本原因和7种可观察症状。

核心发现表明，框架缺陷主要由“API误用”、“API不兼容”和“文档不同步”引起，且高度集中在“自主行动”阶段。其症状主要表现为“功能错误”、“崩溃”和“构建失败”，这些症状会严重破坏任务执行流程和控制流。该研究的意义在于为框架开发者提供了明确的缺陷预防和修复方向，并为构建更可靠、可扩展的智能体系统奠定了实证基础。
