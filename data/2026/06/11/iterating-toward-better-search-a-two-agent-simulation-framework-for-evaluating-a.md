---
title: "Iterating Toward Better Search: A Two-Agent Simulation Framework for Evaluating Agentic Search Architectures in E-Commerce"
authors:
  - "Jetlir Duraj"
  - "Jayanth Yetukuri"
  - "Shuang Zhou"
  - "Dhruv Varma"
  - "Rui Kong"
  - "Ishita Khan"
  - "Qunzhi Zhou"
date: "2026-06-11"
arxiv_id: "2606.12924"
arxiv_url: "https://arxiv.org/abs/2606.12924"
pdf_url: "https://arxiv.org/pdf/2606.12924v1"
categories:
  - "cs.AI"
tags:
  - "多智能体仿真"
  - "电商搜索Agent"
  - "Agent架构评估"
  - "记忆机制对比"
  - "LLM评判一致性"
  - "对话购物助手"
relevance_score: 8.5
---

# Iterating Toward Better Search: A Two-Agent Simulation Framework for Evaluating Agentic Search Architectures in E-Commerce

## 原始摘要

We present a modular two-agent simulation framework for evaluating conversational shopping assistant architectures. An independent buyer agent, configured with personas, missions, and patience levels, is paired with an interchangeable responder that integrates with a real e-commerce search API. Holding the buyer constant across experiments enables controlled comparison of responder designs on identical scenarios. Using 2011 conversations across 14 persona buckets, we establish four empirical findings. First, rolling-window memory outperforms intent-extraction memory on all quality metrics while being 35% faster per query. Second, illustrating rapid evidence-driven iteration, a systematic failure analysis of a responder version enables targeted fixes that reduce failure and near-failure rates by 62% across the full dataset. Third, swapping the responder LLM backbone from Gemini~2.5 to Llama~3.3~70B costs 0.16--0.45 points despite identical architecture. Finally, we document systematic philosophical disagreement between frontier LLM judges: Gemini rewards process correctness while Claude demands concrete outcomes, despite using the same evaluation prompt.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在电商领域构建和评估对话式购物助手时面临的系统迭代瓶颈问题。研究背景是，可靠的离线评估对于开发这类助手至关重要，但现有方法存在明显不足。传统的人工Beta测试虽然信号真实，但速度慢、无法复现相同场景、且有隐私限制；而单智能体生成方法（由一个模型同时生成买家和助手响应）虽然速度快，但生成的对话与真实用户行为系统性地偏离，比如提问过于正式、缺乏点击等操作行为，更关键的是，它无法用于测试助手侧（Responder）的特定架构差异。

本文的核心问题是：**如何构建一个低成本、可重复且能控制变量的评估框架，以科学地比较和迭代不同的对话购物助手架构？** 具体而言，现有方法无法将买家行为作为控制变量，也无法在相同场景下进行公正的AB测试。为此，论文提出了一个模块化的双智能体（Two-Agent）仿真框架，通过一个独立的、可配置的买家智能体与一个可替换的助手智能体进行交互，实现了对助手架构（如记忆策略、意图提取、响应生成）的受控比较和快速迭代，最终目标是提升助手在真实电商场景中的表现。

### Q2: 有哪些相关研究？

在相关工作中，本文主要涉及五类研究。首先是**行为真实性评估**，以往工作如通过预测与历史日志的匹配度来评估购物代理，优化目标是模仿而非系统有效性。本文则转向任务成功率，且每次运行动态生成买家行为，而非回放日志。其次是**生产监控**，现有方法通过融合人类反馈或使用模拟压力测试来优化已固定架构的运行，而本文作为研发实验室，在架构投入生产前测试其失败边界。第三是**个性化与满意度评估**，已有方法使用LLM代理评分聚合指标，本文则评估架构设计选择，并揭示评估器本身也是设计选择。第四是**对话代理记忆架构**，如Reflexion通过自反思改进性能、记忆压缩保持性能。本文实证发现简单滚动窗口记忆在电商对话中优于意图提取流水线。最后是**代理架构与工具使用**及**LLM作为评判者**，如ReAct、模型学习使用API等。本文对比两种后端架构在真实搜索API上的表现，并系统比较不同LLM评判者对同一对话的哲学分歧，证明评判者选择相当于质量准则选择。

### Q3: 论文如何解决这个问题？

该论文通过构建一个模块化的双智能体模拟框架来解决评估电商对话购物助手架构的问题。核心方法是设计一个可互换的买家智能体和响应者智能体，在受控实验中独立比较不同响应器设计。整体框架由编排器、买家智能体和响应器智能体三个主要组件构成。编排器负责管理对话循环，转发查询、记录对话统计信息直至会话终止。买家智能体是固定的Gemini 2.5 Pro推理模型，配有预设任务、人设和耐心等级，生成包含搜索、点击和加购三种动作的查询。响应器智能体则是可替换的组件，包含内存模块、查询理解分类器、重写器、实时搜索API和响应生成器。

论文比较了四种响应器架构，关键技术体现在内存设计和LLM后端替换上。Sys-A采用意图追踪内存，每次查询后额外进行一次LLM调用来提取结构化意图。Sys-B采用滚动窗口内存，当累积查询超过6个时仅调用一次LLM进行压缩摘要，避免了每查询的意图提取，速度比Sys-A快35%。Sys-B+在Sys-B基础上，通过对错误模式的系统性故障分析进行3项针对性修复，将失败和接近失败率降低了62%。Sys-C则保持与Sys-B相同的滚动窗口架构，但将LLM后端从Gemini 2.5替换为Llama 3.3 70B，导致质量分数下降0.16-0.45点。该框架的关键创新点在于：实现了智能体独立性设计，确保性能差异仅由响应器架构引起；并通过受控实验揭示了滚动窗口内存的效率优势、基于实证的迭代改进效果以及LLM评估者间的哲学分歧。

### Q4: 论文做了哪些实验？

论文主要进行了以下实验：基于2011条跨14个用户配置桶的购物对话数据集（按购物风格、耐心程度和任务数量划分），比较了两种会话购物助手架构。实验设置包括：固定买家代理（配置了不同人设和耐心等级），对比可互换的响应器系统。主要对比方法为Sys-A（意图提取记忆）与Sys-B（滚动窗口记忆），并在特定实验中对比了Sys-C（Llama 3.3 70B骨干模型）。实验使用了Gemini 3.1 Pro和Claude Opus 4.6两个前沿LLM评判器，从任务成功率、SRP相关性、CHAT帮助性和查询意图理解四个维度（1-5分）进行评估。主要结果：Sys-B在所有指标上优于Sys-A（提升0.01-0.10分），且查询速度加快35%。通过故障分析，Sys-B+版本使故障率降低62%，灾难性故障降低36%。Sys-C换用Llama模型后质量下降0.16-0.45分。关键发现：裁判模型间存在系统性哲学分歧，Gemini奖励过程正确性而Claude要求具体结果，两者评分差距（0.39-0.97分）远大于架构差异。

### Q5: 有什么可以进一步探索的点？

论文提出的两智能体仿真框架为电商搜索助手评估提供了可控环境，但存在明显局限：首先，仿真逼真度受限，当前买手智能体基于通用LLM生成对话，缺乏真实用户交互数据训练，导致查询模式（平均8词）和行动指令频率（45%）与真实购物行为存在偏差。未来可借鉴行为克隆或人类反馈强化学习（RLHF）方法，用真实用户日志微调买手模型。其次，系统性失败分析虽降低了62%失败率，但仅针对特定LLM版本，未探索架构与LLM的交叉效应——例如，更好的骨干模型（如GPT-4）可能弥补简单意图提取架构的不足。第三，评估体系存在根本矛盾：Gemini偏重过程正确性而Claude关注结果，这暗示需要设计对抗性评估焦耳斯特或人类标注基准来调和分歧。改进方向包括：（1）引入多轮协商机制让不同LLM评判者达成共识；（2）构建动态耐心建模，使买手能根据上下文调整容忍度；（3）探索混合记忆架构，结合滚动窗口与压缩记忆以平衡效率与上下文保留。

### Q6: 总结一下论文的主要内容

我们提出一个模块化双智能体仿真框架，用于评估对话式购物助手的架构。该框架将独立配置了角色、任务和耐心等级买家智能体，与集成真实电商搜索API的可互换响应者配对。通过保持买家不变，我们可在相同场景下对比不同响应者设计。基于2011次对话和14个角色组，我们建立了四个实证发现：第一，滚动窗口内存在质量和速度上均优于意图提取内存，且查询速度提升35%；第二，系统性故障分析能实现62%的故障与近故障率降低，展示了快速迭代的有效性；第三，将响应者LLM从Gemini 2.5换成Llama 3.3 70B导致0.16-0.45分的性能下降；第四，前沿LLM裁判存在根本性哲学分歧，Gemini更关注过程正确性，而Claude更看重具体成果，即便使用相同评估提示。该框架的核心贡献在于提供了可控、快速的电商助手架构评估方法，并揭示了LLM裁判选择本身即是一项重要的架构决策。
