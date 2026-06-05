---
title: "Retrospective Harness Optimization: Improving LLM Agents via Self-Preference over Trajectory Rollouts"
authors:
  - "Wenbo Pan"
  - "Shujie Liu"
  - "Chin-Yew Lin"
  - "Jingying Zeng"
  - "Xianfeng Tang"
  - "Xiangyang Zhou"
  - "Yan Lu"
  - "Xiaohua Jia"
date: "2026-06-04"
arxiv_id: "2606.05922"
arxiv_url: "https://arxiv.org/abs/2606.05922"
pdf_url: "https://arxiv.org/pdf/2606.05922v1"
github_url: "https://github.com/wbopan/retro-harness"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent自我优化"
  - "轨迹反馈"
  - "无监督学习"
  - "策略提升"
  - "代码Agent"
  - "工作流优化"
relevance_score: 10.0
---

# Retrospective Harness Optimization: Improving LLM Agents via Self-Preference over Trajectory Rollouts

## 原始摘要

AI agents rely on a harness of skills, tools, and workflows to solve complex problems. Continually improving this harness is essential for adapting to new tasks. However, existing optimization methods typically require ground-truth validation sets, yet such labeled data is difficult to acquire in practical deployment settings. To address this problem, we introduce Retrospective Harness Optimization (RHO), a self-supervised method that optimizes the agent harness using only past trajectories. Specifically, RHO selects a diverse coreset of challenging tasks from past trajectories and re-solves them in parallel. The agent analyzes these rollouts using self-validation and self-consistency, then generates candidate harness updates and selects the most effective one by its own pairwise self-preference. We evaluate RHO across three diverse domains, spanning software engineering, technical work, and knowledge work. Notably, a single optimization round improves the pass rate on SWE-Bench Pro from 59% to 78% without any external grading. Furthermore, our analysis demonstrates that RHO effectively targets prior failure modes. As a result, the optimized harness alters the agent's behavior patterns and sustains higher accuracy during long-horizon sessions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI智能体在缺乏标注验证集的情况下，如何持续优化自身“装备”（即工具、技能、提示和工作流的集合）的问题。研究背景是，AI智能体在复杂任务中依赖其装备，因此持续改进装备对适应新任务至关重要。现有方法（如验证反馈优化）通常需要真实标注的验证集来评估装备更新效果，但在实际部署场景中，获取能准确反映未来任务分布的标注验证集非常困难。相比之下，智能体在运行过程中自然会积累大量未标注的历史轨迹。本文提出的核心问题是：能否仅利用这些无标签的过去轨迹，通过自我回顾分析来优化智能体装备，从而提升未来任务表现？为了解决这一问题，作者提出了回溯式装备优化（RHO），一种自监督方法。RHO的核心思路是从历史任务中选择多样化的有挑战性核心子集，让智能体重新执行并生成多条并行轨迹；随后通过轨迹内的自我验证和轨迹间的自我一致性提取诊断信号，指导装备更新提案的生成；最后利用智能体自身的成对偏好从多个候选装备中选出最优者，整个过程无需任何外部标签或人工反馈。

### Q2: 有哪些相关研究？

相关研究主要分为两类。第一类是**Harness优化**方法，通过编辑提示、程序参数或工作流代码来改进智能体，如LLM-as-optimizer搜索、声明式流水线编译、文本梯度更新和反思式提示进化，以及ADAS和Meta-Harness等让元智能体重写自身代码的方法。这些方法都需依赖带标签的验证指标来指导搜索，而本文提出的RHO无需任何验证反馈，仅通过一次对未标注历史轨迹的回顾性过程即可改进harness。第二类是**智能体自我改进**方法，利用智能体对轨迹的自我判断替代人工标注，如Dynamic Cheatsheet在测试时自我管理可重用策略与代码片段，ReasoningBank从自我判断的成功与失败中提炼推理策略，MemMA协调多智能体记忆周期，以及SkillOS使用强化学习更新技能库。这些方法主要增强智能体的存储器、上下文或技能列表，不涉及harness的其余部分。RHO则优化完整harness，包括可执行工具和指令，而非仅限记忆模块。

### Q3: 论文如何解决这个问题？

RHO通过自我监督的三阶段流程优化智能体工具箱，无需真实标注数据。首先，核心集选择（Coreset Selection）利用行列式点过程（DPP）对历史轨迹进行排序：大语言模型判官为每条轨迹输出难度分数和文本描述，基于描述嵌入的余弦相似度构建核矩阵，并通过参数θ（默认0.7）平衡难度与多样性，选取k条最困难且多样的轨迹作为优化目标。其次，群体展开（Group Rollout）对每个核心任务并行执行G次代理求解，产生多条轨迹后沿两个维度进行自我偏好分析：自我验证（Self-validation）检查轨迹中工具调用错误、错误假设和过早终止等缺陷；自我一致性（Self-consistency）识别不同轨迹间的分歧（如计划矛盾、工具序列差异），将两者合并形成改进指令。最后，最佳N选1（Best-of-N Harness Proposal）基于改进指令并行生成N个候选工具箱，每个候选在核心集任务上重新执行并计算相对于原工具箱的相对优势分数（基于轨迹排序），仅当最高分>0时才保留该更新。RHO的创新点在于：无需外部奖励或人工标注，完全利用智能体自身对轨迹的对比分析生成优化信号；DPP核函数确保覆盖多样化的失败模式；基于群体相对优势的最佳候选选择机制，有效克服了工具箱优化的随机性。实验表明，单轮优化即可在SWE-Bench Pro上将通过率从59%提升至78%。

### Q4: 论文做了哪些实验？

论文在三个基准测试上评估了Retrospective Harness Optimization (RHO)方法：SWE-Bench Pro（软件工程任务）、Terminal-Bench 2（命令行任务）和GAIA-2（知识工作任务）。实验使用Codex agent作为基础框架，采用GPT-5.5高推理配置，核心集大小k=10，平行轨迹采样和框架建议数均为3。主要对比方法包括Dynamic Cheatsheet、ReasoningBank和Sleep-time Compute，均为无需验证反馈的优化方法。关键实验结果：在SWE-Bench Pro上，单轮RHO优化将通过率从59%提升至78%（绝对提升19%），所有基线方法在此基准上均未取得显著提升。与需要验证标签的Meta-Harness对比，在等计算预算（1轮）下，RHO达到78%通过率，而Meta-Harness仅62%；当Meta-Harness扩展至10轮（3.1倍计算量）时达到80%，但仍需依赖标签数据。RHO生成的框架内容包含新工具（如check_build_and_lint）和技能，有效解决了原始框架的典型失败模式（如Go工具链非标准路径、Python缓存清理等），并改变了agent的行为模式，在长时任务中维持更高准确率。

### Q5: 有什么可以进一步探索的点？

RHO的局限性与未来研究方向主要有三点。首先，其“群组回滚”机制要求环境可重置且容忍重复尝试，这限制了在一次性或不可逆任务（如实时对话、物理机器人控制）中的应用。未来可探索利用预测模型模拟回滚，或设计仅依赖单次轨迹的变体。其次，RHO的有效性高度依赖“可编辑的提示、技能和工具”，对于端到端模型或硬件接口等无法直接编辑的“黑箱”代理，其优化能力受限。未来可研究如何将RHO与模型微调或可微分工具接口相结合。此外，其对困难且多样核心集的选择虽关键，但DPP权重的手动调参（文中θ=0.5）可能并非最优。可探索自适应或基于梯度的方法动态平衡难度与多样性。最后，消融实验显示自一致性和自验证信号至关重要，但其生成过程仍有歧义，未来可研究更鲁棒的后验评分机制，或引入元认知框架让代理主动质疑自身诊断结果，以减少次优候选的生成。

### Q6: 总结一下论文的主要内容

本文提出了一种名为“回顾式工具集优化”（RHO）的自监督方法，旨在解决LLM智能体在缺乏真实标注数据时如何持续改进其技能、工具与工作流的问题。传统优化方法依赖真实标签验证集，但在实际部署中难以获取。RHO的核心思想是：智能体自身的过往轨迹已包含改进信号。具体而言，RHO首先从历史轨迹中选取多样化且具挑战性的核心任务集，并行重新求解；随后，智能体通过自我验证与自我一致性分析这些新轨迹，自主生成候选工具集更新，并基于自身的成对偏好选择最有效的改进。该方法在软件工程、技术工作和知识工作三个不同领域进行了评估。主要结论显示，仅一轮优化即可使SWE-Bench Pro上的通过率从59%提升至78%，且无需任何外部评分。分析表明，RHO能有效针对先前的失败模式，优化后的工具集不仅改变了智能体的行为模式，还在长周期任务中维持了更高准确率。该工作的意义在于，为智能体在缺乏标注数据的部署环境下实现自我进化迈出了重要一步。
