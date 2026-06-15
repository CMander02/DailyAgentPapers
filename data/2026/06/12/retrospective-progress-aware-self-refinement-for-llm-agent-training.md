---
title: "Retrospective Progress-Aware Self-Refinement for LLM Agent Training"
authors:
  - "Xinbei Ma"
  - "Congmin Zheng"
  - "Jiyang Qiu"
  - "Jiale Hong"
  - "Yao Yao"
  - "Xiangmou Qu"
  - "Jiaxin Yin"
  - "Xingyu Lou"
  - "Jun Wang"
  - "Weiwen Liu"
  - "Weinan Zhang"
  - "Zhuosheng Zhang"
  - "Hai Zhao"
date: "2026-06-12"
arxiv_id: "2606.14302"
arxiv_url: "https://arxiv.org/abs/2606.14302"
pdf_url: "https://arxiv.org/pdf/2606.14302v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "强化学习训练"
  - "自我反思"
  - "任务进度感知"
  - "WebAgent"
  - "Agent训练框架"
relevance_score: 9.5
---

# Retrospective Progress-Aware Self-Refinement for LLM Agent Training

## 原始摘要

LLM-based agents trained with reinforcement learning optimize step-wise action prediction but lack metacognitive awareness of task progress, inducing a gap that hinders long-horizon scaling. A pilot study reveals that online progress prompting hurts performance while retrospective demonstrations help, yet this capability cannot emerge from outcome-reward training alone. We present RePro, Retrospective Progress-Aware Training, a framework that trains agents to self-generate progress signals via a forward-then-reflect rollout paradigm: the agent executes actions online, then retrospectively reassesses its step-wise progress given the completed trajectory and known outcome. RePro initializes with a Retrospection Warmup that teaches reflection format from minimal external demonstrations, then further trains through RePro-PO with a composite reward that produces self-generated signals without continuous external supervision. Experiments on WebShop, ALFWorld, and Sokoban show that RePro enhances the Qwen family's performance, with up to $12\%$ absolute success rate gains.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于LLM的智能体在长程任务中缺乏任务进度元认知能力的问题。现有方法主要采用强化学习优化智能体的逐步骤动作预测，但智能体缺乏对整体任务进度的感知（即已完成、待完成和当前轨迹是否正常），这严重限制了其在长程任务中的性能。

研究背景表明，虽然强化学习能带来显著性能提升，但传统训练仅关注步骤级决策和稀疏的结果奖励，无法赋予智能体进度感知能力。初步实验揭示了关键矛盾：在推理时强制要求智能体在线评估自身进度（在线进度提示）反而导致平均成功率下降8.6%，而提供基于已完成轨迹的回顾性进度示范却能带来7.9%的提升。这种不对称性说明进度感知是有益的，但无法通过简单提示获取，需要专门的训练框架。

因此，论文提出RePro框架，其核心问题是：如何让智能体学会从回顾性轨迹中自我生成可靠的进度信号，并将其作为辅助信号来引导训练，从而在不依赖持续外部监督的情况下提升长程任务性能。该框架通过“先执行后反思”的范式，让智能体在完成任务后基于已知结局重新评估各步骤的进度，再结合复合奖励机制进行训练。

### Q2: 有哪些相关研究？

相关研究主要分为三类。在**强化学习方法**方面，许多工作借鉴在线策略优化，如通过轨迹组估计优势或改进采样策略来训练具身智能体，但本文指出这些方法缺乏元认知的任务进度意识。在**奖励设计**方面，基于结果的方法受限于稀疏终端反馈，基于过程的方法需要昂贵标注或环境特定设计，而基于进度的方法通过启发式估计或更强LLM监督来建模完成进度。本文与之区别在于，RePro使用最小外部监督，从智能体自身完成的轨迹结果中内化进度估计，无需额外奖励模型。在**推理与训练时间反思**方面，推理时方法如将失败轨迹转为语言反馈或情境记忆，但未训练新的反思能力；训练时方法如元内省或自校正训练，但聚焦于修正单个动作或规划。本文的创新在于提出回顾式进度感知反思，利用完整轨迹结果回顾性评估中间步骤的任务进度，生成自监督信号以训练智能体追踪长期任务位置。

### Q3: 论文如何解决这个问题？

论文提出RePro（Retrospective Progress-Aware Training）框架，通过“先执行后反思”的两阶段范式解决LLM智能体缺乏任务进展元认知的问题。

核心方法包括两个阶段：**回顾预热阶段**和**进展感知策略优化阶段（RePro-PO）**。整体框架将智能体交互建模为POMDP，重新定义工作模式为前向执行与回顾性反思结合的“forward-then-reflect”模式。在前向执行中，智能体每一步同时生成在线进度评估$\tilde{p}_t$和动作$a_t$；轨迹完成后，通过回顾提示$\pi_\theta^{retro}$基于完整轨迹和已知结果重新评估每步进度$p_t$。

关键技术方面：回顾预热阶段利用外部模型（DeepSeek-V4）在成功轨迹上生成回顾反思示范，构建监督数据集$\mathcal{D}_{warmup}$，通过联合训练前向动作预测和回顾进度评估学习反思格式。RePro-PO阶段设计复合奖励函数$R(\tau)$，整合了环境稀疏奖励$r_{env}$、进度差异塑形$r_p$、在线预测与回顾对齐$r_{align}$及格式合规$r_{format}$，提供细粒度中间信号。创新点包括：1）利用已知结果锚定回顾值（成功时$p_T=1$），基于轨迹长度校准中间值；2）基于GiGPO设计双粒度层次优势函数，结合情节优势$A^{episode}$和基于相同观测状态归因的步骤优势$A^{step}$，实现精细化的信用分配；3）通过自生成进度信号替代持续外部监督，实现元认知能力的自主学习。

该框架在WebShop、ALFWorld和Sokoban上取得最高12%的绝对成功率提升。

### Q4: 论文做了哪些实验？

论文在三个基准上进行了实验：WebShop（电商购物模拟，15步限制）、ALFWorld（文本家务任务，50步限制）和Sokoban（推箱子谜题，含稀疏中间奖励）。对比方法包括两类：1）提示方法，如基础提示、元进度提示、随机进度和回顾进度提示；2）训练方法，包括GRPO、GiGPO及元进度提示基础上的L1（格式惩罚）和L2（直接使用预测进度作为步骤奖励）。使用Qwen2.5-1.5B/3B/7B和Qwen3-4B模型，评估成功率和分数。

主要结果：RePro持续优于所有基线。在WebShop上，平均成功率达到76.13%（1.5B）、79.73%（3B）和80.47%（7B），相较于元进度基线分别提升+8.98%、+11.57%和+5.82%。在ALFWorld上，RePro在1.5B和7B模型上分别实现96.02%和97.54%的成功率，提升+17.54%和+6.17%。在Sokoban上，RePro在Qwen3-4B上取得81.64%成功率，提升+7.58%。消融实验表明，预热数据和组件设计至关重要。

### Q5: 有什么可以进一步探索的点？

RePro目前依赖显式的语言化进度评估，这种形式虽可解释且易监督，但未探索隐状态或隐藏向量监督等更高效的进度表征方式。未来可研究将进度信号编码为潜在表示，直接融入策略网络的中间层，避免生成文本带来的计算开销。其次，当前评估限于WebShop、ALFWorld等模拟环境，未扩展至GUI自动化或开放世界具身交互等复杂场景，这主要由资源限制导致，未来需在更大规模、更具挑战性的任务中验证其泛化能力。最后，进度信号缺乏天然的真实标签，RePro依赖事后回顾派生监督，但可能继承原始轨迹的偏差。一个改进方向是引入人类标注或强LLM评估作为伪参考，通过对比学习或对抗训练校准进度估计的准确性，从而提升模型对任务进展的元认知能力。

### Q6: 总结一下论文的主要内容

这篇论文研究了基于LLM的智能体在执行长期任务时缺乏“进度感知”这一元认知能力的问题。作者通过预实验发现，在线进度提示会损害性能，而回顾性示范则有帮助，且这种能力无法仅通过结果奖励训练获得。为此，提出了RePro（回顾性进度感知训练）框架，采用“先执行后反思”的范式：智能体先在线执行动作，然后根据完整轨迹和已知结果回顾性地评估其步骤级进度。框架包含反思预热和RePro-PO训练阶段，利用复合奖励生成自我信号，无需持续的外部监督。在WebShop、ALFWorld和Sokoban三个环境上的实验表明，RePro显著提升了Qwen系列模型的性能，成功率最高提升12%。该工作的核心贡献在于揭示了进度感知信号在长期任务中的价值，并提出了一种无需外部模型的自主训练方法，为开发具备内省能力的自反射智能体开辟了新方向。
