---
title: "Helix: A Dual-Helix Co-Evolutionary Multi-Agent System for Prompt Optimization and Question Reformulation"
authors:
  - "Kewen Zhu"
  - "Liping Yi"
  - "Zhiming Zhao"
  - "Xiang Li"
  - "Qinghua Hu"
date: "2026-03-20"
arxiv_id: "2603.19732"
arxiv_url: "https://arxiv.org/abs/2603.19732"
pdf_url: "https://arxiv.org/pdf/2603.19732v1"
categories:
  - "cs.MA"
tags:
  - "Multi-Agent System"
  - "Prompt Optimization"
  - "Question Reformulation"
  - "Co-Evolutionary Framework"
  - "Automated Prompt Engineering"
  - "Agent Collaboration"
  - "Multi-Agent Architecture"
relevance_score: 8.0
---

# Helix: A Dual-Helix Co-Evolutionary Multi-Agent System for Prompt Optimization and Question Reformulation

## 原始摘要

Automated prompt optimization (APO) aims to improve large language model performance by refining prompt instructions. However, existing methods are largely constrained by fixed prompt templates, limited search spaces, or single-sided optimization that treats user questions as immutable inputs. In practice, question formulation and prompt design are inherently interdependent: clearer question structures facilitate focused reasoning and task understanding, while effective prompts reveal better ways to organize and restate queries. Ignoring this coupling fundamentally limits the effectiveness and adaptability of current APO approaches. We propose a unified multi-agent system (Helix) that jointly optimizes question reformulation and prompt instructions through a structured three-stage co-evolutionary framework. Helix integrates (1) planner-guided decomposition that breaks optimization into coupled question-prompt objectives, (2) dual-track co-evolution where specialized agents iteratively refine and critique each other to produce complementary improvements, and (3) strategy-driven question generation that instantiates high-quality reformulations for robust inference. Extensive experiments on 12 benchmarks against 6 strong baselines demonstrate the effectiveness of Helix, achieving up to 3.95% performance improvements across tasks with favorable optimization efficiency.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动提示优化（APO）领域的一个核心局限：现有方法通常将用户问题视为固定输入，仅优化提示指令，而忽略了问题表述与提示设计之间内在的相互依赖关系。研究背景是，尽管以GPT-4为代表的大语言模型（LLMs）在各种任务上表现出色，但其输出效果同时受用户问题和提示指令的共同影响，因此APO方法被提出来系统性地改进提示效果。现有方法主要有两类：一是基于元提示模板的方法，其模板固定，适应不同任务和推理模式的灵活性有限；二是生成后搜索的方法，其搜索空间通常局限于预定义的提示簇附近，可能错过全局最优解。即使是近期引入多智能体协作的先进方法（如MARS），也仍然只优化提示，而将问题视为不可变的。这种“单边优化”的假设存在根本不足，因为清晰的问题结构有助于模型进行聚焦推理和理解任务，而有效的提示也能反过来指导如何更好地组织和重述问题。忽略这种耦合关系限制了当前APO方法的有效性和适应性。

因此，本文要解决的核心问题是：如何打破这种单边优化的范式，实现问题重述与提示指令的联合优化。为此，论文提出了名为Helix的双螺旋协同进化多智能体系统，通过一个结构化的三阶段框架（包括规划器引导的分解、双轨道协同进化以及策略驱动的问题生成），让专门的智能体在迭代中相互改进和批评，从而同步优化问题表述和提示指令，以提升LLM在多样化任务上的整体性能。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕自动提示优化和多智能体系统两大领域展开。

在**自动提示优化（APO）**方面，早期研究集中于对硬提示的离散优化或对软提示的连续优化。随着大语言模型（LLM）的兴起，研究方向转向优化自然语言指令。APE开创了利用LLM生成并评估候选提示的先河。后续工作主要遵循两种范式：一是“生成-搜索”方法，它在预定义的提示簇内进行局部探索，限制了全局优化能力；二是“元提示”方法，它使用预定义的优化模板来指导改进，但缺乏跨不同任务特性的灵活性。这些现有APO方法的核心局限在于，它们都专注于优化提示指令，而将用户问题视为固定输入，忽略了问题表述与提示设计之间固有的相互依赖关系。

在**基于多智能体的提示优化**方面，LLM驱动的多智能体系统通过协作机制在复杂任务中展现出优势，关键进展包括用于相互批判的辩论机制、基于反思的迭代优化以及用于高层规划的元智能体协调。这些范式已在软件工程、科学发现等领域证明了其强大性能。在此基础上，MARS通过“教师-批评家-学生”架构将多智能体协作应用于提示优化，相比基于模板的方法更具灵活性。然而，它仍维持固定的智能体角色和单向的批判流程，并且仅专注于提示优化本身。

本文提出的Helix系统与上述工作的主要区别在于：它突破了现有APO方法“单边优化”的局限，首次通过“双螺旋共进化”框架，引入提示架构师与问题架构师之间的双向批判与协同迭代，实现了问题重构与提示设计的联合优化。这超越了MARS等仅优化提示或固定问题表述的方法，探索并利用了问题与提示之间内在的耦合关系，从而在优化效果和适应性上取得了显著进步。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Helix的双螺旋协同进化多智能体系统，来解决现有自动提示优化（APO）方法受限于固定模板、搜索空间狭窄以及将用户问题视为不可变输入的单方面优化问题。其核心思想是认识到问题表述与提示设计本质上是相互依赖的，因此采用联合优化的框架。

**核心方法与架构设计：**
Helix的整体框架分为训练和推理两个阶段。训练阶段通过双螺旋协同进化学习最优的问题重构策略 \(Q^*\) 和提示指令 \(P^*\)，推理阶段则将它们应用于未见过的查询。

**主要模块/组件与工作流程：**
1.  **规划器引导的分解**：首先，一个规划器智能体 \(\mathcal{M}_{planner}\) 根据任务描述和训练样本，将联合优化任务分解为一系列耦合的“螺旋目标”序列 \(\mathcal{H}\)。每个目标 \(h_i\) 包含一个问题重构目标 \(g_Q^i\)、一个提示优化目标 \(g_P^i\) 以及描述两者协同作用的连接约束 \(c_i\)。这种分解实现了渐进式、任务自适应的协同进化。
2.  **双轨道协同进化**：这是系统的核心创新。针对每个螺旋目标，系统初始化当前的问题策略和提示，然后进入多轮迭代的“辩论”过程。此过程涉及两个专门化的智能体：
    *   **提示架构师**：负责设计改进的提示草案。
    *   **问题架构师**：负责设计改进的问题重构策略草案。
    两者以对称的方式进行“提议-批判-精炼”的循环：一方提出草案，另一方进行批判并提供反馈；若草案被拒绝，提出方则根据反馈进行精炼，直至被对方接受。这种双向的、迭代的辩论确保了提示和问题策略能够相互促进、共同改进。
3.  **调解员联合验证**：当一轮中提示和问题策略草案均被各自对方接受后，调解员智能体 \(\mathcal{M}_{mediator}\) 对优化对 \((Q_r, P_r)\) 进行联合验证，检查其是否满足三个维度：提示质量、问题重构质量以及两者的协同一致性。只有全部通过，该螺旋目标才算完成，优化结果作为下一阶段的输入。
4.  **策略驱动的问题生成**：在推理阶段，对于每个测试问题 \(x\)，系统使用训练得到的最优重构策略 \(Q^*\)，通过一个**问题生成器**智能体迭代地生成重构后的问题草案。每个草案由一个**问题评判员**智能体进行验证，确保其语义保真、符合策略 \(Q^*\)、清晰度提升且不泄露答案。通过验证的优化问题 \(x^*\) 与优化后的提示 \(P^*\) 一同输入目标大模型，得到最终答案。

**关键技术亮点与创新点：**
*   **联合协同进化范式**：突破了传统APO单维度优化的局限，首次将问题重构与提示设计置于一个统一的、迭代的、相互驱动的框架中进行联合优化。
*   **结构化多智能体辩论机制**：通过规划器分解目标，并设计提示架构师、问题架构师、调解员、生成器、评判员等角色明确、功能专一的智能体，以结构化的辩论和验证流程，系统性地探索联合优化空间。
*   **解耦的训练与推理**：训练阶段学习通用的优化策略对 \((Q^*, P^*)\)，推理阶段将其高效应用于新问题，兼顾了优化效果与效率。
*   **语义一致性与协同约束**：在整个流程中，通过调解员的联合验证和评判员的多维度检查，严格保证了优化后的问题与提示在提升性能的同时，保持与原始任务的语义一致性，并实现有效的协同。

### Q4: 论文做了哪些实验？

实验设置方面，研究者使用GPT-4o实现Helix中的所有智能体，目标LLM在BBH任务上使用GPT-4o，其余基准测试使用Qwen2.5-32B-Instruct。优化运行次数T设为10，每个螺旋目标最多进行R_max=3轮双螺旋协同进化，推理阶段最多进行K_max=3轮生成器-评判器迭代。

数据集涵盖12个多样化基准，包括BBH（含歧义问答、几何形状、形式谬误、毁坏名称、运动理解子任务）、AGIEval中的LSAT-AR、MMLU（含大学生物学、电气工程、市场营销子任务）、MMLU-Pro（含历史、哲学子任务）以及AQuA-RAT数学推理数据集。

对比方法包括：人工提示策略（无提示、思维链CoT）；自动提示优化方法（APE、OPRO、PE2）；以及最先进的多智能体方法MARS。此外，为分析问题重构和提示优化的贡献，论文评估了四种控制配置：仅优化提示（Q + P-Opt）、仅优化问题重构（Q-Opt）、优化问题+固定CoT提示（Q-Opt + CoT）以及完整双优化（Q-Opt + P-Opt，即Helix）。

主要结果：完整Helix（Q-Opt + P-Opt）在12个任务上平均准确率达到80.36%，优于所有基线。相比最强APO方法MARS提升3.95%，相比人工CoT提示提升7.20%。仅提示优化（Q + P-Opt）达到77.75%，已超过MARS 1.34%。关键数据指标：在最具挑战的任务上，Helix在形式谬误（F.F.）任务准确率达94.05%，在LSAT-AR任务达43.48%，均显著领先。

优化效率方面，Helix所需LLM API调用次数比MARS减少约45%，在仅使用1个训练样本时即达到最高准确率。提示效率（PE）在BBH子任务上持续领先，尤其在歧义问答和形式谬误任务上增益显著。消融实验显示，移除规划器（Planner）导致平均性能下降6.41%，移除提示架构师（P-Arch）或问题架构师（Q-Arch）分别下降8.63%和8.09%，验证了各组件必要性。螺旋数量实验表明，性能提升主要发生在前1-2个螺旋，后续收益递减，体现了高效收敛特性。

### Q5: 有什么可以进一步探索的点？

本文提出的Helix系统在联合优化问题重构与提示指令方面取得了显著进展，但其仍存在一些局限性，为未来研究提供了多个探索方向。首先，系统依赖于预设的分解策略和进化轮次，可能无法自适应地处理高度复杂或动态变化的任务，未来可引入元学习或强化学习机制，让系统能自主调整优化结构和迭代深度。其次，当前框架主要针对单轮对话优化，未能充分探索多轮交互中问题与提示的协同演化，可扩展至对话式场景，研究历史上下文对优化过程的影响。此外，实验基于现有基准，缺乏在真实开放域环境中的验证，未来需在更广泛的应用中测试其鲁棒性和泛化能力。最后，系统未深入分析不同任务类型与优化策略的匹配关系，可结合因果推断等方法，建立任务特征与优化模式的关联图谱，进一步提升自适应性和效率。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为Helix的双螺旋协同进化多智能体系统，用于联合优化提示指令和问题重述。核心贡献在于突破了现有自动提示优化（APO）方法的局限——这些方法通常受限于固定模板、狭窄搜索空间或将用户问题视为不可变的单方面优化。论文指出，问题表述与提示设计本质上是相互依赖的：清晰的问题结构有助于模型聚焦推理，而有效的提示则能揭示更好的问题组织方式。

Helix采用一个结构化的三阶段协同进化框架：首先，通过规划器引导的分解将优化任务拆解为耦合的问题-提示目标；其次，在双轨道协同进化中，专用智能体通过迭代的改进与批评，相互促进以产生互补的优化方案；最后，通过策略驱动的问题生成，实例化高质量的问题重述以进行稳健推理。

实验在12个基准测试上与6个强基线对比，结果表明Helix能实现高达3.95%的性能提升，且优化效率较高。这证明了通过协同进化联合优化问题与提示，能显著增强大语言模型的适应性与任务执行效果。
