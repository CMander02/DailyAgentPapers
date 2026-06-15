---
title: "Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL"
authors:
  - "Yinglun Zhu"
date: "2026-06-12"
arxiv_id: "2606.14211"
arxiv_url: "https://arxiv.org/abs/2606.14211"
pdf_url: "https://arxiv.org/pdf/2606.14211v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent训练与对齐"
  - "Agent自我反思与校准"
  - "强化学习在Agent中的应用"
  - "Agent自我验证"
  - "文本到SQL Agent"
relevance_score: 8.0
---

# Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL

## 原始摘要

LLMs are increasingly deployed as agents that interact with external environments and observe feedback such as execution results, error messages, and tool outputs. A well-functioning agent should be able to leverage this feedback to accurately assess its own performance. Yet we find a persistent reflection gap: LLM agents tend to mis-assess their own outputs after observing concrete environment feedback -- even for questions they correctly answered -- and standard RL barely helps due to a credit-assignment mismatch. To close this gap, we propose RefGRPO, a simple yet effective fix that augments standard RL algorithms with two key ingredients: a free calibration bonus computed by contrasting the agent's own reflection with the actual outcome (requiring no additional reward model, LLM judge, or external annotation), and a dynamic schedule on its coefficient. Compared to standard RL baselines, our method simultaneously improves reflection calibration (e.g., reduces underconfidence rate $44.4\% \to 7.7\%$) and task accuracy (e.g., $75.1\% \to 76.5\%$) on text-to-SQL across five benchmarks. The resulting calibrated reflection turns the agent into its own verifier grounded in environment feedback, which further enables (i) better self-improvement that uses reflections as pseudo-rewards without outcome supervision, and (ii) more effective test-time selective prediction by committing only to rollouts flagged as correct.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在作为智能体与环境交互时存在的“反思差距”（reflection gap）问题。研究背景是，LLM智能体在接收到环境反馈（如执行结果、错误信息）后，应能准确评估自身表现，但现有方法存在不足：即使对于正确回答的问题，智能体也倾向于错误评估自身输出，表现出显著的“不自信”（underconfidence），例如在文本到SQL任务中，智能体标记为错误的答案中高达54.3%实际上是正确的。标准强化学习（如GRPO）虽然能提升任务准确性，但由于存在信用分配不匹配（credit-assignment mismatch）的结构性问题——即对正确但标记错误的轨迹给予负优势，反而抑制了诚实反思，导致这种反思差距持续存在。本文提出的核心问题是：如何在不依赖额外奖励模型、LLM评判或外部标注的情况下，同时改进LLM智能体的任务准确性和反思校准能力？为此，论文提出了RefGRPO算法，通过在标准RL中引入两项关键改进：一是利用自身反思与实际结果对比的自由校准奖励（free calibration bonus），二是动态调度其系数，从而在缩小反思差距的同时提升任务准确率。

### Q2: 有哪些相关研究？

**方法类**：相关工作包括使用RL进行LLM后训练的研究，如PPO、GRPO等算法在可验证奖励领域的应用。本文与这些工作的区别在于，标准RL存在信用分配错位问题，无法有效缩小反思差距，而本文提出的RefGRPO通过免费校准奖励解决了这一问题。**评测类**：相关研究包括对LLM代理自我评估能力的研究，如"反思差距"现象。本文首次系统性揭示了这一差距，并提供了更细粒度的校准评估指标。**应用类**：相关工作涉及Text-to-SQL任务上的代理训练。本文的独特贡献在于将校准反思转化为代理自身的验证器，实现了无需结果监督的伪奖励自我改进，以及基于反思质量的测试时选择性预测。与现有方法相比，RefGRPO无需额外奖励模型、LLM评判或人工标注，仅通过对比代理自身反思与环境实际反馈计算免费校准奖励。

### Q3: 论文如何解决这个问题？

论文通过提出 RefGRPO 算法来解决反射差距问题。该算法在标准强化学习框架 GRPO 中引入两个关键创新：**免费校准奖励（Free Calibration Bonus）** 和 **动态系数调度（Dynamic Schedule）**。

核心方法是在 GRPO 的优势函数计算中，将原始的二进制结果奖励 `outcome` 与一个校准奖励相结合。校准奖励通过对比智能体自身的后反馈反射得分 `reflection` 与实际结果 `outcome` 计算得出：如果两者一致（例如，智能体认为错误且实际错误，或认为正确且实际正确），则给予一个额外的正校准奖励；否则为0。这个校准信号是“免费”的，因为它直接从现有的智能体输出和环境反馈中得出，无需额外的奖励模型、LLM裁判或人工标注。

**架构和关键技术**包括：
1. **校准奖励机制**：对于每个轨迹，将原始奖励 `outcome` 增强为 `augmented_reward = outcome + coefficient * calibration_bonus`。其中 `calibration_bonus` 是二元指示函数，表示反射与结果是否一致。这使得无论任务是否成功，反射准确的轨迹都获得更高奖励，从而解决“信用分配不匹配”问题（即输出结果相同但反射质量不同的轨迹获得相同优势）。
2. **动态系数调度**：为平衡校准质量和任务准确性，引入分阶段调度策略。在训练的前三分之二时间使用较大的校准系数（如0.1）优先优化反射校准，后三分之一时间系数降至0，让模型专注于任务性能同时保留已习得的校准能力。
3. **改进的GRPO目标**：在GRPO基础上加入长度归一化和非对称裁剪，移除KL散度项，使学习更直接由可验证奖励驱动。

实验表明，RefGRPO在文本到SQL等任务上同时降低了44.4%→7.7%的不自信率，并提升了任务准确率，使智能体成为自身基于环境反馈的验证器，还可利用校准反射进行无结果监督的自改进和测试时选择性预测。

### Q4: 论文做了哪些实验？

论文在text-to-SQL任务上进行了实验，这是一个具有可验证奖励的智能体环境。实验设置包括单轮和多轮（最多6轮）两种场景。训练数据来自Spider和OmniSQL训练集的4,660个问题，评估使用Spider-Dev、Spider-Domain Knowledge、Spider-Realistic、Spider-Test和Bird-Dev五个标准基准。对比方法包括GRPOplus（基于GRPO的强化学习基线）和RefGRPO（本文方法），并额外对比了OmniSQL-7B和SQL-R1-7B两个7B SQL专家模型。使用的基座模型为Llama-3.2-3B-Instruct和Qwen2.5-Coder-3B/7B-Instruct。

主要结果：在单轮设置中，RefGRPO在Qwen-3B上将欠自信率从GRPOplus的23.7%降至1.3%，反思准确率从76.6%提升至79.7%；在Llama-3B上欠自信率从30.9%降至23.5%，Chow score从58.4提升至62.2。多轮设置中，RefGRPO在Qwen-7B上任务准确率从75.1%提升至76.5%，欠自信率从44.4%降至7.7%。与7B专家对比，RefGRPO的校准增量Δ（反思准确率减任务准确率）为+1.3%，显著优于SQL-R1（+0.2%）和OmniSQL（-1.0%）。此外，RefGRPO还实现了更好的自我提升（+2.8 vs +0.5准确率提升）和选择性预测效果（单轮提升+1.6 vs +0.6）。

### Q5: 有什么可以进一步探索的点？

该研究在text-to-SQL任务上验证了RefGRPO的有效性，但未来可探索以下几个方向：1) **扩展到更多元化的智能体任务**：当前仅聚焦于SQL生成，未来可推广到代码生成、数学推理、网页导航等具有可验证反馈的环境，检验方法的通用性。2) **探索更复杂的反馈形式**：当前使用执行正确性作为二元结果，但对于部分正确、模糊反馈或连续奖励值场景，如何设计校准奖励机制值得研究。3) **改进动态调度策略**：当前线性衰减系数可能并非最优，可探索自适应学习率或基于验证集性能调整的调度策略。4) **缓解过自信问题**：虽然方法显著降低了欠自信率，但在多轮场景中过自信率改善有限（如7B模型从22.8%降至22.4%），可尝试引入对抗性反思或集成校准机制。5) **结合过程奖励**：将细粒度的过程监督信号融入校准奖励，进一步提升复杂多步推理中的反思质量。

### Q6: 总结一下论文的主要内容

本文研究了大型语言模型（LLM）作为智能体与环境交互时的“反射差距”问题：智能体在观察到环境反馈后，往往无法准确评估自身输出，即使对正确答案也会表现出错误判断，且标准强化学习（RL）因信用分配不匹配而难以解决。为弥合这一差距，作者提出RefGRPO方法，通过两个关键改进增强标准RL算法：一是引入“免费校准奖励”，通过对比智能体自身的反射与实际结果直接计算（无需额外奖励模型、LLM裁判或外部标注），二是动态调整其系数。实验表明，在文本转SQL任务中，RefGRPO相比标准RL基线，同时提升了反射校准（如将过度不自信率从44.4%降至7.7%）和任务准确率（从75.1%提升至76.5%）。校准后的反射使智能体成为基于环境反馈的验证器，进一步支持无需结果监督的自我改进和更有效的测试时选择性预测。该工作为赋予智能体可靠的自我反思能力提供了简洁有效的解决方案。
