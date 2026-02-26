---
title: "HEART: A Unified Benchmark for Assessing Humans and LLMs in Emotional Support Dialogue"
authors:
  - "Laya Iyer"
  - "Kriti Aggarwal"
  - "Sanmi Koyejo"
  - "Gail Heyman"
  - "Desmond C. Ong"
  - "Subhabrata Mukherjee"
date: "2026-01-09"
arxiv_id: "2601.19922"
arxiv_url: "https://arxiv.org/abs/2601.19922"
pdf_url: "https://arxiv.org/pdf/2601.19922v2"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent 评测/基准"
  - "LLM 应用于 Agent 场景"
  - "人机交互"
  - "对话系统"
  - "情感计算"
relevance_score: 7.5
---

# HEART: A Unified Benchmark for Assessing Humans and LLMs in Emotional Support Dialogue

## 原始摘要

Supportive conversation depends on skills that go beyond language fluency, including reading emotions, adjusting tone, and navigating moments of resistance, frustration, or distress. Despite rapid progress in language models, we still lack a clear way to understand how their abilities in these interpersonal domains compare to those of humans. We introduce HEART, the first-ever framework that directly compares humans and LLMs on the same multi-turn emotional-support conversations. For each dialogue history, we pair human and model responses and evaluate them through blinded human raters and an ensemble of LLM-as-judge evaluators. All assessments follow a rubric grounded in interpersonal communication science across five dimensions: Human Alignment, Empathic Responsiveness, Attunement, Resonance, and Task-Following. HEART uncovers striking behavioral patterns. Several frontier models approach or surpass the average human responses in perceived empathy and consistency. At the same time, humans maintain advantages in adaptive reframing, tension-naming, and nuanced tone shifts, particularly in adversarial turns. Human and LLM-as-judge preferences align on about 80 percent of pairwise comparisons, matching inter-human agreement, and their written rationales emphasize similar HEART dimensions. This pattern suggests an emerging convergence in the criteria used to assess supportive quality. By placing humans and models on equal footing, HEART reframes supportive dialogue as a distinct capability axis, separable from general reasoning or linguistic fluency. It provides a unified empirical foundation for understanding where model-generated support aligns with human social judgment, where it diverges, and how affective conversational competence scales with model size.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）评估体系中一个关键但被忽视的空白：如何系统性地评估和比较LLM与人类在**情感支持对话**这一复杂人际沟通任务上的能力。研究背景是，尽管LLM在推理、规划等认知任务上进步显著，但现实世界的高风险互动（如医疗、咨询）不仅要求信息准确，更要求回应能体现情感支持、情绪协调和关系适配，这对建立信任和改善结果至关重要。然而，现有基准测试主要集中于分类、摘要等事实性或认知性任务，缺乏对对话中人际维度的评估。现有方法的不足在于：1）传统NLP数据集（如EmpatheticDialogues）多关注离散的情感标签预测或词汇层面的温暖度，无法衡量对话是否随着时间推移适应说话者的情感需求；2）标准自动指标（如BLEU）完全无法捕捉一次交流是否让人感到被认可、被理解或被有效引导；3）缺乏一个将人类和模型置于完全同等对话任务中进行直接、多维度比较的统一框架。因此，本文要解决的核心问题是：**如何构建一个公平、统一、基于人际沟通科学的基准，以直接比较人类和LLM在多轮情感支持对话（包括对抗性或脆弱情境）中的表现，从而深入理解LLM在提供社会性对齐的情感支持方面，何处接近、何处落后于人类，以及这种能力如何随模型规模变化。** 为此，论文提出了HEART基准，通过结合多轮复杂对话、引入对抗性情感变体，并采用基于人类盲评和LLM作为裁判的混合评估方法，从五个科学维度系统评估支持性互动的质量。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 情感识别与共情建模研究**：早期自然语言处理研究集中于单轮对话的情感分类，使用了如EmpatheticDialogues、EmotionLines等数据集。这些工作主要关注词汇层面的情感，但可能鼓励模式匹配而非上下文敏感推理。近期研究开始评估大语言模型的共情能力，但通常缺乏多轮互动或对情感抵触用户的考量。

**2. 支持性对话与治疗策略研究**：以情感支持为中心的对话数据集，如ESConv和CounselChat，旨在建模反思性倾听、情感确认和应对策略的运用。基于策略的提示框架（如Chain-of-Empathy）和冲突模拟系统（如Rehearsal）试图构建治疗性微观技能。然而，其评估通常较为粗略（如分类器分数、词汇代理指标），难以在相同的对话约束下直接比较模型与人类的表现。

**3. 大语言模型情感与社会推理评估研究**：近期工作表明，大语言模型在推断人类情感方面表现出一定能力。基于对齐研究和“LLM即评委”方法的工作（如MT-Bench）证明结构化评估标准可以近似人类专家评价，但这些基准主要关注通用帮助性和推理能力，而非人际互动的细微差别。其他基准（如MultiChallenge、SENSE-7）强调多轮评估和个性化，但未系统性地测量情感协调、关系修复或情感抵触。

**4. 对话自然度与人机对话研究**：对话分析文献将话轮转换、微观时间协调、修复序列和互动对齐视为自然对话的标志。在人机交互领域，对话智能体通常在自然度、流畅度和拟人性方面接受评估。语音相关基准（如CAVA）表明，即使是几秒钟的延迟也会损害感知自然度，这激励了超越纯文本环境的情感推理评估。

**5. 健康与安全关键情境下的情感推理研究**：临床沟通研究强调共情和关系性沟通对改善健康结果的重要性，并关注边界设定、道德敏感性和风险意识指导。这些考虑为本文的“任务遵循”和“协调”维度提供了依据。

**本文与这些工作的关系与区别**：HEART基准整合并扩展了上述研究方向。其核心创新在于：**（i）** 首次将人类与大语言模型置于相同的、多轮且情感复杂的对话条件下进行直接比较；**（ii）** 依据人际沟通科学，通过五个经过验证的维度（人类对齐、共情反应、协调、共鸣、任务遵循）系统评估情感推理；**（iii）** 纳入了包含情感抵触的对抗性案例；**（iv）** 联合分析人类和LLM评委，以揭示社会判断标准上的对齐与差距。这使得HEART能够为理解模型生成的支持在何处符合或偏离人类的社会判断提供一个统一的实证基础。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为HEART的统一评估框架来解决如何系统比较人类与大型语言模型在情感支持对话中能力的问题。其核心方法是设计一个多维度、标准化的评估体系，并采用人类评估与模型评估相结合的双轨制进行直接比较。

整体框架基于人际沟通科学，定义了五个评估维度：人类一致性（H）、共情反应性（E）、协调性（A）、共鸣感（R）和任务遵循性（T）。在具体实施中，对于每一段给定的多轮情感支持对话历史，研究者会同时收集一个人类回应和一个模型回应，并将其匿名配对（标记为A/B）。评估过程的关键设计是“盲评”：人类评审员和作为评审员的LLM评估集合（LLM-as-judge）在不知道回应来源的情况下，对这两个回应的整体共情质量进行强制偏好选择，并标注其偏好强度。此外，评审员还可以选择性地指出哪个回应在特定的HEART维度上更具优势。

主要模块包括：1）标准化的对话情境与回应收集模块，确保人类与模型面对完全相同的上下文；2）双轨评估模块，整合了人类主观判断和自动化模型评估；3）基于维度的详细评估准则，为判断提供结构化依据。

创新点在于：首先，这是首个将人类与LLM置于完全平等条件下进行直接比较的框架，将情感支持对话能力视为独立于通用推理或语言流畅性的评估轴线。其次，它创新性地结合了人类盲评与LLM-as-judge评估，并发现两者在约80%的配对比较中意见一致，且其书面理由都强调相似的HEART维度，这表明在支持性对话质量的评估标准上出现了人机收敛。最后，该框架不仅揭示了前沿模型在部分维度（如感知共情和一致性）上接近或超越人类平均水平，也精准定位了人类在适应性重构、点明紧张情绪和细微语气转换等方面仍保持的优势。

### Q4: 论文做了哪些实验？

论文构建了HEART基准测试，通过大规模的双盲人工评估和LLM-as-judge评估，在相同的多轮情感支持对话上直接比较人类和多种大语言模型的性能。

**实验设置与数据集**：研究构建了一个包含300个对话历史的数据集，其中280个为常规对话，20个为对抗性对话，涵盖了寻求支持者犹豫不决、学业压力、育儿疲惫等多种高情境。每个对话历史由3名独立的人类参与者（共12人池）和来自5个模型家族的16个大语言模型分别生成回复，共得到900个完整对话。评估采用成对比较方式，每个回复对（包括模型vs.模型和模型vs.人类）由15名独立的人工标注者进行评判，总计进行了42,000次成对比较。人工标注者未被告知HEART评分标准，仅被要求选择哪个回复感觉更具支持性并说明理由。同时，使用LLM评委（GPT、Claude、Gemini）基于HEART五维标准进行结构化评估。

**评估方法与对比基准**：核心评估框架是新颖的HEART五维评分标准，包括：人类对齐性、共情响应性、情感协调性、共鸣性和任务遵循性。评估通过成对比较进行，胜者通过Bradley-Terry模型聚合成Elo风格评分，从而生成模型排行榜。主要对比对象是人类回复与不同LLM的回复，以及不同LLM之间的表现。

**主要结果与关键指标**：
1.  **人类与模型评估者的一致性**：人工评估者与模型评估者在成对比较中的平均一致率达到78.7%，接近于人工评估者之间79.5%的一致性。在双方达成一致的案例中，其理由所关注的主题有68%的重叠。
2.  **模型与人类回复的对比**：在所有人类与模型的正面比较中，人工评估者选择模型回复的比例为46.8%，选择人类回复的比例为35.8%（17.4%为平局）。当由其他LLM评判时，模型回复在所有HEART维度上优于人类回复的比例为53.3%。
3.  **模型性能趋势**：多个前沿模型（如GPT-5、GPT-o3、Claude 4.5 Sonnet、Gemini 2.5 Pro）在感知共情和一致性上接近或超过了人类平均水平。然而，人类在适应性重构、点名紧张情绪和细微语气转换方面（尤其在对抗性对话轮次中）仍保持优势。
4.  **性能与延迟的关系**：HEART的Elo评分通常随响应延迟（以首词时间TTFT为代理指标）的对数增加而提高（斯皮尔曼ρ=0.53）。但研究也发现，经过领域特定优化的模型（如Hippocratic AI的Polaris 4.0）能在亚500毫秒的低延迟下取得与高延迟大模型相当的Elo高分（1604.0），展示了实时语音代理的可行性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度进一步探索。首先，HEART基准尚未明确衡量“共情包容”能力，即处理强烈情绪、设定边界并保持参与的能力，未来可设计相应维度以评估模型在对抗性情境下的深度互动。其次，当前评估侧重于表面共情（如语言流畅性），而人类在情境判断、适应性重构和细微语调转换上的优势提示，需开发更能反映支持实际效能的纵向指标，如关联用户长期心理状态变化。此外，人类与模型评估者间约20%的分歧集中在模糊、混合情绪等复杂场景，未来可引入跨文化、高模糊性对话数据，训练模型提升解释准确性和边界校准能力。最后，为避免模型过度优化为“统一温和”的回应，需探索多目标训练框架，平衡语言亲和力与实质性支持行动，推动共情AI与人类优势互补而非替代。

### Q6: 总结一下论文的主要内容

该论文提出了HEART基准框架，首次在相同的多轮情感支持对话场景中直接比较人类与大型语言模型的表现。核心问题是评估双方在人际沟通技能上的差异，包括情感解读、语调调整及应对对抗性对话等能力。方法上，研究者针对每个对话历史，配对人类与模型回复，通过盲审人类评分员和LLM-as-judge评估器，依据人际沟通科学制定的五个维度（人类对齐、共情反应、协调性、共鸣度和任务遵循性）进行系统评估。

主要结论显示，前沿模型在感知共情和一致性方面接近或超越人类平均水平，但人类在适应性重构、矛盾指认及细微语调转换方面仍具优势，尤其在对抗性对话回合中。人类与LLM评判者在约80%的配对比较中偏好一致，且书面评价理由均聚焦于HEART维度，表明双方在支持性对话质量的评估标准上呈现趋同。论文的意义在于将情感支持对话重新定义为独立于通用推理或语言流畅性的能力维度，为理解模型生成支持与人类社交判断的异同提供了统一实证基础，并揭示了情感对话能力随模型规模扩展的变化规律。
