---
title: "Capability-Aligned Hierarchical Learning for Tool-Augmented LLMs"
authors:
  - "Haotong Yang"
  - "Ting Long"
  - "Yi Chang"
date: "2026-06-08"
arxiv_id: "2606.09371"
arxiv_url: "https://arxiv.org/abs/2606.09371"
pdf_url: "https://arxiv.org/pdf/2606.09371v1"
categories:
  - "cs.AI"
tags:
  - "Tool-Augmented LLM"
  - "Hierarchical Learning"
  - "RLVR (Reinforcement Learning with Verifiable Reward)"
  - "Planner-Executor Alignment"
  - "API-Calling"
  - "Agent Training"
relevance_score: 8.5
---

# Capability-Aligned Hierarchical Learning for Tool-Augmented LLMs

## 原始摘要

Tool learning enables LLMs to invoke external tools to accomplish tasks. Prior studies have demonstrated the effectiveness of a hierarchical structure: a high-level policy handles global planning and decomposes tasks into manageable sub-tasks, and a low-level policy focuses on invoking tools to solve these sub-tasks. However, these works typically optimize the high-level and low-level policies separately, leading to planner-executor misalignment and limiting LLM performance on tool-use tasks. In this paper, we propose a method called Capability-Aligned Hierarchical Learning (CAHL), which leverages RLVR to jointly optimize both policies, enabling better alignment between the high-level planner and the low-level executor. Experiments on constrained tool-use benchmarks (API-Bank and BFCL) and an open-ended environment (Bamboogle) demonstrate the effectiveness of CAHL.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有层次化工具学习（hierarchical tool learning）方法中存在的规划器与执行器不匹配（planner-executor misalignment）问题。在工具学习背景下，大型语言模型（LLM）需要调用外部工具（如API、搜索引擎）来完成复杂任务。现有方法通常采用层次化结构：高层规划器（planner）将用户请求分解为一系列子任务，低层执行器（executor）将每个子任务转化为具体的工具调用。然而，这些方法独立优化规划器和执行器：规划器基于查询生成逻辑正确的子任务序列，却不考虑执行器能否实际完成这些子任务；执行器则独立学习将子任务映射为工具调用。这种独立优化导致**规划器-执行器不匹配**：规划器可能提出理论上合理但不匹配执行器实际工具调用能力的子任务（如粒度过粗或过细），同时执行器也可能无法准确理解规划器的意图。为了解决这一核心问题，本文提出**能力对齐的层次化学习（CAHL）**，通过基于可验证奖励的强化学习（RLVR）联合优化规划器和执行器，使两者相互适应：规划器根据执行器的实际能力调整子任务粒度，执行器则根据规划器的意图调整策略。实验在受限基准（API-Bank、BFCL）和开放环境（Bamboogle）上验证了有效性。

### Q2: 有哪些相关研究？

工具学习领域，早期研究依赖上下文学习，如通过少样本示例和API规范引导LLM调用外部工具。随后，基于大规模指令数据集（如ToolBench、ToolACE、xLAM）的监督微调成为主流，增强了工具调用格式遵循和复杂API执行精度，但泛化到未见工具和复杂多步任务时表现不佳。近期，强化学习方法（如ToolRL）通过交互反馈优化工具使用，引入了细粒度奖励分解以区分格式和语义正确性；ToolZero证明无需SFT预热即可从基础模型激发工具能力；ToolSample则通过动态任务采样和课程学习提升样本效率。

另一类工作是层次化工具使用，采用“规划-执行”范式：高层规划器将用户请求分解为子任务，低层执行器将子任务映射为具体工具调用。现有方法（如Plan-then-Execute）通常独立优化规划器和执行器，导致两者不匹配——规划器生成逻辑合理的子任务但难以被执行器用现有工具实现，或执行器无法对齐规划器意图，造成调用顺序错乱、不完整或冗余。

本文提出的CAHL方法区别于上述工作，通过基于可验证奖励的强化学习联合优化高层和低层策略，解决规划器-执行器对齐问题。与单独优化策略的方法相比，CAHL实现了全局任务分解与局部工具执行的协同，提升了约束工具基准（API-Bank、BFCL）和开放环境（Bamboogle）上的性能。这一方法将强化学习从单层工具优化扩展到层次化策略的联合训练，填补了现有工作中策略对齐的空白。

### Q3: 论文如何解决这个问题？

CAHL 采用分层强化学习框架，通过 RLVR 联合优化高层规划器和低层执行器以解决规划-执行错位问题。核心方法是将工具学习任务分解为两个协同的神经策略：高层策略 π_h 一次性生成全局执行计划 Z，包含有序的子任务序列 [z_1,...,z_k]，每个子任务明确指定所选工具 t_k 及其参数映射；低层策略 π_l 则根据历史反馈 F_{1:k}、当前子任务指令和工具集，生成可执行的工具调用或推理文本。关键技术在于设计了可验证奖励体系和 GRPO 联合优化。高层奖励 R_h 包含参数匹配度 R_(h,param)（检查计划子串是否包含真实工具调用中的参数值）和执行轨迹对齐度 R_(h,exe)（评估低层实际执行结果与真实标签的步级匹配程度），迫使规划者适配执行者的实际能力。低层奖励 R_l 由格式有效性 R_(l,form)（检查特殊标记顺序）、语法合规性 R_(l,syn)（验证参数结构和数据类型）和语义正确性 R_(l,sem)（计算工具名 IoU、参数名交集比和参数值精确匹配）三重约束构成。训练时，双策略各自独立采样候选计划/执行路径，计算组内优势函数进行梯度更新，实现双向对齐：规划者调整指令粒度以适应执行者能力边界，执行者优化策略以更好地完成规划意图。

### Q4: 论文做了哪些实验？

论文在三个基准测试上评估了CAHL方法：BFCL（评估结构化函数调用正确性）、API-Bank（复杂多轮交互工具使用）和Bamboogle（开放式多跳推理）。对比了6种基线方法，包括基础模型（Qwen-2.5-Instruct）和前沿工具学习框架（Tool-N1、ToolRL、ToolSample、EASYTool、TUMIX）。主要结果：CAHL在BFCL上总体准确率达61.10%，在Non-Live AST、Live Acc、Multi Turn和Irrelevance指标上最优；API-Bank总体准确率75.54%，Level 1和Level 3表现最佳；Bamboogle准确率75.2%，超过所有基线。消融实验分析了联合优化的贡献：在BFCL和API-Bank上，CAHL（61.10%/75.54%）优于仅使用低层执行器的LowOnly（59.24%/73.37%）、冻结低层的FreezeLow（50.34%/67.50%）、冻结高层的FreezeHigh（53.30%/73.03%）和单层模型Single-level（56.96%/61.81%）。效率分析显示，CAHL平均每次成功任务仅需1.04次工具调用（低于ToolRL的1.24次），无效调用率16.92%（低于Qwen的28.48%和ToolRL的30.49%），冗余调用率1.51%（低于Qwen的6.53%和ToolRL的11.89%）。案例研究进一步展示了CAHL通过联合优化有效缓解了规划器与执行器之间的不对齐问题。

### Q5: 有什么可以进一步探索的点？

首先，CAHL 的分层架构带来了显著的计算开销，每次低层执行前都需高层规划，增加了推理延迟和训练成本。未来可探索更高效的规划策略，例如通过剪枝或压缩规划步骤来减少冗余，或引入异步执行机制，让规划与执行部分并行，以缓解这一瓶颈。其次，当前方法仅在受限的基准和开放环境中验证，其泛化性有待加强。可以考虑将CAHL扩展到更多样化的工具集或跨领域任务，检验其适应能力。此外，论文使用的RLVR只优化了策略对齐，但未深入探索奖励函数的设计，未来可设计更细粒度的反馈信号，如对工具调用成功率的动态奖励，以进一步提升低层执行器的鲁棒性。最后，当前高层和低层策略的联合优化可能还存在局部最优问题，可尝试引入元学习或多智能体协调思路，让规划更具前瞻性。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为“能力对齐分层学习”（CAHL）的方法，以解决分层工具学习中规划器与执行器之间的失配问题。在工具增强的大型语言模型（LLM）中，高层策略负责全局规划并将任务分解为子任务，低层策略则调用工具执行这些子任务。然而，现有方法通常独立优化这两层，导致规划与执行不一致。CAHL利用可验证奖励的强化学习（RLVR）联合优化高层规划器和低层执行器，使规划生成的子任务与执行器的实际工具调用能力相匹配，同时执行器调整策略以符合规划意图。在受限工具使用基准（API-Bank和BFCL）和开放环境（Bamboogle）上的实验表明，CAHL显著提升了任务性能和执行可靠性。该方法的核心贡献在于解决了分层工具学习中的关键对齐问题，为提升LLM工具使用能力提供了有效方案。
