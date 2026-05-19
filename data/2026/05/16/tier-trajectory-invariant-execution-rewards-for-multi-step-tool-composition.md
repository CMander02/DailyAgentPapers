---
title: "TIER: Trajectory-Invariant Execution Rewards for Multi-Step Tool Composition"
authors:
  - "Anay Kulkarni"
  - "ChiaEn Lu"
  - "Dheeraj Mekala"
  - "Jayanth Srinivasa"
  - "Gaowen Liu"
  - "Jingbo Shang"
date: "2026-05-16"
arxiv_id: "2605.16790"
arxiv_url: "https://arxiv.org/abs/2605.16790"
pdf_url: "https://arxiv.org/pdf/2605.16790v1"
github_url: "https://github.com/anaykulkarni/TIER"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM工具使用"
  - "多步工具组合"
  - "强化学习"
  - "奖励函数设计"
  - "执行轨迹不变性"
  - "密集奖励"
  - "组合推理"
  - "DepthBench"
relevance_score: 9.5
---

# TIER: Trajectory-Invariant Execution Rewards for Multi-Step Tool Composition

## 原始摘要

Tool use enables large language models to solve complex tasks through sequences of API calls, yet existing reinforcement learning approaches fail to scale to multi-step composition settings. Outcome-based rewards provide only sparse feedback, while trajectory-supervised rewards depend on annotated reference solutions, penalizing valid alternatives and limiting scalability. We propose TIER: Trajectory-Invariant Execution Rewards, a reward framework that derives supervision directly from function schemas and runtime execution, rather than from reference trajectories. The reward decomposes into format validity, schema adherence, execution success, and answer correctness, providing dense, interpretable sequence-level feedback derived from fine-grained verification of individual steps of tool use. This design allows any valid execution path to receive credit, naturally supporting multiple solution strategies and adapting to evolving tool interfaces. On DepthBench, a compositional benchmark stratified by depth (1 to 6 steps), TIER achieves >90% accuracy across steps, where trajectory-supervised rewards collapse beyond step-4. We further demonstrate consistent gains on benchmarks like BFCL v3 and NestFUL. Ablation studies confirm that all reward components are necessary, highlighting the importance of multi-level supervision for compositional reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在多步工具组合任务中因奖励设计不善而导致的性能崩溃问题。研究背景是，LLM已能通过API调用执行工具任务，但在需要连续调用多个相互依赖的工具（例如“查询航班目的地天气”）时，随着组合深度增加，准确率急剧下降：使用简单的基于结果的奖励（仅当最终答案正确时给予反馈），2步组合任务准确率低于2%，超过4步则降至0%。现有方法的不足主要有两点：一是结果奖励提供的是稀疏、二元的信号，无法为中间步骤（如工具选择、参数指定、执行顺序）提供有效的信用分配；二是基于轨迹的监督奖励需要人工标注参考解，不仅成本高，且会惩罚合法的替代路径（尤其在多步任务中合法路径众多时），同时难以适应工具接口的变更。本文提出的TIER框架旨在解决核心问题：设计一种不依赖参考轨迹、直接从函数签名和运行时执行中获取密集、可解释反馈的奖励函数，使得任何合法的执行路径都能获得合理奖励，从而在深度可达6步的组合任务中稳定维持90%以上的准确率。

### Q2: 有哪些相关研究？

相关研究主要分为三类：**方法类**包括基于提示的CoT/ReAct和微调方法，它们依赖固定工具接口或标注轨迹，缺乏执行反馈；**工具使用的强化学习类**中，Outcome-based奖励仅依赖最终成功信号，PORTool通过回滚树比较分配路径依赖的奖励，ToolRL匹配模型输出与标注轨迹但惩罚有效替代方案。本文TIER直接从函数模式和运行时执行推导奖励，避免了对参考轨迹的依赖，实现轨迹不变性。**多步工具组合评估类**中，NestFUL、ComplexFuncBench等基准未按组合深度分层，而本文使用的DepthBench能测量各深度准确率，揭示奖励失效模式。TIER在DepthBench上超越前两类方法，尤其在深度>4步时仍保持>90%准确率，而轨迹监督奖励在此处崩溃，验证了多层级监督对组合推理的必要性。

### Q3: 论文如何解决这个问题？

本文提出TIER（轨迹无关执行奖励）框架，解决多步工具组合中强化学习的奖励稀疏与轨迹依赖问题。其核心创新在于**完全摆脱参考轨迹**，直接从函数架构和运行时执行中推导奖励信号，从而支持任意有效路径并获得相同奖励。

整体框架包含四个解耦的奖励组件，在序列层面聚合：
1. **格式有效性（R_format∈{0,1}）**：检查生成的抽象语法树（AST）是否结构完整可解析，若失败则后续奖励归零。
2. **架构遵循度（R_parse∈[0,3]）**：细分为工具名称匹配（二值）、参数名称匹配（基于不匹配数扣分，系数λ_p=0.25）、参数类型匹配（同样基于不匹配数扣分），确保每个API调用的结构正确性。
3. **执行成功（R_exec∈{0,1}）**：所有工具调用必须执行成功，因为步骤失败会导致后续依赖失效，采用全有或全无规则。
4. **答案正确性（R_answer∈{0,5}）**：最终输出匹配预期答案时获得高分，权重显著高于其他组件以防奖励黑客。

技术实现上，将工具序列表示为结构化AST，所有组件通过当前函数架构和运行时行为验证。训练采用GRPO风格的策略梯度优化，在组内对奖励进行归一化得到优势值，并结合PPO风格的裁剪目标和每个token的KL正则化（λ_KL=0.04）。该方法天然支持多种解路径：所有能产生正确答案并满足中间有效性的序列获得最大奖励，而不符合的序列则根据不同违反性质获得差异化的梯度信号，从而实现细粒度、可解释的序列级反馈并自动适应工具接口变化。

### Q4: 论文做了哪些实验？

论文在三个基准上进行实验。实验设置采用Qwen3-8B为基础模型，使用上下文长度12,288 tokens的GRPO目标函数，采样8条轨迹计算优势，KL惩罚系数0.04。主要结果为：1) DepthBench（按组合深度0-6步分层的766样本验证集）：TIER在所有深度上达到≥90%准确率，总准确率98.57%（6步深度90%），而基于结果的奖励（Simple-RL）在2步后降至1.25%，轨迹监督奖励（ToolRL）在5-6步降至0%。2) BFCL v3（真实函数调用基准）：TIER以总准确率68.92%超越所有基线（Simple 66.30%、ToolRL 37.27%、SFT 61.47%、基础模型64.31%），尤其在多轮（39.12% vs ToolRL 0.38%）和无关性（87.65% vs ToolRL 0.81%）任务上表现突出。3) NestFUL（嵌套/顺序API组合）：TIER精确匹配准确率0.684，优于ToolRL的0.476；在3-shot ICL设置下达0.75，超过DeepSeek-V3（685B, 0.60）和GPT-4o（0.60）。消融实验显示，仅格式+正确性奖励（Simple）在4步后归零，单独添加执行或解析奖励仍会在5-6步坍塌至0%，只有完整TIER奖励（格式、解析、执行、正确性四组件）在所有深度保持≥90%。

### Q5: 有什么可以进一步探索的点？

TIER的局限性主要体现在对真实工具环境的简化假设上：它假定执行是廉价、可重复且安全的，忽视了随机性、延迟、部分失败、速率限制、成本和不可逆副作用等现实约束。未来研究需在随机和有成本限制的环境中验证其鲁棒性。此外，当前工作限于单轮强化学习与单一模型规模（Qwen3-8B），多轮交互中的迭代诊断与纠错能力以及跨模型尺度的扩展性尚未探索。一个关键改进方向是引入从浅到深的自适应课程学习策略，利用DepthBench的深度分层特性逐步提升组合复杂度。同时，TIER的确定性验证原则可拓展至代码生成、自然语言到SQL等可执行验证领域，实现无需轨迹监督的强化学习。最后，由于硬件限制，当前训练未利用长上下文能力，未来需突破上下文长度瓶颈以处理复杂函数调用轨迹，并通过系统化的奖励权重调节研究提升领域适应性。

### Q6: 总结一下论文的主要内容

这篇论文提出TIER（轨迹不变执行奖励）框架，用于解决大语言模型在多步工具组合任务中的强化学习奖励设计瓶颈。问题在于：结果奖励仅提供稀疏反馈，而基于轨迹的监督奖励会惩罚有效替代方案且难以扩展。TIER方法直接从函数模式与运行时执行中推导奖励，无需参考轨迹，将奖励分解为格式有效性、模式遵循、执行成功和答案正确性四个部分，提供密集、可解释的序列级反馈。主要结论是：在涵盖1至6步工具组合的DepthBench基准上，TIER在所有深度上实现超过90%的准确率，而轨迹监督方法在4步后崩溃。在BFCL v3和NestFUL等基准上也有持续提升。消融实验证实所有奖励组件都是必要的。核心贡献在于通过轨迹无关的细粒度奖励框架，支持多种有效执行路径，自动适应工具接口变化，显著提升了组合推理的可扩展性和鲁棒性。
