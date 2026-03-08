---
title: "CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification"
authors:
  - "Jinpeng Chen"
  - "Cheng Gong"
  - "Hanbo Li"
  - "Ziru Liu"
  - "Zichen Tian"
date: "2026-03-02"
arxiv_id: "2603.01940"
arxiv_url: "https://arxiv.org/abs/2603.01940"
pdf_url: "https://arxiv.org/pdf/2603.01940v1"
categories:
  - "cs.AI"
tags:
  - "Tool Use & API Interaction"
  - "Learning & Optimization"
relevance_score: 8.5
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "CoVe (Constraint-Verification)"
  primary_benchmark: "τ²-bench"
---

# CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification

## 原始摘要

Developing multi-turn interactive tool-use agents is challenging because real-world user needs are often complex and ambiguous, yet agents must execute deterministic actions to satisfy them. To address this gap, we introduce \textbf{CoVe} (\textbf{Co}nstraint-\textbf{Ve}rification), a post-training data synthesis framework designed for training interactive tool-use agents while ensuring both data complexity and correctness. CoVe begins by defining explicit task constraints, which serve a dual role: they guide the generation of complex trajectories and act as deterministic verifiers for assessing trajectory quality. This enables the creation of high-quality training trajectories for supervised fine-tuning (SFT) and the derivation of accurate reward signals for reinforcement learning (RL). Our evaluation on the challenging $τ^2$-bench benchmark demonstrates the effectiveness of the framework. Notably, our compact \textbf{CoVe-4B} model achieves success rates of 43.0\% and 59.4\% in the Airline and Retail domains, respectively; its overall performance significantly outperforms strong baselines of similar scale and remains competitive with models up to $17\times$ its size. These results indicate that CoVe provides an effective and efficient pathway for synthesizing training data for state-of-the-art interactive tool-use agents. To support future research, we open-source our code, trained model, and the full set of 12K high-quality trajectories used for training.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决训练多轮交互式工具使用智能体时面临的核心挑战：如何高效生成兼具复杂性和正确性的高质量训练数据。研究背景是大语言模型（LLM）推动了从文本生成到任务自动化的范式转变，但现有智能体在应对复杂、模糊的真实用户需求时仍存在不足，因为这些需求需要智能体通过多轮交互澄清意图，并最终转化为确定性的工具调用动作。

现有方法的不足主要体现在数据获取和质量控制上。依赖人工标注成本高昂、难以扩展；而利用LLM自动生成交互轨迹和验证的方法，由于LLM本身具有不可控性，既无法保证生成任务的“可解决性”，也难以确保轨迹验证的绝对正确性。此外，受限于自身能力，LLM倾向于生成工具调用次数和对话轮数较少的简单任务，难以产生具有挑战性的复杂样本，从而限制了智能体高级能力的涌现。

因此，本文要解决的核心问题是：提出一个能够同时确保数据复杂性和轨迹正确性的后训练数据合成框架。为此，论文引入了CoVe（约束验证）框架。该框架通过预先定义明确的任务约束来指导复杂轨迹的生成，并利用这些约束作为确定性验证器来严格评估轨迹质量，从而自动化地合成高质量数据，以支持监督微调（SFT）和强化学习（RL）的训练。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为**基础工具使用智能体研究**和**多轮交互数据合成框架**两大类。

在**基础工具使用智能体**方面，TALM、Toolformer和ReAct等开创性工作展示了大型语言模型调用外部API的潜力，后续研究将其应用于代码生成、GUI导航等复杂领域。然而，这些工作大多聚焦于单轮、需求明确的场景。近期，受相关基准测试推动，**多轮交互式工具使用智能体**研究开始兴起，其核心挑战在于初始用户需求模糊，需通过交替澄清与执行来逐步完成任务。

针对高质量交互数据获取难的问题，出现了多种**自动化数据合成框架**。APIGen-MT采用“蓝图到对话”流程并验证质量；Simia利用LLM模拟环境和用户反馈以支持SFT和RL的扩展训练；GEM从大规模文本中挖掘隐式多步流程并转化为可执行轨迹；MUA-RL则在强化学习中集成动态用户模拟以优化策略。

**本文与这些工作的区别在于**：现有合成方法或依赖LLM模拟（可能引入错误），或从文本中挖掘流程（可能不精确）。而本文提出的CoVe框架**以明确的任务约束为数据生成的起点**。约束不仅指导生成复杂轨迹，更作为确定性验证器来评估轨迹质量，从而在保证数据复杂性的同时，确保了其正确性，为SFT和RL提供了更可靠的数据与奖励信号。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为CoVe（约束引导验证）的后训练数据合成框架来解决多轮交互式工具使用智能体训练中数据复杂性与正确性难以兼顾的问题。其核心方法是利用显式的任务约束来同时引导复杂轨迹的生成和作为确定性验证器来评估轨迹质量，从而生成高质量的训练数据。

整体框架包含三个主要阶段：约束采样、约束模糊化和轨迹生成与验证。首先，从沙盒数据库中采样一组确定性的约束条件集合C，这些约束定义了任务的具体目标，并确保任务的可解性。接着，通过“模糊化”策略将约束中的精确标识符（如订单ID）转换为更接近真实用户表达的模糊描述集合F，例如将订单ID替换为订单中包含的随机商品子集，同时保持逻辑上的唯一性。这一步骤引入了现实世界中的模糊性，迫使智能体进行推理或查询。

在轨迹生成阶段，一个用户模拟器大语言模型基于模糊化指令F，以渐进、自然的方式与智能体进行多轮对话，模拟用户逐步提出需求的过程。智能体需要澄清模糊信息、通过对话同步信息并调用工具来解决问题。对话以特定的终止标记结束，形成包含对话历史和工具调用的轨迹τ。

关键的创新点在于随后的轨迹验证阶段。CoVe设计了一个基于规则的确定性验证函数V(τ, C)，它使用原始的确定性约束集合C作为真实性的检查清单，来严格评估轨迹τ中的工具执行是否满足了C中的所有条件，并且没有冗余操作。验证器关注的是最终结果是否达成，而非固定的动作序列，这提供了评估的灵活性。根据约束满足率和冗余操作数计算出的综合分数，用于筛选出完全正确（分数为1）的轨迹用于监督微调（SFT），或直接作为奖励信号用于强化学习（RL）中的策略更新。

因此，CoVe通过将约束的双重用途（生成引导与验证标准）紧密结合在一个框架内，确保了合成数据既复杂（源于模糊化）又正确（源于确定性验证），为训练先进的交互式工具使用智能体提供了一条高效途径。

### Q4: 论文做了哪些实验？

论文实验主要围绕验证CoVe框架的有效性展开。实验设置方面，以Qwen3-4B-Instruct-2507为基础模型，使用VeRL框架进行训练。SFT阶段采用AdamW优化器，学习率为1e-6，全局批次大小为128；RL阶段采用GRPO算法，学习率保持1e-6，训练批次大小为64。评估在τ²-bench基准的Airline和Retail两个复杂交互领域进行，遵循其默认协议并禁用think工具，使用pass¹到pass⁴的严格指标评估模型在连续k次独立运行中的成功稳定性。

对比方法包括代表性的闭源模型（如GPT-5、GPT-4o）以及不同参数规模的开源模型（如Qwen3-235B、xLAM-2系列、Simia-Tau系列、GEM系列等）。主要结果显示，CoVe-4B在≤8B参数组中表现极具竞争力：在Airline领域pass¹为43.0%，Retail领域为59.4%，平均pass¹达到51.2%，显著优于同规模基线（如Simia-Tau-RL-8B的47.7%），甚至媲美部分∼30B模型（如xLAM-2-32b-fc-r的49.5%），并与规模大17倍的xLAM-2-70b-fc-r（51.5%）性能接近。相比基础模型Qwen3-4B-Instruct，平均pass¹绝对提升了18.6%。

此外，数据质量对比实验表明，在控制5K轨迹规模下，CoVe-5K平均pass¹（44.7%）优于APIGen-MT-5K（41.7%）和Simia-5K（39.7%），且仅用约5.5%数据量即达到与Simia-90K（44.3%）相当的效果。扩展到CoVe-12K后，平均pass¹进一步提升至51.2%。训练范式比较显示，纯SFT效果最佳（51.2%），纯RL为40.7%，而SFT+RL组合（46.9%）因环境瓶颈导致性能下降。轨迹生成动态分析揭示，使用Gemini-3-Pro作为用户模拟器时成功率更高（平均74.0%），且Retail领域的生成成功率普遍高于Airline领域。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在其训练流程和评估范围上。当前，由于在线交互中使用的开源模拟器能力有限，导致序列化的监督微调（SFT）加强化学习（RL）流程效果反而不如纯SFT。此外，研究目前仅聚焦于τ²-bench中的航空和零售两个领域，限制了对其泛化能力的全面验证。

未来研究方向可从多个层面展开。首先，核心是提升用户模拟器的性能，具体路径包括：采用能力更强的大语言模型作为模拟器；利用现有生成管道收集的上下文数据，专门训练一个用户模拟器模型；或通过提示工程优化现有模拟器，使其能准确判断对话终止时机。其次，需要将CoVe框架扩展到更广泛的领域进行验证，例如τ²-bench中的电信领域或其他多轮交互工具使用基准（如BFCL），以检验其普适性。

结合个人见解，可能的改进思路还包括：探索离线强化学习或更高效的在线交互采样策略，以降低对高保真模拟器的依赖；研究如何将约束验证过程本身进行参数化或轻量化，使其能更灵活地适应新领域或新工具，而无需完全重新定义约束；考虑引入课程学习或分层强化学习，让智能体从简单约束的任务开始，逐步学习处理更复杂、模糊的用户需求。

### Q6: 总结一下论文的主要内容

本文提出了CoVe（约束验证）框架，旨在解决训练多轮交互式工具使用智能体时面临的挑战：现实用户需求复杂模糊，而智能体需执行确定性动作以满足需求。其核心贡献在于通过显式任务约束来引导高质量训练数据的合成与验证。具体方法上，CoVe首先定义明确的任务约束，这些约束兼具双重作用：一方面引导生成复杂的多轮交互轨迹以模拟真实场景，另一方面作为确定性检查清单来严格验证轨迹的正确性。由此生成的数据既可用于监督微调（SFT），也能为强化学习（RL）提供精确的奖励信号。实验在具有挑战性的τ²-bench基准上进行，结果表明CoVe框架极具效力和数据效率：仅40亿参数的紧凑模型CoVe-4B在航空和零售领域分别达到43.0%和59.4%的成功率，整体性能显著超越同规模基线，并与规模大17倍的模型竞争。这证明CoVe为合成高质量训练数据、开发先进交互式工具使用智能体提供了一条高效路径。
