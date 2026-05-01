---
title: "From Context to Skills: Can Language Models Learn from Context Skillfully?"
authors:
  - "Shuzheng Si"
  - "Haozhe Zhao"
  - "Yu Lei"
  - "Qingyi Wang"
  - "Dingwei Chen"
  - "Zhitong Wang"
  - "Zhenhailong Wang"
  - "Kangyang Luo"
  - "Zheng Wang"
  - "Gang Chen"
  - "Fanchao Qi"
  - "Minjia Zhang"
  - "Maosong Sun"
date: "2026-04-30"
arxiv_id: "2604.27660"
arxiv_url: "https://arxiv.org/abs/2604.27660"
pdf_url: "https://arxiv.org/pdf/2604.27660v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Context Learning"
  - "Skill Augmentation"
  - "Multi-Agent Self-Play"
  - "Self-Evolving Agent"
  - "Reasoning"
  - "Inference-Time Method"
  - "Agent Architecture"
relevance_score: 9.5
---

# From Context to Skills: Can Language Models Learn from Context Skillfully?

## 原始摘要

Many real-world tasks require language models (LMs) to reason over complex contexts that exceed their parametric knowledge. This calls for context learning, where LMs directly learn relevant knowledge from the given context. An intuitive solution is inference-time skill augmentation: extracting the rules and procedures from context into natural-language skills. However, constructing such skills for context learning scenarios faces two challenges: the prohibitive cost of manual skill annotation for long, technically dense contexts, and the lack of external feedback for automated skill construction, since there is no automatic signal to tell whether a proposed skill is helpful. In this paper, we propose Ctx2Skill, a self-evolving framework that autonomously discovers, refines, and selects context-specific skills without human supervision or external feedback. At its core, a multi-agent self-play loop has a Challenger that generates probing tasks and rubrics, a Reasoner that attempts to solve them guided by an evolving skill set, and a neutral Judge that provides binary feedback. Crucially, both the Challenger and the Reasoner evolve through accumulated skills: dedicated Proposer and Generator agents analyze failure cases and synthesize them into targeted skill updates for both sides, enabling automated skill discovery and refinement. To prevent adversarial collapse caused by increasingly extreme task generation and over-specialized skill accumulation, we further introduce a Cross-time Replay mechanism that identifies the skill set achieving the best balance across representative cases for the Reasoner side, ensuring robust and generalizable skill evolution. The resulting skills can be plugged into any language model to obtain better context learning capability. Evaluated on four context learning tasks from CL-bench, Ctx2Skill consistently improves solving rates across backbone models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文致力于解决语言模型在上下文学习（context learning）场景中面临的技能自动构建难题。研究背景是：许多现实任务要求语言模型从复杂的上下文（如长篇技术文档）中学习新知识并推理，而非仅依赖预训练的参数量知识，这种能力被称为上下文学习。现有的推理时技能增强（inference-time skill augmentation）方法虽有效，但在上下文学习场景中存在两个主要不足：首先，人工标注技能成本极高，因为上下文通常冗长、技术密集且领域特定，要求注释者完全理解复杂文档既费时又昂贵，难以规模化；其次，自动化构建技能也面临障碍，因为像编程或数学题这类任务有明确的执行反馈或标准答案，能用于评估技能质量，但上下文学习任务缺乏外部反馈信号，无法判断提取的技能是否完整且准确地捕捉了上下文知识。本文的核心问题是：如何在不依赖人类标注或外部反馈的情况下，让语言模型能够自主地从复杂上下文中发现、提炼并选择有用的技能，从而提升其在上下文学习任务中的表现。为此，论文提出了Ctx2Skill框架，通过自我对弈的多智能体循环实现技能的自动化演化。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及两类工作。第一类是**上下文学习**研究，指语言模型在复杂上下文中直接学习相关知识并推理的能力。现有工作发现语言模型尚未掌握此能力，且上下文知识格式多样、隐含规则难以直接检索。本文Ctx2Skill旨在通过自动发现可复用的上下文技能来提升模型的上下文学习能力。第二类是**语言模型的技能增强**工作，分为几个子方向：(1) 人工构建技能库，如早期通过人类标注构建知识，但成本高且难扩展；(2) 自动化技能构建方法，如AutoSkill、AutoRefine、CoEvoSkills、EvoSkill、SkillX等，它们从交互轨迹中提取技能，但均依赖外部反馈信号（如执行反馈、任务完成奖励）来评估和改进技能质量，这在上下文学习场景中不可用；(3) 将技能内化为模型参数的方法，如SKILL0和SkillRL，但需要参数访问且牺牲可解释性。与这些工作不同，Ctx2Skill是首个无需人工标注、无需外部反馈、无需参数更新的自进化框架，能直接从复杂上下文本身发现和精炼技能，显著区别于依赖外部信号或参数修改的现有方法。

### Q3: 论文如何解决这个问题？

Ctx2Skill通过一个自演化的多智能体框架，在无需人工标注或外部反馈的条件下，自动从长技术文档中发现、提炼并选择上下文特定的技能。其核心是一个技能驱动的自博弈循环：首先，挑战者（Challenger）基于自身技能集生成探针任务及评分标准；接着，推理者（Reasoner）利用当前技能集尝试解决这些任务；然后，中立的裁判（Judge）输出二元胜负判定，将失败和成功的案例分别路由到两个智能体侧。失败案例触发推理者侧的提议者（Proposer）分析缺失的上下文知识，生成器（Generator）据此更新推理者技能集；成功案例则触发挑战者侧的对应模块，调整挑战者技能集以维持对抗压力。这样，两侧的技能集在迭代中共同演化，自动发现关键知识，无需人工标注或外部反馈。

为防止因挑战者生成越来越极端的任务而导致推理者技能过度特化、丧失泛化能力，该框架还引入了跨时间回放机制。该机制在自博弈过程中，从每次迭代中记录最难失败案例和最简单成功案例，形成代表性子集；然后，在自博弈结束后，用每个候选推理者技能集重新评估这些子集，计算其在硬（失败）和易（成功）案例上的拉普拉斯平滑后求解率的乘积，并选择乘积最大的技能集作为最终结果。这个乘积形式平衡了难度，既避免了因追求高难度而退化基础能力，也防止了只解决简单问题。最终选定的技能集可以在推理时作为系统提示的一部分插入到任何语言模型中，显著提升其在复杂上下文中的学习能力。

### Q4: 论文做了哪些实验？

论文在CL-bench基准上评估了Ctx2Skill框架，该基准包含500个复杂上下文、1,899个任务和31,607条验证规则，覆盖四个类别：领域知识推理、规则系统应用、过程任务执行及经验发现与模拟。实验采用严格的全或无评分标准（仅当所有验证规则通过才视为解决），并使用GPT-5.1作为裁判验证器（与人工一致性超90%）。对比方法为未使用技能增强的原始模型（推理时不增强技能），在7个前沿模型（GPT-5.1、Claude Opus 4.5、Kimi K2.5、GPT-5.2、Gemini 3 Pro、DeepSeek V3.2 Thinking、GPT-4.1）上报告了各类别及总体解决率。主要结果以GPT-4.1为骨干展示了Ctx2Skill相对于Prompting基线的优势：Prompting总体解决率为12.3%（相比于无技能的11.1%，提升+1.2%），但未直接给出Ctx2Skill的数值。实验设置强调了上下文学习任务与长上下文或上下文学习的区别，评估聚焦于模型从全新未见过上下文中提取知识的能力。

### Q5: 有什么可以进一步探索的点？

本文分析了Ctx2Skill框架如何通过自我演化的多智能体循环从上下文中提取技能，但仍存在若干局限性。首先，当前框架依赖“中立评判者”提供二元反馈，但复杂任务中技能有效性难以用简单对错衡量，未来可引入连续评分或人类偏好学习。其次，技能提取可能过度拟合特定上下文，导致泛化性不足，可通过跨任务元学习或多样性正则化改进。第三，Challenger生成极端任务时可能形成对抗性死锁，尽管有重放机制，但技能演化仍可能偏向狭窄分布，未来可加入领域知识或结构化先验。此外，该方法在长文本、技术密集场景计算成本高，可探索分层技能抽象或蒸馏技术减少开销。潜在方向包括：结合检索增强生成，让技能库动态适配新上下文；或将技能树结构融入推理过程，支持组合式泛化。总体而言，该工作为无监督技能发现提供了新范式，但在鲁棒性和效率上仍需突破。

### Q6: 总结一下论文的主要内容

这篇论文提出了Ctx2Skill，一个无需人工标注或外部反馈的自我进化框架，旨在解决语言模型在复杂上下文中的上下文学习难题。该问题定义为使LM能自动从长而专业化的文本中提取规则和程序为自然语言技能，以提升推理能力，但面临手动标注成本高和缺乏自动反馈验证技能质量的挑战。方法上，Ctx2Skill采用多智能体自我博弈循环，包括生成探测任务和评分标准的挑战者、基于技能集解题的推理者，以及提供二进制反馈的评判者。通过失败案例驱动，提议者和生成者智能体自动发现并精炼技能，推动双方共同进化。为防止对抗性崩溃，引入跨时间回放机制选择最佳平衡的技能集。在CL-bench的四个上下文学习任务上，Ctx2Skill持续提升了GPT-4.1、GPT-5.1和GPT-5.2等模型的解题率，证明了自动发现上下文特定技能的有效性和泛化能力。
