---
title: "Modeling Distinct Human Interaction in Web Agents"
authors:
  - "Faria Huq"
  - "Zora Zhiruo Wang"
  - "Zhanqiu Guo"
  - "Venu Arvind Arangarajan"
  - "Tianyue Ou"
  - "Frank Xu"
  - "Shuyan Zhou"
  - "Graham Neubig"
  - "Jeffrey P. Bigham"
date: "2026-02-19"
arxiv_id: "2602.17588"
arxiv_url: "https://arxiv.org/abs/2602.17588"
pdf_url: "https://arxiv.org/pdf/2602.17588v2"
categories:
  - "cs.CL"
  - "cs.HC"
tags:
  - "Human-Agent Interaction"
  - "Web Agent"
  - "Agent Collaboration"
  - "Intervention Modeling"
  - "Agent Adaptation"
  - "Agent Evaluation"
relevance_score: 8.0
---

# Modeling Distinct Human Interaction in Web Agents

## 原始摘要

Despite rapid progress in autonomous web agents, human involvement remains essential for shaping preferences and correcting agent behavior as tasks unfold. However, current agentic systems lack a principled understanding of when and why humans intervene, often proceeding autonomously past critical decision points or requesting unnecessary confirmation. In this work, we introduce the task of modeling human intervention to support collaborative web task execution. We collect CowCorpus, a dataset of 400 real-user web navigation trajectories containing over 4,200 interleaved human and agent actions. We identify four distinct patterns of user interaction with agents -- hands-off supervision, hands-on oversight, collaborative task-solving, and full user takeover. Leveraging these insights, we train language models (LMs) to anticipate when users are likely to intervene based on their interaction styles, yielding a 61.4-63.4% improvement in intervention prediction accuracy over base LMs. Finally, we deploy these intervention-aware models in live web navigation agents and evaluate them in a user study, finding a 26.5% increase in user-rated agent usefulness. Together, our results show structured modeling of human intervention leads to more adaptive, collaborative agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前自主网页代理（web agents）在与人协作时，由于缺乏对人类干预行为的理解而导致协作效率低下的核心问题。研究背景是，尽管大语言模型（LLMs）的进步使得AI代理能够执行复杂的网页导航任务，但在实际应用中，人类的参与对于纠正代理的错误理解和调整其行为以符合用户偏好仍然至关重要。然而，现有方法存在明显不足：当前的代理系统普遍缺乏对人类“何时”以及“为何”进行干预的原则性理解。这导致代理要么在错误的假设下过度自主运行，错过了关键的决策点；要么在不恰当的时机频繁请求用户确认，造成不必要的干扰，反而增加了用户的监督负担。

本文要解决的核心问题，正是如何系统性地建模人类在任务执行过程中的干预行为，从而使代理能够主动预测用户可能的干预，并据此调整自身行为，实现更高效、自适应的人机协作。具体而言，论文引入了“建模人类干预”这一新任务，通过收集真实用户与代理协作的轨迹数据（CowCorpus），识别出四种不同的用户交互模式（如放手监督、动手监督等），并在此基础上训练语言模型来预测干预。最终目标是让代理的自主性与人类参与形成互补，仅在必要时请求用户输入，从而在保证可靠性的同时，显著降低用户的监督负担并提升协作体验。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：自主网络智能体和人机协作研究。

在**自主网络智能体**方面，相关工作包括Mind2Web、WebArena等基准测试，它们推动了智能体在真实多领域HTML环境中的任务执行。Claude、Operator等模型展现的“计算机使用”能力，以及WebCanvas、WebOlympus、OpenWebAgent、Taxy等插件式工具，进一步缩小了机器浏览与人类操作的差距。然而，这些工作通常**优先考虑自主性而非协作**，缺乏用户交互控制的机制。本文基于此插件范式，但将重点转向超越单一自主性的人机协作。

在**人机协作研究**方面，相关工作涵盖机器人、生产力工具和LLM协作等多个领域。Magentic-UI、Cocoa、CoGym、Collaborative STORM、A2C等框架通过引入实时网络环境中的协同规划与执行机制，推进了非轮流式交互协议的发展。在写作辅助领域，CoAuthor、PEER、VISAR等LLM协作系统取得了显著进展。早期的交互式系统如PUMICE和PLOW则展示了最终用户编程和演示的价值。此外，部分研究如TrustAgent、ToolEmu等主要关注安全性与可信度。与这些工作不同，本文**将焦点转向网络浏览协作中整体的沟通模式**，特别是对人类干预行为的结构化建模，以预测干预时机并提升代理的实用性和适应性。

### Q3: 论文如何解决这个问题？

论文通过构建一个能够预测人类干预时机和模式的模型来解决人机协作中代理行为与用户偏好不匹配的问题。其核心方法是基于收集的真实用户交互数据集CowCorpus，训练一个大型多模态模型（LMM）来学习人类在网页导航任务中的干预模式，并将该模型集成到网页代理中，实现自适应的协作。

**整体框架与架构设计**：研究将人机协作形式化为一个部分可观测马尔可夫决策过程（POMDP）。在每一步，系统接收一个包含当前网页截图和可访问性树的多模态观测，代理根据其策略提出一个建议动作。关键创新在于引入了一个二元干预变量，并训练一个预测模型 \( f_\theta \) 来估计用户在当前步骤干预的概率 \( p(y_t = 1 \mid o_t, \hat{a}_t, \tau_{t-1}) \)。模型架构上，它接收一个序列化的提示，包含历史轨迹、当前观测和代理建议动作的描述，经过监督微调（SFT）后，输出特定的token（如 `<ask_user>` 或 `<agent_continue>`）来决定是请求用户干预还是让代理继续执行。

**主要模块与关键技术**：
1.  **数据收集与模式识别**：构建了包含4200多个交错人机动作的CowCorpus数据集，并从中识别出四种不同的用户交互模式：放手监督、动手监督、协作任务解决和完全接管。这为建模提供了细粒度的基础。
2.  **干预预测模型**：采用了两阶段训练策略。首先，使用所有数据训练一个**通用的干预感知模型**，以捕捉常见的用户行为。其次，为了个性化，针对除“放手监督”（无干预）外的三种交互模式，分别使用对应轨迹子集微调出**风格条件模型**，使预测能适应用户的协作偏好。
3.  **评估指标**：除了步骤准确率和F1分数，论文创新性地提出了**完美时机分数（PTS）**，该指标不仅评估干预预测的正确性，还通过惩罚与真实干预时刻的时间距离偏差，来严格衡量预测时机的精准度。
4.  **系统集成与部署**：将训练好的干预感知模型集成到一个网页导航代理（作为Chrome扩展）中。该代理仅在模型预测用户干预可能性高时才主动请求确认，而非每一步都请求或完全自主，从而改变了交互范式。

**创新点**：
- **问题形式化**：首次将网页代理中的人类干预建模为一个时序二元分类任务，并置于POMDP框架下。
- **个性化建模**：超越了单一的通用模型，通过风格条件模型实现了对差异化用户协作风格的适应。
- **精准时机评估**：提出PTS指标，强调干预预测的“时机”与“是否”同等重要。
- **实证验证闭环**：通过用户研究验证，集成该模型的代理在用户评价的“有用性”上提升了26.5%，证明了该方法能有效提升协作体验和代理实用性。

### Q4: 论文做了哪些实验？

论文的实验主要分为两部分：建模人类干预预测和部署协作式网页智能体。

在建模实验中，**实验设置**基于自建的CowCorpus数据集，该数据集包含400条真实用户的网页导航轨迹和超过4200个人与智能体的交错动作。数据集按轨迹级别划分为训练集和测试集，干预步骤与非干预步骤的比例约为1:7。**数据集/基准测试**为Human Intervention Prediction任务，评估指标包括步骤准确率、干预/非干预的F1分数以及完美时机分数（PTS）。**对比方法**包括两个非学习基线（始终不干预、始终干预）、基于提示的闭源大模型（Claude 4 Sonnet、GPT-4o、Gemini 2.5 Pro）以及开源模型（Gemma 27B、Llava 8B）。**主要结果**显示，经过在CowCorpus上监督微调（SFT）的开源模型表现最佳。例如，微调后的Gemma 27B在PTS上达到0.303，优于所有闭源模型；其步骤准确率为85.3%，干预F1为0.302，非干预F1为0.918。相比之下，GPT-4o的PTS仅为0.147，且干预F1（0.198）远低于非干预F1（0.846），表明其过于保守。研究还训练了针对不同用户交互模式（如接管型、动手监督型、协作型）的风格条件模型，这些模型在对应集群的验证集上普遍表现更优。

在部署实验中，**实验设置**是将干预感知模型集成到网页导航智能体中，并作为Chrome扩展部署。**评估方法**是通过用户研究，邀请4名参与者使用该智能体完成标准任务和自由形式任务，并与他们之前使用基线智能体的体验进行对比。**主要结果**显示，用户在使用干预感知智能体后，在六项用户体验维度（如控制感、偏好对齐、任务效率等）的7点李克特量表评分平均提升了26.5%，表明建模人类干预能显著提高智能体的实用性和协作效果。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其数据集规模（400条轨迹）和交互模式的分类可能尚未覆盖所有真实场景的复杂性，特别是跨文化或跨任务类型的差异。未来研究可进一步探索动态交互模式的识别与适应，例如通过在线学习实时调整干预预测模型，而非依赖静态分类。此外，结合多模态信号（如用户眼动或语音语调）可能提升干预时机判断的准确性。从技术角度，可研究如何将干预预测与强化学习结合，使智能体不仅能预测干预，还能主动调整策略以减少不必要的用户介入。最后，扩展到更复杂的多步骤任务或多人协作场景，将有助于验证模型的泛化能力，推动智能体向更自然、高效的协作伙伴发展。

### Q6: 总结一下论文的主要内容

这篇论文研究了如何建模人类在网页导航任务中对AI智能体的干预行为，以构建更具协作性的智能体系统。当前系统缺乏对人类干预时机和原因的理解，导致智能体要么过度自主而犯错，要么不必要地频繁请求确认，增加了用户的监督负担。

论文的核心贡献包括：1) 定义了“建模人类干预”这一新任务，旨在支持协作式网页任务执行；2) 收集并发布了CowCorpus数据集，包含400条真实用户的网页导航轨迹，涵盖超过4200个人类与智能体的交错行动，并识别出四种用户交互模式（放手监督、动手监督、协作任务解决、完全接管）；3) 提出基于语言模型的方法，根据用户协作风格来预测其干预可能性，相比基础模型将干预预测准确率提升了61.4%-63.4%；4) 将干预感知模型部署到实时网页导航智能体中，用户研究表明其能将用户评价的智能体有用性提升26.5%。

主要结论是：人类的干预行为是一种结构化的信号，反映了不同的协作风格。通过有意识地建模人机交互模式，可以开发出更能适应人类偏好、减少不必要干扰、从而更有效和更具协作性的智能体。这项工作标志着从单纯优化智能体自主性，转向设计能动态适应人类协作风格的智能体。
