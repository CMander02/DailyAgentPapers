---
title: "In-Context Reinforcement Learning for Tool Use in Large Language Models"
authors:
  - "Yaoqi Ye"
  - "Yiran Zhao"
  - "Keyu Duan"
  - "Zeyu Zheng"
  - "Kenji Kawaguchi"
  - "Cihang Xie"
  - "Michael Qizhe Shieh"
date: "2026-03-09"
arxiv_id: "2603.08068"
arxiv_url: "https://arxiv.org/abs/2603.08068"
pdf_url: "https://arxiv.org/pdf/2603.08068v1"
categories:
  - "cs.AI"
tags:
  - "Tool Use"
  - "Reinforcement Learning"
  - "In-Context Learning"
  - "Agent Training"
  - "Reasoning"
  - "Data Efficiency"
relevance_score: 9.0
---

# In-Context Reinforcement Learning for Tool Use in Large Language Models

## 原始摘要

While large language models (LLMs) exhibit strong reasoning abilities, their performance on complex tasks is often constrained by the limitations of their internal knowledge. A compelling approach to overcome this challenge is to augment these models with external tools -- such as Python interpreters for mathematical computations or search engines for retrieving factual information. However, enabling models to use these tools effectively remains a significant challenge. Existing methods typically rely on cold-start pipelines that begin with supervised fine-tuning (SFT), followed by reinforcement learning (RL). These approaches often require substantial amounts of labeled data for SFT, which is expensive to annotate or synthesize. In this work, we propose In-Context Reinforcement Learning (ICRL), an RL-only framework that eliminates the need for SFT by leveraging few-shot prompting during the rollout stage of RL. Specifically, ICRL introduces in-context examples within the rollout prompts to teach the model how to invoke external tools. Furthermore, as training progresses, the number of in-context examples is gradually reduced, eventually reaching a zero-shot setting where the model learns to call tools independently. We conduct extensive experiments across a range of reasoning and tool-use benchmarks. Results show that ICRL achieves state-of-the-art performance, demonstrating its effectiveness as a scalable, data-efficient alternative to traditional SFT-based pipelines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在复杂任务中有效利用外部工具（如Python解释器、搜索引擎）的难题。研究背景是，尽管LLM展现出强大的推理能力，但其内部知识的固有限制（如无法获取最新或特定领域信息）制约了其在复杂任务上的表现。通过集成外部工具来增强模型能力已成为一个重要方向，但如何高效训练模型以掌握工具使用技能仍面临挑战。

现有主流方法通常采用“冷启动”流程：先进行监督微调（SFT），再结合强化学习（RL）。这种方法的不足在于，SFT阶段严重依赖大量高质量标注数据（例如人工标注的工具调用轨迹），这些数据获取成本高昂，无论是人工标注还是合成生成都代价不菲。此外，直接从零开始进行RL训练往往效果不佳，因为模型缺乏初始的工具使用能力，导致探索效率低下。

本文要解决的核心问题是：如何摆脱对昂贵监督数据（SFT阶段）的依赖，设计一个更轻量、数据高效的训练框架，使LLM能够学会自主、有效地使用外部工具。为此，论文提出了“上下文强化学习”（ICRL），这是一个纯RL框架，它通过在RL训练过程中的“rollout”阶段引入少量上下文示例（few-shot prompts）来指导模型学习工具调用，从而完全省去了SFT阶段。随着训练进行，这些示例被逐步减少直至为零，使模型最终能在零样本设置下独立使用工具。该方法的核心创新在于将示例提示的引导作用与RL的适应性学习相结合，形成一种渐进式课程学习，旨在实现从模仿到自主工具使用的平稳过渡。

### Q2: 有哪些相关研究？

本文提出的In-Context Reinforcement Learning (ICRL) 主要针对大语言模型（LLM）的工具使用问题，其相关研究可按方法类别进行梳理。

**1. 基于监督微调（SFT）与强化学习（RL）的混合方法**：这是当前训练LLM使用工具的主流范式，通常采用“冷启动”流程，即先进行SFT，再使用RL进行优化。例如，O²-Searcher等工作就依赖此流程。这类方法需要大量高质量的标注数据（如工具调用轨迹）进行SFT，成本高昂。**本文的ICRL与这类工作的核心区别在于，它完全摒弃了SFT阶段**，是一个纯RL的框架，从而显著降低了对监督数据的需求。

**2. 基于提示（Prompting）的方法**：这类方法通过在推理时提供少量示例（few-shot prompting）来引导模型使用工具，例如ZeroSearch等基线模型。它们无需训练，但性能受限于提示工程且缺乏适应性。**本文与这类工作的关系在于，ICRL创新地将这种“上下文示例”机制整合到了RL的训练（rollout）阶段**，作为软监督来引导探索。但ICRL更进一步，通过训练逐步减少并最终移除这些示例，使模型最终学会独立调用工具，实现了从模仿到自主学习的过渡。

**3. 纯强化学习方法**：直接从头开始应用RL训练工具使用，常因探索效率低下而导致性能不佳。**本文ICRL也属于纯RL框架，但通过引入并动态减少上下文示例，有效解决了初始探索困难的问题**，从而在无需SFT的情况下实现了稳定高效的训练。

综上所述，ICRL与现有工作的主要关系是借鉴了提示学习的思想来增强RL，核心区别在于它提供了一种无需昂贵SFT、数据效率更高的端到端训练方案，是对传统SFT+RL混合范式的一种创新替代。

### Q3: 论文如何解决这个问题？

论文提出的核心方法是“情境内强化学习”（ICRL），这是一个纯强化学习框架，旨在解决大语言模型有效使用外部工具的难题，并避免传统方法对大量监督微调数据的依赖。

整体框架将工具增强的推理过程建模为一个马尔可夫决策过程。模型在生成响应时，可以执行内部推理、调用外部工具或给出最终答案，这些动作通过特定的XML标签（如 `<think>`, `<search>`, `<answer>`）在文本中结构化表示。外部工具（如搜索引擎）被建模为一个响应函数，其返回的观察结果会被追加到模型的上下文中。

ICRL的关键创新在于其训练过程。它摒弃了需要大量标注数据的监督微调阶段，转而直接在强化学习的“行动采样”阶段引入情境学习。具体而言，在训练初期，模型的行动采样提示模板中包含少量工具使用的演示示例，这些示例通过情境学习引导模型学习如何调用工具。随着训练的进行，提示中的示例数量被逐步减少，最终过渡到零示例提示，促使模型学会独立调用工具。这个过程通过算法迭代实现，针对不同数量的演示示例，使用对应的数据子集进行多轮强化学习训练。

在技术层面，论文采用了分组相对策略优化方法进行训练。为了适应工具使用的特点，引入了损失掩码策略，确保只有模型自身生成的令牌参与策略梯度计算，而从工具检索到的固定内容则被排除在损失计算之外，从而使优化专注于模型自身的决策行为。奖励函数设计为复合形式，结合了答案准确性和格式正确性。准确性奖励基于预测答案与标准答案的精确匹配，格式奖励则通过惩罚XML标签使用不当（如缺失标签、标签不平衡等）来鼓励模型遵循规定的输出结构。

该方法的主要创新点在于：1) 提出了一个无需监督微调、纯强化学习的工具使用训练框架，显著降低了数据需求；2) 创新性地将情境学习与强化学习探索能力相结合，通过动态减少情境示例来引导模型从依赖示例过渡到自主工具调用；3) 设计了针对工具使用场景的损失掩码和结构化奖励机制，有效提升了训练效率和模型性能。实验结果表明，该方法在多个推理和工具使用基准测试上达到了最先进的性能。

### Q4: 论文做了哪些实验？

论文实验围绕提出的ICRL框架展开，评估其在增强大语言模型工具使用能力方面的效果。实验设置方面，主要使用Qwen2.5系列指令微调模型（如3B、7B、14B参数版本）作为骨干模型，在4张NVIDIA A100 GPU上使用VeRL框架进行训练。训练采用学习率1e-6，批次大小64，并为每个查询采样8条轨迹以计算优势函数。模型通过整合Serper API进行实时谷歌搜索，每次检索返回前三的文档。

数据集与基准测试方面，使用Natural Questions（NQ）作为主要训练数据，并从网络上采样问题由GPT-5.2生成少样本示例。评估则在五个广泛使用的QA基准上进行：TriviaQA、HotpotQA、2Wiki、Musique和Bamboogle，每个数据集随机采样最多500个问题以避免数据泄露，涵盖单跳、多跳和组合推理任务。

对比方法包括三大类：直接提示方法（如Chain-of-Thought）、基于检索的方法（如RAG、IRCoT、Search-o1）以及微调方法（如SFT、RL without search、Rejection Sampling）。还包括近期结合搜索的RL方法，如Search-R1、ZeroSearch、O²-Searcher和ParallelSearch。

主要结果以精确匹配（EM）准确率为指标。ICRL在多个模型规模上均取得最优性能。例如，在Qwen2.5-3B上，ICRL平均EM得分为40.16%，显著超过最佳基线Search-R1（31.10%）8.94个百分点，在多跳数据集上提升尤为明显（如2Wiki提升7.3%）。在Qwen2.5-7B上，ICRL平均得分为49.12%，优于最强基线ParallelSearch（41.78%）7.34个百分点，在五个数据集中四个取得最佳成绩。关键的是，ICRL无需任何监督微调（SFT）或标注数据，在Qwen2.5-3B上仍以40.16%的平均得分超越需要冷启动SFT的O²-Searcher（37.26%），展示了其数据高效性和可扩展性。

### Q5: 有什么可以进一步探索的点？

本文提出的ICRL方法在数据效率和性能上具有优势，但仍存在一些局限性和值得探索的方向。首先，其训练过程依赖于精心设计的课程学习（如3→2→0阶段），但消融实验表明，阶段设计对结果影响显著，过早减少示例会损害多轮推理能力。未来可探索更自适应的课程调度策略，例如根据模型实时表现动态调整示例数量，或引入元学习来优化这一过程。其次，当前方法主要评估了搜索和代码执行工具，对于更复杂的工具链（如多模态工具或需要状态管理的API）的泛化能力尚未验证。未来可扩展至更丰富的工具集，并研究如何让模型自主选择工具序列。此外，奖励设计仅依赖稀疏信号（格式有效性和最终答案准确性），可能无法充分引导复杂推理步骤。可探索更密集的奖励信号，如中间步骤的正确性评估，或结合过程监督。最后，虽然方法在14B模型上有效，但更大模型（如70B以上）的扩展性、计算成本以及与小样本示例的交互机制仍需进一步研究。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为“上下文强化学习”（ICRL）的新框架，旨在解决大语言模型有效使用外部工具（如计算器、搜索引擎）的难题。传统方法通常需要先进行监督微调（SFT），再结合强化学习（RL），但SFT阶段依赖大量标注数据，成本高昂。ICRL的核心贡献在于完全摒弃了SFT，仅通过强化学习训练模型使用工具：它在RL的“rollout”阶段引入少量示例作为上下文提示，直接教导模型如何调用工具，并随着训练逐步减少示例数量，最终使模型在零样本条件下自主学会工具使用。实验表明，ICRL在多项推理和工具使用基准测试中取得了领先性能，验证了其作为一种可扩展、数据高效方法的有效性，为增强语言模型的外部能力提供了新途径。
