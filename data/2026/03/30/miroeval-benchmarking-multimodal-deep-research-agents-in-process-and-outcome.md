---
title: "MiroEval: Benchmarking Multimodal Deep Research Agents in Process and Outcome"
authors:
  - "Fangda Ye"
  - "Yuxin Hu"
  - "Pengxiang Zhu"
  - "Yibo Li"
  - "Ziqi Jin"
  - "Yao Xiao"
  - "Yibo Wang"
  - "Lei Wang"
  - "Zhen Zhang"
  - "Lu Wang"
  - "Yue Deng"
  - "Bin Wang"
  - "Yifan Zhang"
  - "Liangcai Su"
  - "Xinyu Wang"
  - "He Zhao"
  - "Chen Wei"
  - "Qiang Ren"
  - "Bryan Hooi"
  - "An Bo"
date: "2026-03-30"
arxiv_id: "2603.28407"
arxiv_url: "https://arxiv.org/abs/2603.28407"
pdf_url: "https://arxiv.org/pdf/2603.28407v1"
github_url: "https://github.com/MiroMindAI/MiroEval"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Benchmark"
  - "Multimodal"
  - "Research Agent"
  - "Evaluation Framework"
  - "Process Evaluation"
  - "Factuality Verification"
  - "Adaptive Synthesis"
relevance_score: 9.0
---

# MiroEval: Benchmarking Multimodal Deep Research Agents in Process and Outcome

## 原始摘要

Recent progress in deep research systems has been impressive, but evaluation still lags behind real user needs. Existing benchmarks predominantly assess final reports using fixed rubrics, failing to evaluate the underlying research process. Most also offer limited multimodal coverage, rely on synthetic tasks that do not reflect real-world query complexity, and cannot be refreshed as knowledge evolves. To address these gaps, we introduce MiroEval, a benchmark and evaluation framework for deep research systems. The benchmark comprises 100 tasks (70 text-only, 30 multimodal), all grounded in real user needs and constructed via a dual-path pipeline that supports periodic updates, enabling a live and evolving setting. The proposed evaluation suite assesses deep research systems along three complementary dimensions: adaptive synthesis quality evaluation with task-specific rubrics, agentic factuality verification via active retrieval and reasoning over both web sources and multimodal attachments, and process-centric evaluation audits how the system searches, reasons, and refines throughout its investigation. Evaluation across 13 systems yields three principal findings: the three evaluation dimensions capture complementary aspects of system capability, with each revealing distinct strengths and weaknesses across systems; process quality serves as a reliable predictor of overall outcome while revealing weaknesses invisible to output-level metrics; and multimodal tasks pose substantially greater challenges, with most systems declining by 3 to 10 points. The MiroThinker series achieves the most balanced performance, with MiroThinker-H1 ranking the highest overall in both settings. Human verification and robustness results confirm the reliability of the benchmark and evaluation framework. MiroEval provides a holistic diagnostic tool for the next generation of deep research agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前深度研究智能体评估体系存在的系统性不足。随着大语言模型推动智能体系统从被动文本生成转向自主规划执行，深度研究智能体在金融、医疗等高风险领域应用日益广泛，用户不仅需要流畅的最终报告，更要求答案具备事实可靠性、可追溯的深入调查过程以及处理多模态材料的能力。然而，现有评估方法存在明显局限：多数基准测试仅通过固定标准评估最终报告，完全忽视了对产生报告的研究过程本身的评价；评估任务大多仅支持文本模态，难以反映现实查询中常见的多模态需求；任务构建常依赖合成或学术性查询，未能捕捉真实用户需求的复杂性；且静态基准无法随知识演进更新，容易过时。

针对这些不足，本文的核心问题是构建一个全面、动态且贴近真实需求的深度研究系统评估框架。具体而言，研究试图解决如何系统性地评估智能体的整个研究过程（包括搜索、推理、迭代优化）、如何有效纳入并评估多模态任务、如何基于真实用户需求构建可持续更新的任务库，以及如何设计互补的评估维度来更可靠地诊断系统的综合能力与潜在缺陷。为此，论文提出了MiroEval基准测试与评估框架，通过包含100个任务（70个纯文本、30个多模态）的动态基准，以及从自适应合成质量、智能体事实核查、研究过程审计三个互补维度进行评估的完整方案，旨在为下一代深度研究智能体提供一个全面的诊断工具。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测基准类、评估方法类以及研究代理系统类。

在**评测基准类**工作中，现有研究如WebArena、BIRD等主要评估代理在特定环境（如网站、数据库）中的任务完成能力，但通常聚焦于最终输出，且任务多为合成或学术性质，缺乏对真实用户复杂需求和多模态内容的覆盖。MiroEval则直接针对这些局限，构建了基于真实用户需求、包含多模态任务且可定期更新的动态基准。

在**评估方法类**方面，相关工作多采用静态、固定的评估准则（如RAGAS、ARES）来评判报告质量，或仅进行基于检索的简单事实核查。本文提出的评估框架进行了显著扩展：它引入了自适应、任务特定的合成质量评估；设计了能主动检索并基于网络源和多模态附件进行推理的智能事实性验证；并首创了以过程为中心的评估，从多个维度审计研究轨迹及其与报告的追溯一致性。

在**研究代理系统类**中，已有系统如ChatGPT、Claude以及专门的科研代理（如MiroThinker系列）在能力上不断进步。本文的工作并非提出新系统，而是为这类系统提供了一个全面的诊断工具。其评估揭示了不同系统在各维度（合成质量、事实性、过程严谨性）上的互补性强弱，并首次通过实证表明过程质量能可靠预测总体结果，且多模态任务对现有系统构成显著更大挑战。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为MiroEval的多层次、动态评估框架来解决现有基准在评估深度研究系统时的不足。该框架的核心在于摒弃了传统静态、单一维度的评估方式，转而采用一个互补的三维评估体系，分别针对最终报告的合成质量、事实依据以及研究过程本身进行系统性诊断。

整体框架由三个主要模块组成：自适应合成质量评估、代理式事实性验证和以过程为中心的评估。每个模块都针对现有评估的短板进行了创新设计。

在自适应合成质量评估模块中，框架会根据每个任务的具体指令和可能的多模态附件，动态构建评估维度空间和具体标准。对于纯文本查询，大型语言模型会生成1-3个与任务专业领域相关的动态维度；对于包含附件的多模态查询，则会额外引入“基础依据”维度，要求报告必须正确解读附件内容并进行有意义的分析延伸，而非简单引用。该模块还通过上游提取附件中的关键事实，将抽象的评估要求转化为具体、可验证的检查点，并采用动态权重分配进行最终评分。

在代理式事实性验证模块中，框架设计了一个基于MiroFlow的评估代理。该代理会主动从外部网络搜索和任务提供的多模态附件中检索证据，以验证报告中的每个可验证陈述。其关键技术在于采用了混合处理策略来应对异构附件：对于图像、PDF等格式，使用原生多模态模型直接推理；对于电子表格、幻灯片等格式，则先转换为文本并进行分块检索。此外，该模块创新性地引入了“冲突”标签，以明确表征不同来源证据间的结论不一致，而非强行进行二元判断。

在以过程为中心的评估模块中，框架首次系统性地评估研究过程本身的质量。首先将原始过程日志转化为结构化的过程表示，提取原子步骤和关键发现。然后，从搜索广度、分析深度、渐进式精炼、批判性思维和效率五个维度评估过程的内在质量。最后，通过检查过程关键发现与报告关键发现之间的双向对齐（过程到报告、报告到过程）以及矛盾检测，评估最终报告是否忠实于产生它的研究过程，以及过程本身是否负责任地处理了证据冲突。

这些模块共同构成了一个全面的诊断工具，其核心创新点在于：1) 动态、任务自适应的评估标准生成；2) 支持对多模态附件进行证据检索和事实核查的混合处理机制；3) 首次系统性地将研究过程质量及其与最终报告的 alignment 纳入量化评估，揭示了仅靠输出级指标无法发现的系统弱点。

### Q4: 论文做了哪些实验？

论文在MiroEval基准上对13个深度研究系统进行了全面评估。实验设置方面，评估了包括OpenAI Deep Research、Gemini-3.1-Pro Deep Research、Claude-Opus-4.6 Research等10个主流商业系统，以及三个自研的MiroThinker变体（MiroThinker-1.7-mini, MiroThinker-1.7, MiroThinker H1）。自动评估使用GPT-5系列模型作为评判员：GPT-5.1用于合成质量评估，GPT-5.2用于过程评估，GPT-5-mini用于事实性评估。

数据集为MiroEval基准，包含100个任务（70个纯文本任务，30个多模态任务），均基于真实用户需求构建，并支持定期更新。评估从三个互补维度进行：1）使用任务特定量规的自适应合成质量评估；2）通过主动检索和对网络来源及多模态附件的推理进行智能体事实性验证；3）过程中心化评估，审计系统在整个研究过程中的搜索、推理和优化行为。

主要结果如下：在纯文本任务总体得分上，OpenAI Deep Research以76.7分最高，MiroThinker-1.7-mini为72.9分，Kimi-K2.5 Deep Research为68.4分。在多模态任务总体得分上，OpenAI Deep Research（70.2分）和Gemini-3.1-Pro Deep Research（68.1分）表现较好，但相比其纯文本成绩均出现下降。关键发现包括：三个评估维度捕获了系统能力的互补方面；过程质量是整体结果的可信预测指标，并能揭示输出级指标无法发现的弱点；多模态任务带来显著更大挑战，大多数系统得分下降3至10点。MiroThinker系列实现了最平衡的性能，其中MiroThinker-H1在两种设置中均排名最高。人类验证和鲁棒性结果证实了基准和评估框架的可靠性。

### Q5: 有什么可以进一步探索的点？

该论文提出的MiroEval基准在评估深度研究智能体方面迈出了重要一步，但仍存在一些局限性和值得探索的方向。首先，基准任务规模有限（仅100个任务），未来可扩展至更广泛的领域和更复杂的任务类型，如跨语言研究或高度专业化的科学探究。其次，评估框架虽然涵盖了过程、事实性和合成质量三个维度，但对多模态能力的评估仍侧重于静态图像和文档，未来可纳入视频、音频及交互式内容，并研究智能体在动态多模态信息流中的实时推理能力。此外，过程评估主要依赖日志分析，未能深入捕捉智能体的内部认知机制（如假设生成、不确定性管理），未来可结合可解释性技术进行更细粒度的分析。从改进思路看，可引入对抗性评估，例如在任务中嵌入矛盾信息或隐蔽的虚假来源，以测试智能体的批判性验证能力；同时，基准的更新机制虽支持定期刷新，但尚未实现完全自动化的动态难度调整，未来可设计自适应任务生成系统，根据智能体表现实时调整复杂度，形成持续进化的评估环境。最后，该研究未涉及智能体在长期、协作研究场景中的表现，探索多智能体分工与知识整合的评估框架将是另一个有前景的方向。

### Q6: 总结一下论文的主要内容

该论文针对当前深度研究系统评估的不足，提出了一个名为MiroEval的综合基准测试与评估框架。核心问题是现有基准大多仅评估最终报告，忽略了研究过程，且缺乏多模态覆盖、依赖合成任务、难以随知识更新而刷新。

论文的主要贡献是构建了包含100个任务（70个纯文本、30个多模态）的基准，所有任务均基于真实用户需求，并通过双路径管道构建以支持定期更新。方法上，提出了一个三层互补的评估套件：1）使用任务特定量规的自适应综合质量评估；2）通过主动检索和对网络来源及多模态附件进行推理的智能事实性验证；3）审计系统在整个研究过程中如何搜索、推理和优化的过程中心化评估。

主要结论包括：三个评估维度捕捉了系统能力的互补方面，揭示了不同系统的独特优缺点；过程质量是整体结果的可靠预测指标，并能揭示输出级指标无法发现的弱点；多模态任务带来了显著更大的挑战，导致大多数系统得分下降3-10分。其中，MiroThinker系列表现最为均衡，MiroThinker-H1在两种设置下均获得最高总分。该研究为下一代深度研究智能体提供了一个全面的诊断工具。
