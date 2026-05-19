---
title: "OProver: A Unified Framework for Agentic Formal Theorem Proving"
authors:
  - "David Ma"
  - "Kaijing Ma"
  - "Shawn Guo"
  - "Yunfeng Shi"
  - "Enduo Zhao"
  - "Jiajun Shi"
  - "Zhaoxiang Zhang"
  - "Gavin Cheung"
  - "Jiaheng Liu"
  - "Zili Wang"
date: "2026-05-17"
arxiv_id: "2605.17283"
arxiv_url: "https://arxiv.org/abs/2605.17283"
pdf_url: "https://arxiv.org/pdf/2605.17283v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "定理证明Agent"
  - "Lean"
  - "Agent训练"
  - "证明生成"
  - "多轮修正"
relevance_score: 9.0
---

# OProver: A Unified Framework for Agentic Formal Theorem Proving

## 原始摘要

Recent progress in formal theorem proving has benefited from large-scale proof generation and verifier-aware training, but agentic proving is rarely integrated into prover training, appearing only at inference time. We present OProver, a unified framework for agentic formal theorem proving in Lean 4, in which failed proof attempts are iteratively revised using retrieved compiler verified proofs and Lean compiler feedback. OProver is trained through continued pretraining followed by iterative post-training: each iteration runs agentic proving, indexes newly verified proofs into OProofs and the retrieval memory, uses repair trajectories as SFT data, and uses unresolved hard cases for RL. OProofs is built from public Lean resources, large-scale proof synthesis, and agentic proving traces, containing 1.77M Lean statements, 6.86M compiler-verified proofs, and serialized trajectories with retrieved context, failed attempts, feedback, and repairs. Across five benchmarks, OProver-32B attains the best Pass@32 on MiniF2F (93.3%), ProverBench (58.2%), and PutnamBench (11.3%), and ranks second on MathOlympiad (22.8%) and ProofNet (33.2%) more top placements than any prior open-weight whole-proof prover.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有形式化定理证明系统中训练与推理之间的不匹配问题。当前的研究背景是，虽然大规模证明生成和验证器感知训练取得了进展，但大多数系统仍主要依赖单次或最优多次的完整证明生成，未能将检索、编译器反馈和迭代修复等智能体能力整合到训练过程中，往往仅在推理时作为试探性启发式方法使用。现有方法的不足在于：其一，现有的公共形式化证明语料库和合成数据集仅包含最终验证通过的证明，缺少失败尝试、检索上下文和编译器诊断等驱动证明修复的关键信息；其二，基于检索和反馈的迭代式证明通常被视为固定证明器的推理时增强手段，而非模型需学会使用的策略，导致训练时仅接触最终证明，部署时却面对未经优化的反馈数据分布。本文要解决的核心问题，正是如何构建一个统一框架，使证明器在训练阶段就能学会利用检索到的已验证证明和编译器反馈进行端到端的策略性迭代修正，同时创建包含完整证明构建轨迹的大规模语料库，并通过持续训练实现证明器与语料库的协同进化。

### Q2: 有哪些相关研究？

- **方法类相关工作**：  
  包含两类方向：（1）**证明生成**，如GPT-f、DeepSeek-Prover-V1.5等，将定理证明建模为序列生成，依赖大规模合成数据与验证器反馈；（2）**引导搜索**，如HTPS、LeanDojo、ReProver、InternLM2.5-StepProver、BFS-Prover、Bourbaki等，强调状态空间搜索、前提选择、批评者引导或MCTS式探索。OProver的核心区别在于将**agentic proving**（即依据未成功证据的交互修复）集成到训练全过程，而不仅是推理阶段。

- **整体证明生成类工作**：  
  Goedel-Prover、DeepSeek-Prover-V2、Kimina-Prover、Seed-Prover等展示了通过增强基础模型、长程推理、子目标分解和强化学习提升端到端证明生成性能。OProver在它们基础上，创新性地将**修复轨迹作为SFT数据**，并对未解析困难案例应用RL，迭代索引已验证证明并持续更新检索记忆。

- **核心区别**：  
  现有工作多为单次生成或独立搜索，OProver统一了**agentic迭代修复**（基于编译器反馈和检索到的已验证证明）、**持续预训练**与**迭代后训练**三阶段，并构建了包含修复轨迹的OProofs知识库，因此在不同基准上（如MiniF2F 93.3% Pass@32）取得领先结果。

### Q3: 论文如何解决这个问题？

OProver提出了一个统一框架，通过构建迭代式的智能体证明训练流程来解决形式化定理证明问题。核心是OProofs语料库构建、OProver智能体证明和OProver智能体训练三大组件协同工作。

在整体框架上，OProver将定理证明建模为多轮交互过程。每个轮次中，证明策略π会基于当前状态X_t进行推理，该状态包含目标定理s、检索到的已验证证明R_t、上一轮证明尝试p_{t-1}以及对应的编译器反馈f_{t-1}。策略生成新的证明尝试p_t，经Lean 4编译器验证，失败则继续迭代直到成功或达到轮次上限。

关键技术包括三项创新：一是使用紧凑交互状态，只依赖最近一轮的证明和反馈而非完整历史，保持状态简洁同时保留局部修正信号。二是引入检索增强机制，从持续扩展的OProofs语料库中按语义相似度检索top-k个已验证证明，为策略提供可复用的引理模式、策略结构和证明策略。三是利用编译器原始文本反馈作为细粒度的修正信号，而非投影到人工设计的错误分类，使策略能进行针对性的修订。

训练分两个阶段：先在65B token混合数据上进行持续预训练得到OProver-Base基础模型，再进入迭代式后训练循环。每轮后训练中，模型在未解决问题上执行智能体证明，从回滚轨迹中提取轮级修复样本用于监督微调，对有一定成功率的困难问题使用GSPO强化学习。新验证的证明和修复轨迹不断回注到OProofs，实现模型与语料库的共同进化。

### Q4: 论文做了哪些实验？

OProver在五个Lean 4定理证明基准上进行了评估：MiniF2F（244道高中奥数题）、MathOlympiadBench（360道近期竞赛题）、ProofNet（186道本科级定理）、ProverBench（325道奥数与本科混合题）和PutnamBench（672道Putman竞赛题，最难）。对比方法包括开源推理模型（DeepSeek-V3.2、Kimi-K2.5）和开源证明器（Goedel-Prover-V2、LongCat-Flash-Prover等），主要指标为Pass@32（n=64采样）。核心结果：OProver-32B在MiniF2F（93.3%）、ProverBench（58.2%）和PutnamBench（11.3%）上取得最优，在MathOlympiad（22.8%）和ProofNet（33.2%）上排名第二，整体顶级排名次数超过所有现有模型。消融实验显示，移除多轮编译器反馈（-FB）导致Pass@32下降3-10个百分点（如MiniF2F从93.3%降至88.4%），进一步移除检索增强（-RAG）再降0.5-1.7个百分点，表明迭代修正是主要驱动力。测试时扩展实验表明，固定预算下（B=8到256），OProver-32B在MiniF2F上从87.5%提升至92.8%，最优分配策略因难度而异：中等基准采用R=16轮次，困难基准（PutnamBench）采用R=8轮次。迭代后训练验证了持续改进：OProver-32B经过两轮训练从84.7%提升至93.3%。

### Q5: 有什么可以进一步探索的点？

基于OProver框架的局限性与未来探索点主要有：首先，尽管OProver在多数基准上达到最佳，但其在PutnamBench上的绝对成功率仍低于12%，说明对于极困难问题，现有agentic策略仍存在瓶颈。其次，测试时计算资源的分配存在折中：在低成功率基准上，增大采样宽度比加深修复轮次更有效，这意味着需要自适应的预算分配策略。未来可探索自适应策略，即让模型根据当前问题的难度动态决定是否继续修复或开启新样本。此外，OProver的检索依赖已编译的内容，但无法有效利用人类书写的形式化注释或非形式化数学文本，可探索多模态检索（如结合自然语言交互）以增强推理的上下文理解。最后，OProver的训练迭代依赖于自我生成的修复轨迹，存在过拟合到特定失败模式的风险，引入外部验证器或人类反馈进行课程学习可能是提升泛化能力的重要方向。

### Q6: 总结一下论文的主要内容

OProver提出了一个统一的智能体形式化定理证明框架，解决现有方法中检索和编译器反馈仅作为推理时启发式策略、未融入训练过程导致训练-推理不匹配的问题。该框架将定理证明定义为基于检索和编译器反馈的迭代精炼循环，通过持续预训练和交替进行智能体证明、监督微调、强化学习的迭代后训练来优化策略。论文同时构建了OProofs大规模语料库，包含177万条Lean语句、686万个编译器验证证明及序列化的证明轨迹（含检索上下文、失败尝试、反馈和修复）。实验表明，OProver-32B在MiniF2F（93.3%）、ProverBench（58.2%）和PutnamBench（11.3%）上取得最优Pass@32，在MathOlympiad和ProofNet上排名第二，成为开放权重证明器中最强系统。
