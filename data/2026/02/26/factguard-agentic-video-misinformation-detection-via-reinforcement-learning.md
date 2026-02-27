---
title: "FactGuard: Agentic Video Misinformation Detection via Reinforcement Learning"
authors:
  - "Zehao Li"
  - "Hongwei Yu"
  - "Hao Jiang"
  - "Qiang Sheng"
  - "Yilong Xu"
  - "Baolong Bi"
  - "Yang Li"
  - "Zhenlong Yuan"
  - "Yujun Cai"
  - "Zhaoqi Wang"
date: "2026-02-26"
arxiv_id: "2602.22963"
arxiv_url: "https://arxiv.org/abs/2602.22963"
pdf_url: "https://arxiv.org/pdf/2602.22963v1"
categories:
  - "cs.AI"
tags:
  - "Agentic Framework"
  - "Video Misinformation Detection"
  - "Multimodal LLM (MLLM)"
  - "Reinforcement Learning"
  - "Tool Use"
  - "Iterative Reasoning"
  - "Decision Making"
  - "Agent Training"
relevance_score: 8.5
---

# FactGuard: Agentic Video Misinformation Detection via Reinforcement Learning

## 原始摘要

Multimodal large language models (MLLMs) have substantially advanced video misinformation detection through unified multimodal reasoning, but they often rely on fixed-depth inference and place excessive trust in internally generated assumptions, particularly in scenarios where critical evidence is sparse, fragmented, or requires external verification. To address these limitations, we propose FactGuard, an agentic framework for video misinformation detection that formulates verification as an iterative reasoning process built upon MLLMs. FactGuard explicitly assesses task ambiguity and selectively invokes external tools to acquire critical evidence, enabling progressive refinement of reasoning trajectories. To further strengthen this capability, we introduce a two-stage training strategy that combines domain-specific agentic supervised fine-tuning with decision-aware reinforcement learning to optimize tool usage and calibrate risk-sensitive decision making. Extensive experiments on FakeSV, FakeTT, and FakeVV demonstrate FactGuard's state-of-the-art performance and validate its excellent robustness and generalization capacity.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视频虚假信息检测中现有方法存在的关键不足。研究背景是，随着TikTok等在线内容平台的快速发展，视频已成为虚假信息传播的主要且极具挑战性的媒介，其丰富的时序动态和多模态复杂性使得事后人工核查难以应对，亟需准确、及时的自动化检测方法。现有方法主要依赖特定任务的判别模型，缺乏开放场景下处理多样化验证需求所需的通用理解和推理能力。尽管多模态大语言模型（MLLMs）的进步推动了基于推理的检测方法，但它们通常采用固定深度的单次推理范式，缺乏明确的不确定性感知和针对性证据获取机制。在证据稀疏、碎片化或需要外部验证的模糊场景中，这些模型往往过度依赖内部生成的假设，导致跨模态幻觉（例如捏造或错误归因视觉/文本证据），从而产生自信但错误的判断。

因此，本文要解决的核心问题是：如何构建一个能够像智能体（Agent）一样进行不确定性感知、迭代推理并选择性调用外部工具以获取关键证据的视频虚假信息检测框架，从而克服现有方法在证据利用和决策可靠性上的局限。具体而言，论文提出的FactGuard框架将检测任务构建为一个基于强化学习的智能体迭代验证过程，旨在使系统能够（1）识别何时信息不足，（2）选择性地获取外部证据，以及（3）基于新观察迭代优化其判断，最终实现更可靠、可解释的检测。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：视频虚假信息检测方法、多模态大模型（MLLMs）推理技术，以及工具增强与智能体（Agentic）范式。

在**视频虚假信息检测方法**方面，早期研究集中于图文跨模态一致性建模，近期则转向视频领域，通过融合视觉、音频、文本等多模态信号，或结合情感、韵律线索及社交上下文进行检测。这些方法多为基于固定特征融合的单次推断，缺乏对稀疏、碎片化证据的主动获取和迭代推理能力。

在**多模态大模型推理技术**方面，GPT-4V等模型提升了跨模态统一理解与推理能力。后续研究通过思维链提示、强化学习后训练等方式优化推理过程，Fact-R1等工作将大模型与领域微调、强化学习结合用于虚假信息检测。然而，这些方法通常依赖模型内部假设，未系统集成外部工具进行证据验证。

在**工具增强与智能体范式**方面，已有研究探索为多模态模型引入外部工具以获取辅助证据，并通过监督或强化学习优化工具调用。但这些工作在视频虚假信息检测中应用有限，且工具使用多限于被动补充，而非基于任务模糊性评估的主动、迭代式证据收集与决策校准。

本文提出的FactGuard与上述工作的核心区别在于：它将检测构建为一个基于强化学习的智能体迭代验证过程，通过显式评估任务模糊性、选择性调用外部工具获取关键证据，并采用决策感知的强化学习优化工具使用与风险敏感决策，实现了从“单次静态推理”到“动态主动验证”的范式转变。

### Q3: 论文如何解决这个问题？

论文通过提出FactGuard这一智能体框架来解决视频虚假信息检测问题，其核心是将验证过程构建为一个基于多模态大语言模型的迭代推理决策流程。整体框架采用两阶段推理设计：首先，智能体策略对输入的多模态内容进行初始思维链推理，评估任务的模糊性和难度，并决定是否调用外部工具获取关键证据；若调用工具并获得反馈，则进入第二阶段，结合原始输入和工具提供的证据进行精细化推理，生成最终判断。这种设计使模型能够显式处理不确定性，并在证据稀疏时主动寻求外部验证。

主要模块包括证据引导的行动模块和两阶段训练策略。行动模块包含两个关键工具：FactProbe用于外部知识检索，通过结构化查询从网络来源获取事实证据；ClipScout用于视频片段时序检测，通过选择性采样关键帧实现针对性视觉证据提取。这些工具仅在内部推理不足时被触发，避免了盲目调用。

创新点体现在三个方面：一是提出了智能体化的验证流程，将一次性分类任务转化为自我调节的决策过程；二是设计了两阶段训练策略，首先通过领域特定的智能体思维链监督微调，使模型学习多轮推理、工具选择意图和基于证据的反思；随后引入决策感知的强化学习，采用分组相对策略优化方法，通过结构化奖励函数优化工具使用和风险敏感决策。奖励函数综合考虑了决策准确性、工具使用效率和风险偏好，通过显式的风险塑造项来平衡精确率和召回率，并惩罚无效的工具调用。这种训练方式使模型在不确定性下校准验证策略，发展出以证据为导向的推理行为，从而在信息稀缺的真实场景中实现鲁棒的虚假信息检测。

### Q4: 论文做了哪些实验？

论文在三个基准数据集（FakeSV、FakeTT、FakeVV）上进行了广泛的实验，采用时间划分，使用最近15%的样本进行测试。实验设置基于Qwen2.5-VL-7B模型，采用两阶段训练策略：先进行领域特定的智能体监督微调（SFT），再进行基于GRPO的决策感知强化学习（RL）。训练在8张NVIDIA H100 GPU上进行，学习率为1e-6，最大提示长度和响应长度分别为16384和768个令牌，KL正则化系数为0.04。

对比方法包括三类基线：判别式模型（如BERT、TikTec、FANVM、SVFEND、FakingRec）、零样本MLLMs（如Gemini2-thinking、GPT-4o、GPT-o1-mini、Qwen2.5-VL、InternVL2.5、QVQ-72B、InternVL2.5-MPO、DeepSeek-R1）以及任务对齐推理模型（Fact-R1和FactGuard）。评估指标包括准确率（ACC）、精确率、召回率和F1分数。

主要结果显示，FactGuard在所有数据集上均取得了最先进的性能。例如，在FakeSV和FakeTT上，FactGuard的准确率分别达到79.3%和75.3%，F1分数分别为81.4%和75.2%，全面优于基线模型。与最强的判别式模型FakingRec和零样本MLLM GPT-4o相比，FactGuard在准确率和F1分数上均有显著提升。消融实验表明，移除SFT或RL会导致性能大幅下降（如FakeSV上移除RL后准确率从79.3%降至62.0%），而移除工具奖励或风险奖励也会导致适度但一致的性能下降。此外，成本敏感风险分析显示，通过调整错误成本比率（α:γ），FactGuard可以灵活权衡精确率和召回率（例如在FakeSV上，当比率为1:2时，精确率和召回率分别为80.8%和82.1%；当比率为2:1时，分别为83.2%和75.0%）。可解释性分析使用GPT-4o自动评估，证实FactGuard能生成更连贯、基于证据的推理链。

### Q5: 有什么可以进一步探索的点？

该论文提出的FactGuard框架在视频虚假信息检测方面取得了显著进展，但其仍存在一些局限性和值得深入探索的方向。首先，框架高度依赖外部工具（如搜索引擎、事实核查数据库）的质量和覆盖范围，若工具本身存在偏差或信息滞后，可能影响最终判断的可靠性。未来可研究如何动态评估和整合多个异构工具源，或构建更鲁棒的证据检索与验证模块。

其次，虽然引入了强化学习来优化工具调用和决策，但训练过程可能依赖于特定领域的数据和风险设置，其策略在跨领域、跨文化语境下的泛化能力有待验证。可探索元学习或自适应机制，使智能体能够根据新场景快速调整验证策略。

此外，当前框架主要处理视频与文本的多模态信息，对于深伪造视频、AI生成内容等日益复杂的虚假信息形式，可能需要融合更先进的视听分析技术（如声纹检测、帧级篡改识别）作为内部感知能力。最后，如何将此类检测系统应用于实时流媒体环境，并在效率与精度间取得平衡，也是实际部署中的重要挑战。

### Q6: 总结一下论文的主要内容

该论文提出了FactGuard，一个基于强化学习的智能体框架，用于视频虚假信息检测。核心问题是现有多模态大语言模型（MLLMs）在检测时依赖固定深度的推理，并过度信任内部生成的假设，在关键证据稀疏、碎片化或需外部验证的场景中表现受限。

FactGuard将验证过程重新定义为基于MLLMs的迭代推理任务。其方法核心是让智能体主动评估任务模糊性，并选择性调用外部工具（如网络搜索、事实核查库）来获取关键证据，从而逐步优化推理路径。为强化此能力，论文设计了一个两阶段训练策略：首先进行领域特定的智能体监督微调，然后采用决策感知的强化学习来优化工具使用并校准风险敏感决策。

主要实验在FakeSV、FakeTT和FakeVV三个数据集上进行，结果表明FactGuard取得了最先进的性能，并展现出优秀的鲁棒性和泛化能力。其核心贡献在于通过引入强化学习驱动的智能体框架，使虚假信息检测系统具备了动态、迭代且可外部验证的推理能力，显著提升了在复杂、证据不足场景下的检测可靠性。
