---
title: "R2IF: Aligning Reasoning with Decisions via Composite Rewards for Interpretable LLM Function Calling"
authors:
  - "Aijia Cheng"
  - "Kailong Wang"
  - "Ling Shi"
  - "Yongxin Zhao"
date: "2026-04-22"
arxiv_id: "2604.20316"
arxiv_url: "https://arxiv.org/abs/2604.20316"
pdf_url: "https://arxiv.org/pdf/2604.20316v1"
categories:
  - "cs.LG"
tags:
  - "Function Calling"
  - "Reinforcement Learning"
  - "Reasoning Alignment"
  - "Interpretability"
  - "Tool Use"
  - "Reward Design"
  - "GRPO"
relevance_score: 8.0
---

# R2IF: Aligning Reasoning with Decisions via Composite Rewards for Interpretable LLM Function Calling

## 原始摘要

Function calling empowers large language models (LLMs) to interface with external tools, yet existing RL-based approaches suffer from misalignment between reasoning processes and tool-call decisions. We propose R2IF, a reasoning-aware RL framework for interpretable function calling, adopting a composite reward integrating format/correctness constraints, Chain-of-Thought Effectiveness Reward (CER), and Specification-Modification-Value (SMV) reward, optimized via GRPO. Experiments on BFCL/ACEBench show R2IF outperforms baselines by up to 34.62% (Llama3.2-3B on BFCL) with positive Average CoT Effectiveness (0.05 for Llama3.2-3B), enhancing both function-calling accuracy and interpretability for reliable tool-augmented LLM deployment.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在工具调用（Function Calling）任务中，其推理过程与最终工具调用决策之间存在的**错位问题**。研究背景是，LLM通过函数调用能够与外部工具交互，从而获取实时知识并解决复杂任务。早期方法依赖于有监督微调（SFT），但受限于高质量可执行数据的稀缺。随后，强化学习（RL）因其能直接优化功能正确性而成为主流方法。

然而，现有RL方法存在明显不足。它们大多是**结果驱动**的，仅通过抽象语法树（AST）等评估最终调用的正确性。这导致模型可能生成正确的工具调用，但其内部的推理过程（如思维链）却可能是事后合理化（post-hoc rationalization）的产物，并未真正指导工具的选择或参数的构建。这种推理与决策的脱节，使得模型在面对参数格式、默认值等细节时容易出错，也损害了系统的可解释性和鲁棒性，不利于错误诊断和在未见场景下的泛化。

因此，本文要解决的核心问题是：**如何设计一个强化学习框架，使LLM在工具调用任务中的推理过程与可执行的工具调用决策（特别是参数规范、修改和值实例化）保持一致，从而同时提升调用准确性和可解释性**。为此，论文提出了R2IF框架，通过融合格式/正确性约束、思维链效用奖励和参数级对齐奖励的复合奖励机制，来监督和优化整个推理-决策轨迹。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：函数调用方法、强化学习用于LLM推理，以及具体的优化算法。

在**函数调用方法**方面，早期工作主要依赖监督微调（SFT），并提出了如APIGen、ToolACE等可扩展的合成数据生成框架来解决高质量数据稀缺的问题。同时，BFCL等基准测试被建立以进行标准化评估。近期，强化学习（RL）被引入，将函数调用视为策略优化问题，直接优化可验证奖励下的正确性。本文提出的R2IF框架属于此类RL方法，但其核心创新在于通过复合奖励（特别是CER和SMV奖励）解决了现有RL方法中推理过程与工具调用决策之间的错位问题，从而提升了可解释性。

在**RL用于LLM推理**的研究中，强化学习已成为增强LLM推理能力的核心后训练范式，常用PPO及其变体（如GRPO）进行优化。先前工作强调过程感知监督和步骤级评估，为多步推理提供更密集的信号。近期研究进一步将RL扩展到工具增强的推理中。本文工作与此紧密相关，但更专注于在函数调用这一特定结构化任务中，设计专门的奖励来对齐推理与决策。

在**优化算法**层面，本文直接采用了**GRPO（Group Relative Policy Optimization）** 作为优化器。GRPO是PPO风格的一种变体，通过在查询组内归一化奖励来稳定和扩展面向推理的训练。本文的贡献不在于提出新优化器，而是将新颖的复合奖励设计与现有的GRPO算法相结合，以解决特定问题。

### Q3: 论文如何解决这个问题？

论文通过提出R2IF框架来解决大语言模型在工具调用中推理过程与决策之间错位的问题。其核心方法是设计一个复合奖励函数，结合强化学习（使用GRPO优化器）来同时优化模型的可执行动作和可解释的推理过程。

整体框架包含一个策略模型，其输出由推理块（<reason>）和工具调用块（<tool>）组成。训练的关键在于精心设计的复合奖励函数，它由三个主要部分组成，分别从不同粒度进行监督：

1.  **二元奖励（Binary Reward）**：这是一个硬性约束，确保输出的格式正确且工具调用结果与真实值完全一致。它进一步分解为格式有效性奖励（检查输出是否严格包含一个顺序正确的推理块和工具块）和工具调用正确性奖励（检查预测的动作列表是否与真实列表完全匹配）。该奖励在总奖励中权重为3，以确保模型优先满足基本的结构和结果正确性。

2.  **思维链有效性奖励（CER）**：这是核心创新点之一，旨在直接评估和奖励推理过程对促成正确工具调用的贡献。其计算方式是：首先，有一个经过“忠实性”微调的“学生模型”作为基线，其在不看特定推理前缀时的成功率记为基线值。然后，将当前策略模型生成的推理前缀固定，让同一个“学生模型”基于此前缀采样生成多个工具调用，并计算这些采样的成功率。CER奖励即为当前推理前缀带来的成功率相对于基线的提升值。这迫使模型生成能够有效指导后续决策的、信息充分的推理。

3.  **规范-修改-值奖励（SMV Reward）**：这是另一个关键创新点，提供了更细粒度的、参数级别的监督，以确保推理过程明确地支持参数决策。它评估推理是否：（i）正确识别了参数的规范/约束；（ii）描述了从用户查询到有效参数值所需的修改/转换；（iii）最终在工具调用中实例化了正确的参数值。具体实现时，会将模型生成的推理片段与由LLM生成的、包含参数规范、修改说明的真实文档进行语义相似度比对（使用阈值门控），并结合参数是否最终被正确实例化的硬性信号，计算出一个综合分数。

**主要创新点**在于：第一，引入了CER奖励，首次将推理过程的有效性量化为对决策成功率的因果贡献，从而直接对齐推理与决策；第二，设计了SMV奖励，从参数层面强制要求推理显式地关联规范、转换和最终值，增强了决策的可解释性和可靠性；第三，将上述奖励与确保基本正确的二元奖励相结合，通过GRPO进行端到端优化，共同提升了工具调用的准确性和推理过程的质量。

### Q4: 论文做了哪些实验？

论文在实验设置上，使用从ToolACE数据集中筛选和平衡后的2,500个样本作为训练集，在6块NVIDIA RTX PRO 6000 GPU上使用Verl进行训练。对比方法包括：原始指令微调模型（Raw Instruct Model）、使用GPT-4o蒸馏推理过程进行监督微调的模型（SFT）、仅使用二元奖励的GRPO训练（Binary reward）以及使用特定设计奖励的ToolRL方法。

评估在两个主流基准测试上进行：伯克利函数调用排行榜（BFCL）和ACEBench，重点关注单轮测试用例。评价指标包括工具调用准确率（Accuracy）和用于评估推理过程效用的平均思维链有效性（Average CoT Effectiveness, ACE）。

主要结果显示，R2IF在多个模型骨干上均取得了最佳或接近最佳的整体性能。在BFCL上，R2IF在Qwen2.5-3B、Qwen2.5-7B和Llama3.2-3B上取得了最高整体准确率，其中Llama3.2-3B的提升尤为显著，整体准确率达到72.21%，相比基线最高提升达34.62%。在更具挑战性的Live场景中，R2IF也保持了竞争力。在ACEBench上，R2IF在所有四个骨干模型上都取得了最高的整体准确率，尤其在Atom和Single-turn子集上优势明显，表明其提升了核心工具决策质量。

关键数据指标方面，除了准确率，论文还报告了ACE值。R2IF方法生成的推理过程对工具调用决策有正向辅助作用，例如Llama3.2-3B在BFCL上取得了0.05的正向ACE值，而多数基线方法的ACE值为负，这证明了R2IF在提升准确率的同时增强了推理的可解释性与有效性。消融实验进一步证实了复合奖励中各组件（SMV奖励、CER奖励和SFT预热）的必要性，移除任一组件都会导致性能下降。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在两方面：一是仅评估了单轮函数调用任务，未涉及多轮交互场景，这限制了模型在复杂、持续性任务中保持推理连贯性和工具调用准确性的能力验证；二是奖励设计高度针对特定任务，可能难以泛化到其他类型的推理或决策任务中，影响了框架的通用性和可扩展性。

未来研究方向可围绕以下三点展开：首先，探索多轮对话场景下的推理对齐机制，研究如何设计跨步长的奖励函数以维护长期一致性；其次，开发更通用的奖励模块，通过模块化设计适应不同任务结构和工具类型，提升框架的迁移能力；最后，结合因果推理等理论，深入分析推理过程与决策偏差的内在关联，为奖励设计提供更坚实的理论依据。这些改进有望推动可解释性函数调用在复杂实际应用中的落地。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型（LLM）工具调用中存在的推理过程与调用决策不匹配问题，提出了R2IF框架以提升其可解释性和准确性。核心贡献在于设计了一个复合奖励机制，该机制整合了格式/正确性约束、思维链有效性奖励（CER）以及规范-修改-价值（SMV）奖励，并通过GRPO算法进行优化。方法上，R2IF旨在使模型的推理步骤（思维链）与最终的工具调用决策保持一致，从而增强决策过程的透明度和可靠性。实验结果表明，在BFCL和ACEBench基准测试中，R2IF显著优于基线方法（例如Llama3.2-3B在BFCL上提升达34.62%），并实现了正的思维链平均有效性，有效提升了函数调用的准确性和可解释性，为可靠的工具增强型LLM部署提供了解决方案。
