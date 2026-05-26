---
title: "ECHO: Terminal Agents Learn World Models for Free"
authors:
  - "Vaishnavi Shrivastava"
  - "Piero Kauffmann"
  - "Ahmed Awadallah"
  - "Dimitris Papailiopoulos"
date: "2026-05-23"
arxiv_id: "2605.24517"
arxiv_url: "https://arxiv.org/abs/2605.24517"
pdf_url: "https://arxiv.org/pdf/2605.24517v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "CLI Agent"
  - "RL for Agents"
  - "World Model"
  - "Dense Supervision"
  - "Self-Improvement"
  - "Action-Prediction"
  - "Terminal Agent"
  - "Policy Gradient"
relevance_score: 9.5
---

# ECHO: Terminal Agents Learn World Models for Free

## 原始摘要

CLI agents are the closest thing language models have to an embodied setting: the model emits commands, the terminal executes them, and the returned stream -- stdout, errors, files, logs, and traces -- records the consequences. We argue that this stream is a supervision signal, but standard agent RL discards it: GRPO-style training updates action tokens with sparse outcome-level rewards while ignoring environment responses already in the rollout. Failed rollouts provide little policy-gradient signal despite containing rich evidence about how the environment responds. We introduce ECHO (Environment Cross-entropy Hybrid Objective), a hybrid objective that combines the standard policy-gradient loss on action tokens with an auxiliary loss that trains the policy to predict environment observation tokens resulting from its own actions. ECHO reuses the same forward pass as GRPO, requires no additional rollouts, and turns terminal feedback into dense supervision for all rollouts. ECHO doubles GRPO pass@1 on TerminalBench-2.0: Qwen3-8B improves from 2.70% to 5.17%, and Qwen3-14B from 5.17% to 10.79%. ECHO also produces policies that better predict terminal dynamics, even on trajectories they did not generate: across held-out rollouts, it sharply reduces environment-token cross-entropy while GRPO alone barely changes it. From base Qwen3-8B, ECHO matches expert-SFT-then-GRPO performance on held-out terminal tasks without expert demonstrations, and recovers roughly half of the expert-SFT initialization benefit on TerminalBench-2.0. In some settings, the environment prediction loss alone enables verifier-free self-improvement, allowing policies to improve on unseen OOD tasks by learning only from environment interactions. Together, these results suggest that environment observations are not merely context for future actions, but a dense, on-policy supervision signal already present in every rollout.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决终端代理在强化学习训练中面临的核心问题：环境反馈信号的稀疏性。在当前主流的GRPO训练范式下，模型在终端环境中执行命令后，终端会返回丰富的流式输出（stdout、错误、文件内容、日志等），但在标准训练中，这些包含环境状态信息的观察token仅仅作为后续动作的上下文，并未被纳入损失函数进行训练。这导致大多数失败的交互轨迹几乎无法提供策略梯度信号，虽然这些轨迹中蕴含了大量关于环境如何响应不同动作的宝贵信息。作者认为，终端输出是容器状态的文本投影，预测这些输出实际上要求模型理解命令的潜在后果（如哪些文件被创建、哪些测试被破坏）。

因此，本文提出ECHO（Environment Cross-entropy Hybrid Objective）目标函数，其核心思想是将环境观察token作为密集的监督信号，在GRPO对动作token的策略梯度损失基础上，增加一个辅助的交叉熵损失来训练策略预测自身动作所产生的终端输出。这样，即使失败的轨迹也能教会模型环境如何响应，将稀疏的最终奖励转化为对所有rollout都有效的密集监督。该方法的优势在于无需额外的模型、rollout或前向计算。

### Q2: 有哪些相关研究？

相关研究主要分为几类。在方法类中，经典世界模型方法（如Dreamer系列）学习动力学模型用于规划，而具身智能体研究（如CWM）利用Python和Docker环境中的观测-动作轨迹训练大模型。ECHO与之不同，它将观测预测直接注入在线策略GRPO中，无需单独语料库或世界模型阶段。在辅助预测类中，无模型强化学习方法（如预测像素、奖励、前向动力学）通过辅助任务改善稀疏反馈下的表征，ECHO遵循这一思路但面向多轮语言智能体，目标文本终端观测已存在于轨迹中。在语言智能体强化学习类中，RLTF预测裁判生成的批评作为辅助损失，OpenClaw-RL通过裁判提取下一状态信号作为标量过程奖励或token级蒸馏目标，ECHO则直接预测原始环境观测token，无需裁判、批评或蒸馏。此外，SkyRL、SimpleTIR、DAPO和ArCHer等方法专注于稳定策略梯度更新，ECHO与之互补，增加了观测token的并行监督损失。

### Q3: 论文如何解决这个问题？

ECHO通过提出混合目标函数来解决终端代理在强化学习中丢弃环境反馈的问题。核心方法是结合GRPO策略梯度损失和辅助的环境预测损失，将终端输出流转化为密集的监督信号。

整体框架基于标准GRPO的强化学习流程，但修改了损失计算方式。主要模块包括：1) **GRPO策略梯度损失**：作用于动作token（即模型发出的命令），利用稀疏的结果级优势值更新策略；2) **环境预测损失**：作用于观测token（即终端返回的输出，包括stdout、错误、文件内容等），计算这些token的交叉熵损失。两个损失共享同一个前向传播过程，通过不同的掩码分别收集动作位置和观测位置的logits，无需额外的rollout或前向计算。

关键技术包括：1) **混合目标函数**：\(\mathcal{L}_{total}=\mathcal{L}_{GRPO}+\lambda\mathcal{L}_{Env}\)，其中\(\lambda\)设为0.05；2) **掩码设计**：排除规则生成的警告token，仅对携带任务特定反馈（如文件名、测试失败信息）的终端输出token计算环境预测损失；3) **自退火机制**：随着模型预测终端输出统计特性的能力提升，环境预测损失自然下降，无需显式调度。这种设计通过表示塑造（representation shaping）让模型学习命令与观测之间的因果关系，从而在后续决策中形成更好的先验。

### Q4: 论文做了哪些实验？

论文在多个基准上进行了全面实验。实验设置包括：从2700个终端任务（来自Endless Terminals和OpenThoughts-Agent-v1-RL）扩展至8870个任务，训练8770个，保留100个作为分布内验证（val100）。对比方法包括基础策略（Qwen3-8B、OpenThinker-Agent-v1-SFT、Qwen3-14B）、标准GRPO和ECHO。训练使用相同的GRPO设置（16次rollout、批次大小16、学习率1e-6、无KL惩罚），ECHO额外使用λ=0.05的环境预测损失。

主要结果在四个基准上报告：val100（100个任务）、ITD（71个任务）、TBLite（100个任务）和TerminalBench-2.0（TB2，89个任务）。关键数据指标：在TB2上，Qwen3-8B的pass@1从GRPO的2.70%提升至ECHO的5.17%（×1.9）；Qwen3-14B从5.17%提升至10.79%（×2.1）。在内部基准上，Qwen3-8B的val100从34.2%（基础）提升至54.9%（GRPO）和63.7%（ECHO）；ITD从7.0%提升至16.2%和18.9%；TBLite从4.9%提升至9.5%和11.4%。ECHO还将环境token交叉熵从0.24降至0.07（Qwen3-14B，val100），且学习速度比GRPO快1.5-2.3倍。在推理效率上，ECHO将Qwen3-8B的TB2超时率从19.8%减至9.0%，完成token减少30%。

### Q5: 有什么可以进一步探索的点？

ECHO提出的环境预测损失虽然有效，但其核心假设是环境响应是可预测的确定性反馈，这与真实终端环境的随机性（如网络延迟、文件系统状态变化）存在矛盾。未来可探索**不确定性建模**——让策略同时输出动作和对环境观测的置信度，仅在低置信度时激活环境预测损失。此外，当前方法仅对终端输出进行预测，忽视了**隐式反馈信号**（如退出码、stderr中的异常模式）。可以设计分层预测目标：低层预测原子操作结果（如文件是否存在），高层预测任务级状态转移。另一个关键问题是环境预测损失在长轨迹中会加剧**分布偏移**——早期动作的预测误差会层层放大。可引入**时序差分式预测**，让每个时间步的预测仅关注短期环境变化，而非完整序列重建。最后，该方法在模型过小时失效（如1.5B参数），未来可研究知识蒸馏策略：用小模型预训练环境预测器，再将预测能力注入策略网络。

### Q6: 总结一下论文的主要内容

本文介绍了一种名为ECHO（Environment Cross-entropy Hybrid Objective）的混合目标函数，用于解决终端智能体强化学习中监督信号稀疏的问题。核心思想是将环境反馈（如stdout、错误日志、文件内容等）视为稠密的监督信号，通过在GRPO基础上增加环境token的交叉熵损失来利用这些信号。该方法无需额外rollout、教师模型或架构改动，仅复用GRPO的相同前向计算。实验表明，在TerminalBench-2.0上，ECHO使Qwen3-8B的pass@1从2.70%提升至5.17%，Qwen3-14B从5.17%提升至10.79%%，几乎翻倍。此外，ECHO能学习终端动态特性，无需专家演示即可匹配专家SFT+GRPO的性能，甚至在没有验证器的情况下也能实现自我改进。这些发现表明，环境回应是智能体训练中未被充分利用的宝贵监督信号。
