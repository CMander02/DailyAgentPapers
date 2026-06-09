---
title: "ComplexConstraints and Beyond: Expert Rubrics for RLVR"
authors:
  - "Sushant Mehta"
  - "Liudas Panavas"
  - "Edwin Chen"
date: "2026-06-08"
arxiv_id: "2606.09118"
arxiv_url: "https://arxiv.org/abs/2606.09118"
pdf_url: "https://arxiv.org/pdf/2606.09118v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "RLVR"
  - "instruction following"
  - "rubric evaluation"
  - "training signal"
  - "enterprise agentic tasks"
  - "ComplexConstraints"
  - "benchmark"
relevance_score: 7.5
---

# ComplexConstraints and Beyond: Expert Rubrics for RLVR

## 原始摘要

As LLM capabilities advance rapidly, the evaluation methods used to assess them increasingly lag behind. Traditional benchmarks relied on programmatic verification of narrow, surface-level constraints, but real-world instruction following and agentic tasks demand assessment of nuanced, context-dependent behaviors that resist simple scripted checks. We present a systematic analysis of expert-curated rubric-based evaluation as an alternative paradigm, drawing on empirical evidence from two domains: complex instruction following and enterprise agentic tasks. We first articulate five design principles for constructing high-quality rubrics, including Maximum Viable Atomicity, intent-aware criterion design, and iterative LLM-judge calibration. To validate these principles, we introduce ComplexConstraints, a new expert-curated instruction-following dataset in which each prompt is paired with 10-40 atomic rubric criteria. We demonstrate that these expert rubrics are not only better evaluation instruments but also highly effective training signals: training on approximately 1,000 ComplexConstraints examples yields +15.5% improvement for a 4B-parameter model and +12.2% for a 235B-parameter model on instruction following, while single-epoch RL training on a rubric-graded enterprise environment produces gains that transfer to out-of-distribution benchmarks the model was never trained on (+4.5% BFCL, +7.4% Tau2-Bench, +6.8% Tool-Decathlon). Our findings establish that expert-authored rubrics improve both the measurement and the development of frontier LLM capabilities, serving as effective evaluation and RL training signals.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）评估方法严重滞后于模型能力发展的问题。研究背景是：传统基准测试（如IFEval）依赖程序化验证，能检查字数、禁止字符等表面约束，但这种方法有效性有限——模型能产出胡言乱语却仍能通过测试，只要规避特定字符。现有方法的不足在于：它们评估的是狭隘、表面的约束，无法衡量真实世界中复杂的指令遵循和行为控制需求（如多层指令、跨交互的行为约束、专业工作流等），导致基准得分与实际部署能力之间存在严重脱节。核心问题是如何设计更能反映真实任务需求的评估方法，并且使这种评估方法不仅能更有效地衡量模型能力，还能作为训练信号来进一步提升模型能力。因此，本文探索了“专家策划的基于量规（rubric）的评估”这一替代范式，通过将任务成功分解为原子化、可验证的标准来同时解决评估和训练的双重挑战。

### Q2: 有哪些相关研究？

根据论文“Background and Related Work”部分，相关工作可按类别组织如下：

1. **评测方法类**：从程序化验证到基于评分量规的评估是主要演进路径。IFEval 使用25种约束类型的程序化验证；FollowBench 发现模型性能随约束复杂度增加而下降；InFoBench 将复杂指令分解为二元验证问题；ComplexBench 引入了约束组合的分层分类法；AdvancedIF 和 HealthBench 则转向了专家撰写的评分量规。本文的 ComplexConstraints 数据集继承了这些专家设计，但核心区别在于其双重用途：同一套量规既可用于评估，也可作为强化学习的奖励信号。

2. **评测可靠性类**：LLM-as-a-Judge 相关研究关注评估标准的可靠性，如指出评估标准比思维链推理对可靠性更重要，以及受限的单次 LLM 评估局限性。Autorubric 提出了原子化逐标准评估、集成评判和心理测量可靠性指标。本文通过精心设计量规来减少评估歧义。

3. **智能体评测类**：Agent 基准从简化网页界面转向现实执行环境，如 τ-bench/τ²-bench（客服评测）、Toolathlon（108个长时任务）。调查显示 68% 的部署智能体执行少于十步，体现了部署差距。

4. **训练信号类**：强化学习可验证奖励（RLVR）被扩展到基于量规的奖励信号。RIFL 使用微调的量规验证器，VerIF 结合规则和 LLM 验证，RLCF 提取指令专用清单，ToolRL 展示基于 GRPO 的量规奖励可实现工具泛化。本文的直接训练显示，单周期 RL 训练可产生跨分布迁移收益。

5. **并发工作类**：RubricRAG 通过检索领域知识生成推理时量规以降低人工成本。与此不同，ComplexConstraints 贡献在于：专家撰写量规（避免 LLM 生成的语用意图缺失）、高约束密度（每提示 10-40 条标准）、以及明确的双重设计目的（同时作为评估工具和 RL 奖励信号）。

### Q3: 论文如何解决这个问题？

论文通过提出专家设计的评估标准（Expert Rubrics）作为强化学习（RL）的奖励信号来解决当前LLM评估方法滞后的问题。核心方法包含五大设计原则：**最大可行原子性**确保标准反映提示的最小有意义的单元，避免过度分解导致奖励信号失真；**意图感知标准**要求标准体现用户实际意图而非字面表述；**三级标准分类**将标准分为主要意图（核心要求）、额外加分（提升体验但不惩罚未满足）和躲子弹（惩罚错误但不奖励避免），提供非对称奖励信号；**迭代LLM评委校准**通过人机协同验证标准语言的清晰性；**多维度任务分解**将智能体任务分解为完整性、正确性、约束满足和格式合规四个维度。架构上，奖励函数设计为三级标准的加权组合，使用GPT-5-mini作为评委模型，对指令遵循任务采用LoRA微调（约900个单轮任务，每个10-40条标准），对智能体任务采用GRPO算法（每提示16个轨迹）。实验证明，4B模型在指令遵循任务上平均标准通过率提升15.5%，235B模型提升12.2%，且训练后的小模型性能接近未训练的大模型；智能体任务单轮训练后，在未见过的基准测试上BFCL提升4.5%、Tau2-Bench提升7.4%、Tool-Decathlon提升6.8%。创新点在于将专家设计的细粒度评估标准转化为密集的RL奖励信号，实现精确信用分配，克服了二元任务成功或整体偏好判断的局限性。

### Q4: 论文做了哪些实验？

论文在指令跟随和智能体任务两个领域进行了实验。指令跟随实验使用ComplexConstraints数据集（约900个单轮任务，每个任务有10-40条专家标注规则），采用RLVR训练，奖励函数基于主要意图、额外奖励和回避惩罚的规则满足率。对比方法为基线模型（Qwen3-4B和Qwen3-235B）。主要结果：Qwen3-4B的平均规则通过率从57.9%提升至73.4%（+15.5%），Qwen3-235B从73.9%提升至86.1%（+12.2%）。训练后的4B模型接近235B模型的基线性能。这些提升还迁移到Meta的AdvancedIF基准测试上，Qwen3-4B在单轮、系统可控性和多轮上下文分别提升+6.0、+12.4和+7.1个百分点，总体+8.5%。

智能体任务实验使用CoreCraft数据集，对GLM 4.6（357B参数，32B激活）进行单轮GRPO训练，基于规则的奖励信号。主要结果：在保留的CoreCraft任务上提升+11.4%（从25.4%到36.8%）。更重要的是，在训练中未见过的分布外基准上也有显著提升：BFCL Parallel +4.5%（达95.5%）、Tau2-Bench Retail +7.4%（达76.1%）、Toolathlon Pass@1 +6.8%（达25.6%），且Toolathlon的Pass³从9.3%翻倍至17.6%。实验还分析了前沿模型在ComplexConstraints上的表现，即使最强模型（GPT-5.1）完美任务率仅16.55%，揭示了显著的训练空间。

### Q5: 有什么可以进一步探索的点？

**局限性与未来方向**  
1. **专家成本与可扩展性**：当前依赖专家手动构建细粒度rubric（如ComplexConstraints每条含10-40条原子标准），成本高且难以规模化为通用评估框架。未来可探索“种子rubric+主动学习”的半自动生成策略，例如利用LLM生成候选标准再由专家校正，或训练轻量判别器（如RIFL）替代全人工流程。  
2. **任务泛化边界**：虽然rubric在指令遵循和Agent任务中有效，但对需要开放式创意（如文学创作）或高度动态交互（如多轮谈判）的场景，原子化标准可能过度约束。需研究分层rubric设计：顶层定义“柔性目标”（如创意新颖性），底层保留可验证锚点，并通过强化学习动态调整权重。  
3. **训练信号一致性**：单轮RL训练虽提升OOD泛化（如Tool-Decathlon +6.8%），但rubric评分与任务真正目标（如用户满意度）间的对齐度尚未验证。可引入人类偏好排序作为辅助奖惩信号，缓解rubric的“形式正确但语义偏离”风险。  
4. **计算效率**：需探索将专家rubric知识蒸馏为隐式价值函数（如直接预测动作优劣的轻量模型），避免推理阶段反复调用LLM-自我审查，降低部署成本。

### Q6: 总结一下论文的主要内容

本论文提出了一种基于专家设计评分细则（rubric）的评估范式，旨在解决传统可编程验证基准（如IFEval）存在的表面化、脱离实际意图等问题。作者首先阐述了五个设计原则，包括最大可行原子性、意图感知标准设计、迭代式LLM评判校准等。基于这些原则，论文构建了ComplexConstraints数据集，包含约1000条提示，每条提示配有10-40个原子化评分标准。实验表明，这些专家评分细则在评估和训练两方面均表现出色：在指令跟随任务中，使用约1000个ComplexConstraints样本进行强化学习训练，4B参数模型提升15.5%，235B参数模型提升12.2%；在智能体任务中，基于评分细则的单周期强化学习训练产生跨分布迁移增益（BFCL提升4.5%，Tau2-Bench提升7.4%，Tool-Decathlon提升6.8%）。核心结论是，专家设计的评分细则既能作为更有效的评估工具，又能作为高质量的强化学习训练信号，显著提升模型在复杂指令跟随和智能体任务中的能力。
