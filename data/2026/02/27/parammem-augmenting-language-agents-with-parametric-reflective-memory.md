---
title: "ParamMem: Augmenting Language Agents with Parametric Reflective Memory"
authors:
  - "Tianjun Yao"
  - "Yongqiang Chen"
  - "Yujia Zheng"
  - "Pan Li"
  - "Zhiqiang Shen"
  - "Kun Zhang"
date: "2026-02-26"
arxiv_id: "2602.23320"
arxiv_url: "https://arxiv.org/abs/2602.23320"
pdf_url: "https://arxiv.org/pdf/2602.23320v2"
categories:
  - "cs.LG"
  - "cs.MA"
tags:
  - "Agent 架构"
  - "记忆模块"
  - "自我反思"
  - "推理"
  - "参数化记忆"
  - "Agent 自演化"
  - "代码生成"
  - "数学推理"
  - "问答"
relevance_score: 9.5
---

# ParamMem: Augmenting Language Agents with Parametric Reflective Memory

## 原始摘要

Self-reflection enables language agents to iteratively refine solutions, yet often produces repetitive outputs that limit reasoning performance. Recent studies have attempted to address this limitation through various approaches, among which increasing reflective diversity has shown promise. Our empirical analysis reveals a strong positive correlation between reflective diversity and task success, further motivating the need for diverse reflection signals. We introduce ParamMem, a parametric memory module that encodes cross-sample reflection patterns into model parameters, enabling diverse reflection generation through temperature-controlled sampling. Building on this module, we propose ParamAgent, a reflection-based agent framework that integrates parametric memory with episodic and cross-sample memory. Extensive experiments on code generation, mathematical reasoning, and multi-hop question answering demonstrate consistent improvements over state-of-the-art baselines. Further analysis reveals that ParamMem is sample-efficient, enables weak-to-strong transfer across model scales, and supports self-improvement without reliance on stronger external model, highlighting the potential of ParamMem as an effective component for enhancing language agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于自反思的语言智能体在复杂推理任务中，因反思内容重复且缺乏多样性而导致的性能瓶颈问题。研究背景是，大型语言模型在推理任务中常采用测试时扩展策略，其中基于反思的框架通过让智能体在多次尝试中积累自我反思（存储于情景记忆）来改进解决方案，已在编程、数学推理等领域取得成效。然而，现有方法（如Reflexion）存在明显不足：自反思过程容易产生重复且不准确的输出，限制了推理效果的进一步提升。近期研究尝试通过提示级修改（如DoT）或引入跨样本轨迹检索（如DoT-bank）来增加反思多样性，虽有一定效果，但前者改进有限，后者依赖嵌入相似性检索，难以捕捉组合性模式，且嵌入易坍缩到低秩子空间，导致检索多样性受限。

本文的核心问题是：如何进一步扩展反思多样性，以显著提升语言智能体的推理性能？为此，论文提出了ParamMem，一种参数化记忆模块，通过将跨样本反思模式编码到模型参数中，从根本上改变多样性生成机制。该方法不依赖提示变体或显式检索，而是通过在小规模辅助反思数据集上微调轻量级参数模块，使模块在推理时能基于学习到的模式生成多样化反思，从而突破现有方法的局限性。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提升语言智能体自反思能力的多样性展开，可分为方法类和应用类。

在方法类中，相关工作主要包括两类。一是基于情景记忆的反思框架，如 Reflexion 和 DoT，它们通过存储智能体自身迭代中的反思来指导后续推理，但容易产生重复输出，限制性能。二是引入跨样本记忆的方法，如 DoT-bank，它利用外部已解决问题的轨迹库来丰富反思的输入多样性，已被证明能有效提升推理能力。

本文提出的 ParamMem 与上述工作密切相关但存在区别。ParamMem 是一种参数化记忆模块，其核心创新在于将跨样本的反思模式编码到模型参数中，并通过温度控制采样生成多样化反思。这不同于仅依赖固定轨迹检索的跨样本记忆。基于此模块构建的 ParamAgent 框架，首次将情景记忆、跨样本记忆和参数化记忆三者集成，从而在反射多样性上实现了进一步突破。实验表明，该框架在代码生成、数学推理等任务上超越了现有最佳基线，并展现出样本高效性和跨模型规模的弱到强迁移能力。

### Q3: 论文如何解决这个问题？

论文通过引入一个名为ParamMem的参数化记忆模块，并结合一个名为ParamAgent的反思型智能体框架来解决自我反思过程中输出重复、多样性不足的问题。核心方法是将跨样本的反思模式编码到模型参数中，从而生成多样化的反思信号，以提升任务解决能力。

整体框架分为两个主要阶段。首先，构建ParamMem模块：通过收集一个辅助数据集，其中每个样本包含输入任务（如编程问题）和由大型语言模型生成的反思反馈（如潜在错误枚举）或分解后的语义单元（针对多跳问答）。使用LoRA技术对预训练语言模型进行微调，得到一个参数化模块，该模块能够学习跨样本的规律，并可通过温度控制采样生成新颖的反思，而非依赖固定模板或检索相似样本。这提供了额外的多样性来源。

其次，将ParamMem集成到反思型智能体框架中。在每次迭代中，智能体不仅基于历史自我反思，还从ParamMem中采样一个全局级反思（或分解任务），并将其与历史反思拼接，共同作为条件生成新的解决方案。此外，论文还提出了ParamAgent-plus变体，额外从已解决任务的记忆库中检索推理轨迹，结合参数化和跨样本信号进一步强化条件生成。

关键技术包括：1）利用训练动态隐式捕获跨样本规律，实现泛化；2）温度控制采样，调节反思多样性；3）结合参数化记忆、情景记忆和跨样本记忆的多源记忆机制。创新点在于通过参数化模块内生地增强反思多样性，避免对外部强模型的依赖，并支持跨模型规模的弱到强迁移以及自我改进能力。实验表明，该方法在代码生成、数学推理和多跳问答任务上均取得了稳定提升。

### Q4: 论文做了哪些实验？

论文在代码生成、数学推理和多跳问答三个领域进行了广泛的实验。实验设置方面，所有方法（包括基线）均固定迭代次数为5次；对于ParamAgent，首次迭代采样温度设为0.2，后续迭代设为1.0以促进多样性。参数化记忆模块使用Llama3.1-8B-Instruct实例化，并通过LoRA进行微调（秩r=128，缩放因子α=32，学习率2e-5，训练3轮）。

使用的数据集/基准测试包括：代码生成任务采用HumanEval和MBPP（以及更具挑战性的LiveCodeBench进行额外评估）；数学推理采用涵盖七个学科竞赛级问题的MATH数据集；多跳问答采用HotpotQA和2WikiMultiHopQA。评估指标上，代码任务报告Pass@1，数学和QA任务报告0-1准确率。

对比方法包括：无反思的基础LLM代理（Base）、使用情景自反思的Reflexion、同样采用参数化模块但通过策略梯度优化以提高反思准确性的Retroformer、通过提示增强多样性的DoT，以及进一步结合记忆库的DoT-bank。实验在Llama-3.1-8B、Mistral-7B-v0.2和Qwen2-1.5B-instruct三个不同规模的骨干模型上进行。

主要结果显示，ParamAgent在多个任务上一致优于基线。关键数据指标如下：在HumanEval上，ParamAgent使用Llama-3.1-8B达到82.93%的Pass@1，显著优于Base的59.15%和最佳基线DoT-bank的79.56%；在MBPP上达到67.00%（Base为47.61%）；在MATH上，ParamAgent-plus达到75.45%（Base为48.20%）；在HotpotQA上达到78.33%（Base为57.67%）；在2WikiMultiHopQA上达到88.67%（Base为40.33%）。分析表明，参数化记忆模块通过训练动态引入了额外的反思多样性，其生成的反思在静态和动态设置下均表现出更高的语义变化（通过成对余弦距离和聚类轮廓系数衡量），且这种多样性提升与任务成功呈强正相关。此外，研究验证了方法在不依赖更强外部模型的情况下实现自我改进、支持小模块对强代理的弱到强迁移，并具有样本高效性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从以下几个方面探讨。首先，ParamMem 虽能提升反思多样性，但其性能增益在不同任务上不均衡，例如在数学推理上，跨样本记忆似乎比参数化模块更重要，这表明模块的有效性可能高度依赖于任务特性。未来可研究如何动态调整参数化记忆与外部记忆的权重，或设计任务自适应的多样性生成策略。

其次，实验显示参数化模块的训练数据质量（如由GPT-4o-mini生成）显著影响多样性，这暗示了数据偏差风险。未来可探索更稳健的数据合成方法，例如通过对抗训练或课程学习来减少分布偏移，或研究无监督/自监督的预训练目标，以降低对强外部模型的依赖。

此外，ParamAgent 在推理时消耗的提示令牌数显著增加（尤其在MBPP等任务上），可能影响实际部署效率。未来可优化记忆检索与生成机制，例如引入稀疏激活或知识蒸馏，以平衡性能与计算开销。

最后，论文未深入探讨反思多样性与最终解决质量之间的因果机制。未来可结合可解释性分析（如追踪反思路径对决策的影响）来验证多样性如何引导更优的推理，并探索将参数化记忆与符号推理等模块结合，以处理更复杂的多步骤任务。

### Q6: 总结一下论文的主要内容

该论文提出了一种增强语言智能体自我反思能力的新方法。核心问题是现有基于反思的智能体在迭代优化解决方案时，常产生重复性输出，限制了推理性能的提升。论文通过实证分析发现反思多样性与任务成功率呈强正相关，从而强调了生成多样化反思信号的重要性。

为此，作者提出了**ParamMem**，一个参数化记忆模块。其核心方法是将从多个样本中学习到的跨样本反思模式编码到模型参数中，并通过温度控制采样来生成多样化的反思。基于此模块，论文进一步构建了**ParamAgent**框架，该框架将参数化记忆与情景记忆、跨样本记忆相结合。

主要结论是，在代码生成、数学推理和多跳问答任务上的大量实验表明，该方法持续超越了现有最优基线。进一步分析显示，ParamMem具有样本高效性，支持不同模型规模间的弱到强知识迁移，并能不依赖更强的外部模型实现自我改进。其核心贡献在于为增强语言智能体的反思与推理能力提供了一个有效且通用的参数化记忆组件。
