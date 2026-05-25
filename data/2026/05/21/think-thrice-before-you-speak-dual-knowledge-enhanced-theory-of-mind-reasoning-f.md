---
title: "Think Thrice Before You Speak: Dual knowledge-enhanced Theory-of-Mind Reasoning for Persuasive Agents"
authors:
  - "Minghui Ma"
  - "Bin Guo"
  - "Runze Yang"
  - "Mengqi Chen"
  - "Yan Liu"
  - "Jingqi Liu"
  - "Yahan Pei"
  - "Xuehao Ma"
  - "Qiuyun Zhang"
  - "Zhiwen Yu"
date: "2026-05-21"
arxiv_id: "2605.22602"
arxiv_url: "https://arxiv.org/abs/2605.22602"
pdf_url: "https://arxiv.org/pdf/2605.22602v1"
categories:
  - "cs.AI"
tags:
  - "Theory-of-Mind"
  - "Persuasive Dialogue"
  - "BDI Framework"
  - "Knowledge-Enhanced Reasoning"
  - "LLM Agent"
  - "Mental State Inference"
  - "Multi-Turn Dialogue"
relevance_score: 8.5
---

# Think Thrice Before You Speak: Dual knowledge-enhanced Theory-of-Mind Reasoning for Persuasive Agents

## 原始摘要

Persuasive dialogue requires reasoning about others' latent mental states, a capability known as Theory of Mind (ToM). However, due to reliance on simple prompting strategies and insufficient ToM knowledge, existing LLMs often fail to capture the intrinsic dependencies among mental states, leading to fragmented representations and unstable reasoning. To address these challenges, we introduce the ToM-based Persuasive Dialogue (ToM-PD) task, grounded in the Belief-Desire-Intention (BDI) framework, which explicitly models the sequential dependencies among mental states in multi-turn dialogues. To facilitate research on this task, we construct a large-scale annotated dataset, ToM-based Broad Persuasive Dialogues (ToM-BPD), capturing fine-grained mental states and corresponding persuasive strategies. We further propose Think Thrice Before You Speak (TTBYS), a knowledge-enhanced stepwise reasoning framework that leverages both explicit and implicit prior experiences to improve LLMs' inference of desires, beliefs, and persuasive strategies. Experimental results demonstrate that Qwen3-8B equipped with TTBYS outperforms GPT-5 by 1.20%, 22.80%, and 16.97% in predicting desires, beliefs, and persuasive strategies, respectively. Case studies further show that our approach enhances interpretability and consistency in reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有大语言模型在说服性对话中进行心理理论推理时面临的两个核心问题。研究背景是，说服性对话系统需要推断用户的潜在心理状态，这种能力被称为心理理论。尽管已有研究尝试将心理理论融入说服系统，但现有方法主要依赖简单的提示策略，且缺乏足够的心理理论知识。这些方法的不足在于，它们往往将信念、愿望等不同心理状态视为独立变量，忽略了它们之间的内在依赖关系，导致在多轮对话中生成的心理状态表征碎片化，推理过程不稳定，容易出错。为此，论文定义了基于心理理论的说服性对话任务，核心问题是如何系统性地建模并推断用户心理状态及其内在的顺序依赖关系。为了克服现有LLMs因心理理论知识不足导致的推理不稳健问题，论文提出要解决的关键挑战是：如何将显性和隐性的先验知识有效整合到大模型中，引导其进行逐步、合理的推理，从而提升在预测用户愿望、信念及生成相应说服策略时的准确性和一致性。

### Q2: 有哪些相关研究？

在说服性对话领域，相关研究主要分为三类：策略驱动方法，通过预定义或学习到的对话策略增强可控性；知识增强方法，引入外部知识或结构化记忆提升上下文理解；以及多智能体系统，通过多个协调的智能体实现复杂推理。然而，这些方法通常缺乏对用户心理状态的显式建模，限制了可解释性和长期效果。本文提出的框架（TTBYS）通过逐步方式显式建模心理状态间的依赖关系，从而指导说服策略选择。

在心理理论（ToM）研究方面，相关工作也分为三类：基于提示的方法，通过推理阶段的思维支架（如视角采纳提示、角色条件）提升ToM推理；结构化与神经符号方法，通过整合符号表征或概率推理框架显式建模信念和目标推理；以及多智能体认知框架，将ToM推理分解为多个交互组件模拟社会认知过程。现有方法主要关注抽象或静态状态下推理，在动态心理状态建模上不足。本文与此不同，通过基于BDI状态的逐步反向推理结合知识增强推理，在多人说服对话中实现了更准确、一致和可解释的ToM推理。

### Q3: 论文如何解决这个问题？

论文通过提出TTBYS框架解决LLM在说服性对话中心理状态推理不稳定的问题，结合BDI理论建模心理状态依赖性，并引入双重知识增强技术。

核心框架：TTBYS将说服者推理过程分解为三个步骤：意图总结、欲望推理、信念生成和策略选择，每个步骤对应BDI模型中一个心理状态。整体流程从对话历史提取摘要，依次推断欲望、信念，最后联合推理策略。

主要模块：1）**心理状态经验知识库**：将对话历史、摘要、欲望、信念、策略构建为五元组结构知识单元，每个多轮对话分解为多个独立经验。2）**对话摘要生成**：利用LLM生成简洁摘要，保留关键语义，避免错误传播。3）**双重知识增强推理**：欲望推理阶段，通过检索经验构建经验驱动分布，与LLM直觉分布线性融合（α系数调节）；信念推理阶段，基于摘要和欲望检索相关经验显式注入LLM上下文；策略选择阶段，联合摘要和信念检索经验，再次融合经验驱动分布与LLM直觉分布（β系数调节）。

关键技术：概率分布融合机制平衡经验可靠性（来自标注数据）与LLM灵活性；检索采用语义相似度匹配，支持隐式/显式知识引导。创新点包括：1）首次将BDI框架形式化为经验五元组；2）分步推理减少错误累积；3）对话摘要机制弥补LLM意图推理缺陷。实验表明该框架在欲望、信念、策略预测上分别较GPT-5提升1.20%、22.80%、16.97%。

### Q4: 论文做了哪些实验？

实验在ToM-BPD数据集上进行，该数据集包含563段对话，其中前100段对话（399轮）作为测试集，剩余404段对话（1564条ToM经验）构成知识库。对比方法包括两种基础提示方法（零样本提示和思维链CoT）以及两种最新的ToM增强推理方法（Hypothetical Minds HM和MetaMind MM）。评估了六个前沿大语言模型：三个开源模型（LLaMA-3.1-8B-Instruct、Qwen-3-8B、Mixtral-7B-Instruct）和三个闭源模型（Gemini-3-Pro、GPT-4o-mini、GPT-5）。所有模型温度设为0.9，结果取三次运行平均值。混合系数α和β分别设为0.5和0.3。评估指标包括欲望预测、信念预测和策略预测的准确率，其中信念预测使用GPT-5评分协议（极性+原因完全正确得1分，仅极性正确得0.5分，否则0分）。主要结果如表所示：搭载TTBYS的Qwen3-8B在欲望准确率（72.82%）、信念准确率（54.64%）和策略准确率（39.78%）上均取得最优结果，分别超越GPT-5达1.20%、22.80%和16.97%；TTBYS在所有开源模型上均显著优于所有基线方法，例如LLaMA-3.1-8B使用TTBYS后信念准确率达43.62%，策略准确率达37.76%。

### Q5: 有什么可以进一步探索的点？

论文在理论构建与实验验证上虽有突破，但仍有若干可探索方向。首先，BDI框架虽增强了心理状态链式推理，但其对动态情感演变（如情绪波动对信念的影响）建模不足，未来可引入情绪心理学理论细化状态转移。其次，当前ToM-BPD数据集依赖人工标注，存在领域偏差与成本问题，可尝试半自动化的知识图谱增强标注方法。第三，TTBYS框架中的显/隐知识融合依赖线性叠加，未考虑知识冲突情形（如先验经验与当前对话矛盾），可引入对抗性验证或贝叶斯推理来动态消歧。此外，实验仅以Qwen3-8B为基座，不同参数规模的模型对知识蒸馏的鲁棒性差异值得探究。最后，真实场景中劝说效果需结合用户心理倾向（如易感性）个性化调整，现有研究缺乏对受众因素的显式编码。改进方向包括构建多模态ToM模型（如融合语音语调）与探索因果推理替代当前相关推理范式。

### Q6: 总结一下论文的主要内容

本文提出并定义了基于心理理论的说服对话任务，旨在系统建模多轮对话中用户心理状态的顺序依赖关系。针对现有大语言模型因缺乏心理理论知识和简单提示策略导致的推理碎片化与不稳定问题，论文构建了大规模精细标注数据集，并提出了“三思而后言”知识增强逐步推理框架。该框架结合显性与隐性先验知识，引导模型按步骤依次推断用户的愿望、信念及说服策略。实验结果表明，配备该框架的模型在愿望、信念和策略预测上分别比当前最优模型提升1.20%、22.80%和16.97%，案例研究进一步验证了该方法在推理可解释性和一致性上的优势，为构建更鲁棒、可解释的说服对话系统提供了新思路。
