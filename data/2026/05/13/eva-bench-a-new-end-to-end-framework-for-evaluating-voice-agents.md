---
title: "EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents"
authors:
  - "Tara Bogavelli"
  - "Gabrielle Gauthier Melançon"
  - "Katrina Stankiewicz"
  - "Oluwanifemi Bamgbose"
  - "Fanny Riols"
  - "Hoang H. Nguyen"
  - "Raghav Mehndiratta"
  - "Lindsay Devon Brin"
  - "Joseph Marinier"
  - "Hari Subramani"
  - "Anil Madamala"
  - "Sridhar Krishna Nemala"
  - "Srinivas Sunkara"
date: "2026-05-13"
arxiv_id: "2605.13841"
arxiv_url: "https://arxiv.org/abs/2605.13841"
pdf_url: "https://arxiv.org/pdf/2605.13841v1"
categories:
  - "cs.SD"
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "voice agent"
  - "evaluation benchmark"
  - "task completion"
  - "spoken conversation"
  - "multi-turn dialogue"
  - "audio robustness"
  - "enterprise application"
relevance_score: 7.5
---

# EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents

## 原始摘要

Voice agents, artificial intelligence systems that conduct spoken conversations to complete tasks, are increasingly deployed across enterprise applications. However, no existing benchmark jointly addresses two core evaluation challenges: generating realistic simulated conversations, and measuring quality across the full scope of voice-specific failure modes. We present EVA-Bench, an end-to-end evaluation framework that addresses both. On the simulation side, EVA-Bench orchestrates bot-to-bot audio conversations over dynamic multi-turn dialogues, with automatic simulation validation that detects user simulator error and appropriately regenerates conversations before scoring. On the measurement side, EVA-Bench introduces two composite metrics: EVA-A (Accuracy), capturing task completion, faithfulness, and audio-level speech fidelity; and EVA-X (Experience), capturing conversation progression, spoken conciseness, and turn-taking timing. Both metrics apply to different agent architectures, enabling direct cross-architecture comparison. EVA-Bench includes 213 scenarios across three enterprise domains, a controlled perturbation suite for accent and noise robustness, and pass@1, pass@k, pass^k measurements that distinguish peak from reliable capability. Across 12 systems spanning all three architectures, we find: (1) no system simultaneously exceeds 0.5 on both EVA-A pass@1 and EVA-X pass@1; (2) peak and reliable performance diverge substantially (median pass@k - pass^k gap of 0.44 on EVA-A); and (3) accent and noise perturbations expose substantial robustness gaps, with effects varying across architectures, systems, and metrics (mean up to 0.314). We release the full framework, evaluation suite, and benchmark data under an open-source license.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

在研究背景上，语音代理（Voice Agent）作为通过语音交互完成任务的AI系统，已广泛应用于企业场景。然而，现有评估基准面临两大核心挑战：一是如何生成真实可信的模拟对话（需支持多轮交互、工具调用、真实音频及自然人类行为）；二是如何全面衡量语音特有的失败模式（如语音保真度、话轮转换时机、实体错误等超越文本维度的质量问题）。

现有方法存在明显不足：大多数基准仅支持文本或单一架构评估，如τ-Voice、CAVA等缺乏模拟器验证或指标不全面；而像FDB-v3依赖真实人类音频却无法覆盖多轮交互。更重要的是，尚无基准能同时处理语音代理的两大架构类型（级联系统与音频原生系统）的统一评估。

本文核心问题是：构建一个端到端的评估框架EVA-Bench，以同时解决模拟对话的生成与质量测量问题。该框架通过机器人间实时音频对话、自动验证机制确保模拟一致性，并引入EVA-A（准确度，涵盖任务完成、忠诚度、语音保真度）和EVA-X（体验度，涵盖对话进展、简洁性、话轮时机）两个复合指标，实现对不同架构语音代理的公平比较与全面评估。

### Q2: 有哪些相关研究？

现有语音代理评估工作主要分为两个方向。在对话仿真方面，FullDuplex-Bench系列评估脚本化对话但缺乏任务完成与工具使用，VoiceAgentBench依赖静态TTS查询且无交互，FDB-v3虽然改进为真实录音但仍限于单轮。最接近的T-Voice和FDB-v2实现了实时代理间多轮仿真，但缺乏仿真器行为验证，且T-Voice中口音变化与用户角色混叠。本文创新性地引入了带自动质量验证的实时多轮仿真器，并设计了可控扰动套件以隔离口音与噪声影响。在质量评估方面，VoiceAgentBench仅关注工具选择准确性，T-Voice补充了轮次指标但忽略对话忠实性，FDB-v3引入转录级响应质量但未评估策略忠实性或音频级实体准确性。本文填补了这一空白，提出了涵盖任务完成度、忠实性、音频保真度的EVA-A指标，以及包含对话进展、简洁性和轮次时序的EVA-X指标，实现了对语音代理质量的全面评估。

### Q3: 论文如何解决这个问题？

EVA-Bench通过构建一个端到端的自动化评估框架来解决语音智能体的两大核心挑战：生成逼真的模拟对话和全面衡量语音特有的失败模式。

核心方法基于机器人间（bot-to-bot）的音频对话。整体框架包含两大阶段：模拟阶段和质量测量阶段。在模拟阶段，系统并行运行每个场景的对话会话：一个用户模拟器（基于高质量级联管道）根据特定场景的目标、人设和TTS语音，通过WebSocket与待测语音智能体进行多轮音频交互。同时，工具执行器处理智能体的所有工具调用。对话完成后，会经过自动化的模拟验证，通过LLM-as-Judge检测用户模拟器是否偏离目标或语音保真度不足，失败则会自动重新生成，这确保后续评分反映的是智能体行为而非模拟器伪影。

在质量测量阶段，EVA-Bench引入了两个复合指标：**EVA-A（准确性）** 和**EVA-X（体验）**。EVA-A包含三个维度：任务完成（数据库状态哈希对比）、忠实度（LLM判断智能体行为是否基于指令和上下文）以及语音保真度（LALM判断智能体输出语音是否准确复现了文本中的高风险实体）。EVA-X包含三个维度：对话进展（LLM判断回答是否高效推进任务）、简洁性（LLM判断回答是否适合口语）以及轮次计时（基于时间戳，智能体不能打断用户或过度沉默，工具调用有更宽松阈值）。这些指标被聚合，并通过设定的阈值转化为二进制通过/失败，再计算出`pass@1`（平均性能）、`pass@k`（峰值性能，即至少一次通过的场景比例）和`pass^k`（可靠性，即场景中所有k次尝试都通过的概率），从而区分智能体的峰值能力和稳定能力。

创新点在于：将端到端音频交互与严格的模拟验证结合，并设计了覆盖准确性、体验及诊断指标（如逐实体转录准确率）的多层次评估体系，可直接比较不同架构（级联与音频原生）的智能体。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估，涵盖12个系统（7个级联、2个混合、3个S2S）。实验设置包括清洁条件（所有213个场景，每场景k=5次）和扰动条件（法语口音、咖啡馆噪音、二者组合，使用90个场景子集，k=3次）。评估使用EVA-A（准确率）和EVA-X（体验）两大复合指标及pass@1、pass@k、pass^k测量。主要结果：(1) 无系统能同时在EVA-A pass@1和EVA-X pass@1超过0.5；(2) pass@k与pass^k间存在显著差距（EVA-A上中位数0.44），表明峰值与可靠性能差异大；(3) 口音和噪音扰动暴露了大型鲁棒性差距（最高均值0.314），效果因架构、系统和指标而异。实验还验证了评估可靠性：人工-评判员一致性达到实际天花板（Cohen's κ在0.777-0.845之间），方差分解显示评判员随机性影响最小，试验随机性为主导方差来源。

### Q5: 有什么可以进一步探索的点？

EVA-Bench在评估框架上仍有若干可拓展之处。首先，当前场景局限于三个企业域，未来应扩展至开放域、多语言及跨文化对话场景，以检验代理的泛化能力。其次，仅采用模拟的bot-to-bot对话可能无法完全捕捉真实人类用户的行为多样性（如口误、情感波动或非理性决策），未来可引入人类-in-the-loop或混合仿真以提升生态效度。再者，复合指标EVA-A与EVA-X侧重任务和体验，但缺乏对代理长期交互记忆、可解释性、伦理安全及多模态感知（如音频+视觉上下文）的量化。此外，扰动测试仅考察口音与噪声，可补充处理竞争性语音、重叠说话、环境回音等更复杂的声学挑战。最后，当前系统在pass@1与pass^k之间表现差异显著，说明需要更细粒度的置信度校准和自适应重试机制。基于LLM的根因分析或许能帮助系统理解失败模式，并动态调整对话策略。

### Q6: 总结一下论文的主要内容

EVA-Bench是一个端到端的语音智能体评估框架，旨在解决现有基准无法同时生成真实模拟对话和全面测量语音特有故障模式的问题。该框架通过自动化的机器人-机器人音频对话模拟，并引入验证门控质量控件确保模拟一致性，同时支持口音和噪声扰动。在评估方面，EVA-Bench提出了两个复合指标：EVA-A（准确性）衡量任务完成度、忠实度和语音保真度；EVA-X（体验）衡量对话进展、口语简洁性和轮换时机。该基准涵盖213个来自三个企业领域的场景。对12个系统的评估发现：没有任何系统能在EVA-A和EVA-X的pass@1上同时超过0.5；峰值性能与可靠性能差距较大（EVA-A中位数pass@1与pass^k的差为0.44）；口音和噪声扰动暴露了显著的鲁棒性差距。这项工作的核心意义在于为异构架构的语音智能体提供了首个公平、全面的评估平台。
