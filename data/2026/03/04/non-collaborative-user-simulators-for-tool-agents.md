---
title: "Non-Collaborative User Simulators for Tool Agents"
authors:
  - "Jeonghoon Shim"
  - "Woojung Song"
  - "Cheyon Jin"
  - "Seungwon KooK"
  - "Yohan Jo"
date: "2025-09-27"
arxiv_id: "2509.23124"
arxiv_url: "https://arxiv.org/abs/2509.23124"
pdf_url: "https://arxiv.org/pdf/2509.23124v5"
github_url: "https://github.com/holi-lab/NCUser"
categories:
  - "cs.CL"
tags:
  - "Tool Use & API Interaction"
  - "Human-Agent Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Human-Agent Interaction"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "GPT-4, GPT-4o, Llama-3-70B-Instruct, Qwen-2.5-72B-Instruct"
  key_technique: "Non-Collaborative User Simulator (NCUser)"
  primary_benchmark: "MultiWOZ, τ-bench"
---

# Non-Collaborative User Simulators for Tool Agents

## 原始摘要

Tool agents interact with users through multi-turn dialogues to accomplish various tasks. Recent studies have adopted user simulation methods to develop these agents in multi-turn settings. However, existing user simulators tend to be agent-friendly, exhibiting only cooperative behaviors, failing to train and test agents against non-collaborative users in the real world. We propose a novel user simulator architecture that simulates four categories of non-collaborative behaviors: requesting unavailable services, digressing into tangential conversations, expressing impatience, and providing incomplete utterances. Our user simulator can simulate challenging and natural non-collaborative behaviors while reliably delivering all intents and information necessary to accomplish the task. Our experiments on MultiWOZ and τ-bench reveal significant performance degradation in state-of-the-art tool agents when encountering non-collaborative users, as well as agent weaknesses under each non-collaborative condition such as escalated hallucinations and dialogue breakdowns. Our findings point to the need for methods that can improve agent robustness to the wide range of user behaviors encountered in deployment. We release the extensible simulation framework to help the community develop and stress-test tool agents under realistic conditions within their own service domains. Our code is available at https://github.com/holi-lab/NCUser.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前工具智能体（Tool Agents）在开发和评估过程中，由于缺乏对非协作性用户行为的模拟，导致其在实际部署中面对复杂、不友好的真实用户时表现脆弱的问题。

研究背景是，工具智能体通过多轮对话与用户交互以完成任务，而用户模拟器被广泛用于在动态多轮设置中训练和评估这些智能体。然而，现有方法的不足在于，当前主流用户模拟器和训练数据过于“智能体友好”，仅模拟协作性（即配合、理想的）用户行为，未能涵盖真实世界中用户可能表现出的各种非协作性行为。这使得智能体无法在开发阶段得到针对性的训练和压力测试，其在实际部署中的鲁棒性存疑。

因此，本文要解决的核心问题是：如何构建一个能够模拟真实、挑战性非协作用户行为的用户模拟器框架，并利用该框架系统地揭示和诊断现有先进工具智能体在面对此类行为时的性能缺陷与失败模式。具体而言，论文定义了四类非协作行为（请求不可用服务、话题偏离、表达不耐烦、提供不完整话语），并开发了一个在模拟这些行为的同时仍能确保任务目标信息得以传递的新型用户模拟器架构。通过实验，论文不仅展示了智能体性能的显著下降，还深入分析了每类行为如何导致特定的失败机制（如幻觉增加、对话崩溃），从而为开发更鲁棒的智能体指明了方向。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：多轮对话工具代理的评测与模拟，以及面向工具代理的用户模拟方法。

在多轮对话工具代理的评测方面，先前工作如τ-Bench系列和Apigen-mt等构建了基准测试和模拟环境，以评估代理在真实场景中的表现。然而，这些工作大多局限于单轮交互，或虽生成多轮对话（如模拟用户未能提供完整参数的情景），但均假设用户是完全合作的。本文则填补了这一空白，首次系统性地模拟了现实世界中用户可能表现出的**非协作行为**，从而扩展了评测场景的覆盖范围。

在用户模拟方法上，现有研究主要采用基于提示或通过监督微调（SFT）与强化学习（如GRPO）结合的方式，来构建目标导向的、协作型的用户模拟器，并常依赖“LLM-as-a-judge”来确保模拟行为与目标对齐。与之相比，本文的贡献在于：首次将研究焦点从协作用户转向**非协作用户**，通过实证研究归纳了四类具体非协作行为（如请求不可用服务、话题偏离等），并提出了一种新颖的模拟器架构。该架构在可靠传递完成任务所需所有信息和意图（即保持目标对齐）的同时，能生成具有挑战性且自然的非协作行为，从而为压力测试和增强代理的鲁棒性提供了新工具。

### Q3: 论文如何解决这个问题？

论文通过构建一个创新的非协作用户模拟器架构来解决现有用户模拟器过于友好、无法模拟真实世界中非协作用户行为的问题。其核心方法是基于一个协作式用户模拟器框架，通过引入四个专门设计的模块来注入四种非协作行为，从而在确保任务目标（传达所有必要意图和信息）得以完成的前提下，创造具有挑战性的对话环境。

整体框架以来自先前研究的协作式用户模拟器为骨干。该骨干模拟器使用LLM（如GPT-4.1-mini），根据用户目标、指令和对话历史生成上下文合适的语句，并通过一个对话状态跟踪器来确保用户目标中的所有信息片段都被传达，以及一个结束验证器来防止不恰当的对话终止。在此协作基础上，论文通过四个独立的、基于LLM的干预模块来模拟非协作行为，具体架构设计如下：

1.  **不可用服务模块**：为了模拟用户请求代理能力范围之外的服务，该模块使用LLM分析原始用户目标，识别并生成三个额外的、需要缺失API或不支持参数的目标句子。这些句子与原始目标拼接，形成增强目标，使得模拟器能在对话中自然引入无法满足的请求。

2.  **离题行为模块**：为了模拟用户谈论与任务无关的个人兴趣，该模块采用两阶段方法。首先，从Persona Hub随机采样用户画像，并基于此使用LLM生成符合四种预定对话行为（如事实性问题、观点陈述）的离题话语。然后，将这些离题话语与基础模拟器生成的协作话语合并。此外，模块还包含一个抱怨生成机制：当LLM检测到代理的回复忽略了离题内容时，会生成表达失望的抱怨，替换或补充下一次的协作话语。

3.  **不耐烦行为模块**：为了模拟用户在遇到失败或延迟时的愤怒情绪，该模块在两种场景下触发：一是当LLM识别到代理明确传达了失败信息时；二是当对话状态跟踪器判定用户已提供所有必要信息但代理仍未解决问题（被视为延迟）时。触发后，系统从三种预定义的不耐烦对话行为（如辱骂、威胁、催促）中随机采样生成话语。为了模拟真实的愤怒升级，模块采用概率激活机制，触发事件越多，表达愤怒的可能性越高。一旦表达愤怒，用户在后续所有轮次中都会保持愤世嫉俗的语调。

4.  **不完整话语模块**：为了模拟用户表达不清晰的消息，该模块模拟两种类型：极度简略的话语和过早发送的消息。对于前者，使用从真实对话数据中收集的模板，通过少量示例提示对协作话语进行风格转换。对于后者，通过随机截断协作话语来模拟输入中途意外发送。为确保目标完成，对话状态跟踪器会将截断的信息标记为未发送，保证后续重新传达。

**创新点**在于：首次系统性地定义并模拟了四种源于现实研究的非协作用户行为类别；设计了一个可扩展的模拟框架，在保持任务目标对齐的前提下，可靠地注入这些挑战性行为；通过实验揭示了当前先进工具代理在面对非协作用户时的严重性能缺陷和具体弱点（如幻觉增加、对话崩溃），为社区开发和压力测试工具代理提供了重要工具和洞察。

### Q4: 论文做了哪些实验？

论文在两个基准测试上进行了实验：MultiWOZ（专注于多领域预订任务）和τ-bench（涉及航空和零售领域的复杂顺序操作）。实验环境基于ReAct框架，设定了30步的推理限制。评估了五款基线模型，包括专有模型（GPT-4.1-mini、GPT-4.1-nano）和开源模型（Qwen3-235b-a22b、Qwen3-30b-a3b、LLaMA-3.1-70b-instruct）。核心指标是成功率（SR），即最终数据库状态与真实状态完全匹配的比例，并计算了相对于协作模式的相对成功率。

主要结果如下：在四种非协作行为下，所有模型的性能均出现显著下降。具体而言，在“不可用服务”模式下，模型（尤其是GPT-4.1-nano）因重复调用辅助API而失败率上升；在“话题偏离”模式下性能下降最严重（平均下降29.1%），GPT-4.1-nano因引发最多用户投诉而表现最差；在“不耐烦”模式下，模型过度道歉导致任务延迟；在“不完整话语”模式下，MultiWOZ中API参数幻觉错误显著增加。GPT-4.1-mini展现出最强的鲁棒性，其相对成功率下降最小。此外，当同时面对多种非协作行为时，即使GPT-4.1-mini的性能也会大幅下降。实验还扩展至ColBench和MINT基准，验证了模拟器的普适性，并发现仅使用协作数据微调的小型模型在面对非协作用户时依然脆弱。

### Q5: 有什么可以进一步探索的点？

该论文提出的非协作用户模拟器架构虽能有效暴露现有工具智能体的脆弱性，但其局限性和未来探索方向仍值得深入。首先，模拟的四类非协作行为（如请求不可用服务、话题偏离等）虽具代表性，但现实中的用户非协作模式更为复杂多元，例如包含情绪化攻击、恶意误导或文化差异导致的误解，未来可扩展行为类别并引入更细粒度的心理或社会因素建模。其次，实验基于固定数据集（MultiWOZ等），模拟环境与真实动态场景存在差距，需探索在线学习或人机循环框架，使智能体能在交互中实时适应非协作行为。此外，当前工作侧重“暴露问题”，未来可研究针对性增强方法：例如设计对抗训练机制，让智能体在混合协作与非协作对话中优化策略；或引入元学习能力，使智能体能快速识别用户行为模式并调整应对策略。最后，该模拟器未充分考虑多模态交互（如语音、手势中的非协作信号），扩展至多模态场景将更具挑战性与实用价值。

### Q6: 总结一下论文的主要内容

该论文针对工具型对话代理在现实场景中可能遇到的非协作用户问题，提出了一种新型用户模拟器架构。现有用户模拟器通常过于友好，仅模拟合作行为，无法有效训练和测试代理应对真实世界中非协作用户的能力。为此，作者定义了四类非协作行为：请求不可用服务、偏离主题的闲聊、表达不耐烦以及提供不完整话语。

论文方法的核心是设计了一个可扩展的模拟框架，能够生成具有挑战性且自然的非协作对话，同时确保传递完成任务所需的所有关键意图和信息。通过在MultiWOZ和τ-bench数据集上的实验，研究发现当前先进的工具代理在遇到非协作用户时性能显著下降，并暴露出诸如幻觉加剧和对话崩溃等具体弱点。

该工作的主要贡献在于揭示了现有对话代理在鲁棒性上的严重不足，强调了开发能应对多样化用户行为的方法的必要性。所发布的模拟框架有助于社区在各自服务领域内，于更真实的条件下开发和压力测试工具代理，推动面向实际部署的稳健性研究。
