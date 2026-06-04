---
title: "TIDE: Proactive Multi-Problem Discovery via Template-Guided Iteration"
authors:
  - "Soyeong Jeong"
  - "Jinheon Baek"
  - "Minki Kang"
  - "Sung Ju Hwang"
date: "2026-06-03"
arxiv_id: "2606.04743"
arxiv_url: "https://arxiv.org/abs/2606.04743"
pdf_url: "https://arxiv.org/pdf/2606.04743v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent 问题发现"
  - "模板引导迭代"
  - "多问题发现"
  - "工具使用Agent"
  - "代码Agent"
  - "隐式问题发现"
  - "迭代式Agent"
  - "上下文推理"
relevance_score: 9.5
---

# TIDE: Proactive Multi-Problem Discovery via Template-Guided Iteration

## 原始摘要

Agents are widely deployed as assistants over documents, tools, and code. However, they typically act only on explicit user requests, which surface only the problems the user has noticed, while many other important problems coexist, hidden in plain sight, within the broader user context, with their total number unknown in advance. We frame this as the task of discovering multiple hidden problems from context, in which coexisting problems should be uncovered, grounded in supporting evidence, and paired with concrete actions. To this end, we introduce TIDE, a template-guided iterative framework with two complementary mechanisms. Specifically, motivated by the observation that single-pass prediction anchors on the most salient cases and yields generic claims, we propose iterative discovery, which surfaces a small batch of candidates per round while conditioning on what has already been found, so subsequent rounds extend coverage; and thought templates, reusable schemas distilled from previously solved cases that specify what contextual signals to attend to and how to connect them, anchoring each prediction in a recognizable problem class. We validate TIDE on two realistic settings, personal workspaces and software repositories, across four model backbones, showing substantial gains over single-shot and parallel multi-agent baselines on task coverage, identification, and resolution.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI代理（agent）在数字工作环境（如个人工作空间、软件仓库）中仅能被动响应用户显式请求的问题。研究背景是，尽管大语言模型代理能力日益增强，但它们本质上仍是**反应式**的——只有在用户明确提出问题后才会行动。然而，实际工作流中，大量关键问题（如未记录的预算审批、数据冲突的报告、已无人参加的重复会议）早已“隐性地”存在于用户的文档、邮件、日历等上下文中，用户自身甚至尚未察觉，且共存问题的总数未知。

现有方法的不足在于：1）传统反应式代理完全依赖用户识别问题，忽略了用户未发现的隐患；2）现有的主动代理研究侧重于预测单一意图或决定何时干预，但未能处理真实工作流中**多个问题共存**、**相互竞争注意力**、且**数量未知**的复杂场景；3）单次预测容易锚定最显著的问题，生成泛泛的结论，而忽略那些不显著但同样重要的隐藏问题。

本文的核心任务是将主动辅助重新定义为**从上下文中发现多个隐藏问题**，要求系统不仅能全面覆盖所有共存问题，还能为每个问题提供确凿证据和具体可执行的解决方案。为此，作者提出了TIDE框架（模板引导的迭代发现与解决），通过**迭代发现**机制（逐轮小批量生成新候选，并基于已发现问题进行条件化，以扩展覆盖范围）和**思维模板**机制（从历史案例中提取可复用的模式，指引模型关注特定上下文信号，增强预测的精准性），从而在覆盖率和任务解决精度上超越单次和并行多代理基线。

### Q2: 有哪些相关研究？

基于提供的论文和相关工作，主要有以下几类相关研究：

1. **任务导向型LLM Agent**：这类研究（如各类系统与基准）主要关注Agent在文档理解、工具使用、软件工程等环境中遵循用户指令执行既定任务。本文与之本质区别在于，传统工作假设任务已通过用户请求、问题描述等方式明确给出，Agent只需执行；而本文针对的是无明确请求、需要从上下文中主动发现多个共存问题的逆向场景。

2. **主动式Agent**：旨在预测用户需求并主动发起协助。相关工作通过澄清问题、利用用户信号等方式实现单次局部主动干预。本文区别在于，这些工作仍以用户查询为交互锚点，每次仅解决一个特定问题；本文则研究如何联合发现、验证并解决多个共存问题，而非针对单点需求。

3. **LLM推理模板**：相关方法（如Buffer-of-Thoughts、分层模板路径、图式抽象等）将可复用的推理模式外部化为模板，用于辅助解决已给定的问题。本文创新性地将模板重新定义为“发现模式”，即指定关注哪些上下文信号及如何连接以推断未陈述的问题，并迭代应用以覆盖多个共存问题，而非仅用于优化单一解决方案。

### Q3: 论文如何解决这个问题？

TIDE通过两个互补机制解决多问题发现难题：迭代发现和思维模板。整体框架基于一个形式化任务定义，目标是从文档集合D中预测隐藏问题集P^*，每个预测为三元组(b, D̂, a)，包含问题描述、证据和解决方案。

核心方法包括两大模块。第一，思维模板模块：从已解决案例中提取可复用的发现模式，每个模板包含名称、模式描述和证据流，形成结构化知识库。模板构建时，对每个训练案例⟨D_train, p_train, r_train⟩，利用LLM提炼实例无关的通用模式，生成结构化的模板t_i = (name_i, pattern_i, evidence flow_i)。例如工作区场景中的"冲突权威阻碍截止日期签核"模板，指定了发现冲突文档、确认差异、关联截止日期等证据线索。推理时，模板库作为先验知识，将预测锚定在可识别的问题类别，避免从零推断导致的泛化。

第二，迭代发现模块：解决单次预测中显著问题掩盖次要问题的缺陷。系统在多个轮次中逐步发现新问题，每轮生成不超过k个新候选预测，并显式条件于已有发现状态P̂^(t-1)。形式化为ΔP̂^(t) = LLM(D, T, P̂^(t-1), k)，更新状态P̂^(t) = P̂^(t-1) ∪ ΔP̂^(t)。当某轮无新发现或达到最大轮数T时终止。这种策略迫使模型在每轮关注未被覆盖的区域，逐步扩展问题覆盖范围。

关键创新点在于：将问题发现视为迭代过程而非单次推理，利用模板库提供可重用的证据模式先验，以及将识别、证据检索和解决方案生成整合在每个预测三元组中。这种设计同时提升了覆盖率和每项预测的准确性。

### Q4: 论文做了哪些实验？

论文在两个现实场景中进行了实验：个人工作空间（30个实例，每个含4-6个问题、88-113个候选工件）和软件仓库（20个实例，来自11个项目，每个含2-41个问题、6-646个候选函数）。对比方法包括：单次预测的Single-Agent、并行多智能体的Multi-Agent，以及提出的TIDE（迭代发现+思考模板）。使用GPT-5 mini、Gemini 3.5 Flash、Claude Sonnet 4.5和Qwen 3.6 Flash四种长上下文LLM作为骨干模型。评估采用检索、识别和解决三个组件的覆盖率（Cov.）和F1分数。

主要结果：TIDE在所有设置和骨干模型上均显著优于基线。例如，在GPT骨干下，TIDE在工作空间任务上检索Cov./F1为69.06/70.46（单智能体仅47.60/54.32），仓库任务上为16.82/18.61（单智能体8.66/10.34）。多智能体基线表现不佳，即使将预算增至10次调用仍低于TIDE的2次调用。消融实验表明：迭代发现主要提升覆盖率，思考模板主要提升精确率（图5）。使用少样本示例替代模板会显著降低性能（仓库检索Cov.从16.82降至10.40）。模板可在不同LLM间迁移（GPT与Gemini交叉使用表现相当），且模板池越大性能越好。定性分析进一步展示了TIDE在发现多函数耦合问题和跨文档证据整合上的优势。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在模板库的静态性和迭代策略的优化空间。首先，模板目前依赖预先求解的案例库且推理时固定不变，虽然已在多个骨干模型上验证有效性，但无法动态适应新问题模式。未来可探索在线学习机制，让Agent通过交互不断更新模板库，或利用大模型自动生成合成案例来扩充覆盖范围。其次，迭代发现虽在有限预算下优于多智能体基线，但其预算分配策略仍较朴素——当前均匀地每轮探索固定数量候选项。一个改进方向是引入自适应预算控制，根据已发现问题的置信度和新颖性动态调整后续轮次的搜索深度，例如对低置信度区域增加采样。此外，将模板引导与强化学习结合，使Agent学会主动识别“尚未覆盖的问题类型”，可能进一步提升多问题发现的系统性。这些方向能增强TIDE在开放、动态环境中的鲁棒性和可扩展性。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为TIDE的新框架，旨在解决AI助手仅响应明确用户请求而忽略上下文中隐含的多个问题这一挑战。该方法将问题定义为一个从上下文中发现多个隐藏问题的任务，要求系统不仅识别问题，还需提供证据并给出具体行动。TIDE采用两种互补机制：一是迭代发现，每轮仅生成少量候选问题，并基于已发现问题的信息调整后续轮次，以逐步扩大覆盖范围；二是思维模板，从已解决问题的案例中提炼可复用的模式，指导模型关注关键上下文信号并建立连接。在个人工作空间和软件仓库两个场景的实验表明，TIDE在任务覆盖率、识别准确率和解决效果上均显著优于单次预测和多智能体等基线方法。其主要贡献在于将主动辅助重新定义为多步骤发现过程，使AI能主动揭示用户可能未想到的问题，提升了系统的实用价值。
