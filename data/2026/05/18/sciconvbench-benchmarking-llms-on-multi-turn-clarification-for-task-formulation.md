---
title: "SCICONVBENCH: Benchmarking LLMs on Multi-Turn Clarification for Task Formulation in Computational Science"
authors:
  - "Nithin Somasekharan"
  - "Youssef Hassan"
  - "Shiyao Lin"
  - "Gihan Panapitiya"
  - "Patrick Emami"
  - "Anurag Acharya"
  - "Sameera Horawalavithana"
  - "Shaowu Pan"
date: "2026-05-18"
arxiv_id: "2605.18630"
arxiv_url: "https://arxiv.org/abs/2605.18630"
pdf_url: "https://arxiv.org/pdf/2605.18630v1"
github_url: "https://github.com/csml-rpi/SciConvBench"
categories:
  - "cs.AI"
  - "physics.comp-ph"
tags:
  - "Scientific AI Agent"
  - "Multi-Turn Dialogue"
  - "Task Formulation"
  - "Clarification"
  - "Benchmark"
  - "Computational Science"
  - "LLM Evaluation"
  - "Disambiguation"
  - "Inconsistency Resolution"
relevance_score: 8.5
---

# SCICONVBENCH: Benchmarking LLMs on Multi-Turn Clarification for Task Formulation in Computational Science

## 原始摘要

Large Language Models (LLMs) are increasingly deployed as scientific AI as- sistants, and a growing body of benchmarks evaluates their capabilities across knowledge retrieval, reasoning, code generation, and tool use. These evaluations, however, typically assume the scientific problem is already well-posed, whereas practical scientific assistance often begins with an ill-posed user request that must be refined through dialogue before any computation, analysis, or experiment can be carried out reliably. We introduce SCICONVBENCH, a benchmark for multi- turn clarification in scientific task formulation across four computational science problem domains: fluid mechanics, solid mechanics, materials science, and par- tial differential equations (PDEs). SCICONVBENCH targets two complementary capabilities: eliciting missing information (disambiguation) and detecting and correcting erroneous requests containing internally contradictory information (in- consistency resolution). Our benchmark pairs a structured task ontology with a rubric-based evaluation framework, enabling systematic measurement of LLM per- formance across three dimensions: clarification behavior, conversational grounding, and final-specification fidelity. Current frontier models perform relatively well on inconsistency resolution, but even the best model resolves only 52.7% of the disambiguation cases in fluid mechanics. We further find that frontier LLMs fre- quently make silent assumptions and perform implicit specification repairs that are not grounded in the conversation with users. SCICONVBENCH establishes a foundation for evaluating the upstream conversational reasoning that a reliable computational science assistant requires. The code and data can be found at https://github.com/csml-rpi/SciConvBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有科学AI基准评估中的一个关键缺口：大语言模型（LLMs）在处理不完整或存在内在矛盾的科学问题时，缺乏多轮澄清与任务规范化能力。当前的科学计算基准（如代码生成、工具使用）通常假设问题已良好定义，用户能提供清晰、完整且一致的任务描述。然而，实际科学实践中的初始需求往往是“病态”的，例如缺失关键参数（如雷诺数）、包含不兼容的材料属性或存在矛盾的数值约束。如果模型直接在这些不明确的输入上执行计算或代码生成，可能导致物理上无效、不可重复或与用户意图不符的结果。现有的一般性澄清基准（如CLAMBER）和通用信息寻求任务，无法反映计算科学领域特有的知识密集型和物理约束严格的澄清需求。为此，论文提出了SCICONVBENCH基准，核心问题是评估LLMs能否通过多轮对话，主动识别并纠正用户请求中的缺失信息（歧义消解）和矛盾信息（不一致解析），最终生成一个可可靠执行的科学任务规范，从而将评估重心从“解决问题的能力”前移至“正确定义问题的能力”。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可以分为以下三类：

1. **澄清与歧义消解类**：包括Qulac、ClariQ、ClarQ等问答澄清基准，以及AmbigQA、CAmbigNQ等处理歧义问答的数据集。CLAMBER、CondAmbigQA、CLAM等进一步形式化歧义分类和条件性澄清。与本文的区别在于，这些工作处理的歧义主要是多义词选择、搜索子主题偏好或用户偏好等日常场景，而SCICONVBENCH专注于计算科学领域的专业歧义消解。

2. **多轮对话与智能体评估类**：包括MT-Bench、Chatbot Arena等对话质量评估，以及AgentBench、WebArena、GAIA等智能体基准。τ-bench、MirrorBench等研究使用LLM模拟用户评估。本文与它们的关键区别是聚焦于科学任务执行前的对话澄清阶段，而非整体对话质量或工具执行能力。

3. **科学基准与领域智能体类**：包括SciBench、SciCode等科学推理基准，以及OpenFOAMGPT、FEABench、HoneyComb等计算科学领域智能体。这些工作假定科学问题已明确给定，而SCICONVBENCH关注的是其上游步骤——通过多轮对话澄清不完善或矛盾的初始需求，确保后续科学计算具有可靠基础。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为SCICONVBENCH的基准测试来评估和提升LLMs在多轮对话中澄清科学任务定义的能力。核心方法涉及两个方面：精心设计的数据集构建和全面的评估框架。

在数据集构建上，作者首先从流体力学、固体力学、材料科学和偏微分方程四个领域收集并整理出一批结构清晰、定义明确的科学问题（即“干净任务”）。每个任务被分解为一个包含九个要素（如目标、几何、模型、属性、边界条件等）的任务本体。然后，通过人工方式对每个干净任务进行“扰动”，生成初始的用户请求。扰动分为两类：一是“缺失”信息，即故意省略关键参数；二是“冲突”信息，即植入相互矛盾的描述。每个扰动都被明确标注，确保基准测试的难度源于任务定义本身。

评估框架的核心是一个基于“标尺”的自动化评判系统。该评判系统会分析完整的对话记录和最终生成的规范说明，从三个维度评估模型性能：**生成规范的正确性与意图保真度**（即最终规范是否解决了所有问题且符合用户原意）、**对话基础**（即问题是否通过与用户的明确澄清对话解决，而非模型自行“沉默假设”或“隐式修复”）。最终性能通过“最终解决率”（FRR）和“对话基础解决率”（CGRR）等指标量化。创新点在于：1) 提出了一个结构化科学任务本体，为信息缺失和冲突提供了精确的“地面真相”；2) 开发了能够区分模型是“真正通过对话解决”还是“自行猜测或修复”的评估方法；3) 实现了对模型在澄清行为、对话基础和最终规范保真度三个维度的系统化测量。实验发现，即使是当前最先进的模型，在解决某些领域（如流体力学）的歧义问题时表现也不佳，且经常在对话中做出未与用户沟通的“沉默假设”。

### Q4: 论文做了哪些实验？

论文在SCICONVBENCH基准上进行了多轮对话澄清实验，涵盖流体力学、固体力学、材料科学和偏微分方程四个领域。实验设置包括两个任务：信息缺失的消歧和内部矛盾的解析。评估了GPT-5.2、Gemini 2.5 Pro等前沿LLM，主要指标为最终解析率(FRR)，并细分为对话接地解析率(CGRR)和静默解析率(SRR)。结果显示所有模型在FRR与CGRR间均存在差距，消歧任务平均8.2个百分点，矛盾解析平均14.7个百分点。最优模型GPT-5.2在消歧任务中流体力学领域仅解决52.7%的案例，而Gemini 2.5 Pro在矛盾解析中最强。组件级分析发现数值方法和物理假设是最脆弱组件。鲁棒性检验使用80个子集，在不同裁判模型、提示变体(原始与Variant A/B差异约5个百分点FRR)和用户模拟器下结论稳定。人-裁判一致率达87.5% FRR。额外进行了帕累托分析评估能力、鲁棒性和可用性。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于当前模型在科学任务澄清中表现出“沉默假设”倾向，即模型倾向于自行填充缺失信息或修正矛盾，而非通过对话实际验证，严重影响科学可复现性。未来可探索以下方向：第一，构建显式的“不确定性询问机制”，强制模型在关键假设（如数值方法、物理假设）上向用户确认，避免隐式修复；第二，将问题本体（如流体力学中的数值求解器选择）转化为可查询的约束集，使模型能主动检测信息缺口；第三，设计多轮对话中的“可靠性量表”，实时量化每轮澄清是否真正消解了歧义或矛盾；第四，结合反事实推理，要求模型在给出最终规范时同步输出其假设前提的置信度分布。这些改进将推动LLM从“能回答”向“能可靠地合作定义问题”演进。

### Q6: 总结一下论文的主要内容

论文提出了SCICONVBENCH基准，专门评估大语言模型(LLM)在计算科学任务制定中的多轮澄清能力。不同于现有基准假设科学问题已明确定义，该工作针对真实场景中用户初始请求常不明确或不一致的问题，涵盖流体力学、固体力学、材料科学和偏微分方程四个领域。基准设计两个核心任务：澄清缺失信息(消歧)和检测修正矛盾信息(不一致性解决)。通过结构化任务本体和基于评分标准的评估框架，从澄清行为、对话基础和最终规范忠实度三个维度系统测量模型表现。主要结论显示，前沿模型在矛盾解决上相对较好，但最佳模型在流体力学消歧案例中仅解决52.7%，且常进行未与用户对话确认的隐式假设和规范修复。该基准开创性地将对话式任务制定作为可靠科学助手所需的上游能力进行可测量评估。
