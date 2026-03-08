---
title: "Demonstrating ViviDoc: Generating Interactive Documents through Human-Agent Collaboration"
authors:
  - "Yinghao Tang"
  - "Yupeng Xie"
  - "Yingchaojie Feng"
  - "Tingfeng Lan"
  - "Wei Chen"
date: "2026-03-02"
arxiv_id: "2603.01912"
arxiv_url: "https://arxiv.org/abs/2603.01912"
pdf_url: "https://arxiv.org/pdf/2603.01912v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Human-Agent Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Human-Agent Interaction"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "Document Specification (DocSpec), multi-agent pipeline (Planner, Executor, Evaluator)"
  primary_benchmark: "N/A"
---

# Demonstrating ViviDoc: Generating Interactive Documents through Human-Agent Collaboration

## 原始摘要

Interactive articles help readers engage with complex ideas through exploration, yet creating them remains costly, requiring both domain expertise and web development skills. Recent LLM-based agents can automate content creation, but naively applying them yields uncontrollable and unverifiable outputs. We present ViviDoc, a human-agent collaborative system that generates interactive educational documents from a single topic input. ViviDoc introduces a multi-agent pipeline (Planner, Executor, Evaluator) and the Document Specification (DocSpec), a human-readable intermediate representation that decomposes each interactive visualization into State, Render, Transition, and Constraint components. The DocSpec enables educators to review and refine generation plans before code is produced, bridging the gap between pedagogical intent and executable output. Expert evaluation and a user study show that ViviDoc substantially outperforms naive agentic generation and provides an intuitive editing experience. Our project homepage is available at https://vividoc-homepage.vercel.app/.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决交互式教育文档创作成本高昂且技术门槛高的问题。研究背景是，交互式文章通过动态元素（如滑块、下拉菜单）帮助读者深入理解复杂概念，在教育、新闻和科学出版等领域有广泛应用，但现有创作方式需要作者同时具备领域知识和网页开发技能，导致每篇文章耗时数天甚至数周，严重限制了高质量交互内容的普及。

现有基于大语言模型（LLM）的智能体方法虽能自动化内容生成，但直接应用于交互式文档创作存在三大不足：一是生成过程不可控，智能体在将教学意图转化为可执行代码时依赖自身隐含偏好，导致输出与教育者预期脱节；二是人类无法有效参与，智能体作为黑箱运行，教育者难以审查或调整中间决策；三是缺乏相关数据集，难以系统评估方法效果。

本文的核心问题是：如何设计一种人机协作系统，在降低创作成本的同时，确保生成过程可控、可验证，并允许教育者参与关键决策。为此，论文提出ViviDoc系统，通过多智能体流水线（规划、执行、评估）和结构化中间表示“文档规范”（DocSpec），将交互可视化分解为状态、渲染、转换和约束组件，使教育者能在代码生成前审查和修改计划，从而弥合教学意图与可执行输出之间的鸿沟。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：交互式文档、基于LLM的自动化内容生成系统，以及多智能体框架。

在**交互式文档与可探索解释**方面，研究历史悠久，其理论基础可追溯至增强人类智能的早期人机交互范式和超文本结构，并在PLATO等系统中实现。实证研究表明，交互式文章能显著提升学习者的参与度和理解力，已广泛应用于数据新闻和学术传播等领域。然而，其创作成本高昂，需要同时具备领域知识和开发技能，这构成了主要瓶颈。本文的ViviDoc系统正是为了突破这一创作壁垒而设计。

在**基于LLM的自动化内容生成**领域，已有许多工作利用大语言模型或智能体来自动创建可视化内容。例如，在数据可视化方面，LIDA、Infogen、HAIChart和PlotGen等系统能够从非结构化文本生成复杂的信息图表。在演示文稿生成方面，PPTagent和SlideGen等系统利用结构化模式来制作连贯的幻灯片。这些工作展示了自动化内容生成的潜力，但通常缺乏对生成过程的控制和可验证性。

在**多智能体系统**方面，研究如LAVES等将多智能体编排应用于生成同步教育视频，展示了智能体协作处理复杂任务的可行性。然而，将这些智能体方法直接应用于生成交互式教育文档仍属探索不足的领域。简单的应用往往会导致生成结果不可控、缺乏教学对齐、过程不透明且难以进行人工干预。

**本文与这些工作的关系和区别**在于：ViviDoc没有采用“黑箱”式的全自动生成，而是专注于**人机协作范式**，并引入了关键创新——**文档规范（DocSpec）**这一人类可读的中间表示。这使得教育者能在代码生成前审查和调整计划，从而在教学设计意图和可执行输出之间架起桥梁，解决了现有智能体方法在可控性、可验证性和教学对齐方面的核心局限。因此，ViviDoc是对现有自动化内容生成和多智能体框架在特定、高价值应用场景下的重要深化和拓展。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ViviDoc的人机协同系统来解决交互式教育文档创建成本高、自动化生成不可控的问题。其核心方法是设计一个多智能体流水线，并引入一个结构化的中间表示——文档规范（DocSpec），作为连接人类教学意图与最终可执行代码的桥梁。

整体框架遵循“主题→规范→文档”的工作流，主要由三个智能体模块协同完成：
1.  **规划器（Planner）**：接收用户输入的主题，利用大语言模型将其分解为一系列知识单元，并生成结构化的DocSpec。每个知识单元包含文本描述和交互规范（SRTC），后者明确定义了交互式可视化的构成。
2.  **执行器（Executor）**：接收经过用户审阅和可能修改后的DocSpec，分两阶段生成最终的HTML文档。第一阶段根据文本描述生成连贯的文本内容；第二阶段根据SRTC规范生成交互式可视化所需的HTML、CSS和JavaScript代码。该模块包含重试机制以确保生成质量。
3.  **评估器（Evaluator）**：对生成的文档进行质量检查，评估文本连贯性、逻辑流程，并验证所有知识单元是否成功生成且通过HTML验证。发现问题时可提供反馈以触发特定组件的重新执行。

系统的关键创新点在于**DocSpec及其SRTC分解**。DocSpec是一个人类可读、可编辑的中间表示，它将每个交互式可视化分解为四个明确组件：
*   **状态（S）**：定义可视化所基于的变量，包括类型、取值范围和派生规则。
*   **渲染（R）**：描述状态如何映射到屏幕上的视觉元素。
*   **过渡（T）**：描述用户操作如何修改状态，即输入事件与状态变化的因果关系。
*   **约束（C）**：编码可视化旨在演示的教学不变量，即学习者应通过交互发现的核心概念。

这种结构化格式为整个流水线提供了明确的“契约”：它约束规划器产出格式良好的规范，为执行器提供无歧义的代码合成依据，并为评估器提供了验证正确性的客观标准（约束C）。

此外，系统将**人工审阅**深度集成到流程中，尤其是在规划器生成DocSpec之后、执行器生成代码之前。用户可以直接编辑DocSpec（如调整知识单元顺序、修改交互参数），或通过自然语言与AI助手对话来描述修改意图。这种设计将最具错误风险的“意图到代码”的转换过程，约束在一个结构化的规范内进行，允许人类在最具杠杆效应的环节（代码生成前）进行干预和控制，从而在保持自动化效率的同时，确保了输出的可控性、可验证性并符合教学意图。

### Q4: 论文做了哪些实验？

论文进行了两项主要实验：专家盲评和用户可用性研究。

**实验设置与数据集**：从基准数据集中随机选取10个主题，使用两种方法生成交互式教育文档，共产生20份文档。对比方法为：1) **ViviDoc系统**：采用多智能体流程（规划器生成DocSpec，执行器生成文档，评估器检查输出），但为公平比较禁用了人工审核步骤；2) **Naive Agent**：直接提示LLM一次性生成完整HTML文档，无DocSpec规划。两种方法均使用相同底层模型（Gemini 3.0 Flash）以控制模型能力差异。

**专家盲评结果**：三位领域专家对20份文档在三个维度进行5点李克特量表评分。ViviDoc在所有维度上均显著优于Naive Agent：
- **内容丰富度**：4.17 vs. 2.07
- **交互质量**：4.00 vs. 2.40
- **视觉质量**：3.73 vs. 2.37
结果表明，无DocSpec结构化规划时，LLM生成的文档内容浅薄、交互设计不连贯、视觉布局混乱。

**用户研究结果**：三位具有可视化或教育技术背景的参与者使用ViviDoc完成三项文档生成任务。可用性评分（5点量表）显示：
- 易于学习：5.0
- 易于使用：5.0
- DocSpec编辑直观性：4.33±0.58
- 界面满意度：4.33±0.58
- DocSpec符合预期：4.67±0.58
定性反馈证实DocSpec界面允许用户“无需编写代码即可决定交互逻辑”，且文本描述与交互规范的分离使编辑更直观。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其多智能体流程和DocSpec主要针对教育领域的交互式文档生成，通用性有待验证。未来研究可探索更广泛的文档类型（如技术手册、数据报告）的生成，并考虑如何将系统扩展到更复杂的交互逻辑和多媒体内容整合。此外，当前系统依赖人工审核DocSpec，未来可引入更智能的实时协作机制，例如允许用户在生成过程中动态调整智能体的优先级或注入领域知识。另一个方向是增强系统的可解释性，让用户更直观地理解智能体的决策过程，从而提升信任度。结合多模态大模型的能力，进一步自动化图表设计和交互反馈优化，也是值得探索的改进思路。

### Q6: 总结一下论文的主要内容

该论文提出了ViviDoc系统，旨在通过人机协作生成交互式教育文档，以降低创建交互式内容的门槛。核心问题是现有方法需要大量专业知识和开发技能，而单纯使用大语言模型代理生成的内容难以控制和验证。论文的核心贡献是引入了文档规范（DocSpec）作为结构化中间表示，将交互式可视化分解为状态、渲染、过渡和约束组件，使教育者能在代码生成前审查和调整计划，从而在教学设计与可执行输出之间建立桥梁。方法上采用多智能体管道（规划器、执行器、评估器）协作生成文档，并允许人类介入编辑。主要结论显示，基于DocSpec的结构化规划相比单纯代理生成在质量上有显著提升，用户研究证实了编辑界面的直观性和有效性。该系统为交互内容创作提供了新思路，并推动了人机协作在文档创作领域的进一步研究。
