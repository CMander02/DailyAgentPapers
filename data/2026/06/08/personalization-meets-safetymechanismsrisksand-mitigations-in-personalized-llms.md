---
title: "Personalization Meets Safety:Mechanisms,Risks,and Mitigations in Personalized LLMs"
authors:
  - "Yanyan Luo"
  - "Xue Han"
  - "Ruiqiao Bai"
  - "Xin Huang"
  - "Yitong Wang"
  - "Qian Hu"
  - "Qing Wang"
  - "Chunxu Zhao"
  - "Jie Liu"
  - "Cong Geng"
  - "Lehao Xing"
  - "Pengwei Hu"
  - "Junlan Feng"
date: "2026-06-08"
arxiv_id: "2606.09038"
arxiv_url: "https://arxiv.org/abs/2606.09038"
pdf_url: "https://arxiv.org/pdf/2606.09038v1"
categories:
  - "cs.AI"
tags:
  - "LLM安全"
  - "个性化对齐"
  - "多智能体安全"
  - "评测基准"
  - "Agent框架安全"
relevance_score: 8.5
---

# Personalization Meets Safety:Mechanisms,Risks,and Mitigations in Personalized LLMs

## 原始摘要

Large Language Models (LLMs) have enabled increasingly personalized interactions by adapting to users' preferences, contexts, and long-term histories. However, the mechanisms that enable personalization also expand the safety landscape in ways not systematically addressed by existing literature. Existing reviews typically focus either on personalization or safety, leaving their intersection largely unexplored. We present the first comprehensive, safety-aware review of personalized LLMs. We organize personalization along three dimensions-user representation, personalization paradigm, and evaluation-and introduce a unified taxonomy of safety risks. At the representation level, we analyze risks arising from diverse user representations. Across mainstream personalization paradigms, we delineate vulnerabilities inherent to prompting, retrieval augmentation, parameter fine-tuning, reinforcement learning, Mixture-of-Experts (MoE), pruning, agent frameworks, and multimodal personalization, and synthesize mitigation strategies across the model lifecycle. Beyond these fine-grained risks, we characterize paradigm-agnostic safety risks arising from personalized adaptation. We further summarize personalized datasets and evaluation methodologies. Through a case study of OpenClaw, we analyze deployment trends in personalized agent ecosystems. Our analysis reveals three structural inadequacies in existing research: safety is evaluated as user-invariant rather than relational, personalization techniques are analyzed in isolation rather than in composition, and evaluation frameworks cannot capture emergent long-term risks. By jointly examining personalized representations, personalization paradigms, safety risks, defenses, and evaluation methods, we provide a unified framework for developing safe personalized LLMs and highlight key directions for future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决个性化大语言模型（LLMs）在集成用户偏好、上下文和长期历史时，其安全风险未被系统性研究的问题。当前研究的不足主要体现在：（1）现有文献通常将个性化与安全分开讨论，忽略了二者交叉地带产生的结构性风险；（2）安全评估是用户无关的，无法适应不同用户背景、脆弱性水平或场景风险，导致同一响应可能对某个用户合适而对另一用户有害；（3）个性化技术如微调、检索增强、长期记忆、偏好对齐、混合专家模型等各自引入了新的攻击面，如安全对齐退化、敏感数据泄露、记忆注入攻击、谄媚倾向放大、侧信道暴露及后门嵌入等。这些风险在通用部署中并不显著，却因个性化适配而激增。因此，本文核心目标是提供一个以安全为导向的综述，系统梳理个性化LLM的用户表示、个性化范式及评估三个维度，统一分类安全风险，分析各粒度的脆弱点和全生命周期的缓解策略，并指出当前研究在关系性安全评估、技术组合评估及长期风险捕获上的结构性缺陷，为未来构建安全可信的个性化LLM提供统一框架。

### Q2: 有哪些相关研究？

以下是与本文相关的主要研究工作及其关系与区别：

**方法类：** 多篇关于LLM个性化（如A Survey of Personalized Large Language Models、Personalized Generation in Large Model Era、Personalization of Large Language Models）以及多模态个性化（Personalized Multimodal Large Language Models）的综述，均聚焦于个性化技术（如提示工程、检索增强、微调、MoE等），但未系统分析安全风险。本文则首次将安全视角贯穿全个性化栈。

**安全类：** Large Language Model Safety: A Holistic Survey和On Large Language Models Safety, Security, and Privacy等综述全面探讨了LLM安全，但将安全视为全局属性，未区分个性化带来的细粒度风险。本文揭示了不同表示层（如用户画像、历史行为）和个性化范式（如检索操纵、后门攻击）特有的风险。

**对齐与个性化交叠类：** 关于个性化对齐的综述（如A Survey on Personalized Alignment、Two Tales of Persona）虽涉及部分安全（如偏见对齐），但未深入分析范式级脆弱性。本文提出了跨范式的安全风险（如个人信息持久化、敏感属性推断），并系统整理了全生命周期的防御与评估方法。

### Q3: 论文如何解决这个问题？

该论文通过构建一个统一的安全感知分类框架来解决个性化大语言模型的安全问题。整体框架包含四个主要维度：用户表征、个性化范式、安全风险与缓解策略、以及评估方法。

在用户表征层面，论文系统分析了不同表征形式（如语义、行为、时间层级）带来的安全风险，包括过度曝光、敏感属性推断和信息持久性。在个性化范式层面，论文细化了提示工程、检索增强、参数微调、强化学习、混合专家模型、剪枝、智能体框架和多模态个性化等主要范式中固有的脆弱性，例如检索操纵、后门攻击和不安全决策。关键技术创新在于将安全风险与具体个性化机制进行精确映射，而非笼统讨论。

论文的创新点主要体现在三方面：第一，首次提出“细粒度安全”概念，区分了范式特定风险和范式无关风险（如个性化适应本身带来的用户隐私泄露）；第二，揭示了现有研究的三个结构性缺陷——安全评估未考虑用户关系维度、个性化技术被孤立分析而非组合评估、评估框架无法捕获长期涌现性风险；第三，通过OpenClaw案例研究，展示了真实个性化智能体生态系统的部署趋势与安全挑战。整个框架将安全纳入个性化全生命周期考量，从表征、实现、交互到评估，形成闭环分析。

### Q4: 论文做了哪些实验？

该论文未进行传统意义上的实验，而是作为一篇综述性研究，通过对现有文献的系统性分析来构建统一的安全感知个性化LLM分类体系。论文的“实验”体现为对现有研究的全面梳理和分类整理：它按用户表示、个性化范式和评估三个维度组织个性化LLM，并提出统一的安全风险分类法。在数据集/基准测试方面，论文仅总结和归纳了现有个性化数据集与评估方法，未使用特定基准或指标进行新实验。对比方法部分，论文通过与表1中列出的八篇现有综述（如《A Survey of Personalized Large Language Models》《Large Language Model Safety》等）进行对比，突出自身差异：这些综述要么仅聚焦个性化，要么仅关注安全性，且安全性常被视为全局属性，而本文则首次跨全个性化栈（从底层用户表示到高层系统部署）系统覆盖细粒度与范式无关的安全风险及其缓解策略。论文主要结果是：揭示了现有研究的三项结构性不足——安全性仅被视为与用户无关的全局属性而非关系属性；个性化技术孤立分析而非组合分析；评估框架无法捕捉长期涌现风险。此外，论文通过OpenClaw案例分析了实际部署趋势，但未提供量化性能指标。

### Q5: 有什么可以进一步探索的点？

论文的一个核心局限在于对“安全性”的理解过于静态和孤立。现有研究往往将安全视为用户不变的单点属性（如“内容有害”），缺乏对“关系性安全”的考量，即安全风险会因用户与模型之间长期互动的动态关系而演化。例如，一个最初无害的个性化提示，在多次迭代后可能被恶意用户利用来诱使模型泄露隐私。未来研究应开发能够量化这种动态风险的评估指标。

其次，现有工作大多孤立分析单一技术（如微调或提示），忽略了组合效应。实际应用中，个性化系统会同时采用多种技术（如RAG+微调+MoE），其安全漏洞并非简单叠加，可能产生新的攻击面。需要构建组合式威胁模型与联合防御框架。

第三，评估体系严重缺失对长期风险的捕捉。例如模型因持续学习用户偏好而逐渐“越界”或对用户产生不安全的迎合。未来应发展持续评估框架（如在线测试、模拟用户画像的长周期交互），并引入逆向强化学习或因果推断来分析模型行为随时间的变化。

最后，从方法论上可改进方向是：将安全作为个性化目标函数的一个正交约束，而非事后补丁。例如在强化学习训练中设计“安全偏好”与“个性化偏好”的对抗博弈，或利用红蓝对抗自动生成跨范式的攻击样本，以构建更鲁棒的防御基线。

### Q6: 总结一下论文的主要内容

这篇论文首次系统地审视了大语言模型（LLM）个性化与安全性的交叉领域，指出当前研究将安全视为用户无关的，而实际上个性化系统的安全性是用户相关的。论文从三个维度构建分析框架：用户表征（如个人资料、偏好）、个性化范式（如提示、检索增强、微调）以及评估。核心贡献在于统一分类了不同层面的安全风险，包括：微调可能破坏安全对齐、RAG导致隐私泄露、长期记忆易受注入攻击、强化学习会助长谄媚行为、MoE路由暴露侧信道等。此外，还总结了范式无关的普遍风险，并提出了贯穿模型生命周期的缓解策略。通过案例分析，论文揭示了现有研究的三点结构性不足：安全评估的非关系性、技术分析的孤立性、评估框架无法捕捉长期风险。最终，该综述为构建安全、可靠、可部署的个性化LLM系统提供了统一框架和未来研究方向。
