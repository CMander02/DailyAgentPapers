---
title: "Formal Skill: Programmable Runtime Skills for Efficient and Accurate LLM Agents"
authors:
  - "Xi Zhang"
  - "Meijun Gao"
  - "Yuntian Zhao"
  - "Xinyu Tan"
  - "Yilun Yao"
  - "Feiyu Wang"
  - "Yanshu Wang"
  - "Dingsiyi"
  - "Tong Yang"
date: "2026-05-19"
arxiv_id: "2605.19604"
arxiv_url: "https://arxiv.org/abs/2605.19604"
pdf_url: "https://arxiv.org/pdf/2605.19604v1"
categories:
  - "cs.AI"
tags:
  - "Agent架构"
  - "工具使用"
  - "编程技能"
  - "Agent运行时"
  - "LLM Agent"
relevance_score: 8.5
---

# Formal Skill: Programmable Runtime Skills for Efficient and Accurate LLM Agents

## 原始摘要

Large Language Model (LLM) agents increasingly act inside real workspaces, where tools and skills determine whether model reasoning becomes reliable action. Existing skills remain largely informal: Markdown skills and instruction packs encode procedures as long natural-language documents, while function calling, Model Context Protocol (MCP) servers, and framework tools structure individual actions but usually leave workflow state, policy enforcement, and completion discipline outside the skill itself. We introduce Formal Skill, a runtime-native abstraction that represents reusable capability with JSON metadata and action schemas, reliable Python executors, hook-governed control logic, Formal Skill routing, and skill-local runtime state. By moving reusable procedure from repeated prompt text into executable state machines and hook policies, Formal Skill gives agents a token-efficient and enforceable control surface. We implement the abstraction in FairyClaw, an open-source event-driven runtime for executable, observable, and composable Formal Skills. On Harness-Bench, FairyClaw obtains highly competitive average scores while using substantially fewer tokens, with especially strong results on tasks that expose the role of Formal Skill.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文针对大语言模型（LLM）代理在真实工作空间中运行时，现有“技能”（skill）抽象存在的局限性问题，提出了一种新的形式化技能（Formal Skill）方案。研究背景是LLM代理正从对话式助手转向可执行复杂任务（如代码审查、命令运行、文件编辑）的实体，而技能和工具是代理执行动作的“手脚”。现有方法主要分为两类：一是非正式的、基于自然语言文档的技能（如Markdown技能、指令包），其执行逻辑依赖模型对冗长文本的理解，导致Token消耗大、指令模糊、约束松散且恢复状态隐式；二是功能调用、MCP服务器等工具级抽象，虽结构化单个动作，但缺乏对多步工作流的状态、策略和完成规范的表示。这些“非正式技能”的核心不足是其操作语义主要存在于自然语言或外部编排中，而非运行时可直接执行的对象，造成昂贵、模糊、脆弱等问题。本文旨在解决此问题，提出将可复用的代理能力从纯自然语言制品转化为运行时原生、可执行的结构化对象——形式化技能，让运行时拥有程序化不变性（如状态机、钩子策略），从而实现Token高效、可强制执行的代理控制。

### Q2: 有哪些相关研究？

Prompt-based agent skills（如 Anthropic 的 Agent Skills、Claude Code）使用 Markdown 和指令文件编码流程，但过程仍以自然语言文本形式存在，消耗大量 token 且依赖模型解读。Formal Skill 将可复用过程抽象为 JSON 元数据、动作模式、Python 执行器和生命周期钩子，从而消除冗余文本，提升 token 效率和确定性。

在工具使用方面，MRKL、ReAct、Toolformer、Gorilla、API-Bank 和 ToolLLM/ToolBench 等方法定义了结构化动作接口，但只关注单个动作的类型化，而未涉及工作流状态、策略约束和完成机制。OpenAI 函数调用、MCP 协议、LangChain 等生产系统同样仅提供工具调用，缺乏对阶段顺序、恢复状态和副作用策略的内置支持。Formal Skill 通过路由、钩子、技能本地状态和门控机制，将工具集组织为可强制执行的规程。

在 Agent 与编码运行时方面，Reflexion、Self-Refine、Voyager 等研究关注反馈与可复用的可执行技能，SWE-agent 和 AutoCodeRover 则聚焦于代理-计算机接口的设计。Claude Code、Codex CLI、OpenClaw、Hermes Agent 等工程系统提供了工作空间、shell/文件操作、沙箱策略、MCP 集成等功能，但技能仍以工具或文本形式存在。Formal Skill 将可复用过程提升为一等运行时对象，具备紧凑描述、可执行策略、生命周期控制和可观测状态，从而在 Harness-Bench 上以更少 token 取得高竞争力分数，尤其在需要显式技能控制的复杂任务中表现突出。

### Q3: 论文如何解决这个问题？

论文通过提出**Formal Skill**抽象来解决提示技能（prompt skills）在执行效率和控制力上的缺陷。Formal Skill将可复用的能力定义为一种运行时契约，核心设计包含三个层面：

1. **结构化技能接口**：用JSON元数据定义工具和动作schema，用Python执行器实现逻辑，将冗长的自然语言过程知识转化为紧凑的运行时对象。模型仅看到简短的接口描述，减少每次调用消耗的token。

2. **可执行强制约束**：通过钩子（hooks）在运行时强制执行策略。例如，在工具调用前检查参数合法性，在LLM决策后阻止未经验证的完成。约束成为动作语义的一部分，而非模型需要遵循的软性指令。

3. **技能本地运行时状态**：存储阶段（phase）、验证状态、产物清单等显式状态，让恢复和完成决策可编程。状态驱动钩子决定可见工具、策略检查及流程推进。

整体框架FairyClaw实现为事件驱动运行时，包含**技能路由**（将领域技能隔离到子会话，减少无关工具描述）、**单步推理循环**（每一步后更新状态并判断是否继续）以及**父-子会话协作**。以代码修复技能CodeRepairOps为例，它将修复过程分解为收集证据、应用补丁、验证、写报告四个结构化动作，通过钩子在每个阶段自动过滤工具、注入阶段性指导、拒绝非法操作，并保持会话开放直至通过验证门控。创新点在于将可复用过程从提示文本中抽离，变为可执行的状态机和可强制策略的钩子系统，实现token高效与精准控制。

### Q4: 论文做了哪些实验？

论文在Harness-Bench基准测试上进行了实验，包含75个真实工作台任务。实验设置了独立沙箱环境，通过代理适配器启动不同智能体，并记录每个模型请求和响应以计算令牌使用量。评分结合了任务可执行结果、过程评估和安全性检查，输出综合分数、总令牌数和每任务平均令牌数。对比方法包括Moltis、NullClaw、ZeroClaw、Hermes和OpenClaw，使用了gpt-5.4和gemini-3.1-pro两种模型家族。

主要结果：在gpt-5.4上，FairyClaw达到最高综合分数0.746，同时使用最少总令牌数3.51M（每任务46.8K），明显优于Moltis（0.744，6.29M）和Hermes（0.740，7.28M）。在gemini-3.1-pro上，FairyClaw综合分数0.635并非最高，但仍具竞争力，且令牌效率最优（3.84M对比其他方法的4.86M-12.70M）。在代表性代码调试任务中，FairyClaw在gpt-5.4和gemini-3.1-pro上分别获得最高综合分数0.865和0.843，令牌消耗远低于对比方法（如Hermes在gpt-5.4上需750.5K令牌）。结论表明，Formal Skill通过路由机制、阶段指导和窄工具暴露显著提升了令牌效率，同时在程序性任务中保持或提升了表现。

### Q5: 有什么可以进一步探索的点？

该论文提出的Formal Skill将技能从冗长的自然语言提示转化为可编程运行时协议，显著提升了token效率和可执行性，但仍存在进一步探索空间。首先，当前FairyClaw主要基于预定义的钩子和状态机规则，未来可以结合在线学习机制，允许技能在执行过程中根据反馈动态调整钩子逻辑或创建新的路由规则，使技能具备自适应性。其次，论文主要关注技能本身的运行时管理，但对跨技能协作与组合的复杂编排支持有限，可以研究形式化技能间的依赖关系和同步原语，实现更灵活的工作流组合。此外，当前形式化技能的定义依赖于人工设计的JSON模式和Python执行器，未来可探索利用LLM自动从自然语言描述或演示轨迹中生成和验证Formal Skill，降低技能构建门槛。最后，可以研究在联邦或分布式场景下Formal Skill的安全执行与状态隔离，确保多Agent系统中技能的可信运行。

### Q6: 总结一下论文的主要内容

这篇论文提出了Formal Skill，旨在解决现有LLM智能体技能（如Markdown技能、函数调用、MCP等）存在的非正式、高令牌消耗和缺乏运行时控制的问题。Formal Skill将可重用的智能体能力从纯自然语言文档转化为运行时原生、可编程的对象，包含JSON元数据、动作模式、可靠的Python执行器、钩子驱动的控制逻辑、路由元数据和技能本地状态。作者实现了开源事件驱动运行时FairyClaw来执行Formal Skill。在Harness-Bench基准上，FairyClaw在取得有竞争力平均分（排名第三，在gpt-5.4组中第一）的同时，每个任务平均仅消耗49.0K令牌，比其余五个框架的平均值低约48%，在体现Formal Skill特性的任务上表现尤为突出。核心结论是：智能体技能应作为令牌高效、运行时管控的协议，而非仅依赖自然语言文档。
