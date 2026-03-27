---
title: "PICon: A Multi-Turn Interrogation Framework for Evaluating Persona Agent Consistency"
authors:
  - "Minseo Kim"
  - "Sujeong Im"
  - "Junseong Choi"
  - "Junhee Lee"
  - "Chaeeun Shim"
  - "Edward Choi"
date: "2026-03-26"
arxiv_id: "2603.25620"
arxiv_url: "https://arxiv.org/abs/2603.25620"
pdf_url: "https://arxiv.org/pdf/2603.25620v1"
categories:
  - "cs.CL"
tags:
  - "Persona Agent"
  - "Evaluation Framework"
  - "Multi-turn Interaction"
  - "Consistency"
  - "Human-Agent Comparison"
  - "Benchmarking"
relevance_score: 7.5
---

# PICon: A Multi-Turn Interrogation Framework for Evaluating Persona Agent Consistency

## 原始摘要

Large language model (LLM)-based persona agents are rapidly being adopted as scalable proxies for human participants across diverse domains. Yet there is no systematic method for verifying whether a persona agent's responses remain free of contradictions and factual inaccuracies throughout an interaction. A principle from interrogation methodology offers a lens: no matter how elaborate a fabricated identity, systematic interrogation will expose its contradictions. We apply this principle to propose PICon, an evaluation framework that probes persona agents through logically chained multi-turn questioning. PICon evaluates consistency along three core dimensions: internal consistency (freedom from self-contradiction), external consistency (alignment with real-world facts), and retest consistency (stability under repetition). Evaluating seven groups of persona agents alongside 63 real human participants, we find that even systems previously reported as highly consistent fail to meet the human baseline across all three dimensions, revealing contradictions and evasive responses under chained questioning. This work provides both a conceptual foundation and a practical methodology for evaluating persona agents before trusting them as substitutes for human participants. We provide the source code and an interactive demo at: https://kaist-edlab.github.io/picon/

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）驱动的“角色代理”在作为人类参与者替代品时，其行为是否具备“一致性”的评估难题。随着角色代理在医学训练、社会科学实验等领域的广泛应用，其可扩展性和成本效益备受青睐。然而，现有方法缺乏系统化的评估框架来验证这些代理在交互过程中是否始终保持逻辑自洽、事实准确且回答稳定。

现有评估方法存在明显不足。它们主要关注“内部一致性”（即代理自身陈述是否前后矛盾），但评估方式不够严谨：通常采用开放式闲聊或独立问题集，缺乏逻辑紧密相连的追问，无法真正“压力测试”角色设定的牢固性。更重要的是，“外部一致性”（陈述是否符合现实世界事实）和“重测一致性”（对同一问题的回答是否稳定）这两个关键维度在现有工作中几乎被完全忽视。这种评估的片面性导致我们无法确信角色代理能否可靠地替代真实人类参与者。

因此，本文的核心问题是：如何系统、全面且严格地评估角色代理在交互中的一致性？为此，论文借鉴审讯方法论中揭露虚构身份的逻辑，提出了名为PICon的评估框架。该框架通过逻辑链式的多轮追问来深入探测内部一致性，利用实时网络搜索验证外部一致性，并通过重复提问检验重测一致性，从而首次构建了一个统一覆盖这三个核心维度的自动化评估体系，旨在为角色代理的可靠使用提供概念基础和实践方法。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在方法类研究中，相关工作包括基于真实个人数据构建数字复制品（如访谈式生成代理、数字孪生研究的大规模问答数据集），以及人物生成方法（如OpenCharacter和DeepPersona），它们能大规模合成多样且叙事连贯的人物对话对，但存在系统性偏见。本文的PICon框架与这些方法不同，它不旨在生成人物，而是专注于通过逻辑链式多轮提问来系统评估人物代理的一致性。

在应用类研究中，人物代理已用于医患模拟、商业人物对话和合成用户测试等领域。为提高行为稳定性，有研究应用多轮强化学习来减少人物不一致性。本文的工作为这些应用提供了前置评估基础，确保代理在作为人类替代品前具备可靠性。

在评测类研究中，现有工作主要通过开放式闲聊或结构化QA基准（如PersonaGym和InCharacter）来评估人物保真度，但问题间缺乏逻辑链，难以暴露潜在矛盾。评测方法主要包括基于NLI的分类器和LLM-as-a-Judge方法，但它们多关注内部一致性。本文的PICon框架扩展了评测维度，不仅评估内部一致性（无自相矛盾），还涵盖外部一致性（与现实事实对齐）和重测一致性（重复下的稳定性），从而提供了更全面的评估方案。

### Q3: 论文如何解决这个问题？

论文通过提出PICon框架来解决评估角色代理一致性的问题。该框架的核心方法是借鉴审讯学中的系统性盘问原则，通过逻辑链式的多轮提问来暴露角色代理在交互过程中的矛盾和不一致。其整体架构设计围绕三个一致性维度展开：内部一致性（避免自我矛盾）、外部一致性（符合现实世界事实）和重测一致性（重复测试下的稳定性）。

PICon的主要模块包括：1）问题生成器，基于角色描述自动构建逻辑关联的多轮问题链，确保问题之间具有因果或时序关系；2）交互引擎，负责与角色代理进行多轮对话并记录响应；3）一致性评估器，采用规则与模型结合的方式分析响应，检测矛盾点（如直接否定、事实冲突、语义不一致）和逃避回答行为；4）量化评分系统，为三个维度分别设计指标并计算综合得分。

关键技术创新点在于：首先，将审讯逻辑转化为可计算的评估框架，通过链式提问模拟深度质询，而非单点测试；其次，引入多维度一致性评估，覆盖角色代理的自我逻辑、事实对齐和稳定性，全面超越传统单维评估；最后，框架支持自动化大规模评估，同时结合人类基线对比，揭示现有LLM角色代理与人类表现的显著差距。实验表明，即使此前被认为高度一致的系统，在PICon的链式追问下也会出现矛盾或逃避回答，验证了该方法的有效性。

### Q4: 论文做了哪些实验？

论文实验围绕PICon框架评估七组人物智能体与63名真实人类参与者在三个一致性维度上的表现。实验设置采用多智能体架构：使用GPT-5作为提问者，GPT-5.1作为实体与主张提取器，Gemini-2.5-Flash作为评估器。每次审问包含10个了解性问题和40个主要问题，共50轮对话。

评估的数据集基于具体人口属性（如年龄、职业）定义的人物实例，每组随机抽取10个实例。对比方法包括：商业服务Character.ai、微调模型（OpenCharacter、Consistent LLM）以及基于提示或检索增强生成的方法（DeepPersona、Human Simulacra、Twin 2K 500等），后四类均运行于Gemini-3-Flash以控制模型变量。

主要结果如下：在内部一致性（IC）上，人类基准得分为0.90±0.05，最佳人物智能体Human Simulacra为0.79±0.13，最差OpenCharacter仅0.16±0.07；IC分解显示，OpenCharacter和Consistent LLM因合作性得分极低（分别为0.11和0.20）导致IC低下。在外部一致性（EC）上，人类得分为0.66±0.07，Character.ai最高（0.71±0.07），OpenCharacter最低（0.15±0.14）；EC分解中，Character.ai覆盖率达0.66，但非反驳率仅0.79，而Twin 2K 500非反驳率达1.00却覆盖率仅0.16。在重测一致性（RC）上，多数智能体接近人类基准，但Character.ai、OpenCharacter和Consistent LLM表现显著较差。此外，会话间一致性分析显示，在默认设置下，DeepPersona得分为0.65±0.29，Human Simulacra为0.87±0.11，表明部分智能体存在本质不稳定性。总体而言，所有人物智能体在雷达图聚合得分上均未超越人类基线，揭示了现有方法在链式追问下存在矛盾、逃避或事实错误。

### Q5: 有什么可以进一步探索的点？

该论文的局限性为未来研究提供了多个可探索的方向。首先，PICon框架假设智能体持合作态度，但现实中智能体可能采取回避或拒绝策略，导致评估失效。未来可研究更具对抗性的提问策略，例如设计能识别并绕开“安全回答”的追问逻辑，或引入博弈论方法来应对不合作行为。其次，当前评估主要关注客观事实和逻辑一致性，忽略了主观维度（如语言风格、偏好、人格特质的一致性）。未来可探索如何量化这些主观特征，例如通过风格嵌入向量或人格量表评分，并将其整合到一致性评估中。第三，证据收集依赖于公开网络信息，存在覆盖盲区。未来可结合本地数据库、领域知识库甚至多模态信息源（如地图、交通时刻表）来验证更广泛的事实主张。最后，人类基线数据的代表性受限于滚雪球抽样方法。未来可通过分层抽样或与专业调查机构合作，获取更丰富的人口统计学背景数据，从而建立更稳健的人类基准。此外，从方法论角度看，可探索将PICon框架扩展到动态或长期交互场景，评估智能体在时间推移或信息更新下的持续一致性。

### Q6: 总结一下论文的主要内容

该论文提出了PICon框架，用于评估基于大语言模型的人物角色代理在多轮对话中的一致性。核心问题是现有代理缺乏系统化验证方法，可能导致回应中出现矛盾或事实错误。受审讯方法启发，PICon通过逻辑链式多轮提问探测代理，从三个维度评估一致性：内部一致性（避免自相矛盾）、外部一致性（符合现实事实）和重测一致性（重复测试下的稳定性）。实验评估了七组人物角色代理和63名真人参与者，发现即使此前被认为高度一致的代理也无法在所有维度上达到人类基线水平，在链式追问下会暴露出矛盾或回避性回应。主要结论是当前代理仍存在显著缺陷，该框架为系统性评估角色代理提供了概念基础和实践方法，有助于开发更可靠的人类参与者替代方案。
