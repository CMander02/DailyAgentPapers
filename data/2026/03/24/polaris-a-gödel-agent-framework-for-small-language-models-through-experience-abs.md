---
title: "Polaris: A Gödel Agent Framework for Small Language Models through Experience-Abstracted Policy Repair"
authors:
  - "Aditya Kakade"
  - "Vivek Srivastava"
  - "Shirish Karande"
date: "2026-03-24"
arxiv_id: "2603.23129"
arxiv_url: "https://arxiv.org/abs/2603.23129"
pdf_url: "https://arxiv.org/pdf/2603.23129v1"
categories:
  - "cs.LG"
tags:
  - "Agent Architecture"
  - "Self-Improvement"
  - "Policy Repair"
  - "Experience Abstraction"
  - "Reasoning"
  - "Small Language Models"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# Polaris: A Gödel Agent Framework for Small Language Models through Experience-Abstracted Policy Repair

## 原始摘要

Gödel agent realize recursive self-improvement: an agent inspects its own policy and traces and then modifies that policy in a tested loop. We introduce Polaris, a Gödel agent for compact models that performs policy repair via experience abstraction, turning failures into policy updates through a structured cycle of analysis, strategy formation, abstraction, and minimal code pat ch repair with conservative checks. Unlike response level self correction or parameter tuning, Polaris makes policy level changes with small, auditable patches that persist in the policy and are reused on unseen instances within each benchmark. As part of the loop, the agent engages in meta reasoning: it explains its errors, proposes concrete revisions to its own policy, and then updates the policy. To enable cumulative policy refinement, we introduce experience abstraction, which distills failures into compact, reusable strategies that transfer to unseen instances. On MGSM, DROP, GPQA, and LitBench (covering arithmetic reasoning, compositional inference, graduate-level problem solving, and creative writing evaluation), a 7-billion-parameter model equipped with Polaris achieves consistent gains over the base policy and competitive baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何让参数规模较小的语言模型（SLMs）也能实现高效、可追溯的递归自我改进（recursive self-improvement）这一核心问题。研究背景是当前大型语言模型（LLMs）的自我改进方法，如基于响应的自我修正（如Reflexion、Self-Refine）或参数微调，虽然有效，但存在改进难以定位、更新是否具有持久性和可复用性不明确的问题。Gödel Agent框架通过将智能体的策略视为可检查和修改的显式对象，为实现持久性改进提供了理论方向，但其直接实例化通常计算开销巨大，需要大量上下文和历史记录来支持反思，导致在资源受限的小模型上运行时容易出现内存不足和工具调用错误，难以实际应用。

现有方法的不足主要体现在两个方面：一是大多数改进方法发生在响应层面或参数层面，缺乏对策略（policy）本身进行显式、可审计的修改；二是现有的Gödel Agent实现对于计算资源和上下文长度要求高，不适合参数规模较小的模型（如70亿参数），限制了递归自我改进技术的普及和应用。

因此，本文的核心问题是：**如何在计算资源受限的小型语言模型上，实现一种可行、高效且能产生持久性策略更新的递归自我改进框架？** 为此，论文提出了Polaris框架，其解决方案的核心是“经验抽象化的策略修复”（experience-abstracted policy repair）。该方法不是保留大量失败样本和完整历史，而是将失败案例抽象、提炼成紧凑、可复用的策略指令，并生成最小化的代码补丁来更新策略。这种方法控制了上下文增长，降低了计算开销，同时通过小规模、可审计的代码补丁使策略更新具有持久性和可解释性，并能迁移到未见过的任务实例上，从而使得小型模型也能进行持续的策略级自我完善。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在方法类研究中，相关工作主要包括两类。一类是**响应层面的自我修正**，例如通过批判和精炼来优化单个回答的方法，如ReAct、Reflexion、Self-Refine、CRITIC和Self Debugging等。另一类是**参数层面的更新**，例如通过任务算术、针对性知识编辑等方法直接修改模型参数。本文提出的Polaris框架与这些方法的核心区别在于，它进行的是**策略层面的持久性更新**。Polaris将智能体的策略视为一个可检查、可修改的显式对象，通过生成小型、可审计的代码补丁来修复策略，这些更新是持久且可复用于新任务的，而非针对单次响应的临时调整或不可追溯的参数改动。

在应用类研究中，本文直接建立在**Gödel Agent**框架之上，该框架形式化了递归自我改进的思想，即智能体检查自身的策略和执行轨迹，并在测试循环中更新策略。然而，Polaris针对**小型语言模型**在资源受限环境下的挑战进行了关键改进。原始的Gödel Agent框架在应用于7B参数模型时，常因上下文增长导致内存和计算开销过大而失败。Polaris通过引入**经验抽象**机制，将失败案例提炼为紧凑、可复用的策略，并生成最小化代码补丁，从而有效控制了上下文增长，使得递归自我改进在SLMs上变得可行。

在评测类研究方面，本文在多个标准基准上进行了评估，包括MGSM（数学推理）、DROP（组合推理）、GPQA（研究生级问题解决）和LitBench（创意写作评估）。这些基准涵盖了算术推理、组合推理、高阶问题解决和创造性写作评估等多个维度，用于验证Polaris带来的性能增益是广泛且一致的。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Polaris的Gödel智能体框架来解决小型语言模型（SLM）的策略自我改进问题，其核心是**基于经验抽象的策略修复循环**。该方法使智能体能够分析自身失败经验，抽象出通用修复策略，并以最小化、可审计的代码补丁形式持久化更新其任务执行策略。

**整体框架与主要模块**：Polaris实现了一个递归自我改进的闭环，包含四个核心操作符，对应算法中的关键函数：
1.  **失败分析（AnalyzeFailure）**：智能体在验证集上执行当前策略π_t，收集失败实例τ_i。对于每个失败，通过自我反思生成结构化记录A_i，包含错误诊断、修订计划和预防规则。这构成了可解释的经验库。
2.  **策略合成（StrategySynthesis）**：该模块对一批失败反思A={A_i}进行抽象，提炼出紧凑、可重用的修复指令集δ={δ_j}（如“问题分解”、“规范化处理”）。这实现了从具体失败到通用策略的升华，是**经验抽象**的关键创新，确保改进能迁移到未见过的同类问题。
3.  **补丁生成（PatchGeneration）**：针对每个抽象策略δ_j，生成一个最小化的代码补丁p_j。补丁仅修改必要代码行，强调局部性和最小变更，以保持可解释性和可验证性。生成后会进行轻量级的语法和格式验证。
4.  **补丁集成（IntegratePatch）**：将验证通过的补丁集P应用到当前策略π_t上，产生更新后的策略π_{t+1}。集成过程包含语法和执行检查（而非直接性能评估），失败会进行有限重试（默认3次）。所有过程产物（反思、策略、补丁、集成结果）都存入记忆（Memory），确保连续性和避免冗余。

**架构设计与关键技术**：
*   **递归自我改进架构**：框架遵循“内省（Introspect）-执行（Interact）-自我改进（Self-Improve）-递归继续（Continue-Improve）”的循环。智能体不仅能修改任务策略π，还能修订决定如何生成和应用修改的元级改进逻辑I，实现了策略与改进逻辑的协同进化。
*   **运行时代码突变**：这是Gödel智能体的一个核心技术革新。它允许智能体在运行期间动态修改其可执行组件（策略代码），支持对修改进行测试、验证和回滚，而无需完全重新训练，实现了稳定的迭代改进。
*   **记忆（Memory）的持续追踪**：所有分析、策略、补丁和集成结果都存储在Memory中，提供了完整的可追溯性。这不仅是经验库，也用于防止策略合成阶段提出重复的改进方案，支持累积性的策略精炼。

**创新点**：
1.  **策略级、持久化的改进**：不同于仅在响应层面进行自我校正或进行参数调优，Polaris直接在策略代码层面进行微小、可审计的修改。这些补丁持久化在策略中，并可在同一基准内的未见实例上复用。
2.  **经验抽象机制**：这是实现累积性策略改进的核心。它将具体的失败案例提炼为紧凑、可重用的抽象策略，使改进能够泛化，超越了针对单个错误的修补。
3.  **面向小型语言模型的设计**：专门为参数规模较小的模型（如论文中使用的70亿参数模型）设计，通过结构化的、基于代码补丁的更新循环，在算术推理、组合推理、研究生级问题解决和创意写作评估等多个基准上实现了超越基础策略和竞争基线的持续性能提升。

### Q4: 论文做了哪些实验？

实验在四个基准测试上进行：MGSM（算术推理）、DROP（组合推理）、GPQA（研究生水平问题解决）和LitBench（创意写作评估）。实验设置使用Qwen2.5-7B-Instruct模型，在两块32GB NVIDIA V100 GPU上运行。每个实验允许自主演化10小时，而非固定步数，以观察策略修复迭代次数的自然变化。验证集样本量分别为：MGSM和DROP使用50个验证样本和250个测试样本，GPQA使用20个验证样本和100个测试样本，LitBench使用20个验证样本和250个测试样本。关键超参数N（用于反思的失败任务样本数）测试了N=3和N=5以权衡反思深度与稳定性。

对比方法包括：1) 思维链自洽性（COT-SC），每个查询采样五条推理路径并选择最频繁答案；2) 原始Gödel Agent框架的直接复现，但该基线在资源限制下因内存溢出（OOM）和工具调用错误而失败。

主要结果：配备Polaris的70亿参数模型在所有基准上均实现了相对于基础策略和竞争基线的持续性能提升。具体指标方面，在MGSM和GPQA上报告准确率及95%自助法置信区间，在DROP上报告宏观F1分数（因其为跨度选择格式），在LitBench上基于首选响应选择报告准确率。实验进行了十次独立运行，并分类为成功（策略更新提升测试性能）、无改进（策略更新成功但未提升性能）和不成功（因OOM、无限循环或幻觉工具调用而失败）。经验抽象机制通过减少用于元推理的验证样本数（N）和内存中的消息数（从十条减至六条），有效解决了原始Gödel Agent因上下文长度增长导致的计算开销问题。

### Q5: 有什么可以进一步探索的点？

基于论文分析，Polaris框架的局限性及未来可探索方向如下：首先，小语言模型（SLMs）的元推理和工具调用能力不足是核心瓶颈，导致其难以准确诊断失败原因并生成有效的策略修复，未来需研究如何通过更精细的提示工程、外部知识注入或混合模型架构来增强SLMs的元认知能力。其次，经验抽象过程在多样化任务中表现不稳定，抽象出的策略通用性有限，可探索分层抽象机制，将失败案例分解为不同粒度（如任务特定、领域通用）的策略模块，提升迁移效率。此外，上下文累积导致的内存溢出（OOM）问题制约了迭代规模，需设计更高效的经验压缩与缓存策略，或引入动态上下文窗口管理。从系统层面看，当前修复循环缺乏对“修复质量”的自动化评估机制，可能引入噪声，未来可集成强化学习或基于效用的筛选器，确保策略更新的单调改进。最后，框架在复杂推理任务（如DROP）上表现较弱，需结合符号推理或外部工具链来弥补SLMs的结构化处理缺陷，实现更鲁棒的自进化。

### Q6: 总结一下论文的主要内容

该论文提出了Polaris框架，旨在为小型语言模型实现Gödel智能体的递归自我改进能力。核心问题是让智能体能够通过分析自身执行轨迹中的失败经验，直接对策略代码进行持久化修复，而非仅进行响应层面的即时修正或参数微调。方法上，Polaris构建了一个结构化循环：智能体首先分析错误并解释原因，然后制定具体修订方案，接着通过“经验抽象”将失败案例提炼为紧凑、可重用的策略，最后以最小化、可审计的代码补丁形式对策略进行更新，并辅以保守性检查。主要结论显示，在MGSM、DROP、GPQA和LitBench等多个涵盖数学推理、组合推理、研究生级问题解决和创意写作评估的基准测试中，一个70亿参数的模型装备Polaris后，其性能持续超越基础策略并达到与竞争基线相当的水平。该工作的核心贡献在于实现了策略层面的、可累积的自我改进机制，为小型模型赋予了通过经验抽象进行持续性策略修复和泛化的能力。
