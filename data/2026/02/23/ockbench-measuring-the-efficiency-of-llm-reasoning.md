---
title: "OckBench: Measuring the Efficiency of LLM Reasoning"
authors:
  - "Zheng Du"
  - "Hao Kang"
  - "Song Han"
  - "Tushar Krishna"
  - "Ligeng Zhu"
date: "2025-11-07"
arxiv_id: "2511.05722"
arxiv_url: "https://arxiv.org/abs/2511.05722"
pdf_url: "https://arxiv.org/pdf/2511.05722v2"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent评测/基准"
  - "LLM推理"
  - "效率评估"
  - "Token效率"
  - "基准测试"
relevance_score: 7.5
---

# OckBench: Measuring the Efficiency of LLM Reasoning

## 原始摘要

Large language models (LLMs) such as GPT-5 and Gemini 3 have pushed the frontier of automated reasoning and code generation. Yet current benchmarks emphasize accuracy and output quality, neglecting a critical dimension: efficiency of token usage. The token efficiency is highly variable in practical. Models solving the same problem with similar accuracy can exhibit up to a \textbf{5.0$\times$} difference in token length, leading to massive gap of model reasoning ability. Such variance exposes significant redundancy, highlighting the critical need for a standardized benchmark to quantify the gap of token efficiency. Thus, we introduce OckBench, the first benchmark that jointly measures accuracy and token efficiency across reasoning and coding tasks. Our evaluation reveals that token efficiency remains largely unoptimized across current models, significantly inflating serving costs and latency. These findings provide a concrete roadmap for the community to optimize the latent reasoning ability, token efficiency. Ultimately, we argue for an evaluation paradigm shift: tokens must not be multiplied beyond necessity. Our benchmarks are available at https://ockbench.github.io/.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型评估体系中忽视“推理效率”这一关键维度的问题。研究背景是，以GPT-5、Gemini 3等为代表的LLMs，在思维链等技术的加持下，推理能力显著提升，但随之而来的是生成长度急剧膨胀，导致高昂的推理成本和延迟。现有主流评测基准（如HELM、Chatbot Arena）几乎完全聚焦于输出结果的准确性，而忽略了模型在达成相同准确率时所消耗的令牌数量（即令牌效率）存在巨大差异。这种差异（论文指出可达5倍）暴露了模型推理过程中存在显著冗余，表明仅凭准确性已不足以全面评估模型的真实能力。

因此，本文要解决的核心问题是：如何系统性地衡量和比较LLMs在推理和代码生成任务中的“令牌效率”，并将其与准确性结合起来，以提供更全面的模型能力评估。为此，论文提出了首个同时衡量准确性和令牌效率的基准测试OckBench，并引入了“每令牌智能”这一新概念，旨在推动评估范式的转变，引导社区优化模型的潜在推理能力与效率，降低实际部署成本。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测基准类、推理效率优化类和成本评估类。

在**评测基准类**工作中，现有基准如GSM8K、HumanEval和MATH等主要关注推理或代码生成的准确性，而忽视了生成过程中的令牌使用效率。OckBench与这些工作的核心区别在于，它首次将准确性与令牌效率（即生成相同质量答案所需的令牌数量）结合起来进行联合评估，填补了现有基准在衡量推理“经济性”方面的空白。

在**推理效率优化类**研究中，已有工作致力于改进推理链（CoT）或采样策略以减少计算开销，但这些优化通常以提高准确性为目标，或作为独立的效率提升技术。本文的OckBench则为这类优化研究提供了一个具体的、可量化的评估框架，用于衡量不同方法在减少令牌冗余方面的实际效果。

在**成本评估类**工作中，一些研究关注大语言模型部署的推理成本和延迟。OckBench通过实证数据（如高达5倍的令牌使用差异）直接揭示了低效推理如何显著推高服务成本和延迟，从而将抽象的“效率”概念与具体的工程及经济指标联系起来，为成本优化提供了实证依据和优化方向。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为OckBench的基准测试来解决现有基准忽视推理效率（即token使用效率）的问题。其核心方法是构建一个能够同时衡量模型准确性和token效率的标准化评估框架，并引入一个综合评分指标来量化两者的权衡。

整体框架由三个主要部分组成：**基准构建**、**评估协议**和**统一评分**。首先，在基准构建上，OckBench从数学、软件工程和科学推理三个互补领域聚合任务，确保覆盖广泛的推理模式。其关键创新在于**差异化筛选机制**，该机制主动从候选问题池中筛选出那些能引发模型在token消耗上产生显著差异的问题。具体而言，它设定了两个筛选标准：1) **难度分级**：只选择模型平均准确率在0.1到0.9之间的问题，聚焦于“推理前沿”区域，避免问题过于简单或困难导致的效率差异不显著；2) **最大化token方差**：从剩余问题中选择那些在不同模型上产生的token长度方差最大的问题。这种设计确保了基准测试能有效暴露模型在推理路径效率上的本质差异，即区分出能“奥卡姆化”（简洁）推理的模型和“喋喋不休”（冗余）的模型。

其次，在评估协议上，论文采用了严格的标准化流程以保证可复现性和公平比较。这包括使用单次提示和贪婪解码来减少干扰，以及针对不同任务类型（数学、科学、代码）采用精确匹配或功能测试来判定准确性。效率指标则定义为模型在生成结束符之前产生的原始输出token数量，直接反映了实际部署中的计算成本。

最核心的创新点是提出了一个统一的综合评分指标——**OckScore**。该指标旨在捕捉“正确且简洁 > 正确但冗长 > 错误但简洁 > 错误且冗长”的偏好顺序。其计算公式为：`S_ock = Accuracy - λ * log(T/C)`，其中Accuracy是准确率，T是平均输出token数，λ是惩罚系数（设为10），C是归一化常数（设为10,000）。这个设计有三个关键技术考量：1) **准确性优先**：以准确性为基数，确保正确解通常优于错误解；2) **效率的对数惩罚**：使用对数尺度而非线性惩罚，既能处理token数量级差异，又避免了对必要长推理的过度惩罚或对短推理微小差异的过度敏感；3) **基于模型先验的校准**：通过参数λ和C的设定，使评分与“高智能模型应能更好权衡准确性与简洁性”的经验先验保持一致，防止奖励“短但笨”的模型。

综上所述，OckBench通过精心设计的任务筛选机制、标准化的评估协议以及创新的统一评分公式，系统性地解决了量化大语言模型推理效率差距的问题，为社区优化模型的潜在推理能力和token效率提供了具体的路线图。

### Q4: 论文做了哪些实验？

论文实验围绕评估大语言模型的推理效率展开。实验设置上，采用单次生成（single-shot）评估以减少提示工程偏差，使用辅助LLM从原始响应中解析最终答案（如数值或代码块），通过Pass@1准确率衡量正确性，并通过计算EOS标记前的平均输出标记数来量化效率。

数据集/基准测试方面，构建了OckBench基准，涵盖数学、软件工程和科学推理三个领域，但实验部分聚焦于数学子集OckBench-Math。该子集从GSM8K、AIME 2024/2025和AMO-Bench等基准中，通过“差异化筛选”策略选取了200个在不同模型间标记消耗方差最大的实例，以凸显效率差异。

对比方法包括评估了广泛的商业和开源模型。商业模型涉及Google的Gemini 3和Gemini 2.5系列，以及OpenAI的GPT-5.2、GPT-5-mini系列（分高、中、低推理强度）、o3-mini、o4-mini和GPT-4o。开源模型则包括Qwen3系列（含“思考”和“指导”变体）、DeepSeek系列（V3.2和R1架构）、Kimi-K2系列、AReaL-boba-2系列和AceReason-Nemotron模型。

主要结果通过OckScore（S_Ock）排名呈现。关键数据指标显示：Gemini 3 Pro以72.0%的准确率和20,154个平均输出标记数位居榜首（S_Ock=67.21）。Gemini 3 Flash准确率相近（71.0%），但标记消耗近乎翻倍（36,212个），效率得分较低（64.35）。在开源模型中，Kimi-K2-Thinking准确率达52.5%，但消耗标记数最高（41,746个），显著高于同等准确率的GPT-5-mini High（29,297个）。这揭示了前沿模型间存在显著的效率差距，开源模型在达到商业级准确率的同时，往往依赖更冗长的推理路径。

### Q5: 有什么可以进一步探索的点？

该论文聚焦于评估大语言模型的推理效率，提出了首个联合衡量准确性与令牌效率的基准OckBench，但其研究仍存在局限性和可拓展空间。首先，基准任务主要集中于数学推理和代码生成，未来可扩展至更广泛的领域，如逻辑推理、多模态任务或需要长期规划的复杂问题，以检验效率指标的普适性。其次，分析揭示了模型存在“过度思考”和“推理悬崖”等现象，但对其内在机制（如注意力分配、思维链冗余）的归因分析尚浅；未来可结合模型内部表示进行研究，探索更精细的优化方法，例如通过强化学习直接优化令牌效率，或设计能动态调整推理长度的自适应机制。此外，当前评估主要关注输出令牌数，未充分考虑计算成本、延迟及能耗等实际部署因素，后续可建立多维度效率评估框架。最后，该研究呼吁社区重视效率优化，但尚未提供具体的优化工具或训练范式；未来可探索高效推理的架构改进（如状态空间模型）或蒸馏技术，推动“必要不增令牌”成为模型开发的核心准则之一。

### Q6: 总结一下论文的主要内容

该论文针对当前大语言模型（LLM）评估中普遍忽视推理效率的问题，提出了首个联合衡量准确性与令牌效率的基准OckBench。现有基准主要关注输出质量，但实践中模型解决相同问题的令牌使用量差异巨大（可达5倍），导致服务成本和延迟显著增加，这暴露了模型推理能力存在大量冗余。OckBench通过系统性地评估模型在推理和代码生成任务上的表现，量化了令牌效率差距。评估结果表明，当前主流模型的令牌效率普遍未得到优化。论文的核心贡献在于揭示了效率评估的关键性，并倡导评估范式应转向“非必要不增加令牌”，为社区优化模型潜在推理能力和效率提供了具体路线图。
