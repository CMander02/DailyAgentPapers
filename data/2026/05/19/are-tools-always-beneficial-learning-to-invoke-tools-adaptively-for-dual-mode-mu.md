---
title: "Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning"
authors:
  - "Qinghe Ma"
  - "Zhen Zhao"
  - "Yiming Wu"
  - "Jian Zhang"
  - "Lei Bai"
  - "Yinghuan Shi"
date: "2026-05-19"
arxiv_id: "2605.19852"
arxiv_url: "https://arxiv.org/abs/2605.19852"
pdf_url: "https://arxiv.org/pdf/2605.19852v1"
github_url: "https://github.com/MQinghe/AutoTool"
categories:
  - "cs.CL"
tags:
  - "MLLM"
  - "Tool-Augmented Reasoning"
  - "Adaptive Tool Invocation"
  - "Reinforcement Learning"
  - "Dual-Mode Reasoning"
  - "Efficiency"
  - "Multimodal Reasoning"
relevance_score: 7.5
---

# Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning

## 原始摘要

Tool-augmented reasoning has emerged as a promising direction for enhancing the reasoning capabilities of multimodal large language models (MLLMs). However, existing studies mainly focus on enabling models to perform tool invocation, while neglecting the necessity of invoking tools. We argue that tool usage is not always beneficial, as redundant or inappropriate invocations largely increase reasoning overhead and even mislead model predictions. To address this issue, we introduce AutoTool, a model that adaptively decides whether to invoke tools according to the characteristics of each query. Within a reinforcement learning framework, we design an explicit dual-mode reasoning strategy with mode-specific reward functions to guide the model toward producing accurate responses. Moreover, to prevent premature bias toward a single reasoning mode, AutoTool jointly explores and balances tool-assisted and text-centric reasoning throughout training, and promotes free exploration in later stages. Extensive experiments demonstrate that AutoTool exhibits outstanding performance and high efficiency, yielding a 21.8\% accuracy gain on V* benchmark compared to the base model, and a 44.9\% improvement in efficiency over existing tool-augmented methods on POPE benchmark. Code is available at https://github.com/MQinghe/AutoTool.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文针对多模态大语言模型（MLLM）在工具增强推理中存在的过度依赖问题展开研究。现有方法如OpenThinkIMG和DeepEyes，主要关注如何让模型学会使用工具进行推理，却忽视了“是否需要使用工具”这一关键决策。这导致模型对所有查询都倾向于调用外部工具（如放大、搜索等），不仅大幅增加了训练和推理的计算开销（如DeepEyes的推理时间增加了20%以上），而且冗余或不恰当的工具调用会引入无关或错误的视觉信息，干扰模型对全局理解的判断，甚至加剧幻觉现象。例如，在回答关于人与汽车空间关系这类需要全局理解的简单问题时，不必要的局部放大反而会误导推理。为此，本文提出AutoTool模型，其核心创新在于让模型自适应地决定是否调用工具。通过引入两个特殊标记（<tool_on>和<tool_off>），模型可在“使用工具”和“纯文本推理”两种模式间灵活切换，并借助强化学习框架设计了模式特定的奖励函数（MSPO），以鼓励对简单问题不调工具、对复杂问题正确调用工具。同时，为克服模型初期对单一模式的偏好，还提出了自适应模式平衡策略（AMB），确保两种推理模式得到充分探索，最终在提升推理准确性的同时大幅提高效率。

### Q2: 有哪些相关研究？

多项相关研究已围绕多模态大模型（MLLM）的推理能力展开。**基础模型方面**，LLaVA、BLIP、Qwen-VL等采用预训练视觉编码器（如CLIP-ViT）与LLM结合的模块化架构，Flamingo、Cambrian-1集成多编码器增强视觉表示，EVE、MonoInternVL、SAIL则探索统一Transformer的端到端架构。**工具辅助推理方面**，Visual Sketchpad、OpenThinkIMG、Thyme使模型能调用分割、OCR等外部工具获取视觉线索；BAGEL、Visual Planning、GoT则通过生成新视觉状态隐式融入工具能力。获取工具能力的方法分为三类：基于提示的上下文学习、监督微调、以及强化学习优化工具使用策略。**强化学习推理增强方面**，DeepSeek-R1展示简单规则能诱导思维链推理，DeepEyes、TreeVGR、Thyme使用组相对策略优化（GRPO）进行工具辅助推理训练。本文与传统工作的区别在于：（1）现有方法聚焦“如何使用工具”，忽略了工具冗余调用带来的开销和误导风险；（2）与单一工具增强模式不同，本文通过显式双模式推理策略和模式特定奖励函数，在RL框架内平衡工具辅助推理与纯文本推理；（3）采用自适应模式平衡策略，防止模型过早偏向单一推理模式。与DeepEyes等纯粹强化工具调用的方法相比，本文更注重情境自适应的工具调用决策，在V*基准上提升21.8%准确率，POPE基准上效率比现有工具增强方法提升44.9%。

### Q3: 论文如何解决这个问题？

论文提出AutoTool框架来解决“工具并非总是有益”的核心问题。其核心方法是让多模态大模型（MLLM）自适应地决定是否调用工具，从而在推理效率和准确性间取得平衡。整体框架基于强化学习中的组相对策略优化（GRPO）算法。

**核心架构**包含两大推理模式：(1) **纯文本推理**（`<tool_off>`模式）：模型直接在文本空间中进行链式推理，不涉及任何外部工具，适用于简单或无需外部视觉信息的查询。(2) **工具增强推理**（`<tool_on>`模式）：模型首先生成`<tool_call>`动作（如调用zoom-in函数定位图像中的感兴趣区域），然后将工具返回的视觉观察（裁剪后的图像）追加到上下文中，再进行后续推理并输出最终答案`<tool_response>`。

**关键技术**包括三个创新点：第一，**双模式推理策略**：通过定义`<tool_on>`和`<tool_off>`两个特殊控制token，让模型显式选择推理路径。第二，**自适应模式平衡（AMB）策略**：在训练过程中，动态调整两种模式的奖励系数。具体而言，根据当前批次中工具调用频率`F_on`，对`<tool_on>`和`<tool_off>`模式的工具奖励系数`λ_tool`进行自适应补偿（如`λ_tool^on = λ_tool^base + 0.5 - F_on`），确保模型充分探索两种模式。训练后期（最后20步）移除该约束，让模型基于内部置信度自由选择。第三，**多维度奖励函数**：综合三个奖励信号——答案准确性奖励（`R_acc`）、格式合规性奖励（`R_format`）和模式特定工具调用奖励（`R_tool`），其中`R_tool`对工具调用成功且答案正确给予正向奖励，对工具调用但答案错误给予惩罚，从而鼓励模型在必要时才使用工具。

### Q4: 论文做了哪些实验？

论文在多个基准上进行了全面实验。实验设置方面，使用Qwen2.5-VL-7B作为基座模型，采用GRPO算法在8块H200 GPU上训练80轮，使用Qwen2.5-72B-Instruct作为奖励模型。训练数据包括V*细粒度样本、ArxivQA图表数据和ThinkLite-VL推理数据。**基准测试**分为四类：(1) 感知基准（V*、HRbench-4K/8K），评估目标属性和空间关系；(2) 定位基准（refCOCO系列、ReasonSeg），用IoU>0.5评估边界框预测；(3) 幻觉基准（POPE），评估目标存在性判断；(4) 推理基准（MathVista等六个数据集），涵盖数学、逻辑等多类型推理。**对比方法**包括GPT-4o、Qwen2.5-VL系列、InternVL3、SEAL、DyFo、ZoomEye、DeepEyes等。**主要结果**：在感知基准上，AutoTool在V*基准上相比基模型提升21.8%准确率（总体90.1% vs 69.1%），在HRbench-4K上总体76.9%。在定位基准上，在refCOCO test上达88.5%，全面超越DeepEyes。在幻觉基准POPE上，总体准确率88.9%，且推理效率相比DeepEyes提升44.9%。消融实验验证了双模式、惩罚项和自由探索模块均有效。

### Q5: 有什么可以进一步探索的点？

论文的核心创新在于提出工具调用的“必要性”判断，但当前方法仍存在若干可探索的方向。首先，**工具选择的粒度可进一步细化**，目前仅决定“是否调用”，未来可设计多级调用策略，如区分视觉搜索、文本检索或逻辑推理等不同工具类型，并动态组合。其次，**奖励函数的设计**当前依赖任务准确率（如V*基准），可能忽略不同模态内部的细粒度错误（如物体定位与视觉属性判断），可引入对抗性样本或不确定性估计来提升鲁棒性。第三，**模式切换的可解释性**不足，模型仅通过强化学习隐式学习何时调用工具，未来可引入元认知模块（如预测调用成本-收益比），或利用大语言模型的Chain-of-Thought生成调用理由。最后，**长尾场景的泛化**仍是挑战，当前训练数据可能偏向常见调用模式，可借鉴主动学习思想，让模型自主生成高难度样本进行自我博弈训练。

### Q6: 总结一下论文的主要内容

本文提出AutoTool模型，旨在解决多模态大模型工具增强推理中“工具并非总是有益”的问题。现有方法过度依赖工具调用，导致冗余计算、推理开销增加，甚至引入错误信息引发幻觉。AutoTool通过强化学习框架，显式设计双模式推理策略（<tool_on>和<tool_off>），并引入模式特定奖励函数（MSPO）分别优化工具辅助推理与纯文本推理。为避免模型过早偏向某一模式，采用自适应模式平衡（AMB）策略动态调整奖励系数，确保双模式充分探索，后期再放开约束让模型自主决策。在V*基准上，AutoTool相比基础模型准确率提升21.8%；在POPE基准上，相比现有工具增强方法效率提升44.9%，验证了自适应工具调用的有效性。核心贡献在于揭示工具使用的双面性，并提出平衡效率与准确性的自适应框架。
