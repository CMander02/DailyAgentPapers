---
title: "ParamMem: Augmenting Language Agents with Parametric Reflective Memory"
authors:
  - "Tianjun Yao"
  - "Yongqiang Chen"
  - "Yujia Zheng"
  - "Pan Li"
  - "Zhiqiang Shen"
date: "2026-02-26"
arxiv_id: "2602.23320"
arxiv_url: "https://arxiv.org/abs/2602.23320"
pdf_url: "https://arxiv.org/pdf/2602.23320v1"
categories:
  - "cs.LG"
  - "cs.MA"
tags:
  - "Reasoning & Planning"
  - "Memory & Context Management"
relevance_score: 9.0
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Memory & Context Management"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "ParamMem, ParamAgent"
  primary_benchmark: "N/A"
---

# ParamMem: Augmenting Language Agents with Parametric Reflective Memory

## 原始摘要

Self-reflection enables language agents to iteratively refine solutions, yet often produces repetitive outputs that limit reasoning performance. Recent studies have attempted to address this limitation through various approaches, among which increasing reflective diversity has shown promise. Our empirical analysis reveals a strong positive correlation between reflective diversity and task success, further motivating the need for diverse reflection signals. We introduce ParamMem, a parametric memory module that encodes cross-sample reflection patterns into model parameters, enabling diverse reflection generation through temperature-controlled sampling. Building on this module, we propose ParamAgent, a reflection-based agent framework that integrates parametric memory with episodic and cross-sample memory. Extensive experiments on code generation, mathematical reasoning, and multi-hop question answering demonstrate consistent improvements over state-of-the-art baselines. Further analysis reveals that ParamMem is sample-efficient, enables weak-to-strong transfer across model scales, and supports self-improvement without reliance on stronger external model, highlighting the potential of ParamMem as an effective component for enhancing language agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于反思的语言智能体在自我反思过程中容易产生重复、低质量输出，从而限制其推理性能提升的问题。研究背景是，大型语言模型在复杂推理任务中展现出显著进步，其中基于反思的框架通过在推理时进行多轮自我反思来积累经验、改进解决方案，已被证明是一种有效的“测试时扩展”方法。然而，现有方法（如Reflexion、DoT等）存在明显不足：它们生成的反思内容往往重复且不够准确，这制约了智能体的性能提升。虽然近期研究尝试通过修改提示词（DoT）或引入基于检索的跨样本轨迹（DoT-bank）来增加反思的多样性并取得初步成功，但提示方法改进有限，而检索方法依赖于嵌入相似度，其捕捉组合模式的能力有限，且学习到的嵌入容易坍缩到低秩子空间，反而降低了检索的多样性。

本文的核心问题是：如何进一步扩大反思的多样性，以实现更强的推理性能？为此，论文提出了ParamMem，一种参数化反思记忆模块。它通过一种根本不同的机制来提供多样性：该模块在一个辅助反思数据集上进行轻量级微调，将跨样本的反思模式编码到其参数中；在推理时，它基于这些学习到的模式进行泛化生成反思，而非检索现有示例。这旨在克服检索方法的局限性，更有效地捕获和生成多样化的反思信号。基于此模块构建的ParamAgent框架，将参数化记忆与情景记忆、跨样本记忆相结合，以期系统性地提升语言智能体的推理能力。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提升语言智能体自反思能力的各类方法展开，可分为以下几类：

**1. 基于提示的反思方法**：以Reflexion为代表，通过设计提示词引导智能体在任务失败后进行自我反思，并将反思记录存入情景记忆以指导后续尝试。这类方法简单直接，但容易产生重复、低效的反思，限制了性能提升。

**2. 旨在提升反思多样性的方法**：为克服上述局限性，近期研究尝试增加反思的多样性。例如，DoT通过修改提示模板来鼓励不同的反思角度；DoT-bank则进一步引入了跨样本记忆，通过检索相似任务的历史推理轨迹来丰富反思信号。这些方法初步证明了多样性对性能的积极影响，但DoT的提升有限，而DoT-bank这类检索方法依赖于嵌入相似度，其捕捉组合模式的能力有限，且嵌入易坍缩，影响了检索的多样性。

**本文工作与上述研究的关系与区别**：本文同样聚焦于通过提升反思多样性来增强智能体，并首先通过实证分析（发现反思多样性与任务成功率强相关）为这一方向提供了进一步的理论动机。在方法上，本文提出的ParamMem与DoT-bank有相似目标，但采用了根本不同的机制。ParamMem是一个参数化记忆模块，它通过在小规模辅助数据集上微调，将跨样本的反思模式编码到模型参数中，在推理时通过温度控制采样生成多样化反思，而非依赖检索。这使其能更有效地捕获和泛化复杂模式，克服了检索方法的局限性。基于ParamMem构建的ParamAgent框架，则整合了参数化记忆、情景记忆和跨样本记忆，形成了一个更统一和强大的反思智能体系统。

### Q3: 论文如何解决这个问题？

论文通过引入一个名为ParamMem的参数化记忆模块，并将其整合到反思型智能体框架ParamAgent中，来解决语言智能体自我反思过程中输出重复、多样性不足的问题。核心方法是通过微调一个预训练语言模型，使其学习跨样本的反思模式，从而生成多样化的反思信号，以增强智能体的推理能力。

整体框架包含两个主要阶段。第一阶段是基础ParamAgent，它结合了参数化记忆和情景记忆。具体而言，首先构建一个辅助数据集，其中每个样本包括输入任务（如编程问题）和由大型语言模型生成的反思反馈（如潜在错误枚举）或分解后的语义单元（针对多跳问答）。使用LoRA技术对此数据集进行微调，得到参数化模块M_g。在智能体每次迭代生成解决方案时，除了利用历史自我反思，还会从M_g中采样一个全局反思r_k^g，并将其与历史反思拼接，共同作为条件输入给执行模型（actor），以生成新的解决方案。若解决方案不正确，则生成自我反思并存入情景记忆。

第二阶段是增强版ParamAgent-plus，它在第一阶段基础上引入了跨样本记忆库。对于第一阶段未能解决的任务，智能体会从已解决任务的记忆库中检索相似的推理轨迹，并将这些轨迹与参数化反思、自我反思一起作为条件，重新尝试解决问题，从而利用更丰富的跨样本信息。

关键技术包括：1）参数化记忆模块的构建，通过微调隐式捕获跨样本规律，而非依赖固定模板或检索相似样本，从而能够插值和外推生成新颖反思；2）温度控制采样，通过调整温度参数控制反思生成的多样性；3）多类型记忆的集成，将参数化记忆、情景记忆和跨样本记忆有机结合，提供多层次、多样化的反思信号。创新点在于首次将参数化记忆引入反思型智能体，通过模型参数编码反思模式，实现了高效、多样的反思生成，并支持跨模型规模的弱到强迁移以及不依赖外部强模型的自改进能力。

### Q4: 论文做了哪些实验？

论文在代码生成、数学推理和多跳问答三个领域进行了广泛的实验。实验设置方面，所有方法（包括基线）均固定迭代次数为5次；对于ParamAgent，首次迭代采样温度设为0.2，后续迭代设为1.0以促进多样性。参数化记忆模块使用Llama3.1-8B-Instruct实例化，并通过LoRA进行微调（秩r=128，缩放因子α=32，学习率2e-5，训练3轮）。

使用的数据集/基准测试包括：代码生成任务采用HumanEval和MBPP，以及更具挑战性的LiveCodeBench进行额外评估；数学推理采用涵盖七个学科竞赛级问题的MATH数据集；多跳问答采用HotpotQA和2WikiMultiHopQA。评估指标上，代码任务报告Pass@1，数学和QA任务报告0-1准确率。

对比方法包括：无反思的基础LLM代理（Base）、使用情景自反思的Reflexion、同样采用参数化模块但通过策略梯度优化以提高反思准确性的Retroformer、通过提示增强多样性的DoT，以及进一步结合记忆库的DoT-bank。实验在Llama-3.1-8B、Mistral-7B-v0.2和Qwen2-1.5B-instruct三个不同规模的骨干模型上进行。

主要结果显示，ParamAgent在多个任务上一致优于基线。关键数据指标如下：在HumanEval上，ParamAgent使用Llama-3.1-8B达到82.93%的Pass@1，显著优于Base的59.15%和最佳基线DoT-bank的79.56%；在MBPP上，ParamAgent达到67.00%，优于Base的47.61%和DoT-bank的64.82%；在MATH上，ParamAgent-plus（增强版）达到75.45%，优于Base的48.20%和DoT-bank的73.02%；在多跳问答任务上，ParamAgent在HotpotQA和2WikiMultiHopQA上分别达到78.33%和88.67%的准确率，均优于对比方法。分析表明，参数化记忆模块通过训练动态引入了额外的反思多样性，其生成的反思在成对余弦距离和聚类分析中显示出更高的语义变化，这与其性能提升密切相关。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从以下几个方面探讨。首先，ParamMem 虽能提升反思多样性，但其性能增益在不同任务上不均衡，例如在数学推理（MATH）上，其表现弱于依赖跨样本轨迹的方法（如DoT-bank），这表明对于高度结构化的问题，多样反思的收益可能有限，未来可研究如何动态权衡反思的多样性与准确性，或针对不同任务类型自适应调整记忆模块的组合策略。其次，方法依赖于对参数化模块的微调，这带来了额外的计算成本与数据需求；尽管论文提到了样本效率，但未深入探讨在数据稀缺或领域迁移场景下的鲁棒性，未来可探索更高效的适配机制（如轻量级适配器）或元学习策略，以降低对大规模合成数据的依赖。此外，ParamMem 通过温度控制采样来生成多样反思，但温度参数的设置缺乏理论指导，且可能影响生成质量；未来可研究更精细的多样性控制机制，例如基于不确定性或置信度的自适应采样。最后，论文验证了弱到强的知识迁移，但未探索跨模型架构或跨任务的泛化能力；未来可研究如何将参数化记忆模块作为可移植的“反思技能”库，在不同智能体间共享与复用，从而进一步提升学习效率与泛化性。

### Q6: 总结一下论文的主要内容

该论文提出了一种增强语言智能体自我反思能力的新方法。针对现有反思机制容易产生重复输出、限制推理性能的问题，作者通过实证分析发现反思多样性与任务成功率呈强正相关。为此，论文核心贡献是引入了**ParamMem**，一个参数化记忆模块，它将跨样本的反思模式编码到模型参数中，并通过温度控制采样来生成多样化的反思信号。基于此模块，作者构建了**ParamAgent**框架，该框架将参数化记忆与情景记忆、跨样本记忆相结合。实验在代码生成、数学推理和多跳问答任务上进行，结果表明该方法 consistently 超越了现有最优基线。进一步分析显示，ParamMem 具有样本高效性，支持不同模型规模间的弱到强知识迁移，并且能够在不依赖更强外部模型的情况下实现自我改进，这凸显了其作为增强语言智能体有效组件的潜力。
