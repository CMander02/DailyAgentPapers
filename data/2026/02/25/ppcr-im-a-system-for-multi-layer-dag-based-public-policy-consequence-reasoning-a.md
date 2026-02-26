---
title: "PPCR-IM: A System for Multi-layer DAG-based Public Policy Consequence Reasoning and Social Indicator Mapping"
authors:
  - "Zichen Song"
  - "Weijia Li"
date: "2026-02-25"
arxiv_id: "2602.21650"
arxiv_url: "https://arxiv.org/abs/2602.21650"
pdf_url: "https://arxiv.org/pdf/2602.21650v1"
categories:
  - "cs.SI"
  - "cs.AI"
tags:
  - "LLM-driven Agent"
  - "Multi-step Reasoning"
  - "Decision Support System"
  - "Policy Analysis"
  - "Structured Output Generation"
  - "Causal Reasoning"
relevance_score: 7.5
---

# PPCR-IM: A System for Multi-layer DAG-based Public Policy Consequence Reasoning and Social Indicator Mapping

## 原始摘要

Public policy decisions are typically justified using a narrow set of headline indicators, leaving many downstream social impacts unstructured and difficult to compare across policies. We propose PPCR-IM, a system for multi-layer DAG-based consequence reasoning and social indicator mapping that addresses this gap. Given a policy description and its context, PPCR-IM uses an LLM-driven, layer-wise generator to construct a directed acyclic graph of intermediate consequences, allowing child nodes to have multiple parents to capture joint influences. A mapping module then aligns these nodes to a fixed indicator set and assigns one of three qualitative impact directions: increase, decrease, or ambiguous change. For each policy episode, the system outputs a structured record containing the DAG, indicator mappings, and three evaluation measures: an expected-indicator coverage score, a discovery rate for overlooked but relevant indicators, and a relative focus ratio comparing the systems coverage to that of the government. PPCR-IM is available both as an online demo and as a configurable XLSX-to-JSON batch pipeline.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决公共政策决策和评估中存在的关键问题：政策影响分析通常局限于少数几个“头条”指标（如GDP增长、通货膨胀率），而大量下游社会影响则缺乏结构化、可比较的量化分析。研究背景是，尽管“超越GDP”和多维福祉研究已表明传统指标的局限性，但在实践中，具体政策选择、中间机制与下游社会指标之间的关联仍主要隐含在叙述性报告或临时图表中，这使得政策后果推理难以在不同政策间进行比较、审计或复用。

现有方法的不足主要体现在三个方面：首先，现有工作流程难以系统性地枚举政策的中介后果；其次，缺乏将这些后果与一个固定的指标分类体系进行一致性关联的方法；最后，无法量化政府关注点与更广泛潜在影响之间的差异。现有的变革理论图或逻辑模型通常是针对单一项目手工制作的，且未与可复用的指标集对齐。

因此，本文要解决的核心问题是：如何将定性的政策后果推理转化为机器可读的结构化对象，以显式地连接政策、后果链和社会指标。为此，论文提出了PPCR-IM系统，它利用基于大语言模型的分层生成器，为给定的政策描述构建一个多层有向无环图来建模因果影响路径，并通过映射模块将图中的节点对齐到一个固定的社会指标集，并标注定性影响方向。该系统旨在使政策分析更加透明，并揭示那些超出政府官方仪表盘关注范围的影响。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在**方法类**研究中，传统的政策分析工具如“变革理论图”和逻辑模型通常为单一项目手工构建，缺乏可复用的结构化输出。本文提出的PPCR-IM系统则利用LLM驱动、分层生成的方法，自动构建具有多父节点依赖关系的多层有向无环图，将定性推理转化为机器可读的结构化对象，实现了过程的自动化和标准化。

在**应用类**研究中，现有“超越GDP”和多维福祉指标体系的研究虽已指出传统头条指标的局限性，但未能系统地将具体政策选择与下游社会指标动态关联起来。PPCR-IM通过一个映射模块，将DAG节点与一个固定的社会指标集对齐，并标注影响方向，从而在政策分析与多维社会影响评估之间建立了明确的、可比较的桥梁。

在**评测类**研究中，现有工作流程缺乏对政府关注点与更广泛潜在影响之间差异的量化评估。本文的创新在于系统输出了三项评估指标：预期指标覆盖率、被忽视相关指标的发现率，以及系统与政府关注范围的相对聚焦比。这为政策分析的透明度和审计提供了新的量化工具。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为PPCR-IM的系统来解决公共政策影响评估中指标覆盖范围窄、下游社会影响难以结构化比较的问题。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块**：系统采用模块化设计，包含三个主要模块，通过明确的数据流连接。1) **DAG生成器**：输入政策描述及其背景，利用大语言模型（LLM）以分层、广度优先的方式，从政策根节点开始，逐层生成中间后果节点，构建一个允许子节点拥有多个父节点的有向无环图，以捕捉联合影响。当多个父节点产生语义相似的子节点时，系统会将其合并，确保图的简洁性。2) **指标映射器**：将生成的DAG与一个预定义的固定社会指标词汇表对齐。对于每个指标，系统通过结构化提示查询LLM，判断该指标是否可能受政策影响，并为受影响的指标分配“增加”、“减少”或“模糊变化”的定性影响方向，同时记录支持该判断的DAG节点。3) **评估与导出层**：将系统输出的指标影响评估与参考标注（如政府关注的指标）进行比较，为每个政策案例生成包含DAG、指标映射和三项评估度量的结构化JSON记录。

**创新点与关键技术**：1) **多层DAG推理机制**：采用分层、受深度和分支因子约束的图扩展方法，结合显式的多父节点依赖结构，能更真实地模拟政策后果中分支与汇合的通路，超越了线性思维链的单一路径限制。2) **固定指标空间对齐**：将异质的后果图映射到统一的指标词汇表，确保了跨政策比较和统计聚合的可能性。3) **内置量化评估模块**：系统定义了三个核心评估指标——预期指标覆盖率（衡量系统恢复政府预期指标的比例）、被忽视指标发现率（识别相关但未被政府关注的指标的比例）以及模型-政府关注度比率（比较系统与政府覆盖范围的相对比例），从而系统性地量化分析广度与焦点差异。这种将基于图的分层后果推理、固定指标空间对齐以及专注于量化比较的评估模块相结合的设计，在现有工具中较为罕见。

### Q4: 论文做了哪些实验？

论文实验设置上，PPCR-IM系统通过Python模块和命令行接口实现，输入为包含政策描述的XLSX文件，系统使用LLM后端（可配置模型标识、生成温度等参数）逐层生成有向无环图（DAG）并进行指标映射，最终为每个政策案例输出包含DAG、指标映射和评估指标的JSON文件。

实验使用了包含1,027个政策案例的数据集，这些案例覆盖美国（41%）、日本（34%）、欧洲国家（23%）及其他地区（2%）。数据集中每个案例包含政策描述、背景信息，以及两个参考集：政府关注指标集和专家判定的相关指标集。评估基于三个指标：预期指标覆盖率（覆盖政府关注集的比例）、被忽视指标发现率（发现相关但未被政府强调的指标的比例）以及模型-政府关注比率（比较系统与政府覆盖范围的相对比例）。

主要对比方法是两个直接基于政策文本预测受影响指标的LLM基线模型（GPT 5.1和Doubao）。实验结果显示，PPCR-IM在所有三个评估指标上均优于基线。具体关键数据指标如下：预期指标覆盖率的均值达到0.902（标准差0.048），高于GPT 5.1的0.851和Doubao的0.803；被忽视指标发现率达到0.603（标准差0.092），显著高于基线的0.352和0.291；模型-政府关注比率为1.356，表明PPCR-IM在覆盖大部分预期指标的同时，系统性地拓宽了指标覆盖范围，而两个基线的比率分别为1.098和1.023。定性分析表明，PPCR-IM的DAG结构能揭示中间影响机制，从而识别出基线模型无法发现的额外相关指标。

### Q5: 有什么可以进一步探索的点？

该论文的PPCR-IM系统在政策影响结构化推理方面迈出了重要一步，但仍存在多个可深入探索的方向。首先，系统依赖LLM生成DAG，节点和关系可能泛化或存在偏差，未来可引入领域知识图谱或专家反馈循环进行迭代修正，提升推理的准确性和完整性。其次，影响方向仅为定性分类（增/减/模糊），缺乏量化评估，后续可结合实证数据或预测模型，尝试赋予影响程度或概率估计，增强实用性。此外，DAG仅表示合理机制而非因果验证，未来可探索融合反事实推理或因果发现技术，部分验证关键路径的因果效力。最后，评估依赖政府指标集和专家标注，可能受主观优先级影响，可考虑引入多源社会数据（如社交媒体、经济统计）构建更客观的基准，或开发动态指标库以捕捉新兴社会问题。总体而言，系统可向更量化、因果化、自适应化的方向演进，成为政策模拟与评估的强大工具。

### Q6: 总结一下论文的主要内容

该论文提出了PPCR-IM系统，旨在解决公共政策决策中仅依赖少数核心指标而忽略下游社会影响的局限性。核心贡献在于将定性的政策后果分析转化为基于多层有向无环图的结构化推理，并映射到固定的社会与宏观经济指标集。方法上，系统利用大语言模型分层生成政策后果的DAG，允许子节点拥有多个父节点以捕捉联合影响，再通过映射模块将节点与19个世界银行式指标对齐，并定性标注影响方向。实验基于1027个政策案例，结果显示系统在预期指标覆盖分数、被忽略指标发现率及模型与政府关注度比例上均优于基线模型。主要结论表明，显式建模中间后果结构能有效覆盖官方强调的指标，同时系统性地发现额外相关维度，为政策分析提供了更全面、可比较的框架。未来工作将增强图语义的因果标注，并拓展数据覆盖范围。
