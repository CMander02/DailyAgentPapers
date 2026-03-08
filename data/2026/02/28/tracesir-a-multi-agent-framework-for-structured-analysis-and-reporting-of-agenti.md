---
title: "TraceSIR: A Multi-Agent Framework for Structured Analysis and Reporting of Agentic Execution Traces"
authors:
  - "Shu-Xun Yang"
  - "Cunxiang Wang"
  - "Haoke Zhang"
  - "Wenbo Yu"
  - "Lindong Wu"
date: "2026-02-28"
arxiv_id: "2603.00623"
arxiv_url: "https://arxiv.org/abs/2603.00623"
pdf_url: "https://arxiv.org/pdf/2603.00623v1"
github_url: "https://github.com/SHU-XUN/TraceSIR"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Multi-Agent Systems"
  - "Tool Use & API Interaction"
relevance_score: 8.0
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "GLM-4.6"
  key_technique: "TraceSIR (StructureAgent, InsightAgent, ReportAgent), TraceFormat"
  primary_benchmark: "TraceBench (composed of BrowseComp, Tau2Bench, SWE-bench)"
---

# TraceSIR: A Multi-Agent Framework for Structured Analysis and Reporting of Agentic Execution Traces

## 原始摘要

Agentic systems augment large language models with external tools and iterative decision making, enabling complex tasks such as deep research, function calling, and coding. However, their long and intricate execution traces make failure diagnosis and root cause analysis extremely challenging. Manual inspection does not scale, while directly applying LLMs to raw traces is hindered by input length limits and unreliable reasoning. Focusing solely on final task outcomes further discards critical behavioral information required for accurate issue localization. To address these issues, we propose TraceSIR, a multi-agent framework for structured analysis and reporting of agentic execution traces. TraceSIR coordinates three specialized agents: (1) StructureAgent, which introduces a novel abstraction format, TraceFormat, to compress execution traces while preserving essential behavioral information; (2) InsightAgent, which performs fine-grained diagnosis including issue localization, root cause analysis, and optimization suggestions; (3) ReportAgent, which aggregates insights across task instances and generates comprehensive analysis reports. To evaluate TraceSIR, we construct TraceBench, covering three real-world agentic scenarios, and introduce ReportEval, an evaluation protocol for assessing the quality and usability of analysis reports aligned with industry needs. Experiments show that TraceSIR consistently produces coherent, informative, and actionable reports, significantly outperforming existing approaches across all evaluation dimensions. Our project and video are publicly available at https://github.com/SHU-XUN/TraceSIR.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体系统（Agentic Systems）执行轨迹分析困难的问题。随着大语言模型（LLM）与外部工具及迭代决策相结合，智能体系统在深度研究、函数调用和编码等复杂任务中展现出强大能力。然而，其执行轨迹通常冗长且复杂，单个任务可能涉及数千次工具调用和海量token交互，这使得故障诊断和根因分析变得极其困难。

现有方法存在明显不足。首先，人工检查这些长轨迹无法扩展，效率低下。其次，直接将原始轨迹输入LLM进行自动化分析，会受到模型输入长度限制的制约，并且长上下文会干扰LLM的可靠推理，容易产生无意义或幻觉内容。另一种常见的做法是仅关注最终任务结果，但这会丢弃执行轨迹中蕴含的大量关键行为信息，导致无法准确定位问题，也无法进行依赖行为上下文的根因分析。此外，现有研究缺乏能够生成符合实际工业需求、全面且连贯的分析报告的框架。

因此，本文的核心问题是：如何对智能体执行轨迹进行有效的结构化抽象，以在保留核心行为信息的前提下压缩数据，并在此基础上构建一个自动化框架，生成高质量、可操作的分析报告，以支持故障诊断、根因分析和系统优化。为此，论文提出了TraceSIR多智能体框架，通过协调结构抽象、细粒度诊断和报告生成三个专门化智能体，系统性地解决上述挑战。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：评测类、分析类与报告生成类。

在**评测类**工作中，现有方法大多以任务最终结果为导向，如评估任务完成率或最终输出质量。这类方法虽能衡量整体性能，但无法支持依赖细粒度行为上下文的故障定位与根因分析。部分近期研究尝试引入中间信号（如选择特定状态或总结步骤），但这些抽象处理往往会丢失长执行轨迹中的大量上下文信息，难以进行深入的、基于洞察的根因分析。

在**分析类**工作中，已有技术通常孤立地分析单个任务实例，或仅进行浅层的结果汇总。它们难以捕捉跨多个执行轨迹的重复性故障模式。基于简单摘要或聚类式聚合的方法，往往无法保留轨迹级别的证据，导致生成的报告过于粗略或缺乏扎实依据。

在**报告生成类**方面，针对多任务实例进行综合分析并生成整合报告的研究目前有限。现有方法在此场景下面临挑战，难以生成既全面又可操作的报告。

本文提出的TraceSIR框架与上述工作有显著区别：它专门为执行轨迹的结构化分析与报告而设计。通过引入TraceFormat抽象格式压缩轨迹并保留关键行为信息，并协调三个专用智能体（结构化、诊断洞察、报告生成），TraceSIR实现了跨多个案例的可扩展故障定位、根因分析以及可操作的报告生成，弥补了现有工作在系统性诊断与深度报告方面的不足。

### Q3: 论文如何解决这个问题？

TraceSIR 通过一个多智能体框架，结构化地分析和报告智能体执行轨迹，以解决长而复杂的执行轨迹导致的诊断和根因分析难题。其核心方法围绕三个专门化的智能体进行协同工作，整体框架支持从单案例细粒度分析到多案例规模化报告的全流程。

首先，**StructureAgent** 负责轨迹的结构化与压缩。它引入了创新的 **TraceFormat** 抽象表示法，将原始的执行消息序列 $\mathcal{M}$ 通过解析函数 $\Phi$ 转换为结构化的轨迹 $\mathcal{T} = \{ (t_i, a_i, o_i) \}_{i=1}^{N}$，其中 $t_i$、$a_i$、$o_i$ 分别代表智能体的“思考”、“行动”和“观察”。这种格式严格保持了时序和因果对齐，并可以表格形式呈现。针对长轨迹带来的上下文长度限制，该组件进一步执行**轨迹级抽象**，通过一个基于阈值 $\theta$ 的长度感知抽象算子 $\mathcal{A}_{\theta}$，对冗长的内容（如详细推理、代码片段）进行选择性压缩，生成压缩后的轨迹 $\mathcal{T}'$，在保留关键行为语义的同时大幅减少冗余，为下游可靠分析奠定基础。

其次，**InsightAgent** 在结构化轨迹的基础上进行细粒度的实例级诊断。它不再仅仅依赖最终任务结果，而是对整个执行轨迹进行推理。该组件通过自动调用分析工具，为每个轨迹案例生成一组结构化的诊断输出 $\mathcal{D} = \{ s, E, W, R, O \}$。具体包括：任务完成度总体评分 $s$；检测到的错误 $E$（区分主次错误）；揭示的弱点 $W$（有时也包括优点）；深入的**根因分析 $R$**，解释失败或局限性的原因；以及具体的**优化建议 $O$**（包括文本建议和微调样本）。当存在外部评估提供的 `gold_score` 和 `gold_judge` 时，会将其作为辅助参考信号融入分析。

最后，**ReportAgent** 在更高层面进行跨案例的协调分析与报告生成。它接收来自 InsightAgent 的多个案例的诊断输出集合，并自动决定是否触发报告生成。其核心工作是进行**定向统计分析**，包括：对错误进行规范化标签归纳并估算各类错误频率 $P(\ell)$；对任务完成评分进行分布建模 $P(b)$。随后，ReportAgent 将定量统计与来自各案例的定性洞察（如根因分析）相结合，自动调用报告生成工具，产出结构化的 Markdown 格式综合分析报告。报告生成后，系统还会通过匹配工具自动识别报告中引用的标准化轨迹案例ID，并将对应的结构化轨迹数据附于附录，确保分析的透明度和可追溯性。

该框架的关键创新点在于：1) 提出了专为分析设计的 TraceFormat 结构化抽象，有效平衡了信息保留与压缩；2) 设计了分工明确的三智能体协同架构，实现了从轨迹预处理、实例诊断到聚合报告的全链路自动化分析；3) 强调基于全轨迹行为的根因分析与优化建议生成，而非仅关注最终输出；4) 支持单案例与多案例两种分析模式，并通过统计建模和证据聚合，生成兼具连贯性、信息量和可操作性的报告，满足了实际研发与工程决策的需求。

### Q4: 论文做了哪些实验？

实验设置方面，论文构建了名为TraceBench的统一基准，包含从三个真实世界智能体场景（BrowseComp的深度研究、Tau2Bench的函数调用、SWE-bench的智能体编码）收集的150个GLM-4.6失败任务实例。为评估分析报告质量，论文提出了ReportEval协议，从整体结构(OS)、错误分析(EA)、根因分析(RCA)、优化分析(OA)和整体影响(OI)五个维度（各10分制）进行评分，并计算归一化的总体得分（0-100分）。评估采用混合设置，结合了6位专家的人工评估和基于LLM的自动评判。

对比方法上，将TraceSIR系统与基线模型ClaudeCode进行比较，并分别使用GLM-5和Claude-4.6作为骨干大语言模型进行实例化。

主要结果如下：在人工评估中，TraceSIR在所有场景和骨干模型上均显著优于ClaudeCode。使用较弱的GLM-5骨干时，在深度研究、函数调用和智能体编码场景中，总体得分分别提升10.0%、13.0%和5.0%；使用较强的Claude-4.6骨干时，提升幅度分别为15.0%、3.0%和12.0%。平均而言，TraceSIR实现了9.7%的相对改进。在五个评估维度上，平均得分分别提升0.9、1.3、1.2、0.8和0.9分，在错误分析和根因分析方面提升尤为明显。

基于LLM的自动评估结果趋势高度一致。使用GLM-5骨干时，总体得分分别提升5.3%、8.6%和26.0%；使用Claude-4.6时，提升幅度为1.3%、3.3%和0.7%。平均相对改进为7.5%。关键数据指标显示，在最具挑战性的智能体编码场景中使用较弱骨干模型时，TraceSIR取得了最大幅度的性能提升（26.0%），凸显了其在受限模型能力下生成具有诊断意义报告的鲁棒性。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于对底层大语言模型的依赖、大规模轨迹分析的可扩展性以及系统的效率与稳定性。未来研究可以从以下几个方向深入：首先，可探索更鲁棒的轨迹抽象方法，例如结合程序分析或形式化方法，减少对LLM的依赖，提升在复杂专业领域（如深度代码调试）的诊断准确性。其次，针对海量轨迹分析，需设计分层聚合或增量报告机制，以维持报告的可读性与生成效率。再者，优化系统性能是关键，可通过模型蒸馏、缓存策略或小型专用模型来降低延迟与token消耗，并引入确定性解码或后处理校准来提高报告的可复现性。此外，可将框架扩展到更广泛的智能体类型（如多模态智能体）和故障模式，并探索其在实际运维管道中的自动化集成，实现实时监控与干预。最后，评估体系可进一步细化，加入人工评估或长期效用研究，以更全面衡量分析报告的实际影响。

### Q6: 总结一下论文的主要内容

本文针对智能体系统执行轨迹长且复杂、难以诊断故障和定位根因的问题，提出了TraceSIR多智能体框架，旨在对轨迹进行结构化分析与报告生成。其核心贡献是设计了一种名为TraceFormat的新型抽象格式来压缩轨迹并保留关键行为信息，并协调三个专用智能体：StructureAgent负责将原始轨迹结构化表示为TraceFormat；InsightAgent进行细粒度诊断，包括问题定位、根因分析和优化建议；ReportAgent则聚合多个任务实例的洞察并生成综合分析报告。为评估框架，研究构建了涵盖三个真实场景的TraceBench数据集，并提出了符合工业需求的报告评估协议ReportEval。实验表明，TraceSIR能持续生成连贯、信息丰富且可操作的报告，在所有评估维度上显著优于现有方法，为智能体系统的可观测性和调试提供了有效的规模化解决方案。
