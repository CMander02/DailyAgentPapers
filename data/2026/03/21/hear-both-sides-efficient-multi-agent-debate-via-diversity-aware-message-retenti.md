---
title: "Hear Both Sides: Efficient Multi-Agent Debate via Diversity-Aware Message Retention"
authors:
  - "Manh Nguyen"
  - "Anh Nguyen"
  - "Dung Nguyen"
  - "Svetha Venkatesh"
  - "Hung Le"
date: "2026-03-21"
arxiv_id: "2603.20640"
arxiv_url: "https://arxiv.org/abs/2603.20640"
pdf_url: "https://arxiv.org/pdf/2603.20640v1"
categories:
  - "cs.CL"
tags:
  - "Multi-Agent Debate"
  - "Reasoning"
  - "Communication Efficiency"
  - "Message Selection"
  - "Diversity"
  - "Computational Efficiency"
  - "Benchmark Evaluation"
relevance_score: 8.0
---

# Hear Both Sides: Efficient Multi-Agent Debate via Diversity-Aware Message Retention

## 原始摘要

Multi-Agent Debate has emerged as a promising framework for improving the reasoning quality of large language models through iterative inter-agent communication. However, broadcasting all agent messages at every round introduces noise and redundancy that can degrade debate quality and waste computational resources. Current approaches rely on uncertainty estimation to filter low-confidence responses before broadcasting, but this approach is unreliable due to miscalibrated confidence scores and sensitivity to threshold selection. To address this, we propose Diversity-Aware Retention (DAR), a lightweight debate framework that, at each debate round, selects the subset of agent responses that maximally disagree with each other and with the majority vote before broadcasting. Through an explicit index-based retention mechanism, DAR preserves the original messages without modification, ensuring that retained disagreements remain authentic. Experiments on diverse reasoning and question answering benchmarks demonstrate that our selective message propagation consistently improves debate performance, particularly as the number of agents scales, where noise accumulation is most severe. Our results highlight that what agents hear is as important as what agents say in multi-agent reasoning systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体辩论框架中因信息冗余和噪声导致的效率与性能下降问题。研究背景是，基于大语言模型的多智能体系统在复杂问题解决中展现出潜力，其中多智能体辩论通过迭代式相互批评提升了推理质量。然而，现有方法在每一轮辩论中广播所有智能体的消息，这带来了两个主要不足：一是当多个智能体通过相似推理路径得出相同答案时，冗余消息会浪费计算资源；二是低质量或错误的回答会误导其他智能体，导致错误传播。现有解决方案主要依赖基于不确定性的过滤方法，即丢弃置信度低于阈值的信息，但这种方法存在局限：大语言模型的置信度估计往往校准不佳，且性能对阈值选择高度敏感，需要大量调优且泛化能力差。更重要的是，仅基于置信度过滤忽略了辩论中的关键要素——分歧，因为即使置信度较低但提供不同视角的回答，可能比高置信度的重复观点更有助于集体推理。

本文要解决的核心问题是：如何在不引入额外噪声和冗余的前提下，高效地利用多智能体辩论中的分歧信息来提升推理性能。为此，论文提出了多样性感知保留框架，通过选择彼此之间以及与多数投票差异最大的回答子集进行广播，从而保留原始且多样化的观点，减少噪声积累，并降低计算开销。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕多智能体辩论（MAD）以及多智能体LLM系统中的不确定性与多样性展开，可分为方法类与评测类。

在**多智能体辩论（MAD）方法**方面，相关工作旨在通过智能体间的迭代交流提升推理质量。早期研究引入基础MAD框架，后续扩展包括为智能体分配不同角色、引入多样性剪枝与误解反驳机制、设计更有效的通信协议等。近期研究探索利用更丰富的信号（如显式置信度表达）来引导交互、避免过早收敛。并行工作如Tool-Use Mixture（TUMIX）等集成式框架，则强调多样化工具使用策略与跨智能体迭代精炼。然而，现有MAD方法对超参数敏感，且辩论本身带来的提升有时有限。为此，一些研究尝试在轮次间过滤信息，例如主观掩码（使用LLM智能体自评）或客观掩码（丢弃低置信度响应），另一些则通过更激进的采样增加候选多样性，但计算成本较高。**本文提出的DAR框架与这些方法不同**：它不依赖对单个响应的判断或昂贵采样，而是通过一个基于索引的保留机制，选择与多数投票结果分歧最大的响应子集进行广播，从而以轻量、高效的方式保留有信息量的多样性观点。

在**不确定性与多样性研究**方面，不确定性估计常被用作LLM可靠性的代理，已有工作通过词元级概率、言语化置信度或语义熵等方法进行度量，并扩展到多步推理中以捕捉累积误差。在多智能体辩论中，融入置信度信号已被证明能改进聚合、减少过早收敛。另一方面，多样性被普遍认为是提升推理性能的关键因素，如自一致性、提示多样化和多提示集成等方法通过并行提示鼓励多样推理路径。这些研究表明不确定性与多样性存在紧密联系，不确定性有助于识别信息丰富或互补的候选。**本文与这些工作的关系在于**，它同样关注多样性对辩论效果的促进作用，但区别在于不依赖显式的不确定性校准或高成本采样，而是利用智能体间的**分歧**这一隐式信号来轻量级地保留多样性，从而在提升性能的同时保持计算效率。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“多样性感知保留”（DAR）的轻量级辩论框架来解决多智能体辩论中因广播所有消息而产生的噪声和冗余问题。该框架的核心思想是在每一轮辩论中，有选择地保留那些彼此之间以及与多数投票结果存在最大分歧的智能体回应，再进行广播，从而提升辩论质量并节约计算资源。

整体框架遵循标准的多智能体辩论设置，包含N个智能体进行R轮辩论。其创新之处在于，在每一轮辩论开始前，引入了一个基于索引的轻量级过滤模块F。该模块接收上一轮所有智能体的回应以及上一轮的多数投票结果，其任务不是评估回应的正确性或置信度，而是输出一个需要保留的智能体ID子集。这些被保留的回应（其原始内容不做任何修改）将构成下一轮辩论的共享上下文。这种方法确保了保留的分歧是真实、未经篡改的。

关键技术设计主要包括三个方面：首先，**基于分歧的保留准则**。过滤模块F被提示去选择那些观点彼此差异最大、且与多数投票结果差异最大的智能体。这通过一个最大化多样性并控制子集规模的优化目标来近似实现，旨在保留信息丰富的分歧，同时剔除冗余的生成内容。其次，**软性多数信号集成**。在每一轮中，将上一轮的多数投票结果明确地作为共识锚点，与保留的回应一起前置到每个智能体的提示词中。这有助于引导生成过程，既能强化共识验证，又能突出分歧以促进针对性改进。最后，**回退机制与稳定性保障**。当所有智能体答案一致、不存在有意义的分歧时，系统会自动回退到标准的全员广播辩论模式。此外，过滤模块仅输出智能体ID而非修改回应内容，这避免了基于LLM的编辑可能带来的意外扭曲，尤其对于小模型而言，保证了干预的清晰和稳定。

简言之，DAR的创新点在于将辩论优化的焦点从“智能体说什么”转向了“智能体听到什么”，通过一个无需训练、与现有管道兼容的轻量级选择机制，在保留关键分歧信息的同时有效抑制了噪声积累，从而在智能体数量增加时能持续提升辩论性能。

### Q4: 论文做了哪些实验？

论文实验设置方面，主要评估了去中心化和稀疏两种多智能体辩论（MAD）拓扑结构，默认使用4个智能体（N=4），并探索了2和8个智能体的情况。辩论轮数设为2轮（R=2），结果取两轮中的最佳值，所有实验均运行三次取平均。

使用的模型包括五个不同家族和尺寸的指令微调开源模型：Qwen2.5-1.5B、Qwen2.5-3B、Falcon3-7B和Llama3.1-8B。评估基准涵盖五大类：算术推理、数学推理（GSM8K）、对齐标注（HH-RLHF）、事实问答（MMLU专业医学和形式逻辑）以及常识推理（CSQA）。

对比方法包括：（1）Society Of Mind（基础MAD），（2）MAD-M²（基于困惑度过滤前50%最自信的生成），（3）Uncertain Prompt（将不确定性分数融入提示），（4）Majority Vote（无辩论的多数投票），（5）Vote Prompt（通过提示进行“软”多数投票），以及（6）本文提出的多样性感知保留（DAR）方法。

主要结果显示，DAR方法在多个模型和数据集上取得了最佳或接近最佳的平均性能。例如，在去中心化MAD设置下，Qwen2.5-1.5B模型上DAR平均准确率达55.87%，优于其他方法；在Qwen2.5-3B上，DAR平均准确率为64.02%，显著高于多数投票的61.37%。关键指标上，随着智能体数量增加至4个和8个，DAR的优势更加明显，表明其能有效利用额外智能体并控制信息噪声。消融实验进一步验证了DAR各组件（如不确定性提示、投票提示和LLM作为评判者）的有效性。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于DAR框架主要关注消息的选择性传播，但未深入探讨不同任务类型下“多样性”的量化标准如何自适应调整，也未考虑代理异构性（如不同模型或提示）对辩论动态的影响。未来研究可探索动态多样性阈值机制，使保留的消息数量能根据辩论轮次和问题复杂度自动优化。此外，可将DAR与不确定性估计方法结合，形成混合筛选策略，以更稳健地处理边缘情况。另一个方向是研究辩论过程中的长期记忆机制，让代理能参考历史分歧点，从而提升深度推理能力。最后，将DAR扩展至多轮开放式对话场景，评估其在创造性任务中的效果，也是一个值得探索的切入点。

### Q6: 总结一下论文的主要内容

本文提出了一种名为多样性感知保留（DAR）的高效多智能体辩论框架，旨在解决现有多智能体辩论中因广播所有消息而导致的噪声和冗余问题。该方法的核心贡献在于，它不依赖不可靠的置信度估计，而是在每一轮辩论中，通过一个基于索引的保留机制，选择那些彼此之间以及与多数投票结果分歧最大的智能体响应子集进行传播，从而保留原始且真实的分歧信息。实验表明，DAR框架能有效提升在多种推理和问答基准上的性能，尤其在智能体数量增加、噪声累积最严重时效果更为显著。该研究强调了在多智能体推理系统中，控制信息流与智能体发言本身同等重要，为构建可扩展的高效协作系统提供了新思路。
