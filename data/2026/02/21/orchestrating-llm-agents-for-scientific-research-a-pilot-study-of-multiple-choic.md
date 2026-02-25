---
title: "Orchestrating LLM Agents for Scientific Research: A Pilot Study of Multiple Choice Question (MCQ) Generation and Evaluation"
authors:
  - "Yuan An"
date: "2026-02-21"
arxiv_id: "2602.18891"
arxiv_url: "https://arxiv.org/abs/2602.18891"
pdf_url: "https://arxiv.org/pdf/2602.18891v1"
categories:
  - "cs.CY"
  - "cs.AI"
  - "cs.HC"
tags:
  - "Agent Orchestration"
  - "Multi-Agent System"
  - "Agentic Workflow"
  - "LLM Agents"
  - "Scientific Research"
  - "Agent Evaluation"
  - "Human-Agent Collaboration"
  - "AI Research Operations"
relevance_score: 8.0
---

# Orchestrating LLM Agents for Scientific Research: A Pilot Study of Multiple Choice Question (MCQ) Generation and Evaluation

## 原始摘要

Advances in large language models (LLMs) are rapidly transforming scientific work, yet empirical evidence on how these systems reshape research activities remains limited. We report a mixed-methods pilot evaluation of an AI-orchestrated research workflow in which a human researcher coordinated multiple LLM-based agents to perform data extraction, corpus construction, artifact generation, and artifact evaluation. Using the generation and assessment of multiple-choice questions (MCQs) as a testbed, we collected 1,071 SAT Math MCQs and employed LLM agents to extract questions from PDFs, retrieve and convert open textbooks into structured representations, align each MCQ with relevant textbook content, generate new MCQs under specified difficulty and cognitive levels, and evaluate both original and generated MCQs using a 24-criterion quality framework. Across all evaluations, average MCQ quality was high. However, criterion-level analysis and equivalence testing show that generated MCQs are not fully comparable to expert-vetted baseline questions. Strict similarity (24/24 criteria equivalent) was never achieved. Persistent gaps concentrated in skill\ depth, cognitive engagement, difficulty calibration, and metadata alignment, while surface-level qualities, such as {grammar fluency}, {clarity options}, {no duplicates}, were consistently strong. Beyond MCQ outcomes, the study documents a labor shift. The researcher's work moved from ``authoring items'' toward {specification, orchestration, verification}, and {governance}. Formalizing constraints, designing rubrics, building validation loops, recovering from tool failures, and auditing provenance constituted the primary activities. We discuss implications for the future of scientific work, including emerging ``AI research operations'' skills required for AI-empowered research pipelines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决两个核心的、相互关联的问题。首先，它旨在通过一个具体案例（生成和评估SAT数学选择题）来实证探究：当研究者利用AI驱动的流程端到端完成一个研究项目时，哪些任务被委托给了AI，而哪些新的职责和工作模式会随之出现？论文将这一转变描述为从“创作内容”转向“定义、协调、验证和治理”AI系统。其次，论文试图回答一个具体的实证问题：由大语言模型生成的SAT试题，在教学质量、认知需求和评估效度等维度上，在多大程度上能与人类专家编写的题目相媲美？通过设计并运行一个由人类研究者协调多个LLM智能体的工作流，论文不仅评估了生成题目的质量（发现其在表面质量上表现强劲，但在深度、认知参与度等方面仍存在差距），更关键的是，它记录并分析了在这一过程中科学研究劳动性质的根本性转变，并探讨了这对未来科研工作及所需技能（如“AI研究运维”）的深远影响。

### Q2: 有哪些相关研究？

本文相关研究主要涉及四个领域：

1. **生成式AI与知识工作未来**：研究探讨AI如何重塑工作性质，如Autor（2003）的任务分类理论、Acemoglu（2019）的自动化与任务创造框架，以及近期关于AI在专业任务中生产力影响的实证研究（如Noy & Zhang, 2023）。本文在此基础上，将焦点从一般知识工作延伸至更复杂的科学研究活动，实证检验了AI代理对科研工作流程的重构。

2. **科学工作流自动化**：早期e-science研究关注计算工作流的可重复性与溯源（如Gil等，2007）。近期研究则探索LLM作为“粘合层”在工具调用和代码生成中的作用（如ReAct框架）。本文继承了工作流自动化的核心挑战（如工具可靠性、溯源），并具体研究了LLM代理编排如何应对这些挑战。

3. **自动多选题生成与质量评估**：这是一个成熟领域，拥有既定的模块化流水线（如Ch等，2018的综述）和人工命题原则（如Haladyna，2002）。近期研究开始利用LLM进行跨领域（如医学、法律）的题目生成。本文以此作为测试平台，但重点不在于生成技术本身，而在于将其置于一个由多代理协作的完整科研工作流中，并系统评估生成题目的质量差距。

4. **基于LLM的评估（LLM-as-a-judge）**：为解决生成内容的大规模评估瓶颈，研究者提出使用LLM作为评判员（如Zheng等，2023），并发展出结构化评估框架（如G-Eval）。本文借鉴了多准则评估框架的思想，构建了包含24个维度的质量评估体系，并将其应用于对原始题目和生成题目的系统性比较，从而验证了在复杂评估任务中LLM评判的局限性。

本文与这些工作的关系在于：它将上述四个相对独立的研究脉络整合到一个统一的实证框架中。具体而言，本文以多选题生成为具体场景，设计并运行了一个由人类研究者协调多个LLM代理的科学研究工作流，从而在操作层面揭示了生成式AI如何将科研人员的劳动从“直接创作”转向“规范制定、流程编排、结果验证与治理”，为理解AI时代科研工作的转型提供了新的实证证据和概念框架。

### Q3: 论文如何解决这个问题？

论文通过设计一个由人类研究者协调、多个LLM智能体协作的端到端科学工作流来解决多选题（MCQ）的生成与评估问题。核心方法是一个分阶段的、智能体化的流水线架构。

首先，**数据准备与知识库构建**：智能体从官方SAT数学题库PDF中提取并结构化1,071道基础MCQ，同时将开源教科书PDF转换为保留教学连贯性的文本块（chunk），建立可检索的知识源。

其次，**内容映射与约束生成**：系统通过双查询向量检索（30%权重基于元数据查询，70%权重基于内容查询）将每道基础MCQ与最相关的教科书知识块进行语义对齐。然后，提取基础MCQ的元数据（如领域、技能、难度、认知水平）和对应的知识块，作为生成新MCQ的明确约束和背景材料。

**关键技术**在于**多智能体分工与编排**：不同的LLM（如GPT-5-nano和Gemini-2.5-Flash）被指定为“生成智能体”，在给定的元数据约束和知识背景下生成新的MCQ。随后，同样的LLM被作为“评估智能体”，使用一个由AI协助构建的、包含24个细粒度标准的评估框架，对基础MCQ和生成MCQ进行独立双盲评分。这种设计实现了从生成到评估的闭环验证。

最后，**基于等价性测试的统计比较**：研究采用两单侧检验（TOST）的统计方法，而非简单的显著性检验，来严格评估生成MCQ与专家审定MCQ在24个质量标准上是否达到“实际等价”。这揭示了生成题目在表面质量（如语法清晰度）上表现强劲，但在技能深度、认知参与度等深层维度上与专家题目存在差距。整个流程将研究者的角色从“题目作者”转变为工作流的**规范制定者、流程编排者、验证执行者和治理审计者**。

### Q4: 论文做了哪些实验？

论文围绕LLM智能体协作生成和评估多项选择题（MCQ）进行了系统性实验。实验设置包括：收集1,071道SAT数学MCQ作为专家基准；构建由多个LLM智能体（基于Gemini和OpenAI GPT）组成的工作流，执行从PDF提取题目、检索并结构化教科书内容、对齐题目与知识点、按指定难度和认知水平生成新MCQ等任务；最后使用一个包含24项细粒度标准的评估框架，对原始SAT题目和生成题目进行质量评估。评估由两种LLM（Gemini和OpenAI GPT）作为“法官”分别独立完成。

基准测试主要从三个层面展开：1）整体质量：计算所有题目在24项标准上的平均得分（1-5分）。结果显示，无论是原始题还是生成题，平均分都很高（4.64-4.89），生成题的平均分甚至略高于专家基准。2）标准级诊断：分析每个具体标准的得分。发现表面质量（如语法流畅性、选项清晰度）近乎完美，但生成题在技能深度、认知参与度、难度校准、元数据对齐以及干扰项合理性等深层标准上持续存在短板，得分显著较低。3）推断与等价性测试：采用TOST方法检验生成题与基准题是否在统计上等价。结果发现，在24项标准中，没有任何一项能在所有条件下（两位法官、两种生成模型）达到严格等价（即24/24标准全部等价）。仅有8项核心标准（如事实准确性、答案正确性）在所有比较中均等价，而10项标准（主要涉及难度、认知参与度、技能深度等）在所有条件下均不等价。

主要结果表明，LLM智能体协作流程能高效产出表面质量极高的MCQ，但在需要深度教育学和领域专业知识校准的方面，其生成题目仍无法与专家精心设计的题目完全媲美。这揭示了当前AI生成内容在“形似”与“神似”之间的差距。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于生成的多选题在技能深度、认知参与度、难度校准和元数据对齐方面与专家审核的基准问题存在差距，未能实现严格对等。未来可进一步探索的方向包括：1）开发更精细的Agent协调与验证机制，以提升生成内容在深层次认知维度的质量；2）研究如何将人类专家的领域知识更有效地编码到工作流的规范与治理环节，从而改善难度校准等关键指标；3）扩展应用场景，将这种AI编排的研究工作流推广至更复杂的科学任务（如文献综述或假设生成），并系统化研究所需的“AI研究运营”技能体系。

### Q6: 总结一下论文的主要内容

这篇论文通过一个生成和评估SAT数学选择题的案例研究，探讨了LLM智能体如何重塑科研工作流程。核心贡献在于实证展示了由人类研究者协调多个LLM智能体（负责数据提取、语料构建、题目生成与评估）的端到端研究范式。研究发现，虽然LLM生成的题目在平均质量上很高，但在技能深度、认知参与度、难度校准等深层维度上，与专家编写的题目仍存在显著差距，未能实现完全等价。更重要的是，研究揭示了科研劳动的转变：研究者的角色从“创作内容”转向了“规范、协调、验证与治理”，即定义目标、设计评估标准、构建验证循环、处理工具故障和审计溯源。这预示着未来科学工作需要掌握“AI研究运营”等新兴核心技能。
