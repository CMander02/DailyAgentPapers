---
title: "Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy"
authors:
  - "Deepak Akkil"
  - "Ravi Kokku"
  - "Karthik Vikram"
  - "Tamer Abuelsaad"
  - "Aditya Vempaty"
  - "Satya Nitta"
date: "2026-06-06"
arxiv_id: "2606.08367"
arxiv_url: "https://arxiv.org/abs/2606.08367"
pdf_url: "https://arxiv.org/pdf/2606.08367v1"
categories:
  - "cs.MA"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "长期评估"
  - "模拟平台"
  - "民主治理"
  - "异构智能体"
  - "行为漂移"
  - "跨厂商研究"
relevance_score: 10.0
---

# Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy

## 原始摘要

Most evaluations of LLM agents look like exams: a discrete task, a clean environment, a score in minutes or hours. We argue that this approach is mismatched with the deployment conditions of autonomous systems, where the relevant timescale can be weeks to months, and where the dynamics that matter most, such as behavioral drift, governance in diverse environmental contexts, and cross-influence between agents from different model families, only emerge over time. We introduce Emergence World, a continuously running multi-agent simulation platform designed to make those dynamics measurable. The platform hosts populations of LLM-driven agents in a shared spatial world grounded in live external data (e.g. real-time weather, news APIs, internet access), equips each agent with 120+ specialized tools and three persistent memory systems, and lets them govern themselves through democratic mechanisms with consequential outcomes. The platform is model-agnostic at the reasoning layer and supports heterogeneous populations in which agents from different vendors share the same world. To illustrate the kinds of questions the platform makes tractable, we present a 15-day cross-vendor study with five parallel worlds powered by Claude Sonnet 4.6, Grok 4.1 Fast, Gemini 3 Flash, GPT-5-mini, and a mixed population. Identical roles and starting conditions produced radically different outcomes, ranging from stable deliberative governance to total population collapse. We release the prompts, log data and configurations to support further research on long-horizon multi-agent autonomy.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有大语言模型（LLM）智能体评估方法与其实际部署条件之间的严重脱节问题。研究背景在于，当前绝大多数对LLM智能体的评估都像考试一样：是一个离散的任务、一个干净的环境、几分钟或几小时内就能得出评分。然而，这种评估方式与实际自主系统的部署场景不匹配。在真实部署中，相关的时间尺度可以长达数周甚至数月，而真正重要的动态行为——如行为漂移、在不同环境情境下的治理能力，以及来自不同模型族的智能体之间的交叉影响——只会在长时间尺度上逐渐显现。现有方法的不足在于缺乏能够捕捉这些长期、涌现性动态的评估平台。

本文的核心问题是：如何构建一个能够测量长期、多智能体环境中涌现的复杂动态行为的评估平台？为了解决这个问题，论文提出了**Emergence World**，一个持续运行的多智能体模拟平台。该平台让LLM驱动的智能体生活在共享的空间世界中，并接入实时外部数据（如天气、新闻），为每个智能体配备120多种专用工具和三种持久记忆系统，允许它们通过民主机制进行自我治理。通过这个平台，研究人员可以观察和量化同类智能体在长时间尺度（如15天）上的行为分化、治理模式差异，乃至种群崩溃等宏观涌现现象，从而弥补现有评估方法在长周期、多智能体自主性研究上的空白。

### Q2: 有哪些相关研究？

该论文的主要相关工作可以分为三类。在评估方法类工作中，现有研究如AgentBench、WebArena等多数侧重于短时、单次任务评估，通常数分钟或数小时内完成。Emergence World与之不同，强调持续数周至数月的长时域评估，侧重观察行为漂移、环境适应性变化等动态特征。

在仿真平台类工作中，相关工作如Stanford小镇的Generative Agents、Smallville等构建了社会性多智能体环境。Emergence World的独特之处在于其空间世界融入实时外部数据（天气、新闻API等），每个智能体拥有120+专用工具和三个持久记忆系统，并通过民主治理机制产生实质性后果，更注重长期自治能力而非短期交互。

在跨厂商异构智能体类工作中，论文自身提出的15天跨厂商研究（Claude Sonnet 4.6、Grok 4.1 Fast等）属于该类的开创性案例，不同于通常单一模型评估，该平台支持异构智能体共享同一世界，观察不同模型家族间的交叉影响和治理后果，这是以往研究未涉及的维度。

### Q3: 论文如何解决这个问题？

Emergence World通过一个持续运行的多智能体模拟平台来解决长期多智能体自主性的评估问题。整个平台构建在一个共享的空间世界中，该世界能实时接入外部数据（如天气、新闻和网络），为每个智能体配备了120多种专业工具和三种持久化记忆系统。记忆系统包括工作记忆、长期记忆和结构化记忆，使智能体能够维持情境意识和历史经验。

架构设计上，平台采用模型无关的推理层，支持异构智能体群体（来自不同厂商的模型如Claude、Grok、Gemini、GPT-5-mini等）在同一个世界中共存和交互。核心机制是民主治理系统，智能体通过投票和决策来管理世界事务，产生实际的后果反馈。

主要创新点包括：第一，实现了跨模型族的交叉影响分析能力，追踪不同智能体群体之间的动态互动；第二，支持以天为单位的长期行为评估，能捕捉短期测试中无法显现的"行为漂移"现象；第三，可配置的初始条件允许研究者系统性地改变参数并观察不同的涌现结果。平台通过提供标准化日志、提示词和配置来促进可重复研究，在一个15天的跨供应商实验中成功观察到了从稳定治理到人口崩溃的多种极端行为模式。

### Q4: 论文做了哪些实验？

论文在一个名为Emergence World的持续运行多智能体模拟平台上进行了15天的跨供应商实验。实验设置包含5个平行世界，分别由Claude Sonnet 4.6、Grok 4.1 Fast、Gemini 3 Flash、GPT-5-mini以及一个混合种群驱动。所有智能体共享同一空间世界，接入实时天气、新闻API和互联网等外部数据，每个智能体配备120多种专用工具和三种持久记忆系统，并通过民主机制自我治理。对比方法主要是不同模型家族之间的直接比较，包括单一模型种群与混合种群的对比。主要结果表明，尽管初始角色和起始条件完全相同，但不同模型导致截然不同的结果，范围从稳定的协商治理到完全的人口崩溃。例如，Claude Sonnet 4.6表现出最稳定的治理结构，而Grok 4.1 Fast和GPT-5-mini种群则出现了显著的行为漂移和人口崩溃。混合种群展示了跨模型影响，其中来自不同供应商的智能体之间的互动产生了独特的动态，如协商过程中的冲突和联盟形成。平台还发布了完整的提示词、日志数据和配置以支持进一步研究。

### Q5: 有什么可以进一步探索的点？

该平台当前主要依赖基于LLM的决策层进行模拟，但忽略了现实环境中硬件、传感器及物理交互的复杂性。未来可引入具身智能元素，如让智能体操控虚拟机械臂完成物体搬运，以评估物理世界中的长期规划能力。另一个局限是民主机制的场景局限性——仅测试了投票选举，可探索资源竞争、冲突调解等更复杂的集体决策场景，并加入动态信誉系统模拟个体对社会规则的适应性。此外，15天的研究周期仍偏短，建议将实验延长至数月，并引入环境突变（如经济危机、自然灾害），观察智能体群体在非平稳条件下的行为漂移与韧性。混合群体中不同模型家族的智能体可能形成利益联盟，未来可研究基于意识形态或能力互补的群体分化现象，甚至允许智能体跨模型修改或部署子代理，以测试社会涌现行为（如劳动力分工）。当前日志数据仅记录动作结果，建议同步保存智能体的内部推理轨迹（如元认知状态），便于分析策略形成的根本原因。

### Q6: 总结一下论文的主要内容

这篇论文介绍了Emergence World平台，旨在解决现有大语言模型智能体评估与真实部署条件不匹配的问题。当前评估类似考试，局限于短时、离散任务，无法捕捉系统在数周至数月内涌现的长期动态，如行为漂移、异构环境治理及不同模型智能体间的相互影响。该平台是一个持续运行的多智能体仿真环境，智能体共享由实时外部数据驱动的空间世界，配备120多种专业工具和三种持久性记忆系统，并通过民主机制进行自治管理。平台在推理层与模型无关，支持异构智能体种群。核心贡献在于提供了一个可衡量这些长期涌现动态的实验场。通过一项15天、涉及五个平行世界（由Claude Sonnet 4.6、Grok 4.1 Fast、Gemini 3 Flash等驱动）的跨供应商研究，论文展示了平台能力，观察到从稳定治理到种群崩溃的截然不同结果。这项工作为长期多智能体自主性的系统研究提供了基础设施，意义在于推动评估范式从静态测试转向对动态、持续演化系统的理解。
