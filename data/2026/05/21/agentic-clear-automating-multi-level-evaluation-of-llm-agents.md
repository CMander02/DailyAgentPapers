---
title: "Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents"
authors:
  - "Asaf Yehudai"
  - "Lilach Eden"
  - "Michal Shmueli-Scheuer"
date: "2026-05-21"
arxiv_id: "2605.22608"
arxiv_url: "https://arxiv.org/abs/2605.22608"
pdf_url: "https://arxiv.org/pdf/2605.22608v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent评估"
  - "多层级评估"
  - "自动化评估框架"
  - "智能体行为分析"
  - "评估基准"
  - "反馈生成"
relevance_score: 9.0
---

# Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents

## 原始摘要

Agentic systems are becoming more capable: agents define strategies, take actions, and interact with different environments. This autonomy poses serious challenges for overseeing and assessing agent behavior. Most current tools are limited, focusing on observability with basic evaluation capabilities or imposing static, hand-crafted error taxonomies that cannot adapt to new domains. To address this gap, we present Agentic CLEAR, an automatic, dynamic, and easy-to-use evaluation framework. It produces textual insights into the agent behavior on three levels of granularity: system, trace, and node. Agentic CLEAR operates above the observability layer, enabling seamless integration and featuring an intuitive UI that makes agent evaluation highly accessible. In our experiments on four benchmarks, seven agentic settings, and tens of thousands of LLM calls, we show that Agentic CLEAR produces high-quality, data-driven, insightful feedback. Our analysis shows strong alignment with human-annotated errors and the ability to predict task success rate.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前LLM智能体评估中存在的关键瓶颈：随着智能体系统在策略制定、环境交互和多步任务求解方面能力的显著提升，其自主行为带来了严重的监控与评估难题。现有方法存在明显不足：一方面，主流工具局限于“可观测性”层面，仅提供基础的日志记录和简单的指标聚合，缺乏深入的诊断能力；另一方面，研究社区构建的静态错误分类体系或高保真基准测试，由于依赖人工精心设计，无法动态适应智能体开发者面临的多样化、定制化任务。因此，本文的核心问题是填补这一评估鸿沟，即**如何为LLM智能体开发一个自动、动态且易于使用的多层次评估框架**，使其不仅能识别失败（what），还能揭示失败原因（why），从而替代依赖于大量人工检查的低效模式，为开发者提供系统级、轨迹级和节点级的结构化文本洞察，以加速迭代并提升智能体可靠性。

### Q2: 有哪些相关研究？

相关研究可分为两类：

**通用Agent评估框架类**：近期工作致力于标准化Agent评估协议，构建跨环境类型的运行时与执行层基础设施，实现便捷的Agent与基准测试集成。本文与这些工作的区别在于，AgentCLEAR运行在执行层之上，专注于如何解释轨迹，提供开箱即用的多层次Agent评估，而非仅关注基准测试基础设施的标准化。

**Agent元评估类**：多项近期工作创建了评估"评判者"能否检测Agent错误步骤并正确分类的基准测试，这些研究源自LLM元评估体系。与这些方法不同——它们依赖预定义的静态错误分类法并衡量评判者的恢复能力——AgentCLEAR无需预设类别，能动态揭示适应目标系统与领域的失败模式，实现数据驱动的自适应评估。

此外，本文在四个基准、七种Agent设置及数万次LLM调用上的实验表明，其产生的反馈与人工标注错误高度一致，并能有效预测任务成功率，展现了相较于现有可观测性工具和静态分类法的优势。

### Q3: 论文如何解决这个问题？

Agentic CLEAR通过一个两阶段的自动化管道解决多层级评估问题。首先，在**追踪级评估阶段**，对每个任务执行跟踪进行三层分析：1) **步骤级评估**：LLM法官对每一步的输入输出对生成质量分数和自然语言批评，涵盖正确性、完整性和清晰度；2) **追踪级评估**：法官评估整体追踪的完成质量；3) **标准评估**：先由法官自动生成任务特定评价标准，再检查追踪是否满足这些标准。第二阶段是**系统级聚合**：利用CLEAR聚类算法，将每步评估按所属节点(子智能体)分组，识别各节点反复出现的失败模式(节点级洞察)；汇集所有追踪级判断和标准评估结果，发现全局系统行为模式(系统级洞察)。每个洞察都关联到触发它的具体执行步骤或追踪。

关键技术包括：基于OpenTelemetry格式的中间表示转换，支持多种追踪框架；专门设计的不同评估模式提示词，要求法官先给出链式思维文本理由再打分；以及可自定义的评估维度、提示词和法官实现。创新点在于实现了**自动化、动态、多粒度**的评估框架，能生成从细粒度节点到全局系统的可解释文本洞察，并通过实验证明与人工标注错误高度一致，能有效预测任务成功率。

### Q4: 论文做了哪些实验？

该论文在四个基准测试（SWE-bench、GAIA、AppWorld、Tbench）上进行了实验，涵盖了七种代理设置，包括CUGA（AppWorld SOTA）、HAL通用代理和Hugging Face Open Deep Research代理，使用GPT-4o、Claude 4.5 Sonnet、GPT-4.1、OpenAI o3和Claude 3.7 Sonnet等顶级模型。共收集了约939条执行轨迹（AppWorld 417条、GAIA 612条、SWE-bench 50条、TAU-bench 50条），并转换为统一中间表示。评判模型采用开源OSS-120B（高思维模式）和闭源GPT-5，对所有轨迹进行逐迹评估。主要结果包括：Agentic CLEAR生成的评估与人工标注错误高度一致（具体一致性指标未提供，但报告中指出“strong alignment”），并能有效预测任务成功率。该方法在多个代理系统和模型间展示了高质量、数据驱动的洞察能力，支持系统级、轨迹级和节点级三个粒度的行为分析。实验验证了框架的自动化和动态评估能力，无需静态错误分类即可适应不同领域。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向包括：首先，Agentic CLEAR目前主要分析执行过程，未充分结合推理与规划（如Chain-of-Thought）的中间状态，未来可整合这些信息以提供更深入的因果洞察。其次，作为评估基础的LLM裁判在不同任务和领域中的可靠性和偏见问题尚未充分解决，需要探索更鲁棒的验证策略或引入多模型共识机制。此外，当前框架虽支持多粒度分析，但跨配置的系统性对比（如不同Agent架构或提示策略）能力有限，可通过标准化比较模板和自动生成差异报告来增强。最后，可以扩展至多模态或交互式场景（如工具调用、环境反馈），并研究如何将评估结果闭环反馈给Agent以进行在线优化，从而提升框架的实用性和自适应性。

### Q6: 总结一下论文的主要内容

这篇论文提出了Agentic CLEAR框架，旨在解决当前智能体系统评估中静态手工错误分类法无法适应新领域以及现有工具仅提供基础监控能力的问题。核心贡献是一个自动、动态、易用的多层级评估方法，它能从系统、轨迹和节点三个粒度生成关于智能体行为的文本洞察。该框架运行在可观测性层之上，可无缝集成，并配有直观的用户界面。实验在四个基准、七种智能体设置及数万次大语言模型调用上进行，结果表明Agentic CLEAR能生成高质量、数据驱动的反馈，与人工标注的错误高度一致，并能有效预测任务成功率。该方法通过自动化细粒度诊断，大大降低了智能体评估门槛，有助于加速迭代、提升系统可靠性。
