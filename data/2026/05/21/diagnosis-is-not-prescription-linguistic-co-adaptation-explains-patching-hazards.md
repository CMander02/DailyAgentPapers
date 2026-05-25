---
title: "Diagnosis Is Not Prescription: Linguistic Co-Adaptation Explains Patching Hazards in LLM Pipelines"
authors:
  - "Yoon Jeonghun"
  - "Kim Dongchan"
date: "2026-05-21"
arxiv_id: "2605.21958"
arxiv_url: "https://arxiv.org/abs/2605.21958"
pdf_url: "https://arxiv.org/pdf/2605.21958v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "多模块Agent"
  - "诊断悖论"
  - "语言共适应"
  - "Agent调试"
  - "路由模块"
  - "提示注入"
  - "Agent管线"
  - "因果分析"
  - "Agent鲁棒性"
relevance_score: 9.5
---

# Diagnosis Is Not Prescription: Linguistic Co-Adaptation Explains Patching Hazards in LLM Pipelines

## 原始摘要

When a multi-module LLM agent fails, the module most responsible for the failure is not necessarily the best place to intervene. We demonstrate this Diagnostic Paradox empirically: causal analysis consistently identifies the routing module -- which selects which tool to call next -- as the primary bottleneck across three independent agent families. Yet injecting prompt-level correction examples into this module consistently degrades performance, sometimes severely. Patching an upstream query-rewriting module instead reliably improves outcomes. The effect holds with statistical significance on two agent families and directional consistency on a third; alternative repair strategies at the routing module (instruction rewriting, model upgrade) are neutral, confirming that the harm is specific to correction-injection patching.
  We explain this asymmetry through the Linguistic Contract hypothesis: each downstream module implicitly adapts to its upstream's characteristic error distribution, so correcting the bottleneck breaks this implicit alignment in a way that upstream corrections do not. We operationalize this via a per-agent co-adaptation measure, derived from diagnosis alone, and show it is consistently associated with patching harm across agent families: higher co-adaptation co-occurs with harm, lower with safety. This trend holds across all three agent families, providing preliminary support for the hypothesis beyond a single-agent observation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多模块大语言模型（LLM）智能体管道中一个反直觉的诊断与修复分离问题。研究背景是：现代LLM智能体通常由多个顺序连接的NLP模块组成（如查询重写器、规划器、路由器和响应生成器），当系统出现故障时，需要定位故障源并修复。现有方法（如端到端优化器和过程奖励模型）通常将诊断与修复等同对待，即认为导致故障最多的模块就是最佳修复目标。

现有方法的不足在于忽视了模块间存在隐性语言共适应现象：下游模块会隐式适应上游模块输出的特征分布（包括错误模式）。因此，直接修复诊断出的瓶颈模块反而会破坏这种已建立的共适应关系，导致性能下降。

本文要解决的核心问题是：通过因果干预实验揭示并解释这种“诊断悖论”——即因果分析确定的路由模块是导致故障的首要瓶颈，但对该模块注入提示级修正示例却持续降低性能（有时甚至严重退化），而修复上游的查询重写模块反而可靠地提升效果。论文提出“语言契约”假说解释这一不对称性，并通过跨三个智能体家族的实验提供初步支持证据，表明共适应程度与修复危害之间存在一致趋势。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及以下类别：  
- **评测与调试方法类**：传统工作如TextGrad、TRACE等端到端优化器虽能提升流水线整体性能，但未区分错误定位与干预点；过程奖励模型虽可定位步骤级错误，但需昂贵人工标注。本文通过因果框架在LLM调用级别填补了这一空白。  
- **因果分析类**：因果中介分析此前主要用于单模型内部（如神经元、注意力头层级）理解语言信息流动。本文将这一原则提升至流水线中完整LLM模块调用层面，发现模块级共同适应动态产生反直觉的修复特性，这是token级分析无法揭示的。  
- **方法对比**：与迭代自优化、提示优化不同，本文的CCP方法通过复用因果筛选的修正三元组，无需额外推理。跨家族智能体/裁判/设计则避免了LLM裁判的自相关性。  

核心区别在于：本文首次实证“诊断悖论”并系统性解释路由模块补丁危害，而现有工作均未区分“错误责任归属”与“最佳干预位置”。

### Q3: 论文如何解决这个问题？

该论文提出CICA（因果干预分析）框架来系统解决LLM Agent管线中的诊断悖论问题。核心方法包含四个层次：首先构建失败指数$F$，通过LLM裁判对每个模块的严重程度评分$sev_i$进行聚合计算，量化整体行为表现；其次利用因果贡献度$\Delta F_i$，通过替换模块输出为oracle值并重新执行来识别每个模块的因果责任；第三层通过自然间接效应$NIE_i$分析模块间的补偿/放大关系，将模块分为补偿者、放大者和传播者；最后在矫正配置阶段采用CCP（校正示例注入）方法，在目标模块的提示中追加5个严重度排序的校正三元组。

架构设计的关键创新在于揭示语言契约假说：下游模块会隐式适应上游输出的特征错误分布，形成补偿行为。当对瓶颈模块（路由模块）进行CCP干预时，会打破这种隐含对齐，导致补偿机制失效、错误暴露，即处方危害。技术实现上采用自适应z分数路由变体来归一化模块间NIE异质性。实验证明，上游查询重写模块的校正（$M_1$ CCP）仅扰动表面语言层，下游模块能自然补偿；而路由模块校正（$M_3$ CCP）干扰可执行语义层，造成系统退化。该框架还定义了相对危害和绝对危害两种形式，并用$M_3$补偿者比率作为契约强度的经验代理指标。

### Q4: 论文做了哪些实验？

论文围绕“诊断悖论”展开了系统的实验验证。**实验设置**上，使用 τ-bench retail 作为诊断集（500样本）和测试集（111样本），τ-bench airline 用于泛化验证。**数据集/基准**涉及三个独立智能体家族：gpt-4o-mini（OpenAI）、Llama 4 Scout（Meta）和 Qwen3-32b（Alibaba），均搭配相同的 oracle（Claude Sonnet 4.6）和 LLM 评判器（Gemini 2.5 Flash）。**主要实验**包括：1）因果诊断实验（CICA），识别路由模块（M3）为关键瓶颈（ΔF=1.018），该结果跨领域和模型家族一致（Llama 4 Scout 为1.564，Qwen3-32b 为1.148）。2）修补实验，在 M1-M4 应用 Pop CCP（k=5 修正三元组），关键发现：M3 修补导致 gpt-4o-mini 性能下降（+0.243，p<0.05），Qwen3-32b 显著下降（+0.683，p<0.001），而 Llama 4 Scout 微弱下降（-0.013）；M1 修补则带来改善（gpt-4o-mini -0.191，Qwen3-32b -0.659，Llama 4 -0.402）。3）对比策略实验，M3 替代策略（指令重写、模型升级）均产生 Δ≈0，证实危害对 CCP 的特异性。4）语言契约假说验证：补偿率高的智能体（gpt-4o-mini 98.2%，Qwen3-32b 96.0%）出现绝对危害，而 Llama 4 Scout（0%）无危害，跨家族一致性支持该假说。模型间交叉验证通过统计算法（Holm 校正、配对 Wilcoxon 检验）评估显著性，效应量使用配对 Cohen's d_z。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面。首先，诊断与修复矛盾的证据范围有限，目前仅在零售领域的τ-bench基准和固定管道拓扑上验证，其他任务域和架构（如多跳推理或动态路由）的推广性尚不明确。其次，单轮首次动作协议限制了多轮交互场景的适用性，尽管预期矛盾方向不变，但缺乏实证支持。最后，方向性解释（语言共适应）目前基于间接推断（M4余弦相似度与ΔF对比），而非直接几何投影到对齐轴，且共适应度量（补偿率）源于诊断时的NIE，存在循环论证风险。未来可探索三个方向：一是设计独立于诊断的共适应指标（如模块间熵减或互信息），以建立因果机制；二是引入人类评估和开放式任务（如客服对话）验证泛化性；三是将修复策略拓展到对抗性微调或动态重训练，替代当前的提示注入，减少对齐破坏。此外，直接测量下游模块对上游误差分布的隐式适应梯度，可能为语言契约假说提供更直接的证据。

### Q6: 总结一下论文的主要内容

这篇论文揭示了LLM流水线中的“诊断悖论”：在多模块智能体系统中，因果分析识别出的关键瓶颈模块（如路由模块）反而是最不适合进行提示级修正的目标。通过三个独立智能体家族的实证研究，作者发现对瓶颈模块注入修正样例反而会降低性能（危害效应），而修正上游查询重写模块则能可靠提升效果。这种不对称性被归因于“语言契约假说”：下游模块会隐式适应上游模块的典型错误分布，直接修正瓶颈破坏了这种隐式对齐。作者提出基于诊断的协同适应度量，发现在三个智能体家族中，高协同适应与修正危害相关，低协同适应则更安全。这项研究挑战了“哪里出错就修哪里”的直觉，强调理解模块间协同适应对有效干预的重要性，为构建可维护的LLM流水线提供了新视角。
