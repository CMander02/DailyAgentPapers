---
title: "Exploring Agentic Tool-Calling Decisions via Uncertainty-Aligned Reinforcement Learning"
authors:
  - "Yijin Zhou"
  - "Linqian Zeng"
  - "Xiaoya Lu"
  - "Wenyuan Xie"
  - "Dongrui Liu"
  - "Junchi Yan"
  - "Jing Shao"
date: "2026-06-05"
arxiv_id: "2606.06976"
arxiv_url: "https://arxiv.org/abs/2606.06976"
pdf_url: "https://arxiv.org/pdf/2606.06976v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Tool Use"
  - "Reinforcement Learning"
  - "Uncertainty Quantification"
  - "Decision Making"
  - "Multi-turn Interaction"
  - "Reward Design"
relevance_score: 9.5
---

# Exploring Agentic Tool-Calling Decisions via Uncertainty-Aligned Reinforcement Learning

## 原始摘要

Large language model (LLM)-based agents often make suboptimal tool-use decisions, including unsupported tool invocation and hallucinated direct responses, which may accumulate errors throughout multi-step interactions. Existing approaches mainly improve these behaviors through inference-time correction or coarse-grained reward signals based on decision outcomes and structured checklists, leaving the uncertainty characteristics of agent decisions underexplored. We observe that decision-oriented reinforcement learning tends to weaken the uncertainty separation between correct and incorrect actions, resulting in overconfident mistakes and weaker exploration signals. Therefore, we propose TRUST, which incorporates uncertainty quantification into reward design as a repulsive force for maintaining uncertainty separation, and labels lightweight key-turn annotations for unified post-training of multi-turn trajectories. Experimental results across diverse tool-use benchmarks show that TRUST consistently enhances both decision quality and agent performance while maintaining more reliable uncertainty estimates during optimization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大型语言模型（LLM）的智能体在工具调用决策中的失败问题。研究背景是，这类智能体通过调用外部工具来执行知识检索、计算和与环境交互等任务，但经常在特定动作步骤出现决策失误，例如在不支持或不需要工具时仍调用工具，或直接在未执行必要工具调用的情况下编造回答。现有方法的不足主要体现在两方面：一是主要依赖推理阶段的后期纠正或基于决策结果与结构化检查表的粗粒度奖励信号来改进行为；二是这些方法未能深入探索智能体决策过程中的不确定性特征。论文的核心观察是，现有的面向决策的强化学习优化会削弱正确与错误动作之间的不确定性分离，导致模型在犯错时过度自信，并且削弱了探索更可靠替代策略的信号。因此，本文要解决的核心问题是：如何设计一种优化方法，既能提升智能体工具调用的决策质量，又能保持正确与错误决策间清晰的“不确定性分离”，从而避免因过度自信导致的错误累积。为此，论文提出了TRUST框架，通过将不确定性量化融入奖励设计，作为维持不确定性分离的“排斥力”，并标注轻量级关键步骤用于多轮轨迹的统一后训练。

### Q2: 有哪些相关研究？

相关工作主要分为两类：

1. **语言智能体不确定性量化（UQ）**：早期研究主要关注输出层面的不确定性，如模型概率、口头置信度和基于采样的信息信号。近期工作则将不确定性扩展到智能体的中间动作、环境观测和多步轨迹中，并用于调控智能体行为，例如在模糊指令下触发澄清、控制记忆与反思、或通过结构化奖励引导探索。与这些主要将不确定性作为事后诊断或行为控制信号的研究不同，本文明确将不确定性集成到策略优化中，通过不确定性感知的奖励对齐决策正确性与模型置信度。

2. **工具调用决策学习与优化**：工具增强型LLM已被广泛研究。近期工作聚焦于决策过程本身，例如智能体是否应调用工具、追问、直接回答或放弃。相关基准（如When2Call）揭示常见失败模式包括不必要的工具调用和直接回答的幻觉。已有工作采用强化学习优化工具调用行为，如使用校准奖励或决策监督。与之对比，本文不仅优化决策正确性，还深入研究了RL如何重塑工具调用策略的不确定性结构，并利用这一点同时提升决策质量和校准效果。

### Q3: 论文如何解决这个问题？

TRUST方法通过不确定性对齐强化学习解决工具调用决策问题，核心创新在于将不确定性量化（UQ）作为奖励设计中的排斥力，以维持正确与错误决策的不确定性分离。整体框架基于GRPO策略优化，包含以下关键组件：

1. **四维动作空间**：定义Direct（直接回答）、Tool（工具调用）、Ask（请求信息）、Unable（无法处理）四种动作，通过结构化输出格式<think>...<a><answer>y</answer>实现动作与响应的统一表示。

2. **不确定性校准奖励**：采用序列困惑度（PPL）作为不确定性度量，计算正确决策与错误决策的PPL边际差m(s)，经sigmoid函数转换为确定性系数c(s)。奖励函数R_UQ由三部分组成：格式奖励R_fmt（确保结构化输出）、答案奖励R_ans（与真实响应一致性）、动作分类奖励R_cls乘以确定性系数c。当c值较小时，R_cls对错误决策施加排斥力，推动政策向低不确定性区域探索。

3. **轨迹级统一训练**：提出轻量级关键轮次标注方法，仅对每个轨迹中不超过2个决策关键轮次标注真实动作和答案，避免重标整个对话。在GRPO训练中，将CM2清单奖励（监督任务完成质量）与稀疏的R_UQ奖励结合：R = R_CM2 + ΣR_UQ，实现任务性能、工具调用效率和幻觉抑制的联合优化。

该方法无需独立评判器（使用结构化输出时），通过不确定性校准驱动政策在错误决策时扩大探索空间，在正确决策时强化确定性，有效改善了工具调用决策的校准性与多步交互的稳定性。

### Q4: 论文做了哪些实验？

论文在三个基准上进行了实验：When2Call（转折级别调用决策）、ToolSandbox和BFCL-V4（多轮工具使用性能）。实验设置包括两类对比方法：封闭源模型（MiniMax-M2.5、GPT-4o-mini、Claude-Sonnet-4）和开源模型（Qwen3系列，包括235B-A22B、30B-A3B、4B-Thinking、8B-Thinking）。对比方法包括训练免费UQ基线（AUQ、SAGE）和训练后方法（GRPO、CM2）。TRUST使用Qwen3-4B-Thinking进行转折级别GRPO训练，用Qwen3-8B-Base进行轨迹级别统一后训练（包含冷启动SFT和统一RL）。

主要结果：在When2Call上，TRUST(4B-Thinking)达到80.83%准确率（Acc Norm），优于第二名SAGE的73.36%，虚假直接答案率(FDAR)仅5.07%，远低于GRPO的24.76%。在BFCL-V4上，TRUST(4B-Thinking)总分48.04%，超过30B-A3B-Instruct的41.00%。在ToolSandbox上，TRUST(8B-Base)总分68.28%，接近235B-A22B-Instruct的69.88%。消融实验显示，移除不确定性排斥奖励c(s)使准确率从80.83%降至72.46%，整体幻觉率从22.90%升至30.49%，证明不确定性正则化是关键贡献。此外，TRUST正确决策与错误决策的困惑度分布IoU从GRPO后的70.21%降至35.29%，恢复了对模型不确定性的分离能力。

### Q5: 有什么可以进一步探索的点？

尽管TRUST框架在工具调用决策上取得了显著效果，但仍存在几个值得深化的方向。首先，当前依赖困惑度进行不确定性估计相对粗糙，未来可探索基于语义一致性或轨迹级的不确定性建模，例如利用模型集成或贝叶斯近似来更精准地量化决策置信度，避免过度自信错误。其次，实验局限于预定义动作空间的文本基准，这限制了在更动态场景下的泛化能力。未来研究可拓展至具身智能体（如机器人操作）或开放世界工具生态系统，其中动作空间未知且交互更复杂。此外，当前轻量级关键轮次标注依赖人工先验，未来可设计自适应标注策略，结合主动学习自动识别信息增益高的决策点。强化学习奖励设计方面，可尝试将不确定性项与探索奖励解耦，或引入对比学习强化正确与错误决策的表示差异，从而在复杂多轮交互中保持更稳健的校准性能。

### Q6: 总结一下论文的主要内容

本文提出了一种基于不确定性对齐的工具调用决策优化框架TRUST，旨在改善基于大语言模型的智能体在多步交互中的工具使用决策。现有方法主要依赖推理时修正或基于决策结果和结构化检查表的粗粒度奖励信号，忽视了智能体决策的不确定性特征。核心创新在于将不确定性量化信息直接融入奖励设计，作为维持正确与错误动作间不确定性分离的排斥力，从而避免过度自信的错误并增强探索信号。方法上，TRUST通过轻量级关键步骤标注统一多轮轨迹的后训练，实现回合级和轨迹级的联合优化。在When2Call、BFCL-V4和ToolSandbox等多个工具使用基准上的实验表明，该方法在优化过程中能保持更可靠的不确定性估计，持续提升决策质量和智能体性能，有效缓解幻觉生成的直接回应和不支持的工具调用行为。该工作揭示了不确定性量化在智能体工具调用决策中的重要作用。
