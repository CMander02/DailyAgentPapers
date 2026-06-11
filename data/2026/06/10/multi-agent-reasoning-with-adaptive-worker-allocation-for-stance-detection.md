---
title: "Multi-Agent Reasoning with Adaptive Worker Allocation for Stance Detection"
authors:
  - "Meysam Sabbaghan"
  - "Arman Zareian Jahromi"
  - "Doina Caragea"
date: "2026-06-10"
arxiv_id: "2606.11609"
arxiv_url: "https://arxiv.org/abs/2606.11609"
pdf_url: "https://arxiv.org/pdf/2606.11609v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Multi-Agent Systems"
  - "Reasoning"
  - "Adaptive Worker Allocation"
  - "Stance Detection"
  - "Manager-Worker Architecture"
relevance_score: 8.5
---

# Multi-Agent Reasoning with Adaptive Worker Allocation for Stance Detection

## 原始摘要

Stance detection requires identifying an author's position toward a target, often from short-form texts where stance is implicit, indirect, or rhetorically framed. Although large language models (LLMs) achieve strong performance on this task, single-pass prompting can be brittle when multiple interpretations are plausible. Existing aggregation strategies, such as majority voting or self-consistency, improve robustness by combining labels, but they discard the intermediate reasoning needed to resolve conflicting interpretations.
  We introduce a multi-agent reasoning framework with adaptive worker allocation for stance detection that shifts aggregation from label-level voting to reasoning-level synthesis. The framework employs a Manager-Worker architecture in which a Manager adaptively allocates a variable number of Worker agents based on input complexity. Each Worker analyzes the input from a distinct perspective and produces a reasoning-only explanation without emitting a stance label; the Manager then synthesizes these explanations to produce the final prediction.
  We evaluate the proposed framework on SemEval-2016, P-Stance, and COVID-19 Stance using Llama, Mistral, and Gemini. Results show that the framework yields the largest gains on implicit and context-dependent stance cases, achieving 86.07 Macro-F1 on COVID-19 and 82.90 on SemEval-2016, while remaining competitive on more explicit stance datasets such as P-Stance. These findings suggest that adaptive reasoning-level aggregation is most beneficial when stance cannot be reliably inferred from surface cues alone.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决立场检测中，当文本立场表达隐晦、具有讽刺性或修辞复杂时，单次大模型推理结果脆弱，以及现有标签级聚合方法（如多数投票、自一致性）丢弃中间推理过程、无法解决解释冲突的问题。

研究背景是，立场检测需要从短文本中识别作者对特定目标的立场，这通常依赖隐含、间接的线索，而非直接陈述。现有方法中，大型语言模型（LLM）虽表现良好，但单次提示的预测不够鲁棒。为提升鲁棒性，已有工作采用标签级聚合策略，但这忽略了中间推理步骤，无法在聚合时整合和权衡不同解释。

基于此，本文提出核心解决方案：一个名为 SMART-D 的自适应多智能体推理框架。它采用“管理者-工作者”（Manager-Worker）架构，将聚合从标签级投票转向推理级综合。管理者根据输入复杂性动态分配不定数量的工作者，每个工作者从不同视角生成仅包含推理的解释（不含立场标签），最后由管理者综合这些推理来做出最终预测。核心创新在于自适应的推理深度分配，使得模型在复杂案例上投入更多推理资源，而在立场明确的简单案例上则更高效。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：

1. **立场检测与LLM推理**：早期立场检测工作依赖词汇、句法和任务特定特征，近期数据集扩展到政治和公共卫生领域。LLM通过思维链、自一致性、最少到最多提示、思维树等分解推理方法提升了复杂任务性能。本文的不同在于，现有方法往往聚合最终预测标签或使用固定推理结构，无法显式对比竞争性解释，而本文框架在推理层级进行聚合。

2. **多智能体推理与自适应推理**：多智能体框架通过辩论、角色分工（如AutoGen、CAMEL、MetaGPT）以及专家混合（如MSME、DEEM）实现推理分布化。这些方法大多在表征、专家或预测层面进行路由，而本文（SMART-D）首次将推理本身作为聚合和分配的对象——Worker智能体仅生成推理解释，Manager负责综合这些解释并动态分配推理资源，根据输入复杂度调整Worker数量，从而在隐式立场样本上获得最大收益。

### Q3: 论文如何解决这个问题？

该论文提出SMART-D框架，通过“经理-工人”多智能体架构实现自适应推理级聚合，以解决立场检测中隐式、间接或修辞性表达带来的歧义问题。核心创新在于将传统标签级投票转变为推理级综合，保留中间推理过程。

整体框架包含三个阶段。第一阶段是经理规划：经理根据输入文本x、目标t和数据集标识d，首先识别数据集专属标签空间，然后评估输入复杂度，动态选择3至7个工人智能体，并为每个工人分配互补的分析角色，如显式立场线索、讽刺/反讽、间接立场、情感语气和语境框架。第二阶段是工人推理：每个工人基于自身角色分析相同输入，但被严格约束只生成基于证据的推理说明，不得输出立场标签，从而避免过早承诺标签并保留中间证据。第三阶段是经理聚合：经理收集所有工人推理说明，通过比较它们的一致性、相关性和证据支持度，综合生成最终立场预测，从而调和冲突解释。

关键技术包括自适应工人分配，根据输入复杂度调整推理深度，对显式立场使用较少工人，对隐式或上下文依赖立场分配更多视角；采用零样本提示，无微调或少样本示例；通过温度参数控制多样性（工人T=0.7，经理T=0.3）。该框架在处理隐式和上下文依赖立场时效果显著，在COVID-19和SemEval-2016数据集上分别达到86.07和82.90的Macro-F1。

### Q4: 论文做了哪些实验？

论文在三个姿态检测基准上评估了SMART-D框架：SemEval-2016 Task 6（5个目标，三分类）、P-Stance（3个美国总统目标，二分类）和COVID-19 Stance（4个公共卫生目标，三分类）。实验使用Llama-3.3 70B、Mistral-3.2 24B和Gemini-3-Flash-preview三种大语言模型作为骨干网络，每个模型同时担任Manager和Worker角色。主要结果如下：在COVID-19数据集上，SMART-D显著提升所有骨干网络的平均Macro-F1，Gemini达到86.07（相比单模型基线提升+3.99），尤其对"学校关闭"目标从76.01提升至87.35；Llama的Macro-F1从69.78提升至81.31。在SemEval-2016上，Llama取得最佳结果82.90（提升+2.67），Gemini和Mistral也有提升。在P-Stance上，Mistral从81.86提升至85.48，但Gemini和Llama有轻微下降。消融实验发现：动态分配Workers（3-7个）在性能与成本间取得平衡；Worker层面的推理贡献最大（Gemini从78.95提升至85.27）；跨模型Worker分配对弱骨干网络（Mistral从75.99提升至85.23）有益，但对强网络效果不佳。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于实验仅针对英文推特短文本，未来可扩展到多语言、多平台及长文本场景（如新闻评论或辩论记录），验证框架的通用性。计算开销方面，虽然动态分配Worker降低了冗余推理，但每个实例仍需多次LLM调用；可探索更轻量的Worker设计（例如只调用小模型生成推理说明）或利用缓存机制复用相似输入的推理路径。框架在显式立场数据上增益有限，说明结构化推理可能并非最优策略；未来可考虑混合范式，即先由Manager判断输入复杂度，对简单样本直接使用单次预测，复杂样本再启用多Worker。此外，数据集存在人口统计或意识形态偏差，需开发去偏训练或后处理校准技术。从应用角度，未来应研究如何将推理过程与可解释性结合，提供立场判断的证据链，并设计伦理约束来防止滥用系统操纵舆论。

### Q6: 总结一下论文的主要内容

该论文提出一种名为SMART-D的多智能体推理框架，用于解决立场检测任务中隐晦、间接表达难以判别的问题。传统方法依赖单次提示或标签级投票聚合，但会丢弃中间推理信息。SMART-D采用管理者-工作者架构：管理者根据输入复杂度动态分配3-7名工作者，每名工作者从不同视角（如显式线索、讽刺、间接指涉等）生成仅含推理过程的分析，禁止输出立场标签；管理者随后合成所有推理以做出最终预测。在SemEval-2016、P-Stance和COVID-19立场数据集上，基于Llama、Mistral和Gemini模型的实验表明，该方法在隐晦立场案例上提升显著，在COVID-19上宏F1达86.07%，在SemEval-2016上达82.90%，而在显式立场数据集上竞争力持平。消融实验证实推理级合成比标签级投票更关键，动态分配优于固定数量。该工作揭示了自适应推理聚合在复杂立场检测中的核心价值。
