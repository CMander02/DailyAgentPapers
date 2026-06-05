---
title: "Benchmark Everything Everywhere All at Once"
authors:
  - "Shiyun Xiong"
  - "Dongming Wu"
  - "Peiwen Sun"
  - "Yuang Ai"
  - "Bokang Yang"
  - "Wencheng Han"
  - "Xiao-Hui Li"
  - "Xiangyu Yue"
date: "2026-06-04"
arxiv_id: "2606.06462"
arxiv_url: "https://arxiv.org/abs/2606.06462"
pdf_url: "https://arxiv.org/pdf/2606.06462v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Agent for Data Generation"
  - "Benchmark Construction"
  - "Autonomous Agent"
  - "Multi-modality"
  - "Domain-specific Reasoning"
relevance_score: 9.5
---

# Benchmark Everything Everywhere All at Once

## 原始摘要

Benchmarks are fundamental for evaluating and advancing LLMs and MLLMs by providing standardized and explicit measures of performance. However, their construction is labor-intensive and hard to reuse, raising concerns about sustainability and scalability. Moreover, existing benchmarks often quickly reach performance saturation after their release, resulting in insufficient discrimination among state-of-the-art models. To address these challenges, we introduce Benchmark Agent, a fully autonomous agentic system designed for benchmark building. Our framework orchestrates the complete benchmark construction pipeline, from user query analysis and subtask design to data annotation and quality control. To assess Benchmark Agent, we implement it to produce 15 representative benchmarks, spanning diverse evaluation scenarios, including text understanding, multimodal understanding, and domain-specific reasoning. Extensive experiments, including human evaluation, LLM-as-a-judge assessment, and consistency checks, demonstrate Benchmark Agent can generate high-quality benchmark samples with minimal human involvement. More importantly, through continual evaluation, we observe several insightful findings, including that current models struggle with certain domain-specific reasoning tasks. We believe that rapidly evolving benchmarks can contribute significantly to the research community. The preview and code will be publicly available at the demo page and code repository.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）和多模态大语言模型（MLLM）评测中基准构建的可持续性和可扩展性问题。研究背景显示，随着模型能力飞速发展，基准测试在标准化评估中扮演核心角色。然而，现有方法存在两大不足：一是基准构建高度依赖人工，从任务设计、数据收集到人工标注等环节不仅耗时巨大，且每个新基准几乎需要从零开始构建，导致重复劳动和迭代周期缓慢，难以长期持续；二是现有基准发布后很快就会出现性能饱和现象（如论文中Qwen模型系列所示，准确率迅速超过80%），导致对顶尖模型的区分度不足，难以揭示新涌现的瓶颈。为此，本文提出核心问题：如何实现一个全自动化、可定制、具备快速迭代能力的基准构建系统，以替代传统高成本、易饱和的人工构建模式，并让基准能够适应不断变化的用户需求和新兴模型，从而推动持续、动态的模型评估。

### Q2: 有哪些相关研究？

基于论文内容，相关研究可分为三类：

1. **基于Agent的评测方法**：先前工作如MLLM-as-a-Judge利用LLM或MLLM作为裁判评估模型输出，Evaluation Agent实现动态多轮评测。但这些方法均在固定、预定义的基准上操作，依赖动态工具或代理完成评估流程。本文的创新在于让Agent动态构建和适配基准，而非仅在静态基准上执行评估。

2. **基于Agent的数据合成**：近期研究利用Agent通过迭代推理、交互或工具使用生成数据，主要用于大规模训练数据增强或领域特定数据集构建。本文与之区别在于聚焦于基准导向的数据合成，探索如何动态构建评测基准，而非单纯用于训练数据扩充。

3. **Agent系统**：ReAct等范式使Agent能在复杂交互环境（如网页、移动设备）中执行任务。尽管Agent系统在广泛应用中快速发展，但如何构建可靠且可扩展的基准仍是开放问题。本文直接回应这一挑战，提出自主构建基准的Agent框架。

与现有工作的核心区别在于：本文致力于实现基准的全自动、动态构建与适配，以解决传统基准构建成本高、易饱和的问题，而以往的Agent工作或聚焦于评测执行，或关注训练数据生成，或探索交互能力，均未系统性解决基准构建的可持续性挑战。

### Q3: 论文如何解决这个问题？

Benchmark Agent通过一个完全自主的智能体系统将基准构建流程自动化，核心方法包括两大模块。首先是Benchmark Planner，负责高层次决策：它通过多智能体协作，由Design Agent将用户需求分解为可测试的子任务集，并利用Proposer、Revising和Discarding等工具对子任务进行筛选和优化；Grounding Agent为每个子任务搜索候选数据集并验证转换可行性，通过Transformability工具和Score-and-Filter模块从评估意图对齐、转换鲁棒性和信号保留三维度评分，确保每个子任务至少有一个有效的(数据集, 转换方案)对；Allocation Agent则通过闭环分配机制，在全局配额和资源约束下确定可行的样本配额分配，若失败则返回上游修订。其次是Benchmark Executor，负责将规划转化为具体基准：Sample-Level Realization通过编排-执行机制，由LLM自适应生成样本级转换动作，结合非LLM工具（如文本转语音、图像调整、脚本处理等）进行执行；Quality and Quota Control持续验证生成样本的语义有效性和格式合规性，不合格样本触发局部修正或重新生成，并通过补充机制确保达到配额要求。创新点在于实现了全链条自动化，从需求分析到数据标注再到质量控制，无需人工干预即可构建高质量基准，同时通过持续更新避免性能饱和问题。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估，主要围绕Benchmark Agent生成的15个基准测试展开，涵盖文本理解、多模态理解和领域特定推理场景。实验设置采用GPT-5.1作为骨干模型，并基于General-Bench数据集池构建基准。

评估包含三大维度：**人类评价**（报告接受率，Acc.）、**LLM作为裁判评估**（包含用户意图对齐UIA、格式与模式质量FSQ等7个指标）和**一致性检查**（评估模型性能趋势的区分度）。关键结果显示：人类接受率达96-98%（如Multi-Perspective 97.65%，Art-Reasoning 98.65%），LLM裁判总体评分在67.98-78.50之间（如Multilingual最高78.50）。一致性检查中，Qwen3.5系列模型在Multi-Perspective上从2B到27B表现呈71.06-87.23的稳定增长。

对比实验方面：直接使用LLM生成基准的总体评分显著更低（如Multi-Perspective最高59.78 vs Agent 72.55）；不同骨干模型（Qwen3.5、GPT-5.4、Claude-Sonnet、Gemini）均能生成可用基准，且闭源模型表现略优（Gemini达79.88）。消融实验显示，去除Transformability Checking和Plan Scoring导致Omni-Understanding评分骤降至45.69（完整版67.98），验证了各组件的重要性。成本分析表明，Agent的生成速度（0.2-0.3分钟/样本）远快于人工（5-6分钟/样本）。

### Q5: 有什么可以进一步探索的点？

该论文提出的Benchmark Agent框架具有显著创新性，但仍存在几点值得深入探索的方向。首先，当前基准生成依赖预设的评估标准和任务模板，导致对“任务新颖性”的探索不足。未来可引入强化学习中的奖励信号来驱动Agent自主发现评测盲区，例如让Agent通过对抗性测试主动寻找模型弱点。其次，论文仅验证了文本和多模态理解场景，未涉及具身智能、多轮交互等动态环境。建议扩展至机器人任务编制领域，利用动作空间规划来设计物理世界基准。此外，当前质量控制依赖人类判断和LLM裁判，存在评价偏差。可引入多Agent辩论机制或采用博弈论框架进行基准难度的动态校准。最后，可持续性维度值得延伸——考虑设计自进化基准池，当模型在特定子任务上达到饱和度后自动淘汰并生成更具挑战性的变体，形成类似遗传算法的基准迭代生态。

### Q6: 总结一下论文的主要内容

这篇论文提出了Benchmark Agent，一个全自动化的智能体系统，用于解决传统基准测试构建过程中劳动密集、难以复用、易饱和等问题。系统能够从用户查询分析、子任务设计到数据标注和质量控制，自主完成整个基准构建流程。作者通过15个覆盖文本理解、多模态理解和领域特定推理等场景的基准测试验证了其有效性。实验表明，该框架能以极少的人工参与生成高质量、高区分度且成本效益高的基准样本。核心贡献在于解决了基准测试的可扩展性和可持续性瓶颈，支持定制化、细粒度的快速迭代评估。主要结论是，持续评估发现当前模型在特定领域推理任务上仍存在困难，而快速演进的基准测试有望推动社区研究进步。
