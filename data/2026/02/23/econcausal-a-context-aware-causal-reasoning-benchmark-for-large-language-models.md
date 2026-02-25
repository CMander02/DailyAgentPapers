---
title: "EconCausal: A Context-Aware Causal Reasoning Benchmark for Large Language Models in Social Science"
authors:
  - "Donggyu Lee"
  - "Hyeok Yun"
  - "Meeyoung Cha"
  - "Sungwon Park"
  - "Sangyoon Park"
  - "Jihee Kim"
date: "2025-10-08"
arxiv_id: "2510.07231"
arxiv_url: "https://arxiv.org/abs/2510.07231"
pdf_url: "https://arxiv.org/pdf/2510.07231v3"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent评测/基准"
  - "因果推理"
  - "上下文感知"
  - "社会科学"
  - "LLM评估"
relevance_score: 7.5
---

# EconCausal: A Context-Aware Causal Reasoning Benchmark for Large Language Models in Social Science

## 原始摘要

Socio-economic causal effects depend heavily on their specific institutional and environmental context. A single intervention can produce opposite results depending on regulatory or market factors, contexts that are often complex and only partially observed. This poses a significant challenge for large language models (LLMs) in decision-support roles: can they distinguish structural causal mechanisms from surface-level correlations when the context changes?
  To address this, we introduce EconCausal, a large-scale benchmark comprising 10,490 context-annotated causal triplets extracted from 2,595 high-quality empirical studies published in top-tier economics and finance journals. Through a rigorous four-stage pipeline combining multi-run consensus, context refinement, and multi-critic filtering, we ensure each claim is grounded in peer-reviewed research with explicit identification strategies.
  Our evaluation reveals critical limitations in current LLMs' context-dependent reasoning. While top models achieve approximately 88 percent accuracy in fixed, explicit contexts, performance drops sharply under context shifts, with a 32.6 percentage point decline, and falls to 37 percent when misinformation is introduced. Furthermore, models exhibit severe over-commitment in ambiguous cases and struggle to recognize null effects, achieving only 9.5 percent accuracy, exposing a fundamental gap between pattern matching and genuine causal reasoning. These findings underscore substantial risks for high-stakes economic decision-making, where the cost of misinterpreting causality is high.
  The dataset and benchmark are publicly available at https://github.com/econaikaist/econcausal-benchmark.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在社会科学领域，特别是经济学和金融学中进行因果推理时面临的核心挑战：模型能否在复杂且部分可观测的社会经济环境中，区分结构性的因果机制与表面相关性？具体而言，社会经济因果效应高度依赖于特定的制度与环境背景，同一干预措施在不同背景下可能产生相反的结果。现有因果推理基准大多缺乏对实证研究、具体背景以及背景变化鲁棒性的关注。因此，论文提出了EconCausal基准，用于系统评估LLMs在真实、背景依赖的社会经济因果推理任务上的能力，揭示其在决策支持角色中的潜在风险与局限性。

### Q2: 有哪些相关研究？

相关研究主要分为两类。第一类是面向LLMs的通用因果推理基准，如CLADDER（关注形式化演绎推理）、CausalBench（基于日常常识场景）等。这些基准通常在去语境化或合成环境中评估反事实和干预推理，但缺乏对社会经济领域特有的制度背景和背景依赖性的覆盖。第二类是经济推理与科学因果发现研究。前者包括评估微观经济理性的STEER、评估自然语言推理的EconNLI和EconLogicQA等基准，以及从文献中大规模提取因果主张的工作。后者包括Evidence Triangulator、IdeaBench、ResearchAgent等从科学文献中发现因果关系的系统，但它们通常假设自然科学中相对稳定的因果机制。本文的EconCausal与这些工作的主要区别在于，它专注于社会经济环境中根本上是背景依赖的因果解释，要求模型整合复杂的制度和政策约束来确定因果方向，超越了先前工作中普遍存在的背景无关假设。

### Q3: 论文如何解决这个问题？

论文通过构建一个大规模、高质量的基准数据集EconCausal来解决这个问题。核心方法是一个严谨的四阶段LLM辅助数据构建流程：1. **三元组提取与多轮共识**：使用GPT-5 mini对每篇论文独立运行三次，提取“处理-结果”对，通过多数投票和语义相似度合并（余弦相似度≥0.8）确定最终对及其符号标签（+， -， None， Mixed），并保留支持证据。2. **论文级元数据与全局背景提取**：提取论文类型（实证/理论）、概括核心要素的全局背景段落，以及基于固定本体（如DID， IV）的去重识别方法集。3. **三元组特定背景与方法精炼**：仅保留实证论文的三元组。检查全局背景和方法是否适用于特定主张，必要时进行最小化编辑以生成三元组特定背景，否则保留全局默认值。4. **多评判模型评估与保守过滤**：使用三个独立的LLM评判模型（Gemini， Grok， Qwen）从六个质量维度（0-3分）对每个三元组评分。采用保守阈值（任一维度平均分<2或总分<15）进行过滤，最终得到10，490个高质量、背景注释的因果三元组。基于此数据集，论文设计了三个渐进式评估任务：任务1（因果符号识别）测试在固定背景下预测因果方向；任务2（背景依赖符号预测）测试在背景变化下的适应能力；任务3（抗误导符号预测）在提供错误示例符号的情况下，测试模型在新背景下过滤误导信息并进行稳健推理的能力。

### Q4: 论文做了哪些实验？

论文对一系列开源和闭源LLM（包括Gemini、GPT、Grok、Llama、Qwen家族模型）在EconCausal的三个任务上进行了全面评估。主要实验结果如下：1. **任务表现**：在任务1（固定背景）中，顶级模型（如Gemini 3 Flash）在经济学和金融学子集上准确率分别达到88.4%和86.8%。在任务2（背景变化）中，模型整体表现尚可（闭源模型平均73.9%），但在“符号不匹配”子集（示例符号与目标真实符号不同）上性能急剧下降，闭源模型平均跌幅达32.6个百分点。在任务3（引入误导信息）中，模型表现崩溃，闭源和开源模型平均准确率分别仅为37.0%和38.1%，表明模型容易受错误示例锚定。2. **类别偏差**：模型严重偏向预测正负符号，在识别“无效应”和“混合效应”类别上表现极差，平均准确率分别仅为9.5%和19.2%，Macro F1分数远低于准确率，揭示了系统性分类不平衡。3. **领域与时间分析**：在任务1上，模型在涉及具体历史事件或制度背景的JEL类别（如经济思想史）上表现更好，而在依赖抽象或结构推理的类别（如一般经济学）上表现较差。按发表年份分析，模型性能未显示出随年份系统下降的趋势，表明其表现更多受任务结构而非对旧研究的记忆驱动。4. **校准分析**：实验发现模型存在严重“过度承诺”倾向。即使移除所有背景信息并提供“未知”选项，GPT-4o仍极少选择未知，而是强行预测符号。此外，模型对清晰的正负效应校准相对较好，但对“无效应”和“混合效应”类别严重误校准，置信度很高但预测大多错误，这在高风险决策中尤其危险。

### Q5: 有什么可以进一步探索的点？

论文指出了多个未来研究方向：1. **丰富因果结构表示**：当前仅使用方向符号标签过于粗糙。未来可纳入效应大小、统计显著性、异质性类型（如跨群体差异、非线性效应）、时间动态（短期vs长期）以及因果路径（直接效应vs中介效应）等更细粒度的信息，使基准能评估更贴近经济学家解读方式的复杂推理。2. **提升泛化与机制理解**：当前“背景”与具体研究设定绑定。未来可增加一个抽象层，描述影响效应可移植性的制度、市场结构等可迁移特征，以评估模型在“此处的发现能否推广到彼处”这类决策支持场景下的推理能力。同时，可嵌入结构化机制组件或理论依据层，以评估模型对因果通道（如需求变化、生产率调整）的解释能力，而不仅仅是方向预测。3. **改进可靠性与不确定性感知**：当前LLMs在知识边界识别和不确定性量化方面存在严重缺陷，表现为过度承诺和对模糊类别误校准。未来研究需要开发能更好表征认知不确定性、在信息不足时懂得“存疑”的架构或训练方法，这对于高风险经济决策至关重要。4. **扩展基准范围与任务**：可将基准扩展到更多社会科学领域，并设计更复杂的任务，如基于多篇矛盾研究进行因果证据三角验证，或模拟政策制定中的多步因果推理链条。

### Q6: 总结一下论文的主要内容

本文提出了EconCausal，一个用于评估大型语言模型在社会经济领域进行背景感知因果推理的大规模基准。其核心贡献是：1. 通过一个严谨的四阶段LLM辅助流程，从顶级经济金融期刊的2595篇实证研究中构建了一个包含10，490个高质量、背景注释的因果三元组数据集。2. 设计了三个渐进式评估任务，分别测试模型在固定背景下的因果知识内化、在背景变化下的适应能力以及在误导信息下的稳健推理能力。3. 对多种主流LLM的广泛评估揭示了关键局限：模型在固定背景下表现良好，但在背景变化或存在误导时性能急剧下降；严重偏向预测正负符号，难以识别无效应或混合效应；并且存在“过度承诺”和误校准问题，无法可靠地表征不确定性。这些发现表明，当前LLMs的因果推理可能更多依赖于训练数据中的表面模式匹配，而非真正的结构因果理解，将其部署于高风险经济决策支持系统存在显著风险。EconCausal为诊断和开发具备更可靠背景依赖推理能力的AI系统提供了重要工具。
