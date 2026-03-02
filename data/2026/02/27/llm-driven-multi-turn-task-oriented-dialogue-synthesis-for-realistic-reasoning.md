---
title: "LLM-Driven Multi-Turn Task-Oriented Dialogue Synthesis for Realistic Reasoning"
authors:
  - "Yu Zhu"
  - "Kai Yang"
date: "2026-02-27"
arxiv_id: "2602.23610"
arxiv_url: "https://arxiv.org/abs/2602.23610"
pdf_url: "https://arxiv.org/pdf/2602.23610v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent 数据合成"
  - "Agent 评测/基准"
  - "任务导向对话"
  - "LLM 推理"
  - "多轮对话"
relevance_score: 7.5
---

# LLM-Driven Multi-Turn Task-Oriented Dialogue Synthesis for Realistic Reasoning

## 原始摘要

The reasoning capability of large language models (LLMs), defined as their ability to analyze, infer, and make decisions based on input information, is essential for building intelligent task-oriented dialogue systems. However, existing benchmarks do not sufficiently reflect the complexity of real-world scenarios, which limits their effectiveness in evaluating and enhancing LLM reasoning in practical contexts. Many current reasoning datasets are overly simplistic and abstract, often disconnected from realistic task flows, domain constraints, and operational rules, making it difficult to effectively evaluate LLMs' logical reasoning ability. In addition, data contamination from pretraining corpora undermines the reliability of evaluation results, and traditional crowdsourcing methods for dataset construction are labor-intensive and difficult to scale. To address these challenges, we propose a LLM-driven framework for synthesizing multi-turn, task-oriented dialogues grounded in realistic reasoning scenarios, leveraging trilevel optimization to enhance dialogue quality. Our method generates dialogues grounded in authentic task scenarios, enriched with real-world information, and exhibiting strong contextual coherence. Corresponding reasoning tasks are carefully designed around these dialogues and iteratively refined to continuously improve the tasks' quality and challenge. The resulting dataset serves as a valuable benchmark for assessing and advancing the realistic logical reasoning capabilities of LLMs. Experimental results show that our synthetic data-based reasoning tasks introduce non-trivial reasoning challenges and provide meaningful support for improving the reasoning capabilities of LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型在现实场景中逻辑推理能力评估和提升所面临的数据瓶颈问题。研究背景在于，尽管大语言模型在许多标准NLP任务上表现出色，但其在需要结合真实世界信息、领域约束和业务规则进行复杂推理的实用场景中，性能仍不尽如人意。现有方法的不足主要体现在三个方面：首先，现有的推理评估数据集通常过于简单、抽象，与现实任务流程脱节，无法充分反映现实场景的复杂性（如长程上下文连贯性和情境敏感约束）；其次，预训练数据与测试集之间的数据污染问题严重影响了评估结果的可靠性；最后，传统依赖众包构建数据集的方法不仅成本高昂、难以扩展，而且难以获取涉及隐私和商业价值的真实数据。此外，现有基于智能体生成对话数据的方法也严重依赖预定义的结构化任务信息，限制了其模拟现实复杂推理的能力。

因此，本文要解决的核心问题是：如何高效、可控地生成高质量、贴近现实、且能有效评估和提升大语言模型现实逻辑推理能力的多轮任务导向对话数据。为此，论文提出了一种由大语言模型驱动的合成框架，通过模拟真实场景中的用户行为来生成扎根于现实任务场景、信息丰富、上下文连贯的多轮对话，并围绕这些对话精心设计相应的推理任务。同时，论文引入了一个三层优化框架，联合优化评估指标、多轮对话提示和单轮对话提示，以实现对话质量的自动评估与迭代提升，从而构建一个能可靠衡量并推动大语言模型现实推理能力发展的基准数据集。

### Q2: 有哪些相关研究？

本文的相关工作主要涉及三个类别：方法类、应用类和数据构建类。

在**方法类**中，相关工作包括基于大语言模型（LLM）的智能体与多智能体系统。现有研究利用LLM作为智能体的核心控制器，使其具备环境感知与行动能力，并通过多智能体分工协作来模拟复杂场景、解决问题。本文在此基础上，通过为智能体分配特定角色和任务，利用其分工协作来增强对现实世界场景的模拟，从而提升生成数据的质量。此外，本文还引入了**三层优化**框架。该框架在机器学习中常用于处理多层级目标与约束相互依赖的复杂学习问题，已有研究在梯度可用时将其应用于神经架构搜索、超参数优化等领域。本文的创新在于，首次将**零阶三层优化**框架引入对话生成任务，并针对对话质量评估的损失函数结构进行了专门定制，以在梯度信息不可用时优化生成过程。

在**应用类**中，相关工作聚焦于**任务型对话系统**。随着预训练语言模型的进步，各种能够进行多轮对话的系统被提出。与传统静态文本理解任务相比，多轮对话更具交互性、动态性和语境依赖性，其推理任务也更为复杂。本文的研究目标与之紧密相关，专注于生成多轮任务型对话，并将必要的推理信息嵌入对话结构，以增强对话的复杂性和实用价值。

在**数据构建类**中，传统方法主要依赖**众包**收集和构建对话数据集，但这种方法成本高、可扩展性有限。为此，**合成数据生成**方法得到发展，常见做法包括增强现有数据集或基于特定任务直接生成数据，并利用外部知识构建多轮对话。本文针对现有基准测试不足以反映现实世界复杂性的问题，提出了一种LLM驱动的合成框架，旨在生成基于真实任务场景、富含现实信息且上下文连贯的多轮对话，并围绕这些对话设计相应的推理任务，以构建更有效的评估基准。这与传统众包和现有合成方法在数据生成的自动化程度、对现实复杂性的关注以及面向推理评估的针对性上有所区别。

### Q3: 论文如何解决这个问题？

论文通过一个由大语言模型驱动的多轮任务导向对话合成框架来解决现有评测基准在真实场景中过于简化、脱离实际任务流程和领域约束，以及数据污染和人工构建成本高昂的问题。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块**：
框架的核心是一个基于LLM的智能体交互系统，包含用户智能体（User Agent）和助手智能体（Assistant Agent），在一个给定的真实场景（如特定领域任务）中进行多轮对话。流程分为三个阶段：
1.  **候选用户生成**：首先，一个专门的“用户生成器”LLM根据场景描述，生成具有不同角色、意图和待解决问题的候选用户池。这确保了后续对话的多样性和角色真实性。
2.  **用户行动序列生成**：从候选池中选取一个用户，用户智能体基于其角色、意图、外部工具（如搜索引擎）获取的现实世界信息以及不断更新的记忆状态，迭代生成一系列模拟真实用户行为的行动序列。这一步骤为对话注入了基于现实观察和逻辑推理的隐含信息。
3.  **多轮对话生成与优化**：用户智能体基于其完整的行动序列和记忆，与助手智能体进行多轮问答式对话。用户提出问题，助手则需结合外部信息和对话历史进行推理来回应。对话生成后，通过一个**三层优化框架**进行自动评估与迭代优化。

**关键技术：三层优化框架**：
这是方法的核心创新点，旨在自动、端到端地提升合成对话的质量，克服传统评估指标依赖参考文本、难以全面衡量合成对话多维质量的局限。
*   **问题形式化**：将对话质量评估与生成模型的优化建模为一个三层优化问题：
    *   **底层**：优化控制单轮对话生成的提示参数（φ），以最小化单轮对话质量评估指标 `g`。
    *   **中层**：优化控制多轮对话生成的提示参数（θ），以最小化多轮对话质量评估指标 `f`，该指标依赖于底层优化后的φ。
    *   **顶层**：优化定义评估指标本身的参数（ω），目标是最大化由专家LLM实现的最终对话质量评分函数 `h` 的值。
*   **优化技术**：
    *   对于提示参数（θ, φ），由于使用的是黑盒LLM（无法获取梯度），采用**两点零阶估计**来近似梯度并进行优化。
    *   对于指标定义参数（ω），由于评估指标是离散结构（如由多个基础指标通过运算符组合成的计算图），采用**进化算法**进行优化。算法通过选择、复制、突变（如插入、删除、替换运算符节点）等操作，在离散空间中自动搜索能产生最高质量对话的评估指标组合。

**创新点总结**：
1.  **场景驱动的对话合成**：通过引入真实场景、外部信息工具和用户行动序列生成，确保了对话根植于现实任务流，并自然嵌入了需要逻辑推理才能揭示的隐含信息。
2.  **基于智能体的交互仿真**：利用用户和助手智能体的角色扮演与记忆机制，生成了上下文连贯、意图一致的多轮任务导向对话。
3.  **三层优化框架**：创新性地将对话生成、评估与指标自动搜索统一在一个优化框架内，实现了合成对话质量的自动、迭代提升，减少了对人工评估和固定指标的依赖。
4.  **进化指标搜索**：通过进化算法自动发现有效的、复合的对话质量评估指标，以适应合成数据的特点，这是提升数据生成质量的关键驱动力。

### Q4: 论文做了哪些实验？

论文在合成的RealReasoning数据集上进行了实验，以评估大语言模型进行现实逻辑推理的能力。实验设置方面，研究使用多种LLM（主要来自qwen系列和deepseek系列）在零样本提示下执行推理任务。模型被给予包含对话上下文的任务，并被要求仅输出最终答案。生成的回答会与真实标注进行比较以评估性能。作为对比，实验还使用了两个公开数据集GSM8K和CODAH。

对比方法主要涉及不同模型及其推理模式的比较：包括直接回答的模型（如qwen-plus, qwen-turbo）与启用深度思考机制的模型（如qwen-plus-thinking, qwen-turbo-thinking，通过设置`enable_thinking`为`True`实现），以及具备内在推理过程的模型（如DeepSeek-R1）。

主要结果和关键数据指标如下：
1.  **整体表现**：即使如qwen-plus这样的先进模型，在现实逻辑推理任务上也表现不佳，整体准确率仅约48.4%。具备深度推理机制的模型（如DeepSeek-R1）在需要复杂推理的任务上表现更好。
2.  **推理与否的影响**：不启用推理直接回答的模型性能欠佳。启用思考后，qwen-turbo-thinking相比qwen-turbo性能提升明显，证明了深入推理过程的有效性。
3.  **任务类型差异**：常识推理任务比数学词问题推理任务难度大得多。表现最佳的模型deepseek-r1在常识推理任务上的准确率为85.3%，而在数学词问题推理上，由于所有必要信息已外部提供，即使小参数模型（如deepseek-r1-distill-qwen-1.5b）也能有效提取信息并给出正确答案。
4.  **模型行为**：较弱的模型在面对封闭式推理问题时，倾向于机械地选择第一个可用选项，反映出其缺乏对问题背景的深度理解和分析能力。

实验总结表明，与现有相对容易的公共推理数据集任务相比，模型在解决现实场景的逻辑推理任务时仍面临困难，这凸显了本文提出的数据生成方法对于评估模型推理能力的价值。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在数据生成和标注过程对人工的依赖，以及生成质量受限于所用大语言模型的性能。未来研究可以从以下几个方向深入探索：

首先，在技术框架层面，可以探索更复杂的多智能体交互机制，引入动态角色分配、长期记忆模块和对抗性训练，以模拟更真实的协商、辩论或协作场景，从而生成更具挑战性的推理任务。其次，在自动化与可扩展性方面，需重点研究高质量自动标注方法，例如利用强化学习或自监督学习，让模型在生成过程中同步进行难度评估和标签迭代优化，以降低人力成本并实现数据集的快速扩展。此外，可考虑构建跨领域、跨文化的任务场景库，以检验推理能力的泛化性。最后，评估体系本身也需完善，未来可设计更细粒度的推理能力评估维度（如因果推断、反事实推理），并探索合成数据与真实用户对话数据的有效融合策略，以进一步提升基准测试的生态效度和实用价值。

### Q6: 总结一下论文的主要内容

该论文针对现有任务型对话基准在评估大语言模型现实推理能力方面的不足，提出了一种由大语言模型驱动的多轮任务型对话合成框架。核心问题是现有评测数据集过于简化抽象，脱离真实任务流程与约束，且存在数据污染和人工构建成本高的问题。方法上，论文利用大语言模型的生成与角色扮演能力，通过三层优化技术，在真实任务场景中合成具有强上下文连贯性的多轮对话，并围绕对话精心设计与迭代优化相应的推理任务，从而构建高质量评测数据集。主要结论表明，该方法生成的合成数据引入了非平凡的推理挑战，能有效评估并提升大语言模型在现实场景中的逻辑推理能力，实验也证实当前模型在此类复杂任务上仍面临显著困难。其核心贡献在于提供了一个可扩展的、贴近现实的对话与推理任务合成框架及对应基准，对推动面向实际应用的对话系统推理研究具有重要意义。
