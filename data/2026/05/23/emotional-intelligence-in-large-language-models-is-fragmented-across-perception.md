---
title: "Emotional intelligence in large language models is fragmented across perception, cognition, and interaction"
authors:
  - "Minghao Lv"
  - "Lu Chen"
  - "Enchang Zhang"
  - "Anji Zhou"
  - "Xiaoran Xue"
  - "Hanyi Zhang"
  - "Fenghua Tang"
  - "Zhuo Rachel Han"
  - "Mengyue Wu"
date: "2026-05-23"
arxiv_id: "2605.24686"
arxiv_url: "https://arxiv.org/abs/2605.24686"
pdf_url: "https://arxiv.org/pdf/2605.24686v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent评估"
  - "情感智能"
  - "对齐安全"
  - "RLHF"
  - "基准测试"
  - "社交Agent"
relevance_score: 7.5
---

# Emotional intelligence in large language models is fragmented across perception, cognition, and interaction

## 原始摘要

As large language models (LLMs) are increasingly integrated into emotionally sensitive domains, the structural integrity of their emotional intelligence (EI) becomes a critical frontier for safety and alignment. Current benchmarks often conflate superficial politeness with deep affective reasoning, failing to distinguish between perceptual accuracy and interactive efficacy. Here, we introduce FACET (Functional Affective Competence and Empathy Test), a psychometrically grounded framework comprising 480 expert-crafted items. Unlike previous metrics, FACET is theoretically anchored in the Mayer-Salovey-Caruso four-branch ability model, operationalizing EI through perception, facilitation, understanding, and management of emotions. Through an evaluation of nine frontier models (including GPT-5, Claude-Sonnet-4), we demonstrate that emotional intelligence is not a monolithic capability but is fragmented across cognitive and interactive dimensions. While frontier models demonstrate robust proficiency in objective emotion recognition and social reasoning, this does not consistently translate to interactive success. We categorize these discrepancies into three distinct performance profiles: cognitive-dominant, interactive-dominant, and context-dependent. These typologies indicate that emotional skills do not scale uniformly with general intelligence or model size; rather, they are shaped by specific alignment paradigms. Notably, we identify hidden emotion recognition as a universal performance bottleneck across all architectures. Our results suggest that current RLHF processes may optimize for "stochastic empathy", a statistical mimicry of emotional syntax, at the expense of integrated affective reasoning. These findings challenge the assumption of linear emotional scaling and provide a rigorous roadmap for developing socially aware agents capable of genuine clinical resonance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前大语言模型（LLM）情感智能评估中的结构性缺失问题。现有方法往往将情感智能视为单一的整体指标，主要依赖主观的用户偏好排名或简化的情绪分类任务。这些基准仅能捕捉表面的“礼貌”行为（通常是RLHF的副产品），无法区分表面模仿与深层情感推理，更无法有效衡量感知准确性与交互效能之间的差异。论文的核心问题是：**LLM是否具备类似于人类四分支能力模型（感知、促进、理解、管理情绪）的整合性情感推理架构，抑或只是表现出一种“随机共情”式的统计模仿？** 为此，作者提出了FACET基准，这是一个基于心理学Mayer-Salovey-Caruso能力模型、包含480个专家设计项目的评估框架。通过对9个前沿模型（如GPT-5、Claude-Sonnet-4）的评估，论文发现LLM的情感智能在认知和交互维度上存在显著的功能分离：擅长客观情绪感知的模型往往无法在交互中保持共情连贯性。这种解耦表明，情感能力并非随通用智能或模型规模线性扩展，而是受特定对齐范式塑造。论文还揭示了“隐藏情绪识别”是所有架构的通用性能瓶颈，并指出当前RLHF过程可能以牺牲整合性情感推理为代价，优化了“随机共情”。

### Q2: 有哪些相关研究？

本文的相关研究可分为三类。**测评类**：现有基准通常将情绪智力视为单一指标，依赖主观偏好排序或简单情绪分类任务（如情感计算、共情对话系统），仅捕获表层“礼貌性”，未能区分表面模仿与深层情感推理。本文提出的FACET框架基于Mayer-Salovey-Caruso四分支能力模型，通过480个专家设计的任务从感知、认知、交互三维度系统评估，弥补了该缺陷。**方法类**：相关RLHF优化过程可能导致“随机共情”（统计性模仿情感语法），而本文发现情感能力并非随模型规模或通用智能线性增长，而是由特定对齐范式塑造，揭示了隐藏情绪识别是普遍瓶颈。**应用类**：尽管已有结构化情感支持系统，但本文首次证明前沿模型（如GPT-5、Claude-Sonnet-4）在客观情绪识别与社会推理上的强表现，与交互成功之间并无稳定对应关系，且情感能力呈现“碎片化”特征。本文通过双语言（中英）文化代理设计，进一步指出情绪智能并非通用结构能力，而是受训练数据文化偏见影响的语言特定产物。

### Q3: 论文如何解决这个问题？

该论文通过引入FACET（功能性情感能力与共情测试）框架来解决情感智能的碎片化问题。FACET基于Mayer-Salovey-Caruso四分支能力模型，将情感智能分解为感知、促进、理解和管理四个维度，共包含480个专家设计的测试项。

核心方法采用双元评估体系：客观感知和认知任务使用标准准确率评分（0-100），主观交互维度则采用Elo评级系统，通过成对比较捕捉潜在表现层级，避免传统Likert量表的评估者漂移问题。整体框架涵盖六项客观维度（显性情绪识别、隐藏情绪识别、情绪预测、社交适宜性、危机识别）和五项主观交互维度（情绪深化、共情理解等），并支持中英双语测试。

关键技术创新包括：1）识别出隐藏情绪识别是所有架构的普遍性能瓶颈，揭示了模型在解读隐性情感信号上的系统缺陷；2）发现危机识别是区分模型认知可靠性的主要差异维度，高表现模型在此维度展现显著分化；3）通过主观-客观表现差距分析，证明了情感智能在感知、认知和交互维度间的非一致性，并归纳出三种性能画像：认知主导型、交互主导型和情境依赖型。研究还发现当前的RLHF过程可能优化出"随机共情"——对情感句法的统计模仿，而非真正的整合性情感推理。

### Q4: 论文做了哪些实验？

实验包括客观感知/认知任务和主观交互任务两类。客观任务使用FACET框架的六个维度：显性情绪识别、隐藏情绪识别、情绪预测、社会适当性、危机识别和客观总准确性，以准确率（0-100%）作为指标。主观交互任务评估五个维度：情绪深化、共情理解、表达自然度等，采用Elo评分系统进行相对偏好建模。数据集涵盖中文和英文双语语料，共480个专家设计的题目。对比方法评估了9个前沿模型，包括GPT-5、Gemini-2.5-Pro、Claude-Sonnet-4、Grok-4等全球模型，以及Qwen3-235B、DeepSeek-R1、GLM-4.5、Kimi-k2、Doubao-seed-1.6等中文模型。主要结果：1）隐藏情绪识别是普遍性能瓶颈，最佳模型在中文任务中从约67%下降至48-57%，英文任务均低于38.33%；2）危机识别是认知可靠性的主要区分因素，GPT-5（中文72.78%，英文64.44%）和Gemini（中文77.22%，英文72.22%）显著优于其他模型；3）共情理解和表达自然度驱动主观体验差距，中文条件下Doubao共情理解Elo评分（1390.54）远超GPT-5（830.97）；4）存在显著的主客观分离现象，如Kimi-k2客观准确率仅51.78%但主观交互排名第二，GPT-5客观最优但主观交互排名末位。

### Q5: 有什么可以进一步探索的点？

基于FACET框架揭示的情感智能碎片化现象，未来研究可从三个方向展开：首先，当前RLHF优化出的“随机共情”需被更精准的社交语用对齐取代，可通过引入对抗性交互训练和动态奖励塑造，迫使模型在对话中放弃模板化回应。其次，跨文化情感解码存在结构性瓶颈，尤其在高语境（中文）与低语境（英文）的隐性情绪识别上（如“克制抵抗”误判为“被动伤害”），需构建保留权力动态与面子协商机制的训练语料，而非仅依赖解构化文本。最后，危机识别维度存在保守性偏差，未来需从二元风险分类转向细粒度严重性评估，例如建立专家标注的分级基准，结合因果推理而非统计相关性来区分真实危机与矛盾信号。这些改进将推动情感智能从“知识匹配”转向“关系建构”。

### Q6: 总结一下论文的主要内容

本文介绍了一个名为FACET的心理测量学框架，用于评估大语言模型的情感智能。该框架基于Mayer-Salovey-Caruso四分支能力模型，通过480个专家设计的项目，从感知、认知和交互三个维度系统评估情感能力。研究对GPT-5、Claude-Sonnet-4等9个前沿模型进行了评估，发现情感智能并非单一能力，而是在认知和交互维度上呈现碎片化分布。模型虽然能准确识别情绪，却不总能转化为有效的交互表现。研究将模型分为三种类型：认知主导型、交互主导型和情境依赖型，表明情感技能与模型大小不成正比，而是受对齐范式影响，其中隐藏情绪识别是普遍存在的瓶颈。研究还指出当前的RLHF过程可能优化了"随机共情"而牺牲了整合性情感推理。这些发现挑战了情感能力线性增长的假设，为开发具有真实临床共鸣的社会感知型AI提供了路线图。
