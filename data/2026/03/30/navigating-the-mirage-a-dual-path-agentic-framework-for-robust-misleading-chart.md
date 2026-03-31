---
title: "Navigating the Mirage: A Dual-Path Agentic Framework for Robust Misleading Chart Question Answering"
authors:
  - "Yanjie Zhang"
  - "Yafei Li"
  - "Rui Sheng"
  - "Zixin Chen"
  - "Yanna Lin"
  - "Huamin Qu"
  - "Lei Chen"
  - "Yushi Sun"
date: "2026-03-30"
arxiv_id: "2603.28583"
arxiv_url: "https://arxiv.org/abs/2603.28583"
pdf_url: "https://arxiv.org/pdf/2603.28583v1"
categories:
  - "cs.CV"
  - "cs.AI"
  - "cs.MM"
tags:
  - "视觉语言模型"
  - "智能体框架"
  - "多模态推理"
  - "对抗鲁棒性"
  - "图表理解"
  - "工具使用"
  - "指令微调"
relevance_score: 7.5
---

# Navigating the Mirage: A Dual-Path Agentic Framework for Robust Misleading Chart Question Answering

## 原始摘要

Despite the success of Vision-Language Models (VLMs), misleading charts remain a significant challenge due to their deceptive visual structures and distorted data representations. We present ChartCynics, an agentic dual-path framework designed to unmask visual deception via a "skeptical" reasoning paradigm. Unlike holistic models, ChartCynics decouples perception from verification: a Diagnostic Vision Path captures structural anomalies (e.g., inverted axes) through strategic ROI cropping, while an OCR-Driven Data Path ensures numerical grounding. To resolve cross-modal conflicts, we introduce an Agentic Summarizer optimized via a two-stage protocol: Oracle-Informed SFT for reasoning distillation and Deception-Aware GRPO for adversarial alignment. This pipeline effectively penalizes visual traps and enforces logical consistency. Evaluations on two benchmarks show that ChartCynics achieves 74.43% and 64.55% accuracy, providing an absolute performance boost of ~29% over the Qwen3-VL-8B backbone, outperforming state-of-the-art proprietary models. Our results demonstrate that specialized agentic workflows can grant smaller open-source models superior robustness, establishing a new foundation for trustworthy chart interpretation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视觉语言模型（VLMs）在面对具有误导性的图表时，其理解和推理能力严重不足的问题。研究背景是，图表在数据驱动的世界中无处不在，但常被有意或无意地设计成具有误导性（如操纵坐标轴、选择性呈现数据），以扭曲观者的数据感知。随着VLMs在自动化图表理解中变得日益重要，确保它们能抵御这类视觉欺骗已成为一个关键挑战。现有方法主要有两种范式：一是端到端的VLM路径，它整体处理图表，依赖宏观视觉启发（如整体趋势），但极易被恶意编码（如倒置的Y轴）所欺骗，陷入“认知奉承”，忽略真实数据；二是OCR增强的流程，它通过将图表线性化为文本来规避视觉陷阱，但丢失了至关重要的空间和布局语义，导致提取的数字实体（如坐标刻度与数据标签）严重错位，无法用于有效推理。这两种方法均无法在感知结构异常和精确提取数据之间取得良好平衡，且在出现跨模态（视觉趋势与数字事实）冲突时缺乏有效的仲裁机制。

因此，本文要解决的核心问题是：如何构建一个鲁棒的框架，使模型能够像人类审计员一样，主动检测图表中的视觉欺骗，并基于证据进行批判性推理，从而在“误导性图表问答”任务中得出逻辑一致的正确答案。具体而言，论文需要应对三个层面的挑战：在感知层面，如何迫使模型进行细粒度的、针对特定区域（如非零基线、被操纵的图例）的诊断；在推理层面，当视觉线索与OCR提取的数字证据相矛盾时，如何设计机制进行理性仲裁；在优化层面，如何将模型从被动观察者转变为“持怀疑态度的审计员”，抑制其预训练中的视觉偏见，优先考虑证据而非误导性启发。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：图表理解基准与方法、多模态模型增强技术，以及模型优化对齐策略。

在**图表理解基准与方法**方面，早期研究如FigureQA、DVQA等专注于从规范图表中提取事实信息。近年来，Misleading ChartQA、LEAF-QA等基准开始关注具有误导性编码（如截断坐标轴）的图表，揭示了现有视觉语言模型（VLMs）易受视觉“陷阱”影响的问题。本文的ChartCynics框架直接针对此类误导性图表，其核心区别在于采用了“怀疑式”的双路径推理范式，将感知与验证解耦，专门设计用于揭露视觉欺骗，而非进行通用的图表信息提取。

在**多模态模型增强技术**方面，已有工作如MATCHA、DePlot通过数学推理或图表转表格来链接像素与数据。ChartX、AskChart等则探索了利用OCR和文本增强来提供数值约束。本文借鉴了OCR驱动的数据路径以确保数值基础，但创新性地引入了诊断视觉路径，通过战略性的感兴趣区域裁剪来捕捉结构异常，并设计了智能体摘要器来解决跨模态冲突，这比单纯的模态增强更侧重于矛盾检测与一致性推理。

在**模型优化对齐策略**方面，监督微调（SFT）常用于注入领域知识，如调查性思维链。强化学习（RL），特别是群体相对策略优化（GRPO），被用于以可计算成本对齐复杂目标。本文相关工作（如Wang等人的研究）利用GRPO惩罚误导性干扰项，在困难样本上取得了高精度。本文在此基础上，提出了一个两阶段协议（Oracle-Informed SFT 和 Deception-Aware GRPO）进行对抗性对齐，专门针对误导性图表的对抗性环境优化智能体摘要器的推理过程。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ChartCynics的智能体双路径框架来解决误导性图表问答的挑战。其核心方法是采用一种“怀疑式”推理范式，将感知与验证解耦，从而揭露视觉欺骗。

整体框架包含两条并行的路径：诊断视觉路径和OCR驱动数据路径。诊断视觉路径负责捕捉图表的结构性异常（如倒置的坐标轴）。其关键创新在于通过一个自动化的感兴趣区域提取模块，精准定位图表关键组件（如标题、图例、坐标轴）的边界框，并进行语义完整性填充，确保诊断智能体能够进行“阅读”而非“估计”。该路径采用双智能体架构：诊断智能体在仅接收高分辨率ROI裁剪图、而屏蔽问题和选项的“盲测”条件下，生成一份包含诊断和行动指令的结构化报告；推理智能体则必须无条件信任该报告，并在其思维链的第一步明确锚定行动指令，从而将推理轨迹从未经校准的视觉先验转向融合多模态信息的后验概率。

OCR驱动数据路径旨在通过结构化文本和数字数据提取，重建底层的数值关系，绕过欺骗性的视觉编码。它利用先进的多模态OCR解析模块，将所有显式文本和数值实体提取并序列化为统一的Markdown格式。该路径还引入了动态信任评估原则（如对直接数据标签赋予高信任度，对仅依赖坐标轴刻度的情况保持怀疑）和完整性检查规则，以校准OCR提取的数据。

两条路径的信息最终汇入智能体融合模块（即Summarizer）。该模块通过实施一个层次化的权重系统，遵循两条“证据黄金法则”进行不一致感知融合：法则一（启发式校准）利用结构异常信息重新校准视觉推断，使其与数值真相同步；法则二（动态信任校准）根据信任级别标志动态调整OCR数据的认知权重。融合过程通过一个五步的“侦探思维链”具体实现：感知审计、数值锚定、欺骗映射、充分性与完整性检查、对抗性陷阱拒绝。这一过程确保最终答案是通过严格冲突解决而非视觉附和得出的。

此外，框架采用两阶段优化策略来内化上述推理逻辑：首先通过“Oracle-Informed SFT”进行推理知识蒸馏，然后通过“Deception-Aware GRPO”进行对抗性对齐，利用非对称奖励塑造来惩罚视觉陷阱并强化逻辑一致性。

### Q4: 论文做了哪些实验？

论文在三个基准数据集上进行了实验：Misleading ChartQA (MC，305个样本)、Curated Deceptive Chart Collection (CDCC，110个样本) 以及 Mixed Standard and Misleading Benchmark (MSMB，244个样本)。实验设置以Qwen3-VL-8B为骨干模型，采用双阶段优化：首先使用Misleading ChartQA训练集的5,238条推理链进行Oracle-Informed SFT，然后使用GRPO进行对抗性对齐，奖励函数包含事实性、矛盾性、逻辑性和格式等多个目标。

对比方法包括三类：1) 标准多模态基线模型，如ChartMoE、GPT-4o-mini、Gemini系列和Qwen3-VL-8B；2) 结构化缓解启发式方法，如表格式QA和图表重绘；3) 在不同骨干模型上应用ChartCynics框架的训练免费版本和完整版本。

主要结果显示，完整的ChartCynics框架在MC数据集上达到74.43%的准确率，在CDCC数据集上达到64.55%的准确率。相比Qwen3-VL-8B基线模型，在MC上带来了约29%的绝对性能提升。关键指标包括准确率(Acc)、因误导而错误(WM)和因其他原因错误(WO)。在MC数据集上，完整模型的WM低至11.15%，显著降低了模型被视觉陷阱欺骗的比例。实验还表明，训练免费的ChartCynics范式能普遍提升不同骨干模型的性能，例如将GPT-4o-mini在CDCC上的准确率从69.09%提升至79.09%。

### Q5: 有什么可以进一步探索的点？

本文提出的ChartCynics框架在误导性图表问答上取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其双路径设计（视觉诊断与OCR数据）依赖于预定义的规则进行区域裁剪和冲突检测，这可能无法泛化到更复杂或新颖的视觉欺骗模式上。未来研究可探索更自适应的感知模块，例如利用强化学习让智能体自主决定分析焦点。其次，框架的评估集中于静态图表，而现实中的误导可能存在于动态或交互式可视化中，如何扩展至此类场景是一个重要方向。此外，当前方法主要针对视觉结构扭曲，对基于语义误导（如标签误导、统计谬误）的图表处理能力尚未充分验证。结合外部知识库或因果推理来增强逻辑一致性检测是潜在的改进思路。最后，该框架的计算流程相对复杂，在实时应用场景下可能面临效率挑战，未来工作可研究如何优化智能体间的协作机制以平衡精度与速度。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为ChartCynics的新型智能体双路径框架，旨在解决误导性图表问答的挑战。核心问题是，现有视觉语言模型（VLMs）在处理具有欺骗性视觉结构和扭曲数据表示的图表时容易出错。

方法上，该框架采用“怀疑式”推理范式，将感知与验证解耦。它包含两条路径：诊断视觉路径通过策略性的感兴趣区域裁剪来捕捉结构异常（如倒置坐标轴），而OCR驱动的数据路径则确保数值的准确提取与对齐。为了解决视觉与数据信息间的冲突，论文引入了智能体摘要器，并采用两阶段优化协议进行训练：首先通过Oracle-Informed SFT进行推理知识蒸馏，再利用Deception-Aware GRPO进行对抗性对齐，以惩罚视觉陷阱并强化逻辑一致性。

主要结论是，在两个基准测试上的评估表明，ChartCynics取得了74.43%和64.55%的准确率，相比其Qwen3-VL-8B骨干模型实现了约29%的绝对性能提升，甚至超越了最先进的专有模型。论文的核心贡献在于证明，专门设计的智能体工作流可以使较小的开源模型获得卓越的鲁棒性，从而为可信的图表解读奠定了新的基础。
