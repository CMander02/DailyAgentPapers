---
title: "Entropy Guided Diversification and Preference Elicitation in Agentic Recommendation Systems"
authors:
  - "Dat Tran"
  - "Yongce Li"
  - "Hannah Clay"
  - "Negin Golrezaei"
  - "Sajjad Beygi"
  - "Amin Saberi"
date: "2026-03-12"
arxiv_id: "2603.11399"
arxiv_url: "https://arxiv.org/abs/2603.11399"
pdf_url: "https://arxiv.org/pdf/2603.11399v1"
categories:
  - "cs.AI"
tags:
  - "推荐系统"
  - "交互式系统"
  - "不确定性推理"
  - "偏好获取"
  - "熵"
  - "决策支持"
  - "用户模拟"
relevance_score: 7.5
---

# Entropy Guided Diversification and Preference Elicitation in Agentic Recommendation Systems

## 原始摘要

Users on e-commerce platforms can be uncertain about their preferences early in their search. Queries to recommendation systems are frequently ambiguous, incomplete, or weakly specified. Agentic systems are expected to proactively reason, ask clarifying questions, and act on the user's behalf, which makes handling such ambiguity increasingly important. In existing platforms, ambiguity led to excessive interactions and question fatigue or overconfident recommendations prematurely collapsing the search space. We present an Interactive Decision Support System (IDSS) that addresses ambiguous user queries using entropy as a unifying signal. IDSS maintains a dynamically filtered candidate product set and quantifies uncertainty over item attributes using entropy. This uncertainty guides adaptive preference elicitation by selecting follow-up questions that maximize expected information gain. When preferences remain incomplete, IDSS explicitly incorporates residual uncertainty into downstream recommendations through uncertainty-aware ranking and entropy-based diversification, rather than forcing premature resolution. We evaluate IDSS using review-driven simulated users grounded in real user reviews, enabling a controlled study of diverse shopping behaviors. Our evaluation measures both interaction efficiency and recommendation quality. Results show that entropy-guided elicitation reduces unnecessary follow-up questions, while uncertainty-aware ranking and presentation yield more informative, diverse, and transparent recommendation sets under ambiguous intent. These findings demonstrate that entropy-guided reasoning provides an effective foundation for agentic recommendation systems operating under uncertainty.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决电子商务推荐系统中用户意图模糊性带来的挑战。研究背景在于，用户在搜索初期往往对自己的偏好不确定，查询可能模糊、不完整或定义不清，而现有的智能推荐系统需要主动推理、提问并代表用户行动，因此处理这种模糊性变得至关重要。现有方法存在明显不足：传统的交互式推荐系统要么通过过多追问导致用户疲劳，要么过早自信地缩小搜索范围，排除可行选项；同时，许多系统将偏好收集、排序和结果呈现作为独立组件处理，无法在推荐流程中一致地推理不确定性。

本文的核心问题是：如何设计一个统一的交互式决策支持系统，在用户偏好不完整的情况下，有效管理不确定性，平衡交互效率与推荐质量。为此，论文提出了IDSS系统，以信息熵作为统一信号来量化不确定性，并贯穿于偏好收集、排序和呈现全流程。具体而言，系统利用熵指导自适应提问，选择信息增益最大的问题；当偏好仍不完整时，通过不确定性感知排序和基于熵的多样化推荐，避免过早强制解决模糊性，从而提供更信息丰富、多样且透明的推荐结果。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类三个方向。

在方法类研究中，对话推荐系统（CRS）长期关注通过多轮交互进行偏好获取与自适应推荐。随着大语言模型（LLM）的兴起，CRS越来越多地被构建为智能体工作流，例如InteRecAgent将LLM与推荐模型作为工具集成，RecMind则研究具有显式规划的LLM驱动自主推荐智能体。本文与这类工作的关系在于同样探索智能体范式，但区别在于提出了一个可控、可审计的管道，将用户意图转化为明确的数据库约束，并结合嵌入排序与重排序模块。另一方法线涉及可扩展检索/排序与多样性感知推荐，本文在此基础上将多样性作为明确的设计目标，通过结构化过滤与语义排序的结合，在重排序阶段权衡匹配质量与属性覆盖。

在应用类研究中，本文与利用嵌入进行候选生成以及使用LLM作为灵活重排器的研究一脉相承，但重点在于处理用户意图模糊性这一特定挑战。

在评测类研究中，本文借鉴了使用模拟（如RecSim、KuaiSim、SUBER平台及基于LLM的用户模拟器）来评估交互策略的方法。本文的关系在于同样采用基于评论的模拟用户进行受控实验，区别在于评测重点聚焦于交互效率（如减少不必要追问）与推荐质量（在模糊意图下产生信息丰富且多样的推荐集）之间的权衡，从而验证其熵引导方法的有效性。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为IDSS（交互式决策支持系统）的端到端对话推荐框架来解决用户查询模糊、不完整或弱指定所导致的交互效率低下和推荐质量不佳的问题。其核心方法是**以信息熵作为统一信号**，动态量化候选产品集在属性维度上的不确定性，并以此指导三个关键环节：自适应偏好获取、不确定性感知的排序，以及支持探索的多样化呈现。

整体框架是一个**多轮次循环**，每轮包含：1）**语义解析**：利用LLM将用户自由输入解析为结构化状态（硬约束、软偏好、厌恶特征及耐心程度）；2）**候选集检索**：根据当前约束从数据库中过滤出候选产品集；3）**熵引导的提问决策**：计算未指定属性的归一化熵，选择熵值最高（即不确定性最大）且超过阈值（τ_H=0.3）的属性作为下一个提问维度，由LLM生成自然语言问题；若熵值过低或用户表现出不耐烦，则直接进入推荐阶段；4）**双策略排序**：根据偏好不确定性程度，采用两种互补排序策略之一——对于不确定性较低的情况，使用**嵌入相似性与最大边际相关性（MMR）** 来平衡相关性与多样性；对于不确定性较高的情况，采用**覆盖-风险优化排序**，通过贪心算法最大化对用户喜好特征的覆盖，同时最小化触及其厌恶特征的风险；5）**熵引导的多样化呈现**：从用户未指定的属性中选出熵最高的维度作为组织维度，将排序后的候选集按该维度值分组，并以网格形式呈现，使不同选项间的权衡一目了然。

创新点主要体现在：1）**以熵为驱动的统一机制**，将不确定性量化并贯穿于提问、排序和呈现全流程，避免了过早压缩搜索空间或过度提问；2）**数据驱动的自适应提问策略**，基于实时候选集分布选择最具信息增益的问题，而非固定脚本；3）**不确定性感知的双模式排序**，根据不确定性水平灵活切换策略，显式处理未指定属性带来的风险；4）**探索式网格呈现**，通过沿高熵维度分组推荐，主动暴露权衡选项，支持用户通过比较发现偏好。这些设计共同使系统能在模糊意图下，以更少的交互生成更信息丰富、多样且透明的推荐结果。

### Q4: 论文做了哪些实验？

论文通过基于评论的模拟用户框架评估了所提出的交互式决策支持系统（IDSS）。实验设置包括：从真实汽车评论出发，通过重写生成多样化的模拟用户画像，并利用LLM提取结构化偏好信息，形成包含初始查询和潜在行为属性的“用户回合”。系统与模拟用户进行多轮交互，由自动评判器（LLM）对跟进问题和最终推荐列表进行评估。

数据集/基准测试基于150个模拟用户画像，并区分了两种查询场景：“短查询”（少于10词，代表模糊需求）和“长查询”（少于120词，包含详细偏好）。评估指标涵盖对话效率（跟进问题的相关性和新颖性）以及推荐质量（满意度、精确度@k、nDCG@k）和多样性（列表内多样性ILD）。

对比方法包括两种排名方法：嵌入相似性（ES）和覆盖风险（CR），并进行了消融实验，以分析移除基于最大边际相关（MMR）的多样化策略和基于熵的跟进问题选择（EntropyQ）的影响。

主要结果如下：在短查询设置下，ES（完整配置）的Prec@9达到0.903，nDCG@9为0.941，ILD为0.779。移除MMR导致ILD大幅下降（例如ES从0.779降至0.279），但有时会略微提升相关性指标（如长查询下ES的Prec@9从0.744升至0.837），这体现了相关性与多样性的权衡。移除EntropyQ会降低推荐质量，尤其在长查询下更明显（如CR的Prec@9从0.801降至0.753）。在问题质量方面，EntropyQ显著提升了短查询下问题的新颖性（Newness从0.602提升至0.946），而相关性在所有设置中均保持高位（0.967-1.00）。此外，一项小型用户调查（n=12）也支持了实验结果，表明进行跟进询问能提升推荐匹配度，且多样化呈现使结果更易于比较。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于评估方法依赖于基于评论的LLM模拟用户，虽然实现了可控和可扩展的实验，但可能无法完全捕捉真实用户的复杂多变性和策略性行为。未来研究应通过人类主体实验来验证IDSS，重点关注用户满意度、交互效率和系统透明度的感知。此外，实验集中于汽车领域，尽管所提出的熵引导启发和不确定性感知排序机制是领域无关的，但扩展到其他决策支持场景可能需要重新定义属性和多样化目标。

结合个人见解，可能的改进方向包括：第一，开发更精细的用户意图动态建模方法，使系统能实时调整相关性与多样性的平衡策略，而不仅仅是基于静态熵值。第二，探索多模态交互方式，例如结合图像、语音或自然语言对话，以更自然地收集用户偏好。第三，引入个性化熵阈值机制，根据用户的历史行为或交互风格自适应调整提问频率和推荐多样性，避免“一刀切”策略。第四，考虑将社会信任机制或群体偏好信息纳入不确定性量化，以增强推荐的可解释性和说服力。这些方向有望进一步提升智能推荐系统在模糊查询场景下的适应性和用户体验。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为IDSS的交互式决策支持系统，旨在解决电商推荐系统中用户查询模糊、偏好不确定的问题。核心贡献在于将熵作为统一信号，系统化地量化和管理不确定性，从而提升智能体推荐系统的适应性和效率。

研究问题定义为处理用户初始查询的模糊性，避免现有系统因过度交互导致疲劳或过早缩小搜索范围。方法上，IDSS动态维护候选产品集，利用熵度量属性不确定性，并以此指导自适应偏好获取：选择能最大化预期信息增益的后续问题。当偏好仍不完整时，系统通过不确定性感知排序和基于熵的多样化，将残余不确定性明确纳入下游推荐，而非强制过早解决。

主要结论显示，基于熵的引导减少了不必要的后续提问，同时在模糊意图下，不确定性感知的排序与呈现能产生更具信息性、多样化和透明的推荐集合。这证明了熵引导推理为不确定环境下的智能体推荐系统提供了有效基础，并强调了联合设计提问与排序策略的重要性。
