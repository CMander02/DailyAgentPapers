---
title: "TASER: Table Agents for Schema-guided Extraction and Recommendation"
authors:
  - "Nicole Cho"
  - "Kirsty Fielding"
  - "William Watson"
  - "Sumitra Ganesh"
  - "Manuela Veloso"
date: "2025-08-18"
arxiv_id: "2508.13404"
arxiv_url: "https://arxiv.org/abs/2508.13404"
pdf_url: "https://arxiv.org/pdf/2508.13404v4"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.IR"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "工具使用"
  - "数据合成/提取"
  - "持续学习"
  - "表格处理"
  - "金融应用"
relevance_score: 7.5
---

# TASER: Table Agents for Schema-guided Extraction and Recommendation

## 原始摘要

Real-world financial filings report critical information about an entity's investment holdings, essential for assessing that entity's risk, profitability, and relationship profile. Yet, these details are often buried in messy, multi-page, fragmented tables that are difficult to parse, hindering downstream QA and data normalization. Specifically, 99.4% of the tables in our financial table dataset lack bounding boxes, with the largest table spanning 44 pages. To address this, we present TASER (Table Agents for Schema-guided Extraction and Recommendation), a continuously learning, agentic table extraction system that converts highly unstructured, multi-page, heterogeneous tables into normalized, schema-conforming outputs. Guided by an initial portfolio schema, TASER executes table detection, classification, extraction, and recommendations in a single pipeline. Our Recommender Agent reviews unmatched outputs and proposes schema revisions, enabling TASER to outperform vision-based table detection models such as Table Transformer by 10.1%. Within this continuous learning process, larger batch sizes yield a 104.3% increase in useful schema recommendations and a 9.8% increase in total extractions. To train TASER, we manually labeled 22,584 pages and 3,213 tables covering $731.7 billion in holdings, culminating in TASERTab to facilitate research on real-world financial tables and structured outputs. Our results highlight the promise of continuously learning agents for robust extractions from complex tabular data.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决从高度非结构化、多页、异构的金融监管文件（特别是基金年度报告中的财务持仓表）中提取结构化信息的难题。研究背景是，全球高达68.9万亿美元的投资信息记录在这些财务持仓表中，这些数据对于风险评估、盈利分析和关系图谱构建至关重要。然而，这些表格通常跨越多页、格式混乱、缺乏边界框（数据集中99.4%的表格无边界框），且布局高度异构，混合了文本块、脚注和图像，使得传统基于视觉或规则的表提取方法失效。

现有方法的不足主要体现在：1）传统表格检测或结构识别模型（如Table Transformer）在处理文档与表格一对多关系、跨页表格以及无边界框的复杂布局时性能不佳；2）现有研究多集中于网页或SQL等规整表格，缺乏针对金融持仓表这种极端异构场景的持续学习提取方法；3）金融工具结构复杂，信息常嵌套在单个单元格内，进一步增加了解析难度。

本文要解决的核心问题是：如何设计一个能够持续学习、自适应模式引导的智能体系统，以端到端的方式从杂乱的多页金融表格中实现鲁棒的检测、分类、信息提取和模式推荐，并输出规范化的结构化数据。为此，论文提出了TASER系统，通过智能体驱动的解析和自优化循环，在缺乏明确视觉边界的情况下实现准确提取，并利用推荐智能体不断迭代改进初始数据模式，从而提升整体提取效果和系统适应性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 信息与表格提取方法**：早期工作依赖统计模型（如隐马尔可夫模型、条件随机场）和基于启发式或图布局的方法，但在处理复杂、异构表格时仍存在困难。本文提出的TASER系统则采用持续学习的智能体（Agent）管道，能更好地应对缺乏边界框、跨多页的碎片化表格。

**2. 表格表示学习**：基于Transformer的模型（如TaPaS、TaBERT、TableFormer等）专注于编码文本、结构和布局信息，但大多未在冗长、密集的多页财务报告上进行充分评估。TASER针对此类真实金融表格进行了专门设计和验证。

**3. 大语言模型（LLM）与结构化数据**：通用LLM通过微调和提示工程在模式匹配提取中表现出色，多模态方法（如LayoutLM、DONUT、Table Transformer）增强了布局感知能力，但在处理长表格和碎片化表格时性能仍不足。TASER通过智能体驱动的推荐机制进行模式修订，实现了持续优化，超越了单纯基于视觉的检测模型。

**4. 金融文档解析**：相关研究侧重于从图像中提取表格，或构建专家智能体管道。大规模基准数据集（如DocILE、BuDDIE）也聚焦于金融文档。本文贡献了TASERTab数据集，包含大量人工标注的财务表格，以促进该领域研究。

**5. 智能体与递归提取**：近期研究将LLM视为可进行迭代提取和自我修正的智能体，通过基于提示的反馈、内省优化和情景记忆框架来提升复杂提取任务的推理能力。TASER的推荐智能体（Recommender Agent）延续了这一方向，通过审查未匹配输出并提出模式修订建议，实现了系统的持续学习与性能提升。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为TASER的持续学习、智能体驱动的表格提取系统来解决复杂金融表格的解析与归一化问题。其核心方法围绕一个由三个大型语言模型（LLM）智能体组成的管道，并采用模式引导和迭代优化的设计思想。

**整体框架与主要模块**：
TASER的系统架构是一个包含检测、提取和推荐三个核心智能体的自动化流水线。
1.  **检测智能体（Detector Agent）**：负责从多页文档中识别出可能包含目标金融持仓表格的候选页面。其提示词经过优化以追求高召回率，确保不遗漏任何相关表格。
2.  **提取智能体（Extractor Agent）**：核心处理模块。它接收检测到的页面，并将当前定义的投资组合模式（Portfolio Schema）嵌入到给LLM的提示上下文中。LLM根据模式指导生成结构化输出，该输出会通过Pydantic和Instructor库进行即时验证和类型检查，最终产生符合模式定义的、类型安全的金融工具条目。
3.  **推荐智能体（Recommender Agent）**：系统持续学习的关键。它负责审查未能与当前模式匹配的提取结果（包括误报和真阳性）。该智能体首先基于当前模式重新验证以过滤误报，然后针对剩余的真阳性（即有效但模式无法分类的持仓字段），提出最小化的模式修改建议。

**关键技术流程与创新点**：
1.  **模式引导的提取（Schema-Guided Extraction）**：整个提取过程以一个明确的、用户可修改的Portfolio Schema为锚点。该模式使用Pydantic模型实现，定义了目标表格的结构和验证逻辑。将完整模式嵌入提示词的方法（Full Schema Prompting）被证明在精度、F1分数和金额保真度上均优于其他策略。
2.  **递归反馈与迭代优化循环**：TASER实现了一个核心的创新闭环。提取后未匹配的条目会触发推荐智能体进行分析并生成模式更新建议。用户批准建议后，系统自动更新模式缓存并重新运行整个提取管道。这个过程循环进行，直到所有条目都被成功匹配或无法进一步改进。这种设计使系统能够从错误中学习，并动态适应表格中出现的新的、未知的持仓类型。
3.  **批处理驱动的模式推荐算法**：论文将模式精炼形式化为一个LLM驱动的迭代聚类过程。算法将未匹配的持仓集合分批（批次大小B）送入推荐函数，聚合建议后更新模式并重新提取。实验发现，较大的批次大小能显著增加（104.3%）有效的模式建议数量并提升总提取量，但可能更快达到性能平台。
4.  **集成验证与结构化输出**：在每个智能体的前向传播过程中都集成了输出验证（通过Instructor），确保了中间和最终结果的结构化与一致性。整个系统部署在云架构上，实现了任务编排、状态持久化和错误处理的自动化。

综上所述，TASER通过多智能体协作、以动态演进的模式为核心指导，并结合一个闭环的、持续学习的反馈机制，系统地解决了从高度非结构化、多页、异质金融表格中进行鲁棒信息提取的难题。

### Q4: 论文做了哪些实验？

论文实验主要包括检测、提取和模式推荐三部分。实验设置上，使用GPT-4o-2024-11-20作为核心LLM，在一个包含22,584页、3,213个表格（总资产价值7,317亿美元）的金融表格数据集上进行评估，其中所有持仓表均为分层结构，60.2%跨多页。对比方法包括基于视觉的Table Transformer模型以及不同的提示策略（如原始文本提示、结构化思维链等）。

检测实验以召回率、精确率、F1和准确率为指标。TASER在完整模式提示下实现了接近100%的召回率，精确率达43.4%，F1为59.4%，优于Table Transformer（精确率32.8%，F1 49.3%）。提取实验通过总绝对差（TAD）衡量提取完整性，完整模式提示的TAD最低（1.028亿美元），未计入份额仅0.014%。模式推荐实验关注覆盖率、多样性和碰撞率等指标，结果表明较大批次（如250、500）能快速扩展模式，使有用模式推荐增加104.3%，总提取量提升9.8%，但会导致早期饱和；较小批次则能获得更高的模式多样性（以平均Levenshtein距离衡量），但冗余更高。通过解决最大的未匹配持仓，TAD可降低约7-10%。

### Q5: 有什么可以进一步探索的点？

TASER的局限性为未来研究提供了明确方向。首先，系统对低质量扫描文档的敏感性表明，需要增强视觉鲁棒性，例如结合超分辨率技术或更强大的文档图像增强模块。其次，依赖提示的弱监督和缺乏细粒度标注数据限制了泛化能力，未来可探索半监督或自监督学习，利用大量未标注金融文档构建预训练模型。第三，未建模行间关系与金融工具关联，影响了深层分析（如风险聚合），后续可引入图神经网络或结构化预测来捕获表格内部的语义依赖。此外，递归提示导致的延迟问题可通过优化代理调度、引入异步处理或模型蒸馏来缓解。最后，TASER的持续学习机制可扩展至跨领域表格（如医疗、法律），并探索多模态融合（结合文本段落与表格上下文）以解决文档歧义，从而构建更通用、高效的表格智能体系统。

### Q6: 总结一下论文的主要内容

该论文提出了TASER系统，旨在解决金融文件中复杂、多页、无边界框的表格信息提取难题。其核心贡献是设计了一个持续学习的智能体驱动框架，能够将高度非结构化的表格数据转化为符合预定模式的规范化输出。方法上，TASER通过一个初始投资组合模式引导，在单一流程中集成了表格检测、分类、提取和模式推荐功能；其独特的推荐代理能审查不匹配的输出并主动提出模式修订建议，实现了系统的自我优化。主要结论显示，TASER在表格检测上比基于视觉的Table Transformer模型性能提升10.1%，且持续学习中的大批量处理能显著提升有效模式推荐数量和总体提取量。这项工作不仅构建了大规模标注数据集TASERTab以促进相关研究，更验证了持续学习智能体在处理复杂表格数据、实现稳健信息提取方面的巨大潜力。
