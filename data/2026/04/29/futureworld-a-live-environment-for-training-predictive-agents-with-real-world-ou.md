---
title: "FutureWorld: A Live Environment for Training Predictive Agents with Real-World Outcome Rewards"
authors:
  - "Zhixin Han"
  - "Yanzhi Zhang"
  - "Chuyang Wei"
  - "Maohang Gao"
  - "Xiawei Yue"
  - "Kefei Chen"
  - "Yu Zhuang"
  - "Haoxiang Guan"
  - "Jiyan He"
  - "Jian Li"
  - "Yitong Duan"
  - "Yu Shi"
  - "Mengting Hu"
  - "Shuxin Zheng"
date: "2026-04-29"
arxiv_id: "2604.26733"
arxiv_url: "https://arxiv.org/abs/2604.26733"
pdf_url: "https://arxiv.org/pdf/2604.26733v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "LLM Agent"
  - "Reinforcement Learning"
  - "Environment for Agent Training"
  - "Future Prediction"
  - "Benchmark"
  - "Online Learning"
relevance_score: 9.5
---

# FutureWorld: A Live Environment for Training Predictive Agents with Real-World Outcome Rewards

## 原始摘要

Live future prediction refers to the task of making predictions about real-world events before they unfold. This task is increasingly studied using large language model-based agent systems, and it is important for building agents that can continually learn from real-world. Just as interactive environments have often driven progress in agents, advancing live future prediction naturally motivates viewing it as a learning environment. Prior works have explored future prediction from several different parts, but have generally not framed it as a unified learning environment. This task is appealing for learning because it can provide a large number of prediction questions grounded in diverse real-world events, while preventing answer leakage. To leverage the advantages of live future prediction, we present FutureWorld, a live agentic reinforcement learning environment that closes the training loop between prediction, outcome realization, and parameters update. In our environment, we take three open-source base models and train them for consecutive days. The results show that training is effective. Furthermore, we build a daily benchmark based on the environment and evaluate several frontier agents on it to establish performance baselines for current agent systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有研究中缺乏一个统一的、能够持续从真实世界反馈中学习并更新策略的在线预测训练环境的问题。研究背景是，基于大语言模型的智能体系统在实时未来预测任务上日益受到关注，该任务要求系统在事件发生前做出预测，并根据实际结果进行验证和学习。现有方法的不足主要体现在三个方面：首先，一些工作虽然搭建了实时预测评估框架，但并未将其构建为一个完整的学习环境；其次，部分研究引入了强化学习，但其训练信号依赖于过程奖励（如基于评分规则）而非最终的真实结果，导致训练目标与预测目标存在偏差；最后，另一些工作虽尝试了基于结果的强化学习，但仅能在静态的已解密数据集上进行，智能体无法在一个实时环境中自主进行信息检索、证据选择和解读。核心问题是，目前没有一个统一的开源训练环境，能够让智能体在实时环境中自主地生成预测、根据真实世界的结果获取奖励，并动态更新模型参数。为了弥补这一空白，论文提出了FutureWorld，一个实时的、基于智能体强化学习的环境，它通过每日自动生成预测问题、记录智能体轨迹、等待事件结果并计算奖励、最后更新参数，从而闭环地训练智能体，使其能持续从不断演化的真实世界中学习。

### Q2: 有哪些相关研究？

相关研究可分为三类：**交互式环境**、**未来预测基准**和**基于LLM的预测方法**。

**交互式环境**方面，Jericho、ScienceWorld、ALFWorld等构建了受限的文本或任务环境，WebShop、WebArena、VisualWebArena、AppWorld和WorkArena则提供了更真实的网络或软件交互。但这些环境多为封闭或半封闭，无法反映真实世界的开放性变化。FutureWorld则首次将实时预测构建为完整的开放性交互式学习环境。

**未来预测基准**方面，ForecastQA、AutoCast、PROPHET等使用历史或带有证据的问题评估预测能力。ForecastBench和FutureX等实现了实时更新的评估，但主要用于评测而非训练。FutureWorld在此基础上引入了每日滚动的训练基准。

**方法类工作**方面，现有工作尝试改进LLM的预测能力：一部分使用静态已解决数据集进行基于结果奖励的强化学习，但信息收集行为未被训练；另一部分虽采用实时设置但使用基于排名的过程奖励而非直接结果奖励。FutureWorld是首个同时满足三个关键条件的工作：使用结果驱动奖励、在训练循环内进行智能体信息检索、并运行在实时滚动问题流上。

### Q3: 论文如何解决这个问题？

FutureWorld 通过构建一个闭环的实时强化学习环境来解决智能体在现实世界中的预测能力训练问题。其核心方法是将未来预测任务转化为一个完整的在线学习循环，涵盖问题生成、智能体交互、结果反馈和参数更新。

架构上，该系统首先从72个公开网站自动收集候选未来事件，并通过预定义规则或模板将其转化为二元预测问题。随后，系统利用大语言模型对问题进行过滤，去除不可客观验证、预测价值低或内容敏感的问题。接着，通过聚类和中心偏向的软最大采样进行重采样，以平衡不同领域的代表性问题，最终每日保留500个高质量问题，并转化为概率估计提示。

主要模块包括：1) 数据收集与问题生成模块，负责从多样化的网络源获取事件并构建问题-描述对；2) 过滤与重采样模块，提升问题质量并确保领域均衡；3) 交互与回滚轨迹记录模块，智能体需执行至少一次网络搜索后给出概率预测，系统记录完整交互历史；4) 延迟奖励计算模块，在预定时间检索真实结果，基于负Brier分数计算奖励，并利用GRPO算法进行策略优化。

该方法的创新点在于：首次将实时未来预测系统化地构建为一个统一的、可提供持续反馈的强化学习环境，通过闭环训练实现了从预测到结果再到参数更新的完整迭代，并在多个开源模型上验证了其有效性。

### Q4: 论文做了哪些实验？

该论文通过构建名为FutureWorld的在线强化学习环境，进行了连续多天的agent训练实验。实验设置：基于Qwen3-4B、Qwen2.5-3B和DeepSeek-R1-0528-Qwen3-8B三个开源基座模型，每天20:00释放500个预测问题，次日检索真实结果。使用GRPO算法优化策略，每问题采样4条轨迹，以负Brier损失作为奖励（无效预测惩罚-1）。共训练8天，每日保存检查点。所有检查点在同一测试日评估次日将揭晓的预测问题。对比方法为各模型第0天的初始检查点。主要结果：在预测准确率（概率阈值0.5）上，所有模型随训练天数稳步提升；Brier分数持续下降；期望校准误差（ECE）也逐步降低。领域分解显示，第8天检查点在大多数领域优于初始检查点。此外，针对Qwen2.5-3B的规模实验表明，每日问题数从200增至1000时，性能呈正向扩展趋势。数据指标：每日平均35.65%的问题无法按时检索真实结果（延迟1天降至20%）。

### Q5: 有什么可以进一步探索的点？

论文提出的FutureWorld框架虽具创新性，但存在若干局限。其一，依赖延迟的真实世界结果作为奖励信号，可能导致训练效率低下，尤其对长周期事件预测任务，反馈稀疏且延迟；其二，环境仅覆盖有限类型的事件预测（如体育、金融），缺乏对复杂社会或科学问题的建模，限制了泛化能力。未来可探索(1)引入课程学习或元学习策略，逐步延长预测时间跨度以缓解稀疏奖励问题；(2)结合半监督或自监督的代理奖励信号（如事件因果链推理的中间奖励）辅助训练；(3)扩展多模态输入（如新闻、卫星图像）增强对动态环境的感知；(4)设计对抗性过滤机制防止模型记忆历史模式，提升鲁棒性。此外，将人类反馈（RLHF）融入实时预测循环，或能更高效地引导模型适应非平稳变化。

### Q6: 总结一下论文的主要内容

FutureWorld提出了一个名为FutureWorld的实时智能体强化学习环境,用于训练预测智能体.该环境解决了现有工作中预测任务局限于静态数据集或使用过程奖励而非真实结果的问题.其核心贡献在于将预测、结果实现和参数更新闭环,每天自动从多样化事件源生成大量预测问题,让智能体自主检索信息、分析证据并做出预测,待实际结果揭晓后,使用真实结果作为奖励信号更新模型参数.实验表明,基于真实世界结果的延迟奖励能有效提升开源模型的预测能力,连续训练后性能逐步改善.同时,基于该环境构建的每日基准测试为评估前沿智能体在实时预测任务上的表现提供了实用平台.这项工作推动了能通过预测、观察结果并适应真实世界而持续学习的智能体系统发展.
