---
title: "PERMA: Benchmarking Personalized Memory Agents via Event-Driven Preference and Realistic Task Environments"
authors:
  - "Shuochen Liu"
  - "Junyi Zhu"
  - "Long Shu"
  - "Junda Lin"
  - "Yuhao Chen"
  - "Haotian Zhang"
  - "Chao Zhang"
  - "Derong Xu"
  - "Jia Li"
  - "Bo Tang"
  - "Zhiyu Li"
  - "Feiyu Xiong"
  - "Enhong Chen"
  - "Tong Xu"
date: "2026-03-24"
arxiv_id: "2603.23231"
arxiv_url: "https://arxiv.org/abs/2603.23231"
pdf_url: "https://arxiv.org/pdf/2603.23231v1"
github_url: "https://github.com/PolarisLiu1/PERMA"
categories:
  - "cs.AI"
tags:
  - "Agent记忆"
  - "个性化Agent"
  - "评测基准"
  - "长期记忆"
  - "用户偏好建模"
  - "事件驱动"
  - "交互评估"
relevance_score: 8.5
---

# PERMA: Benchmarking Personalized Memory Agents via Event-Driven Preference and Realistic Task Environments

## 原始摘要

Empowering large language models with long-term memory is crucial for building agents that adapt to users' evolving needs. However, prior evaluations typically interleave preference-related dialogues with irrelevant conversations, reducing the task to needle-in-a-haystack retrieval while ignoring relationships between events that drive the evolution of user preferences. Such settings overlook a fundamental characteristic of real-world personalization: preferences emerge gradually and accumulate across interactions within noisy contexts. To bridge this gap, we introduce PERMA, a benchmark designed to evaluate persona consistency over time beyond static preference recall. Additionally, we incorporate (1) text variability and (2) linguistic alignment to simulate erratic user inputs and individual idiolects in real-world data. PERMA consists of temporally ordered interaction events spanning multiple sessions and domains, with preference-related queries inserted over time. We design both multiple-choice and interactive tasks to probe the model's understanding of persona along the interaction timeline. Experiments demonstrate that by linking related interactions, advanced memory systems can extract more precise preferences and reduce token consumption, outperforming traditional semantic retrieval of raw dialogues. Nevertheless, they still struggle to maintain a coherent persona across temporal depth and cross-domain interference, highlighting the need for more robust personalized memory management in agents. Our code and data are open-sourced at https://github.com/PolarisLiu1/PERMA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何有效评估具备长期记忆能力的大型语言模型（LLM）智能体在真实、动态的个性化交互场景中的性能问题。研究背景是，随着LLM从静态知识访问转向能够持续交互的智能体，长期记忆成为维持跨交互一致用户表征的关键。现有基于检索增强生成（RAG）等方法虽提升了知识提取能力，但其评估范式存在严重不足：首先，它们通常将用户偏好预设为静态陈述，并在对话中与无关内容交织，将评估简化为“大海捞针”式的检索任务，忽略了偏好是在事件驱动的对话中逐渐显现和演化的本质；其次，现有评估将用户模型视为静态快照，忽视了跨会话的依赖关系，无法检验智能体在连续交互中进行推理和跨领域综合的能力；最后，评估多聚焦于最终LLM输出，混淆了记忆检索与生成过程，未能独立衡量底层记忆系统的质量、效率及其在交互场景中的效用。因此，本文的核心问题是构建一个更贴近现实的评估基准，以测试智能体如何从嘈杂、渐进的交互事件中推断和整合用户偏好，并长期维持一致、动态演化的“人物状态”，而不仅仅是进行静态偏好回忆。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：记忆评测、个性化代理评测以及记忆系统架构。

在**记忆评测**方面，早期工作如“大海捞针”式测试主要评估模型在长上下文中检索事实的能力。后续的LongMemEval等将评测扩展到超长多轮对话，关注跨会话记忆和问答，但仍侧重于历史信息的访问与推理，而非用户偏好的渐进推断与整合。

在**个性化代理评测**方面，研究从静态偏好条件生成（如PrefEval、PerLTQA）发展到多会话偏好保持（如PersonaMem系列）。这些工作揭示了LLMs在推断隐含偏好并保持一致性的困难，但其评测场景往往将偏好作为孤立信息从大量无关上下文中检索，或假设用户档案是固定的。最近的UserBench和PersonaLens引入了交互式环境，但未将用户档案视为动态演化的结构。KnowMe-Bench则侧重于长篇叙事中的动机推理，而非对话式助理的个性化交互评估。

在**记忆系统架构**方面，为应对长上下文建模的局限，检索增强生成（RAG）将记忆外部化存储，但通常将记忆视为静态文档，缺乏对用户状态时序演化的建模。近期研究如MemOS、Mem0等开始将记忆视为具有生命周期管理的结构化子系统，支持记忆的巩固、衰减和重组，实现了从存储中心到过程导向的转变。

本文提出的PERMA基准与上述工作的主要区别在于：它通过事件驱动的方法，关注偏好如何随时间在充满噪声的交互中逐步形成和演化，评测重点从单点偏好回忆转向跨域、跨时间的复合人格状态一致性维护。PERMA明确引入了上下文噪声、时序探测和交互式评估，以模拟真实世界中用户输入的波动性和人格的连贯性需求，从而超越了传统的对话检索或静态偏好识别任务。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为PERMA的基准测试框架来解决个性化记忆代理的评估问题，其核心方法是将个人偏好建模为随时间动态演化的过程，而非静态的偏好回忆。整体框架分为对话构建与评估两大模块。

在对话构建方面，PERMA采用事件驱动的方法重构对话历史。具体而言，它基于真实的用户画像（来自PRISM数据集）和领域特定的交互摘要，利用大型语言模型（如GPT-4o）作为高层规划器，生成结构化的交互时间线。该时间线将每个领域的交互分解为按时间顺序排列的事件序列，每个事件对应一个连贯的会话，并包含事件描述、交互目标和跨领域依赖关系。对话生成代理在用户画像、兴趣类别和先前对话历史的条件下，为每个时间线条目生成多轮对话，并记录会话中涌现或更新的偏好。最终，所有领域的时间线根据时间戳和显式依赖关系进行交织，形成一个全局时间线。

为了模拟真实世界交互的复杂性，PERMA引入了两个关键创新：一是注入文本变异性，基于常见的用户提示偏差来模拟不稳定的用户输入；二是进行语言风格对齐，使查询语言风格与真实数据保持一致，以反映个体特有的语言习惯。

在评估方面，PERMA设计了两种协议：一次性多项选择题探测和交互式评估。前者通过三个评估维度（如零样本偏好回忆）测量选择准确性；后者通过多轮对话，由用户模拟器评估任务完成度和偏好满意度，并提供纠正反馈。评估任务通过基于时间戳的策略插入全局时间线，并设置了三种类型的评估检查点：类型一（零记忆）任务置于时间线开端，作为非个性化控制；类型二任务置于相关领域事件结束后，评估整个轨迹的整合能力；类型三任务置于全局时间线末尾，跟随一系列无关领域的干扰会话，用于量化模型抗遗忘和抗上下文干扰的鲁棒性。通过比较类型二和类型三的性能差异，可以有效衡量代理在长时程中的记忆一致性。

PERMA的创新点在于超越了传统的“大海捞针”式语义检索评估，通过事件驱动的偏好演化建模、对真实噪声和语言风格的模拟，以及沿时间线深度的多检查点评估，系统性地测试代理在跨领域、长时程交互中维持一致用户画像的能力。实验表明，通过关联相关交互，先进记忆系统能提取更精确的偏好并减少令牌消耗，但在时间深度和跨领域干扰下保持连贯画像方面仍面临挑战，凸显了更鲁棒的个性化记忆管理的必要性。

### Q4: 论文做了哪些实验？

论文实验围绕PERMA基准展开，旨在评估个性化记忆代理在事件驱动偏好和真实任务环境下的表现。实验设置包括构建基于PersonaLens和PRISM数据集的用户对话历史，涵盖20个领域（如电影、航班），并通过事件驱动的对话生成方法，模拟偏好逐步演化的多轮交互。

数据集/基准测试方面，PERMA包含按时间顺序排列的交互事件，涉及多个会话和领域，并随时间插入偏好相关查询。实验设计了两种任务：一次性多项选择（MCQ）探测和交互式评估。MCQ任务通过三个评估维度（如零样本偏好回忆）测量选择准确率；交互式评估则通过多轮对话，由用户模拟器评估任务完成度和偏好满意度，并提供纠正反馈。

对比方法上，实验比较了先进记忆系统（通过关联相关交互提取偏好）与传统语义检索原始对话的方法。主要结果显示，先进记忆系统能提取更精确的偏好并减少token消耗，优于传统检索。关键数据指标包括：在MCQ任务中，模型在Type 2（相关领域事件后）和Type 3（全局时间线末尾，含无关领域干扰）任务上的性能差异，用于量化抗遗忘和上下文干扰的鲁棒性。然而，模型在跨时间深度和跨领域干扰中仍难以维持一致的人设，突显了更鲁棒的个性化记忆管理的需求。

### Q5: 有什么可以进一步探索的点？

基于PERMA论文的局限性，未来研究可从以下几个方向深入探索。首先，论文指出当前记忆系统在跨域干扰和时间深度下仍难以维持一致的用户画像，这表明需要开发更鲁棒的记忆整合与冲突消解机制。例如，可以探索基于因果推理或动态图神经网络的记忆结构，以显式建模偏好间的依赖与演化关系。

其次，基准测试虽引入了会话噪声和语言风格对齐，但现实场景中的偏好演化可能更复杂，涉及多模态交互（如语音、图像）或外部知识注入。未来可扩展至多模态个性化记忆评估，并研究如何在噪声中识别关键偏好信号。

再者，评估主要关注记忆检索的准确性，但对记忆系统的效率（如令牌消耗、响应延迟）和可扩展性分析不足。可设计轻量级记忆压缩与索引方法，并在部署环境中进行端到端评估。

最后，论文的模拟用户基于规则，未来可引入强化学习驱动的自适应用户模拟器，以生成更复杂、动态的交互模式，从而更全面地测试智能体在长期服务中的个性化能力。

### Q6: 总结一下论文的主要内容

该论文提出了PERMA基准，旨在评估具备长期记忆的LLM智能体在真实、动态交互场景中维持用户个性化状态（Persona）的能力。针对现有评估方法将偏好视为静态属性、忽略事件驱动演化和现实对话噪声的局限，PERMA的核心贡献在于构建了一个基于事件驱动偏好和现实任务环境的评估框架。

论文首先定义了问题：现有评估未能捕捉用户偏好随事件和对话逐步演化、并在嘈杂上下文中积累的特性，导致对智能体个性化记忆管理能力的评估失真。为此，PERMA构建了一个包含10位不同背景用户、跨越20多个主题、超过800个时序交互事件的大规模数据集。方法上，采用两阶段生成流程：先由时间线生成代理将事件转化为详细描述和目标，再由对话生成代理构建完整对话，并区分“新偏好出现”和“现有偏好补充”两类事件。为逼近真实世界，注入了五种类型的对话内噪声（如信息省略、语境切换、偏好不一致）并引入了基于真实数据的语言风格对齐查询。

主要结论显示，通过关联相关交互，先进的记忆系统能提取更精确的偏好并减少token消耗，优于传统的原始对话语义检索。然而，现有系统在跨时间深度和跨领域干扰下仍难以维持连贯的个性化状态，突显了开发更鲁棒的个性化记忆管理技术的迫切需求。PERMA通过多项选择问答和基于用户模拟器的交互式任务，为评估记忆系统在动态用户建模、噪声鲁棒性和时序一致性方面的性能提供了全面工具。
