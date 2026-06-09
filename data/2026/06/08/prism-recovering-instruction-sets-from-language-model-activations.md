---
title: "PRISM: Recovering Instruction Sets from Language Model Activations"
authors:
  - "Gilad Gressel"
  - "Rahul Pankajakshan"
  - "Julia Diament"
  - "Efim Hudis"
  - "Krishnashree Achuthan"
  - "Yisroel Mirsky"
date: "2026-06-08"
arxiv_id: "2606.09563"
arxiv_url: "https://arxiv.org/abs/2606.09563"
pdf_url: "https://arxiv.org/pdf/2606.09563v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent安全"
  - "激活监控"
  - "指令提取"
  - "提示注入检测"
  - "Agent可解释性"
relevance_score: 8.0
---

# PRISM: Recovering Instruction Sets from Language Model Activations

## 原始摘要

As LLMs are deployed as agents, reliable monitoring requires knowing not only what they output, but which instructions are steering their behavior. This is difficult when models infer unintended subgoals, follow contextual cues, or are influenced by prompt injections and hidden objectives. While activation-to-language methods suggest that hidden states can reveal natural-language information, existing approaches are not designed to recover the full set of simultaneous instructions, constraints, prohibitions, and subgoals active in agentic settings. We formalize this problem as instruction set retrieval and introduce PRISM, an activation-conditioned interpreter that decodes hidden states from a frozen target model into a faithful bullet list of active instructions. Unlike prior activation-to-language methods, PRISM is trained to recover instruction sets directly, using judge-guided GRPO to reward covered instructions and penalize unsupported ones. Across benign, constrained, prompt-injection, and hidden-objective settings, PRISM outperforms activation-to-language baselines, especially on security-relevant objectives.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

随着大型语言模型被广泛部署为自主智能体，可靠的监控不仅需要知道模型输出了什么文本，更需要了解当前驱动其行为的指令集。然而，现有方法面临多重挑战：在良性场景中，模型可能误解模糊提示、推断出用户未预期的子目标；在对抗性场景中，模型可能受到直接或间接的提示注入、检索内容中的隐藏指令等影响。传统的基于输入提示的表面检查无法揭示实际引导模型行为的因素。

当前基于激活到语言的方法（如Patchscopes、LatentQA等）虽然能从隐藏状态中恢复自然语言信息，但存在根本性不足：它们或回答关于隐藏状态的任意问题，或生成单一的高层级描述，而非提取并枚举所有活跃指令。这些方法在处理现代智能体场景中普遍存在的多目标并行指令时（如同时包含指令、约束、禁令和偏好），往往只能恢复少量指令、混淆不同约束，甚至产生幻觉。

为此，本文形式化定义了指令集检索问题，即从模型内部激活中恢复当前驱动其行为的完整指令集（包括指令、约束、禁令和子目标），并提出PRISM方法。PRISM是一个激活条件解释器，能直接从冻结目标模型的隐藏状态解码出高保真的指令组合列表，从而解决现有方法在覆盖率和忠实性上的根本缺陷。

### Q2: 有哪些相关研究？

相关研究主要分为两类：探针与隐空间分类器方法、激活到文本的可解释性方法。

在探针与隐空间分类器方面，已有工作证明激活值可编码关于真实性、有害性、欺骗性和越狱意图等属性的可恢复信息。但本文指出，此类方法通常仅返回标量或类别标签，无法恢复完整的指令集合，尤其无法应对分布偏移下的表面线索或逃避策略。本文将其视为证据，证明激活值包含指令相关信息，但重点转向自然语言恢复完整指令集。

在激活到文本的可解释性方面，LatentQA、Activation Oracles、Predictive Concept Decoders和Natural Language Autoencoders等方法展示了激活值可支持自然语言读取。然而，本文指出这些方法存在两个关键不匹配：首先，它们未针对目标提取进行专门训练，开放式问答或概念预测可能丢失或合并指令；其次，其损失函数（如交叉熵）优化的是字符串匹配，而非集合级别的忠实度，无法惩罚遗漏的约束或额外添加的指令。PRISM通过专为指令集恢复设计的训练目标和基于评判的GRPO优化，直接解决上述局限，特别是在多指令共现的智能体场景中表现更优。

### Q3: 论文如何解决这个问题？

PRISM解决指令集检索问题的核心方法是一个两阶段训练的激活条件解释器。整体框架包含一个冻结的目标模型M和一个轻量级解释器φ，后者复用M的基权重，仅添加可学习的激活投影和LoRA适配器。

主要模块包括：1) **激活快照提取**: 从目标模型生成的最后128个token位置提取残差流隐状态Hℓ∈ℝT×d；2) **软前缀投影**: 将激活状态投影到M的输入嵌入空间，作为T个token的软前缀输入；3) **LoRA解释器**: 复用M基权重并结合LoRA适配器，自回归解码指令列表。

关键技术分为两阶段训练：**监督预训练阶段**使用交叉熵损失学习从激活到指令序列的基础映射。**强化学习阶段**采用法官引导的GRPO算法，核心创新在于使用LLM法官对候选指令列表进行结构化语义反馈，计算覆盖率和幻觉指标的标量奖励。奖励函数设计为r = w_inst*Coverage - w_halluc*Hallucination - P_len，其中P_len是双向长度惩罚项，防止奖励黑客行为。GRPO在每组候选列表内计算归一化优势值，跳过低方差或高饱和样本，只更新投影和LoRA参数，保持基模型冻结。该设计使PRISM能够直接优化完整的指令集检索目标，而非表面形式的匹配。

### Q4: 论文做了哪些实验？

论文在四个分布外测试集上评估了PRISM，包括Benign (BN, 250条Alpaca单任务指令)、Behavioral Constraints (BC, 250条角色/风格/格式约束)、Hidden Objectives (HO, 250条隐藏目标指令)和Adversarial Prompts (AP, 250条间接提示注入)。训练集来自UltraChat、IF-Multi-Constraints和IFEval，约28万条记录。对比方法包括LatentQA、Activation Oracles（均基于Qwen3.5-9B重新训练）及原始发布版本，以及仅基于文本的GPT-5.5。主要评估指标为Judge Reward (R)、Coverage (Cvg)和Hallucination Rate (H)。

结果显示，PRISM (含RL)在平均表现上最优：奖励0.736、覆盖率0.745、幻觉率仅0.014。相比之下，最优基线Activation Oracles (Qwen3.5-9B)的奖励为0.532、覆盖率为0.536、幻觉率为0.006。在安全关键场景中，PRISM在AP上奖励从0.468 (无RL)提升至0.649，HO上从0.563提升至0.595；在对抗性子集覆盖率上，PRISM达0.740，远优于基线（如Activation Oracles的0.448）。定性分析表明，PRISM能恢复完整的指令列表，而基线常将其简化为通用摘要并产生幻觉。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要包括：实验仅针对Qwen3.5-9B模型的特定层和激活窗口（第16层，最后128个生成token），未验证跨模型族、跨层或更长轨迹的迁移性；评估基于单次检查点而非多随机种子，缺乏置信区间；训练依赖oracle生成的指令列表和judge语义评分，存在标注边界模糊和隐含指令遗漏问题；测试场景规模有限（约5-7条约束，1000 token提示），远未达到真实代理部署的上下文长度和复杂度。

未来可探索的方向包括：设计跨模型架构的迁移学习框架，使PRISM适应不同参数规模和多模态模型；引入动态激活窗口选择机制，根据任务复杂度自适应调整观测范围；开发多轮对话和长上下文场景下的指令恢复方法，处理随时间扩散的隐含目标；结合强化学习与人类偏好对齐，减少对oracle标注的依赖；将指令恢复结果与下游策略决策（如阻断、升级）联动，构建端到端的安全监控管线。

### Q6: 总结一下论文的主要内容

本论文将LLM作为智能体部署时，关键监测问题从“输出什么”转向“哪些指令在驱动行为”。现有方法难以应对模型推理未明示子目标、上下文线索或提示注入等场景。作者首次形式化定义了“指令集检索”（Instruction Set Retrieval, ISR）问题，旨在从冻结目标模型的隐藏状态中恢复完整的活跃指令集，包括约束、禁令和子目标。为此提出PRISM，一种激活条件解释器，它利用法官引导的GRPO（组相对策略优化）训练，直接解码隐藏状态为忠实的指令清单。该方法奖励覆盖的指令并惩罚无依据的内容。在良性、约束、提示注入和隐藏目标四种场景下，PRISM显著优于基础激活到语言方法，尤其在安全相关的目标上表现突出。论文表明，激活状态编码了可恢复的指令信息，为LLM智能体的透明监测提供了新方向。
