---
title: "Recursive Think-Answer Process for LLMs and VLMs"
authors:
  - "Byung-Kwan Lee"
  - "Youngchae Chee"
  - "Yong Man Ro"
date: "2026-03-02"
arxiv_id: "2603.02099"
arxiv_url: "https://arxiv.org/abs/2603.02099"
pdf_url: "https://arxiv.org/pdf/2603.02099v2"
categories:
  - "cs.CL"
tags:
  - "Reasoning & Planning"
  - "Learning & Optimization"
relevance_score: 7.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "Recursive Think-Answer Process (R-TAP), Recursively Confidence Increase Reward, Final Answer Confidence Reward"
  primary_benchmark: "AIME25, HMMT Feb 25, OmniMath, GPQA, LiveCodeBench, MMMU, MathVista, OlympiadBench, MathVision, MMMU-Pro"
---

# Recursive Think-Answer Process for LLMs and VLMs

## 原始摘要

Think-Answer reasoners such as DeepSeek-R1 have made notable progress by leveraging interpretable internal reasoning. However, despite the frequent presence of self-reflective cues like "Oops!", they remain vulnerable to output errors during single-pass inference. To address this limitation, we propose an efficient Recursive Think-Answer Process (R-TAP) that enables models to engage in iterative reasoning cycles and generate more accurate answers, going beyond conventional single-pass approaches. Central to this approach is a confidence generator that evaluates the certainty of model responses and guides subsequent improvements. By incorporating two complementary rewards-Recursively Confidence Increase Reward and Final Answer Confidence Reward-we show that R-TAP-enhanced models consistently outperform conventional single-pass methods for both large language models (LLMs) and vision-language models (VLMs). Moreover, by analyzing the frequency of "Oops"-like expressions in model responses, we find that R-TAP-applied models exhibit significantly fewer self-reflective patterns, resulting in more stable and faster inference-time reasoning. We hope R-TAP pave the way evolving into efficient and elaborated methods to refine the reasoning processes of future AI.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于“思考-回答”范式的大语言模型和视觉语言模型在单次推理过程中存在的局限性问题。研究背景是，以OpenAI的o1和DeepSeek-R1为代表的模型通过将推理过程和最终答案生成显式分离，显著提升了在数学推理、编程等复杂任务上的性能。然而，现有方法普遍采用单次推理轨迹，即模型生成一次“思考-回答”对后便停止，即使其内部推理可能包含错误或不一致。模型输出中常出现“Oops!”等自我反思性提示，表明其自身存在不确定性，但这些信号在现有框架下并未被有效利用以触发修正。现有强化学习训练方法（如GRPO）通常仅优化单次推理轨迹的准确性或格式，缺乏对模型自身置信度的考量，因此无法支持模型进行内省检查或递归修正，导致错误但看似自信的推理无法被纠正，影响了模型的可靠性和一致性。

本文要解决的核心问题是：如何突破单次推理的限制，使模型能够基于对自身推理确定性的评估，进行迭代式的、自我修正的推理。为此，论文提出了递归思考-回答过程（R-TAP），其核心是引入一个置信度生成器来评估模型每次推理循环的确定性，并设计两种互补的奖励机制（递归置信度提升奖励和最终答案置信度奖励），引导模型在置信度不足时主动发起新一轮的推理循环，从而迭代地精炼其思考过程，生成更准确、更稳定的答案。该方法旨在实现无需增加推理时开销的、更高效可靠的推理。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：大模型演进、思维链推理方法，以及迭代精炼技术。

在大模型演进方面，早期工作如GPT-3展示了强大的上下文学习能力，随后的InstructGPT和ChatGPT利用人类反馈强化学习（RLHF）提升了可靠性和指令遵循。开源模型如LLaMA系列提供了轻量高性能架构，而多模态模型如LLaVA-NeXT、MM1等则增强了视觉语言理解。然而，这些模型在推理时大多依赖单次前向预测，缺乏迭代自省。

在思维链推理方法上，Chain-of-Thought提示首次证明了生成中间推理步骤的益处。后续扩展如Program-of-Thoughts、Tree of Thoughts和Graph of Thoughts通过结构化搜索探索更大的推理空间。近期，Think-Answer范式（如DeepSeek-R1和OpenAI o1）将“思考”与“回答”分离，在数学和代码推理上取得显著效果。多模态领域也有类似模型（如LMM-R1、Vision-R1）。但这些方法通常采用单次推理轨迹，即使模型输出中包含“Oops!”等自我反思线索，推理也会终止，缺乏内部置信度评估来引导进一步思考。

在迭代精炼方面，已有工作探索通过外部验证或启发式反馈进行改进，例如Reflexion和Self-Consistency。然而，这些方法要么在思维链框架外运作，要么依赖多数投票而非内省置信度。它们缺乏一个原则性机制，让模型能够内部评估推理的正确性并动态触发额外的推理循环。

本文提出的R-TAP与上述工作的核心区别在于，它首次在Think-Answer框架内，引入了一个置信度生成器来评估模型响应的确定性，并以此指导递归的、迭代的推理循环。通过结合“递归置信度增长奖励”和“最终答案置信度奖励”，R-TAP使模型能够进行内省，检测低置信度推理，并选择性地重新进行推理，从而超越了传统单次推理方法的静态局限性。

### Q3: 论文如何解决这个问题？

论文通过提出一种高效的递归思考-回答过程（R-TAP）来解决单次推理中模型输出易错的问题。其核心是让模型能够进行置信度引导的迭代推理循环，从而超越传统的单次推理方法。

整体框架建立在现有Think-Answer架构之上，但引入了递归生成机制。给定一个问题，模型不再只生成一个思考-回答过程，而是递归地生成一个序列。在训练时，递归深度T是固定的，以便进行高效的批量采样；而在推理时，模型内部会自主决定是继续推理还是终止。

该方法的关键创新组件是置信度生成器。它仅在训练阶段使用，在推理时被移除，因此不增加推理开销。其架构基于参考模型，但将语言头替换为一个输出标量置信度分数（0到1之间）的置信度头，并通过Sigmoid激活。在R-TAP训练前，会使用监督预训练来初始化置信度生成器，使其能够判断给定回答的正确性。

训练的核心是设计了两项互补的置信度驱动奖励，并通过GRPO目标进行优化。第一项是递归置信度提升奖励，旨在鼓励模型在后续步骤中做出有意义的改进，其计算基于置信度是否随着递归步骤增加。第二项是最终答案置信度奖励，要求最终答案的置信度必须达到预设阈值。总奖励是这两项奖励与格式奖励、答案正确性奖励和长度惩罚等常规奖励的加权和。

这种方法的主要创新点在于：1）将单次推理扩展为可内部控制的递归过程，实现了“评估可靠性-不确定时继续推理-足够确信时提前终止”的闭环；2）设计了专门的置信度生成器和双奖励机制，系统性地引导模型进行自我改进；3）保持了推理时的高效性，因为置信度生成器仅在训练时使用，模型在推理时仅依靠自身习得的能力进行递归决策。实验表明，应用R-TAP的模型在多项基准测试上均显著优于单次推理方法，并且其输出中类似“Oops”的自反性表达显著减少，推理更加稳定快速。

### Q4: 论文做了哪些实验？

实验在NVIDIA A100 80GB GPU上进行，使用vLLM加速文本生成。实验设置包括两个主要训练阶段：首先预训练置信度生成器，为每个问题生成128个响应；随后联合训练LLMs/VLMs和置信度生成器，设置递归深度T=4，每轮生成G=12个响应，并使用GRPO算法进行12次迭代优化，关键超参数包括学习率1e-6、温度1.0等。

数据集与基准测试涵盖LLM和VLM任务。LLM评估使用AIME25、HMMT Feb25、OmniMath、GPQA和LiveCodeBench五个数学与代码基准；VLM评估使用MMMU、MathVista、OlympiadBench、MathVision和MMMU-Pro五个多模态数学基准。

对比方法包括单次推理基线（Baseline）与不同配置的R-TAP变体（逐步添加置信度生成器Cφ、递归置信度增长奖励R_Increase、最终答案置信度奖励R_Final）。主要结果显示，完整R-TAP方法在LLM上平均得分达75.8，较基线69.7提升6.1点；在VLM上平均得分达69.2，较基线62.2提升7.0点。关键数据指标如：在LLM的AIME25任务中，R-TAP得分为83.7（基线78.0）；在VLM的MathVista任务中，R-TAP得分为82.3（基线74.0）。消融实验证实各组件均贡献性能提升，且移除答案奖励R_Answer会导致性能大幅下降（LLM平均分降至56.1）。此外，与多种置信度估计方法对比中，R-TAP均取得最优平均性能。

### Q5: 有什么可以进一步探索的点？

该论文提出的R-TAP方法通过递归循环和置信度评估改进了单次推理的局限性，但仍有一些方向值得深入探索。首先，其置信度生成器主要依赖模型内部评分，未来可结合外部验证或不确定性量化方法，以更客观地评估答案可靠性。其次，当前递归过程可能增加计算开销，需研究动态终止机制，在准确性和效率间取得平衡。此外，该方法在视觉-语言模型中的应用仍较初步，可探索多模态任务中递归推理的具体形式，如如何融合图像和文本的交叉验证。最后，论文提到“Oops”类表达减少反映了推理稳定性，但未深入分析其与错误类型的关联，未来可研究不同错误模式下的递归策略优化，实现更精细的自我修正。

### Q6: 总结一下论文的主要内容

该论文针对当前Think-Answer推理器（如DeepSeek-R1）在单次推理中易出错的问题，提出了一种高效的递归思考-回答过程（R-TAP）。核心贡献在于设计了一个迭代推理框架，使大语言模型和视觉语言模型能够通过多轮循环来修正和优化答案，而非依赖传统单次推理。方法上，R-TAP引入了一个置信度生成器来评估模型响应的确定性，并指导后续改进；同时结合两种互补的奖励机制——递归置信度提升奖励和最终答案置信度奖励——以驱动模型在迭代中提升准确性。实验表明，采用R-TAP的模型在多项任务上均稳定优于单次推理方法，且模型输出中“Oops”类自我反思表达显著减少，这意味着推理过程更稳定、更快速。该工作为未来AI推理过程的精细化与高效化提供了新思路。
