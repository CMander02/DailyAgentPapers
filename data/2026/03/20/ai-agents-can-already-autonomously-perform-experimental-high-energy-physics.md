---
title: "AI Agents Can Already Autonomously Perform Experimental High Energy Physics"
authors:
  - "Eric A. Moreno"
  - "Samuel Bright-Thonney"
  - "Andrzej Novak"
  - "Dolores Garcia"
  - "Philip Harris"
date: "2026-03-20"
arxiv_id: "2603.20179"
arxiv_url: "https://arxiv.org/abs/2603.20179"
pdf_url: "https://arxiv.org/pdf/2603.20179v1"
categories:
  - "hep-ex"
  - "cs.AI"
  - "cs.LG"
tags:
  - "AI Agent"
  - "Autonomous Agent"
  - "Scientific Agent"
  - "Multi-Agent"
  - "Tool Use"
  - "Code Generation"
  - "Knowledge Retrieval"
  - "High Energy Physics"
  - "Workflow Automation"
  - "Proof-of-Concept"
relevance_score: 8.0
---

# AI Agents Can Already Autonomously Perform Experimental High Energy Physics

## 原始摘要

Large language model-based AI agents are now able to autonomously execute substantial portions of a high energy physics (HEP) analysis pipeline with minimal expert-curated input. Given access to a HEP dataset, an execution framework, and a corpus of prior experimental literature, we find that Claude Code succeeds in automating all stages of a typical analysis: event selection, background estimation, uncertainty quantification, statistical inference, and paper drafting. We argue that the experimental HEP community is underestimating the current capabilities of these systems, and that most proposed agentic workflows are too narrowly scoped or scaffolded to specific analysis structures. We present a proof-of-concept framework, Just Furnish Context (JFC), that integrates autonomous analysis agents with literature-based knowledge retrieval and multi-agent review, and show that this is sufficient to plan, execute, and document a credible high energy physics analysis. We demonstrate this by conducting analyses on open data from ALEPH, DELPHI, and CMS to perform electroweak, QCD, and Higgs boson measurements. Rather than replacing physicists, these tools promise to offload the repetitive technical burden of analysis code development, freeing researchers to focus on physics insight, truly novel method development, and rigorous validation. Given these developments, we advocate for new strategies for how the community trains students, organizes analysis efforts, and allocates human expertise.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决高能物理（HEP）实验分析中因高度依赖人工编写代码和重复性劳动而导致的效率低下、过程缓慢且易出错的问题。研究背景在于，典型的HEP分析流程（如事件选择、背景估计、不确定性量化、统计推断和论文撰写）通常耗时数年，需要物理学家编写大量结构相似的代码，这不仅消耗了大量时间和精力，还挤占了他们从事更高层次物理洞察和方法创新的机会。现有方法主要依赖人工逐步执行分析，并辅以多层人工审查，但这种方式往往缺乏自动化支持，且现有的一些AI辅助工作流程过于局限，通常需要持续的人工干预或仅限于特定分析结构。

本文的核心问题是：如何利用基于大语言模型的AI代理，实现高能物理分析流程的近乎完全自主化，以减轻研究者的重复性技术负担。为此，论文提出了一个名为“Just Furnish Context”（JFC）的概念验证框架，该框架集成了自主分析代理、基于文献的知识检索和多代理审查机制，仅需少量高层物理提示即可规划、执行并记录完整的HEP分析。通过应用该框架对ALEPH、DELPHI和CMS的开放数据进行电弱、QCD和希格斯玻色子测量分析，论文证明了当前AI代理已能自主完成可信的分析工作，从而呼吁社区重新思考如何培训学生、组织分析工作以及分配人力资源。

### Q2: 有哪些相关研究？

本文相关研究主要分为通用科学AI代理和高能物理（HEP）领域专用代理两大类。

在通用科学AI代理方面，**ChemCrow**和**Coscientist**专注于化学合成与实验自动化，通过集成专业工具实现任务规划与执行；**AI Scientist**展示了从想法生成到论文撰写的全自主流程；**SciAgents**和**PaperQA2**则采用多代理架构或检索增强生成技术，分别用于材料科学发现和文献综合。这些工作体现了AI驱动科研的广泛趋势，但各领域在数据复杂性、验证需求和领域推理方面存在独特挑战。

在HEP专用代理方面，现有工作可按任务类型细分：**方法类**如Gendreau-Distler等人的框架，利用LLM代理与Snakemake工作流管理器自动化希格斯玻色子测量，但缺乏多步骤自主规划能力；Diefenbacher等人研究异常检测代理，能自主制定分析策略。**流程管理类**如**HEPTAPOD**，专注于模拟和工作流管理的结构化编排，强调人在环监督。**协作类**如Badea等人的概念验证，依赖人机迭代反馈循环指导分析。**上游设计类**如**GRACE**，针对实验设计与探测器优化。**工具辅助类**如**CoLLM**，提供从自然语言到深度学习分类的端到端管道，但更接近AI辅助工具包。**评测类**如**CelloAI**基准，专注于代码文档与生成任务评估，尚缺物理分析任务标准。**知识检索类**如**SciTreeRAG**和**SciGraphRAG**，通过层次化或知识图谱方法提升科学文献检索效果；**PaperQA2**则以多步骤代理任务实现文献综合。

本文提出的JFC框架与上述工作的主要区别在于：它首次将**自主多步骤规划**、**基于文献的领域知识检索**和**多代理评审**集成到一个统一框架中，支持从规划、执行到文档化的完整高能物理分析，且仅需在最终“解盲”阶段进行集中人工监督，而非全程干预。这突破了现有系统大多局限于预定义分析结构或缺乏知识集成与自主规划的现状。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为 \slop 的自主智能体框架来解决高能物理（HEP）分析流程自动化的问题。该框架的核心思想是赋予AI智能体真正的自主权，使其能够根据高层物理目标（如“使用ALEPH数据测量Z玻色子的强子截面”）自主规划并执行完整的分析流程，而不仅仅是填充预设的模板。

**整体框架与架构设计**：
\slop 框架基于Claude Code（以Claude Opus为后端模型）构建，采用“编排器-子智能体”的层级结构。编排器将整个分析流程分解为七个顺序阶段，每个阶段必须产出书面成果并通过独立评审才能进入下一阶段，实现了结构化的任务分解和上下文管理。关键创新在于，智能体在由物理学家制定的“方法论规范”和“惯例目录”所构成的“脚手架”内自主运作。前者以自然语言定义分析阶段、产出和评审门控；后者则编码了领域特定的累积知识（如特定测量类型的标准系统不确定性源）。这类似于研究生课程大纲，不规定每一步，但确立了决策和评审的标准。

**主要模块/组件与关键技术**：
1.  **自主分析规划与执行**：核心的“主导分析师”智能体接收高层物理目标后，需自主确定完整分析策略，包括事件选择、本底估计、系统不确定性评估、统计框架和结果呈现。所有分析代码均以列式风格编写，并采用分阶段原型测试（先在小样本上测试，再根据规则自动扩展到全数据集）。
2.  **基于文献的知识检索（SciTreeRAG）**：这是一个关键创新组件。为了解决LLM预训练知识在具体实验细节上的不足，该系统索引了大量已发表的LEP（如ALEPH, DELPHI）论文，利用文档的层次结构进行上下文连贯的检索，而非标准的扁平文本块。当智能体需要领域知识（如事件选择条件、系统不确定性源）时，可查询该系统并获取相关文献段落，从而做出基于已有实验实践的知情决策。
3.  **多智能体评审系统**：该模块模拟了真实HEP合作组的内部评审过程。在每一分析阶段完成后，会由一个由多个 specialized 评审智能体组成的“评审团”进行自动化评审。其中：
    *   **物理评审员**：扮演独立资深合作成员的角色，**故意不接触**框架的方法论和惯例文档，仅基于物理知识和待评审成果进行评判，确保评估的客观性和外部视角。
    *   **关键评审员**：执行最全面的评审，会系统性地应用方法论和惯例文档，进行包括惯例合规性检查、参考分析对比、图表验证、物理合理性检查、回归检测等八项强制性步骤。
    *   此外还有建设性评审员、渲染评审员等。评审结果由“仲裁员”智能体综合，给出通过、迭代或升级的裁决。如果发现问题，分析智能体需修订并重新提交，直到所有评审员批准。
4.  **专业化的子智能体体系**：框架定义了四类功能智能体（执行者、专家、评审者、裁决者），每个都有明确的角色、可用工具和模型层级。所有子智能体都以无状态方式运行（每次调用都是全新进程），接收特定任务相关的工件和指令，这有效防止了长流程中的上下文窗口耗尽问题。

**总结的创新点**：
*   **真正的端到端自主性**：智能体从零开始规划并执行完整HEP分析流程，而非在预设步骤中生成代码。
*   **“脚手架式”自主**：通过“方法论”和“惯例”文档提供领域约束和知识，平衡了自主性与物理可靠性。
*   **深度集成的文献检索**：SciTreeRAG使智能体的决策能够扎根于已发表的实验实践，显著减少了猜测或幻觉。
*   **模拟真实评审的多智能体审查**：特别是设置独立的“物理评审员”，确保了分析在物理实质而不仅仅是流程合规性上得到验证。
*   **可扩展的列式代码生成与执行**：规定了纯Python HEP软件栈，并实现了从原型到大规模计算的自动扩展。

### Q4: 论文做了哪些实验？

论文通过构建名为 \slop 的自主分析框架，在多个高能物理数据集上进行了概念验证实验，以评估基于大语言模型的AI代理能否自主执行完整的物理分析流程。

**实验设置**：核心框架 \slop 基于 Claude Code（模型为 Claude Opus）构建，包含一个协调代理和多个执行、评审子代理。分析被分解为策略制定、数据探索、选择与背景建模、预期结果、部分解盲、完全解盲和文档撰写七个顺序阶段，每个阶段需产出文档并通过独立的多代理评审。框架强制使用特定的纯Python软件栈（如uproot、awkward-array、hist、pyhf等），并集成了基于SciTreeRAG的文献检索系统，为代理提供领域知识。

**数据集/基准测试**：实验使用了来自ALEPH、DELPHI和CMS实验的公开数据，以执行电弱、QCD和希格斯玻色子测量。其中，ALEPH分析可访问基于LEP已发表论文构建的文献检索系统（包含1503个条目，其中575个成功转换为markdown），而DELPHI和CMS的分析则未使用此功能。

**对比方法**：论文主要论证当前AI代理的能力被低估，指出大多数先前提出的代理工作流程范围过窄或局限于特定分析结构。\slop 框架的对比基线是这些“范围过窄”的传统代理工作流，其创新在于赋予代理从高层物理目标出发的**真正自主性**，而非在预定义步骤中填充代码模板。

**主要结果与关键指标**：实验表明，AI代理能够成功自动化典型分析的所有阶段：事例选择、背景估计、不确定性量化、统计推断和论文起草。关键数据包括：1) 文献检索系统成功索引并转换了大量历史文献（如DELPHI目录4305个条目中，1868个被转换）；2) 框架通过多代理评审机制（如4-bot评审）确保分析质量，评审代理能识别并分类问题（A类：阻塞性；B类：重要；C类：次要）；3) 代理能生成完整的分析笔记（ANALYSIS_NOTE.md）并编译为PDF。这些结果证明，仅提供上下文（Just Furnish Context）就足以规划、执行和记录一个可信的高能物理分析。

### Q5: 有什么可以进一步探索的点？

该论文展示了AI代理在自动化高能物理分析流程上的潜力，但仍有多个方向值得深入探索。首先，当前框架依赖预定义的执行环境和有限的文献库，未来可研究如何让代理更灵活地适应不同实验设置或跨领域数据，例如处理实时实验数据流或未结构化的原始数据。其次，代理的决策过程缺乏透明度，可引入可解释性AI技术，让物理学家能追踪和验证分析步骤的逻辑依据。此外，多代理协作虽已初步实现，但如何优化任务分配与冲突解决机制，以处理更复杂的分析场景（如多物理目标并行分析）仍需探索。从方法论看，当前代理依赖于现有文献知识，可能难以突破传统分析范式，未来可结合生成式模型与物理仿真，让代理自主提出创新性假设或分析方法。最后，社区需建立标准化评估体系，以量化代理在不确定性处理、错误恢复及物理洞察生成方面的能力，确保其在实际科研中的可靠性与互补性。

### Q6: 总结一下论文的主要内容

该论文探讨了基于大语言模型的AI智能体在自主执行高能物理实验分析方面的能力。核心问题是验证AI能否在最小专家干预下，完成从事件选择到论文撰写的完整分析流程。作者提出了“只需提供上下文”的概念性框架，整合了自主分析智能体、文献知识检索和多智能体评审机制。方法上，他们利用Claude Code等智能体，在ALEPH、DELPHI和CMS的公开数据上成功进行了电弱测量、QCD研究和希格斯玻色子测量等分析。主要结论表明，当前AI智能体已能可靠地自动化执行高能物理分析中的大量技术性工作，这并非取代物理学家，而是减轻其重复性编码负担，使其更专注于物理洞察和新方法开发。论文强调社区低估了现有系统的能力，并呼吁在人才培养、分析组织与专家资源分配上采取新策略。
