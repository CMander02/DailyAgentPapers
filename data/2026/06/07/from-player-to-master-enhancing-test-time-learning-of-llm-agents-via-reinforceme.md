---
title: "From Player to Master: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory"
authors:
  - "Yishuo Cai"
  - "Xingyu Guo"
  - "Xuancheng Huang"
  - "Jinhua Du"
  - "Can Huang"
  - "Wenxuan Huang"
  - "Wenhan Ma"
  - "Yuyang Hu"
  - "Aohan Zeng"
  - "Jie Tang"
  - "Xu Sun"
date: "2026-06-07"
arxiv_id: "2606.08656"
arxiv_url: "https://arxiv.org/abs/2606.08656"
pdf_url: "https://arxiv.org/pdf/2606.08656v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "记忆更新"
  - "测试时学习"
  - "强化学习"
  - "多智能体博弈"
  - "GRPO"
  - "规划与推理"
relevance_score: 8.0
---

# From Player to Master: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory

## 原始摘要

Large language model (LLM) agents are increasingly deployed in long-running settings where improving through experience at test time becomes important. A common approach is to update an explicit memory after each interaction to guide future decisions. However, most existing methods rely on hand-designed prompting rules, making it difficult to align memory updates with downstream objectives over multi-step horizons consistently. We propose MemoPilot, a plug-in memory copilot that explicitly trains the memory update process to improve a frozen LLM's performance across sequential interactions. We formulate memory updating as a multi-turn decision problem and optimize it end-to-end with multi-turn GRPO. Our training recipe introduces (i) a turn-wise reward signal and (ii) a context-independent, turn-level advantage estimation across rollouts, enabling finer-grained credit assignment and more stable training in multi-turn settings. We evaluate MemoPilot on two testbeds: multi-round Rock-Paper-Scissors (RPS) and Limit Texas Hold'em (LHE). Across both environments, MemoPilot substantially improves test-time learning of a frozen player over strong baselines, ranking first in Elo ratings on both games (1762 on LHE and 1590 on RPS) and outperforming all baseline memory methods and proprietary models, including DeepSeek-V3.2.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）代理在长序列交互中如何实现有效的测试时学习（Test-Time Learning, TTL）的问题。研究背景是，LLM代理被越来越多地部署在需要与任务、用户或环境反复交互的场景中，此时通过经验积累来提升后续决策能力至关重要。现有方法通常构建显式记忆来存储和利用经验，例如Reflexion、ExpeL等方法通过反思或积累经验来迭代改进，但这些方法大多依赖于手工设计的提示规则来更新记忆。这种启发式方法存在关键不足：由于缺乏与下游性能目标的端到端优化，即使是强大的指令遵循LLM也难以在多步交互中持续、一致地改进，记忆更新过程很难与长期目标对齐。因此，本文要解决的核心问题是：如何训练一个可插拔的记忆管理模块，使其能够显式地优化记忆更新过程，从而帮助一个冻结的（frozen）LLM代理在多轮交互中实现更高效的、可学习的测试时性能提升。论文将记忆更新建模为多轮决策问题，并创新性地引入多轮GRPO（Group Relative Policy Optimization）和轮次级奖励信号进行端到端优化，以使代理能像人类玩家一样通过“假设-验证”循环从经验中学习策略。

### Q2: 有哪些相关研究？

相关研究可分为三类。第一类是**记忆增强型语言智能体**，如Generative Agents引入记忆流进行社会模拟，Agent Workflow Memory提取可复用工作流，A-MEM提出自组织记忆，MEM1学习记忆与推理协同，MemGen生成潜在记忆，Buffer of Thoughts维护思维模板。本文与它们的区别在于，大多数工作聚焦于任务内持久化，而本文研究跨游戏对局的战略记忆演化，并端到端训练记忆更新过程以优化下游效用。第二类是**经验驱动与持续学习**，如Reflexion通过言语自反思改进，ExpeL跨任务积累洞察，Dynamic Cheatsheet通过启发式更新维护演化记忆，ReasoningBank通过轨迹比较缩放记忆，SkillWeaver和PolySkill研究可复用技能。这些工作主要依赖启发式或基于提示的经验更新，而本文直接使用下游奖励优化记忆更新策略。第三类是**文本与辅助策略优化的强化学习**，如RLPrompt和OPRO优化提示，Prompt-R1训练提示重写器，RLAD训练抽象生成器，SPIRAL通过自对弈RL优化玩家。本文与后者的核心区别在于，MemoPilot保持玩家模型冻结，训练外部记忆模块，使其可应用于更强或闭源的玩家。

### Q3: 论文如何解决这个问题？

MemoPilot提出了一种强化学习驱动的记忆更新框架，核心是将记忆更新形式化为多轮序贯决策问题，并通过多轮GRPO进行端到端优化。整体框架包含三个模块：状态空间由当前对局轨迹和上一轮记忆组成，动作空间为文本记忆的生成，策略模型基于状态采样新记忆。关键技术包括：1）结构化记忆空间设计，分为诊断分析（识别对手策略）、信念维护（记录假设与置信度）和行动指导（生成可执行策略）三个组件，支持迭代更新和自然停止条件；2）多轮GRPO训练算法，引入轮级奖励信号和上下文无关的轮级优势估计，通过单步代理回报（下一局结果）替代累积回报进行组归一化，实现更精细的信用分配和稳定训练；3）可控对手池构建，通过指令控制对手策略的可复现性、行为多样性和机制性训练测试分离，并基于Elo评级校准难度。创新点在于首次将强化学习显式应用于记忆更新过程，使记忆生成直接对齐下游多步目标，解决了手工设计提示规则难以实现端到端优化的局限。

### Q4: 论文做了哪些实验？

论文在两个主要基准上进行了实验：多轮石头剪刀布（RPS）和有限注德州扑克（LHE），来自TextArena和RLCard。RPS每局6轮，LHE采用双重复制比赛消除方差。评估指标为RPS@k（平均每局净胜轮数差）和LHE@k（平均每局筹码数），所有结果以mean@64报告，内存预算固定为512 token。使用Qwen2.5-14B-Instruct作为基座模型和对手模型，训练时每轮包含3个连续游戏。

对比方法包括无内存、完整历史、人类专家编写策略、Reflexion、ExpeL、MemoryBank、AWM和ReasoningBank，其中基于内存的方法以DeepSeek-V3.2为基座。主要结果：MemoPilot在RPS@5上达到3.28（无内存为0.43），LHE@5上达到2.03（无内存为-1.36）；Elo评分方面，MemoPilot在LHE和RPS上分别排名第一（1762和1590），优于所有基线和DeepSeek-V3.2。此外，MemoPilot展现出快速学习和跨模型泛化能力，零样本迁移至更强的Qwen3-235B-A22B时仍取得RPS@5的3.27和LHE@5的1.31。在StreamBench基准上（CoSQL和DS-1000），MemoPilot也取得最佳准确率（CoSQL 73.5%，DS-1000 56.3%），显著优于无内存和基于提示的方法。

### Q5: 有什么可以进一步探索的点？

论文的局限性集中在三个方向：首先是对信息性经验与奖励信号的强依赖，当轨迹信息量低或奖励稀疏时，记忆更新的学习信号不足。可探索引入辅助奖励（如token效率、轨迹质量评分）来缓解稀疏奖励问题。其次是固定记忆容量限制（512 tokens），虽然可通过预处理解决，但长期任务中记忆的压缩与优先级策略值得深入研究，比如结合动态记忆剪枝或分层记忆结构。最关键的局限是面对非平稳对手时性能退化，反映出稳定性与快速适应的矛盾。未来可考虑将对抗性对手建模为环境变化，引入元学习中的快速适应机制（如MAML），使记忆更新策略能动态调整学习率。此外，当前偏序优势估计虽稳定训练，但多智能体场景下的协作记忆更新（如共享经验池）也是潜在突破点。整体上，将记忆更新从静态规则转向可学习策略是正确方向，但需在泛化性和计算效率间进一步平衡。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为 MemoPilot 的框架，旨在解决大语言模型代理在长期交互场景中的测试时学习问题。现有方法依赖手工设计的记忆更新提示规则，难以与多步长期目标对齐。MemoPilot 将记忆更新形式化为多轮决策问题，并采用多轮 GRPO（组相对策略优化）进行端到端优化。其核心贡献包括设计逐轮奖励信号和上下文无关的回合级优势估计，从而在随机环境中实现更精细的信用分配和更稳定的训练。在多人猜拳和有限注德州扑克两个测试平台上，MemoPilot 显著提升了冻结主模型的测试时学习能力，Elo 评分分别达到1590和1762，超越所有基线方法及包括 DeepSeek-V3.2 在内的专有模型。实验表明，学习到的记忆策略具有良好的鲁棒性，可泛化至未见对手和更大模型，无需额外参数更新。
