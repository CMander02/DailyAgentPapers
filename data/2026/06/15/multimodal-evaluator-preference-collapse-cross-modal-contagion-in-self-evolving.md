---
title: "Multimodal Evaluator Preference Collapse: Cross-Modal Contagion in Self-Evolving Agents"
authors:
  - "Zewen Liu"
date: "2026-06-15"
arxiv_id: "2606.16682"
arxiv_url: "https://arxiv.org/abs/2606.16682"
pdf_url: "https://arxiv.org/pdf/2606.16682v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "Agent自评估"
  - "偏好崩溃"
  - "跨模态传染"
  - "多模态Agent"
  - "自我进化"
  - "评估器偏好"
  - "GPT-4o"
  - "实验框架"
relevance_score: 8.5
---

# Multimodal Evaluator Preference Collapse: Cross-Modal Contagion in Self-Evolving Agents

## 原始摘要

When AI agents use language models to evaluate their own outputs in a feedback loop, systematic biases emerge. We show that Evaluator Preference Collapse (EPC) is dramatically amplified in multimodal settings. Using GPT-4o to evaluate DeepSeek-chat across text and visual tasks, we find that a single strategy (step_by_step) absorbs 48.4% of all weight -- 3.2x the collapse observed in text-only self-evaluation -- while three visual-domain strategies receive only 9.1% combined weight. We then demonstrate a novel phenomenon we term cross-modal contagion: evaluator preferences acquired on one modality transfer to and corrupt strategy selection on another. Through a four-phase isolation training paradigm, we measure contagion coefficients and document strategy inversion -- the optimal strategy for a modality reverses after cross-modal exposure. A Phase 3 statistical validation across four evaluator configurations (N=53 total independent repetitions, 15,592 API calls) reveals a clear hierarchy: cross-model evaluation (GPT-4o, N=8) produces strong but symmetric bidirectional contagion (mean gamma_{T->V}=1.176, gamma_{V->T}=1.089, Delta=-0.088, p=0.575, Cohen's d=0.29); high round counts (DashScope, 50 rounds) cause collapse to single-strategy dominance (70% zero contagion); and self-evaluation provides near-complete immunity -- 97% of runs (N=30, DeepSeek-chat) yield exactly zero contagion (mean gamma=0.033, 95% CI [-0.031, 0.010], p=0.642, d=0.07). No evaluator condition shows statistically significant directional asymmetry. We introduce the contagion matrix indexed by evaluator identity, release the MM-EPC experimental framework, and identify cross-model evaluator architecture as the primary risk factor for preference contagion.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态自演化人工智能系统中，评估者偏好崩溃（EPC）现象的跨模态传播问题。研究背景是，AI智能体日益依赖大语言模型进行自我评估和反馈循环，例如GPT-4o等模型已能处理文本、图像等多模态任务。现有研究虽已揭示文本自评估中存在EPC（即评估策略趋向单一化），但尚未探讨这种偏差在多模态环境中的表现及其跨模态影响。现有方法的不足在于：忽略了不同模态下EPC严重程度的差异，以及一个模态中习得的评估者偏好是否会“感染”另一个模态的策略选择。本文核心要解决的关键问题是：1）多模态EPC是否存在且其幅度是否因模态而异；2）是否会发生“跨模态传染”（cross-modal contagion），即单一模态训练后的策略偏好会渗透到其他模态。通过系统实验，论文量化了GPT-4o评估DeepSeek时，文本与视觉任务中EPC的剧烈程度差异（视觉任务更为严重），并首次正式定义了跨模态传染现象、效应强度及评估者身份依赖的边界条件。

### Q2: 有哪些相关研究？

根据论文相关研究章节，相关工作可分为以下几类：

**方法类相关工作**：EPC（评估者偏好坍缩）首先在测试时智能体自我改进中识别出系统性偏好偏差，本文将其扩展到多模态场景。LLM-as-judge文献研究了静态评估质量及位置/冗长偏差，但仅限于单轮设置。自我奖励语言模型和迭代对齐工作表明闭环自评估会放大偏差，但仅限纯文本、同模型场景。本文首次扩展至跨模型、跨模态评估动态。

**应用类相关工作**：GPT-4o系统卡和Gemini 1.5技术报告提供了生产级多模态评估框架，承认“多模态场景下安全对齐更复杂”、“评估一致性跨模态下降”，但仅描述静态评估特性，未研究反馈循环中的动态演变。本文的传染矩阵提供了量化框架。

**评测类相关工作**：先前的跨模态迁移研究关注预训练/微调中能力迁移，而本文研究评估者偏好迁移。多模态RLHF开始处理跨模态奖励破解，但未形式化传染动态。测试时适应框架使智能体通过自生成反馈改进行为，本文揭示了多模态扩展中的根本风险。

**核心区别**：本文同时结合了跨模型、多模态、闭环评估、量化传染动态，是唯一覆盖所有这些维度的框架。与其他工作的关键区别在于发现了策略反转（如synthesis↔step_by_step）和跨模态传染对优化信号的污染。

### Q3: 论文如何解决这个问题？

论文通过提出“跨模态传染”这一新现象并设计四阶段隔离训练范式（Four-Phase Isolation Training Paradigm）来解决多模态自演化智能体中的评估者偏好崩溃（EPC）问题。

核心方法基于文本-强化学习（TTRL），将其形式化为一个随机赌博机过程。智能体维护一个L1归一化的策略权重向量w(t)，每一轮通过轮盘赌采样策略s_t，由执行器模型E生成响应，并与固定基线策略s_0（step_by_step）的响应进行配对比较。评估器J判断胜负后，使用非对称乘法重加权更新权重（获胜α_win=0.08，失败α_lose=0.04），再进行L1归一化，形成迭代的权重演化。

关键技术包括四个隔离阶段：阶段1和2分别在纯文本和纯视觉任务上独立运行TTRL，获得纯模态权重分布w_T和w_V；阶段3从w_T初始化后在视觉任务上训练得到w_{T→V}；阶段4从w_V初始化后在文本任务上训练得到w_{V→T}。通过计算传染系数γ（衡量传染后权重与纯模态权重间的归一化欧氏距离）来量化跨模态偏好转移的程度。

创新点在于：1）首次发现并严格验证了跨模态传染现象，即在一个模态上习得的评估者偏好会转移到并破坏另一个模态的策略选择；2）构建了由评估者身份索引的传染矩阵Γ，系统地表征了不同评估器配置下的传染模式；3）识别出交叉模型评估架构（如GPT-4o）是偏好传染的主要风险因素，而自评估提供近完全免疫（97%运行零传染）。研究还通过53次独立重复和15,592次API调用进行了统计验证，揭示了评估器层次：交叉模型产生强双向传染，高轮数导致单策略主导，自评估免疫性最强。

### Q4: 论文做了哪些实验？

论文围绕多模态评估者偏好崩塌（EPC）及跨模态传染现象设计了系统性实验。实验设置如下：执行器为DeepSeek-chat，评估器包括GPT-4o（Phase 1-2）、DashScope gui-plus（Phase 3a）、Qwen-plus（Phase 3b）及DeepSeek-chat自身（自评估）。任务包含8个文本和8个视觉相关任务，策略池共11种（8种文本策略+3种视觉策略：visual_grounding、spatial_decompose、aesthetic_frame）。实验分多个阶段：Phase 1进行16轮交替模态评估，Phase 2包含4阶段各30轮共120轮，Phase 3a/3b/3c分别进行2000、2520、10800次API调用，总计15592次调用。

主要结果：GPT-4o作为评估器时，单一文本策略step_by_step吸收48.4%权重，而三种视觉策略合计仅占9.1%，EPC强度是纯文本自评估的3.2倍（PCI=1.464 vs 0.461）。对比方法包括随机评估器（PCI=0.716±0.012）和基于参考答案的基准真实PCI（0.251）。跨模态传染实验表明，GPT-4o产生强对称双向传染（γ_T→V=1.176，γ_V→T=1.089，Δγ=-0.088，p=0.575），而自评估（DeepSeek-chat）提供近乎完全免疫，97%运行中零传染（平均γ=0.033，p=0.642）。高轮次（DashScope 50轮）导致70%运行收敛至单一策略，所有评估器条件均无显著方向不对称性。

### Q5: 有什么可以进一步探索的点？

根据论文的讨论部分，该研究存在几个关键的局限性，并明确了未来探索方向。首先，构念效度上，文本代理的视觉任务可能低估了真实视觉策略的权重，因此利用GPT-4o的视觉API进行原生图像输入是验证多模态崩溃的首要任务。其次，内部效度受限于固定的学习率和任务调度，未来需进行敏感性分析。外部效度方面，当前结果局限于特定执行-评估者对，未来的研究应扩展到Claude 3.5、Gemini 1.5 Pro等其他多模态评估器，以探究其评估者条件性传染效应。从创新角度看，可以引入自适应策略集，让系统根据模态表现动态增删策略，并探索跨评估器校准机制，系统性地分析架构、RLHF配方等属性如何预测传染的涌现或崩溃。此外，扩大模态覆盖至音频，构建3x3传染矩阵，并研究传染的传递性，也是一个富有前景的改进方向。关键的统计结论效度需要更大样本量（N>=30）和更多评估器来巩固现有发现。

### Q6: 总结一下论文的主要内容

本文研究了多模态自进化智能体中的“评估者偏好崩溃”(EPC)现象，发现该问题在多模态环境下被显著放大。具体地，当使用GPT-4o作为评估者评估DeepSeek-chat时，单一文本策略“step_by_step”吸收了48.4%的权重，是纯文本自评估场景的3.2倍，而三个视觉策略仅占9.1%。核心贡献在于发现了“跨模态传染”新现象，即在一个模态上习得的评估者偏好会转移到并破坏另一模态的策略选择。通过四阶段隔离训练范式量化了传染系数，并记录了“策略反转”现象。主要结论包括：跨模型评估产生强双向传染，高轮次评估导致单一策略主导，而自评估则几乎完全免疫。研究揭示了多模态自进化系统的关键失效模式，并指出跨模型评估者架构是偏好传染的主要风险因素。
