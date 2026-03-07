---
title: "MT-PingEval: Evaluating Multi-Turn Collaboration with Private Information Games"
authors:
  - "Jacob Eisenstein"
  - "Fantine Huot"
  - "Adam Fisch"
  - "Jonathan Berant"
  - "Mirella Lapata"
date: "2026-02-27"
arxiv_id: "2602.24188"
arxiv_url: "https://arxiv.org/abs/2602.24188"
pdf_url: "https://arxiv.org/pdf/2602.24188v1"
categories:
  - "cs.CL"
  - "cs.LG"
tags:
  - "Multi-Agent Systems"
  - "Reasoning & Planning"
relevance_score: 7.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Reasoning & Planning"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "MT-PingEval (Multi-Turn Private Information Games Evaluation)"
  primary_benchmark: "MT-PingEval"
---

# MT-PingEval: Evaluating Multi-Turn Collaboration with Private Information Games

## 原始摘要

We present a scalable methodology for evaluating language models in multi-turn interactions, using a suite of collaborative games that require effective communication about private information. This enables an interactive scaling analysis, in which a fixed token budget is divided over a variable number of turns. We find that in many cases, language models are unable to use interactive collaboration to improve over the non-interactive baseline scenario in which one agent attempts to summarize its information and the other agent immediately acts -- despite substantial headroom. This suggests that state-of-the-art models still suffer from significant weaknesses in planning and executing multi-turn collaborative conversations. We analyze the linguistic features of these dialogues, assessing the roles of sycophancy, information density, and discourse coherence. While there is no single linguistic explanation for the collaborative weaknesses of contemporary language models, we note that humans achieve comparable task success at superior token efficiency by producing dialogues that are more coherent than those produced by most language models. The proactive management of private information is a defining feature of real-world communication, and we hope that MT-PingEval will drive further work towards improving this capability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在多轮对话中协作能力评估的难题。研究背景是，多轮对话是语言模型的核心能力，但现有评估方法存在局限。当前主流评估多采用非对称的脚本化场景（例如AI助手根据人类反馈逐步完善输出），这无法反映真实人际对话中双方需主动引导对话、选择性分享私人信息并动态获取对方信息的对称协作本质。此外，这些方法依赖能模拟人类模糊目标和偏好的用户模拟器，其构建本身极具挑战。

现有方法的不足主要体现在两方面：一是评估场景缺乏对称性，无法衡量模型主动管理对话和私人信息的能力；二是依赖难以忠实模拟人类复杂意图的模拟器，限制了评估的可靠性和泛化性。

因此，本文的核心问题是：如何设计一种可扩展、可自动验证的评估框架，以精准衡量语言模型在多轮对话中，通过有效沟通私人信息进行协作的能力。为此，论文提出了MT-PingEval基准，其核心是引入协作性私人信息游戏。在此框架下，论文进一步通过一种新颖的“交互式缩放分析”（固定总token预算，变化对话轮数），来剥离任务本身推理的影响，专门检验模型能否利用更多轮次的交互来提升任务表现，从而揭示其在多轮协作规划与执行方面的根本弱点。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多轮对话评估方法、协作任务基准以及交互式语言模型分析。

在**多轮对话评估方法**方面，现有工作常采用脚本化场景，例如让AI助手根据人类（或模拟用户）的预设目标生成提议并迭代修正（如Shao et al., 2024; Laban et al., 2025）。然而，这类方法存在不对称性（仅助手主动输出）且依赖难以真实模拟的人类用户代理。本文提出的MT-PingEval则通过对称的私有信息协作游戏（PINGs）克服这些局限，强调双方需主动沟通私有信息以达成共同目标，更贴近真实人际对话的动态性。

在**协作任务基准**上，本文借鉴了第二语言教学中的“信息差”任务传统，要求参与者通过语言交流整合私有信息（如图像和结构化知识）。相较于现有侧重于最终输出质量的评估（如代码生成或旅行规划），MT-PingEval专注于对话过程本身的可验证性，并通过自动生成实例实现大规模分析。

在**交互式语言模型分析**层面，本文创新性地引入了“固定令牌预算下的多轮缩放分析”，通过分配不同回合数来检验模型能否利用交互提升性能。这与仅增加思维链或单一回合长度的常见评测形成对比，揭示了当前模型在多轮规划与执行中的薄弱环节，例如对话提前终止或无法基于上下文优化沟通（与Cemri et al., 2025的发现呼应）。总体而言，MT-PingEval为评估模型的主动协作能力提供了新范式，凸显了现有模型在动态信息管理上的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MT-PingEval的可扩展评估框架来解决多轮交互中语言模型协作能力不足的问题。其核心方法是设计一套基于私有信息协作游戏的评估套件，并引入“等量令牌多轮缩放评估”这一创新评估范式。

整体框架包含两个关键部分：一是形式化的“交互层级”理论框架，用于量化协作游戏中私有信息交互的复杂度；二是具体的私有信息游戏任务集。在架构设计上，评估系统模拟两个玩家（均由语言模型扮演）进行多轮对话，每个玩家持有部分私有信息（如图像、结构化数据等），必须通过受限的通信来共同完成一项任务。

主要模块包括：1）**交互层级定义模块**：从Level 0（无需交互）到Level k（需要k轮高效交互）形式化定义了游戏所需的交互深度，为评估设计提供理论指导。2）**多样化游戏任务模块**：包含了国际象棋（比较棋盘时序）、COVR（多图像推理）、MD3与七巧板（图像描述与识别）、姓名游戏（结构化数据库记录匹配）等多种任务，覆盖了图像、文本、结构化数据等不同形式的私有信息，以及对称与非对称的角色互动。3）**等量令牌评估模块**：这是方法的核心创新点。它设定一个固定的总令牌预算，然后将其分割到不同数量的对话轮次中（例如，总预算256个令牌，可分配为2轮每轮128令牌，或16轮每轮16令牌）。通过比较在不同轮次分配下的任务成功率，来评估模型是否能够有效利用更多的交互轮次来提升性能，即检验其“多轮缩放”能力。

关键技术在于通过控制令牌预算和轮次数量，分离了模型“说什么”（信息内容）和“何时说”（交互规划）的能力。研究发现，即使增加轮次（交互机会），许多先进模型的表现也无法显著超越非交互基线（即一个代理总结信息，另一个直接行动），这表明它们在规划和执行多轮协作对话方面存在显著弱点。该方法通过这种可控的、可量化的评估设置，揭示了当前语言模型在需要主动管理私有信息的真实世界沟通中存在的核心缺陷。

### Q4: 论文做了哪些实验？

论文设计了一系列基于私有信息的多轮协作游戏实验，以评估语言模型在多轮交互中的协作能力。实验设置采用了创新的“等量令牌”（isotoken）评估方法，即固定每个玩家的总令牌预算（例如256个总令牌），然后改变对话轮数（如2、4、8、16轮），从而将预算分配到不同长度的对话中，以分析交互性扩展能力。

使用的数据集/基准测试包括五个需要沟通私有信息的协作游戏：1) **国际象棋**：玩家各持一个棋盘配置，需判断哪个棋盘更早出现（基线成功率50%）；2) **COVR**：基于多模态推理，玩家各看一张图像，需协作回答关于图像组合的问题；3) **MD3**和**Tangram**：非对称图像选择任务，描述者向猜测者描述图像以从多个选项中识别；4) **姓名游戏**：玩家各持一个结构化人员数据库，需找到共同记录（数据库规模有9、16、25条记录）。

对比方法涵盖了多个先进模型，包括Gemini 2.5 Pro、Gemini 2.5 Flash、GPT-4o、Qwen-VL8B和Gemma3-12B，部分模型还测试了“思考”模式（如Gemini 2.5 Flash thinking）。

主要结果显示，在许多情况下，语言模型无法通过多轮交互协作超越非交互基线（即一个代理总结信息后另一个立即行动）。例如，在国际象棋任务中，只有Gemini 2.5 Pro发现了“数棋子”的有效策略，其他模型未能利用交互提升性能；在姓名游戏中，增加轮数（更多交互）能提高准确率（如Gemini 2.5 Flash thinking在16轮时达到约72.2%），但整体任务仍具挑战性。关键数据指标包括：在MD3任务中，Gemini 2.5 Pro在2轮时准确率约85.1%，但随轮数增加性能下降（16轮时降至约75.1%）；在Tangram任务中，Qwen-VL8B在2轮时准确率约39.9%，16轮时降至约26.6%。这些结果表明，当前模型在规划和执行多轮协作对话方面仍存在显著弱点，且人类在相同任务中能以更高的令牌效率实现可比性能。

### Q5: 有什么可以进一步探索的点？

本文提出的MT-PingEval方法揭示了当前大语言模型在多轮协作对话中的显著不足，尤其是在规划与执行层面。其局限性在于评估场景相对结构化，且主要关注信息交换效率，未能充分模拟现实世界中更复杂、动态的协作情境（如目标冲突、情绪影响或开放式谈判）。

未来研究可从多个维度深入：一是**机制设计**，探索如何让模型具备更长期的对话规划能力，例如引入显式的信念状态建模或分层决策机制。二是**训练范式**，考虑设计针对多轮协作的强化学习或课程学习框架，而不仅仅是单轮指令微调。三是**评估扩展**，将评估任务从当前的私有信息游戏拓展至更广泛的领域，如多模态协作、多人团队互动，或引入外部知识库的动态查询场景。四是**效率与鲁棒性**，研究如何让模型像人类一样，以更高的语言连贯性和信息密度达成协作，同时避免谄媚（sycophancy）等偏差。最终目标是推动模型从被动响应转向主动协同，真正掌握管理私有信息的战略沟通能力。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为MT-PingEval的可扩展评估方法，用于评测语言模型在多轮交互中的协作能力。其核心问题是评估模型在需要交流私有信息的协作游戏中的表现，通过“交互式缩放分析”将固定令牌预算分配至可变对话轮次，以衡量多轮交互是否能提升任务效果。

方法上，论文设计了一套协作游戏套件，要求两个代理通过多轮对话整合各自的私有信息以完成共同目标。研究对比了交互式协作与非交互式基线（即单代理总结信息后另一代理直接行动）的性能差异。

主要结论发现，尽管存在显著提升空间，当前先进语言模型在多轮协作中往往无法超越非交互基线，表明其在规划和执行多轮协作对话方面存在明显缺陷。语言特征分析显示，人类通过更连贯的对话以更高的令牌效率达成任务，而模型则受制于谄媚倾向、信息密度和话语连贯性等问题。该研究强调了主动管理私有信息在现实通信中的关键性，MT-PingEval框架有望推动语言模型在多轮协作能力方面的进一步改进。
