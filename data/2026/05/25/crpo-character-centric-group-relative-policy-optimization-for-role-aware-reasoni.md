---
title: "CRPO: Character-centric Group Relative Policy Optimization for Role-aware Reasoning in Role-playing Agents"
authors:
  - "Yihong Tang"
  - "Kehai Chen"
  - "Liang Yue"
  - "Benyou Wang"
  - "Min Zhang"
date: "2026-05-25"
arxiv_id: "2605.25511"
arxiv_url: "https://arxiv.org/abs/2605.25511"
pdf_url: "https://arxiv.org/pdf/2605.25511v1"
categories:
  - "cs.CL"
tags:
  - "角色扮演Agent"
  - "强化学习"
  - "GRPO"
  - "人物一致性"
  - "策略优化"
  - "角色感知推理"
  - "多智能体对齐"
relevance_score: 9.5
---

# CRPO: Character-centric Group Relative Policy Optimization for Role-aware Reasoning in Role-playing Agents

## 原始摘要

Recent advancements in Reinforcement Learning (RL), particularly Group Relative Policy Optimization (GRPO), have significantly enhanced the reasoning capabilities of Large Language Models. However, applying these problem-centric optimization methods to role-playing agents often leads to a loss of character fidelity and style collapse, as they prioritize context-specific utility over persona alignment. To address this, we propose Character-Centric Group Relative Policy Optimization (CRPO), a framework designed to realign RL objectives with the role-playing task. CRPO improves character distinctiveness through three mechanisms: decoupling task logic from stylistic rewards to resolve gradient conflicts, dynamically adapting optimization constraints based on character complexity, and utilizing generic responses as negative baselines to prevent the model from reverting to a common distribution. Extensive experiments demonstrate that CRPO outperforms existing methods in consistency, emotion and others.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有强化学习方法在角色扮演智能体中的核心问题：基于问题优化的方法（如GRPO）会导致角色一致性丧失和风格崩溃。研究背景是，近年来强化学习算法（特别是GRPO）显著提升了大型语言模型的推理能力，推动了角色扮演智能体从行为模仿向认知推理的转变。然而，现有方法存在三个主要不足：第一，模糊的奖励信号，标准GRPO使用组内相对归一化，当采样组集体偏离角色风格但逻辑正确时，相对优势仍会分配正向梯度，诱导模型学习去角色化的通用表达；第二，僵化的优化约束，不同角色特征的拟合难度差异显著，与角色无关的约束和更新机制无法适应这种动态变化；第三，风格崩溃风险，由于缺乏显式负样本对比，模型在训练后期容易出现风格退化。为解决这些问题，本文提出了角色中心化的群体相对策略优化（CRPO）框架，旨在将强化学习目标重新对齐到角色扮演任务上，通过解耦任务逻辑与风格奖励、基于角色复杂度的动态约束调整、以及使用通用响应作为负基线防止模型退回到通用分布，来增强角色区分度。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：

1. **角色扮演智能体与认知模拟**：早期工作如Prompt Engineering、SFT、RAG等方法仅关注表面语言模式，易导致逻辑不一致和角色漂移。近期研究如TBS、CoSER、REDEN-R1、CPO、MOA和Character-R1开始建模内部思维过程，利用CoT、蒸馏和RL实现角色感知推理。本文与这些工作的区别在于，前者直接应用通用RL算法，而CRPO专门针对角色维持的优化动态进行调整。

2. **GRPO改进方法**：在GRPO基础上，研究聚焦于(1) 信用分配（OAR、λ-GRPO等通过令牌级权重优化）；(2) 信号增强（NGRPO、SGPO等利用误差变换或风险排序）；(3) 稳定性与效率（DaGRPO、SFPO采用区分性采样或双层次更新）；(4) 引导探索（Scaf-GRPO、PTA-GRPO引入层级提示）。这些方法在数学和代码推理中表现优异，但都遵循"问题为中心"的优化范式，忽略了角色扮演中的人物对齐需求。CRPO则转向"角色为中心"的视角，专门解决角色保真度问题。

3. **社交智能体训练**：Sotopia系列探索在交互环境中训练社交智能体，与角色扮演互补，但本文更侧重于通过强化学习实现角色感知推理，而非纯粹的交互训练。

### Q3: 论文如何解决这个问题？

CRPO框架通过三个核心机制将GRPO从“问题中心”重构为“角色中心”：首先，**双流优势估计**将总奖励解耦为任务奖励（基于组内相对归一化，适应问题难度）和风格奖励（基于全局历史统计归一化，保持角色一致性），然后加权融合，避免梯度冲突。其次，**熵感知自适应利用**在实例级，通过角色识别熵量化模型对响应风格归属的置信度，对高熵样本抑制梯度信号，实现谨慎优化；在模型级，根据角色数据的平均信息熵自适应调整KL散度目标值，并采用比例积分控制器动态调节惩罚系数β，以适应不同角色的拟合难度，实现稳定高效风格对齐。最后，**对比锚点采样**通过向采样组中强制注入一个移除角色指令的通用响应作为负样本，其低风格奖励会拉低组内基线，从而放大角色化样本的风格优势值，隐式引导模型最大化角色特征与通用特征的差异，防止后期风格坍缩。这三个组件协同作用，使强化学习优化在保持角色逼真度的同时提升推理能力，在一致性、情感表现等维度优于现有方法。

### Q4: 论文做了哪些实验？

论文在CharacterBench和SocialBench两个基准测试上评估了CRPO。CharacterBench包含22,859个样本（3,956个角色），覆盖记忆一致性、事实准确性等11个维度；SocialBench包含500个角色档案和30,800轮多轮对话，评估社交智能。实验采用Qwen3-8B和Llama-3.2-3B-Instruct作为骨干模型，对比了四类方法：角色扮演方法（SFT、Neeko、RAR、Character-R1）、专用角色扮演模型（CharacterGLM、Haruhi-Zero等）、通用RL方法（PPO、GRPO、DAPO等）以及大基座模型（GPT-4o、Claude-4-opus等）。主要结果：在CharacterBench上，CRPO在Qwen3-8B上取得了4.043的平均分，远超所有基线（如Character-R1为3.878、GRPO为3.829），在记忆一致性（4.525）、知识边界（4.308）、属性一致性（4.994）等多项指标上达到最优。在SocialBench上，CRPO以0.802的平均分领先（OAR为0.787），尤其在角色知识（0.966）和风格（0.922）方面表现突出。消融实验验证了Dual-Stream Advantage、Adaptive Exploitation和Contrastive Anchor三个组件的有效性。

### Q5: 有什么可以进一步探索的点？

论文提出的CRPO方法在风格奖励与任务奖励的解耦上虽有创新，但存在关键局限：其一，风格奖励的“双流优势”仍依赖手工定义的奖励函数，难以泛化到开放式角色扮演场景；其二，文中对角色复杂度（如对话历史长度、性格维度数）的建模过于简化，仅用单一超参数调节优化约束，可能无法捕捉真实交互中的动态演变。未来可从四个方向探索：1）引入元学习框架自动学习风格与任务奖励的权重，避免人工调参；2）设计可微分角色记忆模块，使熵调节策略能基于连续交互历史自适应重置；3）探索稀疏奖励下的在线探索机制，利用角色专属的知识图谱约束策略搜索空间；4）结合人类反馈（RLHF）进行角色一致性细粒度校准，例如对“角色崩坏”片段提供负偏好对。此外，锚点样本的选取策略可扩展为对抗性负样本生成，以强化角色与通用分布的区分度。

### Q6: 总结一下论文的主要内容

这篇论文提出了角色中心群体相对策略优化（CRPO）框架，旨在解决现有强化学习方法在角色扮演智能体中导致角色保真度丧失和风格崩塌的问题。问题在于，传统基于问题优化的GRPO方法优先考虑上下文效用而非角色对齐，带来奖励信号模糊、优化约束僵化和风格崩塌风险三大挑战。方法上，CRPO通过三种机制重建优化目标：双流优势估计解耦任务逻辑与风格奖励，熵感知自适应利用根据角色复杂度动态调整约束，对比锚采样利用通用响应作为负样本来防止模型退化。实验结果表明，CRPO在角色一致性、情感等维度上显著超越现有方法。核心贡献在于首次提出角色中心的GRPO框架，为角色扮演智能体的深度推理对齐提供了新范式。
