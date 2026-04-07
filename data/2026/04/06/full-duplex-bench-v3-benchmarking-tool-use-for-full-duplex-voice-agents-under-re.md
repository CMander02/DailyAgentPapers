---
title: "Full-Duplex-Bench-v3: Benchmarking Tool Use for Full-Duplex Voice Agents Under Real-World Disfluency"
authors:
  - "Guan-Ting Lin"
  - "Chen Chen"
  - "Zhehuai Chen"
  - "Hung-yi Lee"
date: "2026-04-06"
arxiv_id: "2604.04847"
arxiv_url: "https://arxiv.org/abs/2604.04847"
pdf_url: "https://arxiv.org/pdf/2604.04847v1"
categories:
  - "eess.AS"
  - "cs.CL"
tags:
  - "语音智能体"
  - "工具使用"
  - "基准评测"
  - "实时交互"
  - "多步推理"
  - "真实世界评估"
  - "口语对话系统"
relevance_score: 7.5
---

# Full-Duplex-Bench-v3: Benchmarking Tool Use for Full-Duplex Voice Agents Under Real-World Disfluency

## 原始摘要

We introduce Full-Duplex-Bench-v3 (FDB-v3), a benchmark for evaluating spoken language models under naturalistic speech conditions and multi-step tool use. Unlike prior work, our dataset consists entirely of real human audio annotated for five disfluency categories, paired with scenarios requiring chained API calls across four task domains. We evaluate six model configurations -- GPT-Realtime, Gemini Live 2.5, Gemini Live 3.1, Grok, Ultravox v0.7, and a traditional Cascaded pipeline (Whisper$\rightarrow$GPT-4o$\rightarrow$TTS) -- across accuracy, latency, and turn-taking dimensions. GPT-Realtime leads on Pass@1 (0.600) and interruption avoidance (13.5\%); Gemini Live 3.1 achieves the fastest latency (4.25~s) but the lowest turn-take rate (78.0\%); and the Cascaded baseline, despite a perfect turn-take rate, incurs the highest latency (10.12~s). Across all systems, self-correction handling and multi-step reasoning under hard scenarios remain the most consistent failure modes.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决语音智能体在真实世界交互中，尤其是在存在语言不流畅现象的情况下，如何有效、低延迟地使用外部工具（API）执行多步骤任务的问题。研究背景是，尽管基于文本的大型语言模型已能通过工具调用成为强大的自主助手，但将这种能力扩展到语音模态却相对滞后。现有的语音对话系统大多局限于简单对话，缺乏调用外部API或代表用户执行操作的能力，而这恰恰是语音助手在预订航班、管理账户等场景中创造价值的关键。此外，语音交互引入了文本交互中没有的严格延迟要求，需要在快速响应与谨慎推理之间取得平衡。

现有方法存在明显不足。早期的级联方法（如AudioGPT）专为离线处理设计，不适合实时对话。较新的工作（如StreamRAG）虽然面向对话，但依赖合成数据进行训练，且模型通常不公开，其真实性能未经检验。更重要的是，现有的评测基准存在缺陷：要么（如Audio MultiChallenge）使用真实语音但完全不评估工具使用能力，要么（如VoiceAgentBench）评估工具使用但依赖合成音频或将任务限制在单步操作，从而剥离了真实口语中自然的语言不流畅（如犹豫、自我纠正）现象。这导致现有基准无法有效评估智能体在动态、多步骤的语音交互中处理复杂状态更新（例如，用户中途改变意图）的能力。

因此，本文要解决的核心问题是：如何在一个更贴近现实、包含真实人类语音不流畅现象和复杂多步骤任务的环境中，系统性地评测语音智能体的工具使用能力。为此，论文提出了Full-Duplex-Bench-v3 (FDB-v3) 基准，其核心贡献在于整合了三个关键要素：1）完全使用在非受控环境下录制的真实人类语音，并系统标注了五种不流畅类别；2）专门设计了测试自我纠正和状态回滚的场景；3）要求跨四个任务领域进行多步骤API调用链式执行。通过这个基准，论文对包括GPT-Realtime、Gemini Live等在内的六种系统配置进行了准确性、延迟和对话轮转等多维度评估，揭示了当前系统在处理自我纠正等复杂场景时的普遍不足。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基准评测类、工具使用类以及系统架构类。

在**基准评测类**工作中，Full-Duplex-Bench系列（v1, v1.5, v2）专注于实时语音交互的评估，逐步引入了轮流发言、重叠语音和多轮对话等维度，但其数据多基于TTS合成音频。Audio MultiChallenge和WildSpeech-Bench虽然使用了真实语音，却未评估工具使用能力。另一方面，τ-Voice和AudioCRAG评估了工具调用，但依赖于合成音频且仅支持单步调用，未考虑言语不流畅性。VoiceAgentBench测试了多工具工作流，但仍使用合成音频，忽略了真实语音的延迟和修正等动态因素。本文的FDB-v3则填补了关键空白，首次将**真实人类音频**（标注了五种不流畅类型）与**多步骤API调用**场景相结合，创建了一个开源、可复现的综合性基准。

在**工具使用类**研究中，ComplexFuncBench Audio等专有评测关注多步骤函数调用，但未开源。本文则对GPT-Realtime、Gemini Live等主流闭源商业语音代理以及Ultravox等开源模型进行了统一、可复现的横向评测。

在**系统架构类**方面，早期级联系统如AudioGPT和Speech-Copilot通过LLM协调外部模块，但其多阶段流水线无法实现实时交互。近期研究如StreamRAG通过并行预测查询来降低延迟，SHANKS利用“未说出的思维链”在对话中途执行工具，但这些工作大多未公开完整模型与推理代码。本文评测的Ultravox是一个重要的开源尝试，它融合了Whisper编码器以实现无需独立ASR阶段的原生工具调用。本文的基准正是为了在这种复杂、多步骤的真实场景下，公平比较各类架构的性能而设计。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Full-Duplex-Bench-v3（FDB-v3）的基准测试来解决全双工语音代理在真实世界不流畅条件下的工具使用评估问题。其核心方法围绕一个精心设计的基准框架展开，该框架旨在模拟自然语音交互的复杂性，并隔离关键性能因素。

整体框架包括三个主要组成部分：API设计、场景构建与难度分级，以及自然主义音频数据收集。首先，为了精确测量模型自身的推理和处理延迟，论文没有使用真实的网络服务，而是采用了在本地执行的模拟API。这些API提供确定性的、零延迟的响应，从而排除了网络波动或服务中断等外部干扰，确保所有测量的延迟严格反映模型的处理开销。同时，确定性的输出也支持自动化的评分。

其次，基准测试涵盖了四个任务领域，每个领域都有一小组可调用的工具。场景根据所需工具调用次数和推理复杂度被划分为三个难度等级：简单（单步）、中等（两步且存在适度歧义）和困难（多步且存在冲突约束）。这种分级旨在系统性地评估模型在不同复杂度下的表现。

关键的创新点在于其完全基于真实人类音频的数据集构建。所有音频均在非受控环境中从真人录制，并针对五种不流畅类别进行了标注，每种类别都针对特定的失败模式：错误开始（放弃原意图转向新意图）测试模型能否丢弃过时上下文而不产生幻觉工具调用；自我纠正（在句子中途更新参数）评估动态状态回滚能力；填充词（如“um”、“uh”）探究冗余词是否降低准确性或增加延迟；停顿（话语中的沉默）和犹豫（填充词与重复的组合）测试话轮结束检测的鲁棒性。数据集包含12位说话者（包括母语者和非母语者）的100条录音，录音使用日常内置麦克风在从安静房间到有轻微背景噪声的各种环境中进行，确保了评估的现实性。此外，每条录音后附加的30秒尾随静音是实际环境音的录制，而非数字静音，这使声学背景保持连贯，更逼真地模拟了流式交互。

通过这一架构，论文将模型在准确性、延迟和话轮转换等维度的性能，与真实的不流畅语音和复杂的多步骤工具使用场景直接关联，从而揭示了现有系统（如GPT-Realtime、Gemini Live等）在自我纠正处理和硬场景下的多步推理等方面存在的普遍失败模式。

### Q4: 论文做了哪些实验？

论文在Full-Duplex-Bench-v3 (FDB-v3)基准上进行了实验，该基准使用完全由真实人类音频构成的数据集，音频标注了五种不流利类别（填充词、停顿、犹豫、错误开始、自我纠正），并与需要跨四个任务领域（电子商务、金融、住房、旅行）进行链式API调用的场景配对。

实验评估了六种模型配置：GPT-Realtime、Gemini Live 2.5、Gemini Live 3.1、Grok、Ultravox v0.7以及一个传统的级联流水线基线（Whisper→GPT-4o→TTS）。评估维度包括准确性、延迟和对话轮次接管。

主要结果如下：在整体准确性（Pass@1）上，GPT-Realtime以0.600领先，其次是Gemini Live 3.1（0.540）。在延迟方面，Gemini Live 3.1的任务完成延迟最短（4.25秒），而级联基线延迟最高（10.12秒）。在对话轮次接管率上，级联基线达到完美的100%，但中断率也高达33.0%；GPT-Realtime和Ultravox的接管率均为96.0%，但Ultravox的中断率最高（47.9%），GPT-Realtime则最低（13.5%）。模型性能随场景难度（简单、中等、困难）增加而下降，GPT-Realtime在各难度级别均领先（0.750, 0.588, 0.433）。在不同任务领域中，金融领域对所有模型都最容易（GPT-Realtime达0.960），住房领域最难（GPT-Realtime为0.308）。在处理不同类型不流利现象时，停顿是大多数模型的薄弱环节，而GPT-Realtime在自我纠正处理上表现突出（0.588）。

### Q5: 有什么可以进一步探索的点？

该论文揭示了全双工语音代理在真实世界不流畅场景下的核心挑战，为未来研究提供了多个探索方向。首先，模型在处理用户意图中途修正时普遍表现不佳，这指向了状态管理机制的局限性。未来可探索更灵活的中间表示，允许参数在用户确认前保持“暂定”状态，并设计可靠的回滚机制。其次，各模型在“抢占式工具调用”与“打断用户”行为上存在差异，表明语音活动检测、推理与语音生成的协调是关键。可研究更精细的实时决策模块，动态平衡响应速度与对话礼貌性。此外，Gemini Live 3.1表现出的“沉默工作者”现象（执行工具但无语音输出）揭示了端到端模型中推理与语音生成模块可能脱节，需从架构层面确保行为一致性。最后，传统级联管道与端到端模型在延迟、可靠性和错误传播上的权衡表明，混合架构或许能结合优势，例如使用流式ASR但允许LLM实时修正，或引入增量推理与语音生成的更紧密耦合。总体而言，如何在真实对话的动态性中实现低延迟、高准确率与自然交叠的平衡，仍是核心开放问题。

### Q6: 总结一下论文的主要内容

该论文提出了Full-Duplex-Bench-v3（FDB-v3）基准，旨在评估语音智能体在真实世界不流畅语音条件下的多步骤工具使用能力。其核心贡献是创建了首个完全基于真实人类音频（标注了五类不流畅现象）并需要跨四个任务领域进行链式API调用的评测数据集，弥补了以往使用合成或脚本语音的不足。

方法上，论文系统评估了六种模型配置（包括GPT-Realtime、Gemini Live系列、Grok、Ultravox及传统的级联流水线），从准确性、延迟和对话轮转三个维度进行衡量。主要结论揭示了性能上的显著权衡：GPT-Realtime在任务准确性和避免不当打断方面领先；Gemini Live 3.1延迟最低但轮转率也最低；而传统级联基线虽有完美轮转率，延迟却最高。所有系统在用户自我修正处理和高难度场景的多步骤推理方面均存在普遍失败模式。

该工作的意义在于指出，下一代语音智能体的前沿不仅是降低延迟，更需设计能平衡快速工具执行与灵活适应真实对话动态性（尤其是实时处理用户意图变更）的新型架构。
