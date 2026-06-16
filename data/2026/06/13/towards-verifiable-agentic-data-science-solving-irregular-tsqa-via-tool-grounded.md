---
title: "Towards Verifiable Agentic Data Science: Solving Irregular TSQA Via Tool-Grounded Reasoning"
authors:
  - "Sanhorn Chen"
  - "Xiaoyang Chen"
  - "Boyu Liu"
  - "Roy Zhao"
date: "2026-06-13"
arxiv_id: "2606.15107"
arxiv_url: "https://arxiv.org/abs/2606.15107"
pdf_url: "https://arxiv.org/pdf/2606.15107v1"
github_url: "https://github.com/SanhornC/IRTS-ToolBench"
categories:
  - "cs.AI"
tags:
  - "Time Series Agent"
  - "LLM Agent Benchmark"
  - "Tool-Grounded Reasoning"
  - "LLM for Data Science"
relevance_score: 8.0
---

# Towards Verifiable Agentic Data Science: Solving Irregular TSQA Via Tool-Grounded Reasoning

## 原始摘要

Time series data in real-world deployments is overwhelmingly irregular. Observations are asynchronous, missing values are informative rather than random, and sampling frequencies vary across sensors and operational windows. However, existing Time Series Question Answering (TSQA) benchmarks mostly assume regularly sampled inputs, leaving a fundamental gap in understanding how large language models (LLMs) and AI agents perform under irregular conditions. To bridge this gap, we introduce IRTS-ToolBench, a benchmark of 1,700 questions spanning 10 task types across 13 domains. IRTS-ToolBench is designed to be used independently by any researcher working on LLM-based irregular time series analysis, providing standardized inputs and a reproducible evaluation protocol. Code can be found in https://github.com/SanhornC/IRTS-ToolBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前时序数据分析与问答研究中的一个关键缺口：缺乏针对非规则时间序列的系统性评测基准。现实世界中的时间序列数据（如医疗监护信号、工业传感器读数）普遍具有异步观测、缺失值具有信息性（非随机缺失）、采样频率随窗口变化等不规则特征。然而，现有的时间序列问答基准几乎都假设输入是均匀采样的规则序列，这导致对大型语言模型和AI智能体在真实不规则场景下的推理能力缺乏评估。现有方法虽采用MCAR随机丢弃或稀疏掩码等方式人工制造不规则性，但忽略了缺失的领域语义（如由事件触发、硬件约束或人为记录差异导致），生成的序列统计上不规则但语义上不可信。因此，本文的核心目标是构建一个能真实反映不规则时序特征的可验证评测平台。为此，他们提出了IRTS-ToolBench，包含1700个覆盖10种任务类型、13个领域的问题，并设计了一套基于领域语义的规则到不规则序列转换管线，同时提供了30个工具的库（含7种不规则算子与23种分析工具），以支持对LLM和AI智能体进行基于工具推理的可复现评估。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及三类工作。**评测类**：TSQA、Time-MQA和ITFormer等基准假设规则采样，而本文针对不规则时间序列提出IRTS-ToolBench，填补了LLM在不规则数据上的评测空白。**方法类**：TIME-IMM提供了九种不规则性分类法，本文将其作为转换管道的决策空间；Physiome-ODE提出不规则多元预测基准，但未利用LLM指导不规则化过程，本文则通过工具链实现LLM驱动的推理。**应用类**：TimeART和TS-Agent等工具增强型智能体框架为时序推理提供模板，但局限于规则数据；本文将这些框架扩展到不规则领域，并引入可验证的评估协议。相比现有工作，本文的独特贡献在于：1) 系统化生成不规则时间序列的标准化流程；2) 建立1700个跨领域问题的验证基准；3) 实现可复现的对比评估。主要区别在于本文首次将LLM智能体与不规则数据特性相结合，并通过工具基础推理保证结果的可验证性。

### Q3: 论文如何解决这个问题？

该论文通过设计一个系统化的工具驱动推理框架来解决不规则时间序列问答的验证问题，核心方法包含以下三个互补组件：

**基准构建**：构建了包含1700个问题、跨13个域、覆盖10种任务类型的IRTS-ToolBench基准。任务被设计为三层次推理层级：标准推理（异常检测/分类等基础操作）、不规则性特定推理（时序特征识别/观测关系推断）、规律与不规则接口推理（缺失机制理解/严重性评估）。每个样本都经过三层转换流水线生成：首先通过LLM生成领域上下文描述进行语义增强，然后选择最优不规则类型（缺失、抖动、混合等），最后将转换计划转化为具体的数值参数。

**金标工具集**：为每个评测样本预先定义了最小工具调用序列。通过多LLM共识机制（GPT-5.1、Claude Sonnet 4.5、Gemini 2.5 Flash独立提议后采用投票+并集回退策略）确保工具集的完备性和可验证性。工具库包含30个原子操作，分为两层：不规则操作层（处理异步采样、缺失值等）和高级分析层（23个时间序列原语，如统计量计算、趋势检测）。

**验证机制**：采用三阶段验证管道确保数据质量。问题生成由GPT-5.1驱动，但需经过三模型共识验证（清晰度、可答性检查）。金标工具集本身就是一种验证手段，因为要正确回答问题必须按序调用特定工具组合。基准还提供标准化输入和可复现的评估协议，使不同研究者能够对比LLM的推理能力与AI智能体的工具调用能力。这种设计使得模型行为能被分解为可追踪的工具调用序列，从而实现对复杂时序推理过程的事后验证。

### Q4: 论文做了哪些实验？

论文构建了IRTS-ToolBench基准测试，包含1700个问题，涵盖10种任务类型（如异常检测、缺失值推理、不规则严重性估计等）和13个领域。实验设置采用标准化评估协议，使用二进制评分，主要比较模型输出与标准答案的精确匹配准确率，并报告总体准确率和任务级准确率；启用工具调用时，还计算工具集调用的完全匹配、部分匹配和完全不匹配率。

对比方法包括商业模型Claude-Opus-4.7（分无思考、有思考、有工具调用三种模式）和开源模型Qwen3.5-4B、Qwen3.6-27B、DeepSeek-V4-Flash（分有/无工具调用）。主要结果：Qwen3.6-27B在无工具模式下总体准确率达78.59%，优于其他模型；商业模型Claude-Opus-4.7准确率在74%-77%之间。工具调用带来显著提升：Qwen3.6-27B的异常检测从96.80%提升至99.60%，分类任务达100%；DeepSeek-V4-Flash在不规则严重性估计任务中从31.33%大幅提升至98.67%，规律恢复任务从64.67%提升至89.33%。人类基线准确率分别为80%和78%。然而，时间关系推理和规则vs不规则判别等高级推理任务仍具挑战。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于其三层LLM生成流水线对提示工程、共识质量和变换选择的敏感性，这可能导致基准数据本身存在系统性偏差。未来可通过引入更天然的不规则源数据（如工业传感器流）来增强鲁棒性，避免人工合成序列的伪影。另一个关键方向是向多跳时序问答扩展：当前任务多依赖单步工具调用，而真实场景需链式推理（如先插值缺失值、再计算滑动统计、最后对比趋势），这需要Agent具备动态规划能力并管理中间结果的可信度。此外，作者计划融入可视化模态，但更值得探索的是如何让LLM自主选择多模态表征——例如对高噪声时段调用频谱图而非原始波形。从工具层面看，当前黄金工具集假设固定操作顺序，可改进为让Agent在运行时通过元推理决定是否优先重采样或离群值检测，这能暴露模型在不确定条件下的自适应策略。最后，将评估从单变量转向多变量不规则序列将更具挑战性，因为变量间时域对齐、因果关系推断等问题会指数级增加复杂度。

### Q6: 总结一下论文的主要内容

本文提出了IRTS-ToolBench基准，用于评估大语言模型和AI代理在不规则时间序列问答中的表现。针对现有基准仅处理规则采样数据的局限，该工作定义不规则时间序列问答问题，即输入数据存在异步观测、非随机缺失和可变采样频率等特征。方法上提出基于大语言模型引导的语义化不规则转换流水线，将规则序列转化为符合领域语义的不规则数据，并构建包含7个不规则操作符和23个分析工具的30个工具库。基准涵盖1700个问题、10种任务类型和13个领域。主要结论表明，现有方法在不规则数据上性能显著下降，而工具增强的推理框架能有效提升表现。该工作填补了不规则时间序列评估的关键空白，为开发可验证的代理数据科学系统提供了标准化测试平台。
