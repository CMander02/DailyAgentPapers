---
title: "Scaffold Effects on GAIA: A Controlled Comparison"
authors:
  - "Jason Starace"
date: "2026-06-07"
arxiv_id: "2606.08529"
arxiv_url: "https://arxiv.org/abs/2606.08529"
pdf_url: "https://arxiv.org/pdf/2606.08529v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "LLM Agent 评测"
  - "Agent 架构对比"
  - "Scaffold 效应"
  - "多智能体系统"
  - "工具使用"
  - "GAIA 基准"
  - "规划-执行模式"
  - "ReAct"
relevance_score: 9.5
---

# Scaffold Effects on GAIA: A Controlled Comparison

## 原始摘要

Published agent capability scores conflate what a model can do with what its scaffold lets it do, and the magnitude of this elicitation gap is not well characterized under controlled conditions. This study executes a pre-registered controlled comparison of three scaffolds (ReAct, a Planner-Actor-Rater multi-agent design, and planner-then-executor) across five models from three providers (Claude Opus 4.7, Sonnet 4.6, Haiku 4.5; Gemini 3.1 Pro Preview; GPT-5.5) on GAIA validation Levels 1 and 2, holding tasks and conditions fixed, with three attempts per question. Scaffold choice alone moves measured accuracy by as much as 28 percentage points within a single model (Opus, Level 2, robust slice), confirming the pre-registered hypothesis that scaffold variation produces gaps of at least 10 points. The pre-registered prediction that more capable models would be less scaffold-sensitive is rejected in direction: scaffold effects vary significantly by model in every dataset slice, but the most capable Anthropic model gains the most from structured scaffolds at the harder level, and tier-scaling holds only at Level 1 under the robust slice. The multi-agent advantage over ReAct at Level 2 appears within the Anthropic family but not for the cross-provider models, making model family rather than capability tier the conditioning variable, and the predicted planner-executor advantage on file-reading tasks is falsified. Structured scaffolds make fewer tool calls yet recover more often from mid-trajectory errors at the harder level, and a single cell (Gemini with planner-then-executor) is the cheapest at both levels and the most accurate at Level 2. These results indicate that single-scaffold capability numbers are scaffold-conditional estimates and that the elicitation gap is not guaranteed to shrink as models improve.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI Agent评估中的一个核心混淆问题：公开的模型能力分数实际上混合了模型本身的能力和其所使用的“脚手架”（scaffold）的贡献，但两者之间的“激发差距”（elicitation gap）在受控条件下尚未被准确量化。现有评估方法（如METR的时间范围论文）虽然承认良好激发能显著改变性能，并将其视为合理下界，但没有系统比较过不同脚手架对同一模型表现的影响。当不同团队用各自最佳脚手架比较不同模型时，能力比较被脚手架质量所污染，导致基于这些数字的能力外推和预测隐含了混淆变量。本研究的核心目标是通过一个预注册的受控实验，在GAIA验证集的Level 1和Level 2上，对三个不同脚手架（ReAct、多智能体设计、先规划后执行）和五个前沿模型，在固定任务与条件下进行系统比较，以隔离并量化脚手架效应本身的大小。研究发现，仅更换脚手架就可在同一模型内造成高达28个百分点的准确率差异，推翻了“更强模型对脚手架敏感度更低”的常见假设，证明单一脚手架的性能测量结果本质上是脚手架的条件估计，且激发差距并不会随模型能力提升而自然缩小。

### Q2: 有哪些相关研究？

相关研究可分为三类。首先是方法类工作，如ReAct（标准交替推理-行动循环）、AgentBench（固定agent循环的多环境评估），以及聚焦推理时计算分配而非循环结构的研究。这些工作将scaffold视为评估工具而非研究对象。其次是评测类工作，METR的时间框架研究提出了“elicitation-as-lower-bound”问题，但其局限性附录仅将测量视为受elicitation限制的下界，未在共享基准上进行受控比较。第三是应用与分析类工作，近期研究量化了scaffold和elicitation效应：预测前沿agent能力时，低/高elicitation split导致SWE-Bench上Claude Sonnet 3.5有约30个百分点的差距；评估33种scaffold和70+模型配置发现绝对分数预测因scaffold变化而下降但排序稳定；大型安全基准研究（N=62,808）显示scaffold对安全测量的影响很小。本研究与这些工作的区别在于：它不是在编码或安全基准上，而是在通用助手基准GAIA上对当前前沿模型进行受控比较，专门探究scaffold选择对同一模型能力测量的定量影响幅度，以及该影响是否随模型能力增强而可预测缩小。

### Q3: 论文如何解决这个问题？

本论文通过一个精心设计的受控实验框架来系统性地量化支架（scaffold）对模型能力评估的影响。核心方法采用3（支架）×5（模型）的全因子实验设计，在GAIA验证集的Level 1和Level 2上执行，每个实验单元进行三次尝试，共计6255次验证运行。

整体框架基于Inspect AI开源评估平台实现，确保实验的可复现性。三个主要支架模块包括：S1（ReAct基线），采用标准的单智能体交替推理-行动循环；S2（规划者-执行者-评估者多智能体架构），将任务分解为三个角色共享任务状态，规划者分解任务、执行者执行子任务、评估者审查进度；S3（先规划后执行架构），分为无工具访问的显式规划阶段和基于规划的执行阶段。

关键技术特点包括：统一的工具集设计（S2和S3共享网络搜索、沙箱Shell、Python沙箱和文本编辑器），严格控制模型推理模式（所有模型关闭推理模式避免混淆），采用官方GAIA评分器保证评分一致性，以及完整的统计分析方法（包括bootstrap置信区间、混合效应逻辑回归等）。创新点在于首次在受控条件下系统比较不同支架对同一模型的影响，发现支架选择可导致模型准确率波动高达28个百分点，且更强大的模型反而对结构化支架更敏感，拒绝预注册中关于模型能力提升会降低支架敏感性的假设。

### Q4: 论文做了哪些实验？

该论文在GAIA验证集L1和L2级别上进行了受控实验。实验设置使用三种脚手架：ReAct（s1）、Planner-Actor-Rater多智能体设计（s2）以及planner-then-executor（s3），测试了来自三家提供商的五个模型（Claude Opus 4.7、Sonnet 4.6、Haiku 4.5；Gemini 3.1 Pro Preview；GPT-5.5）。每个（模型、脚手架、级别）组合每个问题尝试三次，共产生159个L1尝试单元和258个L2尝试单元。通过三个数据切片（primary、robust去除序列化bug、intersection共享问题池）报告结果。主要发现：脚手架选择在同一模型内可使准确率最多改变28个百分点（Opus L2 robust切片），证实H1假设。H2（较弱模型脚手架效应更大）被证伪：最强模型Opus在L2获益最多。H3（多智能体优于ReAct）在L2得到条件性支持，但仅限于Anthropic模型家族。H4（planner-executor在文件读取任务上更优）被证伪。行为指标显示：结构化脚手架调用更少工具（s1 22.0次 vs s3 6.4次，L2均值），输出更少token（4.8k vs 2.9k），但中轨迹错误恢复率更高（0.38 vs 0.51）。成本分析显示Gemini+s3组合最经济且L2准确率最高。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向如下：

该研究仅测试了三种固定脚手架设计，未探索更复杂的自适应或动态脚手架。实验仅在GAIA数据集上进行，缺乏对其他复杂任务的泛化验证。模型-支架交互的发现表明，单一支架对不同模型的提升幅度差异显著，提示未来应研究**个性化支架匹配策略**，即为不同模型或任务自动选择最优支架。研究还发现结构化支架能更有效地从中期错误中恢复，但机制不明，可深入分析其失败恢复的逻辑路径。成本-正确率权衡也值得关注：例如Gemini+planner-then-executor组合在L2级别既最便宜又最准确，暗示未来可探索**低成本高效益的支架-模型配对**。此外，当前评估仅关注最终准确率，未考虑推理路径质量、鲁棒性等维度。建议引入多维度评估指标，并开发能自动调整支架复杂度的元控制器，以更有效地激发模型潜力。

### Q6: 总结一下论文的主要内容

这篇论文通过对照实验，量化了不同的智能体框架（scaffold）对模型在GAIA基准测试中表现的影响。研究发现，在固定模型和任务的情况下，仅改变框架就能使准确率产生高达28个百分点的差距（以Claude Opus 4.7在Level 2上的稳健切片为例），证实了框架效应至少为10个百分点的预注册假设。然而，与预期相反，更强大的模型对框架的敏感度并未降低，甚至表现出更强的框架依赖性；在更难的Level 2上，最先进的模型从结构化框架中获益最多。多智能体设计仅在Anthropic模型系列中表现出对ReAct的优势，而规划器-执行器框架在处理文件读取任务时也并未如预期般胜出。论文的核心贡献在于，它首次在受控条件下量化了当前前沿模型群体中的“能力提取差距”，并明确指出单框架能力评分实际上是“框架条件性”的，且随着模型能力提升，这一差距并不会自动缩小。研究结果对基于单一框架的模型能力比较方法论提出了重要警示。
