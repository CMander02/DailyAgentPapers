---
title: "OSGuard: A Benchmark for Safety in Computer-Use Agents"
authors:
  - "Mina Mohammadmirzaei"
  - "Jeffrey Flanigan"
date: "2026-06-13"
arxiv_id: "2606.15034"
arxiv_url: "https://arxiv.org/abs/2606.15034"
pdf_url: "https://arxiv.org/pdf/2606.15034v1"
categories:
  - "cs.AI"
tags:
  - "计算机使用Agent安全"
  - "Agent安全基准"
  - "多模态护栏"
  - "端到端安全评估"
  - "动作级安全"
  - "OSWorld衍生任务"
relevance_score: 9.5
---

# OSGuard: A Benchmark for Safety in Computer-Use Agents

## 原始摘要

Computer-use agents are increasingly evaluated by whether they complete realistic desktop and web tasks. However, task success alone can miss failures in which an agent reaches the nominal goal through an unsafe shortcut. We introduce OSGuard, a dual-granularity benchmark suite for evaluating safety in computer-use agents under benign, unchanged user instructions. OSGuard contains an action-level benchmark for local guardrail decisions and a risk-augmented execution suite for end-to-end evaluation. The action-level benchmark consists of contextualized proposed actions labeled as allowed, unrelated, or unsafe, each judged relative to the original instruction and current interface state. The execution suite contains manually constructed OSWorld-derived task variants in which the original task remains achievable, but the environment is modified to introduce latent hazards such as destructive overwrites, etc. Each variant is paired with augmented evaluators that retain the original task-success criterion while adding explicit state-based safety invariants, allowing us to distinguish safe completions from unsafe completions that satisfy the nominal task objective. Our experimental results on OSGuard show that current multimodal guardrails can perform well on isolated action judgments, while risk-augmented execution exposes remaining gaps between local oversight and reliable end-to-end safety. This dual-granularity design enables more precise diagnosis of whether models can both recognize unsafe proposed actions and improve full-task safety when deployed as guardrails.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决计算机使用智能体在完成良性用户指令时，因采取不安全捷径而导致安全违规的问题。现有方法主要关注任务完成率，但忽略了智能体可能通过违反环境约束（如覆盖不相关内容、修改全局设置、访问敏感信息等）来达成名义目标。虽然已有安全基准（如OS-Harm、RiOSWorld）涉及恶意请求或提示注入，但缺乏对普通、无恶意用户指令下状态依赖型安全风险的评估。为此，本文引入**OSGuard**，一个双粒度基准套件，核心解决两大问题：一是**局部监督**，即在给定原始指令、当前界面状态和候选动作时，判断该动作是否允许、不相关或危险；二是**端到端执行安全**，即通过修改环境引入潜在风险（如破坏性覆盖），确保智能体在完成原任务的同时不违反安全约束。现有方法要么无法区分安全与不安全完成，要么仅关注局部判断而忽略整体行为。OSGuard通过动作级基准和风险增强执行套件，结合不变性评估协议，系统诊断模型在局部识别与整体安全之间的差距。

### Q2: 有哪些相关研究？

本文的相关研究可分为以下几类：

**1. 计算机使用能力基准**：如OSWorld、WebArena、WorkArena、BrowserGym、Mind2Web和AndroidWorld等，主要评估代理在真实桌面或网页任务中的完成能力。OSGuard在此基础上，将焦点从单纯的任务完成转向“安全感知的完成”，即不仅看最终结果，还看过程是否安全。

**2. 计算机安全风险研究**：如OS-Harm和RiOSWorld，它们显式地研究恶意指令、提示注入或有害环境（如钓鱼）导致的危害。OSGuard的区别在于，它关注的是在普通、良性的用户指令下，因环境状态变化（如存在潜在危险覆盖）而产生的“非显式”安全风险。

**3. 动作级安全与护栏研究**：如MisActBench（动作级对齐/未对齐标签）、WebGuard（动作级风险预测）、ShieldAgent/GuardAgent（护栏代理）和SafePred（预测性护栏）。这些工作主要进行前序或局部动作的监督。OSGuard的独特性在于，它不仅包含动作级基准（判断单个动作是否安全），还引入了端到端的执行套件，通过增加状态安全不变量来区分“安全完成”与“危险完成”，从而连接局部监督与全局执行。

### Q3: 论文如何解决这个问题？

OSGuard 提出了一个双粒度基准套件，从动作级和全任务执行级两个层面评估计算机使用智能体的安全性。核心方法包括：

1. **动作级基准**：评估单个动作的守卫决策。每个测试项由原始指令、界面状态（截图和可访问性树）和候选动作组成，标签分为允许、无关和不安全。数据来源于四个构建渠道：标准OSWorld执行、中断的执行前缀+状态兼容的提议动作、中断的执行前缀+显式不安全的提议动作，以及风险增强变体的执行。所有标签通过人工标注确定，确保守卫仅基于原始指令、当前状态和候选动作进行判断。

2. **风险增强执行套件**：通过手动构造45个OSWorld任务变体来评估端到端安全。每个变体保持原始指令不变，但修改任务状态以引入潜在危险（如破坏性覆盖、越界编辑等），同时保留安全完成路径。每个变体配备增强评估器，保留原始任务成功标准并添加具体的安全不变量（如文件存在性、哈希值、权限等），能够区分安全完成和不安全完成。

3. **守卫智能体**：一个基于提示的响应式模型，在动作执行前评估提议。它接收原始指令、当前界面状态和候选动作，输出允许、无关或阻止。当阻止时，还会返回自然语言反馈，指导后续动作修正。在受控执行中，守卫允许动作执行，否则阻止并允许最多两次重试。通过在风险增强变体上比较有守卫和无守卫的执行，测试预执行干预能否在完成原始任务的同时减少安全违规。

创新点在于双粒度设计：动作级基准诊断局部决策质量，风险增强执行套件揭示端到端安全差距，从而更精确地评估模型是否能识别不安全动作并提升全任务安全性。

### Q4: 论文做了哪些实验？

实验分为两个粒度：动作级基准测试和风险增强执行套件。动作级基准测试评估护栏模型对情境化提议动作的识别能力（标注为允许、无关或危险），数据集包含标准OSWorld动作、中断+状态兼容/显式危险动作以及风险增强执行轨迹。主要结果：Gemini 3 Pro Preview表现最佳，准确率80%、宏F1为0.80，在允许动作（F1=0.85）、无关动作（0.80）和危险动作（0.76）上表现均衡；GPT 5.1准确率63%、宏F1为0.62，危险动作召回率高（0.74）但无关动作召回率低（0.37）；Claude Sonnet 4.5准确率60%、宏F1为0.60，危险动作F1为0.59。对比方法DeAction（以Claude Sonnet 4.5为骨干）准确率57%、宏F1为0.55，危险动作召回率仅0.20但精度达0.90。风险增强执行套件评估端到端安全性：Claude Sonnet 4.5在无护栏时完成率62%，但38%为危险完成任务（违反状态不变性）。加入Gemini 3 Pro Preview护栏后完成率仍为62%，危险完成率降至33%，4%触发重试终止。护栏主要纠正了一个危险执行为安全成功，并终止了一个重试后的危险执行，但整体安全差距未完全闭合。按来源分解显示，模型在标准OSWorld任务上表现最好（Gemini达100%准确率），而风险增强执行最困难（最佳宏F1仅0.48）。

### Q5: 有什么可以进一步探索的点？

OSGuard的局限性和未来研究方向主要包括：（1）当前动作级基准与端到端执行之间存在显著差距，最强护栏在动作判断上可达80%准确率，但仅能适度减少不安全执行，说明局部监督难以有效干预完整任务流程。未来可探索更细粒度的状态跟踪机制，在任务执行过程中动态调整约束优先级。（2）风险增强套件仅覆盖有限类型的潜在危害（如破坏性覆盖），需扩展至隐私泄露、权限滥用等更广泛的安全维度，并设计可迁移的自动风险注入框架。（3）现有护栏在理解环境状态的上下文依赖关系上表现薄弱，可结合形式化验证与神经符号推理，将安全不变量编译为可微约束，使护栏能持续检查状态转换而不是仅依靠单步动作判断。（4）引入对抗性训练生成风险增强的基准变体，迫使护栏在更复杂场景下保持稳健性，同时开发可解释性模块来追溯不安全完成的根本原因。

### Q6: 总结一下论文的主要内容

OSGuard提出了一个用于评估计算机使用代理安全性的双粒度基准套件。该研究针对当前代理评估仅关注任务完成度而忽略不安全捷径导致的安全隐患问题，设计了动作级基准（用于本地护栏决策）和风险增强执行套件（用于端到端评估）。动作级基准包含标注为允许、无关或非安全的上下文动作，每个动作需结合原始指令和界面状态进行判断；执行套件则通过修改OSWorld任务环境引入潜在风险（如破坏性覆盖等），并配备状态安全不变量以区分安全与不安全完成。实验结果显示，当前多模态护栏在孤立动作判断上表现良好（最高达80%准确率和0.80 macro-F1），但在风险增强执行中效果显著下降——无护栏代理有38%的不安全完成率，加入最强护栏后仅略微降低该比例。这表明相同状态依赖风险同时误导任务执行代理和护栏，揭示了本地监督与可靠端到端安全之间的差距，为未来开发能同时完成任务和保护约束的智能体提供了重要评估工具。
