---
title: "Revisiting DAgger in the Era of LLM-Agents"
authors:
  - "Changhao Li"
  - "Rushi Qiang"
  - "Jiawei Huang"
  - "Chenxiao Gao"
  - "Chao Zhang"
  - "Niao He"
  - "Bo Dai"
date: "2026-05-13"
arxiv_id: "2605.12913"
arxiv_url: "https://arxiv.org/abs/2605.12913"
pdf_url: "https://arxiv.org/pdf/2605.12913v1"
categories:
  - "cs.LG"
tags:
  - "数据聚合"
  - "长程任务"
  - "策略迁移"
  - "监督微调"
  - "强化学习"
  - "智能体训练"
  - "SWE-bench"
relevance_score: 9.5
---

# Revisiting DAgger in the Era of LLM-Agents

## 原始摘要

Long-horizon LM agents learn from multi-turn interaction, where a single early mistake can alter the subsequent state distribution and derail the whole trajectory. Existing recipes fall short in complementary ways: supervised fine-tuning provides dense teacher supervision but suffers from covariate shift because it is trained on off-policy teacher trajectories; while reinforcement learning with verifiable rewards avoids this off-policy mismatch by learning from on-policy rollouts but with only sparse outcome feedback. We address this dilemma by revisiting Dataset Aggregation (DAgger) for multi-turn LM agents: the algorithm collects trajectories through a turn-level interpolation of student and teacher policies, and the student is then trained on these trajectories using supervised labels provided by the teacher. By directly interacting with environments, we expose the model to realistic states likely to be encountered during deployment, thereby effectively mitigating covariate shift. Besides, since the student is learned by mimicking the teacher's behavior, it receives rich feedback during learning. To demonstrate DAgger enjoys the benefits of both worlds, we tested the algorithm to train a software-engineering agent with 4B- and 8B-scale student models. On SWE-bench Verified, our DAgger-style training improves over the strongest post-training baseline by +3.9 points at 4B and +3.6 points at 8B. The resulting 4B agent reaches 27.3%, outperforming representative published 8B SWE-agent systems, while the 8B agent achieves 29.8%, surpassing SWE-Gym-32B and coming within 5 points of stronger 32B-scale agents. Together with consistent gains on the held-out SWE-Gym split, these results suggest the effectiveness of DAgger for modern long-horizon LM agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多轮、长上下文任务中大型语言模型（LLM）智能体训练的核心问题：现有方法在提供密集监督和避免分布偏移之间存在结构性矛盾。研究背景是LLM正被部署为需要多步交互的智能体（如软件工程智能体），其中早期的一个微小错误会改变后续状态分布并导致路径失败。现有方法各有不足：**监督微调（SFT）** 提供密集的教师监督，但完全训练在专家轨迹上，导致“协变量偏移”（covariate shift）——部署时学生模型自身采样产生的状态分布与训练时的专家状态分布不一致；**基于可验证奖励的强化学习（RLVR）** 通过学生自身采样避免了分布偏移，但只提供稀疏的最终结果反馈，且采样成本高；**在线蒸馏（OPD）** 尝试结合两者优势，但面临冷启动瓶颈，即弱学生的早期轨迹容易过早失败，导致教师只能监督失败的前缀而非完整路径，且不兼容黑盒教师模型。为同时实现“在线状态覆盖、密集反馈、低成本采样、冷启动鲁棒及黑盒兼容”，本文重新审视了经典的**数据集聚合（DAgger）** 算法。其核心是：通过逐轮随机混合学生和教师策略来收集轨迹（教师干预概率逐步衰减），使学生暴露于部署时可能遇到的真实状态，从而有效缓解协变量偏移，同时通过模仿教师行为获得密集监督信号。因此，本文要解决的核心问题是：如何设计一种后训练方法，让LLM智能体既能从自身探索的在线分布中学习，又能获得教师提供的密集、可落地的行为指导。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为两类：**应用类**和**方法类**。

**应用类**方面，论文聚焦于SWE（软件工程）任务中的编码Agent。相关工作包括SWE-Bench（基于真实GitHub问题的长期维护任务基准）、以及SWE-agent和OpenHands等具备文件导航、代码编辑等开发者式交互的Agent框架。本文的DAgger训练方法应用于此类Agent，但更侧重于解决训练中的协变量偏移问题。

**方法类**方面，涉及LLM Agent的后训练技术。相关工作包括：监督微调（SFT），提供密集教师监督但受限于离策略的协变量偏移；基于可验证奖励的强化学习，虽通过策略内轨迹避免偏移但仅提供稀疏结果反馈；以及更密集的监督形式如基于量规的反馈和策略内蒸馏（OPD）。本文的DAgger通过**回合级的学生-教师策略插值**，结合**局部教师标签**，实现了策略内状态覆盖与密集教师监督的双赢，区别于OPD依赖脆弱的冷启动学生轨迹，也不同于部分方法在中期切换为专家完成——DAgger更早地通过混合轨迹修正学生诱导状态。

### Q3: 论文如何解决这个问题？

这篇论文通过重新审视并适配数据集聚合（DAgger）算法来解决长程LM Agent的离线策略分布偏移与稀疏奖励困境。核心方法是在多轮交互中，通过学生与教师策略的混合执行来收集轨迹，并为每次访问的状态提供教师标注的密集监督信号。整体框架包含两个关键设计：随机混合策略的轨迹收集和标准的交叉熵训练目标。具体地，论文提出了两种混合策略：1）DAgger式的轮次级混合，在每一轮以概率β_i独立决定执行学生还是教师动作，并在训练过程中逐渐将β_i衰减至0，使模型逐渐暴露于自身造成的状态分布；2）AggreVaTe式的轨迹级混合，先由学生控制一个变长的前缀序列（κ步），再由教师完成剩余轨迹，学生前缀长度随训练逐渐增加。在每次访问状态时，无论由哪个策略执行动作，都会通过教师模型采集对应的标准动作（标签），整个过程保证了数据标签的密集性。训练目标则使用标准的交叉熵损失，让学生的动作分布拟合教师标签。在软件工程Agent的实验中，论文以4B和8B参数的学生模型验证了方法有效性，在SWE-bench Verified上分别提升了+3.9和+3.6个点。核心创新在于：通过状态分布随迭代逐渐从教师分布迁移到学生分布，有效缓解了监督微调中的协变量偏移问题，同时保持了密集的教师监督信号，结合了SFT与RL的各自优势，通过统一的视角与其他方法（SFT、RL、在线蒸馏）进行了对比分析。

### Q4: 论文做了哪些实验？

论文在软件工程智能体任务上系统评估了提出的DAgger风格训练方法，使用Qwen3-4B-Instruct-2507和Qwen3-8B作为学生模型，并以Qwen3-Coder-30B-A3B-Instruct作为固定教师模型。训练数据集为SWE-Gym（2338个实例），保留100个实例作为域内评估集，域外评估使用SWE-Bench Verified（实际报告466个任务的结果）。对比方法包括SFT（教师专家轨迹+拒绝采样）、GRPO（强化学习，在SkyRL-v0子集上训练）和On-policy Distillation（OPD，学生策略下收集轨迹+教师逆KL蒸馏），所有方法在相同OpenHands框架下评估。

主要结果：4B学生模型上，DAgger在SWE-Gym Holdout达17.0%，SWE-Bench Verified达27.3%，分别超过最强基线OPD 1.0和3.9个百分点；8B模型上达19.0%和29.8%，超过OPD 3.0和3.6个百分点。与已发表系统对比，4B DAgger模型（27.3%）超越所有7-8B系统（最强R2E-Gym-7B仅19.0%），8B模型（29.8%）超越SWE-Gym-32B（20.6%），接近32B级顶尖系统。消融实验表明，DAgger在训练数据扩展时更稳定，在3K样本时已优于OPD；逆KL分析证实其有效缓解协变量偏移，训练后KL散度维持在0.10左右，而SFT在后期反弹至0.126。失败模式分析显示，DAgger在保持高提交率（97.9%）的同时，语法/运行时错误率（15.9%）低于SFT（20.3%），且无重复循环提交问题。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在：DAgger的性能依赖于教师策略的质量，若教师策略本身存在偏差或覆盖不足，可能引入次优行为；同时，轨迹插值比例需要手动调整，缺乏自适应机制。未来可从以下方向探索：1）引入动态策略混合策略，根据学生模型的当前表现自动调整教师干预频率，实现更高效的探索-利用平衡；2）结合过程奖励模型进行残差学习，在DAgger提供的密集监督基础上，对教师行为进行更细粒度的价值评估和修正；3）扩展到多智能体协作场景，利用DAgger的轨迹聚合特性处理智能体间的状态分布偏移问题；4）设计更轻量的状态分布校正机制，如基于先验知识的动作空间剪枝或环境态势感知模块，减少对完整教师轨迹的依赖。这些改进有望进一步提升DAgger在更复杂的长时序任务中的泛化能力和样本效率。

### Q6: 总结一下论文的主要内容

本文针对长周期LM智能体在多轮交互中因早期错误导致状态分布偏移的问题，重新审视了数据集聚合（DAgger）方法。现有方法存在互补性缺陷：监督微调提供密集教师监督但受协变量偏移困扰（训练于离策略教师轨迹），而强化学习虽通过在线策略滚动避免偏移但仅提供稀疏结果反馈。DAgger通过层级插值学生与教师策略收集轨迹，并在其上用教师监督标签训练学生，从而直接与环境交互使模型暴露于部署时的真实状态，有效缓解协变量偏移，同时从教师行为模仿中获得丰富反馈。在软件工程智能体任务中（SWE-bench Verified），采用DAgger训练的4B和8B模型分别超越最强后训练基线3.9和3.6个百分点，4B模型（27.3%）超越代表性8B系统，8B模型（29.8%）接近32B级系统。实验表明DAgger兼具在线策略覆盖与密集监督优势，显著提升长周期搜索、编辑和恢复等行为，为LM智能体后训练提供了有效的状态分布校正方案。
