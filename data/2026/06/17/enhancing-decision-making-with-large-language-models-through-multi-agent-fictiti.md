---
title: "Enhancing Decision-Making with Large Language Models through Multi-Agent Fictitious Play"
authors:
  - "Leyang Shen"
  - "Yang Zhang"
  - "Xiaoyan Zhao"
  - "Chun Kai Ling"
  - "Tat-Seng Chua"
date: "2026-06-17"
arxiv_id: "2606.19308"
arxiv_url: "https://arxiv.org/abs/2606.19308"
pdf_url: "https://arxiv.org/pdf/2606.19308v1"
categories:
  - "cs.CL"
  - "cs.MA"
tags:
  - "LLM智能体"
  - "多智能体系统"
  - "博弈论"
  - "决策制定"
  - "虚构博弈"
  - "姿态纠缠"
relevance_score: 8.5
---

# Enhancing Decision-Making with Large Language Models through Multi-Agent Fictitious Play

## 原始摘要

Large language model (LLM)-based multi-agent systems (MAS) have demonstrated great potential in solving tasks with execution complexity, by distributing subtasks across cooperative agents. However, this divide-and-conquer paradigm falls short on decision-making tasks that are also prevalent in the real world. These tasks require simultaneous reasoning from the stances of all involved stakeholders whose decisions are mutually dependent and thus cannot be solved in isolation. We characterize this challenge as stance entanglement, a form of decision complexity distinct from execution complexity. To address it, we propose Multi-Agent Fictitious Play (MAFP), a novel MAS paradigm that represents stakeholder stances as agents and formulates decision-making as an equilibrium-seeking process. Built on the game-theoretic principle of fictitious play, MAFP iteratively updates each agent's decision by best responding to the empirical mixture of other agents' past decisions. This enables agents to expose and address one another's weaknesses, progressively improving decision quality and robustness. We evaluate MAFP on challenging decision-making tasks that test the capability of deciding strategies for competitive scenarios prior to acting. MAFP outperforms both single-round and multi-round baselines on two complementary metrics, tournament strength and robustness, demonstrating its effectiveness in addressing stance entanglement.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有基于大语言模型的多智能体系统（MAS）在处理现实世界中决策任务时面临的“立场纠缠”（stance entanglement）问题。现有MAS主要擅长处理“执行复杂性”（execution complexity），即通过将任务分解为子任务分配给合作智能体来降低单个推理的难度，例如软件工程或科学研究。然而，许多现实决策任务（如谈判、博弈、竞争市场）的复杂性来源不同：决策必须同时考虑所有利益相关者的立场，而各方的决策相互依赖（形成“相互依赖循环”），无法孤立求解。这种“立场纠缠”超出了单一语言模型或简单分治范式的处理能力。为此，本文基于博弈论中的“虚拟博弈”（fictitious play）原理，提出了多智能体虚拟博弈框架MAFP。其核心思想是将每个利益相关者的立场建模为一个智能体，将决策过程转化为一个寻找博弈均衡的迭代过程：每个智能体通过最优响应其他智能体历史决策的“经验混合”，逐步暴露和修正彼此的弱点，从而协同进化出高质量且鲁棒的决策。简言之，本文要解决的核心问题是：如何设计一种多智能体范式，以有效应对决策任务中相互依赖的立场带来的复杂性，找到接近纳什均衡的稳定决策。

### Q2: 有哪些相关研究？

该研究的相关工作主要可以分为两类：

1. **多智能体系统（MAS）方法类**：现有LLM-based MAS通过“分而治之”范式处理执行复杂度，如软件工程中将任务分解给专业化角色智能体顺序执行，或通过多智能体辩论实现并行探索。这些方法侧重于任务拆分和编排优化（如协调器优化、拓扑优化），但都局限于“拆分-聚合”框架，无法解决立场纠缠问题。本文提出的MAFP将利益相关者立场建模为自利智能体，通过虚拟博弈迭代更新决策，与现有MAS的协作范式有本质区别。

2. **决策推理方法类**：现有方法通过理论心智（ToM）推理增强LLM决策能力，包括单步立场推断、二阶互推理以及递归k级互预期。然而，这类方法依赖单一LLM调用进行高阶信念推理，随着利益相关者数量增加，推理复杂度超出LLM能力限制（如Hi-ToM/FANToM实验验证的准确性下降和虚假ToM问题）。MAFP通过多智能体协同进化将复杂推理分解为单层逻辑推理，每个LLM调用只需完成条件预测，更符合LLM的优势能力。

本文还涉及相关评测基准（如游戏、谈判、社会推理等场景），但MAFP的创新在于将决策问题转化为均衡搜索过程，而非直接提升单智能体推理能力。

### Q3: 论文如何解决这个问题？

MAFP将决策制定形式化为一个基于语言策略博弈的均衡求解过程。整体框架包含三个核心组件：多智能体初始化、聚合操作符和最佳响应操作符。首先，针对每个利益相关者（stance），MAFP实例化一个对应的智能体，并根据场景描述和该利益相关者的立场（包括角色、目标、约束和收益描述）通过LLM生成初始语言策略，同时维护一个历史策略集合。核心创新在于将博弈论中的虚拟博弈思想引入多智能体LLM系统：每一轮迭代中，聚合操作符利用LLM对各智能体历史策略集合进行总结归纳，形成对手策略的经验混合分布（empirical mixture）。随后，最佳响应操作符基于该聚合后的对手策略以及自身立场，通过LLM生成当前智能体的最优回应策略，并追加到历史集合中。通过多轮迭代，每个智能体逐步暴露并应对其他智能体策略的弱点，实现共同进化。最后，对各轮所有历史策略再次进行聚合，作为每个利益相关者的最终语言策略输出。关键技术在于通过重复的单层推理替代递归的相互预期推理，将决策复杂度从深度为d的指数级搜索简化为K次平推最佳响应，有效解决了立场纠缠问题。

### Q4: 论文做了哪些实验？

论文在13个场景中进行实验，涵盖竞争性游戏（如井字棋、尼姆博弈、囚徒困境（IPD）、四子棋、猪博弈、突破棋、库恩扑克、盲人拍卖、骗子骰子）和自然语言谈判（如谈判、买卖、最后通牒、资源交换）。使用Qwen3.5-35B-A3B作为统一动作模型，每对策略进行16场座位交换比赛，8个随机种子取平均值。评估指标为：**锦标赛强度（TS）**——策略对实验中其他8种竞争策略的平均效用（通过循环赛计算）；**鲁棒性（Rob）**——冻结目标策略，让攻击者LLM在10轮内进化反策略，取目标最低效用。对比方法包括单轮基线（COT推理，使用Qwen3-1.7B、Llama-3.1-8B、GPT-5-nano、Qwen3.5-35B）和多轮基线（自反思SR、辩论Debate、心智理论ToM、MAFP及其消融变体MAFP-Last）。主要结果：MAFP在平均TS（0.533）和平均Rob（0.421）上均最优，验证其性能；消融实验表明，聚合历史策略的混合分布（而非最新策略）是关键；MAFP在不完美信息、随机性场景（如猪博弈、库恩扑克）中优势显著，但在确定性完美信息游戏（如井字棋）中与基线持平。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在实验规模和理论深度两个方面。实验上，受计算资源限制，当前评估仅涵盖有限场景，未来可扩展至更复杂的真实商业决策环境，例如动态市场竞争，其中涉及更多利益相关者和更精细的策略结构。这种扩展有望进一步凸显MAFP通过立场分解与虚拟博弈协同演进带来的优势。理论上，MAFP基于博弈论框架，但尚缺乏对语言空间中虚拟博弈收敛率的严格分析，尤其是在存在多重纳什均衡时如何选择特定均衡，以及能否主动引导迭代轨迹趋向期望均衡。这些开放问题具有高影响力。可能的改进方向包括：引入自适应学习率或混合策略正则化以加速收敛，结合人类偏好或外部奖励信号来偏好特定均衡，以及探索将LLM的语义理解与博弈论的策略抽象更深度融合，以处理更模糊的决策边界。

### Q6: 总结一下论文的主要内容

这篇论文提出并解决了大型语言模型（LLM）在多智能体系统（MAS）中面临的决策复杂性挑战。作者将这种挑战定义为“立场纠缠”（stance entanglement），即决策任务中各方利益相互依赖，无法通过简单分而治之的方式解决。为此，他们提出了多智能体虚构博弈（MAFP）框架。MAFP基于博弈论中的虚构博弈原理，将各利益相关方的立场映射为独立的智能体，并通过迭代更新，让每个智能体对其他智能体的历史决策进行最佳回应，从而模拟一个趋近均衡的决策过程。该方法的核心优势在于，智能体在交互中暴露并弥补彼此的弱点，逐步提升决策质量和鲁棒性。在包含竞技游戏和谈判等13个场景的基准测试中，MAFP在锦标赛强度和鲁棒性两项指标上均超越了单轮和多轮基线方法，尤其在处理非完美信息、随机状态转移和混合策略均衡等真实世界复杂场景时优势显著，有效增强了LLM在多智能体决策任务中的能力。
