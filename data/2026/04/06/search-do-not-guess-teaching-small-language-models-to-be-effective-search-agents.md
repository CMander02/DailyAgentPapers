---
title: "Search, Do not Guess: Teaching Small Language Models to Be Effective Search Agents"
authors:
  - "Yizhou Liu"
  - "Qi Sun"
  - "Yulin Chen"
  - "Siyue Zhang"
  - "Chen Zhao"
date: "2026-04-06"
arxiv_id: "2604.04651"
arxiv_url: "https://arxiv.org/abs/2604.04651"
pdf_url: "https://arxiv.org/pdf/2604.04651v1"
categories:
  - "cs.AI"
tags:
  - "Search Agent"
  - "Small Language Model"
  - "Tool Use"
  - "Fine-tuning"
  - "Knowledge-Intensive Tasks"
  - "Multi-hop Reasoning"
  - "Agent Distillation"
relevance_score: 8.0
---

# Search, Do not Guess: Teaching Small Language Models to Be Effective Search Agents

## 原始摘要

Agents equipped with search tools have emerged as effective solutions for knowledge-intensive tasks. While Large Language Models (LLMs) exhibit strong reasoning capabilities, their high computational cost limits practical deployment for search agents. Consequently, recent work has focused on distilling agentic behaviors from LLMs into Small Language Models (SLMs). Through comprehensive evaluation on complex multi-hop reasoning tasks, we find that despite possessing less parametric knowledge, SLMs invoke search tools less frequently and are more prone to hallucinations. To address this issue, we propose \policy, a lightweight fine-tuning approach that explicitly trains SLMs to reliably retrieve and generate answers grounded in retrieved evidence. Compared to agent distillation from LLMs, our approach improves performance by 17.3 scores on Bamboogle and 15.3 scores on HotpotQA, achieving LLM-level results across benchmarks. Our further analysis reveals that adaptive search strategies in SLMs often degrade performance, highlighting the necessity of consistent search behavior for reliable reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何将基于搜索的智能体能力有效蒸馏到小型语言模型（SLMs）中的问题。研究背景是，当前基于大语言模型（LLMs）的搜索智能体（如Search-o1）在知识密集型任务上表现出色，但其庞大的计算成本和延迟限制了在实际部署中的应用，尤其是在有严格延迟或预算约束的场景中。相比之下，参数规模较小（通常小于40亿）的SLMs效率更高，更适合部署，但现有方法直接让SLMs作为搜索智能体时存在明显不足。

现有方法的不足主要体现在两方面：首先，SLMs本身参数知识有限，在复杂的多跳推理任务中，它们倾向于过度依赖自身有限的内参知识进行推测，导致“参数幻觉”问题，即频繁产生事实错误的答案。其次，简单地通过蒸馏从LLMs中学习智能体行为轨迹效果有限，因为LLMs生成的轨迹往往隐含依赖其自身丰富的参数知识，而这些知识是SLMs所不具备的，因此这种蒸馏带来的性能提升非常微小。

因此，本文要解决的核心问题是：如何克服SLMs的“参数幻觉”并有效提升其作为搜索智能体的性能。具体而言，论文提出了一种名为ASP的轻量级微调方法，该方法明确训练SLMs在执行任务时始终优先进行外部搜索检索，并基于检索到的证据生成答案，从而强制模型进行证据驱动的推理，避免对自身参数知识的过度依赖。通过这种方法，论文旨在使SLMs在保持高效的同时，达到接近LLM水平的可靠搜索与推理能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**基于大语言模型（LLM）的搜索智能体**和**面向高效智能体的知识蒸馏方法**。

在**基于LLM的搜索智能体**方面，现有研究通过为语言模型配备外部搜索工具，显著增强了其处理知识密集型任务的能力。这些模型在推理循环中与检索工具交互，以回答复杂的多跳问题。然而，这类工作大多依赖LLM，其高昂的计算成本和延迟限制了实际部署。

在**面向高效智能体的知识蒸馏**方面，为了克服LLM的瓶颈，研究者尝试通过知识蒸馏将能力从教师模型迁移到学生模型。具体而言，思维链（CoT）蒸馏提升了小语言模型（SLM）的推理技能，近期工作也开始探索蒸馏工具使用能力。这些方法虽有效，但往往保留了教师模型的固有特性。

**本文与这些工作的关系和区别在于**：本文同样关注将搜索智能体能力迁移到SLM这一目标，但发现现有蒸馏方法得到的SLM调用搜索工具频率较低、更容易产生幻觉。为此，本文提出了名为 \policy 的轻量级微调方法，其核心区别在于**在蒸馏过程中明确训练SLM执行可靠的检索并基于检索证据生成答案**，从而强制其采取一致的搜索行为，而非自适应（且易退化）的策略。这使得本文方法在性能上显著超越了传统的智能体蒸馏方法。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“始终搜索策略”（Always-Search Policy, ASP）的轻量级微调方法来解决小语言模型（SLMs）在作为搜索智能体时搜索工具调用不足、容易产生幻觉的问题。该方法的核心思想是强制SLMs在回答知识密集型问题时，必须依赖外部搜索工具获取证据，而非依赖自身有限的参数化知识进行猜测。

整体框架基于标准的监督微调（SFT）和策略蒸馏（如On-Policy Distillation, OPD），但关键创新在于将ASP原则深度整合到训练过程中。主要模块和关键技术包括：1）**轨迹过滤**：在SFT阶段，通过设置String-F1阈值（0.65）、搜索工具检查（确保模型使用了搜索工具）和关键词过滤（剔除包含“我记得”等依赖内部知识生成的轨迹），严格筛选训练数据，只保留那些模型持续使用搜索工具获取信息的轨迹。2）**系统提示引导**：在OPD阶段，通过插入系统提示明确要求模型始终使用搜索工具，并利用教师模型（大语言模型）的概率分布来规范和鼓励SLMs的搜索行为。3）**混合训练策略**：采用“混合”设置，先在SFT中融入ASP，再进行OPD，以进一步强化始终搜索的行为。4）**下游增强**：最后应用拒绝微调（RFT）作为最终阶段，通过选择性强化高质量的智能体行为来进一步挖掘已蒸馏模型的潜力。

该方法的创新点在于，它明确训练SLMs形成一种可靠且一致的搜索策略，而非自适应地（且常常是退化地）决定是否搜索。实验表明，ASP显著提高了SLMs的搜索频率（例如从每问题1.72次提升至2.84次），从而减少了幻觉，并在多个复杂的多跳推理和信息寻求基准测试上（如HotpotQA、Bamboogle）实现了性能的大幅提升（分别提升17.3和15.3分），达到了与大语言模型相当的水平。此外，ASP还增强了模型对噪声检索的鲁棒性，在部分检索失败时性能下降更小，显示出更强的恢复能力。

### Q4: 论文做了哪些实验？

论文实验主要分为三个部分。首先，评估了原始（Vanilla）和通过标准智能体蒸馏（Distilled）得到的小语言模型（SLMs）的搜索代理性能。实验在HotpotQA等复杂多跳推理任务上进行，使用Qwen3系列模型（0.6B至32B参数）作为基准。结果表明，与更大模型（≥8B）相比，SLMs性能显著更差，调用搜索工具的频率也更低（例如，蒸馏后的Qwen3-1.7B在HotpotQA上每个问题平均调用1.89次，而教师模型Qwen3-32B为3.02次），且更容易产生幻觉。关键指标显示，蒸馏后的1.7B模型在HotpotQA开发集上的准确率为47.9%，远低于教师模型的60.3%。

其次，论文提出了“始终搜索”策略（Always-Search Policy, ASP），并设计了相应的微调方法，包括融入ASP的监督微调（SFT）、在线策略蒸馏（OPD）以及两者混合（Mixed）。实验在多个基准测试上进行，包括结构化多跳推理（HotpotQA、2WikiMultiHopQA、Bamboogle、MuSiQue）和复杂信息寻求问答（BrowseComp-plus、Frames、LongSeAL）。主要结果以String-F1分数呈现。例如，在HotpotQA上，采用混合策略训练的Qwen3-1.7B达到了58.2分，与Qwen3-8B（58.2分）持平，相比其原始性能（42.3分）和标准蒸馏性能（47.9分）有大幅提升。ASP显著增加了SLMs的搜索频率（从原始模型的1.72次提升至SFT的2.47次和OPD的2.84次），并提高了在噪声检索下的鲁棒性（性能下降仅2.3和1.7分，而标准蒸馏模型下降12.1分）。

最后，论文通过引入置信度探测，评估了SLMs是否应该进行自适应搜索。实验模拟了不同置信度阈值（P=1%, 5%, 10%, 20%）下的自适应搜索，发现在HotpotQA上，大模型（如Qwen3-32B）在P=10%时性能仅下降0.6分，而SLMs（如SFT-Qwen3-1.7B）在P=5%时性能就下降4.8分，表明SLMs缺乏可靠的内部知识，自适应搜索会导致性能显著下降，因此“始终搜索”是最佳策略。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度展开。首先，当前训练框架相对简单，未来可探索将 \policy 融入更先进的训练范式（如课程学习或强化学习），以进一步释放小型语言模型（SLM）的潜力。其次，研究未系统探讨SLM智能体的理论上限，其性能不仅受检索行为影响，还取决于模型本身的推理能力；未来需量化这些因素，以明确SLM与大型语言模型（LLM）的能力边界。此外，\policy 假设检索信息始终可靠，但现实搜索环境存在噪声与误导性内容，因此需开发鲁棒机制（如置信度校准或多源验证）来提升抗干扰能力。最后，实验仅基于Qwen模型系列，未来应在多样化架构（如Decoder-only与Encoder-Decoder模型）上进行验证，以增强方法的普适性。结合领域趋势，还可探索动态搜索策略——让SLM根据查询复杂度自适应调整检索频率，而非完全避免“猜测”，从而在效率与准确性间取得平衡。

### Q6: 总结一下论文的主要内容

该论文针对知识密集型任务中，小型语言模型（SLMs）作为搜索代理时性能不足的问题展开研究。核心问题是SLMs在复杂多跳推理任务中倾向于依赖自身参数知识而非调用搜索工具，导致检索频率低、幻觉增多，从而与大型语言模型（LLMs）存在显著性能差距。为解决此问题，论文提出了ASP方法，这是一种轻量级微调方法，通过显式训练SLMs优先执行搜索并基于检索证据生成答案，从而强化其工具使用行为。实验表明，该方法在Bamboogle和HotpotQA基准上分别提升17.3和15.3分，使SLMs达到LLM级别的性能。主要结论是：自适应搜索策略在SLMs中往往适得其反，而强制一致的搜索行为是提升SLMs推理可靠性的关键，这为高效轻量级搜索代理的构建提供了重要方向。
