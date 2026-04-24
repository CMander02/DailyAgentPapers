---
title: "Efficient Agent Evaluation via Diversity-Guided User Simulation"
authors:
  - "Itay Nakash"
  - "George Kour"
  - "Ateret Anaby-Tavor"
date: "2026-04-23"
arxiv_id: "2604.21480"
arxiv_url: "https://arxiv.org/abs/2604.21480"
pdf_url: "https://arxiv.org/pdf/2604.21480v1"
categories:
  - "cs.AI"
tags:
  - "Agent评估"
  - "用户模拟"
  - "交互测试"
  - "覆盖引导"
  - "分支探索"
  - "多样化探索"
  - "LLM Agent"
  - "效率优化"
relevance_score: 8.5
---

# Efficient Agent Evaluation via Diversity-Guided User Simulation

## 原始摘要

Large language models (LLMs) are increasingly deployed as customer-facing agents, yet evaluating their reliability remains challenging due to stochastic, multi-turn interactions. Current evaluation protocols rely on linear Monte Carlo rollouts of complete agent-user conversations to estimate success. However, this approach is computationally inefficient, repeatedly regenerating identical early prefixes, and often fails to uncover deep failure modes that arise from rare user behaviors.
  We introduce DIVERT (Diversity-Induced Evaluation via Branching of Trajectories), an efficient, snapshot-based, coverage-guided user simulation framework for systematic exploration of agent-user interactions. DIVERT captures the full agent-environment state at critical decision points and resumes execution from these snapshots, enabling reuse of shared conversation prefixes and reducing redundant computation. From each junction, the framework branches using targeted, diversity-inducing user responses, allowing directed exploration of alternative interaction paths.
  By focusing evaluation on semantically diverse and underexplored trajectories, DIVERT improves both efficiency and coverage. Empirical results show that it discovers more failures per token compared to standard linear rollout protocols, while expanding the set of tasks on which failures are identified.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型（LLM）在作为客户交互代理时评估效率低和覆盖率不足的问题。研究背景是LLM正越来越多地部署为多轮对话代理，其行为具有随机性，评估需要多次模拟完整的用户-代理对话以统计成功率。现有方法主要采用“线性蒙特卡洛展开”，即从初始状态重复采样独立随机轨迹。此方法的不足有三点：（1）计算效率低下：反复从头生成对话，导致大量早期前缀（如登录、基本诊断）被重复计算，浪费计算资源；（2）限制了缓存复用：由于每次生成的前缀仅语义相似而非完全相同，无法有效利用KV缓存加速；（3）覆盖率有限：标准用户模拟器倾向于模拟高概率的协作行为，难以暴露由罕见用户行为触发的深层失败模式。核心问题在于现有线性评估范式将本应呈树状结构的对话轨迹视为独立路径，重复生成相同的早期前缀，却无法系统性地探索从关键决策点分支出的不同路径。为此，本文旨在提出一种更高效、覆盖率更高的评估方法。

### Q2: 有哪些相关研究？

相关研究可分为三类。在**评测基准类**工作中，AgentBench、GAIA2和WebArena评估了智能体的通用能力；而τ-bench和τ²-bench专为客服场景设计，包含工具、政策和LLM用户模拟器。本文使用这些基准作为测试平台，但区别于它们依赖的线性Monte Carlo rollout方法。在**用户模拟类**工作中，现有研究从刚性议程规则发展到基于LLM的模拟器，但存在"仁慈偏误"问题。近期非协作式用户模拟器通过建模恶意意图、情感操纵等对抗行为来解决此问题。DIVERT与这些方法正交——它不提出特定的用户策略，而是提供分支评估结构，可整合友好的、对抗的或红队式用户策略。在**评估效率类**工作中，现有基准几乎完全依赖从头开始的Monte Carlo rollout，导致早期对话前缀的冗余计算和深度交互失败模式的低覆盖。Cost-of-Pass分析表明可靠统计需要高昂的token预算。虽然后期出现MCTS等树方法用于训练和推理，但现有评估框架缺乏对应的分支机制。DIVERT通过快照恢复和多样性引导分支直接解决此问题。

### Q3: 论文如何解决这个问题？

DIVERT提出了一种基于用户模拟分支的高效智能体评估框架。核心思想是通过在对话关键节点进行状态快照和分支探索，替代传统的从初始状态开始完整对话rollout方法。

整体框架包含四个阶段：初始rollout与状态快照缓存、关键节点选择、多样性引导的用户响应生成、基于快照的恢复执行。算法首先对每个任务执行R次标准rollout，收集初始轨迹并缓存所有对话节点的完整状态（包括对话历史、智能体状态、工具环境、模拟器上下文和随机种子）。然后从轨迹池中采样轨迹，使用LLM作为节点选择器识别关键节点，该节点需要满足：修改此处的用户响应能在保持任务意图前提下最大程度改变下游智能体行为。

在选定节点后，DIVERT进行多样性引导的用户响应生成：基于完整对话上下文和任务设定，生成K个候选响应。为确保覆盖率，选择与原始响应语义差异最大的候选（基于余弦相似度度量，嵌入使用sentence-transformers模型）。关键创新在于从缓存快照恢复执行而非重新开始整个对话，这使得相同前缀的对话可以重复利用。通过缓存复用和选择性分支，DIVERT显著减少了token消耗（分支开销仅占总成本的0.08%-0.2%），同时提高了失败模式的覆盖率。该方法还可迭代执行，每次分支生成的轨迹可继续作为后续分支的候选，逐步扩展评估覆盖范围。

### Q4: 论文做了哪些实验？

论文在τ-bench基准测试的三个领域（Airline、Retail、Telecom）上评估了DIVERT框架。实验设置包括：使用GPT-OSS-120B和Gemini-2.5-Flash作为评估的指令微调LLM，并以GPT-OSS-120B作为用户模拟器。主要比较方法是标准线性rollout评估（无分支）与DIVERT（分支评估）的对比，两种方法使用相同的token预算和相同的解码参数。

主要实验包括：1）效率指标：每10万Agent token发现的失败轨迹数（Err/100K）。结果显示，在Airline领域，当rollout数为4时，无分支的基线为16.4，而增加8个分支后提升至19.4，效率提升约18%。在所有三个领域和两种模型上，DIVERT都一致地更高效。2）覆盖率指标：发现至少一个失败的独立任务数（Task Failure Count）。在Airline领域，4个rollout时，基线发现40个任务失败，而8个分支后提升至46个。3）消融实验逐步添加三个核心组件：junction chooser (JC)将效率提升至15.1但覆盖率略降至75；添加directed user generation (DG)后效率升至15.8、覆盖率升至80；最后添加diverse response selection (DC)达到16.2和81。4）多样性验证实验表明，最不相似的候选回复比第二、第三相似候选具有更低的语义相似度，且能产生更多样化的下游轨迹。

### Q5: 有什么可以进一步探索的点？

论文核心局限在于当前框架仅对用户回复进行分支，未覆盖工具调用结果或环境动态变化带来的失败模式。未来可拓展至工具输出和环境状态的分支，例如模拟外部API异常或数据库查询失败，以评估智能体在多种反馈下的鲁棒性。另一个方向是改进关键节点的选择机制，当前基于LLM的节点选择器成本较高且可能遗漏关键分岔点，可探索基于语义相似度或困惑度的自动筛选方法，或利用梯度信息识别行为差异最大的决策时刻。多样性度量方面，余弦相似度在稀疏高维语义空间的表现有限，可引入对比学习或基于信息论的距离指标，更精确地推荐探索路径。此外，任务动态变体生成值得深入：当前依赖固定用户回复模板，可通过构造对抗性输入（如故意混淆指令或拒绝协作）系统性地测试智能体边界。最终目标是构建自主收敛的评估循环，让框架根据覆盖率反馈自适应停止分支，平衡效率与故障发现能力。

### Q6: 总结一下论文的主要内容

大型语言模型（LLMs）越来越多地被部署为面向客户的智能体，但其可靠性评估因随机多轮交互而极具挑战性。当前评估协议使用线性蒙特卡洛采样完整对话来估算成功率，这存在计算效率低下的问题：重复生成相同早期前缀浪费资源，且难以暴露罕见用户行为导致的深层失败模式。本文提出DIVERT（基于轨迹分支的多样性诱导评估），一种高效的、基于快照的、覆盖引导的用户模拟框架。DIVERT在关键决策点捕获完整的智能体-环境状态并从这些快照恢复执行，从而重用共享对话前缀并减少冗余计算。在每个分支点，框架通过有针对性、多样性诱导的用户响应进行分支，实现替代交互路径的有向探索。实证结果表明，与标准线性推演相比，DIVERT在每个token上能发现更多失败案例，并扩展了失败被识别的任务集合，显著提升了评估的效率和覆盖范围。这项工作的核心贡献在于将智能体评估从线性思维转向树状结构，通过计算资源重分配实现了更系统、更高效的失败模式发现。
