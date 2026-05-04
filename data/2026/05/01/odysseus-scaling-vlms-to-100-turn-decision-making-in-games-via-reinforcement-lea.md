---
title: "Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning"
authors:
  - "Chengshuai Shi"
  - "Wenzhe Li"
  - "Xinran Liang"
  - "Yizhou Lu"
  - "Wenjia Yang"
  - "Ruirong Feng"
  - "Seth Karten"
  - "Ziran Yang"
  - "Zihan Ding"
  - "Gabriel Sarch"
  - "Danqi Chen"
  - "Karthik Narasimhan"
  - "Chi Jin"
date: "2026-05-01"
arxiv_id: "2605.00347"
arxiv_url: "https://arxiv.org/abs/2605.00347"
pdf_url: "https://arxiv.org/pdf/2605.00347v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM/VLM Agent"
  - "强化学习"
  - "决策智能体"
  - "游戏智能体"
  - "PPO"
  - "多模态智能体"
  - "长期规划"
  - "训练框架"
relevance_score: 9.5
---

# Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning

## 原始摘要

Given the rapidly growing capabilities of vision-language models (VLMs), extending them to interactive decision-making tasks such as video games has emerged as a promising frontier. However, existing approaches either rely on large-scale supervised fine-tuning (SFT) on human trajectories or apply reinforcement learning (RL) only in relatively short-horizon settings (typically around 20--30 turns). In this work, we study RL-based training of VLMs for long-horizon decision-making in Super Mario Land, a visually grounded environment requiring 100+ turns of interaction with coordinated perception, reasoning, and action. We begin with a systematic investigation of key algorithmic components and propose an adapted variant of PPO with a lightweight turn-level critic, which substantially improves training stability and sample efficiency over critic-free methods such as GRPO and Reinforce++. We further show that pretrained VLMs provide strong action priors, significantly improving sample efficiency during RL training and reducing the need for manual design choices such as action engineering, compared to classical deep RL trained from scratch. Building on these insights, we introduce Odysseus, an open training framework for VLM agents, achieving substantial gains across multiple levels of the game and at least 3 times average game progresses than frontier models. Moreover, the trained models exhibit consistent improvements under both in-game and cross-game generalization settings, while maintaining general-domain capabilities. Overall, our results identify key ingredients for making RL stable and effective in long-horizon, multi-modal settings, and provide practical guidance for developing VLMs as embodied agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决将视觉-语言模型扩展到超过100轮交互的长期决策任务中面临的挑战。当前，虽然人工智能体在网页、GUI和软件工程等场景取得进展，但在视频游戏这类需要持续感知、推理与动作协调的模拟具身任务中，现有方法存在明显不足：要么依赖大规模人类轨迹数据进行监督微调（模仿学习），这难以规模化；要么仅将强化学习应用于约20-30轮的短期任务。研究表明，即便前沿视觉-语言模型在超百轮决策环境中也表现不佳，主要障碍包括缺乏有效的长期时序信用分配、训练不稳定、样本效率低下以及计算开销巨大。为此，本文提出Odysseus开放训练框架，核心创新包括：采用轻量级回合级评论家改进PPO算法，替代无评论家方法（如GRPO、Reinforce++）以提升稳定性和样本效率；引入正优势过滤机制解耦时序信用分配与令牌生成，并利用预训练视觉-语言模型提供的强大动作先验，相比从零训练的经典深度强化学习，显著提升样本效率并减少手动动作工程设计需求。通过多任务强化学习稳定训练，模型在Super Mario Land游戏中实现至少三倍于前沿模型的游戏进度提升，并展示了出色的游戏内和跨游戏泛化能力，同时保持通用领域能力。

### Q2: 有哪些相关研究？

相关研究主要分为三类：

1. **游戏与模拟环境类**：传统研究利用视频游戏作为机器学习测试平台，但近期VLM的RL探索多集中于短视距场景（如AlfWorld、Sokoban、FrozenLake，约20-30步）。本文聚焦于《超级马里奥大陆》这一长视距（100+步）具身控制环境，其视觉空间基础与闭环控制要求更高，但比大规模开放世界模拟器更轻量易控。

2. **基础模型决策类**：近年来研究通过监督微调（SFT）将预训练基础模型用于具身控制，在机器人操作和跨游戏泛化中取得进展。本文与这些工作的主要区别在于，不依赖大量带动作标签的演示数据，而是从RL视角出发探索如何有效适应基础模型。

3. **基础模型智能体RL类**：现有工作为多轮语言和视觉-语言智能体引入轨迹分解、令牌级优势估计或分层信用分配等专用机制，但评估仍限于短视距环境。本文专注长视距、视觉具身场景（100+步），通过消融实验证明，采用正确评论家设计的简单PPO变体即可使RL稳定有效，无需复杂算法架构。

### Q3: 论文如何解决这个问题？

论文提出了Odysseus框架，通过强化学习（RL）训练视觉语言模型（VLM）以解决超长回合（100+回合）游戏决策问题。核心方法是对PPO算法进行适应性改进，引入轻量级回合级评论家网络（turn-level critic）和正优势过滤（positive-advantage filtering）。具体而言，传统PPO在训练VLM时需学习大规模token级评论家，导致计算和内存成本翻倍。Odysseus将评论家设计为轻量级CNN模块，仅对回合级奖励信号进行价值估计，相比GRPO和Reinforce++等无评论家方法，显著提升了长时序信用分配能力和训练稳定性。实验表明，无评论家方法（如GRPO）在100+回合任务中难以学习有效策略，而PPO配合CNN评论家能稳定提升性能。进一步，正优势过滤（仅保留优势值为正的样本）优化了训练稳定性，避免了负优势样本导致的优化震荡。在架构设计上，VLM基座模型（如Qwen3-VL-8B-Instruct）提供强大的视觉语义先验和行为先验，减少了传统深度RL中需要手动设计动作空间的依赖。实验显示，VLM-RL相比从零训练的CNN策略PPO，样本效率提高约2倍，且无需动作空间工程。最终Odysseus框架在多个游戏关卡中实现了至少3倍于前沿模型的平均游戏进展，并保持了跨关卡和跨游戏泛化能力以及通用领域性能。该工作揭示了长时序多模态RL训练的关键要素：轻量级评论家设计、正优势过滤，以及VLM预训练先验的有效结合。

### Q4: 论文做了哪些实验？

论文在《超级马里奥大陆》游戏中进行了多组实验。实验设置使用VLM（视觉语言模型）作为决策代理，在需要100+回合交互的长程决策场景中测试。数据集方面，研究人员从10个关卡的两个通关视频中采样约5000帧，并用GPT-o3生成包含<perception>、<reasoning>、<answer>的教师响应。对比方法包括GPT-5.4、Gemini-3-Flash、Claude-Sonnet-4.6、Qwen3-VL-235B、InternVL3.5-241B等前沿模型及基础版本。

主要实验分为三组：首先比较不同RL算法（PPO、GRPO、Reinforce++），发现自适应PPO配合轻量级回合级critic表现最优；其次对比经典深度强化学习与VLM预训练的效果，证明VLM提供强动作先验显著提升样本效率；最后测试Odysseus框架，在五个训练关卡（1-1至2-2）上测得平均进展。关键数据显示，Odysseus（RL on SFT）在所有关卡平均进展达1511.90（最大2315.6），远超其他模型，如GLM-4.6V的512.91和Claude-Sonnet-4.6的348.19，比前沿模型至少提升3倍。模型还展示了跨关卡与跨游戏泛化能力，并保持通用域能力。

### Q5: 有什么可以进一步探索的点？

该工作主要局限在于任务环境单一（Super Mario Land），其“100+回合”的长程决策复杂性仍远不及现实场景（如机器人操作、自动驾驶），且奖励函数高度依赖游戏设计，难以直接迁移。未来方向包括：首先，可探索更通用的回合级奖励塑形机制，例如结合子目标分解或内在动机（ICM），以缓解稀疏奖励问题。其次，当前PPO变体仅使用轻量回合级critic，尚未研究更细粒度的帧级或动作序列级价值函数，后者可能对微观时序策略有更好建模。此外，直觉上可尝试混合专家（MoE）架构，在不同游戏阶段激活不同视觉/策略模块，以缓解长程依赖下的灾难性遗忘。最后，跨游戏泛化目前仅验证了《超级马里奥》系列，未来需测试至更异质的3D游戏环境（如GTA或Minecraft），并探索无监督预训练（如视频对比学习）以替代手工动作先验，降低领域依赖。

### Q6: 总结一下论文的主要内容

该论文研究如何通过强化学习（RL）训练视觉语言模型（VLM）在需要超过100步交互的游戏中完成决策任务。现有方法主要依赖大规模人类轨迹监督微调（SFT）或仅适用于约20-30步的短视任务。论文以游戏《超级马力欧》为环境，系统探究了关键算法组件，提出一种改进的PPO变体，通过引入轻量级的回合级评论家模块和正优势过滤，显著优于无评论家方法（如GRPO）。实验表明，预训练VLM提供的动作先验比经典深度RL更高效，能减少手动动作工程设计。基于此，论文推出开源框架Odysseus，结合轻量监督初始化和多任务RL，使模型在多个关卡上的平均游戏进度超越前沿模型至少3倍，并展现出游戏内和跨游戏泛化能力，同时保持通用视觉语言能力。该工作证明了在长周期多模态环境中使RL稳定有效的关键要素，为VLM作为具身智能体的发展提供了实用指导。
