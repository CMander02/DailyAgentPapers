---
title: "Probe-then-Plan: Environment-Aware Planning for Industrial E-commerce Search"
authors:
  - "Mengxiang Chen"
  - "Zhouwei Zhai"
  - "Jin Li"
date: "2026-03-16"
arxiv_id: "2603.15262"
arxiv_url: "https://arxiv.org/abs/2603.15262"
pdf_url: "https://arxiv.org/pdf/2603.15262v1"
categories:
  - "cs.AI"
tags:
  - "Agent Planning"
  - "Tool Use"
  - "Retrieval-Augmented Agent"
  - "E-commerce Agent"
  - "Reinforcement Learning"
  - "Industrial Application"
  - "Query Understanding"
  - "Search Agent"
relevance_score: 7.5
---

# Probe-then-Plan: Environment-Aware Planning for Industrial E-commerce Search

## 原始摘要

Modern e-commerce search is evolving to resolve complex user intents. While Large Language Models (LLMs) offer strong reasoning, existing LLM-based paradigms face a fundamental blindness-latency dilemma: query rewriting is agnostic to retrieval capabilities and real-time inventory, yielding invalid plans; conversely, deep search agents rely on iterative tool calls and reflection, incurring seconds of latency incompatible with industrial sub-second budgets. To resolve this conflict, we propose Environment-Aware Search Planning (EASP), reformulating search planning as a dynamic reasoning process grounded in environmental reality. EASP introduces a Probe-then-Plan mechanism: a lightweight Retrieval Probe exposes the retrieval snapshot, enabling the Planner to diagnose execution gaps and generate grounded search plans. The methodology comprises three stages: (1) Offline Data Synthesis: A Teacher Agent synthesizes diverse, execution-validated plans by diagnosing the probed environment. (2) Planner Training and Alignment: The Planner is initialized via Supervised Fine-Tuning (SFT) to internalize diagnostic capabilities, then aligned with business outcomes (conversion rate) via Reinforcement Learning (RL). (3) Adaptive Online Serving: A complexity-aware routing mechanism selectively activates planning for complex queries, ensuring optimal resource allocation. Extensive offline evaluations and online A/B testing on JD.com demonstrate that EASP significantly improves relevant recall and achieves substantial lifts in UCVR and GMV. EASP has been successfully deployed in JD.com's AI-Search system.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决工业级电商搜索系统中，现有基于大语言模型（LLM）的搜索规划方法所面临的“盲目性-延迟”两难困境。研究背景是现代电商搜索正从满足明确查询，转向处理包含隐含约束的复杂探索性查询（例如“搭配绿色上衣的下装”）。传统基于词匹配或嵌入向量的检索方法难以分解此类复杂意图，导致召回率不足或语义漂移。虽然LLM具备强大的推理能力，但现有方法存在明显不足：一方面，生成式查询重写方法在规划时对检索系统的实时能力和库存状况“盲目无知”，常产生无效或冗余的查询计划；另一方面，ReAct等深度搜索代理虽能通过迭代工具调用和反思来感知环境，但其多轮交互导致延迟高达数秒，无法满足工业场景下数百毫秒的严格实时性要求。

本文的核心问题是：如何在确保极低延迟（满足工业部署约束）的前提下，让搜索规划过程能够“感知”实时检索环境（如库存、召回结果），从而生成既合理又可行的搜索计划。为此，论文提出了环境感知搜索规划（EASP）范式，将搜索规划重新定义为一种基于环境现实的动态推理过程。其核心创新是“探测-再规划”机制：首先通过一个轻量级的检索探测模块获取当前检索环境的快照，然后规划器基于此快照诊断执行差距（如实体漂移、属性错位），并一步生成接地的搜索计划，从而在单步推理中兼顾环境感知与低延迟。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。

在方法类中，相关工作包括：1）基于大语言模型的查询重写方法，这类方法直接生成改写后的查询，但缺乏对检索环境（如实时库存、检索能力）的感知，容易产生无效计划；2）ReAct风格的深度搜索智能体，这类方法通过迭代的工具调用和反思来与环境交互并修正计划，但会产生数秒的延迟，无法满足工业级实时系统的毫秒级预算要求。本文提出的环境感知搜索规划（EASP）与这些方法的核心区别在于，它通过“探测-再规划”机制，将规划建立在对检索环境快照的单步诊断推理之上，从而在保持强推理能力的同时，实现了低延迟。

在应用类中，相关工作主要集中于开放域的多跳推理搜索任务。本文则聚焦于工业电商搜索这一特定领域，指出其语义空间相对有界，因此无需复杂的多轮迭代，单次环境诊断即可制定有效计划，这构成了本文方法设计的重要观察基础。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“环境感知搜索规划”（EASP）的整体框架来解决工业电商搜索中LLM推理的“盲目性-延迟”困境。其核心是“探测-再规划”（Probe-then-Plan）机制，将搜索规划重构为一个基于环境实时状态的动态推理过程。

**整体框架与主要模块**：
1.  **检索探测模块**：这是一个轻量级模块，在完整搜索引擎中仅保留核心检索和相关性匹配功能，去除为转化率优化的昂贵计算组件。它接收用户查询`q`，与环境`E`交互，快速生成一个初始检索观测`O_init`，作为当前检索能力的“快照”，为后续规划提供现实依据。
2.  **规划器模块**：作为核心决策代理`π_θ`，它接收查询`q`和检索观测`O_init`，输出一个最优的搜索计划`P`（如查询改写、过滤等动作序列）。其训练分为两个阶段：
    *   **监督微调**：利用一个由强大LLM扮演的“教师代理”离线合成的数据集进行训练。教师代理分析`(q, O_init)`，诊断检索状态（有效、召回失败、精度失败及其子类），并生成经过环境执行验证的多样化搜索计划。规划器通过SFT学习这种诊断和规划能力。
    *   **强化学习对齐**：使用分组相对策略优化（GRPO）方法，将规划器与业务指标（转化率）对齐。规划器对同一上下文生成多个计划，每个计划被送入在线搜索引擎执行，根据检索结果的平均预测转化率计算奖励，并引入“硬相关性门控”确保转化奖励建立在语义准确性的基础上。
3.  **自适应在线服务模块**：包含一个**复杂度感知路由器**，它是一个比规划器更小的语言模型，用于动态路由。它将针对特定产品的简单查询（如“iPhone 17”）导向“快速路径”，完全绕过规划器以保障低延迟；仅将复杂查询触发“复杂路径”，激活完整的EASP流程，实现资源最优分配。

**创新点**：
1.  **环境感知的规划范式**：通过“探测-再规划”机制，将规划建立在对实时检索能力和库存状态的观测之上，从根本上解决了传统查询改写方法对检索环境“盲目”的问题。
2.  **诊断驱动的规划生成**：创新性地将检索问题系统分类（如召回失败下的查询噪声与库存空洞，精度失败下的系统偏见与语义鸿沟），并据此指导具体的规划策略（净化、具体化或保持），使规划行为具有明确的针对性和可解释性。
3.  **两阶段训练与业务对齐**：结合了SFT从高质量演示中学习推理模式，以及RL使用生产模型（相关性、CVR预测）和硬约束直接优化最终业务目标，确保了规划的有效性和实用性。
4.  **轻量级与选择性部署**：整个架构注重效率，检索探测模块大幅精简，并通过路由机制使大部分简单流量不产生额外开销，从而在提升复杂查询效果的同时，满足工业级亚秒级延迟预算。

### Q4: 论文做了哪些实验？

论文实验主要包括离线和在线两部分。实验设置上，模型使用Qwen3-4B作为规划器（Planner），DeepSeek-R1作为教师智能体（Teacher Agent），查询复杂度路由使用Qwen3-0.6B。监督微调（SFT）进行2轮，GRPO强化学习使用组大小G=8在8张NVIDIA H800 GPU上完成。数据集基于京东搜索日志构建，采用难度感知策略：SFT数据集通过上采样复杂查询和下采样简单查询，构建了10万查询样本；GRPO子集则选取了奖励标准差高的前5000个高频查询。测试集包含从历史日志中采样的1万个复杂查询。

评估指标包括REL@30（前30名候选中的相关商品数量）和HR@30（命中率@30，衡量最终购买商品是否出现在前30名候选）。对比基线包括：1）Blind Rewriter（仅基于查询的行业标准重写器，用于消融环境感知组件）；2）w/o RL（仅使用SFT训练的规划器，用于消融GRPO对齐）；3）ReAct Agent（具有在线工具访问的多轮智能体，代表推理上限但延迟高）。

主要结果：在离线评估中，EASP在REL@30达到23.3，HR@30达到31.0%，均优于Blind Rewriter（20.7和28.6%）和w/o RL（23.0和29.5%），且延迟保持在毫秒级。与ReAct Agent相比，EASP的REL@30略低（24.1 vs. 23.3），但HR@30更高（30.2% vs. 31.0%），且延迟远低于秒级的ReAct。在线A/B测试显示，EASP在全流量上显著提升UCVR 0.89%（p<0.05）和GMV 0.57%（p<0.05）；在触发复杂路径的请求中，UCVR提升4.10%，GMV提升2.59%。延迟方面，p75为20毫秒，p99低于700毫秒，满足工业级实时要求。

### Q5: 有什么可以进一步探索的点？

本文提出的EASP框架在解决“盲目性-延迟”困境上取得了显著成效，但其探索点仍可进一步拓展。局限性在于当前系统主要依赖实时库存和检索快照进行规划，尚未充分整合动态的用户行为序列和长期偏好，这限制了搜索计划的个性化程度。未来研究可深入探索如何将用户实时点击、浏览历史等行为信号无缝融入“探测-规划”机制，使规划器能进行更精准的个性化策略调整。此外，目前的复杂度感知路由机制相对静态，未来可引入强化学习进行动态路由优化，根据实时系统负载和查询意图复杂度自适应分配资源。另一个重要方向是探索多模态信息的融合，例如结合商品图像和视频特征，使规划能理解更丰富的上下文信息。最后，可将该框架扩展至更广泛的工业场景，如广告推荐或客服对话，验证其跨领域泛化能力。

### Q6: 总结一下论文的主要内容

该论文针对工业级电商搜索中LLM应用面临的“盲目性-延迟”困境，提出了一种环境感知的搜索规划框架EASP。核心问题是现有LLM搜索范式要么因缺乏实时环境感知而生成无效计划，要么因深度迭代推理导致延迟过高。EASP的核心创新是“探测-再规划”机制：首先通过轻量级检索探针获取实时库存与检索能力的快照，然后规划器基于此环境快照进行诊断并生成可行的搜索计划。方法上，采用三阶段流程：离线阶段由教师智能体合成经过执行验证的多样化规划数据；接着通过监督微调初始化规划器，并利用强化学习对齐业务指标（如转化率）；在线阶段则通过复杂度感知路由选择性激活规划模块以优化资源。主要结论表明，该框架在京东的在线A/B测试中显著提升了相关召回率、用户转化率和商品交易总额，成功实现了低延迟下的高效、可落地的搜索规划。
