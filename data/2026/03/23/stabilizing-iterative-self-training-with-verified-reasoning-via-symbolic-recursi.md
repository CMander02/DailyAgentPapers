---
title: "Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment"
authors:
  - "Xinyu Zhang"
date: "2026-03-23"
arxiv_id: "2603.21558"
arxiv_url: "https://arxiv.org/abs/2603.21558"
pdf_url: "https://arxiv.org/pdf/2603.21558v1"
categories:
  - "cs.AI"
tags:
  - "自我训练"
  - "推理验证"
  - "符号验证"
  - "递归自对齐"
  - "数据过滤"
  - "偏好学习"
  - "数学推理"
relevance_score: 7.5
---

# Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment

## 原始摘要

Recursive self-improvement--where a model iteratively trains on its own outputs--promises sustained capability growth but faces a fundamental obstacle: recursive drift. As models train on self-generated data across multiple iterations, errors in intermediate reasoning compound, leading to mode collapse and performance degradation. We propose Neuro-Symbolic Recursive Self-Alignment (NSRSA), which stabilizes iterative self-training by embedding a symbolic verification subsystem that gates training data quality at the reasoning step level. Unlike outcome-only filtering (which admits "lucky guesses" with flawed reasoning), NSRSA verifies each arithmetic operation via sympy, checks logical flow consistency across reasoning steps, and enforces domain constraints. We evaluate NSRSA on GSM8K using Qwen3-4B-Thinking across 5 self-training iterations under five conditions: no verification, outcome verification, majority voting, full NSRSA symbolic verification, and NSRSA with DPO. Our filtering analysis shows that NSRSA rejects approximately 34% of correct-answer solutions that pass outcome verification, eliminating "lucky guesses" with flawed reasoning from the training set. We further demonstrate that constructing DPO preference pairs from NSRSA verification teaches the model to distinguish sound from flawed reasoning (reward accuracy 46% to 63%). NSRSA provides an extensible framework that demonstrates how external symbolic verification can make recursive self-improvement measurable and reliable within domains where automated verification is available.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在递归自我改进过程中出现的“递归漂移”问题。研究背景是递归自我改进（RSI）——即模型通过迭代地使用自身生成的数据进行训练以实现能力持续提升——被视为AI发展的核心愿景。现有方法，如自我训练和自我奖励模型，通常仅依赖结果验证（即最终答案是否正确）来筛选训练数据。这种方法的不足在于，它无法识别并过滤掉那些通过错误推理过程却侥幸得到正确答案的“幸运猜测”。当这些包含错误推理链的解决方案被加入训练集时，模型会学习并复制这些有缺陷的推理模式，导致错误在多次迭代中不断累积和放大，最终引发模型崩溃或性能系统性下降。

因此，本文要解决的核心问题是：如何稳定递归自我训练过程，防止因错误推理链的传播而导致的性能退化。论文提出的解决方案是神经符号递归自对齐框架，其核心思想在于验证的粒度决定了递归稳定的深度。该框架通过嵌入一个符号验证子系统，在推理步骤级别对训练数据进行质量把关，不仅验证最终答案，还使用符号计算工具验证每一步算术运算的正确性、检查逻辑流的一致性以及确保领域约束得到满足，从而从根本上排除有缺陷的推理，使模型能够从真正正确的推理链中学习，实现更可靠、更稳定的递归自我改进。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为四类：

**1. 推理自训练方法**：如STaR通过筛选能得出正确答案的自我生成推理链进行训练，ReST-EM采用EM框架进行多轮采样，V-STaR同时训练生成器和验证器，Self-rewarding语言模型则让模型自身担任评判。这些方法主要依据最终答案的正确性进行过滤。本文提出的NSRSA与这些工作的核心关系是**继承并扩展了自训练框架**，关键区别在于引入了**步骤级的符号验证**来提升训练数据质量，而非仅依赖结果。

**2. 过程监督**：已有研究表明，在训练数学推理模型时，对每个推理步骤进行监督（过程监督）优于仅监督最终结果。本文与这些工作的关系是**目标一致**，都强调步骤正确性的重要性。主要区别在于，现有工作通常依赖**人工标注**的步骤标签，而NSRSA通过符号计算实现了**全自动的步骤级验证**。

**3. 神经符号推理**：例如TORA将工具使用（包括符号计算）集成到推理过程中，生成式定理证明器则采用形式化验证。本文与这些工作的关系是**共享了“利用符号方法提升可靠性”的核心思想**。区别在于，NSRSA将符号验证**应用于训练数据的过滤环节**，而非推理过程本身，因此与这些推理时的方法**是互补的**。

**4. 模型崩溃研究**：有研究指出，在模型自生成数据上训练会导致质量逐渐退化，且大语言模型在没有外部反馈时难以自我纠正。本文工作与这些研究是**问题与解决方案的关系**。NSRSA直接针对递归自训练中的“递归漂移”和错误复合问题，通过提供**外部符号反馈**来防止错误在迭代中传播，从而稳定训练过程。

### Q3: 论文如何解决这个问题？

论文通过提出“神经符号递归自对齐（NSRSA）”方法来解决迭代自训练中的递归漂移问题。其核心思想是在自训练循环中嵌入一个符号验证子系统，在推理步骤级别对训练数据进行严格的质量把关，从而稳定训练过程。

整体框架是一个递归自训练循环。每一轮迭代包含四个步骤：生成、验证、训练和评估。关键创新在于验证过滤器V的设计。NSRSA的验证子系统包含四个层级的检查：1）最终答案正确性：提取最终数值答案并与标准答案匹配；2）算术正确性：使用sympy符号计算库解析并验证推理链中的每个算术表达式（如“A ⊙ B = C”），要求至少80%的可解析表达式计算正确；3）逻辑流一致性：通过字符串匹配跟踪变量赋值历史，检测跨步骤的“幻觉中间值”（即变量被重新赋值为显著不同且不合理的值）；4）领域约束：强制执行非负性、整数性等数学问题约束。

主要模块包括：生成模块（从当前模型采样多个候选解决方案）、符号验证器（执行上述四级检查）、训练模块（使用通过验证的数据微调模型）。创新点体现在：将符号验证深度集成到数据过滤中，超越了仅依赖最终答案正确性的传统方法；通过逻辑流一致性检查捕捉推理过程中的内在矛盾；利用验证结果构建DPO偏好对（选择通过全部验证的解决方案作为正例，拒绝最终答案正确但推理有缺陷的“侥幸猜测”作为负例），直接教导模型区分正确与有缺陷的推理。

该方法通过排除约34%虽答案正确但推理有误的“侥幸猜测”，从根本上减少了错误在迭代中的累积，使递归自我改进变得可测量和可靠。

### Q4: 论文做了哪些实验？

论文在GSM8K和MATH-500数据集上进行了实验，主要评估NSRSA方法在迭代自训练中的稳定性和效果。实验使用Qwen3-4B-Thinking模型，采用LoRA适配器进行微调，并进行了5轮自训练迭代。每轮为每个训练问题生成8个解决方案。

对比方法包括五种条件：无验证、仅结果验证、多数投票、完整的NSRSA符号验证以及NSRSA结合DPO。主要评估指标包括GSM8K测试准确率、MATH-500跨任务迁移准确率、Pass@k、验证率、Self-BLEU和递归深度。

关键结果显示，在GSM8K上，经过5轮迭代，无验证方法准确率从基线的80.5%崩溃至73.2%（递归深度为2）；仅结果验证和多数投票方法在约86%处停滞；而NSRSA符号验证稳步提升至91.0%，NSRSA+DPO达到91.2%。NSRSA在首轮迭代中过滤掉了约34%答案正确但推理有误的“侥幸猜测”解决方案。在MATH-500上，NSRSA实现了从45.5%到51.2%的正向跨任务迁移。此外，NSRSA条件下的验证率（答案正确且通过全部符号检查的比例）随迭代提升，表明模型学会了产生可验证的推理。Self-BLEU指标显示，NSRSA能有效维持解决方案多样性（第5轮为0.35），而无验证方法则出现严重的模式崩溃（升至0.64）。DPO训练使奖励准确率从46%提升至63%。

### Q5: 有什么可以进一步探索的点？

本文提出的NSRSA方法通过符号验证稳定了迭代自训练，但仍存在一些局限性和值得深入探索的方向。首先，当前方法高度依赖特定领域（如数学）的符号验证器，其约束检查和解析器覆盖范围有限。对于自然语言表述或复杂多行推导，解析器可能无法提取表达式，导致错误检测不足而非误拒，这限制了其在更广泛领域的直接应用。其次，验证过程可能过滤过于严格，在模型早期性能较弱时，过激的过滤会减少有效训练数据，影响学习效率。

未来研究可以从以下几个方向展开：一是将NSRSA与轻量级过程奖励模型（PRMs）结合，PRMs可为难以符号验证的推理步骤（如问题分解质量、策略选择）提供软性评分，而NSRSA则确保算术和逻辑一致性的硬性保证，形成互补。二是扩展领域适用性，探索在代码生成、逻辑谜题或形式化定理证明等领域的应用，这需要设计相应的领域特定解析器和约束集。三是研究更稳健的解析技术，如基于NLP的解析方法，以提高对自然语言表达和复杂推导的覆盖能力，减少错误漏检。最后，可以深入探究递归稳定性的深度边界，分析验证信号质量与模型递归改进上限之间的关系，为构建更通用的递归自我改进框架提供理论依据。

### Q6: 总结一下论文的主要内容

本文针对递归自改进中因中间推理错误累积导致的“递归漂移”问题，提出了一种名为神经符号递归自对齐（NSRSA）的稳定化框架。其核心贡献在于将符号验证子系统嵌入自训练循环，在推理步骤级别对训练数据进行质量把关。具体方法上，NSRSA使用sympy验证每个算术运算的正确性，检查推理步骤间的逻辑流一致性，并强制执行领域约束，从而能够剔除仅凭“幸运猜测”得出正确答案但推理过程存在缺陷的样本。实验在GSM8K数学推理数据集上进行，经过五轮自训练迭代，结果表明：无验证的方法性能崩溃至73.2%，仅验证结果的方法停滞在85.8%，而NSRSA将准确率从基线80.5%提升至91.0%。分析显示，NSRSA过滤掉了约34%能通过结果验证但推理有误的“幸运猜测”样本。此外，利用NSRSA构建的偏好对进行DPO训练，能有效教会模型区分合理与有缺陷的推理。该工作为在可自动化验证的领域内，实现可测量且可靠的递归自我改进提供了一个可扩展的原则性框架。
