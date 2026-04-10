---
title: "Towards Knowledgeable Deep Research: Framework and Benchmark"
authors:
  - "Wenxuan Liu"
  - "Zixuan Li"
  - "Bai Long"
  - "Chunmao Zhang"
  - "Fenghui Zhang"
  - "Zhuo Chen"
  - "Wei Li"
  - "Yuxin Zuo"
  - "Fei Wang"
  - "Bingbing Xu"
  - "Xuhui Jiang"
  - "Jin Zhang"
  - "Xiaolong Jin"
  - "Jiafeng Guo"
  - "Tat-Seng Chua"
  - "Xueqi Cheng"
date: "2026-04-09"
arxiv_id: "2604.07720"
arxiv_url: "https://arxiv.org/abs/2604.07720"
pdf_url: "https://arxiv.org/pdf/2604.07720v1"
categories:
  - "cs.AI"
tags:
  - "多智能体架构"
  - "深度研究"
  - "结构化知识"
  - "基准评测"
  - "报告生成"
  - "工具使用"
  - "混合知识分析"
relevance_score: 8.5
---

# Towards Knowledgeable Deep Research: Framework and Benchmark

## 原始摘要

Deep Research (DR) requires LLM agents to autonomously perform multi-step information seeking, processing, and reasoning to generate comprehensive reports. In contrast to existing studies that mainly focus on unstructured web content, a more challenging DR task should additionally utilize structured knowledge to provide a solid data foundation, facilitate quantitative computation, and lead to in-depth analyses. In this paper, we refer to this novel task as Knowledgeable Deep Research (KDR), which requires DR agents to generate reports with both structured and unstructured knowledge. Furthermore, we propose the Hybrid Knowledge Analysis framework (HKA), a multi-agent architecture that reasons over both kinds of knowledge and integrates the texts, figures, and tables into coherent multimodal reports. The key design is the Structured Knowledge Analyzer, which utilizes both coding and vision-language models to produce figures, tables, and corresponding insights. To support systematic evaluation, we construct KDR-Bench, which covers 9 domains, includes 41 expert-level questions, and incorporates a large number of structured knowledge resources (e.g., 1,252 tables). We further annotate the main conclusions and key points for each question and propose three categories of evaluation metrics including general-purpose, knowledge-centric, and vision-enhanced ones. Experimental results demonstrate that HKA consistently outperforms most existing DR agents on general-purpose and knowledge-centric metrics, and even surpasses the Gemini DR agent on vision-enhanced metrics, highlighting its effectiveness in deep, structure-aware knowledge analysis. Finally, we hope this work can serve as a new foundation for structured knowledge analysis in DR agents and facilitate future multimodal DR studies.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）智能体在执行深度研究（Deep Research, DR）任务时，难以有效利用和处理大规模结构化知识（如表格、图表）的局限性。研究背景是，随着LLM智能体在数学、软件工程等复杂任务上展现出强大能力，深度研究——即要求智能体自主进行多步骤信息检索、处理和推理以生成全面报告——已成为一个关键方向。然而，现有方法主要依赖网络搜索非结构化内容或使用预定义工具生成简短回答，它们无法灵活地对大规模结构化知识进行推理，导致在回答需要数据支撑和定量分析的复杂问题时（例如“2025年全球ESG投资的区域差异由哪些因素造成？”），难以进行深入、全面的研究。

现有方法的不足在于：它们要么过度依赖网络搜索，缺乏对结构化数据的处理能力；要么采用固定工具，灵活性差，无法整合结构化知识进行深度分析。结构化知识对于提供坚实的数据基础、促进定量计算和实现深入分析至关重要，但现有DR智能体在此方面存在明显短板。

因此，本文要解决的核心问题是：如何让DR智能体不仅能处理非结构化文本信息，还能有效利用结构化知识，以生成融合文本、图表的多模态、证据翔实的深度研究报告。为此，论文提出了一个名为“知识性深度研究”（Knowledgeable Deep Research, KDR）的新任务，并设计了混合知识分析框架（HKA）来应对这一挑战。同时，为了系统评估，论文构建了涵盖多领域、包含大量结构化知识资源的基准测试KDR-Bench。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕深度研究智能体（Deep Research Agent）和深度研究评测基准（Deep Research Benchmarks）两大类展开。

在深度研究智能体方面，相关工作可分为两类。一是工业界的应用，如Gemini和Perplexity，它们将深度研究视为高级智能体推理和工具使用能力的体现。二是开源社区的努力，旨在通过构建稳健的多智能体工作流来模拟闭源系统，或通过智能体强化学习训练大语言模型掌握复杂工具。然而，现有研究大多侧重于处理非结构化网络内容，对结构化知识的计算和推理支持有限。本文提出的HKA框架及其核心的“结构化知识分析器”，通过结合编码和视觉语言模型来生成图表与洞察，明确增强了在深度研究中对结构化知识的分析与整合能力，这是与现有工作的主要区别。

在深度研究评测基准方面，相关工作主要分为复杂问题解决（如Humanity's Last Exam和BrowserComp）和长报告生成（如DeepResearch Bench和Personal DR）两类。现有报告生成基准通常侧重于文本信息聚合，难以精细评估智能体利用知识进行定量分析和得出新颖结论的能力。本文构建的KDR-Bench则专门设计用于评估深度研究智能体的知识分析能力，其覆盖多领域、包含大量结构化知识资源（如表格），并引入了知识中心和视觉增强等新型评估指标，从而弥补了现有基准的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为混合知识分析框架（HKA）的多智能体架构来解决知识性深度研究（KDR）任务，该框架旨在协同处理结构化和非结构化知识，并生成包含文本、图表的多模态综合报告。其核心方法是设计一个由四个专门子智能体组成的模块化系统，通过分工协作完成从问题分解到报告生成的整个流程。

整体框架始于规划器（Planner），它负责接收研究问题，将其分解为一系列细粒度的子任务，并动态决定每个子任务所需的知识类型（结构化或非结构化），从而调用相应的分析器。这种基于任务规划的流程控制确保了研究过程的系统性和适应性。

框架的主要模块包括：1）结构化知识分析器（SKA），这是该框架的关键创新组件。它专门处理表格等结构化数据，采用“检索-重排”管道获取相关表格，并利用代码大语言模型生成和执行定制化计算代码，以进行灵活的数据分析和可视化（如生成图表）。为了提升效率，它仅将表格模式以注释形式提示给模型，而非注入全部数据，显著减少了令牌消耗。此外，该模块引入了重试机制来处理代码执行失败或输出无效的情况，将执行失败率从31.7%大幅降低至0.51%。结果分析阶段则使用视觉语言模型（VLM）对生成的图表进行分析并提炼见解，同样通过验证重试机制将失败率从55.5%降至1.7%。2）非结构化知识分析器（UKA），负责处理网络内容等非结构化知识。它通过意图生成将简短查询扩展为详细搜索意图，随后进行网络搜索并将结果转换为Markdown格式，最后进行信息摘要，为规划器提供浓缩的关键信息。3）撰写器（Writer），分两步整合材料：首先在完成每个子任务时进行子任务写作，生成保留多模态材料的提纲并填充文本；最后在所有子任务完成后进行最终精炼，调整报告结构、消除冗余与不一致，形成连贯的高质量多模态报告。

该框架的创新点在于首次明确区分并深度融合了两种知识源的处理流程，特别是通过SKA模块实现了对大规模结构化数据的深度计算与洞察生成，并利用多智能体协作与迭代验证机制显著提升了分析的可靠性和报告的多模态整合能力。

### Q4: 论文做了哪些实验？

论文在自建的KDR-Bench基准上进行了系统性实验，该基准涵盖9个领域、包含41个专家级问题，并整合了大量结构化知识资源（如1252个表格）。实验设置方面，作者将提出的混合知识分析框架（HKA）与三类基线方法进行了对比：1）配备搜索工具的大语言模型（如Hunyuan2.0、GLM4.6、Qwen3-Max、Minimax-M2）；2）闭源深度研究智能体（如OpenAI Deep Research、Grok、Perplexity、Gemini）；3）开源深度研究智能体（如Tongyi、Enterprise、LangChain、ThinkDepth）。其中，部分开源智能体被调整为三种搜索设置：仅网页搜索、仅表格搜索、混合搜索。HKA使用Qwen3-235B-A22B作为规划器和写作者的主干模型，并专门设计了结构化知识分析器（使用Qwen3-Coder-480B和Qwen3-VL-235B模型）来处理表格与生成图表。

主要结果基于三类评估指标。在通用指标上，HKA的平均得分超越了除Gemini外的所有基线，相比使用相同主干模型的开源智能体（如LangChain、ThinkDepth）平均高出2.1分以上，表明其能有效融合结构化与非结构化知识生成高质量报告。在知识中心指标上，HKA在主结论对齐（Main Conclusion Alignment）上仅次于Gemini但差距微小，而在关键点覆盖率（Key Point Coverage）和关键点支持度（Key Point Supportiveness）上均优于所有基线（分别超出至少3.4分和6.6分），凸显了其深度分析结构化知识的优势。在视觉增强指标上，HKA的平均得分达到56.1，显著超越了Gemini（41.7），并在多个领域（如农业、科技）取得高分，证明了其生成多模态内容（图表）的有效性。实验还发现，仅使用表格搜索的智能体在分析深度上通常优于仅网页搜索，但简单的混合搜索并未带来显著提升，而HKA通过深度整合两类知识实现了更优性能。

### Q5: 有什么可以进一步探索的点？

本文提出的KDR任务和HKA框架在结合结构化与非结构化知识方面迈出了重要一步，但其探索仍处于初期，存在多个可深入的方向。首先，框架的**知识整合深度**有待加强，当前方法对结构化数据的分析可能仍停留在表层统计，未来可探索更复杂的因果推断或预测模型，使代理能从数据中挖掘更深层的关联与洞见。其次，**评估体系**虽已提出多类指标，但如何更精准地衡量“深度分析”的质量仍是挑战，可能需要引入领域专家评分或基于事实一致性的更细粒度评估。此外，**多模态报告生成**的连贯性与可解释性可以进一步提升，例如让代理能动态选择最合适的图表类型并生成更自然的图文描述。从更广阔的视角看，未来研究可探索让代理在长期任务中持续学习与更新知识库，或处理实时流式结构化数据（如金融市场数据），这将更贴近实际应用场景。最后，推动**开源基准与框架**的社区共建，覆盖更多样化的领域与知识形态，将加速该方向的发展。

### Q6: 总结一下论文的主要内容

该论文提出了“知识化深度研究”（KDR）这一新任务，旨在让大语言模型（LLM）智能体在生成综合性报告时，不仅利用传统的非结构化网络内容，还必须整合结构化知识（如表格数据），以提供坚实的数据基础、支持定量计算并实现深入分析。为此，作者构建了“混合知识分析”（HKA）框架，这是一个多智能体架构，其核心设计是“结构化知识分析器”，它结合编码和视觉语言模型来处理结构化数据，生成图表、表格及相关洞察，并将文本、图表与表格整合成连贯的多模态报告。为支持系统评估，论文创建了KDR-Bench基准，涵盖9个领域、包含41个专家级问题及大量结构化知识资源（如1252个表格），并标注了每个问题的主要结论和关键点，提出了通用、知识中心和视觉增强三类评估指标。实验表明，HKA在通用和知识中心指标上持续优于现有大多数深度研究智能体，在视觉增强指标上甚至超越了Gemini DR智能体，验证了其在深度、结构感知的知识分析中的有效性。这项工作为深度研究智能体中的结构化知识分析奠定了新基础，并推动了未来多模态深度研究的发展。
