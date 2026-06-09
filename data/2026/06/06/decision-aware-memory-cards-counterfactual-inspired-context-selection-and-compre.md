---
title: "Decision-Aware Memory Cards: Counterfactual-Inspired Context Selection and Compression for Tool-Using LLM Agents"
authors:
  - "Xinyu Guan"
  - "Qianyang Zhao"
  - "Yuming Deng"
date: "2026-06-06"
arxiv_id: "2606.08151"
arxiv_url: "https://arxiv.org/abs/2606.08151"
pdf_url: "https://arxiv.org/pdf/2606.08151v1"
github_url: "https://github.com/stephen-guan-researcher/CICL"
categories:
  - "cs.AI"
tags:
  - "Tool-using LLM Agent"
  - "Context Selection"
  - "Memory Cards"
  - "Decision-Aware"
  - "SWE-bench"
  - "Agent Benchmark"
  - "Counterfactual"
  - "Context Compression"
  - "Agent Memory"
relevance_score: 8.5
---

# Decision-Aware Memory Cards: Counterfactual-Inspired Context Selection and Compression for Tool-Using LLM Agents

## 原始摘要

Tool-using LLM agents often fail not because relevant text is absent, but because decisive evidence is not selected, compressed, or surfaced at action time. We present CICL, a decision-aware context layer that turns instance evidence into a context graph, routes deterministic, Opus-assisted, Qwen, Codex/GPT-5.5, and Qwen-QLoRA judgments through a shared eight-field schema, scores units by action shift, outcome uplift, necessity, and negative-transfer risk, and packs high-utility evidence as typed memory cards for a budgeted agent. The design separates the measured decision signal from the judge model, so frontier annotation, local surrogates, and lightweight rankers can be compared under one auditable protocol. Empirically, CICL yields a concrete open-benchmark gain while exposing its limits. On 50 SWE-bench Verified file-retrieval instances, direct Qwen3.6-plus reranking of BM25 top-50 candidates raises hit@1 from 0.58 to 0.78 and MRR@10 from 0.634 to 0.790, with all 2,500 judgments parseable. Controlled diagnostics show action-criticality: at budget 120, CICL reaches F1 0.620 on v1 and 0.425 on v3, and removing the top-utility semantic v3 unit collapses F1 to 0.000. Supplementary checks add Qwen-QLoRA agreement over 710 candidates, a small 200-label real-code Opus-assisted signal, and a three-instance patch smoke validating retrieval-to-patch plumbing without claiming official SWE-bench success. RepoBench-R summaries still beat cards, and compact rankers do not yet replace the heuristic. CICL contributes a reproducible measurement and selection layer for decision-critical context, not an end-to-end coding-agent repair claim.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文解决的是工具型大语言模型（LLM）智能体在行动时，因未能有效选择、压缩和呈现关键上下文信息而导致决策失败的问题。现有方法中，长提示词并不能保证关键证据被准确找到或保留，传统的检索评分（如BM25）通常只关注文本相似性，而非证据对智能体后续决策的实际影响。这导致即便相关文本存在，决定性的证据也可能被遗漏。

本文的核心问题是：如何将智能体的上下文选择建模为一个“决策时刻的干预”问题，并据此设计一个决策感知的上下文层（CICL）。具体来说，CICL将每个候选上下文单元视为一次干预，通过评估其对行动转变、结果改善、必要性和负迁移风险的贡献，最终将高效用证据压缩为“决策感知记忆卡”，在令牌预算下提供给智能体。该研究旨在提供一个可复现的测量与选择层，并验证这种基于决策效用的排序信号是否优于传统检索，且在不同模型间具有可比较性。

### Q2: 有哪些相关研究？

### 相关研究

#### 方法类
- **检索与长上下文选择**：本文与稀疏/稠密检索（如Contriever、FAISS）、RAG系列方法（Atlas、HyDE、Self-RAG）及长上下文工作相关。区别在于CICL将检索视为候选生成，而非直接使用，而是通过评分判断每个候选是否改变预期动作。
- **记忆与压缩**：与AutoContext、ACE、ACON等代理记忆与上下文学习方法相近，但CICL采用类型化字段（触发、证据、动作、失败、范围）保留决策信号，而非直接压缩长度。其贡献感知比较基于因果记忆选择（如RepoShapley），但CICL仅将参数高效适配作为诊断工具，而非完整编码代理。

#### 应用与评测类
- **代理系统与基准**：与AutoGen、ChatDev等协作开发代理及SWE-bench代码基准相关。CICL研究这些系统共享的决策层（在动作前判断检索证据是否改变决策），而非提出端到端修复方案。它使用Comparative Supervision和参数高效适配作为诊断机制，不声称独立编码代理性能。

### Q3: 论文如何解决这个问题？

CICL通过引入一个决策感知的上下文层来解决工具型LLM代理在决策时无法有效选择、压缩和呈现关键证据的问题。其核心方法是将实例证据构建为上下文图，通过结构化的八字段评估方案对候选单元进行评分，并打包为类型化的记忆卡供代理使用。

整体框架包含三个主要模块：首先，**上下文图构建**，将仓库或环境中的文件、符号、任务记忆、规则等作为节点，并建立包含关系、相似度、冲突、前提和任务记忆等边，支持词汇和结构检索以及一跳邻居扩展。其次，**决策效用评分**，核心创新在于用决策时的效用函数\(U(c,x)\)替代传统的相关性相似度，该函数分解为四个反事实启发的因果分量：动作变化 (\(\Delta_{act}\))、结果提升 (\(\Delta_{out}\))、必要性 (\(N\)) 和负迁移风险 (\(R\))。这些分量通过固定线性聚合形成最终效用分数，有三种具体实例化方式：确定性代理、Claude-Opus辅助注释以及基于此训练的轻量级线性排序器。最后，**类型化记忆卡打包**，将选中的高效用证据压缩为包含触发条件、证据、行动提示、忽略失败风险和应用范围五个强制字段的紧凑记忆卡，附带诊断性因果分数用于排序，并确保在固定token预算下打包。

关键技术包括：固定聚合函数确保不同评估模型（Opus、Qwen、Codex/GPT-5.5）的可比性；区分后选择压缩和预预算压缩两种模式以避免混淆；使用QLoRA微调Qwen3.5-9B作为开源替代评估器，保持审计可追溯性。主要创新点在于分离了测量到的决策信号与评估模型，使得前沿标注、本地替代和轻量级排序器能在统一可审计协议下进行比较，从而专注于决策关键上下文的可重复测量和选择。

### Q4: 论文做了哪些实验？

论文在四个数据集上进行了实验：SWE-bench Verified（50个实例，2500条Qwen判断，评估文件检索）、Synthetic v1/v3（各250个任务，分别含1400/1800个标签，检验排名机制和预算效果）、RepoBench-R（100个任务，预算60-400，测试压缩效果）以及CodeSearchNet（提供代码搜索背景）。对比方法包括NoContext、FullContext、VanillaRAG、GraphMemory、SummaryMemory、SelfGeneratedExamples、AutoContextKG和OracleGoldContext（仅用黄金ID作为上界）。主要结果：在SWE-bench Verified上，Qwen3.6-plus重排序将BM25的Hit@1从0.58提升至0.78，MRR@10从0.634提升至0.790。在Synthetic v3上，预算120时CICL的F1为0.425，移除最高效用单元后F1从0.245骤降至0.000（随机移除为0.205），显示因果关键性。在RepoBench-R预算120时，卡片压缩比原始选择提升成功率（0.02→0.06），但摘要方法更高（0.11）。Qwen-QLoRA法官在710个候选上的Josn解析率1.000，Top-5 Jaccard为0.592。额外实验包括Opus辅助的200标签真实代码信号和三个实例的补丁功能验证。

### Q5: 有什么可以进一步探索的点？

论文的局限性与未来研究方向主要体现在四个方面。首先，因果性表述不严谨：当前“反事实启发式”评分仅基于观测数据，未通过随机干预识别因果效应，未来可引入do算子或工具变量方法实现结构化因果推断。其次，评估范围有限：缺乏官方SWE-bench补丁生成成功率，且仅验证文件级检索，未来需扩展至完整代码修复流水线。第三，压缩格式与任务不匹配：RepoBench-R上通用摘要优于记忆卡片，提示需设计任务感知的压缩策略，例如结合代码AST结构的上下文剪枝。第四，代理模型与规模瓶颈：Qwen-QLoRA仅在合成分布上达成一致，且诊断任务规模（25-250个）较小；未来可探索更轻量的学习型排序器（如蒸馏LLM的交叉编码器），并利用主动学习在真实代码修复中动态收集反事实标签。此外，记忆卡片的权重分配可引入图注意力机制，使上下文选择对决策信号的响应更加可控。

### Q6: 总结一下论文的主要内容

工具调用型大语言模型代理的失败通常并非缺乏相关文本，而是因为在决策时刻未能选择、压缩或呈现关键证据。为此，本文提出CICL，一个决策感知的上下文层。它首先将实例证据转化为上下文图，然后通过一个共享的八字段模式，对确定性判断、Opus辅助判断、Qwen、Codex/GPT-5.5及Qwen-QLoRA的判断进行路由，并根据动作偏移、结果提升、必要性和负迁移风险对证据单元进行评分。最后，它将高实用性的证据打包为带类型的记忆卡片，供预算有限的代理使用。该设计分离了测量的决策信号与判断模型，使得前沿标注、局部代理和轻量级排序器可以在一个可审计的协议下进行比较。实验表明，CICL在开放基准测试上取得了显著提升，并揭示了其局限性。例如，在SWE-bench验证集的50个文件检索实例上，对BM25前50候选进行直接重排序，将hit@1从0.58提升至0.78，MRR@10从0.634提升至0.790。消融实验显示，删除最高实用性的语义单元会导致F1值骤降至0.000。CICL的贡献在于提供了一个可复现的、针对决策关键上下文的测量与选择层，而非端到端的编码代理修复方案。
