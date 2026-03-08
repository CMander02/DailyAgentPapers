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
  key_technique: "Recursive Think-Answer Process (R-TAP)"
  primary_benchmark: "AIME25, HMMT Feb 25, OmniMath, GPQA, LiveCodeBench, MMMU, MathVista, OlympiadBench, MathVision, MMMU-Pro"
---

# Recursive Think-Answer Process for LLMs and VLMs

## 原始摘要

Think-Answer reasoners such as DeepSeek-R1 have made notable progress by leveraging interpretable internal reasoning. However, despite the frequent presence of self-reflective cues like "Oops!", they remain vulnerable to output errors during single-pass inference. To address this limitation, we propose an efficient Recursive Think-Answer Process (R-TAP) that enables models to engage in iterative reasoning cycles and generate more accurate answers, going beyond conventional single-pass approaches. Central to this approach is a confidence generator that evaluates the certainty of model responses and guides subsequent improvements. By incorporating two complementary rewards-Recursively Confidence Increase Reward and Final Answer Confidence Reward-we show that R-TAP-enhanced models consistently outperform conventional single-pass methods for both large language models (LLMs) and vision-language models (VLMs). Moreover, by analyzing the frequency of "Oops"-like expressions in model responses, we find that R-TAP-applied models exhibit significantly fewer self-reflective patterns, resulting in more stable and faster inference-time reasoning. We hope R-TAP pave the way evolving into efficient and elaborated methods to refine the reasoning processes of future AI.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前“思维-回答”推理模型（如DeepSeek-R1）在单次推理过程中容易产生错误且无法自我修正的核心问题。研究背景是，以OpenAI o1和DeepSeek-R1为代表的模型通过显式分离思维链和答案生成阶段，显著提升了数学推理和编程等复杂任务的性能，并将此范式扩展到了视觉-语言模型。然而，现有方法存在一个关键不足：它们几乎都依赖于单次推理轨迹。模型生成一个“思维-答案”对后便停止推理，即使其内部推理可能不准确、不一致或表现出明显的不确定性（例如输出“Oops!”等自我反思性提示）。这些不确定性信号未被利用，模型缺乏自我评估和迭代修正的机制，导致错误但看似自信的推理无法被纠正，严重影响了模型的可靠性和一致性。这种局限源于当前强化学习框架（如GRPO）通常只优化单次推理轨迹的奖励（如准确性），而未考虑模型对自身推理过程的置信度，因此无法支持内省检查或递归修正。

本文要解决的核心问题是：如何让大语言模型和视觉-语言模型能够进行迭代式、自我修正的推理，超越僵化的单次“思维-答案”范式。为此，论文提出了递归思维-回答过程，其核心是引入一个置信度生成器来评估模型每次推理循环的确定性，并以此指导后续改进。通过结合两种互补的奖励机制，模型被训练进行多次推理循环，在置信度低时主动重新思考并修正答案，从而实现更准确、稳定的推理。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：大模型演进、思维-答案推理范式，以及迭代与置信度引导的优化方法。

在大模型演进方面，早期如GPT-3展示了强大的上下文学习能力，随后InstructGPT和ChatGPT等通过人类反馈强化学习（RLHF）提升了可靠性和指令遵循。开源模型如LLaMA系列提供了轻量高性能架构，而多模态模型如LLaVA-NeXT、MM1等则增强了视觉语言理解。然而，这些模型在推理时大多依赖单次前向预测，缺乏迭代自省。

在思维-答案推理范式上，Chain-of-Thought提示首次证明了生成中间推理步骤的益处，后续扩展如Tree of Thoughts、Graph of Thoughts通过结构化搜索探索更大推理空间。近期，DeepSeek-R1和OpenAI o1等模型明确分离“思考”与“回答”阶段，在数学和代码推理上取得显著进展。多模态领域也有类似工作，如LMM-R1、Vision-R1等。但这些方法通常采用单次推理轨迹，即使模型输出中出现了“Oops!”等自我反思线索，推理也会终止，缺乏内部置信度评估来引导是否需要进一步推理。

在迭代与置信度引导的优化方面，已有研究探索通过外部验证或启发式反馈进行迭代优化，例如Reflexion和Self-Consistency。然而，这些方法要么在思维-答案框架之外运作，要么依赖于多数投票而非内省式的确定性评估。先前工作缺乏一个原则性的机制，让模型能够内部估计推理的正确性并动态触发额外的推理循环。

本文提出的R-TAP方法与上述工作的核心区别在于，它首次在思维-答案模型中显式引入了置信度生成器，以评估模型响应的确定性，并引导后续的迭代改进。通过结合“递归置信度增长奖励”和“最终答案置信度奖励”，R-TAP使模型能够进行内省、检测低置信度推理，并选择性地重新进入额外的推理循环，从而超越了现有方法的静态、单次推理性质。

### Q3: 论文如何解决这个问题？

论文通过提出一种高效的递归思考-回答过程（R-TAP）来解决单次推理中模型输出易错的问题。其核心方法是让模型进行置信度引导的迭代推理循环，而非传统的单次推理。整体框架允许模型递归生成一系列思考-回答序列，其中每一步的生成都基于之前的所有步骤。关键创新在于引入了一个仅在训练时使用的置信度生成器，该组件能评估模型每次响应的可靠性，并输出一个0到1之间的置信度分数。置信度生成器基于参考模型的结构构建，但将语言头替换为一个置信度头，并通过Sigmoid激活函数输出。

训练过程中，R-TAP采用基于分组相对策略优化（GRPO）的目标函数，并设计了两项互补的置信度驱动奖励来指导学习：一是递归置信度增加奖励，鼓励模型在后续步骤中提升置信度，实现有意义的迭代改进；二是最终答案置信度奖励，要求最终答案的置信度达到预设阈值，以确保输出足够确定。此外，训练目标还结合了格式正确性、答案准确性和长度惩罚等常规奖励。通过这种奖励机制，模型被鼓励在内部检测到低置信度时进行更深度的递归推理，而在置信度足够高时则提前终止，从而在推理时实现动态、自适应的推理深度。

该方法的主要优势在于，置信度生成器仅在训练阶段使用，在推理时被移除，因此不会引入任何额外的推理开销。这使得增强后的模型在保持单次推理效率的同时，获得了自我评估不确定性和选择性优化推理的能力，从而产生更稳定、更准确的输出。实验表明，应用R-TAP的模型在多项数学和推理基准测试中均显著优于传统的单次推理方法。

### Q4: 论文做了哪些实验？

实验在NVIDIA A100 80GB GPU上进行，使用vLLM加速文本生成，并采用DeepSpeed ZeRO-3进行训练。实验设置包括两个主要阶段：首先预训练置信度生成器，为每个问题生成128个响应；然后联合训练LLMs/VLMs和置信度生成器，设置递归深度T=4，每轮生成G=12个输出，使用GRPO算法进行12次迭代更新，并优化了温度、top-p等生成超参数。

使用的数据集和基准测试包括：针对LLMs的AIME25、HMMT Feb25、OmniMath、GPQA和LiveCodeBench；针对VLMs的MMMU、MathVista、OlympiadBench、MathVision和MMMU-Pro。对比方法主要是传统的单次推理基线（Baseline）以及R-TAP的不同变体，包括单独或组合使用置信度生成器（Cφ）、递归置信度提升奖励（R_Increase）、最终答案置信度奖励（R_Final）和答案奖励（R_Answer）。

主要结果显示，完整的R-TAP方法（包含所有组件）在LLMs上取得了最佳平均性能（75.8分），相比基线（69.7分）有显著提升。具体指标上，在AIME25达到83.7分，HMMT Feb25达到60.3分。在VLMs上，完整R-TAP平均得分为69.2分，显著高于基线的62.2分，其中MathVista得分达到82.3分。消融实验表明，移除任一关键奖励都会导致性能下降，特别是移除R_Answer时LLMs平均分骤降至56.1分。此外，与多种置信度估计方法对比，R-TAP在多数基准上表现最优。分析还发现，应用R-TAP后模型响应中“Oops”类自反思表达显著减少，表明推理过程更稳定高效。

### Q5: 有什么可以进一步探索的点？

本文提出的R-TAP方法通过递归循环和置信度评估改进了单次推理的局限性，但仍存在一些可探索的方向。首先，其置信度生成器可能依赖启发式规则或简单标量，未来可研究更精细、可学习的置信度评估模块，例如基于模型内部激活或不确定性量化的方法。其次，当前递归过程可能增加计算开销，未来可探索动态终止机制，在置信度足够高时提前退出循环以提升效率。此外，该方法主要关注封闭式问答，可扩展至开放式生成、多模态规划或复杂决策任务，验证其泛化能力。最后，文中提到“Oops”类表达减少意味着模型更稳定，但这可能掩盖了错误未被识别的情况，未来可研究如何区分“过度自信”与“合理确信”，并引入外部验证或对抗性测试来进一步提升鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文针对当前Think-Answer推理模型（如DeepSeek-R1）在单次推理中易出错、无法自我修正的问题，提出了一种高效的递归Think-Answer过程（R-TAP）。其核心贡献在于设计了一个基于置信度的迭代推理框架，使大语言模型和视觉语言模型能够进行多轮自我反思和修正。

方法上，R-TAP引入了一个置信度生成器来评估模型每次推理的确定性，并设计了两项互补的奖励机制：递归置信度提升奖励和最终答案置信度奖励。通过强化学习，模型被训练为在置信度低时自动启动新一轮的“思考-回答”循环，从而迭代优化推理路径。

主要结论显示，采用R-TAP的模型在多种语言和视觉语言推理基准测试中，性能持续超越传统的单次推理方法。此外，模型输出中“Oops!”等自我反思性表达显著减少，表明其推理过程更加稳定、准确，且推理速度更快。R-TAP为未来AI模型的推理过程提供了一种高效、精细化的优化路径。
