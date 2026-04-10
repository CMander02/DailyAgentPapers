---
title: "When to Trust Tools? Adaptive Tool Trust Calibration For Tool-Integrated Math Reasoning"
authors:
  - "Ruotao Xu"
  - "Yixin Ji"
  - "Yu Luo"
  - "Jinpeng Li"
  - "Dong Li"
  - "Peifeng Li"
  - "Juntao Li"
  - "Min Zhang"
date: "2026-04-09"
arxiv_id: "2604.08281"
arxiv_url: "https://arxiv.org/abs/2604.08281"
pdf_url: "https://arxiv.org/pdf/2604.08281v1"
categories:
  - "cs.CL"
tags:
  - "Tool-Integrated Reasoning"
  - "Tool Trust Calibration"
  - "Math Reasoning"
  - "Code Generation"
  - "Confidence Estimation"
  - "Reasoning Agents"
relevance_score: 8.5
---

# When to Trust Tools? Adaptive Tool Trust Calibration For Tool-Integrated Math Reasoning

## 原始摘要

Large reasoning models (LRMs) have achieved strong performance enhancement through scaling test time computation, but due to the inherent limitations of the underlying language models, they still have shortcomings in tasks that require precise computation and extensive knowledge reserves. Tool-Integrated Reasoning (TIR) has emerged as a promising paradigm that incorporates tool call and execution within the reasoning trajectory. Although recent works have released some powerful open-source TIR models, our analysis reveals that these models still suffer from critical deficiencies. We find that when the reasoning of the model conflicts with the tool results, the model tends to believe in its own reasoning. And there are cases where the tool results are correct but are ignored by the model, resulting in incorrect answers, which we define as "Tool Ignored''. This indicates that the model does not know when to trust or ignore the tool. To overcome these limitations, We introduce Adaptive Tool Trust Calibration (ATTC), a novel framework that guides the model to adaptively choose to trust or ignore the tool results based on the confidence score of generated code blocks. The experimental results from various open-source TIR models of different sizes and across multiple datasets demonstrate that ATTC effectively reduces the "Tool Ignored" issue, resulting in a performance increase of 4.1% to 7.5%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决工具集成推理（TIR）模型中存在的一个关键缺陷：模型在面对自身推理与外部工具（如代码执行器）结果冲突时，缺乏自适应判断能力，倾向于盲目相信自身推理而忽略正确的工具结果，导致错误答案，即“工具被忽略”问题。

研究背景是，大型推理模型通过扩展测试时计算在复杂推理任务上取得了显著进展，但其在精确计算和广泛知识需求方面仍有局限。为此，工具集成推理范式应运而生，通过将工具调用和执行嵌入推理轨迹来弥补模型不足。现有方法包括基于提示工程的早期工作、依赖监督微调（SFT）的方法以及应用强化学习的近期研究。然而，这些方法存在不足：提示工程依赖精心设计的提示，可扩展性差；SFT方法使模型受限于训练数据中的工具使用模式，缺乏适应性；强化学习方法虽提升了灵活性，但现有开源TIR模型仍普遍面临一个核心挑战——无法在自身推理与工具结果之间实现有效权衡。当两者冲突时，模型往往错误地选择忽略工具，显示出其不知道何时该信任或忽略工具。

因此，本文要解决的核心问题是如何让TIR模型能够自适应地校准对工具的信任，即根据情境（特别是模型生成代码块的可信度）动态决定是信任工具结果还是重新思考，从而减少“工具被忽略”现象，提升推理性能和鲁棒性。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕工具集成推理（TIR）这一范式展开，可分为方法演进和训练策略两大类。

在方法演进方面，早期研究主要依赖**提示工程**来引导大语言模型调用工具，但这种方法可扩展性和泛化性有限。后续工作转向**监督微调（SFT）**，通过在包含工具调用演示的数据集上训练模型（如Qwen2.5-Math-Instruct、ReAct、MathCoder），使其能够主动调用并集成工具结果。然而，SFT方法使模型严格遵循训练数据中的工具使用模式，缺乏根据任务难度自适应调整策略的能力。

为克服SFT的局限，近期研究聚焦于应用**强化学习（RL）**。例如，ReTool提出了自动化RL范式以处理多轮代码执行；ToRL允许模型通过无限制探索来发现最优工具使用策略；VerlTool和Effective CIR则分别引入了模块化框架和增强的训练策略来优化多轮交互与平衡探索稳定性；SimpleTIR通过过滤无效轨迹来稳定训练过程。

本文提出的自适应工具信任校准（ATTC）框架与上述工作密切相关，但核心区别在于：现有TIR模型（无论是基于SFT还是RL）普遍存在“工具忽略”问题，即当模型自身推理与工具结果冲突时，倾向于盲目信任自身。ATTC并未改变模型的训练范式，而是引入了一个新颖的**决策校准机制**，指导模型根据生成代码块的置信度分数，自适应地选择信任或忽略工具结果，从而直接针对现有模型在工具信任校准上的缺陷进行改进。

### Q3: 论文如何解决这个问题？

论文通过提出自适应工具信任校准（ATTC）框架来解决工具集成推理（TIR）模型中存在的“工具忽略”问题，即当模型自身推理与工具结果冲突时，倾向于相信自身推理而忽略正确工具结果，导致错误答案。ATTC的核心思想是利用模型生成代码块时的置信度分数，自适应地指导模型选择信任或忽略工具结果。

整体框架包含三个主要模块：工具调用监控器、置信度评估器和工具信任重校准器。首先，工具调用监控器基于规则实时监控模型的生成流，当检测到特定的工具调用标记（如“```output”或“<tool_result>”）时，暂停生成过程，并提取模型生成的代码块（通常包含在“```python”或“<python>”等分隔符内）。其次，置信度评估器负责计算代码块的置信度分数。它定义每个代码令牌的置信度为模型分配给该令牌的最大预测概率，然后通过几何平均所有令牌的置信度来计算整个代码块的总体置信度分数。使用几何平均是因为其对低概率值敏感，能有效反映低置信度令牌的影响，同时具有尺度不变性，避免序列长度或概率尺度变化带来的偏差。最后，工具信任重校准器将计算出的置信度分数与经验阈值λ进行比较：若置信度≥λ，则注入信任控制信号，明确指导模型接受工具输出并基于该结果给出答案；若置信度<λ，则注入重新思考控制信号，指导模型利用工具结果批判性反思先前的推理和生成的代码，从而重新考虑整个推断过程。

ATTC的创新点在于将模型对代码生成的隐式置信度认知转化为显式的、可操作的控制信号，从而在无需修改模型内部参数的情况下，动态调整对工具结果的信任决策。该方法通过轻量级的监控和评估机制，有效减少了“工具忽略”现象，在多个不同规模和架构的开源TIR模型及数学基准测试上实现了4.1%至7.5%的性能提升。

### Q4: 论文做了哪些实验？

论文在多个数学推理基准上进行了实验，评估了所提ATTC框架的有效性、效率和鲁棒性。实验设置方面，研究使用了vLLM框架，解码策略（温度、top-p）与各对比模型原论文最优设置对齐，并报告了3个随机种子的平均结果。

使用的数据集包括五个数学基准：MATH-500、Minerva、Olympiad、AIME24和AMC23，并额外在AIME25上测试了泛化能力。主要评估指标是准确率（Pass@1），同时使用平均生成令牌数（Token Count）和平均推理时间（Time Use）作为效率指标。

对比方法为一系列基于强化学习训练的开源工具集成推理（TIR）模型，包括基于Qwen2.5-7B的ToRL-7B、VerlTool-7B、EffectiveTIR-7B、SimpleTIR-7B，基于Qwen2.5-32B的ReTool-32B、SimpleTIR-32B，以及基于Qwen3-4B的DemyAgent-4B等。

主要结果显示，ATTC在所有模型规模和数据集上均一致提升了性能。在五个数据集上，ATTC将模型准确率平均提升了4.1%至7.5%。在AIME25上，ATTC显著提高了Pass@1和Pass@32的分数，例如EffectiveTIR-7B的Pass@1从30.0%提升至36.7%。效率方面，ATTC平均降低了5%至11%的令牌消耗和6%至14%的推理时间。关键分析表明，ATTC显著缓解了“工具忽略”问题（相关比例下降），且对置信度阈值λ在0.93至0.98范围内表现鲁棒。此外，实验验证了代码块置信度分数与前置推理充分性（由PRM评分衡量）之间存在线性关系，且ATTC并未大幅减少工具调用总次数，而是专注于消除不必要调用。

### Q5: 有什么可以进一步探索的点？

该论文提出的ATTC框架虽有效，但存在明显局限，为未来研究提供了多个探索方向。首先，实验仅覆盖小于32B的开源模型，未来需验证其在更大规模或闭源模型上的泛化能力，并探究模型规模与工具信任校准间的关联。其次，当前方法仅针对代码执行器工具，未来可扩展至搜索引擎、数据库查询等多工具场景，研究跨工具类型的自适应信任机制。再者，本文仅在推理阶段进行优化，未来可从训练阶段入手，通过设计针对性损失函数或偏好对齐方法，从根本上提升模型对工具结果的评估与整合能力。此外，论文未深入探讨模型自信度分数的可靠性问题，未来可结合不确定性量化技术，提升置信度评估的鲁棒性。最后，可探索更复杂的工具交互模式，如多轮工具调用与结果融合，以应对更复杂的数学推理任务。

### Q6: 总结一下论文的主要内容

该论文针对工具集成推理模型中存在的“工具信任”问题展开研究。现有开源TIR模型在自身推理与外部工具结果冲突时，倾向于相信自身推理，导致即使工具结果正确也可能被忽略，作者将此定义为“工具忽略”问题。为解决此问题，论文提出了自适应工具信任校准框架ATTC。该方法的核心是引导模型根据生成的代码块的置信度分数，自适应地选择信任或忽略工具结果。实验表明，在不同规模和多个数据集上的TIR模型中，ATTC能有效减少“工具忽略”现象，将模型性能提升4.1%至7.5%。这项工作的主要贡献在于揭示了TIR模型的关键缺陷，并提出了一个简单有效的校准框架来提升模型对工具结果的合理利用能力，从而增强工具集成推理的可靠性。
