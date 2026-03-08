---
title: "GroupGPT: A Token-efficient and Privacy-preserving Agentic Framework for Multi-User Chat Assistant"
authors:
  - "Zhuokang Shen"
  - "Yifan Wang"
  - "Hanyu Chen"
  - "Wenxuan Huang"
  - "Shaohui Lin"
date: "2026-03-01"
arxiv_id: "2603.01059"
arxiv_url: "https://arxiv.org/abs/2603.01059"
pdf_url: "https://arxiv.org/pdf/2603.01059v1"
github_url: "https://github.com/Eliot-Shen/GroupGPT"
categories:
  - "cs.CL"
tags:
  - "Multi-Agent Systems"
  - "Human-Agent Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Human-Agent Interaction"
  domain: "Social & Behavioral Science"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "GroupGPT (small-large model collaborative architecture)"
  primary_benchmark: "MUIR"
---

# GroupGPT: A Token-efficient and Privacy-preserving Agentic Framework for Multi-User Chat Assistant

## 原始摘要

Recent advances in large language models (LLMs) have enabled increasingly capable chatbots. However, most existing systems focus on single-user settings and do not generalize well to multi-user group chats, where agents require more proactive and accurate intervention under complex, evolving contexts. Existing approaches typically rely on LLMs for both reasoning and generation, leading to high token consumption, limited scalability, and potential privacy risks. To address these challenges, we propose GroupGPT, a token-efficient and privacy-preserving agentic framework for multi-user chat assistant. GroupGPT adopts a small-large model collaborative architecture to decouple intervention timing from response generation, enabling efficient and accurate decision-making. The framework also supports multimodal inputs, including memes, images, videos, and voice messages. We further introduce MUIR, a benchmark dataset for multi-user chat assistant intervention reasoning. MUIR contains 2,500 annotated group chat segments with intervention labels and rationales, supporting evaluation of timing accuracy and response quality. We evaluate a range of models on MUIR, from large language models to smaller counterparts. Extensive experiments demonstrate that GroupGPT produces accurate and well-timed responses, achieving an average score of 4.72/5.0 in LLM-based evaluation, and is well received by users across diverse group chat scenarios. Moreover, GroupGPT reduces token usage by up to 3 times compared to baseline methods, while providing privacy sanitization of user messages before cloud transmission. Code is available at: https://github.com/Eliot-Shen/GroupGPT .

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有聊天机器人系统在**多用户群聊场景**中表现不足的问题。随着大语言模型（LLM）的发展，单用户聊天机器人已相当成熟，但将其直接应用于动态、复杂的多人对话环境时，面临三大核心挑战：**现有方法通常依赖单一LLM进行推理和生成，导致计算令牌（token）消耗巨大、系统可扩展性有限，并且在处理用户消息时存在隐私泄露风险**。此外，当前研究缺乏针对群聊场景中智能体**主动、适时干预**能力的系统化评估基准。

研究背景是，当前业界的群聊机器人大多基于规则、被动响应，难以在诸如头脑风暴、辩论等需要主动参与的复杂对话中发挥作用。先前提出的多用户框架往往令牌效率低下，且隐私保护不足，其评估方法也主要依赖主观性强、场景有限的人工设计或用户研究，难以全面反映真实环境下的性能。

因此，本文的核心问题是：**如何构建一个既能高效、适时地主动参与多用户群聊，又能显著降低计算成本并保护用户隐私的智能体框架？** 为此，论文提出了GroupGPT框架，其核心创新在于采用“小模型-大模型”协同架构，将**干预时机判断**与**最终响应生成**这两个任务解耦，从而在保证响应质量的同时，大幅提升令牌使用效率并集成隐私过滤机制。同时，论文还引入了首个多用户干预推理基准数据集MUIR，以支持对干预时机和响应质量的系统化、定量评估。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为两大类：多用户聊天机器人和基于LLM的对话代理中的隐私问题。

在多用户聊天机器人方面，早期研究主要集中在**单用户任务型对话系统**。针对多用户场景，研究则多集中于对话理解任务（如识别受话者）。近期工作开始关注构建主动的群聊助手。例如，MUCA框架首次形式化了“说什么、何时说、对谁说”的“3W”维度。HUMA框架在此基础上，利用类人对话策略使行为更自然。此外，MAP从个性化角度、Social-RAG从利用社交信号的角度、SeeSawBot从调节群体动态的角度进行了探索。工业界也推出了如ChatGPT群聊功能等产品。**本文提出的GroupGPT与这些工作的核心区别在于其架构设计**：现有方法通常依赖单一LLM进行推理和生成，导致令牌消耗高、可扩展性有限；而GroupGPT采用“小模型-大模型”协作架构，将干预时机决策与响应生成解耦，从而显著提升了效率。

在隐私保护方面，相关研究指出了LLM对话代理的两类隐私风险：传统数据安全问题和LLM特有的记忆泄露风险。现有解决方案多为**以模型为中心的策略**，包括训练时的数据清洗、差分隐私，训练后的知识遗忘，以及推理时的个人身份信息检测与重写。**GroupGPT的贡献在于提供了一个应用层的、轻量化的隐私保护机制**，它在将用户消息发送至云端大模型前进行隐私清洗，这是一种更直接且易于部署的推理时保护方法，与复杂的模型修改方案形成互补。

### Q3: 论文如何解决这个问题？

GroupGPT 通过一个创新的“小-大模型协同架构”来解决多用户群聊场景中高效、精准且保护隐私的智能体干预问题。其核心思想是将干预决策（何时、如何干预）与最终响应生成这两个高计算成本的任务解耦，从而在保证响应质量的同时，显著降低令牌消耗和隐私风险。

**整体框架**是一个顺序协作的在线推理流水线，包含五个核心组件。流程始于**多模态消息处理器**，它将图像、表情包、视频、语音等非文本内容，通过专用模型（如图像分类与描述、语音识别）转化为带特定标签的结构化文本描述，从而将所有输入统一为文本上下文，便于后续处理。

随后，系统并行执行两个关键异步分支。一是**干预判断器**，它是一个在自建MUIR数据集上指令微调的轻量级语言模型，负责持续监控由最近若干消息构成的短期对话窗口，实时判断是否需要干预并输出六类预定义干预动作之一（如保持沉默、提供建议、情感支持等）。这取代了传统基于固定间隔调用大模型的低效策略，实现了精准的按需触发。二是**隐私转录器**，它同样是轻量级模型，负责对每条原始消息进行独立处理，检测并匿名化其中的个人可识别信息，生成一个保留语义但去敏的版本。这两个轻量模型并行运行，在同步点汇合。

**聊天频率记录器**则作为一个辅助模块，持续统计固定时间窗口内的消息总量和用户发言频率，为最终响应提供对话活跃度的信号。

当且仅当干预判断器决定干预时，**最终响应者**才会被激活。它是一个大型语言模型，负责生成最终的助理回复。其输入综合了：来自干预判断器的动作指令、来自隐私转录器的去敏化长期对话历史、来自频率记录器的聊天活跃度信号、以及预设的行为规则和任务提示。通过整合这些信息，大模型能生成符合上下文、时机恰当且安全的响应。

**创新点**主要体现在：1) **架构创新**：通过轻量模型负责高频的决策判断，重型模型仅在被触发时进行生成，实现了计算资源的优化分配，实验表明令牌消耗可比基线方法减少高达3倍。2) **隐私保护内嵌**：在数据上传至云端大模型前，通过本地轻量模型进行实时去敏处理，从流程上降低了隐私泄露风险。3) **多模态与上下文统一**：通过处理器将异构信息转化为统一文本表示，使框架能处理真实场景的复杂输入，同时保持核心架构的简洁性。4) **数据与评估驱动**：引入了专门构建的MUIR基准数据集，用于训练干预判断器并系统评估模型在干预时机和响应质量上的表现。

### Q4: 论文做了哪些实验？

论文实验主要包括在MUIR基准测试上的模型性能评估、用户研究、以及系统效率分析。实验设置上，GroupGPT采用小大模型协作架构，使用Qwen-3-4B作为干预时机判断模型，Llama-3.2-Instruct-3B作为干预理由生成模型，并利用Qwen-2.5-32B进行多模态标注，最终响应由GPT-4o生成。模型在2块A6000 GPU上使用LoRA进行训练。

数据集方面，论文引入了MUIR基准数据集，包含2500个标注的群聊片段，用于评估干预时机和响应质量。对比方法包括随机猜测、人类评估、基于嵌入的KNN分类、微调的小语言模型（SLMs）以及仅使用提示的大语言模型（LLM-only）基线。

主要结果如下：在MUIR测试集上，微调的SLMs在干预时机任务上显著优于大模型，例如Qwen-3 4B在Chime-in Timing任务上达到83.4%的准确率和88.7%的F1分数；Qwen-2.5-Instruct 3B在Chime-in Reason任务上达到86.3%的准确率和81.0%的Macro-F1，综合得分最佳。用户研究中，GroupGPT在LLM评估的四个维度（相关性、连贯性、流畅性、帮助性）平均得分达4.72/5.0，其中流畅性平均4.90。效率方面，GroupGPT相比LLM-only基线将token消耗降低了约3倍（从约20亿token/年降至6.6亿），端到端平均推理延迟为4.36秒，GPU内存占用为18.41 GB。后测问卷显示，超过70%的用户认为其干预有帮助，84%的用户认可其隐私保护效果。

### Q5: 有什么可以进一步探索的点？

该论文提出的GroupGPT框架在效率和隐私方面取得了进展，但仍有多个方向值得深入探索。首先，其干预决策主要基于文本上下文，未来可加强对多模态信息（如图像、视频内容）的语义理解与融合，以更精准判断介入时机。其次，当前框架依赖标注数据进行训练，可研究小样本或自监督方法，提升对动态、开放域群聊场景的适应能力。隐私保护方面，仅进行消息脱敏可能不足，可探索端侧模型协同或联邦学习架构，进一步减少云端数据传输。此外，评估基准MUIR虽具开创性，但规模与场景多样性有限，需扩展至更复杂、跨文化的交互环境，并引入人类实时反馈机制。最后，框架的“主动性”与“非侵入性”平衡仍需优化，可结合用户个性化偏好与群组动态，实现更智能、人性化的干预策略。

### Q6: 总结一下论文的主要内容

该论文针对多用户群聊场景中现有聊天助手存在的干预时机不准、令牌消耗高、隐私风险大等问题，提出了GroupGPT框架。其核心贡献在于设计了一个大小模型协同的架构：使用小型模型高效、本地化地实时分析对话流以决定干预时机，而大型模型仅在需要时生成高质量响应，从而将决策与生成解耦。这种方法显著提升了响应准确性和时效性，同时大幅降低了令牌使用量（可达基线方法的1/3）并保护了用户隐私（在消息上传云端前进行脱敏处理）。此外，论文还构建了MUIR基准数据集，用于评估模型在多元群聊中的干预推理能力。实验表明，GroupGPT在多种场景下均能产生适时、准确的响应，获得了较高的LLM评估分数和用户好评。
