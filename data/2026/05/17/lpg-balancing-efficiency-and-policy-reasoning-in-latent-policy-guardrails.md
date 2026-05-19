---
title: "LPG: Balancing Efficiency and Policy Reasoning in Latent Policy Guardrails"
authors:
  - "Nanxi Li"
  - "Zhengyue Zhao"
  - "Chaowei Xiao"
date: "2026-05-17"
arxiv_id: "2605.17329"
arxiv_url: "https://arxiv.org/abs/2605.17329"
pdf_url: "https://arxiv.org/pdf/2605.17329v1"
github_url: "https://github.com/SaFo-Lab/Latent_Policy_Guard"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Safety"
  - "Guardrails"
  - "Latent Reasoning"
  - "Policy Enforcement"
  - "LLM Agent"
  - "Dynamic Policy Adaptation"
  - "Efficient Inference"
  - "Safety Alignment"
relevance_score: 7.5
---

# LPG: Balancing Efficiency and Policy Reasoning in Latent Policy Guardrails

## 原始摘要

Guardrails are a critical safety layer for modern AI systems, but their operating regime is changing. As LLMs are deployed as customized assistants, safety policies are increasingly specified at inference time by users, organizations, or regulatory contexts. This makes safety enforcement fundamentally dynamic: the guardrail should adapt to changing safety policies without retraining. Yet this requirement creates a fundamental tension: faithfully judging complex policy contexts demands reasoning capability, while practical deployment requires low-latency responses. We introduce Latent Policy Guardrail (LPG), a guardrail framework that learnssemantic latent deliberation over dynamic policies. LPG compresses the internal deliberation needed for intent interpretation and policy grounding into continuous states supervised by decision-relevant semantics. At inference time, it generates only a compact verdict anchored to the violated policy clauses, preserving auditability while avoiding the latency of explicit reasoning. Across policy guardrail benchmarks, LPG-4B reaches 84.5% average safety accuracy and 77.9% F1 by compressing deliberation into just 10 latent tokens, outperforming the strongest dynamic baseline while running roughly 11 times faster than Qwen3-4B-Thinking under the single-sample evaluation setup. Code and data are available at https://github.com/SaFo-Lab/Latent_Policy_Guard.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在动态安全策略场景下，AI系统护栏模型（Guardrail）在效率与推理能力之间的矛盾。研究背景是，随着大语言模型（LLM）被部署为定制化助手，安全策略不再固定，而是在推理时由用户、组织或监管环境动态指定。然而，现有方法陷入两难：非推理型护栏（如DynaGuard）速度虽快但表现脆弱——其判定结果会因策略列表的简单排列而大幅波动（精度变化高达7.4%），且无法基于实际违反的条款给出判定，暴露出仅依赖位置特征和内容先验而非真实策略理解的缺陷；而推理型护栏（如GuardReasoner、ThinkGuard）虽通过显式思维链提升了准确性，但推理速度慢了一个数量级以上，难以满足实时审核管线的低延迟需求。因此，本文要解决的核心问题是：如何设计一种护栏框架，使其既能像推理型方法那样深入理解并锚定具体违反的策略条款，实现动态策略下的精准判断，又能具备非推理型方法的低延迟特性，从而在实际部署中平衡准确性与效率。为此，本文提出了潜在策略护栏（LPG），通过将分解的推理步骤压缩为连续的潜在语义表征，在不生成冗长显式推理文本的前提下，生成可审计的、锚定具体条款的紧凑判定结论。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可分为三类：

**1. 方法类（LLM护栏模型）**：包括Llama Guard（固定安全分类微调）、ShieldGemma、Qwen3Guard等需针对新策略重新训练的方法，以及GuardReasoner、ThinkGuard等基于显式思维链的推理方法。本文的区别在于用紧凑的潜在表示替代冗长的文本推理，平衡了精度与效率。

**2. 应用类（动态策略感知护栏）**：DynaGuard将自然语言策略纳入提示，Yufeng-XGuard解耦策略与风险感知实现无重训练更新，AGrail和AgentDoG则聚焦智能体轨迹监控。本文共享其策略感知思想，但专注于高效推理而非显式生成。

**3. 评测类（基准与框架）**：DynaBench作为动态策略护栏的评测基准被提及。本文在相关基准上评估，并比较了与DynaGuard等方法的性能差异。

此外，潜在推理研究（如COCONUT、CODI）展示了语言模型在连续潜在空间的推理能力，但DRAFT仅针对静态策略的端到端二元交叉熵监督，而LPG支持动态策略，并引入阶段对齐的潜在槽、教师蒸馏语义监督及条款锚定罪状等创新。

### Q3: 论文如何解决这个问题？

LPG 的核心方法是设计一个三阶段隐式推理框架，在保持政策推理能力的同时大幅降低延迟。其整体架构包含三个主要组件：

1. **结构化显式推理模板**：模型被约束遵循固定三阶段流程。第一阶段进行意图分析，识别用户真实意图尤其是越狱攻击；第二阶段进行政策分析，仅选择性地评估相关政策条款，避免全量枚举；第三阶段输出紧凑裁决，格式为“safe”或“unsafe, policy n”，可直接解析并锚定到具体违规条款，保证可审计性。

2. **隐式推理压缩**：将前两个显式推理阶段（意图分析和政策分析）压缩为连续隐层表示，而非生成离散词元。具体通过一个投影层将前一隐状态映射为下一隐词元的嵌入，形成连续思维链。只有第三阶段仍保留显式文本输出以保持可解释性。整个推理过程仅需10个隐词元即可完成关键语义推理。

3. **三项创新性监督信号**：为了训练有效的隐层表示，论文设计了三种独特的监督方式。第一，阶段摘要重建损失：要求从隐层表示中重建阶段核心语义内容（如意图摘要或违规理由），通过基础LM的next-token预测实现语义监督。第二，教师隐状态蒸馏：在裁决位置对齐所有层的学生-教师表示，并在阶段边界对齐顶层表示，直接传递决策相关信息。第三，参考推理损失：通过教师完整显式推理序列的交叉熵防止模型遗忘推理能力。

此外，训练数据构建遵循“无重复政策列表”原则，确保模型学习的是语义理解而非位置匹配。整体采用单阶段端到端训练，融合四个损失项，推理时丢弃重建投影器，仅保留轻量隐式推理路径。

### Q4: 论文做了哪些实验？

论文在两类基准上进行了全面实验。**实验设置**：对比方法涵盖指令遵循模型（Qwen3-4B、GPT-4o）、静态护栏（LlamaGuard3-8B、ShieldGemma-9B、GuardReasoner）和动态护栏（DynaGuard-4B/8B）。**数据集**：分布内使用GuardSet-X和增强版DynaBench（含随机打乱和反事实变体）；分布外使用HarmBench、WildGuardTest及PolicyGuardBench。**主要结果**：在分布内基准上，LPG-4B平均安全准确率84.52%，F1分数77.85%，均优于所有动态基线。推理速度是Qwen3-4B-Thinking的约11倍，比GuardReasoner-8B快5.4倍。在分布外，LPG在HarmBench上达96.44% F1，在WildGuardTest上达84.09%，均为最强；在PolicyGuardBench上以77.85% F1略胜DynaGuard-4B（77.02%），仅次于GPT-4o。关键数据指标：LPG-4B在GuardSet-X上准确率96.85%、F1 96.88%；增强DynaBench上准确率72.19%、F1 58.82%。实验表明LPG通过10个潜在令牌压缩推理，实现了效率与策略推理的优异平衡，并展现出强泛化性。

### Q5: 有什么可以进一步探索的点？

基于论文《LPG》的结论，未来可从以下方向探索：**1. 跨模态与多场景扩展**：当前 LPG 仅处理文本策略，可尝试将视频、音频等模态信息编码为连续隐空间，实现多模态动态策略推理。**2. 隐状态的可解释性**：论文提及“10个隐token”仍存在语义可解释性不足的问题，未来可通过注意力可视化或投影到语义空间，让用户理解隐推理的“决策逻辑”。**3. 策略冲突与联合学习**：当多个用户、组织或法规策略共存时，需设计隐空间中的优先级或冲突消解机制。**4. 小模型泛化极限**：LPG-4B在复杂策略上的表现仍弱于大型推理模型，可尝试引入元学习或知识蒸馏，使小模型在动态策略场景下更快泛化。**5. 实时自适应压缩**：当前固定的10个token可能不适用所有策略复杂度，未来可动态调整隐token数量平衡效率与精度。

### Q6: 总结一下论文的主要内容

这篇论文提出了Latent Policy Guardrail (LPG)框架，用于解决动态安全策略下护栏模型的效率与推理能力之间的矛盾。问题定义是：在推理时需根据用户提供的变化策略进行安全判断，但现有方法要么快速但脆弱（依赖位置伪影而非策略内容），要么准确但推理速度慢一个数量级。LPG方法的核心是将策略推理压缩为连续潜在空间的语义化内部思考，通过三个关键设计实现了“语义潜在推理”：阶段对齐的潜在槽（分离意图与策略分析）、语义内容监督（压缩教师摘要而非重构token）、以及在决策相关位置进行隐状态蒸馏。实验表明，LPG-4B仅用10个潜在token即可达到84.5%的平均安全准确率和77.9%的F1分数，比最强动态基线效果更好，同时比Qwen3-4B-Thinking快约11倍。该工作的核心贡献是首次将潜在推理应用于策略驱动的安全审核，证明潜在压缩是连接快速静态分类器与慢速表达性策略推理护栏的实用桥梁。
