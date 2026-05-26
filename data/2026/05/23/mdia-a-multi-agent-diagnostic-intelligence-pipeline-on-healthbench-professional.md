---
title: "MDIA: A Multi-Agent Diagnostic Intelligence Pipeline on HealthBench Professional"
authors:
  - "Roberto Cruz"
  - "David Rey-Blanco"
date: "2026-05-23"
arxiv_id: "2605.24699"
arxiv_url: "https://arxiv.org/abs/2605.24699"
pdf_url: "https://arxiv.org/pdf/2605.24699v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "多智能体系统"
  - "临床决策支持"
  - "医疗诊断"
  - "智能体架构"
  - "评估基准"
relevance_score: 8.0
---

# MDIA: A Multi-Agent Diagnostic Intelligence Pipeline on HealthBench Professional

## 原始摘要

Most reported gains on agentic-LLM clinical benchmarks are often attributed to prompt engineering, yet our results suggest that larger improvements can come from architectural and engine-level design. We present MDIA, a Multi-agent Diagnostic Intelligence Agent implemented as a 7-node specialty-routed clinical reasoning graph, on the full HealthBench Professional benchmark (n = 525), on a non-fine-tuned LLM. MDIA achieves 0.6272 under OpenAI's GPT-5.4-2026-03-05, which is +3.72 pp above the performance of OpenAI's ChatGPT for Clinicians. The experimental work shows that performance lift is attributable to system architecture: specialty routing, multi-turn context preservation, drug-state safety gating, site-filtered search, length-aware synthesis, and engine-level reliability. These findings support the view that agentic clinical benchmark performance is shaped both by the underlying foundation model and the orchestration architecture. Nevertheless, we also noticed notable differences when using other models as a grader; in particular, when using Gemini 2.5 Pro, MDIA scored 0.6585, which suggests that the choice of grader is a source of variability. Robust evaluation of LLMs would therefore require assessment across several independent grader models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前医疗AI评测基准中，多智能体架构设计与评估方法存在的两个关键不足。研究背景是，大语言模型正快速进入临床实践，OpenAI发布的HealthBench Professional基准（含525个真实病例）为评估提供了严格标准，但现有研究呈现出一个矛盾现象：一方面，大量文献表明，使用工具调用和专用角色的多智能体架构能显著优于单提示基线（中位提升+53个百分点）；另一方面，针对HealthBench Pro的顶级性能却常常被简单归因于提示工程。

现有方法的不足主要体现在：首先，多智能体临床管线尚未在该高难度基准上得到系统评估，尤其缺少对专业路由、多轮对话结构等架构设计的量化分析。其次，评估方法存在严重缺陷——官方的简单评估工具默认使用“展平”策略，只把对话中最后一条用户消息传给智能体，而HealthBench Pro中有22%的病例包含多轮用户追问，这种设计会静默丢弃前序上下文，导致智能体未能针对整个对话（而不是最后一个问题）作答，从而严重低估其真实能力。

本文要解决的核心问题是：通过构建一个7节点、专业路由的、带共享内存的有向无环图（DAG）多智能体诊断管线MDIA，系统性地验证**智能体整体架构**（而非单纯的提示工程）对临床基准性能的提升幅度；同时揭示评估中“对话展平策略”对分数产生的6个百分点级巨大干扰，并提出多轮对话保留的必要性，以及评估结果因评估模型选择而产生的变异性问题。

### Q2: 有哪些相关研究？

相关研究主要分为评测基准和多智能体架构两类。在评测基准方面，早期医学LLM评测多采用MedQA、MedMCQA、PubMedQA及MMLU医学子集等静态问答数据集，主要测试知识储备与结构化推理能力。随后出现了面向工作流程的评测如AgentClinic、MedAgentBench、PhysicianBench，发现前沿模型在顺序性、工具使用的临床场景中表现不佳。OpenAI的HealthBench系列（含5,000个多轮临床对话）及HealthBench Professional（525个跨26专科的真实临床案例）进一步推动评估向真实临床交互靠拢，后者采用医生编写的评分标准（rubric-graded）。MDIA与这些工作的核心区别在于：它不仅验证了特定基准（HealthBench Pro）的性能，更揭示了架构设计（如专科路由、多轮上下文保留）对性能的提升效果超过了单纯提示工程改进。

在多智能体方法方面，一项包含20个智能体研究的系统综述发现，所有智能体架构均优于基线LLM，其中单智能体工具调用系统的中位数提升达+53 pp。MDIA作为7节点专科路由的临床推理图，其架构包含专科路由、多轮上下文保留、药物状态安全门控、站点过滤搜索、长度感知合成及引擎级可靠性等创新设计。与ChatGPT for Clinicians等闭源系统相比，MDIA在未微调通用模型（GPT-5.4）上实现了+3.72 pp的提升（0.6272 vs 0.590），且性能增益主要来自系统架构而非提示工程。研究还首次揭示了评分模型（Grader）选择带来的显著变异性（如Gemini 2.5 Pro评分时得分升至0.6585），这为后续鲁棒评估提出了新要求。

### Q3: 论文如何解决这个问题？

MDIA通过一个7节点专业路由的临床推理图架构来解决HealthBench专业基准测试中的复杂诊断问题。核心方法是将诊断过程分解为多个专门化模块，形成一个有向无环图，由TietAI的Hydra图引擎执行。架构设计包括五个主要组件：首先，Intake节点作为工具调用研究协调器，调用14种医学工具（如PubMed、ClinicalTrials、DailyMed等）收集结构化档案，并保持多轮对话上下文。其次，Router节点作为专业分类器，读取档案后决定路由到哪个专家代理。然后，三个专用推理节点（GI_reasoner、Ophtho_reasoner、Neuro_reasoner）针对特定专科加载精选知识锚点（如Glasgow-Blatchford评分、NIHSS等），解决通用推理器在专科知识上的不足。此外，Generalist推理节点覆盖其他长尾专科。Output节点作为合成器，将推理结果转化为用户友好响应，并采用长度感知合成策略（2000-3000字符目标，4000硬上限）。最后，Verifier节点执行最终安全性和格式检查。

关键技术包括：多轮对话上下文保持，通过multiturn策略传递完整消息列表；药物状态安全门控，在编写任务分支强制进行药物与患者状态检查；站点过滤搜索，限制高权威医学来源；引擎级可靠性改进，包括JSON栅栏剥离、空输出重试、优雅降级消息。这些设计使MDIA在非微调LLM上达到0.6272分数，比OpenAI的ChatGPT for Clinicians高出3.72个百分点。

### Q4: 论文做了哪些实验？

论文围绕MDIA多智能体诊断系统在HealthBench Professional基准上开展了一系列实验。实验设置包括使用非微调的GPT-5.4-2026-03-05作为基础模型，在包含525个样本的HealthBench Professional数据集上进行评估。主要对比方法包括OpenAI的ChatGPT for Clinicians（得分0.590）、GPT-5.4单智能体基线（0.481）以及医生撰写基线（0.437）。MDIA v1.0.53版本在GPT-5.4评分下取得0.6272，比ChatGPT for Clinicians高3.72个百分点，比单智能体高14.62个百分点。关键消融实验显示：多轮上下文保留（v1.0.40版本）使得分提升6.3个百分点；搜索噪声过滤（v1.0.41）带来约1.3个百分点提升；药物状态安全门控（v1.0.27）贡献2.2个百分点；引擎级可靠性修复将空响应率从3.8%降至0.2%，恢复约3-4个百分点。通过自举重采样估计统计变异性得到σ≈0.023。使用Gemini 2.5 Pro作为替代评分器时，MDIA得分为0.6585，表明评分器选择是结果变异的重要来源。4500字符长度限制的引入（v1.0.53）使平均响应长度从4383降至2789字符，进一步提升了1.06个百分点。

### Q5: 有什么可以进一步探索的点？

首先，MDIA的评估完全依赖闭源LLM作为grader，如GPT-5.4和Gemini 2.5 Pro，这引入了显著的grader偏差。未来可探索使用开源模型或多模型投票机制来增强评估的鲁棒性，并量化grader选择对最终分数的影响。

其次，当前架构的7个节点是静态设计的，例如“drug-state safety gating”和“site-filtered search”依赖硬编码规则。可改进方向是引入动态节点路由，让系统根据病例复杂度自动调整推理路径，或引入强化学习来优化节点间的信息传递权重。

另外，论文未讨论跨语言或低资源医疗场景的适应性。未来可将MDIA迁移到非英语临床数据集上测试，并研究其在不同医疗体系（如中国、非洲）的泛化能力。

最后，可探索将MDIA与检索增强生成（RAG）结合，从实时更新的医学知识库中获取证据，而不仅依赖预训练模型的知识截断。同时，增加用户-代理协作反馈循环，让MDIA能从专家纠正中增量学习，可能进一步提升临床决策的准确性与安全性。

### Q6: 总结一下论文的主要内容

本文提出了MDIA（多智能体诊断智能代理）系统，针对HealthBench Professional临床基准（525个案例）进行了评估。该系统是一个7节点、专科路由的有向无环图（DAG），集成了14种医学工具、药物安全门控、多轮对话上下文保留、站点过滤搜索和长度感知合成等机制。在未微调的GPT-5.4模型上，MDIA取得了0.6272的分数，比OpenAI的ChatGPT for Clinicians高出3.72个百分点，比GPT-5.4单智能体基线高出14.62个百分点。核心贡献在于证明了性能提升主要来源于系统架构设计（专科路由、引擎可靠性修复等），而非提示工程。实验还发现，评估时将多轮对话扁平化为仅最后一轮消息会错误地丢弃22%案例的上文，导致分数降低约6个百分点；同时，评分模型的选择（如Gemini 2.5 Pro）会引入显著变异性。该工作强调了在临床基准评估中报告扁平化策略和采用多评分模型的重要性。
