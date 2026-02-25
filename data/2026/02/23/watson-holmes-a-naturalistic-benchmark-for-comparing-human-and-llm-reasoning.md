---
title: "Watson & Holmes: A Naturalistic Benchmark for Comparing Human and LLM Reasoning"
authors:
  - "Thatchawin Leelawat"
  - "Lewis D Griffin"
date: "2026-02-23"
arxiv_id: "2602.19914"
arxiv_url: "https://arxiv.org/abs/2602.19914"
pdf_url: "https://arxiv.org/pdf/2602.19914v1"
categories:
  - "cs.AI"
tags:
  - "Agent 评测/基准"
  - "推理评估"
  - "自然主义基准"
  - "人机比较"
  - "开放答案评估"
relevance_score: 8.0
---

# Watson & Holmes: A Naturalistic Benchmark for Comparing Human and LLM Reasoning

## 原始摘要

Existing benchmarks for AI reasoning provide limited insight into how closely these capabilities resemble human reasoning in naturalistic contexts. We present an adaptation of the Watson & Holmes detective tabletop game as a new benchmark designed to evaluate reasoning performance using incrementally presented narrative evidence, open-ended questions and unconstrained language responses. An automated grading system was developed and validated against human assessors to enable scalable and replicable performance evaluation. Results show a clear improvement in AI model performance over time. Over nine months of 2025, model performance rose from the lower quartile of the human comparison group to approximately the top 5%. Around half of this improvement reflects steady advancement across successive model releases, while the remainder corresponds to a marked step change associated with reasoning-oriented model architectures. Systematic differences in the performance of AI models compared to humans, dependent on features of the specific detection puzzle, were mostly absent with the exception of a fall in performance for models when solving longer cases (case lengths being in the range of 1900-4000 words), and an advantage at inductive reasoning for reasoning models at early stages of case solving when evidence was scant.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有AI推理基准的局限性，特别是它们难以衡量AI在自然主义、开放场景下的推理能力与人类推理的相似度。现有基准大多依赖选择题格式，限制了模型展示开放式推理和解释的能力；同时，它们容易受到训练数据泄露的影响，缺乏稳定的人类基线进行对比，并且难以反映真实世界的复杂推理过程。为此，作者提出了一个名为“Watson & Holmes (WnH)”的新基准，它改编自同名桌面侦探游戏，通过逐步呈现叙事性证据、开放式问题和不受限制的语言回答，来评估AI模型在接近真实人类推理任务中的表现。该基准的核心目标是提供一个防数据泄露、能精确测量性能、与人类基线校准、抗快速饱和且能反映自然主义语境推理的评估工具。

### Q2: 有哪些相关研究？

相关研究主要围绕AI推理评估基准和自动评分方法。在推理基准方面，论文综述了多种类型：1) 常识推理（如CommonsenseQA, HellaSwag）；2) 数学推理（如GSM8K, MATH）；3) 逻辑与演绎推理（如LogiQA, ReClor）；4) 算法与符号推理（如HumanEval, APPS）；5) 领域特定推理（如MedQA, LegalBench）；6) 多跳推理（如HotpotQA, StrategyQA）；7) 抽象推理（如ARC-AGI）；8) 基于游戏的基准（如GTBench, GameArena）；9) 侦探游戏基准（如DetectBench, True Detective, WHODUNIT）。这些基准大多采用选择题格式，可能无法充分评估开放式推理，且存在数据泄露风险。在自动评分方面，早期方法依赖文本相似度匹配，而近期工作则利用“AI-as-Judge”框架对开放式答案进行上下文评估。本文的WnH基准与侦探游戏类基准（如DetectBench）最为相关，但通过采用完全开放的回答格式、更长的叙事案例（1900-4000词）、逐步证据揭示以及经过验证的自动评分系统，旨在提供更自然、更稳健的评估。

### Q3: 论文如何解决这个问题？

论文通过系统性地改编“Watson & Holmes”桌面侦探游戏，构建了WnH基准来解决上述问题。核心方法包括：1) **基准设计**：从原版游戏中选取11个案例（排除教学案例），每个案例包含一个介绍性叙事（约600词）、平均15个地点卡片（每个约160词）以及2-5个开放式问题。案例总长约2900词，内容未在线上公开，极大降低了数据泄露风险。2) **评估流程**：为适应LLM评估，移除了游戏中的策略性竞标元素，改为单玩家模式。模型（或人类参与者）在阅读案例介绍和问题后，可以按任意顺序“访问”地点，每次访问后都需要重新回答所有问题，从而追踪推理的渐进过程。3) **提示工程**：为AI模型设计了三个核心提示模板——介绍提示（提供案例和问题）、选择地点提示（总结已访问信息并选择下一个地点）、回答问题提示（基于当前所有信息输出答案）。每次交互都是独立提示，避免模型看到自己先前的答案。4) **评分系统**：采用精细化的4分制（0-3分）对每个答案进行评分，评估其元素的完整性和正确性。并定义了瞬时分数、渐进分数、最终分数和整体分数等多个指标，以全面衡量推理的准确性和效率。5) **自动评分验证**：开发了基于GPT-4.1的自动评分器，并通过与五位独立人类评分者对示例答案的评分进行对比验证，确保了评分的一致性和可扩展性。这种方法共同创造了一个自然主义、防泄露、可精确测量且包含人类基线的推理评估环境。

### Q4: 论文做了哪些实验？

论文进行了两组主要实验：人类参与者实验和AI模型评估实验。**人类实验**：招募了5名动机明确的UCL计算机科学本科生。他们每人依次解决11个案例（首个案例用于练习，不计入分析）。实验通过在线视频会议和共享幻灯片进行，参与者可以自由访问案例介绍、地点文本并记录答案。采用基于时间和案例表现的奖励机制以确保参与质量。**AI实验**：评估了2023年9月至2025年8月期间发布的23个LLM，包括完成模型（cModel，如GPT-4o）和推理模型（rModel，如Claude 4 Opus, GPT-o3）。所有模型使用统一的提示模板和流程（温度默认1.0）在WnH基准上运行。**主要结果**：1) **性能趋势**：在2025年的9个月内，AI模型的整体性能从低于人类参与者下四分位数提升至接近人类前5%。约一半的提升源于连续模型发布的稳步进步，另一半则与专门面向推理的模型架构（如o3, Claude 4）的显著跃升相关。2) **人机差异**：除了在解决较长案例（1900-4000词）时模型性能会下降，以及在证据稀缺的案例早期阶段推理模型表现出归纳推理优势外，AI模型与人类在解决特定侦探谜题特征上的系统性差异基本不存在。3) **自动评分有效性**：基于GPT-4.1的自动评分器与人类评分者达到了高度一致，验证了其作为可扩展、可复现评估工具的可靠性。这些实验系统地追踪和比较了AI与人类在自然主义推理任务上的表现。

### Q5: 有什么可以进一步探索的点？

论文指出了几个未来可以深入探索的方向和当前局限：1) **基准扩展与多样化**：目前仅包含11个文本案例，未来可以纳入更多案例，甚至引入多模态元素（如图像、音频线索），以测试更广泛的感知和推理能力。2) **推理过程的深入分析**：当前评估主要基于最终答案的评分，未来可以更细致地分析模型在逐步推理中产生的思维链或内部状态，以理解其与人类推理过程的异同，例如是否使用了类似的启发式方法或存在系统性偏见。3) **交互性与动态性**：当前的基准虽然允许自由选择访问顺序，但本质上仍是静态的叙事呈现。可以探索更具交互性的版本，例如允许模型主动提问以获取信息，这更贴近真实的侦探调查和人类问题解决过程。4) **计算成本与性能关系**：论文提到了跟踪性能与计算成本的关系，但未深入分析。未来可以系统研究不同模型规模、推理步长（如o3-high与o3的区别）与在WnH上表现的相关性。5) **泛化能力检验**：需要验证在WnH上表现优异的模型，其推理能力是否能泛化到其他非侦探类但同样需要复杂推理的现实任务中。6) **人类基线的深化**：当前人类参与者样本量较小且来自特定背景（计算机科学学生）。扩大和多样化人类参与者群体（包括不同专业、年龄、推理风格）可以建立更稳健的人类性能分布曲线。

### Q6: 总结一下论文的主要内容

本文提出了Watson & Holmes (WnH)基准，这是一个用于自然主义环境下评估和比较AI与人类推理能力的新工具。该基准创新性地改编了一款商业侦探桌面游戏，通过逐步呈现长篇叙事证据、提出开放式问题并要求自由文本回答，模拟了真实的推理场景。论文开发并验证了一个基于LLM的自动评分系统，确保了评估的可扩展性和一致性。通过对23个LLM（包括完成模型和新兴的推理模型）以及5名人类参与者的实验，研究发现：AI推理性能在短时间内快速提升，从低于人类平均水平跃升至接近人类顶尖水平，其中专门优化的推理模型架构贡献了显著的性能跃升。与人类相比，AI在长文本处理上存在劣势，但在证据稀缺时展现出更强的早期归纳推理能力。WnH基准因其防数据泄露、开放答案格式、精细评分和人类基线校准等特性，为未来更准确、更自然主义的AI推理评估提供了重要基础。
