---
title: "Vibe Researching as Wolf Coming: Can AI Agents with Skills Replace or Augment Social Scientists?"
authors:
  - "Yongjun Zhang"
date: "2026-02-25"
arxiv_id: "2602.22401"
arxiv_url: "https://arxiv.org/abs/2602.22401"
pdf_url: "https://arxiv.org/pdf/2602.22401v2"
categories:
  - "cs.AI"
  - "cs.HC"
tags:
  - "AI Agent"
  - "Tool Use"
  - "Multi-step Reasoning"
  - "Research Automation"
  - "Workflow"
  - "Human-AI Collaboration"
  - "Skill Specialization"
  - "Social Science Application"
relevance_score: 8.5
---

# Vibe Researching as Wolf Coming: Can AI Agents with Skills Replace or Augment Social Scientists?

## 原始摘要

AI agents -- systems that execute multi-step reasoning workflows with persistent state, tool access, and specialist skills -- represent a qualitative shift from prior automation technologies in social science. Unlike chatbots that respond to isolated queries, AI agents can now read files, run code, query databases, search the web, and invoke domain-specific skills to execute entire research pipelines autonomously. This paper introduces the concept of vibe researching -- the AI-era parallel to vibe coding (Karpathy, 2025) -- and uses scholar-skill, a 23-skill plugin for Claude Code covering the full research pipeline from idea to submission, as an illustrative case. I develop a cognitive task framework that classifies research activities along two dimensions -- codifiability and tacit knowledge requirement -- to identify a delegation boundary that is cognitive, not sequential: it cuts through every stage of the research pipeline, not between stages. I argue that AI agents excel at speed, coverage, and methodological scaffolding but struggle with theoretical originality and tacit field knowledge. The paper concludes with an analysis of three implications for the profession -- augmentation with fragile conditions, stratification risk, and a pedagogical crisis -- and proposes five principles for responsible vibe researching.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图探讨在AI智能体技术快速发展的背景下，社会科学研究范式可能面临的根本性变革。研究背景是，自2022年以来，AI已能自动生成代码，2023年能生成连贯文本，2024年更进化到能执行多步骤工作流的智能体阶段。特别是2025年“氛围编程”概念的出现，标志着AI开始接管复杂工作流程。现有研究自动化多局限于单个研究环节的辅助，而未能从认知层面系统分析AI对整个研究链条的渗透。

现有方法的不足在于，传统上认为AI只能替代研究中程式化的部分，而人类研究者保留需要创造力和领域直觉的核心环节。但这种划分过于简单，未能揭示AI智能体如何跨越研究阶段边界，深度介入从文献综述到论文提交的全过程。

本文要解决的核心问题是：当AI智能体能够自主执行完整的研究流程时，研究者的独特贡献究竟是什么？研究者是否还是真正的“作者”，抑或变成了仅仅是“策展人”？论文通过引入“氛围研究”这一概念，并借助一个涵盖23项技能的Claude Code插件案例，构建了一个认知任务分析框架，从“可编码性”和“隐性知识需求”两个维度，识别出贯穿每个研究阶段而非阶段之间的新型人机协作边界。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在**方法类**研究中，本文与劳动经济学中基于任务的框架一脉相承，该框架区分了常规与非常规工作。本文提出的认知任务框架（从“可编码性”和“隐性知识需求”两个维度对研究活动进行分类）是对这一思想的深化和具体应用，旨在更精确地界定人机协作的边界。

在**应用类**研究中，多项工作探讨了AI在科学研究中的潜力。例如，有研究全面回顾了AI在从分子模拟到材料发现等多个科学学科中的应用；也有研究展示了能够自主生成研究想法、编写代码、运行实验并撰写完整科学论文的AI系统，尽管存在质量限制；在社会科学领域，有研究论证了生成式AI在数据收集、分析和理论发展方面的增强作用，但也指出了风险。本文通过介绍一个覆盖从构思到投稿全流程的、包含23项技能的“学者技能”插件（scholar-skill）作为具体案例，扩展了这类应用研究，提供了一个可操作的详细系统分析。

在**评测类**研究中，有工作系统评估了大语言模型在计算社会科学任务上的能力，发现其在结构化任务上表现良好，但在需要深度领域知识的任务上存在局限。另一项研究表明，大语言模型可以高保真地模拟人类调查响应。本文的框架和分析与这些评测工作相互呼应，但更进一步，它并非笼统地问“AI能否做社会科学”，而是聚焦于研究流程的**每一个阶段内部**，具体分析哪些认知任务可被委托、哪些不能，从而更精细地描绘了人机分工的认知边界，而非简单的流程阶段间的顺序边界。

### Q3: 论文如何解决这个问题？

论文通过提出一个认知任务框架来解决AI代理在社会科学研究中如何有效替代或增强人类研究者的问题。该框架的核心是将研究活动沿两个维度进行分类：**可编码性**（任务能否分解为明确的规则程序）和**隐性知识需求**（任务是否依赖于无法完全言传的知识，如领域政治、信任网络、直觉等）。基于这两个维度，研究任务被划分为四种类型，每种类型对应不同的AI自动化潜力。

**整体框架与主要模块**：框架以二维坐标形式呈现，横轴为隐性知识需求（从低到高），纵轴为自动化潜力（从低到高）。由此划分出四个任务类型：  
1. **类型C（执行）**：高自动化潜力、低隐性知识需求。包括运行回归分析、生成统计数据、可视化等高度可编码且可验证的任务，AI代理在此类任务中表现优异。  
2. **类型D（沟通）**：中高自动化潜力、中隐性知识需求。涉及论文起草、期刊格式化、回复审稿意见等。AI可生成草稿，但需要研究者进行判断，属于“危险中间地带”，因细微错误需专家审查。  
3. **类型B（规划）**：中自动化潜力、高隐性知识需求。例如选择识别策略、构建因果图、设计开放科学协议等。AI可提供选项，但决策必须由研究者负责。  
4. **类型A（构想）**：低自动化潜力、极高隐性知识需求。包括提出新研究问题、识别现有框架不足、跨领域借鉴等。AI仅能辅助，判断不可替代地依赖于人类。

**创新点与关键技术**：  
- **认知边界而非顺序边界**：框架的关键创新在于指出委托与保护的边界是**认知性**的，而非按研究流程阶段顺序划分。这意味着在每个研究阶段（如文献综述、方法设计、分析、写作），都同时存在可委托的（高可编码性）和需保护的（高隐性知识需求）任务，而非简单将某些阶段完全交给AI。  
- **委托决策矩阵**：通过具体示例（如文献合成可委托，理论生成不可委托）提供了实操指南，帮助研究者明确何时使用AI代理（如Scholar-Skill插件）自动化执行，何时需保留人类判断。  
- **增强而非替代的定位**：框架强调AI代理在**速度、覆盖范围和方法论支架**方面的优势，但指出其在理论原创性和隐性领域知识上的局限，从而引导研究者走向“负责任的情绪研究”，即通过委托可编码任务来增强效率，同时保护核心认知功能。

这一框架通过结构化分类，使研究者能系统性评估AI代理的适用性，避免盲目自动化，最终实现人机协作的优化研究流程。

### Q4: 论文做了哪些实验？

论文通过Scholar-Skill系统这一案例研究进行了实验。实验设置上，该系统是一个为Claude Code设计的本地插件，整合了23项专门技能，覆盖从构思到投稿的完整研究流程，并在研究者的笔记本电脑上运行，可访问本地文件、数据库和代码环境。

数据集与基准方面，系统利用了研究者个人的Zotero文献库（包含20,000余条条目）进行文献综述，并基于127篇已发表论文（包括作者本人的32篇、合作者的8篇以及顶级期刊的87篇范例）构建知识图谱来驱动写作。

对比方法主要体现在与以往自动化工具（如聊天机器人）的定性区分上，强调AI智能体能够执行多步骤、有状态的工作流，并访问专业工具和技能。主要结果通过各项技能的具体输出来展示：例如，文献综述技能能在三分钟内生成一篇针对目标期刊校准的1,200字综述；因果识别技能能构建因果图并生成R和Stata代码；写作技能能模仿已发表论文的修辞结构生成新颖内容；同行评审模拟能生成包含问题分类（如MAJOR-FEASIBLE）的仪表盘；复制包构建技能能自动创建并验证可复现的研究包。

关键数据指标包括：23项技能、17个协调阶段、43个质量门控项、3个硬性停止点、10步研究问题形式化流程、25+个理论框架候选、8种因果识别策略，以及生成四种格式（Markdown, Word, LaTeX, PDF）的稿件输出能力。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来可进一步探索的点包括：首先，论文指出了AI在理论原创性和隐性领域知识方面的局限，这为未来研究指明了方向——如何设计能更好融入领域直觉或支持理论生成的AI架构，例如通过混合智能系统将人类洞察与AI的覆盖广度结合。其次，论文强调的“脆弱条件”和“分层风险”揭示了人机协作的稳定性问题，未来可探索更鲁棒的交互机制，比如动态能力边界检测或自适应脚手架，以防止过度依赖。此外，技术校准的偏见（如英语中心主义）呼吁开发多语言、跨文化的研究技能库，并推动开放模型和工具以促进公平访问。最后，教育危机指向课程改革，需将方法教学从执行转向评估与批判，并加强理论深度训练，未来可研究如何用AI模拟“反事实推理”或理论辩论来辅助深层学习。这些方向不仅针对社会科学，也为AI Agent的通用设计提供了启示。

### Q6: 总结一下论文的主要内容

该论文探讨了AI智能体（能执行多步骤推理工作流并具备工具调用能力的系统）对社会科学研究范式的变革性影响。核心贡献在于提出了“氛围研究”（vibe researching）这一概念，类比于“氛围编程”，强调AI能自主执行从构思到投稿的全研究流程。作者通过一个涵盖23项研究技能的Claude Code插件案例，构建了一个认知任务框架，将研究活动按“可编码性”和“隐性知识需求”两个维度分类，从而界定人机协作的边界——这一边界是认知性的、贯穿每个研究阶段，而非顺序性的。论文指出，AI智能体在速度、覆盖范围和方法论支持上表现卓越，但在理论原创性和领域隐性知识方面存在局限。主要结论包括：AI代理已实质性地扩展了独立研究者的能力；人机协作应遵循“委托可编码任务，保护隐性判断”的原则；当前学界在规范应对上滞后于技术发展。最后，论文警示了职业增强的脆弱性、分层风险及教学危机，并提出了负责任氛围研究的五项原则，呼吁社会科学家在利用AI拓展研究的同时，保护原创性探究能力，并将AI本身作为塑造劳动、不平等和知识生产的社会现象加以研究。
