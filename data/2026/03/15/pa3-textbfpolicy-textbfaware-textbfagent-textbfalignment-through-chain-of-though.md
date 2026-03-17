---
title: "$PA^3$: $\textbf{P}$olicy-$\textbf{A}$ware $\textbf{A}$gent $\textbf{A}$lignment through Chain-of-Thought"
authors:
  - "Shubhashis Roy Dipta"
  - "Daniel Bis"
  - "Kun Zhou"
  - "Lichao Wang"
  - "Benjamin Z. Yao"
  - "Chenlei Guo"
  - "Ruhi Sarikaya"
date: "2026-03-15"
arxiv_id: "2603.14602"
arxiv_url: "https://arxiv.org/abs/2603.14602"
pdf_url: "https://arxiv.org/pdf/2603.14602v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent Alignment"
  - "Chain-of-Thought"
  - "Policy Compliance"
  - "Tool Use"
  - "Reward Design"
  - "GRPO"
  - "Business Rules"
  - "Efficiency"
relevance_score: 7.5
---

# $PA^3$: $\textbf{P}$olicy-$\textbf{A}$ware $\textbf{A}$gent $\textbf{A}$lignment through Chain-of-Thought

## 原始摘要

Conversational assistants powered by large language models (LLMs) excel at tool-use tasks but struggle with adhering to complex, business-specific rules. While models can reason over business rules provided in context, including all policies for every query introduces high latency and wastes compute. Furthermore, these lengthy prompts lead to long contexts, harming overall performance due to the "needle-in-the-haystack" problem. To address these challenges, we propose a multi-stage alignment method that teaches models to recall and apply relevant business policies during chain-of-thought reasoning at inference time, without including the full business policy in-context. Furthermore, we introduce a novel PolicyRecall reward based on the Jaccard score and a Hallucination Penalty for GRPO training. Altogether, our best model outperforms the baseline by 16 points and surpasses comparable in-context baselines of similar model size by 3 points, while using 40% fewer words.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的对话助手在执行工具调用任务时，难以高效遵循复杂、业务特定规则的问题。研究背景是，不同企业拥有差异化的业务政策（如退货期限），传统方法通常将完整的政策文档（可能长达数万token）作为上下文提供给模型，以确保其遵守规则。然而，现有方法存在明显不足：首先，为每次查询都注入全部政策会带来高昂的延迟和计算成本，且输入token是推理成本的主要来源；其次，过长的上下文会导致“大海捞针”问题，反而损害模型的整体性能。

因此，本文要解决的核心问题是：能否在不将完整业务政策放入上下文的情况下，教导模型在推理时自主回忆并应用相关策略？论文提出了一种多阶段对齐方法，使模型能够在思维链推理过程中，仅回忆与当前查询相关的少量政策（通常为0-5条），从而大幅减少token使用量（降低40%），同时提升政策遵循的准确性和效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：数据集与评测基准、推理过程压缩与优化，以及强化学习对齐方法。

在数据集与评测方面，相关工作包括TauBench等多领域业务策略评估基准及其扩展训练集，以及专注于多轮多步骤但缺乏真实业务策略的数据集。近期还有融合函数调用和意图检测的数据集。本文的评估方法借鉴了使用LLM作为评判员、基于分析的提示以及分解聚合评估等思路，但专注于对中间推理步骤进行多维度评估。

在推理压缩方面，先前工作主要压缩思维链（CoT）本身，例如学习连续的潜在嵌入或使用VQ-VAE将推理路径映射为离散标记。本文则另辟蹊径，专注于压缩系统提示（即业务策略文档），在推理时仅召回相关策略，从而缩短上下文长度，而非压缩推理路径。

在强化学习对齐方法上，本文基于GRPO这一轻量级框架。先前研究将GRPO与基于正确性的奖励或LLM评判分数结合，并在数学推理等领域应用。近期工作扩展了可验证的奖励设计，例如使用函数匹配分数、结合检索指标，或融入人类道德价值观。本文延续了这一方向，但创新地提出了基于Jaccard相似度的PolicyRecall奖励和幻觉惩罚，以鼓励模型准确回忆并应用业务策略，从而实现更忠实、基于策略的推理。

### Q3: 论文如何解决这个问题？

论文通过一个多阶段的训练框架来解决大语言模型在遵循复杂业务规则时面临的上下文过长、计算浪费和性能下降问题。其核心方法是教导模型在推理时通过思维链（CoT）主动回忆并应用相关业务策略，而无需将完整策略文档置于上下文中。

整体框架分为两个主要部分：高质量策略感知思维链的生成，以及基于此数据的多阶段模型训练。在思维链生成阶段，采用“生成-分支-评估-精炼”的四步循环流程。首先，给定业务策略和完整对话历史，使用LLM（如deepseek-r1）为当前回合生成包含策略回忆的思维链。随后，通过四个独立的评估智能体，依据原子性、完整性、忠实性和风格四个核心准则对生成的思维链进行评分。其中，忠实性（即不捏造策略）要求最为严格。未通过评估的思维链会由总结智能体生成反馈，并返回给生成器进行多轮精炼，以此确保最终思维链的高质量。

在模型训练阶段，采用三阶段渐进式方法将业务知识注入模型的参数化知识中。第一阶段，使用通用工具调用数据集和包含业务策略上下文的工具调用数据集对基础模型（Qwen2.5-Instruct-32B）进行微调，目标是提升基础的工具调用能力和策略遵循意识。第二阶段，以第一阶段模型为基础，使用思维链增强的业务策略数据集继续微调，该数据集移除了显式的策略上下文，迫使模型在思维链中主动回忆策略。第三阶段是关键创新所在，采用GRPO（Group Relative Policy Optimization）进行强化学习，以进一步优化模型的输出格式和策略回忆精度。

此阶段的核心技术创新是引入了多项精心设计的奖励与惩罚机制。其中最主要的创新点是**PolicyRecall奖励**，它基于杰卡德（Jaccard）分数计算，旨在奖励模型准确回忆相关策略，同时惩罚过度回忆（即回忆无关策略）。具体而言，通过比较模型回忆的策略集与真实所需策略集的重合度来计算奖励，过度回忆会增大分母从而降低分数。与之配套的是**Hallucination Penalty（幻觉惩罚）**，专门惩罚模型生成策略文档中不存在的策略。此外，还包括针对思维链过长、工具调用正确性以及输出格式的奖励或惩罚。这些奖励项被组合成最终奖励信号，指导模型在强化学习过程中优化行为。

最终，该方法使模型在无需长上下文的情况下，实现了精准的策略回忆与应用，在性能上显著超越基线，同时大幅减少了生成字数。

### Q4: 论文做了哪些实验？

论文实验设置包括三个阶段：使用通用工具调用数据集（GFC）和领域特定工具调用数据集（APIGen）进行训练，其中APIGen与评估数据集TauBench共享相同的业务策略。实验移除了APIGen中包含幻觉工具调用的轨迹，保留了4.8k条高质量轨迹，并从中随机采样50条用于第三阶段的GRPO训练（APIGen-GRPO），其余4.7k条用于第一阶段训练及第二阶段通过合成生成思维链（CoT）进行增强。

主要评估数据集为TauBench，涵盖航空和零售领域，使用pass@1作为核心评估指标。对比方法分为两类：一是“使用业务策略”的基线，包括闭源模型（如Claude-3.5、Claude-3.7、Claude-4）和开源模型（如GLM-4.5、Qwen-2.5、xLAM-2）；二是“不使用业务策略”的基线，包括仅持续SFT的模型（Ours1）、持续SFT加CoT-SFT的模型（Ours2）以及在相同领域直接微调的开源SOTA模型（如xLAM-2）。

关键结果显示，最佳模型（Ours）在性能上比基线提升16个百分点，并比同规模模型的上文基线高出3个百分点，同时输入输出总词数均值仅为27k词，比使用业务策略的基线（如GLM-4.5的40.3k词）显著减少，实现了40%的词数节省。具体数据上，Ours模型的输入词数均值为25k，输出词数均值为2.6k，总词数27k，优于其他对比方法。

### Q5: 有什么可以进一步探索的点？

该论文提出的方法主要依赖于链式思维推理来召回和应用策略，这在实际部署中可能面临推理延迟和计算成本的问题。未来可探索更高效的策略索引与检索机制，例如结合向量数据库或轻量级策略编码器，以降低实时推理开销。此外，当前工作未充分评估策略冲突或动态更新场景下的鲁棒性，可研究多策略优先级调度与增量学习机制。从更广的视角看，将策略对齐与工具使用能力进一步解耦，设计模块化的策略管理组件，可能提升系统的可扩展性和可解释性。同时，引入人类反馈或对抗性测试来优化奖励函数，有助于减少策略幻觉并增强泛化能力。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在工具使用任务中难以遵循复杂商业规则的问题，提出了一种名为$PA^3$的多阶段对齐方法。核心问题是，将全部商业策略放入上下文会导致高延迟、高计算成本，并因长上下文引发“大海捞针”问题，损害整体性能。

方法上，论文提出在推理时通过思维链，教导模型回忆并应用相关商业策略，而无需将完整策略置于上下文中。其核心贡献在于引入了一种基于杰卡德相似度的新颖PolicyRecall奖励，并结合了用于GRPO训练的幻觉惩罚机制，以优化模型的对齐过程。

主要结论显示，该方法的最佳模型性能超越基线16个百分点，并在使用词数减少40%的情况下，比同等规模的上下文基线模型高出3个百分点。其意义在于提供了一种高效、精准的策略感知对齐方案，显著提升了模型在商业规则遵循上的能力与效率。
