---
title: "HLER: Human-in-the-Loop Economic Research via Multi-Agent Pipelines for Empirical Discovery"
authors:
  - "Chen Zhu"
  - "Xiaolu Wang"
date: "2026-03-08"
arxiv_id: "2603.07444"
arxiv_url: "https://arxiv.org/abs/2603.07444"
pdf_url: "https://arxiv.org/pdf/2603.07444v1"
categories:
  - "cs.AI"
  - "econ.GN"
tags:
  - "Multi-Agent System"
  - "Human-in-the-Loop"
  - "Scientific Discovery Agent"
  - "Workflow Automation"
  - "Dataset-Aware Generation"
  - "Empirical Research"
relevance_score: 7.5
---

# HLER: Human-in-the-Loop Economic Research via Multi-Agent Pipelines for Empirical Discovery

## 原始摘要

Large language models (LLMs) have enabled agent-based systems that aim to automate scientific research workflows. Most existing approaches focus on fully autonomous discovery, where AI systems generate research ideas, conduct analyses, and produce manuscripts with minimal human involvement. However, empirical research in economics and the social sciences poses additional constraints: research questions must be grounded in available datasets, identification strategies require careful design, and human judgment remains essential for evaluating economic significance. We introduce HLER (Human-in-the-Loop Economic Research), a multi-agent architecture that supports empirical research automation while preserving critical human oversight. The system orchestrates specialized agents for data auditing, data profiling, hypothesis generation, econometric analysis, manuscript drafting, and automated review. A key design principle is dataset-aware hypothesis generation, where candidate research questions are constrained by dataset structure, variable availability, and distributional diagnostics, reducing infeasible or hallucinated hypotheses. HLER further implements a two-loop architecture: a question quality loop that screens and selects feasible hypotheses, and a research revision loop where automated review triggers re-analysis and manuscript revision. Human decision gates are embedded at key stages, allowing researchers to guide the automated pipeline. Experiments on three empirical datasets show that dataset-aware hypothesis generation produces feasible research questions in 87% of cases (versus 41% under unconstrained generation), while complete empirical manuscripts can be produced at an average API cost of $0.8-$1.5 per run. These results suggest that Human-AI collaborative pipelines may provide a practical path toward scalable empirical research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决利用大型语言模型（LLM）自动化社会科学（尤其是经济学）实证研究时面临的挑战。研究背景是，随着LLM的发展，出现了旨在自动化科学研究流程的智能体系统，现有方法多聚焦于完全自主的发现，即在机器学习等领域实现从生成想法、执行分析到撰写论文的自动化。然而，在经济学等社会科学领域进行实证研究存在特殊约束：研究问题必须基于现有数据集，识别策略需要精心设计，且人类判断对于评估经济意义至关重要。现有方法的不足在于，它们通常是文本中心化的，难以可靠地执行端到端的实证研究步骤，容易产生“幻觉”（即生成流畅但无数据支持的论断），并且缺乏与数据集、计量软件等外部工具有效交互以完成验证、估计等关键环节的能力。

因此，本文要解决的核心问题是：如何构建一个既能自动化经济学实证研究流程，又能嵌入关键人类监督、确保研究可行性与可信度的系统。具体而言，论文提出了HLER（人机交互经济研究）这一多智能体架构，通过协调数据审计、假设生成、计量分析、论文起草和自动评审等专门智能体，将数据约束、计量执行和迭代批判整合到一个流程中。其核心创新在于引入了“数据集感知的假设生成”机制，将研究问题的生成约束在数据集结构和变量可用性之内，以减少不可行的假设，并设计了一个包含“问题质量循环”和“研究修订循环”的双循环架构，在关键阶段嵌入人类决策点，从而实现人机协作的、可扩展的实证研究自动化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。在方法类中，通用多智能体框架（如AutoGen）通过协调多个专用智能体来执行科学工作流的不同环节，为研究自动化提供了基础架构。HLER借鉴了这种多智能体协调思想，但将其专门化用于经济学实证研究。在应用类中，AI Scientist和BioResearcher分别展示了在机器学习与生物医学领域实现端到端自主研究的可行性，它们能自主生成研究想法、编写代码并撰写论文。然而，这些系统主要面向计算或实验科学，可在模拟或实验室环境中直接执行实验。相比之下，HLER专注于经济学和社会科学，其核心挑战在于处理观测数据、设计识别策略并进行因果推断。在评测类中，自主政策评估（APE）项目与HLER最为相关，它同样旨在利用公开数据自动化生成经济学实证研究论文，并采用自动化评审机制。但APE强调完全自动化，而HLER则明确引入了“人在回路”的决策节点，允许研究者在关键阶段进行指导和干预。此外，HLER的创新点在于其数据集感知的假设生成机制，通过数据审计和分析来约束研究问题的可行性，以及其双循环架构（问题质量循环和研究修订循环），这些都与APE等先前系统有显著区别。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为HLER（人机循环经济研究）的多智能体流水线系统来解决自动化实证研究中的问题，其核心在于将人类判断与自动化流程相结合，确保研究的可行性和科学性。

**整体框架与架构设计**：HLER采用中心协调器（Orchestrator）驱动的多智能体架构，将实证研究分解为结构化的阶段。协调器管理一个共享状态对象（RunState），按预定义工作流顺序调度任务：数据审计 → 数据剖析 → 问题生成 → 数据收集 → 分析 → 写作 → 自我批判 → 评审。人类研究者作为首席研究员（PI）在关键决策点（研究问题选择与最终批准）进行干预，形成人机协同闭环。

**主要模块与组件**：系统包含七个专用智能体：
1.  **数据审计智能体**：验证数据集结构，清点可用变量，防止提出缺乏数据支持的假设。
2.  **数据剖析智能体**：分析数据集的统计特性（如摘要统计、缺失模式、分布、相关性），生成结构化数据概要（DataProfile），为后续假设生成提供依据。
3.  **问题智能体**：基于数据审计和剖析结果，生成与数据集结构和统计属性相约束的候选研究问题，大幅减少不可行或虚构的假设。
4.  **数据智能体**：从本地数据集（如CHNS、CMGPD-Liaoning）或公共API（如世界银行、FRED）收集和准备数据。
5.  **计量经济学智能体**：制定实证分析计划并执行计量模型（如OLS、固定效应面板模型、双重差分法），输出结果表格、图表和结构化摘要。
6.  **论文智能体**：根据分析结果生成完整的研究手稿（包括摘要、引言、方法、结果、讨论），遵循学术规范并支持版本迭代。
7.  **评审智能体**：评估手稿的新颖性、识别可信度、数据质量等，生成结构化评审报告并提出修订建议。

**关键技术**：
- **数据集感知的假设生成**：这是核心创新点。问题生成过程明确以数据可用性和统计属性为条件，将可行研究问题的生成率从无约束生成的41%提升至87%。
- **双循环反馈架构**：
  - **问题质量循环**：在假设生成阶段，系统生成多个候选问题并进行可行性评估，人类PI从中选择最优方向，若不满意可请求重新生成。
  - **研究修订循环**：手稿生成后，评审智能体提出修订要求，触发计量经济学智能体进行额外分析（如稳健性检验），论文智能体更新手稿，评审智能体重新评估，迭代直至收敛（通常2-4轮）。
- **结构化实现与模型无关性**：系统使用Python实现，智能体继承统一的BaseAgent接口，输出采用结构化数据对象（如ResearchQuestion, DataProfile），便于日志记录和跨阶段重用。虽然当前使用Claude模型，但架构设计为与模型无关。计量分析结合LLM生成的计划与statsmodels等库的程序化估计，手稿以Markdown生成并可编译为PDF。

总之，HLER通过多智能体流水线、数据集约束的假设生成、双循环质量优化以及关键节点的人类决策门，在保持自动化效率的同时，确保了经济实证研究所需的严谨性和人类判断力。

### Q4: 论文做了哪些实验？

论文实验围绕四个维度展开：实验设置、数据集、对比方法和主要结果。实验使用HLER系统，通过Anthropic API调用Claude Sonnet 4.6模型，在三个经济学常用数据集上进行了14次完整流程运行：中国健康与营养调查（CHNS，285个变量，57,203个观测值）、中国多代面板数据集（CMGPD-Liaoning）和英国生物银行（UK Biobank）。研究领域约束包括劳动经济学、健康经济学等。

对比方法主要针对假设生成环节：将HLER默认的**数据集感知生成**（QuestionAgent接收完整数据审计和统计概要后生成假设）与**无约束生成**（仅提供数据集名称和领域描述，无审计信息）进行对比。评估标准包括变量是否存在、实证设计与数据结构兼容性、是否可用支持的计量方法。

关键结果如下：数据集感知生成在79个候选问题中，87%（69个）完全满足可行性标准；而无约束生成在82个问题中仅41%（34个）可行。无约束生成的主要失败原因是变量缺失（占失败的42%）和设计不兼容（35%）。在流程完成率方面，14次运行中有12次（86%）完整完成了从数据审计到稿件生成的流程。修订循环分析显示，初始稿件平均评分为4.8（1-10分制），经2-3次迭代后最终稿件平均分提升至6.3，其中清晰度（提升2.1分）和识别可信度（提升1.4分）改进最大。计算成本方面，每次完整运行平均耗时20-25分钟，API成本为0.8-1.5美元，显著低于其他AI科研框架。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在：生成的研究问题质量受限于数据集和变量清单，无法保证理论意义或新颖性；计量分析阶段仅支持有限的研究设计，缺乏对工具变量、断点回归等复杂方法的支持；评审环节存在循环性风险，因为评审代理与生成代理基于同一大语言模型；评估规模较小，仅基于三个数据集的14次运行，需更大规模验证。

未来研究方向包括：扩展计量分析方法库，纳入更复杂的识别策略；引入独立的外部评估机制，如人类评审或不同模型，以打破评审循环性；开发更智能的假设生成模块，结合领域知识库提升问题的新颖性和理论深度；建立大规模跨领域基准测试，验证系统的泛化能力；探索如何将系统与预注册、多重检验校正等科研规范更深度整合，以应对自动化可能带来的“p-hacking”风险。

可能的改进思路：可考虑引入“理论代理”，从经济学文献中提取先验知识，引导假设生成朝向更本质的机制问题；构建模块化的计量分析组件，允许研究人员灵活插入自定义模型；设计双层评审架构，第一层由系统进行技术可行性筛选，第二层强制引入人类专家进行意义和贡献度评估。

### Q6: 总结一下论文的主要内容

本文提出了HLER系统，这是一种人机协作的多智能体架构，旨在自动化经济学实证研究流程，同时保留关键的人类监督。核心问题是解决现有全自主研究系统在经济学等社会科学领域面临的挑战，如研究问题需基于可用数据、识别策略需精心设计，以及人类判断对评估经济意义至关重要。方法上，HLER通过编排数据审计、数据剖析、假设生成、计量分析、论文起草和自动评审等专门智能体，构建了一个结构化流程。其关键设计包括数据集感知的假设生成，将候选研究问题约束于数据集结构和变量可用性，以及包含问题质量循环和研究修订循环的双循环架构，并在关键阶段嵌入人工决策点。实验表明，数据集感知的假设生成能在87%的情况下产生可行的研究问题（远高于无约束生成的41%），且端到端研究流程平均每次运行的API成本仅为0.8-1.5美元。主要结论是，HLER作为一种协作工具，能够以可扩展且经济高效的方式辅助实证研究，而非取代研究人员，为人机协同的科学研究提供了实用路径。
