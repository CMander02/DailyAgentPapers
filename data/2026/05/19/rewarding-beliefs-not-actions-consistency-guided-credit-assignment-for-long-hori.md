---
title: "Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assignment for Long-Horizon Agents"
authors:
  - "Wenjie Tang"
  - "Minne Li"
  - "Sijie Huang"
  - "Liquan Xiao"
  - "Yuan Zhou"
date: "2026-05-19"
arxiv_id: "2605.20061"
arxiv_url: "https://arxiv.org/abs/2605.20061"
pdf_url: "https://arxiv.org/pdf/2605.20061v1"
github_url: "https://github.com/Fateyetian/Rebel"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "强化学习"
  - "信贷分配"
  - "部分可观测"
  - "长程任务"
  - "信念状态"
  - "自我监督"
  - "多智能体协作"
relevance_score: 9.0
---

# Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assignment for Long-Horizon Agents

## 原始摘要

Reinforcement learning from verifiable rewards (RLVR) is a promising paradigm for improving large language model (LLM) agents on long-horizon interactive tasks. However, in partially observable environments, incomplete observations cause agent beliefs to drift over time, while delayed rewards obscure the causal impact of intermediate decisions, exacerbating temporal credit assignment challenges. To address this, we propose ReBel (Reward Belief), a process-level reinforcement learning algorithm that explicitly models structured belief states to summarize interaction history and guide subsequent policy learning. ReBel introduces belief-consistency supervision, converting discrepancies between predicted beliefs and observed feedback into dense self-supervised signals without requiring external step-wise annotations or verifiers. It also employs belief-aware grouping to compare trajectories under similar belief states, yielding more robust and lower-variance advantage estimates. We evaluate ReBel on challenging long-horizon benchmarks, including ALFWorld and WebShop. ReBel improves task success by up to $20.4$ percentage points over the episode-level baseline GRPO and increases sample efficiency by $2.1\times$. These results suggest that belief-aware self-supervision is a promising direction for reliable long-horizon decision-making under partial observability. Code is available at: https://github.com/Fateyetian/Rebel.git.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在部分可观测、长周期交互任务中，基于可验证奖励的强化学习（RLVR）所面临的挑战。研究背景是大型语言模型（LLM）被部署为自主智能体，执行如具身指令跟随和网页导航等复杂任务。现有方法存在不足：在部分可观测环境中，智能体必须从不完整的观测历史中推断潜在状态，但微小的推理错误会随时间累积，导致“信念漂移”（belief drift），即智能体内部状态估计与环境真实状态之间的偏差逐渐扩大。同时，延迟的终端奖励（episode-level rewards）过于稀疏，无法有效纠正中间信念错误，使得时间信用分配（temporal credit assignment）变得极其困难，难以区分失败是由糟糕的行动选择还是错误的状态估计造成的。此外，现有的步级监督或外部验证器成本高昂且难以扩展。因此，本文要解决的核心问题是：如何在缺乏步级标注或外部验证器的情况下，为部分可观测的长周期任务中的LLM智能体，提供有效的、密集的过程级反馈信号，以纠正信念漂移，实现更精确的信用分配，从而提升策略的最终性能和样本效率。

### Q2: 有哪些相关研究？

**一、方法类相关工作**  
1. **轨迹级强化学习方法**：包括RAP、Agent Q等引入蒙特卡洛树搜索的探索方法，以及ArCHer的历史感知值估计方法。这些方法依赖于终端奖励或近完全可观测性假设，而ReBel通过显式建模信念状态处理部分可观测性。  
2. **过程监督方法**：如Math-Shepherd、PRIME、Watch Every Step等自动构建步骤级奖励，GiGPO等实现轨迹分组优化。但现有方法依赖当前观测进行分组与奖励估计，易受部分可观测性影响；ReBel提出信念一致性监督与信念感知分组，在潜在状态层面进行优化。  

**二、信念建模与内在动机**  
部分可观测决策领域有检索增强、符号增强、好奇心驱动探索等方法（如随机网络蒸馏）。这些工作虽改善表示学习或探索，但未将信念演化直接与过程级优化耦合。ReBel创新地将信念一致性转化为密集自监督信号，实现策略优化与潜在状态追踪的协同。  

**三、与本文的核心区别**  
ReBel的关键突破在于：①无需外部步骤级标注或验证器，通过预测信念与观测反馈的差异自动生成自监督信号；②在相似信念状态下比较轨迹，获得更稳健的优势估计。相较于依赖终端奖励的GRPO等基线，在ALFWorld和WebShop上成功率提升20.4个百分点，样本效率提升2.1倍。

### Q3: 论文如何解决这个问题？

ReBel通过将策略生成分解为信念-思考-行动（Belief-Think-Action）三阶段来解决问题。核心架构包括：1）显式信念状态建模：将部分可观测环境中的历史信息压缩为结构化的谓词集合\(b_t\)，作为对当前环境状态的符号化估计；2）基于一致性的密集监督：设计信念一致性指标\(C_k(b_t,a_t,o_{t+1})\)，结合可观测性掩码\(m_t\)，将稀疏终端奖励分解为逐步骤的信念一致性奖励\(r_t^{cons}\)；3）延迟验证机制：通过待定信念缓冲区\(\mathcal{U}_t\)存储未验证的信念，当谓词后续可观测时再回溯分配信用；4）信念锚定优势估计：以信念状态\(\tilde{b}\)为锚点构建语义对齐的轨迹组\(\mathcal{G}_S(\tilde{b})\)，在同一信念组内计算标准化优势\(A_S(i,t)\)，解决POMDP中状态不可比导致的孤立样本问题。最终优化目标结合轨迹级优势\(A_E\)和信念锚定步骤级优势\(A_S\)，通过重要性采样与KL正则化更新策略，实现对信念形成、推理过程和动作选择的联合信用分配。创新点在于将信用从动作结果转向信念的因果一致性，利用信念作为语义桥接实现跨轨迹的稳定过程级优化。

### Q4: 论文做了哪些实验？

论文在ALFWorld和WebShop两个部分可观测的长期决策基准上评估了ReBel。实验设置中，所有强化学习方法均使用Qwen2.5-1.5B-Instruct作为基础模型，ReBel在强化学习训练前进行了SFT热身启动。对比方法包括闭源前沿模型（GPT-4o、Gemini-2.5-Pro）、基于提示的开源代理（Qwen2.5、ReAct、Reflexion）、以及基于强化学习的基线（PPO、RLOO、GRPO、GiGPO变体）。主要结果方面，ReBel在ALFWorld上取得了93.2±4.1%的总体成功率，在WebShop上达到75.1±2.7%，分别比最强回合级基线GRPO高出20.4和18.3个百分点；比最强步骤级基线GiGPO$_{w/o std}$高出7.1和7.7个百分点。样本效率方面，ReBel仅需约35次训练迭代即可达到GRPO的最终性能，实现了约2.1倍的样本效率提升。消融实验（从GRPO到完整ReBel逐步添加模块）表明，结构化表示（B1）、细粒度信用分配（B2）和一致性监督（B3）的协同作用带来了主要性能提升。此外，ReBel将平均回合长度从约29.9步减少到9.2步，实现了3.2倍的缩减，并以约1.6倍更少的环境交互步数达到85%的展幵成功率。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来探索点主要集中在以下方面：首先，当前信念状态主要基于文本历史的简单总结，未来可探索更复杂的信念表示（如结构化知识图谱或隐空间表征）以建模深层因果关系。其次，信念一致性监督假设模型预测与观测反馈的偏差能提供有效信号，但在高随机性环境中这种偏差可能引入噪声，需设计自适应阈值或混淆感知机制来过滤噪声。第三，当前基于信念的分组依赖于硬聚类，未来可研究软分组或动态调整分组粒度的策略，以捕获任务中的多尺度语义阶段。此外，可尝试将ReBel扩展到多模态或具身智能场景，其中信念状态需融合视觉、语言等多源信息。最后，探索如何将信念一致性奖励与更细粒度的技能学习（如option发现）结合，进一步提升长时域任务中的样本效率与泛化能力。

### Q6: 总结一下论文的主要内容

ReBel（Reward Belief）提出了一个解决部分可观测环境下长周期智能体任务中信用分配难题的新框架。其核心问题是：延迟奖励和信念漂移导致中间决策的因果贡献难以评估。方法上，ReBel显式建模结构化信念状态以总结交互历史，通过信念一致性监督将信念预测与观测反馈的差异转化为密集的自我监督信号，无需外部逐步骤标注；同时采用信念感知分组，在相似信念状态下比较轨迹，得到更稳健、低方差的优势估计。在ALFWorld和WebShop基准上，ReBel使用1.5B参数模型，任务成功率分别比强基线GRPO提升20.4和18.3个百分点，样本效率提升2.1倍。该工作标志着从纯结果驱动优化向深层过程级对齐的重要转变，证明信念感知的自我监督是实现长周期部分可观测环境下可靠决策的有效路径。
