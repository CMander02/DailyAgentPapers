---
title: "KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation"
authors:
  - "Tongbo Chen"
  - "Zhengxi Lu"
  - "Zhan Xu"
  - "Guocheng Shao"
  - "Shaohan Zhao"
  - "Fei Tang"
  - "Yong Du"
  - "Kaitao Song"
  - "Yizhou Liu"
  - "Yuchen Yan"
  - "Wenqi Zhang"
  - "Xu Tan"
  - "Weiming Lu"
  - "Jun Xiao"
  - "Yueting Zhuang"
  - "Yongliang Shen"
date: "2026-04-09"
arxiv_id: "2604.08455"
arxiv_url: "https://arxiv.org/abs/2604.08455"
pdf_url: "https://arxiv.org/pdf/2604.08455v1"
categories:
  - "cs.AI"
tags:
  - "Agent Evaluation"
  - "Personalized Agent"
  - "Proactive Agent"
  - "Mobile Agent"
  - "User Simulation"
  - "Benchmark"
  - "GUI Interaction"
  - "Preference Inference"
  - "Interactive Agent"
relevance_score: 9.0
---

# KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation

## 原始摘要

Personalized mobile agents that infer user preferences and calibrate proactive assistance hold great promise as everyday digital assistants, yet existing benchmarks fail to capture what this requires. Prior work evaluates preference recovery from static histories or intent prediction from fixed contexts. Neither tests whether an agent can elicit missing preferences through interaction, nor whether it can decide when to intervene, seek consent, or remain silent in a live GUI environment. We introduce KnowU-Bench, an online benchmark for personalized mobile agents built on a reproducible Android emulation environment, covering 42 general GUI tasks, 86 personalized tasks, and 64 proactive tasks. Unlike prior work that treats user preferences as static context, KnowU-Bench hides the user profile from the agent and exposes only behavioral logs, forcing genuine preference inference rather than context lookup. To support multi-turn preference elicitation, it instantiates an LLM-driven user simulator grounded in structured profiles, enabling realistic clarification dialogues and proactive consent handling. Beyond personalization, KnowU-Bench provides comprehensive evaluation of the complete proactive decision chain, including grounded GUI execution, consent negotiation, and post-rejection restraint, evaluated through a hybrid protocol combining rule-based verification with LLM-as-a-Judge scoring. Our experiments reveal a striking degradation: agents that excel at explicit task execution fall below 50% under vague instructions requiring user preference inference or intervention calibration, even for frontier models like Claude Sonnet 4.6. The core bottlenecks are not GUI navigation but preference acquisition and intervention calibration, exposing a fundamental gap between competent interface operation and trustworthy personal assistance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前移动智能体评估体系在个性化与主动服务能力上的严重不足。研究背景是，随着GUI智能体在明确指令下的任务执行能力日益成熟，业界产品（如豆包移动助手、OpenClaw）正朝着能够理解用户偏好、提供个性化主动助手的愿景发展。然而，现有评估基准（如AndroidWorld、MobileWorld）主要关注静态、明确指令下的任务完成度，无法衡量智能体在真实场景中所需的核心能力。

现有方法存在三个系统性缺陷：首先，现有个性化评估（如FingerTip 20K、PersonalAlign）多基于静态历史记录进行偏好恢复或意图预测，是“离线”的，未测试智能体在真实GUI环境中能否正确完成任务。其次，它们忽略了智能体应通过**交互对话**主动获取缺失偏好的关键能力。最后，在主动服务评估（如ProactiveMobile、PIRA-Bench）中，现有工作仅关注意图预测或建议排序，未能完整评估“是否干预、何时征求同意、被拒后如何克制”这一完整的主动决策链。

因此，本文要解决的核心问题是：**如何构建一个能够全面、真实评估移动智能体个性化与主动服务能力的基准**。具体而言，该基准需能评估智能体在交互中动态获取用户偏好的能力，以及在实际GUI环境下，就何时提供主动服务做出合理决策（包括提议、征询、执行及被拒后的克制）的完整链条。为此，论文提出了KnowU-Bench基准，通过可复现的安卓模拟环境、LLM驱动的用户模拟器以及覆盖从偏好获取到主动决策的综合性任务，来填补这一评估空白。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两大类：GUI执行基准测试，以及个性化和主动性基准测试。

在**GUI执行基准测试**方面，早期工作如AITW和AndroidControl建立了基于动作匹配的离线轨迹评估协议。AndroidWorld引入了可复现的全栈Android环境和程序化奖励函数，实现了可靠的端到端评估。后续研究如AndroidLab、SPA-Bench、AndroidDaily和MobileWorld扩展了任务覆盖范围、真实性和交互性，例如MobileWorld支持在模糊指令下进行代理-用户交互。然而，这些基准普遍将任务视为一次性、明确指定的目标，评估主要关注界面执行能力，而忽略了实际部署所需的用户特定推理。

在**个性化和主动性基准测试**方面，PersonalAlign和Me-Agent研究代理如何从历史偏好信号中恢复用户意图，将个性化视为基于固定行为记录的静态推理问题。FingerTip利用长期移动使用日志研究主动性任务建议。ProactiveMobile将上下文感知干预构建为动作预测问题，而PIRA-Bench和Pare则分别关注意图推荐和主动的API级执行。这些工作推进了偏好建模和主动性意图理解，但存在局限：评估在离线或受限协议下进行，缺乏在动态GUI环境中的可验证执行；均未评估代理能否在执行过程中通过多轮澄清对话获取缺失偏好；主动性评估止步于意图预测或建议排序，未涵盖完整的决策链。

本文提出的KnowU-Bench旨在一个统一的、可复现的在线评估框架内，同时解决上述三个关键差距：支持在真实GUI环境中进行验证性执行、评估多轮偏好获取能力、并全面评估包含干预决策、征求同意及被拒后克制在内的完整主动性决策链。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为KnowU-Bench的在线基准测试框架来解决个性化移动代理评估不足的问题。其核心方法是创建一个基于可复现Android仿真环境的交互式评估平台，该平台通过隐藏用户配置文件、引入基于LLM的用户模拟器以及采用混合评估策略，全面测试代理在偏好推断、主动干预和交互澄清等方面的能力。

整体框架将移动自动化建模为一个部分可观测马尔可夫决策过程（POMDP），并包含几个主要模块：一个容器化的在线移动模拟器、一个GUI代理、一个基于用户配置文件和日志的用户模拟器，以及一个混合评估管道。模拟器基于Pixel 8 AVD构建，通过统一的控制器将代理动作映射为可执行的ADB操作，并确保每次任务都从固定的模拟器快照开始，以保证可复现性。框架覆盖了23个应用程序，以支持更广泛的个性化决策场景。

关键技术设计体现在三个方面。首先，**不对称信息设计**：用户的详细结构化配置文件（P）仅对用户模拟器可见，而代理只能访问用户的历史行为日志（H）。这迫使代理必须从可观察的行为模式中主动推断用户偏好，而非直接查找静态上下文，从而评估其真实的偏好获取能力。其次，**基于LLM的用户模拟器**：用户模拟器以结构化配置文件（P）和环境状态（S）为基础，能够根据代理的询问（ask_user动作）生成符合角色设定的自由形式回复。这支持了对多轮偏好澄清对话以及主动任务中同意/拒绝处理的真实评估。最后，**混合评估策略**：结合了基于规则的验证和LLM-as-a-Judge评分。规则法官对可验证状态（如收件人正确性、订单创建、时间窗口有效性、用户拒绝后的行为约束等）进行确定性检查。LLM法官则根据特定任务的加权评估标准（如偏好对齐、沟通风格、上下文适当性等）进行语义评估。最终得分是两者的加权和，权重根据任务的确定性程度动态调整。

创新点在于：1）首次在基准测试中系统性地评估代理通过交互**主动获取缺失偏好**的能力，而不仅仅是恢复静态历史偏好。2）首次全面评估代理在实时GUI环境中的**完整主动决策链**，包括是否干预、何时征求同意、以及被拒绝后是否保持克制。3）通过隐藏配置文件和暴露行为日志的设计，以及引入角色扮演的用户模拟器，创造了一个更贴近真实、要求**动态推理**的评估环境，揭示了当前先进模型在偏好获取和干预校准方面的核心瓶颈。

### Q4: 论文做了哪些实验？

论文在KnowU-Bench基准上进行了全面的实验评估。实验设置基于一个可复现的Android模拟环境，包含42个通用GUI任务、86个个性化任务和64个主动式任务。用户偏好信息对智能体隐藏，仅提供包含无关条目的噪声行为日志，以测试其真实的偏好推断能力。对于需要交互的任务，使用GPT-4o作为用户模拟器来生成基于角色的回复和接受/拒绝决策。

评估了11个前沿模型，分为三类：1) GUI专用模型（如MAI-UI-8B、UI-Venus-1.5-8B）；2) 通用开源模型（如Qwen3-VL系列、Qwen3.5系列）；3) 闭源模型（Gemini 3.1 Pro Preview、Claude Sonnet 4.6、Seed 2.0 Pro）。主要评估指标包括：整体成功率（SR）、执行效率（Efficiency）、个性化任务的平均得分（Average Score）、交互效率（IE），以及针对主动式任务的三个策略指标：干预率（Act）、静默率（Silent）和停止率（Stop）。

主要结果显示，任务难度呈明显递进：通用任务（明确指令）执行已非瓶颈，但一旦涉及个性化推理，性能急剧下降。在困难的个性化任务子集上，表现最佳的Claude Sonnet 4.6成功率为44.2%，而所有开源模型均低于12%。在主动式任务上，模型排名不稳定，表明主动校准并非简单的偏好消歧。总体而言，闭源模型领先，Claude Sonnet 4.6取得最佳整体成功率60.4%。关键数据指标包括：在噪声全历史记忆设置下，Claude Sonnet 4.6在困难个性化任务上的成功率为44.2%，平均得分0.80；在主动任务上，其干预率（Act）达70.8%。实验还发现，更好的个性化并非源于询问更多问题（Claude平均每任务仅询问0.4个问题），而在于能否将用户反馈有效转化为正确的端到端执行。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估环境仍基于模拟器，与真实移动设备的动态性（如网络延迟、多任务切换、传感器输入）存在差距。未来可探索在真实设备上部署代理，以测试其在复杂环境下的鲁棒性。此外，KnowU-Bench 的用户模拟器虽能生成对话，但可能无法完全复现人类行为的随机性和情感因素，未来可引入真人交互数据进行补充评估。

从改进思路看，可进一步探索多模态偏好推断，例如结合用户界面截图、语音指令等丰富输入源，以提升偏好获取的准确性。同时，代理的主动决策机制可引入强化学习进行优化，使其能根据长期用户反馈动态调整干预阈值。另一个方向是增强代理的跨应用个性化能力，使其能整合不同场景下的用户习惯，实现更连贯的个性化服务。最后，隐私保护机制（如本地化偏好学习）也值得深入研究，以解决实际部署中的信任问题。

### Q6: 总结一下论文的主要内容

该论文针对个性化移动智能体缺乏有效评估基准的问题，提出了KnowU-Bench这一在线评测平台。其核心贡献在于构建了一个基于Android模拟环境的交互式、主动式与个性化智能体综合评估框架，覆盖42项通用GUI任务、86项个性化任务及64项主动干预任务。与以往将用户偏好作为静态上下文的方法不同，该基准隐藏用户档案，仅提供行为日志，迫使智能体通过交互主动推断偏好，而非简单查找。方法上，它采用基于结构化档案的LLM驱动用户模拟器，支持多轮偏好澄清对话与主动征询同意机制，并通过规则验证与LLM评分相结合的混合协议，全面评估智能体的GUI执行、同意协商及被拒后克制等完整决策链。实验表明，即使前沿模型在需要推断用户偏好或校准干预时，性能也骤降至50%以下，揭示了当前智能体在界面操作能力与可信个性化辅助之间存在本质差距，其瓶颈主要在于偏好获取与干预校准，而非GUI导航。
