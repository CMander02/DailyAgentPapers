---
title: "Internalizing Agency from Reflective Experience"
authors:
  - "Rui Ge"
  - "Yichao Fu"
  - "Yuyang Qian"
  - "Junda Su"
  - "Yiming Zhao"
  - "Peng Zhao"
  - "Hao Zhang"
date: "2026-03-17"
arxiv_id: "2603.16843"
arxiv_url: "https://arxiv.org/abs/2603.16843"
pdf_url: "https://arxiv.org/pdf/2603.16843v1"
categories:
  - "cs.AI"
tags:
  - "Agent Training"
  - "Feedback Learning"
  - "Reflective Experience"
  - "Supervised Fine-Tuning"
  - "Long-Horizon Interaction"
  - "Code Agent"
  - "Recovery Agency"
  - "Exploration"
relevance_score: 8.5
---

# Internalizing Agency from Reflective Experience

## 原始摘要

Large language models are increasingly deployed as autonomous agents that must plan, act, and recover from mistakes through long-horizon interaction with environments that provide rich feedback. However, prevailing outcome-driven post-training methods (e.g., RL with verifiable rewards) primarily optimize final success signals, leaving rich environment feedback underutilized. Consequently, they often lead to distribution sharpening: the policy becomes better at reproducing a narrow set of already-successful behaviors, while failing to improve the feedback-grounded agency needed to expand problem-solving capacity (e.g., Pass@k) in long-horizon settings.
  To address this, we propose LEAFE (Learning Feedback-Grounded Agency from Reflective Experience), a framework that internalizes recovery agency from reflective experience. Specifically, during exploration, the agent summarizes environment feedback into actionable experience, backtracks to earlier decision points, and explores alternative branches with revised actions. We then distill these experience-guided corrections into the model through supervised fine-tuning, enabling the policy to recover more effectively in future interactions. Across a diverse set of interactive coding and agentic tasks under fixed interaction budgets, LEAFE consistently improves Pass@1 over the base model and achieves higher Pass@k than outcome-driven baselines (GRPO) and experience-based methods such as Early Experience, with gains of up to 14% on Pass@128.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）作为自主智能体在长视野交互任务中，如何更有效地利用环境反馈来提升其“能动性”或“代理能力”的核心问题。研究背景是LLM正从被动响应者转变为需要在复杂环境中规划、行动并从错误中恢复的自主行动者，例如在代码生成、网页导航等交互式任务中，智能体的成功不仅依赖一次性正确输出，更依赖于根据环境的结构化反馈（如编译错误、无效操作）进行持续决策和错误恢复的能力。

现有方法，特别是基于结果的后训练方法（如带有可验证奖励的强化学习，RLVR），主要存在以下不足：它们通常只优化最终的成功信号（一个标量奖励），而忽略了丰富的环境反馈信息。这导致了一种“分布锐化”现象：策略变得更擅长复现一小部分已经成功的行为，但未能提升基于反馈的代理能力，即无法有效扩展模型在长视野任务中的问题解决覆盖范围（如Pass@k指标）。这种方法偏向于利用模型现有能力，而非探索新行为，使得智能体在测试时严重依赖昂贵的计算（如多次重试、采样投票）来弥补早期错误。

因此，本文要解决的核心问题是：如何让LLM智能体“内化”一种基于反馈的恢复能动性，使其能够主动解读环境反馈，识别轨迹中的错误决策点，并进行针对性的修正，从而将恢复过程本身内化为模型的内在能力，减少对测试时大量采样的依赖。为此，论文提出了LEAFE框架，通过从反思经验中学习，将环境反馈转化为可操作的监督信号，以提升模型在固定交互预算下的长期问题解决能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 基于LLM的智能体研究**：早期工作如ReAct、Reflexion和Tree of Thoughts主要依赖提示工程来激发智能体行为，不更新模型权重。近期，强化学习（特别是RLVR）成为提升推理鲁棒性和长程决策的主流方法，代表工作有DeepSeek-R1、o1以及后续扩展的系统如verl-agent/GiGPO和rLLM。本文的LEAFE框架同样旨在提升智能体的长程交互能力，但区别于这些主要优化最终成功信号的方法，LEAFE更专注于利用并内化环境提供的丰富过程反馈。

**2. 基于可验证奖励的强化学习（RLVR）**：这类方法（如PPO、GRPO、GiGPO）利用可自动验证的信号（如单元测试结果）进行后训练，在数学和编程任务上取得了成功。它们主要优化稀疏的结果奖励。近期研究开始探索更密集的逐步监督。本文指出RLVR等方法可能导致分布锐化，即策略仅擅长重现已成功的行为。LEAFE则通过反思性经验学习来内化“恢复能力”，旨在更有效地利用过程反馈以扩展问题解决能力，从而在Pass@k指标上实现更好提升。

**3. 自我演化的LLM智能体**：这类研究关注智能体如何通过交互和反思自我改进。可分为：（a）外部化学习（如存入提示、记忆或经验库，不更新权重），代表工作有ReasoningBank、FLEX；（b）基于训练的自进化（将交互数据转化为更好的策略或技能），如SKILLRL、EvolveR、Agent0；（c）测试时自改进。本文工作属于第二类，但强调将基于反馈的探索性经验内化到策略权重中，以增强长程自主能力。

**4. 从经验中学习**：这是智能体系统的长期目标。在LLM领域，相关研究要么将经验内化到权重中，要么存储精炼的经验以供检索。例如，EarlyExp通过隐式世界建模和自反思从自生成轨迹中学习；Agent Q结合了MCTS和DPO；HOPE利用事后反事实行动驱动探索；GA-Rollback触发逐步回滚以防止错误传播。与LEAFE最接近的是EvolveR（将轨迹提炼为可重用的战略原则）和GA-Rollback。本文的LEAFE与之区别在于，它明确地定位关键失败点，并将纠正性的回滚经验内化到一个单轮次策略中，专注于从反思经验中学习基于反馈的自主恢复能力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为LEAFE的两阶段框架来解决传统结果驱动方法在长视野交互中未能充分利用环境反馈、导致策略分布窄化的问题。该框架的核心思想是从反思性经验中内化“恢复性能动性”，使智能体能够从错误中学习并拓展其问题解决能力。

整体框架分为两个阶段：经验收集与经验蒸馏。在第一阶段，智能体在探索过程中进行周期性反思，识别轨迹中的次优决策点（记为τ），并将环境反馈总结为可操作的经验摘要e。随后，智能体通过回滚机制回溯到决策点τ，在经验e的指导下生成修订后的动作，从而开启新的执行分支。这一过程采用基于队列的广度优先搜索策略进行管理，构建了一个隐式的回滚经验树，直至达到最大深度或尝试预算耗尽。这种方法的关键创新在于将非结构化的语言反馈转化为可引导策略转变的上下文干预，实现了对丰富反馈的主动利用。

第二阶段的目标是将经验引导的策略改进蒸馏到模型参数中，使模型在测试时无需显式经验即可内化改进。为此，框架构建了两类监督数据进行标准的下一个词元似然训练。一是行为复现：从成功轨迹中采样状态-动作对作为复现数据集，通过最大化成功动作的似然来防止灾难性遗忘，保持基础任务能力。二是经验到策略的蒸馏：这是核心监督部分，针对每个分支事件，将经验e指导下产生的改进动作a_τ'作为反事实目标，但训练时只使用原始历史h_τ和指令q作为条件，最大化a_τ'的似然。其创新点在于将经验增强的决策映射回无经验的上下文，从而扩展模型的内在策略空间，使智能体在未来能自主地从次优状态中恢复。

最终的训练目标联合优化了反事实蒸馏损失和复现损失，通过超参数β平衡。由此产生的蒸馏策略既保留了基本任务能力，又内化了从经验中衍生的纠正策略，从而在固定交互预算下显著提升了Pass@1和Pass@k等成功率指标。

### Q4: 论文做了哪些实验？

论文在多个智能体任务上进行了实验。实验设置方面，使用了Qwen2.5 (7B/72B)和Llama-3/3.1 (8B/70B)系列模型作为基础，并采用verl-agent作为统一的训练和评估框架。数据集包括WebShop（网络购物导航）、ALFWorld（具身常识推理）、ScienceWorld（科学实验）和Sokoban（推箱子规划）这四个交互式基准，以及CodeContests（竞争性编程）基准。对比方法包括：未经任务微调的基础模型（Base）、基于可验证最终奖励的强化学习（GRPO-RLVR）、将早期交互经验转化为监督信号的无奖励学习方法（EarlyExp），以及基于提示构建动态策略库的方法（ACE）。

主要结果以Pass@1（单次尝试通过率）和Pass@128（在128次采样中的最佳通过率）为关键指标进行评估。实验表明，LEAFE方法在几乎所有任务和模型上都显著提升了Pass@128性能，证明了其增强模型探索能力和根本性能上限的有效性。例如，在CodeContests上，使用Qwen2.5-72B模型时，LEAFE的Pass@128达到47.88%，相比GRPO-RLVR的36.97%提升了约10.9个百分点（相对提升显著）；在ALFWorld任务上，使用Llama3.1-8B模型时，LEAFE的Pass@128达到96.43%，优于所有基线。此外，消融实验验证了其核心组件（如基于树的回滚探索和经验到策略的蒸馏）的有效性，并展示了方法在不同模型规模上的良好扩展性以及在分布外泛化上的优势。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在两方面：一是依赖环境提供清晰、可诊断的即时反馈，若反馈模糊、延迟或难以归因，方法效果会下降；二是假设环境可确定性地回滚到早期决策点，这在非确定性或状态复杂的现实场景中难以实现。未来研究可探索以下方向：首先，开发更鲁棒的反馈理解机制，例如利用大模型对稀疏或隐含反馈进行推理与增强，以减轻对高质量反馈的依赖。其次，针对非确定性环境，可结合世界模型或概率推理来近似模拟状态回滚，或设计无需精确回滚的在线修正策略。此外，该方法目前侧重于从失败轨迹中学习修正，未来可考虑与课程学习、探索策略优化结合，主动生成多样化的挑战性情景，以更系统地提升智能体的泛化与适应能力。最后，将反馈学习与因果推断结合，以提升错误归因的准确性，可能进一步强化智能体在复杂长程任务中的自主恢复能力。

### Q6: 总结一下论文的主要内容

论文针对大型语言模型作为自主代理在长程交互中过度依赖最终结果信号、未能充分利用环境反馈的问题，提出了LEAFE框架。其核心贡献在于通过“反思经验”内化基于反馈的自主恢复能力，以提升代理在固定交互预算下的问题解决覆盖范围（如Pass@k）。方法上，代理在探索过程中将环境反馈总结为可操作的经验，回溯至早期决策点并探索修订后的替代路径，随后通过监督微调将这些经验引导的修正蒸馏到模型中。主要结论显示，LEAFE在多种交互式编程和代理任务中，相比基础模型显著提高了Pass@1，并在Pass@k上优于基于结果的基线（如GRPO）及其他经验方法，尤其在较大k值下增益最高达14%，表明其能扩展行为覆盖而非仅仅锐化已有成功模式，增强了代理在反馈中适应与恢复的长期能力。
