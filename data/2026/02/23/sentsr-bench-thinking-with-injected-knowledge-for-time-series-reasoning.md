---
title: "SenTSR-Bench: Thinking with Injected Knowledge for Time-Series Reasoning"
authors:
  - "Zelin He"
  - "Boran Han"
  - "Xiyuan Zhang"
  - "Shuai Zhang"
  - "Haotian Lin"
  - "Qi Zhu"
  - "Haoyang Fang"
  - "Danielle C. Maddix"
  - "Abdul Fatir Ansari"
  - "Akash Chandrayan"
  - "Abhinav Pradhan"
  - "Bernie Wang"
  - "Matthew Reimherr"
date: "2026-02-23"
arxiv_id: "2602.19455"
arxiv_url: "https://arxiv.org/abs/2602.19455"
pdf_url: "https://arxiv.org/pdf/2602.19455v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
  - "stat.ML"
tags:
  - "Agent 推理"
  - "知识注入"
  - "强化学习"
  - "时间序列分析"
  - "基准评测"
  - "工具使用"
relevance_score: 7.5
---

# SenTSR-Bench: Thinking with Injected Knowledge for Time-Series Reasoning

## 原始摘要

Time-series diagnostic reasoning is essential for many applications, yet existing solutions face a persistent gap: general reasoning large language models (GRLMs) possess strong reasoning skills but lack the domain-specific knowledge to understand complex time-series patterns. Conversely, fine-tuned time-series LLMs (TSLMs) understand these patterns but lack the capacity to generalize reasoning for more complicated questions. To bridge this gap, we propose a hybrid knowledge-injection framework that injects TSLM-generated insights directly into GRLM's reasoning trace, thereby achieving strong time-series reasoning with in-domain knowledge. As collecting data for knowledge injection fine-tuning is costly, we further leverage a reinforcement learning-based approach with verifiable rewards (RLVR) to elicit knowledge-rich traces without human supervision, then transfer such an in-domain thinking trace into GRLM for efficient knowledge injection. We further release SenTSR-Bench, a multivariate time-series-based diagnostic reasoning benchmark collected from real-world industrial operations. Across SenTSR-Bench and other public datasets, our method consistently surpasses TSLMs by 9.1%-26.1% and GRLMs by 7.9%-22.4%, delivering robust, context-aware time-series diagnostic insights.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决时间序列诊断推理任务中，通用大语言模型与领域专用模型各自存在的局限性问题。研究背景是，在工业监控等实际应用中，从传感器产生的时间序列数据中进行诊断推理（如故障根因分析）至关重要。然而，现有方法存在明显不足：一方面，通用推理大语言模型具备强大的逻辑推理能力，但缺乏对复杂时间序列模式的领域专业知识，导致其无法正确解读数据模式，推理轨迹出现偏差；另一方面，经过微调的时间序列专用语言模型虽能理解领域内的时间序列模式，但其推理深度和泛化能力有限，容易过拟合到狭窄的任务模板上，难以处理分布外或更复杂的推理问题。因此，这两种模型单独使用时，都无法提供既准确又具可操作性的诊断见解。

本文要解决的核心问题是：如何有效结合通用模型的强推理能力与专用模型的领域知识，以提升时间序列诊断推理的准确性和鲁棒性。为此，论文提出了一种混合知识注入框架，将时间序列专用模型生成的领域知识洞察直接注入到通用模型的推理轨迹中，从而在无需更新模型权重的情况下，引导其进行基于领域知识的推理。此外，针对为知识注入微调收集数据成本高昂的挑战，论文进一步提出了一种基于强化学习与可验证奖励的方法，以无监督的方式激发专用模型产生知识丰富的“思维轨迹”，并将其转移给通用模型，实现高效的知识注入。为了推动该领域研究，论文还发布了首个基于真实工业多变量时间序列的诊断推理基准SenTSR-Bench。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：时间序列推理方法、推理过程干预方法以及时间序列基准评测。

在**时间序列推理方法**方面，相关工作主要分为两类。一类是基于提示的结构化推理方法，这类工作通过设计提示词引导大模型对时序数据进行结构化推理，但其缺陷是缺乏领域先验知识，难以捕捉关键的诊断模式。另一类是专门针对时间序列文本对进行后训练的专家模型，这类模型虽能理解领域模式，但容易过拟合于领域内数据，泛化能力较弱。本文提出的知识注入框架旨在弥合这两类方法的不足，将通用大模型的推理能力与领域专家模型的洞察相结合。

在**推理过程干预方法**方面，已有研究探索通过修改推理轨迹或内部推理过程来提升模型的忠实性、安全性和指令遵循能力，或通过控制推理轨迹长度来平衡准确性与效率。本文工作与这些研究的区别在于，我们明确地将来自专业模型（TSLM）的领域知识注入到通用推理模型（GRLM）中，并特别专注于时间序列数据的诊断推理任务。

此外，在**时间序列基准评测**方面，论文附录提及了关于时间序列预测和推理的基准研究。本文也为此领域贡献了SenTSR-Bench，这是一个基于真实工业运营的多变量时间序列诊断推理基准。

### Q3: 论文如何解决这个问题？

论文通过提出一个混合知识注入框架来解决通用推理大模型（GRLM）缺乏领域知识，而领域微调时序大模型（TSLM）缺乏复杂推理能力之间的鸿沟。其核心方法是：在GRLM的推理轨迹中，直接注入由TSLM生成的领域知识，从而结合两者的优势。

整体框架包含三个主要模块：1) **多模态输入处理模块**：将多元时间序列数据通过图像渲染、JSON结构化或专用分词器转换为语言模型可处理的token序列。2) **推理模型定义**：模型被定义为生成内部推理轨迹和最终答案的两阶段过程。具体区分了通用推理模型π^G和时序语言模型π^T。3) **知识注入与推理模块**：这是框架的核心。首先，通过查询塑造函数，基于GRLM当前的推理状态和原始问题，生成一个面向知识注入的查询。然后，调用TSLM基于时间序列数据和该查询生成领域知识片段。接着，通过注入函数，将TSLM生成的知识整合到GRLM的推理轨迹前缀中。最后，GRLM基于更新后的、富含知识的推理轨迹继续生成，并得出最终答案。

在技术实现上，论文提出了几种具体的注入范式。**早期注入**是默认且最有效的方法，即在推理开始后立即注入TSLM生成的知识片段和一个反思触发词，引导GRLM进行深入推理。此外，框架也支持**中期注入**（在GRLM推理置信度低时插入知识进行纠正）和**后期注入**（在最终答案前由TSLM批判整个推理轨迹）。

关键的创新点在于，为了低成本地使TSLM生成适用于注入的、高质量的分析性知识（而非直接答案），论文进一步提出了**基于强化学习的可验证奖励方法**。由于缺乏人工标注的中间推理轨迹，该方法使用**组相对策略优化**，奖励函数结合了**格式奖励**（鼓励输出符合“思考-答案”的结构）和**硬奖励**（鼓励最终答案正确）。通过这种方式，无需监督数据即可训练TSLM首先生成分析性思考轨迹，然后将此轨迹作为知识源注入GRLM，实现了“思维迁移”，有效对齐了TSLM的训练目标与它在注入框架中的角色。整个方案通过两阶段实现：第一阶段用RLVR训练TSLM生成思考轨迹；第二阶段在测试时，将TSLM的思考轨迹注入GRLM以指导其推理。

### Q4: 论文做了哪些实验？

实验在三个数据集上进行评估：新提出的真实世界多元时间序列诊断推理基准SenTSR-Bench（包含“发生了什么”、“如何发生”和“建议修复”三个渐进任务），以及两个公共基准TSEvol（涵盖归纳、演绎和因果推理）和TS&Language Benchmark（MCQ2数据集，涉及文本上下文下的成对时间序列关系查询）。实验设置方面，通用推理模型（GRLM）测试了开源模型DeepSeekR1-Distilled-Qwen-32B、Qwen3-32B以及闭源模型Claude3.7（分别以视觉和文本形式编码时间序列）；微调的时间序列大模型（TSLM）主要使用Qwen2.5-VL-3B进行监督微调（SFT）和强化学习（RL）训练，并使用了ChatTS-14B进行注入策略探索。评估时，生成式问答任务使用RAGAS评估，可验证任务报告准确率，所有结果为三次独立运行的平均值。

对比方法包括：独立的TSLM（SFT和RL变体）、独立的GRLM（零样本和少样本提示），以及论文提出的混合知识注入框架（分为SFT-Injection和RL-Injection）。此外，还比较了不同的知识注入策略（早期、中期、晚期注入）以及知识注入与基于提示的知识提供方法。

主要结果显示，提出的知识注入方法在所有基准上一致超越了基线。在SenTSR-Bench上，相对于专门的TSLM，性能提升在15.5%到26.1%之间；相对于通用GRLM，提升在7.3%到22.4%之间。在公共基准上，相对于TSLM提升5.2%到10.4%，相对于GRLM提升2.7%到10.4%。关键数据指标包括：在SenTSR-Bench上，使用Claude3.7-Vision和RL-Injection的“总体”得分达到0.695±0.012；在TSEvol和TS&Language Benchmark上，使用DeepSeekR1-Distilled-Qwen-32B和RL-Injection的“总体”得分达到0.561±0.011。实验还发现，基于RL的注入比基于SFT的注入带来更大的增益，并且早期注入策略通常表现最佳。与将TSLM输出作为外部提示的替代方法相比，知识注入因其将领域知识直接整合到推理轨迹中而 consistently 表现更优。

### Q5: 有什么可以进一步探索的点？

该论文提出的混合知识注入框架虽有效，但仍有局限。首先，其依赖强化学习生成“分析优先”的思考轨迹，但奖励函数的可验证性（verifiable rewards）在更复杂、定义模糊的工业场景中可能难以保证，可能限制方法的泛化能力。其次，框架假设时间序列专家模型（TSLM）能提供准确的知识片段，若TSLM本身存在偏差或错误，注入的知识会污染通用大模型（GRLM）的推理链。

未来研究方向可包括：1）探索更鲁棒的知识验证机制，例如引入多专家模型投票或不确定性量化，以减少错误知识的注入；2）将框架扩展至动态知识注入，使GRLM能在推理过程中实时查询TSLM或外部知识库，而非依赖静态的事先生成轨迹；3）研究跨模态时间序列推理，如结合文本报告、图像传感器数据，提升诊断的上下文感知能力。此外，基准测试SenTSR-Bench可进一步增加对抗性样本或长时序依赖任务，以评估方法的稳健性和时序因果推理深度。

### Q6: 总结一下论文的主要内容

该论文针对时间序列诊断推理任务中通用大语言模型（GRLM）缺乏领域知识，而专用时间序列模型（TSLM）泛化推理能力不足的问题，提出了一种混合知识注入框架。其核心贡献在于：1）定义了结合领域知识与通用推理能力的时间序列诊断问题；2）提出了一种将TSLM生成的领域知识洞察直接注入GRLM推理链的方法，以增强其上下文感知能力；3）为降低人工标注成本，进一步引入基于可验证奖励的强化学习（RLVR）方法，自动生成富含知识的推理轨迹，并将其高效迁移至GRLM。实验表明，该方法在提出的真实工业多变量时间序列基准SenTSR-Bench及其他公开数据集上，性能显著超越基线TSLM（9.1%-26.1%）和GRLM（7.9%-22.4%）。论文的意义在于通过知识注入有效弥合了领域专业性与通用推理能力之间的鸿沟，为复杂时间序列分析提供了鲁棒且可解释的解决方案。
