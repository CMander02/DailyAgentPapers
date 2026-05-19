---
title: "Implicit Hierarchical GRPO: Decoupling Tool Invocation from Execution for Tool-Integrated Mathematical Reasoning"
authors:
  - "Li Wang"
  - "Xiaohan Wang"
  - "Xiaodong Lu"
  - "Zipeng Zhang"
  - "Jinyang Wu"
  - "Jiajun Chai"
  - "Wei Lin"
  - "Guojun Yin"
date: "2026-05-18"
arxiv_id: "2605.18500"
arxiv_url: "https://arxiv.org/abs/2605.18500"
pdf_url: "https://arxiv.org/pdf/2605.18500v1"
github_url: "https://github.com/Lumina04/IH-GRPO-01"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "工具使用集成推理"
  - "分层强化学习"
  - "隐式分层GRPO"
  - "数学推理"
  - "延迟执行"
  - "多智能体协同"
relevance_score: 9.5
---

# Implicit Hierarchical GRPO: Decoupling Tool Invocation from Execution for Tool-Integrated Mathematical Reasoning

## 原始摘要

Large language models (LLMs) have increasingly leveraged tool invocation to enhance their reasoning capabilities. However, existing approaches typically tightly couple tool invocation with immediate execution. Such immediate tool interaction may disrupt the reasoning coherence of LLMs and constrain their expressivity, ultimately degrading reasoning performance. To this end, for the first time, we propose and formalize the problem of decoupling tool invocation from execution during reasoning, and introduce delayed execution with explicit control to enhance tool-integrated reasoning (TIR). Furthermore, we propose a hierarchical control framework and theoretically derive a surrogate loss that enables an implicitly hierarchical policy to learn behavior equivalent to that of an explicit hierarchical policy, leading to the proposed IH-GRPO algorithm. Extensive experiments on IH-GRPO achieve absolute improvements of 1.87\%, 2.16\%, and 2.53\% on Qwen3-1.7B, Qwen3-4B, and Qwen3-8B across six out-of-domain mathematical reasoning benchmarks over the strongest baseline method, while also yielding consistent performance gains in other domains. Our code is available at https://github.com/Lumina04/IH-GRPO-01.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有工具整合推理（TIR）方法中工具调用与执行紧密耦合所导致的问题。研究背景是，强化学习已被用于增强大语言模型的推理能力，而工具整合推理（如代码工具）能进一步提升模型处理复杂数学推理任务的表现。然而，现有方法的不足在于：它们通常将工具调用（如生成代码块）与立即执行绑定，缺乏判断何时需要外部反馈的机制。这种紧耦合方式存在三个主要缺陷：一是过早的中断会破坏模型推理的连贯性，因为模型可能只是在定义中间变量而非请求外部反馈；二是这种模式要求每个代码块必须是可立即执行的完整单元，限制了模型在多个代码片段间灵活穿插文本推理的能力，从而约束了推理模式的表达力和多样性；三是在复杂计算中，手动计算容易出错，而僵化的工具使用模式无法让模型灵活利用代码处理中间步骤，增加了推理错误的可能性。因此，本文的核心问题是：如何首次形式化并实现工具调用与执行在推理过程中的解耦，让模型能自主决策何时执行代码，从而保持推理连贯性、增强推理模式的灵活性，并最终提升数学推理性能。为此，论文提出了IH-GRPO算法，通过分层控制机制和理论推导的代理损失函数来实现这一目标。

### Q2: 有哪些相关研究？

在相关研究中，工具增强推理（TIR）主要通过两类方法展开：一类是监督微调（SFT）或直接偏好优化（DPO），如ReAct将推理与行动结合，Chain-of-Code允许大模型并行执行伪代码和可执行代码；另一类是在SFT后引入强化学习（RL）或直接从零开始RL交互，SimpleTIR通过过滤无效轨迹缓解梯度不稳定问题。这些方法普遍将工具调用与执行紧密耦合，缺乏对何时需要外部反馈的感知，可能破坏推理连贯性。本文创新性地提出解耦工具调用与执行，引入延迟执行与显式控制，并通过RL训练单一模型。

在层次化学习方面，ReWOO先生成高层计划再在隔离上下文中执行子任务，CodeSteer通过多模型协作协调代码与文本推理。但这些方法依赖外部层次结构（如基于提示的计划、外部模型或手工流程），可能损害推理连续性和可扩展性。本文IH-GRPO通过理论推导的替代损失函数，在单一模型内隐式学习层次控制，无需外部干预即可实现计划与执行的分离，与现有方法形成本质区别。

### Q3: 论文如何解决这个问题？

该论文通过解耦工具调用与执行来解决现有方法中紧密耦合导致的推理连贯性受损和表达受限问题。核心方法包括：

1. **延迟执行机制**：提出新的推理轨迹定义，将文本生成、代码生成和工具执行信号分离。轨迹中，模型先交替生成文本和代码块，仅在特定执行信号`e_l`处才将累积的未执行代码合并执行，得到观察结果`o_l`，从而保持推理流畅性。

2. **隐式分层控制框架**：设计两层策略体系。高层策略（`π_high`）决定是否执行工具（选择C继续推理或E执行），低层策略（`π_low`）在不执行时进行自回归令牌生成。但显式分层需双重决策，成本高。

3. **IH-GRPO算法**：为避免显式分层的计算开销，提出隐式分层策略。通过理论推导，将工具执行令牌视为词汇表中的普通令牌，并设计替代损失函数`L_I'`，使得隐式策略经单步策略梯度更新后，其行为与显式分层策略等价。该损失函数包含优势函数A、层级修正项等核心组件，确保训练过程中两者分布一致。

4. **整体优化目标**：基于GRPO扩展，加入层级修正项`c_{i,t}`，形成`J_{IH-GRPO}`。其中包含`γ`（执行概率比）、`Z`（非执行令牌归一化项）等关键参数，通过超参数`λ`平衡标准GRPO与分层修正。奖励设计仅采用结果正确性奖励。

创新点在于首次形式化解耦问题，并提出隐式分层策略逼近显式分层的理论方法，实现了更高效的工具使用决策，在多个数学推理基准上取得显著提升。

### Q4: 论文做了哪些实验？

论文在数学推理任务上进行了全面实验。**实验设置**：使用Qwen3系列（1.7B、4B、8B）模型，训练数据来自SimpleRL和Deepscaler的Math3-5，采用“无思考”模式、最多5轮交互、8K最大响应长度。**对比方法**：包括STaR（CoT蒸馏）、SimpleTIR、Dr.GRPO、DAPO（RL方法）以及显式分层方法EH-GRPO，均在耦合（C）和解耦（D）工具调用设置下比较。**评估基准**：在6个域外数学基准（MATH500、AIME24、AIME25、AMC23、Hmmt Feb 25、Olympiad）上使用average@8（小数据集用average@32）评估，温度1.0。**主要结果**：IH-GRPO在Qwen3-1.7B、4B、8B上分别比最强基线绝对提升1.87%、2.16%和2.53%，且在所有模型上解耦设置始终优于耦合设置。消融实验验证了各组件的有效性：代理损失贡献显著，超参数λ在10^{-4}-10^{-2}区间鲁棒（1.7B/4B最优λ=10^{-3}，8B最优λ=10^{-2}）。工具执行令牌和提示敏感性分析表明性能稳定，增加交互轮次（至10轮）和训练数据比例均能持续提升性能。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在实验规模上：仅测试了1.7B-8B参数的小模型和Qwen3单一模型家族，且仅限于数学推理场景。未来可沿三个方向探索：（1）将IH-GRPO扩展到更大规模模型（如70B+）和更多模型家族，验证其隐含层次化策略在更大参数量下的泛化能力和性能增益。（2）拓展到更广泛的任务领域，特别是需要多工具协作的场景，如科学计算、代码生成或复杂问答。当前框架在解耦工具调用与执行后，天然支持工具输出复用和灵活编排，这与Agent系统追求的任务分解与协调高度契合。（3）优化延迟控制的粒度，例如引入自适应执行时机决策机制，根据推理状态动态决定何时释放工具执行，以进一步平衡推理连贯性与计算效率。此外，结合显式思维链（CoT）观察HH-GRPO在“思考模式”下的表现，可能揭示层次化控制与结构化推理的互补关系。

### Q6: 总结一下论文的主要内容

本文提出并形式化了在工具增强推理中解耦工具调用与执行的新问题。现有方法通常将工具调用与立即执行紧密耦合，这会打断LLM的推理连贯性，降低表达能力。为了解决这一问题，论文引入了延迟执行与显式控制机制，并提出了层次化控制框架。通过理论推导，作者得到了一种代理损失函数，使隐式层次化策略能够学习与显式层次化策略等价的行为，进而提出了IH-GRPO算法。在Qwen3-1.7B、Qwen3-4B和Qwen3-8B模型上，该方法在六个跨领域数学推理基准测试中分别实现了1.87%、2.16%和2.53%的绝对提升，并在其他领域也取得了持续的性能增益。核心贡献在于解耦工具的调用与执行，通过层次化策略优化推理过程，显著提升数学推理能力。
