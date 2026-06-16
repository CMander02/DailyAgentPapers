---
title: "Human-on-the-Bridge: Scalable Evaluation for AI Agents"
authors:
  - "Fouad Bousetouane"
date: "2026-06-15"
arxiv_id: "2606.16871"
arxiv_url: "https://arxiv.org/abs/2606.16871"
pdf_url: "https://arxiv.org/pdf/2606.16871v1"
categories:
  - "cs.MA"
tags:
  - "Agent评估"
  - "可扩展评估"
  - "多智能体评估"
  - "对抗性评估"
  - "基于LLM的智能体"
  - "工具使用"
  - "策略合规"
  - "幻觉检测"
  - "人机协作评估"
  - "评估框架"
relevance_score: 8.5
---

# Human-on-the-Bridge: Scalable Evaluation for AI Agents

## 原始摘要

AI agents must be evaluated as behavioral systems, not as isolated response generators. They reason across turns, call tools, preserve context, follow policies, and act under uncertainty. Existing methods provide useful but fragmented signals: benchmarks measure fixed capabilities, Human-in-the-Loop review preserves expert judgment but does not scale easily, LLM-as-judge methods depend on evaluator design, red teaming is often episodic, and trace auditing requires explicit evidence rules. This paper introduces Human-on-the-Bridge (HOB), a scalable evaluation paradigm for agentic AI. HOB places human expertise upstream, where experts curate reusable evaluation intelligence before testing begins, including domain context, Red-Team Traps, Juror Personas, scoring guidelines, audit rules, and fallback policies. ProofAgent Harness then executes this curated intelligence repeatedly through multi-turn adversarial evaluations, trace capture, multi-juror scoring, and evidence-linked reporting. We evaluate HOB through symmetric and cost-efficient asymmetric settings across frontier LLM-based agents and Harness LLM tiers. The study covers 23,500 agent turns and produces evidence-linked findings across finance, healthcare, and code generation. The results show that HOB can amplify evaluation quality without requiring equally large evaluator models, allowing smaller Harness LLMs to challenge agents built on frontier LLM backbones. The evaluation surfaces failures often missed by static benchmarks and single-evaluator scoring, including phantom tool-call claims, missing mandatory tool calls, policy drift, manipulation paths, and safe but non-resolving refusals. These findings support HOB as a paradigm for scaling human-curated evaluation intelligence, where expert judgment is encoded upfront and reused across repeated agent evaluations rather than applied manually inside every run.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决AI Agent评估的可扩展性问题。当前AI Agent已从独立的文本生成系统演变为需要跨轮推理、调用工具、遵循策略并承担行为后果的交互系统，其失败可能通过工具调用、记忆错误等传播，造成系统性风险。然而现有评估方法存在明显不足：静态基准只能衡量固定能力，无法捕捉工具误用、策略漂移等多轮行为缺陷；人类参与式评估虽保留专家判断但难以规模化；LLM作为裁判的方法受限于评估模型的性能和任务设计；红队测试常是零散的；轨迹审计又依赖显式规则。这些方法共同导致一个核心矛盾：专家判断的深度与规模化评估的效率无法兼得。为此，本文提出了Human-on-the-Bridge（HOB）范式，将人类专家从每轮评估中解放出来，转而要求他们提前编排可复用的评估智慧（包括领域上下文、红队陷阱、陪审员角色等），再通过自动化测试平台反复执行。其核心创新在于让专家判断在上游沉淀为可复用的评估基础设施，从而在不牺牲评估质量的前提下实现规模化，有效检测那些被静态基准忽略的隐藏失败模式。

### Q2: 有哪些相关研究？

相关研究主要分为以下几类：**（1）静态基准与交互式基准**：如MMLU、HumanEval测试固定能力，AgentBench、ReAct等评估交互环境中的轨迹。本文指出，这些方法虽标准化但难以捕捉代理的行为和程序性错误（如工具调用遗漏、策略漂移），HOB通过前置人类专家知识和对抗性评估弥补了动态过程评估的不足。**（2）人类参与方法**：Human-in-the-Loop (HITL) 提供强专家判断但难扩展，而HOB采用“人类在桥上”（HOB）模式，将专家知识编码为可复用的评估智能（如红队陷阱、评审人格），而非在每个评估回合中手动介入，从而平衡了判断质量与可扩展性。**（3）LLM-as-Judge与红队测试**：G-Eval、MT-Bench等方法利用LLM评分，但存在偏见且难以理解领域策略；传统红队测试虽能发现漏洞，但常是偶发性的。HOB将LLM评委视为执行组件，并结合可复用的红队陷阱实现系统化对抗压力。**（4）追踪审计与日志评估**：如ReAct强调推理-动作轨迹，但HOB要求将轨迹与规则明确链接，支持确定性审计（如检查工具调用是否真实发生）。**（5）开放评估基础设施**：LangSmith、ProofAgent Harness等提供可执行框架，但HOB进一步提出了组织人类、评委模型、规则和报告协同工作的范式。

### Q3: 论文如何解决这个问题？

HOB通过将人类专业知识前置、模块化封装为可复用的评估智能，并利用执行引擎ProofAgent Harness进行规模化执行，来解决现有评估方法的碎片化与扩展性问题。其核心方法是构建一个“人不在回路内、而在桥上”的范式。整体框架由四大部分构成：一是“桥上的专家”，负责在测试开始前策划评估智能（I_HOB），包括领域上下文（D）、红队陷阱库（T）、裁判角色（J）、评分指南（S）、审计规则（R）和降级策略（F）；二是“被测代理”（A），即待评估的AI Agent；三是“执行引擎”（ProofAgent Harness），负责在多轮对抗性评估中与被测代理交互、捕获行为轨迹（τ）；四是“执行引擎的LLM”（Harness LLM），提供评估所需的推理和交互能力。

主要模块及创新点包括：**红队陷阱**（T）编码专家对Agent失败模式的预判，形成对抗性压力测试；**裁判角色**（J）从安全、合规、任务成功等多角度评分，避免单一视角的偏见；**评分指南与审计规则**（S和R）确保每项分数和失败都关联到具体的可观测证据（如虚构工具调用、遗漏工具调用、策略漂移），使评估结果可审查、可复现；**降级策略**（F）处理执行过程中的不稳定事件，保证评估流程的鲁棒性。最终输出不仅是分数，而是包含行为轨迹、分数向量、检测到的失败集（Φ）及报告的完整评估工件。其创新在于将人类专家从每轮评估的手动介入中解放，转为一次性策划可跨多轮、跨版本复用的评估“知识”，显著降低了规模化评估的边际成本，让较小规模的Harness LLM也能有效评估基于前沿大模型的Agent。

### Q4: 论文做了哪些实验？

论文设计了系统性的实验来验证Human-on-the-Bridge (HOB) 范式的可扩展性。实验覆盖代码生成、金融咨询和医疗分诊三个领域，评估了基于 GPT-4.1、GPT-5.5、Claude Opus 4.7 和 Claude Opus 4.8 等前沿 LLM 构建的智能体。实验采用 ProofAgent Harness，包含 5 个评估模型层级：4B Gemma、8B Llama-3.1、32B Qwen-3、70B Llama-3.3 和 120B GPT-OSS。共完成 47 个配置，每个配置进行 10 轮 50 步的对抗性评估，总计 23,500 个智能体轮次。主要指标包括任务成功率、幻觉抵抗、安全性、指令遵循和操控抵抗。关键发现：1) HOB 支持不对称评估，小模型（如 4B Gemma）在结构化流程引导下也能发现基于前沿 LLM 智能体的客观失败（如幻影工具调用、策略漂移），但其主观评分更宽松（中位 7.76）vs 大模型（120B GPT-OSS 中位 6.27）；2) 不同智能体展现多维可靠性差异，如 GPT-4.1 任务成功最高（7.75）但安全性较低（6.10），Claude Opus 4.8 防御性最强（操控抵抗 8.70）。实验还揭示了静态基准难以发现的隐藏失败模式，并验证了故障策略的连续性。

### Q5: 有什么可以进一步探索的点？

论文最大的局限在于对评估智能体行为复杂度的覆盖仍不充分。尽管HOB引入了红队陷阱和陪审团机制，但预定义的专家知识库本质上是静态的，难以动态应对Agent在开放环境中涌现的新兴策略，例如利用长上下文进行隐式推理或跨轮次的社会工程攻击。未来可探索结合对抗性生成网络，让兰斯LLM自动化生成更动态的陷阱情景；同时引入元学习框架，使专家知识库能根据评估历史自动迭代更新。此外，当前多陪审团评分依赖离散投票，忽略了评分过程中的不确定性，可引入贝叶斯置信区间建模替代阈值决策。另一个关键方向是量化专家知识注入的边际收益，建立成本与评估质量之间的解析模型，从而为不同风险等级的Agent任务自适应分配评估资源，避免因过度预定义导致评估偏见。

### Q6: 总结一下论文的主要内容

本文介绍了一种名为Human-on-the-Bridge（HOB）的可扩展AI Agent评估范式。现有方法存在碎片化问题：静态基准仅测量固定能力，人在回路中难以扩展，LLM评判依赖评估器设计，红队测试不具备可重用性，轨迹审计需明确规则。HOB将人类专业知识前置，在测试前创建可复用的评估智能，包括领域上下文、红队陷阱、评审角色、评分指南、审计规则和回退策略。通过ProofAgent Harness执行器，实现多轮对抗评估、轨迹捕获、多评审评分和基于证据的报告。在金融、医疗和代码生成领域评估了23500个Agent回合，发现多种难以通过静态基准检测的失败模式，如幻象工具调用、策略漂移、操纵路径和安全但无效的拒绝。研究表明HOB能使较小的评估模型挑战前沿LLM Agent，从而扩展人类评估智能的可复用性。
