---
title: "Willful Disobedience: Automatically Detecting Failures in Agentic Traces"
authors:
  - "Reshabh K Sharma"
  - "Shraddha Barke"
  - "Benjamin Zorn"
date: "2026-03-25"
arxiv_id: "2603.23806"
arxiv_url: "https://arxiv.org/abs/2603.23806"
pdf_url: "https://arxiv.org/pdf/2603.23806v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent Evaluation"
  - "Agentic Traces"
  - "Specification Compliance"
  - "Failure Detection"
  - "Tool Usage"
  - "Multi-step Workflow"
  - "Benchmarking"
relevance_score: 7.5
---

# Willful Disobedience: Automatically Detecting Failures in Agentic Traces

## 原始摘要

AI agents are increasingly embedded in real software systems, where they execute multi-step workflows through multi-turn dialogue, tool invocations, and intermediate decisions. These long execution histories, called agentic traces, make validation difficult. Outcome-only benchmarks can miss critical procedural failures, such as incorrect workflow routing, unsafe tool usage, or violations of prompt-specified rules. This paper presents AgentPex, an AI-powered tool designed to systematically evaluate agentic traces. AgentPex extracts behavioral rules from agent prompts and system instructions, then uses these specifications to automatically evaluate traces for compliance. We evaluate AgentPex on 424 traces from τ2-bench across models in telecom, retail, and airline customer service. Our results show that AgentPex distinguishes agent behavior across models and surfaces specification violations that are not captured by outcome-only scoring. It also provides fine-grained analysis by domain and metric, enabling developers to understand agent strengths and weaknesses at scale.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI智能体在复杂多步工作流执行中行为评估的难题。随着AI智能体日益嵌入实际软件系统（如GitHub Copilot），它们通过多轮对话、工具调用和中间决策执行长序列任务，产生称为“智能体轨迹”的执行历史。现有评估方法主要依赖结果导向的基准测试，仅关注最终输出是否正确，但无法捕捉轨迹过程中的关键程序性失败，例如错误的工作流路由、不安全工具使用或违反提示中指定的规则（即“故意不服从”行为）。这些不足使得开发者难以在部署规模下有效监控智能体行为，因为手动检查海量轨迹不可行。

因此，本文的核心问题是：如何自动化、系统化地评估智能体轨迹的合规性，以检测多步执行中的过程性错误，并解决结果评估的盲点。为此，论文提出了AgentPex工具，通过从智能体提示和系统指令中提取行为规则作为可检查的规范，并基于这些规范自动评估轨迹合规性，从而实现对智能体行为的细粒度、大规模分析。

### Q2: 有哪些相关研究？

本文（AgentPex）的相关研究主要可分为三类：基于规范的评估、智能体轨迹分析以及传统软件验证方法。

在**基于规范的评估**方面，已有研究致力于从提示中提取可检查的规范。例如，Stoica等人强调了规范对于使提示工程像传统软件工程一样可靠的重要性；Sharma等人使用声明式元语言为视觉语言模型提示定义输入规范；而PromptPex则将提示视为程序，利用LLM从指令中提取结构化的输入/输出规范，并用于生成测试用例和评估提示合规性。**本文的AgentPex与这些工作密切相关，但进行了关键扩展**：它不局限于为单个提示生成测试输入，而是专注于评估包含多轮对话、工具调用和中间决策的**完整智能体执行轨迹**，检查其是否符合从系统指令和提示中提取出的行为规则。

在**智能体轨迹分析与调试**领域，现有工作多关注于事后分析和性能评估。本文则通过自动化的规范检查，为智能体开发提供了**实时的、过程性的**故障检测能力，能够发现仅靠最终结果评分所遗漏的工作流路由错误、不安全工具使用等问题。

最后，**传统软件验证方法**（如形式化规范、模型检查）为基于规范的验证提供了理论基础。AgentPex将这一思想应用于由自然语言指令驱动、行为不确定的AI智能体系统，是对传统方法在新领域的适应和创新。

总之，AgentPex的核心贡献在于，它将从提示提取规范的思想，系统地应用于**长序列、多步骤的智能体轨迹验证**，实现了对过程性故障的自动化、细粒度检测，弥补了现有结果导向型评测的不足。

### Q3: 论文如何解决这个问题？

论文通过设计并实现一个名为AgentPex的系统化评估工具来解决智能体执行轨迹验证困难的问题。其核心方法是一个三阶段的自动化评估流水线，整体框架包括：**1）轨迹导入与标准化**：通过模块化、可扩展的导入器，将多种格式的原始对话轨迹（如τ²-bench格式、OpenAI消息格式）统一转换为包含系统提示、工具模式定义和完整消息历史的自包含标准化工件。**2）规范提取**：利用大语言模型从系统提示和用户任务描述中，严格遵循“仅显式提取”原则，抽取出可检查的行为约束。提取的规范分为两类：一是与具体任务无关的**策略规范**，包括约束响应格式与内容的输出规范、捕获动作间时序与顺序关系的转移规范、明确禁止的工具调用序列（以{from, to, reason}元组形式表示）以及基于工具模式定义的参数规范；二是与具体请求相关的**任务特定规范**，包括预测完成任务所需的工具调用序列（预测计划）以及基于初始状态和用户输入预测的任务成功后的最终状态。**3）基于规范的评估与聚合**：设计了一套基于LLM的评估器，每个评估器使用标准化的提示模板，依据提取的相应规范对轨迹进行合规性检查。评估器涵盖输出规范、转移规范、禁止边、参数真实性、参数规范、预测计划和预测最终状态。关键创新点在于其**门控最小聚合策略**：根据重要性将评估器分为关键级（如预测计划、输出规范）、重要级和低优先级，最终聚合分数是所有评估器的加权平均值，但上限被关键级评估器中的最低分所限制。这确保了任何关键性的功能失败（如完成了本应拒绝的预订）都会直接导致整体评分不及格，从而避免了其他指标的高分掩盖根本性错误。整个流程无需额外的人工标注，完全基于轨迹和任务描述中已有的信息进行自动化、细粒度的合规性评估。

### Q4: 论文做了哪些实验？

论文在τ²-bench数据集上对AgentPex工具进行了系统性实验评估。实验使用了来自航空（航班预订、修改、取消）、零售（订单管理、退货）和电信（套餐变更、账单争议）三个客户服务领域的424条经过筛选的智能体执行轨迹（trace）。评估模型包括Claude 3.5 Sonnet、GPT-4.1和o4-mini，温度设置为0，并使用GPT-4.1作为一致的用户模拟器。

实验设置上，AgentPex无需人工标注，仅基于任务描述、工具模式和执行轨迹，通过LLM（使用gpt-5-mini-2025-08-07）提取行为规则，并运行七项评估器对合规性进行0-100分的打分，最终通过加权平均（受关键最低分限制）计算聚合分数。对比方法为τ²-bench的基于结果的评估，它依赖人工标注的1,145条标准，通过比较最终数据库状态和通信给出二元奖励（0/1）和0-100的复合分数。

主要结果包括：1）AgentPex聚合分数与τ²复合分数趋势一致，低τ²分数的轨迹集中在AgentPex低分段。具体地，代表性评估器output_spec在预测τ²失败任务时ROC-AUC达到0.680，在阈值<65时能标记48%的失败轨迹。2）AgentPex能检测结果评估遗漏的程序违规：在58条τ²奖励为1.0的Claude轨迹中，83%存在至少一项程序违规，例如同一消息中同时生成文本和调用工具（449例），或绕过计算工具进行心算（11例）。3）评估发现对不同模型具有普遍性：三个模型在指标层次上相似，输出规范（Output Spec）和转移规范（Transition Spec）是共同瓶颈（分数分别在63.6-66.9和59.2-80.6之间），而论证基础性（Argument Groundedness）接近满分（98.1-99.1）。电信领域在预测规划上普遍更具挑战性。4）AgentPex揭示了模型特异性行为：Claude更频繁地违反协议（如449次同时调用文本），GPT-4.1出现语义幻觉和批量工具调用，o4-mini则在身份验证步骤上有独特缺失（7例），尽管其转移规范分数最高（80.6）。这些细粒度差异是仅看τ²复合分数（模型间相近）所无法捕捉的。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向主要体现在以下几个方面。首先，在规则解释与执行层面，当前方法难以区分提示词中的强制约束与建议性指导，导致对“故意不服从”行为的判定存在模糊性。未来需探索更细粒度、结构化的策略定义，明确区分这两类指令，并研究智能体在任务完成与规则遵循之间的权衡机制。其次，在评估架构上，论文指出规则提取与合规检查对模型能力要求不同，未来可设计非对称架构，即用强大模型提取规则，再用轻量模型进行批量检查，以降低持续评估成本。此外，当前方法将多维执行轨迹压缩为单一聚合分数，存在规则重叠导致的重复惩罚问题，未来需研究语义去重和根因定位算法，实现因果感知的评分框架。最后，在规模化部署方面，如何对海量违规信号进行分级、去重和可视化汇总，以避免告警疲劳并提升可操作性，是实际应用的关键挑战。未来可探索集成严重性分级、趋势分析面板等机制，使输出结果更易于人工处理与决策。

### Q6: 总结一下论文的主要内容

该论文针对AI智能体在复杂多步工作流中产生的长执行轨迹（agentic traces）难以有效评估的问题，提出了一种名为AgentPex的自动化检测工具。其核心贡献在于超越了仅关注最终结果的评测方法，通过从智能体提示和系统指令中自动提取行为规则，构建了一套规范说明，并据此系统性地检查轨迹中是否存在违规行为，如错误的工作流路由、不安全工具使用或违反既定规则等。该方法在涵盖电信、零售和航空客服领域的424条轨迹上进行了评估，结果表明AgentPex能有效区分不同模型的行为，并发现仅靠结果评分无法捕捉的规范违反情况。其意义在于为开发者提供了细粒度的、可扩展的分析能力，有助于大规模理解智能体的优势与缺陷，从而提升智能体系统的可靠性与安全性。
