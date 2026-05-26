---
title: "DarkForest: Less Talk, Higher Accuracy for Multi-Agent LLMs"
authors:
  - "Yi Li"
  - "Songtao Wei"
  - "Dongming Jiang"
  - "Zhichun Guo"
  - "Qiannan Li"
  - "Bingzhe Li"
date: "2026-05-24"
arxiv_id: "2605.25188"
arxiv_url: "https://arxiv.org/abs/2605.25188"
pdf_url: "https://arxiv.org/pdf/2605.25188v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent LLM"
  - "Controlled Communication"
  - "Belief Distribution"
  - "Error Propagation Mitigation"
  - "Reasoning Benchmark"
relevance_score: 9.5
---

# DarkForest: Less Talk, Higher Accuracy for Multi-Agent LLMs

## 原始摘要

Multi-agent LLM systems improve reasoning by combining outputs from multiple agents, but interaction-heavy methods can introduce error propagation and high communication overhead. When agents exchange raw responses or reasoning traces, incorrect intermediate reasoning may be adopted and amplified, leading to confident but wrong consensus; multi-round communication also increases token consumption, latency, and inference cost. In this paper, we propose a controlled-communication coordination framework named DarkForest. DarkForest first keeps agents independent, so each agent produces an answer without seeing the others' outputs. It then parses the raw responses into structured candidate records, groups semantically equivalent candidates into clusters, and estimates a calibrated belief distribution over these clusters using agent reliability, confidence, parse quality, support-pattern reliability, and independence corrections. A coordinator receives only policy-permitted evidence from this belief state with controlled communication. Experiments on six reasoning benchmarks show that DarkForest achieves leading overall quality, improves the strongest baseline by up to 30.7\% on benchmark metrics, and reduces token consumption by up to $6.5\times$ compared with communication-heavy baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多智能体大语言模型（LLM）系统中因不受控信息交换导致的错误传播和高通信开销问题。研究背景是，现有方法通过多个智能体之间的自由对话、角色扮演或多轮辩论等交互方式来提升推理性能，但这些方法存在两大核心不足：第一，**错误传播**——智能体之间共享原始的推理过程或回答后，错误的中间推理可能被后续智能体采纳并放大，导致系统以高置信度收敛到错误答案，且智能体间的一致意见失去了独立验证的价值；第二，**通信开销**——反复的消息交换显著增加了Token消耗、延迟和推理成本，限制了系统的可扩展性。论文通过实验发现，即使初始智能体池中已存在正确候选答案，许多协调方法仍会丢失这些有效证据，这表明问题不在于如何让智能体更多交流，而在于如何控制哪些信息跨越智能体边界。因此，本文要解决的核心问题是：设计一种受控的通信协调框架，通过结构化信念状态和披露策略，仅向协调器暴露策略许可的紧凑证据，在保持或提升准确性的同时大幅降低通信开销和错误放大风险。

### Q2: 有哪些相关研究？

在多智能体LLM系统中，相关工作可分为三类：  
（1）**辩论法**（如Du et al., 2024；CMS-BMA）：智能体间交换完整推理链并多轮修订答案。本文指出这类方法易导致错误传播——当错误推理链具有说服力时，后续智能体会被误导采纳错误结论，且多轮通信带来高令牌消耗与延迟。本文DarkForest通过控制通信策略（仅传递结构化的信念状态而非原始推理链）从根本上避免此问题。  
（2）**聚合法**（如Fottrell et al., 2024；均匀投票）：将多个候选答案通过无权重投票或简单合并生成最终结果。这些方法未建模智能体可靠性、答案解析质量及智能体间依赖性。DarkForest通过引入置信度校准、可靠性加权、独立校正等机制，对候选答案聚类后生成更精确的信念分布。  
（3）**优化效率方法**（如分散式推理、通信剪枝）：仅关注降低通信成本或提升单方面推理质量，未将信息披露本身作为可控设计变量。DarkForest的创新在于将通信内容（结构化信念状态而非原始响应）和通信策略（单轮控制聚合）作为联合优化对象，在保持准确性的同时大幅降低令牌消耗（最高降低6.5倍）。

### Q3: 论文如何解决这个问题？

DarkForest提出了一种受控通信的协调框架，核心方法基于三个设计原则：独立候选生成、校准聚合和受控通信。整体框架由多个独立LLM代理、解析器、聚类模块、信念状态构建器、披露策略、协调器和确定性防护栏组成。

具体流程为：首先，多个代理独立生成候选答案，互不观察对方的输出，避免错误传播和交互开销。然后，解析器将原始响应解析为结构化观测，包括规范化候选表示、置信度、解析有效性等，并过滤无效观测。接着，将语义等价的候选聚合成簇，每个簇记录支持代理的身份模式。关键技术在于校准信念构建：并非简单投票，而是对每个候选簇计算加权证据分数，综合考量代理历史可靠性、支持模式可靠性、解析质量惩罚、代理间相关性折扣和置信度调制。这些校准参数通过离线阶段在已知结果数据上估计得到，不更新模型本身。最后，披露策略仅向协调器暴露策略允许的紧凑证据（如候选标识符、信念摘要），而非完整原始输出，控制通信成本。协调器基于输入和证据产生最终答案。此外，狭窄的确定性防护栏在信念状态强烈支持某个候选且与协调器输出冲突时进行干预，确保强证据不被单次协调调用丢弃。

创新点在于：1) 独立生成避免运行时分依赖；2) 校准聚合通过支持模式和相关性折扣处理代理间相关性；3) 受控通信显著降低token消耗（最高6.5倍），同时提升精度（最高30.7%）。

### Q4: 论文做了哪些实验？

论文在六个推理基准上评估了DarkForest，包括MATH（数学）、HumanEval（代码）、MMLU-Pro（多领域）、GPQA（科学问答）、FinQA（金融）和LegalBench（法律）。实验设置中，DarkForest协调三个独立代理：通用任务使用Qwen2.5-7B-Instruct、Qwen2.5-Coder-7B-Instruct和Mathstral-7B-v0.1；专业任务额外使用finance-Llama3-8B和Saul-7B-Instruct-v1。对比方法包括Debate、Self-Consistency、Refine、ReConcile、Mixture-of-Agent和Graph-of-Agent两种变体。

主要结果：DarkForest在MATH上取得76.80%精确匹配（领先Self-Consistency 5.00点），MMLU-Pro达58.38%（超越Debate 2.52点），FinQA程序准确率11.33%（最佳），LegalBench达68.00%（接近最优）。在GPQA上排名第二（39.90%），HumanEval以84.00%并列第二。相比通信密集型基线，DarkForest将token消耗降低至1/6.5（如MATH从13.8k降至4.7k），并实现最高30.7%的相对质量提升。

消融实验表明：移除协调器对MATH无影响但降低LegalBench 0.8%；移除防护栏降低MATH至75.40%、LegalBench至65.60%，且防护栏不增加token消耗。

### Q5: 有什么可以进一步探索的点？

**局限性与未来探索方向**

论文虽通过“独立生成+受控通信”降低了开销与错误传播，但其依赖强假设“独立投票”可能限制协同深度：当单智能体自身知识不足时，独立生成会天然丢失集体智慧激发潜力。未来可探索以下方向：

1. **动态通信策略**：设计元控制器根据问题难度、初始置信度自适应决定是否允许额外一轮受控通信（如仅低置信度簇内交换证据），平衡独立性与修正机会。
2. **结构化证据的可信度衰减**：当前对语义等价簇的聚合依赖绝对独立性假设，忽略了智能体输出间潜在的基础模型偏差共性。可引入“相关性惩罚”项，基于智能体输出相似性动态修正信念状态。
3. **细粒度专家分配**：将“单轮独立回答”扩展为“按专长分区独立回答”（如数学问题让擅长推理的智能体先专注推导），再用信念状态聚合，避免全域独立造成的冗余。

此外，该框架在需要常识推理或创意生成的场景（如开放式对话）中可能过于保守，未来可针对任务类型设计混合策略。

### Q6: 总结一下论文的主要内容

多智能体LLM系统通过整合多个智能体的输出来提升推理能力，但现有方法存在错误传播和高通信开销问题。为此，论文提出DarkForest框架，通过受控通信实现高效协调。该方法首先让各智能体独立生成答案，避免相互干扰；然后将原始响应解析为结构化候选记录，对语义等价的候选进行聚类，并利用智能体可靠性、置信度、解析质量、支持模式可靠性和独立性校正等估计校准的信念分布。协调器仅接收策略允许的信念状态证据。在六个推理基准上的实验表明，DarkForest取得了领先的整体质量，相比最强基线提升了高达30.7%的指标，同时相比高通信基线减少了最高6.5倍的Token消耗。核心意义在于揭示了多智能体LLM推理的关键不是如何让智能体更多交流，而是如何保留独立证据并控制跨智能体边界的信息。
