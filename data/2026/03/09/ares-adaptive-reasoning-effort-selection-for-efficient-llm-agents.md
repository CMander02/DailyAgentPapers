---
title: "Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents"
authors:
  - "Jingbo Yang"
  - "Bairu Hou"
  - "Wei Wei"
  - "Yujia Bao"
  - "Shiyu Chang"
date: "2026-03-09"
arxiv_id: "2603.07915"
arxiv_url: "https://arxiv.org/abs/2603.07915"
pdf_url: "https://arxiv.org/pdf/2603.07915v1"
categories:
  - "cs.AI"
tags:
  - "推理效率"
  - "自适应推理"
  - "轻量级路由"
  - "多步任务"
  - "WebAgent"
  - "工具使用"
  - "成本优化"
relevance_score: 9.0
---

# Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents

## 原始摘要

Modern agents powered by thinking LLMs achieve high accuracy through long chain-of-thought reasoning but incur substantial inference costs. While many LLMs now support configurable reasoning levels (e.g., high/medium/low), static strategies are often ineffective: using low-effort modes at every step leads to significant performance degradation, while random selection fails to preserve accuracy or provide meaningful cost reduction. However, agents should reserve high reasoning effort for difficult steps like navigating complex website structures, while using lower-effort modes for simpler steps like opening a target URL. In this paper, we propose Ares, a framework for per-step dynamic reasoning effort selection tailored for multi-step agent tasks. Ares employs a lightweight router to predict the lowest appropriate reasoning level for each step based on the interaction history. To train this router, we develop a data generation pipeline that identifies the minimum reasoning effort required for successful step completion. We then fine-tune the router to predict these levels, enabling plug-and-play integration for any LLM agents. We evaluate Ares on a diverse set of agent tasks, including TAU-Bench for tool use agents, BrowseComp-Plus for deep-research agents, and WebArena for web agents. Experimental results show that Ares reduces reasoning token usage by up to 52.7% compared to fixed high-effort reasoning, while introducing minimal degradation in task success rates.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在执行多步任务时，因采用固定、高强度的链式思维推理而导致的**高昂推理成本**问题。随着GPT-5或Gemini-3等先进LLM开始支持可配置的“思维等级”（如高/中/低），现有方法通常采用静态策略：要么全程使用低强度推理以节省成本，但这会导致任务成功率显著下降；要么随机选择推理强度，但这既无法保证性能，也难以实现有效的成本节约。然而，实际任务中不同步骤的难度差异很大：例如，打开一个目标URL可能很简单，而导航复杂的网站结构则需要深度推理。因此，静态策略无法在**性能（任务成功率）与成本（推理令牌消耗）** 之间取得良好平衡。

本文的核心问题是：如何为LLM智能体的**每一步**动态地、自适应地选择**最低足够**的推理强度，从而在几乎不损失任务性能的前提下，大幅降低推理开销。为此，作者提出了Ares框架，其核心是一个轻量级的“路由器”模型，它根据智能体与环境的交互历史，预测下一步所需的最低合适推理等级。该框架通过一个自动化的数据生成流程进行训练，该流程能为轨迹中的每一步标注出成功完成所需的最小推理努力，进而微调路由器以实现精准预测。Ares的设计与传统的模型路由（涉及切换不同模型，带来额外开销）不同，它利用同一模型内部的不同推理模式，允许跨级别重用KV缓存，从而最大化节省令牌并减少延迟。实验表明，Ares在多种智能体任务上能在保持高成功率的同时，将推理令牌使用量降低高达52.7%。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两大类：LLM路由和高效自适应推理。

在**LLM路由**方面，已有工作通过训练路由器（常基于人类偏好数据）或采用基于聚类的路由（如Avengers、BESTRoute）来为单轮任务（如数学问题）选择最优模型，将其简化为独立分类问题。近期研究如ToolOrchestra和Router-R1将其扩展到多轮智能体任务，前者使用协调器LLM进行联合规划与路由，后者将多轮路由视为序列过程但侧重于简单QA任务。EvoRoute则提出了经验驱动的自路由框架。然而，这些方法多关注多模型范式，存在成本-性能关系非单调和上下文编码冗余的问题。本文的Ares框架则专注于**单模型内可配置推理层级**的动态选择，针对多步智能体任务中步骤相互依赖的特点进行序列决策，并重用KV缓存以避免额外推理成本。

在**高效自适应LLM推理**方面，相关研究旨在根据输入难度或用户指定的思维预算，动态调整单轮设置中的推理轨迹长度或截断中间思考。这些方法主要控制单轮推理。相比之下，Ares将推理努力程度建模为一个**序列决策过程**，使其适用于更复杂、多轮次的智能体任务，实现了在任务步骤级别上的自适应推理资源分配。

### Q3: 论文如何解决这个问题？

论文通过提出Ares框架，采用动态推理努力选择机制来解决LLM智能体推理成本高的问题。核心方法是训练一个轻量级的路由器模型，根据交互历史为每个决策步骤预测最低但足够的推理等级，从而在保持任务成功率的同时显著降低计算开销。

整体框架包含两个核心组件：LLM智能体和路由器模型。智能体负责执行任务，其推理等级可在高中低等预设级别中配置；路由器则接收与智能体相同的输入上下文，输出当前步骤应使用的推理等级。训练流程分为数据生成和路由器优化两阶段。

数据生成阶段包含三个主要模块：轨迹收集、努力标注和原理生成。首先，使用最高推理等级收集成功轨迹，并选择最简洁的轨迹作为参考路径。接着，对每个步骤进行多轮采样验证，确定能可靠复现正确行动的最低推理等级，形成监督标签。然后，利用教师模型为每个标注步骤生成解释性原理，说明为何该等级适合当前子任务。

路由器优化采用监督微调和强化学习相结合的方式。监督微调训练路由器根据上下文生成原理和等级标签，学习单步最优选择。为进一步优化多步动态，论文引入强化学习，使用包含结果奖励、推理成本奖励和格式奖励的复合奖励函数，通过GRPO算法训练路由器平衡任务成功与计算效率。

创新点在于：1) 将长视野优化问题解耦为独立的单步标注任务，通过后验分析确定每步最低充足推理等级，避免了搜索空间爆炸和错误传播；2) 引入原理生成机制，增强路由器的可解释性和决策质量；3) 结合监督学习和强化学习，既学习单步最优，又优化整体轨迹效率；4) 框架设计为即插即用，可适配不同LLM智能体。实验表明，该方法在多种智能体任务上能减少高达52.7%的推理令牌使用，且任务成功率下降极小。

### Q4: 论文做了哪些实验？

论文在三个不同的智能体环境中进行了实验：TAU-Bench（工具使用智能体）、BrowseComp-Plus（深度研究智能体）和WebArena（网页导航智能体）。实验使用gpt-oss-20b作为主干LLM，并对比了多种基线方法：固定推理努力策略（低、中、高）、随机选择策略以及基于提示的策略（使用GPT-5和Gemini 3 Pro等大型LLM进行动态选择）。

主要评估指标包括任务性能（TAU-Bench的平均奖励、BrowseComp-Plus的准确率、WebArena的任务成功率）和推理效率（总推理token数$T_{total}$、每任务平均token数$T_{task}$、每步平均token数$T_{step}$）。关键结果显示，Ares在保持与固定高努力策略相近或更高性能的同时，显著降低了推理开销。例如，在TAU-Bench零售域，Ares达到54.8%的成功率（与高努力基线持平），总推理token减少约35.2%；在BrowseComp-Plus上，Ares准确率为41.3%（接近高努力基线的42.7%），token消耗降低41.8%；在WebArena上，Ares任务成功率为46.5%（略高于高努力基线的45.0%），token消耗减少45.3%。此外，论文还进行了强化学习（RL）微调实验，在TAU-Bench零售域和航空域进一步提升了性能（如零售域成功率从54.8%提升至58.5%）并优化了效率。这些结果表明Ares能够动态分配推理努力，在复杂步骤保留高努力，在简单步骤使用低努力，从而实现高效且准确的智能体决策。

### Q5: 有什么可以进一步探索的点？

该论文提出的Ares框架在动态选择推理强度以平衡性能与成本方面具有创新性，但仍存在一些局限性和值得深入探索的方向。首先，其核心依赖一个轻量级路由器来预测每步所需的最小推理强度，但该路由器的训练数据生成依赖于人工或规则判断“最小成功所需努力”，这可能导致数据偏差或覆盖不全，未来可探索更自动化的数据标注方法，例如利用强化学习让模型自我探索不同努力水平下的成功率，从而生成更优的训练信号。其次，当前方法主要针对已知任务类型进行优化，对于开放域或高度动态的任务环境（如实时交互游戏、未知软件操作），其泛化能力可能不足，未来可研究如何引入元学习或在线适应机制，使路由器能根据任务上下文实时调整策略。此外，论文主要关注推理令牌数量的节省，但未深入讨论延迟、能耗等实际部署成本，未来可结合硬件感知优化，设计更细粒度的推理强度分级（如结合模型剪枝、早期退出等技术）。最后，Ares目前作为独立模块与现有智能体插件集成，未来可探索将其与智能体的规划模块深度融合，实现推理资源分配与任务分解的联合优化，从而在复杂任务中实现更智能的自适应决策。

### Q6: 总结一下论文的主要内容

本文提出Ares框架，旨在解决大语言模型（LLM）智能体在推理过程中因固定使用高计算资源而导致效率低下的问题。核心贡献在于设计了一种动态调整推理努力程度的机制，使智能体能够根据任务步骤的复杂度自适应选择最合适的推理级别（如高/中/低），从而在保证任务成功率的同时显著降低推理成本。

方法上，Ares通过轻量级路由器模块，基于交互历史预测每个步骤所需的最低推理级别。为训练该路由器，研究团队开发了数据生成流程，自动识别成功完成步骤所需的最小推理努力，并据此微调路由器以实现即插即用。实验评估覆盖了工具使用、深度研究和网页操作等多类智能体任务（如TAU-Bench、BrowseComp-Plus和WebArena）。结果表明，相比固定高努力推理，Ares能减少高达52.7%的推理令牌使用，且任务成功率几乎不受影响，为高效LLM智能体的部署提供了实用解决方案。
