---
title: "Iterative Visual Thinking: Teaching Vision-Language Models Spatial Self-Correction through Visual Feedback"
authors:
  - "Animesh Tripathy"
  - "Aswanth Krishnan"
date: "2026-06-11"
arxiv_id: "2606.13156"
arxiv_url: "https://arxiv.org/abs/2606.13156"
pdf_url: "https://arxiv.org/pdf/2606.13156v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "视觉语言模型"
  - "自校正"
  - "空间定位"
  - "闭环框架"
  - "GRPO"
  - "参照表达理解"
relevance_score: 8.5
---

# Iterative Visual Thinking: Teaching Vision-Language Models Spatial Self-Correction through Visual Feedback

## 原始摘要

Vision-language models (VLMs) achieve strong singleshot spatial grounding, yet lack any mechanism to observe and correct their own predictions. We find that naively prompting a VLM to iterate over rendered visualizations of its predictions causes catastrophic failure: Acc@0.5 on referring expression comprehension collapses from 79.6% to 48.7% (a 31 percentage point drop), revealing a fundamental gap between grounding capability and self-correction ability. We propose Iterative Visual Thinking (IVT), a closed-loop framework in which the model predicts a bounding box, observes the prediction rendered on the image, and iteratively refines through visual feedback. A two-phase training recipe closes the self-correction gap: first, we exploit the base model's own predictions as realistic errors and prompt a teacher VLM to generate corrective reasoning traces, yielding supervised data without human annotation; second, we apply Group Relative Policy Optimization (GRPO) with a simple IoU reward to stabilize multi-step refinement. On a mixed benchmark spanning RefCOCOg, Ref-Adv, and Ref-L4 (505 test samples), SFT warm-up with IVT surpasses the single-shot base model on every metric: Acc@0.5 rises to 82.0% (+2.4pp), Acc@0.7 to 74.1% (+3.2pp), and Acc@0.9 to 48.3% (+2.8pp). GRPO further reduces per-step IoU degradation by 5x, stabilizing the refinement trajectory. All training uses only 2,400 samples on a single GPU, demonstrating that spatial self-correction is a learnable capability that can be instilled at modest scale.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视觉语言模型（VLM）在空间推理任务中缺乏自我修正能力的问题。研究背景是，虽然现有VLM在单次前向传播中能较好地完成指代表达理解等空间定位任务（如一个4B模型在复杂基准上可达约80%的Acc@0.5），但其预测过程是开环的，无法像人类那样观察自己的预测并进行迭代修正。现有方法的不足在于，当简单提示VLM基于其预测的可视化渲染结果进行迭代时，性能会灾难性地下降（Acc@0.5从79.6%暴跌至48.7%），暴露出一个“自我修正鸿沟”——模型能生成空间预测，却无法理解并利用自身的可视化预测反馈来修正错误。本文的核心问题是：如何让VLM学会闭环的空间推理过程，即通过观察自身预测的可视化渲染结果作为视觉反馈，进行迭代的自我修正，从而弥合基础定位能力与自我修正能力之间的差距。

### Q2: 有哪些相关研究？

相关研究可从以下几类梳理：**方法类**方面，Referring Expression Comprehension（REC）领域的方法如MDETR、Grounding DINO、Kosmos-2及通用VLM（Qwen2-VL等）均采用单次预测模式，缺乏自校正机制，而本文在此基础上添加了闭环校正功能。**自校正与反馈类**研究中，Self-Refine和Reflexion探索了文本自校正，但Huang等人指出LLM需外部反馈；视觉领域Liao等人发现VLM无法自校正确认误差，Critic-V通过DPO训练独立评审器。本文发现直接迭代视觉思维会导致性能崩溃（Acc@0.5下降31pp），与上述结论一致，但区别在于本文使用视觉反馈（模型观察自身预测的渲染结果）而非文本批评。**视觉推理与测试时计算**方面，CogCoM、GRIT通过视觉操作链推理，ViGoRL采用多轮强化学习动态缩放区域，RRVF提出闭环推理-渲染-视觉反馈范式。本文区别于这些工作在于，它将模型自身空间预测渲染为视觉叠加层并重新注入，用于同一定位任务的自我校正，而非缩放获取新信息或纯文本推理链。**强化学习类**研究中，GRPO被DeepSeek-Math、DeepSeek-R1采用以消除价值函数；VLM-R1证明纯IoU奖励优于复合奖励；本文在多重视觉推理轨迹上应用GRPO，但发现需要SFT预热启动空间自校正（因为基模型rollout中从未自然出现该能力）。

### Q3: 论文如何解决这个问题？

论文通过迭代视觉思考（IVT）框架解决视觉语言模型无法自我修正空间预测的问题。核心方法是一种闭环推理机制，模型生成边界框预测后，将预测结果渲染为图像上的半透明红色框作为视觉反馈，再基于此进行迭代优化。整体框架包含两阶段训练：首先采用监督微调（SFT）预热，利用学生模型自身预测作为起始点（而非人工扰动），通过线性插值构建从学生预测到真实框的修正轨迹，并由教师VLM生成步骤相关的推理踪迹作为训练数据，这避免了数据标注成本。第二阶段采用分组相对策略优化（GRPO），定义基于交并比（IoU）的简单奖励函数（最终步IoU + 格式奖励），通过策略梯度更新稳定多步优化，防止奖励函数复杂导致的训练不稳定。关键技术包括：将坐标归一化为[0,1000]整数表示以解耦分辨率；保留自回归连贯性的单轮对话前缀延续；通过IoU筛选（丢弃>0.85的优良预测）只保留可改进样本；RL阶段使用KL散度正则化防止偏离SFT初始化。创新点在于利用学生自身预测构建轨迹解决了“起始步摆烂”问题，并通过简单IoU奖励使训练稳定，仅用2400样本单GPU即可训练出能进行多步空间自我修正的模型。

### Q4: 论文做了哪些实验？

论文在混合基准测试上进行了实验，包含RefCOCOg、Ref-Adv和Ref-L4三个数据集，共505个测试样本。训练集使用2400个样本，在单GPU上完成训练。基础模型为Qwen3-VL-4B-Instruct，采用LoRA微调。实验比较了五种配置：Base单次推理、Base+IVT无训练迭代、SFT+IVT、SFT+GRPO（单步）和SFT+GRPO+IVT。

主要结果：Base单次推理的Acc@0.5为79.6%，Acc@0.7为70.9%，Acc@0.9为45.5%，平均IoU为0.719。直接使用IVT无训练导致性能骤降，Acc@0.5跌至48.7%（下降31个百分点）。SFT+IVT在所有指标上超越基础模型，Acc@0.5达到82.0%（+2.4pp），Acc@0.7达到74.1%（+3.2pp），Acc@0.9达到48.3%（+2.8pp），平均IoU升至0.743。SFT+GRPO+IVT的Acc@0.5为80.6%，Acc@0.7为72.5%，但GRPO的关键贡献在于稳定性：将每步IoU下降从SFT的0.140降至0.029（减少5倍），恶化样本比例从63.4%降至24.8%。难度分层分析显示，困难样本（初始IoU<0.5）从迭代中获益最多，平均IoU从0.108升至0.149。

### Q5: 有什么可以进一步探索的点？

论文的主要局限性在于：1）迭代推理增加了3倍延迟，且难样本的IoU提升有限（0.108→0.149），易样本反而可能退化（0.920→0.868）；2）训练数据规模仅2400样本，且仅使用单一模型族（Qwen3-VL-4B）；3）GRPO虽稳定了修正轨迹，但真正的步间IoU提升仍未实现。

未来可探索的方向包括：1）设计自适应迭代策略，对难样本应用更多轮次、易样本提前终止，平衡精度与效率；2）将框架扩展到多目标定位、分割等更复杂的空间任务，设计更丰富的视觉反馈信号（如边界距离图）；3）结合更大的基座模型（如70B以上）或MoE架构，观察自修正能力是否随规模涌现；4）探索无需SFT冷启动的方法，例如用合成渲染数据预训练视觉反馈理解模块，或设计自监督的对比目标直接学习修正行为；5）改进GRPO的奖励设计，引入步间IoU改善率的细粒度激励，而非仅用最终IoU。

### Q6: 总结一下论文的主要内容

这篇论文提出了迭代视觉思维（IVT），一种闭环框架，用于解决视觉语言模型（VLM）在空间定位中缺乏自我修正能力的问题。论文首先定义了问题：VLM虽能单次精准定位，但无法观察并修正自己的预测，简单提示迭代利用渲染结果会导致性能崩溃（Acc@0.5从79.6%暴跌至48.7%）。方法上，IVT框架让模型预测边界框、观察渲染结果，并通过视觉反馈迭代优化。论文采用两阶段训练：先用VLM自身预测作为错误样本，让教师VLM生成修正推理轨迹，获取无标注监督数据；再用群体相对策略优化（GRPO）配合IoU奖励稳定多步修正。主要结论是，在RefCOCOg等混合基准上，监督微调预热使IVT在所有指标上超越基线（Acc@0.5达82.0%），GRPO将每步IoU退化降低5倍。核心贡献在于证明了空间自我修正是可通过小规模数据（2400样本）学习的可培养能力，具有重要实际意义。
