---
title: "Try, Check and Retry: A Divide-and-Conquer Framework for Boosting Long-context Tool-Calling Performance of LLMs"
authors:
  - "Kunfeng Chen"
  - "Qihuang Zhong"
  - "Juhua Liu"
  - "Bo Du"
  - "Dacheng Tao"
date: "2026-03-12"
arxiv_id: "2603.11495"
arxiv_url: "https://arxiv.org/abs/2603.11495"
pdf_url: "https://arxiv.org/pdf/2603.11495v1"
categories:
  - "cs.CL"
tags:
  - "Tool-Calling"
  - "Long-Context"
  - "Reasoning"
  - "Self-Reflection"
  - "Divide-and-Conquer"
  - "Training-Free"
  - "Training-Based"
  - "Benchmark Evaluation"
relevance_score: 8.5
---

# Try, Check and Retry: A Divide-and-Conquer Framework for Boosting Long-context Tool-Calling Performance of LLMs

## 原始摘要

Tool-calling empowers Large Language Models (LLMs) to interact with external environments. However, current methods often struggle to handle massive and noisy candidate tools in long-context tool-calling tasks, limiting their real-world application. To this end, we propose Tool-DC, a Divide-and-Conquer framework for boosting tool-calling performance of LLMs. The core of Tool-DC is to reduce the reasoning difficulty and make full use of self-reflection ability of LLMs via a "Try-Check-Retry" paradigm. Specifically, Tool-DC involves two variants: 1) the training-free Tool-DC (TF), which is plug-and-play and flexible; 2) the training-based Tool-DC (TB), which is more inference-efficient. Extensive experiments show that both Tool-DC methods outperform their counterparts by a clear margin. Tool-DC (TF) brings up to +25.10% average gains against the baseline on BFCL and ACEBench benchmarks, while Tool-DC (TB) enables Qwen2.5-7B to achieve comparable or even better performance than proprietary LLMs, e.g., OpenAI o3 and Claude-Haiku-4.5.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在长上下文工具调用任务中，面对海量且可能存在语义混淆的候选工具时性能显著下降的问题。研究背景是，尽管工具调用能力使LLMs能够与外部环境交互以处理复杂现实任务，但现有方法在候选工具数量庞大时，由于长上下文带来的信息过载和相似工具的参数描述干扰，模型难以准确选择工具并填充正确参数。

现有方法存在明显不足。针对长上下文问题，一种常见方法是引入额外的检索器来筛选相关工具子集，但这高度依赖检索器的性能，一旦检索失败遗漏关键工具，LLMs便无法给出正确结果。针对混淆工具导致的参数填写错误，已有工作尝试通过人工构建全局错误检查清单并以上下文学习方式指导模型，但这种方法不够灵活，难以覆盖所有错误类型，且人工设计成本高。

因此，本文要解决的核心问题是：如何设计一个更有效、高效的框架来提升LLMs在长上下文、多混淆候选工具场景下的工具调用性能。为此，论文提出了Tool-DC（分而治之框架），其核心是通过“尝试-检查-重试”范式，降低模型推理难度并充分利用其自我反思能力。该框架包含无需训练的即插即用变体（TF）和基于训练的高效推理变体（TB），旨在从根本上改善LLMs处理大规模候选工具集时的鲁棒性和准确性。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提升大语言模型（LLM）工具调用能力的方法，可分为训练无关和训练相关两大类。

**训练无关方法**：这类方法通过优化推理过程来提升性能，例如通过检索机制筛选相关工具，或向提示中注入约束条件来引导模型。它们无需额外训练，具有即插即用的灵活性，但其性能受限于基础模型本身的能力，且在候选工具数量庞大、描述冗长嘈杂的长上下文场景中表现不佳。

**训练相关方法**：这类方法通过监督微调（SFT）或强化学习（RL）等技术对模型进行对齐训练，以提升其工具调用能力。虽然有效，但它们通常面临高昂的训练成本和合成训练数据的瓶颈。同样，现有方法在应对长上下文、工具数量多且相似度高（仅参数描述不同）的复杂场景时仍存在困难。

与上述研究相比，本文提出的Tool-DC框架的核心区别在于其“分而治之”的“尝试-检查-重试”范式。它旨在系统性降低模型在长上下文工具调用中的推理难度，并充分利用LLM的自我反思能力。此前仅有少数工作尝试通过人工设计全局错误检查清单来缓解工具调用错误，但该方法清单设计复杂，且仍未根本解决长上下文问题。本文的框架则提供了更通用、系统的解决方案，并衍生出训练无关与训练高效两个变体，以兼顾灵活性与性能。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Tool-DC的“分而治之”框架来解决长上下文工具调用中候选工具数量庞大且噪声多的问题。其核心方法是采用“尝试-检查-重试”的范式，降低模型推理难度并充分利用其自我反思能力。该框架包含两种变体：无需训练的Tool-DC（TF）和基于训练的Tool-DC（TB）。

整体框架围绕三个阶段构建。首先，在“尝试”阶段，通过**战略锚点分组**将庞大的全局工具库划分为多个并行的低噪声子空间。具体做法是，先使用检索器（如BM25）获取Top-K相关工具作为锚点，然后为每个锚点工具搭配一个不相交的干扰工具子集（来自剩余工具），形成多个分组，同时保留原始的Top-K集合作为一个独立分组。接着进行**局部推理**，让模型在每个子空间内独立生成初始工具调用或空标记，从而大幅缩小每次决策的搜索空间。

其次，在“检查”阶段，引入一个**基于规则的一致性验证器**来过滤无效调用。该验证器从三个维度检查每个输出：函数名称是否存在于工具集中、参数键是否匹配且必需参数齐全、参数值数据类型是否符合定义。只有通过验证的候选才会被保留到有效集合中。

最后，在“重试”阶段，利用自我反思机制进行**全局精炼决策**。从有效集合中提取对应的原始工具定义，形成一个精炼的候选工具子集，再次输入模型进行最终调用，从而得到更准确的结果。

无需训练的TF变体即插即用，灵活但需要多次前向传播。而基于训练的TB变体则通过微调将上述分治范式内化到模型参数中。其关键是通过枚举策略（每个工具作为一个子空间）构建包含正确推理轨迹的思维链训练数据，然后训练模型在单次前向传播中同时生成推理过程和最终工具调用，从而提升推理效率。

创新点在于：1）通过战略分组将全局决策分解为局部决策，降低了上下文长度和推理干扰；2）设计一致性验证模块，有效减少幻觉调用；3）利用验证反馈驱动模型自我反思，实现精准重试；4）提供训练与免训练两种实现路径，兼顾灵活性

### Q4: 论文做了哪些实验？

论文在BFCL和ACEBench两个基准测试上进行了实验。实验设置包括标准设置（使用原始工具列表）和扩展设置（通过随机注入无关工具将候选工具扩展至20个，模拟真实噪声），评估指标为严格的抽象语法树（AST）精确匹配准确率。对比方法包括训练无关方法（如GT_Funs、All_Funs、Top-K、HiTEC-ICL、ToolGT (Prompting)）和训练方法（如基础模型、普通监督微调基线以及专有模型）。主要结果显示，在标准设置下，Tool-DC (TF)在Qwen2.5系列模型上均取得最高平均分，例如在Qwen2.5-1.5B上平均得分为59.81%，比基线（All_Funs）提升4.61%。在扩展设置下，Tool-DC (TF)展现出强鲁棒性，尤其在Qwen2.5-1.5B上比All_Funs提升25.10%的平均得分。此外，Tool-DC (TF)在其他模型（如Llama3、Gemma3、GPT-4o-mini）上也带来一致性能提升，例如GPT-4o-mini提升5.3%。训练方法Tool-DC (TB)使Qwen2.5-7B在BFCL上整体得分达83.16%，超越OpenAI o3（77.58%）、DeepSeek-V3.2（80.77%）和Claude-Haiku-4.5（82.59%）。消融实验表明，移除Try、Check或Retry任一阶段均导致性能下降，其中移除Retry时整体准确率从64.77%骤降至5.26%。参数分析显示，当分组数K设为5时Tool-DC (TF)性能最优。

### Q5: 有什么可以进一步探索的点？

该论文提出的Tool-DC框架虽然在长上下文工具调用任务上取得了显著提升，但仍存在一些局限性和值得深入探索的方向。首先，其训练版本（TB）依赖的种子数据集多样性和工具数量有限，未能充分模拟真实世界中大规模、高噪声的候选工具场景。未来可构建更复杂、动态的数据集，并探索强化学习（如GRPO）来优化模型在嘈杂环境下的鲁棒性和泛化能力。其次，当前工作仅针对单步工具调用进行评估，未涉及多步嵌套或链式工具调用场景（如BFCL的最新版本）。未来可将“尝试-检查-重试”范式扩展至多步推理，研究如何有效管理中间状态和错误累积问题。此外，框架的推理效率仍有提升空间，例如通过动态调整“分治”粒度或引入轻量级验证模块来减少重复调用开销。最后，可探索该框架与不同规模或架构的LLMs（如MoE模型）的适配性，以及在实际部署中如何平衡插件灵活性与计算成本。

### Q6: 总结一下论文的主要内容

本文提出Tool-DC框架，旨在解决大语言模型在长上下文工具调用任务中因候选工具数量庞大且噪声多而性能受限的问题。其核心贡献是设计了一种“尝试-检查-重试”的分治范式，通过降低推理难度并充分利用模型的自反思能力来提升工具调用的准确率。方法上包含两种变体：无需训练的Tool-DC (TF)，即插即用，灵活性强；基于训练的Tool-DC (TB)，通过微调将分治策略内化到模型参数中，推理效率更高。实验表明，两种方法均显著优于现有基线，其中Tool-DC (TF)在BFCL和ACEBench基准上平均提升达25.10%，而Tool-DC (TB)能使Qwen2.5-7B等开源模型达到甚至超越GPT-4o、Claude-Haiku-4.5等专有模型的性能。该框架为增强LLMs在复杂现实场景中的工具调用能力提供了有效解决方案。
