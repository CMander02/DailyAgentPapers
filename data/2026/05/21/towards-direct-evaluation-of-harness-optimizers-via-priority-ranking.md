---
title: "Towards Direct Evaluation of Harness Optimizers via Priority Ranking"
authors:
  - "Kai Tzu-iunn Ong"
  - "Minseok Kang"
  - "Dongwook Choi"
  - "Junhee Cho"
  - "Seungju Kim"
  - "Seungwon Lim"
  - "Geunha Jang"
  - "Minwoo Oh"
  - "Bogyung Jeong"
  - "Sunghwan Kim"
  - "Taeyoon Kwon"
  - "Jinyoung Yeo"
date: "2026-05-21"
arxiv_id: "2605.22505"
arxiv_url: "https://arxiv.org/abs/2605.22505"
pdf_url: "https://arxiv.org/pdf/2605.22505v1"
github_url: "https://github.com/k59118/Harness_Optimizer_Evaluation"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Agent优化"
  - "Agent评估"
  - "Harness优化"
  - "优先级排序"
relevance_score: 8.5
---

# Towards Direct Evaluation of Harness Optimizers via Priority Ranking

## 原始摘要

Harness optimization enables automated agent creation by having an optimizer agent iteratively update the harness of target agents. Despite its success, current studies evaluate optimizers solely by observing target agents' performance gains. This indirect end-improvement evaluation neglects optimizers' actions at intermediate steps, which are often erroneous and hinder agent performance. Therefore, it is unclear whether harness optimization is driven by optimizers' informed update actions or simply trial-and-error. This necessitates direct evaluation of harness optimizers. However, evaluating harness optimizers directly is non-trivial and costly due to the lack of oracle harnesses. To address this, we present a simple, low-cost design to directly evaluate them, namely priority ranking. By asking harness optimizers to rank components (e.g., tools) in a given harness by their potential to improve/hinder agent performance when updated, our design quantifies optimizer ability at the step level without expensive rollouts or manual examination. More importantly, optimizers' ranking performance correlates with their ability to improve agents in actual multi-step harness optimization, establishing priority ranking as a reliable predictor of optimization ability. Priority ranking is enabled by Shor, a collection of 182 human-verified optimization scenarios spanning across domains, designs, and time stages. Codes and data can be found at https://github.com/k59118/Harness_Optimizer_Evaluation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决增强优化器（harness optimizer）直接评估困难的问题。研究背景是，大型语言模型（LLM）智能体的性能高度依赖于其外部“增强”（harness）设计，而人工设计增强成本高、难以规模化，因此研究者转向使用一个优化器智能体迭代地更新目标智能体的增强来自动化这一过程。现有方法的不足在于，当前研究仅通过观察目标智能体在整个优化过程结束后的性能提升（即间接的最终改进评估）来判断优化器的有效性。这种黑盒评估方式完全忽略了优化器在中间步骤的具体行动，而这些步骤中经常会出现错误的增强更新，反而会阻碍最终性能。因此，研究者无法判断优化性能的提升究竟是源于优化器有信息依据的更新决策，还是仅仅依靠试错。核心问题是，缺乏一个直接、低成本的评估方法来量化优化器在每一步中判断“哪些增强组件更新更有效”的能力，即其进行优先级排序的能力。因为直接评估需要人工判断或大量探索，成本高昂且耗时。本文提出优先排序法（priority ranking），通过让优化器对给定增强中的组件（如工具）按改进或损害性能的潜力进行排序，从而在不进行昂贵探索或人工核查的前提下，在步骤级别直接量化其能力，并证明该排序性能与实际多步优化中的优化能力高度相关。

### Q2: 有哪些相关研究？

相关研究可以分为三类。首先是自演进大语言模型，如OPRO让LLM基于历史方案和分数生成新方案，TextGrad将LLM视为隐藏层并利用自然语言梯度优化提示，Expel通过洞察提取和记忆检索增强经验利用。这些工作聚焦于提示或模型层面的自我改进，而本文研究的是优化器对目标智能体完整框架（harness）的迭代更新，属于更宏观的系统级优化。其次是框架优化方向，包括GEPA基于轨迹和性能跨任务优化框架、ACE采用动态备忘录风格的测试时记忆优化、ADAS将框架优化视为编程任务并更新代码中的前向函数，以及AFlow引入蒙特卡洛树搜索进行工作流搜索。其中ReCreate首次实现从零创建框架，Workflow-R1采用群体子序列策略优化训练优化器。本文与这些工作的关键区别在于不直接提出新优化方法，而是开发评估方案。最后是优化器评估类工作，当前最相关的是利用提交历史手动分析优化器行为，但仅限于通用统计。本文提出的优先级排序设计通过让优化器对框架组件进行排序来量化其步骤级能力，无需昂贵执行或人工审查，且排序性能与实际多步优化表现相关，因此可作为可靠的预测指标。

### Q3: 论文如何解决这个问题？

该论文提出了一种名为“优先级排序”（Priority Ranking）的直接评估优化器能力的方法，解决了传统间接评估无法捕捉优化器中间步骤行为的问题。核心思想是将优化器在每个迭代步骤中的决策抽象为一个排序问题：给定当前智能体的装备（harness）及其运行轨迹，优化器需要判断装备中的哪些组件（如提示词、工具、记忆、工作流）最有潜力通过更新来提升或损害智能体性能。  

具体架构上，首先定义装备由N个组件构成（提示词、工具、记忆、工作流），优化器基于历史轨迹（包括每次迭代的装备、执行轨迹、性能评分和优化器自身生成的摘要）进行推理。然后，优化器需输出一个组件优先级排序（如`prompt > memory`），而非直接生成下一个完整装备。这种方法的关键优势在于：排序仅需相对优先级，无需真实的绝对最优装备作为参照；且排序是单步文本生成任务，避免了多步滚动的计算开销。  

创新点包括：1）将复杂的多步优化过程解构为单步排序任务，大幅降低了直接评估的代价；2）设计了182个人工验证的优化场景（Shor数据集），覆盖不同领域、设计和时间阶段，用于评估优化器的排序能力；3）实证表明优化器的排序能力与其在真实多步优化中的表现高度相关，验证了优先级排序是优化能力的可靠预测指标。通过这种间接但低成本的评估方式，研究者得以直接量化优化器在每一步的决策质量。

### Q4: 论文做了哪些实验？

实验基于Shor数据集（含182个跨领域、设计和时间阶段的优化场景），在4个主流数据集（Spider 2.0-lite、τ²-Bench、GAIA、SWE-bench Verified）及2个域外数据集（AppWorld、GPQA）上评估了5类优化器（mini-swe-agent、OpenHands-CLI、Gemini-CLI、Claude Code、Codex）的优先级排序能力。实验采用Acc@1（首位命中率）和NDCG（归一化折损累计增益）作为评估指标。结果显示：OpenHands-CLI（DeepSeek-V4-Pro）在Acc@1上最高（0.305），Claude Code（Sonnet 4.6）在NDCG上最优（0.793）。但大多数优化器排序能力有限，且表现跨域不一致——例如OpenHands-CLI和Gemini-CLI在SWE-V上表现优异但在τ²-Bench上表现较差，而Claude Code在所有域上相对稳定（除Spider外）。这表明当前无单一优化器能掌握所有场景的组件优先级识别。

### Q5: 有什么可以进一步探索的点？

从论文来看，当前研究主要依赖目标Agent的性能提升来间接评估优化器，这忽略了中间步骤中优化器的具体行为。一个核心局限是缺乏对优化器“试错”与“知情更新”的区分能力，导致难以判断优化策略的真正有效性。未来可探索的方向包括：第一，将优先级排序这一直接评估方法扩展到更复杂的多步优化场景，验证其与传统端到端评估的长期一致性；第二，研究如何将优先级排序结果作为反馈信号，实时指导优化器的行动选择，例如在优化过程中动态调整工具或组件的更新权重；第三，考虑优化场景的分布漂移问题，即当前验证的182个场景是否足够覆盖动态环境中的未见情况；第四，可尝试融合优先级排序与强化学习中的探索-利用策略，设计混合评估框架，使优化器能在低误判成本下更高效地搜索有益更新路径。此外，未来工作还可探索将排序能力作为元认知特征，用于自动选择不同优化器。

### Q6: 总结一下论文的主要内容

本文针对自动化智能体“程序优化”（harness optimization）过程中缺乏对优化器直接评估的问题，提出了一种简单、低成本的优先级排序（priority ranking）评估方法。现有研究仅通过观察目标智能体的最终性能提升来间接评判优化器，忽略了中间步骤的误操作（如错误修改工作流），无法区分优化是源于理性决策还是盲目试错。论文的核心贡献在于：将问题定义为让优化器对给定程序中的组件（如提示词、工具等）按改进潜力进行排序，从而在单步层面量化其决策能力，无需昂贵的完整迭代回滚或人工审查。基于此，作者构建了Shor数据集（含182个人工验证的优化场景），实验表明，优化器的排序性能与其在多步优化中提升智能体的实际能力显著相关（斯皮尔曼相关系数ρ=0.602），且评估成本降低8倍以上、速度提升17倍。研究还发现，明确优化器对优先级排序的意识能显著提升其修正缺陷程序的能力。这一工作首次实现了对程序优化器的直接、高效评估，为构建更可靠的优化器提供了理论基础和实践工具。
