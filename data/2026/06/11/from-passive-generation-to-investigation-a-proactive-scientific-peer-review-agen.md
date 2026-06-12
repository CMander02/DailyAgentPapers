---
title: "From Passive Generation to Investigation: A Proactive Scientific Peer Review Agent"
authors:
  - "Haishuo Fang"
  - "Yue Feng"
  - "Iryna Gurevych"
date: "2026-06-11"
arxiv_id: "2606.13349"
arxiv_url: "https://arxiv.org/abs/2606.13349"
pdf_url: "https://arxiv.org/pdf/2606.13349v1"
categories:
  - "cs.CL"
tags:
  - "LLM-based Agent"
  - "Scientific Agent"
  - "Peer Review Agent"
  - "Reinforcement Learning"
  - "Markov Decision Process"
  - "Proactive Investigation"
  - "Agent Memory/Log"
relevance_score: 9.0
---

# From Passive Generation to Investigation: A Proactive Scientific Peer Review Agent

## 原始摘要

Large language models (LLMs) have shown promise in automating scientific peer review. However, existing approaches often struggle to generate in-depth reviews supported by concrete evidence. We argue that a key limitation is the lack of flexibility to proactively investigate suspicious parts of a paper based on accumulated evidence, as human reviewers do. In this paper, we explore how to enable an LLM-based review agent to perform such proactive investigation. We find that this can be naturally formulated as a Markov Decision Process (MDP), and propose ProReviewer, a scientific peer review agent that proactively reviews a paper guided by a maintained, structured review log. The structured review log serves as a workspace for the agent to track evidence and intermediate findings collected during review. Experiments show that ProReviewer with an 8B backbone, trained by supervised fine-tuning and optimized by reinforcement learning, achieves the highest average score across five quality dimensions, outperforming prompt-based methods with much larger frontier LLMs by up to 39% and the strongest fine-tuned baseline by 16% relatively. It also attains the highest win rates against baselines in human evaluation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前基于大语言模型（LLM）的自动化科学同行评审系统中，评审内容浅薄、缺乏具体证据支撑的问题。

研究背景是，同行评审是学术质量把控的核心机制，而LLM在自动化评审方面展现出潜力。现有方法，如直接提示、多阶段流水线或多智能体协作，主要将评审视为一个被动的文本生成任务，其调查路径是预先固定的。

这些现有方法的不足在于，它们生成的批评往往流于表面，评论缺乏具体证据，容易不假思索地接受作者的主张，且无法有效检测跨章节的逻辑不一致（例如，引言中的论断与实验结果相矛盾）。这源于它们缺乏像人类审稿人那样，根据已积累的证据主动调查论文中可疑部分、并灵活调整调查路径的能力。

本文提出ProReviewer，旨在解决这一核心问题：如何让基于LLM的评审代理具备主动调查能力。具体而言，该方法将评审过程形式化为马尔可夫决策过程（MDP），并通过维护一个结构化的评审日志来追踪证据和中间发现，引导代理进行后续调查，从而生成有据可查、深入的评审意见。

### Q2: 有哪些相关研究？

1. **LLM-based Review Generation类研究**：早期工作如Direct Prompting通过单次生成完成审稿，但缺乏深度和具体性。近期方法通过分阶段子任务（如Hierarchical Question Decomposition）、多智能体角色分配（Multi-agent Role Assignment）或模块化流水线（Modular Pipeline）引入结构，但均采用固定审稿流程，无法根据已积累证据动态调整。本文的ProReviewer与这些方法的区别在于：(1) 通过强化学习（RL）学得审稿策略，而非人工设计，支持基于证据的主动探查；(2) 维护结构化审稿日志，持久化跟踪中间发现。同期工作DeepReviewer 2.0虽也跟踪证据，但其“可追溯审稿包”主要面向人类审计，而本文日志作为智能体的工作记忆，用于决策下一步探查方向。

2. **Agentic Reasoning类研究**：LLM智能体在Web导航、软件工程、科学发现等领域取得显著成果。典型框架如ReAct交替进行思考与行动，Reflexion和Self-Refine引入迭代自校正循环，其他工作通过暂存器（Scratchpad）或持久记忆（Persistent Memory）增强长程信息保留。但这些方法通常积累非结构化推理轨迹，难以选择性修正特定早期发现或追溯批评证据。本文的关键差异在于：将结构化审稿日志作为可训练MDP状态的一部分，支持选择性修订和证据追溯，无需保留完整上下文推理轨迹。

### Q3: 论文如何解决这个问题？

ProReviewer将审稿过程形式化为马尔可夫决策过程(MDP)，通过一个可学习的策略让智能体主动探索论文内容。其核心创新在于引入了一个结构化的“审稿日志”作为工作空间，用于持续追踪审稿过程中收集的证据和中间发现。

整体框架包含以下核心组件：状态空间由当前上下文、审稿日志和论文索引组成。动作空间分为环境动作和日志动作两类，环境动作包括读取章节、关键词搜索和终止；日志动作包括记录新证据、更新现有条目状态以及生成最终审稿要点。该框架采用模块化设计，未来可轻松扩展外部检索等动作。

关键技术包括：(1) 审稿日志机制，维护三类证据条目——声明、问题和笔记，每条证据都有唯一ID和状态标注，最终审稿中的每个要点都必须引用对应的证据ID，形成可验证的证据链；(2) 多维奖励函数，涵盖语法有效性、审稿完整性、内容质量和评分对齐四个维度，兼顾步骤级和轨迹级优化；(3) 两阶段训练流程：先对从强大教师模型蒸馏的轨迹进行监督微调，再使用GRPO强化学习分两阶段优化——第一阶段仅使用确定性规则奖励，第二阶段加入基于大语言模型的评委的质量奖励。实验表明，仅8B参数的ProReviewer在五个质量维度上取得了最高平均分，超越了使用更大规模前沿大语言模型的基于提示的方法。

### Q4: 论文做了哪些实验？

论文使用ICLR 2025-2026年的5011篇论文作为数据集（4011篇训练/验证，1000篇测试），采用时间隔离避免数据污染。对比方法分三类：提示方法（AgentReview、AI-Scientist-v2，覆盖8B到397B参数模型及商业模型Gemini-3.1-flash-lite）、监督微调（CycleReviewer、DeepReview）和强化学习（Vanilla RL基线）。所有微调方法使用Qwen3-8B和Llama3.1-8B作为基础模型，在8×A100 GPU上训练，RL训练使用GPT-OSS-120B作为评判模型。

自动评估由三个多样化的评判模型（GPT-5.4 nano、DeepSeek-V4 flash、RevUtil）在动作性、可验证性、技术深度和基础性四个维度上评分（1-5分制归一化到[0,1]），同时报告分数对齐。ProReviewer（Qwen3-8B）在平均得分（0.57）和最佳四次得分（0.65）上均最高，超越所有基线（包括397B参数的AI-Scientist-v2的0.46平均得分）。具体地，在基础性（0.64 vs 0.44）和技术深度（0.48 vs 0.46）上超越AI-Scientist-v2，在动作性（0.46）和可验证性（0.40）上也领先。RL方法显著优于SFT方法（CycleReviewer和DeepReview仅0.35-0.36）。人类评估由五位顶级会议审稿人对50篇论文进行成对比较，ProReviewer在所有维度上胜率51%-95%，尤其在基础性和技术深度上优势明显（69.2%-94.9%）。

### Q5: 有什么可以进一步探索的点？

ProReviewer虽然性能优异，但存在三个核心拓展方向。首先，当前纯文本处理无法检验图表证据，后续可引入多模态感知能力，直接验证论文中趋势曲线与文本描述的一致性。其次，模型仅在ICLR等AI领域论文上训练，需要积累生物医学、社会科学等领域的公开评阅数据，并通过领域适配迁移。第三，论文仅关注内部推理，未进行外部新颖性检索，未来可将开放语料库检索作为MDP的独立动作集成。值得注意的是，消融实验证实结构化评阅日志和马尔可夫决策过程框架对减少长文性能衰减至关重要，但检测逻辑错误仅27%的准确率仍是显著瓶颈。建议考虑：1）在状态表示中融合图表编码特征；2）设计跨领域奖励函数；3）引入检索增强生成的动态查阅机制。

### Q6: 总结一下论文的主要内容

这篇论文提出了ProReviewer，一个基于LLM的主动科学审稿代理。现有方法通常只能被动生成评论，缺乏灵活性来主动调查论文中可疑部分。作者将审稿过程形式化为马尔可夫决策过程（MDP），通过一个结构化的审稿日志来跟踪证据和中间发现，使代理能够主动调查。实验表明，仅8B参数量的ProReviewer在五个质量维度上平均得分最高，比使用更大前沿LLM的基于提示的方法高出最多39%，比最强的微调基线高出16%，并在人工评估中取得最高胜率。核心贡献是将LLM审稿从被动生成转向主动调查，证明了基于证据跟踪的主动探索是提升LLM辅助审稿质量的关键方向，尤其适用于需要多步分析推理的复杂文档任务。
