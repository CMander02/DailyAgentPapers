---
title: "WorldReasoner: Evaluating Whether Language Model Agents Forecast Events with Valid Reasoning"
authors:
  - "Yizhou Chi"
  - "Eric Chamoun"
  - "Zifeng Ding"
  - "Andreas Vlachos"
date: "2026-06-10"
arxiv_id: "2606.11816"
arxiv_url: "https://arxiv.org/abs/2606.11816"
pdf_url: "https://arxiv.org/pdf/2606.11816v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "事件预测"
  - "推理评估"
  - "因果图"
  - "时间有效性"
  - "基准测试"
  - "信息检索"
relevance_score: 9.5
---

# WorldReasoner: Evaluating Whether Language Model Agents Forecast Events with Valid Reasoning

## 原始摘要

Forecasting real-world events requires language-model agents to reason under uncertainty from incomplete, time-bounded information. Yet evaluating whether agents genuinely forecast requires more than final-answer accuracy: a model may be correct by recalling memorized training facts, citing fabricated evidence, or producing an unsupported causal story. We present WorldReasoner, an evaluation framework for temporally valid event forecasting. Each task gives an agent a resolved forecasting question, a simulated forecast date, and access only to evidence available before that date; after resolution, the framework scores the submitted probability, cited evidence, and optional causal event graph. WorldReasoner reports three complementary axes: outcome quality against resolved answers, evidence quality over cited sources, and reasoning quality against post-resolution hindsight graphs. The benchmark is built by an agentic construction pipeline that generates forecasting questions, collects time-stamped evidence, and builds hindsight reference graphs at scale, yielding 345 resolved tasks derived from 14,141 articles with graphs covering 8,087 extracted events. Across six controlled agent settings, temporally valid retrieval is the strongest driver of outcome accuracy; causal graph construction improves key-event recovery; and correct graph-enabled forecasts are more strongly grounded in key events and relevant sources, yet agents still struggle to convert grounded evidence into calibrated probabilities.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前语言模型智能体在事件预测任务中存在的评估缺陷。具体而言，现有的评估主要关注最终答案的准确性，但忽略了一个关键问题：模型可能在预测正确时是基于记忆中的训练事实、编造的虚假证据，或是不合理的因果叙事，而非真正的有效推理。因此，论文提出WorldReasoner评估框架，旨在系统性地评估智能体是否在时间有效约束下进行有效推理。该框架的核心是评估三个互补维度：1) 结果质量（预测概率与真实结果的匹配度）；2) 证据质量（引用来源的可信度和时效性）；以及3) 推理质量（生成的因果事件图与事后反思图的匹配度）。通过构建包含345个已解析任务、14141篇时间戳文章和8087个提取事件的基准，揭示了时间有效检索是提高结果准确性的最强驱动力，因果图构建有助于关键事件恢复，但智能体在将基于证据的信息转化为校准概率方面仍存在困难。

### Q2: 有哪些相关研究？

相关研究可分为几个方向：首先是事件预测领域的基准测试，如ForecastBench、Autocast、TempLAMA等，它们关注预测准确性但缺乏对推理过程和证据来源的深度评估。其次，在智能体评估方面，有WebArena、SWE-bench、GAIA等工作，它们评估智能体在复杂环境中的任务完成能力，但未专门针对预测任务中的时间有效性和推理有效性。第三，推理评估相关研究包括EntailmentBank和WorldTree，它们关注推理解释的可靠性，但聚焦于静态知识而非动态事件预测。此外，因果推理在NLP中的应用，如CausalNet和Causal-Bench，提供了因果图构建的方法，但未将其整合到智能体预测评估中。本文的创新在于将时间约束、证据验证、因果推理三个维度统一到一个评估框架中，特别强调预测时只能使用截止日期前的信息这一时间有效性原则，并通过自动构建流水线大规模生成带有时间戳证据和事后反思图的评估任务。

### Q3: 论文如何解决这个问题？

论文提出WorldReasoner评估框架，通过三个核心组件解决评估问题。首先，任务构建方面，设计了一个智能体驱动的流水线：1) 从维基百科等来源获取时间敏感事件（如2024年英国大选），自动生成预测问题；2) 收集具有明确时间戳的新闻文章作为证据来源，确保所有证据在预测截止日期前可用；3) 构建事后反思因果图，基于事件发生后的完整信息提取关键事件及其因果关系，作为推理质量的黄金标准。其次，评估方法采用三维度评分：1) 结果质量（Outcome Quality）通过Brier分数等指标比较预测概率与真实结果；2) 证据质量（Evidence Quality）评估引用来源的相关性、时效性和可信度；3) 推理质量（Reasoning Quality）通过构建的因果事件图与反思图的匹配度，评估模型是否抓住了关键因果链。最后，在实验设置中，设计了六种受控智能体配置（包括有无时间有效检索、有无因果图构建），对GPT-4、Claude等模型进行系统比较。结果表明，时间有效检索是预测准确性的最强决定因素，因果图构建有助于识别关键事件，但将证据转化为准确概率预测仍是挑战。

### Q4: 论文做了哪些实验？

论文构建了包含345个已解析预测任务的基准，源自14141篇时间戳文章，提取了8087个事件并构建了相应的因果图。实验采用六种受控智能体配置，覆盖有无时间有效检索（Temporal RAG vs. Non-temporal RAG）和有无因果图构建（Graph vs. No Graph）的组合，在GPT-4、Claude 3.5 Sonnet等模型上进行评估。主要实验结果包括：1) 时间有效检索是结果准确性的最强驱动因素，使Brier分数平均降低0.15以上；2) 因果图构建有助于关键事件恢复（Key Event Recall提升约20%），但转化为概率校准的改善有限；3) 正确使用因果图的预测更强烈地基于关键事件和相关来源，但智能体在将证据转换为校准概率方面表现不足，校准误差仍较高。此外，进行了消融实验验证各个组件的重要性，以及不同模型对时间信息敏感度的比较分析。实验还评估了不同检索策略（如基于时间戳的过滤与基于语义相似度的检索）对预测质量的影响。

### Q5: 有什么可以进一步探索的点？

基于论文的发现，存在多个值得进一步探索的方向：1) 概率校准的改进：当前智能体在将基于证据的信息转化为校准概率方面存在困难，未来可研究专门的校准训练方法或后处理技术。2) 因果推理的深度：当前因果图构建主要识别共现事件，未来可探索更复杂的因果发现方法，如干预推理或反事实推理。3) 时间推理的精细化：如何更准确地理解复杂时间关系（如相对时间、时间跨度、截止日期等）对推理的影响。4) 多智能体协作：可探索多个智能体协作预测，利用不同模型在证据检索和因果推理上的互补优势。5) 动态任务更新：如何自动更新基准任务以涵盖最新事件，避免数据时效性问题。6) 细粒度评估维度：进一步分解推理质量评估，区分因果链的完整性和因果关系的正确性。7) 模型内部的推理过程可解释性：结合链式思考或思维树等方法，探索推理过程中的中间步骤与最终预测质量的关系。

### Q6: 总结一下论文的主要内容

论文WorldReasoner提出了一个评估语言模型智能体事件预测推理有效性的全面框架。核心创新在于从结果质量、证据质量和推理质量三个维度系统评估预测过程，特别强调时间有效性原则——即模型只能使用预测截止日期前的信息。论文构建了包含345个已解析任务的大型基准，通过自动流水线生成带有时间戳证据和事后因果图的评估任务。实验在六种受控智能体配置下进行，揭示了关键发现：时间有效检索是提高预测准确性的最强驱动力，因果图构建有助于关键事件恢复，但智能体在将基于证据的推理转换为校准概率方面仍有显著不足。这项工作的意义在于为评估智能体的真正推理能力提供了更全面的标准，推动了事件预测领域从仅关注最终答案向关注推理过程的转变。
