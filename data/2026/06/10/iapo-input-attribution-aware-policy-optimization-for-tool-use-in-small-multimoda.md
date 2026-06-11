---
title: "IAPO: Input Attribution-Aware Policy Optimization for Tool Use in Small Multimodal Agents"
authors:
  - "Yifan Yang"
  - "Zhen Zhang"
  - "Jiayi Tian"
  - "Liyan Tan"
  - "Zheng Zhang"
date: "2026-06-10"
arxiv_id: "2606.11652"
arxiv_url: "https://arxiv.org/abs/2606.11652"
pdf_url: "https://arxiv.org/pdf/2606.11652v1"
categories:
  - "cs.LG"
tags:
  - "多模态智能体"
  - "工具使用"
  - "小语言模型"
  - "强化学习"
  - "输入归因对齐"
  - "策略优化"
relevance_score: 8.5
---

# IAPO: Input Attribution-Aware Policy Optimization for Tool Use in Small Multimodal Agents

## 原始摘要

This paper investigates reinforcement learning (RL) methods for improving tool-calling capabilities in multimodal small language model (SLM) agents. While existing works have explored various reward designs to improve agentic tool-calling ability, these approaches face inherent limitations for SLM training, especially under multimodal scenarios. First, many existing methods evaluate tool use correctness through exact matching against certain ground-truth or predefined formats. However, this assumption is often unsuitable for multimodal tasks, where multiple tool use paths may be valid and annotated tool trajectories are typically unavailable. Second, such sparse and brittle binary rewards provide little guidance on how to improve the underlying decision process, making them particularly difficult for multimodal SLM to learn from. To address these issues, we propose Input Attribution-Aware Policy Optimization (IAPO), an RL algorithm for improving tool use in multimodal SLM by aligning the model's attribution across input components with that of a stronger teacher. Experiments on Qwen2.5-VL-3B show that the proposed method improves visual question answering accuracy by an average of 3% across six test sets compared with existing visual tool use work, by helping the model attend to the most relevant input evidence.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文的核心问题是：如何通过强化学习有效提升多模态小语言模型（SLM）自主使用工具的决策能力？研究背景是，虽然强化学习（如GRPO）已被广泛用于训练大语言模型（LLM）完成复杂的工具调用任务，但由于SLM参数少、推理能力弱，直接应用现有方法效果不佳。现有方法的不足主要体现在两方面：第一，许多工具使用评估依赖于对标准答案或预定义格式的精确匹配，但多模态任务（如视觉问答）往往存在多种合理的工具调用路径，且缺少标注的工具轨迹，因此这种稀疏的二元奖励并不适用；第二，这种脆弱的二值奖励无法为决策过程提供有效的梯度信号，导致SLM难以从中学习到正确的工具选择策略。针对这些挑战，本文提出了输入归因感知策略优化（IAPO）算法，旨在利用一个更强的教师模型，通过在强化学习过程中比较学生模型与教师模型在各个输入组件上的归因分布（即注意力分配）的KL散度，来提供密集且富含信息的监督信号，从而引导SLM学习更正确、更鲁棒的工具调用行为。

### Q2: 有哪些相关研究？

本文相关研究主要分为推理增强方法和强化学习方法两类。在推理增强方法方面，Visual Sketchpad和Refocus等早期工作通过中间视觉推理步骤提升多模态推理能力，允许模型在推理过程中生成视觉标注或调用图像编辑工具（如裁剪、高亮、遮罩），实现对任务相关视觉区域的迭代聚焦。在强化学习方法方面，DeepEyes首次将图像涉及的tool调用纳入RL训练，鼓励VLM"用图像思考"；OpenThinkIMG和VTool-R1则进一步将视觉编辑工具集成到RL微调框架中，使VLM在文本推理中穿插中间视觉操作。本文与上述工作的核心区别在于奖励设计：现有方法多采用基于地面真值或预定义格式的稀疏二值奖励，难以适应多模态任务中多有效路径和缺乏标注轨迹的场景；而本文提出的IAPO方法通过引入输入属性对齐的新型细粒度中间奖励，将教师模型对输入组件的归因与弱模型对齐，为多模态SLM提供更丰富的学习信号，最终在六个测试集上平均提升3%的视觉问答准确率。

### Q3: 论文如何解决这个问题？

IAPO通过引入基于输入归因的惩罚项来增强GRPO框架，解决多模态小语言模型工具使用中的信用分配问题。其核心设计包括两个关键模块：首先，提出积分梯度归因分数，将输入提示按语义功能划分为四个块类型（纯文本上下文P、用户查询R、图像占位符I、工具定义T），通过计算工具调用序列对数概率关于输入嵌入的梯度，结合梯度和嵌入的点积得到每个标记的归因权重，再聚合为块级分数。其次，基于归因分数设计对齐惩罚，分别计算学生策略和更强的教师模型（如Qwen2.5-VL-72B）在相同输入上的归因分布，用KL散度衡量两者差异作为惩罚项。最终奖励函数由原始结果奖励减去加权后的归因对齐惩罚组成，该奖励经组内归一化后用于GRPO优化。

该方法的核心创新在于：1）打破了传统二进制结果奖励的稀疏性，通过归因惩罚提供细粒度指导信号；2）利用模型输出的对数概率梯度自动计算归因，无需人工标注工具使用轨迹；3）通过教师归因分布蒸馏，促使学生模型将注意力集中在真正影响工具决策的输入成分上。实验显示，该方法在6个测试集上平均提升VQA准确率3%，有效缓解了多模态小模型在工具调用中的过拟合和短路现象。

### Q4: 论文做了哪些实验？

论文在视觉问答任务上评估了IAPO方法，使用Qwen2.5-VL-3B作为骨干模型，并在6个测试集（CharXiv、Horizontal、Vertical、VWTQ、VWTQ_syn、VTabFact）上报告准确率。实验设置包括：使用VeRL框架和AdamW优化器进行强化学习训练，先训练7B教师模型（用GRPO），再分两个阶段训练3B学生模型（冷启动GRPO阶段和IAPO阶段）。对比方法包括：离线模型（GPT-4o、Qwen2.5-VL-7B/3B）、VTool-R1（标准GRPO）、TRM（用GPT-4o作为验证器）、ToRL（添加工具执行惩罚）。主要结果：IAPO在6个测试集上的平均准确率为55.9%，优于VTool-R1的52.9%、TRM的53.4%、ToRL的53.8%，较现有视觉工具使用工作平均提升约3%。在CharXiv上IAPO表现更突出（26.1% vs TRM 23.6%和ToRL 24.1%），显示出更强的泛化能力。消融实验和训练动态分析表明，IAPO维持了更高的工具调用率（接近100%）和工具调用成功率，并改善了模型的输入归因对齐。

### Q5: 有什么可以进一步探索的点？

结合论文的局限性与未来可探索方向，可以从以下几点深入：

1. **教师依赖与泛化性**：IAPO依赖外部教师模型提供“正确”的输入归因分数。当教师模型本身存在偏差或任务超出其知识范围时，学生可能学到错误归因。未来可探索无教师或自监督归因方法，例如利用模型自身置信度或验证反馈动态调整归因。

2. **归因计算效率**：积分梯度（IG）在每次训练迭代中需多次前向传播，计算开销大。可研究近似归因（如随机掩码）或蒸馏归因网络以加速训练。

3. **多步工具链场景**：当前方法主要针对单步工具调用，未涉及多步协作（如连续调用多个工具并依赖中间结果）。扩展归因概念至序列决策过程（如使用因果链或反事实推理）是重要方向。

4. **归因与奖励的协同**：仅通过归因惩罚可能无法完全解决“工具调用路径多样性”问题。建议融入学习后的奖励模型（如基于对比学习的路径排序）来对归因进行加权，平衡探索与利用。

### Q6: 总结一下论文的主要内容

本文提出了一种名为输入归因感知策略优化（IAPO）的新方法，旨在解决多模态小语言模型(SLM)在工具使用场景下的强化学习训练难题。现有方法依赖精确匹配的二进制奖励，不适用于多模态任务中多种有效工具路径并存的情况，且对SLM学习过程的指导不足。IAPO的核心思想是：利用集成梯度(IG)量化模型输入组件对生成工具调用的贡献度，并通过最小化学生模型与更强教师模型之间的IG分布KL散度，构建密集的归因对齐奖励信号。实验基于Qwen2.5-VL-3B模型，在六个视觉问答测试集上，IAPO相比现有方法平均提升了3%的准确率。该方法首次为SLM训练设计了基于输入归因的奖励，通过监督决策过程而非仅结果，有效提升了模型对最相关输入证据的注意力，为构建高效的多模态智能体提供了新范式。
