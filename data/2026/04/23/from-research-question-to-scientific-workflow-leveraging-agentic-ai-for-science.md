---
title: "From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation"
authors:
  - "Bartosz Balis"
  - "Michal Orzechowski"
  - "Piotr Kica"
  - "Michal Dygas"
  - "Michal Kuszewski"
date: "2026-04-23"
arxiv_id: "2604.21910"
arxiv_url: "https://arxiv.org/abs/2604.21910"
pdf_url: "https://arxiv.org/pdf/2604.21910v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Science Automation"
  - "Workflow Generation"
  - "Intent Extraction"
  - "Knowledge Engineering"
relevance_score: 7.5
---

# From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation

## 原始摘要

Scientific workflow systems automate execution -- scheduling, fault tolerance, resource management -- but not the semantic translation that precedes it. Scientists still manually convert research questions into workflow specifications, a task requiring both domain knowledge and infrastructure expertise. We propose an agentic architecture that closes this gap through three layers: an LLM interprets natural language into structured intents (semantic layer); validated generators produce reproducible workflow DAGs (deterministic layer); and domain experts author ``Skills'': markdown documents encoding vocabulary mappings, parameter constraints, and optimization strategies (knowledge layer). This decomposition confines LLM non-determinism to intent extraction: identical intents always yield identical workflows. We implement and evaluate the architecture on the 1000 Genomes population genetics workflow and Hyperflow WMS running on Kubernetes. In an ablation study on 150 queries, Skills raise full-match intent accuracy from 44% to 83%; skill-driven deferred workflow generation reduces data transfer by 92\%; and the end-to-end pipeline completes queries on Kubernetes with LLM overhead below 15 seconds and cost under $0.001 per query.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决科学研究中从自然语言研究问题到可执行科学工作流之间的“语义鸿沟”问题。当前，科学工作流管理系统（如Pegasus、Nextflow等）虽已能自动化执行任务调度、容错等，但研究人员仍需手动将研究意图（如“比较欧洲和非洲人群在1-5号染色体上的突变模式”）转化为具体的工作流规范（如DAG图），这要求同时具备领域知识与基础设施操作经验。现有方法存在明显不足：视觉编辑器仍需要手动配置基础设施；模板方法无法应对非预期的研究问题；直接使用大语言模型生成工作流则会引入非确定性，导致相同问题可能产生不同DAG，损害可重复性。因此，本文核心问题是：如何自动化地将非结构化的自然语言研究问题转化为可复现、确定性的科学工作流，同时降低对用户的专业门槛并保证转换过程的可靠性。为此，作者提出了一种基于智能体（Agentic AI）的三层混合架构，通过分离语义理解与确定性生成来克服这些挑战。

### Q2: 有哪些相关研究？

相关研究可归纳为三类：

1. **基准评测类**：如Yildiz和Peterka在五个HPC系统上评测LLM的流程配置、注释和跨平台翻译能力，Alam和Roy评估GPT-4o、Gemini等在Galaxy和Nextflow流程生成中的表现。一致发现：LLM能生成结构合理的流程，但因缺乏领域词汇和平台规范，无法直接执行。本文的Skills通过持久化、可审计的领域文档（词汇映射、参数约束）解决此问题，而非依赖每次注入的临时示例。

2. **智能体系统类**：Ren等提出包含规划器、记忆、动作空间、验证器的Agent分类；Gridach区分全自主与人机协作系统；Strickland等采用模式门控分离对话权与执行权。本文的Conductor对应“指令型规划器”，但创新在于确定性层完全排除LLM，实现意图到工作流的无歧义映射；且Skills作为专家编写的“外部知识库”，与现有分类中的学习或检索知识不同。

3. **知识落地策略类**：现有方法包括少样本提示（临时有效但不可审计）、模式定义（仅含操作约束）、RAG（检索非确定性且内容非领域特化）。本文的Skills处于独特位置：由领域专家以Markdown编写，无需嵌入或训练数据，通过确定性领域路由（而非相似度搜索）被Agent调用，同时服务于语义解释（如“European”映射为“EUR”）和操作优化（数据暂存策略），这种双重设计在现有文献中未见对应。

### Q3: 论文如何解决这个问题？

论文通过构建一个三层的智能体架构来将自然语言的研究问题转化为可执行的科学工作流。核心方法是将问题分解为语义层、知识层和确定性层三个层次。整体框架由四个智能体和一个外部基础设施层组成：Conductor作为用户入口和编排器，负责接收查询、路由、多轮对话和人工验证；Workflow Composer处理意图解释和DAG生成，它利用LLM和领域Skills从自然语言中提取结构化意图（如种群代码EUR），并在基础设施就绪后生成最终的工作流DAG；Deployment Service负责配置执行环境（如创建Kubernetes命名空间、下载数据和测量实际资源）；Execution Sentinel负责监控运行中的工作流状态。关键技术包括：1) Skills作为知识层，由领域专家编写的Markdown文档，编码词汇映射、参数约束和优化策略，在消融实验中将完全匹配意图准确率从44%提升到83%；2) 延迟DAG生成机制，在基础设施配置后根据实际测量的数据大小和可用vCPU来校准并行度，减少了92%的数据传输；3) 通过ResearchIntent模式约束LLM输出，将非确定性限制在语义层的意图提取阶段，确保相同意图产生相同工作流，实现了完全的可审计性。整个端到端流水线在Kubernetes上运行，LLM开销低于15秒，每次查询成本低于0.001美元。

### Q4: 论文做了哪些实验？

论文在三个层次上评估了所提架构。首先，在意图提取消融实验中，使用150条自然语言查询（分为5个难度等级）和1000 Genomes群体遗传学工作流（包含26个人群代码、5个超级群体、24条染色体、8个命名区域），对比了GPT-5.4、GPT-4.1-mini和Claude Opus 4.6在四种Skill配置下的性能。无Skill时（S0）全匹配准确率最高为44%（Claude Opus），而加载全部Skill（S3）后提升至83.3%，其中词汇Skill（S1）贡献了主要提升（+36个百分点）。对于显式查询（T1-T2），所有模型达到100%；对隐性推断（T3），Opus达到86.7%。

其次，在延迟生成实验中，比较了6个基因组区域（HLA、BRCA1/2等）的预估并行度与实际测量值，展示了数据传输减少92%（从21.6GB降至1.69GB），对小型基因区域（HBB、APOE）节省超过99.9%。

最后，在Kubernetes集群（48 vCPU）上执行了3个端到端查询，结果显示LLM开销仅11-14秒（成本低于$0.001/查询），总执行时间10-145分钟，意图准确率5/5字段，0任务失败。与人工规范相比，该架构将30-50分钟的多步骤专家工作缩减至106秒。

### Q5: 有什么可以进一步探索的点？

该论文的主要局限性在于验证范围局限于单一领域（1000 Genomes），每个新领域都需要重新构建Skills和确定性生成器，限制了跨领域迁移效率。未来可探索以下方向：1）开发半自动化的Skills生成工具，利用大语言模型辅助领域专家提取领域词汇和约束规则，降低人工编写成本；2）构建可复用的Skill库和生成器模板库，通过迁移学习实现跨领域快速适配；3）引入执行反馈循环，将工作流运行中的性能数据（如数据倾斜、资源利用率）作为强化学习信号，自动优化参数并行度和数据分区策略；4）对T3层级隐含推理失败的问题，可尝试混合Skill格式（如结合知识图谱与Markdown）或采用多轮对话机制进行逐步推理；5）探索将确定性生成器与符号推理系统结合，处理需要深层领域逻辑的复杂转换。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种分层智能体架构，用于自动化从研究问题到科学工作流的语义转化。当前科学家需手动将研究问题转换为工作流规范，这既需要领域知识又需要基础设施专长。该架构通过三个层级解决此问题：语义层利用大语言模型将自然语言解释为结构化意图；确定性层通过已验证的生成器产生可复现的工作流有向无环图；知识层由领域专家以Markdown文档形式编写“技能”，编码词汇映射、参数约束和优化策略。这种分解将LLM的不确定性限制在意图提取阶段，确保相同意图总是产生相同工作流。在千人基因组群体遗传学工作流和Kubernetes上的Hyperflow工作流管理系统的评估中，技能将完全匹配准确率从44%提升至83%；延迟生成将数据传输减少92%；端到端管道查询耗时低于15秒，成本低于0.001美元。该架构通过分离非确定性与确定性组件，在保证可复现性的同时显著提升了自动化水平。
