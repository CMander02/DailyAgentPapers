---
title: "Beyond Scaling: Assessing Strategic Reasoning and Rapid Decision-Making Capability of LLMs in Zero-sum Environments"
authors:
  - "Yang Li"
  - "Xing Chen"
  - "Yutao Liu"
  - "Gege Qi"
  - "Yanxian BI"
  - "Zizhe Wang"
  - "Yunjian Zhang"
  - "Yao Zhu"
date: "2026-03-10"
arxiv_id: "2603.09337"
arxiv_url: "https://arxiv.org/abs/2603.09337"
pdf_url: "https://arxiv.org/pdf/2603.09337v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "多智能体评估"
  - "战略推理"
  - "实时决策"
  - "基准测试"
  - "零和博弈"
  - "交互式智能体"
relevance_score: 7.5
---

# Beyond Scaling: Assessing Strategic Reasoning and Rapid Decision-Making Capability of LLMs in Zero-sum Environments

## 原始摘要

Large Language Models (LLMs) have achieved strong performance on static reasoning benchmarks, yet their effectiveness as interactive agents operating in adversarial, time-sensitive environments remains poorly understood. Existing evaluations largely treat reasoning as a single-shot capability, overlooking the challenges of opponent-aware decision-making, temporal constraints, and execution under pressure. This paper introduces Strategic Tactical Agent Reasoning (STAR) Benchmark, a multi-agent evaluation framework that assesses LLMs through 1v1 zero-sum competitive interactions, framing reasoning as an iterative, adaptive decision-making process. STAR supports both turn-based and real-time settings, enabling controlled analysis of long-horizon strategic planning and fast-paced tactical execution within a unified environment. Built on a modular architecture with a standardized API and fully implemented execution engine, STAR facilitates reproducible evaluation and flexible task customization. To move beyond binary win-loss outcomes, we introduce a Strategic Evaluation Suite that assesses not only competitive success but also the quality of strategic behavior, such as execution efficiency and outcome stability. Extensive pairwise evaluations reveal a pronounced strategy-execution gap: while reasoning-intensive models dominate turn-based settings, their inference latency often leads to inferior performance in real-time scenarios, where faster instruction-tuned models prevail. These results show that strategic intelligence in interactive environments depends not only on reasoning depth, but also on the ability to translate plans into timely actions, positioning STAR as a principled benchmark for studying this trade-off in competitive, dynamic settings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型评估体系在衡量其作为交互式智能体、尤其是在对抗性和时间敏感环境中的战略决策能力方面的不足。研究背景是，尽管LLMs在静态推理基准测试中表现出色，但现有评估大多将推理视为单次、独立于上下文的过程，忽略了模型在动态、对抗性互动中所需的关键能力。现有方法的不足主要体现在三个方面：一是多数评估聚焦于单智能体在非对抗环境中的表现，无法考察模型对竞争对手的推理和应对能力；二是忽视了时间结构，允许模型无限制推理时间，掩盖了在序列决策中推理深度与决策及时性之间的权衡；三是评估指标较为粗粒度（如准确率或成功率），难以剖析模型胜负背后的具体原因及其战略行为的稳健性。

本文要解决的核心问题是：如何系统评估LLMs在零和博弈的交互式环境中，进行战略推理和快速决策的能力。为此，论文引入了战略战术智能体推理基准（STAR），这是一个多智能体评估框架，通过1v1零和竞争性互动来评估LLMs，将推理重新定义为迭代的、自适应的决策过程。STAR支持回合制和实时两种设置，能够在一个统一环境中分析长期战略规划和快节奏战术执行。研究旨在超越简单的胜负结果，通过引入战略评估套件，不仅评估竞争胜率，还评估战略行为质量（如执行效率和结果稳定性），从而揭示LLMs在将复杂推理转化为及时有效行动过程中存在的“战略-执行差距”。

### Q2: 有哪些相关研究？

相关研究主要可分为方法类、应用类和评测类三大方向。在评测类工作中，现有基准大多关注静态任务下的单一模型能力评估：例如知识理解类基准（如GLUE系列、MMLU、BigBench及改进版MMLU-Pro），工具学习类基准（如MetaTool、WTU-Eval、APIBench、ToolBench等），代码生成类基准（如HumanEval、MBPP、L2CEval），以及推理能力基准（如GSM8K、MathBench、AGIEval、CRASS等）。这些工作主要评估模型在孤立、单次任务中的表现，缺乏对动态交互环境中多步决策、实时适应和对手感知能力的考察。

本文提出的STAR基准与上述工作的核心区别在于，它将评估重点从静态推理转向了多智能体在零和竞争环境中的交互式决策过程。STAR通过支持回合制与实时对抗两种模式，能够系统评估长期战略规划与快速战术执行能力，从而弥补了现有基准在动态性、交互性和竞争性评估方面的空白。此外，STAR还引入了战略行为质量评估套件，不仅关注胜负结果，还分析执行效率与稳定性，为理解模型在压力下的推理-执行权衡提供了新视角。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为STAR（Strategic Tactical Agent Reasoning）的基准测试框架来解决评估大语言模型在对抗性、时间敏感环境中作为交互式智能体能力的问题。其核心方法是将战略推理形式化为一个有限视界、部分可观测的零和随机博弈，并设计了一个模块化、分层的系统架构来实现可重复且灵活的多智能体评估。

整体框架由四个解耦的层级构成。**框架层**作为核心引擎，基于实体-组件-系统（ECS）范式构建。ECS架构将状态（实体与组件）与行为（系统）分离，实现了严格的数据-逻辑解耦和动态组合性，便于研究者修改或扩展模拟规则。**环境层**封装了具体的游戏规则和世界动态，论文中实例化为一个基于六边形网格的战争游戏场景。该层实现了“战争迷雾”机制，通过视觉系统过滤ECS状态，确保环境是部分可观测的，从而引入信息不对称，这是测试战略推理的关键。**协议层**提供了一个标准化的异步通信接口，使用基于WebSocket的结构化“信封”格式进行数据交换。这种设计使得框架能够无缝集成异构的LLM智能体，从商业API模型到本地开源模型，支持可扩展的多智能体评估。**智能体层**作为LLM的运行时宿主，实现了标准化的感知-规划-行动循环。它负责关键的信息转换：将环境的结构化ECS状态优化为自然语言提示上下文，同时解析模型的输出为可执行的协议指令，从而弥合概率性LLM推理与确定性游戏逻辑之间的鸿沟。

关键技术包括：1）**零和博弈任务设计**：采用对称的、基于网格的战争游戏，强调空间推理、战术协调和长视距规划，以公平地评估对抗性决策。2）**部分可观测性实现**：通过“战争迷雾”机制模拟真实对抗中的不确定性。3）**双重评估模式**：同时支持回合制和实时设置，使得能够在一个统一环境中对比分析长期战略规划和快速战术执行。4）**战略评估套件**：超越简单的胜负结果，引入了执行效率和结果稳定性等指标来评估战略行为质量。

创新点主要体现在：1）**将推理重新定义为迭代、自适应的决策过程**，而非单次静态能力。2）**模块化与可扩展性**：通过分层和解耦设计，允许研究者轻松定制新环境或集成新模型，而无需重写底层引擎。3）**揭示了策略-执行差距**：通过广泛的成对评估，论文发现推理密集型模型在回合制中占优，但其推理延迟在实时场景中往往导致性能下降，而更快的指令调优模型则在实时场景中胜出。这证明了交互环境中的战略智能不仅取决于推理深度，还取决于将计划转化为及时行动的能力。STAR基准正是为系统研究这种权衡而设计的。

### Q4: 论文做了哪些实验？

论文在提出的STAR基准测试框架下，进行了系统性的实验评估，主要包含以下方面：

**实验设置与数据集**：实验在STAR基准上进行，这是一个支持1v1零和竞争交互的多智能体评估框架。测试包含两种模式：**回合制模式**（侧重无约束的深度战略规划）和**实时模式**（评估在时间压力下保持推理质量的能力）。评估采用循环赛制，每个模型与其他所有模型进行对抗。

**对比方法与评估指标**：评估了多个代表性LLM，包括Kimi-K2（Thinking/Instruct）、GLM-4系列、Qwen3系列、DeepSeek系列、Claude-3.7-Sonnet、Llama-4-Scout等。使用了三组互补的指标：胜率、标准ELO评分（SER）和**性能加权ELO评分（PWER）**。PWER是关键创新指标，它通过性能乘数M整合了**单位保存率**（𝒰 = 存活单位数/总单位数）和**时间效率**（𝒯 = 1 - min(游戏时间/最大时间, 1)），以衡量胜利的质量（资源消耗和战略效率），而不仅仅是胜负结果。

**主要结果与关键数据**：
1.  **回合制模式**：推理增强型模型（如Kimi-K2-Thinking）凭借深度规划和显式思考占据主导。Kimi-K2-Thinking的PWER大幅领先其指令微调版Kimi-K2-Instruct达371分，表明战略规划能力而非模型规模是关键。
2.  **实时模式**：性能格局发生显著变化，推理延迟成为关键制约。指令微调且推理速度快的模型（如GLM-4.6、Qwen3-30B-A3B-Instruct）排名前列。例如，GLM-4.6的PWER为1180.8±33.7，胜率0.75。而许多思考型模型排名大幅下降，如Kimi-K2-Thinking的PWER降至842.6±9.5，胜率仅0.210。这揭示了**战略-执行差距**：深度推理能力在时间压力下可能成为负担。
3.  **消融研究（视觉与逻辑推理）**：对比视觉语言模型（VLM）与其纯文本对应模型（LLM），发现**感知-行动权衡**。VLMs（如Qwen3-VL-32B）空间感知错误率低（SAE=5.3%），但每局行动数少（33次），因视觉编码延迟导致行动吞吐量低。标准LLMs行动频率高但空间错误率高。而“思考型”文本模型通过思维链推理，能在不引入视觉延迟的情况下降低空间错误，达到更好平衡。
4.  **涌现战略行为分析**：高性能模型（PWER > 1100）表现出类似人类专家的复杂行为，如自我组织的防御阵型、协同打击（集中火力）和地形利用（占据丛林获得防御优势），而较弱模型则依赖简单的贪婪启发式策略。

这些实验结果表明，在动态竞争环境中，智能体的战略智能不仅取决于推理深度，还依赖于将计划转化为及时行动的能力，STAR基准为研究这种权衡提供了系统性的评估方法。

### Q5: 有什么可以进一步探索的点？

该论文虽构建了STAR基准以评估LLMs在对抗性环境中的战略推理与快速决策能力，但仍存在若干局限与可拓展方向。首先，基准目前聚焦于零和博弈，未来可引入合作博弈、不完全信息博弈等更复杂场景，以检验LLMs在多方互动与信息不对称下的策略适应性。其次，评估虽区分回合制与实时设置，但对“时间压力”的模拟仍较简化；可进一步引入动态变化的时间约束与多任务并行，以更贴近真实世界的决策负荷。此外，论文发现的“策略-执行差距”揭示了模型推理深度与延迟间的权衡，未来可探索轻量化推理架构（如思维蒸馏）、模型并行化优化，或将符号规划与神经网络快速响应相结合，以提升实时决策效率。最后，评估指标可进一步细化，例如引入对手建模能力、策略可解释性分析，以及长期策略稳健性的跨环境迁移测试，从而更全面衡量智能体的动态战略智能。

### Q6: 总结一下论文的主要内容

该论文提出了战略战术智能体推理基准（STAR），旨在系统评估大语言模型在动态对抗环境中的深度推理与快速决策能力。核心问题是现有评估多关注静态单次推理，忽视了对手感知、时间压力和实时交互等挑战。

论文方法上构建了一个多智能体零和博弈评估框架，支持回合制与实时两种模式，通过模块化架构和标准化API实现可复现的评估与任务定制。此外，还引入了战略评估套件，不仅衡量胜负，还评估执行效率和结果稳定性等战略行为质量。

主要结论是通过大量配对实验发现显著的“战略-执行差距”：擅长深度推理的模型在回合制环境中占优，但其推理延迟导致在实时场景中表现不佳，而更快的指令微调模型则占据上风。这表明交互环境中的战略智能不仅取决于推理深度，更依赖于将计划转化为及时行动的能力。STAR基准为研究这种权衡提供了原则性框架，推动了LLM在复杂动态场景中的评估与研究。
