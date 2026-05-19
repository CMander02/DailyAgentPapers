---
title: "SD-Search: On-Policy Hindsight Self-Distillation for Search-Augmented Reasoning"
authors:
  - "Yufei Ma"
  - "Zihan Liang"
  - "Ben Chen"
  - "Zhipeng Qian"
  - "Huangyu Dai"
  - "Lingtao Mao"
  - "Xuxin Zhang"
  - "Chenyi Lei"
  - "Wenwu Ou"
date: "2026-05-18"
arxiv_id: "2605.18299"
arxiv_url: "https://arxiv.org/abs/2605.18299"
pdf_url: "https://arxiv.org/pdf/2605.18299v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.IR"
tags:
  - "搜索增强推理"
  - "强化学习"
  - "过程监督"
  - "自蒸馏"
  - "推理智能体"
  - "查询优化"
relevance_score: 9.5
---

# SD-Search: On-Policy Hindsight Self-Distillation for Search-Augmented Reasoning

## 原始摘要

Search-augmented reasoning agents interleave internal reasoning with calls to an external retriever, and their performance relies on the quality of each issued query. However, under outcome-reward reinforcement learning, every search decision in a rollout shares the same trajectory-level reward, leaving individual queries without step-specific credit. Recent process-supervision approaches address this gap by drawing step-level signals from outside the policy, relying either on a much larger teacher model, or on sub-question annotations produced by a stronger external system. In contrast, we propose SD-Search, which derives step-level supervision from the policy itself through on-policy hindsight self-distillation, requiring neither an external teacher nor additional annotations. In SD-Search, a single model plays two roles that differ only in conditioning: a student that sees only the context available at inference time, and a teacher that additionally conditions on a compact hindsight block summarizing the search queries and final outcomes of a group of rollouts sampled from the same question. Since the teacher knows how each rollout unfolded and which ones succeeded, its query distribution implicitly marks which decisions were worth making, and the student is trained to recover this behavior by minimizing the token-level Jensen--Shannon divergence to the teacher at search-query positions. This layers a dense, step-level signal on top of GRPO's coarse trajectory reward. Crucially, this signal is produced by the policy itself within the standard RL training loop, without external model inference, auxiliary annotation pipeline, or additional training stage.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决搜索增强推理代理中的搜索决策缺乏细粒度监督的问题。现有方法（如AutoRefine）使用结果奖励强化学习训练搜索增强代理，但每个搜索决策只获得相同的轨迹级奖励，无法区分单个查询的好坏，导致模型难以学到最优的搜索策略。近期的过程监督方法（如Thinker和StepSearch）通过引入步骤级信号来弥补这一不足，但它们依赖外部教师模型（如72B模型）或更强大系统（如GPT-4o）生成的子问题标注，这增加了计算成本和外部依赖，并限制了其适用性。本文提出的SD-Search框架通过在线事后自蒸馏，从策略自身导出步骤级监督信号，无需外部教师或额外标注。核心思路是：让同一策略在两种条件下运作——学生模式仅使用推理时可用的上下文，教师模式则额外看到同一问题采样的一组轨迹的紧凑事后摘要（包含搜索查询和最终结果标签）。由于教师知道哪些决策最终成功，其查询分布隐含地标记了哪些值得决策，学生通过最小化查询位置上的token级Jensen-Shannon散度来恢复这种行为。这为GRPO的粗粒度轨迹奖励叠加了密集的步骤级信号，且信号完全由策略在标准RL训练循环中产生，无需外部模型、标注流程或额外训练阶段。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两类。第一类是**方法类**，包括基于结果奖励的搜索增强推理方法，如AutoRefine和MR-Search。它们使用GRPO等强化学习方法，仅根据最终答案的正确性提供轨迹级奖励，但无法对每个搜索查询提供步骤特定的信用分配。本文SD-Search通过提出在线事后自蒸馏，从策略自身派生步骤级监督，无需外部教师或额外标注，相比这些方法取得了显著提升。

第二类是**过程监督类**，如Thinker和StepSearch。Thinker使用72B教师模型将问题分解为子问题，通过监督微调训练学生；StepSearch则利用GPT-4o生成的分解标注推导步骤级奖励。这些方法虽然改进了信用分配，但依赖更强的外部系统。本文SD-Search的不同之处在于，步骤级信号完全来自策略本身的在线事后自蒸馏，无需外部教师、标注或额外训练阶段，在7B规模下平均准确率超过Thinker 2.4个百分点。

此外，本文还与**检索增强生成**相关工作相关，但聚焦于训练模型自主决定何时搜索及查询什么，而非固定检索流程。

### Q3: 论文如何解决这个问题？

SD-Search通过一种新颖的**在线后见之明自蒸馏**框架来解决搜索增强推理中查询级信用分配问题。其核心思想是让同一个策略模型同时扮演两个角色：学生和教师，两者仅在条件上下文上有所不同。

**核心方法**是构建一个**非对称的学生-教师对**。学生（Student）使用标准的推理时上下文（即当前的轨迹前缀）来生成查询分布。教师（Teacher）则在学生上下文的基础上，额外条件于一个**后见之明信息块**（Hindsight Information Block）。这个信息块聚合了同一问题下，策略在GRPO采样过程中产生的所有轨迹（rollouts），并为每条轨迹保留其查询跨度（Search spans）和一个二元结果标签（Correct/Incorrect）。教师通过“看到”不同轨迹的搜索行为及其最终成败，其查询分布隐式地标记了哪些搜索决策是“值得的”。

**架构设计**上，模型采用GRPO作为基础强化学习框架。SD-Search在其轨迹级奖励之上叠加了一个**密集的令牌级自蒸馏损失**。具体地，对于轨迹中的每个搜索查询令牌位置，计算教师分布与学生分布之间的**Jensen-Shannon散度（JSD）**，并将其作为额外的优化目标。为防止教师通过完整的后见之明直接“泄露”答案，方法引入**未来掩码**（Future Masking），只保留搜索跨度而丢弃后续的思考、文档和答案部分。同时，通过**结果条件化**（Outcome Conditioning），让教师从成功和失败的轨迹中对比学习。

**关键技术创新点**包括：1）从策略自身在线采样中产生步骤级监督信号，无需外部教师模型或额外的子问题标注；2）通过JSD损失实现稳定且无偏的分布对齐；3）训练开销仅增加15.5%的推理时长，且推理阶段零额外成本。该方法将粗粒度的轨迹级奖励与细粒度的令牌级监督有效结合。

### Q4: 论文做了哪些实验？

论文在多个基准测试上评估了SD-Search方法。实验设置包括：训练集使用NQ和HotpotQA的联合训练集，评估在七个基准上进行：单跳（NQ、TriviaQA、PopQA）和多跳（HotpotQA、2Wiki、MuSiQue、Bamboogle），报告标准归一化后的Exact Match (EM)准确率。对比方法包括三类：无检索基线（Direct Generation、SFT、R1）、单轮检索基线（Naive RAG）以及多轮检索增强推理方法（包括推理时提示方法：Search-o1、IRCoT；结果奖励RL方法：Search-R1、ReSearch、AutoRefine、MR-Search；以及依赖外部资源的过程监督方法：StepSearch使用GPT-4o子问题标注、Thinker使用72B教师模型）。所有多轮基线共享相同的检索语料库、检索器和检索深度。实现上，SD-Search基于veRL框架和GRPO优化器，主要使用Qwen2.5-3B和Qwen2.5-7B（base和instruct）作为骨干网络，消融实验使用Qwen2.5-3B-Base。

主要结果显示：在3B规模下，SD-Search-Base平均EM为0.428，超过了所有结果奖励基线（如超越AutoRefine-Base 2.3个点，MR-Search-Base 1.4个点），并在统计上与使用72B教师的Thinker-Instruct（0.430）相当。在多跳基准上优势更大，例如Bamboogle上超越AutoRefine-Base 5.8个点。在7B规模下，SD-Search-Instruct平均EM为0.476，超越MR-Search-Base 1.6个点，AutoRefine-Base 2.1个点，并超越Thinker-Instruct（0.452）2.4个点。消融实验表明：移除未来掩码导致3.0个点下降，移除结果标签损失1.4个点，而使用当前步文档代替完整的后见块导致最大下降（3.4个点）。

### Q5: 有什么可以进一步探索的点？

SD-Search 的局限性主要在于对二元结果标签的依赖以及多轨迹组信号退化的问题。未来研究可探索以下方向：首先，针对开域生成任务，可引入基于学习模型的偏好分数或多数投票代理来替代二元标签，使方法能应用于更广泛的场景。其次，当轨迹组内结果标签均匀（全成功或全失败）时，后见信号会失效，可通过设计自适应分组策略或引入基于不确定性采样的多样化轨迹生成来缓解这一问题。此外，可考虑将后见信号与过程奖励模型结合，或利用对比学习框架增强后见块中正负样本的区分度。一个更有趣的方向是将SD-Search扩展到多步推理的中间步骤，通过分层后见蒸馏为每个中间查询提供更细粒度的监督信号。

### Q6: 总结一下论文的主要内容

SD-Search提出了一种针对搜索增强推理智能体的强化学习框架。这类智能体在推理过程中会进行内部推理和外部检索，但传统结果奖励强化学习中，同一轨迹内的所有搜索决策共享相同轨迹级奖励，缺乏针对单个查询的步骤级监督信号。现有方法通常依赖外部教师模型或子问题标注来提供步骤级信号。SD-Search的核心贡献在于通过在线事后自蒸馏，从策略自身推导出步骤级监督，无需外部教师或额外标注。具体来说，同一模型扮演两个角色：仅基于推理时上下文的学生，以及额外基于事后块（总结同一问题多次采样的搜索查询和最终结果）的教师。由于教师知道哪些搜索决策最终成功，其查询分布隐式标记了值得做出的决策。通过最小化学生与教师在搜索查询位置上的令牌级Jensen-Shannon散度，将密集的步骤级信号叠加在GRPO的粗粒度轨迹奖励之上。在七个问答基准测试中，SD-Search超越了仅使用结果奖励的基线，并匹配了依赖更大外部系统的过程监督方法，且额外开销仅15.5%，完全包含在标准RL循环内。这项工作为从轨迹级强化学习中提取步骤级信号提供了一种通用方法。
